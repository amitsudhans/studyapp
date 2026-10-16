<?php

namespace Database\Seeders;

use App\Models\Answer;
use App\Models\Chapter;
use App\Models\Question;
use App\Models\Standard;
use App\Models\Subject;
use App\Models\Topic;
use Illuminate\Database\Seeder;

class ClassNineNumberSystemQuestionSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $standard = Standard::where('name', 'like', '%Class 9%')->first();
        if (! $standard) {
            $standard = Standard::create([
                'name' => 'Class 9',
                'syllabus_id' => 1,
                'created_by' => 2,
            ]);
        }

        $subject = Subject::where('name', 'Mathematics')->first();
        if (! $subject) {
            $subject = Subject::create([
                'name' => 'Mathematics',
                'syllabus_id' => $standard->syllabus_id ?? 1,
            ]);
        }

        $chapter = Chapter::where('standard_id', $standard->id)
            ->where('name', 'like', '%Number System%')
            ->first();

        if (! $chapter) {
            $chapter = Chapter::create([
                'name' => 'Number System',
                'standard_id' => $standard->id,
                'subject_id' => $subject->id,
                'syllabus_id' => $standard->syllabus_id ?? 1,
            ]);
        } else {
            $chapter->update([
                'name' => 'Number System',
                'subject_id' => $subject->id,
            ]);
        }

        $topic = Topic::where('chapter_id', $chapter->id)
            ->where(function ($q) {
                $q->where('name', 'Number System')
                    ->orWhere('name', 'like', '%Number System%');
            })
            ->first();

        if (! $topic) {
            $topic = Topic::create([
                'name' => 'Number System',
                'chapter_id' => $chapter->id,
            ]);
        } else {
            $topic->update(['name' => 'Number System']);
        }

        $question = Question::create([
            'name' => 'Which of the following numbers is an irrational number?',
            'description' => 'CBSE Class 9 Mathematics - Chapter 1: Number Systems. Identification of irrational numbers.',
            'hint' => 'An irrational number has a non-terminating, non-repeating decimal expansion and cannot be expressed as p/q. Check whether the number under the square root is a perfect square.',
            'solution' => '√23 is an irrational number because 23 is a prime number and not a perfect square, resulting in a non-terminating and non-recurring decimal representation. In contrast, √225 = 15 (rational), 0.3796 has a terminating decimal (rational), and 7.478478... is non-terminating recurring (rational).',
            'standard_id' => $standard->id,
            'subject_id' => $subject->id,
            'chapter_id' => $chapter->id,
            'topic_id' => $topic->id,
            'type' => 1, // Single choice MCQ
            'created_by' => 2, // Admin User
            'marks' => 1,
            'status' => 1,
        ]);

        $options = [
            ['name' => '√23', 'is_correct' => 1],
            ['name' => '√225', 'is_correct' => 0],
            ['name' => '0.3796', 'is_correct' => 0],
            ['name' => '7.478478...', 'is_correct' => 0],
        ];

        foreach ($options as $opt) {
            Answer::create([
                'question_id' => $question->id,
                'name' => $opt['name'],
                'is_correct' => $opt['is_correct'],
                'status' => 1,
            ]);
        }

        $this->command->info("CBSE Question created with ID: {$question->id}");
    }
}
