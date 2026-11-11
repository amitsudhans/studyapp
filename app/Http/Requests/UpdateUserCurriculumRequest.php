<?php

namespace App\Http\Requests;

use Illuminate\Contracts\Validation\ValidationRule;
use Illuminate\Foundation\Http\FormRequest;

class UpdateUserCurriculumRequest extends FormRequest
{
    /**
     * Determine if the user is authorized to manage curriculum access.
     */
    public function authorize(): bool
    {
        $user = $this->user();

        if (! $user) {
            return false;
        }

        $type = (int) ($user->profile?->type ?? 1);

        return $user->isAdmin() || ($type !== 1 && $type !== 2);
    }

    /**
     * Get the validation rules that apply to the request.
     *
     * @return array<string, ValidationRule|array<mixed>|string>
     */
    public function rules(): array
    {
        return [
            'mode' => ['required', 'string', 'in:restricted,unrestricted'],
            'items' => ['nullable', 'array'],
            'items.*' => ['string', 'max:120'],
        ];
    }
}
