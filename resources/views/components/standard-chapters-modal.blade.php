@props(['subjects' => [], 'standards' => []])

<div id="standardChaptersModal" class="hidden fixed inset-0 z-50 bg-black/80 backdrop-blur-md flex items-center justify-center p-3 sm:p-5 overflow-y-auto">
    <div class="relative w-full max-w-4xl bg-slate-900 border border-slate-800 rounded-3xl shadow-2xl overflow-hidden my-auto flex flex-col max-h-[92vh]">
        
        <!-- Modal Header -->
        <div class="px-6 py-5 border-b border-slate-800 bg-gradient-to-r from-slate-900 via-indigo-950/40 to-slate-900 flex items-center justify-between shrink-0">
            <div class="flex items-center space-x-3">
                <div class="w-10 h-10 rounded-2xl bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 flex items-center justify-center font-bold text-lg shadow-inner">
                    <span>📚</span>
                </div>
                <div>
                    <div class="flex items-center space-x-2">
                        <h3 class="text-lg font-bold text-white tracking-tight">Curriculum Structure</h3>
                        <span id="scm_standard_badge" class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Standard</span>
                    </div>
                    <p class="text-xs text-slate-400 mt-0.5">
                        Manage chapters inside <span id="scm_standard_title" class="text-indigo-300 font-semibold">Standard</span> and topics inside chapters.
                    </p>
                </div>
            </div>

            <div class="flex items-center space-x-2">
                <button type="button" onclick="closeStandardChaptersModal()" class="w-9 h-9 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-slate-400 hover:text-white flex items-center justify-center transition-all cursor-pointer border border-slate-700/60">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                    </svg>
                </button>
            </div>
        </div>

        <!-- Secondary Controls Toolbar -->
        <div class="px-6 py-3.5 bg-slate-950/70 border-b border-slate-800/80 flex flex-wrap items-center justify-between gap-3 shrink-0">
            <div class="flex items-center space-x-3 flex-1 min-w-[240px]">
                <!-- Standard Switcher -->
                <div class="flex items-center space-x-2 text-xs text-slate-400">
                    <label for="scm_standard_select" class="font-semibold uppercase tracking-wider text-[11px] text-slate-400">Class:</label>
                    <select id="scm_standard_select" onchange="onStandardSelectorChange(this.value)" class="px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-700 text-white font-medium text-xs focus:outline-none focus:border-indigo-500">
                        @foreach($standards as $std)
                            <option value="{{ $std->id }}">{{ $std->name }}</option>
                        @endforeach
                    </select>
                </div>

                <!-- Search Filter -->
                <div class="relative flex-1 max-w-xs">
                    <input type="text" id="scm_chapter_search" oninput="filterChaptersList(this.value)" placeholder="Search chapters..." class="w-full pl-8 pr-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-200 placeholder-slate-500 text-xs focus:outline-none focus:border-indigo-500">
                    <svg class="w-3.5 h-3.5 text-slate-500 absolute left-2.5 top-2.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                </div>
            </div>

            <!-- Add Chapter Button -->
            <button type="button" onclick="toggleAddChapterForm()" class="px-3.5 py-1.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold shadow-md shadow-indigo-600/30 transition-all inline-flex items-center space-x-1.5 cursor-pointer">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
                <span>Add Chapter</span>
            </button>
        </div>

        <!-- Add Chapter Collapsible Form -->
        <div id="scm_add_chapter_form_container" class="hidden px-6 py-4 bg-indigo-950/20 border-b border-indigo-500/20 shrink-0">
            <form id="scm_new_chapter_form" onsubmit="event.preventDefault(); submitCreateChapter();" class="space-y-3">
                <div class="flex items-center justify-between">
                    <h4 class="text-xs font-bold uppercase tracking-wider text-indigo-300 flex items-center space-x-1.5">
                        <span>✨</span>
                        <span>Create New Chapter in this Standard</span>
                    </h4>
                    <button type="button" onclick="toggleAddChapterForm()" class="text-xs text-slate-400 hover:text-slate-200 cursor-pointer">Cancel</button>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-12 gap-3">
                    <div class="sm:col-span-7">
                        <label class="block text-[11px] font-semibold text-slate-300 mb-1">Chapter Name <span class="text-rose-400">*</span></label>
                        <input type="text" id="scm_new_chapter_name" required placeholder="e.g. Chapter 1: Real Numbers" class="w-full px-3.5 py-2 rounded-xl bg-slate-950 border border-slate-700 text-white placeholder-slate-500 text-xs focus:outline-none focus:ring-2 focus:ring-indigo-500">
                    </div>
                    <div class="sm:col-span-5">
                        <label class="block text-[11px] font-semibold text-slate-300 mb-1">Subject (Optional)</label>
                        <select id="scm_new_chapter_subject" class="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-700 text-white text-xs focus:outline-none focus:ring-2 focus:ring-indigo-500">
                            <option value="">-- No Specific Subject --</option>
                            @foreach($subjects as $sub)
                                <option value="{{ $sub->id }}">{{ $sub->name }}</option>
                            @endforeach
                        </select>
                    </div>
                </div>
                <div class="flex justify-end space-x-2 pt-1">
                    <button type="button" onclick="toggleAddChapterForm()" class="px-3.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-medium transition-colors cursor-pointer">
                        Cancel
                    </button>
                    <button type="submit" id="scm_save_chapter_btn" class="px-4 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold shadow-md transition-all inline-flex items-center space-x-1.5 cursor-pointer">
                        <span>Save Chapter</span>
                    </button>
                </div>
            </form>
        </div>

        <!-- Toast Feedback Banner -->
        <div id="scm_feedback_banner" class="hidden px-6 py-2.5 text-xs font-medium flex items-center justify-between border-b shrink-0 transition-all">
            <span id="scm_feedback_text"></span>
            <button type="button" onclick="document.getElementById('scm_feedback_banner').classList.add('hidden')" class="text-slate-400 hover:text-white">✕</button>
        </div>

        <!-- Chapters & Topics Scrollable Body -->
        <div id="scm_chapters_container" class="p-6 overflow-y-auto space-y-4 flex-1">
            <!-- Dynamic Content loaded via JS -->
            <div id="scm_loading_state" class="py-12 text-center text-slate-400 space-y-2">
                <svg class="animate-spin h-8 w-8 text-indigo-500 mx-auto" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8H4z"></path>
                </svg>
                <p class="text-xs font-medium">Loading chapters & topics...</p>
            </div>
            <div id="scm_chapters_list" class="space-y-4"></div>
        </div>

        <!-- Modal Footer -->
        <div class="px-6 py-3.5 border-t border-slate-800 bg-slate-950/80 flex items-center justify-between shrink-0">
            <div class="text-xs text-slate-400 flex items-center space-x-2">
                <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                <span id="scm_summary_count">0 Chapters</span>
            </div>
            <button type="button" onclick="closeStandardChaptersModal()" class="px-4 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white text-xs font-semibold border border-slate-700 transition-colors cursor-pointer">
                Close
            </button>
        </div>

    </div>
</div>

<!-- Subjects data for JS mapping -->
<script>
    const SCM_SUBJECTS = @json($subjects);
    let scmCurrentStandardId = null;
    let scmCurrentStandardName = '';
    let scmChaptersData = [];

    function openStandardChaptersModal(standardId, standardName) {
        scmCurrentStandardId = parseInt(standardId);
        scmCurrentStandardName = standardName || 'Class Standard';

        document.getElementById('scm_standard_title').innerText = scmCurrentStandardName;
        document.getElementById('scm_standard_badge').innerText = 'ID: #' + scmCurrentStandardId;
        
        const select = document.getElementById('scm_standard_select');
        if (select) {
            select.value = scmCurrentStandardId;
        }

        document.getElementById('scm_add_chapter_form_container').classList.add('hidden');
        document.getElementById('scm_chapter_search').value = '';
        document.getElementById('standardChaptersModal').classList.remove('hidden');

        fetchStandardChapters(scmCurrentStandardId);
    }

    function closeStandardChaptersModal() {
        document.getElementById('standardChaptersModal').classList.add('hidden');
    }

    function onStandardSelectorChange(newStandardId) {
        const select = document.getElementById('scm_standard_select');
        const selectedOption = select.options[select.selectedIndex];
        openStandardChaptersModal(newStandardId, selectedOption ? selectedOption.text : 'Class Standard');
    }

    function toggleAddChapterForm() {
        const form = document.getElementById('scm_add_chapter_form_container');
        form.classList.toggle('hidden');
        if (!form.classList.contains('hidden')) {
            document.getElementById('scm_new_chapter_name').focus();
        }
    }

    function showScmFeedback(message, isError = false) {
        const banner = document.getElementById('scm_feedback_banner');
        const text = document.getElementById('scm_feedback_text');
        text.innerText = message;
        banner.className = isError
            ? 'px-6 py-2.5 text-xs font-semibold flex items-center justify-between border-b shrink-0 bg-rose-500/10 border-rose-500/20 text-rose-300'
            : 'px-6 py-2.5 text-xs font-semibold flex items-center justify-between border-b shrink-0 bg-emerald-500/10 border-emerald-500/20 text-emerald-300';
        banner.classList.remove('hidden');
        setTimeout(() => {
            banner.classList.add('hidden');
        }, 4000);
    }

    async function fetchStandardChapters(standardId) {
        const loading = document.getElementById('scm_loading_state');
        const list = document.getElementById('scm_chapters_list');
        loading.classList.remove('hidden');
        list.innerHTML = '';

        try {
            const res = await fetch(`/standards/${standardId}/chapters`, {
                headers: {
                    'Accept': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest'
                }
            });
            const data = await res.json();
            scmChaptersData = data.chapters || [];
            renderChaptersList(scmChaptersData);
        } catch (err) {
            console.error('Failed to load chapters:', err);
            list.innerHTML = `<div class="py-8 text-center text-rose-400 text-xs">Failed to load chapters. Please try again.</div>`;
        } finally {
            loading.classList.add('hidden');
        }
    }

    function filterChaptersList(query) {
        const q = (query || '').toLowerCase().trim();
        if (!q) {
            renderChaptersList(scmChaptersData);
            return;
        }
        const filtered = scmChaptersData.filter(ch => {
            const matchesName = (ch.name || '').toLowerCase().includes(q);
            const matchesSubject = ch.subject && (ch.subject.name || '').toLowerCase().includes(q);
            const matchesTopic = (ch.topics || []).some(tp => (tp.name || '').toLowerCase().includes(q));
            return matchesName || matchesSubject || matchesTopic;
        });
        renderChaptersList(filtered);
    }

    function renderChaptersList(chapters) {
        const list = document.getElementById('scm_chapters_list');
        const summary = document.getElementById('scm_summary_count');
        summary.innerText = `${chapters.length} Chapter${chapters.length === 1 ? '' : 's'}`;

        if (!chapters || chapters.length === 0) {
            list.innerHTML = `
                <div class="py-12 text-center text-slate-500 border border-dashed border-slate-800 rounded-2xl p-8 bg-slate-950/40">
                    <span class="text-3xl block mb-2">📖</span>
                    <p class="text-sm font-semibold text-slate-300">No chapters found for this standard</p>
                    <p class="text-xs text-slate-500 mt-1">Click the "+ Add Chapter" button above to create the first chapter.</p>
                </div>
            `;
            return;
        }

        let html = '';
        chapters.forEach(ch => {
            const topics = ch.topics || [];
            const topicsCount = topics.length;
            const subjectBadge = ch.subject
                ? `<span class="px-2 py-0.5 rounded-md text-[10px] font-semibold bg-sky-500/10 text-sky-300 border border-sky-500/20">${escapeHtml(ch.subject.name)}</span>`
                : `<span class="px-2 py-0.5 rounded-md text-[10px] font-semibold bg-slate-800 text-slate-400">General</span>`;

            html += `
                <div id="scm_chapter_card_${ch.id}" class="bg-slate-950/70 border border-slate-800 rounded-2xl overflow-hidden shadow-lg transition-all hover:border-slate-700/80">
                    <!-- Chapter Card Header -->
                    <div class="p-4 sm:p-5 flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800/60 bg-slate-900/40">
                        <div class="flex items-start space-x-3 flex-1 min-w-0">
                            <div class="w-8 h-8 rounded-xl bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 flex items-center justify-center font-bold text-xs shrink-0 mt-0.5">
                                📑
                            </div>
                            <div class="flex-1 min-w-0">
                                <div class="flex items-center space-x-2 flex-wrap gap-y-1">
                                    <h4 id="scm_chapter_title_${ch.id}" class="text-sm font-bold text-white break-words">${escapeHtml(ch.name)}</h4>
                                    ${subjectBadge}
                                    <span id="scm_topic_count_badge_${ch.id}" class="px-2 py-0.5 rounded-md text-[10px] font-semibold bg-purple-500/10 text-purple-300 border border-purple-500/20">
                                        ${topicsCount} Topic${topicsCount === 1 ? '' : 's'}
                                    </span>
                                </div>
                                <span class="text-[11px] text-slate-500 mt-0.5 block">Chapter ID: #${ch.id}</span>
                            </div>
                        </div>

                        <!-- Chapter Action Buttons -->
                        <div class="flex items-center space-x-1.5 shrink-0 self-end sm:self-auto">
                            <button type="button" onclick="toggleAddTopicForm(${ch.id})" class="px-2.5 py-1.5 rounded-lg bg-indigo-600/20 hover:bg-indigo-600/30 text-indigo-300 border border-indigo-500/30 text-xs font-semibold transition-all inline-flex items-center space-x-1 cursor-pointer">
                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
                                <span>Add Topic</span>
                            </button>
                            <button type="button" onclick="openEditChapterInline(${ch.id})" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-medium transition-all inline-flex items-center space-x-1 cursor-pointer">
                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/></svg>
                                <span>Edit</span>
                            </button>
                            <button type="button" onclick="deleteChapter(${ch.id}, '${escapeJs(ch.name)}')" class="px-2.5 py-1.5 rounded-lg bg-rose-500/10 hover:bg-rose-500/20 text-rose-400 border border-rose-500/20 text-xs font-medium transition-all inline-flex items-center cursor-pointer">
                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/></svg>
                            </button>
                        </div>
                    </div>

                    <!-- Inline Edit Chapter Form (Hidden by default) -->
                    <div id="scm_edit_chapter_box_${ch.id}" class="hidden p-4 bg-slate-900 border-b border-slate-800">
                        <form onsubmit="event.preventDefault(); submitEditChapter(${ch.id});" class="space-y-3">
                            <div class="grid grid-cols-1 sm:grid-cols-12 gap-3">
                                <div class="sm:col-span-7">
                                    <label class="block text-[11px] font-semibold text-slate-300 mb-1">Chapter Name</label>
                                    <input type="text" id="scm_edit_chapter_name_${ch.id}" value="${escapeHtml(ch.name)}" required class="w-full px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-white text-xs focus:outline-none focus:border-indigo-500">
                                </div>
                                <div class="sm:col-span-5">
                                    <label class="block text-[11px] font-semibold text-slate-300 mb-1">Subject</label>
                                    <select id="scm_edit_chapter_subject_${ch.id}" class="w-full px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-white text-xs focus:outline-none focus:border-indigo-500">
                                        <option value="">-- No Subject --</option>
                                        ${SCM_SUBJECTS.map(s => `<option value="${s.id}" ${ch.subject_id == s.id ? 'selected' : ''}>${escapeHtml(s.name)}</option>`).join('')}
                                    </select>
                                </div>
                            </div>
                            <div class="flex justify-end space-x-2">
                                <button type="button" onclick="cancelEditChapterInline(${ch.id})" class="px-3 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs">Cancel</button>
                                <button type="submit" class="px-3.5 py-1 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold">Save Changes</button>
                            </div>
                        </form>
                    </div>

                    <!-- Inline Add Topic Form (Hidden by default) -->
                    <div id="scm_add_topic_box_${ch.id}" class="hidden p-3.5 bg-indigo-950/20 border-b border-indigo-500/20">
                        <form onsubmit="event.preventDefault(); submitCreateTopic(${ch.id});" class="flex items-center space-x-2">
                            <div class="flex-1">
                                <input type="text" id="scm_new_topic_name_${ch.id}" required placeholder="Enter topic name (e.g. Fundamental Theorem of Arithmetic)..." class="w-full px-3.5 py-1.5 rounded-xl bg-slate-950 border border-slate-700 text-white placeholder-slate-500 text-xs focus:outline-none focus:ring-2 focus:ring-indigo-500">
                            </div>
                            <button type="submit" class="px-3.5 py-1.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold shadow shrink-0 cursor-pointer">
                                Save Topic
                            </button>
                            <button type="button" onclick="toggleAddTopicForm(${ch.id})" class="px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-400 hover:text-white text-xs shrink-0 cursor-pointer">
                                ✕
                            </button>
                        </form>
                    </div>

                    <!-- Topics List Section inside Chapter -->
                    <div class="p-4 bg-slate-950/40">
                        <div class="flex items-center justify-between mb-2">
                            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400 flex items-center space-x-1.5">
                                <span>📌</span>
                                <span>Topics in this Chapter</span>
                            </span>
                            <span class="text-[11px] text-slate-500">${topicsCount} recorded</span>
                        </div>

                        <div id="scm_topics_list_${ch.id}" class="space-y-1.5">
                            ${topics.length === 0 
                                ? `<p class="text-xs text-slate-500 italic py-2">No topics in this chapter yet. Click "+ Add Topic" to create one.</p>` 
                                : topics.map(tp => renderSingleTopicItem(tp, ch.id)).join('')}
                        </div>
                    </div>
                </div>
            `;
        });

        list.innerHTML = html;
    }

    function renderSingleTopicItem(tp, chapterId) {
        return `
            <div id="scm_topic_row_${tp.id}" class="flex items-center justify-between py-1.5 px-3 rounded-xl bg-slate-900/60 border border-slate-800/80 hover:bg-slate-800/40 transition-colors">
                <div class="flex items-center space-x-2 flex-1 min-w-0 mr-2">
                    <span class="w-1.5 h-1.5 rounded-full bg-cyan-400 shrink-0"></span>
                    <span id="scm_topic_title_${tp.id}" class="text-xs text-slate-200 font-medium truncate">${escapeHtml(tp.name)}</span>
                </div>
                <div class="flex items-center space-x-1 shrink-0">
                    <button type="button" onclick="openEditTopicInline(${tp.id}, '${escapeJs(tp.name)}', ${chapterId})" class="p-1 rounded text-slate-400 hover:text-indigo-300 hover:bg-slate-800 transition-colors" title="Edit Topic">
                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/></svg>
                    </button>
                    <button type="button" onclick="deleteTopic(${tp.id}, ${chapterId}, '${escapeJs(tp.name)}')" class="p-1 rounded text-slate-400 hover:text-rose-400 hover:bg-slate-800 transition-colors" title="Delete Topic">
                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/></svg>
                    </button>
                </div>
            </div>
        `;
    }

    // CREATE CHAPTER
    async function submitCreateChapter() {
        const nameInput = document.getElementById('scm_new_chapter_name');
        const subjectSelect = document.getElementById('scm_new_chapter_subject');
        const saveBtn = document.getElementById('scm_save_chapter_btn');

        const name = (nameInput.value || '').trim();
        const subjectId = subjectSelect.value || null;

        if (!name) {
            alert('Please enter a chapter name.');
            return;
        }

        saveBtn.disabled = true;
        saveBtn.innerText = 'Saving...';

        try {
            const token = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
            const res = await fetch(`/standards/${scmCurrentStandardId}/chapters`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'X-CSRF-TOKEN': token,
                    'X-Requested-With': 'XMLHttpRequest'
                },
                body: JSON.stringify({
                    name: name,
                    standard_id: scmCurrentStandardId,
                    subject_id: subjectId
                })
            });

            const data = await res.json();
            if (res.ok && data.success) {
                showScmFeedback(data.message || 'Chapter created successfully!');
                nameInput.value = '';
                toggleAddChapterForm();
                // Refresh list
                fetchStandardChapters(scmCurrentStandardId);
            } else {
                showScmFeedback(data.message || 'Failed to create chapter.', true);
            }
        } catch (err) {
            console.error('Error creating chapter:', err);
            showScmFeedback('Error creating chapter.', true);
        } finally {
            saveBtn.disabled = false;
            saveBtn.innerText = 'Save Chapter';
        }
    }

    // EDIT CHAPTER
    function openEditChapterInline(chapterId) {
        const box = document.getElementById(`scm_edit_chapter_box_${chapterId}`);
        if (box) box.classList.remove('hidden');
    }

    function cancelEditChapterInline(chapterId) {
        const box = document.getElementById(`scm_edit_chapter_box_${chapterId}`);
        if (box) box.classList.add('hidden');
    }

    async function submitEditChapter(chapterId) {
        const nameInput = document.getElementById(`scm_edit_chapter_name_${chapterId}`);
        const subjectSelect = document.getElementById(`scm_edit_chapter_subject_${chapterId}`);
        const name = (nameInput.value || '').trim();
        const subjectId = subjectSelect.value || null;

        if (!name) {
            alert('Chapter name is required.');
            return;
        }

        try {
            const token = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
            const res = await fetch(`/chapters/${chapterId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'X-CSRF-TOKEN': token,
                    'X-Requested-With': 'XMLHttpRequest'
                },
                body: JSON.stringify({
                    name: name,
                    subject_id: subjectId,
                    standard_id: scmCurrentStandardId
                })
            });

            const data = await res.json();
            if (res.ok && data.success) {
                showScmFeedback('Chapter updated successfully!');
                cancelEditChapterInline(chapterId);
                fetchStandardChapters(scmCurrentStandardId);
            } else {
                showScmFeedback(data.message || 'Failed to update chapter.', true);
            }
        } catch (err) {
            console.error('Error updating chapter:', err);
            showScmFeedback('Error updating chapter.', true);
        }
    }

    // DELETE CHAPTER
    async function deleteChapter(chapterId, chapterName) {
        if (!confirm(`Are you sure you want to delete chapter "${chapterName}"? All topics inside it will also be deleted.`)) {
            return;
        }

        try {
            const token = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
            const res = await fetch(`/chapters/${chapterId}`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'X-CSRF-TOKEN': token,
                    'X-Requested-With': 'XMLHttpRequest'
                }
            });

            const data = await res.json();
            if (res.ok && data.success) {
                showScmFeedback(`Chapter "${chapterName}" deleted.`);
                fetchStandardChapters(scmCurrentStandardId);
            } else {
                showScmFeedback(data.message || 'Failed to delete chapter.', true);
            }
        } catch (err) {
            console.error('Error deleting chapter:', err);
            showScmFeedback('Error deleting chapter.', true);
        }
    }

    // TOPIC CRUD FUNCTIONS
    function toggleAddTopicForm(chapterId) {
        const box = document.getElementById(`scm_add_topic_box_${chapterId}`);
        if (box) {
            box.classList.toggle('hidden');
            if (!box.classList.contains('hidden')) {
                const input = document.getElementById(`scm_new_topic_name_${chapterId}`);
                if (input) input.focus();
            }
        }
    }

    async function submitCreateTopic(chapterId) {
        const input = document.getElementById(`scm_new_topic_name_${chapterId}`);
        const name = (input.value || '').trim();

        if (!name) {
            alert('Please enter a topic name.');
            return;
        }

        try {
            const token = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
            const res = await fetch(`/chapters/${chapterId}/topics`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'X-CSRF-TOKEN': token,
                    'X-Requested-With': 'XMLHttpRequest'
                },
                body: JSON.stringify({
                    name: name,
                    chapter_id: chapterId
                })
            });

            const data = await res.json();
            if (res.ok && data.success) {
                showScmFeedback('Topic added successfully!');
                input.value = '';
                toggleAddTopicForm(chapterId);
                fetchStandardChapters(scmCurrentStandardId);
            } else {
                showScmFeedback(data.message || 'Failed to add topic.', true);
            }
        } catch (err) {
            console.error('Error adding topic:', err);
            showScmFeedback('Error adding topic.', true);
        }
    }

    function openEditTopicInline(topicId, currentName, chapterId) {
        const newName = prompt('Edit Topic Name:', currentName);
        if (newName === null) return;
        const trimmed = newName.trim();
        if (!trimmed) {
            alert('Topic name cannot be empty.');
            return;
        }
        submitEditTopic(topicId, trimmed, chapterId);
    }

    async function submitEditTopic(topicId, newName, chapterId) {
        try {
            const token = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
            const res = await fetch(`/topics/${topicId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'X-CSRF-TOKEN': token,
                    'X-Requested-With': 'XMLHttpRequest'
                },
                body: JSON.stringify({
                    name: newName,
                    chapter_id: chapterId
                })
            });

            const data = await res.json();
            if (res.ok && data.success) {
                showScmFeedback('Topic updated successfully!');
                fetchStandardChapters(scmCurrentStandardId);
            } else {
                showScmFeedback(data.message || 'Failed to update topic.', true);
            }
        } catch (err) {
            console.error('Error updating topic:', err);
            showScmFeedback('Error updating topic.', true);
        }
    }

    async function deleteTopic(topicId, chapterId, topicName) {
        if (!confirm(`Are you sure you want to delete topic "${topicName}"?`)) {
            return;
        }

        try {
            const token = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
            const res = await fetch(`/topics/${topicId}`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'X-CSRF-TOKEN': token,
                    'X-Requested-With': 'XMLHttpRequest'
                }
            });

            const data = await res.json();
            if (res.ok && data.success) {
                showScmFeedback(`Topic "${topicName}" deleted.`);
                fetchStandardChapters(scmCurrentStandardId);
            } else {
                showScmFeedback(data.message || 'Failed to delete topic.', true);
            }
        } catch (err) {
            console.error('Error deleting topic:', err);
            showScmFeedback('Error deleting topic.', true);
        }
    }

    function escapeHtml(str) {
        if (!str) return '';
        return String(str)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;');
    }

    function escapeJs(str) {
        if (!str) return '';
        return String(str).replace(/\\/g, '\\\\').replace(/'/g, "\\'").replace(/"/g, '\\"');
    }
</script>

