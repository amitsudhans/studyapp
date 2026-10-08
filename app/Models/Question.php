<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;
use Illuminate\Database\Eloquent\Relations\HasMany;

#[Fillable(['name', 'description', 'standard_id', 'type', 'created_by', 'marks', 'status'])]
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
}
