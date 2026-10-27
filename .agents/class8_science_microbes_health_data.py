r"""
Class 8 Science Chapter 1: Microbes and Health
Complete data specification with 20 slides, 32 in-slide checkpoints, and 40 mastery questions with step-by-step solutions.
r"""

SLIDES_DATA = [
    {
        "id": 1,
        "title": "The Unseen World",
        "subtitle": "Discovering Tiny Organisms in Water Drop",
        "badge": "Microbiology Foundations",
        "narration": "Welcome to Chapter 1: Microbes and Health. For thousands of years, humans had no idea that our bodies, our water, and our soil were teeming with trillions of living organisms too small to be seen with the naked eye. In 1674, Antonie van Leeuwenhoek looked through a simple handcrafted microscope at a drop of pond water and discovered tiny, active creatures he named animalcules. Today, we call them microorganisms or microbes.",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                A <strong>microorganism</strong> (or <strong>microbe</strong>) is an organism so minute that it cannot be seen without the aid of a microscope. They range in size from a few tenths of a micrometer ($0.1\,\mu\text{m}$) up to several hundred micrometers ($100\,\mu\text{m}$). One micrometer ($\mu\text{m}$) is one-millionth of a meter ($10^{-6}\text{ m}$).
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900/60 border border-cyan-500/30">
                    <h4 class="text-xs font-bold text-cyan-400 uppercase tracking-wider mb-1">Pioneering Discovery</h4>
                    <p class="text-xs text-slate-300">
                        In 1674, Dutch scientist <strong>Antonie van Leeuwenhoek</strong> used ground glass lenses with up to $300\times$ magnification to observe living microorganisms in pond water and tooth scrapings for the first time in human history.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900/60 border border-emerald-500/30">
                    <h4 class="text-xs font-bold text-emerald-400 uppercase tracking-wider mb-1">Microbial Ubiquity</h4>
                    <p class="text-xs text-slate-300">
                        Microbes thrive everywhere on Earth: boiling thermal vents, frozen polar glaciers, hyper-saline waters, deep soil, air currents, and inside the digestive tracts of humans and animals.
                    </p>
                </div>
            </div>
            <p class="text-xs text-slate-400 leading-relaxed">
                Observing a single drop of stagnant pond water under a compound light microscope reveals a bustling ecosystem of swimming protozoa, green algae ribbons, and motile bacteria.
            </p>
        r""",
        "key_points": [
            r"Microorganisms are microscopic living entities invisible to the naked human eye ($< 100\,\mu\text{m}$).",
            "Antonie van Leeuwenhoek (1674) was the first human to observe living microbes ('animalcules').",
            "Microbes exist in virtually every biosphere on Earth, including extreme thermal and saline habitats.",
            "Standard compound optical microscopes use objective and eyepiece lenses to achieve $100\times$ to $1000\times$ magnification."
        ],
        "sim_id": "microscope_water_drop_sim",
        "checkpoints": [
            {
                "question": "What is the typical size range of most microscopic single-celled bacteria?",
                "options": [
                    "0.5 to 5 micrometers (μm)",
                    "10 to 50 centimeters (cm)",
                    "1 to 2 millimeters (mm)",
                    "0.01 to 0.1 nanometers (nm)"
                ],
                "correct": 0,
                "explanation": "Bacteria typically measure between 0.5 and 5 micrometers (μm), requiring a high-power compound light microscope (400× to 1000×) for clear observation."
            },
            {
                "question": "Who was the first scientist to observe living microorganisms in a drop of water?",
                "options": [
                    "Antonie van Leeuwenhoek",
                    "Robert Hooke",
                    "Louis Pasteur",
                    "Edward Jenner"
                ],
                "correct": 0,
                "explanation": "Antonie van Leeuwenhoek observed living single-celled organisms ('animalcules') in pond water in 1674. Robert Hooke observed dead cork cell walls in 1665."
            }
        ]
    },
    {
        "id": 2,
        "title": "Microbial Diversity",
        "subtitle": "The 5 Major Taxonomic Groups of Microorganisms",
        "badge": "Biological Classification",
        "narration": "Microorganisms are not all alike. Scientists categorize them into five major groups based on their cellular architecture, genetic material, and nutrition: Bacteria, Fungi, Protozoa, Algae, and Viruses. While bacteria are simple single-celled prokaryotes, fungi and protozoa are complex eukaryotes, and viruses stand on the mysterious boundary between the living and the non-living.",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                Microbes display extraordinary structural diversity. Understanding whether a microbe is cellular or acellular, prokaryotic or eukaryotic, dictates how it reproduces and how our immune system fights it.
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-2 my-2 text-xs">
                <div class="p-2.5 rounded-lg bg-amber-950/20 border border-amber-500/30">
                    <span class="font-bold text-amber-400">1. Bacteria (Prokaryotes)</span>
                    <p class="text-slate-300 mt-1">Single-celled, lack membrane-bound nucleus. Shapes include rod-like (Bacillus), spherical (Coccus), and spiral (Spirillum). Cell wall contains peptidoglycan.</p>
                </div>
                <div class="p-2.5 rounded-lg bg-rose-950/20 border border-rose-500/30">
                    <span class="font-bold text-rose-400">2. Fungi (Heterotrophic)</span>
                    <p class="text-slate-300 mt-1">Non-green eukaryotes with chitin cell walls. Can be unicellular (Yeast) or multicellular filamentous molds (Penicillium, Bread mould Rhizopus, Mushrooms).</p>
                </div>
                <div class="p-2.5 rounded-lg bg-cyan-950/20 border border-cyan-500/30">
                    <span class="font-bold text-cyan-400">3. Protozoa (Animal-like)</span>
                    <p class="text-slate-300 mt-1">Unicellular heterotrophic eukaryotes lacking cell walls. Move using pseudopodia (Amoeba), cilia (Paramecium), or flagella (Trypanosoma, Euglena).</p>
                </div>
                <div class="p-2.5 rounded-lg bg-emerald-950/20 border border-emerald-500/30">
                    <span class="font-bold text-emerald-400">4. Algae (Plant-like)</span>
                    <p class="text-slate-300 mt-1">Autotrophic eukaryotes with chlorophyll and cellulose cell walls. Unicellular (Chlamydomonas) or multicellular filamentous (Spirogyra).</p>
                </div>
                <div class="p-2.5 rounded-lg bg-purple-950/20 border border-purple-500/30 col-span-1 sm:col-span-2 lg:col-span-1">
                    <span class="font-bold text-purple-400">5. Viruses (Acellular)</span>
                    <p class="text-slate-300 mt-1">Ultramicroscopic (20–300 nm). Contain only nucleic acid (DNA or RNA) inside a protein capsid. Completely inert outside host cells; reproduce only inside hosts.</p>
                </div>
            </div>
        r""",
        "key_points": [
            "The 5 major microbial groups are Bacteria, Fungi, Protozoa, Algae, and Viruses.",
            "Bacteria lack a membrane-bound nucleus (prokaryotic) and possess peptidoglycan cell walls.",
            "Viruses are acellular and metabolically inert outside a host cell, occupying the border of life.",
            "Fungi are heterotrophic decomposers with chitin walls; Algae are photosynthetic autotrophs."
        ],
        "sim_id": "microbe_classification_morphology_sim",
        "checkpoints": [
            {
                "question": "Which microorganism group possesses chlorophyll and carries out oxygenic photosynthesis like plants?",
                "options": [
                    "Algae (e.g., Spirogyra, Chlamydomonas)",
                    "Fungi (e.g., Yeast, Bread Mould)",
                    "Protozoa (e.g., Amoeba, Paramecium)",
                    "Viruses (e.g., Bacteriophage, Influenza)"
                ],
                "correct": 0,
                "explanation": "Algae contain chlorophyll and carry out photosynthesis, producing their own food using sunlight, water, and carbon dioxide."
            },
            {
                "question": "Why are viruses considered borderline entities between living and non-living things?",
                "options": [
                    "They show no metabolic activity or reproduction until they invade a host cell",
                    "They can turn into mineral crystals that eat bacteria",
                    "They are multicellular organisms that hibernate in dry conditions",
                    "They possess chloroplasts but lack mitochondria"
                ],
                "correct": 0,
                "explanation": "Outside a living host cell, viruses behave like non-living crystalline particles with no metabolism. Inside a host, they hijack the host's machinery to replicate."
            }
        ]
    },
    {
        "id": 3,
        "title": "Pond Water Safari",
        "subtitle": "Observing Protozoa and Micro-Algae in Action",
        "badge": "Microscopic Ecology",
        "narration": "Let us take a droplet of water collected from a freshwater pond and place it under our microscope slide with a coverslip. Immediately, a bustling miniature universe comes alive. You can see Amoeba stretching out its flowing pseudopodia to engulf food particles, Paramecium darting smoothly with thousands of coordinated cilia, and ribbon-like Spirogyra basking in light.",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                Freshwater ecosystems contain rich microbial communities that sustain the aquatic food chain. Microscopic observations reveal how these single cells perform every essential life process: movement, feeding, respiration, and reproduction.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 my-2 text-xs">
                <div class="p-3 rounded-xl bg-slate-900/60 border border-cyan-500/30">
                    <h4 class="font-bold text-cyan-300 text-sm mb-1">Amoeba proteus</h4>
                    <p class="text-slate-300 leading-relaxed">
                        An irregular, constantly shape-shifting protozoan. It moves by pushing out cytoplasmic extensions called <strong>pseudopodia</strong> ('false feet'). When encountering food, pseudopodia surround the prey in a process called <strong>phagocytosis</strong>, forming an internal food vacuole for digestion.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900/60 border border-indigo-500/30">
                    <h4 class="font-bold text-indigo-300 text-sm mb-1">Paramecium caudatum</h4>
                    <p class="text-slate-300 leading-relaxed">
                        A slipper-shaped ciliate protozoan. Thousands of hair-like <strong>cilia</strong> beat rhythmically to propel it through water and sweep bacteria into its oral groove. It has contractile vacuoles that actively pump out excess water to prevent bursting (osmoregulation).
                    </p>
                </div>
            </div>
            <p class="text-xs text-slate-400 mt-2">
                Filamentous green algae like <em>Spirogyra</em> contain characteristic ribbon-like spiral chloroplasts that float in masses called pond silk, releasing oxygen bubbles into the pond.
            </p>
        r""",
        "key_points": [
            "Amoeba moves and engulfs food particles through flowing cytoplasmic extensions called pseudopodia.",
            "Paramecium is slipper-shaped and navigates using thousands of synchronized hair-like cilia.",
            "Contractile vacuoles maintain osmotic balance by pumping out excess water absorbed from hypotonic pond water.",
            "Photosynthetic micro-algae form the primary producer base of aquatic freshwater food chains."
        ],
        "sim_id": "pond_water_micro_ecosystem_sim",
        "checkpoints": [
            {
                "question": "What specialized cellular organelle prevents freshwater protozoa like Paramecium from bursting due to continuous water influx?",
                "options": [
                    "Contractile vacuole",
                    "Food vacuole",
                    "Chloroplast",
                    "Oral groove"
                ],
                "correct": 0,
                "explanation": "Because pond water is hypotonic to protozoan cytoplasm, water constantly enters by osmosis. The contractile vacuole collects and pumps out this excess water."
            },
            {
                "question": "How does Amoeba capture its prey such as bacteria and tiny algae?",
                "options": [
                    "By extending pseudopodia to surround prey in phagocytosis",
                    "By stinging prey with nematocysts",
                    "By filtering water through gills",
                    "By releasing digestive acid into the open water"
                ],
                "correct": 0,
                "explanation": "Amoeba extends two pseudopodia around the food particle until their tips fuse, enclosing the prey inside a membrane-bound food vacuole (phagocytosis)."
            }
        ]
    },
    {
        "id": 4,
        "title": "Helpful Microbes: Food",
        "subtitle": "Fermentation in Curd, Bread, and Traditional Foods",
        "badge": "Biotechnology at Home",
        "narration": "Not all microbes cause harm; in fact, human civilization has relied on beneficial microbes for thousands of years to create delicious, nutritious food. The turning of milk into curd, the rising of fluffy bread dough, and the brewing of beverages all depend on a remarkable biological process called fermentation.",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                <strong>Fermentation</strong> is the metabolic process in which microorganisms convert carbohydrates (such as sugars and starches) into acids, gases, or alcohols in the absence or limitation of oxygen.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 my-2 text-xs">
                <div class="p-3 rounded-xl bg-slate-900/60 border border-amber-500/30">
                    <h4 class="font-bold text-amber-300 text-sm mb-1">Curd Formation (Lactobacillus)</h4>
                    <p class="text-slate-300 leading-relaxed">
                        When a spoon of starter curd is added to warm milk ($35^\circ\text{C}-40^\circ\text{C}$), billions of <em>Lactobacillus</em> bacteria multiply. They convert milk sugar (<strong>lactose</strong>) into <strong>lactic acid</strong> ($\text{C}_3\text{H}_6\text{O}_3$). Lactic acid lowers the milk pH, causing milk protein (<strong>casein</strong>) to coagulate into thick, tangy curd.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900/60 border border-cyan-500/30">
                    <h4 class="font-bold text-cyan-300 text-sm mb-1">Bread Making (Yeast Fermentation)</h4>
                    <p class="text-slate-300 leading-relaxed">
                        Baker's yeast (<em>Saccharomyces cerevisiae</em>) ferments glucose sugars in flour dough, producing ethanol and carbon dioxide gas ($\text{CO}_2$):
                        <br><span class="font-mono text-cyan-300 font-bold block my-1">$\text{Glucose} \xrightarrow{\text{Yeast}} 2\,\text{Ethanol} + 2\,\text{CO}_2 \uparrow + \text{Energy}$</span>
                        Bubbles of $\text{CO}_2$ get trapped inside the elastic gluten mesh, making dough swell and bake into soft, porous bread.
                    </p>
                </div>
            </div>
            <p class="text-xs text-slate-400 mt-2">
                Traditional fermented delicacies like idli, dosa batter, dhokla, and paneer also harness lactic acid bacteria and wild yeasts to enhance bioavailability of B-vitamins and ease digestion.
            </p>
        r""",
        "key_points": [
            "Lactobacillus bacteria ferment milk lactose into lactic acid, coagulating casein proteins into curd.",
            "Yeast (Saccharomyces cerevisiae) ferments sugars into ethanol and carbon dioxide gas (CO₂).",
            "Trapped CO₂ bubbles create the spongy, airy texture of baked bread and steamed idlis.",
            "Louis Pasteur discovered the microbial basis of fermentation in 1857."
        ],
        "sim_id": "fermentation_lactic_alcohol_sim",
        "checkpoints": [
            {
                "question": "Which chemical compound produced by yeast causes bread dough to rise and become spongy?",
                "options": [
                    "Carbon dioxide gas (CO₂)",
                    "Lactic acid",
                    "Oxygen gas (O₂)",
                    "Nitrogen dioxide (NO₂)"
                ],
                "correct": 0,
                "explanation": "Yeast cells respire anaerobically, releasing carbon dioxide gas (CO₂). As the gas expands, it forms thousands of tiny bubbles trapped in the dough, making it rise."
            },
            {
                "question": "What is the primary bacterium responsible for converting lukewarm milk into curd?",
                "options": [
                    "Lactobacillus",
                    "Escherichia coli",
                    "Rhizobium",
                    "Mycobacterium"
                ],
                "correct": 0,
                "explanation": "Lactobacillus bacteria ferment lactose into lactic acid, lowering the pH and coagulating milk casein protein into creamy curd."
            }
        ]
    },
    {
        "id": 5,
        "title": "Soil Superheroes",
        "subtitle": "Biological Nitrogen Fixation and Agriculture",
        "badge": "Agricultural Microbiology",
        "narration": "Even though our atmosphere consists of nearly 78 percent nitrogen gas, plants cannot absorb it directly from the air to make essential proteins and nucleic acids. Enter the soil superheroes: nitrogen-fixing bacteria like Rhizobium and cyanobacteria that bridge the gap between air and life.",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                <strong>Biological Nitrogen Fixation (BNF)</strong> is the conversion of inert atmospheric nitrogen gas ($\text{N}_2$) into plant-usable mineral forms like ammonia ($\text{NH}_3$) and nitrates ($\text{NO}_3^-$) by specialized microorganisms.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 my-2 text-xs">
                <div class="p-3 rounded-xl bg-slate-900/60 border border-emerald-500/30">
                    <h4 class="font-bold text-emerald-300 text-sm mb-1">Symbiotic Rhizobium in Legumes</h4>
                    <p class="text-slate-300 leading-relaxed">
                        <em>Rhizobium</em> bacteria establish a mutualistic relationship in the root nodules of leguminous plants (beans, peas, lentils, gram). The plant provides the bacteria with carbohydrate food and shelter, while the bacteria provide the plant with fixed nitrogen compounds.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900/60 border border-teal-500/30">
                    <h4 class="font-bold text-teal-300 text-sm mb-1">Free-Living Cyanobacteria</h4>
                    <p class="text-slate-300 leading-relaxed">
                        Blue-green algae (Cyanobacteria) such as <em>Anabaena</em> and <em>Nostoc</em>, as well as free-living soil bacteria like <em>Azotobacter</em>, fix atmospheric nitrogen directly in water-logged paddy fields, significantly enriching natural soil fertility without chemical fertilizers.
                    </p>
                </div>
            </div>
            <p class="text-xs text-slate-400 mt-2">
                Farmers practice <strong>crop rotation</strong> by planting legumes between cereal crops to naturally replenish soil nitrate reserves and maintain sustainable crop yields.
            </p>
        r""",
        "key_points": [
            "Atmospheric nitrogen (N₂) cannot be absorbed directly by plant leaves or roots.",
            "Rhizobium bacteria live symbiotically in root nodules of leguminous plants, fixing nitrogen into nitrates.",
            "Cyanobacteria (blue-green algae) such as Nostoc and Anabaena serve as potent bio-fertilizers in rice paddies.",
            "Crop rotation with legumes naturally restores soil fertility and reduces reliance on chemical fertilizers."
        ],
        "sim_id": "nitrogen_fixation_nodule_sim",
        "checkpoints": [
            {
                "question": "Where are Rhizobium bacteria located in leguminous plants such as peas and beans?",
                "options": [
                    "Inside specialized root nodules",
                    "On the upper surface of leaves",
                    "Inside the flower petals",
                    "Inside seed coats only"
                ],
                "correct": 0,
                "explanation": "Rhizobium infects legume roots to form swollen structures called root nodules, where they live symbiotically and fix atmospheric nitrogen."
            },
            {
                "question": "Which of the following is a nitrogen-fixing cyanobacterium (blue-green algae) widely used in paddy fields?",
                "options": [
                    "Anabaena",
                    "Spirogyra",
                    "Yeast",
                    "Amoeba"
                ],
                "correct": 0,
                "explanation": "Anabaena and Nostoc are photosynthetic cyanobacteria with specialized heterocyst cells capable of fixing atmospheric nitrogen in wetland rice fields."
            }
        ]
    },
    {
        "id": 6,
        "title": "Earth's Recyclers",
        "subtitle": "Decomposition, Biocomposting, and Sewage Treatment",
        "badge": "Environmental Cleansing",
        "narration": "What would happen if autumn leaves, fallen branches, and dead animals never disappeared? The Earth would soon be buried under miles of organic debris. Fortunately, saprophytic bacteria and fungi act as nature's ultimate cleaning crew, decomposing organic waste back into elemental nutrients.",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                <strong>Decomposers</strong> (or <strong>saprophytes</strong>) secrete digestive enzymes externally onto dead plant and animal remains, breaking down complex polymers (cellulose, proteins, fats) into simple inorganic minerals, carbon dioxide, and water.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 my-2 text-xs">
                <div class="p-3 rounded-xl bg-slate-900/60 border border-lime-500/30">
                    <h4 class="font-bold text-lime-300 text-sm mb-1">Composting & Humus Formation</h4>
                    <p class="text-slate-300 leading-relaxed">
                        When kitchen vegetable peels, dry leaves, and cattle dung are placed in a pit, aerobic and anaerobic microorganisms degrade the waste. Within a few weeks, the organic matter transforms into dark, nutrient-rich <strong>manure</strong> (humus), recycling nitrogen, phosphorus, and potassium back into the topsoil.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900/60 border border-emerald-500/30">
                    <h4 class="font-bold text-emerald-300 text-sm mb-1">Sewage & Bioremediation</h4>
                    <p class="text-slate-300 leading-relaxed">
                        In municipal wastewater treatment plants, aerobic microbes in aeration tanks digest dissolved human excreta and organic contaminants. Certain specialized bacteria can even metabolize toxic crude oil slicks and chemical industrial pollutants in a process called <strong>bioremediation</strong>.
                    </p>
                </div>
            </div>
            <p class="text-xs text-slate-400 mt-2">
                While organic matter is <strong>biodegradable</strong>, synthetic materials like polyethylene plastics resist microbial enzymatic action, persisting in landfills for centuries.
            </p>
        r""",
        "key_points": [
            "Decomposers secrete extracellular enzymes that break dead organic matter into elemental nutrients.",
            "Biocomposting converts plant and animal waste into dark, fertile organic manure (humus).",
            "Microorganisms in sewage treatment plants purify contaminated wastewater by consuming organic matter.",
            "Bioremediation uses specialized bacteria to clean up environmental pollutants such as crude oil spills."
        ],
        "sim_id": "biodegradation_compost_sim",
        "checkpoints": [
            {
                "question": "What is the primary ecological role of saprophytic bacteria and fungi in nature?",
                "options": [
                    "Breaking down dead organic matter and recycling nutrients",
                    "Producing oxygen through deep underground photosynthesis",
                    "Hunting living animals for food",
                    "Preventing clouds from raining"
                ],
                "correct": 0,
                "explanation": "Saprophytes break down dead plant and animal bodies, converting complex organic compounds into simple soil nutrients for plants, preventing debris accumulation."
            },
            {
                "question": "Why do plastic bags not decompose in a compost pit alongside fruit and vegetable peels?",
                "options": [
                    "Plastics are synthetic polymers that microbial enzymes cannot break down",
                    "Plastics contain toxic acid that kills all bacteria instantly",
                    "Plastics are eaten exclusively by earthworms",
                    "Plastics dissolve into water too quickly"
                ],
                "correct": 0,
                "explanation": "Plastics are non-biodegradable synthetic polymers with chemical bonds that microbial enzymes have not evolved to digest."
            }
        ]
    },
    {
        "id": 7,
        "title": "Microbial Foes",
        "subtitle": "Pathogens, Infection Modes, and Disease Vectors",
        "badge": "Infectious Pathology",
        "narration": "While most microbes are harmless or beneficial, a tiny minority cause serious illnesses in humans, animals, and plants. These disease-causing microorganisms are called pathogens. Understanding how pathogens travel from an infected person to a healthy host is the key to preventing outbreaks.",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                Diseases caused by pathogens that can spread from an infected person to a healthy individual through air, water, food, vectors, or physical contact are called <strong>communicable diseases</strong>.
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 my-2 text-xs">
                <div class="p-2.5 rounded-lg bg-slate-900/60 border border-rose-500/30">
                    <span class="font-bold text-rose-400">1. Airborne Droplets (Aerosols)</span>
                    <p class="text-slate-300 mt-1">Sneezing or coughing expels thousands of microscopic droplets loaded with pathogens into the surrounding air (e.g., Common cold, Influenza, Tuberculosis, COVID-19).</p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900/60 border border-cyan-500/30">
                    <span class="font-bold text-cyan-400">2. Water & Food Contamination</span>
                    <p class="text-slate-300 mt-1">Drinking water or eating food contaminated with fecal pathogens or spoiled by bacterial toxins causes waterborne diseases (e.g., Cholera, Typhoid, Hepatitis A).</p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900/60 border border-amber-500/30">
                    <span class="font-bold text-amber-400">3. Biological Vectors (Insects)</span>
                    <p class="text-slate-300 mt-1">Insects that carry pathogens from an infected host to a healthy person without suffering from the disease themselves (e.g., female <em>Anopheles</em> mosquito transmitting Malaria, <em>Aedes</em> mosquito transmitting Dengue).</p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900/60 border border-purple-500/30">
                    <span class="font-bold text-purple-400">4. Direct Contact & Fomites</span>
                    <p class="text-slate-300 mt-1">Skin-to-skin touch, sharing towels, clothes, or touching contaminated door handles and utensils (e.g., Ringworm, Chickenpox, Conjunctivitis).</p>
                </div>
            </div>
        r""",
        "key_points": [
            "Disease-causing microorganisms are called pathogens.",
            "Communicable diseases spread from infected persons to healthy hosts via air, water, food, vectors, or contact.",
            "Airborne droplet transmission occurs when a sneeze or cough releases pathogen-laden aerosols.",
            "Vectors are carrier organisms (like mosquitoes and houseflies) that transport pathogens between hosts."
        ],
        "sim_id": "pathogen_transmission_routes_sim",
        "checkpoints": [
            {
                "question": "What is an insect or animal called when it carries a pathogen from a sick person to a healthy person?",
                "options": [
                    "A vector (or carrier)",
                    "A parasite host",
                    "A saprophyte",
                    "A producer"
                ],
                "correct": 0,
                "explanation": "A vector is an organism (such as the female Anopheles mosquito or housefly) that transports infectious pathogens between hosts without being killed by the pathogen."
            },
            {
                "question": "Which of the following is an example of an airborne communicable disease spread by droplet infection?",
                "options": [
                    "Tuberculosis",
                    "Malaria",
                    "Cholera",
                    "Tetanus"
                ],
                "correct": 0,
                "explanation": "Tuberculosis (caused by Mycobacterium tuberculosis) is spread through tiny aerosol droplets expelled when an infected person coughs or sneezes."
            }
        ]
    },
    {
        "id": 8,
        "title": "Bacteria vs Viruses",
        "subtitle": "Infection Mechanics and Major Human Illnesses",
        "badge": "Pathogen Profiles",
        "narration": "To choose the right medicine, doctors must know whether an infection is bacterial or viral. Bacteria are complete living cells that multiply independently and can release toxic proteins, while viruses are stealthy invaders that hijack host cell machinery, turning cells into virus factories until they burst.",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                Bacteria and viruses operate by completely different biological mechanisms. Knowing their differences is vital because treatments that destroy bacteria have zero effect on viruses.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 my-2 text-xs">
                <div class="p-3 rounded-xl bg-slate-900/60 border border-amber-500/30">
                    <h4 class="font-bold text-amber-300 text-sm mb-1">Bacterial Infections</h4>
                    <p class="text-slate-300 leading-relaxed">
                        Bacteria divide rapidly by binary fission. Some damage tissues directly, while others secrete harmful chemical poisons called <strong>toxins</strong>:
                    </p>
                    <ul class="list-disc list-inside text-slate-400 mt-1 space-y-1">
                        <li><strong>Tuberculosis (TB):</strong> <em>Mycobacterium tuberculosis</em> destroys lung tissue.</li>
                        <li><strong>Cholera:</strong> <em>Vibrio cholerae</em> causes severe, dehydrating watery diarrhea.</li>
                        <li><strong>Typhoid:</strong> <em>Salmonella typhi</em> invades intestinal walls causing high fever.</li>
                    </ul>
                </div>
                <div class="p-3 rounded-xl bg-slate-900/60 border border-purple-500/30">
                    <h4 class="font-bold text-purple-300 text-sm mb-1">Viral Infections</h4>
                    <p class="text-slate-300 leading-relaxed">
                        A virus attaches to specific receptor proteins on host cell membranes, injects its genetic code, and commands the host ribosomes to assemble thousands of new viruses, eventually bursting (lysing) the host cell:
                    </p>
                    <ul class="list-disc list-inside text-slate-400 mt-1 space-y-1">
                        <li><strong>Polio:</strong> Poliovirus attacks motor nerves in the spinal cord, leading to paralysis.</li>
                        <li><strong>Influenza / Cold:</strong> Respiratory viruses damage throat and airway lining.</li>
                        <li><strong>Dengue & Chickenpox:</strong> Cause high fever, joint pain, rashes, and platelet drop.</li>
                    </ul>
                </div>
            </div>
        r""",
        "key_points": [
            "Bacteria reproduce independently by binary fission and can produce harmful chemical toxins.",
            "Viruses are intracellular obligate parasites that replicate by hijacking host cellular machinery.",
            "Major bacterial diseases: Tuberculosis, Cholera, Typhoid, Tetanus.",
            "Major viral diseases: Polio, Influenza, Common Cold, Measles, Dengue, Rabies."
        ],
        "sim_id": "bacterial_vs_viral_infection_sim",
        "checkpoints": [
            {
                "question": "Which of the following diseases is caused by a virus rather than a bacterium?",
                "options": [
                    "Poliomyelitis (Polio)",
                    "Tuberculosis",
                    "Typhoid fever",
                    "Cholera"
                ],
                "correct": 0,
                "explanation": "Polio is caused by the Poliovirus. Tuberculosis, Typhoid, and Cholera are caused by bacterial pathogens."
            },
            {
                "question": "How do viruses replicate inside a human body?",
                "options": [
                    "By entering host cells and hijacking their genetic and protein-making machinery",
                    "By dividing into two cells through binary fission in the bloodstream",
                    "By absorbing nutrients from food in the stomach lumen",
                    "By forming seeds inside plant roots"
                ],
                "correct": 0,
                "explanation": "Viruses cannot reproduce on their own; they must invade a living host cell and commandeer its cellular machinery to synthesize viral genomes and proteins."
            }
        ]
    },
    {
        "id": 9,
        "title": "Parasites & Fungi",
        "subtitle": "Malaria Life Cycle, Dysentery, and Fungal Skin Infections",
        "badge": "Parasitology & Mycology",
        "narration": "Beyond bacteria and viruses, two other microbial groups cause widespread human suffering: protozoa and fungi. Malaria, one of the deadliest parasitic diseases in human history, is caused by the protozoan Plasmodium and requires two different hosts—the mosquito and the human—to complete its complex life cycle.",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                Protozoan parasites are unicellular animal-like organisms that live inside host tissues, while pathogenic fungi grow as branching filaments on warm, moist skin and mucosal surfaces.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 my-2 text-xs">
                <div class="p-3 rounded-xl bg-slate-900/60 border border-rose-500/30">
                    <h4 class="font-bold text-rose-300 text-sm mb-1">The Malaria Cycle (Plasmodium)</h4>
                    <p class="text-slate-300 leading-relaxed">
                        1. Female <em>Anopheles</em> mosquito bites a human, injecting <strong>sporozoites</strong> with saliva.<br>
                        2. Sporozoites travel to the <strong>liver</strong>, multiply, and become merozoites.<br>
                        3. Merozoites invade <strong>Red Blood Cells (RBCs)</strong>, replicate, and burst them open every 48–72 hours, releasing a toxic pigment called <strong>hemozoin</strong> that triggers chills and recurring high fever.<br>
                        4. Another mosquito ingests sexual gametocytes from the blood, continuing the cycle.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900/60 border border-amber-500/30">
                    <h4 class="font-bold text-amber-300 text-sm mb-1">Amoebic Dysentery & Fungi</h4>
                    <p class="text-slate-300 leading-relaxed">
                        <strong>Amoebic Dysentery:</strong> Caused by <em>Entamoeba histolytica</em> through contaminated drinking water, causing intestinal ulcers and severe abdominal pain.<br><br>
                        <strong>Fungal Infections (Ringworm):</strong> Caused by dermatophyte fungi (<em>Microsporum</em>, <em>Trichophyton</em>). They feed on keratin protein in skin, nails, and scalp, forming circular red, itchy lesions exacerbated by warmth and sweat.
                    </p>
                </div>
            </div>
        r""",
        "key_points": [
            "Malaria is caused by the protozoan Plasmodium and transmitted exclusively by female Anopheles mosquitoes.",
            "Rupture of red blood cells releases hemozoin toxin, causing the recurring high fever and chills of malaria.",
            "Amoebic dysentery is caused by the protozoan Entamoeba histolytica ingested via contaminated food/water.",
            "Ringworm is a contagious fungal skin infection caused by dermatophytes feeding on skin keratin."
        ],
        "sim_id": "malaria_vector_life_cycle_sim",
        "checkpoints": [
            {
                "question": "What is the toxic substance released when Plasmodium ruptures human red blood cells, causing chills and recurring fever?",
                "options": [
                    "Hemozoin",
                    "Hemoglobin",
                    "Penicillin",
                    "Histamine"
                ],
                "correct": 0,
                "explanation": "When malaria parasites burst open human RBCs, they release hemozoin, a toxic byproduct of hemoglobin digestion, which triggers chills and spikes in body temperature."
            },
            {
                "question": "Why is only the female Anopheles mosquito—not the male—responsible for spreading malaria?",
                "options": [
                    "Females require human blood protein to develop their eggs, while males feed only on plant nectar",
                    "Males carry antibodies that kill Plasmodium instantly",
                    "Males do not have wings to fly",
                    "Females are attracted to water while males live underground"
                ],
                "correct": 0,
                "explanation": "Male mosquitoes feed solely on flower nectar. Only female mosquitoes bite humans because they need iron and proteins in blood to nourish developing eggs."
            }
        ]
    },
    {
        "id": 10,
        "title": "Food Shield",
        "subtitle": "Microbial Food Spoilage and Preservation Techniques",
        "badge": "Food Science",
        "narration": "Microbes love our food just as much as we do. If left unprotected, bacteria and molds quickly colonize milk, fruits, and cooked dishes, producing foul odors, changing flavors, and generating dangerous toxins that cause food poisoning. Humans have invented ingenious preservation methods that halt microbial growth.",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                Microbes require moisture, warmth, oxygen, and neutral pH to thrive. <strong>Food preservation</strong> methods alter these physical and chemical conditions so microorganisms cannot survive or reproduce.
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-2 my-2 text-xs">
                <div class="p-2.5 rounded-lg bg-slate-900/60 border border-cyan-500/30">
                    <span class="font-bold text-cyan-400">1. Pasteurization</span>
                    <p class="text-slate-300 mt-1">Invented by Louis Pasteur. Milk is heated to about $70^\circ\text{C}$ for 15 to 30 seconds and then suddenly chilled to $<10^\circ\text{C}$. This thermal shock destroys pathogenic bacteria without altering taste.</p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900/60 border border-amber-500/30">
                    <span class="font-bold text-amber-400">2. Salt & Sugar Curing</span>
                    <p class="text-slate-300 mt-1">High concentrations of salt (pickles, fish) or sugar (jams, jellies) draw water out of bacterial cells by <strong>osmosis</strong> (plasmolysis), causing cells to shrink, dehydrate, and cease metabolic activity.</p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900/60 border border-emerald-500/30">
                    <span class="font-bold text-emerald-400">3. Oil & Vinegar</span>
                    <p class="text-slate-300 mt-1">Oil creates an anaerobic barrier preventing air contact, while acetic acid in vinegar creates an acidic pH ($< 4.0$) in which spoilage bacteria cannot survive.</p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900/60 border border-purple-500/30">
                    <span class="font-bold text-purple-400">4. Sun-Drying / Dehydration</span>
                    <p class="text-slate-300 mt-1">Removing water content from grains, legumes, and dry fruits stops enzyme activity and microbial spore germination entirely.</p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900/60 border border-rose-500/30 col-span-1 sm:col-span-2 lg:col-span-1">
                    <span class="font-bold text-rose-400">5. Chemical Preservatives</span>
                    <p class="text-slate-300 mt-1">Approved chemical additives like <strong>Sodium Benzoate</strong> and <strong>Sodium Metabisulfite</strong> inhibit yeast and fungal spoilage in fruit squashes and sauces.</p>
                </div>
            </div>
        r""",
        "key_points": [
            "Microbial food spoilage produces bad odor, discoloration, and toxins that cause food poisoning.",
            "Pasteurization heats milk to 70°C for 15–30 seconds followed by rapid chilling to kill pathogens.",
            "High salt and sugar concentrations draw water out of microbial cells via osmotic plasmolysis.",
            "Chemical preservatives like Sodium Benzoate and Sodium Metabisulfite protect fruit squashes and syrups."
        ],
        "sim_id": "food_preservation_pasteurizer_sim",
        "checkpoints": [
            {
                "question": "How does heavy salting preserve raw mangoes, lemons, and fish in pickles?",
                "options": [
                    "By drawing water out of bacterial cells via osmosis, causing plasmolysis",
                    "By freezing the bacterial cells into solid ice",
                    "By adding oxygen gas that suffocates bacteria",
                    "By turning all proteins into sugar"
                ],
                "correct": 0,
                "explanation": "High salt concentration creates a hypertonic external environment. Water exits bacterial cells by exosmosis (plasmolysis), dehydrating and inactivating the bacteria."
            },
            {
                "question": "What is the key temperature and timing sequence in the pasteurization of milk?",
                "options": [
                    "Heated to about 70°C for 15–30 seconds, then rapidly chilled",
                    "Boiled at 200°C for 2 hours, then kept warm",
                    "Frozen at -50°C for 3 days, then thawed",
                    "Heated to 37°C for 5 minutes, then filtered"
                ],
                "correct": 0,
                "explanation": "Pasteurization heats milk to approximately 70°C for 15 to 30 seconds to kill pathogenic microbes, followed by immediate chilling to prevent surviving spores from germinating."
            }
        ]
    },
    {
        "id": 11,
        "title": "Innate Immunity",
        "subtitle": "The Body's First and Second Lines of Defense",
        "badge": "Immunology Basics",
        "narration": "Every single minute, thousands of microbes land on our skin, enter our nostrils, or reach our stomach. Why aren't we sick every second of the day? Because our body is protected by a magnificent multi-layered security fortress known as the immune system.",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                The body's defense is divided into <strong>innate (non-specific) immunity</strong>, which acts immediately against any foreign invader, and <strong>adaptive (specific) immunity</strong>, which creates targeted weapons.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 my-2 text-xs">
                <div class="p-3 rounded-xl bg-slate-900/60 border border-blue-500/30">
                    <h4 class="font-bold text-blue-300 text-sm mb-1">First Line of Defense: Physical & Chemical Barriers</h4>
                    <ul class="space-y-1.5 text-slate-300">
                        <li><strong>Unbroken Skin:</strong> A tough, keratinized waterproof shield that blocks microbial entry.</li>
                        <li><strong>Mucus Membranes & Cilia:</strong> Respiratory airways produce sticky mucus that traps dust and microbes, swept upward by microscopic cilia.</li>
                        <li><strong>Stomach Acid ($\text{HCl}$):</strong> Strongly acidic gastric juice ($\text{pH } 1.5 - 2.0$) kills most ingested bacteria.</li>
                        <li><strong>Lysozyme Enzymes:</strong> Present in tears and saliva, lysozyme digests bacterial cell walls.</li>
                    </ul>
                </div>
                <div class="p-3 rounded-xl bg-slate-900/60 border border-emerald-500/30">
                    <h4 class="font-bold text-emerald-300 text-sm mb-1">Second Line of Defense: Cellular & Inflammatory</h4>
                    <ul class="space-y-1.5 text-slate-300">
                        <li><strong>White Blood Cells (Phagocytes):</strong> Macrophages and neutrophils act as cellular soldiers. They patrol tissues and engulf invading pathogens via <strong>phagocytosis</strong>.</li>
                        <li><strong>Inflammatory Response:</strong> When skin is cut, histamine is released, widening capillaries (vasodilation). Blood flows to the site, bringing heat, redness, swelling, and battalions of white blood cells.</li>
                        <li><strong>Fever:</strong> Chemical signals (pyrogens) raise body temperature, which slows bacterial replication and boosts immune cell activity.</li>
                    </ul>
                </div>
            </div>
        r""",
        "key_points": [
            "Innate immunity provides immediate, non-specific protection against all invading foreign microbes.",
            "The first line of defense consists of physical barriers (skin, mucus) and chemical secretions (stomach HCl, tear lysozyme).",
            "The second line features phagocytic white blood cells (macrophages) that engulf and digest microbes.",
            "Inflammation brings increased blood flow, swelling, and white blood cells directly to injured infection sites."
        ],
        "sim_id": "innate_immunity_phagocytosis_sim",
        "checkpoints": [
            {
                "question": "Which enzyme present in human tears and saliva breaks down the cell walls of invading bacteria?",
                "options": [
                    "Lysozyme",
                    "Pepsin",
                    "Amylase",
                    "Lipase"
                ],
                "correct": 0,
                "explanation": "Lysozyme is an antimicrobial enzyme found in tears, saliva, and mucus that catalyzes the hydrolysis of peptidoglycan in bacterial cell walls."
            },
            {
                "question": "What is the process called when a macrophage or white blood cell engulfs and destroys a bacterium?",
                "options": [
                    "Phagocytosis",
                    "Photosynthesis",
                    "Fermentation",
                    "Plasmolysis"
                ],
                "correct": 0,
                "explanation": "Phagocytosis (cellular eating) is the process by which phagocytic white blood cells wrap around and ingest pathogens, digesting them inside phagolysosomes."
            }
        ]
    },
    {
        "id": 12,
        "title": "Antibody Arsenal",
        "subtitle": "Adaptive Immunity, B-Cells, and Lock-and-Key Recognition",
        "badge": "Adaptive Immunology",
        "narration": "If a pathogen slips past our non-specific defenses, the body deploys its elite special forces: adaptive immunity. Here, specialized white blood cells called B-lymphocytes synthesize precision-guided biochemical missiles known as antibodies, designed to neutralize a specific pathogen with lock-and-key accuracy.",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                Adaptive immunity relies on recognizing unique molecular markers on pathogen surfaces, called <strong>antigens</strong>, and manufacturing matching <strong>antibodies</strong>.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 my-2 text-xs">
                <div class="p-3 rounded-xl bg-slate-900/60 border border-cyan-500/30">
                    <h4 class="font-bold text-cyan-300 text-sm mb-1">Antigens vs Antibodies</h4>
                    <p class="text-slate-300 leading-relaxed">
                        An <strong>antigen</strong> is any foreign molecule (such as a viral coat protein or bacterial capsule) that triggers an immune response.<br><br>
                        An <strong>antibody</strong> (immunoglobulin) is a Y-shaped protein manufactured by activated B-lymphocytes (plasma cells). The tips of the Y-fork possess hypervariable binding sites that fit only one specific antigen epitope, like a key into a lock.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900/60 border border-indigo-500/30">
                    <h4 class="font-bold text-indigo-300 text-sm mb-1">Modes of Antibody Action</h4>
                    <ul class="space-y-1.5 text-slate-300">
                        <li><strong>Neutralization:</strong> Antibodies bind to viral spikes or bacterial toxins, blocking them from entering host cells.</li>
                        <li><strong>Agglutination:</strong> Y-shaped antibodies clump hundreds of pathogens together into an immobilized cluster.</li>
                        <li><strong>Opsonization:</strong> Antibodies tag pathogens like glowing beacon flags, signaling phagocytes to devour them rapidly.</li>
                    </ul>
                </div>
            </div>
            <p class="text-xs text-slate-400 mt-2">
                Crucially, some activated B-cells transform into long-lived <strong>memory B-cells</strong> that survive in lymph nodes for decades, ready to launch an immediate, massive defense if that same pathogen ever returns.
            </p>
        r""",
        "key_points": [
            "Antigens are foreign molecular surface markers on pathogens that stimulate antibody production.",
            "Antibodies are Y-shaped proteins that bind specifically to matching antigen epitopes like a lock and key.",
            "Antibodies neutralize toxins, clump pathogens (agglutination), and mark them for destruction by phagocytes.",
            "Memory cells persist in the body for years, providing long-lasting immunological immunity."
        ],
        "sim_id": "antigen_antibody_lock_key_sim",
        "checkpoints": [
            {
                "question": "What is the relationship between an antigen and an antibody?",
                "options": [
                    "An antibody is a defensive Y-shaped protein that binds specifically to a matching foreign antigen",
                    "An antigen is a medicine that kills antibodies",
                    "Antibodies are produced by bacteria to destroy human antigens",
                    "Antigens and antibodies are identical chemicals in plant cells"
                ],
                "correct": 0,
                "explanation": "Antigens are foreign molecules on pathogens, while antibodies are specialized defensive proteins made by our B-cells that bind to matching antigens with lock-and-key specificity."
            },
            {
                "question": "What cellular role do long-lived 'memory B-cells' perform after an infection is cured?",
                "options": [
                    "They remember the pathogen and produce rapid, large amounts of antibodies upon re-infection",
                    "They digest human bone marrow to create calcium",
                    "They turn into red blood cells to transport oxygen",
                    "They exit the body through the kidneys"
                ],
                "correct": 0,
                "explanation": "Memory B-cells persist in the body for years, 'remembering' the specific antigen so that upon future exposure, they produce antibodies immediately before disease symptoms develop."
            }
        ]
    },
    {
        "id": 13,
        "title": "Vaccine Shield",
        "subtitle": "Edward Jenner, Immunization Principles, and Herd Immunity",
        "badge": "Preventive Medicine",
        "narration": "Vaccines represent one of humanity's greatest scientific triumphs, wiping out devastating plagues like smallpox and preventing millions of child deaths every year. A vaccine trains your immune system with target practice, teaching your body how to defeat a dangerous germ without ever getting sick.",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                A <strong>vaccine</strong> is a biological preparation containing weakened (attenuated), inactivated (killed), or harmless fragments of a pathogen that stimulates the body to produce antibodies and memory cells without causing the disease.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 my-2 text-xs">
                <div class="p-3 rounded-xl bg-slate-900/60 border border-emerald-500/30">
                    <h4 class="font-bold text-emerald-300 text-sm mb-1">Edward Jenner's Breakthrough (1796)</h4>
                    <p class="text-slate-300 leading-relaxed">
                        English doctor <strong>Edward Jenner</strong> noticed that milkmaids who contracted mild <em>cowpox</em> never suffered from deadly <em>smallpox</em>. In 1796, he inoculated young James Phipps with cowpox pustule fluid; when later exposed to smallpox, the boy was completely immune. This gave rise to the term <strong>vaccination</strong> (from Latin <em>vacca</em>, meaning cow).
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900/60 border border-teal-500/30">
                    <h4 class="font-bold text-teal-300 text-sm mb-1">The Power of Herd Immunity</h4>
                    <p class="text-slate-300 leading-relaxed">
                        When a high percentage of a population (usually $>85\%-95\%$) is vaccinated, the pathogen cannot find enough susceptible hosts to transmit between people. This <strong>herd immunity</strong> protects vulnerable individuals who cannot be vaccinated, such as newborns and cancer patients. Smallpox was eradicated globally in 1980 through universal vaccination.
                    </p>
                </div>
            </div>
            <p class="text-xs text-slate-400 mt-2">
                Routine childhood vaccines (Polio drops, BCG for tuberculosis, DPT for diphtheria-pertussis-tetanus, MMR for measles-mumps-rubella, and Hepatitis B) protect children worldwide.
            </p>
        r""",
        "key_points": [
            "Vaccines introduce weakened or killed pathogens to trigger antibody and memory cell production safely.",
            "Edward Jenner developed the world's first successful vaccine against smallpox in 1796 using cowpox virus.",
            "Primary immune response to a vaccine creates immunological memory for immediate future protection.",
            "Herd immunity occurs when a sufficiently high percentage of immunized people stops disease transmission in a community."
        ],
        "sim_id": "vaccine_immune_memory_sim",
        "checkpoints": [
            {
                "question": "Who discovered the first vaccine (against smallpox) in 1796?",
                "options": [
                    "Edward Jenner",
                    "Alexander Fleming",
                    "Antonie van Leeuwenhoek",
                    "Louis Pasteur"
                ],
                "correct": 0,
                "explanation": "Edward Jenner pioneered vaccination in 1796 by inoculating a boy with mild cowpox fluid, which provided immunity against deadly smallpox."
            },
            {
                "question": "What is the primary scientific principle behind vaccination?",
                "options": [
                    "Introducing weakened or dead antigens to train the body to build antibodies and memory cells",
                    "Injecting living toxic bacteria to test if a person is strong",
                    "Filtering out all red blood cells from circulation",
                    "Replacing bone marrow with synthetic plastic"
                ],
                "correct": 0,
                "explanation": "Vaccines introduce harmless versions of antigens so the immune system produces antibodies and long-lasting memory cells without causing illness."
            }
        ]
    },
    {
        "id": 14,
        "title": "Antibiotic Magic",
        "subtitle": "Alexander Fleming, Penicillin, and the Resistance Threat",
        "badge": "Pharmacology & Therapeutics",
        "narration": "Before the 20th century, a tiny scratch from a rose thorn or an infected cut could lead to fatal blood poisoning. In 1928, Scottish scientist Alexander Fleming made an accidental discovery in his cluttered laboratory that changed medicine forever: he found a green mold that produced a substance capable of dissolving bacteria. This was penicillin, the world's first true antibiotic.",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                An <strong>antibiotic</strong> is a biochemical substance produced by microorganisms (mostly fungi and soil bacteria) that kills or inhibits the growth of susceptible bacteria.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 my-2 text-xs">
                <div class="p-3 rounded-xl bg-slate-900/60 border border-cyan-500/30">
                    <h4 class="font-bold text-cyan-300 text-sm mb-1">Fleming's Discovery of Penicillin (1928)</h4>
                    <p class="text-slate-300 leading-relaxed">
                        While studying <em>Staphylococcus</em> bacteria, Alexander Fleming noticed that a stray mold contaminant, <em>Penicillium notatum</em>, had landed on a Petri dish. Around the mold colony, a clear halo appeared where bacterial colonies had lysed and dissolved. Penicillin works by blocking the enzyme that synthesizes bacterial peptidoglycan cell walls.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900/60 border border-rose-500/30">
                    <h4 class="font-bold text-rose-300 text-sm mb-1">The Growing Danger: Antibiotic Resistance</h4>
                    <p class="text-slate-300 leading-relaxed">
                        Crucially, <strong>antibiotics have zero effect on viral diseases</strong> (such as common cold, flu, or dengue) because viruses do not have bacterial cell walls or metabolic machinery.<br><br>
                        Overusing or stopping antibiotic courses prematurely allows surviving bacteria to evolve resistance mechanisms (such as producing beta-lactamase enzymes), creating dangerous 'superbugs'.
                    </p>
                </div>
            </div>
            <p class="text-xs text-slate-400 mt-2">
                Common modern antibiotics include Streptomycin, Tetracycline, Erythromycin, and Amoxicillin, which must always be taken only under prescription for the full prescribed duration.
            </p>
        r""",
        "key_points": [
            "Alexander Fleming discovered the first antibiotic, Penicillin, from Penicillium notatum mold in 1928.",
            "Antibiotics specifically kill or inhibit bacteria by disrupting bacterial cell walls or ribosome synthesis.",
            "Antibiotics are completely ineffective against viruses (like the common cold, influenza, and chickenpox).",
            "Misusing or under-dosing antibiotics leads to antibiotic resistance and dangerous multi-drug-resistant superbugs."
        ],
        "sim_id": "antibiotic_kirby_bauer_sim",
        "checkpoints": [
            {
                "question": "Why do doctors advise against taking antibiotics for common cold or influenza?",
                "options": [
                    "Colds and flu are caused by viruses, and antibiotics kill only bacteria",
                    "Antibiotics make the cold virus multiply ten times faster",
                    "Antibiotics dissolve the human stomach lining if taken with cold water",
                    "Antibiotics work only during summer season"
                ],
                "correct": 0,
                "explanation": "Antibiotics target bacterial structures like cell walls and bacterial ribosomes. Viruses lack these structures and are completely immune to antibiotic action."
            },
            {
                "question": "Which fungus produced the substance that Alexander Fleming discovered destroying bacterial cultures in 1928?",
                "options": [
                    "Penicillium notatum",
                    "Saccharomyces cerevisiae",
                    "Rhizopus stolonifer",
                    "Agaricus bisporus"
                ],
                "correct": 0,
                "explanation": "Alexander Fleming discovered penicillin in 1928 as a secretion produced by the green mold Penicillium notatum that dissolved surrounding Staphylococcus bacteria."
            }
        ]
    },
    {
        "id": 15,
        "title": "Lifestyle Defense",
        "subtitle": "Nutrition, Exercise, Hygiene, and Water Sanitation",
        "badge": "Health & Preventive Wellness",
        "narration": "Medicines and doctors are our emergency rescue team, but your everyday lifestyle is your permanent fortress against disease. What you eat, how much you move, and how you practice personal and public sanitation directly determine the strength of your immune system.",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                Immune competence depends on providing your white blood cells and tissues with raw biochemical building blocks and minimizing exposure to pathogen reservoirs.
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-2 my-2 text-xs">
                <div class="p-2.5 rounded-lg bg-slate-900/60 border border-amber-500/30">
                    <span class="font-bold text-amber-400">1. Balanced Immune Nutrition</span>
                    <p class="text-slate-300 mt-1">Proteins for antibody synthesis; Vitamin C (citrus fruits, amla) for phagocyte activity; Vitamin D & Zinc for immune regulation; Iron for oxygen transport in hemoglobin.</p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900/60 border border-cyan-500/30">
                    <span class="font-bold text-cyan-400">2. Physical Exercise & Rest</span>
                    <p class="text-slate-300 mt-1">Regular moderate exercise boosts lymphatic fluid circulation, helping immune cells patrol body tissues. Adequate sleep (8 hours) allows cytokine synthesis and cellular repair.</p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900/60 border border-emerald-500/30">
                    <span class="font-bold text-emerald-400">3. Hand Hygiene & Washing</span>
                    <p class="text-slate-300 mt-1">Washing hands with soap and water for 20 seconds physically dissolves the lipid envelope of viruses and washes away bacterial pathogens from skin.</p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900/60 border border-indigo-500/30">
                    <span class="font-bold text-indigo-400">4. Clean Water & Sanitation</span>
                    <p class="text-slate-300 mt-1">Boiling water ($100^\circ\text{C}$ for 1 minute), chlorination, or RO/UV filtration destroys waterborne pathogens (preventing cholera, typhoid, and amoebiasis).</p>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900/60 border border-purple-500/30 col-span-1 sm:col-span-2 lg:col-span-1">
                    <span class="font-bold text-purple-400">5. Vector Control</span>
                    <p class="text-slate-300 mt-1">Eliminating stagnant water puddles, coolers, and empty tires stops mosquito breeding, wiping out transmission vectors for malaria and dengue.</p>
                </div>
            </div>
        r""",
        "key_points": [
            "A balanced diet rich in proteins, Vitamin C, Vitamin D, and Zinc fuels antibody and immune cell production.",
            "Regular physical exercise accelerates lymphatic circulation, allowing immune cells to detect pathogens faster.",
            "Washing hands with soap for 20 seconds disrupts lipid viral membranes and removes bacterial biofilms.",
            "Boiling water and eliminating stagnant mosquito breeding sites protect communities from epidemic outbreaks."
        ],
        "sim_id": "lifestyle_immune_defense_sim",
        "checkpoints": [
            {
                "question": "How does soap effectively neutralize lipid-enveloped viruses (like Influenza or Coronaviruses)?",
                "options": [
                    "Soap molecules have hydrophobic tails that dissolve the viral fatty outer envelope, bursting the virus",
                    "Soap turns the virus into sugar crystals",
                    "Soap generates electrical voltage that shocks microbes",
                    "Soap cools the skin to below absolute zero"
                ],
                "correct": 0,
                "explanation": "Soap molecules are amphipathic. Their hydrophobic tails wedge into the viral lipid membrane, prying it apart and destroying the virus, which is then washed away with water."
            },
            {
                "question": "Why is boiling drinking water one of the most effective methods to prevent waterborne diseases like cholera?",
                "options": [
                    "Sustained boiling temperature denatures microbial proteins and ruptures pathogen cell membranes",
                    "Boiling adds vitamins to water",
                    "Boiling turns salt into pure sugar",
                    "Boiling removes all hydrogen from water"
                ],
                "correct": 0,
                "explanation": "Heating water to 100°C rapidly denatures essential proteins and enzymes inside bacteria, viruses, and protozoan cysts, killing pathogens and rendering water safe."
            }
        ]
    },
    {
        "id": 16,
        "title": "Microbes & Health Matrix",
        "subtitle": "Chapter Synthesis, Formulas, and Scientific Principles",
        "badge": "Chapter Synthesis",
        "narration": "We have explored the microbial world from single-celled protozoa in pond water to modern vaccines and antibiotics. Here is our master summary matrix bringing together the five microbial kingdoms, their beneficial roles, pathogenic diseases, body defenses, and disease prevention strategies.",
        "theory": r"""
            <p class="text-base text-slate-300 mb-3 leading-relaxed">
                Review this comprehensive synthesis table connecting microbial classification, beneficial applications, human diseases, and healthcare interventions.
            </p>
            <div class="overflow-x-auto my-2">
                <table class="w-full text-left text-xs border-collapse">
                    <thead>
                        <tr class="border-b border-slate-700 bg-slate-900/80 text-cyan-400 font-bold">
                            <th class="p-2">Group</th>
                            <th class="p-2">Key Cellular Traits</th>
                            <th class="p-2">Beneficial Uses</th>
                            <th class="p-2">Pathogenic Diseases</th>
                            <th class="p-2">Treatment / Defense</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800 text-slate-300">
                        <tr class="hover:bg-slate-900/40">
                            <td class="p-2 font-bold text-amber-400">Bacteria</td>
                            <td class="p-2">Prokaryotic, unicellular, peptidoglycan wall</td>
                            <td class="p-2">Curd (<em>Lactobacillus</em>), Nitrogen fixation (<em>Rhizobium</em>)</td>
                            <td class="p-2">Tuberculosis, Cholera, Typhoid</td>
                            <td class="p-2 text-cyan-300 font-mono">Antibiotics, Vaccines (BCG)</td>
                        </tr>
                        <tr class="hover:bg-slate-900/40">
                            <td class="p-2 font-bold text-rose-400">Fungi</td>
                            <td class="p-2">Eukaryotic, chitin cell wall, saprophytic</td>
                            <td class="p-2">Baking & brewing (Yeast), Penicillin mold</td>
                            <td class="p-2">Ringworm, Athlete's foot, Rust in wheat</td>
                            <td class="p-2 text-cyan-300 font-mono">Antifungal creams, Dryness</td>
                        </tr>
                        <tr class="hover:bg-slate-900/40">
                            <td class="p-2 font-bold text-cyan-400">Protozoa</td>
                            <td class="p-2">Eukaryotic, unicellular, animal-like, no wall</td>
                            <td class="p-2">Aquatic food web base, wastewater digestion</td>
                            <td class="p-2">Malaria (<em>Plasmodium</em>), Amoebic dysentery</td>
                            <td class="p-2 text-cyan-300 font-mono">Antimalarials, Vector control</td>
                        </tr>
                        <tr class="hover:bg-slate-900/40">
                            <td class="p-2 font-bold text-emerald-400">Algae</td>
                            <td class="p-2">Photosynthetic, cellulose wall, autotrophic</td>
                            <td class="p-2">Oxygen production, bio-fertilizer (Cyanobacteria)</td>
                            <td class="p-2">Harmful algal blooms (eutrophication)</td>
                            <td class="p-2 text-cyan-300 font-mono">Water aerating, Nutrient balance</td>
                        </tr>
                        <tr class="hover:bg-slate-900/40">
                            <td class="p-2 font-bold text-purple-400">Viruses</td>
                            <td class="p-2">Acellular, DNA/RNA in protein capsid</td>
                            <td class="p-2">Bacteriophage therapy, genetic vectors</td>
                            <td class="p-2">Polio, Influenza, Dengue, Chickenpox, COVID-19</td>
                            <td class="p-2 text-cyan-300 font-mono">Vaccines, Antivirals, Hygiene</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        r""",
        "key_points": [
            "Bacteria are prokaryotic targets of antibiotics, but also essential for curd and soil nitrogen fixation.",
            "Viruses reproduce only inside host cells and are prevented primarily through vaccination and sanitation.",
            "Innate physical barriers (skin, stomach acid) and adaptive antibodies protect the human body.",
            "Maintaining clean water, balanced nutrition, vector eradication, and hygiene shields humanity from pandemics."
        ],
        "sim_id": "microbes_health_matrix_sim",
        "checkpoints": [
            {
                "question": "Which combination correctly pairs a microbe, its beneficial role, and a disease it or its relatives can cause?",
                "options": [
                    "Bacteria • Curd & Nitrogen Fixation • Cholera & Tuberculosis",
                    "Viruses • Bread Fermentation • Malaria",
                    "Fungi • Rice Paddy Nitrogen Fixation • Polio",
                    "Protozoa • Antibiotic Synthesis • Common Cold"
                ],
                "correct": 0,
                "explanation": "Bacteria like Lactobacillus and Rhizobium provide curd and nitrogen fixation, while pathogenic bacteria like Vibrio cholerae and Mycobacterium tuberculosis cause cholera and TB."
            },
            {
                "question": "What is the most effective global strategy to permanently eliminate viral diseases like smallpox or polio?",
                "options": [
                    "Widespread universal immunization creating herd immunity",
                    "Spraying antibiotics into drinking water reservoirs",
                    "Boiling all soil in agricultural fields",
                    "Giving vitamins only after permanent paralysis occurs"
                ],
                "correct": 0,
                "explanation": "Universal childhood vaccination prevents transmission and builds herd immunity, which successfully eradicated smallpox and has brought polio near global extinction."
            }
        ]
    },
    {
        "id": 17,
        "title": "Mastery Challenge • Part I",
        "subtitle": "Questions 1–10: Discovery, Taxonomy, and Beneficial Microbes",
        "badge": "Exam Certification",
        "narration": "Test your mastery of foundational microbiology. Click Solution on any question to view step-by-step scientific explanations.",
        "theory": "<p class='text-sm text-slate-300'>Challenge questions covering microbial discovery, microscope optics, major taxonomic groups, pond water protozoa, and food fermentation.</p>",
        "key_points": [
            "Attempt all 10 questions independently.",
            "Review step-by-step scientific solutions.",
            "Identify key concepts: magnification, cell classification, fermentation biochemistry."
        ],
        "is_quiz_slide": True,
        "quiz_range": "1–10"
    },
    {
        "id": 18,
        "title": "Mastery Challenge • Part II",
        "subtitle": "Questions 11–20: Ecology, Pathogens, and Transmission Modes",
        "badge": "Exam Certification",
        "narration": "Mastery challenge part two covers biological nitrogen fixation, composting, infectious pathogens, and vector transmission dynamics.",
        "theory": "<p class='text-sm text-slate-300'>Challenge questions covering Rhizobium symbiosis, decomposers, airborne transmission, vectors, and bacterial vs viral pathology.</p>",
        "key_points": [
            "Evaluate soil fertility mechanisms and nitrogen cycle steps.",
            "Differentiate between communicable infection routes.",
            "Understand insect vector lifecycles (Anopheles, Aedes, houseflies)."
        ],
        "is_quiz_slide": True,
        "quiz_range": "11–20"
    },
    {
        "id": 19,
        "title": "Mastery Challenge • Part III",
        "subtitle": "Questions 21–30: Food Safety, Innate Immunity, and Antibodies",
        "badge": "Exam Certification",
        "narration": "Part three tests your understanding of food preservation methods, innate immune barriers, white blood cell phagocytosis, and antigen-antibody mechanics.",
        "theory": "<p class='text-sm text-slate-300'>Challenge questions covering pasteurization thermal curves, osmotic food preservation, physical barriers, phagocytes, and antibody neutralization.</p>",
        "key_points": [
            "Examine pasteurization conditions and osmotic cell plasmolysis.",
            "Analyze innate physical, chemical, and cellular defense lines.",
            "Master antigen-antibody binding specificity and immunological memory."
        ],
        "is_quiz_slide": True,
        "quiz_range": "21–30"
    },
    {
        "id": 20,
        "title": "Mastery Challenge • Part IV",
        "subtitle": "Questions 31–40: Vaccines, Antibiotics, and Preventive Wellness",
        "badge": "Exam Certification",
        "narration": "The final mastery challenge covers Jenner's smallpox vaccine, Fleming's penicillin, antibiotic resistance, herd immunity, and lifestyle hygiene.",
        "theory": "<p class='text-sm text-slate-300'>Challenge questions covering vaccination mechanisms, antibiotic target structures, resistance evolution, nutrition, and water sanitation.</p>",
        "key_points": [
            "Understand historical breakthroughs: Jenner (1796) and Fleming (1928).",
            "Explain why antibiotics do not cure viral infections.",
            "Formulate comprehensive public health and lifestyle prevention strategies."
        ],
        "is_quiz_slide": True,
        "quiz_range": "31–40"
    }
]

QUIZ_QUESTIONS = [
    # Questions 1–10 (Slide 17)
    {
        "id": 1,
        "question": "Which instrument is indispensable for observing single-celled bacteria and protozoa, and who first reported living microbes in water?",
        "options": [
            "Compound light microscope; Antonie van Leeuwenhoek (1674)",
            "Telescope; Galileo Galilei (1609)",
            "Barometer; Evangelista Torricelli (1643)",
            "Stethoscope; René Laennec (1816)"
        ],
        "correct": 0,
        "solution": "Step 1: Bacteria measure between $0.5\\,\\mu\\text{m}$ and $5\\,\\mu\\text{m}$, far below the resolving power of the human eye ($100\\,\\mu\\text{m}$).\nStep 2: A compound microscope with lenses magnifying $100\\times$ to $1000\\times$ is required.\nStep 3: In 1674, Antonie van Leeuwenhoek used his handcrafted lenses to observe living pond water 'animalcules' (microbes)."
    },
    {
        "id": 2,
        "question": "One micrometer (1 μm) is equal to which fraction of a meter?",
        "options": [
            "10⁻⁶ meter (one-millionth of a meter)",
            "10⁻³ meter (one-thousandth of a meter)",
            "10⁻⁹ meter (one-billionth of a meter)",
            "10⁻² meter (one-hundredth of a meter)"
        ],
        "correct": 0,
        "solution": r"Step 1: The metric prefix 'micro-' ($\mu$) denotes $10^{-6}$.\nStep 2: Therefore, $1\,\mu\text{m} = 10^{-6}\text{ m} = \frac{1}{1,000,000}\text{ meter}$.\nStep 3: For comparison, a millimeter is $10^{-3}\text{ m}$ and a nanometer is $10^{-9}\text{ m}$."
    },
    {
        "id": 3,
        "question": "Which of the following microbial groups is completely acellular and replicates only inside living host cells?",
        "options": [
            "Viruses",
            "Bacteria",
            "Fungi",
            "Protozoa"
        ],
        "correct": 0,
        "solution": "Step 1: Bacteria, fungi, and protozoa have cellular structures (cell membranes, cytoplasm, ribosomes).\nStep 2: Viruses are acellular particles composed strictly of a nucleic acid genome (DNA or RNA) enclosed in a protein capsid.\nStep 3: Outside host cells, viruses are inert; they can replicate only by hijacking host metabolic machinery."
    },
    {
        "id": 4,
        "question": "Which group of microorganisms includes unicellular baker's yeast and filamentous bread mold (Rhizopus)?",
        "options": [
            "Fungi",
            "Algae",
            "Bacteria",
            "Protozoa"
        ],
        "correct": 0,
        "solution": "Step 1: Yeasts and molds are heterotrophic eukaryotes with chitinous cell walls.\nStep 2: They obtain nutrients by absorbing organic matter as saprophytes.\nStep 3: Therefore, both belong to the kingdom Fungi."
    },
    {
        "id": 5,
        "question": "Which organism in pond water uses temporary flowing extensions of cytoplasm called pseudopodia to capture prey?",
        "options": [
            "Amoeba",
            "Paramecium",
            "Spirogyra",
            "Euglena"
        ],
        "correct": 0,
        "solution": "Step 1: Amoeba has a flexible cell membrane and no fixed shape.\nStep 2: It projects cytoplasmic flows termed pseudopodia ('false feet') for both locomotion and engulfing food.\nStep 3: In contrast, Paramecium uses cilia, Euglena uses a flagellum, and Spirogyra is non-motile."
    },
    {
        "id": 6,
        "question": "What happens biochemically when warm milk turns into curd after adding a small starter spoonful of curd?",
        "options": [
            "Lactobacillus multiplies and converts milk lactose into lactic acid, coagulating casein protein",
            "Yeast ferments sugar into alcohol and carbon dioxide bubbles",
            "Rhizobium converts atmospheric nitrogen into nitric acid",
            "Protozoa absorb all the water, leaving solid milk powder"
        ],
        "correct": 0,
        "solution": "Step 1: The starter curd contains millions of viable *Lactobacillus* bacteria.\nStep 2: In warm milk ($35^\\circ\\text{C}-40^\\circ\\text{C}$), they ferment lactose sugar into lactic acid.\nStep 3: The lowering pH causes milk protein (casein) to precipitate and coagulate, forming thick curd."
    },
    {
        "id": 7,
        "question": "What gas is produced during alcoholic fermentation by yeast in bread dough that causes it to rise and become spongy?",
        "options": [
            "Carbon dioxide (CO₂)",
            "Oxygen (O₂)",
            "Nitrogen (N₂)",
            "Hydrogen sulfide (H₂S)"
        ],
        "correct": 0,
        "solution": "Step 1: In the absence of oxygen, yeast (*Saccharomyces cerevisiae*) breaks down glucose:\n$$\\text{C}_6\\text{H}_{12}\\text{O}_6 \\xrightarrow{\\text{Yeast}} 2\\,\\text{C}_2\\text{H}_5\\text{OH} + 2\\,\\text{CO}_2 \\uparrow$$\nStep 2: The released $\\text{CO}_2$ gas bubbles are trapped by the elastic gluten network of the dough, making it expand and become spongy."
    },
    {
        "id": 8,
        "question": "Which scientist discovered the biological process of fermentation in 1857?",
        "options": [
            "Louis Pasteur",
            "Robert Koch",
            "Alexander Fleming",
            "Edward Jenner"
        ],
        "correct": 0,
        "solution": "Step 1: In 1857, French chemist and microbiologist Louis Pasteur demonstrated that fermentation is carried out by living microorganisms (yeast and bacteria).\nStep 2: He disproved the earlier belief that fermentation was a purely chemical, non-living decomposition."
    },
    {
        "id": 9,
        "question": "Which of the following microscopic algae has spiral, ribbon-like chloroplasts and floats on ponds as 'pond silk'?",
        "options": [
            "Spirogyra",
            "Chlamydomonas",
            "Amoeba",
            "Penicillium"
        ],
        "correct": 0,
        "solution": "Step 1: *Spirogyra* is a filamentous green alga named after its distinctive spiral, ribbon-shaped chloroplasts.\nStep 2: It forms slippery green floating mats on freshwater ponds, often termed water silk or pond silk."
    },
    {
        "id": 10,
        "question": "What cellular structure provides rigidity and prevents osmotic bursting in bacterial cells?",
        "options": [
            "A peptidoglycan cell wall",
            "A nucleus",
            "A contractile vacuole",
            "A lipid bilayer without wall"
        ],
        "correct": 0,
        "solution": "Step 1: Bacteria live in hypotonic environments where water naturally tends to flow inwards by osmosis.\nStep 2: The tough outer peptidoglycan cell wall withstands high internal turgor pressure, preventing cell lysis (bursting)."
    },

    # Questions 11–20 (Slide 18)
    {
        "id": 11,
        "question": "Why do farmers plant leguminous crops (peas, beans, pulses) in rotation with cereal crops like wheat and rice?",
        "options": [
            "Rhizobium bacteria in legume root nodules fix atmospheric nitrogen, naturally restoring soil nitrates",
            "Legumes absorb toxic chemicals and turn them into sugar",
            "Legumes do not require any sunlight to grow",
            "Legumes kill all insects living in the soil"
        ],
        "correct": 0,
        "solution": "Step 1: Legumes have root nodules hosting symbiotic *Rhizobium* bacteria.\nStep 2: *Rhizobium* converts unreactive atmospheric $\\text{N}_2$ into ammonium and nitrates.\nStep 3: This enriches soil nitrogen reserves naturally, reducing the need for expensive chemical fertilizers."
    },
    {
        "id": 12,
        "question": "Which pair of blue-green algae (cyanobacteria) can fix atmospheric nitrogen and are widely used as bio-fertilizers in rice paddies?",
        "options": [
            "Anabaena and Nostoc",
            "Spirogyra and Chlamydomonas",
            "Yeast and Penicillium",
            "Amoeba and Paramecium"
        ],
        "correct": 0,
        "solution": "Step 1: *Anabaena* and *Nostoc* are photosynthetic cyanobacteria with specialized thick-walled cells called heterocysts.\nStep 2: Heterocysts maintain an anaerobic environment suitable for the nitrogenase enzyme to convert $\\text{N}_2$ into nitrates."
    },
    {
        "id": 13,
        "question": "What is the primary role of saprophytic microorganisms in the decomposition of organic waste in a compost pit?",
        "options": [
            "Secreting enzymes to break complex organic polymers into simple soil nutrients and humus",
            "Synthesizing plastic polymers from dry leaves",
            "Generating radioactive energy to heat the soil",
            "Consuming soil oxygen and turning soil into rock"
        ],
        "correct": 0,
        "solution": "Step 1: Decomposers (bacteria and fungi) secrete digestive enzymes into dead plant and animal remains.\nStep 2: They break down proteins, cellulose, and lipids into carbon dioxide, water, and nutrient-rich dark organic humus (manure)."
    },
    {
        "id": 14,
        "question": "What is the scientific term for disease-causing microorganisms?",
        "options": [
            "Pathogens",
            "Producers",
            "Antioxidants",
            "Antibiotics"
        ],
        "correct": 0,
        "solution": "Step 1: The Greek roots *pathos* (disease) and *genes* (producer) form the word **pathogen**.\nStep 2: Any biological agent (bacterium, virus, fungus, protozoan, or worm) capable of causing disease in a host is called a pathogen."
    },
    {
        "id": 15,
        "question": "How are droplet infections like the common cold, influenza, and tuberculosis transmitted between people?",
        "options": [
            "Through microscopic aerosol droplets sneezed or coughed into the air",
            "Exclusively through mosquito bites during the night",
            "By looking into the eyes of an infected person",
            "By eating boiled vegetables"
        ],
        "correct": 0,
        "solution": "Step 1: A single sneeze can expel thousands of microscopic saliva droplets containing millions of viral or bacterial particles.\nStep 2: Healthy individuals nearby inhale these pathogen-laden airborne droplets, contracting the infection."
    },
    {
        "id": 16,
        "question": "Which insect acts as a biological vector for the deadly protozoan parasite Plasmodium, which causes malaria?",
        "options": [
            "Female Anopheles mosquito",
            "Male Culex mosquito",
            "Housefly (Musca domestica)",
            "Honeybee (Apis mellifera)"
        ],
        "correct": 0,
        "solution": "Step 1: *Plasmodium* is transmitted exclusively by the female *Anopheles* mosquito.\nStep 2: Female mosquitoes require iron and protein from human blood to produce fertile eggs."
    },
    {
        "id": 17,
        "question": "Which mosquito acts as the primary carrier (vector) of the Dengue virus?",
        "options": [
            "Aedes aegypti mosquito",
            "Anopheles mosquito",
            "Housefly",
            "Bedbug"
        ],
        "correct": 0,
        "solution": "Step 1: The Dengue virus is transmitted by female *Aedes aegypti* mosquitoes, easily recognized by white markings on their legs.\nStep 2: They bite predominantly during daylight hours and breed in clean, stagnant domestic water."
    },
    {
        "id": 18,
        "question": "How does the common housefly transmit pathogens like Vibrio cholerae onto human food?",
        "options": [
            "By sitting on garbage and feces, picking up microbes on its hairy legs, and depositing them on uncovered food",
            "By biting humans and injecting cholera into blood",
            "By laying eggs inside refrigerated milk",
            "By converting sugar directly into cholera bacteria"
        ],
        "correct": 0,
        "solution": "Step 1: Houseflies feed on human waste, sewage, and decaying garbage.\nStep 2: Pathogens adhere to the fly's legs, body hairs, and mouthparts.\nStep 3: When the fly lands on uncovered food, it deposits these pathogens, transmitting cholera, typhoid, and dysentery."
    },
    {
        "id": 19,
        "question": "Which of the following diseases is caused by a bacterial pathogen rather than a virus?",
        "options": [
            "Cholera (caused by Vibrio cholerae)",
            "Polio (caused by Poliovirus)",
            "Chickenpox (caused by Varicella zoster)",
            "Influenza (caused by Influenza virus)"
        ],
        "correct": 0,
        "solution": "Step 1: Cholera is caused by the comma-shaped bacterium *Vibrio cholerae*.\nStep 2: Polio, chickenpox, and influenza are all caused by viral pathogens."
    },
    {
        "id": 20,
        "question": "What organ in the human body is primarily attacked by Mycobacterium tuberculosis in pulmonary tuberculosis?",
        "options": [
            "Lungs",
            "Liver",
            "Kidneys",
            "Heart"
        ],
        "correct": 0,
        "solution": "Step 1: *Mycobacterium tuberculosis* is inhaled into the respiratory airways.\nStep 2: It establishes infection in the lungs (pulmonary TB), forming granulomas, destroying alveolar tissue, and causing persistent coughing with blood."
    },

    # Questions 21–30 (Slide 19)
    {
        "id": 21,
        "question": "Which protozoan parasite ingested through contaminated drinking water causes amoebic dysentery with bloody stools and abdominal cramps?",
        "options": [
            "Entamoeba histolytica",
            "Plasmodium vivax",
            "Paramecium caudatum",
            "Euglena viridis"
        ],
        "correct": 0,
        "solution": "Step 1: *Entamoeba histolytica* cysts are transmitted via food or water contaminated with fecal matter.\nStep 2: In the large intestine, active trophozoites invade the mucosa, creating ulcers that cause severe bloody dysentery."
    },
    {
        "id": 22,
        "question": "Ringworm, a common skin condition characterized by circular, dry, scaly, and intensely itchy lesions, is caused by:",
        "options": [
            "Fungi (Dermatophytes like Trichophyton)",
            "Parasitic roundworms",
            "Viruses",
            "Bacteria"
        ],
        "correct": 0,
        "solution": "Step 1: Despite its name, ringworm is not caused by a worm; it is a fungal infection caused by dermatophytes (such as *Trichophyton* and *Microsporum*).\nStep 2: These fungi feed on keratin in skin, hair, and nails in warm, humid conditions."
    },
    {
        "id": 23,
        "question": "Why does commercial packaged milk treated by pasteurization stay fresh longer in sealed cartons even without immediate boiling?",
        "options": [
            "It was heated to ~70°C for 15–30 seconds and rapidly chilled, killing vegetative pathogenic microbes",
            "All water was completely evaporated from the milk",
            "Chemical bleach was added to destroy bacteria",
            "It was exposed to radioactive nuclear rays"
        ],
        "correct": 0,
        "solution": "Step 1: In high-temperature short-time (HTST) pasteurization, milk is heated to $70^\\circ\\text{C}-72^\\circ\\text{C}$ for 15 to 30 seconds.\nStep 2: It is instantly chilled to below $10^\\circ\\text{C}$, shocking and destroying heat-sensitive pathogenic bacteria without curdling milk proteins."
    },
    {
        "id": 24,
        "question": "What physical phenomenon occurs inside bacterial cells when food is preserved with very high concentrations of salt or sugar (e.g., in pickles and jams)?",
        "options": [
            "Exosmosis (plasmolysis) draws water out of bacterial cells, halting their metabolic activity",
            "Endosmosis fills the bacteria with water until they explode",
            "The cell wall dissolves into oil",
            "The bacteria instantly freeze into ice crystals"
        ],
        "correct": 0,
        "solution": "Step 1: High salt or sugar creates a hypertonic extracellular medium with low water potential.\nStep 2: By osmosis, water moves out of the bacterial cytoplasm into the surroundings.\nStep 3: The bacterial cell shrivels (plasmolysis), inhibiting enzyme reactions and preventing cell division."
    },
    {
        "id": 25,
        "question": "Which chemical compounds are commonly used as permitted food preservatives in fruit jams, jellies, and squashes?",
        "options": [
            "Sodium Benzoate and Sodium Metabisulfite",
            "Sodium Hydroxide and Hydrochloric Acid",
            "Copper Sulfate and Lead Nitrate",
            "Calcium Carbide and Chlorine"
        ],
        "correct": 0,
        "solution": "Step 1: Sodium Benzoate and Sodium Metabisulfite are approved food additives.\nStep 2: They inhibit the growth of yeasts and molds in acidic fruit preparations without altering taste or being toxic at prescribed low levels."
    },
    {
        "id": 26,
        "question": "What is the primary function of hydrochloric acid (HCl) secreted by the gastric glands in the human stomach?",
        "options": [
            "To create a highly acidic environment (pH 1.5–2) that kills ingested pathogens and activates pepsin",
            "To produce bile for digesting fats",
            "To manufacture red blood cells",
            "To absorb oxygen from digested food"
        ],
        "correct": 0,
        "solution": "Step 1: Gastric juice contains concentrated hydrochloric acid ($\\text{HCl}$) maintaining $\\text{pH } 1.5-2.0$.\nStep 2: This intense acidity denatures proteins and destroys the cell membranes of most bacteria swallowed with food, serving as a chemical immune barrier."
    },
    {
        "id": 27,
        "question": "Which type of white blood cell patrols the tissues and engulfs invading bacteria through phagocytosis?",
        "options": [
            "Macrophages and Neutrophils",
            "Erythrocytes (Red Blood Cells)",
            "Thrombocytes (Platelets)",
            "Adipocytes (Fat cells)"
        ],
        "correct": 0,
        "solution": "Step 1: Macrophages and neutrophils are professional phagocytes.\nStep 2: They recognize foreign surface patterns, migrate to infection sites, extend pseudopods, and engulf pathogens into phagosomes for destruction."
    },
    {
        "id": 28,
        "question": "What are the cardinal signs of the inflammatory response triggered when tissues are injured and infected?",
        "options": [
            "Redness, heat, swelling, and pain caused by increased capillary blood flow and white blood cell migration",
            "Severe drop in body temperature and blue skin color",
            "Immediate growth of hair over the wound",
            "Complete numbness and bone fracture"
        ],
        "correct": 0,
        "solution": "Step 1: Injured mast cells release histamine, which dilates local blood vessels (vasodilation) and increases capillary permeability.\nStep 2: Influx of blood causes redness (*rubor*) and warmth (*calor*); fluid leakage causes swelling (*tumor*); chemical stimulation of nerve endings causes pain (*dolor*)."
    },
    {
        "id": 29,
        "question": "What is an antibody?",
        "options": [
            "A Y-shaped defensive protein produced by B-lymphocytes that binds specifically to a matching antigen",
            "A toxic protein injected by bacteria into human cells",
            "A chemical fertilizer used in agriculture",
            "A type of virus that destroys plant roots"
        ],
        "correct": 0,
        "solution": "Step 1: When B-lymphocytes detect a foreign antigen, they differentiate into plasma cells.\nStep 2: Plasma cells secrete Y-shaped immunoglobulin proteins called antibodies.\nStep 3: The variable tips of the antibody bind specifically to matching antigen epitopes, neutralizing the threat."
    },
    {
        "id": 30,
        "question": "What is the key mechanism of 'neutralization' by antibodies during a viral infection?",
        "options": [
            "Antibodies bind to viral surface spike proteins, physically preventing the virus from docking with host receptors",
            "Antibodies burn the virus with flame",
            "Antibodies feed the virus sugar until it gets tired",
            "Antibodies transform the virus into a human red blood cell"
        ],
        "correct": 0,
        "solution": "Step 1: Viruses require specific surface proteins (like spikes) to bind to host cell receptors and gain entry.\nStep 2: Antibodies coat these viral spikes, blocking the attachment sites so the virus cannot infect host cells."
    },

    # Questions 31–40 (Slide 20)
    {
        "id": 31,
        "question": "How did Edward Jenner develop the world's first successful vaccine in 1796?",
        "options": [
            "He inoculated a boy with mild cowpox fluid, which induced cross-protective immunity against lethal smallpox",
            "He boiled smallpox scabs and fed them to cows",
            "He extracted penicillin from moldy bread",
            "He filtered river water through sand"
        ],
        "correct": 0,
        "solution": "Step 1: Edward Jenner observed that milkmaids infected with benign cowpox were resistant to smallpox.\nStep 2: He inoculated James Phipps with cowpox pustule matter in 1796.\nStep 3: Because cowpox and smallpox viruses share similar surface antigens, the antibodies formed against cowpox protected against smallpox."
    },
    {
        "id": 32,
        "question": "What biological components are typically contained inside a modern vaccine?",
        "options": [
            "Weakened (attenuated) pathogens, killed pathogens, or specific purified surface antigens",
            "High doses of broad-spectrum chemical antibiotics",
            "Living lethal pathogens without any alteration",
            "Pure distilled water with salt only"
        ],
        "correct": 0,
        "solution": "Step 1: Vaccines contain weakened (attenuated), killed (inactivated), or subunit antigens (proteins, mRNA).\nStep 2: These components cannot cause full disease, but they safely stimulate the immune system to generate antibodies and memory cells."
    },
    {
        "id": 33,
        "question": "What is 'herd immunity' and why is it crucial for public health?",
        "options": [
            "When enough people are vaccinated, disease transmission drops so low that even unvaccinated individuals are protected",
            "When domestic cattle are vaccinated to stop cow fever",
            "When human beings stop drinking milk to prevent infections",
            "When a disease infects 100% of a population at the same time"
        ],
        "correct": 0,
        "solution": r"Step 1: When a high threshold (e.g. $85\%-95\%$) of a community is immunized, the pathogen cannot easily find susceptible hosts to spread.\nStep 2: Chain of transmission breaks down, protecting vulnerable individuals (newborns, immunocompromised patients) who cannot receive vaccines."
    },
    {
        "id": 34,
        "question": "In 1928, Alexander Fleming discovered the first natural antibiotic, Penicillin, after observing that:",
        "options": [
            "A green mold (Penicillium notatum) contaminating a culture plate had destroyed the surrounding Staphylococcus colonies",
            "Boiling milk killed all bacteria",
            "Yeast fermented grape juice into wine",
            "Cowpox fluid cured rabies in dogs"
        ],
        "correct": 0,
        "solution": "Step 1: Fleming returned from vacation to find a fungal mold (*Penicillium notatum*) growing on an unwashed *Staphylococcus* agar plate.\nStep 2: He noticed a clear, bacteria-free halo around the mold where bacterial cells had lysed.\nStep 3: He deduced the mold was secreting an antibacterial substance, which he named penicillin."
    },
    {
        "id": 35,
        "question": "How do penicillin and related beta-lactam antibiotics selectively kill bacteria without harming human cells?",
        "options": [
            "They inhibit the synthesis of bacterial peptidoglycan cell walls, a structure human cells completely lack",
            "They destroy human mitochondria",
            "They freeze the nucleus of bacteria",
            "They make bacteria too heavy to swim"
        ],
        "correct": 0,
        "solution": "Step 1: Bacteria rely on a rigid peptidoglycan cell wall to maintain structural integrity against osmotic pressure.\nStep 2: Penicillin blocks the transpeptidase enzymes that cross-link peptidoglycan chains.\nStep 3: Because human cells possess only a plasma membrane and lack peptidoglycan cell walls, penicillin is selectively toxic to bacteria."
    },
    {
        "id": 36,
        "question": "Why are antibiotics completely ineffective against viral diseases like the common cold, flu, COVID-19, or measles?",
        "options": [
            "Viruses do not possess cell walls, ribosomes, or their own metabolic machinery for antibiotics to target",
            "Viruses eat antibiotics as food",
            "Antibiotics cannot dissolve in human blood",
            "Viruses are 1000 times larger than bacteria"
        ],
        "correct": 0,
        "solution": "Step 1: Antibiotics work by disrupting specific bacterial pathways (cell wall synthesis, 70S ribosomes, bacterial folate synthesis).\nStep 2: Viruses are acellular and lack these structures; they use the host's own cellular machinery to replicate, rendering bacterial antibiotics useless."
    },
    {
        "id": 37,
        "question": "What serious medical crisis occurs when patients take antibiotics improperly or fail to complete the prescribed full course?",
        "options": [
            "Surviving bacteria develop antibiotic resistance, producing multi-drug-resistant 'superbugs'",
            "The human body permanently stops producing red blood cells",
            "All bacteria on Earth go extinct",
            "The patient develops smallpox instantly"
        ],
        "correct": 0,
        "solution": "Step 1: Incomplete or indiscriminate antibiotic use kills only sensitive bacteria, leaving partially resistant bacteria alive.\nStep 2: These surviving bacteria multiply and spread resistance genes, leading to multi-drug-resistant 'superbugs' untreatable by standard medicines."
    },
    {
        "id": 38,
        "question": "Which vitamin, abundant in amla, oranges, lemons, and guavas, is essential for maintaining strong immune phagocyte activity?",
        "options": [
            "Vitamin C (Ascorbic acid)",
            "Vitamin K",
            "Vitamin D",
            "Vitamin B12"
        ],
        "correct": 0,
        "solution": "Step 1: Vitamin C (ascorbic acid) is a water-soluble antioxidant.\nStep 2: It accumulates in phagocytes and lymphocytes, enhancing chemotaxis, phagocytosis, and the generation of reactive oxygen species to kill engulfed pathogens."
    },
    {
        "id": 39,
        "question": "Why does washing hands with soap and warm water for at least 20 seconds effectively eliminate viral pathogens?",
        "options": [
            "Soap molecules have hydrophobic tails that insert into and break apart the lipid membrane of enveloped viruses",
            "Soap freezes viruses at room temperature",
            "Soap changes water into strong hydrochloric acid",
            "Soap turns virus RNA into pure gold"
        ],
        "correct": 0,
        "solution": "Step 1: Many viruses (including Influenza, Coronaviruses, and Measles) are enveloped in a protective lipid (fat) membrane.\nStep 2: Soap contains amphiphilic molecules whose hydrophobic tails wedge into this lipid bilayer, rupturing the viral membrane and washing away fragments."
    },
    {
        "id": 40,
        "question": "Which combination of public health measures is most effective for preventing outbreaks of waterborne diseases like cholera and typhoid?",
        "options": [
            "Providing boiled or chlorinated drinking water, sanitary sewage disposal, and personal hand hygiene",
            "Spraying perfume into storm drains and avoiding sunlight",
            "Taking antibiotic tablets daily throughout life without medical advice",
            "Drinking raw unboiled river water to build resistance"
        ],
        "correct": 0,
        "solution": "Step 1: Waterborne pathogens (*Vibrio cholerae*, *Salmonella typhi*) spread through the fecal-oral route.\nStep 2: Effective prevention requires boiling or chlorinating drinking water, properly treating municipal sewage to prevent groundwater contamination, and washing hands before handling food."
    }
]
