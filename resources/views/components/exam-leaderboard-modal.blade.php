<!-- EXAM LEADERBOARD REUSABLE MODAL -->
<div id="examLeaderboardModal" class="hidden fixed inset-0 z-50 bg-black/80 backdrop-blur-md flex items-center justify-center p-4 overflow-y-auto">
    <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-4xl overflow-hidden shadow-2xl my-8">
        <!-- Modal Header -->
        <div class="px-6 py-5 border-b border-slate-800 flex items-center justify-between bg-gradient-to-r from-amber-950/40 via-slate-950 to-indigo-950/40">
            <div class="flex items-center space-x-3">
                <div class="w-10 h-10 rounded-xl bg-amber-500/10 border border-amber-500/30 text-amber-400 font-bold flex items-center justify-center text-lg shrink-0">
                    🏆
                </div>
                <div>
                    <h3 id="lb_modal_title" class="text-lg font-extrabold text-white flex items-center space-x-2">
                        <span>Exam Leaderboard</span>
                    </h3>
                    <p id="lb_modal_subtitle" class="text-xs text-slate-400">Class rankings & student performance metrics</p>
                </div>
            </div>
            <button type="button" onclick="closeExamLeaderboardModal()" class="text-slate-400 hover:text-white transition-colors cursor-pointer p-1.5 rounded-lg bg-slate-800 border border-slate-700">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
            </button>
        </div>

        <!-- Modal Body Content -->
        <div class="p-6 space-y-6">
            <!-- Loading State -->
            <div id="lb_modal_loading" class="py-12 text-center text-slate-400 space-y-3">
                <div class="w-10 h-10 border-4 border-amber-500/30 border-t-amber-500 rounded-full animate-spin mx-auto"></div>
                <p class="text-xs font-semibold text-amber-400">Fetching leaderboard rankings...</p>
            </div>

            <!-- Content State -->
            <div id="lb_modal_content" class="hidden space-y-6">
                <!-- Summary Stats Pills -->
                <div class="grid grid-cols-1 sm:grid-cols-4 gap-4">
                    <div class="bg-amber-950/20 border border-amber-500/30 rounded-xl p-4">
                        <span class="text-[10px] font-bold uppercase tracking-wider text-amber-400 block">Top Scorer 🥇</span>
                        <span id="lb_stat_top_scorer" class="text-base font-extrabold text-white truncate block mt-1">N/A</span>
                    </div>
                    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4">
                        <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400 block">Highest Score</span>
                        <span id="lb_stat_highest_score" class="text-xl font-black text-emerald-400 font-mono block mt-1">0</span>
                    </div>
                    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4">
                        <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400 block">Average Marks</span>
                        <span id="lb_stat_average_score" class="text-xl font-black text-indigo-400 font-mono block mt-1">0</span>
                    </div>
                    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4">
                        <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400 block">Submissions</span>
                        <span id="lb_stat_total_submissions" class="text-xl font-black text-sky-400 font-mono block mt-1">0</span>
                    </div>
                </div>

                <!-- Table Container -->
                <div class="rounded-xl border border-slate-800 overflow-hidden bg-slate-950">
                    <div class="overflow-x-auto max-h-[420px] overflow-y-auto">
                        <table class="w-full text-left text-xs text-slate-300 border-collapse">
                            <thead class="sticky top-0 bg-slate-900 border-b border-slate-800 text-slate-400 uppercase font-bold text-[10px] tracking-wider z-10">
                                <tr>
                                    <th scope="col" class="py-3 px-4 text-center w-16">Rank</th>
                                    <th scope="col" class="py-3 px-4">Student Name</th>
                                    <th scope="col" class="py-3 px-4">Class</th>
                                    <th scope="col" class="py-3 px-4 text-center">Correct Qs</th>
                                    <th scope="col" class="py-3 px-4 text-center">Score</th>
                                    <th scope="col" class="py-3 px-4 text-center">Percentage</th>
                                    <th scope="col" class="py-3 px-4 text-right">Submitted</th>
                                </tr>
                            </thead>
                            <tbody id="lb_modal_table_body" class="divide-y divide-slate-800/60">
                                <!-- Dynamic Rows -->
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            <!-- Empty State -->
            <div id="lb_modal_empty" class="hidden py-12 text-center text-slate-400 space-y-3">
                <span class="text-4xl block">🏆</span>
                <h4 class="text-base font-bold text-white">No Submissions Found</h4>
                <p class="text-xs text-slate-400 max-w-sm mx-auto">No students have submitted this exam yet. Check back after students complete their attempts.</p>
            </div>
        </div>

        <!-- Modal Footer -->
        <div class="px-6 py-4 border-t border-slate-800 flex items-center justify-between bg-slate-950/80">
            <a id="lb_modal_full_page_link" href="#" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-semibold text-xs transition-all inline-flex items-center space-x-2">
                <span>Open Full Page Leaderboard</span>
                <svg class="w-3.5 h-3.5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
            </a>
            <button type="button" onclick="closeExamLeaderboardModal()" class="px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs shadow-md transition-all cursor-pointer">
                Close
            </button>
        </div>
    </div>
</div>

<script>
    function openExamLeaderboardModal(examId, examName) {
        const modal = document.getElementById('examLeaderboardModal');
        const loading = document.getElementById('lb_modal_loading');
        const content = document.getElementById('lb_modal_content');
        const empty = document.getElementById('lb_modal_empty');
        const titleEl = document.getElementById('lb_modal_title');
        const fullLink = document.getElementById('lb_modal_full_page_link');
        const tbody = document.getElementById('lb_modal_table_body');

        if (!modal) return;

        if (titleEl) titleEl.innerHTML = `<span>🏆 ${examName} - Leaderboard</span>`;
        if (fullLink) fullLink.href = `/exams/${examId}/leaderboard`;

        modal.classList.remove('hidden');
        loading.classList.remove('hidden');
        content.classList.add('hidden');
        empty.classList.add('hidden');

        fetch(`/exams/${examId}/leaderboard`, {
            headers: {
                'Accept': 'application/json',
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(res => res.json())
        .then(data => {
            loading.classList.add('hidden');

            if (!data.leaderboard || data.leaderboard.length === 0) {
                empty.classList.remove('hidden');
                return;
            }

            content.classList.remove('hidden');

            // Populate Stats
            document.getElementById('lb_stat_top_scorer').textContent = data.summary.top_scorer || 'N/A';
            document.getElementById('lb_stat_highest_score').textContent = `${data.summary.highest_marks} / ${data.exam.total_mark}`;
            document.getElementById('lb_stat_average_score').textContent = `${data.summary.average_marks} / ${data.exam.total_mark}`;
            document.getElementById('lb_stat_total_submissions').textContent = `${data.summary.total_submissions} Student(s)`;

            // Populate Table
            let rowsHtml = '';
            data.leaderboard.forEach(row => {
                const rank = row.rank;
                const isTop1 = rank === 1;
                const isTop2 = rank === 2;
                const isTop3 = rank === 3;
                const isCurrent = row.is_current_user;

                let rankBadge = `<span class="inline-flex items-center justify-center w-7 h-7 rounded-lg bg-slate-800 text-slate-300 font-extrabold text-xs border border-slate-700">#${rank}</span>`;
                if (isTop1) rankBadge = `<span class="inline-flex items-center justify-center w-8 h-8 rounded-full bg-gradient-to-br from-amber-300 to-amber-600 text-slate-950 font-black text-sm shadow-md">🥇</span>`;
                if (isTop2) rankBadge = `<span class="inline-flex items-center justify-center w-8 h-8 rounded-full bg-gradient-to-br from-slate-200 to-slate-400 text-slate-950 font-black text-sm shadow-md">🥈</span>`;
                if (isTop3) rankBadge = `<span class="inline-flex items-center justify-center w-8 h-8 rounded-full bg-gradient-to-br from-amber-600 to-amber-800 text-amber-100 font-black text-sm shadow-md">🥉</span>`;

                let rowBg = isCurrent
                    ? 'bg-indigo-950/40 border-l-4 border-l-indigo-500'
                    : (isTop1 ? 'bg-amber-950/20 border-l-4 border-l-amber-500' : (isTop2 ? 'bg-slate-800/40 border-l-4 border-l-slate-400' : (isTop3 ? 'bg-amber-900/10 border-l-4 border-l-amber-700' : 'hover:bg-slate-900/60')));

                const pct = row.percentage;
                let pctBadge = `<span class="px-2.5 py-0.5 rounded-full text-[11px] font-extrabold border ${pct >= 80 ? 'bg-emerald-500/20 text-emerald-300 border-emerald-500/40' : (pct >= 50 ? 'bg-amber-500/20 text-amber-300 border-amber-500/40' : 'bg-rose-500/20 text-rose-300 border-rose-500/40')}">${pct}%</span>`;

                rowsHtml += `
                    <tr class="${rowBg} transition-colors">
                        <td class="py-3 px-4 text-center">${rankBadge}</td>
                        <td class="py-3 px-4 font-bold text-white">
                            <div class="flex items-center space-x-2">
                                <span class="w-6 h-6 rounded-full bg-indigo-500/20 border border-indigo-500/30 text-indigo-300 font-bold flex items-center justify-center text-[10px]">
                                    ${(row.student_name || 'S').charAt(0).toUpperCase()}
                                </span>
                                <span>${row.student_name}</span>
                                ${isCurrent ? '<span class="px-1.5 py-0.5 rounded text-[9px] font-black bg-indigo-500 text-white uppercase">You</span>' : ''}
                            </div>
                        </td>
                        <td class="py-3 px-4"><span class="px-2 py-0.5 rounded bg-slate-800 text-slate-300 border border-slate-700 text-[11px] font-medium">${row.student_class}</span></td>
                        <td class="py-3 px-4 text-center font-mono text-slate-300"><strong class="text-emerald-400">${row.correct_count}</strong> / ${row.total_questions} Qs</td>
                        <td class="py-3 px-4 text-center font-mono font-bold text-emerald-400 text-sm">${row.obtained_marks} / ${row.total_marks}</td>
                        <td class="py-3 px-4 text-center">${pctBadge}</td>
                        <td class="py-3 px-4 text-right text-slate-400 font-mono text-[11px]">${row.submitted_at || 'N/A'}</td>
                    </tr>
                `;
            });

            tbody.innerHTML = rowsHtml;
        })
        .catch(err => {
            console.error('Leaderboard Fetch Error:', err);
            loading.classList.add('hidden');
            empty.classList.remove('hidden');
        });
    }

    function closeExamLeaderboardModal() {
        const modal = document.getElementById('examLeaderboardModal');
        if (modal) modal.classList.add('hidden');
    }
</script>
