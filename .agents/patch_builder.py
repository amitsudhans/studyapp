with open('.agents/build_class7_math_working_with_fractions_lab.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace KaTeX in head
old_head = '''  <!-- KaTeX CSS & JS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script>
    function triggerMathRender(el) {
      if (window.renderMathInElement) {
        window.renderMathInElement(el || document.body, {
          delimiters: [
            {left: \'$$\', right: \'$$\', display: true},
            {left: \'$\', right: \'$\', display: false}
          ],
          throwOnError: false
        });
      }
    }
  </script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
          onload="if (window.triggerMathRender) triggerMathRender(document.body);"></script>'''

new_head = '''  <!-- KaTeX CSS & JS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
  <script>
    function triggerMathRender(el) {
      const target = el || document.body;
      if (typeof renderMathInElement === 'function') {
        try {
          renderMathInElement(target, {
            delimiters: [
              {left: '$$', right: '$$', display: true},
              {left: '$', right: '$', display: false},
              {left: '\\\\[', right: '\\\\]', display: true},
              {left: '\\\\(', right: '\\\\)', display: false}
            ],
            ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
            throwOnError: false
          });
        } catch (e) {
          console.warn('KaTeX render error:', e);
        }
      } else {
        setTimeout(() => triggerMathRender(target), 80);
      }
    }
    window.triggerMathRender = triggerMathRender;
  </script>'''

if old_head in text:
    text = text.replace(old_head, new_head)
    print("✓ Replaced KaTeX head block with robust synchronous loader and retry")
else:
    print("Warning: old_head not found directly!")

# Replace triggerMathRender(theoryCol) with slideContent
old_call = '        if (window.triggerMathRender) triggerMathRender(theoryCol);'
new_call = '        if (window.triggerMathRender) triggerMathRender(document.getElementById(\'slideContent\') || document.body);'

if old_call in text:
    text = text.replace(old_call, new_call)
    print("✓ Updated renderSlide to render math across whole slideContent (theory + simulator)")
else:
    print("Warning: old_call not found directly!")

with open('.agents/build_class7_math_working_with_fractions_lab.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated .agents/build_class7_math_working_with_fractions_lab.py successfully!")

