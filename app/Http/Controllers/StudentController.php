<?php

namespace App\Http\Controllers;

use App\Models\Exam;
use App\Models\Standard;
use App\Models\StudentExamDetail;
use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Pagination\LengthAwarePaginator;
use Illuminate\View\View;

class StudentController extends Controller
{
    /**
     * Display a listing of students linked to classes with performance metrics.
     */
    public function index(Request $request): View
    {
        $user = $request->user();

        if (! $user->canAssignExams()) {
            abort(403, 'Unauthorized access to student directory.');
        }

        if ($user->isAdmin()) {
            $teacherStandards = Standard::orderBy('name')->get();
            $teacherStandardIds = $teacherStandards->pluck('id')->toArray();
        } else {
            $teacherStandards = $user->standards;
            $teacherStandardIds = $teacherStandards->pluck('id')->toArray();
        }

        if (! empty($teacherStandardIds)) {
            $studentBaseQuery = fn () => User::where(function ($q) {
                $q->whereHas('profile', fn ($p) => $p->where('type', 2))
                    ->orWhereHas('student');
            });

            $query = $studentBaseQuery();

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
            } else {
                $query->where(function ($q) use ($teacherStandardIds) {
                    $q->whereHas('studentStandards', fn ($st) => $st->whereIn('standards.id', $teacherStandardIds))
                        ->orWhereHas('student', fn ($st) => $st->whereIn('standard_id', $teacherStandardIds));
                });
            }

            $students = $query->with(['profile', 'student.standard', 'studentStandards'])
                ->latest()
                ->paginate(10)
                ->appends($request->query());

            $totalStudentsCount = $studentBaseQuery()->where(function ($q) use ($teacherStandardIds) {
                $q->whereHas('studentStandards', fn ($st) => $st->whereIn('standards.id', $teacherStandardIds))
                    ->orWhereHas('student', fn ($st) => $st->whereIn('standard_id', $teacherStandardIds));
            })->count();
        } else {
            $students = new LengthAwarePaginator([], 0, 10);
            $totalStudentsCount = 0;
        }

        // Student exam performance stats mapping
        $perfExamQuery = Exam::query();
        if ($user->isTeacher() && ! $user->isAdmin()) {
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

        $studentPerformanceMap = [];
        $studentsToMap = $students ? $students->items() : [];
        foreach ($studentsToMap as $sUser) {
            $stId = $sUser->id;
            $stStandardId = $sUser->student?->standard_id;

            $relevantExams = $allTeacherExamsList->filter(function ($ex) use ($stStandardId, $user) {
                if ($stStandardId && $ex->standards->pluck('id')->contains($stStandardId)) {
                    return true;
                }

                return $ex->created_by === $user->id;
            });

            $attemptedCount = 0;
            $totalEarnedMarks = 0;
            $totalPossibleMarks = 0;

            foreach ($relevantExams as $ex) {
                $stExamRows = $allPerfDetails->filter(fn ($d) => $d->student_id === $stId && $d->exam_id === $ex->id);
                if ($stExamRows->isNotEmpty()) {
                    $attemptedCount++;
                    $examMax = ($ex->questions->sum('marks') ?: $ex->questions->sum('mark')) ?: 1;
                    $earned = 0;
                    foreach ($stExamRows as $row) {
                        $earned += $row->getEarnedMarks();
                    }
                    $totalEarnedMarks += $earned;
                    $totalPossibleMarks += $examMax;
                }
            }

            $avgScore = $totalPossibleMarks > 0 ? round(($totalEarnedMarks / $totalPossibleMarks) * 100, 1) : null;

            $studentPerformanceMap[$stId] = [
                'relevant_exams_count' => $relevantExams->count(),
                'attempted_exams_count' => $attemptedCount,
                'avg_score' => $avgScore,
            ];
        }

        return view('students.index', compact(
            'students',
            'teacherStandards',
            'totalStudentsCount',
            'studentPerformanceMap'
        ));
    }
}
