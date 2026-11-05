"""
Part 3 Generator for NCERT Class 5 Science - Chapter 2: Journey of a River
Mastery Challenges (Slides 17 to 20):
- 40 Rigorous Multiple-Choice Questions (10 per challenge)
- Options A, B, C, D
- 0-indexed correct answer
- Scientific explanation
- Step-by-step solution HTML
- Zero raw LaTeX (Clean Unicode only)
"""

QUIZ_QUESTIONS = [
    # ==================== Challenge 1 (Questions 1 to 10) ====================
    {
        "id": 1,
        "question": "Where does the Godavari River originate in the Western Ghats?",
        "options": [
            "Brahmagiri Hills at Trimbakeshwar, Maharashtra",
            "Gangotri Glacier in Uttarakhand",
            "Amarkantak Plateau in Madhya Pradesh",
            "Muppandal in Tamil Nadu"
        ],
        "answer": 0,
        "explanation": "The Godavari originates at Trimbakeshwar in the Brahmagiri Hills of the Western Ghats, Nashik district, Maharashtra.",
        "solution_html": "<p><strong>Step-by-step Geographical Origin:</strong></p><p>1. <strong>Source Location:</strong> Brahmagiri Hills at Trimbakeshwar, Nashik district, Maharashtra.</p><p>2. <strong>Elevation:</strong> Approximately 1,067 m above mean sea level.</p><p>3. <strong>Cultural Title:</strong> Revered as 'Dakshin Ganga' (Ganga of the South).</p>"
    },
    {
        "id": 2,
        "question": "What is the total length of the Godavari River from its origin to its mouth at the Bay of Bengal?",
        "options": [
            "Approximately 1,465 kilometres",
            "Approximately 200 kilometres",
            "Over 10,000 kilometres",
            "Exactly 500 metres"
        ],
        "answer": 0,
        "explanation": "The Godavari flows for about 1,465 km, making it the longest river in Peninsular India and the second longest river in the entire country.",
        "solution_html": "<p><strong>Step-by-step River Length Verification:</strong></p><p>1. <strong>Total Distance:</strong> 1,465 km (910 miles).</p><p>2. <strong>Basin Extent:</strong> Spans across Maharashtra, Telangana, Andhra Pradesh, Chhattisgarh, and Odisha, covering nearly 10% of India's total geographical area.</p>"
    },
    {
        "id": 3,
        "question": "Into which major body of water does the Godavari River empty at the end of its journey?",
        "options": [
            "The Bay of Bengal",
            "The Arabian Sea",
            "The Arctic Ocean",
            "The Caspian Sea"
        ],
        "answer": 0,
        "explanation": "After flowing eastward across peninsular India, the Godavari splits into distributaries in Andhra Pradesh and empties into the Bay of Bengal.",
        "solution_html": "<p><strong>Step-by-step Drainage Verification:</strong></p><p>1. <strong>Eastward Flow:</strong> Peninsular tilt slopes gently eastward toward the Bay of Bengal.</p><p>2. <strong>Delta Discharge:</strong> The river enters the Bay of Bengal through multiple mouths near Yanam and Antarvedi.</p>"
    },
    {
        "id": 4,
        "question": "What is the term for a smaller river or stream that flows into and joins a larger parent river?",
        "options": [
            "A tributary",
            "A glacier",
            "An ocean trench",
            "An island"
        ],
        "answer": 0,
        "explanation": "A tributary is a freshwater stream or feeder river that joins a larger parent river, increasing its width, depth, and volume.",
        "solution_html": "<p><strong>Step-by-step Terminology:</strong></p><p>1. <strong>Tributary:</strong> A stream contributing water to a main river.</p><p>2. <strong>Distributary:</strong> A stream that branches off from the main river near its delta and flows away into the sea.</p>"
    },
    {
        "id": 5,
        "question": "Which of the following is a major left-bank tributary of the Godavari River that flows through Bastar?",
        "options": [
            "Indravati River",
            "Yamuna River",
            "Narmada River",
            "Kaveri River"
        ],
        "answer": 0,
        "explanation": "The Indravati River originates in Odisha, flows through Bastar in Chhattisgarh, and joins the Godavari as a major left-bank tributary.",
        "solution_html": "<p><strong>Step-by-step Tributary Mapping:</strong></p><p>1. <strong>Indravati:</strong> Rushes through the dense sal forests of Dandakaranya.</p><p>2. <strong>Confluence:</strong> Joins the Godavari at the border junction of Maharashtra, Chhattisgarh, and Telangana.</p>"
    },
    {
        "id": 6,
        "question": "Why is the Godavari classified as a 'perennial river'?",
        "options": [
            "It maintains a continuous flow of water throughout all twelve months of the year",
            "It flows only during heavy thunderstorms for two days",
            "It flows only underground in total darkness",
            "Its water turns into solid ice every afternoon"
        ],
        "answer": 0,
        "explanation": "Perennial rivers flow continuously throughout the year, sustained by reliable groundwater aquifers, deep springs, and extensive tributary networks.",
        "solution_html": "<p><strong>Step-by-step River Classification:</strong></p><p>1. <strong>Perennial River:</strong> Year-round continuous discharge (e.g., Godavari, Ganga).</p><p>2. <strong>Seasonal/Non-perennial River:</strong> Water flows only during the monsoon season, drying to isolated pools in summer.</p>"
    },
    {
        "id": 7,
        "question": "How do seasonal rain-fed rivers differ fundamentally from perennial rivers?",
        "options": [
            "Seasonal rivers flow only during and shortly after the monsoon, drying up in summer",
            "Seasonal rivers contain boiling saltwater",
            "Seasonal rivers flow backwards up mountain peaks",
            "There is no difference between them"
        ],
        "answer": 0,
        "explanation": "Seasonal rivers rely entirely on seasonal rainfall runoff without persistent glacial or deep spring baseflow, drying out during hot summer months.",
        "solution_html": "<p><strong>Step-by-step Hydrological Distinction:</strong></p><p>1. <strong>Baseflow Source:</strong> Perennial rivers have sustained baseflow from aquifers/glaciers.</p><p>2. <strong>Ephemeral Nature:</strong> Seasonal rivers lack sufficient baseflow, so the riverbed dries into sand during rainless months.</p>"
    },
    {
        "id": 8,
        "question": "What is the meeting point where a tributary merges with the main river called in India?",
        "options": [
            "A confluence (Sangam)",
            "A crater",
            "A volcano",
            "A desert ridge"
        ],
        "answer": 0,
        "explanation": "The junction where two or more rivers or streams meet and blend their waters is called a confluence, known culturally in India as a 'Sangam'.",
        "solution_html": "<p><strong>Step-by-step Confluence Definition:</strong></p><p>1. <strong>Confluence:</strong> The geographic point where a tributary flows into a parent river.</p><p>2. <strong>Examples:</strong> Prayagraj (Ganga & Yamuna), Someshwara (Godavari & Indravati).</p>"
    },
    {
        "id": 9,
        "question": "Which of the following is a key right-bank tributary that joins the Godavari after flowing through Karnataka and Telangana?",
        "options": [
            "Manjira River",
            "Brahmaputra River",
            "Sutlej River",
            "Indus River"
        ],
        "answer": 0,
        "explanation": "The Manjira River is a major right-bank tributary of the Godavari, providing drinking water to Hyderabad and surrounding districts.",
        "solution_html": "<p><strong>Step-by-step Basin Hydrography:</strong></p><p>1. <strong>Manjira:</strong> Originates in Balaghat range, passes through Maharashtra, Karnataka, and Telangana.</p><p>2. <strong>Importance:</strong> Nizamsagar and Singur reservoirs are built across the Manjira River.</p>"
    },
    {
        "id": 10,
        "question": "Why is the Godavari River culturally celebrated across India as 'Dakshin Ganga'?",
        "options": [
            "It is the largest, longest, and most sacred river in Southern (Peninsular) India",
            "It is painted blue by priests",
            "It flows only at midnight",
            "It was built by modern factory workers"
        ],
        "answer": 0,
        "explanation": "Due to its vast length (1,465 km), immense basin area, spiritual significance, and life-giving role across the Deccan, it is revered as the Southern Ganga.",
        "solution_html": "<p><strong>Step-by-step Cultural Geography:</strong></p><p>1. <strong>Dakshin Ganga:</strong> 'Dakshin' means South. Just as the Ganga is the lifeline of Northern India, the Godavari is the spiritual and agricultural lifeline of Peninsular India.</p>"
    },

    # ==================== Challenge 2 (Questions 11 to 20) ====================
    {
        "id": 11,
        "question": "What rare, nocturnal reptile endemic to rocky river gorges is found in the Godavari basin?",
        "options": [
            "Indian Golden Gecko",
            "Chameleon of Africa",
            "Galapagos giant tortoise",
            "Komodo dragon"
        ],
        "answer": 0,
        "explanation": "The Indian Golden Gecko (Calodactylodes aureus) is a rare, protected gecko found in rocky boulder crevices of the Eastern Ghats along river valleys.",
        "solution_html": "<p><strong>Step-by-step Biodiversity Verification:</strong></p><p>1. <strong>Endemic Species:</strong> Confined exclusively to specific habitats of the Eastern Ghats in Andhra Pradesh, Odisha, and Tamil Nadu.</p><p>2. <strong>Habitat:</strong> Granite rock faces and riparian boulder clefts.</p>"
    },
    {
        "id": 12,
        "question": "What is the name of the renowned mangrove wetland located at the mouth of the Godavari River in Andhra Pradesh?",
        "options": [
            "Coringa Mangroves",
            "Thar Desert dunes",
            "Gir Lion Sanctuary",
            "Valley of Flowers"
        ],
        "answer": 0,
        "explanation": "The Coringa Wildlife Sanctuary and mangrove forest is situated in the Godavari estuary near Kakinada, Andhra Pradesh.",
        "solution_html": "<p><strong>Step-by-step Mangrove Geography:</strong></p><p>1. <strong>Coringa:</strong> Spans over 235 square kilometers in the Godavari delta.</p><p>2. <strong>Significance:</strong> Second largest stretch of mangrove forests on India's east coast after the Sundarbans.</p>"
    },
    {
        "id": 13,
        "question": "What are pneumatophores?",
        "options": [
            "Vertical breathing roots of mangrove trees that project above coastal mud to take in atmospheric air",
            "Heavy stones used to anchor fishing boats",
            "Poisonous thorns found on cactus plants",
            "Deep underground caves where bats live"
        ],
        "answer": 0,
        "explanation": "Pneumatophores are specialized erect roots produced by mangroves that grow upward out of waterlogged, anaerobic mud to breathe atmospheric oxygen through lenticels.",
        "solution_html": "<p><strong>Step-by-step Botanical Adaptation:</strong></p><p>1. <strong>Anaerobic Substrate:</strong> Coastal estuarine mud is saturated with water and lacks dissolved oxygen.</p><p>2. <strong>Negative Geotropism:</strong> Mangrove roots grow upward against gravity into the air to absorb oxygen for root respiration.</p>"
    },
    {
        "id": 14,
        "question": "How do mangrove forests in river deltas protect coastal villages during severe ocean cyclones?",
        "options": [
            "Their dense stilt root network acts as a natural bio-shield, absorbing wave energy and reducing storm surges",
            "They blow giant fans that push cyclone winds into space",
            "They turn seawater into fresh ice cream",
            "They make the sea disappear"
        ],
        "answer": 0,
        "explanation": "The dense interlocking roots and trunks of mangroves dramatically attenuate cyclone wind speeds and dissipate the destructive kinetic energy of storm surge waves.",
        "solution_html": "<p><strong>Step-by-step Coastal Protection:</strong></p><p>1. <strong>Wave Dissipation:</strong> Mangrove roots and trunks reduce wave height by up to 66% over 100 meters of forest.</p><p>2. <strong>Soil Stabilization:</strong> Root networks prevent coastal erosion and bind delta sediments.</p>"
    },
    {
        "id": 15,
        "question": "Which valuable, fragrant timber tree is native to the hill forests of the Godavari river basin?",
        "options": [
            "Red Sandalwood (Raktachandan)",
            "Arctic spruce",
            "Coconut palm of beaches",
            "Desert cactus"
        ],
        "answer": 0,
        "explanation": "Red Sandalwood (Pterocarpus santalinus) is a prized, endemic timber tree native to the rocky hills of the Eastern Ghats in Andhra Pradesh.",
        "solution_html": "<p><strong>Step-by-step Forestry Verification:</strong></p><p>1. <strong>Species:</strong> Pterocarpus santalinus, valued for its rich red-hued, dense acoustic wood and therapeutic properties.</p><p>2. <strong>Conservation:</strong> Strictly protected under national forestry laws.</p>"
    },
    {
        "id": 16,
        "question": "What is ecotourism along river valleys?",
        "options": [
            "Responsible travel to natural areas to observe wildlife and scenery without harming the environment",
            "Building giant cement chemical factories along the riverbank",
            "Dumping busloads of plastic bottles into the water",
            "Hunting endangered animals with guns"
        ],
        "answer": 0,
        "explanation": "Ecotourism emphasizes low-impact, sustainable travel that fosters environmental awareness, respects wildlife, and provides livelihood opportunities to local communities.",
        "solution_html": "<p><strong>Step-by-step Ecotourism Principles:</strong></p><p>1. <strong>Low Impact:</strong> Leaving zero plastic waste and causing no habitat disruption.</p><p>2. <strong>Community Benefit:</strong> Generates fair income for local boat operators, homestays, and nature guides.</p>"
    },
    {
        "id": 17,
        "question": "What famous scenic gorge on the Godavari is a celebrated destination for river ecotourism boat tours?",
        "options": [
            "Papikondalu (Papi Hills)",
            "Kolkata Howrah Bridge",
            "Gateway of India",
            "Qutub Minar"
        ],
        "answer": 0,
        "explanation": "Papikondalu is a dramatic river gorge where the Godavari narrows to squeeze between verdant mountain cliffs in Andhra Pradesh.",
        "solution_html": "<p><strong>Step-by-step Ecotourism Geography:</strong></p><p>1. <strong>Location:</strong> Rajahmundry to Bhadrachalam stretch along the Godavari.</p><p>2. <strong>Scenery:</strong> Breathtaking forested hills flanking the calm, winding river channel.</p>"
    },
    {
        "id": 18,
        "question": "Approximately how many large and medium dams have been constructed across the Godavari River basin?",
        "options": [
            "Over 900 dams",
            "Exactly zero dams",
            "Only one small pond",
            "Over 50,000 dams"
        ],
        "answer": 0,
        "explanation": "Due to extensive irrigation and power requirements, more than 900 large and medium dams and barrages regulate flow across the Godavari basin.",
        "solution_html": "<p><strong>Step-by-step Water Engineering:</strong></p><p>1. <strong>Dams in Basin:</strong> Over 900 dams (e.g., Jayakwadi, Sriram Sagar, Nizam Sagar, Upper Penganga, Polavaram).</p><p>2. <strong>Purpose:</strong> Water storage for dry months, irrigation, flood control, and power generation.</p>"
    },
    {
        "id": 19,
        "question": "What is the primary function of building a dam across a flowing river?",
        "options": [
            "To store water in a reservoir for dry seasons, irrigation, drinking, and hydroelectric power",
            "To turn fresh water into boiling oil",
            "To stop the river from ever reaching the ocean",
            "To build shopping malls in the riverbed"
        ],
        "answer": 0,
        "explanation": "Dams hold back river flow during monsoon surplus, creating artificial reservoirs that release water steadily during dry months for cities and farming.",
        "solution_html": "<p><strong>Step-by-step Dam Multi-Purpose Functions:</strong></p><p>1. <strong>Irrigation:</strong> Directs water through canals to farmland.</p><p>2. <strong>Municipal Supply:</strong> Supplies potable water to cities.</p><p>3. <strong>Hydroelectricity:</strong> Water drops through turbines generating carbon-free power.</p>"
    },
    {
        "id": 20,
        "question": "Which of the following is a major landmark dam located on the Godavari River in Maharashtra?",
        "options": [
            "Jayakwadi Dam near Paithan",
            "Bhakra Nangal Dam in Himachal",
            "Hirakud Dam in Odisha",
            "Tehri Dam in Uttarakhand"
        ],
        "answer": 0,
        "explanation": "Jayakwadi Dam (Nath Sagar reservoir) on the Godavari at Paithan, Maharashtra, is one of the largest earthen dams in Asia.",
        "solution_html": "<p><strong>Step-by-step Landmark Dam Identification:</strong></p><p>1. <strong>Jayakwadi:</strong> Built across the Godavari River in Paithan, Chhatrapati Sambhajinagar (Aurangabad) district, Maharashtra.</p><p>2. <strong>Benefit:</strong> Irrigates over 2.5 lakh hectares of drought-prone Marathwada farmland.</p>"
    },

    # ==================== Challenge 3 (Questions 21 to 30) ====================
    {
        "id": 21,
        "question": "What negative ecological effect can occur upstream when a large dam reservoir fills with water?",
        "options": [
            "Thousands of hectares of forests and wildlife habitats are permanently submerged",
            "The clouds stop raining completely everywhere",
            "The mountains turn into dust",
            "The Sun disappears"
        ],
        "answer": 0,
        "explanation": "Filling a reservoir inundates valley forests, drowning plant life, destroying terrestrial wildlife habitats, and disrupting ecological corridors.",
        "solution_html": "<p><strong>Step-by-step Environmental Assessment:</strong></p><p>1. <strong>Submergence:</strong> Forests, riverbanks, and fertile soils are submerged beneath deep reservoir waters.</p><p>2. <strong>Habitat Fragmentation:</strong> Terrestrial animals are displaced or isolated on reservoir islands.</p>"
    },
    {
        "id": 22,
        "question": "How does dam construction impact human communities residing in valley villages?",
        "options": [
            "Villages are submerged, displacing families and requiring comprehensive resettlement and rehabilitation",
            "Villagers receive wings to fly across clouds",
            "All villages become independent nations",
            "Dams have zero effect on human settlements"
        ],
        "answer": 0,
        "explanation": "Large reservoirs submerge villages, farmlands, and schools, forcing thousands of families (often indigenous tribal communities) to relocate.",
        "solution_html": "<p><strong>Step-by-step Social Impact:</strong></p><p>1. <strong>Displacement:</strong> Involuntary loss of ancestral homes, agricultural lands, and livelihoods.</p><p>2. <strong>Rehabilitation:</strong> Governments must provide fair compensation, new housing, and sustainable livelihood support.</p>"
    },
    {
        "id": 23,
        "question": "What is the primary source of domestic pollution that enters rivers from modern cities?",
        "options": [
            "Untreated sewage containing toilet waste, detergents, and soapy wastewater",
            "Fallen flower petals",
            "Clean rainwater from mountain skies",
            "Pure mineral spring water"
        ],
        "answer": 0,
        "explanation": "Municipal drains often empty millions of liters of untreated domestic sewage and greywater directly into rivers, introducing harmful pathogens.",
        "solution_html": "<p><strong>Step-by-step Urban Water Pollution:</strong></p><p>1. <strong>Point Source Pollution:</strong> Sewage discharge pipes releasing faecal coliforms, phosphates from detergents, and organic waste.</p><p>2. <strong>Remedy:</strong> Installation and 100% operation of Sewage Treatment Plants (STPs).</p>"
    },
    {
        "id": 24,
        "question": "Why is plastic waste dumped into rivers especially hazardous to aquatic creatures like fish and river turtles?",
        "options": [
            "Plastic never decomposes naturally; animals can ingest it or become fatally entangled in it",
            "Plastic dissolves into pure sugar that makes fish overweight",
            "Plastic turns into clean oxygen bubbles",
            "Plastic attracts lightning bolts to the water"
        ],
        "answer": 0,
        "explanation": "Plastics persist for centuries, breaking into microplastics. Fish and turtles mistake plastic debris for food, causing intestinal blockages and death.",
        "solution_html": "<p><strong>Step-by-step Marine & Riverine Plastic Hazards:</strong></p><p>1. <strong>Ingestion:</strong> Blocks digestive tracts and starves aquatic organisms.</p><p>2. <strong>Entanglement:</strong> Discarded fishing nets and plastic rings trap turtles and diving birds.</p>"
    },
    {
        "id": 25,
        "question": "What harmful condition occurs when agricultural fertilizers wash from farm fields into a river?",
        "options": [
            "Eutrophication: an explosive growth of algae and weeds forms a 'green blanket' that depletes oxygen",
            "The river turns into sparkling mineral water",
            "The water freezes into solid diamond",
            "Fish double in size within two minutes"
        ],
        "answer": 0,
        "explanation": "Fertilizers contain nitrogen and phosphorus that over-nourish algae, causing rapid algal blooms that cover the surface like a green blanket and starve the water of oxygen.",
        "solution_html": "<p><strong>Step-by-step Eutrophication Process:</strong></p><p>1. <strong>Nutrient Runoff:</strong> Excess N and P from fertilizers enter water.</p><p>2. <strong>Algal Bloom:</strong> Massive population explosion of algae and water hyacinth.</p><p>3. <strong>Oxygen Depletion:</strong> Decay of dead algae consumes dissolved oxygen, creating dead zones.</p>"
    },
    {
        "id": 26,
        "question": "Why do fish die when an overgrown 'green blanket' of algae in a polluted river decays?",
        "options": [
            "Decomposing bacteria consume all the dissolved oxygen in the water, causing fish to suffocate",
            "The green algae bite the fish fins",
            "The water turns into solid wood",
            "Fish forget how to swim"
        ],
        "answer": 0,
        "explanation": "Aerobic bacteria that feed on decaying algae multiply rapidly and consume dissolved oxygen, lowering oxygen levels below the threshold fish need to breathe.",
        "solution_html": "<p><strong>Step-by-step Dissolved Oxygen Depletion:</strong></p><p>1. <strong>Bacterial Decomposition:</strong> Dead algae sink and decay.</p><p>2. <strong>Hypoxia:</strong> Bacterial respiration drives dissolved oxygen below 2 mg/L, suffocating aquatic gill-breathing animals.</p>"
    },
    {
        "id": 27,
        "question": "What natural seasonal event causes rivers to swell dramatically and overflow their banks onto floodplains?",
        "options": [
            "Intense, prolonged monsoon rainfall across the river catchment",
            "A mild evening breeze",
            "A drop in atmospheric humidity",
            "Falling autumn leaves"
        ],
        "answer": 0,
        "explanation": "Continuous heavy monsoon downpours generate surface runoff that exceeds the carrying capacity of the river channel, causing it to breach its banks.",
        "solution_html": "<p><strong>Step-by-step Flood Mechanics:</strong></p><p>1. <strong>Precipitation Input:</strong> Extreme rain over saturated soils.</p><p>2. <strong>Channel Overflow:</strong> Peak flood discharge exceeds channel capacity, inundating adjacent floodplains.</p>"
    },
    {
        "id": 28,
        "question": "What is a river floodplain?",
        "options": [
            "The flat, low-lying land adjacent to a river that naturally receives water and sediment during floods",
            "A mountaintop where snow never melts",
            "A desert with zero water",
            "An underground gold mine"
        ],
        "answer": 0,
        "explanation": "A floodplain is the natural valley floor bordering a river that acts as a buffer zone, accommodating excess water during peak floods.",
        "solution_html": "<p><strong>Step-by-step Fluvial Geomorphology:</strong></p><p>1. <strong>Floodplain Role:</strong> Natural safety valve for floodwaters.</p><p>2. <strong>Human Hazard:</strong> Building permanent concrete settlements on floodplains leads to catastrophic urban disasters.</p>"
    },
    {
        "id": 29,
        "question": "What valuable material does a river deposit on its floodplain during floods that benefits agriculture?",
        "options": [
            "Fertile mineral-rich alluvial silt",
            "Crushed plastic bottles",
            "Chemical paint sludge",
            "Solid iron ore slabs"
        ],
        "answer": 0,
        "explanation": "Floodwaters carry fine mineral sediments eroded from upstream mountains, laying down a fresh, fertile layer of alluvium that rejuvenates farmland.",
        "solution_html": "<p><strong>Step-by-step Alluvial Renewal:</strong></p><p>1. <strong>Sediment Deposition:</strong> As floodwaters spread and slow down, suspended silt settles.</p><p>2. <strong>Nutrient Replenishment:</strong> Adds potassium, phosphorus, and organic matter without chemical fertilizers.</p>"
    },
    {
        "id": 30,
        "question": "Which of the following industrial pollutants dumped into rivers can cause severe long-term poisoning in humans?",
        "options": [
            "Toxic heavy metals like lead and mercury",
            "Clean rainwater from clouds",
            "Fallen mango leaves",
            "Pure river sand"
        ],
        "answer": 0,
        "explanation": "Industrial effluents from tanneries, chemical factories, and metal plating plants release heavy metals (mercury, lead, cadmium) that bioaccumulate in fish and poison humans.",
        "solution_html": "<p><strong>Step-by-step Heavy Metal Bioaccumulation:</strong></p><p>1. <strong>Toxicity:</strong> Heavy metals do not break down in water.</p><p>2. <strong>Biomagnification:</strong> Plankton ➔ Small Fish ➔ Big Fish ➔ Humans, causing severe neurological, kidney, and liver damage.</p>"
    },

    # ==================== Challenge 4 (Questions 31 to 40) ====================
    {
        "id": 31,
        "question": "How do trees and riverside forests act as natural flood shields?",
        "options": [
            "Canopies break raindrop velocity, spongy humus absorbs water, and roots anchor riverbanks",
            "Trees turn all floodwaters into solid ice",
            "Trees push the river into outer space",
            "Trees drink all the water in one second"
        ],
        "answer": 0,
        "explanation": "Forests intercept rain, increase soil infiltration, reduce surface runoff speed, and their root mesh binds riverbanks to prevent erosion.",
        "solution_html": "<p><strong>Step-by-step Watershed Hydrology:</strong></p><p>1. <strong>Interception:</strong> Canopies cushion rain impact.</p><p>2. <strong>Infiltration Sponge:</strong> Humus and root conduits absorb precipitation.</p><p>3. <strong>Bank Stabilization:</strong> Roots physically anchor soil against hydraulic shear stress.</p>"
    },
    {
        "id": 32,
        "question": "Why does clear-cutting forests in mountain catchments make downstream floods far worse?",
        "options": [
            "Rainwater rushes rapidly down bare slopes in minutes, carrying eroded mud that silts up riverbeds",
            "The mountains turn into gold nuggets",
            "The river starts flowing backward into the sky",
            "The clouds stop raining"
        ],
        "answer": 0,
        "explanation": "Without trees to intercept and absorb rainwater, surface runoff surges rapidly into rivers, and severe soil erosion silts up channels, reducing their carrying capacity.",
        "solution_html": "<p><strong>Step-by-step Deforestation Impact:</strong></p><p>1. <strong>Accelerated Runoff:</strong> Peak flood timing becomes shorter and far more intense.</p><p>2. <strong>Siltation:</strong> Eroded topsoil raises riverbed levels, making future floods more frequent and severe.</p>"
    },
    {
        "id": 33,
        "question": "What is the single most critical safety rule when encountering fast-flowing floodwaters across a road?",
        "options": [
            "Never attempt to walk, swim, or drive through moving floodwaters ('Turn Around, Don't Drown')",
            "Jump in and try to swim across for exercise",
            "Wash your school backpack in the current",
            "Drive the car as fast as possible through the water"
        ],
        "answer": 0,
        "explanation": "Just 15 cm of rushing water can knock an adult off their feet, and 30 cm can float a vehicle. Collapsed bridges and roadbeds under murky water make crossing deadly.",
        "solution_html": "<p><strong>Step-by-step Flood Safety Principle:</strong></p><p>1. <strong>Hydrodynamic Force:</strong> Moving water exerts immense lateral force.</p><p>2. <strong>Universal Protocol:</strong> 'Turn Around, Don't Drown' — seek high ground immediately.</p>"
    },
    {
        "id": 34,
        "question": "What must families do with drinking water after returning home following a major river flood?",
        "options": [
            "Boil it vigorously for at least one minute to kill waterborne bacteria and pathogens",
            "Drink straight from murky flooded wells",
            "Mix it with dirt to make it thicker",
            "Store it in rusty iron barrels in the sun"
        ],
        "answer": 0,
        "explanation": "Floods contaminate wells and municipal pipes with sewage, mud, and microbes; boiling kills deadly waterborne pathogens (cholera, typhoid).",
        "solution_html": "<p><strong>Step-by-step Post-Disaster Sanitation:</strong></p><p>1. <strong>Contamination:</strong> Floodwaters breach sewerage networks and submerge drinking water wells.</p><p>2. <strong>Disinfection:</strong> Rolling boil for at least 1 minute destroys bacteria, viruses, and parasites.</p>"
    },
    {
        "id": 35,
        "question": "What severe urban water emergency occurred in the city of Chennai during the summer of 2019?",
        "options": [
            "All four major drinking water reservoirs ran completely dry ('Day Zero'), requiring special water trains",
            "The entire city was buried under ten meters of snow",
            "The sea water turned into boiling soup",
            "All taps began dispensing petrol"
        ],
        "answer": 0,
        "explanation": "A severe drought dried up Chennai's four reservoirs (Poondi, Cholavaram, Red Hills, Chembarambakkam), forcing Indian Railways to run special water trains to save the city.",
        "solution_html": "<p><strong>Step-by-step Chennai 2019 Water Crisis:</strong></p><p>1. <strong>Day Zero:</strong> Major municipal reservoirs dried up due to consecutive monsoon deficits and poor recharge.</p><p>2. <strong>Jaldoot Express:</strong> 50-wagon trains carried millions of liters from Jolarpettai to Chennai daily.</p>"
    },
    {
        "id": 36,
        "question": "What was the special railway train deployed by Indian Railways to carry drinking water to Chennai in 2019 called?",
        "options": [
            "Jaldoot Water Train",
            "Bullet Train Express",
            "Himalayan Glacier Rocket",
            "Desert Dune Cruiser"
        ],
        "answer": 0,
        "explanation": "The 'Jaldoot' water train comprised 50 modified BTPN railway tank wagons carrying millions of liters of fresh water per trip from Jolarpettai.",
        "solution_html": "<p><strong>Step-by-step Emergency Logistics:</strong></p><p>1. <strong>Operation:</strong> Dispatched by Indian Railways to relieve severe municipal water distress.</p><p>2. <strong>Capacity:</strong> Delivered 2.5 to 5 million liters of drinking water per day directly into Chennai's distribution network.</p>"
    },
    {
        "id": 37,
        "question": "What is an automated 'Water ATM'?",
        "options": [
            "A decentralized public kiosk that dispenses purified drinking water when a coin or smart card is used",
            "A machine that prints paper currency notes from river water",
            "A device that sprays cold water on passing aeroplanes",
            "A kitchen refrigerator that cooks rice"
        ],
        "answer": 0,
        "explanation": "Water ATMs are self-service automated kiosks dispensing clean, affordable RO/UV-filtered drinking water in rural and urban areas, eliminating single-use plastic bottles.",
        "solution_html": "<p><strong>Step-by-step Water ATM Technology:</strong></p><p>1. <strong>Function:</strong> Purifies local water via RO/UV and dispenses precise quantities upon swiping a card or inserting a coin.</p><p>2. <strong>Benefits:</strong> Affordable clean water, reduction in waterborne diseases, and zero plastic bottle waste.</p>"
    },
    {
        "id": 38,
        "question": "What is the primary objective of India's 'National Water Mission'?",
        "options": [
            "To conserve water, minimize wastage, and increase water-use efficiency across all sectors by 20%",
            "To pump all river water into outer space",
            "To build concrete roofs over all oceans",
            "To replace all rivers with tar roads"
        ],
        "answer": 0,
        "explanation": "The National Water Mission, under the National Action Plan on Climate Change, focuses on water conservation, rainwater harvesting ('Catch the Rain'), and a 20% boost in water efficiency.",
        "solution_html": "<p><strong>Step-by-step Policy Verification:</strong></p><p>1. <strong>Mission Goal:</strong> Integrated water resources management and 20% water use efficiency increase.</p><p>2. <strong>Campaign:</strong> 'Catch the Rain, Where it Falls, When it Falls' encourages widespread rainwater harvesting.</p>"
    },
    {
        "id": 39,
        "question": "Which of the following everyday domestic habits can save up to 15 liters of pure water per person every day?",
        "options": [
            "Turning off the running tap while brushing teeth and soaping hands",
            "Leaving the garden hose running on the driveway all day",
            "Washing a bicycle with three hundred liters of water",
            "Taking five 30-minute showers every day"
        ],
        "answer": 0,
        "explanation": "Leaving a tap running while brushing wastes up to 6 liters per minute (~15 liters per brushing session). Closing the tap saves thousands of liters per person annually.",
        "solution_html": "<p><strong>Step-by-step Conservation Audit:</strong></p><p>1. <strong>Tap Flow Rate:</strong> Standard faucet flows at 6-10 L/min.</p><p>2. <strong>Savings:</strong> Turning off the tap while brushing saves ~15 L per person daily, or over 5,400 L per year per person!</p>"
    },
    {
        "id": 40,
        "question": "How can families reuse water used for washing vegetables, dal, and rice in the kitchen?",
        "options": [
            "Pour it onto garden plants and potted flowers instead of letting it go down the drain",
            "Boil it into tea for house guests",
            "Store it inside car batteries",
            "Freeze it into ice cubes for cold drinks"
        ],
        "answer": 0,
        "explanation": "Kitchen rinse water from grains and vegetables contains beneficial trace nutrients and zero toxic chemicals, making it ideal for irrigating potted garden plants.",
        "solution_html": "<p><strong>Step-by-step Greywater Reuse:</strong></p><p>1. <strong>Nutrient-Rich Rinse:</strong> Starch and micronutrients in rice/vegetable wash water naturally nourish soil microbes.</p><p>2. <strong>Conservation Impact:</strong> Replaces fresh municipal tap water for garden irrigation, reducing household water consumption.</p>"
    }
]

