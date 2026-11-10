#!/usr/bin/env python3
"""
NCERT Class 3 Mathematics - Chapter 14: The Surajkund Fair
Part 2: Slides 9 to 16 (Teaching Content + Checkpoints)
Strict spoken word count: 195 to 215 words per slide.
Strict titles: 1 to 3 words.
Zero human character names, zero lecturer personas.
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Mirror Line Reflection",
        "subtitle": "Lateral Inversion & Axis of Reflection",
        "speech": (
            "When we place a flat mirror along a line of symmetry, we observe the magical phenomenon of optical reflection. "
            "A mirror reflection duplicates every shape on the opposite side of the mirror line, maintaining identical sizes, angles, "
            "and distances. However, have you noticed that a mirror produces a subtle transformation known as lateral inversion? "
            "In a mirror, left and right are reversed! When you raise your right hand in front of a mirror, your reflection appears to "
            "raise its left hand. This directional flip explains why asymmetrical letters look reversed in a mirror. For example, "
            "the letter B or letter R looks backwards when held up to a mirror. But look at symmetrical letters like capital A, capital M, "
            "or capital T. When a vertical mirror is placed down the exact center of the letter A, the reflected half matches the hidden "
            "half so perfectly that the letter looks completely natural and unchanged. Testing capital alphabet letters against a mirror "
            "line is an entertaining way to identify which letters possess vertical symmetry, which possess horizontal symmetry like the letter E, "
            "and which possess both like the letter H and the letter O in our language."
        ),
        "checkpoints": [
            {
                "question": "Which of these capital letters has a vertical line of symmetry?",
                "options": ["Letter F", "Letter A", "Letter P", "Letter G"],
                "answer": 1,
                "hint": "Dividing this letter down the middle leaves identical left and right sides.",
                "explanation": "Capital letter A has a vertical line of symmetry down its middle."
            },
            {
                "question": "Which capital letter has both vertical and horizontal lines of symmetry?",
                "options": ["Letter B", "Letter H", "Letter C", "Letter L"],
                "answer": 1,
                "hint": "You can fold it in half vertically and horizontally.",
                "explanation": "Letter H can be divided into identical halves both vertically and horizontally."
            }
        ]
    },
    {
        "id": 10,
        "title": "Grid Counter Symmetry",
        "subtitle": "Balancing Tokens Across Central Boundaries",
        "speech": (
            "At the mathematics puzzle stall, children gather around grid boards to play an engaging interactive mirror game using colored "
            "counters with great excitement. The board is divided down the middle by a bold red mirror line, creating two identical halves: "
            "a left grid section and a matching right grid section. One player places colored tokens on specific squares of the left grid, "
            "and the partner must immediately place matching tokens on the right grid to create a perfectly symmetrical reflection. To succeed, "
            "players must follow the golden mathematical rule of coordinate reflection: distance from the mirror line must be strictly preserved "
            "across both sides. If a blue token sits two squares to the left of the center line on row three, its twin blue token must be placed "
            "exactly two squares to the right of the center line on that same row three. Placing it three squares away or shifting it to row four "
            "breaks the symmetry immediately! Playing this counter placement game trains quick spatial reflexes, sharpens observation, and reinforces "
            "the vital geometric concept that every point in a symmetrical object has a corresponding partner at an equal, opposite distance across the line of balance."
        ),
        "checkpoints": [
            {
                "question": "If a red counter is placed 3 squares left of the center line on row 2, where must the matching counter go?",
                "options": ["3 squares right on row 2", "2 squares right on row 3", "3 squares right on row 4", "5 squares left on row 2"],
                "answer": 0,
                "hint": "Keep the same row and the same distance to the right.",
                "explanation": "Mirror symmetry requires the matching token to sit 3 squares to the right on the same row (row 2)."
            },
            {
                "question": "What happens if a player places a matching counter on the wrong row?",
                "options": ["The counter changes color", "The symmetry is broken", "The board becomes larger", "The counter disappears"],
                "answer": 1,
                "hint": "Symmetry requires matching height and distance.",
                "explanation": "Shifting the row alters the height, breaking the bilateral reflection."
            }
        ]
    },
    {
        "id": 11,
        "title": "Floor Path Tessellation",
        "subtitle": "Paving Surfaces Without Gaps or Overlaps",
        "speech": (
            "As visitors stroll along the craft fair walkways, their feet tread upon beautifully paved stone and ceramic paths laid with immense care. "
            "Notice how the floor tiles fit together so neatly that they cover the entire walking ground without any gaps or overlapping edges. "
            "In mathematics, covering a two-dimensional surface completely using repeating geometric shapes without any gaps or overlaps is called "
            "a tessellation, or tiling pattern. Why is gapless tiling essential for public fairground pathways? Imagine walking along a tiled path where tiles "
            "do not fit together tightly, leaving open holes and uneven gaps between stones. A visitor could easily trip, catch their sandal or walking "
            "stick in an irregular crevice, and stumble or fall down! Architects, civil engineers, and stone masons prevent accidents by choosing tile shapes "
            "that interlock seamlessly across large communal areas. Simple regular polygons like squares, rectangles, and equilateral triangles tessellate "
            "naturally because their corner angles meet together to form exactly three hundred sixty degrees around every joint vertex. Observing paved "
            "fairground paths reveals how practical pedestrian safety, structural engineering, and geometric beauty unite harmoniously through the mathematical "
            "principles of seamless tessellations in civil construction throughout our towns and cities."
        ),
        "checkpoints": [
            {
                "question": "What is the mathematical term for covering a surface with repeating shapes without any gaps or overlaps?",
                "options": ["Perimeter", "Tessellation (Tiling)", "Capacity", "Subtraction"],
                "answer": 1,
                "hint": "Think of ceramic floor tiles covering a kitchen floor completely.",
                "explanation": "A tessellation is a pattern formed by repeating tiles without gaps or overlapping."
            },
            {
                "question": "Why must outdoor fairground pathway tiles fit together without open gaps?",
                "options": ["To save water", "To prevent visitors from tripping and falling", "To make tiles lighter", "To absorb sunlight"],
                "answer": 1,
                "hint": "Uneven gaps create tripping hazards for walkers.",
                "explanation": "Gapless tiling creates smooth, safe walking surfaces where feet cannot get trapped."
            }
        ]
    },
    {
        "id": 12,
        "title": "Rangometry Tile Shapes",
        "subtitle": "Snug Geometric Interlocking & Angle Sums",
        "speech": (
            "At the craft workshops, children explore rangometry kits, which contain colorful geometric plastic tiles of various shapes and sizes. "
            "The kit includes equilateral triangles, squares, rhombuses, and regular hexagons. Let us experiment with how different shapes "
            "interlock around a single corner vertex point with mathematical precision and curiosity. When you take four square tiles and bring their corners "
            "together, their ninety-degree angles sum to exactly three hundred sixty degrees, forming a completely flat, unbroken surface. Now try "
            "regular hexagons, like the honeycomb cells built by honeybees in natural hives. Each corner angle of a regular hexagon measures one "
            "hundred twenty degrees. When three hexagons meet at a common vertex, one hundred twenty multiplied by three equals three hundred sixty "
            "degrees, fitting together with astonishing snugness without any gaps! But what happens if you try to tile a floor using only regular "
            "pentagons? Five-sided pentagons leave awkward diamond-shaped gaps because their angles do not combine to form three hundred sixty degrees. "
            "Discovering which polygon shapes tessellate teaches young students why nature and master artisans rely on hexagons, triangles, and squares "
            "to construct sturdy, gapless structures that endure across centuries of architectural history in our great monuments and palaces."
        ),
        "checkpoints": [
            {
                "question": "How many squares meet at a vertex to tile a flat surface without gaps?",
                "options": ["2 squares", "3 squares", "4 squares", "6 squares"],
                "answer": 2,
                "hint": "4 × 90 degrees equals 360 degrees.",
                "explanation": "Four 90-degree square corners meet to make 360 degrees around a flat point."
            },
            {
                "question": "Which of these shapes is famously found in natural honeybee combs because it tiles without gaps?",
                "options": ["Circle", "Regular Hexagon", "Regular Pentagon", "Oval"],
                "answer": 1,
                "hint": "It has 6 equal sides.",
                "explanation": "Regular hexagons tessellate perfectly with 3 meeting at each vertex (3 × 120° = 360°)."
            }
        ]
    },
    {
        "id": 13,
        "title": "Continuous Repeating Tiles",
        "subtitle": "Designing Custom Tessellation Units & Borders",
        "speech": (
            "Artisans do not limit themselves to plain squares or triangles; they invent custom, creative tile shapes that repeat continuously "
            "along decorative borders and courtyards with remarkable artistic flair. How do designers invent a custom interlocking tile? There is a brilliant "
            "geometric trick: start with a standard square. If you cut out a curved shape from the left side of the square and slide it across to paste "
            "it onto the right side, the total area of the tile remains completely unchanged! Next, if you carve a triangular notch out of the bottom edge "
            "and attach that exact triangle to the top edge, you have created a unique puzzle-piece tile. Because every cut on one side is matched by an "
            "identical extension on the opposite side, multiple copies of this custom tile will interlock flawlessly across an entire floor, like interlocking "
            "jigsaw pieces. When colored in alternating contrasting shades, such as deep indigo and ivory white, the floor bursts into a dynamic tapestry "
            "of marching motifs. Creating custom tessellations allows students to combine artistic imagination with mathematical area conservation, "
            "showing how geometry powers creative industrial design, textile printing, ceramic pottery, and decorative architecture throughout our world today."
        ),
        "checkpoints": [
            {
                "question": "If you cut a shape from one side of a square tile and paste it on the opposite side, what happens to the total tile area?",
                "options": ["It doubles", "It stays exactly the same", "It decreases by half", "It turns to zero"],
                "answer": 1,
                "hint": "Nothing is lost; the piece is merely moved to the other side.",
                "explanation": "Area is conserved: subtracting from one edge and adding the identical piece to the opposite edge preserves total area."
            },
            {
                "question": "What everyday item interlocks seamlessly like custom tessellating tiles?",
                "options": ["Round marbles", "Jigsaw puzzle pieces", "Loose coins", "Fallen leaves"],
                "answer": 1,
                "hint": "The tabs on one piece fit into the blanks of the neighbor.",
                "explanation": "Jigsaw puzzle pieces feature matching tabs and slots that fit together without gaps."
            }
        ]
    },
    {
        "id": 14,
        "title": "Fairground Map Reading",
        "subtitle": "Navigating Layouts with Legends & Landmarks",
        "speech": (
            "The Surajkund fair spreads across many sprawling acres of open parkland, making a printed fairground guide map indispensable for all visiting families. "
            "Let us learn how to read and interpret a large public festival map with mathematical confidence and spatial clarity. A map is a scaled "
            "bird's-eye view of the physical environment, using standardized symbols, lines, and icons to represent real-world locations accurately. At the bottom "
            "of the map, a legend, or key, explains what each symbol means: an icon of a car indicates visitor parking lots, a rupee sign marks automated teller "
            "machines, a plate and spoon marks food courts, and a wavy blue patch represents the water reservoir pond. In the center of the grounds sits "
            "the open-air performance arena, known as the chaupal, while towering above the pavilions stands the giant Ferris wheel. By identifying your "
            "current location near the entrance gate and finding target landmarks on the map, you can plan the shortest walking route between various craft stalls. "
            "Map reading connects spatial orientation with coordinate geometry, empowering children to explore large, bustling festival fairgrounds safely, "
            "independently, and with complete directional awareness and joyful mathematical curiosity throughout their entire family day."
        ),
        "checkpoints": [
            {
                "question": "What map feature explains the meaning of various symbols and icons?",
                "options": ["The border line", "The legend (or key)", "The price tag", "The paper fold"],
                "answer": 1,
                "hint": "It translates symbols like car icons or rupee signs into words.",
                "explanation": "The map legend or key explains what each symbol, color, and icon represents."
            },
            {
                "question": "What central landmark in the Surajkund fair hosts traditional folk dance and music performances?",
                "options": ["The parking lot", "The chaupal (performance arena)", "The ATM booth", "The water tank"],
                "answer": 1,
                "hint": "The central open-air cultural gathering stage.",
                "explanation": "The chaupal is the central cultural stage for folk performances at the fair."
            }
        ]
    },
    {
        "id": 15,
        "title": "Colored Pathway Navigation",
        "subtitle": "Following Directional Color Lanes & Waypoints",
        "speech": (
            "To help thousands of visiting families navigate smoothly without getting lost, fair organizers paint distinct color-coded lanes along "
            "the main fairground avenues with clear directional signposts and colorful banners. Let us follow the directional colored pathways to reach important destinations "
            "throughout the park with ease and confidence. The Golden Lane leads straight from the primary entrance gate toward the central chaupal stage and state craft emporiums. "
            "The Blue Lane branches off toward the peaceful lakeside promenade and water ponds. The Green Lane meanders through the lush botanical gardens "
            "and eco-friendly bamboo craft stalls, while the Red Lane connects the bustling food stalls, kulfi carts, and the giant Ferris wheel. Suppose "
            "a family stands at the giant wheel on the Red Lane and wants to visit an automated teller machine located on the Golden Lane. By consulting "
            "the map, they determine the navigation sequence: walk straight along the Red Lane past the kulfi cart, turn right at the central junction onto "
            "the Golden Lane, and proceed fifty paces to the banking kiosk. Following directional color lanes teaches children sequential route planning, "
            "turn-by-turn tracking, and practical spatial awareness in everyday community environments, school campuses, and festive outdoor gatherings."
        ),
        "checkpoints": [
            {
                "question": "Why do large public fairs use color-coded pedestrian pathways?",
                "options": ["To make the ground slippery", "To help visitors navigate easily to different zones without getting lost", "To test new paint colors", "To stop people from walking"],
                "answer": 1,
                "hint": "Color lanes guide crowds toward specific attractions and amenities.",
                "explanation": "Color-coded lanes guide visitors smoothly to specific festival zones and exits."
            },
            {
                "question": "If you are at the Red Lane and turn right at the junction onto Golden Lane, what skill are you practicing?",
                "options": ["Calendar subtraction", "Sequential route navigation and directional orientation", "Weight measurement", "Coin counting"],
                "answer": 1,
                "hint": "Following turn-by-turn directions on a path.",
                "explanation": "Turning onto specific lanes to reach a destination exercises route navigation and spatial orientation."
            }
        ]
    },
    {
        "id": 16,
        "title": "Fair Maze Exit",
        "subtitle": "Logical Pathfinding & Dead-End Elimination",
        "speech": (
            "Near the exit pavilion of the fairgrounds, children encounter an exciting life-sized green hedge maze puzzle that tests their problem-solving "
            "wits, memory, and patience. A maze is a branching network of pathways where travelers must find an unobstructed route from an entry point to an exit "
            "goal while avoiding frustrating dead ends. Let us apply mathematical logic to solve maze navigation systematically without confusion or panic. "
            "At every intersection, or decision junction, we evaluate our pathway options with careful consideration. If a path terminates at a solid hedge barrier with "
            "nowhere forward to go, that path is an authentic dead end. In mathematical pathfinding, we eliminate dead ends by backtracking to the previous "
            "junction and testing the alternative open branch. Furthermore, keen navigators track physical landmarks encountered along the trail, such as "
            "a carved wooden owl, a stone water fountain, or a painted terracotta pot. Recognizing previously passed landmarks confirms whether you are progressing "
            "forward toward the exit gate or walking in repetitive circles. Solving mazes strengthens deductive reasoning, persistent problem-solving, "
            "and spatial mapping abilities that form the very foundation for modern computer routing algorithms, GPS satellite mapping, and intelligent robotic navigation systems used worldwide."
        ),
        "checkpoints": [
            {
                "question": "What should a maze navigator do upon encountering a closed dead end?",
                "options": ["Give up immediately", "Backtrack to the previous intersection and try the alternative branch", "Jump over the hedge", "Stand still forever"],
                "answer": 1,
                "hint": "Retrace your steps to the last choice point.",
                "explanation": "Backtracking from dead ends allows pathfinders to systematically explore open routes."
            },
            {
                "question": "Why is observing distinct landmarks helpful when navigating through a maze?",
                "options": ["It changes the maze layout", "It helps verify whether you are making forward progress or walking in circles", "It unlocks hidden doors", "It makes the path shorter"],
                "answer": 1,
                "hint": "Landmarks tell you if you have visited that spot before.",
                "explanation": "Landmarks act as visual waypoints to confirm direction and avoid looping in circles."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(slides_part2)} slides for Part 2.")
    for s in slides_part2:
        words = len(s["speech"].strip().split())
        title_words = len(s["title"].strip().split())
        print(f"Slide {s['id']}: '{s['title']}' ({title_words} words) -> Speech: {words} words")
        assert 1 <= title_words <= 3, f"Title length violation on slide {s['id']}"
        assert 195 <= words <= 215, f"Speech word count {words} out of range (195-215) on slide {s['id']}"
    print("Part 2 passed all strict validation checks!")
