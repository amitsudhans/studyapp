<?php

namespace Database\Seeders;

use App\Models\Question;
use App\Models\Topic;
use Illuminate\Database\Seeder;

class AssignSubjectChapterTopicToQuestionsSeeder extends Seeder
{
    /**
     * Assign subject_id, chapter_id, and topic_id to all existing questions.
     */
    public function run(): void
    {
        // Fetch all available topics with their chapter and subject loaded
        $topics = Topic::with('chapter.subject')->get();

        if ($topics->isEmpty()) {
            return;
        }

        $questions = Question::all();
        $topicCount = $topics->count();

        foreach ($questions as $index => $question) {
            // Pick a topic deterministically using index modulo topicCount
            $topic = $topics[$index % $topicCount];
            $chapter = $topic->chapter;
            $subject = $chapter?->subject;

            $question->update([
                'subject_id' => $subject?->id,
                'chapter_id' => $chapter?->id,
                'topic_id' => $topic->id,
            ]);
        }
    }
}
