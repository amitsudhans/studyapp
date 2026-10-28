# -*- coding: utf-8 -*-
"""
Class 8 Science - Chapter 9: Solutions, Solubility, and Density
Comprehensive Dataset:
- 20 Slides (16 Interactive Theory/Sim Slides + 4 Dedicated Mastery Challenge Slides)
- 32 In-Slide Checkpoints (2 per content slide) with instant feedback
- 40 Mastery Quiz Questions with full step-by-step solutions
- Key Technical Vocabulary for every slide
- Teacher Avatar Narration (Dr. Asima Chatterjee & Acharya Charaka)
"""

SLIDES = [
    {
        "id": 1,
        "tag": "Solution Fundamentals",
        "title": "Defining Solutions & Solvents",
        "sim_id": "solution_solute_solvent_sim",
        "avatar_dialogue": "Welcome to our Solutions and Density Laboratory! A solution is a uniform, homogeneous mixture where solute particles seamlessly blend into a solvent without ever settling down.",
        "vocabulary": [
            {"word": "Solution", "definition": "A uniform (homogeneous) mixture where two or more substances blend so thoroughly that individual components cannot be distinguished separately."},
            {"word": "Solute", "definition": "The substance that dissolves in the solvent (e.g., solid salt or sugar)."},
            {"word": "Solvent", "definition": "The dissolving medium that incorporates the solute (typically the liquid present in larger quantity, like water)."},
            {"word": "Non-Uniform Mixture", "definition": "A heterogeneous mixture (such as sand or sawdust in water) where components remain unevenly distributed and distinctly visible."}
        ],
        "theory": r"""
          <p>When you dissolve sugar or salt in water, something extraordinary happens at the microscopic level: the solid crystals break down into individual molecules or ions that disperse evenly throughout the liquid. This forms a <strong>solution</strong>—a <em>homogeneous (uniform) mixture</em>.</p>
          <ul>
            <li><strong>Uniform Composition:</strong> Every single drop of a salt solution contains exactly the same proportion of salt and water; you cannot visually distinguish the salt particles even under an ordinary microscope.</li>
            <li><strong>Oral Rehydration Solution (ORS):</strong> A life-saving aqueous solution of glucose, sodium chloride, potassium chloride, and trisodium citrate that rapidly restores electrolyte balance in dehydrated patients.</li>
            <li><strong>Non-Uniform (Heterogeneous) Mixtures:</strong> If you stir sand, chalk powder, or sawdust into water, the particles do not dissolve. They remain suspended or settle at the bottom, retaining distinct visible boundaries.</li>
          </ul>
          <div style="background: rgba(56, 189, 248, 0.1); border-left: 3px solid #38bdf8; padding: 0.6rem 0.85rem; border-radius: 4px; margin-top: 0.5rem;">
            $$\text{Solution} = \text{Solute (Dissolved Substance)} + \text{Solvent (Dissolving Medium)}$$
          </div>
        """,
        "checkpoints": [
            {
                "question": "Which of the following is an example of a uniform (homogeneous) solution?",
                "options": [
                    "A. Sawdust thoroughly stirred in water",
                    "B. Oral Rehydration Solution (ORS) dissolved in boiled water",
                    "C. Chalk powder suspended in water",
                    "D. River sand mixed in a beaker of water"
                ],
                "correct": 1,
                "explanation": "ORS dissolves completely into a uniform single-phase mixture where components are distributed evenly and cannot be distinguished separately."
            },
            {
                "question": "When solid table salt dissolves in liquid water to form brine, what role does salt play?",
                "options": [
                    "A. The solvent",
                    "B. The solute",
                    "C. The suspension",
                    "D. The emulsion"
                ],
                "correct": 1,
                "explanation": "In a solid-liquid solution, the solid substance that dissolves is termed the solute, while the liquid that dissolves it is the solvent."
            }
        ]
    },
    {
        "id": 2,
        "tag": "Solute vs Solvent",
        "title": "Gulab Jamun Chashni & Liquids",
        "sim_id": "chashni_liquid_solutions_sim",
        "avatar_dialogue": "Look at the sweet chashni syrup of Gulab Jamun! Even though a huge mass of sugar dissolves in a small volume of water, water remains the solvent because it provides the liquid state.",
        "vocabulary": [
            {"word": "Chashni", "definition": "A viscous Indian sugar syrup prepared by dissolving high masses of sugar in water under heat."},
            {"word": "Liquid-Liquid Solution", "definition": "A homogeneous mixture formed by mixing two miscible liquids (e.g., alcohol and water)."},
            {"word": "Amount Rule", "definition": "When two liquids mix to form a solution, the liquid in smaller volume is the solute, while the one in larger volume is the solvent."}
        ],
        "theory": r"""
          <p>Determining which component is the solute and which is the solvent follows precise scientific rules:</p>
          <ol>
            <li><strong>Solid dissolved in Liquid:</strong> The solid is <em>always</em> the solute, and the liquid is <em>always</em> the solvent, regardless of relative masses. In the preparation of <strong>Gulab Jamun chashni (sugar syrup)</strong>, up to $150\text{ g}$ of sugar dissolves in just $100\text{ mL}$ of water. Despite the greater mass of sugar, water is considered the solvent because the final mixture retains water's liquid phase!</li>
            <li><strong>Two Liquids Forming a Solution:</strong>
              <ul>
                <li>The liquid present in <strong>smaller amount</strong> is the <strong>solute</strong>.</li>
                <li>The liquid present in <strong>larger amount</strong> is the <strong>solvent</strong>.</li>
                <li>For example, in a disinfectant mixture of $70\text{ mL}$ alcohol and $30\text{ mL}$ water, alcohol is the solvent and water is the solute. In an after-shave splash of $90\text{ mL}$ water and $10\text{ mL}$ alcohol, water is the solvent.</li>
              </ul>
            </li>
          </ol>
        """,
        "checkpoints": [
            {
                "question": "In preparing thick Gulab Jamun chashni, 200 g of sugar is dissolved in 100 mL of water. Which component is the solvent?",
                "options": [
                    "A. Sugar, because its mass is greater",
                    "B. Water, because the final solution retains the liquid state",
                    "C. Both are solvents simultaneously",
                    "D. Neither, it is a heterogeneous suspension"
                ],
                "correct": 1,
                "explanation": "When a solid dissolves in a liquid, the liquid component that determines the physical state of the solution is the solvent, regardless of solute mass."
            },
            {
                "question": "If 15 mL of lemon juice is mixed into 200 mL of pure water, what is the solute?",
                "options": [
                    "A. Water, because it is neutral",
                    "B. Lemon juice, because it is present in a smaller amount",
                    "C. Lemon juice is the solvent",
                    "D. Both liquid components are solutes"
                ],
                "correct": 1,
                "explanation": "When two miscible liquids blend into a solution, the liquid present in the smaller volume (lemon juice, 15 mL) is the solute."
            }
        ]
    },
    {
        "id": 3,
        "tag": "Traditional Science",
        "title": "Ayurveda, Siddha & Solvents",
        "sim_id": "ayurvedic_solvents_sim",
        "avatar_dialogue": "For thousands of years, traditional Indian medicine systems like Ayurveda and Siddha mastered solvent extraction using water, oils, and ghee to draw out botanical medicines.",
        "vocabulary": [
            {"word": "Ayurveda & Siddha", "definition": "Ancient Indian systems of medicine relying on natural herbs, botanical compounds, and lifestyle harmony."},
            {"word": "Solvent Extraction", "definition": "The biochemical process where a liquid solvent selectively dissolves active therapeutic compounds from plant tissues."},
            {"word": "Hydro-Alcoholic Extracts", "definition": "Solvent mixtures of water and natural alcohol (asava/arishta) that extract both water-soluble and alcohol-soluble herbal actives."},
            {"word": "Sneha Kalpana", "definition": "Ayurvedic pharmaceutical preparation of medicated oils (Taila) and ghee (Ghrita) acting as lipophilic (fat-loving) solvents."}
        ],
        "theory": r"""
          <p>Traditional Indian scientific heritage contains profound mastery of solvent properties in pharmacology:</p>
          <ul>
            <li><strong>Water as an Aqueous Solvent (Kashaya / Kwatha):</strong> Boiling herbs in water extracts water-soluble polar phyto-compounds such as tannins, flavonoids, and glycosides.</li>
            <li><strong>Hydro-Alcoholic Fermentation (Asava & Arishta):</strong> Self-generated natural ethanol in herbal mixtures acts as a dual solvent, dissolving substances that are insoluble in pure water and preserving formulations for decades.</li>
            <li><strong>Lipophilic Solvents (Taila & Ghrita):</strong> Medicated sesame oil and clarified butter (cow's ghee) serve as non-polar lipid solvents (<em>Sneha Kalpana</em>). They extract fat-soluble therapeutic alkaloids and transport them across cellular lipid membranes and the blood-brain barrier!</li>
          </ul>
        """,
        "checkpoints": [
            {
                "question": "Why do Ayurvedic pharmacies use medicated oils and ghee (Ghrita) as solvents instead of only plain water?",
                "options": [
                    "A. Oils are cheaper than natural river water",
                    "B. Lipid solvents selectively dissolve fat-soluble (lipophilic) medicinal compounds that cannot dissolve in water",
                    "C. Plain water destroys all plant compounds immediately",
                    "D. Oils make medicines evaporate instantly into steam"
                ],
                "correct": 1,
                "explanation": "Many active botanical phytochemicals are non-polar and insoluble in water; vegetable oils and ghee act as non-polar lipid solvents to dissolve and deliver them."
            },
            {
                "question": "What primary solvent is traditionally used in preparing Ayurvedic herbal decoctions known as Kwatha or Kashaya?",
                "options": [
                    "A. Kerosene",
                    "B. Pure water",
                    "C. Mercury",
                    "D. Liquid nitrogen"
                ],
                "correct": 1,
                "explanation": "Kwatha/Kashaya preparations boil medicinal herbs in water, utilizing water as the polar solvent to extract water-soluble plant principles."
            }
        ]
    },
    {
        "id": 4,
        "tag": "Indian Pioneers",
        "title": "Asima Chatterjee & Plant Chemistry",
        "sim_id": "asima_chatterjee_lab_sim",
        "avatar_dialogue": "I am proud to honor Dr. Asima Chatterjee! She harnessed fractional solvent systems to isolate life-saving anti-epileptic and anti-malarial drugs from Indian flora.",
        "vocabulary": [
            {"word": "Prof. Asima Chatterjee", "definition": "Renowned Indian chemist (1917–2006) who pioneered the chemistry of natural plant alkaloids, coumarins, and medicinal solutions."},
            {"word": "Alkaloid", "definition": "A naturally occurring organic nitrogenous compound produced by plants, having potent pharmacological effects on humans."},
            {"word": "Ayush-56", "definition": "An anti-epileptic drug formulation developed by Dr. Chatterjee from the medicinal plant Marsilea minuta."},
            {"word": "Fractional Extraction", "definition": "Using solvents of differing polarities (petroleum ether, chloroform, alcohol) to separate complex chemical mixtures."}
        ],
        "theory": r"""
          <p><strong>Professor Asima Chatterjee (1917–2006)</strong> was a luminary in the chemical sciences:</p>
          <ul>
            <li><strong>Historic Milestones:</strong> She was the <em>first woman</em> to be awarded a Doctorate of Science ($\text{D.Sc.}$) by an Indian university (University of Calcutta, 1944). She later received the prestigious Shanti Swarup Bhatnagar Award and the Padma Bhushan.</li>
            <li><strong>Mastery of Solvents:</strong> Dr. Chatterjee extensively used solutions and solvent extraction techniques to isolate bioactive alkaloids from indigenous plants such as <em>Rauvolfia serpentina</em> (Sarpagandha), <em>Vinca rosea</em> (periwinkle), and <em>Marsilea minuta</em>.</li>
            <li><strong>Therapeutic Breakthroughs:</strong> Her research yielded <strong>Ayush-56</strong>, an acclaimed anti-epileptic drug, and potent anti-malarial medications, bridging ancient Ayurvedic wisdom with rigorous modern analytical chemistry.</li>
          </ul>
        """,
        "checkpoints": [
            {
                "question": "Which historic academic distinction was achieved by renowned chemist Dr. Asima Chatterjee in 1944?",
                "options": [
                    "A. First Indian woman to climb Mount Everest",
                    "B. First woman to receive a Doctorate of Science (D.Sc.) from an Indian university",
                    "C. First woman to pilot an Indian commercial aircraft",
                    "D. Inventor of artificial plastic fibers"
                ],
                "correct": 1,
                "explanation": "Dr. Asima Chatterjee was the first woman to earn a Doctorate of Science (D.Sc.) from an Indian university (Calcutta University, 1944) for her work on plant alkaloids."
            },
            {
                "question": "What fundamental chemical technique did Dr. Asima Chatterjee utilize to extract anti-epileptic compounds from medicinal plants?",
                "options": [
                    "A. Magnetically attracting plant leaves",
                    "B. Solvent extraction and differential solubility in liquid solutions",
                    "C. High-voltage electrocution of dry roots",
                    "D. Freezing plants in solid ice blocks"
                ],
                "correct": 1,
                "explanation": "She utilized solvent extraction techniques, exploiting differing solubilities across solvents to isolate pure bioactive medicinal alkaloids."
            }
        ]
    },
    {
        "id": 5,
        "tag": "Indigenous Heritage",
        "title": "Ningel Salt Wells of Manipur",
        "sim_id": "manipur_salt_wells_sim",
        "avatar_dialogue": "In Ningel village of Manipur, women have practiced the science of evaporation and crystallization for centuries, boiling brine from ancient salt wells into sacred salt cakes!",
        "vocabulary": [
            {"word": "Ningel Salt Wells", "definition": "Ancient underground natural saline water wells located in Ningel village, Thoubal district, Manipur."},
            {"word": "Salt Cakes (Thum)", "definition": "Round, flat solidified circular cakes of crystallized salt, traditionally molded and wrapped in banana leaves."},
            {"word": "Thermal Crystallization", "definition": "The process of evaporating the solvent (water) through continuous boiling until the solute (salt) crystallizes out of solution."}
        ],
        "theory": r"""
          <p>In <strong>Ningel village (Thoubal district, Manipur)</strong>, an indigenous scientific tradition has flourished for hundreds of years:</p>
          <ul>
            <li><strong>Natural Saline Wells:</strong> Underground aquifers in this inland region produce highly concentrated salty brine water, drawn up by local village women.</li>
            <li><strong>Boiling Down the Solution:</strong> The brine is poured into massive flat shallow metal pans heated continuously over firewood furnaces. As water (the solvent) evaporates as steam, the solution surpasses its saturation limit.</li>
            <li><strong>Molding Salt Cakes:</strong> The concentrated slurry precipitates glistening salt crystals. While still warm and pliable, the salt is pressed into circular round cakes, dried, and wrapped in banana leaves and cloth for trade, culinary use, and sacred Manipuri rituals.</li>
          </ul>
        """,
        "checkpoints": [
            {
                "question": "In Ningel village of Manipur, what physical process is used to recover solid salt from the subterranean well brine?",
                "options": [
                    "A. Magnetic filtration",
                    "B. Thermal evaporation of the liquid solvent (water)",
                    "C. Condensation of atmospheric fog",
                    "D. Centrifugal shaking in plastic tubes"
                ],
                "correct": 1,
                "explanation": "Boiling the saline well water evaporates the solvent (water), causing the dissolved solute (salt) to crystallize into solid cakes."
            },
            {
                "question": "Why does solid salt precipitate in the metal pans during the Ningel salt-making process?",
                "options": [
                    "A. As water evaporates, the remaining solution exceeds its saturation limit, forcing excess salt to crystallize",
                    "B. The pan dissolves into the liquid water",
                    "C. Fire produces chemical salt atoms out of nothing",
                    "D. Salt turns into a lighter gas"
                ],
                "correct": 0,
                "explanation": "Removing the solvent by boiling concentrates the solution beyond saturation, driving the crystallization of solid salt."
            }
        ]
    },
    {
        "id": 6,
        "tag": "Saturation Dynamics",
        "title": "Saturated & Unsaturated Solutions",
        "sim_id": "saturated_unsaturated_sim",
        "avatar_dialogue": "Add one spoonful of salt—it vanishes! Keep adding spoonful after spoonful, and eventually no more dissolves. That is the exact boundary between unsaturated and saturated solutions!",
        "vocabulary": [
            {"word": "Unsaturated Solution", "definition": "A solution in which more solute can be dissolved at a given temperature."},
            {"word": "Saturated Solution", "definition": "A solution that has dissolved the maximum possible amount of solute at a given temperature; any additional solute settles undissolved."},
            {"word": "Undissolved Residue", "definition": "Excess solid solute resting at the bottom of a container because all interparticle solvent spaces are occupied."}
        ],
        "theory": r"""
          <p>Every solvent at a specific temperature has a finite capacity to accommodate solute particles:</p>
          <ul>
            <li><strong>Unsaturated State:</strong> When you add a teaspoon of salt to $100\text{ mL}$ of water at $20^\circ\text{C}$, ample empty spaces exist between water molecules. The solution can readily dissolve more salt; it is <strong>unsaturated</strong>.</li>
            <li><strong>Dynamic Saturation Limit:</strong> As you continue adding salt with constant stirring, the intermolecular gaps become completely occupied by dissolved hydrated ions.</li>
            <li><strong>Saturated State:</strong> Once approximately $36\text{ g}$ of $\text{NaCl}$ dissolves in $100\text{ mL}$ of water at $20^\circ\text{C}$, the solution reaches its limit. Adding even half a gram more results in solid salt grains settling at the bottom. The solution is now <strong>saturated</strong>.</li>
          </ul>
          <div style="background: rgba(16, 185, 129, 0.1); border-left: 3px solid #10b981; padding: 0.6rem 0.85rem; border-radius: 4px; margin-top: 0.5rem;">
            $$\text{Unsaturated Solution} \xrightarrow{+\text{More Solute Until Limit}} \text{Saturated Solution} \xrightarrow{+\text{Extra Solute}} \text{Precipitate at Bottom}$$
          </div>
        """,
        "checkpoints": [
            {
                "question": "What defines an unsaturated solution at 25°C?",
                "options": [
                    "A. It can no longer dissolve any additional solute",
                    "B. It has reached its absolute maximum solubility limit",
                    "C. It is capable of dissolving more solute at that temperature",
                    "D. It contains only gaseous molecules"
                ],
                "correct": 2,
                "explanation": "An unsaturated solution contains less than the maximum possible amount of solute, meaning more solute can dissolve at that specific temperature."
            },
            {
                "question": "You add a spoon of sugar to a cup of tea and stir vigorously, but sugar grains remain settled at the bottom. What is the state of the tea solution?",
                "options": [
                    "A. Unsaturated",
                    "B. Saturated",
                    "C. Pure solvent",
                    "D. Immiscible emulsion"
                ],
                "correct": 1,
                "explanation": "When excess solid solute can no longer dissolve and remains at the bottom, the solution has reached saturation at that temperature."
            }
        ]
    },
    {
        "id": 7,
        "tag": "Concentration Scales",
        "title": "Solute Concentration Levels",
        "sim_id": "solution_concentration_sim",
        "avatar_dialogue": "Concentration is all about proportion! A single drop of food coloring in a bucket creates a dilute solution; ten drops in a small glass produces a deeply concentrated solution.",
        "vocabulary": [
            {"word": "Concentration", "definition": "The exact amount of solute present in a specified quantity (mass or volume) of solution or solvent."},
            {"word": "Dilute Solution", "definition": "A solution that contains a relatively small quantity of solute dissolved in a large amount of solvent."},
            {"word": "Concentrated Solution", "definition": "A solution that contains a relatively large quantity of solute dissolved in a given amount of solvent."},
            {"word": "Mass by Volume %", "definition": "Concentration expressed as grams of solute per 100 mL of solution: $\\frac{\\text{Mass of Solute}}{\\text{Volume of Solution}} \\times 100$."}
        ],
        "theory": r"""
          <p><strong>Concentration</strong> describes the relative crowding of solute particles within a solvent:</p>
          <ul>
            <li><strong>Qualitative Comparison:</strong>
              <ul>
                <li><strong>Dilute:</strong> A pinch of potassium permanganate in a liter of water yields a faint pink color—few solute particles per unit volume.</li>
                <li><strong>Concentrated:</strong> A tablespoon of potassium permanganate in $100\text{ mL}$ of water yields an intense dark violet liquid—densely packed solute particles.</li>
              </ul>
            </li>
            <li><strong>Quantitative Measurement:</strong> In science, concentration is measured accurately through mass-by-mass or mass-by-volume percentages:
              $$\text{Concentration (Mass/Volume \%)} = \frac{\text{Mass of Solute (g)}}{\text{Volume of Solution (mL)}} \times 100$$
            </li>
            <li><strong>Dilution Principle:</strong> Adding more solvent to a concentrated solution decreases its concentration without changing the total mass of the solute.</li>
          </ul>
        """,
        "checkpoints": [
            {
                "question": "If 10 g of salt is dissolved in water to make 200 mL of brine solution, what is its mass-by-volume concentration percentage?",
                "options": [
                    "A. 2%",
                    "B. 5%",
                    "C. 10%",
                    "D. 20%"
                ],
                "correct": 1,
                "explanation": "Concentration = (10 g / 200 mL) × 100 = 5% (w/v)."
            },
            {
                "question": "What happens to the concentration of a sweet drink if you pour an extra glass of plain water into it?",
                "options": [
                    "A. Concentration increases",
                    "B. Concentration decreases (it becomes more dilute)",
                    "C. The total mass of dissolved sugar decreases",
                    "D. The solution instantly turns into a solid"
                ],
                "correct": 1,
                "explanation": "Adding more solvent increases total volume while solute mass remains constant, reducing the concentration (dilution)."
            }
        ]
    },
    {
        "id": 8,
        "tag": "Solubility Dynamics",
        "title": "Solubility & Thermal Influence",
        "sim_id": "solubility_temperature_sim",
        "avatar_dialogue": "Watch this beaker: salt settles at the bottom at room temperature. But turn on the Bunsen burner, and all the excess salt magically dissolves! Heat expands solubility for most solids.",
        "vocabulary": [
            {"word": "Solubility", "definition": "The maximum amount of solute (in grams) that can dissolve in 100 mL (or 100 g) of a solvent at a specific temperature."},
            {"word": "Thermal Kinetic Energy", "definition": "The heat energy that increases molecular vibrations, expanding intermolecular spaces and breaking solute lattices faster."},
            {"word": "Recrystallization", "definition": "The reformation of solid crystals when a hot, saturated solution cools down to a lower temperature."}
        ],
        "theory": r"""
          <p><strong>Solubility</strong> is an intrinsic property that depends heavily on temperature:</p>
          <ul>
            <li><strong>Standard Definition:</strong> Solubility is defined as the maximum mass (in grams) of solute that dissolves in $100\text{ mL}$ of water at a specified temperature:
              $$\text{Solubility of Sugar at } 20^\circ\text{C} \approx 204\text{ g / } 100\text{ mL}$$
              $$\text{Solubility of Sugar at } 100^\circ\text{C} \approx 487\text{ g / } 100\text{ mL}$$
            </li>
            <li><strong>Effect of Temperature on Solids:</strong> For the vast majority of solid solutes (sugar, potassium nitrate, copper sulfate), <strong>solubility increases as temperature rises</strong>. Heat increases the kinetic motion of solvent molecules, creating larger transient gaps between them and overcoming solute-solute crystal bonds.</li>
            <li><strong>Thermal Transition:</strong> A saturated solution with settled solute at $25^\circ\text{C}$ becomes <strong>unsaturated</strong> upon heating. When cooled back down, the excess solute precipitates out as pure glittering crystals!</li>
          </ul>
        """,
        "checkpoints": [
            {
                "question": "How does heating a liquid solvent typically affect the solubility of solid solutes like sugar or potassium nitrate?",
                "options": [
                    "A. Solubility decreases to zero",
                    "B. Solubility remains exactly unchanged",
                    "C. Solubility increases",
                    "D. Solid turns into gaseous nitrogen"
                ],
                "correct": 2,
                "explanation": "Thermal energy increases solvent molecular motion and interparticle spaces, allowing more solid solute to dissolve."
            },
            {
                "question": "A beaker contains a saturated sugar solution with solid sugar resting at the bottom at 20°C. If the beaker is heated to 70°C without adding water, what will happen?",
                "options": [
                    "A. More sugar will precipitate out",
                    "B. The settled sugar will dissolve, and the solution becomes unsaturated at 70°C",
                    "C. Water will freeze into solid ice",
                    "D. Sugar will turn into metallic iron"
                ],
                "correct": 1,
                "explanation": "Because solid solubility increases with temperature, heating makes the solution unsaturated relative to 70°C, causing the settled sugar to dissolve."
            }
        ]
    },
    {
        "id": 9,
        "tag": "Gas Solubility",
        "title": "Dissolved Oxygen & Aquatic Life",
        "sim_id": "gas_solubility_temp_sim",
        "avatar_dialogue": "Here is a surprising reversal of physics! While solids dissolve better in hot water, gases dissolve much better in icy cold water. That is why trout and salmon thrive in cold mountain streams!",
        "vocabulary": [
            {"word": "Dissolved Oxygen (DO)", "definition": "Microscopic oxygen gas (O₂) molecules dispersed uniformly within liquid water, essential for aquatic respiration."},
            {"word": "Thermal Gas Inversion", "definition": "The scientific principle stating that gas solubility in liquids decreases as temperature increases."},
            {"word": "Aquatic Respiration", "definition": "The physiological process whereby fish and aquatic organisms extract dissolved oxygen through gill filaments."}
        ],
        "theory": r"""
          <p>Gases behave very differently from solids when dissolving in liquids:</p>
          <ul>
            <li><strong>Gas Dissolution in Water:</strong> Atmospheric gases like oxygen ($\text{O}_2$) and carbon dioxide ($\text{CO}_2$) dissolve in water to a small but vital extent (approximately $8\text{ to }14\text{ mg/L}$ depending on temperature). Fish and aquatic creatures breathe this <em>dissolved oxygen</em> using specialized gills.</li>
            <li><strong>Temperature Inversion Law:</strong> Unlike solids, <strong>the solubility of gases in liquids decreases as temperature rises</strong>!
              $$\text{Temperature } \uparrow \quad \Longrightarrow \quad \text{Gas Solubility } \downarrow$$
            </li>
            <li><strong>Physical Cause:</strong> Heating imparts high kinetic energy to gas molecules dissolved in the liquid, causing them to overcome weak solvent attractions and escape back into the atmosphere as bubbles.</li>
            <li><strong>Ecological Consequence:</strong> Cold mountain streams hold abundant dissolved oxygen, supporting active fish. When industrial factories release warm thermal effluent into rivers (thermal pollution), dissolved oxygen plummets, causing fish suffocation.</li>
          </ul>
        """,
        "checkpoints": [
            {
                "question": "Why do fish find it significantly easier to survive in cold river waters compared to warm summer ponds?",
                "options": [
                    "A. Cold water contains zero dissolved salt",
                    "B. Cold water holds a higher concentration of dissolved oxygen than warm water",
                    "C. Fish do not need oxygen in cold weather",
                    "D. Warm water freezes fish gills instantly"
                ],
                "correct": 1,
                "explanation": "Gas solubility decreases with rising temperature; cold water dissolves and retains more oxygen than warm water."
            },
            {
                "question": "What happens to the dissolved gas when a cold bottle of carbonated soda is opened and allowed to warm up in the sun?",
                "options": [
                    "A. More gas dissolves into the soda",
                    "B. Dissolved CO₂ gas bubbles escape rapidly into the air, making the soda go flat",
                    "C. Soda turns into pure diamond crystals",
                    "D. Gas solubility increases by 500%"
                ],
                "correct": 1,
                "explanation": "As the liquid warms, the solubility of CO₂ gas drops sharply, driving gas bubbles out of solution and leaving the soda flat."
            }
        ]
    },
    {
        "id": 10,
        "tag": "Density Fundamentals",
        "title": "Density: Mass per Unit Volume",
        "sim_id": "density_mass_volume_sim",
        "avatar_dialogue": "Which is heavier: a kilogram of iron or a kilogram of cotton? Both have identical mass! But iron occupies a tiny volume because its density is far greater.",
        "vocabulary": [
            {"word": "Density (ρ)", "definition": "The mass of a substance contained within a unit volume: $\\text{Density} = \\frac{\\text{Mass}}{\\text{Volume}}$."},
            {"word": "SI Unit of Density", "definition": "Kilograms per cubic metre ($\\text{kg/m}^3$). In laboratory chemistry, grams per cubic centimetre ($\\text{g/cm}^3$) or $\\text{g/mL}$ is widely used."},
            {"word": "Relative Density", "definition": "The ratio of a substance's density to the density of pure water at $4^\\circ\\text{C}$ (a dimensionless pure number)."}
        ],
        "theory": r"""
          <p><strong>Density</strong> describes the compactness of matter within an object:</p>
          <div style="background: rgba(14, 165, 233, 0.1); border-left: 3px solid #38bdf8; padding: 0.6rem 0.85rem; border-radius: 4px; margin-bottom: 0.75rem;">
            $$\text{Density } (d\text{ or }\rho) = \frac{\text{Mass } (m)}{\text{Volume } (V)}$$
          </div>
          <ul>
            <li><strong>Intrinsic Characteristic:</strong> Density is an intrinsic physical property. A tiny iron nail and a gigantic iron anchor have the exact same density ($\approx 7.87\text{ g/cm}^3$) because mass and volume scale proportionally!</li>
            <li><strong>Units of Measurement:</strong>
              <ul>
                <li><strong>SI Unit:</strong> $\text{kg/m}^3$ ($1\text{ g/cm}^3 = 1000\text{ kg/m}^3$).</li>
                <li><strong>Common Lab Units:</strong> $\text{g/cm}^3$ for solids and $\text{g/mL}$ for liquids ($1\text{ cm}^3 = 1\text{ mL}$). Pure water has a density of $1.0\text{ g/cm}^3 = 1.0\text{ g/mL} = 1000\text{ kg/m}^3$.</li>
              </ul>
            </li>
            <li><strong>Relative Density (Specific Gravity):</strong>
              $$\text{Relative Density} = \frac{\text{Density of Substance}}{\text{Density of Water at } 4^\circ\text{C}}$$
              Because it is a ratio of identical units, relative density has <strong>no units</strong>! For example, aluminium's relative density is $2.7$ (meaning it is $2.7\times$ denser than water).
            </li>
          </ul>
        """,
        "checkpoints": [
            {
                "question": "An iron block has a mass of 156 g and occupies a volume of 20 cm³. What is the density of iron?",
                "options": [
                    "A. 3.12 g/cm³",
                    "B. 7.8 g/cm³",
                    "C. 15.6 g/cm³",
                    "D. 78.0 g/cm³"
                ],
                "correct": 1,
                "explanation": "Density = Mass / Volume = 156 g / 20 cm³ = 7.8 g/cm³."
            },
            {
                "question": "What is the unit of Relative Density?",
                "options": [
                    "A. kg/m³",
                    "B. g/cm³",
                    "C. g/mL",
                    "D. It is a dimensionless ratio with no units"
                ],
                "correct": 3,
                "explanation": "Relative density divides the density of a substance by the density of water; because the units cancel out, it is a pure dimensionless number."
            }
        ]
    },
    {
        "id": 11,
        "tag": "Measurement Protocols",
        "title": "Measuring Mass & Volume Precision",
        "sim_id": "mass_volume_measurement_sim",
        "avatar_dialogue": "Precision is the heartbeat of science! Mass is measured with balances in grams, while liquid volume is measured with calibrated cylinders in milliliters.",
        "vocabulary": [
            {"word": "Mass", "definition": "The fundamental measure of the amount of matter inside an object, measured in grams (g) or kilograms (kg). Invariant across gravity."},
            {"word": "Weight", "definition": "The downward gravitational force exerted on an object: $W = mg$, measured in newtons (N). Changes with planetary gravity."},
            {"word": "Volume", "definition": "The three-dimensional spatial extent occupied by matter, measured in litres (L), millilitres (mL), or cubic centimetres (cm³)."}
        ],
        "theory": r"""
          <p>Accurate density calculation demands rigorous measurement of its two component parameters: <strong>mass</strong> and <strong>volume</strong>.</p>
          <ul>
            <li><strong>Mass vs. Weight:</strong>
              <ul>
                <li><strong>Mass ($m$):</strong> Measured using an electronic analytical balance or beam balance. It represents the quantity of matter and never changes, whether on Earth, on the Moon, or in deep space.</li>
                <li><strong>Weight ($W$):</strong> The gravitational pull ($W = mg$) acting downward. A $60\text{ kg}$ student weighs $\approx 588\text{ N}$ on Earth but only $\approx 98\text{ N}$ on the Moon!</li>
              </ul>
            </li>
            <li><strong>Volume Measurements:</strong>
              <ul>
                <li>$1\text{ Litre (L)} = 1000\text{ mL} = 1000\text{ cm}^3 = 0.001\text{ m}^3$.</li>
                <li>$1\text{ Millilitre (mL)} = 1\text{ cm}^3$ ($1\text{ cc}$).</li>
              </ul>
            </li>
            <li><strong>Measuring Cylinders:</strong> Specially engineered glassware designed tall and narrow so that small changes in volume produce substantial vertical shifts in the liquid level, maximizing reading sensitivity.</li>
          </ul>
        """,
        "checkpoints": [
            {
                "question": "Which instrument is used to determine the mass of a solid chemical sample in the laboratory?",
                "options": [
                    "A. Calibrated thermometer",
                    "B. Electronic digital balance",
                    "C. Glass measuring cylinder",
                    "D. Barometer"
                ],
                "correct": 1,
                "explanation": "An electronic digital balance or beam balance measures the mass of a sample in grams or kilograms."
            },
            {
                "question": "How are 1 millilitre (mL) and 1 cubic centimetre (cm³) related in scientific volume measurement?",
                "options": [
                    "A. 1 mL = 1000 cm³",
                    "B. 1 mL = 0.01 cm³",
                    "C. 1 mL is exactly equal to 1 cm³",
                    "D. They measure two completely unrelated physical quantities"
                ],
                "correct": 2,
                "explanation": "By definition, 1 millilitre (mL) equals exactly 1 cubic centimetre (cm³)."
            }
        ]
    },
    {
        "id": 12,
        "tag": "Laboratory Techniques",
        "title": "The Meniscus & Reading Accuracy",
        "sim_id": "meniscus_reading_lab_sim",
        "avatar_dialogue": "Notice how water curves inside a narrow glass tube! That curve is called a meniscus. Always align your eye level with the bottom of the curve to eliminate parallax error.",
        "vocabulary": [
            {"word": "Meniscus", "definition": "The curved upper surface of a liquid column caused by the balance between adhesive forces (liquid to glass) and cohesive forces (liquid to liquid)."},
            {"word": "Concave Meniscus", "definition": "A downward-curving surface formed by water where adhesive forces exceed cohesive forces; read at the lowest central point."},
            {"word": "Convex Meniscus", "definition": "An upward-curving surface formed by mercury where cohesive forces exceed adhesive forces; read at the highest point."},
            {"word": "Parallax Error", "definition": "An optical reading error occurring when your line of sight is angled above or below the plane of the meniscus."}
        ],
        "theory": r"""
          <p>Whenever liquid is poured into a narrow measuring cylinder, surface tension curves the liquid surface into a <strong>meniscus</strong>:</p>
          <ul>
            <li><strong>Colorless & Transparent Liquids (Water):</strong> Water molecules adhere strongly to glass walls (adhesion $>$ cohesion), forming a <strong>concave meniscus</strong> (curved downward like a shallow bowl).
              <div style="background: rgba(14, 165, 233, 0.1); border-left: 3px solid #38bdf8; padding: 0.5rem 0.8rem; margin: 0.4rem 0; border-radius: 4px;">
                <strong>Standard Scientific Rule:</strong> Always position your eye strictly horizontal to the scale and take the reading at the <strong>bottom of the meniscus</strong>!
              </div>
            </li>
            <li><strong>Colored & Opaque Liquids:</strong> For deeply colored solutions (like potassium permanganate or dark iodine) where the bottom curve is obscured, the reading is taken at the <strong>top of the meniscus</strong>.</li>
            <li><strong>Avoiding Parallax Error:</strong> Looking from above causes you to overestimate the volume; looking from below causes you to underestimate it. Eye level must align exactly with the meniscus plane.</li>
          </ul>
        """,
        "checkpoints": [
            {
                "question": "When measuring the volume of colorless pure water in a graduated cylinder, where should your eye take the reading?",
                "options": [
                    "A. At the upper edges touching the glass wall",
                    "B. At the bottom of the concave meniscus at eye level",
                    "C. Looking down from above the cylinder mouth",
                    "D. Looking upward from below the table bench"
                ],
                "correct": 1,
                "explanation": "For transparent liquids forming a concave meniscus, the accurate volume reading is taken horizontally at the bottom of the curved meniscus to avoid parallax error."
            },
            {
                "question": "What error occurs if your eyes are tilted above the meniscus line while reading a measuring cylinder?",
                "options": [
                    "A. Zero error",
                    "B. Parallax error, leading to an incorrect volume measurement",
                    "C. Thermal error",
                    "D. Gravitational error"
                ],
                "correct": 1,
                "explanation": "Viewing from an angle above or below eye level introduces parallax error, skewing the recorded volume."
            }
        ]
    },
    {
        "id": 13,
        "tag": "Volume Determination",
        "title": "Regular Shapes & Water Displacement",
        "sim_id": "water_displacement_volume_sim",
        "avatar_dialogue": "How do you find the volume of an irregular stone? You cannot use a ruler! Instead, drop it into water and watch the water rise. The volume displaced equals the volume of the stone!",
        "vocabulary": [
            {"word": "Geometric Volume", "definition": "Volume calculated mathematically for regular solids using standard formulas ($V = l \\times w \\times h$ for cuboids; $V = \\frac{4}{3}\\pi r^3$ for spheres)."},
            {"word": "Water Displacement Method", "definition": "A laboratory technique to measure the volume of irregular insoluble solids by measuring the volume of liquid they push aside."},
            {"word": "Displaced Volume", "definition": "The difference between the final water level and initial water level: $V = V_{\\text{final}} - V_{\\text{initial}}$."}
        ],
        "theory": r"""
          <p>Depending on geometry, solids require different volume measurement methods:</p>
          <ol>
            <li><strong>Regular Geometric Shapes:</strong> Regular objects with defined flat or spherical boundaries are measured with rulers or vernier callipers and calculated algebraically:
              $$\text{Cuboid: } V = \text{length } (l) \times \text{width } (w) \times \text{height } (h)$$
              $$\text{Sphere: } V = \frac{4}{3}\pi r^3 \qquad \text{Cylinder: } V = \pi r^2 h$$
            </li>
            <li><strong>Irregular Solids (Water Displacement Method):</strong>
              <ul>
                <li>Pour water into a measuring cylinder and note the initial volume ($V_1$).</li>
                <li>Tie the irregular stone or metal key with a thin thread and gently submerge it completely beneath the water surface.</li>
                <li>Record the new, elevated water level ($V_2$).</li>
                <li>The volume of the irregular solid equals the displaced water:
                  $$V_{\text{solid}} = V_2 - V_1$$
                </li>
              </ul>
            </li>
          </ol>
        """,
        "checkpoints": [
            {
                "question": "A measuring cylinder contains 50 mL of water. When an irregular pebble is gently lowered into the cylinder, the water level rises to 68 mL. What is the volume of the pebble?",
                "options": [
                    "A. 118 cm³",
                    "B. 50 cm³",
                    "C. 18 cm³",
                    "D. 8 cm³"
                ],
                "correct": 2,
                "explanation": "Volume of solid = Final level - Initial level = 68 mL - 50 mL = 18 mL = 18 cm³."
            },
            {
                "question": "A wooden block has a length of 5 cm, width of 4 cm, and height of 2 cm. What is its volume?",
                "options": [
                    "A. 11 cm³",
                    "B. 20 cm³",
                    "C. 40 cm³",
                    "D. 80 cm³"
                ],
                "correct": 2,
                "explanation": "Volume of cuboid = length × width × height = 5 cm × 4 cm × 2 cm = 40 cm³."
            }
        ]
    },
    {
        "id": 14,
        "tag": "Environmental Influences",
        "title": "Temperature & Pressure on Density",
        "sim_id": "temp_pressure_density_sim",
        "avatar_dialogue": "Watch a hot air balloon soar! As the burner heats the trapped air, the particles spread out, volume expands, density drops, and buoyant upthrust lifts it into the sky!",
        "vocabulary": [
            {"word": "Thermal Expansion", "definition": "The increase in volume of a substance when heated, while its mass remains constant, resulting in decreased density."},
            {"word": "Buoyant Lift", "definition": "The net upward force exerted by a denser surrounding fluid on an object of lower density."},
            {"word": "Compressibility", "definition": "The capacity of a substance to decrease in volume under applied external pressure; very high in gases, virtually zero in liquids and solids."}
        ],
        "theory": r"""
          <p>Density is not a static constant; it shifts with ambient temperature and pressure:</p>
          <ul>
            <li><strong>Effect of Temperature on Density:</strong>
              <ul>
                <li>When any typical substance is heated, its constituent particles absorb thermal energy and vibrate vigorously, increasing interparticle spacing.</li>
                <li>Because mass remains constant while volume expands, <strong>heating decreases density</strong>:
                  $$\text{Temperature } \uparrow \quad \Longrightarrow \quad \text{Volume } \uparrow \quad \Longrightarrow \quad \text{Density } \downarrow$$
                </li>
                <li><strong>Hot Air Balloons:</strong> Burners heat the air inside the nylon envelope. The warm air expands, spills excess mass out the bottom, and becomes significantly less dense than the cooler surrounding atmosphere, floating upward!</li>
              </ul>
            </li>
            <li><strong>Effect of Pressure on Density:</strong>
              <ul>
                <li><strong>Gases:</strong> Particles are separated by immense empty voids. Increasing pressure forces particles tightly together, dramatically decreasing volume and increasing density!</li>
                <li><strong>Liquids & Solids:</strong> Particles are already touching tightly; increasing pressure has a negligible, nearly imperceptible effect on their volume or density (incompressible).</li>
              </ul>
            </li>
          </ul>
        """,
        "checkpoints": [
            {
                "question": "Why does a hot air balloon rise upward into the morning sky when its propane burner is fired?",
                "options": [
                    "A. Hot air is heavier than cold air",
                    "B. Heating causes the air inside to expand and become less dense than the cooler surrounding air",
                    "C. Fire creates an anti-gravity magnetic field",
                    "D. Burning propane destroys Earth's gravity"
                ],
                "correct": 1,
                "explanation": "Heating expands the air inside the envelope, reducing its density below that of the surrounding cool atmospheric air and creating net upward buoyancy."
            },
            {
                "question": "How does increasing external pressure affect the density of a trapped volume of gas compared to a solid steel ball?",
                "options": [
                    "A. Gas density increases significantly, while steel density remains virtually unchanged",
                    "B. Steel density increases dramatically, while gas density drops to zero",
                    "C. Both change density by exactly 500%",
                    "D. Pressure has zero effect on any gas"
                ],
                "correct": 0,
                "explanation": "Gases are highly compressible, so pressure compresses their volume and increases their density; solids are virtually incompressible."
            }
        ]
    },
    {
        "id": 15,
        "tag": "Anomalous Physics",
        "title": "Anomalous Expansion of Water & Ice",
        "sim_id": "water_ice_anomalous_sim",
        "avatar_dialogue": "Water exhibits one of nature's greatest miracles: anomalous expansion! Water reaches maximum density at 4°C. When freezing into ice at 0°C, it expands, causing ice to float and saving aquatic life!",
        "vocabulary": [
            {"word": "Anomalous Expansion", "definition": "The unusual property of water whereby it contracts on heating from 0°C to 4°C, and expands on cooling from 4°C to 0°C."},
            {"word": "Maximum Density Point", "definition": "Water reaches its absolute maximum density of 1.000 g/cm³ at exactly 4°C."},
            {"word": "Open Hexagonal Lattice", "definition": "The spacious crystal framework adopted by frozen ice molecules held by hydrogen bonds, creating large internal voids."},
            {"word": "Insulating Ice Blanket", "definition": "Floating surface ice that shields deeper lake water from sub-zero air, keeping water at 4°C underneath."}
        ],
        "theory": r"""
          <p>Almost all liquids contract and become denser as they freeze. Water is a miraculous exception to this rule due to <strong>hydrogen bonding</strong>:</p>
          <ul>
            <li><strong>Thermal Curve of Water:</strong>
              <ul>
                <li>As warm water cools down toward $4^\circ\text{C}$, it contracts normally, reaching its <strong>maximum density ($1.0000\text{ g/cm}^3$) at exactly $4^\circ\text{C}$</strong>.</li>
                <li>Below $4^\circ\text{C}$, water begins to expand! From $4^\circ\text{C}$ down to $0^\circ\text{C}$, water expands continuously as hydrogen bonds start locking molecules into fixed orientations.</li>
              </ul>
            </li>
            <li><strong>The Structure of Ice:</strong> When liquid water freezes into solid ice at $0^\circ\text{C}$, the water molecules lock into an <strong>open, cage-like hexagonal lattice</strong> with vast empty voids. This causes the volume to expand by $\approx 9\%$, dropping ice's density to $\approx 0.917\text{ g/cm}^3$.</li>
            <li><strong>Life-Saving Ecology:</strong> Because ice is less dense than liquid water, <strong>ice floats on top of ponds and lakes</strong>. This floating surface ice acts as a thermal insulator, preventing the underlying water from freezing and maintaining liquid water at $4^\circ\text{C}$ at the lake bottom, preserving aquatic life through bitter winters!</li>
          </ul>
        """,
        "checkpoints": [
            {
                "question": "At what temperature does liquid water attain its maximum density?",
                "options": [
                    "A. -10°C",
                    "B. 0°C",
                    "C. 4°C",
                    "D. 100°C"
                ],
                "correct": 2,
                "explanation": "Liquid water reaches its maximum density of 1.000 g/cm³ at exactly 4°C due to its anomalous expansion curve."
            },
            {
                "question": "Why does solid ice float on liquid water rather than sinking to the lake bottom?",
                "options": [
                    "A. Ice contains trapped bubbles of helium gas",
                    "B. Molecules in ice lock into an open hexagonal lattice with larger volume, making ice less dense (~0.92 g/cm³) than water (1.0 g/cm³)",
                    "C. Ice is made of pure air",
                    "D. Gravity repels solid ice crystals"
                ],
                "correct": 1,
                "explanation": "The cage-like hexagonal crystal lattice of ice occupies more volume than liquid water, lowering ice's density to ~0.92 g/cm³ and allowing it to float."
            }
        ]
    },
    {
        "id": 16,
        "tag": "Planetary Geology",
        "title": "Earth's Density Stratification",
        "sim_id": "earth_density_layers_sim",
        "avatar_dialogue": "Journey deep beneath our feet! Earth is like an immense density sorting centrifuge: light rocks form the crust, while dense iron and nickel sank to form the core.",
        "vocabulary": [
            {"word": "Density Stratification", "definition": "The geological layering of a planet where denser materials sink toward the center while lighter materials float to the surface."},
            {"word": "Crust", "definition": "Earth's outermost brittle rock shell, composed mainly of low-density granitic and basaltic silicates (2.7 to 3.0 g/cm³)."},
            {"word": "Mantle", "definition": "The thick layer of dense silicate rock underneath the crust (3.3 to 5.7 g/cm³)."},
            {"word": "Core (Inner & Outer)", "definition": "The dense metallic center of Earth, composed of iron and nickel alloy under immense pressure (9.9 to 13.1 g/cm³)."}
        ],
        "theory": r"""
          <p>Earth's internal structure exhibits profound <strong>density stratification</strong> resulting from planetary differentiation during its molten infancy:</p>
          <ul>
            <li><strong>The Density Gradient:</strong>
              $$\text{Crust } (2.7\text{--}3.0\text{ g/cm}^3) \;\longrightarrow\; \text{Mantle } (3.3\text{--}5.7\text{ g/cm}^3) \;\longrightarrow\; \text{Outer Core } (9.9\text{--}12.2\text{ g/cm}^3) \;\longrightarrow\; \text{Inner Core } (12.8\text{--}13.1\text{ g/cm}^3)$$
            </li>
            <li><strong>Geological Mechanics:</strong>
              <ul>
                <li><strong>Chemical Differentiation:</strong> When proto-Earth was completely molten, heavy, dense metallic elements (iron $\text{Fe}$ and nickel $\text{Ni}$) sank toward the gravitational center, while lighter silicates ($\text{Si}, \text{Al}, \text{Mg}$) floated to form the mantle and crust.</li>
                <li><strong>Gravitational Compaction:</strong> Escalating overburden pressure (exceeding $3.6\text{ million atmospheres}$ at the center) further compresses the crystalline lattice of the solid inner core, driving its density up to $13.1\text{ g/cm}^3$!</li>
              </ul>
            </li>
          </ul>
        """,
        "checkpoints": [
            {
                "question": "Which layer of the Earth possesses the highest density?",
                "options": [
                    "A. Continental Crust (~2.7 g/cm³)",
                    "B. Oceanic Crust (~3.0 g/cm³)",
                    "C. Upper Mantle (~3.4 g/cm³)",
                    "D. Solid Inner Core (~13.1 g/cm³)"
                ],
                "correct": 3,
                "explanation": "Earth's inner core has the highest density (~13.1 g/cm³) due to its dense iron-nickel metallic composition and immense gravitational compaction."
            },
            {
                "question": "What primary physical process caused heavy iron and nickel to concentrate at Earth's core while silicates formed the surface crust?",
                "options": [
                    "A. Density differentiation in molten proto-Earth, where denser materials sank and lighter rocks floated",
                    "B. Wind erosion blowing metal into caves",
                    "C. Ocean waves washing rocks onto continents",
                    "D. Plant roots absorbing iron downward"
                ],
                "correct": 0,
                "explanation": "During Earth's early molten phase, gravitational differentiation caused dense metals to sink to the core and lighter silicates to float upward."
            }
        ]
    },
    {
        "id": 17,
        "is_quiz_slide": True,
        "quiz_start_idx": 1,
        "quiz_count": 10,
        "title": "Mastery Challenge • Part I",
        "tag": "Mastery Quiz",
        "avatar_dialogue": "Welcome to Mastery Challenge Part I! Test your understanding of solutions, solvents, and the scientific contributions of Asima Chatterjee."
    },
    {
        "id": 18,
        "is_quiz_slide": True,
        "quiz_start_idx": 11,
        "quiz_count": 10,
        "title": "Mastery Challenge • Part II",
        "tag": "Mastery Quiz",
        "avatar_dialogue": "Outstanding work! Now let us conquer Mastery Challenge Part II, tackling saturation limits, concentration mathematics, and temperature effects."
    },
    {
        "id": 19,
        "is_quiz_slide": True,
        "quiz_start_idx": 21,
        "quiz_count": 10,
        "title": "Mastery Challenge • Part III",
        "tag": "Mastery Quiz",
        "avatar_dialogue": "Superb momentum! In Mastery Challenge Part III, we explore gas solubility, density equations, and meniscus reading protocols."
    },
    {
        "id": 20,
        "is_quiz_slide": True,
        "quiz_start_idx": 31,
        "quiz_count": 10,
        "title": "Mastery Challenge • Part IV",
        "tag": "Mastery Quiz",
        "avatar_dialogue": "The final frontier! Tackle water displacement, anomalous water expansion, floating ice physics, and Earth's planetary density layers."
    }
]

QUIZ_QUESTIONS = [
    {
        "id": 1,
        "concept": "Solution Homogeneity",
        "question": "Why is an aqueous solution of common salt classified scientifically as a homogeneous mixture?",
        "options": [
            "A. Because the salt particles settle at the bottom after standing for 5 minutes",
            "B. Because the solute particles distribute uniformly throughout the liquid and cannot be distinguished separately",
            "C. Because the salt chemically reacts with water to form chlorine gas",
            "D. Because the solution is opaque and reflects all light"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Definition of Homogeneous:</strong> A mixture is homogeneous when its constituent particles are uniformly dispersed at the molecular/ionic scale without phase boundaries.<br><strong>Step 2: Salt in Water:</strong> Na⁺ and Cl⁻ ions distribute uniformly among water molecules; every portion has identical properties and composition.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 2,
        "concept": "Solute vs Solvent",
        "question": "In a laboratory experiment, 5 g of iodine crystals are dissolved completely in 100 mL of ethanol to prepare tincture of iodine. Which is the solute?",
        "options": [
            "A. Ethanol",
            "B. Iodine",
            "C. Both iodine and ethanol are solvents",
            "D. Water"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Solid-Liquid Solution:</strong> When a solid dissolves in a liquid, the solid is the solute and the liquid is the solvent.<br><strong>Step 2: Identification:</strong> Iodine is the solid dissolved substance (solute); ethanol is the dissolving medium (solvent).<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 3,
        "concept": "Gulab Jamun Chashni",
        "question": "Why is water considered the solvent in Gulab Jamun chashni, even though 150 g of sugar dissolves in just 100 mL of water?",
        "options": [
            "A. Because water has a higher boiling point than sugar",
            "B. Because water determines the physical liquid state of the final solution",
            "C. Because sugar disappears and ceases to exist",
            "D. Because sugar is lighter than water"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Physical State Rule:</strong> When a solid dissolves in a liquid to form a liquid solution, the liquid component that maintains the solution's phase is defined as the solvent.<br><strong>Step 2: Application:</strong> Water maintains the liquid state of the syrup, so it remains the solvent despite sugar having greater mass.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 4,
        "concept": "Liquid-Liquid Solutions",
        "question": "A liquid mixture contains 80 mL of pure water and 20 mL of liquid glycerin. According to scientific convention, what is glycerin?",
        "options": [
            "A. The solvent",
            "B. The solute",
            "C. A suspension",
            "D. A precipitate"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Rule for Two Liquids:</strong> When two miscible liquids form a solution, the liquid in the smaller quantity is the solute, and the one in the larger quantity is the solvent.<br><strong>Step 2: Comparison:</strong> Glycerin is present in smaller volume (20 mL vs 80 mL water), making glycerin the solute.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 5,
        "concept": "Ayurvedic Solvents",
        "question": "In traditional Indian medicine, why are cow's ghee (Ghrita) and sesame oil used as solvents in Sneha Kalpana formulations?",
        "options": [
            "A. They act as lipophilic solvents to extract fat-soluble therapeutic phytochemicals",
            "B. They turn all herbs into pure alcohol",
            "C. They prevent the medicine from ever being digested",
            "D. They are completely solid at 100°C"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Polarity of Phyto-compounds:</strong> Many active botanical compounds are non-polar (lipophilic) and insoluble in water.<br><strong>Step 2: Lipid Solvents:</strong> Oils and ghee are non-polar lipid solvents that dissolve and deliver these fat-soluble actives across cellular membranes.<br><strong>Step 3: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 6,
        "concept": "Asima Chatterjee Contributions",
        "question": "Which major scientific recognition was bestowed upon Professor Asima Chatterjee for her groundbreaking work on natural plant alkaloids and solvent extraction?",
        "options": [
            "A. First woman Doctorate of Science (D.Sc.) from an Indian university and Shanti Swarup Bhatnagar Awardee",
            "B. Field Medal in Mathematics",
            "C. Commander of the British Navy",
            "D. Nobel Prize in Literature"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Historical Fact:</strong> Dr. Asima Chatterjee was the first woman to earn a D.Sc. from an Indian university (Calcutta University, 1944).<br><strong>Step 2: Honours:</strong> She won the Shanti Swarup Bhatnagar Award and Padma Bhushan for natural drug chemistry.<br><strong>Step 3: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 7,
        "concept": "Ayush-56 Drug",
        "question": "The anti-epileptic medicine 'Ayush-56' developed through the research of Dr. Asima Chatterjee was extracted from which Indian medicinal plant?",
        "options": [
            "A. Marsilea minuta",
            "B. Eucalyptus globulus",
            "C. Mangifera indica",
            "D. Oryza sativa"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Botanical Source:</strong> Ayush-56 was formulated by isolating bioactive alkaloids and coumarins from the aquatic fern <em>Marsilea minuta</em>.<br><strong>Step 2: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 8,
        "concept": "Ningel Manipur Salt Wells",
        "question": "What is the primary scientific principle used by women of Ningel village in Manipur to produce traditional salt cakes?",
        "options": [
            "A. Freezing water into glaciers",
            "B. Boiling underground saline brine to evaporate water and precipitate solid salt crystals",
            "C. Chemical electrolysis using car batteries",
            "D. Passing brine through paper sieves"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Process:</strong> Saline well water is boiled continuously in metal pans over wood fires.<br><strong>Step 2: Physical Principle:</strong> Evaporation of water (solvent) concentrates the solution past saturation, causing solid salt (solute) to crystallize.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 9,
        "concept": "Salt Cake Packaging",
        "question": "Traditional salt cakes of Ningel (Manipur) are historically wrapped in which sustainable natural material?",
        "options": [
            "A. Aluminum foil",
            "B. Banana leaves and cloth",
            "C. Polyethylene plastic sheets",
            "D. Waxed cardboard"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Cultural Practice:</strong> The circular salt cakes are traditionally packed and preserved using fresh banana leaves tied with cloth and bamboo fibers.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 10,
        "concept": "Heterogeneous vs Homogeneous",
        "question": "Which of the following mixtures will exhibit visible non-uniformity and settle into distinct layers over time?",
        "options": [
            "A. Chalk powder thoroughly shaken in water",
            "B. Salt dissolved in water",
            "C. Sugar dissolved in water",
            "D. Filtered clear apple juice"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Heterogeneous Mixture:</strong> Chalk powder does not dissolve in water; it forms an unstable suspension where particles settle under gravity.<br><strong>Step 2: Comparison:</strong> Salt and sugar form true homogeneous solutions that never settle.<br><strong>Step 3: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 11,
        "concept": "Unsaturated Definition",
        "question": "A solution contains 15 g of solute dissolved in 100 mL of solvent at 25°C. If its maximum solubility limit is 36 g at 25°C, how is the solution classified?",
        "options": [
            "A. Saturated",
            "B. Unsaturated",
            "C. Supersaturated precipitate",
            "D. Solid compound"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Capacity Comparison:</strong> Dissolved amount = 15 g; Maximum capacity = 36 g.<br><strong>Step 2: Classification:</strong> Since 15 g < 36 g, more solute can dissolve at 25°C, making it an <strong>unsaturated solution</strong>.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 12,
        "concept": "Saturation Limit",
        "question": "When a solution reaches a state where no more solute can dissolve at that temperature and excess solute remains as settled solid, the solution is:",
        "options": [
            "A. Unsaturated",
            "B. Saturated",
            "C. Dilute",
            "D. Pure solvent"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Saturation State:</strong> A saturated solution holds the maximum possible dissolved solute at dynamic equilibrium with undissolved solid.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 13,
        "concept": "Concentration Concept",
        "question": "Beaker A contains 2 g of copper sulfate in 100 mL of water (light blue). Beaker B contains 25 g of copper sulfate in 100 mL of water (deep navy blue). Which statement is true?",
        "options": [
            "A. Beaker A is more concentrated than Beaker B",
            "B. Beaker B is more concentrated than Beaker A",
            "C. Both have identical concentration",
            "D. Beaker B is pure solvent"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Concentration Definition:</strong> Concentration = Solute mass / Solution volume.<br><strong>Step 2: Comparison:</strong> Beaker A has 0.02 g/mL; Beaker B has 0.25 g/mL. Beaker B has more solute per unit volume, making it more concentrated.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 14,
        "concept": "Concentration Calculation",
        "question": "Calculate the mass-by-volume concentration percentage of a glucose solution prepared by dissolving 20 g of glucose in water to make 250 mL of solution.",
        "options": [
            "A. 5%",
            "B. 8%",
            "C. 12.5%",
            "D. 20%"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Formula:</strong> $\text{Concentration \% (m/v)} = \frac{\text{Mass of Solute (g)}}{\text{Volume of Solution (mL)}} \times 100$.<br><strong>Step 2: Calculation:</strong> $\frac{20\text{ g}}{250\text{ mL}} \times 100 = 0.08 \times 100 = 8\%$.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 15,
        "concept": "Solubility Definition",
        "question": "Solubility of a substance in laboratory science is typically expressed as:",
        "options": [
            "A. The number of seconds required to stir the liquid",
            "B. The maximum grams of solute that dissolve in 100 mL (or 100 g) of solvent at a given temperature",
            "C. The total weight of the glass beaker",
            "D. The boiling point of pure mercury"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Standard Definition:</strong> Solubility is defined as the maximum mass (in grams) of solute capable of dissolving in 100 mL (or 100 g) of solvent at a fixed temperature.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 16,
        "concept": "Temperature vs Solid Solubility",
        "question": "For most common solid solutes (such as potassium nitrate or table sugar), how does increasing the temperature affect solubility in water?",
        "options": [
            "A. Solubility increases",
            "B. Solubility decreases to zero",
            "C. Solubility fluctuates randomly every 2 seconds",
            "D. Solubility remains strictly constant at all temperatures"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Thermal Kinetic Effect:</strong> Heat expands interparticle voids between water molecules and breaks solute crystal lattices faster, increasing solid solubility.<br><strong>Step 2: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 17,
        "concept": "Heating Saturated Solution",
        "question": "A saturated solution of copper sulfate at 20°C contains crystals at the bottom. When heated to 60°C without adding water, the crystals dissolve. Why?",
        "options": [
            "A. Copper sulfate turns into liquid water",
            "B. The solubility of copper sulfate increases at higher temperature, making the solution unsaturated at 60°C",
            "C. Heat destroys the mass of the copper atoms",
            "D. Water molecules evaporate into solid ice"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Phase Shift:</strong> Raising temperature expands the solvent's solute capacity.<br><strong>Step 2: Transition:</strong> A solution saturated at 20°C becomes unsaturated at 60°C, readily dissolving the residual crystals.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 18,
        "concept": "Cooling Saturated Solution",
        "question": "What occurs when a clear, hot saturated sugar solution at 80°C is allowed to cool undisturbed to room temperature (20°C)?",
        "options": [
            "A. It explodes into steam",
            "B. The solution dissolves more sugar automatically",
            "C. Excess dissolved sugar precipitates out as solid crystals (recrystallization)",
            "D. It turns into pure metallic copper"
        ],
        "correct": 2,
        "solution": r"<p><strong>Step 1: Solubility Drop:</strong> As temperature drops from 80°C to 20°C, sugar solubility decreases significantly.<br><strong>Step 2: Recrystallization:</strong> The solvent can no longer hold the excess dissolved sugar, forcing it to crystallize out of solution.<br><strong>Step 3: Conclusion:</strong> Option C is correct.</p>"
    },
    {
        "id": 19,
        "concept": "Dilution Effect",
        "question": "If you add 200 mL of pure distilled water to a 10% salt solution, what changes occur?",
        "options": [
            "A. The total mass of dissolved salt decreases",
            "B. The solution becomes more dilute (concentration percentage decreases)",
            "C. The solution becomes more concentrated",
            "D. Salt crystallizes out immediately"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Dilution Mechanics:</strong> Adding solvent increases total volume while solute mass remains identical, lowering solute mass per unit volume (dilution).<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 20,
        "concept": "Oral Rehydration Solution (ORS)",
        "question": "Why is ORS (Oral Rehydration Solution) dissolved in clean water rather than swallowed as dry powder?",
        "options": [
            "A. Water acts as the solvent to disperse ions for immediate cellular absorption across intestinal walls",
            "B. Water destroys all the salts",
            "C. Dry powder cannot be touched by human hands",
            "D. Water turns the salts into solid stone"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Biological Transport:</strong> Dissolving ORS in water creates a homogeneous electrolyte solution, allowing Na⁺, K⁺, and glucose to be rapidly absorbed through intestinal epithelial co-transporters.<br><strong>Step 2: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 21,
        "concept": "Gas Dissolution in Water",
        "question": "How does oxygen gas exist inside a natural freshwater river?",
        "options": [
            "A. As chemical hydrogen peroxide (H₂O₂)",
            "B. As dissolved O₂ molecules dispersed uniformly throughout the water",
            "C. As giant visible air bubbles trapped under stones",
            "D. Oxygen does not dissolve in water at all"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Gaseous Solution:</strong> Atmospheric oxygen dissolves into water up to several milligrams per litre, forming a uniform liquid solution of dissolved O₂.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 22,
        "concept": "Gas Solubility vs Temperature",
        "question": "Unlike solid solutes, how does increasing temperature affect the solubility of gases (like oxygen or carbon dioxide) in water?",
        "options": [
            "A. Gas solubility increases dramatically",
            "B. Gas solubility decreases",
            "C. Gas turns into solid gold",
            "D. Gas solubility is completely unaffected by temperature"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Gas Thermodynamics:</strong> Increasing temperature increases the kinetic energy of dissolved gas molecules, allowing them to overcome weak solvent attractions and escape.<br><strong>Step 2: Law:</strong> Gas solubility decreases as temperature increases.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 23,
        "concept": "Thermal Pollution Ecology",
        "question": "When power plants discharge warm cooling water into natural lakes (thermal pollution), why do aquatic fish often suffocate?",
        "options": [
            "A. Warm water boils the fish alive instantly",
            "B. Warm water holds significantly less dissolved oxygen than cool water",
            "C. Warm water turns into hydrochloric acid",
            "D. Warm water freezes fish gills into solid ice"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Thermal Pollution Effect:</strong> Elevated water temperature causes dissolved oxygen to escape, depleting the oxygen concentration below levels required for fish respiration.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 24,
        "concept": "Density Definition",
        "question": "What is the scientific definition of density?",
        "options": [
            "A. Weight divided by gravity",
            "B. Mass per unit volume (Mass / Volume)",
            "C. Volume multiplied by length",
            "D. Temperature divided by pressure"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Formula:</strong> Density is defined as mass per unit volume: $\text{Density} = \frac{\text{Mass}}{\text{Volume}}$.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 25,
        "concept": "SI Unit of Density",
        "question": "What is the standard International System of Units (SI) unit for density?",
        "options": [
            "A. g/cm³",
            "B. kg/m³",
            "C. g/mL",
            "D. N/m²"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: SI Units:</strong> SI unit of mass is kilogram ($\text{kg}$); SI unit of volume is cubic metre ($\text{m}^3$). Therefore, the SI unit of density is $\text{kg/m}^3$.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 26,
        "concept": "Density Calculation",
        "question": "A sample of aluminium has a mass of 54 g and a volume of 20 cm³. What is its density?",
        "options": [
            "A. 1.08 g/cm³",
            "B. 2.7 g/cm³",
            "C. 5.4 g/cm³",
            "D. 27.0 g/cm³"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Formula:</strong> $\text{Density} = \frac{\text{Mass}}{\text{Volume}} = \frac{54\text{ g}}{20\text{ cm}^3} = 2.7\text{ g/cm}^3$.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 27,
        "concept": "Relative Density Concept",
        "question": "The relative density of silver is 10.5. Given that water density is 1.0 g/cm³, what is the actual density of silver?",
        "options": [
            "A. 1.05 g/cm³",
            "B. 10.5 g/cm³",
            "C. 105 g/cm³",
            "D. 0.105 g/cm³"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Formula:</strong> $\text{Relative Density} = \frac{\text{Density of Substance}}{\text{Density of Water}}$.<br><strong>Step 2: Calculation:</strong> $\text{Density of Silver} = 10.5 \times 1.0\text{ g/cm}^3 = 10.5\text{ g/cm}^3$.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 28,
        "concept": "Mass vs Weight",
        "question": "Which of the following statements correctly distinguishes mass from weight?",
        "options": [
            "A. Mass changes with gravity, while weight is constant everywhere",
            "B. Mass is the invariant amount of matter in grams or kilograms; weight is the gravitational force in newtons",
            "C. Mass is measured in newtons; weight is measured in cubic metres",
            "D. Mass and weight are identical physical terms"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Scientific Definition:</strong> Mass is the fundamental quantity of matter (measured in kg or g) invariant to location; weight is the downward gravitational pull ($W = mg$, measured in N).<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 29,
        "concept": "Meniscus Curve Cause",
        "question": "What physical interactions cause water in a narrow glass cylinder to form a curved concave meniscus?",
        "options": [
            "A. Water evaporates within 1 second",
            "B. Adhesive forces between water molecules and glass exceed the cohesive forces between water molecules",
            "C. Gravity pulls only on the center of the cylinder",
            "D. Atmospheric air pushes the edges downward"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Surface Forces:</strong> Water molecules adhere strongly to silica glass (adhesion > cohesion), crawling slightly up the walls to form a downward-curved concave meniscus.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 30,
        "concept": "Colored Solution Meniscus",
        "question": "When measuring the volume of an opaque, deeply colored liquid like potassium permanganate in a cylinder, why is the reading taken at the top of the meniscus?",
        "options": [
            "A. Because the dark color obscures the lower curved boundary, making the upper edge the only visible reference line",
            "B. Because colored liquids have zero mass",
            "C. Because colored liquids freeze immediately",
            "D. Because top readings are always 50 mL higher"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Optical Visibility:</strong> Deeply colored liquids prevent sight of the bottom curve through the liquid; the top boundary is distinctly visible and used consistently to ensure reproducibility.<br><strong>Step 2: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 31,
        "concept": "Water Displacement Volume",
        "question": "A graduated cylinder contains 65 mL of water. A dense metal bolt is submerged, causing the water level to rise to 82 mL. What is the volume of the bolt?",
        "options": [
            "A. 147 mL",
            "B. 17 cm³",
            "C. 65 cm³",
            "D. 82 cm³"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Displacement Principle:</strong> $\text{Volume} = V_{\text{final}} - V_{\text{initial}} = 82\text{ mL} - 65\text{ mL} = 17\text{ mL} = 17\text{ cm}^3$.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 32,
        "concept": "Geometric Formula Volume",
        "question": "A solid rectangular brick has dimensions: length = 10 cm, width = 5 cm, and height = 4 cm. If its mass is 400 g, what is its density?",
        "options": [
            "A. 0.5 g/cm³",
            "B. 1.0 g/cm³",
            "C. 2.0 g/cm³",
            "D. 4.0 g/cm³"
        ],
        "correct": 2,
        "solution": r"<p><strong>Step 1: Volume Calculation:</strong> $V = l \times w \times h = 10 \times 5 \times 4 = 200\text{ cm}^3$.<br><strong>Step 2: Density Calculation:</strong> $\text{Density} = \frac{\text{Mass}}{\text{Volume}} = \frac{400\text{ g}}{200\text{ cm}^3} = 2.0\text{ g/cm}^3$.<br><strong>Step 3: Conclusion:</strong> Option C is correct.</p>"
    },
    {
        "id": 33,
        "concept": "Thermal Effect on Density",
        "question": "Why does heating a metal rod cause its density to decrease slightly?",
        "options": [
            "A. Heating destroys the mass of the metal atoms",
            "B. Thermal expansion increases volume while mass remains unchanged, resulting in lower density",
            "C. Metal absorbs light and turns into a gas",
            "D. Gravity stops pulling on heated metals"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Thermal Mechanics:</strong> Thermal energy causes metal atoms to vibrate with greater amplitude, expanding the volume while mass remains strictly constant. Since $d = m/V$, increasing $V$ decreases density.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 34,
        "concept": "Pressure on Gas vs Solid",
        "question": "Why does doubling the external pressure dramatically increase the density of trapped air in a syringe, but has no measurable effect on a solid wooden block?",
        "options": [
            "A. Wood is a gas at room temperature",
            "B. Gases have vast interparticle spaces making them highly compressible; solids have tightly packed particles and are nearly incompressible",
            "C. Syringes generate heat that destroys air atoms",
            "D. Air contains zero mass"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Compressibility:</strong> Gas particles are separated by large voids; pressure forces them closer, reducing volume and increasing density. Solids have contact packing with negligible compressibility.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 35,
        "concept": "Water Maximum Density",
        "question": "At what specific temperature does liquid water attain its highest density of exactly 1.000 g/cm³?",
        "options": [
            "A. 0°C",
            "B. 4°C",
            "C. 25°C",
            "D. 100°C"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Anomalous Property:</strong> Water contracts on cooling until 4°C, reaching its peak density ($1.000\text{ g/cm}^3$). Below 4°C, it expands.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 36,
        "concept": "Why Ice Floats",
        "question": "Why does ice float on liquid water?",
        "options": [
            "A. Ice has a lower density (~0.92 g/cm³) than liquid water (1.0 g/cm³) due to its open hexagonal crystal cage",
            "B. Ice is made of helium and hydrogen gas",
            "C. Ice is repelled by the magnetic field of the liquid",
            "D. Surface tension prevents ice from ever breaking the surface"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Crystal Structure:</strong> As water freezes at 0°C, hydrogen bonds form an open hexagonal cage-like lattice that occupies ~9% more volume, reducing density to ~0.92 g/cm³, allowing it to float.<br><strong>Step 2: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 37,
        "concept": "Aquatic Winter Survival",
        "question": "How does the anomalous expansion and floating of surface ice protect aquatic life in deep lakes during severe freezing winters?",
        "options": [
            "A. Floating ice heats the entire lake to 50°C",
            "B. Surface ice acts as an insulating blanket, keeping the denser water underneath liquid at 4°C",
            "C. Ice dissolves all fish into dormant seeds",
            "D. Fish jump on top of the ice and breathe air"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Ecological Insulation:</strong> Surface ice acts as a thermal insulator preventing heat loss from the deep lake water. Densest water (at 4°C) settles to the bottom, remaining liquid and supporting fish life.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 38,
        "concept": "Planetary Density Layers",
        "question": "As one travels from Earth's outer crust down to the inner core, how does the density of materials change?",
        "options": [
            "A. Density continuously decreases toward zero",
            "B. Density increases progressively from ~2.7 g/cm³ at the crust to ~13.1 g/cm³ at the inner core",
            "C. Density remains exactly 1.0 g/cm³ throughout all layers",
            "D. Only the crust has density; the core is a hollow vacuum"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Planetary Layering:</strong> Earth is density-stratified: Crust (~2.7–3.0 g/cm³) → Mantle (~3.3–5.7 g/cm³) → Outer Core (~10–12 g/cm³) → Inner Core (~13.1 g/cm³).<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 39,
        "concept": "Core Composition",
        "question": "Why is Earth's core so much denser than the rocky continental crust?",
        "options": [
            "A. The core is composed of heavy metallic iron and nickel compacted under immense gravitational pressure",
            "B. The core is made of compressed sea water",
            "C. The crust contains lead and gold while the core contains wood",
            "D. The core has zero temperature"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Chemical Composition:</strong> The core is composed of an iron-nickel metallic alloy (NiFe) subjected to over 3.6 million atmospheres of compacting pressure, creating extreme density.<br><strong>Step 2: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 40,
        "concept": "Float or Sink Criterion",
        "question": "An object has a density of 0.85 g/cm³. If placed in a beaker of pure water (density = 1.0 g/cm³), what will the object do?",
        "options": [
            "A. Sink rapidly to the bottom",
            "B. Float with part of its volume above the water surface",
            "C. Dissolve into water vapor instantly",
            "D. Cause the water to boil"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Flotation Law:</strong> Any object with a density less than the liquid density will float ($0.85\text{ g/cm}^3 < 1.0\text{ g/cm}^3$). Specifically, 85% of its volume will be submerged and 15% will remain above the waterline.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    }
]

