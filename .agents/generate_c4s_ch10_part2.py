# -*- coding: utf-8 -*-
"""
Generate Slides 9 to 16 for Class 4 Science Chapter 10: Our Sky.
Strictly 195-215 words per speech.
Strictly 1-3 words per title.
2 checkpoints per slide with 4 options each.
Zero human character names, zero lecturer personas.
"""

import re
import json

slides_part2 = [
    {
        "id": 9,
        "title": "Dazzling Night Sky",
        "badge": "Stargazing Astronomy",
        "sim_id": "sim_night_stargazing",
        "description": "Observe thousands of sparkling stars against the velvet night sky, celestial constellations, and atmospheric twinkling.",
        "speech": "When twilight fades and the Sun sinks beneath the western horizon, the sky unveils one of nature's most breathtaking scientific panoramas: the dazzling night sky. In areas away from artificial city glare, the deep velvet darkness sparkles with thousands of distant twinkling stars. Each star is a gargantuan nuclear furnace burning trillions of kilometres away in interstellar space. Stars appear to twinkle, or scintillate, because their pinpoint light rays must travel through multiple turbulent layers of Earth's atmosphere, where varying air temperatures and shifting densities continuously bend the light rays before they reach our eyes. Over thousands of years, ancient human observers recognized that groups of bright stars form recognizable patterns, which astronomers call constellations. For example, observers in India easily identify the prominent constellation Ursa Major, revered in Indian tradition as the Saptarishi, seven bright stars forming a celestial ladle. The two outer pointer stars of the ladle align in a direct straight line toward Polaris, the steadfast North Pole Star that guides nocturnal navigators. Gazing upward at the sparkling night sky instills profound humility, showing us that our home planet Earth is part of an unimaginably vast, interconnected cosmos stretching across endless space.",
        "checkpoints": [
            {
                "q": "Why do distant stars appear to twinkle when observed from the surface of Earth?",
                "options": ["Their light bends through turbulent moving layers of atmospheric air", "The stars physically turn on and off like blinking electric bulbs", "Giant space clouds pass in front of every star every few seconds", "The Moon's gravity blocks and unblocks starlight continuously"],
                "ans": "Their light bends through turbulent moving layers of atmospheric air",
                "explanation": "Atmospheric scintillation occurs because starlight refracts through shifting air pockets of differing temperatures and densities in Earth's atmosphere."
            },
            {
                "q": "What traditional Indian astronomical name is given to the seven prominent stars of the Great Bear constellation?",
                "options": ["Saptarishi", "Navagraha", "Chandrayaan", "Surya Namaskar"],
                "ans": "Saptarishi",
                "explanation": "In Indian astronomy, the seven prominent stars forming the celestial ladle of Ursa Major are traditionally identified as the Saptarishi."
            }
        ]
    },
    {
        "id": 10,
        "title": "Moon Surface Glow",
        "badge": "Lunar Geology",
        "sim_id": "sim_moon_surface",
        "description": "Examine Earth's natural satellite, discovering that the Moon does not produce its own light but reflects bright sunlight.",
        "speech": "Dominating the night sky is the Moon, Earth's only natural satellite, orbiting our planet at an average distance of approximately three hundred and eighty-four thousand kilometres. Although the Moon glows with silvery brilliance at night, it is not a luminous body like the Sun or distant stars. The Moon does not produce any light or heat of its own. Instead, it acts like a colossal spherical rock mirror, reflecting a fraction of the bright sunlight that strikes its rugged dusty surface. When we observe the lunar surface through binoculars or an astronomical telescope, we discover an ancient, airless world scarred by billions of years of cosmic history. Dark, smooth lowland plains, historically called lunar maria, consist of solidified basaltic lava flows from ancient volcanic eruptions. Surrounding these darker plains are bright, heavily cratered highlands marked by impact craters formed when speeding meteorites and asteroids slammed into the lunar surface at cosmic velocities. Because the Moon possesses no protective atmospheric envelope, there is no wind, weather, or flowing liquid water to erode these features; consequently, astronaut footprints and meteorite craters remain preserved unchanged for millions of years across the silent, airless lunar landscape for future space scientists to explore.",
        "checkpoints": [
            {
                "q": "How does the Moon shine so brightly in the night sky if it has no light of its own?",
                "options": ["It reflects bright sunlight that falls upon its surface toward Earth", "It burns thick layers of coal and natural gas inside deep craters", "It absorbs lightning from clouds and stores it in lunar rocks", "It is covered in glowing bioluminescent jellyfish and fireflies"],
                "ans": "It reflects bright sunlight that falls upon its surface toward Earth",
                "explanation": "The Moon is a non-luminous body that shines entirely by reflecting incident solar radiation like a giant cosmic mirror."
            },
            {
                "q": "Why do meteorite craters and footprints on the Moon remain preserved for millions of years?",
                "options": ["The Moon has no atmosphere, wind, or rain to cause erosion", "The surface of the Moon is covered in wet liquid concrete", "Magnetic forces instantly freeze every rock in permanent place", "The Moon is surrounded by an impenetrable shield of solid ice"],
                "ans": "The Moon has no atmosphere, wind, or rain to cause erosion",
                "explanation": "Without an atmosphere or liquid water, there is no weather, rainfall, or wind erosion to degrade impact craters or footprints on the lunar surface."
            }
        ]
    },
    {
        "id": 11,
        "title": "Phases Of Moon",
        "badge": "Orbital Geometry",
        "sim_id": "sim_lunar_phases",
        "description": "Track the monthly 29.5-day lunar cycle from New Moon (Amavasya) to Full Moon (Poornima) and back as orbital angles change.",
        "speech": "One of the most captivating observations in astronomy is that the Moon appears to change its visible shape from night to night in a repeating monthly cycle. These changing visible shapes are known scientifically as the phases of the Moon. It is crucial to understand that the Moon itself never physically changes size or shape; it always remains a solid spherical rock. Exactly half of the Moon is continuously illuminated by the Sun, while the opposite half remains cast in shadow. As the Moon travels in its twenty-nine-and-a-half-day elliptical orbit around Earth, our perspective of that illuminated half changes continuously. When the Moon passes directly between Earth and the Sun, its sunlit hemisphere faces away from us, making the Moon completely invisible from Earth—a phase called the New Moon, or Amavasya. Over the following two weeks, as the Moon orbits eastward, we observe an expanding sliver of light: first a slender waxing crescent, then a half-moon, and a swelling gibbous moon, until the entire illuminated face points directly toward Earth, creating the radiant Full Moon, or Poornima. Following Poornima, the visible illuminated portion steadily wanes through crescent slivers until returning to Amavasya once again to begin the cycle anew.",
        "checkpoints": [
            {
                "q": "What is the lunar phase called when the illuminated side of the Moon faces away, making it invisible?",
                "options": ["New Moon (Amavasya)", "Full Moon (Poornima)", "Gibbous Moon", "Solar Eclipse"],
                "ans": "New Moon (Amavasya)",
                "explanation": "During New Moon (Amavasya), the Moon lies between the Earth and Sun, with its illuminated side facing away from our earthly perspective."
            },
            {
                "q": "Approximately how many days does the Moon take to complete one full cycle of lunar phases?",
                "options": ["About 29.5 days", "Exactly 365 days", "Only 24 hours", "About 7 days"],
                "ans": "About 29.5 days",
                "explanation": "The synodic lunar month, measuring the time from one New Moon to the next, takes approximately 29.5 days."
            }
        ]
    },
    {
        "id": 12,
        "title": "Lunar Calendar Festivals",
        "badge": "Cultural Chronometry",
        "sim_id": "sim_lunar_festivals",
        "description": "Discover how ancient cultures designed lunar calendars and how major Indian festivals align with specific Moon phases.",
        "speech": "Because the phases of the Moon cycle with predictable, observable precision every twenty-nine-and-a-half days, ancient human civilizations across the world utilized the lunar month as their earliest calendar system to measure the passage of time. In India, traditional astronomical calendars—such as the Hindu Panchang and the Islamic Hijri calendar—are fundamentally linked to the lunar cycle, designating each day as a specific tithi. Consequently, many of our most cherished national and cultural festivals are scheduled precisely to coincide with key phases of the Moon. The joyous festival of lights, Diwali, is celebrated on the darkest night of the year, the Kartik Amavasya, where millions of flickering earthen diyas illuminate homes in celebration of light over darkness. Conversely, festivals of spiritual enlightenment and gratitude—including Buddha Poornima, Guru Poornima, and Rakshabandhan—are celebrated beneath the radiant glow of the Full Moon, when the entire lunar disc shines brightly. The joyous festival of Eid is heralded by the first sighting of the delicate crescent moon in the twilight evening sky, while festivals like Karva Chauth and Chhath Puja involve evening prayers honoring the Moon and Sun, demonstrating the profound cultural bond between celestial rhythms and joyful human celebrations across generations of cultural heritage.",
        "checkpoints": [
            {
                "q": "On which lunar phase is the national festival of lights, Diwali, traditionally celebrated?",
                "options": ["Amavasya (New Moon)", "Poornima (Full Moon)", "First Quarter Half Moon", "Gibbous Moon"],
                "ans": "Amavasya (New Moon)",
                "explanation": "Diwali is celebrated on Kartik Amavasya, the darkest new moon night of the autumn season, illuminated by rows of oil lamps."
            },
            {
                "q": "Which major festival is celebrated immediately upon the first evening sighting of the slender crescent Moon?",
                "options": ["Eid", "Diwali", "Holi", "Christmas"],
                "ans": "Eid",
                "explanation": "The celebration of Eid-ul-Fitr begins with the certified first sighting of the crescent moon (hilal) marking the start of Shawwal."
            }
        ]
    },
    {
        "id": 13,
        "title": "Chandrayaan Lunar Landing",
        "badge": "Space Exploration",
        "sim_id": "sim_chandrayaan_landing",
        "description": "Celebrate India's historic Chandrayaan-3 mission, executing a soft touchdown near the lunar south pole on August 23, 2023.",
        "speech": "On August 23, 2023, India achieved a historic triumph in modern planetary science when the Indian Space Research Organisation, known as ISRO, successfully executed a flawless soft landing on the surface of the Moon with the Chandrayaan-3 mission. This remarkable technological milestone made India the fourth nation in human history to land spacecraft safely on the lunar surface, and the very first country ever to touch down near the unexplored lunar south polar region. Space scientists engineered the robust Vikram Lander, named in honor of the pioneer of the Indian space programme, Vikram Sarabhai. Landing on the Moon is extraordinarily difficult because the airless environment prevents the use of parachutes to slow down descending spacecraft. Instead, the Vikram Lander relied upon four throttleable liquid-propellant rocket engines that fired precisely in reverse, acting as retro-rockets to counteract gravitational acceleration and gently touch down on four shock-absorbing legs. Upon achieving touchdown, automated sensors confirmed stability and transmitted the historic message back to Earth: 'India is on the Moon!' In honor of this scientific achievement, August 23 is now celebrated across India as National Space Day, inspiring millions of young students to pursue careers in space science and astronomy.",
        "checkpoints": [
            {
                "q": "On which historic date did India's Chandrayaan-3 mission successfully achieve a soft landing on the Moon?",
                "options": ["August 23, 2023", "January 26, 2020", "October 2, 2022", "August 15, 2021"],
                "ans": "August 23, 2023",
                "explanation": "On August 23, 2023, ISRO's Vikram Lander made a historic soft landing near the south pole of the Moon, celebrated as National Space Day."
            },
            {
                "q": "Why cannot parachutes be used to slow down spacecraft landing on the surface of the Moon?",
                "options": ["The Moon has no atmosphere or air to create aerodynamic drag", "The Moon's surface is too cold for parachute fabric to open", "Parachutes only function when falling toward salty ocean waters", "The Moon's magnetic field immediately dissolves all nylon ropes"],
                "ans": "The Moon has no atmosphere or air to create aerodynamic drag",
                "explanation": "Parachutes require an atmosphere to generate aerodynamic drag resistance; because the Moon is an airless vacuum, retro-rocket thrusters are required."
            }
        ]
    },
    {
        "id": 14,
        "title": "Pragyan Surface Exploration",
        "badge": "Robotic Exploration",
        "sim_id": "sim_pragyan_rover",
        "description": "Investigate the six-wheeled Pragyan rover rolling onto lunar soil, analyzing regolith minerals and searching for water ice.",
        "speech": "Shortly after the Vikram Lander safely stabilized on the lunar surface, a motorized ramp deployed from its chassis, allowing the six-wheeled Pragyan robotic rover to roll gracefully onto the virgin lunar regolith. Pragyan, an ancient Sanskrit word signifying 'wisdom', was designed to operate as a mobile autonomous scientific laboratory. As the twenty-six-kilogram rover navigated across the undulating terrain, its specialized rear wheels permanently embossed the national emblem of India and the ISRO logo into the powdery lunar soil with every rotation. Pragyan deployed advanced scientific instruments, including the Alpha Particle X-Ray Spectrometer and the Laser-Induced Breakdown Spectroscope. By firing rapid laser pulses onto nearby lunar rocks, the spectrometer vaporized tiny mineral particles and analyzed the emitted optical spectrum, discovering unequivocal evidence of sulfur, aluminum, calcium, iron, titanium, and chromium in the south polar soil. Furthermore, thermal probes measured sharp temperature differences between the surface soil and subsurface layers just eight centimetres deep. Most importantly, scientists searched for hidden traces of subterranean water ice inside permanently shadowed polar craters, which future space missions could purify into drinking water and rocket fuel, opening pathways for permanent scientific bases on the Moon for future generations of scientists, engineers, and cosmic explorers.",
        "checkpoints": [
            {
                "q": "What was the name of the six-wheeled robotic rover carried to the Moon by the Vikram Lander?",
                "options": ["Pragyan", "Pushpak", "Gaganyaan", "Mangalyaan"],
                "ans": "Pragyan",
                "explanation": "The robotic lunar rover of Chandrayaan-3 was named Pragyan (meaning wisdom), designed to conduct mobile chemical exploration."
            },
            {
                "q": "What crucial element did Pragyan's laser-induced spectroscope definitively detect on the lunar south pole?",
                "options": ["Sulfur", "Liquid gasoline", "Solid plastic", "Pure table sugar"],
                "ans": "Sulfur",
                "explanation": "Pragyan's Laser-Induced Breakdown Spectroscope (LIBS) confirmed the unambiguous presence of sulfur on the lunar surface."
            }
        ]
    },
    {
        "id": 15,
        "title": "Apparent Solar Motion",
        "badge": "Celestial Mechanics",
        "sim_id": "sim_earth_rotation",
        "description": "Understand that the Sun's apparent East-to-West movement across the sky is an optical illusion caused by Earth's 24-hour axial rotation.",
        "speech": "When we watch the Sun rise in the east, climb through the sky at noon, and set in the west, our senses suggest that the Sun is physically moving around a stationary Earth. However, astronomical science reveals that this apparent motion is an optical illusion! In reality, it is our planet Earth that is constantly spinning like a giant top upon its own invisible central axis. Earth completes one full counter-clockwise rotation from west to east once every twenty-four hours. We can understand this illusion by imagining riding in a moving train: when your train smoothly pulls out of the railway platform, the trees, lampposts, and station benches appear to rush backwards in the opposite direction, even though they remain perfectly stationary on the ground. Similarly, because we stand firmly upon a rotating Earth spinning smoothly eastward, the stationary Sun and distant stars appear to sweep across our sky in the opposite direction, from east to west. Earth's steady axial rotation divides our days into continuous cycles of light and dark. The half of Earth facing toward the Sun experiences daylight, while the opposite half facing away rests in nighttime darkness, illustrating the mechanical elegance of celestial physics.",
        "checkpoints": [
            {
                "q": "What is the true scientific cause of the Sun appearing to move across the sky from East to West?",
                "options": ["Earth rotates upon its axis from West to East every 24 hours", "The Sun physically flies around the Earth like a giant airplane", "Earth remains completely stationary while the entire universe spins", "Giant ocean waves push the continents backwards throughout the day"],
                "ans": "Earth rotates upon its axis from West to East every 24 hours",
                "explanation": "The apparent East-to-West journey of the Sun is caused by Earth's continuous rotational spin from West to East every 24 hours."
            },
            {
                "q": "How long does Earth take to complete one full 360-degree rotation upon its axis?",
                "options": ["24 hours (one day)", "365 days (one year)", "60 minutes (one hour)", "30 days (one month)"],
                "ans": "24 hours (one day)",
                "explanation": "Earth completes one full axial rotation in approximately 24 hours, defining the standard planetary day-and-night cycle."
            }
        ]
    },
    {
        "id": 16,
        "title": "Sky Observations Synthesis",
        "badge": "Observational Astronomy",
        "sim_id": "sim_sky_tracker_matrix",
        "description": "Synthesize key sky phenomena comparing sunrise, midday zenith, sunset twilight, and the starlit nocturnal sky.",
        "speech": "As we conclude our comprehensive scientific investigation of the celestial realm, synthesizing our daily observations reveals the elegant harmony connecting the sky with terrestrial life. The sky is not a static ceiling; it is a dynamic cosmic theater governed by predictable physical principles. During the early morning, the eastern Sun projects long western shadows while songbirds awaken and flowers open their petals to capture soft sunlight. At midday, the Sun reaches its peak elevation, casting the shortest shadows of the day while delivering maximum thermal energy to power plant photosynthesis and the planetary water cycle. As evening twilight sets in, elongated eastern shadows mirror the setting western Sun, signaling daytime creatures to return to safe roosts while nocturnal hunters prepare for activity. Finally, the night sky provides a window into the wider universe, revealing thousands of twinkling stars, familiar constellations like the Saptarishi, and the serene Moon waxing and waning through its monthly phases to guide traditional calendars and cultural festivals. From ancient sundials at Jantar Mantar to modern lunar rovers exploring the south pole of the Moon, observing our sky inspires endless curiosity, scientific reasoning, and technological innovation across human generations for all time.",
        "checkpoints": [
            {
                "q": "What overarching scientific lesson is learned by documenting sky changes throughout the day and night?",
                "options": ["Predictable planetary motions govern daylight, shadows, temperatures, and living rhythms", "The sky changes randomly without following any physical rules of science", "Human beings have no ability to measure or predict when the Sun will rise", "The Moon and Sun are located at the exact same distance from our eyes"],
                "ans": "Predictable planetary motions govern daylight, shadows, temperatures, and living rhythms",
                "explanation": "Observing the sky demonstrates that regular celestial mechanics (Earth's rotation and lunar orbit) dictate diurnal cycles of light, heat, and life."
            },
            {
                "q": "Which Indian space mission achieved humanity's first historic landing near the lunar south pole?",
                "options": ["Chandrayaan-3", "Apollo 11", "Voyager 1", "Sputnik 1"],
                "ans": "Chandrayaan-3",
                "explanation": "India's Chandrayaan-3 mission made history on August 23, 2023, by achieving the first-ever soft landing near the Moon's south pole."
            }
        ]
    }
]

# Validation
HUMAN_NAMES = [
    'Meera', 'Dhruv', 'Raghav', 'Chandan', 'Navya', 'Amit', 'Reena', 'Pihu',
    'Gurpreet', 'Ritika', 'Chandni', 'Nayan', 'Satyajit Ray',
    'Dada', 'Dadaji', 'Diya', 'Raziya', 'Rukhsana', 'Simran', 'Sunil', 'Bablu',
    'Ikra', 'Samina', 'Sumedha', 'Vinayak', 'Kumar', 'Paridhi', 'Idha', 'Karan',
    'Jaspreet', 'Gulnaz', 'Mithali', 'Suzie', 'Bates', 'Gundappa', 'Muniamma',
    'Shirley', 'Shiv', 'Jagat', 'Bholu', 'Rani', 'Preet', 'Diksha', 'Raman',
    'Sheela', 'Sunita', 'Mary', 'Akira', 'Preetha', 'Adrit', 'Rohan', 'Anjali',
    'Aarav', 'Ananya', 'Priya', 'Rahul', 'Neha', 'Sanjay', 'Shrinathan',
    'Mirabai', 'Gulabo', 'Anvi', 'Raju', 'Parv', 'Chinnu', 'Abha', 'Didi',
    'Daisy', 'Lou', 'Sapan', 'Udaya', 'Krishna', 'Sudama', 'Mala', 'Neela', 'Bhola'
]

FORBIDDEN_PERSONAS = [
    r'\bDr\b', r'\bDr\.\b', r'\bSir\b', r'\bMadam\b', r'\bMr\b', r'\bMr\.\b', r'\bMrs\b', r'\bMrs\.\b', r'\bMiss\b'
]

print("=== CHECKING SLIDES 9 TO 16 ===")
for s in slides_part2:
    sid = s['id']
    title = s['title']
    wc = len(s['speech'].split())
    print(f"Slide {sid} '{title}': {wc} words")

for s in slides_part2:
    sid = s['id']
    title = s['title']
    title_words = len(title.split())
    assert 1 <= title_words <= 3, f"Slide {sid} title '{title}' must be 1-3 words (got {title_words})"
    
    wc = len(s['speech'].split())
    assert 195 <= wc <= 215, f"Slide {sid} speech word count out of range: {wc} words (must be 195-215)"
    
    s_str = json.dumps(s)
    for name in HUMAN_NAMES:
        assert not re.search(r'\b' + re.escape(name) + r'\b', s_str, re.IGNORECASE), f"Slide {sid} contains name '{name}'"
    for persona in FORBIDDEN_PERSONAS:
        assert not re.search(persona, s_str, re.IGNORECASE), f"Slide {sid} contains persona '{persona}'"
    
    assert len(s['checkpoints']) == 2, f"Slide {sid} must have 2 checkpoints"
    for cp in s['checkpoints']:
        assert len(cp['options']) == 4, f"Slide {sid} checkpoint must have 4 options"

print("Slides 9 to 16 verified successfully!")
