# -*- coding: utf-8 -*-
"""
Class 9 Science • Chapter 5: Exploring Mixtures and their Separation
Complete curriculum data with 20 slides:
- Slides 1-16: Core teaching slides with 32 in-slide checkpoints (2 per slide)
- Slides 17-20: Dedicated quiz challenges (10 questions each = 40 questions total)
Syllabus Competencies: C-1.2, C-5.1, C-5.2, C-5.3, C-6.1, C-7.1, C-7.2, C-8.1, C-8.2
"""

SLIDES_DATA = [
    # SLIDE 1
    {
        "id": 1,
        "title": "Matter & Purity: Pure Substances vs Mixtures",
        "subtitle": "Homogeneous vs Heterogeneous Systems: Physical Combinations without Fixed Ratios",
        "narration": "Welcome students! In chemistry, 'pure' means something very specific: a single form of matter with fixed chemical composition and sharp melting points, like distilled water or gold. Most substances around us, however, are mixtures—physical combinations of two or more pure substances in variable proportions, retaining their original individual properties.",
        "points": [
            "<strong>Pure Substances:</strong> Composed of only one type of particle (elements like Iron $\\text{Fe}$ or compounds like pure Water $\\text{H}_2\\text{O}$); exhibit fixed melting/boiling points and cannot be separated into constituents by physical methods.",
            "<strong>Mixtures:</strong> Contain two or more pure substances mixed together in any proportion without chemical bonding; constituent components retain their distinct physical and chemical identities.",
            "<strong>Homogeneous Mixtures:</strong> Uniform composition and single phase throughout (e.g., salt dissolved in water, air, brass alloy); individual particles are indistinguishable under an optical microscope.",
            "<strong>Heterogeneous Mixtures:</strong> Non-uniform composition with physically distinct boundaries of separation (e.g., sand and iron filings, oil and water, chalk in water); components remain visibly distinct."
        ],
        "checkpoints": [
            {
                "q": "Why is 24-carat pure gold considered a pure substance, while 22-carat jewelry gold is classified as a mixture?",
                "options": [
                    "22-carat gold has chemical bonds between gold and copper",
                    "22-carat gold contains copper or silver alloyed in variable proportion without chemical reaction",
                    "24-carat gold can be separated into components by simple filtration",
                    "22-carat gold has a higher fixed melting point than pure gold"
                ],
                "correct": 1,
                "explanation": "22-carat gold is a homogeneous mixture (solid alloy) containing 22 parts gold and 2 parts copper or silver physically mixed without chemical combination, whereas 24-carat gold consists entirely of pure elemental gold atoms."
            },
            {
                "q": "Which of the following represents a homogeneous mixture?",
                "options": [
                    "A mixture of sulfur powder and iron filings",
                    "Muddy pond water",
                    "A clear solution of cane sugar completely dissolved in water",
                    "Milk containing suspended fat globules"
                ],
                "correct": 2,
                "explanation": "Sugar completely dissolved in water forms a true solution with uniform composition and single liquid phase throughout, making it a homogeneous mixture."
            }
        ]
    },

    # SLIDE 2
    {
        "id": 2,
        "title": "True Solutions & Their Fundamental Properties",
        "subtitle": "Homogeneous Molecular Dispersions: Solute, Solvent, Particle Size < 1 nm, and Stability",
        "narration": "A true solution is a homogeneous mixture of two or more substances. The component present in larger quantity that dissolves the other is the solvent, while the component dissolved is the solute. Because solute particles are smaller than 1 nanometer, they do not scatter light and will never settle out over time.",
        "points": [
            "<strong>Components of a Solution:</strong> Solute (substance dissolved, usually lesser amount) + Solvent (dissolving medium, usually greater amount). In an aqueous tincture of iodine, iodine solid is solute and alcohol is solvent.",
            "<strong>Ultramicroscopic Particle Size:</strong> Solute particles are individual ions or molecules with diameters less than $1\\text{ nm}$ ($10^{-9}\\text{ m}$), making them invisible even under powerful light microscopes.",
            "<strong>Optical Clarity & Absence of Tyndall Effect:</strong> Because particles are extraordinarily minute, they cannot scatter a beam of visible light passing through; the path of light is not visible in a true solution.",
            "<strong>High Stability & Filterability:</strong> Solute particles cannot be separated by ordinary filter paper or parchment membranes, and they never settle down when left undisturbed.",
            "<strong>Non-Liquid Solutions:</strong> Solutions are not always liquid: Air is a gaseous solution ($78\\%\\ \\text{N}_2, 21\\%\\ \\text{O}_2$), and Brass is a solid solution (alloy of $\\sim 70\\%\\ \\text{Cu}$ and $\\sim 30\\%\\ \\text{Zn}$)."
        ],
        "checkpoints": [
            {
                "q": "Why does a beam of light passed through a clear copper sulfate aqueous solution not show a illuminated visible beam path?",
                "options": [
                    "Copper sulfate chemically absorbs 100% of the light photons",
                    "Solute ions are smaller than 1 nm and cannot scatter visible light wavelengths",
                    "The solution is opaque to visible radiation",
                    "Solute particles settle too quickly to scatter light"
                ],
                "correct": 1,
                "explanation": "In a true solution, solute particles are smaller than 1 nanometer (less than the wavelength of light), so they do not scatter light. Hence, true solutions do not show the Tyndall effect."
            },
            {
                "q": "In aerated soda water, what are the solute and solvent respectively?",
                "options": [
                    "Solute: Water; Solvent: Carbon dioxide gas",
                    "Solute: Carbon dioxide gas; Solvent: Water",
                    "Both are solutes dissolved in air",
                    "Both act simultaneously as solvents"
                ],
                "correct": 1,
                "explanation": "In soda water, gaseous carbon dioxide (solute) is dissolved under high pressure in liquid water (solvent)."
            }
        ]
    },

    # SLIDE 3
    {
        "id": 3,
        "title": "Suspensions & Heterogeneous Settling Dynamics",
        "subtitle": "Macroscopic Particulate Systems: Particle Size > 100 nm, Instability, and Filterability",
        "narration": "A suspension is a heterogeneous mixture in which solute-like solid particles do not dissolve, but remain suspended throughout the bulk of the liquid medium. Because the particles are larger than 100 nanometers, they are visible to the naked eye, scatter light while in suspension, and eventually settle down under gravity.",
        "points": [
            "<strong>Macroscopic Particle Dimension:</strong> Suspended particles have diameters greater than $100\\text{ nm}$ ($10^{-7}\\text{ m}$), often visible to the naked eye or ordinary magnifying lens.",
            "<strong>Heterogeneous Bulk Phase:</strong> The solute particles remain suspended throughout the medium without molecular dissolution (e.g., chalk powder in water, sand in water, milk of magnesia).",
            "<strong>Dynamic Optical Behavior:</strong> While particles remain suspended, they scatter a beam of light, making its path visible. However, once particles settle, the scattering stops.",
            "<strong>Thermodynamic Instability:</strong> When left undisturbed, suspended particles settle at the bottom of the container due to gravity (sedimentation).",
            "<strong>Separation by Filtration:</strong> Suspended solid particles are larger than the pore diameter of ordinary filter paper and can be completely separated as a residue."
        ],
        "checkpoints": [
            {
                "q": "What happens to the ability of a chalk-water suspension to scatter light after it has been left undisturbed for 30 minutes?",
                "options": [
                    "Its light-scattering capacity increases exponentially",
                    "It stops scattering light because the heavy chalk particles settle down to the bottom",
                    "It converts spontaneously into a true solution",
                    "The chalk particles dissolve into ions smaller than 1 nm"
                ],
                "correct": 1,
                "explanation": "Suspensions are unstable. Once left undisturbed, the dense chalk particles sediment to the bottom under gravity; the supernatant liquid no longer scatters light."
            },
            {
                "q": "Which property correctly distinguishes a suspension from a true solution?",
                "options": [
                    "Suspension particles pass freely through filter paper without residue",
                    "Suspension particles settle down on standing, whereas true solution particles never settle",
                    "Suspensions are always completely transparent and homogeneous",
                    "Suspension particle diameter is strictly less than 1 nm"
                ],
                "correct": 1,
                "explanation": "Suspensions are unstable heterogeneous mixtures where particles sediment over time under gravity, whereas true solutions are permanently stable homogeneous mixtures."
            }
        ]
    },

    # SLIDE 4
    {
        "id": 4,
        "title": "Colloids & The Tyndall Effect",
        "subtitle": "Intermediate Dispersions (1–100 nm): Brownian Motion, Light Scattering, and Colloidal Forms",
        "narration": "Colloids occupy the fascinating intermediate territory between true solutions and suspensions. With particle sizes between 1 and 100 nanometers, colloids appear homogeneous to the naked eye, like milk or ink, but are actually heterogeneous! Their particles are large enough to scatter light—producing the famous Tyndall effect—yet light enough to remain permanently suspended due to continuous molecular bombardment called Brownian motion.",
        "points": [
            "<strong>Intermediate Colloidal Scale:</strong> Particle diameter ranges between $1\\text{ nm}$ and $100\\text{ nm}$ ($10^{-9}\\text{ m}$ to $10^{-7}\\text{ m}$).",
            "<strong>Two-Phase Architecture:</strong> Consists of a <em>Dispersed Phase</em> (the solute-like colloidal substance) distributed within a <em>Dispersion Medium</em> (the continuous solvent-like medium).",
            "<strong>The Tyndall Effect (John Tyndall, 1869):</strong> Scattering of a visible light beam by colloidal particles, illuminating the path of the beam as a luminous cone (e.g., sunlight passing through dense forest mist or dust in a cinema hall).",
            "<strong>Brownian Motion (Robert Brown, 1827):</strong> Constant, erratic zig-zag motion of colloidal particles caused by unequal collisions with dispersion medium molecules, preventing gravitational settling.",
            "<strong>Colloidal Types:</strong> Sol (solid in liquid: ink, paint), Gel (liquid in solid: jelly, cheese, butter), Emulsion (liquid in liquid: milk, face cream), Aerosol (liquid/solid in gas: fog, clouds, smoke), Foam (gas in liquid/solid: shaving cream, foam rubber)."
        ],
        "checkpoints": [
            {
                "q": "Why do fat and protein particles in milk remain suspended indefinitely without settling to the bottom?",
                "options": [
                    "They are held by chemical covalent bonds to water",
                    "Constant random collisions with water molecules (Brownian motion) counteract gravity",
                    "Milk is a true solution with particles smaller than 0.1 nm",
                    "Milk is an unstable coarse suspension"
                ],
                "correct": 1,
                "explanation": "In colloids, continuous chaotic bombardment by dispersion medium molecules (Brownian motion) imparts kinetic energy that prevents colloidal particles from settling under gravity."
            },
            {
                "q": "What type of colloid is formed when liquid water droplets are dispersed in atmospheric air (fog or cloud)?",
                "options": [
                    "Solid Sol",
                    "Aerosol",
                    "Gel",
                    "Emulsion"
                ],
                "correct": 1,
                "explanation": "When a liquid (water droplets) is dispersed in a gas (air), the resulting colloidal system is classified as an Aerosol."
            }
        ]
    },

    # SLIDE 5
    {
        "id": 5,
        "title": "Expressing Concentration of Solutions: Mass & Volume Formulas",
        "subtitle": "Quantifying Solute Content: Mass %, Mass by Volume %, and Volume % with Standard SI Units",
        "narration": "Concentration is the precise amount of solute present in a given amount of solution. In chemistry, we use three standard percentage conventions: mass by mass percentage, mass by volume percentage, and volume by volume percentage. Mastering these formulas is essential for laboratory preparation, medicine, and industrial chemistry.",
        "points": [
            "<strong>Mass by Mass Percentage (\\% w/w):</strong><br>$$\\text{Mass \\% of Solute} = \\frac{\\text{Mass of Solute}}{\\text{Mass of Solution}} \\times 100 = \\frac{\\text{Mass of Solute}}{\\text{Mass of Solute} + \\text{Mass of Solvent}} \\times 100$$",
            "<strong>Mass by Volume Percentage (\\% w/v):</strong><br>$$\\text{Mass by Volume \\%} = \\frac{\\text{Mass of Solute (in g)}}{\\text{Volume of Solution (in mL)}} \\times 100$$",
            "<strong>Volume by Volume Percentage (\\% v/v):</strong><br>$$\\text{Volume \\% of Solute} = \\frac{\\text{Volume of Solute}}{\\text{Volume of Solution}} \\times 100$$",
            "<strong>Crucial Problem-Solving Invariant:</strong> Remember that $\\text{Mass of Solution} = \\text{Mass of Solute} + \\text{Mass of Solvent}$. Never divide solely by the solvent mass!",
            "<strong>NCERT Standard Solved Example:</strong> A solution contains $40\\text{ g}$ of common salt in $320\\text{ g}$ of water. Total mass of solution = $40 + 320 = 360\\text{ g}$.<br>$$\\text{Mass \\%} = \\frac{40}{360} \\times 100 = 11.11\\%$$"
        ],
        "checkpoints": [
            {
                "q": "If 50 g of sodium chloride is dissolved in 200 g of distilled water, what is the mass by mass percentage of the solution?",
                "options": [
                    "25%",
                    "20%",
                    "16.67%",
                    "10%"
                ],
                "correct": 1,
                "explanation": "Total mass of solution = 50 g (solute) + 200 g (solvent) = 250 g. Mass % = (50 / 250) × 100 = 20%."
            },
            {
                "q": "A medical antiseptic solution contains 15 mL of pure alcohol dissolved in enough water to make 150 mL of solution. What is its volume by volume percentage?",
                "options": [
                    "10%",
                    "15%",
                    "11.1%",
                    "5%"
                ],
                "correct": 0,
                "explanation": "Volume % = (Volume of solute / Volume of solution) × 100 = (15 mL / 150 mL) × 100 = 10% (v/v)."
            }
        ]
    },

    # SLIDE 6
    {
        "id": 6,
        "title": "Solubility, Saturated Solutions & Temperature Dynamics",
        "subtitle": "Equilibrium Thermodynamics: Saturated, Unsaturated, Supersaturated States & Solubility Curves",
        "narration": "At any given temperature, a solvent can dissolve only a finite amount of solute. When no more solute can dissolve at that specific temperature, the solution is saturated. The maximum mass of solute dissolved in 100 grams of solvent at that temperature is called its solubility. For most solids, heating increases solubility, while cooling causes excess solute to crystallize out.",
        "points": [
            "<strong>Unsaturated Solution:</strong> A solution in which more solute can be dissolved at the existing temperature without changing conditions.",
            "<strong>Saturated Solution:</strong> A thermodynamic equilibrium state where no more solute can dissolve in the solvent at the specified temperature.",
            "<strong>Supersaturated Solution:</strong> A metastable condition containing more dissolved solute than the equilibrium saturation limit, prepared by cooling a hot saturated solution slowly without disturbance.",
            "<strong>Solubility Definition:</strong> The maximum mass of solute (in grams) that dissolves in $100\\text{ g}$ of a given solvent at a specific temperature to form a saturated solution.",
            "<strong>Temperature Influence on Solubility:</strong> For salts with endothermic dissolution (e.g., $\\text{KNO}_3$, $\\text{NH}_4\\text{Cl}$), solubility increases steeply with rising temperature. For salts like $\\text{NaCl}$, solubility rises only marginally with heat.",
            "<strong>Crystallisation on Cooling:</strong> If a saturated solution prepared at $60^\\circ\\text{C}$ is allowed to cool to $20^\\circ\\text{C}$, the difference in solubility cannot remain dissolved and precipitates as pure crystals."
        ],
        "checkpoints": [
            {
                "q": "The solubility of potassium nitrate (KNO3) in water is 32 g at 20°C and 106 g at 60°C. If 100 g of water saturated with KNO3 at 60°C is cooled down to 20°C, how much KNO3 will crystallize out?",
                "options": [
                    "32 g",
                    "106 g",
                    "74 g",
                    "138 g"
                ],
                "correct": 2,
                "explanation": "Mass of KNO3 dissolved at 60°C = 106 g. Mass of KNO3 dissolved at 20°C = 32 g. The excess solute that must crystallize out = 106 g - 32 g = 74 g."
            },
            {
                "q": "What happens when a single tiny seed crystal of solute is dropped into an undisturbed supersaturated solution?",
                "options": [
                    "The seed crystal immediately dissolves",
                    "Rapid precipitation of all excess dissolved solute occurs around the crystal",
                    "The temperature of the solution drops to absolute zero",
                    "The solution turns permanently into a gas"
                ],
                "correct": 1,
                "explanation": "A supersaturated solution is metastable. Introducing a seed crystal provides nucleation sites, triggering rapid crystallization of all excess solute until equilibrium saturation is reached."
            }
        ]
    },

    # SLIDE 7
    {
        "id": 7,
        "title": "Separation by Sublimation: Solid-Gas Direct Phase Shift",
        "subtitle": "Purifying Sublimable Volatile Solids from Non-Volatile Impurities (NH4Cl, Camphor, Iodine)",
        "narration": "Sublimation is a phase transition where a solid changes directly into gas without passing through the intermediate liquid state, and on cooling, the vapour condenses directly back to pure solid (sublimate). We use this technique to separate a volatile, sublimable component from a non-sublimable impurity like common salt or sand.",
        "points": [
            "<strong>Scientific Principle:</strong> Exploits the sharp difference in sublimation tendency; one component sublimes upon gentle heating while the other component has a very high melting/boiling point and remains non-volatile.",
            "<strong>Sublimable Compounds:</strong> Ammonium chloride ($\\text{NH}_4\\text{Cl}$), Camphor, Naphthalene balls, Anthracene, and solid Iodine ($\\text{I}_2$).",
            "<strong>Standard Laboratory Setup:</strong> Mixture of $\\text{NH}_4\\text{Cl}$ and $\\text{NaCl}$ placed in a china dish covered with an inverted glass funnel. The stem of the funnel is plugged with cotton to prevent vapour escape.",
            "<strong>Thermal Deposition:</strong> On heating over a Bunsen burner, $\\text{NH}_4\\text{Cl}$ turns into white dense vapours, rises, and condenses as pure solid crystals on the cooler inner walls of the inverted funnel.",
            "<strong>Non-Sublimable Residue:</strong> Pure non-volatile common salt ($\\text{NaCl}$) remains behind undisturbed in the china dish."
        ],
        "checkpoints": [
            {
                "q": "Why is the top stem of the inverted glass funnel plugged with cotton during sublimation of ammonium chloride?",
                "options": [
                    "To prevent air from entering and burning the mixture",
                    "To trap the ammonium chloride vapours inside so they condense on the funnel walls without escaping into the atmosphere",
                    "To filter solid salt particles from the vapour",
                    "To speed up the burning of the china dish"
                ],
                "correct": 1,
                "explanation": "The cotton plug closes the stem of the funnel, containing the sublimed vapours so they deposit as pure solid sublimate on the cool inner walls rather than escaping."
            },
            {
                "q": "Which of the following pairs of substances CANNOT be separated by sublimation?",
                "options": [
                    "Ammonium chloride and common salt",
                    "Camphor and sand",
                    "Sodium chloride (salt) and sugar",
                    "Iodine crystals and potassium chloride"
                ],
                "correct": 2,
                "explanation": "Neither sodium chloride nor sugar is sublimable; both decompose or melt rather than subliming, so sublimation cannot separate them."
            }
        ]
    },

    # SLIDE 8
    {
        "id": 8,
        "title": "Separation by Centrifugation & The Spinning Dance Analogy",
        "subtitle": "High-Speed Radial Acceleration: Cream Separation, Blood Diagnostics & Kathak Dance Physics",
        "narration": "When microscopic particles in a liquid suspension are too small to be separated by ordinary filter paper, centrifugation comes to the rescue! By spinning the mixture at thousands of revolutions per minute, centrifugal force drives denser particles radially outward to the bottom of the tube, while lighter liquid remains at the top. This principle mirrors the spinning turns in classical Indian Kathak and Sufi dancing!",
        "points": [
            "<strong>Scientific Principle:</strong> Uses rapid rotational motion to generate high centrifugal acceleration (many multiples of Earth's gravity $g$), causing denser suspended particles to sediment rapidly to the bottom while lighter fluid rises.",
            "<strong>Clinical Diagnostic Applications:</strong> Separates whole blood into cellular components (dense red blood cells at the bottom, white blood cells/platelets in the buffy coat, and straw-colored liquid plasma on top).",
            "<strong>Dairy & Domestic Applications:</strong> Used in dairies to separate lighter butterfat/cream from denser skimmed milk, and in washing machines to squeeze water out of wet clothes during spin cycles.",
            "<strong>C-5.3 Dance Biomechanics Analogy:</strong> In Indian classical Kathak (*chakkars*) and Sufi whirling, as a dancer spins with high angular velocity, their costume skirt flares outward due to centrifugal inertia. If the dancer extends their arms, rotational momentum and outward radial forces demonstrate the exact centrifugal physics used in centrifuges!"
        ],
        "checkpoints": [
            {
                "q": "When whole blood is centrifuged in a clinical diagnostic laboratory, why do the red blood cells settle at the very bottom of the centrifuge tube?",
                "options": [
                    "Red blood cells have lower density than liquid plasma",
                    "Red blood cells are denser than plasma and are driven to the bottom by centrifugal acceleration",
                    "Red blood cells dissolve completely in the tube glass",
                    "Centrifugation neutralizes the mass of blood plasma"
                ],
                "correct": 1,
                "explanation": "Centrifugation forces denser components radially outward to the tube bottom; since red blood cells have higher density (~1.09 g/mL) than plasma (~1.025 g/mL), they pack at the bottom."
            },
            {
                "q": "How does the flaring of a Kathak dancer's flared costume (ghaghra) during rapid pirouettes (chakkars) correlate to centrifugation?",
                "options": [
                    "Both rely on gravity pulling objects vertically downward",
                    "Both demonstrate outward radial displacement driven by high angular rotational acceleration",
                    "Both require vacuum chambers to operate",
                    "Both involve chemical phase changes from solid to gas"
                ],
                "correct": 1,
                "explanation": "In both cases, rapid circular rotation generates outward inertial acceleration that propels matter away from the central axis of rotation."
            }
        ]
    },

    # SLIDE 9
    {
        "id": 9,
        "title": "Paper Chromatography: Separating Solutes by Differential Adsorption",
        "subtitle": "Stationary vs Mobile Phase Dynamics, Dye Separation, and Retention Factor (Rf)",
        "narration": "Chromatography, derived from the Greek word 'chroma' meaning color, is a separation technique used to separate solutes that dissolve in the same solvent. As the solvent front creeps upward through a porous paper strip via capillary action, components that are more soluble in the mobile phase travel faster, separating into distinct colored bands.",
        "points": [
            "<strong>Scientific Principle:</strong> Differential partition and relative solubility between a <em>Stationary Phase</em> (porous cellulose chromatography filter paper) and a <em>Mobile Phase</em> (running solvent, such as water or ethanol).",
            "<strong>Capillary Ascent:</strong> The solvent rises up the paper strip by capillary action, carrying the dissolved dye molecules along with it.",
            "<strong>Differential Mobility:</strong> A component that is more soluble in the mobile phase and less adsorbed onto the paper fibers moves faster and travels higher. A less soluble component lags behind.",
            "<strong>Retention Factor ($R_f$ Metric):</strong> Standard scientific convention to identify compounds:<br>$$R_f = \\frac{\\text{Distance travelled by the solute from baseline}}{\\text{Distance travelled by the solvent front from baseline}}$$",
            "<strong>Real-World Applications:</strong> Separating synthetic dyes in black ink, isolating plant photosynthetic pigments (chlorophyll a, b, xanthophyll, carotene), and detecting drugs or toxic metabolites in forensic blood/urine tests."
        ],
        "checkpoints": [
            {
                "q": "In a paper chromatography experiment with black ink, why does the green dye component travel higher up the paper strip than the red dye component?",
                "options": [
                    "Green dye has a higher molecular weight than red dye",
                    "Green dye is more soluble in the rising water solvent and less strongly adsorbed by the paper fibers",
                    "Green dye undergoes sublimation during the test",
                    "Red dye reacts chemically with water to form an insoluble solid"
                ],
                "correct": 1,
                "explanation": "Chromatographic separation depends on differential solubility and paper affinity: components that are more soluble in the mobile phase travel faster and farther."
            },
            {
                "q": "If a dye spot moves 4.5 cm from the origin line while the solvent front moves 9.0 cm, what is the retention factor (Rf) of the dye?",
                "options": [
                    "2.0",
                    "0.50",
                    "0.45",
                    "13.5"
                ],
                "correct": 1,
                "explanation": "Rf = (Distance travelled by solute) / (Distance travelled by solvent front) = 4.5 cm / 9.0 cm = 0.50."
            }
        ]
    },

    # SLIDE 10
    {
        "id": 10,
        "title": "Simple Distillation & Traditional Kannauj Deg-Bhapka",
        "subtitle": "Separating Miscible Liquids (ΔTb > 25°C) & India's Ancient Perfume Hydro-Distillation (C-6.1)",
        "narration": "Simple distillation is used to separate miscible liquids that boil without decomposition and possess a significant boiling point difference of more than 25°C. In India, traditional hydro-distillation has been practiced for over 1,000 years in Kannauj—the Perfume Capital of India—using the ingenious copper 'Deg-Bhapka' method to extract pure rose and petrichor attars!",
        "points": [
            "<strong>Simple Distillation Principle:</strong> Liquid mixture is heated in a distillation flask. The component with the lower boiling point vaporizes first, passes through a water-cooled Liebig condenser where it liquifies, and is collected in a receiver flask as distillate.",
            "<strong>Boiling Point Criterion:</strong> Applicable when the boiling points of two miscible liquids differ by at least $25^\\circ\\text{C}$ (or $25\\text{ K}$), e.g., Acetone (b.p. $56^\\circ\\text{C}$) and Water (b.p. $100^\\circ\\text{C}$, $\\Delta T_b = 44^\\circ\\text{C}$).",
            "<strong>C-6.1 Cultural Legacy: Deg-Bhapka of Kannauj:</strong> Kannauj in Uttar Pradesh produces authentic natural perfumes (*Attar*) using traditional copper stills without modern electricity:",
            "• <strong>The Deg (Still):</strong> Large copper vessel holding fresh flower petals (Damask Rose) and water, sealed hermetically with clay and cotton (*multani mitti*).",
            "• <strong>The Chonga:</strong> Bamboo pipe wrapped with twine connecting the Deg to the receiver.",
            "• <strong>The Bhapka (Receiver):</strong> Long-necked copper vessel filled with sandalwood base oil, submerged in a cold water tank (*Gaddi*) acting as a natural condenser."
        ],
        "checkpoints": [
            {
                "q": "Why can a mixture of acetone (boiling point 56°C) and water (boiling point 100°C) be separated cleanly by simple distillation?",
                "options": [
                    "They form an azeotrope that boils at a single temperature",
                    "Their boiling point difference is 44°C, which is well above the required threshold of 25°C",
                    "Water decomposes before reaching its boiling point",
                    "Acetone sublimes while water remains solid"
                ],
                "correct": 1,
                "explanation": "Simple distillation works efficiently when miscible liquids have a boiling point difference greater than 25°C. For acetone (56°C) and water (100°C), the difference is 44°C."
            },
            {
                "q": "In the traditional Kannauj Deg-Bhapka distillation system, what serves the functional role of the modern water condenser?",
                "options": [
                    "The wood-fired mud hearth (Bhatti)",
                    "The copper Bhapka vessel submerged inside a cold water tank (Gaddi)",
                    "The bamboo Chonga pipe wrapped in twine",
                    "The clay sealing paste on the rim"
                ],
                "correct": 1,
                "explanation": "The Bhapka (copper receiver) is kept submerged in a large tank of cold water, functioning as a condenser to cool and liquefy fragrant steam vapours flowing through the bamboo pipe."
            }
        ]
    },

    # SLIDE 11
    {
        "id": 11,
        "title": "Fractional Distillation & Industrial Air Liquefaction",
        "subtitle": "Separating Liquids with Close Boiling Points (ΔTb < 25°C) & Liquefying Atmospheric Gases",
        "narration": "When two or more miscible liquids have boiling points that differ by less than 25°C, simple distillation fails because both vapours rise together. Fractional distillation solves this with a fractionating column packed with glass beads, creating repeated condensation-evaporation cycles. This exact principle allows us to separate atmospheric air into pure nitrogen, argon, and oxygen!",
        "points": [
            "<strong>Fractionating Column Architecture:</strong> A vertical column packed with inert glass beads fitted between the flask and condenser. The beads provide a huge surface area for rising vapours to cool and condense repeatedly.",
            "<strong>Mechanism of Action:</strong> In each vaporization-condensation step up the column, the ascending vapour becomes richer in the more volatile (lower boiling) component, while the descending liquid becomes richer in the less volatile component.",
            "<strong>Separating Components of Air:</strong> Air is a homogeneous gaseous mixture of $78.08\\%\\ \\text{N}_2$, $20.95\\%\\ \\text{O}_2$, $0.93\\%\\ \\text{Ar}$, and trace gases.",
            "• <strong>Step 1: Liquefaction:</strong> Air is filtered, compressed under high pressure, and cooled by rapid expansion to produce liquid air.",
            "• <strong>Step 2: Fractional Warming:</strong> Liquid air is allowed to warm slowly in a fractional distillation column:",
            "  1. <strong>Nitrogen</strong> boils off first at $-196^\\circ\\text{C}$ ($77\\text{ K}$).",
            "  2. <strong>Argon</strong> boils off second at $-186^\\circ\\text{C}$ ($87\\text{ K}$).",
            "  3. <strong>Oxygen</strong> remains liquid longest, boiling at $-183^\\circ\\text{C}$ ($90\\text{ K}$), and is collected from the bottom."
        ],
        "checkpoints": [
            {
                "q": "Why does nitrogen gas boil off first when liquid air is gently warmed in a fractional distillation column?",
                "options": [
                    "Nitrogen has the lowest boiling point (-196°C) among the major air components",
                    "Nitrogen is denser than liquid oxygen",
                    "Nitrogen reacts chemically with argon to form a solid",
                    "Nitrogen has the highest critical temperature"
                ],
                "correct": 0,
                "explanation": "Nitrogen has the lowest boiling point (-196°C) compared to Argon (-186°C) and Oxygen (-183°C), so it vaporizes first at the lowest temperature."
            },
            {
                "q": "What is the primary function of the glass beads packed inside a fractional distillation column?",
                "options": [
                    "To chemically catalyze the reaction between the liquids",
                    "To provide an increased surface area for repeated cycles of condensation and re-vaporization",
                    "To absorb water vapor and act as a drying agent",
                    "To filter out suspended dirt particles"
                ],
                "correct": 1,
                "explanation": "The glass beads provide a large surface area for hot ascending vapours to cool and condense repeatedly, progressively enriching the vapour in the more volatile liquid."
            }
        ]
    },

    # SLIDE 12
    {
        "id": 12,
        "title": "Crystallisation & Micro-Scale Green Chemistry (C-7.1)",
        "subtitle": "Purifying Soluble Solids: Copper Sulfate, Alum & Waste-Minimizing Microscale Labs",
        "narration": "Crystallisation is a technique that separates a pure solid in the form of its geometric crystals from a solution. It is vastly superior to simple evaporation to dryness because evaporation often causes sensitive compounds to decompose, char (like sugar), or leaves behind soluble impurities. In modern laboratories, micro-scale crystallisation dramatically reduces chemical waste!",
        "points": [
            "<strong>Why Crystallisation is Superior to Evaporation:</strong><br>• During evaporation to dryness, solids may decompose or get charred upon excessive heating (e.g., sugar decomposes to carbon).<br>• Soluble impurities remain mixed with the solid during complete evaporation, whereas crystallisation leaves impurities dissolved in the mother liquor.",
            "<strong>Laboratory Crystallisation Protocol (Copper Sulfate $\\text{CuSO}_4\\cdot 5\\text{H}_2\\text{O}$):</strong><br>1. Dissolve impure sample in minimum volume of distilled water.<br>2. Filter out insoluble dirt impurities.<br>3. Heat gently until the crystallization point is reached (tested by dipping a glass rod—crust forms).<br>4. Leave undisturbed to cool slowly: magnificent blue triclinic crystals grow!",
            "<strong>C-7.1 Micro-scale Chemistry Innovation:</strong> Instead of using hundreds of grams of toxic heavy metal salts, micro-scale setups use milligram-level reagents (few drops on cavity well-plates or capillary tubes). This adheres to <em>Green Chemistry</em>: zero toxic effluent, minimal hazard, and identical crystalline discovery!"
        ],
        "checkpoints": [
            {
                "q": "Why is crystallisation preferred over heating to dryness for obtaining pure copper sulfate from an impure sample?",
                "options": [
                    "Evaporation requires expensive catalysts",
                    "Heating to dryness can decompose copper sulfate and traps all soluble impurities in the crust",
                    "Crystallisation converts copper into gold",
                    "Copper sulfate will sublime and escape if crystallized"
                ],
                "correct": 1,
                "explanation": "Heating to dryness can decompose hydrated copper sulfate and causes soluble impurities to deposit with the product. Crystallisation leaves impurities behind in the mother liquor."
            },
            {
                "q": "What core principle of Green Chemistry (C-7.1) is demonstrated by using micro-scale crystallisation experiments?",
                "options": [
                    "Using plastic disposable beakers instead of glassware",
                    "Drastically reducing reagent quantities and hazardous chemical waste while achieving identical pedagogical outcomes",
                    "Eliminating the need to record experimental data",
                    "Increasing the heating temperature to 1000°C"
                ],
                "correct": 1,
                "explanation": "Micro-scale experimentation uses minute reagent volumes, dramatically minimizing hazardous chemical waste and environmental footprint."
            }
        ]
    },

    # SLIDE 13
    {
        "id": 13,
        "title": "Coagulation, Loading & Municipal Water Purification (C-5.2)",
        "subtitle": "Engineering Clean Drinking Water: Sedimentation, Alum Loading, Multi-tier Filtration & Chlorination",
        "narration": "Water from rivers or lakes contains suspended clay, colloidal impurities, and harmful pathogens. The municipal water purification system uses a sequential series of physical separation processes—sedimentation, loading with alum, multi-tier filtration, and chlorination—to deliver safe, potable water to millions of homes every day.",
        "points": [
            "<strong>Stage 1: Sedimentation Tank:</strong> Coarse suspended debris and heavy soil particles settle to the bottom under gravitational force over several hours.",
            "<strong>Stage 2: Loading / Coagulation Tank (Potash Alum):</strong> Fine colloidal clay particles carry negative electrical charges and repel each other, staying suspended. Adding Potash Alum ($\\text{KAl(SO}_4)_2\\cdot 12\\text{H}_2\\text{O}$) releases trivalent aluminium cations ($\\text{Al}^{3+}$), neutralizing the negative charge. The neutralized clay particles agglomerate into heavy 'flocs' that rapidly settle to the bottom.",
            "<strong>Stage 3: Multi-tier Filtration Tank:</strong> Clarified water passes through three successive layers: fine sand on top, coarse sand in the middle, and gravel at the base, trapping all remaining micro-particulates.",
            "<strong>Stage 4: Chlorination Tank:</strong> Controlled chlorine gas or bleaching powder ($\\text{CaOCl}_2$) is dissolved to destroy pathogenic bacteria and viruses before pumping to municipal overhead storage reservoirs.",
            "<strong>C-5.2 Societal & Environmental Impact:</strong> Access to purified municipal water eliminated water-borne epidemics (typhoid, cholera, dysentery), extending human life expectancy worldwide."
        ],
        "checkpoints": [
            {
                "q": "What is the exact scientific role of adding alum (phitkari) to the loading tank during municipal water purification?",
                "options": [
                    "It sweetens the taste of water by adding glucose",
                    "It neutralizes the electrical charges on fine colloidal clay particles so they coagulate into heavy flocs and settle",
                    "It reacts with chlorine to produce oxygen bubbles",
                    "It boils the water instantly to 100°C"
                ],
                "correct": 1,
                "explanation": "Alum provides trivalent aluminium ions (Al³⁺) that neutralize the mutually repelling negative charges on colloidal clay particles, causing them to coagulate (loading) and settle."
            },
            {
                "q": "In a municipal sand-and-gravel filtration tank, what is the correct sequence of media layers from top to bottom?",
                "options": [
                    "Top: Coarse gravel; Middle: Sand; Bottom: Fine sand",
                    "Top: Fine sand; Middle: Coarse sand; Bottom: Gravel",
                    "Top: Alum; Middle: Chlorine tablets; Bottom: Clay",
                    "Top: Activated charcoal; Middle: Gravel; Bottom: Fine sand"
                ],
                "correct": 1,
                "explanation": "Water flows from top to bottom through progressively coarser layers: fine sand at top traps fine particles, coarse sand in middle, and gravel at the base supports drainage."
            }
        ]
    },

    # SLIDE 14
    {
        "id": 14,
        "title": "Frugal Scientific Innovation: The Paperfuge (C-8.1)",
        "subtitle": "Dr. Manu Prakash's 20-Cent Centrifuge: 125,000 RPM Whirligig Separating Blood in 90 Seconds",
        "narration": "Who says cutting-edge medical science requires million-rupee electric machines? In 2017, Indian-origin Stanford bioengineer Dr. Manu Prakash invented the 'Paperfuge'—a 20-cent centrifuge made from paper, string, and plastic handles based on a 5,000-year-old whirligig children's toy. Spinning at an astonishing 125,000 RPM, it separates pure plasma from whole blood in 90 seconds in remote clinics with zero electricity!",
        "points": [
            "<strong>The Global Healthcare Problem:</strong> Heavy commercial electric centrifuges cost $\\$1,000\\text{ to }\\$5,000$, weigh kilograms, and require reliable grid electricity—making them useless in off-grid rural health centers across developing nations.",
            "<strong>The Ancient Whirligig Toy Connection:</strong> By analyzing the non-linear physics of two braided twisted strings pulling a central disc, Dr. Manu Prakash discovered that the unwinding disc stores kinetic energy, reversing direction and accelerating to blistering speeds.",
            "<strong>Mechanical Breakthrough:</strong> The paper disc achieves rotational speeds up to $125,000\\text{ RPM}$ and centrifugal acceleration of $30,000\\ g$—surpassing many laboratory electric centrifuges!",
            "<strong>Clinical Separation in 90 Seconds:</strong> Capillary tubes attached radially to the paper disc cleanly separate pure plasma from red blood cells in 90 seconds, enabling point-of-care diagnosis for malaria, HIV, and anemia.",
            "<strong>C-8.1 Pedagogical Inspiration:</strong> Proves that deep scientific principles (centripetal force, fluid dynamics, conservation of angular momentum) can be harnessed using eco-friendly, accessible materials to solve urgent human problems."
        ],
        "checkpoints": [
            {
                "q": "What ancient mechanism inspired Dr. Manu Prakash to invent the high-speed Paperfuge for field diagnostics?",
                "options": [
                    "A grandfather clock pendulum",
                    "The traditional whirligig button-and-string spinning toy",
                    "A water wheel mill",
                    "An archery bow and arrow"
                ],
                "correct": 1,
                "explanation": "The Paperfuge was inspired by the classical whirligig toy, where rhythmic pulling on strings creates rapid alternating rotational cycles reaching 125,000 RPM."
            },
            {
                "q": "Why is the Paperfuge considered a milestone in frugal medical engineering for developing nations?",
                "options": [
                    "It costs only ~20 cents, weighs 2 grams, operates without electricity, and separates blood in 90 seconds",
                    "It replaces the need for doctors and hospitals completely",
                    "It converts dirty water into pure drinking water instantaneously",
                    "It uses diamond bearings to achieve hypersonic rotation"
                ],
                "correct": 0,
                "explanation": "The Paperfuge is ultra-low-cost (~20 cents), completely manual (zero electricity), lightweight, and separates blood plasma rapidly for field diagnosis."
            }
        ]
    },

    # SLIDE 15
    {
        "id": 15,
        "title": "Indian Scientific Pioneer: Dr. Dilip Mahalanabis & The Chemistry of ORS",
        "subtitle": "Homogeneous Solution Chemistry Saving 50 Million Lives: SGLT1 Sodium-Glucose Co-Transport (C-6.1)",
        "narration": "During the 1971 Bangladesh Liberation War, millions of refugees fled into West Bengal. In the refugee camps of Bangaon, a devastating cholera epidemic struck. Intravenous saline bags ran out, and patients were dying by the hour. An Indian pediatrician, Dr. Dilip Mahalanabis, applied the fundamental chemistry of homogeneous solutions to formulate Oral Rehydration Solution (ORS)—saving over 50 million human lives!",
        "points": [
            "<strong>The Cholera Crisis of 1971:</strong> Cholera toxin causes massive osmotic fluid loss from intestinal cells, leading to catastrophic dehydration, shock, and death within hours. Hospital intravenous (IV) saline supply was completely overwhelmed.",
            "<strong>The Biochemical Solution Formulation:</strong> Dr. Dilip Mahalanabis prepared a precise homogeneous aqueous solution containing:<br>• $3.5\\text{ g}$ Sodium chloride ($\\text{NaCl}$)<br>• $2.5\\text{ g}$ Sodium bicarbonate ($\\text{NaHCO}_3$, later replaced by Trisodium citrate)<br>• $1.5\\text{ g}$ Potassium chloride ($\\text{KCl}$)<br>• $20\\text{ g}$ Glucose (anhydrous) dissolved in exactly $1\\text{ Litre}$ of clean drinking water.",
            "<strong>The SGLT1 Mechanism:</strong> Cholera toxin disables single ion pumps, but leaves the intestinal <em>Sodium-Glucose Co-transporter 1 (SGLT1)</em> intact! When sodium ions and glucose are present in equimolar ratio in a homogeneous solution, SGLT1 transports them together across the intestinal lining into blood vessels, pulling water along by rapid osmosis!",
            "<strong>Monumental Historic Impact:</strong> In Dr. Mahalanabis's camp, cholera mortality plummeted from over $30\\%$ to under $3.6\\%$! The prestigious medical journal <em>The Lancet</em> declared ORS 'potentially the most important medical advance of the 20th century'."
        ],
        "checkpoints": [
            {
                "q": "Why is glucose an indispensable chemical component in the Oral Rehydration Solution (ORS) formulated by Dr. Dilip Mahalanabis?",
                "options": [
                    "It acts merely as a flavoring agent to make the medicine sweet",
                    "It binds with sodium via the SGLT1 co-transporter, driving massive osmotic reabsorption of water back into the bloodstream",
                    "It kills cholera bacteria directly by boiling them",
                    "It solidifies the liquid solution inside the stomach"
                ],
                "correct": 1,
                "explanation": "Glucose activates the intestinal SGLT1 co-transporter: one glucose molecule and two sodium ions are transported simultaneously across mucosal cells, pulling water molecules along by osmosis."
            },
            {
                "q": "What was the direct societal impact of Dr. Dilip Mahalanabis's discovery during the 1971 Bangaon refugee crisis?",
                "options": [
                    "It eradicated all mosquito populations in West Bengal",
                    "It slashed cholera dehydration mortality from 30% down to under 3.6%, saving an estimated 50+ million lives globally",
                    "It invented the first atomic microscope",
                    "It discovered a new synthetic element on the periodic table"
                ],
                "correct": 1,
                "explanation": "Dr. Mahalanabis's field deployment of ORS reduced cholera mortality from over 30% to below 3.6%, transforming global diarrhea treatment and saving over 50 million lives."
            }
        ]
    },

    # SLIDE 16
    {
        "id": 16,
        "title": "Open Scientific Inquiry: Can We Create Artificial Blood? (C-7.2)",
        "subtitle": "The Colloid Challenge: Perfluorocarbons (PFCs), Hemoglobin Carriers & Future Biomimetics",
        "narration": "Have you ever wondered: can chemists synthesize artificial blood that works just as real blood for all patients, regardless of blood group? Human blood is an astonishingly complex colloidal fluid: a living suspension of erythrocytes, leukocytes, and platelets inside an aqueous protein-electrolyte solution. Creating an artificial replacement has challenged scientists for over six decades!",
        "points": [
            "<strong>The Colloid Complexity of Natural Blood:</strong> Real blood is a non-Newtonian shear-thinning fluid consisting of $55\\%$ plasma (a complex solution of albumin, globulins, fibrinogen, electrolytes) and $45\\%$ formed cellular elements in colloidal suspension.",
            "<strong>Primary Candidate 1: Perfluorocarbons (PFCs):</strong> Chemically inert synthetic fluorocarbon liquids capable of dissolving up to $50$ times more non-polar oxygen gas than water. Formulated as micro-emulsions to circulate safely through micro-capillaries.",
            "<strong>Primary Candidate 2: Hemoglobin-Based Oxygen Carriers (HBOCs):</strong> Purified tetrameric hemoglobin extracted from outdated human blood or bovine sources, polymerized with glutaraldehyde to prevent renal toxicity.",
            "<strong>Why Creating True Artificial Blood is Extremely Difficult:</strong><br>1. <em>Universal Multifunctionality:</em> Real blood does not just transport oxygen; it fights infections (leukocytes), clots wounds (platelet thrombi), and buffers pH.<br>2. <em>Nitric Oxide Scavenging:</em> Free cell-free hemoglobin strips nitric oxide ($\\text{NO}$) from arterial walls, causing dangerous vasoconstriction and hypertension.<br>3. <em>Colloid Osmotic Pressure:</em> Maintaining exact oncotic pressure across capillary walls without triggering immune rejection or kidney damage.",
            "<strong>C-7.2 The Future Frontier:</strong> Nanoscale synthetic synthetic polymersomes and artificial platelets using biodegradable PEG-lipids are currently in clinical trials."
        ],
        "checkpoints": [
            {
                "q": "From a physical chemistry standpoint, how is natural human blood best classified?",
                "options": [
                    "A pure chemical element",
                    "A complex colloidal suspension of living cells in an aqueous electrolyte-protein solution",
                    "A completely homogeneous single-phase true solution",
                    "A coarse gaseous aerosol"
                ],
                "correct": 1,
                "explanation": "Blood is a complex heterogeneous system: cellular elements (RBCs, WBCs, platelets) are suspended in blood plasma, which itself is a colloidal solution of proteins and dissolved electrolytes."
            },
            {
                "q": "What is one major biochemical hurdle that prevents cell-free hemoglobin solutions from easily replacing natural cellular blood?",
                "options": [
                    "Hemoglobin cannot bind oxygen molecules outside a living body",
                    "Cell-free hemoglobin scavenges arterial nitric oxide, causing severe blood vessel constriction and systemic hypertension",
                    "Hemoglobin turns into lead upon contact with air",
                    "Hemoglobin freezes solid at normal human body temperature"
                ],
                "correct": 1,
                "explanation": "Outside the protective red blood cell membrane, free hemoglobin rapidly binds and scavenges nitric oxide (NO) from vascular endothelia, inducing coronary and systemic vasoconstriction."
            }
        ]
    },

    # SLIDE 17 - QUIZ 1
    {
        "id": 17,
        "title": "Dedicated Quiz Challenge 1: Mixtures, Solutions, Suspensions & Colloids",
        "subtitle": "Mastery Assessment: Particle Size, Tyndall Effect, Brownian Motion & Phases (C-1.2)",
        "narration": "Welcome to Quiz Challenge 1! Test your foundational understanding of pure substances, homogeneous and heterogeneous mixtures, true solutions, suspensions, and colloids. Answer all 10 questions and use 'View Solution' for detailed step-by-step explanations.",
        "questions": [
            {
                "q": "Which of the following mixtures exhibits a visible path of light when a laser beam is shone through it?",
                "options": ["Aqueous copper sulfate solution", "Sodium chloride in water", "Dilute milk in water", "Alcohol in distilled water"],
                "correct": 2,
                "solution": "Milk is a colloidal emulsion where dispersed fat and protein particles (1–100 nm) scatter light wavelengths, producing the Tyndall effect. Copper sulfate, salt, and alcohol form true solutions (<1 nm) that cannot scatter light."
            },
            {
                "q": "What is the typical particle diameter in a true solution?",
                "options": ["Greater than 1000 nm", "Between 1 nm and 100 nm", "Less than 1 nm (< 10⁻⁹ m)", "Exactly 1 mm"],
                "correct": 2,
                "solution": "In a true solution, solute particles are single ions or molecules with dimensions strictly less than 1 nanometer (10⁻⁹ m), allowing them to pass through filter paper without scattering light."
            },
            {
                "q": "Which statement regarding Brownian motion in colloidal systems is scientifically accurate?",
                "options": [
                    "It is caused by gravitational attraction towards the Earth's core",
                    "It results from continuous, unbalanced collisions of dispersion medium molecules with colloidal particles",
                    "It causes colloidal particles to immediately settle at the bottom",
                    "It occurs only in gaseous aerosols at 1000°C"
                ],
                "correct": 1,
                "solution": "Brownian motion is the rapid, random zig-zag motion of colloidal particles caused by unequal, chaotic bombardment from the surrounding dispersion medium molecules, preventing gravitational settling."
            },
            {
                "q": "Shaving cream is a colloidal system. What are its dispersed phase and dispersion medium?",
                "options": [
                    "Dispersed phase: Liquid; Dispersion medium: Gas",
                    "Dispersed phase: Gas; Dispersion medium: Liquid",
                    "Dispersed phase: Solid; Dispersion medium: Liquid",
                    "Dispersed phase: Gas; Dispersion medium: Solid"
                ],
                "correct": 1,
                "solution": "Shaving cream is a foam, which consists of gas bubbles (dispersed phase) entrapped in a liquid soap matrix (dispersion medium)."
            },
            {
                "q": "Which of the following is classified as a pure chemical compound rather than a mixture?",
                "options": ["Pure air", "Distilled pure water (H₂O)", "Brass (alloy of Cu and Zn)", "Petroleum crude oil"],
                "correct": 1,
                "solution": "Distilled water (H₂O) is a pure chemical compound with fixed hydrogen-to-oxygen mass ratio (1:8 by mass) and sharp melting/boiling points. Air, brass, and petroleum are mixtures of variable composition."
            },
            {
                "q": "Why can suspended particles in muddy water be separated using ordinary filter paper, whereas starch in water cannot?",
                "options": [
                    "Suspension particles (>100 nm) are larger than filter paper pores, while colloidal starch particles (1–100 nm) pass through",
                    "Starch particles react chemically with cellulose fibers",
                    "Muddy water is a true solution while starch is a gas",
                    "Filter paper carries a strong electrical charge that repels mud"
                ],
                "correct": 0,
                "solution": "Suspension particles exceed 100 nm and are larger than the microscopic pores of filter paper, so they are retained as residue. Colloidal particles (1–100 nm) are smaller than filter pores and pass through."
            },
            {
                "q": "What happens when a cold carbonated soda bottle is opened at room temperature?",
                "options": [
                    "Carbon dioxide gas solubility increases",
                    "Pressure drops, drastically reducing the solubility of CO₂ gas and causing effervescent bubbling",
                    "The soda freezes into solid dry ice",
                    "Liquid water converts into gas"
                ],
                "correct": 1,
                "solution": "According to Henry's law, gas solubility is directly proportional to pressure. Opening the cap releases pressure, lowering CO₂ solubility and causing gas bubbles to vigorously escape."
            },
            {
                "q": "Cheese and butter are examples of which colloidal classification?",
                "options": ["Aerosol", "Solid Sol", "Gel (liquid dispersed in solid)", "Foam"],
                "correct": 2,
                "solution": "Cheese, butter, and jellies are classified as Gels, where a liquid dispersed phase is trapped within a solid continuous dispersion medium."
            },
            {
                "q": "Which of the following is an example of a solid-in-solid homogeneous solution?",
                "options": ["Brass alloy (Zinc in Copper)", "Granite rock with mica and quartz", "Sand mixed with iron filings", "Chalk powder in sulfur"],
                "correct": 0,
                "solution": "Brass is an alloy (homogeneous solid solution) where ~30% zinc atoms are uniformly dispersed in ~70% copper lattice at the atomic level."
            },
            {
                "q": "A mixture whose components can be distinguished under a simple magnifying glass and settle on standing is a:",
                "options": ["True solution", "Colloid", "Suspension", "Pure element"],
                "correct": 2,
                "solution": "A suspension is a heterogeneous mixture with macroscopic particles (>100 nm) visible to the eye/magnifying glass that sediment over time under gravity."
            }
        ]
    },

    # SLIDE 18 - QUIZ 2
    {
        "id": 18,
        "title": "Dedicated Quiz Challenge 2: Concentration Formulas & Solubility Curves",
        "subtitle": "Mastery Assessment: Mass %, Volume %, Solubility Math & Thermodynamic Precipitates",
        "narration": "Welcome to Quiz Challenge 2! Sharpen your quantitative problem-solving skills on mass percentages, mass by volume percentages, and solubility curve interpretations. Work through each calculation with scientific precision.",
        "questions": [
            {
                "q": "A solution is prepared by dissolving 25 g of glucose in 175 g of distilled water. What is the mass by mass percentage of the solution?",
                "options": ["14.28%", "12.50%", "10.00%", "25.00%"],
                "correct": 1,
                "solution": "Total mass of solution = 25 g (solute) + 175 g (solvent) = 200 g. Mass % = (Mass of Solute / Total Mass of Solution) × 100 = (25 / 200) × 100 = 12.50%."
            },
            {
                "q": "How many grams of common salt (NaCl) are required to prepare 250 g of a 12% (w/w) aqueous salt solution?",
                "options": ["12 g", "25 g", "30 g", "40 g"],
                "correct": 2,
                "solution": "Mass % = (Mass of solute / Mass of solution) × 100. Rearranging: Mass of solute = (Mass % × Mass of solution) / 100 = (12 × 250) / 100 = 30 g."
            },
            {
                "q": "If 20 mL of pure lemon juice is diluted with water to a total solution volume of 200 mL, what is the volume by volume percentage?",
                "options": ["5%", "10%", "15%", "20%"],
                "correct": 1,
                "solution": "Volume % = (Volume of solute / Total volume of solution) × 100 = (20 mL / 200 mL) × 100 = 10% (v/v)."
            },
            {
                "q": "The solubility of salt X in water at 25°C is 36 g per 100 g of water. If a student stirs 45 g of salt X into 100 g of water at 25°C, what will be observed?",
                "options": [
                    "All 45 g dissolves to give an unsaturated solution",
                    "36 g dissolves to form a saturated solution, and 9 g remains undissolved at the bottom",
                    "The solution boils vigorously",
                    "The water turns entirely into ice"
                ],
                "correct": 1,
                "solution": "At 25°C, exactly 36 g of salt dissolves in 100 g of water to reach saturation equilibrium. The remaining 9 g (45 g - 36 g) cannot dissolve and settles as undissolved solid."
            },
            {
                "q": "The solubility of potassium chloride (KCl) is 34 g at 20°C and 54 g at 80°C. If 200 g of water saturated with KCl at 80°C is cooled down to 20°C, what total mass of KCl crystals precipitates?",
                "options": ["20 g", "40 g", "54 g", "68 g"],
                "correct": 1,
                "solution": "In 100 g water, mass precipitating = 54 g - 34 g = 20 g. Therefore, in 200 g water, mass of KCl precipitating = 20 g × 2 = 40 g."
            },
            {
                "q": "What is the mass by volume percentage of a solution containing 15 g of sodium hydroxide dissolved in 300 mL of solution?",
                "options": ["3%", "5%", "15%", "20%"],
                "correct": 1,
                "solution": "Mass by volume % = (Mass of solute in g / Volume of solution in mL) × 100 = (15 / 300) × 100 = 5% (w/v)."
            },
            {
                "q": "Why does a hot saturated solution of copper sulfate begin to deposit blue crystals when allowed to cool slowly to room temperature?",
                "options": [
                    "Solubility of copper sulfate decreases as temperature drops, forcing excess solute out of solution",
                    "Water evaporates instantly upon cooling",
                    "Copper undergoes nuclear fission into sulfate",
                    "The glass beaker contracts and squeezes the solution"
                ],
                "correct": 0,
                "solution": "For copper sulfate, dissolution is endothermic and solubility decreases with lowering temperature. As the solution cools, the excess solute beyond the lower saturation limit crystallizes out."
            },
            {
                "q": "A 10% (w/w) aqueous sodium chloride solution has a mass of 500 g. How much water solvent is present in this solution?",
                "options": ["50 g", "450 g", "500 g", "400 g"],
                "correct": 1,
                "solution": "Mass of solute NaCl = 10% of 500 g = 50 g. Mass of solvent (water) = Total mass of solution - Mass of solute = 500 g - 50 g = 450 g."
            },
            {
                "q": "Which salt exhibits an almost flat solubility curve with very little increase in solubility from 0°C to 100°C?",
                "options": ["Potassium nitrate (KNO₃)", "Ammonium chloride (NH₄Cl)", "Sodium chloride (NaCl)", "Cerium sulfate"],
                "correct": 2,
                "solution": "Sodium chloride (NaCl) has an enthalpy of solution close to zero, so its solubility in water increases only very slightly (~35.7 g to ~39.8 g per 100 g water) between 0°C and 100°C."
            },
            {
                "q": "A solution contains 30 mL of ethanol in 120 mL of water. Assuming volumes are additive, what is the volume percentage of ethanol?",
                "options": ["25%", "20%", "15%", "30%"],
                "correct": 1,
                "solution": "Total volume of solution = 30 mL (solute) + 120 mL (solvent) = 150 mL. Volume % = (30 / 150) × 100 = 20% (v/v)."
            }
        ]
    },

    # SLIDE 19 - QUIZ 3
    {
        "id": 19,
        "title": "Dedicated Quiz Challenge 3: Separation Techniques & Principles",
        "subtitle": "Mastery Assessment: Sublimation, Centrifugation, Chromatography & Distillation (C-1.2, C-5.1)",
        "narration": "Welcome to Quiz Challenge 3! Put your knowledge of physical separation techniques to the test: from sublimation apparatus and chromatographic Rf values to Kannauj Deg-Bhapka distillation.",
        "questions": [
            {
                "q": "Which technique is best suited to separate a mixture of iodine crystals and sodium chloride?",
                "options": ["Simple filtration", "Sublimation", "Fractional distillation", "Centrifugation"],
                "correct": 1,
                "solution": "Iodine is a volatile sublimable solid that vaporizes directly upon gentle heating, while sodium chloride is non-volatile. Sublimation cleanly separates iodine on a cold surface."
            },
            {
                "q": "What physical property enables the separation of components in paper chromatography?",
                "options": [
                    "Differences in boiling points",
                    "Differences in partition solubility in the mobile phase and adsorption affinity for the stationary phase",
                    "Differences in magnetic susceptibility",
                    "Differences in mass density under gravity"
                ],
                "correct": 1,
                "solution": "Chromatography separates solutes based on their differential solubility in the moving solvent (mobile phase) versus their adsorption affinity to the stationary paper fibers."
            },
            {
                "q": "Simple distillation is strictly recommended only when two miscible liquids have a boiling point difference of at least:",
                "options": ["5°C", "10°C", "25°C", "100°C"],
                "correct": 2,
                "solution": "According to IUPAC and NCERT standards, simple distillation requires a boiling point difference greater than 25°C (or 25 K) to achieve clean single-stage separation."
            },
            {
                "q": "In the fractional distillation of crude liquid air, what is the correct sequence of gases evaporating as the column warms up?",
                "options": [
                    "Oxygen (-183°C) → Argon (-186°C) → Nitrogen (-196°C)",
                    "Nitrogen (-196°C) → Argon (-186°C) → Oxygen (-183°C)",
                    "Argon (-186°C) → Nitrogen (-196°C) → Oxygen (-183°C)",
                    "All three gases evaporate simultaneously at 0°C"
                ],
                "correct": 1,
                "solution": "Gases boil in ascending order of their boiling points: Nitrogen boils first at -196°C, followed by Argon at -186°C, leaving Oxygen liquid longest until -183°C."
            },
            {
                "q": "In Kannauj's traditional Deg-Bhapka perfume hydro-distillation (C-6.1), what is the function of the clay-and-cotton paste (multani mitti)?",
                "options": [
                    "It acts as a chemical fragrance enhancer",
                    "It provides a leak-proof hermetic seal on the copper Deg rim to prevent aromatic steam escape",
                    "It absorbs all water vapor so only oil passes",
                    "It keeps the fire cool"
                ],
                "correct": 1,
                "solution": "The traditional multani mitti and cotton wrap hermetically seals the rim of the copper Deg still, ensuring aromatic steam builds pressure and flows through the Chonga without leaking."
            },
            {
                "q": "Which mixture CANNOT be separated by fractional distillation?",
                "options": [
                    "Crude petroleum into petrol, kerosene, and diesel",
                    "Liquid air into nitrogen, argon, and oxygen",
                    "Ethanol (78.3°C) and water (100°C)",
                    "Sand and common salt"
                ],
                "correct": 3,
                "solution": "Sand and salt is a solid-solid heterogeneous mixture; sand is insoluble in water while salt dissolves, so they are separated by dissolution, filtration, and crystallisation, not distillation."
            },
            {
                "q": "If the solvent front moves 8.0 cm and a blue dye spot moves 6.4 cm in a paper chromatogram, what is the Rf value of the blue dye?",
                "options": ["1.25", "0.80", "0.64", "0.16"],
                "correct": 1,
                "solution": "Rf = Distance travelled by solute / Distance travelled by solvent front = 6.4 cm / 8.0 cm = 0.80."
            },
            {
                "q": "What happens in a dairy separator when whole milk is spun at high rotational speeds?",
                "options": [
                    "Denser skimmed milk is driven to the outer perimeter, while lighter cream/butterfat collects near the central axis",
                    "Milk turns into solid cheese instantly",
                    "All protein molecules are destroyed by nuclear forces",
                    "Cream sinks to the bottom because fat is denser than water"
                ],
                "correct": 0,
                "solution": "Butterfat cream has lower density (~0.92 g/mL) than water and skimmed milk (~1.03 g/mL). Under centrifugal force, denser skimmed milk moves outward, while lighter cream concentrates near the center."
            },
            {
                "q": "Why is water circulated through the Liebig condenser from the bottom inlet to the top outlet?",
                "options": [
                    "To save water pressure",
                    "To ensure the cooling jacket remains completely filled with cold water without air pockets, maximizing heat exchange",
                    "To heat up the distillate quickly",
                    "To prevent glass from cracking due to sudden boiling"
                ],
                "correct": 1,
                "solution": "Introducing cold water at the bottom forces water to flow upward against gravity, filling the entire cooling jacket and eliminating air bubbles for maximum cooling efficiency."
            },
            {
                "q": "Which method is most suitable to separate volatile acetone from non-volatile dissolved mineral impurities?",
                "options": ["Simple distillation", "Paper chromatography", "Magnetic separation", "Sedimentation"],
                "correct": 0,
                "solution": "Acetone boils at 56°C and vaporizes, leaving non-volatile mineral impurities in the distillation flask; the pure condensed acetone is collected in the receiver."
            }
        ]
    },

    # SLIDE 20 - QUIZ 4
    {
        "id": 20,
        "title": "Dedicated Quiz Challenge 4: Water Purification, Pioneers & Artificial Blood",
        "subtitle": "Mastery Assessment: Alum Loading, Dr. Dilip Mahalanabis, Paperfuge & Future Chemistry (C-5.2, C-6.1, C-7.1, C-7.2)",
        "narration": "Welcome to the final Mastery Quiz Challenge! Synthesize your deep understanding across municipal water treatment, Dr. Dilip Mahalanabis's life-saving ORS formulation, the Paperfuge, and cutting-edge artificial blood colloidal chemistry.",
        "questions": [
            {
                "q": "During municipal water purification, what chemical role is performed by the addition of Potash Alum in the loading tank?",
                "options": [
                    "It disinfects water by killing 100% of bacterial viruses",
                    "Trivalent Al³⁺ ions neutralize negative surface charges on colloidal clay particles, causing them to aggregate into settlable flocs",
                    "It converts hard calcium ions into soft sodium ions",
                    "It acts as a synthetic bleaching agent"
                ],
                "correct": 1,
                "solution": "Colloidal clay particles carry negative surface charges that cause mutual repulsion. Alum releases Al³⁺ ions that neutralize these charges, enabling particles to coagulate into heavy flocs (loading) that quickly settle."
            },
            {
                "q": "What physiological mechanism enabled Dr. Dilip Mahalanabis's Oral Rehydration Solution (ORS) to stop deadly dehydration during the 1971 cholera crisis (C-6.1)?",
                "options": [
                    "Cholera toxin destroys all blood cells immediately",
                    "The intestinal SGLT1 co-transporter simultaneously carries sodium and glucose into mucosal cells, pulling water back into the blood by osmosis",
                    "Glucose chemically neutralizes the stomach hydrochloric acid",
                    "Sodium chloride coats the stomach with a waterproof rubber lining"
                ],
                "correct": 1,
                "solution": "Even when cholera toxin disrupts normal fluid transport, the SGLT1 carrier protein remains active. It co-transports sodium and glucose in 1:1 equimolar ratio across the intestinal epithelium, creating an osmotic gradient that pulls water back into circulation."
            },
            {
                "q": "Dr. Manu Prakash's Paperfuge (C-8.1) achieves up to 125,000 RPM by utilizing which mechanical physics principle?",
                "options": [
                    "A miniature rechargeable lithium-ion battery",
                    "Non-linear mechanics of twisting and unwinding braided strings coupled to a central disc (whirligig dynamics)",
                    "Steam pressure generated from boiling water",
                    "Magnetic levitation over superconducting coils"
                ],
                "correct": 1,
                "solution": "The Paperfuge is a purely manual device based on whirligig dynamics: rhythmic outward pulling on twisted strings stores and releases rotational kinetic energy, accelerating the paper disc up to 125,000 RPM."
            },
            {
                "q": "Which gas or compound is added at the final stage of municipal water treatment to ensure bactericidal disinfection before distribution?",
                "options": ["Helium gas", "Chlorine gas or bleaching powder (CaOCl₂)", "Nitrogen dioxide gas", "Carbon monoxide"],
                "correct": 1,
                "solution": "Chlorine (or bleaching powder) forms hypochlorous acid (HOCl) in water, a potent oxidizing agent that destroys pathogenic bacteria and viral microorganisms, rendering water potable."
            },
            {
                "q": "Why is Perfluorocarbon (PFC) emulsion investigated as a candidate for artificial blood substitutes (C-7.2)?",
                "options": [
                    "PFCs can dissolve up to 50 times more non-polar oxygen gas than blood plasma",
                    "PFCs are identical in amino acid sequence to human hemoglobin",
                    "PFCs replicate white blood cell phagocytosis",
                    "PFCs form blood clots automatically"
                ],
                "correct": 0,
                "solution": "Perfluorocarbons are synthetic fluorinated hydrocarbons that possess extraordinary non-polar gas solubility, dissolving ~40–50 mL of oxygen per 100 mL of fluid without requiring binding heme proteins."
            },
            {
                "q": "What fatal complication arises when unencapsulated cell-free hemoglobin is directly transfused into human blood vessels?",
                "options": [
                    "Cell-free hemoglobin scavenges nitric oxide (NO) from endothelial walls, causing profound vasoconstriction and hypertension",
                    "Hemoglobin evaporates into nitrogen gas inside the heart",
                    "Hemoglobin turns into bone marrow immediately",
                    "It causes instant hypothermia"
                ],
                "correct": 0,
                "solution": "Without the RBC membrane shield, free hemoglobin extravasates into blood vessel walls and binds nitric oxide (NO), destroying the primary vasodilator and causing severe arterial hypertension and kidney damage."
            },
            {
                "q": "What is the key advantage of micro-scale chemistry experiments (C-7.1) over traditional bulk laboratory demonstrations?",
                "options": [
                    "They require larger beakers and higher chemical costs",
                    "They minimize hazardous chemical consumption and waste generation while preserving full pedagogical discovery",
                    "They replace all chemicals with digital photographs",
                    "They produce toxic radioactive byproducts"
                ],
                "correct": 1,
                "solution": "Micro-scale experiments use minimal reagent quantities (drops/milligrams), significantly reducing environmental chemical waste, storage hazards, and costs while teaching core principles."
            },
            {
                "q": "The prestigious British medical journal The Lancet described which Indian medical breakthrough as 'potentially the most important medical advance of the 20th century'?",
                "options": [
                    "The synthesis of artificial insulin",
                    "Dr. Dilip Mahalanabis's field formulation and deployment of Oral Rehydration Solution (ORS)",
                    "The discovery of the electron microscope",
                    "The invention of the stethoscope"
                ],
                "correct": 1,
                "solution": "The Lancet bestowed this historic praise on Oral Rehydration Therapy (ORT/ORS) in 1978, recognising Dr. Mahalanabis's simple, scalable solution that has saved more than 50 million lives."
            },
            {
                "q": "In the municipal water treatment process, why must water pass through the sedimentation tank BEFORE entering the sand-gravel filtration tank?",
                "options": [
                    "To allow heavy sand and silt to settle first so they do not instantly clog the fine filtration beds",
                    "To heat the water to 100°C",
                    "To dissolve all river fish",
                    "To add toxic chlorine gas early"
                ],
                "correct": 0,
                "solution": "Sedimentation allows coarse, heavy suspended solids to settle gravitationally first; otherwise, these macroscopic particles would rapidly block and clog the pore spaces of fine filtration beds."
            },
            {
                "q": "Which of the following is NOT an essential ingredient in the standard WHO / Dr. Mahalanabis Oral Rehydration Solution?",
                "options": ["Sodium chloride (NaCl)", "Glucose (anhydrous)", "Potassium chloride (KCl)", "Concentrated Sulfuric acid (H₂SO₄)"],
                "correct": 3,
                "solution": "Sulfuric acid is a corrosive poison. Standard ORS contains sodium chloride, glucose, potassium chloride, and trisodium citrate (or sodium bicarbonate) in pure water."
            }
        ]
    }
]

