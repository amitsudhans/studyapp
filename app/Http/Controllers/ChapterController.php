<?php

namespace App\Http\Controllers;

use App\Models\Chapter;
use App\Models\Standard;
use App\Models\Subject;
use App\Models\Syllabus;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\View\View;

class ChapterController extends Controller
{
    /**
     * Display chapters, optionally filtered by standard.
     */
    public function index(Request $request, ?Standard $standard = null): JsonResponse|View
    {
        $user = $request->user();
        if (! $user->canAssignExams()) {
            abort(403, 'Unauthorized access.');
        }

        $standardId = $standard?->id ?? $request->input('standard_id');

        $query = Chapter::with(['standard', 'subject', 'topics'])
            ->withCount('topics');

        if ($standardId) {
            $query->where('standard_id', $standardId);
        }

        if ($request->filled('subject_id')) {
            $query->where('subject_id', (int) $request->input('subject_id'));
        }

        if ($request->filled('search')) {
            $search = trim($request->input('search'));
            $query->where('name', 'like', "%{$search}%");
        }

        $chapters = $query->orderBy('name')->get();

        if ($request->wantsJson() || $request->ajax()) {
            return response()->json([
                'success' => true,
                'chapters' => $chapters,
            ]);
        }

        $standards = Standard::orderBy('name')->get();
        $subjects = Subject::orderBy('name')->get();

        return view('chapters.index', compact('chapters', 'standards', 'subjects', 'standard'));
    }

    /**
     * Store a newly created chapter inside a standard.
     */
    public function store(Request $request, ?Standard $standard = null): JsonResponse|RedirectResponse
    {
        $user = $request->user();
        if (! $user->canAssignExams()) {
            abort(403, 'Unauthorized access.');
        }

        $standardId = $standard?->id ?? $request->input('standard_id');

        $validated = $request->validate([
            'name' => ['required', 'string', 'max:255'],
            'standard_id' => [$standard ? 'nullable' : 'required', 'integer', 'exists:standards,id'],
            'subject_id' => ['nullable', 'integer', 'exists:subjects,id'],
            'syllabus_id' => ['nullable', 'integer', 'exists:syllabuses,id'],
        ]);

        $finalStandardId = $standardId ?: $validated['standard_id'];
        $std = $finalStandardId ? Standard::find($finalStandardId) : null;
        $syllabusId = $validated['syllabus_id'] ?? $std?->syllabus_id ?? Syllabus::first()?->id ?? 1;

        $chapter = Chapter::create([
            'name' => trim($validated['name']),
            'standard_id' => $finalStandardId,
            'subject_id' => $validated['subject_id'] ?? null,
            'syllabus_id' => $syllabusId,
        ]);

        $chapter->load(['standard', 'subject', 'topics']);
        $chapter->topics_count = 0;

        if ($request->wantsJson() || $request->ajax()) {
            return response()->json([
                'success' => true,
                'message' => 'Chapter created successfully!',
                'chapter' => $chapter,
            ]);
        }

        return back()->with('status', "Chapter '{$chapter->name}' created successfully!");
    }

    /**
     * Update the specified chapter.
     */
    public function update(Request $request, Chapter $chapter): JsonResponse|RedirectResponse
    {
        $user = $request->user();
        if (! $user->canAssignExams()) {
            abort(403, 'Unauthorized access.');
        }

        $validated = $request->validate([
            'name' => ['required', 'string', 'max:255'],
            'standard_id' => ['nullable', 'integer', 'exists:standards,id'],
            'subject_id' => ['nullable', 'integer', 'exists:subjects,id'],
        ]);

        $updateData = [
            'name' => trim($validated['name']),
        ];

        if (array_key_exists('standard_id', $validated)) {
            $updateData['standard_id'] = $validated['standard_id'];
        }

        if (array_key_exists('subject_id', $validated)) {
            $updateData['subject_id'] = $validated['subject_id'];
        }

        $chapter->update($updateData);
        $chapter->load(['standard', 'subject', 'topics']);
        $chapter->loadCount('topics');

        if ($request->wantsJson() || $request->ajax()) {
            return response()->json([
                'success' => true,
                'message' => 'Chapter updated successfully!',
                'chapter' => $chapter,
            ]);
        }

        return back()->with('status', "Chapter '{$chapter->name}' updated successfully!");
    }

    /**
     * Remove the specified chapter.
     */
    public function destroy(Request $request, Chapter $chapter): JsonResponse|RedirectResponse
    {
        $user = $request->user();
        if (! $user->canAssignExams()) {
            abort(403, 'Unauthorized access.');
        }

        $chapterName = $chapter->name;
        $chapter->topics()->delete();
        $chapter->delete();

        if ($request->wantsJson() || $request->ajax()) {
            return response()->json([
                'success' => true,
                'message' => "Chapter '{$chapterName}' deleted successfully!",
            ]);
        }

        return back()->with('status', "Chapter '{$chapterName}' deleted successfully!");
    }
}
