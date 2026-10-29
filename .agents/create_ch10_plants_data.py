# -*- coding: utf-8 -*-
"""
Generates the comprehensive data module for Chapter 10: Life Processes in Plants
NCERT Class 7 Science.
Strictly zero raw LaTeX code or commands. Clean Unicode everywhere.
"""
import json
import re

slides = [
    # Slide 1
    {
        "id": 1,
        "slide_num": 1,
        "title": "Autotrophy: Producers of the Biosphere",
        "subtitle": "Chapter 10.1 & 10.2: How Plants Power Life on Earth",
        "badge": "Core Foundation",
        "summary": "Unlike animals that must ingest ready-made organic matter, green plants are primary autotrophs. They convert radiant solar photons, ambient carbon dioxide, and soil water into chemical food energy, sustaining virtually all terrestrial ecosystems.",
        "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        Every living organism on Earth requires an uninterrupted supply of metabolic energy to survive, grow, repair tissues, and reproduce. In Chapter 9, we discovered that animals are <strong class="text-amber-400">heterotrophs</strong>—they must feed upon other organisms because their bodies cannot synthesize organic nutrients from inorganic atmospheric molecules.
    </p>
    <div class="p-4 rounded-xl bg-emerald-950/40 border border-emerald-500/30">
        <h4 class="font-bold text-emerald-300 text-base mb-1">The Miracle of Autotrophic Nutrition</h4>
        <p class="text-sm text-slate-300 leading-relaxed">
            Green plants are <strong class="text-emerald-400">autotrophs</strong> (from Greek <em>auto</em> = self, <em>trophe</em> = nourishment). Through the light-harvesting process of <strong class="text-emerald-300">photosynthesis</strong>, they transform simple, low-energy inorganic raw materials—carbon dioxide (CO₂) from the ambient air and water (H₂O) from the soil—into rich, high-energy organic carbohydrates (glucose and starch) while replenishing Earth's atmospheric oxygen (O₂).
        </p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3 pt-2">
        <div class="p-3 rounded-lg bg-slate-900/60 border border-slate-700/60">
            <span class="text-xs font-semibold text-emerald-400 uppercase tracking-wider block mb-1">Primary Producers</span>
            <p class="text-xs text-slate-300">Plants occupy Trophic Level 1 in ecological pyramids. Every bite of food eaten by herbivores and carnivores traces its molecular origin back to sunlight trapped inside plant leaves.</p>
        </div>
        <div class="p-3 rounded-lg bg-slate-900/60 border border-slate-700/60">
            <span class="text-xs font-semibold text-cyan-400 uppercase tracking-wider block mb-1">Atmospheric Guardians</span>
            <p class="text-xs text-slate-300">Plants serve as massive carbon sinks and oxygen factories, maintaining the delicate 21% oxygen and 0.04% carbon dioxide planetary equilibrium essential for animal respiration.</p>
        </div>
    </div>
</div>
""",
        "takeaways": [
            "Plants are autotrophs capable of manufacturing organic nutrients from inorganic minerals, water, and CO₂.",
            "Photosynthesis converts luminous solar radiant energy into stable chemical bond energy stored in glucose.",
            "All heterotrophic animals, directly or indirectly, depend on plants for food energy and breathable oxygen."
        ],
        "checkpoints": [
            {
                "id": "cp1_1",
                "question": "Why are green plants classified as autotrophs in ecological food chains?",
                "options": [
                    "They digest decomposed soil organic debris through their roots",
                    "They synthesize their own organic food using sunlight, water, and carbon dioxide",
                    "They actively hunt microscopic insects for all their metabolic energy",
                    "They absorb ready-made starch directly from raindrops falling on leaves"
                ],
                "correct": 1,
                "explanation": "Plants are autotrophs because they synthesize high-energy organic compounds (carbohydrates) from inorganic environmental precursors (sunlight, CO₂, and H₂O) via photosynthesis."
            },
            {
                "id": "cp1_2",
                "question": "What gas is released into the atmosphere as a vital byproduct of plant photosynthesis?",
                "options": [
                    "Nitrogen gas (N₂)",
                    "Methane gas (CH₄)",
                    "Oxygen gas (O₂)",
                    "Sulfur dioxide (SO₂)"
                ],
                "correct": 2,
                "explanation": "During photosynthesis, the photolysis of absorbed water molecules releases oxygen gas (O₂) into the surrounding atmosphere, which sustains animal respiration."
            }
        ]
    },

    # Slide 2
    {
        "id": 2,
        "slide_num": 2,
        "title": "10.1 How Do Plants Grow?: Essential Growth Factors",
        "subtitle": "Experimental Verification: The Roles of Water and Sunlight",
        "badge": "Controlled Experiment",
        "summary": "Through controlled botanical setups with potted seedlings, we observe that plants require both uninterrupted solar illumination and regular moisture. Without water, cells lose turgor and wilt; without light, seedlings undergo etiolation and starvation.",
        "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        Plant growth is not merely a spontaneous increase in size—it is a tightly regulated physiological process requiring structural cell division, cell elongation, and continuous metabolic fuel. When a seed germinates, the embryonic root (<strong class="text-emerald-400">radicle</strong>) anchors into moist soil while the embryonic shoot (<strong class="text-emerald-400">plumule</strong>) ascends towards sunlight.
    </p>
    <div class="p-4 rounded-xl bg-slate-900/60 border border-slate-700/60">
        <h4 class="font-bold text-amber-300 text-sm mb-2">The Four-Pot Growth Investigation</h4>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs text-slate-300">
            <div class="p-2.5 rounded bg-emerald-950/40 border border-emerald-500/30">
                <strong class="text-emerald-400 block mb-1">Pot A: Sunlit + Watered (Control)</strong>
                Vigorous stem elongation, rich emerald green leaves, robust hydrostatic turgor pressure, active cell division.
            </div>
            <div class="p-2.5 rounded bg-rose-950/40 border border-rose-500/30">
                <strong class="text-rose-400 block mb-1">Pot B: Sunlit + Dehydrated</strong>
                Loss of cellular turgor, stomatal closure, droopiness and permanent wilting within days; xylem vessels dry out.
            </div>
            <div class="p-2.5 rounded bg-amber-950/40 border border-amber-500/30">
                <strong class="text-amber-400 block mb-1">Pot C: Dark Cupboard + Watered</strong>
                Etiolation: abnormally elongated, pale, yellowish-white spindly stems lacking chlorophyll; eventually collapses.
            </div>
            <div class="p-2.5 rounded bg-slate-950/40 border border-slate-600/30">
                <strong class="text-slate-400 block mb-1">Pot D: Dark + Dehydrated</strong>
                Rapid desiccation, total cessation of growth, shriveling of shoot tissue, and early plant death.
            </div>
        </div>
    </div>
    <p class="text-xs text-slate-300 leading-relaxed">
        <strong class="text-cyan-300">Scientific Conclusion:</strong> Neither water alone nor sunlight alone can sustain healthy botanical life. Both factors operate synergistically: water maintains hydrostatic turgidity and delivers dissolved minerals, while sunlight energizes photosynthesis.
    </p>
</div>
""",
        "takeaways": [
            "Water provides necessary hydrostatic turgor pressure for cell expansion and acts as a solvent for mineral transport.",
            "Sunlight is obligatory to stimulate chlorophyll biosynthesis and drive photosynthetic carbon fixation.",
            "Seedlings deprived of light become etiolated—spindly, fragile, and pale yellow—and quickly starve."
        ],
        "checkpoints": [
            {
                "id": "cp2_1",
                "question": "What happens to a healthy seedling placed in complete darkness for two weeks despite regular watering?",
                "options": [
                    "It grows thicker dark green leaves and flowers profusely",
                    "It develops pale yellow spindly stems (etiolation) due to lack of chlorophyll and light",
                    "Its leaves double their chlorophyll concentration to capture darkness",
                    "It converts into an insect-eating carnivorous plant immediately"
                ],
                "correct": 1,
                "explanation": "Without sunlight, plants cannot synthesize chlorophyll or carry out photosynthesis. They exhaust stored cotyledon reserves and undergo etiolation (producing pale yellow, spindly shoots)."
            },
            {
                "id": "cp2_2",
                "question": "Why does a plant wilt and droop when deprived of soil water?",
                "options": [
                    "Its cell walls lose internal hydrostatic turgor pressure",
                    "Its chlorophyll turns into heavy lead metal",
                    "Its leaves absorb too much atmospheric nitrogen gas",
                    "Its roots actively pull the stem downward into the soil"
                ],
                "correct": 0,
                "explanation": "Water fills the central vacuoles of plant cells, exerting turgor pressure against the rigid cell walls. Without water, cells lose turgidity, causing the stem and leaves to droop and wilt."
            }
        ]
    },

    # Slide 3
    {
        "id": 3,
        "slide_num": 3,
        "title": "10.2.1 Anatomy of a Leaf: Nature's Solar Collector",
        "subtitle": "Petiole, Lamina, Veins & Chloroplast-Rich Mesophyll",
        "badge": "Structural Biology",
        "summary": "Leaves are specialized flattened organs designed for maximal photon interception and gas exchange. From the protective waxy cuticle to the palisade mesophyll packed with chlorophyll-filled chloroplasts, each layer fulfills a dedicated role in food production.",
        "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        Leaves are appropriately celebrated as the <strong class="text-emerald-400">'food factories'</strong> of the botanical world. Their broad, flattened morphology—termed the <strong class="text-cyan-300">lamina</strong> or leaf blade—maximizes the surface area available to absorb incident sunlight.
    </p>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
        <div class="p-3 rounded-lg bg-slate-900/60 border border-slate-700/60">
            <h5 class="text-xs font-bold text-emerald-300 uppercase mb-1">1. Macroscopic Parts</h5>
            <ul class="text-xs text-slate-300 space-y-1">
                <li>• <strong class="text-slate-100">Petiole:</strong> Leaf stalk attaching the blade to the stem node.</li>
                <li>• <strong class="text-slate-100">Lamina:</strong> Flat green expanse capturing solar photons.</li>
                <li>• <strong class="text-slate-100">Midrib & Veins:</strong> Vascular conduits delivering water and exporting sugars.</li>
            </ul>
        </div>
        <div class="p-3 rounded-lg bg-slate-900/60 border border-slate-700/60">
            <h5 class="text-xs font-bold text-cyan-300 uppercase mb-1">2. Cellular Layers</h5>
            <ul class="text-xs text-slate-300 space-y-1">
                <li>• <strong class="text-slate-100">Cuticle:</strong> Water-repelling waxy coat minimizing transpiration.</li>
                <li>• <strong class="text-slate-100">Epidermis:</strong> Upper and lower transparent protective shields.</li>
                <li>• <strong class="text-slate-100">Mesophyll:</strong> Chloroplast-dense palisade and airy spongy tissue.</li>
            </ul>
        </div>
        <div class="p-3 rounded-lg bg-slate-900/60 border border-slate-700/60">
            <h5 class="text-xs font-bold text-amber-300 uppercase mb-1">3. The Chloroplast</h5>
            <ul class="text-xs text-slate-300 space-y-1">
                <li>• <strong class="text-slate-100">Organelle:</strong> Double-membrane kitchen of the plant cell.</li>
                <li>• <strong class="text-slate-100">Chlorophyll:</strong> Magnesium-bearing pigment absorbing red and blue light while reflecting green light.</li>
            </ul>
        </div>
    </div>
    <div class="p-3 rounded-xl bg-emerald-950/40 border border-emerald-500/30 text-xs text-slate-300">
        <strong class="text-emerald-300">Why are leaves green?</strong> Chlorophyll absorbs photon wavelengths in the blue (430–450 nm) and red (640–660 nm) spectral regions with extraordinary efficiency, while reflecting and transmitting green wavelengths (500–550 nm) directly to our retinas.
    </div>
</div>
""",
        "takeaways": [
            "The broad, flat leaf lamina provides a large surface area for solar capture and gas absorption.",
            "The mesophyll layer contains vertically packed palisade cells densely populated with chloroplasts.",
            "Chlorophyll selectively absorbs red and blue light photons, reflecting green wavelengths back to our eyes."
        ],
        "checkpoints": [
            {
                "id": "cp3_1",
                "question": "Which specific microscopic cellular organelle inside green leaf cells performs photosynthesis?",
                "options": [
                    "Mitochondrion",
                    "Chloroplast",
                    "Ribosome",
                    "Centriole"
                ],
                "correct": 1,
                "explanation": "Chloroplasts are the specialized photosynthetic organelles in plant cells that house chlorophyll pigments and enzymes for sugar production."
            },
            {
                "id": "cp3_2",
                "question": "What is the primary function of the waxy cuticle covering the upper leaf epidermis?",
                "options": [
                    "To digest falling dust particles",
                    "To prevent excessive evaporation of water from leaf tissues",
                    "To attract harmful insects to the stem",
                    "To absorb oxygen gas directly from the soil"
                ],
                "correct": 1,
                "explanation": "The waxy cuticle forms a hydrophobic, impermeable barrier over the outer epidermal cells, preventing excessive desiccation and water vapor loss."
            }
        ]
    },

    # Slide 4
    {
        "id": 4,
        "slide_num": 4,
        "title": "10.2.1 The Starch Test: Proving the Food Factory",
        "subtitle": "Decolourisation via Boiling Alcohol & The Iodine Reaction",
        "badge": "Classic Laboratory",
        "summary": "To confirm that leaves synthesize carbohydrates, botanists test for starch—the insoluble storage polymer of glucose. Because intense green chlorophyll masks subtle color changes, the leaf must first be decolourised in a hot ethanol water bath before applying amber iodine.",
        "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        Plants convert simple soluble glucose molecules produced during photosynthesis into an insoluble, multi-branched polysaccharide called <strong class="text-amber-400">starch</strong>. Testing for the presence of starch serves as conclusive empirical evidence of recent photosynthetic activity.
    </p>
    <div class="p-4 rounded-xl bg-slate-900/60 border border-slate-700/60">
        <h4 class="font-bold text-cyan-300 text-sm mb-2">The Standard 4-Step Starch Extraction Protocol</h4>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-2 text-xs">
            <div class="p-2 rounded bg-slate-800/80 border border-slate-700">
                <span class="font-bold text-amber-400 block mb-1">Step 1: Water Boil</span>
                Boil the plucked green leaf in beaker water for 2–3 minutes to kill cell protoplasm and rupture cellular membranes.
            </div>
            <div class="p-2 rounded bg-slate-800/80 border border-slate-700">
                <span class="font-bold text-amber-400 block mb-1">Step 2: Ethanol Bath</span>
                Immerse leaf in test tube with ethanol placed in a water bath; chlorophyll dissolves, rendering leaf pale creamy-white.
            </div>
            <div class="p-2 rounded bg-slate-800/80 border border-slate-700">
                <span class="font-bold text-amber-400 block mb-1">Step 3: Warm Rinse</span>
                Dip brittle decolourised leaf briefly in warm water to soften the cellulose cell walls and wash away residual alcohol.
            </div>
            <div class="p-2 rounded bg-slate-800/80 border border-slate-700">
                <span class="font-bold text-amber-400 block mb-1">Step 4: Iodine Test</span>
                Spread leaf in a petri dish; drop dilute brown iodine solution. Starch-rich zones turn intensely <strong class="text-blue-400">blue-black</strong>.
            </div>
        </div>
    </div>
    <div class="p-3 rounded-lg bg-rose-950/40 border border-rose-500/30 text-xs text-rose-200">
        <strong class="text-rose-400">Crucial Laboratory Safety Note:</strong> Alcohol (ethanol) is highly volatile and flammable! Never heat a test tube containing alcohol directly over an open Bunsen burner flame. Always use a hot water bath to avoid flash fires.
    </div>
</div>
""",
        "takeaways": [
            "Glucose synthesized during photosynthesis is rapidly assembled into insoluble starch granules for storage.",
            "Chlorophyll must be extracted with hot ethanol so that color changes during the iodine test can be observed clearly.",
            "Dilute iodine solution changes from yellowish-brown to deep blue-black in the presence of starch."
        ],
        "checkpoints": [
            {
                "id": "cp4_1",
                "question": "Why is a green leaf boiled in alcohol placed in a hot water bath rather than over a direct Bunsen burner flame?",
                "options": [
                    "Water baths make the leaf change directly into pure sugar",
                    "Alcohol is highly inflammable and can catch fire if exposed to a direct flame",
                    "Direct flames freeze the leaf instantly into solid ice",
                    "Boiling directly in flame increases the green color of chlorophyll"
                ],
                "correct": 1,
                "explanation": "Alcohol is flammable. Heating it safely inside a boiling water bath prevents the alcohol vapors from coming into direct contact with the burner flame."
            },
            {
                "id": "cp4_2",
                "question": "What characteristic color reaction confirms the presence of starch when iodine solution is dripped onto a decolourised leaf?",
                "options": [
                    "Bright pink to scarlet red",
                    "Milky white to transparent",
                    "Yellowish-brown turning to deep blue-black",
                    "Pale green turning to bright neon yellow"
                ],
                "correct": 2,
                "explanation": "Iodine molecules slip inside the helical amylose coils of starch, forming a polyiodide complex that shifts absorption from yellowish-brown to intense blue-black."
            }
        ]
    },

    # Slide 5
    {
        "id": 5,
        "slide_num": 5,
        "title": "10.2.2 The Essential Gas: Role of Carbon Dioxide",
        "subtitle": "Moll's Half-Leaf Experiment & Caustic Soda Absorption",
        "badge": "Gas Verification",
        "summary": "Carbon dioxide from atmospheric air provides the carbon atoms necessary to assemble carbohydrate backbones. In Moll's half-leaf experiment, enclosing half a leaf in a bottle containing caustic soda (which absorbs CO₂) proves that without CO₂, no starch can form.",
        "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        Air is a mixture of diverse gases: roughly 78% nitrogen, 21% oxygen, 0.9% argon, and approximately <strong class="text-emerald-400">0.04% carbon dioxide (CO₂)</strong>. Despite this modest concentration, carbon dioxide provides every single carbon atom required to forge plant sugars, starch, cellulose, and plant proteins.
    </p>
    <div class="p-4 rounded-xl bg-slate-900/60 border border-slate-700/60">
        <h4 class="font-bold text-amber-300 text-sm mb-2">Moll's Classic Half-Leaf Experiment Setup</h4>
        <div class="space-y-2 text-xs text-slate-300">
            <p>1. <strong class="text-slate-100">Destarching:</strong> A potted plant is kept in complete darkness for 48 hours to deplete all pre-existing starch stored in its leaves.</p>
            <p>2. <strong class="text-slate-100">The Split-Cork Chamber:</strong> A wide-mouthed glass bottle contains pellets or concentrated solution of <strong class="text-rose-400">potassium hydroxide (KOH) / caustic soda</strong>, a chemical that greedily absorbs gaseous CO₂:
                <br><span class="text-cyan-300 font-mono text-center block my-1">2 KOH + CO₂ → K₂CO₃ + H₂O</span>
            </p>
            <p>3. <strong class="text-slate-100">Assembly:</strong> One leaf, still firmly attached to the plant, is inserted through a split cork such that its apical outer half remains exposed to fresh atmospheric air, while its basal inner half is sealed inside the CO₂-free bottle.</p>
            <p>4. <strong class="text-slate-100">Sunlight Exposure & Test:</strong> After 4 to 6 hours of full sunlight, the leaf is plucked, decolourised in boiling ethanol, and treated with iodine.</p>
        </div>
    </div>
    <div class="p-3 rounded-lg bg-emerald-950/40 border border-emerald-500/30 text-xs text-slate-300">
        <strong class="text-emerald-300">Empirical Verdict:</strong> The outer exposed half turns vibrant <strong class="text-blue-400">blue-black</strong> (starch synthesized), while the inner half remains dull <strong class="text-amber-500">yellowish-brown</strong> (no starch). This conclusively proves that carbon dioxide is indispensable for photosynthesis.
    </div>
</div>
""",
        "takeaways": [
            "Destarching plants in the dark for 48 hours ensures that any newly detected starch is synthesized during the experiment.",
            "Potassium hydroxide (KOH) or caustic soda chemically scrubs carbon dioxide from enclosed air.",
            "Only the leaf section with access to CO₂ tests positive for starch with iodine, proving CO₂ is essential."
        ],
        "checkpoints": [
            {
                "id": "cp5_1",
                "question": "What is the specific role of caustic soda (KOH) in Moll's half-leaf experiment?",
                "options": [
                    "To generate extra bright sunlight inside the bottle",
                    "To chemically absorb and remove all carbon dioxide from the bottle air",
                    "To supply extra water directly to the tip of the leaf",
                    "To dye the leaf blue-black before adding iodine"
                ],
                "correct": 1,
                "explanation": "Potassium hydroxide (caustic soda) reacts with gaseous CO₂ to form potassium carbonate, creating a CO₂-free microenvironment inside the experimental glass flask."
            },
            {
                "id": "cp5_2",
                "question": "Why is the experimental potted plant placed in a dark cupboard for 2 days before setting up the experiment?",
                "options": [
                    "To allow the leaves to accumulate extra starch for the test",
                    "To destarch the leaves so pre-existing starch does not give a false positive",
                    "To destroy the plant's root system completely",
                    "To turn all green chlorophyll permanently into yellow carotene"
                ],
                "correct": 1,
                "explanation": "Keeping the plant in darkness for 48 hours halts photosynthesis, forcing cells to metabolize and clear out all pre-existing starch reserves (destarching)."
            }
        ]
    },

    # Slide 6
    {
        "id": 6,
        "slide_num": 6,
        "title": "10.2.3 The Master Chemistry: Photosynthesis in a Nutshell",
        "subtitle": "The Universal Balanced Chemical Equation & Energy Conversion",
        "badge": "Core Chemistry",
        "summary": "Photosynthesis is the foundational biochemical reaction of life on Earth. In the presence of sunlight absorbed by chlorophyll, carbon dioxide and water undergo redox transformation to yield energy-rich glucose and life-giving oxygen gas.",
        "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        The word <strong class="text-emerald-400">photosynthesis</strong> unites two classical Greek roots: <em>photo</em> (meaning light) and <em>synthesis</em> (meaning putting together). It encapsulates the molecular miracle whereby photon energy drives the assembly of carbon chains.
    </p>
    <div class="p-4 rounded-xl bg-slate-900/80 border border-emerald-500/40 text-center">
        <span class="text-xs uppercase tracking-wider text-emerald-400 font-bold block mb-2">The Balanced Word & Chemical Equations</span>
        <div class="text-sm font-semibold text-slate-200 mb-2">
            Carbon dioxide + Water + Sunlight [Chlorophyll] → Glucose + Oxygen
        </div>
        <div class="text-base sm:text-lg font-mono font-bold text-amber-300 bg-slate-950/70 p-3 rounded-lg border border-slate-700">
            6 CO₂ + 6 H₂O + Light Energy → C₆H₁₂O₆ + 6 O₂
        </div>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs text-slate-300">
        <div class="p-3 rounded-lg bg-slate-900/60 border border-slate-700/60">
            <strong class="text-cyan-300 block mb-1">Reactants (Inputs)</strong>
            <p>• <strong class="text-slate-100">Carbon Dioxide (6 CO₂):</strong> Enters through stomata from atmospheric air.</p>
            <p>• <strong class="text-slate-100">Water (6 H₂O):</strong> Absorbed by root hairs from soil capillary moisture.</p>
            <p>• <strong class="text-slate-100">Photons:</strong> Energize pigment electrons inside thylakoid membranes.</p>
        </div>
        <div class="p-3 rounded-lg bg-slate-900/60 border border-slate-700/60">
            <strong class="text-emerald-300 block mb-1">Products (Outputs)</strong>
            <p>• <strong class="text-slate-100">Glucose (C₆H₁₂O₆):</strong> Hexose sugar used for cellular fuel, growth, or polymerized into storage starch and structural cellulose.</p>
            <p>• <strong class="text-slate-100">Oxygen (6 O₂):</strong> Diffuses out of stomata to sustain all aerobic respiration.</p>
        </div>
    </div>
</div>
""",
        "takeaways": [
            "Photosynthesis is a solar-powered anabolic process that synthesizes glucose from carbon dioxide and water.",
            "The balanced equation is: 6 CO₂ + 6 H₂O + Light Energy [Chlorophyll] → C₆H₁₂O₆ + 6 O₂.",
            "Water molecules are split (photolysis) to provide electrons and protons, liberating pure oxygen gas as a byproduct."
        ],
        "checkpoints": [
            {
                "id": "cp6_1",
                "question": "In the chemical formula of photosynthesis (6 CO₂ + 6 H₂O → C₆H₁₂O₆ + 6 O₂), what does C₆H₁₂O₆ represent?",
                "options": [
                    "Sodium chloride table salt",
                    "Glucose carbohydrate sugar",
                    "Carbonic acid",
                    "Liquid nitrogen"
                ],
                "correct": 1,
                "explanation": "C₆H₁₂O₆ is the chemical formula for glucose, a six-carbon monosaccharide sugar synthesized during photosynthesis."
            },
            {
                "id": "cp6_2",
                "question": "Where does the oxygen released during plant photosynthesis fundamentally originate?",
                "options": [
                    "From the split of absorbed soil water molecules (H₂O)",
                    "From the nitrogen gas inside plant stems",
                    "From the breakdown of calcium ions in leaf cells",
                    "From air trapped under the flower petals"
                ],
                "correct": 0,
                "explanation": "During the light-dependent phase of photosynthesis, absorbed water molecules (H₂O) are photolytically cleaved, releasing O₂ gas into the air."
            }
        ]
    },

    # Slide 7
    {
        "id": 7,
        "slide_num": 7,
        "title": "10.2.3 Oxygen Evolution: The Ingenhousz Hydrilla Experiment",
        "subtitle": "Trapping Gas Bubbles with an Inverted Funnel & Glowing Splinter Test",
        "badge": "Historical Discovery",
        "summary": "In 1779, Dutch physician Jan Ingenhousz demonstrated that only green parts of plants exposed to sunlight release gas bubbles. Using aquatic Hydrilla under an inverted glass funnel, the collected gas rekindles a glowing wooden splinter, proving it is pure oxygen.",
        "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        How do scientists prove that the gas bubbling from aquatic weeds in a sunlit pond is genuinely oxygen? In the late 18th century, <strong class="text-amber-400">Jan Ingenhousz</strong> built upon Joseph Priestley's bell jar discoveries to prove that plants restore fouled air strictly in the presence of <strong class="text-cyan-300">light</strong>.
    </p>
    <div class="p-4 rounded-xl bg-slate-900/60 border border-slate-700/60">
        <h4 class="font-bold text-emerald-300 text-sm mb-2">The Inverted Funnel Hydrilla Demonstration</h4>
        <div class="space-y-2 text-xs text-slate-300">
            <p>1. <strong class="text-slate-100">Setup:</strong> Fresh sprigs of the submerged aquatic plant <em>Hydrilla verticillata</em> are placed under a short-stemmed glass funnel inside a glass beaker filled with clear pond water containing dissolved bicarbonate.</p>
            <p>2. <strong class="text-slate-100">Water-Filled Test Tube:</strong> A test tube completely filled with water is inverted over the stem of the glass funnel, ensuring no initial air bubble exists at the top.</p>
            <p>3. <strong class="text-slate-100">Sunlight vs Shade:</strong> When placed in direct sunlight, a continuous stream of tiny silvery gas bubbles streams from the cut stems, rising and displacing water downwards at the tip of the test tube. In the dark, bubble generation ceases entirely.</p>
            <p>4. <strong class="text-slate-100">The Burning Splinter Confirmation:</strong> Once a column of gas collects, the tube is lifted with a thumb over its mouth. A glowing (smoldering) wooden splinter inserted into the gas column <strong class="text-amber-400">bursts vigorously into a bright flame</strong>.</p>
        </div>
    </div>
    <div class="p-3 rounded-lg bg-emerald-950/40 border border-emerald-500/30 text-xs text-slate-300">
        <strong class="text-emerald-300">Scientific Law:</strong> Oxygen is a strong supporter of combustion. The rekindling of a smoldering ember is the gold-standard chemical test for oxygen gas.
    </div>
</div>
""",
        "takeaways": [
            "Aquatic plants like Hydrilla make oxygen release visible through continuous rising bubbles under sunlight.",
            "Downward displacement of water in an inverted test tube safely captures the liberated gas.",
            "A smoldering wooden splinter bursts into flame when inserted into oxygen gas, confirming its identity."
        ],
        "checkpoints": [
            {
                "id": "cp7_1",
                "question": "What happens to a glowing wooden splinter when it is thrust into the gas collected from sunlit Hydrilla sprigs?",
                "options": [
                    "It is instantly extinguished with a loud pop sound",
                    "It bursts into a bright flame because oxygen supports combustion",
                    "It turns into green liquid paint",
                    "It turns completely into pure white snow"
                ],
                "correct": 1,
                "explanation": "Oxygen vigorously supports combustion. Thrusting a glowing (smoldering) ember into collected oxygen gas rekindles it into an active flame."
            },
            {
                "id": "cp7_2",
                "question": "Why does the stream of gas bubbles from Hydrilla stop completely when the beaker is moved into a pitch-black room?",
                "options": [
                    "The water freezes into solid rock in the dark",
                    "Photosynthesis requires light photons to split water and release oxygen",
                    "Hydrilla plants die within 2 seconds of being in the dark",
                    "The glass funnel absorbs all the water in the dark"
                ],
                "correct": 1,
                "explanation": "Photosynthesis is strictly light-dependent. In the absence of light, photolysis of water halts and no oxygen gas bubbles can be formed."
            }
        ]
    },

    # Slide 8
    {
        "id": 8,
        "slide_num": 8,
        "title": "10.2.4 Stomatal Portals: Microscopic Gas Exchange",
        "subtitle": "Guard Cell Turgor Mechanics & Diffusion Through Leaf Pores",
        "badge": "Cellular Dynamics",
        "summary": "Leaves breathe through thousands of microscopic epidermal valves called stomata. Each stoma is flanked by a pair of kidney-shaped guard cells whose osmotic swelling and shrinking dynamically open and close the central pore to regulate CO₂ intake and water vapor loss.",
        "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        If leaves are sealed with a protective waxy cuticle, how do atmospheric carbon dioxide and oxygen pass in and out? The epidermis of a leaf is perforated by millions of microscopic apertures termed <strong class="text-emerald-400">stomata</strong> (singular: <em>stoma</em>, meaning mouth).
    </p>
    <div class="p-4 rounded-xl bg-slate-900/60 border border-slate-700/60">
        <h4 class="font-bold text-cyan-300 text-sm mb-2">Anatomy & Turgor Biomechanics of Guard Cells</h4>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs text-slate-300">
            <div class="p-2.5 rounded bg-emerald-950/40 border border-emerald-500/30">
                <strong class="text-emerald-400 block mb-1">Open Stoma (Turgid Guard Cells)</strong>
                During daylight, guard cells actively accumulate potassium ions (K⁺), drawing water in by osmosis. Guard cells swell with turgor. Because their inner cellulose wall bordering the pore is thick and rigid while the outer wall is thin and elastic, the cells bow outwards like crescent bananas, pulling the central pore wide open (CO₂ diffuses in).
            </div>
            <div class="p-2.5 rounded bg-amber-950/40 border border-amber-500/30">
                <strong class="text-amber-400 block mb-1">Closed Stoma (Flaccid Guard Cells)</strong>
                In darkness or during water stress, guard cells lose potassium ions and water exits back into neighboring epidermal cells. The guard cells lose turgidity, becoming limp (flaccid). The elastic inner walls spring back together, tightly sealing the central pore to prevent water loss.
            </div>
        </div>
    </div>
    <div class="p-3 rounded-lg bg-slate-900/60 border border-slate-700/60 text-xs text-slate-300">
        <strong class="text-amber-300">Stomatal Distribution:</strong> In most terrestrial broadleaf dicot plants, stomata are substantially more numerous on the cooler, shaded <strong class="text-slate-100">lower epidermis</strong> than on the sun-exposed upper surface, minimizing unnecessary evaporative water loss.
    </div>
</div>
""",
        "takeaways": [
            "Stomata are microscopic pores located primarily on the lower epidermis of leaves for gas exchange.",
            "Each stoma is bordered by two specialized, chloroplast-containing kidney-shaped guard cells.",
            "When guard cells absorb water and swell (turgid), the pore opens; when they lose water (flaccid), the pore closes."
        ],
        "checkpoints": [
            {
                "id": "cp8_1",
                "question": "What happens to stomatal guard cells when they absorb water and become turgid during daylight?",
                "options": [
                    "They shrink and seal the pore completely shut",
                    "They swell and bow outward, opening the central stomatal pore",
                    "They detach from the leaf and fall into the soil",
                    "They dissolve into liquid carbon dioxide"
                ],
                "correct": 1,
                "explanation": "When water enters guard cells, their differential wall thickness causes them to curve outward, opening the central aperture for gas diffusion."
            },
            {
                "id": "cp8_2",
                "question": "Why are stomata generally more abundant on the lower epidermis of leaves than on the upper epidermis?",
                "options": [
                    "To collect muddy water from splashing puddles",
                    "To prevent raindrops from blocking sunlight",
                    "To minimize excessive water loss from direct sunlight and wind heating",
                    "To help the plant hear underground vibrations"
                ],
                "correct": 2,
                "explanation": "Placing stomata on the cooler, shaded lower leaf surface reduces the rate of excessive water vapor loss (transpiration) caused by direct solar radiation."
            }
        ]
    },

    # Slide 9
    {
        "id": 9,
        "slide_num": 9,
        "title": "10.3 Transport Architecture: Dual Vascular Highways",
        "subtitle": "Xylem vs Phloem: Structural Specialization & Transport Rules",
        "badge": "Vascular Anatomy",
        "summary": "Complex vascular plants have evolved two distinct circulatory pipelines: xylem and phloem. Xylem transports water and dissolved soil minerals upward in a unidirectional flow, whereas phloem distributes soluble organic food bidirectionally to all metabolic sinks.",
        "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        A towering banyan or eucalyptus tree can stand dozens of metres tall. How do water molecules absorbed by roots in deep subterranean soil reach leaves high in the canopy, and how do sugars made in the leaves travel back down to nourish non-green roots? The answer lies in <strong class="text-cyan-400">vascular bundles</strong>.
    </p>
    <div class="p-4 rounded-xl bg-slate-900/60 border border-slate-700/60">
        <h4 class="font-bold text-amber-300 text-sm mb-2">Comparative Matrix: The Two Conducting Tissues</h4>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
            <div class="p-3 rounded-lg bg-cyan-950/40 border border-cyan-500/30">
                <span class="font-bold text-cyan-300 text-sm block mb-1">Xylem (Water Highway)</span>
                <ul class="text-slate-300 space-y-1">
                    <li>• <strong class="text-slate-100">Components:</strong> Tracheids, vessels, xylem parenchyma, xylem fibres.</li>
                    <li>• <strong class="text-slate-100">Cell Nature:</strong> Mature vessels are dead, hollow, non-living pipes reinforced with tough, impermeable <strong class="text-cyan-200">lignin</strong>.</li>
                    <li>• <strong class="text-slate-100">Cargo:</strong> Water and dissolved inorganic mineral salts (nitrates, phosphates, potassium).</li>
                    <li>• <strong class="text-slate-100">Direction:</strong> <strong class="text-emerald-400">Strictly unidirectional (upwards only)</strong> from roots → stem → leaves.</li>
                </ul>
            </div>
            <div class="p-3 rounded-lg bg-emerald-950/40 border border-emerald-500/30">
                <span class="font-bold text-emerald-300 text-sm block mb-1">Phloem (Food Highway)</span>
                <ul class="text-slate-300 space-y-1">
                    <li>• <strong class="text-slate-100">Components:</strong> Sieve tube elements, companion cells, phloem parenchyma, phloem fibres.</li>
                    <li>• <strong class="text-slate-100">Cell Nature:</strong> Sieve tubes are <strong class="text-emerald-200">living cells</strong> with perforated end-plates (sieve plates), connected to companion cells.</li>
                    <li>• <strong class="text-slate-100">Cargo:</strong> Dissolved organic nutrients (sucrose, amino acids, plant hormones).</li>
                    <li>• <strong class="text-slate-100">Direction:</strong> <strong class="text-amber-400">Multidirectional / Bidirectional</strong> from sources (leaves) to any active sink (roots, flowers, seeds).</li>
                </ul>
            </div>
        </div>
    </div>
    <p class="text-xs text-slate-300">
        In stems, xylem and phloem run side-by-side within continuous strands termed <strong class="text-slate-100">vascular bundles</strong>, extending seamlessly from the finest root tip through the trunk into every leaf vein.
    </p>
</div>
""",
        "takeaways": [
            "Xylem vessels are dead, lignified hollow tubes that conduct water and minerals strictly upward (unidirectional).",
            "Phloem comprises living sieve tubes and companion cells that translocate sugars bidirectionally to growing organs and roots.",
            "Vascular bundles create an interconnected plumbing network throughout root, stem, leaf, and flower tissues."
        ],
        "checkpoints": [
            {
                "id": "cp9_1",
                "question": "Which plant vascular tissue is composed of dead, lignified hollow vessels that conduct water strictly upwards?",
                "options": [
                    "Phloem sieve tubes",
                    "Xylem vessels",
                    "Epidermal cuticle",
                    "Palisade mesophyll"
                ],
                "correct": 1,
                "explanation": "Xylem vessels lose their protoplasts at maturity, forming hollow, lignified microscopic pipelines dedicated to the upward transport of water and dissolved minerals."
            },
            {
                "id": "cp9_2",
                "question": "Why is transport through phloem described as bidirectional, unlike transport through xylem?",
                "options": [
                    "Water can only evaporate into outer space",
                    "Synthesized sugars move from source leaves to both upward shoot buds and downward root storage organs",
                    "Phloem tubes spin in complete 360 degree circles every hour",
                    "Roots synthesize all the food during cold winter months"
                ],
                "correct": 1,
                "explanation": "Phloem carries sucrose from photosynthetic leaves (sources) upward to developing flowers, fruits, and apical buds, as well as downward to roots and storage tubers (sinks)."
            }
        ]
    },

    # Slide 10
    {
        "id": 10,
        "slide_num": 10,
        "title": "10.3.1 Water Uptake: Root Hairs & Soil Solution",
        "subtitle": "Microscopic Surface Area Expansion & Osmotic Entry",
        "badge": "Root Dynamics",
        "summary": "Root hairs are delicate tubular outgrowths of root epidermal cells that dramatically increase the surface area in contact with soil capillary water. Water enters root hairs by osmosis down a water potential gradient and travels through cortex cells to enter the central xylem cylinder.",
        "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        The hidden root system of a plant is a vast underground foraging apparatus. To satisfy the enormous daily water demands of aerial leaves, roots produce millions of microscopic, thread-like extensions termed <strong class="text-emerald-400">root hairs</strong>.
    </p>
    <div class="p-4 rounded-xl bg-slate-900/60 border border-slate-700/60">
        <h4 class="font-bold text-cyan-300 text-sm mb-2">The Osmotic Absorption Cascade</h4>
        <div class="space-y-2 text-xs text-slate-300">
            <p>1. <strong class="text-slate-100">Surface Area Multiplication:</strong> Root hairs increase the root absorptive contact area by several hundred-fold, squeezing between micro-pores between soil mineral particles to contact capillary film water.</p>
            <p>2. <strong class="text-slate-100">Osmosis Across Cell Membrane:</strong> The root hair cell sap inside the central vacuole contains concentrated dissolved sugars and mineral ions, creating a higher solute concentration (lower water potential) than the surrounding dilute soil water. Water molecules naturally diffuse across the semi-permeable cell membrane by <strong class="text-cyan-300">osmosis</strong>.</p>
            <p>3. <strong class="text-slate-100">Radial Cortex Transit:</strong> From the root hair epidermis, water travels cell-to-cell through the root cortex and endodermis until it discharges into the non-living lumen of root <strong class="text-cyan-400">xylem vessels</strong>.</p>
            <p>4. <strong class="text-slate-100">Root Pressure:</strong> Continuous osmotic water intake generates a modest positive hydrostatic push known as <strong class="text-amber-400">root pressure</strong>, which can push sap upward a few inches or cause guttation droplets on leaf margins.</p>
        </div>
    </div>
    <div class="p-3 rounded-lg bg-emerald-950/40 border border-emerald-500/30 text-xs text-slate-300">
        <strong class="text-emerald-300">Mineral Transport:</strong> Plants cannot absorb rock minerals as solid granules. They absorb essential minerals (nitrogen, phosphorus, potassium, magnesium) as dissolved ionic solutes (NO₃⁻, H₂PO₄⁻, K⁺, Mg²⁺) dissolved inside the water stream.
    </div>
</div>
""",
        "takeaways": [
            "Root hairs are thin, unicellular tubular extensions that maximize absorptive surface area with soil water.",
            "Water enters root hair vacuoles by osmosis because cell sap has a higher solute concentration than soil moisture.",
            "Water crosses cortical cells to enter the central vascular cylinder, creating root pressure."
        ],
        "checkpoints": [
            {
                "id": "cp10_1",
                "question": "By what primary physical process do water molecules enter root hair cells from the surrounding soil moisture?",
                "options": [
                    "Active mechanical pumping by root muscles",
                    "Osmosis down a water potential concentration gradient",
                    "Direct boiling into hot steam",
                    "Magnetic attraction by iron in the leaves"
                ],
                "correct": 1,
                "explanation": "Osmosis is the net movement of water molecules from a region of higher water concentration (dilute soil solution) to lower water concentration (concentrated root cell sap) across a semi-permeable membrane."
            },
            {
                "id": "cp10_2",
                "question": "What is the primary structural benefit of millions of microscopic root hairs covering a plant's root tips?",
                "options": [
                    "To anchor heavy rocks above ground",
                    "To vastly increase the surface area available for absorbing water and dissolved minerals",
                    "To reflect sunlight underground",
                    "To scare away burrowing earthworms"
                ],
                "correct": 1,
                "explanation": "Root hairs dramatically expand the total surface area of root epidermis in contact with soil moisture, maximizing water and nutrient absorption rates."
            }
        ]
    },

    # Slide 11
    {
        "id": 11,
        "slide_num": 11,
        "title": "10.3.1 Ascent of Sap: Transpiration Pull & Capillary Action",
        "subtitle": "The Balsam Plant Eosin Demonstration & Suction Forces",
        "badge": "Physical Forces",
        "summary": "Root pressure alone cannot lift water to the tops of tall trees. The primary engine of the ascent of sap is transpiration pull—evaporation of water vapor through stomata creates a immense negative suction tension that pulls cohesive water columns up through xylem vessels.",
        "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        More than 95% of the water absorbed by plant roots is not retained inside cells—it evaporates into the atmosphere through open leaf stomata as invisible water vapor. This evaporative loss is called <strong class="text-emerald-400">transpiration</strong>. Far from being a wasteful leak, transpiration powers the entire vascular circulation of the plant!
    </p>
    <div class="p-4 rounded-xl bg-slate-900/60 border border-slate-700/60">
        <h4 class="font-bold text-cyan-300 text-sm mb-2">The Suction Straw Mechanism: Transpiration Pull</h4>
        <div class="space-y-2 text-xs text-slate-300">
            <p>1. <strong class="text-slate-100">Evaporation Creates Suction:</strong> When water evaporates from mesophyll cell walls into stomatal sub-chambers, a negative hydrostatic pressure (suction) develops, pulling water from adjacent xylem veins.</p>
            <p>2. <strong class="text-slate-100">Cohesion & Adhesion:</strong> Water molecules have strong polarity; they cling tenaciously to one another via hydrogen bonds (<strong class="text-cyan-300">cohesion</strong>) and adhere to the hydrophilic cellulose walls of xylem vessels (<strong class="text-cyan-300">adhesion</strong>). This maintains unbroken, continuous columns of water from root tip to topmost leaf.</p>
            <p>3. <strong class="text-slate-100">The Ascent of Sap:</strong> Transpiration pull acts like a giant biological drinking straw, hauling millions of litres of sap upwards against gravity without requiring any mechanical pump.</p>
        </div>
    </div>
    <div class="p-3 rounded-lg bg-emerald-950/40 border border-emerald-500/30 text-xs text-slate-300">
        <strong class="text-emerald-300">The Balsam Red Dye Experiment:</strong> Place a tender herbaceous balsam plant (with intact roots) in a beaker containing water stained with red eosin dye. Within a few hours, the red dye visibly climbs up the translucent stem, tracing fine red veins through the leaves and tinting white petals pink! Transverse cross-sections reveal that only the ring of <strong class="text-rose-400">xylem vessels</strong> is dyed red.
    </div>
</div>
""",
        "takeaways": [
            "Transpiration is the evaporative loss of water vapor from aerial plant surfaces, predominantly through stomata.",
            "Transpiration generates a powerful negative pressure (transpiration pull) that hoists unbroken water columns up xylem vessels.",
            "Water molecules stay connected due to strong intermolecular cohesion (H-bonding) and adhesion to xylem walls."
        ],
        "checkpoints": [
            {
                "id": "cp11_1",
                "question": "What primary physical force pulls water columns upwards to the tops of tall trees through xylem vessels?",
                "options": [
                    "Gravitational downward pull",
                    "Transpiration pull caused by evaporative suction at leaf stomata",
                    "Centrifugal rotation of the Earth",
                    "Magnetic attraction from clouds in the sky"
                ],
                "correct": 1,
                "explanation": "Transpiration pull creates a continuous negative suction pressure in the xylem vessels, drawing water up from the roots like drinking through a straw."
            },
            {
                "id": "cp11_2",
                "question": "In the classic balsam plant experiment with red eosin dye, which specific tissue stains red in the stem cross-section?",
                "options": [
                    "Outer waxy bark",
                    "Xylem vessels",
                    "Phloem sieve tubes only",
                    "Pith air bubbles"
                ],
                "correct": 1,
                "explanation": "Water and dissolved dyes travel exclusively through xylem vessels, so only the xylem pipes stain red when the stem is examined in cross-section."
            }
        ]
    },

    # Slide 12
    {
        "id": 12,
        "slide_num": 12,
        "title": "10.3.2 Food Translocation: The Living Phloem Network",
        "subtitle": "Source-to-Sink Transport & Girdling Experiment Proof",
        "badge": "Nutrient Allocation",
        "summary": "Sugars manufactured in photosynthetic leaves must be translocated to non-photosynthetic roots, storage tubers, and growing shoot buds. This process occurs through living phloem sieve tubes driven by hydrostatic pressure gradients from source to sink.",
        "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        The transportation of soluble organic food substances (mainly the non-reducing disaccharide <strong class="text-amber-400">sucrose</strong>) from green leaves to non-green tissues is termed <strong class="text-emerald-400">translocation</strong>.
    </p>
    <div class="p-4 rounded-xl bg-slate-900/60 border border-slate-700/60">
        <h4 class="font-bold text-cyan-300 text-sm mb-2">The Source-to-Sink Dynamic Framework</h4>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs text-slate-300">
            <div class="p-2.5 rounded bg-emerald-950/40 border border-emerald-500/30">
                <strong class="text-emerald-400 block mb-1">Sources (Producers / Exporters)</strong>
                Mature leaves photosynthesizing in bright daylight produce excess glucose, convert it to soluble sucrose, and actively load it into neighboring phloem sieve tubes using ATP energy.
            </div>
            <div class="p-2.5 rounded bg-cyan-950/40 border border-cyan-500/30">
                <strong class="text-cyan-400 block mb-1">Sinks (Consumers / Importers)</strong>
                Developing shoot apical buds, unexpanded leaves, flower petals, developing seeds, fruits, and underground storage roots (potatoes, carrots) unload and consume or store the incoming sucrose.
            </div>
        </div>
    </div>
    <div class="p-3 rounded-lg bg-slate-900/60 border border-slate-700/60 text-xs text-slate-300">
        <strong class="text-amber-300">Malpighi's Classic Girdling (Ringing) Experiment:</strong> If a complete circular ring of outer bark—containing the phloem layer—is carefully carved away from a woody tree trunk while keeping the central xylem cylinder intact:
        <ul class="mt-1 space-y-1 list-disc list-inside">
            <li>Leaves above the ring remain crisp and green (xylem water flow continues uninterrupted).</li>
            <li>After a few weeks, the bark immediately <strong class="text-emerald-400">above the girdle swells dramatically</strong> due to accumulated downward-flowing sugars blocked at the cut.</li>
            <li>Eventually, the subterranean roots starve to death without food, causing the whole tree to perish. This definitively proves that phloem conducts downward food translocation.</li>
        </ul>
    </div>
</div>
""",
        "takeaways": [
            "Translocation is the movement of soluble organic nutrients (sucrose, amino acids) through living phloem tissue.",
            "Sugar travels from photosynthetic 'sources' (mature leaves) to metabolic 'sinks' (roots, fruits, growing tips).",
            "The girdling (ringing) experiment proves that phloem is located in the outer bark and transports food downward."
        ],
        "checkpoints": [
            {
                "id": "cp12_1",
                "question": "What is the primary form of carbohydrate sugar translocated through plant phloem sieve tubes?",
                "options": [
                    "Insoluble coarse starch granules",
                    "Soluble sucrose disaccharide",
                    "Solid cellulose wood fibres",
                    "Pure carbon dioxide gas"
                ],
                "correct": 1,
                "explanation": "Plants convert glucose into soluble, non-reducing sucrose for safe, efficient translocation through phloem sieve tubes."
            },
            {
                "id": "cp12_2",
                "question": "What happens when a ring of outer bark containing phloem is removed from a tree trunk (girdling experiment)?",
                "options": [
                    "Water immediately stops reaching the top leaves",
                    "Sugars accumulate above the girdle, forming a swollen bark ridge",
                    "Leaves immediately turn blue and begin shouting",
                    "The roots double in size overnight"
                ],
                "correct": 1,
                "explanation": "Because the downward food-transporting phloem path is severed while upward xylem water flow remains intact, sugars accumulate just above the ring, causing noticeable swelling."
            }
        ]
    },

    # Slide 13
    {
        "id": 13,
        "slide_num": 13,
        "title": "10.4 Plant Respiration: The Hidden Metabolic Flame",
        "subtitle": "24/7 Cellular Respiration vs Daylight Photosynthesis",
        "badge": "Metabolic Balance",
        "summary": "A common misconception is that plants only photosynthesize and do not respire. In truth, every living plant cell respires 24 hours a day, breaking down glucose with oxygen in mitochondria to release cellular ATP energy for maintenance, synthesis, and root nutrient uptake.",
        "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        Do plants breathe? Many students erroneously believe that plants 'inhale carbon dioxide and exhale oxygen' at all times. In reality, <strong class="text-amber-400">every living plant cell carries out cellular respiration 24 hours a day, day and night</strong>!
    </p>
    <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-700/60 text-center">
        <span class="text-xs uppercase tracking-wider text-rose-400 font-bold block mb-1">The Universal Respiration Equation (Identical to Animals!)</span>
        <div class="text-base sm:text-lg font-mono font-bold text-cyan-300 bg-slate-950/70 p-3 rounded-lg border border-slate-700">
            Glucose + Oxygen → Carbon Dioxide + Water + ATP Energy
            <br><span class="text-amber-300 text-sm">C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O + 38 ATP</span>
        </div>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs text-slate-300">
        <div class="p-3 rounded-lg bg-emerald-950/40 border border-emerald-500/30">
            <strong class="text-emerald-400 block mb-1">During Bright Daylight (Sunlight Present)</strong>
            The rate of photosynthesis is roughly 10 to 20 times faster than the rate of respiration. Photosynthesis consumes all internally generated respiratory CO₂ and takes in extra CO₂ from the air, releasing an abundant net surplus of oxygen (O₂).
        </div>
        <div class="p-3 rounded-lg bg-rose-950/40 border border-rose-500/30">
            <strong class="text-rose-400 block mb-1">During Dark Night (No Sunlight)</strong>
            Photosynthesis stops completely. However, cellular respiration continues unabated. The plant absorbs oxygen from the air and releases carbon dioxide. This is why people are traditionally advised not to sleep under dense trees at night.
        </div>
    </div>
    <div class="p-3 rounded-lg bg-slate-900/60 border border-slate-700/60 text-xs text-slate-300">
        <strong class="text-cyan-300">The Compensation Point:</strong> At dawn and dusk, when light intensity is dim, the rate of photosynthesis exactly equals the rate of respiration. At this precise light compensation point, there is <strong class="text-slate-100">zero net gaseous exchange</strong> between the plant and the surrounding air.
    </div>
</div>
""",
        "takeaways": [
            "All living plant cells carry out cellular respiration continuously (24 hours a day), breaking down glucose with oxygen.",
            "In bright daylight, photosynthesis vastly outpaces respiration, resulting in a net uptake of CO₂ and net release of O₂.",
            "In pitch darkness, photosynthesis ceases, so plants consume oxygen and release carbon dioxide like animals."
        ],
        "checkpoints": [
            {
                "id": "cp13_1",
                "question": "What is the net gaseous exchange of a green plant kept in total darkness during the night?",
                "options": [
                    "It consumes oxygen and releases carbon dioxide",
                    "It consumes carbon dioxide and releases oxygen",
                    "It releases nitrogen gas and absorbs chlorine",
                    "No gas exchange of any kind takes place"
                ],
                "correct": 0,
                "explanation": "In darkness, photosynthesis halts while respiration continues 24/7. Consequently, the plant takes in oxygen and releases carbon dioxide."
            },
            {
                "id": "cp13_2",
                "question": "What is meant by the 'compensation point' in plant physiology at dawn and dusk?",
                "options": [
                    "The time when leaves turn completely blue",
                    "The light intensity where the rate of photosynthesis exactly equals the rate of respiration",
                    "The moment when roots detach from the soil to sleep",
                    "The temperature where all plant enzymes permanently freeze"
                ],
                "correct": 1,
                "explanation": "At the compensation point, all carbon dioxide released by respiration is immediately consumed by photosynthesis, resulting in zero net gas exchange with the environment."
            }
        ]
    },

    # Slide 14
    {
        "id": 14,
        "slide_num": 14,
        "title": "10.4 Respiration in Action: The Germinating Seeds Experiment",
        "subtitle": "Lime Water Turbidity, Oxygen Uptake & Thermal Heat Release",
        "badge": "Laboratory Experiment",
        "summary": "Because germinating seeds lack chlorophyll and undergo rapid cellular division, they exhibit intense respiration rates without the interference of photosynthesis. In sealed conical flasks, germinating seeds consume oxygen, turn lime water milky with CO₂, and release detectable heat.",
        "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        Why are <strong class="text-amber-400">germinating gram or bean seeds</strong> the ideal botanical specimen to demonstrate respiration? Because germinating seeds are non-green—they possess no functional chlorophyll and perform zero photosynthesis. Their intense metabolic activity is pure cellular respiration!
    </p>
    <div class="p-4 rounded-xl bg-slate-900/60 border border-slate-700/60">
        <h4 class="font-bold text-cyan-300 text-sm mb-2">The Sealed Flask Respirometer Demonstration</h4>
        <div class="space-y-2 text-xs text-slate-300">
            <p>1. <strong class="text-slate-100">Setup:</strong> Moistened, actively germinating gram seeds are placed inside a conical flask sealed with an airtight rubber stopper. A small suspended test tube containing concentrated <strong class="text-rose-400">KOH solution</strong> is hung inside.</p>
            <p>2. <strong class="text-slate-100">U-Tube Manometer:</strong> A bent glass delivery tube dips into a beaker of colored water outside. As the seeds consume oxygen (O₂) and the emitted CO₂ is absorbed by the KOH, a partial vacuum forms inside the flask. The colored water level in the glass tube <strong class="text-cyan-300">rises noticeably</strong>, proving oxygen gas consumption.</p>
            <p>3. <strong class="text-slate-100">Lime Water Test:</strong> In an alternative setup without KOH, the gas from the germinating seeds is bubbled through clear <strong class="text-emerald-400">lime water (calcium hydroxide, Ca(OH)₂)</strong>. The lime water turns distinctly <strong class="text-slate-100 font-bold">milky white</strong> due to insoluble calcium carbonate precipitation (CaCO₃), confirming carbon dioxide emission.</p>
            <p>4. <strong class="text-slate-100">Thermodynamic Heat Release:</strong> In a thermos vacuum flask, germinating seeds show a measurable <strong class="text-amber-400">temperature rise of 2°C to 5°C</strong> on a sensitive thermometer, proving that respiration releases heat energy.</p>
        </div>
    </div>
    <div class="p-3 rounded-lg bg-emerald-950/40 border border-emerald-500/30 text-xs text-slate-300">
        <strong class="text-emerald-300">Control Experiment:</strong> Boiled (dead) seeds treated with antiseptic show zero water rise, zero lime water milkiness, and zero temperature increase, proving that the reactions are biological life processes of living tissue.
    </div>
</div>
""",
        "takeaways": [
            "Germinating seeds respire rapidly without photosynthesis interference because they lack active chlorophyll.",
            "Respiration consumes oxygen, creating a negative pressure that draws water up a connected manometer tube.",
            "Released carbon dioxide turns clear lime water milky, and exothermic cellular reactions produce detectable heat."
        ],
        "checkpoints": [
            {
                "id": "cp14_1",
                "question": "What happens when gas from a flask of germinating seeds is bubbled into clear lime water?",
                "options": [
                    "The lime water turns distinctly milky white due to carbon dioxide (CO₂)",
                    "The lime water turns bright purple and freezes into ice",
                    "The lime water turns into thick petrol",
                    "The lime water remains 100% clear with zero change"
                ],
                "correct": 0,
                "explanation": "Germinating seeds release carbon dioxide as a respiratory byproduct, which reacts with calcium hydroxide (lime water) to form insoluble white calcium carbonate precipitate."
            },
            {
                "id": "cp14_2",
                "question": "Why is a vacuum flask of boiled (dead) seeds included alongside the germinating seeds in the temperature experiment?",
                "options": [
                    "To cook dinner for the laboratory technicians",
                    "To serve as a negative control proving heat release is caused by living seed respiration",
                    "To speed up the growth of the live seeds",
                    "To generate extra oxygen gas for the room"
                ],
                "correct": 1,
                "explanation": "A control experiment with boiled (dead) seeds proves that temperature rise is caused strictly by the metabolic respiration of living cells and not by simple physical warming."
            }
        ]
    },

    # Slide 15
    {
        "id": 15,
        "slide_num": 15,
        "title": "10.4 Root & Bark Respiration: Aerial Roots & Lenticels",
        "subtitle": "Soil Aeration, Waterlogged Asphyxiation & Mangrove Pneumatophores",
        "badge": "Ecological Adaptations",
        "summary": "Plant respiration is not confined to leaves; underground roots and woody stems must respire continuously. Roots breathe through microscopic soil air pockets, while woody tree trunks breathe through porous lenticels. In waterlogged swamps, mangroves produce specialized upward breathing roots.",
        "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        Every organ of a plant requires energy to survive. Underground roots, embedded in the dark soil, carry out intense aerobic respiration to power the active uptake of dissolved mineral ions against concentration gradients.
    </p>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs text-slate-300">
        <div class="p-3 rounded-lg bg-slate-900/60 border border-slate-700/60">
            <strong class="text-cyan-300 block mb-1">Root Respiration & Soil Porosity</strong>
            <p class="leading-relaxed">Root hair cells absorb dissolved oxygen gas from tiny <strong class="text-slate-100">air pockets trapped between soil particles</strong>. If a potted plant is chronically over-watered, water displaces all interstitial soil air. Deprived of oxygen, the roots undergo anaerobic asphyxiation, accumulate toxic ethanol, and succumb to <strong class="text-rose-400">root rot</strong>.</p>
        </div>
        <div class="p-3 rounded-lg bg-slate-900/60 border border-slate-700/60">
            <strong class="text-amber-300 block mb-1">Woody Stems & Lenticels</strong>
            <p class="leading-relaxed">As herbaceous stems grow into mature woody trunks, the green epidermis is replaced by thick, impermeable cork bark. To allow gas exchange to living underlying cortex and phloem cells, bark is perforated by loosely packed, spongy aerating pores called <strong class="text-slate-100">lenticels</strong>.</p>
        </div>
    </div>
    <div class="p-4 rounded-xl bg-emerald-950/40 border border-emerald-500/30 text-xs text-slate-300">
        <h5 class="font-bold text-emerald-300 text-sm mb-1">Mangrove Adaptation: Pneumatophores (Breathing Roots)</h5>
        <p class="leading-relaxed">
            In saline coastal mudflats and mangrove estuaries (such as the Sundarbans), the waterlogged soil is completely anaerobic (oxygen-deficient) and saline. Mangrove trees (like <em>Rhizophora</em> and <em>Avicennia</em>) evolve specialized <strong class="text-emerald-400">pneumatophores</strong>—slender, pencil-like roots that grow vertically upward against gravity (<strong class="text-cyan-300">negatively geotropic</strong>) out of the mud and water. Their tips are studded with prominent breathing pores (lenticels) that inhale oxygen directly from the air and channel it down to subterranean root systems.
        </p>
    </div>
</div>
""",
        "takeaways": [
            "Root hair cells absorb oxygen from air pockets between soil grains to power active mineral uptake.",
            "Waterlogged soil displaces air, suffocating roots and causing lethal root rot due to oxygen starvation.",
            "Lenticels on woody bark and mangrove pneumatophores (breathing roots) provide vital gas exchange in dense or muddy environments."
        ],
        "checkpoints": [
            {
                "id": "cp15_1",
                "question": "Why do the roots of a potted houseplant rot and die if the pot is continuously over-watered?",
                "options": [
                    "Water dissolves the plant stem into sugar",
                    "Excess water displaces soil air pockets, suffocating the roots through oxygen deprivation",
                    "The water turns into pure liquid helium",
                    "Roots cannot survive when touching clean water"
                ],
                "correct": 1,
                "explanation": "Over-watering floods the interstitial spaces between soil grains, driving out all air pockets. Root cells are starved of oxygen, cannot perform aerobic respiration, and rot."
            },
            {
                "id": "cp15_2",
                "question": "What is the biological function of pneumatophores found in coastal mangrove trees?",
                "options": [
                    "To capture swimming fish for digestion",
                    "To grow upward out of waterlogged anaerobic mud to breathe atmospheric oxygen",
                    "To absorb moonlight during the full moon",
                    "To anchor flying birds onto the leaves"
                ],
                "correct": 1,
                "explanation": "Pneumatophores are specialized negatively geotropic breathing roots that project out of oxygen-deficient swamp mud to intake atmospheric oxygen through lenticels."
            }
        ]
    },

    # Slide 16
    {
        "id": 16,
        "slide_num": 16,
        "title": "Ancient Indian Botanical Heritage: Parashara & J.C. Bose",
        "subtitle": "Maharishi Parashara's Vrikshayurveda & Acharya Bose's Crescograph",
        "badge": "Scientific Heritage",
        "summary": "Centuries before modern microscopy, ancient Indian natural philosophers recognized plant vitality and circulatory structures. Maharishi Parashara accurately described sap-conducting vessels, while modern pioneer Acharya J.C. Bose proved plant sensitivity and sap pulsation.",
        "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        India possesses a rich tradition of plant science and botanical medicine. In antiquity, the study of botanical life was codified under <strong class="text-amber-400">Vrikshayurveda</strong> (the science of plant life and arboriculture).
    </p>
    <div class="p-4 rounded-xl bg-slate-900/60 border border-slate-700/60">
        <h4 class="font-bold text-emerald-300 text-sm mb-2">1. Maharishi Parashara: Vrikshayurveda (Ancient Botanical Genius)</h4>
        <div class="space-y-1.5 text-xs text-slate-300">
            <p>• <strong class="text-slate-100">Internal Anatomy:</strong> Maharishi Parashara identified that plant stems contain specialized internal tissue layers called <em class="text-cyan-300">Kala</em> and conducting pipelines termed <strong class="text-emerald-400">Syandani</strong> (the ancient Sanskrit equivalent of xylem and phloem vascular vessels).</p>
            <p>• <strong class="text-slate-100">Sap Conduction (Syandana):</strong> He observed that roots absorb moisture and nourishment (<em class="text-slate-100">Ahara-rasa</em>) from the earth, and through the influence of terrestrial heat and solar light (<em class="text-slate-100">Tejas</em>), sap moves upward through <em class="text-cyan-300">Syandani</em> conduits to nourish leaves, fruits, and flowers.</p>
            <p>• <strong class="text-slate-100">Leaf Classification:</strong> Parashara cataloged leaf arrangements and venation patterns (parallel vs reticulate venation) thousands of years before European botanical taxonomy.</p>
        </div>
    </div>
    <div class="p-4 rounded-xl bg-slate-900/60 border border-slate-700/60">
        <h4 class="font-bold text-cyan-300 text-sm mb-2">2. Acharya Jagadish Chandra Bose: The Crescograph & Plant Sensitivity</h4>
        <div class="space-y-1.5 text-xs text-slate-300">
            <p>• <strong class="text-slate-100">The Crescograph (1910s):</strong> Acharya J.C. Bose invented the <strong class="text-amber-400">Crescograph</strong>, an extraordinary precision instrument capable of magnifying infinitesimal plant growth and cellular movements by up to <strong class="text-cyan-300">10,000 to 100,000 times</strong>.</p>
            <p>• <strong class="text-slate-100">Plants Feel & React:</strong> Bose demonstrated that plants are not inert mechanisms—they generate electrical action potentials, respond to touch, temperature shifts, electrical stimuli, anesthetics, and chemical poisons just like animal nervous systems.</p>
            <p>• <strong class="text-slate-100">Pulsatile Sap Ascent Theory:</strong> Bose proved that the ascent of sap involves living cellular rhythmic pulsations in the inner cortex, pioneering modern plant electrophysiology.</p>
        </div>
    </div>
</div>
""",
        "takeaways": [
            "Maharishi Parashara's Vrikshayurveda systematically classified plant anatomy, venation, and Syandani conducting vessels.",
            "Ancient Indian treatises recognized that soil moisture and solar energy (Tejas) interact to produce plant sap.",
            "Acharya Jagadish Chandra Bose invented the Crescograph, demonstrating plant growth magnification and electrical sensitivity."
        ],
        "checkpoints": [
            {
                "id": "cp16_1",
                "question": "What groundbreaking scientific instrument did Acharya Jagadish Chandra Bose invent to measure microscopic plant growth?",
                "options": [
                    "The Galvanized Barometer",
                    "The Crescograph",
                    "The Seismograph",
                    "The Astronomical Sextant"
                ],
                "correct": 1,
                "explanation": "Acharya J.C. Bose invented the Crescograph, which used compound optical levers and gear trains to magnify and record microscopic plant growth by up to 100,000 times."
            },
            {
                "id": "cp16_2",
                "question": "In ancient Indian Vrikshayurveda, what term did Maharishi Parashara use to describe the internal sap-conducting vessels of plants?",
                "options": [
                    "Syandani",
                    "Vayu Chakra",
                    "Agni Kund",
                    "Surya Netra"
                ],
                "correct": 0,
                "explanation": "Maharishi Parashara described the internal sap-carrying channels of plants as 'Syandani', which correspond remarkably to modern xylem and phloem vascular tissues."
            }
        ]
    },

    # Slide 17: Mastery Quiz 1
    {
        "id": 17,
        "slide_num": 17,
        "title": "Mastery Challenge 1: Growth Factors, Leaf Anatomy & The Starch Test",
        "subtitle": "10 Conceptual & Experimental Questions with Step-by-Step Pop-up Solutions",
        "badge": "Quiz Challenge 1",
        "summary": "Put your understanding of seedling growth requirements, leaf internal micro-architecture, chlorophyll absorption, and the multi-step starch decolourisation test to the test.",
        "theory": "<div class='text-slate-300 text-sm'>Test your grasp of plant growth experiments, leaf anatomy, and the iodine starch test. Complete all 10 questions to achieve mastery!</div>",
        "takeaways": [],
        "checkpoints": [],
        "quiz_questions": [
            {
                "id": "q17_1",
                "question": "Which of the following environmental combinations is absolutely essential for a germinated seedling to thrive and maintain normal green leaves?",
                "options": [
                    "Complete darkness and dry sand",
                    "Both sunlight and soil water",
                    "Pure nitrogen gas and zero moisture",
                    "Continuous refrigeration at -10°C"
                ],
                "correct": 1,
                "solution": "Seedlings require water for cell turgor and mineral transport, and sunlight to synthesize chlorophyll and power photosynthesis. Lacking either causes wilting or etiolation."
            },
            {
                "id": "q17_2",
                "question": "What is the phenomenon called when a seedling grown in complete darkness develops an abnormally tall, spindly, pale-yellow stem?",
                "options": [
                    "Etiolation",
                    "Photosynthesis",
                    "Guttation",
                    "Transpiration"
                ],
                "correct": 0,
                "solution": "Etiolation is the physiological response of angiosperms grown in prolonged darkness, characterized by rapid stem elongation, small unexpanded leaves, and lack of green chlorophyll."
            },
            {
                "id": "q17_3",
                "question": "Which leaf tissue layer contains the highest density of chloroplasts and performs the vast majority of photosynthesis?",
                "options": [
                    "Upper waxy cuticle",
                    "Palisade mesophyll layer",
                    "Dead wood xylem vessels",
                    "Lower epidermal hair cells"
                ],
                "correct": 1,
                "solution": "The palisade mesophyll consists of vertically oriented, tightly packed columnar cells located just below the upper epidermis, maximally packed with light-absorbing chloroplasts."
            },
            {
                "id": "q17_4",
                "question": "Why do healthy plant leaves appear green to human eyes?",
                "options": [
                    "Chlorophyll reflects green light wavelengths while absorbing blue and red photons",
                    "Chlorophyll absorbs exclusively green light photons",
                    "Green light is synthesized inside the leaf mitochondria",
                    "Leaves contain copper paint pigments"
                ],
                "correct": 0,
                "solution": "Chlorophyll pigments absorb light efficiently in the blue (~430 nm) and red (~660 nm) spectral bands, while green wavelengths (~500–550 nm) are reflected and transmitted to our eyes."
            },
            {
                "id": "q17_5",
                "question": "What is the primary biological reason for boiling a plucked leaf in plain water for 2–3 minutes before performing the starch test?",
                "options": [
                    "To turn the leaf completely into sugar crystals",
                    "To kill the protoplasm and rupture cellular membranes so chemicals can penetrate",
                    "To remove all carbon atoms from the cell walls",
                    "To freeze the leaf into glass"
                ],
                "correct": 1,
                "solution": "Boiling in water kills the living cell protoplasm, denatures enzymes, and softens the cellulose walls, allowing subsequent solvents (ethanol and iodine) to penetrate."
            },
            {
                "id": "q17_6",
                "question": "Why is ethanol placed in a water bath rather than heated directly on an open gas burner?",
                "options": [
                    "Ethanol only boils when mixed with river mud",
                    "Ethanol is highly inflammable and its volatile vapors can catch fire easily",
                    "Direct flames turn ethanol into solid wood",
                    "Ethanol destroys the glass beaker if heated directly"
                ],
                "correct": 1,
                "solution": "Ethanol is an inflammable organic solvent with a low flash point. Heating it indirectly in a water bath prevents flammable vapor from contacting naked flames."
            },
            {
                "id": "q17_7",
                "question": "What is the visual appearance of a green leaf after being thoroughly boiled in alcohol in a water bath?",
                "options": [
                    "Bright neon blue",
                    "Pale, creamy white or straw-colored as chlorophyll is dissolved away",
                    "Jet black like coal",
                    "Completely invisible"
                ],
                "correct": 1,
                "solution": "Alcohol extracts the green chlorophyll pigments into solution, leaving the bleached leaf pale creamy-white or light straw-colored."
            },
            {
                "id": "q17_8",
                "question": "What color indicates a positive reaction when dilute iodine solution is dropped onto a starch-containing leaf?",
                "options": [
                    "Bright yellow",
                    "Intense blue-black",
                    "Pale green",
                    "Translucent pink"
                ],
                "correct": 1,
                "solution": "Iodine reacts specifically with the helical amylose chains in starch to form a dark blue-black polyiodide complex."
            },
            {
                "id": "q17_9",
                "question": "In a variegated croton or Coleus leaf (having green and white patches), which regions test positive for starch with iodine?",
                "options": [
                    "Only the non-green white patches",
                    "Only the previously green chlorophyll-rich patches",
                    "None of the patches",
                    "The entire petiole stalk only"
                ],
                "correct": 1,
                "solution": "Only the green patches contain chlorophyll to perform photosynthesis and produce starch. The white patches lack chlorophyll, produce no starch, and stain brown with iodine."
            },
            {
                "id": "q17_10",
                "question": "What is the primary carbohydrate form in which green plants temporarily store excess photosynthetic energy in their leaves?",
                "options": [
                    "Insoluble starch",
                    "Gaseous methane",
                    "Liquid olive oil",
                    "Pure calcium metal"
                ],
                "correct": 0,
                "solution": "Plants convert excess soluble glucose into insoluble, osmotic-neutral starch granules, preventing cellular water imbalance during daylight storage."
            }
        ]
    },

    # Slide 18: Mastery Quiz 2
    {
        "id": 18,
        "slide_num": 18,
        "title": "Mastery Challenge 2: Carbon Dioxide, Chemical Equations & Stomatal Mechanics",
        "subtitle": "10 Rigorous Inquiries on Photosynthesis Chemistry & Gas Exchange",
        "badge": "Quiz Challenge 2",
        "summary": "Evaluate your mastery of the balanced photosynthetic equation, Moll's half-leaf experiment with caustic soda, the Ingenhousz oxygen test, and the guard cell turgor mechanism.",
        "theory": "<div class='text-slate-300 text-sm'>Test your understanding of the chemical inputs and outputs of photosynthesis, gas exchange, and stomatal opening. Solve all 10 questions to proceed!</div>",
        "takeaways": [],
        "checkpoints": [],
        "quiz_questions": [
            {
                "id": "q18_1",
                "question": "What is the exact balanced chemical equation representing green plant photosynthesis?",
                "options": [
                    "6 CO₂ + 6 H₂O + Light Energy → C₆H₁₂O₆ + 6 O₂",
                    "C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O + Heat",
                    "CO₂ + H₂O → C + H + O",
                    "2 H₂ + O₂ → 2 H₂O"
                ],
                "correct": 0,
                "solution": "Photosynthesis uses 6 molecules of carbon dioxide and 6 molecules of water, powered by sunlight captured by chlorophyll, to yield 1 molecule of glucose (C₆H₁₂O₆) and 6 molecules of oxygen (O₂)."
            },
            {
                "id": "q18_2",
                "question": "In Moll's half-leaf experiment, what happens to the half of the leaf sealed inside the bottle containing KOH?",
                "options": [
                    "It turns dark blue-black with iodine because it made extra starch",
                    "It remains yellowish-brown with iodine because no starch formed without CO₂",
                    "It dissolves completely into green smoke",
                    "It produces giant strawberries inside the flask"
                ],
                "correct": 1,
                "solution": "KOH absorbs all carbon dioxide in the bottle. Without CO₂, the inner half cannot synthesize glucose or starch, and thus gives a negative (brown) iodine test."
            },
            {
                "id": "q18_3",
                "question": "What gas is confirmed when bubbles collected from sunlit Hydrilla rekindle a glowing wooden splinter into an open flame?",
                "options": [
                    "Carbon dioxide (CO₂)",
                    "Pure oxygen gas (O₂)",
                    "Hydrogen gas (H₂)",
                    "Methane gas (CH₄)"
                ],
                "correct": 1,
                "solution": "Oxygen is a vigorous supporter of combustion. Rekindling a glowing ember into an active flame is the diagnostic chemical test for pure oxygen gas."
            },
            {
                "id": "q18_4",
                "question": "What cellular shape do typical stomatal guard cells exhibit in the leaves of dicotyledonous plants?",
                "options": [
                    "Perfect square cubes",
                    "Kidney or bean-shaped paired cells",
                    "Elongated needle fibres",
                    "Hollow triangular pyramids"
                ],
                "correct": 1,
                "solution": "In dicots, each stomatal pore is bounded by a pair of kidney-shaped or bean-shaped guard cells that regulate pore aperture via turgor pressure."
            },
            {
                "id": "q18_5",
                "question": "Why do stomatal guard cells curve outwards and open the pore when they absorb water?",
                "options": [
                    "Their inner cellulose wall is thick and inelastic, while the outer wall is thin and flexible",
                    "Their inner wall dissolves completely in water",
                    "The guard cells have tiny motors pushing them apart",
                    "Water freezes inside the cells pushing them outward"
                ],
                "correct": 0,
                "solution": "Differential wall thickening—thick and rigid along the inner pore margin, thin and extensible on the outer flank—forces guard cells to bow outward when turgid."
            },
            {
                "id": "q18_6",
                "question": "What is the approximate volumetric concentration of carbon dioxide (CO₂) in Earth's ambient atmosphere?",
                "options": [
                    "Approximately 21%",
                    "Approximately 78%",
                    "Approximately 0.04%",
                    "Approximately 50%"
                ],
                "correct": 2,
                "solution": "Atmospheric air contains approximately 78% nitrogen, 21% oxygen, 0.9% argon, and roughly 0.04% (around 420 ppm) carbon dioxide."
            },
            {
                "id": "q18_7",
                "question": "Why must a plant be kept in complete darkness for 48 hours prior to beginning a photosynthesis experiment?",
                "options": [
                    "To kill all harmful insects on the leaves",
                    "To destarch the leaves so pre-existing starch is cleared out",
                    "To turn the roots into flower petals",
                    "To remove all water from the xylem vessels"
                ],
                "correct": 1,
                "solution": "Destarching ensures that any starch detected at the end of the experiment was synthesized strictly under the experimental conditions being tested."
            },
            {
                "id": "q18_8",
                "question": "Which of the following factors does NOT directly increase the rate of plant photosynthesis?",
                "options": [
                    "Higher light intensity (up to saturation point)",
                    "Optimal carbon dioxide concentration",
                    "Complete absence of water in the soil",
                    "Moderate warmth (25°C to 35°C)"
                ],
                "correct": 2,
                "solution": "Water is a mandatory reactant. Severe dehydration causes stomatal closure (preventing CO₂ uptake) and ceases photosynthesis."
            },
            {
                "id": "q18_9",
                "question": "What happens to the rate of oxygen bubble evolution from aquatic Hydrilla when a lamp is moved from 80 cm to 15 cm from the beaker?",
                "options": [
                    "Bubble evolution rate increases significantly due to higher light intensity",
                    "Bubble evolution halts completely",
                    "The plant starts releasing chlorine gas",
                    "The water turns instantly into ice"
                ],
                "correct": 0,
                "solution": "Moving the light source closer increases photon flux density, accelerating the light reactions and increasing the rate of oxygen bubble production."
            },
            {
                "id": "q18_10",
                "question": "What chemical is formed when gaseous carbon dioxide reacts with caustic soda (KOH) pellets inside Moll's experimental bottle?",
                "options": [
                    "Potassium carbonate (K₂CO₃) and water",
                    "Hydrochloric acid",
                    "Pure gold crystals",
                    "Gaseous chlorine"
                ],
                "correct": 0,
                "solution": "The reaction is: 2 KOH + CO₂ → K₂CO₃ + H₂O. Carbon dioxide is chemically trapped as solid potassium carbonate salt."
            }
        ]
    },

    # Slide 19: Mastery Quiz 3
    {
        "id": 19,
        "slide_num": 19,
        "title": "Mastery Challenge 3: Xylem, Transpiration Pull & Phloem Translocation",
        "subtitle": "10 Problem-Solving Questions on Vascular Transport & Osmosis",
        "badge": "Quiz Challenge 3",
        "summary": "Demonstrate your knowledge of root hair osmosis, xylem dead tracheary conduits, transpiration pull suction, cohesion-tension dynamics, and phloem source-to-sink translocation.",
        "theory": "<div class='text-slate-300 text-sm'>Test your grasp of plant vascular tissues, root absorption, transpiration pull, and phloem translocation. Complete all 10 questions to continue!</div>",
        "takeaways": [],
        "checkpoints": [],
        "quiz_questions": [
            {
                "id": "q19_1",
                "question": "Which tissue conducts water and dissolved soil minerals from the roots upwards through the stem to the leaves?",
                "options": [
                    "Phloem sieve tubes",
                    "Xylem vessels",
                    "Epidermal cuticle",
                    "Spongy parenchyma"
                ],
                "correct": 1,
                "solution": "Xylem vessels form an unbroken network of lignified hollow dead pipes that conduct water and inorganic minerals upwards from roots to aerial organs."
            },
            {
                "id": "q19_2",
                "question": "By what mechanism does soil water enter root hair cells across their semi-permeable cell membranes?",
                "options": [
                    "Osmosis from high water potential (soil) to lower water potential (cell sap)",
                    "Active mechanical pumping by root muscles",
                    "Thermal evaporation into steam",
                    "Gravity pulling water upwards"
                ],
                "correct": 0,
                "solution": "Because root cell sap has a higher concentration of dissolved solutes than the surrounding soil moisture, water enters spontaneously by osmosis."
            },
            {
                "id": "q19_3",
                "question": "What is the primary driving force for the ascent of sap against gravity in tall forest trees?",
                "options": [
                    "Transpiration pull generated by water evaporation from leaf stomata",
                    "Gravitational attraction of the Sun",
                    "Volcanic heat beneath the soil",
                    "Root hairs pushing with high-pressure air pumps"
                ],
                "correct": 0,
                "solution": "Transpiration pull generates immense negative suction tension in leaf xylem, pulling continuous water columns upwards through cohesive forces."
            },
            {
                "id": "q19_4",
                "question": "What property of water molecules prevents the thin water column in a tall xylem vessel from breaking under severe tension?",
                "options": [
                    "High intermolecular cohesion due to hydrogen bonds",
                    "Electrical repulsion between hydrogen atoms",
                    "High viscosity like motor oil",
                    "Zero density"
                ],
                "correct": 0,
                "solution": "Cohesion—the strong mutual attraction between polar water molecules via hydrogen bonding—gives water extraordinary tensile strength."
            },
            {
                "id": "q19_5",
                "question": "In what direction does organic food translocation occur through the living phloem sieve tubes?",
                "options": [
                    "Strictly downwards only",
                    "Strictly upwards only",
                    "Bidirectional / multidirectional from source leaves to various metabolic sinks",
                    "Food does not move through plants"
                ],
                "correct": 2,
                "solution": "Phloem translocation is bidirectional: it transports sucrose downward to root storage tissues and upward to developing flowers, fruits, and growing shoots."
            },
            {
                "id": "q19_6",
                "question": "Which living cellular components make up the functional conducting pipeline of angiosperm phloem tissue?",
                "options": [
                    "Dead hollow tracheids and wood fibres",
                    "Sieve tube elements connected to companion cells",
                    "Epidermal guard cells and hairs",
                    "Cork cells impregnated with suberin"
                ],
                "correct": 1,
                "solution": "Phloem conducting channels consist of living sieve tube elements with porous end-plates, metabolically supported by adjacent nucleated companion cells."
            },
            {
                "id": "q19_7",
                "question": "In the classic tree girdling (ringing) experiment, why does the bark immediately above the removed ring swell after several weeks?",
                "options": [
                    "Water accumulates because xylem was severed",
                    "Translocated organic food travelling downward through phloem is blocked at the cut",
                    "Air bubbles inflate the bark like a balloon",
                    "Insects build nests inside the dead wood"
                ],
                "correct": 1,
                "solution": "Removing the ring of bark severs the outer phloem tissue. Downward-moving sugars accumulate above the girdle, causing cellular hypertrophy and tissue swelling."
            },
            {
                "id": "q19_8",
                "question": "If a balsam plant is placed in water containing red ink, which part of the stem stains red when sliced in cross-section?",
                "options": [
                    "Only the central pith",
                    "The vascular xylem vessel rings",
                    "The outermost epidermal cuticle only",
                    "The phloem sieve tubes exclusively"
                ],
                "correct": 1,
                "solution": "Water-soluble red eosin dye travels exclusively in the water-conducting stream of xylem vessels, causing only xylem tissue to turn red."
            },
            {
                "id": "q19_9",
                "question": "Which of the following atmospheric conditions significantly increases the rate of plant transpiration?",
                "options": [
                    "High wind speed, warm temperature, and low humidity (dry air)",
                    "100% relative humidity on a rainy day",
                    "Pitch-black darkness with closed stomata",
                    "Freezing temperatures at 0°C"
                ],
                "correct": 0,
                "solution": "Warm temperatures, brisk wind, and low air humidity steepen the vapor pressure gradient between the leaf interior and the air, speeding up transpiration."
            },
            {
                "id": "q19_10",
                "question": "How do dissolved soil minerals such as nitrates and phosphates travel to the upper canopy leaves?",
                "options": [
                    "They fly through the air as dry dust",
                    "They are dissolved as ionic solutes in the ascending xylem water stream",
                    "They are pushed downward through the phloem",
                    "They travel only inside root hair vacuoles without leaving the soil"
                ],
                "correct": 1,
                "solution": "Minerals are absorbed from soil water as inorganic ions (NO₃⁻, H₂PO₄⁻, K⁺) and carried upward dissolved in the xylem transpiration stream."
            }
        ]
    },

    # Slide 20: Mastery Quiz 4
    {
        "id": 20,
        "slide_num": 20,
        "title": "Mastery Challenge 4: Plant Respiration, Diurnal Balance & Botanical Heritage",
        "subtitle": "10 Integrative Questions on Seed Respiration, Lenticels & Scientific History",
        "badge": "Final Mastery",
        "summary": "Master the final challenge covering germinating seed experiments, diurnal gas exchange balances, root aeration, mangrove pneumatophores, and ancient to modern Indian botanical heritage.",
        "theory": "<div class='text-slate-300 text-sm'>Demonstrate your final mastery across plant respiration, adaptations, and Indian botanical heritage. Answer all 10 questions to complete Chapter 10!</div>",
        "takeaways": [],
        "checkpoints": [],
        "quiz_questions": [
            {
                "id": "q20_1",
                "question": "Do green plants carry out cellular respiration during the daytime when bright sunlight is present?",
                "options": [
                    "No, plants only respire on cold winter nights",
                    "Yes, all living plant cells carry out cellular respiration 24 hours a day",
                    "No, respiration is an animal-only metabolic process",
                    "Yes, but only in their dead flower petals"
                ],
                "correct": 1,
                "solution": "Every living cell in a plant respires continuously (24 hours a day, day and night) to generate ATP energy required for cellular maintenance and synthesis."
            },
            {
                "id": "q20_2",
                "question": "Why is the net release of carbon dioxide from a plant leaf virtually undetectable during bright midday sunlight?",
                "options": [
                    "The plant stops respiring entirely during the day",
                    "Photosynthesis occurs much faster than respiration, consuming all released CO₂ internally",
                    "Carbon dioxide turns into solid iron in sunlight",
                    "Leaf cells destroy all mitochondria during daylight hours"
                ],
                "correct": 1,
                "solution": "In bright light, the rate of photosynthesis is 10 to 20 times faster than respiration. All CO₂ produced by mitochondria is instantly consumed by chloroplasts."
            },
            {
                "id": "q20_3",
                "question": "What is the biological significance of the 'light compensation point' occurring at dawn and dusk?",
                "options": [
                    "The rate of photosynthetic CO₂ uptake exactly equals the rate of respiratory CO₂ release",
                    "The leaves detach from the stem to rest",
                    "Photosynthesis operates at 1,000 times maximum capacity",
                    "The plant consumes 100% of the surrounding atmosphere"
                ],
                "correct": 0,
                "solution": "At the compensation point, photosynthesis and respiration balance each other perfectly, resulting in zero net intake or output of either CO₂ or O₂."
            },
            {
                "id": "q20_4",
                "question": "Why do actively germinating seeds release measurable thermal heat in a thermos vacuum flask experiment?",
                "options": [
                    "Cellular respiration is an exothermic biochemical reaction that releases energy, some of which dissipates as heat",
                    "Seeds absorb microwave radiation from the flask walls",
                    "Boiling water was poured over the live seeds",
                    "The thermometer generates electricity that warms the flask"
                ],
                "correct": 0,
                "solution": "Cellular respiration breaks down glucose bonds to form ATP, and thermodynamic inefficiency causes a portion of this chemical energy to be lost as sensible heat."
            },
            {
                "id": "q20_5",
                "question": "Through what specialized structural openings on the bark of woody tree trunks does gas exchange for respiration occur?",
                "options": [
                    "Stomata on leaves",
                    "Lenticels in the outer cork bark",
                    "Root hair tips",
                    "Pollen tubes"
                ],
                "correct": 1,
                "solution": "Lenticels are porous, loosely packed cork tissue regions in the bark of woody stems and roots that permit oxygen to diffuse to underlying living cells."
            },
            {
                "id": "q20_6",
                "question": "What happens to the roots of a plant growing in permanently waterlogged, un-aerated soil?",
                "options": [
                    "They double in length within 24 hours",
                    "They suffer anaerobic asphyxiation due to lack of oxygen and rot",
                    "They begin synthesizing starch from mud",
                    "They turn into thick steel cables"
                ],
                "correct": 1,
                "solution": "Waterlogged soil excludes air pockets. Deprived of oxygen, root cells cannot perform aerobic respiration, accumulate toxic fermentation byproducts, and rot."
            },
            {
                "id": "q20_7",
                "question": "What are pneumatophores, and in which ecological habitat are they commonly found?",
                "options": [
                    "Downward anchor roots found in dry desert sand dunes",
                    "Negatively geotropic breathing roots found in waterlogged mangrove swamps",
                    "Thorny leaves found on alpine cacti",
                    "Floating air bladders in freshwater ponds"
                ],
                "correct": 1,
                "solution": "Pneumatophores are specialized erect breathing roots that grow upward out of saline, oxygen-poor mangrove mud to absorb atmospheric oxygen through lenticels."
            },
            {
                "id": "q20_8",
                "question": "What ancient Indian treatise composed by Maharishi Parashara systematically documented plant anatomy, sap conduction, and taxonomy?",
                "options": [
                    "Vrikshayurveda",
                    "Surya Siddhanta",
                    "Arthashastra",
                    "Natya Shastra"
                ],
                "correct": 0,
                "solution": "Maharishi Parashara's Vrikshayurveda is an ancient Indian botanical classic that details plant internal anatomy, Syandani conducting vessels, and agricultural sciences."
            },
            {
                "id": "q20_9",
                "question": "What scientific instrument did Acharya Jagadish Chandra Bose invent to record microscopic plant growth and electrical responses?",
                "options": [
                    "The Crescograph",
                    "The Spectroheliograph",
                    "The Mechanical Barograph",
                    "The Acoustic Gramophone"
                ],
                "correct": 0,
                "solution": "Acharya J.C. Bose designed the Crescograph, using high-magnification optical levers to record plant growth rates and physiological responses to stimuli."
            },
            {
                "id": "q20_10",
                "question": "Why is it traditionally considered inadvisable to sleep beneath large leafy trees during pitch-black nighttime hours?",
                "options": [
                    "Trees release deadly poisonous neurotoxins in the dark",
                    "In the dark, photosynthesis halts while continuous plant respiration consumes oxygen and releases carbon dioxide",
                    "Trees absorb gravity, making people float into the sky",
                    "Tree leaves turn into solid stone at midnight"
                ],
                "correct": 1,
                "solution": "At night, photosynthesis is inactive, but millions of tree cells continue respiring, consuming ambient oxygen and releasing carbon dioxide around the canopy."
            }
        ]
    }
]

def main():
    print("Generating class7_science_plants_data.py...")
    # Verify no raw LaTeX commands exist in any slide text or questions
    latex_pattern = re.compile(r'\\[a-zA-Z]+')
    
    with open(".agents/class7_science_plants_data.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""Auto-generated data file for Class 7 Science Chapter 10: Life Processes in Plants."""\n\n')
        f.write("CHAPTER_META = {\n")
        f.write('    "title": "NCERT Class 7 Science • Chapter 10 • Life Processes in Plants Master Lab",\n')
        f.write('    "chapter_num": 10,\n')
        f.write('    "chapter_title": "Life Processes in Plants",\n')
        f.write('    "mentor": "Jan Ingenhousz & Acharya J.C. Bose",\n')
        f.write('    "mentor_desc": "Pioneers of Photosynthesis Discovery, Plant Electrophysiology & Sap Conduction",\n')
        f.write('    "total_slides": 20,\n')
        f.write('    "checkpoints_count": 32,\n')
        f.write('    "quiz_questions_count": 40,\n')
        f.write("}\n\n")
        f.write("SLIDES = " + repr(slides) + "\n")

    print(f"Successfully generated class7_science_plants_data.py with {len(slides)} slides.")
    
    # Validation check
    with open(".agents/class7_science_plants_data.py", "r", encoding="utf-8") as f:
        content = f.read()
    
    matches = latex_pattern.findall(content)
    # Ignore safe python escape sequences like \n, \t
    bad_latex = [m for m in matches if m not in ['\\n', '\\t', '\\r', '\\f', '\\b']]
    if bad_latex:
        print(f"WARNING: Found potential raw LaTeX commands: {bad_latex[:10]}")
    else:
        print("PASS: Zero raw LaTeX commands detected in data file!")

if __name__ == "__main__":
    main()

