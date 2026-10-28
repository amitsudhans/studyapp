import re

files_to_check = [
    'public/animations/class7-math-number-play.html',
    'public/animations/class7-math-parallel-intersecting-lines.html',
    'public/animations/class7-math-expressions-letter-numbers.html',
    'public/animations/class7-math-peek-beyond-the-point.html',
    'public/animations/class7-math-expressions.html',
    'public/animations/class7-math-large-numbers-around-us.html'
]

for file_path in files_to_check:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Skipping {file_path}: {e}")
        continue

    # Update openSolutionModal in this file
    pattern = r'function openSolutionModal\(q\)\s*\{[\s\S]*?solutionModal\.style\.display\s*=\s*[\'"]flex[\'"];[\s\S]*?\}'
    
    new_fn = """function openSolutionModal(qOrId) {
      const q = (typeof qOrId === 'object' && qOrId !== null) ? qOrId : (typeof QUIZ_QUESTIONS !== 'undefined' ? QUIZ_QUESTIONS.find(item => item.id === Number(qOrId)) : null);
      if (!q) return;

      if (typeof modalTitleText !== 'undefined' && modalTitleText) modalTitleText.textContent = `Question ${q.id} Detailed Derivation`;
      if (typeof modalQuestionText !== 'undefined' && modalQuestionText) modalQuestionText.innerHTML = `<strong>Q${q.id}:</strong> ${q.question}`;
      if (typeof modalSolutionSteps !== 'undefined' && modalSolutionSteps) {
        modalSolutionSteps.innerHTML = '';
        const correctOpt = (q.options && q.options[q.correct] !== undefined) ? q.options[q.correct] : '';
        const solText = q.solution || (q.solution_steps ? q.solution_steps.join('<br>') : '') || q.explanation || 'Detailed step-by-step mathematical derivation provided above.';
        
        const sBox = document.createElement('div');
        sBox.className = 'modal-solution-step';
        sBox.innerHTML = `
          <div style="font-weight:800; color:#34d399; margin-bottom:0.5rem; font-size:0.92rem;">
            ✓ Correct Answer: Option ${String.fromCharCode(65 + q.correct)} (${correctOpt})
          </div>
          <div style="color:#e2e8f0; line-height:1.6;">${solText}</div>
        `;
        modalSolutionSteps.appendChild(sBox);
      }

      if (typeof solutionModal !== 'undefined' && solutionModal) {
        solutionModal.style.setProperty('display', 'flex', 'important');
        solutionModal.classList.add('is-active');
      }
      if (window.triggerMathRender && typeof solutionModal !== 'undefined' && solutionModal) triggerMathRender(solutionModal);
      if (typeof sfx !== 'undefined' && sfx.playClick) sfx.playClick();
    }
    window.openSolutionModal = openSolutionModal;"""

    if re.search(pattern, content):
        content = re.sub(pattern, new_fn, content, count=1)
        # Also ensure #solutionModal z-index is high
        content = content.replace('z-index: 100;', 'z-index: 99999;')
        content = content.replace('z-index: 1000;', 'z-index: 99999;')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file_path} successfully!")
    else:
        print(f"Pattern not found in {file_path}")

