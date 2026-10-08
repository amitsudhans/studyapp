<?php

namespace App\Http\Controllers;

use App\Models\Exam;
use App\Models\Student;
use App\Models\StudentExamDetail;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class StudentExamController extends Controller
{
    /**
     * Store student exam responses in student_exam_details upon clicking submit exam.
     */
    public function submit(Request $request, Exam $exam): RedirectResponse
    {
        $user = $request->user();

        // Ensure user is a student
        if ((int) ($user->profile?->type ?? 1) !== 2) {
            abort(403, 'Only students are permitted to submit exams.');
        }

        // Retrieve or create student record
        $student = $user->student;
        if (! $student) {
            $student = Student::firstOrCreate(
                ['id' => $user->id],
                [
                    'name' => $user->name,
                    'standard_id' => $user->profile?->standard_id ?? 1,
                ]
            );
        }

        // Prevent double submission
        $alreadySubmitted = StudentExamDetail::where('student_id', $student->id)
            ->where('exam_id', $exam->id)
            ->exists();

        if ($alreadySubmitted) {
            return back()->with('error', 'You have already submitted this exam.');
        }

        // Validate payload
        $validated = $request->validate([
            'answers' => ['nullable', 'array'],
            'answers.*' => ['nullable', 'integer', 'exists:answers,id'],
        ]);

        $submittedAnswers = $validated['answers'] ?? [];

        // Load exam questions to save answers for each question
        $exam->load('questions');

        DB::transaction(function () use ($student, $exam, $submittedAnswers) {
            foreach ($exam->questions as $question) {
                $chosenAnsId = $submittedAnswers[$question->id] ?? null;

                StudentExamDetail::create([
                    'student_id' => $student->id,
                    'exam_id' => $exam->id,
                    'question_id' => $question->id,
                    'student_written_ans_id' => $chosenAnsId ? (int) $chosenAnsId : null,
                ]);
            }
        });

        return redirect()->route('dashboard')->with('status', 'Exam submitted successfully! All your answers have been recorded.');
    }
}
