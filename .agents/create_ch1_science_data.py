import re
import json

CHAPTER_META = {
    "chapter_num": 1,
    "title": "The Wonderful World of Science",
    "subtitle": "Curiosity, the Infinite Jigsaw & The Scientific Method",
    "mentors": "Dr. C.V. Raman & Curious Tara",
    "mentors_title": "Nobel Laureate Physicist & The Inquiring Young Explorer",
    "class": "Class 6",
    "subject": "Science",
    "curriculum": "NCERT Curiosity (NEP 2020)"
}

SLIDES = [
    {
        "id": 1,
        "badge": "Intro • Nature of Science",
        "title": "Spark of Curiosity",
        "subtitle": "Science as Thinking, Observing, and Unravelling Secrets",
        "theory": """
            <p>What is science? Science is not just a thick book of memorized facts. It is an exciting <strong>way of thinking, observing, and doing things</strong> to understand the wondrous natural world around us.</p>
            <p class="mt-2">At the very heart of science lies a single magical spark: <strong>Curiosity</strong>! When you look up and wonder why the sky is blue, why birds can fly without engines, or why leaves change color, you have already taken your first step as a scientist.</p>
            <p class="mt-2">Scientists never stop asking questions. They observe tiny clues, perform tests, and gradually unravel the deep secrets of the universe.</p>
        """,
        "summary": "Dr. C.V. Raman smiles: Curiosity is the lifeblood of discovery! When I gazed at the deep blue Mediterranean Sea in 1921, I asked 'Why is it blue?' That simple question led to the discovery of the Raman Effect!",
        "checkpoints": [
            {
                "id": "1-1",
                "question": "What is the primary foundation and driving force of scientific discovery?",
                "options": ["Rote memorization", "Curiosity and questioning", "Repeating old stories", "Guessing blindly"],
                "correct": 1,
                "explanation": "Curiosity — the desire to wonder, observe, and ask 'Why?' — is the core foundation of all scientific inquiry."
            },
            {
                "id": "1-2",
                "question": "Which of the following best defines science?",
                "options": [
                    "A static list of fixed rules that never change",
                    "A way of observing, thinking, and doing to understand nature",
                    "Only laboratory experiments with chemicals",
                    "A subject studied only by adults in universities"
                ],
                "correct": 1,
                "explanation": "Science is a dynamic process of observing, questioning, and experimenting to understand the natural world."
            }
        ]
    },
    {
        "id": 2,
        "badge": "1.1 • Ubiquitous Science",
        "title": "Science Everywhere",
        "subtitle": "From Grains of Sand and Kitchen Pots to Distant Galaxies",
        "theory": """
            <p>You don't need a high-tech laboratory with white coats to find science. Science is active in every corner of daily life!</p>
            <ul class="list-disc pl-5 mt-2 space-y-1 text-slate-300">
                <li><strong>In the Kitchen:</strong> Dough rising with yeast, milk curdling into paneer, and pressure cookers boiling lentils are chemical and physical transformations.</li>
                <li><strong>In Nature:</strong> A tiny grain of sand, an ant lifting ten times its body weight, and morning dew drops clinging to petals.</li>
                <li><strong>In the Oceans:</strong> Strange luminous creatures thriving in crushing dark deep-sea trenches.</li>
                <li><strong>In the Cosmos:</strong> The blazing heat of our Sun and billions of swirling stars across galaxies.</li>
            </ul>
        """,
        "summary": "Curious Tara exclaims: When my grandmother boils water or makes idli batter rise, that's science happening right on our kitchen stove!",
        "checkpoints": [
            {
                "id": "2-1",
                "question": "Where does scientific inquiry take place?",
                "options": [
                    "Only in specialized underground research labs",
                    "Everywhere — in kitchens, gardens, oceans, and outer space",
                    "Only in school science textbooks",
                    "Only on factory assembly lines"
                ],
                "correct": 1,
                "explanation": "Science encompasses the entire universe, from everyday kitchen cooking to deep ocean trenches and distant galaxies."
            },
            {
                "id": "2-2",
                "question": "Why is cooking in the kitchen considered a scientific activity?",
                "options": [
                    "Because cooks wear white aprons",
                    "Because it involves heat transfer, state changes, and chemical reactions",
                    "Because food is expensive",
                    "It is not related to science"
                ],
                "correct": 1,
                "explanation": "Cooking involves temperature measurement, state changes (boiling, melting), and chemical transformations of ingredients."
            }
        ]
    },
    {
        "id": 3,
        "badge": "1.1 • Evolving Knowledge",
        "title": "The Infinite Jigsaw",
        "subtitle": "How New Evidence Re-arranges the Pieces of Understanding",
        "theory": """
            <p>Imagine science as a giant, infinite jigsaw puzzle. Every time scientists make a discovery, they place another piece into the puzzle.</p>
            <p class="mt-2">Unlike a cardboard toy puzzle, however, our picture of the universe is continually expanding! Sometimes, a newly discovered piece reveals that older pieces were placed in the wrong spot.</p>
            <p class="mt-2">When <strong>new evidence</strong> appears, scientists do not cling stubbornly to old mistakes; they move the pieces and update their understanding. Science is self-correcting and never truly finished!</p>
        """,
        "summary": "Dr. C.V. Raman nods: Science is never a closed book. If a careful experiment produces new reliable evidence, the old theory must bend to welcome the truth!",
        "checkpoints": [
            {
                "id": "3-1",
                "question": "What happens in science when new, verified experimental evidence contradicts an old theory?",
                "options": [
                    "The new evidence is hidden and ignored",
                    "The scientific understanding is updated and revised",
                    "Science stops completely",
                    "People vote on which idea they like best"
                ],
                "correct": 1,
                "explanation": "Science is self-correcting; when new, verified evidence arises, theories are revised to fit the new discoveries."
            },
            {
                "id": "3-2",
                "question": "Why is scientific knowledge compared to an unending jigsaw puzzle?",
                "options": [
                    "Because it is made of wooden blocks",
                    "Because each discovery adds a piece, and the puzzle expands as we learn more",
                    "Because jigsaw puzzles are hard to finish",
                    "Because scientists only play games"
                ],
                "correct": 1,
                "explanation": "Every discovery adds a piece to our growing picture of nature, and new discoveries continually expand our understanding."
            }
        ]
    },
    {
        "id": 4,
        "badge": "1.2 • Living Diversity",
        "title": "Earth's Living Quilt",
        "subtitle": "The Only Known Haven for Life Across Varied Habitats",
        "theory": """
            <p>Among all the planets orbiting our Sun and the thousands discovered beyond our solar system, <strong>Earth is the only known planet that harbors life</strong>.</p>
            <p class="mt-2">Life on Earth is astonishingly diverse. Organisms have adapted to survive in almost every extreme environment:</p>
            <ul class="list-disc pl-5 mt-2 space-y-1 text-slate-300">
                <li>Thick cacti storing water in boiling desert sands.</li>
                <li>Snow leopards and yaks insulated by thick fur on icy Himalayan peaks.</li>
                <li>Mangrove trees with breathing roots in coastal saltwater mudflats.</li>
                <li>Colorful coral reefs teeming with thousands of marine fish species.</li>
            </ul>
        """,
        "summary": "Curious Tara marvels: From tiny moss clinging to cold mountain rocks to giant blue whales in warm oceans, Earth is a vibrant tapestry of living wonders!",
        "checkpoints": [
            {
                "id": "4-1",
                "question": "What unique feature distinguishes Earth from all other known planets in our solar system?",
                "options": ["It is the largest planet", "It is the only known planet that supports life", "It has the most moons", "It is the closest to the Sun"],
                "correct": 1,
                "explanation": "Earth is currently the only known planet in the universe that supports life, liquid water, and a breathable atmosphere."
            },
            {
                "id": "4-2",
                "question": "How do cacti manage to survive in arid, dry desert environments?",
                "options": [
                    "They migrate to rivers during summer",
                    "They store water in fleshy stems and reduce water loss through spine-like leaves",
                    "They freeze into ice",
                    "They only grow at night"
                ],
                "correct": 1,
                "explanation": "Cacti have adapted fleshy stems to store water and needle-like spines that minimize water loss through transpiration."
            }
        ]
    },
    {
        "id": 5,
        "badge": "1.2 • Life Cycles",
        "title": "Miracles of Growth",
        "subtitle": "From Tiny Seeds to Giant Banyan Trees & Caterpillars to Butterflies",
        "theory": """
            <p>One of the most breathtaking themes in science is the transformation of living beings during growth.</p>
            <p class="mt-2">A tiny mustard or banyan seed, smaller than a rice grain, contains the complete biological blueprint to draw moisture and soil minerals, sprouting roots downward and shooting branches upward into a massive tree providing shade for centuries.</p>
            <p class="mt-2">Similarly, an egg hatches into a crawling leaf-munching caterpillar. Inside a protective chrysalis (pupa), its body undergoes <strong>metamorphosis</strong>, reorganizing into a delicate, winged butterfly!</p>
        """,
        "summary": "Dr. C.V. Raman observes: Growth is organized energy at work. When you watch a seed germinate, you are witnessing the chemistry of life transforming soil, water, and sunlight into wood and leaves.",
        "checkpoints": [
            {
                "id": "5-1",
                "question": "What is the biological process called when a crawling caterpillar transforms into a winged butterfly?",
                "options": ["Photosynthesis", "Metamorphosis", "Evaporation", "Crystallization"],
                "correct": 1,
                "explanation": "Metamorphosis is the biological process of transformation from an immature larval form (caterpillar) to an adult form (butterfly)."
            },
            {
                "id": "5-2",
                "question": "What does a germinating seed require to sprout roots and shoots?",
                "options": ["Only dark soil", "Water, warmth, and air", "Sugar syrup", "Direct fire"],
                "correct": 1,
                "explanation": "A seed requires moisture (water), warmth (optimal temperature), and oxygen (air) to germinate and begin growing."
            }
        ]
    },
    {
        "id": 6,
        "badge": "1.2 • Nutrition",
        "title": "Cuisines & Nutrients",
        "subtitle": "Diverse Indian Dishes and the Science of What We Eat",
        "theory": """
            <p>India is blessed with an incredible variety of regional foods: steamed idlis in Tamil Nadu, makki di roti and sarson ka saag in Punjab, fish curry and rice in West Bengal, and dal baati churma in Rajasthan.</p>
            <p class="mt-2">Beyond rich flavors, food provides essential <strong>nutrients</strong> that our bodies need to grow, repair tissues, and stay healthy:</p>
            <ul class="list-disc pl-5 mt-2 space-y-1 text-slate-300">
                <li><strong>Carbohydrates & Fats:</strong> Energy givers (rice, wheat, ghee, oil).</li>
                <li><strong>Proteins:</strong> Body builders (lentils/dal, beans, eggs, milk).</li>
                <li><strong>Vitamins & Minerals:</strong> Protectors against illness (leafy greens, citrus fruits, carrots).</li>
            </ul>
        """,
        "summary": "Curious Tara notes: Our bodies are like living machines! Food is the fuel that powers our muscles and the construction material that repairs our bones.",
        "checkpoints": [
            {
                "id": "6-1",
                "question": "Which food group is primarily responsible for building muscles and repairing worn-out tissues?",
                "options": ["Fats", "Carbohydrates", "Proteins (like lentils, milk, and eggs)", "Water only"],
                "correct": 2,
                "explanation": "Proteins are the essential building blocks of the body required for growth, muscle building, and cellular repair."
            },
            {
                "id": "6-2",
                "question": "Why are green leafy vegetables and fresh fruits essential in our daily diet?",
                "options": [
                    "They provide vital vitamins and minerals to protect us from diseases",
                    "They contain only fats",
                    "They replace water completely",
                    "They stop food digestion"
                ],
                "correct": 0,
                "explanation": "Fresh fruits and leafy greens supply protective vitamins and minerals that boost immunity and maintain organ health."
            }
        ]
    },
    {
        "id": 7,
        "badge": "1.2 • Water Cycle",
        "title": "The Journey of Water",
        "subtitle": "From Oceans and Clouds to Falling Monsoons",
        "theory": """
            <p>Water is the lifeblood of our planet. Without fresh water, neither plants, animals, nor human civilizations could survive.</p>
            <p class="mt-2">Where does rain come from? Water moves in a perpetual cosmic loop called the <strong>Water Cycle</strong>:</p>
            <ol class="list-decimal pl-5 mt-1 space-y-1 text-slate-300">
                <li><strong>Evaporation:</strong> Solar heat warms lakes, rivers, and oceans, turning liquid water into invisible water vapor that rises into the sky.</li>
                <li><strong>Condensation:</strong> Cool air high above causes water vapor to cluster into tiny liquid droplets, forming clouds.</li>
                <li><strong>Precipitation:</strong> When droplets grow heavy and merge, they fall back to Earth as life-giving rain or snow!</li>
            </ol>
        """,
        "summary": "Dr. C.V. Raman observes: The water you drink today may have once rained upon ancient dinosaurs millions of years ago! Nature constantly recycles every drop through the atmosphere.",
        "checkpoints": [
            {
                "id": "7-1",
                "question": "What process turns liquid water from rivers and oceans into rising water vapor?",
                "options": ["Condensation", "Evaporation", "Freezing", "Filtration"],
                "correct": 1,
                "explanation": "Evaporation is the phase change where solar heat transforms liquid water into gaseous water vapor."
            },
            {
                "id": "7-2",
                "question": "What happens during condensation in the upper atmosphere?",
                "options": [
                    "Water vapor cools and condenses into tiny liquid droplets to form clouds",
                    "Liquid water turns into steam",
                    "Clouds fall directly to the ground",
                    "Water disappears forever"
                ],
                "correct": 0,
                "explanation": "Condensation occurs when rising warm vapor meets colder air aloft, gathering into microscopic droplets that compose clouds."
            }
        ]
    },
    {
        "id": 8,
        "badge": "1.2 • States of Matter",
        "title": "Three States of Matter",
        "subtitle": "Ice, Liquid Water, and Steam Governed by Temperature",
        "theory": """
            <p>Water is unique because we commonly experience it in all three physical states of matter simply by changing temperature:</p>
            <div class="grid grid-cols-3 gap-2 my-2 text-center text-xs">
                <div class="p-2 rounded-xl bg-blue-950/50 border border-blue-500/30">
                    <span class="font-bold text-blue-300 block">🧊 Solid</span>
                    Ice (< 0 °C)<br>Fixed shape & volume
                </div>
                <div class="p-2 rounded-xl bg-cyan-950/50 border border-cyan-500/30">
                    <span class="font-bold text-cyan-300 block">💧 Liquid</span>
                    Water (0 °C – 100 °C)<br>Takes shape of container
                </div>
                <div class="p-2 rounded-xl bg-slate-900 border border-slate-700">
                    <span class="font-bold text-slate-300 block">💨 Gas</span>
                    Steam (> 100 °C)<br>Expands to fill any space
                </div>
            </div>
            <p class="text-xs text-slate-300">Heating gives water molecules kinetic energy, loosening bonds from rigid solid ice to free-flowing liquid, and finally liberating them as energetic gas molecules.</p>
        """,
        "summary": "Curious Tara observes: Put an ice cube in the sun, and it melts into water. Boil that water, and it disappears as steam. It is the same substance in three disguise cloaks!",
        "checkpoints": [
            {
                "id": "8-1",
                "question": "What happens to the molecules of solid ice when heat energy is added?",
                "options": [
                    "They freeze tighter",
                    "They gain energy, vibrate faster, and break out of rigid positions to flow as liquid",
                    "They turn into stone",
                    "They vanish permanently"
                ],
                "correct": 1,
                "explanation": "Heat energy increases molecular vibration, overcoming intermolecular attractions and melting rigid ice into liquid water."
            },
            {
                "id": "8-2",
                "question": "At what sea-level temperature does pure liquid water boil into gaseous steam?",
                "options": ["0 °C", "50 °C", "100 °C", "200 °C"],
                "correct": 2,
                "explanation": "The standard boiling point of pure water at atmospheric sea-level pressure is 100 °C."
            }
        ]
    },
    {
        "id": 9,
        "badge": "1.2 • Thermal Senses",
        "title": "Hot or Cold?",
        "subtitle": "Why Our Sense of Touch Deceives and Thermometers Tell the Truth",
        "theory": """
            <p>Can you rely on your hands to measure temperature? Let's try an experiment:</p>
            <p class="mt-2 text-xs text-slate-300">Place one hand in warm water and the other in ice-cold water for a minute. Then place both hands together into lukewarm water. The warm hand feels cold, while the cold hand feels warm!</p>
            <p class="mt-2">Our skin only detects the <strong>relative transfer of heat</strong>, not true absolute temperature. To be objective scientists, we require precision instruments: <strong>Thermometers</strong> with standardized scales (Celsius °C or Fahrenheit °F) that never get fooled by perception.</p>
        """,
        "summary": "Dr. C.V. Raman emphasizes: Personal perception is subjective. Science requires objective, reproducible instruments so that every researcher across the globe measures the exact same value.",
        "checkpoints": [
            {
                "id": "9-1",
                "question": "Why can our sense of touch give misleading impressions about temperature?",
                "options": [
                    "Because our hands cannot touch water",
                    "Because skin only senses the relative rate of heat gain or loss, not absolute temperature",
                    "Because all water is identical",
                    "Skin is always 100% accurate"
                ],
                "correct": 1,
                "explanation": "Human skin senses relative thermal transfer compared to recent sensation, making touch subjective and easily fooled."
            },
            {
                "id": "9-2",
                "question": "Which scientific tool provides an objective, reliable measurement of temperature?",
                "options": ["A ruler", "A thermometer", "A balance scale", "A compass"],
                "correct": 1,
                "explanation": "A thermometer measures thermal energy quantitatively on calibrated numerical scales like Celsius."
            }
        ]
    },
    {
        "id": 10,
        "badge": "1.2 • Materials",
        "title": "Sorting Materials",
        "subtitle": "Classifying Matter by Properties: Metals, Plastics, and Magnets",
        "theory": """
            <p>Look around your classroom or room: clothes are made of cotton or polyester fabric, drinking tumblers are glass or steel, chairs are wooden or plastic, and electrical wires are copper.</p>
            <p class="mt-2">Scientists classify materials based on measurable physical properties:</p>
            <ul class="list-disc pl-5 mt-2 space-y-1 text-slate-300 text-xs sm:text-sm">
                <li><strong>Luster & Conductivity:</strong> Metals (iron, copper, gold) are shiny and conduct heat/electricity well.</li>
                <li><strong>Hardness & Flexibility:</strong> Wood is rigid; rubber is elastic and flexible.</li>
                <li><strong>Magnetic Attraction:</strong> Iron and nickel are pulled strongly by magnets; plastic, glass, and wood are non-magnetic.</li>
            </ul>
        """,
        "summary": "Curious Tara smiles: Knowing material properties helps us choose wisely! We make cooking pans out of heat-conducting steel, but pan handles out of heat-insulating bakelite plastic so we don't burn our hands!",
        "checkpoints": [
            {
                "id": "10-1",
                "question": "Why are cooking pan handles typically made of wood or heat-resistant plastic rather than metal?",
                "options": [
                    "Because metals are too soft",
                    "Because wood and plastics are poor conductors of heat (insulators), keeping hands safe",
                    "Because plastics are magnetic",
                    "Because metals melt instantly on a stove"
                ],
                "correct": 1,
                "explanation": "Wood and plastic are thermal insulators that prevent heat from conducting into your hands."
            },
            {
                "id": "10-2",
                "question": "Which of the following objects will be attracted to a magnet?",
                "options": ["A plastic ruler", "A steel safety pin", "A wooden pencil", "A cotton handkerchief"],
                "correct": 1,
                "explanation": "Steel safety pins contain iron, which is ferromagnetic and strongly attracted by magnets."
            }
        ]
    },
    {
        "id": 11,
        "badge": "1.2 • Astronomy",
        "title": "Celestial Wonders",
        "subtitle": "Gazing Beyond Earth: The Sun, Moon, and Cosmic Stars",
        "theory": """
            <p>When the sun sets, our window into the grand cosmos opens. Science reaches far beyond our planet into the boundless ocean of space.</p>
            <p class="mt-2">Our <strong>Sun</strong> is a roaring thermonuclear star around which Earth and 7 other sibling planets revolve. The <strong>Moon</strong>, Earth's natural companion, circles us every 27.3 days, reflecting sunlight in changing phases.</p>
            <p class="mt-2">And every twinkling star in the night sky is another sun, many with their own planetary systems, located light-years across the Milky Way galaxy!</p>
        """,
        "summary": "Dr. C.V. Raman muses: Astronomy teaches us profound humility and limitless curiosity. We are explorers on a pale blue dot looking out into a universe of trillions of luminous stars.",
        "checkpoints": [
            {
                "id": "11-1",
                "question": "What is the Sun at the center of our solar system?",
                "options": ["A giant solid rock", "A star — a massive glowing ball of hot gas", "A giant planet", "A cosmic moon"],
                "correct": 1,
                "explanation": "The Sun is a medium-sized star generating colossal heat and light through nuclear fusion at its core."
            },
            {
                "id": "11-2",
                "question": "Why does the Moon shine in the night sky?",
                "options": [
                    "It produces its own light like a torch",
                    "It reflects light from the Sun towards Earth",
                    "It is covered in glowing neon moss",
                    "It absorbs light from city streetlights"
                ],
                "correct": 1,
                "explanation": "The Moon does not emit its own light; it shines because its rocky surface reflects sunlight back to our eyes."
            }
        ]
    },
    {
        "id": 12,
        "badge": "1.3 • Inquiry",
        "title": "The Scientific Method",
        "subtitle": "Structured Troubleshooting: The Story of the Broken Pen",
        "theory": """
            <p>How do scientists find truth? They don't guess blindly or believe rumors. They employ a systematic detective process called the <strong>Scientific Method</strong>.</p>
            <p class="mt-2">Consider a simple everyday mystery: You are writing notes and suddenly your ballpoint pen stops writing!</p>
            <ul class="list-disc pl-5 mt-2 space-y-1 text-slate-300 text-xs sm:text-sm">
                <li><strong>Observation:</strong> No ink appears on the paper.</li>
                <li><strong>Question:</strong> Why did the pen stop writing?</li>
                <li><strong>Hypothesis 1:</strong> Maybe the ink refill is completely empty.</li>
                <li><strong>Test 1:</strong> Unscrew the barrel. You see the transparent tube is half-full of blue ink! (Hypothesis 1 rejected).</li>
                <li><strong>Hypothesis 2:</strong> Maybe dry ink is clogging the ball at the tip.</li>
                <li><strong>Test 2:</strong> Scribble firmly on a rough scrap sheet or warm the tip gently. The ball rolls and fresh ink flows! (Hypothesis 2 verified).</li>
            </ul>
        """,
        "summary": "Curious Tara laughs: I used the scientific method this morning without even realizing it when I fixed my pen!",
        "checkpoints": [
            {
                "id": "12-1",
                "question": "In the pen troubleshooting example, what did unscrewing the barrel to check ink level represent?",
                "options": ["Formulating a guess", "Testing a hypothesis through observation", "Giving up on science", "Writing a poem"],
                "correct": 1,
                "explanation": "Inspecting the transparent refill was a test designed to check the hypothesis that the pen was empty."
            },
            {
                "id": "12-2",
                "question": "What is the primary advantage of the scientific method over blind guessing?",
                "options": [
                    "It is much faster than thinking",
                    "It provides a structured, evidence-based pathway to uncover verified causes",
                    "It never requires experiments",
                    "It makes all pens write forever"
                ],
                "correct": 1,
                "explanation": "The scientific method tests hypotheses against repeatable evidence, eliminating false assumptions systematically."
            }
        ]
    },
    {
        "id": 13,
        "badge": "1.3 • Core Steps",
        "title": "Observe & Question",
        "subtitle": "Stage 1 & 2: Noticing the Unexpected and Formulating 'Why?'",
        "theory": """
            <p>Every great breakthrough in human history began with two foundational steps:</p>
            <div class="space-y-3 my-2 text-xs sm:text-sm">
                <div class="p-3 rounded-xl bg-cyan-950/40 border border-cyan-500/30">
                    <strong class="text-cyan-300 block mb-1">Step 1: Careful Observation</strong>
                    Using your senses (sight, hearing, touch, smell) and tools to notice an intriguing pattern, anomaly, or unexplained event in nature.
                </div>
                <div class="p-3 rounded-xl bg-amber-950/40 border border-amber-500/30">
                    <strong class="text-amber-300 block mb-1">Step 2: Formulating Sharp Questions</strong>
                    Converting that observation into an actionable question: <em>'Why does this happen?' 'What causes that change?' 'Under what conditions does it fail?'</em>
                </div>
            </div>
            <p class="text-xs text-slate-300">When Alexander Fleming observed that green mold killed bacteria in a forgotten petri dish, his sharp question birthed penicillin and saved millions of lives!</p>
        """,
        "summary": "Dr. C.V. Raman notes: Millions had seen apples fall before Newton, but Newton asked 'Why does the apple fall towards Earth rather than sideways or upward?' Great questions spark revolutions.",
        "checkpoints": [
            {
                "id": "13-1",
                "question": "What is the very first step in the scientific method?",
                "options": ["Drawing conclusions", "Careful observation of a phenomenon", "Publishing a textbook", "Selling an invention"],
                "correct": 1,
                "explanation": "Careful observation — noticing an interesting, unexplained occurrence in nature — is the starting point of inquiry."
            },
            {
                "id": "13-2",
                "question": "Why is asking specific, testable questions crucial in scientific research?",
                "options": [
                    "Because questions help identify what needs to be investigated and tested",
                    "Because scientists like arguments",
                    "Questions are not needed if you guess",
                    "Because all questions have already been answered"
                ],
                "correct": 0,
                "explanation": "A sharp, specific question defines the scope of the investigation and guides the hypothesis."
            }
        ]
    },
    {
        "id": 14,
        "badge": "1.3 • Core Steps",
        "title": "Hypothesize & Test",
        "subtitle": "Stage 3 & 4: Crafting Testable Explanations and Fair Experiments",
        "theory": """
            <p>Once you have a clear question, the inquiry advances to prediction and experimentation:</p>
            <div class="space-y-3 my-2 text-xs sm:text-sm">
                <div class="p-3 rounded-xl bg-purple-950/40 border border-purple-500/30">
                    <strong class="text-purple-300 block mb-1">Step 3: Propose a Hypothesis</strong>
                    A hypothesis is not a wild guess; it is an <strong>educated, testable explanation</strong> based on prior knowledge (e.g., <em>'If plants receive sunlight, then they will grow taller than plants in darkness.'</em>).
                </div>
                <div class="p-3 rounded-xl bg-emerald-950/40 border border-emerald-500/30">
                    <strong class="text-emerald-300 block mb-1">Step 4: Conduct a Fair Experiment</strong>
                    Design a test where only <strong>one factor (variable)</strong> is changed while keeping all other conditions identical (fair comparison).
                </div>
            </div>
        """,
        "summary": "Curious Tara explains: If I want to test if sunlight helps plants grow, I keep soil, water, pot size, and seed type identical for both pots, changing ONLY sunlight exposure!",
        "checkpoints": [
            {
                "id": "14-1",
                "question": "What is a scientific hypothesis?",
                "options": [
                    "An indisputable truth that cannot be questioned",
                    "An educated, testable proposed explanation for an observation",
                    "A random guess with no reasoning",
                    "The final conclusion of a project"
                ],
                "correct": 1,
                "explanation": "A hypothesis is an educated proposition that can be verified or falsified through controlled experiments."
            },
            {
                "id": "14-2",
                "question": "What is a 'fair test' (controlled experiment)?",
                "options": [
                    "An experiment where everything is changed all at once",
                    "An experiment where only one variable is altered at a time, keeping all other factors constant",
                    "An experiment where everyone wins a prize",
                    "An experiment conducted without any measurements"
                ],
                "correct": 1,
                "explanation": "A fair test controls all extraneous variables so that any observed effect can be attributed solely to the single variable being tested."
            }
        ]
    },
    {
        "id": 15,
        "badge": "1.3 • Core Steps",
        "title": "Analyze & Conclude",
        "subtitle": "Stage 5: Inspecting Evidence, Drawing Conclusions, and Iterating",
        "theory": """
            <p>After running experiments and recording data, the crucial moment of judgment arrives:</p>
            <ul class="list-disc pl-5 mt-2 space-y-1 text-slate-300 text-xs sm:text-sm">
                <li><strong>Analyze the Data:</strong> Organize numbers, measurements, and logs into charts and graphs. Look for clear trends.</li>
                <li><strong>Draw Conclusions:</strong> Does the data support your hypothesis or disprove it?</li>
                <li><strong>If Supported:</strong> Share your findings with the community for peer review and replication.</li>
                <li><strong>If Disproved:</strong> Don't despair! A failed hypothesis is a huge discovery — it proves what doesn't work, pointing towards a better hypothesis!</li>
            </ul>
        """,
        "summary": "Dr. C.V. Raman smiles: Thomas Edison tried thousands of materials before perfecting the lightbulb filament. He said: 'I have not failed 1,000 times; I have successfully found 1,000 ways that do not work!'",
        "checkpoints": [
            {
                "id": "15-1",
                "question": "What should a scientist do if the experimental data contradicts their original hypothesis?",
                "options": [
                    "Falsify the data to match the hypothesis",
                    "Accept the findings honestly, learn from them, and formulate an improved hypothesis",
                    "Throw away the laboratory notebook",
                    "Stop doing science"
                ],
                "correct": 1,
                "explanation": "Disproving a hypothesis provides valuable evidence that rules out false paths and leads to refined theories."
            },
            {
                "id": "15-2",
                "question": "Why do scientists record measurements and share their results openly with others?",
                "options": [
                    "To boast on social media",
                    "So other researchers can verify, replicate, and build upon the discoveries",
                    "Because textbooks demand it",
                    "It has no practical benefit"
                ],
                "correct": 1,
                "explanation": "Open peer review and independent replication verify scientific findings, ensuring reliability and collective progress."
            }
        ]
    },
    {
        "id": 16,
        "badge": "1.3 • Everyday Inquiry",
        "title": "Everyday Scientists",
        "subtitle": "Cooks, Mechanics, Electricians & The Journey of a 'Whys' Person",
        "theory": """
            <p>You don't need a diploma to be a scientist. Anyone who observes carefully, diagnoses problems logically, and tests solutions is practicing genuine science:</p>
            <ul class="list-disc pl-5 mt-2 space-y-1 text-slate-300 text-xs sm:text-sm">
                <li><strong>The Cook:</strong> Dal sputters out of the cooker vent. The cook reasons: <em>'Did I add too much water or turn the flame too high?'</em> They adjust the flame and test again.</li>
                <li><strong>The Bicycle Mechanic:</strong> A tyre goes flat. The mechanic immerses the pumped tube into a water basin. Bubbles pinpoint the puncture!</li>
                <li><strong>The Electrician:</strong> A ceiling fan won't turn. They systematically check the wall switch, fuse, and capacitor.</li>
            </ul>
            <p class="mt-2 text-xs text-amber-300 font-semibold">Science is a team journey. When you keep asking 'Why?', you become a truly wise person — a lifelong 'whys' person!</p>
        """,
        "summary": "Curious Tara beams: Whenever you investigate a mystery in your neighborhood with your friends, you are walking shoulder-to-shoulder with the greatest scientists in history!",
        "checkpoints": [
            {
                "id": "16-1",
                "question": "How does a bicycle repairer use the scientific method to locate a puncture in an inner tube?",
                "options": [
                    "By guessing blindly where the hole might be",
                    "By immersing the inflated tube in water and observing where escaping air creates bubbles",
                    "By replacing the whole bicycle",
                    "By painting the tyre blue"
                ],
                "correct": 1,
                "explanation": "Submerging the tube in water is an ingenious test: escaping air forms visible bubbles, pinpointing the puncture."
            },
            {
                "id": "16-2",
                "question": "What does it mean to become a lifelong 'whys' person?",
                "options": [
                    "Someone who complains all day",
                    "A curious individual who continually questions, observes, and seeks evidence to gain wisdom",
                    "Someone who only memorizes facts for tests",
                    "A person who avoids learning new things"
                ],
                "correct": 1,
                "explanation": "A 'whys' person never loses curiosity, constantly questioning the world to deepen understanding and wisdom."
            }
        ]
    },
    # Quiz Slides 17 to 20
    {
        "id": 17,
        "badge": "Quiz 1 • Foundations",
        "title": "Mastery Challenge I",
        "subtitle": "Questions 1 – 10: Nature of Science, Curiosity & Everyday Wonders",
        "is_quiz": True,
        "quiz_range": [1, 10]
    },
    {
        "id": 18,
        "badge": "Quiz 2 • Earth & Living World",
        "title": "Mastery Challenge II",
        "subtitle": "Questions 11 – 20: Living Diversity, Growth, Cuisines & Nutrients",
        "is_quiz": True,
        "quiz_range": [11, 20]
    },
    {
        "id": 19,
        "badge": "Quiz 3 • Matter & Cycles",
        "title": "Mastery Challenge III",
        "subtitle": "Questions 21 – 30: Water Cycle, States of Matter, Heat & Materials",
        "is_quiz": True,
        "quiz_range": [21, 30]
    },
    {
        "id": 20,
        "badge": "Quiz 4 • The Scientific Method",
        "title": "Mastery Challenge IV",
        "subtitle": "Questions 31 – 40: Steps of Inquiry, Controlled Tests & Everyday Scientists",
        "is_quiz": True,
        "quiz_range": [31, 40]
    }
]

QUIZ_QUESTIONS = [
    # Q1 - Q10 (Slide 17)
    {
        "id": 1,
        "question": "What is the primary driving emotion that sparks scientific exploration?",
        "options": ["Fear", "Curiosity", "Anger", "Boredom"],
        "correct": 1,
        "solution": "Curiosity — the innate desire to wonder and ask 'Why?' and 'How?' — is the core spark of all scientific discovery."
    },
    {
        "id": 2,
        "question": "Why is science compared to an unending jigsaw puzzle?",
        "options": [
            "Because scientists only play table games",
            "Because each discovery adds a new piece, and new evidence can re-arrange existing pieces",
            "Because jigsaw puzzles are made of cardboard",
            "Because science was completed 100 years ago"
        ],
        "correct": 1,
        "solution": "Science is an evolving, self-correcting body of knowledge where new discoveries add pieces and improve our overall understanding."
    },
    {
        "id": 3,
        "question": "Which of the following is an example of science taking place in the kitchen?",
        "options": [
            "Boiling water turning to steam",
            "Milk curdling when lemon juice is added",
            "Dough rising with yeast",
            "All of the above"
        ],
        "correct": 3,
        "solution": "All listed events represent physical phase changes (boiling) and chemical transformations (curdling, fermentation) in the kitchen."
    },
    {
        "id": 4,
        "question": "What should a scientist do when verified new evidence contradicts an established theory?",
        "options": [
            "Destroy the new evidence",
            "Update the theory to accommodate the new evidence",
            "Ban experiments",
            "Ignore the findings"
        ],
        "correct": 1,
        "solution": "Science is self-correcting. Theories must adapt or be replaced when valid new experimental evidence contradicts them."
    },
    {
        "id": 5,
        "question": "Who among the following acts as a scientist in daily life?",
        "options": [
            "A cook figuring out why food burned",
            "A mechanic diagnosing a flat tyre in a water tub",
            "An electrician testing a faulty light switch",
            "All of the above"
        ],
        "correct": 3,
        "solution": "Anyone who systematically observes, diagnoses, and tests solutions is practicing the scientific method."
    },
    {
        "id": 6,
        "question": "Which of the following statements about science is FALSE?",
        "options": [
            "Science is only done by famous professors in university laboratories",
            "Science is an ongoing journey of exploration",
            "Science requires testing ideas with evidence",
            "Science involves teamwork and collaboration"
        ],
        "correct": 0,
        "solution": "Science is accessible to everyone — students, cooks, farmers, mechanics, and researchers alike."
    },
    {
        "id": 7,
        "question": "What led Dr. C.V. Raman to discover the Raman Effect in 1921?",
        "options": [
            "Wondering why the Mediterranean Sea looked intensely blue during a voyage",
            "Reading a novel",
            "Accidentally dropping a magnifying glass",
            "Dreaming about stars"
        ],
        "correct": 0,
        "solution": "Observing the vivid blue color of the sea during a ship voyage sparked Raman's curiosity about light scattering, winning him the Nobel Prize."
    },
    {
        "id": 8,
        "question": "How do scientific discoveries benefit human society?",
        "options": [
            "By discovering medicines, clean energy, and technologies to improve life",
            "By making school exams harder",
            "By locking up knowledge in secret vaults",
            "They have no practical impact"
        ],
        "correct": 0,
        "solution": "Science drives medical advancements, clean water systems, agriculture, and technological breakthroughs that support human well-being."
    },
    {
        "id": 9,
        "question": "What is the best attitude for a young science student to adopt?",
        "options": [
            "Accepting everything without questioning",
            "Remaining curious, observant, and asking 'Why?'",
            "Memorizing facts without understanding",
            "Avoiding experiments"
        ],
        "correct": 1,
        "solution": "A healthy scientific attitude combines open curiosity, keen observation, and asking critical questions based on evidence."
    },
    {
        "id": 10,
        "question": "Why is teamwork and collaboration important in modern science?",
        "options": [
            "Complex questions often require diverse skills, shared data, and mutual peer review",
            "Because scientists get lonely",
            "It saves paper",
            "So one person does all the work"
        ],
        "correct": 0,
        "solution": "Modern science tackles vast global challenges (like climate and medicine) that require collective expertise and shared verification."
    },

    # Q11 - Q20 (Slide 18)
    {
        "id": 11,
        "question": "What makes planet Earth unique compared to other known celestial bodies?",
        "options": [
            "It is made entirely of gold",
            "It is the only planet confirmed to support living organisms",
            "It has three rings of ice",
            "It is the coldest planet in the universe"
        ],
        "correct": 1,
        "solution": "Earth uniquely possesses liquid surface water, a protective atmosphere, and conditions that harbor life."
    },
    {
        "id": 12,
        "question": "How does a desert cactus conserve water in arid climates?",
        "options": [
            "It has needle-like spines instead of broad leaves to minimize water loss",
            "It grows under water",
            "It drinks salt water from oceans",
            "It sleeps for 50 years"
        ],
        "correct": 0,
        "solution": "Cactus leaves are modified into sharp spines, dramatically reducing transpiration surface area and conserving water in its thick stem."
    },
    {
        "id": 13,
        "question": "What major biological transformation occurs inside a butterfly's chrysalis?",
        "options": ["Photosynthesis", "Metamorphosis", "Rusting", "Evaporation"],
        "correct": 1,
        "solution": "Metamorphosis transforms the larval caterpillar tissues into the adult anatomy of a winged butterfly."
    },
    {
        "id": 14,
        "question": "What three basic conditions are essential for a dormant seed to germinate?",
        "options": [
            "Water, warmth, and air (oxygen)",
            "Fertilizer, direct fire, and sugar",
            "Darkness, ice, and salt",
            "Wind, stone, and oil"
        ],
        "correct": 0,
        "solution": "Water hydrates the seed enzymes, warmth provides the optimal metabolic temperature, and oxygen fuels cellular respiration."
    },
    {
        "id": 15,
        "question": "Which essential nutrient group is primarily known as 'energy-giving' food?",
        "options": ["Carbohydrates and Fats", "Proteins only", "Water", "Vitamins only"],
        "correct": 0,
        "solution": "Carbohydrates (rice, wheat) and fats (oils, ghee) provide the primary caloric energy for daily activities."
    },
    {
        "id": 16,
        "question": "Why does a growing child require adequate protein in their diet?",
        "options": [
            "Proteins build new cells, muscles, and repair bodily tissues",
            "Proteins make bones turn into glass",
            "Proteins replace breathing",
            "Proteins stop the heart"
        ],
        "correct": 0,
        "solution": "Proteins provide the essential amino acid building blocks required for cellular division, muscle synthesis, and growth."
    },
    {
        "id": 17,
        "question": "Which food items are rich sources of dietary proteins?",
        "options": ["Pulses (dal), beans, eggs, and milk", "Pure sugar and candy", "Cooking oil and butter", "Plain carbonated water"],
        "correct": 0,
        "solution": "Lentils (dal), paneer, soybeans, eggs, and dairy products are rich in dietary protein."
    },
    {
        "id": 18,
        "question": "How do vitamins and minerals protect our health?",
        "options": [
            "They boost our immune system and help fight off illnesses",
            "They provide heavy body weight",
            "They make our skin glow in the dark",
            "They replace the need for drinking water"
        ],
        "correct": 0,
        "solution": "Vitamins (like Vitamin C and A) and minerals (iron, calcium) maintain enzyme function and immune defense."
    },
    {
        "id": 19,
        "question": "Why is eating a balanced, diverse diet of regional Indian dishes healthy?",
        "options": [
            "It ensures our body receives all required nutrients in optimal proportions",
            "It only contains sugar",
            "It avoids all vegetables",
            "It is required by law"
        ],
        "correct": 0,
        "solution": "A balanced diet containing cereals, lentils, vegetables, and dairy fulfills the body's complete spectrum of nutritional needs."
    },
    {
        "id": 20,
        "question": "What is the primary role of roots in a growing plant?",
        "options": [
            "To anchor the plant securely and absorb water and dissolved minerals from soil",
            "To catch flying insects",
            "To produce flowers",
            "To reflect sunlight"
        ],
        "correct": 0,
        "solution": "Roots anchor the plant firmly in the soil and absorb moisture and essential mineral nutrients for upward transport."
    },

    # Q21 - Q30 (Slide 19)
    {
        "id": 21,
        "question": "What natural engine drives the global water cycle?",
        "options": ["Solar energy (heat from the Sun)", "Underground ocean pumps", "Human water taps", "Volcanic smoke"],
        "correct": 0,
        "solution": "Solar thermal radiation heats surface water across oceans and continents, powering evaporation and cloud formation."
    },
    {
        "id": 22,
        "question": "What happens when rising water vapor encounters colder air high in the sky?",
        "options": [
            "It condenses into microscopic liquid water droplets to form clouds",
            "It catches fire",
            "It turns into stone",
            "It escapes into outer space"
        ],
        "correct": 0,
        "solution": "Condensation transforms cooling gaseous water vapor into tiny liquid water droplets suspended as clouds."
    },
    {
        "id": 23,
        "question": "What are the three common physical states of water?",
        "options": [
            "Solid (ice), liquid (water), and gas (steam/vapor)",
            "Hot, warm, and cool",
            "Sweet, salty, and sour",
            "Hard, soft, and rough"
        ],
        "correct": 0,
        "solution": "Water exists in solid (ice), liquid (liquid water), and gaseous (steam/vapor) states depending on temperature."
    },
    {
        "id": 24,
        "question": "At what temperature does liquid water freeze into solid ice at standard pressure?",
        "options": ["0 °C", "50 °C", "100 °C", "−100 °C"],
        "correct": 0,
        "solution": "The standard freezing point of pure liquid water is 0 °C."
    },
    {
        "id": 25,
        "question": "Why is water vapor invisible, while clouds and steam clouds are visible?",
        "options": [
            "Water vapor is a true gas of individual molecules; clouds consist of clustered liquid droplets that scatter light",
            "Water vapor is black",
            "Clouds are made of cotton",
            "Steam is a solid rock"
        ],
        "correct": 0,
        "solution": "Individual gaseous water vapor molecules are microscopic and transparent, whereas condensed liquid droplets in clouds scatter visible light."
    },
    {
        "id": 26,
        "question": "Why is human touch an unreliable tool for measuring absolute temperature?",
        "options": [
            "Because skin only perceives relative heat flow compared to recent exposure",
            "Because human skin cannot touch liquids",
            "Because everyone has different colored skin",
            "Because hands are always at 0 °C"
        ],
        "correct": 0,
        "solution": "Sensory thermal receptors signal whether heat is entering or leaving the skin relative to recent temperature, making touch subjective."
    },
    {
        "id": 27,
        "question": "What property makes metals ideal for fabricating cooking pots and electric cables?",
        "options": [
            "They are excellent conductors of thermal heat and electricity",
            "They are lightweight like feathers",
            "They are transparent",
            "They melt in warm water"
        ],
        "correct": 0,
        "solution": "Metals possess free conduction electrons that rapidly transfer thermal energy and electric charge."
    },
    {
        "id": 28,
        "question": "Which of the following materials is NON-MAGNETIC?",
        "options": ["Plastic bottle cap", "Iron nail", "Steel paperclip", "Nickel coin"],
        "correct": 0,
        "solution": "Plastic is a non-magnetic organic polymer that experiences no magnetic attraction."
    },
    {
        "id": 29,
        "question": "Why are copper electric wires wrapped with outer plastic coatings?",
        "options": [
            "Plastic is an electrical insulator that prevents accidental electric shocks",
            "Plastic makes the wire heavier",
            "Plastic speeds up electricity",
            "To make the wire magnetic"
        ],
        "correct": 0,
        "solution": "Plastic does not conduct electricity (an insulator), protecting users from electrical contact and preventing short circuits."
    },
    {
        "id": 30,
        "question": "What is our Sun?",
        "options": [
            "A medium-sized star at the gravitational center of our solar system",
            "A giant burning coal mountain",
            "Earth's natural moon",
            "A cosmic planet"
        ],
        "correct": 0,
        "solution": "The Sun is a glowing star composed primarily of hydrogen and helium undergoing nuclear fusion."
    },

    # Q31 - Q40 (Slide 20)
    {
        "id": 31,
        "question": "What is the correct sequential order of the steps in the Scientific Method?",
        "options": [
            "Observe → Question → Hypothesize → Experiment → Analyze",
            "Experiment → Guess → Observe → Conclusion",
            "Analyze → Memorize → Write → Question",
            "Guess → Conclude → Observe → Forget"
        ],
        "correct": 0,
        "solution": "Scientific inquiry systematically moves from Observation to Questioning, formulating a Hypothesis, Experimenting, and Analyzing data."
    },
    {
        "id": 32,
        "question": "In a controlled experiment, why must scientists change only ONE variable at a time?",
        "options": [
            "To be confident that the observed outcome is caused solely by that single changed factor",
            "Because scientists are lazy",
            "So that all experiments fail",
            "To save lab equipment"
        ],
        "correct": 0,
        "solution": "Isolating a single independent variable ensures that any observed change in the dependent variable is caused by that factor alone."
    },
    {
        "id": 33,
        "question": "A student tests if salt water freezes faster than plain water. What is the variable being tested?",
        "options": [
            "The presence of dissolved salt in the water",
            "The shape of the freezer",
            "The color of the kitchen walls",
            "The time of day"
        ],
        "correct": 0,
        "solution": "The presence or absence of salt is the independent variable being tested for its effect on freezing rate."
    },
    {
        "id": 34,
        "question": "When a ballpoint pen stops writing, what is an example of an initial observation?",
        "options": [
            "Noticing that ink fails to appear on the paper when writing",
            "Assuming the manufacturer is bad",
            "Throwing the pen out the window",
            "Buying five new pens"
        ],
        "correct": 0,
        "solution": "Observing that no ink mark is transferred to the sheet is the factual, raw observation."
    },
    {
        "id": 35,
        "question": "What constitutes an experimental test for the hypothesis: 'The pen refill is completely out of ink'?",
        "options": [
            "Unscrewing the pen barrel to directly inspect the ink column inside the refill",
            "Sniffing the outside of the pen",
            "Wishing the pen would write",
            "Weighing the notebook"
        ],
        "correct": 0,
        "solution": "Direct visual inspection of the ink reservoir provides verifiable evidence to support or refute the hypothesis."
    },
    {
        "id": 36,
        "question": "Why is an experiment that disproves a hypothesis still considered a scientific success?",
        "options": [
            "It eliminates an incorrect possibility and points the investigation toward new, better ideas",
            "It proves the scientist should retire",
            "It saves time by ending science",
            "It proves that nature is dishonest"
        ],
        "correct": 0,
        "solution": "Falsifying a hypothesis provides conclusive negative data, narrowing down the truth and preventing wasted efforts."
    },
    {
        "id": 37,
        "question": "How does an electrician use the scientific method when an entire room's lights go dark?",
        "options": [
            "They check the central circuit breaker first, then inspect individual switches and bulbs systematically",
            "They immediately smash the light fixtures",
            "They blame the sunset",
            "They wait for morning"
        ],
        "correct": 0,
        "solution": "The electrician performs logical step-by-step diagnostic tests from the power source down to the individual fixtures."
    },
    {
        "id": 38,
        "question": "What does a pressure cooker whistle indicate to a cook in the kitchen?",
        "options": [
            "Steam pressure inside has reached the threshold to lift the weight valve",
            "The food is poisoned",
            "The stove has run out of gas",
            "It is time to eat"
        ],
        "correct": 0,
        "solution": "The whistle releases excess steam pressure when internal boiling creates sufficient force to lift the safety weight."
    },
    {
        "id": 39,
        "question": "What characterizes a truly scientifically literate person (a 'whys' person)?",
        "options": [
            "Someone who asks evidence-based questions, tests claims, and remains curious throughout life",
            "Someone who believes everything they read on the internet",
            "Someone who argues without evidence",
            "Someone who memorizes entire dictionaries"
        ],
        "correct": 0,
        "solution": "A 'whys' person relies on evidence, critical thinking, open curiosity, and continuous learning."
    },
    {
        "id": 40,
        "question": "What is the ultimate goal of the ongoing journey of science?",
        "options": [
            "To understand the natural universe, solve human problems, and foster wonder and harmony",
            "To memorize all existing facts and stop asking questions",
            "To replace nature with machines",
            "To win trophies"
        ],
        "correct": 0,
        "solution": "Science seeks to unravel natural truths, alleviate suffering, protect biodiversity, and elevate human understanding."
    }
]

# Verify zero raw LaTeX and zero surrogates
raw_latex_pattern = re.compile(r'\\[a-zA-Z]+')

def verify_text(text, ctx):
    matches = raw_latex_pattern.findall(text)
    if matches:
        raise ValueError(f"Found raw LaTeX in {ctx}: {set(matches)}")
    surrogates = [c for c in text if 0xD800 <= ord(c) <= 0xDFFF]
    if surrogates:
        raise ValueError(f"Found surrogates in {ctx}")

verify_text(CHAPTER_META['title'], "CHAPTER_META title")
for s in SLIDES:
    verify_text(s['title'], f"Slide {s['id']} title")
    if 'theory' in s:
        verify_text(s['theory'], f"Slide {s['id']} theory")
    if 'summary' in s:
        verify_text(s['summary'], f"Slide {s['id']} summary")
    for cp in s.get('checkpoints', []):
        verify_text(cp['question'], f"Slide {s['id']} cp question")
        verify_text(cp['explanation'], f"Slide {s['id']} cp explanation")

for q in QUIZ_QUESTIONS:
    verify_text(q['question'], f"Quiz Q{q['id']} question")
    verify_text(q['solution'], f"Quiz Q{q['id']} solution")

print("VERIFIED PASS: Zero raw LaTeX and zero surrogates in all 20 Slides and 40 Quiz Questions!")

with open(".agents/class6_science_ch1_data.py", "w", encoding="utf-8") as f:
    f.write('"""\nNCERT Class 6 Science Chapter 1: The Wonderful World of Science Data Module\n"""\n\n')
    f.write('CHAPTER_META = ' + repr(CHAPTER_META) + '\n\n')
    f.write('SLIDES = ' + repr(SLIDES) + '\n\n')
    f.write('QUIZ_QUESTIONS = ' + repr(QUIZ_QUESTIONS) + '\n')

print("Successfully wrote .agents/class6_science_ch1_data.py")
