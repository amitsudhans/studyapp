<?php

namespace App\Http\Controllers;

use App\Models\Chapter;
use App\Models\Exam;
use App\Models\Question;
use App\Models\Standard;
use App\Models\Student;
use App\Models\StudentExamDetail;
use App\Models\Subject;
use App\Models\Syllabus;
use App\Models\Topic;
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

        $examsQuery = Exam::with([
            'creator',
            'questions.standard',
            'questions.answers',
            'standards',
            'syllabus',
            'standard',
            'subject',
            'chapter',
            'topic',
        ])->withCount('studentExamDetails');

        if ($user && $user->isTeacher() && ! $user->isAdmin()) {
            $examsQuery->where('created_by', $user->id);
        }

        // Search by Exam Name
        if ($request->filled('name')) {
            $name = trim($request->input('name'));
            $examsQuery->where('name', 'like', "%{$name}%");
        }

        // Filter by Exam Type (1 - Timed, 2 - Non-Timed, 3 - Text Entry)
        if ($request->filled('type')) {
            $examsQuery->where('type', (int) $request->input('type'));
        }

        // Filter by Syllabus
        if ($request->filled('syllabus_id')) {
            $syllabusId = (int) $request->input('syllabus_id');
            $examsQuery->where(function ($q) use ($syllabusId) {
                $q->where('syllabus_id', $syllabusId)
                    ->orWhere(function ($sq) use ($syllabusId) {
                        $sq->whereNull('syllabus_id')
                            ->whereHas('standards', fn ($std) => $std->where('syllabus_id', $syllabusId));
                    });
            });
        }

        // Filter by Subject (Strictly match the exam's assigned subject)
        if ($request->filled('subject_id')) {
            $examsQuery->where('subject_id', (int) $request->input('subject_id'));
        }

        // Filter by Chapter (Strictly match the exam's assigned chapter)
        if ($request->filled('chapter_id')) {
            $examsQuery->where('chapter_id', (int) $request->input('chapter_id'));
        }

        // Filter by Topic (Strictly match the exam's assigned topic)
        if ($request->filled('topic_id')) {
            $examsQuery->where('topic_id', (int) $request->input('topic_id'));
        }

        $exams = $examsQuery->latest()->paginate(10)->appends($request->query());

        $examIds = $exams->pluck('id')->toArray();
        $examSubmissions = collect();
        if (! empty($examIds)) {
            $allDetails = StudentExamDetail::whereIn('exam_id', $examIds)
                ->with(['student.standard', 'student.user', 'question.answers', 'writtenAnswer'])
                ->get();

            $examSubmissions = $allDetails->groupBy('exam_id')->map(function ($examGroup) {
                return $examGroup->groupBy('student_id');
            });
        }

        $availableQuestions = Question::with(['standard', 'subject', 'chapter', 'topic', 'answers', 'creator'])
            ->latest()
            ->get();

        if ($user && $user->isTeacher() && ! $user->isAdmin()) {
            $standards = Standard::where(function ($q) use ($user) {
                $q->where('created_by', $user->id)
                    ->orWhereHas('teachers', fn ($tq) => $tq->where('users.id', $user->id));
            })->orderBy('name')->get();
        } else {
            $standards = Standard::orderBy('name')->get();
        }

        $allStandardsForSelect = $standards;
        $syllabi = Syllabus::orderBy('name')->get();
        $syllabuses = $syllabi;
        $syllabusesData = Syllabus::with(['standards', 'subjects.chapters.topics'])->orderBy('name')->get();
        $subjects = Subject::orderBy('name')->get();
        $chapters = Chapter::orderBy('name')->get();
        $topics = Topic::orderBy('name')->get();
        $subjectsData = Subject::with(['chapters.topics'])->orderBy('name')->get();

        return view('exams.index', compact(
            'exams',
            'examSubmissions',
            'availableQuestions',
            'standards',
            'allStandardsForSelect',
            'syllabuses',
            'syllabi',
            'syllabusesData',
            'subjects',
            'chapters',
            'topics',
            'subjectsData'
        ));
    }

    /**
     * Display details of a specific exam with question management options.
     */
    public function show(Exam $exam): View
    {
        $user = request()->user();

        if ($user && $user->isTeacher() && ! $user->isAdmin() && (int) $exam->created_by !== (int) $user->id) {
            abort(403, 'Teachers can only view exams created by themselves.');
        }
        $exam->load([
            'creator',
            'questions.standard',
            'questions.answers',
            'standards',
            'syllabus',
            'standard',
            'subject',
            'chapter',
            'topic',
        ]);
        $exam->loadCount('studentExamDetails');

        $attachedQuestionIds = $exam->questions->pluck('id')->toArray();

        $availableQuestionsQuery = Question::with(['standard', 'subject', 'chapter', 'topic', 'answers', 'creator'])
            ->whereNotIn('id', $attachedQuestionIds);

        if ((int) $exam->type === 3) {
            $availableQuestionsQuery->where('type', 3);
        } else {
            $availableQuestionsQuery->where('type', '!=', 3);
        }

        $availableQuestions = $availableQuestionsQuery->latest()->get();

        if ($user && $user->isTeacher() && ! $user->isAdmin()) {
            $standards = Standard::where(function ($q) use ($user) {
                $q->where('created_by', $user->id)
                    ->orWhereHas('teachers', fn ($tq) => $tq->where('users.id', $user->id));
            })->orderBy('name')->get();
        } else {
            $standards = Standard::orderBy('name')->get();
        }

        $syllabuses = Syllabus::orderBy('name')->get();
        $syllabusesData = Syllabus::with(['standards', 'subjects.chapters.topics'])->orderBy('name')->get();
        $subjects = Subject::orderBy('name')->get();
        $chapters = Chapter::orderBy('name')->get();
        $topics = Topic::orderBy('name')->get();
        $subjectsData = Subject::with(['chapters.topics'])->orderBy('name')->get();

        return view('exams.show', compact(
            'exam',
            'availableQuestions',
            'standards',
            'syllabuses',
            'syllabusesData',
            'subjects',
            'chapters',
            'topics',
            'subjectsData'
        ));
    }

    /**
     * Store a newly created exam.
     */
    public function store(Request $request): RedirectResponse
    {
        $user = $request->user();

        $validated = $request->validate([
            'name' => ['required', 'string', 'max:255'],
            'type' => ['required', 'integer', 'in:1,2,3'],
            'duration' => ['nullable', 'required_if:type,1', 'integer', 'min:1', 'max:1440'],
            'status' => ['required', 'integer', 'in:1,2'],
            'syllabus_id' => ['nullable', 'exists:syllabuses,id'],
            'standard_id' => ['nullable', 'exists:standards,id'],
            'subject_id' => ['nullable', 'exists:subjects,id'],
            'chapter_id' => ['nullable', 'exists:chapters,id'],
            'topic_id' => ['nullable', 'exists:topics,id'],
            'question_ids' => ['nullable', 'array'],
            'question_ids.*' => ['integer', 'exists:questions,id'],
            'standard_ids' => ['nullable', 'array'],
            'standard_ids.*' => ['integer', 'exists:standards,id'],
            'assignment_status' => ['nullable', 'integer', 'in:1,2'],
        ]);

        if (! empty($validated['question_ids'])) {
            $selectedQuestions = Question::whereIn('id', $validated['question_ids'])->get();
            $examType = (int) $validated['type'];

            if ($examType === 3) {
                if ($selectedQuestions->contains(fn ($q) => (int) $q->type !== 3)) {
                    return back()->withErrors(['question_ids' => 'Only Text Entry questions can be added to a Text Entry type exam.'])->withInput();
                }
            } else {
                if ($selectedQuestions->contains(fn ($q) => (int) $q->type === 3)) {
                    return back()->withErrors(['question_ids' => 'Text Entry questions can only be added to Text Entry type exams.'])->withInput();
                }
            }
        }

        $requestedStdIds = array_map('intval', $validated['standard_ids'] ?? []);
        if (! empty($validated['standard_id']) && ! in_array((int) $validated['standard_id'], $requestedStdIds)) {
            $requestedStdIds[] = (int) $validated['standard_id'];
        }

        if (! empty($requestedStdIds)) {
            if (! $user->canAssignExams()) {
                abort(403, 'Only teachers and administrators can assign exams to standards.');
            }

            if ($user->isTeacher() && ! $user->isAdmin()) {
                $uniqueStdIds = array_unique($requestedStdIds);
                $allowedCount = Standard::whereIn('id', $uniqueStdIds)
                    ->where(function ($q) use ($user) {
                        $q->where('created_by', $user->id)
                            ->orWhereHas('teachers', fn ($tq) => $tq->where('users.id', $user->id));
                    })
                    ->count();

                if ($allowedCount !== count($uniqueStdIds)) {
                    return back()->withErrors(['standard_id' => 'Teachers can only select/assign standards assigned to them.']);
                }
            }
        }

        DB::transaction(function () use ($validated, $request, $requestedStdIds) {
            $exam = Exam::create([
                'name' => $validated['name'],
                'type' => (int) $validated['type'],
                'duration' => (int) $validated['type'] === 1 ? (int) ($validated['duration'] ?? 0) : null,
                'status' => (int) $validated['status'],
                'syllabus_id' => ! empty($validated['syllabus_id']) ? (int) $validated['syllabus_id'] : null,
                'standard_id' => ! empty($validated['standard_id']) ? (int) $validated['standard_id'] : null,
                'subject_id' => ! empty($validated['subject_id']) ? (int) $validated['subject_id'] : null,
                'chapter_id' => ! empty($validated['chapter_id']) ? (int) $validated['chapter_id'] : null,
                'topic_id' => ! empty($validated['topic_id']) ? (int) $validated['topic_id'] : null,
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

            $finalStdIds = array_unique($requestedStdIds);
            if (! empty($finalStdIds) && $request->user()->canAssignExams()) {
                $assignStatus = (int) ($validated['assignment_status'] ?? 1);
                $syncStandards = [];
                foreach ($finalStdIds as $stdId) {
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

        if ($user && $user->isTeacher() && ! $user->isAdmin() && (int) $exam->created_by !== (int) $user->id) {
            abort(403, 'Teachers can only modify exams created by themselves.');
        }

        if ($exam->studentExamDetails()->exists()) {
            return back()->withErrors(['name' => 'This exam cannot be modified because students have already taken it.']);
        }

        $validated = $request->validate([
            'name' => ['required', 'string', 'max:255'],
            'type' => ['required', 'integer', 'in:1,2,3'],
            'duration' => ['nullable', 'required_if:type,1', 'integer', 'min:1', 'max:1440'],
            'status' => ['required', 'integer', 'in:1,2'],
            'syllabus_id' => ['nullable', 'exists:syllabuses,id'],
            'standard_id' => ['nullable', 'exists:standards,id'],
            'subject_id' => ['nullable', 'exists:subjects,id'],
            'chapter_id' => ['nullable', 'exists:chapters,id'],
            'topic_id' => ['nullable', 'exists:topics,id'],
            'question_ids' => ['nullable', 'array'],
            'question_ids.*' => ['integer', 'exists:questions,id'],
            'standard_ids' => ['nullable', 'array'],
            'standard_ids.*' => ['integer', 'exists:standards,id'],
            'assignment_status' => ['nullable', 'integer', 'in:1,2'],
        ]);

        $examType = (int) $validated['type'];
        if (array_key_exists('question_ids', $validated)) {
            if (! empty($validated['question_ids'])) {
                $selectedQuestions = Question::whereIn('id', $validated['question_ids'])->get();
                if ($examType === 3) {
                    if ($selectedQuestions->contains(fn ($q) => (int) $q->type !== 3)) {
                        return back()->withErrors(['question_ids' => 'Only Text Entry questions can be added to a Text Entry type exam.'])->withInput();
                    }
                } else {
                    if ($selectedQuestions->contains(fn ($q) => (int) $q->type === 3)) {
                        return back()->withErrors(['question_ids' => 'Text Entry questions can only be added to Text Entry type exams.'])->withInput();
                    }
                }
            }
        } else {
            $existingQuestions = $exam->questions;
            if ($existingQuestions->isNotEmpty()) {
                if ($examType === 3) {
                    if ($existingQuestions->contains(fn ($q) => (int) $q->type !== 3)) {
                        return back()->withErrors(['type' => 'Cannot change exam type to Text Entry because it contains non-Text-Entry questions.'])->withInput();
                    }
                } else {
                    if ($existingQuestions->contains(fn ($q) => (int) $q->type === 3)) {
                        return back()->withErrors(['type' => 'Cannot change exam type to Timed/Non-Timed because it contains Text Entry questions.'])->withInput();
                    }
                }
            }
        }

        $requestedStdIds = array_map('intval', $validated['standard_ids'] ?? []);
        if (! empty($validated['standard_id']) && ! in_array((int) $validated['standard_id'], $requestedStdIds)) {
            $requestedStdIds[] = (int) $validated['standard_id'];
        }

        if (! empty($requestedStdIds)) {
            if (! $user->canAssignExams()) {
                abort(403, 'Only teachers and administrators can assign exams to standards.');
            }

            if ($user->isTeacher() && ! $user->isAdmin()) {
                $uniqueStdIds = array_unique($requestedStdIds);
                $allowedCount = Standard::whereIn('id', $uniqueStdIds)
                    ->where(function ($q) use ($user) {
                        $q->where('created_by', $user->id)
                            ->orWhereHas('teachers', fn ($tq) => $tq->where('users.id', $user->id));
                    })
                    ->count();

                if ($allowedCount !== count($uniqueStdIds)) {
                    return back()->withErrors(['standard_id' => 'Teachers can only select/assign standards assigned to them.']);
                }
            }
        }

        DB::transaction(function () use ($exam, $validated, $user, $requestedStdIds) {
            $examData = [
                'name' => $validated['name'],
                'type' => (int) $validated['type'],
                'duration' => (int) $validated['type'] === 1 ? (int) ($validated['duration'] ?? 0) : null,
                'status' => (int) $validated['status'],
            ];

            if (array_key_exists('syllabus_id', $validated)) {
                $examData['syllabus_id'] = ! empty($validated['syllabus_id']) ? (int) $validated['syllabus_id'] : null;
            }
            if (array_key_exists('standard_id', $validated)) {
                $examData['standard_id'] = ! empty($validated['standard_id']) ? (int) $validated['standard_id'] : null;
            }
            if (array_key_exists('subject_id', $validated)) {
                $examData['subject_id'] = ! empty($validated['subject_id']) ? (int) $validated['subject_id'] : null;
            }
            if (array_key_exists('chapter_id', $validated)) {
                $examData['chapter_id'] = ! empty($validated['chapter_id']) ? (int) $validated['chapter_id'] : null;
            }
            if (array_key_exists('topic_id', $validated)) {
                $examData['topic_id'] = ! empty($validated['topic_id']) ? (int) $validated['topic_id'] : null;
            }

            $exam->update($examData);

            if (array_key_exists('question_ids', $validated)) {
                $syncData = [];
                foreach ($validated['question_ids'] ?? [] as $qId) {
                    $syncData[$qId] = ['status' => 1];
                }
                $exam->questions()->sync($syncData);
            }

            if ((array_key_exists('standard_ids', $validated) || array_key_exists('standard_id', $validated)) && $user->canAssignExams()) {
                $assignStatus = (int) ($validated['assignment_status'] ?? 1);
                $syncStandards = [];

                $selectedStds = array_unique($requestedStdIds);

                if ($user->isTeacher() && ! $user->isAdmin()) {
                    $myStdIds = Standard::where(function ($q) use ($user) {
                        $q->where('created_by', $user->id)
                            ->orWhereHas('teachers', fn ($tq) => $tq->where('users.id', $user->id));
                    })->pluck('id')->toArray();
                    $otherAssigned = $exam->standards()
                        ->whereNotIn('standards.id', $myStdIds)
                        ->get()
                        ->pluck('pivot.status', 'id')
                        ->toArray();

                    foreach ($selectedStds as $stdId) {
                        $syncStandards[$stdId] = ['status' => $assignStatus];
                    }
                    foreach ($otherAssigned as $stdId => $pStatus) {
                        $syncStandards[$stdId] = ['status' => (int) $pStatus];
                    }
                } else {
                    foreach ($selectedStds as $stdId) {
                        $syncStandards[$stdId] = ['status' => $assignStatus];
                    }
                }

                $exam->standards()->sync($syncStandards);
            }

            $exam->recalculateTotalMarks();
        });

        if ($request->has('_redirect_to_dashboard')) {
            return redirect()->route('dashboard')->with('status', 'Exam updated successfully!');
        }

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
        $user = request()->user();
        if ($user && $user->isTeacher() && ! $user->isAdmin() && (int) $exam->created_by !== (int) $user->id) {
            abort(403, 'Teachers can only delete exams created by themselves.');
        }

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

        $selectedQuestions = Question::whereIn('id', $validated['question_ids'])->get();
        if ((int) $exam->type === 3) {
            if ($selectedQuestions->contains(fn ($q) => (int) $q->type !== 3)) {
                return back()->withErrors(['error' => 'Only Text Entry questions can be added to a Text Entry exam.']);
            }
        } else {
            if ($selectedQuestions->contains(fn ($q) => (int) $q->type === 3)) {
                return back()->withErrors(['error' => 'Text Entry questions can only be added to Text Entry type exams.']);
            }
        }

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
                $obtainedMarks += $d->getEarnedMarks();
                if ($d->isCorrect()) {
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

    /**
     * Evaluate and award marks/feedback for a student's text entry exam submission.
     * ONLY permitted for Text Entry exams (type === 3).
     */
    public function evaluateTextEntrySubmission(Request $request, Exam $exam, Student $student): JsonResponse|RedirectResponse
    {
        $user = $request->user();

        // 1. Strict restriction: Only for text entry exams!
        if ((int) $exam->type !== 3) {
            if ($request->expectsJson() || $request->ajax()) {
                return response()->json([
                    'success' => false,
                    'message' => 'Manual marks evaluation can only be performed for Text Entry type exams.',
                ], 422);
            }
            abort(403, 'Manual marks evaluation can only be performed for Text Entry type exams.');
        }

        // 2. Authorization: Teacher who created the exam or Admin
        $isTeacher = $user && $user->isTeacher();
        $isAdmin = $user && $user->isAdmin();

        if (! $isTeacher && ! $isAdmin) {
            abort(403, 'Unauthorized. Only teachers and administrators can evaluate exams.');
        }

        if ($isTeacher && ! $isAdmin && (int) $exam->created_by !== (int) $user->id) {
            abort(403, 'You can only evaluate submissions for exams created by yourself.');
        }

        // 3. Validation: marks and feedback arrays
        $validated = $request->validate([
            'marks' => ['required', 'array'],
            'marks.*' => ['nullable', 'numeric', 'min:0'],
            'feedback' => ['nullable', 'array'],
            'feedback.*' => ['nullable', 'string', 'max:2000'],
        ]);

        $marksInput = $validated['marks'];
        $feedbackInput = $validated['feedback'] ?? [];

        // 4. Fetch the details for this student & exam
        $details = StudentExamDetail::where('exam_id', $exam->id)
            ->where('student_id', $student->id)
            ->with('question')
            ->get();

        if ($details->isEmpty()) {
            if ($request->expectsJson() || $request->ajax()) {
                return response()->json([
                    'success' => false,
                    'message' => 'No submission records found for this student on this exam.',
                ], 404);
            }

            return back()->with('error', 'No submission records found for this student on this exam.');
        }

        // 5. Update each detail
        DB::transaction(function () use ($details, $marksInput, $feedbackInput) {
            foreach ($details as $detail) {
                // Must be a text entry question
                if ((int) ($detail->question?->type ?? 0) !== 3) {
                    continue;
                }

                $detailId = $detail->id;
                if (! array_key_exists($detailId, $marksInput) && ! array_key_exists((string) $detailId, $marksInput)) {
                    continue;
                }

                $rawMark = $marksInput[$detailId] ?? $marksInput[(string) $detailId];
                $maxMarks = (int) ($detail->question?->marks ?? 0);

                $awardedMark = null;
                if ($rawMark !== null && $rawMark !== '') {
                    $parsed = (int) round((float) $rawMark);
                    $awardedMark = max(0, $maxMarks > 0 ? min($parsed, $maxMarks) : $parsed);
                }

                $feedback = $feedbackInput[$detailId] ?? $feedbackInput[(string) $detailId] ?? null;
                $feedback = $feedback !== null && trim((string) $feedback) !== '' ? trim((string) $feedback) : null;

                $detail->update([
                    'teacher_marks' => $awardedMark,
                    'teacher_feedback' => $feedback,
                ]);
            }
        });

        // 6. Reload updated details and recalculate totals
        $details->each->refresh();
        $totalObtained = 0;
        $totalExamMarks = $exam->total_mark > 0 ? $exam->total_mark : $exam->questions->sum('marks');

        $updatedDetails = $details->map(function ($d) use (&$totalObtained) {
            $earnedMarks = $d->getEarnedMarks();
            $totalObtained += $earnedMarks;

            return [
                'id' => $d->id,
                'question_id' => $d->question_id,
                'earned_marks' => $earnedMarks,
                'teacher_marks' => $d->teacher_marks,
                'teacher_feedback' => $d->teacher_feedback,
                'is_evaluated' => $d->isEvaluated(),
                'is_correct' => $d->isCorrect(),
                'is_partially_correct' => $d->isPartiallyCorrect(),
            ];
        });

        $pct = $totalExamMarks > 0 ? (int) round(($totalObtained / $totalExamMarks) * 100) : 0;

        if ($request->expectsJson() || $request->ajax()) {
            return response()->json([
                'success' => true,
                'message' => 'Marks and feedback successfully saved for this student.',
                'obtained_mark' => $totalObtained,
                'total_mark' => $totalExamMarks,
                'percentage' => $pct,
                'details' => $updatedDetails,
            ]);
        }

        return back()->with('status', 'Student submission evaluated successfully.');
    }
}
