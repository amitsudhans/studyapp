with open('.agents/create_ch8_js.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace in calcBrahmaguptaProduct
text = text.replace(
    '  if (prodDenEl) prodDenEl.textContent = rawDen;\n  if (simpNumEl) simpNumEl.textContent = sNum;\n  if (simpDenEl) simpDenEl.textContent = sDen;',
    '  if (prodDenEl) prodDenEl.textContent = rawDen;\n  if (simpNumEl) simpNumEl.textContent = sNum;\n  if (simpDenEl) simpDenEl.textContent = sDen;\n  if (expEl && window.triggerMathRender) setTimeout(() => triggerMathRender(expEl), 10);'
)

# Replace in setReciprocalFraction
text = text.replace(
    '    notice.innerHTML = `Original: <strong>${a}/${b}</strong> &rarr; Reciprocal (Multiplicative Inverse): <strong>${b}/${a}</strong>. Product: $(${a}/${b}) \\times (${b}/${a}) = \\frac{${a*b}}{${a*b}} = \\mathbf{1}$.`;\n  }',
    '    notice.innerHTML = `Original: <strong>${a}/${b}</strong> &rarr; Reciprocal (Multiplicative Inverse): <strong>${b}/${a}</strong>. Product: $(${a}/${b}) \\times (${b}/${a}) = \\frac{${a*b}}{${a*b}} = \\mathbf{1}$.`;\n    if (window.triggerMathRender) setTimeout(() => triggerMathRender(notice), 10);\n  }'
)

# Replace in revealLilavatiSolution
text = text.replace(
    '    box.innerHTML = `<span class=\'text-amber-400 font-bold\'>Bhāskara II\'s Viparīta-vidhi (Method of Inversion):</span><br>\n    Final remainder = $20$ coins, which represents $1 - \\frac{1}{2} - \\frac{1}{6} = \\frac{1}{3}$ of the original wealth $x$.<br>\n    Therefore: $x \\times \\frac{1}{3} = 20 \\implies x = 20 \\div \\frac{1}{3} = 20 \\times 3 = \\mathbf{${init}\\text{ coins}}$!`;\n  }',
    '    box.innerHTML = `<span class=\'text-amber-400 font-bold\'>Bhāskara II\'s Viparīta-vidhi (Method of Inversion):</span><br>\n    Final remainder = $20$ coins, which represents $1 - \\frac{1}{2} - \\frac{1}{6} = \\frac{1}{3}$ of the original wealth $x$.<br>\n    Therefore: $x \\times \\frac{1}{3} = 20 \\implies x = 20 \\div \\frac{1}{3} = 20 \\times 3 = \\mathbf{${init}\\text{ coins}}$!`;\n    if (window.triggerMathRender) setTimeout(() => triggerMathRender(box), 10);\n  }'
)

# Replace in updateQuotientMagnifier
text = text.replace(
    '      expl.innerHTML = `Because the divisor <strong>${divisor.toFixed(1)} < 1</strong>, division magnifies the dividend: $6 \\div ${divisor.toFixed(1)} = \\mathbf{${quotient.toFixed(2)}} > 6$.`;\n    } else if (divisor === 1.0) {\n      badge.textContent = \'Quotient Unchanged (= Dividend)\';\n      badge.className = \'text-xs font-bold px-2 py-0.5 rounded bg-blue-500/20 text-blue-300 border border-blue-500/40\';\n      expl.innerHTML = `Dividing by 1 leaves the dividend exactly unchanged: $6 \\div 1 = 6$.`;\n    } else {\n      badge.textContent = \'Quotient Shrinks! (< Dividend)\';\n      badge.className = \'text-xs font-bold px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40\';\n      expl.innerHTML = `Because the divisor <strong>${divisor.toFixed(1)} > 1</strong>, division shrinks the value: $6 \\div ${divisor.toFixed(1)} = \\mathbf{${quotient.toFixed(2)}} < 6$.`;\n    }\n  }',
    '      expl.innerHTML = `Because the divisor <strong>${divisor.toFixed(1)} < 1</strong>, division magnifies the dividend: $6 \\div ${divisor.toFixed(1)} = \\mathbf{${quotient.toFixed(2)}} > 6$.`;\n    } else if (divisor === 1.0) {\n      badge.textContent = \'Quotient Unchanged (= Dividend)\';\n      badge.className = \'text-xs font-bold px-2 py-0.5 rounded bg-blue-500/20 text-blue-300 border border-blue-500/40\';\n      expl.innerHTML = `Dividing by 1 leaves the dividend exactly unchanged: $6 \\div 1 = 6$.`;\n    } else {\n      badge.textContent = \'Quotient Shrinks! (< Dividend)\';\n      badge.className = \'text-xs font-bold px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40\';\n      expl.innerHTML = `Because the divisor <strong>${divisor.toFixed(1)} > 1</strong>, division shrinks the value: $6 \\div ${divisor.toFixed(1)} = \\mathbf{${quotient.toFixed(2)}} < 6$.`;\n    }\n    if (window.triggerMathRender) setTimeout(() => triggerMathRender(expl), 10);\n  }'
)

with open('.agents/create_ch8_js.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated .agents/create_ch8_js.py successfully!')

