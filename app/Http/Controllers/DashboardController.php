<?php

namespace App\Http\Controllers;

use App\Models\Chapter;
use App\Models\Exam;
use App\Models\Standard;
use App\Models\StudentExamDetail;
use App\Models\Subject;
use App\Models\Syllabus;
use App\Models\Topic;
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
        $teacherExamList = null;
        $teacherExamSubmissions = collect();
        $studentAssignedCount = 0;
        $studentActiveCount = 0;
        $studentTotalMarks = 0;

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

            // Admin All Exams Query with Name & Curriculum Filters
            $adminExamQuery = Exam::query();
            if ($request->filled('exam_name')) {
                $name = trim($request->input('exam_name'));
                $adminExamQuery->where('name', 'like', "%{$name}%");
            }
            if ($request->filled('exam_type') || $request->filled('type')) {
                $typeVal = (int) ($request->input('exam_type') ?: $request->input('type'));
                $adminExamQuery->where('type', $typeVal);
            }
            if ($request->filled('exam_syllabus_id')) {
                $syllabusId = (int) $request->input('exam_syllabus_id');
                $adminExamQuery->where(function ($q) use ($syllabusId) {
                    $q->where('syllabus_id', $syllabusId)
                        ->orWhere(function ($sq) use ($syllabusId) {
                            $sq->whereNull('syllabus_id')
                                ->whereHas('standards', fn ($std) => $std->where('syllabus_id', $syllabusId));
                        });
                });
            }
            if ($request->filled('exam_subject_id')) {
                $adminExamQuery->where('subject_id', (int) $request->input('exam_subject_id'));
            }
            if ($request->filled('exam_chapter_id')) {
                $adminExamQuery->where('chapter_id', (int) $request->input('exam_chapter_id'));
            }
            if ($request->filled('exam_topic_id')) {
                $adminExamQuery->where('topic_id', (int) $request->input('exam_topic_id'));
            }

            $adminExams = $adminExamQuery->withCount('studentExamDetails')->with(['creator', 'questions.answers', 'standards', 'syllabus', 'standard', 'subject', 'chapter', 'topic'])
                ->latest()
                ->paginate(10, ['*'], 'admin_exams_page')
                ->appends($request->query());

            $totalExamsCount = Exam::count();
        } elseif ($isStudent) {
            $studentId = $user->student?->id ?? $user->id;
            $stdIds = $user->studentStandards->pluck('id')->merge(array_filter([$user->student?->standard_id]))->unique()->toArray();

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

            $studentExamsQuery = Exam::query();
            if (! empty($stdIds)) {
                $studentExamsQuery->whereHas('standards', function ($query) use ($stdIds) {
                    $query->whereIn('standards.id', $stdIds);
                });
            } else {
                $studentExamsQuery->whereRaw('1 = 0');
            }

            $allAssignedExams = (clone $studentExamsQuery)->get(['id', 'status', 'total_mark']);
            $studentAssignedCount = $allAssignedExams->count();
            $studentActiveCount = $allAssignedExams->filter(fn ($e) => (int) $e->status === 1 && ! in_array($e->id, $submittedExamIds))->count();
            $studentTotalMarks = $allAssignedExams->sum('total_mark');

            $pageName = $request->has('assigned_exams_page') ? 'assigned_exams_page' : 'page';
            $studentExams = $studentExamsQuery
                ->with(['creator', 'questions.standard', 'questions.answers', 'standards', 'syllabus', 'standard', 'subject', 'chapter', 'topic'])
                ->latest()
                ->paginate(10, ['*'], $pageName)
                ->appends($request->query());
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
            $examQuery->where('created_by', $user->id);

            // Curriculum & Name search for Teacher's exams
            if ($request->filled('exam_name')) {
                $name = trim($request->input('exam_name'));
                $examQuery->where('name', 'like', "%{$name}%");
            }
            if ($request->filled('exam_type') || $request->filled('type')) {
                $typeVal = (int) ($request->input('exam_type') ?: $request->input('type'));
                $examQuery->where('type', $typeVal);
            }
            if ($request->filled('exam_syllabus_id')) {
                $syllabusId = (int) $request->input('exam_syllabus_id');
                $examQuery->where(function ($q) use ($syllabusId) {
                    $q->where('syllabus_id', $syllabusId)
                        ->orWhere(function ($sq) use ($syllabusId) {
                            $sq->whereNull('syllabus_id')
                                ->whereHas('standards', fn ($std) => $std->where('syllabus_id', $syllabusId));
                        });
                });
            }
            if ($request->filled('exam_subject_id')) {
                $examQuery->where('subject_id', (int) $request->input('exam_subject_id'));
            }
            if ($request->filled('exam_chapter_id')) {
                $examQuery->where('chapter_id', (int) $request->input('exam_chapter_id'));
            }
            if ($request->filled('exam_topic_id')) {
                $examQuery->where('topic_id', (int) $request->input('exam_topic_id'));
            }

            $reportPageName = $request->has('exams_page') && ! $request->has('report_page') ? 'exams_page' : 'report_page';
            $teacherExams = (clone $examQuery)
                ->withCount('studentExamDetails')
                ->with(['creator', 'questions.answers', 'standards', 'syllabus', 'standard', 'subject', 'chapter', 'topic'])
                ->latest()
                ->paginate(10, ['*'], $reportPageName)
                ->appends($request->query());

            $teacherExamList = (clone $examQuery)
                ->withCount('studentExamDetails')
                ->with(['creator', 'questions.answers', 'standards', 'syllabus', 'standard', 'subject', 'chapter', 'topic'])
                ->latest()
                ->paginate(10, ['*'], 'exam_list_page')
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
                            $qMarks = $d->getQuestionMarks();
                            $isCorrect = $d->isCorrect();
                            $earnedMarks = $d->getEarnedMarks();
                            $obtained += $earnedMarks;

                            $qDetailsPayload[] = [
                                'question_name' => $d->question?->name ?? 'N/A',
                                'question_marks' => $qMarks,
                                'selected_answer' => $d->getSelectedAnswerDisplay(),
                                'is_correct' => $isCorrect,
                                'is_partially_correct' => $d->isPartiallyCorrect(),
                                'earned_marks' => $earnedMarks,
                                'correct_answer' => $d->getCorrectAnswerDisplay(),
                                'match_pairs' => $d->getMatchPairsReview(),
                                'hint' => $d->question?->hint,
                                'solution' => $d->question?->solution,
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
            $standardsQuery = Standard::withCount(['students', 'chapters'])
                ->with(['creator.profile', 'syllabus', 'chapters.topics', 'chapters.subject']);

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

        $syllabi = Syllabus::orderBy('name')->get();
        $syllabusesData = Syllabus::with(['standards', 'subjects.chapters.topics'])->orderBy('name')->get();
        $subjects = Subject::orderBy('name')->get();
        $chapters = Chapter::orderBy('name')->get();
        $topics = Topic::orderBy('name')->get();
        $subjectsData = Subject::with(['chapters.topics'])->orderBy('name')->get();

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
            'syllabusesData' => $syllabusesData,
            'subjects' => $subjects,
            'chapters' => $chapters,
            'topics' => $topics,
            'subjectsData' => $subjectsData,
            'studentExams' => $studentExams,
            'studentAssignedCount' => $studentAssignedCount,
            'studentActiveCount' => $studentActiveCount,
            'studentTotalMarks' => $studentTotalMarks,
            'submittedExamIds' => $submittedExamIds,
            'submittedDetails' => $submittedDetails,
            'totalUsersCount' => $totalUsersCount,
            'totalExamsCount' => $totalExamsCount ?? 0,
            'adminExams' => $adminExams ?? null,
            'teacherCount' => $teacherCount,
            'studentCount' => $studentCount,
            'adminCount' => $adminCount,
            'teacherStudents' => $teacherStudents,
            'teacherStudentsCount' => $teacherStudentsCount,
            'teacherExams' => $teacherExams,
            'teacherExamList' => $teacherExamList,
            'teacherExamSubmissions' => $teacherExamSubmissions,
            'teacherStudentPerformanceMap' => $teacherStudentPerformanceMap,
            'allStudents' => $allStudents,
            'allStandardsForSelect' => $allStandardsForSelect,
        ]);

    }
}
