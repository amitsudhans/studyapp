<x-layouts.app title="Questions Management - Study App">
    <!-- KaTeX Mathematical Typography Engine -->
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>

    <!-- Quill.js Rich Text Editor Assets -->
    <link href="https://cdn.jsdelivr.net/npm/quill@2.0.2/dist/quill.snow.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/quill@2.0.2/dist/quill.js"></script>

    <style>
        /* Quill Dark Mode Customization */
        .ql-toolbar.ql-snow {
            background-color: #0f172a !important;
            border-color: #334155 !important;
            border-top-left-radius: 0.75rem;
            border-top-right-radius: 0.75rem;
            border-bottom: 1px solid #1e293b !important;
            padding: 4px 8px !important;
        }
        .ql-container.ql-snow {
            background-color: #020617 !important;
            border-color: #334155 !important;
            border-top: none !important;
            border-bottom-left-radius: 0.75rem;
            border-bottom-right-radius: 0.75rem;
            color: #f1f5f9 !important;
            font-size: 0.8125rem !important;
            font-family: inherit;
        }
        .ql-editor {
            min-height: 85px;
            max-height: 260px;
            overflow-y: auto;
            color: #f1f5f9;
            line-height: 1.5;
            font-size: 0.8125rem;
            padding: 8px 12px !important;
        }
        .ql-editor img {
            max-width: 100%;
            max-height: 240px;
            height: auto;
            display: inline-block;
            border-radius: 0.5rem;
            background: #ffffff;
            padding: 3px;
            margin: 4px 0;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
        }
        .prose img {
            max-width: 100%;
            max-height: 320px;
            height: auto;
            display: inline-block;
            border-radius: 0.5rem;
            background: #ffffff;
            padding: 4px;
            margin: 6px 0;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
        }
        .ql-snow .ql-stroke {
            stroke: #94a3b8 !important;
        }
        .ql-snow .ql-fill {
            fill: #94a3b8 !important;
        }
        .ql-snow .ql-picker {
            color: #94a3b8 !important;
            font-size: 0.75rem !important;
        }
        .ql-snow .ql-picker-label {
            border: none !important;
            outline: none !important;
        }
        .ql-snow .ql-picker-options {
            background-color: #0f172a !important;
            border-color: #334155 !important;
            color: #f1f5f9 !important;
            border-radius: 0.5rem;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
            padding: 4px;
        }
        .ql-snow .ql-picker-item:hover,
        .ql-snow .ql-picker-item.ql-selected {
            color: #818cf8 !important;
        }
        .ql-snow button:hover,
        .ql-snow button.ql-active {
            background-color: #1e293b !important;
            border-radius: 0.375rem;
        }
        .ql-snow button:hover .ql-stroke,
        .ql-snow button.ql-active .ql-stroke {
            stroke: #818cf8 !important;
        }
        .ql-snow button:hover .ql-fill,
        .ql-snow button.ql-active .ql-fill {
            fill: #818cf8 !important;
        }
        .ql-editor.ql-blank::before {
            color: #64748b !important;
            font-style: normal;
        }
        .ql-snow .ql-tooltip {
            background-color: #0f172a !important;
            border-color: #334155 !important;
            color: #f1f5f9 !important;
            border-radius: 0.5rem;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
        }
        .ql-snow .ql-tooltip input[type=text] {
            background-color: #020617 !important;
            border-color: #334155 !important;
            color: #f1f5f9 !important;
            border-radius: 0.375rem;
            padding: 4px 8px !important;
        }
        /* KaTeX formula font & color */
        .katex {
            color: #f1f5f9 !important;
            font-size: 1.05em !important;
        }
        .ql-snow .ql-tooltip[data-mode="formula"]::before {
            content: "Enter LaTeX formula (e.g. \\sqrt{x}, \\frac{a}{b}, x^2):" !important;
            color: #94a3b8;
            font-size: 0.75rem;
            display: block;
            margin-bottom: 4px;
        }
        .ql-snow .ql-tooltip a.ql-action::after {
            content: 'Insert' !important;
            border-right: none !important;
            padding: 2px 8px;
            background-color: #4f46e5;
            color: #ffffff;
            border-radius: 4px;
            font-size: 11px;
            font-weight: 600;
        }
        .ql-snow .ql-tooltip a.ql-remove::after {
            content: 'Cancel' !important;
            padding: 2px 6px;
            color: #94a3b8;
            font-size: 11px;
        }
        /* Custom scrollbar for math symbol grids */
        .scrollbar-thin::-webkit-scrollbar {
            height: 4px;
            width: 4px;
        }
        .scrollbar-thin::-webkit-scrollbar-thumb {
            background-color: #334155;
            border-radius: 9999px;
        }
    </style>

    <div class="py-8 w-full px-4 sm:px-6 lg:px-8 space-y-8">
        
        <!-- Header Banner -->
        <div class="relative overflow-hidden rounded-2xl bg-gradient-to-r from-indigo-950 via-slate-900 to-slate-900 border border-indigo-500/30 p-6 sm:p-8 shadow-2xl">
            <div class="relative z-10 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-6">
                <div>
                    <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-indigo-500/20 border border-indigo-500/40 text-indigo-300 text-xs font-semibold uppercase tracking-wider mb-3">
                        <span class="w-2 h-2 rounded-full bg-indigo-400 animate-pulse"></span>
                        <span>Question Bank</span>
                    </div>
                    <h1 class="text-3xl font-extrabold text-white tracking-tight sm:text-4xl">
                        Questions & Answers Management
                    </h1>
                    <p class="mt-2 text-slate-300 text-sm max-w-xl">
                        Create, search, and manage questions classified by Standard, Subject, Chapter, and Topic.
                    </p>
                </div>

                <div class="flex items-center gap-3">
                    <a href="{{ route('dashboard') }}" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium text-sm transition-all flex items-center space-x-2">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
                        </svg>
                        <span>Back to Dashboard</span>
                    </a>

                    <button onclick="openCreateQuestionModal()" class="px-5 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-sm transition-all shadow-lg shadow-indigo-600/30 flex items-center space-x-2 cursor-pointer">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
                        </svg>
                        <span>Add Question</span>
                    </button>
                </div>
            </div>
        </div>

        <!-- Search & Filter Section (Mobile App Optimized) -->
        <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-xl space-y-3">
            @php
                $activeFiltersCount = collect(['search', 'type', 'created_by', 'syllabus_id', 'standard_id', 'subject_id', 'chapter_id', 'topic_id'])
                    ->filter(fn($field) => request()->filled($field))
                    ->count();

                $hasDrawerFiltersActive = request()->anyFilled(['type', 'syllabus_id', 'standard_id', 'subject_id', 'chapter_id', 'topic_id']);
            @endphp

            <!-- App Bar Header -->
            <div class="flex items-center justify-between gap-2">
                <div class="flex items-center space-x-2 min-w-0">
                    <div class="w-8 h-8 rounded-xl bg-indigo-500/20 border border-indigo-500/30 flex items-center justify-center shrink-0 text-indigo-400">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z"/></svg>
                    </div>
                    <div class="min-w-0">
                        <h3 class="text-sm sm:text-base font-bold text-white truncate flex items-center gap-1.5">
                            <span>Search & Filters</span>
                            @if($activeFiltersCount > 0)
                                <span class="px-2 py-0.5 rounded-full text-[10px] font-extrabold bg-indigo-500/25 text-indigo-300 border border-indigo-500/40">
                                    {{ $activeFiltersCount }} active
                                </span>
                            @endif
                        </h3>
                    </div>
                </div>

                <div class="flex items-center space-x-2 shrink-0">
                    @if(request()->anyFilled(['search', 'type', 'created_by', 'syllabus_id', 'standard_id', 'subject_id', 'chapter_id', 'topic_id']))
                        <a href="{{ route('questions.index') }}" class="text-xs text-amber-400 hover:text-amber-300 font-semibold underline flex items-center space-x-1 cursor-pointer">
                            <span>Clear All</span>
                        </a>
                    @endif
                    <!-- Mobile Filter Toggle Button -->
                    <button type="button" onclick="toggleFilterDrawer()" class="md:hidden inline-flex items-center space-x-1.5 px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-semibold transition-all cursor-pointer active:scale-95 shadow-sm">
                        <svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"/></svg>
                        <span id="filterToggleBtnText">{{ $hasDrawerFiltersActive ? 'Filters' : 'Filters' }}</span>
                        @if($activeFiltersCount > 0)
                            <span class="w-4 h-4 rounded-full bg-indigo-600 text-white text-[10px] font-black flex items-center justify-center">{{ $activeFiltersCount }}</span>
                        @endif
                        <svg id="filterDrawerChevron" class="w-3.5 h-3.5 text-slate-400 transition-transform duration-200 {{ $hasDrawerFiltersActive ? 'rotate-180' : '' }}" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
                    </button>
                </div>
            </div>

            <form id="questionFilterForm" method="GET" action="{{ route('questions.index') }}" class="space-y-3">
                <!-- Mobile App Search Bar -->
                <div class="flex items-center gap-2">
                    <div class="relative flex-1">
                        <div class="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-slate-400">
                            <svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                        </div>
                        <input type="text" id="filter_search" name="search" value="{{ request('search') }}" placeholder="Search questions, syllabus (e.g. CBSE, SCERT), formulas, options, ID..." class="w-full pl-10 pr-9 py-2.5 sm:py-2 rounded-xl bg-slate-950 border border-slate-800 text-slate-100 placeholder-slate-500 text-xs sm:text-sm focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 shadow-inner transition-colors">
                        @if(request('search'))
                            <a href="{{ request()->fullUrlWithQuery(['search' => null, 'page' => null]) }}" class="absolute inset-y-0 right-0 pr-3 flex items-center text-slate-400 hover:text-slate-200" title="Clear search text">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                            </a>
                        @endif
                    </div>

                    <button type="submit" id="apply_filter_btn" class="shrink-0 px-4 py-2.5 sm:py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs sm:text-sm shadow-md shadow-indigo-600/30 transition-all cursor-pointer flex items-center space-x-1.5 active:scale-95">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                        <span class="hidden sm:inline">Search</span>
                    </button>
                </div>

                <!-- Filter Dropdowns Container (Desktop: always visible grid; Mobile: collapsible drawer) -->
                <div id="filterDrawerContent" class="{{ $hasDrawerFiltersActive ? 'block' : 'hidden' }} md:block pt-1">
                    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6 gap-3 pt-3 border-t border-slate-800/80">
                        <!-- Syllabus Filter -->
                        <div>
                            <label for="filter_syllabus" class="block text-[10px] font-bold text-slate-400 uppercase tracking-wider mb-1">Syllabus</label>
                            <select id="filter_syllabus" name="syllabus_id" onchange="filterStandardsBySyllabus('filter', this.value)" class="w-full px-3 py-2.5 sm:py-2 rounded-xl bg-slate-950 border border-slate-800 text-slate-200 text-xs focus:outline-none focus:border-indigo-500">
                                <option value="">All Syllabuses</option>
                                @foreach($syllabuses as $syl)
                                    <option value="{{ $syl->id }}" {{ request('syllabus_id') == $syl->id ? 'selected' : '' }}>{{ $syl->name }}</option>
                                @endforeach
                            </select>
                        </div>

                        <!-- Question Type Filter -->
                        <div>
                            <label for="filter_type" class="block text-[10px] font-bold text-slate-400 uppercase tracking-wider mb-1">Question Type</label>
                            <select id="filter_type" name="type" class="w-full px-3 py-2.5 sm:py-2 rounded-xl bg-slate-950 border border-slate-800 text-slate-200 text-xs focus:outline-none focus:border-indigo-500">
                                <option value="">All Question Types</option>
                                <option value="1" {{ request('type') == '1' ? 'selected' : '' }}>Single Option</option>
                                <option value="2" {{ request('type') == '2' ? 'selected' : '' }}>Multiple Option</option>
                                <option value="3" {{ request('type') == '3' ? 'selected' : '' }}>Text Entry</option>
                                <option value="4" {{ request('type') == '4' ? 'selected' : '' }}>True / False</option>
                                <option value="5" {{ request('type') == '5' ? 'selected' : '' }}>Match the Following</option>
                            </select>
                        </div>

                        <!-- Standard Filter -->
                        <div>
                            <label for="filter_standard" class="block text-[10px] font-bold text-slate-400 uppercase tracking-wider mb-1">Standard / Class</label>
                            <select id="filter_standard" name="standard_id" class="w-full px-3 py-2.5 sm:py-2 rounded-xl bg-slate-950 border border-slate-800 text-slate-200 text-xs focus:outline-none focus:border-indigo-500">
                                <option value="">All Standards</option>
                                @foreach($standards as $std)
                                    <option value="{{ $std->id }}" {{ request('standard_id') == $std->id ? 'selected' : '' }}>{{ $std->name }}</option>
                                @endforeach
                            </select>
                        </div>

                        <!-- Subject Filter -->
                        <div>
                            <label for="filter_subject" class="block text-[10px] font-bold text-slate-400 uppercase tracking-wider mb-1">Subject</label>
                            <select id="filter_subject" name="subject_id" onchange="filterChapters('filter', this.value)" class="w-full px-3 py-2.5 sm:py-2 rounded-xl bg-slate-950 border border-slate-800 text-slate-200 text-xs focus:outline-none focus:border-indigo-500">
                                <option value="">All Subjects</option>
                                @foreach($subjects as $sbj)
                                    <option value="{{ $sbj->id }}" {{ request('subject_id') == $sbj->id ? 'selected' : '' }}>{{ $sbj->name }}</option>
                                @endforeach
                            </select>
                        </div>

                        <!-- Chapter Filter -->
                        <div>
                            <label for="filter_chapter" class="block text-[10px] font-bold text-slate-400 uppercase tracking-wider mb-1">Chapter</label>
                            <select id="filter_chapter" name="chapter_id" onchange="filterTopics('filter', this.value)" class="w-full px-3 py-2.5 sm:py-2 rounded-xl bg-slate-950 border border-slate-800 text-slate-200 text-xs focus:outline-none focus:border-indigo-500">
                                <option value="">All Chapters</option>
                                @foreach($chapters as $ch)
                                    <option value="{{ $ch->id }}" {{ request('chapter_id') == $ch->id ? 'selected' : '' }}>{{ $ch->name }}</option>
                                @endforeach
                            </select>
                        </div>

                        <!-- Topic Filter -->
                        <div>
                            <label for="filter_topic" class="block text-[10px] font-bold text-slate-400 uppercase tracking-wider mb-1">Topic</label>
                            <select id="filter_topic" name="topic_id" class="w-full px-3 py-2.5 sm:py-2 rounded-xl bg-slate-950 border border-slate-800 text-slate-200 text-xs focus:outline-none focus:border-indigo-500">
                                <option value="">All Topics</option>
                                @foreach($topics as $tp)
                                    <option value="{{ $tp->id }}" {{ request('topic_id') == $tp->id ? 'selected' : '' }}>{{ $tp->name }}</option>
                                @endforeach
                            </select>
                        </div>

                        <!-- Action Buttons inside Drawer -->
                        <div class="col-span-full flex items-center justify-end space-x-2 pt-2 border-t border-slate-800/80">
                            @if(request()->anyFilled(['search', 'type', 'created_by', 'syllabus_id', 'standard_id', 'subject_id', 'chapter_id', 'topic_id']))
                                <a href="{{ route('questions.index') }}" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold transition-colors flex items-center space-x-1.5 cursor-pointer">
                                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                                    <span>Reset</span>
                                </a>
                            @endif
                            <button type="submit" class="w-full sm:w-auto px-5 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs shadow-md shadow-indigo-600/30 transition-all cursor-pointer flex items-center justify-center space-x-1.5 active:scale-95">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z"/></svg>
                                <span>Apply Filters</span>
                            </button>
                        </div>
                    </div>
                </div>
            </form>

            <!-- Active Filter Chips Bar (Mobile App Style Scrollable/Wrapping Pills) -->
            @if(request()->anyFilled(['search', 'type', 'created_by', 'syllabus_id', 'standard_id', 'subject_id', 'chapter_id', 'topic_id']))
                @php
                    $typeName = match((int) request('type')) {
                        1 => 'Single Option',
                        2 => 'Multiple Option',
                        3 => 'Text Entry',
                        4 => 'True / False',
                        5 => 'Match Following',
                        default => null,
                    };
                    $sylObj = $syllabuses->firstWhere('id', request('syllabus_id'));
                    $stdObj = $standards->firstWhere('id', request('standard_id'));
                    $sbjObj = $subjects->firstWhere('id', request('subject_id'));
                    $chObj = $chapters->firstWhere('id', request('chapter_id'));
                    $tpObj = $topics->firstWhere('id', request('topic_id'));
                @endphp
                <div class="flex items-center gap-1.5 overflow-x-auto py-1 scrollbar-thin text-xs">
                    <span class="text-[11px] font-semibold text-slate-400 shrink-0 uppercase tracking-wider">Filtered by:</span>
                    
                    @if(request()->filled('search'))
                        <a href="{{ request()->fullUrlWithQuery(['search' => null, 'page' => null]) }}" class="inline-flex items-center space-x-1 px-2.5 py-1 rounded-full bg-indigo-500/15 text-indigo-300 border border-indigo-500/30 hover:bg-indigo-500/25 transition-colors shrink-0" title="Remove search filter">
                            <span>🔍 "{{ Str::limit(request('search'), 18) }}"</span>
                            <svg class="w-3 h-3 text-indigo-300 hover:text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                        </a>
                    @endif

                    @if($sylObj)
                        <a href="{{ request()->fullUrlWithQuery(['syllabus_id' => null, 'page' => null]) }}" class="inline-flex items-center space-x-1 px-2.5 py-1 rounded-full bg-pink-500/15 text-pink-300 border border-pink-500/30 hover:bg-pink-500/25 transition-colors shrink-0" title="Remove syllabus filter">
                            <span>🏛️ Syllabus: {{ $sylObj->name }}</span>
                            <svg class="w-3 h-3 text-pink-300 hover:text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                        </a>
                    @endif

                    @if($typeName)
                        <a href="{{ request()->fullUrlWithQuery(['type' => null, 'page' => null]) }}" class="inline-flex items-center space-x-1 px-2.5 py-1 rounded-full bg-cyan-500/15 text-cyan-300 border border-cyan-500/30 hover:bg-cyan-500/25 transition-colors shrink-0" title="Remove type filter">
                            <span>Type: {{ $typeName }}</span>
                            <svg class="w-3 h-3 text-cyan-300 hover:text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                        </a>
                    @endif

                    @if($stdObj)
                        <a href="{{ request()->fullUrlWithQuery(['standard_id' => null, 'page' => null]) }}" class="inline-flex items-center space-x-1 px-2.5 py-1 rounded-full bg-violet-500/15 text-violet-300 border border-violet-500/30 hover:bg-violet-500/25 transition-colors shrink-0" title="Remove standard filter">
                            <span>Class: {{ $stdObj->name }}</span>
                            <svg class="w-3 h-3 text-violet-300 hover:text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                        </a>
                    @endif

                    @if($sbjObj)
                        <a href="{{ request()->fullUrlWithQuery(['subject_id' => null, 'chapter_id' => null, 'topic_id' => null, 'page' => null]) }}" class="inline-flex items-center space-x-1 px-2.5 py-1 rounded-full bg-amber-500/15 text-amber-300 border border-amber-500/30 hover:bg-amber-500/25 transition-colors shrink-0" title="Remove subject filter">
                            <span>Subject: {{ $sbjObj->name }}</span>
                            <svg class="w-3 h-3 text-amber-300 hover:text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                        </a>
                    @endif

                    @if($chObj)
                        <a href="{{ request()->fullUrlWithQuery(['chapter_id' => null, 'topic_id' => null, 'page' => null]) }}" class="inline-flex items-center space-x-1 px-2.5 py-1 rounded-full bg-blue-500/15 text-blue-300 border border-blue-500/30 hover:bg-blue-500/25 transition-colors shrink-0" title="Remove chapter filter">
                            <span>Chapter: {{ Str::limit($chObj->name, 16) }}</span>
                            <svg class="w-3 h-3 text-blue-300 hover:text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                        </a>
                    @endif

                    @if($tpObj)
                        <a href="{{ request()->fullUrlWithQuery(['topic_id' => null, 'page' => null]) }}" class="inline-flex items-center space-x-1 px-2.5 py-1 rounded-full bg-emerald-500/15 text-emerald-300 border border-emerald-500/30 hover:bg-emerald-500/25 transition-colors shrink-0" title="Remove topic filter">
                            <span>Topic: {{ Str::limit($tpObj->name, 16) }}</span>
                            <svg class="w-3 h-3 text-emerald-300 hover:text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                        </a>
                    @endif

                    <a href="{{ route('questions.index') }}" class="inline-flex items-center px-2 py-0.5 rounded-full bg-rose-500/10 text-rose-300 border border-rose-500/30 hover:bg-rose-500/20 text-[11px] font-semibold transition-colors shrink-0">
                        Clear All
                    </a>
                </div>
            @endif
        </div>

        <!-- Questions Listing Directory (Responsive Table + Mobile App Cards) -->
        <div class="bg-slate-900 border border-slate-800 rounded-2xl shadow-xl overflow-hidden">
            <div class="px-4 py-4 sm:px-6 sm:py-5 border-b border-slate-800 flex items-center justify-between">
                <div>
                    <h3 class="text-base sm:text-lg font-bold text-white">Question Directory</h3>
                    <p class="text-xs text-slate-400 hidden sm:block">Browse and manage questions with instant answers and status</p>
                </div>
                <span class="text-xs font-semibold text-slate-300 bg-slate-800 px-3 py-1 rounded-full border border-slate-700">
                    Total: {{ $questions->total() }}
                </span>
            </div>

            <!-- MOBILE APP CARDS VIEW (visible on mobile, hidden on desktop) -->
            <div class="block md:hidden divide-y divide-slate-800">
                @forelse ($questions as $q)
                    @php
                        $qPayload = [
                            'id' => $q->id,
                            'name' => $q->name,
                            'description' => $q->description ?? '',
                            'hint' => $q->hint ?? '',
                            'solution' => $q->solution ?? '',
                            'syllabus_id' => $q->standard?->syllabus_id ?? $q->subject?->syllabus_id,
                            'syllabus_name' => $q->standard?->syllabus?->name ?? $q->subject?->syllabus?->name ?? 'CBSE',
                            'standard_id' => $q->standard_id,
                            'standard_name' => $q->standard?->name ?? 'Unassigned Class',
                            'subject_id' => $q->subject_id,
                            'subject_name' => $q->subject?->name ?? 'Unassigned Subject',
                            'chapter_id' => $q->chapter_id,
                            'chapter_name' => $q->chapter?->name ?? 'Unassigned Chapter',
                            'topic_id' => $q->topic_id,
                            'topic_name' => $q->topic?->name ?? 'Unassigned Topic',
                            'type' => $q->type,
                            'marks' => $q->marks,
                            'creator_name' => $q->creator?->name ?? 'System',
                            'created_at' => $q->created_at?->format('M d, Y h:i A') ?? 'N/A',
                            'status' => $q->status ?? 1,
                            'answers' => $q->answers->map(fn($a) => [
                                'id' => $a->id,
                                'name' => $a->name,
                                'match_answer' => $a->match_answer,
                                'is_correct' => $a->is_correct,
                            ])->toArray(),
                        ];
                    @endphp
                    <div class="p-4 space-y-3 hover:bg-slate-800/30 transition-colors">
                        <!-- Top Header: ID, Type Badge, Marks -->
                        <div class="flex items-center justify-between gap-2">
                            <div class="flex items-center space-x-2">
                                <span class="px-2 py-0.5 rounded-md text-[11px] font-mono font-bold bg-slate-800 text-slate-300 border border-slate-700">
                                    #{{ $q->id }}
                                </span>
                                @if($q->type == 1)
                                    <span class="inline-flex items-center px-2 py-0.5 rounded-full text-[11px] font-semibold bg-indigo-500/15 text-indigo-300 border border-indigo-500/30">Single Option</span>
                                @elseif($q->type == 2)
                                    <span class="inline-flex items-center px-2 py-0.5 rounded-full text-[11px] font-semibold bg-violet-500/15 text-violet-300 border border-violet-500/30">Multiple Option</span>
                                @elseif($q->type == 4)
                                    <span class="inline-flex items-center px-2 py-0.5 rounded-full text-[11px] font-semibold bg-emerald-500/15 text-emerald-300 border border-emerald-500/30">True / False</span>
                                @elseif($q->type == 5)
                                    <span class="inline-flex items-center px-2 py-0.5 rounded-full text-[11px] font-semibold bg-cyan-500/15 text-cyan-300 border border-cyan-500/30">Match Following</span>
                                @else
                                    <span class="inline-flex items-center px-2 py-0.5 rounded-full text-[11px] font-semibold bg-amber-500/15 text-amber-300 border border-amber-500/30">Text Entry</span>
                                @endif
                            </div>

                            <span class="px-2.5 py-0.5 rounded-lg text-xs font-bold bg-indigo-600/20 text-indigo-300 border border-indigo-500/30 shrink-0">
                                {{ $q->marks }} {{ Str::plural('mark', $q->marks) }}
                            </span>
                        </div>

                        <!-- Question Prompt Body -->
                        <div onclick="openViewQuestionModal({{ json_encode($qPayload) }})" class="text-sm text-white font-medium prose prose-invert max-w-none break-words leading-relaxed cursor-pointer hover:text-indigo-300 transition-colors" title="Click to view full question details">
                            {!! $q->name !!}
                        </div>

                        @if($q->description)
                            <p class="text-xs text-slate-400 italic">{{ $q->description }}</p>
                        @endif

                        <!-- Hint & Solution Badges (if present) -->
                        @if($q->hint || $q->solution)
                            <div class="flex items-center gap-1.5 flex-wrap pt-0.5">
                                @if($q->hint)
                                    <span class="inline-flex items-center px-2 py-0.5 rounded-md text-[10px] font-bold bg-amber-500/15 text-amber-300 border border-amber-500/30">
                                        💡 Hint: {{ Str::limit($q->hint, 60) }}
                                    </span>
                                @endif
                                @if($q->solution)
                                    <span class="inline-flex items-center px-2 py-0.5 rounded-md text-[10px] font-bold bg-emerald-500/15 text-emerald-300 border border-emerald-500/30">
                                        📝 Solution: {{ Str::limit($q->solution, 60) }}
                                    </span>
                                @endif
                            </div>
                        @endif

                        <!-- Answers Preview for Mobile -->
                        @if($q->type == 5)
                            <div class="bg-slate-950/70 p-2.5 rounded-xl border border-slate-800/80 space-y-1 text-xs">
                                <span class="text-[10px] font-bold text-slate-400 uppercase tracking-wider block mb-1">Matching Pairs:</span>
                                @foreach($q->answers as $idx => $ans)
                                    <div class="flex items-center justify-between text-xs py-0.5 border-b border-slate-800/40 last:border-0">
                                        <span class="text-cyan-300 font-medium truncate max-w-[45%]"><strong class="text-cyan-400">{{ chr(65 + $idx) }}.</strong> {{ $ans->name }}</span>
                                        <span class="text-slate-500">&harr;</span>
                                        <span class="text-emerald-300 font-medium truncate max-w-[45%]">{{ $ans->match_answer }}</span>
                                    </div>
                                @endforeach
                            </div>
                        @elseif($q->answers->isNotEmpty() && $q->type != 3)
                            <div class="bg-slate-950/70 p-2.5 rounded-xl border border-slate-800/80 space-y-1 text-xs">
                                <span class="text-[10px] font-bold text-slate-400 uppercase tracking-wider block mb-1">Options:</span>
                                @foreach($q->answers as $ans)
                                    <div class="flex items-center space-x-2 py-0.5">
                                        <span class="w-2 h-2 rounded-full shrink-0 {{ $ans->is_correct == 1 ? 'bg-emerald-400' : 'bg-slate-600' }}"></span>
                                        <span class="{{ $ans->is_correct == 1 ? 'text-emerald-300 font-semibold' : 'text-slate-400' }} truncate">{{ $ans->name }}</span>
                                        @if($ans->is_correct == 1)
                                            <span class="text-[9px] text-emerald-400 font-bold uppercase">(✓)</span>
                                        @endif
                                    </div>
                                @endforeach
                            </div>
                        @endif

                        <!-- Classification Tags -->
                        <div class="flex items-center gap-1.5 flex-wrap text-[11px] text-slate-400">
                            <span class="px-2 py-0.5 rounded bg-pink-500/10 text-pink-300 border border-pink-500/20 font-medium">
                                🏛️ {{ $q->standard?->syllabus?->name ?? $q->subject?->syllabus?->name ?? 'CBSE' }}
                            </span>
                            <span class="px-2 py-0.5 rounded bg-slate-800 text-slate-300 border border-slate-700 font-medium">
                                {{ $q->standard?->name ?? 'Standard' }}
                            </span>
                            @if($q->subject)
                                <span class="px-2 py-0.5 rounded bg-indigo-500/10 text-indigo-300 border border-indigo-500/20 font-medium">
                                    📚 {{ $q->subject->name }}
                                </span>
                            @endif
                            @if($q->chapter)
                                <span class="px-2 py-0.5 rounded bg-slate-800/80 text-slate-300 border border-slate-700">
                                    📖 {{ $q->chapter->name }}
                                </span>
                            @endif
                            @if($q->topic)
                                <span class="px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                                    🏷️ {{ $q->topic->name }}
                                </span>
                            @endif
                        </div>

                        <!-- Footer: Creator & Action Buttons -->
                        <div class="pt-2 flex items-center justify-between border-t border-slate-800/60">
                            <span class="text-[11px] text-slate-500">By {{ $q->creator?->name ?? 'Teacher' }}</span>
                            <div class="flex items-center space-x-2">
                                <button type="button" onclick="openViewQuestionModal({{ json_encode($qPayload) }})" class="px-3 py-1.5 rounded-xl bg-indigo-600/20 hover:bg-indigo-600/30 text-indigo-300 text-xs font-semibold border border-indigo-500/30 transition-colors inline-flex items-center space-x-1 cursor-pointer active:scale-95">
                                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                                    <span>View</span>
                                </button>
                                <button onclick="openEditQuestionModal({{ json_encode($qPayload) }})" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-indigo-300 text-xs font-semibold border border-slate-700 transition-colors inline-flex items-center space-x-1 cursor-pointer active:scale-95">
                                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/></svg>
                                    <span>Edit</span>
                                </button>

                                <form method="POST" action="{{ route('questions.destroy', $q) }}" class="inline" onsubmit="return confirm('Are you sure you want to delete this question?')">
                                    @csrf
                                    @method('DELETE')
                                    <button type="submit" class="px-3.5 py-1.5 rounded-xl bg-red-950/60 hover:bg-red-900/60 text-red-300 text-xs font-semibold border border-red-800/40 transition-colors inline-flex items-center space-x-1 cursor-pointer active:scale-95">
                                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/></svg>
                                        <span>Delete</span>
                                    </button>
                                </form>
                            </div>
                        </div>
                    </div>
                @empty
                    <div class="p-8 text-center text-slate-500 text-sm">
                        No questions matching your search filters. Try adjusting your filters or click "Add Question" to create one.
                    </div>
                @endforelse
            </div>

            <!-- DESKTOP TABLE VIEW (visible on desktop md+, hidden on mobile) -->
            <div class="hidden md:block overflow-x-auto">
                <table class="w-full text-left border-collapse text-sm">
                    <thead>
                        <tr class="bg-slate-950/60 border-b border-slate-800 text-slate-400 uppercase text-[11px] font-semibold tracking-wider">
                            <th class="py-3.5 px-6">Question Name</th>
                            <th class="py-3.5 px-6">Standard</th>
                            <th class="py-3.5 px-6">Subject & Chapter</th>
                            <th class="py-3.5 px-6">Topic</th>
                            <th class="py-3.5 px-6">Type</th>
                            <th class="py-3.5 px-6">Marks</th>
                            <th class="py-3.5 px-6">Answers Options</th>
                            <th class="py-3.5 px-6">Created By</th>
                            <th class="py-3.5 px-6 text-right">Actions</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800/60 text-slate-300">
                        @forelse ($questions as $q)
                            @php
                                $qPayload = [
                                    'id' => $q->id,
                                    'name' => $q->name,
                                    'description' => $q->description ?? '',
                                    'hint' => $q->hint ?? '',
                                    'solution' => $q->solution ?? '',
                                    'syllabus_id' => $q->standard?->syllabus_id ?? $q->subject?->syllabus_id,
                                    'syllabus_name' => $q->standard?->syllabus?->name ?? $q->subject?->syllabus?->name ?? 'CBSE',
                                    'standard_id' => $q->standard_id,
                                    'standard_name' => $q->standard?->name ?? 'Unassigned Class',
                                    'subject_id' => $q->subject_id,
                                    'subject_name' => $q->subject?->name ?? 'Unassigned Subject',
                                    'chapter_id' => $q->chapter_id,
                                    'chapter_name' => $q->chapter?->name ?? 'Unassigned Chapter',
                                    'topic_id' => $q->topic_id,
                                    'topic_name' => $q->topic?->name ?? 'Unassigned Topic',
                                    'type' => $q->type,
                                    'marks' => $q->marks,
                                    'creator_name' => $q->creator?->name ?? 'System',
                                    'created_at' => $q->created_at?->format('M d, Y h:i A') ?? 'N/A',
                                    'status' => $q->status ?? 1,
                                    'answers' => $q->answers->map(fn($a) => [
                                        'id' => $a->id,
                                        'name' => $a->name,
                                        'match_answer' => $a->match_answer,
                                        'is_correct' => $a->is_correct,
                                    ])->toArray(),
                                ];
                            @endphp
                            <tr class="hover:bg-slate-800/40 transition-colors">
                                <td class="py-4 px-6 max-w-xs">
                                    <div onclick="openViewQuestionModal({{ json_encode($qPayload) }})" class="font-medium text-white line-clamp-3 max-w-md prose prose-invert prose-sm break-words cursor-pointer hover:text-indigo-300 transition-colors" title="Click to view full question details">{!! $q->name !!}</div>
                                    @if($q->description)
                                        <div class="text-xs text-slate-400 mt-0.5 line-clamp-1" title="{{ $q->description }}">{{ $q->description }}</div>
                                    @endif
                                    @if($q->hint || $q->solution)
                                        <div class="flex items-center gap-1.5 mt-1.5 flex-wrap">
                                            @if($q->hint)
                                                <span class="inline-flex items-center px-1.5 py-0.5 rounded text-[10px] font-bold bg-amber-500/15 text-amber-300 border border-amber-500/30" title="Hint: {{ Str::limit($q->hint, 80) }}">
                                                    💡 Hint
                                                </span>
                                            @endif
                                            @if($q->solution)
                                                <span class="inline-flex items-center px-1.5 py-0.5 rounded text-[10px] font-bold bg-emerald-500/15 text-emerald-300 border border-emerald-500/30" title="Solution: {{ Str::limit($q->solution, 80) }}">
                                                    📝 Solution
                                                </span>
                                            @endif
                                        </div>
                                    @endif
                                </td>
                                <td class="py-4 px-6">
                                    <div class="flex flex-col items-start gap-1">
                                        <span class="inline-flex items-center px-2.5 py-0.5 rounded-md text-xs font-medium bg-slate-800 text-slate-200 border border-slate-700">
                                            {{ $q->standard?->name ?? 'N/A' }}
                                        </span>
                                        <span class="inline-flex items-center px-1.5 py-0.5 rounded text-[10px] font-semibold bg-pink-500/10 text-pink-300 border border-pink-500/20">
                                            🏛️ {{ $q->standard?->syllabus?->name ?? $q->subject?->syllabus?->name ?? 'CBSE' }}
                                        </span>
                                    </div>
                                </td>
                                <td class="py-4 px-6">
                                    <div class="flex flex-col space-y-1">
                                        @if($q->subject)
                                            <span class="inline-flex items-center px-2 py-0.5 rounded text-[11px] font-bold bg-indigo-500/10 text-indigo-300 border border-indigo-500/20 w-max">
                                                📚 {{ $q->subject->name }}
                                            </span>
                                        @else
                                            <span class="text-xs text-slate-500 italic">No Subject</span>
                                        @endif

                                        @if($q->chapter)
                                            <span class="text-xs text-slate-300 font-medium">
                                                📖 {{ $q->chapter->name }}
                                            </span>
                                        @endif
                                    </div>
                                </td>
                                <td class="py-4 px-6">
                                    @if($q->topic)
                                        <span class="inline-flex items-center px-2 py-0.5 rounded text-[11px] font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                                            🏷️ {{ $q->topic->name }}
                                        </span>
                                    @else
                                        <span class="text-xs text-slate-500 italic">No Topic</span>
                                    @endif
                                </td>
                                <td class="py-4 px-6">
                                    @if($q->type == 1)
                                        <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold bg-indigo-500/10 text-indigo-400 border border-indigo-500/20">Single Option</span>
                                    @elseif($q->type == 2)
                                        <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold bg-violet-500/10 text-violet-400 border border-violet-500/20">Multiple Option</span>
                                    @elseif($q->type == 4)
                                        <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">True / False</span>
                                    @elseif($q->type == 5)
                                        <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold bg-cyan-500/10 text-cyan-400 border border-cyan-500/20">Match the Following</span>
                                    @else
                                        <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold bg-amber-500/10 text-amber-400 border border-amber-500/20">Text Entry</span>
                                    @endif
                                </td>
                                <td class="py-4 px-6 font-semibold text-indigo-300">
                                    {{ $q->marks }}
                                </td>
                                <td class="py-4 px-6">
                                    @if($q->type == 3)
                                        <span class="text-xs text-slate-500">N/A (Text Entry)</span>
                                    @elseif($q->type == 5)
                                        <div class="flex flex-col gap-1 max-w-xs text-xs">
                                            @foreach($q->answers as $idx => $ans)
                                                <div class="flex items-center space-x-1.5 text-slate-300">
                                                    <span class="text-cyan-400 font-bold shrink-0">{{ chr(65 + $idx) }}.</span>
                                                    <span class="text-slate-200 font-medium truncate max-w-[100px]">{{ $ans->name }}</span>
                                                    <span class="text-slate-500 shrink-0">&harr;</span>
                                                    <span class="text-emerald-400 font-semibold truncate max-w-[100px]">{{ $ans->match_answer }}</span>
                                                </div>
                                            @endforeach
                                        </div>
                                    @elseif($q->answers->isNotEmpty())
                                        <div class="flex flex-col gap-1 max-w-xs">
                                            @foreach($q->answers as $ans)
                                                <div class="text-xs flex items-center space-x-1.5">
                                                    <span class="w-2 h-2 rounded-full shrink-0 {{ $ans->is_correct == 1 ? 'bg-emerald-400' : 'bg-slate-600' }}"></span>
                                                    <span class="{{ $ans->is_correct == 1 ? 'text-emerald-300 font-medium' : 'text-slate-400' }} truncate">{{ $ans->name }}</span>
                                                    @if($ans->is_correct == 1)
                                                        <span class="text-[10px] text-emerald-400 font-bold uppercase">(Correct)</span>
                                                    @endif
                                                </div>
                                            @endforeach
                                        </div>
                                    @else
                                        <span class="text-xs text-slate-500">No options added</span>
                                    @endif
                                </td>
                                <td class="py-4 px-6 text-xs text-slate-400">
                                    {{ $q->creator?->name ?? 'System' }}
                                </td>
                                <td class="py-4 px-6 text-right whitespace-nowrap space-x-1.5">
                                    <button type="button" onclick="openViewQuestionModal({{ json_encode($qPayload) }})" class="px-2.5 py-1.5 rounded-lg bg-indigo-600/20 hover:bg-indigo-600/30 text-indigo-300 text-xs font-medium border border-indigo-500/30 transition-colors inline-flex items-center space-x-1 cursor-pointer" title="View Full Details">
                                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                                        <span>View</span>
                                    </button>

                                    <button onclick="openEditQuestionModal({{ json_encode($qPayload) }})" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-indigo-300 text-xs font-medium border border-slate-700 transition-colors inline-flex items-center space-x-1 cursor-pointer">
                                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/></svg>
                                        <span>Edit</span>
                                    </button>

                                    <form method="POST" action="{{ route('questions.destroy', $q) }}" class="inline" onsubmit="return confirm('Are you sure you want to delete this question?')">
                                        @csrf
                                        @method('DELETE')
                                        <button type="submit" class="px-3 py-1.5 rounded-lg bg-red-950/60 hover:bg-red-900/60 text-red-300 text-xs font-medium border border-red-800/40 transition-colors inline-flex items-center space-x-1 cursor-pointer">
                                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/></svg>
                                            <span>Delete</span>
                                        </button>
                                    </form>
                                </td>
                            </tr>
                        @empty
                            <tr>
                                <td colspan="9" class="py-8 text-center text-slate-500">
                                    No questions matching your search filters. Try adjusting your filters or click "Add Question" to create one.
                                </td>
                            </tr>
                        @endforelse
                    </tbody>
                </table>
            </div>

            @if($questions->hasPages())
                <div class="px-4 py-3 sm:px-6 sm:py-4 border-t border-slate-800">
                    {{ $questions->links() }}
                </div>
            @endif
        </div>

        <!-- CREATE QUESTION MODAL -->
        @php
            $isCreateModalOpen = $errors->any() && old('_method') !== 'PUT';
        @endphp
        <div id="createQuestionModal" class="{{ $isCreateModalOpen ? '' : 'hidden' }} fixed inset-0 z-50 bg-black/75 backdrop-blur-sm overflow-y-auto p-2 sm:p-4 flex justify-center items-start">
            <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-5xl max-h-[92vh] flex flex-col overflow-hidden shadow-2xl my-2 sm:my-3">
                <div class="px-5 py-3 border-b border-slate-800 flex items-center justify-between bg-slate-950/80 shrink-0">
                    <h3 class="text-base font-bold text-white flex items-center gap-2">
                        <svg class="w-5 h-5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                        <span>Add New Question</span>
                    </h3>
                    <button onclick="closeCreateQuestionModal()" class="text-slate-400 hover:text-white transition-colors cursor-pointer p-1">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                    </button>
                </div>

                <form id="createQuestionForm" method="POST" action="{{ route('questions.store') }}" class="flex flex-col flex-1 overflow-hidden">
                    @csrf
                    
                    <div class="p-4 sm:p-5 space-y-3 overflow-y-auto flex-1 scrollbar-thin">
                        @if ($isCreateModalOpen && $errors->any())
                            <div class="p-3 rounded-xl bg-red-950/80 border border-red-500/40 text-red-200 text-xs">
                                <span class="font-bold flex items-center gap-1 text-red-300">
                                    <svg class="w-4 h-4 inline" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                                    Validation errors occurred. Please check the fields below.
                                </span>
                            </div>
                        @endif

                        <!-- Question Name / Prompt (Rich Text Editor + Math Symbols) -->
                        <div>
                            <div class="flex items-center justify-between mb-1 flex-wrap gap-2">
                                <div class="flex items-center space-x-2 flex-wrap gap-y-1">
                                    <label class="block text-xs font-semibold text-slate-300 uppercase tracking-wider">
                                        Question Name / Prompt <span class="text-red-400">*</span>
                                    </label>
                                    <button type="button" onclick="toggleMathPalette('create')" class="inline-flex items-center space-x-1.5 px-2 py-0.5 rounded-lg bg-indigo-500/20 hover:bg-indigo-500/30 text-indigo-300 hover:text-indigo-200 border border-indigo-500/40 text-[11px] font-semibold transition-all cursor-pointer shadow-sm">
                                        <span class="text-xs font-bold font-serif leading-none">∑</span>
                                        <span>Math & 🧪 Chemistry Symbols</span>
                                    </button>
                                    <button type="button" onclick="openDrawToolModal('create')" class="inline-flex items-center space-x-1.5 px-2.5 py-0.5 rounded-lg bg-emerald-500/20 hover:bg-emerald-500/30 text-emerald-300 hover:text-emerald-200 border border-emerald-500/40 text-[11px] font-semibold transition-all cursor-pointer shadow-sm">
                                        <span class="text-xs">📐</span>
                                        <span>Draw Shapes & Geometry</span>
                                    </button>
                                </div>
                                <span class="text-[11px] text-slate-400 font-medium">Rich text, math & chemistry enabled</span>
                            </div>

                            <!-- Interactive Math Symbols & Formula Palette -->
                            <div id="create_math_palette" class="hidden mb-2 p-2.5 rounded-xl bg-slate-900 border border-indigo-500/40 shadow-xl space-y-2">
                                <div class="flex items-center justify-between gap-2 border-b border-slate-800 pb-1.5">
                                    <div class="flex items-center space-x-2 flex-1 min-w-0">
                                        <div class="relative w-44 shrink-0">
                                            <input type="text" id="create_math_search" oninput="filterMathSymbols('create', this.value)" placeholder="Search (H2O, eq, pi)..." class="w-full pl-7 pr-2 py-1 rounded-md bg-slate-950 border border-slate-700 text-slate-100 placeholder-slate-500 text-xs focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                            <svg class="w-3.5 h-3.5 text-slate-400 absolute left-2 top-1.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                                        </div>
                                        <div id="create_math_tabs" class="flex items-center space-x-1 overflow-x-auto text-xs py-0.5 scrollbar-thin">
                                            <button type="button" onclick="selectMathTab('create', 'all', this)" class="create-math-tab active px-2 py-0.5 rounded bg-indigo-600 text-white font-medium text-[11px] whitespace-nowrap">All</button>
                                            <button type="button" onclick="selectMathTab('create', 'chemistry', this)" class="create-math-tab px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium text-[11px] whitespace-nowrap">🧪 Chemistry (⇌,↑,↓,≡)</button>
                                            <button type="button" onclick="selectMathTab('create', 'compounds', this)" class="create-math-tab px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium text-[11px] whitespace-nowrap">Compounds (H₂O, CO₂)</button>
                                            <button type="button" onclick="selectMathTab('create', 'operators', this)" class="create-math-tab px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium text-[11px] whitespace-nowrap">Basic Math (±,×,≤)</button>
                                            <button type="button" onclick="selectMathTab('create', 'greek', this)" class="create-math-tab px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium text-[11px] whitespace-nowrap">Greek (π,θ,α)</button>
                                            <button type="button" onclick="selectMathTab('create', 'fractions', this)" class="create-math-tab px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium text-[11px] whitespace-nowrap">Roots & Powers (√,x²)</button>
                                            <button type="button" onclick="selectMathTab('create', 'calculus', this)" class="create-math-tab px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium text-[11px] whitespace-nowrap">Calculus (∫,∑,∂)</button>
                                            <button type="button" onclick="selectMathTab('create', 'geometry', this)" class="create-math-tab px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium text-[11px] whitespace-nowrap">Geometry (°,∠,⊥)</button>
                                            <button type="button" onclick="selectMathTab('create', 'formulas', this)" class="create-math-tab px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium text-[11px] whitespace-nowrap">Formulas & Reactions</button>
                                        </div>
                                    </div>
                                    <button type="button" onclick="toggleMathPalette('create')" class="p-1 rounded text-slate-400 hover:text-white hover:bg-slate-800" title="Close">
                                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                                    </button>
                                </div>
                                <div id="create_math_symbols_grid" class="flex flex-wrap gap-1 max-h-32 overflow-y-auto p-1.5 bg-slate-950/60 rounded-lg border border-slate-800/80">
                                    <!-- Populated dynamically by JS -->
                                </div>
                            </div>

                            <input type="hidden" id="create_q_name" name="name" value="{{ old('name') }}">
                            <div id="create_q_editor_container" class="rounded-xl overflow-hidden border border-slate-700 bg-slate-950 focus-within:ring-2 focus-within:ring-indigo-500 @error('name') border-red-500 ring-1 ring-red-500 @enderror">
                                <div id="create_q_editor"></div>
                            </div>
                            <p id="create_q_name_client_error" class="hidden mt-1 text-xs text-red-400">Please enter a question prompt.</p>
                            @error('name')
                                <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                            @enderror
                        </div>

                        <!-- Subject, Chapter, Topic Selection Grid -->
                        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5 p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                            <!-- Standard Select (Required) -->
                            <div>
                                <label for="create_q_standard" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Standard <span class="text-red-400">*</span></label>
                                <select id="create_q_standard" name="standard_id" required class="w-full px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-xs @error('standard_id') border-red-500 focus:ring-red-500 @enderror">
                                    <option value="" disabled {{ old('standard_id') ? '' : 'selected' }}>Select Standard</option>
                                    @foreach($standards as $std)
                                        <option value="{{ $std->id }}" {{ old('standard_id') == $std->id ? 'selected' : '' }}>{{ $std->name }}</option>
                                    @endforeach
                                </select>
                                @error('standard_id')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>

                            <!-- Subject Select (Optional) -->
                            <div>
                                <label for="create_subject" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Subject</label>
                                <select id="create_subject" name="subject_id" onchange="filterChapters('create', this.value)" class="w-full px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-xs @error('subject_id') border-red-500 focus:ring-red-500 @enderror">
                                    <option value="">Select Subject</option>
                                    @foreach($subjects as $sbj)
                                        <option value="{{ $sbj->id }}" {{ old('subject_id') == $sbj->id ? 'selected' : '' }}>{{ $sbj->name }}</option>
                                    @endforeach
                                </select>
                                @error('subject_id')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>

                            <!-- Chapter Select (Optional) -->
                            <div>
                                <label for="create_chapter" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Chapter</label>
                                <select id="create_chapter" name="chapter_id" onchange="filterTopics('create', this.value)" class="w-full px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-xs @error('chapter_id') border-red-500 focus:ring-red-500 @enderror">
                                    <option value="">Select Chapter</option>
                                    @foreach($chapters as $ch)
                                        <option value="{{ $ch->id }}" {{ old('chapter_id') == $ch->id ? 'selected' : '' }}>{{ $ch->name }}</option>
                                    @endforeach
                                </select>
                                @error('chapter_id')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>

                            <!-- Topic Select (Optional) -->
                            <div>
                                <label for="create_topic" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Topic</label>
                                <select id="create_topic" name="topic_id" class="w-full px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-xs @error('topic_id') border-red-500 focus:ring-red-500 @enderror">
                                    <option value="">Select Topic</option>
                                    @foreach($topics as $tp)
                                        <option value="{{ $tp->id }}" {{ old('topic_id') == $tp->id ? 'selected' : '' }}>{{ $tp->name }}</option>
                                    @endforeach
                                </select>
                                @error('topic_id')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>
                        </div>

                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
                            <!-- Type Select (Required) -->
                            <div>
                                <label for="create_q_type" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Question Type <span class="text-red-400">*</span></label>
                                <select id="create_q_type" name="type" required onchange="toggleAnswersSection('create', this.value)" class="w-full px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-xs @error('type') border-red-500 focus:ring-red-500 @enderror">
                                    <option value="1" {{ old('type', '1') == '1' ? 'selected' : '' }}>1 - Single Option</option>
                                    <option value="2" {{ old('type') == '2' ? 'selected' : '' }}>2 - Multiple Option</option>
                                    <option value="4" {{ old('type') == '4' ? 'selected' : '' }}>4 - True / False</option>
                                    <option value="5" {{ old('type') == '5' ? 'selected' : '' }}>5 - Match the Following</option>
                                    <option value="3" {{ old('type') == '3' ? 'selected' : '' }}>3 - Text Entry</option>
                                </select>
                                @error('type')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>

                            <!-- Marks (Required, Numbers Only) -->
                            <div>
                                <label for="create_q_marks" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Marks <span class="text-red-400">*</span></label>
                                <input type="number" id="create_q_marks" name="marks" required min="0" step="1" value="{{ old('marks', 1) }}" placeholder="1" class="w-full px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-xs @error('marks') border-red-500 focus:ring-red-500 @enderror">
                                <p id="create_marks_hint" class="mt-1 text-[11px] text-amber-300 font-medium hidden">Auto-calculated: 1 mark per valid matching pair (e.g. 4 pairs = 4 marks)</p>
                                @error('marks')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>
                        </div>

                        <!-- Description (Optional) -->
                        <div>
                            <label for="create_q_desc" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Description (Optional)</label>
                            <textarea id="create_q_desc" name="description" rows="1" placeholder="Additional explanation or context..." class="w-full px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-xs @error('description') border-red-500 focus:ring-red-500 @enderror">{{ old('description') }}</textarea>
                            @error('description')
                                <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                            @enderror
                        </div>

                        <!-- Hint / Solution (Optional) -->
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-1 border-t border-slate-800/60">
                            <!-- Hint (Optional) -->
                            <div>
                                <div class="flex items-center justify-between mb-1">
                                    <label for="create_q_hint" class="block text-xs font-semibold text-amber-300 uppercase tracking-wider flex items-center gap-1.5">
                                        <svg class="w-3.5 h-3.5 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/></svg>
                                        <span>Hint (Optional)</span>
                                    </label>
                                    <span class="text-[10px] text-slate-400">Shown in exam if clicked</span>
                                </div>
                                <textarea id="create_q_hint" name="hint" rows="2" placeholder="Provide a hint or clue to guide students during exam..." class="w-full px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-amber-500 text-xs @error('hint') border-red-500 focus:ring-red-500 @enderror">{{ old('hint') }}</textarea>
                                @error('hint')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>

                            <!-- Solution (Optional) -->
                            <div>
                                <div class="flex items-center justify-between mb-1">
                                    <label for="create_q_solution" class="block text-xs font-semibold text-emerald-300 uppercase tracking-wider flex items-center gap-1.5">
                                        <svg class="w-3.5 h-3.5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                                        <span>Solution / Explanation (Optional)</span>
                                    </label>
                                    <span class="text-[10px] text-slate-400">Full answer breakdown</span>
                                </div>
                                <textarea id="create_q_solution" name="solution" rows="2" placeholder="Provide complete solution / working for the question..." class="w-full px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-emerald-500 text-xs @error('solution') border-red-500 focus:ring-red-500 @enderror">{{ old('solution') }}</textarea>
                                @error('solution')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>
                        </div>

                        <!-- Answers Options Section (Max 4 Answers) -->
                        <div id="create_answers_container" class="space-y-2 pt-2 border-t border-slate-800">
                            <div class="flex items-center justify-between">
                                <label id="create_answers_label" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider">Answer Options (Min 2, Max 4)</label>
                                <span id="create_answers_hint" class="text-[11px] text-slate-400 italic">Single: 1 correct. Multiple: ≥1 correct.</span>
                            </div>

                            @error('answers')
                                <div class="p-2 rounded-lg bg-red-950/80 border border-red-500/40 text-red-300 text-xs font-semibold">
                                    {{ $message }}
                                </div>
                            @enderror

                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2" id="create_answers_grid">
                                @for($i = 0; $i < 4; $i++)
                                    <div id="create_ans_slot_{{ $i }}" class="flex items-center space-x-2 bg-slate-950 p-2 rounded-lg border border-slate-800">
                                        <span id="create_ans_badge_{{ $i }}" class="text-xs font-bold text-slate-400 shrink-0 w-5">#{{ $i + 1 }}</span>
                                        <input type="text" id="create_ans_{{ $i }}_name" name="answers[{{ $i }}][name]" value="{{ old('answers.'.$i.'.name') }}" placeholder="Option {{ $i + 1 }} text" oninput="updateMatchMarks('create')" class="flex-1 px-2.5 py-1 rounded-md bg-slate-900 border border-slate-700 text-slate-100 text-xs focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                        <span id="create_ans_arrow_{{ $i }}" class="hidden text-indigo-400 font-bold text-xs shrink-0">&harr;</span>
                                        <input type="text" id="create_ans_{{ $i }}_match" name="answers[{{ $i }}][match_answer]" value="{{ old('answers.'.$i.'.match_answer') }}" placeholder="Matching item..." oninput="updateMatchMarks('create')" class="hidden flex-1 px-2.5 py-1 rounded-md bg-slate-900 border border-slate-700 text-slate-100 text-xs focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                        <label id="create_ans_correct_label_{{ $i }}" class="inline-flex items-center space-x-1 text-[11px] text-slate-300 cursor-pointer shrink-0">
                                            <input type="checkbox" id="create_ans_{{ $i }}_correct" name="answers[{{ $i }}][is_correct]" value="1" {{ old('answers.'.$i.'.is_correct') ? 'checked' : '' }} onchange="handleAnswerCorrectChange('create', {{ $i }})" class="rounded bg-slate-900 border-slate-700 text-emerald-500 focus:ring-emerald-500">
                                            <span class="text-emerald-400 font-medium">Correct</span>
                                        </label>
                                    </div>
                                @endfor
                            </div>
                        </div>
                    </div>

                    <!-- Sticky Modal Footer -->
                    <div class="px-5 py-3 border-t border-slate-800 flex justify-end space-x-3 bg-slate-950/80 shrink-0">
                        <button type="button" onclick="closeCreateQuestionModal()" class="px-4 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-medium transition-colors cursor-pointer">Cancel</button>
                        <button type="submit" class="px-5 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold shadow-lg shadow-indigo-600/30 transition-all cursor-pointer">Save Question</button>
                    </div>
                </form>
            </div>
        </div>

        <!-- EDIT QUESTION MODAL -->
        @php
            $isEditModalOpen = $errors->any() && old('_method') === 'PUT';
        @endphp
        <div id="editQuestionModal" class="{{ $isEditModalOpen ? '' : 'hidden' }} fixed inset-0 z-50 bg-black/75 backdrop-blur-sm overflow-y-auto p-2 sm:p-4 flex justify-center items-start">
            <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-5xl max-h-[92vh] flex flex-col overflow-hidden shadow-2xl my-2 sm:my-3">
                <div class="px-5 py-3 border-b border-slate-800 flex items-center justify-between bg-slate-950/80 shrink-0">
                    <h3 class="text-base font-bold text-white flex items-center gap-2">
                        <svg class="w-5 h-5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/></svg>
                        <span>Edit Question</span>
                    </h3>
                    <button onclick="closeEditQuestionModal()" class="text-slate-400 hover:text-white transition-colors cursor-pointer p-1">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                    </button>
                </div>

                <form id="editQuestionForm" method="POST" action="{{ old('_method') === 'PUT' ? old('_edit_action_url', '') : '' }}" class="flex flex-col flex-1 overflow-hidden">
                    @csrf
                    @method('PUT')
                    <input type="hidden" id="edit_action_url" name="_edit_action_url" value="{{ old('_method') === 'PUT' ? old('_edit_action_url', '') : '' }}">
                    
                    <div class="p-4 sm:p-5 space-y-3 overflow-y-auto flex-1 scrollbar-thin">
                        @if ($isEditModalOpen && $errors->any())
                            <div class="p-3 rounded-xl bg-red-950/80 border border-red-500/40 text-red-200 text-xs">
                                <span class="font-bold flex items-center gap-1 text-red-300">
                                    <svg class="w-4 h-4 inline" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                                    Validation errors occurred. Please check the fields below.
                                </span>
                            </div>
                        @endif

                        <!-- Question Name / Prompt (Rich Text Editor + Math Symbols) -->
                        <div>
                            <div class="flex items-center justify-between mb-1 flex-wrap gap-2">
                                <div class="flex items-center space-x-2 flex-wrap gap-y-1">
                                    <label class="block text-xs font-semibold text-slate-300 uppercase tracking-wider">
                                        Question Name / Prompt <span class="text-red-400">*</span>
                                    </label>
                                    <button type="button" onclick="toggleMathPalette('edit')" class="inline-flex items-center space-x-1.5 px-2 py-0.5 rounded-lg bg-indigo-500/20 hover:bg-indigo-500/30 text-indigo-300 hover:text-indigo-200 border border-indigo-500/40 text-[11px] font-semibold transition-all cursor-pointer shadow-sm">
                                        <span class="text-xs font-bold font-serif leading-none">∑</span>
                                        <span>Math & 🧪 Chemistry Symbols</span>
                                    </button>
                                    <button type="button" onclick="openDrawToolModal('edit')" class="inline-flex items-center space-x-1.5 px-2.5 py-0.5 rounded-lg bg-emerald-500/20 hover:bg-emerald-500/30 text-emerald-300 hover:text-emerald-200 border border-emerald-500/40 text-[11px] font-semibold transition-all cursor-pointer shadow-sm">
                                        <span class="text-xs">📐</span>
                                        <span>Draw Shapes & Geometry</span>
                                    </button>
                                </div>
                                <span class="text-[11px] text-slate-400 font-medium">Rich text, math & chemistry enabled</span>
                            </div>

                            <!-- Interactive Math Symbols & Formula Palette -->
                            <div id="edit_math_palette" class="hidden mb-2 p-2.5 rounded-xl bg-slate-900 border border-indigo-500/40 shadow-xl space-y-2">
                                <div class="flex items-center justify-between gap-2 border-b border-slate-800 pb-1.5">
                                    <div class="flex items-center space-x-2 flex-1 min-w-0">
                                        <div class="relative w-44 shrink-0">
                                            <input type="text" id="edit_math_search" oninput="filterMathSymbols('edit', this.value)" placeholder="Search (H2O, eq, pi)..." class="w-full pl-7 pr-2 py-1 rounded-md bg-slate-950 border border-slate-700 text-slate-100 placeholder-slate-500 text-xs focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                            <svg class="w-3.5 h-3.5 text-slate-400 absolute left-2 top-1.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                                        </div>
                                        <div id="edit_math_tabs" class="flex items-center space-x-1 overflow-x-auto text-xs py-0.5 scrollbar-thin">
                                            <button type="button" onclick="selectMathTab('edit', 'all', this)" class="edit-math-tab active px-2 py-0.5 rounded bg-indigo-600 text-white font-medium text-[11px] whitespace-nowrap">All</button>
                                            <button type="button" onclick="selectMathTab('edit', 'chemistry', this)" class="edit-math-tab px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium text-[11px] whitespace-nowrap">🧪 Chemistry (⇌,↑,↓,≡)</button>
                                            <button type="button" onclick="selectMathTab('edit', 'compounds', this)" class="edit-math-tab px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium text-[11px] whitespace-nowrap">Compounds (H₂O, CO₂)</button>
                                            <button type="button" onclick="selectMathTab('edit', 'operators', this)" class="edit-math-tab px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium text-[11px] whitespace-nowrap">Basic Math (±,×,≤)</button>
                                            <button type="button" onclick="selectMathTab('edit', 'greek', this)" class="edit-math-tab px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium text-[11px] whitespace-nowrap">Greek (π,θ,α)</button>
                                            <button type="button" onclick="selectMathTab('edit', 'fractions', this)" class="edit-math-tab px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium text-[11px] whitespace-nowrap">Roots & Powers (√,x²)</button>
                                            <button type="button" onclick="selectMathTab('edit', 'calculus', this)" class="edit-math-tab px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium text-[11px] whitespace-nowrap">Calculus (∫,∑,∂)</button>
                                            <button type="button" onclick="selectMathTab('edit', 'geometry', this)" class="edit-math-tab px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium text-[11px] whitespace-nowrap">Geometry (°,∠,⊥)</button>
                                            <button type="button" onclick="selectMathTab('edit', 'formulas', this)" class="edit-math-tab px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium text-[11px] whitespace-nowrap">Formulas & Reactions</button>
                                        </div>
                                    </div>
                                    <button type="button" onclick="toggleMathPalette('edit')" class="p-1 rounded text-slate-400 hover:text-white hover:bg-slate-800" title="Close">
                                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                                    </button>
                                </div>
                                <div id="edit_math_symbols_grid" class="flex flex-wrap gap-1 max-h-32 overflow-y-auto p-1.5 bg-slate-950/60 rounded-lg border border-slate-800/80">
                                    <!-- Populated dynamically by JS -->
                                </div>
                            </div>

                            <input type="hidden" id="edit_q_name" name="name" value="{{ old('_method') === 'PUT' ? old('name') : '' }}">
                            <div id="edit_q_editor_container" class="rounded-xl overflow-hidden border border-slate-700 bg-slate-950 focus-within:ring-2 focus-within:ring-indigo-500 @error('name') border-red-500 ring-1 ring-red-500 @enderror">
                                <div id="edit_q_editor"></div>
                            </div>
                            <p id="edit_q_name_client_error" class="hidden mt-1 text-xs text-red-400">Please enter a question prompt.</p>
                            @error('name')
                                <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                            @enderror
                        </div>

                        <!-- Subject, Chapter, Topic Selection Grid -->
                        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5 p-3 rounded-xl bg-slate-950/60 border border-slate-800">
                            <!-- Standard Select (Required) -->
                            <div>
                                <label for="edit_q_standard" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Standard <span class="text-red-400">*</span></label>
                                <select id="edit_q_standard" name="standard_id" required class="w-full px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-xs @error('standard_id') border-red-500 focus:ring-red-500 @enderror">
                                    <option value="" disabled>Select Standard</option>
                                    @foreach($standards as $std)
                                        <option value="{{ $std->id }}" {{ old('_method') === 'PUT' && old('standard_id') == $std->id ? 'selected' : '' }}>{{ $std->name }}</option>
                                    @endforeach
                                </select>
                                @error('standard_id')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>

                            <!-- Subject Select (Optional) -->
                            <div>
                                <label for="edit_subject" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Subject</label>
                                <select id="edit_subject" name="subject_id" onchange="filterChapters('edit', this.value)" class="w-full px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-xs @error('subject_id') border-red-500 focus:ring-red-500 @enderror">
                                    <option value="">Select Subject</option>
                                    @foreach($subjects as $sbj)
                                        <option value="{{ $sbj->id }}" {{ old('_method') === 'PUT' && old('subject_id') == $sbj->id ? 'selected' : '' }}>{{ $sbj->name }}</option>
                                    @endforeach
                                </select>
                                @error('subject_id')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>

                            <!-- Chapter Select (Optional) -->
                            <div>
                                <label for="edit_chapter" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Chapter</label>
                                <select id="edit_chapter" name="chapter_id" onchange="filterTopics('edit', this.value)" class="w-full px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-xs @error('chapter_id') border-red-500 focus:ring-red-500 @enderror">
                                    <option value="">Select Chapter</option>
                                    @foreach($chapters as $ch)
                                        <option value="{{ $ch->id }}" {{ old('_method') === 'PUT' && old('chapter_id') == $ch->id ? 'selected' : '' }}>{{ $ch->name }}</option>
                                    @endforeach
                                </select>
                                @error('chapter_id')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>

                            <!-- Topic Select (Optional) -->
                            <div>
                                <label for="edit_topic" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Topic</label>
                                <select id="edit_topic" name="topic_id" class="w-full px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-xs @error('topic_id') border-red-500 focus:ring-red-500 @enderror">
                                    <option value="">Select Topic</option>
                                    @foreach($topics as $tp)
                                        <option value="{{ $tp->id }}" {{ old('_method') === 'PUT' && old('topic_id') == $tp->id ? 'selected' : '' }}>{{ $tp->name }}</option>
                                    @endforeach
                                </select>
                                @error('topic_id')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>
                        </div>

                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
                            <!-- Type Select (Required) -->
                            <div>
                                <label for="edit_q_type" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Question Type <span class="text-red-400">*</span></label>
                                <select id="edit_q_type" name="type" required onchange="toggleAnswersSection('edit', this.value)" class="w-full px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-xs @error('type') border-red-500 focus:ring-red-500 @enderror">
                                    <option value="1" {{ old('_method') === 'PUT' && old('type') == '1' ? 'selected' : '' }}>1 - Single Option</option>
                                    <option value="2" {{ old('_method') === 'PUT' && old('type') == '2' ? 'selected' : '' }}>2 - Multiple Option</option>
                                    <option value="4" {{ old('_method') === 'PUT' && old('type') == '4' ? 'selected' : '' }}>4 - True / False</option>
                                    <option value="5" {{ old('_method') === 'PUT' && old('type') == '5' ? 'selected' : '' }}>5 - Match the Following</option>
                                    <option value="3" {{ old('_method') === 'PUT' && old('type') == '3' ? 'selected' : '' }}>3 - Text Entry</option>
                                </select>
                                @error('type')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>

                            <!-- Marks (Required, Numbers Only) -->
                            <div>
                                <label for="edit_q_marks" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Marks <span class="text-red-400">*</span></label>
                                <input type="number" id="edit_q_marks" name="marks" required min="0" step="1" value="{{ old('_method') === 'PUT' ? old('marks') : '' }}" class="w-full px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-xs @error('marks') border-red-500 focus:ring-red-500 @enderror">
                                <p id="edit_marks_hint" class="mt-1 text-[11px] text-amber-300 font-medium hidden">Auto-calculated: 1 mark per valid matching pair (e.g. 4 pairs = 4 marks)</p>
                                @error('marks')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>
                        </div>

                        <!-- Description (Optional) -->
                        <div>
                            <label for="edit_q_desc" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Description (Optional)</label>
                            <textarea id="edit_q_desc" name="description" rows="1" class="w-full px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-xs @error('description') border-red-500 focus:ring-red-500 @enderror">{{ old('_method') === 'PUT' ? old('description') : '' }}</textarea>
                            @error('description')
                                <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                            @enderror
                        </div>

                        <!-- Hint / Solution (Optional) -->
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-1 border-t border-slate-800/60">
                            <!-- Hint (Optional) -->
                            <div>
                                <div class="flex items-center justify-between mb-1">
                                    <label for="edit_q_hint" class="block text-xs font-semibold text-amber-300 uppercase tracking-wider flex items-center gap-1.5">
                                        <svg class="w-3.5 h-3.5 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/></svg>
                                        <span>Hint (Optional)</span>
                                    </label>
                                    <span class="text-[10px] text-slate-400">Shown in exam if clicked</span>
                                </div>
                                <textarea id="edit_q_hint" name="hint" rows="2" placeholder="Provide a hint or clue to guide students during exam..." class="w-full px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-amber-500 text-xs @error('hint') border-red-500 focus:ring-red-500 @enderror">{{ old('_method') === 'PUT' ? old('hint') : '' }}</textarea>
                                @error('hint')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>

                            <!-- Solution (Optional) -->
                            <div>
                                <div class="flex items-center justify-between mb-1">
                                    <label for="edit_q_solution" class="block text-xs font-semibold text-emerald-300 uppercase tracking-wider flex items-center gap-1.5">
                                        <svg class="w-3.5 h-3.5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                                        <span>Solution / Explanation (Optional)</span>
                                    </label>
                                    <span class="text-[10px] text-slate-400">Full answer breakdown</span>
                                </div>
                                <textarea id="edit_q_solution" name="solution" rows="2" placeholder="Provide complete solution / working for the question..." class="w-full px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-emerald-500 text-xs @error('solution') border-red-500 focus:ring-red-500 @enderror">{{ old('_method') === 'PUT' ? old('solution') : '' }}</textarea>
                                @error('solution')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>
                        </div>

                        <!-- Answers Options Section (Max 4 Answers) -->
                        <div id="edit_answers_container" class="space-y-2 pt-2 border-t border-slate-800">
                            <div class="flex items-center justify-between">
                                <label id="edit_answers_label" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider">Answer Options (Min 2, Max 4)</label>
                                <span id="edit_answers_hint" class="text-[11px] text-slate-400 italic">Single: 1 correct. Multiple: ≥1 correct.</span>
                            </div>

                            @error('answers')
                                <div class="p-2 rounded-lg bg-red-950/80 border border-red-500/40 text-red-300 text-xs font-semibold">
                                    {{ $message }}
                                </div>
                            @enderror

                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2" id="edit_answers_grid">
                                @for($i = 0; $i < 4; $i++)
                                    <div id="edit_ans_slot_{{ $i }}" class="flex items-center space-x-2 bg-slate-950 p-2 rounded-lg border border-slate-800">
                                        <span id="edit_ans_badge_{{ $i }}" class="text-xs font-bold text-slate-400 shrink-0 w-5">#{{ $i + 1 }}</span>
                                        <input type="text" id="edit_ans_{{ $i }}_name" name="answers[{{ $i }}][name]" value="{{ old('_method') === 'PUT' ? old('answers.'.$i.'.name') : '' }}" placeholder="Option {{ $i + 1 }} text" oninput="updateMatchMarks('edit')" class="flex-1 px-2.5 py-1 rounded-md bg-slate-900 border border-slate-700 text-slate-100 text-xs focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                        <span id="edit_ans_arrow_{{ $i }}" class="hidden text-indigo-400 font-bold text-xs shrink-0">&harr;</span>
                                        <input type="text" id="edit_ans_{{ $i }}_match" name="answers[{{ $i }}][match_answer]" value="{{ old('_method') === 'PUT' ? old('answers.'.$i.'.match_answer') : '' }}" placeholder="Matching item..." oninput="updateMatchMarks('edit')" class="hidden flex-1 px-2.5 py-1 rounded-md bg-slate-900 border border-slate-700 text-slate-100 text-xs focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                        <label id="edit_ans_correct_label_{{ $i }}" class="inline-flex items-center space-x-1 text-[11px] text-slate-300 cursor-pointer shrink-0">
                                            <input type="checkbox" id="edit_ans_{{ $i }}_correct" name="answers[{{ $i }}][is_correct]" value="1" {{ old('_method') === 'PUT' && old('answers.'.$i.'.is_correct') ? 'checked' : '' }} onchange="handleAnswerCorrectChange('edit', {{ $i }})" class="rounded bg-slate-900 border-slate-700 text-emerald-500 focus:ring-emerald-500">
                                            <span class="text-emerald-400 font-medium">Correct</span>
                                        </label>
                                    </div>
                                @endfor
                            </div>
                        </div>
                    </div>

                    <!-- Sticky Modal Footer -->
                    <div class="px-5 py-3 border-t border-slate-800 flex justify-end space-x-3 bg-slate-950/80 shrink-0">
                        <button type="button" onclick="closeEditQuestionModal()" class="px-4 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-medium transition-colors cursor-pointer">Cancel</button>
                        <button type="submit" class="px-5 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold shadow-lg shadow-indigo-600/30 transition-all cursor-pointer">Update Question</button>
                    </div>
                </form>
            </div>
        </div>

        <!-- VIEW QUESTION DETAILS MODAL -->
        <div id="viewQuestionModal" class="hidden fixed inset-0 z-50 bg-black/80 backdrop-blur-md overflow-y-auto p-2 sm:p-4 flex justify-center items-start">
            <div class="bg-slate-900 border border-slate-800 rounded-3xl w-full max-w-4xl max-h-[92vh] flex flex-col overflow-hidden shadow-2xl my-2 sm:my-3">
                <!-- Modal Header -->
                <div class="px-6 py-4 border-b border-slate-800 flex items-center justify-between bg-slate-950/90 shrink-0">
                    <div class="flex items-center space-x-3">
                        <div class="w-10 h-10 rounded-2xl bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 flex items-center justify-center font-bold text-lg shadow-inner">
                            <span>📋</span>
                        </div>
                        <div>
                            <div class="flex items-center space-x-2 flex-wrap gap-y-1">
                                <h3 class="text-base font-bold text-white tracking-tight">Question Details</h3>
                                <span id="vq_badge_id" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">#105</span>
                                <span id="vq_badge_type" class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-purple-500/20 text-purple-300 border border-purple-500/30">Single Option</span>
                                <span id="vq_badge_marks" class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">1 Mark</span>
                            </div>
                            <p class="text-xs text-slate-400 mt-0.5">Comprehensive view of question prompt, answers, hint, and solution.</p>
                        </div>
                    </div>
                    <button type="button" onclick="closeViewQuestionModal()" class="w-9 h-9 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-slate-400 hover:text-white flex items-center justify-center transition-all cursor-pointer border border-slate-700/60">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                    </button>
                </div>

                <!-- Curriculum Classification Breadcrumbs -->
                <div class="px-6 py-2.5 bg-slate-950/60 border-b border-slate-800 flex items-center flex-wrap gap-2 text-xs text-slate-300 shrink-0">
                    <span class="text-[10px] font-bold text-slate-500 uppercase tracking-wider">Classification:</span>
                    <span id="vq_syllabus" class="px-2.5 py-0.5 rounded-lg bg-pink-500/10 text-pink-300 border border-pink-500/20 font-medium">Syllabus: CBSE</span>
                    <span id="vq_standard" class="px-2.5 py-0.5 rounded-lg bg-sky-500/10 text-sky-300 border border-sky-500/20 font-medium">Class 9</span>
                    <span id="vq_subject" class="px-2.5 py-0.5 rounded-lg bg-indigo-500/10 text-indigo-300 border border-indigo-500/20 font-medium">Mathematics</span>
                    <span id="vq_chapter" class="px-2.5 py-0.5 rounded-lg bg-purple-500/10 text-purple-300 border border-purple-500/20 font-medium">Number System</span>
                    <span id="vq_topic" class="px-2.5 py-0.5 rounded-lg bg-emerald-500/10 text-emerald-300 border border-emerald-500/20 font-medium">Number System</span>
                </div>

                <!-- Modal Body (Scrollable) -->
                <div class="p-6 overflow-y-auto space-y-5 flex-1">
                    <!-- Question Prompt Card -->
                    <div class="space-y-1.5">
                        <label class="text-[11px] font-bold text-slate-400 uppercase tracking-wider flex items-center space-x-1.5">
                            <span>❓</span>
                            <span>Question Prompt</span>
                        </label>
                        <div class="p-4 sm:p-5 rounded-2xl bg-slate-950/80 border border-slate-800 shadow-inner">
                            <div id="vq_prompt" class="text-sm sm:text-base text-white font-medium leading-relaxed prose prose-invert max-w-none break-words"></div>
                        </div>
                    </div>

                    <!-- Description / Subtext -->
                    <div id="vq_desc_container" class="space-y-1.5 hidden">
                        <label class="text-[11px] font-bold text-slate-400 uppercase tracking-wider flex items-center space-x-1.5">
                            <span>📌</span>
                            <span>Description / Context</span>
                        </label>
                        <div class="p-3.5 rounded-xl bg-slate-950/40 border border-slate-800 text-xs text-slate-300 italic" id="vq_desc"></div>
                    </div>

                    <!-- Options / Answers Section -->
                    <div class="space-y-2">
                        <label class="text-[11px] font-bold text-slate-400 uppercase tracking-wider flex items-center space-x-1.5">
                            <span>🎯</span>
                            <span>Answer Options & Key</span>
                        </label>
                        <div id="vq_answers_container" class="space-y-2"></div>
                    </div>

                    <!-- Hint Section -->
                    <div id="vq_hint_container" class="p-4 sm:p-5 rounded-2xl bg-amber-500/10 border border-amber-500/30 space-y-1.5">
                        <div class="flex items-center space-x-2 text-amber-300 font-bold text-xs uppercase tracking-wider">
                            <span>💡</span>
                            <span>Hint for Students</span>
                        </div>
                        <div id="vq_hint_text" class="text-xs sm:text-sm text-amber-200/90 leading-relaxed font-normal"></div>
                    </div>

                    <!-- Solution Section -->
                    <div id="vq_solution_container" class="p-4 sm:p-5 rounded-2xl bg-emerald-500/10 border border-emerald-500/30 space-y-1.5">
                        <div class="flex items-center space-x-2 text-emerald-300 font-bold text-xs uppercase tracking-wider">
                            <span>📝</span>
                            <span>Step-by-Step Solution & Explanation</span>
                        </div>
                        <div id="vq_solution_text" class="text-xs sm:text-sm text-emerald-200/90 leading-relaxed font-normal whitespace-pre-line"></div>
                    </div>

                    <!-- Creator & Timestamp Metadata -->
                    <div class="p-3.5 rounded-xl bg-slate-950/40 border border-slate-800 flex items-center justify-between text-xs text-slate-400 flex-wrap gap-2">
                        <div>
                            Created by: <span id="vq_creator" class="font-semibold text-slate-200"></span>
                        </div>
                        <div>
                            Timestamp: <span id="vq_date" class="font-medium text-slate-300"></span>
                        </div>
                    </div>
                </div>

                <!-- Footer -->
                <div class="px-6 py-3.5 border-t border-slate-800 bg-slate-950/80 flex items-center justify-between shrink-0">
                    <button type="button" onclick="closeViewQuestionModal()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition-colors cursor-pointer">
                        Close
                    </button>
                    <button type="button" id="vq_edit_btn" onclick="editCurrentViewQuestion()" class="px-5 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold shadow-lg shadow-indigo-600/30 transition-all inline-flex items-center space-x-1.5 cursor-pointer">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/></svg>
                        <span>Edit Question</span>
                    </button>
                </div>
            </div>
        </div>

        <!-- DRAW TOOL MODAL -->
        <x-draw-tool-modal />

        <script>
            const allStandardsData = @json($standards);
            const subjectsData = @json($subjectsData);
            const allChaptersData = @json($chapters);
            const allTopicsData = @json($topics);

            function filterStandardsBySyllabus(prefix, selectedSyllabusId) {
                const standardSelect = document.getElementById(prefix + '_standard');
                if (!standardSelect) return;
                const currentVal = standardSelect.value;
                const defaultText = prefix === 'filter' ? 'All Standards' : 'Select Standard';
                standardSelect.innerHTML = `<option value="">${defaultText}</option>`;

                const filtered = selectedSyllabusId
                    ? allStandardsData.filter(s => parseInt(s.syllabus_id) === parseInt(selectedSyllabusId))
                    : allStandardsData;

                filtered.forEach(std => {
                    const opt = document.createElement('option');
                    opt.value = std.id;
                    opt.textContent = std.name;
                    if (currentVal && parseInt(currentVal) === parseInt(std.id)) {
                        opt.selected = true;
                    }
                    standardSelect.appendChild(opt);
                });
            }

            function filterChapters(prefix, selectedSubjectId, selectedChapterId = null, selectedTopicId = null) {
                const chapterSelect = document.getElementById(prefix + '_chapter');
                const topicSelect = document.getElementById(prefix + '_topic');

                if (!chapterSelect) return;

                const defaultText = prefix === 'filter' ? 'All Chapters' : 'Select Chapter';
                chapterSelect.innerHTML = `<option value="">${defaultText}</option>`;

                if (topicSelect) {
                    const defaultTopicText = prefix === 'filter' ? 'All Topics' : 'Select Topic';
                    topicSelect.innerHTML = `<option value="">${defaultTopicText}</option>`;
                }

                if (!selectedSubjectId) {
                    allChaptersData.forEach(ch => {
                        const opt = document.createElement('option');
                        opt.value = ch.id;
                        opt.textContent = ch.name;
                        if (selectedChapterId && parseInt(selectedChapterId) === parseInt(ch.id)) opt.selected = true;
                        chapterSelect.appendChild(opt);
                    });

                    if (selectedChapterId && topicSelect) {
                        filterTopics(prefix, selectedChapterId, selectedTopicId);
                    }
                    return;
                }

                const subject = subjectsData.find(s => parseInt(s.id) === parseInt(selectedSubjectId));
                if (subject && subject.chapters) {
                    subject.chapters.forEach(ch => {
                        const opt = document.createElement('option');
                        opt.value = ch.id;
                        opt.textContent = ch.name;
                        if (selectedChapterId && parseInt(selectedChapterId) === parseInt(ch.id)) opt.selected = true;
                        chapterSelect.appendChild(opt);
                    });
                }

                if (selectedChapterId && topicSelect) {
                    filterTopics(prefix, selectedChapterId, selectedTopicId);
                }
            }

            function filterTopics(prefix, selectedChapterId, selectedTopicId = null) {
                const topicSelect = document.getElementById(prefix + '_topic');
                if (!topicSelect) return;

                const defaultTopicText = prefix === 'filter' ? 'All Topics' : 'Select Topic';
                topicSelect.innerHTML = `<option value="">${defaultTopicText}</option>`;

                if (!selectedChapterId) {
                    allTopicsData.forEach(tp => {
                        const opt = document.createElement('option');
                        opt.value = tp.id;
                        opt.textContent = tp.name;
                        if (selectedTopicId && parseInt(selectedTopicId) === parseInt(tp.id)) opt.selected = true;
                        topicSelect.appendChild(opt);
                    });
                    return;
                }

                let targetTopics = [];
                subjectsData.forEach(s => {
                    if (s.chapters) {
                        const ch = s.chapters.find(c => parseInt(c.id) === parseInt(selectedChapterId));
                        if (ch && ch.topics) {
                            targetTopics = ch.topics;
                        }
                    }
                });

                if (targetTopics.length === 0) {
                    allTopicsData.forEach(tp => {
                        if (parseInt(tp.chapter_id) === parseInt(selectedChapterId)) {
                            targetTopics.push(tp);
                        }
                    });
                }

                targetTopics.forEach(tp => {
                    const opt = document.createElement('option');
                    opt.value = tp.id;
                    opt.textContent = tp.name;
                    if (selectedTopicId && parseInt(selectedTopicId) === parseInt(tp.id)) opt.selected = true;
                    topicSelect.appendChild(opt);
                });
            }

            function toggleAnswersSection(prefix, typeVal) {
                const container = document.getElementById(prefix + '_answers_container');
                const label = document.getElementById(prefix + '_answers_label');
                const hint = document.getElementById(prefix + '_answers_hint');
                const val = parseInt(typeVal);

                if (!container) return;

                if (val === 3) {
                    container.classList.add('hidden');
                } else if (val === 4) {
                    container.classList.remove('hidden');
                    if (label) label.textContent = 'Answer Options (True / False)';
                    if (hint) hint.textContent = 'Select whether True or False is the correct answer';

                    // Reset Match inputs if previously opened
                    for (let i = 0; i < 4; i++) {
                        const arrow = document.getElementById(prefix + '_ans_arrow_' + i);
                        const matchInp = document.getElementById(prefix + '_ans_' + i + '_match');
                        const chkLabel = document.getElementById(prefix + '_ans_correct_label_' + i);
                        if (arrow) arrow.classList.add('hidden');
                        if (matchInp) { matchInp.classList.add('hidden'); matchInp.value = ''; }
                        if (chkLabel) chkLabel.classList.remove('hidden');
                    }

                    // Slot 0 -> True
                    const slot0 = document.getElementById(prefix + '_ans_slot_0');
                    const inp0 = document.getElementById(prefix + '_ans_0_name');
                    const chk0 = document.getElementById(prefix + '_ans_0_correct');
                    const badge0 = document.getElementById(prefix + '_ans_badge_0');
                    if (slot0) slot0.classList.remove('hidden');
                    if (badge0) badge0.textContent = 'T';
                    if (inp0) {
                        inp0.value = 'True';
                        inp0.placeholder = 'True';
                        inp0.readOnly = true;
                    }

                    // Slot 1 -> False
                    const slot1 = document.getElementById(prefix + '_ans_slot_1');
                    const inp1 = document.getElementById(prefix + '_ans_1_name');
                    const chk1 = document.getElementById(prefix + '_ans_1_correct');
                    const badge1 = document.getElementById(prefix + '_ans_badge_1');
                    if (slot1) slot1.classList.remove('hidden');
                    if (badge1) badge1.textContent = 'F';
                    if (inp1) {
                        inp1.value = 'False';
                        inp1.placeholder = 'False';
                        inp1.readOnly = true;
                    }

                    // Default to True if neither is checked
                    if (chk0 && chk1 && !chk0.checked && !chk1.checked) {
                        chk0.checked = true;
                    }

                    // Slots 2 & 3 -> Hide
                    for (let i = 2; i < 4; i++) {
                        const slot = document.getElementById(prefix + '_ans_slot_' + i);
                        const inp = document.getElementById(prefix + '_ans_' + i + '_name');
                        const chk = document.getElementById(prefix + '_ans_' + i + '_correct');
                        if (slot) slot.classList.add('hidden');
                        if (inp) inp.value = '';
                        if (chk) chk.checked = false;
                    }
                } else if (val === 5) {
                    container.classList.remove('hidden');
                    if (label) label.textContent = 'Matching Pairs (Min 2, Max 4 Pairs)';
                    if (hint) hint.textContent = 'Enter the Left item and its corresponding Right match (1 mark per pair)';

                    const marksHint = document.getElementById(prefix + '_marks_hint');
                    if (marksHint) marksHint.classList.remove('hidden');

                    for (let i = 0; i < 4; i++) {
                        const slot = document.getElementById(prefix + '_ans_slot_' + i);
                        const inpName = document.getElementById(prefix + '_ans_' + i + '_name');
                        const arrow = document.getElementById(prefix + '_ans_arrow_' + i);
                        const matchInp = document.getElementById(prefix + '_ans_' + i + '_match');
                        const chkLabel = document.getElementById(prefix + '_ans_correct_label_' + i);
                        const badge = document.getElementById(prefix + '_ans_badge_' + i);

                        if (slot) slot.classList.remove('hidden');
                        if (badge) badge.textContent = String.fromCharCode(65 + i);
                        if (inpName) {
                            inpName.readOnly = false;
                            inpName.placeholder = 'Left item ' + String.fromCharCode(65 + i);
                            if (inpName.value === 'True' || inpName.value === 'False') inpName.value = '';
                        }
                        if (arrow) arrow.classList.remove('hidden');
                        if (matchInp) {
                            matchInp.classList.remove('hidden');
                            matchInp.placeholder = 'Right match ' + (i + 1);
                        }
                        if (chkLabel) chkLabel.classList.add('hidden');
                    }

                    updateMatchMarks(prefix);
                } else {
                    container.classList.remove('hidden');
                    if (label) label.textContent = 'Answer Options (Min 2, Max 4)';
                    if (hint) hint.textContent = 'Single: 1 correct. Multiple: ≥1 correct.';

                    const marksHint = document.getElementById(prefix + '_marks_hint');
                    if (marksHint) marksHint.classList.add('hidden');

                    for (let i = 0; i < 4; i++) {
                        const slot = document.getElementById(prefix + '_ans_slot_' + i);
                        const inp = document.getElementById(prefix + '_ans_' + i + '_name');
                        const arrow = document.getElementById(prefix + '_ans_arrow_' + i);
                        const matchInp = document.getElementById(prefix + '_ans_' + i + '_match');
                        const chkLabel = document.getElementById(prefix + '_ans_correct_label_' + i);
                        const badge = document.getElementById(prefix + '_ans_badge_' + i);

                        if (slot) slot.classList.remove('hidden');
                        if (badge) badge.textContent = '#' + (i + 1);
                        if (inp) {
                            inp.readOnly = false;
                            inp.placeholder = 'Option ' + (i + 1) + ' text';
                            if (inp.value === 'True' || inp.value === 'False') inp.value = '';
                        }
                        if (arrow) arrow.classList.add('hidden');
                        if (matchInp) { matchInp.classList.add('hidden'); matchInp.value = ''; }
                        if (chkLabel) chkLabel.classList.remove('hidden');
                    }
                }
            }

            function updateMatchMarks(prefix) {
                const typeEl = document.getElementById(prefix + '_q_type');
                if (!typeEl || parseInt(typeEl.value) !== 5) return;

                let pairCount = 0;
                for (let i = 0; i < 4; i++) {
                    const inpName = document.getElementById(prefix + '_ans_' + i + '_name');
                    const matchInp = document.getElementById(prefix + '_ans_' + i + '_match');
                    if (inpName && matchInp && inpName.value.trim() !== '' && matchInp.value.trim() !== '') {
                        pairCount++;
                    }
                }

                const marksInput = document.getElementById(prefix + '_q_marks');
                if (marksInput && (pairCount > 0 || prefix === 'create')) {
                    marksInput.value = pairCount > 0 ? pairCount : 4;
                }
            }

            function handleAnswerCorrectChange(prefix, index) {
                const typeEl = document.getElementById(prefix + '_q_type');
                const typeVal = typeEl ? parseInt(typeEl.value) : 1;
                const chk = document.getElementById(prefix + '_ans_' + index + '_correct');

                if ((typeVal === 1 || typeVal === 4) && chk && chk.checked) {
                    for (let i = 0; i < 4; i++) {
                        if (i !== index) {
                            const otherChk = document.getElementById(prefix + '_ans_' + i + '_correct');
                            if (otherChk) otherChk.checked = false;
                        }
                    }
                }
            }

            let createQuill = null;
            let editQuill = null;

            const mathSymbolsData = [
                // --- Chemistry: Reactions, Equilibrium & Phase ---
                { category: 'chemistry', name: 'Equilibrium Arrow', symbol: '⇌' },
                { category: 'chemistry', name: 'Reversible Reaction Arrow', symbol: '⇄' },
                { category: 'chemistry', name: 'Forward Reaction Arrow', symbol: '→' },
                { category: 'chemistry', name: 'Reverse Reaction Arrow', symbol: '←' },
                { category: 'chemistry', name: 'Resonance Arrow', symbol: '↔' },
                { category: 'chemistry', name: 'Gas Released / Upward Arrow', symbol: '↑' },
                { category: 'chemistry', name: 'Precipitate Formed / Downward Arrow', symbol: '↓' },
                { category: 'chemistry', name: 'Forward Half-Arrow', symbol: '⇀' },
                { category: 'chemistry', name: 'Reverse Half-Arrow', symbol: '⇁' },
                { category: 'chemistry', name: 'Heat of Reaction / Thermal (Delta)', symbol: 'Δ' },
                { category: 'chemistry', name: 'Light / Photochemical (hv)', symbol: 'hν' },

                // --- Chemistry: Chemical Bonds ---
                { category: 'chemistry', name: 'Single Bond', symbol: '−' },
                { category: 'chemistry', name: 'Double Bond', symbol: '=' },
                { category: 'chemistry', name: 'Triple Bond', symbol: '≡' },
                { category: 'chemistry', name: 'Hydrogen / Dotted Bond', symbol: '···' },
                { category: 'chemistry', name: 'Coordinate / Dative Bond', symbol: '→' },

                // --- Chemistry: States of Matter ---
                { category: 'chemistry', name: 'Solid State', symbol: '(s)' },
                { category: 'chemistry', name: 'Liquid State', symbol: '(l)' },
                { category: 'chemistry', name: 'Gas State', symbol: '(g)' },
                { category: 'chemistry', name: 'Aqueous Solution', symbol: '(aq)' },
                { category: 'chemistry', name: 'Precipitate', symbol: '(ppt)' },

                // --- Chemistry: Charges & Radicals ---
                { category: 'chemistry', name: 'Positive Charge (Cation)', symbol: '⁺' },
                { category: 'chemistry', name: 'Negative Charge (Anion)', symbol: '⁻' },
                { category: 'chemistry', name: '2+ Charge', symbol: '²⁺' },
                { category: 'chemistry', name: '3+ Charge', symbol: '³⁺' },
                { category: 'chemistry', name: '2- Charge', symbol: '²⁻' },
                { category: 'chemistry', name: '3- Charge', symbol: '³⁻' },
                { category: 'chemistry', name: 'Partial Positive Charge', symbol: 'δ⁺' },
                { category: 'chemistry', name: 'Partial Negative Charge', symbol: 'δ⁻' },
                { category: 'chemistry', name: 'Free Radical (Dot)', symbol: '•' },
                { category: 'chemistry', name: 'Electron', symbol: 'e⁻' },
                { category: 'chemistry', name: 'Proton', symbol: 'p⁺' },
                { category: 'chemistry', name: 'Neutron', symbol: 'n⁰' },
                { category: 'chemistry', name: 'Alpha Particle', symbol: 'α' },
                { category: 'chemistry', name: 'Beta Particle', symbol: 'β' },
                { category: 'chemistry', name: 'Gamma Radiation', symbol: 'γ' },

                // --- Chemistry: Thermodynamics & Properties ---
                { category: 'chemistry', name: 'Standard State', symbol: '°' },
                { category: 'chemistry', name: 'Enthalpy Change', symbol: 'ΔH' },
                { category: 'chemistry', name: 'Standard Enthalpy', symbol: 'ΔH°' },
                { category: 'chemistry', name: 'Gibbs Free Energy', symbol: 'ΔG' },
                { category: 'chemistry', name: 'Standard Gibbs Free Energy', symbol: 'ΔG°' },
                { category: 'chemistry', name: 'Entropy Change', symbol: 'ΔS' },
                { category: 'chemistry', name: 'Standard Entropy', symbol: 'ΔS°' },
                { category: 'chemistry', name: 'Standard Electrode Potential', symbol: 'E°' },
                { category: 'chemistry', name: 'pH', symbol: 'pH' },
                { category: 'chemistry', name: 'pOH', symbol: 'pOH' },
                { category: 'chemistry', name: 'Acid Dissociation Constant', symbol: 'Kₐ' },
                { category: 'chemistry', name: 'Base Dissociation Constant', symbol: 'K_b' },
                { category: 'chemistry', name: 'Solubility Product Constant', symbol: 'K_sp' },
                { category: 'chemistry', name: 'Equilibrium Constant (Concentration)', symbol: 'K_c' },
                { category: 'chemistry', name: 'Equilibrium Constant (Pressure)', symbol: 'K_p' },
                { category: 'chemistry', name: 'Activation Energy', symbol: 'E_a' },
                { category: 'chemistry', name: 'Half-Life', symbol: 't₁/₂' },
                { category: 'chemistry', name: 'Wavelength', symbol: 'λ' },
                { category: 'chemistry', name: 'Frequency', symbol: 'ν' },

                // --- Chemistry: Common Formulas & Ions ---
                { category: 'compounds', name: 'Water', symbol: 'H₂O' },
                { category: 'compounds', name: 'Carbon Dioxide', symbol: 'CO₂' },
                { category: 'compounds', name: 'Oxygen Gas', symbol: 'O₂' },
                { category: 'compounds', name: 'Hydrogen Gas', symbol: 'H₂' },
                { category: 'compounds', name: 'Nitrogen Gas', symbol: 'N₂' },
                { category: 'compounds', name: 'Ammonia', symbol: 'NH₃' },
                { category: 'compounds', name: 'Methane', symbol: 'CH₄' },
                { category: 'compounds', name: 'Hydrochloric Acid', symbol: 'HCl' },
                { category: 'compounds', name: 'Sulfuric Acid', symbol: 'H₂SO₄' },
                { category: 'compounds', name: 'Nitric Acid', symbol: 'HNO₃' },
                { category: 'compounds', name: 'Sodium Hydroxide', symbol: 'NaOH' },
                { category: 'compounds', name: 'Sodium Chloride', symbol: 'NaCl' },
                { category: 'compounds', name: 'Hydronium Ion', symbol: 'H₃O⁺' },
                { category: 'compounds', name: 'Hydroxide Ion', symbol: 'OH⁻' },
                { category: 'compounds', name: 'Sulfate Ion', symbol: 'SO₄²⁻' },
                { category: 'compounds', name: 'Nitrate Ion', symbol: 'NO₃⁻' },
                { category: 'compounds', name: 'Carbonate Ion', symbol: 'CO₃²⁻' },
                { category: 'compounds', name: 'Bicarbonate Ion', symbol: 'HCO₃⁻' },
                { category: 'compounds', name: 'Ammonium Ion', symbol: 'NH₄⁺' },
                { category: 'compounds', name: 'Phosphate Ion', symbol: 'PO₄³⁻' },
                { category: 'compounds', name: 'Calcium Carbonate', symbol: 'CaCO₃' },
                { category: 'compounds', name: 'Glucose', symbol: 'C₆H₁₂O₆' },
                { category: 'compounds', name: 'Ethanol', symbol: 'C₂H₅OH' },
                { category: 'compounds', name: 'Acetic Acid', symbol: 'CH₃COOH' },
                { category: 'compounds', name: 'Potassium Permanganate', symbol: 'KMnO₄' },
                { category: 'compounds', name: 'Ferrous Ion', symbol: 'Fe²⁺' },
                { category: 'compounds', name: 'Ferric Ion', symbol: 'Fe³⁺' },
                { category: 'compounds', name: 'Cupric Ion', symbol: 'Cu²⁺' },
                { category: 'compounds', name: 'Silver Ion', symbol: 'Ag⁺' },
                { category: 'compounds', name: 'Zinc Ion', symbol: 'Zn²⁺' },

                // Basic Operators & Relations
                { category: 'operators', name: 'Plus-Minus', symbol: '±' },
                { category: 'operators', name: 'Minus-Plus', symbol: '∓' },
                { category: 'operators', name: 'Multiply', symbol: '×' },
                { category: 'operators', name: 'Divide', symbol: '÷' },
                { category: 'operators', name: 'Not Equal', symbol: '≠' },
                { category: 'operators', name: 'Approximately Equal', symbol: '≈' },
                { category: 'operators', name: 'Identical To / Equivalent', symbol: '≡' },
                { category: 'operators', name: 'Less Than or Equal', symbol: '≤' },
                { category: 'operators', name: 'Greater Than or Equal', symbol: '≥' },
                { category: 'operators', name: 'Much Less Than', symbol: '≪' },
                { category: 'operators', name: 'Much Greater Than', symbol: '≫' },
                { category: 'operators', name: 'Infinity', symbol: '∞' },
                { category: 'operators', name: 'Proportional To', symbol: '∝' },
                { category: 'operators', name: 'Dot Operator', symbol: '·' },

                // Greek Letters
                { category: 'greek', name: 'Alpha', symbol: 'α' },
                { category: 'greek', name: 'Beta', symbol: 'β' },
                { category: 'greek', name: 'Gamma', symbol: 'γ' },
                { category: 'greek', name: 'Delta (lower)', symbol: 'δ' },
                { category: 'greek', name: 'Delta (capital)', symbol: 'Δ' },
                { category: 'greek', name: 'Epsilon', symbol: 'ε' },
                { category: 'greek', name: 'Theta (lower)', symbol: 'θ' },
                { category: 'greek', name: 'Theta (capital)', symbol: 'Θ' },
                { category: 'greek', name: 'Lambda (lower)', symbol: 'λ' },
                { category: 'greek', name: 'Lambda (capital)', symbol: 'Λ' },
                { category: 'greek', name: 'Mu (micro)', symbol: 'μ' },
                { category: 'greek', name: 'Pi (lower)', symbol: 'π' },
                { category: 'greek', name: 'Pi (capital)', symbol: 'Π' },
                { category: 'greek', name: 'Rho', symbol: 'ρ' },
                { category: 'greek', name: 'Sigma (lower)', symbol: 'σ' },
                { category: 'greek', name: 'Sigma (capital)', symbol: 'Σ' },
                { category: 'greek', name: 'Tau', symbol: 'τ' },
                { category: 'greek', name: 'Phi (lower)', symbol: 'φ' },
                { category: 'greek', name: 'Phi (capital)', symbol: 'Φ' },
                { category: 'greek', name: 'Psi', symbol: 'ψ' },
                { category: 'greek', name: 'Omega (lower)', symbol: 'ω' },
                { category: 'greek', name: 'Omega (capital)', symbol: 'Ω' },

                // Fractions, Roots & Powers
                { category: 'fractions', name: 'One Half', symbol: '½' },
                { category: 'fractions', name: 'One Third', symbol: '⅓' },
                { category: 'fractions', name: 'Two Thirds', symbol: '⅔' },
                { category: 'fractions', name: 'One Quarter', symbol: '¼' },
                { category: 'fractions', name: 'Three Quarters', symbol: '¾' },
                { category: 'fractions', name: 'Square Root', symbol: '√' },
                { category: 'fractions', name: 'Cube Root', symbol: '∛' },
                { category: 'fractions', name: 'Fourth Root', symbol: '∜' },
                { category: 'fractions', name: 'Squared', symbol: '²' },
                { category: 'fractions', name: 'Cubed', symbol: '³' },
                { category: 'fractions', name: 'Power 4', symbol: '⁴' },
                { category: 'fractions', name: 'Power n', symbol: 'ⁿ' },
                { category: 'fractions', name: 'Subscript 0', symbol: '₀' },
                { category: 'fractions', name: 'Subscript 1', symbol: '₁' },
                { category: 'fractions', name: 'Subscript 2', symbol: '₂' },
                { category: 'fractions', name: 'Subscript 3', symbol: '₃' },
                { category: 'fractions', name: 'Subscript 4', symbol: '₄' },
                { category: 'fractions', name: 'Subscript n', symbol: 'ₙ' },

                // Calculus & Analysis
                { category: 'calculus', name: 'Summation', symbol: '∑' },
                { category: 'calculus', name: 'Product', symbol: '∏' },
                { category: 'calculus', name: 'Integral', symbol: '∫' },
                { category: 'calculus', name: 'Double Integral', symbol: '∬' },
                { category: 'calculus', name: 'Contour Integral', symbol: '∮' },
                { category: 'calculus', name: 'Partial Derivative', symbol: '∂' },
                { category: 'calculus', name: 'Nabla / Del', symbol: '∇' },

                // Sets & Logic
                { category: 'geometry', name: 'Element Of', symbol: '∈' },
                { category: 'geometry', name: 'Not Element Of', symbol: '∉' },
                { category: 'geometry', name: 'Subset Of', symbol: '⊂' },
                { category: 'geometry', name: 'Subset or Equal', symbol: '⊆' },
                { category: 'geometry', name: 'Union', symbol: '∪' },
                { category: 'geometry', name: 'Intersection', symbol: '∩' },
                { category: 'geometry', name: 'Empty Set', symbol: '∅' },
                { category: 'geometry', name: 'For All', symbol: '∀' },
                { category: 'geometry', name: 'There Exists', symbol: '∃' },
                { category: 'geometry', name: 'Therefore', symbol: '∴' },
                { category: 'geometry', name: 'Because', symbol: '∵' },

                // Geometry & Angles
                { category: 'geometry', name: 'Degree', symbol: '°' },
                { category: 'geometry', name: 'Angle', symbol: '∠' },
                { category: 'geometry', name: 'Measured Angle', symbol: '∡' },
                { category: 'geometry', name: 'Perpendicular', symbol: '⊥' },
                { category: 'geometry', name: 'Parallel', symbol: '∥' },
                { category: 'geometry', name: 'Triangle', symbol: '△' },
                { category: 'geometry', name: 'Congruent', symbol: '≅' },
                { category: 'geometry', name: 'Similar', symbol: '∼' },

                // Arrows
                { category: 'operators', name: 'Right Arrow', symbol: '→' },
                { category: 'operators', name: 'Left Arrow', symbol: '←' },
                { category: 'operators', name: 'Left-Right Arrow', symbol: '↔' },
                { category: 'operators', name: 'Implies', symbol: '⇒' },
                { category: 'operators', name: 'If and Only If', symbol: '⇔' }
            ];

            const mathFormulaTemplates = [
                // Chemistry Reaction & Equation Templates
                { name: 'Equilibrium Reaction', latex: 'a\\text{A} + b\\text{B} \\rightleftharpoons c\\text{C} + d\\text{D}', preview: 'A+B⇌C+D' },
                { name: 'Neutralization Reaction', latex: '\\text{HCl} + \\text{NaOH} \\rightarrow \\text{NaCl} + \\text{H}_2\\text{O}', preview: 'Acid+Base' },
                { name: 'Gas Evolution Reaction', latex: '\\text{Zn}_{(s)} + 2\\text{HCl}_{(aq)} \\rightarrow \\text{ZnCl}_{2(aq)} + \\text{H}_{2(g)}\\uparrow', preview: 'Gas (↑)' },
                { name: 'Precipitation Reaction', latex: '\\text{Ag}^+_{(aq)} + \\text{Cl}^-_{(aq)} \\rightarrow \\text{AgCl}_{(s)}\\downarrow', preview: 'Precip (↓)' },
                { name: 'Thermochemical Reaction', latex: '\\text{A} \\xrightarrow{\\Delta} \\text{B} + \\text{C}', preview: 'Heat (Δ)' },
                { name: 'Gibbs Free Energy Equation', latex: '\\Delta G^\\circ = \\Delta H^\\circ - T\\Delta S^\\circ', preview: 'ΔG=ΔH-TΔS' },
                { name: 'Nernst Equation', latex: 'E = E^\\circ - \\frac{RT}{nF} \\ln Q', preview: 'Nernst' },
                { name: 'Arrhenius Rate Equation', latex: 'k = A e^{-\\frac{E_a}{RT}}', preview: 'Arrhenius' },
                { name: 'Ideal Gas Law', latex: 'PV = nRT', preview: 'PV=nRT' },

                // Mathematical Templates
                { name: 'Fraction', latex: '\\frac{a}{b}', preview: 'a/b' },
                { name: 'Square Root', latex: '\\sqrt{x}', preview: '√x' },
                { name: 'n-th Root', latex: '\\sqrt[n]{x}', preview: 'ⁿ√x' },
                { name: 'Power / Exponent', latex: 'x^{2}', preview: 'x²' },
                { name: 'Subscript Index', latex: 'x_{1}', preview: 'x₁' },
                { name: 'Definite Integral', latex: '\\int_{a}^{b} f(x) \\, dx', preview: '∫f(x)dx' },
                { name: 'Summation Notation', latex: '\\sum_{i=1}^{n} x_i', preview: '∑x_i' },
                { name: 'Limit Notation', latex: '\\lim_{x \\to 0} f(x)', preview: 'lim f(x)' },
                { name: 'Quadratic Equation', latex: 'x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}', preview: 'Quadratic' }
            ];

            function renderMathSymbolsGrid(prefix, category = 'all', searchQuery = '') {
                const grid = document.getElementById(prefix + '_math_symbols_grid');
                if (!grid) return;

                grid.innerHTML = '';
                const q = (searchQuery || '').toLowerCase().trim();

                if (category === 'formulas') {
                    mathFormulaTemplates.forEach(item => {
                        if (q && !item.name.toLowerCase().includes(q) && !item.latex.toLowerCase().includes(q)) return;
                        const btn = document.createElement('button');
                        btn.type = 'button';
                        btn.className = 'px-2.5 py-1.5 rounded-lg bg-slate-900 hover:bg-indigo-600/30 border border-slate-700 hover:border-indigo-500/50 text-slate-200 text-xs font-mono transition-all flex items-center space-x-2 cursor-pointer shadow-sm active:scale-95';
                        btn.title = `Insert Formula: ${item.name} (${item.latex})`;
                        btn.innerHTML = `<span class="text-indigo-400 font-bold">${item.preview}</span><span class="text-[11px] text-slate-400 font-sans">${item.name}</span>`;
                        btn.onclick = () => insertMathSymbol(prefix, item.latex, true);
                        grid.appendChild(btn);
                    });
                    return;
                }

                const filtered = mathSymbolsData.filter(item => {
                    const matchesCat = category === 'all' || item.category === category;
                    const matchesSearch = !q || item.name.toLowerCase().includes(q) || item.symbol.toLowerCase().includes(q);
                    return matchesCat && matchesSearch;
                });

                if (filtered.length === 0) {
                    grid.innerHTML = '<span class="text-xs text-slate-500 italic p-2 w-full text-center">No symbols found matching "' + searchQuery + '"</span>';
                    return;
                }

                filtered.forEach(item => {
                    const btn = document.createElement('button');
                    btn.type = 'button';
                    btn.className = 'min-w-[2rem] h-8 px-2 rounded-lg bg-slate-900 hover:bg-indigo-600 hover:text-white border border-slate-800 hover:border-indigo-500 text-slate-200 font-medium text-xs flex items-center justify-center transition-all cursor-pointer shadow-sm active:scale-95 shrink-0 select-none';
                    btn.title = `${item.name} (${item.symbol})`;
                    btn.textContent = item.symbol;
                    btn.onclick = () => insertMathSymbol(prefix, item.symbol, false);
                    grid.appendChild(btn);
                });
            }

            function toggleMathPalette(prefix) {
                const palette = document.getElementById(prefix + '_math_palette');
                if (!palette) return;

                if (palette.classList.contains('hidden')) {
                    palette.classList.remove('hidden');
                    const activeBtn = document.querySelector(`#${prefix}_math_tabs button.active`);
                    let curCat = 'all';
                    if (activeBtn) {
                        const match = activeBtn.getAttribute('onclick')?.match(/selectMathTab\('[^']+',\s*'([^']+)'/);
                        if (match) curCat = match[1];
                    }
                    renderMathSymbolsGrid(prefix, curCat, '');
                    const searchInput = document.getElementById(prefix + '_math_search');
                    if (searchInput) searchInput.value = '';
                } else {
                    palette.classList.add('hidden');
                }
            }

            function selectMathTab(prefix, category, btn) {
                const container = document.getElementById(prefix + '_math_tabs');
                if (container) {
                    container.querySelectorAll('button').forEach(b => {
                        b.classList.remove('bg-indigo-600', 'text-white', 'active');
                        b.classList.add('bg-slate-800', 'text-slate-300');
                    });
                    if (btn) {
                        btn.classList.remove('bg-slate-800', 'text-slate-300');
                        btn.classList.add('bg-indigo-600', 'text-white', 'active');
                    }
                }
                const searchVal = document.getElementById(prefix + '_math_search')?.value || '';
                renderMathSymbolsGrid(prefix, category, searchVal);
            }

            function filterMathSymbols(prefix, query) {
                const activeBtn = document.querySelector(`#${prefix}_math_tabs button.active`);
                let category = 'all';
                if (activeBtn) {
                    const match = activeBtn.getAttribute('onclick')?.match(/selectMathTab\('[^']+',\s*'([^']+)'/);
                    if (match) category = match[1];
                }
                renderMathSymbolsGrid(prefix, category, query);
            }

            function insertMathSymbol(prefix, content, isFormula = false) {
                const targetQuill = prefix === 'edit' ? editQuill : createQuill;
                if (!targetQuill) return;

                targetQuill.focus();
                let range = targetQuill.getSelection();
                if (!range) {
                    range = { index: targetQuill.getLength() - 1, length: 0 };
                }

                if (isFormula) {
                    targetQuill.insertEmbed(range.index, 'formula', content, 'user');
                    targetQuill.setSelection(range.index + 1, 0);
                } else {
                    targetQuill.insertText(range.index, content, 'user');
                    targetQuill.setSelection(range.index + content.length, 0);
                }

                // Sync to hidden input
                const text = targetQuill.getText().trim();
                const hasImage = targetQuill.root.querySelector('img') !== null;
                const targetInputId = prefix === 'edit' ? 'edit_q_name' : 'create_q_name';
                document.getElementById(targetInputId).value = (text.length > 0 || hasImage) ? targetQuill.root.innerHTML : '';
                
                const clientErr = document.getElementById(prefix + '_q_name_client_error');
                if (clientErr) clientErr.classList.add('hidden');
                const container = document.getElementById(prefix + '_q_editor_container');
                if (container) container.classList.remove('border-red-500', 'ring-1', 'ring-red-500');
            }

            const quillToolbarOptions = [
                [{ 'header': [2, 3, false] }],
                ['bold', 'italic', 'underline', 'strike'],
                [{ 'script': 'sub' }, { 'script': 'super' }],
                [{ 'list': 'ordered' }, { 'list': 'bullet' }],
                ['blockquote', 'code-block'],
                ['formula', 'image'],
                ['clean']
            ];

            function initQuillEditors() {
                if (typeof Quill === 'undefined') {
                    return;
                }

                // Initialize Create Modal Quill
                const createEditorElem = document.getElementById('create_q_editor');
                if (createEditorElem && !createQuill) {
                    createQuill = new Quill('#create_q_editor', {
                        theme: 'snow',
                        placeholder: 'Enter rich question prompt (supports formatting, formulas, geometry drawings, subscripts, superscripts, lists)...',
                        modules: { toolbar: quillToolbarOptions }
                    });
                    window.createQuill = createQuill;

                    // Image icon in toolbar opens Draw Tool
                    const createToolbar = createQuill.getModule('toolbar');
                    if (createToolbar) {
                        createToolbar.addHandler('image', function() {
                            if (typeof openDrawToolModal === 'function') {
                                openDrawToolModal('create');
                            }
                        });
                    }

                    const initVal = document.getElementById('create_q_name').value;
                    if (initVal) {
                        createQuill.root.innerHTML = initVal;
                    }

                    createQuill.on('text-change', function() {
                        const text = createQuill.getText().trim();
                        const hasImg = createQuill.root.querySelector('img') !== null;
                        const clientErr = document.getElementById('create_q_name_client_error');
                        const container = document.getElementById('create_q_editor_container');
                        if (text.length > 0 || hasImg) {
                            document.getElementById('create_q_name').value = createQuill.root.innerHTML;
                            if (clientErr) clientErr.classList.add('hidden');
                            if (container) container.classList.remove('border-red-500', 'ring-1', 'ring-red-500');
                        } else {
                            document.getElementById('create_q_name').value = '';
                        }
                    });
                }

                // Initialize Edit Modal Quill
                const editEditorElem = document.getElementById('edit_q_editor');
                if (editEditorElem && !editQuill) {
                    editQuill = new Quill('#edit_q_editor', {
                        theme: 'snow',
                        placeholder: 'Enter question prompt...',
                        modules: { toolbar: quillToolbarOptions }
                    });
                    window.editQuill = editQuill;

                    // Image icon in toolbar opens Draw Tool
                    const editToolbar = editQuill.getModule('toolbar');
                    if (editToolbar) {
                        editToolbar.addHandler('image', function() {
                            if (typeof openDrawToolModal === 'function') {
                                openDrawToolModal('edit');
                            }
                        });
                    }

                    const initVal = document.getElementById('edit_q_name').value;
                    if (initVal) {
                        editQuill.root.innerHTML = initVal;
                    }

                    editQuill.on('text-change', function() {
                        const text = editQuill.getText().trim();
                        const hasImg = editQuill.root.querySelector('img') !== null;
                        const clientErr = document.getElementById('edit_q_name_client_error');
                        const container = document.getElementById('edit_q_editor_container');
                        if (text.length > 0 || hasImg) {
                            document.getElementById('edit_q_name').value = editQuill.root.innerHTML;
                            if (clientErr) clientErr.classList.add('hidden');
                            if (container) container.classList.remove('border-red-500', 'ring-1', 'ring-red-500');
                        } else {
                            document.getElementById('edit_q_name').value = '';
                        }
                    });
                }

                // Setup create form submission intercept
                const createForm = document.getElementById('createQuestionForm');
                if (createForm && !createForm.dataset.quillBound) {
                    createForm.dataset.quillBound = "true";
                    createForm.addEventListener('submit', function(e) {
                        if (createQuill) {
                            const text = createQuill.getText().trim();
                            const hasImg = createQuill.root.querySelector('img') !== null;
                            const clientErr = document.getElementById('create_q_name_client_error');
                            const container = document.getElementById('create_q_editor_container');
                            if (text.length === 0 && !hasImg) {
                                e.preventDefault();
                                document.getElementById('create_q_name').value = '';
                                if (clientErr) clientErr.classList.remove('hidden');
                                if (container) container.classList.add('border-red-500', 'ring-1', 'ring-red-500');
                                createQuill.focus();
                                return false;
                            } else {
                                document.getElementById('create_q_name').value = createQuill.root.innerHTML;
                                if (clientErr) clientErr.classList.add('hidden');
                                if (container) container.classList.remove('border-red-500', 'ring-1', 'ring-red-500');
                            }
                        }
                    });
                }

                // Setup edit form submission intercept
                const editForm = document.getElementById('editQuestionForm');
                if (editForm && !editForm.dataset.quillBound) {
                    editForm.dataset.quillBound = "true";
                    editForm.addEventListener('submit', function(e) {
                        if (editQuill) {
                            const text = editQuill.getText().trim();
                            const hasImg = editQuill.root.querySelector('img') !== null;
                            const clientErr = document.getElementById('edit_q_name_client_error');
                            const container = document.getElementById('edit_q_editor_container');
                            if (text.length === 0 && !hasImg) {
                                e.preventDefault();
                                document.getElementById('edit_q_name').value = '';
                                if (clientErr) clientErr.classList.remove('hidden');
                                if (container) container.classList.add('border-red-500', 'ring-1', 'ring-red-500');
                                editQuill.focus();
                                return false;
                            } else {
                                document.getElementById('edit_q_name').value = editQuill.root.innerHTML;
                                if (clientErr) clientErr.classList.add('hidden');
                                if (container) container.classList.remove('border-red-500', 'ring-1', 'ring-red-500');
                            }
                        }
                    });
                }
            }

            function openCreateQuestionModal() {
                initQuillEditors();
                document.getElementById('createQuestionModal').classList.remove('hidden');
                if (createQuill) {
                    setTimeout(() => createQuill.focus(), 80);
                }
            }

            function closeCreateQuestionModal() {
                document.getElementById('createQuestionModal').classList.add('hidden');
                const mathPal = document.getElementById('create_math_palette');
                if (mathPal) mathPal.classList.add('hidden');
            }

            function openEditQuestionModal(data) {
                initQuillEditors();
                const actionUrl = '/questions/' + data.id;
                document.getElementById('editQuestionForm').action = actionUrl;
                document.getElementById('edit_action_url').value = actionUrl;
                
                const qContent = data.name || '';
                document.getElementById('edit_q_name').value = qContent;
                if (editQuill) {
                    editQuill.root.innerHTML = qContent;
                }

                document.getElementById('edit_q_desc').value = data.description || '';
                document.getElementById('edit_q_hint').value = data.hint || '';
                document.getElementById('edit_q_solution').value = data.solution || '';
                document.getElementById('edit_q_standard').value = data.standard_id || '';
                document.getElementById('edit_q_type').value = data.type || 1;
                document.getElementById('edit_q_marks').value = data.marks !== undefined ? data.marks : 1;

                // Cascading Subject, Chapter, Topic selections
                document.getElementById('edit_subject').value = data.subject_id || '';
                filterChapters('edit', data.subject_id || '', data.chapter_id || '');
                filterTopics('edit', data.chapter_id || '', data.topic_id || '');

                toggleAnswersSection('edit', data.type || 1);

                // Pre-fill answer slots
                const answers = data.answers || [];
                if (parseInt(data.type) === 4) {
                    const trueAns = answers.find(a => (a.name || '').trim().toLowerCase() === 'true');
                    const falseAns = answers.find(a => (a.name || '').trim().toLowerCase() === 'false');

                    const inp0 = document.getElementById('edit_ans_0_name');
                    const chk0 = document.getElementById('edit_ans_0_correct');
                    const inp1 = document.getElementById('edit_ans_1_name');
                    const chk1 = document.getElementById('edit_ans_1_correct');

                    if (inp0) {
                        inp0.value = 'True';
                        inp0.readOnly = true;
                    }
                    if (chk0) chk0.checked = trueAns ? parseInt(trueAns.is_correct) === 1 : true;

                    if (inp1) {
                        inp1.value = 'False';
                        inp1.readOnly = true;
                    }
                    if (chk1) chk1.checked = falseAns ? parseInt(falseAns.is_correct) === 1 : false;

                    if (chk0 && chk1 && !chk0.checked && !chk1.checked) {
                        chk0.checked = true;
                    }
                } else if (parseInt(data.type) === 5) {
                    for (let i = 0; i < 4; i++) {
                        const ansInput = document.getElementById('edit_ans_' + i + '_name');
                        const matchInput = document.getElementById('edit_ans_' + i + '_match');
                        if (i < answers.length) {
                            if (ansInput) ansInput.value = answers[i].name || '';
                            if (matchInput) matchInput.value = answers[i].match_answer || '';
                        } else {
                            if (ansInput) ansInput.value = '';
                            if (matchInput) matchInput.value = '';
                        }
                    }
                    if (data.marks !== undefined && parseInt(data.marks) > 0) {
                        document.getElementById('edit_q_marks').value = data.marks;
                    } else {
                        updateMatchMarks('edit');
                    }
                } else {
                    for (let i = 0; i < 4; i++) {
                        const ansInput = document.getElementById('edit_ans_' + i + '_name');
                        const ansCorrect = document.getElementById('edit_ans_' + i + '_correct');
                        if (i < answers.length) {
                            ansInput.value = answers[i].name || '';
                            ansCorrect.checked = parseInt(answers[i].is_correct) === 1;
                        } else {
                            ansInput.value = '';
                            ansCorrect.checked = false;
                        }
                    }
                }

                document.getElementById('editQuestionModal').classList.remove('hidden');
                if (editQuill) {
                    setTimeout(() => editQuill.focus(), 80);
                }
            }

            function closeEditQuestionModal() {
                document.getElementById('editQuestionModal').classList.add('hidden');
                const mathPal = document.getElementById('edit_math_palette');
                if (mathPal) mathPal.classList.add('hidden');
            }

            let currentViewQuestionData = null;

            function openViewQuestionModal(data) {
                currentViewQuestionData = data;
                if (!data) return;

                // Header badges
                const badgeId = document.getElementById('vq_badge_id');
                const badgeType = document.getElementById('vq_badge_type');
                const badgeMarks = document.getElementById('vq_badge_marks');

                if (badgeId) badgeId.textContent = '#' + (data.id || '');

                const typeNum = parseInt(data.type) || 1;
                const typeLabels = {
                    1: 'Single Choice (MCQ)',
                    2: 'Multiple Choice',
                    3: 'Text Entry',
                    4: 'True / False',
                    5: 'Match the Following'
                };
                if (badgeType) badgeType.textContent = typeLabels[typeNum] || 'Single Choice';

                const marksCount = data.marks !== undefined && data.marks !== null ? data.marks : 1;
                if (badgeMarks) badgeMarks.textContent = marksCount + (parseInt(marksCount) === 1 ? ' Mark' : ' Marks');

                // Curriculum breadcrumbs
                const sylEl = document.getElementById('vq_syllabus');
                const stdEl = document.getElementById('vq_standard');
                const subjEl = document.getElementById('vq_subject');
                const chEl = document.getElementById('vq_chapter');
                const topEl = document.getElementById('vq_topic');

                if (sylEl) sylEl.textContent = 'Syllabus: ' + (data.syllabus_name || 'CBSE');
                if (stdEl) stdEl.textContent = 'Class: ' + (data.standard_name || 'General');
                if (subjEl) subjEl.textContent = 'Subject: ' + (data.subject_name || 'General');
                if (chEl) chEl.textContent = 'Chapter: ' + (data.chapter_name || 'General');
                if (topEl) topEl.textContent = 'Topic: ' + (data.topic_name || 'General');

                // Question Prompt
                const promptEl = document.getElementById('vq_prompt');
                if (promptEl) {
                    promptEl.innerHTML = data.name || '<span class="text-slate-500 italic">No question prompt text available.</span>';
                }

                // Description
                const descCont = document.getElementById('vq_desc_container');
                const descEl = document.getElementById('vq_desc');
                if (data.description && data.description.trim() !== '') {
                    if (descCont) descCont.classList.remove('hidden');
                    if (descEl) descEl.textContent = data.description;
                } else {
                    if (descCont) descCont.classList.add('hidden');
                }

                // Answers & Options
                const answersCont = document.getElementById('vq_answers_container');
                if (answersCont) {
                    answersCont.innerHTML = '';
                    const answers = data.answers || [];

                    if (typeNum === 3) {
                        answersCont.innerHTML = `
                            <div class="p-4 rounded-2xl bg-slate-950/50 border border-slate-800 text-slate-400 text-xs flex items-center space-x-2.5">
                                <span class="text-base">✍️</span>
                                <div>
                                    <span class="font-semibold text-slate-200">Text Entry Question:</span>
                                    <span> Students formulate and type their custom response directly into the text field.</span>
                                </div>
                            </div>
                        `;
                    } else if (typeNum === 4) {
                        const trueAns = answers.find(a => (a.name || '').trim().toLowerCase() === 'true');
                        const falseAns = answers.find(a => (a.name || '').trim().toLowerCase() === 'false');
                        const isTrueCorrect = trueAns && parseInt(trueAns.is_correct) === 1;
                        const isFalseCorrect = falseAns && parseInt(falseAns.is_correct) === 1;

                        answersCont.innerHTML = `
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                                <div class="p-4 rounded-2xl border transition-all flex items-center justify-between ${isTrueCorrect ? 'bg-emerald-500/10 border-emerald-500/40 text-emerald-200 shadow-md shadow-emerald-500/5' : 'bg-slate-950/60 border-slate-800 text-slate-300'}">
                                    <div class="flex items-center space-x-3">
                                        <span class="w-8 h-8 rounded-xl font-black text-sm flex items-center justify-center ${isTrueCorrect ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30' : 'bg-slate-800 text-slate-400'}">T</span>
                                        <span class="font-semibold text-sm">True</span>
                                    </div>
                                    ${isTrueCorrect ? '<span class="px-2.5 py-1 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 flex items-center space-x-1"><span>✓</span><span>Correct Answer</span></span>' : ''}
                                </div>

                                <div class="p-4 rounded-2xl border transition-all flex items-center justify-between ${isFalseCorrect ? 'bg-emerald-500/10 border-emerald-500/40 text-emerald-200 shadow-md shadow-emerald-500/5' : 'bg-slate-950/60 border-slate-800 text-slate-300'}">
                                    <div class="flex items-center space-x-3">
                                        <span class="w-8 h-8 rounded-xl font-black text-sm flex items-center justify-center ${isFalseCorrect ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30' : 'bg-slate-800 text-slate-400'}">F</span>
                                        <span class="font-semibold text-sm">False</span>
                                    </div>
                                    ${isFalseCorrect ? '<span class="px-2.5 py-1 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 flex items-center space-x-1"><span>✓</span><span>Correct Answer</span></span>' : ''}
                                </div>
                            </div>
                        `;
                    } else if (typeNum === 5) {
                        let pairsHtml = '<div class="space-y-2.5">';
                        if (answers.length === 0) {
                            pairsHtml += '<div class="p-4 rounded-xl bg-slate-950/40 border border-slate-800 text-xs text-slate-500 italic">No matching pairs recorded.</div>';
                        } else {
                            answers.forEach((ans, idx) => {
                                const letter = String.fromCharCode(65 + idx);
                                pairsHtml += `
                                    <div class="p-3.5 rounded-2xl bg-slate-950/70 border border-slate-800 flex flex-col sm:flex-row sm:items-center justify-between gap-2.5">
                                        <div class="flex items-center space-x-3">
                                            <span class="w-7 h-7 rounded-xl font-black text-xs flex items-center justify-center bg-cyan-500/15 text-cyan-300 border border-cyan-500/30">${letter}</span>
                                            <span class="text-sm font-medium text-slate-200">${ans.name || '<span class="text-slate-500 italic">Empty</span>'}</span>
                                        </div>
                                        <div class="flex items-center space-x-2.5 pl-10 sm:pl-0">
                                            <span class="text-slate-500 text-xs">&harr; matches to &rarr;</span>
                                            <span class="px-3 py-1 rounded-xl bg-emerald-500/15 text-emerald-300 border border-emerald-500/30 text-xs font-semibold">${ans.match_answer || '<span class="text-slate-500 italic">Empty</span>'}</span>
                                        </div>
                                    </div>
                                `;
                            });
                        }
                        pairsHtml += '</div>';
                        answersCont.innerHTML = pairsHtml;
                    } else {
                        // Single (1) or Multiple (2) MCQ
                        let mcqHtml = '<div class="space-y-2.5">';
                        if (answers.length === 0) {
                            mcqHtml += '<div class="p-4 rounded-xl bg-slate-950/40 border border-slate-800 text-xs text-slate-500 italic">No answer choices configured for this question.</div>';
                        } else {
                            answers.forEach((ans, idx) => {
                                const letter = String.fromCharCode(65 + idx);
                                const isCorrect = parseInt(ans.is_correct) === 1;
                                mcqHtml += `
                                    <div class="p-3.5 sm:p-4 rounded-2xl border transition-all flex items-center justify-between gap-3 ${isCorrect ? 'bg-emerald-500/10 border-emerald-500/40 text-emerald-200 shadow-md shadow-emerald-500/5' : 'bg-slate-950/60 border-slate-800 text-slate-300'}">
                                        <div class="flex items-center space-x-3.5 flex-1 min-w-0">
                                            <span class="w-8 h-8 rounded-xl font-black text-xs shrink-0 flex items-center justify-center ${isCorrect ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/40' : 'bg-slate-800 text-slate-400 border border-slate-700/60'}">
                                                ${letter}
                                            </span>
                                            <span class="text-sm font-medium break-words">${ans.name || ''}</span>
                                        </div>
                                        ${isCorrect ? `
                                            <span class="shrink-0 px-3 py-1 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 inline-flex items-center space-x-1">
                                                <span>✓</span>
                                                <span class="hidden sm:inline">Correct Answer</span>
                                                <span class="sm:hidden">Correct</span>
                                            </span>
                                        ` : ''}
                                    </div>
                                `;
                            });
                        }
                        mcqHtml += '</div>';
                        answersCont.innerHTML = mcqHtml;
                    }
                }

                // Hint
                const hintCont = document.getElementById('vq_hint_container');
                const hintText = document.getElementById('vq_hint_text');
                if (data.hint && data.hint.trim() !== '') {
                    if (hintCont) hintCont.classList.remove('hidden');
                    if (hintText) hintText.textContent = data.hint;
                } else {
                    if (hintCont) hintCont.classList.add('hidden');
                }

                // Solution
                const solCont = document.getElementById('vq_solution_container');
                const solText = document.getElementById('vq_solution_text');
                if (data.solution && data.solution.trim() !== '') {
                    if (solCont) solCont.classList.remove('hidden');
                    if (solText) solText.textContent = data.solution;
                } else {
                    if (solCont) solCont.classList.add('hidden');
                }

                // Metadata
                const creatorEl = document.getElementById('vq_creator');
                const dateEl = document.getElementById('vq_date');
                if (creatorEl) creatorEl.textContent = data.creator_name || 'System / Teacher';
                if (dateEl) dateEl.textContent = data.created_at || 'Recently';

                // Open modal
                const modal = document.getElementById('viewQuestionModal');
                if (modal) modal.classList.remove('hidden');
            }

            function closeViewQuestionModal() {
                const modal = document.getElementById('viewQuestionModal');
                if (modal) modal.classList.add('hidden');
            }

            function editCurrentViewQuestion() {
                if (!currentViewQuestionData) return;
                closeViewQuestionModal();
                openEditQuestionModal(currentViewQuestionData);
            }

            function toggleFilterDrawer() {
                const drawer = document.getElementById('filterDrawerContent');
                const chevron = document.getElementById('filterDrawerChevron');
                const btnText = document.getElementById('filterToggleBtnText');
                if (!drawer) return;

                if (drawer.classList.contains('hidden')) {
                    drawer.classList.remove('hidden');
                    if (chevron) chevron.classList.add('rotate-180');
                    if (btnText) btnText.textContent = 'Hide Filters';
                } else {
                    drawer.classList.add('hidden');
                    if (chevron) chevron.classList.remove('rotate-180');
                    if (btnText) btnText.textContent = 'Filters';
                }
            }

            // Maintain current filter selections on page load and initialize editors
            document.addEventListener('DOMContentLoaded', function() {
                try {
                    initQuillEditors();
                } catch (e) {
                    console.warn('Quill editor initialization skipped:', e);
                }

                const filterForm = document.getElementById('questionFilterForm');
                if (filterForm) {
                    filterForm.addEventListener('submit', function() {
                        const inputs = filterForm.querySelectorAll('input, select');
                        inputs.forEach(input => {
                            if (!input.value || input.value.trim() === '') {
                                input.disabled = true;
                            }
                        });
                        return true;
                    });
                }

                const currentSyl = "{{ request('syllabus_id') }}";
                const currentStd = "{{ request('standard_id') }}";
                const currentSubj = "{{ request('subject_id') }}";
                const currentChap = "{{ request('chapter_id') }}";
                const currentTopic = "{{ request('topic_id') }}";

                if (currentSyl) {
                    filterStandardsBySyllabus('filter', currentSyl);
                    if (currentStd) {
                        const stdSelect = document.getElementById('filter_standard');
                        if (stdSelect) stdSelect.value = currentStd;
                    }
                }

                if (currentSubj) {
                    filterChapters('filter', currentSubj, currentChap, currentTopic);
                } else if (currentChap) {
                    filterTopics('filter', currentChap, currentTopic);
                }
            });

            window.addEventListener('pageshow', function() {
                const filterForm = document.getElementById('questionFilterForm');
                if (filterForm) {
                    filterForm.querySelectorAll('input, select').forEach(input => input.disabled = false);
                }
            });

            @if($isEditModalOpen)
                document.addEventListener('DOMContentLoaded', function() {
                    toggleAnswersSection('edit', "{{ old('type', 1) }}");
                    filterChapters('edit', "{{ old('subject_id') }}", "{{ old('chapter_id') }}");
                    filterTopics('edit', "{{ old('chapter_id') }}", "{{ old('topic_id') }}");
                });
            @endif

            @if($isCreateModalOpen)
                document.addEventListener('DOMContentLoaded', function() {
                    toggleAnswersSection('create', "{{ old('type', 1) }}");
                    filterChapters('create', "{{ old('subject_id') }}", "{{ old('chapter_id') }}");
                    filterTopics('create', "{{ old('chapter_id') }}", "{{ old('topic_id') }}");
                });
            @endif
        </script>

    </div>
</x-layouts.app>
