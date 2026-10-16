<?php

namespace App\Models;

use Database\Factories\StudentExamDetailFactory;
use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

#[Fillable(['student_id', 'exam_id', 'question_id', 'student_written_ans_id', 'match_answers', 'student_text_answer', 'teacher_marks', 'teacher_feedback'])]
class StudentExamDetail extends Model
{
    /** @use HasFactory<StudentExamDetailFactory> */
    use HasFactory;

    /**
     * Get the attributes that should be cast.
     *
     * @return array<string, string>
     */
    protected function casts(): array
    {
        return [
            'match_answers' => 'array',
            'teacher_marks' => 'integer',
        ];
    }

    /**
     * Get the student associated with the detail record.
     *
     * @return BelongsTo<Student, $this>
     */
    public function student(): BelongsTo
    {
        return $this->belongsTo(Student::class);
    }

    /**
     * Get the exam associated with the detail record.
     *
     * @return BelongsTo<Exam, $this>
     */
    public function exam(): BelongsTo
    {
        return $this->belongsTo(Exam::class);
    }

    /**
     * Get the question associated with the detail record.
     *
     * @return BelongsTo<Question, $this>
     */
    public function question(): BelongsTo
    {
        return $this->belongsTo(Question::class);
    }

    /**
     * Get the student written answer option associated with the detail record.
     *
     * @return BelongsTo<Answer, $this>
     */
    public function writtenAnswer(): BelongsTo
    {
        return $this->belongsTo(Answer::class, 'student_written_ans_id');
    }

    /**
     * Get count of correctly matched pairs for Match the Following questions.
     */
    public function getCorrectMatchCount(): int
    {
        if ($this->question?->type !== 5) {
            return 0;
        }

        $answers = $this->question->answers;
        if ($answers->isEmpty()) {
            return 0;
        }

        $matches = is_array($this->match_answers)
            ? $this->match_answers
            : json_decode($this->match_answers ?? '[]', true);

        if (empty($matches) || ! is_array($matches)) {
            return 0;
        }

        $correctCount = 0;
        foreach ($answers as $ans) {
            $submitted = $matches[$ans->id] ?? $matches[(string) $ans->id] ?? null;
            if ($submitted !== null && trim(strtolower((string) $submitted)) === trim(strtolower((string) $ans->match_answer))) {
                $correctCount++;
            }
        }

        return $correctCount;
    }

    /**
     * Determine if this question is a Text Entry question.
     */
    public function isTextEntry(): bool
    {
        return (int) ($this->question?->type ?? 0) === 3;
    }

    /**
     * Determine if this Text Entry question has been evaluated by the teacher.
     */
    public function isEvaluated(): bool
    {
        return $this->teacher_marks !== null;
    }

    /**
     * Get the earned marks for this student response.
     * For Match the Following: 1 mark for each correctly matched pair.
     * For Text Entry: manually awarded teacher_marks (or 0 if pending evaluation).
     * For standard questions: question marks if correct, 0 if wrong.
     */
    public function getEarnedMarks(): int
    {
        if ((int) $this->question?->type === 5) {
            return $this->getCorrectMatchCount();
        }

        if ((int) $this->question?->type === 3) {
            return $this->teacher_marks !== null ? (int) $this->teacher_marks : 0;
        }

        return $this->isCorrect() ? (int) ($this->question?->marks ?? 0) : 0;
    }

    /**
     * Get the total possible marks for this question.
     */
    public function getQuestionMarks(): int
    {
        if ($this->question?->type === 5) {
            $answersCount = $this->question->answers->count();

            return $answersCount > 0 ? $answersCount : (int) ($this->question?->marks ?? 0);
        }

        return (int) ($this->question?->marks ?? 0);
    }

    /**
     * Determine if this question response is 100% correct.
     * For Text Entry: full marks awarded by teacher.
     */
    public function isCorrect(): bool
    {
        if ((int) $this->question?->type === 3) {
            $qMarks = (int) ($this->question?->marks ?? 0);

            return $this->teacher_marks !== null && $qMarks > 0 && (int) $this->teacher_marks >= $qMarks;
        }

        if ($this->question?->type === 5) {
            $answers = $this->question->answers;
            if ($answers->isEmpty()) {
                return false;
            }

            return $this->getCorrectMatchCount() === $answers->count();
        }

        return $this->writtenAnswer && ((int) $this->writtenAnswer->is_correct === 1);
    }

    /**
     * Determine if this question response is partially correct.
     */
    public function isPartiallyCorrect(): bool
    {
        if ((int) $this->question?->type === 3) {
            $qMarks = (int) ($this->question?->marks ?? 0);

            return $this->teacher_marks !== null && (int) $this->teacher_marks > 0 && (int) $this->teacher_marks < $qMarks;
        }

        if ($this->question?->type !== 5) {
            return false;
        }

        $correctCount = $this->getCorrectMatchCount();
        $totalCount = $this->question->answers->count();

        return $correctCount > 0 && $correctCount < $totalCount;
    }

    /**
     * Accessor for is_correct property.
     */
    public function getIsCorrectAttribute(): bool
    {
        return $this->isCorrect();
    }

    /**
     * Get human-readable summary of student's selected answer(s).
     */
    public function getSelectedAnswerDisplay(): string
    {
        if ((int) $this->question?->type === 3) {
            return ! empty($this->student_text_answer) ? $this->student_text_answer : 'No Text Answer Submitted';
        }

        if ($this->question?->type === 5) {
            $answers = $this->question->answers;
            $matches = is_array($this->match_answers)
                ? $this->match_answers
                : json_decode($this->match_answers ?? '[]', true);

            if (empty($matches) || ! is_array($matches)) {
                return 'No Matches Selected';
            }

            $parts = [];
            foreach ($answers as $idx => $ans) {
                $letter = chr(65 + $idx);
                $submitted = $matches[$ans->id] ?? $matches[(string) $ans->id] ?? 'None';
                $parts[] = "{$letter}. {$ans->name} → {$submitted}";
            }

            return implode(' | ', $parts);
        }

        return $this->writtenAnswer?->name ?? 'No Answer Selected';
    }

    /**
     * Get human-readable summary of correct answer(s).
     */
    public function getCorrectAnswerDisplay(): ?string
    {
        if ((int) $this->question?->type === 3) {
            return $this->question?->solution ?? 'Subjective Text Answer (No Auto-Answer)';
        }

        if ($this->question?->type === 5) {
            $answers = $this->question->answers;
            if ($answers->isEmpty()) {
                return null;
            }

            $parts = [];
            foreach ($answers as $idx => $ans) {
                $letter = chr(65 + $idx);
                $parts[] = "{$letter}. {$ans->name} → {$ans->match_answer}";
            }

            return implode(' | ', $parts);
        }

        return $this->question?->answers?->firstWhere('is_correct', 1)?->name;
    }

    /**
     * Detailed pair review for Match the Following questions.
     *
     * @return array<int, array{letter: string, left: string, student_match: string, correct_match: ?string, is_correct: bool}>
     */
    public function getMatchPairsReview(): array
    {
        if ($this->question?->type !== 5) {
            return [];
        }

        $answers = $this->question->answers;
        $matches = is_array($this->match_answers)
            ? $this->match_answers
            : json_decode($this->match_answers ?? '[]', true);

        $review = [];
        foreach ($answers as $idx => $ans) {
            $submitted = $matches[$ans->id] ?? $matches[(string) $ans->id] ?? null;
            $isPairCorrect = $submitted !== null && trim(strtolower((string) $submitted)) === trim(strtolower((string) $ans->match_answer));

            $review[] = [
                'letter' => chr(65 + $idx),
                'left' => $ans->name,
                'student_match' => $submitted ?? 'Not Answered',
                'correct_match' => $ans->match_answer,
                'is_correct' => $isPairCorrect,
                'earned_marks' => $isPairCorrect ? 1 : 0,
            ];
        }

        return $review;
    }
}
