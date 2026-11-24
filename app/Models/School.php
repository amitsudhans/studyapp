<?php

namespace App\Models;

use Database\Factories\SchoolFactory;
use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

#[Fillable([
    'name',
    'address',
    'contactno',
    'head',
    'district',
    'state',
    'country',
])]
class School extends Model
{
    /** @use HasFactory<SchoolFactory> */
    use HasFactory;

    /**
     * Get the profiles belonging to this school.
     *
     * @return HasMany<UserProfile, $this>
     */
    public function profiles(): HasMany
    {
        return $this->hasMany(UserProfile::class, 'school_id');
    }
}
