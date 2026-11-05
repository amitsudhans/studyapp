# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 2: Hide and Seek - Part 2 (Slides 9 to 16)
Generates slides 9 to 16 with strict word counts (195-215 words), 2 checkpoints each, zero human names.
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Grid System Navigation",
        "lecture": (
            "When physical spaces become larger or more intricate, casual descriptions like 'near the corner' or 'somewhere to the left' "
            "are no longer sufficient. To achieve mathematical precision, cartographers and mathematicians organize space using a formal "
            "grid system. Let us examine a standard three-by-three geometric grid drawn neatly on paper or chalked on the classroom "
            "floor. A three-by-three grid consists of nine square compartments called cells, formed by the perpendicular intersection of "
            "horizontal rows and vertical columns. The three horizontal layers are numbered from top to bottom as Row One, Row Two, and "
            "Row Three. Meanwhile, the three vertical pathways are numbered from left to right as Column One, Column Two, and Column Three. "
            "Every single cell in this grid represents the unique intersection of exactly one row and one column. For example, the very "
            "center compartment of the grid is uniquely identified as Row Two, Column Two. Because rows and columns form an organized "
            "Cartesian matrix, every cell has an exact, unmistakable two-coordinate address that can be referenced by anyone without "
            "confusion. Mastering row and column navigation introduces young learners to the powerful coordinate frameworks that power "
            "chessboards, spreadsheet tables, digital computer screens, and global satellite navigation systems used worldwide."
        ),
        "checkpoints": [
            {
                "question": "How many total cells are formed in a 3×3 grid system?",
                "options": ["6 cells", "8 cells", "9 cells", "12 cells"],
                "answer": 2,
                "explanation": "A 3×3 grid contains 3 rows of 3 cells each: 3 × 3 = 9 cells in total."
            },
            {
                "question": "Which compartment sits at the exact center of a 3×3 grid?",
                "options": ["Row 1, Column 1", "Row 3, Column 3", "Row 2, Column 2", "Row 1, Column 3"],
                "answer": 2,
                "explanation": "Row 2 is the middle horizontal row, and Column 2 is the middle vertical column."
            }
        ]
    },
    {
        "id": 10,
        "title": "Locating Grid Coordinates",
        "lecture": (
            "Now let us turn formal grid addresses into an exciting, hands-on interactive placement game in our classroom. In the classroom "
            "workshop, students play the grid coordinate game by listening attentively to spatial clues and drawing miniature icons in "
            "designated grid compartments. For example, the first instruction asks a young navigator to place a soccer ball at the address "
            "of Row One, Column One. Checking the chart, Row One is the uppermost horizontal band, and Column One is the leftmost vertical "
            "column; their perpendicular intersection is the top-left corner cell. The next clue commands: 'Draw a juicy red apple at the "
            "exact center of the board.' Translating this descriptive clue into coordinates leads directly to Row Two, Column Two. A third "
            "clue instructs the student to place a yellow flower at Row Three, Column Two, which corresponds to the bottom middle "
            "compartment. If another player asks where the storybook is located, and they see it resting in the top-right corner, they "
            "announce its coordinates as Row One, Column Three. Following and giving coordinate clues develops active listening, "
            "two-dimensional spatial orientation, methodical thinking, and logical indexing skills that bridge playful classroom puzzles "
            "with formal coordinate geometry in higher mathematics."
        ),
        "checkpoints": [
            {
                "question": "Which grid cell represents the top-right corner of a 3×3 grid?",
                "options": ["Row 1, Column 1", "Row 1, Column 3", "Row 3, Column 1", "Row 3, Column 3"],
                "answer": 1,
                "explanation": "Row 1 is the top row, and Column 3 is the rightmost column, making Row 1, Column 3 the top-right cell."
            },
            {
                "question": "If an apple is drawn at Row 3, Column 1, where is it positioned on the grid?",
                "options": ["Top-left corner", "Bottom-left corner", "Exact center", "Bottom-right corner"],
                "answer": 1,
                "explanation": "Row 3 is the bottom row, and Column 1 is the leftmost column, so it is the bottom-left corner."
            }
        ]
    },
    {
        "id": 11,
        "title": "Treasure Hunt Grid",
        "lecture": (
            "Expanding our navigational canvas from a three-by-three matrix to a larger four-by-four grid unlocks the thrilling adventure "
            "of a mathematical treasure hunt! In this strategic classroom activity, a sixteen-cell grid represents an enchanted island map "
            "with hidden treasures like gold coins, sweet ripe mangoes, flowering trees, and sleeping animals scattered across various "
            "compartments. However, moving across the grid requires strict adherence to formal mathematical rules. Explorers must navigate "
            "strictly along orthogonal pathways: moving one step Up, one step Down, one step Left, or one step Right at each turn. Diagonal "
            "leaps across cell corners are strictly prohibited because real roads, classroom aisles, and city blocks follow perpendicular "
            "corridors without shortcut jumps. Starting from the baseline anchor cell at the bottom-left corner, players receive coded "
            "step sequences such as: 'Move two steps Up, then three steps Right.' Following these directional commands step by step "
            "ensures that every player traces the exact same pathway across the grid without getting lost or confused. Orthogonal grid "
            "movement teaches young explorers how modern robotics, computer game programming, and autonomous vehicles plan reliable "
            "navigational trajectories along perpendicular grid tracks safely and efficiently. This disciplined spatial logic forms the "
            "foundation for digital algorithms."
        ),
        "checkpoints": [
            {
                "question": "Which type of movement is strictly prohibited in an orthogonal grid treasure hunt game?",
                "options": ["Moving one step Up", "Moving one step Left", "Diagonal leaps across cell corners", "Moving one step Down"],
                "answer": 2,
                "explanation": "Orthogonal movement permits only Up, Down, Left, and Right steps along grid lines; diagonal jumps are not allowed."
            },
            {
                "question": "Starting at bottom-left (Row 4, Col 1), moving 2 steps Up and 2 steps Right lands on which cell?",
                "options": ["Row 2, Column 3", "Row 1, Column 4", "Row 3, Column 2", "Row 4, Column 3"],
                "answer": 0,
                "explanation": "Moving 2 steps Up changes Row 4 to Row 2; moving 2 steps Right changes Column 1 to Column 3."
            }
        ]
    },
    {
        "id": 12,
        "title": "Path Step Counting",
        "lecture": (
            "Once directional paths are established on a grid, calculating travel distance becomes a matter of systematic step counting. "
            "In everyday life on city streets, we cannot fly over buildings in a direct diagonal line; we must walk along perpendicular "
            "paved sidewalks. In mathematics, the total distance measured along horizontal and vertical grid lines is called the Manhattan "
            "distance or grid step count. Suppose a young explorer starts at coordinate cell Row Four, Column One and wants to reach a "
            "hidden ripe mango located at Row One, Column Three. To calculate the total path length, we break the journey into its two "
            "orthogonal components: vertical steps along rows and horizontal steps along columns. Moving vertically from Row Four upward "
            "to Row One requires three upward steps. Moving horizontally from Column One rightward to Column Three requires two rightward "
            "steps. Adding these components together yields three plus two equals five total steps along the grid lines! Interestingly, "
            "whether the explorer walks three steps Up first and then two steps Right, or walks two steps Right first and then three steps "
            "Up, the total step count remains exactly five steps. Counting grid steps helps young mathematicians understand distance "
            "conservation and path optimization along city grids."
        ),
        "checkpoints": [
            {
                "question": "What is the total step count to travel from Row 4, Column 1 to Row 1, Column 3 on a grid?",
                "options": ["3 steps", "4 steps", "5 steps", "7 steps"],
                "answer": 2,
                "explanation": "Vertical steps: 4 - 1 = 3; Horizontal steps: 3 - 1 = 2; Total steps = 3 + 2 = 5 steps."
            },
            {
                "question": "Does taking horizontal steps before vertical steps change the total minimum step count on a grid?",
                "options": ["Yes, it increases distance", "No, the total sum of perpendicular steps remains identical", "Yes, it doubles the steps", "Only on cloudy days"],
                "answer": 1,
                "explanation": "Addition is commutative: 3 + 2 = 2 + 3 = 5 steps. Order of orthogonal turns does not alter total length."
            }
        ]
    },
    {
        "id": 13,
        "title": "Drone Aerial Views",
        "lecture": (
            "Modern technology provides exciting new aerial perspectives that connect real three-dimensional architecture with flat "
            "two-dimensional maps. Imagine launching a small camera drone straight up from the central school playground high into the "
            "clear blue sky. As the drone climbs higher and higher above the school, the familiar buildings undergo a dramatic, fascinating "
            "visual transformation. Ground-level architectural features like doorways, vertical brick walls, and window frames gradually "
            "disappear from view beneath overhanging eaves. Instead, the airborne camera looks straight down at the roofs, open courtyards, "
            "and pathways, producing a true aerial top-down photograph. High sloping pitched roofs appear as flat geometric rectangles, "
            "the round assembly flag base shows up as a crisp circle, and lush garden trees appear as leafy circular canopies casting "
            "dark shadows on the grass. Looking at drone imagery teaches young cartographers how real-world three-dimensional landscapes "
            "are converted into flat two-dimensional maps. By recognizing building outlines from high above, students realize that maps "
            "are not magical abstractions, but accurate bird's-eye geometric representations of the physical world viewed directly from "
            "an overhead vantage point. This elevated camera perspective helps cartographers and urban planners map expansive landscapes "
            "with flawless geometric accuracy. Capturing crystal-clear aerial views from flying drones bridges everyday ground perception "
            "with scientific cartography and satellite navigation seamlessly for everyone."
        ),
        "checkpoints": [
            {
                "question": "What happens to the vertical walls of a building when viewed directly from above by a drone?",
                "options": ["They appear taller", "They flatten out and become mostly invisible beneath the roofline", "They turn into circles", "They change into glass"],
                "answer": 1,
                "explanation": "Looking perpendicularly from directly above, vertical walls lie parallel to the sight line and hide under the roof."
            },
            {
                "question": "How does a circular flagpole base appear in an aerial top-down drone photograph?",
                "options": ["As a tall triangle", "As a flat circle", "As a wavy line", "As a square box"],
                "answer": 1,
                "explanation": "A cylindrical or round base projects as a flat, geometric circle when viewed directly from above."
            }
        ]
    },
    {
        "id": 14,
        "title": "School Campus Blueprint",
        "lecture": (
            "From aerial drone photographs, cartographers and civil engineers create standardized architectural campus blueprints. A "
            "school campus map is an organized, detailed two-dimensional layout that represents all major school buildings, outdoor "
            "zones, interconnected walkways, and corridors in clear, labeled geometric symbols. Let us examine our school site map closely: "
            "at the bottom baseline rests the main security entrance gate. Passing through the entrance gate, a wide central paved corridor "
            "leads straight forward into the open assembly courtyard, flanked by the elevated performance stage on the left side. Further "
            "down the western corridor stand the vibrant Class Four classrooms and the well-stocked school library. On the eastern side, "
            "we find the clean medical care room and the mid-day meal kitchen where warm, nutritious lunches are prepared daily. Beyond "
            "the academic wings stretches the expansive green sports playground equipped with football goalposts and running tracks. "
            "Every facility on the campus map occupies a specific relative position in space. Learning to read blueprints enables young "
            "citizens to orient themselves instantly within large public complexes, understand the spatial relationships between diverse "
            "campus facilities, and navigate complex public environments safely, confidently, and independently. Campus blueprints turn "
            "large school grounds into manageable visual layouts."
        ),
        "checkpoints": [
            {
                "question": "What is the primary function of a school campus blueprint or site map?",
                "options": ["To show what books are in the library", "To represent the spatial layout and relative locations of campus buildings and paths", "To test the school bell volume", "To count the number of trees outside"],
                "answer": 1,
                "explanation": "A campus site map shows the 2D layout, positions, and connections between all buildings, rooms, and outdoor zones."
            },
            {
                "question": "Where is the main entrance gate typically positioned on a standard campus navigation blueprint?",
                "options": ["On the classroom ceiling", "At the boundary baseline where visitors enter the campus grounds", "Inside the library bookshelf", "Under the football goalpost"],
                "answer": 1,
                "explanation": "The entrance gate marks the perimeter boundary access point where people enter the campus."
            }
        ]
    },
    {
        "id": 15,
        "title": "Shortest Route Navigation",
        "lecture": (
            "Once a campus blueprint is in our hands, we can solve practical pathfinding problems: how do we travel from one location to "
            "another using the most efficient route? Suppose a group of students in the Class Four classroom needs to transport freshly "
            "borrowed science project books to the assembly stage for an afternoon exhibition. Looking at the campus site map, they notice "
            "two distinct corridors leading to the stage. Route A runs directly through the covered indoor corridor past the administration "
            "office, measuring sixty meters in total. Route B winds outward around the perimeter of the sports playground and passes by "
            "the mid-day meal kitchen, measuring ninety-five meters in total distance. By calculating and comparing the distances of both "
            "alternative paths, students discover that Route A is thirty-five meters shorter than Route B! Choosing the shortest route "
            "saves valuable time and energy, especially when carrying heavy boxes of books. Navigating campus maps trains young minds in "
            "critical decision-making, spatial comparison, distance estimation, and optimization techniques that form the bedrock of "
            "logistics, civil planning, and everyday travel efficiency. Finding optimal pathways is a core mathematical skill used by "
            "pilots, delivery drivers, and robotic navigation systems worldwide."
        ),
        "checkpoints": [
            {
                "question": "If Route A is 60 meters long and Route B is 95 meters long, which is the shorter route and by how much?",
                "options": ["Route B is shorter by 35 meters", "Route A is shorter by 35 meters", "Both routes are equal", "Route A is shorter by 15 meters"],
                "answer": 1,
                "explanation": "Comparing the lengths: 95 m - 60 m = 35 m, so Route A is shorter by 35 meters."
            },
            {
                "question": "Why is finding the shortest route between campus facilities beneficial?",
                "options": ["It increases walking time", "It minimizes travel distance, saving time and physical effort", "It makes books heavier", "It closes the library"],
                "answer": 1,
                "explanation": "The shortest route reduces travel distance, saving time and physical energy during campus movement."
            }
        ]
    },
    {
        "id": 16,
        "title": "Campus Sight Mapping",
        "lecture": (
            "The crowning milestone of our journey through views and perspectives is creating our very own personal sight map! A sight map "
            "is an original, hand-drawn navigational sketch that records the sequential visual landmarks and directional turns an observer "
            "experiences while walking step-by-step through a physical space. In this hands-on project, students start at the main school "
            "entrance gate and walk carefully toward their classroom desk. Along the way, they record every major visual landmark: passing "
            "the drinking water fountain on the right, turning ninety degrees left at the tall ashoka tree, walking straight past the "
            "principal's office, climbing the central stone staircase, and turning right into the second doorway on the corridor. By "
            "plotting these observed waypoints on paper with clear directional arrows, recognizable symbols, and approximate step counts, "
            "students synthesize all the core lessons of this chapter: line-of-sight observations, view angles, grid coordinates, and "
            "route optimization. Creating personal maps empowers young learners with lifelong spatial mastery, turning everyday walks into "
            "joyful geometric adventures with immense curiosity, creative excitement, and mathematical precision. Mapping our physical "
            "surroundings deepens our lifelong appreciation for how simple two-dimensional symbols represent the rich three-dimensional "
            "world we inhabit every day. Every young explorer, architect, and navigator begins their journey by mapping the familiar "
            "paths around them with pride."
        ),
        "checkpoints": [
            {
                "question": "What is an essential feature to include when drawing a practical campus sight map?",
                "options": ["Drawings of clouds only", "Sequential landmarks, directional turn arrows, and labeled pathways", "Random scribbles", "Only the color of the paint"],
                "answer": 1,
                "explanation": "A practical sight map requires recognizable waypoints, turn directions, and labeled paths to guide travelers."
            },
            {
                "question": "How does creating a personal sight map help develop spatial intelligence?",
                "options": ["It makes pencils sharper", "It connects physical 3D walking experiences with structured 2D map representations", "It makes the classroom smaller", "It eliminates the need for doors"],
                "answer": 1,
                "explanation": "Mapping translates physical 3D environmental memories into structured 2D geometric representations."
            }
        ]
    }
]

if __name__ == '__main__':
    for s in slides_part2:
        wc = len(s['lecture'].split())
        title_wc = len(s['title'].split())
        print(f"Slide {s['id']}: '{s['title']}' (Title: {title_wc} words, Lecture: {wc} words)")
        assert 1 <= title_wc <= 3, f"Title length violation in slide {s['id']}"
        assert 195 <= wc <= 215, f"Lecture word count {wc} out of range in slide {s['id']}"
    print("Part 2: All 8 slides verified successfully!")
