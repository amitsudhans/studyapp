# -*- coding: utf-8 -*-
"""
Generator script for Class 7 Science Chapter 2: Exploring Substances: Acidic, Basic, and Neutral
Simulator templates: 16 bespoke SVG/HTML interactive labs
"""

SIMULATORS = {
    # 1. Household Substance Matrix
    "household_substance_matrix": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-amber-400">Lab Simulator 1</span>
            <h3 class="text-sm font-bold text-slate-100">Household Substances: Acid, Base or Neutral?</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-rose-500/20 text-rose-300 border border-rose-500/30 font-semibold" id="substanceClassBadge">Acidic (Citric Acid)</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="substanceSvg" viewBox="0 0 500 240" class="w-full h-auto max-h-[220px]"></svg>
        </div>

        <div class="grid grid-cols-3 gap-1.5 text-xs">
          <button data-item="lemon" class="substanceBtn px-2 py-1.5 rounded-lg bg-amber-600 text-white font-bold transition">1. Lemon Juice</button>
          <button data-item="vinegar" class="substanceBtn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition">2. Vinegar</button>
          <button data-item="water" class="substanceBtn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition">3. Pure Water</button>
          <button data-item="baking" class="substanceBtn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition">4. Baking Soda</button>
          <button data-item="soap" class="substanceBtn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition">5. Soap Water</button>
          <button data-item="lime" class="substanceBtn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition">6. Lime Water</button>
        </div>

        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300" id="substanceDesc">
          <strong>Lemon Juice:</strong> Naturally sour taste due to citric acid ($\text{C}_6\text{H}_8\text{O}_7$). Turns blue litmus red. $\text{pH} \approx 2.2$.
        </div>
      </div>
    """,

    # 2. Litmus Paper Test Bench
    "litmus_test_bench": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-blue-400">Lab Simulator 2</span>
            <h3 class="text-sm font-bold text-slate-100">Interactive Litmus Paper Test Bench</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-blue-500/20 text-blue-300 border border-blue-500/30 font-semibold" id="litmusResultBadge">Blue Litmus ➔ RED</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="litmusSvg" viewBox="0 0 500 240" class="w-full h-auto max-h-[220px]"></svg>
        </div>

        <div class="grid grid-cols-3 gap-2 text-xs">
          <button data-sol="acid" class="litmusSolBtn px-2.5 py-1.5 rounded-lg bg-rose-600 text-white font-bold transition">1. Acid (Lemon / HCl)</button>
          <button data-sol="neutral" class="litmusSolBtn px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition">2. Distilled Water</button>
          <button data-sol="base" class="litmusSolBtn px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition">3. Base (Soap / NaOH)</button>
        </div>

        <div class="p-2 rounded-xl bg-slate-950 border border-slate-800 flex justify-between items-center text-[11px] font-mono">
          <span class="text-rose-400 font-bold" id="redLitmusText">Red Litmus: Stays RED</span>
          <span class="text-cyan-400 font-bold" id="blueLitmusText">Blue Litmus: Turns RED ✔</span>
        </div>
      </div>
    """,

    # 3. Red Rose Extract Indicator
    "red_rose_indicator_lab": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-rose-400">Lab Simulator 3</span>
            <h3 class="text-sm font-bold text-slate-100">Red Rose Petal Extract Lab</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-rose-500/20 text-rose-300 border border-rose-500/30 font-semibold" id="roseColorBadge">Acid: Turns Deep Red</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="roseSvg" viewBox="0 0 500 240" class="w-full h-auto max-h-[220px]"></svg>
        </div>

        <div class="grid grid-cols-3 gap-2 text-xs">
          <button data-test="acid" class="roseBtn px-2.5 py-1.5 rounded-lg bg-rose-600 text-white font-bold transition">1. Acidic Solution</button>
          <button data-test="neutral" class="roseBtn px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition">2. Neutral Water</button>
          <button data-test="base" class="roseBtn px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition">3. Basic Solution</button>
        </div>

        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300" id="roseDesc">
          Anthocyanin pigments in red rose petals respond to pH: turns <strong>vivid deep red</strong> in acidic solutions and <strong>emerald green</strong> in alkaline solutions!
        </div>
      </div>
    """,

    # 4. Turmeric Paper & Curry Stain
    "turmeric_curry_lab": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-amber-400">Lab Simulator 4</span>
            <h3 class="text-sm font-bold text-slate-100">Turmeric (Haldi) & The Red Curry Stain</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-amber-500/20 text-amber-300 border border-amber-500/30 font-semibold" id="turmericStatus">Natural Yellow State</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="turmericSvg" viewBox="0 0 500 240" class="w-full h-auto max-h-[220px]"></svg>
        </div>

        <div class="grid grid-cols-3 gap-2 text-xs">
          <button id="applyNeutralBtn" class="px-2.5 py-1.5 rounded-lg bg-amber-600 text-white font-bold transition">1. Fresh Curry (Yellow)</button>
          <button id="applySoapBtn" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition">2. Rub Soap (Alkaline)</button>
          <button id="applyLemonBtn" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition">3. Rinse + Lemon (Acid)</button>
        </div>

        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300" id="turmericExplanation">
          Curcumin in turmeric stays <strong>yellow</strong> in acidic and neutral conditions. When alkaline laundry soap is rubbed on the stain, it turns <strong>reddish-brown</strong>!
        </div>
      </div>
    """,

    # 5. China Rose & Floral Spectra
    "china_rose_spectrum_lab": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-pink-400">Lab Simulator 5</span>
            <h3 class="text-sm font-bold text-slate-100">China Rose (Hibiscus) & Cabbage Spectrum</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-pink-500/20 text-pink-300 border border-pink-500/30 font-semibold" id="chinaRoseBadge">China Rose: Magenta in Acid</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="chinaRoseSvg" viewBox="0 0 500 240" class="w-full h-auto max-h-[220px]"></svg>
        </div>

        <div class="grid grid-cols-3 gap-2 text-xs">
          <button data-med="acid" class="chinaMedBtn px-2.5 py-1.5 rounded-lg bg-pink-600 text-white font-bold transition">1. Acidic (pH 2)</button>
          <button data-med="neutral" class="chinaMedBtn px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition">2. Neutral (pH 7)</button>
          <button data-med="base" class="chinaMedBtn px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition">3. Basic (pH 11)</button>
        </div>

        <div class="p-2 rounded-xl bg-slate-950 border border-slate-800 flex justify-between text-xs text-slate-300 font-mono">
          <span>China Rose: <strong class="text-pink-400" id="crColorText">Dark Pink (Magenta)</strong></span>
          <span>Red Cabbage: <strong class="text-rose-400" id="rcColorText">Bright Red</strong></span>
        </div>
      </div>
    """,

    # 6. Olfactory Odor Meter Lab
    "olfactory_odor_lab": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-emerald-400">Lab Simulator 6</span>
            <h3 class="text-sm font-bold text-slate-100">Olfactory Indicator (Odor Science)</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold" id="odorStatusBadge">Odor: Strong & Intact ✔</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="olfactorySvg" viewBox="0 0 500 240" class="w-full h-auto max-h-[220px]"></svg>
        </div>

        <div class="grid grid-cols-2 gap-3 text-xs">
          <button id="odorAcidBtn" class="px-3 py-2 rounded-xl bg-emerald-600 text-white font-bold transition">
            1. Treat with Acid (Dilute HCl)
          </button>
          <button id="odorBaseBtn" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition">
            2. Treat with Base (NaOH Solution)
          </button>
        </div>

        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300" id="odorDesc">
          <strong>Acidic Medium:</strong> Onion/vanilla organic aroma molecules remain intact; the characteristic scent is strongly perceived. In basic medium, the smell is completely destroyed!
        </div>
      </div>
    """,

    # 7. Phenolphthalein Chamber Lab
    "phenolphthalein_chamber_lab": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-pink-400">Lab Simulator 7</span>
            <h3 class="text-sm font-bold text-slate-100">Synthetic Phenolphthalein Indicator</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-slate-800 text-slate-400 border border-slate-700 font-semibold" id="phptStateBadge">Acidic: COLORLESS</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="phptSvg" viewBox="0 0 500 240" class="w-full h-auto max-h-[220px]"></svg>
        </div>

        <div class="flex items-center justify-between pt-1">
          <button id="phptAddBaseBtn" class="px-3.5 py-1.5 rounded-xl bg-pink-600 hover:bg-pink-500 text-white font-bold text-xs transition shadow-md shadow-pink-600/30">
            + Add Base Drops (NaOH)
          </button>
          <button id="phptAddAcidBtn" class="px-3.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold text-xs transition">
            + Add Acid Drops (HCl)
          </button>
          <button id="phptResetBtn" class="px-2.5 py-1.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-slate-400 text-xs transition">
            Reset
          </button>
        </div>
      </div>
    """,

    # 8. Universal pH Scale Strip
    "universal_ph_scale_strip": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-cyan-400">Lab Simulator 8</span>
            <h3 class="text-sm font-bold text-slate-100">Universal pH Spectrum & Meter</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold" id="phValueBadge">pH 7.0: Pure Water (Neutral)</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="phStripSvg" viewBox="0 0 500 230" class="w-full h-auto max-h-[210px]"></svg>
        </div>

        <div class="space-y-1">
          <div class="flex justify-between text-xs text-slate-400">
            <span class="text-rose-400 font-bold">Acidic (pH 0)</span>
            <span class="text-emerald-400 font-bold">Neutral (pH 7)</span>
            <span class="text-purple-400 font-bold">Basic (pH 14)</span>
          </div>
          <input type="range" id="phSlider" min="0" max="14" value="7" step="0.5" class="w-full accent-cyan-500 cursor-pointer">
        </div>

        <div class="p-2 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 flex justify-between items-center font-mono">
          <span>Target Sample: <strong class="text-cyan-400" id="phSampleName">Distilled Water</strong></span>
          <span>Color: <strong class="text-emerald-400" id="phColorName">Emerald Green</strong></span>
        </div>
      </div>
    """,

    # 9. Neutralisation Reaction Chamber
    "neutralisation_reaction_chamber": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-emerald-400">Lab Simulator 9</span>
            <h3 class="text-sm font-bold text-slate-100">Neutralisation Reactor & Heat Monitor</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold" id="reactionStateBadge">Ready: Acid + Base</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="neutReactSvg" viewBox="0 0 500 240" class="w-full h-auto max-h-[220px]"></svg>
        </div>

        <div class="flex items-center justify-between pt-1">
          <button id="triggerReactionBtn" class="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition shadow-md shadow-emerald-600/30">
            ⚡ Pour & Neutralize (HCl + NaOH)
          </button>
          <div class="text-xs text-amber-300 font-mono" id="tempReadout">Thermometer: 24.0°C (Ambient)</div>
        </div>
      </div>
    """,

    # 10. Titration Burette Lab
    "titration_burette_lab": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-pink-400">Lab Simulator 10</span>
            <h3 class="text-sm font-bold text-slate-100">Volumetric Titration & End-Point</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-slate-800 text-slate-300 border border-slate-700 font-semibold" id="titrationBadge">Flask: Acidic (Colorless)</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="titrationSvg" viewBox="0 0 500 240" class="w-full h-auto max-h-[220px]"></svg>
        </div>

        <div class="flex items-center justify-between pt-1">
          <button id="dispenseDropBtn" class="px-3.5 py-1.5 rounded-xl bg-pink-600 hover:bg-pink-500 text-white font-bold text-xs transition shadow-md shadow-pink-600/30">
            💧 Dispense Base Drop
          </button>
          <span class="text-xs font-mono text-cyan-300" id="titrationDropsText">Base Added: 0.0 mL (0 drops)</span>
          <button id="resetTitrationBtn" class="px-2.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-400 text-xs transition">
            Reset
          </button>
        </div>
      </div>
    """,

    # 11. Ant Bite Neutraliser Lab
    "ant_bite_neutraliser_lab": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-rose-400">Lab Simulator 11</span>
            <h3 class="text-sm font-bold text-slate-100">Ant Bite Venom & Calamine Neutraliser</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-rose-500/20 text-rose-300 border border-rose-500/30 font-semibold" id="antBiteStatus">Skin: Acidic Formic Injection ⚠️</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="antBiteSvg" viewBox="0 0 500 240" class="w-full h-auto max-h-[220px]"></svg>
        </div>

        <div class="grid grid-cols-2 gap-3 text-xs">
          <button id="applyBakingSodaBtn" class="px-3 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold transition shadow-md shadow-emerald-600/30">
            Apply Moist Baking Soda (NaHCO3)
          </button>
          <button id="applyCalamineBtn" class="px-3 py-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold transition shadow-md shadow-cyan-600/30">
            Apply Calamine Lotion (ZnCO3)
          </button>
        </div>
      </div>
    """,

    # 12. Soil pH Management Lab
    "soil_ph_management_lab": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-emerald-400">Lab Simulator 12</span>
            <h3 class="text-sm font-bold text-slate-100">Agricultural Soil pH Regulator</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-rose-500/20 text-rose-300 border border-rose-500/30 font-semibold" id="soilStatusBadge">Soil: Excessively Acidic (pH 4.8)</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="soilSvg" viewBox="0 0 500 240" class="w-full h-auto max-h-[220px]"></svg>
        </div>

        <div class="grid grid-cols-2 gap-3 text-xs">
          <button id="addLimeBtn" class="px-3 py-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold transition">
            Add Slaked Lime (Ca(OH)2) ➔ Neutralize
          </button>
          <button id="addManureBtn" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition">
            Add Organic Manure (For Basic Soil)
          </button>
        </div>
      </div>
    """,

    # 13. Factory Effluent Plant Lab
    "factory_effluent_plant_lab": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-cyan-400">Lab Simulator 13</span>
            <h3 class="text-sm font-bold text-slate-100">Factory Effluent Neutralisation Plant</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold" id="riverSafetyBadge">River Safe (pH 7.1) ✔</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="effluentSvg" viewBox="0 0 500 240" class="w-full h-auto max-h-[220px]"></svg>
        </div>

        <div class="space-y-1">
          <div class="flex justify-between text-xs text-slate-400">
            <span>Lime Treatment Dosing Rate:</span>
            <span id="limeDoseText" class="text-cyan-400 font-mono font-bold">Optimal Neutralization (100%)</span>
          </div>
          <input type="range" id="limeValveSlider" min="0" max="100" value="100" step="10" class="w-full accent-cyan-500 cursor-pointer">
        </div>
      </div>
    """,

    # 14. Antacid & Dental Health Lab
    "antacid_dental_health_lab": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-blue-400">Lab Simulator 14</span>
            <h3 class="text-sm font-bold text-slate-100">Stomach Antacid & Dental Protection</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-blue-500/20 text-blue-300 border border-blue-500/30 font-semibold" id="bioModeBadge">Stomach: Hyperacidity Relief</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="bioHealthSvg" viewBox="0 0 500 240" class="w-full h-auto max-h-[220px]"></svg>
        </div>

        <div class="grid grid-cols-2 gap-3 text-xs">
          <button id="toggleStomachBtn" class="px-3 py-2 rounded-xl bg-blue-600 text-white font-bold transition">
            1. Stomach: Take Antacid (Mg(OH)2)
          </button>
          <button id="toggleDentalBtn" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition">
            2. Teeth: Brush with Alkaline Toothpaste
          </button>
        </div>
      </div>
    """,

    # 15. Acharya P.C. Ray Historical Lab
    "pc_ray_chemistry_heritage": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-amber-400">Lab Simulator 15</span>
            <h3 class="text-sm font-bold text-slate-100">Acharya P.C. Ray & Indian Chemistry</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-amber-500/20 text-amber-300 border border-amber-500/30 font-semibold" id="pcRayBadge">Mercurous Nitrite (1896)</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="pcRaySvg" viewBox="0 0 500 240" class="w-full h-auto max-h-[220px]"></svg>
        </div>

        <div class="grid grid-cols-3 gap-2 text-xs">
          <button data-view="nitrite" class="rayBtn px-2 py-1.5 rounded-lg bg-amber-600 text-white font-bold transition">1. Nitrite Discovery</button>
          <button data-view="bengal" class="rayBtn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition">2. Bengal Chemicals</button>
          <button data-view="rasashastra" class="rayBtn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition">3. Hindu Chemistry</button>
        </div>
      </div>
    """,

    # 16. Master Substance Wheel
    "master_substance_wheel": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-emerald-400">Lab Simulator 16</span>
            <h3 class="text-sm font-bold text-slate-100">Master Acid-Base Equation Synthesizer</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold" id="synthSaltBadge">Salt: Sodium Chloride (NaCl)</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="synthSvg" viewBox="0 0 500 230" class="w-full h-auto max-h-[210px]"></svg>
        </div>

        <div class="grid grid-cols-2 gap-3 text-xs">
          <div>
            <label class="block text-slate-400 text-[10px] font-bold uppercase mb-1">Select Acid (H+ donor):</label>
            <select id="synthAcidSelect" class="w-full p-1.5 rounded-lg bg-slate-950 border border-slate-700 text-xs text-rose-300 font-mono">
              <option value="hcl">Hydrochloric Acid (HCl)</option>
              <option value="h2so4">Sulfuric Acid (H2SO4)</option>
              <option value="hno3">Nitric Acid (HNO3)</option>
              <option value="ch3cooh">Acetic Acid (CH3COOH)</option>
            </select>
          </div>
          <div>
            <label class="block text-slate-400 text-[10px] font-bold uppercase mb-1">Select Base (OH- donor):</label>
            <select id="synthBaseSelect" class="w-full p-1.5 rounded-lg bg-slate-950 border border-slate-700 text-xs text-cyan-300 font-mono">
              <option value="naoh">Sodium Hydroxide (NaOH)</option>
              <option value="koh">Potassium Hydroxide (KOH)</option>
              <option value="caoh2">Calcium Hydroxide (Ca(OH)2)</option>
              <option value="mgoh2">Magnesium Hydroxide (Mg(OH)2)</option>
            </select>
          </div>
        </div>
      </div>
    """
}

with open(".agents/class7_science_substances_sims.py", "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 7 Science Chapter 2: Exploring Substances Simulator Templates"""\n\n')
    f.write("SIMULATORS_HTML = " + repr(SIMULATORS) + "\n")

print(f"Generated .agents/class7_science_substances_sims.py with {len(SIMULATORS)} simulators.")

