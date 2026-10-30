# -*- coding: utf-8 -*-
"""
Generates the comprehensive data module for NCERT Class 7 Science Chapter 12: Earth, Moon, and the Sun.
Output: .agents/class7_science_earth_moon_sun_data.py
Strictly zero raw LaTeX. Clean Unicode everywhere.
"""
import json
import re

def create_data_file():
    print("Generating class7_science_earth_moon_sun_data.py...")

    CHAPTER_META = {
        "chapter_num": 12,
        "title": "Earth, Moon, and the Sun",
        "subtitle": "NCERT Class 7 Science • Chapter 12 Interactive Master Laboratory",
        "mentors": "Acharya Aryabhata & Nicolaus Copernicus",
        "mentors_title": "Pioneers of Earth's Rotation, Heliocentrism & Eclipse Shadow Geometry",
        "badge": "Celestial Mechanics & Optics",
        "total_slides": 20,
        "checkpoints_count": 32,
        "quiz_questions_count": 40,
    }

    SLIDES = [
        # Slide 1: Introduction & Cosmic Trio Architecture
        {
            "id": 1,
            "slide_num": 1,
            "title": "Earth, Moon, and the Sun: The Cosmic Trio",
            "subtitle": "Chapter 12 Overview: Celestial Mechanics, Scale & Orbital Architecture",
            "badge": "Cosmic Foundations",
            "summary": "Our planetary home Earth, its natural satellite the Moon, and our parent star the Sun form an interconnected celestial trio. Their spins, orbital revolutions, and shadow alignments govern the fundamental rhythms of our lives: day and night, the calendar year, changing constellations, the cycles of seasons, and magnificent solar and lunar eclipses.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        Look up at the clear daytime sky, and you witness the brilliant golden light of the <strong class="text-amber-400">Sun</strong>. Look into the night sky, and you see the gentle silvery glow of the <strong class="text-slate-300">Moon</strong> alongside thousands of twinkling distant stars. Beneath your feet is planet <strong class="text-cyan-400">Earth</strong>.
    </p>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
        <div class="p-3.5 rounded-xl bg-amber-950/40 border border-amber-500/30">
            <div class="flex items-center gap-2 mb-1.5">
                <span class="w-2.5 h-2.5 rounded-full bg-amber-400 animate-pulse"></span>
                <h4 class="font-bold text-amber-300 text-sm">1. The Sun (Sol)</h4>
            </div>
            <p class="text-xs text-slate-300 leading-relaxed mb-2">
                A massive glowing ball of hot plasma powered by nuclear fusion. It contains <strong>99.86%</strong> of all mass in the Solar System.
            </p>
            <ul class="text-xs text-slate-300 space-y-1 list-disc list-inside">
                <li><strong class="text-slate-100">Diameter:</strong> 1,392,700 km (~109 Earth diameters).</li>
                <li><strong class="text-slate-100">Distance from Earth:</strong> ~150,000,000 km (1 Astronomical Unit, AU).</li>
                <li><strong class="text-slate-100">Light Travel Time:</strong> ~8 minutes and 20 seconds.</li>
            </ul>
        </div>
        <div class="p-3.5 rounded-xl bg-cyan-950/40 border border-cyan-500/30">
            <div class="flex items-center gap-2 mb-1.5">
                <span class="w-2.5 h-2.5 rounded-full bg-cyan-400"></span>
                <h4 class="font-bold text-cyan-300 text-sm">2. Planet Earth</h4>
            </div>
            <p class="text-xs text-slate-300 leading-relaxed mb-2">
                Our active, life-bearing terrestrial planet with a liquid water hydrosphere and protective atmosphere.
            </p>
            <ul class="text-xs text-slate-300 space-y-1 list-disc list-inside">
                <li><strong class="text-slate-100">Diameter:</strong> 12,742 km (equatorial).</li>
                <li><strong class="text-slate-100">Axial Tilt:</strong> 23.5° to the orbital perpendicular.</li>
                <li><strong class="text-slate-100">Motions:</strong> Spins in ~24 h, revolves in ~365¼ days.</li>
            </ul>
        </div>
        <div class="p-3.5 rounded-xl bg-slate-900/60 border border-slate-700/60">
            <div class="flex items-center gap-2 mb-1.5">
                <span class="w-2.5 h-2.5 rounded-full bg-slate-400"></span>
                <h4 class="font-bold text-slate-300 text-sm">3. The Moon (Luna)</h4>
            </div>
            <p class="text-xs text-slate-300 leading-relaxed mb-2">
                Earth's sole natural satellite; an airless, rocky non-luminous body reflecting solar photons.
            </p>
            <ul class="text-xs text-slate-300 space-y-1 list-disc list-inside">
                <li><strong class="text-slate-100">Diameter:</strong> 3,474 km (~¼ of Earth diameter).</li>
                <li><strong class="text-slate-100">Distance from Earth:</strong> ~384,400 km.</li>
                <li><strong class="text-slate-100">Light Travel Time:</strong> ~1.28 seconds.</li>
            </ul>
        </div>
    </div>
    <div class="p-3 rounded-lg bg-slate-900/60 border border-slate-700/60 text-xs text-slate-300">
        <strong class="text-amber-300">Astronomical Insight:</strong> If Earth were the size of a standard basketball (diameter ~24 cm), the Moon would be the size of a tennis ball (~6.5 cm) placed about 7.3 metres away, and the Sun would be a towering sphere 26 metres tall located 2.8 kilometres in the distance!
    </div>
</div>
""",
            "takeaways": [
                "The Sun is our primary luminous energy source, located approximately 150 million km from Earth (8 min 20 s light transit time).",
                "Earth is a spherical planet revolving around the Sun while rotating continuously on its own 23.5° tilted axis.",
                "The Moon orbits Earth at an average distance of 384,400 km, acting as a non-luminous reflector of sunlight."
            ],
            "checkpoints": [
                {
                    "id": "cp1_1",
                    "question": "How long does light from the Sun take to traverse the 150 million kilometres to reach Earth?",
                    "options": [
                        "Instantly (0 seconds)",
                        "Approximately 8 minutes and 20 seconds",
                        "Exactly 24 hours",
                        "365 days and 6 hours"
                    ],
                    "correct": 1,
                    "explanation": "Light travels at 300,000 km/s. Traversing the 150,000,000 km distance requires 150,000,000 ÷ 300,000 = 500 seconds, which equals 8 minutes and 20 seconds."
                },
                {
                    "id": "cp1_2",
                    "question": "What is the average distance between planet Earth and its natural satellite, the Moon?",
                    "options": [
                        "12,742 km",
                        "384,400 km",
                        "150,000,000 km",
                        "1 light-year"
                    ],
                    "correct": 1,
                    "explanation": "The Moon orbits Earth at an average distance of approximately 384,400 km, allowing reflected moonlight to reach Earth in just 1.28 seconds."
                }
            ]
        },

        # Slide 2: 12.1 Earth's Axial Rotation: The 24-Hour Cycle
        {
            "id": 2,
            "slide_num": 2,
            "title": "12.1 Rotation of the Earth: The 24-Hour Spin",
            "subtitle": "Chapter 12.1: Axial Spin Direction, Speed & The Day-Night Periodicity",
            "badge": "Axial Mechanics",
            "summary": "Earth spins continuously on an imaginary central rod passing through its North and South geographic poles, called its axis of rotation. Earth completes one full rotation in approximately 24 hours (1 mean solar day). When viewed from above the North Pole, Earth rotates in an anti-clockwise direction, which corresponds to spinning from West to East.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        Have you ever spun a top or watched a basketball balance on a fingertip? The planet Earth is similarly spinning continuously in the vacuum of space. This spinning motion of the Earth around its own imaginary central axis is called <strong class="text-amber-400">rotation</strong>.
    </p>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70">
            <h4 class="font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2">
                <span>🔄</span> Direction of Rotation
            </h4>
            <p class="text-xs text-slate-300 leading-relaxed mb-2">
                Earth rotates from <strong class="text-amber-300">West to East</strong>.
            </p>
            <ul class="text-xs text-slate-300 space-y-1 list-disc list-inside">
                <li>Viewed from high above the <strong class="text-slate-100">North Pole</strong>, the rotation is distinctly <strong>anti-clockwise</strong> (counter-clockwise).</li>
                <li>Viewed from above the <strong class="text-slate-100">South Pole</strong>, the rotation appears <strong>clockwise</strong>.</li>
                <li>Because Earth spins West to East, places situated towards the East (like Japan and Arunachal Pradesh) turn into sunlight before locations to the West (like London or Mumbai).</li>
            </ul>
        </div>
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70">
            <h4 class="font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2">
                <span>⏱️</span> Period and Speed of Rotation
            </h4>
            <p class="text-xs text-slate-300 leading-relaxed mb-2">
                Earth requires approximately <strong class="text-cyan-300">24 hours</strong> to complete one full 360° turn.
            </p>
            <ul class="text-xs text-slate-300 space-y-1 list-disc list-inside">
                <li><strong class="text-slate-100">Solar Day:</strong> 24 hours (86,400 seconds) relative to the Sun.</li>
                <li><strong class="text-slate-100">Sidereal Day:</strong> 23 hours, 56 minutes, 4.09 seconds relative to distant fixed stars.</li>
                <li><strong class="text-slate-100">Equatorial Speed:</strong> Earth's equator spans ~40,075 km. Dividing by 24 hours yields an astonishing surface speed of <strong class="text-emerald-400 font-mono">~1,670 km/h</strong> (faster than the speed of sound)!</li>
            </ul>
        </div>
    </div>
    <div class="p-3 rounded-lg bg-emerald-950/40 border border-emerald-500/30 text-xs text-slate-300">
        <strong class="text-emerald-300">Why don't we feel Earth spinning?</strong> Because the atmosphere, the oceans, the ground, and everything on Earth share the exact same constant rotational velocity without sudden acceleration or braking, just like passengers smoothly cruising inside a high-speed aircraft with windows closed!
    </div>
</div>
""",
            "takeaways": [
                "Earth rotates on its axis from West to East (anti-clockwise when observed from above the North Pole).",
                "One complete rotation takes approximately 24 hours, defining one day.",
                "At the Equator, Earth's surface moves eastward at approximately 1,670 km/h."
            ],
            "checkpoints": [
                {
                    "id": "cp2_1",
                    "question": "In which direction does the Earth spin on its axis when viewed from above the North Pole?",
                    "options": [
                        "Clockwise (East to West)",
                        "Anti-clockwise (West to East)",
                        "North to South",
                        "South to North"
                    ],
                    "correct": 1,
                    "explanation": "When observed from above the North Pole, Earth rotates in an anti-clockwise direction, which translates to spinning from West to East."
                },
                {
                    "id": "cp2_2",
                    "question": "What is the approximate time taken by the Earth to complete one full rotation on its axis?",
                    "options": [
                        "12 hours",
                        "24 hours",
                        "30 days",
                        "365¼ days"
                    ],
                    "correct": 1,
                    "explanation": "The Earth takes approximately 24 hours (one solar day) to complete one 360° rotation relative to the Sun."
                }
            ]
        },

        # Slide 3: 12.1 Day and Night Dynamics & The Terminator Line
        {
            "id": 3,
            "slide_num": 3,
            "title": "12.1 Day and Night: The Illuminated Globe",
            "subtitle": "Chapter 12.1: The Circle of Illumination, Shadows & Planetary Twilight",
            "badge": "Day-Night Physics",
            "summary": "Because Earth is an opaque sphere in space, sunlight can only illuminate one half of its surface at any given instant. The illuminated hemisphere experiences daytime, while the opposite hemisphere facing away into shadow experiences night. The great circular boundary dividing day from night is called the circle of illumination (terminator line).",
            "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        Why does daylight never last forever? Why is it dark while you sleep, but bright while you study at school? The answer lies in the fundamental interaction between an opaque spherical body and an external source of light.
    </p>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
        <div class="p-3.5 rounded-xl bg-amber-950/30 border border-amber-500/30">
            <h4 class="font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2">
                <span>☀️</span> Illuminated Daylight Hemisphere
            </h4>
            <p class="text-xs text-slate-300 leading-relaxed">
                As Earth rotates eastward, continents and oceans continuously turn towards the Sun. The hemisphere bathed in direct sunlight receives thermal radiation and visible light, marking the period of <strong>daytime</strong>.
            </p>
        </div>
        <div class="p-3.5 rounded-xl bg-indigo-950/40 border border-indigo-500/30">
            <h4 class="font-bold text-indigo-300 text-sm mb-1.5 flex items-center gap-2">
                <span>🌙</span> Dark Night Hemisphere
            </h4>
            <p class="text-xs text-slate-300 leading-relaxed">
                Simultaneously, the opposite half of the Earth is turned away from the Sun, cast into its own planetary shadow. Here, shielded from direct solar rays, we observe the darkness of <strong>nighttime</strong>, unveiling the moon and distant stars.
            </p>
        </div>
    </div>
    <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70 space-y-2">
        <h4 class="font-bold text-cyan-300 text-sm flex items-center gap-2">
            <span>🌐</span> The Circle of Illumination (The Terminator)
        </h4>
        <p class="text-xs text-slate-300 leading-relaxed">
            The sharp circular line that separates the sunlit day hemisphere from the darkened night hemisphere is termed the <strong class="text-cyan-300">circle of illumination</strong> or <strong class="text-cyan-300">terminator line</strong>.
        </p>
        <ul class="text-xs text-slate-300 space-y-1 list-disc list-inside">
            <li>As the Earth rotates beneath the terminator, an observer crossing from the dark side into the sunlit side experiences <strong class="text-amber-300">Dawn & Sunrise</strong>.</li>
            <li>Hours later, as rotation carries that observer across the terminator into the shadow side, they witness <strong class="text-amber-300">Sunset & Dusk (Twilight)</strong>.</li>
            <li>Atmospheric scattering of sunlight by air molecules creates soft twilight before the Sun actually crests the horizon and after it sets.</li>
        </ul>
    </div>
</div>
""",
            "takeaways": [
                "Day and night occur because Earth is an opaque sphere rotating in front of the distant Sun.",
                "Only one half of the Earth receives sunlight at any given moment, while the other half remains in shadow.",
                "The boundary dividing the sunlit and darkened hemispheres is called the circle of illumination (terminator)."
            ],
            "checkpoints": [
                {
                    "id": "cp3_1",
                    "question": "What is the primary scientific reason for the alternation of day and night on Earth?",
                    "options": [
                        "The Sun turns its light off like a switch at night",
                        "The Earth rotates on its own axis once every 24 hours in front of the Sun",
                        "The Moon blocks the Sun every night",
                        "Clouds completely cover the sky to create darkness"
                    ],
                    "correct": 1,
                    "explanation": "Because Earth is an opaque sphere rotating on its axis, each location continually passes into sunlight (day) and out into Earth's shadow (night) once every 24 hours."
                },
                {
                    "id": "cp3_2",
                    "question": "What is the name given to the circular boundary line on Earth dividing the sunlit day side from the dark night side?",
                    "options": [
                        "The Prime Meridian",
                        "The Circle of Illumination (Terminator)",
                        "The Equator",
                        "The Tropic of Cancer"
                    ],
                    "correct": 1,
                    "explanation": "The circle of illumination (or terminator) is the geometric boundary dividing the daylight hemisphere from the nighttime hemisphere."
                }
            ]
        },

        # Slide 4: 12.1 Apparent Celestial Motion: Rising East, Setting West
        {
            "id": 4,
            "slide_num": 4,
            "title": "12.1 Apparent Celestial Motion: The East-to-West Illusion",
            "subtitle": "Chapter 12.1: Why the Sun, Moon, and Stars Appear to Rise in East & Set in West",
            "badge": "Relative Motion",
            "summary": "Every day, the Sun rises in the East, traverses the southern sky (in the northern hemisphere), and sets in the West. The Moon, planets, and constellations follow this exact same east-to-west path. This apparent diurnal motion of celestial bodies is an optical illusion caused entirely by Earth's real counter-clockwise rotation from West to East.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        From ancient times, humans observed the Sun rising over the eastern hills and dipping below the western horizon. Naturally, ancient observers believed that the Sun was physically circling around a stationary Earth. However, modern physics proves that this motion is purely <strong class="text-amber-400">apparent motion</strong>.
    </p>
    <div class="p-4 rounded-xl bg-amber-950/30 border border-amber-500/30">
        <h4 class="font-bold text-amber-300 text-sm mb-2 flex items-center gap-2">
            <span>🚂</span> The Train Window Relative Motion Analogy
        </h4>
        <p class="text-xs text-slate-300 leading-relaxed mb-2">
            Imagine sitting in a smooth express train speeding forward towards the <strong class="text-emerald-400">East</strong>. When you look out the passenger window, what do stationary trees, telegraph poles, and buildings appear to do?
        </p>
        <p class="text-xs text-slate-200 font-semibold bg-slate-900/80 p-2.5 rounded-lg border border-slate-700">
            They appear to rush rapidly backwards towards the <span class="text-amber-400">West</span>! The trees are not moving; your moving reference frame creates the illusion of reverse motion.
        </p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs text-slate-300">
        <div class="p-3 rounded-lg bg-slate-900/70 border border-slate-800">
            <strong class="text-cyan-300 block mb-1">True Motion (Space View):</strong>
            Earth spins continuously on its axis from <strong>West to East</strong>.
        </div>
        <div class="p-3 rounded-lg bg-slate-900/70 border border-slate-800">
            <strong class="text-amber-300 block mb-1">Apparent Motion (Earth View):</strong>
            All celestial bodies (Sun, Moon, stars) appear to drift across our sky from <strong>East to West</strong>.
        </div>
    </div>
    <div class="p-3 rounded-lg bg-slate-900/60 border border-slate-700/60 text-xs text-slate-300">
        <strong class="text-cyan-300">The Stationary Pole Star (Polaris):</strong> There is one remarkable exception! <strong class="text-slate-100">Polaris (Dhruva Tara)</strong> appears almost completely motionless in the night sky. Why? Because it lies directly along the extension of Earth's rotational axis above the North Pole. As the Earth spins, the spindle points right at Polaris!
    </div>
</div>
""",
            "takeaways": [
                "The rising of the Sun, Moon, and stars in the East and setting in the West is an apparent motion caused by Earth's West-to-East rotation.",
                "Relative motion makes stationary external objects appear to move in the exact opposite direction of the observer's motion.",
                "Polaris (the North Star) appears stationary because it aligns directly with Earth's axis of rotation."
            ],
            "checkpoints": [
                {
                    "id": "cp4_1",
                    "question": "Why do the Sun, Moon, and stars appear to move across the sky from East to West every day?",
                    "options": [
                        "The Sun and stars are physically racing around the Earth at millions of km/h",
                        "The Earth rotates on its axis from West to East, creating the opposite apparent motion",
                        "Strong stratospheric winds push celestial bodies across the sky",
                        "Earth's gravity repels the Sun towards the West"
                    ],
                    "correct": 1,
                    "explanation": "Because Earth rotates towards the East, distant stationary celestial objects appear to move in the opposite direction (from East to West), just like trees appearing to move backwards from a forward-moving train."
                },
                {
                    "id": "cp4_2",
                    "question": "Why does Polaris (the North Star / Dhruva Tara) appear almost completely motionless in our night sky?",
                    "options": [
                        "It is the only star that does not emit light",
                        "It lies almost exactly directly above Earth's North rotational axis",
                        "It is held fixed in place by the Moon's magnetic field",
                        "It rotates at the exact same speed as the Sun"
                    ],
                    "correct": 1,
                    "explanation": "Polaris lies along the northern projection of Earth's rotational axis. Just as the central hub of a spinning bicycle wheel stays in place, Polaris appears stationary while all other stars seem to circle around it."
                }
            ]
        },

        # Slide 5: 12.1 Acharya Aryabhata's Revolution (499 CE)
        {
            "id": 5,
            "slide_num": 5,
            "title": "12.1 Acharya Aryabhata's Revolution (499 CE)",
            "subtitle": "Chapter 12.1: Ancient Indian Astronomy & The Moving Earth Discovery",
            "badge": "Heritage & History",
            "summary": "In 499 CE, at the age of just 23, the great ancient Indian mathematician and astronomer Acharya Aryabhata recorded in his treatise 'Aryabhatiya' that the Earth is a sphere rotating daily on its axis, while the starry sphere is stationary. He brilliantly used the analogy of a person traveling on a boat seeing stationary trees moving backwards.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        More than a thousand years before Nicolaus Copernicus (1543) and Galileo Galilei (1632) sparked the European scientific revolution, the brilliant astronomer <strong class="text-amber-400">Acharya Aryabhata</strong> (born 476 CE in Kusumapura / Pataliputra, modern-day Patna, Bihar) laid the foundational truths of planetary kinematics.
    </p>
    <div class="p-4 rounded-xl bg-gradient-to-br from-amber-950/40 via-slate-900 to-cyan-950/40 border border-amber-500/30 space-y-3">
        <div class="flex items-center gap-2">
            <span class="text-amber-400 text-lg font-bold">📜</span>
            <h4 class="font-bold text-amber-300 text-sm">Aryabhatiya (Golapada, Verse 9):</h4>
        </div>
        <p class="font-serif italic text-amber-200 text-sm bg-slate-950/70 p-3 rounded-lg border border-amber-500/20 leading-relaxed">
            "Anulomagatir nausthah pashyaty achalam vilomagam yadvat |<br>
            Achalani bhani tadvat samapashchimagani lankayam ||"
        </p>
        <p class="text-xs text-slate-300 leading-relaxed">
            <strong class="text-cyan-300">English Translation:</strong> <em>"Just as a passenger seated in a boat traveling forward sees stationary objects (trees and rocks on the riverbanks) moving in the reverse direction, so do the stationary stars appear to move due West to an observer situated on Earth."</em>
        </p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs text-slate-300">
        <div class="p-3 rounded-lg bg-slate-900/70 border border-slate-800">
            <strong class="text-amber-300 block mb-1">Axial Rotation:</strong>
            Aryabhata proposed that Earth is spherical (<em>Bhugola</em>) and rotates continuously on its axis (<em>Chala Prithvi Sthira Bhamandala</em>), debunking the rigid belief that the entire cosmic sphere circled a flat, resting Earth.
        </div>
        <div class="p-3 rounded-lg bg-slate-900/70 border border-slate-800">
            <strong class="text-cyan-300 block mb-1">Accurate Constants:</strong>
            Aryabhata calculated the sidereal rotation period of the Earth as <strong>23 hours, 56 minutes, and 4.1 seconds</strong>, amazingly accurate when compared to modern satellite atomic clock values (23 h 56 m 4.091 s)!
        </div>
    </div>
</div>
""",
            "takeaways": [
                "Acharya Aryabhata in 499 CE was the first recorded astronomer to explicitly state that the Earth rotates on its axis while the stars remain stationary.",
                "He used the insightful boat analogy (relative motion) to explain the apparent East-to-West drift of the night sky.",
                "His calculated sidereal rotation period was extraordinarily precise (23 h 56 m 4.1 s)."
            ],
            "checkpoints": [
                {
                    "id": "cp5_1",
                    "question": "What analogy did Acharya Aryabhata use in the Aryabhatiya to explain why stars appear to move Westward?",
                    "options": [
                        "A horse galloping across a dusty desert",
                        "A passenger in a moving boat seeing stationary trees on the bank moving in the reverse direction",
                        "A potter spinning a clay wheel",
                        "An archer releasing an arrow into the wind"
                    ],
                    "correct": 1,
                    "explanation": "Aryabhata used the analogy of a person in a moving boat who sees stationary trees on the riverbank appearing to move backwards, explaining how Earth's forward rotation creates the illusion of moving stars."
                },
                {
                    "id": "cp5_2",
                    "question": "In what famous 499 CE Sanskrit astronomical treatise did Aryabhata propose that the Earth rotates on its axis?",
                    "options": [
                        "Surya Siddhanta",
                        "Aryabhatiya",
                        "Panchasiddhantika",
                        "Brahmasphutasiddhanta"
                    ],
                    "correct": 1,
                    "explanation": "Aryabhata composed the revolutionary treatise 'Aryabhatiya' at the age of 23 in 499 CE in Kusumapura (modern Patna)."
                }
            ]
        },

        # Slide 6: 12.2 Earth's Revolution Around the Sun: The 365¼-Day Journey
        {
            "id": 6,
            "slide_num": 6,
            "title": "12.2 Revolution of the Earth: The 365¼-Day Orbit",
            "subtitle": "Chapter 12.2: Orbital Mechanics, Velocities & The Leap Year Arithmetic",
            "badge": "Orbital Dynamics",
            "summary": "While spinning on its axis, the Earth also travels in a giant, nearly circular orbital path around the Sun. This motion of Earth around the Sun is called revolution. One complete revolution requires approximately 365 days and 6 hours (365¼ days). The extra 6 hours accumulated over four successive years form one complete 24-hour day, giving rise to Leap Years.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        Earth does not remain stationary in one corner of space. Bound by the powerful gravitational pull of the massive Sun, Earth cruises in an elliptical (nearly circular) trajectory around the Sun at a blistering orbital speed of approximately <strong class="text-amber-400 font-mono">29.8 km/s</strong> (over 107,000 km/h).
    </p>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70">
            <h4 class="font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2">
                <span>🔄</span> Rotation vs Revolution
            </h4>
            <ul class="text-xs text-slate-300 space-y-1.5">
                <li><strong class="text-slate-100">Rotation:</strong> Spinning of Earth on its <em>internal axis</em>; period = ~24 hours; causes day and night.</li>
                <li><strong class="text-slate-100">Revolution:</strong> Movement of Earth in an <em>orbit around the Sun</em>; period = ~365 days 6 hours; causes the year and seasons.</li>
                <li><strong class="text-slate-100">Orbital Perimeter:</strong> Earth travels ~940 million kilometres in completing one revolution!</li>
            </ul>
        </div>
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70">
            <h4 class="font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2">
                <span>📅</span> The Leap Year Formula
            </h4>
            <p class="text-xs text-slate-300 leading-relaxed mb-2">
                A standard calendar year contains exactly 365 whole days. However, Earth's actual orbital period is <strong class="text-cyan-300">365 days and 6 hours</strong> (365.2422 days).
            </p>
            <div class="p-2 rounded bg-slate-950 text-xs font-mono text-amber-300 space-y-0.5">
                <div>Year 1: +6 hours</div>
                <div>Year 2: +6 hours (+12 h total)</div>
                <div>Year 3: +6 hours (+18 h total)</div>
                <div>Year 4: +6 hours = 24 hours = 1 Extra Full Day!</div>
            </div>
            <p class="text-[11px] text-slate-400 mt-2">
                Every 4th year, this extra 24 hours is appended to February (giving it 29 days instead of 28), creating a 366-day <strong class="text-emerald-300">Leap Year</strong>!
            </p>
        </div>
    </div>
</div>
""",
            "takeaways": [
                "Revolution is the motion of the Earth around the Sun in a nearly circular orbit.",
                "One complete revolution takes approximately 365 days and 6 hours (365¼ days).",
                "The 6 extra hours accumulated over 4 consecutive years equal 24 hours, creating a 366-day Leap Year with 29 days in February."
            ],
            "checkpoints": [
                {
                    "id": "cp6_1",
                    "question": "What is the exact approximate time taken by the Earth to complete one full revolution around the Sun?",
                    "options": [
                        "24 hours",
                        "30 days",
                        "365 days and 6 hours (365¼ days)",
                        "1,000 days"
                    ],
                    "correct": 2,
                    "explanation": "Earth completes one full orbit around the Sun in approximately 365 days and 6 hours."
                },
                {
                    "id": "cp6_2",
                    "question": "Why does a leap year occur once every four years?",
                    "options": [
                        "Because the Earth stops rotating for one day every four years",
                        "The 6 extra hours per year accumulate over 4 years to equal 24 hours (1 full day)",
                        "The Moon crashes into Earth every four years",
                        "To celebrate the summer solstice"
                    ],
                    "correct": 1,
                    "explanation": "6 hours × 4 years = 24 hours = 1 full day. Adding this extra day to February keeps our calendar synchronized with the physical seasons."
                }
            ]
        },

        # Slide 7: 12.2.1 Changing View of the Night Sky: Constellations Through the Seasons
        {
            "id": 7,
            "slide_num": 7,
            "title": "12.2.1 Changing View of the Night Sky",
            "subtitle": "Chapter 12.2.1: Seasonal Constellations & The 4-Minute Daily Star Shift",
            "badge": "Night Sky Mechanics",
            "summary": "Have you ever wondered why you cannot spot the magnificent constellation Orion (the Hunter) on a warm June night, but see it dominating the winter sky in December and January? As Earth revolves around the Sun, its nighttime side looks outward into different directions of deep space, causing the visible stars and constellations to change progressively across the months.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        The night sky is not static from month to month. If you observe the night sky at 9:00 PM in January, you will see a dramatically different collection of stellar constellations than at 9:00 PM in July.
    </p>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70">
            <h4 class="font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2">
                <span>🌌</span> Orbital Perspective Shift
            </h4>
            <p class="text-xs text-slate-300 leading-relaxed mb-2">
                Remember that we can only see stars during <strong>nighttime</strong>, when our side of Earth is pointing directly <em>away</em> from the Sun.
            </p>
            <ul class="text-xs text-slate-300 space-y-1 list-disc list-inside">
                <li><strong class="text-cyan-300">In December–January:</strong> Earth is on one side of the Sun; nighttime faces constellations like <strong class="text-slate-100">Orion, Taurus, and Canis Major (Sirius)</strong>.</li>
                <li><strong class="text-amber-300">In June–July:</strong> Earth has moved to the opposite side of its orbit; nighttime now faces constellations like <strong class="text-slate-100">Scorpius, Sagittarius, and Cygnus</strong>.</li>
                <li>The stars that were visible in winter are now positioned behind the Sun in daytime, drowned out by intense solar glare!</li>
            </ul>
        </div>
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70">
            <h4 class="font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2">
                <span>⏰</span> The 4-Minute Daily Shift
            </h4>
            <p class="text-xs text-slate-300 leading-relaxed mb-2">
                Because Earth completes a 360° revolution in ~365 days, it advances approximately <strong class="text-emerald-400 font-mono">~1° per day</strong> along its orbit.
            </p>
            <ul class="text-xs text-slate-300 space-y-1 list-disc list-inside">
                <li>This orbital advance causes every star to rise approximately <strong class="text-amber-300">4 minutes earlier</strong> each night!</li>
                <li>In 30 days (1 month), this accumulates to: 30 × 4 minutes = <strong class="text-cyan-300 font-mono">120 minutes (2 hours) earlier</strong>.</li>
                <li>A star that rises at 10:00 PM on October 1 will rise at 8:00 PM on November 1 and at 6:00 PM on December 1!</li>
            </ul>
        </div>
    </div>
</div>
""",
            "takeaways": [
                "The constellations visible in the night sky change throughout the year due to Earth's revolution around the Sun.",
                "Nighttime faces different directions in space as Earth orbits the Sun; stars behind the Sun are invisible in daytime.",
                "Stars rise approximately 4 minutes earlier each day (2 hours earlier each month) because of Earth's ~1° daily orbital advancement."
            ],
            "checkpoints": [
                {
                    "id": "cp7_1",
                    "question": "Why are different constellations visible in the night sky in winter compared to summer?",
                    "options": [
                        "Stars migrate like birds towards warm countries in winter",
                        "Earth revolves around the Sun, causing the night side to point into different sectors of outer space",
                        "Stars extinguish their nuclear fuel in summer and reignite in winter",
                        "The Moon casts a shadow covering the stars during summer months"
                    ],
                    "correct": 1,
                    "explanation": "As Earth revolves around the Sun, the night side (facing away from the Sun) continually looks out into different regions of the galaxy."
                },
                {
                    "id": "cp7_2",
                    "question": "How much earlier does a given star rise each successive night due to Earth's orbital revolution?",
                    "options": [
                        "1 hour earlier",
                        "4 minutes earlier",
                        "12 hours earlier",
                        "It rises at the exact same minute every night forever"
                    ],
                    "correct": 1,
                    "explanation": "Because Earth moves ~1° around the Sun each day, stars rise roughly 4 minutes earlier each night, adding up to 2 hours earlier each month."
                }
            ]
        },

        # Slide 8: 12.2.2 The Tilt of Earth's Axis: 23.5° Obliquity
        {
            "id": 8,
            "slide_num": 8,
            "title": "12.2.2 The Tilt of Earth's Axis: 23.5° Obliquity",
            "subtitle": "Chapter 12.2.2: The Unchanging Lean Towards Polaris (Axial Parallelism)",
            "badge": "Orbital Geometry",
            "summary": "Earth's axis of rotation is not perpendicular to its orbital plane; it is permanently tilted at an angle of 23.5° from the vertical (or 66.5° to the orbital plane). Crucially, this axis maintains fixed orientation in space throughout the entire 365¼-day orbit, constantly pointing towards the North Star (Polaris). This phenomenon is known as axial parallelism.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        If you look at any classroom globe of the Earth, you will notice that it is never mounted perfectly straight up-and-down. It is deliberately mounted at a jaunty angle. This is not an artistic choice; it represents one of the most critical facts of our planetary existence: <strong class="text-amber-400">axial tilt (obliquity)</strong>.
    </p>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70">
            <h4 class="font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2">
                <span>📐</span> The Geometry of the Tilt
            </h4>
            <ul class="text-xs text-slate-300 space-y-1.5">
                <li><strong class="text-slate-100">Orbital Plane (Ecliptic):</strong> The flat plane on which Earth revolves around the Sun.</li>
                <li><strong class="text-slate-100">Perpendicular to Orbit:</strong> An imaginary 90° line vertical to the orbital flat table.</li>
                <li><strong class="text-amber-300 font-bold">Angle of Tilt:</strong> Earth's axis tilts at <strong class="text-amber-300 font-mono">23.5°</strong> from the perpendicular line.</li>
                <li><strong class="text-slate-100">Angle to Orbital Plane:</strong> 90° − 23.5° = <strong class="text-cyan-300 font-mono">66.5°</strong> relative to the orbital plane itself.</li>
            </ul>
        </div>
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70">
            <h4 class="font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2">
                <span>🧭</span> Parallelism of the Axis
            </h4>
            <p class="text-xs text-slate-300 leading-relaxed mb-2">
                As Earth journeys around its 940-million-km annual racetrack, its axis <strong class="text-cyan-300">does not wobble wildly</strong> back and forth.
            </p>
            <ul class="text-xs text-slate-300 space-y-1 list-disc list-inside">
                <li>Like a spinning gyroscope, the axis maintains its tilt pointing in the <strong class="text-slate-100">same fixed direction in space</strong> year-round.</li>
                <li>The North Pole points continuously towards the distant star <strong class="text-emerald-300">Polaris</strong> (the North Star).</li>
                <li>Because the tilt direction remains fixed while the Earth travels around the Sun, at one point in the orbit the Northern Hemisphere leans <em>toward</em> the Sun, and six months later it leans <em>away</em> from the Sun!</li>
            </ul>
        </div>
    </div>
</div>
""",
            "takeaways": [
                "Earth's axis is tilted at 23.5° from the perpendicular to its orbital plane (66.5° to the orbital plane).",
                "The axis points in a fixed direction in space (towards Polaris) throughout Earth's revolution.",
                "This fixed tilt causes the Northern and Southern hemispheres to take turns leaning towards or away from the Sun."
            ],
            "checkpoints": [
                {
                    "id": "cp8_1",
                    "question": "What is the angle of tilt of Earth's rotational axis relative to the perpendicular to its orbital plane?",
                    "options": [
                        "0° (perfectly upright)",
                        "23.5°",
                        "45.0°",
                        "90.0°"
                    ],
                    "correct": 1,
                    "explanation": "Earth's axis of rotation is tilted at an angle of approximately 23.5° relative to the perpendicular to its orbital plane."
                },
                {
                    "id": "cp8_2",
                    "question": "What distant star does Earth's North rotational axis continuously point toward throughout its entire annual revolution?",
                    "options": [
                        "Sirius",
                        "Polaris (The North Star)",
                        "Betelgeuse",
                        "Alpha Centauri"
                    ],
                    "correct": 1,
                    "explanation": "Because of axial parallelism, Earth's northern axis remains fixed in direction, pointing continuously towards Polaris."
                }
            ]
        },

        # Slide 9: 12.2.2 The Origin of Seasons: Angle of Sunlight & Insolation
        {
            "id": 9,
            "slide_num": 9,
            "title": "12.2.2 The Origin of Seasons: Solar Angle & Energy Flux",
            "subtitle": "Chapter 12.2.2: Dispelling the Distance Myth & The Physics of Slanted Sunlight",
            "badge": "Atmospheric Physics",
            "summary": "Seasons are NOT caused by changes in Earth's distance from the Sun! In fact, Earth is closest to the Sun in early January (perihelion) during Northern Hemisphere winter. Seasons are caused purely by the 23.5° axial tilt, which changes the angle at which sunlight strikes the ground (direct vs slanted rays) and the duration of daytime.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        Ask most people why summer is hotter than winter, and many will guess: <em>"Because the Earth is closer to the Sun in summer!"</em> This is a <strong class="text-rose-400 font-bold">major scientific misconception</strong>.
    </p>
    <div class="p-3.5 rounded-xl bg-rose-950/40 border border-rose-500/30 text-xs text-slate-300 space-y-1.5">
        <strong class="text-rose-300 text-sm block">🚫 BUSTING THE DISTANCE MYTH:</strong>
        <p>
            Earth's orbit is nearly circular. Earth is at <strong class="text-slate-100">Perihelion (closest: 147.1 million km)</strong> around <strong>January 3</strong>, right in the middle of freezing winter in India, Europe, and North America! Conversely, Earth is at <strong class="text-slate-100">Aphelion (farthest: 152.1 million km)</strong> around <strong>July 4</strong>, during the sweltering heat of northern summer.
        </p>
        <p class="text-emerald-300 font-semibold">
            Distance differences (~3%) have virtually no effect on seasons. The true reason is the 23.5° axial tilt!
        </p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs text-slate-300">
        <div class="p-3.5 rounded-xl bg-amber-950/30 border border-amber-500/30">
            <h4 class="font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2">
                <span>🔦</span> 1. Direct Rays (High Angle / Summer)
            </h4>
            <p class="mb-2">
                When a hemisphere tilts toward the Sun, solar rays strike the ground almost vertically (steep angle).
            </p>
            <ul class="space-y-1 list-disc list-inside">
                <li>Solar energy is concentrated over a <strong class="text-amber-300">small surface area</strong>, producing intense thermal heating.</li>
                <li>Rays traverse a <strong class="text-slate-100">shorter atmospheric path</strong>, losing minimal energy to atmospheric absorption and scattering.</li>
                <li>Long daylight hours allow heat to accumulate throughout the day.</li>
            </ul>
        </div>
        <div class="p-3.5 rounded-xl bg-cyan-950/30 border border-cyan-500/30">
            <h4 class="font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2">
                <span>📐</span> 2. Slanted Rays (Low Angle / Winter)
            </h4>
            <p class="mb-2">
                When a hemisphere tilts away from the Sun, solar rays strike at a shallow, grazing angle.
            </p>
            <ul class="space-y-1 list-disc list-inside">
                <li>The exact same amount of solar light spreads out over a <strong class="text-cyan-300">much larger surface area</strong>, producing weak, diffuse warming.</li>
                <li>Rays must penetrate a <strong class="text-slate-100">much thicker layer of atmosphere</strong>, getting scattered and absorbed.</li>
                <li>Short daylight hours give less time for heating and long nights permit extensive radiative cooling.</li>
            </ul>
        </div>
    </div>
</div>
""",
            "takeaways": [
                "Seasons are NOT caused by distance from the Sun (Earth is closest to the Sun in January).",
                "Direct vertical rays concentrate solar energy over smaller areas, causing intense summer heating.",
                "Slanted, oblique rays spread the same energy over larger areas, resulting in cold winter temperatures."
            ],
            "checkpoints": [
                {
                    "id": "cp9_1",
                    "question": "In which month is planet Earth actually closest to the Sun (at perihelion)?",
                    "options": [
                        "January (Northern Hemisphere winter)",
                        "June (Northern Hemisphere summer)",
                        "September (Autumnal Equinox)",
                        "July (Northern Hemisphere summer)"
                    ],
                    "correct": 0,
                    "explanation": "Earth is closest to the Sun (~147.1 million km) around January 3–4, proving that distance from the Sun does not cause seasons."
                },
                {
                    "id": "cp9_2",
                    "question": "Why do direct, perpendicular rays of sunlight heat the ground much more effectively than slanted rays?",
                    "options": [
                        "Direct rays turn into blue laser light",
                        "Direct rays concentrate solar energy onto a smaller surface area and travel through less atmosphere",
                        "Slanted rays are frozen by high-altitude clouds",
                        "The Sun only burns hydrogen when rays are perpendicular"
                    ],
                    "correct": 1,
                    "explanation": "Perpendicular rays concentrate maximum photon energy over a small ground footprint with minimal atmospheric scattering, whereas slanted rays spread that energy over a much wider area."
                }
            ]
        },

        # Slide 10: 12.2.2 Solstices and Hemispheric Asymmetry
        {
            "id": 10,
            "slide_num": 10,
            "title": "12.2.2 Solstices and Hemispheric Opposition",
            "subtitle": "Chapter 12.2.2: June 21 Summer Solstice, Dec 22 Winter Solstice & Polar Extremes",
            "badge": "Solstice Extremes",
            "summary": "Because of Earth's axial tilt, the two hemispheres experience opposite seasons simultaneously. Around June 21 (Summer Solstice), the Northern Hemisphere is tilted maximally towards the Sun, receiving direct rays at the Tropic of Cancer with the longest daytime of the year. Around December 22 (Winter Solstice), the Northern Hemisphere tilts away, enduring the shortest day, while the Southern Hemisphere enjoys summer.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        The word <strong class="text-amber-400">Solstice</strong> comes from the Latin <em>sol</em> (Sun) and <em>sistere</em> (to stand still), because the Sun's apparent path halts its northward or southward march before reversing direction.
    </p>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
        <div class="p-3.5 rounded-xl bg-amber-950/40 border border-amber-500/30">
            <div class="flex items-center gap-2 mb-1.5">
                <span class="w-2.5 h-2.5 rounded-full bg-amber-400"></span>
                <h4 class="font-bold text-amber-300 text-sm">Summer Solstice (Around June 21)</h4>
            </div>
            <ul class="text-xs text-slate-300 space-y-1.5">
                <li><strong class="text-slate-100">Northern Hemisphere:</strong> Tilted directly towards the Sun; Sun is overhead at the <strong class="text-amber-300">Tropic of Cancer (23.5°N)</strong>.</li>
                <li><strong class="text-slate-100">Day Length:</strong> Longest daytime and shortest night of the year in places like India, Japan, Europe, and USA.</li>
                <li><strong class="text-emerald-300">Arctic Circle (66.5°N to 90°N):</strong> Remains bathed in continuous sunlight 24 hours a day (<strong class="text-emerald-300">Midnight Sun</strong>)!</li>
                <li><strong class="text-cyan-300">Southern Hemisphere:</strong> Tilted away from Sun; experiences shortest day, longest night, and <strong class="text-cyan-300">Winter</strong>.</li>
            </ul>
        </div>
        <div class="p-3.5 rounded-xl bg-cyan-950/40 border border-cyan-500/30">
            <div class="flex items-center gap-2 mb-1.5">
                <span class="w-2.5 h-2.5 rounded-full bg-cyan-400"></span>
                <h4 class="font-bold text-cyan-300 text-sm">Winter Solstice (Around December 22)</h4>
            </div>
            <ul class="text-xs text-slate-300 space-y-1.5">
                <li><strong class="text-slate-100">Northern Hemisphere:</strong> Tilted away from the Sun; Sun is overhead at the <strong class="text-cyan-300">Tropic of Capricorn (23.5°S)</strong>.</li>
                <li><strong class="text-slate-100">Day Length:</strong> Shortest daytime and longest night of the year in the north (<strong class="text-cyan-300">Winter</strong>).</li>
                <li><strong class="text-slate-100">Arctic Circle:</strong> Plunged into continuous 24-hour darkness (Polar Night).</li>
                <li><strong class="text-amber-300">Southern Hemisphere:</strong> Tilted towards Sun; enjoys longest day and peak <strong class="text-amber-300">Summer</strong> (e.g., warm sunny Christmases on beaches in Australia and South Africa)!</li>
            </ul>
        </div>
    </div>
</div>
""",
            "takeaways": [
                "Summer Solstice (June 21): Northern Hemisphere tilts toward Sun (longest day); Southern Hemisphere has winter.",
                "Winter Solstice (December 22): Northern Hemisphere tilts away (shortest day); Southern Hemisphere has summer.",
                "The two hemispheres always experience opposite seasons simultaneously."
            ],
            "checkpoints": [
                {
                    "id": "cp10_1",
                    "question": "When India (Northern Hemisphere) is experiencing peak winter in December, what season is Australia (Southern Hemisphere) enjoying?",
                    "options": [
                        "Freezing winter with heavy snow",
                        "Peak summer with long, warm days",
                        "Monsoon floods everywhere",
                        "Spring equinox"
                    ],
                    "correct": 1,
                    "explanation": "Because Earth's hemispheres tilt in opposite directions relative to the Sun, Southern Hemisphere lands like Australia experience summer in December."
                },
                {
                    "id": "cp10_2",
                    "question": "What unusual phenomenon occurs in the Arctic Circle (above 66.5°N) around the Summer Solstice (June 21)?",
                    "options": [
                        "Complete darkness for 6 months",
                        "The Sun never sets below the horizon (24 hours of continuous daylight, the Midnight Sun)",
                        "Earthquakes every hour",
                        "The oceans completely boil away"
                    ],
                    "correct": 1,
                    "explanation": "Because the northern polar cap leans towards the Sun, the entire Arctic Circle remains inside the circle of illumination for a full 24-hour rotation (the Midnight Sun)."
                }
            ]
        },

        # Slide 11: 12.2.2 Equinoxes: Worldwide Equal Day and Night
        {
            "id": 11,
            "slide_num": 11,
            "title": "12.2.2 Equinoxes: Worldwide Equal Day and Night",
            "subtitle": "Chapter 12.2.2: March 21 (Vernal) and September 23 (Autumnal) Planetary Balance",
            "badge": "Equinox Balance",
            "summary": "Twice a year, on March 21 and September 23, the Earth reaches points in its orbit where neither hemisphere is tilted towards or away from the Sun. The Sun shines directly vertically over the Equator. On these two dates, known as Equinoxes (from Latin 'equal night'), every location on planet Earth experiences exactly 12 hours of daytime and 12 hours of nighttime.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        Between the extremes of the solstices lie two wondrous moments of celestial balance. The term <strong class="text-amber-400">Equinox</strong> translates from Latin <em>aequus</em> (equal) and <em>nox</em> (night).
    </p>
    <div class="p-3.5 rounded-xl bg-gradient-to-r from-emerald-950/50 via-slate-900 to-amber-950/50 border border-emerald-500/30">
        <h4 class="font-bold text-emerald-300 text-sm mb-2 flex items-center gap-2">
            <span>⚖️</span> The Geometry of the Equinox
        </h4>
        <p class="text-xs text-slate-300 leading-relaxed mb-2">
            On the equinox dates, Earth's axis of tilt is oriented <strong class="text-slate-100">perpendicular to the incoming solar rays</strong>.
        </p>
        <ul class="text-xs text-slate-300 space-y-1.5 list-disc list-inside">
            <li>The Sun is directly overhead at noon for an observer standing at the <strong class="text-amber-300">Equator (0° latitude)</strong>.</li>
            <li>The <strong class="text-cyan-300">circle of illumination</strong> passes directly through both the geographic North Pole and South Pole.</li>
            <li>Every city and town on Earth—from Tromsø in Norway to Nairobi in Kenya to Melbourne in Australia—experiences approximately <strong class="text-emerald-300 font-bold">12 hours of daylight and 12 hours of darkness</strong>!</li>
        </ul>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs text-slate-300">
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70">
            <h5 class="font-bold text-emerald-300 text-xs mb-1 flex items-center gap-1.5">
                <span>🌱</span> Vernal (Spring) Equinox: Around March 21
            </h5>
            <p>
                Marks the start of <strong class="text-slate-100">Spring</strong> in the Northern Hemisphere (leaves budding, warming temperatures) and the onset of <strong class="text-slate-100">Autumn</strong> in the Southern Hemisphere.
            </p>
        </div>
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70">
            <h5 class="font-bold text-amber-300 text-xs mb-1 flex items-center gap-1.5">
                <span>🍂</span> Autumnal Equinox: Around September 23
            </h5>
            <p>
                Marks the arrival of <strong class="text-slate-100">Autumn</strong> in the Northern Hemisphere (golden leaves, cooling weather) and the arrival of <strong class="text-slate-100">Spring</strong> in the Southern Hemisphere.
            </p>
        </div>
    </div>
</div>
""",
            "takeaways": [
                "On March 21 (Spring Equinox) and September 23 (Autumn Equinox), neither hemisphere tilts towards or away from the Sun.",
                "Sunlight falls vertically over the Equator, and the terminator runs through both geographic poles.",
                "Every location on Earth experiences equal 12-hour day and 12-hour night on equinoxes."
            ],
            "checkpoints": [
                {
                    "id": "cp11_1",
                    "question": "What does the Latin-derived word 'Equinox' literally mean?",
                    "options": [
                        "Burning Sun",
                        "Equal Night",
                        "Shortest Day",
                        "Frozen Earth"
                    ],
                    "correct": 1,
                    "explanation": "'Equinox' is derived from Latin 'aequus' (equal) and 'nox' (night), signifying equal 12-hour duration of day and night worldwide."
                },
                {
                    "id": "cp11_2",
                    "question": "On which two dates of the year do equinoxes occur across the globe?",
                    "options": [
                        "June 21 and December 22",
                        "January 1 and July 4",
                        "Around March 21 and September 23",
                        "October 31 and February 14"
                    ],
                    "correct": 2,
                    "explanation": "The Vernal Equinox occurs around March 21, and the Autumnal Equinox occurs around September 23."
                }
            ]
        },

        # Slide 12: 12.3 Celestial Shadow Alignment (Syzygy) & Eclipses
        {
            "id": 12,
            "slide_num": 12,
            "title": "12.3 Celestial Shadow Alignments & Eclipse Optics",
            "subtitle": "Chapter 12.3: Straight-Line Shadows, Umbra vs Penumbra in Space",
            "badge": "Eclipse Optics",
            "summary": "An eclipse is a natural celestial shadow event where the light from a luminous source (the Sun) is obstructed by an opaque celestial body (the Moon or the Earth). Because light travels in straight lines (rectilinear propagation), an illuminated opaque spherical body casts a dual-structured shadow cone into space: the dark inner Umbra and the lighter outer Penumbra.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        From Chapter 11, you learned that when an opaque object blocks straight-line light rays, a dark shadow forms behind it. In astronomy, when three celestial bodies align along a single straight line in space (a condition known as <strong class="text-amber-400">syzygy</strong>), one body casts its shadow onto another, creating an <strong class="text-cyan-400">eclipse</strong>.
    </p>
    <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70 space-y-3">
        <h4 class="font-bold text-amber-300 text-sm">The Anatomy of a Celestial Shadow Cone</h4>
        <p class="text-xs text-slate-300 leading-relaxed">
            Because the Sun is an extended luminous light source (not a tiny point), any illuminated sphere like Earth or the Moon produces two distinct shadow regions:
        </p>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
            <div class="p-3 rounded-lg bg-slate-950/70 border border-slate-800">
                <div class="flex items-center gap-2 mb-1">
                    <span class="w-3 h-3 rounded-full bg-slate-950 border border-slate-600"></span>
                    <strong class="text-slate-100 text-xs">1. The Umbra (Total Shadow)</strong>
                </div>
                <p class="text-xs text-slate-300 leading-relaxed">
                    The dark, converging central cone of complete shadow where <em>all</em> direct sunlight is blocked. An observer situated inside the umbra sees a <strong>Total Eclipse</strong>.
                </p>
            </div>
            <div class="p-3 rounded-lg bg-slate-950/70 border border-slate-800">
                <div class="flex items-center gap-2 mb-1">
                    <span class="w-3 h-3 rounded-full bg-slate-600"></span>
                    <strong class="text-slate-300 text-xs">2. The Penumbra (Partial Shadow)</strong>
                </div>
                <p class="text-xs text-slate-300 leading-relaxed">
                    The lighter, diverging outer shadow zone where only a <em>portion</em> of the Sun is obscured. An observer inside the penumbra sees a <strong>Partial Eclipse</strong>.
                </p>
            </div>
        </div>
    </div>
    <div class="p-3 rounded-lg bg-amber-950/40 border border-amber-500/30 text-xs text-slate-300">
        <strong class="text-amber-300">Two Types of Eclipses:</strong>
        <ul class="mt-1 space-y-0.5 list-disc list-inside">
            <li><strong class="text-slate-100">Solar Eclipse:</strong> The Moon passes between the Sun and Earth (Sun – Moon – Earth).</li>
            <li><strong class="text-slate-100">Lunar Eclipse:</strong> The Earth passes between the Sun and Moon (Sun – Earth – Moon).</li>
        </ul>
    </div>
</div>
""",
            "takeaways": [
                "Eclipses are celestial shadow events created by the straight-line propagation of sunlight.",
                "The Umbra is the dark central zone of total shadow where all direct sunlight is blocked.",
                "The Penumbra is the outer lighter zone of partial shadow where only part of the Sun is obscured."
            ],
            "checkpoints": [
                {
                    "id": "cp12_1",
                    "question": "What is the dark central region of a celestial shadow where all direct light from the Sun is blocked called?",
                    "options": [
                        "Penumbra",
                        "Corona",
                        "Umbra",
                        "Antumbra"
                    ],
                    "correct": 2,
                    "explanation": "The Umbra is the region of complete, total shadow where the entire light source is blocked."
                },
                {
                    "id": "cp12_2",
                    "question": "What fundamental property of light is responsible for the formation of sharp shadows and eclipses in space?",
                    "options": [
                        "Light bends into circular loops",
                        "Light travels in straight lines (rectilinear propagation)",
                        "Light travels backwards in space",
                        "Light only reflects off water"
                    ],
                    "correct": 1,
                    "explanation": "Because light travels in straight lines, opaque celestial obstacles like Earth or Moon block straight rays, casting defined shadows behind them."
                }
            ]
        },

        # Slide 13: 12.3.1 Solar Eclipse: The Moon Obstructs the Sun
        {
            "id": 13,
            "slide_num": 13,
            "title": "12.3.1 Solar Eclipse: The Moon Obstructs the Sun",
            "subtitle": "Chapter 12.3.1: Sun–Moon–Earth Alignment & The Path of Totality",
            "badge": "Solar Eclipses",
            "summary": "A solar eclipse occurs when the Moon, revolving in its orbit, passes directly between the Sun and the Earth (Sun – Moon – Earth alignment). This alignment can only happen during the New Moon (Amavasya) phase. The Moon casts its shadow onto the surface of the Earth, temporarily turning day into twilight.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        Imagine holding a single coin close to your eye; you can easily block out an entire building located hundreds of metres away! In a <strong class="text-amber-400">Solar Eclipse</strong>, the small Moon performs this exact cosmic trick, blocking the colossal Sun from our view on Earth.
    </p>
    <div class="p-3.5 rounded-xl bg-amber-950/40 border border-amber-500/30">
        <h4 class="font-bold text-amber-300 text-sm mb-2 flex items-center gap-2">
            <span>🌑</span> Alignment Order and Phase
        </h4>
        <div class="p-2.5 rounded-lg bg-slate-950/80 text-xs font-mono text-center text-amber-300 mb-2 border border-slate-700">
            ☀️ SUN &nbsp; ────▶ &nbsp; 🌑 MOON &nbsp; ────▶ &nbsp; 🌍 EARTH
        </div>
        <p class="text-xs text-slate-300 leading-relaxed">
            A solar eclipse can <strong class="text-amber-300">only occur on a New Moon day (Amavasya)</strong>, when the Moon's unlit side faces Earth and its illuminated face points toward the Sun.
        </p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs text-slate-300">
        <div class="p-3 rounded-lg bg-slate-900/80 border border-slate-700">
            <strong class="text-slate-100 block mb-1 text-sm font-bold">1. Total Solar Eclipse (Path of Totality):</strong>
            <p class="leading-relaxed">
                The tip of the Moon's dark umbral cone touches Earth, sweeping a narrow track across the continents (~100 to 250 km wide). Within this narrow strip, the Sun's bright disc is 100% covered. Stars emerge in daytime, temperatures drop noticeably, birds stop chirping, and the ethereal pearly white <strong>Solar Corona</strong> (the Sun's outer atmosphere) flashes into view!
            </p>
        </div>
        <div class="p-3 rounded-lg bg-slate-900/80 border border-slate-700">
            <strong class="text-slate-300 block mb-1 text-sm font-bold">2. Partial Solar Eclipse:</strong>
            <p class="leading-relaxed">
                Observers situated across the much broader penumbral shadow zone see only a portion of the Sun covered, appearing as though a celestial "bite" has been taken out of the solar disc.
            </p>
        </div>
    </div>
</div>
""",
            "takeaways": [
                "A solar eclipse occurs when the Moon passes directly between the Sun and the Earth (Sun – Moon – Earth).",
                "Solar eclipses can only take place during the New Moon (Amavasya) phase.",
                "Observers in the Moon's umbra experience a Total Solar Eclipse (corona visible), while those in the penumbra see a Partial Solar Eclipse."
            ],
            "checkpoints": [
                {
                    "id": "cp13_1",
                    "question": "What is the correct alignment of celestial bodies during a solar eclipse?",
                    "options": [
                        "Sun – Earth – Moon",
                        "Sun – Moon – Earth",
                        "Earth – Sun – Moon",
                        "Moon – Sun – Earth"
                    ],
                    "correct": 1,
                    "explanation": "During a solar eclipse, the Moon is situated in the middle, passing between the Sun and the Earth (Sun – Moon – Earth)."
                },
                {
                    "id": "cp13_2",
                    "question": "During which lunar phase is it exclusively possible for a solar eclipse to occur?",
                    "options": [
                        "Full Moon (Purnima)",
                        "First Quarter Moon",
                        "New Moon (Amavasya)",
                        "Waxing Gibbous Moon"
                    ],
                    "correct": 2,
                    "explanation": "The Moon can only stand directly between the Sun and Earth when its dark side faces Earth, which occurs exclusively at the New Moon (Amavasya) phase."
                }
            ]
        },

        # Slide 14: 12.3.1 The 400:1 Cosmic Coincidence & Safe Viewing
        {
            "id": 14,
            "slide_num": 14,
            "title": "12.3.1 The 400:1 Cosmic Ratio & Eye Safety",
            "subtitle": "Chapter 12.3.1: The Angular Size Match & How to Safely Observe a Solar Eclipse",
            "badge": "Safety & Optics",
            "summary": "By a remarkable celestial coincidence, the Sun is approximately 400 times wider than the Moon, but it is also approximately 400 times farther away from Earth. Consequently, both bodies have the exact same apparent angular diameter in our sky (~0.5°). Looking directly at the Sun during an eclipse without certified filters can permanently blind you via thermal retinal burns.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <div class="p-3.5 rounded-xl bg-cyan-950/40 border border-cyan-500/30">
        <h4 class="font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2">
            <span>✨</span> The 400:1 Cosmic Coincidence
        </h4>
        <p class="text-xs text-slate-300 leading-relaxed mb-2">
            Why does the tiny Moon (~3,474 km) fit so perfectly over the colossal Sun (~1,392,700 km)?
        </p>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs">
            <div class="p-2 rounded bg-slate-900 border border-slate-700">
                <strong class="text-amber-300">Diameter Ratio:</strong><br>
                Sun is ~400 times larger in diameter than the Moon.
            </div>
            <div class="p-2 rounded bg-slate-900 border border-slate-700">
                <strong class="text-cyan-300">Distance Ratio:</strong><br>
                Sun is ~400 times farther away from Earth than the Moon.
            </div>
        </div>
        <p class="text-xs text-slate-200 mt-2 font-semibold">
            Result: Both appear almost identically sized in the sky, spanning an angular width of approximately <span class="text-amber-400 font-mono">0.5 degrees (½°)</span>!
        </p>
    </div>
    <div class="p-3.5 rounded-xl bg-rose-950/40 border border-rose-500/30 space-y-2">
        <h4 class="font-bold text-rose-300 text-sm flex items-center gap-2">
            <span>⚠️</span> CRITICAL SAFETY WARNING: Eclipse Eye Protection
        </h4>
        <p class="text-xs text-slate-300 leading-relaxed">
            <strong class="text-rose-400">NEVER, under any circumstances, look directly at the Sun or a solar eclipse with naked eyes, regular sunglasses, x-ray films, or smoked glass!</strong> The intense infrared and ultraviolet radiation focuses onto your retina, causing painless, irreversible blindness (<em class="text-slate-100">solar retinopathy</em>) in mere seconds.
        </p>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs text-slate-200 pt-1">
            <div class="p-2 rounded bg-slate-900/90 border border-emerald-500/30">
                <strong class="text-emerald-400">Safe Methods:</strong>
                <ul class="list-disc list-inside mt-1 space-y-0.5 text-slate-300">
                    <li>Certified <strong>ISO 12312-2</strong> eclipse viewing glasses.</li>
                    <li>Welder's glass shade 14.</li>
                    <li><strong>Pinhole projection box:</strong> Projecting sunlight through a pinhole onto white cardboard.</li>
                    <li>Dappled sunlight through tree leaves onto the sidewalk.</li>
                </ul>
            </div>
            <div class="p-2 rounded bg-slate-900/90 border border-rose-500/30">
                <strong class="text-rose-400">Dangerous / Forbidden:</strong>
                <ul class="list-disc list-inside mt-1 space-y-0.5 text-slate-300">
                    <li>Naked eyes.</li>
                    <li>Regular black sunglasses (even 10 stacked pairs!).</li>
                    <li>Exposed photographic film or medical X-rays.</li>
                    <li>Looking through telescopes or binoculars without certified front-aperture solar filters.</li>
                </ul>
            </div>
        </div>
    </div>
</div>
""",
            "takeaways": [
                "The Sun is ~400× wider than the Moon but ~400× farther away, making them appear identical in angular size (~0.5°).",
                "Looking directly at the Sun during an eclipse without certified protection can cause permanent blindness.",
                "Safe observation requires certified ISO 12312-2 solar viewers or indirect pinhole projection."
            ],
            "checkpoints": [
                {
                    "id": "cp14_1",
                    "question": "Why does the Moon appear to be the exact same size in the sky as the colossal Sun?",
                    "options": [
                        "The Moon and Sun are physically the identical diameter",
                        "The Sun is ~400 times wider than the Moon, but also ~400 times farther away",
                        "Earth's atmosphere magnifies the Moon by 400 times",
                        "It is an optical trick played by the northern lights"
                    ],
                    "correct": 1,
                    "explanation": "Because the Sun's diameter is ~400 times greater than the Moon's, but its distance is also ~400 times greater, both span the exact same ~0.5° angular diameter from Earth's surface."
                },
                {
                    "id": "cp14_2",
                    "question": "Which of the following is a SAFE method to observe a solar eclipse?",
                    "options": [
                        "Wearing dark designer sunglasses",
                        "Looking through an exposed medical X-ray film",
                        "Using a certified ISO 12312-2 eclipse viewer or indirect pinhole cardboard projection",
                        "Looking through smoked glass over a candle"
                    ],
                    "correct": 2,
                    "explanation": "Only certified ISO 12312-2 solar filters or indirect pinhole projection safeguard your eyes from permanent retinal burning caused by invisible infrared and ultraviolet radiation."
                }
            ]
        },

        # Slide 15: 12.3.2 Lunar Eclipse: Earth's Shadow on the Moon
        {
            "id": 15,
            "slide_num": 15,
            "title": "12.3.2 Lunar Eclipse: Earth's Shadow on the Moon",
            "subtitle": "Chapter 12.3.2: Sun–Earth–Moon Alignment & The Vast Terrestrial Shadow Cone",
            "badge": "Lunar Eclipses",
            "summary": "A lunar eclipse occurs when the Earth, in its orbit around the Sun, moves directly between the Sun and the Moon (Sun – Earth – Moon alignment). This alignment can only occur during the Full Moon (Purnima) phase. The Earth casts its gigantic shadow cone into space, eclipsing the lunar disc. Unlike solar eclipses, lunar eclipses are visible to everyone on Earth's night side and are 100% safe to watch with naked eyes.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <p class="leading-relaxed">
        While a solar eclipse is caused by the Moon's small shadow falling onto Earth, a <strong class="text-cyan-400">Lunar Eclipse</strong> occurs when our massive home planet Earth casts its colossal shadow onto the Moon!
    </p>
    <div class="p-3.5 rounded-xl bg-indigo-950/40 border border-indigo-500/30">
        <h4 class="font-bold text-indigo-300 text-sm mb-2 flex items-center gap-2">
            <span>🌕</span> Alignment Order and Phase
        </h4>
        <div class="p-2.5 rounded-lg bg-slate-950/80 text-xs font-mono text-center text-cyan-300 mb-2 border border-slate-700">
            ☀️ SUN &nbsp; ────▶ &nbsp; 🌍 EARTH &nbsp; ────▶ &nbsp; 🌕 MOON
        </div>
        <p class="text-xs text-slate-300 leading-relaxed">
            A lunar eclipse can <strong class="text-cyan-300">only occur on a Full Moon night (Purnima)</strong>, when the Moon is directly opposite the Sun in our sky and fully illuminated.
        </p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs text-slate-300">
        <div class="p-3 rounded-lg bg-slate-900/80 border border-slate-700">
            <strong class="text-slate-100 block mb-1 text-sm font-bold">1. Stages of a Lunar Eclipse:</strong>
            <ul class="space-y-1 list-disc list-inside">
                <li><strong class="text-slate-300">Penumbral Stage:</strong> Moon enters Earth's outer penumbra; causes faint, subtle dimming often unnoticed by casual observers.</li>
                <li><strong class="text-amber-300">Partial Eclipse:</strong> Moon begins entering Earth's dark umbra; a distinct dark curved bite appears on the Moon's edge.</li>
                <li><strong class="text-rose-400">Total Eclipse:</strong> The entire Moon passes inside Earth's umbral cone; totality can last for well over an hour!</li>
            </ul>
        </div>
        <div class="p-3 rounded-lg bg-slate-900/80 border border-slate-700">
            <strong class="text-emerald-300 block mb-1 text-sm font-bold">2. Key Features of Lunar Eclipses:</strong>
            <ul class="space-y-1 list-disc list-inside">
                <li><strong class="text-emerald-400 font-bold">100% Safe to Watch:</strong> Moonlight is merely gentle reflected sunlight; viewing a lunar eclipse with naked eyes, binoculars, or telescopes is completely safe.</li>
                <li><strong class="text-slate-100">Broad Visibility:</strong> A solar eclipse is visible only along a narrow strip, but a lunar eclipse can be watched by everyone on the entire nighttime hemisphere of Earth!</li>
                <li><strong class="text-slate-100">Curved Shadow Proof:</strong> The edge of Earth's shadow on the Moon is always curved, which ancient Greeks and Aryabhata recognized as definitive proof that Earth is a sphere!</li>
            </ul>
        </div>
    </div>
</div>
""",
            "takeaways": [
                "A lunar eclipse occurs when the Earth stands between the Sun and the Moon (Sun – Earth – Moon).",
                "Lunar eclipses can only take place during the Full Moon (Purnima) phase.",
                "Lunar eclipses are visible from anywhere on the night side of Earth and are completely safe to view with the naked eye."
            ],
            "checkpoints": [
                {
                    "id": "cp15_1",
                    "question": "What is the alignment of celestial bodies during a lunar eclipse?",
                    "options": [
                        "Sun – Moon – Earth",
                        "Sun – Earth – Moon",
                        "Moon – Sun – Earth",
                        "Earth – Moon – Sun"
                    ],
                    "correct": 1,
                    "explanation": "During a lunar eclipse, the Earth is in the center, between the Sun and the Moon (Sun – Earth – Moon)."
                },
                {
                    "id": "cp15_2",
                    "question": "During which lunar phase is it exclusively possible for a lunar eclipse to occur?",
                    "options": [
                        "New Moon (Amavasya)",
                        "Crescent Moon",
                        "Full Moon (Purnima)",
                        "First Quarter"
                    ],
                    "correct": 2,
                    "explanation": "A lunar eclipse can only take place when the Moon is directly opposite the Sun in our sky, which occurs exclusively at the Full Moon (Purnima) phase."
                }
            ]
        },

        # Slide 16: 12.3.2 The Blood Moon & Why Eclipses Are Rare (The 5° Orbital Tilt)
        {
            "id": 16,
            "slide_num": 16,
            "title": "12.3.2 The Blood Moon & The 5° Orbital Tilt",
            "subtitle": "Chapter 12.3.2: Atmospheric Rayleigh Refraction & Why Eclipses Don't Occur Every Month",
            "badge": "Atmospheric Optics",
            "summary": "During totality in a lunar eclipse, the Moon does not disappear into total blackness; it glows an eerie coppery-red, known as a Blood Moon. This is caused by Rayleigh scattering and atmospheric refraction bending red sunsets into Earth's shadow cone. Furthermore, eclipses do NOT happen every New and Full Moon because the Moon's orbit is tilted at 5.14° to Earth's orbital plane.",
            "theory": """
<div class="space-y-4 text-slate-200">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
        <div class="p-3.5 rounded-xl bg-rose-950/40 border border-rose-500/30">
            <h4 class="font-bold text-rose-300 text-sm mb-1.5 flex items-center gap-2">
                <span>🔴</span> Why Does the Moon Turn Red? (Blood Moon)
            </h4>
            <p class="text-xs text-slate-300 leading-relaxed mb-2">
                If Earth completely blocks all direct sunlight, why does the totally eclipsed Moon glow copper-red instead of pitch black?
            </p>
            <ul class="text-xs text-slate-300 space-y-1 list-disc list-inside">
                <li>Earth is enveloped in a blanket of atmosphere.</li>
                <li>As sunlight skims through Earth's atmosphere, short blue wavelengths are scattered away in all directions (<strong class="text-slate-100">Rayleigh scattering</strong>).</li>
                <li>Longer red and orange wavelengths pass through and get <strong class="text-amber-300">refracted (bent)</strong> inward by the atmosphere into Earth's dark umbral cone.</li>
                <li>This redirected red light shines onto the Moon. If you stood on the Moon during totality, you would look back and see a brilliant glowing red ring: <strong class="text-rose-300 font-semibold">every sunrise and sunset on Earth occurring at the exact same moment!</strong></li>
            </ul>
        </div>
        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70">
            <h4 class="font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2">
                <span>📐</span> Why Don't Eclipses Occur Every Month?
            </h4>
            <p class="text-xs text-slate-300 leading-relaxed mb-2">
                If the Moon orbits Earth every 29.5 days, why isn't there a solar eclipse every New Moon and a lunar eclipse every Full Moon?
            </p>
            <ul class="text-xs text-slate-300 space-y-1 list-disc list-inside">
                <li><strong class="text-amber-300 font-bold">The 5.14° Orbital Tilt:</strong> The plane of the Moon's orbit around Earth is tilted at an angle of approximately <strong class="text-amber-300 font-mono">5.14°</strong> relative to Earth's orbital plane (the ecliptic).</li>
                <li>In most months, the New Moon passes slightly <strong>above or below</strong> the Sun in the sky, so its shadow misses Earth entirely.</li>
                <li>Similarly, at most Full Moons, the Moon passes slightly above or below Earth's shadow cone.</li>
                <li>Eclipses can only occur when the Sun, Earth, and Moon line up precisely near the two intersection points of their orbital planes, called the <strong class="text-cyan-300">orbital nodes</strong> (known in ancient Indian astronomy as <em>Rahu</em> and <em>Ketu</em>)!</li>
            </ul>
        </div>
    </div>
    <div class="p-3 rounded-lg bg-emerald-950/40 border border-emerald-500/30 text-xs text-slate-300">
        <strong class="text-emerald-300">Aryabhata's Eclipse Breakthrough (499 CE):</strong> For centuries, superstition claimed eclipses were caused by demons (Rahu and Ketu) physically swallowing the Sun and Moon. In the <em>Aryabhatiya</em>, Acharya Aryabhata courageously proved mathematically that lunar eclipses are simply the Moon entering Earth's shadow (<em>Bhuchhaya</em>), and solar eclipses are the Moon blocking the Sun!
    </div>
</div>
""",
            "takeaways": [
                "The Moon turns red during a total lunar eclipse because Earth's atmosphere scatters blue light and refracts red sunlight into the umbra.",
                "Eclipses do NOT occur every month because the Moon's orbit is tilted at ~5° to Earth's orbital plane.",
                "Eclipses only occur when celestial bodies align precisely at the orbital intersection points (nodes)."
            ],
            "checkpoints": [
                {
                    "id": "cp16_1",
                    "question": "Why does the Moon appear copper-red (Blood Moon) during a total lunar eclipse instead of becoming completely invisible?",
                    "options": [
                        "The Moon heats up and glows red like hot iron",
                        "Earth's atmosphere scatters blue light and refracts bent red sunlight into the umbral shadow",
                        "Volcanoes on the Moon erupt during eclipses",
                        "The Sun turns off all red light"
                    ],
                    "correct": 1,
                    "explanation": "Rayleigh scattering strips away short blue light in Earth's atmosphere, while long red wavelengths are bent (refracted) inward into Earth's shadow cone, gently illuminating the Moon in copper-red."
                },
                {
                    "id": "cp16_2",
                    "question": "Why do solar and lunar eclipses NOT occur every single month during New Moon and Full Moon?",
                    "options": [
                        "The Moon stops moving for two weeks every month",
                        "The Moon's orbit is tilted at approximately 5° relative to Earth's orbital plane",
                        "The Sun's gravity turns off eclipses",
                        "Clouds in space block the shadows"
                    ],
                    "correct": 1,
                    "explanation": "Because the Moon's orbit is tilted at ~5° to the ecliptic, at most New and Full Moons the Moon passes slightly above or below the alignment line, missing the shadow cone."
                }
            ]
        },

        # Slide 17: Mastery Challenge 1 (Rotation & Day-Night Mechanics)
        {
            "id": 17,
            "slide_num": 17,
            "title": "Mastery Challenge 1: Earth's Rotation & Apparent Motion",
            "subtitle": "Interactive Assessment • Questions 1 to 10 with Step-by-Step Pop-up Solutions",
            "badge": "Challenge 1",
            "summary": "Put your understanding of Earth's axial rotation, rotation period, equatorial velocity, circle of illumination, apparent celestial motions, and Acharya Aryabhata's historic insights to the test across 10 challenging questions.",
            "quiz_questions": [
                {
                    "id": "q17_1",
                    "question": "What is the primary physical consequence of the Earth rotating on its own axis?",
                    "options": [
                        "The cycle of four seasons",
                        "The alternation of day and night",
                        "Solar and lunar eclipses",
                        "The Moon changing its physical shape"
                    ],
                    "correct": 1,
                    "solution": "Earth's rotation on its axis once every 24 hours causes locations to continuously turn into sunlight (day) and away into shadow (night)."
                },
                {
                    "id": "q17_2",
                    "question": "In what direction does the Earth rotate on its axis when viewed from above the North Pole?",
                    "options": [
                        "Clockwise (East to West)",
                        "Anti-clockwise (West to East)",
                        "North to South",
                        "South to North"
                    ],
                    "correct": 1,
                    "solution": "When viewed from above the North Pole, Earth rotates anti-clockwise, which corresponds to rotating from West to East."
                },
                {
                    "id": "q17_3",
                    "question": "What is the approximate speed of rotation of the Earth's surface at the Equator?",
                    "options": [
                        "10 km/h",
                        "100 km/h",
                        "~1,670 km/h",
                        "300,000 km/s"
                    ],
                    "correct": 2,
                    "solution": "The equatorial circumference is ~40,075 km. Completed in 24 hours, speed = 40,075 ÷ 24 ≈ 1,670 km/h."
                },
                {
                    "id": "q17_4",
                    "question": "What is the circular boundary line that divides the daylit hemisphere of Earth from the night hemisphere called?",
                    "options": [
                        "The Tropic of Cancer",
                        "The Circle of Illumination (Terminator)",
                        "The Prime Meridian",
                        "The International Date Line"
                    ],
                    "correct": 1,
                    "solution": "The circle of illumination (or terminator) is the great circle dividing the sunlit day hemisphere from the darkened night hemisphere."
                },
                {
                    "id": "q17_5",
                    "question": "Why do the Sun, Moon, and stars appear to rise in the East and set in the West?",
                    "options": [
                        "They physically revolve around Earth once every 24 hours",
                        "Earth's real West-to-East rotation creates an apparent East-to-West motion",
                        "Atmospheric winds blow the stars westward",
                        "Earth's magnetic field repels the Sun towards the West"
                    ],
                    "correct": 1,
                    "solution": "Just as trees appear to move backwards when viewed from a forward-moving train, Earth's West-to-East spin makes celestial bodies appear to drift East-to-West."
                },
                {
                    "id": "q17_6",
                    "question": "Which ancient Indian astronomer first stated in 499 CE that the Earth rotates on its axis and used a moving boat analogy to explain it?",
                    "options": [
                        "Varahamihira",
                        "Acharya Aryabhata",
                        "Brahmagupta",
                        "Bhaskaracharya"
                    ],
                    "correct": 1,
                    "solution": "Acharya Aryabhata in his treatise Aryabhatiya (499 CE) stated that the Earth rotates on its axis, comparing it to stationary trees appearing to move backwards from a moving boat."
                },
                {
                    "id": "q17_7",
                    "question": "Why does Polaris (the North Star) appear stationary in the night sky while all other stars seem to rotate around it?",
                    "options": [
                        "It is the closest star to the Earth",
                        "It lies almost exactly along the northern extension of Earth's rotational axis",
                        "It is anchored by the gravitational pull of the Moon",
                        "It only emits light when Earth stops spinning"
                    ],
                    "correct": 1,
                    "solution": "Polaris lies directly along the projection of Earth's axis of rotation, like the stationary central axle of a spinning wheel."
                },
                {
                    "id": "q17_8",
                    "question": "What is the duration of one mean solar day on Earth?",
                    "options": [
                        "12 hours",
                        "24 hours",
                        "28 days",
                        "365 days"
                    ],
                    "correct": 1,
                    "solution": "One mean solar day is defined as the time taken for the Sun to return to the same meridian in the sky, which is exactly 24 hours (86,400 seconds)."
                },
                {
                    "id": "q17_9",
                    "question": "If an astronaut stands on the Moon looking at the Earth, does the Earth appear to rise and set like the Moon does from Earth?",
                    "options": [
                        "Yes, every 24 hours",
                        "No, because the Moon is tidally locked to Earth, the Earth stays virtually fixed in the lunar sky, rotating in place",
                        "No, the Earth is invisible from the Moon",
                        "Yes, but only during solar eclipses"
                    ],
                    "correct": 1,
                    "solution": "Because the Moon keeps the same face turned towards Earth (synchronous rotation), from any given spot on the near side of the Moon, Earth remains hanging in almost the exact same spot in the sky."
                },
                {
                    "id": "q17_10",
                    "question": "Which Indian state witnesses the sunrise earliest each morning?",
                    "options": [
                        "Gujarat",
                        "Arunachal Pradesh",
                        "Kerala",
                        "Rajasthan"
                    ],
                    "correct": 1,
                    "solution": "Because Earth spins from West to East, easternmost locations turn into the sunlight first. Arunachal Pradesh (literally 'land of the dawn-lit mountains') sees sunrise first in India."
                }
            ]
        },

        # Slide 18: Mastery Challenge 2 (Revolution, Leap Year & Night Sky)
        {
            "id": 18,
            "slide_num": 18,
            "title": "Mastery Challenge 2: Revolution, Orbits & Seasonal Sky",
            "subtitle": "Interactive Assessment • Questions 11 to 20 with Step-by-Step Pop-up Solutions",
            "badge": "Challenge 2",
            "summary": "Test your mastery of Earth's 365¼-day revolution around the Sun, orbital velocity, leap year calculations, and the shifting constellations of the seasonal night sky.",
            "quiz_questions": [
                {
                    "id": "q18_1",
                    "question": "How long does the Earth take to complete one full revolution around the Sun?",
                    "options": [
                        "24 hours",
                        "30 days",
                        "365 days and approximately 6 hours",
                        "500 days"
                    ],
                    "correct": 2,
                    "solution": "Earth's orbital revolution around the Sun requires approximately 365 days, 5 hours, 48 minutes, and 46 seconds (~365¼ days)."
                },
                {
                    "id": "q18_2",
                    "question": "What is the average orbital velocity of planet Earth as it revolves around the Sun?",
                    "options": [
                        "1,670 km/h",
                        "Approximately 29.8 km/s (~107,000 km/h)",
                        "300,000 km/s",
                        "100 km/h"
                    ],
                    "correct": 1,
                    "solution": "Earth covers its 940 million kilometre orbit at a breathtaking speed of approximately 29.8 km/s (nearly 107,000 km/h)."
                },
                {
                    "id": "q18_3",
                    "question": "How many days are there in a standard Leap Year, and which month receives an extra day?",
                    "options": [
                        "365 days; January has 32 days",
                        "366 days; February has 29 days",
                        "364 days; December has 30 days",
                        "366 days; July has 32 days"
                    ],
                    "correct": 1,
                    "solution": "A leap year contains 366 days, with the extra day appended to February (29 days instead of 28) to account for the accumulated 6 hours per year."
                },
                {
                    "id": "q18_4",
                    "question": "Why do the constellations visible in the night sky change progressively from month to month?",
                    "options": [
                        "Stars drift randomly through space every few weeks",
                        "As Earth revolves around the Sun, the night side faces different sectors of outer space",
                        "Earth's magnetic poles reverse every month",
                        "The Sun's gravity turns stars off in summer"
                    ],
                    "correct": 1,
                    "solution": "Night is the hemisphere facing away from the Sun. As Earth journeys around the Sun, that outward nighttime gaze sweeps across different constellations."
                },
                {
                    "id": "q18_5",
                    "question": "Due to Earth's orbital advance, approximately how much earlier does a star rise each successive night?",
                    "options": [
                        "4 minutes earlier",
                        "1 hour earlier",
                        "24 hours earlier",
                        "It rises at the same time"
                    ],
                    "correct": 0,
                    "solution": "Earth moves ~1° around the Sun each day (360° ÷ 365 days). This ~1° shift causes stars to rise ~4 minutes earlier each night (2 hours earlier per month)."
                },
                {
                    "id": "q18_6",
                    "question": "If a bright star rises at 9:00 PM on October 15, approximately what time will it rise on November 15 (30 days later)?",
                    "options": [
                        "11:00 PM (2 hours later)",
                        "7:00 PM (2 hours earlier)",
                        "9:00 PM (exact same time)",
                        "3:00 AM"
                    ],
                    "correct": 1,
                    "solution": "30 days × 4 minutes/day = 120 minutes = 2 hours earlier. 9:00 PM minus 2 hours = 7:00 PM."
                },
                {
                    "id": "q18_7",
                    "question": "Which famous constellation featuring three bright belt stars is predominantly visible in the winter night sky in India?",
                    "options": [
                        "Orion (Mriga / The Hunter)",
                        "Scorpius (Vrishchika)",
                        "Cygnus (The Swan)",
                        "Ursa Minor"
                    ],
                    "correct": 0,
                    "solution": "Orion (Mriga) is a quintessential winter constellation, easily recognized by its distinctive three-star belt."
                },
                {
                    "id": "q18_8",
                    "question": "What is the shape of Earth's orbit around the Sun?",
                    "options": [
                        "A perfect circle with the Sun exactly in the dead center",
                        "An ellipse (slightly flattened circle) with the Sun at one focus",
                        "A figure-8 spiral",
                        "A zigzag triangle"
                    ],
                    "correct": 1,
                    "solution": "According to Kepler's First Law, Earth's orbit is an ellipse with a very low eccentricity (0.0167), making it nearly circular."
                },
                {
                    "id": "q18_9",
                    "question": "What term describes the point in Earth's orbit where it is farthest from the Sun?",
                    "options": [
                        "Perihelion",
                        "Aphelion",
                        "Perigee",
                        "Solstice"
                    ],
                    "correct": 1,
                    "solution": "Aphelion (occurring around July 4) is the point in Earth's orbit farthest from the Sun (~152.1 million km)."
                },
                {
                    "id": "q18_10",
                    "question": "Which leap year rule ensures long-term astronomical alignment for century years?",
                    "options": [
                        "All century years are leap years",
                        "Century years are only leap years if divisible by 400 (e.g., 2000 was, but 1900 was not)",
                        "Century years have 370 days",
                        "Century years skip February completely"
                    ],
                    "correct": 1,
                    "solution": "In the Gregorian calendar, century years must be divisible by 400 to be leap years (2000 was a leap year, but 1900 and 2100 are common years)."
                }
            ]
        },

        # Slide 19: Mastery Challenge 3 (Axial Tilt, Solstices & Seasons)
        {
            "id": 19,
            "slide_num": 19,
            "title": "Mastery Challenge 3: Axial Tilt, Seasons & Solstices",
            "subtitle": "Interactive Assessment • Questions 21 to 30 with Step-by-Step Pop-up Solutions",
            "badge": "Challenge 3",
            "summary": "Assess your understanding of Earth's 23.5° axial tilt, direct versus slanted solar rays, summer and winter solstices, equinoxes, and hemispheric seasonal opposition.",
            "quiz_questions": [
                {
                    "id": "q19_1",
                    "question": "What is the primary cause of seasons on planet Earth?",
                    "options": [
                        "Changes in the distance between the Earth and the Sun",
                        "The tilt of Earth's axis of rotation combined with its revolution around the Sun",
                        "Ocean currents speeding up and slowing down",
                        "The Moon blocking solar heat during winter"
                    ],
                    "correct": 1,
                    "solution": "Earth's 23.5° axial tilt combined with its revolution changes the angle and duration of sunlight hitting each hemisphere throughout the year."
                },
                {
                    "id": "q19_2",
                    "question": "What is the angle of tilt of Earth's axis relative to the plane of its orbit?",
                    "options": [
                        "23.5°",
                        "66.5°",
                        "90.0°",
                        "0.0°"
                    ],
                    "correct": 1,
                    "solution": "The axis tilts 23.5° from the perpendicular to the orbit, which means it makes an angle of 90° − 23.5° = 66.5° with the orbital plane itself."
                },
                {
                    "id": "q19_3",
                    "question": "On which date does the Summer Solstice occur in the Northern Hemisphere?",
                    "options": [
                        "March 21",
                        "Around June 21",
                        "September 23",
                        "December 22"
                    ],
                    "correct": 1,
                    "solution": "The Summer Solstice in the Northern Hemisphere occurs around June 21, providing the longest daylight and shortest night of the year."
                },
                {
                    "id": "q19_4",
                    "question": "Over which line of latitude is the Sun directly overhead at noon during the June Summer Solstice?",
                    "options": [
                        "The Equator (0°)",
                        "The Tropic of Cancer (23.5°N)",
                        "The Tropic of Capricorn (23.5°S)",
                        "The Antarctic Circle (66.5°S)"
                    ],
                    "correct": 1,
                    "solution": "During the June solstice, the Northern Hemisphere is tilted towards the Sun, bringing direct overhead rays to the Tropic of Cancer (23.5°N)."
                },
                {
                    "id": "q19_5",
                    "question": "What is the term for the two days of the year when day and night are of equal 12-hour length worldwide?",
                    "options": [
                        "Solstices",
                        "Equinoxes",
                        "Aphelion and Perihelion",
                        "Eclipses"
                    ],
                    "correct": 1,
                    "solution": "Equinoxes (occurring around March 21 and September 23) feature equal 12-hour day and 12-hour night everywhere on Earth."
                },
                {
                    "id": "q19_6",
                    "question": "Why is summer warmer than winter?",
                    "options": [
                        "The Sun burns hotter nuclear fuel in June",
                        "Sunlight strikes at a steeper, more direct angle and days are longer",
                        "Earth gets 50 million km closer to the Sun",
                        "Clouds vanish completely across the globe in summer"
                    ],
                    "correct": 1,
                    "solution": "In summer, direct sunlight concentrates energy over a smaller surface area, and longer daylight hours allow more heat energy to accumulate."
                },
                {
                    "id": "q19_7",
                    "question": "During the December Winter Solstice (around Dec 22), which region experiences 24 hours of continuous polar daylight (Midnight Sun)?",
                    "options": [
                        "The North Pole and Arctic Circle (66.5°N to 90°N)",
                        "The Antarctic Circle and South Pole (66.5°S to 90°S)",
                        "The Equator",
                        "The Tropic of Cancer"
                    ],
                    "correct": 1,
                    "solution": "In December, the Southern Hemisphere tilts toward the Sun, placing Antarctica into continuous 24-hour sunlight, while the Arctic experiences 24-hour polar night."
                },
                {
                    "id": "q19_8",
                    "question": "If Earth's axis had ZERO tilt (0° to perpendicular, completely upright), what would happen to seasons?",
                    "options": [
                        "Seasons would become twice as extreme",
                        "There would be no seasons at all; every day would have 12h daylight and unchanged climate year-round",
                        "The entire Earth would instantly freeze solid",
                        "Night would disappear permanently"
                    ],
                    "correct": 1,
                    "solution": "Without axial tilt, the angle and duration of sunlight at any given latitude would remain identical every day of the year, eliminating seasons completely."
                },
                {
                    "id": "q19_9",
                    "question": "What season begins in the Southern Hemisphere on March 21 when the Northern Hemisphere enters Spring?",
                    "options": [
                        "Autumn (Fall)",
                        "Summer",
                        "Winter",
                        "Monsoon"
                    ],
                    "correct": 0,
                    "solution": "Seasons are opposite in the two hemispheres. When the Northern Hemisphere begins Spring in March, the Southern Hemisphere begins Autumn."
                },
                {
                    "id": "q19_10",
                    "question": "Where on Earth do day and night remain approximately 12 hours long throughout the entire year, regardless of seasons?",
                    "options": [
                        "The North Pole",
                        "The Equator (0° latitude)",
                        "The Arctic Circle",
                        "London, UK"
                    ],
                    "correct": 1,
                    "solution": "At the Equator, the circle of illumination cuts the latitude line in exact halves year-round, resulting in approximately 12 hours of day and 12 hours of night every single day."
                }
            ]
        },

        # Slide 20: Mastery Challenge 4 (Solar & Lunar Eclipses)
        {
            "id": 20,
            "slide_num": 20,
            "title": "Mastery Challenge 4: Solar & Lunar Eclipses",
            "subtitle": "Interactive Assessment • Questions 31 to 40 with Step-by-Step Pop-up Solutions",
            "badge": "Challenge 4",
            "summary": "Master the final frontier of celestial optics: the mechanics of solar and lunar eclipses, umbra vs penumbra, the 400:1 cosmic ratio, eclipse safety, the Blood Moon, and the 5° orbital inclination.",
            "quiz_questions": [
                {
                    "id": "q20_1",
                    "question": "What is the celestial alignment during a total solar eclipse?",
                    "options": [
                        "Sun – Earth – Moon",
                        "Sun – Moon – Earth",
                        "Earth – Sun – Moon",
                        "Moon – Sun – Earth"
                    ],
                    "correct": 1,
                    "solution": "In a solar eclipse, the Moon stands between the Sun and the Earth, casting its shadow onto the Earth."
                },
                {
                    "id": "q20_2",
                    "question": "A lunar eclipse can only occur during which lunar phase?",
                    "options": [
                        "New Moon (Amavasya)",
                        "First Quarter",
                        "Full Moon (Purnima)",
                        "Crescent Moon"
                    ],
                    "correct": 2,
                    "solution": "A lunar eclipse occurs when Earth stands directly between Sun and Moon, which can only happen during the Full Moon (Purnima) phase."
                },
                {
                    "id": "q20_3",
                    "question": "What is the dark inner region of a celestial shadow where all direct sunlight is blocked called?",
                    "options": [
                        "Penumbra",
                        "Umbra",
                        "Corona",
                        "Node"
                    ],
                    "correct": 1,
                    "solution": "The Umbra is the dark central cone of total shadow where all light from the Sun is blocked."
                },
                {
                    "id": "q20_4",
                    "question": "Why can the relatively small Moon completely cover the massive Sun during a total solar eclipse?",
                    "options": [
                        "The Moon expands in size during eclipses",
                        "The Sun is ~400 times wider than the Moon, but also ~400 times farther away",
                        "The Sun shrinks when the Moon approaches",
                        "Earth's atmosphere magnifies the Moon"
                    ],
                    "correct": 1,
                    "solution": "The Sun's diameter is ~400× that of the Moon, but its distance is also ~400× greater, giving both identical ~0.5° angular diameters in our sky."
                },
                {
                    "id": "q20_5",
                    "question": "What outer atmospheric layer of the Sun becomes spectacularly visible to the naked eye during totality in a solar eclipse?",
                    "options": [
                        "The Troposphere",
                        "The Solar Corona",
                        "The Photosphere",
                        "The Core"
                    ],
                    "correct": 1,
                    "solution": "When the Moon completely blocks the dazzling solar disc (photosphere), the pearly-white outer atmosphere—the Solar Corona—becomes visible."
                },
                {
                    "id": "q20_6",
                    "question": "Why does the Moon appear copper-red (Blood Moon) during a total lunar eclipse?",
                    "options": [
                        "The Moon is struck by red laser beams from satellites",
                        "Earth's atmosphere scatters blue light and refracts bent red sunlight into the umbra",
                        "The Moon catches on fire due to lack of sunlight",
                        "Sunspots emit red smoke"
                    ],
                    "correct": 1,
                    "solution": "Sunlight skimming past Earth has its blue light scattered away by Rayleigh scattering; the remaining red light is refracted into Earth's shadow cone onto the Moon."
                },
                {
                    "id": "q20_7",
                    "question": "Why do eclipses NOT happen every month at every New Moon and Full Moon?",
                    "options": [
                        "The Moon only has shadows once a year",
                        "The Moon's orbit is tilted at approximately 5° relative to Earth's orbital plane",
                        "The Sun stops emitting light at night",
                        "Space dust absorbs all shadows"
                    ],
                    "correct": 1,
                    "solution": "Because the Moon's orbit is tilted at ~5.14° to the ecliptic, the Moon usually passes slightly above or below the Sun-Earth line, causing the shadows to miss."
                },
                {
                    "id": "q20_8",
                    "question": "What is the ONLY completely safe way to directly observe a solar eclipse with your eyes?",
                    "options": [
                        "Squinting through your fingers",
                        "Wearing dark polarized sunglasses",
                        "Using certified ISO 12312-2 solar eclipse viewers or a pinhole projection box",
                        "Looking through a CD or DVD disc"
                    ],
                    "correct": 2,
                    "explanation": "Certified ISO 12312-2 eclipse viewers or indirect pinhole projection methods block harmful infrared and ultraviolet rays that cause painless permanent retinal burns.",
                    "solution": "Certified ISO 12312-2 eclipse viewers or indirect pinhole projection methods block harmful infrared and ultraviolet rays that cause painless permanent retinal burns."
                },
                {
                    "id": "q20_9",
                    "question": "How did ancient Greek astronomers and Acharya Aryabhata prove that the Earth is a sphere using lunar eclipses?",
                    "options": [
                        "They saw Earth's reflection in the ocean",
                        "Earth's shadow cast onto the Moon is always curved, regardless of the eclipse angle",
                        "They flew into space with hot air balloons",
                        "The Moon became square during eclipses"
                    ],
                    "correct": 1,
                    "solution": "Only a sphere always casts a circular, curved shadow in every orientation; a flat disc would cast an oval or straight-line shadow at various angles."
                },
                {
                    "id": "q20_10",
                    "question": "In ancient Indian astronomy, what names were given to the two orbital nodes where the Moon's tilted path crosses the ecliptic to cause eclipses?",
                    "options": [
                        "Surya and Chandra",
                        "Rahu and Ketu",
                        "Budha and Shukra",
                        "Agni and Vayu"
                    ],
                    "correct": 1,
                    "solution": "The ascending and descending intersection nodes of the Moon's orbit with the ecliptic were identified in ancient Indian astronomy as Rahu and Ketu."
                }
            ]
        }
    ]

    # Convert to python source
    with open(".agents/class7_science_earth_moon_sun_data.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""NCERT Class 7 Science Chapter 12: Earth, Moon, and the Sun Data Module."""\n\n')
        f.write(f"CHAPTER_META = {json.dumps(CHAPTER_META, indent=4, ensure_ascii=False)}\n\n")
        f.write(f"SLIDES = {json.dumps(SLIDES, indent=4, ensure_ascii=False)}\n")

    print(f"Successfully generated .agents/class7_science_earth_moon_sun_data.py with {len(SLIDES)} slides.")

    # Validation: check for raw LaTeX
    with open(".agents/class7_science_earth_moon_sun_data.py", "r", encoding="utf-8") as f:
        text = f.read()

    latex_pattern = re.compile(r'\\[a-zA-Z]+')
    matches = latex_pattern.findall(text)
    bad_latex = [m for m in matches if m not in ['\\n', '\\t', '\\r', '\\f', '\\b']]
    if bad_latex:
        print(f"WARNING: Found potential raw LaTeX commands: {bad_latex[:10]}")
    else:
        print("VERIFIED PASS: Zero raw LaTeX in data module!")

if __name__ == "__main__":
    create_data_file()

