"""
Part 3 of NCERT Class 5 Science Chapter 7: Energy - How Things Work
Mastery Challenge Quiz Questions 1 to 40 (Slides 17 to 20)
10 Questions per Challenge Slide with instant feedback, explanation, and solution_html.
Zero Raw LaTeX! Pure clean Unicode symbols.
"""

import sys

QUIZ_QUESTIONS = [
    # Challenge 1 (Q1 to Q10): Slides 1 to 4 Concepts
    {
        "id": 1,
        "question": "In science, what is energy defined as?",
        "options": [
            "A material solid that takes up space and has mass",
            "The ability or capacity to do work, cause motion, produce heat, light, and sound",
            "A magnetic liquid found only in car batteries",
            "A chemical element found only in diamonds"
        ],
        "answer": 1,
        "explanation": "Energy is scientifically defined as the ability or capacity to perform work, create motion, or produce light, sound, and thermal changes.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Fundamental Definition of Energy:</strong></p>
                <p class='text-slate-300'>Energy is not matter; it has no mass and occupies no volume. Rather, it is an intrinsic property of physical systems that enables them to exert forces, perform mechanical work, radiate waves, or transfer heat.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (The ability or capacity to do work)</p>
            </div>
        """
    },
    {
        "id": 2,
        "question": "What kind of energy does a stretched rubber balloon contain before its nozzle is released?",
        "options": [
            "Nuclear atomic energy",
            "Elastic potential energy stored in its stretched skin and compressed air",
            "Electrical current energy",
            "Magnetic rotational energy"
        ],
        "answer": 1,
        "explanation": "Inflating the balloon stretches its rubber polymer chains and compresses air molecules inside, storing elastic potential energy.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Elastic Potential Energy:</strong></p>
                <p class='text-slate-300'>Potential energy is stored energy resulting from deformation or relative position. When rubber is stretched, molecular bonds act like miniature coiled springs storing mechanical potential energy.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Elastic potential energy)</p>
            </div>
        """
    },
    {
        "id": 3,
        "question": "According to Newton's law of motion, why does a balloon rocket accelerate forward along a guide string?",
        "options": [
            "Because the rapid backward ejection of compressed air produces an equal and opposite forward thrust",
            "Because the string magnetically pulls the straw forward",
            "Because the air inside turns into hot steam",
            "Because room air pulls the balloon from the front"
        ],
        "answer": 0,
        "explanation": "For every action, there is an equal and opposite reaction. The backward jet of escaping air produces forward reaction thrust on the balloon.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Action-Reaction Rocket Thrust:</strong></p>
                <p class='text-slate-300'>As air rushes out backward (Action), it imparts an equal forward momentum to the balloon-straw assembly (Reaction), pushing it along the guide string.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Equal and opposite forward thrust)</p>
            </div>
        """
    },
    {
        "id": 4,
        "question": "What physical phenomenon is essential for any musical instrument or rubber band to generate sound?",
        "options": [
            "Rapid back-and-forth mechanical vibrations",
            "Melting into a liquid puddle",
            "Complete chemical combustion with fire",
            "Cooling down to absolute zero"
        ],
        "answer": 0,
        "explanation": "All sound originates from physical vibrations. Vibrating objects disturb surrounding air particles, creating compression waves.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Sound Generation & Acoustic Waves:</strong></p>
                <p class='text-slate-300'>When a string oscillates, it pushes against air molecules. These colliding molecules propagate outward as alternating longitudinal compressions and rarefactions, detected by our ears as sound.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Rapid back-and-forth mechanical vibrations)</p>
            </div>
        """
    },
    {
        "id": 5,
        "question": "How does stretching a rubber band tighter across a shoebox change the sound pitch it produces when plucked?",
        "options": [
            "The pitch becomes higher because the band vibrates at a higher frequency",
            "The pitch becomes much deeper like thunder",
            "The sound disappears and turns into electricity",
            "The pitch remains completely unchanged"
        ],
        "answer": 0,
        "explanation": "Higher tension increases the restoring force of the rubber band, causing it to oscillate more cycles per second (higher frequency/pitch).",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Tension and Acoustic Frequency:</strong></p>
                <p class='text-slate-300'>Frequency (f) is directly proportional to the square root of tension. Greater tension = faster oscillations = higher frequency = higher perceived pitch.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Pitch becomes higher)</p>
            </div>
        """
    },
    {
        "id": 6,
        "question": "What is the role of the hollow cardboard shoebox in the rubber band guitar experiment?",
        "options": [
            "It acts as a resonance chamber that amplifies the vibrating sound waves",
            "It absorbs all sound so nobody can hear it",
            "It generates electricity to power a speaker",
            "It prevents the rubber band from stretching"
        ],
        "answer": 0,
        "explanation": "The hollow box vibrates sympathetically with the plucked rubber band, forcing a larger volume of enclosed air to oscillate and amplifying the volume.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Resonance and Acoustic Amplification:</strong></p>
                <p class='text-slate-300'>The wooden body of an acoustic guitar, sitar, or cardboard shoebox provides a large surface area that couples vibrational energy efficiently into surrounding air.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Resonance chamber that amplifies sound)</p>
            </div>
        """
    },
    {
        "id": 7,
        "question": "What happens at the molecular level when a bowl of water absorbs radiant solar energy on a sunny terrace?",
        "options": [
            "Water molecules absorb radiant energy and jiggle faster, raising the water temperature",
            "Water molecules stop moving and freeze into ice",
            "Water splits into solid gold bars",
            "Water molecules lose all mass"
        ],
        "answer": 0,
        "explanation": "Radiant solar photons excite the kinetic motion of water molecules, increasing the average internal kinetic energy (temperature).",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Thermal Physics of Solar Absorption:</strong></p>
                <p class='text-slate-300'>Temperature is the direct microscopic measure of molecular kinetic energy. Absorbing electromagnetic radiation converts radiant energy into thermal molecular vibration.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Molecules jiggle faster, raising temperature)</p>
            </div>
        """
    },
    {
        "id": 8,
        "question": "Why does black-painted metal absorb radiant solar heat significantly faster than polished white metal?",
        "options": [
            "Black surfaces absorb nearly all incoming solar wavelengths rather than reflecting them",
            "Black paint contains tiny electric batteries",
            "Black metal is much lighter in weight",
            "White paint absorbs radio waves"
        ],
        "answer": 0,
        "explanation": "Dark, non-reflective surfaces absorb nearly 95% of incident electromagnetic radiation, whereas white surfaces reflect most visible light back into space.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Albedo and Radiant Absorption:</strong></p>
                <p class='text-slate-300'>White objects have high albedo (reflectance); black objects have low albedo and high emissivity, maximizing solar thermal conversion.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Black surfaces absorb nearly all incoming solar wavelengths)</p>
            </div>
        """
    },
    {
        "id": 9,
        "question": "What fundamental law of physics states that energy can neither be created nor destroyed, only transformed?",
        "options": [
            "The Law of Conservation of Energy",
            "The Law of Magnetic Gravity",
            "The Law of Floating Objects",
            "The Law of Sound Speed"
        ],
        "answer": 0,
        "explanation": "The First Law of Thermodynamics (Law of Conservation of Energy) establishes that the total energy of an isolated system remains constant.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Law of Conservation of Energy:</strong></p>
                <p class='text-slate-300'>Energy can change forms (e.g. chemical to mechanical, electrical to light), but the total amount of energy in the universe is immutable.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (The Law of Conservation of Energy)</p>
            </div>
        """
    },
    {
        "id": 10,
        "question": "Which of the following is an example of kinetic energy in daily life?",
        "options": [
            "A fast-flowing mountain river carrying pebbles downstream",
            "A rock resting motionless on top of a hill",
            "A charged battery kept inside a drawer",
            "A lump of coal stored in a sack"
        ],
        "answer": 0,
        "explanation": "Kinetic energy is the energy possessed by an object due to its motion. A flowing river is in active motion, possessing kinetic energy.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Kinetic Energy vs Potential Energy:</strong></p>
                <p class='text-slate-300'>Kinetic energy is energy of motion (E = 0.5 * m * v²). Moving water, flying birds, and rolling balls possess kinetic energy.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (A fast-flowing mountain river)</p>
            </div>
        """
    },

    # Challenge 2 (Q11 to Q20): Slides 5 to 8 Concepts
    {
        "id": 11,
        "question": "What primary form of energy is stored inside food items like rotis, rice, dal, and bananas?",
        "options": [
            "Chemical potential energy",
            "High-voltage electrical energy",
            "Nuclear radioactive energy",
            "Magnetic rotational energy"
        ],
        "answer": 0,
        "explanation": "Food stores chemical potential energy within the chemical bonds of glucose, starches, fats, and proteins synthesized by plants.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Chemical Energy in Biological Nutrition:</strong></p>
                <p class='text-slate-300'>Photosynthesis converts radiant solar energy into chemical bond energy in carbohydrates (C6H12O6), which cellular respiration unlocks.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Chemical potential energy)</p>
            </div>
        """
    },
    {
        "id": 12,
        "question": "How does the human body function like a rechargeable battery regarding energy storage?",
        "options": [
            "It stores surplus energy from food as glycogen in the liver/muscles and fat tissue to supply steady energy later",
            "It must be plugged into a 220V wall socket overnight",
            "It runs on liquid petrol poured into the ears",
            "It has positive and negative copper terminals on the hands"
        ],
        "answer": 0,
        "explanation": "The human body stores excess dietary glucose as glycogen in liver and muscle cells, and lipids in adipose tissue, releasing it during fasting or exertion.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Biological Glycogen & Fat Storage:</strong></p>
                <p class='text-slate-300'>When blood glucose rises, insulin stimulates glycogen synthesis. Between meals, glucagon converts glycogen back to glucose, sustaining energy.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Stores surplus energy from food as glycogen and fat)</p>
            </div>
        """
    },
    {
        "id": 13,
        "question": "What is the primary definition of a 'fuel' in science and engineering?",
        "options": [
            "Any substance that releases useful thermal energy when burned with oxygen",
            "Any liquid that freezes below zero degrees",
            "A metal that conducts electricity without resistance",
            "A type of rock that repels water"
        ],
        "answer": 0,
        "explanation": "A fuel is a combustible substance containing concentrated chemical energy that produces heat and expanding gases upon oxidation.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Combustion Chemistry of Fuels:</strong></p>
                <p class='text-slate-300'>Fuel + Oxygen -> Carbon Dioxide + Water + Intense Heat (Thermal Energy). This released heat powers engines, turbines, and cooking stoves.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Releases useful thermal energy when burned with oxygen)</p>
            </div>
        """
    },
    {
        "id": 14,
        "question": "What fossil fuel is stored under high pressure in red domestic kitchen cylinders across India?",
        "options": [
            "LPG (Liquefied Petroleum Gas)",
            "Liquid Nitrogen",
            "Solid Coal Dust",
            "Uranium Oxide"
        ],
        "answer": 0,
        "explanation": "LPG, primarily consisting of propane and butane compressed into a liquid state, powers domestic kitchen gas burners cleanly and instantly.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Domestic LPG Gas:</strong></p>
                <p class='text-slate-300'>LPG burns with a hot, soot-free blue flame when mixed with appropriate oxygen, producing far less indoor smoke than traditional firewood or dung cakes.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (LPG - Liquefied Petroleum Gas)</p>
            </div>
        """
    },
    {
        "id": 15,
        "question": "How does an internal combustion engine inside a bus convert chemical fuel into wheel rotation?",
        "options": [
            "Burning fuel produces hot expanding gases that push metal pistons downward, turning the crankshaft and wheels",
            "Fuel dissolves the rubber tires so they roll faster",
            "Fuel turns into steam that pulls the vehicle magnetically",
            "The engine freezes the fuel into solid carbon gears"
        ],
        "answer": 0,
        "explanation": "The rapid expansion of hot combustion gases in the engine cylinder forces the piston down, converting linear thrust into rotary motion.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Internal Combustion Cycle:</strong></p>
                <p class='text-slate-300'>Intake -> Compression -> Power (Ignition & Expansion pushing Piston) -> Exhaust. The mechanical connecting rod converts reciprocating piston motion into continuous shaft rotation.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Burning fuel produces hot expanding gases pushing pistons)</p>
            </div>
        """
    },
    {
        "id": 16,
        "question": "By what scientific mechanism does oil climb from the clay reservoir up to the tip of a cotton diya wick?",
        "options": [
            "Capillary action through microscopic spaces between twisted cotton fibres",
            "Gravitational pull from the moon",
            "Electrical conduction along copper threads",
            "Evaporation into the clouds"
        ],
        "answer": 0,
        "explanation": "Capillary action draws liquid oil upward against gravity due to adhesive forces between oil molecules and cellulose fibers.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Capillary Action in Wicks:</strong></p>
                <p class='text-slate-300'>Narrow pores between cotton fibres create high surface tension capillary forces that draw liquid oil upward, maintaining a continuous fuel feed.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Capillary action through microscopic spaces)</p>
            </div>
        """
    },
    {
        "id": 17,
        "question": "In a burning diya or candle, what is actually burning to produce the luminous golden flame?",
        "options": [
            "Hot oil or wax vapor reacting with oxygen at the tip",
            "The solid cotton thread itself",
            "The earthen clay bowl",
            "The nitrogen gas in the room"
        ],
        "answer": 0,
        "explanation": "The flame's heat vaporizes ascending liquid oil into hydrocarbon gas, which mixes with ambient oxygen and combusts with a bright flame.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Vapor Phase Combustion:</strong></p>
                <p class='text-slate-300'>Liquids and solids do not burn directly; they must first be volatilized into vapor. The cotton wick merely acts as a transport siphon and support structure.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Hot oil or wax vapor reacting with oxygen)</p>
            </div>
        """
    },
    {
        "id": 18,
        "question": "What is an electric current fundamentally composed of in a conductive circuit?",
        "options": [
            "The organized drift of negatively charged electrons through a conductor",
            "A stream of microscopic water droplets flowing inside cables",
            "A beam of radio waves traveling through the air",
            "Compressed air expanding inside copper tubes"
        ],
        "answer": 0,
        "explanation": "Electric current is the continuous movement of free conduction electrons propelled through metallic crystal lattices by an electric potential gradient.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Nature of Electric Current:</strong></p>
                <p class='text-slate-300'>Metals like copper possess a 'sea' of delocalized valence electrons. When a voltage is applied, electrons drift in unison, transferring electrical energy.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Organized drift of negatively charged electrons)</p>
            </div>
        """
    },
    {
        "id": 19,
        "question": "Which of the following household appliances converts electrical energy primarily into thermal heat?",
        "options": [
            "An electric clothes iron and room heater",
            "A ceiling fan",
            "A radio loudspeaker",
            "A battery torch"
        ],
        "answer": 0,
        "explanation": "An electric iron contains high-resistance nichrome heating elements that convert electrical current into intense thermal heat via Joule heating.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Joule Heating Effect:</strong></p>
                <p class='text-slate-300'>When electric current encounters resistance in a heating element (H = I² * R * t), electrical potential energy transforms into thermal energy.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (An electric clothes iron and room heater)</p>
            </div>
        """
    },
    {
        "id": 20,
        "question": "What happens immediately when an electrical switch is turned off in a home circuit?",
        "options": [
            "The circuit is broken open, stopping the flow of electrons instantly",
            "Electricity spills out of the wire onto the floor",
            "The appliance turns into a gas",
            "The voltage increases ten times"
        ],
        "answer": 0,
        "explanation": "Opening a switch creates an air gap in the circuit; because air is a powerful insulator, the electron loop is interrupted and current stops immediately.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Open Circuit vs Closed Circuit:</strong></p>
                <p class='text-slate-300'>Electrons can only flow through an unbroken, continuous conductive loop. An open switch breaks the continuity, terminating power delivery.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (The circuit is broken open, stopping flow of electrons)</p>
            </div>
        """
    },

    # Challenge 3 (Q21 to Q30): Slides 9 to 12 Concepts
    {
        "id": 21,
        "question": "Why does an old incandescent filament bulb become extremely hot to the touch after just a few minutes?",
        "options": [
            "Because nearly 90% of the electrical energy is wasted as heat, with only 10% emitted as light",
            "Because the glass reacts chemically with air",
            "Because the light bulb produces nuclear fire",
            "Because the wire absorbs cold from the room"
        ],
        "answer": 0,
        "explanation": "Tungsten filaments require extreme temperatures (>2,500°C) to glow (incandesce), wasting approximately 90% of incoming electricity as infrared heat.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Incandescence Inefficiency:</strong></p>
                <p class='text-slate-300'>Incandescent bulbs produce light as an incidental byproduct of extreme thermal heating, making them notoriously inefficient energy converters.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Nearly 90% of electricity is wasted as heat)</p>
            </div>
        """
    },
    {
        "id": 22,
        "question": "How do modern solid-state LED bulbs generate bright light so efficiently without getting burning hot?",
        "options": [
            "Semiconductor chips release light photons directly through electronic electroluminescence",
            "They burn tiny drops of oil inside sealed glass",
            "They reflect sunlight stored from daytime",
            "They use miniature nuclear batteries"
        ],
        "answer": 0,
        "explanation": "LEDs produce cold light via semiconductor recombination, converting over 80% of electrical energy directly into visible light photons.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Electroluminescence in LEDs:</strong></p>
                <p class='text-slate-300'>In a p-n junction diode, electrons drop across the bandgap, shedding excess energy directly as light photons rather than random thermal vibrations.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Semiconductor chips release light photons directly)</p>
            </div>
        """
    },
    {
        "id": 23,
        "question": "Why does moisture or wet skin make handling electrical switches especially dangerous?",
        "options": [
            "Water containing dissolved salts drastically lowers skin electrical resistance, allowing lethal current to enter the body",
            "Water makes switches explode into dust",
            "Wet fingers attract lightning bolts from the clouds",
            "Water turns plastic switches into iron"
        ],
        "answer": 0,
        "explanation": "Dry human skin has high electrical resistance (~100,000 ohms), but wet skin with perspiration salts drops to below 1,000 ohms, permitting dangerous current flow.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Ohm's Law & Human Skin Resistance:</strong></p>
                <p class='text-slate-300'>Current I = V / R. When skin resistance (R) drops due to water and sweat, a standard 230V household supply can deliver lethal shocks (>50 mA).</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Water with salts drastically lowers skin resistance)</p>
            </div>
        """
    },
    {
        "id": 24,
        "question": "What material is coated over copper electrical wires to prevent shocks and short circuits?",
        "options": [
            "Flexible PVC plastic, which acts as a strong electrical insulator",
            "Aluminium foil, which attracts electrons",
            "Wet cotton string",
            "Saltwater jelly"
        ],
        "answer": 0,
        "explanation": "Polyvinyl chloride (PVC) plastic has tightly bound valence electrons that do not permit current flow, making it an ideal protective insulator.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Conductors vs Insulators:</strong></p>
                <p class='text-slate-300'>Copper cores provide low-resistance pathways for current, while exterior PVC insulation confines electrons safely within the circuit.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Flexible PVC plastic as an electrical insulator)</p>
            </div>
        """
    },
    {
        "id": 25,
        "question": "What does a Miniature Circuit Breaker (MCB) do during an accidental overload or short circuit?",
        "options": [
            "It automatically trips and opens the circuit, halting dangerous current flow before a fire starts",
            "It blows air to cool down the house",
            "It doubles the electricity to overcome the problem",
            "It rings an alarm and plays recorded music"
        ],
        "answer": 0,
        "explanation": "MCBs utilize thermal bimetallic strips and electromagnetic coils to automatically trip open within milliseconds when current exceeds safe operating thresholds.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Modern Circuit Breaker Protection:</strong></p>
                <p class='text-slate-300'>MCBs replaced old sacrificial fuse wires because they can be easily reset with a toggle switch once the electrical fault is cleared.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Automatically trips and opens the circuit)</p>
            </div>
        """
    },
    {
        "id": 26,
        "question": "What toxic environmental emissions are released when coal is burned in thermal power stations?",
        "options": [
            "Soot (PM2.5), sulfur dioxide, nitrogen oxides, and greenhouse carbon dioxide",
            "Clean pure oxygen gas",
            "Fresh drinking water drops",
            "Fragrant flower perfume"
        ],
        "answer": 0,
        "explanation": "Burning coal releases heavy greenhouse gases, acid-rain causing sulfur oxides, and particulate matter that trigger severe lung and heart illnesses.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Thermal Power Environmental Impact:</strong></p>
                <p class='text-slate-300'>Coal combustion produces ash slurry containing toxic heavy metals (mercury, arsenic, lead) and massive greenhouse emissions driving global warming.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Soot, sulfur dioxide, nitrogen oxides, and carbon dioxide)</p>
            </div>
        """
    },
    {
        "id": 27,
        "question": "Why are solar, wind, and water energy called 'renewable' sources of energy?",
        "options": [
            "Because natural planetary processes constantly replenish them and they will never run out",
            "Because they must be replaced by new machines every week",
            "Because they are made from recycled plastic bags",
            "Because they can only be used during rainy seasons"
        ],
        "answer": 0,
        "explanation": "Unlike finite fossil fuels that take millions of years to form, solar radiation, atmospheric winds, and hydrological river cycles replenish perpetually.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Renewable Energy Sustainability:</strong></p>
                <p class='text-slate-300'>The Sun will radiate energy for another 5 billion years; its thermal gradient drives winds and rain cycles continuously without depleting resource stocks.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Naturally replenished and will never run out)</p>
            </div>
        """
    },
    {
        "id": 28,
        "question": "In the paper pinwheel experiment (Activity 6), what forces the curved blades to spin?",
        "options": [
            "Moving air molecules transferring their kinetic energy and exerting pressure against the angled blades",
            "Static electricity in the pushpin",
            "Thermal heat melting the paper",
            "Magnetic fields from the wooden pencil"
        ],
        "answer": 0,
        "explanation": "Air in motion possesses kinetic energy. As moving air strikes the angled paper flaps, an aerodynamic pressure differential generates rotational torque.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Aerodynamics of Pinwheel Rotors:</strong></p>
                <p class='text-slate-300'>The cupped geometry creates high pressure on the concave face and lower pressure behind it, producing unbalanced forces that spin the rotor.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Moving air molecules transferring kinetic energy)</p>
            </div>
        """
    },
    {
        "id": 29,
        "question": "What is the ultimate origin of all wind on planet Earth?",
        "options": [
            "The Sun heating the Earth's surface and atmosphere unevenly",
            "Ocean waves pushing air from underneath",
            "Trees waving their branches simultaneously",
            "Automobiles driving on highways"
        ],
        "answer": 0,
        "explanation": "The equator receives more direct solar radiation than the poles, creating atmospheric temperature and pressure differences that drive global wind circulation.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Solar Origin of Wind Energy:</strong></p>
                <p class='text-slate-300'>Warm air at the equator expands and rises, creating low pressure. Cooler, denser polar air flows in to replace it, creating perpetual planetary wind currents.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (The Sun heating the Earth's surface unevenly)</p>
            </div>
        """
    },
    {
        "id": 30,
        "question": "How do modern utility wind turbines generate electricity from passing coastal breezes?",
        "options": [
            "Aerodynamic rotor blades rotate a central shaft connected to an electromagnetic generator",
            "They capture wind in plastic sacks to burn later",
            "They bounce sunlight onto electric solar panels",
            "They use wind to pump diesel fuel into trucks"
        ],
        "answer": 0,
        "explanation": "Aerodynamic lift spins the rotor blades (10-20 rpm), which a gearbox speeds up to ~1,500 rpm to drive an induction generator producing electricity.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Wind Turbine Electromechanics:</strong></p>
                <p class='text-slate-300'>Wind Kinetic Energy -> Rotor Shaft Mechanical Energy -> Generator Electromagnetic Energy -> High Voltage Grid AC Current.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Rotor blades rotate a shaft connected to an electric generator)</p>
            </div>
        """
    },

    # Challenge 4 (Q31 to Q40): Slides 13 to 16 Concepts
    {
        "id": 31,
        "question": "In Activity 7, what optical phenomenon allows a magnifying glass to focus scattered sunlight onto a single hot spot?",
        "options": [
            "Refraction (bending) of light rays passing through a curved convex glass lens",
            "Reflection from a flat mirror surface",
            "Complete absorption of all light into the glass",
            "Diffraction through a razor blade"
        ],
        "answer": 0,
        "explanation": "A convex lens is thicker in the center, causing parallel light rays to refract (bend inward) toward a single concentrated focal point.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Convex Lens Refraction & Focal Point:</strong></p>
                <p class='text-slate-300'>Light travels slower in glass than in air. The curved glass curvature slows the perimeter of the light wave differently, bending all rays into focus.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Refraction of light rays through a convex lens)</p>
            </div>
        """
    },
    {
        "id": 32,
        "question": "What practical clean cooking technology utilizes concentrated solar radiation without gas or electricity?",
        "options": [
            "A parabolic solar cooker",
            "A kerosene pressure stove",
            "A diesel camping burner",
            "A coal-fired tandoor"
        ],
        "answer": 0,
        "explanation": "Solar cookers use shiny curved parabolic reflectors or insulated glass boxes to concentrate sunlight, heating cooking pots to over 150°C.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Solar Thermal Cooking:</strong></p>
                <p class='text-slate-300'>Curved mirrors focus sunlight rays onto a black cooking pot, cooking rice, dal, and vegetables purely through free, zero-pollution solar thermal energy.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (A parabolic solar cooker)</p>
            </div>
        """
    },
    {
        "id": 33,
        "question": "In the homemade water wheel experiment (Activity 8), what enables falling water to lift a suspended weight?",
        "options": [
            "Falling water transfers its kinetic energy to the paddles, producing axle rotation that winds up the thread",
            "Water turns the string into an electric wire",
            "The weight floats upward because it smells the water",
            "The cardboard pillar pulls the string magnetically"
        ],
        "answer": 0,
        "explanation": "Falling water transfers momentum to the cups, turning the axle. The rotating axle provides mechanical shaft work that reels up the suspended weight.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Mechanical Work from Hydraulic Energy:</strong></p>
                <p class='text-slate-300'>Work = Force * Distance. The gravitational potential energy of falling water translates into torque, lifting the load against gravity.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Falling water transfers kinetic energy to paddles, producing rotation)</p>
            </div>
        """
    },
    {
        "id": 34,
        "question": "What is a traditional Himalayan 'Gharaat'?",
        "options": [
            "An indigenous watermill powered by diverted mountain streams to grind grain into flour without electricity",
            "A diesel-powered tractor used on snow slopes",
            "A stone bridge built across dry rivers",
            "A wooden boat used for ocean fishing"
        ],
        "answer": 0,
        "explanation": "A Gharaat is an ancient Himalayan hydraulic watermill where rushing glacier torrents strike wooden turbine blades to spin heavy stone grain mills.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Himalayan Gharaat Heritage:</strong></p>
                <p class='text-slate-300'>Gharaats have operated across the Himalayas for centuries, grinding wheat, corn, and barley cleanly with zero fossil fuels or greenhouse emissions.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Indigenous watermill powered by mountain streams)</p>
            </div>
        """
    },
    {
        "id": 35,
        "question": "Why does stone-milled flour from a traditional Gharaat have superior nutritional value compared to fast industrial electric mills?",
        "options": [
            "Cold stone grinding keeps temperatures low, preserving sensitive vitamins and natural wheat-germ oils",
            "The stone injects chemical preservatives into the flour",
            "The water adds sugar to the grain",
            "The stone bleaches the wheat white"
        ],
        "answer": 0,
        "explanation": "High-speed electric roller mills generate friction heat exceeding 90°C that degrades wheat-germ oils and vitamins. Cool Gharaat stone milling preserves nutrients.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Nutritional Benefits of Cold Milling:</strong></p>
                <p class='text-slate-300'>Gharaat milling preserves heat-sensitive vitamins (thiamine, vitamin E) and prevents the oxidation of essential fatty acids present in the grain germ.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Cold stone grinding preserves vitamins and wheat-germ oils)</p>
            </div>
        """
    },
    {
        "id": 36,
        "question": "How did ancient merchant ships cross vast oceans before the invention of steam and diesel engines?",
        "options": [
            "They hoisted large fabric sails that captured the kinetic energy of trade winds to push the ship forward",
            "They plugged extension cords into coastal lighthouses",
            "They used giant underwater electric propellers",
            "They waited for ocean water to flow downhill"
        ],
        "answer": 0,
        "explanation": "Sailing ships utilized expansive canvas sails to harness the aerodynamic thrust of prevailing ocean trade winds, navigating thousands of nautical miles.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Historical Wind Navigation:</strong></p>
                <p class='text-slate-300'>Indian maritime trade across the Arabian Sea and Bay of Bengal relied on seasonal monsoon winds to propel wooden dhows and sailing craft.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Hoisting large fabric sails to capture kinetic wind energy)</p>
            </div>
        """
    },
    {
        "id": 37,
        "question": "What is 'phantom power draw' (or vampire power) in domestic household electricity?",
        "options": [
            "Electricity continuously consumed by electronic appliances left in standby mode or plugged-in chargers",
            "Electricity stolen by ghosts in old houses",
            "Power generated by lightning striking rooftop antennas",
            "A magnetic surge that makes lights turn purple"
        ],
        "answer": 0,
        "explanation": "Appliances like TVs, microwaves, game consoles, and phone chargers consume electrical power even when switched off if their plugs remain energized.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Standby Power Consumption:</strong></p>
                <p class='text-slate-300'>Standby power accounts for up to 10% of total residential electricity bills. Turning off wall switches completely stops this unnecessary drain.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Electricity consumed by appliances left in standby mode)</p>
            </div>
        """
    },
    {
        "id": 38,
        "question": "What certification label on Indian household appliances indicates superior electrical energy efficiency?",
        "options": [
            "BEE Star Rating Label (Bureau of Energy Efficiency, 1 to 5 Stars)",
            "A plastic red danger triangle",
            "A diamond warranty sticker",
            "A golden medal ribbon"
        ],
        "answer": 0,
        "explanation": "The Bureau of Energy Efficiency (BEE) rates refrigerators, air conditioners, and fans from 1 to 5 stars; 5-star models consume the least electricity.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>BEE Star Rating Standards:</strong></p>
                <p class='text-slate-300'>A 5-star inverter air conditioner or refrigerator uses advanced variable-speed compressors, saving up to 30% more power than a 1-star appliance.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (BEE Star Rating Label from 1 to 5 Stars)</p>
            </div>
        """
    },
    {
        "id": 39,
        "question": "Why is drying washed clothes outdoors on a sunny clothesline scientifically wiser than using an electric tumble dryer?",
        "options": [
            "It utilizes free, zero-emission solar radiant and wind energy instead of consuming high-wattage electricity from coal power plants",
            "It makes clothes turn completely transparent",
            "It takes three weeks for clothes to dry",
            "It shrinks clothes to half their size"
        ],
        "answer": 0,
        "explanation": "Solar drying uses natural radiant heat and ambient air circulation to evaporate moisture cleanly, while ultraviolet sunlight naturally disinfects fabrics.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Natural Solar Dehydration:</strong></p>
                <p class='text-slate-300'>Electric tumble dryers consume 2,000 to 4,000 watts per load. Sun drying eliminates this energy footprint and utilizes solar UV rays to kill microbes.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Utilizes free, zero-emission solar and wind energy)</p>
            </div>
        """
    },
    {
        "id": 40,
        "question": "What overarching message does Chapter 7 convey about humanity's relationship with energy?",
        "options": [
            "Energy is essential for all life and progress; by embracing clean renewables and active conservation, we secure a prosperous, green planet",
            "Humans should stop moving and stay motionless to save energy",
            "We should burn all remaining coal as fast as possible",
            "Only batteries can provide real energy"
        ],
        "answer": 0,
        "explanation": "Energy drives all living systems and modern society. Shifting to renewable sources and practicing daily conservation ensures sustainable planetary survival.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>The Sustainable Energy Paradigm:</strong></p>
                <p class='text-slate-300'>Understanding how energy transforms empowers students to become proactive ecological stewards who champion solar, wind, and mindful energy habits.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Embracing clean renewables and active conservation secures a green planet)</p>
            </div>
        """
    }
]

print("Mastery quiz questions defined:", len(QUIZ_QUESTIONS))

