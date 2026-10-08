<?php

namespace App\Http\Controllers;

use App\Models\Standard;
use App\Models\Student;
use App\Models\Syllabus;
use App\Models\User;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class StandardController extends Controller
{
    /**
     * Store a newly created standard in storage.
     */
    public function store(Request $request): RedirectResponse
    {
        $user = $request->user();

        if (! $user->canAssignExams()) {
            abort(403, 'Only teachers and administrators can create standards.');
        }

        $validated = $request->validate([
            'name' => ['required', 'string', 'max:255'],
            'syllabus_id' => ['nullable', 'integer', 'exists:syllabuses,id'],
        ]);

        $syllabusId = $validated['syllabus_id'] ?? Syllabus::first()?->id ?? 1;

        $standard = Standard::create([
            'name' => $validated['name'],
            'syllabus_id' => $syllabusId,
            'created_by' => $user->id,
        ]);

        if ($user->isTeacher()) {
            $user->standards()->syncWithoutDetaching([$standard->id]);
        }

        return back()->with('status', 'Standard created successfully!');
    }

    /**
     * Update the specified standard in storage.
     */
    public function update(Request $request, Standard $standard): RedirectResponse
    {
        $user = $request->user();

        if (! $user->canAssignExams()) {
            abort(403, 'Only teachers and administrators can edit standards.');
        }

        if (! $user->isAdmin() && $standard->created_by !== $user->id) {
            abort(403, 'Teachers can only edit standards created by themselves.');
        }

        $validated = $request->validate([
            'name' => ['required', 'string', 'max:255'],
            'syllabus_id' => ['nullable', 'integer', 'exists:syllabuses,id'],
        ]);

        $updateData = [
            'name' => $validated['name'],
        ];

        if (! empty($validated['syllabus_id'])) {
            $updateData['syllabus_id'] = $validated['syllabus_id'];
        }

        if (empty($standard->created_by)) {
            $updateData['created_by'] = $user->id;
        }

        $standard->update($updateData);

        return back()->with('status', 'Standard updated successfully!');
    }

    /**
     * Assign student(s) to the specified standard (Teachers & Admins).
     */
    public function assignStudents(Request $request, Standard $standard): RedirectResponse
    {
        $user = $request->user();

        if (! $user->canAssignExams()) {
            abort(403, 'Only teachers and administrators can assign students to standards.');
        }

        if (! $user->isAdmin() && $standard->created_by !== $user->id) {
            abort(403, 'Teachers can only assign students to standards created by themselves.');
        }

        $studentIds = [];
        if ($request->has('student_ids')) {
            $studentIds = array_filter(array_map('intval', (array) $request->input('student_ids')));
        } elseif ($request->has('student_id')) {
            $singleId = (int) $request->input('student_id');
            if ($singleId > 0) {
                $studentIds = [$singleId];
            }
        }

        if (count($studentIds) > 100) {
            return back()->withErrors(['student_ids' => 'A standard cannot have more than 100 students.']);
        }

        if (! empty($studentIds)) {
            $validStudentCount = User::whereIn('id', $studentIds)
                ->where(function ($q) {
                    $q->whereHas('profile', fn ($p) => $p->where('type', 2))
                        ->orWhereHas('student');
                })
                ->count();

            if ($validStudentCount !== count($studentIds)) {
                return back()->withErrors(['student_ids' => 'One or more selected users are not valid students.']);
            }
        }

        DB::transaction(function () use ($request, $standard, $studentIds) {
            foreach ($studentIds as $studentUserId) {
                $studentUser = User::find($studentUserId);
                if ($studentUser) {
                    Student::updateOrCreate(
                        ['id' => $studentUser->id],
                        [
                            'name' => $studentUser->name,
                            'standard_id' => $standard->id,
                        ]
                    );
                }
            }

            if ($request->input('_assign_mode') === 'bulk') {
                Student::where('standard_id', $standard->id)
                    ->whereNotIn('id', $studentIds)
                    ->update(['standard_id' => null]);
            }
        });

        return back()->with('status', 'Students assigned to standard successfully!');
    }
}
