<?php

namespace App\Http\Controllers;

use App\Models\Standard;
use App\Models\Student;
use App\Models\Subject;
use App\Models\Syllabus;
use App\Models\User;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use Illuminate\View\View;

class StandardController extends Controller
{
    /**
     * Display a listing of standards with filtering, metrics, and modals.
     */
    public function index(Request $request): View
    {
        $user = $request->user();

        if (! $user->canAssignExams()) {
            abort(403, 'Only teachers and administrators can view standards.');
        }

        Standard::cleanUpAllIneligibleCustomGroupEnrollments();

        $query = Standard::with(['creator', 'syllabus', 'students', 'teachers', 'chapters.topics', 'chapters.subject'])->withCount(['students', 'chapters']);

        if ($user->isTeacher() && ! $user->isAdmin()) {
            $query->accessibleTo($user);
        }

        if ($request->filled('search')) {
            $search = trim($request->input('search'));
            $query->where('name', 'like', "%{$search}%");
        }

        if ($request->filled('syllabus_id')) {
            $query->where('syllabus_id', (int) $request->input('syllabus_id'));
        }

        $standards = $query->orderBy('name')->paginate(10)->appends($request->query());
        $syllabuses = Syllabus::orderBy('name')->get();

        // All active students for assigning to standards
        $allStudentsQuery = User::where(function ($q) {
            $q->whereHas('profile', fn ($p) => $p->where('type', 2))
                ->orWhereHas('student');
        });

        $teacherAssignedAdminStandards = collect();
        if ($user->isTeacher() && ! $user->isAdmin()) {
            $teacherAssignedAdminStandards = $user->standards()
                ->adminCreated()
                ->get(['standards.id', 'standards.name']);
            $teacherAdminStdIds = $teacherAssignedAdminStandards->pluck('id')->toArray();

            if (! empty($teacherAdminStdIds)) {
                $allStudentsQuery->where(function ($q) use ($teacherAdminStdIds) {
                    $q->whereHas('studentStandards', fn ($st) => $st->whereIn('standards.id', $teacherAdminStdIds))
                        ->orWhereHas('student', fn ($st) => $st->whereIn('standard_id', $teacherAdminStdIds));
                });
            } else {
                $allStudentsQuery->whereRaw('1 = 0');
            }
        }

        $allStudents = $allStudentsQuery
            ->with(['profile', 'studentStandards.creator.profile', 'student.standard.creator.profile'])
            ->orderBy('name')
            ->get();

        $totalStandardsCount = $standards->total();
        $myStandardsCount = $user->isTeacher() && ! $user->isAdmin()
            ? Standard::accessibleTo($user)->count()
            : $totalStandardsCount;
        $subjects = Subject::orderBy('name')->get();

        return view('standards.index', compact(
            'standards',
            'syllabuses',
            'allStudents',
            'teacherAssignedAdminStandards',
            'totalStandardsCount',
            'myStandardsCount',
            'subjects'
        ));
    }

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

        if (! $user->isAdmin() && (int) $standard->created_by !== (int) $user->id) {
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

        if (! $user->isAdmin() && (int) $standard->created_by !== (int) $user->id) {
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

        // Teacher restriction: Teachers can only assign students belonging to their admin-assigned standards
        if ($user->isTeacher() && ! $user->isAdmin() && ! empty($studentIds)) {
            $teacherAdminStandards = $user->standards()
                ->adminCreated()
                ->get(['standards.id', 'standards.name']);
            $teacherAdminStdIds = $teacherAdminStandards->pluck('id')->toArray();

            if (empty($teacherAdminStdIds)) {
                return back()->withErrors([
                    'student_ids' => 'You have not been assigned any class standards by the administrator. You cannot assign students to your custom group until the administrator assigns you classes.',
                ]);
            }

            $unauthorizedStudents = User::whereIn('id', $studentIds)
                ->where(function ($q) use ($teacherAdminStdIds) {
                    $q->whereDoesntHave('studentStandards', fn ($st) => $st->whereIn('standards.id', $teacherAdminStdIds))
                        ->whereDoesntHave('student', fn ($st) => $st->whereIn('standard_id', $teacherAdminStdIds));
                })
                ->pluck('name')
                ->toArray();

            if (! empty($unauthorizedStudents)) {
                $classNames = $teacherAdminStandards->pluck('name')->join(', ');

                return back()->withErrors([
                    'student_ids' => 'You can only assign students from your assigned classes ('.$classNames.') to your custom group. The following student(s) cannot be assigned: '.implode(', ', $unauthorizedStudents).'.',
                ]);
            }
        }

        // A student assigned to one admin-created standard cannot be assigned to another admin-created standard
        if ($standard->isAdminCreated() && ! empty($studentIds)) {
            $otherAdminStandardIds = Standard::adminCreated()
                ->where('id', '!=', $standard->id)
                ->pluck('id')
                ->toArray();

            if (! empty($otherAdminStandardIds)) {
                $conflictsFromPivot = DB::table('student_standards')
                    ->join('standards', 'student_standards.standard_id', '=', 'standards.id')
                    ->join('users', 'student_standards.student_id', '=', 'users.id')
                    ->whereIn('student_standards.student_id', $studentIds)
                    ->whereIn('student_standards.standard_id', $otherAdminStandardIds)
                    ->select('users.id as student_id', 'users.name as student_name', 'standards.name as standard_name')
                    ->get();

                if ($conflictsFromPivot->isNotEmpty()) {
                    $messages = $conflictsFromPivot->map(fn ($c) => "{$c->student_name} is already assigned to admin-created standard '{$c->standard_name}'")->values()->all();

                    return back()->withErrors([
                        'student_ids' => 'Students assigned to one admin-created standard cannot be assigned to another admin-created standard: '.implode('; ', $messages).'.',
                    ]);
                }
            }
        }

        DB::transaction(function () use ($request, $standard, $studentIds) {
            foreach ($studentIds as $studentUserId) {
                $studentUser = User::find($studentUserId);
                if ($studentUser) {
                    DB::table('student_standards')->updateOrInsert(
                        [
                            'student_id' => $studentUser->id,
                            'standard_id' => $standard->id,
                        ],
                        [
                            'created_at' => now(),
                            'updated_at' => now(),
                        ]
                    );

                    $existingStudent = Student::find($studentUser->id);
                    $hasAdminStandard = $existingStudent && $existingStudent->standard && $existingStudent->standard->isAdminCreated();

                    $stdIdToSet = ($standard->isAdminCreated() || ! $hasAdminStandard)
                        ? $standard->id
                        : $existingStudent->standard_id;

                    Student::updateOrCreate(
                        ['id' => $studentUser->id],
                        [
                            'name' => $studentUser->name,
                            'standard_id' => $stdIdToSet,
                        ]
                    );
                }
            }

            if ($request->input('_assign_mode') === 'bulk') {
                $unassignQuery = DB::table('student_standards')
                    ->where('standard_id', $standard->id);

                if (! empty($studentIds)) {
                    $unassignQuery->whereNotIn('student_id', $studentIds);
                }

                $unassignedStudentIds = $unassignQuery->pluck('student_id')->toArray();

                if (! empty($unassignedStudentIds)) {
                    DB::table('student_standards')
                        ->where('standard_id', $standard->id)
                        ->whereIn('student_id', $unassignedStudentIds)
                        ->delete();

                    if ($standard->isAdminCreated()) {
                        Student::whereIn('id', $unassignedStudentIds)
                            ->where('standard_id', $standard->id)
                            ->update(['standard_id' => null]);

                        Standard::removeStudentsFromRelatedCustomGroups($unassignedStudentIds, $standard->id);
                    }
                }
            }
        });

        Standard::cleanUpAllIneligibleCustomGroupEnrollments();

        return back()->with('status', 'Students assigned to standard successfully!');
    }

    /**
     * Unassign a single student from the standard.
     */
    public function unassignStudent(Request $request, Standard $standard): RedirectResponse
    {
        $user = $request->user();

        if (! $user->canAssignExams()) {
            abort(403, 'Unauthorized.');
        }

        if (! $user->isAdmin() && (int) $standard->created_by !== (int) $user->id) {
            abort(403, 'Teachers can only unassign students from standards created by themselves.');
        }

        $studentId = (int) $request->input('student_id');
        if (! $studentId) {
            return back()->withErrors(['student_id' => 'Invalid student.']);
        }

        DB::transaction(function () use ($standard, $studentId) {
            DB::table('student_standards')
                ->where('standard_id', $standard->id)
                ->where('student_id', $studentId)
                ->delete();

            if ($standard->isAdminCreated()) {
                Student::where('id', $studentId)
                    ->where('standard_id', $standard->id)
                    ->update(['standard_id' => null]);

                Standard::removeStudentsFromRelatedCustomGroups([$studentId], $standard->id);
            }
        });

        Standard::cleanUpAllIneligibleCustomGroupEnrollments();

        return back()->with('status', 'Student unassigned successfully!');
    }

    /**
     * Remove the specified standard from storage.
     */
    public function destroy(Request $request, Standard $standard): RedirectResponse
    {
        $user = $request->user();

        if (! $user->canAssignExams()) {
            abort(403, 'Only teachers and administrators can delete standards.');
        }

        if (! $user->isAdmin() && (int) $standard->created_by !== (int) $user->id) {
            abort(403, 'Teachers can only delete standards created by themselves.');
        }

        if ($standard->students()->count() > 0) {
            return back()->with('error', 'Cannot delete standard/group with enrolled students in it. Please remove or reassign all students first.');
        }

        DB::transaction(function () use ($standard) {
            $standard->teachers()->detach();
            $standard->assignedExams()->detach();
            $standard->delete();
        });

        return back()->with('status', 'Standard deleted successfully!');
    }
}
