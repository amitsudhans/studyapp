<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

#[Fillable(['name'])]
class Syllabus extends Model
{
    use HasFactory;

    /**
     * The table associated with the model.
     *
     * @var string
     */
    protected $table = 'syllabuses';

    /**
     * Get the standards for the syllabus.
     *
     * @return HasMany<Standard, $this>
     */
    public function standards(): HasMany
    {
        return $this->hasMany(Standard::class, 'syllabus_id');
    }
}
