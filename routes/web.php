<?php

use App\Http\Controllers\AdminUserController;
use App\Http\Controllers\AuthController;
use App\Http\Controllers\ChapterController;
use App\Http\Controllers\ChatController;
use App\Http\Controllers\DashboardController;
use App\Http\Controllers\ExamController;
use App\Http\Controllers\MultimediaController;
use App\Http\Controllers\QuestionController;
use App\Http\Controllers\StandardController;
use App\Http\Controllers\StudentController;
use App\Http\Controllers\StudentExamController;
use App\Http\Controllers\TopicController;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return redirect()->route('dashboard');
});

Route::middleware('guest')->group(function () {
    Route::get('/login', [AuthController::class, 'showLoginForm'])->name('login');
    Route::post('/login', [AuthController::class, 'login']);

    Route::get('/register', [AuthController::class, 'showRegisterForm'])->name('register');
    Route::post('/register', [AuthController::class, 'register']);
});

Route::middleware('auth')->group(function () {
    Route::get('/dashboard', [DashboardController::class, 'index'])->name('dashboard');
    Route::get('/multimedia', [MultimediaController::class, 'index'])->name('multimedia.index');
    Route::post('/logout', [AuthController::class, 'logout'])->name('logout');

    // Admin User Management Routes
    Route::post('/admin/users', [AdminUserController::class, 'store'])->name('admin.users.store');
    Route::put('/admin/users/{user}', [AdminUserController::class, 'update'])->name('admin.users.update');
    Route::delete('/admin/users/{user}', [AdminUserController::class, 'destroy'])->name('admin.users.destroy');
    Route::post('/admin/change-password', [AuthController::class, 'changePassword'])->name('admin.change-password');

    // Standards Management Routes
    Route::get('/standards', [StandardController::class, 'index'])->name('standards.index');
    Route::post('/standards', [StandardController::class, 'store'])->name('standards.store');
    Route::put('/standards/{standard}', [StandardController::class, 'update'])->name('standards.update');
    Route::delete('/standards/{standard}', [StandardController::class, 'destroy'])->name('standards.destroy');
    Route::post('/standards/{standard}/assign-students', [StandardController::class, 'assignStudents'])->name('standards.assign-students');

    // Chapters Management Routes (Inside Standard)
    Route::get('/standards/{standard}/chapters', [ChapterController::class, 'index'])->name('standards.chapters.index');
    Route::post('/standards/{standard}/chapters', [ChapterController::class, 'store'])->name('standards.chapters.store');
    Route::get('/chapters', [ChapterController::class, 'index'])->name('chapters.index');
    Route::post('/chapters', [ChapterController::class, 'store'])->name('chapters.store');
    Route::put('/chapters/{chapter}', [ChapterController::class, 'update'])->name('chapters.update');
    Route::delete('/chapters/{chapter}', [ChapterController::class, 'destroy'])->name('chapters.destroy');

    // Topics Management Routes (Inside Chapter)
    Route::get('/chapters/{chapter}/topics', [TopicController::class, 'index'])->name('chapters.topics.index');
    Route::post('/chapters/{chapter}/topics', [TopicController::class, 'store'])->name('chapters.topics.store');
    Route::get('/topics', [TopicController::class, 'index'])->name('topics.index');
    Route::post('/topics', [TopicController::class, 'store'])->name('topics.store');
    Route::put('/topics/{topic}', [TopicController::class, 'update'])->name('topics.update');
    Route::delete('/topics/{topic}', [TopicController::class, 'destroy'])->name('topics.destroy');

    // Students Directory Routes
    Route::get('/students', [StudentController::class, 'index'])->name('students.index');

    // Questions Management Routes
    Route::get('/questions', [QuestionController::class, 'index'])->name('questions.index');
    Route::post('/questions', [QuestionController::class, 'store'])->name('questions.store');
    Route::put('/questions/{question}', [QuestionController::class, 'update'])->name('questions.update');
    Route::delete('/questions/{question}', [QuestionController::class, 'destroy'])->name('questions.destroy');

    // Exams Management Routes
    Route::get('/exams', [ExamController::class, 'index'])->name('exams.index');
    Route::post('/exams', [ExamController::class, 'store'])->name('exams.store');
    Route::get('/exams/{exam}', [ExamController::class, 'show'])->name('exams.show');
    Route::get('/exams/{exam}/leaderboard', [ExamController::class, 'leaderboard'])->name('exams.leaderboard');
    Route::put('/exams/{exam}', [ExamController::class, 'update'])->name('exams.update');
    Route::delete('/exams/{exam}', [ExamController::class, 'destroy'])->name('exams.destroy');
    Route::post('/exams/{exam}/questions', [ExamController::class, 'addQuestions'])->name('exams.questions.add');
    Route::delete('/exams/{exam}/questions/{question}', [ExamController::class, 'removeQuestion'])->name('exams.questions.remove');
    Route::post('/exams/{exam}/assign-standards', [ExamController::class, 'assignStandards'])->name('exams.assign-standards');
    Route::post('/exams/{exam}/evaluate/{student}', [ExamController::class, 'evaluateTextEntrySubmission'])->name('exams.evaluate-submission');

    // Student Exam Attempt Route
    Route::post('/student/exams/{exam}/submit', [StudentExamController::class, 'submit'])->name('student.exams.submit');

    // Chat & Notification Routes
    Route::get('/chat/contacts', [ChatController::class, 'contacts'])->name('chat.contacts');
    Route::get('/chat/messages/{user}', [ChatController::class, 'getMessages'])->name('chat.messages');
    Route::post('/chat/send', [ChatController::class, 'sendMessage'])->name('chat.send');
    Route::get('/chat/notifications', [ChatController::class, 'notifications'])->name('chat.notifications');
});
