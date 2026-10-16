<x-layouts.app title="Students in My Classes - Study App">
    <div class="py-8 w-full px-4 sm:px-6 lg:px-8 space-y-8">

        <!-- Header Banner -->
        <div class="relative overflow-hidden rounded-2xl bg-gradient-to-r from-sky-950 via-slate-900 to-slate-900 border border-sky-500/30 p-6 sm:p-8 shadow-2xl">
            <div class="relative z-10 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-6">
                <div>
                    <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-sky-500/20 border border-sky-500/40 text-sky-300 text-xs font-semibold uppercase tracking-wider mb-3">
                        <span class="w-2 h-2 rounded-full bg-sky-400 animate-pulse"></span>
                        <span>Enrolled Students</span>
                    </div>
                    <h1 class="text-3xl font-extrabold text-white tracking-tight sm:text-4xl">
                        Students in My Classes
                    </h1>
                    <p class="mt-2 text-slate-300 text-sm max-w-xl">
                        Displaying enrolled students linked to your assigned classes, individual performance, and communications.
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
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>
                        <span>Standards</span>
                    </a>

                    <a href="{{ route('exams.index') }}" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-indigo-300 border border-slate-700 font-medium text-sm transition-all flex items-center space-x-2">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                        </svg>
                        <span>Exams & Reports</span>
                    </a>

                    <a href="{{ route('questions.index') }}" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-violet-300 border border-slate-700 font-medium text-sm transition-all flex items-center space-x-2">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                        </svg>
                        <span>Question Bank</span>
                    </a>
                </div>
            </div>
        </div>

        <!-- Metric Stat Cards -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-6">
            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Total Linked Students</span>
                    <div class="p-2 bg-sky-500/10 rounded-lg text-sky-400">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0112 20.055a11.952 11.952 0 01-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"/></svg>
                    </div>
                </div>
                <p class="mt-4 text-3xl font-extrabold text-white">{{ $totalStudentsCount }}</p>
                <p class="mt-1 text-xs text-slate-400">Students across your assigned classes</p>
            </div>

            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Assigned Classes</span>
                    <div class="p-2 bg-violet-500/10 rounded-lg text-violet-400">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
                    </div>
                </div>
                <p class="mt-4 text-3xl font-extrabold text-white">{{ $teacherStandards->count() }}</p>
                <p class="mt-1 text-xs text-slate-400">Active class standards</p>
            </div>

            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Status</span>
                    <div class="p-2 bg-emerald-500/10 rounded-lg text-emerald-400">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                    </div>
                </div>
                <p class="mt-4 text-3xl font-extrabold text-emerald-400">Active</p>
                <p class="mt-1 text-xs text-slate-400">Class synchronization active</p>
            </div>
        </div>

        <!-- Students Directory Table -->
        <div class="bg-slate-900 border border-slate-800 rounded-2xl shadow-xl overflow-hidden">
            <div class="px-6 py-5 border-b border-slate-800 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                <div>
                    <h3 class="text-lg font-semibold text-white flex items-center space-x-2">
                        <svg class="w-5 h-5 text-sky-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"/>
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0112 20.055a11.952 11.952 0 01-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"/>
                        </svg>
                        <span>Students in My Classes</span>
                        @if(request()->filled('search') || request()->filled('standard_id'))
                            <span class="text-xs px-2.5 py-0.5 rounded-full bg-sky-500/20 text-sky-300 border border-sky-500/30 font-medium">Filtered</span>
                        @endif
                    </h3>
                    <p class="text-xs text-slate-400 mt-0.5">Displaying enrolled students linked to your assigned classes</p>
                </div>

                <div class="flex items-center space-x-2">
                    @if($teacherStandards->isNotEmpty())
                        <div class="flex flex-wrap gap-1 max-w-xs">
                            @foreach($teacherStandards as $std)
                                <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold bg-sky-500/10 text-sky-300 border border-sky-500/20">
                                    {{ $std->name }}
                                </span>
                            @endforeach
                        </div>
                    @else
                        <span class="text-xs text-rose-400 italic">No classes assigned to you yet</span>
                    @endif
                </div>
            </div>

            <!-- Search & Class Filter Bar -->
            <div class="px-4 py-3 sm:px-6 sm:py-4 bg-slate-950/40 border-b border-slate-800">
                <form method="GET" action="{{ route('students.index') }}" class="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3">
                    <div class="flex flex-col sm:flex-row items-center gap-3 w-full sm:w-auto">
                        <!-- Search by Name / Email -->
                        <div class="relative w-full sm:w-72">
                            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-500">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                                </svg>
                            </div>
                            <input type="text" name="search" value="{{ request('search') }}" placeholder="Search student name or email..." class="w-full pl-9 pr-3 py-2 rounded-xl bg-slate-900 border border-slate-700 text-slate-100 placeholder-slate-500 text-xs focus:outline-none focus:ring-2 focus:ring-sky-500">
                        </div>

                        <!-- Filter by Class / Standard -->
                        <div class="w-full sm:w-56 shrink-0">
                            <select name="standard_id" class="w-full px-3 py-2 rounded-xl bg-slate-900 border border-slate-700 text-slate-100 text-xs focus:outline-none focus:ring-2 focus:ring-sky-500">
                                <option value="">All Classes</option>
                                @foreach($teacherStandards as $std)
                                    <option value="{{ $std->id }}" {{ request('standard_id') == $std->id ? 'selected' : '' }}>
                                        {{ $std->name }}
                                    </option>
                                @endforeach
                            </select>
                        </div>
                    </div>

                    <div class="flex items-center space-x-2 shrink-0 justify-end">
                        @if(request()->filled('search') || request()->filled('standard_id'))
                            <a href="{{ route('students.index') }}" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs border border-slate-700 transition-colors inline-flex items-center space-x-1">
                                <svg class="w-3.5 h-3.5 text-rose-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                                </svg>
                                <span>Reset</span>
                            </a>
                        @endif
                        <button type="submit" class="px-4 py-2 rounded-xl bg-sky-600 hover:bg-sky-500 text-white font-semibold text-xs transition-all shadow-md shadow-sky-600/20 flex items-center space-x-1 cursor-pointer">
                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                            </svg>
                            <span>Filter</span>
                        </button>
                    </div>
                </form>
            </div>

            <!-- Table -->
            <div class="overflow-x-auto w-full">
                @if($students && $students->count() > 0)
                    <table class="w-full text-left border-collapse text-sm">
                        <thead>
                            <tr class="bg-slate-950/60 border-b border-slate-800 text-slate-400 uppercase text-[11px] font-semibold tracking-wider">
                                <th class="py-3.5 px-6">Student Name</th>
                                <th class="py-3.5 px-6">Assigned Class</th>
                                <th class="py-3.5 px-6">Exams & Performance</th>
                                <th class="py-3.5 px-6 text-right">Actions</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-800/60 text-slate-300">
                            @foreach ($students as $s)
                                @php
                                    $perf = $studentPerformanceMap[$s->id] ?? null;
                                @endphp
                                <tr class="hover:bg-slate-800/40 transition-colors">
                                    <td class="py-4 px-6 font-medium text-white flex items-center space-x-3">
                                        <div class="w-9 h-9 rounded-full bg-slate-800 border border-slate-700 text-sky-400 font-bold flex items-center justify-center text-sm shrink-0">
                                            {{ strtoupper(substr($s->name, 0, 1)) }}
                                        </div>
                                        <div class="min-w-0">
                                            <span class="font-bold text-white block text-sm truncate">{{ $s->name }}</span>
                                            <span class="text-xs text-slate-400 font-mono truncate block">{{ $s->email }}</span>
                                        </div>
                                    </td>
                                    <td class="py-4 px-6">
                                        @php
                                            $stNames = $s->studentStandards ? $s->studentStandards->pluck('name') : collect();
                                            if ($s->student?->standard && ! $stNames->contains($s->student->standard->name)) {
                                                $stNames->prepend($s->student->standard->name);
                                            }
                                        @endphp
                                        @if($stNames->isNotEmpty())
                                            <div class="flex flex-wrap gap-1">
                                                @foreach($stNames as $stName)
                                                    <span class="inline-flex items-center px-2.5 py-1 rounded-full text-xs font-semibold bg-sky-500/10 text-sky-300 border border-sky-500/20">
                                                        {{ $stName }}
                                                    </span>
                                                @endforeach
                                            </div>
                                        @else
                                            <span class="text-xs text-slate-500 italic">Unassigned</span>
                                        @endif
                                    </td>
                                    <td class="py-4 px-6">
                                        @if($perf && $perf['attempted_exams_count'] > 0)
                                            <div class="flex items-center space-x-2">
                                                <span class="text-xs font-bold {{ $perf['avg_score'] >= 75 ? 'text-emerald-400' : ($perf['avg_score'] >= 50 ? 'text-amber-400' : 'text-rose-400') }}">
                                                    {{ $perf['avg_score'] }}%
                                                </span>
                                                <span class="text-[11px] text-slate-400">
                                                    ({{ $perf['attempted_exams_count'] }}/{{ $perf['relevant_exams_count'] }} Exams)
                                                </span>
                                            </div>
                                        @else
                                            <span class="text-xs text-slate-500">No attempts yet</span>
                                        @endif
                                    </td>
                                    <td class="py-4 px-6 text-right whitespace-nowrap space-x-1.5">
                                        <button type="button" onclick="openChatModal({{ $s->id }})" class="px-3 py-1.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-xs transition-all shadow-md shadow-indigo-600/20 inline-flex items-center space-x-1.5 cursor-pointer">
                                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"/></svg>
                                            <span>Chat</span>
                                        </button>
                                        <button type="button" onclick="openViewStudentDetailsModal({{ json_encode([
                                            'id' => $s->id,
                                            'name' => $s->name,
                                            'email' => $s->email,
                                            'mobile' => $s->profile?->mobile ?? 'N/A',
                                            'address' => $s->profile?->address ?? 'N/A',
                                            'school' => $s->profile?->school ?? 'N/A',
                                            'designation' => $s->profile?->designation ?? 'Student',
                                            'standard' => $stNames->isNotEmpty() ? $stNames->join(', ') : 'Unassigned',
                                            'status' => $s->status ?? 1,
                                        ]) }})" class="px-3 py-1.5 rounded-xl bg-sky-600 hover:bg-sky-500 text-white font-semibold text-xs transition-all shadow-md shadow-sky-600/20 inline-flex items-center space-x-1.5 cursor-pointer">
                                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                                            </svg>
                                            <span>View Details</span>
                                        </button>
                                    </td>
                                </tr>
                            @endforeach
                        </tbody>
                    </table>
                @else
                    <div class="p-12 text-center">
                        <div class="w-16 h-16 rounded-2xl bg-slate-800 border border-slate-700 text-slate-500 flex items-center justify-center mx-auto mb-3">
                            <svg class="w-8 h-8 text-sky-400/80" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
                            </svg>
                        </div>
                        @if(request()->filled('search') || request()->filled('standard_id'))
                            <h3 class="text-base font-semibold text-slate-300">No Matching Students Found</h3>
                            <p class="mt-1 text-sm text-slate-500 max-w-sm mx-auto">No students match your search query or selected class filter.</p>
                        @elseif($teacherStandards->isNotEmpty())
                            <h3 class="text-base font-semibold text-slate-300">No Students Found in Assigned Classes</h3>
                            <p class="mt-1 text-sm text-slate-500 max-w-sm mx-auto">No students are currently enrolled in your assigned classes.</p>
                        @else
                            <h3 class="text-base font-semibold text-slate-300">No Classes Assigned</h3>
                            <p class="mt-1 text-sm text-slate-500 max-w-sm mx-auto">Your teacher profile does not have any assigned class standards. Contact system admin to assign standards.</p>
                        @endif
                    </div>
                @endif
            </div>

            @if($students && method_exists($students, 'hasPages') && $students->hasPages())
                <div class="px-6 py-4 border-t border-slate-800 bg-slate-950/40">
                    {{ $students->links() }}
                </div>
            @endif
        </div>
    </div>

    <!-- VIEW STUDENT DETAILS MODAL -->
    <div id="viewStudentDetailsModal" class="hidden fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4 overflow-y-auto">
        <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-lg overflow-hidden shadow-2xl my-8">
            <div class="px-6 py-4 border-b border-slate-800 flex items-center justify-between bg-slate-950/60">
                <div class="flex items-center space-x-3">
                    <div class="w-9 h-9 rounded-xl bg-sky-500/10 border border-sky-500/30 text-sky-400 font-bold flex items-center justify-center text-sm">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                        </svg>
                    </div>
                    <div>
                        <h3 id="view_student_modal_title" class="text-base font-extrabold text-white">Student Profile Details</h3>
                        <p class="text-xs text-slate-400">Complete information for selected student</p>
                    </div>
                </div>
                <button type="button" onclick="document.getElementById('viewStudentDetailsModal').classList.add('hidden')" class="text-slate-400 hover:text-white transition-colors cursor-pointer p-1">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                </button>
            </div>

            <div class="p-6 space-y-4">
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div class="bg-slate-950/60 p-3.5 rounded-xl border border-slate-800">
                        <span class="text-[11px] font-semibold text-slate-400 uppercase tracking-wider block">Full Name</span>
                        <span id="view_student_modal_full_name" class="text-sm font-bold text-white mt-1 block"></span>
                    </div>
                    <div class="bg-slate-950/60 p-3.5 rounded-xl border border-slate-800">
                        <span class="text-[11px] font-semibold text-slate-400 uppercase tracking-wider block">Class / Standard</span>
                        <span id="view_student_modal_standard" class="text-sm font-semibold text-sky-300 mt-1 block"></span>
                    </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div class="bg-slate-950/60 p-3.5 rounded-xl border border-slate-800">
                        <span class="text-[11px] font-semibold text-slate-400 uppercase tracking-wider block">Email Address</span>
                        <span id="view_student_modal_email" class="text-sm font-medium text-slate-300 mt-1 block break-all"></span>
                    </div>
                    <div class="bg-slate-950/60 p-3.5 rounded-xl border border-slate-800">
                        <span class="text-[11px] font-semibold text-slate-400 uppercase tracking-wider block">Mobile Number</span>
                        <span id="view_student_modal_mobile" class="text-sm font-medium text-slate-300 mt-1 block"></span>
                    </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div class="bg-slate-950/60 p-3.5 rounded-xl border border-slate-800">
                        <span class="text-[11px] font-semibold text-slate-400 uppercase tracking-wider block">School</span>
                        <span id="view_student_modal_school" class="text-sm font-semibold text-slate-200 mt-1 block"></span>
                    </div>
                    <div class="bg-slate-950/60 p-3.5 rounded-xl border border-slate-800">
                        <span class="text-[11px] font-semibold text-slate-400 uppercase tracking-wider block">Account Status</span>
                        <span id="view_student_modal_status" class="text-sm font-bold mt-1 block"></span>
                    </div>
                </div>

                <div class="bg-slate-950/60 p-3.5 rounded-xl border border-slate-800">
                    <span class="text-[11px] font-semibold text-slate-400 uppercase tracking-wider block">Full Address</span>
                    <span id="view_student_modal_address" class="text-sm font-medium text-slate-300 mt-1 block"></span>
                </div>
            </div>

            <div class="px-6 py-3.5 bg-slate-950/80 border-t border-slate-800 flex items-center justify-between">
                <button type="button" id="view_student_modal_chat_btn" onclick="openChatFromStudentModal()" class="px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-xs transition-all shadow-md flex items-center space-x-1.5 cursor-pointer">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"/></svg>
                    <span>Chat with Student</span>
                </button>
                <button type="button" onclick="document.getElementById('viewStudentDetailsModal').classList.add('hidden')" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-semibold text-xs transition-all cursor-pointer">
                    Close
                </button>
            </div>
        </div>
    </div>

    <script>
        let currentSelectedStudentId = null;

        function openViewStudentDetailsModal(data) {
            currentSelectedStudentId = data.id;
            document.getElementById('view_student_modal_full_name').textContent = data.name || 'N/A';
            document.getElementById('view_student_modal_email').textContent = data.email || 'N/A';
            document.getElementById('view_student_modal_mobile').textContent = data.mobile || 'N/A';
            document.getElementById('view_student_modal_address').textContent = data.address || 'N/A';
            document.getElementById('view_student_modal_school').textContent = data.school || 'N/A';
            document.getElementById('view_student_modal_standard').textContent = data.standard || 'Unassigned';

            const statusEl = document.getElementById('view_student_modal_status');
            if (data.status == 1) {
                statusEl.textContent = 'Active';
                statusEl.className = 'text-sm font-bold text-emerald-400 mt-1 block';
            } else {
                statusEl.textContent = 'Inactive';
                statusEl.className = 'text-sm font-bold text-rose-400 mt-1 block';
            }

            document.getElementById('viewStudentDetailsModal').classList.remove('hidden');
        }

        function openChatFromStudentModal() {
            if (currentSelectedStudentId) {
                document.getElementById('viewStudentDetailsModal').classList.add('hidden');
                if (typeof openChatModal === 'function') {
                    openChatModal(currentSelectedStudentId);
                }
            }
        }
    </script>
</x-layouts.app>
