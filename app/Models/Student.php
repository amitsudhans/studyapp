<?php

namespace App\Models;

use Database\Factories\StudentFactory;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Validation\ValidationException;

class Student extends Model
{
    /** @use HasFactory<StudentFactory> */
    use HasFactory;

    /**
     * The attributes that are mass assignable.
     *
     * @var array<int, string>
     */
    protected $fillable = [
        'id',
        'name',
        'standard_id',
    ];

    /**
     * Get the attributes that should be cast.
     *
     * @return array<string, string>
     */
    protected function casts(): array
    {
        return [
            'standard_id' => 'integer',
        ];
    }

    /**
     * Boot the model.
     */
    protected static function booted(): void
    {
        static::saving(function (Student $student) {
            if ($student->isDirty('standard_id') && $student->standard_id) {
                $count = static::where('standard_id', $student->standard_id)
                    ->where('id', '!=', $student->id)
                    ->count();

                if ($count >= 100) {
                    throw ValidationException::withMessages([
                        'standard_id' => ['The selected class has reached the maximum limit of 100 students.'],
                    ]);
                }
            }
        });
    }

    /**
     * Get the standard that the student belongs to.
     *
     * @return BelongsTo<Standard, $this>
     */
    public function standard(): BelongsTo
    {
        return $this->belongsTo(Standard::class);
    }

    /**
     * Get the user that the student belongs to.
     *
     * @return BelongsTo<User, $this>
     */
    public function user(): BelongsTo
    {
        return $this->belongsTo(User::class, 'id', 'id');
    }
}
