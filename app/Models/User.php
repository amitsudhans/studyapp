<?php

namespace App\Models;

// use Illuminate\Contracts\Auth\MustVerifyEmail;
use Database\Factories\UserFactory;
use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Attributes\Hidden;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;
use Illuminate\Database\Eloquent\Relations\HasMany;
use Illuminate\Database\Eloquent\Relations\HasOne;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;

#[Fillable(['name', 'email', 'password', 'status'])]
#[Hidden(['password', 'remember_token'])]
class User extends Authenticatable
{
    /** @use HasFactory<UserFactory> */
    use HasFactory, Notifiable;

    /**
     * Get the profile associated with the user.
     *
     * @return HasOne<UserProfile, $this>
     */
    public function profile(): HasOne
    {
        return $this->hasOne(UserProfile::class);
    }

    /**
     * Get the standards assigned to the user (teacher).
     *
     * @return BelongsToMany<Standard, $this>
     */
    public function standards(): BelongsToMany
    {
        return $this->belongsToMany(Standard::class, 'teacher_standards');
    }

    /**
     * Get the student record associated with the user.
     *
     * @return HasOne<Student, $this>
     */
    public function student(): HasOne
    {
        return $this->hasOne(Student::class, 'id', 'id');
    }

    /**
     * Get the standards assigned to the user (student).
     *
     * @return BelongsToMany<Standard, $this>
     */
    public function studentStandards(): BelongsToMany
    {
        return $this->belongsToMany(Standard::class, 'student_standards', 'student_id', 'standard_id');
    }

    /**
     * Get messages sent by this user.
     *
     * @return HasMany<ChatMessage, $this>
     */
    public function sentMessages(): HasMany
    {
        return $this->hasMany(ChatMessage::class, 'sender_id');
    }

    /**
     * Get messages received by this user.
     *
     * @return HasMany<ChatMessage, $this>
     */
    public function receivedMessages(): HasMany
    {
        return $this->hasMany(ChatMessage::class, 'receiver_id');
    }

    /**
     * Get unread messages received by this user.
     *
     * @return HasMany<ChatMessage, $this>
     */
    public function unreadMessages(): HasMany
    {
        return $this->hasMany(ChatMessage::class, 'receiver_id')->where('is_read', false);
    }

    /**
     * Check if user is an Administrator.
     */
    public function isAdmin(): bool
    {
        $type = (int) ($this->profile?->type ?? 1);

        return $type === 3 || $type === 0 || $type === 99 || $this->email === 'admin@example.com' || $this->profile?->designation === 'Administrator';
    }

    /**
     * Check if user is a Teacher.
     */
    public function isTeacher(): bool
    {
        return (int) ($this->profile?->type ?? 1) === 1;
    }

    /**
     * Check if user is a Student.
     */
    public function isStudent(): bool
    {
        return (int) ($this->profile?->type ?? 1) === 2;
    }

    /**
     * Check if user has permission to manage/assign exams.
     */
    public function canAssignExams(): bool
    {
        return $this->isTeacher() || $this->isAdmin();
    }

    /**
     * Get the attributes that should be cast.
     *
     * @return array<string, string>
     */
    protected function casts(): array
    {
        return [
            'email_verified_at' => 'datetime',
            'password' => 'hashed',
            'status' => 'integer',
        ];
    }
}
