import re
import subprocess

def fix_file(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            print(f"Replaced in {filepath}: {old[:50]}...")
        else:
            print(f"NOT FOUND in {filepath}: {old[:50]}...")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# 1. life-processes.html
lp_reps = [
    (
        'status.innerHTML = "<span class=\'text-emerald-400 font-bold\'>Photosynthesis in Action!</span> Chlorophyll absorbs photons; water is split ($O_2\\uparrow$) and $CO_2$ is reduced to starch!";',
        'status.innerHTML = "<span class=\'text-emerald-400 font-bold\'>Photosynthesis in Action!</span> Chlorophyll absorbs photons; water is split (O₂↑) and CO₂ is reduced to starch!";'
    ),
    (
        'status.innerHTML = "<span class=\'text-rose-400 font-bold\'>Stomach Secretions:</span> $HCl$ ($pH \\approx 1.8$) activates Pepsin; proteins digested while mucus coats lining!";',
        'status.innerHTML = "<span class=\'text-rose-400 font-bold\'>Stomach Secretions:</span> HCl (pH ≈ 1.8) activates Pepsin; proteins digested while mucus coats lining!";'
    ),
    (
        'status.innerHTML = "<span class=\'text-rose-400 font-bold\'>Lack of Oxygen (Muscle Cells during sprint):</span> Pyruvate $\\to$ Lactic acid + Energy. Causes painful muscle cramps!";',
        'status.innerHTML = "<span class=\'text-rose-400 font-bold\'>Lack of Oxygen (Muscle Cells during sprint):</span> Pyruvate → Lactic acid + Energy. Causes painful muscle cramps!";'
    ),
    (
        'status.innerHTML = "<span class=\'text-amber-300 font-bold\'>Absence of Oxygen (Yeast Fermentation):</span> Pyruvate $\\to$ Ethanol ($C_2H_5OH$) + $CO_2$ + 2 ATP!";',
        'status.innerHTML = "<span class=\'text-amber-300 font-bold\'>Absence of Oxygen (Yeast Fermentation):</span> Pyruvate → Ethanol (C₂H₅OH) + CO₂ + 2 ATP!";'
    )
]

fix_file('public/animations/life-processes.html', lp_reps)

# 2. metals-and-non-metals.html
mn_reps = [
    (
        'status.innerHTML = "<span class=\'text-amber-300 font-bold\'>Gallium Melted into Liquid!</span> Body heat ($37^\\circ\\text{C}$) exceeds Gallium\'s low melting point ($29.8^\\circ\\text{C}$)."',
        'status.innerHTML = "<span class=\'text-amber-300 font-bold\'>Gallium Melted into Liquid!</span> Body heat (37°C) exceeds Gallium\'s low melting point (29.8°C)."'
    ),
    (
        'status.innerHTML = "<span class=\'text-blue-400 font-bold\'>Basic Metal Oxide:</span> $2Mg + O_2 \\to 2MgO$. Ash dissolved in water forms $Mg(OH)_2$, turning Red Litmus <strong>BLUE</strong>!";',
        'status.innerHTML = "<span class=\'text-blue-400 font-bold\'>Basic Metal Oxide:</span> 2Mg + O₂ → 2MgO. Ash dissolved in water forms Mg(OH)₂, turning Red Litmus <strong>BLUE</strong>!";'
    ),
    (
        'status.innerHTML = "<span class=\'text-rose-400 font-bold\'>Acidic Non-metal Oxide:</span> $S + O_2 \\to SO_2$. Fumes dissolved in water form sulphurous acid ($H_2SO_3$), turning Blue Litmus <strong>RED</strong>!";',
        'status.innerHTML = "<span class=\'text-rose-400 font-bold\'>Acidic Non-metal Oxide:</span> S + O₂ → SO₂. Fumes dissolved in water form sulphurous acid (H₂SO₃), turning Blue Litmus <strong>RED</strong>!";'
    ),
    (
        'status.innerHTML = "<span class=\'text-sky-300 font-bold\'>Acts as a Base with Acid:</span> $Al_2O_3 + 6HCl \\to 2AlCl_3 + 3H_2O$ (Forms Aluminium chloride salt + water).";',
        'status.innerHTML = "<span class=\'text-sky-300 font-bold\'>Acts as a Base with Acid:</span> Al₂O₃ + 6HCl → 2AlCl₃ + 3H₂O (Forms Aluminium chloride salt + water).";'
    ),
    (
        'status.innerHTML = "<span class=\'text-amber-300 font-bold\'>Acts as an Acid with Base:</span> $Al_2O_3 + 2NaOH \\to 2NaAlO_2 + H_2O$ (Forms Sodium aluminate salt + water).";',
        'status.innerHTML = "<span class=\'text-amber-300 font-bold\'>Acts as an Acid with Base:</span> Al₂O₃ + 2NaOH → 2NaAlO₂ + H₂O (Forms Sodium aluminate salt + water).";'
    ),
    (
        'status.innerHTML = "<span class=\'text-rose-400 font-bold\'>Sodium Ignites on Cold Water!</span> $2Na + 2H_2O \\to 2NaOH + H_2\\uparrow + \\text{Heat}$. High exothermicity sets hydrogen on fire!";',
        'status.innerHTML = "<span class=\'text-rose-400 font-bold\'>Sodium Ignites on Cold Water!</span> 2Na + 2H₂O → 2NaOH + H₂↑ + Heat. High exothermicity sets hydrogen on fire!";'
    ),
    (
        'status.innerHTML = "<span class=\'text-emerald-400 font-bold\'>Calcium Starts Floating!</span> $Ca + 2H_2O \\to Ca(OH)_2 + H_2$. Hydrogen bubbles stick to metal surface, buoying it up.";',
        'status.innerHTML = "<span class=\'text-emerald-400 font-bold\'>Calcium Starts Floating!</span> Ca + 2H₂O → Ca(OH)₂ + H₂↑. Hydrogen bubbles stick to metal surface, buoying it up.";'
    ),
    (
        'status.innerHTML = "<span class=\'text-slate-300 font-bold\'>Red-Hot Iron Reacts with Steam:</span> $3Fe(s) + 4H_2O(g) \\to Fe_3O_4(s) + 4H_2(g)$ (Requires steam, no reaction with cold water).";',
        'status.innerHTML = "<span class=\'text-slate-300 font-bold\'>Red-Hot Iron Reacts with Steam:</span> 3Fe(s) + 4H₂O(g) → Fe₃O₄(s) + 4H₂(g) (Requires steam, no reaction with cold water).";'
    ),
    (
        'status.innerHTML = "<span class=\'text-emerald-400 font-bold\'>Iron Displaces Copper!</span> $Fe + CuSO_4 \\to FeSO_4 + Cu$. Solution turns pale green and reddish copper coats the nail.";',
        'status.innerHTML = "<span class=\'text-emerald-400 font-bold\'>Iron Displaces Copper!</span> Fe + CuSO₄ → FeSO₄ + Cu. Solution turns pale green and reddish copper coats the nail.";'
    ),
    (
        'status.innerHTML = "<span class=\'text-emerald-400 font-bold\'>Thermal Reduction of Cinnabar:</span> $2HgS + 3O_2 \\xrightarrow{\\Delta} 2HgO + 2SO_2$, then $2HgO \\xrightarrow{\\Delta} 2Hg(l) + O_2$. Pure liquid mercury condensed!";',
        'status.innerHTML = "<span class=\'text-emerald-400 font-bold\'>Thermal Reduction of Cinnabar:</span> 2HgS + 3O₂ → 2HgO + 2SO₂, then 2HgO → 2Hg(l) + O₂. Pure liquid mercury condensed!";'
    ),
    (
        'status.innerHTML = "<span class=\'text-amber-300 font-bold\'>Thermit Flare Ignited!</span> $Fe_2O_3 + 2Al \\to 2Fe(l) + Al_2O_3$. White-hot molten iron flows into railway fracture and fuses it!";',
        'status.innerHTML = "<span class=\'text-amber-300 font-bold\'>Thermit Flare Ignited!</span> Fe₂O₃ + 2Al → 2Fe(l) + Al₂O₃. White-hot molten iron flows into railway fracture and fuses it!";'
    ),
    (
        'status.innerHTML = "<span class=\'text-rose-400 font-bold\'>Test Tube A (Air + Water):</span> Heavy brown flaky rust ($Fe_2O_3\\cdot xH_2O$) forms! Both moisture and oxygen present.";',
        'status.innerHTML = "<span class=\'text-rose-400 font-bold\'>Test Tube A (Air + Water):</span> Heavy brown flaky rust (Fe₂O₃·xH₂O) forms! Both moisture and oxygen present.";'
    )
]

fix_file('public/animations/metals-and-non-metals.html', mn_reps)

# 3. acids-bases-and-salts.html
ab_reps = [
    (
        'status.innerHTML = "<span class=\'text-amber-300 font-bold\'>Stage 1 (Milkiness):</span> $Ca(OH)_2 + CO_2 \\to CaCO_3\\downarrow + H_2O$. Insoluble calcium carbonate precipitates white!";',
        'status.innerHTML = "<span class=\'text-amber-300 font-bold\'>Stage 1 (Milkiness):</span> Ca(OH)₂ + CO₂ → CaCO₃↓ + H₂O. Insoluble calcium carbonate precipitates white!";'
    ),
    (
        'status.innerHTML = "<span class=\'text-emerald-400 font-bold\'>Stage 2 (Clear Solution):</span> $CaCO_3 + H_2O + CO_2 \\to Ca(HCO_3)_2(aq)$. Soluble calcium hydrogencarbonate dissolves the milkiness!";',
        'status.innerHTML = "<span class=\'text-emerald-400 font-bold\'>Stage 2 (Clear Solution):</span> CaCO₃ + H₂O + CO₂ → Ca(HCO₃)₂(aq). Soluble calcium hydrogencarbonate dissolves the milkiness!";'
    ),
    (
        'status.innerHTML = "<span class=\'text-rose-400 font-bold\'>Moist Blue Litmus turns RED!</span> $HCl(g) + H_2O(l) \\to H_3O^+(aq) + Cl^-(aq)$. Water is essential for acid ionisation!";',
        'status.innerHTML = "<span class=\'text-rose-400 font-bold\'>Moist Blue Litmus turns RED!</span> HCl(g) + H₂O(l) → H₃O⁺(aq) + Cl⁻(aq). Water is essential for acid ionisation!";'
    ),
    (
        'status.innerHTML = "<span class=\'text-emerald-400 font-bold\'>POP Sets Hard as Gypsum!</span> $CaSO_4\\cdot\\frac{1}{2}H_2O + 1\\frac{1}{2}H_2O \\to CaSO_4\\cdot 2H_2O$. Forms rigid interlocking crystals in 10 minutes!";',
        'status.innerHTML = "<span class=\'text-emerald-400 font-bold\'>POP Sets Hard as Gypsum!</span> CaSO₄·½H₂O + 1½H₂O → CaSO₄·2H₂O. Forms rigid interlocking crystals in 10 minutes!";'
    ),
    (
        'status.innerHTML = "<span class=\'text-slate-300 font-bold\'>Dry White POP Powder:</span> Calcium sulphate hemihydrate ($CaSO_4\\cdot\\frac{1}{2}H_2O$) produced by heating gypsum at $373\\text{ K}$.";',
        'status.innerHTML = "<span class=\'text-slate-300 font-bold\'>Dry White POP Powder:</span> Calcium sulphate hemihydrate (CaSO₄·½H₂O) produced by heating gypsum at 373 K.";'
    )
]

fix_file('public/animations/acids-bases-and-salts.html', ab_reps)
print("Done fixing files!")

