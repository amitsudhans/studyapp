import re
import subprocess

def update_life_processes():
    path = 'public/animations/life-processes.html'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Enhance checkCheckpointAnswer
    old_pattern = r'function checkCheckpointAnswer\(slideIdx, qIdx, selectedOption, correctOption, solutionId\) \{.*?solEl\.classList\.remove\(\'hidden\'\);\s*\}\s*\}'
    new_code = '''function checkCheckpointAnswer(slideIdx, qIdx, selectedOption, correctOption, solutionId) {
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

    content, n = re.subn(old_pattern, new_code, content, count=1, flags=re.DOTALL)
    print(f"checkCheckpointAnswer replaced: {n}")

    # Add audio unlock
    if 'let audioUnlocked = false;' not in content:
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
        content = content.replace("        window.addEventListener('DOMContentLoaded', () => {", unlock_code)
        print("Audio unlock added to life-processes.html")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

update_life_processes()

