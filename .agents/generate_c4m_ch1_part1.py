# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 1: Shapes Around Us - Part 1 (Slides 1 to 8)
Generates slides 1 to 8 with strict word counts (195-215 words), 2 checkpoints each, zero human names.
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Building Monument Models",
        "lecture": (
            "Welcome to the architectural world of shapes and structures. When a young explorer visits the historic capital city "
            "of New Delhi, magnificent heritage monuments immediately capture attention. The towering India Gate arch stands firmly "
            "across the ceremonial boulevard, while the ancient Qutub Minar reaches high into the sky, and the magnificent Akshardham "
            "temple showcases intricate stone carvings. Back in the classroom workshop, the young explorer attempts to construct a "
            "faithful miniature model of India Gate using wooden toy building blocks. This creative engineering project immediately "
            "raises important spatial questions. Which geometric solids should be chosen to support the structure, and which shapes "
            "can form the upper roof? Solid rectangular blocks called cuboids provide stable, wide foundation bases that will not "
            "wobble under pressure. For the vertical pillars, identical cuboids or sturdy cylinders rise evenly on both sides. A "
            "curved arch block spans the central opening to let imaginary traffic pass through safely. Finally, a long horizontal "
            "cuboid slab rests across the top to complete the roof monument. By selecting solids according to flat faces, right-angled "
            "corners, and balanced proportions, young builders discover how basic three-dimensional geometry creates enduring, "
            "beautiful structures in both historic architecture and classroom models."
        ),
        "checkpoints": [
            {
                "question": "Which 3D shape provides the most stable foundation base for building an India Gate pillar model?",
                "options": ["A round sphere", "A flat-faced cuboid block", "A rolling cylinder on its side", "A pointed cone"],
                "answer": 1,
                "explanation": "A cuboid has broad, flat rectangular faces that rest firmly on the ground without rolling or tipping over."
            },
            {
                "question": "Why are curved arch blocks used over the central opening of monument gates?",
                "options": ["To make the structure heavier", "To span open space while distributing weight to side pillars", "To prevent any sunlight from entering", "To turn the gate into a pyramid"],
                "answer": 1,
                "explanation": "Curved arches span openings gracefully while directing downward loads outward onto the supportive side pillars."
            }
        ]
    },
    {
        "id": 2,
        "title": "Historic Brick Architecture",
        "lecture": (
            "Let us travel back through centuries of construction craftsmanship by exploring the renowned Qutub Minar minaret in Delhi. "
            "Constructed of intricately carved red sandstone and marble, this soaring tower stands seventy-two point five meters high, "
            "making it the tallest historic brick minaret in the entire world. The tower comprises five distinct tapering storeys, "
            "connected internally by three hundred seventy-nine winding spiral stone stairs. Traditional Indian master builders "
            "selected durable materials that could withstand centuries of weather. They utilized kiln-fired clay bricks, hand-chiseled "
            "sandstone blocks, and sturdy lime mortar to bind every layer securely. In contrast, modern constructors often employ "
            "reinforced concrete slabs, steel girders, and hollow manufactured blocks. Examine a single building brick closely. A "
            "brick is a classic cuboid featuring six flat rectangular faces, twelve straight edges, and eight corner vertices. Notice "
            "how masons lay bricks in interlocking patterns known as running bonds. Rather than stacking vertical mortar seams in one "
            "straight line, each upper brick bridges the gap between two lower bricks. This clever overlapping arrangement distributes "
            "structural weight evenly across the entire wall. By understanding the geometric properties of individual bricks, we "
            "appreciate how simple rectangular units combine to form colossal monuments that endure for generations."
        ),
        "checkpoints": [
            {
                "question": "How many storeys and winding stairs does the historic Qutub Minar minaret feature?",
                "options": ["3 storeys and 150 stairs", "5 storeys and 379 stairs", "7 storeys and 500 stairs", "4 storeys and 250 stairs"],
                "answer": 1,
                "explanation": "The Qutub Minar features 5 distinct tapering storeys with 379 internal spiral steps reaching the top."
            },
            {
                "question": "Why do masons lay bricks in overlapping interlocking patterns rather than straight vertical seams?",
                "options": ["To use less mortar only", "To distribute weight evenly and prevent cracks from running through", "To make the wall curved", "To create triangular windows"],
                "answer": 1,
                "explanation": "Overlapping brick bonds distribute loads across the wall and prevent continuous vertical crack lines."
            }
        ]
    },
    {
        "id": 3,
        "title": "Prisms and Pyramids",
        "lecture": (
            "When we unfold a cardboard box and lay it completely flat on a table, we reveal its two-dimensional net. Folding this net "
            "along dotted crease lines transforms flat card into a hollow three-dimensional solid. In three-dimensional solid geometry, "
            "all flat-faced polyhedra are broadly classified into two grand families: prisms and pyramids. A prism is characterized by "
            "two identical, parallel polygon bases positioned at opposite ends, joined together by flat rectangular side faces. For "
            "instance, a triangular prism features two matching triangular bases connected by three rectangular sides. A hexagonal "
            "prism has two six-sided hexagonal bases linked by six rectangular faces, while a square prism, commonly known as a cuboid, "
            "possesses square bases and rectangular sides. In sharp contrast, a pyramid features only one single polygonal base resting "
            "on the ground. All of its triangular side faces tilt inward and converge upward to meet at a single top vertex called the "
            "apex. A triangular pyramid has a triangular base and three triangular walls, forming a tetrahedron. A square pyramid has "
            "a flat square base and four triangular faces sloping to the peak. Remembering this clear, simple distinction allows young "
            "mathematicians to classify any unfamiliar solid box instantly and accurately."
        ),
        "checkpoints": [
            {
                "question": "What is the defining feature of all prisms that distinguishes them from pyramids?",
                "options": ["Prisms have only triangular faces", "Prisms have two identical parallel bases connected by rectangular side faces", "Prisms always taper to a single sharp apex", "Prisms have zero flat faces"],
                "answer": 1,
                "explanation": "Prisms possess two identical, parallel opposite bases joined by rectangular side faces, whereas pyramids taper to an apex."
            },
            {
                "question": "How many triangular side faces meet at the apex of a square pyramid?",
                "options": ["2 triangular faces", "3 triangular faces", "4 triangular faces", "6 triangular faces"],
                "answer": 2,
                "explanation": "Because the base has 4 straight edges, exactly 4 triangular side faces rise upward to meet at the top apex."
            }
        ]
    },
    {
        "id": 4,
        "title": "Euler Formula Table",
        "lecture": (
            "Hands-on modeling provides an exciting pathway to discover hidden mathematical truths about polyhedra. In the classroom "
            "geometry lab, students construct skeleton frames of three-dimensional solids using hollow drinking straws and small "
            "balls of kneaded modeling clay. In these skeletal structures, each straight straw represents an edge, while each clay ball "
            "at the corners forms a vertex. The flat, enclosed open spaces bounded by the straw outlines represent the faces. When we count "
            "these features systematically, remarkable mathematical harmony emerges. Take a standard cube: it possesses six flat "
            "faces, eight corner vertices, and twelve straight edges. Add faces and vertices together to get fourteen, then subtract "
            "the twelve edges, leaving a difference of two. Next, carefully examine a triangular prism: it has five faces, six vertices, "
            "and nine edges. Adding five and six yields eleven; subtracting nine again leaves two. Now test a square pyramid: it has "
            "five faces, five vertices, and eight edges. Five plus five is ten, minus eight equals two. This universal mathematical "
            "law is famously known as Euler's polyhedral formula, expressed as Faces plus Vertices minus Edges equals two, or F plus "
            "V minus E equals two, beautifully proving geometric balance across all convex polyhedral solids."
        ),
        "checkpoints": [
            {
                "question": "What is Euler's polyhedral formula relating faces (F), vertices (V), and edges (E)?",
                "options": ["F + V + E = 2", "F + V - E = 2", "F - V + E = 2", "F × V - E = 2"],
                "answer": 1,
                "explanation": "Euler's formula states that for any convex polyhedron, Faces plus Vertices minus Edges always equals 2."
            },
            {
                "question": "A triangular prism has 5 faces and 6 vertices. Using Euler's formula, how many edges must it have?",
                "options": ["8 edges", "9 edges", "10 edges", "12 edges"],
                "answer": 1,
                "explanation": "Using F + V - E = 2: 5 + 6 - E = 2, so 11 - E = 2, giving E = 9 edges."
            }
        ]
    },
    {
        "id": 5,
        "title": "Cube Face Views",
        "lecture": (
            "Playing with gaming dice reveals fascinating spatial secrets of cubes. On every standard fair gaming die, the dots or "
            "pips on opposite facing sides always sum to exactly seven. That means one is always positioned directly opposite six, "
            "two is opposite five, and three is opposite four. Faces that touch along a shared edge are called adjacent faces. Because "
            "opposite faces lie across the solid cube from each other, they can never share a border or touch. This fundamental "
            "geometric principle helps us solve multi-view three-dimensional cube puzzles. Imagine observing an opaque colored cube "
            "from three different viewing angles. In the first view, you observe red on top, blue on the front, and green on the right. "
            "In the second view, you see red on top, green on the front, and yellow on the right. In the third view, you see blue on "
            "the front, purple on the bottom, and green on the right. Since green is seen touching red, blue, yellow, and purple, "
            "none of those four colors can be opposite green. Therefore, the remaining sixth color must be green's true opposite face. "
            "Through systematic spatial elimination, young detectives deduce every hidden cube face with confidence."
        ),
        "checkpoints": [
            {
                "question": "On a standard gaming die, what number is always situated directly opposite to the face with 2 pips?",
                "options": ["3", "4", "5", "6"],
                "answer": 2,
                "explanation": "Opposite faces on a standard fair die always sum to 7. Since 7 - 2 = 5, the opposite face has 5 pips."
            },
            {
                "question": "Can two opposite faces of a cube ever share a common boundary edge or corner?",
                "options": ["Yes, always", "No, opposite faces are on parallel planes and never touch", "Only in wooden cubes", "Only when viewed from above"],
                "answer": 1,
                "explanation": "Opposite faces are situated on opposite parallel sides of the cube, so they can never share an edge."
            }
        ]
    },
    {
        "id": 6,
        "title": "Sorting Shape Properties",
        "lecture": (
            "Classifying geometric shapes helps organize our understanding of the physical world. A powerful visual tool for sorting "
            "solids is the Venn diagram, where overlapping circular regions group objects according to specific structural "
            "attributes. Let us carefully examine three key geometric properties: flat polygonal faces, curved surfaces, and straight "
            "edges. Solids like cubes, rectangular cuboids, prisms, and pyramids belong entirely to the flat-face polyhedron category "
            "because every single surface is a flat polygon bounded by straight edges. On the other hand, a sphere has only one "
            "continuous curved surface with zero flat faces and zero edges. A cylinder possesses two flat circular bases joined by a "
            "smooth curved wall, giving it two curved boundary rims. A cone features one flat circular base, one curved side surface, "
            "and a pointed apex. Now consider a Venn diagram sorting shapes with rectangular faces in one circle and shapes with "
            "triangular faces in another circle. Where does a triangular prism belong? It belongs directly in the overlapping central "
            "intersection because it possesses three rectangular side faces and two triangular end bases at the same time. Sorting "
            "shapes through Venn diagrams trains our mathematical minds to spot shared properties and unique geometric classifications "
            "quickly and clearly."
        ),
        "checkpoints": [
            {
                "question": "Where does a triangular prism sit in a Venn diagram comparing shapes with rectangular faces and triangular faces?",
                "options": ["Outside both circles", "Only in the rectangular circle", "Only in the triangular circle", "In the overlapping intersection of both circles"],
                "answer": 3,
                "explanation": "A triangular prism has both 3 rectangular faces and 2 triangular bases, placing it directly in the intersection."
            },
            {
                "question": "Which of the following solids has both flat faces and a curved surface?",
                "options": ["A cube", "A cylinder", "A square pyramid", "A rectangular cuboid"],
                "answer": 1,
                "explanation": "A cylinder features two flat circular bases along with one smooth curved surface wrapping around its body."
            }
        ]
    },
    {
        "id": 7,
        "title": "Cube Tower Counting",
        "lecture": (
            "Stacking identical unit cubes allows young architects to build imaginative three-dimensional towers, castle battlements, "
            "and stepped pyramid formations. However, determining the total volume of such structures requires careful spatial "
            "reasoning, because upper blocks often conceal hidden cubes beneath them. A unit cube cannot hover unsupported in mid-air "
            "above an empty gap; every single cube on an upper floor must rest upon another solid cube situated directly beneath it "
            "on the floor below. Therefore, counting only the blocks visible from one camera angle will lead to an incorrect count. The "
            "most dependable method is systematic layer-by-layer counting, starting from the ground up. First, count the bottom "
            "ground-floor footprint: how many unit cubes form the base foundation? Next, count the second level cubes resting on top "
            "of that base. Continue counting each subsequent floor upward, level by level, until reaching the topmost rooftop pinnacle. "
            "Alternatively, count by vertical columns: write down the height of each vertical stack, such as one, two, or three cubes "
            "high, and then sum all column heights together. For example, a three-tier stepped staircase with columns of height one, "
            "two, and three blocks contains exactly six unit cubes. Systematic layered analysis ensures every single hidden block is "
            "accounted for completely and accurately."
        ),
        "checkpoints": [
            {
                "question": "Why is counting only the cubes visible from the front view insufficient for finding total volume?",
                "options": ["Because cubes change shape when viewed", "Because upper cubes rest on hidden support cubes directly beneath them", "Because bottom cubes weigh more", "Because front cubes are always transparent"],
                "answer": 1,
                "explanation": "In physical gravity, elevated blocks must rest on lower support blocks that may be completely hidden from front view."
            },
            {
                "question": "A cube structure has three vertical columns with heights 3, 2, and 1. What is the total number of unit cubes?",
                "options": ["5 unit cubes", "6 unit cubes", "7 unit cubes", "9 unit cubes"],
                "answer": 1,
                "explanation": "Summing column heights gives 3 + 2 + 1 = 6 unit cubes in total."
            }
        ]
    },
    {
        "id": 8,
        "title": "Isometric Net Matching",
        "lecture": (
            "Representing three-dimensional objects on a flat sheet of paper is an essential skill for engineers and designers. To "
            "create realistic three-dimensional perspective drawings, mathematicians and architects use triangular dot paper, also "
            "widely known as isometric dot paper. On an isometric grid, the dots form repeating equilateral triangles. Vertical lines "
            "are drawn straight up and down along the grid columns, while receding depth edges angle upward at thirty degrees. This "
            "allows cubes to be drawn without optical perspective distortion, showing the top, front, and side faces clearly in true "
            "proportion. Alongside isometric grid drawing, matching flat two-dimensional nets to their folded three-dimensional "
            "shapes requires sharp spatial visualization and practice. A cube has exactly eleven distinct valid nets composed of six "
            "connected squares. The most familiar is the Latin cross net, with four squares in a straight row and two lateral wings. "
            "When mentally folding this net, the four central squares form the vertical walls, while the side flaps fold over to cap "
            "the top and bottom. Beware of invalid nets: if two squares end up on the exact same face when folded, they will overlap, "
            "leaving an opposite side completely open. Mastering isometric nets bridges the flat page and solid three-dimensional space "
            "with immense clarity."
        ),
        "checkpoints": [
            {
                "question": "How many distinct valid 2D nets of 6 connected squares can fold into a closed 3D cube?",
                "options": ["6 valid nets", "8 valid nets", "11 valid nets", "16 valid nets"],
                "answer": 2,
                "explanation": "There are exactly 11 distinct hexomino arrangements that successfully fold into a complete, closed 3D cube."
            },
            {
                "question": "What happens when an invalid net with two adjacent flaps folding to the same position is assembled?",
                "options": ["It forms a sphere", "The flaps overlap, leaving one face open and unclosed", "It forms a pyramid", "It doubles in volume"],
                "answer": 1,
                "explanation": "If two flaps overlap on the same side, one face is left uncovered, failing to enclose the solid cube."
            }
        ]
    }
]

if __name__ == '__main__':
    for s in slides_part1:
        wc = len(s['lecture'].split())
        title_wc = len(s['title'].split())
        print(f"Slide {s['id']}: '{s['title']}' (Title: {title_wc} words, Lecture: {wc} words)")
        assert 1 <= title_wc <= 3, f"Title length violation in slide {s['id']}"
        assert 195 <= wc <= 215, f"Lecture word count {wc} out of range in slide {s['id']}"
    print("Part 1: All 8 slides verified successfully!")
