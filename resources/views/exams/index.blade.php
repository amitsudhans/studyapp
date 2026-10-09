<x-layouts.app title="Exams Management - Study App">
    <div class="py-8 w-full px-4 sm:px-6 lg:px-8 space-y-8">
        
        <!-- Header Banner -->
        <div class="relative overflow-hidden rounded-2xl bg-gradient-to-r from-indigo-950 via-slate-900 to-slate-900 border border-indigo-500/30 p-6 sm:p-8 shadow-2xl">
            <div class="relative z-10 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-6">
                <div>
                    <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-indigo-500/20 border border-indigo-500/40 text-indigo-300 text-xs font-semibold uppercase tracking-wider mb-3">
                        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                        <span>Exams & Assessment</span>
                    </div>
                    <h1 class="text-3xl font-extrabold text-white tracking-tight sm:text-4xl">
                        Exams Management
                    </h1>
                    <p class="mt-2 text-slate-300 text-sm max-w-xl">
                        Create and edit exams, attach questions from the Question Bank, and track total marks automatically.
                    </p>
                </div>

                <div class="flex items-center flex-wrap gap-3">
                    <a href="{{ route('dashboard') }}" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium text-sm transition-all flex items-center space-x-2">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
                        </svg>
                        <span>Dashboard</span>
                    </a>

                    <a href="{{ route('questions.index') }}" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium text-sm transition-all flex items-center space-x-2">
                        <svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                        </svg>
                        <span>Question Bank</span>
                    </a>

                    <button onclick="document.getElementById('createExamModal').classList.remove('hidden')" class="px-5 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-sm transition-all shadow-lg shadow-indigo-600/30 flex items-center space-x-2 cursor-pointer">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
                        </svg>
                        <span>Create New Exam</span>
                    </button>
                </div>
            </div>
        </div>

        <!-- Metric Stat Summary -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-6">
            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Total Exams</span>
                    <div class="p-2 bg-indigo-500/10 rounded-lg text-indigo-400">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                    </div>
                </div>
                <p class="mt-4 text-3xl font-extrabold text-white">{{ $exams->total() }}</p>
                <p class="mt-1 text-xs text-slate-400">Created in the system</p>
            </div>

            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Active Exams</span>
                    <div class="p-2 bg-emerald-500/10 rounded-lg text-emerald-400">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                    </div>
                </div>
                <p class="mt-4 text-3xl font-extrabold text-white">{{ $exams->filter(fn($e) => $e->status == 1)->count() }}</p>
                <p class="mt-1 text-xs text-slate-400">Status set to Active (1)</p>
            </div>

            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Question Bank Pool</span>
                    <div class="p-2 bg-violet-500/10 rounded-lg text-violet-400">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                    </div>
                </div>
                <p class="mt-4 text-3xl font-extrabold text-white">{{ $availableQuestions->count() }}</p>
                <p class="mt-1 text-xs text-slate-400">Questions ready to add to exams</p>
            </div>
        </div>

        <!-- Exams Directory List -->
        <div class="bg-slate-900 border border-slate-800 rounded-2xl shadow-xl overflow-hidden">
            <div class="px-6 py-5 border-b border-slate-800 flex items-center justify-between">
                <div>
                    <h3 class="text-lg font-semibold text-white flex items-center space-x-2">
                        <svg class="w-5 h-5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
                        </svg>
                        <span>All Exams</span>
                    </h3>
                    <p class="text-xs text-slate-400 mt-0.5">Click any exam name to expand its details and manage actions</p>
                </div>
                <span class="text-xs text-slate-400 bg-slate-800 px-3 py-1 rounded-full border border-slate-700">Total: {{ $exams->total() }}</span>
            </div>

            @if($exams->isNotEmpty())
                <div class="divide-y divide-slate-800/80">
                    @foreach ($exams as $exam)
                        <div class="bg-slate-900 hover:bg-slate-800/40 transition-colors">
                            <!-- Header Row: Displays ONLY Exam Name First -->
                            <div onclick="toggleExamManagementDetails({{ $exam->id }})" class="px-6 py-4 flex items-center justify-between cursor-pointer group select-none">
                                <div class="flex items-center space-x-3.5">
                                    <div class="w-9 h-9 rounded-xl bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 font-bold flex items-center justify-center text-sm group-hover:bg-indigo-500/20 transition-colors shrink-0">
                                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                                    </div>
                                    <div>
                                        <h4 class="text-base font-bold text-white group-hover:text-indigo-300 transition-colors flex items-center space-x-2">
                                            <span>{{ $exam->name }}</span>
                                        </h4>
                                        <p class="text-xs text-slate-400 mt-0.5">Click to view exam details & actions</p>
                                    </div>
                                </div>

                                <div class="flex items-center space-x-3">
                                    @if($exam->status == 1)
                                        <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                                            Active
                                        </span>
                                    @else
                                        <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold bg-rose-500/10 text-rose-400 border border-rose-500/20">
                                            Inactive
                                        </span>
                                    @endif
                                    <div class="p-1.5 rounded-lg bg-slate-800 border border-slate-700 text-slate-400 group-hover:text-white group-hover:border-slate-600 transition-all">
                                        <svg id="chevron-exam-mgmt-{{ $exam->id }}" class="w-4 h-4 transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                                        </svg>
                                    </div>
                                </div>
                            </div>

                            <!-- Expandable Details Section (Shown when clicking Exam Name) -->
                            <div id="details-exam-mgmt-{{ $exam->id }}" class="hidden px-6 py-5 bg-slate-950/80 border-t border-slate-800/80 space-y-4">
                                <!-- Key Details Cards -->
                                <div class="grid grid-cols-2 sm:grid-cols-6 gap-3">
                                    <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-800">
                                        <span class="block text-[10px] font-semibold text-slate-400 uppercase tracking-wider">Type</span>
                                        @if($exam->type == 1)
                                            <span class="inline-flex items-center px-2 py-0.5 rounded-full text-xs font-semibold bg-indigo-500/10 text-indigo-400 border border-indigo-500/20 mt-1">
                                                Timed {{ $exam->duration ? "({$exam->duration} mins)" : '(1)' }}
                                            </span>
                                        @else
                                            <span class="inline-flex items-center px-2 py-0.5 rounded-full text-xs font-semibold bg-slate-800 text-slate-300 border border-slate-700 mt-1">
                                                Non-Timed (2)
                                            </span>
                                        @endif
                                    </div>

                                    <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-800">
                                        <span class="block text-[10px] font-semibold text-slate-400 uppercase tracking-wider">Status</span>
                                        @if($exam->status == 1)
                                            <span class="inline-flex items-center px-2 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 mt-1">
                                                Active (1)
                                            </span>
                                        @else
                                            <span class="inline-flex items-center px-2 py-0.5 rounded-full text-xs font-semibold bg-rose-500/10 text-rose-400 border border-rose-500/20 mt-1">
                                                Inactive (2)
                                            </span>
                                        @endif
                                    </div>

                                    <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-800 col-span-2 sm:col-span-2">
                                        <span class="block text-[10px] font-semibold text-slate-400 uppercase tracking-wider mb-1">Assigned Standards</span>
                                        <div class="flex flex-wrap gap-1">
                                            @forelse($exam->standards as $std)
                                                <span class="inline-flex items-center px-2 py-0.5 rounded text-[11px] font-medium bg-indigo-500/10 text-indigo-300 border border-indigo-500/20">
                                                    {{ $std->name }}
                                                </span>
                                            @empty
                                                <span class="text-xs text-slate-500 italic">Unassigned</span>
                                            @endforelse
                                        </div>
                                    </div>

                                    <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-800">
                                        <span class="block text-[10px] font-semibold text-slate-400 uppercase tracking-wider">Questions</span>
                                        <span class="text-xs font-bold text-violet-300 mt-1 block">
                                            {{ $exam->questions->count() }} Questions
                                        </span>
                                    </div>

                                    <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-800">
                                        <span class="block text-[10px] font-semibold text-slate-400 uppercase tracking-wider">Total Marks</span>
                                        <span class="text-xs font-bold text-amber-400 mt-1 block">
                                            {{ $exam->total_mark }} Marks
                                        </span>
                                    </div>
                                </div>

                                <!-- Actions Bar -->
                                <div class="pt-3 border-t border-slate-800/80 flex items-center justify-between flex-wrap gap-3">
                                    <div class="text-xs text-slate-400">
                                        Created by: <span class="font-semibold text-slate-200">{{ $exam->creator?->name ?? 'System' }}</span>
                                    </div>

                                    @php
                                        $hasCompletions = ($exam->student_exam_details_count ?? 0) > 0;
                                    @endphp

                                    <div class="flex items-center space-x-2 flex-wrap gap-y-2">
                                        <button onclick="openViewExamModal({{ json_encode([
                                            'id' => $exam->id,
                                            'name' => $exam->name,
                                            'type' => $exam->type == 1 ? ('1 - Timed' . ($exam->duration ? ' (' . $exam->duration . ' mins)' : '')) : '2 - Non-Timed',
                                            'status' => $exam->status == 1 ? '1 - Active' : '2 - Inactive',
                                            'status_id' => $exam->status,
                                            'duration' => $exam->duration,
                                            'creator' => $exam->creator?->name ?? 'System',
                                            'total_mark' => $exam->total_mark,
                                            'show_url' => route('exams.show', $exam),
                                            'has_completions' => $hasCompletions,
                                            'standards' => $exam->standards->pluck('name')->toArray(),
                                            'questions' => $exam->questions->map(function($q) {
                                                return [
                                                    'id' => $q->id,
                                                    'name' => $q->name,
                                                    'description' => $q->description ?? '',
                                                    'marks' => $q->marks,
                                                    'standard' => $q->standard?->name ?? 'N/A',
                                                    'type_id' => $q->type,
                                                    'type' => $q->type == 1 ? 'Single Option' : ($q->type == 2 ? 'Multiple Option' : 'Text Entry'),
                                                    'creator' => $q->creator?->name ?? 'System',
                                                    'answers' => $q->answers->map(fn($a) => ['id' => $a->id, 'name' => $a->name, 'is_correct' => $a->is_correct])->toArray(),
                                                ];
                                            })->toArray(),
                                        ]) }})" class="px-3.5 py-1.5 rounded-lg bg-emerald-950/80 hover:bg-emerald-900/80 text-emerald-300 text-xs font-medium border border-emerald-800/40 transition-colors inline-flex items-center space-x-1 cursor-pointer">
                                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                                            <span>View</span>
                                        </button>

                                        <button type="button" onclick="openExamLeaderboardModal({{ $exam->id }}, '{{ addslashes($exam->name) }}')" class="px-3.5 py-1.5 rounded-lg bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 text-xs font-bold border border-amber-500/40 transition-colors inline-flex items-center space-x-1 cursor-pointer">
                                            <span>🏆 Leaderboard</span>
                                        </button>

                                        @if(!$hasCompletions)
                                            <button onclick="openEditExamModal({{ json_encode([
                                                'id' => $exam->id,
                                                'name' => $exam->name,
                                                'type' => $exam->type,
                                                'duration' => $exam->duration,
                                                'status' => $exam->status,
                                                'standard_ids' => $exam->standards->pluck('id')->toArray(),
                                                'question_ids' => $exam->questions->pluck('id')->toArray(),
                                            ]) }})" class="px-3.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-medium border border-slate-700 transition-colors inline-flex items-center space-x-1 cursor-pointer">
                                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/></svg>
                                                <span>Edit</span>
                                            </button>

                                            <a href="{{ route('exams.show', $exam) }}" class="px-3.5 py-1.5 rounded-lg bg-indigo-950/80 hover:bg-indigo-900/80 text-indigo-300 text-xs font-medium border border-indigo-800/40 transition-colors inline-flex items-center space-x-1 cursor-pointer" title="Manage questions in this exam">
                                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"/></svg>
                                                <span>Manage Questions</span>
                                            </a>

                                            <form method="POST" action="{{ route('exams.destroy', $exam) }}" class="inline" onsubmit="return confirm('Are you sure you want to delete this exam?')">
                                                @csrf
                                                @method('DELETE')
                                                <button type="submit" class="px-3.5 py-1.5 rounded-lg bg-red-950/60 hover:bg-red-900/60 text-red-300 text-xs font-medium border border-red-800/40 transition-colors inline-flex items-center space-x-1 cursor-pointer">
                                                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/></svg>
                                                    <span>Delete</span>
                                                </button>
                                            </form>
                                        @else
                                            <span class="inline-flex items-center px-3 py-1.5 rounded-lg bg-amber-500/10 text-amber-400 border border-amber-500/20 text-xs font-semibold" title="Student has taken this exam - edit, delete, and manage questions options are disabled">
                                                <svg class="w-3.5 h-3.5 mr-1.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/></svg>
                                                Completed by Student
                                            </span>
                                        @endif
                                    </div>
                                </div>
                            </div>
                        </div>
                    @endforeach
                </div>
            @else
                <div class="p-12 text-center text-slate-500">
                    No exams created yet. Click "Create New Exam" to get started.
                </div>
            @endif

            @if($exams->hasPages())
                <div class="px-6 py-4 border-t border-slate-800">
                    {{ $exams->links() }}
                </div>
            @endif
        </div>

        <!-- CREATE EXAM MODAL -->
        @php
            $isCreateModalOpen = $errors->any() && old('_method') !== 'PUT';
        @endphp
        <div id="createExamModal" class="{{ $isCreateModalOpen ? '' : 'hidden' }} fixed inset-0 z-50 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4 overflow-y-auto">
            <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-6xl overflow-hidden shadow-2xl my-8">
                <div class="px-6 py-4 border-b border-slate-800 flex items-center justify-between bg-slate-950/50">
                    <h3 class="text-lg font-bold text-white">Create New Exam</h3>
                    <button onclick="document.getElementById('createExamModal').classList.add('hidden')" class="text-slate-400 hover:text-white transition-colors cursor-pointer">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                    </button>
                </div>

                <form method="POST" action="{{ route('exams.store') }}" class="p-6 space-y-4">
                    @csrf

                    @if ($isCreateModalOpen && $errors->any())
                        <div class="p-3.5 rounded-xl bg-red-950/80 border border-red-500/40 text-red-200 text-xs">
                            <span class="font-bold flex items-center gap-1 text-red-300">
                                <svg class="w-4 h-4 inline" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                                Validation errors occurred. Please check the fields below.
                            </span>
                        </div>
                    @endif

                    <!-- Exam Name (Required) -->
                    <div>
                        <label for="create_exam_name" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Exam Name <span class="text-red-400">*</span></label>
                        <input type="text" id="create_exam_name" name="name" required value="{{ old('name') }}" placeholder="e.g. Mid-Term Science Assessment" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('name') border-red-500 focus:ring-red-500 @enderror">
                        @error('name')
                            <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                        @enderror
                    </div>

                    <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                        <!-- Exam Type -->
                        <div>
                            <label for="create_exam_type" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Exam Type <span class="text-red-400">*</span></label>
                            <select id="create_exam_type" name="type" required onchange="toggleCreateExamDuration(this.value)" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm">
                                <option value="1" {{ old('type', '1') == '1' ? 'selected' : '' }}>1 - Timed</option>
                                <option value="2" {{ old('type') == '2' ? 'selected' : '' }}>2 - Non-Timed</option>
                            </select>
                            @error('type')
                                <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                            @enderror
                        </div>

                        <!-- Duration (Minutes) -->
                        <div id="create_duration_wrapper" class="{{ old('type', '1') == '2' ? 'hidden' : '' }}">
                            <label for="create_exam_duration" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Duration (Minutes) <span class="text-red-400">*</span></label>
                            <input type="number" id="create_exam_duration" name="duration" min="1" max="1440" value="{{ old('duration', 60) }}" placeholder="e.g. 60" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('duration') border-red-500 focus:ring-red-500 @enderror">
                            @error('duration')
                                <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                            @enderror
                        </div>

                        <!-- Status -->
                        <div>
                            <label for="create_exam_status" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Status <span class="text-red-400">*</span></label>
                            <select id="create_exam_status" name="status" required class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm">
                                <option value="1" {{ old('status', '1') == '1' ? 'selected' : '' }}>1 - Active</option>
                                <option value="2" {{ old('status') == '2' ? 'selected' : '' }}>2 - Inactive</option>
                            </select>
                            @error('status')
                                <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                            @enderror
                        </div>
                    </div>

                    <!-- Assign Standards (Teachers only) -->
                    <div>
                        <label class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Assign to Standards / Classes (Table: exam_assign)</label>
                        <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 bg-slate-950 p-3 rounded-lg border border-slate-800 max-h-36 overflow-y-auto">
                            @foreach($standards as $std)
                                <label class="flex items-center space-x-2 text-xs text-slate-300 cursor-pointer hover:text-white">
                                    <input type="checkbox" name="standard_ids[]" value="{{ $std->id }}" {{ in_array($std->id, old('standard_ids', [])) ? 'checked' : '' }} class="rounded bg-slate-900 border-slate-700 text-indigo-600 focus:ring-indigo-500">
                                    <span>{{ $std->name }}</span>
                                </label>
                            @endforeach
                        </div>
                        @error('standard_ids')
                            <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                        @enderror
                    </div>

                    <!-- Select Questions from Question Bank -->
                    <div>
                        <div class="flex items-center justify-between mb-2">
                            <label class="block text-xs font-semibold text-slate-300 uppercase tracking-wider">Add Questions from Question Bank (Optional)</label>
                            <span class="text-[11px] text-slate-400">Check questions to link to this exam</span>
                        </div>

                        <!-- Search & Filter Controls for Create Modal -->
                        <div class="p-3 mb-2 rounded-lg bg-slate-950 border border-slate-800 space-y-2">
                            <div class="grid grid-cols-2 gap-2">
                                <input type="text" id="create_search_q_name" oninput="filterModalQuestions('create')" placeholder="Search question name..." class="px-2.5 py-1.5 rounded bg-slate-900 border border-slate-700 text-slate-200 placeholder-slate-500 text-xs focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                <input type="text" id="create_search_q_creator" oninput="filterModalQuestions('create')" placeholder="Search created by..." class="px-2.5 py-1.5 rounded bg-slate-900 border border-slate-700 text-slate-200 placeholder-slate-500 text-xs focus:outline-none focus:ring-1 focus:ring-indigo-500">
                            </div>
                            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
                                <select id="create_search_q_standard" onchange="filterModalQuestions('create')" class="px-2.5 py-1.5 rounded bg-slate-900 border border-slate-700 text-slate-200 text-xs focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                    <option value="">All Classes / Standards</option>
                                    @foreach($standards as $std)
                                        <option value="{{ $std->id }}">{{ $std->name }}</option>
                                    @endforeach
                                </select>
                                <select id="create_search_q_subject" onchange="onModalSubjectChange('create')" class="px-2.5 py-1.5 rounded bg-slate-900 border border-slate-700 text-slate-200 text-xs focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                    <option value="">All Subjects</option>
                                    @foreach($subjectsData as $subj)
                                        <option value="{{ $subj->id }}">{{ $subj->name }}</option>
                                    @endforeach
                                </select>
                                <select id="create_search_q_chapter" onchange="onModalChapterChange('create')" class="px-2.5 py-1.5 rounded bg-slate-900 border border-slate-700 text-slate-200 text-xs focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                    <option value="">All Chapters</option>
                                </select>
                                <select id="create_search_q_topic" onchange="filterModalQuestions('create')" class="px-2.5 py-1.5 rounded bg-slate-900 border border-slate-700 text-slate-200 text-xs focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                    <option value="">All Topics</option>
                                </select>
                            </div>
                            <div class="grid grid-cols-1 gap-2">
                                <select id="create_search_q_type" onchange="filterModalQuestions('create')" class="px-2.5 py-1.5 rounded bg-slate-900 border border-slate-700 text-slate-200 text-xs focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                    <option value="">All Question Types</option>
                                    <option value="1">1 - Single Option</option>
                                    <option value="2">2 - Multiple Option</option>
                                    <option value="3">3 - Text Entry</option>
                                </select>
                            </div>
                            <!-- Pagination Bar for Create Modal -->
                            <div class="flex items-center justify-between pt-1 text-[11px] text-slate-400">
                                <div class="flex items-center space-x-1.5">
                                    <span>Show:</span>
                                    <select id="create_items_per_page" onchange="changeModalItemsPerPage('create', this.value)" class="px-1.5 py-0.5 rounded bg-slate-900 border border-slate-700 text-slate-200 text-xs focus:ring-indigo-500 focus:outline-none">
                                        <option value="10">10 per page</option>
                                        <option value="20">20 per page</option>
                                        <option value="50">50 per page</option>
                                        <option value="100">100 per page</option>
                                        <option value="9999">All</option>
                                    </select>
                                </div>
                                <span id="create_pagination_info" class="font-medium text-slate-300">Showing 0 of 0</span>
                            </div>
                        </div>

                        <div class="bg-slate-950 p-3 rounded-lg border border-slate-800 max-h-[500px] overflow-y-auto space-y-2" style="max-height: 500px; overflow-y: auto;">
                            @forelse($availableQuestions as $q)
                                <div class="create-q-item flex items-start space-x-3 p-2.5 rounded-lg bg-slate-900/60 hover:bg-slate-900 transition-colors border border-slate-800/60"
                                     data-name="{{ strtolower($q->name) }}"
                                     data-creator="{{ strtolower($q->creator?->name ?? 'system') }}"
                                     data-standard="{{ strtolower($q->standard?->name ?? '') }}"
                                     data-standard-id="{{ $q->standard_id }}"
                                     data-subject-id="{{ $q->subject_id }}"
                                     data-chapter-id="{{ $q->chapter_id }}"
                                     data-topic-id="{{ $q->topic_id }}"
                                     data-type="{{ $q->type }}">
                                    <input type="checkbox" name="question_ids[]" value="{{ $q->id }}" id="create_q_add_{{ $q->id }}" {{ in_array($q->id, old('question_ids', [])) ? 'checked' : '' }} class="mt-1 rounded bg-slate-900 border-slate-700 text-indigo-600 focus:ring-indigo-500 cursor-pointer">
                                    <div class="flex-1 text-xs">
                                        <div class="flex items-center justify-between gap-2">
                                            <label for="create_q_add_{{ $q->id }}" class="font-medium text-slate-200 hover:text-white cursor-pointer flex-1">{{ $q->name }}</label>
                                            <div class="flex items-center space-x-2 shrink-0">
                                                <button type="button" onclick="event.preventDefault(); event.stopPropagation(); openQuestionPreviewModal({{ json_encode([
                                                    'id' => $q->id,
                                                    'name' => $q->name,
                                                    'description' => $q->description ?? '',
                                                    'marks' => $q->marks,
                                                    'type' => $q->type,
                                                    'standard_name' => $q->standard?->name ?? 'N/A',
                                                    'subject_name' => $q->subject?->name ?? 'N/A',
                                                    'chapter_name' => $q->chapter?->name ?? 'N/A',
                                                    'topic_name' => $q->topic?->name ?? 'N/A',
                                                    'creator_name' => $q->creator?->name ?? 'System',
                                                    'answers' => $q->answers->map(fn($a) => ['id' => $a->id, 'name' => $a->name, 'is_correct' => $a->is_correct])->toArray(),
                                                ]) }})" class="px-2 py-0.5 rounded bg-indigo-500/10 hover:bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 text-[11px] font-medium transition-all inline-flex items-center space-x-1 cursor-pointer">
                                                    <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                                                    <span>View</span>
                                                </button>
                                                <span class="text-amber-400 font-semibold">{{ $q->marks }} mark(s)</span>
                                            </div>
                                        </div>
                                        <label for="create_q_add_{{ $q->id }}" class="flex items-center flex-wrap gap-2 mt-1 text-[11px] text-slate-400 cursor-pointer block">
                                            <span class="text-indigo-400 font-semibold">Class: {{ $q->standard?->name ?? 'N/A' }}</span>
                                            @if($q->subject)
                                                <span>&bull;</span>
                                                <span class="text-emerald-400 font-semibold">Subject: {{ $q->subject->name }}</span>
                                            @endif
                                            @if($q->chapter)
                                                <span>&bull;</span>
                                                <span class="text-cyan-400">Ch: {{ $q->chapter->name }}</span>
                                            @endif
                                            @if($q->topic)
                                                <span>&bull;</span>
                                                <span class="text-purple-400">Topic: {{ $q->topic->name }}</span>
                                            @endif
                                            <span>&bull;</span>
                                            <span>By: {{ $q->creator?->name ?? 'System' }}</span>
                                            <span>&bull;</span>
                                            <span>Type: @if($q->type == 1) Single Option @elseif($q->type == 2) Multiple Option @else Text Entry @endif</span>
                                        </label>
                                    </div>
                                </div>
                            @empty
                                <p class="text-xs text-slate-500 text-center py-4">No questions available in Question Bank.</p>
                            @endforelse
                        </div>

                        <!-- Modal Pagination Footer for Create -->
                        <div class="mt-2 flex items-center justify-between text-xs">
                            <div class="flex items-center space-x-1">
                                <button type="button" id="create_prev_btn" onclick="prevModalPage('create')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 disabled:opacity-40 disabled:cursor-not-allowed text-slate-300 text-[11px] font-semibold border border-slate-700 cursor-pointer">&larr; Prev</button>
                                <div id="create_page_numbers" class="flex items-center space-x-1"></div>
                                <button type="button" id="create_next_btn" onclick="nextModalPage('create')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 disabled:opacity-40 disabled:cursor-not-allowed text-slate-300 text-[11px] font-semibold border border-slate-700 cursor-pointer">Next &rarr;</button>
                            </div>
                        </div>
                        @error('question_ids')
                            <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                        @enderror
                    </div>

                    <div class="pt-4 flex justify-end space-x-3 border-t border-slate-800">
                        <button type="button" onclick="document.getElementById('createExamModal').classList.add('hidden')" class="px-4 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-sm font-medium transition-colors cursor-pointer">Cancel</button>
                        <button type="submit" class="px-5 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-semibold shadow-lg shadow-indigo-600/30 transition-all cursor-pointer">Save Exam</button>
                    </div>
                </form>
            </div>
        </div>

        <!-- EDIT EXAM MODAL -->
        @php
            $isEditModalOpen = $errors->any() && old('_method') === 'PUT';
        @endphp
        <div id="editExamModal" class="{{ $isEditModalOpen ? '' : 'hidden' }} fixed inset-0 z-50 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4 overflow-y-auto">
            <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-6xl overflow-hidden shadow-2xl my-8">
                <div class="px-6 py-4 border-b border-slate-800 flex items-center justify-between bg-slate-950/50">
                    <h3 class="text-lg font-bold text-white">Edit Exam</h3>
                    <button onclick="document.getElementById('editExamModal').classList.add('hidden')" class="text-slate-400 hover:text-white transition-colors cursor-pointer">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                    </button>
                </div>

                <form id="editExamForm" method="POST" action="{{ old('_method') === 'PUT' ? old('_edit_action_url', '') : '' }}" class="p-6 space-y-4">
                    @csrf
                    @method('PUT')
                    <input type="hidden" id="edit_action_url" name="_edit_action_url" value="{{ old('_method') === 'PUT' ? old('_edit_action_url', '') : '' }}">

                    @if ($isEditModalOpen && $errors->any())
                        <div class="p-3.5 rounded-xl bg-red-950/80 border border-red-500/40 text-red-200 text-xs">
                            <span class="font-bold flex items-center gap-1 text-red-300">
                                <svg class="w-4 h-4 inline" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                                Validation errors occurred. Please check the fields below.
                            </span>
                        </div>
                    @endif

                    <!-- Exam Name (Required) -->
                    <div>
                        <label for="edit_exam_name" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Exam Name <span class="text-red-400">*</span></label>
                        <input type="text" id="edit_exam_name" name="name" required value="{{ old('_method') === 'PUT' ? old('name') : '' }}" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('name') border-red-500 focus:ring-red-500 @enderror">
                        @error('name')
                            <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                        @enderror
                    </div>

                    <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                        <!-- Exam Type -->
                        <div>
                            <label for="edit_exam_type" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Exam Type <span class="text-red-400">*</span></label>
                            <select id="edit_exam_type" name="type" required onchange="toggleEditExamDuration(this.value)" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm">
                                <option value="1">1 - Timed</option>
                                <option value="2">2 - Non-Timed</option>
                            </select>
                            @error('type')
                                <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                            @enderror
                        </div>

                        <!-- Duration (Minutes) -->
                        <div id="edit_duration_wrapper">
                            <label for="edit_exam_duration" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Duration (Minutes) <span class="text-red-400">*</span></label>
                            <input type="number" id="edit_exam_duration" name="duration" min="1" max="1440" value="{{ old('_method') === 'PUT' ? old('duration') : '' }}" placeholder="e.g. 60" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('duration') border-red-500 focus:ring-red-500 @enderror">
                            @error('duration')
                                <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                            @enderror
                        </div>

                        <!-- Status -->
                        <div>
                            <label for="edit_exam_status" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Status <span class="text-red-400">*</span></label>
                            <select id="edit_exam_status" name="status" required class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm">
                                <option value="1">1 - Active</option>
                                <option value="2">2 - Inactive</option>
                            </select>
                            @error('status')
                                <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                            @enderror
                        </div>
                    </div>

                    <!-- Assign Standards (Teachers only) -->
                    <div>
                        <label class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Assign to Standards / Classes (Table: exam_assign)</label>
                        <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 bg-slate-950 p-3 rounded-lg border border-slate-800 max-h-36 overflow-y-auto">
                            @foreach($standards as $std)
                                <label class="flex items-center space-x-2 text-xs text-slate-300 cursor-pointer hover:text-white">
                                    <input type="checkbox" name="standard_ids[]" value="{{ $std->id }}" class="edit-exam-std-checkbox rounded bg-slate-900 border-slate-700 text-indigo-600 focus:ring-indigo-500">
                                    <span>{{ $std->name }}</span>
                                </label>
                            @endforeach
                        </div>
                        @error('standard_ids')
                            <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                        @enderror
                    </div>

                    <!-- Manage Questions from Question Bank -->
                    <div>
                        <div class="flex items-center justify-between mb-2">
                            <label class="block text-xs font-semibold text-slate-300 uppercase tracking-wider">Exam Questions (Question Bank)</label>
                            <span class="text-[11px] text-slate-400">Check/uncheck to update linked questions</span>
                        </div>

                        <!-- Search & Filter Controls for Edit Modal -->
                        <div class="p-3 mb-2 rounded-lg bg-slate-950 border border-slate-800 space-y-2">
                            <div class="grid grid-cols-2 gap-2">
                                <input type="text" id="edit_search_q_name" oninput="filterModalQuestions('edit')" placeholder="Search question name..." class="px-2.5 py-1.5 rounded bg-slate-900 border border-slate-700 text-slate-200 placeholder-slate-500 text-xs focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                <input type="text" id="edit_search_q_creator" oninput="filterModalQuestions('edit')" placeholder="Search created by..." class="px-2.5 py-1.5 rounded bg-slate-900 border border-slate-700 text-slate-200 placeholder-slate-500 text-xs focus:outline-none focus:ring-1 focus:ring-indigo-500">
                            </div>
                            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
                                <select id="edit_search_q_standard" onchange="filterModalQuestions('edit')" class="px-2.5 py-1.5 rounded bg-slate-900 border border-slate-700 text-slate-200 text-xs focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                    <option value="">All Classes / Standards</option>
                                    @foreach($standards as $std)
                                        <option value="{{ $std->id }}">{{ $std->name }}</option>
                                    @endforeach
                                </select>
                                <select id="edit_search_q_subject" onchange="onModalSubjectChange('edit')" class="px-2.5 py-1.5 rounded bg-slate-900 border border-slate-700 text-slate-200 text-xs focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                    <option value="">All Subjects</option>
                                    @foreach($subjectsData as $subj)
                                        <option value="{{ $subj->id }}">{{ $subj->name }}</option>
                                    @endforeach
                                </select>
                                <select id="edit_search_q_chapter" onchange="onModalChapterChange('edit')" class="px-2.5 py-1.5 rounded bg-slate-900 border border-slate-700 text-slate-200 text-xs focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                    <option value="">All Chapters</option>
                                </select>
                                <select id="edit_search_q_topic" onchange="filterModalQuestions('edit')" class="px-2.5 py-1.5 rounded bg-slate-900 border border-slate-700 text-slate-200 text-xs focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                    <option value="">All Topics</option>
                                </select>
                            </div>
                            <div class="grid grid-cols-1 gap-2">
                                <select id="edit_search_q_type" onchange="filterModalQuestions('edit')" class="px-2.5 py-1.5 rounded bg-slate-900 border border-slate-700 text-slate-200 text-xs focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                    <option value="">All Question Types</option>
                                    <option value="1">1 - Single Option</option>
                                    <option value="2">2 - Multiple Option</option>
                                    <option value="3">3 - Text Entry</option>
                                </select>
                            </div>
                            <!-- Pagination Bar for Edit Modal -->
                            <div class="flex items-center justify-between pt-1 text-[11px] text-slate-400">
                                <div class="flex items-center space-x-1.5">
                                    <span>Show:</span>
                                    <select id="edit_items_per_page" onchange="changeModalItemsPerPage('edit', this.value)" class="px-1.5 py-0.5 rounded bg-slate-900 border border-slate-700 text-slate-200 text-xs focus:ring-indigo-500 focus:outline-none">
                                        <option value="10">10 per page</option>
                                        <option value="20">20 per page</option>
                                        <option value="50">50 per page</option>
                                        <option value="100">100 per page</option>
                                        <option value="9999">All</option>
                                    </select>
                                </div>
                                <span id="edit_pagination_info" class="font-medium text-slate-300">Showing 0 of 0</span>
                            </div>
                        </div>

                        <div class="bg-slate-950 p-3 rounded-lg border border-slate-800 max-h-[500px] overflow-y-auto space-y-2" style="max-height: 500px; overflow-y: auto;">
                            @forelse($availableQuestions as $q)
                                <div class="edit-q-item flex items-start space-x-3 p-2.5 rounded-lg bg-slate-900/60 hover:bg-slate-900 transition-colors border border-slate-800/60"
                                     data-name="{{ strtolower($q->name) }}"
                                     data-creator="{{ strtolower($q->creator?->name ?? 'system') }}"
                                     data-standard="{{ strtolower($q->standard?->name ?? '') }}"
                                     data-standard-id="{{ $q->standard_id }}"
                                     data-subject-id="{{ $q->subject_id }}"
                                     data-chapter-id="{{ $q->chapter_id }}"
                                     data-topic-id="{{ $q->topic_id }}"
                                     data-type="{{ $q->type }}">
                                    <input type="checkbox" name="question_ids[]" value="{{ $q->id }}" id="edit_q_add_{{ $q->id }}" class="edit-exam-q-checkbox mt-1 rounded bg-slate-900 border-slate-700 text-indigo-600 focus:ring-indigo-500 cursor-pointer">
                                    <div class="flex-1 text-xs">
                                        <div class="flex items-center justify-between gap-2">
                                            <label for="edit_q_add_{{ $q->id }}" class="font-medium text-slate-200 hover:text-white cursor-pointer flex-1">{{ $q->name }}</label>
                                            <div class="flex items-center space-x-2 shrink-0">
                                                <button type="button" onclick="event.preventDefault(); event.stopPropagation(); openQuestionPreviewModal({{ json_encode([
                                                    'id' => $q->id,
                                                    'name' => $q->name,
                                                    'description' => $q->description ?? '',
                                                    'marks' => $q->marks,
                                                    'type' => $q->type,
                                                    'standard_name' => $q->standard?->name ?? 'N/A',
                                                    'subject_name' => $q->subject?->name ?? 'N/A',
                                                    'chapter_name' => $q->chapter?->name ?? 'N/A',
                                                    'topic_name' => $q->topic?->name ?? 'N/A',
                                                    'creator_name' => $q->creator?->name ?? 'System',
                                                    'answers' => $q->answers->map(fn($a) => ['id' => $a->id, 'name' => $a->name, 'is_correct' => $a->is_correct])->toArray(),
                                                ]) }})" class="px-2 py-0.5 rounded bg-indigo-500/10 hover:bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 text-[11px] font-medium transition-all inline-flex items-center space-x-1 cursor-pointer">
                                                    <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                                                    <span>View</span>
                                                </button>
                                                <span class="text-amber-400 font-semibold">{{ $q->marks }} mark(s)</span>
                                            </div>
                                        </div>
                                        <label for="edit_q_add_{{ $q->id }}" class="flex items-center flex-wrap gap-2 mt-1 text-[11px] text-slate-400 cursor-pointer block">
                                            <span class="text-indigo-400 font-semibold">Class: {{ $q->standard?->name ?? 'N/A' }}</span>
                                            @if($q->subject)
                                                <span>&bull;</span>
                                                <span class="text-emerald-400 font-semibold">Subject: {{ $q->subject->name }}</span>
                                            @endif
                                            @if($q->chapter)
                                                <span>&bull;</span>
                                                <span class="text-cyan-400">Ch: {{ $q->chapter->name }}</span>
                                            @endif
                                            @if($q->topic)
                                                <span>&bull;</span>
                                                <span class="text-purple-400">Topic: {{ $q->topic->name }}</span>
                                            @endif
                                            <span>&bull;</span>
                                            <span>By: {{ $q->creator?->name ?? 'System' }}</span>
                                            <span>&bull;</span>
                                            <span>Type: @if($q->type == 1) Single Option @elseif($q->type == 2) Multiple Option @else Text Entry @endif</span>
                                        </label>
                                    </div>
                                </div>
                            @empty
                                <p class="text-xs text-slate-500 text-center py-4">No questions available in Question Bank.</p>
                            @endforelse
                        </div>

                        <!-- Modal Pagination Footer for Edit -->
                        <div class="mt-2 flex items-center justify-between text-xs">
                            <div class="flex items-center space-x-1">
                                <button type="button" id="edit_prev_btn" onclick="prevModalPage('edit')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 disabled:opacity-40 disabled:cursor-not-allowed text-slate-300 text-[11px] font-semibold border border-slate-700 cursor-pointer">&larr; Prev</button>
                                <div id="edit_page_numbers" class="flex items-center space-x-1"></div>
                                <button type="button" id="edit_next_btn" onclick="nextModalPage('edit')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 disabled:opacity-40 disabled:cursor-not-allowed text-slate-300 text-[11px] font-semibold border border-slate-700 cursor-pointer">Next &rarr;</button>
                            </div>
                        </div>
                        @error('question_ids')
                            <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                        @enderror
                    </div>

                    <div class="pt-4 flex justify-end space-x-3 border-t border-slate-800">
                        <button type="button" onclick="document.getElementById('editExamModal').classList.add('hidden')" class="px-4 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-sm font-medium transition-colors cursor-pointer">Cancel</button>
                        <button type="submit" class="px-5 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-semibold shadow-lg shadow-indigo-600/30 transition-all cursor-pointer">Update Exam</button>
                    </div>
                </form>
            </div>
        </div>

        <!-- VIEW EXAM MODAL -->
        <div id="viewExamModal" class="hidden fixed inset-0 z-50 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4 overflow-y-auto">
            <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-6xl overflow-hidden shadow-2xl my-8">
                <div class="px-6 py-4 border-b border-slate-800 flex items-center justify-between bg-slate-950/50">
                    <h3 class="text-lg font-bold text-white flex items-center gap-2">
                        <svg class="w-5 h-5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                        <span>Exam Overview</span>
                    </h3>
                    <button onclick="document.getElementById('viewExamModal').classList.add('hidden')" class="text-slate-400 hover:text-white transition-colors cursor-pointer">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                    </button>
                </div>

                <div class="p-6 space-y-5">
                    <div>
                        <h4 id="view_exam_name" class="text-xl font-extrabold text-white"></h4>
                        <p class="text-xs text-slate-400 mt-1">Exam Details and Linked Questions</p>
                    </div>

                    <!-- Key Metadata Cards -->
                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
                        <div class="p-3 bg-slate-950 rounded-xl border border-slate-800">
                            <span class="block text-[10px] font-semibold text-slate-400 uppercase">Type</span>
                            <span id="view_exam_type" class="text-xs font-bold text-indigo-300 mt-0.5 block"></span>
                        </div>
                        <div class="p-3 bg-slate-950 rounded-xl border border-slate-800">
                            <span class="block text-[10px] font-semibold text-slate-400 uppercase">Status</span>
                            <span id="view_exam_status" class="text-xs font-bold text-emerald-400 mt-0.5 block"></span>
                        </div>
                        <div class="p-3 bg-slate-950 rounded-xl border border-slate-800">
                            <span class="block text-[10px] font-semibold text-slate-400 uppercase">Total Marks</span>
                            <span id="view_exam_total_mark" class="text-xs font-bold text-amber-400 mt-0.5 block"></span>
                        </div>
                        <div class="p-3 bg-slate-950 rounded-xl border border-slate-800">
                            <span class="block text-[10px] font-semibold text-slate-400 uppercase">Created By</span>
                            <span id="view_exam_creator" class="text-xs font-bold text-slate-200 mt-0.5 block"></span>
                        </div>
                    </div>

                    <!-- Questions List -->
                    <div>
                        <div class="flex items-center justify-between mb-2">
                            <h5 class="text-xs font-bold text-slate-300 uppercase tracking-wider">Linked Exam Questions</h5>
                            <span id="view_exam_q_count" class="text-[11px] text-indigo-300 font-semibold"></span>
                        </div>

                        <div id="view_exam_questions_list" class="bg-slate-950 p-3 rounded-xl border border-slate-800 max-h-[500px] overflow-y-auto space-y-2" style="max-height: 500px; overflow-y: auto;">
                            <!-- Populated dynamically via JS -->
                        </div>
                    </div>

                    <div class="pt-4 flex justify-between items-center border-t border-slate-800">
                        <a id="view_exam_manage_btn" href="#" class="px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold shadow-lg shadow-indigo-600/30 transition-all cursor-pointer flex items-center space-x-1.5">
                            <span>Open Full Exam Details & Question Manager &rarr;</span>
                        </a>
                        <button type="button" onclick="document.getElementById('viewExamModal').classList.add('hidden')" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-medium transition-colors cursor-pointer">Close</button>
                    </div>
                </div>
            </div>
        </div>

        <script>
            function toggleExamManagementDetails(examId) {
                const detailsBox = document.getElementById('details-exam-mgmt-' + examId);
                const chevron = document.getElementById('chevron-exam-mgmt-' + examId);
                if (detailsBox) {
                    detailsBox.classList.toggle('hidden');
                }
                if (chevron) {
                    chevron.classList.toggle('rotate-180');
                }
            }

            function openViewExamModal(data) {
                document.getElementById('view_exam_name').textContent = data.name || '';
                document.getElementById('view_exam_type').textContent = data.type || '';
                document.getElementById('view_exam_status').textContent = data.status || '';
                document.getElementById('view_exam_total_mark').textContent = (data.total_mark || 0) + ' Mark(s)';
                document.getElementById('view_exam_creator').textContent = data.creator || 'System';
                
                const manageBtn = document.getElementById('view_exam_manage_btn');
                if (manageBtn) {
                    manageBtn.href = data.show_url || '#';
                    if (data.has_completions) {
                        manageBtn.classList.add('hidden');
                    } else {
                        manageBtn.classList.remove('hidden');
                    }
                }

                const qListContainer = document.getElementById('view_exam_questions_list');
                const qCountBadge = document.getElementById('view_exam_q_count');
                qListContainer.innerHTML = '';

                const questions = data.questions || [];
                qCountBadge.textContent = questions.length + ' Question(s)';

                if (questions.length === 0) {
                    qListContainer.innerHTML = '<p class="text-xs text-slate-500 text-center py-6">No questions linked to this exam yet.</p>';
                } else {
                    questions.forEach((q, idx) => {
                        const qDataJson = JSON.stringify({
                            id: q.id,
                            name: q.name,
                            description: q.description || '',
                            marks: q.marks,
                            type: q.type_id || (q.type === 'Multiple Option' ? 2 : (q.type === 'Text Entry' ? 3 : 1)),
                            standard_name: q.standard || 'N/A',
                            creator_name: q.creator || 'System',
                            answers: q.answers || []
                        }).replace(/"/g, '&quot;');

                        const itemHtml = `
                            <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 hover:border-slate-700 transition-all flex items-start justify-between gap-3">
                                <div class="space-y-1 flex-1">
                                    <div class="flex items-center space-x-2">
                                        <span class="text-xs font-bold text-indigo-400">Q${idx + 1}.</span>
                                        <h6 class="text-xs font-semibold text-slate-200 hover:text-white transition-colors cursor-pointer" onclick="openQuestionPreviewModal(${qDataJson})">${q.name}</h6>
                                    </div>
                                    ${q.description ? `<p class="text-xs text-slate-400 pl-6 line-clamp-1">${q.description}</p>` : ''}
                                    <div class="flex items-center flex-wrap gap-2 mt-1.5 text-[11px] text-slate-400">
                                        <span class="px-2 py-0.5 rounded bg-indigo-500/10 text-indigo-300 border border-indigo-500/20 font-medium">Class: ${q.standard}</span>
                                        <span class="px-2 py-0.5 rounded bg-slate-800 text-slate-300 border border-slate-700">By: ${q.creator}</span>
                                        <span class="px-2 py-0.5 rounded bg-slate-800 text-slate-300 border border-slate-700">Type: ${q.type}</span>
                                    </div>
                                </div>
                                <div class="flex items-center space-x-2 shrink-0">
                                    <button type="button" onclick="openQuestionPreviewModal(${qDataJson})" class="px-2.5 py-1 rounded-lg bg-indigo-500/10 hover:bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 text-xs font-medium transition-all inline-flex items-center space-x-1 cursor-pointer">
                                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                                        <span>View</span>
                                    </button>
                                    <span class="text-xs font-bold text-amber-400 bg-amber-500/10 px-2 py-0.5 rounded border border-amber-500/20">${q.marks} Mark(s)</span>
                                </div>
                            </div>
                        `;
                        qListContainer.innerHTML += itemHtml;
                    });
                }

                document.getElementById('viewExamModal').classList.remove('hidden');
            }

            function openEditExamModal(data) {
                const actionUrl = '/exams/' + data.id;
                document.getElementById('editExamForm').action = actionUrl;
                document.getElementById('edit_action_url').value = actionUrl;
                document.getElementById('edit_exam_name').value = data.name || '';
                document.getElementById('edit_exam_type').value = data.type || 1;
                document.getElementById('edit_exam_duration').value = data.duration || '';
                toggleEditExamDuration(data.type || 1);
                document.getElementById('edit_exam_status').value = data.status || 1;

                const assignedStdIds = data.standard_ids || [];
                document.querySelectorAll('.edit-exam-std-checkbox').forEach(cb => {
                    cb.checked = assignedStdIds.includes(parseInt(cb.value));
                });

                const attachedIds = data.question_ids || [];
                document.querySelectorAll('.edit-exam-q-checkbox').forEach(cb => {
                    cb.checked = attachedIds.includes(parseInt(cb.value));
                });

                document.getElementById('editExamModal').classList.remove('hidden');
            }

            function toggleCreateExamDuration(typeVal) {
                const wrapper = document.getElementById('create_duration_wrapper');
                const input = document.getElementById('create_exam_duration');
                if (parseInt(typeVal) === 1) {
                    wrapper.classList.remove('hidden');
                    input.required = true;
                } else {
                    wrapper.classList.add('hidden');
                    input.required = false;
                }
            }

            function toggleEditExamDuration(typeVal) {
                const wrapper = document.getElementById('edit_duration_wrapper');
                const input = document.getElementById('edit_exam_duration');
                if (parseInt(typeVal) === 1) {
                    wrapper.classList.remove('hidden');
                    input.required = true;
                } else {
                    wrapper.classList.add('hidden');
                    input.required = false;
                }
            }

            const subjectsDataExam = @json($subjectsData);

            function onModalSubjectChange(prefix) {
                const subjectId = document.getElementById(prefix + '_search_q_subject')?.value || '';
                const chapterSelect = document.getElementById(prefix + '_search_q_chapter');
                const topicSelect = document.getElementById(prefix + '_search_q_topic');

                if (chapterSelect) {
                    chapterSelect.innerHTML = '<option value="">All Chapters</option>';
                }
                if (topicSelect) {
                    topicSelect.innerHTML = '<option value="">All Topics</option>';
                }

                if (subjectId && chapterSelect) {
                    const selectedSubject = subjectsDataExam.find(s => String(s.id) === String(subjectId));
                    if (selectedSubject && selectedSubject.chapters) {
                        selectedSubject.chapters.forEach(ch => {
                            const opt = document.createElement('option');
                            opt.value = ch.id;
                            opt.textContent = ch.name;
                            chapterSelect.appendChild(opt);
                        });
                    }
                }

                filterModalQuestions(prefix);
            }

            function onModalChapterChange(prefix) {
                const subjectId = document.getElementById(prefix + '_search_q_subject')?.value || '';
                const chapterId = document.getElementById(prefix + '_search_q_chapter')?.value || '';
                const topicSelect = document.getElementById(prefix + '_search_q_topic');

                if (topicSelect) {
                    topicSelect.innerHTML = '<option value="">All Topics</option>';
                }

                if (subjectId && chapterId && topicSelect) {
                    const selectedSubject = subjectsDataExam.find(s => String(s.id) === String(subjectId));
                    if (selectedSubject && selectedSubject.chapters) {
                        const selectedChapter = selectedSubject.chapters.find(c => String(c.id) === String(chapterId));
                        if (selectedChapter && selectedChapter.topics) {
                            selectedChapter.topics.forEach(tp => {
                                const opt = document.createElement('option');
                                opt.value = tp.id;
                                opt.textContent = tp.name;
                                topicSelect.appendChild(opt);
                            });
                        }
                    }
                }

                filterModalQuestions(prefix);
            }

            const modalState = {
                create: { currentPage: 1, itemsPerPage: 10, filteredItems: [] },
                edit: { currentPage: 1, itemsPerPage: 10, filteredItems: [] }
            };

            function filterModalQuestions(prefix) {
                const nameQuery = (document.getElementById(prefix + '_search_q_name')?.value || '').toLowerCase().trim();
                const creatorQuery = (document.getElementById(prefix + '_search_q_creator')?.value || '').toLowerCase().trim();
                const standardQuery = document.getElementById(prefix + '_search_q_standard')?.value || '';
                const subjectQuery = document.getElementById(prefix + '_search_q_subject')?.value || '';
                const chapterQuery = document.getElementById(prefix + '_search_q_chapter')?.value || '';
                const topicQuery = document.getElementById(prefix + '_search_q_topic')?.value || '';
                const typeQuery = document.getElementById(prefix + '_search_q_type')?.value || '';

                const items = Array.from(document.querySelectorAll('.' + prefix + '-q-item'));
                modalState[prefix].filteredItems = [];

                items.forEach(item => {
                    const qName = item.getAttribute('data-name') || '';
                    const qCreator = item.getAttribute('data-creator') || '';
                    const qStandard = item.getAttribute('data-standard') || '';
                    const qStandardId = item.getAttribute('data-standard-id') || '';
                    const qSubjectId = item.getAttribute('data-subject-id') || '';
                    const qChapterId = item.getAttribute('data-chapter-id') || '';
                    const qTopicId = item.getAttribute('data-topic-id') || '';
                    const qType = item.getAttribute('data-type') || '';

                    const matchesName = !nameQuery || qName.includes(nameQuery);
                    const matchesCreator = !creatorQuery || qCreator.includes(creatorQuery);
                    const matchesStandard = !standardQuery || qStandardId === standardQuery || qStandard.includes(standardQuery);
                    const matchesSubject = !subjectQuery || qSubjectId === subjectQuery;
                    const matchesChapter = !chapterQuery || qChapterId === chapterQuery;
                    const matchesTopic = !topicQuery || qTopicId === topicQuery;
                    const matchesType = !typeQuery || qType === typeQuery;

                    if (matchesName && matchesCreator && matchesStandard && matchesSubject && matchesChapter && matchesTopic && matchesType) {
                        modalState[prefix].filteredItems.push(item);
                    }
                });

                modalState[prefix].currentPage = 1;
                renderModalPagination(prefix);
            }

            function renderModalPagination(prefix) {
                const state = modalState[prefix];
                const total = state.filteredItems.length;
                const infoElem = document.getElementById(prefix + '_pagination_info');
                const pageNumbersElem = document.getElementById(prefix + '_page_numbers');
                const prevBtn = document.getElementById(prefix + '_prev_btn');
                const nextBtn = document.getElementById(prefix + '_next_btn');

                const allItems = document.querySelectorAll('.' + prefix + '-q-item');
                allItems.forEach(item => item.classList.add('hidden'));

                if (total === 0) {
                    if (infoElem) infoElem.textContent = 'Showing 0 of 0';
                    if (pageNumbersElem) pageNumbersElem.innerHTML = '';
                    if (prevBtn) prevBtn.disabled = true;
                    if (nextBtn) nextBtn.disabled = true;
                    return;
                }

                const totalPages = Math.ceil(total / state.itemsPerPage);
                if (state.currentPage > totalPages) state.currentPage = totalPages;
                if (state.currentPage < 1) state.currentPage = 1;

                const startIdx = (state.currentPage - 1) * state.itemsPerPage;
                const endIdx = Math.min(startIdx + state.itemsPerPage, total);

                for (let i = startIdx; i < endIdx; i++) {
                    if (state.filteredItems[i]) {
                        state.filteredItems[i].classList.remove('hidden');
                    }
                }

                if (infoElem) infoElem.textContent = `Showing ${startIdx + 1}-${endIdx} of ${total}`;
                if (prevBtn) prevBtn.disabled = (state.currentPage === 1);
                if (nextBtn) nextBtn.disabled = (state.currentPage === totalPages);

                if (pageNumbersElem) {
                    pageNumbersElem.innerHTML = '';
                    const maxVisible = 5;
                    let startPage = Math.max(1, state.currentPage - 2);
                    let endPage = Math.min(totalPages, startPage + maxVisible - 1);
                    if (endPage - startPage < maxVisible - 1) {
                        startPage = Math.max(1, endPage - maxVisible + 1);
                    }

                    for (let p = startPage; p <= endPage; p++) {
                        const btn = document.createElement('button');
                        btn.type = 'button';
                        btn.textContent = p;
                        btn.className = p === state.currentPage
                            ? 'px-2 py-0.5 rounded bg-indigo-600 text-white font-bold text-[11px] shadow-sm cursor-pointer'
                            : 'px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-[11px] border border-slate-700 cursor-pointer';
                        btn.onclick = () => { state.currentPage = p; renderModalPagination(prefix); };
                        pageNumbersElem.appendChild(btn);
                    }
                }
            }

            function prevModalPage(prefix) {
                if (modalState[prefix].currentPage > 1) {
                    modalState[prefix].currentPage--;
                    renderModalPagination(prefix);
                }
            }

            function nextModalPage(prefix) {
                const totalPages = Math.ceil(modalState[prefix].filteredItems.length / modalState[prefix].itemsPerPage);
                if (modalState[prefix].currentPage < totalPages) {
                    modalState[prefix].currentPage++;
                    renderModalPagination(prefix);
                }
            }

            function changeModalItemsPerPage(prefix, val) {
                modalState[prefix].itemsPerPage = parseInt(val, 10);
                modalState[prefix].currentPage = 1;
                renderModalPagination(prefix);
            }

            document.addEventListener('DOMContentLoaded', () => {
                filterModalQuestions('create');
                filterModalQuestions('edit');
                const createType = document.getElementById('create_exam_type');
                if (createType) toggleCreateExamDuration(createType.value);
            });
        </script>

        <!-- QUESTION PREVIEW POPUP MODAL -->
        <div id="questionPreviewModal" class="hidden fixed inset-0 z-50 bg-black/75 backdrop-blur-md flex items-center justify-center p-4 overflow-y-auto">
            <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-3xl overflow-hidden shadow-2xl my-8">
                <div class="px-6 py-4 border-b border-slate-800 flex items-center justify-between bg-slate-950/60">
                    <div class="flex items-center space-x-3">
                        <div class="w-9 h-9 rounded-xl bg-indigo-500/10 border border-indigo-500/30 text-indigo-400 font-bold flex items-center justify-center text-sm">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                        </div>
                        <div>
                            <h3 class="text-base font-extrabold text-white">Question Details Preview</h3>
                            <p class="text-xs text-slate-400">View question prompt and option answers</p>
                        </div>
                    </div>
                    <button type="button" onclick="document.getElementById('questionPreviewModal').classList.add('hidden')" class="text-slate-400 hover:text-white transition-colors cursor-pointer p-1">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                    </button>
                </div>

                <div class="p-6 space-y-5">
                    <!-- Question Heading & Badges -->
                    <div class="space-y-3 p-4 rounded-xl bg-slate-950 border border-slate-800">
                        <h4 id="preview_q_name" class="text-lg font-extrabold text-white leading-snug"></h4>
                        
                        <div class="flex items-center flex-wrap gap-2 text-xs">
                            <span id="preview_q_standard" class="px-2.5 py-1 rounded-lg bg-indigo-500/10 text-indigo-300 border border-indigo-500/30 font-semibold"></span>
                            <span id="preview_q_subject" class="hidden px-2.5 py-1 rounded-lg bg-emerald-500/10 text-emerald-300 border border-emerald-500/30 font-semibold"></span>
                            <span id="preview_q_chapter" class="hidden px-2.5 py-1 rounded-lg bg-cyan-500/10 text-cyan-300 border border-cyan-500/30 font-medium"></span>
                            <span id="preview_q_topic" class="hidden px-2.5 py-1 rounded-lg bg-purple-500/10 text-purple-300 border border-purple-500/30 font-medium"></span>
                            <span id="preview_q_type" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-200 border border-slate-700 font-medium"></span>
                            <span id="preview_q_marks" class="px-2.5 py-1 rounded-lg bg-amber-500/10 text-amber-400 border border-amber-500/30 font-bold"></span>
                            <span id="preview_q_creator" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 border border-slate-700"></span>
                        </div>
                    </div>

                    <!-- Description Container -->
                    <div id="preview_q_desc_container" class="hidden p-4 rounded-xl bg-slate-950/60 border border-slate-800">
                        <span class="block text-[11px] font-semibold text-slate-400 uppercase tracking-wider mb-1">Description / Explanation</span>
                        <p id="preview_q_description" class="text-xs text-slate-300 leading-relaxed"></p>
                    </div>

                    <!-- Options Container -->
                    <div>
                        <h5 class="text-xs font-semibold text-slate-300 uppercase tracking-wider mb-2.5">Answer Options</h5>
                        <div id="preview_q_answers_list" class="space-y-2">
                            <!-- Dynamically populated -->
                        </div>
                    </div>

                    <div class="pt-4 flex justify-end border-t border-slate-800">
                        <button type="button" onclick="document.getElementById('questionPreviewModal').classList.add('hidden')" class="px-5 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold transition-colors cursor-pointer">Close Preview</button>
                    </div>
                </div>
            </div>
        </div>

        <script>
            function openQuestionPreviewModal(data) {
                document.getElementById('preview_q_name').textContent = data.name || '';
                document.getElementById('preview_q_standard').textContent = 'Class: ' + (data.standard_name || 'N/A');

                const subjBadge = document.getElementById('preview_q_subject');
                if (data.subject_name && data.subject_name !== 'N/A') {
                    subjBadge.textContent = 'Subject: ' + data.subject_name;
                    subjBadge.classList.remove('hidden');
                } else {
                    subjBadge.classList.add('hidden');
                }

                const chBadge = document.getElementById('preview_q_chapter');
                if (data.chapter_name && data.chapter_name !== 'N/A') {
                    chBadge.textContent = 'Ch: ' + data.chapter_name;
                    chBadge.classList.remove('hidden');
                } else {
                    chBadge.classList.add('hidden');
                }

                const tpBadge = document.getElementById('preview_q_topic');
                if (data.topic_name && data.topic_name !== 'N/A') {
                    tpBadge.textContent = 'Topic: ' + data.topic_name;
                    tpBadge.classList.remove('hidden');
                } else {
                    tpBadge.classList.add('hidden');
                }
                
                let typeStr = 'Single Option';
                if (parseInt(data.type) === 2) typeStr = 'Multiple Option';
                if (parseInt(data.type) === 3) typeStr = 'Text Entry';
                document.getElementById('preview_q_type').textContent = 'Type: ' + typeStr;

                document.getElementById('preview_q_marks').textContent = (data.marks || 0) + ' Mark(s)';
                document.getElementById('preview_q_creator').textContent = 'By: ' + (data.creator_name || 'System');

                const descContainer = document.getElementById('preview_q_desc_container');
                const descText = document.getElementById('preview_q_description');
                if (data.description && data.description.trim() !== '') {
                    descText.textContent = data.description;
                    descContainer.classList.remove('hidden');
                } else {
                    descContainer.classList.add('hidden');
                }

                const answersList = document.getElementById('preview_q_answers_list');
                answersList.innerHTML = '';

                const answers = data.answers || [];
                if (parseInt(data.type) === 3) {
                    answersList.innerHTML = '<p class="text-xs text-slate-400 italic p-3 rounded-lg bg-slate-950 border border-slate-800">Students will type a written text answer for this question.</p>';
                } else if (answers.length === 0) {
                    answersList.innerHTML = '<p class="text-xs text-slate-500 italic p-3 rounded-lg bg-slate-950 border border-slate-800">No answer options configured.</p>';
                } else {
                    answers.forEach((ans, idx) => {
                        const isCorrect = parseInt(ans.is_correct) === 1;
                        const itemHtml = `
                            <div class="p-3 rounded-xl border flex items-center justify-between text-xs transition-all ${
                                isCorrect
                                    ? 'bg-emerald-950/30 border-emerald-500/40 text-emerald-200 font-semibold'
                                    : 'bg-slate-950 border-slate-800 text-slate-300'
                            }">
                                <div class="flex items-center space-x-2.5">
                                    <span class="w-6 text-[11px] font-bold ${isCorrect ? 'text-emerald-400' : 'text-slate-500'}">#${idx + 1}</span>
                                    <span>${ans.name}</span>
                                </div>
                                ${
                                    isCorrect
                                        ? '<span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-extrabold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 uppercase tracking-wider">✓ Correct Answer</span>'
                                        : ''
                                }
                            </div>
                        `;
                        answersList.innerHTML += itemHtml;
                    });
                }

                document.getElementById('questionPreviewModal').classList.remove('hidden');
            }
        </script>

        <x-exam-leaderboard-modal />

    </div>
</x-layouts.app>
