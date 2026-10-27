with open('app/Http/Controllers/MultimediaController.php', 'r') as f:
    content = f.read()

# 1. Add Chapters 8, 9, 10, 11, 12 to ncert-science-class9
science_target = "            // NCERT Science Class 10"
science_addition = """                [
                    'chapter_num' => 8,
                    'name' => 'Earth as a System: Energy, Matter & Life',
                    'has_multimedia' => true,
                    'media_key' => 'class9-earth-as-a-system',
                    'media_title' => 'NCERT Class 9 Science • Chapter 8 • Earth as a System: Energy, Matter & Life Lab',
                    'media_url' => asset('animations/class9-earth-as-a-system.html'),
                    'description' => 'Comprehensive 20-slide interactive multimedia animated lab covering Earth as an interconnected open system (biosphere, geosphere, hydrosphere, cryosphere, atmosphere), solar electromagnetic radiation, differential solar heating, winds, biogeochemical cycles, human impact, 32 in-slide checkpoints, and 4 dedicated quiz slides (40 questions) with pop-up solutions.',
                    'topics' => [
                        'Earth as Interconnected System (Spheres)',
                        'Solar Energy, EM Spectrum & Speed of Light',
                        'Differential Heating & Global Atmospheric Winds',
                        'Biogeochemical Cycles (Water, Carbon, Nitrogen, Oxygen)',
                        'Human Impact & Sustainable Ecological Stewardship',
                        '32 In-Slide Checkpoints with Teacher Explanations',
                        '4 Dedicated Mastery Quiz Slides with Pop-up Solutions',
                    ],
                ],
                [
                    'chapter_num' => 9,
                    'name' => 'Motion',
                    'has_multimedia' => true,
                    'media_key' => 'class9-motion',
                    'media_title' => 'NCERT Class 9 Science • Chapter 9 • Motion Master Lab',
                    'media_url' => asset('animations/class9-motion.html'),
                    'description' => 'Comprehensive 20-slide interactive multimedia animated lab covering Motion in a straight line: distance vs displacement, speed vs velocity, acceleration, position-time and velocity-time graphs, graphical derivations of the 3 kinematic equations (v = u + at, s = ut + 0.5at², v² = u² + 2as), uniform circular motion, 32 in-slide checkpoints, and 4 dedicated quiz slides (40 questions) with pop-up solutions.',
                    'topics' => [
                        'Describing Motion: Distance vs Displacement & Reference Points',
                        'Speed vs Velocity: Uniform vs Non-Uniform Motion',
                        'Acceleration: Graphical Interpretations & Vectors',
                        'Graphical Derivation of Kinematic Equations',
                        'Uniform Circular Motion Dynamics & Centripetal Acceleration',
                        '32 In-Slide Checkpoints with Teacher Explanations',
                        '4 Dedicated Mastery Quiz Slides with Pop-up Solutions',
                    ],
                ],
                [
                    'chapter_num' => 10,
                    'name' => 'Force and Laws of Motion',
                    'has_multimedia' => true,
                    'media_key' => 'class9-force-and-laws-of-motion',
                    'media_title' => 'NCERT Class 9 Science • Chapter 10 • Force and Laws of Motion Master Lab',
                    'media_url' => asset('animations/class9-force-and-laws-of-motion.html'),
                    'description' => 'Comprehensive 20-slide interactive multimedia animated lab covering Force and Laws of Motion: balanced vs unbalanced forces, friction, Galileo inclined planes, Newton First Law (Inertia), Newton Second Law (F = ma and momentum p = mv), Newton Third Law (action-reaction pairs), conservation of momentum, 32 in-slide checkpoints, and 4 dedicated quiz slides (40 questions) with pop-up solutions.',
                    'topics' => [
                        'Force: Balanced vs Unbalanced Forces & Friction',
                        'Newton\'s First Law of Motion: Inertia and Mass',
                        'Newton\'s Second Law of Motion: Momentum & F = ma',
                        'Newton\'s Third Law of Motion: Action & Reaction Pairs',
                        'Conservation of Linear Momentum & Everyday Applications',
                        '32 In-Slide Checkpoints with Teacher Explanations',
                        '4 Dedicated Mastery Quiz Slides with Pop-up Solutions',
                    ],
                ],
                [
                    'chapter_num' => 11,
                    'name' => 'Work, Energy and Simple Machines',
                    'has_multimedia' => true,
                    'media_key' => 'class9-work-energy-simple-machines',
                    'media_title' => 'NCERT Class 9 Science • Chapter 11 • Work, Energy and Simple Machines Master Lab',
                    'media_url' => asset('animations/class9-work-energy-simple-machines.html'),
                    'description' => 'Comprehensive 20-slide interactive multimedia animated lab covering Work, Energy and Simple Machines: work done by a constant force (W = F·s·cosθ), Work-Energy Theorem, kinetic energy (0.5mv²), gravitational potential energy (mgh), conservation of mechanical energy in free fall, power (P = W/t in Watts), simple machines (levers, inclined planes, pulleys and mechanical advantage MA = Load/Effort), 32 in-slide checkpoints, and 4 dedicated quiz slides (40 questions) with pop-up solutions.',
                    'topics' => [
                        'Work Done by Constant Force: Positive, Negative & Zero Work',
                        'Kinetic Energy Derivation & Work-Energy Theorem',
                        'Gravitational Potential Energy & Mechanical Energy Conservation',
                        'Power & Commercial Unit of Electrical Energy (kWh)',
                        'Simple Machines: Mechanical Advantage (Levers, Pulleys, Inclined Planes)',
                        '32 In-Slide Checkpoints with Teacher Explanations',
                        '4 Dedicated Mastery Quiz Slides with Pop-up Solutions',
                    ],
                ],
                [
                    'chapter_num' => 12,
                    'name' => 'Sound',
                    'has_multimedia' => true,
                    'media_key' => 'class9-sound',
                    'media_title' => 'NCERT Class 9 Science • Chapter 12 • Sound Master Lab',
                    'media_url' => asset('animations/class9-sound.html'),
                    'description' => 'Comprehensive 20-slide interactive multimedia animated lab covering Sound: production by vibrations, longitudinal waves and medium compression/rarefactions, wave characteristics (wavelength λ, frequency ν, period T, amplitude, speed v = νλ), speed in various media, human ear perception (pitch and loudness), reflection of sound, echo distance (d = vt/2), reverberation, ultrasound SONAR, 32 in-slide checkpoints, and 4 dedicated quiz slides (40 questions) with pop-up solutions.',
                    'topics' => [
                        'Production of Sound & Need of Medium for Propagation',
                        'Sound as Longitudinal Waves: Compressions & Rarefactions',
                        'Wave Characteristics: λ, ν, T, Amplitude & Speed Formula v = νλ',
                        'Reflection of Sound: Echo, Reverberation & Echolocation (SONAR)',
                        'Human Perception: Audible Range (20 Hz - 20 kHz), Pitch & Loudness',
                        '32 In-Slide Checkpoints with Teacher Explanations',
                        '4 Dedicated Mastery Quiz Slides with Pop-up Solutions',
                    ],
                ],
            ],

            // NCERT Science Class 10"""

content = content.replace(science_target, science_addition)

# 2. Add ncert-english-class9 right before ncert-english-class10
english_target = "            // NCERT English Class 10"
english_addition = """            // NCERT English Class 9
            'ncert-english-class9' => [
                [
                    'chapter_num' => 1,
                    'name' => 'Effective Communication and Writing in Diverse Forms',
                    'has_multimedia' => true,
                    'media_key' => 'class9-english-communication-writing',
                    'media_title' => 'NCERT Class 9 English • Chapter 1 • Effective Communication & Writing Master Lab',
                    'media_url' => asset('animations/class9-english-communication-writing.html'),
                    'description' => 'Comprehensive 20-slide interactive multimedia animated laboratory covering Curricular Goal CG-1 and Competencies C-1.1, C-1.2, C-1.3, C-1.4: Effective communication loops and noise filters, formal vs informal linguistic registers, constructive debate and principled disagreement, Freytag\'s narrative pyramid, sensory descriptive imagery, expository compare-and-contrast matrix, Aristotelian rhetorical persuasion (Ethos, Pathos, Logos), formal event invitations & RSVP etiquette, solemn condolence messages & sincere empathy, high-impact notices & classified advertisements, school magazine journalism and inverted pyramid reporting, technology-enabled two-column audio-visual scripting, podcast production workflows, professional email netiquette, collaborative multi-author drafting, 32 in-slide checkpoints, and 4 dedicated quiz challenge slides (40 questions) with step-by-step pop-up solution modals.',
                    'topics' => [
                        'Effective Communication Loop, Sender-Receiver Channels & Noise Barriers (CG-1)',
                        'Social Context & Sociolinguistic Registers (Frozen, Formal, Consultative, Casual, Intimate) (C-1.1)',
                        'Constructive Debate, Principled Disagreement & Persuasive Rebuttal Strategies (C-1.1)',
                        'Deliberative Consensus, Active Listening & Conflict Resolution Frameworks (C-1.1)',
                        "Narrative Craft: Freytag's Pyramid, Suspense Arc & Sensory Vignettes (C-1.2)",
                        'Sensory Descriptive Mastery: Show-Don\'t-Tell Imagery & Figurative Palette (C-1.2)',
                        'Expository Architecture: Thesis Statements, Cause-Effect & Compare-Contrast (C-1.2)',
                        'Persuasive Rhetoric: Aristotelian Triangle (Ethos, Pathos, Logos) & Fallacy Traps (C-1.2)',
                        'Formal & Informal Invitations: 5 Ws, Card Layout & RSVP Etiquette (C-1.3)',
                        'Speech Writing Craft: The Hook, Rhetorical Devices & Emphatic Peroration (C-1.3)',
                        'Solemn Condolence Messages: Sincere Empathy, Respect & Bereavement Sensitivity (C-1.3)',
                        'Public Notices & Classified Advertisements: 50-Word Precision Box Layout (C-1.3)',
                        'School Newsletter Journalism: Inverted Pyramid, Catchy Headlines & Lead Paragraphs (C-1.3)',
                        'New Media Scripting: Two-Column Audio-Visual (AV) Production & Shot Calling (C-1.4)',
                        'Podcast Production Architecture: Narrative Arcs, Intro Stingers & Audio Cues (C-1.4)',
                        'Professional Email Netiquette: Executive Subject Lines, Structure & Cyber Tone (C-1.4)',
                        '32 Slide Checkpoint Inquiries with Real-Time Teacher Explanations',
                        '4 Dedicated Mastery Quiz Challenge Slides (40 Questions) with Step-by-Step Pop-up Solution Modals',
                    ],
                ],
            ],

            // NCERT English Class 10"""

content = content.replace(english_target, english_addition)

with open('app/Http/Controllers/MultimediaController.php', 'w') as f:
    f.write(content)
print('Successfully updated MultimediaController with all chapters!')
