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
        'syllabus_id',
        'standard_id',
        'subject_id',
        'chapter_id',
        'topic_id',
        'total_mark',
    ];

    protected $casts = [
        'type' => 'integer',
        'duration' => 'integer',
        'status' => 'integer',
        'syllabus_id' => 'integer',
        'standard_id' => 'integer',
        'subject_id' => 'integer',
        'chapter_id' => 'integer',
        'topic_id' => 'integer',
        'total_mark' => 'integer',
    ];

    /**
     * Get the syllabus associated with the exam.
     */
    public function syllabus(): BelongsTo
    {
        return $this->belongsTo(Syllabus::class);
    }

    /**
     * Get the primary class / standard associated with the exam.
     */
    public function standard(): BelongsTo
    {
        return $this->belongsTo(Standard::class);
    }

    /**
     * Get the subject associated with the exam.
     */
    public function subject(): BelongsTo
    {
        return $this->belongsTo(Subject::class);
    }

    /**
     * Get the chapter associated with the exam.
     */
    public function chapter(): BelongsTo
    {
        return $this->belongsTo(Chapter::class);
    }

    /**
     * Get the topic associated with the exam.
     */
    public function topic(): BelongsTo
    {
        return $this->belongsTo(Topic::class);
    }

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

    public const TYPE_TIMED = 1;

    public const TYPE_NON_TIMED = 2;

    public const TYPE_TEXT_ENTRY = 3;

    /**
     * Determine if exam is timed.
     */
    public function isTimed(): bool
    {
        return (int) $this->type === self::TYPE_TIMED;
    }

    /**
     * Determine if exam is non-timed.
     */
    public function isNonTimed(): bool
    {
        return (int) $this->type === self::TYPE_NON_TIMED;
    }

    /**
     * Determine if exam is text entry type.
     */
    public function isTextEntry(): bool
    {
        return (int) $this->type === self::TYPE_TEXT_ENTRY;
    }

    /**
     * Get human-readable exam type label.
     */
    public function getTypeNameAttribute(): string
    {
        return match ((int) $this->type) {
            self::TYPE_TIMED => 'Timed',
            self::TYPE_NON_TIMED => 'Non-Timed',
            self::TYPE_TEXT_ENTRY => 'Text Entry',
            default => 'Unknown',
        };
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
