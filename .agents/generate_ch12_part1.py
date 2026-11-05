"""
Class 6 Science Chapter 12: Beyond Earth
Part 1: Slides 1 to 8 Data Module
Headings are short (1-3 words) with exact same meaning. Zero raw LaTeX.
"""

CHAPTER_META = {
    "title": "Beyond Earth",
    "class_grade": "Class 6",
    "chapter_num": 12,
    "theme": "Curiosity • NEP 2020 Science",
    "short_titles": [
        "Night Caravans",
        "Star Patterns",
        "Hunter & Dog",
        "North Anchor",
        "Dark Sky City",
        "Star Finder",
        "Solar Heart",
        "Rocky Four",
        "Gas Giants",
        "Dwarf Worlds",
        "Twinkle or Steady",
        "Moon & Craters",
        "Touch the Moon",
        "Belt of Rocks",
        "Cosmic Ice",
        "Milky Way",
        "Challenge 1",
        "Challenge 2",
        "Challenge 3",
        "Challenge 4"
    ]
}

SLIDES_PART1 = [
    {
        "id": 1,
        "title": "Night Caravans",
        "subtitle": "Yangdol & Dorjay under Nubra's Crystal Sky & Ancient Celestial Navigation",
        "concept_html": """
            <p>High in the cold mountain desert of Nubra in Ladakh, the air is thin, crisp, and completely free from urban haze. Looking up into the deep night sky, twin siblings Yangdol and Dorjay were mesmerized by thousands of dazzling stars glittering like diamond dust across an ink-black canvas.</p>
            <p class='mt-2'>Their grandfather shared an enchanting historical truth: centuries ago, intrepid Silk Route traders and desert caravans navigated treacherous mountain passes and boundless sandy deserts at night using these exact same celestial beacons long before the magnetic compass was invented!</p>
            <div class='mt-3 p-3 rounded-xl bg-slate-950/60 border border-slate-800 text-xs text-indigo-300'>
                ✨ <strong>Celestial Landmark:</strong> Stars maintain virtually fixed relative geometric configurations over human lifetimes, turning the night sky into humanity's oldest, most reliable celestial clock and compass.
            </div>
        """,
        "spoken_text": "Welcome to our cosmic journey beyond Earth. High in the cold mountain desert of Nubra in Ladakh, twin siblings Yangdol and Dorjay gazed upward into the crystal-clear night sky. Far from the smoke and glare of modern cities, thousands of brilliant stars sparkled across the dark heavens. For thousands of years, ancient Silk Route caravans and ocean sailors looked up at these exact same stars to navigate across uncharted continents and stormy seas. Let us explore the wonders of the night sky, our solar neighborhood, and the vast universe beyond.",
        "lecture_script": "Welcome to our cosmic journey beyond Earth. High in the cold mountain desert of Nubra in Ladakh, twin siblings Yangdol and Dorjay gazed upward into the crystal-clear night sky. Far from the smoke and glare of modern cities, thousands of brilliant stars sparkled across the dark heavens. For thousands of years, ancient Silk Route caravans and ocean sailors looked up at these exact same stars to navigate across uncharted continents and stormy seas. Let us explore the wonders of the night sky, our solar neighborhood, and the vast universe beyond.",
        "checkpoints": [
            {
                "question": "Why is the Nubra Valley in Ladakh considered an exceptional terrestrial site for astronomical sky observation?",
                "options": [
                    "It has dense artificial city neon lights on every hill",
                    "Its high altitude, low humidity, cloudless weather, and minimal light pollution provide pristine atmospheric clarity",
                    "It is located directly on top of the Moon's surface",
                    "Stars are physically closer to Ladakh than to any other place on Earth"
                ],
                "correct": 1,
                "explanation": "High altitude, dry thin air, low atmospheric turbulence, and absence of urban light pollution make Ladakh an ideal astronomical observing window.",
                "study_insight": "Astronomical observatories are intentionally built in high, dry, isolated mountain zones."
            },
            {
                "question": "How did ancient desert caravans and seafaring sailors reliably determine travel directions before the invention of magnetic compasses?",
                "options": [
                    "By following migratory bird calls exclusively during dense blizzards",
                    "By observing the positions of recognizable star patterns and the stationary Pole Star in the night sky",
                    "By measuring the temperature of sand with wooden rulers",
                    "By rolling dice at every crossroads"
                ],
                "correct": 1,
                "explanation": "Celestial navigation relied on tracking prominent constellations and the stationary Pole Star to identify cardinal directions at night.",
                "study_insight": "The predictable apparent positions of stars provided reliable direction-finding for ancient explorers."
            }
        ]
    },
    {
        "id": 2,
        "title": "Star Patterns",
        "subtitle": "Self-Luminous Stars, Historic Constellations & The 88 IAU Sky Sectors",
        "concept_html": """
            <p>What is a star? A <strong>star</strong> is a colossal, self-luminous cosmic sphere of incandescent plasma held together by its own gravity, producing tremendous heat and light through thermonuclear fusion.</p>
            <div class='space-y-2 mt-2 text-slate-300'>
                <p><strong>Constellations:</strong> Ancient civilizations observed imaginative patterns formed by prominent stars, naming them after mythological heroes, animals, and revered deities.</p>
                <div class='p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-indigo-300'>
                    🌐 <strong>IAU Scientific Standardization:</strong> In the early 20th century, the <strong>International Astronomical Union (IAU)</strong> standardized the night sky, dividing the entire celestial sphere into <strong>88 officially recognized constellations</strong> with precise boundary lines.
                </div>
                <p class='text-xs text-slate-400'>Every star, galaxy, or nebular object visible from Earth resides within one of these 88 distinct celestial territories, much like every town belongs to a specific state or province!</p>
            </div>
        """,
        "spoken_text": "A star is a colossal, glowing sphere of hot gas that generates its own light and heat through nuclear reactions deep in its core. For millennia, different human cultures connected bright stars with imaginary lines, creating recognizable pictures called constellations. In the early twentieth century, the International Astronomical Union brought scientific order to the heavens by dividing the entire sky into exactly eighty-eight official constellations. Today, every single star and distant galaxy belongs to one of these eighty-eight mapped cosmic regions.",
        "lecture_script": "A star is a colossal, glowing sphere of hot gas that generates its own light and heat through nuclear reactions deep in its core. For millennia, different human cultures connected bright stars with imaginary lines, creating recognizable pictures called constellations. In the early twentieth century, the International Astronomical Union brought scientific order to the heavens by dividing the entire sky into exactly eighty-eight official constellations. Today, every single star and distant galaxy belongs to one of these eighty-eight mapped cosmic regions.",
        "checkpoints": [
            {
                "question": "What is the defining astronomical property that distinguishes a star from a planet or moon?",
                "options": [
                    "A star shines with its own internally generated light produced by nuclear fusion",
                    "A star is always made of solid green granite rock",
                    "A star only reflects sunlight like a giant mirror",
                    "A star orbits around human-made satellites"
                ],
                "correct": 0,
                "explanation": "Stars are self-luminous thermonuclear reactors generating light and heat, whereas planets and moons merely reflect incident light from stars.",
                "study_insight": "Nuclear fusion in stellar cores converts hydrogen into helium, liberating massive electromagnetic energy."
            },
            {
                "question": "Into how many official constellations did the International Astronomical Union (IAU) systematically divide the celestial sphere?",
                "options": [
                    "12 constellations",
                    "88 constellations",
                    "365 constellations",
                    "1,000 constellations"
                ],
                "correct": 1,
                "explanation": "The IAU adopted 88 official constellations in 1922, mapping the entire sky into contiguous, non-overlapping geometric sectors.",
                "study_insight": "Constellations serve as standardized coordinates for astronomers cataloging deep-sky objects."
            }
        ]
    },
    {
        "id": 3,
        "title": "Hunter & Dog",
        "subtitle": "Orion's Belt, Sirius (The Brightest Star), Taurus & Indian Nakshatra Heritage",
        "concept_html": """
            <p>Among the 88 constellations, several majestic star groupings dominate the winter night sky:</p>
            <div class='grid grid-cols-1 md:grid-cols-2 gap-3 mt-3'>
                <div class='p-3 rounded-xl bg-slate-950/70 border border-slate-800'>
                    <h4 class='text-xs font-bold text-indigo-400 uppercase'>Orion (The Celestial Hunter)</h4>
                    <p class='text-xs text-slate-300 mt-1'>Features an unmistakable straight line of three brilliant stars forming <strong>Orion's Belt</strong> (Mṛgaśīrṣā in Indian astronomy). Its reddish supergiant shoulder star is <strong>Betelgeuse</strong> (called <em>Ārdrā</em> nakshatra), and its icy blue foot star is <strong>Rigel</strong>.</p>
                </div>
                <div class='p-3 rounded-xl bg-slate-950/70 border border-slate-800'>
                    <h4 class='text-xs font-bold text-sky-400 uppercase'>Canis Major & Sirius (Dog Star)</h4>
                    <p class='text-xs text-slate-300 mt-1'>Following the line of Orion's belt southeast points directly to <strong>Sirius</strong> (Vyādha), the <strong>brightest star in the entire night sky</strong>, radiating with a piercing blue-white glow roughly 8.6 light-years away!</p>
                </div>
            </div>
            <div class='p-3 rounded-xl bg-amber-950/30 border border-amber-500/20 text-xs text-amber-200 mt-3'>
                🌟 <strong>Indian Nakshatra Heritage:</strong> Indian traditional astronomy divides the ecliptic path into 27 lunar mansions (Nakshatras), celebrating famous asterisms like <em>Krittikā</em> (the Pleiades star cluster) and fiery red <em>Rohiņi</em> (Aldebaran in Taurus).
            </div>
        """,
        "spoken_text": "One of the most magnificent sights in the winter sky is the constellation Orion, depicted as a mighty celestial hunter. At its heart lies an unmistakable belt of three bright stars in a straight row. If you trace a line through Orion's belt toward the southeast, it leads your eyes directly to Sirius in the constellation Canis Major. Sirius is the brightest star in the entire night sky, blazing with piercing blue-white light. Indian astronomers deeply studied these stars, incorporating them into our heritage of twenty-seven Nakshatras, including Ārdrā, Krittikā, and red Rohiņi.",
        "lecture_script": "One of the most magnificent sights in the winter sky is the constellation Orion, depicted as a mighty celestial hunter. At its heart lies an unmistakable belt of three bright stars in a straight row. If you trace a line through Orion's belt toward the southeast, it leads your eyes directly to Sirius in the constellation Canis Major. Sirius is the brightest star in the entire night sky, blazing with piercing blue-white light. Indian astronomers deeply studied these stars, incorporating them into our heritage of twenty-seven Nakshatras, including Ārdrā, Krittikā, and red Rohiņi.",
        "checkpoints": [
            {
                "question": "Which star holds the title of the brightest individual star visible in the night sky from Earth?",
                "options": [
                    "The Pole Star (Polaris)",
                    "Sirius (in Canis Major)",
                    "Betelgeuse (in Orion)",
                    "Proxima Centauri"
                ],
                "correct": 1,
                "explanation": "Sirius (the Dog Star) has an apparent magnitude of -1.46, making it visually brighter than any other star in Earth's night sky.",
                "study_insight": "Apparent brightness depends on both intrinsic stellar luminosity and proximity to Earth."
            },
            {
                "question": "Which prominent visual feature makes the constellation Orion (The Hunter) instantly identifiable in the winter sky?",
                "options": [
                    "A perfect circle of twenty green stars",
                    "A straight belt of three bright, evenly spaced stars",
                    "A single isolated yellow star with zero neighbors",
                    "A bright square that rotates every minute"
                ],
                "correct": 1,
                "explanation": "Orion's Belt is formed by three bright stars (Alnitak, Alnilam, Mintaka) in a distinctive straight alignment.",
                "study_insight": "Orion's Belt serves as a prime celestial signpost for locating neighboring stars like Sirius and Aldebaran."
            }
        ]
    },
    {
        "id": 4,
        "title": "North Anchor",
        "subtitle": "The Pole Star (Dhruva Tārā), Ursa Major Pointers & Cultural Lore",
        "concept_html": """
            <p>While all stars appear to slowly wheel across the night sky from east to west due to Earth's axial rotation, one unique star remains nearly motionless: the <strong>Pole Star (Polaris / Dhruva Tārā)</strong>.</p>
            <div class='space-y-2 mt-2 text-slate-300'>
                <ul class='list-disc pl-5 space-y-1.5'>
                    <li><strong>Why Is It Stationary?</strong> The Pole Star lies almost directly along the northern extension of Earth's rotational axis. As Earth spins on its axis, Polaris appears fixed directly above the true geographic North Pole!</li>
                    <li><strong>Locating the Pole Star:</strong> Find the famous <strong>Big Dipper (part of Ursa Major / Saptarishi)</strong>, resembling a giant ladle. The two stars at the outer edge of the cup are called <strong>Pointer Stars</strong>. An imaginary line drawn through them points straight to Dhruva Tārā in Ursa Minor!</li>
                    <li><strong>Indigenous Folk Stories:</strong> Indian cultural traditions view this constellation with rich imagination: some rural communities saw it as an elderly grandmother's cot (*khatiyā*) with three thieves sneaking away, while coastal sailors saw an anchored fishing boat.</li>
                </ul>
            </div>
        """,
        "spoken_text": "As Earth spins on its rotational axis, most stars appear to rise in the east and set in the west. However, one remarkable star appears completely stationary: the Pole Star, revered in Indian heritage as Dhruva Tārā. Because Polaris sits directly above Earth's geographic North Pole, it never changes its position, acting as an unwavering northern beacon for travelers. You can easily find it using the seven stars of the Saptarishi, or Big Dipper. Drawing an imaginary line through the two pointer stars on the dipper's bowl leads straight to the Pole Star.",
        "lecture_script": "As Earth spins on its rotational axis, most stars appear to rise in the east and set in the west. However, one remarkable star appears completely stationary: the Pole Star, revered in Indian heritage as Dhruva Tārā. Because Polaris sits directly above Earth's geographic North Pole, it never changes its position, acting as an unwavering northern beacon for travelers. You can easily find it using the seven stars of the Saptarishi, or Big Dipper. Drawing an imaginary line through the two pointer stars on the dipper's bowl leads straight to the Pole Star.",
        "checkpoints": [
            {
                "question": "Why does the Pole Star (Dhruva Tārā) appear almost completely stationary in the night sky while other stars appear to move?",
                "options": [
                    "Because it is glued to the surface of the Moon",
                    "Because it lies almost directly in line with Earth's northern rotational axis",
                    "Because it is an artificial satellite launched by ancient astronomers",
                    "Because it burns out and disappears whenever Earth rotates"
                ],
                "correct": 1,
                "explanation": "Because Polaris is aligned with Earth's northern axis of rotation, planetary spin does not displace its apparent celestial position.",
                "study_insight": "The altitude of the Pole Star above the horizon equals the observer's geographic latitude in the Northern Hemisphere."
            },
            {
                "question": "Which pair of stars in the Big Dipper (Ursa Major / Saptarishi) is used as 'Pointer Stars' to find the Pole Star?",
                "options": [
                    "The two stars forming the handle of the ladle",
                    "The two stars forming the outer bowl edge opposite the handle",
                    "The central three stars of Orion's belt",
                    "The two brightest stars inside the constellation Taurus"
                ],
                "correct": 1,
                "explanation": "The two stars on the outer edge of the Big Dipper's bowl (Merak and Dubhe) point in a straight line directly to Polaris.",
                "study_insight": "Extending the distance between the pointer stars roughly 5 times leads directly to Polaris."
            }
        ]
    },
    {
        "id": 5,
        "title": "Dark Sky City",
        "subtitle": "Light Pollution, Hanle Dark Sky Reserve & Night Vision Preparation",
        "concept_html": """
            <p>Why can we see thousands of sparkling stars in rural villages, but barely a dozen dim dots in bustling cities? The answer is <strong>light pollution</strong>:</p>
            <div class='grid grid-cols-1 md:grid-cols-2 gap-3 mt-3'>
                <div class='p-3 rounded-xl bg-slate-950/70 border border-slate-800'>
                    <h4 class='text-xs font-bold text-rose-400 uppercase'>City Skyglow & Pollution</h4>
                    <p class='text-xs text-slate-300 mt-1'>Streetlights, illuminated billboards, vehicle headlights, and industrial smog scatter photons into the atmosphere, creating a luminous 'skyglow' that drowns out faint cosmic light from distant stars.</p>
                </div>
                <div class='p-3 rounded-xl bg-slate-950/70 border border-slate-800'>
                    <h4 class='text-xs font-bold text-emerald-400 uppercase'>Dark Sky Sanctuaries (Hanle)</h4>
                    <p class='text-xs text-slate-300 mt-1'>To safeguard pristine night skies for scientific research, India established the <strong>Hanle Dark Sky Reserve</strong> in eastern Ladakh, enforcing strict dark sky protocols so massive optical telescopes can peer billions of light-years into deep space.</p>
                </div>
            </div>
            <div class='p-3 rounded-xl bg-indigo-950/40 border border-indigo-500/30 text-xs text-indigo-200 mt-3'>
                👁️ <strong>Dark Adaptation Secret:</strong> When heading out for stargazing, your eyes require roughly <strong>20 to 30 minutes in total darkness</strong> to produce rhodopsin pigment and dilate pupils, unlocking true night vision sensitivity!
            </div>
        """,
        "spoken_text": "If you look up from a brightly lit city street at night, you can barely see a handful of dim stars. This is caused by light pollution, where excessive artificial streetlights, neon signs, and vehicular glare bounce off airborne dust, washing out the delicate light of distant stars. To protect the night sky for scientific discovery, India established the Hanle Dark Sky Reserve high in Ladakh, creating a pristine sanctuary for deep-space astronomy. When stargazing, patience is key: waiting twenty to thirty minutes away from bright screens allows your eyes to adapt fully to the dark, revealing thousands of hidden stars.",
        "lecture_script": "If you look up from a brightly lit city street at night, you can barely see a handful of dim stars. This is caused by light pollution, where excessive artificial streetlights, neon signs, and vehicular glare bounce off airborne dust, washing out the delicate light of distant stars. To protect the night sky for scientific discovery, India established the Hanle Dark Sky Reserve high in Ladakh, creating a pristine sanctuary for deep-space astronomy. When stargazing, patience is key: waiting twenty to thirty minutes away from bright screens allows your eyes to adapt fully to the dark, revealing thousands of hidden stars.",
        "checkpoints": [
            {
                "question": "What is the primary cause of 'light pollution' that obscures the view of stars in modern urban centers?",
                "options": [
                    "Stars turning off their light when passing over cities",
                    "Excessive, unshielded artificial lighting from streetlights, buildings, and billboards scattering into the atmosphere",
                    "The Moon shining ten times brighter above city centers",
                    "Clouds made exclusively of reflective silver foil"
                ],
                "correct": 1,
                "explanation": "Artificial skyglow scatters upward-directed light off atmospheric molecules and dust particles, overpowering the faint contrast of stars.",
                "study_insight": "Shielding streetlights downward significantly reduces urban skyglow without reducing ground illumination."
            },
            {
                "question": "Where is India's premier officially notified Dark Sky Reserve established to preserve pristine darkness for deep-space astronomy?",
                "options": [
                    "Connaught Place, New Delhi",
                    "Hanle, Eastern Ladakh",
                    "Marine Drive, Mumbai",
                    "Salt Lake, Kolkata"
                ],
                "correct": 1,
                "explanation": "The Hanle Dark Sky Reserve is located in high-altitude Changthang, Ladakh, housing the Indian Astronomical Observatory at 4,500 meters altitude.",
                "study_insight": "Hanle's high, cloudless, dry desert plateau provides world-class astronomical seeing conditions."
            }
        ]
    },
    {
        "id": 6,
        "title": "Star Finder",
        "subtitle": "Activities 12.2 & 12.3: Hands-On Sky Navigations with Digital Maps & Compass",
        "concept_html": """
            <p>Becoming an amateur astronomer is an exhilarating outdoor activity! Activities 12.2 and 12.3 guide you step-by-step through practical sky navigation:</p>
            <div class='space-y-2 mt-2 text-slate-300'>
                <ul class='list-disc pl-5 space-y-1.5'>
                    <li><strong>Preparation:</strong> Choose a clear, moonless night away from glaring streetlights. Carry a star chart or mobile sky app (like Stellarium or Sky Map) in 'red light mode' to preserve night vision.</li>
                    <li><strong>Activity 12.2 (Find the Pole Star):</strong> Face north. Locate the seven prominent stars of the Big Dipper ladle. Connect the two outer cup stars (Merak and Dubhe) and extend that line roughly 5 times forward to find steady Polaris.</li>
                    <li><strong>Activity 12.3 (Locate Orion & Sirius):</strong> Look south in winter. Spot the three close, bright belt stars of Orion. Follow the belt line southeast to lock onto brilliant, sparkling Sirius. Follow the belt northwest to locate orange-red Aldebaran in Taurus!</li>
                </ul>
            </div>
        """,
        "spoken_text": "Stargazing is an exciting hands-on adventure that anyone can enjoy. In Activity 12.2, you face northward on a clear night to spot the Big Dipper. Following the two pointer stars on the edge of the dipper's bowl leads directly to the Pole Star, fixing your northern horizon. In Activity 12.3, looking toward the southern winter sky reveals Orion the Hunter. Tracing an imaginary line straight through Orion's three belt stars to the left guides your gaze directly to brilliant Sirius, while extending the line to the right points to the fiery red giant Aldebaran. With a simple compass and red flashlight, the entire night sky unfolds like a cosmic map.",
        "lecture_script": "Stargazing is an exciting hands-on adventure that anyone can enjoy. In Activity 12.2, you face northward on a clear night to spot the Big Dipper. Following the two pointer stars on the edge of the dipper's bowl leads directly to the Pole Star, fixing your northern horizon. In Activity 12.3, looking toward the southern winter sky reveals Orion the Hunter. Tracing an imaginary line straight through Orion's three belt stars to the left guides your gaze directly to brilliant Sirius, while extending the line to the right points to the fiery red giant Aldebaran. With a simple compass and red flashlight, the entire night sky unfolds like a cosmic map.",
        "checkpoints": [
            {
                "question": "Why do professional and amateur astronomers use a red flashlight rather than bright white light while reading star charts outdoors?",
                "options": [
                    "Red light is the only color that can shine through paper",
                    "Red light does not disrupt dark adaptation of human eye rod cells, preserving night vision",
                    "Red light creates artificial heat that keeps the astronomer warm",
                    "White light is illegal during the night hours"
                ],
                "correct": 1,
                "explanation": "Human eye rods (sensitive to low light) are insensitive to deep red wavelengths, allowing charts to be read without bleaching rhodopsin or resetting dark adaptation.",
                "study_insight": "Preserving pupil dilation and rhodopsin concentration is essential for spotting faint celestial objects."
            },
            {
                "question": "If you follow the line of Orion's three belt stars towards the northwest (opposite from Sirius), which bright orange-red star do you encounter in Taurus?",
                "options": [
                    "Aldebaran (Rohiņi)",
                    "Polaris",
                    "The Sun",
                    "Alpha Centauri"
                ],
                "correct": 0,
                "explanation": "Tracing Orion's belt northwest leads directly to the red giant star Aldebaran (Rohiņi in Indian astronomy), marking the fiery eye of Taurus the Bull.",
                "study_insight": "Orion's belt acts as a two-way celestial pointer: southeast to Sirius, northwest to Aldebaran."
            }
        ]
    },
    {
        "id": 7,
        "title": "Solar Heart",
        "subtitle": "The Sun at 1 Astronomical Unit (AU), Thermonuclear Fusion & Proxima Centauri",
        "concept_html": """
            <p>Our Solar System is anchored by an extraordinary stellar engine: the <strong>Sun</strong>. The Sun is not a planet; it is an average-sized, yellow dwarf main-sequence <strong>star</strong> situated at the focal center of our planetary neighborhood.</p>
            <div class='space-y-2 mt-2 text-slate-300'>
                <ul class='list-disc pl-5 space-y-1.5'>
                    <li><strong>Proximity & The Astronomical Unit (AU):</strong> The Sun is our closest star, positioned roughly <strong>150 million kilometers (1.5 × 10⁸ km)</strong> away from Earth. This average Earth-Sun distance is scientifically defined as <strong>1 Astronomical Unit (1 AU)</strong>. Sunlight traveling at 300,000 km/s takes approximately <strong>8 minutes and 20 seconds</strong> to reach Earth!</li>
                    <li><strong>Thermonuclear Powerhouse:</strong> Deep within its core, temperatures reach 15 million degrees Celsius, fusing 600 million tons of hydrogen into helium every second, radiating the heat and light that fuels all terrestrial life.</li>
                    <li><strong>Our Next Stellar Neighbor:</strong> After the Sun, the nearest known star system to Earth is <strong>Proxima Centauri</strong>, located roughly 4.24 light-years (over 40 trillion kilometers) away!</li>
                </ul>
            </div>
        """,
        "spoken_text": "At the very heart of our solar system blazes the Sun. The Sun is our closest star, located approximately one hundred and fifty million kilometers away. In astronomy, this fundamental distance is called one Astronomical Unit. Sunlight travels at three hundred thousand kilometers per second, taking about eight minutes and twenty seconds to reach Earth. Inside the Sun's core, immense pressure and heat fuse hydrogen into helium, generating the light and warmth that sustains all living creatures. After the Sun, the next closest star to Earth is Proxima Centauri, lying over forty trillion kilometers away in deep space.",
        "lecture_script": "At the very heart of our solar system blazes the Sun. The Sun is our closest star, located approximately one hundred and fifty million kilometers away. In astronomy, this fundamental distance is called one Astronomical Unit. Sunlight travels at three hundred thousand kilometers per second, taking about eight minutes and twenty seconds to reach Earth. Inside the Sun's core, immense pressure and heat fuse hydrogen into helium, generating the light and warmth that sustains all living creatures. After the Sun, the next closest star to Earth is Proxima Centauri, lying over forty trillion kilometers away in deep space.",
        "checkpoints": [
            {
                "question": "What is the standard astronomical definition of '1 Astronomical Unit' (1 AU)?",
                "options": [
                    "The distance between the North Pole and the South Pole of Earth",
                    "The average distance from the Earth to the Sun (approx. 150 million kilometers)",
                    "The distance between Earth and the Moon",
                    "The length of time it takes Jupiter to complete one orbit"
                ],
                "correct": 1,
                "explanation": "1 AU is defined as the mean distance between Earth and the Sun, approximately 149.6 million km, used as a yardstick across the Solar System.",
                "study_insight": "Using AU scales down colossal solar system distances into manageable units."
            },
            {
                "question": "Excluding our Sun, which star is closest to planet Earth?",
                "options": [
                    "Sirius",
                    "Betelgeuse",
                    "Proxima Centauri",
                    "Polaris"
                ],
                "correct": 2,
                "explanation": "Proxima Centauri, a red dwarf star in the Alpha Centauri system, is Earth's nearest stellar neighbor at roughly 4.24 light-years distance.",
                "study_insight": "Even traveling at the speed of light, a spacecraft would take over 4 years to reach Proxima Centauri."
            }
        ]
    },
    {
        "id": 8,
        "title": "Rocky Four",
        "subtitle": "The Inner Terrestrial Planets: Mercury, Venus (Runaway Greenhouse), Earth & Mars",
        "concept_html": """
            <p>The four planets closest to the Sun are known as the <strong>Inner Planets (Terrestrial Planets)</strong>. They are characterized by compact sizes, high densities, solid silicate rocky crusts, and metallic iron cores:</p>
            <div class='grid grid-cols-2 sm:grid-cols-4 gap-2 mt-3 text-center'>
                <div class='p-2 rounded-xl bg-slate-900 border border-slate-800'>
                    <div class='text-xs font-bold text-amber-400'>Mercury</div>
                    <p class='text-[10px] text-slate-400 mt-1'>Closest to Sun; cratered, no atmosphere; extreme 430°C day / -180°C night</p>
                </div>
                <div class='p-2 rounded-xl bg-slate-900 border border-slate-800'>
                    <div class='text-xs font-bold text-yellow-300'>Venus</div>
                    <p class='text-[10px] text-slate-400 mt-1'>Brightest; 96% CO₂ runaway greenhouse makes it hottest (465°C); Morning Star</p>
                </div>
                <div class='p-2 rounded-xl bg-slate-900 border border-slate-800'>
                    <div class='text-xs font-bold text-sky-400'>Earth</div>
                    <p class='text-[10px] text-slate-400 mt-1'>Our Blue Planet; liquid water, 21% O₂, protective magnetosphere, flourishing life</p>
                </div>
                <div class='p-2 rounded-xl bg-slate-900 border border-slate-800'>
                    <div class='text-xs font-bold text-rose-400'>Mars</div>
                    <p class='text-[10px] text-slate-400 mt-1'>Red Planet; iron oxide dust; Olympus Mons volcano, polar ice caps, 2 tiny moons</p>
                </div>
            </div>
            <div class='p-3 rounded-xl bg-amber-950/40 border border-amber-500/30 text-xs text-amber-200 mt-3'>
                🌡️ <strong>The Venus Paradox:</strong> Although Mercury is closest to the Sun, Venus is significantly hotter! Venus's dense atmosphere of carbon dioxide and sulfuric acid clouds acts as an impenetrable blanket, trapping solar heat in a ferocious runaway greenhouse effect.
            </div>
        """,
        "spoken_text": "The four planets closest to the Sun are known as the inner terrestrial planets: Mercury, Venus, Earth, and Mars. Unlike the giant outer worlds, these planets are small, dense, and composed of solid rock and metals. Mercury is a cratered, airless world experiencing dramatic temperature extremes. Next is Venus, often called the Morning or Evening Star. Although Mercury is closer to the Sun, Venus is the hottest planet in the solar system, roasting at over four hundred and sixty degrees Celsius because its thick carbon dioxide atmosphere traps heat in an extreme greenhouse effect. Earth is our living blue haven, while Mars glows rust-red due to iron oxide dust across its barren deserts.",
        "lecture_script": "The four planets closest to the Sun are known as the inner terrestrial planets: Mercury, Venus, Earth, and Mars. Unlike the giant outer worlds, these planets are small, dense, and composed of solid rock and metals. Mercury is a cratered, airless world experiencing dramatic temperature extremes. Next is Venus, often called the Morning or Evening Star. Although Mercury is closer to the Sun, Venus is the hottest planet in the solar system, roasting at over four hundred and sixty degrees Celsius because its thick carbon dioxide atmosphere traps heat in an extreme greenhouse effect. Earth is our living blue haven, while Mars glows rust-red due to iron oxide dust across its barren deserts.",
        "checkpoints": [
            {
                "question": "Why is Venus significantly hotter (approx. 465°C) than Mercury, even though Mercury orbits much closer to the Sun?",
                "options": [
                    "Venus has thousands of active nuclear power plants",
                    "Venus has an extremely dense atmosphere of 96% carbon dioxide that traps heat in a runaway greenhouse effect",
                    "Mercury is made entirely of cold liquid ice",
                    "Venus has four suns orbiting around it"
                ],
                "correct": 1,
                "explanation": "Venus's dense CO₂ atmosphere generates an extreme greenhouse effect, trapping solar thermal radiation and raising surface temperatures to 465°C.",
                "study_insight": "Atmospheric composition plays a decisive role in determining planetary surface temperatures."
            },
            {
                "question": "What chemical compound covers the surface of Mars, scattering sunlight to give it its distinctive rust-red appearance?",
                "options": [
                    "Liquid nitrogen",
                    "Iron oxide (rust)",
                    "Copper sulfate crystals",
                    "Chlorophyll algae"
                ],
                "correct": 1,
                "explanation": "The Martian regolith is rich in iron oxide (Fe₂O₃), commonly known as rust, which oxidizes and creates the characteristic red coloration.",
                "study_insight": "Spectroscopic analysis reveals surface mineralogy across celestial bodies."
            }
        ]
    }
]

