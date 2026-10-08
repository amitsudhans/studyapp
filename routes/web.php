<?php

use App\Http\Controllers\AdminUserController;
use App\Http\Controllers\AuthController;
use App\Http\Controllers\DashboardController;
use App\Http\Controllers\ExamController;
use App\Http\Controllers\QuestionController;
use App\Http\Controllers\StandardController;
use App\Http\Controllers\StudentExamController;
use App\Http\Controllers\ChatController;
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
    Route::post('/logout', [AuthController::class, 'logout'])->name('logout');

    // Admin User Management Routes
    Route::post('/admin/users', [AdminUserController::class, 'store'])->name('admin.users.store');
    Route::put('/admin/users/{user}', [AdminUserController::class, 'update'])->name('admin.users.update');
    Route::delete('/admin/users/{user}', [AdminUserController::class, 'destroy'])->name('admin.users.destroy');
    Route::post('/admin/change-password', [AuthController::class, 'changePassword'])->name('admin.change-password');

    // Standards Management Routes
    Route::post('/standards', [StandardController::class, 'store'])->name('standards.store');
    Route::put('/standards/{standard}', [StandardController::class, 'update'])->name('standards.update');
    Route::post('/standards/{standard}/assign-students', [StandardController::class, 'assignStudents'])->name('standards.assign-students');

    // Questions Management Routes
    Route::get('/questions', [QuestionController::class, 'index'])->name('questions.index');
    Route::post('/questions', [QuestionController::class, 'store'])->name('questions.store');
    Route::put('/questions/{question}', [QuestionController::class, 'update'])->name('questions.update');
    Route::delete('/questions/{question}', [QuestionController::class, 'destroy'])->name('questions.destroy');

    // Exams Management Routes
    Route::get('/exams', [ExamController::class, 'index'])->name('exams.index');
    Route::post('/exams', [ExamController::class, 'store'])->name('exams.store');
    Route::get('/exams/{exam}', [ExamController::class, 'show'])->name('exams.show');
    Route::put('/exams/{exam}', [ExamController::class, 'update'])->name('exams.update');
    Route::delete('/exams/{exam}', [ExamController::class, 'destroy'])->name('exams.destroy');
    Route::post('/exams/{exam}/questions', [ExamController::class, 'addQuestions'])->name('exams.questions.add');
    Route::delete('/exams/{exam}/questions/{question}', [ExamController::class, 'removeQuestion'])->name('exams.questions.remove');
    Route::post('/exams/{exam}/assign-standards', [ExamController::class, 'assignStandards'])->name('exams.assign-standards');

    // Student Exam Attempt Route
    Route::post('/student/exams/{exam}/submit', [StudentExamController::class, 'submit'])->name('student.exams.submit');

    // Chat & Notification Routes
    Route::get('/chat/contacts', [ChatController::class, 'contacts'])->name('chat.contacts');
    Route::get('/chat/messages/{user}', [ChatController::class, 'getMessages'])->name('chat.messages');
    Route::post('/chat/send', [ChatController::class, 'sendMessage'])->name('chat.send');
    Route::get('/chat/notifications', [ChatController::class, 'notifications'])->name('chat.notifications');
});
