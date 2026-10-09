<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;

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
}
