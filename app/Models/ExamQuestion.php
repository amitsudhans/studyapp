<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class ExamQuestion extends Model
{
    use HasFactory;

    protected $fillable = [
        'exam_id',
        'question_id',
        'status',
    ];

    protected $casts = [
        'status' => 'integer',
    ];

    /**
     * Get the exam that owns the exam question link.
     */
    public function exam(): BelongsTo
    {
        return $this->belongsTo(Exam::class);
    }

    /**
     * Get the question linked to the exam.
     */
    public function question(): BelongsTo
    {
        return $this->belongsTo(Question::class);
    }
}
