"""
Class 6 Science Chapter 12: Beyond Earth
Part 3: 40 Quiz Questions across 4 Mastery Challenge Slides (Slides 17 to 20)
Every question contains id, question, options, answer, explanation, and solution_html.
Zero raw LaTeX. Pure clean Unicode.
"""

QUIZ_QUESTIONS = [
    # Challenge 1: Questions 1 to 10 (Slide 17)
    {
        "id": 1,
        "question": "What is the fundamental scientific difference between a star and a planet?",
        "options": [
            "A star is always made of green solid ice, while a planet is always made of gold",
            "A star generates its own light through thermonuclear fusion in its core, whereas a planet only shines by reflecting starlight",
            "A star orbits around planets, while planets stay stationary in space",
            "A star only shines during morning hours, while planets only appear at midnight"
        ],
        "answer": 1,
        "explanation": "Stars are self-luminous cosmic bodies generating immense electromagnetic radiation via nuclear fusion, while planets are non-luminous bodies reflecting starlight.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Energy Generation:</strong> Stars have high core temperatures (>10 million Kelvin) enabling hydrogen fusion into helium, radiating continuous light and heat.</p>
            <p>2. <strong>Reflected Illumination:</strong> Planets lack the critical mass required to ignite nuclear fusion; their luminosity is purely reflected light from their parent star.</p>
            <p>3. <strong>Conclusion:</strong> Self-luminosity through fusion defines a star (Option B).</p>
        """
    },
    {
        "id": 2,
        "question": "How many officially recognized constellations did the International Astronomical Union (IAU) establish to map the entire sky?",
        "options": [
            "12 constellations",
            "88 constellations",
            "365 constellations",
            "100 constellations"
        ],
        "answer": 1,
        "explanation": "In 1922, the IAU standardized 88 official constellations, partitioning the entire celestial sphere into defined, non-overlapping borders.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Historical Consolidation:</strong> While various cultures identified hundreds of folk constellations, the IAU officially codified 88 modern constellations.</p>
            <p>2. <strong>Spatial Coverage:</strong> Together, these 88 constellations tile the 41,253 square degrees of the celestial sphere without gaps.</p>
            <p>3. <strong>Conclusion:</strong> Exactly 88 constellations (Option B).</p>
        """
    },
    {
        "id": 3,
        "question": "Which prominent star in the constellation Canis Major holds the distinction of being the brightest individual star in the night sky?",
        "options": [
            "Betelgeuse",
            "Sirius (Vyādha)",
            "Polaris",
            "Rigel"
        ],
        "answer": 1,
        "explanation": "Sirius (the Dog Star) has an apparent visual magnitude of -1.46, making it brighter than any other star visible in Earth's night sky.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Visual Magnitude:</strong> Lower (and negative) magnitude values denote greater brightness. Sirius at -1.46 outshines Canopus (-0.74) and Alpha Centauri (-0.27).</p>
            <p>2. <strong>Physical Basis:</strong> Sirius is both intrinsically luminous (25 times more luminous than our Sun) and relatively close to Earth (~8.6 light-years).</p>
            <p>3. <strong>Conclusion:</strong> Sirius is the brightest night star (Option B).</p>
        """
    },
    {
        "id": 4,
        "question": "How can an observer on a clear winter night easily locate the brilliant star Sirius using the constellation Orion?",
        "options": [
            "By drawing a line straight through the three belt stars of Orion and extending it toward the southeast",
            "By looking directly beneath the North Pole Star",
            "By finding the Moon and looking 180 degrees opposite",
            "By tracing the tail of the Big Dipper backwards"
        ],
        "answer": 0,
        "explanation": "Tracing an imaginary line along the three prominent stars of Orion's Belt towards the southeast points directly to dazzling Sirius in Canis Major.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Asterism Signpost:</strong> Orion's Belt (Alnitak, Alnilam, Mintaka) forms a prominent three-star alignment in the winter sky.</p>
            <p>2. <strong>Pointer Vector:</strong> Extending this belt line downward to the southeast leads directly to brilliant blue-white Sirius.</p>
            <p>3. <strong>Conclusion:</strong> Trace Orion's belt southeast (Option A).</p>
        """
    },
    {
        "id": 5,
        "question": "Which red supergiant star marks the prominent shoulder of the celestial hunter in the constellation Orion, known as 'Ārdrā' in Indian astronomy?",
        "options": [
            "Rigel",
            "Betelgeuse",
            "Aldebaran",
            "Polaris"
        ],
        "answer": 1,
        "explanation": "Betelgeuse (Alpha Orionis) is a colossal red supergiant star marking Orion's right shoulder, celebrated as the nakshatra Ārdrā in Indian traditional astronomy.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Stellar Characteristics:</strong> Betelgeuse is an aging red supergiant so vast that if placed at the center of our solar system, its surface would engulf the orbit of Mars!</p>
            <p>2. <strong>Indian Astronomy:</strong> It is revered as the 6th lunar Nakshatra, named Ārdrā.</p>
            <p>3. <strong>Conclusion:</strong> Betelgeuse (Option B).</p>
        """
    },
    {
        "id": 6,
        "question": "Why does the Pole Star (Dhruva Tārā) appear almost completely stationary throughout the night while all other stars appear to rotate?",
        "options": [
            "Because the Pole Star is frozen inside an iceberg at the North Pole",
            "Because it lies almost directly in line with Earth's northern axis of rotation",
            "Because the Pole Star is a reflection of streetlights in the clouds",
            "Because Earth only rotates under the southern stars"
        ],
        "answer": 1,
        "explanation": "Earth rotates on an imaginary axis extending through the North and South Poles. The Pole Star sits virtually at the northern celestial pole, so planetary spin does not alter its position.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Diurnal Motion:</strong> As Earth rotates from west to east, stars appear to trace concentric circular arcs around the celestial poles.</p>
            <p>2. <strong>Axial Alignment:</strong> Polaris is located within 0.7 degrees of the true northern rotational axis, meaning its apparent circular orbit is virtually imperceptible to the naked eye.</p>
            <p>3. <strong>Conclusion:</strong> Aligned with Earth's northern rotational axis (Option B).</p>
        """
    },
    {
        "id": 7,
        "question": "In Activity 12.2, which two stars in the Big Dipper (Ursa Major / Saptarishi) are designated as 'Pointer Stars' to find the Pole Star?",
        "options": [
            "The two stars at the end of the ladle's handle",
            "The two stars on the outer edge of the ladle's bowl (Merak and Dubhe)",
            "The central star inside the ladle's bowl",
            "The three stars of Orion's Belt"
        ],
        "answer": 1,
        "explanation": "The two outer stars of the Big Dipper's bowl (Merak and Dubhe) point in a straight line directly towards Polaris at roughly five times their separation distance.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Asterism Geometry:</strong> Ursa Major includes the 7-star Big Dipper. Four stars form the bowl, three form the curved handle.</p>
            <p>2. <strong>Pointer Method:</strong> A straight line extending upward from Merak through Dubhe leads directly to Polaris (the tip of Ursa Minor's tail).</p>
            <p>3. <strong>Conclusion:</strong> The outer edge stars of the bowl (Option B).</p>
        """
    },
    {
        "id": 8,
        "question": "In various Indian rural and tribal folk traditions, how was the distinctive seven-star constellation of the Big Dipper imaginatively perceived?",
        "options": [
            "As an electric train running across a track",
            "As an elderly grandmother's cot (khatiyā) with three thieves sneaking away, or an anchored fishing boat",
            "As a flying aeroplane with passenger windows",
            "As a solid concrete skyscraper"
        ],
        "answer": 1,
        "explanation": "Indian oral folklore often characterized the 4 bowl stars as a grandmother's charpai (cot) and the 3 handle stars as thieves sneaking away, or as a boat navigating heavenly waters.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Cultural Ethnoastronomy:</strong> Diverse Indian folklore integrated star patterns into daily life stories: the four bedposts of an elder's cot (*khatiyā*) and three pursuing thieves.</p>
            <p>2. <strong>Classical Tradition:</strong> In Vedic tradition, the same seven stars represent the revered Seven Sages (Saptarishi).</p>
            <p>3. <strong>Conclusion:</strong> Option B captures these indigenous folk traditions.</p>
        """
    },
    {
        "id": 9,
        "question": "What happens to the apparent altitude (height in degrees above the northern horizon) of the Pole Star as an observer travels from the Equator northward toward the North Pole?",
        "options": [
            "The Pole Star drops below the horizon and disappears completely",
            "The Pole Star's altitude above the northern horizon increases, exactly matching the observer's geographic latitude",
            "The Pole Star turns into the planet Mars",
            "The Pole Star spins around the Moon every minute"
        ],
        "answer": 1,
        "explanation": "By spherical geometry, the angular height of Polaris above the northern horizon precisely equals the observer's geographic northern latitude (0° at Equator, 90° at North Pole).",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Latitude Metric:</strong> At the Equator (0° N), Polaris sits on the northern horizon (0° altitude). In Delhi (28.6° N), Polaris is ~28.6° high. At the North Pole (90° N), it is at the zenith (90°).</p>
            <p>2. <strong>Navigational Value:</strong> Ancient navigators measured the Pole Star's altitude using astrolabes or sextants to calculate their exact latitude at sea.</p>
            <p>3. <strong>Conclusion:</strong> Altitude increases to match geographic latitude (Option B).</p>
        """
    },
    {
        "id": 10,
        "question": "Which of the following nakshatras in Indian astronomy corresponds to the fiery red giant star Aldebaran in the constellation Taurus?",
        "options": [
            "Rohiņi",
            "Ārdrā",
            "Krittikā",
            "Ashwini"
        ],
        "answer": 0,
        "explanation": "Aldebaran (Alpha Tauri), marking the eye of Taurus, is the prominent red giant star known as the Nakshatra Rohiņi in Indian astronomy.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Nakshatra Matching:</strong></p>
            <p>- <em>Rohiņi</em> = Aldebaran (in Taurus)</p>
            <p>- <em>Ārdrā</em> = Betelgeuse (in Orion)</p>
            <p>- <em>Krittikā</em> = Pleiades star cluster</p>
            <p>2. <strong>Conclusion:</strong> Rohiņi corresponds to Aldebaran (Option A).</p>
        """
    },

    # Challenge 2: Questions 11 to 20 (Slide 18)
    {
        "id": 11,
        "question": "What is 'light pollution', and why does it severely hinder astronomical stargazing in modern metropolitan cities?",
        "options": [
            "It is sunlight that turns the night into boiling steam",
            "Excessive, poorly directed artificial urban lighting scatters across atmospheric air and dust, creating a luminous skyglow that drowns out faint stars",
            "Light pollution is when stars shine too brightly and hurt human eyes",
            "It is the sound of thunder interfering with telescope radio signals"
        ],
        "answer": 1,
        "explanation": "Unshielded urban artificial light reflects and scatters off atmospheric particles, creating artificial skyglow that reduces the contrast between stars and the night sky.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Rayleigh & Mie Scattering:</strong> Upward artificial streetlights and neon signs bounce off airborne gas molecules and aerosols, producing an illuminated dome over cities.</p>
            <p>2. <strong>Contrast Loss:</strong> Faint stars and the Milky Way require high contrast against an ink-black sky. Urban skyglow elevates background brightness, obscuring all but the brightest stars and planets.</p>
            <p>3. <strong>Conclusion:</strong> Option B describes artificial skyglow and contrast loss.</p>
        """
    },
    {
        "id": 12,
        "question": "Where is the Indian Astronomical Observatory and India's first designated Dark Sky Reserve located?",
        "options": [
            "Marina Beach, Chennai",
            "Hanle, Eastern Ladakh",
            "Gateway of India, Mumbai",
            "Victoria Memorial, Kolkata"
        ],
        "answer": 1,
        "explanation": "The Hanle Dark Sky Reserve is located at Hanle in Eastern Ladakh at an altitude of 4,500 meters, home to the Himalayan Chandra Telescope.",
        "solution_html": "<p><strong>Step-by-step Astronomical Verification:</strong></p><p>1. <strong>Location Selection:</strong> Large professional optical and infrared telescopes require high elevation, dry air, cloud-free nights, and dark skies far from city lights.</p><p>2. <strong>Hanle:</strong> Located in Eastern Ladakh at 4,500 m above sea level, Hanle houses the Indian Astronomical Observatory and was officially established as India's first Dark Sky Reserve.</p>"
    },
    {
        "id": 13,
        "question": "Why must an amateur astronomer wait about 20 to 30 minutes in complete darkness before starting to observe faint stars?",
        "options": [
            "To allow the telescope glass to cool down to sub-zero temperatures",
            "To allow human eyes to adapt to darkness by dilating pupils and synthesizing the sensitive vision pigment rhodopsin",
            "Because stars only appear 30 minutes after sunset",
            "To allow the Moon to hide behind the clouds"
        ],
        "answer": 1,
        "explanation": "Dark adaptation requires ~20 to 30 minutes for retinal rod cells to accumulate rhodopsin and for pupils to dilate fully, increasing visual light sensitivity by up to 10,000 times.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Photoreceptor Physiology:</strong> Bright light bleaches the rod pigment rhodopsin. In darkness, rhodopsin regenerates gradually.</p>
            <p>2. <strong>Pupillary Response:</strong> Pupils dilate from ~2 mm in daylight to ~7 mm in darkness, allowing significantly more photons to hit the retina.</p>
            <p>3. <strong>Conclusion:</strong> Dark adaptation takes 20 to 30 minutes (Option B).</p>
        """
    },
    {
        "id": 14,
        "question": "What is the primary scientific reason for using a red flashlight rather than a white flashlight while reading star charts outdoors?",
        "options": [
            "Red light is visible from Mars, alerting other astronomers",
            "Red light does not bleach retinal rhodopsin, preserving human night-vision dark adaptation",
            "Red light changes the temperature of the paper star chart",
            "White light attracts nocturnal bears and wolves"
        ],
        "answer": 1,
        "explanation": "Retinal rod cells responsible for night vision are insensitive to longer red wavelengths (>650 nm), allowing charts to be read without resetting dark adaptation.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Spectral Sensitivity:</strong> Human rod cells peak in sensitivity near 500 nm (blue-green) and drop to near zero in the deep red spectrum.</p>
            <p>2. <strong>Night Vision Protection:</strong> Dim red light is detected primarily by cone cells in the fovea, leaving rod cells unbleached so dark vision is maintained.</p>
            <p>3. <strong>Conclusion:</strong> Red light preserves night vision (Option B).</p>
        """
    },
    {
        "id": 15,
        "question": "What is the average distance from the Earth to the Sun, and what standard astronomical unit does it define?",
        "options": [
            "About 384,400 km; defined as 1 Lunar Distance",
            "Approximately 150 million kilometers (1.5 × 10⁸ km); defined as 1 Astronomical Unit (1 AU)",
            "About 1,000 km; defined as 1 Light-Year",
            "About 40 trillion km; defined as 1 Parsec"
        ],
        "answer": 1,
        "explanation": "1 Astronomical Unit (1 AU) is defined as the mean distance between Earth and the Sun, equal to approximately 149,597,870.7 kilometers (~150 million km).",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Definition:</strong> 1 AU represents the mean semi-major axis of Earth's orbit around the Sun (~150 million km).</p>
            <p>2. <strong>Light Travel Time:</strong> Traveling at c = 300,000 km/s: Time = (150,000,000 km) / (300,000 km/s) = 500 seconds = 8 minutes and 20 seconds.</p>
            <p>3. <strong>Conclusion:</strong> Approx. 150 million km = 1 AU (Option B).</p>
        """
    },
    {
        "id": 16,
        "question": "Approximately how long does it take for sunlight traveling across space at 300,000 km/s to reach the surface of Earth?",
        "options": [
            "Instantaneously (0 seconds)",
            "About 8 minutes and 20 seconds (approx. 500 seconds)",
            "Exactly 24 hours",
            "Approximately one full year"
        ],
        "answer": 1,
        "explanation": "Sunlight traveling at the speed of light (300,000 km/s) traverses the 150 million kilometer distance to Earth in approximately 500 seconds (8 minutes and 20 seconds).",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Formula:</strong> Time = Distance / Speed.</p>
            <p>2. <strong>Calculation:</strong> Time = (1.496 × 10⁸ km) / (3.0 × 10⁵ km/s) = 499 seconds ≈ 8 minutes and 19 to 20 seconds.</p>
            <p>3. <strong>Conclusion:</strong> ~8 minutes and 20 seconds (Option B).</p>
        """
    },
    {
        "id": 17,
        "question": "Which star is our closest stellar neighbor in the universe after the Sun?",
        "options": [
            "Sirius",
            "Proxima Centauri",
            "Betelgeuse",
            "Polaris"
        ],
        "answer": 1,
        "explanation": "Proxima Centauri is a red dwarf star in the Alpha Centauri system located approximately 4.24 light-years (roughly 40 trillion km) from Earth.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Stellar Proximity:</strong> While the Sun is at 1 AU (0.0000158 light-years), the next closest star is Proxima Centauri at 4.246 light-years.</p>
            <p>2. <strong>Comparison:</strong> Sirius is at 8.6 light-years, Polaris is at ~430 light-years, and Betelgeuse is at ~640 light-years.</p>
            <p>3. <strong>Conclusion:</strong> Proxima Centauri (Option B).</p>
        """
    },
    {
        "id": 18,
        "question": "Which planet is the hottest in the Solar System, and why does its temperature exceed that of Mercury despite being farther from the Sun?",
        "options": [
            "Mars; because of its active red volcanoes",
            "Venus; because its dense atmosphere of 96% carbon dioxide creates a fierce runaway greenhouse effect that traps heat at ~465°C",
            "Jupiter; because it generates heat through nuclear fusion",
            "Mercury; because it is closest to the Sun"
        ],
        "answer": 1,
        "explanation": "Venus's dense carbon dioxide atmosphere with sulfuric acid cloud decks produces a runaway greenhouse effect, trapping surface heat at a blistering 465°C, hotter than Mercury's 430°C.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Mercury's Thermal Reality:</strong> Mercury is airless; its sunlit face reaches 430°C, while its night side drops to -180°C.</p>
            <p>2. <strong>Venusian Greenhouse Blanket:</strong> Venus's surface atmospheric pressure is 92 times Earth's, consisting of 96.5% CO₂. This extreme greenhouse blanket traps heat day and night at ~465°C.</p>
            <p>3. <strong>Conclusion:</strong> Venus is the hottest due to runaway greenhouse trapping (Option B).</p>
        """
    },
    {
        "id": 19,
        "question": "Which characteristic correctly describes the group of planets known as the 'Inner Planets' (Mercury, Venus, Earth, Mars)?",
        "options": [
            "They are giant balls of liquid hydrogen with no solid rock",
            "They are relatively small, dense, and composed predominantly of solid silicate rocks and metallic cores",
            "They all have giant icy rings and over fifty moons each",
            "They have surfaces made of pure frozen methane"
        ],
        "answer": 1,
        "explanation": "Inner terrestrial planets are small, rocky, dense bodies composed of silicate mantles surrounding iron-nickel metallic cores, possessing few or no moons.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Compositional Zoning:</strong> In the hot inner protoplanetary disk, only refractory materials with high melting points (silicates, metals) could condense into solid planets.</p>
            <p>2. <strong>Contrast with Giants:</strong> Volatile gases (hydrogen, helium, ices) were pushed outward past the frost line to form the outer giants.</p>
            <p>3. <strong>Conclusion:</strong> Dense, rocky silicate worlds (Option B).</p>
        """
    },
    {
        "id": 20,
        "question": "Why is Mars famously nicknamed the 'Red Planet'?",
        "options": [
            "Because its surface is covered with burning red coal fires",
            "Because its surface rocks and regolith are rich in iron oxide (rust), which oxidizes and imparts a distinctive reddish-orange hue",
            "Because it reflects the red tail-lights of spacecraft",
            "Because it has an atmosphere made of red neon gas"
        ],
        "answer": 1,
        "explanation": "Mars's crust is rich in iron minerals that have oxidized over geological history into iron(III) oxide (Fe₂O₃, commonly rust), tinting the soil and dust red.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Mineral Chemistry:</strong> Basaltic crust rocks on Mars weathered in the presence of ancient atmospheric oxidants, forming ferric oxide minerals (haematite and rust).</p>
            <p>2. <strong>Global Dust Storms:</strong> Fine ferric oxide particles are lifted by winds into the thin Martian atmosphere, casting a global reddish tint.</p>
            <p>3. <strong>Conclusion:</strong> Surface iron oxide (rust) (Option B).</p>
        """
    },

    # Challenge 3: Questions 21 to 30 (Slide 19)
    {
        "id": 21,
        "question": "Which planet is the largest in our Solar System, featuring the centuries-old cyclonic storm known as the Great Red Spot?",
        "options": [
            "Saturn",
            "Jupiter",
            "Neptune",
            "Earth"
        ],
        "answer": 1,
        "explanation": "Jupiter is the most massive and voluminous planet in the solar system, with a diameter 11 times Earth's and a giant anticyclonic storm called the Great Red Spot.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Massive Scale:</strong> Jupiter contains more mass than all other solar system planets combined (2.5 times total planetary mass).</p>
            <p>2. <strong>The Great Red Spot:</strong> An immense high-pressure storm in Jupiter's southern hemisphere, wider than the diameter of planet Earth, observed for over 300 years.</p>
            <p>3. <strong>Conclusion:</strong> Jupiter (Option B).</p>
        """
    },
    {
        "id": 22,
        "question": "What unique physical property characterizes the gas giant Saturn regarding its average bulk density?",
        "options": [
            "Saturn is denser than pure solid platinum",
            "Saturn has an average density of ~0.69 g/cm³, meaning it is less dense than water and would theoretically float in a colossal bathtub",
            "Saturn is made of heavy lead that sinks in liquid mercury",
            "Saturn's density is infinite because it is a black hole"
        ],
        "answer": 1,
        "explanation": "Composed overwhelmingly of light hydrogen and helium gases, Saturn's bulk density is roughly 0.687 g/cm³, significantly lower than liquid water's 1.0 g/cm³.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Density Calculation:</strong> Density = Mass / Volume. Saturn's mass is ~95 Earth masses, but its enormous volume (~764 Earths) yields a very low mean density of 0.687 g/cm³.</p>
            <p>2. <strong>Theoretical Gedankenexperiment:</strong> Since water has a density of 1.0 g/cm³, Saturn would float if placed in a hypothetical body of water large enough to hold it.</p>
            <p>3. <strong>Conclusion:</strong> Less dense than water (Option B).</p>
        """
    },
    {
        "id": 23,
        "question": "What are the spectacular rings of Saturn primarily composed of?",
        "options": [
            "Solid iron bars welded together by ancient astronauts",
            "Billions of individual chunks of water ice, rocky debris, and dust ranging in size from tiny grains to house-sized boulders",
            "Glowing neon gas tubes",
            "Pure liquid petroleum"
        ],
        "answer": 1,
        "explanation": "Saturn's rings are a vast disk of orbiting particles consisting of 99% pure water ice fragments with minor silicate dust, ranging from micrometers to several meters in diameter.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Ring Dynamics:</strong> The rings span up to 282,000 km in width but are astonishingly paper-thin, typically only 10 to 30 meters thick!</p>
            <p>2. <strong>Composition:</strong> Spectroscopy confirms they are composed of clean, highly reflective water ice fragments resulting from shredded icy comets or moons.</p>
            <p>3. <strong>Conclusion:</strong> Orbiting water ice and rocky fragments (Option B).</p>
        """
    },
    {
        "id": 24,
        "question": "Why does the ice giant Uranus appear cyan (blue-green) in telescope imagery, and what is notable about its axis of rotation?",
        "options": [
            "It is covered in green grass; its axis is completely straight at 0 degrees",
            "Atmospheric methane gas absorbs red light and reflects blue-green light; its rotational axis is tilted by 98 degrees, so it rolls on its side along its orbit",
            "It has blue oceans of fresh drinking water; it does not rotate at all",
            "It is painted with synthetic blue enamel"
        ],
        "answer": 1,
        "explanation": "Atmospheric methane absorbs red photons, giving Uranus its cyan hue. Its extreme 97.8° axial tilt causes it to orbit the Sun on its side.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Color Origin:</strong> Upper atmospheric methane (CH₄) gas selectively absorbs red wavelengths of sunlight while scattering and reflecting blue and green light.</p>
            <p>2. <strong>Orbital Geometry:</strong> An ancient giant impact knocked Uranus onto its side (97.8° tilt), resulting in extreme 42-year polar seasons.</p>
            <p>3. <strong>Conclusion:</strong> Methane cyan color and rolls on its side (Option B).</p>
        """
    },
    {
        "id": 25,
        "question": "Which of the following is an official criterion established by the IAU in 2006 for a celestial body to be classified as a full planet?",
        "options": [
            "It must have at least ten human space stations on its surface",
            "It must orbit the Sun, be pulled into a nearly spherical shape by self-gravity, and have cleared the neighborhood around its orbit",
            "It must be made entirely of solid diamond",
            "It must possess active green plant life"
        ],
        "answer": 1,
        "explanation": "The 2006 IAU definition requires three conditions: (1) Sun orbit, (2) hydrostatic equilibrium (spherical shape), and (3) cleared its orbital neighborhood of debris.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>IAU Resolution 5A:</strong> Formalized criteria to distinguish classical planets from dwarf planets and small solar system bodies.</p>
            <p>2. <strong>The Three Tests:</strong> Orbit the Sun, attain hydrostatic roundness, and gravitationally dominate/clear its orbital zone.</p>
            <p>3. <strong>Conclusion:</strong> Option B states the complete threefold definition.</p>
        """
    },
    {
        "id": 26,
        "question": "Why did the International Astronomical Union (IAU) reclassify Pluto from a planet to a 'dwarf planet' in 2006?",
        "options": [
            "Pluto stopped revolving around the Sun",
            "Pluto failed to clear the neighborhood around its orbit, sharing its orbital path with thousands of icy Kuiper Belt objects",
            "Pluto melted into liquid water and evaporated",
            "Pluto's color changed from blue to pink"
        ],
        "answer": 1,
        "explanation": "Pluto's mass is far too small to gravitationally clear its orbital zone; it orbits within the crowded Kuiper Belt and periodically crosses Neptune's orbit.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Dynamical Dominance:</strong> A true planet clears its orbital zone by accreting, ejecting, or locking debris into resonance. Earth is 1.7 million times the mass of other debris in its zone.</p>
            <p>2. <strong>Pluto's Ratio:</strong> Pluto is only 0.07 times the mass of other objects in its zone, sharing its space with thousands of Kuiper Belt bodies.</p>
            <p>3. <strong>Conclusion:</strong> Failed to clear its neighborhood (Option B).</p>
        """
    },
    {
        "id": 27,
        "question": "What causes the apparent visual 'twinkling' (scintillation) of distant stars when viewed through Earth's atmosphere?",
        "options": [
            "Stars physically pulsate and explode ten times every second",
            "Light from point-source stars passes through turbulent atmospheric layers of varying temperatures and densities, causing continuous refraction and flickering",
            "Air molecules inside human eyeballs vibrate when looking at stars",
            "The Moon casts high-speed shadows across starlight"
        ],
        "answer": 1,
        "explanation": "Atmospheric turbulence creates pockets of air with shifting refractive indices that continuously bend starlight rays, causing rapid shifts in brightness and position.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Point-Source Geometry:</strong> Due to extreme distances, starlight arrives as a near-perfect single ray of light.</p>
            <p>2. <strong>Refractive Fluctuations:</strong> Atmospheric wind currents create thermal gradients, deflecting the ray rapidly in random directions (scintillation).</p>
            <p>3. <strong>Conclusion:</strong> Atmospheric refraction of point-source light (Option B).</p>
        """
    },
    {
        "id": 28,
        "question": "Why do planets like Venus, Mars, and Jupiter appear to shine with a calm, steady light rather than twinkling like stars?",
        "options": [
            "Planets are equipped with giant electric battery lights",
            "Planets are much closer to Earth, appearing as extended disks of light where multiple flickering points average out to zero net scintillation",
            "Planets only shine when Earth's atmosphere is completely frozen",
            "Planets emit sound waves that cancel air turbulence"
        ],
        "answer": 1,
        "explanation": "Because planets are relatively close, they subtend measurable angular disks. Different points across the disk scintillate out of phase, canceling each other out into a steady glow.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Extended Source vs. Point Source:</strong> A planetary disk acts as an array of millions of adjacent light points.</p>
            <p>2. <strong>Statistical Averaging:</strong> When atmospheric turbulence dims light from one edge of the disk, it brightens light from another edge. The integrated light flux remains constant.</p>
            <p>3. <strong>Conclusion:</strong> Extended disk averages out scintillation (Option B).</p>
        """
    },
    {
        "id": 29,
        "question": "Approximately how many days does it take for the Moon to complete one full revolution around the Earth?",
        "options": [
            "24 hours",
            "Approximately 27.3 days",
            "365.25 days",
            "100 days"
        ],
        "answer": 1,
        "explanation": "The Moon completes one orbital revolution around Earth relative to background stars (sidereal month) in approximately 27.3 days.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Sidereal Orbit:</strong> The Moon orbits Earth once every 27.32 days relative to the fixed stars.</p>
            <p>2. <strong>Synodic Month:</strong> Because Earth also orbits the Sun, completing a full cycle of lunar phases (new moon to new moon) takes 29.53 days.</p>
            <p>3. <strong>Conclusion:</strong> Approximately 27.3 days (Option B).</p>
        """
    },
    {
        "id": 30,
        "question": "Why are impact craters so abundant and sharply preserved on the Moon compared to Earth?",
        "options": [
            "The Moon is made of soft clay that dented easily when young",
            "The Moon lacks an atmosphere, liquid water, active plate tectonics, and wind to weather, erode, or bury surface craters",
            "Alien spaceships built all the craters as landing docks",
            "Earth has never been struck by any meteorites in its history"
        ],
        "answer": 1,
        "explanation": "Without an atmosphere to burn incoming space rocks, and without wind, rainfall, or tectonic subduction to erode surface topography, lunar craters remain pristine for billions of years.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Absence of Weathering:</strong> Earth possesses an active hydrological cycle, wind erosion, vegetation, and volcanic recycling that constantly erase craters.</p>
            <p>2. <strong>Lunar Stasis:</strong> The geologically inactive, airless, dry Moon preserves ancient impact craters as a cosmic fossil record of solar system history.</p>
            <p>3. <strong>Conclusion:</strong> Lack of atmosphere, erosion, and water (Option B).</p>
        """
    },

    # Challenge 4: Questions 31 to 40 (Slide 20)
    {
        "id": 31,
        "question": "What historic scientific discovery was made on the lunar surface by India's Chandrayaan-1 orbiter mission in 2008?",
        "options": [
            "Discovery of active volcanic magma lakes",
            "Definitive detection of water molecules (H₂O) and hydroxyl ions trapped in the polar lunar regolith",
            "Discovery of alien radio transmission towers",
            "Discovery of diamond glaciers in lunar craters"
        ],
        "answer": 1,
        "explanation": "Chandrayaan-1's Moon Mineralogy Mapper (M3) detected diagnostic 3.0-micrometer infrared absorption bands proving the widespread presence of water and hydroxyl in lunar soil.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Historic Breakthrough:</strong> Prior to Chandrayaan-1, the Moon was widely presumed to be bone-dry. The mission discovered water molecules adsorbed onto lunar mineral grains.</p>
            <p>2. <strong>Moon Impact Probe (MIP):</strong> On November 14, 2008, the MIP instrument confirmed water vapour in the thin lunar exosphere during descent.</p>
            <p>3. <strong>Conclusion:</strong> Direct detection of water molecules (Option B).</p>
        """
    },
    {
        "id": 32,
        "question": "On August 23, 2023, India achieved a historic first in space exploration with Chandrayaan-3. What was this milestone?",
        "options": [
            "First nation to land human astronauts on Mars",
            "First nation to successfully soft-land a robotic spacecraft (Vikram lander & Pragyan rover) near the uncharted South Pole of the Moon",
            "First nation to build a hotel on the Moon",
            "First nation to capture a piece of the Sun"
        ],
        "answer": 1,
        "explanation": "Chandrayaan-3 made India the first nation in history to execute a soft landing in the rugged, shadowed lunar south polar region.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>South Polar Triumph:</strong> The lunar south pole is scientifically coveted due to permanently shadowed craters holding water ice reservoirs.</p>
            <p>2. <strong>National Space Day:</strong> In honor of this milestone, August 23rd was officially declared India's National Space Day.</p>
            <p>3. <strong>Conclusion:</strong> First soft-landing near lunar south pole (Option B).</p>
        """
    },
    {
        "id": 33,
        "question": "What were the official names of the lander and rover modules of India's historic Chandrayaan-3 mission?",
        "options": [
            "Vikram (Lander) and Pragyan (Rover)",
            "Pushpak (Lander) and Rakesh (Rover)",
            "Aryabhata (Lander) and Rohini (Rover)",
            "Mangal (Lander) and Aditya (Rover)"
        ],
        "answer": 0,
        "explanation": "The Chandrayaan-3 landing module was named Vikram (honoring Dr. Vikram Sarabhai, father of the Indian space program) and the 6-wheeled robotic rover was named Pragyan (meaning wisdom).",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Vikram Lander:</strong> Contained hazard detection cameras and throttleable thrusters to achieve safe touchdown.</p>
            <p>2. <strong>Pragyan Rover:</strong> 26 kg solar-powered rover equipped with APXS and LIBS spectrometers to assay lunar elemental soil composition.</p>
            <p>3. <strong>Conclusion:</strong> Vikram and Pragyan (Option A).</p>
        """
    },
    {
        "id": 34,
        "question": "Where is the main Asteroid Belt situated within our Solar System?",
        "options": [
            "Between the orbits of Mars and Jupiter",
            "Between Mercury and Venus",
            "Beyond the orbit of Pluto",
            "Between Earth and the Moon"
        ],
        "answer": 0,
        "explanation": "The main asteroid belt forms a circumstellar toroidal ring between the orbits of the inner rocky planet Mars and the outer gas giant Jupiter.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Orbital Demarcation:</strong> Located roughly 2.2 to 3.2 AU from the Sun, it marks the boundary between terrestrial rocky planets and Jovian gas giants.</p>
            <p>2. <strong>Content:</strong> Contains millions of rocky bodies, including dwarf planet Ceres and large asteroids Vesta, Pallas, and Hygiea.</p>
            <p>3. <strong>Conclusion:</strong> Between Mars and Jupiter (Option A).</p>
        """
    },
    {
        "id": 35,
        "question": "What is the primary physical composition of a comet's solid core (nucleus)?",
        "options": [
            "Solid molten lava and iron",
            "Frozen water ice, dry ice (carbon dioxide), methane, ammonia, and embedded dark rocky organic dust ('dirty snowball')",
            "Liquid petrol and diesel fuel",
            "Pure polished glass"
        ],
        "answer": 1,
        "explanation": "A comet nucleus is an icy conglomeration of frozen volatile gases (water, CO, CO₂, CH₄) interspersed with mineral silicates and refractory organic dust.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Whipple's Model:</strong> Astronomer Fred Whipple famously termed comet nuclei 'dirty snowballs'.</p>
            <p>2. <strong>Deep Freeze:</strong> Formed in the frigid outer reaches (Kuiper Belt and Oort Cloud), comets preserve primordial matter from the solar system's birth.</p>
            <p>3. <strong>Conclusion:</strong> Frozen ices mixed with rocky organic dust (Option B).</p>
        """
    },
    {
        "id": 36,
        "question": "Why does the luminous tail of a comet always point directly away from the Sun, even when the comet is moving away from the Sun?",
        "options": [
            "Because solar gravity repels ice crystals",
            "Because solar radiation pressure (photons) and the outward stream of charged particles (solar wind) constantly push sublimated gas and dust away from the Sun",
            "Because the tail is pulled towards the North Pole Star",
            "Because comets have jet engines pointed backwards"
        ],
        "answer": 1,
        "explanation": "Solar wind and sunlight photon radiation pressure exert outward repulsive forces on sublimated coma ions and micro-dust, blowing them anti-sunward.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Dual Tails:</strong> Comets exhibit an ion (plasma) tail pointed straight away along solar wind magnetic field lines, and a curved dust tail lagging behind along its orbital path.</p>
            <p>2. <strong>Anti-Sunward Vector:</strong> Both tails point generally away from the Sun regardless of the comet's travel direction.</p>
            <p>3. <strong>Conclusion:</strong> Pushed by solar wind and radiation pressure (Option B).</p>
        """
    },
    {
        "id": 37,
        "question": "What is the orbital period of the famous Halley's Comet, and in which year is it next predicted to return to perihelion near Earth?",
        "options": [
            "Every 10 years; next expected in 2030",
            "Approximately every 75 to 76 years; next expected to appear in the year 2061",
            "Every 365 days; next expected tomorrow",
            "Once every 1,000 years; next expected in 3000"
        ],
        "answer": 1,
        "explanation": "Halley's Comet has an orbital period of roughly 75 to 76 years. It last reached perihelion in early 1986 and will return to perihelion in mid-2061.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Orbital Mechanics:</strong> Halley travels out beyond Neptune's orbit (aphelion ~35 AU) before gravity pulls it back toward the Sun (perihelion ~0.59 AU).</p>
            <p>2. <strong>Timeline:</strong> 1986 + 75.3 years ≈ 2061.</p>
            <p>3. <strong>Conclusion:</strong> ~75–76 years, returning in 2061 (Option B).</p>
        """
    },
    {
        "id": 38,
        "question": "What type of galaxy is our home galaxy, the Milky Way (Ākāśha Gangā), and how many stars does it approximately contain?",
        "options": [
            "A tiny spherical dwarf galaxy containing only three stars",
            "A giant barred spiral galaxy spanning over 100,000 light-years across, containing between 100 to 400 billion stars",
            "A flat square galaxy containing only our Sun and the Moon",
            "A dark cloud of dust containing zero stars"
        ],
        "answer": 1,
        "explanation": "The Milky Way is a barred spiral galaxy with a central stellar bar and spiral arms, spanning roughly 100,000 light-years and housing over 200 billion stars.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Galactic Architecture:</strong> Our Solar System is situated in the Orion-Cygnus spur of the Sagittarius spiral arm, roughly 26,000 light-years from the galactic supermassive black hole (Sagittarius A*).</p>
            <p>2. <strong>Stellar Population:</strong> Estimates place the stellar count between 100 and 400 billion stars.</p>
            <p>3. <strong>Conclusion:</strong> Barred spiral galaxy with hundreds of billions of stars (Option B).</p>
        """
    },
    {
        "id": 39,
        "question": "What astronomical term refers to a planet that orbits a distant star located outside our own Solar System?",
        "options": [
            "An asteroid",
            "An exoplanet (extrasolar planet)",
            "A meteorite",
            "A brown dwarf star"
        ],
        "answer": 1,
        "explanation": "An exoplanet (extrasolar planet) is any planet that revolves around a star other than our Sun in interstellar space.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>Discovery Era:</strong> Since the 1990s, telescopes like Kepler, TESS, and James Webb have confirmed over 5,500 exoplanets across the Milky Way.</p>
            <p>2. <strong>Habitable Zones:</strong> Astronomers specifically search for rocky exoplanets in 'Goldilocks zones' where liquid surface water could exist.</p>
            <p>3. <strong>Conclusion:</strong> An exoplanet (Option B).</p>
        """
    },
    {
        "id": 40,
        "question": "As modern science gazes across the vast observable universe containing over two trillion galaxies, what profound biological reality remains unique to planet Earth?",
        "options": [
            "Earth is the only planet made of solid granite",
            "Earth is currently the ONLY celestial body in the known universe confirmed to harbor and sustain biological life",
            "Earth is the largest planet in the entire universe",
            "Earth is the only planet that possesses gravity"
        ],
        "answer": 1,
        "explanation": "Despite extensive searches across thousands of exoplanets and solar system bodies, Earth remains the sole confirmed haven for biological life in the known cosmos.",
        "solution_html": """
            <h4 class='font-bold text-indigo-300 mb-1'>Detailed Solution:</h4>
            <p>1. <strong>The Cosmic Oasis:</strong> Earth's liquid water, protective magnetosphere, dynamic plate tectonics, and balanced atmospheric oxygen make it uniquely habitable.</p>
            <p>2. <strong>Ecological Imperative:</strong> As Carl Sagan emphasized in his 'Pale Blue Dot' reflection, this uniqueness underscores humanity's responsibility to cherish and protect our fragile planetary home.</p>
            <p>3. <strong>Conclusion:</strong> Earth is the only confirmed haven for life (Option B).</p>
        """
    }
]
