"""
Part 2 of NCERT Class 5 Science Chapter 7: Energy - How Things Work
Slides 9 to 16
Short Headings (1-3 words) with exact same meaning:
9. Efficient Lighting
10. Electric Safety
11. Clean Energy
12. Wind Pinwheel
13. Sun Lens
14. Water Wheel
15. Mountain Gharaats
16. Green Future
Zero Raw LaTeX! Pure clean Unicode symbols.
"""

import sys

SLIDES_PART2 = [
    {
        "id": 9,
        "title": "Efficient Lighting",
        "subtitle": "Energy Efficiency: Incandescent Filaments vs Solid-State LED Bulbs",
        "concept_html": """
            <p>Not all light fixtures are created equal. When electricity flows into a lighting device, we want it to produce bright <strong>light</strong>, not wasteful <strong>heat</strong>. This is the heart of <strong>energy efficiency</strong>.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-rose-400 block mb-1">💡 Old Incandescent Filament Bulb</span>
                    <p class="text-xs text-slate-300">
                        Traditional yellow bulbs force electric current through a thin tungsten metal wire. The wire gets white-hot (over 2,500°C). Shockingly, <strong>90% of electricity is wasted as scorching heat</strong>, with only 10% emitted as useful visible light!
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">🌟 Modern Solid-State LED Bulb</span>
                    <p class="text-xs text-slate-300">
                        A Light Emitting Diode (LED) uses semiconductor microchips. Electrons release photons of light directly without needing to heat up a glowing wire. LEDs convert over <strong>80% of electricity directly into light</strong>, staying cool and using a fraction of the power!
                    </p>
                </div>
            </div>
            <p>A 9-watt modern LED bulb produces the exact same illumination as an old 60-watt filament bulb, conserving precious electricity and significantly lowering household electricity bills.</p>
        """,
        "spoken_text": "Let us explore energy efficiency in modern lighting. For over a century, homes were illuminated by traditional glass bulbs with thin glowing tungsten filaments. But did you know that an old incandescent bulb wastes ninety percent of its electricity as scorching heat? You cannot even touch it after a few minutes! Today, India has revolutionized illumination with modern Light Emitting Diodes, or LEDs. LEDs use semiconductor chips that emit cool, brilliant light directly without wasting energy as heat. A tiny nine-watt LED produces the exact same brightness as an old sixty-watt bulb while using eighty-five percent less electrical energy!",
        "lecture_script": "Compares traditional incandescent filament bulbs with solid-state LED lighting, detailing the principles of energy efficiency, thermal energy waste, and electricity conservation.",
        "checkpoints": [
            {
                "question": "Why are modern LED bulbs considered far more energy-efficient than traditional tungsten filament bulbs?",
                "options": [
                    "They convert most electrical energy directly into light rather than wasting 90% as heat",
                    "They burn kerosene fuel secretly inside plastic",
                    "They only work when exposed to rain",
                    "They require three times more electricity to turn on"
                ],
                "correct": 0,
                "explanation": "LEDs produce cold light via semiconductor luminescence, converting over 80% of energy into light, whereas filament bulbs waste up to 90% as unwanted thermal heat.",
                "study_insight": "India's national UJALA scheme distributed hundreds of millions of subsidized LED bulbs, saving gigawatts of electricity and reducing carbon dioxide emissions."
            },
            {
                "question": "If an old filament bulb consumes 60 watts of power to light a study desk, what wattage of modern LED can produce the same brightness?",
                "options": [
                    "About 7 to 9 watts",
                    "150 watts",
                    "600 watts",
                    "Zero watts because LEDs cannot light a desk"
                ],
                "correct": 0,
                "explanation": "Because LEDs have an exceptionally high luminous efficacy, a 7 to 9 watt LED matches the light output (lumens) of a 60 watt incandescent bulb.",
                "study_insight": "Wider adoption of energy-efficient appliances earned the BEE (Bureau of Energy Efficiency) 5-star rating saves national coal reserves and reduces household utility costs."
            }
        ]
    },
    {
        "id": 10,
        "title": "Electric Safety",
        "subtitle": "Insulation, Water Hazards, Ceramic Fuses & Vital Life-Saving Precautions",
        "concept_html": """
            <p>Electricity is a fantastic servant, but it can be an unforgiving hazard if treated carelessly. The human body is composed of over 60% water containing dissolved mineral salts, making us <strong>conductors of electricity</strong>.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-amber-400 block mb-1">🚫 Wet Hands & Water Danger</span>
                    <p class="text-xs text-slate-300">
                        Pure water is a poor conductor, but moisture on human skin contains sweat and salts that drastically lower electrical skin resistance. <strong>Never touch any switch, plug, or wire with wet hands or while standing barefoot on a damp bathroom floor!</strong>
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-cyan-400 block mb-1">🛡️ Insulation & Protective Fuses</span>
                    <p class="text-xs text-slate-300">
                        Copper wires are coated in flexible PVC plastic (an insulator that prevents electron leakage). Household distribution boxes feature safety <strong>fuses and Miniature Circuit Breakers (MCBs)</strong> that automatically trip and break the circuit during dangerous power surges!
                    </p>
                </div>
            </div>
            <p>Always insert safety plugs properly, never overload multi-plug sockets, and never poke metallic pencils, pins, or forks into wall sockets!</p>
        """,
        "spoken_text": "Listen carefully to these vital rules of electrical safety! Because our human bodies are composed mostly of water with dissolved salts, our tissues conduct electric current very easily. If electric current passes through the body, it can cause severe burns, muscle spasms, or heart stoppage. Always remember: never, ever touch an electrical switch, socket, or wire with wet hands or while standing barefoot on wet ground! Water lowers skin resistance, allowing current to enter easily. Electrical wires are safely wrapped in colourful PVC plastic insulation. If you ever spot a frayed wire with exposed copper, alert an adult immediately and do not touch it!",
        "lecture_script": "Outlines electrical safety protocols, the human body as an electrolytic conductor, water hazard physics, plastic wire insulation, and circuit breaker/fuse protective mechanisms.",
        "checkpoints": [
            {
                "question": "Why is it extremely dangerous to operate an electric switch or plug with wet hands?",
                "options": [
                    "Water on the skin contains mineral salts that drastically reduce electrical resistance, risking severe electric shock",
                    "Water turns copper wires into rubber instantly",
                    "Wet fingers make the light bulb shine too brightly",
                    "Water makes plastic switches freeze"
                ],
                "correct": 0,
                "explanation": "Moisture containing dissolved salts provides a low-resistance conductive pathway, allowing potentially lethal electrical currents to flow into the body.",
                "study_insight": "Wearing rubber-soled slippers provides an insulating barrier that prevents electric current from finding an exit pathway to the ground."
            },
            {
                "question": "What is the primary function of a safety fuse or Miniature Circuit Breaker (MCB) in a home electrical panel?",
                "options": [
                    "To generate extra electric current during power cuts",
                    "To automatically melt or trip, breaking the circuit whenever current exceeds safe limits",
                    "To play pleasant music when lights are turned on",
                    "To change the colour of the electricity"
                ],
                "correct": 1,
                "explanation": "A fuse contains a low-melting-point wire that safely melts during an overload, or an MCB trips open electromagnetically, interrupting the current before wires catch fire.",
                "study_insight": "Never replace a blown fuse wire with a thick iron nail or heavy copper cable; doing so disables the safety mechanism and can cause house fires."
            }
        ]
    },
    {
        "id": 11,
        "title": "Clean Energy",
        "subtitle": "Fossil Fuel Emissions vs Zero-Pollution Sun, Wind & Water Energy",
        "concept_html": """
            <p>Most of the electricity powering our cities today is generated by burning pulverized <strong>coal</strong> inside massive thermal power plants. However, burning fossil fuels comes at a catastrophic environmental cost.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-rose-400 block mb-1">🏭 Coal Combustion & Smog</span>
                    <p class="text-xs text-slate-300">
                        Burning coal spews thick plumes of toxic smoke, fine particulate soot (PM2.5), sulfur dioxide, and greenhouse gases (carbon dioxide). These pollutants poison the air we breathe, cause respiratory illnesses like asthma, and accelerate global climate change.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">🌿 Renewable Clean Energy</span>
                    <p class="text-xs text-slate-300">
                        In sharp contrast, the <strong>Sun</strong>, <strong>wind</strong>, and <strong>flowing water</strong> generate clean, green energy without emitting a single puff of smoke, soot, or toxic ash! Furthermore, unlike coal which will run out, sunlight and wind are inexhaustible.
                    </p>
                </div>
            </div>
            <p>Harnessing renewable energy is humanity's most crucial scientific mission to protect our blue planet and ensure fresh, clean air for future generations.</p>
        """,
        "spoken_text": "Let us compare how our world produces electricity. In conventional thermal power plants, thousands of tonnes of black coal are burned every single hour. This combustion boils water into high-pressure steam, but it also releases massive clouds of suffocating black smoke, poisonous sulfur gases, and planet-warming carbon dioxide! This causes air pollution and smog. But nature offers us a far superior path: clean, renewable energy! Sunlight, blowing breezes, and gushing mountain rivers provide limitless power without creating any smoke, ash, or chemical waste. Clean energy keeps our skies crystal blue and our lungs healthy!",
        "lecture_script": "Contrasts the pollution, greenhouse emissions, and finite nature of coal-fired electricity with clean, infinite renewable energy harnessed from sunlight, wind, and water.",
        "checkpoints": [
            {
                "question": "What is the major environmental drawback of generating electricity by burning coal in thermal power plants?",
                "options": [
                    "It releases toxic smoke, soot, sulfur dioxide, and carbon dioxide that cause severe air pollution and global warming",
                    "It causes rivers to dry up instantly into ice",
                    "It makes the sky turn completely purple",
                    "It uses too much rubber"
                ],
                "correct": 0,
                "explanation": "Coal combustion produces vast quantities of greenhouse gases and particulate air pollutants that harm human respiratory health and heat the global atmosphere.",
                "study_insight": "Coal is a non-renewable fossil fuel; once Earth's geological deposits are mined and burned, they cannot be replenished within human lifetimes."
            },
            {
                "question": "Why are solar, wind, and hydroelectric energy classified as 'clean renewable energy'?",
                "options": [
                    "They generate electricity without producing smoke or toxic waste, and their natural sources never run out",
                    "They can only be used on completely silent days",
                    "They are made from melted plastic bottles",
                    "They only work when connected to car batteries"
                ],
                "correct": 0,
                "explanation": "Renewable energy sources naturally replenish themselves constantly without emitting harmful exhaust fumes or generating toxic combustion residues.",
                "study_insight": "India possesses one of the world's largest solar installations, such as the Bhadla Solar Park in Rajasthan spanning over 5,700 hectares."
            }
        ]
    },
    {
        "id": 12,
        "title": "Wind Pinwheel",
        "subtitle": "Activity 6: Aerodynamic Pinwheels & Kinetic Wind Force in Action",
        "concept_html": """
            <p>Wind is simply air in motion. Though air is invisible, moving air possesses tremendous <strong>kinetic energy</strong>. In <strong>Activity 6: The Paper Pinwheel</strong>, students capture this invisible force.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-cyan-400 block mb-1">🌀 Curved Vane Aerodynamics</span>
                    <p class="text-xs text-slate-300">
                        Cut a square sheet of craft paper diagonally from the four corners toward the centre. Fold every alternate corner flap to the central axis and secure with a smooth pushpin into a wooden pencil or stick.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">⚡ Kinetic Energy Transfer</span>
                    <p class="text-xs text-slate-300">
                        Blow a puff of breath or run forward holding the pinwheel into the breeze. The moving air molecules strike the cupped, angled paper blades, generating unequal aerodynamic pressure that spins the rotor into a dazzling visual blur!
                    </p>
                </div>
            </div>
            <p>Gigantic 100-metre industrial wind turbines across Tamil Nadu, Gujarat, and Rajasthan work on this exact same aerodynamic rotor principle, spinning generators to power entire cities!</p>
        """,
        "spoken_text": "Observe Activity 6: The Paper Pinwheel. Have you ever crafted a colourful paper pinwheel using origami paper and a simple pin attached to an eraser pencil? When the pinwheel sits motionless on a table, nothing happens. But the moment you blow a gentle puff of air or sprint across the school courtyard holding it, the paper blades spin vigorously! Invisible air molecules, rushing forward with kinetic energy, strike the angled curved blades. The air exerts mechanical pressure on the vanes, converting the wind's straight-line motion into continuous rotary spinning. This is precisely how modern wind turbines generate electricity!",
        "lecture_script": "Explains Activity 6 Paper Pinwheels, demonstrating how curved aerodynamic blades intercept horizontal wind kinetic energy and convert it into rotational mechanical motion.",
        "checkpoints": [
            {
                "question": "What causes the angled paper blades of a pinwheel to spin rapidly when you blow on them?",
                "options": [
                    "Moving air molecules possess kinetic energy that pushes against the curved blades, forcing them to rotate",
                    "The pushpin melts and pulls the paper",
                    "The paper becomes magnetic in moving air",
                    "The paper absorbs moisture and expands"
                ],
                "correct": 0,
                "explanation": "Kinetic energy from the moving air stream exerts mechanical pressure against the angled paper surfaces, translating linear wind force into rotational torque.",
                "study_insight": "Wind energy is an indirect form of solar energy: the Sun heats the Earth's surface unevenly, creating atmospheric pressure differences that cause wind to blow."
            },
            {
                "question": "How do modern utility-scale wind turbine farms use this pinwheel principle to supply electricity to cities?",
                "options": [
                    "Giant aerodynamic blades spin in the wind, turning an internal shaft connected to an electric generator",
                    "The blades reflect sunlight onto rooftop water tanks",
                    "The blades chop incoming clouds into rain drops",
                    "The turbines burn firewood inside their towers"
                ],
                "correct": 0,
                "explanation": "Huge aerodynamic blades capture the kinetic force of the wind, rotating a central low-speed shaft linked through a gearbox to an electric generator producing alternating current.",
                "study_insight": "Modern wind turbine blades are constructed from lightweight glass-fiber reinforced polymer, shaped like aircraft wings to maximize aerodynamic lift."
            }
        ]
    },
    {
        "id": 13,
        "title": "Sun Lens",
        "subtitle": "Activity 7: Optical Refraction & Concentrated Solar Radiant Energy",
        "concept_html": """
            <p>Sunlight illuminates our surroundings gently because its rays are dispersed evenly across the landscape. But what happens when you concentrate millions of dispersed light rays onto a single tiny point? <strong>Activity 7: The Magnifying Glass Experiment</strong> demonstrates this dramatically.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-amber-400 block mb-1">🔍 Convex Lens Refraction</span>
                    <p class="text-xs text-slate-300">
                        A magnifying glass features a double convex lens (thicker in the middle, thinner at edges). As parallel sunlight rays enter the curved glass, optical refraction bends (refracts) every ray toward a single central <strong>focal point</strong>.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-rose-400 block mb-1">🔥 Intense Thermal Concentration</span>
                    <p class="text-xs text-slate-300">
                        Holding the lens over a dry fallen leaf or dark paper focuses all radiant energy into a blindingly bright pinhead spot. Within seconds, temperatures at that focal point exceed 250°C! The dry leaf begins to char, smoulder, and emit curls of smoke!
                    </p>
                </div>
            </div>
            <p><strong>Safety Warning:</strong> Never look directly at the Sun through any lens, as concentrated rays will instantly cause permanent blindness. Always perform this experiment under adult supervision on a fire-safe stone surface.</p>
        """,
        "spoken_text": "Now explore Activity 7: Focusing Sunlight with a Magnifying Glass. On a bright sunny morning, hold a curved convex magnifying glass over a piece of dry fallen leaf resting safely on a stone slab. Watch the circle of light shrink as you adjust the height, concentrating until it becomes a tiny, intensely bright golden dot! What is happening? The curved glass lens refracts and focuses hundreds of spread-out sunlight rays into a single microscopic point. All that radiant solar energy is concentrated into one spot, shooting the temperature above two hundred degrees Celsius! The leaf starts to smoulder and smoke! This proves the immense concentrated power of solar radiation.",
        "lecture_script": "Covers Activity 7 with the magnifying glass convex lens, explaining optical refraction focusing dispersed sunlight rays into an intense focal point that generates scorching heat.",
        "checkpoints": [
            {
                "question": "Why does a dry leaf begin to smoke when sunlight is focused onto it through a magnifying glass?",
                "options": [
                    "The curved convex lens concentrates many dispersed sunlight rays onto a single focal point, generating extreme thermal heat",
                    "The magnifying glass contains gunpowder inside its glass",
                    "The leaf is allergic to glass",
                    "The lens freezes the leaf until it shatters"
                ],
                "correct": 0,
                "explanation": "Refraction through the convex lens gathers radiant energy spread across the lens surface and focuses it onto a tiny focal spot, raising the temperature above the leaf's combustion threshold.",
                "study_insight": "Concentrated Solar Power (CSP) plants use curved mirrors to focus sunlight onto central boiler towers, melting molten salt to drive steam turbines day and night!"
            },
            {
                "question": "What critical safety warning must always be observed when experimenting with magnifying lenses outdoors?",
                "options": [
                    "Never look directly at the Sun through any lens because concentrated rays can instantly destroy your eyesight",
                    "Never let the lens touch water",
                    "Only hold the lens upside down in the dark",
                    "Never allow shadows to touch the lens"
                ],
                "correct": 0,
                "explanation": "Focusing direct sunlight onto the sensitive retina at the back of the human eye will burn retinal cells within milliseconds, causing irreversible blindness.",
                "study_insight": "Solar cookers utilize this identical thermal concentration principle with shiny parabolic mirrors to boil lentils, rice, and bake bread without any gas or electricity."
            }
        ]
    },
    {
        "id": 14,
        "title": "Water Wheel",
        "subtitle": "Activity 8: Hydro-Kinetic Power: Flowing Water Driving Rotational Work",
        "concept_html": """
            <p>Water may feel soft and soothing to the touch, but a rushing river or falling waterfall packs immense mechanical force. In <strong>Activity 8: The Homemade Water Wheel</strong>, students construct a working hydraulic turbine.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-cyan-400 block mb-1">🥣 Spoons, Cups & Rotor Axis</span>
                    <p class="text-xs text-slate-300">
                        Insert 6 plastic spoons or small paper cups radially into a circular foam core or cork disc. Thread a smooth bamboo skewer or bicycle spoke through the centre as an axle, supported horizontally on two slotted cardboard pillars.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-blue-400 block mb-1">🌊 Gravitational Potential to Rotation</span>
                    <p class="text-xs text-slate-300">
                        Pour water steadily from a jug onto the curved cups. Water falling from a height possesses gravitational potential energy that converts into rushing kinetic energy. The impact force against each cup pushes it downward, creating rapid, unstoppable wheel rotation!
                    </p>
                </div>
            </div>
            <p>Tying a thread with a small paperclip to the spinning axle demonstrates mechanical work: the spinning water wheel easily hoists the weight upward against gravity!</p>
        """,
        "spoken_text": "Observe Activity 8: The Homemade Water Wheel. Imagine crafting a wheel using a cork disc, six plastic spoons arranged like paddle blades, and a smooth wooden axle. Position your miniature water wheel beneath a steady stream of water poured from a jug. The instant water cascades down, the spoons catch the falling stream! The gravitational potential energy of the elevated water transforms into rushing kinetic energy, striking the spoon bowls with continuous impact force. The wheel spins vigorously on its axle! If you tie a thread with a tiny pebble to the axle, the rotating wheel hoists the pebble up into the air, proving that flowing water performs real mechanical work!",
        "lecture_script": "Explains Activity 8 Water Wheel construction, demonstrating how falling water converts gravitational potential energy into kinetic rotational force that performs useful mechanical work.",
        "checkpoints": [
            {
                "question": "What energy transformation occurs when water poured from a pitcher strikes the paddles of a water wheel?",
                "options": [
                    "Gravitational potential energy of falling water converts into mechanical kinetic energy of the spinning wheel",
                    "Water turns into chemical petroleum inside the spoons",
                    "The wheel turns into an ice cube",
                    "Light energy turns into nuclear radiation"
                ],
                "correct": 0,
                "explanation": "As water drops downward under gravity, its potential energy converts into kinetic energy. The momentum transferred upon striking the spoon paddles rotates the wheel.",
                "study_insight": "Hydropower stations store millions of tonnes of water behind high concrete dams; releasing this water through deep penstock pipes spins massive hydraulic turbines."
            },
            {
                "question": "How did ancient civilizations use water wheels before electricity was ever discovered?",
                "options": [
                    "To grind wheat into flour, lift irrigation water into farm fields, and power blacksmith hammers",
                    "To charge electric mobile phones",
                    "To broadcast television signals across mountains",
                    "To fly aeroplanes across the sea"
                ],
                "correct": 0,
                "explanation": "Traditional water wheels provided direct mechanical shaft power for milling grains, driving irrigation water scoops (Norias), and powering sawmill blades.",
                "study_insight": "The Archimedes screw and the Persian wheel are related ancient hydraulic engineering marvels that utilized rotational water mechanics."
            }
        ]
    },
    {
        "id": 15,
        "title": "Mountain Gharaats",
        "subtitle": "Traditional Himalayan Watermills: Zero-Carbon Engineering Heritage",
        "concept_html": """
            <p>Long before electrical grids reached remote mountain valleys, indigenous communities in Himachal Pradesh, Uttarakhand, and Jammu & Kashmir mastered zero-carbon water engineering through the <strong>Gharaat</strong> (traditional watermill).</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">🏔️ Diverted Torrent & Wooden Chute</span>
                    <p class="text-xs text-slate-300">
                        Villagers construct a gentle stone-lined channel (kuhl) that diverts a portion of a raging glacier stream. The water is channeled into a steeply angled hollow wooden chute (penstock) carved from tree trunks, which shoots water at high velocity!
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-amber-400 block mb-1">⚙️ Heavy Stone Grinding Wheels</span>
                    <p class="text-xs text-slate-300">
                        The high-pressure jet hits a submerged multi-bladed wooden turbine wheel (panchakkari). An upright central spindle connects directly to a heavy circular grinding stone inside the upper room. As the stream flows, the stone rotates quietly, grinding whole wheat, maize, and millets into fresh nutritious flour!
                    </p>
                </div>
            </div>
            <p>Gharaats operate without a single drop of fuel or electricity, generating zero pollution. Furthermore, because stone grinding stays cool, heat-sensitive vitamins in the grain are preserved!</p>
        """,
        "spoken_text": "Travel in your imagination to the snow-peaked mountains of Himachal Pradesh and Uttarakhand! Nestled beside foaming Himalayan mountain torrents stand small stone cottages called Gharaats. A Gharaat is an ingenious traditional watermill that has ground grain for over a thousand years without using a single watt of electricity or a single drop of petrol! Fast-flowing mountain water is diverted down a steep wooden flume. The high-speed water jet strikes angled wooden turbine blades underneath the floor, spinning an upright axle. Upstairs, a heavy circular grinding stone rotates smoothly over another, grinding wheat and corn into wholesome flour. It is a masterclass in clean, traditional engineering!",
        "lecture_script": "Details the traditional Himalayan Gharaat (watermill), explaining the diversion canal, wooden chute, horizontal turbine runner, and upper grinding stones operating purely on hydraulic stream power.",
        "checkpoints": [
            {
                "question": "What powers a traditional Himalayan 'Gharaat' to grind grain into flour without electricity?",
                "options": [
                    "The kinetic force of fast-flowing mountain stream water striking wooden turbine blades",
                    "A hidden underground diesel generator",
                    "Solar electric batteries charged during the night",
                    "Trained horses walking in continuous circles"
                ],
                "correct": 0,
                "explanation": "A Gharaat harnesses the natural kinetic and potential energy of high-altitude mountain torrents directed through a wooden chute onto a submerged runner turbine.",
                "study_insight": "Slow cold-stone milling in a Gharaat keeps flour temperatures low, preserving healthy wheat-germ oils, bran fibre, and B-complex vitamins."
            },
            {
                "question": "Why are indigenous traditional technologies like the Gharaat being revived and modernized today?",
                "options": [
                    "Because they provide 100% clean, renewable, decentralized local energy with zero carbon footprint",
                    "Because they produce heavy black smoke",
                    "Because they consume high-voltage electricity",
                    "Because they make grain turn into plastic"
                ],
                "correct": 0,
                "explanation": "Modernizing Gharaat turbines with precision ball bearings and micro-generators allows mountain villages to mill grain and generate local electricity sustainably.",
                "study_insight": "Decentralized micro-hydro installations based on modernized Gharaats provide self-reliant energy security to isolated Himalayan border communities."
            }
        ]
    },
    {
        "id": 16,
        "title": "Green Future",
        "subtitle": "Modern Renewable Infrastructure & Responsible Energy Conservation Habits",
        "concept_html": """
            <p>Our global transition from polluting fossil fuels to clean renewable energy requires both <strong>grand national infrastructure</strong> and <strong>mindful individual habits</strong>.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-cyan-400 block mb-1">☀️ Mega Solar Parks & Wind Farms</span>
                    <p class="text-xs text-slate-300">
                        Across sun-drenched plains and windy coastlines, thousands of photovoltaic solar panels and tall aerodynamic wind turbines generate clean electricity directly feeding into India's National Power Grid, powering trains, schools, and hospitals.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">🌱 Everyday Conservation Habits</span>
                    <p class="text-xs text-slate-300">
                        Remember the golden scientific rule: <em>The cleanest energy is the energy we never waste!</em> Simple daily actions preserve our planet:
                        <ul class="list-disc pl-4 mt-1 text-[11px] space-y-1">
                            <li>Switch off fans, lights, and monitors when stepping out of a room.</li>
                            <li>Unplug chargers when devices reach 100% to stop phantom power draw.</li>
                            <li>Walk, cycle, or use school buses instead of individual petrol cars.</li>
                            <li>Dry washed clothes in warm natural sunshine rather than electric dryers.</li>
                        </ul>
                    </p>
                </div>
            </div>
            <p>Every student is an active Earth Guardian: through conscious energy conservation, we safeguard our atmosphere and preserve Earth's climate for all living beings!</p>
        """,
        "spoken_text": "We conclude our exploration of energy with a shared pledge for a green future! Across our nation, magnificent modern infrastructure is rising: vast solar photovoltaic parks in our deserts, towering wind turbines along ocean coasts, and smart electrical grids. But large solar parks alone cannot save our planet; our personal habits matter just as much! Remember that the cleanest kilowatt of energy is the one you never waste. Always switch off fans, computers, and lights when leaving an empty room. Walk or ride a bicycle for short errands. By choosing clean renewable energy and cutting wasteful consumption, every young scientist helps protect our precious planet Earth!",
        "lecture_script": "Synthesizes modern renewable energy infrastructure (solar parks, wind farms, hydro grids) with personal energy conservation practices and environmental stewardship.",
        "checkpoints": [
            {
                "question": "Which of the following actions is the most effective daily habit for conserving electrical energy at home?",
                "options": [
                    "Switching off fans, air conditioners, and lights immediately upon exiting an empty room",
                    "Leaving the television running while sleeping to keep the room cheerful",
                    "Keeping the refrigerator door wide open while studying",
                    "Charging a smartphone continuously for three days straight"
                ],
                "correct": 0,
                "explanation": "Turning off appliances when not in use stops unnecessary electricity consumption, reducing the amount of coal burned at power stations.",
                "study_insight": "'Phantom loads' or vampire draw refers to the electricity consumed by appliances (televisions, microwave displays, chargers) even when placed in standby mode."
            },
            {
                "question": "What core message does the scientific principle 'The cleanest energy is the energy saved' teach us?",
                "options": [
                    "Preventing wasteful energy consumption eliminates the pollution and resource depletion needed to generate it in the first place",
                    "That we should never use any electricity ever again",
                    "That burning coal produces cleaner air than solar panels",
                    "That energy can only be saved inside glass jars"
                ],
                "correct": 0,
                "explanation": "Energy conservation directly reduces demand on power generating stations, preventing greenhouse gas emissions, saving water, and cutting fossil fuel extraction.",
                "study_insight": "Replacing ordinary household appliances with BEE 5-star rated equipment can cut a family's electricity consumption by up to 30% annually."
            }
        ]
    }
]

print("Part 2 slides defined:", len(SLIDES_PART2))

