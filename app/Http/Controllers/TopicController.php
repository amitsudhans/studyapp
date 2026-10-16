<?php

namespace App\Http\Controllers;

use App\Models\Chapter;
use App\Models\Topic;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;

class TopicController extends Controller
{
    /**
     * Display topics, optionally filtered by chapter.
     */
    public function index(Request $request, ?Chapter $chapter = null): JsonResponse
    {
        $user = $request->user();
        if (! $user->canAssignExams()) {
            abort(403, 'Unauthorized access.');
        }

        $chapterId = $chapter?->id ?? $request->input('chapter_id');

        $query = Topic::with('chapter');

        if ($chapterId) {
            $query->where('chapter_id', $chapterId);
        }

        if ($request->filled('search')) {
            $search = trim($request->input('search'));
            $query->where('name', 'like', "%{$search}%");
        }

        $topics = $query->orderBy('name')->get();

        return response()->json([
            'success' => true,
            'topics' => $topics,
        ]);
    }

    /**
     * Store a newly created topic inside a chapter.
     */
    public function store(Request $request, ?Chapter $chapter = null): JsonResponse|RedirectResponse
    {
        $user = $request->user();
        if (! $user->canAssignExams()) {
            abort(403, 'Unauthorized access.');
        }

        $chapterId = $chapter?->id ?? $request->input('chapter_id');

        $validated = $request->validate([
            'name' => ['required', 'string', 'max:255'],
            'chapter_id' => [$chapter ? 'nullable' : 'required', 'integer', 'exists:chapters,id'],
        ]);

        $finalChapterId = $chapterId ?: $validated['chapter_id'];

        $topic = Topic::create([
            'name' => trim($validated['name']),
            'chapter_id' => $finalChapterId,
        ]);

        $topic->load('chapter');

        if ($request->wantsJson() || $request->ajax()) {
            return response()->json([
                'success' => true,
                'message' => 'Topic created successfully!',
                'topic' => $topic,
            ]);
        }

        return back()->with('status', "Topic '{$topic->name}' created successfully!");
    }

    /**
     * Update the specified topic.
     */
    public function update(Request $request, Topic $topic): JsonResponse|RedirectResponse
    {
        $user = $request->user();
        if (! $user->canAssignExams()) {
            abort(403, 'Unauthorized access.');
        }

        $validated = $request->validate([
            'name' => ['required', 'string', 'max:255'],
            'chapter_id' => ['nullable', 'integer', 'exists:chapters,id'],
        ]);

        $updateData = [
            'name' => trim($validated['name']),
        ];

        if (array_key_exists('chapter_id', $validated)) {
            $updateData['chapter_id'] = $validated['chapter_id'];
        }

        $topic->update($updateData);
        $topic->load('chapter');

        if ($request->wantsJson() || $request->ajax()) {
            return response()->json([
                'success' => true,
                'message' => 'Topic updated successfully!',
                'topic' => $topic,
            ]);
        }

        return back()->with('status', "Topic '{$topic->name}' updated successfully!");
    }

    /**
     * Remove the specified topic.
     */
    public function destroy(Request $request, Topic $topic): JsonResponse|RedirectResponse
    {
        $user = $request->user();
        if (! $user->canAssignExams()) {
            abort(403, 'Unauthorized access.');
        }

        $topicName = $topic->name;
        $topic->delete();

        if ($request->wantsJson() || $request->ajax()) {
            return response()->json([
                'success' => true,
                'message' => "Topic '{$topicName}' deleted successfully!",
            ]);
        }

        return back()->with('status', "Topic '{$topicName}' deleted successfully!");
    }
}
