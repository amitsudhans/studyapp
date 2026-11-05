QUIZ_QUESTIONS = [
    # Challenge 1: Q1 - Q10 (Handpicking, Threshing, Winnowing, Sieving)
    {
        "id": 1,
        "question": "Which of the following is the primary criterion for separating impurities using the handpicking method?",
        "options": [
            "Difference in electrical conductivity",
            "Noticeable differences in particle size, colour, or shape when impurities are present in small quantities",
            "Difference in magnetic attraction",
            "Difference in boiling point"
        ],
        "answer": 1,
        "explanation": "Handpicking relies directly on human vision and manual dexterity to detect and pluck out impurities that contrast visibly in size, shape, or colour in small batches.",
        "solution_html": "<strong>Handpicking Criteria:</strong><br>• Visually distinct size, shape, or colour.<br>• Low percentage of total volume.<br>• Dry solid-solid mixture."
    },
    {
        "id": 2,
        "question": "Why is threshing performed after harvesting cereal crops like wheat and paddy?",
        "options": [
            "To wash the crops with river water",
            "To dislodge and detach grains from dry harvested stalks",
            "To ferment the stalks into vinegar",
            "To grind wheat into fine powder"
        ],
        "answer": 1,
        "explanation": "Threshing utilizes kinetic impact (beating bundles against logs or using mechanical rollers) to break the brittle connection between mature grains and dry stalks.",
        "solution_html": "<strong>Threshing Physics:</strong> Deceleration impact fractures the brittle attachment of seeds to the stalk, releasing grains without damaging them."
    },
    {
        "id": 3,
        "question": "A farmer is winnowing a threshed mixture of wheat and husk on a windy afternoon. Where will the wheat grains fall relative to the husk?",
        "options": [
            "Wheat grains blow far away, while husk falls straight down",
            "Wheat grains fall almost vertically to form a heap below, while lighter husk is carried away by the wind",
            "Both wheat and husk fall into the exact same spot",
            "Neither falls; both float into the stratosphere"
        ],
        "answer": 1,
        "explanation": "Heavier wheat grains experience greater gravitational pull and minimal wind deflection, falling vertically. Lightweight, high-surface-area husk is carried horizontally by the breeze.",
        "solution_html": "<strong>Aerodynamic Winnowing:</strong><br>• Heavy grains = High inertia, falls straight down.<br>• Light husk = High drag-to-mass ratio, blown sideways."
    },
    {
        "id": 4,
        "question": "Which traditional bamboo tray is utilized by Indian farmers to oscillate and drop grain mixtures during winnowing?",
        "options": [
            "Kadhai",
            "Soop (Winnowing basket)",
            "Mathni",
            "Lota"
        ],
        "answer": 1,
        "explanation": "A soop is a flat, scoop-like bamboo woven tray designed to spread grain in a thin, steady trickle into cross-blowing wind.",
        "solution_html": "<strong>Cultural Heritage:</strong> The soop is celebrated in Kabir's dohas as a symbol of wisdom that discards empty superficiality."
    },
    {
        "id": 5,
        "question": "When making rotis, what component is retained on the fine mesh of a flour sieve (chalni)?",
        "options": [
            "Pure white starch powder",
            "Coarse wheat bran (choker) and husk fragments",
            "Liquid water drops",
            "Melted butter"
        ],
        "answer": 1,
        "explanation": "Fine flour particles pass through the tiny mesh perforations, while larger bran flakes and husk particles remain trapped on the screen.",
        "solution_html": "<strong>Sieving Cutoff:</strong> The mesh pore size acts as a geometric threshold separating fine endosperm flour from fibrous outer bran."
    },
    {
        "id": 6,
        "question": "Why is an inclined coarse wire sieve used at building construction sites?",
        "options": [
            "To separate fine sand from large pebbles, gravel, and stones",
            "To generate electrical power from falling rocks",
            "To dry sand by friction",
            "To attract magnetic minerals"
        ],
        "answer": 0,
        "explanation": "Masonry mortar and concrete plaster require fine, uniform sand particles; coarse stones roll off the inclined screen to prevent weak structural joints.",
        "solution_html": "<strong>Construction Sieving:</strong> Passing sand over an inclined wire grid filters out rocks and leaves fine aggregate for mortar."
    },
    {
        "id": 7,
        "question": "Why would winnowing be completely useless for separating a mixture of wheat grains and dried chickpea (chana) seeds?",
        "options": [
            "Because chickpeas are poisonous in wind",
            "Both components are heavy solids; wind cannot blow either of them away to form separate piles",
            "Wheat and chickpeas react to produce smoke",
            "Both components dissolve in moving air"
        ],
        "answer": 1,
        "explanation": "Winnowing requires a substantial difference in mass and aerodynamic drag (heavy grain vs paper-light husk). Since both wheat and chana are dense, both fall straight down.",
        "solution_html": "<strong>Winnowing Limitation:</strong> Requires one very light component (husk) and one heavy component (grain). Handpicking or sieving works here."
    },
    {
        "id": 8,
        "question": "Which modern machine executes reaping, threshing, and winnowing in a single continuous pass across crop fields?",
        "options": [
            "Rotary tiller",
            "Combine harvester",
            "Centrifugal cream separator",
            "Electric flour mill"
        ],
        "answer": 1,
        "explanation": "Combine harvesters combine all three stages: cutting the stalks (reaping), dislodging seeds (threshing), and blowing away chaff (winnowing).",
        "solution_html": "<strong>Mechanized Farming:</strong> The combine harvester integrates three distinct separation operations into a single continuous automated vehicle."
    },
    {
        "id": 9,
        "question": "Which of the following is an everyday example of handpicking?",
        "options": [
            "Filtering river water through sand beds",
            "Removing whole cloves and green chilies from a plate of biryani",
            "Skimming cream from boiled milk",
            "Evaporating salt in coastal pans"
        ],
        "answer": 1,
        "explanation": "Manually picking out discrete, visually contrasting spice pieces like cloves or chilies from a meal is classic handpicking.",
        "solution_html": "<strong>Visual Sorting:</strong> Picking spices or stones by hand utilizes optical and tactile discrimination."
    },
    {
        "id": 10,
        "question": "If you need to separate tiny iron filings mixed with chalk powder, why is handpicking impractical?",
        "options": [
            "Chalk powder is magnetic",
            "The particles are far too small and numerous for individual human fingers to grasp",
            "Iron filings evaporate at room temperature",
            "Chalk reacts with skin to form gold"
        ],
        "answer": 1,
        "explanation": "Microscopic and fine powders cannot be picked individually by fingers. A magnet should be used instead for rapid separation.",
        "solution_html": "<strong>Physical Scale:</strong> Particle diameter < 1 mm precludes manual picking; field forces (magnetism) must be used."
    },

    # Challenge 2: Q11 - Q20 (Evaporation, Salt Pans, Sedimentation, Decantation)
    {
        "id": 11,
        "question": "By which natural process is common salt commercially harvested from seawater in coastal areas?",
        "options": [
            "Magnetic extraction",
            "Evaporation driven by solar heat and wind",
            "Handpicking salt molecules",
            "Sublimation under ice"
        ],
        "answer": 1,
        "explanation": "Seawater in shallow pans absorbs heat from sunlight, causing water to evaporate into the atmosphere while non-volatile crystalline salt remains behind.",
        "solution_html": "<strong>Solar Evaporation:</strong> Water liquid converts to gas at ambient temperatures, concentrating the solution until NaCl precipitates."
    },
    {
        "id": 12,
        "question": "Which historic salt lake in Rajasthan is India's largest inland source of salt produced via solar evaporation?",
        "options": [
            "Dal Lake",
            "Sambhar Salt Lake",
            "Wular Lake",
            "Chilika Lake"
        ],
        "answer": 1,
        "explanation": "Sambhar Salt Lake in Rajasthan is a vast hypersaline playa lake where intense desert sunlight evaporates brine into mountains of edible salt.",
        "solution_html": "<strong>Indian Geography:</strong> Sambhar Lake produces a significant percentage of India's iodised edible and industrial salt."
    },
    {
        "id": 13,
        "question": "What happens when muddy river water is left completely undisturbed in a glass beaker for 20 minutes?",
        "options": [
            "Water boils and turns into ice",
            "Heavier insoluble soil particles settle down to the bottom due to gravity (Sedimentation)",
            "The mud dissolves and turns into clear blue ink",
            "The beaker loses all its mass"
        ],
        "answer": 1,
        "explanation": "In an undisturbed suspension, gravitational force causes particles denser than water to descend, forming a sediment layer at the bottom.",
        "solution_html": "<strong>Sedimentation Principle:</strong> Dense solid particles overcome convective currents and settle under gravitational acceleration."
    },
    {
        "id": 14,
        "question": "What is the process of gently pouring off the clear liquid above settled sediment called?",
        "options": [
            "Sublimation",
            "Decantation",
            "Threshing",
            "Distillation"
        ],
        "answer": 1,
        "explanation": "Decantation transfers the clear supernatant liquid into another vessel by tilting the container, leaving the solid sediment behind.",
        "solution_html": "<strong>Decantation:</strong> Pouring the supernatant liquid without disturbing the underlying sediment cake."
    },
    {
        "id": 15,
        "question": "Why is decantation considered an incomplete separation method for muddy water?",
        "options": [
            "Decantation destroys the water molecules",
            "Fine colloidal clay and organic particles remain suspended in water and pour over with the liquid",
            "Decanted water always freezes instantly",
            "Decantation leaves behind no liquid whatsoever"
        ],
        "answer": 1,
        "explanation": "Decantation only separates particles heavy enough to settle quickly. Fine silt and colloidal clay stay suspended and transfer into the second glass.",
        "solution_html": "<strong>Decantation Limits:</strong> Colloidal suspensions require filtration through micro-porous media to attain true optical clarity."
    },
    {
        "id": 16,
        "question": "In Activity 9.2, when a saltwater streak on black paper dries under sunlight, what is observed?",
        "options": [
            "The paper turns into molten glass",
            "Crisp white sparkling crystals of salt appear as water evaporates",
            "The black paper turns bright green",
            "The paper bursts into flames"
        ],
        "answer": 1,
        "explanation": "Water molecules absorb ambient heat and escape as invisible water vapour, leaving non-volatile sodium chloride crystals visible against the dark paper.",
        "solution_html": "<strong>Salt Solution Test:</strong> Black paper creates high visual contrast for observing white microcrystalline salt residue."
    },
    {
        "id": 17,
        "question": "Why does heating a salt solution in a china dish over a burner accelerate the separation of salt?",
        "options": [
            "Heat converts salt into liquid nitrogen",
            "Thermal energy dramatically increases the rate of evaporation, boiling water away in minutes",
            "Heat destroys all bacteria in the china dish",
            "Burners create strong magnetic fields"
        ],
        "answer": 1,
        "explanation": "Supplying active thermal energy raises water temperature to its boiling point (100°C), driving rapid vaporization while salt (boiling point 1465°C) stays behind.",
        "solution_html": "<strong>Kinetic Energy:</strong> Heat supplies the latent heat of vaporization, drastically speeding up solvent loss."
    },
    {
        "id": 18,
        "question": "In traditional Ayurveda, why are medicinal herbs like Tulsi and Neem dried in the shade (Chhaya-Shushka)?",
        "options": [
            "To allow insects to eat the leaves",
            "To gently evaporate moisture without degrading delicate heat-sensitive therapeutic compounds and essential oils",
            "To prevent leaves from absorbing gravity",
            "To freeze the herbs into stone"
        ],
        "answer": 1,
        "explanation": "Direct harsh solar UV and high heat break down phytochemicals. Gentle shade evaporation removes water to prevent mould while locking in medicinal potency.",
        "solution_html": "<strong>Ayurvedic Heritage:</strong> Shade drying removes water activity ($a_w$) while preventing thermal pyrolysis of active principles."
    },
    {
        "id": 19,
        "question": "Before cooking dal or rice, cooks rinse them in a pot with water and pour off the cloudy rinse water. Which two processes are occurring?",
        "options": [
            "Evaporation and condensation",
            "Sedimentation (grains sink) followed by decantation (cloudy water poured off)",
            "Threshing and winnowing",
            "Magnetic separation and sieving"
        ],
        "answer": 1,
        "explanation": "Heavy rice grains settle quickly to the bottom (sedimentation), allowing the cook to tilt the pot and discard the murky wash water containing dust (decantation).",
        "solution_html": "<strong>Culinary Science:</strong> Washing rice is a classical two-phase gravity settling and decanting operation."
    },
    {
        "id": 20,
        "question": "Can a mixture of two completely miscible liquids like oil and water be separated by simple sedimentation and decantation?",
        "options": [
            "No, because oil and water evaporate together",
            "Yes, because oil and water do not mix (immiscible) and form two distinct density layers that can be decanted",
            "No, because oil turns into solid ice at room temperature",
            "Yes, but only by using an electromagnet"
        ],
        "answer": 1,
        "explanation": "Oil is immiscible and less dense than water, floating on top as a distinct layer. Decantation or a separating funnel cleanly isolates the upper oil layer.",
        "solution_html": "<strong>Liquid-Liquid Decantation:</strong> Immiscible liquids with different densities stratify into distinct layers separated by gravity."
    },

    # Challenge 3: Q21 - Q30 (Filtration, Filter Paper Cone, Residue/Filtrate, Churning)
    {
        "id": 21,
        "question": "What is the fundamental working principle of filtration?",
        "options": [
            "Using magnetic coils to repel liquid",
            "Passing a solid-liquid mixture through a porous barrier with pores small enough to trap solids while permitting liquid to pass",
            "Boiling the liquid until both components turn into gas",
            "Exposing the mixture to high-frequency sound"
        ],
        "answer": 1,
        "explanation": "Filtration relies on pore-size exclusion: liquid molecules permeate the pores, while insoluble solid particles larger than the pores are physically intercepted.",
        "solution_html": "<strong>Filtration Principle:</strong> Geometric size exclusion across a porous membrane or fibrous matrix."
    },
    {
        "id": 22,
        "question": "In laboratory filtration of muddy water, what is the clear liquid collected in the flask called?",
        "options": [
            "Residue",
            "Filtrate",
            "Precipitate",
            "Sediment"
        ],
        "answer": 1,
        "explanation": "The liquid that passes through the filter medium and collects in the receiving vessel is scientifically termed the filtrate.",
        "solution_html": "<strong>Terminology:</strong><br>• Filtrate = Permeated clear liquid.<br>• Residue = Retained solid cake."
    },
    {
        "id": 23,
        "question": "What is the solid material collected and retained on the filter paper called?",
        "options": [
            "Filtrate",
            "Residue",
            "Solvent",
            "Distillate"
        ],
        "answer": 1,
        "explanation": "The insoluble solid particles intercepted and retained on the filter surface are termed the residue.",
        "solution_html": "<strong>Terminology:</strong> The retentate trapped by pore exclusion is universally designated the residue."
    },
    {
        "id": 24,
        "question": "How many folds are made to a circular filter paper to prepare it for insertion into a 60° glass funnel?",
        "options": [
            "One fold into a circle",
            "Folded in half into a semicircle, then folded again into a quadrant, and opened into a cone",
            "Torn into ten strips",
            "Crushed into a sphere"
        ],
        "answer": 1,
        "explanation": "Two sequential perpendicular folds yield a 4-ply quadrant. Opening three plies on one side creates a conical geometry with a 60° apex angle.",
        "solution_html": "<strong>Filter Cone Folding:</strong> Circle ➔ Semicircle (180°) ➔ Quadrant (90°) ➔ Open 3-and-1 ply cone (60°)."
    },
    {
        "id": 25,
        "question": "Which household kitchen item is a direct everyday application of filtration?",
        "options": [
            "A tea strainer separating tea leaves from brewed chai",
            "A rolling pin flattening roti dough",
            "A stainless steel spoon stirring soup",
            "An oven baking a cake"
        ],
        "answer": 0,
        "explanation": "The mesh of a tea strainer permits liquid chai to flow through while physically blocking and retaining solid spent tea leaves.",
        "solution_html": "<strong>Daily Filtration:</strong> Wire strainers, coffee filter papers, and muslin cloth are household filters."
    },
    {
        "id": 26,
        "question": "When curd is churned in a traditional pot with a mathni, why does butter rise and float to the surface?",
        "options": [
            "Butter is strongly magnetic",
            "Butter fat has a lower density than the watery buttermilk, making it buoyant",
            "Butter reacts with oxygen to turn into helium gas",
            "Curd contains heavy stones that push butter up"
        ],
        "answer": 1,
        "explanation": "Milk fat has a density of ~0.91 g/cm³, whereas water is 1.0 g/cm³ and buttermilk serum is ~1.03 g/cm³. The lighter fat floats on top.",
        "solution_html": "<strong>Buoyancy in Churning:</strong> Coalesced lipid globules possess lower specific gravity than the aqueous serum, driving upward phase separation."
    },
    {
        "id": 27,
        "question": "What is the liquid that remains at the bottom of the pot after butter is skimmed off during churning?",
        "options": [
            "Pure alcohol",
            "Buttermilk (chhach / mattha)",
            "Kerosene oil",
            "Distilled vinegar"
        ],
        "answer": 1,
        "explanation": "Churning curd yields two delicious and valuable food products: solid floating butter (makhan) and liquid seasoned buttermilk (chhach).",
        "solution_html": "<strong>Dairy Separation:</strong> Curd emulsion separates into insoluble lipid phase (butter) and aqueous protein-rich serum (buttermilk)."
    },
    {
        "id": 28,
        "question": "Why is a fine muslin cloth used instead of a coarse sieve when straining freshly coagulated paneer (cottage cheese)?",
        "options": [
            "Muslin cloth is magnetic",
            "Muslin has tight, flexible microscopic pores that retain soft curd protein curds while draining watery whey liquid",
            "Muslin heats the cheese to 500°C",
            "Coarse sieves would dissolve the paneer completely"
        ],
        "answer": 1,
        "explanation": "Soft, delicate casein protein curd blocks would squeeze through coarse holes. Muslin cloth has the ideal pore density to retain curds while draining liquid whey.",
        "solution_html": "<strong>Cheese Straining:</strong> Muslin cloth has tight, flexible microscopic pores that retain soft curd protein blocks while draining liquid whey."
    },
    {
        "id": 29,
        "question": "How do nylon fishing nets function as large-scale environmental filters in rivers and oceans?",
        "options": [
            "They chemically purify the river water into alcohol",
            "They allow water molecules to flow freely through the mesh while retaining fish larger than the mesh opening",
            "They freeze fish using electricity",
            "They attract fish using magnetic fields"
        ],
        "answer": 1,
        "explanation": "A fishing net is a macroscopic sieve/filter: water passes through with minimal resistance, while fish larger than the mesh gauge are retained.",
        "solution_html": "<strong>Macroscopic Filtration:</strong> Net aperture acts as a mechanical cutoff selecting organisms based on dimensional size."
    },
    {
        "id": 30,
        "question": "Which vital biological organ inside the human body acts as a continuous microscopic blood filter, filtering over 180 litres of fluid daily?",
        "options": [
            "The stomach",
            "The kidneys (nephrons)",
            "The skeletal bones",
            "The vocal cords"
        ],
        "answer": 1,
        "explanation": "The human kidneys contain millions of microscopic capillary filters called glomeruli that filter blood, retaining cells/proteins and expelling wastes in urine.",
        "solution_html": "<strong>Biological Filtration:</strong> Renal nephrons perform ultrafiltration driven by blood hydrostatic pressure across specialized cell membranes."
    },

    # Challenge 4: Q31 - Q40 (Magnetic Sorting, Industrial Scrap Cranes, Multi-Step Workflows)
    {
        "id": 31,
        "question": "Which of the following metals can be cleanly separated from a mixture of saw-dust using a hand magnet?",
        "options": [
            "Pure copper filings",
            "Iron nails and steel screws",
            "Aluminum foil shavings",
            "Gold dust"
        ],
        "answer": 1,
        "explanation": "Iron and steel are ferromagnetic materials that experience strong magnetic attraction. Wood, copper, aluminum, and gold are non-magnetic under ordinary conditions.",
        "solution_html": "<strong>Ferromagnetism:</strong> Only iron, nickel, cobalt, and certain alloys are attracted by standard permanent magnets."
    },
    {
        "id": 32,
        "question": "How do industrial recycling cranes separate heavy steel scrap from municipal waste heaps?",
        "options": [
            "They blow giant air fans over the garbage",
            "They use massive electromagnets that attract iron and steel when electrified and release them when switched off",
            "They boil the entire dump in acid",
            "They use sound waves to dissolve plastic"
        ],
        "answer": 1,
        "explanation": "Cranes with large electromagnets generate massive magnetic fields to lift tonnes of ferrous metal. When moved over a hopper, the current is turned off, dropping the load.",
        "solution_html": "<strong>Industrial Electromagnetics:</strong> Solenoid coils produce switchable magnetic fields ($B \\propto I$) for batch material handling."
    },
    {
        "id": 33,
        "question": "In iron ore processing plants, how are rich magnetite minerals separated from worthless non-magnetic rocky gangue?",
        "options": [
            "By boiling crushed rock in vegetable oil",
            "By passing crushed ore over rotating magnetic conveyor pulleys",
            "By burning the rock with gunpowder",
            "By handpicking every sand grain"
        ],
        "answer": 1,
        "explanation": "Crushed ore travels along a conveyor belt with a magnetic head pulley. Magnetic magnetite hugs the belt and drops into one chute; non-magnetic rock flies off into another.",
        "solution_html": "<strong>Mineral Beneficiation:</strong> Continuous magnetic pulleys sort crushed ore into magnetic concentrate and non-magnetic tailings."
    },
    {
        "id": 34,
        "question": "To completely separate a dry mixture of common salt, sand, and iron pins, what is the first logical separation step?",
        "options": [
            "Boil the dry mixture to 1000°C",
            "Run a magnet over the mixture to instantly remove the iron pins",
            "Add 10 litres of water and stir",
            "Burn the mixture in an oven"
        ],
        "answer": 1,
        "explanation": "Using a magnet first takes advantage of the dry state to extract all sharp iron pins cleanly without wetting or rusting them.",
        "solution_html": "<strong>Separation Strategy:</strong> Always remove dry magnetic components first before introducing liquid solvents."
    },
    {
        "id": 35,
        "question": "After removing iron pins from a salt and sand mixture, what is the next step to separate the sand from the salt?",
        "options": [
            "Sieve through a cloth",
            "Add water to dissolve the salt, then filter out the insoluble sand",
            "Freeze the dry powder",
            "Winnow with a hair dryer"
        ],
        "answer": 1,
        "explanation": "Salt is highly soluble in water, while sand is completely insoluble. Adding water dissolves the salt, enabling mechanical filtration to catch the sand.",
        "solution_html": "<strong>Differential Solubility:</strong> Salt dissolves into aqueous phase; sand remains solid and is caught on filter paper."
    },
    {
        "id": 36,
        "question": "After filtering out sand from a saltwater solution, how can you recover both dry salt AND liquid water?",
        "options": [
            "Leave the beaker in a dark cupboard",
            "Heat the solution in a distillation apparatus or covered kettle, condensing the steam on a cooled surface to collect pure water, while dry salt remains behind",
            "Throw the solution away and buy new salt",
            "Stir the liquid with a wooden stick"
        ],
        "answer": 1,
        "explanation": "Distillation/condensation captures vaporized water when it contacts a cool surface, liquefying it into a separate beaker while non-volatile salt crystals remain in the boiler.",
        "solution_html": "<strong>Complete Recovery:</strong> Evaporation vaporizes the solvent; condensation captures it as pure distillate."
    },
    {
        "id": 37,
        "question": "Why is it important to select the correct separation method based on physical properties rather than guessing?",
        "options": [
            "Guessing changes the laws of physics",
            "Each method relies on specific differences like particle size, density, solubility, boiling point, or magnetism; matching the method guarantees clean, efficient separation",
            "Incorrect methods will always cause nuclear explosions",
            "Science forbids trying new experiments"
        ],
        "answer": 1,
        "explanation": "Separation processes are thermodynamic and mechanical unit operations designed around specific property differences (size, mass, magnetism, volatility).",
        "solution_html": "<strong>Scientific Principle:</strong> Matching the separation technique to physical properties ensures clean, efficient, and reproducible separation."
    },
    {
        "id": 38,
        "question": "Which of the following mixtures CANNOT be separated by filtration through standard filter paper?",
        "options": [
            "Mud particles suspended in water",
            "Chalk powder stirred in water",
            "Sugar completely dissolved in warm water",
            "Coarse coffee grounds suspended in water"
        ],
        "answer": 2,
        "explanation": "Dissolved sugar molecules are dispersed at the molecular level (~1 nm) and pass freely through filter paper pores (~2–10 µm) alongside water molecules.",
        "solution_html": "<strong>Homogeneous Solutions:</strong> Solute molecules in true solutions cannot be caught by physical filter pores; evaporation is required."
    },
    {
        "id": 39,
        "question": "What is the primary difference between sieving and filtration?",
        "options": [
            "Sieving only separates gases, while filtration only separates solids",
            "Sieving separates dry solid mixtures of varying particle sizes, whereas filtration typically separates insoluble solids from liquids",
            "Sieving uses magnets, while filtration uses electricity",
            "There is no difference; they are identical words"
        ],
        "answer": 1,
        "explanation": "Sieving is predominantly used for dry solid-solid classification (flour bran, construction sand), while filtration separates insoluble solid phases from liquid suspensions.",
        "solution_html": "<strong>Unit Operations:</strong><br>• Sieving: Solid-Solid mechanical size separation.<br>• Filtration: Solid-Liquid phase separation."
    },
    {
        "id": 40,
        "question": "How does learning methods of separation empower students in everyday life and environmental sustainability?",
        "options": [
            "It allows students to turn garbage into gold",
            "It teaches practical skills for purifying drinking water, preparing wholesome food, recycling metal resources, and reducing environmental waste",
            "It eliminates the need for farming crops",
            "It makes food cook instantly without fire"
        ],
        "answer": 1,
        "explanation": "Separation science is the bedrock of clean drinking water, food hygiene, circular scrap metal recycling, and environmental waste management.",
        "solution_html": "<strong>Scientific Empowerment:</strong> Mastering separation principles fosters resource conservation, sustainable waste sorting, and public health."
    }
]
