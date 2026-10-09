<?php

namespace App\Http\Controllers;

use App\Models\Answer;
use App\Models\Chapter;
use App\Models\Question;
use App\Models\Standard;
use App\Models\Subject;
use App\Models\Topic;
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
        $query = Question::with(['standard', 'subject', 'chapter', 'topic', 'creator', 'answers'])->latest();

        if ($request->filled('search')) {
            $search = $request->search;
            $query->where(function ($q) use ($search) {
                $q->where('name', 'like', "%{$search}%")
                    ->orWhere('description', 'like', "%{$search}%");
            });
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

        $standards = Standard::orderBy('name')->get();
        $subjects = Subject::orderBy('name')->get();
        $chapters = Chapter::orderBy('name')->get();
        $topics = Topic::orderBy('name')->get();
        $subjectsData = Subject::with(['chapters.topics'])->orderBy('name')->get();

        return view('questions.index', compact(
            'questions',
            'standards',
            'subjects',
            'chapters',
            'topics',
            'subjectsData'
        ));
    }

    /**
     * Store a newly created question with answers.
     */
    public function store(Request $request): RedirectResponse
    {
        $validated = $request->validate([
            'name' => ['required', 'string', 'max:255'],
            'description' => ['nullable', 'string', 'max:2000'],
            'standard_id' => ['required', 'exists:standards,id'],
            'subject_id' => ['nullable', 'exists:subjects,id'],
            'chapter_id' => ['nullable', 'exists:chapters,id'],
            'topic_id' => ['nullable', 'exists:topics,id'],
            'type' => ['required', 'integer', 'in:1,2,3'],
            'marks' => ['required', 'integer', 'min:0'],
            'answers' => ['nullable', 'array', 'max:4'],
            'answers.*.name' => ['nullable', 'string', 'max:255'],
            'answers.*.is_correct' => ['nullable', 'in:0,1'],
        ]);

        $this->validateAnswers($validated);

        DB::transaction(function () use ($validated, $request) {
            $question = Question::create([
                'name' => $validated['name'],
                'description' => $validated['description'] ?? null,
                'standard_id' => $validated['standard_id'],
                'subject_id' => $validated['subject_id'] ?? null,
                'chapter_id' => $validated['chapter_id'] ?? null,
                'topic_id' => $validated['topic_id'] ?? null,
                'type' => (int) $validated['type'],
                'marks' => (int) $validated['marks'],
                'created_by' => $request->user()->id,
                'status' => 1,
            ]);

            // Save answers if type is 1 (Single Option) or 2 (Multiple Option)
            if (in_array((int) $validated['type'], [1, 2]) && ! empty($validated['answers'])) {
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
            'name' => ['required', 'string', 'max:255'],
            'description' => ['nullable', 'string', 'max:2000'],
            'standard_id' => ['required', 'exists:standards,id'],
            'subject_id' => ['nullable', 'exists:subjects,id'],
            'chapter_id' => ['nullable', 'exists:chapters,id'],
            'topic_id' => ['nullable', 'exists:topics,id'],
            'type' => ['required', 'integer', 'in:1,2,3'],
            'marks' => ['required', 'integer', 'min:0'],
            'answers' => ['nullable', 'array', 'max:4'],
            'answers.*.name' => ['nullable', 'string', 'max:255'],
            'answers.*.is_correct' => ['nullable', 'in:0,1'],
        ]);

        $this->validateAnswers($validated);

        DB::transaction(function () use ($question, $validated) {
            $question->update([
                'name' => $validated['name'],
                'description' => $validated['description'] ?? null,
                'standard_id' => $validated['standard_id'],
                'subject_id' => $validated['subject_id'] ?? null,
                'chapter_id' => $validated['chapter_id'] ?? null,
                'topic_id' => $validated['topic_id'] ?? null,
                'type' => (int) $validated['type'],
                'marks' => (int) $validated['marks'],
            ]);

            // Remove existing answers and re-create updated answers if type is 1 or 2
            $question->answers()->delete();

            if (in_array((int) $validated['type'], [1, 2]) && ! empty($validated['answers'])) {
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

        if (in_array($type, [1, 2])) {
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
