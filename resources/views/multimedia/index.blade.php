<x-layouts.app title="Textbook Multimedia Curriculum Tree - Study App">
    <div class="py-6 w-full px-4 sm:px-6 lg:px-8 space-y-6">

        <!-- Top Breadcrumb & Hero Header -->
        <div class="relative overflow-hidden rounded-2xl bg-gradient-to-r from-emerald-950/80 via-slate-900 to-indigo-950/80 border border-emerald-500/30 p-6 sm:p-8 shadow-2xl">
            <!-- Decorative Orbs -->
            <div class="absolute -top-12 -right-12 w-64 h-64 rounded-full bg-emerald-500/10 blur-3xl pointer-events-none"></div>
            <div class="absolute -bottom-10 left-16 w-56 h-56 rounded-full bg-indigo-500/10 blur-3xl pointer-events-none"></div>

            <div class="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-6">
                <div class="space-y-2">
                    <div class="flex items-center space-x-2 flex-wrap gap-y-1">
                        <a href="{{ route('dashboard') }}" class="text-xs font-semibold text-slate-400 hover:text-white transition-colors">
                            ← Back to Dashboard
                        </a>
                        <span class="text-xs text-slate-600">•</span>
                        <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
                            🌳 Curriculum Tree Explorer
                        </span>
                        <span class="text-xs text-slate-600">•</span>
                        <span class="text-xs font-mono text-cyan-300">NCERT / CBSE / SCERT Kerala Framework</span>
                    </div>

                    <h1 class="text-2xl sm:text-3xl font-black text-white tracking-tight flex items-center space-x-2.5">
                        <span>📚</span>
                        <span>Textbook Multimedia Curriculum Tree</span>
                    </h1>
                    <p class="text-xs sm:text-sm text-slate-300 max-w-3xl leading-relaxed">
                        Explore interactive multimedia animations arranged strictly by textbook hierarchy: 
                        <strong class="text-emerald-300">Syllabus</strong> (NCERT, CBSE, SCERT Kerala) &rarr; 
                        <strong class="text-cyan-300">Subject</strong> (English, Mathematics, Science) &rarr; 
                        <strong class="text-indigo-300">Class</strong> (1 to 10) &rarr; 
                        <strong class="text-amber-300">Chapters</strong>.
                    </p>
                </div>

                <!-- Global Stats Card -->
                <div class="flex items-center gap-3 shrink-0 flex-wrap sm:flex-nowrap">
                    <div class="px-4 py-3 rounded-xl bg-slate-950/70 border border-slate-800 text-center shadow-md">
                        <div class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Total Chapters</div>
                        <div class="text-xl font-mono font-black text-white">{{ $totalChaptersCount }}</div>
                    </div>
                    <div class="px-4 py-3 rounded-xl bg-emerald-950/60 border border-emerald-500/40 text-center shadow-md">
                        <div class="text-[11px] font-bold uppercase tracking-wider text-emerald-400">Interactive Labs</div>
                        <div class="text-xl font-mono font-black text-emerald-300 flex items-center justify-center space-x-1">
                            <span>🎬</span>
                            <span>{{ $totalMediaCount }}</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Interactive Textbook Selector Filter Bar -->
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-xl space-y-4">
            
            <!-- Step 1: Select Syllabus -->
            <div class="space-y-2">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-black uppercase tracking-wider text-slate-400 flex items-center space-x-1.5">
                        <span class="w-5 h-5 rounded-full bg-slate-800 text-emerald-400 font-bold flex items-center justify-center text-[10px]">1</span>
                        <span>Select Syllabus:</span>
                    </span>
                    <span class="text-[11px] text-slate-500">Board / Educational Framework</span>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
                    @foreach($syllabuses as $sId => $sData)
                        @php $isSylActive = ($selectedSyllabus === $sId); @endphp
                        <a href="{{ route('multimedia.index', ['syllabus' => $sId, 'subject' => $selectedSubject, 'class' => $selectedClass]) }}"
                           class="p-3.5 rounded-xl border transition-all flex items-center justify-between {{ $isSylActive ? 'bg-emerald-950/60 border-emerald-500/60 text-white shadow-lg shadow-emerald-950/50' : 'bg-slate-950/60 border-slate-800 text-slate-300 hover:border-slate-700 hover:text-white' }}">
                            <div class="flex items-center space-x-3">
                                <span class="text-2xl">{{ $sId === 'ncert' ? '📘' : ($sId === 'cbse' ? '🏛️' : '🌴') }}</span>
                                <div>
                                    <h4 class="text-sm font-bold {{ $isSylActive ? 'text-emerald-300' : 'text-slate-200' }}">{{ $sData['name'] }}</h4>
                                    <p class="text-[11px] text-slate-400">{{ $sData['badge'] }}</p>
                                </div>
                            </div>
                            @if($isSylActive)
                                <span class="w-5 h-5 rounded-full bg-emerald-500 text-slate-950 flex items-center justify-center text-xs font-black">✓</span>
                            @endif
                        </a>
                    @endforeach
                </div>
            </div>

            <div class="border-t border-slate-800/80"></div>

            <!-- Step 2: Select Subject -->
            <div class="space-y-2">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-black uppercase tracking-wider text-slate-400 flex items-center space-x-1.5">
                        <span class="w-5 h-5 rounded-full bg-slate-800 text-cyan-400 font-bold flex items-center justify-center text-[10px]">2</span>
                        <span>Select Subject:</span>
                    </span>
                    <span class="text-[11px] text-slate-500">English • Mathematics • Science</span>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
                    @foreach($subjects as $subId => $subData)
                        @php $isSubActive = ($selectedSubject === $subId); @endphp
                        <a href="{{ route('multimedia.index', ['syllabus' => $selectedSyllabus, 'subject' => $subId, 'class' => $selectedClass]) }}"
                           class="p-3 rounded-xl border transition-all flex items-center justify-between {{ $isSubActive ? 'bg-cyan-950/60 border-cyan-500/60 text-white shadow-lg shadow-cyan-950/50' : 'bg-slate-950/60 border-slate-800 text-slate-300 hover:border-slate-700 hover:text-white' }}">
                            <div class="flex items-center space-x-2.5">
                                <span class="text-xl">{{ $subData['icon'] }}</span>
                                <span class="text-sm font-bold {{ $isSubActive ? 'text-cyan-300' : 'text-slate-200' }}">{{ $subData['name'] }}</span>
                            </div>
                            @if($isSubActive)
                                <span class="w-4 h-4 rounded-full bg-cyan-400 text-slate-950 flex items-center justify-center text-[10px] font-black">✓</span>
                            @endif
                        </a>
                    @endforeach
                </div>
            </div>

            <div class="border-t border-slate-800/80"></div>

            <!-- Step 3: Select Class / Standard -->
            <div class="space-y-2">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-black uppercase tracking-wider text-slate-400 flex items-center space-x-1.5">
                        <span class="w-5 h-5 rounded-full bg-slate-800 text-indigo-400 font-bold flex items-center justify-center text-[10px]">3</span>
                        <span>Select Class (Standard 1 to 12):</span>
                    </span>
                    <span class="text-[11px] text-slate-500">Primary • Middle • Secondary • Higher Secondary</span>
                </div>
                <div class="flex items-center gap-2 overflow-x-auto pb-2 scrollbar-none">
                    @foreach($classes as $cId => $cData)
                        @php $isClassActive = ($selectedClass === $cId); @endphp
                        <a href="{{ route('multimedia.index', ['syllabus' => $selectedSyllabus, 'subject' => $selectedSubject, 'class' => $cId]) }}"
                           class="px-3.5 py-2 rounded-xl text-xs font-bold shrink-0 border transition-all flex items-center space-x-1.5 {{ $isClassActive ? 'bg-indigo-600 text-white border-indigo-400 shadow-md shadow-indigo-600/30 scale-105' : 'bg-slate-950 border-slate-800 text-slate-400 hover:text-white hover:border-slate-700' }}">
                            <span>🎓</span>
                            <span>{{ $cData['name'] }}</span>
                            @if(in_array($cId, ['class9', 'class10', 'class12']) && $selectedSyllabus === 'ncert' && $selectedSubject === 'mathematics')
                                <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" title="Multimedia Lab Ready"></span>
                            @endif
                        </a>
                    @endforeach
                </div>
            </div>
        </div>

        <!-- CURRENT SELECTION & CONTENT SECTION -->
        <div class="space-y-4">
            
            <!-- Breadcrumb Path Status Banner -->
            <div class="p-3.5 sm:p-4 rounded-xl bg-slate-900 border border-slate-800 flex flex-col sm:flex-row sm:items-center justify-between gap-3 text-xs">
                <div class="flex items-center space-x-2 font-mono flex-wrap">
                    <span class="text-slate-400 font-sans font-bold">Selected Path:</span>
                    <span class="px-2.5 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-bold uppercase">{{ $selectedSyllabus }}</span>
                    <span class="text-slate-600">&rarr;</span>
                    <span class="px-2.5 py-0.5 rounded bg-cyan-500/20 text-cyan-300 font-bold capitalize">{{ $selectedSubject }}</span>
                    <span class="text-slate-600">&rarr;</span>
                    <span class="px-2.5 py-0.5 rounded bg-indigo-500/20 text-indigo-300 font-bold capitalize">{{ $classes[$selectedClass]['name'] ?? $selectedClass }}</span>
                </div>

                <div class="flex items-center space-x-2 shrink-0">
                    @if($hasAnyMultimedia)
                        <span class="inline-flex items-center px-2.5 py-1 rounded-full text-xs font-black bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">
                            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse mr-1.5"></span>
                            Interactive Labs Available
                        </span>
                    @else
                        <!-- EXACT SPECIFICATION REQUIREMENT: <syllabus>-<subject>-<class> - empty -->
                        <span class="inline-flex items-center px-2.5 py-1 rounded-full text-xs font-mono font-bold bg-amber-500/10 text-amber-300 border border-amber-500/30">
                            {{ $selectedSyllabus }}-{{ $selectedSubject }}-{{ $selectedClass }} - empty
                        </span>
                    @endif
                </div>
            </div>

            <!-- CHAPTERS / MULTIMEDIA CONTENT STAGE -->
            @if(count($activeChapters) > 0)
                <div class="space-y-4">
                    <div class="flex items-center justify-between">
                        <h3 class="text-base font-bold text-white flex items-center space-x-2 flex-wrap">
                            <span>📖</span>
                            <span>Chapters for {{ strtoupper($selectedSyllabus) }} • {{ ucfirst($selectedSubject) }} • {{ $classes[$selectedClass]['name'] ?? $selectedClass }}</span>
                            @if($selectedClass === 'class12')
                                <span class="px-2 py-0.5 rounded text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 uppercase tracking-wider">Part - 1 & Part - 2</span>
                            @endif
                        </h3>
                        <span class="text-xs text-slate-400">{{ count($activeChapters) }} Chapter(s) in Curriculum</span>
                    </div>

                    <div class="grid grid-cols-1 gap-4">
                        @foreach($activeChapters as $chapter)
                            @if(!empty($chapter['has_multimedia']))
                                <!-- MULTIMEDIA LAB READY CARD -->
                                <div class="relative overflow-hidden rounded-2xl bg-gradient-to-br from-emerald-950/80 via-slate-900 to-slate-900 border-2 border-emerald-500/40 p-5 sm:p-6 shadow-2xl space-y-4">
                                    <div class="flex flex-col sm:flex-row sm:items-start justify-between gap-4">
                                        <div class="space-y-2">
                                            <div class="flex items-center space-x-2 flex-wrap gap-y-1">
                                                <span class="px-2.5 py-0.5 rounded-full text-[10px] font-black uppercase tracking-wider bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
                                                    Chapter {{ $chapter['chapter_num'] }}
                                                </span>
                                                @if($selectedClass === 'class12')
                                                    <span class="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 uppercase tracking-wider">
                                                        {{ $chapter['part'] ?? 'Part - 1' }}
                                                    </span>
                                                @endif
                                                <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
                                                    🎬 Interactive Multimedia Animation
                                                </span>
                                                <span class="text-xs font-mono text-emerald-400 font-bold">Slide-by-Slide Mode Ready</span>
                                            </div>

                                            <div>
                                                <h4 class="text-xl font-black text-white flex items-center space-x-2">
                                                    <span>{{ $chapter['media_key'] === 'real-numbers' ? '🌳' : '📐' }}</span>
                                                    <span>Chapter {{ $chapter['chapter_num'] }}: {{ $chapter['name'] }}</span>
                                                </h4>
                                                @if($selectedClass === 'class12')
                                                    <div class="text-xs font-bold text-amber-400 tracking-wide mt-0.5">{{ $chapter['part'] ?? 'Part - 1' }}</div>
                                                @endif
                                            </div>

                                            <p class="text-xs sm:text-sm text-slate-300 max-w-3xl leading-relaxed">
                                                {{ $chapter['description'] }}
                                            </p>

                                            <!-- Topics Covered -->
                                            @if(!empty($chapter['topics']))
                                                <div class="pt-2">
                                                    <div class="text-[11px] font-bold uppercase tracking-wider text-slate-400 mb-1.5">Interactive Modules in this Lab:</div>
                                                    <div class="flex items-center space-x-1.5 flex-wrap gap-y-1">
                                                        @foreach($chapter['topics'] as $topic)
                                                            <span class="px-2.5 py-1 rounded-lg bg-slate-950 border border-slate-800 text-xs font-medium text-slate-200">
                                                                ✓ {{ $topic }}
                                                            </span>
                                                        @endforeach
                                                    </div>
                                                </div>
                                            @endif
                                        </div>

                                        <!-- Launch Actions -->
                                        <div class="flex sm:flex-col items-center gap-2 shrink-0 sm:w-56">
                                            <button type="button" onclick="openStudentAnimationModal('{{ $chapter['media_key'] }}')"
                                                    class="w-full py-3 px-4 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-500 hover:from-emerald-500 hover:to-teal-400 text-white font-bold text-xs sm:text-sm shadow-xl shadow-emerald-600/30 flex items-center justify-center space-x-2 transition-all cursor-pointer active:scale-95">
                                                <span class="text-base">▶</span>
                                                <span>Watch Slide Lab</span>
                                            </button>

                                            <a href="{{ $chapter['media_url'] }}" target="_blank"
                                               class="w-full py-2.5 px-4 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 hover:text-white border border-slate-700 text-xs font-semibold flex items-center justify-center space-x-1.5 transition-all"
                                               title="Open in dedicated tab">
                                                <svg class="w-4 h-4 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
                                                <span>Open Fullscreen Tab</span>
                                            </a>
                                        </div>
                                    </div>
                                </div>
                            @else
                                <!-- REGULAR CHAPTER CARD WITHOUT MULTIMEDIA (EMPTY STATE FOR THIS CHAPTER) -->
                                <div class="p-4 sm:p-5 rounded-2xl bg-slate-900/60 border border-slate-800/80 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                                    <div class="space-y-1.5">
                                        <div class="flex items-center space-x-2">
                                            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-slate-800 text-slate-400">
                                                Chapter {{ $chapter['chapter_num'] }}
                                            </span>
                                            @if($selectedClass === 'class12')
                                                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 uppercase tracking-wider">
                                                    {{ $chapter['part'] ?? 'Part - 1' }}
                                                </span>
                                            @endif
                                            <h4 class="text-sm sm:text-base font-bold text-slate-200">
                                                {{ $chapter['name'] }}
                                            </h4>
                                        </div>
                                        <p class="text-xs text-slate-400 leading-relaxed max-w-2xl">
                                            {{ $chapter['description'] ?? 'Curriculum chapter content aligned with textbook syllabus.' }}
                                        </p>
                                    </div>

                                    <!-- Empty Multimedia Indicator -->
                                    <div class="shrink-0 p-2.5 rounded-xl bg-slate-950/80 border border-slate-800 text-center sm:text-right">
                                        <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-mono text-slate-500 bg-slate-900 border border-slate-800">
                                            📭 {{ $selectedSyllabus }}-{{ $selectedSubject }}-{{ $selectedClass }}-ch{{ $chapter['chapter_num'] }} - empty
                                        </span>
                                        <div class="text-[11px] text-slate-500 mt-1">No animation uploaded yet</div>
                                    </div>
                                </div>
                            @endif
                        @endforeach
                    </div>
                </div>
            @else
                <!-- EMPTY PLACEHOLDER: USER SPECIFIC EXAMPLE: cbse-mathematics-class6 -enpty -->
                <div class="p-8 sm:p-12 rounded-2xl bg-slate-900/60 border-2 border-dashed border-slate-800 text-center space-y-4">
                    <div class="w-16 h-16 rounded-2xl bg-slate-800/80 border border-slate-700/80 flex items-center justify-center text-3xl mx-auto shadow-inner text-slate-400">
                        📭
                    </div>

                    <div class="space-y-1">
                        <!-- User's exact prompt format -->
                        <div class="inline-flex items-center px-3 py-1 rounded-full text-xs font-mono font-bold bg-amber-500/10 text-amber-300 border border-amber-500/30">
                            {{ $selectedSyllabus }}-{{ $selectedSubject }}-{{ $selectedClass }} - empty
                        </div>
                        <h3 class="text-lg font-bold text-white mt-2">
                            No Multimedia Animations in this Section Yet
                        </h3>
                        <p class="text-xs sm:text-sm text-slate-400 max-w-md mx-auto leading-relaxed">
                            There is currently no interactive animation module uploaded for 
                            <strong class="text-slate-300 uppercase">{{ $selectedSyllabus }}</strong> &bull; 
                            <strong class="text-slate-300 capitalize">{{ $selectedSubject }}</strong> &bull; 
                            <strong class="text-slate-300 capitalize">{{ $classes[$selectedClass]['name'] ?? $selectedClass }}</strong>.
                        </p>
                    </div>

                    <!-- Quick suggestions to view available labs -->
                    <div class="pt-4 border-t border-slate-800/80 max-w-lg mx-auto space-y-2">
                        <span class="text-xs font-bold text-slate-400 uppercase tracking-wider block">Available Animated Labs in Syllabus:</span>
                        <div class="flex items-center justify-center gap-2 flex-wrap">
                            <a href="{{ route('multimedia.index', ['syllabus' => 'ncert', 'subject' => 'mathematics', 'class' => 'class12']) }}"
                               class="px-3 py-1.5 rounded-lg bg-indigo-950/60 hover:bg-indigo-900/60 border border-indigo-500/40 text-indigo-300 text-xs font-bold transition-all flex items-center space-x-1.5">
                                <span>⚡</span>
                                <span>Class 12 • Relations &amp; Functions (Ch 1)</span>
                            </a>
                            <a href="{{ route('multimedia.index', ['syllabus' => 'ncert', 'subject' => 'mathematics', 'class' => 'class10']) }}"
                               class="px-3 py-1.5 rounded-lg bg-emerald-950/60 hover:bg-emerald-900/60 border border-emerald-500/40 text-emerald-300 text-xs font-bold transition-all flex items-center space-x-1.5">
                                <span>🌳</span>
                                <span>Class 10 • Real Numbers (Ch 1)</span>
                            </a>
                            <a href="{{ route('multimedia.index', ['syllabus' => 'ncert', 'subject' => 'mathematics', 'class' => 'class9']) }}"
                               class="px-3 py-1.5 rounded-lg bg-cyan-950/60 hover:bg-cyan-900/60 border border-cyan-500/40 text-cyan-300 text-xs font-bold transition-all flex items-center space-x-1.5">
                                <span>📐</span>
                                <span>Class 9 • Number System (Ch 1)</span>
                            </a>
                        </div>
                    </div>
                </div>
            @endif

        </div>

    </div>
</x-layouts.app>

