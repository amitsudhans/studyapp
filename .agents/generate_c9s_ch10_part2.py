#!/usr/bin/env python3
# -*- coding: utf-8 -*-

slides_part2 = [
    {
        "id": 9,
        "title": "Amplitude & Intensity",
        "subtitle": "Section 10.6.2: Peak Displacement, Energy & Inverse Square Law",
        "speech": (
            "What makes a whisper different from a roar? Section 10.6.2 explores Amplitude and Intensity! Amplitude "
            "is the maximum magnitude of displacement or density change of the medium particles from their average "
            "equilibrium position. When you strike a tabla gently, its skin vibrates with small amplitude, producing "
            "a quiet, gentle sound. Strike the tabla vigorously with your hand: the skin deflects deeply with large "
            "amplitude, transferring much greater kinetic energy to the air and producing a loud booming sound! "
            "The energy carried by a wave is directly proportional to the square of its amplitude! Now define Intensity: "
            "the amount of sound energy passing through a unit area perpendicular to the direction of propagation per "
            "unit time, measured in watts per square meter. Notice why sound fades as you walk farther from a speaker: "
            "as sound radiates outward in three-dimensional concentric spheres, the total acoustic energy spreads "
            "over a sphere surface area of four pi r squared! Consequently, intensity drops with the square of the "
            "distance, explaining why whispers are audible only nearby while megaphones focus energy along a beam! "
            "Remember: larger amplitude means greater energy, which our auditory perception interprets as louder sound "
            "across every auditory frequency we experience."
        ),
        "checkpoints": [
            {
                "question": "How does wave energy depend on the amplitude (A) of vibration?",
                "options": [
                    "Energy is inversely proportional to amplitude",
                    "Energy is directly proportional to the square of amplitude (Energy ∝ A²)",
                    "Energy is completely independent of amplitude",
                    "Energy equals the square root of amplitude"
                ],
                "answer": 1,
                "hint": "Doubling amplitude quadruples the energy carried by the wave.",
                "explanation": "Wave energy scales with the square of amplitude: E ∝ A²."
            },
            {
                "question": "Why does the intensity of sound from a point source decrease as you move farther away?",
                "options": [
                    "Air destroys acoustic energy permanently",
                    "Sound waves spread outward over expanding spherical surfaces (Area = 4πr²), so energy per unit area decreases",
                    "Frequency decreases to zero",
                    "Wavelength collapses into heat"
                ],
                "answer": 1,
                "hint": "Think of spherical wave expansion: geometric spreading.",
                "explanation": "Energy spreads over the surface of expanding spheres, following the inverse-square law: I ∝ 1/r²."
            }
        ]
    },
    {
        "id": 10,
        "title": "Speed of Sound",
        "subtitle": "Section 10.6.3 & Examples 10.2–10.4: v = λν & Lightning Delay",
        "speech": (
            "How fast does sound travel, and what equation connects its fundamental wave characteristics? Section 10.6.3 "
            "gives the universal Wave Equation: Speed v equals Wavelength lambda multiplied by Frequency nu! Because "
            "frequency nu is one divided by time period T, speed also equals lambda divided by T! The speed of sound "
            "depends strictly on the nature, temperature, and density of the medium. Sound travels slowest in gases "
            "(approximately 344 meters per second in air at 22 degrees Celsius), faster in liquids (about 1530 meters "
            "per second in water), and fastest in rigid solids (around 5000 meters per second in steel)! Look at our "
            "worked examples: in Example 10.2, for the human hearing range, a 20 hertz sound has a massive wavelength "
            "of 17.2 meters, while a 20 kilohertz ultrasonic wave has a tiny wavelength of 1.72 centimeters! In Example "
            "10.3, seeing lightning flash and hearing thunder 5 seconds later locates the lightning strike distance: "
            "multiply 340 meters per second by 5 seconds to get 1700 meters, or 1.7 kilometers away! Notice that "
            "light travels at three hundred million meters per second, so you see the flash instantly, while acoustic "
            "sound follows far behind at its characteristic medium speed."
        ),
        "checkpoints": [
            {
                "question": "What is the universal wave equation connecting speed (v), wavelength (λ), and frequency (ν)?",
                "options": [
                    "v = λ / ν",
                    "v = λ × ν (or v = λ / T)",
                    "v = λ² + ν²",
                    "v = ν / λ"
                ],
                "answer": 1,
                "hint": "Speed = distance / time = wavelength / time period = wavelength × frequency.",
                "explanation": "Speed equals wavelength times frequency: v = λν."
            },
            {
                "question": "In Example 10.3, a lightning flash is seen and thunder is heard 5 seconds later (speed of sound in air = 340 m/s). How far away was the lightning strike?",
                "options": [
                    "68 m",
                    "1700 m (1.7 km)",
                    "340 m",
                    "850 m"
                ],
                "answer": 1,
                "hint": "Distance = speed × time = 340 m/s × 5 s.",
                "explanation": "Distance = 340 × 5 = 1700 m = 1.7 km."
            }
        ]
    },
    {
        "id": 11,
        "title": "Pitch, Loudness, Timbre",
        "subtitle": "Section 10.6.4: Human Perception, Ear Anatomy & C. V. Raman's Acoustics",
        "speech": (
            "How do human senses decode acoustic waves? Section 10.6.4 links physical wave properties to sensory "
            "perception! Pitch is our subjective perception of frequency: high frequency produces a shrill, sharp "
            "high-pitched tone (like a bird chirping or a whistle), while low frequency produces a deep, bass low-pitched "
            "tone (like a roaring lion or a bass drum). Normal human hearing spans an audible range from 20 hertz to "
            "20,000 hertz! Sounds below 20 hertz are infrasonic, and sounds above 20 kilohertz are ultrasonic. Loudness "
            "is our subjective perception of amplitude, measured on a decibel scale. Timbre or quality is the unique "
            "harmonic overtone structure that lets you distinguish a violin from a flute playing the exact same note "
            "at the exact same loudness! Our ears capture these waves: the outer ear funnel directs sound into the "
            "ear canal, vibrating the eardrum, which moves three tiny bones—the hammer, anvil, and stirrup—amplifying "
            "vibrations into the fluid-filled cochlea! Also explore C. V. Raman's pioneering acoustic research on "
            "Indian percussion instruments, explaining how the black syaahi patch on tabla heads creates pure musical "
            "harmonics! This brilliant fusion of Indian musical heritage and classical wave mechanics proved that "
            "traditional instruments follow precise mathematical principles of acoustic harmony."
        ),
        "checkpoints": [
            {
                "question": "What is the normal audible frequency range for human ears, and what are sounds below and above this range called?",
                "options": [
                    "0 to 100 Hz; sub-bass and ultra-bass",
                    "20 Hz to 20,000 Hz (20 kHz); Infrasonic (<20 Hz) and Ultrasonic (>20 kHz)",
                    "1000 to 5000 Hz; radio and microwave",
                    "50 to 500 Hz; low and high"
                ],
                "answer": 1,
                "hint": "Normal hearing spans three orders of magnitude: 20 Hz to 20 kHz.",
                "explanation": "Human hearing covers 20 Hz to 20 kHz; below 20 Hz is infrasound, above 20 kHz is ultrasound."
            },
            {
                "question": "What acoustic discovery did Nobel laureate C. V. Raman make regarding traditional Indian drums like the tabla and mridangam?",
                "options": [
                    "They produce no sound in humid air",
                    "The black composite syaahi patch loads the membrane non-uniformly to produce pure harmonic musical overtones",
                    "They only emit ultrasonic frequencies",
                    "Their wooden shells act as vacuum chambers"
                ],
                "answer": 1,
                "hint": "The central black paste (syaahi) tunes the overtone frequencies harmonically.",
                "explanation": "Raman proved that the syaahi paste makes circular drum membranes vibrate with harmonic, bell-like overtones."
            }
        ]
    },
    {
        "id": 12,
        "title": "Reflection & Echoes",
        "subtitle": "Sections 10.7 & 10.7.1: Law of Reflection, 0.1 s Persistence & 17 m Rule",
        "speech": (
            "Just like light bouncing off a silvered mirror, sound waves reflect when striking a solid or liquid "
            "boundary! Section 10.7 establishes the Laws of Reflection of Sound: the incident acoustic wave, the "
            "reflected wave, and the normal to the reflecting surface at the point of incidence all lie in the same "
            "plane, and the angle of incidence strictly equals the angle of reflection! When you shout toward a distant "
            "tall cliff, building, or hillside in an open valley, you hear your own voice repeated clearly a moment "
            "later. This reflected acoustic repetition is called an Echo! Why does an echo require a large distance? "
            "Because the human brain retains an auditory sensation for approximately zero point one seconds—known "
            "as the persistence of hearing! To hear a distinct, separate echo, the reflected sound must return at "
            "least zero point one seconds after the original shout! Taking the speed of sound in air as 340 meters per "
            "second, the total round-trip distance must be at least 34 meters—meaning the obstacle must be at least "
            "half that, or 17 meters away! In Example 10.5, if an echo returns after 0.5 seconds, the obstacle distance "
            "is 340 times 0.5 divided by 2, which equals 85 meters!"
        ),
        "checkpoints": [
            {
                "question": "What is the minimum distance between a person and a reflecting obstacle in air (v = 340 m/s) to hear a distinct echo?",
                "options": [
                    "1.7 m",
                    "17 m (or 17.2 m at 22°C)",
                    "34 m",
                    "100 m"
                ],
                "answer": 1,
                "hint": "Round-trip time must exceed human hearing persistence (0.1 s): 2d = v × t = 340 × 0.1 = 34 m.",
                "explanation": "The minimum distance d = (v × t) / 2 = (340 × 0.1) / 2 = 17 meters."
            },
            {
                "question": "In Example 10.5, a person claps near a cliff and hears an echo 0.5 seconds later (v = 340 m/s). How far is the cliff?",
                "options": [
                    "170 m",
                    "85 m",
                    "340 m",
                    "42.5 m"
                ],
                "answer": 1,
                "hint": "Distance = (speed × echo time) / 2 = (340 × 0.5) / 2.",
                "explanation": "Round-trip distance = 340 × 0.5 = 170 m; one-way distance to cliff = 170 / 2 = 85 m."
            }
        ]
    },
    {
        "id": 13,
        "title": "Reverberation Control",
        "subtitle": "Section 10.7.2: Persistence in Halls, Drapery & Gol Gumbaz",
        "speech": (
            "What happens when sound reflects repeatedly inside an enclosed auditorium or concert hall? Section 10.7.2 "
            "examines Reverberation! In a large hall, sound emitted from a stage bounces successively off the ceiling, "
            "walls, and floor. Because the distances between walls are often less than 17 meters, multiple reflected "
            "sound waves arrive at intervals under zero point zero five seconds, blending together into a prolonged, "
            "confused drone! This persistence of sound resulting from multiple repeated reflections is called "
            "Reverberation. If reverberation is too long, spoken words blur together and become completely unintelligible! "
            "To manage reverberation, acoustic architects install sound-absorbing porous wall panels made of compressed "
            "fiberboard, hang heavy pleated fabric draperies, lay thick carpets, and use upholstered auditorium seats "
            "that absorb acoustic reflections. In architectural history, marvel at the Whispering Gallery inside the "
            "magnificent dome of Gol Gumbaz in Vijayapura, Karnataka, built in 1656: its curved acoustic masonry causes "
            "the faintest whisper to reflect and circle the dome clearly over ten times, heard sixty meters across! "
            "This historic marvel proves how structural geometry and hard masonry surfaces preserve acoustic energy "
            "through seamless multiple reflections, delighting visitors from across the country and the world who test "
            "its whispering archways daily."
        ),
        "checkpoints": [
            {
                "question": "What is reverberation, and why is excessive reverberation undesirable in school auditoriums?",
                "options": [
                    "Sound turning into ultrasound; it damages ears",
                    "The prolonged persistence of sound due to multiple repeated reflections; it blurs speech and makes words unintelligible",
                    "Complete silence caused by vacuum",
                    "Destructive interference that breaks windows"
                ],
                "answer": 1,
                "hint": "Overlapping reflections arrive too quickly to distinguish individual words.",
                "explanation": "Multiple rapid reflections prolong sound persistence, causing speech syllables to overlap and become garbled."
            },
            {
                "question": "Which materials and design techniques are employed in modern cinema halls and auditoriums to control reverberation?",
                "options": [
                    "Smooth polished marble tiles and steel walls",
                    "Sound-absorbing fiberboard panels, heavy fabric draperies, carpets, and upholstered seating",
                    "Replacing all air with helium gas",
                    "Using only parabolic brass mirrors"
                ],
                "answer": 1,
                "hint": "Porous, soft materials absorb sound wave reflections.",
                "explanation": "Porous acoustic tiles, carpets, curtains, and upholstered chairs absorb reflected energy, reducing reverberation time."
            }
        ]
    },
    {
        "id": 14,
        "title": "Infrasound & Ultrasound",
        "subtitle": "Section 10.8: Earthquakes, Imaging & Medical Lithotripsy",
        "speech": (
            "Beyond the limits of human hearing lies a vast acoustic frontier explored in Section 10.8! First, look "
            "at Infrasound—sound waves with frequencies below 20 hertz. Rhinoceroses, elephants, and whales communicate "
            "across dozens of kilometers using deep infrasonic rumbles that travel effortlessly through the ground and "
            "ocean water! Infrasound sensors detect early shockwaves from earthquakes, violent volcanic eruptions, and "
            "approaching tsunamis hours before macroscopic devastation occurs! Second, look at Ultrasound—sound waves "
            "with frequencies higher than 20,000 hertz, or 20 kilohertz! Ultrasound has extraordinary practical powers "
            "because its short wavelength allows it to penetrate deep into dense media along narrow, well-defined beams! "
            "In medicine, ultrasonography uses high-frequency ultrasonic pulses reflected off internal organs to produce "
            "real-time diagnostic images of hearts, livers, and developing fetuses with zero dangerous ionizing radiation! "
            "In medical lithotripsy, concentrated high-energy ultrasound pulses shatter hard kidney stones inside patients "
            "into fine powder without any surgical incisions! In heavy industry, ultrasound cleans delicate electronic "
            "components in spiral tanks and detects invisible internal cracks inside metal aircraft wings and railway "
            "tracks! From deep subterranean seismic monitoring to life-saving medical procedures, inaudible acoustic "
            "frequencies transform modern technology, providing indispensable diagnostic and industrial capabilities "
            "without destructive testing or radioactive hazards."
        ),
        "checkpoints": [
            {
                "question": "Which natural phenomena and animals are associated with infrasonic sound waves (<20 Hz)?",
                "options": [
                    "Bat navigation and dolphin hunting",
                    "Earthquakes, volcanic eruptions, and communication among elephants and whales",
                    "Hospital fetal ultrasound imaging",
                    "Violin harmonics"
                ],
                "answer": 1,
                "hint": "Very low frequencies travel massive distances through Earth and oceans.",
                "explanation": "Earthquakes and volcanic seismic waves produce infrasound; elephants and whales communicate via infrasonic rumbles."
            },
            {
                "question": "Which medical and industrial applications rely on high-frequency ultrasonic waves (>20 kHz)?",
                "options": [
                    "AM radio broadcasts and television antennas",
                    "Diagnostic ultrasonography, breaking kidney stones (lithotripsy), and non-destructive metal flaw detection",
                    "Measuring atmospheric wind speed only",
                    "Detecting cosmic dark matter"
                ],
                "answer": 1,
                "hint": "Ultrasound beams penetrate tissues safely and detect internal cracks in metals.",
                "explanation": "Ultrasound is used in medical imaging (ultrasonography), kidney stone pulverization (lithotripsy), and flaw detection."
            }
        ]
    },
    {
        "id": 15,
        "title": "Echolocation & Sonar",
        "subtitle": "Sections 10.8.1 & Example 10.6: Bats, Submarines & 2d = vt",
        "speech": (
            "Nature and human engineering converge beautifully in Section 10.8.1: Echolocation and SONAR! At night, "
            "flying bats emit high-pitched ultrasonic squeaks. When these high-frequency pulses bounce off tiny flying "
            "moths or tree branches, the bat's specialized ears analyze the echo's delay, pitch shift, and direction—building "
            "an instant, three-dimensional acoustic map of their surroundings to seize prey in mid-air! Marine dolphins "
            "and toothed whales use the exact same technique underwater. Humans copied nature to create SONAR, which "
            "stands for Sound Navigation and Ranging! A ship's underwater transmitter sends out a beam of ultrasonic "
            "pulses through seawater: the pulse travels down, reflects off the seabed, a sunken shipwreck, or an enemy "
            "submarine, and returns to an underwater receiver. Because the pulse travels down distance d and back up "
            "distance d, the total travel path is two d! Thus two d equals speed v multiplied by return time t, so "
            "distance d equals v times t divided by two! Look at Example 10.6: if a sonar signal returns in 0.90 "
            "seconds in seawater where sound speed is 1530 meters per second, the underwater object distance is 1530 "
            "times 0.90 divided by 2, which equals 688.5 meters! Whether mapping the deepest ocean trenches or "
            "tracking marine life, sonar demonstrates the unmatched versatility of ultrasonic waves underwater."
        ),
        "checkpoints": [
            {
                "question": "What is the acronym meaning of SONAR, and what fundamental equation calculates object distance from its echo return time?",
                "options": [
                    "Sound Observation Near Acoustic Radar; d = v × t",
                    "Sound Navigation and Ranging; 2d = v × t (or d = v × t / 2)",
                    "Submarine Optical Network Audio Ray; d = v / t",
                    "Sonic Ocean Navigation And Radio; d = 2v / t"
                ],
                "answer": 1,
                "hint": "The ultrasound pulse travels round-trip down and back up (distance 2d).",
                "explanation": "SONAR stands for Sound Navigation and Ranging; round-trip travel gives 2d = vt, so d = vt / 2."
            },
            {
                "question": "In Example 10.6, a sonar signal sent from a ship returns from an underwater reef after 0.90 s (speed in seawater = 1530 m/s). What is the reef distance?",
                "options": [
                    "1377 m",
                    "688.5 m",
                    "344.25 m",
                    "1530 m"
                ],
                "answer": 1,
                "hint": "d = (v × t) / 2 = (1530 × 0.90) / 2.",
                "explanation": "d = (1530 × 0.90) / 2 = 1377 / 2 = 688.5 meters."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter Summary",
        "subtitle": "At a Glance: Production, Wave Equations, Acoustics & Applications",
        "speech": (
            "Let us synthesize all of Chapter 10 in our comprehensive At a Glance roadmap! First, sound is a form of "
            "mechanical energy produced strictly by vibrating objects, such as strings, membranes, air columns, or "
            "human vocal cords inside the larynx. Second, sound is a mechanical longitudinal wave requiring a material "
            "medium to propagate—it cannot travel through a vacuum, as the bell jar experiment proves! Third, sound "
            "moves via alternating compressions (high density C) and rarefactions (low density R), characterized by "
            "wavelength lambda, frequency nu, time period T equals one over nu, and the universal wave equation: "
            "speed v equals lambda times nu! Fourth, speed of sound is fastest in solids, intermediate in liquids, and "
            "slowest in gases, increasing with temperature. Fifth, pitch reflects frequency, loudness reflects amplitude, "
            "and timbre reflects wave quality. Sixth, reflection of sound obeys equal angle laws, producing distinct "
            "echoes when obstacles are at least 17 meters away with a zero point one second delay, while excessive "
            "repeated reflections cause reverberation. Finally, infrasound below 20 hertz monitors earthquakes, and "
            "ultrasound above 20 kilohertz powers echolocation, medical imaging, lithotripsy, and ocean sonar. You "
            "are now fully prepared to demonstrate your mastery in the four silent quizzes ahead!"
        ),
        "checkpoints": [
            {
                "question": "Which complete formula set accurately captures the primary wave physics taught in Chapter 10?",
                "options": [
                    "v = λ / ν; T = ν²; 2d = v / t",
                    "v = λ × ν; T = 1 / ν; 2d = v × t (Echo / SONAR); Audible range = 20 Hz to 20 kHz",
                    "v = λ + ν; T = 2ν; d = 2vt",
                    "v = F / m; T = λ / 2; d = vt²"
                ],
                "answer": 1,
                "hint": "Verify wave speed, frequency-period inverse, echo round-trip, and hearing range.",
                "explanation": "v = λν, T = 1/ν, 2d = vt, and the 20 Hz–20 kHz audible range define Chapter 10."
            },
            {
                "question": "Which medium order correctly ranks the speed of sound from slowest to fastest?",
                "options": [
                    "Solids < Liquids < Gases",
                    "Gases (Air ~344 m/s) < Liquids (Water ~1530 m/s) < Solids (Steel ~5000 m/s)",
                    "Vacuum < Solids < Liquids",
                    "Liquids < Gases < Solids"
                ],
                "answer": 1,
                "hint": "Tighter particle packing in solids allows faster elastic collision propagation.",
                "explanation": "Sound travels slowest in gases, faster in liquids, and fastest in dense, elastic solids."
            }
        ]
    }
]
