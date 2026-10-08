<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

#[Fillable(['user_id', 'standard_id'])]
class TeacherStandard extends Model
{
    use HasFactory;

    /**
     * The table associated with the model.
     *
     * @var string
     */
    protected $table = 'teacher_standards';

    /**
     * Get the user (teacher) for the standard.
     *
     * @return BelongsTo<User, $this>
     */
    public function user(): BelongsTo
    {
        return $this->belongsTo(User::class);
    }

    /**
     * Get the standard assigned to the teacher.
     *
     * @return BelongsTo<Standard, $this>
     */
    public function standard(): BelongsTo
    {
        return $this->belongsTo(Standard::class);
    }
}
