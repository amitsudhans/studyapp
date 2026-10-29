# -*- coding: utf-8 -*-
"""
Generator script for Class 7 Science Chapter 2: Exploring Substances: Acidic, Basic, and Neutral
Data dictionary: 20 slides (16 theory + 4 quiz slides, 40 questions with complete step-by-step solutions)
Mentor: Acharya Prafulla Chandra Ray (Father of Indian Chemistry & Founder of Bengal Chemicals)
"""

import json

SLIDES_DATA = [
    # -------------------------------------------------------------
    # 1. Nature - Our Science Laboratory
    # -------------------------------------------------------------
    {
        "id": 1,
        "type": "concept_slide",
        "title": "Nature - Our Science Laboratory",
        "subtitle": "Classifying Everyday Substances: Acids, Bases, and Neutral Matter",
        "content": r"""
          <p>Look around your kitchen, garden, and medicine cabinet: nature has surrounded us with thousands of chemical compounds. In ancient times, people classified foods and materials by direct sensory experience—taste and touch.</p>
          <p class="mt-2">Through these observations, substances are classified into three major groups:</p>
          <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
            <li><strong>Acidic Substances (Acids):</strong> Taste characteristically <strong>sour</strong>. The word <em>acid</em> derives from the Latin <em>acere</em>, meaning sour. Examples: citric acid in lemons and oranges, acetic acid in vinegar, lactic acid in curd, and tartaric acid in tamarind.</li>
            <li><strong>Basic Substances (Bases):</strong> Taste characteristically <strong>bitter</strong> and feel <strong>slippery or soapy</strong> to the touch. Examples: sodium hydroxide in washing soaps, sodium hydrogen carbonate in baking soda, and calcium hydroxide in lime water.</li>
            <li><strong>Neutral Substances:</strong> Neither acidic nor basic. They do not taste sour or bitter, and do not alter indicator colors. Examples: pure distilled water, common salt ($\text{NaCl}$) solution, and cane sugar ($\text{C}_{12}\text{H}_{22}\text{O}_{11}$) solution.</li>
          </ul>
          <p class="mt-2 text-rose-300 font-semibold text-xs">⚠️ Cardinal Laboratory Safety Rule: NEVER taste or touch unknown chemical substances! Many strong acids (like concentrated sulfuric acid) and strong bases (like caustic soda) are intensely corrosive to human skin.</p>
        """,
        "formula": r"$$\text{Substance Spectrum}: \underbrace{\text{Acids (Sour, pH } < 7)}_{\text{Citric, Acetic, Lactic}} \quad \longleftrightarrow \quad \underbrace{\text{Neutral (pH } = 7)}_{\text{Pure } \text{H}_2\text{O}, \text{ NaCl}} \quad \longleftrightarrow \quad \underbrace{\text{Bases (Bitter, Soapy, pH } > 7)}_{\text{NaOH, } \text{NaHCO}_3, \text{ Ca(OH)}_2}$$",
        "key_takeaways": [
            "Acids taste sour and contain hydrogen ions; the word originates from Latin 'acere' (sour).",
            "Bases feel slippery/soapy, taste bitter, and neutralize acids.",
            "Neutral substances are neither acidic nor basic (e.g., pure water, table salt, sugar).",
            "Never taste laboratory chemicals to test acidity; use safe chemical indicators instead."
        ],
        "checkpoints": [
            {
                "question": "Which of the following common household substances is naturally acidic?",
                "options": [
                    "Baking soda solution",
                    "Lemon juice (citric acid)",
                    "Washing soap lather",
                    "Lime water (calcium hydroxide)"
                ],
                "correct": 1,
                "explanation": "Lemon juice contains citric acid and ascorbic acid, giving it a characteristic sour taste and acidic chemical behavior."
            },
            {
                "question": "Why is it strictly forbidden to determine whether a laboratory chemical is an acid or base by tasting it?",
                "options": [
                    "Because all chemicals taste identical to sugar",
                    "Because laboratory acids and bases can be highly toxic, poisonous, and corrosive to tissues",
                    "Because tasting chemicals ruins the glass beaker",
                    "Because tasting changes an acid into a base immediately"
                ],
                "correct": 1,
                "explanation": "Many laboratory chemicals (such as hydrochloric acid or sodium hydroxide) are intensely corrosive and can cause severe chemical burns or fatal poisoning upon ingestion."
            }
        ],
        "simulator_type": "household_substance_matrix"
    },

    # -------------------------------------------------------------
    # 2. Litmus - The Lichen's Colorful Gift
    # -------------------------------------------------------------
    {
        "id": 2,
        "type": "concept_slide",
        "title": "Litmus — The Lichen's Natural Indicator",
        "subtitle": "Discovering Acid-Base Color Shifts with Red and Blue Litmus Papers",
        "content": r"""
          <p>How can we safely test whether a solution is acidic or basic without tasting it? We use special substances called <strong>indicators</strong>—compounds that display distinctly different colors in acidic and basic environments.</p>
          <p class="mt-2">The most widely used natural indicator is <strong>Litmus</strong>, a natural water-soluble dye extracted from <strong>lichens</strong> (a symbiotic organism composed of an alga and a fungus living together):</p>
          <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
            <li><strong>Neutral Litmus Solution:</strong> Has a distinctive mauve (purple) color in pure distilled water.</li>
            <li><strong>Action in Acids:</strong> When added to an acidic solution, litmus turns <strong>red</strong>.</li>
            <li><strong>Action in Bases:</strong> When added to a basic solution, litmus turns <strong>blue</strong>.</li>
          </ul>
          <p class="mt-2">For convenience in laboratories, litmus dye is infused into absorbent paper strips, available as <strong>Red Litmus Paper</strong> and <strong>Blue Litmus Paper</strong>:</p>
          <div class="grid grid-cols-2 gap-2 my-2 text-xs font-mono">
            <div class="p-2.5 rounded-xl bg-slate-900 border border-rose-500/30 text-rose-300">
              <strong>Acid Test:</strong><br>Blue Litmus $\longrightarrow$ <strong>RED</strong><br>(Red litmus remains red)
            </div>
            <div class="p-2.5 rounded-xl bg-slate-900 border border-blue-500/30 text-blue-300">
              <strong>Base Test:</strong><br>Red Litmus $\longrightarrow$ <strong>BLUE</strong><br>(Blue litmus remains blue)
            </div>
          </div>
          <p>Neutral solutions (such as pure water or sugar syrup) do not change the color of either red or blue litmus paper.</p>
        """,
        "formula": r"$$\text{Litmus Rule}: \text{Acid turns Blue Litmus } \longrightarrow \mathbf{\text{RED}}, \quad \text{Base turns Red Litmus } \longrightarrow \mathbf{\text{BLUE}}$$ ",
        "key_takeaways": [
            "Litmus is a natural indicator dye extracted from lichens.",
            "Acids turn blue litmus paper red; bases turn red litmus paper blue.",
            "Neutral solutions produce no color change on either red or blue litmus paper.",
            "Memory Trick: 'B'ase turns litmus 'B'lue; 'A'cid turns litmus 'R'ed."
        ],
        "checkpoints": [
            {
                "question": "If a drop of soap solution is placed on dry red litmus paper, what color transformation occurs?",
                "options": [
                    "It turns bright blue",
                    "It turns bright yellow",
                    "It turns black",
                    "It remains unchanged because soap is completely neutral"
                ],
                "correct": 0,
                "explanation": "Soap is an alkaline (basic) substance. Bases turn red litmus paper blue."
            },
            {
                "question": "What happens when blue litmus paper is dipped into pure distilled water?",
                "options": [
                    "It turns red immediately",
                    "It turns green",
                    "It remains blue because pure water is neutral",
                    "It dissolves into thin air"
                ],
                "correct": 2,
                "explanation": "Distilled water is strictly neutral ($\text{pH} = 7$); it causes no color change on either red or blue litmus paper."
            }
        ],
        "simulator_type": "litmus_test_bench"
    },

    # -------------------------------------------------------------
    # 3. Red Rose Petal Extract as a Natural Indicator
    # -------------------------------------------------------------
    {
        "id": 3,
        "type": "concept_slide",
        "title": "Red Rose Petal Extract Indicator",
        "subtitle": "Harnessing Floral Anthocyanin Pigments for Chemical Detection",
        "content": r"""
          <p>Nature's flower petals are packed with water-soluble plant pigments known as <strong>anthocyanins</strong>. These organic pigments act as exquisite, natural acid-base indicators because their molecular structure alters when exposed to hydrogen ions ($\text{H}^+$) or hydroxide ions ($\text{OH}^-$).</p>
          <p class="mt-2"><strong>How to Prepare Red Rose Indicator:</strong></p>
          <ol class="list-decimal pl-5 mt-1 space-y-1 text-slate-300">
            <li>Collect fresh red rose petals and place them into a clean glass beaker.</li>
            <li>Add warm distilled water and allow the petals to steep for 15 to 20 minutes.</li>
            <li>Filter the liquid: you will obtain a pleasant light pink/red colored floral extract.</li>
          </ol>
          <p class="mt-2"><strong>Color Behavior in Different Mediums:</strong></p>
          <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
            <li><strong>In Acidic Solutions (e.g., lemon juice, dilute $\text{HCl}$):</strong> The extract turns a vibrant, deep <strong>red / dark pink</strong>.</li>
            <li><strong>In Basic Solutions (e.g., baking soda, washing soda, $\text{NaOH}$):</strong> The extract undergoes a dramatic transformation into <strong>green / yellowish-green</strong>.</li>
            <li><strong>In Neutral Solutions (e.g., pure water, salt solution):</strong> The extract retains its original light pink coloration without changing.</li>
          </ul>
        """,
        "formula": r"$$\text{Red Rose Indicator}: \text{Acidic Medium } \longrightarrow \mathbf{\text{Deep Red / Dark Pink}}, \quad \text{Basic Medium } \longrightarrow \mathbf{\text{Green}}$$ ",
        "key_takeaways": [
            "Flower petals contain anthocyanin pigments that change color across different pH levels.",
            "Red rose extract turns deep red/dark pink in acidic solutions.",
            "Red rose extract turns green or yellowish-green in basic (alkaline) solutions.",
            "Natural flower extracts provide an accessible, non-toxic way to explore chemistry at home."
        ],
        "checkpoints": [
            {
                "question": "When red rose extract is added to a test tube containing washing soda solution, what color does it turn?",
                "options": [
                    "Green",
                    "Deep red",
                    "Colorless",
                    "Bright purple"
                ],
                "correct": 0,
                "explanation": "Washing soda is basic (alkaline). Red rose extract turns green or yellowish-green when added to basic solutions."
            },
            {
                "question": "What happens when red rose extract is added to vinegar (acetic acid)?",
                "options": [
                    "It turns green",
                    "It turns dark red/pink",
                    "It turns deep blue",
                    "It produces a black precipitate"
                ],
                "correct": 1,
                "explanation": "Vinegar contains acetic acid; in acidic solutions, red rose extract turns an intensified dark red or magenta-pink."
            }
        ],
        "simulator_type": "red_rose_indicator_lab"
    },

    # -------------------------------------------------------------
    # 4. Turmeric (Haldi) - The Kitchen Indicator
    # -------------------------------------------------------------
    {
        "id": 4,
        "type": "concept_slide",
        "title": "Turmeric (Haldi) — The Kitchen Indicator",
        "subtitle": "The Curious Case of the Red Curry Stain and Curcumin Chemistry",
        "content": r"""
          <p>Every Indian kitchen stores a powerful chemical indicator: common <strong>turmeric powder (haldi)</strong>. Turmeric contains a bright yellow polyphenolic pigment called <strong>curcumin</strong>.</p>
          <p class="mt-2"><strong>Making Turmeric Indicator Paper:</strong> Mix a teaspoon of turmeric powder with a little water or alcohol to make a paste. Spread it evenly onto blotting paper or filter paper, let it dry, and cut it into thin yellow strips.</p>
          <p class="mt-2"><strong>The Color Invariant of Turmeric:</strong></p>
          <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
            <li><strong>In Acidic Solutions:</strong> Turmeric remains bright <strong>yellow</strong> (no color change).</li>
            <li><strong>In Neutral Solutions:</strong> Turmeric remains bright <strong>yellow</strong> (no color change).</li>
            <li><strong>In Basic Solutions:</strong> Turmeric turns a dramatic, deep <strong>reddish-brown</strong>!</li>
          </ul>
          <p class="mt-2"><strong>The Mystery of the Curry Stain:</strong> Have you ever spilled vegetable curry onto a white cotton shirt? When you wash it with laundry soap, the yellow spot immediately turns <strong>red</strong>! Why? Laundry soap is alkaline (basic), which reacts with curcumin to produce a red complex. When you rinse the soap thoroughly with water and apply lemon juice (an acid), the spot turns yellow again!</p>
        """,
        "formula": r"$$\text{Curcumin Equilibrium}: \underbrace{\text{Curcumin (Yellow)}}_{\text{Acidic \& Neutral (pH } < 7.4\text{)}} \quad \xrightarrow{+\text{Base (OH}^-\text{)}} \quad \underbrace{\text{Dianion Complex (Reddish-Brown)}}_{\text{Basic Medium (pH } > 8.5\text{)}}$$ ",
        "key_takeaways": [
            "Turmeric indicator turns deep reddish-brown in basic solutions.",
            "Turmeric remains yellow in both acidic and neutral solutions (it does NOT turn red in acid!).",
            "Soap turns curry stains red because soap is basic; rinsing with mild acid restores the yellow color.",
            "Turmeric paper can be used to write greeting cards with soap solution as 'invisible' red ink."
        ],
        "checkpoints": [
            {
                "question": "A student dips yellow turmeric paper into lime juice (citric acid). What color change will be observed?",
                "options": [
                    "It turns bright blue",
                    "It turns deep red",
                    "It remains yellow (no color change)",
                    "It turns pitch black"
                ],
                "correct": 2,
                "explanation": "Turmeric is unaffected by acids; it remains yellow in both acidic and neutral solutions. It only turns reddish-brown in basic solutions."
            },
            {
                "question": "Why does a yellow curry stain on a white shirt turn reddish-brown when rubbed with bathing soap?",
                "options": [
                    "Soap contains red food coloring",
                    "Soap is basic in nature and reacts with curcumin in turmeric to turn it reddish-brown",
                    "The fabric permanently burns from friction",
                    "Water dissolves the yellow pigment completely"
                ],
                "correct": 1,
                "explanation": "Soap is alkaline (basic); basic substances react with curcumin in turmeric to produce a characteristic reddish-brown coloration."
            }
        ],
        "simulator_type": "turmeric_curry_lab"
    },

    # -------------------------------------------------------------
    # 5. China Rose (Hibiscus) & Floral Spectra
    # -------------------------------------------------------------
    {
        "id": 5,
        "type": "concept_slide",
        "title": "China Rose (Gudhal) & Floral Spectra",
        "subtitle": "Extracting Nature's Universal Palette from Hibiscus Flowers",
        "content": r"""
          <p>Another classic natural indicator is prepared from the petals of the <strong>China rose</strong> (<em>Hibiscus rosa-sinensis</em>, commonly known in Hindi as <em>Gudhal</em>).</p>
          <p class="mt-2"><strong>Preparation:</strong> Place warm water in a beaker with several China rose petals. After steeping, a light pink-colored solution forms. This filtered solution serves as a sensitive indicator:</p>
          <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
            <li><strong>In Acidic Solutions:</strong> China rose extract turns a bright, intense <strong>dark pink (magenta)</strong>.</li>
            <li><strong>In Basic Solutions:</strong> China rose extract turns an unmistakable, vibrant <strong>green</strong>.</li>
            <li><strong>In Neutral Solutions:</strong> The extract remains its original light pink shade without alteration.</li>
          </ul>
          <p class="mt-2"><strong>Red Cabbage Indicator:</strong> Similarly, purple-red cabbage leaves boiled in water yield a universal-type floral extract: it turns <strong>red</strong> in strong acid, <strong>purple</strong> at neutral, and <strong>green to yellow</strong> in strong alkalis!</p>
        """,
        "formula": r"$$\text{China Rose Indicator}: \text{Acid } \longrightarrow \mathbf{\text{Dark Pink (Magenta)}}, \quad \text{Neutral } \longrightarrow \mathbf{\text{Light Pink}}, \quad \text{Base } \longrightarrow \mathbf{\text{Green}}$$ ",
        "key_takeaways": [
            "China rose (Hibiscus) extract is light pink in neutral water.",
            "China rose extract turns dark pink (magenta) in acidic solutions.",
            "China rose extract turns green in basic solutions.",
            "Red cabbage juice provides a multi-color spectrum across the entire pH range."
        ],
        "checkpoints": [
            {
                "question": "When China rose indicator is added to shampoo lather (mildly alkaline), what color does the solution become?",
                "options": [
                    "Green",
                    "Magenta (dark pink)",
                    "Colorless",
                    "Jet black"
                ],
                "correct": 0,
                "explanation": "Shampoo solution is generally mildly basic; China rose indicator turns green in basic solutions."
            },
            {
                "question": "What color does China rose indicator exhibit in pure distilled water?",
                "options": [
                    "Bright green",
                    "Dark magenta",
                    "Light pink (its original neutral color)",
                    "Fluorescent orange"
                ],
                "correct": 2,
                "explanation": "In neutral solutions like distilled water, China rose indicator maintains its original light pink coloration."
            }
        ],
        "simulator_type": "china_rose_spectrum_lab"
    },

    # -------------------------------------------------------------
    # 6. Olfactory Indicators - The Science of Scents
    # -------------------------------------------------------------
    {
        "id": 6,
        "type": "concept_slide",
        "title": "Olfactory Indicators: The Chemistry of Scents",
        "subtitle": "Detecting Acids and Bases Through Odor Changes",
        "content": r"""
          <p>Not all chemical indicators rely on visual color changes. Some substances signal acidity or basicity through a change in their characteristic smell. These are called <strong>olfactory indicators</strong> (from the Latin <em>olfacere</em>, to smell).</p>
          <p class="mt-2">Common natural olfactory indicators include <strong>chopped onions</strong>, <strong>vanilla extract</strong>, and <strong>clove oil</strong>:</p>
          <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
            <li><strong>The Onion Strip Test:</strong> Cloth strips soaked overnight with finely chopped onions absorb pungent organic sulfur compounds (allicin derivatives).
              <ul class="list-disc pl-5 mt-1">
                <li>When treated with an <strong>acid</strong> (like dilute $\text{HCl}$), the characteristic onion smell <strong>persists strongly</strong>.</li>
                <li>When treated with a <strong>base</strong> (like $\text{NaOH}$ solution), the chemical reaction destroys the odor-producing molecules, and the onion smell <strong>completely vanishes</strong>!</li>
              </ul>
            </li>
            <li><strong>Vanilla & Clove Oil:</strong> In basic medium, the sweet fragrance of vanilla or spicy aroma of clove oil is neutralized and cannot be detected. In acidic medium, their scents remain fully intact.</li>
          </ul>
          <p class="mt-2 text-cyan-300 text-xs">⭐ Inclusive Science: Olfactory indicators enable visually impaired students to conduct rigorous chemical acid-base experiments using their sense of smell!</p>
        """,
        "formula": r"$$\text{Olfactory Rule}: \text{In Acid } \longrightarrow \mathbf{\text{Smell Persists}}, \quad \text{In Base } \longrightarrow \mathbf{\text{Smell is Destroyed / Vanishes}}$$ ",
        "key_takeaways": [
            "Olfactory indicators change their odor depending on whether they are in an acidic or basic medium.",
            "Onion cloth strips, vanilla extract, and clove oil lose their scent in basic solutions.",
            "In acidic solutions, olfactory indicators retain their distinctive smell.",
            "Olfactory testing makes chemistry accessible to visually impaired researchers."
        ],
        "checkpoints": [
            {
                "question": "What happens to the characteristic pungent smell of an onion cloth strip when it is treated with sodium hydroxide (a strong base)?",
                "options": [
                    "The smell becomes ten times stronger",
                    "The characteristic onion smell is destroyed and disappears",
                    "The cloth strip starts smelling like fresh roses",
                    "The cloth strip explodes into flames"
                ],
                "correct": 1,
                "explanation": "Bases chemically alter and neutralize the sulfur-bearing organic compounds responsible for onion odor, causing the smell to vanish."
            },
            {
                "question": "If you add drops of dilute hydrochloric acid to vanilla essence, what will you observe regarding its aroma?",
                "options": [
                    "Its sweet vanilla smell is completely destroyed",
                    "Its characteristic vanilla smell persists unchanged",
                    "It begins smelling like rotten eggs",
                    "It loses all liquid volume instantly"
                ],
                "correct": 1,
                "explanation": "In an acidic medium, olfactory indicators like vanilla retain their characteristic pleasant aroma."
            }
        ],
        "simulator_type": "olfactory_odor_lab"
    },

    # -------------------------------------------------------------
    # 7. Synthetic Indicators: Phenolphthalein & Methyl Orange
    # -------------------------------------------------------------
    {
        "id": 7,
        "type": "concept_slide",
        "title": "Synthetic Indicators: Phenolphthalein",
        "subtitle": "Precision Laboratory Dyes for Quantitative Chemical Analysis",
        "content": r"""
          <p>While natural indicators from lichens, roses, and turmeric are wonderful for exploration, precision scientific titrations often rely on pure <strong>synthetic indicators</strong> manufactured in chemical laboratories.</p>
          <p class="mt-2">The most important laboratory indicator for Grade 7 Science is <strong>Phenolphthalein</strong> ($\text{C}_{20}\text{H}_{14}\text{O}_4$):</p>
          <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
            <li><strong>In Acidic Solutions:</strong> Phenolphthalein remains completely <strong>colorless</strong>.</li>
            <li><strong>In Neutral Solutions:</strong> Phenolphthalein remains completely <strong>colorless</strong>.</li>
            <li><strong>In Basic Solutions:</strong> Phenolphthalein instantly turns a spectacular, vivid <strong>magenta-pink</strong>!</li>
          </ul>
          <p class="mt-2"><strong>Methyl Orange:</strong> Another synthetic dye that is bright <strong>red</strong> in acidic solutions ($\text{pH} < 3.1$) and <strong>yellow</strong> in neutral and basic solutions ($\text{pH} > 4.4$).</p>
          <p class="mt-2">Because phenolphthalein gives an unmistakable on/off color switch (colorless $\leftrightarrow$ deep pink), it serves as the ideal indicator to pinpoint the exact moment of complete neutralisation!</p>
        """,
        "formula": r"$$\text{Phenolphthalein}: \underbrace{\text{Colorless}}_{\text{Acidic / Neutral (pH } < 8.2\text{)}} \quad \underset{-\text{H}^+}{\overset{+\text{OH}^-}{\rightleftharpoons}} \quad \underbrace{\text{Vivid Magenta Pink}}_{\text{Basic Medium (pH } > 10.0\text{)}}$$ ",
        "key_takeaways": [
            "Phenolphthalein is completely colorless in acidic and neutral solutions.",
            "Phenolphthalein turns vivid magenta-pink in basic (alkaline) solutions.",
            "Methyl orange is red in acid and yellow in basic/neutral medium.",
            "Synthetic indicators provide sharp, reproducible end-points for quantitative neutralisation experiments."
        ],
        "checkpoints": [
            {
                "question": "A few drops of phenolphthalein are added to a beaker containing dilute sodium hydroxide solution. What color appears?",
                "options": [
                    "Vivid pink / magenta",
                    "Completely colorless",
                    "Bright yellow",
                    "Dark green"
                ],
                "correct": 0,
                "explanation": "Sodium hydroxide is a strong base. Phenolphthalein turns an unmistakable, vivid magenta-pink in basic solutions."
            },
            {
                "question": "What happens when excess hydrochloric acid is slowly poured into the pink phenolphthalein-base mixture until it is acidic?",
                "options": [
                    "The solution turns dark black",
                    "The pink color completely vanishes and the solution turns colorless",
                    "The solution solidifies into an ice cube",
                    "The solution begins glowing in the dark"
                ],
                "correct": 1,
                "explanation": "When acid neutralizes the base and makes the solution acidic, phenolphthalein switches back to its colorless form."
            }
        ],
        "simulator_type": "phenolphthalein_chamber_lab"
    },

    # -------------------------------------------------------------
    # 8. The pH Scale - Quantifying Acidity & Basicity
    # -------------------------------------------------------------
    {
        "id": 8,
        "type": "concept_slide",
        "title": "The pH Scale: Measuring Acidity & Basicity",
        "subtitle": "From Danish Breweries to the Universal 0 to 14 Scale",
        "content": r"""
          <p>Indicators like litmus tell us <em>whether</em> a substance is an acid or a base, but they cannot tell us <em>how strong</em> or <em>how weak</em> it is! To measure the exact degree of acidity or alkalinity, Danish chemist <strong>S.P.L. Sørensen</strong> invented the <strong>pH scale</strong> in 1909.</p>
          <p class="mt-2">The pH scale extends from <strong>0 to 14</strong> at room temperature ($25^\circ\text{C}$):</p>
          <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
            <li><strong>$\text{pH} < 7$ (Acidic):</strong> The lower the number, the stronger the acid. (Stomach acid $\text{pH} \approx 1.5$; lemon juice $\text{pH} \approx 2.2$; coffee $\text{pH} \approx 5.0$).</li>
            <li><strong>$\text{pH} = 7$ (Neutral):</strong> Equal concentration of $\text{H}^+$ and $\text{OH}^-$ ions. Pure distilled water has $\text{pH} = 7.0$ at $25^\circ\text{C}$.</li>
            <li><strong>$\text{pH} > 7$ (Basic / Alkaline):</strong> The higher the number, the stronger the base. (Human blood $\text{pH} \approx 7.4$; baking soda $\text{pH} \approx 8.4$; soap water $\text{pH} \approx 10.0$; drain cleaner $\text{pH} \approx 13.5$).</li>
          </ul>
          <p class="mt-2"><strong>Universal Indicator:</strong> A carefully calibrated blend of several dyes that exhibits a continuous rainbow spectrum across the entire pH range: red for strong acids, green for neutral, and violet for strong bases!</p>
        """,
        "formula": r"$$\text{The pH Spectrum}: \underbrace{0 \quad 1 \quad 2 \quad 3 \quad 4 \quad 5 \quad 6}_{\text{Acidic (Red } \rightarrow \text{ Yellow)}} \quad \underbrace{\mathbf{7}}_{\text{Neutral (Green)}} \quad \underbrace{8 \quad 9 \quad 10 \quad 11 \quad 12 \quad 13 \quad 14}_{\text{Basic (Blue } \rightarrow \text{ Violet)}}$$ ",
        "key_takeaways": [
            "The pH scale ranges from 0 (most acidic) to 14 (most basic).",
            "A pH value of exactly 7 represents neutral matter like pure distilled water.",
            "Universal indicator paper shows a continuous rainbow spectrum matching exact pH values.",
            "Each unit drop on the pH scale represents a tenfold increase in hydrogen ion concentration."
        ],
        "checkpoints": [
            {
                "question": "Which of the following pH values indicates a strongly acidic solution?",
                "options": [
                    "pH = 1.5",
                    "pH = 7.0",
                    "pH = 8.5",
                    "pH = 13.5"
                ],
                "correct": 0,
                "explanation": "Values significantly lower than 7 indicate acidity; a pH of 1.5 corresponds to a strong acid like human gastric juice."
            },
            {
                "question": "What color does Universal Indicator paper display in a neutral solution of pH 7.0?",
                "options": [
                    "Bright red",
                    "Emerald green",
                    "Deep violet",
                    "Pure black"
                ],
                "correct": 1,
                "explanation": "Universal indicator is calibrated to turn emerald green in neutral solutions at pH 7.0."
            }
        ],
        "simulator_type": "universal_ph_scale_strip"
    },

    # -------------------------------------------------------------
    # 9. Neutralisation: Acid Meets Base
    # -------------------------------------------------------------
    {
        "id": 9,
        "type": "concept_slide",
        "title": "What Happens When Acids and Bases Mix?",
        "subtitle": "The Neutralisation Reaction: Acid + Base ➔ Salt + Water + Heat",
        "content": r"""
          <p>What happens when an acidic substance and a basic substance are mixed together in balanced proportions? Do their opposite properties wage war, or do they cancel each other out?</p>
          <p class="mt-2">They neutralize each other! The reaction between an acid and a base is called a <strong>neutralisation reaction</strong>. In this chemical process, the acidic nature of the acid and the basic nature of the base are completely destroyed:</p>
          <div class="p-3 my-2 rounded-xl bg-slate-900 border border-emerald-500/40 text-center text-xs sm:text-sm font-mono text-emerald-300">
            $$\text{Acid} + \text{Base} \longrightarrow \text{Salt} + \text{Water} + \text{Heat}$$
          </div>
          <p class="mt-2">Consider the classic laboratory reaction between <strong>Hydrochloric acid ($\text{HCl}$)</strong> and <strong>Sodium hydroxide ($\text{NaOH}$)</strong>:</p>
          <div class="p-3 my-2 rounded-xl bg-slate-950 border border-cyan-500/30 text-center text-xs font-mono text-cyan-300">
            $$\text{HCl} + \text{NaOH} \longrightarrow \text{NaCl (common table salt)} + \text{H}_2\text{O (water)} + \text{Heat}$$
          </div>
          <p class="mt-2"><strong>Heat is Always Released (Exothermic):</strong> If you touch the conical flask immediately after mixing an acid and a base, it feels distinctly <strong>warm</strong>! Neutralisation always releases thermal energy.</p>
        """,
        "formula": r"$$\text{Neutralisation Invariant}: \text{H}^+\text{(aq)} + \text{OH}^-\text{(aq)} \longrightarrow \text{H}_2\text{O(l)} + 57.3\text{ kJ/mol (Heat)}$$",
        "key_takeaways": [
            "Neutralisation is the reaction between an acid and a base forming a salt and water.",
            "The products of neutralisation are neither acidic nor basic (neutral in equal strength).",
            "Neutralisation is strictly exothermic: heat is evolved, raising the mixture's temperature.",
            "The chemical formula: Acid + Base ➔ Salt + Water + Heat."
        ],
        "checkpoints": [
            {
                "question": "What two chemical products are always formed when an acid reacts with a base in a neutralisation reaction?",
                "options": [
                    "Carbon dioxide and methane gas",
                    "Salt and water",
                    "Pure oxygen and hydrogen gas",
                    "Gold and silver crystals"
                ],
                "correct": 1,
                "explanation": "In any neutralisation reaction, the acid and base react to form a salt and water: $\\text{Acid} + \\text{Base} \\rightarrow \\text{Salt} + \\text{Water} + \\text{Heat}$."
            },
            {
                "question": "When you touch the bottom of a test tube immediately following a neutralisation reaction, what will you feel?",
                "options": [
                    "The test tube feels noticeably warm because heat is evolved",
                    "The test tube freezes into solid ice",
                    "The test tube becomes magnetically charged",
                    "No temperature change whatsoever"
                ],
                "correct": 0,
                "explanation": "Neutralisation reactions are exothermic; the formation of water from hydrogen and hydroxide ions releases thermal energy ($57.3\\text{ kJ/mol}$), warming the container."
            }
        ],
        "simulator_type": "neutralisation_reaction_chamber"
    },

    # -------------------------------------------------------------
    # 10. Titration Mechanics & Exothermic Tracking
    # -------------------------------------------------------------
    {
        "id": 10,
        "type": "concept_slide",
        "title": "Titration Mechanics & Exothermic Tracking",
        "subtitle": "Pinpointing the Exact Equivalence Point with Phenolphthalein",
        "content": r"""
          <p>How do chemists ensure that an acid and a base have reacted in exact, stoichiometric equivalence? They perform a precise technique called a <strong>titration</strong> using a graduated glass burette and a conical flask.</p>
          <p class="mt-2"><strong>Step-by-Step Titration Experiment:</strong></p>
          <ol class="list-decimal pl-5 mt-1 space-y-1 text-slate-300">
            <li>Measure $10\text{ mL}$ of dilute hydrochloric acid ($\text{HCl}$) into a conical flask.</li>
            <li>Add 2 to 3 drops of phenolphthalein indicator. The solution remains completely <strong>colorless</strong>.</li>
            <li>Fill a burette with dilute sodium hydroxide ($\text{NaOH}$) solution.</li>
            <li>Slowly add $\text{NaOH}$ drop by drop, swirling the flask continuously. A thermometer records rising temperature.</li>
            <li>As long as acid is in excess, the mixture stays colorless. At the exact drop where the acid is fully neutralized, the very next fraction of a drop turns the entire solution a faint, permanent <strong>pink</strong>!</li>
          </ol>
          <p class="mt-2">This sharp color change marks the <strong>end-point</strong>: the acid has been 100% neutralized into neutral saltwater ($\text{NaCl} + \text{H}_2\text{O}$).</p>
        """,
        "formula": r"$$\text{Equivalence Point}: \text{Moles of H}^+ = \text{Moles of OH}^- \quad (\text{Phenolphthalein transitions Colorless } \longrightarrow \text{ Faint Pink})$$",
        "key_takeaways": [
            "Titration allows precise volumetric addition of base to acid to find the neutral point.",
            "Phenolphthalein serves as an on/off indicator: colorless in acid, faint pink at neutral end-point.",
            "Swirling ensures rapid, uniform mixing and complete chemical neutralisation.",
            "Continuous temperature monitoring proves the exothermic release of chemical bond energy."
        ],
        "checkpoints": [
            {
                "question": "During a titration of hydrochloric acid with sodium hydroxide using phenolphthalein, what indicates that the end-point has been reached?",
                "options": [
                    "The liquid suddenly turns bright green",
                    "A single drop of base causes the colorless solution to turn a permanent faint pink",
                    "Dense white smoke shoots out of the flask",
                    "The flask becomes completely frozen"
                ],
                "correct": 1,
                "explanation": "At the equivalence point, all acid is consumed; the very next trace of hydroxide turns phenolphthalein to its characteristic pink form."
            },
            {
                "question": "If you add several more drops of hydrochloric acid to the newly pink solution, what will occur?",
                "options": [
                    "The solution stays pink forever",
                    "The solution turns colorless again because the mixture becomes acidic",
                    "The liquid turns bright purple",
                    "The flask shatters from pressure"
                ],
                "correct": 1,
                "explanation": "Adding excess acid shifts the solution back to an acidic state, returning phenolphthalein to its colorless form."
            }
        ],
        "simulator_type": "titration_burette_lab"
    },

    # -------------------------------------------------------------
    # 11. Neutralisation in Daily Life: Ant Bites & Stings
    # -------------------------------------------------------------
    {
        "id": 11,
        "type": "concept_slide",
        "title": "Neutralisation in Daily Life: Ant Bites & Stings",
        "subtitle": "Soothing Formic Acid Injections with Mild Alkaline Bases",
        "content": r"""
          <p>Neutralisation is not confined to laboratory test tubes—it is a vital biological defense that we use every day! Consider the sharp, burning sting of a red ant bite.</p>
          <p class="mt-2"><strong>The Chemistry of an Ant Bite:</strong></p>
          <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
            <li>When an ant bites, it pierces human skin and injects an acidic venom containing <strong>formic acid (methanoic acid, $\text{HCOOH}$)</strong>.</li>
            <li>Formic acid irritates sensory pain nerves, triggering immediate swelling, redness, and a painful burning sensation.</li>
          </ul>
          <p class="mt-2"><strong>The Neutralisation Remedy:</strong></p>
          <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
            <li>To soothe the burning pain, we rub the stung skin with a mild, safe basic substance:
              <ul class="list-disc pl-5 mt-1">
                <li><strong>Moist Baking Soda:</strong> Sodium hydrogen carbonate ($\text{NaHCO}_3$), a mild household base.</li>
                <li><strong>Calamine Lotion:</strong> Contains zinc carbonate ($\text{ZnCO}_3$), which chemically neutralizes the acidic venom.</li>
              </ul>
            </li>
            <li>The base reacts with formic acid, neutralizing it into harmless zinc or sodium formate salt and water, providing rapid relief!</li>
          </ul>
          <p class="mt-2 text-amber-300 text-xs">🐝 Contrast with Wasp Stings: A wasp sting is <strong>alkaline (basic)</strong>! Rubbing baking soda on a wasp sting makes it worse. Instead, wasp stings are neutralized with a mild acid like <strong>vinegar</strong>!</p>
        """,
        "formula": r"$$\text{Ant Bite Remedy}: \underbrace{\text{HCOOH (Formic Acid Venom)}}_{\text{Acidic Stinger}} + \underbrace{\text{NaHCO}_3 \text{ (Baking Soda)}}_{\text{Mild Base}} \longrightarrow \underbrace{\text{HCOONa (Sodium Formate Salt)} + \text{H}_2\text{O} + \text{CO}_2}_{\text{Harmless Neutral Products}}$$",
        "key_takeaways": [
            "Ant venom contains formic acid (methanoic acid), causing burning and inflammation.",
            "Applying moist baking soda ($\text{NaHCO}_3$) or calamine lotion ($\text{ZnCO}_3$) neutralizes the acid.",
            "Wasp stings are alkaline and are soothed with mild acids like vinegar.",
            "Knowing whether a sting is acidic or basic determines the correct neutralisation cure!"
        ],
        "checkpoints": [
            {
                "question": "What chemical acid is injected into human skin during an ant bite?",
                "options": [
                    "Formic acid (methanoic acid)",
                    "Concentrated sulfuric acid",
                    "Citric acid",
                    "Nitric acid"
                ],
                "correct": 0,
                "explanation": "Ants secrete formic acid (from Latin 'formica', ant) into the sting wound, causing painful local inflammation."
            },
            {
                "question": "Which of the following household substances should be applied to soothe an ant bite?",
                "options": [
                    "Lemon juice",
                    "Moist baking soda paste or calamine lotion",
                    "Pure vinegar",
                    "Battery acid"
                ],
                "correct": 1,
                "explanation": "Baking soda and calamine are mild bases that chemically neutralize the acidic formic acid venom without harming skin."
            }
        ],
        "simulator_type": "ant_bite_neutraliser_lab"
    },

    # -------------------------------------------------------------
    # 12. Neutralisation in Daily Life: Soil Management
    # -------------------------------------------------------------
    {
        "id": 12,
        "type": "concept_slide",
        "title": "Neutralisation in Daily Life: Soil Management",
        "subtitle": "Balancing Agricultural Soil pH for Optimum Crop Yield",
        "content": r"""
          <p>Agriculture depends fundamentally on soil chemistry. Most food crops (wheat, rice, pulses, and vegetables) thrive best in nearly neutral soil with a pH between <strong>6.0 and 7.5</strong>. If soil becomes excessively acidic or excessively basic, plant roots cannot absorb vital nutrients!</p>
          <p class="mt-2"><strong>Case 1: When Soil is Too Acidic ($\text{pH} < 5.5$)</strong></p>
          <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
            <li><em>Cause:</em> Heavy overuse of synthetic chemical nitrogen fertilizers (like urea and ammonium sulfate) or continuous acid rain.</li>
            <li><em>Remedy:</em> Farmers treat acidic soil with basic compounds:
              <ul class="list-disc pl-5 mt-1">
                <li><strong>Quicklime:</strong> Calcium oxide ($\text{CaO}$).</li>
                <li><strong>Slaked lime:</strong> Calcium hydroxide ($\text{Ca(OH)}_2$) or powdered chalk/limestone ($\text{CaCO}_3$).</li>
              </ul>
            </li>
            <li>These bases react with soil acids, raising the pH back to the ideal fertile neutral zone.</li>
          </ul>
          <p class="mt-2"><strong>Case 2: When Soil is Too Basic ($\text{pH} > 8.5$)</strong></p>
          <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
            <li><em>Remedy:</em> Farmers add <strong>organic matter (manure and compost)</strong>. As microbes decompose organic waste, they naturally release organic acids that neutralize alkaline soil compounds!</li>
          </ul>
        """,
        "formula": r"$$\text{Acidic Soil Liming}: \text{Soil Acidity (2H}^+\text{)} + \text{Ca(OH)}_2 \text{ (Slaked Lime)} \longrightarrow \text{Ca}^{2+} + 2\text{H}_2\text{O} \quad (\text{pH restored to 6.8})$$",
        "key_takeaways": [
            "Plants cannot absorb nutrients efficiently if soil is excessively acidic or excessively basic.",
            "Excess chemical fertilizers cause soil acidification.",
            "Acidic soil is treated with quicklime ($\text{CaO}$) or slaked lime ($\text{Ca(OH)}_2$).",
            "Basic soil is treated with decomposing organic matter/manure which releases natural acids."
        ],
        "checkpoints": [
            {
                "question": "What should a farmer add to an agricultural field that has become excessively acidic due to over-fertilization?",
                "options": [
                    "Quicklime (calcium oxide) or slaked lime (calcium hydroxide)",
                    "Battery acid",
                    "Lemon juice",
                    "Vinegar"
                ],
                "correct": 0,
                "explanation": "Quicklime and slaked lime are basic compounds that neutralize excess soil acidity, restoring healthy pH for plant roots."
            },
            {
                "question": "How does adding compost or farmyard manure help cure excessively basic (alkaline) soil?",
                "options": [
                    "Manure adds more lime to the soil",
                    "Decomposing organic matter releases natural acids that neutralize soil bases",
                    "Manure freezes the soil solid",
                    "Manure removes all water from the soil"
                ],
                "correct": 1,
                "explanation": "Microbial decomposition of organic compost releases organic acids (humic and fulvic acids) that naturally neutralize soil alkalinity."
            }
        ],
        "simulator_type": "soil_ph_management_lab"
    },

    # -------------------------------------------------------------
    # 13. Neutralisation in Daily Life: Industrial Effluents
    # -------------------------------------------------------------
    {
        "id": 13,
        "type": "concept_slide",
        "title": "Industrial Effluent & Environmental Protection",
        "subtitle": "Treating Factory Acid Wastes to Safeguard Aquatic Ecosystems",
        "content": r"""
          <p>Modern industrial facilities—including textile dyeing mills, battery manufacturers, electroplating units, and chemical synthesis plants—generate millions of liters of liquid waste containing strong acids like sulfuric acid ($\text{H}_2\text{SO}_4$) and hydrochloric acid ($\text{HCl}$).</p>
          <p class="mt-2"><strong>The Environmental Hazard:</strong></p>
          <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
            <li>If untreated acidic factory waste is directly discharged into rivers, streams, and lakes, water pH plunges below 4.0.</li>
            <li>Acidic water damages the gills of fish, destroys microscopic phytoplankton (the base of aquatic food chains), and leaches toxic heavy metals (like lead and mercury) from riverbed sediments.</li>
          </ul>
          <p class="mt-2"><strong>The Neutralisation Protocol:</strong></p>
          <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
            <li>Environmental protection laws mandate that industrial plants establish dedicated <strong>Effluent Treatment Plants (ETPs)</strong>.</li>
            <li>Acidic wastewater is routed into large treatment holding tanks where controlled quantities of cheap basic substances—such as <strong>slaked lime ($\text{Ca(OH)}_2$)</strong> or limestone powder—are thoroughly churned in.</li>
            <li>The base neutralizes the corrosive acids into harmless, insoluble calcium salts and neutral water before environmental discharge!</li>
          </ul>
        """,
        "formula": r"$$\text{Effluent Neutralisation}: \text{H}_2\text{SO}_4\text{(aq)} + \text{Ca(OH)}_2\text{(s)} \longrightarrow \text{CaSO}_4\text{(s)} \downarrow + 2\text{H}_2\text{O(l)} \quad (\text{Safe Effluent pH } \approx 7.0)$$",
        "key_takeaways": [
            "Industrial wastewater often contains concentrated, corrosive acids.",
            "Dumping acidic factory waste directly into water bodies kills fish and destroys ecosystems.",
            "Factories must neutralize acidic waste by adding basic lime ($\text{Ca(OH)}_2$) before discharge.",
            "Neutralisation in ETPs protects biodiversity and keeps drinking water sources safe."
        ],
        "checkpoints": [
            {
                "question": "Why must acidic industrial factory waste be treated with basic substances before discharging into rivers?",
                "options": [
                    "To turn the river water into drinkable milk",
                    "To prevent acidic water from poisoning fish and destroying the aquatic ecosystem",
                    "To make the river flow faster",
                    "To generate electricity inside the river"
                ],
                "correct": 1,
                "explanation": "Untreated acidic effluent suffocates aquatic life and destabilizes aquatic ecosystems; neutralizing with base prevents environmental disaster."
            },
            {
                "question": "Which inexpensive basic substance is universally used in industrial Effluent Treatment Plants (ETPs) to neutralize acid waste?",
                "options": [
                    "Slaked lime (calcium hydroxide)",
                    "Pure molten gold",
                    "Concentrated sulfuric acid",
                    "Distilled water"
                ],
                "correct": 0,
                "explanation": "Slaked lime is an abundant, cost-effective base that effectively neutralizes strong industrial acids into neutral salts."
            }
        ],
        "simulator_type": "factory_effluent_plant_lab"
    },

    # -------------------------------------------------------------
    # 14. Neutralisation in Daily Life: Indigestion & Dental Health
    # -------------------------------------------------------------
    {
        "id": 14,
        "type": "concept_slide",
        "title": "Indigestion Antacids & Dental Protection",
        "subtitle": "Biochemical Neutralisation Inside the Human Body",
        "content": r"""
          <p>Neutralisation is essential to human health, working continuously to balance digestive processes in our stomachs and protect enamel on our teeth.</p>
          <p class="mt-2"><strong>1. Soothing Stomach Acidity & Indigestion:</strong></p>
          <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
            <li>Our stomach's gastric glands naturally produce dilute <strong>hydrochloric acid ($\text{HCl}$, pH $\approx 1.5$ to $2.0$)</strong> to activate digestive enzymes (pepsin) and destroy harmful bacteria.</li>
            <li>Stress, irregular eating, or excess spicy food can cause <strong>hyperacidity (indigestion)</strong>, where excess acid causes painful burning in the stomach and esophagus (heartburn).</li>
            <li>We consume <strong>antacids</strong>—mild, non-corrosive basic medicines such as <strong>Milk of Magnesia (magnesium hydroxide, $\text{Mg(OH)}_2$)</strong> or aluminium hydroxide. The antacid neutralizes excess acid:
              $$\text{Mg(OH)}_2 + 2\text{HCl} \longrightarrow \text{MgCl}_2 + 2\text{H}_2\text{O}$$
            </li>
          </ul>
          <p class="mt-2"><strong>2. Tooth Decay & Toothpaste:</strong> Bacteria in our mouth feed on lingering food sugars and secrete acids. If mouth pH drops below $5.5$, tooth enamel (calcium hydroxyapatite) begins to dissolve! Modern toothpaste is formulated to be <strong>mildly alkaline</strong> to neutralize residual mouth acids and prevent cavities.</p>
        """,
        "formula": r"$$\text{Antacid Relief}: \text{Mg(OH)}_2\text{ (Milk of Magnesia)} + 2\text{HCl (Stomach Acid)} \longrightarrow \text{MgCl}_2\text{ (Salt)} + 2\text{H}_2\text{O} \quad (\text{Pain Relieved!})$$",
        "key_takeaways": [
            "The stomach secretes dilute hydrochloric acid ($\text{HCl}$) for healthy digestion.",
            "Excess stomach acid produces painful indigestion, treated with antacids.",
            "Antacids contain mild bases like Milk of Magnesia ($\text{Mg(OH)}_2$).",
            "Toothpaste is mildly basic to neutralize mouth acids that erode tooth enamel."
        ],
        "checkpoints": [
            {
                "question": "What active chemical base is present in the common antacid 'Milk of Magnesia'?",
                "options": [
                    "Magnesium hydroxide [$\\text{Mg(OH)}_2$]",
                    "Concentrated hydrochloric acid [$\\text{HCl}$]",
                    "Sodium chloride [$\\text{NaCl}$]",
                    "Pure copper sulfate [$\\text{CuSO}_4$]"
                ],
                "correct": 0,
                "explanation": "Milk of Magnesia is a suspension of magnesium hydroxide, a mild insoluble base that neutralizes excess gastric hydrochloric acid without burning tissues."
            },
            {
                "question": "Why is commercial toothpaste formulated to be mildly basic (alkaline)?",
                "options": [
                    "To color the teeth blue",
                    "To neutralize acids produced by mouth bacteria that cause enamel erosion and tooth decay",
                    "To make teeth softer for chewing",
                    "To help bacteria grow faster"
                ],
                "correct": 1,
                "explanation": "Alkaline toothpaste neutralizes microbial acids produced from fermenting sugars, preserving dental enamel."
            }
        ],
        "simulator_type": "antacid_dental_health_lab"
    },

    # -------------------------------------------------------------
    # 15. Acharya P.C. Ray & Indian Chemistry Heritage
    # -------------------------------------------------------------
    {
        "id": 15,
        "type": "concept_slide",
        "title": "Acharya P.C. Ray & The Heritage of Chemistry",
        "subtitle": "Pioneering Indian Synthetic Chemistry & Indigenous Industry",
        "content": r"""
          <p>India holds a rich, thousands-of-years-old heritage in chemistry, known in Sanskrit as <strong>Rasashastra</strong> (the science of juices, minerals, and chemical reactions). Ancient Indian scholars classified alkalis as <strong>Kṣāra (क्षार)</strong> and acids as <strong>Amla (अम्ल)</strong>.</p>
          <p class="mt-2">The revered father of modern Indian chemistry is <strong>Acharya Prafulla Chandra Ray (1861–1944)</strong>:</p>
          <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
            <li><strong>Synthesis of Mercurous Nitrite:</strong> In 1896, working in his modest laboratory at Presidency College Kolkata, Ray made a breakthrough discovery by synthesizing <strong>mercurous nitrite ($\text{Hg}_2(\text{NO}_2)_2$)</strong>, a compound previously believed to be too unstable to exist!</li>
            <li><strong>Historian of Science:</strong> He authored the monumental work <em>"A History of Hindu Chemistry"</em>, documenting the sophisticated metallurgical, distillation, and alkali-purification techniques of ancient Indian scholars like Nagarjuna.</li>
            <li><strong>Founder of Indigenous Industry:</strong> P.C. Ray founded <strong>Bengal Chemical & Pharmaceutical Works</strong> in 1901—India's first modern chemical and pharmaceutical company—demonstrating that science must foster economic self-reliance.</li>
          </ul>
        """,
        "formula": r"$$\text{Mercurous Nitrite Discovery (1896)}: 2\text{Hg} + 4\text{HNO}_3\text{ (dilute)} \longrightarrow \text{Hg}_2(\text{NO}_2)_2 + 2\text{H}_2\text{O} + 2\text{NO} \uparrow$$",
        "key_takeaways": [
            "Acharya Prafulla Chandra Ray is celebrated as the Father of Modern Indian Chemistry.",
            "In 1896, Ray synthesized stable mercurous nitrite ($\text{Hg}_2(\text{NO}_2)_2$), gaining global acclaim.",
            "He founded Bengal Chemicals (1901), pioneering indigenous Indian manufacturing.",
            "His historical research uncovered ancient Indian traditions of Rasashastra (alkalis and acids)."
        ],
        "checkpoints": [
            {
                "question": "Which historic chemical compound was synthesized by Acharya Prafulla Chandra Ray in 1896, winning international acclaim?",
                "options": [
                    "Mercurous nitrite [$\\text{Hg}_2(\\text{NO}_2)_2$]",
                    "Synthetic plastic",
                    "Pure liquid uranium",
                    "Stainless steel"
                ],
                "correct": 0,
                "explanation": "P.C. Ray's synthesis of stable mercurous nitrite from mercury and dilute nitric acid in 1896 established modern Indian experimental chemistry."
            },
            {
                "question": "What historic pharmaceutical manufacturing enterprise was founded by Acharya P.C. Ray in 1901 to promote Indian self-reliance?",
                "options": [
                    "Bengal Chemical & Pharmaceutical Works",
                    "The East India Tea Company",
                    "The Indian Railway Board",
                    "ISRO Rocket Laboratory"
                ],
                "correct": 0,
                "explanation": "Ray founded Bengal Chemical & Pharmaceutical Works in Kolkata, pioneering India's indigenous chemical and pharmaceutical industry."
            }
        ],
        "simulator_type": "pc_ray_chemistry_heritage"
    },

    # -------------------------------------------------------------
    # 16. Chapter Summary & The Acid-Base Master Wheel
    # -------------------------------------------------------------
    {
        "id": 16,
        "type": "concept_slide",
        "title": "Master Synthesis: The Acid-Base-Salt Map",
        "subtitle": "Consolidating All Indicators, Reactions, and Daily Applications",
        "content": r"""
          <p>Let us consolidate everything you have mastered across Chapter 2 into one comprehensive diagnostic matrix:</p>
          <div class="overflow-x-auto my-3 text-[11px]">
            <table class="w-full text-left border-collapse border border-slate-700 bg-slate-950">
              <thead>
                <tr class="bg-slate-900 text-amber-400 border-b border-slate-700">
                  <th class="p-2 border-r border-slate-700">Indicator</th>
                  <th class="p-2 border-r border-slate-700 text-rose-300">Acidic Medium</th>
                  <th class="p-2 border-r border-slate-700 text-slate-300">Neutral Medium</th>
                  <th class="p-2 text-cyan-300">Basic Medium</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-800 text-slate-300">
                <tr>
                  <td class="p-2 font-bold border-r border-slate-800 text-amber-300">Blue Litmus Paper</td>
                  <td class="p-2 border-r border-slate-800 text-rose-400 font-bold">Turns RED</td>
                  <td class="p-2 border-r border-slate-800">Remains Blue</td>
                  <td class="p-2 text-cyan-400">Remains Blue</td>
                </tr>
                <tr>
                  <td class="p-2 font-bold border-r border-slate-800 text-amber-300">Red Litmus Paper</td>
                  <td class="p-2 border-r border-slate-800 text-rose-400">Remains Red</td>
                  <td class="p-2 border-r border-slate-800">Remains Red</td>
                  <td class="p-2 text-cyan-400 font-bold">Turns BLUE</td>
                </tr>
                <tr>
                  <td class="p-2 font-bold border-r border-slate-800 text-amber-300">Turmeric (Haldi)</td>
                  <td class="p-2 border-r border-slate-800">Remains Yellow</td>
                  <td class="p-2 border-r border-slate-800">Remains Yellow</td>
                  <td class="p-2 text-rose-400 font-bold">Turns REDDISH-BROWN</td>
                </tr>
                <tr>
                  <td class="p-2 font-bold border-r border-slate-800 text-amber-300">Red Rose Extract</td>
                  <td class="p-2 border-r border-slate-800 text-rose-400 font-bold">Turns Deep Red</td>
                  <td class="p-2 border-r border-slate-800">Light Pink</td>
                  <td class="p-2 text-emerald-400 font-bold">Turns GREEN</td>
                </tr>
                <tr>
                  <td class="p-2 font-bold border-r border-slate-800 text-amber-300">China Rose (Gudhal)</td>
                  <td class="p-2 border-r border-slate-800 text-pink-400 font-bold">Turns Magenta</td>
                  <td class="p-2 border-r border-slate-800">Light Pink</td>
                  <td class="p-2 text-emerald-400 font-bold">Turns GREEN</td>
                </tr>
                <tr>
                  <td class="p-2 font-bold border-r border-slate-800 text-amber-300">Phenolphthalein</td>
                  <td class="p-2 border-r border-slate-800">Colorless</td>
                  <td class="p-2 border-r border-slate-800">Colorless</td>
                  <td class="p-2 text-pink-400 font-bold">Turns VIVID PINK</td>
                </tr>
                <tr>
                  <td class="p-2 font-bold border-r border-slate-800 text-amber-300">Olfactory (Onion/Vanilla)</td>
                  <td class="p-2 border-r border-slate-800 text-emerald-400">Odor Persists</td>
                  <td class="p-2 border-r border-slate-800">Odor Persists</td>
                  <td class="p-2 text-rose-400 font-bold">Odor DESTROYED</td>
                </tr>
              </tbody>
            </table>
          </div>
        """,
        "formula": r"$$\text{Universal Formula}: \text{Acid (H}^+\text{)} + \text{Base (OH}^-\text{)} \longrightarrow \text{Salt} + \text{H}_2\text{O} + \text{Heat}$$",
        "key_takeaways": [
            "Acids turn blue litmus red, rose extract dark red, and keep turmeric yellow.",
            "Bases turn red litmus blue, turmeric reddish-brown, rose extract green, and phenolphthalein pink.",
            "Neutralisation always yields salt, water, and heat.",
            "Real-life applications: antacids for heartburn, lime for acidic soil, and baking soda for ant bites."
        ],
        "checkpoints": [
            {
                "question": "Which of the following substances will produce a green color with China rose indicator?",
                "options": [
                    "Baking soda solution (basic)",
                    "Lemon juice (acidic)",
                    "Distilled water (neutral)",
                    "Vinegar (acidic)"
                ],
                "correct": 0,
                "explanation": "China rose indicator turns green in basic solutions like baking soda."
            },
            {
                "question": "What is the common term for a reaction where an acid and base react completely to form salt and water?",
                "options": [
                    "Neutralisation reaction",
                    "Combustion reaction",
                    "Fermentation",
                    "Photosynthesis"
                ],
                "correct": 0,
                "explanation": "The chemical process where acids and bases eliminate each other's properties to form salt and water is called neutralisation."
            }
        ],
        "simulator_type": "master_substance_wheel"
    },

    # -------------------------------------------------------------
    # 17. Mastery Quiz 1: Natural Indicators (Questions 1 - 10)
    # -------------------------------------------------------------
    {
        "id": 17,
        "type": "quiz_slide",
        "title": "Mastery Challenge I: Natural Indicators",
        "subtitle": "Test Your Knowledge on Litmus, Red Rose, Turmeric, and China Rose",
        "questions": [
            {
                "question": "1. From which organism is the natural acid-base indicator litmus extracted?",
                "options": [
                    "Lichens (symbiosis of algae and fungi)",
                    "Rose petals",
                    "Mushrooms",
                    "Bark of the neem tree"
                ],
                "correct": 0,
                "solution": "Litmus is a natural water-soluble dye extracted from lichens, which are composite symbiotic organisms formed by algae and fungi."
            },
            {
                "question": "2. What color does blue litmus paper turn when dipped into fresh orange juice?",
                "options": [
                    "Red",
                    "Green",
                    "Remains blue",
                    "Yellow"
                ],
                "correct": 0,
                "solution": "Orange juice contains citric acid and ascorbic acid. Acidic solutions turn blue litmus paper red."
            },
            {
                "question": "3. What happens to yellow turmeric paper when placed into washing soda solution?",
                "options": [
                    "It turns deep reddish-brown",
                    "It turns bright blue",
                    "It remains yellow",
                    "It turns completely colorless"
                ],
                "correct": 0,
                "solution": "Washing soda is alkaline (basic). Curcumin in turmeric reacts with hydroxide ions to turn deep reddish-brown."
            },
            {
                "question": "4. Red rose petal extract turns which color when added to a basic solution?",
                "options": [
                    "Green / yellowish-green",
                    "Dark red",
                    "Colorless",
                    "Bright pink"
                ],
                "correct": 0,
                "solution": "Red rose petal extract turns green or yellowish-green in a basic medium, while turning deep red in acidic solutions."
            },
            {
                "question": "5. What color does China rose indicator exhibit in acidic solutions like vinegar?",
                "options": [
                    "Dark pink (magenta)",
                    "Green",
                    "Yellow",
                    "Colorless"
                ],
                "correct": 0,
                "solution": "China rose (Gudhal) extract turns an intense dark pink (magenta) in acidic solutions."
            },
            {
                "question": "6. A solution has no effect on either red litmus paper or blue litmus paper. What is the nature of this solution?",
                "options": [
                    "Neutral",
                    "Strongly acidic",
                    "Strongly basic",
                    "Highly toxic"
                ],
                "correct": 0,
                "solution": "Neutral solutions (like pure distilled water or sodium chloride brine) cause no color change on either red or blue litmus paper."
            },
            {
                "question": "7. Why does scrubbing a turmeric curry stain on a shirt with soap turn it red?",
                "options": [
                    "Laundry soap is basic, causing turmeric's curcumin to turn reddish-brown",
                    "Soap contains red chemical dye",
                    "The cloth fabric burns from heat",
                    "The yellow dye evaporates instantly"
                ],
                "correct": 0,
                "solution": "Laundry soap is a basic substance ($\text{pH} > 9$), which triggers a color reaction with curcumin, turning the yellow stain reddish-brown."
            },
            {
                "question": "8. If you add lemon juice to the red curry stain mentioned above, what will happen?",
                "options": [
                    "The stain turns yellow again as acid neutralizes the soap base",
                    "The cloth dissolves completely",
                    "The stain turns black",
                    "The stain starts glowing"
                ],
                "correct": 0,
                "solution": "Lemon juice contains citric acid, which neutralizes the alkaline soap residue, restoring curcumin to its native yellow form."
            },
            {
                "question": "9. What is the color of neutral litmus solution in pure distilled water?",
                "options": [
                    "Mauve (purple)",
                    "Bright yellow",
                    "Emerald green",
                    "Colorless"
                ],
                "correct": 0,
                "solution": "Neutral litmus solution has a distinctive mauve (purple) coloration in distilled water."
            },
            {
                "question": "10. Which of the following pairs contains natural indicators exclusively?",
                "options": [
                    "Turmeric and China rose extract",
                    "Phenolphthalein and methyl orange",
                    "Litmus and phenolphthalein",
                    "Hydrochloric acid and sodium hydroxide"
                ],
                "correct": 0,
                "solution": "Turmeric and China rose are both plant-derived natural indicators, unlike synthetic phenolphthalein or methyl orange."
            }
        ]
    },

    # -------------------------------------------------------------
    # 18. Mastery Quiz 2: Synthetic & Olfactory Indicators (Questions 11 - 20)
    # -------------------------------------------------------------
    {
        "id": 18,
        "type": "quiz_slide",
        "title": "Mastery Challenge II: Synthetic & Olfactory Indicators",
        "subtitle": "Test Your Understanding of Phenolphthalein, Odors, and the pH Scale",
        "questions": [
            {
                "question": "11. What color is phenolphthalein indicator in an acidic solution?",
                "options": [
                    "Colorless",
                    "Pink",
                    "Blue",
                    "Green"
                ],
                "correct": 0,
                "solution": "Phenolphthalein remains completely colorless in acidic and neutral solutions; it only turns pink in basic solutions."
            },
            {
                "question": "12. In which medium does phenolphthalein turn vivid magenta-pink?",
                "options": [
                    "Basic medium",
                    "Acidic medium",
                    "Pure distilled water",
                    "Dry air"
                ],
                "correct": 0,
                "solution": "Phenolphthalein turns a vivid magenta-pink in basic (alkaline) solutions above approximately pH 8.2."
            },
            {
                "question": "13. What is an 'olfactory indicator'?",
                "options": [
                    "An indicator whose odor changes depending on whether it is in an acidic or basic medium",
                    "An indicator that glows in the dark",
                    "An indicator that changes into a solid crystal",
                    "An indicator that only works in freezing temperatures"
                ],
                "correct": 0,
                "solution": "Olfactory indicators (from Latin 'olfacere', to smell) are substances whose distinctive smell changes or vanishes in acidic or basic mediums."
            },
            {
                "question": "14. What happens to the smell of vanilla extract when added to sodium hydroxide solution?",
                "options": [
                    "The vanilla aroma is destroyed and cannot be detected",
                    "The vanilla smell becomes much stronger",
                    "It begins smelling like rotten onions",
                    "No change in smell occurs"
                ],
                "correct": 0,
                "solution": "Bases react with the aromatic aldehyde vanillin, neutralizing and eliminating its characteristic sweet smell."
            },
            {
                "question": "15. Who invented the pH scale in 1909 to quantify acidity and alkalinity?",
                "options": [
                    "S.P.L. Sørensen",
                    "Sir Isaac Newton",
                    "Alexander Fleming",
                    "Galileo Galilei"
                ],
                "correct": 0,
                "solution": "Danish chemist S.P.L. Sørensen introduced the pH scale at the Carlsberg Laboratory in 1909."
            },
            {
                "question": "16. A solution has a pH of 7.0 at 25°C. What is its chemical classification?",
                "options": [
                    "Neutral",
                    "Strongly acidic",
                    "Strongly basic",
                    "Super-saturated"
                ],
                "correct": 0,
                "solution": "A pH of exactly 7.0 represents a neutral solution where hydrogen ion and hydroxide ion concentrations are balanced."
            },
            {
                "question": "17. Which of the following pH values indicates the strongest acid?",
                "options": [
                    "pH = 1.0",
                    "pH = 5.0",
                    "pH = 7.0",
                    "pH = 13.0"
                ],
                "correct": 0,
                "solution": "On the pH scale, lower numbers signify higher hydrogen ion concentration; pH 1.0 is the strongest acid among the options."
            },
            {
                "question": "18. What is 'Universal Indicator'?",
                "options": [
                    "A calibrated mixture of several indicators that exhibits distinct rainbow colors across the entire pH range",
                    "A single chemical that turns red in everything",
                    "Pure liquid mercury used to measure temperature",
                    "A dye that only works in outer space"
                ],
                "correct": 0,
                "solution": "Universal indicator is a mixture of organic dyes (including thymol blue, methyl red, bromothymol blue, and phenolphthalein) showing continuous color gradients from red to purple."
            },
            {
                "question": "19. Which indicator would be ideal for a visually impaired student conducting an acid-base experiment?",
                "options": [
                    "Onion cloth strip or clove oil (olfactory indicator)",
                    "Phenolphthalein",
                    "Blue litmus paper",
                    "Turmeric paper"
                ],
                "correct": 0,
                "solution": "Olfactory indicators rely on sense of smell rather than visual color perception, allowing visually impaired students to detect acid-base reactions."
            },
            {
                "question": "20. What color does methyl orange indicator turn in an acidic solution?",
                "options": [
                    "Red",
                    "Yellow",
                    "Green",
                    "Colorless"
                ],
                "correct": 0,
                "solution": "Methyl orange is red in acidic solutions ($\text{pH} < 3.1$) and turns yellow in neutral and basic solutions."
            }
        ]
    },

    # -------------------------------------------------------------
    # 19. Mastery Quiz 3: Neutralisation Chemistry (Questions 21 - 30)
    # -------------------------------------------------------------
    {
        "id": 19,
        "type": "quiz_slide",
        "title": "Mastery Challenge III: Neutralisation Reactions",
        "subtitle": "Test Your Mastery on Equations, Salts, Exothermic Heat, and Titration",
        "questions": [
            {
                "question": "21. What is the general word equation for any neutralisation reaction?",
                "options": [
                    "$\\text{Acid} + \\text{Base} \\rightarrow \\text{Salt} + \\text{Water} + \\text{Heat}$",
                    "$\\text{Acid} + \\text{Metal} \\rightarrow \\text{Hydrogen} + \\text{Heat}$",
                    "$\\text{Salt} + \\text{Water} \\rightarrow \\text{Acid} + \\text{Base}$",
                    "$\\text{Base} + \\text{Oxygen} \\rightarrow \\text{Carbon Dioxide}$"
                ],
                "correct": 0,
                "solution": "Neutralisation is the reaction of an acid and a base producing a salt and water, accompanied by the evolution of heat."
            },
            {
                "question": "22. Which salt is formed when hydrochloric acid ($\\text{HCl}$) reacts with sodium hydroxide ($\\text{NaOH}$)?",
                "options": [
                    "Sodium chloride [$\\text{NaCl}$]",
                    "Calcium carbonate [$\\text{CaCO}_3$]",
                    "Magnesium sulfate [$\\text{MgSO}_4$]",
                    "Sodium nitrate [$\\text{NaNO}_3$]"
                ],
                "correct": 0,
                "solution": "$\\text{HCl} + \\text{NaOH} \\rightarrow \\text{NaCl} + \\text{H}_2\\text{O}$. The salt formed is sodium chloride (common table salt)."
            },
            {
                "question": "23. Why is neutralisation classified as an 'exothermic' reaction?",
                "options": [
                    "Because heat energy is released, raising the temperature of the reaction mixture",
                    "Because it absorbs heat, causing water to freeze",
                    "Because it emits bright ultraviolet light",
                    "Because it produces sound waves"
                ],
                "correct": 0,
                "solution": "Exothermic reactions evolve heat into the surroundings; combining $\text{H}^+$ and $\text{OH}^-$ ions releases $57.3\text{ kJ/mol}$ of enthalpy."
            },
            {
                "question": "24. In an acid-base titration, what piece of laboratory glassware holds the base solution and dispenses it drop by drop?",
                "options": [
                    "A graduated Burette with a stopcock",
                    "A Petri dish",
                    "A microscope slide",
                    "A mortar and pestle"
                ],
                "correct": 0,
                "solution": "A burette is a long, graduated glass tube with a stopcock tap at the bottom used to deliver precise volumes in titrations."
            },
            {
                "question": "25. What is the fundamental ionic equation underlying all aqueous acid-base neutralisation reactions?",
                "options": [
                    "$\\text{H}^+\\text{(aq)} + \\text{OH}^-\\text{(aq)} \\rightarrow \\text{H}_2\\text{O(l)}$",
                    "$\\text{Na}^+ + \\text{Cl}^- \\rightarrow \\text{NaCl}$",
                    "$\\text{C} + \\text{O}_2 \\rightarrow \\text{CO}_2$",
                    "$\\text{Fe} + \\text{S} \\rightarrow \\text{FeS}$"
                ],
                "correct": 0,
                "solution": "The essence of neutralisation in water is the combination of hydrogen ions (from acid) and hydroxide ions (from base) to form neutral water molecules."
            },
            {
                "question": "26. When sulfuric acid ($\\text{H}_2\\text{SO}_4$) reacts with potassium hydroxide ($\\text{KOH}$), what salt is formed?",
                "options": [
                    "Potassium sulfate [$\\text{K}_2\\text{SO}_4$]",
                    "Potassium chloride [$\\text{KCl}$]",
                    "Sodium sulfate [$\\text{Na}_2\\text{SO}_4$]",
                    "Calcium sulfate [$\\text{CaSO}_4$]"
                ],
                "correct": 0,
                "solution": "$\\text{H}_2\\text{SO}_4 + 2\\text{KOH} \\rightarrow \\text{K}_2\\text{SO}_4 + 2\\text{H}_2\\text{O}$. The resulting salt is potassium sulfate."
            },
            {
                "question": "27. What happens to the pH of a hydrochloric acid solution as sodium hydroxide solution is gradually added to it?",
                "options": [
                    "The pH increases from strongly acidic towards 7.0 and beyond",
                    "The pH drops to negative values",
                    "The pH remains permanently at 1.0",
                    "The pH turns into zero"
                ],
                "correct": 0,
                "solution": "Adding base consumes hydrogen ions ($\text{H}^+$), causing the pH to rise toward the neutral point ($\text{pH} = 7$) and into the alkaline range."
            },
            {
                "question": "28. Can a salt formed by neutralisation be acidic, basic, or neutral?",
                "options": [
                    "Yes, depending on whether strong/weak acids react with strong/weak bases",
                    "No, all salts without exception are always acidic",
                    "No, all salts without exception are always basic",
                    "Salts do not have any pH"
                ],
                "correct": 0,
                "solution": "A strong acid + strong base yields a neutral salt ($\text{NaCl}$); a strong acid + weak base yields an acidic salt; a weak acid + strong base yields a basic salt."
            },
            {
                "question": "29. If equal volumes of $1\\text{ M } \\text{HCl}$ and $1\\text{ M } \\text{NaOH}$ are mixed, what will be the effect on red litmus paper?",
                "options": [
                    "No color change, because the resulting sodium chloride solution is neutral",
                    "It will turn bright blue",
                    "It will turn bright yellow",
                    "It will turn dark black"
                ],
                "correct": 0,
                "solution": "Equal molar amounts of strong acid and strong base fully neutralize to form neutral salt water ($\text{pH} = 7$), which leaves red litmus unchanged."
            },
            {
                "question": "30. Why must the conical flask be swirled continuously during a titration?",
                "options": [
                    "To ensure thorough mixing and immediate chemical neutralisation of the reactants",
                    "To cool down the glass so it doesn't melt",
                    "To generate static electricity",
                    "To create bubbles of air"
                ],
                "correct": 0,
                "solution": "Swirling ensures that the incoming drops of base are uniformly distributed throughout the acid solution, preventing localized concentration gradients."
            }
        ]
    },

    # -------------------------------------------------------------
    # 20. Mastery Quiz 4: Daily Life Applications & Pioneers (Questions 31 - 40)
    # -------------------------------------------------------------
    {
        "id": 20,
        "type": "quiz_slide",
        "title": "Mastery Challenge IV: Real-Life Applications & Pioneers",
        "subtitle": "Test Your Knowledge on Ant Bites, Soil, Industrial Effluents & P.C. Ray",
        "questions": [
            {
                "question": "31. An ant bite causes stinging pain due to the injection of which chemical?",
                "options": [
                    "Formic acid (methanoic acid)",
                    "Acetic acid",
                    "Sodium hydroxide",
                    "Nitric acid"
                ],
                "correct": 0,
                "solution": "Ants inject formic acid ($\text{HCOOH}$) under the skin, triggering nerve irritation, local swelling, and burning pain."
            },
            {
                "question": "32. What common household substance can be applied as a paste to relieve the pain of an ant bite?",
                "options": [
                    "Baking soda (sodium hydrogen carbonate) or calamine lotion",
                    "Lemon juice",
                    "Pure vinegar",
                    "Dilute hydrochloric acid"
                ],
                "correct": 0,
                "solution": "Baking soda and calamine contain mild bases that neutralize the injected formic acid into harmless formate salt and water."
            },
            {
                "question": "33. What chemical compound is present in calamine lotion that helps soothe acidic stings?",
                "options": [
                    "Zinc carbonate [$\\text{ZnCO}_3$]",
                    "Sulfuric acid [$\\text{H}_2\\text{SO}_4$]",
                    "Sodium chloride [$\\text{NaCl}$]",
                    "Copper sulfate [$\\text{CuSO}_4$]"
                ],
                "correct": 0,
                "solution": "Calamine lotion consists primarily of zinc oxide and zinc carbonate ($\text{ZnCO}_3$), a mild insoluble base that neutralizes acid on skin."
            },
            {
                "question": "34. How should excessively acidic agricultural soil be treated to restore fertility?",
                "options": [
                    "By adding quicklime (calcium oxide) or slaked lime (calcium hydroxide)",
                    "By pouring vinegar over the field",
                    "By adding more acidic fertilizers",
                    "By flooding the field with sea water"
                ],
                "correct": 0,
                "solution": "Quicklime ($\text{CaO}$) and slaked lime ($\text{Ca(OH)}_2$) are alkaline compounds that neutralize excessive soil acidity."
            },
            {
                "question": "35. If garden soil is too basic (alkaline), what should be added to correct its pH?",
                "options": [
                    "Decomposing organic matter (compost/manure)",
                    "More slaked lime",
                    "Washing soda powder",
                    "Pure chalk"
                ],
                "correct": 0,
                "solution": "Decomposing organic manure releases organic acids that naturally neutralize soil alkalinity, bringing the pH down to an optimal range."
            },
            {
                "question": "36. Why must acidic industrial effluents be neutralized before discharge into rivers?",
                "options": [
                    "To prevent acidic water from destroying fish gills, aquatic flora, and river ecology",
                    "To turn the river water into carbonated soda",
                    "To increase the salt concentration for ocean ships",
                    "To prevent rain clouds from forming"
                ],
                "correct": 0,
                "solution": "Untreated acidic factory wastes lower water pH, killing fish, disrupting aquatic food chains, and leaching heavy metals into drinking sources."
            },
            {
                "question": "37. What active ingredient in antacid tablets like 'Milk of Magnesia' relieves indigestion?",
                "options": [
                    "Magnesium hydroxide [$\\text{Mg(OH)}_2$]",
                    "Citric acid",
                    "Acetic acid",
                    "Potassium cyanide"
                ],
                "correct": 0,
                "solution": "Magnesium hydroxide is a safe, mild base that neutralizes excess hydrochloric acid in the stomach to form magnesium chloride and water."
            },
            {
                "question": "38. Why is commercial toothpaste formulated to be mildly alkaline?",
                "options": [
                    "To neutralize microbial acids produced in the mouth that erode tooth enamel",
                    "To bleach the teeth yellow",
                    "To feed bacteria between teeth",
                    "To dissolve the tongue's taste buds"
                ],
                "correct": 0,
                "solution": "Bacteria ferment oral sugars into acids that dissolve enamel ($\text{pH} < 5.5$). Alkaline toothpaste neutralizes these acids, preventing tooth decay."
            },
            {
                "question": "39. Who is reverently known as the 'Father of Modern Indian Chemistry'?",
                "options": [
                    "Acharya Prafulla Chandra Ray",
                    "Sir C.V. Raman",
                    "Dr. Homi J. Bhabha",
                    "Aryabhata"
                ],
                "correct": 0,
                "solution": "Acharya Prafulla Chandra Ray (1861–1944) established modern synthetic chemical research in India and founded Bengal Chemicals."
            },
            {
                "question": "40. In 1896, Acharya P.C. Ray achieved international fame by synthesizing which stable chemical compound?",
                "options": [
                    "Mercurous nitrite [$\\text{Hg}_2(\\text{NO}_2)_2$]",
                    "Aspirin",
                    "Polythene",
                    "Penicillin"
                ],
                "correct": 0,
                "solution": "Acharya P.C. Ray discovered and synthesized stable mercurous nitrite from mercury and dilute nitric acid in 1896."
            }
        ]
    }
]

with open(".agents/class7_science_substances_data.py", "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 7 Science Chapter 2: Exploring Substances: Acidic, Basic, and Neutral Data"""\n\n')
    f.write("SLIDES_DATA = " + json.dumps(SLIDES_DATA, indent=2, ensure_ascii=False) + "\n")

print(f"Generated .agents/class7_science_substances_data.py with {len(SLIDES_DATA)} slides.")

