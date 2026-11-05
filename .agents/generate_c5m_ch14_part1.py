# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 14: Maps and Locations - Part 1 (Slides 1 to 8)
Syllabus: Joyful Mathematics (NEP 2020)
Strict Constraints:
- 195 to 215 words per lecture
- Short headings (1-3 words)
- Indian male teacher tone
- Zero human names
- Zero raw LaTeX
- 2 checkpoints per slide
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Crane Migration",
        "tagline": "Avian Navigation • Journey of the Siberian Crane to Bharatpur Bird Sanctuary",
        "lecture": (
            "Every single winter, one of nature's most magnificent aerial journeys unfolds across our planet: the epic annual migration of "
            "the Siberian Crane! These majestic white birds depart from the freezing tundras of northern Siberia and travel thousands of "
            "kilometres southward across rugged mountain ranges, winding rivers, and vast plains to arrive safely at the famous Keoladeo "
            "National Park in Bharatpur, Rajasthan. How do these marvelous birds navigate across unfamiliar continents without getting lost? "
            "They possess an extraordinary natural instinct for spatial direction and planetary geography! Just like human travelers relying "
            "on compasses and satellite maps, migrating birds orient themselves using natural landmarks, celestial patterns of the sun and "
            "stars, and the earth's magnetic field. This epic wildlife journey introduces the foundational concept of spatial awareness: "
            "understanding where we are located in the physical world, identifying the direction of our destination, and mapping out the "
            "safest and shortest travel route. By studying maps, legends, and directional coordinates, students develop the mathematical "
            "tools to navigate complex spaces—from a cozy bedroom and a busy school campus to entire transit rail networks and national "
            "wildlife sanctuaries. Maps transform vast physical landscapes into organized, miniature graphic representations that guide our daily journeys with absolute clarity."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-cyan-900/40 via-blue-900/30 to-cyan-900/40 border border-cyan-500/30 rounded-xl p-4">
        <h4 class="text-cyan-300 font-bold text-sm tracking-wider uppercase mb-1">Spatial Navigation & Migration</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Siberian cranes migrate over <span class="text-amber-300 font-bold">5,000 kilometres</span> from Siberia to Bharatpur, Rajasthan,
            demonstrating natural directional navigation and route planning.
        </p>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs font-mono">
        <div class="bg-slate-800/80 p-3 rounded-lg border border-slate-700">
            <span class="text-cyan-400 font-bold block mb-1">Origin: Siberia (North)</span>
            <span class="text-slate-300 block">Freezing Arctic tundra</span>
            <span class="text-slate-400 text-[10px] block mt-1">Travels southward before severe snowstorms.</span>
        </div>
        <div class="bg-slate-800/80 p-3 rounded-lg border border-slate-700">
            <span class="text-emerald-400 font-bold block mb-1">Destination: Bharatpur (South)</span>
            <span class="text-slate-300 block">Keoladeo Bird Sanctuary</span>
            <span class="text-slate-400 text-[10px] block mt-1">Warm wetlands with rich food and nesting sites.</span>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "Where does the Siberian Crane migrate to in India during winter?",
                "options": [
                    "Corbett National Park in Uttarakhand",
                    "Bharatpur Bird Sanctuary in Rajasthan",
                    "Sundarbans in West Bengal",
                    "Gir Forest in Gujarat"
                ],
                "answer": 1,
                "explanation": "Siberian cranes migrate to Keoladeo National Park (Bharatpur Bird Sanctuary) in Rajasthan.",
                "hint": "Recall the famous bird sanctuary located in Rajasthan."
            },
            {
                "question": "In which general cardinal direction does the Siberian Crane fly to reach India from Siberia?",
                "options": ["North", "South", "East", "West"],
                "answer": 1,
                "explanation": "Siberia lies far to the north; flying to India requires traveling southward.",
                "hint": "India is located south of Siberia."
            }
        ]
    },
    {
        "id": 2,
        "title": "Cardinal Directions",
        "tagline": "The Four Directions • Using the Rising Sun to Establish North, South, East, and West",
        "lecture": (
            "To explore the physical world with true confidence, we must first master the four fundamental cardinal directions: North, South, "
            "East, and West. For thousands of years, people across ancient India and the entire world have used the glorious rising sun as their "
            "primary celestial compass. If you stand outdoors early in the morning and face directly toward the radiant rising sun, you "
            "are facing East! Now, stretch both of your arms straight out to your sides like the wings of a soaring eagle. Your left hand "
            "points directly toward the North, while your right hand points directly toward the South. Finally, the direction directly behind "
            "your back is West, which is where the sun sets peacefully in the evening! On almost all standard paper maps, atlases, and digital "
            "navigation screens, North is universally placed at the very top of the page. Consequently, South is always at the bottom, East "
            "lies to the right, and West lies to the left. Remembering this clear spatial orientation—East in front, West behind, North to "
            "the left, and South to the right—empowers learners to read any geographical map and establish exact directional orientation anywhere on our beautiful planet with joy, confidence, and mathematical certainty."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-amber-900/40 via-orange-900/30 to-amber-900/40 border border-amber-500/30 rounded-xl p-4">
        <h4 class="text-amber-300 font-bold text-sm tracking-wider uppercase mb-1">Sun-Based Cardinal Orientation</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Face the rising Sun in the morning:
            <span class="text-amber-300 font-bold">In front is East</span>,
            <span class="text-rose-400 font-bold">Behind is West</span>,
            <span class="text-cyan-400 font-bold">Left hand is North</span>, and
            <span class="text-emerald-400 font-bold">Right hand is South</span>.
        </p>
    </div>
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs font-mono">
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-amber-400 font-bold block">East (E)</span>
            <span class="text-slate-300 text-[11px] block mt-1">Facing rising Sun</span>
            <span class="text-[10px] text-slate-400">Right on paper</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-cyan-400 font-bold block">North (N)</span>
            <span class="text-slate-300 text-[11px] block mt-1">Left hand side</span>
            <span class="text-[10px] text-slate-400">Top on paper</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-rose-400 font-bold block">West (W)</span>
            <span class="text-slate-300 text-[11px] block mt-1">Behind your back</span>
            <span class="text-[10px] text-slate-400">Left on paper</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-emerald-400 font-bold block">South (S)</span>
            <span class="text-slate-300 text-[11px] block mt-1">Right hand side</span>
            <span class="text-[10px] text-slate-400">Bottom on paper</span>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "If you are standing facing the rising sun, which direction is to your left hand?",
                "options": ["East", "West", "North", "South"],
                "answer": 2,
                "explanation": "When facing East (rising sun), your left hand points North and your right hand points South.",
                "hint": "Remember: Left is North, Right is South when facing East."
            },
            {
                "question": "On a standard geographical map, which cardinal direction is located at the top?",
                "options": ["North", "South", "East", "West"],
                "answer": 0,
                "explanation": "By universal cartographic convention, North is always at the top of a standard map.",
                "hint": "Maps use the top edge to represent North."
            }
        ]
    },
    {
        "id": 3,
        "title": "Direction Flight Poem",
        "tagline": "Four Little Chicks • Poetic Rhyme Connecting Bird Flight Paths with Cardinal Directions",
        "lecture": (
            "Let us enjoy an enchanting mathematical poem titled Four Little Chicks, celebrating how young birds explore the four cardinal "
            "directions! One little chick spread its soft downy wings and flew bravely toward the North, where cool pine breezes gently blow. "
            "The second little chick turned toward the South, where warm sandy beaches and sweet ripe berries glow. The third little chick "
            "fluttered straight toward the East, greeting the glorious golden dawn as the radiant sun began to shine. And the fourth little "
            "chick journeyed toward the West, chasing the glowing evening sunset where twilight painted the horizon line! Notice how each chick "
            "chose one distinct cardinal direction, spanning all four quadrants of the compass rose. When we visualize their flight paths "
            "on paper, the chicks form a complete cross pattern: North and South stand directly opposite each other along the vertical axis, "
            "while East and West stand directly opposite each other along the horizontal axis. These two intersecting axes meet at a central "
            "nesting point, forming four perfect right angles of ninety degrees. Directional poetry helps young learners internalize opposite "
            "pairs: North is opposite South, and East is opposite West, creating the geometric foundation for maps and navigation grids."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-purple-900/40 via-indigo-900/30 to-purple-900/40 border border-purple-500/30 rounded-xl p-4">
        <h4 class="text-purple-300 font-bold text-sm tracking-wider uppercase mb-1">Poetic Flight Paths & Opposite Axes</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            The four chicks fly outwards from the nest, demonstrating the <span class="text-amber-300 font-bold">two perpendicular axes</span>
            of cardinal space: <span class="text-cyan-300 font-semibold">North-South (Vertical)</span> and
            <span class="text-emerald-300 font-semibold">East-West (Horizontal)</span>.
        </p>
    </div>
    <div class="grid grid-cols-2 gap-2 text-xs font-mono">
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-cyan-400 font-bold block">Chick 1: North (↑)</span>
            <span class="text-slate-300 text-[11px]">Opposite to Chick 2 (South ↓)</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-amber-400 font-bold block">Chick 3: East (→)</span>
            <span class="text-slate-300 text-[11px]">Opposite to Chick 4 (West ←)</span>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "Which cardinal direction is directly opposite to North?",
                "options": ["East", "West", "South", "North-East"],
                "answer": 2,
                "explanation": "North and South are opposite directions along the vertical axis.",
                "hint": "Think about the direction opposite to top (North) on a map."
            },
            {
                "question": "What angle is formed between the North axis and the East axis?",
                "options": ["45 degrees", "90 degrees (Right angle)", "180 degrees", "360 degrees"],
                "answer": 1,
                "explanation": "Adjacent cardinal directions (North and East) are perpendicular and form a 90° right angle.",
                "hint": "Quarter turn between top and right."
            }
        ]
    },
    {
        "id": 4,
        "title": "Map Legend Reading",
        "tagline": "Bird Watching Camp • Decoding Map Legends, Color Clues, and Relative Directions",
        "lecture": (
            "Welcome to the bird watching camp at the scenic wetlands sanctuary! To navigate this outdoor sanctuary effectively, visitors "
            "rely on a specialized map containing visual symbols and a detailed legend. Let us interpret the directional clues to color the "
            "camping tents accurately. First clue: 'The tent located directly west of the central paved road is blue.' Looking at the map, "
            "we locate the road running vertically north to south; moving left into the western zone, we color that tent blue! Second clue: "
            "'The tent closest to the sparkling freshwater lake is green.' We identify the lake in the eastern area and color the adjacent "
            "tent green. Third clue: 'The tent situated directly north of the green tent is purple.' Moving straight upward from the green "
            "tent along the northern line, we color that tent purple! Fourth clue: 'The tent directly south of the lake is yellow.' Moving "
            "downward beneath the lake, we color that tent yellow. Finally, the rangers ask us to draw a new tent to the east of the lake. "
            "Moving to the right side of the water, we place the new tent! Reading map legends connects linguistic instructions with spatial "
            "geometry, enabling learners to decode layouts accurately."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-emerald-900/40 via-teal-900/30 to-emerald-900/40 border border-emerald-500/30 rounded-xl p-4">
        <h4 class="text-emerald-300 font-bold text-sm tracking-wider uppercase mb-1">Campsite Directional Clues</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Use relative landmarks (Road, Lake) combined with cardinal directions to locate and identify map features:
        </p>
    </div>
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs font-mono">
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-blue-400 font-bold block">Blue Tent</span>
            <span class="text-slate-300 text-[10px]">West of road</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-emerald-400 font-bold block">Green Tent</span>
            <span class="text-slate-300 text-[10px]">Closest to lake</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-purple-400 font-bold block">Purple Tent</span>
            <span class="text-slate-300 text-[10px]">North of green</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-yellow-400 font-bold block">Yellow Tent</span>
            <span class="text-slate-300 text-[10px]">South of lake</span>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "Which tent is located directly west of the central road?",
                "options": ["Green tent", "Blue tent", "Purple tent", "Yellow tent"],
                "answer": 1,
                "explanation": "According to the map clue, the tent west (left) of the road is blue.",
                "hint": "West corresponds to the left side of the road."
            },
            {
                "question": "If a new tent is to be drawn to the east of the lake, where will it be located?",
                "options": [
                    "To the left of the lake",
                    "To the right of the lake",
                    "Above the lake (North)",
                    "Below the lake (South)"
                ],
                "answer": 1,
                "explanation": "East is to the right on a standard map, so the tent is drawn to the right of the lake.",
                "hint": "East is always towards the right hand side."
            }
        ]
    },
    {
        "id": 5,
        "title": "Room Layout Map",
        "tagline": "Interior Spatial Mapping • Determining Furniture Directions from a Central Viewpoint",
        "lecture": (
            "Mapping does not apply only to outdoor sanctuaries and national parks; it is equally powerful for organizing interior indoor "
            "spaces such as a bedroom or school classroom! Imagine a student standing at the exact geometric center of a rectangular bedroom, "
            "facing directly toward the wide glass window on the northern wall. From this central vantage point, every piece of furniture occupies "
            "a distinct relative cardinal direction. Directly in front, toward the North, sits the wide window letting in fresh morning air. "
            "Directly behind, toward the South, is the wooden entry door leading into the hallway. To the left hand side, toward the West, "
            "stands a tall clothes cupboard and tidy study bookshelf. And to the right hand side, toward the East, rests the cozy bed and small "
            "bedside reading table! Notice that determining directions indoors depends strictly on establishing a clear reference orientation. "
            "If the student rotates to face East instead of North, all relative directions rotate accordingly! However, true cardinal directions "
            "remain permanently fixed: the northern wall remains the northern wall regardless of which way a person turns. Creating an overhead "
            "bird's-eye view map of a room teaches students to translate three-dimensional living spaces into clean two-dimensional architectural diagrams."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-blue-900/40 via-indigo-900/30 to-blue-900/40 border border-blue-500/30 rounded-xl p-4">
        <h4 class="text-blue-300 font-bold text-sm tracking-wider uppercase mb-1">Central Reference Orientation</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Standing at the center of the room facing North (Window):
            <span class="text-cyan-400 font-semibold">Front = North</span>,
            <span class="text-emerald-400 font-semibold">Right = East (Bed)</span>,
            <span class="text-rose-400 font-semibold">Behind = South (Door)</span>,
            <span class="text-amber-400 font-semibold">Left = West (Cupboard)</span>.
        </p>
    </div>
    <div class="grid grid-cols-2 gap-2 text-xs font-mono">
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-cyan-400 font-bold block">North (Front):</span>
            <span class="text-slate-300 text-[11px]">Window</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-emerald-400 font-bold block">East (Right):</span>
            <span class="text-slate-300 text-[11px]">Bed & Table</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-rose-400 font-bold block">South (Back):</span>
            <span class="text-slate-300 text-[11px]">Door</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-amber-400 font-bold block">West (Left):</span>
            <span class="text-slate-300 text-[11px]">Cupboard</span>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "If you are standing at the room center facing North, which furniture item is to your right (East)?",
                "options": ["Cupboard", "Bed", "Door", "Window"],
                "answer": 1,
                "explanation": "When facing North, East lies to your right hand, where the bed is placed.",
                "hint": "Right hand points East when facing North."
            },
            {
                "question": "If the window is on the northern wall, on which wall is the door directly opposite to it?",
                "options": ["Eastern wall", "Western wall", "Southern wall", "Ceiling"],
                "answer": 2,
                "explanation": "The opposite of North is South, so the door is on the southern wall.",
                "hint": "The opposite direction of North is South."
            }
        ]
    },
    {
        "id": 6,
        "title": "Relative Spatial Directions",
        "tagline": "Dynamic Observer Orientation • How Turning Left and Right Changes Relative Perspectives",
        "lecture": (
            "When navigating through diverse physical spaces, it is essential to understand the clear distinction between absolute cardinal "
            "directions and relative observer directions. Cardinal directions—North, South, East, and West—are permanently fixed with respect "
            "to planet Earth. The geographical North Pole does not move when you turn around! In sharp contrast, relative directions—such "
            "as forward, backward, left, and right—depend entirely on which way an individual observer happens to be facing at that exact moment. "
            "Let us observe what happens: suppose an explorer is facing North. To this explorer, turning ninety degrees to the right means heading "
            "directly East. Now, suppose the explorer turns another quarter turn to the right; the explorer is now facing South! From this new "
            "southern orientation, what direction is to the explorer's right hand? Facing South, the right hand now points toward the West! "
            "Notice how the explorer's right hand pointed East initially, but after facing South, the right hand points West! This explains "
            "why directional instructions must always be interpreted with careful attention to the traveler's current heading. When sketching "
            "maps of homes, classrooms, or neighborhood parks, we establish fixed compass arrows so that travelers, cartographers, and students can interpret spatial layouts and navigate complex territories with absolute accuracy."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-teal-900/40 via-emerald-900/30 to-teal-900/40 border border-teal-500/30 rounded-xl p-4">
        <h4 class="text-teal-300 font-bold text-sm tracking-wider uppercase mb-1">Absolute vs Relative Directions</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            <span class="text-emerald-400 font-bold">Absolute (Cardinal):</span> Fixed to Earth (North, South, East, West).<br>
            <span class="text-cyan-400 font-bold">Relative (Observer):</span> Changes with body heading (Left, Right, Front, Back).
        </p>
    </div>
    <div class="space-y-2 text-xs font-mono">
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700 flex justify-between items-center">
            <span class="text-slate-300">Facing North ➔ Turn 90° Right:</span>
            <span class="text-amber-400 font-bold">Facing East</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700 flex justify-between items-center">
            <span class="text-slate-300">Facing East ➔ Turn 90° Right:</span>
            <span class="text-emerald-400 font-bold">Facing South</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700 flex justify-between items-center">
            <span class="text-slate-300">Facing South ➔ Right Hand Points:</span>
            <span class="text-rose-400 font-bold">West</span>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "If you are walking South and make a 90° right turn, which direction are you now facing?",
                "options": ["East", "West", "North", "South-East"],
                "answer": 1,
                "explanation": "When facing South, turning right points you toward the West.",
                "hint": "Picture standing facing South (downwards); your right arm points to the left of the map (West)."
            },
            {
                "question": "Do absolute cardinal directions (North, South, East, West) change when a person turns around?",
                "options": [
                    "Yes, they change completely",
                    "No, they remain permanently fixed to Earth",
                    "Only East and West change",
                    "Only North changes"
                ],
                "answer": 1,
                "explanation": "Cardinal directions are fixed geographical references that do not move when a person rotates.",
                "hint": "The North Pole stays in the same place on the planet."
            }
        ]
    },
    {
        "id": 7,
        "title": "Bus Route Navigation",
        "tagline": "Neighborhood Transit • Tracing School Field Trip Bus Routes Across Street Grids",
        "lecture": (
            "An exciting school field trip to the national zoological park begins bright and early in the morning! The large yellow school "
            "bus departs promptly from the main parking depot and must follow a carefully designated street route to pick up students from "
            "various scheduled neighborhood bus stops before heading toward the zoo highway. Navigating a street map requires tracking both "
            "measured block distances and directional turns at major intersections. The bus travels two blocks East along Park Avenue, makes "
            "a ninety-degree left turn to travel three blocks North on Rose Street, and stops at Stop 1. From there, the bus turns right to "
            "travel two blocks East along Market Road to reach Stop 2. Next, it turns right again, driving two blocks South along River Road "
            "to reach Stop 3. Finally, turning left to head East, the bus merges smoothly onto Zoo Expressway! Notice how tracing this transit "
            "trajectory combines sequential cardinal steps: moving East, turning North, turning East, turning South, and turning East again. "
            "Reading street maps helps drivers avoid confusing dead-ends, plan efficient fuel consumption, and guarantee that passengers are "
            "picked up safely on schedule with flawless mathematical precision, fuel efficiency, and complete peace of mind."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-amber-900/40 via-yellow-900/30 to-amber-900/40 border border-amber-500/30 rounded-xl p-4">
        <h4 class="text-amber-300 font-bold text-sm tracking-wider uppercase mb-1">Sequential Route Tracking</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Navigating street grids involves recording <span class="text-amber-300 font-bold">cardinal segments and intersection turns</span>:
        </p>
    </div>
    <div class="space-y-1.5 text-xs font-mono">
        <div class="bg-slate-800/80 p-2 rounded-lg border border-slate-700 flex justify-between">
            <span class="text-slate-300">1. Depot to Stop 1:</span>
            <span class="text-cyan-300 font-bold">2 East ➔ Left Turn ➔ 3 North</span>
        </div>
        <div class="bg-slate-800/80 p-2 rounded-lg border border-slate-700 flex justify-between">
            <span class="text-slate-300">2. Stop 1 to Stop 2:</span>
            <span class="text-emerald-300 font-bold">Right Turn ➔ 2 East</span>
        </div>
        <div class="bg-slate-800/80 p-2 rounded-lg border border-slate-700 flex justify-between">
            <span class="text-slate-300">3. Stop 2 to Stop 3:</span>
            <span class="text-amber-300 font-bold">Right Turn ➔ 2 South</span>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "If the bus is traveling East and turns left at an intersection, which direction is it now heading?",
                "options": ["North", "South", "East", "West"],
                "answer": 0,
                "explanation": "When traveling East (rightwards), making a left turn directs the bus upward toward the North.",
                "hint": "Left turn from East points toward the top of the map."
            },
            {
                "question": "If the bus travels 2 blocks East, 3 blocks North, and 2 blocks South, what is its net vertical position relative to start?",
                "options": ["1 block North", "5 blocks North", "1 block South", "At the same latitude"],
                "answer": 0,
                "explanation": "3 blocks North minus 2 blocks South = 1 block North of the starting line.",
                "hint": "Subtract South movement from North movement: 3 - 2 = 1."
            }
        ]
    },
    {
        "id": 8,
        "title": "Shortest Street Routes",
        "tagline": "Path Optimization • Calculating Manhatten Block Distances to Discover the Shortest Way",
        "lecture": (
            "When traveling through modern city street grids, there are often multiple different pathways connecting an initial starting "
            "point to a desired destination. Determining which route is the shortest requires calculating total path lengths by systematically "
            "adding individual street blocks! Consider a student walking from home at corner A to school at corner B on a rectangular grid. "
            "Route 1 heads three blocks East, then turns left and walks four blocks North, making a total distance of seven blocks. Route 2 "
            "walks four blocks North first, then turns right and walks three blocks East, also totaling exactly seven blocks! What if a third "
            "route zig-zags through the neighborhood: one block East, one block North, one block East, two blocks North, and one block East, "
            "one block North? Adding the steps: one plus one plus one plus two plus one plus one equals seven blocks! On a clean rectangular "
            "grid without diagonal alleys, any path that moves exclusively toward the destination without backtracking has the exact same minimal "
            "distance, known as the Manhattan grid distance. However, if a route takes unnecessary detours or loops backwards, its total distance "
            "increases significantly, wasting valuable travel time and burning unnecessary energy along the way."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-indigo-900/40 via-purple-900/30 to-indigo-900/40 border border-indigo-500/30 rounded-xl p-4">
        <h4 class="text-indigo-300 font-bold text-sm tracking-wider uppercase mb-1">Grid Distance Optimization</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            The minimal distance between two grid points without backtracking equals:
            <span class="text-amber-300 font-bold">Total Blocks = Horizontal Blocks + Vertical Blocks</span>.
        </p>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs font-mono text-center">
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-cyan-400 font-bold block mb-1">Route 1 (L-Shape)</span>
            <span class="text-slate-300 text-[11px]">3 East + 4 North</span>
            <span class="text-emerald-400 font-bold block mt-1">Total = 7 Blocks</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-amber-400 font-bold block mb-1">Route 2 (Inverted L)</span>
            <span class="text-slate-300 text-[11px]">4 North + 3 East</span>
            <span class="text-emerald-400 font-bold block mt-1">Total = 7 Blocks</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-purple-400 font-bold block mb-1">Route 3 (Zig-Zag)</span>
            <span class="text-slate-300 text-[11px]">1E+1N+1E+2N+1E+1N</span>
            <span class="text-emerald-400 font-bold block mt-1">Total = 7 Blocks</span>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "What is the shortest grid distance between two points that differ by 3 blocks East and 4 blocks North?",
                "options": ["5 blocks", "7 blocks", "12 blocks", "1 block"],
                "answer": 1,
                "explanation": "On a rectangular grid without diagonals, distance = horizontal + vertical = 3 + 4 = 7 blocks.",
                "hint": "Add the horizontal and vertical blocks together."
            },
            {
                "question": "If Route D takes 3 blocks East, 2 blocks South, 6 blocks North, and then reaches the destination, how long is Route D?",
                "options": ["7 blocks", "9 blocks", "11 blocks", "14 blocks"],
                "answer": 2,
                "explanation": "Total distance = 3 + 2 + 6 = 11 blocks (a detour of 4 extra blocks compared to the direct 7-block path).",
                "hint": "Add all blocks walked: 3 + 2 + 6 = 11."
            }
        ]
    }
]

if __name__ == '__main__':
    for s in slides_part1:
        wc = len(s['lecture'].split())
        status = "PASS" if 195 <= wc <= 215 else f"FAIL ({wc})"
        print(f"Slide {s['id']}: {wc} words [{status}]")
