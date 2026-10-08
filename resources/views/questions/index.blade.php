<x-layouts.app title="Questions Management - Study App">
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
                        Create, manage, and edit questions with options across standards.
                    </p>
                </div>

                <div class="flex items-center gap-3">
                    <a href="{{ route('dashboard') }}" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium text-sm transition-all flex items-center space-x-2">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
                        </svg>
                        <span>Back to Dashboard</span>
                    </a>

                    <button onclick="document.getElementById('createQuestionModal').classList.remove('hidden')" class="px-5 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-sm transition-all shadow-lg shadow-indigo-600/30 flex items-center space-x-2 cursor-pointer">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
                        </svg>
                        <span>Add Question</span>
                    </button>
                </div>
            </div>
        </div>

        <!-- Questions Listing Directory -->
        <div class="bg-slate-900 border border-slate-800 rounded-2xl shadow-xl overflow-hidden">
            <div class="px-6 py-5 border-b border-slate-800 flex items-center justify-between">
                <h3 class="text-lg font-semibold text-white">All Questions</h3>
                <span class="text-xs text-slate-400 bg-slate-800 px-3 py-1 rounded-full border border-slate-700">Total: {{ $questions->total() }}</span>
            </div>

            <div class="overflow-x-auto">
                <table class="w-full text-left border-collapse text-sm">
                    <thead>
                        <tr class="bg-slate-950/60 border-b border-slate-800 text-slate-400 uppercase text-[11px] font-semibold tracking-wider">
                            <th class="py-3.5 px-6">Question Name</th>
                            <th class="py-3.5 px-6">Standard</th>
                            <th class="py-3.5 px-6">Type</th>
                            <th class="py-3.5 px-6">Marks</th>
                            <th class="py-3.5 px-6">Answers Options</th>
                            <th class="py-3.5 px-6">Created By</th>
                            <th class="py-3.5 px-6 text-right">Actions</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800/60 text-slate-300">
                        @forelse ($questions as $q)
                            <tr class="hover:bg-slate-800/40 transition-colors">
                                <td class="py-4 px-6 max-w-xs">
                                    <div class="font-medium text-white">{{ $q->name }}</div>
                                    @if($q->description)
                                        <div class="text-xs text-slate-400 mt-0.5 line-clamp-1" title="{{ $q->description }}">{{ $q->description }}</div>
                                    @endif
                                </td>
                                <td class="py-4 px-6">
                                    <span class="inline-flex items-center px-2.5 py-0.5 rounded-md text-xs font-medium bg-slate-800 text-slate-200 border border-slate-700">
                                        {{ $q->standard?->name ?? 'N/A' }}
                                    </span>
                                </td>
                                <td class="py-4 px-6">
                                    @if($q->type == 1)
                                        <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold bg-indigo-500/10 text-indigo-400 border border-indigo-500/20">Single Option</span>
                                    @elseif($q->type == 2)
                                        <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold bg-violet-500/10 text-violet-400 border border-violet-500/20">Multiple Option</span>
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
                                <td class="py-4 px-6 text-right space-x-2">
                                    <button onclick="openEditQuestionModal({{ json_encode([
                                        'id' => $q->id,
                                        'name' => $q->name,
                                        'description' => $q->description ?? '',
                                        'standard_id' => $q->standard_id,
                                        'type' => $q->type,
                                        'marks' => $q->marks,
                                        'answers' => $q->answers->map(fn($a) => ['id' => $a->id, 'name' => $a->name, 'is_correct' => $a->is_correct])->toArray(),
                                    ]) }})" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-indigo-300 text-xs font-medium border border-slate-700 transition-colors inline-flex items-center space-x-1 cursor-pointer">
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
                                <td colspan="7" class="py-8 text-center text-slate-500">
                                    No questions created yet. Click "Add Question" to create one.
                                </td>
                            </tr>
                        @endforelse
                    </tbody>
                </table>
            </div>

            @if($questions->hasPages())
                <div class="px-6 py-4 border-t border-slate-800">
                    {{ $questions->links() }}
                </div>
            @endif
        </div>

        <!-- CREATE QUESTION MODAL -->
        @php
            $isCreateModalOpen = $errors->any() && old('_method') !== 'PUT';
        @endphp
        <div id="createQuestionModal" class="{{ $isCreateModalOpen ? '' : 'hidden' }} fixed inset-0 z-50 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4 overflow-y-auto">
            <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-6xl overflow-hidden shadow-2xl my-8">
                <div class="px-6 py-4 border-b border-slate-800 flex items-center justify-between bg-slate-950/50">
                    <h3 class="text-lg font-bold text-white">Add New Question</h3>
                    <button onclick="document.getElementById('createQuestionModal').classList.add('hidden')" class="text-slate-400 hover:text-white transition-colors cursor-pointer">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                    </button>
                </div>

                <form method="POST" action="{{ route('questions.store') }}" class="p-6 space-y-4">
                    @csrf
                    
                    @if ($isCreateModalOpen && $errors->any())
                        <div class="p-3.5 rounded-xl bg-red-950/80 border border-red-500/40 text-red-200 text-xs">
                            <span class="font-bold flex items-center gap-1 text-red-300">
                                <svg class="w-4 h-4 inline" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                                Validation errors occurred. Please check the fields below.
                            </span>
                        </div>
                    @endif

                    <!-- Question Name (Required) -->
                    <div>
                        <label for="create_q_name" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Question Name / Prompt <span class="text-red-400">*</span></label>
                        <input type="text" id="create_q_name" name="name" required value="{{ old('name') }}" placeholder="Enter question prompt..." class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('name') border-red-500 focus:ring-red-500 @enderror">
                        @error('name')
                            <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                        @enderror
                    </div>

                    <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                        <!-- Standard Select (Required) -->
                        <div>
                            <label for="create_q_standard" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Standard <span class="text-red-400">*</span></label>
                            <select id="create_q_standard" name="standard_id" required class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('standard_id') border-red-500 focus:ring-red-500 @enderror">
                                <option value="" disabled {{ old('standard_id') ? '' : 'selected' }}>Select Standard</option>
                                @foreach($standards as $std)
                                    <option value="{{ $std->id }}" {{ old('standard_id') == $std->id ? 'selected' : '' }}>{{ $std->name }}</option>
                                @endforeach
                            </select>
                            @error('standard_id')
                                <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                            @enderror
                        </div>

                        <!-- Type Select (Required) -->
                        <div>
                            <label for="create_q_type" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Question Type <span class="text-red-400">*</span></label>
                            <select id="create_q_type" name="type" required onchange="toggleAnswersSection('create', this.value)" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('type') border-red-500 focus:ring-red-500 @enderror">
                                <option value="1" {{ old('type', '1') == '1' ? 'selected' : '' }}>1 - Single Option</option>
                                <option value="2" {{ old('type') == '2' ? 'selected' : '' }}>2 - Multiple Option</option>
                                <option value="3" {{ old('type') == '3' ? 'selected' : '' }}>3 - Text Entry</option>
                            </select>
                            @error('type')
                                <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                            @enderror
                        </div>

                        <!-- Marks (Required, Numbers Only) -->
                        <div>
                            <label for="create_q_marks" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Marks <span class="text-red-400">*</span></label>
                            <input type="number" id="create_q_marks" name="marks" required min="0" step="1" value="{{ old('marks', 1) }}" placeholder="1" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('marks') border-red-500 focus:ring-red-500 @enderror">
                            @error('marks')
                                <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                            @enderror
                        </div>
                    </div>

                    <!-- Description (Optional) -->
                    <div>
                        <label for="create_q_desc" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Description (Optional)</label>
                        <textarea id="create_q_desc" name="description" rows="2" placeholder="Additional explanation or context..." class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('description') border-red-500 focus:ring-red-500 @enderror">{{ old('description') }}</textarea>
                        @error('description')
                            <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                        @enderror
                    </div>

                    <!-- Answers Options Section (Max 4 Answers) -->
                    <div id="create_answers_container" class="space-y-3 pt-2 border-t border-slate-800">
                        <div class="flex items-center justify-between">
                            <label class="block text-xs font-semibold text-slate-300 uppercase tracking-wider">Answer Options (Min 2, Max 4)</label>
                            <span class="text-[11px] text-slate-400 italic">Single Option: exactly 1 correct answer. Multiple Option: at least 1 correct answer.</span>
                        </div>

                        @error('answers')
                            <div class="p-2.5 rounded-lg bg-red-950/80 border border-red-500/40 text-red-300 text-xs font-semibold">
                                {{ $message }}
                            </div>
                        @enderror

                        @for($i = 0; $i < 4; $i++)
                            <div class="flex items-center space-x-3 bg-slate-950 p-3 rounded-lg border border-slate-800">
                                <span class="text-xs font-bold text-slate-400 shrink-0 w-6">#{{ $i + 1 }}</span>
                                <input type="text" name="answers[{{ $i }}][name]" value="{{ old('answers.'.$i.'.name') }}" placeholder="Option {{ $i + 1 }} text" class="flex-1 px-3 py-1.5 rounded-md bg-slate-900 border border-slate-700 text-slate-100 text-xs focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                <label class="inline-flex items-center space-x-1 text-xs text-slate-300 cursor-pointer shrink-0">
                                    <input type="checkbox" name="answers[{{ $i }}][is_correct]" value="1" {{ old('answers.'.$i.'.is_correct') ? 'checked' : '' }} class="rounded bg-slate-900 border-slate-700 text-emerald-500 focus:ring-emerald-500">
                                    <span class="text-emerald-400 font-medium">Is Correct (1)</span>
                                </label>
                            </div>
                        @endfor
                    </div>

                    <div class="pt-4 flex justify-end space-x-3 border-t border-slate-800">
                        <button type="button" onclick="document.getElementById('createQuestionModal').classList.add('hidden')" class="px-4 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-sm font-medium transition-colors cursor-pointer">Cancel</button>
                        <button type="submit" class="px-5 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-semibold shadow-lg shadow-indigo-600/30 transition-all cursor-pointer">Save Question</button>
                    </div>
                </form>
            </div>
        </div>

        <!-- EDIT QUESTION MODAL -->
        @php
            $isEditModalOpen = $errors->any() && old('_method') === 'PUT';
        @endphp
        <div id="editQuestionModal" class="{{ $isEditModalOpen ? '' : 'hidden' }} fixed inset-0 z-50 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4 overflow-y-auto">
            <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-6xl overflow-hidden shadow-2xl my-8">
                <div class="px-6 py-4 border-b border-slate-800 flex items-center justify-between bg-slate-950/50">
                    <h3 class="text-lg font-bold text-white">Edit Question</h3>
                    <button onclick="document.getElementById('editQuestionModal').classList.add('hidden')" class="text-slate-400 hover:text-white transition-colors cursor-pointer">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                    </button>
                </div>

                <form id="editQuestionForm" method="POST" action="{{ old('_method') === 'PUT' ? old('_edit_action_url', '') : '' }}" class="p-6 space-y-4">
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

                    <!-- Question Name (Required) -->
                    <div>
                        <label for="edit_q_name" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Question Name / Prompt <span class="text-red-400">*</span></label>
                        <input type="text" id="edit_q_name" name="name" required value="{{ old('_method') === 'PUT' ? old('name') : '' }}" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('name') border-red-500 focus:ring-red-500 @enderror">
                        @error('name')
                            <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                        @enderror
                    </div>

                    <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                        <!-- Standard Select (Required) -->
                        <div>
                            <label for="edit_q_standard" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Standard <span class="text-red-400">*</span></label>
                            <select id="edit_q_standard" name="standard_id" required class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('standard_id') border-red-500 focus:ring-red-500 @enderror">
                                @foreach($standards as $std)
                                    <option value="{{ $std->id }}" {{ old('_method') === 'PUT' && old('standard_id') == $std->id ? 'selected' : '' }}>{{ $std->name }}</option>
                                @endforeach
                            </select>
                            @error('standard_id')
                                <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                            @enderror
                        </div>

                        <!-- Type Select (Required) -->
                        <div>
                            <label for="edit_q_type" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Question Type <span class="text-red-400">*</span></label>
                            <select id="edit_q_type" name="type" required onchange="toggleAnswersSection('edit', this.value)" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('type') border-red-500 focus:ring-red-500 @enderror">
                                <option value="1" {{ old('_method') === 'PUT' && old('type') == '1' ? 'selected' : '' }}>1 - Single Option</option>
                                <option value="2" {{ old('_method') === 'PUT' && old('type') == '2' ? 'selected' : '' }}>2 - Multiple Option</option>
                                <option value="3" {{ old('_method') === 'PUT' && old('type') == '3' ? 'selected' : '' }}>3 - Text Entry</option>
                            </select>
                            @error('type')
                                <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                            @enderror
                        </div>

                        <!-- Marks (Required, Numbers Only) -->
                        <div>
                            <label for="edit_q_marks" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Marks <span class="text-red-400">*</span></label>
                            <input type="number" id="edit_q_marks" name="marks" required min="0" step="1" value="{{ old('_method') === 'PUT' ? old('marks') : '' }}" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('marks') border-red-500 focus:ring-red-500 @enderror">
                            @error('marks')
                                <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                            @enderror
                        </div>
                    </div>

                    <!-- Description (Optional) -->
                    <div>
                        <label for="edit_q_desc" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Description (Optional)</label>
                        <textarea id="edit_q_desc" name="description" rows="2" class="w-full px-3.5 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm @error('description') border-red-500 focus:ring-red-500 @enderror">{{ old('_method') === 'PUT' ? old('description') : '' }}</textarea>
                        @error('description')
                            <p class="mt-1 text-xs text-red-400">{{ $message }}</p>
                        @enderror
                    </div>

                    <!-- Answers Options Section (Max 4 Answers) -->
                    <div id="edit_answers_container" class="space-y-3 pt-2 border-t border-slate-800">
                        <div class="flex items-center justify-between">
                            <label class="block text-xs font-semibold text-slate-300 uppercase tracking-wider">Answer Options (Min 2, Max 4)</label>
                            <span class="text-[11px] text-slate-400 italic">Single Option: exactly 1 correct answer. Multiple Option: at least 1 correct answer.</span>
                        </div>

                        @error('answers')
                            <div class="p-2.5 rounded-lg bg-red-950/80 border border-red-500/40 text-red-300 text-xs font-semibold">
                                {{ $message }}
                            </div>
                        @enderror

                        @for($i = 0; $i < 4; $i++)
                            <div class="flex items-center space-x-3 bg-slate-950 p-3 rounded-lg border border-slate-800">
                                <span class="text-xs font-bold text-slate-400 shrink-0 w-6">#{{ $i + 1 }}</span>
                                <input type="text" id="edit_ans_{{ $i }}_name" name="answers[{{ $i }}][name]" value="{{ old('_method') === 'PUT' ? old('answers.'.$i.'.name') : '' }}" placeholder="Option {{ $i + 1 }} text" class="flex-1 px-3 py-1.5 rounded-md bg-slate-900 border border-slate-700 text-slate-100 text-xs focus:outline-none focus:ring-1 focus:ring-indigo-500">
                                <label class="inline-flex items-center space-x-1 text-xs text-slate-300 cursor-pointer shrink-0">
                                    <input type="checkbox" id="edit_ans_{{ $i }}_correct" name="answers[{{ $i }}][is_correct]" value="1" {{ old('_method') === 'PUT' && old('answers.'.$i.'.is_correct') ? 'checked' : '' }} class="rounded bg-slate-900 border-slate-700 text-emerald-500 focus:ring-emerald-500">
                                    <span class="text-emerald-400 font-medium">Is Correct (1)</span>
                                </label>
                            </div>
                        @endfor
                    </div>

                    <div class="pt-4 flex justify-end space-x-3 border-t border-slate-800">
                        <button type="button" onclick="document.getElementById('editQuestionModal').classList.add('hidden')" class="px-4 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-sm font-medium transition-colors cursor-pointer">Cancel</button>
                        <button type="submit" class="px-5 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-semibold shadow-lg shadow-indigo-600/30 transition-all cursor-pointer">Update Question</button>
                    </div>
                </form>
            </div>
        </div>

        <script>
            function toggleAnswersSection(prefix, typeVal) {
                const container = document.getElementById(prefix + '_answers_container');
                if (container) {
                    if (parseInt(typeVal) === 3) {
                        container.classList.add('hidden');
                    } else {
                        container.classList.remove('hidden');
                    }
                }
            }

            function openEditQuestionModal(data) {
                const actionUrl = '/questions/' + data.id;
                document.getElementById('editQuestionForm').action = actionUrl;
                document.getElementById('edit_action_url').value = actionUrl;
                document.getElementById('edit_q_name').value = data.name || '';
                document.getElementById('edit_q_desc').value = data.description || '';
                document.getElementById('edit_q_standard').value = data.standard_id || '';
                document.getElementById('edit_q_type').value = data.type || 1;
                document.getElementById('edit_q_marks').value = data.marks !== undefined ? data.marks : 1;

                toggleAnswersSection('edit', data.type || 1);

                // Pre-fill answer slots (up to 4)
                const answers = data.answers || [];
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

                document.getElementById('editQuestionModal').classList.remove('hidden');
            }

            @if($isEditModalOpen)
                document.addEventListener('DOMContentLoaded', function() {
                    toggleAnswersSection('edit', "{{ old('type', 1) }}");
                });
            @endif

            @if($isCreateModalOpen)
                document.addEventListener('DOMContentLoaded', function() {
                    toggleAnswersSection('create', "{{ old('type', 1) }}");
                });
            @endif
        </script>

    </div>
</x-layouts.app>
