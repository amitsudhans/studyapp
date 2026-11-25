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
     * Get count of correctly ordered puzzle pieces for Puzzle questions.
     * Evaluates index-by-index comparison of submitted sequence vs. correct sequence.
     */
    public function getCorrectPuzzleCount(): int
    {
        if ((int) ($this->question?->type ?? 0) !== 6) {
            return 0;
        }

        $answers = $this->question->answers->values();
        if ($answers->isEmpty()) {
            return 0;
        }

        $submittedList = is_array($this->match_answers)
            ? $this->match_answers
            : json_decode($this->match_answers ?? '[]', true);

        if (empty($submittedList) || ! is_array($submittedList)) {
            return 0;
        }

        // Standardize list to indexed array
        $submittedList = array_values($submittedList);

        $correctCount = 0;
        foreach ($answers as $index => $correctAnswer) {
            $submittedVal = $submittedList[$index] ?? null;
            if ($submittedVal !== null) {
                // Check either by answer ID or answer text
                if ((string) $submittedVal === (string) $correctAnswer->id || trim(strtolower((string) $submittedVal)) === trim(strtolower((string) $correctAnswer->name))) {
                    $correctCount++;
                }
            }
        }

        return $correctCount;
    }

    /**
     * Get count of correctly answered sub-questions for Case Study questions.
     */
    public function getCorrectCaseStudyCount(): int
    {
        if ((int) ($this->question?->type ?? 0) !== 9) {
            return 0;
        }

        $answers = $this->question->answers->values();
        if ($answers->isEmpty()) {
            return 0;
        }

        $submittedMatches = is_array($this->match_answers)
            ? $this->match_answers
            : json_decode($this->match_answers ?? '[]', true);

        if (empty($submittedMatches) || ! is_array($submittedMatches)) {
            return 0;
        }

        $correctCount = 0;
        foreach ($answers as $index => $correctAns) {
            $submitted = $submittedMatches[$correctAns->id]
                ?? $submittedMatches[(string) $correctAns->id]
                ?? $submittedMatches[$index]
                ?? $submittedMatches[(string) $index]
                ?? null;

            if ($submitted !== null && trim(mb_strtolower((string) $submitted)) === trim(mb_strtolower((string) $correctAns->name))) {
                $correctCount++;
            }
        }

        return $correctCount;
    }

    /**
     * Get count of correctly identified pins for Image Hotspot / Diagram questions.
     */
    public function getCorrectHotspotsCount(): int
    {
        if ((int) ($this->question?->type ?? 0) !== 8) {
            return 0;
        }

        $answers = $this->question->answers->values();
        if ($answers->isEmpty()) {
            return 0;
        }

        $submittedMatches = is_array($this->match_answers)
            ? $this->match_answers
            : json_decode($this->match_answers ?? '[]', true);

        if (empty($submittedMatches) || ! is_array($submittedMatches)) {
            return 0;
        }

        $correctCount = 0;
        foreach ($answers as $index => $correctAns) {
            $submitted = $submittedMatches[$correctAns->id]
                ?? $submittedMatches[(string) $correctAns->id]
                ?? $submittedMatches[$index]
                ?? $submittedMatches[(string) $index]
                ?? null;

            if ($submitted !== null && trim(mb_strtolower((string) $submitted)) === trim(mb_strtolower((string) $correctAns->name))) {
                $correctCount++;
            }
        }

        return $correctCount;
    }

    /**
     * Get count of correctly answered blanks for Fill in the Blanks questions.
     * Compares student's submitted text per blank index or answer ID against correct answers (case-insensitive & trimmed).
     */
    public function getCorrectBlanksCount(): int
    {
        if ((int) ($this->question?->type ?? 0) !== 7) {
            return 0;
        }

        $answers = $this->question->answers->values();
        if ($answers->isEmpty()) {
            return 0;
        }

        $submittedMatches = is_array($this->match_answers)
            ? $this->match_answers
            : json_decode($this->match_answers ?? '[]', true);

        if (empty($submittedMatches) || ! is_array($submittedMatches)) {
            return 0;
        }

        $correctCount = 0;
        foreach ($answers as $index => $correctAns) {
            // Student submitted answer can be keyed by answer ID or by zero-based index
            $submitted = $submittedMatches[$correctAns->id]
                ?? $submittedMatches[(string) $correctAns->id]
                ?? $submittedMatches[$index]
                ?? $submittedMatches[(string) $index]
                ?? null;

            if ($submitted !== null && trim(mb_strtolower((string) $submitted)) === trim(mb_strtolower((string) $correctAns->name))) {
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
     * Determine if this question is a Puzzle question.
     */
    public function isPuzzle(): bool
    {
        return (int) ($this->question?->type ?? 0) === 6;
    }

    /**
     * Determine if this question is a Fill in the Blanks question.
     */
    public function isFillInTheBlanks(): bool
    {
        return (int) ($this->question?->type ?? 0) === 7;
    }

    /**
     * Determine if this question is an Image Hotspot / Diagram Labeling question.
     */
    public function isImageLabeling(): bool
    {
        return (int) ($this->question?->type ?? 0) === 8;
    }

    /**
     * Determine if this question is a Case-Based / Source-Based question.
     */
    public function isCaseStudy(): bool
    {
        return (int) ($this->question?->type ?? 0) === 9;
    }

    /**
     * Determine if this question is an Assertion & Reason question.
     */
    public function isAssertionReason(): bool
    {
        return (int) ($this->question?->type ?? 0) === 10;
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
     * For Puzzle: 1 mark for each correctly ordered piece.
     * For Fill in the Blanks: 1 mark for each correctly answered blank.
     * For Text Entry: manually awarded teacher_marks (or 0 if pending evaluation).
     * For standard questions: question marks if correct, 0 if wrong.
     */
    public function getEarnedMarks(): int
    {
        if ((int) $this->question?->type === 5) {
            return $this->getCorrectMatchCount();
        }

        if ((int) $this->question?->type === 6) {
            return $this->getCorrectPuzzleCount();
        }

        if ((int) $this->question?->type === 7) {
            return $this->getCorrectBlanksCount();
        }

        if ((int) $this->question?->type === 8) {
            return $this->getCorrectHotspotsCount();
        }

        if ((int) $this->question?->type === 9) {
            return $this->getCorrectCaseStudyCount();
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
        if (in_array((int) ($this->question?->type ?? 0), [5, 6, 7, 8, 9])) {
            $answersCount = $this->question->answers->count();

            return $answersCount > 0 ? $answersCount : (int) ($this->question?->marks ?? 1);
        }

        return max(1, (int) ($this->question?->marks ?? 1));
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

        if ((int) $this->question?->type === 6) {
            $answers = $this->question->answers;
            if ($answers->isEmpty()) {
                return false;
            }

            return $this->getCorrectPuzzleCount() === $answers->count();
        }

        if ((int) $this->question?->type === 7) {
            $answers = $this->question->answers;
            if ($answers->isEmpty()) {
                return false;
            }

            return $this->getCorrectBlanksCount() === $answers->count();
        }

        if ((int) $this->question?->type === 8) {
            $answers = $this->question->answers;
            if ($answers->isEmpty()) {
                return false;
            }

            return $this->getCorrectHotspotsCount() === $answers->count();
        }

        if ((int) $this->question?->type === 9) {
            $answers = $this->question->answers;
            if ($answers->isEmpty()) {
                return false;
            }

            return $this->getCorrectCaseStudyCount() === $answers->count();
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

        if ($this->question?->type === 5) {
            $correctCount = $this->getCorrectMatchCount();
            $totalCount = $this->question->answers->count();

            return $correctCount > 0 && $correctCount < $totalCount;
        }

        if ((int) $this->question?->type === 6) {
            $correctCount = $this->getCorrectPuzzleCount();
            $totalCount = $this->question->answers->count();

            return $correctCount > 0 && $correctCount < $totalCount;
        }

        if ((int) $this->question?->type === 7) {
            $correctCount = $this->getCorrectBlanksCount();
            $totalCount = $this->question->answers->count();

            return $correctCount > 0 && $correctCount < $totalCount;
        }

        if ((int) $this->question?->type === 8) {
            $correctCount = $this->getCorrectHotspotsCount();
            $totalCount = $this->question->answers->count();

            return $correctCount > 0 && $correctCount < $totalCount;
        }

        if ((int) $this->question?->type === 9) {
            $correctCount = $this->getCorrectCaseStudyCount();
            $totalCount = $this->question->answers->count();

            return $correctCount > 0 && $correctCount < $totalCount;
        }

        return false;
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

        if ((int) $this->question?->type === 6) {
            $answers = $this->question->answers->keyBy('id');
            $submittedList = is_array($this->match_answers)
                ? $this->match_answers
                : json_decode($this->match_answers ?? '[]', true);

            if (empty($submittedList) || ! is_array($submittedList)) {
                return 'No Sequence Arranged';
            }

            $parts = [];
            $pos = 1;
            foreach ($submittedList as $val) {
                // If it's an answer ID, look up its text name; otherwise use string directly
                $name = $answers->get($val)?->name ?? (string) $val;
                $parts[] = "#{$pos} {$name}";
                $pos++;
            }

            return implode(' → ', $parts);
        }

        if ((int) $this->question?->type === 7) {
            $answers = $this->question->answers->values();
            $submittedMatches = is_array($this->match_answers)
                ? $this->match_answers
                : json_decode($this->match_answers ?? '[]', true);

            if (empty($submittedMatches) || ! is_array($submittedMatches)) {
                return 'No Blanks Answered';
            }

            $parts = [];
            foreach ($answers as $idx => $correctAns) {
                $submitted = $submittedMatches[$correctAns->id]
                    ?? $submittedMatches[(string) $correctAns->id]
                    ?? $submittedMatches[$idx]
                    ?? $submittedMatches[(string) $idx]
                    ?? '—';
                $parts[] = 'Blank #'.($idx + 1).': '.trim((string) $submitted);
            }

            return implode(' | ', $parts);
        }

        if ((int) $this->question?->type === 8) {
            $answers = $this->question->answers->values();
            $submittedMatches = is_array($this->match_answers)
                ? $this->match_answers
                : json_decode($this->match_answers ?? '[]', true);

            if (empty($submittedMatches) || ! is_array($submittedMatches)) {
                return 'No Labels Selected';
            }

            $parts = [];
            foreach ($answers as $idx => $correctAns) {
                $submitted = $submittedMatches[$correctAns->id]
                    ?? $submittedMatches[(string) $correctAns->id]
                    ?? $submittedMatches[$idx]
                    ?? $submittedMatches[(string) $idx]
                    ?? '—';
                $parts[] = 'Pin #'.($idx + 1).': '.trim((string) $submitted);
            }

            return implode(' | ', $parts);
        }

        if ((int) $this->question?->type === 9) {
            $answers = $this->question->answers->values();
            $submittedMatches = is_array($this->match_answers)
                ? $this->match_answers
                : json_decode($this->match_answers ?? '[]', true);

            if (empty($submittedMatches) || ! is_array($submittedMatches)) {
                return 'No Sub-Questions Answered';
            }

            $parts = [];
            foreach ($answers as $idx => $correctAns) {
                $submitted = $submittedMatches[$correctAns->id]
                    ?? $submittedMatches[(string) $correctAns->id]
                    ?? $submittedMatches[$idx]
                    ?? $submittedMatches[(string) $idx]
                    ?? '—';
                $parts[] = 'Q'.($idx + 1).': '.trim((string) $submitted);
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

        if ((int) $this->question?->type === 6) {
            $answers = $this->question->answers->values();
            if ($answers->isEmpty()) {
                return null;
            }

            $parts = [];
            foreach ($answers as $idx => $ans) {
                $pos = $idx + 1;
                $parts[] = "#{$pos} {$ans->name}";
            }

            return implode(' → ', $parts);
        }

        if ((int) $this->question?->type === 7) {
            $answers = $this->question->answers->values();
            if ($answers->isEmpty()) {
                return null;
            }

            $parts = [];
            foreach ($answers as $idx => $ans) {
                $pos = $idx + 1;
                $parts[] = "Blank #{$pos}: {$ans->name}";
            }

            return implode(' | ', $parts);
        }

        if ((int) $this->question?->type === 8) {
            $answers = $this->question->answers->values();
            if ($answers->isEmpty()) {
                return null;
            }

            $parts = [];
            foreach ($answers as $idx => $ans) {
                $pos = $idx + 1;
                $parts[] = "Pin #{$pos}: {$ans->name}";
            }

            return implode(' | ', $parts);
        }

        if ((int) $this->question?->type === 9) {
            $answers = $this->question->answers->values();
            if ($answers->isEmpty()) {
                return null;
            }

            $parts = [];
            foreach ($answers as $idx => $ans) {
                $pos = $idx + 1;
                $parts[] = "Q{$pos}: {$ans->name}";
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

    /**
     * Detailed piece review for Puzzle questions.
     *
     * @return array<int, array{position: int, student_piece: string, correct_piece: string, is_correct: bool}>
     */
    public function getPuzzleReview(): array
    {
        if ((int) ($this->question?->type ?? 0) !== 6) {
            return [];
        }

        $answers = $this->question->answers->values();
        $answersMap = $this->question->answers->keyBy('id');

        $submittedList = is_array($this->match_answers)
            ? $this->match_answers
            : json_decode($this->match_answers ?? '[]', true);

        $submittedList = array_values(is_array($submittedList) ? $submittedList : []);

        $review = [];
        foreach ($answers as $idx => $correctAns) {
            $submittedVal = $submittedList[$idx] ?? null;
            $submittedText = 'Not Arranged';
            $isPieceCorrect = false;

            if ($submittedVal !== null) {
                $submittedText = $answersMap->get($submittedVal)?->name ?? (string) $submittedVal;
                if ((string) $submittedVal === (string) $correctAns->id || trim(strtolower((string) $submittedVal)) === trim(strtolower((string) $correctAns->name))) {
                    $isPieceCorrect = true;
                }
            }

            $review[] = [
                'position' => $idx + 1,
                'student_piece' => $submittedText,
                'correct_piece' => $correctAns->name,
                'is_correct' => $isPieceCorrect,
            ];
        }

        return $review;
    }

    /**
     * Detailed blank review for Fill in the Blanks questions.
     *
     * @return array<int, array{blank_number: int, student_answer: string, correct_answer: string, is_correct: bool}>
     */
    public function getBlanksReview(): array
    {
        if ((int) ($this->question?->type ?? 0) !== 7) {
            return [];
        }

        $answers = $this->question->answers->values();
        $submittedMatches = is_array($this->match_answers)
            ? $this->match_answers
            : json_decode($this->match_answers ?? '[]', true);

        $submittedMatches = is_array($submittedMatches) ? $submittedMatches : [];

        $review = [];
        foreach ($answers as $idx => $correctAns) {
            $submitted = $submittedMatches[$correctAns->id]
                ?? $submittedMatches[(string) $correctAns->id]
                ?? $submittedMatches[$idx]
                ?? $submittedMatches[(string) $idx]
                ?? null;

            $isCorrect = $submitted !== null && trim(mb_strtolower((string) $submitted)) === trim(mb_strtolower((string) $correctAns->name));

            $review[] = [
                'blank_number' => $idx + 1,
                'student_answer' => $submitted !== null && trim((string) $submitted) !== '' ? (string) $submitted : 'Not Answered',
                'correct_answer' => $correctAns->name,
                'is_correct' => $isCorrect,
            ];
        }

        return $review;
    }

    /**
     * Detailed sub-question review for Case-Based / Source-Based questions.
     *
     * @return array<int, array{sub_question_number: int, prompt: string, options: array<int, string>, student_answer: string, correct_answer: string, is_correct: bool}>
     */
    public function getCaseStudyReview(): array
    {
        if ((int) ($this->question?->type ?? 0) !== 9) {
            return [];
        }

        $answers = $this->question->answers->values();
        $submittedMatches = is_array($this->match_answers)
            ? $this->match_answers
            : json_decode($this->match_answers ?? '[]', true);

        $submittedMatches = is_array($submittedMatches) ? $submittedMatches : [];

        $review = [];
        foreach ($answers as $idx => $correctAns) {
            $submitted = $submittedMatches[$correctAns->id]
                ?? $submittedMatches[(string) $correctAns->id]
                ?? $submittedMatches[$idx]
                ?? $submittedMatches[(string) $idx]
                ?? null;

            $isCorrect = $submitted !== null && trim(mb_strtolower((string) $submitted)) === trim(mb_strtolower((string) $correctAns->name));

            $review[] = [
                'sub_question_number' => $idx + 1,
                'prompt' => $correctAns->getCasePrompt(),
                'options' => $correctAns->getBlankOptions(),
                'student_answer' => $submitted !== null && trim((string) $submitted) !== '' ? (string) $submitted : 'Not Answered',
                'correct_answer' => $correctAns->name,
                'is_correct' => $isCorrect,
            ];
        }

        return $review;
    }

    /**
     * Detailed hotspot review for Image Hotspot / Diagram Labeling questions.
     *
     * @return array<int, array{pin_number: int, x: float, y: float, student_answer: string, correct_answer: string, is_correct: bool}>
     */
    public function getHotspotsReview(): array
    {
        if ((int) ($this->question?->type ?? 0) !== 8) {
            return [];
        }

        $answers = $this->question->answers->values();
        $submittedMatches = is_array($this->match_answers)
            ? $this->match_answers
            : json_decode($this->match_answers ?? '[]', true);

        $submittedMatches = is_array($submittedMatches) ? $submittedMatches : [];

        $review = [];
        foreach ($answers as $idx => $correctAns) {
            $submitted = $submittedMatches[$correctAns->id]
                ?? $submittedMatches[(string) $correctAns->id]
                ?? $submittedMatches[$idx]
                ?? $submittedMatches[(string) $idx]
                ?? null;

            $isCorrect = $submitted !== null && trim(mb_strtolower((string) $submitted)) === trim(mb_strtolower((string) $correctAns->name));
            $coords = $correctAns->getHotspotCoordinates();

            $review[] = [
                'pin_number' => $idx + 1,
                'x' => $coords['x'],
                'y' => $coords['y'],
                'student_answer' => $submitted !== null && trim((string) $submitted) !== '' ? (string) $submitted : 'Not Answered',
                'correct_answer' => $correctAns->name,
                'is_correct' => $isCorrect,
            ];
        }

        return $review;
    }
}
