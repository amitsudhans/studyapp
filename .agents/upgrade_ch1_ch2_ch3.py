import re
import json

def upgrade_chemical_reactions():
    path = 'public/animations/chemical-reactions-and-equations.html'
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Add CSS for talking-mouth and teacher-bob if missing
    if '.talking-mouth' not in html:
        css_inject = '''        .talking-mouth {
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
    </style>'''
        html = html.replace('    </style>', css_inject)

    # 2. Extract slidesData
    m = re.search(r'const slidesData = (\[.*?\]);', html, re.DOTALL)
    slides_data = json.loads(m.group(1))

    # 3. Inject Teacher Avatar on each content slide (0 to 16)
    for i in range(17):
        slide = slides_data[i]
        narr = slide.get('narration', '')
        avatar_card = f'''
                <!-- Person Talking: Dr. Evelyn Chemistry Teacher Avatar -->
                <div class="mb-6 p-4 rounded-2xl bg-gradient-to-r from-cyan-950/40 via-slate-900 to-cyan-950/20 border border-cyan-500/30 flex flex-col sm:flex-row items-center sm:items-start gap-4 shadow-xl">
                    <div class="relative shrink-0 flex flex-col items-center teacher-bob">
                        <svg viewBox="0 0 120 120" class="w-20 h-20 sm:w-24 sm:h-24 drop-shadow-lg">
                            <!-- Lab coat shoulders -->
                            <path d="M20 115 C20 85, 45 80, 60 80 C75 80, 100 85, 100 115 Z" fill="#0891b2" stroke="#06b6d4" stroke-width="2"/>
                            <polygon points="50,80 60,105 70,80" fill="#ffffff"/>
                            <!-- Head / Face -->
                            <circle cx="60" cy="50" r="26" fill="#fed7aa" stroke="#f97316" stroke-width="1.5"/>
                            <!-- Hair -->
                            <path d="M34 50 C34 25, 86 25, 86 50 C86 35, 75 22, 60 22 C45 22, 34 35, 34 50 Z" fill="#451a03"/>
                            <!-- Eyes & Glasses -->
                            <circle cx="50" cy="48" r="7" fill="none" stroke="#0891b2" stroke-width="2"/>
                            <circle cx="70" cy="48" r="7" fill="none" stroke="#0891b2" stroke-width="2"/>
                            <line x1="57" y1="48" x2="63" y2="48" stroke="#0891b2" stroke-width="2"/>
                            <circle cx="50" cy="48" r="2.5" fill="#1e293b"/>
                            <circle cx="70" cy="48" r="2.5" fill="#1e293b"/>
                            <!-- Eyebrows -->
                            <path d="M44 38 Q50 35 56 38" fill="none" stroke="#78350f" stroke-width="2"/>
                            <path d="M64 38 Q70 35 76 38" fill="none" stroke="#78350f" stroke-width="2"/>
                            <!-- Talking Mouth -->
                            <ellipse id="teacherMouth-{i}" cx="60" cy="64" rx="5" ry="3" fill="#be123c"/>
                        </svg>
                        <span class="px-2 py-0.5 rounded-full text-[9px] font-extrabold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 mt-1">
                            Dr. Evelyn • Chemistry Teacher
                        </span>
                    </div>

                    <!-- Speech Bubble Dialogue -->
                    <div class="flex-1 bg-slate-950 p-3.5 rounded-2xl border border-slate-800 relative">
                        <div class="hidden sm:block absolute -left-2 top-6 w-3 h-3 bg-slate-950 border-l border-b border-slate-800 transform rotate-45"></div>
                        <div class="flex items-center justify-between mb-1">
                            <span class="text-xs font-bold text-cyan-400 flex items-center gap-1.5">
                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/></svg>
                                Teacher\'s Live Audio Commentary
                            </span>
                            <span class="text-[10px] text-slate-500 font-mono">Web Speech Narration</span>
                        </div>
                        <p class="text-xs sm:text-sm text-slate-300 italic leading-relaxed">
                            "{narr}"
                        </p>
                    </div>
                </div>
'''
        # Find where the slide grid starts:
        slide_pattern = rf'(<div id="slide-{i}" class="slide-container">.*?</div>\s*</div>\s*)(<div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start mb-6">)'
        if f'id="teacherMouth-{i}"' not in html:
            html = re.sub(slide_pattern, rf'\1{avatar_card}\n                \2', html, count=1, flags=re.DOTALL)

    # 4. Inject setTeacherTalking and sync speakText
    if 'function setTeacherTalking' not in html:
        talking_fn = '''        function setTeacherTalking(isTalking) {
            const mouth = document.getElementById(`teacherMouth-${currentSlideIndex}`);
            if (mouth) {
                if (isTalking) {
                    mouth.classList.add('talking-mouth');
                } else {
                    mouth.classList.remove('talking-mouth');
                }
            }
        }
'''
        html = html.replace('        function speakText(text) {', talking_fn + '\n        function speakText(text) {')

    # Update speakText event handlers
    old_speak_end = '''            if (preferred) currentUtterance.voice = preferred;

            synth.speak(currentUtterance);'''
    new_speak_end = '''            if (preferred) currentUtterance.voice = preferred;

            currentUtterance.onstart = () => {
                setTeacherTalking(true);
            };
            currentUtterance.onend = () => {
                setTeacherTalking(false);
            };
            currentUtterance.onerror = () => {
                setTeacherTalking(false);
            };

            synth.speak(currentUtterance);'''
    if old_speak_end in html:
        html = html.replace(old_speak_end, new_speak_end)

    # In goToSlide: cancel mouth talk
    if 'setTeacherTalking(false);' not in html:
        html = html.replace("if (synth) synth.cancel();", "if (synth) synth.cancel();\n            setTeacherTalking(false);")

    # Audio unlock
    if 'let audioUnlocked = false;' not in html:
        unlock_code = '''        let audioUnlocked = false;
        function unlockAudio() {
            if (audioUnlocked) return;
            audioUnlocked = true;
            try {
                const ctx = getAudioContext();
                if (ctx && ctx.state === 'suspended') {
                    ctx.resume();
                }
            } catch (e) {}
            if (voiceActive && synth && !synth.speaking) {
                replayVoice();
            }
        }
        document.addEventListener('click', unlockAudio, { once: true });
        document.addEventListener('touchstart', unlockAudio, { once: true });
        document.addEventListener('keydown', unlockAudio, { once: true });

        window.addEventListener('DOMContentLoaded', () => {'''
        html = html.replace("        window.addEventListener('DOMContentLoaded', () => {", unlock_code)

    # Enhanced checkCheckpointAnswer
    old_chk = '''function checkCheckpointAnswer(slideIdx, qIdx, selectedOption, correctOption, solutionId) {
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
        }'''

    new_chk = '''function checkCheckpointAnswer(slideIdx, qIdx, selectedOption, correctOption, solutionId) {
            const solEl = document.getElementById(solutionId);
            let feedbackEl = document.getElementById(`feedback-${slideIdx}-${qIdx}`);
            if (!feedbackEl && solEl && solEl.id && solEl.id.startsWith('quiz-feedback')) {
                feedbackEl = solEl;
            }
            
            if (selectedOption === correctOption) {
                playCorrectSound();
                if (feedbackEl) feedbackEl.innerHTML = `<span class="inline-flex items-center gap-1 text-emerald-400 font-bold text-xs"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Correct! Excellent</span>`;
                if (solEl && solEl !== feedbackEl) solEl.classList.remove('hidden');
            } else {
                playIncorrectSound();
                if (feedbackEl) feedbackEl.innerHTML = `<span class="inline-flex items-center gap-1 text-rose-400 font-bold text-xs"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg> Incorrect. Click Solution</span>`;
                if (solEl && solEl !== feedbackEl) solEl.classList.remove('hidden');
            }
        }'''
    if old_chk in html:
        html = html.replace(old_chk, new_chk)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Chapter 1 (Chemical Reactions) successfully upgraded with talking teacher avatar!")

def upgrade_metals_and_nonmetals():
    path = 'public/animations/metals-and-non-metals.html'
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Audio unlock
    if 'let audioUnlocked = false;' not in html:
        unlock_code = '''        let audioUnlocked = false;
        function unlockAudio() {
            if (audioUnlocked) return;
            audioUnlocked = true;
            try {
                const ctx = getAudioContext();
                if (ctx && ctx.state === 'suspended') {
                    ctx.resume();
                }
            } catch (e) {}
            if (voiceActive && synth && !synth.speaking) {
                replayVoice();
            }
        }
        document.addEventListener('click', unlockAudio, { once: true });
        document.addEventListener('touchstart', unlockAudio, { once: true });
        document.addEventListener('keydown', unlockAudio, { once: true });

        window.addEventListener('DOMContentLoaded', () => {'''
        html = html.replace("        window.addEventListener('DOMContentLoaded', () => {", unlock_code)

    # Enhanced checkCheckpointAnswer
    old_chk = '''function checkCheckpointAnswer(slideIdx, qIdx, selectedOption, correctOption, solutionId) {
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
        }'''

    new_chk = '''function checkCheckpointAnswer(slideIdx, qIdx, selectedOption, correctOption, solutionId) {
            const solEl = document.getElementById(solutionId);
            let feedbackEl = document.getElementById(`feedback-${slideIdx}-${qIdx}`);
            if (!feedbackEl && solEl && solEl.id && solEl.id.startsWith('quiz-feedback')) {
                feedbackEl = solEl;
            }
            
            if (selectedOption === correctOption) {
                playCorrectSound();
                if (feedbackEl) feedbackEl.innerHTML = `<span class="inline-flex items-center gap-1 text-emerald-400 font-bold text-xs"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Correct! Excellent</span>`;
                if (solEl && solEl !== feedbackEl) solEl.classList.remove('hidden');
            } else {
                playIncorrectSound();
                if (feedbackEl) feedbackEl.innerHTML = `<span class="inline-flex items-center gap-1 text-rose-400 font-bold text-xs"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg> Incorrect. Click Solution</span>`;
                if (solEl && solEl !== feedbackEl) solEl.classList.remove('hidden');
            }
        }'''
    if old_chk in html:
        html = html.replace(old_chk, new_chk)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Chapter 3 (Metals and Non-metals) successfully upgraded!")

upgrade_chemical_reactions()
upgrade_metals_and_nonmetals()

