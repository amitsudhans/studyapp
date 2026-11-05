"""
Part 3 of NCERT Class 5 Science Chapter 9: Rhythms of Nature
Mastery Challenge Quiz Questions 1 to 40 (Slides 17 to 20)
10 Questions per Challenge Slide with instant feedback, explanation, and solution_html.
Zero Raw LaTeX! Pure clean Unicode symbols.
"""

import sys

QUIZ_QUESTIONS = [
    # =========================================================================
    # Challenge 1 (Q1 to Q10): Nature's Clock, Day & Night, Earth's Spin, Seasons' Journal
    # =========================================================================
    {
        "id": 1,
        "question": "Which of the following events represents a change that takes place over a time scale of seconds rather than days or years?",
        "options": [
            "Blinking your eyes or catching a dropped cricket ball",
            "A mango sapling growing into a mature tree",
            "A baby tooth falling out and being replaced by a permanent tooth",
            "A caterpillar transforming inside a cocoon into a silk moth"
        ],
        "answer": 0,
        "explanation": "Blinking and catching objects happen in fractions of a second, whereas biological growth and metamorphosis require days, months, or years.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Time Scales of Change:</strong></p>
                <p class='text-slate-300'>Nature operates across multiple orders of temporal magnitude: instantaneous reflex actions (seconds), daily astronomical rotations (hours), and organismal growth (months to years).</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Blinking your eyes or catching a dropped cricket ball)</p>
            </div>
        """
    },
    {
        "id": 2,
        "question": "What primary astronomical motion causes day to turn into night and night to turn into day on Earth?",
        "options": [
            "The Earth rotating on its internal axis once every 24 hours",
            "The Sun traveling in an orbit around the Earth every 12 hours",
            "The Moon blocking the Sun's light every single evening",
            "Giant storm clouds covering the sky every night"
        ],
        "answer": 0,
        "explanation": "Day and night are caused by the Earth rotating on its axis once every 24 hours relative to the stationary Sun.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Mechanics of Day and Night:</strong></p>
                <p class='text-slate-300'>The Sun remains fixed at the center of the solar system. As the spherical Earth spins eastward, half of the planet is exposed to solar rays (daytime) while the other half rests in planetary shadow (nighttime).</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (The Earth rotating on its internal axis once every 24 hours)</p>
            </div>
        """
    },
    {
        "id": 3,
        "question": "In classroom Activity 1, a torch shines light onto a globe in a darkened room. What does the illuminated half of the globe represent?",
        "options": [
            "The hemisphere experiencing daytime",
            "The hemisphere experiencing midnight",
            "A lunar eclipse",
            "The South Pole during a winter blizzard"
        ],
        "answer": 0,
        "explanation": "Light from the torch illuminates exactly one half of the globe at a time, modeling daytime on that portion of Earth.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Illumination Geometry:</strong></p>
                <p class='text-slate-300'>The torch simulates the Sun. The lit side represents the hemisphere experiencing daylight, while the dark side represents the nocturnal hemisphere in shadow.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (The hemisphere experiencing daytime)</p>
            </div>
        """
    },
    {
        "id": 4,
        "question": "Why does the Sun appear to rise in the eastern horizon and set in the western horizon every day?",
        "options": [
            "Because the Earth rotates from west to east beneath our feet",
            "Because the Sun physically races across space from east to west",
            "Because the North Pole is tilting upside down every hour",
            "Because ocean waves push the Sun across the sky"
        ],
        "answer": 0,
        "explanation": "Earth's counter-clockwise rotation from west to east creates the visual illusion that celestial objects travel from east to west.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Apparent vs Real Motion:</strong></p>
                <p class='text-slate-300'>Just as sitting in an eastward-moving train makes external telephone poles appear to rush westward, Earth's eastward spin creates the apparent westward trajectory of the Sun.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Because the Earth rotates from west to east)</p>
            </div>
        """
    },
    {
        "id": 5,
        "question": "What is the imaginary line connecting the North Pole and South Pole, around which Earth spins, called?",
        "options": [
            "The Equator",
            "The Axis of rotation",
            "The Tropic of Cancer",
            "The Prime Meridian"
        ],
        "answer": 1,
        "explanation": "Earth's axis of rotation is the imaginary central pivot line connecting the geographic North and South Poles.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Planetary Axis:</strong></p>
                <p class='text-slate-300'>The rotational axis is tilted at approximately 23.5 degrees relative to its orbital plane, governing both diurnal spin (24-hour day) and seasonal variations during annual revolution.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (The Axis of rotation)</p>
            </div>
        """
    },
    {
        "id": 6,
        "question": "How long does the Earth take to complete one full 360-degree rotation on its axis?",
        "options": [
            "24 hours (1 full day)",
            "365 days (1 full year)",
            "30 days (1 full month)",
            "60 minutes (1 hour)"
        ],
        "answer": 0,
        "explanation": "One full rotation of Earth on its axis takes 24 hours, defining the standard solar day.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Duration of Rotation:</strong></p>
                <p class='text-slate-300'>A complete axial rotation takes approximately 23 hours, 56 minutes, and 4 seconds (sidereal day), harmonized to 24 hours as a solar day due to Earth's concurrent orbital travel.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (24 hours (1 full day))</p>
            </div>
        """
    },
    {
        "id": 7,
        "question": "In a classroom Seasons' Journal chart, into how many quarterly time-periods is the calendar year organized?",
        "options": [
            "Four quarters (April–June, July–September, October–December, January–March)",
            "Twelve separate daily periods",
            "Just two periods (Day and Night)",
            "One hundred weekly sections"
        ],
        "answer": 0,
        "explanation": "The annual journal divides the 12 calendar months into 4 quarterly three-month blocks to observe seasonal shifts.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Quarterly Environmental Mapping:</strong></p>
                <p class='text-slate-300'>Dividing the year into four 3-month blocks (Q1: Summer, Q2: Monsoon, Q3: Autumn/Pre-winter, Q4: Winter/Spring) allows students to track environmental trends across quarters.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Four quarters)</p>
            </div>
        """
    },
    {
        "id": 8,
        "question": "Which of these is NOT one of the five core environmental themes tracked in the classroom Seasons' Journal?",
        "options": [
            "Plant life and vegetation changes",
            "Birds and animal behaviors",
            "Air temperature and wind patterns",
            "The price of plastic toys in shopping malls"
        ],
        "answer": 3,
        "explanation": "The 5 core ecological themes are: Plant life, Birds & Animals, Air/Wind, Heat/Light, and Water bodies & Human activities.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>The Five Core Ecological Themes:</strong></p>
                <p class='text-slate-300'>1. Flora (Plant life)<br>2. Fauna (Birds and animals)<br>3. Atmosphere (Air and wind)<br>4. Insolation (Heat and light)<br>5. Hydrosphere & Anthroposphere (Water bodies and human routines).</p>
                <p class='text-emerald-400 font-bold'>Correct Option: D (The price of plastic toys in shopping malls)</p>
            </div>
        """
    },
    {
        "id": 9,
        "question": "What happens to the shadow of a stationary tree or flagpole between sunrise, midday, and sunset?",
        "options": [
            "It is long in the morning, shortest at solar noon, and stretches long again in the late afternoon",
            "It remains exactly the same size all day long",
            "It vanishes completely at 9:00 AM and never returns",
            "It turns bright purple in the afternoon"
        ],
        "answer": 0,
        "explanation": "Low-angle sunlight at sunrise and sunset casts long shadows, whereas high overhead sunlight at midday casts the shortest shadow.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Solar Altitude & Shadow Length:</strong></p>
                <p class='text-slate-300'>Shadow length is inversely related to the Sun's elevation angle. When the Sun is low on the horizon (morning/evening), light strikes at a shallow angle, creating extended shadows. At solar noon, high elevation creates minimal shadow length.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Long in the morning, shortest at solar noon, and long again in late afternoon)</p>
            </div>
        """
    },
    {
        "id": 10,
        "question": "If students observe that a banyan tree's shadow points toward the west, what time of day is it?",
        "options": [
            "Morning, because the Sun is in the east, casting the shadow toward the west",
            "Late evening sunset",
            "Exact midnight",
            "Noon when the sun is overhead"
        ],
        "answer": 0,
        "explanation": "Shadows fall directly opposite the light source. With the Sun rising in the east, shadows are cast toward the west.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Opposing Shadow Physics:</strong></p>
                <p class='text-slate-300'>Light travels in straight lines. An opaque object obstructs light rays, casting a dark umbra in the direction opposite to the illumination source (Sun in East ➔ Shadow in West).</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Morning, because the Sun is in the east)</p>
            </div>
        """
    },

    # =========================================================================
    # Challenge 2 (Q11 to Q20): Yearly Rhythms, Vasanta, Grishma, Varsha
    # =========================================================================
    {
        "id": 11,
        "question": "How many traditional seasons (Shad Ritu) are recognized in the classical Indian ecological calendar?",
        "options": [
            "Six seasons (Vasanta, Grishma, Varsha, Sharad, Hemant, Shishir)",
            "Only two seasons (Hot and Cold)",
            "Twelve seasons (one for each month)",
            "Four seasons like Western temperate regions"
        ],
        "answer": 0,
        "explanation": "The Indian subcontinent tracks six distinct two-month seasons known as the Shad Ritu, reflecting regional biodiversity and weather patterns.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>The Indian Shad Ritu System:</strong></p>
                <p class='text-slate-300'>Unlike the 4 temperate European seasons, India's geographical location creates six distinct ecological periods: Vasanta (Spring), Grishma (Summer), Varsha (Monsoon), Sharad (Autumn), Hemant (Pre-winter), and Shishir (Winter).</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Six seasons)</p>
            </div>
        """
    },
    {
        "id": 12,
        "question": "Which season in India is traditionally celebrated as 'Rituraj'—the King of Seasons?",
        "options": [
            "Vasanta (Spring)",
            "Grishma (Summer)",
            "Shishir (Winter)",
            "Varsha (Monsoon)"
        ],
        "answer": 0,
        "explanation": "Vasanta is honored as Rituraj due to its moderate climate, refreshing breezes, and profuse blossoming of flora.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Rituraj Vasanta:</strong></p>
                <p class='text-slate-300'>Occurring in March and April, Vasanta brings an optimal balance of temperature, bursting blossoms on mango and palash trees, and the joyful songs of cuckoos.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Vasanta (Spring))</p>
            </div>
        """
    },
    {
        "id": 13,
        "question": "Which tree is famous across central and northern India for exploding into vibrant orange-red blossoms known as the 'Flame of the Forest' during Vasanta?",
        "options": [
            "Palash (Butea monosperma / Tesu)",
            "Coconut palm",
            "Pine tree",
            "Eucalyptus"
        ],
        "answer": 0,
        "explanation": "The Palash tree sheds its leaves and bursts into brilliant fiery orange blooms in spring, earning its title 'Flame of the Forest'.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Palash (Flame of the Forest):</strong></p>
                <p class='text-slate-300'>During Vasanta, Palash trees shed their foliage and become entirely covered in bright crimson-orange flowers, traditionally collected to extract natural organic herbal Holi colours.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Palash (Butea monosperma / Tesu))</p>
            </div>
        """
    },
    {
        "id": 14,
        "question": "What are the hot, dusty, dehydrating summer winds blowing across northern India in May and June called?",
        "options": [
            "The Loo",
            "The Monsoon gale",
            "The Blizzard",
            "The Polar vortex"
        ],
        "answer": 0,
        "explanation": "The Loo is a fierce, dry, and scorching summer wind that originates over the Thar desert and sweeps across the Indo-Gangetic plains.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>The Loo Phenomenon:</strong></p>
                <p class='text-slate-300'>Temperatures in the Loo can reach 45 °C to 48 °C with extremely low humidity, causing rapid fluid evaporation from human skin and triggering severe heat exhaustion if unprotected.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (The Loo)</p>
            </div>
        """
    },
    {
        "id": 15,
        "question": "Which traditional cooling beverage made from roasted raw green mangoes is consumed during Grishma summer to prevent heatstroke?",
        "options": [
            "Aam Panna",
            "Hot tomato soup",
            "Boiling black coffee",
            "Warm ginger tea"
        ],
        "answer": 0,
        "explanation": "Aam Panna is prepared from boiled or roasted unripe mangoes blended with cumin, mint, and black salt, providing electrolytes that counteract dehydration.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Nutritional Chemistry of Aam Panna:</strong></p>
                <p class='text-slate-300'>Raw green mango contains high concentrations of pectin and vitamin C. When seasoned with rock salt (sodium chloride) and cumin, it replenishes depleted electrolytes lost via perspiration during Grishma.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Aam Panna)</p>
            </div>
        """
    },
    {
        "id": 16,
        "question": "What is the pleasant earthy smell produced when the first rain drops of the Varsha monsoon hit dry parched soil called?",
        "options": [
            "Petrichor",
            "Chloroform",
            "Methane",
            "Hydrogen peroxide"
        ],
        "answer": 0,
        "explanation": "Petrichor is the distinct earthy scent released when rain moistens dry soil, produced by soil actinobacteria synthesizing geosmin and plant oils.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Science of Petrichor:</strong></p>
                <p class='text-slate-300'>During dry periods, plants secrete organic oils absorbed by clay minerals. When raindrops strike, tiny air bubbles trap these oils along with bacterial geosmin and burst into aerosols, releasing the fragrance of petrichor.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Petrichor)</p>
            </div>
        """
    },
    {
        "id": 17,
        "question": "Which bird famously fans its magnificent eye-spotted tail covert feathers and performs courtship dances at the arrival of dark monsoon clouds in Varsha?",
        "options": [
            "The Indian Peafowl (Peacock)",
            "The common house sparrow",
            "The barn owl",
            "The white gull"
        ],
        "answer": 0,
        "explanation": "Peacocks display their iridescent feather trains and dance energetically with the onset of monsoon cloud cover and raindrops.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Monsoon Courtship Biology:</strong></p>
                <p class='text-slate-300'>The arrival of the monsoon coincides with the peak breeding season of the Indian Peafowl (<em>Pavo cristatus</em>). Abundant food, moisture, and cooler temperatures trigger elaborate courtship displays.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (The Indian Peafowl (Peacock))</p>
            </div>
        """
    },
    {
        "id": 18,
        "question": "Why do earthworms leave their subterranean burrows and crawl onto the ground surface during heavy Varsha downpours?",
        "options": [
            "Their underground burrows become completely waterlogged, depriving them of atmospheric oxygen needed for skin respiration",
            "They come out to sunbathe under the clouds",
            "They are searching for ice cream",
            "They want to swim in deep rivers"
        ],
        "answer": 0,
        "explanation": "Earthworms breathe through their moist skin by absorbing oxygen from air pockets in soil; when flooded with water, they must surface to avoid suffocation.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Cutaneous Respiration in Earthworms:</strong></p>
                <p class='text-slate-300'>Earthworms possess no lungs. Heavy rainfall fills microscopic air spaces in the soil with water, depleting dissolved oxygen and forcing earthworms to migrate to the surface to breathe.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Underground burrows become waterlogged, depriving them of oxygen)</p>
            </div>
        """
    },
    {
        "id": 19,
        "question": "Which of these major agricultural crops is a classic Kharif crop, sown with the arrival of monsoon rains in June and harvested in autumn?",
        "options": [
            "Paddy (Rice)",
            "Wheat",
            "Mustard",
            "Barley"
        ],
        "answer": 0,
        "explanation": "Paddy rice requires substantial water and warm temperatures, making it the primary Kharif staple across India.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Kharif Monsoon Staples:</strong></p>
                <p class='text-slate-300'>Kharif crops (rice, maize, jowar, bajra, soybean, cotton) depend on monsoon moisture. In contrast, wheat and mustard are Rabi crops sown in the cooler months of autumn.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Paddy (Rice))</p>
            </div>
        """
    },
    {
        "id": 20,
        "question": "What happens to the water levels in village open dug wells and reservoirs between the end of Grishma summer and the end of Varsha monsoon?",
        "options": [
            "Water levels recharge and rise significantly due to rainwater percolation into the groundwater table",
            "Water levels drop by 50 metres",
            "The water turns into solid granite",
            "All the water disappears into outer space"
        ],
        "answer": 0,
        "explanation": "Monsoon rains saturate the topsoil and infiltrate downwards, replenishing depleted aquifers and raising well water tables.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Aquifer Recharge Dynamics:</strong></p>
                <p class='text-slate-300'>Summer evaporation depletes soil moisture and lowers groundwater. Monsoon rainfall infiltrates permeable soil strata, recharging unconfined aquifers and refilling surface lakes and open dug wells.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Water levels recharge and rise significantly)</p>
            </div>
        """
    },

    # =========================================================================
    # Challenge 3 (Q21 to Q30): Sharad, Hemant, Shishir, Regional Contrasts
    # =========================================================================
    {
        "id": 21,
        "question": "Which lunar season arrives immediately after the Varsha monsoon retreats, characterized by cloudless sapphire skies and blooming white Kash flowers?",
        "options": [
            "Sharad (Autumn)",
            "Grishma (Summer)",
            "Vasanta (Spring)",
            "Varsha (Monsoon)"
        ],
        "answer": 0,
        "explanation": "Sharad (mid-September to mid-November) brings clear skies, receding floods, sparkling clean river waters, and blooming Kash grass.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Atmospheric Clarity of Sharad:</strong></p>
                <p class='text-slate-300'>With the retreat of monsoon winds, atmospheric humidity decreases and rain-washed air allows brilliant, deep blue skies. Feathery white Kash grass lines river floodplains.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Sharad (Autumn))</p>
            </div>
        """
    },
    {
        "id": 22,
        "question": "What nocturnal flower with sweet fragrance and small white petals with an orange stem carpets the ground on Sharad autumn mornings?",
        "options": [
            "Shiuli / Parijat (Nyctanthes arbor-tristis)",
            "Cactus flower",
            "Water lily",
            "Sunflower"
        ],
        "answer": 0,
        "explanation": "Shiuli (Parijat) blossoms bloom exclusively at night during autumn, shedding their fragrant white and orange flowers onto the dewy grass at sunrise.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>The Shiuli Flower:</strong></p>
                <p class='text-slate-300'>Also known as the Tree of Sorrow (because flowers drop at first dawn), Shiuli's sweet fragrance and vibrant orange corolla tube are celebrated in traditional autumn festivities.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Shiuli / Parijat)</p>
            </div>
        """
    },
    {
        "id": 23,
        "question": "In the pre-winter season of Hemant (November–December), what causes glistening dewdrops to form on grass tips during the night?",
        "options": [
            "Radiative cooling of ground surfaces causing ambient atmospheric water vapor to condense into liquid droplets",
            "Tiny rain showers falling every midnight from invisible clouds",
            "Plants actively pumping sap out through their leaves",
            "Frost melting from polar glaciers"
        ],
        "answer": 0,
        "explanation": "On clear, calm Hemant nights, the ground radiates heat into space. When surface temperature drops to the dew point, airborne moisture condenses into liquid dew.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Dew Formation Mechanism:</strong></p>
                <p class='text-slate-300'>The ground loses heat rapidly on clear winter nights. Air in direct contact with cold grass blades cools below its saturation temperature (dew point), forcing water vapor to condense into beads of liquid dew.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Radiative cooling causing ambient water vapor to condense into droplets)</p>
            </div>
        """
    },
    {
        "id": 24,
        "question": "What sweet treat made from freshly harvested sugarcane juice and roasted sesame seeds is popular across Indian households during Hemant and Shishir?",
        "options": [
            "Til-Gur (Sesame and Jaggery sweets / Gajak)",
            "Iced lemonade popsicles",
            "Raw mango pickle in vinegar",
            "Chilled watermelon slush"
        ],
        "answer": 0,
        "explanation": "Til (sesame) and Gur (jaggery) are rich in healthy fats, iron, and calories, providing essential warmth and energy in cold weather.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Nutritional Value of Til-Gur:</strong></p>
                <p class='text-slate-300'>Sesame seeds are packed with calcium and warming unsaturated lipids, while unrefined jaggery provides easily absorbed iron and sustained carbohydrate calories to maintain body core temperature in cold weather.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Til-Gur)</p>
            </div>
        """
    },
    {
        "id": 25,
        "question": "Which of the six Indian seasons brings the lowest temperatures, frosty mornings, and dense fog to northern India?",
        "options": [
            "Shishir (Winter)",
            "Vasanta (Spring)",
            "Grishma (Summer)",
            "Sharad (Autumn)"
        ],
        "answer": 0,
        "explanation": "Shishir (mid-January to mid-March) is the peak winter season, bringing sub-zero temperatures to the hills and cold fog to the plains.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Shishir Winter Characteristics:</strong></p>
                <p class='text-slate-300'>Marked by the lunar months of Magha and Phalguna, Shishir features cold northern winds from the snow-covered Himalayas, frequent radiation fog, and the shortest daylight spans of the year.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Shishir (Winter))</p>
            </div>
        """
    },
    {
        "id": 26,
        "question": "Why do people living in Jammu & Kashmir carry a 'Kangri' (a wicker-covered earthen pot with burning embers) under their pherans during winter?",
        "options": [
            "To provide portable personal warmth against sub-zero Himalayan freezing temperatures",
            "To cook food while walking on mountain trails",
            "To scare away wild mountain goats",
            "To light up dark caves at night"
        ],
        "answer": 0,
        "explanation": "The Kangri is an ingenious traditional Kashmiri portable heater that keeps individuals warm beneath their loose woollen gowns (pherans) during snowy winters.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Traditional Thermal Engineering: The Kangri:</strong></p>
                <p class='text-slate-300'>The Kangri consists of an inner clay bowl filled with glowing charcoal embers, encased within an insulated wicker basket with a sturdy handle. Kept under the woollen pheran, it traps hot air close to the torso.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (To provide portable personal warmth against sub-zero temperatures)</p>
            </div>
        """
    },
    {
        "id": 27,
        "question": "Why does coastal Kerala maintain mild, warm weather in January, while Srinagar in Kashmir is covered in thick snow?",
        "options": [
            "Kerala is near the tropical equator and bordered by the vast Arabian Sea, which regulates temperature, whereas Kashmir is at high latitude and elevated altitude",
            "Kerala has no winter season because the Sun is physically closer to southern India than to northern India",
            "Kashmir is shielded from all sunlight by outer space clouds",
            "Kerala's sea water is boiled by underwater heaters"
        ],
        "answer": 0,
        "explanation": "Proximity to the equator and the moderating maritime effect of the Arabian Sea keep Kerala warm, while Kashmir's elevation and high latitude bring sub-zero snow.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Geographical Drivers of Climate:</strong></p>
                <p class='text-slate-300'>1. Latitude: Kerala is closer to the equator, receiving more direct solar insolation.<br>2. Altitude: Srinagar sits at ~1,585 m elevation in the Himalayas, experiencing lapse-rate cooling.<br>3. Maritime Moderation: Water has a high specific heat capacity, preventing extreme temperature drops along coastlines.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Kerala is near the equator and bordered by the sea, while Kashmir is elevated and at high latitude)</p>
            </div>
        """
    },
    {
        "id": 28,
        "question": "What type of climate is experienced by the Thar Desert in western Rajasthan across seasons?",
        "options": [
            "Arid climate with extreme temperature swings: blazing 48 °C summer days, cold winter nights, and very sparse annual rainfall",
            "Wet tropical rainforest climate with constant downpours every week",
            "Arctic tundra climate with permanent ice sheets",
            "Alpine mountain climate with freezing glaciers"
        ],
        "answer": 0,
        "explanation": "Sand has low specific heat capacity, causing it to heat up rapidly under daytime sun and cool down rapidly at night, creating extreme temperature swings in dry desert air.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Thermodynamics of Desert Sand:</strong></p>
                <p class='text-slate-300'>Because dry quartz sand heats up and cools down four times faster than water, desert regions exhibit severe diurnal and seasonal extremes, accompanied by scant precipitation.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Arid climate with extreme temperature swings and very sparse rainfall)</p>
            </div>
        """
    },
    {
        "id": 29,
        "question": "Why do deciduous trees like the Teak and Sheesham drop their leaves in dry seasons?",
        "options": [
            "To prevent transpiration water loss through leaf pores during months when soil moisture is low",
            "Because leaves get too heavy for branches to carry",
            "Because animals eat all the roots",
            "Because trees sleep during winter and forget to hold leaves"
        ],
        "answer": 0,
        "explanation": "Dropping leaves eliminates leaf surface area, preventing stomatal transpiration and conserving internal moisture until the next rains.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Abscission and Water Conservation:</strong></p>
                <p class='text-slate-300'>Over 95% of a tree's water loss occurs via transpiration through microscopic stomata on leaf surfaces. Shedding leaves (abscission) allows trees to enter a protective dormancy state during drought.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (To prevent transpiration water loss when soil moisture is low)</p>
            </div>
        """
    },
    {
        "id": 30,
        "question": "What seasonal fruit, rich in natural vitamin C and antioxidants, is harvested in abundance during Indian winters to boost immunity?",
        "options": [
            "Amla (Indian Gooseberry) and Oranges (Santra)",
            "Watermelons",
            "Raw green mangoes",
            "Litchis"
        ],
        "answer": 0,
        "explanation": "Amla and citrus oranges ripen in winter, providing concentrated vitamin C that protects the respiratory system and enhances immune defenses.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Seasonal Immunity: Amla and Citrus:</strong></p>
                <p class='text-slate-300'>Fresh Amla contains approximately twenty times more vitamin C than orange juice by weight. Ripening during cold Shishir months, it naturally shields human cells against winter respiratory pathogens.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Amla and Oranges)</p>
            </div>
        """
    },

    # =========================================================================
    # Challenge 4 (Q31 to Q40): Crops, Harvest Festivals, Rhythm of Life, Harmony
    # =========================================================================
    {
        "id": 31,
        "question": "What are crops like watermelon, cucumber, muskmelon, and bitter gourd grown in the short summer gap between March and June called?",
        "options": [
            "Zaid crops",
            "Kharif crops",
            "Rabi crops",
            "Winter crops"
        ],
        "answer": 0,
        "explanation": "Zaid crops are fast-growing summer crops cultivated with irrigation between the Rabi harvest and the onset of the Kharif monsoon.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>The Zaid Cropping Season:</strong></p>
                <p class='text-slate-300'>In the tripartite Indian agricultural calendar, Zaid occupies the warm summer months of March through June. Melons and cucurbit vegetables mature rapidly in warm soils with supplementary irrigation.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Zaid crops)</p>
            </div>
        """
    },
    {
        "id": 32,
        "question": "Which of the following represents a Rabi crop sown in autumn (November) and harvested in spring (March–April)?",
        "options": [
            "Wheat (Gehun)",
            "Paddy rice (Dhan)",
            "Jowar (Sorghum)",
            "Cotton (Kapas)"
        ],
        "answer": 0,
        "explanation": "Wheat is the staple Rabi grain crop across northern and central India, requiring cool growth conditions and bright sunshine for grain filling.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Rabi Wheat Cultivation:</strong></p>
                <p class='text-slate-300'>Wheat requires temperatures around 10 °C to 15 °C during germination and vegetative tillering, and warm temperatures (21 °C to 26 °C) during ripening, making it the supreme Rabi grain.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Wheat (Gehun))</p>
            </div>
        """
    },
    {
        "id": 33,
        "question": "What is the famous harvest festival celebrated in Tamil Nadu in mid-January, where fresh milk and newly harvested rice are boiled in decorated clay pots until they bubble over?",
        "options": [
            "Pongal",
            "Baisakhi",
            "Holi",
            "Diwali"
        ],
        "answer": 0,
        "explanation": "Pongal (meaning 'to boil over' or 'spill over') is a 4-day Tamil harvest festival celebrating the overflowing abundance of newly harvested rice, milk, and jaggery.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Pongal Harvest Tradition:</strong></p>
                <p class='text-slate-300'>Families boil sweet rice in clay pots until the frothy milk spills over, chanting 'Pongalo Pongal!' to symbolize prosperity and express gratitude to the Sun god (Surya) and farm cattle (Mattu Pongal).</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Pongal)</p>
            </div>
        """
    },
    {
        "id": 34,
        "question": "Which joyful festival celebrated in Punjab in April marks the harvesting of golden winter wheat crops and is commemorated with energetic Bhangra and Giddha dances?",
        "options": [
            "Baisakhi (Vaisakhi)",
            "Makar Sankranti",
            "Onam",
            "Christmas"
        ],
        "answer": 0,
        "explanation": "Baisakhi marks the joyous culmination of the Rabi wheat harvest in Punjab, filled with celebratory drumbeats and traditional dances.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Baisakhi Wheat Harvest:</strong></p>
                <p class='text-slate-300'>Celebrated on April 13 or 14, Baisakhi marks the ripening of wheat fields across Punjab and Haryana. Farmers celebrate the fruitful reward of months of hard labor with community meals and cultural dances.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Baisakhi (Vaisakhi))</p>
            </div>
        """
    },
    {
        "id": 35,
        "question": "Which Assamese festival celebrated in mid-April marks the arrival of spring, seed sowing, and the Assamese New Year with joyous folk dances?",
        "options": [
            "Rongali Bihu (Bohag Bihu)",
            "Magh Bihu",
            "Kati Bihu",
            "Lohri"
        ],
        "answer": 0,
        "explanation": "Rongali Bihu (Bohag Bihu) is Assam's spring harvest festival celebrating the new agricultural cycle, fertility, and community dances with dhol and pepa flutes.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>The Three Bihus of Assam:</strong></p>
                <p class='text-slate-300'>Assam celebrates three Bihus tied to agriculture: Rongali Bihu in spring (sowing), Kati Bihu in autumn (crop protection), and Magh Bihu in winter (harvest feasting).</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Rongali Bihu (Bohag Bihu))</p>
            </div>
        """
    },
    {
        "id": 36,
        "question": "Why do traditional festivals like Makar Sankranti, Pongal, Lohri, and Magh Bihu all occur within the same week in mid-January?",
        "options": [
            "They all celebrate the exact same astronomical event: the winter crop harvest and the Sun beginning its northward journey (Uttarayana)",
            "Because schools ordered all holidays to be grouped together",
            "Because all calendars were printed on the same day",
            "Because the Moon turns blue every January"
        ],
        "answer": 0,
        "explanation": "Despite different regional languages and cultural customs, all these festivals celebrate the winter harvest and the astronomical northward shift of the Sun.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Astronomical Unity in Diversity:</strong></p>
                <p class='text-slate-300'>On January 14/15, the Sun transitions into the zodiac of Makara (Capricorn), beginning Uttarayana. Across India, diverse communities celebrate the harvest of rice, sugarcane, and sesame under localized regional traditions.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (They celebrate the winter harvest and the Sun's northward journey)</p>
            </div>
        """
    },
    {
        "id": 37,
        "question": "In the science of seasonal living (Ritucharya), why are cooling foods like barley, cucumbers, and buttermilk recommended during peak summer Grishma?",
        "options": [
            "They naturally soothe internal body heat, promote sweat evaporation, and prevent dehydration during intense heatwaves",
            "They freeze the stomach into solid ice",
            "They eliminate the need to breathe air",
            "They turn the body completely invisible"
        ],
        "answer": 0,
        "explanation": "Water-rich and easily digestible foods prevent core overheating and restore fluid and electrolyte balances lost through sweating.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Dietary Thermoregulation:</strong></p>
                <p class='text-slate-300'>During hot weather, peripheral blood vessels dilate to lose heat, which can reduce digestive capacity. Light, hydrating, probiotic foods like buttermilk (Chaas) and barley water restore gut balance without heavy digestive strain.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (They soothe internal heat, promote sweat evaporation, and prevent dehydration)</p>
            </div>
        """
    },
    {
        "id": 38,
        "question": "Why do people wear airy, loose, light-colored cotton clothes in summer and dark, heavy, layered woollens in winter?",
        "options": [
            "Light cotton reflects sunlight and allows sweat evaporation in summer; dark wool absorbs radiant heat and traps insulating air in winter",
            "Because wool melts in summer into toxic glue",
            "Because cotton catches fire in winter frost",
            "Because color determines how heavy a person is"
        ],
        "answer": 0,
        "explanation": "White/light cotton reflects solar radiation and breathes well for evaporative cooling; dark wool absorbs light and traps stagnant warm air pockets.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Thermal Physics of Clothing:</strong></p>
                <p class='text-slate-300'>1. Albedo: White surfaces reflect up to 80% of incident solar radiation, keeping skin cool in summer.<br>2. Permeability: Cotton weaves let evaporated perspiration escape.<br>3. Insulation: Wool's crimped structure traps dead-air pockets with low thermal conductivity (k ~ 0.026 W/mK), preserving body warmth in winter.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Light cotton reflects sun and breathes; dark wool absorbs heat and traps insulating air)</p>
            </div>
        """
    },
    {
        "id": 39,
        "question": "What ecological consequence would occur if the scorching heat of Grishma summer never occurred in India?",
        "options": [
            "The low-pressure thermodynamic engine pulling monsoon clouds from the Indian Ocean would fail, causing severe drought and crop failure",
            "Rivers would flow twice as fast forever",
            "All trees would turn into gold",
            "Fish would walk onto land"
        ],
        "answer": 0,
        "explanation": "The summer heat over the Tibetan plateau and Indian landmass creates the low-pressure suction that draws moisture-rich monsoon winds inland.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>The Thermodynamic Monsoon Engine:</strong></p>
                <p class='text-slate-300'>Solar heating warms the landmass far more than the surrounding oceans, creating intense thermal low-pressure. This pressure gradient pulls moisture-saturated winds from the southern hemisphere across the equator as the southwest monsoon.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (The low-pressure engine pulling monsoon clouds would fail, causing drought)</p>
            </div>
        """
    },
    {
        "id": 40,
        "question": "What is the core philosophical and scientific message taught by Chapter 9, 'Rhythms of Nature'?",
        "options": [
            "Change is continuous, natural, and cyclic; every season is necessary for life, and human well-being depends on living in harmony with planetary rhythms",
            "Humans should stop the Earth from spinning so that night never falls",
            "We should destroy forests so that seasons stop changing",
            "Only winter is good, and all other seasons should be banned"
        ],
        "answer": 0,
        "explanation": "Nature is a balanced, repeating cycle where each season plays a vital ecological role, and human cultures thrive when harmonized with these rhythms.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Living in Ecological Harmony:</strong></p>
                <p class='text-slate-300'>Nature's rhythms—from daily diurnal rotation to annual seasonal revolutions—form the scaffolding of life on Earth. Recognizing this cyclic interconnectedness inspires responsible environmental stewardship, sustainable agriculture, and gratitude for our planet's living tapestry.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Change is continuous, natural, and cyclic; living in harmony with planetary rhythms sustains life)</p>
            </div>
        """
    }
]

print("Mastery quiz questions defined:", len(QUIZ_QUESTIONS))

