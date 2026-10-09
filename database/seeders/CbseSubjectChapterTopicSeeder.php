<?php

namespace Database\Seeders;

use App\Models\Chapter;
use App\Models\Subject;
use App\Models\Syllabus;
use App\Models\Topic;
use Illuminate\Database\Seeder;

class CbseSubjectChapterTopicSeeder extends Seeder
{
    /**
     * Run the database seeds for CBSE Subjects, Chapters, and Topics.
     */
    public function run(): void
    {
        // 1. Get or create CBSE Syllabus
        $syllabus = Syllabus::firstOrCreate(['name' => 'CBSE']);

        // 2. Define Subjects, Chapters, and Topics under CBSE
        $data = [
            'Mathematics' => [
                'Real Numbers' => [
                    'Fundamental Theorem of Arithmetic',
                    'Irrational Numbers & Proofs',
                ],
                'Polynomials' => [
                    'Zeros of a Polynomial',
                    'Relationship between Zeros and Coefficients',
                ],
                'Quadratic Equations' => [
                    'Standard Form of Quadratic Equation',
                    'Quadratic Formula & Nature of Roots',
                ],
            ],
            'Physics' => [
                'Light - Reflection and Refraction' => [
                    'Spherical Mirrors & Image Formation',
                    'Refraction through Glass Prism & Lenses',
                ],
                'Electricity' => [
                    'Ohm\'s Law & Resistance',
                    'Heating Effect of Electric Current & Electric Power',
                ],
            ],
            'Chemistry' => [
                'Chemical Reactions and Equations' => [
                    'Types of Chemical Reactions',
                    'Oxidation and Reduction Reactions',
                ],
                'Acids, Bases and Salts' => [
                    'Indicators & pH Scale',
                    'Preparation & Uses of Salts',
                ],
            ],
            'Biology' => [
                'Life Processes' => [
                    'Nutrition & Photosynthesis',
                    'Respiration, Circulation & Excretion',
                ],
                'Control and Coordination' => [
                    'Nervous System & Reflex Action',
                    'Plant & Animal Hormones',
                ],
            ],
        ];

        foreach ($data as $subjectName => $chapters) {
            $subject = Subject::firstOrCreate([
                'name' => $subjectName,
                'syllabus_id' => $syllabus->id,
            ]);

            foreach ($chapters as $chapterName => $topics) {
                $chapter = Chapter::firstOrCreate([
                    'name' => $chapterName,
                    'subject_id' => $subject->id,
                    'syllabus_id' => $syllabus->id,
                ]);

                foreach ($topics as $topicName) {
                    Topic::firstOrCreate([
                        'name' => $topicName,
                        'chapter_id' => $chapter->id,
                    ]);
                }
            }
        }
    }
}
