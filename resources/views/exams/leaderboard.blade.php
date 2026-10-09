<x-layouts.app title="Exam Leaderboard - {{ $exam->name }}">
    <div class="py-8 w-full px-4 sm:px-6 lg:px-8 space-y-8">

        <!-- Header Banner -->
        <div class="relative overflow-hidden rounded-2xl bg-gradient-to-r from-amber-950 via-slate-900 to-indigo-950 border border-amber-500/30 p-6 sm:p-8 shadow-2xl">
            <div class="relative z-10 flex flex-col md:flex-row md:items-center md:justify-between gap-6">
                <div>
                    <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-amber-500/20 border border-amber-500/40 text-amber-300 text-xs font-semibold uppercase tracking-wider mb-3">
                        <svg class="w-4 h-4 text-amber-400 animate-bounce" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"/>
                        </svg>
                        <span>Official Exam Leaderboard</span>
                    </div>
                    <h1 class="text-3xl font-extrabold text-white tracking-tight sm:text-4xl flex items-center space-x-3">
                        <span>🏆 {{ $exam->name }}</span>
                    </h1>
                    <div class="mt-2 flex items-center flex-wrap gap-3 text-xs text-slate-300">
                        <span>Total Marks: <strong class="text-amber-400 font-mono text-sm">{{ $totalExamMarks }}</strong></span>
                        <span>&bull;</span>
                        <span>Questions: <strong class="text-white">{{ $exam->questions->count() }}</strong></span>
                        @if($exam->standards->isNotEmpty())
                            <span>&bull;</span>
                            <span>Assigned Class: <strong class="text-indigo-300">{{ $exam->standards->pluck('name')->join(', ') }}</strong></span>
                        @endif
                        <span>&bull;</span>
                        <span>Total Submissions: <strong class="text-emerald-400">{{ $summary['total_submissions'] }} Student(s)</strong></span>
                    </div>
                </div>

                <div class="flex items-center flex-wrap gap-3">
                    <a href="{{ route('dashboard') }}" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium text-sm transition-all flex items-center space-x-2 shadow-md">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
                        </svg>
                        <span>Dashboard</span>
                    </a>
                    <a href="{{ route('exams.show', $exam) }}" class="px-4 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-sm transition-all shadow-lg shadow-indigo-600/30 flex items-center space-x-2">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
                        </svg>
                        <span>Exam Details</span>
                    </a>
                </div>
            </div>
        </div>

        <!-- Metric Stat Cards -->
        <div class="grid grid-cols-1 sm:grid-cols-4 gap-6">
            <div class="bg-gradient-to-br from-amber-950/40 to-slate-900 border border-amber-500/30 rounded-2xl p-6 shadow-xl">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Top Scorer 🥇</span>
                    <div class="p-2.5 bg-amber-500/20 rounded-xl text-amber-400">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"/></svg>
                    </div>
                </div>
                <p class="mt-4 text-2xl font-extrabold text-white truncate">{{ $summary['top_scorer'] }}</p>
                <p class="mt-1 text-xs text-amber-300/80">Rank 1 Champion</p>
            </div>

            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Highest Score</span>
                    <div class="p-2.5 bg-emerald-500/10 rounded-xl text-emerald-400">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                    </div>
                </div>
                <p class="mt-4 text-3xl font-extrabold text-emerald-400 font-mono">{{ $summary['highest_marks'] }} <span class="text-slate-500 text-lg">/ {{ $totalExamMarks }}</span></p>
                <p class="mt-1 text-xs text-slate-400">Maximum marks scored</p>
            </div>

            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Average Marks</span>
                    <div class="p-2.5 bg-indigo-500/10 rounded-xl text-indigo-400">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/></svg>
                    </div>
                </div>
                <p class="mt-4 text-3xl font-extrabold text-white font-mono">{{ $summary['average_marks'] }} <span class="text-slate-500 text-lg">/ {{ $totalExamMarks }}</span></p>
                <p class="mt-1 text-xs text-slate-400">Class performance average</p>
            </div>

            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Total Participants</span>
                    <div class="p-2.5 bg-sky-500/10 rounded-xl text-sky-400">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"/></svg>
                    </div>
                </div>
                <p class="mt-4 text-3xl font-extrabold text-white font-mono">{{ $summary['total_submissions'] }}</p>
                <p class="mt-1 text-xs text-slate-400">Student exam submissions</p>
            </div>
        </div>

        <!-- Leaderboard Table Section -->
        <div class="bg-slate-900 border border-slate-800 rounded-2xl shadow-xl overflow-hidden">
            <div class="px-6 py-5 border-b border-slate-800 flex items-center justify-between flex-wrap gap-4 bg-slate-950/40">
                <div class="flex items-center space-x-3">
                    <div class="w-10 h-10 rounded-xl bg-amber-500/10 border border-amber-500/30 text-amber-400 flex items-center justify-center text-lg font-bold">
                        🏆
                    </div>
                    <div>
                        <h3 class="text-lg font-extrabold text-white">Student Leaderboard Rankings</h3>
                        <p class="text-xs text-slate-400">Ranked by score obtained (descending), tie-broken by earliest submission time</p>
                    </div>
                </div>
                <span class="text-xs font-medium text-slate-400 bg-slate-800 px-3 py-1 rounded-full border border-slate-700">
                    Showing {{ count($rankings) }} Student(s)
                </span>
            </div>

            @if(count($rankings) > 0)
                <div class="overflow-x-auto">
                    <table class="w-full text-left border-collapse text-sm">
                        <thead>
                            <tr class="bg-slate-950/80 border-b border-slate-800 text-slate-400 uppercase text-[11px] font-bold tracking-wider">
                                <th class="py-4 px-6 text-center w-24">Rank</th>
                                <th class="py-4 px-6">Student Name</th>
                                <th class="py-4 px-6">Class / Standard</th>
                                <th class="py-4 px-6 text-center">Correct / Total</th>
                                <th class="py-4 px-6 text-center">Score Obtained</th>
                                <th class="py-4 px-6 text-center">Percentage</th>
                                <th class="py-4 px-6 text-right">Submitted At</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-800/60 bg-slate-900">
                            @foreach ($rankings as $row)
                                @php
                                    $rank = $row['rank'];
                                    $isTop1 = ($rank === 1);
                                    $isTop2 = ($rank === 2);
                                    $isTop3 = ($rank === 3);
                                    $isCurrent = $row['is_current_user'];

                                    $rowBgClass = $isCurrent
                                        ? 'bg-indigo-950/40 border-l-4 border-l-indigo-500 hover:bg-indigo-900/50'
                                        : ($isTop1 ? 'bg-amber-950/20 border-l-4 border-l-amber-500 hover:bg-amber-900/30' : ($isTop2 ? 'bg-slate-800/40 border-l-4 border-l-slate-400 hover:bg-slate-800/60' : ($isTop3 ? 'bg-amber-900/10 border-l-4 border-l-amber-700 hover:bg-amber-900/20' : 'hover:bg-slate-800/40')));
                                @endphp

                                <tr class="transition-colors {{ $rowBgClass }}">
                                    <!-- Rank Badge -->
                                    <td class="py-4 px-6 text-center">
                                        @if($isTop1)
                                            <span class="inline-flex items-center justify-center w-9 h-9 rounded-full bg-gradient-to-br from-amber-300 to-amber-600 text-slate-950 font-black text-base shadow-lg shadow-amber-500/30 border border-amber-200">
                                                🥇
                                            </span>
                                        @elseif($isTop2)
                                            <span class="inline-flex items-center justify-center w-9 h-9 rounded-full bg-gradient-to-br from-slate-200 to-slate-400 text-slate-950 font-black text-base shadow-md border border-slate-100">
                                                🥈
                                            </span>
                                        @elseif($isTop3)
                                            <span class="inline-flex items-center justify-center w-9 h-9 rounded-full bg-gradient-to-br from-amber-600 to-amber-800 text-amber-100 font-black text-base shadow-md border border-amber-500">
                                                🥉
                                            </span>
                                        @else
                                            <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-slate-800 text-slate-300 font-extrabold text-xs border border-slate-700">
                                                #{{ $rank }}
                                            </span>
                                        @endif
                                    </td>

                                    <!-- Student Name & Email -->
                                    <td class="py-4 px-6">
                                        <div class="flex items-center space-x-3">
                                            <div class="w-9 h-9 rounded-full bg-slate-800 border border-slate-700 text-indigo-400 font-bold flex items-center justify-center text-xs shrink-0">
                                                {{ strtoupper(substr($row['student_name'], 0, 1)) }}
                                            </div>
                                            <div>
                                                <div class="flex items-center space-x-2">
                                                    <span class="font-extrabold text-white text-sm sm:text-base">{{ $row['student_name'] }}</span>
                                                    @if($isCurrent)
                                                        <span class="px-2 py-0.5 rounded-full text-[10px] font-black bg-indigo-500 text-white uppercase tracking-wider">You</span>
                                                    @endif
                                                </div>
                                                @if($row['student_email'])
                                                    <span class="text-xs text-slate-400 font-mono block">{{ $row['student_email'] }}</span>
                                                @endif
                                            </div>
                                        </div>
                                    </td>

                                    <!-- Class / Standard -->
                                    <td class="py-4 px-6">
                                        <span class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 border border-slate-700 text-xs font-semibold">
                                            {{ $row['student_class'] }}
                                        </span>
                                    </td>

                                    <!-- Correct / Total Questions -->
                                    <td class="py-4 px-6 text-center font-mono text-xs text-slate-300">
                                        <span class="font-bold text-emerald-400">{{ $row['correct_count'] }}</span> / {{ $row['total_questions'] }} Qs
                                    </td>

                                    <!-- Score Obtained -->
                                    <td class="py-4 px-6 text-center">
                                        <span class="font-mono font-black text-base {{ $isTop1 ? 'text-amber-400' : 'text-emerald-400' }}">
                                            {{ $row['obtained_marks'] }}
                                        </span>
                                        <span class="text-slate-500 text-xs font-medium">/ {{ $totalExamMarks }}</span>
                                    </td>

                                    <!-- Percentage Badge -->
                                    <td class="py-4 px-6 text-center">
                                        @php
                                            $pct = $row['percentage'];
                                        @endphp
                                        <span class="px-3 py-1 rounded-full text-xs font-black border {{ $pct >= 80 ? 'bg-emerald-500/20 text-emerald-300 border-emerald-500/40' : ($pct >= 50 ? 'bg-amber-500/20 text-amber-300 border-amber-500/40' : 'bg-rose-500/20 text-rose-300 border-rose-500/40') }}">
                                            {{ $pct }}%
                                        </span>
                                    </td>

                                    <!-- Submitted At -->
                                    <td class="py-4 px-6 text-right text-xs text-slate-400 font-mono">
                                        {{ $row['submitted_at'] ?? 'N/A' }}
                                    </td>
                                </tr>
                            @endforeach
                        </tbody>
                    </table>
                </div>
            @else
                <div class="p-12 text-center text-slate-400 space-y-3">
                    <svg class="w-16 h-16 mx-auto text-slate-600 animate-pulse" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"/></svg>
                    <h4 class="text-lg font-bold text-white">No Exam Submissions Yet</h4>
                    <p class="text-xs text-slate-400 max-w-md mx-auto">Rankings will automatically appear on this leaderboard once students complete and submit their exam attempts.</p>
                </div>
            @endif
        </div>

    </div>
</x-layouts.app>
