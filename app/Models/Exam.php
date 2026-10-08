<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;
use Illuminate\Database\Eloquent\Relations\HasMany;

class Exam extends Model
{
    use HasFactory;

    protected $fillable = [
        'name',
        'created_by',
        'type',
        'duration',
        'status',
        'total_mark',
    ];

    protected $casts = [
        'type' => 'integer',
        'duration' => 'integer',
        'status' => 'integer',
        'total_mark' => 'integer',
    ];

    /**
     * Get the user who created the exam.
     */
    public function creator(): BelongsTo
    {
        return $this->belongsTo(User::class, 'created_by');
    }

    /**
     * Get the questions linked to this exam.
     */
    public function questions(): BelongsToMany
    {
        return $this->belongsToMany(Question::class, 'exam_questions')
            ->withPivot('id', 'status')
            ->withTimestamps();
    }

    /**
     * Get the standards assigned to this exam via exam_assign table.
     */
    public function standards(): BelongsToMany
    {
        return $this->belongsToMany(Standard::class, 'exam_assign')
            ->withPivot('id', 'status')
            ->withTimestamps();
    }

    /**
     * Get the pivot exam questions entries.
     */
    public function examQuestions()
    {
        return $this->hasMany(ExamQuestion::class);
    }

    /**
     * Get the student exam submission details for this exam.
     */
    public function studentExamDetails(): HasMany
    {
        return $this->hasMany(StudentExamDetail::class);
    }

    /**
     * Recalculate and update the total mark for this exam based on attached questions.
     */
    public function recalculateTotalMarks(): void
    {
        $totalMarks = (int) $this->questions()->sum('marks');
        $this->update(['total_mark' => $totalMarks]);
    }
}
