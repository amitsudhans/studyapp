<?php

namespace App\Http\Controllers;

use App\Models\Exam;
use App\Models\Question;
use App\Models\Standard;
use App\Models\StudentExamDetail;
use App\Models\Subject;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use Illuminate\View\View;

class ExamController extends Controller
{
    /**
     * Display a listing of exams.
     */
    public function index(Request $request): View
    {
        $user = $request->user();

        $exams = Exam::with(['creator', 'questions.standard', 'questions.answers', 'standards'])
            ->withCount('studentExamDetails')
            ->latest()
            ->paginate(10);

        $availableQuestions = Question::with(['standard', 'subject', 'chapter', 'topic', 'answers', 'creator'])
            ->latest()
            ->get();

        if ($user && $user->isTeacher() && ! $user->isAdmin()) {
            $standards = Standard::where('created_by', $user->id)->orderBy('name')->get();
        } else {
            $standards = Standard::orderBy('name')->get();
        }

        $subjectsData = Subject::with(['chapters.topics'])->orderBy('name')->get();

        return view('exams.index', compact('exams', 'availableQuestions', 'standards', 'subjectsData'));
    }

    /**
     * Display details of a specific exam with question management options.
     */
    public function show(Exam $exam): View
    {
        $user = request()->user();
        $exam->load(['creator', 'questions.standard', 'questions.answers', 'standards']);
        $exam->loadCount('studentExamDetails');

        $attachedQuestionIds = $exam->questions->pluck('id')->toArray();

        $availableQuestions = Question::with(['standard', 'subject', 'chapter', 'topic', 'answers', 'creator'])
            ->whereNotIn('id', $attachedQuestionIds)
            ->latest()
            ->get();

        if ($user && $user->isTeacher() && ! $user->isAdmin()) {
            $standards = Standard::where('created_by', $user->id)->orderBy('name')->get();
        } else {
            $standards = Standard::orderBy('name')->get();
        }

        $subjectsData = Subject::with(['chapters.topics'])->orderBy('name')->get();

        return view('exams.show', compact('exam', 'availableQuestions', 'standards', 'subjectsData'));
    }

    /**
     * Store a newly created exam.
     */
    public function store(Request $request): RedirectResponse
    {
        $user = $request->user();

        $validated = $request->validate([
            'name' => ['required', 'string', 'max:255'],
            'type' => ['required', 'integer', 'in:1,2'],
            'duration' => ['nullable', 'required_if:type,1', 'integer', 'min:1', 'max:1440'],
            'status' => ['required', 'integer', 'in:1,2'],
            'question_ids' => ['nullable', 'array'],
            'question_ids.*' => ['integer', 'exists:questions,id'],
            'standard_ids' => ['nullable', 'array'],
            'standard_ids.*' => ['integer', 'exists:standards,id'],
            'assignment_status' => ['nullable', 'integer', 'in:1,2'],
        ]);

        if (! empty($validated['standard_ids'])) {
            if (! $user->canAssignExams()) {
                abort(403, 'Only teachers and administrators can assign exams to standards.');
            }

            if ($user->isTeacher() && ! $user->isAdmin()) {
                $requestedStdIds = array_unique($validated['standard_ids']);
                $allowedCount = Standard::whereIn('id', $requestedStdIds)
                    ->where('created_by', $user->id)
                    ->count();

                if ($allowedCount !== count($requestedStdIds)) {
                    return back()->withErrors(['standard_ids' => 'Teachers can only assign exams to standards created by them.']);
                }
            }
        }

        DB::transaction(function () use ($validated, $request) {
            $exam = Exam::create([
                'name' => $validated['name'],
                'type' => (int) $validated['type'],
                'duration' => (int) $validated['type'] === 1 ? (int) ($validated['duration'] ?? 0) : null,
                'status' => (int) $validated['status'],
                'created_by' => $request->user()->id,
                'total_mark' => 0,
            ]);

            if (! empty($validated['question_ids'])) {
                $syncData = [];
                foreach ($validated['question_ids'] as $qId) {
                    $syncData[$qId] = ['status' => 1];
                }
                $exam->questions()->sync($syncData);
            }

            if (! empty($validated['standard_ids']) && $request->user()->canAssignExams()) {
                $assignStatus = (int) ($validated['assignment_status'] ?? 1);
                $syncStandards = [];
                foreach ($validated['standard_ids'] as $stdId) {
                    $syncStandards[$stdId] = ['status' => $assignStatus];
                }
                $exam->standards()->sync($syncStandards);
            }

            $exam->recalculateTotalMarks();
        });

        return redirect()->route('exams.index')->with('status', 'Exam created successfully!');
    }

    /**
     * Update the specified exam details and linked questions.
     */
    public function update(Request $request, Exam $exam): RedirectResponse
    {
        $user = $request->user();

        if ($exam->studentExamDetails()->exists()) {
            return back()->withErrors(['name' => 'This exam cannot be modified because students have already taken it.']);
        }

        $validated = $request->validate([
            'name' => ['required', 'string', 'max:255'],
            'type' => ['required', 'integer', 'in:1,2'],
            'duration' => ['nullable', 'required_if:type,1', 'integer', 'min:1', 'max:1440'],
            'status' => ['required', 'integer', 'in:1,2'],
            'question_ids' => ['nullable', 'array'],
            'question_ids.*' => ['integer', 'exists:questions,id'],
            'standard_ids' => ['nullable', 'array'],
            'standard_ids.*' => ['integer', 'exists:standards,id'],
            'assignment_status' => ['nullable', 'integer', 'in:1,2'],
        ]);

        if (array_key_exists('standard_ids', $validated) && ! empty($validated['standard_ids'])) {
            if (! $user->canAssignExams()) {
                abort(403, 'Only teachers and administrators can assign exams to standards.');
            }

            if ($user->isTeacher() && ! $user->isAdmin()) {
                $requestedStdIds = array_unique($validated['standard_ids']);
                $allowedCount = Standard::whereIn('id', $requestedStdIds)
                    ->where('created_by', $user->id)
                    ->count();

                if ($allowedCount !== count($requestedStdIds)) {
                    return back()->withErrors(['standard_ids' => 'Teachers can only assign exams to standards created by them.']);
                }
            }
        }

        DB::transaction(function () use ($exam, $validated, $user) {
            $exam->update([
                'name' => $validated['name'],
                'type' => (int) $validated['type'],
                'duration' => (int) $validated['type'] === 1 ? (int) ($validated['duration'] ?? 0) : null,
                'status' => (int) $validated['status'],
            ]);

            if (array_key_exists('question_ids', $validated)) {
                $syncData = [];
                foreach ($validated['question_ids'] ?? [] as $qId) {
                    $syncData[$qId] = ['status' => 1];
                }
                $exam->questions()->sync($syncData);
            }

            if (array_key_exists('standard_ids', $validated) && $user->canAssignExams()) {
                $assignStatus = (int) ($validated['assignment_status'] ?? 1);
                $syncStandards = [];

                if ($user->isTeacher() && ! $user->isAdmin()) {
                    $myStdIds = Standard::where('created_by', $user->id)->pluck('id')->toArray();
                    $otherAssigned = $exam->standards()
                        ->whereNotIn('standards.id', $myStdIds)
                        ->get()
                        ->pluck('pivot.status', 'id')
                        ->toArray();

                    foreach ($validated['standard_ids'] ?? [] as $stdId) {
                        $syncStandards[$stdId] = ['status' => $assignStatus];
                    }
                    foreach ($otherAssigned as $stdId => $pStatus) {
                        $syncStandards[$stdId] = ['status' => (int) $pStatus];
                    }
                } else {
                    foreach ($validated['standard_ids'] ?? [] as $stdId) {
                        $syncStandards[$stdId] = ['status' => $assignStatus];
                    }
                }

                $exam->standards()->sync($syncStandards);
            }

            $exam->recalculateTotalMarks();
        });

        if ($request->has('_redirect_to_show')) {
            return redirect()->route('exams.show', $exam)->with('status', 'Exam details updated successfully!');
        }

        return redirect()->route('exams.index')->with('status', 'Exam updated successfully!');
    }

    /**
     * Remove the specified exam from storage.
     */
    public function destroy(Exam $exam): RedirectResponse
    {
        if ($exam->studentExamDetails()->exists()) {
            return back()->withErrors(['error' => 'This exam cannot be deleted because students have already taken it.']);
        }

        $exam->delete();

        return redirect()->route('exams.index')->with('status', 'Exam deleted successfully!');
    }

    /**
     * Assign exam to standard(s) via exam_assign table (Teachers & Admins).
     */
    public function assignStandards(Request $request, Exam $exam): RedirectResponse
    {
        $user = $request->user();

        if (! $user->canAssignExams()) {
            abort(403, 'Only teachers and administrators can assign exams to standards.');
        }

        $validated = $request->validate([
            'standard_ids' => ['nullable', 'array'],
            'standard_ids.*' => ['integer', 'exists:standards,id'],
            'status' => ['nullable', 'integer', 'in:1,2'],
        ]);

        $requestedStdIds = array_unique($validated['standard_ids'] ?? []);

        if ($user->isTeacher() && ! $user->isAdmin()) {
            if (! empty($requestedStdIds)) {
                $allowedCount = Standard::whereIn('id', $requestedStdIds)
                    ->where('created_by', $user->id)
                    ->count();

                if ($allowedCount !== count($requestedStdIds)) {
                    return back()->withErrors(['standard_ids' => 'Teachers can only assign exams to standards created by them.']);
                }
            }

            $myStdIds = Standard::where('created_by', $user->id)->pluck('id')->toArray();
            $otherAssigned = $exam->standards()
                ->whereNotIn('standards.id', $myStdIds)
                ->get()
                ->pluck('pivot.status', 'id')
                ->toArray();

            $status = (int) ($validated['status'] ?? 1);
            $syncData = [];
            foreach ($requestedStdIds as $stdId) {
                $syncData[$stdId] = ['status' => $status];
            }
            foreach ($otherAssigned as $stdId => $pStatus) {
                $syncData[$stdId] = ['status' => (int) $pStatus];
            }

            $exam->standards()->sync($syncData);
        } else {
            $status = (int) ($validated['status'] ?? 1);
            $syncData = [];
            foreach ($requestedStdIds as $stdId) {
                $syncData[$stdId] = ['status' => $status];
            }

            $exam->standards()->sync($syncData);
        }

        return back()->with('status', 'Exam assigned to standard(s) successfully!');
    }

    /**
     * Add question(s) from question bank to the exam.
     */
    public function addQuestions(Request $request, Exam $exam): RedirectResponse
    {
        if ($exam->studentExamDetails()->exists()) {
            return back()->withErrors(['error' => 'Cannot add questions to an exam that has already been taken by students.']);
        }

        $validated = $request->validate([
            'question_ids' => ['required', 'array', 'min:1'],
            'question_ids.*' => ['integer', 'exists:questions,id'],
        ]);

        $syncData = [];
        foreach ($validated['question_ids'] as $qId) {
            $syncData[$qId] = ['status' => 1];
        }

        $exam->questions()->syncWithoutDetaching($syncData);
        $exam->recalculateTotalMarks();

        return back()->with('status', 'Question(s) added to exam successfully!');
    }

    /**
     * Remove a question from the exam (deletes from exam_questions).
     */
    public function removeQuestion(Request $request, Exam $exam, Question $question): RedirectResponse
    {
        if ($exam->studentExamDetails()->exists()) {
            return back()->withErrors(['error' => 'Cannot remove questions from an exam that has already been taken by students.']);
        }

        $exam->questions()->detach($question->id);
        $exam->recalculateTotalMarks();

        return back()->with('status', 'Question removed from exam successfully!');
    }

    /**
     * Display the leaderboard for a specific exam.
     */
    public function leaderboard(Request $request, Exam $exam): View|JsonResponse
    {
        $currentUser = $request->user();
        $exam->load(['creator', 'questions.answers', 'standards']);

        $totalExamMarks = $exam->total_mark > 0 ? $exam->total_mark : $exam->questions->sum('marks');

        $allDetails = StudentExamDetail::where('exam_id', $exam->id)
            ->with(['student.standard', 'student.user', 'question.answers', 'writtenAnswer'])
            ->get();

        $studentGroups = $allDetails->groupBy('student_id');

        $rankings = [];
        $totalObtainedSum = 0;

        foreach ($studentGroups as $studentId => $details) {
            $studentObj = $details->first()->student;
            $studentName = $studentObj?->name ?? $studentObj?->user?->name ?? 'Student #'.$studentId;
            $studentEmail = $studentObj?->user?->email ?? '';
            $studentClass = $studentObj?->standard?->name ?? 'N/A';
            $submittedAt = $details->max('created_at');

            $obtainedMarks = 0;
            $correctCount = 0;
            $totalQuestions = $details->count();

            foreach ($details as $d) {
                $qMarks = $d->question?->marks ?? 0;
                $isCorrect = $d->writtenAnswer && ((int) $d->writtenAnswer->is_correct === 1);
                if ($isCorrect) {
                    $obtainedMarks += $qMarks;
                    $correctCount++;
                }
            }

            $totalObtainedSum += $obtainedMarks;
            $pct = $totalExamMarks > 0 ? (int) round(($obtainedMarks / $totalExamMarks) * 100) : 0;

            $isCurrentUser = ($currentUser && $currentUser->student && (int) $currentUser->student->id === (int) $studentId)
                             || ($currentUser && (int) $currentUser->id === (int) $studentId);

            $rankings[] = [
                'student_id' => $studentId,
                'student_name' => $studentName,
                'student_email' => $studentEmail,
                'student_class' => $studentClass,
                'obtained_marks' => $obtainedMarks,
                'total_marks' => $totalExamMarks,
                'correct_count' => $correctCount,
                'total_questions' => $totalQuestions,
                'percentage' => $pct,
                'submitted_at' => $submittedAt ? $submittedAt->format('M d, Y H:i') : null,
                'submitted_at_timestamp' => $submittedAt ? $submittedAt->timestamp : 0,
                'is_current_user' => $isCurrentUser,
            ];
        }

        // Sort: obtained_marks DESC, submitted_at_timestamp ASC
        usort($rankings, function ($a, $b) {
            if ($b['obtained_marks'] !== $a['obtained_marks']) {
                return $b['obtained_marks'] <=> $a['obtained_marks'];
            }

            return $a['submitted_at_timestamp'] <=> $b['submitted_at_timestamp'];
        });

        // Assign rank numbers (1, 2, 3...)
        foreach ($rankings as $index => &$item) {
            $item['rank'] = $index + 1;
        }
        unset($item);

        $totalSubmissions = count($rankings);
        $highestMarks = $totalSubmissions > 0 ? $rankings[0]['obtained_marks'] : 0;
        $averageMarks = $totalSubmissions > 0 ? (int) round($totalObtainedSum / $totalSubmissions) : 0;
        $topScorer = $totalSubmissions > 0 ? $rankings[0]['student_name'] : 'N/A';

        $summary = [
            'total_submissions' => $totalSubmissions,
            'highest_marks' => $highestMarks,
            'average_marks' => $averageMarks,
            'top_scorer' => $topScorer,
        ];

        if ($request->expectsJson() || $request->ajax()) {
            return response()->json([
                'exam' => [
                    'id' => $exam->id,
                    'name' => $exam->name,
                    'total_mark' => $totalExamMarks,
                    'questions_count' => $exam->questions->count(),
                    'standards' => $exam->standards->pluck('name')->toArray(),
                ],
                'summary' => $summary,
                'leaderboard' => $rankings,
            ]);
        }

        return view('exams.leaderboard', compact('exam', 'totalExamMarks', 'rankings', 'summary'));
    }
}
