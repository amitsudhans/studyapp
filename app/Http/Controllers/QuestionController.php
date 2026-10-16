<?php

namespace App\Http\Controllers;

use App\Models\Answer;
use App\Models\Chapter;
use App\Models\Question;
use App\Models\Standard;
use App\Models\Subject;
use App\Models\Syllabus;
use App\Models\Topic;
use App\Models\User;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use Illuminate\Validation\ValidationException;
use Illuminate\View\View;

class QuestionController extends Controller
{
    /**
     * Display a listing of questions with filter options and modal data.
     */
    public function index(Request $request): View
    {
        $query = Question::with(['standard.syllabus', 'subject.syllabus', 'chapter', 'topic', 'creator', 'answers'])->latest();

        if ($request->filled('search')) {
            $search = trim($request->search);
            $query->where(function ($q) use ($search) {
                // Search in question prompt, description, hint, and solution
                $q->where('name', 'like', "%{$search}%")
                    ->orWhere('description', 'like', "%{$search}%")
                    ->orWhere('hint', 'like', "%{$search}%")
                    ->orWhere('solution', 'like', "%{$search}%");

                // Numeric ID or question label search (e.g. 104, Q104, #104)
                if (is_numeric($search)) {
                    $q->orWhere('id', (int) $search);
                } elseif (preg_match('/^q?#?(\d+)$/i', $search, $matches)) {
                    $q->orWhere('id', (int) $matches[1]);
                }

                // Search in answer options and matching pairs
                $q->orWhereHas('answers', function ($aq) use ($search) {
                    $aq->where('name', 'like', "%{$search}%")
                        ->orWhere('match_answer', 'like', "%{$search}%");
                });

                // Search by creator name
                $q->orWhereHas('creator', function ($cq) use ($search) {
                    $cq->where('name', 'like', "%{$search}%");
                });

                // Search by syllabus name (via standard, subject, or chapter)
                $q->orWhereHas('standard.syllabus', function ($sylq) use ($search) {
                    $sylq->where('name', 'like', "%{$search}%");
                })->orWhereHas('subject.syllabus', function ($sylq) use ($search) {
                    $sylq->where('name', 'like', "%{$search}%");
                });

                // Search by standard/class name
                $q->orWhereHas('standard', function ($sq) use ($search) {
                    $sq->where('name', 'like', "%{$search}%");
                });

                // Search by subject, chapter, or topic name
                $q->orWhereHas('subject', function ($subq) use ($search) {
                    $subq->where('name', 'like', "%{$search}%");
                })->orWhereHas('chapter', function ($chq) use ($search) {
                    $chq->where('name', 'like', "%{$search}%");
                })->orWhereHas('topic', function ($tpq) use ($search) {
                    $tpq->where('name', 'like', "%{$search}%");
                });

                // Match question type keywords
                $searchLower = strtolower($search);
                if (str_contains($searchLower, 'single')) {
                    $q->orWhere('type', 1);
                }
                if (str_contains($searchLower, 'multiple') || str_contains($searchLower, 'multi')) {
                    $q->orWhere('type', 2);
                }
                if (str_contains($searchLower, 'text')) {
                    $q->orWhere('type', 3);
                }
                if (str_contains($searchLower, 'true') || str_contains($searchLower, 'false') || str_contains($searchLower, 't/f')) {
                    $q->orWhere('type', 4);
                }
                if (str_contains($searchLower, 'match')) {
                    $q->orWhere('type', 5);
                }
            });
        }

        if ($request->filled('syllabus_id')) {
            $query->where(function ($q) use ($request) {
                $q->whereHas('standard', function ($sq) use ($request) {
                    $sq->where('syllabus_id', $request->syllabus_id);
                })->orWhereHas('subject', function ($subq) use ($request) {
                    $subq->where('syllabus_id', $request->syllabus_id);
                })->orWhereHas('chapter', function ($chq) use ($request) {
                    $chq->where('syllabus_id', $request->syllabus_id);
                });
            });
        }

        if ($request->filled('type')) {
            $query->where('type', $request->type);
        }

        if ($request->filled('created_by')) {
            $query->where('created_by', $request->created_by);
        }

        if ($request->filled('standard_id')) {
            $query->where('standard_id', $request->standard_id);
        }

        if ($request->filled('subject_id')) {
            $query->where('subject_id', $request->subject_id);
        }

        if ($request->filled('chapter_id')) {
            $query->where('chapter_id', $request->chapter_id);
        }

        if ($request->filled('topic_id')) {
            $query->where('topic_id', $request->topic_id);
        }

        $questions = $query->paginate(10)->appends($request->query());

        $syllabuses = Syllabus::orderBy('name')->get();
        $standards = Standard::with('syllabus')->orderBy('name')->get();
        $subjects = Subject::orderBy('name')->get();
        $chapters = Chapter::orderBy('name')->get();
        $topics = Topic::orderBy('name')->get();
        $subjectsData = Subject::with(['chapters.topics'])->orderBy('name')->get();
        $creators = User::whereIn('id', Question::select('created_by')->distinct())->orderBy('name')->get();

        return view('questions.index', compact(
            'questions',
            'syllabuses',
            'standards',
            'subjects',
            'chapters',
            'topics',
            'subjectsData',
            'creators'
        ));
    }

    /**
     * Store a newly created question with answers.
     */
    public function store(Request $request): RedirectResponse
    {
        $validated = $request->validate([
            'name' => ['required', 'string', 'max:2000000'],
            'description' => ['nullable', 'string', 'max:2000'],
            'hint' => ['nullable', 'string', 'max:65535'],
            'solution' => ['nullable', 'string', 'max:65535'],
            'standard_id' => ['required', 'exists:standards,id'],
            'subject_id' => ['nullable', 'exists:subjects,id'],
            'chapter_id' => ['nullable', 'exists:chapters,id'],
            'topic_id' => ['nullable', 'exists:topics,id'],
            'type' => ['required', 'integer', 'in:1,2,3,4,5'],
            'marks' => ['required', 'integer', 'min:0'],
            'answers' => ['nullable', 'array', 'max:6'],
            'answers.*.name' => ['nullable', 'string', 'max:255'],
            'answers.*.match_answer' => ['nullable', 'string', 'max:255'],
            'answers.*.is_correct' => ['nullable', 'in:0,1'],
        ]);

        $this->validateAnswers($validated);

        DB::transaction(function () use ($validated, $request) {
            $question = Question::create([
                'name' => $validated['name'],
                'description' => $validated['description'] ?? null,
                'hint' => $validated['hint'] ?? null,
                'solution' => $validated['solution'] ?? null,
                'standard_id' => $validated['standard_id'],
                'subject_id' => $validated['subject_id'] ?? null,
                'chapter_id' => $validated['chapter_id'] ?? null,
                'topic_id' => $validated['topic_id'] ?? null,
                'type' => (int) $validated['type'],
                'marks' => (int) $validated['marks'],
                'created_by' => $request->user()->id,
                'status' => 1,
            ]);

            // Save answers if type is 1 (Single Option), 2 (Multiple Option), or 4 (True / False)
            if (in_array((int) $validated['type'], [1, 2, 4]) && ! empty($validated['answers'])) {
                $count = 0;
                foreach ($validated['answers'] as $ans) {
                    if (! empty(trim($ans['name'] ?? ''))) {
                        if ($count >= 4) {
                            break;
                        }
                        Answer::create([
                            'question_id' => $question->id,
                            'name' => trim($ans['name']),
                            'is_correct' => ! empty($ans['is_correct']) ? 1 : 0,
                            'status' => 1,
                        ]);
                        $count++;
                    }
                }
            } elseif ((int) $validated['type'] === 5 && ! empty($validated['answers'])) {
                $count = 0;
                foreach ($validated['answers'] as $ans) {
                    $left = trim($ans['name'] ?? '');
                    $right = trim($ans['match_answer'] ?? '');
                    if ($left !== '' && $right !== '') {
                        if ($count >= 6) {
                            break;
                        }
                        Answer::create([
                            'question_id' => $question->id,
                            'name' => $left,
                            'match_answer' => $right,
                            'is_correct' => 1,
                            'status' => 1,
                        ]);
                        $count++;
                    }
                }

                // 1 mark for each matching pair
                if ($count > 0) {
                    $question->update(['marks' => $count]);
                }
            }
        });

        return redirect()->route('questions.index')->with('status', 'Question created successfully!');
    }

    /**
     * Update the specified question and its answers.
     */
    public function update(Request $request, Question $question): RedirectResponse
    {
        $validated = $request->validate([
            'name' => ['required', 'string', 'max:2000000'],
            'description' => ['nullable', 'string', 'max:2000'],
            'hint' => ['nullable', 'string', 'max:65535'],
            'solution' => ['nullable', 'string', 'max:65535'],
            'standard_id' => ['required', 'exists:standards,id'],
            'subject_id' => ['nullable', 'exists:subjects,id'],
            'chapter_id' => ['nullable', 'exists:chapters,id'],
            'topic_id' => ['nullable', 'exists:topics,id'],
            'type' => ['required', 'integer', 'in:1,2,3,4,5'],
            'marks' => ['required', 'integer', 'min:0'],
            'answers' => ['nullable', 'array', 'max:6'],
            'answers.*.name' => ['nullable', 'string', 'max:255'],
            'answers.*.match_answer' => ['nullable', 'string', 'max:255'],
            'answers.*.is_correct' => ['nullable', 'in:0,1'],
        ]);

        $this->validateAnswers($validated);

        DB::transaction(function () use ($question, $validated) {
            $question->update([
                'name' => $validated['name'],
                'description' => $validated['description'] ?? null,
                'hint' => $validated['hint'] ?? null,
                'solution' => $validated['solution'] ?? null,
                'standard_id' => $validated['standard_id'],
                'subject_id' => $validated['subject_id'] ?? null,
                'chapter_id' => $validated['chapter_id'] ?? null,
                'topic_id' => $validated['topic_id'] ?? null,
                'type' => (int) $validated['type'],
                'marks' => (int) $validated['marks'],
            ]);

            // Remove existing answers and re-create updated answers
            $question->answers()->delete();

            if (in_array((int) $validated['type'], [1, 2, 4]) && ! empty($validated['answers'])) {
                $count = 0;
                foreach ($validated['answers'] as $ans) {
                    if (! empty(trim($ans['name'] ?? ''))) {
                        if ($count >= 4) {
                            break;
                        }
                        Answer::create([
                            'question_id' => $question->id,
                            'name' => trim($ans['name']),
                            'is_correct' => ! empty($ans['is_correct']) ? 1 : 0,
                            'status' => 1,
                        ]);
                        $count++;
                    }
                }
            } elseif ((int) $validated['type'] === 5 && ! empty($validated['answers'])) {
                $count = 0;
                foreach ($validated['answers'] as $ans) {
                    $left = trim($ans['name'] ?? '');
                    $right = trim($ans['match_answer'] ?? '');
                    if ($left !== '' && $right !== '') {
                        if ($count >= 6) {
                            break;
                        }
                        Answer::create([
                            'question_id' => $question->id,
                            'name' => $left,
                            'match_answer' => $right,
                            'is_correct' => 1,
                            'status' => 1,
                        ]);
                        $count++;
                    }
                }

                // 1 mark for each matching pair
                if ($count > 0) {
                    $question->update(['marks' => $count]);
                }
            }

            // Recalculate total marks for any attached exams
            foreach ($question->exams as $exam) {
                $exam->recalculateTotalMarks();
            }
        });

        return redirect()->route('questions.index')->with('status', 'Question updated successfully!');
    }

    /**
     * Remove the specified question from storage.
     */
    public function destroy(Question $question): RedirectResponse
    {
        $question->delete();

        return redirect()->route('questions.index')->with('status', 'Question deleted successfully!');
    }

    /**
     * Validate question answers according to question type rules.
     *
     * @param  array<string, mixed>  $validated
     *
     * @throws ValidationException
     */
    protected function validateAnswers(array $validated): void
    {
        $type = (int) ($validated['type'] ?? 3);

        if ($type === 5) {
            $rawAnswers = $validated['answers'] ?? [];
            $validPairsCount = 0;

            foreach ($rawAnswers as $ans) {
                $left = trim($ans['name'] ?? '');
                $right = trim($ans['match_answer'] ?? '');
                if ($left !== '' && $right !== '') {
                    $validPairsCount++;
                } elseif ($left !== '' || $right !== '') {
                    throw ValidationException::withMessages([
                        'answers' => ['Each match pair must have both a Left item and a Right match entered.'],
                    ]);
                }
            }

            if ($validPairsCount < 2) {
                throw ValidationException::withMessages([
                    'answers' => ['Match the Following questions must have at least 2 matching pairs.'],
                ]);
            }

            return;
        }

        if (in_array($type, [1, 2, 4])) {
            $rawAnswers = $validated['answers'] ?? [];
            $validAnswersCount = 0;
            $correctCount = 0;

            foreach ($rawAnswers as $ans) {
                $name = trim($ans['name'] ?? '');
                if ($name !== '') {
                    $validAnswersCount++;
                    if (! empty($ans['is_correct'])) {
                        $correctCount++;
                    }
                }
            }

            // Rule for True/False: At least 2 options ("True" & "False"), exactly 1 correct answer
            if ($type === 4) {
                if ($validAnswersCount < 2) {
                    throw ValidationException::withMessages([
                        'answers' => ['True / False questions must have both True and False answer options.'],
                    ]);
                }

                if ($correctCount !== 1) {
                    throw ValidationException::withMessages([
                        'answers' => ['True / False questions must have exactly ONE correct answer (either True or False) selected.'],
                    ]);
                }

                return;
            }

            // Rule 1: At least 2 non-empty answers required
            if ($validAnswersCount < 2) {
                throw ValidationException::withMessages([
                    'answers' => ['Single Option and Multiple Option questions must have at least 2 answer options entered.'],
                ]);
            }

            // Rule 2: Single option question must have exactly ONE correct answer
            if ($type === 1 && $correctCount !== 1) {
                throw ValidationException::withMessages([
                    'answers' => ['Single Option questions must have exactly ONE correct answer selected.'],
                ]);
            }

            // Rule 3: Multiple option question must have AT LEAST ONE correct answer
            if ($type === 2 && $correctCount < 1) {
                throw ValidationException::withMessages([
                    'answers' => ['Multiple Option questions must have at least ONE correct answer selected.'],
                ]);
            }
        }
    }
}
