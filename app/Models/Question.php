<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;
use Illuminate\Database\Eloquent\Relations\HasMany;

#[Fillable(['name', 'description', 'hint', 'solution', 'standard_id', 'subject_id', 'chapter_id', 'topic_id', 'type', 'created_by', 'marks', 'status'])]
class Question extends Model
{
    use HasFactory;

    /**
     * Get the standard associated with the question.
     *
     * @return BelongsTo<Standard, $this>
     */
    public function standard(): BelongsTo
    {
        return $this->belongsTo(Standard::class);
    }

    /**
     * Get the subject associated with the question.
     *
     * @return BelongsTo<Subject, $this>
     */
    public function subject(): BelongsTo
    {
        return $this->belongsTo(Subject::class);
    }

    /**
     * Get the chapter associated with the question.
     *
     * @return BelongsTo<Chapter, $this>
     */
    public function chapter(): BelongsTo
    {
        return $this->belongsTo(Chapter::class);
    }

    /**
     * Get the topic associated with the question.
     *
     * @return BelongsTo<Topic, $this>
     */
    public function topic(): BelongsTo
    {
        return $this->belongsTo(Topic::class);
    }

    /**
     * Get the user who created the question.
     *
     * @return BelongsTo<User, $this>
     */
    public function creator(): BelongsTo
    {
        return $this->belongsTo(User::class, 'created_by');
    }

    /**
     * Get the answers for the question.
     *
     * @return HasMany<Answer, $this>
     */
    public function answers(): HasMany
    {
        return $this->hasMany(Answer::class);
    }

    /**
     * Get the exams associated with this question.
     *
     * @return BelongsToMany<Exam, $this>
     */
    public function exams(): BelongsToMany
    {
        return $this->belongsToMany(Exam::class, 'exam_questions')
            ->withPivot('id', 'status')
            ->withTimestamps();
    }

    /**
     * Get the attributes that should be cast.
     *
     * @return array<string, string>
     */
    protected function casts(): array
    {
        return [
            'type' => 'integer',
            'marks' => 'integer',
            'status' => 'integer',
        ];
    }

    public const TYPE_SINGLE_OPTION = 1;

    public const TYPE_MULTIPLE_OPTION = 2;

    public const TYPE_TEXT_ENTRY = 3;

    public const TYPE_TRUE_FALSE = 4;

    public const TYPE_MATCH_THE_FOLLOWING = 5;

    /**
     * Determine if the question is Text Entry.
     */
    public function isTextEntry(): bool
    {
        return (int) $this->type === self::TYPE_TEXT_ENTRY;
    }

    /**
     * Determine if the question is True / False.
     */
    public function isTrueFalse(): bool
    {
        return (int) $this->type === self::TYPE_TRUE_FALSE;
    }

    /**
     * Determine if the question is Match the Following.
     */
    public function isMatch(): bool
    {
        return (int) $this->type === self::TYPE_MATCH_THE_FOLLOWING;
    }

    /**
     * Get human-readable question type name.
     */
    public function getTypeNameAttribute(): string
    {
        return match ((int) $this->type) {
            self::TYPE_SINGLE_OPTION => 'Single Option',
            self::TYPE_MULTIPLE_OPTION => 'Multiple Option',
            self::TYPE_TEXT_ENTRY => 'Text Entry',
            self::TYPE_TRUE_FALSE => 'True / False',
            self::TYPE_MATCH_THE_FOLLOWING => 'Match the Following',
            default => 'Unknown',
        };
    }
}
