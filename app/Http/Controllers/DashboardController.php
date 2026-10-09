<?php

namespace App\Http\Controllers;

use App\Models\Exam;
use App\Models\Standard;
use App\Models\StudentExamDetail;
use App\Models\Syllabus;
use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Pagination\LengthAwarePaginator;
use Illuminate\Support\Facades\Auth;
use Illuminate\View\View;

class DashboardController extends Controller
{
    /**
     * Display the dashboard.
     */
    public function index(Request $request): View
    {
        $user = Auth::user()->load(['profile', 'standards', 'student.standard']);

        $type = (int) ($user->profile?->type ?? 1);
        $isStudent = ($type === 2);
        $isAdmin = ($type === 3 || $type === 0 || $type === 99 || $user->email === 'admin@example.com' || $user->profile?->designation === 'Administrator');

        $users = null;
        $standards = collect();
        $studentExams = collect();
        $submittedExamIds = [];
        $submittedDetails = collect();
        $totalUsersCount = 0;
        $teacherCount = 0;
        $studentCount = 0;
        $adminCount = 0;
        $teacherStudents = null;
        $teacherStudentsCount = 0;
        $teacherExams = collect();
        $teacherExamSubmissions = collect();

        if ($isAdmin) {
            $adminQuery = User::with(['profile', 'standards', 'student.standard']);

            if ($request->filled('role')) {
                $role = (int) $request->input('role');
                if ($role === 1) { // Teacher
                    $adminQuery->where(function ($q) {
                        $q->whereHas('profile', fn ($p) => $p->where('type', 1))
                            ->orWhereDoesntHave('profile');
                    });
                } elseif ($role === 2) { // Student
                    $adminQuery->whereHas('profile', fn ($p) => $p->where('type', 2));
                } elseif ($role === 3) { // Admin
                    $adminQuery->whereHas('profile', fn ($p) => $p->where('type', 3));
                }
            }

            if ($request->filled('admin_search')) {
                $search = trim($request->input('admin_search'));
                $adminQuery->where(function ($q) use ($search) {
                    $q->where('name', 'like', "%{$search}%")
                        ->orWhere('email', 'like', "%{$search}%")
                        ->orWhereHas('profile', function ($p) use ($search) {
                            $p->where('mobile', 'like', "%{$search}%")
                                ->orWhere('designation', 'like', "%{$search}%")
                                ->orWhere('school', 'like', "%{$search}%")
                                ->orWhere('address', 'like', "%{$search}%");
                        });
                });
            }

            $users = $adminQuery->latest()
                ->paginate(10, ['*'], 'users_page')
                ->appends($request->query());

            $standards = Standard::withCount('students')->with('creator.profile')->orderBy('id')->paginate(10, ['*'], 'standards_page')->appends($request->query());
            $totalUsersCount = User::count();
            $teacherCount = User::whereHas('profile', fn ($q) => $q->where('type', 1))->orWhereDoesntHave('profile')->count();
            $studentCount = User::whereHas('profile', fn ($q) => $q->where('type', 2))->count();
            $adminCount = User::whereHas('profile', fn ($q) => $q->where('type', 3))->count();
        } elseif ($isStudent) {
            $studentId = $user->student?->id ?? $user->id;
            $standardId = $user->student?->standard_id;
            if ($standardId) {
                $studentExams = Exam::whereHas('standards', function ($query) use ($standardId) {
                    $query->where('standards.id', $standardId);
                })
                    ->with(['creator', 'questions.standard', 'questions.answers', 'standards'])
                    ->latest()
                    ->get();
            }

            if ($studentId) {
                $submittedExamIds = StudentExamDetail::where('student_id', $studentId)
                    ->pluck('exam_id')
                    ->unique()
                    ->toArray();

                $submittedDetails = StudentExamDetail::where('student_id', $studentId)
                    ->with(['question.answers', 'writtenAnswer'])
                    ->get()
                    ->groupBy('exam_id');
            }
        } else {
            $teacherStandardIds = $user->standards->pluck('id')->toArray();
            if (! empty($teacherStandardIds)) {
                $query = User::whereHas('student', function ($query) use ($teacherStandardIds) {
                    $query->whereIn('standard_id', $teacherStandardIds);
                });

                if ($request->filled('search')) {
                    $search = trim($request->input('search'));
                    $query->where(function ($q) use ($search) {
                        $q->where('name', 'like', "%{$search}%")
                            ->orWhere('email', 'like', "%{$search}%");
                    });
                }

                if ($request->filled('standard_id')) {
                    $selectedStandardId = (int) $request->input('standard_id');
                    $query->whereHas('student', function ($q) use ($selectedStandardId) {
                        $q->where('standard_id', $selectedStandardId);
                    });
                }

                $teacherStudents = $query->with(['profile', 'student.standard'])
                    ->latest()
                    ->paginate(10)
                    ->appends($request->query());

                $teacherStudentsCount = User::whereHas('student', function ($query) use ($teacherStandardIds) {
                    $query->whereIn('standard_id', $teacherStandardIds);
                })->count();
            }

            $examQuery = Exam::query();
            if (! empty($teacherStandardIds)) {
                $examQuery->where(function ($q) use ($teacherStandardIds, $user) {
                    $q->whereHas('standards', function ($sub) use ($teacherStandardIds) {
                        $sub->whereIn('standards.id', $teacherStandardIds);
                    })->orWhere('created_by', $user->id);
                });
            } else {
                $examQuery->where('created_by', $user->id);
            }

            $teacherExams = $examQuery->with(['creator', 'questions.answers', 'standards'])
                ->latest()
                ->paginate(10, ['*'], 'exams_page')
                ->appends($request->query());

            $examIds = $teacherExams->pluck('id')->toArray();
            if (! empty($examIds)) {
                $allDetails = StudentExamDetail::whereIn('exam_id', $examIds)
                    ->with(['student.standard', 'student.user', 'question.answers', 'writtenAnswer'])
                    ->get();

                $teacherExamSubmissions = $allDetails->groupBy('exam_id')->map(function ($examGroup) {
                    return $examGroup->groupBy('student_id');
                });
            }
        }

        if ($user->canAssignExams() && ($standards->isEmpty() || ! ($standards instanceof LengthAwarePaginator))) {
            $query = Standard::withCount('students')->with('creator.profile');

            if (! $isAdmin) {
                $query->where(function ($q) use ($user) {
                    $q->where('created_by', $user->id)
                        ->orWhereNull('created_by')
                        ->orWhereHas('creator', function ($cq) {
                            $cq->whereHas('profile', fn ($p) => $p->whereIn('type', [0, 3, 99]))
                                ->orWhereDoesntHave('profile')
                                ->orWhere('email', 'admin@example.com');
                        });
                });
            }

            $standards = $query->orderBy('id')->paginate(10, ['*'], 'standards_page')->appends($request->query());
        }

        $syllabi = Syllabus::orderBy('id')->get();

        $allStudents = collect();
        if ($user->canAssignExams()) {
            if ($request->filled('role') && (int) $request->input('role') === 1) {
                $allStudents = collect();
            } else {
                $allStudentsQuery = User::where(function ($q) {
                    $q->whereHas('profile', fn ($p) => $p->where('type', 2))
                        ->orWhereHas('student');
                });

                if ($request->filled('admin_search')) {
                    $search = trim($request->input('admin_search'));
                    $allStudentsQuery->where(function ($q) use ($search) {
                        $q->where('name', 'like', "%{$search}%")
                            ->orWhere('email', 'like', "%{$search}%");
                    });
                }

                $allStudents = $allStudentsQuery
                    ->with(['profile', 'student.standard'])
                    ->orderBy('name')
                    ->get();
            }
        }

        return view('dashboard', [
            'user' => $user,
            'isAdmin' => $isAdmin,
            'isStudent' => $isStudent,
            'users' => $users,
            'standards' => $standards,
            'syllabi' => $syllabi,
            'studentExams' => $studentExams,
            'submittedExamIds' => $submittedExamIds,
            'submittedDetails' => $submittedDetails,
            'totalUsersCount' => $totalUsersCount,
            'teacherCount' => $teacherCount,
            'studentCount' => $studentCount,
            'adminCount' => $adminCount,
            'teacherStudents' => $teacherStudents,
            'teacherStudentsCount' => $teacherStudentsCount,
            'teacherExams' => $teacherExams,
            'teacherExamSubmissions' => $teacherExamSubmissions,
            'allStudents' => $allStudents,
        ]);
    }
}
