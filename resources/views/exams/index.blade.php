<x-layouts.app title="Exam Performance & Submissions Report - Study App">
    <div class="py-8 w-full px-4 sm:px-6 lg:px-8 space-y-8">
        
        <!-- Header Banner -->
        <div class="relative overflow-hidden rounded-2xl bg-gradient-to-r from-indigo-950 via-slate-900 to-slate-900 border border-indigo-500/30 p-6 sm:p-8 shadow-2xl">
            <div class="relative z-10 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-6">
                <div>
                    <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-indigo-500/20 border border-indigo-500/40 text-indigo-300 text-xs font-semibold uppercase tracking-wider mb-3">
                        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                        <span>Exams & Performance Reports</span>
                    </div>
                    <h1 class="text-3xl font-extrabold text-white tracking-tight sm:text-4xl">
                        Exam Performance & Submissions Report
                    </h1>
                    <p class="mt-2 text-slate-300 text-sm max-w-xl">
                        Track student completions, scores, and question-level evaluation details, or create and manage exams.
                    </p>
                </div>

                <div class="flex items-center flex-wrap gap-3">
                    <a href="{{ route('dashboard') }}" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium text-sm transition-all flex items-center space-x-2">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
                        </svg>
                        <span>Dashboard</span>
                    </a>

                    <a href="{{ route('standards.index') }}" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700 font-medium text-sm transition-all flex items-center space-x-2">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
                        </svg>
                        <span>Standards</span>
                    </a>

                    <a href="{{ route('questions.index') }}" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-violet-300 border border-slate-700 font-medium text-sm transition-all flex items-center space-x-2">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                        </svg>
                        <span>Question Bank</span>
                    </a>

                    <a href="{{ route('students.index') }}" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-sky-300 border border-slate-700 font-medium text-sm transition-all flex items-center space-x-2">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z" />
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0112 20.055a11.952 11.952 0 01-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z" />
                        </svg>
                        <span>My Students</span>
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
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 shadow-lg">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Total Exams</span>
                    <div class="p-2 bg-indigo-500/10 rounded-lg text-indigo-400">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                    </div>
                </div>
                <p class="mt-3 text-2xl font-extrabold text-white">{{ $exams->total() }}</p>
                <p class="mt-0.5 text-xs text-slate-400">Created in the system</p>
            </div>

            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 shadow-lg">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Active Exams</span>
                    <div class="p-2 bg-emerald-500/10 rounded-lg text-emerald-400">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                    </div>
                </div>
                <p class="mt-3 text-2xl font-extrabold text-white">{{ $exams->filter(fn($e) => $e->status == 1)->count() }}</p>
                <p class="mt-0.5 text-xs text-slate-400">Status set to Active (1)</p>
            </div>

            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 shadow-lg">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Completions</span>
                    <div class="p-2 bg-sky-500/10 rounded-lg text-sky-400">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0112 20.055a11.952 11.952 0 01-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"/></svg>
                    </div>
                </div>
                <p class="mt-3 text-2xl font-extrabold text-white">{{ $examSubmissions->sum(fn($g) => $g->count()) }}</p>
                <p class="mt-0.5 text-xs text-slate-400">Student submissions</p>
            </div>

            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 shadow-lg">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Question Bank</span>
                    <div class="p-2 bg-violet-500/10 rounded-lg text-violet-400">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                    </div>
                </div>
                <p class="mt-3 text-2xl font-extrabold text-white">{{ $availableQuestions->count() }}</p>
                <p class="mt-0.5 text-xs text-slate-400">Questions in bank pool</p>
            </div>
        </div>

        <!-- Exams Directory List -->
        <div class="bg-slate-900 border border-slate-800 rounded-2xl shadow-xl overflow-hidden">
            <div class="px-6 py-5 border-b border-slate-800 flex items-center justify-between flex-wrap gap-4">
                <div>
                    <h3 class="text-lg font-semibold text-white flex items-center space-x-2">
                        <svg class="w-5 h-5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>
                        </svg>
                        <span>Exam Performance & Submissions Directory</span>
                        @if(request()->filled('name') || request()->filled('type') || request()->filled('syllabus_id') || request()->filled('subject_id') || request()->filled('chapter_id') || request()->filled('topic_id'))
                            <span class="text-xs px-2.5 py-0.5 rounded-full bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 font-medium">Filtered</span>
                        @endif
                    </h3>
                    <p class="text-xs text-slate-400 mt-0.5">Click any exam name to expand its details, student completion results, and manage questions</p>
                </div>
                <div class="flex items-center space-x-3">
                    <span class="text-xs text-slate-400 bg-slate-800 px-3 py-1 rounded-full border border-slate-700">Total: {{ $exams->total() }}</span>
                </div>
            </div>

            <!-- Exam Search & Curriculum Filter Bar -->
            <div class="p-4 sm:p-5 bg-slate-950/60 border-b border-slate-800/80">
                <form method="GET" action="{{ route('exams.index') }}" id="examFilterForm" class="space-y-3">
                    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-3">
                        <!-- Exam Name Search -->
                        <div>
                            <label class="block text-[11px] font-semibold text-slate-400 uppercase tracking-wider mb-1">Exam Name</label>
                            <div class="relative">
                                <input type="text" name="name" id="filter_exam_name" value="{{ request('name') }}" placeholder="Search exam name..." class="w-full pl-8 pr-3 py-2 bg-slate-900 border border-slate-800 rounded-xl text-xs text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                <svg class="w-3.5 h-3.5 text-slate-500 absolute left-2.5 top-2.5 pointer-events-none" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                            </div>
                        </div>

                        <!-- Exam Type Filter -->
                        <div>
                            <label class="block text-[11px] font-semibold text-slate-400 uppercase tracking-wider mb-1">Exam Type</label>
                            <select name="type" id="index_filter_type" class="w-full px-3 py-2 bg-slate-900 border border-slate-800 rounded-xl text-xs text-slate-200 focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                <option value="">All Types</option>
                                <option value="1" {{ request('type') == '1' ? 'selected' : '' }}>1 - Timed Exam</option>
                                <option value="2" {{ request('type') == '2' ? 'selected' : '' }}>2 - Non-Timed Exam</option>
                                <option value="3" {{ request('type') == '3' ? 'selected' : '' }}>3 - Text Entry Exam</option>
                            </select>
                        </div>

                        <!-- Syllabus -->
                        <div>
                            <label class="block text-[11px] font-semibold text-slate-400 uppercase tracking-wider mb-1">Syllabus</label>
                            <select name="syllabus_id" id="index_filter_syllabus" onchange="onIndexFilterSyllabusChange()" class="w-full px-3 py-2 bg-slate-900 border border-slate-800 rounded-xl text-xs text-slate-200 focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                <option value="">All Syllabuses</option>
                                @foreach($syllabuses as $syl)
                                    <option value="{{ $syl->id }}" {{ request('syllabus_id') == $syl->id ? 'selected' : '' }}>{{ $syl->name }}</option>
                                @endforeach
                            </select>
                        </div>

                        <!-- Subject -->
                        <div>
                            <label class="block text-[11px] font-semibold text-slate-400 uppercase tracking-wider mb-1">Subject</label>
                            <select name="subject_id" id="index_filter_subject" onchange="onIndexFilterSubjectChange()" class="w-full px-3 py-2 bg-slate-900 border border-slate-800 rounded-xl text-xs text-slate-200 focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                <option value="">All Subjects</option>
                                @foreach($subjects as $subj)
                                    <option value="{{ $subj->id }}" {{ request('subject_id') == $subj->id ? 'selected' : '' }}>{{ $subj->name }}</option>
                                @endforeach
                            </select>
                        </div>

                        <!-- Chapter -->
                        <div>
                            <label class="block text-[11px] font-semibold text-slate-400 uppercase tracking-wider mb-1">Chapter</label>
                            <select name="chapter_id" id="index_filter_chapter" onchange="onIndexFilterChapterChange()" class="w-full px-3 py-2 bg-slate-900 border border-slate-800 rounded-xl text-xs text-slate-200 focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                <option value="">All Chapters</option>
                                @foreach($chapters as $ch)
                                    <option value="{{ $ch->id }}" {{ request('chapter_id') == $ch->id ? 'selected' : '' }}>{{ $ch->name }}</option>
                                @endforeach
                            </select>
                        </div>

                        <!-- Topic -->
                        <div>
                            <label class="block text-[11px] font-semibold text-slate-400 uppercase tracking-wider mb-1">Topic</label>
                            <select name="topic_id" id="index_filter_topic" class="w-full px-3 py-2 bg-slate-900 border border-slate-800 rounded-xl text-xs text-slate-200 focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                <option value="">All Topics</option>
                                @foreach($topics as $tp)
                                    <option value="{{ $tp->id }}" {{ request('topic_id') == $tp->id ? 'selected' : '' }}>{{ $tp->name }}</option>
                                @endforeach
                            </select>
                        </div>
                    </div>

                    <div class="flex items-center justify-end space-x-2 pt-1">
                        @if(request()->filled('name') || request()->filled('type') || request()->filled('syllabus_id') || request()->filled('subject_id') || request()->filled('chapter_id') || request()->filled('topic_id'))
                            <a href="{{ route('exams.index') }}" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition-colors inline-flex items-center space-x-1.5">
                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                                <span>Clear Filters</span>
                            </a>
                        @endif
                        <button type="submit" class="px-5 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold shadow-md shadow-indigo-600/30 transition-all inline-flex items-center space-x-1.5 cursor-pointer">
                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                            <span>Search</span>
                        </button>
                    </div>
                </form>
            </div>

            @if($exams->isNotEmpty())
                <div class="divide-y divide-slate-800/80">
                    @foreach ($exams as $exam)
                        @php
                            $examSubmissionsForExam = $examSubmissions->get($exam->id, collect());
                            $completedStudentCount = $examSubmissionsForExam->count();
                            $totalExamMarks = $exam->total_mark > 0 ? $exam->total_mark : $exam->questions->sum('marks');
                            $hasCompletions = ($exam->student_exam_details_count ?? $completedStudentCount) > 0;
                        @endphp
                        <div class="bg-slate-900 hover:bg-slate-800/40 transition-colors">
                            <!-- Header Row: Displays Exam Name, Badges, and Completion Count -->
                            <div onclick="toggleExamManagementDetails({{ $exam->id }})" class="px-6 py-4 flex flex-col sm:flex-row sm:items-center justify-between gap-3 cursor-pointer group select-none">
                                <div class="flex items-center space-x-3.5">
                                    <div class="w-9 h-9 rounded-xl bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 font-bold flex items-center justify-center text-sm group-hover:bg-indigo-500/20 transition-colors shrink-0">
                                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                                    </div>
                                    <div>
                                        <h4 class="text-base font-bold text-white group-hover:text-indigo-300 transition-colors flex items-center space-x-2">
                                            <span>{{ $exam->name }}</span>
                                        </h4>
                                        <p class="text-xs text-slate-400 mt-0.5">
                                            Teacher: <strong class="text-sky-300">{{ $exam->creator?->name ?? 'System' }}</strong>
                                            <span class="text-slate-500 mx-1">&bull;</span>
                                            Marks: <strong class="text-amber-400 font-mono">{{ $totalExamMarks }}</strong>
                                            <span class="text-slate-500 mx-1">&bull;</span>
                                            Questions: <strong class="text-slate-200">{{ $exam->questions->count() }}</strong>
                                            @if($exam->syllabus || $exam->standard || $exam->subject)
                                                <span class="text-slate-500 mx-1">&bull;</span>
                                                <span class="text-indigo-300 font-medium">{{ $exam->syllabus?->name }}</span>
                                                @if($exam->standard)<span class="text-slate-500 mx-1">&bull;</span><span class="text-sky-300 font-medium">{{ $exam->standard?->name }}</span>@endif
                                                @if($exam->subject)<span class="text-slate-500 mx-1">&bull;</span><span class="text-emerald-300 font-medium">{{ $exam->subject?->name }}</span>@endif
                                                @if($exam->chapter)<span class="text-slate-500 mx-1">&bull;</span><span class="text-cyan-300 font-medium">{{ $exam->chapter?->name }}</span>@endif
                                                @if($exam->topic)<span class="text-slate-500 mx-1">&bull;</span><span class="text-purple-300 font-medium">{{ $exam->topic?->name }}</span>@endif
                                            @endif
                                        </p>
                                    </div>
                                </div>

                                <div class="flex items-center space-x-2 sm:space-x-3 shrink-0 flex-wrap gap-y-2">
                                    <button type="button" onclick="event.stopPropagation(); openExamLeaderboardModal({{ $exam->id }}, '{{ addslashes($exam->name) }}')" class="px-3 py-1.5 rounded-xl bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 border border-amber-500/40 text-xs font-bold transition-all inline-flex items-center space-x-1.5 cursor-pointer shadow-sm active:scale-95" title="View Student Rankings & Leaderboard for {{ $exam->name }}">
                                        <span>🏆</span>
                                        <span>Leaderboard</span>
                                    </button>

                                    @if($completedStudentCount > 0)
                                        <span class="inline-flex items-center px-2.5 py-1 rounded-full text-xs font-extrabold bg-emerald-500/20 text-emerald-400 border border-emerald-500/40">
                                            <svg class="w-3.5 h-3.5 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>
                                            {{ $completedStudentCount }} Completed
                                        </span>
                                    @else
                                        <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold bg-slate-800 text-slate-400 border border-slate-700">
                                            0 Completed
                                        </span>
                                    @endif

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
                                        @elseif($exam->type == 2)
                                            <span class="inline-flex items-center px-2 py-0.5 rounded-full text-xs font-semibold bg-slate-800 text-slate-300 border border-slate-700 mt-1">
                                                Non-Timed (2)
                                            </span>
                                        @elseif($exam->type == 3)
                                            <span class="inline-flex items-center px-2 py-0.5 rounded-full text-xs font-semibold bg-amber-500/15 text-amber-300 border border-amber-500/30 mt-1">
                                                Text Entry (3)
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
                                            {{ $totalExamMarks }} Marks
                                        </span>
                                    </div>
                                </div>

                                <!-- Curriculum Classification Row -->
                                <div class="p-3 bg-slate-900/60 rounded-xl border border-slate-800 flex items-center flex-wrap gap-2 text-xs">
                                    <span class="text-[10px] font-bold text-slate-400 uppercase tracking-wider mr-1">Curriculum:</span>
                                    <span class="px-2 py-0.5 rounded bg-indigo-500/10 text-indigo-300 border border-indigo-500/20 font-medium">Syllabus: {{ $exam->syllabus?->name ?? 'Unset' }}</span>
                                    <span class="px-2 py-0.5 rounded bg-sky-500/10 text-sky-300 border border-sky-500/20 font-medium">Class: {{ $exam->standard?->name ?? 'Unset' }}</span>
                                    <span class="px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-300 border border-emerald-500/20 font-medium">Subject: {{ $exam->subject?->name ?? 'Unset' }}</span>
                                    <span class="px-2 py-0.5 rounded bg-cyan-500/10 text-cyan-300 border border-cyan-500/20 font-medium">Chapter: {{ $exam->chapter?->name ?? 'Unset' }}</span>
                                    <span class="px-2 py-0.5 rounded bg-purple-500/10 text-purple-300 border border-purple-500/20 font-medium">Topic: {{ $exam->topic?->name ?? 'Unset' }}</span>
                                </div>

                                <!-- Completed Students Performance Section -->
                                <div class="space-y-3 pt-2">
                                    <div class="flex items-center justify-between pb-2 border-b border-slate-800/60">
                                        <h5 class="text-xs font-bold uppercase tracking-wider text-slate-300 flex items-center space-x-2">
                                            <span>Students Completed This Exam ({{ $completedStudentCount }})</span>
                                        </h5>
                                        <div class="flex items-center space-x-3">
                                            {{-- <button type="button" onclick="event.stopPropagation(); openExamLeaderboardModal({{ $exam->id }}, '{{ addslashes($exam->name) }}')" class="px-3.5 py-1.5 rounded-xl bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 border border-amber-500/40 text-xs font-bold transition-all inline-flex items-center space-x-1.5 cursor-pointer shadow-sm active:scale-95">
                                                <span>🏆</span>
                                                <span>View Full Leaderboard</span>
                                            </button> --}}
                                            <span class="text-[11px] text-slate-400 hidden sm:inline">Click student entry to view question-level marks</span>
                                        </div>
                                    </div>

                                    @if($completedStudentCount > 0)
                                        <div class="overflow-x-auto rounded-xl border border-slate-800">
                                            <table class="w-full text-left text-xs text-slate-300">
                                                <thead class="bg-slate-900 text-slate-400 uppercase font-semibold text-[10px] tracking-wider border-b border-slate-800">
                                                    <tr>
                                                        <th scope="col" class="px-4 py-3">Student Name</th>
                                                        <th scope="col" class="px-4 py-3">Class / Standard</th>
                                                        <th scope="col" class="px-4 py-3">Score Obtained</th>
                                                        <th scope="col" class="px-4 py-3 text-right">Question Marks</th>
                                                    </tr>
                                                </thead>
                                                <tbody class="divide-y divide-slate-800/60 bg-slate-950">
                                                    @foreach($examSubmissionsForExam as $studentId => $studentDetails)
                                                        @php
                                                            $studentObj = $studentDetails->first()->student;
                                                            $studentName = $studentObj?->name ?? $studentObj?->user?->name ?? 'Student #' . $studentId;
                                                            $studentClass = $studentObj?->standard?->name ?? 'N/A';
                                                            $currentUser = auth()->user();
                                                            $isTextEntryExam = (int) $exam->type === 3;
                                                            $canEvaluate = $currentUser && ($currentUser->isAdmin() || (int) $exam->created_by === (int) $currentUser->id);

                                                            $obtainedMarks = 0;
                                                            $detailsPayload = $studentDetails->map(function($d) use (&$obtainedMarks) {
                                                                $qMarks = $d->getQuestionMarks();
                                                                $earnedMarks = $d->getEarnedMarks();
                                                                $isCorrect = $d->isCorrect();
                                                                $isPartial = $d->isPartiallyCorrect();
                                                                $obtainedMarks += $earnedMarks;

                                                                return [
                                                                    'id' => $d->id,
                                                                    'question_name' => $d->question?->name ?? 'N/A',
                                                                    'question_marks' => $qMarks,
                                                                    'selected_answer' => $d->getSelectedAnswerDisplay(),
                                                                    'is_correct' => $isCorrect,
                                                                    'is_partially_correct' => $isPartial,
                                                                    'is_text_entry' => (int) ($d->question?->type ?? 0) === 3,
                                                                    'student_text_answer' => $d->student_text_answer,
                                                                    'teacher_marks' => $d->teacher_marks,
                                                                    'teacher_feedback' => $d->teacher_feedback,
                                                                    'is_evaluated' => $d->isEvaluated(),
                                                                    'earned_marks' => $earnedMarks,
                                                                    'correct_answer' => $d->getCorrectAnswerDisplay(),
                                                                    'match_pairs' => $d->getMatchPairsReview(),
                                                                    'hint' => $d->question?->hint,
                                                                    'solution' => $d->question?->solution,
                                                                ];
                                                            })->values()->toArray();

                                                            $pct = $totalExamMarks > 0 ? (int)round(($obtainedMarks / $totalExamMarks) * 100) : 0;
                                                            $allEvaluated = $isTextEntryExam ? $studentDetails->every(fn($d) => $d->isEvaluated()) : true;
                                                            $anyEvaluated = $isTextEntryExam ? $studentDetails->contains(fn($d) => $d->isEvaluated()) : true;
                                                        @endphp

                                                        <tr class="hover:bg-slate-900/60 transition-colors">
                                                            <td class="px-4 py-3 font-semibold text-white">
                                                                <div class="flex items-center space-x-2">
                                                                    <div class="w-6 h-6 rounded-full bg-indigo-500/20 border border-indigo-500/30 text-indigo-300 font-bold flex items-center justify-center text-[10px]">
                                                                        {{ strtoupper(substr($studentName, 0, 1)) }}
                                                                    </div>
                                                                    <span>{{ $studentName }}</span>
                                                                </div>
                                                            </td>
                                                            <td class="px-4 py-3">
                                                                <span class="px-2 py-0.5 rounded-md bg-slate-800 text-slate-300 border border-slate-700 text-[11px] font-medium">
                                                                    {{ $studentClass }}
                                                                </span>
                                                            </td>
                                                            <td class="px-4 py-3">
                                                                <div class="flex items-center space-x-2 flex-wrap gap-1">
                                                                    <span id="score-display-{{ $exam->id }}-{{ $studentId }}" class="font-mono font-bold text-emerald-400 text-sm">
                                                                        {{ $obtainedMarks }} / {{ $totalExamMarks }}
                                                                    </span>
                                                                    <span id="pct-display-{{ $exam->id }}-{{ $studentId }}" class="px-2 py-0.5 rounded text-[10px] font-extrabold {{ $pct >= 80 ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30' : ($pct >= 50 ? 'bg-amber-500/20 text-amber-300 border border-amber-500/30' : 'bg-rose-500/20 text-rose-300 border border-rose-500/30') }}">
                                                                        {{ $pct }}%
                                                                    </span>
                                                                    @if($isTextEntryExam)
                                                                        <span id="eval-status-badge-{{ $exam->id }}-{{ $studentId }}" class="px-2 py-0.5 rounded text-[10px] font-bold {{ $allEvaluated ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30' : ($anyEvaluated ? 'bg-amber-500/20 text-amber-300 border border-amber-500/30' : 'bg-rose-500/20 text-rose-300 border border-rose-500/30') }}">
                                                                            {{ $allEvaluated ? 'Evaluated' : ($anyEvaluated ? 'Partially Evaluated' : 'Pending Evaluation') }}
                                                                        </span>
                                                                    @endif
                                                                </div>
                                                            </td>
                                                            <td class="px-4 py-3 text-right">
                                                                <script type="application/json" id="submission-data-{{ $exam->id }}-{{ $studentId }}">
                                                                    {!! json_encode([
                                                                        'id' => $exam->id,
                                                                        'name' => $exam->name,
                                                                        'student_id' => $studentId,
                                                                        'student_name' => $studentName,
                                                                        'is_text_entry_exam' => $isTextEntryExam,
                                                                        'can_evaluate' => $canEvaluate,
                                                                        'evaluate_url' => route('exams.evaluate-submission', [$exam->id, $studentId]),
                                                                        'total_mark' => $totalExamMarks,
                                                                        'obtained_mark' => $obtainedMarks,
                                                                        'details' => $detailsPayload,
                                                                    ], JSON_HEX_TAG | JSON_HEX_APOS | JSON_HEX_QUOT | JSON_HEX_AMP) !!}
                                                                </script>
                                                                <button type="button" onclick="event.stopPropagation(); openStudentViewSubmissionModal('{{ $exam->id }}-{{ $studentId }}')" class="px-3 py-1.5 rounded-lg {{ $isTextEntryExam && $canEvaluate ? 'bg-emerald-600 hover:bg-emerald-500' : 'bg-indigo-600 hover:bg-indigo-500' }} text-white font-bold text-xs shadow-md transition-all inline-flex items-center space-x-1.5 cursor-pointer">
                                                                    @if($isTextEntryExam && $canEvaluate)
                                                                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/></svg>
                                                                        <span>Check Answers &amp; Give Marks</span>
                                                                    @else
                                                                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                                                                        <span>View Question Marks</span>
                                                                    @endif
                                                                </button>
                                                            </td>
                                                        </tr>
                                                    @endforeach
                                                </tbody>
                                            </table>
                                        </div>
                                    @else
                                        <div class="p-6 text-center bg-slate-900/60 rounded-xl border border-slate-800 text-slate-400 text-xs">
                                            No students have completed this exam yet.
                                        </div>
                                    @endif
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
                                        <script type="application/json" id="exam-view-data-{{ $exam->id }}">
                                            {!! json_encode([
                                                'id' => $exam->id,
                                                'name' => $exam->name,
                                                'type' => $exam->type == 1 ? ('1 - Timed' . ($exam->duration ? ' (' . $exam->duration . ' mins)' : '')) : ($exam->type == 2 ? '2 - Non-Timed' : '3 - Text Entry'),
                                                'status' => $exam->status == 1 ? '1 - Active' : '2 - Inactive',
                                                'status_id' => $exam->status,
                                                'duration' => $exam->duration,
                                                'creator' => $exam->creator?->name ?? 'System',
                                                'total_mark' => $exam->total_mark,
                                                'show_url' => route('exams.show', $exam),
                                                'has_completions' => $hasCompletions,
                                                'syllabus_id' => $exam->syllabus_id,
                                                'syllabus_name' => $exam->syllabus?->name ?? 'N/A',
                                                'standard_id' => $exam->standard_id,
                                                'standard_name' => $exam->standard?->name ?? 'N/A',
                                                'subject_id' => $exam->subject_id,
                                                'subject_name' => $exam->subject?->name ?? 'N/A',
                                                'chapter_id' => $exam->chapter_id,
                                                'chapter_name' => $exam->chapter?->name ?? 'N/A',
                                                'topic_id' => $exam->topic_id,
                                                'topic_name' => $exam->topic?->name ?? 'N/A',
                                                'standards' => $exam->standards->pluck('name')->toArray(),
                                                'questions' => $exam->questions->map(function($q) {
                                                    return [
                                                        'id' => $q->id,
                                                        'name' => $q->name,
                                                        'description' => $q->description ?? '',
                                                        'marks' => $q->marks,
                                                        'standard' => $q->standard?->name ?? 'N/A',
                                                        'type_id' => $q->type,
                                                        'type' => $q->type == 1 ? 'Single Option' : ($q->type == 2 ? 'Multiple Option' : ($q->type == 4 ? 'True / False' : ($q->type == 5 ? 'Match the Following' : 'Text Entry'))),
                                                        'creator' => $q->creator?->name ?? 'System',
                                                        'answers' => $q->answers->map(fn($a) => ['id' => $a->id, 'name' => $a->name, 'match_answer' => $a->match_answer, 'is_correct' => $a->is_correct])->toArray(),
                                                        'hint' => $q->hint,
                                                        'solution' => $q->solution,
                                                    ];
                                                })->toArray(),
                                            ], JSON_HEX_TAG | JSON_HEX_APOS | JSON_HEX_QUOT | JSON_HEX_AMP) !!}
                                        </script>

                                        <script type="application/json" id="exam-edit-data-{{ $exam->id }}">
                                            {!! json_encode([
                                                'id' => $exam->id,
                                                'name' => $exam->name,
                                                'type' => $exam->type,
                                                'duration' => $exam->duration,
                                                'status' => $exam->status,
                                                'syllabus_id' => $exam->syllabus_id,
                                                'standard_id' => $exam->standard_id,
                                                'subject_id' => $exam->subject_id,
                                                'chapter_id' => $exam->chapter_id,
                                                'topic_id' => $exam->topic_id,
                                                'standard_ids' => $exam->standards->pluck('id')->toArray(),
                                                'question_ids' => $exam->questions->pluck('id')->toArray(),
                                            ], JSON_HEX_TAG | JSON_HEX_APOS | JSON_HEX_QUOT | JSON_HEX_AMP) !!}
                                        </script>

                                        <button type="button" onclick="event.stopPropagation(); openViewExamModal({{ $exam->id }})" class="px-3.5 py-1.5 rounded-lg bg-emerald-950/80 hover:bg-emerald-900/80 text-emerald-300 text-xs font-medium border border-emerald-800/40 transition-colors inline-flex items-center space-x-1 cursor-pointer">
                                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                                            <span>View</span>
                                        </button>


                                        @if(!$hasCompletions)
                                            <button type="button" onclick="event.stopPropagation(); openEditExamModal({{ $exam->id }})" class="px-3.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-medium border border-slate-700 transition-colors inline-flex items-center space-x-1 cursor-pointer">
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
                    <svg class="w-10 h-10 mx-auto mb-3 text-slate-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                    @if(request()->filled('name') || request()->filled('type') || request()->filled('syllabus_id') || request()->filled('subject_id') || request()->filled('chapter_id') || request()->filled('topic_id'))
                        <p class="text-slate-300 font-medium">No exams match your search criteria.</p>
                        <p class="text-xs text-slate-500 mt-1">Try clearing or adjusting your filters to find exams.</p>
                        <a href="{{ route('exams.index') }}" class="inline-block mt-3 px-4 py-1.5 rounded-lg bg-indigo-600/20 text-indigo-300 border border-indigo-500/30 text-xs font-semibold hover:bg-indigo-600/30 transition-colors">Clear All Filters</a>
                    @else
                        No exams created yet. Click "Create New Exam" to get started.
                    @endif
                </div>
            @endif

            @if($exams && method_exists($exams, 'total'))
                <div class="px-6 py-4 border-t border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs text-slate-400">
                    <div>
                        Showing <span class="font-semibold text-slate-200">{{ $exams->firstItem() ?? 0 }}</span>
                        to <span class="font-semibold text-slate-200">{{ $exams->lastItem() ?? 0 }}</span>
                        of <span class="font-semibold text-slate-200">{{ $exams->total() }}</span> exam(s)
                        (10 per page)
                    </div>
                    @if($exams->hasPages())
                        <div>
                            {{ $exams->links() }}
                        </div>
                    @endif
                </div>
            @endif
        </div>

        <!-- CREATE EXAM MODAL -->
        @php
            $isCreateModalOpen = $errors->any() && old('_method') !== 'PUT';
        @endphp
        <div id="createExamModal" class="{{ $isCreateModalOpen ? '' : 'hidden' }} fixed inset-0 z-50 bg-black/70 backdrop-blur-sm overflow-y-auto p-2 sm:p-4 flex justify-center items-start" style="z-index: 9999;">
            <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-5xl max-h-[92vh] flex flex-col overflow-hidden shadow-2xl my-2 sm:my-4">
                <div class="px-5 py-3 border-b border-slate-800 flex items-center justify-between bg-slate-950/80 shrink-0">
                    <h3 class="text-base font-bold text-white flex items-center gap-2">
                        <svg class="w-5 h-5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                        <span>Create New Exam</span>
                    </h3>
                    <button onclick="document.getElementById('createExamModal').classList.add('hidden')" class="text-slate-400 hover:text-white transition-colors cursor-pointer p-1">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                    </button>
                </div>

                <form method="POST" action="{{ route('exams.store') }}" class="flex flex-col flex-1 overflow-hidden min-h-0">
                    @csrf

                    <div class="p-4 sm:p-5 overflow-y-auto space-y-3 flex-1">
                        @if ($isCreateModalOpen && $errors->any())
                            <div class="p-3 rounded-xl bg-red-950/80 border border-red-500/40 text-red-200 text-xs">
                                <span class="font-bold flex items-center gap-1 text-red-300">
                                    <svg class="w-4 h-4 inline" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                                    Validation errors occurred. Please check the fields below.
                                </span>
                            </div>
                        @endif

                        <!-- Compact Primary Row: Exam Name, Type, Duration, Status -->
                        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-12 gap-2.5 items-start">
                            <!-- Exam Name -->
                            <div class="md:col-span-5">
                                <label for="create_exam_name" class="block text-[11px] font-semibold text-slate-300 uppercase tracking-wider mb-1">Exam Name <span class="text-red-400">*</span></label>
                                <input type="text" id="create_exam_name" name="name" required value="{{ old('name') }}" placeholder="e.g. Mid-Term Science Assessment" class="w-full px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-xs @error('name') border-red-500 focus:ring-red-500 @enderror">
                                @error('name')
                                    <p class="mt-1 text-[11px] text-red-400">{{ $message }}</p>
                                @enderror
                            </div>

                            <!-- Exam Type -->
                            <div class="md:col-span-2">
                                <label for="create_exam_type" class="block text-[11px] font-semibold text-slate-300 uppercase tracking-wider mb-1">Type <span class="text-red-400">*</span></label>
                                <select id="create_exam_type" name="type" required onchange="toggleCreateExamDuration(this.value)" class="w-full px-2.5 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-xs">
                                    <option value="1" {{ old('type', '1') == '1' ? 'selected' : '' }}>1 - Timed</option>
                                    <option value="2" {{ old('type') == '2' ? 'selected' : '' }}>2 - Non-Timed</option>
                                    <option value="3" {{ old('type') == '3' ? 'selected' : '' }}>3 - Text Entry</option>
                                </select>
                                @error('type')
                                    <p class="mt-1 text-[11px] text-red-400">{{ $message }}</p>
                                @enderror
                            </div>

                            <!-- Duration (Minutes) -->
                            <div id="create_duration_wrapper" class="md:col-span-2 {{ old('type', '1') == '2' ? 'hidden' : '' }}">
                                <label for="create_exam_duration" class="block text-[11px] font-semibold text-slate-300 uppercase tracking-wider mb-1">Duration (Min) <span class="text-red-400">*</span></label>
                                <input type="number" id="create_exam_duration" name="duration" min="1" max="1440" value="{{ old('duration', 60) }}" placeholder="60" class="w-full px-2.5 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-xs @error('duration') border-red-500 focus:ring-red-500 @enderror">
                                @error('duration')
                                    <p class="mt-1 text-[11px] text-red-400">{{ $message }}</p>
                                @enderror
                            </div>

                            <!-- Status -->
                            <div class="md:col-span-3">
                                <label for="create_exam_status" class="block text-[11px] font-semibold text-slate-300 uppercase tracking-wider mb-1">Status <span class="text-red-400">*</span></label>
                                <select id="create_exam_status" name="status" required class="w-full px-2.5 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-xs">
                                    <option value="1" {{ old('status', '1') == '1' ? 'selected' : '' }}>1 - Active</option>
                                    <option value="2" {{ old('status') == '2' ? 'selected' : '' }}>2 - Inactive</option>
                                </select>
                                @error('status')
                                    <p class="mt-1 text-[11px] text-red-400">{{ $message }}</p>
                                @enderror
                            </div>
                        </div>

                        <!-- Row 2: Curriculum Classification -->
                        <div class="p-3 rounded-xl bg-slate-950/70 border border-slate-800 space-y-2">
                            <div class="flex items-center justify-between">
                                <label class="block text-[11px] font-bold text-indigo-300 uppercase tracking-wider flex items-center gap-1.5">
                                    <svg class="w-3.5 h-3.5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
                                    <span>Curriculum Classification</span>
                                </label>
                                <span class="text-[10px] text-slate-400">Classify exam by academic curriculum</span>
                            </div>

                            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-5 gap-2">
                                <!-- 1. Syllabus -->
                                <div>
                                    <label for="create_exam_syllabus" class="block text-[10px] font-semibold text-slate-300 uppercase tracking-wider mb-0.5">Syllabus</label>
                                    <select id="create_exam_syllabus" name="syllabus_id" onchange="onExamSyllabusChange('create')" class="w-full px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-100 text-xs focus:ring-2 focus:ring-indigo-500 focus:outline-none">
                                        <option value="">Select Syllabus</option>
                                        @foreach($syllabuses as $syl)
                                            <option value="{{ $syl->id }}" {{ old('syllabus_id') == $syl->id ? 'selected' : '' }}>{{ $syl->name }}</option>
                                        @endforeach
                                    </select>
                                </div>

                                <!-- 2. Class / Standard -->
                                <div>
                                    <label for="create_exam_standard" class="block text-[10px] font-semibold text-slate-300 uppercase tracking-wider mb-0.5">Class / Standard</label>
                                    <select id="create_exam_standard" name="standard_id" onchange="onExamStandardChange('create')" class="w-full px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-100 text-xs focus:ring-2 focus:ring-indigo-500 focus:outline-none">
                                        <option value="">Select Class</option>
                                        @foreach($standards as $std)
                                            <option value="{{ $std->id }}" data-syllabus-id="{{ $std->syllabus_id }}" {{ old('standard_id') == $std->id ? 'selected' : '' }}>{{ $std->name }}</option>
                                        @endforeach
                                    </select>
                                </div>

                                <!-- 3. Subject -->
                                <div>
                                    <label for="create_exam_subject" class="block text-[10px] font-semibold text-slate-300 uppercase tracking-wider mb-0.5">Subject</label>
                                    <select id="create_exam_subject" name="subject_id" onchange="onExamSubjectChange('create')" class="w-full px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-100 text-xs focus:ring-2 focus:ring-indigo-500 focus:outline-none">
                                        <option value="">Select Subject</option>
                                        @foreach($subjectsData as $sb)
                                            <option value="{{ $sb->id }}" data-syllabus-id="{{ $sb->syllabus_id }}" {{ old('subject_id') == $sb->id ? 'selected' : '' }}>{{ $sb->name }}</option>
                                        @endforeach
                                    </select>
                                </div>

                                <!-- 4. Chapter -->
                                <div>
                                    <label for="create_exam_chapter" class="block text-[10px] font-semibold text-slate-300 uppercase tracking-wider mb-0.5">Chapter</label>
                                    <select id="create_exam_chapter" name="chapter_id" onchange="onExamChapterChange('create')" class="w-full px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-100 text-xs focus:ring-2 focus:ring-indigo-500 focus:outline-none">
                                        <option value="">Select Chapter</option>
                                    </select>
                                </div>

                                <!-- 5. Topic -->
                                <div>
                                    <label for="create_exam_topic" class="block text-[10px] font-semibold text-slate-300 uppercase tracking-wider mb-0.5">Topic</label>
                                    <select id="create_exam_topic" name="topic_id" onchange="onExamTopicChange('create')" class="w-full px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-100 text-xs focus:ring-2 focus:ring-indigo-500 focus:outline-none">
                                        <option value="">Select Topic</option>
                                    </select>
                                </div>
                            </div>
                        </div>

                        <!-- Assign Standards (Teachers only) -->
                        <div>
                            <label class="block text-[11px] font-semibold text-slate-300 uppercase tracking-wider mb-1">Assign to Standards / Classes</label>
                            <div class="grid grid-cols-2 sm:grid-cols-4 gap-1.5 bg-slate-950 p-2.5 rounded-lg border border-slate-800 max-h-24 overflow-y-auto">
                                @foreach($standards as $std)
                                    <label class="flex items-center space-x-1.5 text-xs text-slate-300 cursor-pointer hover:text-white">
                                        <input type="checkbox" name="standard_ids[]" value="{{ $std->id }}" {{ in_array($std->id, old('standard_ids', [])) ? 'checked' : '' }} class="rounded bg-slate-900 border-slate-700 text-indigo-600 focus:ring-indigo-500 text-xs">
                                        <span class="truncate">{{ $std->name }}</span>
                                    </label>
                                @endforeach
                            </div>
                            @error('standard_ids')
                                <p class="mt-1 text-[11px] text-red-400">{{ $message }}</p>
                            @enderror
                        </div>

                    <!-- Select Questions from Question Bank -->
                    <div>
                        <div class="flex items-center justify-between mb-1.5">
                            <label class="block text-xs font-semibold text-slate-300 uppercase tracking-wider">Add Questions from Question Bank (Optional)</label>
                            <span class="text-[11px] text-slate-400">Check questions to link to this exam</span>
                        </div>

                        <!-- Search & Filter Controls for Create Modal -->
                        <div class="p-2.5 mb-2 rounded-lg bg-slate-950 border border-slate-800 space-y-1.5">
                            <div class="grid grid-cols-2 gap-2">
                                <input type="text" id="create_search_q_name" oninput="filterModalQuestions('create')" placeholder="Search question name..." class="px-2.5 py-1 rounded bg-slate-900 border border-slate-700 text-slate-200 placeholder-slate-500 text-xs focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                <input type="text" id="create_search_q_creator" oninput="filterModalQuestions('create')" placeholder="Search created by..." class="px-2.5 py-1 rounded bg-slate-900 border border-slate-700 text-slate-200 placeholder-slate-500 text-xs focus:outline-none focus:ring-1 focus:ring-indigo-500">
                            </div>
                            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
                                <select id="create_search_q_standard" onchange="filterModalQuestions('create')" class="px-2 py-1 rounded bg-slate-900 border border-slate-700 text-slate-200 text-xs focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                    <option value="">All Classes / Standards</option>
                                    @foreach($standards as $std)
                                        <option value="{{ $std->id }}">{{ $std->name }}</option>
                                    @endforeach
                                </select>
                                <select id="create_search_q_subject" onchange="onModalSubjectChange('create')" class="px-2 py-1 rounded bg-slate-900 border border-slate-700 text-slate-200 text-xs focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                    <option value="">All Subjects</option>
                                    @foreach($subjectsData as $subj)
                                        <option value="{{ $subj->id }}">{{ $subj->name }}</option>
                                    @endforeach
                                </select>
                                <select id="create_search_q_chapter" onchange="onModalChapterChange('create')" class="px-2 py-1 rounded bg-slate-900 border border-slate-700 text-slate-200 text-xs focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                    <option value="">All Chapters</option>
                                </select>
                                <select id="create_search_q_topic" onchange="filterModalQuestions('create')" class="px-2 py-1 rounded bg-slate-900 border border-slate-700 text-slate-200 text-xs focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                    <option value="">All Topics</option>
                                </select>
                            </div>
                            <div class="grid grid-cols-1 gap-2">
                                <select id="create_search_q_type" onchange="filterModalQuestions('create')" class="px-2 py-1 rounded bg-slate-900 border border-slate-700 text-slate-200 text-xs focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                    <option value="">All Question Types</option>
                                    <option value="1">1 - Single Option</option>
                                    <option value="2">2 - Multiple Option</option>
                                    <option value="3">3 - Text Entry</option>
                                    <option value="4">4 - True / False</option>
                                    <option value="5">5 - Match the Following</option>
                                </select>
                            </div>
                            <!-- Pagination Bar for Create Modal -->
                            <div class="flex items-center justify-between pt-0.5 text-[11px] text-slate-400">
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

                        <div class="bg-slate-950 p-2.5 rounded-lg border border-slate-800 max-h-40 overflow-y-auto space-y-1.5">
                            @forelse($availableQuestions as $q)
                                <div class="create-q-item flex items-start space-x-3 p-2 rounded-lg bg-slate-900/60 hover:bg-slate-900 transition-colors border border-slate-800/60"
                                     data-name="{{ strtolower(strip_tags($q->name)) }}"
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
                                            <label for="create_q_add_{{ $q->id }}" class="font-medium text-slate-200 hover:text-white cursor-pointer flex-1 prose prose-invert prose-sm max-w-none">{!! $q->name !!}</label>
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
                                                    'answers' => $q->answers->map(fn($a) => ['id' => $a->id, 'name' => $a->name, 'match_answer' => $a->match_answer, 'is_correct' => $a->is_correct])->toArray(),
                                                ]) }})" class="px-2 py-0.5 rounded bg-indigo-500/10 hover:bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 text-[10px] font-medium transition-all inline-flex items-center space-x-1 cursor-pointer">
                                                    <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                                                    <span>View</span>
                                                </button>
                                                <span class="text-amber-400 font-semibold">{{ $q->marks }} mark(s)</span>
                                            </div>
                                        </div>
                                        <label for="create_q_add_{{ $q->id }}" class="flex items-center flex-wrap gap-2 mt-0.5 text-[10px] text-slate-400 cursor-pointer block">
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
                                            <span>Type: @if($q->type == 1) Single Option @elseif($q->type == 2) Multiple Option @elseif($q->type == 4) True / False @elseif($q->type == 5) Match the Following @else Text Entry @endif</span>
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
                </div>

                    <div class="px-5 py-3 border-t border-slate-800 flex justify-end space-x-3 bg-slate-950/80 shrink-0">
                        <button type="button" onclick="document.getElementById('createExamModal').classList.add('hidden')" class="px-4 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-medium transition-colors cursor-pointer">Cancel</button>
                        <button type="submit" class="px-5 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold shadow-lg shadow-indigo-600/30 transition-all cursor-pointer">Save Exam</button>
                    </div>
                </form>
            </div>
        </div>

        <!-- EDIT EXAM MODAL -->
        @php
            $isEditModalOpen = $errors->any() && old('_method') === 'PUT';
        @endphp
        <div id="editExamModal" class="{{ $isEditModalOpen ? '' : 'hidden' }} fixed inset-0 z-50 bg-black/70 backdrop-blur-sm overflow-y-auto p-2 sm:p-4 flex justify-center items-start" style="z-index: 9999;">
            <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-5xl max-h-[92vh] flex flex-col overflow-hidden shadow-2xl my-2 sm:my-4">
                <div class="px-5 py-3 border-b border-slate-800 flex items-center justify-between bg-slate-950/80 shrink-0">
                    <h3 class="text-base font-bold text-white flex items-center gap-2">
                        <svg class="w-5 h-5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/></svg>
                        <span>Edit Exam</span>
                    </h3>
                    <button onclick="document.getElementById('editExamModal').classList.add('hidden')" class="text-slate-400 hover:text-white transition-colors cursor-pointer p-1">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                    </button>
                </div>

                <form id="editExamForm" method="POST" action="{{ old('_method') === 'PUT' ? old('_edit_action_url', '') : '' }}" class="flex flex-col flex-1 overflow-hidden min-h-0">
                    @csrf
                    @method('PUT')
                    <input type="hidden" id="edit_action_url" name="_edit_action_url" value="{{ old('_method') === 'PUT' ? old('_edit_action_url', '') : '' }}">

                    <div class="p-4 sm:p-5 overflow-y-auto space-y-3 flex-1">
                        @if ($isEditModalOpen && $errors->any())
                            <div class="p-3 rounded-xl bg-red-950/80 border border-red-500/40 text-red-200 text-xs">
                                <span class="font-bold flex items-center gap-1 text-red-300">
                                    <svg class="w-4 h-4 inline" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                                    Validation errors occurred. Please check the fields below.
                                </span>
                            </div>
                        @endif

                        <!-- Compact Primary Row: Exam Name, Type, Duration, Status -->
                        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-12 gap-2.5 items-start">
                            <!-- Exam Name (Required) -->
                            <div class="md:col-span-5">
                                <label for="edit_exam_name" class="block text-[11px] font-semibold text-slate-300 uppercase tracking-wider mb-1">Exam Name <span class="text-red-400">*</span></label>
                                <input type="text" id="edit_exam_name" name="name" required value="{{ old('_method') === 'PUT' ? old('name') : '' }}" class="w-full px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-xs @error('name') border-red-500 focus:ring-red-500 @enderror">
                                @error('name')
                                    <p class="mt-1 text-[11px] text-red-400">{{ $message }}</p>
                                @enderror
                            </div>

                            <!-- Exam Type -->
                            <div class="md:col-span-2">
                                <label for="edit_exam_type" class="block text-[11px] font-semibold text-slate-300 uppercase tracking-wider mb-1">Type <span class="text-red-400">*</span></label>
                                <select id="edit_exam_type" name="type" required onchange="toggleEditExamDuration(this.value)" class="w-full px-2.5 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-xs">
                                    <option value="1">1 - Timed</option>
                                    <option value="2">2 - Non-Timed</option>
                                    <option value="3">3 - Text Entry</option>
                                </select>
                                @error('type')
                                    <p class="mt-1 text-[11px] text-red-400">{{ $message }}</p>
                                @enderror
                            </div>

                            <!-- Duration (Minutes) -->
                            <div id="edit_duration_wrapper" class="md:col-span-2">
                                <label for="edit_exam_duration" class="block text-[11px] font-semibold text-slate-300 uppercase tracking-wider mb-1">Duration (Min) <span class="text-red-400">*</span></label>
                                <input type="number" id="edit_exam_duration" name="duration" min="1" max="1440" value="{{ old('_method') === 'PUT' ? old('duration') : '' }}" placeholder="60" class="w-full px-2.5 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-xs @error('duration') border-red-500 focus:ring-red-500 @enderror">
                                @error('duration')
                                    <p class="mt-1 text-[11px] text-red-400">{{ $message }}</p>
                                @enderror
                            </div>

                            <!-- Status -->
                            <div class="md:col-span-3">
                                <label for="edit_exam_status" class="block text-[11px] font-semibold text-slate-300 uppercase tracking-wider mb-1">Status <span class="text-red-400">*</span></label>
                                <select id="edit_exam_status" name="status" required class="w-full px-2.5 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-xs">
                                    <option value="1">1 - Active</option>
                                    <option value="2">2 - Inactive</option>
                                </select>
                                @error('status')
                                    <p class="mt-1 text-[11px] text-red-400">{{ $message }}</p>
                                @enderror
                            </div>
                        </div>

                        <!-- Row 2: Curriculum Hierarchy: Syllabus, Class (Standard), Subject, Chapter, Topic -->
                        <div class="p-3 rounded-xl bg-slate-950/70 border border-slate-800 space-y-2">
                            <div class="flex items-center justify-between">
                                <label class="block text-[11px] font-bold text-indigo-300 uppercase tracking-wider flex items-center gap-1.5">
                                    <svg class="w-3.5 h-3.5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
                                    <span>Curriculum Classification</span>
                                </label>
                                <span class="text-[10px] text-slate-400">Classify exam by academic curriculum</span>
                            </div>

                            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-5 gap-2">
                                <!-- 1. Syllabus -->
                                <div>
                                    <label for="edit_exam_syllabus" class="block text-[10px] font-semibold text-slate-300 uppercase tracking-wider mb-0.5">Syllabus</label>
                                    <select id="edit_exam_syllabus" name="syllabus_id" onchange="onExamSyllabusChange('edit')" class="w-full px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-100 text-xs focus:ring-2 focus:ring-indigo-500 focus:outline-none">
                                        <option value="">Select Syllabus</option>
                                        @foreach($syllabuses as $syl)
                                            <option value="{{ $syl->id }}">{{ $syl->name }}</option>
                                        @endforeach
                                    </select>
                                </div>

                                <!-- 2. Class / Standard -->
                                <div>
                                    <label for="edit_exam_standard" class="block text-[10px] font-semibold text-slate-300 uppercase tracking-wider mb-0.5">Class / Standard</label>
                                    <select id="edit_exam_standard" name="standard_id" onchange="onExamStandardChange('edit')" class="w-full px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-100 text-xs focus:ring-2 focus:ring-indigo-500 focus:outline-none">
                                        <option value="">Select Class</option>
                                        @foreach($standards as $std)
                                            <option value="{{ $std->id }}" data-syllabus-id="{{ $std->syllabus_id }}">{{ $std->name }}</option>
                                        @endforeach
                                    </select>
                                </div>

                                <!-- 3. Subject -->
                                <div>
                                    <label for="edit_exam_subject" class="block text-[10px] font-semibold text-slate-300 uppercase tracking-wider mb-0.5">Subject</label>
                                    <select id="edit_exam_subject" name="subject_id" onchange="onExamSubjectChange('edit')" class="w-full px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-100 text-xs focus:ring-2 focus:ring-indigo-500 focus:outline-none">
                                        <option value="">Select Subject</option>
                                        @foreach($subjectsData as $sb)
                                            <option value="{{ $sb->id }}" data-syllabus-id="{{ $sb->syllabus_id }}">{{ $sb->name }}</option>
                                        @endforeach
                                    </select>
                                </div>

                                <!-- 4. Chapter -->
                                <div>
                                    <label for="edit_exam_chapter" class="block text-[10px] font-semibold text-slate-300 uppercase tracking-wider mb-0.5">Chapter</label>
                                    <select id="edit_exam_chapter" name="chapter_id" onchange="onExamChapterChange('edit')" class="w-full px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-100 text-xs focus:ring-2 focus:ring-indigo-500 focus:outline-none">
                                        <option value="">Select Chapter</option>
                                    </select>
                                </div>

                                <!-- 5. Topic -->
                                <div>
                                    <label for="edit_exam_topic" class="block text-[10px] font-semibold text-slate-300 uppercase tracking-wider mb-0.5">Topic</label>
                                    <select id="edit_exam_topic" name="topic_id" onchange="onExamTopicChange('edit')" class="w-full px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-100 text-xs focus:ring-2 focus:ring-indigo-500 focus:outline-none">
                                        <option value="">Select Topic</option>
                                    </select>
                                </div>
                            </div>
                        </div>

                        <!-- Assign Standards (Teachers only) -->
                        <div>
                            <label class="block text-[11px] font-semibold text-slate-300 uppercase tracking-wider mb-1">Assign to Standards / Classes</label>
                            <div class="grid grid-cols-2 sm:grid-cols-4 gap-1.5 bg-slate-950 p-2.5 rounded-lg border border-slate-800 max-h-24 overflow-y-auto">
                                @foreach($standards as $std)
                                    <label class="flex items-center space-x-1.5 text-xs text-slate-300 cursor-pointer hover:text-white">
                                        <input type="checkbox" name="standard_ids[]" value="{{ $std->id }}" class="edit-exam-std-checkbox rounded bg-slate-900 border-slate-700 text-indigo-600 focus:ring-indigo-500 text-xs">
                                        <span class="truncate">{{ $std->name }}</span>
                                    </label>
                                @endforeach
                            </div>
                            @error('standard_ids')
                                <p class="mt-1 text-[11px] text-red-400">{{ $message }}</p>
                            @enderror
                        </div>

                        <!-- Manage Questions from Question Bank -->
                        <div>
                            <div class="flex items-center justify-between mb-1.5">
                                <label class="block text-[11px] font-semibold text-slate-300 uppercase tracking-wider">Exam Questions (Question Bank)</label>
                                <span class="text-[10px] text-slate-400">Check/uncheck to update linked questions</span>
                            </div>

                            <!-- Search & Filter Controls for Edit Modal -->
                            <div class="p-2.5 mb-2 rounded-lg bg-slate-950 border border-slate-800 space-y-1.5">
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
                                        <option value="4">4 - True / False</option>
                                        <option value="5">5 - Match the Following</option>
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

                            <div class="bg-slate-950 p-2.5 rounded-lg border border-slate-800 max-h-40 overflow-y-auto space-y-1.5">
                                @forelse($availableQuestions as $q)
                                    <div class="edit-q-item flex items-start space-x-3 p-2 rounded-lg bg-slate-900/60 hover:bg-slate-900 transition-colors border border-slate-800/60"
                                         data-name="{{ strtolower(strip_tags($q->name)) }}"
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
                                                <label for="edit_q_add_{{ $q->id }}" class="font-medium text-slate-200 hover:text-white cursor-pointer flex-1 prose prose-invert prose-sm max-w-none">{!! $q->name !!}</label>
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
                                                        'answers' => $q->answers->map(fn($a) => ['id' => $a->id, 'name' => $a->name, 'match_answer' => $a->match_answer, 'is_correct' => $a->is_correct])->toArray(),
                                                    ]) }})" class="px-2 py-0.5 rounded bg-indigo-500/10 hover:bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 text-[10px] font-medium transition-all inline-flex items-center space-x-1 cursor-pointer">
                                                        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                                                        <span>View</span>
                                                    </button>
                                                    <span class="text-amber-400 font-semibold">{{ $q->marks }} mark(s)</span>
                                                </div>
                                            </div>
                                            <label for="edit_q_add_{{ $q->id }}" class="flex items-center flex-wrap gap-2 mt-0.5 text-[10px] text-slate-400 cursor-pointer block">
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
                                                <span>Type: @if($q->type == 1) Single Option @elseif($q->type == 2) Multiple Option @elseif($q->type == 4) True / False @elseif($q->type == 5) Match the Following @else Text Entry @endif</span>
                                            </label>
                                        </div>
                                    </div>
                                @empty
                                    <p class="text-xs text-slate-500 text-center py-4">No questions available in Question Bank.</p>
                                @endforelse
                            </div>

                            <!-- Modal Pagination Footer for Edit -->
                            <div class="mt-1.5 flex items-center justify-between text-xs">
                                <div class="flex items-center space-x-1">
                                    <button type="button" id="edit_prev_btn" onclick="prevModalPage('edit')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 disabled:opacity-40 disabled:cursor-not-allowed text-slate-300 text-[11px] font-semibold border border-slate-700 cursor-pointer">&larr; Prev</button>
                                    <div id="edit_page_numbers" class="flex items-center space-x-1"></div>
                                    <button type="button" id="edit_next_btn" onclick="nextModalPage('edit')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 disabled:opacity-40 disabled:cursor-not-allowed text-slate-300 text-[11px] font-semibold border border-slate-700 cursor-pointer">Next &rarr;</button>
                                </div>
                            </div>
                            @error('question_ids')
                                <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                            @enderror
                        </div>
                    </div>

                    <div class="px-5 py-3 border-t border-slate-800 flex justify-end space-x-3 bg-slate-950/80 shrink-0">
                        <button type="button" onclick="document.getElementById('editExamModal').classList.add('hidden')" class="px-4 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-medium transition-colors cursor-pointer">Cancel</button>
                        <button type="submit" class="px-5 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold shadow-lg shadow-indigo-600/30 transition-all cursor-pointer">Update Exam</button>
                    </div>
                </form>
            </div>
        </div>

        <!-- VIEW EXAM MODAL -->
        <div id="viewExamModal" class="hidden fixed inset-0 z-50 bg-black/70 backdrop-blur-sm overflow-y-auto p-2 sm:p-4 flex justify-center items-start" style="z-index: 9999;">
            <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-6xl overflow-hidden shadow-2xl my-3 sm:my-6">
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

                    <!-- Curriculum Classification Metadata -->
                    <div class="p-3.5 bg-slate-950 rounded-xl border border-slate-800 space-y-2">
                        <span class="block text-[10px] font-bold text-slate-400 uppercase tracking-wider">Curriculum Hierarchy</span>
                        <div class="grid grid-cols-2 sm:grid-cols-5 gap-2">
                            <div class="p-2 bg-slate-900 rounded-lg border border-slate-800">
                                <span class="block text-[9px] font-semibold text-slate-400 uppercase">Syllabus</span>
                                <span id="view_exam_syllabus" class="text-xs font-bold text-indigo-300 mt-0.5 block truncate">N/A</span>
                            </div>
                            <div class="p-2 bg-slate-900 rounded-lg border border-slate-800">
                                <span class="block text-[9px] font-semibold text-slate-400 uppercase">Class</span>
                                <span id="view_exam_standard" class="text-xs font-bold text-sky-300 mt-0.5 block truncate">N/A</span>
                            </div>
                            <div class="p-2 bg-slate-900 rounded-lg border border-slate-800">
                                <span class="block text-[9px] font-semibold text-slate-400 uppercase">Subject</span>
                                <span id="view_exam_subject" class="text-xs font-bold text-emerald-300 mt-0.5 block truncate">N/A</span>
                            </div>
                            <div class="p-2 bg-slate-900 rounded-lg border border-slate-800">
                                <span class="block text-[9px] font-semibold text-slate-400 uppercase">Chapter</span>
                                <span id="view_exam_chapter" class="text-xs font-bold text-cyan-300 mt-0.5 block truncate">N/A</span>
                            </div>
                            <div class="p-2 bg-slate-900 rounded-lg border border-slate-800">
                                <span class="block text-[9px] font-semibold text-slate-400 uppercase">Topic</span>
                                <span id="view_exam_topic" class="text-xs font-bold text-purple-300 mt-0.5 block truncate">N/A</span>
                            </div>
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

            function escapeHtmlText(str) {
                if (!str && str !== 0) return '';
                return String(str)
                    .replace(/&/g, '&amp;')
                    .replace(/</g, '&lt;')
                    .replace(/>/g, '&gt;')
                    .replace(/"/g, '&quot;')
                    .replace(/'/g, '&#039;');
            }

            function openViewExamModal(dataOrId) {
                let data = dataOrId;
                if (typeof dataOrId === 'string' || typeof dataOrId === 'number') {
                    const el = document.getElementById('exam-view-data-' + dataOrId);
                    if (el) {
                        try {
                            data = JSON.parse(el.textContent);
                        } catch (e) {
                            console.error('Error parsing exam-view-data:', e);
                        }
                    }
                }
                if (!data) return;

                document.getElementById('view_exam_name').textContent = data.name || '';
                document.getElementById('view_exam_type').textContent = data.type || '';
                document.getElementById('view_exam_status').textContent = data.status || '';
                document.getElementById('view_exam_total_mark').textContent = (data.total_mark || 0) + ' Mark(s)';
                document.getElementById('view_exam_creator').textContent = data.creator || 'System';

                // Curriculum Metadata
                document.getElementById('view_exam_syllabus').textContent = data.syllabus_name || 'N/A';
                document.getElementById('view_exam_standard').textContent = data.standard_name || 'N/A';
                document.getElementById('view_exam_subject').textContent = data.subject_name || 'N/A';
                document.getElementById('view_exam_chapter').textContent = data.chapter_name || 'N/A';
                document.getElementById('view_exam_topic').textContent = data.topic_name || 'N/A';
                
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
                window.currentExamViewQuestions = questions;
                qCountBadge.textContent = questions.length + ' Question(s)';

                if (questions.length === 0) {
                    qListContainer.innerHTML = '<p class="text-xs text-slate-500 text-center py-6">No questions linked to this exam yet.</p>';
                } else {
                    questions.forEach((q, idx) => {
                        const itemHtml = `
                            <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 hover:border-slate-700 transition-all flex items-start justify-between gap-3">
                                <div class="space-y-1 flex-1">
                                    <div class="flex items-center space-x-2">
                                        <span class="text-xs font-bold text-indigo-400">Q${idx + 1}.</span>
                                        <h6 class="text-xs font-semibold text-slate-200 hover:text-white transition-colors cursor-pointer" onclick="openQuestionPreviewModalByIndex(${idx})">${escapeHtmlText(q.name)}</h6>
                                    </div>
                                    ${q.description ? `<p class="text-xs text-slate-400 pl-6 line-clamp-1">${escapeHtmlText(q.description)}</p>` : ''}
                                    <div class="flex items-center flex-wrap gap-2 mt-1.5 text-[11px] text-slate-400">
                                        <span class="px-2 py-0.5 rounded bg-indigo-500/10 text-indigo-300 border border-indigo-500/20 font-medium">Class: ${escapeHtmlText(q.standard || 'N/A')}</span>
                                        <span class="px-2 py-0.5 rounded bg-slate-800 text-slate-300 border border-slate-700">By: ${escapeHtmlText(q.creator || 'System')}</span>
                                        <span class="px-2 py-0.5 rounded bg-slate-800 text-slate-300 border border-slate-700">Type: ${escapeHtmlText(q.type || 'Single Option')}</span>
                                        ${q.hint ? `<span class="px-2 py-0.5 rounded bg-amber-500/10 text-amber-300 border border-amber-500/20 font-bold text-[10px]">💡 Hint</span>` : ''}
                                        ${q.solution ? `<span class="px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-300 border border-emerald-500/20 font-bold text-[10px]">📝 Solution</span>` : ''}
                                    </div>
                                </div>
                                <div class="flex items-center space-x-2 shrink-0">
                                    <button type="button" onclick="openQuestionPreviewModalByIndex(${idx})" class="px-2.5 py-1 rounded-lg bg-indigo-500/10 hover:bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 text-xs font-medium transition-all inline-flex items-center space-x-1 cursor-pointer">
                                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                                        <span>View</span>
                                    </button>
                                    <span class="text-xs font-bold text-amber-400 bg-amber-500/10 px-2 py-0.5 rounded border border-amber-500/20">${escapeHtmlText(q.marks)} Mark(s)</span>
                                </div>
                            </div>
                        `;
                        qListContainer.innerHTML += itemHtml;
                    });
                }

                document.getElementById('viewExamModal').classList.remove('hidden');
            }

            function openQuestionPreviewModalByIndex(idx) {
                if (window.currentExamViewQuestions && window.currentExamViewQuestions[idx]) {
                    openQuestionPreviewModal(window.currentExamViewQuestions[idx]);
                }
            }

            function openEditExamModal(dataOrId) {
                let data = dataOrId;
                if (typeof dataOrId === 'string' || typeof dataOrId === 'number') {
                    const el = document.getElementById('exam-edit-data-' + dataOrId);
                    if (el) {
                        try {
                            data = JSON.parse(el.textContent);
                        } catch (e) {
                            console.error('Error parsing exam-edit-data:', e);
                        }
                    }
                }
                if (!data) return;

                const actionUrl = '/exams/' + data.id;
                document.getElementById('editExamForm').action = actionUrl;
                document.getElementById('edit_action_url').value = actionUrl;
                document.getElementById('edit_exam_name').value = data.name || '';
                document.getElementById('edit_exam_type').value = data.type || 1;
                document.getElementById('edit_exam_duration').value = data.duration || '';
                toggleEditExamDuration(data.type || 1);
                document.getElementById('edit_exam_status').value = data.status || 1;

                // Curriculum Hierarchy population
                const sylElem = document.getElementById('edit_exam_syllabus');
                if (sylElem) {
                    sylElem.value = data.syllabus_id || '';
                    onExamSyllabusChange('edit');
                }

                const stdElem = document.getElementById('edit_exam_standard');
                if (stdElem) {
                    stdElem.value = data.standard_id || '';
                }

                const subjElem = document.getElementById('edit_exam_subject');
                if (subjElem) {
                    subjElem.value = data.subject_id || '';
                    onExamSubjectChange('edit');
                }

                const chElem = document.getElementById('edit_exam_chapter');
                if (chElem) {
                    chElem.value = data.chapter_id || '';
                    onExamChapterChange('edit');
                }

                const tpElem = document.getElementById('edit_exam_topic');
                if (tpElem) {
                    tpElem.value = data.topic_id || '';
                }

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
                filterModalQuestions('create');
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
                filterModalQuestions('edit');
            }

            const syllabusesDataExam = @json($syllabusesData);
            const subjectsDataExam = @json($subjectsData);
            const standardsDataExam = @json($standards);

            function onIndexFilterSyllabusChange() {
                const syllabusId = document.getElementById('index_filter_syllabus')?.value || '';
                const subjectSelect = document.getElementById('index_filter_subject');
                const chapterSelect = document.getElementById('index_filter_chapter');
                const topicSelect = document.getElementById('index_filter_topic');

                if (subjectSelect) {
                    subjectSelect.innerHTML = '<option value="">All Subjects</option>';
                    let subjectsToShow = [];
                    if (syllabusId) {
                        const syl = syllabusesDataExam.find(s => String(s.id) === String(syllabusId));
                        if (syl && syl.subjects) {
                            subjectsToShow = syl.subjects;
                        }
                    } else {
                        subjectsToShow = subjectsDataExam;
                    }
                    subjectsToShow.forEach(subj => {
                        const opt = document.createElement('option');
                        opt.value = subj.id;
                        opt.textContent = subj.name;
                        subjectSelect.appendChild(opt);
                    });
                }

                if (chapterSelect) {
                    chapterSelect.innerHTML = '<option value="">All Chapters</option>';
                }
                if (topicSelect) {
                    topicSelect.innerHTML = '<option value="">All Topics</option>';
                }
            }

            function onIndexFilterSubjectChange() {
                const subjectId = document.getElementById('index_filter_subject')?.value || '';
                const chapterSelect = document.getElementById('index_filter_chapter');
                const topicSelect = document.getElementById('index_filter_topic');

                if (chapterSelect) {
                    chapterSelect.innerHTML = '<option value="">All Chapters</option>';
                    if (subjectId) {
                        const subj = subjectsDataExam.find(s => String(s.id) === String(subjectId));
                        if (subj && subj.chapters) {
                            subj.chapters.forEach(ch => {
                                const opt = document.createElement('option');
                                opt.value = ch.id;
                                opt.textContent = ch.name;
                                chapterSelect.appendChild(opt);
                            });
                        }
                    }
                }

                if (topicSelect) {
                    topicSelect.innerHTML = '<option value="">All Topics</option>';
                }
            }

            function onIndexFilterChapterChange() {
                const subjectId = document.getElementById('index_filter_subject')?.value || '';
                const chapterId = document.getElementById('index_filter_chapter')?.value || '';
                const topicSelect = document.getElementById('index_filter_topic');

                if (topicSelect) {
                    topicSelect.innerHTML = '<option value="">All Topics</option>';
                    if (subjectId && chapterId) {
                        const subj = subjectsDataExam.find(s => String(s.id) === String(subjectId));
                        if (subj && subj.chapters) {
                            const ch = subj.chapters.find(c => String(c.id) === String(chapterId));
                            if (ch && ch.topics) {
                                ch.topics.forEach(tp => {
                                    const opt = document.createElement('option');
                                    opt.value = tp.id;
                                    opt.textContent = tp.name;
                                    topicSelect.appendChild(opt);
                                });
                            }
                        }
                    }
                }
            }

            function onExamSyllabusChange(prefix) {
                const syllabusId = document.getElementById(prefix + '_exam_syllabus')?.value || '';
                const standardSelect = document.getElementById(prefix + '_exam_standard');
                const subjectSelect = document.getElementById(prefix + '_exam_subject');
                const chapterSelect = document.getElementById(prefix + '_exam_chapter');
                const topicSelect = document.getElementById(prefix + '_exam_topic');

                if (standardSelect) {
                    const curStdVal = standardSelect.value;
                    standardSelect.innerHTML = '<option value="">Select Class</option>';
                    standardsDataExam.forEach(std => {
                        if (!syllabusId || String(std.syllabus_id) === String(syllabusId)) {
                            const opt = document.createElement('option');
                            opt.value = std.id;
                            opt.textContent = std.name;
                            opt.setAttribute('data-syllabus-id', std.syllabus_id || '');
                            if (String(std.id) === String(curStdVal)) opt.selected = true;
                            standardSelect.appendChild(opt);
                        }
                    });
                }

                if (subjectSelect) {
                    const curSubjVal = subjectSelect.value;
                    subjectSelect.innerHTML = '<option value="">Select Subject</option>';
                    subjectsDataExam.forEach(sb => {
                        if (!syllabusId || String(sb.syllabus_id) === String(syllabusId)) {
                            const opt = document.createElement('option');
                            opt.value = sb.id;
                            opt.textContent = sb.name;
                            opt.setAttribute('data-syllabus-id', sb.syllabus_id || '');
                            if (String(sb.id) === String(curSubjVal)) opt.selected = true;
                            subjectSelect.appendChild(opt);
                        }
                    });
                }

                if (chapterSelect) chapterSelect.innerHTML = '<option value="">Select Chapter</option>';
                if (topicSelect) topicSelect.innerHTML = '<option value="">Select Topic</option>';
            }

            function onExamStandardChange(prefix) {
                const standardSelect = document.getElementById(prefix + '_exam_standard');
                const standardId = standardSelect?.value || '';

                if (standardId) {
                    const stdObj = standardsDataExam.find(s => String(s.id) === String(standardId));
                    if (stdObj && stdObj.syllabus_id) {
                        const sylSelect = document.getElementById(prefix + '_exam_syllabus');
                        if (sylSelect && !sylSelect.value) {
                            sylSelect.value = stdObj.syllabus_id;
                            onExamSyllabusChange(prefix);
                            if (standardSelect) standardSelect.value = standardId;
                        }
                    }

                    const checkboxes = document.querySelectorAll(prefix === 'create' ? 'input[name="standard_ids[]"]' : '.edit-exam-std-checkbox');
                    checkboxes.forEach(cb => {
                        if (String(cb.value) === String(standardId)) {
                            cb.checked = true;
                        }
                    });

                    const qStdFilter = document.getElementById(prefix + '_search_q_standard');
                    if (qStdFilter) {
                        qStdFilter.value = standardId;
                        filterModalQuestions(prefix);
                    }
                }
            }

            function onExamSubjectChange(prefix) {
                const subjectId = document.getElementById(prefix + '_exam_subject')?.value || '';
                const chapterSelect = document.getElementById(prefix + '_exam_chapter');
                const topicSelect = document.getElementById(prefix + '_exam_topic');

                if (chapterSelect) {
                    chapterSelect.innerHTML = '<option value="">Select Chapter</option>';
                }
                if (topicSelect) {
                    topicSelect.innerHTML = '<option value="">Select Topic</option>';
                }

                if (subjectId) {
                    const selectedSubject = subjectsDataExam.find(s => String(s.id) === String(subjectId));
                    if (selectedSubject) {
                        if (selectedSubject.syllabus_id) {
                            const sylSelect = document.getElementById(prefix + '_exam_syllabus');
                            if (sylSelect && !sylSelect.value) {
                                sylSelect.value = selectedSubject.syllabus_id;
                            }
                        }

                        if (chapterSelect && selectedSubject.chapters) {
                            selectedSubject.chapters.forEach(ch => {
                                const opt = document.createElement('option');
                                opt.value = ch.id;
                                opt.textContent = ch.name;
                                chapterSelect.appendChild(opt);
                            });
                        }
                    }
                }

                const qSubjFilter = document.getElementById(prefix + '_search_q_subject');
                if (qSubjFilter) {
                    qSubjFilter.value = subjectId;
                    onModalSubjectChange(prefix);
                }
            }

            function onExamChapterChange(prefix) {
                const subjectId = document.getElementById(prefix + '_exam_subject')?.value || '';
                const chapterId = document.getElementById(prefix + '_exam_chapter')?.value || '';
                const topicSelect = document.getElementById(prefix + '_exam_topic');

                if (topicSelect) {
                    topicSelect.innerHTML = '<option value="">Select Topic</option>';
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

                const qChFilter = document.getElementById(prefix + '_search_q_chapter');
                if (qChFilter) {
                    qChFilter.value = chapterId;
                    onModalChapterChange(prefix);
                }
            }

            function onExamTopicChange(prefix) {
                const topicId = document.getElementById(prefix + '_exam_topic')?.value || '';
                const qTpFilter = document.getElementById(prefix + '_search_q_topic');
                if (qTpFilter) {
                    qTpFilter.value = topicId;
                    filterModalQuestions(prefix);
                }
            }

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

                const examTypeElem = document.getElementById(prefix + '_exam_type');
                const examTypeVal = examTypeElem ? parseInt(examTypeElem.value) : 1;
                const isTextEntryExam = examTypeVal === 3;

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
                    const qType = parseInt(item.getAttribute('data-type') || '1');

                    const matchesExamType = isTextEntryExam ? (qType === 3) : (qType !== 3);

                    // Uncheck incompatible questions if exam type was changed
                    const checkbox = item.querySelector('input[type="checkbox"]');
                    if (checkbox && checkbox.checked && !matchesExamType) {
                        checkbox.checked = false;
                    }

                    const matchesName = !nameQuery || qName.includes(nameQuery);
                    const matchesCreator = !creatorQuery || qCreator.includes(creatorQuery);
                    const matchesStandard = !standardQuery || qStandardId === standardQuery || qStandard.includes(standardQuery);
                    const matchesSubject = !subjectQuery || qSubjectId === subjectQuery;
                    const matchesChapter = !chapterQuery || qChapterId === chapterQuery;
                    const matchesTopic = !topicQuery || qTopicId === topicQuery;
                    const matchesType = !typeQuery || String(qType) === typeQuery;

                    if (matchesExamType && matchesName && matchesCreator && matchesStandard && matchesSubject && matchesChapter && matchesTopic && matchesType) {
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

                // Restore index search filter cascade if query parameters are present
                const curFilterSyl = "{{ request('syllabus_id') }}";
                const curFilterSubj = "{{ request('subject_id') }}";
                const curFilterCh = "{{ request('chapter_id') }}";
                const curFilterTp = "{{ request('topic_id') }}";

                if (curFilterSyl) {
                    onIndexFilterSyllabusChange();
                    const subjEl = document.getElementById('index_filter_subject');
                    if (subjEl && curFilterSubj) {
                        subjEl.value = curFilterSubj;
                        onIndexFilterSubjectChange();
                        const chEl = document.getElementById('index_filter_chapter');
                        if (chEl && curFilterCh) {
                            chEl.value = curFilterCh;
                            onIndexFilterChapterChange();
                            const tpEl = document.getElementById('index_filter_topic');
                            if (tpEl && curFilterTp) {
                                tpEl.value = curFilterTp;
                            }
                        }
                    }
                } else if (curFilterSubj) {
                    onIndexFilterSubjectChange();
                    const chEl = document.getElementById('index_filter_chapter');
                    if (chEl && curFilterCh) {
                        chEl.value = curFilterCh;
                        onIndexFilterChapterChange();
                        const tpEl = document.getElementById('index_filter_topic');
                        if (tpEl && curFilterTp) {
                            tpEl.value = curFilterTp;
                        }
                    }
                }
            });
        </script>

        <!-- QUESTION PREVIEW POPUP MODAL -->
        <div id="questionPreviewModal" class="hidden fixed inset-0 z-50 bg-black/75 backdrop-blur-md overflow-y-auto p-2 sm:p-4 flex justify-center items-start" style="z-index: 10000;">
            <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-3xl overflow-hidden shadow-2xl my-3 sm:my-6">
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

                    <!-- Hint Container -->
                    <div id="preview_q_hint_container" class="hidden p-4 rounded-xl bg-amber-950/30 border border-amber-800/40">
                        <span class="block text-[11px] font-extrabold text-amber-300 uppercase tracking-wider mb-1">💡 Hint</span>
                        <p id="preview_q_hint" class="text-xs text-amber-200/90 leading-relaxed whitespace-pre-line"></p>
                    </div>

                    <!-- Solution Container -->
                    <div id="preview_q_solution_container" class="hidden p-4 rounded-xl bg-emerald-950/30 border border-emerald-800/40">
                        <span class="block text-[11px] font-extrabold text-emerald-300 uppercase tracking-wider mb-1">📝 Solution / Explanation</span>
                        <p id="preview_q_solution" class="text-xs text-emerald-200/90 leading-relaxed whitespace-pre-line"></p>
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
                document.getElementById('preview_q_name').innerHTML = data.name || '';
                document.getElementById('preview_q_standard').textContent = 'Class: ' + (data.standard_name || data.standard || 'N/A');

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
                if (parseInt(data.type) === 2 || parseInt(data.type_id) === 2) typeStr = 'Multiple Option';
                if (parseInt(data.type) === 3 || parseInt(data.type_id) === 3) typeStr = 'Text Entry';
                if (parseInt(data.type) === 4 || parseInt(data.type_id) === 4) typeStr = 'True / False';
                if (parseInt(data.type) === 5 || parseInt(data.type_id) === 5) typeStr = 'Match the Following';
                document.getElementById('preview_q_type').textContent = 'Type: ' + typeStr;

                document.getElementById('preview_q_marks').textContent = (data.marks || 0) + ' Mark(s)';
                document.getElementById('preview_q_creator').textContent = 'By: ' + (data.creator_name || data.creator || 'System');

                const descContainer = document.getElementById('preview_q_desc_container');
                const descText = document.getElementById('preview_q_description');
                if (data.description && data.description.trim() !== '') {
                    descText.textContent = data.description;
                    descContainer.classList.remove('hidden');
                } else {
                    descContainer.classList.add('hidden');
                }

                const hintContainer = document.getElementById('preview_q_hint_container');
                const hintText = document.getElementById('preview_q_hint');
                if (hintContainer && hintText) {
                    if (data.hint && data.hint.trim() !== '') {
                        hintText.textContent = data.hint;
                        hintContainer.classList.remove('hidden');
                    } else {
                        hintContainer.classList.add('hidden');
                    }
                }

                const solutionContainer = document.getElementById('preview_q_solution_container');
                const solutionText = document.getElementById('preview_q_solution');
                if (solutionContainer && solutionText) {
                    if (data.solution && data.solution.trim() !== '') {
                        solutionText.textContent = data.solution;
                        solutionContainer.classList.remove('hidden');
                    } else {
                        solutionContainer.classList.add('hidden');
                    }
                }

                const answersList = document.getElementById('preview_q_answers_list');
                answersList.innerHTML = '';

                const answers = data.answers || [];
                if (parseInt(data.type) === 3 || parseInt(data.type_id) === 3) {
                    answersList.innerHTML = '<p class="text-xs text-slate-400 italic p-3 rounded-lg bg-slate-950 border border-slate-800">Students will type a written text answer for this question.</p>';
                } else if (parseInt(data.type) === 5 || parseInt(data.type_id) === 5) {
                    if (answers.length === 0) {
                        answersList.innerHTML = '<p class="text-xs text-slate-500 italic p-3 rounded-lg bg-slate-950 border border-slate-800">No matching pairs configured.</p>';
                    } else {
                        answers.forEach((ans, idx) => {
                            const itemHtml = `
                                <div class="p-3 rounded-xl border border-indigo-500/30 bg-slate-950/80 flex items-center justify-between text-xs">
                                    <div class="flex items-center space-x-2.5">
                                        <span class="w-6 text-[11px] font-bold text-indigo-400">#${idx + 1}</span>
                                        <span class="text-white font-medium">${escapeHtmlText(ans.name)}</span>
                                    </div>
                                    <div class="flex items-center space-x-2">
                                        <span class="text-indigo-400 font-bold">⟷</span>
                                        <span class="px-2.5 py-1 rounded-lg bg-indigo-500/10 text-indigo-300 border border-indigo-500/20 font-semibold">${escapeHtmlText(ans.match_answer || 'N/A')}</span>
                                    </div>
                                </div>
                            `;
                            answersList.innerHTML += itemHtml;
                        });
                    }
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

            let currentEvaluationData = null;

            function openStudentViewSubmissionModal(dataOrId) {
                let data = dataOrId;
                if (typeof dataOrId === 'string' || typeof dataOrId === 'number') {
                    const el = document.getElementById('submission-data-' + dataOrId);
                    if (el) {
                        try {
                            data = JSON.parse(el.textContent);
                        } catch (e) {
                            console.error('Error parsing submission-data:', e);
                        }
                    }
                }
                if (!data) return;

                currentEvaluationData = data;

                const totalMark = data.total_mark || 0;
                const obtainedMark = data.obtained_mark || 0;
                const pct = totalMark > 0 ? Math.round((obtainedMark / totalMark) * 100) : 0;

                const examTitle = data.name || 'Submitted Exam Performance';
                const studentLabel = data.student_name ? ` (${data.student_name})` : '';
                document.getElementById('modal_top_exam_name').textContent = examTitle + studentLabel;
                document.getElementById('modal_top_score_badge').textContent = `${obtainedMark}/${totalMark}`;

                document.getElementById('sub_exam_name').textContent = examTitle + (data.student_name ? ` - Student: ${data.student_name}` : '');
                document.getElementById('sub_exam_score_heading').textContent = `${obtainedMark}/${totalMark}`;
                
                const pctBadge = document.getElementById('sub_exam_percentage_badge');
                pctBadge.textContent = `${pct}% Overall`;
                if (pct >= 80) {
                    pctBadge.className = "px-4 py-2 rounded-xl bg-emerald-100 text-black border border-emerald-300 font-black text-sm text-center shadow-sm";
                } else if (pct >= 50) {
                    pctBadge.className = "px-4 py-2 rounded-xl bg-amber-100 text-black border border-amber-300 font-black text-sm text-center shadow-sm";
                } else {
                    pctBadge.className = "px-4 py-2 rounded-xl bg-rose-100 text-black border border-rose-300 font-black text-sm text-center shadow-sm";
                }

                const container = document.getElementById('sub_details_list');
                container.innerHTML = '';

                const details = data.details || [];
                let correctCount = 0;
                let wrongCount = 0;
                let partialCount = 0;
                let textEntryCount = 0;

                details.forEach(d => {
                    if (d.is_text_entry) textEntryCount++;
                    else if (d.is_correct) correctCount++;
                    else if (d.is_partially_correct) partialCount++;
                    else wrongCount++;
                });

                document.getElementById('sub_summary_total_q').textContent = details.length;
                document.getElementById('sub_summary_correct_cnt').textContent = textEntryCount > 0
                    ? `${correctCount} Correct${partialCount > 0 ? `, ${partialCount} Partial` : ''}`
                    : (partialCount > 0 ? `${correctCount} Correct, ${partialCount} Partial` : `${correctCount} Question(s)`);
                document.getElementById('sub_summary_wrong_cnt').textContent = textEntryCount > 0
                    ? `${textEntryCount} Text Entry`
                    : `${wrongCount} Question(s)`;

                if (details.length === 0) {
                    container.innerHTML = '<div class="p-8 text-center bg-white rounded-xl border border-slate-200 text-slate-500 text-sm font-medium">No detailed questions or answers found for this submission.</div>';
                } else {
                    details.forEach((d, idx) => {
                        const isTextEntry = d.is_text_entry;
                        const isEvaluated = d.is_evaluated || (d.teacher_marks !== null && d.teacher_marks !== undefined);
                        const isCorrect = d.is_correct;
                        const isPartial = d.is_partially_correct;
                        const earnedMarks = d.earned_marks !== undefined ? d.earned_marks : (isCorrect ? d.question_marks : 0);

                        let cardBorderClass = 'border-l-4 border-l-rose-500 border-t border-r border-b border-slate-200 bg-white';
                        let statusBadge = `<span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-black bg-rose-100 text-black border border-rose-300">
                                             <svg class="w-3.5 h-3.5 mr-1 text-black shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12"/></svg>
                                             Wrong (0 Marks)
                                           </span>`;

                        if (isTextEntry) {
                            if (isEvaluated) {
                                cardBorderClass = 'border-l-4 border-l-emerald-500 border-t border-r border-b border-slate-200 bg-white';
                                statusBadge = `<span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-black bg-emerald-100 text-black border border-emerald-300">
                                                 <svg class="w-3.5 h-3.5 mr-1 text-black shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>
                                                 Evaluated (+${escapeHtmlText(earnedMarks)} / ${escapeHtmlText(d.question_marks)} Marks)
                                               </span>`;
                            } else {
                                cardBorderClass = 'border-l-4 border-l-amber-500 border-t border-r border-b border-slate-200 bg-white';
                                statusBadge = `<span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-black bg-amber-100 text-black border border-amber-300">
                                                 <svg class="w-3.5 h-3.5 mr-1 text-black shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
                                                 Pending Evaluation
                                               </span>`;
                            }
                        } else if (isCorrect) {
                            cardBorderClass = 'border-l-4 border-l-emerald-500 border-t border-r border-b border-slate-200 bg-white';
                            statusBadge = `<span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-black bg-emerald-100 text-black border border-emerald-300">
                                             <svg class="w-3.5 h-3.5 mr-1 text-black shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>
                                             Correct (+${escapeHtmlText(earnedMarks)} Marks)
                                           </span>`;
                        } else if (isPartial) {
                            cardBorderClass = 'border-l-4 border-l-amber-500 border-t border-r border-b border-slate-200 bg-white';
                            statusBadge = `<span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-black bg-amber-100 text-black border border-amber-300">
                                             <svg class="w-3.5 h-3.5 mr-1 text-black shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
                                             Partial (+${escapeHtmlText(earnedMarks)} Marks)
                                           </span>`;
                        }

                        const ansBoxClass = isCorrect
                            ? 'bg-emerald-50/80 border-emerald-300'
                            : 'bg-rose-50/80 border-rose-300';

                        const ansIcon = isCorrect
                            ? `<span class="w-5 h-5 rounded-full bg-emerald-600 text-white flex items-center justify-center font-bold text-[10px] shrink-0">✓</span>`
                            : `<span class="w-5 h-5 rounded-full bg-rose-600 text-white flex items-center justify-center font-bold text-[10px] shrink-0">✕</span>`;

                        let correctAnswerMarkup = '';
                        if (!isCorrect && !isTextEntry && d.correct_answer) {
                            correctAnswerMarkup = `
                                <div class="mt-2 p-3 rounded-xl bg-emerald-50 border border-emerald-300 flex items-center space-x-2 text-xs">
                                    <span class="w-5 h-5 rounded-full bg-emerald-600 text-white flex items-center justify-center font-bold text-[10px] shrink-0">✓</span>
                                    <span class="text-black font-extrabold uppercase tracking-wider text-[11px]">Correct Answer:</span>
                                    <span class="text-black font-black text-sm sm:text-base ml-1">${escapeHtmlText(d.correct_answer)}</span>
                                </div>
                            `;
                        }

                        let matchPairsMarkup = '';
                        if (d.match_pairs && d.match_pairs.length > 0) {
                            matchPairsMarkup = `
                                <div class="mt-2 space-y-2">
                                    <div class="flex items-center justify-between pb-1 border-b border-slate-100">
                                        <span class="text-[10px] font-extrabold uppercase tracking-wider text-black">Matching Pairs Details (1 Mark per Match):</span>
                                        <span class="text-xs font-black text-black bg-slate-100 px-2.5 py-0.5 rounded-full border border-slate-200">${escapeHtmlText(earnedMarks)} / ${escapeHtmlText(d.question_marks)} Marks</span>
                                    </div>
                                    ${d.match_pairs.map(p => `
                                        <div class="p-2.5 rounded-xl border ${p.is_correct ? 'bg-emerald-50/90 border-emerald-300' : 'bg-rose-50/90 border-rose-300'} flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-xs">
                                            <div class="flex items-center space-x-2">
                                                <span class="w-5 h-5 rounded-md ${p.is_correct ? 'bg-emerald-600' : 'bg-rose-600'} text-white font-bold text-[10px] flex items-center justify-center shrink-0">
                                                    ${p.is_correct ? '✓' : '✕'}
                                                </span>
                                                <span class="font-bold text-black">${p.letter}. ${escapeHtmlText(p.left)}</span>
                                            </div>
                                            <div class="flex items-center space-x-2 pl-7 sm:pl-0 flex-wrap">
                                                <span class="text-black font-medium">Selected: <span class="font-extrabold ${p.is_correct ? 'text-emerald-950' : 'text-rose-950'}">${escapeHtmlText(p.student_match)}</span></span>
                                                ${!p.is_correct && p.correct_match ? `<span class="text-emerald-900 font-bold">→ Correct: <span class="font-black underline">${escapeHtmlText(p.correct_match)}</span></span>` : ''}
                                                <span class="ml-auto inline-flex items-center px-1.5 py-0.5 rounded text-[10px] font-black ${p.is_correct ? 'bg-emerald-200/80 text-emerald-950' : 'bg-rose-200/80 text-rose-950'}">
                                                    ${p.is_correct ? '+1 Mark' : '0 Marks'}
                                                </span>
                                            </div>
                                        </div>
                                    `).join('')}
                                </div>
                            `;
                        }

                        let textEntrySectionMarkup = '';
                        if (isTextEntry) {
                            let evalBox = '';
                            if (data.can_evaluate && data.is_text_entry_exam) {
                                evalBox = `
                                    <div class="mt-3 p-3.5 rounded-xl bg-indigo-50/80 border border-indigo-200 space-y-2.5">
                                        <div class="flex items-center justify-between">
                                            <span class="text-[11px] font-black text-indigo-950 uppercase tracking-wider flex items-center space-x-1">
                                                <svg class="w-3.5 h-3.5 text-indigo-700" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/></svg>
                                                <span>Teacher Marks &amp; Evaluation</span>
                                            </span>
                                            <span class="text-[11px] font-black text-indigo-900 bg-white px-2 py-0.5 rounded border border-indigo-200">Max: ${escapeHtmlText(d.question_marks)} Marks</span>
                                        </div>
                                        <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 items-end">
                                            <div>
                                                <label class="block text-[10px] font-bold text-black uppercase mb-1">Marks (0 to ${escapeHtmlText(d.question_marks)}):</label>
                                                <input type="number" min="0" max="${escapeHtmlText(d.question_marks)}" step="1" value="${d.teacher_marks !== null && d.teacher_marks !== undefined ? escapeHtmlText(d.teacher_marks) : ''}" placeholder="0" class="eval-marks-input w-full px-3 py-1.5 rounded-lg border border-slate-300 text-sm font-bold text-black bg-white focus:ring-2 focus:ring-indigo-500 focus:outline-none" data-detail-id="${d.id}" data-max="${escapeHtmlText(d.question_marks)}">
                                            </div>
                                            <div class="sm:col-span-2">
                                                <label class="block text-[10px] font-bold text-black uppercase mb-1">Teacher Feedback (Optional):</label>
                                                <input type="text" value="${escapeHtmlText(d.teacher_feedback || '')}" placeholder="e.g. Accurate steps, clear working" class="eval-feedback-input w-full px-3 py-1.5 rounded-lg border border-slate-300 text-xs text-black bg-white focus:ring-2 focus:ring-indigo-500 focus:outline-none" data-detail-id="${d.id}">
                                            </div>
                                        </div>
                                    </div>
                                `;
                            } else if (d.teacher_feedback) {
                                evalBox = `
                                    <div class="mt-2.5 p-3 rounded-xl bg-indigo-50 border border-indigo-200 text-xs">
                                        <span class="text-black font-extrabold uppercase tracking-wider text-[11px]">Teacher Feedback:</span>
                                        <p class="text-black font-medium mt-1 leading-relaxed">${escapeHtmlText(d.teacher_feedback)}</p>
                                    </div>
                                `;
                            }

                            textEntrySectionMarkup = `
                                <div class="p-3.5 rounded-xl border bg-slate-50 border-slate-300 space-y-1.5">
                                    <div class="flex items-center justify-between">
                                        <span class="text-[10px] font-extrabold uppercase tracking-wider text-black block">Student's Written Response:</span>
                                        <span class="text-xs font-bold text-black">${escapeHtmlText(earnedMarks)} / ${escapeHtmlText(d.question_marks)} Marks</span>
                                    </div>
                                    <div class="text-sm font-medium text-black whitespace-pre-wrap leading-relaxed p-2.5 rounded-lg bg-white border border-slate-200 font-sans">${escapeHtmlText(d.student_text_answer || d.selected_answer || 'No answer submitted')}</div>
                                </div>
                                ${evalBox}
                            `;
                        }

                        let hintSolutionReviewMarkup = '';
                        if (d.hint || d.solution) {
                            hintSolutionReviewMarkup = `
                                <div class="mt-2.5 p-3 rounded-xl bg-slate-50 border border-slate-200 space-y-2 text-xs">
                                    ${d.hint ? `
                                        <div class="flex items-start space-x-2">
                                            <span class="px-1.5 py-0.5 rounded bg-amber-100 text-amber-900 border border-amber-300 font-extrabold text-[10px] shrink-0 uppercase">Hint</span>
                                            <span class="text-black leading-relaxed whitespace-pre-line">${escapeHtmlText(d.hint)}</span>
                                        </div>
                                    ` : ''}
                                    ${d.solution ? `
                                        <div class="flex items-start space-x-2">
                                            <span class="px-1.5 py-0.5 rounded bg-emerald-100 text-emerald-950 border border-emerald-300 font-extrabold text-[10px] shrink-0 uppercase">Solution</span>
                                            <span class="text-black font-medium leading-relaxed whitespace-pre-line">${escapeHtmlText(d.solution)}</span>
                                        </div>
                                    ` : ''}
                                </div>
                            `;
                        }

                        const html = `
                            <div class="p-4 sm:p-5 rounded-xl ${cardBorderClass} shadow-sm space-y-3 transition-all hover:shadow-md" id="eval-card-${d.id}">
                                <div class="flex items-start justify-between gap-3">
                                    <div class="space-y-1">
                                        <div class="flex items-center space-x-2">
                                            <span class="px-2.5 py-0.5 rounded-md bg-slate-900 text-white text-xs font-extrabold shrink-0">Q${idx + 1}</span>
                                            <div class="text-sm sm:text-base font-bold text-black prose prose-sm max-w-none">${d.question_name}</div>
                                        </div>
                                    </div>
                                    <div class="shrink-0 flex items-center space-x-2" id="eval-status-${d.id}">
                                        ${statusBadge}
                                    </div>
                                </div>

                                <div class="pt-1 space-y-2">
                                    ${isTextEntry ? textEntrySectionMarkup : (d.match_pairs && d.match_pairs.length > 0 ? matchPairsMarkup : `
                                        <div class="p-3 rounded-xl border ${ansBoxClass} flex items-center justify-between gap-3">
                                            <div class="flex items-center space-x-2.5">
                                                ${ansIcon}
                                                <div>
                                                    <span class="text-[10px] font-extrabold uppercase tracking-wider text-black block">Submitted Answer</span>
                                                    <span class="text-sm sm:text-base font-black text-black">${escapeHtmlText(d.selected_answer)}</span>
                                                </div>
                                            </div>
                                            <span class="text-xs font-bold text-black">${escapeHtmlText(earnedMarks)} / ${escapeHtmlText(d.question_marks)} Marks</span>
                                        </div>

                                        ${correctAnswerMarkup}
                                    `)}
                                    ${hintSolutionReviewMarkup}
                                </div>
                            </div>
                        `;
                        container.innerHTML += html;
                    });
                }

                // Show or hide evaluation actions bar
                const evalBar = document.getElementById('modal_evaluate_actions_bar');
                if (evalBar) {
                    if (data.can_evaluate && data.is_text_entry_exam) {
                        evalBar.classList.remove('hidden');
                    } else {
                        evalBar.classList.add('hidden');
                    }
                }

                document.getElementById('studentViewSubmissionModal').classList.remove('hidden');
            }

            function submitEvaluationMarks() {
                if (!currentEvaluationData || !currentEvaluationData.evaluate_url) return;

                const marksInputs = document.querySelectorAll('.eval-marks-input');
                const feedbackInputs = document.querySelectorAll('.eval-feedback-input');

                const marks = {};
                const feedback = {};

                let hasValidationError = false;

                marksInputs.forEach(input => {
                    const detailId = input.getAttribute('data-detail-id');
                    const maxMarks = parseInt(input.getAttribute('data-max') || '0', 10);
                    const val = input.value.trim();

                    if (val !== '') {
                        const numVal = parseInt(val, 10);
                        if (isNaN(numVal) || numVal < 0 || (maxMarks > 0 && numVal > maxMarks)) {
                            alert(`Marks for question must be between 0 and ${maxMarks}.`);
                            input.focus();
                            hasValidationError = true;
                            return;
                        }
                        marks[detailId] = numVal;
                    } else {
                        marks[detailId] = null;
                    }
                });

                if (hasValidationError) return;

                feedbackInputs.forEach(input => {
                    const detailId = input.getAttribute('data-detail-id');
                    feedback[detailId] = input.value.trim();
                });

                const btn = document.getElementById('btn_save_evaluation');
                const btnText = document.getElementById('btn_save_evaluation_text');
                if (btn) btn.disabled = true;
                if (btnText) btnText.textContent = 'Saving...';

                const csrfToken = document.querySelector('meta[name="csrf-token"]')?.getAttribute('content') 
                    || document.querySelector('input[name="_token"]')?.value;

                fetch(currentEvaluationData.evaluate_url, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                        'X-CSRF-TOKEN': csrfToken
                    },
                    body: JSON.stringify({ marks, feedback })
                })
                .then(res => {
                    if (!res.ok) {
                        return res.json().then(j => { throw new Error(j.message || 'Failed to save marks'); });
                    }
                    return res.json();
                })
                .then(res => {
                    if (btn) btn.disabled = false;
                    if (btnText) btnText.textContent = 'Save Marks & Feedback';

                    // Update modal metrics
                    const totalMark = res.total_mark || currentEvaluationData.total_mark;
                    const obtainedMark = res.obtained_mark !== undefined ? res.obtained_mark : 0;
                    const pct = res.percentage !== undefined ? res.percentage : (totalMark > 0 ? Math.round((obtainedMark / totalMark) * 100) : 0);

                    document.getElementById('modal_top_score_badge').textContent = `${obtainedMark}/${totalMark}`;
                    document.getElementById('sub_exam_score_heading').textContent = `${obtainedMark}/${totalMark}`;

                    const pctBadge = document.getElementById('sub_exam_percentage_badge');
                    if (pctBadge) {
                        pctBadge.textContent = `${pct}% Overall`;
                        if (pct >= 80) {
                            pctBadge.className = "px-4 py-2 rounded-xl bg-emerald-100 text-black border border-emerald-300 font-black text-sm text-center shadow-sm";
                        } else if (pct >= 50) {
                            pctBadge.className = "px-4 py-2 rounded-xl bg-amber-100 text-black border border-amber-300 font-black text-sm text-center shadow-sm";
                        } else {
                            pctBadge.className = "px-4 py-2 rounded-xl bg-rose-100 text-black border border-rose-300 font-black text-sm text-center shadow-sm";
                        }
                    }

                    // Update table row in background
                    const rowScore = document.getElementById(`score-display-${currentEvaluationData.id}-${currentEvaluationData.student_id}`);
                    if (rowScore) {
                        rowScore.textContent = `${obtainedMark} / ${totalMark}`;
                    }
                    const rowPct = document.getElementById(`pct-display-${currentEvaluationData.id}-${currentEvaluationData.student_id}`);
                    if (rowPct) {
                        rowPct.textContent = `${pct}%`;
                        rowPct.className = `px-2 py-0.5 rounded text-[10px] font-extrabold ${pct >= 80 ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30' : (pct >= 50 ? 'bg-amber-500/20 text-amber-300 border border-amber-500/30' : 'bg-rose-500/20 text-rose-300 border border-rose-500/30')}`;
                    }
                    const evalBadge = document.getElementById(`eval-status-badge-${currentEvaluationData.id}-${currentEvaluationData.student_id}`);
                    if (evalBadge) {
                        evalBadge.textContent = 'Evaluated';
                        evalBadge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
                    }

                    // Update current cached submission data
                    currentEvaluationData.obtained_mark = obtainedMark;
                    if (res.details && Array.isArray(res.details)) {
                        res.details.forEach(ud => {
                            const target = (currentEvaluationData.details || []).find(d => d.id === ud.id);
                            if (target) {
                                target.earned_marks = ud.earned_marks;
                                target.teacher_marks = ud.teacher_marks;
                                target.teacher_feedback = ud.teacher_feedback;
                                target.is_evaluated = ud.is_evaluated;
                                target.is_correct = ud.is_correct;
                                target.is_partially_correct = ud.is_partially_correct;

                                const cardEl = document.getElementById(`eval-card-${ud.id}`);
                                const statusEl = document.getElementById(`eval-status-${ud.id}`);
                                if (cardEl) {
                                    cardEl.className = 'p-4 sm:p-5 rounded-xl border-l-4 border-l-emerald-500 border-t border-r border-b border-slate-200 bg-white shadow-sm space-y-3 transition-all hover:shadow-md';
                                }
                                if (statusEl) {
                                    statusEl.innerHTML = `<span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-black bg-emerald-100 text-black border border-emerald-300">
                                        <svg class="w-3.5 h-3.5 mr-1 text-black shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>
                                        Evaluated (+${ud.earned_marks} / ${target.question_marks} Marks)
                                    </span>`;
                                }
                            }
                        });
                    }

                    // Also update script element if present
                    const scriptEl = document.getElementById(`submission-data-${currentEvaluationData.id}-${currentEvaluationData.student_id}`);
                    if (scriptEl) {
                        scriptEl.textContent = JSON.stringify(currentEvaluationData);
                    }

                    alert('Marks and feedback have been successfully saved!');
                })
                .catch(err => {
                    if (btn) btn.disabled = false;
                    if (btnText) btnText.textContent = 'Save Marks & Feedback';
                    alert('Error saving evaluation: ' + err.message);
                });
            }
        </script>

        <!-- STUDENT VIEW SUBMISSION DETAILS MODAL -->
        <div id="studentViewSubmissionModal" class="hidden fixed inset-0 z-50 bg-slate-900/70 backdrop-blur-sm flex items-center justify-center p-4" style="z-index: 9999;">
            <div class="bg-white rounded-2xl w-full max-w-2xl flex flex-col shadow-2xl border border-slate-200/80 text-slate-900" style="height:85vh;max-height:85vh;overflow:hidden;">

                <!-- Header -->
                <div class="px-6 py-4 bg-indigo-900 flex items-center justify-between" style="flex-shrink:0;">
                    <div class="flex items-center gap-3">
                        <div class="w-9 h-9 rounded-xl bg-emerald-400/20 border border-emerald-400/30 flex items-center justify-center shrink-0">
                            <svg class="w-5 h-5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                            </svg>
                        </div>
                        <div>
                            <h3 id="modal_top_exam_name" class="text-sm sm:text-base font-bold text-white line-clamp-1">Exam Performance</h3>
                            <p class="text-[11px] text-white font-bold">Question-by-question evaluation &amp; marks</p>
                        </div>
                    </div>
                    <div class="flex items-center gap-3 shrink-0">
                        <div class="px-3 py-1.5 rounded-lg bg-emerald-500/15 border border-emerald-500/30 flex items-center gap-1.5">
                            <span class="text-[10px] font-semibold text-slate-400 uppercase tracking-wider">Score</span>
                            <span id="modal_top_score_badge" class="font-mono font-bold text-sm text-white">0/0</span>
                        </div>
                        <button type="button" onclick="document.getElementById('studentViewSubmissionModal').classList.add('hidden')" class="w-8 h-8 rounded-lg bg-white/5 hover:bg-white/15 text-slate-400 hover:text-white flex items-center justify-center transition-colors cursor-pointer">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                        </button>
                    </div>
                </div>

                <!-- Scrollable Body -->
                <div class="bg-slate-50" style="flex:1;min-height:0;overflow-y:auto;">
                    <!-- Summary Banner -->
                    <div class="p-5 border-b border-slate-200 bg-white">
                        <div class="flex flex-col sm:flex-row sm:items-start justify-between gap-4">
                            <div class="flex-1 min-w-0">
                                <p class="text-[10px] font-semibold text-slate-400 uppercase tracking-widest">Exam Title</p>
                                <h4 id="sub_exam_name" class="text-lg font-extrabold text-slate-900 mt-0.5 leading-tight"></h4>
                            </div>
                            <div class="flex items-center gap-3 shrink-0">
                                <div class="text-center px-4 py-2.5 rounded-xl bg-slate-900 shadow-lg">
                                    <p class="text-[9px] font-bold uppercase tracking-widest text-slate-400">Final Score</p>
                                    <p id="sub_exam_score_heading" class="text-lg font-black text-emerald-400 font-mono mt-0.5">0/0</p>
                                </div>
                                <div id="sub_exam_percentage_badge" class="text-center px-4 py-2.5 rounded-xl border-2 border-emerald-300 bg-emerald-50 font-black text-base text-emerald-700 shadow-sm min-w-[60px]">
                                    <!-- JS fills % -->
                                </div>
                            </div>
                        </div>

                        <!-- Stat Pills -->
                        <div class="grid grid-cols-3 gap-3 mt-4">
                            <div class="flex items-center gap-2.5 p-3 rounded-xl bg-slate-50 border border-slate-200">
                                <div class="w-8 h-8 rounded-lg bg-slate-800 flex items-center justify-center shrink-0">
                                    <svg class="w-4 h-4 text-slate-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                                </div>
                                <div>
                                    <p class="text-[10px] font-semibold text-slate-400 uppercase leading-none">Total</p>
                                    <p id="sub_summary_total_q" class="text-base font-extrabold text-slate-800 mt-0.5">0</p>
                                </div>
                            </div>
                            <div class="flex items-center gap-2.5 p-3 rounded-xl bg-emerald-50 border border-emerald-200">
                                <div class="w-8 h-8 rounded-lg bg-emerald-600 flex items-center justify-center text-white font-bold text-sm shrink-0">✓</div>
                                <div>
                                    <p class="text-[10px] font-semibold text-emerald-600 uppercase leading-none">Correct</p>
                                    <p id="sub_summary_correct_cnt" class="text-base font-extrabold text-emerald-700 mt-0.5">0</p>
                                </div>
                            </div>
                            <div class="flex items-center gap-2.5 p-3 rounded-xl bg-rose-50 border border-rose-200">
                                <div class="w-8 h-8 rounded-lg bg-rose-600 flex items-center justify-center text-white font-bold text-sm shrink-0">✕</div>
                                <div>
                                    <p class="text-[10px] font-semibold text-rose-600 uppercase leading-none">Wrong</p>
                                    <p id="sub_summary_wrong_cnt" class="text-base font-extrabold text-rose-700 mt-0.5">0</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Question List -->
                    <div class="p-5 space-y-3">
                        <div class="flex items-center justify-between">
                            <h4 class="text-xs font-bold text-slate-500 uppercase tracking-widest">Question Breakdown</h4>
                            <span class="text-xs text-slate-400">Review each answer below</span>
                        </div>
                        <div id="sub_details_list" class="space-y-2.5">
                            <!-- Populated dynamically via JS -->
                        </div>
                    </div>
                </div>

                <!-- Footer -->
                <div class="px-5 py-3.5 bg-white border-t border-slate-200 flex items-center justify-between gap-3 shrink-0">
                    <div id="modal_evaluate_actions_bar" class="hidden flex items-center space-x-2">
                        <button type="button" id="btn_save_evaluation" onclick="submitEvaluationMarks()" class="px-5 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold shadow-md transition-all inline-flex items-center space-x-1.5 cursor-pointer">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                            <span id="btn_save_evaluation_text">Save Marks &amp; Feedback</span>
                        </button>
                    </div>
                    <button type="button" onclick="document.getElementById('studentViewSubmissionModal').classList.add('hidden')" class="px-5 py-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-white text-xs font-bold shadow-md transition-all cursor-pointer ml-auto">
                        Close
                    </button>
                </div>
            </div>
        </div>

        <x-exam-leaderboard-modal />

    </div>
</x-layouts.app>
