"""
Class 6 Science Chapter 11: Nature's Treasures
Part 3: 40 Quiz Questions across 4 Mastery Challenge Slides (Slides 17 to 20)
Every question contains id, question, options, answer, explanation, and solution_html.
Zero raw LaTeX. Pure clean Unicode.
"""

QUIZ_QUESTIONS = [
    # Challenge 1: Questions 1 to 10 (Slide 17)
    {
        "id": 1,
        "question": "Which of the following is classified as a genuine natural resource rather than a human-made synthetic creation?",
        "options": [
            "A molded plastic bucket",
            "A fertile alluvial riverbank soil",
            "A multi-lane asphalt expressway",
            "A synthetic nylon fishing net"
        ],
        "answer": 1,
        "explanation": "Natural resources are materials provided directly by Earth without human manufacture, such as fertile topsoil, clean air, sunlight, and freshwater.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Natural vs. Human-Made:</strong> Natural resources originate directly from the lithosphere, hydrosphere, atmosphere, or biosphere without industrial processing.</p>
            <p>2. <strong>Analysis of Options:</strong> Plastic buckets, asphalt roads, and nylon nets are synthetic materials manufactured by human industry.</p>
            <p>3. <strong>Conclusion:</strong> Alluvial soil is formed naturally over centuries through geological rock weathering and organic matter decay (Option B).</p>
        """
    },
    {
        "id": 2,
        "question": "In Activity 11.1, why does holding one's breath for more than a minute trigger an uncontrollable physical reflex to inhale fresh air?",
        "options": [
            "Because lungs fill with solid gold crystals that must be emptied",
            "Because body tissues and brain cells continuously require oxygen to carry out cellular respiration and maintain life",
            "Because human beings prefer eating air instead of vegetables",
            "Because the heart ceases to beat whenever the mouth is closed"
        ],
        "answer": 1,
        "explanation": "Cellular respiration requires oxygen every second to combust glucose into ATP. Lack of oxygen causes rapid hypoxia and carbon dioxide buildup, triggering the brain's breathing reflex.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Physiological Necessity:</strong> Aerobic cells cannot store oxygen; they depend on uninterrupted pulmonary gas exchange.</p>
            <p>2. <strong>Respiratory Reflex:</strong> As oxygen levels drop and arterial carbon dioxide rises, the respiratory center in the medulla oblongata forces diaphragm contraction.</p>
            <p>3. <strong>Conclusion:</strong> Continuous cellular demand for oxygen makes holding breath for long periods impossible (Option B).</p>
        """
    },
    {
        "id": 3,
        "question": "What is the relative proportion of gases in Earth's clean atmospheric air by volume?",
        "options": [
            "50% Oxygen, 50% Carbon dioxide",
            "78% Nitrogen, 21% Oxygen, and roughly 1% Argon, Carbon Dioxide, and other trace gases",
            "90% Hydrogen, 10% Helium",
            "78% Carbon dioxide, 21% Methane, 1% Oxygen"
        ],
        "answer": 1,
        "explanation": "Earth's atmosphere consists of approximately 78% nitrogen, 21% oxygen, and 1% other gases (argon 0.93%, carbon dioxide 0.04%, water vapour, and noble gases).",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Major Component:</strong> Nitrogen (N₂) comprises ~78% of dry atmospheric air.</p>
            <p>2. <strong>Vital Oxidant:</strong> Oxygen (O₂) comprises ~21%.</p>
            <p>3. <strong>Minor Constituents:</strong> Argon (~0.93%), Carbon dioxide (~0.04%), water vapour, and noble gases constitute the remaining ~1%.</p>
            <p>4. <strong>Conclusion:</strong> Option B correctly states the precise atmospheric composition.</p>
        """
    },
    {
        "id": 4,
        "question": "What vital ecological role does inert nitrogen gas (78% of air) play in supporting terrestrial plant growth?",
        "options": [
            "Plants inhale nitrogen gas directly through flowers to illuminate at night",
            "Nitrogen is converted by soil bacteria into nitrates and ammonium, synthesizing essential plant proteins",
            "Nitrogen freezes soil so weeds cannot grow",
            "Nitrogen turns rainwater into sweet honey"
        ],
        "answer": 1,
        "explanation": "Atmospheric nitrogen cannot be absorbed directly by plants, but nitrogen-fixing bacteria (like Rhizobium) convert it into soluble nitrates that plants absorb to build proteins.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Biological Nitrogen Fixation:</strong> Gaseous N₂ has a strong triple chemical bond. Specialized diazotrophic bacteria fix it into ammonia (NH₃) and nitrates (NO₃⁻).</p>
            <p>2. <strong>Protein Synthesis:</strong> Absorbed nitrates are combined with glucose from photosynthesis to synthesize amino acids, the building blocks of plant enzymes and proteins.</p>
            <p>3. <strong>Conclusion:</strong> Option B provides the accurate biological mechanism.</p>
        """
    },
    {
        "id": 5,
        "question": "Why does clean atmospheric air not ignite in uncontrollable flames despite containing 21% oxygen?",
        "options": [
            "Because atmospheric air is frozen solid at all times",
            "Because the high concentration of inert nitrogen (78%) dilutes oxygen, moderating the rate of chemical combustion",
            "Because oxygen only catches fire when mixed with ocean salt",
            "Because gravity prevents oxygen from interacting with fuels"
        ],
        "answer": 1,
        "explanation": "Nitrogen acts as a natural chemical buffer. By diluting oxygen to 21%, it prevents runaway combustion and keeps fires manageable on Earth.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Combustion Chemistry:</strong> Oxygen supports combustion, while pure nitrogen is chemically inert under ambient temperatures.</p>
            <p>2. <strong>Buffering Effect:</strong> The 4:1 ratio of nitrogen to oxygen ensures that burning requires an ignition source and proceeds at a controlled, sustainable rate.</p>
            <p>3. <strong>Conclusion:</strong> Inert nitrogen moderates oxygen's reactivity (Option B).</p>
        """
    },
    {
        "id": 6,
        "question": "What scientific principle is demonstrated by constructing and spinning a traditional paper firki (pinwheel)?",
        "options": [
            "Moving air (wind) possesses kinetic energy that exerts mechanical force on tilted blades, producing rotation",
            "Paper can generate electricity without touching any air",
            "Cold air destroys the weight of wooden sticks",
            "Air is a vacuum that pulls objects towards the Moon"
        ],
        "answer": 0,
        "explanation": "A firki demonstrates aerodynamic lift and drag: moving air molecules collide with the angled paper vanes, transferring their kinetic energy into rotational mechanical work.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Kinetic Energy Transfer:</strong> Wind is air in motion. The velocity of moving air molecules confers kinetic energy (E = 0.5 * m * v²).</p>
            <p>2. <strong>Blade Geometry:</strong> The angled folds of the firki deflect air currents, causing a pressure differential that spins the pinwheel on its axle.</p>
            <p>3. <strong>Conclusion:</strong> Option A describes the exact physical mechanism.</p>
        """
    },
    {
        "id": 7,
        "question": "How do modern commercial wind turbine generators convert natural wind into electrical power?",
        "options": [
            "Wind blades catch wind to spin an internal rotor shaft connected to an electromagnetic generator",
            "Wind friction heats the blades until they melt into liquid electricity",
            "Turbines collect wind in plastic bags and compress it into batteries",
            "Windmills use coal burners inside the nacelle to generate steam"
        ],
        "answer": 0,
        "explanation": "Wind turns the aerodynamic rotor blades, spinning a low-speed shaft, gearbox, and high-speed generator shaft. Electromagnetic induction converts this rotational kinetic energy into electricity.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Aerodynamic Lift:</strong> Airflow across aerofoil blades generates rotational torque.</p>
            <p>2. <strong>Faraday's Induction:</strong> The rotating shaft turns copper coils within powerful magnetic fields inside the generator, producing electric alternating current (AC).</p>
            <p>3. <strong>Conclusion:</strong> Option A outlines the standard wind-to-electricity conversion.</p>
        """
    },
    {
        "id": 8,
        "question": "Which of the following locations hosts the famous Muppandal Wind Farm, renowned as one of India's largest onshore wind energy facilities?",
        "options": [
            "Kanyakumari district, Tamil Nadu",
            "Thar Desert, Jaisalmer, Rajasthan",
            "Dhule district, Maharashtra",
            "Rann of Kutch, Gujarat"
        ],
        "answer": 0,
        "explanation": "Muppandal Wind Farm is located in Kanyakumari district, Tamil Nadu, benefiting from seasonal high-velocity winds channeled through a mountain gap in the Western Ghats.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Geographic Advantage:</strong> The Muppandal pass in the Western Ghats acts as a natural wind funnel between the Arabian Sea and the Bay of Bengal.</p>
            <p>2. <strong>Capacity:</strong> It has an installed capacity exceeding 1,500 MW, making it one of the largest onshore wind complexes in the world.</p>
            <p>3. <strong>Conclusion:</strong> Located in Kanyakumari, Tamil Nadu (Option A).</p>
        """
    },
    {
        "id": 9,
        "question": "What is the primary difference between a gentle atmospheric 'breeze' and a violent 'gale' or 'storm'?",
        "options": [
            "A breeze contains oxygen while a storm contains only helium",
            "A breeze consists of slow, gentle air movement, whereas a storm involves high-velocity moving air carrying immense kinetic energy",
            "A breeze moves upwards towards the stars, while storms only occur underground",
            "There is no physical difference in wind speed or pressure"
        ],
        "answer": 1,
        "explanation": "Wind classification is based on air velocity and atmospheric pressure gradients. Breezes have low speed (gentle), while storms have high velocity capable of causing structural damage.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Beaufort Scale:</strong> Wind speeds range from calm (under 1 km/h) and gentle breezes (12–19 km/h) to gales (62–74 km/h) and storm cyclones (>100 km/h).</p>
            <p>2. <strong>Energy Impact:</strong> Kinetic energy scales with the square of wind velocity, meaning storm winds carry hundreds of times more destructive power than a light breeze.</p>
            <p>3. <strong>Conclusion:</strong> Option B correctly distinguishes them based on air velocity.</p>
        """
    },
    {
        "id": 10,
        "question": "Why is wind energy considered a 100% clean and renewable power source?",
        "options": [
            "Because wind turbines consume huge amounts of diesel to create wind",
            "Because wind is naturally driven by solar heating of the Earth and generates electricity without burning fuels or emitting greenhouse gases",
            "Because wind energy stops rain from falling on agricultural fields",
            "Because windmills can only be constructed from solid edible sugar"
        ],
        "answer": 1,
        "explanation": "Wind is generated by uneven solar thermal heating of Earth's atmosphere. Harnessing wind consumes no chemical fuels, produces zero greenhouse gas emissions, and never depletes.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Renewable Nature:</strong> As long as the Sun shines and Earth rotates, atmospheric pressure differentials will continue to generate wind currents indefinitely.</p>
            <p>2. <strong>Zero Emissions:</strong> Operational wind turbines emit zero carbon dioxide, sulfur oxides, or particulate matter during electricity generation.</p>
            <p>3. <strong>Conclusion:</strong> Option B provides the rigorous scientific justification.</p>
        """
    },

    # Challenge 2: Questions 11 to 20 (Slide 18)
    {
        "id": 11,
        "question": "What percentage of Earth's total water reserves is saline ocean water, and why is it unsuited for direct agricultural irrigation?",
        "options": [
            "50%; because it contains too much dissolved sugar",
            "Over 97%; because its high concentration of dissolved salts draws water out of plant roots via osmosis and damages crops",
            "25%; because ocean water is frozen into solid iron blocks",
            "100%; because all water on Earth contains toxic chemical dyes"
        ],
        "answer": 1,
        "explanation": "Over 97% of Earth's water resides in saline oceans (approx. 3.5% salinity). High salt concentration causes hypertonic osmotic shock, dehydrating and killing terrestrial crops.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Ocean Dominance:</strong> Approximately 97.5% of all planetary water is held in oceans and saline seas.</p>
            <p>2. <strong>Osmotic Mechanism:</strong> Saline water has higher solute concentration than plant root cell sap. Instead of absorbing water, root cells lose water by exosmosis, causing fatal wilting.</p>
            <p>3. <strong>Conclusion:</strong> Option B accurately explains both the percentage and physiological barrier.</p>
        """
    },
    {
        "id": 12,
        "question": "Where is the largest portion of Earth's 2.5% freshwater locked away, making it inaccessible for immediate daily human consumption?",
        "options": [
            "In household swimming pools and bathtubs",
            "In polar ice sheets, glaciers, and deep subterranean aquifers",
            "In atmospheric clouds over the Sahara Desert",
            "In plastic bottled water warehouses"
        ],
        "answer": 1,
        "explanation": "Nearly 69% of Earth's freshwater is trapped in polar ice caps and alpine glaciers (Antarctica, Greenland, Himalayas), and roughly 30% is deep groundwater.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Freshwater Breakdown:</strong> Out of total freshwater (2.5%): ~68.7% is frozen in ice caps/glaciers; ~30.1% is groundwater; only ~1.2% is surface and atmospheric water.</p>
            <p>2. <strong>Accessibility:</strong> Polar ice is remote and solid, while deep aquifers require deep drilling.</p>
            <p>3. <strong>Conclusion:</strong> Polar ice and deep aquifers hold the vast majority (Option B).</p>
        """
    },
    {
        "id": 13,
        "question": "In the famous 'Bucket Analogy', if a 10-liter bucket represents all the water on planet Earth, how much represents readily accessible liquid surface freshwater (rivers, lakes)?",
        "options": [
            "Five full 10-liter buckets",
            "Roughly half a bucket (5 liters)",
            "Barely a single drop of water (less than 0.01 liters)",
            "Two large teacups"
        ],
        "answer": 2,
        "explanation": "Accessible surface freshwater (rivers, freshwater lakes) represents less than 0.01% of total global water. On a 10-liter scale, it equates to barely a fraction of a single droplet!",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Mathematical Proportions:</strong> Total water = 10,000 mL (10 L). Total freshwater (~2.5%) = 250 mL (one cup).</p>
            <p>2. <strong>Accessible Surface Water:</strong> Rivers and lakes represent ~0.009% of total water: 10,000 mL * 0.00009 = 0.9 mL, which is barely one to two small water drops.</p>
            <p>3. <strong>Conclusion:</strong> Option C vividly captures Earth's freshwater scarcity.</p>
        """
    },
    {
        "id": 14,
        "question": "In Activity 11.3 (water audit), how much clean treated water is typically wasted if a tap is left running while brushing teeth for two minutes?",
        "options": [
            "Zero liters, because water immediately loops back into the faucet",
            "About 10 to 15 liters of water",
            "Over 5,000 liters of water",
            "Exactly 50 milliliters"
        ],
        "answer": 1,
        "explanation": "A standard bathroom tap discharges water at 5 to 7.5 liters per minute. Leaving it running while brushing teeth for two minutes wastes 10 to 15 liters.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Flow Rate:</strong> Municipal domestic taps have an average flow rate of ~6 L/min under typical water pressure.</p>
            <p>2. <strong>Calculation:</strong> 2 minutes * 6 L/min = 12 Liters wasted.</p>
            <p>3. <strong>Conservation Fix:</strong> Using a single mug (0.25 L) saves over 95% of this water.</p>
            <p>4. <strong>Conclusion:</strong> 10 to 15 liters are squandered (Option B).</p>
        """
    },
    {
        "id": 15,
        "question": "What is the primary function of a dripping tap being repaired promptly with a new rubber washer?",
        "options": [
            "It turns the tap into an electric generator",
            "It prevents wasting over 30 liters per day (more than 10,000 liters per year) from continuous leaking",
            "It changes the color of tap water from clear to green",
            "It stops the sound of the television from being heard"
        ],
        "answer": 1,
        "explanation": "A single leak dripping once per second squanders roughly 30 to 35 liters of water every 24 hours, exceeding 10,000 liters across a full year.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Cumulative Volume:</strong> 1 drip/sec = 60 drips/min = 3,600 drips/hr = 86,400 drips/day. At ~0.35 mL per drip, this totals ~30.2 Liters per day.</p>
            <p>2. <strong>Annual Impact:</strong> 30.2 L/day * 365 days = ~11,000 Liters wasted per year from a single faulty tap washer.</p>
            <p>3. <strong>Conclusion:</strong> Repairing washers eliminates massive cumulative waste (Option B).</p>
        """
    },
    {
        "id": 16,
        "question": "What architectural and hydrological purpose did traditional stepwells (Bawadi in Rajasthan, Vav in Gujarat) serve in ancient India?",
        "options": [
            "They were built as underground prison dungeons for pirates",
            "They captured monsoon runoff and allowed subterranean seepage, storing clean drinking water through severe summer droughts",
            "They were outdoor stadiums for elephant racing",
            "They were giant ovens used to bake bricks with volcanic lava"
        ],
        "answer": 1,
        "explanation": "Stepwells were ingenious multi-storied civil engineering structures designed to collect rainwater, recharge subterranean aquifers, and provide community water access via stairs.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Arid Zone Engineering:</strong> Western India faces semi-arid climates with brief, intense monsoon rains followed by long dry periods.</p>
            <p>2. <strong>Stepwell Design:</strong> Descending tiers of stone steps allowed access to water at varying seasonal depths, while shade reduced surface evaporative loss.</p>
            <p>3. <strong>Conclusion:</strong> Stored runoff and groundwater for dry seasons (Option B).</p>
        """
    },
    {
        "id": 17,
        "question": "How does modern rooftop rainwater harvesting contribute to sustainable municipal water security?",
        "options": [
            "It diverts rooftop precipitation through filters into storage tanks or recharge borewells to replenish aquifers",
            "It evaporates all rainwater before it can touch the ground",
            "It converts rainwater into chemical petrol for motorcycles",
            "It washes roof dust directly into domestic drinking glasses without filtration"
        ],
        "answer": 0,
        "explanation": "Rooftop harvesting catches clean rainwater, routes it through silt/sand filters, and stores it for household use or injects it into deep aquifers to reverse water table depletion.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Process Flow:</strong> Catchment (clean roof) ➔ Conveyance (gutters & downpipes) ➔ First-flush diverter & mesh filter ➔ Storage sump or recharge percolation well.</p>
            <p>2. <strong>Ecological Benefit:</strong> Reduces stormwater urban flooding, curbs municipal water demand, and naturally recharges over-pumped aquifers.</p>
            <p>3. <strong>Conclusion:</strong> Option A describes modern rooftop harvesting.</p>
        """
    },
    {
        "id": 18,
        "question": "Why is dumping untreated chemical effluents and plastic municipal garbage into rivers and lakes hazardous to ecosystems?",
        "options": [
            "It turns freshwater sweet and attracts too many migrating birds",
            "It depletes dissolved oxygen, introduces toxic heavy metals, destroys aquatic life, and poisons drinking water sources",
            "It causes river water to freeze into ice during peak summer",
            "It prevents boats from sailing due to excessive magnetic attraction"
        ],
        "answer": 1,
        "explanation": "Water pollution introduces pathogens, non-biodegradable microplastics, and toxic chemical compounds, causing eutrophication, fish mortality, and human waterborne diseases.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Biochemical Oxygen Demand (BOD):</strong> Decomposing organic sewage consumes dissolved oxygen, suffocating fish and aquatic fauna.</p>
            <p>2. <strong>Bioaccumulation:</strong> Industrial toxins (lead, mercury, cadmium) enter the food chain, causing organ failure in animals and humans.</p>
            <p>3. <strong>Conclusion:</strong> Option B provides the accurate ecological hazard.</p>
        """
    },
    {
        "id": 19,
        "question": "How does solar thermal radiation drive the continuous operation of Earth's global water cycle?",
        "options": [
            "Solar radiation provides the latent heat needed to evaporate surface water into water vapour, which rises, cools, condenses into clouds, and precipitates as rain",
            "Sunlight pushes ocean water into underground caves using magnetic beams",
            "The Sun freezes ocean water into clouds at noon every day",
            "Solar rays condense clouds directly into solid plastic flakes"
        ],
        "answer": 0,
        "explanation": "Solar energy provides the thermal energy required for phase transition from liquid water to vapour (evaporation), powering atmospheric convection, condensation, and precipitation.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Thermodynamic Driver:</strong> Solar insolation heats oceans, lakes, and soil, driving evaporation and plant transpiration.</p>
            <p>2. <strong>Atmospheric Circulation:</strong> Warm, moist air ascends; adiabatic cooling causes condensation onto airborne nuclei, forming clouds that precipitate as freshwater rain.</p>
            <p>3. <strong>Conclusion:</strong> Option A defines solar thermodynamic hydrologic drive.</p>
        """
    },
    {
        "id": 20,
        "question": "What would happen to planet Earth if the Sun suddenly stopped emitting light and thermal radiant heat?",
        "options": [
            "Plants would grow ten times faster using starlight",
            "Global temperatures would plummet below freezing, oceans would freeze solid, photosynthesis would halt, and life would perish",
            "Earth would turn into a giant ball of pure liquid gold",
            "Wind speeds would increase to 1,000 km/h due to absolute darkness"
        ],
        "answer": 1,
        "explanation": "Without solar heat, Earth would lose thermal equilibrium, freezing oceans solid within weeks. Without sunlight, photosynthesis would cease, collapsing the planetary food web.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Thermal Catastrophe:</strong> Without solar radiation (~1,361 W/m² top of atmosphere), surface temperatures would drop to -73°C within weeks and eventually to -240°C.</p>
            <p>2. <strong>Trophic Collapse:</strong> Primary producers (plants, phytoplankton) would die immediately, halting all oxygen synthesis and food generation for consumers.</p>
            <p>3. <strong>Conclusion:</strong> Total biological extinction and planetary freeze (Option B).</p>
        """
    },

    # Challenge 3: Questions 21 to 30 (Slide 19)
    {
        "id": 21,
        "question": "What is the physical mechanism by which a solar photovoltaic (PV) panel generates usable electric current?",
        "options": [
            "Solar light photons strike semiconductor silicon cells, dislodging electrons and creating a flow of direct electric current (DC)",
            "Water flowing inside the glass tubes spins miniature water wheels",
            "Sunlight burns charcoal inside the solar panel to boil water",
            "Magnets inside the panel attract atmospheric lightning"
        ],
        "answer": 0,
        "explanation": "Photovoltaic cells use p-n junction silicon semiconductors. Photons with sufficient energy knock valence electrons into the conduction band, generating an electric current.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Photoelectric Effect:</strong> Light packets (photons) transfer energy to semiconductor valence electrons.</p>
            <p>2. <strong>Built-in Electric Field:</strong> The internal electric field across the p-n junction forces free electrons toward the n-type layer, creating an external DC current circuit.</p>
            <p>3. <strong>Conclusion:</strong> Option A describes the photovoltaic conversion process.</p>
        """
    },
    {
        "id": 22,
        "question": "Why is a solar box cooker equipped with an insulated black-painted interior and a clear double-glass lid?",
        "options": [
            "The black paint absorbs maximum solar radiation, while the glass lid traps heat via the greenhouse effect, raising temperatures to 100°C–140°C",
            "To prevent the cook from smelling the aroma of spices",
            "To allow radio waves to enter and cook the food like a microwave",
            "To keep the food frozen cold during summer afternoons"
        ],
        "answer": 0,
        "explanation": "Black surfaces absorb broad-spectrum solar radiation. Glass transmits incoming shortwave solar light but reflects longwave infrared thermal radiation, trapping heat inside.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Thermal Absorption:</strong> Matte black surfaces have an emissivity/absorptivity close to 0.95, absorbing visible and infrared light.</p>
            <p>2. <strong>Greenhouse Trapping:</strong> Glass is transparent to incoming visible light (0.4–0.7 µm) but opaque to re-radiated thermal infrared (>3 µm), preventing convective and radiative heat loss.</p>
            <p>3. <strong>Conclusion:</strong> Option A details the solar thermal cooking mechanism.</p>
        """
    },
    {
        "id": 23,
        "question": "How do natural forest ecosystems regulate regional climate and enhance atmospheric humidity?",
        "options": [
            "Trees absorb all clouds and store them in underground tree roots",
            "Vast tree canopies transpire gigatons of water vapour into the atmosphere through leaf stomata, seeding clouds and inducing regional rainfall",
            "Trees blow atmospheric air away into outer space",
            "Tree leaves produce synthetic air conditioning chemicals"
        ],
        "answer": 1,
        "explanation": "Through transpiration, extensive forest canopies release immense volumes of water vapour, increasing atmospheric relative humidity and creating biogenic cloud condensation nuclei.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Evapotranspiration Engine:</strong> A single mature tree can transpire hundreds of liters of water daily through its stomata.</p>
            <p>2. <strong>Precipitation Recycling:</strong> Transpired moisture ascends, condenses into local cumulus clouds, and returns as precipitation, sustaining regional agricultural zones.</p>
            <p>3. <strong>Conclusion:</strong> Option B describes forest-climate biotic feedback.</p>
        """
    },
    {
        "id": 24,
        "question": "What is the biological significance of fallen leaf litter decomposing into 'humus' on the forest floor?",
        "options": [
            "It turns the forest floor into a solid concrete highway",
            "Microbes, fungi, and earthworms break down organic matter into nutrient-rich humus, recycling minerals back to plant roots naturally",
            "It poisons tree roots so only one giant tree can survive",
            "It transforms falling leaves into non-renewable plastic bags"
        ],
        "answer": 1,
        "explanation": "Humus is formed through decomposition of organic debris by detritivores and saprophytic microbes, returning essential nitrogen, phosphorus, and potassium to the soil.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Nutrient Cycling:</strong> Forests do not require artificial chemical fertilizers because fallen leaves, twigs, and organic waste are recycled in situ.</p>
            <p>2. <strong>Soil Health:</strong> Humus improves soil crumb structure, increases microbial biodiversity, and enhances water-holding capacity.</p>
            <p>3. <strong>Conclusion:</strong> Option B summarizes natural nutrient recycling.</p>
        """
    },
    {
        "id": 25,
        "question": "What courageous non-violent action characterized the historic 1970s Chipko Movement in the Chamoli district of Uttarakhand?",
        "options": [
            "Villagers built stone fortresses around all forest animals",
            "Local village women embraced and clung to tree trunks, physically interposing their bodies to prevent commercial loggers from felling them",
            "Villagers boycotted all vegetables and ate only river sand",
            "Villagers migrated permanently to coastal fishing ports"
        ],
        "answer": 1,
        "explanation": "Led by grassroots leaders like Gaura Devi, village women encircled and hugged tree trunks ('Chipko'), daring commercial contractors to cut them down before harming the trees.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Historical Context:</strong> In 1973–74, commercial lumber companies sought to log forest trees in the Alaknanda river basin, threatening village livelihoods and mountain slope stability.</p>
            <p>2. <strong>Non-violent Clinging:</strong> Women organized community vigils, literally clinging to trees. The sheer moral power of this non-violent resistance prompted the state to declare a 15-year ban on green felling.</p>
            <p>3. <strong>Conclusion:</strong> Hugging tree trunks to stop logging (Option B).</p>
        """
    },
    {
        "id": 26,
        "question": "Why is the annual tree plantation festival 'Van Mahotsav' celebrated across India during the first week of July?",
        "options": [
            "Because July marks the coldest winter snowfall in central India",
            "Because the onset of southwest monsoon rains provides abundant natural moisture for newly planted saplings to establish deep root systems",
            "Because tree leaves only grow during the month of July",
            "Because school students are not allowed outdoors during any other month"
        ],
        "answer": 1,
        "explanation": "Instituted in 1950 by K.M. Munshi, Van Mahotsav is synchronized with the southwest monsoon so regular rainfall irrigates young saplings naturally without artificial watering.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Monsoon Alignment:</strong> Planting in early July coincides with heavy monsoon downpours across most Indian states.</p>
            <p>2. <strong>Sapling Survival:</strong> Continuous ambient moisture allows roots to penetrate surrounding soil, maximizing survival before the arrival of dry post-monsoon weather.</p>
            <p>3. <strong>Conclusion:</strong> Option B provides the agricultural-ecological rationale.</p>
        """
    },
    {
        "id": 27,
        "question": "What is 'soil weathering', and approximately how long does nature take to produce just one single centimeter of fertile topsoil?",
        "options": [
            "An instant chemical explosion that produces soil in two seconds",
            "The slow physical, chemical, and biological disintegration of bedrock over hundreds to thousands of years",
            "The manufacturing of clay bricks in industrial kilns over three days",
            "The freezing of rainwater into solid white marble"
        ],
        "answer": 1,
        "explanation": "Soil genesis (pedogenesis) involves the mechanical breakdown and chemical alteration of parent bedrock by wind, water, temperature swings, and organisms, taking centuries per centimeter.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Pedogenesis Rates:</strong> Disintegrating hard granite or basalt into mineral silt and enriching it with 5% organic humus requires 200 to 1,000 years per centimeter of topsoil.</p>
            <p>2. <strong>Non-Renewability on Human Scales:</strong> Because topsoil formation requires geological spans, agricultural topsoil loss via erosion is practically irreversible.</p>
            <p>3. <strong>Conclusion:</strong> Weathering takes hundreds to thousands of years (Option B).</p>
        """
    },
    {
        "id": 28,
        "question": "What are the four primary components that constitute balanced, healthy agricultural soil?",
        "options": [
            "Pure petrol, motor oil, plastic beads, and table salt",
            "Mineral particles (sand, silt, clay), organic humus, soil water, and soil air",
            "Crushed glass, concrete rubble, iron filings, and chemical acids",
            "Solid diamonds, gold nuggets, copper wires, and boiling water"
        ],
        "answer": 1,
        "explanation": "Healthy soil typically comprises approximately 45% mineral particles, 5% organic matter (humus), 25% soil water (with dissolved ions), and 25% soil air (with oxygen).",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Four-Phase Matrix:</strong> Soil is a complex multi-phase system: solid mineral matrix (~45%), solid organic fraction (~5%), liquid pore water (~25%), and gaseous pore air (~25%).</p>
            <p>2. <strong>Functional Balance:</strong> Air provides O₂ for root respiration; water carries dissolved mineral nutrients; minerals and humus provide cation exchange capacity.</p>
            <p>3. <strong>Conclusion:</strong> Option B accurately specifies the four primary components.</p>
        """
    },
    {
        "id": 29,
        "question": "Why are earthworms scientifically recognized as 'ecosystem engineers' and 'the farmer's best friend'?",
        "options": [
            "They poison all insects and birds within five kilometers",
            "Their subterranean burrows loosen and aerate the soil, facilitating root respiration and water infiltration, while their casts provide nutrient-rich vermicompost",
            "They cement soil particles into hard, impermeable rock",
            "They replace the need for sunlight in crop photosynthesis"
        ],
        "answer": 1,
        "explanation": "Earthworms ingest mineral soil and organic matter, creating porous subterranean macropores that improve aeration and drainage, while their casts are rich in plant-available nutrients.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Bioturbation:</strong> Earthworm tunneling mixes organic matter into subsoil layers and breaks up compacted soil pans.</p>
            <p>2. <strong>Vermicompost:</strong> Earthworm casts contain 5× more available nitrogen, 7× more available phosphorus, and 11× more available potassium than surrounding soil.</p>
            <p>3. <strong>Conclusion:</strong> Soil aeration and vermicompost enrichment (Option B).</p>
        """
    },
    {
        "id": 30,
        "question": "Which of the following describes the difference between a 'rock' and a 'mineral' in geological science?",
        "options": [
            "A rock is an aggregate composed of one or more minerals, whereas a mineral is a naturally occurring inorganic solid with a definite chemical composition and crystalline structure",
            "A rock is made of wood, while a mineral is made of ocean water",
            "Rocks are living organisms, while minerals are manufactured in factories",
            "There is no geological difference between rocks and minerals"
        ],
        "answer": 0,
        "explanation": "Minerals are pure, naturally occurring inorganic solids with specific chemical formulas and crystal lattices (e.g., quartz, calcite). Rocks (e.g., granite, limestone) are aggregates of minerals.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Mineral Definition:</strong> Homogeneous natural solid with an orderly internal atomic arrangement and fixed chemical composition (e.g., SiO₂ for quartz).</p>
            <p>2. <strong>Rock Definition:</strong> Heterogeneous composite of mineral grains (e.g., granite is composed of quartz, feldspar, and mica minerals).</p>
            <p>3. <strong>Conclusion:</strong> Option A provides the rigorous geological distinction.</p>
        """
    },

    # Challenge 4: Questions 31 to 40 (Slide 20)
    {
        "id": 31,
        "question": "Which metamorphic rock splits cleanly along natural parallel cleavage planes into thin, waterproof slabs traditionally used for building roofs?",
        "options": [
            "Pumice",
            "Slate",
            "Rock salt",
            "Chalk"
        ],
        "answer": 1,
        "explanation": "Slate is a fine-grained, foliated metamorphic rock derived from shale or mudstone. Its slaty cleavage allows it to be split into flat, durable, impermeable roofing tiles.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Metamorphic Foliation:</strong> Regional metamorphism aligns microscopic platy mica minerals perpendicularly to the direction of compressive stress.</p>
            <p>2. <strong>Architectural Utility:</strong> This produces clean structural cleavage, yielding thin, weather-resistant, non-porous sheets ideal for roofing shingles.</p>
            <p>3. <strong>Conclusion:</strong> Slate (Option B).</p>
        """
    },
    {
        "id": 32,
        "question": "From which natural mineral ore is iron metal commercially smelted in industrial blast furnaces to manufacture steel for construction rebars and bridges?",
        "options": [
            "Bauxite",
            "Haematite and Magnetite",
            "Cinnabar",
            "Rock phosphate"
        ],
        "answer": 1,
        "explanation": "Iron is commercially extracted primarily from oxide mineral ores, predominantly haematite (Fe₂O₃) and magnetite (Fe₃O₄), via carbothermic reduction in blast furnaces.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Iron Ores:</strong> Haematite (Fe₂O₃) contains ~70% iron by weight; magnetite (Fe₃O₄) contains ~72% iron and possesses natural magnetic properties.</p>
            <p>2. <strong>Smelting:</strong> Ores are reacted with carbon coke and limestone flux at temperatures exceeding 1,500°C to yield molten pig iron, refined into structural steel.</p>
            <p>3. <strong>Conclusion:</strong> Haematite and Magnetite (Option B).</p>
        """
    },
    {
        "id": 33,
        "question": "How were fossil fuels like coal, crude petroleum, and natural gas formed inside the Earth?",
        "options": [
            "From prehistoric volcanic lava cooling inside ocean trenches over three days",
            "From ancient swamp forests and microscopic marine plankton buried under sediment layers, subjected to high heat and pressure over hundreds of millions of years",
            "From synthetic chemicals injected into subterranean rock caverns by ancient humans",
            "From meteors crashing into Earth from outer space"
        ],
        "answer": 1,
        "explanation": "Fossil fuels are carbonized remnants of ancient biological organisms buried under anaerobic conditions and metamorphosed by geothermal heat and pressure over 300 million years.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Coal Genesis:</strong> Terrestrial plants in Carboniferous swamp forests died, formed peat, and were compressed under rock strata into lignite, bituminous coal, and anthracite.</p>
            <p>2. <strong>Petroleum & Gas Genesis:</strong> Marine microscopic phytoplankton and zooplankton settled in ocean mud; thermal cracking over millions of years formed hydrocarbons.</p>
            <p>3. <strong>Conclusion:</strong> Option B provides the accurate paleobiological description.</p>
        """
    },
    {
        "id": 34,
        "question": "What refined liquid fuels are extracted from crude petroleum (crude oil) through industrial fractional distillation?",
        "options": [
            "Petrol, diesel, kerosene, and aviation turbine fuel",
            "Fresh milk, fruit juice, and vegetable soup",
            "Pure liquid oxygen and liquid hydrogen",
            "Liquid salt and dissolved limestone"
        ],
        "answer": 0,
        "explanation": "Fractional distillation separates crude oil hydrocarbons based on boiling points into petroleum gas, petrol (gasoline), naphtha, kerosene, diesel, lubricating oils, and bitumen.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Fractionation Column:</strong> Heated crude oil enters a distillation tower with a vertical temperature gradient.</p>
            <p>2. <strong>Boiling Point Cuts:</strong> Low boiling fractions (petrol: 40°C–200°C) condense near the top; mid fractions (kerosene: 175°C–275°C, diesel: 250°C–350°C) condense lower down.</p>
            <p>3. <strong>Conclusion:</strong> Petrol, diesel, kerosene, and jet fuel (Option A).</p>
        """
    },
    {
        "id": 35,
        "question": "Why is burning fossil fuels (coal, diesel, petrol) a major environmental and public health concern?",
        "options": [
            "Because burning fossil fuels produces too much clean cold drinking water",
            "Because combustion releases carbon dioxide (greenhouse gas driving global warming), carbon monoxide, sulfur dioxide, and toxic particulate soot (PM2.5) that pollutes air",
            "Because fossil fuel flames make city streets too bright at night",
            "Because burning coal turns nearby trees into solid stone"
        ],
        "answer": 1,
        "explanation": "Fossil fuel combustion releases greenhouse gases (CO₂) causing climate destabilization, along with toxic pollutants (CO, SO₂, NOx, PM2.5) triggering severe respiratory illnesses.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Climate Destabilization:</strong> Billions of tons of fossil carbon sequestered over millions of years are released into the atmosphere, intensifying the greenhouse effect.</p>
            <p>2. <strong>Air Quality Crisis:</strong> Incomplete combustion generates dangerous fine particulate matter (PM2.5) that penetrates deep into human lung alveoli and bloodstreams.</p>
            <p>3. <strong>Conclusion:</strong> Option B details the environmental and health impacts.</p>
        """
    },
    {
        "id": 36,
        "question": "What defines a 'renewable resource' in environmental science?",
        "options": [
            "A resource that can never be touched or seen by human eyes",
            "A resource that is naturally replenished, regenerated, or restored by environmental processes within a reasonable human timeframe",
            "A resource that turns into toxic poison after two days",
            "A resource that can only be manufactured inside a nuclear reactor"
        ],
        "answer": 1,
        "explanation": "Renewable resources regenerate through natural biogeochemical cycles or ongoing solar/geophysical fluxes at a rate equal to or faster than their consumption rate.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Replenishment Horizon:</strong> Resources like timber, freshwater, and wind regenerate over timescales ranging from seconds (wind/solar) to years (trees/water cycle).</p>
            <p>2. <strong>Sustainability Condition:</strong> A renewable resource remains sustainable as long as harvest rates do not exceed biological regeneration capacity.</p>
            <p>3. <strong>Conclusion:</strong> Naturally replenished within human timeframes (Option B).</p>
        """
    },
    {
        "id": 37,
        "question": "Which of the following resources is non-renewable and will eventually be exhausted if consumption continues unabated?",
        "options": [
            "Wind energy blowing through mountain passes",
            "Solar radiation radiating from the Sun",
            "Coal and petroleum deposits buried in Earth's crust",
            "Ocean waves propelled by tides"
        ],
        "answer": 2,
        "explanation": "Coal and petroleum reserves exist in fixed geological deposits. Because they require hundreds of millions of years to form, extraction causes irreversible net depletion.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Finite Stocks:</strong> Global proven petroleum and coal reserves represent finite geological inventory.</p>
            <p>2. <strong>Depletion Inevitability:</strong> At current global consumption rates of ~100 million barrels of oil per day, accessible reserves face depletion within decades to centuries.</p>
            <p>3. <strong>Conclusion:</strong> Coal and petroleum are strictly non-renewable (Option C).</p>
        """
    },
    {
        "id": 38,
        "question": "Which of the following is classified as a 'human-made resource' created by processing natural raw materials?",
        "options": [
            "A pristine virgin mountain pine forest",
            "A clear natural freshwater spring",
            "Electronic microchips manufactured from refined silicon, copper, and gold",
            "A rich alluvial soil deposit"
        ],
        "answer": 2,
        "explanation": "Human-made resources are artificial products, structures, or technologies created by applying human labor, engineering, and chemical processing to raw natural materials.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Raw Material to Tech:</strong> Quartz sand is refined into semiconductor-grade monocrystalline silicon, lithographically etched, and connected with copper/gold circuitry.</p>
            <p>2. <strong>Human-Made Status:</strong> Although its constituent chemical elements are natural, the microchip is an artificial invention of human engineering.</p>
            <p>3. <strong>Conclusion:</strong> Electronic microchips (Option C).</p>
        """
    },
    {
        "id": 39,
        "question": "In Activity 11.6, when students trace a simple paper school notebook back to its natural origins, what primary natural resources are involved?",
        "options": [
            "Crude oil pumped from desert oil wells exclusively",
            "Forest wood pulp harvested from trees, processed using freshwater, and bleached with mineral compounds",
            "Synthetic rubber melted from old car tyres",
            "Ocean salt crystallized in solar pans"
        ],
        "answer": 1,
        "explanation": "Paper is produced from cellulose wood fibers obtained from forest trees, utilizing clean water for pulping and mineral fillers (like clay, calcium carbonate) for smoothness.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Cellulose Source:</strong> Wood chips from softwoods and hardwoods are digested mechanically and chemically into pulp.</p>
            <p>2. <strong>Resource Interconnection:</strong> Pulping requires substantial volumes of water, while energy from power plants (coal/renewables) dries the slurry into paper sheets.</p>
            <p>3. <strong>Conclusion:</strong> Forest trees, freshwater, and mineral processing (Option B).</p>
        """
    },
    {
        "id": 40,
        "question": "What is the profound ethical message of Mahatma Gandhi's quote: 'Earth provides enough to satisfy every man's need, but not every man's greed'?",
        "options": [
            "Planet Earth has limitless resources that should be consumed as rapidly as possible",
            "Human society must practice sustainable, responsible consumption because planetary resources can meet genuine needs but cannot withstand wasteful over-exploitation",
            "All technology should be destroyed and humans should live in caves",
            "Only wild animals have the right to consume Earth's natural treasures"
        ],
        "answer": 1,
        "explanation": "Gandhi emphasized environmental stewardship, intergenerational equity, and voluntary restraint, warning that greedy over-consumption exhausts nature's finite treasures.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Ethical Stewardship:</strong> Earth's biocapacity is sufficient to nourish humanity if resources are equitably shared and sustainably stewarded.</p>
            <p>2. <strong>The Peril of Greed:</strong> Extravagant over-consumption, planned obsolescence, and destructive resource extraction exceed ecological planetary boundaries.</p>
            <p>3. <strong>Conclusion:</strong> Sustainable, responsible consumption meeting genuine needs (Option B).</p>
        """
    }
]

