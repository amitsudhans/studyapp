import json
import html

with open('/home/lead-programmer/.gemini/antigravity/brain/a82d247f-53b7-4d46-bc5c-c38667735695/scratch/life_processes_content_slides.json', 'r') as f:
    content_slides = json.load(f)

with open('/home/lead-programmer/.gemini/antigravity/brain/a82d247f-53b7-4d46-bc5c-c38667735695/scratch/life_processes_quiz_slides.json', 'r') as f:
    quiz_slides = json.load(f)

all_slides = content_slides + quiz_slides
print(f"Total life-processes slides: {len(all_slides)}")

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NCERT Class 10 Science • Chapter 5: Life Processes Master Multimedia Lab</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- KaTeX CDN -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
        onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500;600&display=swap');
        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
        }
        .code-font {
            font-family: 'Fira Code', monospace;
        }
        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        ::-webkit-scrollbar-track {
            background: #0f172a;
        }
        ::-webkit-scrollbar-thumb {
            background: #334155;
            border-radius: 3px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #475569;
        }
        .slide-container {
            display: none;
        }
        .slide-container.active {
            display: block;
            animation: fadeIn 0.3s ease-in-out;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(6px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .pulse-glow {
            animation: pulseGlow 2s infinite;
        }
        @keyframes pulseGlow {
            0%, 100% { filter: drop-shadow(0 0 4px rgba(16, 185, 129, 0.6)); }
            50% { filter: drop-shadow(0 0 14px rgba(16, 185, 129, 0.95)); }
        }
        .heart-beat {
            animation: heartBeat 1s infinite ease-in-out;
        }
        @keyframes heartBeat {
            0%, 100% { transform: scale(1); }
            15% { transform: scale(1.08); }
            30% { transform: scale(1); }
            45% { transform: scale(1.05); }
        }
        .talking-mouth {
            animation: mouthTalk 0.25s infinite alternate ease-in-out;
        }
        @keyframes mouthTalk {
            0% { transform: scaleY(0.2); }
            100% { transform: scaleY(1.4); }
        }
        .teacher-bob {
            animation: teacherBob 3s infinite ease-in-out;
        }
        @keyframes teacherBob {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-4px); }
        }
        .modal-backdrop {
            background-color: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(8px);
        }
        .bubble-rise {
            animation: bubbleRise 2.2s infinite linear;
        }
        @keyframes bubbleRise {
            0% { transform: translateY(20px); opacity: 0; }
            50% { opacity: 0.8; }
            100% { transform: translateY(-40px); opacity: 0; }
        }
        .flow-blood {
            animation: bloodFlow 2s infinite linear;
        }
        @keyframes bloodFlow {
            0% { stroke-dashoffset: 40; }
            100% { stroke-dashoffset: 0; }
        }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col antialiased selection:bg-emerald-500 selection:text-white">

    <!-- Top Master Header -->
    <header class="sticky top-0 z-40 bg-slate-900/90 backdrop-blur-md border-b border-slate-800">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 py-3 flex items-center justify-between gap-4">
            <div class="flex items-center gap-3">
                <a href="/" class="p-2 rounded-xl bg-slate-800/80 hover:bg-slate-700/80 border border-slate-700 transition flex items-center justify-center text-slate-300 hover:text-white">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/></svg>
                </a>
                <div>
                    <div class="flex items-center gap-2">
                        <span class="px-2 py-0.5 rounded text-[10px] font-extrabold uppercase tracking-wide bg-gradient-to-r from-emerald-500 to-teal-600 text-white">Class 10 Science</span>
                        <span class="text-xs text-slate-400 font-medium">NCERT Chapter 5 • Person-Talking Teacher Animated Multimedia</span>
                    </div>
                    <h1 class="text-sm sm:text-base font-bold text-white tracking-tight">Life Processes (Complete Master Laboratory)</h1>
                </div>
            </div>

            <!-- Header Voice & Nav Controls -->
            <div class="flex items-center gap-2">
                <button id="voiceToggleBtn" onclick="toggleVoiceNarration()" class="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-emerald-600/20 text-emerald-300 hover:bg-emerald-600/30 border border-emerald-500/40 text-xs font-semibold transition">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"/></svg>
                    <span id="voiceStatusText">Teacher Voice: Active</span>
                </button>
                <button onclick="replayVoice()" title="Replay Teacher Narration" class="p-1.5 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700 hover:text-white border border-slate-700 transition">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/></svg>
                </button>
            </div>
        </div>
    </header>

    <!-- Main Presentation Workspace -->
    <main class="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 py-6 flex flex-col">
        __SLIDES_CONTENT__
    </main>

    <!-- Navigation Control Bar (Bottom Floating) -->
    <footer class="sticky bottom-0 z-40 bg-slate-900/95 backdrop-blur-md border-t border-slate-800 py-3">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 flex flex-col gap-2.5">
            <!-- Footer Scrollable Topic Pills -->
            <div class="flex items-center gap-1.5 overflow-x-auto pb-1 text-xs">
                __FOOTER_PILLS__
            </div>

            <div class="flex items-center justify-between gap-4 pt-1 border-t border-slate-800/60">
                <div class="flex items-center gap-2 text-xs font-mono text-slate-400">
                    <span>Slide</span>
                    <span id="currentSlideIndicator" class="px-2 py-0.5 rounded bg-slate-800 text-white font-bold">1</span>
                    <span>of</span>
                    <span id="totalSlidesIndicator" class="text-slate-300 font-bold">21</span>
                </div>

                <div class="flex items-center gap-3">
                    <button id="prevBtn" onclick="navigateSlide(-1)" class="flex items-center gap-1.5 px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold transition disabled:opacity-40 disabled:cursor-not-allowed">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
                        <span>Previous</span>
                    </button>
                    <button id="nextBtn" onclick="navigateSlide(1)" class="flex items-center gap-1.5 px-5 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition shadow-lg shadow-emerald-950/50">
                        <span>Next</span>
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                    </button>
                </div>
            </div>
        </div>
    </footer>

    <!-- Universal Quiz Solution Modal -->
    <div id="solutionModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 modal-backdrop">
        <div class="bg-slate-900 border border-slate-700 rounded-2xl max-w-xl w-full p-6 shadow-2xl relative max-h-[85vh] overflow-y-auto">
            <button onclick="closeSolutionModal()" class="absolute top-4 right-4 p-1.5 rounded-lg bg-slate-800 text-slate-400 hover:text-white hover:bg-slate-700 transition">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
            </button>
            <div class="flex items-center gap-2 mb-2">
                <span class="px-2.5 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">Step-by-Step Teacher Solution</span>
                <span id="modalQuestionId" class="text-xs text-slate-400 font-mono"></span>
            </div>
            <h3 id="modalQuestionTitle" class="text-sm font-semibold text-white mb-3 leading-snug"></h3>
            <div id="modalSolutionContent" class="text-xs sm:text-sm text-slate-300 bg-slate-950 p-4 rounded-xl border border-slate-800 leading-relaxed space-y-2">
            </div>
            <div class="mt-4 flex justify-end">
                <button onclick="closeSolutionModal()" class="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition">
                    Got it, Close
                </button>
            </div>
        </div>
    </div>

    <!-- Master Controller Script -->
    <script>
        const slidesData = __SLIDES_JSON__;
        let currentSlideIndex = 0;
        let voiceActive = true;
        let synth = window.speechSynthesis;
        let currentUtterance = null;
        let audioCtx = null;

        function getAudioContext() {
            if (!audioCtx) {
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            }
            if (audioCtx.state === 'suspended') {
                audioCtx.resume();
            }
            return audioCtx;
        }

        function playTone(freq, type = 'sine', duration = 0.15) {
            try {
                const ctx = getAudioContext();
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                osc.type = type;
                osc.frequency.setValueAtTime(freq, ctx.currentTime);
                gain.gain.setValueAtTime(0.08, ctx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start();
                osc.stop(ctx.currentTime + duration);
            } catch (e) {
                console.warn("Web Audio tone error:", e);
            }
        }

        function playCorrectSound() {
            playTone(523.25, 'triangle', 0.1);
            setTimeout(() => playTone(659.25, 'triangle', 0.1), 100);
            setTimeout(() => playTone(783.99, 'triangle', 0.2), 200);
        }

        function playIncorrectSound() {
            playTone(330, 'sawtooth', 0.15);
            setTimeout(() => playTone(280, 'sawtooth', 0.25), 120);
        }

        function playHeartbeatSound() {
            playTone(120, 'sine', 0.1);
            setTimeout(() => playTone(95, 'sine', 0.15), 180);
        }

        function playSlideClickSound() {
            playTone(440, 'sine', 0.08);
        }

        function setTeacherTalking(isTalking) {
            const mouth = document.getElementById(`teacherMouth-${currentSlideIndex}`);
            if (mouth) {
                if (isTalking) {
                    mouth.classList.add('talking-mouth');
                } else {
                    mouth.classList.remove('talking-mouth');
                }
            }
        }

        function speakText(text) {
            if (!voiceActive || !synth) return;
            synth.cancel();
            const cleanText = text.replace(/<[^>]*>/g, '').replace(/\\$/g, '').replace(/\\\[|\\\]|\\\(|\\\)/g, '');
            currentUtterance = new SpeechSynthesisUtterance(cleanText);
            currentUtterance.rate = 1.0;
            currentUtterance.pitch = 1.08;
            
            const voices = synth.getVoices();
            const preferred = voices.find(v => v.lang.startsWith('en') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Samantha') || v.name.includes('Teacher')));
            if (preferred) currentUtterance.voice = preferred;

            currentUtterance.onstart = () => {
                setTeacherTalking(true);
            };
            currentUtterance.onend = () => {
                setTeacherTalking(false);
            };
            currentUtterance.onerror = () => {
                setTeacherTalking(false);
            };

            synth.speak(currentUtterance);
        }

        function toggleVoiceNarration() {
            voiceActive = !voiceActive;
            const statusText = document.getElementById('voiceStatusText');
            if (voiceActive) {
                statusText.textContent = "Teacher Voice: Active";
                document.getElementById('voiceToggleBtn').className = "flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-emerald-600/20 text-emerald-300 hover:bg-emerald-600/30 border border-emerald-500/40 text-xs font-semibold transition";
                playTone(660, 'sine', 0.1);
                replayVoice();
            } else {
                statusText.textContent = "Teacher Voice: Muted";
                document.getElementById('voiceToggleBtn').className = "flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-800 text-slate-400 hover:bg-slate-700 border border-slate-700 text-xs font-semibold transition";
                if (synth) synth.cancel();
                setTeacherTalking(false);
                playTone(330, 'sine', 0.1);
            }
        }

        function replayVoice() {
            const slide = slidesData[currentSlideIndex];
            if (slide && slide.narration) {
                speakText(slide.narration);
            }
        }

        function navigateSlide(direction) {
            const newIndex = currentSlideIndex + direction;
            if (newIndex >= 0 && newIndex < slidesData.length) {
                goToSlide(newIndex);
            }
        }

        function goToSlide(index) {
            playSlideClickSound();
            if (synth) synth.cancel();
            setTeacherTalking(false);

            const currentEl = document.getElementById(`slide-${currentSlideIndex}`);
            if (currentEl) currentEl.classList.remove('active');

            const currentPill = document.getElementById(`pill-${currentSlideIndex}`);
            if (currentPill) {
                currentPill.classList.remove('bg-emerald-600', 'text-white', 'font-bold');
                currentPill.classList.add('bg-slate-800', 'text-slate-300');
            }

            currentSlideIndex = index;
            const newEl = document.getElementById(`slide-${currentSlideIndex}`);
            if (newEl) newEl.classList.add('active');

            const newPill = document.getElementById(`pill-${currentSlideIndex}`);
            if (newPill) {
                newPill.classList.remove('bg-slate-800', 'text-slate-300');
                newPill.classList.add('bg-emerald-600', 'text-white', 'font-bold');
                newPill.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
            }

            document.getElementById('currentSlideIndicator').textContent = currentSlideIndex + 1;
            document.getElementById('prevBtn').disabled = (currentSlideIndex === 0);

            // Hide next button on last slide (Slide 21 / index 20)
            const nextBtn = document.getElementById('nextBtn');
            if (currentSlideIndex === slidesData.length - 1) {
                nextBtn.style.display = 'none';
            } else {
                nextBtn.style.display = 'flex';
            }

            replayVoice();

            if (window.renderMathInElement) {
                renderMathInElement(newEl, {
                    delimiters: [
                        {left: '$$', right: '$$', display: true},
                        {left: '$', right: '$', display: false}
                    ]
                });
            }
        }

        function checkCheckpointAnswer(slideIdx, qIdx, selectedOption, correctOption, solutionId) {
            const solEl = document.getElementById(solutionId);
            const feedbackEl = document.getElementById(`feedback-${slideIdx}-${qIdx}`);
            
            if (selectedOption === correctOption) {
                playCorrectSound();
                if (feedbackEl) feedbackEl.innerHTML = `<span class="inline-flex items-center gap-1 text-emerald-400 font-bold text-xs"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Correct! Excellent</span>`;
                if (solEl) solEl.classList.remove('hidden');
            } else {
                playIncorrectSound();
                if (feedbackEl) feedbackEl.innerHTML = `<span class="inline-flex items-center gap-1 text-rose-400 font-bold text-xs"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg> Incorrect. Solution below</span>`;
                if (solEl) solEl.classList.remove('hidden');
            }
        }

        function openQuizSolution(qId, title, solutionHtml) {
            playTone(550, 'sine', 0.1);
            document.getElementById('modalQuestionId').textContent = `Question ${qId} Solution`;
            document.getElementById('modalQuestionTitle').textContent = title;
            const solEl = document.getElementById('modalSolutionContent');
            solEl.innerHTML = solutionHtml;
            document.getElementById('solutionModal').classList.remove('hidden');

            if (window.renderMathInElement) {
                renderMathInElement(solEl, {
                    delimiters: [
                        {left: '$$', right: '$$', display: true},
                        {left: '$', right: '$', display: false}
                    ]
                });
            }
        }

        function closeSolutionModal() {
            playTone(400, 'sine', 0.08);
            document.getElementById('solutionModal').classList.add('hidden');
        }

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') closeSolutionModal();
            if (e.key === 'ArrowRight' && currentSlideIndex < slidesData.length - 1) navigateSlide(1);
            if (e.key === 'ArrowLeft' && currentSlideIndex > 0) navigateSlide(-1);
        });

        // ==========================================
        // 17 INTERACTIVE LAB SIMULATORS
        // ==========================================

        // 1. Molecular Movement vs Virus (Slide 0)
        let isMoleculeActive = false;
        function toggleMolecularMotion() {
            isMoleculeActive = !isMoleculeActive;
            const molGroup = document.getElementById('cellMolecules');
            const status = document.getElementById('moleculeStatus');
            const btn = document.getElementById('moleculeBtn');

            if (isMoleculeActive) {
                molGroup.classList.remove('hidden');
                btn.textContent = "Freeze Molecules (Inanimate State)";
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Living Cell:</span> Active molecular shuttling repairs structures and maintains order!";
                playTone(650, 'triangle', 0.2);
            } else {
                molGroup.classList.add('hidden');
                btn.textContent = "Simulate Living Molecular Movement";
                status.innerHTML = "<span class='text-amber-400 font-bold'>Dormant Virus / Inanimate:</span> Zero intrinsic molecular movement until infecting a host cell!";
                playTone(400, 'sine', 0.1);
            }
        }

        // 2. Photosynthesis Solar Converter (Slide 1)
        function triggerSolarHarvest() {
            const photon = document.getElementById('solarRay');
            const o2 = document.getElementById('oxygenBubble');
            const starch = document.getElementById('starchStore');
            const status = document.getElementById('photoStatus');
            photon.classList.remove('hidden');
            o2.classList.remove('hidden');
            starch.classList.remove('hidden');
            status.innerHTML = "<span class='text-emerald-400 font-bold'>Photosynthesis in Action!</span> Chlorophyll absorbs photons; water is split ($O_2\\uparrow$) and $CO_2$ is reduced to starch!";
            playTone(750, 'sine', 0.25);
        }

        // 3. Variegated Leaf Iodine Test (Slide 2)
        let isStarchTested = false;
        function toggleLeafIodine() {
            isStarchTested = !isStarchTested;
            const greenZone = document.getElementById('leafGreenZone');
            const whiteZone = document.getElementById('leafWhiteZone');
            const status = document.getElementById('leafStatus');
            const btn = document.getElementById('leafBtn');

            if (isStarchTested) {
                greenZone.setAttribute('fill', '#1e1b4b'); // Blue-black
                whiteZone.setAttribute('fill', '#fef08a'); // Pale yellow iodine
                btn.textContent = "Reset Variegated Leaf";
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Iodine Test Positive!</span> Green areas (with chlorophyll) turn <strong>BLUE-BLACK</strong> with starch!";
                playTone(700, 'sine', 0.2);
            } else {
                greenZone.setAttribute('fill', '#22c55e'); // Green
                whiteZone.setAttribute('fill', '#fef9c3'); // White croton patch
                btn.textContent = "Dip in Iodine Solution";
                status.innerHTML = "Variegated leaf (money plant / croton) with green and white zones.";
                playTone(450, 'sine', 0.1);
            }
        }

        // 4. Stomata Guard Cells & KOH Bell-Jar (Slide 3)
        let isStomaOpen = false;
        function toggleStomatalPore() {
            isStomaOpen = !isStomaOpen;
            const leftGuard = document.getElementById('leftGuardCell');
            const rightGuard = document.getElementById('rightGuardCell');
            const pore = document.getElementById('stomaPore');
            const status = document.getElementById('stomaStatus');
            const btn = document.getElementById('stomaBtn');

            if (isStomaOpen) {
                pore.setAttribute('width', '24');
                leftGuard.setAttribute('cx', '138');
                rightGuard.setAttribute('cx', '182');
                btn.textContent = "Lose Water (Shrink & Close Pore)";
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Guard Cells Turgid & Swollen!</span> Water flows in; pore bows open for $CO_2$ uptake.";
                playTone(600, 'triangle', 0.2);
            } else {
                pore.setAttribute('width', '4');
                leftGuard.setAttribute('cx', '150');
                rightGuard.setAttribute('cx', '170');
                btn.textContent = "Absorb Water (Swell & Open Pore)";
                status.innerHTML = "<span class='text-amber-300 font-bold'>Guard Cells Flaccid & Shrunk!</span> Stomatal pore closes tightly to halt transpiration water loss.";
                playTone(400, 'sine', 0.1);
            }
        }

        // 5. Heterotrophic Modes (Slide 4)
        function selectNutritionMode(mode) {
            const status = document.getElementById('heteroStatus');
            if (mode === 'saprophyte') {
                status.innerHTML = "<span class='text-amber-300 font-bold'>Saprophytic Mode (Bread Mould / Mushroom):</span> Digestive enzymes secreted externally; absorbs liquefied nutrients.";
                playTone(550, 'sine', 0.15);
            } else if (mode === 'parasite') {
                status.innerHTML = "<span class='text-rose-400 font-bold'>Parasitic Mode (Cuscuta / Tapeworm):</span> Siphons nutrients directly from living host without killing it!";
                playTone(480, 'sine', 0.15);
            } else {
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Holozoic Mode (Humans / Amoeba):</span> Ingests solid food internally for digestion, absorption, and assimilation.";
                playTone(650, 'sine', 0.15);
            }
        }

        // 6. Amoeba Phagocytosis (Slide 5)
        let amoebaStep = 0;
        function advanceAmoeba() {
            amoebaStep = (amoebaStep + 1) % 4;
            const status = document.getElementById('amoebaStatus');
            const armL = document.getElementById('pseudoArmL');
            const armR = document.getElementById('pseudoArmR');
            const food = document.getElementById('amoebaFood');

            if (amoebaStep === 1) {
                armL.setAttribute('d', 'M110 80 Q140 40 160 55');
                armR.setAttribute('d', 'M210 80 Q180 40 160 55');
                status.innerHTML = "<span class='text-amber-300 font-bold'>1. Pseudopodia Extension:</span> False feet flow around the detected food particle.";
                playTone(500, 'sine', 0.15);
            } else if (amoebaStep === 2) {
                armL.setAttribute('d', 'M110 80 Q150 35 160 50');
                armR.setAttribute('d', 'M210 80 Q170 35 160 50');
                food.setAttribute('cy', '75');
                status.innerHTML = "<span class='text-emerald-400 font-bold'>2. Food-Vacuole Fused:</span> Pseudopodia fuse over particle, enclosing it inside vacuole.";
                playTone(600, 'triangle', 0.2);
            } else if (amoebaStep === 3) {
                food.setAttribute('r', '2');
                status.innerHTML = "<span class='text-emerald-400 font-bold'>3. Digestion & Diffusion:</span> Enzymes hydrolyse food; nutrients diffuse into cytoplasm; wastes expelled.";
                playTone(700, 'sine', 0.2);
            } else {
                armL.setAttribute('d', 'M120 80 Q130 60 140 70');
                armR.setAttribute('d', 'M200 80 Q190 60 180 70');
                food.setAttribute('r', '6');
                food.setAttribute('cy', '50');
                status.innerHTML = "Amoeba approaching fresh food particle.";
                playTone(400, 'sine', 0.1);
            }
        }

        // 7. Salivary Amylase & Peristalsis (Slide 6)
        let bolusPos = 35;
        function advancePeristalsis() {
            bolusPos = (bolusPos >= 130) ? 35 : bolusPos + 30;
            const bolus = document.getElementById('foodBolus');
            const status = document.getElementById('peristalsisStatus');
            bolus.setAttribute('cy', bolusPos);
            status.innerHTML = `<span class='text-amber-300 font-bold'>Peristaltic Wave:</span> Circular muscles squeeze behind bolus, pushing it down oesophagus (${bolusPos}px).`;
            playTone(500 + bolusPos * 2, 'sine', 0.12);
        }

        // 8. Stomach Acid & Villi (Slide 7)
        function triggerStomachDigest() {
            const pepsin = document.getElementById('pepsinBubbles');
            const status = document.getElementById('stomachStatus');
            pepsin.classList.remove('hidden');
            status.innerHTML = "<span class='text-rose-400 font-bold'>Stomach Secretions:</span> $HCl$ ($pH \\approx 1.8$) activates Pepsin; proteins digested while mucus coats lining!";
            playTone(600, 'triangle', 0.25);

            if (window.renderMathInElement) {
                renderMathInElement(status, { delimiters: [{left: '$', right: '$', display: false}] });
            }
        }

        // 9. Lime Water Exhalation vs Syringe (Slide 8)
        function testLimeWaterBreath(isHuman) {
            const liquid = document.getElementById('respirLiquid');
            const status = document.getElementById('respirStatus');

            if (isHuman) {
                liquid.setAttribute('fill', '#f1f5f9');
                liquid.setAttribute('fill-opacity', '0.9');
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Human Breath (Activity 5.4):</span> Exhaled air is rich in $CO_2$ (~4.4%), turning lime water milky in seconds!";
                playTone(650, 'sine', 0.2);
            } else {
                liquid.setAttribute('fill', '#38bdf8');
                liquid.setAttribute('fill-opacity', '0.2');
                status.innerHTML = "<span class='text-sky-300 font-bold'>Syringe Ambient Air:</span> Atmospheric air has only ~0.04% $CO_2$; lime water remains clear for a long time.";
                playTone(400, 'sine', 0.1);
            }
        }

        // 10. Glucose 3 Pathways (Slide 9)
        function selectRespirationPathway(pathway) {
            const status = document.getElementById('pathwayStatus');
            if (pathway === 'mitochondria') {
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Presence of Oxygen (Mitochondria):</span> $6CO_2 + 6H_2O$ + Massive ATP Energy! (Aerobic Respiration)";
                playTone(750, 'triangle', 0.25);
            } else if (pathway === 'muscle') {
                status.innerHTML = "<span class='text-rose-400 font-bold'>Lack of Oxygen (Muscle Cells during sprint):</span> Pyruvate $\\to$ Lactic acid + Energy. Causes painful muscle cramps!";
                playTone(350, 'sawtooth', 0.25);
            } else {
                status.innerHTML = "<span class='text-amber-300 font-bold'>Absence of Oxygen (Yeast Fermentation):</span> Pyruvate $\\to$ Ethanol ($C_2H_5OH$) + $CO_2$ + 2 ATP!";
                playTone(550, 'sine', 0.2);
            }

            if (window.renderMathInElement) {
                renderMathInElement(status, { delimiters: [{left: '$', right: '$', display: false}] });
            }
        }

        // 11. Fish Gills vs Human Cartilage Trachea (Slide 10)
        function triggerGillIrrigation() {
            const waterFlow = document.getElementById('gillWaterFlow');
            const status = document.getElementById('gillStatus');
            waterFlow.classList.remove('hidden');
            status.innerHTML = "<span class='text-sky-300 font-bold'>Fish Gill Irrigation:</span> Water forced past gills rapidly because dissolved $O_2$ is very low compared to air!";
            playTone(620, 'sine', 0.2);
        }

        // 12. Alveoli Gas Diffusion (Slide 11)
        let isAlveolusInflated = false;
        function toggleAlveolus() {
            isAlveolusInflated = !isAlveolusInflated;
            const alv = document.getElementById('alveolusSac');
            const o2 = document.getElementById('alvO2');
            const co2 = document.getElementById('alvCO2');
            const status = document.getElementById('alvStatus');
            const btn = document.getElementById('alvBtn');

            if (isAlveolusInflated) {
                alv.setAttribute('r', '42');
                o2.classList.remove('hidden');
                co2.classList.remove('hidden');
                btn.textContent = "Exhale (Deflate Alveolus)";
                status.innerHTML = "<span class='text-emerald-400 font-bold'>Inspiration:</span> 80 m² alveolar surface inflates! $O_2$ diffuses into RBC haemoglobin; $CO_2$ diffuses into alveolus!";
                playTone(680, 'sine', 0.2);
            } else {
                alv.setAttribute('r', '30');
                o2.classList.add('hidden');
                co2.classList.add('hidden');
                btn.textContent = "Inhale (Inflate Alveolus)";
                status.innerHTML = "Resting alveolus wrapped in pulmonary capillary meshwork.";
                playTone(420, 'sine', 0.1);
            }
        }

        // 13. Beating Heart & Double Circulation (Slide 12)
        function pumpHeartCycle() {
            playHeartbeatSound();
            const heart = document.getElementById('heartSvg');
            const status = document.getElementById('heartStatus');
            heart.classList.add('heart-beat');
            status.innerHTML = "<span class='text-rose-400 font-bold'>Systole & Double Circulation:</span> Left ventricle pumps oxygenated blood to body; Right ventricle pumps deoxygenated blood to lungs!";
            setTimeout(() => heart.classList.remove('heart-beat'), 1200);
        }

        // 14. Sphygmomanometer Cuff (Slide 13)
        let cuffPressure = 80;
        function pumpCuff() {
            cuffPressure = (cuffPressure >= 160) ? 80 : cuffPressure + 40;
            const needle = document.getElementById('cuffNeedle');
            const status = document.getElementById('bpStatus');
            needle.setAttribute('transform', `rotate(${(cuffPressure - 80) * 1.5} 160 100)`);
            status.innerHTML = `<span class='text-amber-300 font-bold'>Cuff Pressure: ${cuffPressure} mm Hg</span> (Normal Systolic ~120 mm Hg, Diastolic ~80 mm Hg).`;
            playTone(300 + cuffPressure * 2, 'sine', 0.12);
        }

        // 15. Transpiration Pull Tree (Slide 14)
        function triggerTranspirationPull() {
            const drop = document.getElementById('transpireDrop');
            const col = document.getElementById('xylemWaterColumn');
            const status = document.getElementById('treeStatus');
            drop.classList.remove('hidden');
            col.setAttribute('stroke', '#38bdf8');
            status.innerHTML = "<span class='text-emerald-400 font-bold'>Transpiration Pull Active!</span> Evaporation from stomata pulls continuous water column hundreds of feet up tree!";
            playTone(700, 'sine', 0.25);
        }

        // 16. Phloem Pressure Flow (Slide 15)
        function triggerPhloemFlow() {
            const sucrose = document.getElementById('phloemSugar');
            const status = document.getElementById('phloemStatus');
            sucrose.classList.remove('hidden');
            status.innerHTML = "<span class='text-amber-300 font-bold'>ATP Pressure Flow:</span> Sucrose actively loaded into sieve tubes; osmotic pressure drives bulk sap to growing buds and roots!";
            playTone(660, 'triangle', 0.2);
        }

        // 17. Nephron & Hemodialysis (Slide 16)
        function triggerNephronFilter() {
            const filt = document.getElementById('nephronFiltrate');
            const reabs = document.getElementById('reabsorbArrow');
            const status = document.getElementById('nephronStatus');
            filt.classList.remove('hidden');
            reabs.classList.remove('hidden');
            status.innerHTML = "<span class='text-emerald-400 font-bold'>Glomerular Ultrafiltration:</span> 180 L filtered daily! >99% water, glucose, and salts reabsorbed; only 1-2 L excreted as urine!";
            playTone(720, 'sine', 0.25);
        }

        window.addEventListener('DOMContentLoaded', () => {
            goToSlide(0);
        });
    </script>
</body>
</html>
"""

# Slide Card Generator
slides_html = []
pills_html = []

for idx, s in enumerate(all_slides):
    is_quiz = (idx >= 17)
    pill_text = s.get('short_title', f"S{idx+1}")
    pills_html.append(f"""
        <button id="pill-{idx}" onclick="goToSlide({idx})" class="px-2.5 py-1 rounded-md bg-slate-800 text-slate-300 hover:bg-slate-700 transition whitespace-nowrap text-xs">
            {html.escape(pill_text)}
        </button>
    """)

    if not is_quiz:
        theory_cards_html = ""
        for tb in s.get('theory_blocks', []):
            theory_cards_html += f"""
                <div class="bg-slate-900/80 border border-slate-800/80 rounded-xl p-4 hover:border-slate-700 transition">
                    <h4 class="text-xs font-bold uppercase tracking-wider text-emerald-400 mb-1.5 flex items-center gap-1.5">
                        <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
                        {tb['heading']}
                    </h4>
                    <div class="text-xs sm:text-sm text-slate-300 leading-relaxed space-y-1.5">
                        {tb['content']}
                    </div>
                </div>
            """

        checkpoints_html = ""
        for q_idx, cp in enumerate(s.get('checkpoints', [])):
            opts_html = ""
            for o_idx, opt in enumerate(cp['options']):
                opts_html += f"""
                    <label class="flex items-start gap-2.5 p-2 rounded-lg bg-slate-950/70 border border-slate-800 hover:border-slate-700 cursor-pointer text-xs transition">
                        <input type="radio" name="chk-{idx}-{q_idx}" value="{o_idx}" onchange="checkCheckpointAnswer({idx}, {q_idx}, {o_idx}, {cp['ans']}, 'chk-sol-{idx}-{q_idx}')" class="mt-0.5 text-emerald-600 focus:ring-emerald-500 bg-slate-900 border-slate-700">
                        <span class="text-slate-300">{html.escape(opt)}</span>
                    </label>
                """
            checkpoints_html += f"""
                <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-4 mb-3">
                    <div class="flex items-center justify-between gap-2 mb-2">
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Checkpoint {q_idx + 1} of 2</span>
                        <div id="feedback-{idx}-{q_idx}"></div>
                    </div>
                    <p class="text-xs sm:text-sm font-semibold text-white mb-2.5">{cp['q']}</p>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 mb-2">
                        {opts_html}
                    </div>
                    <div id="chk-sol-{idx}-{q_idx}" class="hidden mt-2.5 p-3 rounded-lg bg-emerald-950/30 border border-emerald-500/30 text-xs text-slate-200">
                        <span class="font-bold text-emerald-400">Step-by-Step Teacher Explanation:</span><br>
                        {cp['solution']}
                    </div>
                </div>
            """

        # Interactive SVG/Card Component
        interactive_html = ""
        itype = s.get('interactive_type', 'default')

        if itype == "molecular_virus_sim":
            interactive_html = """
                <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-xl">
                    <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
                        <h4 class="text-xs sm:text-sm font-bold text-white uppercase tracking-wider">Molecular Movement vs Dormant Virus</h4>
                    </div>
                    <div id="moleculeStatus" class="text-xs text-slate-300 mb-3 bg-slate-950 p-2.5 rounded-lg border border-slate-800">
                        Living cells constantly shuttle molecules for repair against environmental breakdown.
                    </div>
                    <div class="bg-slate-950 rounded-xl p-2 border border-slate-800 mb-3 flex justify-center">
                        <svg viewBox="0 0 320 160" class="w-full h-36 sm:h-44">
                            <!-- Cell boundary -->
                            <rect x="40" y="30" width="110" height="100" rx="20" fill="#065f46" fill-opacity="0.25" stroke="#10b981" stroke-width="2"/>
                            <text x="50" y="50" fill="#34d399" font-size="9" font-weight="bold">LIVING CELL</text>
                            <!-- Molecular Motion Particles -->
                            <g id="cellMolecules" class="hidden">
                                <circle cx="70" cy="75" r="4" fill="#facc15" class="bubble-rise"/>
                                <circle cx="95" cy="95" r="3" fill="#38bdf8" class="bubble-rise"/>
                                <circle cx="120" cy="65" r="3.5" fill="#f43f5e" class="bubble-rise"/>
                            </g>
                            <!-- Virus Particle -->
                            <polygon points="230,50 255,65 255,95 230,110 205,95 205,65" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
                            <circle cx="230" cy="80" r="10" fill="#475569"/>
                            <text x="210" y="130" fill="#94a3b8" font-size="9" font-weight="bold">VIRUS (INERT)</text>
                        </svg>
                    </div>
                    <button id="moleculeBtn" onclick="toggleMolecularMotion()" class="w-full py-2 px-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition shadow-lg shadow-emerald-950/40">
                        Simulate Living Molecular Movement
                    </button>
                </div>
            """
        elif itype == "photosynthesis_solar_sim":
            interactive_html = """
                <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-xl">
                    <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
                        <h4 class="text-xs sm:text-sm font-bold text-white uppercase tracking-wider">The Photosynthesis Solar Energy Converter</h4>
                    </div>
                    <div id="photoStatus" class="text-xs text-slate-300 mb-3 bg-slate-950 p-2.5 rounded-lg border border-slate-800">
                        Chlorophyll absorbs sunlight; water splits and CO₂ reduces to starch.
                    </div>
                    <div class="bg-slate-950 rounded-xl p-2 border border-slate-800 mb-3 flex justify-center">
                        <svg viewBox="0 0 320 160" class="w-full h-36 sm:h-44">
                            <!-- Sun -->
                            <circle cx="50" cy="40" r="18" fill="#facc15" class="pulse-glow"/>
                            <!-- Solar ray beam -->
                            <line id="solarRay" x1="68" y1="50" x2="150" y2="90" stroke="#fef08a" stroke-width="3" stroke-dasharray="4,4" class="hidden"/>
                            <!-- Chloroplast leaf cell -->
                            <ellipse cx="160" cy="100" rx="60" ry="35" fill="#047857" stroke="#10b981" stroke-width="2"/>
                            <text x="130" y="95" fill="#a7f3d0" font-size="9" font-weight="bold">CHLOROPLAST</text>
                            <!-- O2 Bubble -->
                            <g id="oxygenBubble" class="hidden">
                                <circle cx="250" cy="60" r="14" fill="#38bdf8" fill-opacity="0.3" stroke="#38bdf8" stroke-width="2" class="bubble-rise"/>
                                <text x="242" y="64" fill="#ffffff" font-size="9" font-weight="bold">O₂↑</text>
                            </g>
                            <!-- Starch granule -->
                            <ellipse id="starchStore" cx="160" cy="115" rx="20" ry="8" fill="#fef08a" class="hidden pulse-glow"/>
                        </svg>
                    </div>
                    <button onclick="triggerSolarHarvest()" class="w-full py-2 px-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition shadow-lg shadow-emerald-950/40">
                        Illuminate with Solar Photons (Synthesize Starch)
                    </button>
                </div>
            """
        elif itype == "variegated_iodine_leaf_sim":
            interactive_html = """
                <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-xl">
                    <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
                        <h4 class="text-xs sm:text-sm font-bold text-white uppercase tracking-wider">Activity 5.1: Variegated Leaf Iodine Starch Test</h4>
                    </div>
                    <div id="leafStatus" class="text-xs text-slate-300 mb-3 bg-slate-950 p-2.5 rounded-lg border border-slate-800">
                        Variegated leaf (money plant / croton) with green and white zones.
                    </div>
                    <div class="bg-slate-950 rounded-xl p-2 border border-slate-800 mb-3 flex justify-center">
                        <svg viewBox="0 0 320 160" class="w-full h-36 sm:h-44">
                            <!-- Leaf shape -->
                            <path d="M160 20 C230 40, 240 120, 160 145 C80 120, 90 40, 160 20 Z" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
                            <!-- White non-chlorophyll outer zone -->
                            <path id="leafWhiteZone" d="M160 22 C225 42, 235 118, 160 143 C85 118, 95 42, 160 22 Z" fill="#fef9c3" class="transition-colors duration-700"/>
                            <!-- Green chlorophyll inner zone -->
                            <path id="leafGreenZone" d="M160 40 C195 55, 200 105, 160 125 C120 105, 125 55, 160 40 Z" fill="#22c55e" class="transition-colors duration-700"/>
                            <text x="135" y="85" fill="#ffffff" font-size="9" font-weight="bold">CHLOROPHYLL</text>
                        </svg>
                    </div>
                    <button id="leafBtn" onclick="toggleLeafIodine()" class="w-full py-2 px-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition shadow-lg shadow-emerald-950/40">
                        Dip in Iodine Solution (Test Starch)
                    </button>
                </div>
            """
        elif itype == "stomata_koh_belljar_sim":
            interactive_html = """
                <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-xl">
                    <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
                        <h4 class="text-xs sm:text-sm font-bold text-white uppercase tracking-wider">Fig 5.3: Stomatal Guard Cell Hydraulic Mechanics</h4>
                    </div>
                    <div id="stomaStatus" class="text-xs text-slate-300 mb-3 bg-slate-950 p-2.5 rounded-lg border border-slate-800">
                        Guard cells control pore opening and closing via osmotic turgor pressure.
                    </div>
                    <div class="bg-slate-950 rounded-xl p-2 border border-slate-800 mb-3 flex justify-center">
                        <svg viewBox="0 0 320 160" class="w-full h-36 sm:h-44">
                            <!-- Left Guard Cell -->
                            <ellipse id="leftGuardCell" cx="150" cy="80" rx="16" ry="38" fill="#10b981" stroke="#047857" stroke-width="2" class="transition-all duration-500"/>
                            <!-- Right Guard Cell -->
                            <ellipse id="rightGuardCell" cx="170" cy="80" rx="16" ry="38" fill="#10b981" stroke="#047857" stroke-width="2" class="transition-all duration-500"/>
                            <!-- Pore aperture -->
                            <rect id="stomaPore" x="158" y="55" width="4" height="50" rx="2" fill="#0f172a" class="transition-all duration-500"/>
                            <text x="140" y="140" fill="#6ee7b7" font-size="9" font-weight="bold">STOMATAL PORE</text>
                        </svg>
                    </div>
                    <button id="stomaBtn" onclick="toggleStomatalPore()" class="w-full py-2 px-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition shadow-lg shadow-emerald-950/40">
                        Absorb Water (Swell & Open Pore)
                    </button>
                </div>
            """
        elif itype == "nutrition_modes_matcher_sim":
            interactive_html = """
                <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-xl">
                    <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
                        <h4 class="text-xs sm:text-sm font-bold text-white uppercase tracking-wider">Heterotrophic Modes: Saprophytic vs Parasitic vs Holozoic</h4>
                    </div>
                    <div id="heteroStatus" class="text-xs text-slate-300 mb-3 bg-slate-950 p-2.5 rounded-lg border border-slate-800">
                        Select a heterotrophic strategy to see its ecological feeding mechanism.
                    </div>
                    <div class="grid grid-cols-3 gap-2">
                        <button onclick="selectNutritionMode('saprophyte')" class="p-3 rounded-xl bg-slate-950 hover:bg-slate-800 border border-slate-800 text-left transition">
                            <span class="text-xs font-bold text-amber-300 block mb-1">Saprophytic</span>
                            <span class="text-[10px] text-slate-400">Bread mould, yeast, mushroom (external digestion).</span>
                        </button>
                        <button onclick="selectNutritionMode('parasite')" class="p-3 rounded-xl bg-slate-950 hover:bg-slate-800 border border-slate-800 text-left transition">
                            <span class="text-xs font-bold text-rose-400 block mb-1">Parasitic</span>
                            <span class="text-[10px] text-slate-400">Cuscuta, ticks, leeches, tapeworms (feed on live host).</span>
                        </button>
                        <button onclick="selectNutritionMode('holozoic')" class="p-3 rounded-xl bg-slate-950 hover:bg-slate-800 border border-slate-800 text-left transition">
                            <span class="text-xs font-bold text-emerald-300 block mb-1">Holozoic</span>
                            <span class="text-[10px] text-slate-400">Humans, Amoeba (internal ingestion & digestion).</span>
                        </button>
                    </div>
                </div>
            """
        elif itype == "amoeba_pseudopodia_anim_sim":
            interactive_html = """
                <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-xl">
                    <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
                        <h4 class="text-xs sm:text-sm font-bold text-white uppercase tracking-wider">Fig 5.5: Amoeba Phagocytosis & Food-Vacuole</h4>
                    </div>
                    <div id="amoebaStatus" class="text-xs text-slate-300 mb-3 bg-slate-950 p-2.5 rounded-lg border border-slate-800">
                        Amoeba approaching fresh food particle.
                    </div>
                    <div class="bg-slate-950 rounded-xl p-2 border border-slate-800 mb-3 flex justify-center">
                        <svg viewBox="0 0 320 160" class="w-full h-36 sm:h-44">
                            <!-- Amoeba body -->
                            <path d="M90 100 Q60 60 100 40 Q160 20 220 50 Q260 80 230 120 Q160 150 90 100 Z" fill="#047857" fill-opacity="0.3" stroke="#10b981" stroke-width="2"/>
                            <circle cx="120" cy="90" r="12" fill="#065f46" stroke="#34d399" stroke-width="1.5"/>
                            <text x="110" y="93" fill="#a7f3d0" font-size="8">Nucleus</text>
                            <!-- Pseudopodia Arms -->
                            <path id="pseudoArmL" d="M120 80 Q130 60 140 70" fill="none" stroke="#10b981" stroke-width="6" stroke-linecap="round" class="transition-all duration-500"/>
                            <path id="pseudoArmR" d="M200 80 Q190 60 180 70" fill="none" stroke="#10b981" stroke-width="6" stroke-linecap="round" class="transition-all duration-500"/>
                            <!-- Food Particle -->
                            <circle id="amoebaFood" cx="160" cy="50" r="6" fill="#f59e0b" class="transition-all duration-500 pulse-glow"/>
                        </svg>
                    </div>
                    <button onclick="advanceAmoeba()" class="w-full py-2 px-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition shadow-lg shadow-emerald-950/40">
                        Step Forward Phagocytosis
                    </button>
                </div>
            """
        elif itype == "peristalsis_bolus_sim":
            interactive_html = """
                <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-xl">
                    <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
                        <h4 class="text-xs sm:text-sm font-bold text-white uppercase tracking-wider">Peristaltic Waves in Oesophagus & Salivary Amylase</h4>
                    </div>
                    <div id="peristalsisStatus" class="text-xs text-slate-300 mb-3 bg-slate-950 p-2.5 rounded-lg border border-slate-800">
                        Click button to trigger muscular peristaltic wave pushing food bolus down gut.
                    </div>
                    <div class="bg-slate-950 rounded-xl p-2 border border-slate-800 mb-3 flex justify-center">
                        <svg viewBox="0 0 320 160" class="w-full h-36 sm:h-44">
                            <!-- Oesophagus muscular tube -->
                            <path d="M135 10 L135 150" stroke="#f43f5e" stroke-width="4" stroke-linecap="round"/>
                            <path d="M185 10 L185 150" stroke="#f43f5e" stroke-width="4" stroke-linecap="round"/>
                            <text x="195" y="80" fill="#fda4af" font-size="9">Oesophagus</text>
                            <!-- Food Bolus -->
                            <circle id="foodBolus" cx="160" cy="35" r="14" fill="#f59e0b" stroke="#d97706" stroke-width="2" class="transition-all duration-500"/>
                        </svg>
                    </div>
                    <button onclick="advancePeristalsis()" class="w-full py-2 px-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition shadow-lg shadow-emerald-950/40">
                        Contract Circular Muscles (Peristalsis)
                    </button>
                </div>
            """
        elif itype == "stomach_villi_digestion_sim":
            interactive_html = """
                <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-xl">
                    <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
                        <h4 class="text-xs sm:text-sm font-bold text-white uppercase tracking-wider">Stomach Secretions ($HCl$, Pepsin) & Intestinal Villi</h4>
                    </div>
                    <div id="stomachStatus" class="text-xs text-slate-300 mb-3 bg-slate-950 p-2.5 rounded-lg border border-slate-800">
                        Gastric glands release $HCl$ (acidic medium), pepsin (protein digestion), and mucus.
                    </div>
                    <div class="bg-slate-950 rounded-xl p-2 border border-slate-800 mb-3 flex justify-center">
                        <svg viewBox="0 0 320 160" class="w-full h-36 sm:h-44">
                            <!-- J-shaped stomach contour -->
                            <path d="M130 30 Q120 70 125 100 Q130 135 170 130 Q205 125 210 90 Q215 50 180 50" fill="none" stroke="#f43f5e" stroke-width="5" stroke-linecap="round"/>
                            <text x="145" y="85" fill="#fda4af" font-size="9" font-weight="bold">STOMACH</text>
                            <!-- Acid / Pepsin bubbles -->
                            <g id="pepsinBubbles" class="hidden">
                                <circle cx="150" cy="110" r="4" fill="#38bdf8" class="bubble-rise"/>
                                <circle cx="170" cy="115" r="5" fill="#38bdf8" class="bubble-rise"/>
                                <text x="140" y="145" fill="#38bdf8" font-size="8">HCl + Pepsin</text>
                            </g>
                        </svg>
                    </div>
                    <button onclick="triggerStomachDigest()" class="w-full py-2 px-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition shadow-lg shadow-emerald-950/40">
                        Secrete Gastric Juice (Acid & Pepsin Activation)
                    </button>
                </div>
            """
        elif itype == "respiration_limewater_pichkari_sim":
            interactive_html = """
                <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-xl">
                    <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
                        <h4 class="text-xs sm:text-sm font-bold text-white uppercase tracking-wider">Activity 5.4: Exhaled Breath vs Syringe Lime Water Test</h4>
                    </div>
                    <div id="respirStatus" class="text-xs text-slate-300 mb-3 bg-slate-950 p-2.5 rounded-lg border border-slate-800">
                        Test lime water with human exhaled breath vs atmospheric air from a syringe.
                    </div>
                    <div class="bg-slate-950 rounded-xl p-2 border border-slate-800 mb-3 flex justify-center">
                        <svg viewBox="0 0 320 150" class="w-full h-36 sm:h-40">
                            <!-- Test tube with Lime Water -->
                            <rect x="135" y="20" width="50" height="110" rx="14" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
                            <rect id="respirLiquid" x="137" y="55" width="46" height="73" rx="12" fill="#38bdf8" fill-opacity="0.2" class="transition-all duration-700"/>
                            <!-- Glass delivery tube -->
                            <rect x="157" y="10" width="6" height="80" fill="#94a3b8" rx="2"/>
                            <text x="135" y="145" fill="#94a3b8" font-size="8">Lime Water</text>
                        </svg>
                    </div>
                    <div class="grid grid-cols-2 gap-2">
                        <button onclick="testLimeWaterBreath(true)" class="py-2 px-3 rounded-xl bg-emerald-600/30 hover:bg-emerald-600/50 text-emerald-300 border border-emerald-500/40 text-xs font-bold transition">
                            Blow Exhaled Breath (Milky Fast!)
                        </button>
                        <button onclick="testLimeWaterBreath(false)" class="py-2 px-3 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 text-xs font-bold transition">
                            Pump Syringe Air (Stays Clear)
                        </button>
                    </div>
                </div>
            """
        elif itype == "three_pathways_pyruvate_sim":
            interactive_html = """
                <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-xl">
                    <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
                        <h4 class="text-xs sm:text-sm font-bold text-white uppercase tracking-wider">Fig 5.8: The 3 Divergent Metabolic Fates of Pyruvate</h4>
                    </div>
                    <div id="pathwayStatus" class="text-xs text-slate-300 mb-3 bg-slate-950 p-2.5 rounded-lg border border-slate-800">
                        Glucose (6C) in cytoplasm splits into Pyruvate (3C). Choose metabolic branch below.
                    </div>
                    <div class="grid grid-cols-3 gap-2">
                        <button onclick="selectRespirationPathway('mitochondria')" class="p-3 rounded-xl bg-slate-950 hover:bg-slate-800 border border-slate-800 text-left transition">
                            <span class="text-xs font-bold text-emerald-400 block mb-1">Mitochondria (+O₂)</span>
                            <span class="text-[10px] text-slate-400">CO₂ + H₂O + 36-38 ATP (Aerobic).</span>
                        </button>
                        <button onclick="selectRespirationPathway('muscle')" class="p-3 rounded-xl bg-slate-950 hover:bg-slate-800 border border-slate-800 text-left transition">
                            <span class="text-xs font-bold text-rose-400 block mb-1">Muscle Cells (Low O₂)</span>
                            <span class="text-[10px] text-slate-400">Lactic acid + Cramps (Sudden sprint).</span>
                        </button>
                        <button onclick="selectRespirationPathway('yeast')" class="p-3 rounded-xl bg-slate-950 hover:bg-slate-800 border border-slate-800 text-left transition">
                            <span class="text-xs font-bold text-amber-400 block mb-1">Yeast Ferment (-O₂)</span>
                            <span class="text-[10px] text-slate-400">Ethanol + CO₂ + 2 ATP (Anaerobic).</span>
                        </button>
                    </div>
                </div>
            """
        elif itype == "fish_vs_human_airway_sim":
            interactive_html = """
                <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-xl">
                    <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
                        <h4 class="text-xs sm:text-sm font-bold text-white uppercase tracking-wider">Aquatic Gills (Rapid Rate) vs Human Cartilaginous Trachea</h4>
                    </div>
                    <div id="gillStatus" class="text-xs text-slate-300 mb-3 bg-slate-950 p-2.5 rounded-lg border border-slate-800">
                        Fish gills extract low dissolved O₂ at high frequency; human trachea has cartilage rings.
                    </div>
                    <div class="bg-slate-950 rounded-xl p-2 border border-slate-800 mb-3 flex justify-center">
                        <svg viewBox="0 0 320 150" class="w-full h-36 sm:h-40">
                            <!-- Fish profile with Gill Slits -->
                            <path d="M40 80 Q90 40 140 80 Q90 120 40 80 Z" fill="#0284c7" fill-opacity="0.3" stroke="#38bdf8" stroke-width="2"/>
                            <!-- Gill slit curves -->
                            <path d="M100 65 Q95 80 100 95" stroke="#f43f5e" stroke-width="3"/>
                            <path d="M110 65 Q105 80 110 95" stroke="#f43f5e" stroke-width="3"/>
                            <text x="85" y="115" fill="#fca5a5" font-size="8">Gills</text>
                            <path id="gillWaterFlow" d="M125 75 L155 75" stroke="#38bdf8" stroke-width="4" stroke-dasharray="3,3" class="hidden"/>
                            
                            <!-- Human Trachea with C-rings -->
                            <rect x="220" y="30" width="20" height="90" fill="#334155" rx="4"/>
                            <line x1="220" y1="45" x2="240" y2="45" stroke="#94a3b8" stroke-width="2.5"/>
                            <line x1="220" y1="65" x2="240" y2="65" stroke="#94a3b8" stroke-width="2.5"/>
                            <line x1="220" y1="85" x2="240" y2="85" stroke="#94a3b8" stroke-width="2.5"/>
                            <line x1="220" y1="105" x2="240" y2="105" stroke="#94a3b8" stroke-width="2.5"/>
                            <text x="210" y="135" fill="#cbd5e1" font-size="8">Cartilage Rings</text>
                        </svg>
                    </div>
                    <button onclick="triggerGillIrrigation()" class="w-full py-2 px-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition shadow-lg shadow-emerald-950/40">
                        Pump Water Past Fish Gills (Rapid Aquatic Breathing)
                    </button>
                </div>
            """
        elif itype == "alveoli_capillary_gas_exchange_sim":
            interactive_html = """
                <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-xl">
                    <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
                        <h4 class="text-xs sm:text-sm font-bold text-white uppercase tracking-wider">Alveolar Gas Exchange (80 m² Tennis Court Surface Area)</h4>
                    </div>
                    <div id="alvStatus" class="text-xs text-slate-300 mb-3 bg-slate-950 p-2.5 rounded-lg border border-slate-800">
                        Resting alveolus wrapped in pulmonary capillary meshwork.
                    </div>
                    <div class="bg-slate-950 rounded-xl p-2 border border-slate-800 mb-3 flex justify-center">
                        <svg viewBox="0 0 320 160" class="w-full h-36 sm:h-44">
                            <!-- Alveolus Sac -->
                            <circle id="alveolusSac" cx="160" cy="80" r="30" fill="#047857" fill-opacity="0.3" stroke="#10b981" stroke-width="2.5" class="transition-all duration-700"/>
                            <text x="140" y="85" fill="#a7f3d0" font-size="9" font-weight="bold">ALVEOLUS</text>
                            <!-- Gas diffusion arrows -->
                            <text id="alvO2" x="180" y="55" fill="#38bdf8" font-size="10" font-weight="bold" class="hidden">O₂ → Blood</text>
                            <text id="alvCO2" x="100" y="55" fill="#f87171" font-size="10" font-weight="bold" class="hidden">CO₂ → Alveolus</text>
                            <!-- Surrounding capillary -->
                            <path d="M110 80 Q160 125 210 80" fill="none" stroke="#ef4444" stroke-width="4" stroke-linecap="round"/>
                        </svg>
                    </div>
                    <button id="alvBtn" onclick="toggleAlveolus()" class="w-full py-2 px-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition shadow-lg shadow-emerald-950/40">
                        Inhale (Inflate Alveolus)
                    </button>
                </div>
            """
        elif itype == "beating_heart_circulation_sim":
            interactive_html = """
                <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-xl">
                    <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
                        <h4 class="text-xs sm:text-sm font-bold text-white uppercase tracking-wider">Fig 5.10 & 5.11: 4-Chambered Human Heart & Double Circulation</h4>
                    </div>
                    <div id="heartStatus" class="text-xs text-slate-300 mb-3 bg-slate-950 p-2.5 rounded-lg border border-slate-800">
                        Click button to trigger heartbeat systolic pumping and double circulation.
                    </div>
                    <div class="bg-slate-950 rounded-xl p-2 border border-slate-800 mb-3 flex justify-center">
                        <svg id="heartSvg" viewBox="0 0 320 160" class="w-full h-36 sm:h-44 transition-transform duration-300">
                            <!-- Right Atrium & Ventricle (Deox - Blue) -->
                            <rect x="95" y="35" width="55" height="40" rx="4" fill="#1e3a8a" stroke="#3b82f6" stroke-width="1.5"/>
                            <text x="105" y="60" fill="#93c5fd" font-size="9" font-weight="bold">R. Atrium</text>
                            <rect x="95" y="80" width="55" height="55" rx="4" fill="#1e40af" stroke="#3b82f6" stroke-width="2"/>
                            <text x="100" y="112" fill="#bfdbfe" font-size="9" font-weight="bold">R. Ventricle</text>
                            
                            <!-- Left Atrium & Ventricle (Ox - Red) -->
                            <rect x="170" y="35" width="55" height="40" rx="4" fill="#991b1b" stroke="#ef4444" stroke-width="1.5"/>
                            <text x="180" y="60" fill="#fca5a5" font-size="9" font-weight="bold">L. Atrium</text>
                            <rect x="170" y="80" width="55" height="55" rx="4" fill="#b91c1c" stroke="#ef4444" stroke-width="3"/>
                            <text x="175" y="112" fill="#fecaca" font-size="9" font-weight="bold">L. Ventricle</text>
                            
                            <!-- Central Dividing Septum -->
                            <line x1="160" y1="35" x2="160" y2="135" stroke="#e2e8f0" stroke-width="4"/>
                        </svg>
                    </div>
                    <button onclick="pumpHeartCycle()" class="w-full py-2 px-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition shadow-lg shadow-emerald-950/40">
                        Trigger Heartbeat Systole (Pump Double Circulation)
                    </button>
                </div>
            """
        elif itype == "sphygmomanometer_vessels_sim":
            interactive_html = """
                <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-xl">
                    <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
                        <h4 class="text-xs sm:text-sm font-bold text-white uppercase tracking-wider">Clinical Hemodynamics: Sphygmomanometer & Vessels</h4>
                    </div>
                    <div id="bpStatus" class="text-xs text-slate-300 mb-3 bg-slate-950 p-2.5 rounded-lg border border-slate-800">
                        Sphygmomanometer measures systolic (120 mm Hg) and diastolic (80 mm Hg) pressure.
                    </div>
                    <div class="bg-slate-950 rounded-xl p-2 border border-slate-800 mb-3 flex justify-center">
                        <svg viewBox="0 0 320 150" class="w-full h-36 sm:h-40">
                            <!-- Dial Gauge -->
                            <circle cx="160" cy="100" r="50" fill="#1e293b" stroke="#64748b" stroke-width="3"/>
                            <line id="cuffNeedle" x1="160" y1="100" x2="160" y2="60" stroke="#f43f5e" stroke-width="3" stroke-linecap="round" class="transition-transform duration-500"/>
                            <text x="135" y="130" fill="#94a3b8" font-size="8">mm Hg Gauge</text>
                            <!-- Marks -->
                            <text x="120" y="80" fill="#cbd5e1" font-size="7">80</text>
                            <text x="150" y="55" fill="#facc15" font-size="8" font-weight="bold">120</text>
                            <text x="185" y="80" fill="#cbd5e1" font-size="7">160</text>
                        </svg>
                    </div>
                    <button onclick="pumpCuff()" class="w-full py-2 px-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition shadow-lg shadow-emerald-950/40">
                        Inflate Pressure Cuff (Measure BP)
                    </button>
                </div>
            """
        elif itype == "transpiration_pull_tree_sim":
            interactive_html = """
                <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-xl">
                    <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
                        <h4 class="text-xs sm:text-sm font-bold text-white uppercase tracking-wider">Fig 5.12: Transpiration Pull Moving Water up Tall Tree</h4>
                    </div>
                    <div id="treeStatus" class="text-xs text-slate-300 mb-3 bg-slate-950 p-2.5 rounded-lg border border-slate-800">
                        Evaporation from stomata pulls water column up xylem continuous conduit.
                    </div>
                    <div class="bg-slate-950 rounded-xl p-2 border border-slate-800 mb-3 flex justify-center">
                        <svg viewBox="0 0 320 160" class="w-full h-36 sm:h-44">
                            <!-- Tree canopy & trunk -->
                            <ellipse cx="160" cy="45" rx="55" ry="30" fill="#047857" stroke="#10b981" stroke-width="2"/>
                            <rect x="152" y="75" width="16" height="65" fill="#78350f"/>
                            <!-- Xylem tube line -->
                            <line id="xylemWaterColumn" x1="160" y1="140" x2="160" y2="45" stroke="#64748b" stroke-width="4" stroke-linecap="round"/>
                            <!-- Transpiration vapour droplet -->
                            <circle id="transpireDrop" cx="160" cy="20" r="5" fill="#38bdf8" class="hidden bubble-rise"/>
                            <text x="125" y="152" fill="#94a3b8" font-size="8">Root Absorption</text>
                        </svg>
                    </div>
                    <button onclick="triggerTranspirationPull()" class="w-full py-2 px-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition shadow-lg shadow-emerald-950/40">
                        Sunlight Evaporation (Trigger Transpiration Pull)
                    </button>
                </div>
            """
        elif itype == "phloem_pressure_flow_sim":
            interactive_html = """
                <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-xl">
                    <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
                        <h4 class="text-xs sm:text-sm font-bold text-white uppercase tracking-wider">Phloem Sieve Tube ATP Osmotic Pressure Flow</h4>
                    </div>
                    <div id="phloemStatus" class="text-xs text-slate-300 mb-3 bg-slate-950 p-2.5 rounded-lg border border-slate-800">
                        Sucrose loaded with ATP increases osmotic pressure, driving sap to sinks.
                    </div>
                    <div class="bg-slate-950 rounded-xl p-2 border border-slate-800 mb-3 flex justify-center">
                        <svg viewBox="0 0 320 150" class="w-full h-36 sm:h-40">
                            <!-- Sieve tube cylinder -->
                            <rect x="140" y="20" width="40" height="110" rx="4" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
                            <!-- Sieve plates -->
                            <line x1="140" y1="55" x2="180" y2="55" stroke="#cbd5e1" stroke-width="2" stroke-dasharray="3,3"/>
                            <line x1="140" y1="95" x2="180" y2="95" stroke="#cbd5e1" stroke-width="2" stroke-dasharray="3,3"/>
                            <!-- Sucrose sap droplet -->
                            <circle id="phloemSugar" cx="160" cy="40" r="7" fill="#facc15" class="hidden bubble-rise"/>
                            <text x="90" y="75" fill="#fde047" font-size="9" font-weight="bold">ATP Load</text>
                            <text x="190" y="75" fill="#a7f3d0" font-size="9" font-weight="bold">Water In</text>
                        </svg>
                    </div>
                    <button onclick="triggerPhloemFlow()" class="w-full py-2 px-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition shadow-lg shadow-emerald-950/40">
                        Load Sucrose with ATP (Drive Bulk Flow)
                    </button>
                </div>
            """
        elif itype == "nephron_hemodialysis_sim":
            interactive_html = """
                <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-xl">
                    <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-3">
                        <h4 class="text-xs sm:text-sm font-bold text-white uppercase tracking-wider">Fig 5.14: Nephron Ultrafiltration & Reabsorption (180 L → 1.5 L)</h4>
                    </div>
                    <div id="nephronStatus" class="text-xs text-slate-300 mb-3 bg-slate-950 p-2.5 rounded-lg border border-slate-800">
                        Glomerulus filters 180 L of blood daily; tubules reabsorb >99% water & nutrients.
                    </div>
                    <div class="bg-slate-950 rounded-xl p-2 border border-slate-800 mb-3 flex justify-center">
                        <svg viewBox="0 0 320 160" class="w-full h-36 sm:h-44">
                            <!-- Bowman's Capsule Cup -->
                            <path d="M100 40 C60 40, 60 90, 100 90 L160 90 Q180 90 180 120 L180 145" fill="none" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>
                            <!-- Glomerulus Capillary Knot -->
                            <circle cx="85" cy="65" r="14" fill="#ef4444" class="pulse-glow"/>
                            <text x="50" y="35" fill="#fca5a5" font-size="8">Glomerulus</text>
                            <!-- Filtrate drop in capsule -->
                            <circle id="nephronFiltrate" cx="95" cy="65" r="4" fill="#facc15" class="hidden"/>
                            <!-- Reabsorption capillary arrow -->
                            <path id="reabsorbArrow" d="M160 90 L160 70" stroke="#38bdf8" stroke-width="3" stroke-linecap="round" class="hidden"/>
                            <text x="190" y="135" fill="#fde047" font-size="8">Urine (1-2 L)</text>
                        </svg>
                    </div>
                    <button onclick="triggerNephronFilter()" class="w-full py-2 px-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition shadow-lg shadow-emerald-950/40">
                        Filter Blood in Glomerulus (Reabsorb 99% Water)
                    </button>
                </div>
            """

        # Teacher Talking Avatar & Whiteboard Dialogue Box
        teacher_avatar_html = f"""
            <div class="bg-gradient-to-r from-slate-900 via-slate-800 to-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 mb-5 shadow-xl flex flex-col sm:flex-row items-center gap-4">
                <!-- Person Talking: Dr. Sophia Teacher Avatar -->
                <div class="relative shrink-0 flex flex-col items-center teacher-bob">
                    <svg viewBox="0 0 120 120" class="w-20 h-20 sm:w-24 sm:h-24 drop-shadow-lg">
                        <!-- Lab coat shoulders -->
                        <path d="M20 115 C20 85, 45 80, 60 80 C75 80, 100 85, 100 115 Z" fill="#059669" stroke="#10b981" stroke-width="2"/>
                        <polygon points="50,80 60,105 70,80" fill="#ffffff"/>
                        <!-- Head / Face -->
                        <circle cx="60" cy="50" r="26" fill="#fed7aa" stroke="#f97316" stroke-width="1.5"/>
                        <!-- Hair -->
                        <path d="M34 50 C34 25, 86 25, 86 50 C86 35, 75 22, 60 22 C45 22, 34 35, 34 50 Z" fill="#78350f"/>
                        <!-- Eyes & Glasses -->
                        <circle cx="50" cy="48" r="7" fill="none" stroke="#047857" stroke-width="2"/>
                        <circle cx="70" cy="48" r="7" fill="none" stroke="#047857" stroke-width="2"/>
                        <line x1="57" y1="48" x2="63" y2="48" stroke="#047857" stroke-width="2"/>
                        <circle cx="50" cy="48" r="2.5" fill="#1e293b"/>
                        <circle cx="70" cy="48" r="2.5" fill="#1e293b"/>
                        <!-- Eyebrows -->
                        <path d="M44 38 Q50 35 56 38" fill="none" stroke="#78350f" stroke-width="2"/>
                        <path d="M64 38 Q70 35 76 38" fill="none" stroke="#78350f" stroke-width="2"/>
                        <!-- Talking Mouth -->
                        <ellipse id="teacherMouth-{idx}" cx="60" cy="64" rx="5" ry="3" fill="#be123c"/>
                    </svg>
                    <span class="px-2 py-0.5 rounded-full text-[9px] font-extrabold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 mt-1">
                        Dr. Sophia • Biology Teacher
                    </span>
                </div>

                <!-- Speech Bubble Dialogue -->
                <div class="flex-1 bg-slate-950 p-3.5 rounded-2xl border border-slate-800 relative">
                    <div class="hidden sm:block absolute -left-2 top-6 w-3 h-3 bg-slate-950 border-l border-b border-slate-800 transform rotate-45"></div>
                    <div class="flex items-center justify-between mb-1">
                        <span class="text-xs font-bold text-emerald-400 flex items-center gap-1.5">
                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/></svg>
                            Teacher's Live Audio Commentary
                        </span>
                        <span class="text-[10px] text-slate-500 font-mono">Web Speech Narration</span>
                    </div>
                    <p class="text-xs sm:text-sm text-slate-300 italic leading-relaxed">
                        "{s.get('narration', '')}"
                    </p>
                </div>
            </div>
        """

        slide_card = f"""
            <div id="slide-{idx}" class="slide-container">
                <!-- Slide Header Banner -->
                <div class="bg-gradient-to-r from-slate-900 via-slate-800 to-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-6 mb-4 shadow-xl">
                    <div class="flex flex-wrap items-center justify-between gap-3 mb-2">
                        <span class="px-2.5 py-1 rounded-md text-xs font-extrabold uppercase tracking-wider bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">
                            {s['badge']}
                        </span>
                        <span class="text-xs font-mono font-semibold text-slate-400">Slide {idx + 1} of {len(all_slides)}</span>
                    </div>
                    <h2 class="text-xl sm:text-2xl font-extrabold text-white tracking-tight mb-2">
                        {s['title']}
                    </h2>
                    <blockquote class="text-xs sm:text-sm text-emerald-200/90 italic border-l-2 border-emerald-500/60 pl-3 py-0.5 mb-3 bg-emerald-950/20 rounded-r-lg">
                        "{s.get('quote', '')}"
                    </blockquote>
                    <p class="text-xs sm:text-sm text-slate-300 max-w-4xl leading-relaxed">
                        {s.get('lead', '')}
                    </p>
                </div>

                <!-- Teacher Talking Avatar with Speech Bubble -->
                {teacher_avatar_html}

                <!-- Main Content Grid: Theory & Interactive Simulator -->
                <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 mb-6">
                    <!-- Left: In-Depth NCERT Theory & Equations (7 Cols) -->
                    <div class="lg:col-span-7 space-y-4">
                        {theory_cards_html}
                    </div>

                    <!-- Right: Interactive SVG Simulator (5 Cols) -->
                    <div class="lg:col-span-5">
                        {interactive_html}
                    </div>
                </div>

                <!-- Bottom Checkpoints Section (2 Questions with Explanations) -->
                <div class="bg-slate-900/60 border border-slate-800/80 rounded-2xl p-4 sm:p-5 mt-6">
                    <div class="flex items-center gap-2 mb-3">
                        <span class="p-1 rounded bg-emerald-500/20 text-emerald-400">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                        </span>
                        <h3 class="text-xs sm:text-sm font-bold text-white uppercase tracking-wider">Concept Checkpoint Challenge (2 Questions)</h3>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        {checkpoints_html}
                    </div>
                </div>
            </div>
        """
        slides_html.append(slide_card)

    else:
        # Quiz Slide HTML
        quiz_q_html = ""
        for q_idx, q in enumerate(s.get('questions', [])):
            q_num = q['id']
            escaped_q = q['q'].replace('"', '&quot;')
            escaped_sol = q['solution'].replace('"', '&quot;').replace('\n', '<br>')

            opts_html = ""
            for o_idx, opt in enumerate(q['options']):
                opts_html += f"""
                    <label class="flex items-start gap-2.5 p-2 rounded-lg bg-slate-950/70 border border-slate-800 hover:border-slate-700 cursor-pointer text-xs transition">
                        <input type="radio" name="quiz-{idx}-{q_num}" value="{o_idx}" onchange="checkCheckpointAnswer({idx}, {q_num}, {o_idx}, {q['ans']}, 'quiz-feedback-{q_num}')" class="mt-0.5 text-emerald-600 focus:ring-emerald-500 bg-slate-900 border-slate-700">
                        <span class="text-slate-300">{html.escape(opt)}</span>
                    </label>
                """

            quiz_q_html += f"""
                <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-4 shadow">
                    <div class="flex items-center justify-between gap-2 mb-2">
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Question {q_num}</span>
                        <div class="flex items-center gap-2">
                            <div id="quiz-feedback-{q_num}"></div>
                            <button onclick="openQuizSolution({q_num}, '{escaped_q}', '{escaped_sol}')" class="px-2.5 py-1 rounded-md bg-emerald-600/30 hover:bg-emerald-600/50 border border-emerald-500/40 text-emerald-300 text-xs font-bold transition flex items-center gap-1">
                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                                <span>Solution</span>
                            </button>
                        </div>
                    </div>
                    <p class="text-xs sm:text-sm font-semibold text-white mb-3">{q['q']}</p>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
                        {opts_html}
                    </div>
                </div>
            """

        last_notice_html = ""
        if idx == len(all_slides) - 1:
            last_notice_html = """
                <div id="lastSlideNotice" class="mt-8 p-6 rounded-2xl bg-gradient-to-r from-emerald-950/60 via-slate-900 to-emerald-950/60 border-2 border-emerald-500/50 text-center shadow-2xl">
                    <div class="inline-flex p-3 rounded-full bg-emerald-500/20 text-emerald-400 mb-2">
                        <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                    </div>
                    <h3 class="text-lg sm:text-xl font-bold text-white mb-1">Congratulations!</h3>
                    <p class="text-sm font-semibold text-emerald-300 mb-2">You have reached the last slide of this chapter</p>
                    <p class="text-xs text-slate-400 max-w-xl mx-auto">You have thoroughly mastered NCERT Class 10 Science Chapter 5: Life Processes, covering nutrition (autotrophic & heterotrophic), human digestion, aerobic and anaerobic respiration pathways, cardiovascular circulation, plant vascular transport (xylem & phloem), renal excretion, nephron ultrafiltration, and hemodialysis.</p>
                </div>
            """

        slide_card = f"""
            <div id="slide-{idx}" class="slide-container">
                <div class="bg-gradient-to-r from-slate-900 via-slate-800 to-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-6 mb-6 shadow-xl">
                    <div class="flex flex-wrap items-center justify-between gap-3 mb-2">
                        <span class="px-2.5 py-1 rounded-md text-xs font-extrabold uppercase tracking-wider bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">
                            {s['badge']}
                        </span>
                        <span class="text-xs font-mono font-semibold text-slate-400">Slide {idx + 1} of {len(all_slides)}</span>
                    </div>
                    <h2 class="text-xl sm:text-2xl font-extrabold text-white tracking-tight mb-2">
                        {s['title']}
                    </h2>
                    <p class="text-xs sm:text-sm text-slate-300 max-w-3xl leading-relaxed">
                        {s.get('description', '')}
                    </p>
                </div>

                <div class="space-y-4">
                    {quiz_q_html}
                </div>

                {last_notice_html}
            </div>
        """
        slides_html.append(slide_card)

output_html = html_template.replace('__SLIDES_CONTENT__', '\n'.join(slides_html))
output_html = output_html.replace('__FOOTER_PILLS__', '\n'.join(pills_html))
output_html = output_html.replace('__SLIDES_JSON__', json.dumps(all_slides))

output_path = '/home/lead-programmer/study-app/public/animations/life-processes.html'
with open(output_path, 'w') as f:
    f.write(output_html)

print(f"Generated {output_path} successfully. Total file size: {len(output_html)} bytes.")

