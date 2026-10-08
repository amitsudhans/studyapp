<?php

namespace App\Models;

use Database\Factories\ExamAssignFactory;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class ExamAssign extends Model
{
    /** @use HasFactory<ExamAssignFactory> */
    use HasFactory;

    /**
     * The table associated with the model.
     *
     * @var string
     */
    protected $table = 'exam_assign';

    /**
     * The attributes that are mass assignable.
     *
     * @var array<int, string>
     */
    protected $fillable = [
        'exam_id',
        'standard_id',
        'status',
    ];

    /**
     * Get the attributes that should be cast.
     *
     * @return array<string, string>
     */
    protected function casts(): array
    {
        return [
            'exam_id' => 'integer',
            'standard_id' => 'integer',
            'status' => 'integer',
        ];
    }

    /**
     * Get the exam associated with the assignment.
     *
     * @return BelongsTo<Exam, $this>
     */
    public function exam(): BelongsTo
    {
        return $this->belongsTo(Exam::class);
    }

    /**
     * Get the standard associated with the assignment.
     *
     * @return BelongsTo<Standard, $this>
     */
    public function standard(): BelongsTo
    {
        return $this->belongsTo(Standard::class);
    }
}
