"""
Part 1 of NCERT Class 5 Science Chapter 7: Energy - How Things Work
Slides 1 to 8
Short Headings (1-3 words) with exact same meaning:
1. What Energy Does
2. Balloon Rocket
3. Vibrating Strings
4. Warming Sun
5. Food Battery
6. Fuel Power
7. Burning Diya
8. Electric Current
Zero Raw LaTeX! Pure clean Unicode symbols.
"""

import sys

SLIDES_PART1 = [
    {
        "id": 1,
        "title": "What Energy Does",
        "subtitle": "Definition: Movement, Light, Sound, Work & Thermal Changes",
        "concept_html": """
            <p>Every single activity in our bustling world requires <strong>energy</strong>. From a soaring eagle and a speeding school bus to the gentle flicker of a bedside lamp and the warmth of a morning cup of milk, energy is the fundamental driving force of nature.</p>
            <div class="p-3.5 my-3 rounded-2xl bg-amber-950/40 border border-amber-500/40">
                <span class="text-xs font-bold text-amber-300 block mb-1">Scientific Definition of Energy:</span>
                <p class="text-xs text-slate-200 leading-relaxed">
                    <strong>Energy</strong> is defined in physical science as the capacity or ability to do work, make things move, produce light or sound, and cause temperature changes. Whenever anything happens in the universe, energy is being used or transformed!
                </p>
            </div>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5 my-3 text-xs text-center">
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-lg block mb-1">🏃</span>
                    <span class="font-bold text-cyan-400 block">Movement</span>
                    <span class="text-slate-400 text-[10px]">Kinetic action of moving bodies</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-lg block mb-1">💡</span>
                    <span class="font-bold text-amber-400 block">Light</span>
                    <span class="text-slate-400 text-[10px]">Radiant waves illuminating space</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-lg block mb-1">🔔</span>
                    <span class="font-bold text-purple-400 block">Sound</span>
                    <span class="text-slate-400 text-[10px]">Pressure vibrations through air</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-lg block mb-1">🔥</span>
                    <span class="font-bold text-rose-400 block">Thermal</span>
                    <span class="text-slate-400 text-[10px]">Heat raising particle temperatures</span>
                </div>
            </div>
            <p>Energy cannot be seen directly, but its effects are unmistakably visible. When leaves rustle in the breeze, wind energy is pushing them; when water boils on a stove, thermal energy is speeding up water molecules.</p>
        """,
        "spoken_text": "Welcome young scientists to Chapter 7: Energy, How Things Work! Look around your room right now. What makes the ceiling fan rotate, the bulb glow with bright light, or your smartphone chime with ringtones? It is energy! In science, energy is defined as the capacity to do work, create motion, generate sound, emit light, and change temperature. While we cannot hold energy in our hands like a pebble, we observe its incredible power whenever objects accelerate, warm up, or illuminate our surroundings.",
        "lecture_script": "Introduces the scientific definition of energy as the capacity to cause motion, work, light, sound, and thermal changes, connecting everyday phenomena to energy manifestations.",
        "checkpoints": [
            {
                "question": "Which of the following is the most scientifically accurate definition of energy?",
                "options": [
                    "A visible liquid stored inside power stations",
                    "The capacity to do work, cause movement, or produce heat, light, and sound",
                    "A chemical substance found only in petroleum",
                    "A force that only acts during the daytime"
                ],
                "correct": 1,
                "explanation": "Energy is fundamentally defined as the ability or capacity to perform work, create motion, or produce light, sound, and thermal changes.",
                "study_insight": "Although energy takes many forms such as kinetic, chemical, and electrical, it is governed by the Law of Conservation of Energy: energy cannot be created or destroyed, only changed from one form to another."
            },
            {
                "question": "When a ringing school bell vibrates and sends chime notes across the playground, which form of energy is reaching your ears?",
                "options": [
                    "Sound energy travelling as pressure waves through air",
                    "Magnetic energy flowing through the ground",
                    "Nuclear energy radiated from the sun",
                    "Chemical energy stored in brass metal"
                ],
                "correct": 0,
                "explanation": "Striking the bell causes it to vibrate rapidly, transferring mechanical vibrations into air molecules as sound waves that stimulate our eardrums.",
                "study_insight": "Sound cannot travel through a vacuum; it requires a physical medium such as air, water, or solid metal to propagate its energy waves."
            }
        ]
    },
    {
        "id": 2,
        "title": "Balloon Rocket",
        "subtitle": "Activity 1: Stored Elastic Energy Converted into Forward Thrust",
        "concept_html": """
            <p>How does stored energy produce rapid forward motion? In <strong>Activity 1: The Balloon Air Rocket</strong>, we explore how trapped, pressurized air can propel an object across a room along a guide string.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-cyan-400 block mb-1">🎈 Stored Elastic Energy</span>
                    <p class="text-xs text-slate-300">
                        Blowing air into a rubber balloon forces its elastic walls to stretch outward. The compressed air molecules inside are pushed closer together, storing <strong>elastic potential energy</strong> under pressure.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-amber-400 block mb-1">🚀 Action and Reaction Thrust</span>
                    <p class="text-xs text-slate-300">
                        When the balloon neck is released, the stretched rubber snaps back, forcing compressed air backward at high speed. Following Newton's law of motion, the escaping backward jet produces an equal forward push (thrust) that shoots the balloon rocket forward along the taut straw guide!
                    </p>
                </div>
            </div>
            <p>This simple classroom experiment mirrors the exact engineering propulsion principle that launches modern ISRO space launch vehicles like the PSLV and LVM3 into orbit!</p>
        """,
        "spoken_text": "Let us examine Activity 1: The Balloon Air Rocket. When we blow breath into a rubber balloon, the rubber skin stretches taut. Stored elastic potential energy builds up within the trapped, compressed air. Now, tape that balloon to a drinking straw threaded along a smooth horizontal string. What happens the moment you let go of the nozzle? The pressurized air rushes backward in a furious jet! That backward rush exerts an equal and opposite forward reaction force, shooting your balloon rocket whizzing across the room! This exact rocket thrust mechanism powers satellites into outer space.",
        "lecture_script": "Explains Activity 1 Balloon Rocket experiment, demonstrating the conversion of stored elastic potential energy into kinetic motion via backward air jet action and forward reaction thrust.",
        "checkpoints": [
            {
                "question": "What form of energy is stored inside an inflated, stretched balloon before its nozzle is released?",
                "options": [
                    "Electrical energy stored in copper wires",
                    "Elastic potential energy in the stretched rubber and compressed air",
                    "Nuclear energy in atomic cores",
                    "Thermal energy from boiling water"
                ],
                "correct": 1,
                "explanation": "Inflating the balloon stretches its rubber molecules and compresses air particles inside, storing elastic potential energy waiting to be released.",
                "study_insight": "Potential energy is stored energy possessed by an object due to its position, compression, or chemical state."
            },
            {
                "question": "Why does the balloon rocket zoom forward when air rushes backward out of its open nozzle?",
                "options": [
                    "Because warm air is attracted to the opposite wall",
                    "Because the escaping backward air stream creates an equal and opposite forward push",
                    "Because gravity pulls the balloon sideways",
                    "Because the string pulls the straw magnetically"
                ],
                "correct": 1,
                "explanation": "According to the principle of action and reaction, as air exhausts backward with force, an opposing reactive thrust propels the rocket assembly forward.",
                "study_insight": "This physical action-reaction principle governs rocket engines, jet aeroplanes, and even the propulsion of swimming squids in the ocean."
            }
        ]
    },
    {
        "id": 3,
        "title": "Vibrating Strings",
        "subtitle": "Activity 2: Rubber Band Guitars & Sound Energy Wave Physics",
        "concept_html": """
            <p>Sound is not magical; it is pure mechanical energy in rapid motion. In <strong>Activity 2: The Rubber Band Guitar</strong>, students stretch rubber bands of varying widths across an empty shoebox or hollow cardboard container.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-purple-400 block mb-1">🎸 Plucking and Mechanical Vibration</span>
                    <p class="text-xs text-slate-300">
                        When you pull and release a stretched rubber band, you supply mechanical kinetic energy. The band oscillates rapidly back and forth in a blurry vibration, colliding with adjacent air molecules thousands of times every second.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-cyan-400 block mb-1">🔊 Resonance Chamber Amplification</span>
                    <p class="text-xs text-slate-300">
                        A thin rubber band vibrating alone in open air produces a faint hum. But when mounted over an open cardboard box, the vibrating band sets the enclosed column of air into sympathetic resonance, dramatically amplifying the volume into clear, musical notes!
                    </p>
                </div>
            </div>
            <p>Tighter and thinner rubber bands vibrate faster (higher frequency), generating a high-pitched sharp note, whereas looser, thicker bands oscillate more slowly, creating deep bass vibrations.</p>
        """,
        "spoken_text": "Now let us construct Activity 2: The Rubber Band Guitar. Take an empty cardboard shoebox and stretch three different rubber bands across its open top: one thin, one medium, and one thick. When you pluck a band with your fingertip, your finger delivers mechanical energy. Watch closely: the rubber band blurs as it vibrates back and forth! Each rapid vibration strikes neighboring air molecules, sending invisible pressure waves rippling across the room into your ears. Notice that tighter, thinner bands vibrate faster to produce high-pitched notes, while thick bands vibrate slowly to produce deep tones.",
        "lecture_script": "Covers Activity 2 Rubber Band Guitars, detailing how mechanical plucking generates acoustic sound energy through high-frequency vibrations and cardboard chamber resonance.",
        "checkpoints": [
            {
                "question": "What physical motion must occur in an object for it to produce sound energy?",
                "options": [
                    "It must undergo rapid back-and-forth vibrations",
                    "It must completely melt into a liquid",
                    "It must be painted in bright primary colours",
                    "It must remain perfectly motionless"
                ],
                "correct": 0,
                "explanation": "All sound originates from mechanical vibrations. As an object vibrates, it repeatedly compresses and rarefies surrounding air particles, creating sound waves.",
                "study_insight": "Placing your fingers gently against your throat while humming lets you directly feel the vibrations of your vocal cords producing sound energy."
            },
            {
                "question": "In the rubber band guitar experiment, how does stretching a rubber band tighter change the musical note it produces?",
                "options": [
                    "It stops vibrating completely",
                    "It vibrates faster, creating a higher-pitched sound",
                    "It turns the sound into green light",
                    "It produces a lower bass rumble"
                ],
                "correct": 1,
                "explanation": "Increasing tension causes the rubber band to oscillate at a higher frequency (more cycles per second), resulting in a noticeably higher pitch.",
                "study_insight": "Musicians tuning a violin, sitar, or guitar tighten peg keys to raise pitch and loosen them to lower pitch based on this identical physics principle."
            }
        ]
    },
    {
        "id": 4,
        "title": "Warming Sun",
        "subtitle": "Activity 3: Solar Radiation Absorption & Thermal Temperature Rise",
        "concept_html": """
            <p>The primary source of nearly all energy on planet Earth is the blazing Sun located 150 million kilometres away. In <strong>Activity 3: Warming Water in the Sun</strong>, students measure solar radiant energy directly.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-amber-400 block mb-1">☀️ Radiant Heat Transfer</span>
                    <p class="text-xs text-slate-300">
                        Fill two identical bowls with equal amounts of room-temperature tap water (say, 24°C). Place Bowl A in a cool, shaded classroom cupboard and place Bowl B outside under open, direct sunshine.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-rose-400 block mb-1">🌡️ Molecular Kinetic Warming</span>
                    <p class="text-xs text-slate-300">
                        After two hours, dip a laboratory thermometer into both bowls. Bowl A remains at 24°C, but Bowl B has warmed to 38°C! Solar light rays carrying radiant energy were absorbed by the water, speeding up its molecules and raising its temperature.
                    </p>
                </div>
            </div>
            <p>Dark or black-bottomed containers absorb solar heat even more aggressively than light, reflective silver surfaces, demonstrating how radiant energy converts directly into thermal heat.</p>
        """,
        "spoken_text": "Observe Activity 3: Warming Water in the Sun. Imagine placing two identical metal bowls filled with fresh tap water at room temperature. Keep one bowl inside a cool shaded cupboard, and place the other outdoors directly under blazing afternoon sunshine. Two hours later, touch the water in both bowls! The bowl kept in the cupboard is still cool, while the bowl under the sun is distinctly warm. Why? Because the Sun continuously beams radiant light and infrared energy across 150 million kilometres of empty space. As water absorbs this radiant energy, its molecules jiggle faster, causing a measurable rise in thermal temperature!",
        "lecture_script": "Explores Activity 3, showing how radiant solar energy travels through space, is absorbed by matter like water, and converts directly into internal thermal energy.",
        "checkpoints": [
            {
                "question": "What happens to the molecules of water inside a bowl as it absorbs thermal energy from the Sun?",
                "options": [
                    "They jiggle and move faster, causing the water temperature to rise",
                    "They freeze into solid crystal cubes",
                    "They lose all their electrical charge and vanish",
                    "They slow down until they become completely motionless"
                ],
                "correct": 0,
                "explanation": "Temperature is a measure of the average kinetic energy of molecules. Absorbing solar thermal energy causes water molecules to jiggle and move faster.",
                "study_insight": "Heat always flows spontaneously from a warmer object to a cooler object until thermal equilibrium is established."
            },
            {
                "question": "Why do traditional rooftop solar water heaters use black-painted metal tubes instead of white tubes?",
                "options": [
                    "Black surfaces absorb radiant solar heat much more effectively than reflective white surfaces",
                    "Black paint prevents water from leaking",
                    "Black tubes weigh less than white tubes",
                    "Black paint makes the water taste sweet"
                ],
                "correct": 0,
                "explanation": "Dark, matte black surfaces absorb virtually all incoming wavelengths of visible and infrared solar radiation, converting them efficiently into heat.",
                "study_insight": "Wearing dark clothes in peak summer feels much warmer because dark pigments absorb solar radiant energy rather than reflecting it away."
            }
        ]
    },
    {
        "id": 5,
        "title": "Food Battery",
        "subtitle": "Chemical Energy Storage: Human Metabolism & Biological Energy Reserves",
        "concept_html": """
            <p>Every living creature—from an energetic child sprinting across a football field to a chirping sparrow—requires constant energy. Where does biological energy come from? From the <strong>food we eat</strong>!</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">🍎 Chemical Energy in Nutrients</span>
                    <p class="text-xs text-slate-300">
                        Grains (rotis, rice), pulses (dal), vegetables, and fruits contain <strong>chemical energy</strong> synthesized by green plants through photosynthesis. When we chew and digest food, enzymes break down complex carbohydrates into simple glucose sugars.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-amber-400 block mb-1">🔋 The Living Battery Storage</span>
                    <p class="text-xs text-slate-300">
                        Our bodies do not consume all energy immediately. Just like rechargeable electronic batteries store chemical charge, our liver and muscles store surplus glucose as <strong>glycogen</strong> and body fat, releasing energy steadily as we walk, study, and breathe throughout the night!
                    </p>
                </div>
            </div>
            <p>Without regular food intake, our biological battery runs low: we feel sluggish, weak, and tired because our cells lack fuel to power cellular respiration.</p>
        """,
        "spoken_text": "Think about your own daily energy. How do you sprint across the playground, solve math puzzles, or keep your heart beating 24 hours a day? You run on food energy! Plants harness sunlight to create carbohydrates, proteins, and fats packed with chemical energy. When we consume rotis, fruits, and dal, our digestive system breaks these down. Inside every living cell, glucose reacts with inhaled oxygen to release mechanical energy for our muscles and heat energy to keep our body at a steady 37 degrees Celsius. Our liver and muscles act just like rechargeable batteries, storing surplus energy so we can stay active even between meals!",
        "lecture_script": "Explains food as the primary source of biological chemical energy, cellular respiration with oxygen, and internal glycogen/fat reserves acting like rechargeable batteries.",
        "checkpoints": [
            {
                "question": "What type of energy is stored inside the rice, rotis, fruits, and vegetables we eat daily?",
                "options": [
                    "Chemical energy bound in nutrient molecules",
                    "Electrical energy circulating along cables",
                    "Sound energy trapped inside seeds",
                    "Nuclear energy in atomic reactors"
                ],
                "correct": 0,
                "explanation": "Food stores chemical potential energy within the atomic bonds of carbohydrates, proteins, and lipids, created originally by plants using sunlight.",
                "study_insight": "Food energy is measured in units called Calories or Joules; 1 kilocalorie equals approximately 4,184 Joules of mechanical work!"
            },
            {
                "question": "How does the human body resemble a rechargeable battery in how it manages energy?",
                "options": [
                    "It has metal terminals sticking out of the head",
                    "It stores surplus energy from food in muscles and liver for later use during activity and sleep",
                    "It only functions when plugged into an electrical wall socket",
                    "It never requires any food or water"
                ],
                "correct": 1,
                "explanation": "The human body stores excess chemical energy as glycogen in the liver and muscles, as well as adipose fat tissue, discharging it whenever energy is needed.",
                "study_insight": "Even during sound sleep, our body consumes significant energy to keep the brain dreaming, the lungs inhaling, and the heart pumping blood."
            }
        ]
    },
    {
        "id": 6,
        "title": "Fuel Power",
        "subtitle": "Combustion Engines: Petrol, Diesel, Cooking Gas (LPG) & Coal",
        "concept_html": """
            <p>Just as human bodies burn food to move, human machines burn <strong>fuels</strong> to perform heavy mechanical work. A fuel is any substance that releases useful thermal energy when burned (combusted) with oxygen.</p>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 my-3 text-xs">
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="font-bold text-cyan-400 block mb-1">🚗 Transport Fuels</span>
                    <span class="text-slate-300"><strong>Petrol & Diesel:</strong> Liquid petroleum fractions refined from crude oil that power cars, trucks, trains, and tractors.</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="font-bold text-amber-400 block mb-1">🍳 Domestic Cooking</span>
                    <span class="text-slate-300"><strong>LPG (Liquefied Petroleum Gas):</strong> Pressurized gas cylinders powering kitchen stoves cleanly and instantly.</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="font-bold text-rose-400 block mb-1">🏭 Industrial Power</span>
                    <span class="text-slate-300"><strong>Coal & Natural Gas:</strong> Fossil fuels burned inside thermal power stations to generate high-pressure steam for turbines.</span>
                </div>
            </div>
            <p>Inside an automobile's engine cylinder, tiny droplets of petrol are mixed with air and ignited by a spark plug. The rapid combustion causes gas to expand explosively, pushing the metal piston down and spinning the vehicle's wheels!</p>
        """,
        "spoken_text": "Consider the vehicles on our roads. A motorbike or a school bus cannot run on apples or rice; it requires fuel! Fuels like petrol, diesel, compressed natural gas, and liquefied cooking gas are rich in chemical energy formed millions of years ago. Inside an engine cylinder, a tiny mist of petrol is mixed with air and ignited with a spark. The fuel burns instantly, generating super-hot, expanding gases that push the engine pistons with immense force. That piston thrust spins the crankshaft, turns the wheels, and carries passengers across hundreds of kilometres!",
        "lecture_script": "Details the role of fuels (petrol, diesel, LPG, coal) as chemical energy carriers, explaining the internal combustion engine process where burning fuel expands gases to turn wheels.",
        "checkpoints": [
            {
                "question": "What is the primary scientific function of a fuel such as petrol or LPG gas?",
                "options": [
                    "To release useful thermal and mechanical energy when combusted with oxygen",
                    "To freeze automobile engines in hot weather",
                    "To dissolve metal vehicle parts safely",
                    "To clean the car windshield while driving"
                ],
                "correct": 0,
                "explanation": "A fuel stores concentrated chemical energy that is released as intense heat and expanding gases during combustion with atmospheric oxygen.",
                "study_insight": "Fossil fuels like coal and petroleum originated from prehistoric plant and marine organism remains compressed underground under immense pressure for millions of years."
            },
            {
                "question": "What happens inside an automobile engine cylinder to push the pistons and turn the wheels?",
                "options": [
                    "Air freezes into heavy ice blocks",
                    "Fuel ignites and burns rapidly, producing high-pressure hot expanding gas that pushes pistons",
                    "Magnets pull the wheels directly without any heat",
                    "Water turns into stone"
                ],
                "correct": 1,
                "explanation": "The rapid combustion of fuel produces intensely hot, expanding gases that drive the engine pistons down, converting thermal energy into mechanical rotation.",
                "study_insight": "Modern engines use electronic fuel injectors to vaporize fuel into ultra-fine droplets, ensuring complete combustion and maximizing mileage."
            }
        ]
    },
    {
        "id": 7,
        "title": "Burning Diya",
        "subtitle": "Activity 4: Capillary Action, Fuel Vaporization & Steady Flame Chemistry",
        "concept_html": """
            <p>Every festival of lights brings an ancient scientific marvel to our doorsteps: the traditional earthen oil lamp, or <strong>diya</strong>. In <strong>Activity 4: Understanding Fuel in a Diya</strong>, students investigate what sustains a steady flame.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-amber-400 block mb-1">🪔 Capillary Liquid Siphon</span>
                    <p class="text-xs text-slate-300">
                        The twisted cotton wick rests inside the reservoir of mustard or sesame oil. Microscopic pores between cotton fibres act like tiny straw channels. Through <strong>capillary action</strong>, liquid oil defies gravity and creeps upward to the tip of the wick!
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-rose-400 block mb-1">🔥 Continuous Vapor Combustion</span>
                    <p class="text-xs text-slate-300">
                        When lit, the heat of the flame vaporizes the ascending liquid oil into gas. It is actually the <em>oil vapor</em> reacting with surrounding oxygen that burns, not the cotton wick itself! The wick simply serves as the transport pipeline.
                    </p>
                </div>
            </div>
            <p>If the oil reservoir runs dry, the protective liquid shield vanishes and the dry cotton wick burns away in seconds, proving that the oil was the true fuel supplying energy to the flame!</p>
        """,
        "spoken_text": "Examine Activity 4: The Science of a Burning Diya. During Diwali, we light beautiful clay lamps filled with mustard or sesame oil. But ask yourself: what is actually burning? It is not the cotton wick! The cotton wick is full of microscopic spaces between its twisted fibres. Through capillary action, liquid oil climbs steadily up the wick against gravity. At the burning tip, the high temperature vaporizes this liquid oil into gas. It is this hot oil vapor reacting with oxygen that burns with a warm golden flame! As long as oil flows up the wick, the flame glows brightly.",
        "lecture_script": "Covers Activity 4 on the burning diya, explaining capillary action drawing liquid oil up the cotton wick and oil vapor combustion with atmospheric oxygen.",
        "checkpoints": [
            {
                "question": "By what scientific physical process does liquid oil climb upward against gravity through a cotton diya wick?",
                "options": [
                    "Capillary action through microscopic spaces between cotton fibres",
                    "Magnetic attraction from the stars",
                    "Freezing into solid ice crystals",
                    "Solar reflection from the clay dish"
                ],
                "correct": 0,
                "explanation": "Capillary action occurs because intermolecular forces of adhesion between oil and cotton fibers overcome gravity, drawing liquid upward through narrow pores.",
                "study_insight": "The same capillary action helps tall redwood and banyan trees draw water from deep subterranean roots all the way up to leaves 50 metres high!"
            },
            {
                "question": "What happens when the oil reservoir in an earthen diya is completely exhausted?",
                "options": [
                    "The cotton wick burns away quickly and the flame extinguishes because oil was the real fuel",
                    "The diya starts producing electricity",
                    "The flame becomes ten times larger permanently",
                    "The clay bowl melts into water"
                ],
                "correct": 0,
                "explanation": "The oil is the actual chemical fuel sustaining combustion. Once oil runs out, the unprotected cotton fibers char and the flame goes out.",
                "study_insight": "A candle works on the exact same principle: melted paraffin wax is drawn up the central braided wick and vaporized to sustain the flame."
            }
        ]
    },
    {
        "id": 8,
        "title": "Electric Current",
        "subtitle": "Flowing Electrons: Versatile Transformation into Motion, Heat & Light",
        "concept_html": """
            <p>Among all human discoveries, <strong>electricity</strong> is perhaps the most versatile and adaptable form of energy. Flowing through conductive copper wires, electric current powers our modern civilization.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-cyan-400 block mb-1">⚡ Flow of Electrons</span>
                    <p class="text-xs text-slate-300">
                        Electric current is the continuous directed flow of microscopic subatomic particles called <strong>electrons</strong> through a closed conductive loop (circuit). A power source (like a battery or generator) creates the electrical push (voltage).
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-amber-400 block mb-1">🔄 Universal Energy Chameleon</span>
                    <p class="text-xs text-slate-300">
                        Electricity effortlessly converts into any desired form: into <strong>movement</strong> via electric motors in fans and mixer-grinders, into <strong>heat</strong> via nichrome coils in toasters and geysers, into <strong>light</strong> via LEDs, and into <strong>sound</strong> via loudspeakers!
                    </p>
                </div>
            </div>
            <p>If any part of an electrical circuit is broken or switched off, electron flow ceases instantly, stopping all connected appliances.</p>
        """,
        "spoken_text": "Consider the magic of electricity! At the flip of a tiny plastic wall switch, a dark room instantly floods with bright light, a refrigerator chills fresh milk, or a washing machine drum spins vigorously. Electricity is the rapid, organized drift of tiny charged particles called electrons moving through metal copper wires. Electricity is like an energy chameleon: connect it to a ceiling fan motor and it becomes kinetic rotation; connect it to an electric iron and it becomes soothing heat; connect it to a television and it becomes vibrant light and sound!",
        "lecture_script": "Explains electricity as the directed flow of electrons through conductive closed circuits, demonstrating its universal conversion into rotational motion, thermal heat, and light.",
        "checkpoints": [
            {
                "question": "What is an electric current fundamentally composed of in a copper wire circuit?",
                "options": [
                    "The directed flow of tiny charged subatomic particles called electrons",
                    "A stream of liquid water drops running inside metal pipes",
                    "Tiny magnetic marbles rolling along the outside of plastic cables",
                    "Compressed hot air expanding through glass tubes"
                ],
                "correct": 0,
                "explanation": "Electric current in metallic conductors consists of the collective drift of negatively charged valence electrons driven by electrical voltage.",
                "study_insight": "Copper and aluminum are excellent electrical conductors because their outer electrons are loosely bound and free to move from atom to atom."
            },
            {
                "question": "Which household appliance converts electrical energy primarily into kinetic rotational motion?",
                "options": [
                    "A ceiling fan",
                    "An electric bread toaster",
                    "A room heating rod",
                    "A glowing torch bulb"
                ],
                "correct": 0,
                "explanation": "A ceiling fan uses an electromagnetic motor to convert incoming electrical energy into the mechanical rotational motion of its spinning blades.",
                "study_insight": "Electric motors utilize the interaction between magnetic fields and current-carrying wire coils to produce continuous torque and rotation."
            }
        ]
    }
]

print("Part 1 slides defined:", len(SLIDES_PART1))

