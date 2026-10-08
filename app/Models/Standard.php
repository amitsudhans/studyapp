<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;
use Illuminate\Database\Eloquent\Relations\HasMany;

#[Fillable(['name', 'syllabus_id', 'created_by'])]
class Standard extends Model
{
    use HasFactory;

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
     * Get the students belonging to this standard.
     *
     * @return HasMany<Student, $this>
     */
    public function students(): HasMany
    {
        return $this->hasMany(Student::class);
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
}
