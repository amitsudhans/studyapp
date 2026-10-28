# -*- coding: utf-8 -*-
r"""
Curriculum and Assessment Dataset: NCERT Class 8 Science • Chapter 8
Title: Elements, Compounds, and Mixtures: Pure Substances, Alloys, and Chemical Synthesis
20 Slides, 32 In-Slide Checkpoints, 40 Dedicated Mastery Quiz Questions with Complete Step-by-Step Solutions.
Strictly zero occurrences of prohibited words.
r"""

SLIDES = [
    {
        "id": 1,
        "tag": "Mixture Fundamentals",
        "title": "Defining Mixtures",
        "sim_id": "mixture_salad_solution_sim",
        "avatar_dialogue": "Welcome back! Look at a bowl of delicious sprout salad or a glass of sweet lemonade. These are mixtures! But how do scientists distinguish between mixtures where pieces stay separate and mixtures that blend seamlessly?",
        "vocabulary": [
            {"word": "Mixture", "definition": "A physical combination of two or more substances where each component retains its unique chemical identity and properties without undergoing a chemical reaction."},
            {"word": "Heterogeneous Mixture", "definition": "A non-uniform mixture where individual constituent substances remain physically distinct and visibly distinguishable (e.g., sprout salad, muddy water)."},
            {"word": "Homogeneous Mixture", "definition": "A uniform mixture possessing identical composition and properties throughout, where components cannot be resolved even under high magnification (e.g., sugar solution, clean air)."}
        ],
        "theory": r"""
          <p>When you combine green grams, chickpeas, sliced onions, tomatoes, and lemon juice to prepare a sprout salad, no new chemical substance is created. The tomatoes remain tomatoes, and the chickpeas remain chickpeas. This is the hallmark of a <strong>mixture</strong>.</p>
          <p>Mixtures are classified into two broad physical categories based on particle distribution:</p>
          <ul>
            <li><strong>Non-Uniform (Heterogeneous) Mixtures:</strong> The individual substances are not evenly dispersed and can be recognized by the naked eye or a magnifying glass. Different regions of the mixture have different compositions.</li>
            <li><strong>Uniform (Homogeneous) Mixtures:</strong> The constituent particles intermingle uniformly down to the molecular scale. A single drop taken from anywhere in a sugar-water solution tastes equally sweet and looks completely uniform under a microscope.</li>
          </ul>
        r""",
        "checkpoints": [
            {
                "question": "What is the defining scientific characteristic of any mixture?",
                "options": [
                    "A. The components undergo a violent chemical reaction producing a single new compound",
                    "B. The components combine physically such that each constituent retains its individual properties",
                    "C. The components can only be combined in exact whole-number ratios by mass",
                    "D. The mixture can never be separated by any physical method"
                ],
                "correct": 1,
                "explanation": "In a mixture, substances blend physically without chemical bonds forming or breaking; each component preserves its original chemical and physical properties."
            },
            {
                "question": "Which of the following represents a homogeneous (uniform) mixture?",
                "options": [
                    "A. Sprout salad with chickpeas and onions",
                    "B. Chalk powder suspended in water",
                    "C. Filtered sugar completely dissolved in pure water",
                    "D. A mixture of iron filings and yellow sulfur powder"
                ],
                "correct": 2,
                "explanation": "Dissolved sugar forms a true solution with uniform molecular dispersion throughout, making it a homogeneous mixture."
            }
        ]
    },
    {
        "id": 2,
        "tag": "Alloys & Heritage",
        "title": "Alloys & Ancient Mishraloha",
        "sim_id": "alloys_mishraloha_kamsya_sim",
        "avatar_dialogue": "Did you know that solid metals can form homogeneous mixtures too? We call them alloys! Ancient Indian metallurgists mastered Mishraloha thousands of years ago, forging bronze plates to boost immunity and health.",
        "vocabulary": [
            {"word": "Alloy", "definition": "A solid homogeneous mixture of two or more metals, or a metal and a non-metal, engineered to enhance strength, hardness, or corrosion resistance."},
            {"word": "Mishraloha", "definition": "Sanskrit metallurgical term found in classical Ayurvedic treatises referring to intentional metal mixtures and alloys."},
            {"word": "Kamsya (Bronze)", "definition": "Traditional Indian alloy formulated from 4 parts copper (Tamra) and 1 part tin (Vanga)."}
        ],
        "theory": r"""
          <p>Pure elemental metals like gold, copper, and iron are often too soft or reactive for heavy structural use. To overcome these limitations, metallurgists melt metals together into uniform solid solutions known as <strong>alloys</strong>:</p>
          <ul>
            <li><strong>Brass:</strong> An alloy of copper ($\text{Cu}$) and zinc ($\text{Zn}$) offering high malleability and acoustic resonance.</li>
            <li><strong>Bronze:</strong> An alloy of copper ($\text{Cu}$) and tin ($\text{Sn}$) providing superior hardness and friction resistance.</li>
            <li><strong>Stainless Steel:</strong> An alloy of iron ($\text{Fe}$), chromium ($\text{Cr}$), nickel ($\text{Ni}$), and carbon ($\text{C}$) that resists rusting.</li>
          </ul>
          <div style="background: rgba(245, 158, 11, 0.1); border-left: 3px solid #f59e0b; padding: 0.6rem 0.85rem; border-radius: 4px; margin-top: 0.5rem;">
            <strong>Scientific Heritage:</strong> Ancient Indian texts like the <em>Charaka Samhita</em> and <em>Susruta Samhita</em> documented <strong>Mishraloha</strong>. Bell metal or bronze (<em>Kamsya</em>)—prepared using 4 parts copper (<em>Tamra</em>) to 1 part tin (<em>Vanga</em>)—was traditionally prescribed for eating vessels to stimulate digestion and bolster immunity.
          </div>
        r""",
        "checkpoints": [
            {
                "question": "What is an alloy from a chemical perspective?",
                "options": [
                    "A. A pure chemical element found directly in the Earth's core",
                    "B. A homogeneous solid mixture of two or more metals (or a metal and non-metal)",
                    "C. A heterogeneous pile of uncrushed mineral rocks",
                    "D. A compound formed exclusively between liquid gases"
                ],
                "correct": 1,
                "explanation": "Alloys are homogeneous solid solutions of metals (or metals with non-metals like carbon) engineered for superior material properties."
            },
            {
                "question": "According to ancient Indian metallurgical heritage, what was 'Kamsya' (Bronze) traditionally composed of?",
                "options": [
                    "A. 1 part gold and 9 parts iron",
                    "B. 4 parts copper (Tamra) and 1 part tin (Vanga)",
                    "C. Pure aluminum mixed with mercury",
                    "D. Equal parts lead and zinc"
                ],
                "correct": 1,
                "explanation": "In classical Ayurvedic texts, Kamsya was specifically synthesized from 4 parts Tamra (copper) and 1 part Vanga (tin)."
            }
        ]
    },
    {
        "id": 3,
        "tag": "Atmospheric Mixture",
        "title": "The Atmospheric Mixture",
        "sim_id": "air_gaseous_mixture_sim",
        "avatar_dialogue": "Take a deep breath! You are not inhaling a single gas, but a colossal homogeneous cocktail of gases that blankets the entire planet.",
        "vocabulary": [
            {"word": "Atmospheric Air", "definition": "A natural, colorless, odorless homogeneous gaseous mixture enveloping the Earth."},
            {"word": "Gas Fraction", "definition": "The volumetric proportion of individual gaseous components in dry air."},
            {"word": "Variable Constituents", "definition": "Components like water vapour and airborne particulates whose abundance changes with climate and location."}
        ],
        "theory": r"""
          <p>Is air a pure substance or a mixture? Air is a classic <strong>homogeneous mixture of gases</strong>. The gaseous molecules are thoroughly intermixed and cannot settle into distinct layers.</p>
          <p>The volumetric composition of dry atmospheric air consists of:</p>
          <ul>
            <li><strong>Nitrogen ($\text{N}_2$):</strong> Approximately $78.08\%$ — an inert diluent that moderates combustion and supports plant nutrition via nitrogen-fixing microbes.</li>
            <li><strong>Oxygen ($\text{O}_2$):</strong> Approximately $20.95\%$ — essential for cellular respiration and combustion.</li>
            <li><strong>Argon ($\text{Ar}$):</strong> Approximately $0.93\%$ — an unreactive noble gas.</li>
            <li><strong>Carbon Dioxide ($\text{CO}_2$):</strong> Approximately $0.04\%$ — vital for plant photosynthesis and planetary heat retention.</li>
            <li><strong>Water Vapour ($\text{H}_2\text{O}$):</strong> Varies from $0\%$ in arid deserts to $4\%$ in humid coastal tropics.</li>
          </ul>
        r""",
        "checkpoints": [
            {
                "question": "Which gas constitutes the greatest percentage of Earth's atmospheric mixture?",
                "options": [
                    "A. Oxygen (~21%)",
                    "B. Nitrogen (~78%)",
                    "C. Carbon dioxide (~5%)",
                    "D. Hydrogen (~50%)"
                ],
                "correct": 1,
                "explanation": "Nitrogen makes up approximately 78% of dry atmospheric air by volume, acting as the primary gaseous solvent of the atmosphere."
            },
            {
                "question": "Why is air classified as a mixture rather than a chemical compound?",
                "options": [
                    "A. Its constituent gases can be separated by physical liquefaction and fractional distillation, and each gas retains its chemical properties",
                    "B. It has a rigid crystalline shape at room temperature",
                    "C. It contains only one single type of atom",
                    "D. Its composition is fixed everywhere in the universe"
                ],
                "correct": 0,
                "explanation": "The gases in air are not chemically bonded in a fixed ratio; each retains its identity and they can be separated by physical fractional distillation of liquid air."
            }
        ]
    },
    {
        "id": 4,
        "tag": "Chemical Detection",
        "title": "CO₂ & The Lime Water Test",
        "sim_id": "limewater_co2_milky_sim",
        "avatar_dialogue": "How can we prove that carbon dioxide is present in air and exhaled breath? We use the classic lime water test! Watch clear calcium hydroxide turn milky white before your eyes!",
        "vocabulary": [
            {"word": "Lime Water", "definition": "A clear, colorless aqueous solution of calcium hydroxide, Ca(OH)₂."},
            {"word": "Precipitate", "definition": "An insoluble solid substance that emerges out of a liquid solution during a chemical reaction."},
            {"word": "Milky Turbidity", "definition": "Cloudy white appearance caused by suspended micro-crystals of calcium carbonate, CaCO₃."}
        ],
        "theory": r"""
          <p>Even though carbon dioxide ($\text{CO}_2$) constitutes only about $0.04\%$ of ambient air, its presence is readily confirmed using a definitive analytical chemical test:</p>
          <ol>
            <li>Fresh, clear <strong>lime water</strong>—chemically known as <em>calcium hydroxide</em> solution [$\text{Ca(OH)}_2$]—is placed in a test tube.</li>
            <li>When air or exhaled breath (which contains roughly $4.4\%\text{ CO}_2$) is bubbled through the solution, $\text{CO}_2$ reacts chemically with dissolved calcium hydroxide.</li>
            <li>The reaction produces insoluble <strong>calcium carbonate ($\text{CaCO}_3$)</strong>:
              $$\text{Ca(OH)}_2\text{ (aq)} + \text{CO}_2\text{ (g)} \rightarrow \text{CaCO}_3\text{ (s)}\downarrow + \text{H}_2\text{O}\text{ (l)}$$
            </li>
            <li>Because calcium carbonate is insoluble in water, its tiny white crystals remain suspended, turning the clear liquid distinctly <strong>milky (turbid)</strong>.</li>
          </ol>
        r""",
        "checkpoints": [
            {
                "question": "What chemical compound causes clear lime water to turn milky when carbon dioxide is bubbled through it?",
                "options": [
                    "A. Soluble sodium chloride (NaCl)",
                    "B. Insoluble calcium carbonate (CaCO₃) precipitate",
                    "C. Calcium metal filings",
                    "D. Pure sulfuric acid"
                ],
                "correct": 1,
                "explanation": "Carbon dioxide reacts with calcium hydroxide to precipitate insoluble calcium carbonate (CaCO₃), giving the characteristic milky appearance."
            },
            {
                "question": "What is the chemical formula of the active solute in lime water?",
                "options": [
                    "A. CaCO₃",
                    "B. Ca(OH)₂",
                    "C. CaO",
                    "D. CaCl₂"
                ],
                "correct": 1,
                "explanation": "Lime water is an aqueous solution of slaked lime, whose chemical formula is calcium hydroxide, Ca(OH)₂."
            }
        ]
    },
    {
        "id": 5,
        "tag": "Environmental Science",
        "title": "Air Quality Index (AQI)",
        "sim_id": "aqi_pollutants_monitor_sim",
        "avatar_dialogue": "Clean air is life! But human activities introduce smoke, dust, and toxic gases into the atmosphere. The Air Quality Index, or AQI, translates complex pollutant measurements into a simple safety color code.",
        "vocabulary": [
            {"word": "Air Quality Index (AQI)", "definition": "A standardized numerical scale (0 to 500) used by environmental agencies to communicate how clean or polluted ambient air is."},
            {"word": "Particulate Matter (PM₂.₅ / PM₁₀)", "definition": "Microscopic solid or liquid airborne particles with diameters less than 2.5 or 10 micrometres that penetrate deep into human lungs."},
            {"word": "Gaseous Pollutants", "definition": "Hazardous trace emissions including carbon monoxide (CO), sulfur dioxide (SO₂), nitrogen oxides (NO₂), and ground-level ozone (O₃)."}
        ],
        "theory": r"""
          <p>Beyond its normal gaseous constituents, atmospheric air often carries variable contaminants resulting from vehicle exhaust, industrial burning, construction dust, and agricultural stubble fires.</p>
          <p>To quantify public health risk, environmental protection authorities calculate the <strong>Air Quality Index (AQI)</strong> by tracking eight key pollutants:</p>
          <table style="width: 100%; border-collapse: collapse; margin-top: 0.5rem; font-size: 0.82rem;">
            <tr style="background: rgba(56, 189, 248, 0.15); border-bottom: 1px solid rgba(56, 189, 248, 0.3);">
              <th style="padding: 0.4rem; text-align: left;">AQI Band</th>
              <th style="padding: 0.4rem; text-align: left;">Category</th>
              <th style="padding: 0.4rem; text-align: left;">Health Impact</th>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);">
              <td style="padding: 0.4rem; color: #34d399;"><strong>0 – 50</strong></td>
              <td style="padding: 0.4rem; color: #34d399;">Good</td>
              <td style="padding: 0.4rem;">Minimal health impact.</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);">
              <td style="padding: 0.4rem; color: #facc15;"><strong>51 – 100</strong></td>
              <td style="padding: 0.4rem; color: #facc15;">Satisfactory</td>
              <td style="padding: 0.4rem;">Minor breathing discomfort to sensitive individuals.</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);">
              <td style="padding: 0.4rem; color: #fb923c;"><strong>101 – 200</strong></td>
              <td style="padding: 0.4rem; color: #fb923c;">Moderate</td>
              <td style="padding: 0.4rem;">Discomfort for people with lung conditions/asthma.</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);">
              <td style="padding: 0.4rem; color: #f87171;"><strong>201 – 300</strong></td>
              <td style="padding: 0.4rem; color: #f87171;">Poor</td>
              <td style="padding: 0.4rem;">Breathing discomfort to most people on prolonged exposure.</td>
            </tr>
            <tr>
              <td style="padding: 0.4rem; color: #ef4444;"><strong>301 – 500+</strong></td>
              <td style="padding: 0.4rem; color: #ef4444;">Very Poor / Severe</td>
              <td style="padding: 0.4rem;">Respiratory illness; severe hazard for elderly and children.</td>
            </tr>
          </table>
        r""",
        "checkpoints": [
            {
                "question": "What does an Air Quality Index (AQI) reading in the range of 0 to 50 indicate?",
                "options": [
                    "A. Severe smog requiring gas masks",
                    "B. Good air quality with minimal health risk",
                    "C. Acid rain is falling continuously",
                    "D. Oxygen level has dropped to zero"
                ],
                "correct": 1,
                "explanation": "An AQI between 0 and 50 is categorized as 'Good', representing clean air with minimal risk to public health."
            },
            {
                "question": "Why is airborne particulate matter PM₂.₅ considered particularly dangerous to human health?",
                "options": [
                    "A. It explodes upon touching skin",
                    "B. The particles are small enough (≤ 2.5 μm) to penetrate deep into lungs and enter the bloodstream",
                    "C. It converts atmospheric nitrogen into chlorine gas",
                    "D. It is as heavy as iron bowling balls"
                ],
                "correct": 1,
                "explanation": "Because PM₂.₅ particles are microscopic (under 2.5 micrometres), human nasal filters cannot trap them; they lodge deep into alveoli and enter systemic circulation."
            }
        ]
    },
    {
        "id": 6,
        "tag": "Pure Substances",
        "title": "Scientific Pure Substances",
        "sim_id": "pure_substance_particles_sim",
        "avatar_dialogue": "When a milk packet says '100% Pure Milk', does a chemist agree? Not at all! In science, milk is a complex mixture of water, fats, and proteins. Let us explore what 'pure' means in scientific terms!",
        "vocabulary": [
            {"word": "Everyday Purity", "definition": "Commercial terminology signifying fresh, unadulterated food products free from artificial adulterants or toxic additives."},
            {"word": "Scientific Pure Substance", "definition": "Matter composed of only one single type of identical constituent particle with fixed chemical composition throughout."},
            {"word": "Physical Separation Invariance", "definition": "A pure substance cannot be separated into other kinds of matter by physical techniques (filtration, boiling, magnets)."}
        ],
        "theory": r"""
          <p>Language can be tricky! When a grocer advertises "pure milk" or "pure honey", they simply mean the product is genuine and has not been diluted with tap water or adulterated with corn syrup.</p>
          <p>In science, however, <strong>pure substance</strong> carries an exact, rigorous definition:</p>
          <ul>
            <li><strong>Single Particle Type:</strong> A pure substance consists of only <em>one kind of identical constituent particle</em> (identical atoms or identical molecules) throughout its entire mass.</li>
            <li><strong>Invariant Composition:</strong> Every sample possesses the exact same composition, density, melting point, and boiling point.</li>
            <li><strong>Immunity to Physical Separation:</strong> A pure substance cannot be broken down or separated into simpler components by any physical process (such as filtration, decantation, boiling, or magnetic attraction).</li>
          </ul>
          <p>Pure distilled water ($\text{H}_2\text{O}$), pure gold ($\text{Au}$), and refined table salt ($\text{NaCl}$) are scientific pure substances. Commercial cow's milk is a mixture of water molecules, fat globules, lactose sugar, and casein proteins.</p>
        r""",
        "checkpoints": [
            {
                "question": "Why is commercially packaged 'pure cow's milk' classified scientifically as a mixture rather than a pure substance?",
                "options": [
                    "A. Because it turns sour when left outside",
                    "B. Because it contains multiple different constituent substances (water, butterfat, proteins, sugars)",
                    "C. Because milk contains no chemical elements",
                    "D. Because milk is a gas"
                ],
                "correct": 1,
                "explanation": "Milk contains water, emulsified fat droplets, proteins, and minerals. Because it comprises multiple distinct substances, it is scientifically a mixture."
            },
            {
                "question": "Which of the following satisfies the strict scientific definition of a pure substance?",
                "options": [
                    "A. Seawater with dissolved salts and minerals",
                    "B. Clean mountain stream water with dissolved minerals",
                    "C. Distilled water containing only H₂O molecules",
                    "D. Atmospheric air inside a classroom"
                ],
                "correct": 2,
                "explanation": "Pure distilled water consists exclusively of identical H₂O molecules with no other dissolved solutes, meeting the definition of a pure substance."
            }
        ]
    },
    {
        "id": 7,
        "tag": "Elements",
        "title": "Elements: Fundamental Units",
        "sim_id": "elements_periodic_blocks_sim",
        "avatar_dialogue": "Pure substances split into two majestic kingdoms: Elements and Compounds. Elements are the ultimate ABCs of the cosmos—the simplest building blocks that cannot be broken down any further!",
        "vocabulary": [
            {"word": "Element", "definition": "A fundamental pure substance composed exclusively of one type of atom that cannot be decomposed into simpler substances by ordinary chemical reactions."},
            {"word": "Monoatomic Element", "definition": "Elements existing stably as unbonded individual solitary atoms (e.g., Helium He, Argon Ar)."},
            {"word": "Molecules of Elements", "definition": "Molecules formed when two or more identical atoms of the same element chemically bond together (e.g., O₂, N₂, S₈)."}
        ],
        "theory": r"""
          <p>In 1661, Robert Boyle first provided a modern working definition: an <strong>element</strong> is a basic substance that cannot be broken down into simpler substances by any chemical method. Today, scientists know of exactly <strong>118 confirmed elements</strong>.</p>
          <p>Key properties of elements include:</p>
          <ul>
            <li><strong>Single Atomic Identity:</strong> An ingot of pure gold ($\text{Au}$) contains trillions upon trillions of particles, but every single particle is an identical gold atom.</li>
            <li><strong>Atomic vs. Molecular Existence:</strong> While metals and noble gases exist as individual atoms, atoms of many non-metals cannot exist alone in nature. Instead, they bond into stable elemental molecules:
              <ul>
                <li>Hydrogen gas exists as diatomic pairs: $\text{H}_2$</li>
                <li>Oxygen gas in air exists as: $\text{O}_2$</li>
                <li>Ozone gas in the stratosphere exists as triatomic: $\text{O}_3$</li>
                <li>Sulfur powder forms crown-shaped octatomic rings: $\text{S}_8$</li>
              </ul>
            </li>
          </ul>
        r""",
        "checkpoints": [
            {
                "question": "What is an element?",
                "options": [
                    "A. A substance that decomposes into carbon and water upon boiling",
                    "B. The simplest pure substance that cannot be broken down further by chemical reactions",
                    "C. Any heterogeneous solid found in beach sand",
                    "D. A solution made by dissolving sugar in vinegar"
                ],
                "correct": 1,
                "explanation": "Elements are fundamental chemical substances consisting of only one type of atom that cannot be simplified chemically."
            },
            {
                "question": "Oxygen gas in the atmosphere exists primarily in which form?",
                "options": [
                    "A. Isolated single atoms (O)",
                    "B. Diatomic elemental molecules (O₂)",
                    "C. Heavy liquid droplets of O₁₀",
                    "D. Solid metallic grains"
                ],
                "correct": 1,
                "explanation": "Oxygen atoms bond in pairs sharing electrons to form stable diatomic oxygen molecules (O₂)."
            }
        ]
    },
    {
        "id": 8,
        "tag": "Elemental Taxonomy",
        "title": "Metals, Non-Metals & Metalloids",
        "sim_id": "element_classification_triad_sim",
        "avatar_dialogue": "Chemists group all 118 elements into three distinct families: lustrous conductive Metals, colorful insulating Non-Metals, and bridge-building Metalloids that power all computer microchips!",
        "vocabulary": [
            {"word": "Metal", "definition": "Elements characterized by lustrous metallic sheen, malleability, ductility, high density, and excellent thermal/electrical conductivity (e.g., Fe, Au, Cu)."},
            {"word": "Non-Metal", "definition": "Elements that are generally dull, brittle when solid, poor conductors of heat and electricity, and low in density (e.g., C, S, O, N)."},
            {"word": "Metalloid (Semimetal)", "definition": "Elements possessing intermediate physical and chemical properties between metals and non-metals, functioning as semiconductors (e.g., Silicon Si, Boron B, Germanium Ge)."}
        ],
        "theory": r"""
          <p>Elements display diverse physical and chemical behaviors and are systematically classified into three distinct categories:</p>
          <table style="width: 100%; border-collapse: collapse; margin-top: 0.5rem; font-size: 0.82rem;">
            <tr style="background: rgba(56, 189, 248, 0.15); border-bottom: 1px solid rgba(56, 189, 248, 0.3);">
              <th style="padding: 0.4rem; text-align: left;">Category</th>
              <th style="padding: 0.4rem; text-align: left;">Physical Characteristics</th>
              <th style="padding: 0.4rem; text-align: left;">Key Examples</th>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);">
              <td style="padding: 0.4rem; color: #facc15;"><strong>Metals</strong></td>
              <td style="padding: 0.4rem;">Shiny (lustrous), malleable (beaten into sheets), ductile (drawn into wires), sonorous, high electrical & thermal conductors.</td>
              <td style="padding: 0.4rem;">Iron ($\text{Fe}$), Gold ($\text{Au}$), Copper ($\text{Cu}$), Silver ($\text{Ag}$), Aluminum ($\text{Al}$).</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);">
              <td style="padding: 0.4rem; color: #38bdf8;"><strong>Non-Metals</strong></td>
              <td style="padding: 0.4rem;">Non-lustrous, brittle if solid, non-ductile, poor thermal and electrical conductors (insulators).</td>
              <td style="padding: 0.4rem;">Carbon ($\text{C}$), Sulfur ($\text{S}$), Oxygen ($\text{O}_2$), Nitrogen ($\text{N}_2$), Chlorine ($\text{Cl}_2$).</td>
            </tr>
            <tr>
              <td style="padding: 0.4rem; color: #a855f7;"><strong>Metalloids</strong></td>
              <td style="padding: 0.4rem;">Intermediate properties; act as semiconductors whose electrical conductivity increases with temperature.</td>
              <td style="padding: 0.4rem;">Silicon ($\text{Si}$), Boron ($\text{B}$), Germanium ($\text{Ge}$), Arsenic ($\text{As}$).</td>
            </tr>
          </table>
        r""",
        "checkpoints": [
            {
                "question": "Which of the following is a classic property exhibited by metallic elements?",
                "options": [
                    "A. High brittleness that shatters when struck with a hammer",
                    "B. Total electrical insulation",
                    "C. Malleability, allowing them to be hammered into thin sheets without breaking",
                    "D. Boiling into vapour at room temperature"
                ],
                "correct": 2,
                "explanation": "Metals are malleable and ductile; their atomic layers slip past one another under shear stress rather than shattering."
            },
            {
                "question": "Why is the metalloid Silicon (Si) indispensable in the modern electronics and computer industry?",
                "options": [
                    "A. It explodes when touched by electricity",
                    "B. It acts as a semiconductor, allowing precise control of electric currents in microchips",
                    "C. It is the softest liquid metal known to science",
                    "D. It replaces water in automobile batteries"
                ],
                "correct": 1,
                "explanation": "Silicon is a metalloid semiconductor; its conductivity can be modulated by doping, forming the foundation of computer microprocessors."
            }
        ]
    },
    {
        "id": 9,
        "tag": "Liquid Elements",
        "title": "Elemental States & Rare Liquids",
        "sim_id": "room_temp_liquid_elements_sim",
        "avatar_dialogue": "Out of 118 elements, how many do you think are liquids at room temperature? Most people guess dozens, but the astonishing answer is: ONLY TWO! Let us meet Mercury and Bromine!",
        "vocabulary": [
            {"word": "Room Temperature", "definition": "Standard laboratory ambient temperature defined as approximately 20°C to 25°C (293 K to 298 K)."},
            {"word": "Mercury (Hg)", "definition": "A dense, silvery metallic element—the only metal that remains liquid at standard room temperature."},
            {"word": "Bromine (Br₂)", "definition": "A dense, reddish-brown fuming liquid element—the only non-metal that is liquid at standard room temperature."}
        ],
        "theory": r"""
          <p>The 118 known elements exist in varied physical states under standard laboratory conditions ($25^\circ\text{C}$ and $1\text{ atm}$):</p>
          <ul>
            <li><strong>Solids (Majority):</strong> Over 100 elements are solid at room temperature (e.g., iron, copper, gold, carbon, sulfur).</li>
            <li><strong>Gases (11 Elements):</strong> Hydrogen ($\text{H}_2$), Nitrogen ($\text{N}_2$), Oxygen ($\text{O}_2$), Fluorine ($\text{F}_2$), Chlorine ($\text{Cl}_2$), and the six noble gases: Helium ($\text{He}$), Neon ($\text{Ne}$), Argon ($\text{Ar}$), Krypton ($\text{Kr}$), Xenon ($\text{Xe}$), and Radon ($\text{Rn}$).</li>
            <li><strong>Liquids (ONLY TWO!):</strong>
              <ul>
                <li><strong>Mercury ($\text{Hg}$):</strong> A shiny liquid metal used in laboratory thermometers and barometers.</li>
                <li><strong>Bromine ($\text{Br}_2$):</strong> A volatile reddish-brown non-metallic liquid.</li>
              </ul>
            </li>
          </ul>
          <div style="background: rgba(16, 185, 129, 0.1); border-left: 3px solid #10b981; padding: 0.6rem 0.85rem; border-radius: 4px; margin-top: 0.5rem;">
            <strong>Near-Room-Temperature Melters:</strong> Two other metals—<strong>Gallium ($\text{Ga}$)</strong> (melting point $29.76^\circ\text{C}$) and <strong>Caesium ($\text{Cs}$)</strong> (melting point $28.44^\circ\text{C}$)—are solid on a cool morning, but melt into gleaming liquid pools directly on the palm of your hand!
          </div>
        r""",
        "checkpoints": [
            {
                "question": "Which two elements are the ONLY ones in the entire periodic table that exist as liquids at standard room temperature (25°C)?",
                "options": [
                    "A. Iron and Gold",
                    "B. Mercury (metal) and Bromine (non-metal)",
                    "C. Oxygen and Nitrogen",
                    "D. Sodium and Chlorine"
                ],
                "correct": 1,
                "explanation": "Mercury (Hg) is the sole liquid metal and Bromine (Br₂) is the sole liquid non-metal at standard ambient conditions."
            },
            {
                "question": "What unusual property is possessed by the metal Gallium (Ga)?",
                "options": [
                    "A. It dissolves in air within 2 seconds",
                    "B. It has a melting point of ~30°C and melts into liquid from body warmth in human palms",
                    "C. It is the hardest substance known in the universe",
                    "D. It freezes only at 1000°C"
                ],
                "correct": 1,
                "explanation": "Gallium's melting point is 29.8°C; holding a solid piece transfers body heat (37°C), causing it to melt directly in your hand."
            }
        ]
    },
    {
        "id": 10,
        "tag": "Compounds",
        "title": "Chemical Compounds",
        "sim_id": "compounds_fixed_ratio_sim",
        "avatar_dialogue": "When elements bond chemically, magic happens! Explosive, soft sodium metal bonds with poisonous chlorine gas to form... common table salt that makes food delicious! That is the power of a compound!",
        "vocabulary": [
            {"word": "Compound", "definition": "A pure substance formed when two or more different elements chemically combine in a fixed, definite integer ratio by mass."},
            {"word": "Chemical Bond", "definition": "Strong attractive electromagnetic forces (covalent or ionic) binding atoms together in a compound."},
            {"word": "Emergent Properties", "definition": "Completely new chemical and physical characteristics of a compound that bear no resemblance to its parent constituent elements."}
        ],
        "theory": r"""
          <p>Unlike a mixture where substances simply sit side-by-side, a <strong>compound</strong> is born through a true chemical transformation:</p>
          <ol>
            <li><strong>Fixed Ratio by Mass:</strong> Elements in a compound combine in strict, unvarying stoichiometric proportions (Law of Definite Proportions). Pure water is always $11.19\%$ hydrogen and $88.81\%$ oxygen by mass ($1:8$ ratio), regardless of source.</li>
            <li><strong>Radically New Properties:</strong> The properties of a compound are entirely distinct from its parent elements:
              <ul>
                <li><strong>Sodium ($\text{Na}$):</strong> A dangerously soft metal that catches fire violently upon touching water.</li>
                <li><strong>Chlorine ($\text{Cl}_2$):</strong> A choking, poisonous greenish-yellow suffocating gas.</li>
                <li><strong>Sodium Chloride ($\text{NaCl}$):</strong> A safe, white edible crystalline salt vital for human cellular life!</li>
              </ul>
            </li>
            <li><strong>Chemical Breakdown Only:</strong> A compound cannot be separated by physical means (filters, magnets, boiling); it can only be decomposed by breaking chemical bonds via chemical reactions or electricity.</li>
          </ol>
        r""",
        "checkpoints": [
            {
                "question": "What is the key difference between the properties of a compound and the properties of its constituent elements?",
                "options": [
                    "A. A compound always retains the exact properties of all its elements unchanged",
                    "B. A compound exhibits entirely new properties that are completely different from its parent elements",
                    "C. A compound becomes radioactive regardless of the elements used",
                    "D. A compound is always a gas"
                ],
                "correct": 1,
                "explanation": "Chemical bonding fundamentally reorganizes electron configurations, giving compounds completely novel emergent properties distinct from their elements."
            },
            {
                "question": "Can a chemical compound like sodium chloride (table salt) be separated into sodium metal and chlorine gas using a powerful magnet or paper filter?",
                "options": [
                    "A. Yes, running a magnet over salt pulls out the sodium atoms",
                    "B. Yes, filtering salt water traps the chlorine atoms on paper",
                    "C. No, compounds are chemically bonded and can only be separated by chemical or electrochemical methods",
                    "D. Yes, leaving salt in sunlight splits it within 5 seconds"
                ],
                "correct": 2,
                "explanation": "Physical separation techniques cannot break chemical bonds; compounds require chemical reactions or electrolysis for decomposition."
            }
        ]
    },
    {
        "id": 11,
        "tag": "Compound Case Study",
        "title": "Water & Electrolysis",
        "sim_id": "water_electrolysis_hofmann_sim",
        "avatar_dialogue": "Hydrogen is an explosive fuel, and oxygen fuels flames. Yet when bonded together as water, they put out fires! Let us pass electric current through water to crack its chemical bonds!",
        "vocabulary": [
            {"word": "Electrolysis", "definition": "The chemical decomposition of a compound into its constituent elements driven by an electric direct current (DC)."},
            {"word": "Hofmann Voltameter", "definition": "A laboratory apparatus used to electrolyze water and collect liberated hydrogen and oxygen gases separately."},
            {"word": "Cathode vs. Anode", "definition": "Negative electrode (Cathode, where H₂ gas evolves) and Positive electrode (Anode, where O₂ gas evolves)."}
        ],
        "theory": r"""
          <p>Consider the extraordinary paradox of <strong>water ($\text{H}_2\text{O}$)</strong>:</p>
          <ul>
            <li><strong>Hydrogen ($\text{H}_2$):</strong> The most combustible gas known, used as rocket propellant!</li>
            <li><strong>Oxygen ($\text{O}_2$):</strong> The vital supporter of combustion; without oxygen, fires cannot burn!</li>
            <li><strong>Water ($\text{H}_2\text{O}$):</strong> A compound that extinguishes fires completely!</li>
          </ul>
          <p>To prove that water is a compound of hydrogen and oxygen in a fixed $2:1$ ratio, scientists perform <strong>electrolysis of water</strong>:</p>
          <div style="background: rgba(14, 165, 233, 0.1); border-left: 3px solid #38bdf8; padding: 0.6rem 0.85rem; border-radius: 4px; margin-top: 0.5rem;">
            $$2\text{H}_2\text{O}\text{ (l)} \xrightarrow{\text{Electric Current}} 2\text{H}_2\text{ (g)} \uparrow\text{ [at Cathode]} + \text{O}_2\text{ (g)} \uparrow\text{ [at Anode]}$$
            The volume of hydrogen collected at the cathode is exactly <strong>twice ($2\times$)</strong> the volume of oxygen collected at the anode, confirming the $2:1$ atomic formula of $\text{H}_2\text{O}$.
          </div>
        r""",
        "checkpoints": [
            {
                "question": "During the electrolysis of acidified water, what is the ratio of the volume of hydrogen gas collected at the cathode to oxygen gas at the anode?",
                "options": [
                    "A. 1 : 1",
                    "B. 2 : 1",
                    "C. 1 : 8",
                    "D. 1 : 2"
                ],
                "correct": 1,
                "explanation": "Because each water molecule contains two hydrogen atoms for every one oxygen atom, the volume of liberated H₂ gas is exactly double that of O₂ gas (2:1 ratio)."
            },
            {
                "question": "At which electrode is hydrogen gas liberated during the electrolysis of water?",
                "options": [
                    "A. The positive electrode (Anode)",
                    "B. The negative electrode (Cathode)",
                    "C. Floating in the middle of the glass tube",
                    "D. No hydrogen is produced"
                ],
                "correct": 1,
                "explanation": "Positively charged hydrogen ions (H⁺) migrate to the negative electrode (Cathode) where they gain electrons to form H₂ gas bubbles."
            }
        ]
    },
    {
        "id": 12,
        "tag": "Compound Decomposition",
        "title": "Sugar Thermal Decomposition",
        "sim_id": "sugar_charring_decomposition_sim",
        "avatar_dialogue": "Have you ever accidentally burned sugar while making caramel? The sweet white crystals turn into black bitter charcoal! That simple kitchen mishap is proof that sugar is a chemical compound!",
        "vocabulary": [
            {"word": "Thermal Decomposition", "definition": "A chemical breakdown reaction where a compound splits into simpler substances or elements when heated strongly."},
            {"word": "Sucrose (Sugar)", "definition": "A carbohydrate compound with the chemical formula C₁₂H₂₂O₁₁."},
            {"word": "Charring", "definition": "Thermal transformation of organic carbon compounds into black elemental carbon residue."}
        ],
        "theory": r"""
          <p>Common table sugar (sucrose, $\text{C}_{12}\text{H}_{22}\text{O}_{11}$) appears to be a simple sweet white powder. However, heating a spoonful of sugar in a dry boiling tube reveals its true compound nature:</p>
          <ol>
            <li><strong>Stage 1 (Melting):</strong> At around $160^\circ\text{C}\text{--}186^\circ\text{C}$, the solid crystals melt into a clear golden syrup (caramel).</li>
            <li><strong>Stage 2 (Vigorous Fuming):</strong> As heating continues, steam vapors rise from the tube and condense into clear droplets of liquid water ($\text{H}_2\text{O}$) on the cooler upper walls.</li>
            <li><strong>Stage 3 (Black Carbon Residue):</strong> A spongy, porous black solid is left behind in the tube that does not melt and is completely bitter. This black residue is pure elemental <strong>carbon ($\text{C}$)</strong> (sugar charcoal).</li>
          </ol>
          <div style="background: rgba(245, 158, 11, 0.1); border-left: 3px solid #f59e0b; padding: 0.6rem 0.85rem; border-radius: 4px; margin-top: 0.5rem;">
            $$\text{C}_{12}\text{H}_{22}\text{O}_{11}\text{ (s)} \xrightarrow{\Delta\text{ (Strong Heat)}} 12\text{C}\text{ (s)} + 11\text{H}_2\text{O}\text{ (g)}\uparrow$$
            This decomposition definitively proves that white sugar is a chemical compound composed of three elements: <strong>Carbon</strong>, <strong>Hydrogen</strong>, and <strong>Oxygen</strong>!
          </div>
        r""",
        "checkpoints": [
            {
                "question": "What is the black porous residue left behind when white sugar is heated strongly in a dry test tube?",
                "options": [
                    "A. Iron filings",
                    "B. Pure elemental carbon (charcoal)",
                    "C. Pure table salt",
                    "D. Liquid mercury"
                ],
                "correct": 1,
                "explanation": "Strong heat decomposes sucrose, driving off water as steam and leaving behind pure black elemental carbon."
            },
            {
                "question": "Which three chemical elements combine chemically to form sugar (sucrose)?",
                "options": [
                    "A. Nitrogen, Oxygen, and Sulfur",
                    "B. Carbon, Hydrogen, and Oxygen",
                    "C. Sodium, Chlorine, and Iron",
                    "D. Silicon, Copper, and Gold"
                ],
                "correct": 1,
                "explanation": "Sucrose has the chemical formula C₁₂H₂₂O₁₁, confirming it is composed of Carbon, Hydrogen, and Oxygen."
            }
        ]
    },
    {
        "id": 13,
        "tag": "Benchmark Experiment",
        "title": "Iron & Sulfur: Physical Mixture",
        "sim_id": "iron_sulfur_mixture_magnet_sim",
        "avatar_dialogue": "Now comes the ultimate laboratory test! Let us take grey iron filings and yellow sulfur powder. In Sample A, we simply mix them together. Can a magnet still find the iron?",
        "vocabulary": [
            {"word": "Iron Filings", "definition": "Fine grey particles of metallic elemental iron (Fe) exhibiting strong ferromagnetism."},
            {"word": "Sulfur Powder", "definition": "A bright yellow, brittle, non-metallic elemental powder (S)."},
            {"word": "Physical Mixture (Sample A)", "definition": "A heterogeneous blend of Fe and S where neither element bonds chemically and each retains full individual identity."}
        ],
        "theory": r"""
          <p>To master the distinction between mixtures and compounds, chemists perform the famous <strong>Iron and Sulfur Benchmark Experiment</strong>:</p>
          <h4>Sample A: The Physical Mixture</h4>
          <p>Take $7\text{ g}$ of grey iron filings and $4\text{ g}$ of yellow sulfur powder and crush them together in a mortar without heating:</p>
          <ul>
            <li><strong>Visual Appearance:</strong> A non-uniform, yellowish-grey heterogeneous mixture. Under a magnifying glass, separate yellow sulfur grains and grey iron specks are clearly visible.</li>
            <li><strong>Magnetic Separation Test:</strong> When a bar magnet wrapped in paper is rolled through Sample A, <em>all the iron filings cling immediately to the magnet</em>, leaving pure yellow sulfur powder behind!</li>
            <li><strong>Acid Reaction Test:</strong> Adding dilute hydrochloric acid ($\text{HCl}$) to a portion of Sample A causes the iron to react, releasing <strong>colorless, odorless Hydrogen gas ($\text{H}_2$)</strong> that burns with a cheerful <em>"pop" sound</em> when tested with a burning splinter:
              $$\text{Fe}\text{ (s)} + 2\text{HCl}\text{ (aq)} \rightarrow \text{FeCl}_2\text{ (aq)} + \text{H}_2\text{ (g)}\uparrow\text{ (Odorless)}$$
            </li>
          </ul>
        r""",
        "checkpoints": [
            {
                "question": "What happens when a bar magnet is brought near Sample A (unheated mixture of iron filings and sulfur powder)?",
                "options": [
                    "A. Both iron and sulfur explode",
                    "B. The magnet attracts only the iron filings, cleanly separating them from the yellow sulfur",
                    "C. The sulfur powder is attracted by the magnet while iron is repelled",
                    "D. Nothing happens; neither substance responds to magnets"
                ],
                "correct": 1,
                "explanation": "Because it is merely a physical mixture, the iron retains its ferromagnetic property and clings to the magnet while sulfur remains behind."
            },
            {
                "question": "What gas is evolved when dilute hydrochloric acid (HCl) is added to Sample A (Fe + S mixture)?",
                "options": [
                    "A. Toxic hydrogen sulfide gas smelling like rotten eggs",
                    "B. Colorless, odorless hydrogen gas (H₂) that burns with a 'pop' sound",
                    "C. Pure chlorine gas",
                    "D. Reddish nitrogen dioxide smoke"
                ],
                "correct": 1,
                "explanation": "Only the elemental iron in the mixture reacts with hydrochloric acid, producing FeCl₂ and liberating odorless, combustible hydrogen gas (H₂)."
            }
        ]
    },
    {
        "id": 14,
        "tag": "Chemical Synthesis",
        "title": "Iron Sulfide: Chemical Compound",
        "sim_id": "iron_sulfide_compound_reaction_sim",
        "avatar_dialogue": "Now let us take Sample A and heat it strongly over a flame. Watch closely—it glows red-hot with an exothermic burst, and transforms into a uniform black substance: Iron Sulfide!",
        "vocabulary": [
            {"word": "Iron(II) Sulfide (FeS)", "definition": "A dark grey/black chemical compound synthesized by the exothermic reaction of iron and sulfur."},
            {"word": "Hydrogen Sulfide (H₂S)", "definition": "A colorless, poisonous gas with an unmistakable, repulsive foul odor of rotten eggs."},
            {"word": "Exothermic Synthesis", "definition": "A chemical reaction that generates and releases thermal heat energy into its surroundings."}
        ],
        "theory": r"""
          <p>Now take a second portion of the iron-sulfur mixture in a china dish and heat it strongly over a burner flame:</p>
          <h4>Sample B: The Chemical Compound (Iron Sulfide)</h4>
          <p>Soon, the sulfur melts and the mixture begins to glow with a brilliant reddish glow. Even if you remove the burner, the reaction continues on its own—it is strongly <em>exothermic</em>! A hard, uniform, dull black mass is formed: <strong>Iron(II) Sulfide ($\text{FeS}$)</strong>.</p>
          $$\text{Fe}\text{ (s)} + \text{S}\text{ (s)} \xrightarrow{\Delta\text{ (Heat)}} \text{FeS}\text{ (s)}\text{ [A New Compound!]}$$
          <p>Testing Sample B reveals that the original properties of iron and sulfur have completely vanished:</p>
          <ol>
            <li><strong>Magnetic Test:</strong> When a bar magnet is brought near the crushed black powder, <strong>it is NOT attracted</strong>! The iron is now chemically bonded.</li>
            <li><strong>Acid Reaction Test:</strong> When dilute hydrochloric acid ($\text{HCl}$) is added to Sample B, it does NOT produce hydrogen. Instead, it reacts to release <strong>Hydrogen Sulfide gas ($\text{H}_2\text{S}$)</strong>:
              $$\text{FeS}\text{ (s)} + 2\text{HCl}\text{ (aq)} \rightarrow \text{FeCl}_2\text{ (aq)} + \text{H}_2\text{S}\text{ (g)}\uparrow\text{ [Rotten-Egg Odor!]}$$
            </li>
          </ol>
        r""",
        "checkpoints": [
            {
                "question": "How does the chemical compound Iron Sulfide (Sample B) respond to a bar magnet?",
                "options": [
                    "A. It is attracted twice as strongly as pure iron",
                    "B. It is not attracted by the magnet because the iron atoms are chemically bonded",
                    "C. It flies through the air towards the ceiling",
                    "D. It converts into yellow sulfur powder instantly"
                ],
                "correct": 1,
                "explanation": "In iron sulfide (FeS), the iron atoms are bonded into a new compound lattice; the characteristic magnetic property of elemental iron is completely lost."
            },
            {
                "question": "What gas is produced when dilute hydrochloric acid is added to Iron Sulfide (FeS), and what is its distinctive odor?",
                "options": [
                    "A. Hydrogen gas with a sweet rose fragrance",
                    "B. Hydrogen sulfide gas (H₂S) with a repulsive rotten-egg odor",
                    "C. Carbon dioxide gas with no smell",
                    "D. Pure steam with a minty smell"
                ],
                "correct": 1,
                "explanation": "FeS reacts with HCl to liberate hydrogen sulfide gas (H₂S), notorious for its foul rotten-egg stench."
            }
        ]
    },
    {
        "id": 15,
        "tag": "Mineralogy",
        "title": "Native & Compound Minerals",
        "sim_id": "native_compound_minerals_sim",
        "avatar_dialogue": "Where do elements and compounds come from in nature? From rocks and minerals beneath our feet! Minerals are Earth's geological treasure chest.",
        "vocabulary": [
            {"word": "Mineral", "definition": "A naturally occurring, inorganic solid substance possessing an orderly internal crystalline atomic structure and a definite chemical composition."},
            {"word": "Native Mineral", "definition": "A mineral found in nature in an uncombined, elemental state (e.g., native gold, native copper, native sulfur)."},
            {"word": "Compound Mineral", "definition": "A mineral composed of two or more chemically bonded elements (e.g., Quartz SiO₂, Calcite CaCO₃, Pyrite FeS₂)."}
        ],
        "theory": r"""
          <p>The solid Earth's crust is composed of rocks, and rocks are composed of <strong>minerals</strong>. A mineral is a naturally occurring, inorganic solid with a definite crystalline structure.</p>
          <p>Minerals are divided into two fundamental chemical classes:</p>
          <ul>
            <li><strong>Native Minerals (Pure Elements):</strong> Minerals composed of only one uncombined element:
              <ul>
                <li><em>Native Gold ($\text{Au}$):</em> Unreactive noble metal nuggets found in alluvial river sands.</li>
                <li><em>Native Copper ($\text{Cu}$):</em> Found in volcanic basalt formations.</li>
                <li><em>Native Diamond & Graphite:</em> Pure crystalline allotropes of elemental carbon ($\text{C}$).</li>
                <li><em>Native Sulfur ($\text{S}$):</em> Bright yellow crystals found around volcanic fumaroles.</li>
              </ul>
            </li>
            <li><strong>Compound Minerals (Chemical Combinations):</strong> Over $99\%$ of Earth's minerals are compounds:
              <ul>
                <li><em>Quartz ($\text{SiO}_2$):</em> Silicon dioxide, forming beach sand and glass crystals.</li>
                <li><em>Calcite ($\text{CaCO}_3$):</em> Calcium carbonate, forming limestone, marble, and coral reefs.</li>
                <li><em>Hematite ($\text{Fe}_2\text{O}_3$) & Magnetite ($\text{Fe}_3\text{O}_4$):</em> Iron oxide ores.</li>
              </ul>
            </li>
          </ul>
        r""",
        "checkpoints": [
            {
                "question": "Which of the following is classified as a native mineral composed of a single uncombined element?",
                "options": [
                    "A. Quartz (SiO₂)",
                    "B. Calcite (CaCO₃)",
                    "C. Native Gold nugget (Au)",
                    "D. Table salt (NaCl)"
                ],
                "correct": 2,
                "explanation": "Gold nuggets occur naturally as uncombined, elemental atoms due to gold's low chemical reactivity."
            },
            {
                "question": "What is the chemical composition of the abundant mineral Quartz?",
                "options": [
                    "A. Pure elemental iron (Fe)",
                    "B. Silicon dioxide (SiO₂)",
                    "C. Calcium carbonate (CaCO₃)",
                    "D. Sodium hydroxide (NaOH)"
                ],
                "correct": 1,
                "explanation": "Quartz is a compound mineral consisting of silicon and oxygen bonded in a 1:2 ratio as silicon dioxide (SiO₂)."
            }
        ]
    },
    {
        "id": 16,
        "tag": "Advanced Materials",
        "title": "Smartphones, Aerogels & Dhokra Art",
        "sim_id": "advanced_graphene_dhokra_sim",
        "avatar_dialogue": "Look at the modern smartphone in your pocket: it contains over 45 chemical elements! From ancient tribal Dhokra bronze casting to futuristic Graphene aerogels, elements shape human civilization.",
        "vocabulary": [
            {"word": "Smartphone Elements", "definition": "Over 45 distinct periodic elements integrated into mobile electronics (e.g., Indium for touchscreens, Lithium for batteries, Neodymium for speakers)."},
            {"word": "Graphene Aerogel", "definition": "A revolutionary carbon nanomaterial recognized as the world's lightest solid (density ~0.16 mg/cm³), capable of absorbing 900 times its weight in oil."},
            {"word": "Dhokra Art", "definition": "Ancient non-ferrous lost-wax bell metal (brass/bronze) alloy casting craft practiced for over 4,000 years in Bihar, Jharkhand, West Bengal, and Odisha."}
        ],
        "theory": r"""
          <p>Elements, compounds, and alloys form the technological backbone of human society across four millennia:</p>
          <ul>
            <li><strong>The Modern Smartphone:</strong> A handheld smartphone incorporates over <strong>45 chemical elements</strong>:
              <ul>
                <li><em>Screen:</em> Indium Tin Oxide ($\text{In}_2\text{O}_3\text{--}\text{SnO}_2$) provides transparent electrical conductivity for capacitive touch sensing.</li>
                <li><em>Processor Chip:</em> Billions of microscopic silicon ($\text{Si}$) transistors doped with phosphorus and boron.</li>
                <li><em>Battery:</em> Lithium cobalt oxide ($\text{LiCoO}_2$) cathode with graphite carbon anode.</li>
                <li><em>Acoustics & Vibration:</em> Powerful neodymium ($\text{Nd}$) and dysprosium ($\text{Dy}$) rare-earth magnets.</li>
              </ul>
            </li>
            <li><strong>Graphene Aerogel:</strong> Developed by modern materials scientists, this carbon-based sponge is the <em>lightest solid on Earth</em> ($7\times$ lighter than air!). It possesses incredible porosity, absorbing up to 900 times its mass in petroleum oils during ocean oil spill remediations.</li>
            <li><strong>Traditional Dhokra Metalcraft:</strong> Originating from the ancient Indus Valley Civilization (such as the famed 'Dancing Girl' of Mohenjo-daro), tribal artisans in Bihar, Odisha, and West Bengal use a <strong>lost-wax casting process</strong> with beeswax molds to cast intricate brass and bronze (<em>Mishraloha</em>) artifacts inspired by wildlife and folk lore.</li>
          </ul>
        r""",
        "checkpoints": [
            {
                "question": "Approximately how many different chemical elements are utilized in the manufacturing of a modern smartphone?",
                "options": [
                    "A. Exactly 2 elements (copper and plastic)",
                    "B. Over 45 different elements",
                    "C. All 118 elements equally",
                    "D. Only 1 element (pure gold)"
                ],
                "correct": 1,
                "explanation": "A smartphone requires over 45 distinct periodic elements across its display, processor, battery, casing, and circuitry."
            },
            {
                "question": "What traditional metalcraft technique is used in the ancient Dhokra art of Bihar and Odisha?",
                "options": [
                    "A. Plastic 3D printing",
                    "B. Lost-wax casting with molten brass or bronze alloys",
                    "C. Chiseling frozen ice sculptures",
                    "D. Chemical acid etching on glass"
                ],
                "correct": 1,
                "explanation": "Dhokra artisans use the ancient lost-wax casting technique with clay and beeswax cores, pouring molten brass/bronze alloys to cast figurines."
            }
        ]
    },
    {
        "id": 17,
        "is_quiz_slide": True,
        "quiz_start_idx": 1,
        "quiz_count": 10,
        "title": "Mastery Challenge • Part I",
        "avatar_dialogue": "Sensational work mastering the core foundations! Now, show off your analytical skills in Part I of our Elements, Compounds, and Mixtures Mastery Challenge (Questions 1 to 10)."
    },
    {
        "id": 18,
        "is_quiz_slide": True,
        "quiz_start_idx": 11,
        "quiz_count": 10,
        "title": "Mastery Challenge • Part II",
        "avatar_dialogue": "Keep your analytical sharpness! Here is Part II of the Challenge (Questions 11 to 20), focusing on alloys, air quality, pure substances, and periodic states."
    },
    {
        "id": 19,
        "is_quiz_slide": True,
        "quiz_start_idx": 21,
        "quiz_count": 10,
        "title": "Mastery Challenge • Part III",
        "avatar_dialogue": "You are making tremendous headway! Part III (Questions 21 to 30) tests your deep conceptual grasp of the Iron and Sulfur experiment and compound stoichiometry."
    },
    {
        "id": 20,
        "is_quiz_slide": True,
        "quiz_start_idx": 31,
        "quiz_count": 10,
        "title": "Mastery Challenge • Part IV",
        "avatar_dialogue": "The grand finale! Tackle the final 10 inquiries (Questions 31 to 40) on minerals, Dhokra metallurgy, and advanced materials to earn your Master Chemist Certification!"
    }
]

QUIZ_QUESTIONS = [
    {
        "id": 1,
        "question": "What is the primary scientific difference between a mixture and a compound?",
        "options": [
            "A. A mixture always has a boiling point of 100°C while a compound does not",
            "B. In a mixture, components combine physically and retain their individual properties; in a compound, elements combine chemically in a fixed ratio to produce entirely new properties",
            "C. Mixtures are always liquids while compounds are always solid rocks",
            "D. A mixture can only be formed in outer space"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Physical vs Chemical Combination:</strong> A mixture is a physical blend where constituent substances retain their individual properties and can be separated physically.<br><strong>Step 2: Compound Formation:</strong> A compound is formed via chemical bonds in a fixed mass ratio, acquiring completely new chemical properties.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 2,
        "question": "Which of the following is an example of a non-uniform (heterogeneous) mixture?",
        "options": [
            "A. Sprout salad with green grams, chickpeas, onions, and tomatoes",
            "B. Completely dissolved sugar syrup",
            "C. Clean atmospheric air",
            "D. Solid brass alloy"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Heterogeneous Definition:</strong> A mixture whose components remain physically separate and visibly distinguishable.<br><strong>Step 2: Sprout Salad:</strong> Grams, chickpeas, onions, and tomatoes are plainly visible and distinct.<br><strong>Step 3: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 3,
        "question": "What are alloys, such as brass, bronze, and stainless steel?",
        "options": [
            "A. Pure non-metallic gases",
            "B. Uniform (homogeneous) solid mixtures of metals or metals with non-metals",
            "C. Heterogeneous rocks that shatter in water",
            "D. Radioactive elements created in nuclear reactors"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Alloy Definition:</strong> Alloys are homogeneous solid solutions formed by melting metals together with other metals or carbon.<br><strong>Step 2: Examples:</strong> Brass (Cu + Zn), Bronze (Cu + Sn), Stainless Steel (Fe + Cr + Ni + C).<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 4,
        "question": "According to ancient Indian texts such as the Charaka Samhita, what was 'Kamsya' (Bronze) composed of, and what was its traditional use?",
        "options": [
            "A. 1 part gold and 3 parts silver for royal crowns",
            "B. 4 parts copper (Tamra) and 1 part tin (Vanga), traditionally used for dining vessels to boost digestion and immunity",
            "C. Pure lead for building weapons",
            "D. Equal parts mercury and sulfur for making paint"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Heritage Context:</strong> Ancient Indian Ayurveda classified metal mixtures as <em>Mishraloha</em>.<br><strong>Step 2: Formulation:</strong> Kamsya (Bronze) was formulated with 4 parts Tamra (copper) to 1 part Vanga (tin).<br><strong>Step 3: Application:</strong> Used for eating plates to promote digestion and health.<br><strong>Step 4: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 5,
        "question": "Why is clean atmospheric air classified as a uniform (homogeneous) mixture rather than a compound?",
        "options": [
            "A. Air consists of separate gases (N₂, O₂, Ar, CO₂) that can be separated by physical liquefaction and retain their individual properties",
            "B. Air has a fixed chemical formula: N₇₈O₂₁",
            "C. Air freezes into a diamond at 0°C",
            "D. Air contains only one type of atom"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Mixture vs Compound:</strong> The gases in air are not chemically bonded; they maintain their individual chemical properties.<br><strong>Step 2: Physical Separation:</strong> Fractional distillation of liquid air cleanly separates nitrogen, oxygen, and argon.<br><strong>Step 3: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 6,
        "question": "What happens when exhaled human breath or air containing carbon dioxide is bubbled through clear lime water?",
        "options": [
            "A. The lime water catches fire with a blue flame",
            "B. It turns milky white due to the formation of insoluble calcium carbonate (CaCO₃)",
            "C. It turns into pure yellow sulfur powder",
            "D. It evaporates into thin air instantly"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Chemical Reaction:</strong> $\text{Ca(OH)}_2\text{ (aq)} + \text{CO}_2\text{ (g)} \rightarrow \text{CaCO}_3\text{ (s)}\downarrow + \text{H}_2\text{O}\text{ (l)}$.<br><strong>Step 2: Turbidity:</strong> Insoluble $\text{CaCO}_3$ precipitates as tiny white suspended crystals, making the liquid milky.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 7,
        "question": "What does an Air Quality Index (AQI) value of 350 signify?",
        "options": [
            "A. Pristine air quality with zero health risks",
            "B. Very Poor air quality causing respiratory illness on prolonged exposure",
            "C. Air that is 100% pure oxygen",
            "D. Freezing blizzards are imminent"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: AQI Bands:</strong> 0–50 is Good; 51–100 Satisfactory; 101–200 Moderate; 201–300 Poor; 301–400 Very Poor; 401–500 Severe.<br><strong>Step 2: Health Effect:</strong> An AQI of 350 falls into 'Very Poor', posing severe respiratory risks.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 8,
        "question": "In scientific terminology, what constitutes a 'pure substance'?",
        "options": [
            "A. Any food product with no added chemical preservatives bought from an organic grocery store",
            "B. Matter composed of only one type of identical constituent particle that cannot be separated by physical methods",
            "C. A bowl of salad with fresh washed vegetables",
            "D. Tap water that has been boiled once"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Scientific Definition:</strong> A pure substance contains only one kind of particle (identical atoms or molecules) with invariant physical and chemical properties.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 9,
        "question": "Which of the following is the best example of a chemical element?",
        "options": [
            "A. Pure 24-karat Gold (Au)",
            "B. Distilled Water (H₂O)",
            "C. Sodium chloride (NaCl)",
            "D. Carbon dioxide (CO₂)"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Element Definition:</strong> A substance consisting of only one type of atom that cannot be chemically simplified.<br><strong>Step 2: Gold:</strong> Gold ($\text{Au}$) is a pure element. Water, salt, and carbon dioxide are compounds.<br><strong>Step 3: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 10,
        "question": "Which two chemical elements are the ONLY ones that exist as liquids at standard room temperature (25°C)?",
        "options": [
            "A. Iron and Copper",
            "B. Mercury (metal) and Bromine (non-metal)",
            "C. Hydrogen and Helium",
            "D. Silicon and Carbon"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Periodic States:</strong> Out of 118 elements, only two are liquid at $25^\circ\text{C}$.<br><strong>Step 2: Identity:</strong> Mercury ($\text{Hg}$) is the sole liquid metal, and Bromine ($\text{Br}_2$) is the sole liquid non-metal.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 11,
        "question": "What happens when a piece of the metal Gallium (Ga) is placed on the palm of a human hand?",
        "options": [
            "A. It catches fire and burns through the hand",
            "B. It melts into a gleaming liquid pool because its melting point (~30°C) is below human body temperature (37°C)",
            "C. It freezes the hand into solid ice",
            "D. It turns into radioactive uranium"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Melting Point of Gallium:</strong> Gallium melts at $29.76^\circ\text{C}$.<br><strong>Step 2: Body Temperature:</strong> Normal human body core/palm temperature is approximately $36^\circ\text{C}\text{--}37^\circ\text{C}$.<br><strong>Step 3: Phase Change:</strong> Body heat melts the solid gallium into liquid.<br><strong>Step 4: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 12,
        "question": "Why is water (H₂O) classified as a chemical compound rather than a mixture?",
        "options": [
            "A. It is composed of hydrogen and oxygen chemically bonded in a fixed 2:1 ratio by volume, with properties entirely different from its parent elements",
            "B. It can be separated into hydrogen and oxygen by pouring it through paper filter",
            "C. It is formed by mixing ice and steam in a bucket",
            "D. Water burns with an explosive pop sound"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Chemical Bonding:</strong> Hydrogen and oxygen are bonded covalently in a strict $2:1$ atomic ratio.<br><strong>Step 2: Distinct Properties:</strong> Hydrogen is combustible and oxygen supports combustion, but water extinguishes fire.<br><strong>Step 3: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 13,
        "question": "What is the result when pure white sugar (sucrose) is subjected to strong thermal heating in a test tube?",
        "options": [
            "A. It turns into sweet liquid milk",
            "B. It decomposes into black elemental carbon (charcoal) and water vapour, proving it is a compound of carbon, hydrogen, and oxygen",
            "C. It sublimates into chlorine gas",
            "D. It converts into gold nuggets"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Chemical Formula:</strong> Sucrose is $\text{C}_{12}\text{H}_{22}\text{O}_{11}$.<br><strong>Step 2: Decomposition:</strong> Heat breaks chemical bonds, releasing water vapour ($\text{H}_2\text{O}$) and leaving black elemental carbon ($\text{C}$) residue.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 14,
        "question": "In the Iron and Sulfur experiment, how does Sample A (the unheated physical mixture of Fe and S) behave when tested with a bar magnet?",
        "options": [
            "A. The magnet attracts only the grey iron filings, cleanly separating them from the yellow sulfur powder",
            "B. The sulfur powder is attracted to the magnet while iron is repelled",
            "C. The mixture explodes violently upon touching the magnet",
            "D. Neither component responds to the magnet"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Mixture Properties:</strong> Physical mixing preserves individual component properties.<br><strong>Step 2: Magnetism:</strong> Elemental iron remains ferromagnetic; a magnet attracts and separates all iron filings cleanly from sulfur.<br><strong>Step 3: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 15,
        "question": "What gas is liberated when dilute hydrochloric acid (HCl) is added to Sample A (unheated Fe + S mixture)?",
        "options": [
            "A. Rotten-egg smelling hydrogen sulfide gas",
            "B. Colorless, odorless hydrogen gas (H₂) that burns with a 'pop' sound",
            "C. Brown nitrogen dioxide fumes",
            "D. Pure liquid water"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Chemical Reaction:</strong> $\text{Fe}\text{ (s)} + 2\text{HCl}\text{ (aq)} \rightarrow \text{FeCl}_2\text{ (aq)} + \text{H}_2\text{ (g)}\uparrow$.<br><strong>Step 2: Gas Properties:</strong> Elemental iron reacts with acid to release odorless $\text{H}_2$ gas, which burns with a characteristic pop sound.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 16,
        "question": "In the Iron and Sulfur experiment, how is Sample B (the chemical compound Iron Sulfide) prepared from Sample A?",
        "options": [
            "A. By freezing the mixture in an ice bath for three weeks",
            "B. By heating the mixture strongly until it glows red-hot in an exothermic reaction and forms a uniform black mass",
            "C. By dissolving the mixture in cooking oil",
            "D. By shaking the mixture in a plastic bottle"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Synthesis:</strong> Heating supplies activation energy for $\text{Fe} + \text{S} \rightarrow \text{FeS}$.<br><strong>Step 2: Exothermic Glow:</strong> The reaction glows red-hot exothermically, synthesizing black iron sulfide.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 17,
        "question": "When a magnet is brought near crushed Iron Sulfide (Sample B), what occurs?",
        "options": [
            "A. The entire compound is attracted strongly to the magnet",
            "B. The compound is NOT attracted to the magnet because iron has chemically bonded into FeS",
            "C. The compound turns into yellow sulfur powder immediately",
            "D. The magnet loses its magnetism forever"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Compound Structure:</strong> In iron sulfide ($\text{FeS}$), iron atoms are bound in a crystal lattice.<br><strong>Step 2: Loss of Individual Properties:</strong> The magnetic property of free elemental iron is lost; $\text{FeS}$ is not ferromagnetic under standard conditions.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 18,
        "question": "What gas is produced when dilute hydrochloric acid is poured onto Iron Sulfide (FeS), and what is its sensory signature?",
        "options": [
            "A. Hydrogen gas with a pleasant lemon scent",
            "B. Hydrogen sulfide gas (H₂S) with an unmistakable, foul odor of rotten eggs",
            "C. Carbon dioxide gas that smells like freshly baked bread",
            "D. Oxygen gas with zero smell"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Reaction:</strong> $\text{FeS}\text{ (s)} + 2\text{HCl}\text{ (aq)} \rightarrow \text{FeCl}_2\text{ (aq)} + \text{H}_2\text{S}\text{ (g)}\uparrow$.<br><strong>Step 2: Odor Signature:</strong> $\text{H}_2\text{S}$ gas possesses an extremely distinctive, foul stench of decaying rotten eggs.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 19,
        "question": "What is a mineral according to geology and chemistry?",
        "options": [
            "A. Any manufactured plastic toy found in sand",
            "B. A naturally occurring, inorganic solid with an orderly crystalline structure and definite chemical composition",
            "C. An artificial chemical synthesized in a pharmaceutical factory",
            "D. A pool of gasoline in an oil refinery"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Geological Criteria:</strong> A mineral must be naturally occurring, inorganic, solid, with an ordered atomic lattice and definite chemical formula.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 20,
        "question": "Which of the following is classified as a native mineral found in nature as an uncombined pure element?",
        "options": [
            "A. Quartz (SiO₂)",
            "B. Calcite (CaCO₃)",
            "C. Native Copper (Cu)",
            "D. Iron Pyrite (FeS₂)"
        ],
        "correct": 2,
        "solution": r"<p><strong>Step 1: Native Mineral Definition:</strong> A mineral formed from a single uncombined element.<br><strong>Step 2: Examples:</strong> Native copper ($\text{Cu}$), gold ($\text{Au}$), silver ($\text{Ag}$), and sulfur ($\text{S}$).<br><strong>Step 3: Conclusion:</strong> Option C is correct.</p>"
    },
    {
        "id": 21,
        "question": "Approximately how many different chemical elements are required to manufacture a typical modern smartphone?",
        "options": [
            "A. Exactly 3 elements",
            "B. Over 45 different elements",
            "C. Only 1 element",
            "D. All 118 elements"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Mobile Electronics:</strong> A smartphone integrates over 45 chemical elements across its display, chips, circuit boards, speakers, and battery.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 22,
        "question": "What remarkable properties make Graphene Aerogel a breakthrough material in modern nanotechnology?",
        "options": [
            "A. It is the densest metal on Earth and sinks in liquid mercury",
            "B. It is the lightest solid known on Earth, highly porous, and can absorb up to 900 times its weight in oil",
            "C. It is an edible dessert powder made of sucrose",
            "D. It replaces drinking water in desert areas"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Graphene Aerogel:</strong> A carbon-based sponge recognized as the world's lightest solid material ($\rho \approx 0.16\text{ mg/cm}^3$).<br><strong>Step 2: Porosity:</strong> Absorbs massive quantities of organic solvents and crude oils, making it ideal for environmental cleanup.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 23,
        "question": "What traditional casting method is employed in the ancient Dhokra metalcraft of Bihar, Jharkhand, and Odisha?",
        "options": [
            "A. Lost-wax casting using beeswax models and molten brass or bronze alloys",
            "B. Hammering cold steel bars by hand",
            "C. Laser sintering of titanium powder",
            "D. Electroplating plastic toys"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Dhokra Craft:</strong> An ancient non-ferrous lost-wax bell metal casting technique practicing for millennia in eastern India.<br><strong>Step 2: Materials:</strong> Beeswax patterns coated in clay, fired to burn out the wax, and filled with molten brass/bronze.<br><strong>Step 3: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 24,
        "question": "Stainless steel is an alloy composed primarily of which elements?",
        "options": [
            "A. Copper and Zinc",
            "B. Iron, Chromium, Nickel, and Carbon",
            "C. Aluminum and Mercury",
            "D. Gold and Silver"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Stainless Steel Formulation:</strong> Iron is alloyed with chromium (min $10.5\%$), nickel, and carbon.<br><strong>Step 2: Corrosion Resistance:</strong> Chromium forms an invisible protective passive oxide layer preventing rust.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 25,
        "question": "Which of the following is a metalloid possessing properties intermediate between metals and non-metals?",
        "options": [
            "A. Iron (Fe)",
            "B. Silicon (Si)",
            "C. Oxygen (O₂)",
            "D. Helium (He)"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Metalloids:</strong> Elements along the periodic diagonal boundary (B, Si, Ge, As, Sb, Te).<br><strong>Step 2: Silicon:</strong> Silicon is a classic metalloid semiconductor.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 26,
        "question": "Why can an aqueous solution of sodium chloride (salt water) be separated by physical evaporation, but pure sodium chloride cannot be physically split into sodium and chlorine?",
        "options": [
            "A. Salt water is a mixture whose components are not chemically bonded, whereas sodium chloride is a chemical compound held by strong ionic bonds",
            "B. Salt water contains no chemical elements",
            "C. Sodium and chlorine do not exist",
            "D. Salt water is a living bacterial colony"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Mixture vs Compound Separation:</strong> Evaporation breaks weak intermolecular attractions between water and dissolved ions, leaving solid $\text{NaCl}$.<br><strong>Step 2: Compound Bonds:</strong> $\text{Na}^+$ and $\text{Cl}^-$ are bound by strong chemical ionic bonds that cannot be cleaved by simple boiling.<br><strong>Step 3: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 27,
        "question": "What is the physical state of the element Bromine (Br₂) at 25°C and 1 atm pressure?",
        "options": [
            "A. A solid metallic crystal",
            "B. A dense, reddish-brown fuming liquid",
            "C. A colorless noble gas",
            "D. An ionized plasma"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Bromine State:</strong> Bromine ($\text{Br}_2$) is the only non-metallic element that is a liquid at standard room temperature, appearing as a dense, volatile reddish-brown liquid.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 28,
        "question": "When iron rusts to form reddish-brown iron oxide (Fe₂O₃), what type of substance has been formed?",
        "options": [
            "A. A homogeneous mixture of iron and air",
            "B. A chemical compound formed by the chemical reaction of iron, oxygen, and moisture",
            "C. An unbonded physical solution",
            "D. A new radioactive element"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Rusting Reaction:</strong> Iron reacts with atmospheric oxygen and water chemically: $4\text{Fe} + 3\text{O}_2 + 2x\text{H}_2\text{O} \rightarrow 2\text{Fe}_2\text{O}_3\cdot x\text{H}_2\text{O}$.<br><strong>Step 2: Nature:</strong> Rust is a chemical compound with entirely new properties (brittle, non-conductive).<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 29,
        "question": "What gas is produced at the anode during the electrolysis of water?",
        "options": [
            "A. Hydrogen gas (H₂)",
            "B. Oxygen gas (O₂)",
            "C. Nitrogen gas (N₂)",
            "D. Carbon dioxide (CO₂)"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Electrolysis Electrodes:</strong> Negative electrode = Cathode ($\text{H}_2$ gas evolved); Positive electrode = Anode ($\text{O}_2$ gas evolved).<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 30,
        "question": "Why is brass used to make musical horns and trumpets instead of pure copper?",
        "options": [
            "A. Pure copper is too soft and easily bent, whereas alloying copper with zinc creates brass with greater hardness, durability, and acoustic resonance",
            "B. Brass is a gas that floats in air",
            "C. Copper dissolves in spit",
            "D. Zinc makes brass magnetic"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Alloying Benefits:</strong> Pure copper is relatively soft. Adding zinc ($30\%\text{--}40\%$) forms brass, which is harder, stronger, highly workable, and possesses superior musical acoustics.<br><strong>Step 2: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 31,
        "question": "Which of the following compounds is composed of atoms in an exact 1:1 ratio?",
        "options": [
            "A. Water (H₂O)",
            "B. Sodium chloride (NaCl)",
            "C. Carbon dioxide (CO₂)",
            "D. Ammonia (NH₃)"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Atomic Ratios:</strong> $\text{NaCl}$ contains 1 sodium atom for every 1 chlorine atom ($1:1$).<br><strong>Step 2: Contrast:</strong> $\text{H}_2\text{O}$ is $2:1$, $\text{CO}_2$ is $1:2$, $\text{NH}_3$ is $1:3$.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 32,
        "question": "What is the common term used for a homogeneous mixture of a solute dissolved in a solvent?",
        "options": [
            "A. A suspension",
            "B. A solution",
            "C. An emulsion",
            "D. An alloy pellet"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Solution Definition:</strong> A homogeneous mixture of two or more substances is scientifically called a <strong>solution</strong>.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 33,
        "question": "Which of the following minerals is composed of calcium, carbon, and oxygen (CaCO₃)?",
        "options": [
            "A. Quartz",
            "B. Calcite",
            "C. Mica",
            "D. Diamond"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Mineral Formulas:</strong> Calcite is calcium carbonate ($\text{CaCO}_3$). Quartz is $\text{SiO}_2$. Diamond is pure carbon ($\text{C}$).<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 34,
        "question": "Why does a piece of burning wood eventually turn into ash and smoke, losing mass in the fireplace?",
        "options": [
            "A. Matter is permanently destroyed by fire",
            "B. The chemical compounds in wood react with atmospheric oxygen, converting into gaseous carbon dioxide and water vapour that escape into the air",
            "C. Fire turns wood into pure light photons",
            "D. Wood turns into ice crystals"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Combustion Chemistry:</strong> Wood (cellulose/lignin) reacts with $\text{O}_2$ to produce $\text{CO}_2$ and $\text{H}_2\text{O}$ gases, leaving non-combustible mineral ash behind.<br><strong>Step 2: Mass Conservation:</strong> Total mass is conserved if escaping gases are captured.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 35,
        "question": "Which non-metal is an exceptional conductor of electricity despite being a non-metal?",
        "options": [
            "A. Sulfur powder",
            "B. Graphite (an allotrope of carbon)",
            "C. Diamond",
            "D. Phosphorus"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Graphite Conductivity:</strong> In graphite, each carbon atom is bonded to three others in planar sheets, leaving free delocalized electrons that conduct electricity.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 36,
        "question": "What is the chemical name of rust that forms on iron gates exposed to damp air?",
        "options": [
            "A. Pure iron filings",
            "B. Hydrated iron(III) oxide (Fe₂O₃·xH₂O)",
            "C. Iron sulfide (FeS)",
            "D. Calcium carbonate (CaCO₃)"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Rust Composition:</strong> Rust is chemically hydrated ferric oxide: $\text{Fe}_2\text{O}_3\cdot x\text{H}_2\text{O}$.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 37,
        "question": "If you mix sand and water in a beaker, stir vigorously, and allow it to sit undisturbed for 10 minutes, what will you observe?",
        "options": [
            "A. The sand dissolves completely, forming a clear homogeneous solution",
            "B. The heavy sand particles settle at the bottom as a precipitate, demonstrating a heterogeneous suspension",
            "C. The sand and water combine into a flammable gas",
            "D. The water freezes solid"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Suspension Behavior:</strong> Sand does not dissolve in water; it forms a heterogeneous suspension where gravity causes sand particles to sediment at the base.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 38,
        "question": "Why is the Indium Tin Oxide (ITO) compound used on modern smartphone screens?",
        "options": [
            "A. Because it is completely opaque and blocks all light",
            "B. Because it is both optically transparent and electrically conductive, enabling capacitive touch detection",
            "C. Because it prevents the glass from breaking from drops of 50 metres",
            "D. Because it recharges the battery from sunlight"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: ITO Material Properties:</strong> Indium tin oxide is a rare transparent conducting oxide (TCO).<br><strong>Step 2: Function:</strong> It transmits $>90\%$ of visible light while conducting electrical charges, allowing touchscreens to register fingertip capacitance.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 39,
        "question": "What type of chemical bond holds sodium and chlorine atoms together in a grain of table salt?",
        "options": [
            "A. Ionic bond (electrostatic attraction between Na⁺ and Cl⁻ ions)",
            "B. Gravitational bond",
            "C. Magnetic force between iron poles",
            "D. Nuclear friction"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Ionic Bonding:</strong> Sodium transfers its valence electron to chlorine, forming $\text{Na}^+$ and $\text{Cl}^-$ ions that are bound by strong electrostatic ionic attraction.<br><strong>Step 2: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 40,
        "question": "Which of the following summaries provides the most accurate and comprehensive synthesis of elements, compounds, and mixtures?",
        "options": [
            "A. All matter is a mixture; elements and compounds do not exist in reality",
            "B. Elements are fundamental pure substances of one atomic type; compounds are pure substances formed by chemically bonding elements in fixed ratios; mixtures are physical blends where components retain their individual identities",
            "C. Compounds can be separated using magnets, while mixtures require nuclear reactors",
            "D. Metals are compounds and non-metals are mixtures"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Grand Synthesis:</strong> Pure substances divide into Elements (single atom species) and Compounds (chemically bonded in fixed ratios). Mixtures are physical combinations without chemical reaction where individual identities are preserved.<br><strong>Step 2: Conclusion:</strong> Option B is the complete, scientifically rigorous synthesis.</p>"
    }
]
