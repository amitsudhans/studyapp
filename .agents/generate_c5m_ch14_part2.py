# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 14: Maps and Locations - Part 2 (Slides 9 to 16)
Syllabus: Joyful Mathematics (NEP 2020)
Strict Constraints:
- 195 to 215 words per lecture
- Short headings (1-3 words)
- Indian male teacher tone
- Zero human names
- Zero raw LaTeX
- 2 checkpoints per slide
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Metro Network Map",
        "tagline": "Urban Transit Systems • Reading Color-Coded Lines and Interchange Hubs on Rail Networks",
        "lecture": (
            "Modern bustling metropolitan cities across the world rely heavily on intricate public rapid transit networks, such as the famous "
            "world-class Delhi Metro! To help millions of daily commuters travel smoothly and comfortably without confusion, transit engineers "
            "design highly specialized schematic network maps. Instead of depicting actual curved geographical terrain, a modern transit map "
            "uses simplified straight lines, bold distinct colors, and clear standardized symbols that can be understood in seconds. Each major "
            "subway route is represented by a unique vivid color: the Yellow Line connects northern districts to southern tech corridors, the "
            "Blue Line crosses horizontally across bustling east and west suburbs, the Red Line serves northern historical sectors, and the "
            "Violet Line links central heritage gates to southern industrial towns! Along these colorful transit corridors, specific stations "
            "feature prominent circular ring symbols or interlocking dual circles. These are vital interchange stations, where passengers can "
            "step off one train and board a completely different line without leaving the station premises! For example, Kashmere Gate is a "
            "major triple-interchange hub connecting three different lines. Reading transit legends, identifying junction nodes, and recognizing "
            "color codes enable students to navigate complex urban transportation systems independently, efficiently, and with complete mathematical confidence."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-red-900/40 via-yellow-900/30 to-blue-900/40 border border-slate-700 rounded-xl p-4">
        <h4 class="text-amber-300 font-bold text-sm tracking-wider uppercase mb-1">Color-Coded Transit System</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Metro transit maps use <span class="text-cyan-300 font-semibold">color codes</span> for lines and
            <span class="text-amber-300 font-bold">dual-circle icons</span> for interchange stations.
        </p>
    </div>
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs font-mono">
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-yellow-500/40">
            <span class="text-yellow-400 font-bold block">Yellow Line</span>
            <span class="text-slate-300 text-[10px]">North ↔ South</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-blue-500/40">
            <span class="text-blue-400 font-bold block">Blue Line</span>
            <span class="text-slate-300 text-[10px]">East ↔ West</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-red-500/40">
            <span class="text-red-400 font-bold block">Red Line</span>
            <span class="text-slate-300 text-[10px]">North Corridor</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-purple-500/40">
            <span class="text-purple-400 font-bold block">Violet Line</span>
            <span class="text-slate-300 text-[10px]">Heritage Route</span>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "What special symbol on a transit map indicates an interchange station where you can switch lines?",
                "options": [
                    "A single solid dot",
                    "Interlocking double circles or ring icons",
                    "A dashed square",
                    "A green arrow"
                ],
                "answer": 1,
                "explanation": "Interchange stations where multiple lines meet are represented by double circles or interlocking ring icons.",
                "hint": "Look for a symbol that connects more than one line."
            },
            {
                "question": "Why do transit maps use simplified straight lines rather than exact curved road geography?",
                "options": [
                    "To save printing ink",
                    "Because metro trains only move in triangles",
                    "To make routes, stops, and transfer hubs easy to read at a glance",
                    "Because cities have no curved roads"
                ],
                "answer": 2,
                "explanation": "Schematic transit maps prioritize clear readability of stops, colors, and junctions over geographic curvature.",
                "hint": "Clarity for quick commuter decision making."
            }
        ]
    },
    {
        "id": 10,
        "title": "Metro Route Optimization",
        "tagline": "Interchange Mathematics • Comparing Alternative Metro Paths to Minimize Total Stops",
        "lecture": (
            "When traveling across an interconnected modern metro rail network, passengers frequently discover multiple distinct routes to "
            "reach their intended destination. Selecting the truly optimal travel path requires calculating and comparing the total number "
            "of intermediate stations, line transfers, and walking distances! Suppose a student wishes to travel from Qutb Minar station on the "
            "Yellow Line to Supreme Court station on the Blue Line. Let us evaluate two possible travel strategies. In Route A, the passenger "
            "rides the Yellow Line northward all the way to Rajiv Chowk interchange station, passing through thirteen stations, and then "
            "switches onto the Blue Line to travel two stops east to Supreme Court, totaling fifteen stops and only one transfer. In Route B, "
            "the passenger rides just three stops to Hauz Khas, switches to the Magenta Line for five stops to Botanical Garden, and then transfers "
            "to the Blue Line heading west to Supreme Court! While Route B connects three lines, Route A requires only one single train transfer "
            "and significantly less walking across crowded interchange corridors. Analyzing metro itineraries teaches students real-world "
            "mathematical optimization: we weigh total stop counts, transfer waiting times, and directional flow to choose the most efficient journey."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-blue-900/40 via-indigo-900/30 to-blue-900/40 border border-blue-500/30 rounded-xl p-4">
        <h4 class="text-blue-300 font-bold text-sm tracking-wider uppercase mb-1">Route Comparison: Qutb Minar to Supreme Court</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Compare transfer complexity and total intermediate stops to choose the optimal commute:
        </p>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs font-mono">
        <div class="bg-slate-800/80 p-3 rounded-lg border border-slate-700">
            <span class="text-emerald-400 font-bold block mb-1">Route A (Via Rajiv Chowk)</span>
            <span class="text-slate-300 text-[11px] block">Yellow Line (13 stops) ➔ Blue Line (2 stops)</span>
            <span class="text-amber-300 text-[11px] font-bold block mt-1">Total: 15 Stops • Only 1 Transfer</span>
        </div>
        <div class="bg-slate-800/80 p-3 rounded-lg border border-slate-700">
            <span class="text-cyan-400 font-bold block mb-1">Route B (Via Magenta Line)</span>
            <span class="text-slate-300 text-[11px] block">Yellow ➔ Magenta ➔ Blue Line</span>
            <span class="text-slate-400 text-[11px] block mt-1">Total: 16 Stops • 2 Transfers (More walking!)</span>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "Why is Route A (via Rajiv Chowk) preferred over Route B for this journey?",
                "options": [
                    "Route A is free of cost",
                    "Route A requires only 1 train transfer compared to 2 transfers in Route B",
                    "Route A does not use metro trains",
                    "Route B has no train tracks"
                ],
                "answer": 1,
                "explanation": "Route A requires only 1 transfer at Rajiv Chowk, saving walking time and transfer waiting delays.",
                "hint": "Fewer transfers generally mean a faster, simpler trip."
            },
            {
                "question": "At which major interchange station does Route A switch from the Yellow Line to the Blue Line?",
                "options": ["Hauz Khas", "Central Secretariat", "Rajiv Chowk", "Kashmere Gate"],
                "answer": 2,
                "explanation": "Rajiv Chowk is the premier central interchange station between the Yellow Line and Blue Line in Delhi.",
                "hint": "The central crossroads of Yellow and Blue lines."
            }
        ]
    },
    {
        "id": 11,
        "title": "School Map Symbols",
        "tagline": "Cartographic Legend Creation • Designing Standardized Icons for Campus Architecture",
        "lecture": (
            "When creating a detailed map of our own school campus, drawing every single leaf, brick, and classroom doorway realistically "
            "would make the paper overcrowded, confusing, and impossible to decipher! Professional cartographers solve this challenge by "
            "inventing a standardized map key, which is also commonly called a map legend. A map key replaces complex physical structures with "
            "clean, intuitive geometric symbols and vivid colors. Let us examine the official school cartography palette! A sturdy solid "
            "rectangle represents the main school Building; a double parallel gap indicates the grand Entrance Gate; a small circle with a "
            "cross stands for the clean drinking Water Tank; a dashed boundary line denotes the outer Security Fence; a solid thick outline "
            "marks the brick Boundary Wall; a dotted winding strip traces the gravel Footpath; a tiny brown rectangle represents a garden Bench; "
            "a flowering cluster symbolizes the Botanical Garden; and a cheerful green canopy icon marks an ancient Banyan Tree! By assigning "
            "a distinct, unmistakable symbol to each real-world feature, anyone holding the school map can immediately identify locations, "
            "calculate distances, and explore the campus grounds with effortless clarity, remarkable consistency, complete peace of mind, and absolute spatial accuracy on every field journey."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-emerald-900/40 via-teal-900/30 to-emerald-900/40 border border-emerald-500/30 rounded-xl p-4">
        <h4 class="text-emerald-300 font-bold text-sm tracking-wider uppercase mb-1">Standardized School Map Legend</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Cartographic symbols replace real-world objects with clean visual icons:
        </p>
    </div>
    <div class="grid grid-cols-3 sm:grid-cols-6 gap-2 text-center text-xs font-mono">
        <div class="bg-slate-800/80 p-2 rounded-lg border border-slate-700">
            <span class="text-cyan-400 font-bold block text-base">🏫</span>
            <span class="text-[10px] text-slate-300">Building</span>
        </div>
        <div class="bg-slate-800/80 p-2 rounded-lg border border-slate-700">
            <span class="text-amber-400 font-bold block text-base">🚪</span>
            <span class="text-[10px] text-slate-300">Gate</span>
        </div>
        <div class="bg-slate-800/80 p-2 rounded-lg border border-slate-700">
            <span class="text-blue-400 font-bold block text-base">🚰</span>
            <span class="text-[10px] text-slate-300">Water Tank</span>
        </div>
        <div class="bg-slate-800/80 p-2 rounded-lg border border-slate-700">
            <span class="text-emerald-400 font-bold block text-base">🌳</span>
            <span class="text-[10px] text-slate-300">Tree</span>
        </div>
        <div class="bg-slate-800/80 p-2 rounded-lg border border-slate-700">
            <span class="text-purple-400 font-bold block text-base">🌺</span>
            <span class="text-[10px] text-slate-300">Garden</span>
        </div>
        <div class="bg-slate-800/80 p-2 rounded-lg border border-slate-700">
            <span class="text-slate-400 font-bold block text-base">⋯</span>
            <span class="text-[10px] text-slate-300">Path</span>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "What is the primary purpose of a map key or legend?",
                "options": [
                    "To lock and unlock paper maps",
                    "To explain the meaning of symbols, colors, and markings used on the map",
                    "To show only roads and nothing else",
                    "To count how many colors were printed"
                ],
                "answer": 1,
                "explanation": "A map key explains what each symbol, line, and color represents on the map.",
                "hint": "Think of the key as a dictionary for the map."
            },
            {
                "question": "On the school map, what icon represents the water tank?",
                "options": ["A tree symbol", "A circle with water tap / tank marking", "A door symbol", "A dashed fence"],
                "answer": 1,
                "explanation": "The water tank is marked by a specialized water tank icon with clear plumbing or circle markers.",
                "hint": "Look for the symbol related to drinking water."
            }
        ]
    },
    {
        "id": 12,
        "title": "Treasure Hunt Map",
        "tagline": "Interactive Exploration • Finding Secret Clues with Map Keys and Cardinal Coordinates",
        "lecture": (
            "One of the most thrilling mathematical applications of campus cartography is organizing an interactive outdoor treasure hunt! "
            "In this lively game, a team of young explorers hides secret numbered clue tokens across the school grounds and marks their exact "
            "locations on a master campus map using colored flags and coordinates. To discover the hidden treasure, another team of students "
            "must carefully interpret the map legend, establish cardinal orientation from the central courtyard flagpole, and follow precise "
            "navigational directions across the campus. Clue one directs the seekers: 'Start at the main gate, walk thirty paces East along the "
            "perimeter wall, and inspect the base of the tallest banyan tree.' Consulting their map key, the searchers identify the banyan tree "
            "symbol, verify its eastern bearing with their magnetic compass, and locate the first silver token nestled safely in its aerial roots! "
            "Clue two instructs: 'Now head forty paces North past the herbal garden to the eastern corner of the water tank.' By systematically "
            "connecting cardinal headings, pacing distances, and map icons, the searchers solve the puzzle without taking a single wrong turn! "
            "Treasure hunts prove that spatial navigation is both an exact mathematical science and an exhilarating real-world adventure."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-amber-900/40 via-orange-900/30 to-amber-900/40 border border-amber-500/30 rounded-xl p-4">
        <h4 class="text-amber-300 font-bold text-sm tracking-wider uppercase mb-1">Treasure Hunt Navigational Protocol</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Combine <span class="text-amber-300 font-bold">landmark symbols</span>,
            <span class="text-cyan-300 font-semibold">cardinal directions</span>, and
            <span class="text-emerald-300 font-semibold">measured paces</span> to locate hidden tokens:
        </p>
    </div>
    <div class="space-y-1.5 text-xs font-mono">
        <div class="bg-slate-800/80 p-2 rounded-lg border border-slate-700 flex justify-between">
            <span class="text-slate-300">Token 1: Main Gate ➔</span>
            <span class="text-amber-300 font-bold">30 paces East to Banyan Tree</span>
        </div>
        <div class="bg-slate-800/80 p-2 rounded-lg border border-slate-700 flex justify-between">
            <span class="text-slate-300">Token 2: Banyan Tree ➔</span>
            <span class="text-cyan-300 font-bold">40 paces North to Water Tank</span>
        </div>
        <div class="bg-slate-800/80 p-2 rounded-lg border border-slate-700 flex justify-between">
            <span class="text-slate-300">Final Treasure: Water Tank ➔</span>
            <span class="text-emerald-300 font-bold">25 paces West to Garden Pavilion</span>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "What three vital pieces of information are needed to locate a hidden treasure on a map?",
                "options": [
                    "Temperature, rainfall, and wind speed",
                    "Starting landmark, cardinal direction, and distance (or pace count)",
                    "Color of shoes, time of sunset, and ruler weight",
                    "Names of birds, trees, and flowers only"
                ],
                "answer": 1,
                "explanation": "Precise navigation always requires an origin landmark, a cardinal heading, and a distance metric.",
                "hint": "Where you start, which way you face, and how far you walk."
            },
            {
                "question": "If you are at the Water Tank and walk 25 paces West, in which direction are you moving on the map?",
                "options": ["Upward (North)", "Downward (South)", "To the right (East)", "To the left (West)"],
                "answer": 3,
                "explanation": "West corresponds to moving leftwards on a standard map layout.",
                "hint": "West is always to the left hand side."
            }
        ]
    },
    {
        "id": 13,
        "title": "Grid Crawling Path",
        "tagline": "Anthill Navigation • Step-by-Step Directional Crawling on 1 cm Coordinate Paper",
        "lecture": (
            "Inside a bustling corner of the zoological park, an industrious ant departs from its underground anthill on an important daily "
            "foraging expedition! To trace the ant's precise movements across the terrain, entomologists and mathematicians record its exact "
            "trajectory along a standard one-centimetre square grid paper. The anthill sits at the bottom-left origin point. Scattered across "
            "the grid are four delicious food treats: a golden sweet laddoo, sparkling sugar crystals, a slice of bakery bread, and a crunchy "
            "red apple slice. Let us trace the ant's journey to the laddoo! From the anthill, the ant crawls two centimetres East along the "
            "bottom grid line. Next, it makes a sharp ninety-degree turn and crawls three centimetres North, reaching the golden laddoo! "
            "Recording this route in formal direction shorthand, we write: two centimetres East, three centimetres North. What if the ant then "
            "travels from the laddoo to the sugar crystals? It crawls four centimetres East and two centimetres North. By breaking continuous "
            "physical journeys into discrete centimetre segments aligned with cardinal axes, students connect geometric grid lines with coordinate "
            "distances, turning complex organic animal pathways into clean, quantifiable mathematical vectors and reliable, highly predictable navigational tracks across the entire landscape."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-amber-900/40 via-red-900/30 to-amber-900/40 border border-amber-500/30 rounded-xl p-4">
        <h4 class="text-amber-300 font-bold text-sm tracking-wider uppercase mb-1">Anthill Grid Navigation Rules</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Every grid square represents exactly <span class="text-amber-300 font-bold">1 cm × 1 cm</span>. Movements are written as
            <span class="text-cyan-300 font-semibold">Distance + Cardinal Direction</span>.
        </p>
    </div>
    <div class="grid grid-cols-2 gap-2 text-xs font-mono">
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-amber-400 font-bold block">Anthill ➔ Laddoo:</span>
            <span class="text-slate-200 text-[11px]">2 cm East, 3 cm North</span>
            <span class="text-emerald-400 text-[10px] block mt-0.5">Total = 5 cm path</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-cyan-400 font-bold block">Laddoo ➔ Sugar:</span>
            <span class="text-slate-200 text-[11px]">4 cm East, 2 cm North</span>
            <span class="text-emerald-400 text-[10px] block mt-0.5">Total = 6 cm path</span>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "If an ant moves 2 cm East and then 3 cm North on a 1 cm grid, how many total centimetres did it crawl?",
                "options": ["4 cm", "5 cm", "6 cm", "1 cm"],
                "answer": 1,
                "explanation": "2 cm East + 3 cm North = 5 cm total path length.",
                "hint": "Add the two step segments together."
            },
            {
                "question": "From the laddoo at (2, 3), which movement reaches the sugar crystals at (6, 5)?",
                "options": [
                    "4 cm East and 2 cm North",
                    "2 cm West and 4 cm South",
                    "6 cm East and 5 cm North",
                    "3 cm North and 2 cm East"
                ],
                "answer": 0,
                "explanation": "6 - 2 = 4 cm East; 5 - 3 = 2 cm North.",
                "hint": "Subtract the starting coordinates from the ending coordinates."
            }
        ]
    },
    {
        "id": 14,
        "title": "Shortest Grid Path",
        "tagline": "Ant Foraging Optimization • Comparing Multi-Segment Crawling Paths Across Food Targets",
        "lecture": (
            "Now let us examine an important mathematical puzzle regarding ant foraging optimization! Suppose our hungry ant at position "
            "origin (0, 0) wants to reach a piece of sweet bread located at grid coordinate (5, 4). The ant considers two alternative crawling "
            "trajectories along the grid lines. Path A crawls five centimetres East first, arriving at point (5, 0), and then crawls four "
            "centimetres North directly to the bread at (5, 4), covering five plus four, or nine centimetres. Path B crawls four centimetres "
            "North first to (0, 4), and then turns right to crawl five centimetres East to (5, 4), also covering four plus five, or nine "
            "centimetres. Both paths achieve the minimal Manhattan distance of nine centimetres! But now consider Path C, taken by an "
            "inexperienced ant: it crawls three centimetres East, turns North for two centimetres, crawls two centimetres West, turns North "
            "for two centimetres, and finally crawls four centimetres East! Adding these steps: three plus two plus two plus two plus four "
            "equals thirteen centimetres! Because Path C backtracked westward by two centimetres, it added four wasted centimetres of extra "
            "travel. Minimizing path lengths on grids requires eliminating backtracking and moving strictly toward target coordinate boundaries."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-teal-900/40 via-emerald-900/30 to-teal-900/40 border border-teal-500/30 rounded-xl p-4">
        <h4 class="text-teal-300 font-bold text-sm tracking-wider uppercase mb-1">Grid Route Comparison: Anthill to Bread</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Target is at coordinate <span class="text-amber-300 font-bold">(5, 4)</span>.
            Comparing direct non-backtracking routes with inefficient looping paths:
        </p>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs font-mono text-center">
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-emerald-400 font-bold block mb-1">Path A (East then North)</span>
            <span class="text-slate-300 text-[10px]">5 cm E + 4 cm N</span>
            <span class="text-emerald-300 font-bold block mt-1">9 cm (Optimal)</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-cyan-400 font-bold block mb-1">Path B (North then East)</span>
            <span class="text-slate-300 text-[10px]">4 cm N + 5 cm E</span>
            <span class="text-cyan-300 font-bold block mt-1">9 cm (Optimal)</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-rose-400 font-bold block mb-1">Path C (Backtracking)</span>
            <span class="text-slate-300 text-[10px]">3E + 2N + 2W + 2N + 4E</span>
            <span class="text-rose-400 font-bold block mt-1">13 cm (4 cm wasted!)</span>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "What is the shortest grid distance from (0, 0) to (5, 4)?",
                "options": ["7 cm", "9 cm", "11 cm", "20 cm"],
                "answer": 1,
                "explanation": "Shortest distance = horizontal displacement + vertical displacement = 5 + 4 = 9 cm.",
                "hint": "Add 5 cm (East) and 4 cm (North)."
            },
            {
                "question": "Why did Path C take 13 cm instead of the optimal 9 cm?",
                "options": [
                    "Because the grid squares shrank",
                    "Because it crawled 2 cm West (backtracking away from the destination)",
                    "Because bread moved away",
                    "Because ants move slower at night"
                ],
                "answer": 1,
                "explanation": "Crawling 2 cm West required an extra 2 cm East later, adding 4 cm of wasted distance.",
                "hint": "Backtracking forces the traveler to re-cover lost ground."
            }
        ]
    },
    {
        "id": 15,
        "title": "Zoo Coordinate Grid",
        "tagline": "Two-Dimensional Grid Systems • Standard (x, y) Ordering: Horizontal First, Vertical Second",
        "lecture": (
            "We now arrive at one of the greatest crowning jewels of mathematics: the formal two-dimensional coordinate grid system! "
            "To map out the expansive national zoological park containing hundreds of animal enclosures, cartographers divide the park into "
            "a numbered twelve-by-twelve square grid. On this coordinate map, every point is uniquely identified by an ordered pair written "
            "inside parentheses as (x, y). But how do we determine which number comes first? Mathematicians established an ironclad universal "
            "convention that must never be broken: always move horizontally first along the columns (x-axis / East), and then move vertically "
            "second along the rows (y-axis / North)! Think of it like reading a book: your eyes move from left to right first, and then move "
            "downward row by row. Or imagine entering an apartment building: you first walk along the hallway to the correct elevator column, "
            "and then ride the elevator upward to the target floor! Thus, coordinate (4, 1) means: start at the bottom-left origin (0, 0), "
            "walk four steps East along the ground, and then climb one step North! Reversing this order to (1, 4) lands on an entirely "
            "different location in the park. Master the rule: horizontal x first, vertical y second."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-blue-900/40 via-indigo-900/30 to-blue-900/40 border border-blue-500/30 rounded-xl p-4">
        <h4 class="text-blue-300 font-bold text-sm tracking-wider uppercase mb-1">Standard (x, y) Coordinate Convention</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Ordered pair <span class="text-amber-300 font-bold">(x, y)</span>:
            <span class="text-cyan-300 font-bold">x = Horizontal steps (East along columns)</span> first, followed by
            <span class="text-emerald-300 font-bold">y = Vertical steps (North along rows)</span> second.
        </p>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs font-mono">
        <div class="bg-slate-800/80 p-3 rounded-lg border border-slate-700">
            <span class="text-amber-400 font-bold block mb-1">Example: Tortoise at (4, 1)</span>
            <span class="text-slate-300 block text-[11px]">1. Move 4 units East along x-axis</span>
            <span class="text-slate-300 block text-[11px]">2. Move 1 unit North along y-axis</span>
            <span class="text-emerald-400 font-bold block mt-1">Location = (4, 1)</span>
        </div>
        <div class="bg-slate-800/80 p-3 rounded-lg border border-slate-700">
            <span class="text-rose-400 font-bold block mb-1">Common Mistake Alert!</span>
            <span class="text-slate-300 block text-[11px]">(4, 1) is NOT the same as (1, 4)!</span>
            <span class="text-slate-400 text-[10px] block mt-1">(1, 4) is 1 East, 4 North (a completely different animal enclosure).</span>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "In the standard coordinate pair (x, y), which direction do you move first from origin (0, 0)?",
                "options": [
                    "Vertically upward (North)",
                    "Horizontally to the right (East along x-axis)",
                    "Diagonally towards North-West",
                    "Backward toward West"
                ],
                "answer": 1,
                "explanation": "Standard convention requires horizontal movement along the x-axis first, then vertical movement second.",
                "hint": "Remember: x comes before y in the alphabet, and horizontal comes before vertical."
            },
            {
                "question": "What is the location of the Panda enclosure if it is 1 unit East and 1 unit North of origin?",
                "options": ["(0, 1)", "(1, 0)", "(1, 1)", "(2, 2)"],
                "answer": 2,
                "explanation": "1 unit East gives x = 1, and 1 unit North gives y = 1. The coordinate pair is (1, 1).",
                "hint": "(x, y) = (1, 1)."
            }
        ]
    },
    {
        "id": 16,
        "title": "Animal Coordinate Plotting",
        "tagline": "Park Cartography • Plotting Zoo Animals on a 12x12 Grid and Reading Exact Coordinates",
        "lecture": (
            "Let us apply our coordinate mastery to complete a comprehensive cartographic survey of the national zoological park! Across our "
            "numbered twelve-by-twelve grid system, various beloved wildlife species live in spacious natural habitats designed to mimic their "
            "native environments. Let us locate each animal with mathematical exactness! Near the bottom-left entrance, the Giant Panda resides "
            "at coordinate (1, 1). Moving eastward along row one, we find the Giant Tortoise basking peacefully at coordinate (4, 1). Continuing "
            "further east and slightly north, the spotted Deer grazes in an open meadow at coordinate (8, 3). In the central wetland lagoon, "
            "the saltwater Crocodile rests on a sandy bank at coordinate (7, 6). High up in the north-western forest sector, the majestic Lion "
            "guards its rocky den at coordinate (3, 10). And near the top-right sanctuary border, the Asian Elephant family drinks from a deep "
            "pool at coordinate (11, 11)! Notice how each animal's unique ordered pair specifies its exact spatial address with zero ambiguity. "
            "By plotting color-coded dots at intersection vertices, cartographers, wildlife biologists, and visitors maintain perfect spatial "
            "records. You now possess the complete geometric language of maps, cardinal directions, and coordinate systems to navigate our world."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-emerald-900/40 via-teal-900/30 to-emerald-900/40 border border-emerald-500/30 rounded-xl p-4">
        <h4 class="text-emerald-300 font-bold text-sm tracking-wider uppercase mb-1">Zoo Animal Coordinate Registry</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Exact 2D coordinates <span class="text-amber-300 font-bold">(Column x, Row y)</span> on the 12 × 12 park grid:
        </p>
    </div>
    <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 text-xs font-mono">
        <div class="bg-slate-800/80 p-2 rounded-lg border border-slate-700">
            <span class="text-emerald-400 font-bold block">🐼 Panda:</span>
            <span class="text-slate-300 text-[11px]">(1, 1)</span>
        </div>
        <div class="bg-slate-800/80 p-2 rounded-lg border border-slate-700">
            <span class="text-cyan-400 font-bold block">🐢 Tortoise:</span>
            <span class="text-slate-300 text-[11px]">(4, 1)</span>
        </div>
        <div class="bg-slate-800/80 p-2 rounded-lg border border-slate-700">
            <span class="text-amber-400 font-bold block">🦌 Deer:</span>
            <span class="text-slate-300 text-[11px]">(8, 3)</span>
        </div>
        <div class="bg-slate-800/80 p-2 rounded-lg border border-slate-700">
            <span class="text-purple-400 font-bold block">🐊 Crocodile:</span>
            <span class="text-slate-300 text-[11px]">(7, 6)</span>
        </div>
        <div class="bg-slate-800/80 p-2 rounded-lg border border-slate-700">
            <span class="text-yellow-400 font-bold block">🦁 Lion:</span>
            <span class="text-slate-300 text-[11px]">(3, 10)</span>
        </div>
        <div class="bg-slate-800/80 p-2 rounded-lg border border-slate-700">
            <span class="text-blue-400 font-bold block">🐘 Elephant:</span>
            <span class="text-slate-300 text-[11px]">(11, 11)</span>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "Which animal enclosure is located at coordinate (4, 1)?",
                "options": ["Giant Panda", "Giant Tortoise", "Lion", "Asian Elephant"],
                "answer": 1,
                "explanation": "At x = 4, y = 1 lies the Giant Tortoise enclosure.",
                "hint": "Look for column 4, row 1."
            },
            {
                "question": "What are the exact coordinates of the Asian Elephant enclosure near the top-right border?",
                "options": ["(1, 1)", "(7, 6)", "(3, 10)", "(11, 11)"],
                "answer": 3,
                "explanation": "The Asian Elephant is located at column 11, row 11, written as (11, 11).",
                "hint": "Both horizontal and vertical values are 11."
            }
        ]
    }
]

if __name__ == '__main__':
    for s in slides_part2:
        wc = len(s['lecture'].split())
        status = "PASS" if 195 <= wc <= 215 else f"FAIL ({wc})"
        print(f"Slide {s['id']}: {wc} words [{status}]")
