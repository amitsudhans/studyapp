# -*- coding: utf-8 -*-
"""
Generate Slides 1 to 8 for Class 4 Science Chapter 10: Our Sky.
Strictly 195-215 words per speech.
Strictly 1-3 words per title.
2 checkpoints per slide with 4 options each.
Zero human character names, zero lecturer personas.
"""

import re
import json

slides_part1 = [
    {
        "id": 1,
        "title": "Changing Daily Sky",
        "badge": "Diurnal Sky Rhythms",
        "sim_id": "sim_daily_sky_cycle",
        "description": "Observe how atmospheric light, color gradients, and solar positions transform across morning, afternoon, evening, and night.",
        "speech": "Welcome young astronomers to our scientific exploration of the celestial canopy above us. When we observe the sky throughout a single twenty-four-hour cycle, we witness an ever-changing spectacle of light, color, and motion. At dawn, as the Sun begins to rise along the eastern horizon, the dark sky brightens with soft amber, rose, and brilliant golden hues. The cool morning air fills with the gentle chirping of birds taking flight from their treetop roosts. By midday, the Sun ascends high into the sky, illuminating the landscape with intense white light and warming the terrestrial surface. The sky takes on a crisp azure blue shade because microscopic air molecules scatter high-frequency blue sunlight across the atmosphere. As late afternoon transitions toward twilight, the Sun descends toward the western horizon, painting dramatic crimson, purple, and fiery orange gradients across evening clouds. Once the Sun sinks completely below the horizon, darkness envelops the Earth, revealing the tranquil expanse of the night sky adorned with thousands of glistening stars and the glowing Moon. Tracking these predictable daily sky transformations teaches us how Earth's continuous rotation orchestrates the fundamental rhythms of daylight, temperature, and natural wonder across our planet every single day.",
        "checkpoints": [
            {
                "q": "What causes the sky to display brilliant orange and red colors during sunrise and sunset?",
                "options": ["Sunlight traveling through a thicker layer of atmosphere scatters away blue light", "The sky gets covered in red desert sand every morning and evening", "Giant fires burning on distant mountain peaks illuminate the clouds", "The Sun changes its physical chemical composition twice every day"],
                "ans": "Sunlight traveling through a thicker layer of atmosphere scatters away blue light",
                "explanation": "At sunrise and sunset, sunlight travels through a longer path of atmospheric air; shorter blue wavelengths scatter away, leaving longer red and orange wavelengths."
            },
            {
                "q": "In which cardinal direction does the Sun appear to rise at the beginning of each day?",
                "options": ["East", "West", "North", "South"],
                "ans": "East",
                "explanation": "Due to Earth's counter-clockwise rotation from West to East, the Sun always appears to rise along the eastern horizon."
            }
        ]
    },
    {
        "id": 2,
        "title": "The Radiant Sun",
        "badge": "Solar Astronomy",
        "sim_id": "sim_solar_radiance",
        "description": "Investigate the Sun as a massive incandescent star that provides the essential light and heat powering all life on Earth.",
        "speech": "The Sun is the most dominant, radiant, and energetic celestial body in our sky. Scientifically, our Sun is a colossal glowing star—a massive sphere of superheated hydrogen and helium gases undergoing continuous nuclear fusion in its core. Although there are countless trillions of stars in the vast universe, the Sun appears overwhelmingly larger and brighter than any other star because it is located astronomically close to Earth, roughly one hundred and fifty million kilometres away. The Sun functions as the ultimate engine of planetary life, radiating immense electromagnetic energy that reaches our surface in the form of bright daylight and life-sustaining thermal warmth. Without steady solar energy, our planet would become a frozen, pitch-black wasteland devoid of liquid water, living plants, or breathable oxygen. Solar heat drives the global water cycle by evaporating ocean water to form rain clouds, generates planetary wind currents by unevenly warming atmospheric air, and powers plant photosynthesis to produce food and oxygen for all animals. Because solar rays are exceptionally concentrated, looking directly at the Sun can cause severe permanent retinal damage to human eyes. Observing the radiant Sun safely allows us to appreciate its role as Earth's vital cosmic furnace.",
        "checkpoints": [
            {
                "q": "Why does the Sun appear so much larger and brighter than all the other stars in the sky?",
                "options": ["It is located much closer to Earth than any other star", "It is the only star that possesses any internal heat energy", "It is made entirely of solid polished gold that reflects light", "It moves around the Earth faster than the speed of sound"],
                "ans": "It is located much closer to Earth than any other star",
                "explanation": "The Sun is our nearest star (~150 million km away), while all other stars are trillions of kilometres distant, making them appear as tiny points of light."
            },
            {
                "q": "Why is it dangerous to look directly at the Sun with unprotected human eyes?",
                "options": ["Concentrated solar rays can permanently damage retinal cells", "The Sun will suddenly turn off if humans stare at it", "It causes the observer to become invisible immediately", "It transforms human eye lenses into solid frozen ice"],
                "ans": "Concentrated solar rays can permanently damage retinal cells",
                "explanation": "Intense ultraviolet and infrared solar radiation can burn delicate retinal tissues in the eye, causing irreversible vision loss or blindness."
            }
        ]
    },
    {
        "id": 3,
        "title": "Daytime Biological Rhythms",
        "badge": "Circadian Biology",
        "sim_id": "sim_biological_rhythms",
        "description": "Examine how animals, birds, flowering plants, and human beings adapt their daily behaviors to changing solar cycles.",
        "speech": "All living organisms on Earth possess internal biological clocks that respond to the rising and setting of the Sun. As morning daylight breaks, the natural world undergoes a dramatic awakening. Roosters crow, songbirds burst into melodious chorus, and honeybees leave their protective hives to forage for nectar among blossoming wildflowers. Many daytime flowers, such as vibrant sunflowers and bright water lilies, unfurl their petals to absorb morning sunbeams, actively turning their flower heads to track the solar path across the sky in a botanical behavior called heliotropism. Diurnal animals, including cattle, squirrels, butterflies, and humans, conduct their primary feeding, working, learning, and gathering activities during well-lit daylight hours. Conversely, as twilight deepens into night, daytime birds return to roost in leafy tree branches, cows settle in peaceful barns, and daytime blossoms close their delicate petals to conserve moisture. Simultaneously, nocturnal creatures begin their active shift under cover of darkness. Owls glide silently through nighttime forests, bats deploy high-frequency echolocation to catch night-flying moths, and night-blooming jasmine flowers release intoxicating perfumes to attract nocturnal pollinators. These harmonious behavioral transitions illustrate how solar illumination governs the circadian rhythms and survival strategies of terrestrial ecosystems worldwide throughout the entire year.",
        "checkpoints": [
            {
                "q": "What botanical term describes a plant's ability to turn its leaves or flowers toward the Sun?",
                "options": ["Heliotropism", "Metamorphosis", "Echolocation", "Sedimentation"],
                "ans": "Heliotropism",
                "explanation": "Heliotropism is the directional growth or movement of a plant organ (like sunflower heads) in response to the direction of sunlight."
            },
            {
                "q": "Which of the following animals is naturally adapted to be active during the dark night (nocturnal)?",
                "options": ["Owl", "Butterfly", "Sparrow", "Honeybee"],
                "ans": "Owl",
                "explanation": "Owls possess specialized low-light vision and silent flight adaptations that enable them to hunt actively during the night."
            }
        ]
    },
    {
        "id": 4,
        "title": "Forming Light Shadows",
        "badge": "Optical Physics",
        "sim_id": "sim_shadow_formation",
        "description": "Discover how shadows form when opaque objects obstruct straight light rays, creating dark silhouettes on surfaces.",
        "speech": "To understand shadows, we must explore a fundamental law of optical physics: light travels through uniform media in straight lines, known as rectilinear propagation. When radiant light emitted from a source, such as the Sun or an electric lamp, encounters an object in its straight path, the physical properties of that object determine the outcome. Transparent materials, like clear glass windowpanes and pure water, allow light rays to pass straight through without obstruction. Translucent materials, like frosted butter paper, scatter light rays, creating faint, hazy silhouettes. However, when light strikes an opaque object—such as a wooden post, a brick wall, or a human body—the light rays cannot pass through or bend around sharp solid corners. The blocked light leaves a dark area of darkness on the screen or ground directly behind the object. This dark area devoid of direct light is called a shadow. Three essential components are required to produce any shadow: a bright light source, an opaque obstructing object, and a screen or flat surface upon which the shadow falls. Without all three elements present simultaneously, a shadow cannot exist, proving that shadows are simply dark regions where straight light rays have been physically obstructed.",
        "checkpoints": [
            {
                "q": "What fundamental property of light causes distinct shadows to form behind solid objects?",
                "options": ["Light travels in straight lines and cannot bend around opaque objects", "Light travels in complete zig-zag loops around every surface", "Light can only travel through magnetic iron and copper wires", "Light stops existing whenever it touches outdoor air molecules"],
                "ans": "Light travels in straight lines and cannot bend around opaque objects",
                "explanation": "Because light travels in straight lines (rectilinear propagation), an opaque obstacle blocks the rays, leaving an unlit silhouette behind it."
            },
            {
                "q": "Which three elements are strictly required to observe a shadow?",
                "options": ["A light source, an opaque object, and a surface or screen", "A battery, a magnet, and a glass of water", "A telescope, a mirror, and an electric motor", "A thermometer, a ruler, and a wooden whistle"],
                "ans": "A light source, an opaque object, and a surface or screen",
                "explanation": "Creating a shadow requires: 1) an emitting light source, 2) an opaque object to obstruct light rays, and 3) a surface/screen to cast the shadow upon."
            }
        ]
    },
    {
        "id": 5,
        "title": "Daylong Shadow Shifts",
        "badge": "Solar Geometry",
        "sim_id": "sim_daylong_shadows",
        "description": "Investigate how a vertical gnomon post casts changing shadows: long at dawn and dusk, shortest at noon, and aligned opposite to the Sun.",
        "speech": "When we observe outdoor shadows cast by a vertical flagpole or tree over the course of a clear sunny day, we discover fascinating geometric patterns governed by solar elevation. In the early morning, right after sunrise, the Sun sits low along the eastern horizon. Because incoming solar rays strike the ground at a shallow, slanted angle, the vertical object casts an exceptionally long shadow stretching far toward the west. As morning progresses and the Sun climbs higher in the sky, the angle of incoming rays steepens, causing the cast shadow to gradually shrink in length while shifting smoothly northward. At midday, when the Sun reaches its highest zenith elevation in the sky, solar rays strike the ground almost vertically from above. Consequently, midday shadows become the shortest and most compact of the entire day. As afternoon turns toward evening, the Sun descends lower toward the western horizon, and the shadow elongates once again, pointing far toward the east. A vital scientific rule emerges: a shadow always points in the exact opposite direction of the light source. By measuring shadow length and compass direction, human beings across antiquity could accurately determine the time of day without mechanical clocks.",
        "checkpoints": [
            {
                "q": "At what time of day are outdoor shadows cast by vertical posts the shortest?",
                "options": ["Around noon when the Sun is at its highest point in the sky", "Early morning right after the Sun rises above the horizon", "Late evening just before sunset begins", "At midnight when only stars illuminate the trees"],
                "ans": "Around noon when the Sun is at its highest point in the sky",
                "explanation": "At solar noon, the Sun is at its highest zenith angle overhead, causing incoming rays to strike vertically and casting the shortest possible shadow."
            },
            {
                "q": "If the morning Sun is in the East, in which direction will a flagpole's shadow point?",
                "options": ["West", "East", "North", "South"],
                "ans": "West",
                "explanation": "Shadows are cast directly opposite the position of the light source; hence, an eastern light source casts a shadow pointing toward the West."
            }
        ]
    },
    {
        "id": 6,
        "title": "Torchlight Shadow Lab",
        "badge": "Experimental Optics",
        "sim_id": "sim_torch_shadow_lab",
        "description": "Experiment hands-on with a movable torch and a stick to observe how distance and illumination angle alter shadow size and sharpness.",
        "speech": "We can test the geometric principles of shadow formation inside our laboratory using a simple torch, a small wooden figurine, and a flat white screen. When we position the torch close to the figurine, the opaque object intercepts a broad cone of diverging light rays, blocking a large angle of illumination and casting an enormous, magnified shadow upon the screen. As we move the torch farther away from the figurine, the intercepting angle narrows, and the projected shadow shrinks in proportion, becoming crisper and more compact. Next, we can investigate the effect of light source elevation. When we hold the torch directly above the figurine, shining downward from a ninety-degree angle, a tiny circular shadow forms directly beneath the object's base. However, when we lower the torch to a shallow thirty-degree angle near the table surface, the shadow stretches out into an elongated oval across the tabletop. Furthermore, using a concentrated point light source produces sharp shadow boundaries called the umbra, whereas a broad diffused light source creates softer, blurred edges known as the penumbra. Through these controlled optical tests, young scientists discover that shadow geometry is entirely predictable through the spatial arrangement of light.",
        "checkpoints": [
            {
                "q": "What happens to the size of a shadow on a screen when a torch is moved closer to the opaque object?",
                "options": ["The shadow becomes significantly larger and magnified", "The shadow shrinks down until it completely disappears", "The shadow turns into bright glowing neon green light", "The shadow splits into four identical separate triangles"],
                "ans": "The shadow becomes significantly larger and magnified",
                "explanation": "Bringing the light source closer increases the angle of blocked light rays, casting a larger, magnified shadow on the background screen."
            },
            {
                "q": "What is the dark, completely obstructed central portion of a cast shadow called in optics?",
                "options": ["Umbra", "Penumbra", "Spectrum", "Reflection"],
                "ans": "Umbra",
                "explanation": "The umbra is the darkest central zone of a shadow where the light source is completely blocked by the opaque object."
            }
        ]
    },
    {
        "id": 7,
        "title": "Historical Shadow Sundials",
        "badge": "Archaeoastronomy",
        "sim_id": "sim_sundial_astronomy",
        "description": "Examine how ancient astronomers measured time with shadows, highlighting the colossal Samrat Yantra sundial at Jantar Mantar.",
        "speech": "Long before the invention of mechanical spring clocks, quartz crystals, or digital watches, ancient civilizations relied upon the reliable movement of solar shadows to track the passage of time. They constructed instruments called sundials, consisting of a flat calibrated dial plate marked with hour divisions and a raised angled pointer called a gnomon. As the Sun traces its daily arc across the sky, the gnomon casts a moving shadow across the hour markings, functioning like the hour hand of a natural solar clock. In India, astronomical shadow engineering reached its zenith during the early eighteenth century with the construction of the Jantar Mantar observatories in Delhi, Jaipur, Ujjain, Varanasi, and Mathura. The crowning jewel of these observatories is the monumental Brihat Samrat Yantra in Jaipur, the world's largest stone sundial, rising twenty-seven metres into the sky. Its massive triangular gnomon is aligned precisely with Earth's geographic rotational axis, pointing directly toward the North Pole Star. The curved marble quadrant scales flanking the gnomon measure shadow movement with astonishing precision, calculating local solar time to an accuracy of just two seconds, proving the incredible scientific genius, mathematical sophistication, and astronomical mastery of historical Indian astronomers across centuries of discovery.",
        "checkpoints": [
            {
                "q": "What is the angled shadow-casting triangular pointer of a traditional sundial called?",
                "options": ["Gnomon", "Pendulum", "Compass needle", "Tuning fork"],
                "ans": "Gnomon",
                "explanation": "The gnomon is the upright or angled triangular blade of a sundial that casts its shadow onto the calibrated time scale."
            },
            {
                "q": "What is the historic Brihat Samrat Yantra located at Jantar Mantar in Jaipur famous for?",
                "options": ["Being the world's largest precision stone sundial", "Being an underground coal-powered railway station", "Being a deep sea submarine testing tank", "Being a factory that manufactures mechanical wristwatches"],
                "ans": "Being the world's largest precision stone sundial",
                "explanation": "The Brihat Samrat Yantra in Jaipur is the largest stone sundial in the world, capable of measuring local solar time to an accuracy of 2 seconds."
            }
        ]
    },
    {
        "id": 8,
        "title": "Creative Shadow Puppetry",
        "badge": "Folk Arts & Optics",
        "sim_id": "sim_shadow_puppetry",
        "description": "Explore traditional Indian shadow puppetry, hand silhouette figures, and the optical artistry of translucent leather puppets.",
        "speech": "Beyond scientific timekeeping, the physics of shadow formation has inspired captivating storytelling traditions for thousands of years through the ancient folk art of shadow puppetry. Known by celebrated regional heritage titles across India—such as Togalu Gombeyaata in Karnataka, Tholu Bommalata in Andhra Pradesh, and Ravanachhaya in Odisha—shadow theatre combines cultural mythology, music, and optical mastery. Master artisans handcraft flat puppet figures from seasoned, translucent leather, meticulously perforating intricate openwork lace patterns and coloring them with natural plant dyes. When puppeteers hold these articulated figures against a translucent white cotton screen illuminated from behind by an oil lamp or electric spotlight, the opaque outlines cast crisp dark contours while translucent tinted sections glow with luminous amber, ruby, and jade hues. Puppeteers skillfully manipulate slender bamboo rods attached to the puppet's limbs, bringing mythical heroes, soaring eagles, and dancing deer to life on the glowing screen. Children can also create delightful hand shadows using their own fingers, positioning their hands between a flashlight and a blank bedroom wall to form barking dogs, fluttering butterflies, and soaring swans, proving how simple light blockages can spark extraordinary artistic imagination, theatrical drama, folk cultural storytelling, and inspiring scientific wonder across generations.",
        "checkpoints": [
            {
                "q": "What ancient Indian performing art form uses articulated leather cut-outs to cast stories onto an illuminated screen?",
                "options": ["Traditional shadow puppetry", "Classical marble sculpture", "Oil canvas painting", "Pottery wheel molding"],
                "ans": "Traditional shadow puppetry",
                "explanation": "Shadow puppetry (such as Togalu Gombeyaata and Tholu Bommalata) uses flat articulated leather figures to project dramatic stories on illuminated cloth screens."
            },
            {
                "q": "How can children create hand shadow figures on a blank wall without any paper cut-outs?",
                "options": ["Interlocking fingers at specific angles between a torch and the wall", "Painting dark black ink directly onto the wall surface", "Turning off all room lights so total darkness fills the room", "Sticking magnetic metal toys directly onto the flashlight lens"],
                "ans": "Interlocking fingers at specific angles between a torch and the wall",
                "explanation": "Interlocking hands and fingers in front of a light beam obstructs light rays in recognizable animal silhouettes on a flat surface."
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
    'Aarav', 'Ananya', 'Priya', 'Rahul', 'Neha', 'Sanjay', 'Vikram', 'Shrinathan',
    'Mirabai', 'Gulabo', 'Anvi', 'Raju', 'Parv', 'Chinnu', 'Abha', 'Didi',
    'Daisy', 'Lou', 'Sapan', 'Udaya', 'Krishna', 'Sudama', 'Mala', 'Neela', 'Bhola'
]

FORBIDDEN_PERSONAS = [
    r'\bDr\b', r'\bDr\.\b', r'\bSir\b', r'\bMadam\b', r'\bMr\b', r'\bMr\.\b', r'\bMrs\b', r'\bMrs\.\b', r'\bMiss\b'
]

print("=== CHECKING SLIDES 1 TO 8 ===")
for s in slides_part1:
    sid = s['id']
    title = s['title']
    wc = len(s['speech'].split())
    print(f"Slide {sid} '{title}': {wc} words")

for s in slides_part1:
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

print("Slides 1 to 8 verified successfully!")
