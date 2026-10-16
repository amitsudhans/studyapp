<x-layouts.app title="Dashboard - Study App">
    <div class="py-8 w-full px-4 sm:px-6 lg:px-8 space-y-8">
        
        @if ($isAdmin)
            <!-- ADMIN DASHBOARD (Type = 2) -->
            
            <!-- Hero Banner -->
            <div class="relative overflow-hidden rounded-2xl bg-gradient-to-r from-indigo-950 via-slate-900 to-slate-900 border border-indigo-500/30 p-6 sm:p-8 shadow-2xl">
                <div class="relative z-10 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-6">
                    <div>
                        <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-indigo-500/20 border border-indigo-500/40 text-indigo-300 text-xs font-semibold uppercase tracking-wider mb-3">
                            <span class="w-2 h-2 rounded-full bg-indigo-400 animate-pulse"></span>
                            <span>System Administrator</span>
                        </div>
                        <h1 class="text-3xl font-extrabold text-white tracking-tight sm:text-4xl">
                            Admin Control Panel
                        </h1>
                        <p class="mt-2 text-slate-300 text-sm max-w-xl">
                            Welcome, <span class="text-indigo-300 font-semibold">{{ $user->name }}</span>! Manage users, assign standards, and create/edit questions below.
                        </p>
                    </div>

                    <div class="flex items-center flex-wrap gap-3">
                        <a href="{{ route('exams.index') }}" class="px-5 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-sm transition-all shadow-lg shadow-indigo-600/30 flex items-center space-x-2 cursor-pointer">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                            </svg>
                            <span>Exams Management</span>
                        </a>
                        <a href="{{ route('questions.index') }}" class="px-5 py-2.5 rounded-xl bg-violet-600 hover:bg-violet-500 text-white font-semibold text-sm transition-all shadow-lg shadow-violet-600/30 flex items-center space-x-2 cursor-pointer">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                            </svg>
                            <span>Questions Bank</span>
                        </a>
                        <button onclick="toggleStandardsDirectory()" class="px-5 py-2.5 rounded-xl bg-teal-600 hover:bg-teal-500 text-white font-semibold text-sm transition-all shadow-lg shadow-teal-600/30 flex items-center space-x-2 cursor-pointer">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
                            </svg>
                            <span>Standards Directory</span>
                        </button>
                        @php
                            $firstAdminStd = ($allStandardsForSelect ?? $standards)->first();
                        @endphp
                        <button type="button" onclick="openStandardChaptersModal({{ $firstAdminStd?->id ?? 1 }}, '{{ addslashes($firstAdminStd?->name ?? 'Class Standard') }}')" class="px-5 py-2.5 rounded-xl bg-purple-600 hover:bg-purple-500 text-white font-semibold text-sm transition-all shadow-lg shadow-purple-600/30 flex items-center space-x-2 cursor-pointer">
                            <span class="text-base">📚</span>
                            <span>Curriculum (Chapters & Topics)</span>
                        </button>
                        <button onclick="document.getElementById('createStandardModal').classList.remove('hidden')" class="px-5 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-semibold text-sm transition-all shadow-lg shadow-emerald-600/30 flex items-center space-x-2 cursor-pointer">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
                            </svg>
                            <span>Add Standard</span>
                        </button>
                        <button onclick="document.getElementById('createUserModal').classList.remove('hidden')" class="px-5 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-white font-semibold text-sm transition-all border border-slate-700 flex items-center space-x-2 cursor-pointer">
                            <svg class="w-5 h-5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
                            </svg>
                            <span>Add New User</span>
                        </button>
                    </div>
                </div>
            </div>

            <!-- Stats Overview -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Total Users</span>
                        <div class="p-2 bg-indigo-500/10 rounded-lg text-indigo-400">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
                        </div>
                    </div>
                    <p class="mt-4 text-3xl font-extrabold text-white">{{ $totalUsersCount ?? $users->count() }}</p>
                    <p class="mt-1 text-xs text-slate-400">Registered system accounts</p>
                </div>

                <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Teachers (Type 1)</span>
                        <div class="p-2 bg-emerald-500/10 rounded-lg text-emerald-400">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
                        </div>
                    </div>
                    <p class="mt-4 text-3xl font-extrabold text-white">{{ $teacherCount ?? $users->filter(fn($u) => ($u->profile?->type ?? 1) == 1)->count() }}</p>
                    <p class="mt-1 text-xs text-slate-400">Teacher profiles</p>
                </div>

                <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Students (Type 2)</span>
                        <div class="p-2 bg-sky-500/10 rounded-lg text-sky-400">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0112 20.055a11.952 11.952 0 01-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"/></svg>
                        </div>
                    </div>
                    <p class="mt-4 text-3xl font-extrabold text-white">{{ $studentCount ?? $users->filter(fn($u) => ($u->profile?->type ?? 1) == 2)->count() }}</p>
                    <p class="mt-1 text-xs text-slate-400">Student accounts</p>
                </div>

                <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Administrators (Type 3)</span>
                        <div class="p-2 bg-violet-500/10 rounded-lg text-violet-400">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
                        </div>
                    </div>
                    <p class="mt-4 text-3xl font-extrabold text-white">{{ $adminCount ?? $users->filter(fn($u) => ($u->profile?->type ?? 1) == 3)->count() }}</p>
                    <p class="mt-1 text-xs text-slate-400">Admin accounts</p>
                </div>
            </div>

            <!-- Users Listing Table -->
            <div class="bg-slate-900 border border-slate-800 rounded-2xl shadow-xl overflow-hidden">
                <div class="px-6 py-5 border-b border-slate-800 flex flex-col md:flex-row md:items-center justify-between gap-4">
                    <div>
                        <h3 class="text-lg font-semibold text-white flex items-center space-x-2">
                            <span>Users Directory</span>
                            @if(request()->filled('role') || request()->filled('admin_search'))
                                <span class="text-xs px-2.5 py-0.5 rounded-full bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 font-medium">Filtered</span>
                            @endif
                        </h3>
                        <p class="text-xs text-slate-400 mt-0.5">Filter by role (Teacher, Student, Admin) and search by keyword.</p>
                    </div>

                    <!-- Role & Word Search Filter Form -->
                    <form method="GET" action="{{ route('dashboard') }}" class="flex flex-wrap items-center gap-2">
                        <!-- Role Filter -->
                        <select name="role" class="px-3 py-2 rounded-lg bg-slate-950 border border-slate-700 text-slate-200 text-xs focus:outline-none focus:ring-2 focus:ring-indigo-500">
                            <option value="">All Roles (Teacher, Student, Admin)</option>
                            <option value="1" {{ request('role') == '1' ? 'selected' : '' }}>Teacher</option>
                            <option value="2" {{ request('role') == '2' ? 'selected' : '' }}>Student</option>
                            <option value="3" {{ request('role') == '3' ? 'selected' : '' }}>Administrator</option>
                        </select>

                        <!-- Keyword Search Input -->
                        <div class="relative">
                            <input type="text" name="admin_search" value="{{ request('admin_search') }}" placeholder="Search name, email, mobile..." class="w-48 sm:w-64 pl-8 pr-3 py-2 rounded-lg bg-slate-950 border border-slate-700 text-slate-200 text-xs placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500">
                            <svg class="w-4 h-4 text-slate-500 absolute left-2.5 top-2.5 pointer-events-none" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                        </div>

                        <!-- Search Button -->
                        <button type="submit" class="px-3.5 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-xs shadow-md transition-all inline-flex items-center space-x-1 cursor-pointer">
                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                            <span>Search</span>
                        </button>

                        <!-- Clear Filter Button -->
                        @if(request()->filled('role') || request()->filled('admin_search'))
                            <a href="{{ route('dashboard') }}" class="px-3 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-medium border border-slate-700 transition-colors">
                                Clear
                            </a>
                        @endif
                    </form>
                </div>

                <div class="overflow-x-auto">
                    <table class="w-full text-left border-collapse text-sm">
                        <thead>
                            <tr class="bg-slate-950/60 border-b border-slate-800 text-slate-400 uppercase text-[11px] font-semibold tracking-wider">
                                <th class="py-3.5 px-6">User Name</th>
                                <th class="py-3.5 px-6">Email Address</th>
                                <th class="py-3.5 px-6">Mobile</th>
                                <th class="py-3.5 px-6">Address</th>
                                <th class="py-3.5 px-6">School / Designation</th>
                                <th class="py-3.5 px-6">Assigned Standards</th>
                                <th class="py-3.5 px-6">Type</th>
                                <th class="py-3.5 px-6">Status</th>
                                <th class="py-3.5 px-6 text-right">Actions</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-800/60 text-slate-300">
                            @foreach ($users as $u)
                                <tr class="hover:bg-slate-800/40 transition-colors">
                                    <td class="py-4 px-6 font-medium text-white flex items-center space-x-3">
                                        <div class="w-8 h-8 rounded-full bg-slate-800 border border-slate-700 text-indigo-400 font-semibold flex items-center justify-center text-xs shrink-0">
                                            {{ strtoupper(substr($u->name, 0, 1)) }}
                                        </div>
                                        <span>{{ $u->name }}</span>
                                    </td>
                                    <td class="py-4 px-6 text-indigo-300 font-mono text-xs">{{ $u->email }}</td>
                                    <td class="py-4 px-6">{{ $u->profile?->mobile ?? 'N/A' }}</td>
                                    <td class="py-4 px-6 max-w-xs truncate" title="{{ $u->profile?->address }}">{{ $u->profile?->address ?? 'N/A' }}</td>
                                    <td class="py-4 px-6">
                                        <div class="font-medium text-slate-200">{{ $u->profile?->school ?? '-' }}</div>
                                        <div class="text-xs text-slate-400">{{ $u->profile?->designation ?? '-' }}</div>
                                    </td>
                                    <td class="py-4 px-6">
                                        @if(($u->profile?->type ?? 1) == 2 && $u->student?->standard)
                                            <span class="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-sky-500/10 text-sky-300 border border-sky-500/20">
                                                {{ $u->student->standard->name }}
                                            </span>
                                        @elseif($u->standards->count() > 0)
                                            <div class="flex flex-wrap gap-1 max-w-xs">
                                                @foreach($u->standards as $std)
                                                    <span class="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-slate-800 text-slate-300 border border-slate-700">
                                                        {{ $std->name }}
                                                    </span>
                                                @endforeach
                                            </div>
                                        @else
                                            <span class="text-xs text-slate-500">None assigned</span>
                                        @endif
                                    </td>
                                    <td class="py-4 px-6">
                                        @if(($u->profile?->type ?? 1) == 3)
                                            <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold bg-violet-500/10 text-violet-400 border border-violet-500/20">Administrator</span>
                                        @elseif(($u->profile?->type ?? 1) == 2)
                                            <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold bg-sky-500/10 text-sky-400 border border-sky-500/20">Student</span>
                                        @else
                                            <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Teacher</span>
                                        @endif
                                    </td>
                                    <td class="py-4 px-6">
                                        @if(($u->status ?? 1) == 1)
                                            <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Active (1)</span>
                                        @else
                                            <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold bg-rose-500/10 text-rose-400 border border-rose-500/20">Inactive (0)</span>
                                        @endif
                                    </td>
                                    <td class="py-4 px-6 text-right space-x-2">
                                        @if($u->id !== $user->id)
                                            <button type="button" onclick="openChatModal({{ $u->id }})" class="px-3 py-1.5 rounded-lg bg-indigo-950/80 hover:bg-indigo-900/80 text-indigo-300 text-xs font-medium border border-indigo-800/40 transition-colors inline-flex items-center space-x-1 cursor-pointer">
                                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"/></svg>
                                                <span>Chat</span>
                                            </button>
                                        @endif
                                        <button onclick="openEditUserModal({{ json_encode([
                                            'id' => $u->id,
                                            'name' => $u->name,
                                            'email' => $u->email,
                                            'mobile' => $u->profile?->mobile ?? '',
                                            'address' => $u->profile?->address ?? '',
                                            'type' => $u->profile?->type ?? 1,
                                            'school' => $u->profile?->school ?? '',
                                            'designation' => $u->profile?->designation ?? '',
                                            'remark' => $u->profile?->remark ?? '',
                                            'status' => $u->status ?? 1,
                                            'standards' => $u->standards->pluck('id')->toArray(),
                                            'standard_id' => $u->student?->standard_id,
                                        ]) }})" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-indigo-300 text-xs font-medium border border-slate-700 transition-colors inline-flex items-center space-x-1 cursor-pointer">
                                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/></svg>
                                            <span>Edit</span>
                                        </button>
                                        @if($u->id !== $user->id)
                                            <form method="POST" action="{{ route('admin.users.destroy', $u) }}" class="inline" onsubmit="return confirm('Are you sure you want to delete this user?')">
                                                @csrf
                                                @method('DELETE')
                                                <button type="submit" class="px-3 py-1.5 rounded-lg bg-red-950/60 hover:bg-red-900/60 text-red-300 text-xs font-medium border border-red-800/40 transition-colors inline-flex items-center space-x-1 cursor-pointer">
                                                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/></svg>
                                                    <span>Delete</span>
                                                </button>
                                            </form>
                                        @endif
                                    </td>
                                </tr>
                            @endforeach
                        </tbody>
                    </table>
                </div>

                @if($users && method_exists($users, 'hasPages') && $users->hasPages())
                    <div class="px-6 py-4 border-t border-slate-800">
                        {{ $users->links() }}
                    </div>
                @endif
            </div>

            <!-- Change Password Section (Admin Only) -->
            <div class="bg-slate-900 border border-slate-800 rounded-2xl shadow-xl overflow-hidden">
                <div class="px-6 py-5 border-b border-slate-800 flex items-center justify-between">
                    <div class="flex items-center space-x-3">
                        <div class="p-2 rounded-lg bg-indigo-500/10 text-indigo-400">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>
                            </svg>
                        </div>
                        <div>
                            <h3 class="text-lg font-semibold text-white">Change Admin Password</h3>
                            <p class="text-xs text-slate-400">Update your account credentials securely.</p>
                        </div>
                    </div>
                    <span class="text-xs font-semibold px-2.5 py-1 rounded-full bg-indigo-500/10 text-indigo-300 border border-indigo-500/20">Admin Only</span>
                </div>

                <form method="POST" action="{{ route('admin.change-password') }}" class="p-6 space-y-4">
                    @csrf
                    <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                        <div>
                            <label for="admin_current_password" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Current Password <span class="text-red-400">*</span></label>
                            <input type="password" id="admin_current_password" name="current_password" required placeholder="Current Password" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('current_password') border-red-500 focus:ring-red-500 @enderror">
                            @error('current_password')
                                <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                            @enderror
                        </div>

                        <div>
                            <label for="admin_new_password" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">New Password <span class="text-red-400">*</span></label>
                            <input type="password" id="admin_new_password" name="password" required placeholder="Min 8 chars" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('password') border-red-500 focus:ring-red-500 @enderror">
                            @error('password')
                                <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                            @enderror
                        </div>

                        <div>
                            <label for="admin_password_confirmation" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Confirm New Password <span class="text-red-400">*</span></label>
                            <input type="password" id="admin_password_confirmation" name="password_confirmation" required placeholder="Re-enter New Password" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm">
                        </div>
                    </div>

                    <div class="pt-2 flex justify-start">
                        <button type="submit" class="px-5 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-semibold shadow-lg shadow-indigo-600/30 transition-all flex items-center space-x-2 cursor-pointer">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                            </svg>
                            <span>Update Admin Password</span>
                        </button>
                    </div>
                </form>
            </div>

            <!-- CREATE USER MODAL -->
            @php
                $isCreateModalOpen = $errors->any() && old('_method') !== 'PUT';
            @endphp
            <div id="createUserModal" class="{{ $isCreateModalOpen ? '' : 'hidden' }} fixed inset-0 z-50 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4 overflow-y-auto">
                <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-2xl overflow-hidden shadow-2xl my-8">
                    <div class="px-6 py-4 border-b border-slate-800 flex items-center justify-between bg-slate-950/50">
                        <h3 class="text-lg font-bold text-white">Add New User / Teacher</h3>
                        <button onclick="document.getElementById('createUserModal').classList.add('hidden')" class="text-slate-400 hover:text-white transition-colors cursor-pointer">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                        </button>
                    </div>

                    <form method="POST" action="{{ route('admin.users.store') }}" class="p-6 space-y-4">
                        @csrf
                        
                        @if ($isCreateModalOpen && $errors->any())
                            <div class="p-3.5 rounded-xl bg-red-950/80 border border-red-500/40 text-red-200 text-xs">
                                <span class="font-bold flex items-center gap-1 text-red-300">
                                    <svg class="w-4 h-4 inline" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                                    Validation errors occurred. Please check the fields below.
                                </span>
                            </div>
                        @endif

                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                            <!-- Name (Mandatory) -->
                            <div>
                                <label for="create_name" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Full Name <span class="text-red-400">*</span></label>
                                <input type="text" id="create_name" name="name" required value="{{ old('name') }}" placeholder="John Doe" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('name') border-red-500 focus:ring-red-500 @enderror">
                                @error('name')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>

                            <!-- Email (Mandatory) -->
                            <div>
                                <label for="create_email" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Email Address <span class="text-red-400">*</span></label>
                                <input type="email" id="create_email" name="email" required value="{{ old('email') }}" placeholder="john@example.com" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('email') border-red-500 focus:ring-red-500 @enderror">
                                @error('email')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>

                            <!-- Password (Mandatory) -->
                            <div>
                                <label for="create_password" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Password <span class="text-red-400">*</span></label>
                                <input type="password" id="create_password" name="password" required placeholder="Min. 8 characters" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('password') border-red-500 focus:ring-red-500 @enderror">
                                @error('password')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>

                            <!-- Mobile (Mandatory) -->
                            <div>
                                <label for="create_mobile" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Mobile Number <span class="text-red-400">*</span></label>
                                <input type="text" id="create_mobile" name="mobile" required value="{{ old('mobile') }}" placeholder="+1234567890" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('mobile') border-red-500 focus:ring-red-500 @enderror">
                                @error('mobile')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>
                        </div>

                        <!-- Address (Mandatory) -->
                        <div>
                            <label for="create_address" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Address <span class="text-red-400">*</span></label>
                            <textarea id="create_address" name="address" rows="2" required placeholder="Full street address" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('address') border-red-500 focus:ring-red-500 @enderror">{{ old('address') }}</textarea>
                            @error('address')
                                <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                            @enderror
                        </div>

                        <!-- User Type & Status Selection -->
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                            <div>
                                <label for="create_type" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">User Type <span class="text-red-400">*</span></label>
                                <select id="create_type" name="type" onchange="toggleCreateUserTypeFields(this.value)" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm">
                                    <option value="1" {{ old('type', '1') == '1' ? 'selected' : '' }}>Teacher (1)</option>
                                    <option value="2" {{ old('type') == '2' ? 'selected' : '' }}>Student (2)</option>
                                    <option value="3" {{ old('type') == '3' ? 'selected' : '' }}>Administrator (3)</option>
                                </select>
                                @error('type')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>

                            <div>
                                <label for="create_status" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Status</label>
                                <select id="create_status" name="status" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm">
                                    <option value="1" {{ old('status', '1') == '1' ? 'selected' : '' }}>Active (1)</option>
                                    <option value="0" {{ old('status') == '0' ? 'selected' : '' }}>Inactive (0)</option>
                                </select>
                                @error('status')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>
                        </div>

                        <!-- Teacher Standards (Multiple) -->
                        <div id="create_teacher_standards_wrapper">
                            <label class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-2">Assign Standards (Teacher)</label>
                            <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 bg-slate-950 p-3 rounded-lg border border-slate-800 max-h-36 overflow-y-auto">
                                @foreach($allStandardsForSelect ?? $standards as $std)
                                    <label class="inline-flex items-center space-x-2 text-xs text-slate-300 cursor-pointer hover:text-white">
                                        <input type="checkbox" name="standards[]" value="{{ $std->id }}" {{ in_array($std->id, old('standards', [])) ? 'checked' : '' }} class="rounded bg-slate-900 border-slate-700 text-indigo-600 focus:ring-indigo-500">
                                        <span>{{ $std->name }}</span>
                                    </label>
                                @endforeach
                            </div>
                            @error('standards')
                                <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                            @enderror
                        </div>

                        <!-- Student Class / Standard (Single) -->
                        <div id="create_student_standard_wrapper" class="hidden">
                            <label for="create_standard_id" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Select Class / Standard (Student) <span class="text-red-400">*</span></label>
                            <select id="create_standard_id" name="standard_id" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm">
                                <option value="">-- Select Class --</option>
                                @foreach($allStandardsForSelect ?? $standards as $std)
                                    @php
                                        $count = $std->students_count ?? $std->students->count();
                                        $isFull = $count >= 100;
                                    @endphp
                                    <option value="{{ $std->id }}" {{ old('standard_id') == $std->id ? 'selected' : '' }} {{ $isFull ? 'disabled' : '' }}>
                                        {{ $std->name }} ({{ $count }}/100 students){{ $isFull ? ' - CLASS FULL' : '' }}
                                    </option>
                                @endforeach
                            </select>
                            @error('standard_id')
                                <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                            @enderror
                        </div>

                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                            <!-- School (Optional) -->
                            <div>
                                <label for="create_school" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">School</label>
                                <input type="text" id="create_school" name="school" value="{{ old('school') }}" placeholder="School Name" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('school') border-red-500 focus:ring-red-500 @enderror">
                                @error('school')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>

                            <!-- Designation (Optional) -->
                            <div>
                                <label for="create_designation" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Designation</label>
                                <input type="text" id="create_designation" name="designation" value="{{ old('designation') }}" placeholder="Teacher, Coordinator, etc." class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('designation') border-red-500 focus:ring-red-500 @enderror">
                                @error('designation')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>
                        </div>

                        <!-- Remark (Optional) -->
                        <div>
                            <label for="create_remark" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Remark</label>
                            <textarea id="create_remark" name="remark" rows="2" placeholder="Additional notes" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('remark') border-red-500 focus:ring-red-500 @enderror">{{ old('remark') }}</textarea>
                            @error('remark')
                                <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                            @enderror
                        </div>

                        <div class="pt-4 flex justify-end space-x-3 border-t border-slate-800">
                            <button type="button" onclick="document.getElementById('createUserModal').classList.add('hidden')" class="px-4 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-sm font-medium transition-colors cursor-pointer">Cancel</button>
                            <button type="submit" class="px-5 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-semibold shadow-lg shadow-indigo-600/30 transition-all cursor-pointer">Create User</button>
                        </div>
                    </form>
                </div>
            </div>

            <!-- EDIT USER MODAL -->
            @php
                $isEditModalOpen = $errors->any() && old('_method') === 'PUT';
            @endphp
            <div id="editUserModal" class="{{ $isEditModalOpen ? '' : 'hidden' }} fixed inset-0 z-50 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4 overflow-y-auto">
                <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-2xl overflow-hidden shadow-2xl my-8">
                    <div class="px-6 py-4 border-b border-slate-800 flex items-center justify-between bg-slate-950/50">
                        <h3 class="text-lg font-bold text-white">Edit User / Teacher</h3>
                        <button onclick="document.getElementById('editUserModal').classList.add('hidden')" class="text-slate-400 hover:text-white transition-colors cursor-pointer">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                        </button>
                    </div>

                    <form id="editUserForm" method="POST" action="{{ old('_edit_action_url', '') }}" class="p-6 space-y-4">
                        @csrf
                        @method('PUT')
                        <input type="hidden" id="edit_action_url" name="_edit_action_url" value="{{ old('_edit_action_url', '') }}">
                        
                        @if ($isEditModalOpen && $errors->any())
                            <div class="p-3.5 rounded-xl bg-red-950/80 border border-red-500/40 text-red-200 text-xs">
                                <span class="font-bold flex items-center gap-1 text-red-300">
                                    <svg class="w-4 h-4 inline" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                                    Validation errors occurred. Please check the fields below.
                                </span>
                            </div>
                        @endif

                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                            <!-- Name (Mandatory) -->
                            <div>
                                <label for="edit_name" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Full Name <span class="text-red-400">*</span></label>
                                <input type="text" id="edit_name" name="name" required value="{{ old('name') }}" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('name') border-red-500 focus:ring-red-500 @enderror">
                                @error('name')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>

                            <!-- Email (Mandatory) -->
                            <div>
                                <label for="edit_email" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Email Address <span class="text-red-400">*</span></label>
                                <input type="email" id="edit_email" name="email" required value="{{ old('email') }}" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('email') border-red-500 focus:ring-red-500 @enderror">
                                @error('email')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>

                            <!-- Password (Optional on update) -->
                            <div>
                                <label for="edit_password" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Password (Leave blank to keep)</label>
                                <input type="password" id="edit_password" name="password" placeholder="New password" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('password') border-red-500 focus:ring-red-500 @enderror">
                                @error('password')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>

                            <!-- Mobile (Mandatory) -->
                            <div>
                                <label for="edit_mobile" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Mobile Number <span class="text-red-400">*</span></label>
                                <input type="text" id="edit_mobile" name="mobile" required value="{{ old('mobile') }}" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('mobile') border-red-500 focus:ring-red-500 @enderror">
                                @error('mobile')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>
                        </div>

                        <!-- Address (Mandatory) -->
                        <div>
                            <label for="edit_address" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Address <span class="text-red-400">*</span></label>
                            <textarea id="edit_address" name="address" rows="2" required class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('address') border-red-500 focus:ring-red-500 @enderror">{{ old('address') }}</textarea>
                            @error('address')
                                <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                            @enderror
                        </div>

                        <!-- User Type & Status Selection -->
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                            <div>
                                <label for="edit_type" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">User Type <span class="text-[10px] text-slate-500 font-normal lowercase">(read-only)</span></label>
                                <select id="edit_type" disabled class="w-full px-3.5 py-2.5 rounded-lg bg-slate-900 border border-slate-800 text-slate-400 focus:outline-none text-sm cursor-not-allowed">
                                    <option value="1">Teacher (1)</option>
                                    <option value="2">Student (2)</option>
                                    <option value="3">Administrator (3)</option>
                                </select>
                            </div>

                            <div>
                                <label for="edit_status" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Status</label>
                                <select id="edit_status" name="status" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm">
                                    <option value="1">Active (1)</option>
                                    <option value="0">Inactive (0)</option>
                                </select>
                                @error('status')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>
                        </div>

                        <!-- Teacher Standards (Multiple) -->
                        <div id="edit_teacher_standards_wrapper">
                            <label class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-2">Assign Standards (Teacher)</label>
                            <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 bg-slate-950 p-3 rounded-lg border border-slate-800 max-h-36 overflow-y-auto">
                                @foreach($allStandardsForSelect ?? $standards as $std)
                                    <label class="inline-flex items-center space-x-2 text-xs text-slate-300 cursor-pointer hover:text-white">
                                        <input type="checkbox" name="standards[]" value="{{ $std->id }}" class="edit-std-checkbox rounded bg-slate-900 border-slate-700 text-indigo-600 focus:ring-indigo-500">
                                        <span>{{ $std->name }}</span>
                                    </label>
                                @endforeach
                            </div>
                            @error('standards')
                                <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                            @enderror
                        </div>

                        <!-- Student Class / Standard (Single) -->
                        <div id="edit_student_standard_wrapper" class="hidden">
                            <label for="edit_standard_id" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Select Class / Standard (Student)</label>
                            <select id="edit_standard_id" name="standard_id" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm">
                                <option value="">-- Select Class --</option>
                                @foreach($allStandardsForSelect ?? $standards as $std)
                                    @php
                                        $count = $std->students_count ?? $std->students->count();
                                    @endphp
                                    <option value="{{ $std->id }}" data-count="{{ $count }}" data-base-name="{{ $std->name }}">
                                        {{ $std->name }} ({{ $count }}/100 students)
                                    </option>
                                @endforeach
                            </select>
                            @error('standard_id')
                                <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                            @enderror
                        </div>

                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                            <!-- School (Optional) -->
                            <div>
                                <label for="edit_school" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">School</label>
                                <input type="text" id="edit_school" name="school" value="{{ old('school') }}" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('school') border-red-500 focus:ring-red-500 @enderror">
                                @error('school')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>

                            <!-- Designation (Optional) -->
                            <div>
                                <label for="edit_designation" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Designation</label>
                                <input type="text" id="edit_designation" name="designation" value="{{ old('designation') }}" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('designation') border-red-500 focus:ring-red-500 @enderror">
                                @error('designation')
                                    <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                                @enderror
                            </div>
                        </div>

                        <!-- Remark (Optional) -->
                        <div>
                            <label for="edit_remark" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Remark</label>
                            <textarea id="edit_remark" name="remark" rows="2" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('remark') border-red-500 focus:ring-red-500 @enderror">{{ old('remark') }}</textarea>
                            @error('remark')
                                <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                            @enderror
                        </div>

                        <div class="pt-4 flex justify-end space-x-3 border-t border-slate-800">
                            <button type="button" onclick="document.getElementById('editUserModal').classList.add('hidden')" class="px-4 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-sm font-medium transition-colors cursor-pointer">Cancel</button>
                            <button type="submit" class="px-5 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-semibold shadow-lg shadow-indigo-600/30 transition-all cursor-pointer">Update User</button>
                        </div>
                    </form>
                </div>
            </div>

            <script>
                function toggleCreateUserTypeFields(typeVal) {
                    const teacherWrapper = document.getElementById('create_teacher_standards_wrapper');
                    const studentWrapper = document.getElementById('create_student_standard_wrapper');
                    const typeInt = parseInt(typeVal);
                    if (typeInt === 2) { // Student
                        teacherWrapper.classList.add('hidden');
                        studentWrapper.classList.remove('hidden');
                    } else if (typeInt === 1) { // Teacher
                        teacherWrapper.classList.remove('hidden');
                        studentWrapper.classList.add('hidden');
                    } else { // Administrator (3)
                        teacherWrapper.classList.add('hidden');
                        studentWrapper.classList.add('hidden');
                    }
                }

                function toggleEditUserTypeFields(typeVal) {
                    const teacherWrapper = document.getElementById('edit_teacher_standards_wrapper');
                    const studentWrapper = document.getElementById('edit_student_standard_wrapper');
                    const typeInt = parseInt(typeVal);
                    if (typeInt === 2) { // Student
                        teacherWrapper.classList.add('hidden');
                        studentWrapper.classList.remove('hidden');
                    } else if (typeInt === 1) { // Teacher
                        teacherWrapper.classList.remove('hidden');
                        studentWrapper.classList.add('hidden');
                    } else { // Administrator (3)
                        teacherWrapper.classList.add('hidden');
                        studentWrapper.classList.add('hidden');
                    }
                }

                function openEditUserModal(data) {
                    const actionUrl = '/admin/users/' + data.id;
                    document.getElementById('editUserForm').action = actionUrl;
                    document.getElementById('edit_action_url').value = actionUrl;
                    document.getElementById('edit_name').value = data.name || '';
                    document.getElementById('edit_email').value = data.email || '';
                    document.getElementById('edit_mobile').value = data.mobile || '';
                    document.getElementById('edit_address').value = data.address || '';
                    document.getElementById('edit_school').value = data.school || '';
                    document.getElementById('edit_designation').value = data.designation || '';
                    document.getElementById('edit_remark').value = data.remark || '';
                    document.getElementById('edit_status').value = data.status !== undefined ? data.status : 1;
                    
                    const userType = data.type !== undefined ? data.type : 1;
                    document.getElementById('edit_type').value = userType;
                    toggleEditUserTypeFields(userType);

                    document.getElementById('edit_standard_id').value = data.standard_id || '';
                    document.getElementById('edit_password').value = '';

                    // Disable full class options in Edit Modal unless it is student's current class
                    document.querySelectorAll('#edit_standard_id option').forEach(opt => {
                        if (!opt.value) return;
                        const count = parseInt(opt.getAttribute('data-count') || '0');
                        const baseName = opt.getAttribute('data-base-name') || opt.textContent;
                        const isCurrent = parseInt(opt.value) === parseInt(data.standard_id || 0);
                        if (count >= 100 && !isCurrent) {
                            opt.disabled = true;
                            opt.textContent = baseName + ' (' + count + '/100 students) - CLASS FULL';
                        } else {
                            opt.disabled = false;
                            opt.textContent = baseName + ' (' + count + '/100 students)';
                        }
                    });

                    // Pre-select teacher_standards checkboxes
                    const assignedStdIds = data.standards || [];
                    document.querySelectorAll('.edit-std-checkbox').forEach(cb => {
                        cb.checked = assignedStdIds.includes(parseInt(cb.value));
                    });

                    document.getElementById('editUserModal').classList.remove('hidden');
                }

                function openEditStandardModal(data) {
                    const url = '/standards/' + data.id;
                    document.getElementById('editStandardForm').action = url;
                    document.getElementById('edit_standard_url').value = url;
                    document.getElementById('edit_standard_name').value = data.name || '';
                    if (data.syllabus_id) {
                        document.getElementById('edit_standard_syllabus_id').value = data.syllabus_id;
                    }
                    document.getElementById('editStandardModal').classList.remove('hidden');
                }
            </script>

            <!-- Admin All Exams Directory Table -->
            {{-- Commented Admin All Exams Directory Table
            @if(isset($adminExams))
                <div id="adminExamsDirectoryContainer" class="bg-slate-900 border border-slate-800 rounded-2xl shadow-xl overflow-hidden mt-6">
                    <div class="px-6 py-5 border-b border-slate-800 flex items-center justify-between flex-wrap gap-4">
                        <div>
                            <h3 class="text-lg font-semibold text-white flex items-center space-x-2">
                                <svg class="w-5 h-5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
                                </svg>
                                <span>All Exams Directory</span>
                                @if(request()->filled('exam_name') || request()->filled('exam_type') || request()->filled('type') || request()->filled('exam_syllabus_id') || request()->filled('exam_subject_id') || request()->filled('exam_chapter_id') || request()->filled('exam_topic_id'))
                                    <span class="text-xs px-2.5 py-0.5 rounded-full bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 font-medium">Filtered</span>
                                @endif
                            </h3>
                            <p class="text-xs text-slate-400 mt-0.5">Filter and search all exams across the platform by syllabus, subject, chapter, topic, and name</p>
                        </div>
                        <div class="flex items-center space-x-3">
                            <span class="text-xs text-slate-400 bg-slate-800 px-3 py-1 rounded-full border border-slate-700">
                                Total: {{ $adminExams->total() }} Exam(s)
                            </span>
                            <a href="{{ route('exams.index') }}" class="px-3.5 py-1.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold shadow-md transition-all inline-flex items-center space-x-1.5">
                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
                                <span>Manage All Exams</span>
                            </a>
                        </div>
                    </div>

                    <!-- Search & Curriculum Filters Bar for Admin Dashboard -->
                    <div class="p-4 sm:p-5 bg-slate-950/60 border-b border-slate-800/80">
                        <form method="GET" action="{{ route('dashboard') }}" class="space-y-3">
                            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-3">
                                <!-- Exam Name -->
                                <div>
                                    <label class="block text-[11px] font-semibold text-slate-400 uppercase tracking-wider mb-1">Exam Name</label>
                                    <div class="relative">
                                        <input type="text" name="exam_name" value="{{ request('exam_name') }}" placeholder="Search exam name..." class="w-full pl-8 pr-3 py-2 bg-slate-900 border border-slate-800 rounded-xl text-xs text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                        <svg class="w-3.5 h-3.5 text-slate-500 absolute left-2.5 top-2.5 pointer-events-none" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                                    </div>
                                </div>

                                <!-- Exam Type -->
                                <div>
                                    <label class="block text-[11px] font-semibold text-slate-400 uppercase tracking-wider mb-1">Exam Type</label>
                                    <select name="exam_type" id="admin_filter_type" class="w-full px-3 py-2 bg-slate-900 border border-slate-800 rounded-xl text-xs text-slate-200 focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                        <option value="">All Types</option>
                                        <option value="1" {{ (request('exam_type') == '1' || request('type') == '1') ? 'selected' : '' }}>1 - Timed Exam</option>
                                        <option value="2" {{ (request('exam_type') == '2' || request('type') == '2') ? 'selected' : '' }}>2 - Non-Timed Exam</option>
                                        <option value="3" {{ (request('exam_type') == '3' || request('type') == '3') ? 'selected' : '' }}>3 - Text Entry Exam</option>
                                    </select>
                                </div>

                                <!-- Syllabus -->
                                <div>
                                    <label class="block text-[11px] font-semibold text-slate-400 uppercase tracking-wider mb-1">Syllabus</label>
                                    <select name="exam_syllabus_id" id="admin_filter_syllabus" onchange="onAdminFilterSyllabusChange()" class="w-full px-3 py-2 bg-slate-900 border border-slate-800 rounded-xl text-xs text-slate-200 focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                        <option value="">All Syllabuses</option>
                                        @foreach($syllabi as $syl)
                                            <option value="{{ $syl->id }}" {{ request('exam_syllabus_id') == $syl->id ? 'selected' : '' }}>{{ $syl->name }}</option>
                                        @endforeach
                                    </select>
                                </div>

                                <!-- Subject -->
                                <div>
                                    <label class="block text-[11px] font-semibold text-slate-400 uppercase tracking-wider mb-1">Subject</label>
                                    <select name="exam_subject_id" id="admin_filter_subject" onchange="onAdminFilterSubjectChange()" class="w-full px-3 py-2 bg-slate-900 border border-slate-800 rounded-xl text-xs text-slate-200 focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                        <option value="">All Subjects</option>
                                        @foreach($subjects as $subj)
                                            <option value="{{ $subj->id }}" {{ request('exam_subject_id') == $subj->id ? 'selected' : '' }}>{{ $subj->name }}</option>
                                        @endforeach
                                    </select>
                                </div>

                                <!-- Chapter -->
                                <div>
                                    <label class="block text-[11px] font-semibold text-slate-400 uppercase tracking-wider mb-1">Chapter</label>
                                    <select name="exam_chapter_id" id="admin_filter_chapter" onchange="onAdminFilterChapterChange()" class="w-full px-3 py-2 bg-slate-900 border border-slate-800 rounded-xl text-xs text-slate-200 focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                        <option value="">All Chapters</option>
                                        @foreach($chapters as $ch)
                                            <option value="{{ $ch->id }}" {{ request('exam_chapter_id') == $ch->id ? 'selected' : '' }}>{{ $ch->name }}</option>
                                        @endforeach
                                    </select>
                                </div>

                                <!-- Topic -->
                                <div>
                                    <label class="block text-[11px] font-semibold text-slate-400 uppercase tracking-wider mb-1">Topic</label>
                                    <select name="exam_topic_id" id="admin_filter_topic" class="w-full px-3 py-2 bg-slate-900 border border-slate-800 rounded-xl text-xs text-slate-200 focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                        <option value="">All Topics</option>
                                        @foreach($topics as $tp)
                                            <option value="{{ $tp->id }}" {{ request('exam_topic_id') == $tp->id ? 'selected' : '' }}>{{ $tp->name }}</option>
                                        @endforeach
                                    </select>
                                </div>
                            </div>

                            <div class="flex items-center justify-end space-x-2 pt-1">
                                @if(request()->filled('exam_name') || request()->filled('exam_type') || request()->filled('type') || request()->filled('exam_syllabus_id') || request()->filled('exam_subject_id') || request()->filled('exam_chapter_id') || request()->filled('exam_topic_id'))
                                    <a href="{{ route('dashboard') }}" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition-colors inline-flex items-center space-x-1.5">
                                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                                        <span>Clear Filters</span>
                                    </a>
                                @endif
                                <button type="submit" class="px-5 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold shadow-md shadow-indigo-600/30 transition-all inline-flex items-center space-x-1.5 cursor-pointer">
                                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                                    <span>Search Exams</span>
                                </button>
                            </div>
                        </form>
                    </div>

                    <!-- Exam List Table -->
                    @if($adminExams->isNotEmpty())
                        <div class="overflow-x-auto">
                            <table class="w-full text-left text-sm text-slate-300">
                                <thead class="bg-slate-950/60 text-[11px] font-bold text-slate-400 uppercase tracking-wider border-b border-slate-800">
                                    <tr>
                                        <th class="px-6 py-4">Exam Info</th>
                                        <th class="px-6 py-4">Curriculum</th>
                                        <th class="px-6 py-4">Type & Duration</th>
                                        <th class="px-6 py-4">Marks & Questions</th>
                                        <th class="px-6 py-4">Status</th>
                                        <th class="px-6 py-4 text-right">Actions</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-slate-800/80">
                                    @foreach($adminExams as $aExam)
                                        @php
                                            $aMarks = $aExam->total_mark > 0 ? $aExam->total_mark : $aExam->questions->sum('marks');
                                        @endphp
                                        <tr class="hover:bg-slate-800/30 transition-colors">
                                            <td class="px-6 py-4">
                                                <div class="font-bold text-white text-sm hover:text-indigo-300 transition-colors">{{ $aExam->name }}</div>
                                                <div class="text-xs text-slate-400 mt-0.5">By: <span class="text-sky-300 font-medium">{{ $aExam->creator?->name ?? 'System' }}</span></div>
                                            </td>
                                            <td class="px-6 py-4 text-xs space-y-1">
                                                <div class="flex items-center space-x-1.5 flex-wrap">
                                                    @if($aExam->syllabus)
                                                        <span class="px-2 py-0.5 rounded bg-indigo-500/10 text-indigo-300 border border-indigo-500/20 font-medium">{{ $aExam->syllabus->name }}</span>
                                                    @endif
                                                    @if($aExam->subject)
                                                        <span class="px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-300 border border-emerald-500/20 font-medium">{{ $aExam->subject->name }}</span>
                                                    @endif
                                                </div>
                                                @if($aExam->chapter || $aExam->topic)
                                                    <div class="text-[11px] text-slate-400">
                                                        @if($aExam->chapter) <span>Ch: {{ $aExam->chapter->name }}</span> @endif
                                                        @if($aExam->topic) <span class="ml-1">• Top: {{ $aExam->topic->name }}</span> @endif
                                                    </div>
                                                @endif
                                            </td>
                                            <td class="px-6 py-4 text-xs">
                                                <span class="font-semibold text-slate-200">{{ $aExam->type === 1 ? 'Timed' : 'Practice' }}</span>
                                                @if($aExam->type === 1 && $aExam->duration)
                                                    <div class="text-[11px] text-slate-400 mt-0.5">{{ $aExam->duration }} mins</div>
                                                @endif
                                            </td>
                                            <td class="px-6 py-4 text-xs">
                                                <div class="font-bold text-amber-400">{{ $aMarks }} Marks</div>
                                                <div class="text-[11px] text-slate-400 mt-0.5">{{ $aExam->questions->count() }} Questions</div>
                                            </td>
                                            <td class="px-6 py-4 text-xs">
                                                @if($aExam->status === 1)
                                                    <span class="inline-flex items-center px-2 py-0.5 rounded-full text-[11px] font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Active</span>
                                                @else
                                                    <span class="inline-flex items-center px-2 py-0.5 rounded-full text-[11px] font-semibold bg-rose-500/10 text-rose-400 border border-rose-500/20">Inactive</span>
                                                @endif
                                            </td>
                                            <td class="px-6 py-4 text-right">
                                                <div class="inline-flex items-center space-x-2">
                                                    @if(($aExam->student_exam_details_count ?? 0) === 0)
                                                        <button type="button" onclick="openDashboardEditExamModal({{ json_encode([
                                                            'id' => $aExam->id,
                                                            'name' => $aExam->name,
                                                            'type' => $aExam->type,
                                                            'duration' => $aExam->duration,
                                                            'status' => $aExam->status,
                                                            'syllabus_id' => $aExam->syllabus_id,
                                                            'standard_id' => $aExam->standard_id,
                                                            'subject_id' => $aExam->subject_id,
                                                            'chapter_id' => $aExam->chapter_id,
                                                            'topic_id' => $aExam->topic_id,
                                                            'standards' => $aExam->standards->pluck('id')->toArray(),
                                                            'action' => route('exams.update', $aExam->id),
                                                        ]) }})" class="inline-flex items-center space-x-1 px-2.5 py-1.5 rounded-lg bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 border border-amber-500/40 text-xs font-semibold transition-all cursor-pointer">
                                                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/></svg>
                                                            <span>Edit</span>
                                                        </button>
                                                    @endif
                                                    <a href="{{ route('exams.show', $aExam->id) }}" class="inline-flex items-center space-x-1 px-3 py-1.5 rounded-lg bg-indigo-600/20 hover:bg-indigo-600/40 text-indigo-300 border border-indigo-500/30 text-xs font-semibold transition-all">
                                                        <span>Manage Questions</span>
                                                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                                                    </a>
                                                </div>
                                            </td>
                                        </tr>
                                    @endforeach
                                </tbody>
                            </table>
                        </div>
                    @else
                        <div class="p-8 text-center text-slate-400">
                            <svg class="w-10 h-10 mx-auto mb-3 text-slate-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                            @if(request()->filled('exam_name') || request()->filled('exam_syllabus_id') || request()->filled('exam_subject_id') || request()->filled('exam_chapter_id') || request()->filled('exam_topic_id'))
                                <p class="text-slate-300 font-medium text-sm">No exams match your search criteria.</p>
                                <p class="text-xs text-slate-500 mt-1">Try clearing or adjusting your filters to find exams.</p>
                                <a href="{{ route('dashboard') }}" class="inline-block mt-3 px-4 py-1.5 rounded-lg bg-indigo-600/20 text-indigo-300 border border-indigo-500/30 text-xs font-semibold hover:bg-indigo-600/30 transition-colors">Clear All Filters</a>
                            @else
                                <p class="text-sm font-medium">No exams created in the system yet.</p>
                            @endif
                        </div>
                    @endif

                    @if($adminExams && method_exists($adminExams, 'total'))
                        <div class="px-6 py-4 border-t border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs text-slate-400">
                            <div>
                                Showing <span class="font-semibold text-slate-200">{{ $adminExams->firstItem() ?? 0 }}</span>
                                to <span class="font-semibold text-slate-200">{{ $adminExams->lastItem() ?? 0 }}</span>
                                of <span class="font-semibold text-slate-200">{{ $adminExams->total() }}</span> exam(s)
                                (10 per page)
                            </div>
                            @if($adminExams->hasPages())
                                <div>
                                    {{ $adminExams->links() }}
                                </div>
                            @endif
                        </div>
                    @endif
                </div>
            @endif
            --}}

        @elseif($isStudent ?? false)
            <!-- STUDENT DASHBOARD (Type = 2) -->
            <div class="space-y-6">
                <!-- Welcome Hero Banner for Student -->
                <div class="relative overflow-hidden rounded-2xl bg-gradient-to-br from-sky-950 via-slate-900 to-indigo-950 border border-sky-500/20 p-6 sm:p-10 shadow-2xl">
                    <!-- decorative orbs -->
                    <div class="absolute -top-10 -right-10 w-56 h-56 rounded-full bg-sky-500/10 blur-3xl pointer-events-none"></div>
                    <div class="absolute bottom-0 left-10 w-40 h-40 rounded-full bg-indigo-500/10 blur-2xl pointer-events-none"></div>

                    <div class="relative z-10 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-6">
                        <div class="flex items-center gap-5">
                            <!-- Avatar -->
                            <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-sky-500 to-indigo-600 flex items-center justify-center text-white text-2xl font-extrabold shadow-lg shadow-sky-500/30 shrink-0 select-none">
                                {{ strtoupper(substr($user->name, 0, 1)) }}
                            </div>
                            <div>
                                <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-sky-500/10 border border-sky-500/25 text-sky-300 text-[11px] font-semibold uppercase tracking-widest mb-2">
                                    <span class="w-1.5 h-1.5 rounded-full bg-sky-400 animate-pulse"></span>
                                    <span>Student Portal</span>
                                </div>
                                <h1 class="text-2xl sm:text-3xl font-extrabold text-white tracking-tight leading-tight">
                                    Welcome back, <span class="text-sky-300">{{ $user->name }}</span>!
                                </h1>
                                <p class="mt-1.5 text-slate-400 text-sm flex items-center gap-2 flex-wrap">
                                    <svg class="w-3.5 h-3.5 text-slate-500 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
                                    <span>Class / Standard:</span>
                                    @if($user->student?->standard)
                                        <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-bold bg-sky-500/20 text-sky-200 border border-sky-400/40">
                                            {{ $user->student->standard->name }}
                                        </span>
                                    @else
                                        <span class="text-rose-400 font-semibold italic text-xs">Not assigned to any class yet</span>
                                    @endif
                                </p>
                            </div>
                        </div>

                        <div class="shrink-0 flex items-center gap-3">
                            <form method="POST" action="{{ route('logout') }}">
                                @csrf
                                <button type="submit" class="px-4 py-2.5 rounded-xl bg-white/5 hover:bg-white/10 text-slate-300 hover:text-white border border-white/10 font-medium text-sm transition-all shadow-md flex items-center space-x-2 cursor-pointer backdrop-blur-sm">
                                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
                                    </svg>
                                    <span>Sign Out</span>
                                </button>
                            </form>
                        </div>
                    </div>
                </div>

                <!-- Metric Stat Summary for Student -->
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                    <!-- Your Class -->
                    <div class="relative overflow-hidden rounded-2xl bg-slate-900 border border-sky-500/20 p-5 shadow-lg group hover:border-sky-500/40 transition-all">
                        <div class="absolute inset-0 bg-gradient-to-br from-sky-500/5 to-transparent pointer-events-none"></div>
                        <div class="relative flex items-start justify-between">
                            <div>
                                <p class="text-[11px] font-semibold text-sky-400/80 uppercase tracking-widest">Your Class</p>
                                <p class="mt-3 text-xl font-extrabold text-white truncate max-w-[140px]" title="{{ $user->student?->standard?->name ?? 'None' }}">
                                    {{ $user->student?->standard?->name ?? 'N/A' }}
                                </p>
                                <p class="mt-1 text-xs text-slate-500">Enrolled Standard</p>
                            </div>
                            <div class="p-2.5 bg-sky-500/10 rounded-xl text-sky-400 shrink-0">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
                            </div>
                        </div>
                        <div class="mt-4 h-0.5 bg-gradient-to-r from-sky-500/40 to-transparent rounded-full"></div>
                    </div>

                    <!-- Assigned Exams -->
                    <div class="relative overflow-hidden rounded-2xl bg-slate-900 border border-indigo-500/20 p-5 shadow-lg group hover:border-indigo-500/40 transition-all">
                        <div class="absolute inset-0 bg-gradient-to-br from-indigo-500/5 to-transparent pointer-events-none"></div>
                        <div class="relative flex items-start justify-between">
                            <div>
                                <p class="text-[11px] font-semibold text-indigo-400/80 uppercase tracking-widest">Assigned Exams</p>
                                <p class="mt-3 text-4xl font-extrabold text-white">{{ $studentAssignedCount ?? (method_exists($studentExams, 'total') ? $studentExams->total() : $studentExams->count()) }}</p>
                                <p class="mt-1 text-xs text-slate-500">Exams for your class</p>
                            </div>
                            <div class="p-2.5 bg-indigo-500/10 rounded-xl text-indigo-400 shrink-0">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                            </div>
                        </div>
                        <div class="mt-4 h-0.5 bg-gradient-to-r from-indigo-500/40 to-transparent rounded-full"></div>
                    </div>

                    <!-- Active Exams -->
                    <div class="relative overflow-hidden rounded-2xl bg-slate-900 border border-emerald-500/20 p-5 shadow-lg group hover:border-emerald-500/40 transition-all">
                        <div class="absolute inset-0 bg-gradient-to-br from-emerald-500/5 to-transparent pointer-events-none"></div>
                        <div class="relative flex items-start justify-between">
                            <div>
                                <p class="text-[11px] font-semibold text-emerald-400/80 uppercase tracking-widest">Active Exams</p>
                                <p class="mt-3 text-4xl font-extrabold text-emerald-400">{{ $studentActiveCount ?? $studentExams->filter(fn($e) => $e->status == 1 && !in_array($e->id, $submittedExamIds ?? []))->count() }}</p>
                                <p class="mt-1 text-xs text-slate-500">Available to attempt</p>
                            </div>
                            <div class="p-2.5 bg-emerald-500/10 rounded-xl text-emerald-400 shrink-0">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                            </div>
                        </div>
                        <div class="mt-4 h-0.5 bg-gradient-to-r from-emerald-500/40 to-transparent rounded-full"></div>
                    </div>

                    <!-- Total Marks -->
                    <div class="relative overflow-hidden rounded-2xl bg-slate-900 border border-amber-500/20 p-5 shadow-lg group hover:border-amber-500/40 transition-all">
                        <div class="absolute inset-0 bg-gradient-to-br from-amber-500/5 to-transparent pointer-events-none"></div>
                        <div class="relative flex items-start justify-between">
                            <div>
                                <p class="text-[11px] font-semibold text-amber-400/80 uppercase tracking-widest">Total Marks</p>
                                <p class="mt-3 text-4xl font-extrabold text-amber-400">{{ $studentTotalMarks ?? $studentExams->sum('total_mark') }}</p>
                                <p class="mt-1 text-xs text-slate-500">Across assigned exams</p>
                            </div>
                            <div class="p-2.5 bg-amber-500/10 rounded-xl text-amber-400 shrink-0">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"/></svg>
                            </div>
                        </div>
                        <div class="mt-4 h-0.5 bg-gradient-to-r from-amber-500/40 to-transparent rounded-full"></div>
                    </div>
                </div>

                <!-- Student Assigned Exams Directory -->
                <div class="bg-slate-900 border border-slate-800/80 rounded-2xl shadow-xl overflow-hidden">
                    <div class="px-6 py-5 border-b border-slate-800 flex flex-col sm:flex-row sm:items-center justify-between gap-3 bg-slate-950/40">
                        <div class="flex items-center gap-3">
                            <div class="p-2.5 rounded-xl bg-sky-500/10 border border-sky-500/20 text-sky-400 shrink-0">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                                </svg>
                            </div>
                            <div>
                                <h3 class="text-base font-bold text-white tracking-tight">My Assigned Exams</h3>
                                <p class="text-xs text-slate-400 mt-0.5">Standard: <strong class="text-sky-300 font-semibold">{{ $user->student?->standard?->name ?? 'Unassigned' }}</strong></p>
                            </div>
                        </div>
                        <span class="text-xs font-semibold text-slate-300 bg-slate-800 px-3.5 py-1.5 rounded-full border border-slate-700 self-start sm:self-center">
                            {{ method_exists($studentExams, 'total') ? $studentExams->total() : $studentExams->count() }} Exam(s)
                        </span>
                    </div>

                    @if($studentExams->isNotEmpty())
                        <div class="divide-y divide-slate-800/80">
                            @foreach ($studentExams as $exam)
                                @php
                                    $isSubmitted = in_array($exam->id, $submittedExamIds ?? []);
                                    $examDetails = ($submittedDetails[$exam->id] ?? collect());

                                    $obtainedMarks = 0;
                                    $totalExamMarks = $exam->total_mark > 0 ? $exam->total_mark : $exam->questions->sum('marks');

                                    $detailsPayload = $examDetails->map(function($d) use (&$obtainedMarks) {
                                        $qMarks = $d->getQuestionMarks();
                                        $isCorrect = $d->isCorrect();
                                        $earnedMarks = $d->getEarnedMarks();
                                        $obtainedMarks += $earnedMarks;

                                        return [
                                            'question_name' => $d->question?->name ?? 'N/A',
                                            'question_marks' => $qMarks,
                                            'selected_answer' => $d->getSelectedAnswerDisplay(),
                                            'is_correct' => $isCorrect,
                                            'is_partially_correct' => $d->isPartiallyCorrect(),
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
                                @endphp

                                <div class="bg-slate-900/70 hover:bg-slate-800/50 transition-colors group/row">
                                    <!-- Header Row: Displays ONLY Exam Name First -->
                                    <div onclick="toggleStudentExamDetails({{ $exam->id }})" class="px-6 py-4 flex items-center justify-between cursor-pointer select-none">
                                        <div class="flex items-center space-x-4">
                                            <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-sky-500/20 to-indigo-500/10 border border-sky-500/25 text-sky-400 flex items-center justify-center group-hover/row:from-sky-500/30 transition-all shrink-0">
                                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                                            </div>
                                            <div>
                                                <h4 class="text-sm font-bold text-slate-100 group-hover/row:text-sky-300 transition-colors">
                                                    {{ $exam->name }}
                                                </h4>
                                                <p class="text-xs text-slate-500 mt-0.5">Click to expand details &amp; actions</p>
                                            </div>
                                        </div>

                                        <div class="flex items-center space-x-3">
                                            @if($isSubmitted)
                                                <span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-500/15 text-emerald-300 border border-emerald-500/30">
                                                    <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>Submitted
                                                </span>
                                            @elseif($exam->status == 1)
                                                <span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-semibold bg-sky-500/10 text-sky-300 border border-sky-500/20">
                                                    <span class="w-1.5 h-1.5 rounded-full bg-sky-400 animate-pulse"></span>Active
                                                </span>
                                            @else
                                                <span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-semibold bg-rose-500/10 text-rose-400 border border-rose-500/20">
                                                    <span class="w-1.5 h-1.5 rounded-full bg-rose-500"></span>Inactive
                                                </span>
                                            @endif
                                            <div class="p-1.5 rounded-lg bg-slate-800/80 border border-slate-700/60 text-slate-500 group-hover/row:text-sky-400 group-hover/row:border-sky-500/30 transition-all">
                                                <svg id="chevron-exam-{{ $exam->id }}" class="w-4 h-4 transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                                                </svg>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Expandable Details Section (Shown when clicking Exam Name) -->
                                    <div id="details-exam-{{ $exam->id }}" class="hidden px-6 py-5 bg-slate-950/80 border-t border-slate-800/80 space-y-4">
                                        <!-- Key Details Cards -->
                                        <div class="grid grid-cols-2 sm:grid-cols-5 gap-3">
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

                                            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-800 col-span-2 sm:col-span-1">
                                                <span class="block text-[10px] font-semibold text-slate-400 uppercase tracking-wider">Assigned By</span>
                                                <span class="text-xs font-bold text-slate-200 mt-1 block">
                                                    {{ $exam->creator?->name ?? 'System' }}
                                                </span>
                                            </div>
                                        </div>

                                        <!-- Actions Control Footer -->
                                        <div class="pt-3 border-t border-slate-800/80 flex items-center justify-between flex-wrap gap-3">
                                            <div class="text-xs text-slate-400">
                                                Exam Options & Actions
                                            </div>

                                            <div class="flex items-center space-x-2">
                                                @if($isSubmitted)
                                                    <span class="inline-flex items-center px-2.5 py-1 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/40">
                                                        <svg class="w-3.5 h-3.5 mr-1 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                                                        Submitted
                                                    </span>

                                                    <button onclick="openStudentViewSubmissionModal({{ json_encode([
                                                        'id' => $exam->id,
                                                        'name' => $exam->name,
                                                        'total_mark' => $totalExamMarks,
                                                        'obtained_mark' => $obtainedMarks,
                                                        'details' => $detailsPayload,
                                                    ]) }})" class="px-4 py-2 rounded-xl bg-indigo-900 hover:bg-indigo-800 text-white text-xs font-bold border border-indigo-800/50 transition-colors inline-flex items-center space-x-1.5 cursor-pointer shadow-md">
                                                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                                                        <span>View Submission Details</span>
                                                    </button>

                                                    <button type="button" onclick="openExamLeaderboardModal({{ $exam->id }}, '{{ addslashes($exam->name) }}')" class="px-4 py-2 rounded-xl bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 border border-amber-500/40 text-xs font-bold transition-all inline-flex items-center space-x-1.5 cursor-pointer shadow-md">
                                                        <span>🏆 Leaderboard</span>
                                                    </button>
                                                @elseif($exam->status == 1)
                                                    <button onclick="openStartExamModal({{ json_encode([
                                                        'id' => $exam->id,
                                                        'name' => $exam->name,
                                                        'type' => $exam->type == 1 ? '1 - Timed' : ($exam->type == 2 ? '2 - Non-Timed' : '3 - Text Entry'),
                                                        'type_id' => $exam->type,
                                                        'duration' => $exam->duration,
                                                        'total_mark' => $exam->total_mark,
                                                        'submit_url' => route('student.exams.submit', $exam),
                                                        'questions' => $exam->questions->map(function($q) {
                                                            return [
                                                                'id' => $q->id,
                                                                'name' => $q->name,
                                                                'description' => $q->description,
                                                                'hint' => $q->hint,
                                                                'solution' => $q->solution,
                                                                'marks' => $q->marks,
                                                                'type' => $q->type,
                                                                'answers' => $q->answers->map(function($a) {
                                                                    return [
                                                                        'id' => $a->id,
                                                                        'name' => $a->name,
                                                                        'match_answer' => $a->match_answer,
                                                                    ];
                                                                })->toArray(),
                                                            ];
                                                        })->toArray(),
                                                    ]) }})" class="px-5 py-2 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white text-xs font-extrabold shadow-lg shadow-emerald-600/30 transition-all inline-flex items-center space-x-1.5 cursor-pointer">
                                                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                                                        <span>Start Exam</span>
                                                    </button>

                                                    <button onclick="openStudentViewExamModal({{ json_encode([
                                                        'id' => $exam->id,
                                                        'name' => $exam->name,
                                                        'type' => $exam->type == 1 ? '1 - Timed' : ($exam->type == 2 ? '2 - Non-Timed' : '3 - Text Entry'),
                                                        'status' => $exam->status == 1 ? '1 - Active' : '2 - Inactive',
                                                        'creator' => $exam->creator?->name ?? 'System',
                                                        'total_mark' => $exam->total_mark,
                                                        'standard' => $user->student?->standard?->name ?? 'N/A',
                                                        'questions' => $exam->questions->map(function($q) {
                                                            return [
                                                                'name' => $q->name,
                                                                'description' => $q->description,
                                                                'hint' => $q->hint,
                                                                'solution' => $q->solution,
                                                                'marks' => $q->marks,
                                                                'type' => $q->type == 1 ? 'Single Option' : ($q->type == 2 ? 'Multiple Option' : ($q->type == 4 ? 'True / False' : ($q->type == 5 ? 'Match the Following' : 'Text Entry'))),
                                                                'answers' => $q->type == 5
                                                                    ? $q->answers->map(fn($a) => $a->name . ' ⟷ ' . $a->match_answer)->toArray()
                                                                    : $q->answers->pluck('name')->toArray(),
                                                            ];
                                                        })->toArray(),
                                                    ]) }})" class="px-4 py-2 rounded-xl bg-sky-950 hover:bg-sky-900 text-sky-300 text-xs font-semibold border border-sky-800/40 transition-colors inline-flex items-center space-x-1.5 cursor-pointer">
                                                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                                                        <span>Preview</span>
                                                    </button>
                                                @else
                                                    <span class="text-xs text-slate-500 italic">Exam Inactive</span>
                                                @endif
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            @endforeach
                        </div>

                        @if(method_exists($studentExams, 'total'))
                            <div class="px-6 py-4 border-t border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs text-slate-400 bg-slate-950/40">
                                <div>
                                    Showing <span class="font-semibold text-slate-200">{{ $studentExams->firstItem() ?? 0 }}</span>
                                    to <span class="font-semibold text-slate-200">{{ $studentExams->lastItem() ?? 0 }}</span>
                                    of <span class="font-semibold text-slate-200">{{ $studentExams->total() }}</span> exam(s)
                                    (10 per page)
                                </div>
                                @if($studentExams->hasPages())
                                    <div>
                                        {{ $studentExams->links() }}
                                    </div>
                                @endif
                            </div>
                        @endif
                    @else
                        <div class="p-12 text-center shadow-lg">
                            <div class="w-16 h-16 rounded-2xl bg-slate-800 border border-slate-700 text-slate-500 flex items-center justify-center mx-auto mb-4">
                                <svg class="w-8 h-8 text-sky-400/80" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
                                </svg>
                            </div>
                            @if($user->student?->standard)
                                <h3 class="text-base font-semibold text-slate-300">No Exams Assigned Yet</h3>
                                <p class="mt-1 text-sm text-slate-500 max-w-sm mx-auto">There are currently no exams assigned to your class (<strong class="text-sky-300">{{ $user->student->standard->name }}</strong>). Check back later!</p>
                            @else
                                <h3 class="text-base font-semibold text-slate-300">No Class / Standard Assigned</h3>
                                <p class="mt-1 text-sm text-slate-500 max-w-sm mx-auto">Your student profile has not been assigned to a class standard yet. Please contact your school admin.</p>
                            @endif
                        </div>
                    @endif
                </div>
            </div>

            <!-- START EXAM WIZARD MODAL FOR STUDENTS -->
            <div id="takeExamModal" class="hidden fixed inset-0 z-50 bg-black/80 backdrop-blur-md flex items-center justify-center p-4 overflow-y-auto">
                <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-6xl overflow-hidden shadow-2xl my-8">
                    
                    <!-- Modal Header -->
                    <div class="px-6 py-4 border-b border-slate-800 flex items-center justify-between bg-slate-950/60">
                        <div class="flex items-center space-x-3">
                            <div class="w-9 h-9 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 font-bold flex items-center justify-center text-sm">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
                            </div>
                            <div>
                                <h3 id="take_exam_title" class="text-base font-extrabold text-white"></h3>
                                <p id="take_exam_subtitle" class="text-xs text-slate-400">Step-by-step examination session</p>
                            </div>
                        </div>
                        <button type="button" onclick="confirmCancelExam()" class="text-slate-400 hover:text-white transition-colors cursor-pointer p-1">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                        </button>
                    </div>

                    <!-- Progress Indicator & Timer Bar -->
                    <div class="bg-slate-950 px-6 py-3 border-b border-slate-800 flex items-center justify-between flex-wrap gap-3">
                        <div class="flex items-center space-x-2 flex-wrap gap-2">
                            <span id="take_exam_step_badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
                                Question 1 of 1
                            </span>
                            <span id="take_exam_marks_badge" class="text-xs text-amber-400 font-bold bg-amber-500/10 px-2.5 py-0.5 rounded-full border border-amber-500/20">
                                0 Marks
                            </span>
                        </div>

                        <!-- Live Countdown Clock Timer (Runs in seconds) -->
                        <div id="take_exam_timer_wrapper" class="hidden flex items-center space-x-2 bg-rose-950/80 border border-rose-500/40 px-3.5 py-1 rounded-full text-rose-300 shadow-md">
                            <svg class="w-4 h-4 text-rose-400 animate-pulse shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                            </svg>
                            <span class="text-[11px] font-bold text-slate-300 uppercase tracking-wider">Time Left:</span>
                            <span id="take_exam_clock_text" class="font-mono text-sm font-black text-rose-400 tracking-wider">00:00:00</span>
                        </div>

                        <div class="w-48 bg-slate-800 rounded-full h-2.5 overflow-hidden border border-slate-700">
                            <div id="take_exam_progress_bar" class="bg-gradient-to-r from-indigo-500 to-emerald-400 h-2.5 rounded-full transition-all duration-300" style="width: 0%"></div>
                        </div>
                    </div>

                    <!-- Time Expiration Lock Banner -->
                    <div id="take_exam_time_lock_banner" class="hidden px-6 py-3 bg-red-950/90 border-b border-red-500/50 text-red-200 text-xs font-semibold flex items-center justify-between">
                        <div class="flex items-center space-x-2">
                            <svg class="w-5 h-5 text-red-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
                            <span>⏰ <strong>Time's Up!</strong> Exam duration completed. Inputs are locked and answers are being automatically saved to database...</span>
                        </div>
                    </div>

                    <!-- Voice Assistant Control & Feedback Bar -->
                    <div class="px-6 py-2.5 bg-slate-950/90 border-b border-slate-800/80 flex flex-wrap items-center justify-between gap-3 text-xs">
                        <div class="flex items-center space-x-2">
                            <button type="button" id="speechToggleBtn" onclick="toggleSpeechRecognition()" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-semibold border border-slate-700 transition-all cursor-pointer inline-flex items-center space-x-2">
                                <svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z"/></svg>
                                <span id="speech_mic_icon" class="w-2.5 h-2.5 rounded-full bg-slate-500 inline-block"></span>
                                <span id="speech_toggle_text">Voice Control: OFF</span>
                            </button>
                            <span id="speech_status_badge" class="hidden px-2.5 py-1 rounded-lg bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 text-[11px] font-medium flex items-center space-x-1.5">
                                <span class="animate-ping w-2 h-2 rounded-full bg-emerald-400"></span>
                                <span id="speech_status_text">Listening...</span>
                            </span>
                        </div>
                        <div class="flex items-center space-x-2">
                            <span class="text-[11px] text-slate-400 font-medium">Say: <span class="text-indigo-300 font-mono">"Option A"</span>, <span class="text-indigo-300 font-mono">"Option B"</span>, <span class="text-indigo-300 font-mono">"Next"</span></span>
                            <div id="speech_feedback_box" class="hidden px-3 py-1 rounded-lg bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 text-xs font-bold animate-pulse"></div>
                        </div>
                    </div>

                    <!-- Form wrapping the entire exam session -->
                    <form id="takeExamForm" method="POST" action="" onsubmit="stopExamTimer(); updateAllFormAnswers();" class="p-6 space-y-6">
                        @csrf

                        <!-- Question Step Display -->
                        <div id="questionStepContainer" class="space-y-4">
                            <!-- Dynamically rendered via JS -->
                        </div>

                        <!-- Footer Action Controls -->
                        <div class="pt-4 border-t border-slate-800 flex items-center justify-between">
                            <button type="button" id="prevQuestionBtn" onclick="navigateExamStep(-1)" class="px-5 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition-colors flex items-center space-x-1.5 cursor-pointer disabled:opacity-40 disabled:cursor-not-allowed">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
                                <span>Previous Question</span>
                            </button>

                            <!-- Next Button (Navigates client-side, NO database saving) -->
                            <button type="button" id="nextQuestionBtn" onclick="navigateExamStep(1)" class="px-6 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold shadow-lg shadow-indigo-600/30 transition-all flex items-center space-x-1.5 cursor-pointer">
                                <span>Next Question</span>
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                            </button>

                            <!-- Final Submit Exam Button (ONLY SHOWN ON LAST QUESTION) -->
                            <button type="submit" id="submitExamBtn" class="hidden px-6 py-2.5 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white text-xs font-extrabold shadow-lg shadow-emerald-600/40 transition-all flex items-center space-x-2 cursor-pointer">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                                <span>Submit Exam</span>
                            </button>
                        </div>
                    </form>
                </div>
            </div>

            <!-- STUDENT VIEW SUBMISSION DETAILS MODAL -->
            <div id="studentViewSubmissionModal" class="hidden fixed inset-0 z-50 bg-slate-900/70 backdrop-blur-sm flex items-center justify-center p-4">
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
                    <div class="px-5 py-3.5 bg-white border-t border-slate-200 flex items-center justify-end" style="flex-shrink:0;">
                        <button type="button" onclick="document.getElementById('studentViewSubmissionModal').classList.add('hidden')" class="px-5 py-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-white text-xs font-bold shadow-md transition-all cursor-pointer">
                            Close
                        </button>
                    </div>
                </div>
            </div>

            <!-- STUDENT VIEW EXAM PREVIEW MODAL -->
            <div id="studentViewExamModal" class="hidden fixed inset-0 z-50 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4 overflow-y-auto">
                <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-6xl overflow-hidden shadow-2xl my-8">
                    <div class="px-6 py-4 border-b border-slate-800 flex items-center justify-between bg-slate-950/50">
                        <h3 class="text-lg font-bold text-white flex items-center gap-2">
                            <svg class="w-5 h-5 text-sky-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                            <span>Exam Overview</span>
                        </h3>
                        <button onclick="document.getElementById('studentViewExamModal').classList.add('hidden')" class="text-slate-400 hover:text-white transition-colors cursor-pointer">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                        </button>
                    </div>

                    <div class="p-6 space-y-5">
                        <div>
                            <h4 id="student_view_exam_name" class="text-xl font-extrabold text-white"></h4>
                            <p class="text-xs text-slate-400 mt-1">Class Exam Overview & Questions</p>
                        </div>

                        <!-- Key Metadata Cards -->
                        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
                            <div class="p-3 bg-slate-950 rounded-xl border border-slate-800">
                                <span class="block text-[10px] font-semibold text-slate-400 uppercase">Type</span>
                                <span id="student_view_exam_type" class="text-xs font-bold text-indigo-300 mt-0.5 block"></span>
                            </div>
                            <div class="p-3 bg-slate-950 rounded-xl border border-slate-800">
                                <span class="block text-[10px] font-semibold text-slate-400 uppercase">Status</span>
                                <span id="student_view_exam_status" class="text-xs font-bold text-emerald-400 mt-0.5 block"></span>
                            </div>
                            <div class="p-3 bg-slate-950 rounded-xl border border-slate-800">
                                <span class="block text-[10px] font-semibold text-slate-400 uppercase">Total Marks</span>
                                <span id="student_view_exam_total_mark" class="text-xs font-bold text-amber-400 mt-0.5 block"></span>
                            </div>
                            <div class="p-3 bg-slate-950 rounded-xl border border-slate-800">
                                <span class="block text-[10px] font-semibold text-slate-400 uppercase">Created By</span>
                                <span id="student_view_exam_creator" class="text-xs font-bold text-slate-200 mt-0.5 block"></span>
                            </div>
                        </div>

                        <!-- Questions List -->
                        <div>
                            <div class="flex items-center justify-between mb-2">
                                <h5 class="text-xs font-bold text-slate-300 uppercase tracking-wider">Exam Questions</h5>
                                <span id="student_view_exam_q_count" class="text-[11px] text-sky-300 font-semibold"></span>
                            </div>

                            <div id="student_view_exam_questions_list" class="bg-slate-950 p-3 rounded-xl border border-slate-800 max-h-[400px] overflow-y-auto space-y-3" style="max-height: 400px; overflow-y: auto;">
                                <!-- Populated dynamically via JS -->
                            </div>
                        </div>

                        <div class="pt-4 flex justify-end items-center border-t border-slate-800">
                            <button type="button" onclick="document.getElementById('studentViewExamModal').classList.add('hidden')" class="px-5 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-medium transition-colors cursor-pointer">Close</button>
                        </div>
                    </div>
                </div>
            </div>

            <script>
                function toggleStudentExamDetails(examId) {
                    const detailsBox = document.getElementById('details-exam-' + examId);
                    const chevron = document.getElementById('chevron-exam-' + examId);
                    if (detailsBox) {
                        detailsBox.classList.toggle('hidden');
                    }
                    if (chevron) {
                        chevron.classList.toggle('rotate-180');
                    }
                }

                let currentExamData = null;
                let currentExamStep = 0;
                let userSelectedAnswers = {};
                let userSelectedMatches = {};
                let userSelectedTextAnswers = {};
                let examTimerInterval = null;
                let examTimeRemainingSeconds = 0;
                let isExamTimerLocked = false;

                const studentPaletteSymbols = {
                    chem: [
                        { label: '→', val: '→', title: 'Forward Reaction Arrow' },
                        { label: '⇌', val: '⇌', title: 'Reversible Reaction / Equilibrium' },
                        { label: '↑', val: '↑', title: 'Gas Evolution' },
                        { label: '↓', val: '↓', title: 'Precipitate Formation' },
                        { label: 'Δ', val: 'Δ', title: 'Heat / Change' },
                        { label: '°C', val: '°C', title: 'Degrees Celsius' },
                        { label: '(s)', val: '(s)', title: 'Solid State' },
                        { label: '(l)', val: '(l)', title: 'Liquid State' },
                        { label: '(g)', val: '(g)', title: 'Gaseous State' },
                        { label: '(aq)', val: '(aq)', title: 'Aqueous Solution' },
                        { label: 'H₂O', val: 'H₂O', title: 'Water' },
                        { label: 'CO₂', val: 'CO₂', title: 'Carbon Dioxide' },
                        { label: 'O₂', val: 'O₂', title: 'Oxygen Gas' },
                        { label: 'H₂', val: 'H₂', title: 'Hydrogen Gas' },
                        { label: 'N₂', val: 'N₂', title: 'Nitrogen Gas' },
                        { label: 'HCl', val: 'HCl', title: 'Hydrochloric Acid' },
                        { label: 'H₂SO₄', val: 'H₂SO₄', title: 'Sulfuric Acid' },
                        { label: 'HNO₃', val: 'HNO₃', title: 'Nitric Acid' },
                        { label: 'NaOH', val: 'NaOH', title: 'Sodium Hydroxide' },
                        { label: 'NaCl', val: 'NaCl', title: 'Sodium Chloride' },
                        { label: 'CaCO₃', val: 'CaCO₃', title: 'Calcium Carbonate' },
                        { label: 'H⁺', val: 'H⁺', title: 'Hydrogen Ion' },
                        { label: 'OH⁻', val: 'OH⁻', title: 'Hydroxide Ion' },
                        { label: 'SO₄²⁻', val: 'SO₄²⁻', title: 'Sulfate Ion' },
                        { label: 'NO₃⁻', val: 'NO₃⁻', title: 'Nitrate Ion' },
                        { label: 'CO₃²⁻', val: 'CO₃²⁻', title: 'Carbonate Ion' },
                        { label: 'NH₄⁺', val: 'NH₄⁺', title: 'Ammonium Ion' },
                        { label: 'Na⁺', val: 'Na⁺', title: 'Sodium Ion' },
                        { label: 'Cl⁻', val: 'Cl⁻', title: 'Chloride Ion' },
                        { label: 'Ca²⁺', val: 'Ca²⁺', title: 'Calcium Ion' },
                        { label: 'Mg²⁺', val: 'Mg²⁺', title: 'Magnesium Ion' },
                        { label: 'Fe²⁺', val: 'Fe²⁺', title: 'Ferrous Ion' },
                        { label: 'Fe³⁺', val: 'Fe³⁺', title: 'Ferric Ion' },
                        { label: 'Cu²⁺', val: 'Cu²⁺', title: 'Cupric Ion' },
                        { label: 'Zn²⁺', val: 'Zn²⁺', title: 'Zinc Ion' },
                        { label: 'Ag⁺', val: 'Ag⁺', title: 'Silver Ion' }
                    ],
                    math: [
                        { label: '±', val: '±', title: 'Plus-Minus' },
                        { label: '∓', val: '∓', title: 'Minus-Plus' },
                        { label: '×', val: '×', title: 'Multiply' },
                        { label: '÷', val: '÷', title: 'Divide' },
                        { label: '≠', val: '≠', title: 'Not Equal' },
                        { label: '≈', val: '≈', title: 'Approximately Equal' },
                        { label: '≤', val: '≤', title: 'Less Than or Equal' },
                        { label: '≥', val: '≥', title: 'Greater Than or Equal' },
                        { label: '√', val: '√', title: 'Square Root' },
                        { label: '∛', val: '∛', title: 'Cube Root' },
                        { label: 'π', val: 'π', title: 'Pi' },
                        { label: '∞', val: '∞', title: 'Infinity' },
                        { label: '°', val: '°', title: 'Degree' },
                        { label: '∠', val: '∠', title: 'Angle' },
                        { label: '△', val: '△', title: 'Triangle' },
                        { label: '⊥', val: '⊥', title: 'Perpendicular' },
                        { label: '∥', val: '∥', title: 'Parallel' },
                        { label: '∵', val: '∵', title: 'Because' },
                        { label: '∴', val: '∴', title: 'Therefore' },
                        { label: '∈', val: '∈', title: 'Element Of' },
                        { label: '∉', val: '∉', title: 'Not Element Of' },
                        { label: '⊂', val: '⊂', title: 'Subset Of' },
                        { label: '∪', val: '∪', title: 'Union' },
                        { label: '∩', val: '∩', title: 'Intersection' },
                        { label: '½', val: '½', title: 'One Half' },
                        { label: '⅓', val: '⅓', title: 'One Third' },
                        { label: '¼', val: '¼', title: 'One Quarter' },
                        { label: '¾', val: '¾', title: 'Three Quarters' },
                        { label: '∑', val: '∑', title: 'Summation' },
                        { label: '∫', val: '∫', title: 'Integral' }
                    ],
                    scripts: [
                        { label: 'x²', val: '²', title: 'Superscript 2 (Squared)' },
                        { label: 'x³', val: '³', title: 'Superscript 3 (Cubed)' },
                        { label: 'x⁴', val: '⁴', title: 'Superscript 4' },
                        { label: 'xⁿ', val: 'ⁿ', title: 'Superscript n' },
                        { label: '⁺', val: '⁺', title: 'Superscript +' },
                        { label: '⁻', val: '⁻', title: 'Superscript -' },
                        { label: 'x₀', val: '₀', title: 'Subscript 0' },
                        { label: 'x₁', val: '₁', title: 'Subscript 1' },
                        { label: 'x₂', val: '₂', title: 'Subscript 2' },
                        { label: 'x₃', val: '₃', title: 'Subscript 3' },
                        { label: 'x₄', val: '₄', title: 'Subscript 4' },
                        { label: 'x₅', val: '₅', title: 'Subscript 5' },
                        { label: 'x₆', val: '₆', title: 'Subscript 6' },
                        { label: 'xₙ', val: 'ₙ', title: 'Subscript n' }
                    ],
                    greek: [
                        { label: 'α', val: 'α', title: 'Alpha' },
                        { label: 'β', val: 'β', title: 'Beta' },
                        { label: 'γ', val: 'γ', title: 'Gamma' },
                        { label: 'δ', val: 'δ', title: 'Delta (lower)' },
                        { label: 'Δ', val: 'Δ', title: 'Delta (capital)' },
                        { label: 'θ', val: 'θ', title: 'Theta' },
                        { label: 'λ', val: 'λ', title: 'Lambda' },
                        { label: 'μ', val: 'μ', title: 'Mu (micro)' },
                        { label: 'π', val: 'π', title: 'Pi' },
                        { label: 'ρ', val: 'ρ', title: 'Rho' },
                        { label: 'σ', val: 'σ', title: 'Sigma' },
                        { label: 'Σ', val: 'Σ', title: 'Sigma (capital)' },
                        { label: 'ω', val: 'ω', title: 'Omega' },
                        { label: 'Ω', val: 'Ω', title: 'Omega (capital/Ohms)' }
                    ]
                };

                function insertStudentSymbol(qId, val) {
                    if (isExamTimerLocked) return;
                    const textarea = document.getElementById('student_text_ans_' + qId);
                    if (!textarea) return;

                    const start = textarea.selectionStart ?? textarea.value.length;
                    const end = textarea.selectionEnd ?? textarea.value.length;
                    const oldVal = textarea.value;

                    textarea.value = oldVal.substring(0, start) + val + oldVal.substring(end);
                    const newPos = start + val.length;
                    textarea.selectionStart = textarea.selectionEnd = newPos;
                    textarea.focus();

                    recordTextAnswer(qId, textarea.value);
                }

                function switchStudentSymbolTab(qId, cat) {
                    ['chem', 'math', 'scripts', 'greek'].forEach(c => {
                        const tab = document.getElementById(`tab_${c}_${qId}`);
                        if (tab) {
                            if (c === cat) {
                                tab.className = 'px-2.5 py-1 rounded-lg text-[11px] font-bold bg-indigo-600 text-white transition-colors cursor-pointer';
                            } else {
                                tab.className = 'px-2.5 py-1 rounded-lg text-[11px] font-bold bg-slate-800 hover:bg-slate-700 text-slate-300 transition-colors cursor-pointer';
                            }
                        }
                    });
                    renderStudentSymbols(qId, cat);
                }

                function renderStudentSymbols(qId, cat) {
                    const container = document.getElementById('palette_container_' + qId);
                    if (!container) return;

                    const symbols = studentPaletteSymbols[cat] || studentPaletteSymbols.chem;
                    let html = '<div class="flex flex-wrap gap-1.5 p-1">';
                    symbols.forEach(s => {
                        html += `
                            <button
                                type="button"
                                onclick="insertStudentSymbol(${qId}, '${escapeExamHtml(s.val)}')"
                                title="${escapeExamHtml(s.title)}"
                                class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-indigo-600 hover:text-white border border-slate-700/80 hover:border-indigo-500 text-slate-200 font-mono text-xs font-semibold shadow-sm transition-all cursor-pointer active:scale-95">
                                ${escapeExamHtml(s.label)}
                            </button>
                        `;
                    });
                    html += '</div>';
                    container.innerHTML = html;
                }

                function recordTextAnswer(qId, val) {
                    if (isExamTimerLocked) return;
                    userSelectedTextAnswers[qId] = val;
                    const cntElem = document.getElementById('text_char_count_' + qId);
                    if (cntElem) cntElem.textContent = (val ? val.length : 0) + ' character(s)';
                    updateAllFormAnswers();
                }

                function escapeExamHtml(str) {
                    if (str === null || str === undefined) return '';
                    return String(str)
                        .replace(/&/g, '&amp;')
                        .replace(/</g, '&lt;')
                        .replace(/>/g, '&gt;')
                        .replace(/"/g, '&quot;')
                        .replace(/'/g, '&#039;');
                }

                function openStartExamModal(data) {
                    currentExamData = data;
                    currentExamStep = 0;
                    userSelectedAnswers = {};
                    userSelectedMatches = {};
                    userSelectedTextAnswers = {};
                    isExamTimerLocked = false;

                    const lockBanner = document.getElementById('take_exam_time_lock_banner');
                    if (lockBanner) lockBanner.classList.add('hidden');

                    document.getElementById('take_exam_title').textContent = data.name || 'Exam Session';
                    document.getElementById('take_exam_subtitle').textContent = `Total Marks: ${data.total_mark} | Questions: ${data.questions ? data.questions.length : 0}`;
                    document.getElementById('takeExamForm').action = data.submit_url || '';

                    stopExamTimer();

                    const isTimed = (data.type_id == 1 || parseInt(data.type) === 1 || (typeof data.type === 'string' && data.type.includes('Timed')));
                    const durationMins = parseInt(data.duration);

                    const timerWrapper = document.getElementById('take_exam_timer_wrapper');
                    const clockText = document.getElementById('take_exam_clock_text');

                    if (isTimed && durationMins > 0) {
                        examTimeRemainingSeconds = durationMins * 60;
                        if (clockText) clockText.textContent = formatExamTime(examTimeRemainingSeconds);
                        if (timerWrapper) timerWrapper.classList.remove('hidden');

                        startExamTimer();
                    } else {
                        if (timerWrapper) timerWrapper.classList.add('hidden');
                    }

                    renderExamStep();
                    document.getElementById('takeExamModal').classList.remove('hidden');
                }

                function startExamTimer() {
                    stopExamTimer();
                    examTimerInterval = setInterval(() => {
                        examTimeRemainingSeconds--;
                        const clockText = document.getElementById('take_exam_clock_text');

                        if (examTimeRemainingSeconds > 0) {
                            if (clockText) clockText.textContent = formatExamTime(examTimeRemainingSeconds);
                        } else {
                            if (clockText) clockText.textContent = "00:00 (Time's Up!)";
                            stopExamTimer();
                            lockAndAutoSubmitExam();
                        }
                    }, 1000);
                }

                function stopExamTimer() {
                    if (examTimerInterval) {
                        clearInterval(examTimerInterval);
                        examTimerInterval = null;
                    }
                }

                function formatExamTime(totalSeconds) {
                    if (totalSeconds < 0) totalSeconds = 0;
                    const hours = Math.floor(totalSeconds / 3600);
                    const minutes = Math.floor((totalSeconds % 3600) / 60);
                    const seconds = totalSeconds % 60;

                    const pad = (n) => String(n).padStart(2, '0');

                    if (hours > 0) {
                        return `${pad(hours)}:${pad(minutes)}:${pad(seconds)}`;
                    } else {
                        return `${pad(minutes)}:${pad(seconds)}`;
                    }
                }

                function lockAndAutoSubmitExam() {
                    isExamTimerLocked = true;

                    const lockBanner = document.getElementById('take_exam_time_lock_banner');
                    if (lockBanner) lockBanner.classList.remove('hidden');

                    renderExamStep();

                    const prevBtn = document.getElementById('prevQuestionBtn');
                    const nextBtn = document.getElementById('nextQuestionBtn');
                    const submitBtn = document.getElementById('submitExamBtn');
                    if (prevBtn) prevBtn.disabled = true;
                    if (nextBtn) nextBtn.disabled = true;
                    if (submitBtn) {
                        submitBtn.disabled = true;
                        submitBtn.classList.remove('hidden');
                        submitBtn.innerHTML = `
                            <svg class="w-4 h-4 animate-spin text-white inline" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                            <span>Time Expired - Saving Results...</span>
                        `;
                    }

                    stopSpeechRecognition();
                    updateAllFormAnswers();

                    setTimeout(() => {
                        const form = document.getElementById('takeExamForm');
                        if (form) form.submit();
                    }, 1200);
                }

                function renderExamStep() {
                    if (!currentExamData || !currentExamData.questions || currentExamData.questions.length === 0) {
                        document.getElementById('questionStepContainer').innerHTML = `
                            <div class="p-8 text-center text-slate-500">
                                This exam does not have any questions available yet.
                            </div>
                        `;
                        document.getElementById('prevQuestionBtn').classList.add('hidden');
                        document.getElementById('nextQuestionBtn').classList.add('hidden');
                        document.getElementById('submitExamBtn').classList.add('hidden');
                        return;
                    }

                    const totalQuestions = currentExamData.questions.length;
                    const q = currentExamData.questions[currentExamStep];

                    // Update Badges & Progress Bar
                    document.getElementById('take_exam_step_badge').textContent = `Question ${currentExamStep + 1} of ${totalQuestions}`;
                    document.getElementById('take_exam_marks_badge').textContent = `${q.marks} Mark(s)`;

                    const progressPct = Math.round(((currentExamStep + 1) / totalQuestions) * 100);
                    document.getElementById('take_exam_progress_bar').style.width = progressPct + '%';

                    // Build Options
                    let optionsHtml = '';
                    const selectedAnsId = userSelectedAnswers[q.id] || null;
                    const isTrueFalse = parseInt(q.type) === 4;
                    const isMatch = parseInt(q.type) === 5;
                    const isTextEntry = parseInt(q.type) === 3;

                    if (isTextEntry) {
                        const currentTextAns = userSelectedTextAnswers[q.id] || '';
                        const disabledAttr = isExamTimerLocked ? 'disabled' : '';
                        optionsHtml = `
                            <div class="mt-4 space-y-3">
                                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-1.5">
                                    <label for="student_text_ans_${q.id}" class="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center space-x-1.5">
                                        <svg class="w-4 h-4 text-amber-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/></svg>
                                        <span>Your Answer (Type here or use Math/Chemistry symbol palette):</span>
                                    </label>
                                    <span class="text-[10px] font-semibold text-slate-400 bg-slate-900 px-2 py-0.5 rounded-full border border-slate-800 w-fit">No Autocorrection • Manual Evaluation</span>
                                </div>
                                <div class="relative">
                                    <textarea
                                        id="student_text_ans_${q.id}"
                                        rows="6"
                                        ${disabledAttr}
                                        oninput="recordTextAnswer(${q.id}, this.value)"
                                        placeholder="Write your complete step-by-step solution, equations, formula, chemical reaction, or explanation here..."
                                        class="w-full px-4 py-3 rounded-xl bg-slate-900 border border-slate-700 text-slate-100 placeholder-slate-500 font-sans text-sm focus:ring-2 focus:ring-amber-500 focus:border-amber-500 focus:outline-none transition-all leading-relaxed">${escapeExamHtml(currentTextAns)}</textarea>
                                </div>
                                
                                <!-- Math & Chemistry Symbol Palette -->
                                <div class="p-3 rounded-xl bg-slate-900/90 border border-slate-800 space-y-2">
                                    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
                                        <span class="text-xs font-bold text-slate-300 flex items-center gap-1.5">
                                            <span>⌨️ Math & Chemistry Symbol Palette</span>
                                            <span class="text-[10px] text-slate-500 font-normal hidden sm:inline">(Click any symbol to insert)</span>
                                        </span>
                                        <div class="flex items-center space-x-1 bg-slate-950 p-1 rounded-lg border border-slate-800">
                                            <button type="button" onclick="switchStudentSymbolTab(${q.id}, 'chem')" id="tab_btn_${q.id}_chem" class="px-2.5 py-1 rounded-md text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 transition-all">Chemistry</button>
                                            <button type="button" onclick="switchStudentSymbolTab(${q.id}, 'math')" id="tab_btn_${q.id}_math" class="px-2.5 py-1 rounded-md text-[11px] font-semibold text-slate-400 hover:text-white transition-all">Math</button>
                                            <button type="button" onclick="switchStudentSymbolTab(${q.id}, 'scripts')" id="tab_btn_${q.id}_scripts" class="px-2.5 py-1 rounded-md text-[11px] font-semibold text-slate-400 hover:text-white transition-all">Sub/Super</button>
                                            <button type="button" onclick="switchStudentSymbolTab(${q.id}, 'greek')" id="tab_btn_${q.id}_greek" class="px-2.5 py-1 rounded-md text-[11px] font-semibold text-slate-400 hover:text-white transition-all">Greek</button>
                                        </div>
                                    </div>
                                    <div id="palette_container_${q.id}" class="flex flex-wrap gap-1.5 max-h-36 overflow-y-auto p-1 custom-scrollbar">
                                        <!-- Populated via renderStudentSymbols -->
                                    </div>
                                </div>
                            </div>
                        `;
                    } else if (isMatch) {
                        if (q.answers && q.answers.length > 0) {
                            if (!q._shuffledMatches) {
                                const rightOptions = [...new Set(q.answers.map(a => a.match_answer).filter(Boolean))];
                                q._shuffledMatches = rightOptions.sort(() => 0.5 - Math.random());
                            }

                            const currentQMatches = userSelectedMatches[q.id] || {};
                            let matchedCount = 0;
                            q.answers.forEach(a => {
                                if (currentQMatches[a.id]) matchedCount++;
                            });

                            optionsHtml = `
                                <div class="mt-4 space-y-3">
                                    <div class="flex items-center justify-between text-xs text-slate-400 font-semibold px-1">
                                        <span>Premise / Question Item</span>
                                        <span class="text-indigo-400 font-mono">${matchedCount}/${q.answers.length} Paired</span>
                                    </div>
                                    <div class="space-y-2.5">
                            `;

                            q.answers.forEach((opt, idx) => {
                                const optionLetter = String.fromCharCode(65 + idx);
                                const chosenMatch = currentQMatches[opt.id] || '';
                                const isPaired = Boolean(chosenMatch);
                                const disabledAttr = isExamTimerLocked ? 'disabled' : '';

                                optionsHtml += `
                                    <div class="p-3.5 sm:p-4 rounded-xl border ${isPaired ? 'bg-slate-900/90 border-indigo-500/50 shadow-md ring-1 ring-indigo-500/30' : 'bg-slate-950/80 border-slate-800'} flex flex-col sm:flex-row sm:items-center justify-between gap-3 transition-all">
                                        <div class="flex items-center space-x-3 min-w-0">
                                            <span class="w-8 h-8 rounded-xl ${isPaired ? 'bg-indigo-600 text-white font-extrabold' : 'bg-slate-800 text-slate-300 border border-slate-700 font-bold'} flex items-center justify-center text-sm shrink-0 shadow-sm">
                                                ${optionLetter}
                                            </span>
                                            <div class="min-w-0">
                                                <span class="text-xs text-slate-500 font-mono font-medium block">Item ${optionLetter}</span>
                                                <span class="text-sm font-semibold text-slate-100 break-words">${escapeExamHtml(opt.name)}</span>
                                            </div>
                                        </div>
                                        <div class="flex items-center space-x-2 w-full sm:w-auto shrink-0">
                                            <span class="text-xs text-slate-500 font-bold hidden sm:inline">⟷</span>
                                            <select
                                                onchange="recordMatchChoice(${q.id}, ${opt.id}, this.value)"
                                                ${disabledAttr}
                                                class="w-full sm:w-64 px-3 py-2 rounded-xl text-xs font-semibold bg-slate-900 border ${isPaired ? 'border-emerald-500/80 text-emerald-300 ring-1 ring-emerald-500/40' : 'border-slate-700 text-slate-300'} focus:ring-2 focus:ring-emerald-500 focus:outline-none transition-all cursor-pointer">
                                                <option value="">-- Choose matching answer --</option>
                                                ${q._shuffledMatches.map(m => `
                                                    <option value="${escapeExamHtml(m)}" ${chosenMatch === m ? 'selected' : ''}>${escapeExamHtml(m)}</option>
                                                `).join('')}
                                            </select>
                                        </div>
                                    </div>
                                `;
                            });

                            optionsHtml += `
                                    </div>
                                </div>
                            `;
                        } else {
                            optionsHtml = '<p class="text-xs text-slate-500 italic mt-3">No matching pairs defined for this question.</p>';
                        }
                    } else if (q.answers && q.answers.length > 0) {
                        optionsHtml = `<div class="${isTrueFalse ? 'grid grid-cols-1 sm:grid-cols-2 gap-3' : 'space-y-2.5'} mt-4">`;
                        q.answers.forEach((opt, idx) => {
                            const optionLetter = String.fromCharCode(65 + idx);
                            const isChecked = selectedAnsId == opt.id ? 'checked' : '';
                            const isSelected = selectedAnsId == opt.id;
                            const disabledAttr = isExamTimerLocked ? 'disabled' : '';
                            const cursorClass = isExamTimerLocked ? 'cursor-not-allowed opacity-60' : 'cursor-pointer';

                            const isTrue = opt.name.toLowerCase() === 'true';
                            const isFalse = opt.name.toLowerCase() === 'false';

                            let containerClass = '';
                            let badgeClass = '';

                            if (isTrueFalse) {
                                if (isSelected) {
                                    containerClass = isTrue
                                        ? 'bg-emerald-950/60 border-emerald-500 shadow-lg shadow-emerald-950/50 ring-2 ring-emerald-500/60'
                                        : 'bg-rose-950/60 border-rose-500 shadow-lg shadow-rose-950/50 ring-2 ring-rose-500/60';
                                    badgeClass = isTrue
                                        ? 'bg-emerald-500 text-slate-950 font-black'
                                        : 'bg-rose-500 text-white font-black';
                                } else {
                                    containerClass = isTrue
                                        ? 'bg-slate-950 border-slate-800 hover:border-emerald-500/60 hover:bg-slate-900/60'
                                        : 'bg-slate-950 border-slate-800 hover:border-rose-500/60 hover:bg-slate-900/60';
                                    badgeClass = isTrue
                                        ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 font-extrabold'
                                        : 'bg-rose-500/20 text-rose-300 border border-rose-500/40 font-extrabold';
                                }
                            } else {
                                containerClass = isSelected
                                    ? 'bg-emerald-950/40 border-emerald-500/70 shadow-lg shadow-emerald-950/40 ring-1 ring-emerald-500/50'
                                    : 'bg-slate-950 border-slate-800 hover:border-indigo-500/60 hover:bg-slate-900/60';
                                badgeClass = isSelected
                                    ? 'bg-emerald-500 text-slate-950 font-black'
                                    : 'bg-indigo-500/20 text-indigo-300 border border-indigo-500/40 font-extrabold';
                            }

                            const displayBadgeContent = isTrueFalse
                                ? (isTrue ? '✓' : (isFalse ? '✗' : optionLetter))
                                : optionLetter;

                            optionsHtml += `
                                <label id="option_label_${opt.id}" class="group p-4 rounded-xl border ${containerClass} ${cursorClass} flex items-center justify-between transition-all">
                                    <div class="flex items-center space-x-3.5">
                                        <span class="w-8 h-8 rounded-xl ${badgeClass} flex items-center justify-center text-sm shrink-0 shadow-sm">
                                            ${displayBadgeContent}
                                        </span>
                                        <input type="radio" id="option_radio_${opt.id}" name="temp_option_${q.id}" value="${opt.id}" ${isChecked} ${disabledAttr} onchange="recordAnswerChoice(${q.id}, ${opt.id})" class="w-4 h-4 text-emerald-600 bg-slate-900 border-slate-700 focus:ring-emerald-500">
                                        <span class="text-sm font-semibold text-slate-200 group-hover:text-white">${opt.name}</span>
                                    </div>
                                    <span class="text-xs text-slate-500 font-mono font-medium">${isTrueFalse ? opt.name : 'Option ' + optionLetter}</span>
                                </label>
                            `;
                        });
                        optionsHtml += '</div>';
                    } else {
                        optionsHtml = '<p class="text-xs text-slate-500 italic mt-3">No multiple choice options defined for this question.</p>';
                    }

                    let typeBadge = '';
                    if (isTrueFalse) {
                        typeBadge = '<span class="px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 text-[10px] font-bold">True / False</span>';
                    } else if (isMatch) {
                        typeBadge = '<span class="px-2 py-0.5 rounded-full bg-indigo-500/10 text-indigo-400 border border-indigo-500/20 text-[10px] font-bold">Match the Following</span>';
                    } else if (isTextEntry) {
                        typeBadge = '<span class="px-2 py-0.5 rounded-full bg-amber-500/10 text-amber-400 border border-amber-500/20 text-[10px] font-bold">Text Entry</span>';
                    }

                    let hintSolutionButtonHtml = '';
                    let hintSolutionContentHtml = '';

                    const hasHint = Boolean(q.hint && q.hint.trim() !== '');
                    const hasSolution = Boolean(q.solution && q.solution.trim() !== '');

                    if (hasHint || hasSolution) {
                        let btnLabel = '💡 Hint / Solution';
                        if (hasHint && !hasSolution) btnLabel = '💡 Hint';
                        else if (!hasHint && hasSolution) btnLabel = '📝 Solution';

                        hintSolutionButtonHtml = `
                            <button type="button" onclick="toggleExamHintSolution()" class="inline-flex items-center space-x-1.5 px-3 py-1.5 rounded-xl bg-amber-500/15 hover:bg-amber-500/25 text-amber-300 border border-amber-500/30 text-xs font-bold transition-all shadow-sm cursor-pointer shrink-0">
                                <svg class="w-3.5 h-3.5 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/></svg>
                                <span>${btnLabel}</span>
                            </button>
                        `;

                        hintSolutionContentHtml = `
                            <div id="exam_hint_solution_panel" class="hidden p-4 rounded-xl bg-slate-900 border border-amber-500/40 shadow-inner space-y-3 transition-all">
                                <div class="flex items-center justify-between pb-2 border-b border-slate-800">
                                    <div class="flex items-center space-x-2">
                                        <span class="w-2 h-2 rounded-full bg-amber-400 animate-pulse"></span>
                                        <span class="text-xs font-extrabold uppercase tracking-wider text-amber-300">Question Help & Solution</span>
                                    </div>
                                    <button type="button" onclick="toggleExamHintSolution()" class="text-slate-400 hover:text-white text-xs font-semibold px-2 py-0.5 rounded-md hover:bg-slate-800 transition-colors">
                                        ✕ Hide
                                    </button>
                                </div>

                                ${hasHint ? `
                                    <div class="p-3 rounded-lg bg-amber-950/40 border border-amber-500/30 text-xs space-y-1">
                                        <div class="font-extrabold text-amber-400 flex items-center gap-1.5 uppercase tracking-wider text-[11px]">
                                            <span>💡 Hint:</span>
                                        </div>
                                        <div class="text-slate-200 leading-relaxed whitespace-pre-line pl-0.5">${escapeExamHtml(q.hint)}</div>
                                    </div>
                                ` : ''}

                                ${hasSolution ? `
                                    <div class="p-3 rounded-lg bg-emerald-950/40 border border-emerald-500/30 text-xs space-y-1">
                                        <div class="font-extrabold text-emerald-400 flex items-center gap-1.5 uppercase tracking-wider text-[11px]">
                                            <span>📝 Solution / Explanation:</span>
                                        </div>
                                        <div class="text-slate-200 leading-relaxed whitespace-pre-line pl-0.5">${escapeExamHtml(q.solution)}</div>
                                    </div>
                                ` : ''}
                            </div>
                        `;
                    }

                    document.getElementById('questionStepContainer').innerHTML = `
                        <div class="p-5 rounded-2xl bg-slate-950/80 border border-slate-800/80 shadow-md space-y-3">
                            <div class="flex items-start justify-between gap-4">
                                <div class="space-y-1">
                                    <div class="flex items-center space-x-2">
                                        <span class="text-xs font-bold uppercase tracking-wider text-indigo-400">Question ${currentExamStep + 1}</span>
                                        ${typeBadge}
                                    </div>
                                    <h4 class="text-lg font-bold text-white mt-1">${q.name}</h4>
                                    ${q.description ? `<p class="text-xs text-slate-300 mt-1">${q.description}</p>` : ''}
                                </div>
                                <div class="flex items-center space-x-2 shrink-0">
                                    ${hintSolutionButtonHtml}
                                    <span class="px-3 py-1 rounded-lg bg-amber-500/10 text-amber-300 border border-amber-500/20 text-xs font-bold shrink-0">
                                        ${q.marks} Mark(s)
                                    </span>
                                </div>
                            </div>
                            ${hintSolutionContentHtml}
                            ${optionsHtml}
                        </div>
                    `;

                    if (isTextEntry) {
                        renderStudentSymbols(q.id, 'chem');
                    }

                    // Update Button Controls
                    const prevBtn = document.getElementById('prevQuestionBtn');
                    const nextBtn = document.getElementById('nextQuestionBtn');
                    const submitBtn = document.getElementById('submitExamBtn');

                    prevBtn.classList.remove('hidden');
                    prevBtn.disabled = (currentExamStep === 0 || isExamTimerLocked);

                    if (currentExamStep === totalQuestions - 1) {
                        nextBtn.classList.add('hidden');
                        submitBtn.classList.remove('hidden');
                    } else {
                        nextBtn.classList.remove('hidden');
                        submitBtn.classList.add('hidden');
                    }

                    if (isExamTimerLocked) {
                        prevBtn.disabled = true;
                        nextBtn.disabled = true;
                        submitBtn.disabled = true;
                    }

                    updateAllFormAnswers();
                }

                function toggleExamHintSolution() {
                    const el = document.getElementById('exam_hint_solution_panel');
                    if (el) {
                        el.classList.toggle('hidden');
                    }
                }

                function recordAnswerChoice(qId, ansId) {
                    if (isExamTimerLocked) return;
                    userSelectedAnswers[qId] = ansId;
                    renderExamStep();
                }

                function recordMatchChoice(qId, ansId, chosenValue) {
                    if (isExamTimerLocked) return;
                    if (!userSelectedMatches[qId]) {
                        userSelectedMatches[qId] = {};
                    }
                    userSelectedMatches[qId][ansId] = chosenValue;
                    renderExamStep();
                }

                function updateAllFormAnswers() {
                    const form = document.getElementById('takeExamForm');
                    if (!form) return;
                    form.querySelectorAll('.answer-payload-input').forEach(el => el.remove());

                    Object.keys(userSelectedAnswers).forEach(qId => {
                        const val = userSelectedAnswers[qId];
                        if (val) {
                            const input = document.createElement('input');
                            input.type = 'hidden';
                            input.name = `answers[${qId}]`;
                            input.value = val;
                            input.className = 'answer-payload-input';
                            form.appendChild(input);
                        }
                    });

                    Object.keys(userSelectedMatches).forEach(qId => {
                        const qMatches = userSelectedMatches[qId];
                        if (qMatches && typeof qMatches === 'object') {
                            Object.keys(qMatches).forEach(ansId => {
                                const val = qMatches[ansId];
                                if (val !== undefined && val !== null && val !== '') {
                                    const input = document.createElement('input');
                                    input.type = 'hidden';
                                    input.name = `match_answers[${qId}][${ansId}]`;
                                    input.value = val;
                                    input.className = 'answer-payload-input';
                                    form.appendChild(input);
                                }
                            });
                        }
                    });

                    Object.keys(userSelectedTextAnswers).forEach(qId => {
                        const val = userSelectedTextAnswers[qId];
                        if (val !== undefined && val !== null && val.trim() !== '') {
                            const input = document.createElement('input');
                            input.type = 'hidden';
                            input.name = `text_answers[${qId}]`;
                            input.value = val;
                            input.className = 'answer-payload-input';
                            form.appendChild(input);
                        }
                    });
                }

                function navigateExamStep(direction) {
                    if (!currentExamData || !currentExamData.questions) return;
                    const totalQuestions = currentExamData.questions.length;

                    const newStep = currentExamStep + direction;
                    if (newStep >= 0 && newStep < totalQuestions) {
                        currentExamStep = newStep;
                        renderExamStep();
                    }
                }

                function confirmCancelExam() {
                    if (confirm('Are you sure you want to exit this exam session? Any selected answers will not be saved until submitted.')) {
                        stopExamTimer();
                        stopSpeechRecognition();
                        document.getElementById('takeExamModal').classList.add('hidden');
                    }
                }

                /* SPEECH RECOGNITION ENGINE FOR STUDENT EXAMS */
                let speechRecognitionInstance = null;
                let isSpeechActive = false;

                function toggleSpeechRecognition() {
                    if (isSpeechActive) {
                        stopSpeechRecognition();
                    } else {
                        startSpeechRecognition();
                    }
                }

                function startSpeechRecognition() {
                    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
                    if (!SpeechRecognition) {
                        alert('Speech Recognition is not supported by your browser. Please use Google Chrome, Microsoft Edge, or Safari.');
                        return;
                    }

                    try {
                        speechRecognitionInstance = new SpeechRecognition();
                        speechRecognitionInstance.continuous = true;
                        speechRecognitionInstance.interimResults = false;
                        speechRecognitionInstance.lang = 'en-US';

                        speechRecognitionInstance.onstart = function() {
                            isSpeechActive = true;
                            updateSpeechUI(true, 'Listening for voice commands...');
                        };

                        speechRecognitionInstance.onresult = function(event) {
                            const lastIndex = event.results.length - 1;
                            const transcript = event.results[lastIndex][0].transcript.trim().toLowerCase();
                            handleVoiceCommand(transcript);
                        };

                        speechRecognitionInstance.onerror = function(event) {
                            if (event.error === 'not-allowed') {
                                alert('Microphone permission was denied. Please allow microphone access in your browser settings.');
                                stopSpeechRecognition();
                            }
                        };

                        speechRecognitionInstance.onend = function() {
                            const modal = document.getElementById('takeExamModal');
                            if (isSpeechActive && modal && !modal.classList.contains('hidden')) {
                                try {
                                    speechRecognitionInstance.start();
                                } catch(e) {}
                            } else {
                                isSpeechActive = false;
                                updateSpeechUI(false);
                            }
                        };

                        speechRecognitionInstance.start();
                    } catch(err) {
                        console.error('Speech recognition error:', err);
                    }
                }

                function stopSpeechRecognition() {
                    isSpeechActive = false;
                    if (speechRecognitionInstance) {
                        try {
                            speechRecognitionInstance.stop();
                        } catch(e) {}
                    }
                    updateSpeechUI(false);
                }

                function updateSpeechUI(active, text) {
                    const micIcon = document.getElementById('speech_mic_icon');
                    const toggleText = document.getElementById('speech_toggle_text');
                    const statusBadge = document.getElementById('speech_status_badge');
                    const statusText = document.getElementById('speech_status_text');
                    const btn = document.getElementById('speechToggleBtn');

                    if (active) {
                        if (micIcon) micIcon.className = 'w-2.5 h-2.5 rounded-full bg-emerald-400 inline-block animate-pulse';
                        if (toggleText) toggleText.textContent = 'Voice Control: ON';
                        if (statusBadge) statusBadge.classList.remove('hidden');
                        if (statusText) statusText.textContent = text || 'Listening...';
                        if (btn) btn.className = 'px-3 py-1.5 rounded-xl bg-emerald-950 hover:bg-emerald-900 text-emerald-300 font-bold border border-emerald-500/40 transition-all cursor-pointer inline-flex items-center space-x-2';
                    } else {
                        if (micIcon) micIcon.className = 'w-2.5 h-2.5 rounded-full bg-slate-500 inline-block';
                        if (toggleText) toggleText.textContent = 'Voice Control: OFF';
                        if (statusBadge) statusBadge.classList.add('hidden');
                        if (btn) btn.className = 'px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-semibold border border-slate-700 transition-all cursor-pointer inline-flex items-center space-x-2';
                    }
                }

                function showSpeechFeedback(msg) {
                    const feedbackBox = document.getElementById('speech_feedback_box');
                    if (feedbackBox) {
                        feedbackBox.textContent = msg;
                        feedbackBox.classList.remove('hidden');
                        setTimeout(() => {
                            feedbackBox.classList.add('hidden');
                        }, 4000);
                    }
                }

                function handleVoiceCommand(transcript) {
                    console.log('Voice Command Spoken:', transcript);
                    showSpeechFeedback(`Spoken: "${transcript}"`);

                    if (!currentExamData || !currentExamData.questions) return;
                    const q = currentExamData.questions[currentExamStep];
                    if (!q) return;

                    // Voice Dictation for Text Entry Questions
                    if (parseInt(q.type) === 3) {
                        const textarea = document.getElementById(`student_text_ans_${q.id}`);
                        if (textarea) {
                            const prev = textarea.value;
                            const newVal = prev ? prev + ' ' + transcript : transcript;
                            textarea.value = newVal;
                            recordTextAnswer(q.id, newVal);
                            showSpeechFeedback(`✍ Dictated into answer: "${transcript}"`);
                            return;
                        }
                    }

                    if (!q.answers) return;

                    let targetIndex = -1;

                    // Option A / 1 / First
                    if (transcript.includes('option a') || transcript.includes('option 1') || transcript.includes('select a') || transcript.includes('choice a') || transcript.includes('first option') || transcript === 'a' || transcript.endsWith(' a') || transcript === 'option a') {
                        targetIndex = 0;
                    } 
                    // Option B / 2 / Second
                    else if (transcript.includes('option b') || transcript.includes('option 2') || transcript.includes('select b') || transcript.includes('choice b') || transcript.includes('second option') || transcript === 'b' || transcript.endsWith(' b') || transcript === 'option b') {
                        targetIndex = 1;
                    } 
                    // Option C / 3 / Third
                    else if (transcript.includes('option c') || transcript.includes('option 3') || transcript.includes('select c') || transcript.includes('choice c') || transcript.includes('third option') || transcript === 'c' || transcript.endsWith(' c') || transcript === 'option c') {
                        targetIndex = 2;
                    } 
                    // Option D / 4 / Fourth
                    else if (transcript.includes('option d') || transcript.includes('option 4') || transcript.includes('select d') || transcript.includes('choice d') || transcript.includes('fourth option') || transcript === 'd' || transcript.endsWith(' d') || transcript === 'option d') {
                        targetIndex = 3;
                    } 
                    // Option E / 5
                    else if (transcript.includes('option e') || transcript.includes('option 5') || transcript === 'e' || transcript.endsWith(' e') || transcript === 'option e') {
                        targetIndex = 4;
                    }

                    if (targetIndex >= 0 && targetIndex < q.answers.length) {
                        const selectedOpt = q.answers[targetIndex];
                        const letter = String.fromCharCode(65 + targetIndex);
                        
                        recordAnswerChoice(q.id, selectedOpt.id);
                        showSpeechFeedback(`✔ Selected Option ${letter}: ${selectedOpt.name}`);
                        return;
                    }

                    // Navigation commands
                    if (transcript.includes('next') || transcript.includes('forward') || transcript.includes('move on')) {
                        const totalQuestions = currentExamData.questions.length;
                        if (currentExamStep < totalQuestions - 1) {
                            navigateExamStep(1);
                            showSpeechFeedback('▶ Moved to Next Question');
                        }
                    } else if (transcript.includes('previous') || transcript.includes('prev') || transcript.includes('back')) {
                        if (currentExamStep > 0) {
                            navigateExamStep(-1);
                            showSpeechFeedback('◀ Moved to Previous Question');
                        }
                    }
                }

                function openStudentViewSubmissionModal(data) {
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
                    document.getElementById('sub_summary_correct_cnt').textContent = partialCount > 0
                        ? `${correctCount} Correct, ${partialCount} Partial`
                        : `${correctCount} Question(s)`;
                    document.getElementById('sub_summary_wrong_cnt').textContent = textEntryCount > 0
                        ? `${wrongCount} Wrong, ${textEntryCount} Text Entry`
                        : `${wrongCount} Question(s)`;

                    if (details.length === 0) {
                        container.innerHTML = '<div class="p-8 text-center bg-white rounded-xl border border-slate-200 text-slate-500 text-sm font-medium">No detailed questions or answers found for this submission.</div>';
                    } else {
                        details.forEach((d, idx) => {
                            const isTextEntry = d.is_text_entry;
                            const isCorrect = d.is_correct;
                            const isPartial = d.is_partially_correct;
                            const earnedMarks = d.earned_marks !== undefined ? d.earned_marks : (isCorrect ? d.question_marks : 0);

                            let cardBorderClass = 'border-l-4 border-l-rose-500 border-t border-r border-b border-slate-200 bg-white';
                            let statusBadge = `<span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-black bg-rose-100 text-black border border-rose-300">
                                                 <svg class="w-3.5 h-3.5 mr-1 text-black shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12"/></svg>
                                                 Wrong (0 Marks)
                                               </span>`;

                            const isEvaluated = d.is_evaluated || (d.teacher_marks !== null && d.teacher_marks !== undefined);

                            if (isTextEntry) {
                                if (isEvaluated) {
                                    cardBorderClass = 'border-l-4 border-l-emerald-500 border-t border-r border-b border-slate-200 bg-white';
                                    statusBadge = `<span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-black bg-emerald-100 text-black border border-emerald-300">
                                                     <svg class="w-3.5 h-3.5 mr-1 text-black shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>
                                                     Evaluated by Teacher (+${earnedMarks} / ${d.question_marks} Marks)
                                                   </span>`;
                                } else {
                                    cardBorderClass = 'border-l-4 border-l-amber-500 border-t border-r border-b border-slate-200 bg-white';
                                    statusBadge = `<span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-black bg-amber-100 text-black border border-amber-300">
                                                     <svg class="w-3.5 h-3.5 mr-1 text-black shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
                                                     Pending Teacher Evaluation
                                                   </span>`;
                                }
                            } else if (isCorrect) {
                                cardBorderClass = 'border-l-4 border-l-emerald-500 border-t border-r border-b border-slate-200 bg-white';
                                statusBadge = `<span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-black bg-emerald-100 text-black border border-emerald-300">
                                                 <svg class="w-3.5 h-3.5 mr-1 text-black shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>
                                                 Correct (+${earnedMarks} Marks)
                                               </span>`;
                            } else if (isPartial) {
                                cardBorderClass = 'border-l-4 border-l-amber-500 border-t border-r border-b border-slate-200 bg-white';
                                statusBadge = `<span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-black bg-amber-100 text-black border border-amber-300">
                                                 <svg class="w-3.5 h-3.5 mr-1 text-black shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
                                                 Partial (+${earnedMarks} Marks)
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
                                        <span class="text-black font-black text-sm sm:text-base ml-1">${d.correct_answer}</span>
                                    </div>
                                `;
                            }

                            let matchPairsMarkup = '';
                            if (d.match_pairs && d.match_pairs.length > 0) {
                                matchPairsMarkup = `
                                    <div class="mt-2 space-y-2">
                                        <div class="flex items-center justify-between pb-1 border-b border-slate-100">
                                            <span class="text-[10px] font-extrabold uppercase tracking-wider text-black">Matching Pairs Details (1 Mark per Match):</span>
                                            <span class="text-xs font-black text-black bg-slate-100 px-2.5 py-0.5 rounded-full border border-slate-200">${earnedMarks} / ${d.question_marks} Marks</span>
                                        </div>
                                        ${d.match_pairs.map(p => `
                                            <div class="p-2.5 rounded-xl border ${p.is_correct ? 'bg-emerald-50/90 border-emerald-300' : 'bg-rose-50/90 border-rose-300'} flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-xs">
                                                <div class="flex items-center space-x-2">
                                                    <span class="w-5 h-5 rounded-md ${p.is_correct ? 'bg-emerald-600' : 'bg-rose-600'} text-white font-bold text-[10px] flex items-center justify-center shrink-0">
                                                        ${p.is_correct ? '✓' : '✕'}
                                                    </span>
                                                    <span class="font-bold text-black">${p.letter}. ${p.left}</span>
                                                </div>
                                                <div class="flex items-center space-x-2 pl-7 sm:pl-0 flex-wrap">
                                                    <span class="text-black font-medium">Selected: <span class="font-extrabold ${p.is_correct ? 'text-emerald-950' : 'text-rose-950'}">${p.student_match}</span></span>
                                                    ${!p.is_correct && p.correct_match ? `<span class="text-emerald-900 font-bold">→ Correct: <span class="font-black underline">${p.correct_match}</span></span>` : ''}
                                                    <span class="ml-auto inline-flex items-center px-1.5 py-0.5 rounded text-[10px] font-black ${p.is_correct ? 'bg-emerald-200/80 text-emerald-950' : 'bg-rose-200/80 text-rose-950'}">
                                                        ${p.is_correct ? '+1 Mark' : '0 Marks'}
                                                    </span>
                                                </div>
                                            </div>
                                        `).join('')}
                                    </div>
                                `;
                            }

                            let hintSolutionReviewMarkup = '';
                            if (d.hint || d.solution) {
                                hintSolutionReviewMarkup = `
                                    <div class="mt-2.5 p-3 rounded-xl bg-slate-50 border border-slate-200 space-y-2 text-xs">
                                        ${d.hint ? `
                                            <div class="flex items-start space-x-2">
                                                <span class="px-1.5 py-0.5 rounded bg-amber-100 text-amber-900 border border-amber-300 font-extrabold text-[10px] shrink-0 uppercase">Hint</span>
                                                <span class="text-black leading-relaxed whitespace-pre-line">${d.hint}</span>
                                            </div>
                                        ` : ''}
                                        ${d.solution ? `
                                            <div class="flex items-start space-x-2">
                                                <span class="px-1.5 py-0.5 rounded bg-emerald-100 text-emerald-950 border border-emerald-300 font-extrabold text-[10px] shrink-0 uppercase">Solution</span>
                                                <span class="text-black font-medium leading-relaxed whitespace-pre-line">${d.solution}</span>
                                            </div>
                                        ` : ''}
                                    </div>
                                `;
                            }

                            const html = `
                                <div class="p-4 sm:p-5 rounded-xl ${cardBorderClass} shadow-sm space-y-3 transition-all hover:shadow-md">
                                    <div class="flex items-start justify-between gap-3">
                                        <div class="space-y-1">
                                            <div class="flex items-center space-x-2">
                                                <span class="px-2.5 py-0.5 rounded-md bg-slate-900 text-white text-xs font-extrabold">Q${idx + 1}</span>
                                                <h5 class="text-sm sm:text-base font-bold text-black">${d.question_name}</h5>
                                            </div>
                                        </div>
                                        <div class="shrink-0 flex items-center space-x-2">
                                            ${statusBadge}
                                        </div>
                                    </div>

                                    <div class="pt-1 space-y-2">
                                        ${isTextEntry ? `
                                            <div class="p-3.5 rounded-xl border border-amber-200 bg-amber-50/50 space-y-2">
                                                <div class="flex items-center justify-between">
                                                    <span class="text-[10px] font-extrabold uppercase tracking-wider text-black flex items-center gap-1.5">
                                                        <span>✍️ Student Written Answer</span>
                                                    </span>
                                                    <span class="text-[10px] font-bold ${isEvaluated ? 'text-emerald-900 bg-emerald-100 border border-emerald-300' : 'text-amber-900 bg-amber-100 border border-amber-300'} px-2 py-0.5 rounded-full">
                                                        ${isEvaluated ? `Evaluated: ${earnedMarks} / ${d.question_marks} Marks` : 'Requires Teacher Evaluation'}
                                                    </span>
                                                </div>
                                                <div class="text-sm font-medium text-black whitespace-pre-wrap leading-relaxed p-3 rounded-lg bg-white border border-slate-200 font-sans">${escapeExamHtml(d.student_text_answer || d.selected_answer || '(No text answer entered)')}</div>
                                                ${d.teacher_feedback ? `
                                                    <div class="p-3 rounded-lg bg-indigo-50 border border-indigo-200 text-xs mt-2">
                                                        <span class="text-indigo-950 font-extrabold uppercase tracking-wider text-[11px] block">Teacher Feedback:</span>
                                                        <p class="text-black font-medium mt-1 leading-relaxed">${escapeExamHtml(d.teacher_feedback)}</p>
                                                    </div>
                                                ` : ''}
                                            </div>
                                        ` : (d.match_pairs && d.match_pairs.length > 0 ? matchPairsMarkup : `
                                            <div class="p-3 rounded-xl border ${ansBoxClass} flex items-center justify-between gap-3">
                                                <div class="flex items-center space-x-2.5">
                                                    ${ansIcon}
                                                    <div>
                                                        <span class="text-[10px] font-extrabold uppercase tracking-wider text-black block">Submitted Answer</span>
                                                        <span class="text-sm sm:text-base font-black text-black">${d.selected_answer}</span>
                                                    </div>
                                                </div>
                                                <span class="text-xs font-bold text-black">${earnedMarks} / ${d.question_marks} Marks</span>
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

                    document.getElementById('studentViewSubmissionModal').classList.remove('hidden');
                }

                function openStudentViewExamModal(data) {
                    document.getElementById('student_view_exam_name').textContent = data.name || '';
                    document.getElementById('student_view_exam_type').textContent = data.type || '';
                    document.getElementById('student_view_exam_status').textContent = data.status || '';
                    document.getElementById('student_view_exam_total_mark').textContent = (data.total_mark || 0) + ' Mark(s)';
                    document.getElementById('student_view_exam_creator').textContent = data.creator || 'System';

                    const qListContainer = document.getElementById('student_view_exam_questions_list');
                    const qCountBadge = document.getElementById('student_view_exam_q_count');
                    qListContainer.innerHTML = '';

                    const questions = data.questions || [];
                    qCountBadge.textContent = questions.length + ' Question(s)';

                    if (questions.length === 0) {
                        qListContainer.innerHTML = '<p class="text-xs text-slate-500 text-center py-6">No questions linked to this exam yet.</p>';
                    } else {
                        questions.forEach((q, idx) => {
                            let optionsHtml = '';
                            if (q.answers && q.answers.length > 0) {
                                optionsHtml = '<div class="mt-2 grid grid-cols-1 sm:grid-cols-2 gap-1.5">';
                                q.answers.forEach(opt => {
                                    optionsHtml += `<div class="text-[11px] px-2.5 py-1 rounded bg-slate-900 border border-slate-800 text-slate-300 font-mono">${opt}</div>`;
                                });
                                optionsHtml += '</div>';
                            }

                            const itemHtml = `
                                <div class="p-3.5 rounded-lg bg-slate-900/80 border border-slate-800">
                                    <div class="flex items-start justify-between gap-3">
                                        <div>
                                            <div class="flex items-center space-x-2">
                                                <span class="text-xs font-bold text-sky-400">Q${idx + 1}.</span>
                                                <h6 class="text-xs font-semibold text-slate-200">${q.name}</h6>
                                            </div>
                                            ${q.description ? `<p class="text-xs text-slate-400 mt-1 pl-6">${q.description}</p>` : ''}
                                            <div class="flex items-center flex-wrap gap-2 mt-1.5 text-[11px] text-slate-400">
                                                <span class="px-2 py-0.5 rounded bg-slate-800 text-slate-300 border border-slate-700">Type: ${q.type}</span>
                                            </div>
                                            ${(q.hint || q.solution) ? `
                                                <div class="mt-2 pl-6 space-y-1 text-xs">
                                                    ${q.hint ? `<div class="text-amber-300"><span class="font-bold">💡 Hint:</span> ${escapeExamHtml(q.hint)}</div>` : ''}
                                                    ${q.solution ? `<div class="text-emerald-300"><span class="font-bold">📝 Solution:</span> ${escapeExamHtml(q.solution)}</div>` : ''}
                                                </div>
                                            ` : ''}
                                        </div>
                                        <span class="text-xs font-bold text-amber-400 bg-amber-500/10 px-2 py-0.5 rounded border border-amber-500/20 shrink-0">${q.marks} Mark(s)</span>
                                    </div>
                                    ${optionsHtml}
                                </div>
                            `;
                            qListContainer.innerHTML += itemHtml;
                        });
                    }

                    document.getElementById('studentViewExamModal').classList.remove('hidden');
                }
            </script>

        @else
            <!-- TEACHER DASHBOARD (Type = 1) -->

            <!-- Welcome Hero Banner -->
            <div class="relative overflow-hidden rounded-2xl bg-gradient-to-r from-indigo-900/60 via-slate-900 to-slate-900 border border-indigo-500/20 p-6 sm:p-8 shadow-xl">
                <div class="relative z-10 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-6">
                    <div>
                        <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-indigo-500/10 border border-indigo-500/20 text-indigo-300 text-xs font-semibold uppercase tracking-wider mb-3">
                            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                            <span>Active Session</span>
                        </div>
                        <h1 class="text-3xl font-extrabold text-white tracking-tight sm:text-4xl">
                            Welcome back, {{ $user->name }}!
                        </h1>
                        <p class="mt-2 text-slate-300 text-sm max-w-xl">
                            You are signed in as <span class="text-indigo-300 font-medium">{{ $user->email }}</span>. Manage your assigned standards and add questions.
                        </p>
                    </div>
                    <div class="shrink-0 flex items-center flex-wrap gap-3">
                        <form method="POST" action="{{ route('logout') }}">
                            @csrf
                            <button type="submit" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium text-sm transition-all shadow-md flex items-center space-x-2 cursor-pointer">
                                <svg class="w-4 h-4 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
                                </svg>
                                <span>Sign Out</span>
                            </button>
                        </form>
                    </div>

                </div>
            </div>

            <!-- Quick Actions Cards Grid -->
            <div class="grid grid-cols-2 lg:grid-cols-4 gap-3.5">
                <!-- Quick Standards Action Banner Card -->
                <div onclick="window.location.href='{{ route('standards.index') }}'" class="bg-gradient-to-r from-emerald-950/80 to-slate-900 border border-emerald-500/30 hover:border-emerald-500/60 rounded-xl p-3.5 shadow-md flex flex-col justify-between gap-2.5 cursor-pointer transition-all group">
                    <div class="flex items-center space-x-2.5 min-w-0">
                        <div class="w-8 h-8 rounded-lg bg-emerald-600/20 border border-emerald-500/30 text-emerald-400 flex items-center justify-center shrink-0 group-hover:bg-emerald-600/30 transition-all">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
                            </svg>
                        </div>
                        <div class="min-w-0 flex-1">
                            <h3 class="text-xs sm:text-sm font-bold text-white truncate group-hover:text-emerald-300 transition-colors">Class Standards</h3>
                            <p class="text-[11px] text-slate-400 truncate">Manage or add classes</p>
                        </div>
                    </div>
                    <div class="flex items-center justify-end space-x-1.5 pt-1 border-t border-slate-800/60">
                        <a href="{{ route('standards.index') }}" class="px-2.5 py-1 rounded-lg bg-teal-600 hover:bg-teal-500 text-white font-medium text-[11px] transition-all shadow-sm flex items-center space-x-1 cursor-pointer">
                            <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>
                            <span>Manage</span>
                        </a>
                        <button onclick="event.stopPropagation(); document.getElementById('createStandardModal').classList.remove('hidden')" class="px-2.5 py-1 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-medium text-[11px] transition-all shadow-sm flex items-center space-x-1 cursor-pointer">
                            <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
                            <span>Add</span>
                        </button>
                    </div>
                </div>

                <!-- Quick Exams Action Banner Card -->
                <div onclick="window.location.href='{{ route('exams.index') }}'" class="bg-gradient-to-r from-indigo-950/80 to-slate-900 border border-indigo-500/30 hover:border-indigo-500/60 rounded-xl p-3.5 shadow-md flex flex-col justify-between gap-2.5 cursor-pointer transition-all group">
                    <div class="flex items-center space-x-2.5 min-w-0">
                        <div class="w-8 h-8 rounded-lg bg-indigo-600/20 border border-indigo-500/30 text-indigo-400 flex items-center justify-center shrink-0 group-hover:bg-indigo-600/30 transition-all">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                            </svg>
                        </div>
                        <div class="min-w-0 flex-1">
                            <h3 class="text-xs sm:text-sm font-bold text-white truncate group-hover:text-indigo-300 transition-colors">Exams & Assessment</h3>
                            <p class="text-[11px] text-slate-400 truncate">Performance & reports</p>
                        </div>
                    </div>
                    <div class="flex items-center justify-end pt-1 border-t border-slate-800/60">
                        <a href="{{ route('exams.index') }}" class="px-2.5 py-1 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-medium text-[11px] transition-all shadow-sm flex items-center space-x-1">
                            <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
                            <span>Manage Exams</span>
                        </a>
                    </div>
                </div>

                <!-- Quick Questions Action Banner Card -->
                <div onclick="window.location.href='{{ route('questions.index') }}'" class="bg-gradient-to-r from-slate-900 to-indigo-950/60 border border-slate-800 hover:border-violet-500/60 rounded-xl p-3.5 shadow-md flex flex-col justify-between gap-2.5 cursor-pointer transition-all group">
                    <div class="flex items-center space-x-2.5 min-w-0">
                        <div class="w-8 h-8 rounded-lg bg-violet-600/20 border border-violet-500/30 text-violet-400 flex items-center justify-center shrink-0 group-hover:bg-violet-600/30 transition-all">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                            </svg>
                        </div>
                        <div class="min-w-0 flex-1">
                            <h3 class="text-xs sm:text-sm font-bold text-white truncate group-hover:text-violet-300 transition-colors">Question Bank</h3>
                            <p class="text-[11px] text-slate-400 truncate">Add new questions</p>
                        </div>
                    </div>
                    <div class="flex items-center justify-end pt-1 border-t border-slate-800/60">
                        <a href="{{ route('questions.index') }}" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium text-[11px] transition-all shadow-sm flex items-center space-x-1">
                            <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
                            <span>Add Questions</span>
                        </a>
                    </div>
                </div>

                <!-- Quick My Students Action Banner Card -->
                <div onclick="window.location.href='{{ route('students.index') }}'" class="bg-gradient-to-r from-sky-950/80 to-slate-900 border border-sky-500/30 hover:border-sky-500/60 rounded-xl p-3.5 shadow-md flex flex-col justify-between gap-2.5 cursor-pointer transition-all group">
                    <div class="flex items-center space-x-2.5 min-w-0">
                        <div class="w-8 h-8 rounded-lg bg-sky-600/20 border border-sky-500/30 text-sky-400 flex items-center justify-center shrink-0 group-hover:bg-sky-600/30 transition-all">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z" />
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0112 20.055a11.952 11.952 0 01-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z" />
                            </svg>
                        </div>
                        <div class="min-w-0 flex-1">
                            <h3 class="text-xs sm:text-sm font-bold text-white truncate group-hover:text-sky-300 transition-colors">My Students</h3>
                            <p class="text-[11px] text-slate-400 truncate">Students in my classes</p>
                        </div>
                    </div>
                    <div class="flex items-center justify-end pt-1 border-t border-slate-800/60">
                        <a href="{{ route('students.index') }}" class="px-2.5 py-1 rounded-lg bg-sky-600 hover:bg-sky-500 text-white font-medium text-[11px] transition-all shadow-sm flex items-center space-x-1">
                            <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
                            <span>View Students</span>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Metric Stat Cards -->
            <div class="grid grid-cols-2 lg:grid-cols-4 gap-3.5">
                <div class="bg-slate-900 border border-slate-800 rounded-xl p-3.5 sm:p-4 shadow-md hover:border-slate-700 transition-all">
                    <div class="flex items-center justify-between">
                        <span class="text-[11px] font-semibold text-slate-400 uppercase tracking-wider">Account Status</span>
                        <div class="p-1.5 bg-emerald-500/10 rounded-lg text-emerald-400">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                        </div>
                    </div>
                    <p class="mt-2 text-xl font-bold text-white">{{ ($user->status ?? 1) == 1 ? 'Active' : 'Inactive' }}</p>
                    <p class="mt-0.5 text-[11px] text-slate-400">Teacher Account Status</p>
                </div>

                <div class="bg-slate-900 border border-slate-800 rounded-xl p-3.5 sm:p-4 shadow-md hover:border-slate-700 transition-all">
                    <div class="flex items-center justify-between">
                        <span class="text-[11px] font-semibold text-slate-400 uppercase tracking-wider">User ID</span>
                        <div class="p-1.5 bg-indigo-500/10 rounded-lg text-indigo-400">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
                        </div>
                    </div>
                    <p class="mt-2 text-xl font-bold text-white">#{{ str_pad($user->id, 4, '0', STR_PAD_LEFT) }}</p>
                    <p class="mt-0.5 text-[11px] text-slate-400">Unique user identifier</p>
                </div>

                <div onclick="window.location.href='{{ route('standards.index') }}'" class="bg-slate-900 border border-slate-800 hover:border-violet-500/50 rounded-xl p-3.5 sm:p-4 shadow-md hover:shadow-violet-500/10 transition-all cursor-pointer group">
                    <div class="flex items-center justify-between">
                        <span class="text-[11px] font-semibold text-slate-400 group-hover:text-slate-300 uppercase tracking-wider">Assigned Standards</span>
                        <div class="p-1.5 bg-violet-500/10 group-hover:bg-violet-500/20 rounded-lg text-violet-400 transition-colors">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
                        </div>
                    </div>
                    <p class="mt-2 text-xl font-bold text-white">{{ $user->standards->count() }}</p>
                    <p class="mt-0.5 text-[11px] text-slate-400">Classes assigned</p>
                </div>

                <div onclick="window.location.href='{{ route('students.index') }}'" class="bg-slate-900 border border-slate-800 hover:border-sky-500/50 rounded-xl p-3.5 sm:p-4 shadow-md hover:shadow-sky-500/10 transition-all cursor-pointer group">
                    <div class="flex items-center justify-between">
                        <span class="text-[11px] font-semibold text-slate-400 group-hover:text-slate-300 uppercase tracking-wider">Linked Students</span>
                        <div class="p-1.5 bg-sky-500/10 group-hover:bg-sky-500/20 rounded-lg text-sky-400 transition-colors">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0112 20.055a11.952 11.952 0 01-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"/></svg>
                        </div>
                    </div>
                    <p class="mt-2 text-xl font-bold text-white">{{ $teacherStudentsCount ?? 0 }}</p>
                    <p class="mt-0.5 text-[11px] text-slate-400">Students in your classes</p>
                </div>
            </div>

            <!-- Exam Performance & Submissions Report (Teacher View - Moved to /exams) -->
            {{-- Commented out: Exam Performance & Submissions Report now lives on dedicated page /exams
            <div id="teacherExamPerformanceReportContainer" class="bg-slate-900 border border-slate-800 rounded-2xl shadow-xl overflow-hidden scroll-mt-20 transition-all duration-500">
                <div class="px-6 py-5 border-b border-slate-800 flex items-center justify-between flex-wrap gap-4">
                    <div>
                        <h3 class="text-lg font-semibold text-white flex items-center space-x-2">
                            <svg class="w-5 h-5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                            </svg>
                            <span>Exam Performance & Submissions Report</span>
                            @if(request()->filled('exam_name') || request()->filled('exam_type') || request()->filled('type') || request()->filled('exam_syllabus_id') || request()->filled('exam_subject_id') || request()->filled('exam_chapter_id') || request()->filled('exam_topic_id'))
                                <span class="text-xs px-2.5 py-0.5 rounded-full bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 font-medium">Filtered</span>
                            @endif
                        </h3>
                        <p class="text-xs text-slate-400 mt-0.5">Track student completions, scores, and question-level evaluation details</p>
                    </div>
                    <span class="text-xs text-slate-400 bg-slate-800 px-3 py-1 rounded-full border border-slate-700">
                        Total: {{ method_exists($teacherExams, 'total') ? $teacherExams->total() : $teacherExams->count() }} Exam(s)
                    </span>
                </div>

                <!-- Teacher Exam Search & Curriculum Filter Bar -->
                <div class="p-4 sm:p-5 bg-slate-950/60 border-b border-slate-800/80">
                    <form method="GET" action="{{ route('dashboard') }}" class="space-y-3">
                        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-3">
                            <!-- Exam Name -->
                            <div>
                                <label class="block text-[11px] font-semibold text-slate-400 uppercase tracking-wider mb-1">Exam Name</label>
                                <div class="relative">
                                    <input type="text" name="exam_name" value="{{ request('exam_name') }}" placeholder="Search exam name..." class="w-full pl-8 pr-3 py-2 bg-slate-900 border border-slate-800 rounded-xl text-xs text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                    <svg class="w-3.5 h-3.5 text-slate-500 absolute left-2.5 top-2.5 pointer-events-none" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                                </div>
                            </div>

                            <!-- Exam Type -->
                            <div>
                                <label class="block text-[11px] font-semibold text-slate-400 uppercase tracking-wider mb-1">Exam Type</label>
                                <select name="exam_type" id="teacher_filter_type" class="w-full px-3 py-2 bg-slate-900 border border-slate-800 rounded-xl text-xs text-slate-200 focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                    <option value="">All Types</option>
                                    <option value="1" {{ (request('exam_type') == '1' || request('type') == '1') ? 'selected' : '' }}>1 - Timed Exam</option>
                                    <option value="2" {{ (request('exam_type') == '2' || request('type') == '2') ? 'selected' : '' }}>2 - Non-Timed Exam</option>
                                    <option value="3" {{ (request('exam_type') == '3' || request('type') == '3') ? 'selected' : '' }}>3 - Text Entry Exam</option>
                                </select>
                            </div>

                            <!-- Syllabus -->
                            <div>
                                <label class="block text-[11px] font-semibold text-slate-400 uppercase tracking-wider mb-1">Syllabus</label>
                                <select name="exam_syllabus_id" id="teacher_filter_syllabus" onchange="onTeacherFilterSyllabusChange()" class="w-full px-3 py-2 bg-slate-900 border border-slate-800 rounded-xl text-xs text-slate-200 focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                    <option value="">All Syllabuses</option>
                                    @foreach($syllabi as $syl)
                                        <option value="{{ $syl->id }}" {{ request('exam_syllabus_id') == $syl->id ? 'selected' : '' }}>{{ $syl->name }}</option>
                                    @endforeach
                                </select>
                            </div>

                            <!-- Subject -->
                            <div>
                                <label class="block text-[11px] font-semibold text-slate-400 uppercase tracking-wider mb-1">Subject</label>
                                <select name="exam_subject_id" id="teacher_filter_subject" onchange="onTeacherFilterSubjectChange()" class="w-full px-3 py-2 bg-slate-900 border border-slate-800 rounded-xl text-xs text-slate-200 focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                    <option value="">All Subjects</option>
                                    @foreach($subjects as $subj)
                                        <option value="{{ $subj->id }}" {{ request('exam_subject_id') == $subj->id ? 'selected' : '' }}>{{ $subj->name }}</option>
                                    @endforeach
                                </select>
                            </div>

                            <!-- Chapter -->
                            <div>
                                <label class="block text-[11px] font-semibold text-slate-400 uppercase tracking-wider mb-1">Chapter</label>
                                <select name="exam_chapter_id" id="teacher_filter_chapter" onchange="onTeacherFilterChapterChange()" class="w-full px-3 py-2 bg-slate-900 border border-slate-800 rounded-xl text-xs text-slate-200 focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                    <option value="">All Chapters</option>
                                    @foreach($chapters as $ch)
                                        <option value="{{ $ch->id }}" {{ request('exam_chapter_id') == $ch->id ? 'selected' : '' }}>{{ $ch->name }}</option>
                                    @endforeach
                                </select>
                            </div>

                            <!-- Topic -->
                            <div>
                                <label class="block text-[11px] font-semibold text-slate-400 uppercase tracking-wider mb-1">Topic</label>
                                <select name="exam_topic_id" id="teacher_filter_topic" class="w-full px-3 py-2 bg-slate-900 border border-slate-800 rounded-xl text-xs text-slate-200 focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                    <option value="">All Topics</option>
                                    @foreach($topics as $tp)
                                        <option value="{{ $tp->id }}" {{ request('exam_topic_id') == $tp->id ? 'selected' : '' }}>{{ $tp->name }}</option>
                                    @endforeach
                                </select>
                            </div>
                        </div>

                        <div class="flex items-center justify-end space-x-2 pt-1">
                            @if(request()->filled('exam_name') || request()->filled('exam_type') || request()->filled('type') || request()->filled('exam_syllabus_id') || request()->filled('exam_subject_id') || request()->filled('exam_chapter_id') || request()->filled('exam_topic_id'))
                                <a href="{{ route('dashboard') }}" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition-colors inline-flex items-center space-x-1.5">
                                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                                    <span>Clear Filters</span>
                                </a>
                            @endif
                            <button type="submit" class="px-5 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold shadow-md shadow-indigo-600/30 transition-all inline-flex items-center space-x-1.5 cursor-pointer">
                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                                <span>Filter Exams</span>
                            </button>
                        </div>
                    </form>
                </div>

                @if($teacherExams->isNotEmpty())
                    <div class="divide-y divide-slate-800/80">
                        @foreach ($teacherExams as $exam)
                            @php
                                $examSubmissions = $teacherExamSubmissions->get($exam->id, collect());
                                $completedStudentCount = $examSubmissions->count();
                                $totalExamMarks = $exam->total_mark > 0 ? $exam->total_mark : $exam->questions->sum('marks');
                            @endphp

                            <div class="bg-slate-900 hover:bg-slate-800/40 transition-colors">
                                <!-- Collapsible Exam Header -->
                                <div onclick="toggleTeacherExamDetails({{ $exam->id }})" class="px-6 py-4 flex flex-col sm:flex-row sm:items-center justify-between gap-3 cursor-pointer group select-none">
                                    <div class="flex items-center space-x-3.5">
                                        <div class="w-10 h-10 rounded-xl bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 font-bold flex items-center justify-center text-sm group-hover:bg-indigo-500/20 transition-colors shrink-0">
                                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                                        </div>
                                        <div>
                                            <h4 class="text-base font-bold text-white group-hover:text-indigo-300 transition-colors flex items-center space-x-2">
                                                <span>{{ $exam->name }}</span>
                                            </h4>
                                            <div class="flex items-center flex-wrap gap-2 mt-1 text-xs text-slate-400">
                                                <span>Teacher: <strong class="text-sky-300">{{ $exam->creator?->name ?? 'System' }}</strong></span>
                                                <span>•</span>
                                                <span>Total Marks: <strong class="text-amber-400 font-mono">{{ $totalExamMarks }}</strong></span>
                                                <span>•</span>
                                                <span>Questions: <strong class="text-slate-200">{{ $exam->questions->count() }}</strong></span>
                                                @if($exam->standards->isNotEmpty())
                                                    <span>•</span>
                                                    <span>Class: <strong class="text-indigo-300">{{ $exam->standards->pluck('name')->join(', ') }}</strong></span>
                                                @endif
                                            </div>
                                        </div>
                                    </div>

                                    <div class="flex items-center space-x-3 shrink-0">
                                        <button type="button" onclick="event.stopPropagation(); openExamLeaderboardModal({{ $exam->id }}, '{{ addslashes($exam->name) }}')" class="px-3 py-1 rounded-lg bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 border border-amber-500/40 text-xs font-extrabold transition-all inline-flex items-center space-x-1 cursor-pointer shadow-sm">
                                            <span>🏆 Leaderboard</span>
                                        </button>

                                        @if(($exam->student_exam_details_count ?? $completedStudentCount) === 0 && ($isAdmin || (int)$exam->created_by === (int)$user->id))
                                            <button type="button" onclick="event.stopPropagation(); openDashboardEditExamModal({{ json_encode([
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
                                                'standards' => $exam->standards->pluck('id')->toArray(),
                                                'action' => route('exams.update', $exam->id),
                                            ]) }})" class="px-2.5 py-1 rounded-lg bg-indigo-500/20 hover:bg-indigo-500/30 text-indigo-300 border border-indigo-500/40 text-xs font-bold transition-all inline-flex items-center space-x-1 cursor-pointer shadow-sm">
                                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/></svg>
                                                <span>Edit</span>
                                            </button>

                                            <a href="{{ route('exams.show', $exam->id) }}" onclick="event.stopPropagation();" class="inline-flex items-center space-x-1 px-3 py-1 rounded-lg bg-indigo-600/20 hover:bg-indigo-600/40 text-indigo-300 border border-indigo-500/30 text-xs font-semibold transition-all shadow-sm">
                                                <span>Manage Questions</span>
                                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                                            </a>
                                        @endif

                                        @if($completedStudentCount > 0)
                                            <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-extrabold bg-emerald-500/20 text-emerald-400 border border-emerald-500/40">
                                                <svg class="w-3.5 h-3.5 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>
                                                {{ $completedStudentCount }} Student(s) Completed
                                            </span>
                                        @else
                                            <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-semibold bg-slate-800 text-slate-400 border border-slate-700">
                                                0 Students Completed
                                            </span>
                                        @endif

                                        <div class="p-1.5 rounded-lg bg-slate-800 border border-slate-700 text-slate-400 group-hover:text-white transition-all">
                                            <svg id="chevron-teacher-exam-{{ $exam->id }}" class="w-4 h-4 transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                                            </svg>
                                        </div>
                                    </div>
                                </div>

                                <!-- Collapsible Body with Completed Students Table -->
                                <div id="details-teacher-exam-{{ $exam->id }}" class="hidden px-6 py-5 bg-slate-950/80 border-t border-slate-800/80 space-y-4">
                                    <div class="flex items-center justify-between pb-2 border-b border-slate-800/60">
                                        <h5 class="text-xs font-bold uppercase tracking-wider text-slate-300 flex items-center space-x-2">
                                            <span>Students Completed This Exam ({{ $completedStudentCount }})</span>
                                        </h5>
                                        <div class="flex items-center space-x-3">
                                            <!-- <button type="button" onclick="event.stopPropagation(); openExamLeaderboardModal({{ $exam->id }}, this.getAttribute('data-exam-name'))" data-exam-name="{{ $exam->name }}" class="px-3 py-1 rounded-lg bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 border border-amber-500/40 text-xs font-bold transition-all inline-flex items-center space-x-1 cursor-pointer">
                                                <span>🏆 View all students Leaderboard</span>
                                            </button> -->
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
                                                    @foreach($examSubmissions as $studentId => $studentDetails)
                                                        @php
                                                            $studentObj = $studentDetails->first()->student;
                                                            $studentName = $studentObj?->name ?? $studentObj?->user?->name ?? 'Student #' . $studentId;
                                                            $studentClass = $studentObj?->standard?->name ?? 'N/A';
                                                            $isTextEntryExam = (int) $exam->type === 3;
                                                            $canEvaluate = $user && ($user->isAdmin() || (int) $exam->created_by === (int) $user->id);

                                                            $obtainedMarks = 0;
                                                            $detailsPayload = $studentDetails->map(function($d) use (&$obtainedMarks) {
                                                                $qMarks = $d->getQuestionMarks();
                                                                $isCorrect = $d->isCorrect();
                                                                $earnedMarks = $d->getEarnedMarks();
                                                                $obtainedMarks += $earnedMarks;

                                                                return [
                                                                    'id' => $d->id,
                                                                    'question_name' => $d->question?->name ?? 'N/A',
                                                                    'question_marks' => $qMarks,
                                                                    'selected_answer' => $d->getSelectedAnswerDisplay(),
                                                                    'is_correct' => $isCorrect,
                                                                    'is_partially_correct' => $d->isPartiallyCorrect(),
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
                                                                <button type="button" onclick="openStudentViewSubmissionModal({{ json_encode([
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
                                                                ]) }})" class="px-3 py-1.5 rounded-lg {{ $isTextEntryExam && $canEvaluate ? 'bg-emerald-600 hover:bg-emerald-500' : 'bg-indigo-600 hover:bg-indigo-500' }} text-white font-bold text-xs shadow-md transition-all inline-flex items-center space-x-1.5 cursor-pointer">
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
                            </div>
                        @endforeach
                    </div>
                @else
                    <div class="p-8 text-center text-slate-400">
                        <svg class="w-10 h-10 mx-auto mb-3 text-slate-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                        @if(request()->filled('exam_name') || request()->filled('exam_type') || request()->filled('type') || request()->filled('exam_syllabus_id') || request()->filled('exam_subject_id') || request()->filled('exam_chapter_id') || request()->filled('exam_topic_id'))
                            <p class="text-slate-300 font-medium text-sm">No exams match your search criteria.</p>
                            <p class="text-xs text-slate-500 mt-1">Try clearing or adjusting your filters to find exams.</p>
                            <a href="{{ route('dashboard') }}" class="inline-block mt-3 px-4 py-1.5 rounded-lg bg-indigo-600/20 text-indigo-300 border border-indigo-500/30 text-xs font-semibold hover:bg-indigo-600/30 transition-colors">Clear All Filters</a>
                        @else
                            <p class="text-sm font-medium">No exams found for your assigned classes.</p>
                        @endif
                    </div>
                @endif

                @if($teacherExams && method_exists($teacherExams, 'total'))
                    <div class="px-6 py-4 border-t border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs text-slate-400">
                        <div>
                            Showing <span class="font-semibold text-slate-200">{{ $teacherExams->firstItem() ?? 0 }}</span>
                            to <span class="font-semibold text-slate-200">{{ $teacherExams->lastItem() ?? 0 }}</span>
                            of <span class="font-semibold text-slate-200">{{ $teacherExams->total() }}</span> exam(s)
                            (10 per page)
                        </div>
                        @if($teacherExams->hasPages())
                            <div>
                                {{ $teacherExams->links() }}
                            </div>
                        @endif
                    </div>
                @endif
            </div>

            <script>
                function scrollToExamPerformanceReport(e) {
                    if (e) {
                        e.preventDefault();
                    }
                    const el = document.getElementById('teacherExamPerformanceReportContainer');
                    if (el) {
                        el.scrollIntoView({ behavior: 'smooth', block: 'start' });
                        el.classList.add('ring-2', 'ring-indigo-500', 'ring-offset-2', 'ring-offset-slate-950');
                        setTimeout(() => {
                            el.classList.remove('ring-2', 'ring-indigo-500', 'ring-offset-2', 'ring-offset-slate-950');
                        }, 2000);
                        if (window.history && window.history.replaceState) {
                            window.history.replaceState(null, '', '#teacherExamPerformanceReportContainer');
                        }
                    }
                }

                function scrollToTeacherStudentsDirectory(e) {
                    if (e) {
                        e.preventDefault();
                    }
                    const el = document.getElementById('teacherStudentsDirectoryContainer');
                    if (el) {
                        el.scrollIntoView({ behavior: 'smooth', block: 'start' });
                        el.classList.add('ring-2', 'ring-sky-500', 'ring-offset-2', 'ring-offset-slate-950');
                        setTimeout(() => {
                            el.classList.remove('ring-2', 'ring-sky-500', 'ring-offset-2', 'ring-offset-slate-950');
                        }, 2000);
                        if (window.history && window.history.replaceState) {
                            window.history.replaceState(null, '', '#teacherStudentsDirectoryContainer');
                        }
                    }
                }

                function toggleTeacherExamDetails(examId) {
                    const detailsBox = document.getElementById('details-teacher-exam-' + examId);
                    const chevron = document.getElementById('chevron-teacher-exam-' + examId);
                    if (detailsBox) {
                        detailsBox.classList.toggle('hidden');
                    }
                    if (chevron) {
                        chevron.classList.toggle('rotate-180');
                    }
                }
            </script>
            --}}
            <!-- Teacher Exams Listing Directory Table -->
            {{-- Commented Teacher Exams Listing Directory Table
            @if(isset($teacherExamList))
                <div id="teacherExamsListingContainer" class="bg-slate-900 border border-slate-800 rounded-2xl shadow-xl overflow-hidden">
                    <div class="px-6 py-5 border-b border-slate-800 flex items-center justify-between flex-wrap gap-4">
                        <div>
                            <h3 class="text-lg font-semibold text-white flex items-center space-x-2">
                                <svg class="w-5 h-5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
                                </svg>
                                <span>Exams Listing</span>
                                @if(request()->filled('exam_name') || request()->filled('exam_syllabus_id') || request()->filled('exam_subject_id') || request()->filled('exam_chapter_id') || request()->filled('exam_topic_id'))
                                    <span class="text-xs px-2.5 py-0.5 rounded-full bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 font-medium">Filtered</span>
                                @endif
                            </h3>
                            <p class="text-xs text-slate-400 mt-0.5">Directory of all exams created by you with curriculum tags, total marks, and questions</p>
                        </div>
                        <div class="flex items-center space-x-3">
                            <span class="text-xs text-slate-400 bg-slate-800 px-3 py-1 rounded-full border border-slate-700">
                                Total: {{ $teacherExamList->total() }} Exam(s)
                            </span>
                            <a href="{{ route('exams.index') }}" class="px-3.5 py-1.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold shadow-md transition-all inline-flex items-center space-x-1.5">
                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
                                <span>Manage All Exams</span>
                            </a>
                        </div>
                    </div>

                    <!-- Exam List Table -->
                    @if($teacherExamList->isNotEmpty())
                        <div class="overflow-x-auto">
                            <table class="w-full text-left text-sm text-slate-300">
                                <thead class="bg-slate-950/60 text-[11px] font-bold text-slate-400 uppercase tracking-wider border-b border-slate-800">
                                    <tr>
                                        <th class="px-6 py-4">Exam Info</th>
                                        <th class="px-6 py-4">Curriculum</th>
                                        <th class="px-6 py-4">Type & Duration</th>
                                        <th class="px-6 py-4">Marks & Questions</th>
                                        <th class="px-6 py-4">Status</th>
                                        <th class="px-6 py-4 text-right">Actions</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-slate-800/80">
                                    @foreach($teacherExamList as $tExam)
                                        @php
                                            $tMarks = $tExam->total_mark > 0 ? $tExam->total_mark : $tExam->questions->sum('marks');
                                        @endphp
                                        <tr class="hover:bg-slate-800/30 transition-colors">
                                            <td class="px-6 py-4">
                                                <div class="font-bold text-white text-sm hover:text-indigo-300 transition-colors">{{ $tExam->name }}</div>
                                                <div class="text-xs text-slate-400 mt-0.5">Created: <span class="text-slate-300">{{ $tExam->created_at?->format('M d, Y') ?? 'N/A' }}</span></div>
                                            </td>
                                            <td class="px-6 py-4 text-xs space-y-1">
                                                <div class="flex items-center space-x-1.5 flex-wrap">
                                                    @if($tExam->syllabus)
                                                        <span class="px-2 py-0.5 rounded bg-indigo-500/10 text-indigo-300 border border-indigo-500/20 font-medium">{{ $tExam->syllabus->name }}</span>
                                                    @endif
                                                    @if($tExam->subject)
                                                        <span class="px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-300 border border-emerald-500/20 font-medium">{{ $tExam->subject->name }}</span>
                                                    @endif
                                                </div>
                                                @if($tExam->chapter || $tExam->topic)
                                                    <div class="text-[11px] text-slate-400">
                                                        @if($tExam->chapter) <span>Ch: {{ $tExam->chapter->name }}</span> @endif
                                                        @if($tExam->topic) <span class="ml-1">• Top: {{ $tExam->topic->name }}</span> @endif
                                                    </div>
                                                @endif
                                            </td>
                                            <td class="px-6 py-4 text-xs">
                                                <span class="font-semibold text-slate-200">{{ $tExam->type === 1 ? 'Timed' : 'Practice' }}</span>
                                                @if($tExam->type === 1 && $tExam->duration)
                                                    <div class="text-[11px] text-slate-400 mt-0.5">{{ $tExam->duration }} mins</div>
                                                @endif
                                            </td>
                                            <td class="px-6 py-4 text-xs">
                                                <div class="font-bold text-amber-400">{{ $tMarks }} Marks</div>
                                                <div class="text-[11px] text-slate-400 mt-0.5">{{ $tExam->questions->count() }} Questions</div>
                                            </td>
                                            <td class="px-6 py-4 text-xs">
                                                @if($tExam->status === 1)
                                                    <span class="inline-flex items-center px-2 py-0.5 rounded-full text-[11px] font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Active</span>
                                                @else
                                                    <span class="inline-flex items-center px-2 py-0.5 rounded-full text-[11px] font-semibold bg-rose-500/10 text-rose-400 border border-rose-500/20">Inactive</span>
                                                @endif
                                            </td>
                                            <td class="px-6 py-4 text-right">
                                                <div class="inline-flex items-center space-x-2">
                                                    @if(($tExam->student_exam_details_count ?? 0) === 0 && ($isAdmin || (int)$tExam->created_by === (int)$user->id))
                                                        <button type="button" onclick="openDashboardEditExamModal({{ json_encode([
                                                            'id' => $tExam->id,
                                                            'name' => $tExam->name,
                                                            'type' => $tExam->type,
                                                            'duration' => $tExam->duration,
                                                            'status' => $tExam->status,
                                                            'syllabus_id' => $tExam->syllabus_id,
                                                            'standard_id' => $tExam->standard_id,
                                                            'subject_id' => $tExam->subject_id,
                                                            'chapter_id' => $tExam->chapter_id,
                                                            'topic_id' => $tExam->topic_id,
                                                            'standards' => $tExam->standards->pluck('id')->toArray(),
                                                            'action' => route('exams.update', $tExam->id),
                                                        ]) }})" class="inline-flex items-center space-x-1 px-2.5 py-1.5 rounded-lg bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 border border-amber-500/40 text-xs font-semibold transition-all cursor-pointer">
                                                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/></svg>
                                                            <span>Edit</span>
                                                        </button>
                                                    @endif
                                                    <a href="{{ route('exams.show', $tExam->id) }}" class="inline-flex items-center space-x-1 px-3 py-1.5 rounded-lg bg-indigo-600/20 hover:bg-indigo-600/40 text-indigo-300 border border-indigo-500/30 text-xs font-semibold transition-all">
                                                        <span>Manage Questions</span>
                                                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                                                    </a>
                                                </div>
                                            </td>
                                        </tr>
                                    @endforeach
                                </tbody>
                            </table>
                        </div>
                    @else
                        <div class="p-8 text-center text-slate-400">
                            <svg class="w-10 h-10 mx-auto mb-3 text-slate-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                            @if(request()->filled('exam_name') || request()->filled('exam_syllabus_id') || request()->filled('exam_subject_id') || request()->filled('exam_chapter_id') || request()->filled('exam_topic_id'))
                                <p class="text-slate-300 font-medium text-sm">No exams match your search criteria.</p>
                                <p class="text-xs text-slate-500 mt-1">Try clearing or adjusting your filters to find exams.</p>
                                <a href="{{ route('dashboard') }}" class="inline-block mt-3 px-4 py-1.5 rounded-lg bg-indigo-600/20 text-indigo-300 border border-indigo-500/30 text-xs font-semibold hover:bg-indigo-600/30 transition-colors">Clear All Filters</a>
                            @else
                                <p class="text-sm font-medium">No exams created yet. Click "Manage All Exams" or create one.</p>
                            @endif
                        </div>
                    @endif

                    @if($teacherExamList && method_exists($teacherExamList, 'total'))
                        <div class="px-6 py-4 border-t border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs text-slate-400">
                            <div>
                                Showing <span class="font-semibold text-slate-200">{{ $teacherExamList->firstItem() ?? 0 }}</span>
                                to <span class="font-semibold text-slate-200">{{ $teacherExamList->lastItem() ?? 0 }}</span>
                                of <span class="font-semibold text-slate-200">{{ $teacherExamList->total() }}</span> exam(s)
                                (10 per page)
                            </div>
                            @if($teacherExamList->hasPages())
                                <div>
                                    {{ $teacherExamList->links() }}
                                </div>
                            @endif
                        </div>
                    @endif
                </div>
            @endif
            --}}

            <!-- Students Directory Table (Teacher Linked Classes - Moved to /students) -->
            {{--
            <div id="teacherStudentsDirectoryContainer" class="bg-slate-900 border border-slate-800 rounded-2xl shadow-xl overflow-hidden scroll-mt-20 transition-all duration-500">
                <div class="px-6 py-5 border-b border-slate-800 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                    <div>
                        <h3 class="text-lg font-semibold text-white flex items-center space-x-2">
                            <svg class="w-5 h-5 text-sky-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"/>
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0112 20.055a11.952 11.952 0 01-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"/>
                            </svg>
                            <span>Students in My Classes</span>
                        </h3>
                        <p class="text-xs text-slate-400 mt-0.5">Displaying enrolled students linked to your assigned classes</p>
                    </div>

                    <div class="flex items-center space-x-2">
                        @if($user->standards->isNotEmpty())
                            <div class="flex flex-wrap gap-1 max-w-xs">
                                @foreach($user->standards as $std)
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

                <!-- Search & Class Filter Bar for Teacher -->
                <div class="px-3 py-3 sm:px-6 sm:py-4 bg-slate-950/40 border-b border-slate-800">
                    <form method="GET" action="{{ route('dashboard') }}" class="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-2 sm:gap-3">
                        <div class="flex flex-row items-center gap-2 w-full sm:w-auto">
                            <!-- Search by Name / Email -->
                            <div class="relative w-full sm:w-72">
                                <div class="absolute inset-y-0 left-0 pl-2.5 flex items-center pointer-events-none text-slate-500">
                                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                                    </svg>
                                </div>
                                <input type="text" name="search" value="{{ request('search') }}" placeholder="Search student name..." class="w-full pl-8 pr-2.5 py-1.5 rounded-lg sm:rounded-xl bg-slate-900 border border-slate-700 text-slate-100 placeholder-slate-500 text-xs focus:outline-none focus:ring-2 focus:ring-sky-500">
                            </div>

                            <!-- Filter by Class / Standard -->
                            <div class="w-44 sm:w-52 shrink-0">
                                <select name="standard_id" class="w-full px-2.5 py-1.5 rounded-lg sm:rounded-xl bg-slate-900 border border-slate-700 text-slate-100 text-xs focus:outline-none focus:ring-2 focus:ring-sky-500">
                                    <option value="">All Classes</option>
                                    @foreach($user->standards as $std)
                                        <option value="{{ $std->id }}" {{ request('standard_id') == $std->id ? 'selected' : '' }}>
                                            {{ $std->name }}
                                        </option>
                                    @endforeach
                                </select>
                            </div>
                        </div>

                        <div class="flex items-center space-x-2 shrink-0 justify-end mt-1 sm:mt-0">
                            <button type="submit" class="px-3.5 py-1.5 sm:px-4 sm:py-2 rounded-lg sm:rounded-xl bg-sky-600 hover:bg-sky-500 text-white font-semibold text-xs transition-all shadow-md shadow-sky-600/20 flex items-center space-x-1 cursor-pointer">
                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                                </svg>
                                <span>Filter</span>
                            </button>

                            @if(request()->filled('search') || request()->filled('standard_id'))
                                <a href="{{ route('dashboard') }}" class="px-3 py-1.5 sm:px-3.5 sm:py-2 rounded-lg sm:rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs border border-slate-700 transition-colors inline-flex items-center space-x-1">
                                    <svg class="w-3.5 h-3.5 text-rose-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                                    </svg>
                                    <span>Reset</span>
                                </a>
                            @endif
                        </div>
                    </form>
                </div>

                <div class="overflow-x-auto w-full">
                    @if($teacherStudents && $teacherStudents->count() > 0)
                        <table class="w-full text-left border-collapse text-sm">
                            <thead>
                                <tr class="bg-slate-950/60 border-b border-slate-800 text-slate-400 uppercase text-[11px] font-semibold tracking-wider">
                                    <th class="py-3 px-4 sm:py-3.5 sm:px-6">Student Name</th>
                                    <th class="py-3 px-4 sm:py-3.5 sm:px-6">Assigned Class</th>
                                    <th class="py-3 px-4 sm:py-3.5 sm:px-6 text-right">Action</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-slate-800/60 text-slate-300">
                                @foreach ($teacherStudents as $s)
                                    <tr class="hover:bg-slate-800/40 transition-colors">
                                        <td class="py-3 px-4 sm:py-4 sm:px-6 font-medium text-white flex items-center space-x-2.5 sm:space-x-3">
                                            <div class="w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-slate-800 border border-slate-700 text-sky-400 font-semibold flex items-center justify-center text-xs shrink-0">
                                                {{ strtoupper(substr($s->name, 0, 1)) }}
                                            </div>
                                            <div class="min-w-0">
                                                <span class="font-bold text-white block text-xs sm:text-sm truncate">{{ $s->name }}</span>
                                                <span class="text-[11px] sm:text-xs text-slate-400 font-mono truncate block">{{ $s->email }}</span>
                                            </div>
                                        </td>
                                        <td class="py-3 px-4 sm:py-4 sm:px-6">
                                            @php
                                                $stNames = $s->studentStandards ? $s->studentStandards->pluck('name') : collect();
                                                if ($s->student?->standard && ! $stNames->contains($s->student->standard->name)) {
                                                    $stNames->prepend($s->student->standard->name);
                                                }
                                            @endphp
                                            @if($stNames->isNotEmpty())
                                                <div class="flex flex-wrap gap-1">
                                                    @foreach($stNames as $stName)
                                                        <span class="inline-flex items-center px-2 py-0.5 sm:px-2.5 sm:py-1 rounded-full text-[11px] sm:text-xs font-semibold bg-sky-500/10 text-sky-300 border border-sky-500/20">
                                                            {{ $stName }}
                                                        </span>
                                                    @endforeach
                                                </div>
                                            @else
                                                <span class="text-xs text-slate-500 italic">Unassigned</span>
                                            @endif
                                        </td>
                                        <td class="py-3 px-4 sm:py-4 sm:px-6 text-right whitespace-nowrap space-x-1.5">
                                            <button type="button" onclick="openStudentPerformanceModal({{ $s->id }})" class="px-2.5 py-1 sm:px-3 sm:py-1.5 rounded-lg sm:rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-semibold text-xs transition-all shadow-md shadow-emerald-600/20 inline-flex items-center space-x-1 sm:space-x-1.5 cursor-pointer">
                                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>
                                                <span>Exams Performance</span>
                                            </button>
                                            <button type="button" onclick="openChatModal({{ $s->id }})" class="px-2.5 py-1 sm:px-3 sm:py-1.5 rounded-lg sm:rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-xs transition-all shadow-md shadow-indigo-600/20 inline-flex items-center space-x-1 sm:space-x-1.5 cursor-pointer">
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
                                            ]) }})" class="px-2.5 py-1 sm:px-3 sm:py-1.5 rounded-lg sm:rounded-xl bg-sky-600 hover:bg-sky-500 text-white font-semibold text-xs transition-all shadow-md shadow-sky-600/20 inline-flex items-center space-x-1 sm:space-x-1.5 cursor-pointer">
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
                        <div class="p-8 sm:p-12 text-center">
                            <div class="w-12 h-12 sm:w-16 sm:h-16 rounded-2xl bg-slate-800 border border-slate-700 text-slate-500 flex items-center justify-center mx-auto mb-3">
                                <svg class="w-6 h-6 sm:w-8 sm:h-8 text-sky-400/80" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
                                </svg>
                            </div>
                            @if(request()->filled('search') || request()->filled('standard_id'))
                                <h3 class="text-sm sm:text-base font-semibold text-slate-300">No Matching Students Found</h3>
                                <p class="mt-1 text-xs sm:text-sm text-slate-500 max-w-sm mx-auto">No students match your search query or selected class filter.</p>
                            @elseif($user->standards->isNotEmpty())
                                <h3 class="text-sm sm:text-base font-semibold text-slate-300">No Students Found in Assigned Classes</h3>
                                <p class="mt-1 text-xs sm:text-sm text-slate-500 max-w-sm mx-auto">No students are currently enrolled in your assigned classes.</p>
                            @else
                                <h3 class="text-sm sm:text-base font-semibold text-slate-300">No Classes Assigned</h3>
                                <p class="mt-1 text-xs sm:text-sm text-slate-500 max-w-sm mx-auto">Your teacher profile does not have any assigned class standards. Contact system admin to assign standards.</p>
                            @endif
                        </div>
                    @endif
                </div>

                @if($teacherStudents && method_exists($teacherStudents, 'hasPages') && $teacherStudents->hasPages())
                    <div class="px-6 py-4 border-t border-slate-800">
                        {{ $teacherStudents->links() }}
                    </div>
                @endif
            </div>
            --}}

            <!-- VIEW STUDENT DETAILS MODAL FOR TEACHER -->
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
                                <span class="text-[11px] font-semibold text-slate-400 uppercase tracking-wider block">Email Address</span>
                                <span id="view_student_modal_email" class="text-sm font-semibold text-indigo-300 mt-1 block break-all"></span>
                            </div>
                            <div class="bg-slate-950/60 p-3.5 rounded-xl border border-slate-800">
                                <span class="text-[11px] font-semibold text-slate-400 uppercase tracking-wider block">Mobile Number</span>
                                <span id="view_student_modal_mobile" class="text-sm font-semibold text-slate-200 mt-1 block"></span>
                            </div>
                            <div class="bg-slate-950/60 p-3.5 rounded-xl border border-slate-800">
                                <span class="text-[11px] font-semibold text-slate-400 uppercase tracking-wider block">Assigned Class</span>
                                <span id="view_student_modal_standard" class="text-sm font-bold text-sky-400 mt-1 block"></span>
                            </div>
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
                    currentSelectedStudentId = data.id || null;
                    document.getElementById('view_student_modal_title').textContent = (data.name || 'Student') + ' - Details';
                    document.getElementById('view_student_modal_full_name').textContent = data.name || '-';
                    document.getElementById('view_student_modal_email').textContent = data.email || '-';
                    document.getElementById('view_student_modal_mobile').textContent = data.mobile || 'N/A';
                    document.getElementById('view_student_modal_standard').textContent = data.standard || 'Unassigned';
                    document.getElementById('view_student_modal_school').textContent = data.school || 'N/A';
                    document.getElementById('view_student_modal_address').textContent = data.address || 'N/A';
                    
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
                    document.getElementById('viewStudentDetailsModal').classList.add('hidden');
                    if (currentSelectedStudentId) {
                        openChatModal(currentSelectedStudentId);
                    } else {
                        openChatModal();
                    }
                }
            </script>

            <!-- Profile Info Card -->
            <div class="bg-slate-900 border border-slate-800 rounded-2xl shadow-xl overflow-hidden">
                <div class="px-6 py-5 border-b border-slate-800 flex items-center justify-between">
                    <h3 class="text-lg font-semibold text-white">User Profile Details</h3>
                    <span class="text-xs text-slate-400 bg-slate-800 px-3 py-1 rounded-full border border-slate-700">Teacher</span>
                </div>

                <div class="p-6">
                    <dl class="grid grid-cols-1 sm:grid-cols-2 gap-6">
                        <div class="bg-slate-950/60 p-4 rounded-xl border border-slate-800/80">
                            <dt class="text-xs font-medium text-slate-400">Full Name</dt>
                            <dd class="mt-1 text-base font-semibold text-slate-100">{{ $user->name }}</dd>
                        </div>

                        <div class="bg-slate-950/60 p-4 rounded-xl border border-slate-800/80">
                            <dt class="text-xs font-medium text-slate-400">Email Address</dt>
                            <dd class="mt-1 text-base font-semibold text-indigo-300">{{ $user->email }}</dd>
                        </div>

                        <div class="bg-slate-950/60 p-4 rounded-xl border border-slate-800/80">
                            <dt class="text-xs font-medium text-slate-400">Address</dt>
                            <dd class="mt-1 text-sm font-medium text-slate-200">{{ $user->profile?->address ?? 'N/A' }}</dd>
                        </div>

                        <div class="bg-slate-950/60 p-4 rounded-xl border border-slate-800/80">
                            <dt class="text-xs font-medium text-slate-400">Assigned Standards</dt>
                            <dd class="mt-1 text-sm font-medium text-slate-200">
                                @if($user->standards->isNotEmpty())
                                    <div class="flex flex-wrap gap-1 mt-1">
                                        @foreach($user->standards as $std)
                                            <span class="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-indigo-500/10 text-indigo-300 border border-indigo-500/20">
                                                {{ $std->name }}
                                            </span>
                                        @endforeach
                                    </div>
                                @else
                                    <span class="text-slate-500">None assigned</span>
                                @endif
                            </dd>
                        </div>
                    </dl>
                </div>
            </div>

        @endif

        @if ($user->canAssignExams())
            <!-- Standards / Classes Directory Table for Teacher & Admin -->
            <div id="standardsDirectoryContainer" class="{{ (request()->filled('standards_page') || request()->filled('standards_search')) ? '' : 'hidden' }} bg-slate-900 border border-slate-800 rounded-2xl shadow-xl overflow-hidden mt-6">
                <div class="px-6 py-5 border-b border-slate-800 flex items-center justify-between flex-wrap gap-4">
                    <div>
                        <h3 class="text-lg font-semibold text-white flex items-center space-x-2">
                            <svg class="w-5 h-5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
                            </svg>
                            <span>Manage Standards</span>
                        </h3>
                        <p class="text-xs text-slate-400 mt-0.5">Manage standards created by you or assigned to you.</p>
                    </div>
                    <div class="flex items-center space-x-3 flex-wrap gap-2">
                        <form method="GET" action="{{ route('dashboard') }}" class="flex items-center space-x-2">
                            <input type="hidden" name="standards_page" value="1">
                            <div class="relative">
                                <input type="text" name="standards_search" value="{{ request('standards_search') }}" placeholder="Search standards..." class="w-40 sm:w-56 pl-8 pr-3 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 placeholder-slate-500 text-xs focus:outline-none focus:ring-2 focus:ring-emerald-500">
                                <svg class="w-3.5 h-3.5 text-slate-500 absolute left-2.5 top-2.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                            </div>
                            @if(request()->filled('standards_search'))
                                <a href="{{ route('dashboard') }}?standards_page=1" class="px-2.5 py-1.5 rounded-lg bg-slate-800 text-slate-300 hover:text-white text-xs font-semibold">Clear</a>
                            @endif
                        </form>
                        <button onclick="document.getElementById('createStandardModal').classList.remove('hidden')" class="px-3.5 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-semibold shadow-md transition-all inline-flex items-center space-x-1 cursor-pointer">
                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
                            <span>Add Standard</span>
                        </button>
                    </div>
                </div>

                <div class="overflow-x-auto">
                    <table class="w-full text-left border-collapse text-sm">
                        <thead>
                            <tr class="bg-slate-950/60 border-b border-slate-800 text-slate-400 uppercase text-[11px] font-semibold tracking-wider">
                                <th class="py-3.5 px-6">Standard Name</th>
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
                                        <div class="flex items-center space-x-2">
                                            <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                                            <span class="text-sm font-bold text-white">{{ $std->name }}</span>
                                        </div>
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
                                        @if($std->created_by === $user->id)
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
                                        @if ($isAdmin || $std->created_by === $user->id)
                                            <button onclick="openAssignStudentsModal({{ json_encode([
                                                'id' => $std->id,
                                                'name' => $std->name,
                                                'student_ids' => $std->students->pluck('id')->toArray(),
                                            ]) }})" class="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-semibold shadow transition-all inline-flex items-center space-x-1 cursor-pointer">
                                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z"/></svg>
                                                <span>Assign Students</span>
                                            </button>
                                        @endif
                                        @if ($isAdmin || $std->created_by === $user->id)
                                            <button onclick="openEditStandardModal({{ json_encode([
                                                'id' => $std->id,
                                                'name' => $std->name,
                                                'syllabus_id' => $std->syllabus_id,
                                            ]) }})" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-indigo-300 text-xs font-medium border border-slate-700 transition-colors inline-flex items-center space-x-1 cursor-pointer">
                                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/></svg>
                                                <span>Edit</span>
                                            </button>
                                            <form method="POST" action="{{ route('standards.destroy', $std->id) }}" class="inline-block" onsubmit="return confirm('Are you sure you want to delete this standard? This will unassign students and detach exams associated with it.');">
                                                @csrf
                                                @method('DELETE')
                                                <button type="submit" class="px-3 py-1.5 rounded-lg bg-rose-500/10 hover:bg-rose-500/20 text-rose-400 hover:text-rose-300 text-xs font-semibold border border-rose-500/20 transition-all inline-flex items-center space-x-1 cursor-pointer">
                                                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/></svg>
                                                    <span>Delete</span>
                                                </button>
                                            </form>
                                        @elseif(! ($user->standards->contains($std->id)))
                                            <span class="text-xs text-slate-500 italic font-medium px-2 py-1 rounded bg-slate-800/50 border border-slate-800">Admin Standard</span>
                                        @endif
                                    </td>
                                </tr>
                            @empty
                                <tr>
                                    <td colspan="4" class="py-8 text-center text-slate-500 text-xs">No standards found. Click "Add Standard" to create one.</td>
                                </tr>
                            @endforelse
                        </tbody>
                    </table>
                </div>

                @if($standards && method_exists($standards, 'hasPages') && $standards->hasPages())
                    <div class="px-6 py-4 border-t border-slate-800">
                        {{ $standards->links() }}
                    </div>
                @endif
            </div>
        @endif



        <script>
            let currentEvaluationData = null;

            function escapeExamHtml(str) {
                if (str === null || str === undefined) return '';
                const map = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' };
                return String(str).replace(/[&<>"']/g, m => map[m]);
            }

            function openStudentViewSubmissionModal(data) {
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
                                                 Evaluated (+${escapeExamHtml(earnedMarks)} / ${escapeExamHtml(d.question_marks)} Marks)
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
                                             Correct (+${escapeExamHtml(earnedMarks)} Marks)
                                           </span>`;
                        } else if (isPartial) {
                            cardBorderClass = 'border-l-4 border-l-amber-500 border-t border-r border-b border-slate-200 bg-white';
                            statusBadge = `<span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-black bg-amber-100 text-black border border-amber-300">
                                             <svg class="w-3.5 h-3.5 mr-1 text-black shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
                                             Partial (+${escapeExamHtml(earnedMarks)} Marks)
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
                                    <span class="text-black font-black text-sm sm:text-base ml-1">${escapeExamHtml(d.correct_answer)}</span>
                                </div>
                            `;
                        }

                        let matchPairsMarkup = '';
                        if (d.match_pairs && d.match_pairs.length > 0) {
                            matchPairsMarkup = `
                                <div class="mt-2 space-y-2">
                                    <div class="flex items-center justify-between pb-1 border-b border-slate-100">
                                        <span class="text-[10px] font-extrabold uppercase tracking-wider text-black">Matching Pairs Details (1 Mark per Match):</span>
                                        <span class="text-xs font-black text-black bg-slate-100 px-2.5 py-0.5 rounded-full border border-slate-200">${escapeExamHtml(earnedMarks)} / ${escapeExamHtml(d.question_marks)} Marks</span>
                                    </div>
                                    ${d.match_pairs.map(p => `
                                        <div class="p-2.5 rounded-xl border ${p.is_correct ? 'bg-emerald-50/90 border-emerald-300' : 'bg-rose-50/90 border-rose-300'} flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-xs">
                                            <div class="flex items-center space-x-2">
                                                <span class="w-5 h-5 rounded-md ${p.is_correct ? 'bg-emerald-600' : 'bg-rose-600'} text-white font-bold text-[10px] flex items-center justify-center shrink-0">
                                                    ${p.is_correct ? '✓' : '✕'}
                                                </span>
                                                <span class="font-bold text-black">${p.letter}. ${escapeExamHtml(p.left)}</span>
                                            </div>
                                            <div class="flex items-center space-x-2 pl-7 sm:pl-0 flex-wrap">
                                                <span class="text-black font-medium">Selected: <span class="font-extrabold ${p.is_correct ? 'text-emerald-950' : 'text-rose-950'}">${escapeExamHtml(p.student_match)}</span></span>
                                                ${!p.is_correct && p.correct_match ? `<span class="text-emerald-900 font-bold">→ Correct: <span class="font-black underline">${escapeExamHtml(p.correct_match)}</span></span>` : ''}
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
                                            <span class="text-[11px] font-black text-indigo-900 bg-white px-2 py-0.5 rounded border border-indigo-200">Max: ${escapeExamHtml(d.question_marks)} Marks</span>
                                        </div>
                                        <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 items-end">
                                            <div>
                                                <label class="block text-[10px] font-bold text-black uppercase mb-1">Marks (0 to ${escapeExamHtml(d.question_marks)}):</label>
                                                <input type="number" min="0" max="${escapeExamHtml(d.question_marks)}" step="1" value="${d.teacher_marks !== null && d.teacher_marks !== undefined ? escapeExamHtml(d.teacher_marks) : ''}" placeholder="0" class="eval-marks-input w-full px-3 py-1.5 rounded-lg border border-slate-300 text-sm font-bold text-black bg-white focus:ring-2 focus:ring-indigo-500 focus:outline-none" data-detail-id="${d.id}" data-max="${escapeExamHtml(d.question_marks)}">
                                            </div>
                                            <div class="sm:col-span-2">
                                                <label class="block text-[10px] font-bold text-black uppercase mb-1">Teacher Feedback (Optional):</label>
                                                <input type="text" value="${escapeExamHtml(d.teacher_feedback || '')}" placeholder="e.g. Accurate steps, clear working" class="eval-feedback-input w-full px-3 py-1.5 rounded-lg border border-slate-300 text-xs text-black bg-white focus:ring-2 focus:ring-indigo-500 focus:outline-none" data-detail-id="${d.id}">
                                            </div>
                                        </div>
                                    </div>
                                `;
                            } else if (d.teacher_feedback) {
                                evalBox = `
                                    <div class="mt-2.5 p-3 rounded-xl bg-indigo-50 border border-indigo-200 text-xs">
                                        <span class="text-black font-extrabold uppercase tracking-wider text-[11px]">Teacher Feedback:</span>
                                        <p class="text-black font-medium mt-1 leading-relaxed">${escapeExamHtml(d.teacher_feedback)}</p>
                                    </div>
                                `;
                            }

                            textEntrySectionMarkup = `
                                <div class="p-3.5 rounded-xl border bg-slate-50 border-slate-300 space-y-1.5">
                                    <div class="flex items-center justify-between">
                                        <span class="text-[10px] font-extrabold uppercase tracking-wider text-black block">Student's Written Response:</span>
                                        <span class="text-xs font-bold text-black">${escapeExamHtml(earnedMarks)} / ${escapeExamHtml(d.question_marks)} Marks</span>
                                    </div>
                                    <div class="text-sm font-medium text-black whitespace-pre-wrap leading-relaxed p-2.5 rounded-lg bg-white border border-slate-200 font-sans">${escapeExamHtml(d.student_text_answer || d.selected_answer || 'No answer submitted')}</div>
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
                                            <span class="text-black leading-relaxed whitespace-pre-line">${escapeExamHtml(d.hint)}</span>
                                        </div>
                                    ` : ''}
                                    ${d.solution ? `
                                        <div class="flex items-start space-x-2">
                                            <span class="px-1.5 py-0.5 rounded bg-emerald-100 text-emerald-950 border border-emerald-300 font-extrabold text-[10px] shrink-0 uppercase">Solution</span>
                                            <span class="text-black font-medium leading-relaxed whitespace-pre-line">${escapeExamHtml(d.solution)}</span>
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
                                                    <span class="text-sm sm:text-base font-black text-black">${escapeExamHtml(d.selected_answer)}</span>
                                                </div>
                                            </div>
                                            <span class="text-xs font-bold text-black">${escapeExamHtml(earnedMarks)} / ${escapeExamHtml(d.question_marks)} Marks</span>
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

                    alert('Marks and feedback have been successfully saved!');
                })
                .catch(err => {
                    if (btn) btn.disabled = false;
                    if (btnText) btnText.textContent = 'Save Marks & Feedback';
                    alert('Error saving evaluation: ' + err.message);
                });
            }

            function toggleStandardsDirectory() {
                const el = document.getElementById('standardsDirectoryContainer');
                if (el) {
                    el.classList.toggle('hidden');
                    if (!el.classList.contains('hidden')) {
                        el.scrollIntoView({ behavior: 'smooth', block: 'start' });
                    }
                }
            }

            function openCreateStandardModal() {
                const modal = document.getElementById('createStandardModal');
                if (modal) {
                    modal.classList.remove('hidden');
                }
            }

            function openEditStandardModal(data) {
                const url = '/standards/' + data.id;
                const form = document.getElementById('editStandardForm');
                if (form) form.action = url;
                const urlInput = document.getElementById('edit_standard_url');
                if (urlInput) urlInput.value = url;
                const nameInput = document.getElementById('edit_standard_name');
                if (nameInput) nameInput.value = data.name || '';
                const sylInput = document.getElementById('edit_standard_syllabus_id');
                if (sylInput && data.syllabus_id) {
                    sylInput.value = data.syllabus_id;
                }
                const modal = document.getElementById('editStandardModal');
                if (modal) modal.classList.remove('hidden');
            }

            // Dashboard Curriculum Cascading Filters Logic for Admin and Teacher
            const syllabusesDataDashboard = @json($syllabusesData ?? []);
            const subjectsDataDashboard = @json($subjectsData ?? []);

            function handleCurriculumSyllabusChange(sylId, subjectSelectId, chapterSelectId, topicSelectId) {
                const subjectSelect = document.getElementById(subjectSelectId);
                const chapterSelect = document.getElementById(chapterSelectId);
                const topicSelect = document.getElementById(topicSelectId);

                if (subjectSelect) {
                    subjectSelect.innerHTML = '<option value="">All Subjects</option>';
                    let subjectsToShow = [];
                    if (sylId) {
                        const syl = syllabusesDataDashboard.find(s => String(s.id) === String(sylId));
                        if (syl && syl.subjects) {
                            subjectsToShow = syl.subjects;
                        }
                    } else {
                        subjectsToShow = subjectsDataDashboard;
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

            function handleCurriculumSubjectChange(subjId, chapterSelectId, topicSelectId) {
                const chapterSelect = document.getElementById(chapterSelectId);
                const topicSelect = document.getElementById(topicSelectId);

                if (chapterSelect) {
                    chapterSelect.innerHTML = '<option value="">All Chapters</option>';
                    if (subjId) {
                        const subj = subjectsDataDashboard.find(s => String(s.id) === String(subjId));
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

            function handleCurriculumChapterChange(subjId, chId, topicSelectId) {
                const topicSelect = document.getElementById(topicSelectId);
                if (topicSelect) {
                    topicSelect.innerHTML = '<option value="">All Topics</option>';
                    if (subjId && chId) {
                        const subj = subjectsDataDashboard.find(s => String(s.id) === String(subjId));
                        if (subj && subj.chapters) {
                            const ch = subj.chapters.find(c => String(c.id) === String(chId));
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

            function onAdminFilterSyllabusChange() {
                const sId = document.getElementById('admin_filter_syllabus')?.value || '';
                handleCurriculumSyllabusChange(sId, 'admin_filter_subject', 'admin_filter_chapter', 'admin_filter_topic');
            }
            function onAdminFilterSubjectChange() {
                const subId = document.getElementById('admin_filter_subject')?.value || '';
                handleCurriculumSubjectChange(subId, 'admin_filter_chapter', 'admin_filter_topic');
            }
            function onAdminFilterChapterChange() {
                const subId = document.getElementById('admin_filter_subject')?.value || '';
                const chId = document.getElementById('admin_filter_chapter')?.value || '';
                handleCurriculumChapterChange(subId, chId, 'admin_filter_topic');
            }

            function onTeacherFilterSyllabusChange() {
                const sId = document.getElementById('teacher_filter_syllabus')?.value || '';
                handleCurriculumSyllabusChange(sId, 'teacher_filter_subject', 'teacher_filter_chapter', 'teacher_filter_topic');
            }
            function onTeacherFilterSubjectChange() {
                const subId = document.getElementById('teacher_filter_subject')?.value || '';
                handleCurriculumSubjectChange(subId, 'teacher_filter_chapter', 'teacher_filter_topic');
            }
            function onTeacherFilterChapterChange() {
                const subId = document.getElementById('teacher_filter_subject')?.value || '';
                const chId = document.getElementById('teacher_filter_chapter')?.value || '';
                handleCurriculumChapterChange(subId, chId, 'teacher_filter_topic');
            }

            document.addEventListener('DOMContentLoaded', () => {
                const curExamSyl = "{{ request('exam_syllabus_id') }}";
                const curExamSubj = "{{ request('exam_subject_id') }}";
                const curExamCh = "{{ request('exam_chapter_id') }}";
                const curExamTp = "{{ request('exam_topic_id') }}";

                ['admin', 'teacher'].forEach(prefix => {
                    const sylEl = document.getElementById(prefix + '_filter_syllabus');
                    if (sylEl && curExamSyl) {
                        if (prefix === 'admin') onAdminFilterSyllabusChange();
                        if (prefix === 'teacher') onTeacherFilterSyllabusChange();

                        const subjEl = document.getElementById(prefix + '_filter_subject');
                        if (subjEl && curExamSubj) {
                            subjEl.value = curExamSubj;
                            if (prefix === 'admin') onAdminFilterSubjectChange();
                            if (prefix === 'teacher') onTeacherFilterSubjectChange();

                            const chEl = document.getElementById(prefix + '_filter_chapter');
                            if (chEl && curExamCh) {
                                chEl.value = curExamCh;
                                if (prefix === 'admin') onAdminFilterChapterChange();
                                if (prefix === 'teacher') onTeacherFilterChapterChange();

                                const tpEl = document.getElementById(prefix + '_filter_topic');
                                if (tpEl && curExamTp) {
                                    tpEl.value = curExamTp;
                                }
                            }
                        }
                    } else if (sylEl && curExamSubj) {
                        if (prefix === 'admin') onAdminFilterSubjectChange();
                        if (prefix === 'teacher') onTeacherFilterSubjectChange();

                        const chEl = document.getElementById(prefix + '_filter_chapter');
                        if (chEl && curExamCh) {
                            chEl.value = curExamCh;
                            if (prefix === 'admin') onAdminFilterChapterChange();
                            if (prefix === 'teacher') onTeacherFilterChapterChange();

                            const tpEl = document.getElementById(prefix + '_filter_topic');
                            if (tpEl && curExamTp) {
                                tpEl.value = curExamTp;
                            }
                        }
                    }
                });
            });

            function openDashboardEditExamModal(data) {
                const actionUrl = data.action || ('/exams/' + data.id);
                const form = document.getElementById('dashboardEditExamForm');
                if (form) form.action = actionUrl;

                const actionInput = document.getElementById('dashboard_edit_exam_action_url');
                if (actionInput) actionInput.value = actionUrl;

                const nameInput = document.getElementById('dashboard_edit_exam_name');
                if (nameInput) nameInput.value = data.name || '';

                const typeSelect = document.getElementById('dashboard_edit_exam_type');
                if (typeSelect) {
                    typeSelect.value = data.type !== undefined ? data.type : 1;
                    toggleDashboardEditExamDuration(typeSelect.value);
                }

                const durationInput = document.getElementById('dashboard_edit_exam_duration');
                if (durationInput) durationInput.value = data.duration || 60;

                const statusSelect = document.getElementById('dashboard_edit_exam_status');
                if (statusSelect) statusSelect.value = data.status !== undefined ? data.status : 1;

                // Syllabus
                const sylSelect = document.getElementById('dashboard_edit_exam_syllabus');
                if (sylSelect) sylSelect.value = data.syllabus_id || '';

                // Standard / Class
                const stdSelect = document.getElementById('dashboard_edit_exam_standard');
                if (stdSelect) stdSelect.value = data.standard_id || '';

                // Populate Subjects, Chapters, Topics
                populateDashboardEditExamSubjects(data.syllabus_id, data.subject_id);
                populateDashboardEditExamChapters(data.subject_id, data.chapter_id);
                populateDashboardEditExamTopics(data.subject_id, data.chapter_id, data.topic_id);

                // Pre-check assigned standards checkboxes
                const assignedStdIds = (data.standards || []).map(id => parseInt(id));
                document.querySelectorAll('.dashboard-edit-std-checkbox').forEach(cb => {
                    cb.checked = assignedStdIds.includes(parseInt(cb.value));
                });

                document.getElementById('dashboardEditExamModal').classList.remove('hidden');
            }

            function closeDashboardEditExamModal() {
                document.getElementById('dashboardEditExamModal').classList.add('hidden');
            }

            function toggleDashboardEditExamDuration(typeVal) {
                const wrapper = document.getElementById('dashboard_edit_exam_duration_wrapper');
                const input = document.getElementById('dashboard_edit_exam_duration');
                if (wrapper) {
                    if (parseInt(typeVal) === 1) {
                        wrapper.classList.remove('hidden');
                        if (input) input.required = true;
                    } else {
                        wrapper.classList.add('hidden');
                        if (input) input.required = false;
                    }
                }
            }

            function populateDashboardEditExamSubjects(sylId, selectedSubjId) {
                const subjectSelect = document.getElementById('dashboard_edit_exam_subject');
                if (!subjectSelect) return;
                subjectSelect.innerHTML = '<option value="">Select Subject</option>';

                let subjectsToShow = [];
                if (sylId) {
                    const syl = syllabusesDataDashboard.find(s => String(s.id) === String(sylId));
                    if (syl && syl.subjects) {
                        subjectsToShow = syl.subjects;
                    }
                } else {
                    subjectsToShow = subjectsDataDashboard;
                }

                subjectsToShow.forEach(subj => {
                    const opt = document.createElement('option');
                    opt.value = subj.id;
                    opt.textContent = subj.name;
                    if (selectedSubjId && String(subj.id) === String(selectedSubjId)) {
                        opt.selected = true;
                    }
                    subjectSelect.appendChild(opt);
                });
            }

            function populateDashboardEditExamChapters(subjId, selectedChId) {
                const chapterSelect = document.getElementById('dashboard_edit_exam_chapter');
                if (!chapterSelect) return;
                chapterSelect.innerHTML = '<option value="">Select Chapter</option>';

                if (subjId) {
                    const subj = subjectsDataDashboard.find(s => String(s.id) === String(subjId));
                    if (subj && subj.chapters) {
                        subj.chapters.forEach(ch => {
                            const opt = document.createElement('option');
                            opt.value = ch.id;
                            opt.textContent = ch.name;
                            if (selectedChId && String(ch.id) === String(selectedChId)) {
                                opt.selected = true;
                            }
                            chapterSelect.appendChild(opt);
                        });
                    }
                }
            }

            function populateDashboardEditExamTopics(subjId, chId, selectedTopicId) {
                const topicSelect = document.getElementById('dashboard_edit_exam_topic');
                if (!topicSelect) return;
                topicSelect.innerHTML = '<option value="">Select Topic</option>';

                if (subjId && chId) {
                    const subj = subjectsDataDashboard.find(s => String(s.id) === String(subjId));
                    if (subj && subj.chapters) {
                        const ch = subj.chapters.find(c => String(c.id) === String(chId));
                        if (ch && ch.topics) {
                            ch.topics.forEach(tp => {
                                const opt = document.createElement('option');
                                opt.value = tp.id;
                                opt.textContent = tp.name;
                                if (selectedTopicId && String(tp.id) === String(selectedTopicId)) {
                                    opt.selected = true;
                                }
                                topicSelect.appendChild(opt);
                            });
                        }
                    }
                }
            }

            function onDashboardEditExamSyllabusChange() {
                const sylId = document.getElementById('dashboard_edit_exam_syllabus')?.value || '';
                populateDashboardEditExamSubjects(sylId, '');
                const chapterSelect = document.getElementById('dashboard_edit_exam_chapter');
                const topicSelect = document.getElementById('dashboard_edit_exam_topic');
                if (chapterSelect) chapterSelect.innerHTML = '<option value="">Select Chapter</option>';
                if (topicSelect) topicSelect.innerHTML = '<option value="">Select Topic</option>';
            }

            function onDashboardEditExamSubjectChange() {
                const subjId = document.getElementById('dashboard_edit_exam_subject')?.value || '';
                populateDashboardEditExamChapters(subjId, '');
                const topicSelect = document.getElementById('dashboard_edit_exam_topic');
                if (topicSelect) topicSelect.innerHTML = '<option value="">Select Topic</option>';
            }

            function onDashboardEditExamChapterChange() {
                const subjId = document.getElementById('dashboard_edit_exam_subject')?.value || '';
                const chId = document.getElementById('dashboard_edit_exam_chapter')?.value || '';
                populateDashboardEditExamTopics(subjId, chId, '');
            }
        </script>

        @if ($user->canAssignExams())
            <!-- CREATE STANDARD MODAL -->
            @php
                $isCreateStandardModalOpen = $errors->has('name') && old('_standard_mode') === 'create';
            @endphp
            <div id="createStandardModal" class="{{ $isCreateStandardModalOpen ? '' : 'hidden' }} fixed inset-0 z-50 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4 overflow-y-auto">
                <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-lg overflow-hidden shadow-2xl my-8">
                    <div class="px-6 py-4 border-b border-slate-800 flex items-center justify-between bg-slate-950/50">
                        <h3 class="text-lg font-bold text-white flex items-center space-x-2">
                            <svg class="w-5 h-5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
                            <span>Add New Standard / Class</span>
                        </h3>
                        <button onclick="document.getElementById('createStandardModal').classList.add('hidden')" class="text-slate-400 hover:text-white transition-colors cursor-pointer">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                        </button>
                    </div>

                    <form method="POST" action="{{ route('standards.store') }}" class="p-6 space-y-4">
                        @csrf
                        <input type="hidden" name="_standard_mode" value="create">

                        <div>
                            <label for="create_standard_name" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Standard / Class Name <span class="text-red-400">*</span></label>
                            <input type="text" id="create_standard_name" name="name" required value="{{ old('name') }}" placeholder="e.g. Class 10 - Science" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-emerald-500 text-sm @error('name') border-red-500 focus:ring-red-500 @enderror">
                            @error('name')
                                <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                            @enderror
                        </div>

                        <div>
                            <label for="create_standard_syllabus_id" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Syllabus</label>
                            <select id="create_standard_syllabus_id" name="syllabus_id" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-emerald-500 text-sm">
                                @foreach($syllabi ?? [] as $syl)
                                    <option value="{{ data_get($syl, 'id') }}">{{ data_get($syl, 'name') }}</option>
                                @endforeach
                            </select>
                        </div>

                        <div class="pt-4 flex justify-end space-x-3 border-t border-slate-800">
                            <button type="button" onclick="document.getElementById('createStandardModal').classList.add('hidden')" class="px-4 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-sm font-medium transition-colors cursor-pointer">Cancel</button>
                            <button type="submit" class="px-5 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-sm font-semibold shadow-lg shadow-emerald-600/30 transition-all cursor-pointer">Create Standard</button>
                        </div>
                    </form>
                </div>
            </div>

            <!-- EDIT STANDARD MODAL -->
            @php
                $isEditStandardModalOpen = $errors->has('name') && old('_standard_mode') === 'edit';
            @endphp
            <div id="editStandardModal" class="{{ $isEditStandardModalOpen ? '' : 'hidden' }} fixed inset-0 z-50 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4 overflow-y-auto">
                <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-lg overflow-hidden shadow-2xl my-8">
                    <div class="px-6 py-4 border-b border-slate-800 flex items-center justify-between bg-slate-950/50">
                        <h3 class="text-lg font-bold text-white flex items-center space-x-2">
                            <svg class="w-5 h-5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/></svg>
                            <span>Edit Standard / Class</span>
                        </h3>
                        <button onclick="document.getElementById('editStandardModal').classList.add('hidden')" class="text-slate-400 hover:text-white transition-colors cursor-pointer">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                        </button>
                    </div>

                    <form id="editStandardForm" method="POST" action="{{ old('_edit_standard_url', '') }}" class="p-6 space-y-4">
                        @csrf
                        @method('PUT')
                        <input type="hidden" name="_standard_mode" value="edit">
                        <input type="hidden" id="edit_standard_url" name="_edit_standard_url" value="{{ old('_edit_standard_url', '') }}">

                        <div>
                            <label for="edit_standard_name" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Standard / Class Name <span class="text-red-400">*</span></label>
                            <input type="text" id="edit_standard_name" name="name" required value="{{ old('name') }}" placeholder="e.g. Class 10 - Science" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('name') border-red-500 focus:ring-red-500 @enderror">
                            @error('name')
                                <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                            @enderror
                        </div>

                        <div>
                            <label for="edit_standard_syllabus_id" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Syllabus</label>
                            <select id="edit_standard_syllabus_id" name="syllabus_id" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm">
                                @foreach($syllabi ?? [] as $syl)
                                    <option value="{{ data_get($syl, 'id') }}">{{ data_get($syl, 'name') }}</option>
                                @endforeach
                            </select>
                        </div>

                        <div class="pt-4 flex justify-end space-x-3 border-t border-slate-800">
                            <button type="button" onclick="document.getElementById('editStandardModal').classList.add('hidden')" class="px-4 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-sm font-medium transition-colors cursor-pointer">Cancel</button>
                            <button type="submit" class="px-5 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-semibold shadow-lg shadow-indigo-600/30 transition-all cursor-pointer">Update Standard</button>
                        </div>
                    </form>
                </div>
            </div>

            <!-- BULK ASSIGN STUDENTS TO STANDARD MODAL -->
            <div id="assignStudentsModal" class="hidden fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4 overflow-y-auto">
                <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-2xl overflow-hidden shadow-2xl my-8 flex flex-col max-h-[85vh]">
                    <div class="px-6 py-4 border-b border-slate-800 flex items-center justify-between bg-slate-950/60 shrink-0">
                        <div class="flex items-center space-x-3">
                            <div class="w-9 h-9 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 font-bold flex items-center justify-center text-sm">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z"/></svg>
                            </div>
                            <div>
                                <h3 id="assign_modal_standard_title" class="text-base font-extrabold text-white">Assign Students to Class</h3>
                                <p class="text-xs text-slate-400">Select students to enroll in this class standard (Max 100)</p>
                            </div>
                        </div>
                        <button type="button" onclick="closeAssignStudentsModal()" class="text-slate-400 hover:text-white transition-colors cursor-pointer p-1">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                        </button>
                    </div>

                    <form id="assignStudentsForm" method="POST" action="" class="flex flex-col flex-1 overflow-hidden">
                        @csrf
                        <input type="hidden" name="_assign_mode" value="bulk">

                        <div class="p-4 bg-slate-950/40 border-b border-slate-800 flex items-center justify-between gap-3 shrink-0">
                            <div class="relative flex-1">
                                <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-500">
                                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                                </div>
                                <input type="text" id="assign_student_search" onkeyup="filterAssignStudentsList()" placeholder="Filter students by name or email..." class="w-full pl-9 pr-3 py-2 rounded-xl bg-slate-900 border border-slate-700 text-slate-100 placeholder-slate-500 text-xs focus:outline-none focus:ring-2 focus:ring-emerald-500">
                            </div>
                            <div class="text-xs text-slate-400 shrink-0 font-medium">
                                Selected: <span id="assign_selected_count" class="text-emerald-400 font-bold">0</span> / <span id="assign_total_students_count">0</span>
                            </div>
                        </div>

                        <!-- 10-Students Pagination Controls -->
                        <div class="px-4 py-2.5 bg-slate-950/60 border-b border-slate-800/80 flex flex-wrap items-center justify-between gap-2 text-xs shrink-0">
                            <span class="text-slate-400 font-medium" id="assign_pagination_info">
                                Showing 1-10 of 0 students
                            </span>
                            <div class="flex items-center space-x-1.5 overflow-x-auto py-0.5">
                                <button type="button" id="assign_prev_btn" onclick="changeAssignPage(-1)" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 disabled:opacity-40 disabled:cursor-not-allowed text-slate-200 font-semibold transition-colors cursor-pointer inline-flex items-center space-x-1">
                                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
                                    <span>Prev</span>
                                </button>
                                <div id="assign_page_buttons" class="flex items-center space-x-1"></div>
                                <button type="button" id="assign_next_btn" onclick="changeAssignPage(1)" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 disabled:opacity-40 disabled:cursor-not-allowed text-slate-200 font-semibold transition-colors cursor-pointer inline-flex items-center space-x-1">
                                    <span>Next</span>
                                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                                </button>
                            </div>
                        </div>

                        <div class="p-4 space-y-2 overflow-y-auto flex-1 bg-slate-950/20" id="assign_students_list">
                            @forelse($allStudents ?? [] as $stUser)
                                @php
                                    $stId = data_get($stUser, 'id');
                                    $stName = data_get($stUser, 'name', '');
                                    $stEmail = data_get($stUser, 'email', '');
                                    $stStandardName = data_get($stUser, 'student.standard.name', 'Unassigned');
                                    $stStandardId = data_get($stUser, 'student.standard_id');
                                @endphp
                                <label class="assign-student-item flex items-center justify-between p-3 rounded-xl bg-slate-900 border border-slate-800 hover:border-slate-700 transition-colors cursor-pointer" data-name="{{ strtolower($stName) }}" data-email="{{ strtolower($stEmail) }}">
                                    <div class="flex items-center space-x-3">
                                        <input type="checkbox" name="student_ids[]" value="{{ $stId }}" data-std-id="{{ $stStandardId }}" onchange="updateAssignSelectedCount()" class="assign-student-checkbox w-4 h-4 rounded border-slate-700 bg-slate-950 text-emerald-600 focus:ring-emerald-500 focus:ring-offset-slate-900">
                                        <div>
                                            <span class="text-sm font-bold text-white block">{{ $stName }}</span>
                                            <span class="text-xs text-slate-400 font-mono">{{ $stEmail }}</span>
                                        </div>
                                    </div>
                                    <span class="px-2.5 py-1 rounded-full text-[11px] font-semibold {{ $stStandardId ? 'bg-indigo-500/10 text-indigo-300 border border-indigo-500/20' : 'bg-slate-800 text-slate-400 border border-slate-700' }}">
                                        {{ $stStandardName }}
                                    </span>
                                </label>
                            @empty
                                <div class="p-6 text-center text-slate-500 text-xs">No student accounts found.</div>
                            @endforelse
                        </div>

                        <div class="px-6 py-3.5 bg-slate-950/80 border-t border-slate-800 flex items-center justify-between shrink-0">
                            <span class="text-xs text-slate-400">Class limit: 100 students</span>
                            <div class="flex items-center space-x-3">
                                <button type="button" onclick="closeAssignStudentsModal()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold transition-colors cursor-pointer">Cancel</button>
                                <button type="submit" class="px-5 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold shadow-lg shadow-emerald-600/30 transition-all cursor-pointer">Save Student Assignments</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>

            <!-- SINGLE STUDENT ASSIGNMENT MODAL -->
            <div id="assignSingleStudentModal" class="hidden fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4 overflow-y-auto">
                <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-md overflow-hidden shadow-2xl my-8">
                    <div class="px-6 py-4 border-b border-slate-800 flex items-center justify-between bg-slate-950/60">
                        <div class="flex items-center space-x-3">
                            <div class="w-9 h-9 rounded-xl bg-indigo-500/10 border border-indigo-500/30 text-indigo-400 font-bold flex items-center justify-center text-sm">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>
                            </div>
                            <div>
                                <h3 id="single_student_modal_title" class="text-base font-extrabold text-white">Assign Student to Class</h3>
                                <p class="text-xs text-slate-400">Select a class standard created by or assigned to you</p>
                            </div>
                        </div>
                        <button type="button" onclick="document.getElementById('assignSingleStudentModal').classList.add('hidden')" class="text-slate-400 hover:text-white transition-colors cursor-pointer p-1">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                        </button>
                    </div>

                    <form id="assignSingleStudentForm" method="POST" action="" class="p-6 space-y-4">
                        @csrf
                        <input type="hidden" id="single_student_id" name="student_id" value="">

                        <div>
                            <label for="single_student_select_standard" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1.5">Select Class Standard <span class="text-red-400">*</span></label>
                            <select id="single_student_select_standard" required class="w-full px-3.5 py-2.5 rounded-xl bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm">
                                <option value="">-- Choose Class Standard --</option>
                                @foreach($allStandardsForSelect ?? $standards as $std)
                                    @if($isAdmin || $std->created_by === $user->id)
                                        <option value="{{ $std->id }}">{{ $std->name }}</option>
                                    @endif
                                @endforeach
                            </select>
                        </div>

                        <div class="pt-4 flex justify-end space-x-3 border-t border-slate-800">
                            <button type="button" onclick="document.getElementById('assignSingleStudentModal').classList.add('hidden')" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-sm font-medium transition-colors cursor-pointer">Cancel</button>
                            <button type="submit" class="px-5 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-semibold shadow-lg shadow-indigo-600/30 transition-all cursor-pointer">Assign to Selected Class</button>
                        </div>
                    </form>
                </div>
            </div>

            <script>
                window.assignModalCurrentPage = 1;
                window.ASSIGN_MODAL_PER_PAGE = 10;

                window.closeAssignStudentsModal = function() {
                    const modal = document.getElementById('assignStudentsModal');
                    if (modal) {
                        modal.classList.add('hidden');
                        modal.style.display = 'none';
                    }
                };

                window.openAssignStudentsModal = function(data) {
                    const form = document.getElementById('assignStudentsForm');
                    if (form) {
                        form.action = '/standards/' + data.id + '/assign-students';
                    }
                    const title = document.getElementById('assign_modal_standard_title');
                    if (title) {
                        title.textContent = 'Assign Students to ' + (data.name || 'Class');
                    }

                    const checkboxes = document.querySelectorAll('.assign-student-checkbox');
                    const studentIds = (data.student_ids || []).map(id => parseInt(id));
                    checkboxes.forEach(cb => {
                        const val = parseInt(cb.value);
                        cb.checked = studentIds.includes(val);
                    });

                    if (typeof window.updateAssignSelectedCount === 'function') {
                        window.updateAssignSelectedCount();
                    }
                    const searchInput = document.getElementById('assign_student_search');
                    if (searchInput) {
                        searchInput.value = '';
                    }

                    window.assignModalCurrentPage = 1;

                    const modal = document.getElementById('assignStudentsModal');
                    if (modal) {
                        modal.classList.remove('hidden');
                        modal.style.display = 'flex';
                    }

                    window.filterAssignStudentsList();
                };

                window.setAssignPage = function(page) {
                    window.assignModalCurrentPage = page;
                    window.filterAssignStudentsList();
                };

                window.changeAssignPage = function(delta) {
                    window.assignModalCurrentPage += delta;
                    window.filterAssignStudentsList();
                };

                window.filterAssignStudentsList = function() {
                    const searchInput = document.getElementById('assign_student_search');
                    const search = (searchInput ? searchInput.value : '').toLowerCase();
                    const items = Array.from(document.querySelectorAll('.assign-student-item'));

                    const matchingItems = items.filter(item => {
                        const name = (item.getAttribute('data-name') || '').toLowerCase();
                        const email = (item.getAttribute('data-email') || '').toLowerCase();
                        return name.includes(search) || email.includes(search);
                    });

                    const totalMatching = matchingItems.length;
                    const totalPages = Math.max(1, Math.ceil(totalMatching / window.ASSIGN_MODAL_PER_PAGE));

                    if (window.assignModalCurrentPage > totalPages) {
                        window.assignModalCurrentPage = totalPages;
                    }
                    if (window.assignModalCurrentPage < 1) {
                        window.assignModalCurrentPage = 1;
                    }

                    const startIndex = (window.assignModalCurrentPage - 1) * window.ASSIGN_MODAL_PER_PAGE;
                    const endIndex = startIndex + window.ASSIGN_MODAL_PER_PAGE;

                    items.forEach(item => {
                        const matchIndex = matchingItems.indexOf(item);
                        if (matchIndex >= startIndex && matchIndex < endIndex) {
                            item.classList.remove('hidden');
                            item.style.display = 'flex';
                        } else {
                            item.classList.add('hidden');
                            item.style.display = 'none';
                        }
                    });

                    const paginationInfoEl = document.getElementById('assign_pagination_info');
                    const pageBtnsContainer = document.getElementById('assign_page_buttons');
                    const prevBtn = document.getElementById('assign_prev_btn');
                    const nextBtn = document.getElementById('assign_next_btn');

                    if (totalMatching === 0) {
                        if (paginationInfoEl) paginationInfoEl.textContent = 'Showing 0-0 of 0 students';
                        if (pageBtnsContainer) pageBtnsContainer.innerHTML = '';
                        if (prevBtn) prevBtn.disabled = true;
                        if (nextBtn) nextBtn.disabled = true;
                    } else {
                        const displayStart = startIndex + 1;
                        const displayEnd = Math.min(endIndex, totalMatching);
                        if (paginationInfoEl) paginationInfoEl.textContent = `Showing ${displayStart}-${displayEnd} of ${totalMatching} students`;

                        if (prevBtn) prevBtn.disabled = window.assignModalCurrentPage <= 1;
                        if (nextBtn) nextBtn.disabled = window.assignModalCurrentPage >= totalPages;

                        if (pageBtnsContainer) {
                            let btnsHtml = '';
                            for (let p = 1; p <= totalPages; p++) {
                                const isActive = p === window.assignModalCurrentPage;
                                const activeClasses = isActive
                                    ? 'bg-emerald-600 text-white font-bold shadow-md shadow-emerald-600/30'
                                    : 'bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold';
                                btnsHtml += `<button type="button" onclick="setAssignPage(${p})" class="px-2.5 py-1 rounded-lg text-xs transition-colors cursor-pointer ${activeClasses}">${p}</button>`;
                            }
                            pageBtnsContainer.innerHTML = btnsHtml;
                        }
                    }
                };

                function updateAssignSelectedCount() {
                    const checked = document.querySelectorAll('.assign-student-checkbox:checked').length;
                    const total = document.querySelectorAll('.assign-student-checkbox').length;
                    const selectedCountEl = document.getElementById('assign_selected_count');
                    const totalCountEl = document.getElementById('assign_total_students_count');
                    if (selectedCountEl) selectedCountEl.textContent = checked;
                    if (totalCountEl) totalCountEl.textContent = total;
                }

                function openAssignSingleStudentModal(data) {
                    const form = document.getElementById('assignSingleStudentForm');
                    const select = document.getElementById('single_student_select_standard');
                    const studentIdInput = document.getElementById('single_student_id');
                    const title = document.getElementById('single_student_modal_title');

                    if (studentIdInput) studentIdInput.value = data.id || '';
                    if (title) title.textContent = 'Assign ' + (data.name || 'Student') + ' to Class';

                    if (select) {
                        select.value = data.standard_id || '';
                    }

                    if (form) {
                        form.onsubmit = function(e) {
                            e.preventDefault();
                            const stdId = select.value;
                            if (!stdId) {
                                alert('Please select a class standard.');
                                return false;
                            }
                            form.action = '/standards/' + stdId + '/assign-students';
                            form.submit();
                        };
                    }

                    const modal = document.getElementById('assignSingleStudentModal');
                    if (modal) modal.classList.remove('hidden');
                }

                window.teacherStudentPerformanceMap = @json($teacherStudentPerformanceMap ?? []);

                window.openStudentPerformanceModal = function(studentId) {
                    const data = (window.teacherStudentPerformanceMap && window.teacherStudentPerformanceMap[studentId])
                        ? window.teacherStudentPerformanceMap[studentId]
                        : {
                            student_id: studentId,
                            student_name: 'Student #' + studentId,
                            student_email: 'N/A',
                            standard_name: 'Unassigned',
                            total_exams: 0,
                            completed_exams: 0,
                            overall_percentage: 0,
                            total_obtained_marks: 0,
                            total_possible_marks: 0,
                            exams: []
                        };

                    window.currentPerfData = data;

                    document.getElementById('perf_student_name').textContent = (data.student_name || 'Student') + ' - Exams Performance';
                    document.getElementById('perf_student_subtext').textContent = `Email: ${data.student_email || 'N/A'} | Class: ${data.standard_name || 'Unassigned'}`;

                    document.getElementById('perf_total_exams_badge').textContent = `${data.total_exams || 0} Exam(s)`;
                    document.getElementById('perf_completed_exams_badge').textContent = `${data.completed_exams || 0} Completed`;
                    document.getElementById('perf_overall_score_badge').textContent = `${data.overall_percentage || 0}% (${data.total_obtained_marks || 0}/${data.total_possible_marks || 0})`;

                    const container = document.getElementById('perf_exams_container');
                    const exams = data.exams || [];

                    if (exams.length === 0) {
                        container.innerHTML = '<div class="p-8 text-center bg-slate-900/60 text-slate-400 text-xs">No exams found for this student.</div>';
                    } else {
                        let tableHtml = `
                            <table class="w-full text-left text-xs text-slate-300">
                                <thead class="bg-slate-950 text-slate-400 uppercase font-semibold text-[10px] tracking-wider border-b border-slate-800">
                                    <tr>
                                        <th class="px-4 py-3">Exam Name</th>
                                        <th class="px-4 py-3">Status</th>
                                        <th class="px-4 py-3">Score Obtained</th>
                                        <th class="px-4 py-3">Percentage</th>
                                        <th class="px-4 py-3 text-right">Action</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-slate-800/60 bg-slate-900">
                        `;

                        exams.forEach(ex => {
                            const isCompleted = ex.status === 'Completed';
                            const statusBadge = isCompleted
                                ? '<span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Completed</span>'
                                : '<span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold bg-slate-800 text-slate-400 border border-slate-700">Not Attempted</span>';

                            const pctColor = ex.percentage >= 80 ? 'text-emerald-400' : (ex.percentage >= 50 ? 'text-amber-400' : 'text-slate-400');

                            const actionBtn = isCompleted
                                ? `<button type="button" onclick="viewPerfExamSubmissionDetails(${ex.exam_id})" class="px-3 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-xs transition-all shadow-md inline-flex items-center space-x-1 cursor-pointer">
                                     <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                                     <span>View Breakdown</span>
                                   </button>`
                                : '<span class="text-[11px] text-slate-500 italic">Pending</span>';

                            tableHtml += `
                                <tr class="hover:bg-slate-800/40 transition-colors">
                                    <td class="px-4 py-3.5 font-bold text-white">
                                        <div>${ex.exam_name}</div>
                                        <div class="text-[10px] text-slate-400 font-normal">${ex.questions_count} Question(s)</div>
                                    </td>
                                    <td class="px-4 py-3.5">${statusBadge}</td>
                                    <td class="px-4 py-3.5 font-bold text-slate-200">${isCompleted ? ex.obtained_mark + ' / ' + ex.total_mark : '-'}</td>
                                    <td class="px-4 py-3.5 font-extrabold ${pctColor}">${isCompleted ? ex.percentage + '%' : '-'}</td>
                                    <td class="px-4 py-3.5 text-right">${actionBtn}</td>
                                </tr>
                            `;
                        });

                        tableHtml += '</tbody></table>';
                        container.innerHTML = tableHtml;
                    }

                    const modal = document.getElementById('studentPerformanceModal');
                    if (modal) {
                        modal.classList.remove('hidden');
                    }
                };

                window.viewPerfExamSubmissionDetails = function(examId) {
                    if (!window.currentPerfData || !window.currentPerfData.exams) return;
                    const ex = window.currentPerfData.exams.find(e => e.exam_id == examId);
                    if (!ex) return;

                    openStudentViewSubmissionModal({
                        name: ex.exam_name,
                        student_name: window.currentPerfData.student_name,
                        obtained_mark: ex.obtained_mark,
                        total_mark: ex.total_mark,
                        details: ex.details || []
                    });
                };
            </script>
        @endif

        <!-- STUDENT EXAM PERFORMANCE MODAL FOR TEACHERS & ADMIN -->
        <div id="studentPerformanceModal" class="hidden fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4 overflow-y-auto" style="z-index: 9000;">
            <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-4xl overflow-hidden shadow-2xl my-8 flex flex-col max-h-[90vh]">
                <div class="px-6 py-5 border-b border-slate-800 flex items-center justify-between bg-slate-950/60 shrink-0">
                    <div class="flex items-center space-x-3">
                        <div class="w-10 h-10 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 font-bold flex items-center justify-center text-base shrink-0">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>
                        </div>
                        <div>
                            <h3 id="perf_student_name" class="text-lg font-extrabold text-white">Student Exams Performance</h3>
                            <p class="text-xs text-slate-400" id="perf_student_subtext">Individual exam results across all teacher assigned exams</p>
                        </div>
                    </div>
                    <button type="button" onclick="document.getElementById('studentPerformanceModal').classList.add('hidden')" class="text-slate-400 hover:text-white transition-colors cursor-pointer p-1.5 rounded-lg hover:bg-slate-800">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                    </button>
                </div>

                <div class="p-6 bg-slate-950/40 border-b border-slate-800/80 grid grid-cols-1 sm:grid-cols-3 gap-4 shrink-0">
                    <div class="bg-slate-900 border border-slate-800 rounded-xl p-4 flex items-center justify-between">
                        <div>
                            <span class="text-xs text-slate-400 uppercase font-semibold">Exams Conducted</span>
                            <h4 id="perf_total_exams_badge" class="text-xl font-extrabold text-white mt-1">0 Exams</h4>
                        </div>
                        <div class="p-2.5 rounded-lg bg-indigo-500/10 text-indigo-400">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                        </div>
                    </div>

                    <div class="bg-slate-900 border border-slate-800 rounded-xl p-4 flex items-center justify-between">
                        <div>
                            <span class="text-xs text-slate-400 uppercase font-semibold">Exams Completed</span>
                            <h4 id="perf_completed_exams_badge" class="text-xl font-extrabold text-emerald-400 mt-1">0 Completed</h4>
                        </div>
                        <div class="p-2.5 rounded-lg bg-emerald-500/10 text-emerald-400">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                        </div>
                    </div>

                    <div class="bg-slate-900 border border-slate-800 rounded-xl p-4 flex items-center justify-between">
                        <div>
                            <span class="text-xs text-slate-400 uppercase font-semibold">Overall Score</span>
                            <h4 id="perf_overall_score_badge" class="text-xl font-extrabold text-amber-400 mt-1">0%</h4>
                        </div>
                        <div class="p-2.5 rounded-lg bg-amber-500/10 text-amber-400">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 3.055A9.001 9.001 0 1020.945 13H11V3.055z"/></svg>
                        </div>
                    </div>
                </div>

                <div class="p-6 overflow-y-auto space-y-4 flex-1">
                    <h4 class="text-xs font-bold uppercase tracking-wider text-slate-300">Exams Performance Breakdown</h4>
                    <div id="perf_exams_container" class="overflow-x-auto rounded-xl border border-slate-800">
                    </div>
                </div>

                <div class="px-6 py-4 bg-slate-950/80 border-t border-slate-800 flex justify-end shrink-0">
                    <button type="button" onclick="document.getElementById('studentPerformanceModal').classList.add('hidden')" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-sm font-semibold transition-colors cursor-pointer">Close</button>
                </div>
            </div>
        </div>

        <!-- GLOBAL SUBMISSION DETAILS MODAL FOR STUDENTS AND TEACHERS -->
        <div id="studentViewSubmissionModal" class="hidden fixed inset-0 bg-slate-900/70 backdrop-blur-sm flex items-center justify-center p-4" style="z-index: 9999;">
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

        <!-- DASHBOARD EDIT EXAM MODAL -->
        @php
            $isDashboardEditExamModalOpen = $errors->any() && old('_redirect_to_dashboard') == '1';
        @endphp
        <div id="dashboardEditExamModal" class="{{ $isDashboardEditExamModalOpen ? '' : 'hidden' }} fixed inset-0 z-50 bg-black/75 backdrop-blur-sm overflow-y-auto p-2 sm:p-4 flex justify-center items-start">
            <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-4xl max-h-[92vh] flex flex-col overflow-hidden shadow-2xl my-2 sm:my-4">
                <!-- Header -->
                <div class="px-6 py-4 border-b border-slate-800 flex items-center justify-between bg-slate-950/80 shrink-0">
                    <h3 class="text-base font-bold text-white flex items-center gap-2">
                        <svg class="w-5 h-5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>
                        </svg>
                        <span>Edit Exam Details</span>
                    </h3>
                    <button type="button" onclick="closeDashboardEditExamModal()" class="text-slate-400 hover:text-white transition-colors cursor-pointer p-1">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                    </button>
                </div>

                <form id="dashboardEditExamForm" method="POST" action="{{ old('_action_url', '') }}" class="flex flex-col flex-1 overflow-hidden min-h-0">
                    @csrf
                    @method('PUT')
                    <input type="hidden" name="_redirect_to_dashboard" value="1">
                    <input type="hidden" name="_action_url" id="dashboard_edit_exam_action_url" value="{{ old('_action_url', '') }}">

                    <div class="p-4 sm:p-6 overflow-y-auto space-y-4 flex-1">
                        @if ($isDashboardEditExamModalOpen && $errors->any())
                            <div class="p-3.5 rounded-xl bg-red-950/80 border border-red-500/40 text-red-200 text-xs">
                                <span class="font-bold flex items-center gap-1.5 text-red-300">
                                    <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                                    <span>{{ $errors->first() }}</span>
                                </span>
                            </div>
                        @endif

                        <!-- Primary Row: Name, Type, Duration, Status -->
                        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-12 gap-3 items-start">
                            <div class="md:col-span-5">
                                <label for="dashboard_edit_exam_name" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Exam Name <span class="text-rose-400">*</span></label>
                                <input type="text" id="dashboard_edit_exam_name" name="name" required value="{{ old('name') }}" placeholder="Enter exam title" class="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-xs">
                            </div>

                            <div class="md:col-span-2">
                                <label for="dashboard_edit_exam_type" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Type <span class="text-rose-400">*</span></label>
                                <select id="dashboard_edit_exam_type" name="type" required onchange="toggleDashboardEditExamDuration(this.value)" class="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-xs">
                                    <option value="1">1 - Timed</option>
                                    <option value="2">2 - Non-Timed</option>
                                    <option value="3">3 - Text Entry</option>
                                </select>
                            </div>

                            <div id="dashboard_edit_exam_duration_wrapper" class="md:col-span-2">
                                <label for="dashboard_edit_exam_duration" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Duration (Min) <span class="text-rose-400">*</span></label>
                                <input type="number" id="dashboard_edit_exam_duration" name="duration" min="1" max="1440" value="{{ old('duration', 60) }}" placeholder="60" class="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-xs">
                            </div>

                            <div class="md:col-span-3">
                                <label for="dashboard_edit_exam_status" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Status <span class="text-rose-400">*</span></label>
                                <select id="dashboard_edit_exam_status" name="status" required class="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-xs">
                                    <option value="1">1 - Active</option>
                                    <option value="2">2 - Inactive</option>
                                </select>
                            </div>
                        </div>

                        <!-- Curriculum Hierarchy -->
                        <div class="p-4 rounded-xl bg-slate-950/70 border border-slate-800 space-y-3">
                            <div class="flex items-center justify-between">
                                <label class="block text-xs font-bold text-indigo-300 uppercase tracking-wider flex items-center gap-1.5">
                                    <svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
                                    <span>Curriculum Classification</span>
                                </label>
                                <span class="text-[11px] text-slate-400">Classify exam by academic curriculum</span>
                            </div>

                            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-5 gap-3">
                                <!-- 1. Syllabus -->
                                <div>
                                    <label for="dashboard_edit_exam_syllabus" class="block text-[11px] font-semibold text-slate-300 uppercase tracking-wider mb-1">Syllabus</label>
                                    <select id="dashboard_edit_exam_syllabus" name="syllabus_id" onchange="onDashboardEditExamSyllabusChange()" class="w-full px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-100 text-xs focus:ring-2 focus:ring-indigo-500 focus:outline-none">
                                        <option value="">Select Syllabus</option>
                                        @foreach($syllabi ?? [] as $syl)
                                            <option value="{{ $syl->id }}">{{ $syl->name }}</option>
                                        @endforeach
                                    </select>
                                </div>

                                <!-- 2. Primary Class / Standard -->
                                <div>
                                    <label for="dashboard_edit_exam_standard" class="block text-[11px] font-semibold text-slate-300 uppercase tracking-wider mb-1">Primary Class</label>
                                    <select id="dashboard_edit_exam_standard" name="standard_id" class="w-full px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-100 text-xs focus:ring-2 focus:ring-indigo-500 focus:outline-none">
                                        <option value="">Select Class</option>
                                        @foreach($allStandardsForSelect ?? [] as $std)
                                            <option value="{{ $std->id }}">{{ $std->name }}</option>
                                        @endforeach
                                    </select>
                                </div>

                                <!-- 3. Subject -->
                                <div>
                                    <label for="dashboard_edit_exam_subject" class="block text-[11px] font-semibold text-slate-300 uppercase tracking-wider mb-1">Subject</label>
                                    <select id="dashboard_edit_exam_subject" name="subject_id" onchange="onDashboardEditExamSubjectChange()" class="w-full px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-100 text-xs focus:ring-2 focus:ring-indigo-500 focus:outline-none">
                                        <option value="">Select Subject</option>
                                        @foreach($subjectsData ?? [] as $sb)
                                            <option value="{{ $sb->id }}">{{ $sb->name }}</option>
                                        @endforeach
                                    </select>
                                </div>

                                <!-- 4. Chapter -->
                                <div>
                                    <label for="dashboard_edit_exam_chapter" class="block text-[11px] font-semibold text-slate-300 uppercase tracking-wider mb-1">Chapter</label>
                                    <select id="dashboard_edit_exam_chapter" name="chapter_id" onchange="onDashboardEditExamChapterChange()" class="w-full px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-100 text-xs focus:ring-2 focus:ring-indigo-500 focus:outline-none">
                                        <option value="">Select Chapter</option>
                                    </select>
                                </div>

                                <!-- 5. Topic -->
                                <div>
                                    <label for="dashboard_edit_exam_topic" class="block text-[11px] font-semibold text-slate-300 uppercase tracking-wider mb-1">Topic</label>
                                    <select id="dashboard_edit_exam_topic" name="topic_id" class="w-full px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-100 text-xs focus:ring-2 focus:ring-indigo-500 focus:outline-none">
                                        <option value="">Select Topic</option>
                                    </select>
                                </div>
                            </div>
                        </div>

                        <!-- Assigned Classes / Standards -->
                        @if(isset($allStandardsForSelect) && $allStandardsForSelect->isNotEmpty())
                            <div class="p-4 rounded-xl bg-slate-950/70 border border-slate-800 space-y-3">
                                <div class="flex items-center justify-between">
                                    <label class="block text-xs font-bold text-sky-300 uppercase tracking-wider flex items-center gap-1.5">
                                        <svg class="w-4 h-4 text-sky-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>
                                        <span>Assign to Classes / Standards</span>
                                    </label>
                                    <span class="text-[11px] text-slate-400">Students in selected classes will see this exam</span>
                                </div>

                                <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-2.5 max-h-48 overflow-y-auto p-1">
                                    @foreach($allStandardsForSelect as $std)
                                        <label class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 hover:border-indigo-500/40 cursor-pointer flex items-center space-x-2.5 transition-colors">
                                            <input type="checkbox" name="standard_ids[]" value="{{ $std->id }}" class="dashboard-edit-std-checkbox rounded bg-slate-950 border-slate-700 text-indigo-600 focus:ring-indigo-500">
                                            <span class="text-xs font-semibold text-slate-200">{{ $std->name }}</span>
                                        </label>
                                    @endforeach
                                </div>
                            </div>
                        @endif
                    </div>

                    <!-- Footer -->
                    <div class="px-6 py-4 border-t border-slate-800 flex justify-end space-x-3 bg-slate-950/80 shrink-0">
                        <button type="button" onclick="closeDashboardEditExamModal()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold transition-colors cursor-pointer">Cancel</button>
                        <button type="submit" class="px-5 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold shadow-lg shadow-indigo-600/30 transition-all cursor-pointer">Update Exam</button>
                    </div>
                </form>
            </div>
        </div>

        <x-exam-leaderboard-modal />

        <x-standard-chapters-modal :subjects="$subjects" :standards="$allStandardsForSelect ?? $standards" />

    </div>
</x-layouts.app>
