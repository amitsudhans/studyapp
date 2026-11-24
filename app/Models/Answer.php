<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

#[Fillable(['name', 'match_answer', 'question_id', 'is_correct', 'status'])]
class Answer extends Model
{
    use HasFactory;

    /**
     * Get the question that owns the answer.
     *
     * @return BelongsTo<Question, $this>
     */
    public function question(): BelongsTo
    {
        return $this->belongsTo(Question::class);
    }

    /**
     * Get options array for Fill in the Blanks question blank or Case Study sub-question.
     *
     * @return array<int, string>
     */
    public function getBlankOptions(): array
    {
        if (empty($this->match_answer)) {
            return [$this->name];
        }

        $decoded = json_decode($this->match_answer, true);
        if (is_array($decoded)) {
            // Hotspot coordinates & options payload: {"x": 30, "y": 45, "options": [...]}
            // Case Study payload: {"prompt": "...", "options": [...]}
            if (isset($decoded['options']) && is_array($decoded['options'])) {
                return array_values($decoded['options']);
            }

            return array_values($decoded);
        }

        return array_values(array_filter(array_map('trim', explode(',', (string) $this->match_answer))));
    }

    /**
     * Get prompt text for Case Study sub-question.
     */
    public function getCasePrompt(): string
    {
        if (empty($this->match_answer)) {
            return '';
        }

        $decoded = json_decode($this->match_answer, true);
        if (is_array($decoded) && isset($decoded['prompt'])) {
            return (string) $decoded['prompt'];
        }

        return '';
    }

    /**
     * Get coordinates (x, y percentages) for Image Hotspot answer pin.
     *
     * @return array{x: float, y: float}
     */
    public function getHotspotCoordinates(): array
    {
        if (empty($this->match_answer)) {
            return ['x' => 50.0, 'y' => 50.0];
        }

        $decoded = json_decode($this->match_answer, true);
        if (is_array($decoded)) {
            return [
                'x' => isset($decoded['x']) ? (float) $decoded['x'] : 50.0,
                'y' => isset($decoded['y']) ? (float) $decoded['y'] : 50.0,
            ];
        }

        return ['x' => 50.0, 'y' => 50.0];
    }

    /**
     * Get the attributes that should be cast.
     *
     * @return array<string, string>
     */
    protected function casts(): array
    {
        return [
            'is_correct' => 'integer',
            'status' => 'integer',
        ];
    }
}
