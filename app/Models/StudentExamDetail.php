<?php

namespace App\Models;

use Database\Factories\StudentExamDetailFactory;
use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

#[Fillable(['student_id', 'exam_id', 'question_id', 'student_written_ans_id'])]
class StudentExamDetail extends Model
{
    /** @use HasFactory<StudentExamDetailFactory> */
    use HasFactory;

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
}
