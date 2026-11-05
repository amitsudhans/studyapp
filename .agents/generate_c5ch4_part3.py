"""
Data generator for NCERT Class 5 Science Chapter 4: Our School - A Happy Place - Part 3 (40 Mastery Challenge Questions)
Questions 1 to 40 distributed across slides 17 to 20 (10 questions per slide).
Zero raw LaTeX. Pure clean Unicode.
"""

QUIZ_QUESTIONS = [
    # Slide 17: Challenge 1 (Q1 to Q10) - Green Campus, Explorer Teams & Waste Management
    {
        "id": 1,
        "question": "What is the primary defining characteristic of an eco-friendly 'green school'?",
        "options": [
            "Painting every classroom wall and bench dark green",
            "A campus that actively manages waste, conserves water, uses electricity responsibly, and nurtures trees",
            "Replacing all printed textbooks with artificial plastic models",
            "Locking all gates so students cannot enter the playground"
        ],
        "answer": 1,
        "explanation": "A green school practices holistic environmental stewardship by minimizing waste, conserving water and energy, and cultivating native biodiversity.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Core Concept of a Green School:</strong></p>
                <p>A green school transforms the campus into a living environmental laboratory. It engages students and staff in sustainable daily habits: segregating waste, composting wet scraps, harvesting rainwater, harvesting natural daylight, and planting shade trees.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B is the correct definition.</p>
            </div>
        """
    },
    {
        "id": 2,
        "question": "Which student explorer team is responsible for inspecting classroom dustbins and ensuring proper waste segregation?",
        "options": [
            "Traffic Trackers",
            "Waste Warriors",
            "Electricity Savers",
            "Water Watchers"
        ],
        "answer": 1,
        "explanation": "The Waste Warriors team audits waste generation, checks that dry and wet waste are separated into proper bins, and monitors composting pits.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Team Functional Specialization:</strong></p>
                <ul class="list-disc pl-4 space-y-1">
                    <li><strong>Waste Warriors:</strong> Litter auditing, bin checks, and compost monitoring.</li>
                    <li><strong>Water Watchers:</strong> Detecting leaks and monitoring water tanks.</li>
                    <li><strong>Electricity Savers:</strong> Turning off idle fans and lights.</li>
                    <li><strong>Green Guardians:</strong> Caring for trees, gardens, and visiting pollinators.</li>
                </ul>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B is the Waste Warriors.</p>
            </div>
        """
    },
    {
        "id": 3,
        "question": "In the waste hierarchy known as the '3Rs', which action is considered the most effective first step for environmental protection?",
        "options": [
            "Recycling all materials repeatedly forever",
            "Reducing waste generation at the source by avoiding unnecessary consumption",
            "Burying mixed waste in deep city landfills",
            "Burning waste piles in open playgrounds"
        ],
        "answer": 1,
        "explanation": "Reducing waste at the source prevents waste from being created in the first place, saving raw materials, water, and industrial processing energy.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>The 3Rs Hierarchy:</strong></p>
                <p>The 3Rs are prioritized in order of ecological efficiency: <strong>Reduce > Reuse > Recycle</strong>. Reducing is paramount because preventing waste generation avoids extraction of raw resources, manufacturing pollution, and transport emissions altogether.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B is the top priority.</p>
            </div>
        """
    },
    {
        "id": 4,
        "question": "Why is 'source segregation' (separating wet and dry waste at the classroom bin) essential for successful waste management?",
        "options": [
            "To make the classroom look like a colorful art exhibition",
            "Wet organic scraps soil dry paper and plastic, rendering recyclable materials contaminated and unrecyclable",
            "Wet waste turns all metal cans into combustible gas",
            "Dry waste cannot be touched by air currents"
        ],
        "answer": 1,
        "explanation": "Mixing wet food with dry recyclables contaminates paper and cardboard with moisture and oils, causing foul odors and making mechanical recycling impossible.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Principles of Source Segregation:</strong></p>
                <p>When waste is mixed, clean dry paper absorbs moisture and grease from food scraps, jamming paper recycling pulpers. Separating waste at source allows wet waste to become rich compost and dry materials to enter recycling factories cleanly.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B explains the necessity of source separation.</p>
            </div>
        """
    },
    {
        "id": 5,
        "question": "Which of the following discarded lunch items belongs strictly in the green bin for wet organic waste?",
        "options": [
            "Plastic juice pouch straws",
            "Banana peels, orange skins, and apple cores",
            "Torn aluminum tiffin wrapping foil",
            "Used dry ballpoint pen plastic bodies"
        ],
        "answer": 1,
        "explanation": "Fruit peels and vegetable scraps are biodegradable organic waste that naturally decompose into rich compost when placed in the green bin.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Green Bin Classification:</strong></p>
                <p>The green bin is universally reserved for biodegradable organic matter: food leftovers, fruit skins, vegetable peels, tea leaves, and garden leaves. Microorganisms break these down aerobically into nutrient-rich humus (compost).</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B belongs in the green bin.</p>
            </div>
        """
    },
    {
        "id": 6,
        "question": "Which items belong in the blue bin designated for dry, recyclable non-biodegradable waste?",
        "options": [
            "Leftover sambar and boiled rice",
            "Used exam question papers, cardboard cartons, clean plastic wrappers, and metal tins",
            "Wet tea leaves and banana skins",
            "Rotten tomatoes and watermelon rinds"
        ],
        "answer": 1,
        "explanation": "The blue bin collects clean, dry non-biodegradable items: scrap paper, cardboard, plastics, glass, and metal, which are sorted and recycled.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Blue Bin Classification:</strong></p>
                <p>Blue bins collect clean recyclable dry discards: stationery papers, worksheets, cardboard packaging, clean plastic wrappers, and tins. These materials are forwarded to scrap recyclers for industrial reprocessing.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B belongs in the blue bin.</p>
            </div>
        """
    },
    {
        "id": 7,
        "question": "What is meant by the ethical principle of the 'Dignity of Labour' in school life?",
        "options": [
            "Believing that only office workers do valuable work",
            "Respecting, appreciating, and valuing all forms of honest work equally, including sanitation workers and scrap recyclers",
            "Forbidding students from ever cleaning their own desks",
            "Assigning cleaning duties only as a punishment"
        ],
        "answer": 1,
        "explanation": "Dignity of labour recognizes that all honest work contributes to society. Sanitation staff and recyclers protect public health and deserve our deepest respect and gratitude.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Dignity of Labour:</strong></p>
                <p>This core ethical value teaches that no honest occupation is inferior. Sanitation workers and recyclers perform vital community health duties by preventing disease outbreaks and conserving natural resources. We honor them through polite respect and cleaning up after ourselves.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B defines dignity of labour.</p>
            </div>
        """
    },
    {
        "id": 8,
        "question": "How many mature trees are conserved on average by recycling one single metric ton of discarded school paper?",
        "options": [
            "Zero trees",
            "Approximately 17 mature trees and thousands of liters of water",
            "Exactly 1,000,000 trees",
            "Half a small blade of grass"
        ],
        "answer": 1,
        "explanation": "Recycling one ton of scrap paper saves roughly 17 mature forest trees, 26,000 liters of water, and significant industrial electricity.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Ecological Math of Paper Recycling:</strong></p>
                <p>Virgin paper manufacturing requires felling trees and boiling wood pulp with heavy water and chemicals. Recycling one ton of collected classroom paper spares 17 mature trees from deforestation and prevents water pollution.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B is the proven environmental saving.</p>
            </div>
        """
    },
    {
        "id": 9,
        "question": "What harmful environmental consequence occurs when mixed wet food waste is dumped into municipal landfills instead of being composted?",
        "options": [
            "It turns into pure solid gold underground",
            "It rots in airless conditions, producing methane—a potent greenhouse gas that drives global climate change",
            "It converts all landfill soil into drinking water",
            "It cools down the entire Earth's atmosphere permanently"
        ],
        "answer": 1,
        "explanation": "Deep in landfills, anaerobic bacteria decompose buried food without oxygen, generating methane gas, which traps 28 times more atmospheric heat than carbon dioxide.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Anaerobic Landfill Emissions:</strong></p>
                <p>When food scraps are buried under mixed trash, oxygen is absent. Anaerobic methanogenic bacteria break down the food, releasing methane ($CH_4$). Aerobic composting in schools allows oxygen flow, turning waste into harmless organic fertilizer instead.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B explains the danger of landfilling food scraps.</p>
            </div>
        """
    },
    {
        "id": 10,
        "question": "Which classroom habit best demonstrates personal responsibility and civility regarding waste?",
        "options": [
            "Throwing pencil shavings under your friend's desk when the teacher is looking away",
            "Collecting your own pencil shavings and snack wrappers, and placing them neatly in designated bins",
            "Leaving crushed tiffin foil on the floor for cleaning staff to pick up",
            "Shoving plastic wrappers into the gaps between desk planks"
        ],
        "answer": 1,
        "explanation": "Personal responsibility means cleaning up after yourself, depositing trash in the correct bin, and maintaining shared classroom spaces cleanly.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Personal Stewardship:</strong></p>
                <p>A green campus begins with personal discipline. Discarding personal pencil shavings and snack wrappers into the correct dustbin shows respect for classmates and campus housekeeping workers.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B is the responsible habit.</p>
            </div>
        """
    },

    # Slide 18: Challenge 2 (Q11 to Q20) - Natural Cooling, Water Leaks & Canopies
    {
        "id": 11,
        "question": "What are the three fundamental principles of passive natural cooling used in eco-friendly school building architecture?",
        "options": [
            "Electric air conditioners, closed glass windows, and black tar roofs",
            "Tree canopy shade, cross-ventilation through opposing windows, and reflective white cool roofs",
            "Underground heaters, plastic curtains, and neon lights",
            "Sealed doors, diesel fans, and asphalt courtyards"
        ],
        "answer": 1,
        "explanation": "Passive architecture relies on natural physics: tree shade blocks solar heat, cross-ventilation creates convective air currents, and white roofs reflect radiant light.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Passive Thermal Architecture:</strong></p>
                <p>Passive cooling maintains comfortable indoor temperatures without high electricity consumption by combining three scientific methods: vegetative shading, cross-ventilation breezes, and high-albedo reflective roof coatings.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B correctly lists the three principles.</p>
            </div>
        """
    },
    {
        "id": 12,
        "question": "Why does a rooftop coated with reflective white lime or solar paint keep classrooms 3°C to 5°C cooler than a dark black tar roof?",
        "options": [
            "White surfaces attract cold polar winds from the sky",
            "White surfaces possess high solar reflectance (albedo), reflecting incoming sunlight instead of absorbing thermal radiation",
            "White paint turns concrete into solid ice",
            "Black surfaces repel all forms of light"
        ],
        "answer": 1,
        "explanation": "White surfaces have high albedo, bouncing back up to 80-85% of solar energy. Dark surfaces absorb solar wavelengths, conducting heat into ceilings.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Solar Albedo & Heat Absorption:</strong></p>
                <p>Albedo is the fraction of solar radiation reflected by a surface. Dark roofs have low albedo, absorbing solar photons and heating up to 65°C. White roofs have high albedo, reflecting sunlight away and keeping roof slabs close to ambient air temperature.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B is the physical explanation.</p>
            </div>
        """
    },
    {
        "id": 13,
        "question": "How does cross-ventilation create a refreshing breeze inside a classroom on a warm afternoon?",
        "options": [
            "It freezes the air molecules into solid blocks",
            "Opening windows on opposite walls allows outdoor wind pressure to push out hot, stagnant air and replace it with cooler moving air",
            "It turns classroom oxygen into liquid nitrogen",
            "It permanently seals all doors so air cannot escape"
        ],
        "answer": 1,
        "explanation": "Cross-ventilation uses wind pressure differentials across opposite exterior walls to draw in fresh outdoor air while venting warm indoor air.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Fluid Dynamics of Cross-Ventilation:</strong></p>
                <p>Wind striking one side of a building creates positive pressure, while the opposite sheltered side experiences negative suction. Opening windows on both sides creates a continuous draft that flushes out heat and carbon dioxide.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B describes cross-ventilation dynamics.</p>
            </div>
        """
    },
    {
        "id": 14,
        "question": "How much clean drinking water is lost each day from a single school washroom tap that drips at the rate of one drop per second?",
        "options": [
            "Less than 50 milliliters",
            "Over 30 liters per day (more than 10,000 liters per year)",
            "Exactly 500,000 liters",
            "Zero, because dripping water is destroyed by air"
        ],
        "answer": 1,
        "explanation": "At 1 drop per second, 86,400 drops fall every 24 hours, adding up to over 30 liters daily and exceeding 10,000 liters annually from a single tap.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>The Quantitative Math of Water Loss:</strong></p>
                <p>A single water drop measures approximately 0.05 mL. At 1 drop per second: 60 drops/min × 60 min × 24 hr = 86,400 drops/day = 4.3 liters every 4 hours, totaling over 30 liters daily. Over 365 days, this exceeds 10,000 liters!</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B is the correct calculation.</p>
            </div>
        """
    },
    {
        "id": 15,
        "question": "What is the most frequent mechanical cause of a dripping tap that will not shut off tightly?",
        "options": [
            "The tap pipe is made of solid copper",
            "A worn, cracked, or hardened internal rubber washer (gasket) that fails to seal the valve seat",
            "The water inside the pipe is too cold to flow",
            "The metal handle is painted blue"
        ],
        "answer": 1,
        "explanation": "Water taps rely on a flexible rubber washer to press against a metal seat. Over time, friction and mineral deposits degrade the washer, allowing water to seep past.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Plumbing Mechanics:</strong></p>
                <p>Inside a compression tap, turning the spindle presses a rubber washer against the valve seat. When this washer wears out, cracks, or hardens, it leaves microscopic gaps through which pressurized water continuously drips.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B is the mechanical cause.</p>
            </div>
        """
    },
    {
        "id": 16,
        "question": "What key national water conservation objective is promoted under community programs like the Jal Shakti Abhiyan?",
        "options": [
            "Paving entire school playgrounds with impervious concrete slabs",
            "Rooftop rainwater harvesting, recharging groundwater aquifers, repairing leaks, and planting trees",
            "Emptying clean lake water into city gutters",
            "Stopping all drinking water supplies to schools"
        ],
        "answer": 1,
        "explanation": "Jal Shakti Abhiyan is a nationwide water conservation campaign focused on rainwater harvesting, watershed management, groundwater recharge, and intensive afforestation.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Jal Shakti Abhiyan Mandate:</strong></p>
                <p>Launched by the Government of India, this mission rallies schools, panchayats, and citizens to capture monsoon rainwater, fix leaky infrastructure, restore traditional water bodies, and plant trees to secure water for future generations.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B states the mission goals.</p>
            </div>
        """
    },
    {
        "id": 17,
        "question": "Through which biological process do mature leafy trees actively lower the surrounding air temperature on a hot afternoon?",
        "options": [
            "Photosynthetic combustion",
            "Transpiration—evaporating water from leaf pores (stomata) which absorbs heat from the air",
            "Releasing liquid ice through trunk roots",
            "Absorbing all atmospheric nitrogen"
        ],
        "answer": 1,
        "explanation": "Transpiration is the evaporative cooling engine of trees. Water evaporating through leaf stomata absorbs ambient heat, acting like a natural air conditioner.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Foliar Transpiration Cooling:</strong></p>
                <p>Tree roots pump water from soil up to the leaves. Solar warmth evaporates this water through microscopic leaf stomata. The latent heat of vaporization absorbs thermal energy from surrounding air, lowering the microclimate temperature by 3°C to 8°C.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B is the biological mechanism.</p>
            </div>
        """
    },
    {
        "id": 18,
        "question": "Why did the Green Guardians measure a 9°C temperature difference between the open basketball court and beneath a neem tree?",
        "options": [
            "The basketball court was on fire",
            "Asphalt absorbs and re-radiates intense solar heat, while the tree canopy blocks sunlight and cools the air through transpiration",
            "The neem tree releases artificial liquid nitrogen",
            "The thermometer was broken on the court"
        ],
        "answer": 1,
        "explanation": "Dark pavement absorbs solar energy and radiates it as heat (urban heat island effect), whereas tree leaves block direct rays and transpire cool water vapor.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Microclimate Comparison:</strong></p>
                <p>Asphalt and concrete surfaces have high thermal mass, soaking in solar radiation and reaching temperatures over 45°C. Tree canopies intercept sunlight before it hits the ground, and leaf transpiration actively removes heat.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B accurately explains the difference.</p>
            </div>
        """
    },
    {
        "id": 19,
        "question": "Which of the following indigenous Indian trees is celebrated for purifying air, providing dense shade, and supporting diverse native wildlife?",
        "options": [
            "Artificial plastic palm trees",
            "Neem, Peepal, Banyan, and Jamun trees",
            "Thorny desert cactus in closed pots",
            "Ornamental plastic ivy vines"
        ],
        "answer": 1,
        "explanation": "Native keystone species like neem, peepal, and banyan thrive in Indian climates, providing large shade canopies, filtering air, and feeding indigenous birds and insects.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Ecological Value of Native Trees:</strong></p>
                <p>Indigenous Indian trees co-evolved with local fauna. Neem has antimicrobial properties and dense leaves; banyan and peepal produce figs that sustain barbets, parakeets, and fruit bats; jamun provides sweet summer berries and butterfly host foliage.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B is the correct group of native trees.</p>
            </div>
        """
    },
    {
        "id": 20,
        "question": "How do leafy tree canopies on school perimeters help clean the air that students breathe?",
        "options": [
            "By vaporizing air molecules into thin dust",
            "Rough, hairy leaf surfaces trap airborne dust, soot, and fine particulate matter, washing it harmlessly into the soil during rain",
            "By producing carbon monoxide gas",
            "By blocking all oxygen from entering the campus"
        ],
        "answer": 1,
        "explanation": "Leaves and bark act as physical air filters, trapping particulate matter (PM2.5 and PM10) from vehicle exhausts, which is later washed into soil by rain.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Particulate Matter Filtration:</strong></p>
                <p>Tree leaves have microscopic ridges, hairs, and waxy coatings that physically intercept airborne dust and soot particles from surrounding traffic. This green barrier drastically reduces air pollution in classrooms.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B describes tree particulate filtration.</p>
            </div>
        """
    },

    # Slide 19: Challenge 3 (Q21 to Q30) - Butterfly Gardens & Traffic Safety
    {
        "id": 21,
        "question": "What is the biological difference between 'nectar plants' and 'larval host plants' in a butterfly conservation garden?",
        "options": [
            "Nectar plants are painted blue while host plants are painted red",
            "Nectar plants provide sugary nectar for flying adult butterflies, while host plants provide specific foliage where mother butterflies lay eggs and caterpillars feed",
            "Nectar plants only grow in winter while host plants grow only in desert sand",
            "There is no difference between them"
        ],
        "answer": 1,
        "explanation": "Adult butterflies sip nectar from open flowers for flight energy, but female butterflies strictly deposit eggs on specific host plants whose leaves nourish caterpillars.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Butterfly Garden Botany:</strong></p>
                <p>Butterflies undergo complete metamorphosis: egg, larva (caterpillar), pupa, and adult. Adult butterflies drink nectar from many bright flowers. However, caterpillars are specialized herbivores that can only feed on specific host plants (like curry leaves or milkweed).</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B is the scientific distinction.</p>
            </div>
        """
    },
    {
        "id": 22,
        "question": "Which of the following common garden plants provides rich nectar sources for adult butterflies on a school campus?",
        "options": [
            "Plastic ferns",
            "Marigold, Zinnia, Cosmos, and Periwinkle (Sadabahar)",
            "Thorny iron fencing poles",
            "Dry gravel stones"
        ],
        "answer": 1,
        "explanation": "Marigold, zinnia, cosmos, and sadabahar have open, nectar-rich blossoms with landing platforms ideal for butterflies' delicate legs and long proboscis.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Nectar Floral Structure:</strong></p>
                <p>Butterflies prefer composite flowers with accessible nectar wells and broad petals where they can perch comfortably. Zinnias, marigolds, and cosmos flower profusely in sunny school plots, providing continuous nectar.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B correctly lists nectar plants.</p>
            </div>
        """
    },
    {
        "id": 23,
        "question": "Which plant serves as the specific larval host plant for the Common Mormon butterfly to lay its eggs and feed its caterpillars?",
        "options": [
            "Hardwood teak logs",
            "Curry leaf plant (Kadi Patta) and citrus saplings",
            "Dry wheat straw",
            "Cement concrete paving blocks"
        ],
        "answer": 1,
        "explanation": "The Common Mormon butterfly lays its round eggs on the tender leaves of curry leaf (Murraya koenigii) and citrus plants, which the hatched caterpillars eat.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Host Plant Specificity:</strong></p>
                <p>Female butterflies use chemical sensors on their feet to identify the precise botanical species. The Common Mormon and Lime Butterfly require citrus family plants (Rutaceae), including the common kitchen curry leaf plant.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B is the specific host plant.</p>
            </div>
        """
    },
    {
        "id": 24,
        "question": "Why are insect pollinators like butterflies and honeybees essential for the human food supply?",
        "options": [
            "They consume agricultural crops so people don't have to harvest them",
            "They transfer pollen between flower blossoms, enabling plants to produce fruits, vegetables, nuts, and viable seeds",
            "They frighten away birds from school playgrounds",
            "They turn garden soil into pure sand"
        ],
        "answer": 1,
        "explanation": "Pollinators transfer pollen grains from male anthers to female stigmas. Without pollination, flowering plants cannot develop fruits, vegetables, or seeds.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>The Crucial Role of Pollinators:</strong></p>
                <p>Over 75% of the world's leading food crops depend directly on insect pollination. When butterflies and bees drink nectar, pollen sticks to their bodies and is carried to other flowers, enabling plant fertilization and fruit production.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B explains the role of pollinators.</p>
            </div>
        """
    },
    {
        "id": 25,
        "question": "Why is a strict motor vehicle speed limit of 20 to 25 km/h enforced in designated school zones?",
        "options": [
            "To make school buses arrive late for classes",
            "To shorten stopping distances so drivers can brake instantly if an excited student steps onto the roadway",
            "Because vehicles cannot travel faster than 25 km/h in reverse",
            "To make car engines produce louder exhaust sounds"
        ],
        "answer": 1,
        "explanation": "Lowering vehicle speed to 20-25 km/h drastically cuts braking distance and reduces pedestrian collision impact forces, preventing severe injuries.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Physics of Vehicle Stopping Distance:</strong></p>
                <p>Stopping distance equals reaction distance plus braking distance. At 20 km/h, a car stops within 6 meters. At 50 km/h, it takes 25 meters. In school zones with unpredictable child movement, slow speeds prevent accidents.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B is the safety rationale.</p>
            </div>
        """
    },
    {
        "id": 26,
        "question": "What is the correct, safe pedestrian sequence taught to students before stepping across any road in India?",
        "options": [
            "Look straight down at your shoes and run fast",
            "Look Right, Look Left, Look Right Again, listen for vehicles, and cross only when traffic has stopped",
            "Close your eyes and hold your friend's hand tightly",
            "Look behind you and walk backward across the street"
        ],
        "answer": 1,
        "explanation": "In India's left-hand traffic system, oncoming vehicles approach from your right first. Looking Right, Left, and Right Again ensures clear vision before crossing.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Defensive Crossing Rule:</strong></p>
                <p>Because traffic drives on the left in India, the lane closest to you carries vehicles from your right. Looking Right first checks immediate danger; looking Left checks the second lane; looking Right once more ensures no vehicle has turned in.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B is the life-saving rule.</p>
            </div>
        """
    },
    {
        "id": 27,
        "question": "Which geometric shape and color code signify 'Mandatory / Regulatory' traffic signs that drivers MUST obey by law?",
        "options": [
            "Blue rectangles with white lettering",
            "Circular signs with bold red borders (such as Stop, No Entry, Speed Limit)",
            "Yellow triangles pointing downward",
            "Green octagons with pink stripes"
        ],
        "answer": 1,
        "explanation": "Circular signs with red borders are mandatory regulatory signs. Violating them is a direct breach of traffic law.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Mandatory Road Signs:</strong></p>
                <p>Mandatory traffic signs issue direct legal commands. They are circular with a red ring border (like 'No Parking' or 'Speed Limit 20'). The iconic 'STOP' sign is uniquely octagonal, and 'GIVE WAY' is an inverted triangle.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B is the mandatory sign format.</p>
            </div>
        """
    },
    {
        "id": 28,
        "question": "What does a triangular traffic sign with a red border depicting silhouettes of two school children walking signify to drivers?",
        "options": [
            "Children are forbidden from walking on the footpath",
            "Cautionary warning: 'School Ahead'—drivers must slow down and watch out for crossing children",
            "A toy store is open 24 hours ahead",
            "The road is reserved only for school buses"
        ],
        "answer": 1,
        "explanation": "Triangular signs are cautionary. The 'School Ahead' sign alerts motorists to reduce speed and remain vigilant for young pedestrians.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Cautionary Traffic Signs:</strong></p>
                <p>Warning signs are equilateral triangles pointing up with red borders. The 'School Ahead' sign warns drivers that children are likely to be crossing, requiring immediate deceleration and alert driving.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B is the correct meaning.</p>
            </div>
        """
    },
    {
        "id": 29,
        "question": "What is the purpose of rectangular traffic signs with blue backgrounds located near school campuses?",
        "options": [
            "They are decorative advertisements for sports brands",
            "Informatory signs providing directions and useful facilities (such as Hospital, Bus Stop, or Pedestrian Crossing)",
            "They indicate that the road is underwater",
            "They command drivers to accelerate immediately"
        ],
        "answer": 1,
        "explanation": "Rectangular blue signs are informatory, providing helpful navigation, facility locations, and public service information to commuters.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Informatory Road Signs:</strong></p>
                <p>Informatory signs guide road users without giving legal orders or warnings. They feature blue rectangles with white symbols indicating hospitals, public transit stops, parking zones, and first aid stations.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B defines informatory signs.</p>
            </div>
        """
    },
    {
        "id": 30,
        "question": "What is the legal rule regarding painted zebra crossings marked across roads outside school gates?",
        "options": [
            "Vehicles should speed up to pass pedestrians before they step onto the road",
            "Pedestrians have absolute right-of-way; drivers must slow down and stop before the line when pedestrians are crossing",
            "Zebra crossings are parking spots for school delivery trucks",
            "Only zebras from the zoo are permitted to cross on the stripes"
        ],
        "answer": 1,
        "explanation": "Zebra crossings give pedestrians right-of-way. Motorists must yield and come to a complete halt before the stop line to let pedestrians cross safely.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Zebra Crossing Pedestrian Priority:</strong></p>
                <p>Painted alternating white and black stripes designate pedestrian crosswalks. Traffic laws mandate that vehicles must yield right-of-way to pedestrians on or entering a zebra crossing, coming to a complete stop.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B is the legal rule.</p>
            </div>
        """
    },

    # Slide 20: Challenge 4 (Q31 to Q40) - Fire Safety, Accessibility & Civic Empathy
    {
        "id": 31,
        "question": "What is the critical personal conduct rule when a school fire alarm rings loudly during class?",
        "options": [
            "Sprint as fast as you can, shouting and pushing past everyone on the stairs",
            "Stay calm, do not panic, leave school bags behind, and walk quickly in a single-file line toward the exit",
            "Lock the classroom door and hide underneath wooden benches",
            "Search for lost stationery in your backpack"
        ],
        "answer": 1,
        "explanation": "Panic and running cause stampedes and injuries. Walking briskly and calmly in a single file ensures a fast, safe, orderly evacuation.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Orderly Evacuation vs Stampede:</strong></p>
                <p>In fire emergencies, human stampedes and falling down staircases often cause more physical harm than the fire itself. Leaving heavy bags behind and walking calmly in single file ensures everyone gets out safely.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B is the correct emergency conduct.</p>
            </div>
        """
    },
    {
        "id": 32,
        "question": "Why do hot smoke, poisonous gases, and black soot rise rapidly toward the ceiling during a building fire?",
        "options": [
            "Because smoke is attracted to ceiling lights by magnetism",
            "Thermal convection: hot air and combustion gases are less dense than cooler room air, making them buoyant and rise",
            "Because gravity reverses its direction during fires",
            "Smoke only moves toward dark ceiling corners"
        ],
        "answer": 1,
        "explanation": "Hot air and combustion gases expand and become less dense than surrounding air, causing thermal convection currents that push smoke up against the ceiling.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Thermal Convection Physics:</strong></p>
                <p>Heated gases expand, decreasing in density ($\rho = m/V$). The cooler, denser air pushes the superheated smoke upward. Consequently, the hottest and most toxic fumes accumulate in a thick layer starting at the ceiling and slowly descending.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B explains why smoke rises.</p>
            </div>
        """
    },
    {
        "id": 33,
        "question": "What is the life-saving 'Crawl Low under Smoke' technique used when escaping a smoke-filled hallway?",
        "options": [
            "Standing on tiptoes and jumping through the smoke",
            "Dropping onto hands and knees where the coolest, cleanest, breathable air remains 30 to 60 cm above the floor",
            "Rolling backward down staircases",
            "Lying completely still and closing eyes"
        ],
        "answer": 1,
        "explanation": "The cleanest air with the highest oxygen and lowest temperature stays in a 30 to 60 cm layer near the floor. Crawling low avoids inhaling lethal toxic smoke.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>The Mechanics of Crawling Low:</strong></p>
                <p>Dropping to hands and knees keeps your nose and mouth in the lowest, coolest air zone. Covering your face with a cloth helps filter soot particles. Keeping your head in the bottom 30-60 cm allows you to see exit signs and breathe safely.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B is the life-saving method.</p>
            </div>
        """
    },
    {
        "id": 34,
        "question": "Why is it strictly forbidden to hide inside cupboards, closets, or washrooms during a building fire?",
        "options": [
            "Closets are reserved only for teachers' coats",
            "Hiding traps you in dead-end confined spaces without escape exits, making it extremely difficult for rescue firefighters to find you in thick smoke",
            "Washrooms have no water taps",
            "Cupboards make fire alarms ring louder"
        ],
        "answer": 1,
        "explanation": "Hiding traps students in confined areas with no secondary escape. Firefighters searching rapidly through smoke-filled rooms may miss closed closets.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>The Danger of Hiding in Emergencies:</strong></p>
                <p>Young children often hide out of fear. But closed closets and bathrooms quickly fill with toxic smoke through vents, trapping occupants. Always move toward emergency exits, and never hide.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B explains why hiding is dangerous.</p>
            </div>
        """
    },
    {
        "id": 35,
        "question": "What essential procedure must take place immediately after reaching the open assembly point during a school fire drill?",
        "options": [
            "Students run home without telling anyone",
            "Students assemble in their designated class lines so teachers can take attendance and account for every child",
            "Students start playing cricket immediately",
            "Students run back inside to inspect the flames"
        ],
        "answer": 1,
        "explanation": "Roll call at the muster point ensures that every student is accounted for. If a student is missing, teachers can immediately alert emergency firefighters.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Assembly Point Roll Call:</strong></p>
                <p>Reaching the assembly point is not the end of the drill. Standing quietly in class lines allows teachers to take attendance. If anyone is unaccounted for, emergency rescue teams are dispatched immediately to the exact missing location.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B is the vital roll call step.</p>
            </div>
        """
    },
    {
        "id": 36,
        "question": "Why is scribbling graffiti or carving marks into wooden school desks and library books considered harmful and unacceptable?",
        "options": [
            "It turns the desks into pure stone",
            "Desks and books are shared community property; defacing them damages school heritage and deprives future students of clean resources",
            "Permanent ink dissolves wood into water",
            "Desks will stop holding notebooks"
        ],
        "answer": 1,
        "explanation": "School furniture and library books are shared public goods. Protecting them preserves resources and shows respect for the learning community.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Public Property Stewardship:</strong></p>
                <p>Civic responsibility means treating shared school facilities with the same care as personal belongings at home. Preserving clean desks and books ensures that younger students entering the school next year inherit a beautiful, welcoming campus.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B is the civic principle.</p>
            </div>
        """
    },
    {
        "id": 37,
        "question": "How does showing empathy and kindness transform a school into a truly happy place?",
        "options": [
            "It eliminates all homework permanently",
            "It makes every student feel valued, included, and emotionally safe, eliminating fear and bullying",
            "It turns classroom lights off forever",
            "It makes students stop talking to each other"
        ],
        "answer": 1,
        "explanation": "Empathy fosters mutual respect, trust, and emotional safety, creating a supportive environment where children can thrive and learn without fear.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Social-Emotional Climate:</strong></p>
                <p>When students practice empathy—listening, taking turns, welcoming lonely classmates, and offering help—the school becomes a community of trust. Emotional safety is the foundation of high academic engagement and joy.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B is the transformative power of empathy.</p>
            </div>
        """
    },
    {
        "id": 38,
        "question": "What is the recommended gentle slope (gradient) for wheelchair entrance ramps in accessible schools?",
        "options": [
            "A vertical 90° drop like a ladder",
            "A gentle slope of at least 1:12 (1 unit rise for every 12 units of ramp length) equipped with continuous handrails",
            "A steep 1:2 ramp so wheelchairs slide down fast",
            "Zero ramp, stairs are sufficient for all wheels"
        ],
        "answer": 1,
        "explanation": "A 1:12 slope ensures that wheelchair users can wheel themselves up safely without excessive effort, loss of balance, or tipping backward.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Universal Ramp Design:</strong></p>
                <p>Accessibility standards mandate a slope no steeper than 1:12 (approx. 4.8° angle), along with non-slip flooring, double handrails at two heights, and a level landing platform at the top and bottom.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B is the accessibility standard.</p>
            </div>
        """
    },
    {
        "id": 39,
        "question": "What is the tactile difference between straight directional lines and raised round dots on yellow guiding floor tiles?",
        "options": [
            "Lines mean stop, while dots mean run",
            "Straight raised lines indicate a safe, clear walking path, while raised round dots warn of hazards, doors, turns, or approaching stairs",
            "Dots are for playing games, while lines are for parking bicycles",
            "There is no difference between them"
        ],
        "answer": 1,
        "explanation": "In tactile ground surface indicators, directional linear bars guide along paths, while hazard blister dots signal attention, turns, or staircases.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>Tactile Paving Standards:</strong></p>
                <p>Visually impaired individuals feel these floor textures through walking canes or footwear. Linear 'guiding tiles' show safe corridors; truncated 'blister tiles' warn that stairs, platforms, or intersections lie immediately ahead.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B describes the tactile code.</p>
            </div>
        """
    },
    {
        "id": 40,
        "question": "What is the lasting purpose of creating a campus 'Happiness Tree' bulletin display?",
        "options": [
            "To sell paper leaves to visitors for money",
            "To visually celebrate student acts of kindness, environmental stewardship, and gratitude, inspiring a caring school culture",
            "To replace living garden trees with cardboard",
            "To list disciplinary warnings for students"
        ],
        "answer": 1,
        "explanation": "The Happiness Tree serves as an ongoing visual testament to kindness, sustainable eco-actions, and mutual gratitude, reinforcing a supportive community.",
        "solution_html": """
            <div class="space-y-2 text-xs">
                <p><strong>The Happiness Tree Celebration:</strong></p>
                <p>By writing and pinning leaves representing kind acts, water savings, tree planting, and thank-you notes to staff, students build a shared identity of empathy, ecological responsibility, and pride in their school.</p>
                <p class="text-cyan-300"><strong>Conclusion:</strong> Option B is the purpose of the Happiness Tree.</p>
            </div>
        """
    }
]

