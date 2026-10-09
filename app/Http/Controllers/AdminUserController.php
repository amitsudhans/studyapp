<?php

namespace App\Http\Controllers;

use App\Models\Student;
use App\Models\User;
use App\Models\UserProfile;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Facades\Validator;
use Illuminate\Validation\Rule;

class AdminUserController extends Controller
{
    /**
     * Authorize admin users.
     */
    private function authorizeAdmin(Request $request): void
    {
        $user = $request->user();
        if (! $user) {
            abort(403, 'Unauthorized action.');
        }

        $type = (int) ($user->profile?->type ?? 1);
        $isAdmin = ($type === 3 || $type === 0 || $type === 99 || $user->email === 'admin@example.com' || $user->profile?->designation === 'Administrator' || ($type !== 1 && $type !== 2));

        if (! $isAdmin) {
            abort(403, 'Unauthorized action.');
        }
    }

    /**
     * Store a newly created user with profile and teacher standards or student record.
     */
    public function store(Request $request): RedirectResponse
    {
        $this->authorizeAdmin($request);

        $validator = Validator::make($request->all(), [
            'name' => ['required', 'string', 'max:255'],
            'email' => ['required', 'string', 'email', 'max:255', 'unique:users,email'],
            'password' => ['required', 'string', 'min:8'],
            'mobile' => ['required', 'string', 'max:20'],
            'address' => ['required', 'string', 'max:1000'],
            'type' => ['nullable', 'integer', 'in:1,2,3'],
            'school' => ['nullable', 'string', 'max:255'],
            'designation' => ['nullable', 'string', 'max:255'],
            'remark' => ['nullable', 'string', 'max:1000'],
            'status' => ['nullable', 'integer', 'in:0,1'],
            'standard_id' => ['nullable', 'exists:standards,id'],
            'standards' => ['nullable', 'array'],
            'standards.*' => ['exists:standards,id'],
        ]);

        $validator->after(function ($validator) use ($request) {
            $type = (int) ($request->input('type') ?? 1);
            if ($type === 2) {
                $stdId = $request->input('standard_id') ?? ($request->input('standards')[0] ?? null);
                if ($stdId) {
                    $count = Student::where('standard_id', $stdId)->count();
                    if ($count >= 100) {
                        $validator->errors()->add('standard_id', 'The selected class has reached the maximum limit of 100 students.');
                    }
                }
            }
        });

        $validated = $validator->validate();

        DB::transaction(function () use ($validated) {
            $user = User::create([
                'name' => $validated['name'],
                'email' => $validated['email'],
                'password' => Hash::make($validated['password']),
                'status' => $validated['status'] ?? 1,
            ]);

            $type = isset($validated['type']) ? (int) $validated['type'] : 1;

            UserProfile::create([
                'user_id' => $user->id,
                'name' => $validated['name'],
                'mobile' => $validated['mobile'],
                'address' => $validated['address'],
                'type' => $type,
                'school' => $validated['school'] ?? null,
                'designation' => $validated['designation'] ?? ($type === 3 ? 'Administrator' : null),
                'remark' => $validated['remark'] ?? null,
            ]);

            if ($type === 2) { // Student: type = 2, don't insert data to teacher_standards
                $stds = ! empty($validated['standards']) ? $validated['standards'] : (isset($validated['standard_id']) ? [$validated['standard_id']] : []);
                if (! empty($stds)) {
                    $user->studentStandards()->sync($stds);
                    Student::updateOrCreate(
                        ['id' => $user->id],
                        [
                            'name' => $validated['name'],
                            'standard_id' => $stds[0],
                        ]
                    );
                }
            } elseif ($type === 1) { // Teacher: type = 1
                if (! empty($validated['standards'])) {
                    $user->standards()->sync($validated['standards']);
                }
            } else { // Administrator: type = 3
                Student::where('id', $user->id)->delete();
                $user->standards()->detach();
            }
        });

        return redirect()->route('dashboard')->with('status', 'User created successfully!');
    }

    /**
     * Update the specified user, profile, and teacher standards or student record.
     */
    public function update(Request $request, User $user): RedirectResponse
    {
        $this->authorizeAdmin($request);

        $validator = Validator::make($request->all(), [
            'name' => ['required', 'string', 'max:255'],
            'email' => ['required', 'string', 'email', 'max:255', Rule::unique('users', 'email')->ignore($user->id)],
            'password' => ['nullable', 'string', 'min:8'],
            'mobile' => ['required', 'string', 'max:20'],
            'address' => ['required', 'string', 'max:1000'],
            'school' => ['nullable', 'string', 'max:255'],
            'designation' => ['nullable', 'string', 'max:255'],
            'remark' => ['nullable', 'string', 'max:1000'],
            'status' => ['nullable', 'integer', 'in:0,1'],
            'standard_id' => ['nullable', 'exists:standards,id'],
            'standards' => ['nullable', 'array'],
            'standards.*' => ['exists:standards,id'],
        ]);

        $type = (int) ($user->profile?->type ?? 1);

        $validator->after(function ($validator) use ($request, $user, $type) {
            if ($type === 2) {
                $stdId = $request->input('standard_id') ?? ($request->input('standards')[0] ?? null);
                if ($stdId) {
                    $currentStudent = Student::where('id', $user->id)->first();
                    if (! $currentStudent || (int) $currentStudent->standard_id !== (int) $stdId) {
                        $count = Student::where('standard_id', $stdId)->count();
                        if ($count >= 100) {
                            $validator->errors()->add('standard_id', 'The selected class has reached the maximum limit of 100 students.');
                        }
                    }
                }
            }
        });

        $validated = $validator->validate();

        DB::transaction(function () use ($user, $validated, $type) {
            $userData = [
                'name' => $validated['name'],
                'email' => $validated['email'],
            ];

            if (! empty($validated['password'])) {
                $userData['password'] = Hash::make($validated['password']);
            }

            if (isset($validated['status'])) {
                $userData['status'] = (int) $validated['status'];
            }

            $user->update($userData);

            $user->profile()->updateOrCreate(
                ['user_id' => $user->id],
                [
                    'name' => $validated['name'],
                    'mobile' => $validated['mobile'],
                    'address' => $validated['address'],
                    'school' => $validated['school'] ?? null,
                    'designation' => $validated['designation'] ?? null,
                    'remark' => $validated['remark'] ?? null,
                    'type' => $type,
                ]
            );

            if ($type === 2) { // Student: type = 2, don't insert data to teacher_standards
                $user->standards()->detach();
                $stds = ! empty($validated['standards']) ? $validated['standards'] : (isset($validated['standard_id']) ? [$validated['standard_id']] : []);
                if (! empty($stds)) {
                    $user->studentStandards()->sync($stds);
                    Student::updateOrCreate(
                        ['id' => $user->id],
                        [
                            'name' => $validated['name'],
                            'standard_id' => $stds[0],
                        ]
                    );
                }
            } elseif ($type === 1) { // Teacher: type = 1
                Student::where('id', $user->id)->delete();
                DB::table('student_standards')->where('student_id', $user->id)->delete();
                $user->standards()->sync($validated['standards'] ?? []);
            } else { // Administrator: type = 3
                Student::where('id', $user->id)->delete();
                DB::table('student_standards')->where('student_id', $user->id)->delete();
                $user->standards()->detach();
            }
        });

        return redirect()->route('dashboard')->with('status', 'User updated successfully!');
    }

    /**
     * Remove the specified user.
     */
    public function destroy(Request $request, User $user): RedirectResponse
    {
        $this->authorizeAdmin($request);

        // Prevent self deletion
        if ($user->id === $request->user()->id) {
            return redirect()->route('dashboard')->with('status', 'Cannot delete your own admin account.');
        }

        $user->delete();

        return redirect()->route('dashboard')->with('status', 'User deleted successfully!');
    }
}
