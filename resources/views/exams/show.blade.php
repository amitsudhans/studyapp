<x-layouts.app title="Exam Details - {{ $exam->name }}">
    <div class="py-8 w-full px-4 sm:px-6 lg:px-8 space-y-8">
        
        <!-- Header Banner & Navigation -->
        <div class="relative overflow-hidden rounded-2xl bg-gradient-to-r from-indigo-950 via-slate-900 to-slate-900 border border-indigo-500/30 p-6 sm:p-8 shadow-2xl">
            <div class="relative z-10 flex flex-col md:flex-row md:items-center md:justify-between gap-6">
                <div>
                    <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-indigo-500/20 border border-indigo-500/40 text-indigo-300 text-xs font-semibold uppercase tracking-wider mb-3">
                        <span class="w-2 h-2 rounded-full bg-indigo-400 animate-pulse"></span>
                        <span>Exam Overview & Questions</span>
                    </div>
                    <h1 class="text-3xl font-extrabold text-white tracking-tight sm:text-4xl">
                        {{ $exam->name }}
                    </h1>
                    <div class="mt-2 flex items-center flex-wrap gap-3 text-xs text-slate-300">
                        <span>Created by: <strong class="text-white">{{ $exam->creator?->name ?? 'System' }}</strong></span>
                        <span>&bull;</span>
                        <span>Type: 
                            @if($exam->type == 1)
                                <span class="text-indigo-400 font-semibold">Timed ({{ $exam->duration ? $exam->duration . ' mins' : '1' }})</span>
                            @else
                                <span class="text-slate-400 font-semibold">Non-Timed (2)</span>
                            @endif
                        </span>
                        <span>&bull;</span>
                        <span>Status: 
                            @if($exam->status == 1)
                                <span class="text-emerald-400 font-semibold">Active (1)</span>
                            @else
                                <span class="text-rose-400 font-semibold">Inactive (2)</span>
                            @endif
                        </span>
                    </div>
                </div>

                <div class="flex items-center flex-wrap gap-3">
                    <a href="{{ route('exams.index') }}" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium text-sm transition-all flex items-center space-x-2">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
                        </svg>
                        <span>Back to Exams</span>
                    </a>

                    <button type="button" onclick="openExamLeaderboardModal({{ $exam->id }}, '{{ addslashes($exam->name) }}')" class="px-4 py-2.5 rounded-xl bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 border border-amber-500/40 font-bold text-sm transition-all flex items-center space-x-2 cursor-pointer shadow-md">
                        <span>🏆 View Leaderboard</span>
                    </button>

                    @php
                        $hasCompletions = ($exam->student_exam_details_count ?? 0) > 0;
                    @endphp

                    @if(!$hasCompletions)
                        <button onclick="document.getElementById('editExamDetailsModal').classList.remove('hidden')" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium text-sm transition-all flex items-center space-x-2 cursor-pointer">
                            <svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                            </svg>
                            <span>Edit Exam Name</span>
                        </button>
                    @else
                        <span class="px-3 py-2 rounded-xl bg-amber-500/10 text-amber-400 border border-amber-500/20 text-xs font-semibold inline-flex items-center">
                            <svg class="w-4 h-4 mr-1.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/></svg>
                            Completed by Student (Locked)
                        </span>
                    @endif
                </div>
            </div>
        </div>

        <!-- Metric Stat Cards -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-6">
            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Total Questions</span>
                    <div class="p-2 bg-indigo-500/10 rounded-lg text-indigo-400">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                    </div>
                </div>
                <p class="mt-4 text-3xl font-extrabold text-white">{{ $exam->questions->count() }}</p>
                <p class="mt-1 text-xs text-slate-400">Linked to this exam in <code class="text-indigo-300">exam_questions</code></p>
            </div>

            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Total Mark</span>
                    <div class="p-2 bg-amber-500/10 rounded-lg text-amber-400">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                    </div>
                </div>
                <p class="mt-4 text-3xl font-extrabold text-amber-400">{{ $exam->total_mark }}</p>
                <p class="mt-1 text-xs text-slate-400">Calculated sum of question marks</p>
            </div>

            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Available Questions</span>
                    <div class="p-2 bg-emerald-500/10 rounded-lg text-emerald-400">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
                    </div>
                </div>
                <p class="mt-4 text-3xl font-extrabold text-white">{{ $availableQuestions->count() }}</p>
                <p class="mt-1 text-xs text-slate-400">Questions in bank available to add</p>
            </div>
        </div>

        <!-- ASSIGNED STANDARDS SECTION (Table: exam_assign) -->
        <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl space-y-4">
            <div class="flex items-center justify-between">
                <div>
                    <h3 class="text-lg font-bold text-white flex items-center gap-2">
                        <svg class="w-5 h-5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>
                        <span>Assigned Standards / Classes (Table: exam_assign)</span>
                    </h3>
                    <p class="text-xs text-slate-400 mt-0.5">Standards linked to this exam. Teachers and Administrators are permitted to assign exams to standards.</p>
                </div>
                <span class="text-xs text-slate-400 bg-slate-800 px-3 py-1 rounded-full border border-slate-700">
                    {{ $exam->standards->count() }} Standard(s) Assigned
                </span>
            </div>

            @if(auth()->user()->canAssignExams())
                <form method="POST" action="{{ route('exams.assign-standards', $exam) }}" class="space-y-4 pt-2">
                    @csrf
                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
                        @foreach($standards as $std)
                            <label class="p-3 rounded-xl bg-slate-950 border border-slate-800 hover:border-indigo-500/40 cursor-pointer flex items-center space-x-3 transition-colors">
                                <input type="checkbox" name="standard_ids[]" value="{{ $std->id }}" {{ $exam->standards->contains($std->id) ? 'checked' : '' }} class="rounded bg-slate-900 border-slate-700 text-indigo-600 focus:ring-indigo-500">
                                <span class="text-xs font-semibold text-slate-200">{{ $std->name }}</span>
                            </label>
                        @endforeach
                    </div>

                    <div class="flex items-center justify-between pt-2 border-t border-slate-800/80">
                        <div class="flex items-center space-x-2">
                            <label for="assignment_status_select" class="text-xs font-medium text-slate-400">Assignment Status:</label>
                            <select id="assignment_status_select" name="status" class="px-2.5 py-1 rounded-lg bg-slate-950 border border-slate-700 text-slate-200 text-xs focus:ring-indigo-500">
                                <option value="1">1 - Active</option>
                                <option value="2">2 - Inactive</option>
                            </select>
                        </div>
                        <button type="submit" class="px-5 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-xs transition-all shadow-lg shadow-indigo-600/30 cursor-pointer flex items-center space-x-1.5">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                            <span>Save Standard Assignments</span>
                        </button>
                    </div>
                </form>
            @else
                <div class="flex items-center flex-wrap gap-2 pt-2">
                    @forelse($exam->standards as $std)
                        <span class="px-3 py-1 rounded-lg bg-indigo-500/10 text-indigo-300 border border-indigo-500/20 text-xs font-semibold">
                            {{ $std->name }}
                        </span>
                    @empty
                        <p class="text-xs text-slate-500 italic">No standards currently assigned to this exam.</p>
                    @endforelse
                </div>
            @endif
        </div>

        <!-- SECTION 1: QUESTIONS IN THIS EXAM -->
        <div class="bg-slate-900 border border-slate-800 rounded-2xl shadow-xl overflow-hidden">
            <div class="px-6 py-5 border-b border-slate-800 flex items-center justify-between">
                <div class="flex items-center space-x-2">
                    <div class="w-3 h-3 rounded-full bg-emerald-400"></div>
                    <h3 class="text-lg font-semibold text-white">Questions in this Exam ({{ $exam->questions->count() }})</h3>
                </div>
                <span class="text-xs text-slate-400 bg-slate-800 px-3 py-1 rounded-full border border-slate-700">Updated in Table: exam_questions</span>
            </div>

            <div class="divide-y divide-slate-800">
                @forelse($exam->questions as $index => $q)
                    <div class="p-6 hover:bg-slate-800/30 transition-colors flex flex-col md:flex-row md:items-center justify-between gap-4">
                        <div class="space-y-2 max-w-3xl">
                            <div class="flex items-center space-x-3">
                                <span class="w-7 h-7 rounded-lg bg-indigo-500/20 border border-indigo-500/40 text-indigo-300 font-bold flex items-center justify-center text-xs shrink-0">
                                    #{{ $index + 1 }}
                                </span>
                                <h4 class="text-base font-semibold text-white">{{ $q->name }}</h4>
                            </div>

                            @if($q->description)
                                <p class="text-xs text-slate-400 pl-10">{{ $q->description }}</p>
                            @endif

                            <div class="flex items-center flex-wrap gap-2 pl-10 pt-1 text-xs">
                                <span class="px-2.5 py-0.5 rounded-md bg-slate-800 text-slate-200 border border-slate-700">
                                    Standard: {{ $q->standard?->name ?? 'N/A' }}
                                </span>

                                @if($q->type == 1)
                                    <span class="px-2.5 py-0.5 rounded-full bg-indigo-500/10 text-indigo-400 border border-indigo-500/20 font-medium">Single Option</span>
                                @elseif($q->type == 2)
                                    <span class="px-2.5 py-0.5 rounded-full bg-violet-500/10 text-violet-400 border border-violet-500/20 font-medium">Multiple Option</span>
                                @else
                                    <span class="px-2.5 py-0.5 rounded-full bg-amber-500/10 text-amber-400 border border-amber-500/20 font-medium">Text Entry</span>
                                @endif

                                <span class="px-2.5 py-0.5 rounded-md bg-amber-500/10 text-amber-300 border border-amber-500/20 font-semibold">
                                    {{ $q->marks }} Mark(s)
                                </span>
                            </div>

                            <!-- Options Preview -->
                            @if($q->answers->isNotEmpty())
                                <div class="pl-10 pt-2 grid grid-cols-1 sm:grid-cols-2 gap-2">
                                    @foreach($q->answers as $ans)
                                        <div class="text-xs p-2 rounded-lg bg-slate-950/80 border border-slate-800 flex items-center justify-between">
                                            <span class="text-slate-300 truncate">{{ $ans->name }}</span>
                                            @if($ans->is_correct == 1)
                                                <span class="text-[10px] text-emerald-400 font-bold uppercase shrink-0 px-1.5 py-0.5 rounded bg-emerald-500/10 border border-emerald-500/20">Correct</span>
                                            @endif
                                        </div>
                                    @endforeach
                                </div>
                            @endif
                        </div>

                        <!-- Action Buttons -->
                        <div class="shrink-0 flex items-center justify-end space-x-2">
                            <button type="button" onclick="openQuestionPreviewModal({{ json_encode([
                                'id' => $q->id,
                                'name' => $q->name,
                                'description' => $q->description ?? '',
                                'marks' => $q->marks,
                                'type' => $q->type,
                                'standard_name' => $q->standard?->name ?? 'N/A',
                                'creator_name' => $q->creator?->name ?? 'System',
                                'answers' => $q->answers->map(fn($a) => ['id' => $a->id, 'name' => $a->name, 'is_correct' => $a->is_correct])->toArray(),
                            ]) }})" class="px-3.5 py-2 rounded-xl bg-indigo-500/10 hover:bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 text-xs font-semibold transition-colors flex items-center space-x-1.5 cursor-pointer">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                                <span>View Details</span>
                            </button>

                            @if(!$hasCompletions)
                                <form method="POST" action="{{ route('exams.questions.remove', [$exam, $q]) }}" onsubmit="return confirm('Remove this question from the exam?')">
                                    @csrf
                                    @method('DELETE')
                                    <button type="submit" class="px-3.5 py-2 rounded-xl bg-red-950/80 hover:bg-red-900 text-red-300 border border-red-800/40 text-xs font-semibold transition-colors flex items-center space-x-1.5 cursor-pointer">
                                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/></svg>
                                        <span>Remove from Exam</span>
                                    </button>
                                </form>
                            @endif
                        </div>
                    </div>
                @empty
                    <div class="p-12 text-center text-slate-500">
                        <svg class="w-12 h-12 mx-auto text-slate-600 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                        <p class="text-base font-medium text-slate-400">No questions attached to this exam yet.</p>
                        <p class="text-xs text-slate-500 mt-1">Select questions below from the Question Bank to add them to this exam.</p>
                    </div>
                @endforelse
            </div>
        </div>

        <!-- SECTION 2: ADD QUESTIONS FROM QUESTION BANK -->
        <div class="bg-slate-900 border border-slate-800 rounded-2xl shadow-xl overflow-hidden">
            <div class="px-6 py-5 border-b border-slate-800 flex flex-col sm:flex-row sm:items-center justify-between gap-4 bg-slate-950/40">
                <div>
                    <h3 class="text-lg font-semibold text-white">Add Questions from Question Bank</h3>
                    <p class="text-xs text-slate-400">Select available questions below to attach them to this exam in table <code class="text-indigo-300">exam_questions</code></p>
                </div>
                <span class="text-xs text-slate-400 bg-slate-800 px-3 py-1 rounded-full border border-slate-700 shrink-0">Available: {{ $availableQuestions->count() }}</span>
            </div>

            @if($hasCompletions)
                <div class="p-8 text-center bg-slate-950/60 border-t border-slate-800 text-amber-400">
                    <p class="text-sm font-semibold flex items-center justify-center gap-2">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/></svg>
                        This exam has been completed by student(s). Adding or removing questions is locked to maintain result data integrity.
                    </p>
                </div>
            @elseif($availableQuestions->isNotEmpty())
                <div class="p-6 border-b border-slate-800 bg-slate-950/60">
                    <!-- Search & Filter Controls -->
                    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 lg:grid-cols-7 gap-3">
                        <!-- Search by Name -->
                        <div>
                            <label for="search_q_name" class="block text-[11px] font-semibold text-slate-300 uppercase tracking-wider mb-1">Question Name</label>
                            <input type="text" id="search_q_name" oninput="filterQuestionsShowPage()" placeholder="Search name..." class="w-full px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-200 placeholder-slate-500 text-xs focus:outline-none focus:ring-2 focus:ring-indigo-500">
                        </div>

                        <!-- Search by Created By -->
                        <div>
                            <label for="search_q_creator" class="block text-[11px] font-semibold text-slate-300 uppercase tracking-wider mb-1">Created By</label>
                            <input type="text" id="search_q_creator" oninput="filterQuestionsShowPage()" placeholder="Search creator..." class="w-full px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-200 placeholder-slate-500 text-xs focus:outline-none focus:ring-2 focus:ring-indigo-500">
                        </div>

                        <!-- Search by Class / Standard -->
                        <div>
                            <label for="search_q_standard" class="block text-[11px] font-semibold text-slate-300 uppercase tracking-wider mb-1">Class / Standard</label>
                            <select id="search_q_standard" onchange="filterQuestionsShowPage()" class="w-full px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-200 text-xs focus:outline-none focus:ring-2 focus:ring-indigo-500">
                                <option value="">All Classes</option>
                                @foreach($standards as $std)
                                    <option value="{{ $std->id }}">{{ $std->name }}</option>
                                @endforeach
                            </select>
                        </div>

                        <!-- Search by Subject -->
                        <div>
                            <label for="search_q_subject" class="block text-[11px] font-semibold text-slate-300 uppercase tracking-wider mb-1">Subject</label>
                            <select id="search_q_subject" onchange="onShowSubjectChange()" class="w-full px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-200 text-xs focus:outline-none focus:ring-2 focus:ring-indigo-500">
                                <option value="">All Subjects</option>
                                @foreach($subjectsData as $subj)
                                    <option value="{{ $subj->id }}">{{ $subj->name }}</option>
                                @endforeach
                            </select>
                        </div>

                        <!-- Search by Chapter -->
                        <div>
                            <label for="search_q_chapter" class="block text-[11px] font-semibold text-slate-300 uppercase tracking-wider mb-1">Chapter</label>
                            <select id="search_q_chapter" onchange="onShowChapterChange()" class="w-full px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-200 text-xs focus:outline-none focus:ring-2 focus:ring-indigo-500">
                                <option value="">All Chapters</option>
                            </select>
                        </div>

                        <!-- Search by Topic -->
                        <div>
                            <label for="search_q_topic" class="block text-[11px] font-semibold text-slate-300 uppercase tracking-wider mb-1">Topic</label>
                            <select id="search_q_topic" onchange="filterQuestionsShowPage()" class="w-full px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-200 text-xs focus:outline-none focus:ring-2 focus:ring-indigo-500">
                                <option value="">All Topics</option>
                            </select>
                        </div>

                        <!-- Search by Question Type -->
                        <div>
                            <label for="search_q_type" class="block text-[11px] font-semibold text-slate-300 uppercase tracking-wider mb-1">Question Type</label>
                            <select id="search_q_type" onchange="filterQuestionsShowPage()" class="w-full px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-200 text-xs focus:outline-none focus:ring-2 focus:ring-indigo-500">
                                <option value="">All Types</option>
                                <option value="1">1 - Single Option</option>
                                <option value="2">2 - Multiple Option</option>
                                <option value="3">3 - Text Entry</option>
                            </select>
                        </div>
                    </div>

                    <div class="mt-3 flex flex-col sm:flex-row sm:items-center justify-between gap-3 pt-2 border-t border-slate-800/60">
                        <!-- Per page selector & page info -->
                        <div class="flex items-center space-x-3 text-xs text-slate-400">
                            <div class="flex items-center space-x-1.5">
                                <span>Show:</span>
                                <select id="show_items_per_page" onchange="changeItemsPerPageShowPage(this.value)" class="px-2 py-1 rounded bg-slate-900 border border-slate-700 text-slate-200 text-xs focus:ring-indigo-500 focus:outline-none">
                                    <option value="10">10 per page</option>
                                    <option value="20">20 per page</option>
                                    <option value="50">50 per page</option>
                                    <option value="100">100 per page</option>
                                    <option value="9999">All</option>
                                </select>
                            </div>
                            <span id="show_pagination_info" class="font-medium text-slate-300">Showing 0 of 0</span>
                        </div>

                        <div class="flex items-center space-x-2">
                            <button type="button" onclick="resetQuestionsSearchShowPage()" class="text-xs text-indigo-400 hover:text-indigo-300 font-medium underline flex items-center space-x-1 cursor-pointer mr-2">
                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/></svg>
                                <span>Clear Filters</span>
                            </button>
                        </div>
                    </div>
                </div>

                <form method="POST" action="{{ route('exams.questions.add', $exam) }}" class="p-6">
                    @csrf
                    
                    <div class="space-y-3 max-h-[500px] overflow-y-auto pr-2" style="max-height: 500px; overflow-y: auto;">
                        @foreach($availableQuestions as $q)
                            <div class="available-q-item p-3.5 rounded-xl bg-slate-950 border border-slate-800/80 hover:border-indigo-500/40 transition-all flex items-start space-x-3"
                                 data-name="{{ strtolower($q->name) }}"
                                 data-creator="{{ strtolower($q->creator?->name ?? 'system') }}"
                                 data-standard="{{ strtolower($q->standard?->name ?? '') }}"
                                 data-standard-id="{{ $q->standard_id }}"
                                 data-subject-id="{{ $q->subject_id }}"
                                 data-chapter-id="{{ $q->chapter_id }}"
                                 data-topic-id="{{ $q->topic_id }}"
                                 data-type="{{ $q->type }}">
                                <input type="checkbox" name="question_ids[]" value="{{ $q->id }}" id="q_add_{{ $q->id }}" class="mt-1 rounded bg-slate-900 border-slate-700 text-indigo-600 focus:ring-indigo-500 cursor-pointer">
                                <div class="flex-1">
                                    <div class="flex items-center justify-between gap-2">
                                        <label for="q_add_{{ $q->id }}" class="cursor-pointer flex-1">
                                            <h5 class="text-sm font-semibold text-white hover:text-indigo-300 transition-colors">{{ $q->name }}</h5>
                                        </label>
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
                                            ]) }})" class="px-2.5 py-1 rounded-lg bg-indigo-500/10 hover:bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 text-xs font-medium transition-all inline-flex items-center space-x-1 cursor-pointer">
                                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                                                <span>View</span>
                                            </button>
                                            <span class="text-xs font-bold text-amber-400 bg-amber-500/10 px-2 py-0.5 rounded border border-amber-500/20">{{ $q->marks }} Mark(s)</span>
                                        </div>
                                    </div>
                                    <label for="q_add_{{ $q->id }}" class="cursor-pointer block">
                                        @if($q->description)
                                            <p class="text-xs text-slate-400 mt-0.5 line-clamp-1">{{ $q->description }}</p>
                                        @endif
                                        <div class="flex items-center flex-wrap gap-2.5 mt-1.5 text-[11px] text-slate-400">
                                            <span class="px-2 py-0.5 rounded bg-indigo-500/10 text-indigo-300 border border-indigo-500/20 font-medium">
                                                Class: {{ $q->standard?->name ?? 'N/A' }}
                                            </span>
                                            @if($q->subject)
                                                <span class="px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-300 border border-emerald-500/20 font-medium">
                                                    Subject: {{ $q->subject->name }}
                                                </span>
                                            @endif
                                            @if($q->chapter)
                                                <span class="px-2 py-0.5 rounded bg-cyan-500/10 text-cyan-300 border border-cyan-500/20 font-medium">
                                                    Ch: {{ $q->chapter->name }}
                                                </span>
                                            @endif
                                            @if($q->topic)
                                                <span class="px-2 py-0.5 rounded bg-purple-500/10 text-purple-300 border border-purple-500/20 font-medium">
                                                    Topic: {{ $q->topic->name }}
                                                </span>
                                            @endif
                                            <span class="px-2 py-0.5 rounded bg-slate-800 text-slate-300 border border-slate-700">
                                                Created by: <strong class="text-slate-200">{{ $q->creator?->name ?? 'System' }}</strong>
                                            </span>
                                            <span class="px-2 py-0.5 rounded bg-slate-800 text-slate-300 border border-slate-700">
                                                Type: 
                                                @if($q->type == 1) Single Option @elseif($q->type == 2) Multiple Option @else Text Entry @endif
                                            </span>
                                        </div>
                                    </label>
                                </div>
                            </div>
                        @endforeach

                        <div id="no_search_results_msg" class="hidden p-8 text-center text-slate-500">
                            <p class="text-sm font-medium text-slate-400">No questions match your search filters.</p>
                            <button type="button" onclick="resetQuestionsSearchShowPage()" class="mt-2 text-xs text-indigo-400 hover:underline">Clear search filters</button>
                        </div>
                    </div>

                    <!-- Bottom Pagination Bar -->
                    <div class="mt-4 pt-4 border-t border-slate-800 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                        <div class="flex items-center space-x-1.5">
                            <button type="button" id="show_prev_btn" onclick="prevPageShowPage()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 disabled:opacity-40 disabled:cursor-not-allowed text-slate-200 font-semibold text-xs border border-slate-700 transition-all flex items-center space-x-1 cursor-pointer">
                                <span>&larr; Prev</span>
                            </button>
                            <div id="show_page_numbers" class="flex items-center space-x-1"></div>
                            <button type="button" id="show_next_btn" onclick="nextPageShowPage()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 disabled:opacity-40 disabled:cursor-not-allowed text-slate-200 font-semibold text-xs border border-slate-700 transition-all flex items-center space-x-1 cursor-pointer">
                                <span>Next &rarr;</span>
                            </button>
                        </div>

                        <button type="submit" class="px-6 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-sm transition-all shadow-lg shadow-indigo-600/30 flex items-center space-x-2 cursor-pointer">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
                            <span>Add Selected Questions to Exam</span>
                        </button>
                    </div>
                </form>
            @else
                <div class="p-8 text-center text-slate-500">
                    <p class="text-sm text-slate-400">All available questions in the Question Bank have already been added to this exam!</p>
                    <a href="{{ route('questions.index') }}" class="mt-3 inline-flex items-center space-x-1 text-xs text-indigo-400 hover:text-indigo-300 font-semibold">
                        <span>Create new questions in Question Bank &rarr;</span>
                    </a>
                </div>
            @endif
        </div>

        <script>
            const subjectsDataExamShow = @json($subjectsData);
            let showCurrentPage = 1;
            let showItemsPerPage = 10;
            let showFilteredItems = [];

            function onShowSubjectChange() {
                const subjectId = document.getElementById('search_q_subject')?.value || '';
                const chapterSelect = document.getElementById('search_q_chapter');
                const topicSelect = document.getElementById('search_q_topic');

                if (chapterSelect) chapterSelect.innerHTML = '<option value="">All Chapters</option>';
                if (topicSelect) topicSelect.innerHTML = '<option value="">All Topics</option>';

                if (subjectId && chapterSelect) {
                    const selectedSubject = subjectsDataExamShow.find(s => String(s.id) === String(subjectId));
                    if (selectedSubject && selectedSubject.chapters) {
                        selectedSubject.chapters.forEach(ch => {
                            const opt = document.createElement('option');
                            opt.value = ch.id;
                            opt.textContent = ch.name;
                            chapterSelect.appendChild(opt);
                        });
                    }
                }

                filterQuestionsShowPage();
            }

            function onShowChapterChange() {
                const subjectId = document.getElementById('search_q_subject')?.value || '';
                const chapterId = document.getElementById('search_q_chapter')?.value || '';
                const topicSelect = document.getElementById('search_q_topic');

                if (topicSelect) topicSelect.innerHTML = '<option value="">All Topics</option>';

                if (subjectId && chapterId && topicSelect) {
                    const selectedSubject = subjectsDataExamShow.find(s => String(s.id) === String(subjectId));
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

                filterQuestionsShowPage();
            }

            function filterQuestionsShowPage() {
                const nameQuery = (document.getElementById('search_q_name')?.value || '').toLowerCase().trim();
                const creatorQuery = (document.getElementById('search_q_creator')?.value || '').toLowerCase().trim();
                const standardQuery = document.getElementById('search_q_standard')?.value || '';
                const subjectQuery = document.getElementById('search_q_subject')?.value || '';
                const chapterQuery = document.getElementById('search_q_chapter')?.value || '';
                const topicQuery = document.getElementById('search_q_topic')?.value || '';
                const typeQuery = document.getElementById('search_q_type')?.value || '';

                const items = Array.from(document.querySelectorAll('.available-q-item'));
                showFilteredItems = [];

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
                        showFilteredItems.push(item);
                    }
                });

                const noResultsMsg = document.getElementById('no_search_results_msg');
                if (noResultsMsg) {
                    noResultsMsg.classList.toggle('hidden', showFilteredItems.length > 0);
                }

                showCurrentPage = 1;
                renderPaginationShowPage();
            }

            function renderPaginationShowPage() {
                const total = showFilteredItems.length;
                const infoElem = document.getElementById('show_pagination_info');
                const pageNumbersElem = document.getElementById('show_page_numbers');
                const prevBtn = document.getElementById('show_prev_btn');
                const nextBtn = document.getElementById('show_next_btn');

                if (total === 0) {
                    if (infoElem) infoElem.textContent = 'Showing 0 of 0';
                    if (pageNumbersElem) pageNumbersElem.innerHTML = '';
                    if (prevBtn) prevBtn.disabled = true;
                    if (nextBtn) nextBtn.disabled = true;
                    
                    const allItems = document.querySelectorAll('.available-q-item');
                    allItems.forEach(item => item.classList.add('hidden'));
                    return;
                }

                const totalPages = Math.ceil(total / showItemsPerPage);
                if (showCurrentPage > totalPages) showCurrentPage = totalPages;
                if (showCurrentPage < 1) showCurrentPage = 1;

                const startIdx = (showCurrentPage - 1) * showItemsPerPage;
                const endIdx = Math.min(startIdx + showItemsPerPage, total);

                // Hide all items first
                const allItems = document.querySelectorAll('.available-q-item');
                allItems.forEach(item => item.classList.add('hidden'));

                // Show slice for current page
                for (let i = startIdx; i < endIdx; i++) {
                    if (showFilteredItems[i]) {
                        showFilteredItems[i].classList.remove('hidden');
                    }
                }

                // Update text summary
                if (infoElem) {
                    infoElem.textContent = `Showing ${startIdx + 1}-${endIdx} of ${total} questions`;
                }

                // Update prev/next buttons
                if (prevBtn) prevBtn.disabled = (showCurrentPage === 1);
                if (nextBtn) nextBtn.disabled = (showCurrentPage === totalPages);

                // Render page buttons
                if (pageNumbersElem) {
                    pageNumbersElem.innerHTML = '';

                    const maxVisible = 5;
                    let startPage = Math.max(1, showCurrentPage - 2);
                    let endPage = Math.min(totalPages, startPage + maxVisible - 1);
                    if (endPage - startPage < maxVisible - 1) {
                        startPage = Math.max(1, endPage - maxVisible + 1);
                    }

                    if (startPage > 1) {
                        const firstBtn = document.createElement('button');
                        firstBtn.type = 'button';
                        firstBtn.textContent = '1';
                        firstBtn.className = 'px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs border border-slate-700 cursor-pointer';
                        firstBtn.onclick = () => { showCurrentPage = 1; renderPaginationShowPage(); };
                        pageNumbersElem.appendChild(firstBtn);

                        if (startPage > 2) {
                            const dots = document.createElement('span');
                            dots.className = 'px-1 text-slate-500 text-xs';
                            dots.textContent = '...';
                            pageNumbersElem.appendChild(dots);
                        }
                    }

                    for (let p = startPage; p <= endPage; p++) {
                        const btn = document.createElement('button');
                        btn.type = 'button';
                        btn.textContent = p;
                        btn.className = p === showCurrentPage
                            ? 'px-3 py-1 rounded-lg bg-indigo-600 text-white font-bold text-xs shadow-sm cursor-pointer'
                            : 'px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs border border-slate-700 cursor-pointer';
                        btn.onclick = () => { showCurrentPage = p; renderPaginationShowPage(); };
                        pageNumbersElem.appendChild(btn);
                    }

                    if (endPage < totalPages) {
                        if (endPage < totalPages - 1) {
                            const dots = document.createElement('span');
                            dots.className = 'px-1 text-slate-500 text-xs';
                            dots.textContent = '...';
                            pageNumbersElem.appendChild(dots);
                        }

                        const lastBtn = document.createElement('button');
                        lastBtn.type = 'button';
                        lastBtn.textContent = totalPages;
                        lastBtn.className = 'px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs border border-slate-700 cursor-pointer';
                        lastBtn.onclick = () => { showCurrentPage = totalPages; renderPaginationShowPage(); };
                        pageNumbersElem.appendChild(lastBtn);
                    }
                }
            }

            function prevPageShowPage() {
                if (showCurrentPage > 1) {
                    showCurrentPage--;
                    renderPaginationShowPage();
                }
            }

            function nextPageShowPage() {
                const totalPages = Math.ceil(showFilteredItems.length / showItemsPerPage);
                if (showCurrentPage < totalPages) {
                    showCurrentPage++;
                    renderPaginationShowPage();
                }
            }

            function changeItemsPerPageShowPage(val) {
                showItemsPerPage = parseInt(val, 10);
                showCurrentPage = 1;
                renderPaginationShowPage();
            }

            function resetQuestionsSearchShowPage() {
                if (document.getElementById('search_q_name')) document.getElementById('search_q_name').value = '';
                if (document.getElementById('search_q_creator')) document.getElementById('search_q_creator').value = '';
                if (document.getElementById('search_q_standard')) document.getElementById('search_q_standard').value = '';
                if (document.getElementById('search_q_subject')) document.getElementById('search_q_subject').value = '';
                if (document.getElementById('search_q_chapter')) document.getElementById('search_q_chapter').innerHTML = '<option value="">All Chapters</option>';
                if (document.getElementById('search_q_topic')) document.getElementById('search_q_topic').innerHTML = '<option value="">All Topics</option>';
                if (document.getElementById('search_q_type')) document.getElementById('search_q_type').value = '';
                filterQuestionsShowPage();
            }

            function toggleShowExamDuration(typeVal) {
                const wrapper = document.getElementById('show_duration_wrapper');
                const input = document.getElementById('show_exam_duration');
                if (parseInt(typeVal) === 1) {
                    wrapper.classList.remove('hidden');
                    input.required = true;
                } else {
                    wrapper.classList.add('hidden');
                    input.required = false;
                }
            }

            document.addEventListener('DOMContentLoaded', () => {
                filterQuestionsShowPage();
                const showType = document.getElementById('show_exam_type');
                if (showType) toggleShowExamDuration(showType.value);
            });
        </script>

        <!-- EDIT EXAM DETAILS MODAL -->
        <div id="editExamDetailsModal" class="hidden fixed inset-0 z-50 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4 overflow-y-auto">
            <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-4xl overflow-hidden shadow-2xl my-8">
                <div class="px-6 py-4 border-b border-slate-800 flex items-center justify-between bg-slate-950/50">
                    <h3 class="text-lg font-bold text-white">Edit Exam Details</h3>
                    <button onclick="document.getElementById('editExamDetailsModal').classList.add('hidden')" class="text-slate-400 hover:text-white transition-colors cursor-pointer">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                    </button>
                </div>

                <form method="POST" action="{{ route('exams.update', $exam) }}" class="p-6 space-y-4">
                    @csrf
                    @method('PUT')
                    <input type="hidden" name="_redirect_to_show" value="1">

                    <div>
                        <label for="show_exam_name" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Exam Name <span class="text-red-400">*</span></label>
                        <input type="text" id="show_exam_name" name="name" required value="{{ old('name', $exam->name) }}" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm">
                    </div>

                    <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                        <div>
                            <label for="show_exam_type" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Exam Type <span class="text-red-400">*</span></label>
                            <select id="show_exam_type" name="type" required onchange="toggleShowExamDuration(this.value)" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm">
                                <option value="1" {{ old('type', $exam->type) == 1 ? 'selected' : '' }}>1 - Timed</option>
                                <option value="2" {{ old('type', $exam->type) == 2 ? 'selected' : '' }}>2 - Non-Timed</option>
                            </select>
                        </div>

                        <div id="show_duration_wrapper" class="{{ old('type', $exam->type) == 2 ? 'hidden' : '' }}">
                            <label for="show_exam_duration" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Duration (Minutes) <span class="text-red-400">*</span></label>
                            <input type="number" id="show_exam_duration" name="duration" min="1" max="1440" value="{{ old('duration', $exam->duration ?? 60) }}" placeholder="e.g. 60" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm">
                        </div>

                        <div>
                            <label for="show_exam_status" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Status <span class="text-red-400">*</span></label>
                            <select id="show_exam_status" name="status" required class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm">
                                <option value="1" {{ old('status', $exam->status) == 1 ? 'selected' : '' }}>1 - Active</option>
                                <option value="2" {{ old('status', $exam->status) == 2 ? 'selected' : '' }}>2 - Inactive</option>
                            </select>
                        </div>
                    </div>

                    <div class="pt-4 flex justify-end space-x-3 border-t border-slate-800">
                        <button type="button" onclick="document.getElementById('editExamDetailsModal').classList.add('hidden')" class="px-4 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-sm font-medium transition-colors cursor-pointer">Cancel</button>
                        <button type="submit" class="px-5 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-semibold shadow-lg shadow-indigo-600/30 transition-all cursor-pointer">Update Exam</button>
                    </div>
                </form>
            </div>
        </div>

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
