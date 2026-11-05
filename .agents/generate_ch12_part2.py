"""
Class 6 Science Chapter 12: Beyond Earth
Part 2: Slides 9 to 16 Data Module
Headings are short (1-3 words) with exact same meaning. Zero raw LaTeX.
"""

SLIDES_PART2 = [
    {
        "id": 9,
        "title": "Gas Giants",
        "subtitle": "The Majestic Outer Worlds: Jupiter, Saturn's Rings, Uranus & Neptune",
        "concept_html": """
            <p>Beyond the asteroid belt lie the <strong>Outer Planets (Jovian Planets)</strong>. Far larger and more massive than terrestrial worlds, they lack solid surfaces, consisting primarily of deep hydrogen, helium, methane, and water-ammonia atmospheres:</p>
            <div class='grid grid-cols-2 sm:grid-cols-4 gap-2 mt-3 text-center'>
                <div class='p-2 rounded-xl bg-slate-900 border border-slate-800'>
                    <div class='text-xs font-bold text-amber-400'>Jupiter</div>
                    <p class='text-[10px] text-slate-400 mt-1'>Largest planet; Great Red Spot storm, over 90 moons (Ganymede, Io, Europa)</p>
                </div>
                <div class='p-2 rounded-xl bg-slate-900 border border-slate-800'>
                    <div class='text-xs font-bold text-yellow-300'>Saturn</div>
                    <p class='text-[10px] text-slate-400 mt-1'>Spectacular rings of ice and rock; lower density than water; giant moon Titan</p>
                </div>
                <div class='p-2 rounded-xl bg-slate-900 border border-slate-800'>
                    <div class='text-xs font-bold text-teal-300'>Uranus</div>
                    <p class='text-[10px] text-slate-400 mt-1'>Ice giant; cyan methane color; rotates on its side with a 98° axial tilt!</p>
                </div>
                <div class='p-2 rounded-xl bg-slate-900 border border-slate-800'>
                    <div class='text-xs font-bold text-blue-400'>Neptune</div>
                    <p class='text-[10px] text-slate-400 mt-1'>Farthest official planet; deep cobalt blue, supersonic winds (>2,000 km/h)</p>
                </div>
            </div>
            <p class='text-xs text-slate-300 mt-3'>All four outer giants possess systems of planetary rings made of orbiting ice, dust, and boulders, with Saturn's rings being the most prominent and luminous.</p>
        """,
        "spoken_text": "Beyond the asteroid belt lie the four colossal outer planets: Jupiter, Saturn, Uranus, and Neptune. Unlike the rocky inner worlds, these giants are composed primarily of swirling hydrogen, helium, methane, and ice, with no solid surface to walk upon. Jupiter is the undisputed king of planets, so massive that over thirteen hundred Earths could fit inside it, home to the centuries-old Great Red Spot anticyclone. Saturn is famed for its breathtaking, shimmering rings made of billions of icy fragments. Uranus and Neptune are chilly ice giants, with Uranus rotating curiously on its side and Neptune howling with supersonic winds over two thousand kilometers per hour.",
        "lecture_script": "Beyond the asteroid belt lie the four colossal outer planets: Jupiter, Saturn, Uranus, and Neptune. Unlike the rocky inner worlds, these giants are composed primarily of swirling hydrogen, helium, methane, and ice, with no solid surface to walk upon. Jupiter is the undisputed king of planets, so massive that over thirteen hundred Earths could fit inside it, home to the centuries-old Great Red Spot anticyclone. Saturn is famed for its breathtaking, shimmering rings made of billions of icy fragments. Uranus and Neptune are chilly ice giants, with Uranus rotating curiously on its side and Neptune howling with supersonic winds over two thousand kilometers per hour.",
        "checkpoints": [
            {
                "question": "What unique physical property sets Saturn apart from all other planets in our solar system regarding its overall density?",
                "options": [
                    "Saturn is denser than solid gold",
                    "Saturn's average density is less than liquid water (approx. 0.69 g/cm³), meaning it would theoretically float in a colossal ocean",
                    "Saturn is made entirely of compressed lead",
                    "Saturn has zero mass"
                ],
                "correct": 1,
                "explanation": "Composed mostly of light hydrogen and helium gases, Saturn's mean density is roughly 0.687 g/cm³, which is lower than the density of pure water (1.0 g/cm³).",
                "study_insight": "Low density combined with rapid rotation causes Saturn to be visibly flattened at its poles (oblate spheroid)."
            },
            {
                "question": "What unusual rotational characteristic distinguishes the ice giant Uranus from other solar system planets?",
                "options": [
                    "It does not rotate at all",
                    "Its rotational axis is tilted by 98 degrees, so it rolls along its orbital path on its side",
                    "It changes its rotation direction every single day",
                    "It rotates faster than the speed of light"
                ],
                "correct": 1,
                "explanation": "Uranus has an extreme axial tilt of 97.8°, likely caused by a massive protoplanetary collision during the early formation of the Solar System.",
                "study_insight": "Because Uranus rotates on its side, its poles experience 42 years of continuous sunlight followed by 42 years of darkness."
            }
        ]
    },
    {
        "id": 10,
        "title": "Dwarf Worlds",
        "subtitle": "The 2006 IAU Planetary Definition & The Reclassification of Pluto",
        "concept_html": """
            <p>For over seven decades (1930–2006), textbooks listed Pluto as the ninth planet. In 2006, the <strong>International Astronomical Union (IAU)</strong> established three rigorous criteria to define a true planet:</p>
            <div class='p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 space-y-1.5 mt-2'>
                <p>1. Must orbit directly around the Sun.</p>
                <p>2. Must possess sufficient mass for its self-gravity to shape it into a nearly spherical hydrostatic equilibrium shape.</p>
                <p>3. <strong>Must have cleared the neighborhood around its orbit</strong> of other competing debris and planetesimals.</p>
            </div>
            <p class='text-xs text-slate-300 mt-3'>Pluto easily meets Criteria 1 and 2, but <strong>fails Criterion 3</strong>: it orbits inside the crowded Kuiper Belt surrounded by thousands of icy trans-Neptunian bodies. Hence, the IAU reclassified Pluto, along with Ceres (in the asteroid belt) and Eris, as <strong>dwarf planets</strong>.</p>
        """,
        "spoken_text": "For over seventy years, Pluto was celebrated as the ninth planet of our solar system. However, in 2006, the International Astronomical Union established a formal scientific definition of a planet. To be classified as a full planet, an object must orbit the Sun, be pulled into a round spherical shape by its own gravity, and possess enough gravitational muscle to clear its orbital neighborhood of competing debris. While Pluto is spherical and orbits the Sun, it travels through the crowded Kuiper Belt packed with thousands of icy objects. Consequently, the IAU reclassified Pluto, alongside Ceres and Eris, into an exciting new category: dwarf planets.",
        "lecture_script": "For over seventy years, Pluto was celebrated as the ninth planet of our solar system. However, in 2006, the International Astronomical Union established a formal scientific definition of a planet. To be classified as a full planet, an object must orbit the Sun, be pulled into a round spherical shape by its own gravity, and possess enough gravitational muscle to clear its orbital neighborhood of competing debris. While Pluto is spherical and orbits the Sun, it travels through the crowded Kuiper Belt packed with thousands of icy objects. Consequently, the IAU reclassified Pluto, alongside Ceres and Eris, into an exciting new category: dwarf planets.",
        "checkpoints": [
            {
                "question": "Which of the three official IAU planetary criteria did Pluto fail to satisfy, leading to its reclassification as a dwarf planet in 2006?",
                "options": [
                    "It failed to be spherical in shape",
                    "It failed to clear the neighborhood around its orbital path",
                    "It stopped revolving around the Sun",
                    "It lost all its gravitational pull"
                ],
                "correct": 1,
                "explanation": "Pluto's mass is only a fraction of the total mass in its orbital zone; it shares its orbit with thousands of Kuiper Belt objects and periodically crosses Neptune's orbit.",
                "study_insight": "Scientific definitions evolve as new observational technologies discover thousands of previously unknown celestial bodies."
            },
            {
                "question": "Which dwarf planet is located closest to Earth, orbiting inside the main Asteroid Belt between Mars and Jupiter?",
                "options": [
                    "Pluto",
                    "Ceres",
                    "Eris",
                    "Makemake"
                ],
                "correct": 1,
                "explanation": "Ceres is the largest object in the asteroid belt and the only dwarf planet located in the inner Solar System.",
                "study_insight": "Ceres contains roughly one-third of the total mass of the entire asteroid belt."
            }
        ]
    },
    {
        "id": 11,
        "title": "Twinkle or Steady",
        "subtitle": "Atmospheric Scintillation: Why Stars Twinkle While Planets Shine Steadily",
        "concept_html": """
            <p>When you gaze into the night sky, you will notice a fascinating optical distinction: <strong>stars twinkle and shimmer vigorously, whereas bright planets shine with a calm, steady glow</strong>. Why?</p>
            <div class='grid grid-cols-1 md:grid-cols-2 gap-3 mt-3'>
                <div class='p-3 rounded-xl bg-slate-950/70 border border-slate-800'>
                    <h4 class='text-xs font-bold text-amber-400 uppercase'>Why Stars Twinkle</h4>
                    <p class='text-xs text-slate-300 mt-1'>Stars are trillions of kilometers away, acting as microscopic <strong>point sources of light</strong>. As this narrow beam enters Earth's turbulent atmosphere, fluctuating air temperatures and densities continuously refract the beam in zigzags, causing rapid changes in brightness and position (<strong>scintillation</strong>).</p>
                </div>
                <div class='p-3 rounded-xl bg-slate-950/70 border border-slate-800'>
                    <h4 class='text-xs font-bold text-sky-400 uppercase'>Why Planets Shine Steadily</h4>
                    <p class='text-xs text-slate-300 mt-1'>Planets are much closer to Earth, appearing through telescopes as <strong>extended optical disks</strong> composed of millions of adjacent light points. The atmospheric flickering of different points averages out, neutralizing scintillation into a solid, unwavering beam!</p>
                </div>
            </div>
        """,
        "spoken_text": "Have you ever wondered why stars twinkle like diamonds while planets shine with a calm, steady light? The secret lies in Earth's atmosphere. Because stars are trillions of kilometers away, their light arrives as a microscopic, hair-thin point of light. As this delicate beam passes through fluctuating layers of hot and cold atmospheric winds, it gets continuously bent and refracted, making the star appear to flicker and twinkle. Planets, on the other hand, are much closer to Earth. They appear as larger extended disks of light. The atmospheric fluctuations from different edges cancel each other out, giving planets their calm, steady glow.",
        "lecture_script": "Have you ever wondered why stars twinkle like diamonds while planets shine with a calm, steady light? The secret lies in Earth's atmosphere. Because stars are trillions of kilometers away, their light arrives as a microscopic, hair-thin point of light. As this delicate beam passes through fluctuating layers of hot and cold atmospheric winds, it gets continuously bent and refracted, making the star appear to flicker and twinkle. Planets, on the other hand, are much closer to Earth. They appear as larger extended disks of light. The atmospheric fluctuations from different edges cancel each other out, giving planets their calm, steady glow.",
        "checkpoints": [
            {
                "question": "What causes the apparent visual 'twinkling' of distant stars when viewed from Earth's surface?",
                "options": [
                    "Stars turning on and off their nuclear cores every second",
                    "Atmospheric refraction of narrow point-source starlight passing through turbulent air layers of varying temperatures and densities",
                    "Swallows flying rapidly in front of the telescope lenses",
                    "The rotation of the Moon casting fast shadows"
                ],
                "correct": 1,
                "explanation": "Atmospheric scintillation occurs because turbulent, moving pockets of air with changing refractive indices constantly deflect narrow starlight beams.",
                "study_insight": "In the vacuum of outer space (e.g., viewed from the Hubble or James Webb telescopes), stars do not twinkle at all."
            },
            {
                "question": "Why do planets like Venus and Jupiter appear as steady, non-twinkling disks of light to the naked eye?",
                "options": [
                    "Because planets are infinitely farther away than any star",
                    "Because their relative proximity makes them extended sources of light where multiple flickering points average out to zero net scintillation",
                    "Because planets emit laser beams that pierce through all air clouds",
                    "Because planets are covered with solid glass lenses"
                ],
                "correct": 1,
                "explanation": "Planets subtend a measurable angular diameter; light coming from across the disk averages out atmospheric fluctuations, providing a steady image.",
                "study_insight": "A non-twinkling bright point in the dawn or dusk sky is almost always a planet rather than a star."
            }
        ]
    },
    {
        "id": 12,
        "title": "Moon & Craters",
        "subtitle": "Earth's Natural Satellite: 27.3-Day Orbit, Impact Craters & Vacuum Environment",
        "concept_html": """
            <p>The <strong>Moon</strong> is Earth's only natural satellite, orbiting at an average distance of roughly 384,400 km. It completes one revolution around Earth in approximately <strong>27.3 days</strong>:</p>
            <div class='space-y-2 mt-2 text-slate-300'>
                <ul class='list-disc pl-5 space-y-1.5'>
                    <li><strong>Synchronous Rotation:</strong> The Moon rotates on its axis in the exact same time it takes to orbit Earth (tidal locking). Consequently, the Moon always presents the <strong>same near side</strong> facing Earth!</li>
                    <li><strong>Impact Craters:</strong> Looking through binoculars reveals thousands of bowl-shaped craters (like Tycho and Copernicus). Because the Moon has <strong>no atmosphere</strong> to burn incoming meteors and zero wind or water to erode soil, crater scars remain perfectly preserved for billions of years!</li>
                    <li><strong>Hostile Environment:</strong> With no protective atmospheric blanket, lunar daytime temperatures soar to 120°C in direct sunlight and plunge to -130°C in shadow. There is no liquid water, no air to breathe, and total silence.</li>
                </ul>
            </div>
        """,
        "spoken_text": "The Moon is Earth's faithful celestial companion, orbiting our planet at a distance of about three hundred and eighty-four thousand kilometers. It takes roughly twenty-seven days to complete one full revolution. Because its rotation speed matches its orbital speed, the Moon always shows the exact same face toward Earth. When viewed through binoculars, the lunar surface is scarred by thousands of impact craters formed by meteorite collisions. Because the Moon lacks an atmosphere, there is no wind, rain, or flowing water to wash these scars away, preserving craters unchanged for billions of years. With no air and extreme temperature swings, the lunar surface is an eerie, silent world.",
        "lecture_script": "The Moon is Earth's faithful celestial companion, orbiting our planet at a distance of about three hundred and eighty-four thousand kilometers. It takes roughly twenty-seven days to complete one full revolution. Because its rotation speed matches its orbital speed, the Moon always shows the exact same face toward Earth. When viewed through binoculars, the lunar surface is scarred by thousands of impact craters formed by meteorite collisions. Because the Moon lacks an atmosphere, there is no wind, rain, or flowing water to wash these scars away, preserving craters unchanged for billions of years. With no air and extreme temperature swings, the lunar surface is an eerie, silent world.",
        "checkpoints": [
            {
                "question": "Why do ancient impact craters on the Moon remain sharp and perfectly preserved for billions of years, unlike craters on Earth?",
                "options": [
                    "Astronauts regularly repair and polish the craters",
                    "The Moon has no atmosphere, wind, or liquid water to erode, weather, or erase surface craters",
                    "The Moon's crust is made of indestructible diamond",
                    "Meteorites on the Moon are made of soft sponge"
                ],
                "correct": 1,
                "explanation": "Without an atmosphere, the Moon experiences zero weather, wind erosion, or water runoff, keeping meteorite impact features pristine over geological eons.",
                "study_insight": "Earth's active tectonic plate movements, vegetation, and hydrologic erosion continually erase terrestrial impact craters."
            },
            {
                "question": "Why does an observer on Earth always see the exact same hemisphere of the Moon facing them?",
                "options": [
                    "The Moon does not rotate on its axis at all",
                    "The Moon's rotational period on its axis precisely matches its orbital period around Earth (synchronous tidal locking)",
                    "The backside of the Moon is invisible black matter",
                    "The Moon is physically attached to Earth by an iron cable"
                ],
                "correct": 1,
                "explanation": "Tidal friction over billions of years locked the Moon's rotation period to its orbital period (27.3 days), ensuring the same face always points toward Earth.",
                "study_insight": "The 'far side' of the Moon was only photographed when human spacecraft orbited behind it in 1959."
            }
        ]
    },
    {
        "id": 13,
        "title": "Touch the Moon",
        "subtitle": "India's Lunar Odyssey: Chandrayaan Missions & National Space Day (August 23)",
        "concept_html": """
            <p>India's space agency, <strong>ISRO (Indian Space Research Organisation)</strong>, has scripted golden chapters in lunar exploration:</p>
            <div class='space-y-2 mt-2 text-slate-300'>
                <ul class='list-disc pl-5 space-y-1.5'>
                    <li><strong>Chandrayaan-1 (2008):</strong> Carried the Moon Impact Probe (MIP) and Moon Mineralogy Mapper (M3). India made the historic breakthrough discovery of <strong>water molecules (H₂O and hydroxyl)</strong> trapped in polar lunar regolith!</li>
                    <li><strong>Chandrayaan-3 (August 23, 2023):</strong> India achieved an unprecedented triumph! The <strong>Vikram lander</strong> executed a flawless soft landing near the uncharted <strong>South Pole of the Moon</strong>, deploying the <strong>Pragyan rover</strong> to conduct on-site soil seismology and elemental composition assays.</li>
                </ul>
                <div class='p-3 rounded-xl bg-amber-950/40 border border-amber-500/30 text-xs text-amber-200 mt-2'>
                    🚀 <strong>National Space Day (August 23rd):</strong> Declared by the Government of India to honor the historic soft-landing of Chandrayaan-3, inspiring generations of Indian students to pursue careers in space science and robotics.
                </div>
            </div>
        """,
        "spoken_text": "India's space journey to the Moon has inspired the entire world. In 2008, ISRO's Chandrayaan-1 mission made the groundbreaking discovery of water molecules on the Moon, reshaping lunar science forever. On August twenty-third, 2023, India achieved historic glory when the Chandrayaan-3 mission executed a flawless soft landing near the Moon's uncharted south pole. As the Vikram lander touched down, the Pragyan rover rolled onto the lunar soil, leaving India's national emblem imprinted in the dust. To celebrate this historic scientific achievement, August twenty-third is proudly observed across our country as National Space Day.",
        "lecture_script": "India's space journey to the Moon has inspired the entire world. In 2008, ISRO's Chandrayaan-1 mission made the groundbreaking discovery of water molecules on the Moon, reshaping lunar science forever. On August twenty-third, 2023, India achieved historic glory when the Chandrayaan-3 mission executed a flawless soft landing near the Moon's uncharted south pole. As the Vikram lander touched down, the Pragyan rover rolled onto the lunar soil, leaving India's national emblem imprinted in the dust. To celebrate this historic scientific achievement, August twenty-third is proudly observed across our country as National Space Day.",
        "checkpoints": [
            {
                "question": "What historic scientific discovery was made on the lunar surface by India's Chandrayaan-1 orbiter mission in 2008?",
                "options": [
                    "Living alien bacteria in volcanic craters",
                    "Direct definitive evidence of water molecules (H₂O) trapped in the lunar regolith",
                    "Extensive underground lakes of liquid petrol",
                    "Fossilized dinosaur bones"
                ],
                "correct": 1,
                "explanation": "Chandrayaan-1's Moon Mineralogy Mapper detected unambiguous infrared spectral absorption signatures of water molecules and hydroxyl on the lunar surface.",
                "study_insight": "Chandrayaan-1 transformed the scientific consensus from a 'bone-dry Moon' to a hydrated celestial body."
            },
            {
                "question": "On which calendar date is National Space Day celebrated annually in India to commemorate the historic soft-landing of Chandrayaan-3 near the lunar South Pole?",
                "options": [
                    "January 26th",
                    "August 23rd",
                    "October 2nd",
                    "November 14th"
                ],
                "correct": 1,
                "explanation": "August 23rd was declared National Space Day to honor the touchdown of the Vikram lander near the lunar south pole on August 23, 2023.",
                "study_insight": "India became the first nation to soft-land near the rugged lunar south polar region."
            }
        ]
    },
    {
        "id": 14,
        "title": "Belt of Rocks",
        "subtitle": "Asteroids: The Rocky Remnants in Orbit Between Mars and Jupiter",
        "concept_html": """
            <p>Between the orbits of Mars and giant Jupiter lies a vast cosmic demolition zone called the <strong>Asteroid Belt</strong>:</p>
            <div class='space-y-2 mt-2 text-slate-300'>
                <p><strong>What Are Asteroids?</strong> Asteroids are small, airless, irregularly shaped rocky and metallic bodies left over from the initial formation of our Solar System 4.6 billion years ago.</p>
                <div class='grid grid-cols-1 md:grid-cols-2 gap-3 mt-2'>
                    <div class='p-3 rounded-xl bg-slate-900 border border-slate-800'>
                        <h4 class='text-xs font-bold text-amber-400 uppercase'>Why Did They Not Form a Planet?</h4>
                        <p class='text-xs text-slate-300 mt-1'>The colossal gravitational tug of neighboring giant Jupiter continuously stirred and accelerated these rocks, causing violent collisions that shattered them rather than letting them coalesce into a single planet!</p>
                    </div>
                    <div class='p-3 rounded-xl bg-slate-900 border border-slate-800'>
                        <h4 class='text-xs font-bold text-sky-400 uppercase'>Composition & Mining Future</h4>
                        <p class='text-xs text-slate-300 mt-1'>Asteroids range in size from tiny pebbles to massive bodies like Ceres (nearly 1,000 km across). They are rich in carbon, silicates, and valuable industrial metals like nickel, iron, and platinum.</p>
                    </div>
                </div>
            </div>
        """,
        "spoken_text": "Between the orbits of Mars and Jupiter lies a vast celestial highway packed with rocky rubble known as the Asteroid Belt. Asteroids are rocky, metallic remnants left over from the birth of our solar system four point six billion years ago. Why didn't these millions of rocks gather together to form a planet? Giant Jupiter's enormous gravitational pull constantly stirred the region, causing ancient rocks to smash into each other rather than fusing together. Asteroids range from tiny pebbles to giant boulders hundreds of kilometers wide, holding valuable clues to the origin of our solar neighborhood.",
        "lecture_script": "Between the orbits of Mars and Jupiter lies a vast celestial highway packed with rocky rubble known as the Asteroid Belt. Asteroids are rocky, metallic remnants left over from the birth of our solar system four point six billion years ago. Why didn't these millions of rocks gather together to form a planet? Giant Jupiter's enormous gravitational pull constantly stirred the region, causing ancient rocks to smash into each other rather than fusing together. Asteroids range from tiny pebbles to giant boulders hundreds of kilometers wide, holding valuable clues to the origin of our solar neighborhood.",
        "checkpoints": [
            {
                "question": "Between which two planetary orbits is the main Asteroid Belt situated in our Solar System?",
                "options": [
                    "Between Earth and Venus",
                    "Between Mars and Jupiter",
                    "Between Saturn and Uranus",
                    "Between Mercury and the Sun"
                ],
                "correct": 1,
                "explanation": "The main asteroid belt occupies the orbital zone roughly 2.1 to 3.3 AU from the Sun, bounded by Mars on the inside and Jupiter on the outside.",
                "study_insight": "Despite movies showing dense swarms, asteroid belt space is mostly empty, with millions of kilometers between large bodies."
            },
            {
                "question": "What prevented the rocky fragments inside the Asteroid Belt from coalescing into a single large terrestrial planet?",
                "options": [
                    "The intense gravitational perturbations and orbital resonances of nearby giant Jupiter",
                    "Extreme heat from the Sun melted them all into gas",
                    "Human mining operations destroyed the original planet",
                    "Magnetic repulsion from the Moon's orbit"
                ],
                "correct": 0,
                "explanation": "Jupiter's immense gravity pumped orbital eccentricities into planetesimals, increasing collision velocities from constructive accretion to destructive fragmentation.",
                "study_insight": "Jupiter acted as a gravitational gatekeeper during planetary disk formation."
            }
        ]
    },
    {
        "id": 15,
        "title": "Cosmic Ice",
        "subtitle": "Comets: Dirty Snowballs, Sublimating Coma & Halley's 76-Year Cycle",
        "concept_html": """
            <p>While asteroids are dry rocks, <strong>comets</strong> are icy celestial wanderers often described as 'dirty cosmic snowballs':</p>
            <div class='space-y-2 mt-2 text-slate-300'>
                <ul class='list-disc pl-5 space-y-1.5'>
                    <li><strong>Anatomy of a Comet:</strong> The central solid core (<strong>nucleus</strong>) consists of frozen water ice, carbon dioxide, methane, ammonia, and dark organic dust particles.</li>
                    <li><strong>How Tails Form:</strong> Deep in outer space, comets are frozen and invisible. As an eccentric orbit brings a comet close to the Sun, solar radiation vaporizes (sublimates) the ices directly into gas, forming a glowing envelope (<strong>coma</strong>) and a spectacular luminous <strong>tail</strong> millions of kilometers long!</li>
                    <li><strong>Tail Points Away from Sun:</strong> Solar wind and radiation pressure always push the gas and dust particles directly <strong>away from the Sun</strong>, regardless of which direction the comet is traveling!</li>
                    <li><strong>Halley's Comet:</strong> The most famous periodic comet, returning into Earth's view approximately every <strong>75 to 76 years</strong> (last seen in 1986, next expected in 2061).</li>
                </ul>
            </div>
        """,
        "spoken_text": "From the deep, freezing fringes of the solar system come comets, often described as dirty cosmic snowballs. A comet's nucleus is composed of frozen water, methane, and ammonia mixed with dark cosmic dust. Far from the Sun, a comet travels silently in the dark. But as its elongated orbit swoops close to solar heat, the ices instantly vaporize, forming a glowing cloud called a coma and sweeping out a magnificent tail millions of kilometers long. Solar wind always blows this glowing tail directly away from the Sun. The most famous visitor is Halley's Comet, which graces our skies once every seventy-six years, scheduled to return in the year 2061.",
        "lecture_script": "From the deep, freezing fringes of the solar system come comets, often described as dirty cosmic snowballs. A comet's nucleus is composed of frozen water, methane, and ammonia mixed with dark cosmic dust. Far from the Sun, a comet travels silently in the dark. But as its elongated orbit swoops close to solar heat, the ices instantly vaporize, forming a glowing cloud called a coma and sweeping out a magnificent tail millions of kilometers long. Solar wind always blows this glowing tail directly away from the Sun. The most famous visitor is Halley's Comet, which graces our skies once every seventy-six years, scheduled to return in the year 2061.",
        "checkpoints": [
            {
                "question": "In what direction does the luminous tail of a comet always point as it orbits near the Sun?",
                "options": [
                    "Directly toward the center of planet Earth",
                    "Directly away from the Sun, pushed by solar radiation pressure and solar wind",
                    "Always trailing straight behind the comet like smoke from a car",
                    "Directly downward toward the South Pole"
                ],
                "correct": 1,
                "explanation": "Photons and charged particles emitted by the Sun (solar wind) exert pressure on sublimated gas ions and dust, pushing the tail directly away from the Sun.",
                "study_insight": "A comet travels tail-first when heading back out toward the outer solar system!"
            },
            {
                "question": "What is the orbital period of the famous Halley's Comet as it travels from the outer solar system to loop around the Sun?",
                "options": [
                    "Every 365 days",
                    "Approximately every 75 to 76 years",
                    "Once every 10,000 years",
                    "Every 5 years"
                ],
                "correct": 1,
                "explanation": "Halley's Comet has a highly eccentric elliptical orbit with an orbital period of roughly 75 to 76 years, last perihelion in 1986, next in mid-2061.",
                "study_insight": "Edmond Halley used Newton's laws of gravitation to successfully predict the comet's 1758 return."
            }
        ]
    },
    {
        "id": 16,
        "title": "Milky Way",
        "subtitle": "Ākāśha Gangā Spiral Galaxy, Billions of Stars & The Quest for Exoplanets",
        "concept_html": """
            <p>Step outside on a pitch-black night in a dark sky sanctuary, and you will see a faint, luminous arch of pearly mist spanning the sky: our home galaxy, the <strong>Milky Way (Ākāśha Gangā)</strong>.</p>
            <div class='space-y-2 mt-2 text-slate-300'>
                <ul class='list-disc pl-5 space-y-1.5'>
                    <li><strong>Our Island Universe:</strong> A <strong>galaxy</strong> is a colossal gravitationally bound system containing gas, cosmic dust, and anywhere from millions to hundreds of billions of stars. The Milky Way is a barred spiral galaxy spanning over <strong>100,000 light-years across</strong>, holding over 200 billion stars, including our tiny Solar System!</li>
                    <li><strong>The Vast Observable Universe:</strong> Our galaxy is just one among an estimated <strong>two trillion galaxies</strong> scattered across the cosmic ocean.</li>
                    <li><strong>The Search for Life (Exoplanets):</strong> Modern space telescopes (like Kepler and James Webb) have discovered thousands of <strong>exoplanets</strong> (planets orbiting distant stars), searching for atmospheric water and biomarkers in 'habitable goldilocks zones'. While Earth remains the only known haven for life today, the search continues!</li>
                </ul>
            </div>
        """,
        "spoken_text": "On clear, moonless nights far from city lights, a luminous river of milky light stretches across the heavens. This is our home galaxy, the Milky Way, celebrated in Indian lore as the celestial Ākāśha Gangā. A galaxy is a majestic cosmic city of stars, gas, and dust held together by gravity. Our Milky Way is a barred spiral galaxy containing more than two hundred billion stars, with our Sun orbiting along one of its spiral arms. Across the vast observable universe lie trillions of other galaxies. Today, astronomers use space telescopes to discover exoplanets orbiting distant stars, hunting for signs of life beyond Earth.",
        "lecture_script": "On clear, moonless nights far from city lights, a luminous river of milky light stretches across the heavens. This is our home galaxy, the Milky Way, celebrated in Indian lore as the celestial Ākāśha Gangā. A galaxy is a majestic cosmic city of stars, gas, and dust held together by gravity. Our Milky Way is a barred spiral galaxy containing more than two hundred billion stars, with our Sun orbiting along one of its spiral arms. Across the vast observable universe lie trillions of other galaxies. Today, astronomers use space telescopes to discover exoplanets orbiting distant stars, hunting for signs of life beyond Earth.",
        "checkpoints": [
            {
                "question": "What is the traditional Indian astronomical name for the glowing celestial band of our Milky Way Galaxy visible in dark night skies?",
                "options": [
                    "Ākāśha Gangā",
                    "Dhruva Tārā",
                    "Saptarishi",
                    "Mṛgaśīrṣā"
                ],
                "correct": 0,
                "explanation": "The Milky Way is traditionally named Ākāśha Gangā in India, poetically envisioned as a celestial river of heavenly light flowing across the night sky.",
                "study_insight": "The milky glow is the combined light of billions of distant, unresolved stars along the galactic disk."
            },
            {
                "question": "What astronomical term describes a planet that orbits around a star outside our own Solar System?",
                "options": [
                    "An asteroid",
                    "An exoplanet (extrasolar planet)",
                    "A comet",
                    "A meteoroid"
                ],
                "correct": 1,
                "explanation": "An exoplanet (extrasolar planet) is any planet located beyond our Solar System orbiting another parent star or wandering freely in interstellar space.",
                "study_insight": "Astronomers use transit photometry and radial velocity methods to detect thousands of exoplanets."
            }
        ]
    }
]

