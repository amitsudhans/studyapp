<x-layouts.app title="Class Standards Management - Study App">
    <div class="py-8 w-full px-4 sm:px-6 lg:px-8 space-y-8">

        <!-- Header Banner -->
        <div class="relative overflow-hidden rounded-2xl bg-gradient-to-r from-emerald-950 via-slate-900 to-slate-900 border border-emerald-500/30 p-6 sm:p-8 shadow-2xl">
            <div class="relative z-10 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-6">
                <div>
                    <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-emerald-500/20 border border-emerald-500/40 text-emerald-300 text-xs font-semibold uppercase tracking-wider mb-3">
                        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                        <span>Class Standards</span>
                    </div>
                    <h1 class="text-3xl font-extrabold text-white tracking-tight sm:text-4xl">
                        Standards Management
                    </h1>
                    <p class="mt-2 text-slate-300 text-sm max-w-xl">
                        Create and manage academic standards, organize classes, and assign enrolled students.
                    </p>
                </div>

                <div class="flex items-center flex-wrap gap-3">
                    <a href="{{ route('dashboard') }}" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium text-sm transition-all flex items-center space-x-2">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
                        </svg>
                        <span>Dashboard</span>
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

                    <a href="{{ route('students.index') }}" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-sky-300 border border-slate-700 font-medium text-sm transition-all flex items-center space-x-2">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z" />
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0112 20.055a11.952 11.952 0 01-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z" />
                        </svg>
                        <span>My Students</span>
                    </a>

                    @php
                        $firstStdIndex = $standards->first();
                    @endphp
                    <button type="button" onclick="openStandardChaptersModal({{ $firstStdIndex?->id ?? 1 }}, '{{ addslashes($firstStdIndex?->name ?? 'Class Standard') }}')" class="px-5 py-2.5 rounded-xl bg-purple-600 hover:bg-purple-500 text-white font-semibold text-sm transition-all shadow-lg shadow-purple-600/30 flex items-center space-x-2 cursor-pointer">
                        <span class="text-base">📚</span>
                        <span>Manage Chapters & Topics</span>
                    </button>

                    <button onclick="document.getElementById('createStandardModal').classList.remove('hidden')" class="px-5 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-semibold text-sm transition-all shadow-lg shadow-emerald-600/30 flex items-center space-x-2 cursor-pointer">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
                        </svg>
                        <span>Create New Standard</span>
                    </button>
                </div>
            </div>
        </div>

        <!-- Metric Stat Cards -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-6">
            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Total Standards</span>
                    <div class="p-2 bg-emerald-500/10 rounded-lg text-emerald-400">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>
                    </div>
                </div>
                <p class="mt-4 text-3xl font-extrabold text-white">{{ $totalStandardsCount }}</p>
                <p class="mt-1 text-xs text-slate-400">Standards in directory</p>
            </div>

            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">My Assigned Standards</span>
                    <div class="p-2 bg-teal-500/10 rounded-lg text-teal-400">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                    </div>
                </div>
                <p class="mt-4 text-3xl font-extrabold text-white">{{ $myStandardsCount }}</p>
                <p class="mt-1 text-xs text-slate-400">Standards linked to your account</p>
            </div>

            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Available Students</span>
                    <div class="p-2 bg-sky-500/10 rounded-lg text-sky-400">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0112 20.055a11.952 11.952 0 01-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"/></svg>
                    </div>
                </div>
                <p class="mt-4 text-3xl font-extrabold text-white">{{ $allStudents->count() }}</p>
                <p class="mt-1 text-xs text-slate-400">Enrolled student pool</p>
            </div>
        </div>

        <!-- Standards Directory Table -->
        <div class="bg-slate-900 border border-slate-800 rounded-2xl shadow-xl overflow-hidden">
            <div class="px-6 py-5 border-b border-slate-800 flex items-center justify-between flex-wrap gap-4">
                <div>
                    <h3 class="text-lg font-semibold text-white flex items-center space-x-2">
                        <svg class="w-5 h-5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
                        </svg>
                        <span>Standards Directory</span>
                        @if(request()->filled('search') || request()->filled('syllabus_id'))
                            <span class="text-xs px-2.5 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-medium">Filtered</span>
                        @endif
                    </h3>
                    <p class="text-xs text-slate-400 mt-0.5">Manage class standards, syllabus assignments, and student enrollments</p>
                </div>
                <span class="text-xs text-slate-400 bg-slate-800 px-3 py-1 rounded-full border border-slate-700">
                    Total: {{ $standards->total() }} Standards
                </span>
            </div>

            <!-- Search & Filter Bar -->
            <div class="p-4 sm:p-5 bg-slate-950/60 border-b border-slate-800/80">
                <form method="GET" action="{{ route('standards.index') }}" class="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3">
                    <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-3 w-full sm:w-auto">
                        <!-- Search Name -->
                        <div class="relative w-full sm:w-72">
                            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-500">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                            </div>
                            <input type="text" name="search" value="{{ request('search') }}" placeholder="Search standard name..." class="w-full pl-9 pr-3 py-2 rounded-xl bg-slate-900 border border-slate-700 text-slate-100 placeholder-slate-500 text-xs focus:outline-none focus:ring-2 focus:ring-emerald-500">
                        </div>

                        <!-- Syllabus Filter -->
                        <div class="w-full sm:w-56">
                            <select name="syllabus_id" class="w-full px-3 py-2 rounded-xl bg-slate-900 border border-slate-700 text-slate-100 text-xs focus:outline-none focus:ring-2 focus:ring-emerald-500">
                                <option value="">All Syllabuses</option>
                                @foreach($syllabuses as $syl)
                                    <option value="{{ $syl->id }}" {{ request('syllabus_id') == $syl->id ? 'selected' : '' }}>{{ $syl->name }}</option>
                                @endforeach
                            </select>
                        </div>
                    </div>

                    <div class="flex items-center space-x-2 shrink-0 justify-end">
                        @if(request()->filled('search') || request()->filled('syllabus_id'))
                            <a href="{{ route('standards.index') }}" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition-colors">
                                Clear
                            </a>
                        @endif
                        <button type="submit" class="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-semibold text-xs transition-all shadow-md flex items-center space-x-1.5 cursor-pointer">
                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                            <span>Filter</span>
                        </button>
                    </div>
                </form>
            </div>

            <!-- Table -->
            <div class="overflow-x-auto">
                <table class="w-full text-left border-collapse text-sm">
                    <thead>
                        <tr class="bg-slate-950/60 border-b border-slate-800 text-slate-400 uppercase text-[11px] font-semibold tracking-wider">
                            <th class="py-3.5 px-6">Standard / Class Name</th>
                            <th class="py-3.5 px-6">Syllabus</th>
                            <th class="py-3.5 px-6">Enrolled Students</th>
                            <th class="py-3.5 px-6">Chapters & Topics</th>
                            <th class="py-3.5 px-6">Created By</th>
                            <th class="py-3.5 px-6 text-right">Actions</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800/60 text-slate-300">
                        @forelse ($standards as $std)
                            <tr class="hover:bg-slate-800/40 transition-colors">
                                <td class="py-4 px-6 font-medium text-white">
                                    <div class="flex items-center space-x-2.5">
                                        <div class="w-8 h-8 rounded-lg bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold text-xs">
                                            #{{ $std->id }}
                                        </div>
                                        <div>
                                            <span class="text-sm font-bold text-white block">{{ $std->name }}</span>
                                            <span class="text-[11px] text-slate-400">Created: {{ $std->created_at?->format('M d, Y') ?? 'N/A' }}</span>
                                        </div>
                                    </div>
                                </td>
                                <td class="py-4 px-6">
                                    <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold bg-indigo-500/10 text-indigo-300 border border-indigo-500/20">
                                        {{ $std->syllabus?->name ?? 'Default Syllabus' }}
                                    </span>
                                </td>
                                <td class="py-4 px-6">
                                    @php
                                        $stCount = $std->students_count ?? $std->students->count();
                                    @endphp
                                    <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold {{ $stCount >= 100 ? 'bg-rose-500/10 text-rose-400 border border-rose-500/20' : 'bg-sky-500/10 text-sky-400 border border-sky-500/20' }}">
                                        {{ $stCount }}/100 Students
                                    </span>
                                </td>
                                <td class="py-4 px-6">
                                    <button type="button" onclick="openStandardChaptersModal({{ $std->id }}, '{{ addslashes($std->name) }}')" class="inline-flex items-center space-x-1.5 px-3 py-1.5 rounded-xl bg-purple-500/10 hover:bg-purple-500/20 text-purple-300 border border-purple-500/30 text-xs font-semibold transition-all cursor-pointer shadow-sm group">
                                        <span>📖</span>
                                        <span class="group-hover:underline">{{ $std->chapters_count ?? $std->chapters->count() }} Chapters</span>
                                        <svg class="w-3.5 h-3.5 text-purple-400 opacity-60 group-hover:opacity-100" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                                    </button>
                                </td>
                                <td class="py-4 px-6 text-xs text-slate-400">
                                    @if($std->created_by === Auth::id())
                                        <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">You (Owner)</span>
                                    @else
                                        <span>{{ $std->creator?->name ?? 'System Admin' }}</span>
                                    @endif
                                </td>
                                <td class="py-4 px-6 text-right whitespace-nowrap space-x-1.5">
                                    <button type="button" onclick="openStandardChaptersModal({{ $std->id }}, '{{ addslashes($std->name) }}')" class="px-2.5 py-1.5 rounded-lg bg-purple-600/20 hover:bg-purple-600/30 text-purple-300 border border-purple-500/30 text-xs font-medium transition-all inline-flex items-center space-x-1 cursor-pointer" title="Manage Chapters & Topics">
                                        <span>📚</span>
                                        <span>Chapters</span>
                                    </button>
                                    @if (Auth::user()->isAdmin() || $std->created_by === Auth::id())
                                        <button onclick="openAssignStudentsModal({{ json_encode([
                                            'id' => $std->id,
                                            'name' => $std->name,
                                            'student_ids' => $std->students->pluck('id')->toArray(),
                                        ]) }})" class="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-semibold shadow transition-all inline-flex items-center space-x-1 cursor-pointer">
                                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z"/></svg>
                                            <span>Assign Students</span>
                                        </button>

                                        <button onclick="openEditStandardModal({{ json_encode([
                                            'id' => $std->id,
                                            'name' => $std->name,
                                            'syllabus_id' => $std->syllabus_id,
                                        ]) }})" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-semibold transition-all inline-flex items-center space-x-1 cursor-pointer">
                                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/></svg>
                                            <span>Edit</span>
                                        </button>

                                        <form method="POST" action="{{ route('standards.destroy', $std->id) }}" onsubmit="return confirm('Are you sure you want to delete this standard?');" class="inline">
                                            @csrf
                                            @method('DELETE')
                                            <button type="submit" class="px-2.5 py-1.5 rounded-lg bg-rose-600/10 hover:bg-rose-600 text-rose-400 hover:text-white border border-rose-500/20 text-xs font-semibold transition-all inline-flex items-center cursor-pointer">
                                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/></svg>
                                            </button>
                                        </form>
                                    @endif
                                </td>
                            </tr>
                        @empty
                            <tr>
                                <td colspan="5" class="py-12 text-center text-slate-500">
                                    <svg class="w-12 h-12 mx-auto mb-3 opacity-40 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>
                                    <p class="text-sm font-semibold text-slate-400">No standards found</p>
                                    <p class="text-xs text-slate-500 mt-1">Try modifying your filters or create a new standard.</p>
                                </td>
                            </tr>
                        @endforelse
                    </tbody>
                </table>
            </div>

            @if($standards->hasPages())
                <div class="px-6 py-4 border-t border-slate-800 bg-slate-950/40">
                    {{ $standards->links() }}
                </div>
            @endif
        </div>
    </div>

    <!-- Create Standard Modal -->
    <div id="createStandardModal" class="hidden fixed inset-0 z-50 flex items-center justify-center bg-slate-950/80 backdrop-blur-sm p-4">
        <div class="bg-slate-900 border border-slate-800 rounded-2xl max-w-md w-full shadow-2xl overflow-hidden animate-in fade-in zoom-in-95 duration-150">
            <div class="px-6 py-4 border-b border-slate-800 flex items-center justify-between">
                <h3 class="text-base font-bold text-white flex items-center space-x-2">
                    <svg class="w-5 h-5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
                    <span>Create New Standard</span>
                </h3>
                <button type="button" onclick="document.getElementById('createStandardModal').classList.add('hidden')" class="text-slate-400 hover:text-white transition-colors cursor-pointer">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                </button>
            </div>
            <form method="POST" action="{{ route('standards.store') }}" class="p-6 space-y-4">
                @csrf
                <div>
                    <label for="create_standard_name" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-2">Standard / Class Name</label>
                    <input type="text" id="create_standard_name" name="name" required placeholder="e.g. Standard 10, Grade 12" class="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-700 text-slate-100 text-sm focus:ring-2 focus:ring-emerald-500 focus:outline-none">
                </div>
                <div>
                    <label for="create_standard_syllabus" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-2">Curriculum / Syllabus</label>
                    <select id="create_standard_syllabus" name="syllabus_id" class="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-700 text-slate-100 text-sm focus:ring-2 focus:ring-emerald-500 focus:outline-none">
                        @foreach($syllabuses as $syl)
                            <option value="{{ $syl->id }}">{{ $syl->name }}</option>
                        @endforeach
                    </select>
                </div>
                <div class="flex justify-end space-x-3 pt-2">
                    <button type="button" onclick="document.getElementById('createStandardModal').classList.add('hidden')" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold transition-colors cursor-pointer">Cancel</button>
                    <button type="submit" class="px-5 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold shadow-lg shadow-emerald-600/30 transition-all cursor-pointer">Create Standard</button>
                </div>
            </form>
        </div>
    </div>

    <!-- Edit Standard Modal -->
    <div id="editStandardModal" class="hidden fixed inset-0 z-50 flex items-center justify-center bg-slate-950/80 backdrop-blur-sm p-4">
        <div class="bg-slate-900 border border-slate-800 rounded-2xl max-w-md w-full shadow-2xl overflow-hidden animate-in fade-in zoom-in-95 duration-150">
            <div class="px-6 py-4 border-b border-slate-800 flex items-center justify-between">
                <h3 class="text-base font-bold text-white flex items-center space-x-2">
                    <svg class="w-5 h-5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/></svg>
                    <span>Edit Standard</span>
                </h3>
                <button type="button" onclick="document.getElementById('editStandardModal').classList.add('hidden')" class="text-slate-400 hover:text-white transition-colors cursor-pointer">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                </button>
            </div>
            <form id="editStandardForm" method="POST" action="" class="p-6 space-y-4">
                @csrf
                @method('PUT')
                <div>
                    <label for="edit_standard_name" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-2">Standard / Class Name</label>
                    <input type="text" id="edit_standard_name" name="name" required class="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-700 text-slate-100 text-sm focus:ring-2 focus:ring-emerald-500 focus:outline-none">
                </div>
                <div>
                    <label for="edit_standard_syllabus_id" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-2">Curriculum / Syllabus</label>
                    <select id="edit_standard_syllabus_id" name="syllabus_id" class="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-700 text-slate-100 text-sm focus:ring-2 focus:ring-emerald-500 focus:outline-none">
                        @foreach($syllabuses as $syl)
                            <option value="{{ $syl->id }}">{{ $syl->name }}</option>
                        @endforeach
                    </select>
                </div>
                <div class="flex justify-end space-x-3 pt-2">
                    <button type="button" onclick="document.getElementById('editStandardModal').classList.add('hidden')" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold transition-colors cursor-pointer">Cancel</button>
                    <button type="submit" class="px-5 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold shadow-lg shadow-emerald-600/30 transition-all cursor-pointer">Save Changes</button>
                </div>
            </form>
        </div>
    </div>

    <!-- Assign Students Modal -->
    <div id="assignStudentsModal" class="hidden fixed inset-0 z-50 flex items-center justify-center bg-slate-950/80 backdrop-blur-sm p-4">
        <div class="bg-slate-900 border border-slate-800 rounded-2xl max-w-xl w-full shadow-2xl overflow-hidden flex flex-col max-h-[90vh]">
            <div class="px-6 py-4 border-b border-slate-800 flex items-center justify-between">
                <div>
                    <h3 class="text-base font-bold text-white flex items-center space-x-2">
                        <svg class="w-5 h-5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z"/></svg>
                        <span id="assign_modal_standard_title">Assign Students</span>
                    </h3>
                    <p class="text-xs text-slate-400 mt-0.5">Select up to 100 students to link with this class standard</p>
                </div>
                <button type="button" onclick="document.getElementById('assignStudentsModal').classList.add('hidden')" class="text-slate-400 hover:text-white transition-colors cursor-pointer">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                </button>
            </div>

            <form id="assignStudentsForm" method="POST" action="" class="flex flex-col flex-1 overflow-hidden">
                @csrf
                <div class="p-4 border-b border-slate-800 bg-slate-950/50 flex items-center justify-between gap-3">
                    <div class="relative flex-1">
                        <input type="text" id="assign_student_search" onkeyup="filterAssignStudentList()" placeholder="Quick filter student name or email..." class="w-full pl-8 pr-3 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-xs text-slate-200 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-emerald-500">
                        <svg class="w-3.5 h-3.5 text-slate-500 absolute left-2.5 top-2.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                    </div>
                    <span id="assign_student_count_badge" class="text-xs font-semibold text-emerald-400 bg-emerald-500/10 px-2.5 py-1 rounded-lg border border-emerald-500/20 whitespace-nowrap">0 / 100 Selected</span>
                </div>

                <div class="p-6 overflow-y-auto space-y-2 flex-1 max-h-96" id="assign_students_checkbox_container">
                    @foreach ($allStudents as $student)
                        <label class="assign-student-item flex items-center justify-between p-3 rounded-xl bg-slate-950/60 border border-slate-800/80 hover:border-emerald-500/40 cursor-pointer transition-all" data-name="{{ strtolower($student->name) }}" data-email="{{ strtolower($student->email) }}">
                            <div class="flex items-center space-x-3">
                                <input type="checkbox" name="student_ids[]" value="{{ $student->id }}" onchange="updateAssignSelectedCount()" class="assign-student-checkbox rounded bg-slate-900 border-slate-700 text-emerald-600 focus:ring-emerald-500">
                                <div>
                                    <span class="text-sm font-semibold text-white block">{{ $student->name }}</span>
                                    <span class="text-xs text-slate-400">{{ $student->email }}</span>
                                </div>
                            </div>
                            <span class="text-[11px] text-slate-500">#{{ str_pad($student->id, 4, '0', STR_PAD_LEFT) }}</span>
                        </label>
                    @endforeach
                </div>

                <div class="px-6 py-4 border-t border-slate-800 bg-slate-950/80 flex items-center justify-between shrink-0">
                    <button type="button" onclick="document.getElementById('assignStudentsModal').classList.add('hidden')" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold transition-colors cursor-pointer">Cancel</button>
                    <button type="submit" class="px-5 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold shadow-lg shadow-emerald-600/30 transition-all cursor-pointer">Save Assignments</button>
                </div>
            </form>
        </div>
    </div>

    <script>
        function openEditStandardModal(data) {
            const form = document.getElementById('editStandardForm');
            if (form) form.action = '/standards/' + data.id;
            const nameInput = document.getElementById('edit_standard_name');
            if (nameInput) nameInput.value = data.name || '';
            const sylInput = document.getElementById('edit_standard_syllabus_id');
            if (sylInput && data.syllabus_id) sylInput.value = data.syllabus_id;
            document.getElementById('editStandardModal').classList.remove('hidden');
        }

        function openAssignStudentsModal(data) {
            const form = document.getElementById('assignStudentsForm');
            if (form) form.action = '/standards/' + data.id + '/assign-students';
            document.getElementById('assign_modal_standard_title').textContent = 'Assign Students to ' + data.name;

            const selectedIds = (data.student_ids || []).map(String);
            const checkboxes = document.querySelectorAll('.assign-student-checkbox');
            checkboxes.forEach(cb => {
                cb.checked = selectedIds.includes(String(cb.value));
            });
            updateAssignSelectedCount();
            document.getElementById('assignStudentsModal').classList.remove('hidden');
        }

        function updateAssignSelectedCount() {
            const checked = document.querySelectorAll('.assign-student-checkbox:checked').length;
            const badge = document.getElementById('assign_student_count_badge');
            if (badge) {
                badge.textContent = checked + ' / 100 Selected';
                if (checked > 100) {
                    badge.classList.remove('text-emerald-400', 'bg-emerald-500/10', 'border-emerald-500/20');
                    badge.classList.add('text-rose-400', 'bg-rose-500/10', 'border-rose-500/20');
                } else {
                    badge.classList.remove('text-rose-400', 'bg-rose-500/10', 'border-rose-500/20');
                    badge.classList.add('text-emerald-400', 'bg-emerald-500/10', 'border-emerald-500/20');
                }
            }
        }

        function filterAssignStudentList() {
            const q = (document.getElementById('assign_student_search')?.value || '').toLowerCase();
            const items = document.querySelectorAll('.assign-student-item');
            items.forEach(el => {
                const name = el.getAttribute('data-name') || '';
                const email = el.getAttribute('data-email') || '';
                if (name.includes(q) || email.includes(q)) {
                    el.style.display = 'flex';
                } else {
                    el.style.display = 'none';
                }
            });
    </script>

    <x-standard-chapters-modal :subjects="$subjects" :standards="$standards" />
</x-layouts.app>
