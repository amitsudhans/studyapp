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

            $totalUsersCount = User::count();
            $teacherCount = User::whereHas('profile', fn ($q) => $q->where('type', 1))->orWhereDoesntHave('profile')->count();
            $studentCount = User::whereHas('profile', fn ($q) => $q->where('type', 2))->count();
            $adminCount = User::whereHas('profile', fn ($q) => $q->where('type', 3))->count();
        } elseif ($isStudent) {
            $studentId = $user->student?->id ?? $user->id;
            $stdIds = $user->studentStandards->pluck('id')->merge(array_filter([$user->student?->standard_id]))->unique()->toArray();
            if (! empty($stdIds)) {
                $studentExams = Exam::whereHas('standards', function ($query) use ($stdIds) {
                    $query->whereIn('standards.id', $stdIds);
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
            $teacherStandardIds = Standard::where('created_by', $user->id)
                ->orWhereHas('teachers', fn ($tq) => $tq->where('users.id', $user->id))
                ->pluck('id')
                ->toArray();

            if (! empty($teacherStandardIds)) {
                $query = User::where(function ($q) use ($teacherStandardIds) {
                    $q->whereHas('studentStandards', fn ($st) => $st->whereIn('standards.id', $teacherStandardIds))
                        ->orWhereHas('student', fn ($st) => $st->whereIn('standard_id', $teacherStandardIds));
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
                    if (in_array($selectedStandardId, $teacherStandardIds)) {
                        $query->where(function ($q) use ($selectedStandardId) {
                            $q->whereHas('studentStandards', fn ($st) => $st->where('standards.id', $selectedStandardId))
                                ->orWhereHas('student', fn ($st) => $st->where('standard_id', $selectedStandardId));
                        });
                    } else {
                        $query->whereRaw('1 = 0');
                    }
                }

                $teacherStudents = $query->with(['profile', 'student.standard', 'studentStandards'])
                    ->latest()
                    ->paginate(10)
                    ->appends($request->query());

                $teacherStudentsCount = User::where(function ($q) use ($teacherStandardIds) {
                    $q->whereHas('studentStandards', fn ($st) => $st->whereIn('standards.id', $teacherStandardIds))
                        ->orWhereHas('student', fn ($st) => $st->whereIn('standard_id', $teacherStandardIds));
                })->count();
            } else {
                $teacherStudents = new LengthAwarePaginator([], 0, 10);
                $teacherStudentsCount = 0;
            }

            $examQuery = Exam::query();
            if ($isAdmin) {
                if (! empty($teacherStandardIds)) {
                    $examQuery->whereHas('standards', function ($sub) use ($teacherStandardIds) {
                        $sub->whereIn('standards.id', $teacherStandardIds);
                    });
                }
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

        $teacherStudentPerformanceMap = [];
        if ($user->isTeacher() || $isAdmin) {
            $perfExamQuery = Exam::query();
            if ($isAdmin) {
                if (! empty($teacherStandardIds)) {
                    $perfExamQuery->whereHas('standards', function ($sub) use ($teacherStandardIds) {
                        $sub->whereIn('standards.id', $teacherStandardIds);
                    });
                }
            } else {
                $perfExamQuery->where('created_by', $user->id);
            }

            $allTeacherExamsList = $perfExamQuery->with(['questions.answers', 'standards'])->get();
            $allTeacherExamIds = $allTeacherExamsList->pluck('id')->toArray();

            $allPerfDetails = collect();
            if (! empty($allTeacherExamIds)) {
                $allPerfDetails = StudentExamDetail::whereIn('exam_id', $allTeacherExamIds)
                    ->with(['student.standard', 'student.user', 'question.answers', 'writtenAnswer'])
                    ->get();
            }

            $studentsToMap = $teacherStudents ? $teacherStudents->items() : [];
            foreach ($studentsToMap as $sUser) {
                $stId = $sUser->id;
                $stStandardId = $sUser->student?->standard_id;

                $relevantExams = $allTeacherExamsList->filter(function ($ex) use ($stStandardId, $user) {
                    if ($stStandardId && $ex->standards->pluck('id')->contains($stStandardId)) {
                        return true;
                    }

                    return $ex->created_by === $user->id;
                });

                $studentExamsReport = [];
                $completedCount = 0;
                $totalObtainedSum = 0;
                $totalMaxSum = 0;

                foreach ($relevantExams as $exam) {
                    $examTotalMark = $exam->total_mark > 0 ? $exam->total_mark : $exam->questions->sum('marks');
                    $studentExamDetails = $allPerfDetails->where('exam_id', $exam->id)->where('student_id', $stId);

                    if ($studentExamDetails->isNotEmpty()) {
                        $completedCount++;
                        $obtained = 0;
                        $qDetailsPayload = [];

                        foreach ($studentExamDetails as $d) {
                            $qMarks = $d->question?->marks ?? 0;
                            $isCorrect = $d->writtenAnswer && ((int) $d->writtenAnswer->is_correct === 1);
                            if ($isCorrect) {
                                $obtained += $qMarks;
                            }
                            $correctOption = $d->question?->answers?->firstWhere('is_correct', 1);
                            $qDetailsPayload[] = [
                                'question_name' => $d->question?->name ?? 'N/A',
                                'question_marks' => $qMarks,
                                'selected_answer' => $d->writtenAnswer?->name ?? 'No Answer Selected',
                                'is_correct' => $isCorrect,
                                'earned_marks' => $isCorrect ? $qMarks : 0,
                                'correct_answer' => $correctOption?->name ?? null,
                            ];
                        }

                        $totalObtainedSum += $obtained;
                        $totalMaxSum += $examTotalMark;
                        $pct = $examTotalMark > 0 ? (int) round(($obtained / $examTotalMark) * 100) : 0;

                        $studentExamsReport[] = [
                            'exam_id' => $exam->id,
                            'exam_name' => $exam->name,
                            'status' => 'Completed',
                            'obtained_mark' => $obtained,
                            'total_mark' => $examTotalMark,
                            'percentage' => $pct,
                            'questions_count' => $exam->questions->count(),
                            'details' => $qDetailsPayload,
                        ];
                    } else {
                        $studentExamsReport[] = [
                            'exam_id' => $exam->id,
                            'exam_name' => $exam->name,
                            'status' => 'Not Attempted',
                            'obtained_mark' => 0,
                            'total_mark' => $examTotalMark,
                            'percentage' => 0,
                            'questions_count' => $exam->questions->count(),
                            'details' => [],
                        ];
                    }
                }

                $overallPct = $totalMaxSum > 0 ? (int) round(($totalObtainedSum / $totalMaxSum) * 100) : 0;

                $teacherStudentPerformanceMap[$stId] = [
                    'student_id' => $stId,
                    'student_name' => $sUser->name,
                    'student_email' => $sUser->email,
                    'standard_name' => $sUser->student?->standard?->name ?? 'Unassigned',
                    'total_exams' => count($studentExamsReport),
                    'completed_exams' => $completedCount,
                    'overall_percentage' => $overallPct,
                    'total_obtained_marks' => $totalObtainedSum,
                    'total_possible_marks' => $totalMaxSum,
                    'exams' => $studentExamsReport,
                ];
            }
        }

        if ($user->canAssignExams()) {
            $standardsQuery = Standard::withCount('students')->with('creator.profile');

            if (! $isAdmin) {
                $standardsQuery->where(function ($q) use ($user) {
                    $q->where('created_by', $user->id)
                        ->orWhereHas('teachers', function ($tq) use ($user) {
                            $tq->where('users.id', $user->id);
                        });
                });
            }

            if ($request->filled('standards_search')) {
                $search = trim($request->input('standards_search'));
                $standardsQuery->where(function ($q) use ($search) {
                    $q->where('name', 'like', "%{$search}%")
                        ->orWhereHas('creator', fn ($cq) => $cq->where('name', 'like', "%{$search}%"));
                });
            }

            $standards = $standardsQuery->orderBy('id')->paginate(10, ['*'], 'standards_page')->appends($request->query());
        }

        if (! $isAdmin) {
            $allStandardsForSelect = Standard::where(function ($q) use ($user) {
                $q->where('created_by', $user->id)
                    ->orWhereHas('teachers', function ($tq) use ($user) {
                        $tq->where('users.id', $user->id);
                    });
            })->orderBy('name')->get();
        } else {
            $allStandardsForSelect = Standard::orderBy('name')->get();
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

                if (! $isAdmin) {
                    $tIds = isset($teacherStandardIds) ? $teacherStandardIds : [];
                    if (! empty($tIds)) {
                        $allStudentsQuery->whereHas('student', function ($q) use ($tIds) {
                            $q->whereIn('standard_id', $tIds);
                        });
                    } else {
                        $allStudentsQuery->whereRaw('1 = 0');
                    }
                }

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
            'teacherStudentPerformanceMap' => $teacherStudentPerformanceMap,
            'allStudents' => $allStudents,
            'allStandardsForSelect' => $allStandardsForSelect,
        ]);

    }
}
