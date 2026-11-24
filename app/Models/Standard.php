<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;
use Illuminate\Database\Eloquent\Relations\HasMany;
use Illuminate\Support\Facades\DB;

#[Fillable(['name', 'syllabus_id', 'created_by'])]
class Standard extends Model
{
    use HasFactory;

    /**
     * Get the attributes that should be cast.
     *
     * @return array<string, string>
     */
    protected function casts(): array
    {
        return [
            'created_by' => 'integer',
            'syllabus_id' => 'integer',
        ];
    }

    /**
     * Scope a query to only include standards accessible to the given user.
     *
     * @param  Builder<Standard>  $query
     * @return Builder<Standard>
     */
    public function scopeAccessibleTo(Builder $query, User $user): Builder
    {
        if ($user->isAdmin()) {
            return $query;
        }

        return $query->where(function (Builder $q) use ($user) {
            $q->where('created_by', $user->id)
                ->orWhereHas('teachers', function (Builder $tq) use ($user) {
                    $tq->where('users.id', $user->id);
                });
        });
    }

    /**
     * Check if this standard was created by an admin or is a system standard.
     */
    public function isAdminCreated(): bool
    {
        if (is_null($this->created_by)) {
            return true;
        }

        $creator = $this->creator;
        if (! $creator) {
            return true;
        }

        return $creator->isAdmin();
    }

    /**
     * Scope a query to only include standards created by admins or system standards.
     *
     * @param  Builder<Standard>  $query
     * @return Builder<Standard>
     */
    public function scopeAdminCreated(Builder $query): Builder
    {
        return $query->where(function (Builder $q) {
            $q->whereNull('standards.created_by')
                ->orWhereHas('creator', function (Builder $cq) {
                    $cq->where('email', 'admin@example.com')
                        ->orWhereHas('profile', function (Builder $pq) {
                            $pq->whereIn('type', [0, 3, 99])
                                ->orWhere('designation', 'Administrator');
                        });
                });
        });
    }

    /**
     * Remove student(s) from custom groups when they are moved or unassigned from admin-created standard(s).
     *
     * @param  array<int>|int  $studentIds
     * @param  array<int>|int  $removedAdminStandardIds
     */
    public static function removeStudentsFromRelatedCustomGroups(array|int $studentIds, array|int $removedAdminStandardIds = []): void
    {
        $studentIds = array_filter(array_map('intval', (array) $studentIds));
        $removedAdminStandardIds = array_filter(array_map('intval', (array) $removedAdminStandardIds));

        if (empty($studentIds)) {
            return;
        }

        // 1. Find teachers assigned to the removed admin standard(s)
        if (! empty($removedAdminStandardIds)) {
            $teacherIds = DB::table('teacher_standards')
                ->whereIn('standard_id', $removedAdminStandardIds)
                ->pluck('user_id')
                ->toArray();

            // 2. Find all custom groups created by these teachers and remove the student(s)
            if (! empty($teacherIds)) {
                $customGroupIds = static::whereIn('created_by', $teacherIds)
                    ->whereNotNull('created_by')
                    ->pluck('id')
                    ->toArray();

                if (! empty($customGroupIds)) {
                    DB::table('student_standards')
                        ->whereIn('student_id', $studentIds)
                        ->whereIn('standard_id', $customGroupIds)
                        ->delete();
                }
            }
        }

        // 3. Clean up any custom groups where the creator is not assigned to the student's current admin standard
        foreach ($studentIds as $sId) {
            $studentUser = User::find($sId);
            if (! $studentUser) {
                continue;
            }

            $currentAdminStd = $studentUser->adminCreatedStandard();
            if (! $currentAdminStd) {
                // No admin standard -> cannot be in any teacher custom group
                $adminStdIds = static::adminCreated()->pluck('standards.id')->toArray();
                DB::table('student_standards')
                    ->where('student_id', $sId)
                    ->whereNotIn('standard_id', $adminStdIds)
                    ->delete();
            } else {
                // Has admin standard -> can only be in custom groups of teachers who teach this admin standard
                $authorizedTeacherIds = DB::table('teacher_standards')
                    ->where('standard_id', $currentAdminStd->id)
                    ->pluck('user_id')
                    ->toArray();

                $ineligibleCustomStandards = DB::table('student_standards')
                    ->join('standards', 'student_standards.standard_id', '=', 'standards.id')
                    ->where('student_standards.student_id', $sId)
                    ->whereNotNull('standards.created_by')
                    ->whereNotIn('standards.created_by', $authorizedTeacherIds)
                    ->pluck('standards.id')
                    ->toArray();

                if (! empty($ineligibleCustomStandards)) {
                    DB::table('student_standards')
                        ->where('student_id', $sId)
                        ->whereIn('standard_id', $ineligibleCustomStandards)
                        ->delete();
                }
            }
        }
    }

    /**
     * Clean up any custom groups that contain students not enrolled in the creator's assigned admin standards.
     * Ensures custom groups never have orphaned/stale students or count discrepancies.
     */
    public static function cleanUpAllIneligibleCustomGroupEnrollments(): int
    {
        $customGroups = static::whereNotNull('standards.created_by')
            ->whereDoesntHave('creator.profile', fn ($pq) => $pq->whereIn('type', [0, 3, 99])->orWhere('designation', 'Administrator'))
            ->whereDoesntHave('creator', fn ($cq) => $cq->where('email', 'admin@example.com'))
            ->get();

        $deletedCount = 0;

        foreach ($customGroups as $cg) {
            $creator = $cg->creator;
            if (! $creator) {
                continue;
            }

            $creatorAdminStdIds = $creator->standards()
                ->adminCreated()
                ->pluck('standards.id')
                ->toArray();

            $enrolledStudentIds = DB::table('student_standards')
                ->where('standard_id', $cg->id)
                ->pluck('student_id')
                ->toArray();

            if (empty($enrolledStudentIds)) {
                continue;
            }

            if (empty($creatorAdminStdIds)) {
                $deletedCount += DB::table('student_standards')
                    ->where('standard_id', $cg->id)
                    ->delete();
            } else {
                $ineligibleStudentIds = User::whereIn('id', $enrolledStudentIds)
                    ->where(function ($q) use ($creatorAdminStdIds) {
                        $q->whereDoesntHave('studentStandards', fn ($st) => $st->whereIn('standards.id', $creatorAdminStdIds))
                            ->whereDoesntHave('student', fn ($st) => $st->whereIn('standard_id', $creatorAdminStdIds));
                    })
                    ->pluck('id')
                    ->toArray();

                if (! empty($ineligibleStudentIds)) {
                    $deletedCount += DB::table('student_standards')
                        ->where('standard_id', $cg->id)
                        ->whereIn('student_id', $ineligibleStudentIds)
                        ->delete();
                }
            }
        }

        return $deletedCount;
    }

    /**
     * Get the syllabus that owns the standard.
     *
     * @return BelongsTo<Syllabus, $this>
     */
    public function syllabus(): BelongsTo
    {
        return $this->belongsTo(Syllabus::class, 'syllabus_id');
    }

    /**
     * Get the user who created the standard.
     *
     * @return BelongsTo<User, $this>
     */
    public function creator(): BelongsTo
    {
        return $this->belongsTo(User::class, 'created_by');
    }

    /**
     * Get the teachers (users) assigned to this standard.
     *
     * @return BelongsToMany<User, $this>
     */
    public function teachers(): BelongsToMany
    {
        return $this->belongsToMany(User::class, 'teacher_standards');
    }

    /**
     * Get the students (users) belonging to this standard via student_standards table.
     *
     * @return BelongsToMany<User, $this>
     */
    public function students(): BelongsToMany
    {
        return $this->belongsToMany(User::class, 'student_standards', 'standard_id', 'student_id');
    }

    /**
     * Get the exams assigned to this standard via exam_assign table.
     *
     * @return BelongsToMany<Exam, $this>
     */
    public function assignedExams(): BelongsToMany
    {
        return $this->belongsToMany(Exam::class, 'exam_assign')
            ->withPivot('id', 'status')
            ->withTimestamps();
    }

    /**
     * Get the chapters belonging to this standard.
     *
     * @return HasMany<Chapter, $this>
     */
    public function chapters(): HasMany
    {
        return $this->hasMany(Chapter::class, 'standard_id');
    }
}
