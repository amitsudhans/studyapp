# -*- coding: utf-8 -*-
"""
Generate Slides 17 to 20 for Class 4 Science Chapter 10: Our Sky.
4 Mastery Challenge Slides × 10 Questions each = 40 Questions total.
Each question has id, q, 4 options, ans, hint, explanation, and 3 solution steps.
Zero human character names, zero lecturer personas.
"""

import re
import json

slides_part3 = [
    {
        "id": 17,
        "title": "Challenge 1",
        "badge": "Solar & Shadows",
        "sim_id": "sim_quiz_shadows",
        "description": "Mastery challenge testing scientific concepts of the Sun as a star, diurnal sky color changes, and daylong shadow lengths.",
        "questions": [
            {
                "id": "c1_q1",
                "q": "What type of celestial object is the Sun classified as by astronomers?",
                "options": ["A luminous incandescent star", "A rocky terrestrial planet", "A frozen icy comet", "A reflective natural satellite"],
                "ans": "A luminous incandescent star",
                "hint": "It generates its own immense light and heat through nuclear fusion.",
                "explanation": "The Sun is an incandescent main-sequence star composed of superheated hydrogen and helium undergoing nuclear fusion.",
                "solution_steps": [
                    "Step 1: Understand that stars generate their own light and heat energy.",
                    "Step 2: Contrast stars with non-luminous planets and rocky moons.",
                    "Step 3: Confirm that the Sun is classified as a luminous incandescent star."
                ]
            },
            {
                "id": "c1_q2",
                "q": "Why does the daytime sky appear bright blue rather than dark black?",
                "options": ["Microscopic air molecules scatter high-frequency blue sunlight", "The sky reflects the blue saltwater of Earth's oceans", "The Sun radiates exclusively blue light during the day", "Green tree leaves reflect blue rays into upper clouds"],
                "ans": "Microscopic air molecules scatter high-frequency blue sunlight",
                "hint": "This atmospheric scattering process is known as Rayleigh scattering.",
                "explanation": "Rayleigh scattering occurs when atmospheric gas molecules scatter shorter blue wavelengths of solar light in all directions across the sky.",
                "solution_steps": [
                    "Step 1: Recall that solar white light contains all spectral colors.",
                    "Step 2: Recognize that atmospheric molecules scatter shorter blue wavelengths far more efficiently than red wavelengths.",
                    "Step 3: Conclude that scattered blue light gives the daytime sky its characteristic blue color."
                ]
            },
            {
                "id": "c1_q3",
                "q": "At what time of day will a vertical flagpole cast its shortest possible shadow?",
                "options": ["Around solar noon", "At early dawn sunrise", "In the late evening twilight", "At midnight under stars"],
                "ans": "Around solar noon",
                "hint": "The Sun reaches its highest point in the sky directly overhead.",
                "explanation": "At solar noon, the Sun reaches its maximum altitude (zenith), causing incoming rays to strike vertically and forming the shortest shadow.",
                "solution_steps": [
                    "Step 1: Analyze how shadow length depends inversely on solar elevation angle.",
                    "Step 2: Note that the Sun reaches its highest sky angle at solar noon.",
                    "Step 3: Confirm that vertical posts cast their shortest shadows at solar noon."
                ]
            },
            {
                "id": "c1_q4",
                "q": "If the morning Sun rises in the East, in which compass direction does a person's shadow point?",
                "options": ["West", "East", "North", "South"],
                "ans": "West",
                "hint": "A shadow is always cast directly opposite the incoming light source.",
                "explanation": "Because light travels in straight lines, an opaque object blocks light from the East, creating a dark shadow pointing toward the West.",
                "solution_steps": [
                    "Step 1: Apply the fundamental optical rule: shadows form opposite to the light source.",
                    "Step 2: Identify the position of the morning Sun as the East.",
                    "Step 3: Conclude that the shadow points in the opposite direction, toward the West."
                ]
            },
            {
                "id": "c1_q5",
                "q": "Which property of light explains why opaque objects create dark, sharp-edged shadows?",
                "options": ["Light travels through uniform media in straight lines", "Light bends completely around solid objects", "Light travels only through electrical wires", "Light stops moving whenever it enters room air"],
                "ans": "Light travels through uniform media in straight lines",
                "hint": "Rectilinear propagation means light cannot curve around solid obstructions.",
                "explanation": "Light travels in straight lines (rectilinear propagation). When an opaque obstacle blocks these rays, the area directly behind remains unlit.",
                "solution_steps": [
                    "Step 1: Consider how light moves through the air from a source.",
                    "Step 2: Recognize that light rays travel along straight paths and cannot bend around solid obstacles.",
                    "Step 3: Confirm that straight-line propagation creates distinct dark shadows behind opaque objects."
                ]
            },
            {
                "id": "c1_q6",
                "q": "What three elements are simultaneously required to observe any cast shadow?",
                "options": ["A light source, an opaque object, and a screen or surface", "A prism, a thermometer, and a magnifying glass", "A battery, a magnet, and a container of liquid water", "A telescope, a stopwatch, and an electric motor"],
                "ans": "A light source, an opaque object, and a screen or surface",
                "hint": "You need something to emit rays, something to block them, and something to catch the shadow.",
                "explanation": "A shadow requires: 1) a light source to emit rays, 2) an opaque object to intercept the rays, and 3) a surface/screen to display the shadow.",
                "solution_steps": [
                    "Step 1: Identify that without light, no shadows can be created.",
                    "Step 2: Identify that without an opaque object, light passes unhindered without obstruction.",
                    "Step 3: Conclude that a light source, an opaque object, and a screen or surface are required."
                ]
            },
            {
                "id": "c1_q7",
                "q": "Why do shadows appear longer in the early morning and late afternoon compared to midday?",
                "options": ["Sunlight strikes the ground at a lower, slanted angle", "The Sun moves closer to the Earth in the morning", "Air molecules expand the shadow like a balloon", "The ground becomes magnetized during morning hours"],
                "ans": "Sunlight strikes the ground at a lower, slanted angle",
                "hint": "When light rays hit an object from a low angle, the shadow projects farther.",
                "explanation": "When the Sun is low near the horizon, its slanted light rays hit vertical objects at a shallow angle, projecting elongated shadows across the ground.",
                "solution_steps": [
                    "Step 1: Observe the Sun's position near the horizon during early morning and late afternoon.",
                    "Step 2: Notice that low solar angles project longer geometric shadows across the horizontal plane.",
                    "Step 3: Confirm that slanted sunlight angles cause long morning and afternoon shadows."
                ]
            },
            {
                "id": "c1_q8",
                "q": "What botanical response causes sunflower blossoms to track the Sun's path from East to West?",
                "options": ["Heliotropism", "Photosynthesis", "Germination", "Transpiration"],
                "ans": "Heliotropism",
                "hint": "The Greek root 'helios' refers to the Sun.",
                "explanation": "Heliotropism is the biological tracking movement in plants where young blossoms follow the Sun's daily path to maximize solar absorption.",
                "solution_steps": [
                    "Step 1: Review biological adaptations in plants that respond to sunlight.",
                    "Step 2: Identify heliotropism as the directional solar-tracking behavior exhibited by sunflowers.",
                    "Step 3: Confirm that heliotropism causes sunflower heads to face the Sun throughout the day."
                ]
            },
            {
                "id": "c1_q9",
                "q": "Which classification applies to a transparent sheet of clean window glass?",
                "options": ["Allows light rays to pass straight through without forming dark shadows", "Completely blocks all light rays to cast an ink-black shadow", "Reflects all light rays back into the light source like a mirror", "Absorbs all incoming light to turn into a glowing ember"],
                "ans": "Allows light rays to pass straight through without forming dark shadows",
                "hint": "Transparent materials let light transmit freely.",
                "explanation": "Transparent materials allow light to pass through with minimal scattering or absorption, meaning they do not cast dark shadows.",
                "solution_steps": [
                    "Step 1: Differentiate between transparent, translucent, and opaque optical materials.",
                    "Step 2: Recognize that clear glass transmits almost all incident visible light rays.",
                    "Step 3: Conclude that transparent materials allow light to pass through without forming dark shadows."
                ]
            },
            {
                "id": "c1_q10",
                "q": "Why does the Sun appear to move from East to West across our sky every day?",
                "options": ["Earth rotates counter-clockwise on its axis from West to East", "The Sun orbits around the Earth once every 24 hours", "Earth swings back and forth like a giant clock pendulum", "Ocean currents pull the continents towards the West"],
                "ans": "Earth rotates counter-clockwise on its axis from West to East",
                "hint": "This apparent movement is an optical illusion caused by Earth's rotational spin.",
                "explanation": "Because Earth spins on its axis from West to East, stationary celestial bodies like the Sun appear to move in the opposite direction (East to West).",
                "solution_steps": [
                    "Step 1: Understand that Earth is rotating on its axis once every 24 hours from West to East.",
                    "Step 2: Apply relative motion: an observer on a spinning platform sees stationary objects moving backwards.",
                    "Step 3: Confirm that Earth's West-to-East rotation causes the Sun's apparent East-to-West transit."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "badge": "Sundials & Optics",
        "sim_id": "sim_quiz_optics",
        "description": "Mastery challenge testing laboratory torch experiments, umbra-penumbra physics, sundial astronomy, and shadow puppetry.",
        "questions": [
            {
                "id": "c2_q1",
                "q": "In a laboratory investigation, what happens to an object's shadow on a wall as a torch is moved closer to the object?",
                "options": ["The shadow becomes significantly larger", "The shadow becomes smaller and tiny", "The shadow turns into bright white light", "The shadow disappears into thin air"],
                "ans": "The shadow becomes significantly larger",
                "hint": "Moving the light closer causes the object to intercept a wider angle of light rays.",
                "explanation": "When the light source is brought closer to the object, it subtends a larger obstruction angle, projecting a magnified shadow onto the screen.",
                "solution_steps": [
                    "Step 1: Draw the ray diagram from a point light source past the edges of an opaque object.",
                    "Step 2: Observe that decreasing the distance between source and object widens the shadow cone.",
                    "Step 3: Confirm that bringing the torch closer makes the shadow significantly larger."
                ]
            },
            {
                "id": "c2_q2",
                "q": "What is the dark central zone of a shadow where all direct light is completely blocked?",
                "options": ["Umbra", "Penumbra", "Spectrum", "Cornea"],
                "ans": "Umbra",
                "hint": "The Latin word for 'shade' or 'shadow'.",
                "explanation": "The umbra is the innermost, darkest region of a shadow where the light source is completely obstructed by the opaque body.",
                "solution_steps": [
                    "Step 1: Differentiate between the zones of a shadow cast by an extended light source.",
                    "Step 2: Identify the umbra as the region of total light obstruction and the penumbra as partial obstruction.",
                    "Step 3: Confirm that the umbra is the completely blocked central dark zone."
                ]
            },
            {
                "id": "c2_q3",
                "q": "What is the partially shaded outer border of a shadow cast by a broad light source called?",
                "options": ["Penumbra", "Umbra", "Focal point", "Refraction"],
                "ans": "Penumbra",
                "hint": "The prefix 'paene' means almost; it is the almost-shadow region.",
                "explanation": "The penumbra is the lighter, blurred outer boundary of a shadow where only a portion of the light source is occluded.",
                "solution_steps": [
                    "Step 1: Recall that extended light sources create two distinct shadow regions.",
                    "Step 2: Identify the penumbra as the region receiving partial illumination from the light source.",
                    "Step 3: Conclude that the partially shaded outer region is the penumbra."
                ]
            },
            {
                "id": "c2_q4",
                "q": "What is the upright or angled triangular pointer of a sundial that casts a shadow called?",
                "options": ["Gnomon", "Pendulum", "Quadrant", "Prism"],
                "ans": "Gnomon",
                "hint": "The shadow of this pointer moves across the marked hour dial like a clock hand.",
                "explanation": "The gnomon is the vertical or angled blade on a sundial designed to cast a shadow indicating solar time on a calibrated base.",
                "solution_steps": [
                    "Step 1: Identify the working components of an astronomical sundial.",
                    "Step 2: Recall that the angled shadow-casting blade is termed the gnomon.",
                    "Step 3: Confirm that the pointer of a sundial is called a gnomon."
                ]
            },
            {
                "id": "c2_q5",
                "q": "Where is the world's largest stone precision sundial, the Brihat Samrat Yantra, located?",
                "options": ["Jantar Mantar in Jaipur", "Red Fort in Delhi", "Taj Mahal in Agra", "Gateway of India in Mumbai"],
                "ans": "Jantar Mantar in Jaipur",
                "hint": "This 27-metre-tall astronomical instrument is a UNESCO World Heritage site in Rajasthan.",
                "explanation": "The Brihat Samrat Yantra is the 27-metre-high giant sundial located at the Jantar Mantar observatory in Jaipur, measuring time to 2 seconds precision.",
                "solution_steps": [
                    "Step 1: Recall historical Indian astronomical observatories built by Sawai Jai Singh II.",
                    "Step 2: Identify the largest sundial instrument among them: the Brihat Samrat Yantra.",
                    "Step 3: Confirm that it is located at Jantar Mantar in Jaipur."
                ]
            },
            {
                "id": "c2_q6",
                "q": "How was the triangular gnomon of the Samrat Yantra aligned during construction?",
                "options": ["Parallel to Earth's rotational axis pointing directly toward the North Pole Star", "Facing straight toward the ocean to detect tidal waves", "Pointed randomly toward the nearest mountain summit", "Aligned with the direction of the summer monsoon wind"],
                "ans": "Parallel to Earth's rotational axis pointing directly toward the North Pole Star",
                "hint": "Aligning with the Earth's rotational axis ensures accurate solar time measurement all year.",
                "explanation": "The gnomon is tilted at an angle equal to the local latitude, aligning it parallel to Earth's axis and pointing directly toward Polaris.",
                "solution_steps": [
                    "Step 1: Analyze how equatorial and horizontal sundials achieve seasonal accuracy.",
                    "Step 2: Recognize that aligning the gnomon with Earth's rotational axis ensures uniform shadow movement.",
                    "Step 3: Confirm that the gnomon points toward the celestial North Pole Star."
                ]
            },
            {
                "id": "c2_q7",
                "q": "Which traditional Indian folk art form uses articulated translucent leather cut-outs to project stories on a screen?",
                "options": ["Shadow puppetry", "Terracotta pottery", "Madhubani painting", "Wood carving"],
                "ans": "Shadow puppetry",
                "hint": "Known regionally as Togalu Gombeyaata, Tholu Bommalata, and Ravanachhaya.",
                "explanation": "Traditional shadow puppetry uses translucent leather puppets held behind a backlit cloth screen to cast colorful silhouettes for dramatic storytelling.",
                "solution_steps": [
                    "Step 1: Connect shadow physics with cultural performing arts in India.",
                    "Step 2: Identify shadow theatre traditions that project puppet silhouettes using oil lamps.",
                    "Step 3: Confirm that shadow puppetry is the traditional folk art using articulated cut-outs."
                ]
            },
            {
                "id": "c2_q8",
                "q": "What optical material property allows colorful light to glow through traditional shadow puppets?",
                "options": ["Translucency of treated leather and plant dyes", "Complete opacity of thick industrial iron plates", "Total transparency of clear window glass", "Magnetic conductivity of copper wire"],
                "ans": "Translucency of treated leather and plant dyes",
                "hint": "Translucent materials allow light to pass through while coloring the transmitted rays.",
                "explanation": "Carefully cured translucent goat or deer leather stained with vegetable dyes allows filtered colored light to pass through, creating vibrant illuminated projections.",
                "solution_steps": [
                    "Step 1: Analyze how translucent materials interact with light rays.",
                    "Step 2: Note that master puppet makers treat leather until it becomes translucent and absorbs dye.",
                    "Step 3: Conclude that translucency allows colored light to shine through the puppets."
                ]
            },
            {
                "id": "c2_q9",
                "q": "What happens to the shadow of a stick on the ground if a torch held directly above it is tilted to a low angle?",
                "options": ["The shadow elongates significantly across the table", "The shadow immediately turns into a tiny circle", "The shadow jumps into the air and floats", "The stick loses all color and becomes invisible"],
                "ans": "The shadow elongates significantly across the table",
                "hint": "Lower angles of incident light create longer projected shadows.",
                "explanation": "Tilting the light source closer to the surface plane causes the projected geometric shadow to stretch out into an elongated shape.",
                "solution_steps": [
                    "Step 1: Recall the torchlight investigation with varying angles.",
                    "Step 2: Understand that lower angles of incidence cast longer shadows across a horizontal surface.",
                    "Step 3: Confirm that lowering the torch angle causes the shadow to elongate significantly."
                ]
            },
            {
                "id": "c2_q10",
                "q": "Why cannot a traditional sundial indicate the time of day during a heavily overcast or rainy afternoon?",
                "options": ["Dense clouds obstruct direct solar rays, preventing a distinct shadow from forming", "Cold rainwater breaks the stone gnomon immediately", "Sundials only operate when the Moon is fully visible", "Cloudy air causes the gnomon to rotate in reverse"],
                "ans": "Dense clouds obstruct direct solar rays, preventing a distinct shadow from forming",
                "hint": "A sundial requires direct, unscattered sunlight to cast a visible shadow.",
                "explanation": "Sundials require direct solar rays to cast a sharp gnomon shadow; diffused light on overcast days eliminates distinct shadows entirely.",
                "solution_steps": [
                    "Step 1: Recall that sundials depend strictly on casting shadows from direct sunlight.",
                    "Step 2: Understand that thick cloud cover scatters sunlight into diffused ambient light without directional rays.",
                    "Step 3: Conclude that sundials cannot function on overcast days because no distinct shadow is cast."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "badge": "Moon & Calendars",
        "sim_id": "sim_quiz_moon",
        "description": "Mastery challenge testing lunar geology, light reflection, the 29.5-day phase cycle, and traditional lunar calendars.",
        "questions": [
            {
                "id": "c3_q1",
                "q": "Does the Moon produce its own light, or how does it shine in the night sky?",
                "options": ["It reflects sunlight that strikes its rocky surface", "It burns hydrogen gas in an internal nuclear core", "It glows from radioactive lava oceans across its craters", "It absorbs city electrical lights and shines them back"],
                "ans": "It reflects sunlight that strikes its rocky surface",
                "hint": "The Moon is a non-luminous rocky body acting like a giant natural mirror.",
                "explanation": "The Moon is a non-luminous body that shines entirely by reflecting incident sunlight off its rocky, dusty regolith surface.",
                "solution_steps": [
                    "Step 1: Differentiate between luminous celestial bodies (like stars) and non-luminous bodies (like moons).",
                    "Step 2: Recognize that the Moon has no internal energy source to generate visible light.",
                    "Step 3: Confirm that the Moon shines by reflecting sunlight toward Earth."
                ]
            },
            {
                "id": "c3_q2",
                "q": "What are the dark, relatively smooth lowland plains observed on the lunar surface called?",
                "options": ["Lunar maria", "Lunar oceans", "Glacial ice sheets", "Subterranean trenches"],
                "ans": "Lunar maria",
                "hint": "The Latin word 'maria' means 'seas', because early observers thought they were bodies of water.",
                "explanation": "Lunar maria are expansive dark basaltic plains formed by ancient volcanic lava flows that filled giant impact basins on the Moon.",
                "solution_steps": [
                    "Step 1: Observe telescopic images of the Moon showing light highlands and dark plains.",
                    "Step 2: Identify the dark plains as lunar maria, consisting of solidified basaltic lava.",
                    "Step 3: Confirm that the dark lowland plains are termed lunar maria."
                ]
            },
            {
                "id": "c3_q3",
                "q": "What lunar phase occurs when the Moon lies directly between the Earth and Sun, making it invisible from Earth?",
                "options": ["New Moon (Amavasya)", "Full Moon (Poornima)", "First Quarter Half Moon", "Waxing Gibbous Moon"],
                "ans": "New Moon (Amavasya)",
                "hint": "Its illuminated side faces completely away from Earth into space.",
                "explanation": "During New Moon (Amavasya), the Moon's sunlit side faces away from Earth, rendering the lunar disc invisible in the night sky.",
                "solution_steps": [
                    "Step 1: Analyze the orbital alignment where the Moon is between the Sun and Earth.",
                    "Step 2: Understand that the sunlit hemisphere is turned toward the Sun, away from Earth's view.",
                    "Step 3: Conclude that this phase is the New Moon, or Amavasya."
                ]
            },
            {
                "id": "c3_q4",
                "q": "What lunar phase is observed when the entire sunlit hemisphere of the Moon faces Earth directly?",
                "options": ["Full Moon (Poornima)", "New Moon (Amavasya)", "Crescent Moon", "Third Quarter Moon"],
                "ans": "Full Moon (Poornima)",
                "hint": "The Moon appears as a complete, glowing circular disc in the night sky.",
                "explanation": "At Full Moon (Poornima), the Earth is positioned between the Sun and Moon, allowing us to see the entire sunlit face of the Moon.",
                "solution_steps": [
                    "Step 1: Examine the orbital position where the Moon is opposite the Sun from Earth's viewpoint.",
                    "Step 2: Note that the fully illuminated hemisphere faces Earth directly.",
                    "Step 3: Confirm that this phase is the Full Moon, or Poornima."
                ]
            },
            {
                "id": "c3_q5",
                "q": "Approximately how long does it take for the Moon to cycle from one New Moon to the next New Moon?",
                "options": ["About 29.5 days", "Exactly 24 hours", "365 days", "7 days"],
                "ans": "About 29.5 days",
                "hint": "This duration defines a lunar month (synodic month).",
                "explanation": "A complete lunar phase cycle (synodic month) takes approximately 29.5 days, forming the basis of traditional lunar calendars.",
                "solution_steps": [
                    "Step 1: Recall the duration of the lunar orbit relative to the Sun.",
                    "Step 2: Note that one complete phase cycle from New Moon to New Moon is roughly 29.5 days.",
                    "Step 3: Confirm that the lunar phase cycle lasts about 29.5 days."
                ]
            },
            {
                "id": "c3_q6",
                "q": "On which lunar phase is the major national festival of lights, Diwali, celebrated?",
                "options": ["Kartik Amavasya (New Moon)", "Kartik Poornima (Full Moon)", "Chaitra Shukla Pratipada", "Makar Sankranti"],
                "ans": "Kartik Amavasya (New Moon)",
                "hint": "The celebration of lighting diyas happens on the darkest night of the autumn month.",
                "explanation": "Diwali is celebrated on the dark night of Kartik Amavasya, where the lack of moonlight is countered by millions of earthen oil lamps.",
                "solution_steps": [
                    "Step 1: Connect Indian festivals with specific lunar calendar dates.",
                    "Step 2: Identify Diwali as the festival of lights occurring on the darkest night of Kartik.",
                    "Step 3: Confirm that Diwali is celebrated on Kartik Amavasya (New Moon)."
                ]
            },
            {
                "id": "c3_q7",
                "q": "Which of the following festivals is traditionally celebrated on a Full Moon (Poornima) night?",
                "options": ["Buddha Poornima and Guru Poornima", "Diwali", "Eid-ul-Fitr", "Karva Chauth"],
                "ans": "Buddha Poornima and Guru Poornima",
                "hint": "The name of the festival explicitly contains the Sanskrit word for Full Moon.",
                "explanation": "Buddha Poornima, Guru Poornima, and Rakshabandhan are all celebrated on the Full Moon (Poornima) when the lunar disc is completely illuminated.",
                "solution_steps": [
                    "Step 1: Check the lunar alignment of major Indian spiritual celebrations.",
                    "Step 2: Notice that Buddha Poornima and Guru Poornima take place on the Full Moon.",
                    "Step 3: Confirm that Buddha Poornima and Guru Poornima occur on Poornima."
                ]
            },
            {
                "id": "c3_q8",
                "q": "What celestial sighting officially marks the beginning of the joyous festival of Eid?",
                "options": ["First sighting of the slender crescent Moon in the evening sky", "A total solar eclipse at midday", "The appearance of a bright red shooting star", "The sunrise on the winter solstice"],
                "ans": "First sighting of the slender crescent Moon in the evening sky",
                "hint": "The delicate waxing crescent moon is known as the 'hilal'.",
                "explanation": "The Islamic lunar calendar months begin with the verified sighting of the waxing crescent Moon (hilal) just after sunset.",
                "solution_steps": [
                    "Step 1: Review how Islamic calendar months are determined.",
                    "Step 2: Recall that the end of Ramadan and the start of Eid-ul-Fitr depend on spotting the new crescent moon.",
                    "Step 3: Conclude that the first sighting of the crescent Moon marks the festival of Eid."
                ]
            },
            {
                "id": "c3_q9",
                "q": "Why does the Moon never physically change shape, even though its phases look different?",
                "options": ["It is always a spherical rock; only the illuminated fraction visible from Earth changes", "The Moon melts into liquid and resolidifies every two weeks", "Space monsters carve off slices of the Moon each week", "The Moon deflates and reinflates like a cosmic basketball"],
                "ans": "It is always a spherical rock; only the illuminated fraction visible from Earth changes",
                "hint": "Half the Moon is always lit by the Sun; our angle of view is what changes.",
                "explanation": "The Moon remains a solid sphere. Exactly half is always sunlit, but our view of that sunlit half shifts as the Moon orbits the Earth.",
                "solution_steps": [
                    "Step 1: Recognize that the Moon's physical mass and spherical geometry remain constant.",
                    "Step 2: Understand that lunar phases result entirely from our shifting angle of observation as the Moon orbits Earth.",
                    "Step 3: Confirm that only the visible illuminated fraction changes, not the physical Moon."
                ]
            },
            {
                "id": "c3_q10",
                "q": "What term describes the Moon when the visible illuminated portion is growing larger night after night?",
                "options": ["Waxing Moon", "Waning Moon", "Eclipse", "Perigee"],
                "ans": "Waxing Moon",
                "hint": "Waxing means growing or increasing in illumination.",
                "explanation": "A waxing Moon refers to the two-week period from New Moon to Full Moon when the visible sunlit portion steadily increases in size.",
                "solution_steps": [
                    "Step 1: Differentiate between the two halves of the lunar phase cycle.",
                    "Step 2: Recall that 'waxing' denotes growing illumination and 'waning' denotes shrinking illumination.",
                    "Step 3: Confirm that a growing Moon is termed a waxing Moon."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "badge": "Space Exploration",
        "sim_id": "sim_quiz_space",
        "description": "Mastery challenge testing India's Chandrayaan-3 lunar landing, Vikram lander engineering, and Pragyan rover discoveries.",
        "questions": [
            {
                "id": "c4_q1",
                "q": "Which premier Indian space agency engineered and executed the Chandrayaan-3 lunar mission?",
                "options": ["ISRO (Indian Space Research Organisation)", "NASA", "ESA", "Roscosmos"],
                "ans": "ISRO (Indian Space Research Organisation)",
                "hint": "India's national space agency headquartered in Bengaluru.",
                "explanation": "ISRO (Indian Space Research Organisation) designed, launched, and operated the Chandrayaan-3 mission from Sriharikota.",
                "solution_steps": [
                    "Step 1: Identify India's national civilian space agency.",
                    "Step 2: Recognize the acronym ISRO: Indian Space Research Organisation.",
                    "Step 3: Confirm that ISRO developed and executed Chandrayaan-3."
                ]
            },
            {
                "id": "c4_q2",
                "q": "What is the official name of the Chandrayaan-3 lunar lander that touched down on the Moon?",
                "options": ["Vikram Lander", "Pragyan Lander", "Pushpak Lander", "Aryabhata Lander"],
                "ans": "Vikram Lander",
                "hint": "Named in honor of Vikram Sarabhai, the visionary founder of India's space programme.",
                "explanation": "The Chandrayaan-3 landing module was named the Vikram Lander, commemorating the pioneer of Indian space science.",
                "solution_steps": [
                    "Step 1: Distinguish between the lander module and the rover module.",
                    "Step 2: Recall that the four-legged landing craft was named Vikram.",
                    "Step 3: Confirm that the landing craft is the Vikram Lander."
                ]
            },
            {
                "id": "c4_q3",
                "q": "Near which unique and historically unexplored geographical region of the Moon did Chandrayaan-3 land?",
                "options": ["Lunar south pole region", "Lunar north pole ocean", "Equatorial Sea of Tranquility", "Direct center of the dark side"],
                "ans": "Lunar south pole region",
                "hint": "India became the very first nation in history to land near this frozen polar area.",
                "explanation": "Chandrayaan-3 made human space history by becoming the first spacecraft ever to land successfully in the rugged lunar south polar region.",
                "solution_steps": [
                    "Step 1: Review the unique achievement of Chandrayaan-3.",
                    "Step 2: Note that previous nations landed near the equator, while India targeted the south pole.",
                    "Step 3: Confirm that Chandrayaan-3 touched down near the lunar south pole."
                ]
            },
            {
                "id": "c4_q4",
                "q": "How did the Vikram Lander slow down its descent toward the airless lunar surface?",
                "options": ["Using throttleable reverse-firing rocket thrusters (retro-rockets)", "Deploying a massive aerodynamic silk parachute", "Gliding on carbon-fiber airplane wings", "Floating down using giant helium gas balloons"],
                "ans": "Using throttleable reverse-firing rocket thrusters (retro-rockets)",
                "hint": "Because the Moon has no air, only rocket thrust can counteract gravitational descent.",
                "explanation": "In the vacuum of the Moon, parachutes cannot function. The lander used computer-controlled retro-rockets firing downwards to brake and land gently.",
                "solution_steps": [
                    "Step 1: Recognize that the Moon has no atmosphere to deploy parachutes or wings.",
                    "Step 2: Understand that reverse rocket thrust counteracts gravitational acceleration in a vacuum.",
                    "Step 3: Conclude that throttleable retro-rockets slowed the Vikram Lander's descent."
                ]
            },
            {
                "id": "c4_q5",
                "q": "What was the name of the six-wheeled mobile rover that rolled out from the Vikram Lander?",
                "options": ["Pragyan", "Curiosity", "Perseverance", "Sputnik"],
                "ans": "Pragyan",
                "hint": "Its name is the Sanskrit word for 'wisdom'.",
                "explanation": "The six-wheeled robotic rover deployed onto the lunar soil was named Pragyan, equipped with laser spectrometers to analyze minerals.",
                "solution_steps": [
                    "Step 1: Identify the robotic rover deployed from the Vikram Lander's ramp.",
                    "Step 2: Recall that the rover was named Pragyan (meaning wisdom).",
                    "Step 3: Confirm that the six-wheeled rover was Pragyan."
                ]
            },
            {
                "id": "c4_q6",
                "q": "What permanent symbols were embossed into the lunar soil by Pragyan's rear wheels as it rolled?",
                "options": ["The State Emblem of India and the ISRO logo", "A map of the solar system and a clock", "A picture of a tiger and a peacock", "The numbers 1 to 10 in Roman numerals"],
                "ans": "The State Emblem of India and the ISRO logo",
                "hint": "Special treads on the rover's wheels leave these historic insignia in the regolith.",
                "explanation": "Pragyan's wheels were engraved with the Lion Capital of Ashoka (National Emblem of India) and the ISRO emblem, printing them into the lunar dust.",
                "solution_steps": [
                    "Step 1: Recall the patriotic and scientific details engineered into Pragyan's wheel treads.",
                    "Step 2: Identify the two symbols: India's National State Emblem and the ISRO agency logo.",
                    "Step 3: Confirm that these symbols were embossed into the lunar soil."
                ]
            },
            {
                "id": "c4_q7",
                "q": "Which chemical element was unambiguously detected on the lunar south pole by Pragyan's laser spectroscope?",
                "options": ["Sulfur", "Liquid petroleum", "Plastic polymers", "Pure table salt"],
                "ans": "Sulfur",
                "hint": "A vital non-metallic yellow mineral important for understanding volcanic history.",
                "explanation": "Pragyan's Laser-Induced Breakdown Spectroscope (LIBS) conclusively detected sulfur (S) on the lunar surface, along with aluminum, calcium, and iron.",
                "solution_steps": [
                    "Step 1: Review scientific payload discoveries made by Pragyan on the Moon.",
                    "Step 2: Identify the definitive detection of sulfur announced by ISRO scientists.",
                    "Step 3: Confirm that sulfur was unambiguously detected on the lunar south pole."
                ]
            },
            {
                "id": "c4_q8",
                "q": "Why are scientists eager to find subterranean water ice in permanently shadowed polar craters on the Moon?",
                "options": ["It can be purified into drinking water and split into hydrogen and oxygen rocket fuel", "It will be used to make ice cream for tourists on Earth", "It can freeze the entire Moon so it stops moving in orbit", "It can be melted to create a giant freshwater swimming pool"],
                "ans": "It can be purified into drinking water and split into hydrogen and oxygen rocket fuel",
                "hint": "Water (H2O) provides both life support and rocket propellants.",
                "explanation": "Lunar water ice can sustain human astronaut bases with drinking water and oxygen, while its hydrogen and oxygen can fuel rockets for deep space voyages.",
                "solution_steps": [
                    "Step 1: Understand the logistical value of in-situ resource utilization in space exploration.",
                    "Step 2: Recognize that water provides life-support oxygen, drinking water, and liquid rocket propellant.",
                    "Step 3: Conclude that lunar water ice can be used for drinking water and rocket fuel."
                ]
            },
            {
                "id": "c4_q9",
                "q": "What official commemorative designation was declared in India for August 23 to celebrate the Chandrayaan-3 landing?",
                "options": ["National Space Day", "National Science Festival", "Astronomy Holiday", "Lunar Discovery Day"],
                "ans": "National Space Day",
                "hint": "A special annual day honoring India's space achievements and inspiring students.",
                "explanation": "August 23 was officially declared by the Government of India as National Space Day to commemorate the historic landing of Chandrayaan-3.",
                "solution_steps": [
                    "Step 1: Identify national commemorative observances created following Chandrayaan-3's triumph.",
                    "Step 2: Recall that August 23 was designated as National Space Day.",
                    "Step 3: Confirm that August 23 is celebrated as National Space Day."
                ]
            },
            {
                "id": "c4_q10",
                "q": "What overarching scientific takeaway connects sky observation from ancient sundials to modern lunar landers?",
                "options": ["Careful observation and physical reasoning enable humanity to understand and explore the cosmos", "Only modern digital computers can observe anything in the sky", "Ancient humans had no understanding of shadows or the Sun", "Space exploration has no connection to the science of light and shadows"],
                "ans": "Careful observation and physical reasoning enable humanity to understand and explore the cosmos",
                "hint": "From tracking shadows on stone to landing on the Moon, scientific inquiry drives human progress.",
                "explanation": "The journey from ancient sundials measuring shadows to spacecraft exploring the Moon shows that systematic observation and science empower cosmic discovery.",
                "solution_steps": [
                    "Step 1: Synthesize the progression of astronomical knowledge throughout Chapter 10.",
                    "Step 2: Observe that basic shadow principles lead directly to advanced celestial mechanics and space exploration.",
                    "Step 3: Conclude that careful observation and physical reasoning enable humanity to understand and explore the cosmos."
                ]
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

print("=== CHECKING SLIDES 17 TO 20 ===")
assert len(slides_part3) == 4, f"Expected 4 slides, got {len(slides_part3)}"

for s in slides_part3:
    sid = s['id']
    title = s['title']
    title_words = len(title.split())
    assert 1 <= title_words <= 3, f"Slide {sid} title '{title}' must be 1-3 words (got {title_words})"
    
    assert len(s['questions']) == 10, f"Slide {sid} must have 10 questions (got {len(s['questions'])})"
    
    s_str = json.dumps(s)
    for name in HUMAN_NAMES:
        assert not re.search(r'\b' + re.escape(name) + r'\b', s_str, re.IGNORECASE), f"Slide {sid} contains name '{name}'"
    for persona in FORBIDDEN_PERSONAS:
        assert not re.search(persona, s_str, re.IGNORECASE), f"Slide {sid} contains persona '{persona}'"
        
    for q in s['questions']:
        qid = q['id']
        assert len(q['options']) == 4, f"Question {qid} must have 4 options"
        assert q['ans'] in q['options'], f"Question {qid} ans '{q['ans']}' not in options"
        assert len(q['hint']) > 5, f"Question {qid} hint too short"
        assert len(q['explanation']) > 15, f"Question {qid} explanation too short"
        assert len(q['solution_steps']) == 3, f"Question {qid} must have 3 solution steps (got {len(q['solution_steps'])})"

print("Slides 17 to 20 verified successfully!")

