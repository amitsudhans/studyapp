# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 10: The Human Eye and the Colourful World
Part 3: Slides 17 to 20 Generator (40 Comprehensive Challenge Questions)
Strictly silent (speech = ""). Titles strictly 1-3 words. Zero persona titles or forbidden names.
"""

import json

slides_part3 = [
    {
        "id": 17,
        "title": "Eye Vision Review",
        "subtitle": "Anatomy, Accommodation, and Vision Defects Mastery",
        "badge": "Review Set 1",
        "speech": "",
        "theory": """
            <div class="space-y-2 text-slate-300 text-xs leading-relaxed">
                <p><strong class="text-amber-400">Section Focus:</strong> Review of human eye anatomy, pupil aperture reflexes, crystalline lens accommodation, myopia, hypermetropia, and presbyopia.</p>
            </div>
        """,
        "questions": [
            {
                "id": "c10_q1",
                "question": "Which transparent front membrane of the human eye provides approximately 80% of total light refraction?",
                "options": ["Cornea", "Crystalline lens", "Pupil", "Retina"],
                "answer": 0,
                "hint": "Identify the convex anterior bulge where light transitions from air into biological tissue.",
                "explanation": "The outer curved surface of the cornea accounts for the majority of the eye's total refractive optical power.",
                "steps": [
                    "Step 1: Recall the optical boundary between atmospheric air (n ≈ 1.0) and corneal tissue (n ≈ 1.376).",
                    "Step 2: The large refractive index difference at the corneal surface produces approximately 40 to 45 dioptres of converging power.",
                    "Step 3: Therefore, the cornea performs about 80% of total ocular light refraction."
                ]
            },
            {
                "id": "c10_q2",
                "question": "What is the primary optical role of the iris in the human eye?",
                "options": [
                    "Regulating the diameter of the pupil to control entering light flux",
                    "Providing fine dynamic adjustment of crystalline focal length",
                    "Transducing incident photons into electrical impulses",
                    "Maintaining intraocular fluid pressure in the vitreous humor"
                ],
                "answer": 0,
                "hint": "Think of the iris as the adjustable camera diaphragm.",
                "explanation": "The iris is a pigmented muscular diaphragm whose circular and radial muscles adjust the pupil aperture.",
                "steps": [
                    "Step 1: The iris is positioned between the cornea and crystalline lens.",
                    "Step 2: Its muscular contractions constrict or dilate the central aperture known as the pupil.",
                    "Step 3: This modulates the amount of light entering the interior eye chamber according to ambient brightness."
                ]
            },
            {
                "id": "c10_q3",
                "question": "What is the least distance of distinct vision (near point) for a healthy young adult eye?",
                "options": ["25 cm", "2.5 cm", "50 cm", "Infinity"],
                "answer": 0,
                "hint": "Recall the standard reading distance benchmark in NCERT Section 10.1.1.",
                "explanation": "For a normal young adult eye, the near point is approximately 25 cm. Objects held closer cause strain on the ciliary muscles.",
                "steps": [
                    "Step 1: The near point represents the minimum distance at which an object can be seen distinctly without eyestrain.",
                    "Step 2: Ciliary muscles contract maximally to achieve maximum lens convexity at this focal limit.",
                    "Step 3: In a healthy young adult, this distance equals exactly 25 cm."
                ]
            },
            {
                "id": "c10_q4",
                "question": "During distant object viewing, what state are the ciliary muscles in?",
                "options": [
                    "Completely relaxed, stretching the lens thin",
                    "Maximally contracted, making the lens thick",
                    "Rapidly oscillating between states",
                    "Detached from suspensory ligaments"
                ],
                "answer": 0,
                "hint": "Consider how the eye rests when looking at distant mountains or stars.",
                "explanation": "For distant vision, ciliary muscles relax, increasing tension on suspensory ligaments and stretching the crystalline lens into a thin, long-focal-length profile.",
                "steps": [
                    "Step 1: When gazing at distant objects, parallel rays enter the pupil.",
                    "Step 2: Ciliary muscles relax, pulling suspensory zonules taut.",
                    "Step 3: The lens becomes thin with maximum focal length (~2.27 cm), focusing rays effortlessly on the retina."
                ]
            },
            {
                "id": "c10_q5",
                "question": "Where does the image of a distant object form in an uncorrected myopic eye?",
                "options": [
                    "In front of the retina",
                    "Behind the retina",
                    "Directly on the fovea centralis",
                    "Within the corneal stroma"
                ],
                "answer": 0,
                "hint": "Myopia involves over-convergence or an elongated eyeball.",
                "explanation": "In myopia, parallel rays converge prematurely in front of the retina, causing distant objects to appear blurry.",
                "steps": [
                    "Step 1: In a myopic eye, the eyeball is elongated or the lens curvature is excessively steep.",
                    "Step 2: Parallel incident rays from infinity undergo excessive convergence.",
                    "Step 3: The focused image is formed in front of the retina, resulting in blurred distance vision."
                ]
            },
            {
                "id": "c10_q6",
                "question": "A student cannot see the blackboard clearly from a distance of 4 metres. Which lens corrects this defect?",
                "options": [
                    "Concave lens of power -0.25 D",
                    "Convex lens of power +0.25 D",
                    "Concave lens of power -4.0 D",
                    "Convex lens of power +4.0 D"
                ],
                "answer": 0,
                "hint": "Apply the lens formula with u = -∞ and v = -4 m.",
                "explanation": "The student has myopia with a far point of 4 m. A concave lens with focal length f = -4 m gives power P = 1/(-4) = -0.25 D.",
                "steps": [
                    "Step 1: Identify the myopic far point d = 4 m. To view distant objects, u = -∞ and v = -4 m.",
                    "Step 2: Apply the lens formula: 1/f = 1/v - 1/u = 1/(-4) - 0 = -1/4 m⁻¹, so f = -4 m.",
                    "Step 3: Calculate dioptric power: P = 1/f = 1/(-4) = -0.25 D (a concave lens)."
                ]
            },
            {
                "id": "c10_q7",
                "question": "Where does the image of a nearby reading source form in an uncorrected hypermetropic eye?",
                "options": [
                    "Behind the retina",
                    "In front of the retina",
                    "Directly on the optic disk",
                    "Inside the crystalline lens"
                ],
                "answer": 0,
                "hint": "Hypermetropia involves under-convergence or a shortened eyeball.",
                "explanation": "In hypermetropia, light rays from near objects have insufficient convergence and focus behind the retina.",
                "steps": [
                    "Step 1: Hypermetropic eyes possess a short eyeball or a lens with too long a focal length.",
                    "Step 2: Diverging rays from an object at 25 cm cannot be sufficiently converged by the eye lens.",
                    "Step 3: Rays project their focus behind the retina, producing a blurred retinal image."
                ]
            },
            {
                "id": "c10_q8",
                "question": "A person's near point has receded to 1 metre. What power convex lens is needed to read at 25 cm?",
                "options": ["+3.0 D", "+4.0 D", "-3.0 D", "+1.0 D"],
                "answer": 0,
                "hint": "Use 1/f = 1/v - 1/u with u = -25 cm = -0.25 m and v = -1 m.",
                "explanation": "The corrective lens must form a virtual image of the object at 25 cm at the receded near point of -100 cm. 1/f = 1/(-1) - 1/(-0.25) = -1 + 4 = +3 D.",
                "steps": [
                    "Step 1: Object distance u = -0.25 m; desired virtual image distance v = -1.0 m.",
                    "Step 2: Lens formula: 1/f = 1/v - 1/u = 1/(-1.0) - 1/(-0.25) = -1 + 4 = +3 m⁻¹.",
                    "Step 3: Optical power P = 1/f = +3.0 D (converging convex lens)."
                ]
            },
            {
                "id": "c10_q9",
                "question": "Why do elderly individuals develop presbyopia?",
                "options": [
                    "Weakening of ciliary muscles and diminishing lens elasticity",
                    "Complete elongation of the optical eyeball",
                    "Loss of photoreceptor rods on the retina",
                    "Accumulation of excess aqueous humor fluid"
                ],
                "answer": 0,
                "hint": "Consider the aging changes affecting the ciliary ring and lens protein flexibility.",
                "explanation": "Presbyopia is caused by the gradual weakening of ciliary muscles and reduced flexibility of the crystalline lens.",
                "steps": [
                    "Step 1: Aging causes crystalline lens proteins to become progressively less pliable.",
                    "Step 2: Concurrently, the circular ciliary muscles undergo gradual loss of contractile strength.",
                    "Step 3: The lens cannot bulge sufficiently to focus on nearby objects, causing presbyopia."
                ]
            },
            {
                "id": "c10_q10",
                "question": "In a traditional bi-focal spectacle lens, what are the upper and lower portions composed of?",
                "options": [
                    "Upper concave for distance vision; lower convex for reading",
                    "Upper convex for reading; lower concave for distance vision",
                    "Both upper and lower are identical concave lenses",
                    "Both upper and lower are identical convex lenses"
                ],
                "answer": 0,
                "hint": "Consider how you angle your head and gaze when looking at the horizon versus reading a book.",
                "explanation": "The upper part is a concave lens to correct myopia (distance vision), while the lower part is a convex lens to correct presbyopia (reading).",
                "steps": [
                    "Step 1: Straight-ahead gaze is used for distant viewing, requiring a diverging concave lens.",
                    "Step 2: Downward gaze is used for near reading, requiring a converging convex lens.",
                    "Step 3: A bi-focal integrates an upper concave lens and a lower convex lens in a single frame."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Prism Dispersion Review",
        "subtitle": "Refraction Geometry, Angle of Deviation, and Spectrum Synthesis",
        "badge": "Review Set 2",
        "speech": "",
        "theory": """
            <div class="space-y-2 text-slate-300 text-xs leading-relaxed">
                <p><strong class="text-amber-400">Section Focus:</strong> Review of triangular prism optics, angle of prism, angle of deviation, dispersion into VIBGYOR, Newton's inverted prism recombination, and rainbow physics.</p>
            </div>
        """,
        "questions": [
            {
                "id": "c10_q11",
                "question": "What is the angle between the two lateral refracting surfaces of a triangular prism called?",
                "options": ["Angle of the prism", "Angle of deviation", "Angle of emergence", "Critical angle"],
                "answer": 0,
                "hint": "Denoted by capital letter A in optical prism diagrams.",
                "explanation": "The angle between the two inclined lateral refracting surfaces of a prism is termed the angle of the prism (A).",
                "steps": [
                    "Step 1: A triangular prism has two triangular end faces and three rectangular lateral faces.",
                    "Step 2: Light enters one lateral face and emerges through an adjacent lateral face.",
                    "Step 3: The dihedral angle between these two refracting faces is defined as the angle of the prism (A)."
                ]
            },
            {
                "id": "c10_q12",
                "question": "Which relation correctly connects the angles involved in refraction through a triangular prism?",
                "options": ["i + e = A + D", "i + A = e + D", "i - e = A - D", "i × e = A × D"],
                "answer": 0,
                "hint": "Recall the fundamental geometric sum theorem established in NCERT Section 10.3.",
                "explanation": "For any triangular prism, the sum of incidence angle (i) and emergence angle (e) equals the sum of prism angle (A) and deviation angle (D).",
                "steps": [
                    "Step 1: In the quadrilateral formed by prism normals, opposite angles sum to 180°.",
                    "Step 2: Within the ray refraction triangle, r₁ + r₂ = A.",
                    "Step 3: Summing the deviation at both surfaces yields D = (i - r₁) + (e - r₂) = i + e - A, giving i + e = A + D."
                ]
            },
            {
                "id": "c10_q13",
                "question": "When white light undergoes dispersion through a glass prism, which color is deviated the most?",
                "options": ["Violet", "Red", "Green", "Yellow"],
                "answer": 0,
                "hint": "Identify the color with the shortest visible wavelength and lowest speed in glass.",
                "explanation": "Violet light has the shortest wavelength, travels slowest in glass, has the highest refractive index, and deviates the most.",
                "steps": [
                    "Step 1: Speed in glass v = c/n, where n is inversely related to wavelength (Cauchy's relation).",
                    "Step 2: Violet light has the shortest wavelength (~400 nm), giving it the largest refractive index in glass.",
                    "Step 3: A larger refractive index produces greater refraction and the maximum angle of deviation."
                ]
            },
            {
                "id": "c10_q14",
                "question": "Which color of visible light travels fastest inside a dense glass prism?",
                "options": ["Red", "Violet", "Blue", "Indigo"],
                "answer": 0,
                "hint": "Consider the visible wavelength that encounters the lowest refractive index.",
                "explanation": "Red light has the longest wavelength, encounters the smallest refractive index, and travels fastest in optical glass.",
                "steps": [
                    "Step 1: Wavelength of red light is ~700 nm, the longest in the visible spectrum.",
                    "Step 2: In glass, refractive index n(red) < n(violet).",
                    "Step 3: Since v = c/n, a smaller n results in the highest propagation speed for red light."
                ]
            },
            {
                "id": "c10_q15",
                "question": "How did Isaac Newton prove that white sunlight consists of seven constituent colors?",
                "options": [
                    "By recombining the spectrum into white light using a second inverted prism",
                    "By reflecting the spectrum off a concave spherical mirror",
                    "By filtering the light through a beaker of pure alcohol",
                    "By heating the prism to high temperature"
                ],
                "answer": 0,
                "hint": "Newton used two identical prisms in opposite orientations.",
                "explanation": "Newton placed a second identical prism inverted behind the first prism, reversing the dispersion and producing white light.",
                "steps": [
                    "Step 1: The first upright prism dispersed sunlight into the VIBGYOR spectrum.",
                    "Step 2: An identical inverted prism introduced equal and opposite angular deviations to all rays.",
                    "Step 3: The emerging recombined beam was pure white light, proving sunlight contains all seven colors."
                ]
            },
            {
                "id": "c10_q16",
                "question": "What is the critical angle condition required for internal reflection inside a raindrop during rainbow formation?",
                "options": [
                    "Angle of incidence on the back inner surface must exceed the critical angle",
                    "Angle of incidence must be exactly zero degrees",
                    "Water must be completely frozen into solid ice crystals",
                    "The droplet must have a cubical crystalline geometry"
                ],
                "answer": 0,
                "hint": "Total internal reflection occurs when incident angle exceeds the critical angle.",
                "explanation": "Dispersed light striking the back inner water-air interface at an angle greater than water's critical angle (~48.6°) undergoes internal reflection.",
                "steps": [
                    "Step 1: Light refracts into the spherical drop and strikes the back inner surface.",
                    "Step 2: For rainbow-forming rays, the incidence angle exceeds the critical angle of water (≈ 48.6°).",
                    "Step 3: This causes the light to reflect internally rather than escape out the back of the droplet."
                ]
            },
            {
                "id": "c10_q17",
                "question": "What is the approximate angular elevation of red light in a primary rainbow relative to incident solar rays?",
                "options": ["42°", "40°", "90°", "180°"],
                "answer": 0,
                "hint": "Red emerges slightly higher than violet (which emerges at 40°).",
                "explanation": "Red light emerges from raindrops at an angle of ~42°, forming the outer top border of the primary rainbow.",
                "steps": [
                    "Step 1: Ray tracing through spherical water drops yields an emergence cone.",
                    "Step 2: Red light emerges at an angle of 42° relative to incoming parallel sunlight.",
                    "Step 3: Violet light emerges at 40°, placing red along the uppermost arc of the primary rainbow."
                ]
            },
            {
                "id": "c10_q18",
                "question": "Under what condition can an observer see a natural rainbow in the sky?",
                "options": [
                    "The Sun is behind the observer while water droplets hang in front",
                    "The Sun is directly overhead at solar noon with clear skies",
                    "The observer faces directly towards the setting Sun",
                    "During a nighttime full moon without any raindrops"
                ],
                "answer": 0,
                "hint": "The observer's back must face the source of illumination.",
                "explanation": "A rainbow is always formed opposite to the Sun, so the observer must stand with the Sun behind them facing raindrops in front.",
                "steps": [
                    "Step 1: Raindrops reflect light back towards the source direction via internal reflection.",
                    "Step 2: Light emerging at 40° to 42° travels back toward the observer.",
                    "Step 3: Therefore, the observer must have their back to the Sun to intercept the reflected rainbow cone."
                ]
            },
            {
                "id": "c10_q19",
                "question": "Why does a rectangular glass slab not produce an angular spectrum like a triangular prism?",
                "options": [
                    "Its opposite faces are parallel, causing emergent rays to emerge parallel to incident rays",
                    "Glass in slabs has a constant zero refractive index",
                    "Light speed does not change in flat glass slabs",
                    "A rectangular slab absorbs all blue wavelengths completely"
                ],
                "answer": 0,
                "hint": "Consider the equal and opposite refractions at parallel surfaces.",
                "explanation": "In a rectangular slab, the second surface is parallel to the first, causing emergent rays of all colors to emerge parallel to each other with only lateral displacement.",
                "steps": [
                    "Step 1: Dispersion occurs at the first air-glass interface in both slabs and prisms.",
                    "Step 2: In a slab with parallel faces, refraction at the second interface cancels the angular deviation.",
                    "Step 3: All colors emerge parallel to each other, recombining visually into white light."
                ]
            },
            {
                "id": "c10_q20",
                "question": "What is the acronym used to remember the sequence of colors in the visible spectrum?",
                "options": ["VIBGYOR", "ROYGBIV", "VIBYGOR", "RGBVIOY"],
                "answer": 0,
                "hint": "Starts with Violet and ends with Red.",
                "explanation": "VIBGYOR represents Violet, Indigo, Blue, Green, Yellow, Orange, and Red in order of increasing wavelength.",
                "steps": [
                    "Step 1: Violet is the most refracted color at the base of the spectrum.",
                    "Step 2: The intermediate hues are Indigo, Blue, Green, Yellow, and Orange.",
                    "Step 3: Red is the least refracted color at the top, forming the acronym VIBGYOR."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Atmospheric Phenomena Review",
        "subtitle": "Atmospheric Refraction, Scintillation, and Horizon Shifts",
        "badge": "Review Set 3",
        "speech": "",
        "theory": """
            <div class="space-y-2 text-slate-300 text-xs leading-relaxed">
                <p><strong class="text-amber-400">Section Focus:</strong> Review of non-uniform atmospheric refraction, twinkling of point-source stars, stability of planetary extended disks, and sunrise/sunset duration shifts.</p>
            </div>
        """,
        "questions": [
            {
                "id": "c10_q21",
                "question": "What physical phenomenon causes the twinkling of stars at night?",
                "options": [
                    "Atmospheric refraction of starlight through turbulent air layers",
                    "Periodic thermonuclear pulsations inside star cores",
                    "Periodic occultation by passing orbital satellites",
                    "Total internal reflection within the stratosphere"
                ],
                "answer": 0,
                "hint": "Recall that turbulent air currents continuously alter atmospheric optical density.",
                "explanation": "Turbulent convection in atmospheric layers constantly fluctuates the local refractive index, causing starlight to waver and twinkle.",
                "steps": [
                    "Step 1: Starlight passes through multiple turbulent layers of Earth's atmosphere.",
                    "Step 2: Fluctuations in air density and temperature cause random changes in refractive index.",
                    "Step 3: The ray path shifts continuously, varying the intensity of starlight entering the pupil."
                ]
            },
            {
                "id": "c10_q22",
                "question": "Why do planets not twinkle like distant stars?",
                "options": [
                    "They are closer and act as extended sources whose fluctuations cancel out",
                    "They emit steady cold polarized light",
                    "Planetary light does not undergo atmospheric refraction",
                    "Their light consists exclusively of green wavelengths"
                ],
                "answer": 0,
                "hint": "Consider the difference between a point source and an extended source of light.",
                "explanation": "Planets are close to Earth and act as extended sources containing numerous points of light. Individual brightness variations average out to zero.",
                "steps": [
                    "Step 1: Stars are trillions of kilometres away and act as point sources.",
                    "Step 2: Planets are much closer, subtending measurable optical disks that act as collections of point sources.",
                    "Step 3: Random dimming from some points is balanced by brightening from others, producing steady light."
                ]
            },
            {
                "id": "c10_q23",
                "question": "How does atmospheric refraction affect the apparent position of a star relative to its true position?",
                "options": [
                    "The apparent position is slightly higher than the true position",
                    "The apparent position is slightly lower than the true position",
                    "The apparent position is shifted strictly toward the west",
                    "The star's apparent position is completely unchanged"
                ],
                "answer": 0,
                "hint": "Light rays bend towards the normal as they enter denser air near Earth's surface.",
                "explanation": "Because starlight bends continuously towards the normal as it enters denser lower air, backward extrapolation makes the star appear higher.",
                "steps": [
                    "Step 1: Starlight enters from vacuum into progressively denser atmospheric air layers.",
                    "Step 2: Light rays bend continuously towards the normal, curving downward toward the observer.",
                    "Step 3: Tangents drawn backward to the curved ray point to an apparent position slightly higher in the sky."
                ]
            },
            {
                "id": "c10_q24",
                "question": "By approximately how many minutes before actual sunrise is the Sun visible due to atmospheric refraction?",
                "options": ["About 2 minutes", "About 20 minutes", "About 4 minutes", "About 30 seconds"],
                "answer": 0,
                "hint": "Recall the time shift when the Sun is about 0.5 degrees below the horizon.",
                "explanation": "Atmospheric refraction bends sunlight over the horizon when the Sun is 0.5° below, making it visible ~2 minutes before actual sunrise.",
                "steps": [
                    "Step 1: Actual sunrise occurs when the physical solar disk crosses the geometric horizon.",
                    "Step 2: When the Sun is 0.5° below the horizon, atmospheric refraction curves rays downward to the observer.",
                    "Step 3: Earth rotates 0.5° in approximately 2 minutes, making the Sun appear 2 minutes early."
                ]
            },
            {
                "id": "c10_q25",
                "question": "What is the total increase in daylight duration each day on Earth caused by atmospheric refraction?",
                "options": ["About 4 minutes", "About 2 minutes", "About 8 minutes", "About 1 hour"],
                "answer": 0,
                "hint": "Add the 2 minutes gained at sunrise to the 2 minutes gained at sunset.",
                "explanation": "Atmospheric refraction advances sunrise by ~2 minutes and delays sunset by ~2 minutes, lengthening each day by ~4 minutes.",
                "steps": [
                    "Step 1: Advanced sunrise adds approximately 2 minutes of visible daylight in the morning.",
                    "Step 2: Delayed sunset adds approximately 2 minutes of visible daylight in the evening.",
                    "Step 3: Total daylight extension per day = 2 min + 2 min = approximately 4 minutes."
                ]
            },
            {
                "id": "c10_q26",
                "question": "Why does the disk of the Sun appear oval or flattened at sunrise and sunset?",
                "options": [
                    "Unequal atmospheric refraction across the upper and lower rims of the solar disk",
                    "Thermal expansion of solar gas along the equatorial axis",
                    "Gravitational tides exerted by lunar pull",
                    "Selective absorption of yellow light by atmospheric ozone"
                ],
                "answer": 0,
                "hint": "Consider the vertical gradient in air density across the solar diameter near the horizon.",
                "explanation": "The lower rim of the Sun traverses denser air and suffers greater refraction than the upper rim, vertically compressing the disk into an oval.",
                "steps": [
                    "Step 1: The solar disk subtends an angle of about 0.5° near the horizon.",
                    "Step 2: Rays from the lower edge pass through denser air than rays from the upper edge, undergoing greater refraction.",
                    "Step 3: This differential vertical displacement flattens the circular disk into an apparent oval."
                ]
            },
            {
                "id": "c10_q27",
                "question": "How does air temperature affect its optical refractive index?",
                "options": [
                    "Hot air is less dense and has a lower refractive index than cool air",
                    "Hot air is denser and has a higher refractive index than cool air",
                    "Temperature has zero effect on the refractive index of air",
                    "Hot air behaves as an optically opaque metallic mirror"
                ],
                "answer": 0,
                "hint": "Recall that thermal expansion causes gases to become rarer and less dense.",
                "explanation": "When air is heated, it expands and becomes less dense, resulting in a lower refractive index than surrounding cooler, denser air.",
                "steps": [
                    "Step 1: Heating causes air to expand, reducing its molecular number density.",
                    "Step 2: Fewer gas molecules per unit volume interact with propagating light waves.",
                    "Step 3: Consequently, hotter air has a lower optical refractive index than cooler air."
                ]
            },
            {
                "id": "c10_q28",
                "question": "What causes the shimmering and wavering of objects viewed through hot air rising over a radiator?",
                "options": [
                    "Rapid random fluctuations in the refractive index of turbulent convective air",
                    "Rapid molecular vibration of the physical object itself",
                    "Complete chromatic aberration of human corneal tissue",
                    "Total absorption of green wavelengths by radiator metal"
                ],
                "answer": 0,
                "hint": "Turbulent convection creates a constantly shifting optical medium.",
                "explanation": "Convection currents create turbulent eddies of hot and cool air with constantly shifting refractive indices, causing light rays to waver.",
                "steps": [
                    "Step 1: Air above a radiator heats up and rises in turbulent convective plumes.",
                    "Step 2: The optical refractive index fluctuates rapidly and unpredictably along the line of sight.",
                    "Step 3: Light rays are deflected erratically, causing background objects to appear to shimmer."
                ]
            },
            {
                "id": "c10_q29",
                "question": "What path does a light ray follow as it travels from outer space down through Earth's atmosphere?",
                "options": [
                    "A downward-concave curved path bending toward the normal",
                    "A perfectly straight geometric line with no deflection",
                    "A zig-zag rectangular staircase path",
                    "An upward-curving path reflecting back into space"
                ],
                "answer": 0,
                "hint": "The ray moves through a medium whose refractive index increases continuously downward.",
                "explanation": "Because atmospheric density increases continuously toward the ground, light continuously refracts towards the normal, forming a downward-curving trajectory.",
                "steps": [
                    "Step 1: Outer space has a refractive index of 1.000 (vacuum).",
                    "Step 2: As altitude decreases, air density and refractive index increase continuously.",
                    "Step 3: Continuous refraction towards the normal curves the ray downward toward Earth's surface."
                ]
            },
            {
                "id": "c10_q30",
                "question": "If Earth had no atmosphere, what would be the appearance of the sky during the daytime?",
                "options": [
                    "Completely black with visible stars",
                    "Bright glowing orange throughout",
                    "Solid uniform bright green",
                    "Identical to the current azure blue sky"
                ],
                "answer": 0,
                "hint": "Without gas molecules, there can be no optical scattering of sunlight.",
                "explanation": "Without an atmosphere, there are no air molecules to scatter sunlight into our eyes, so the sky would appear completely black.",
                "steps": [
                    "Step 1: Daytime sky illumination is caused by the scattering of sunlight by atmospheric gas molecules.",
                    "Step 2: In the absence of an atmosphere, sunlight would travel in straight lines without diffuse scattering.",
                    "Step 3: Looking away from the direct solar disk, the sky would appear pitch black, just as astronauts see in space."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Scattering Applications Review",
        "subtitle": "Tyndall Effect, Rayleigh Law, Sky Color, and Safety Signals",
        "badge": "Review Set 4",
        "speech": "",
        "theory": """
            <div class="space-y-2 text-slate-300 text-xs leading-relaxed">
                <p><strong class="text-amber-400">Section Focus:</strong> Review of colloidal light scattering, Rayleigh's inverse-fourth-power law, azure sky illumination, red danger signals, and corrective ophthalmic lens calculations.</p>
            </div>
        """,
        "questions": [
            {
                "id": "c10_q31",
                "question": "What is the Tyndall effect?",
                "options": [
                    "The scattering of light by colloidal particles rendering the beam path visible",
                    "The emission of electrons when ultraviolet light strikes a metal plate",
                    "The rotation of the plane of polarization by sugar solution",
                    "The splitting of spectral lines in an intense magnetic field"
                ],
                "answer": 0,
                "hint": "Recall the visible light beam observed in dusty rooms and misty forests.",
                "explanation": "The Tyndall effect is the scattering of light by suspended colloidal particles, making the beam trajectory visible.",
                "steps": [
                    "Step 1: Colloidal particles have sizes ranging between 1 nm and 1000 nm.",
                    "Step 2: When illuminated, these particles scatter incident light waves diffusely in all directions.",
                    "Step 3: This diffuse scattering illuminates the path of the light beam, known as the Tyndall effect."
                ]
            },
            {
                "id": "c10_q32",
                "question": "According to Rayleigh scattering law, how does scattering intensity I relate to wavelength λ?",
                "options": [
                    "I ∝ 1/λ⁴",
                    "I ∝ λ⁴",
                    "I ∝ 1/λ²",
                    "I ∝ λ"
                ],
                "answer": 0,
                "hint": "Recall the inverse fourth power dependence for particles much smaller than wavelength.",
                "explanation": "Rayleigh's law states that for particles much smaller than wavelength, scattered intensity is inversely proportional to the fourth power of wavelength (I ∝ 1/λ⁴).",
                "steps": [
                    "Step 1: Lord Rayleigh analyzed scattering by particles much smaller than the wavelength of light (a ≪ λ).",
                    "Step 2: Electromagnetic dipole scattering theory yields an inverse-fourth-power dependence.",
                    "Step 3: Thus, scattering intensity is expressed as I ∝ 1/λ⁴."
                ]
            },
            {
                "id": "c10_q33",
                "question": "Why does a clear daytime sky appear bright blue?",
                "options": [
                    "Fine atmospheric gas molecules scatter short blue wavelengths much more than red",
                    "Earth's blue oceans reflect their color directly onto upper clouds",
                    "The Sun emits blue photons exclusively during midday hours",
                    "Atmospheric oxygen emits blue fluorescence when excited by cosmic rays"
                ],
                "answer": 0,
                "hint": "Apply Rayleigh's inverse-fourth-power law to nitrogen and oxygen molecules.",
                "explanation": "Molecules of nitrogen and oxygen scatter shorter blue wavelengths ~10 times more intensely than red, filling the sky with blue light.",
                "steps": [
                    "Step 1: Nitrogen and oxygen molecules have diameters of ~0.3 nm, much smaller than visible light wavelengths.",
                    "Step 2: By Rayleigh's law (I ∝ 1/λ⁴), shorter blue wavelengths (λ ≈ 400 nm) scatter ~10 times more than red (λ ≈ 700 nm).",
                    "Step 3: Scattered blue photons reach our eyes from all directions in the atmosphere, creating an azure sky."
                ]
            },
            {
                "id": "c10_q34",
                "question": "Why are emergency danger signal lights universally painted red?",
                "options": [
                    "Red light has the longest visible wavelength and is scattered least by fog and smoke",
                    "Red light has the highest photon frequency in the visible spectrum",
                    "Red light undergoes total internal reflection inside human retinas",
                    "Red light travels at twice the cosmic speed of blue light in air"
                ],
                "answer": 0,
                "hint": "Consider which color penetrates dense fog and haze over maximum distances.",
                "explanation": "Because red light has the longest wavelength, Rayleigh scattering is minimal, allowing it to penetrate fog and smoke with little loss.",
                "steps": [
                    "Step 1: Red light has the longest wavelength in the visible spectrum (λ ≈ 700 nm).",
                    "Step 2: According to Rayleigh's law (I ∝ 1/λ⁴), red light experiences the lowest scattering intensity.",
                    "Step 3: It penetrates through atmospheric smoke, mist, and fog over long distances, remaining visible as a warning signal."
                ]
            },
            {
                "id": "c10_q35",
                "question": "Why do clouds in the atmosphere generally appear white rather than blue?",
                "options": [
                    "Water droplets in clouds are large (a ≫ λ) and scatter all wavelengths equally",
                    "Cloud moisture absorbs all visible wavelengths completely",
                    "Clouds only reflect monochromatic white laser radiation from the Sun",
                    "Cloud ice crystals undergo destructive interference for blue light"
                ],
                "answer": 0,
                "hint": "Consider how scattering changes when particle size is much larger than light wavelength.",
                "explanation": "Cloud droplets are much larger than light wavelengths, causing non-selective (Mie) scattering of all colors equally, producing white light.",
                "steps": [
                    "Step 1: Cloud water droplets have diameters of 1 to 20 micrometres, much larger than light wavelengths (~0.5 µm).",
                    "Step 2: For particles where a ≫ λ, Rayleigh's law does not apply; scattering becomes wavelength-independent.",
                    "Step 3: All visible spectral colors scatter with equal intensity, recombining to appear bright white."
                ]
            },
            {
                "id": "c10_q36",
                "question": "A person with a myopic eye has a far point of 80 cm. What is the power of the required corrective lens?",
                "options": ["-1.25 D", "+1.25 D", "-0.80 D", "+0.80 D"],
                "answer": 0,
                "hint": "Use P = 1/f where f = -d = -0.80 m.",
                "explanation": "To focus distant objects (u = -∞) at the far point v = -80 cm = -0.8 m, f = -0.8 m, so P = 1/(-0.8) = -1.25 D (concave lens).",
                "steps": [
                    "Step 1: Identify myopic far point d = 0.80 m. Object at infinity requires u = -∞ and v = -0.80 m.",
                    "Step 2: From the lens formula: 1/f = 1/v - 1/u = 1/(-0.80) - 0 = -1.25 m⁻¹.",
                    "Step 3: Optical power P = 1/f = -1.25 D (a diverging concave lens)."
                ]
            },
            {
                "id": "c10_q37",
                "question": "A hypermetropic person has a near point of 75 cm. What lens power is needed to read at 25 cm?",
                "options": ["+2.67 D", "-2.67 D", "+1.33 D", "-1.33 D"],
                "answer": 0,
                "hint": "Use 1/f = 1/v - 1/u with u = -25 cm = -0.25 m and v = -75 cm = -0.75 m.",
                "explanation": "1/f = 1/(-0.75) - 1/(-0.25) = -1.333 + 4.000 = +2.667 D (converging convex lens).",
                "steps": [
                    "Step 1: Set object distance u = -0.25 m and virtual image distance v = -0.75 m.",
                    "Step 2: Lens formula: 1/f = 1/(-0.75) - 1/(-0.25) = -4/3 + 4 = 8/3 ≈ +2.67 m⁻¹.",
                    "Step 3: Corrective optical power P = 1/f = +2.67 D (a converging convex lens)."
                ]
            },
            {
                "id": "c10_q38",
                "question": "What is the color of the sky perceived by an astronaut orbiting outside Earth's atmosphere?",
                "options": [
                    "Pitch dark / black",
                    "Radiant blue",
                    "Deep scarlet red",
                    "Bright glowing orange"
                ],
                "answer": 0,
                "hint": "Consider whether any scattering occurs in the vacuum of space.",
                "explanation": "In space, there are no atmospheric gas molecules to scatter sunlight, so the sky appears completely black.",
                "steps": [
                    "Step 1: Outside Earth's atmosphere, space is a near-perfect vacuum.",
                    "Step 2: Sunlight travels directly along rectilinear rays without experiencing any particulate scattering.",
                    "Step 3: Because no scattered photons enter the astronaut's eyes from the surrounding space, the sky appears pitch black."
                ]
            },
            {
                "id": "c10_q39",
                "question": "At sunrise and sunset, why does the solar disk and surrounding sky appear reddish?",
                "options": [
                    "Sunlight traverses maximum atmospheric thickness, scattering away blue light and leaving unscattered red",
                    "The Sun cools down significantly at morning and evening hours",
                    "Atmospheric carbon dioxide emits intense red radiation at low angles",
                    "Red light is selectively focused by the curvature of ocean waters"
                ],
                "answer": 0,
                "hint": "Consider the long atmospheric path traversed by horizon sunlight.",
                "explanation": "Sunlight passes through a much greater thickness of atmosphere near the horizon; shorter blue rays are scattered away, leaving mostly red rays.",
                "steps": [
                    "Step 1: Near the horizon, sunlight travels through a significantly longer atmospheric path than at noon.",
                    "Step 2: Shorter blue and violet wavelengths are scattered out of the direct line of sight by gas molecules.",
                    "Step 3: The less-scattered longer red wavelengths pass through directly to our eyes, making the Sun appear red."
                ]
            },
            {
                "id": "c10_q40",
                "question": "What happens to the focal length of the eye lens when ciliary muscles relax?",
                "options": [
                    "Focal length increases to its maximum value",
                    "Focal length decreases to zero",
                    "Focal length becomes negative",
                    "The lens ceases all refraction completely"
                ],
                "answer": 0,
                "hint": "Relaxation stretches the lens thin, increasing its radii of curvature.",
                "explanation": "When ciliary muscles relax, suspensory ligaments pull the lens thin, increasing its radius of curvature and focal length.",
                "steps": [
                    "Step 1: Ciliary relaxation pulls the suspensory zonules outward.",
                    "Step 2: The elastic crystalline lens is flattened and stretched thin.",
                    "Step 3: Flatter lens surfaces have larger radii of curvature, maximizing focal length for distant vision."
                ]
            }
        ]
    }
]

with open(".agents/c10s_ch10_part3.json", "w", encoding="utf-8") as f:
    json.dump(slides_part3, f, indent=2)

print(f"Generated {len(slides_part3)} review slides in Part 3.")
total_qs = 0
for s in slides_part3:
    tc = len(s["title"].split())
    qs = len(s["questions"])
    total_qs += qs
    print(f"Slide {s['id']}: '{s['title']}' ({tc} words) | Questions: {qs} | Speech: '{s['speech']}'")
    assert s["speech"] == "", f"Slide {s['id']} must have empty speech"
    assert 1 <= tc <= 3, f"Slide {s['id']} title out of range: {tc}"
    assert qs == 10, f"Slide {s['id']} must have 10 questions"
    for q in s["questions"]:
        assert len(q["options"]) == 4, f"Question {q['id']} must have 4 options"
        assert len(q["steps"]) == 3, f"Question {q['id']} must have 3 steps"
print(f"Total review challenge questions: {total_qs}")
