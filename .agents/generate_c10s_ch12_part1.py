# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 12: Part 1 (Slides 1 to 8)
Magnetic Effects of Electric Current
"""

import json

slides_part1 = [
    {
        "id": 1,
        "title": "Oersted Discovery Experiment",
        "subtitle": "Activity 12.1 & Hans Christian Oersted's 1820 Breakthrough",
        "speech": "In 1820, the Danish physicist Hans Christian Oersted made an epochal discovery that permanently united the separate scientific realms of electricity and magnetism. While setting up an electric circuit in his laboratory, he observed that a compass needle resting near a straight, thick copper wire deflected whenever current flowed through the conductor. When the electric current ceased, the needle promptly returned to its natural North-South alignment along Earth's geomagnetic field. This historic breakthrough established that moving electric charges directly generate a surrounding magnetic field. A compass needle is simply a tiny permanent magnet pivoted on a delicate friction-free axis so it rotates freely in the horizontal plane. The needle deflects because the magnetic field produced by the current exerts an instantaneous mechanical torque on the magnetic poles of the compass. Oersted's discovery laid the intellectual groundwork for electromagnets, electric motors, dynamos, telecommunications, radio, television, and modern fiber optics. In international scientific honor, the historical cgs unit of magnetic field strength is named the oersted. By grasping this foundational relationship between electrical current and magnetic disturbance, we commence our systematic study of electromagnetic phenomena, exploring how magnetic force fields interact with matter throughout nature and engineering.",
        "checkpoints": [
            {
                "question": "What primary phenomenon did Oersted observe in his historic 1820 laboratory experiment?",
                "options": [
                    "A compass needle deflected whenever electric current flowed through an adjacent wire",
                    "A copper wire melted spontaneously when placed near a natural lodestone",
                    "Electric sparks leaped continuously across open air gaps between two magnets",
                    "A compass needle lost its intrinsic magnetism permanently near a battery"
                ],
                "answer": 0,
                "hint": "Recall the behavior of a freely pivoted magnetic needle near a current-carrying copper conductor.",
                "explanation": "Oersted observed that a magnetic compass needle deflected when an electric current flowed through an adjacent straight copper conductor, proving electricity generates magnetism."
            },
            {
                "question": "Why does a compass needle experience deflection near a current-carrying conductor?",
                "options": [
                    "The current creates a magnetic field that exerts a magnetic torque on the needle",
                    "Static electrical charges on the needle attract the copper conductor wire",
                    "Atmospheric air heating pushes the needle sideways by convective draft",
                    "Gravitational pull of flowing electrons pulls the compass needle toward the battery"
                ],
                "answer": 0,
                "hint": "Consider the magnetic interaction between the field created by current and the compass magnet.",
                "explanation": "The electric current produces a magnetic field in the surrounding space, which exerts a magnetic force and torque on the magnetic poles of the compass needle."
            }
        ]
    },
    {
        "id": 2,
        "title": "Magnetic Field Lines",
        "subtitle": "Magnetic Fields, Poles & Iron Filings Alignment Pattern",
        "speech": "The region surrounding any magnet where its magnetic force can be detected by other magnetic objects is defined as a magnetic field. A magnetic compass needle is itself a miniature bar magnet whose ends point approximately toward the geographic North and South poles. The end pointing toward the geographic north is termed the north-seeking pole or simply the North pole, while the opposite end is the south-seeking or South pole. Like poles repel each other, whereas unlike poles mutually attract. In Activity 12.2, a bar magnet is placed at the center of a smooth cardboard sheet and fine iron filings are sprinkled uniformly over its surface. When the cardboard is gently tapped with a finger, the iron filings spontaneously rearrange themselves into beautiful, symmetrical curved lines. This striking pattern emerges because the magnetic field exerts forces on each tiny iron filing, turning it into a momentary induced magnetic dipole. The filings align along lines of magnetic force, providing a vivid visual map of the invisible force field. Near the poles of the magnet, the filings cluster densely together, directly demonstrating that the magnetic field possesses its highest intensity in the immediate vicinity of the magnetic poles.",
        "checkpoints": [
            {
                "question": "Why do sprinkled iron filings align in curved patterns around a bar magnet upon tapping?",
                "options": [
                    "Each filing becomes an induced magnetic dipole aligning along lines of force",
                    "The filings melt and flow into grooves carved into the cardboard surface",
                    "Static electricity attracts the iron filings toward the central cardboard axis",
                    "Frictional vibrations magnetize the cardboard into circular electrostatic zones"
                ],
                "answer": 0,
                "hint": "Think about how iron reacts to an external magnetic field and aligns with field vectors.",
                "explanation": "The magnetic field of the bar magnet exerts forces on the iron filings, inducing temporary magnetic poles in them so they align along the local lines of magnetic force."
            },
            {
                "question": "What does a dense clustering of iron filings near the ends of a bar magnet indicate?",
                "options": [
                    "The magnetic field strength is strongest at the magnetic poles",
                    "The cardboard is thinner near the outer edges of the bar magnet",
                    "The magnet has lost its polarity at those specific edge points",
                    "The filings have experienced greater gravitational pull near the pole ends"
                ],
                "answer": 0,
                "hint": "Crowded field lines indicate regions where magnetic force has maximum magnitude.",
                "explanation": "Crowded filings near the poles demonstrate that the magnetic field has its highest magnitude and exerts the strongest forces near the magnet's poles."
            }
        ]
    },
    {
        "id": 3,
        "title": "Field Line Tracing",
        "subtitle": "Activity 12.3 Plotting Compass Step-by-Step Mapping",
        "speech": "To trace the exact geometry of magnetic field lines around a bar magnet, Activity 12.3 utilizes a small plotting compass. The bar magnet is fixed on a white drawing sheet and its outer boundary outlined with pencil. When the plotting compass is placed near the North pole of the bar magnet, its south pole is strongly attracted toward the magnet's North pole, while its north pole points directly outward into free space. Small pencil dots are marked at the exact positions of the two compass needle tips. The compass is then repositioned so that its south pole occupies the dot previously marked by its north pole. Repeating this systematic stepping process across the entire sheet yields a clear sequence of guide points. Joining these points with a smooth curve produces an authentic magnetic field line. By repeating the procedure from various starting points around the North pole, an entire family of continuous curves is plotted. Outside the bar magnet, these field lines always emerge from the North pole and merge gracefully into the South pole. Inside the magnet, the lines continue traveling from the South pole back to the North pole. Consequently, magnetic field lines form unbroken, continuous closed loops spanning space.",
        "checkpoints": [
            {
                "question": "What is the conventional direction of magnetic field lines outside a bar magnet?",
                "options": [
                    "Emerging from the North pole and entering the South pole",
                    "Emerging from the South pole and entering the North pole",
                    "Radiating radially outwards in straight lines from all surfaces",
                    "Flowing exclusively clockwise around the magnetic equator"
                ],
                "answer": 0,
                "hint": "Recall the path followed by an isolated north-seeking magnetic pole outside the magnet.",
                "explanation": "By international scientific convention, magnetic field lines outside a magnet emerge from the North pole and curve around to merge into the South pole."
            },
            {
                "question": "Why are magnetic field lines described as continuous closed loops?",
                "options": [
                    "They continue inside the magnet from the South pole back to the North pole",
                    "They stop abruptly at the South pole without penetrating the magnet body",
                    "They form concentric circles exclusively in empty outer atmospheric space",
                    "They reflect back to the North pole along the exact same path they emerged"
                ],
                "answer": 0,
                "hint": "Consider the direction of field lines both outside and inside the body of the magnet.",
                "explanation": "Outside the magnet field lines go from North to South, while inside the magnet they travel from South to North, forming unbroken, continuous closed loops."
            }
        ]
    },
    {
        "id": 4,
        "title": "Field Line Properties",
        "subtitle": "Vector Nature, Line Density & The Non-Intersection Principle",
        "speech": "Magnetic field is a physical vector quantity that possesses both magnitude and spatial direction, classifying it unambiguously as an essential physical force field. The direction of the magnetic field at any given point is taken as the direction in which the north pole of a plotting compass needle points when placed at that exact location. The tangent drawn to a magnetic field line at any point gives the instantaneous direction of the local magnetic field vector. The relative strength or magnitude of the magnetic field is indicated by the degree of closeness or crowding of the field lines. Where the lines lie densely packed together, such as near the magnetic poles, the magnetic field is strong and exerts powerful forces on magnetic bodies. Where the field lines spread far apart, the field is correspondingly weak. A paramount fundamental property is that no two magnetic field lines are ever found to cross or intersect each other. If two field lines were to intersect at a single geometric point, it would mean that a compass needle placed at that exact intersection would have to point simultaneously in two different directions, which is physically impossible. Hence, field lines remain distinctly separate everywhere.",
        "checkpoints": [
            {
                "question": "Why can two magnetic field lines never cross or intersect each other?",
                "options": [
                    "A compass needle at the intersection cannot point in two directions at once",
                    "Magnetic forces between lines cause them to neutralize and vanish completely",
                    "Field lines carry identical electric charges that repel each other to infinity",
                    "The magnetic medium acts as a physical barrier that prevents line convergence"
                ],
                "answer": 0,
                "hint": "Think about what a compass needle would do if placed at an intersection point.",
                "explanation": "If two field lines intersected, the compass needle at that point would have to point in two different directions simultaneously, which is a physical impossibility."
            },
            {
                "question": "How is the relative strength of a magnetic field represented pictorially?",
                "options": [
                    "By the degree of closeness and crowding of the magnetic field lines",
                    "By the color and thickness of individual pencil line tracings",
                    "By the physical length of the bar magnet placed on the paper",
                    "By the speed at which iron filings fall under local gravity"
                ],
                "answer": 0,
                "hint": "Regions with closely spaced lines correspond to stronger magnetic forces.",
                "explanation": "The magnitude of the magnetic field is indicated by the crowding of field lines; densely packed lines denote a strong field, while sparse lines represent a weak field."
            }
        ]
    },
    {
        "id": 5,
        "title": "Current Direction Influence",
        "subtitle": "Activity 12.4 Deflection Reversal & Polarity Dependence",
        "speech": "Activity 12.4 systematically examines how changing the direction of electric current alters the surrounding magnetic field. A long straight copper wire is connected into an electrical circuit through a plug key, an ammeter, a variable rheostat, and a direct current battery source. The wire is oriented horizontally along the geographic North-South direction, positioned parallel directly over a small compass needle resting steadily on a laboratory table. When the plug key is closed and current flows from North to South through the overhead conductor, the north pole of the compass needle instantly deflects toward the East. Next, the battery connections are reversed so that the electric current flows through the copper wire from South to North. Upon closing the circuit, the north pole of the compass needle deflects in the opposite direction, pointing toward the West. This clear observation proves two critical principles of electromagnetism. First, the magnetic field is actively generated by the moving charges of the electric current itself. Second, the spatial direction of the magnetic field vector reverses immediately whenever the direction of electric current in the conductor is reversed. Electric current direction directly dictates the orientation and polarity of the generated magnetic field.",
        "checkpoints": [
            {
                "question": "What happens to the compass needle when the current direction through an overhead wire is reversed?",
                "options": [
                    "Its deflection reverses to point in the opposite geographic direction",
                    "Its needle stops moving entirely and points permanently due North",
                    "Its needle spins continuously in full 360-degree clockwise rotations",
                    "Its needle demagnetizes and drops flat against the compass glass base"
                ],
                "answer": 0,
                "hint": "Remember how changing current polarity changes the direction of the magnetic field.",
                "explanation": "Reversing the direction of electric current reverses the direction of the generated magnetic field, causing the compass needle's deflection to flip to the opposite side."
            },
            {
                "question": "If current flows from North to South in a wire directly over a compass, which way does the North pole deflect?",
                "options": [
                    "Toward the East",
                    "Toward the West",
                    "Directly toward the ceiling vertically",
                    "It experiences zero deflection"
                ],
                "answer": 0,
                "hint": "Recall Activity 12.4: current North-to-South overhead yields an eastward needle deflection.",
                "explanation": "According to Activity 12.4 (and Ampere's swimming rule), when current flows from North to South over a compass needle, the north pole deflects toward the East."
            }
        ]
    },
    {
        "id": 6,
        "title": "Straight Conductor Field",
        "subtitle": "Activity 12.5 Concentric Rings Pattern & Governing Variables",
        "speech": "To investigate the geometric structure of the magnetic field produced by a straight current-carrying wire, Activity 12.5 passes a thick vertical copper wire through the center of a horizontal cardboard sheet. Fine iron filings are sprinkled evenly across the cardboard surface, and a variable electric current is supplied by a battery pack through a sensitive rheostat. When the plug key is inserted and electric current flows vertically through the wire, tapping the cardboard causes the iron filings to arrange themselves in a series of concentric circles centered precisely on the wire. These concentric circles represent the magnetic field lines. When a compass is placed at any point on a circle, its needle aligns tangentially to that circle. When the current through the wire is increased by adjusting the rheostat, the needle deflection becomes sharper and larger, showing that the magnetic field strength B is directly proportional to current I. Conversely, when the compass is moved radially farther away from the wire, the needle deflection diminishes, and the concentric circles spread wider apart. This proves that the magnetic field strength is inversely proportional to distance r from the conductor: B is proportional to I divided by r.",
        "checkpoints": [
            {
                "question": "What geometric pattern do magnetic field lines form around a straight current-carrying conductor?",
                "options": [
                    "Concentric circles centered on the axis of the conductor wire",
                    "Parallel straight lines extending outward radially in all directions",
                    "Parabolic curves bending toward the negative terminal of the cell",
                    "Elliptical spirals that collapse into the center of the conductor"
                ],
                "answer": 0,
                "hint": "Activity 12.5 iron filings form concentric rings around the vertical wire.",
                "explanation": "Magnetic field lines around a straight current-carrying conductor form concentric circles centered on the wire in planes perpendicular to the conductor."
            },
            {
                "question": "How does the magnetic field strength B change as the radial distance r from the wire increases?",
                "options": [
                    "B decreases inversely with distance (B ∝ 1/r)",
                    "B increases directly with the square of distance (B ∝ r²)",
                    "B remains perfectly constant regardless of distance",
                    "B oscillates sinusoidally between positive and negative values"
                ],
                "answer": 0,
                "hint": "As you move farther from the wire, the magnetic effect weakens.",
                "explanation": "The magnetic field strength produced by a straight conductor is inversely proportional to the distance from the wire (B ∝ 1/r), decreasing as distance increases."
            }
        ]
    },
    {
        "id": 7,
        "title": "Right Hand Rule",
        "subtitle": "Rule Statement, Corkscrew Analogy & Overhead Line Example 12.1",
        "speech": "The Right-Hand Thumb Rule provides a remarkably simple and convenient method to determine the direction of magnetic field lines around a straight current-carrying conductor. The rule states: imagine grasping the current-carrying wire with your right hand such that your outstretched thumb points in the direction of conventional electric current; then your fingers curled around the wire indicate the direction of the magnetic field lines. This handy mnemonic is also widely known as Maxwell's corkscrew rule: if we imagine driving a right-handed corkscrew in the direction of electric current, then the direction in which the corkscrew handle is turned represents the direction of the surrounding magnetic field lines. In NCERT Example 12.1, a horizontal power line carries an electric current flowing from East to West. Applying the right-hand thumb rule by pointing the right thumb Westward, an observer looking at the line from the East end sees the curled fingers circulating in a clockwise sense below the wire and above it. Looking from the West end, the circulating field appears counter-clockwise. Below the wire, the field points toward the North; above the wire, it points South. This elegant rule reliably establishes field orientations in diverse three-dimensional configurations.",
        "checkpoints": [
            {
                "question": "In the Right-Hand Thumb Rule, what physical quantity does the outstretched thumb represent?",
                "options": [
                    "Direction of conventional electric current flowing in the conductor",
                    "Direction of the mechanical magnetic force acting on the wire",
                    "Direction of the geographic North pole of planet Earth",
                    "Direction of electron drift velocity inside the metal lattice"
                ],
                "answer": 0,
                "hint": "The thumb points along the wire in the direction electric current travels.",
                "explanation": "In the Right-Hand Thumb Rule, the outstretched thumb points along the direction of conventional electric current, while the curled fingers indicate magnetic field lines."
            },
            {
                "question": "According to Example 12.1, what is the magnetic field direction directly below an East-to-West power line?",
                "options": [
                    "Directed toward the North (clockwise when viewed from the East)",
                    "Directed toward the South (counter-clockwise from the East)",
                    "Directed vertically upward toward the overhead sky",
                    "Directed due West parallel along the length of the wire"
                ],
                "answer": 0,
                "hint": "Point your right thumb West: your fingers sweep toward the North under the wire.",
                "explanation": "Pointing the right thumb Westward, the curled fingers sweep from East to North underneath the wire, so the magnetic field directly below the conductor points toward the North."
            }
        ]
    },
    {
        "id": 8,
        "title": "Circular Loop Field",
        "subtitle": "Figures 12.8 & 12.9 Superposition & Uniform Central Field",
        "speech": "When a straight wire is bent into a circular loop and an electric current is passed through it, the magnetic field pattern develops remarkable geometric properties. As shown in Figures 12.8 and 12.9, concentric circular field lines form around every infinitesimal segment of the circular wire. Near the wire rim, the circles are small and clearly defined. As we move away from the wire toward the center of the loop, the concentric circles expand dramatically in radius. By the time we reach the geometric center of the circular loop, the arcs of these large circles appear as straight, parallel lines perpendicular to the plane of the loop. Applying the right-hand thumb rule to every section of the loop reveals that all wire segments contribute magnetic field lines that enter the loop face in the exact same direction and emerge together from the opposite face. Inside the boundary of the loop, all individual field contributions add up constructively by vector superposition. Consequently, one face of the circular coil behaves as a magnetic North pole where field lines emerge, while the opposite face behaves as a magnetic South pole where field lines enter, transforming the loop into a magnetic dipole.",
        "checkpoints": [
            {
                "question": "What appearance do magnetic field lines take near the center of a circular current loop?",
                "options": [
                    "Straight parallel lines perpendicular to the plane of the loop",
                    "Tightly wound concentric spirals collapsing onto the wire",
                    "Random criss-crossing lines with zero net magnetic field",
                    "Semicircles that reflect backwards toward the battery terminals"
                ],
                "answer": 0,
                "hint": "As the concentric circles expand near the center, their arcs straighten out.",
                "explanation": "Near the center of the circular loop, the expanding concentric circles become so large that their arcs appear as straight, parallel lines perpendicular to the coil's plane."
            },
            {
                "question": "Why does a current-carrying circular loop act like a magnetic dipole?",
                "options": [
                    "Field lines emerge from one face (North) and enter the other face (South)",
                    "The wire produces static positive charges on top and negative on bottom",
                    "Electric current cannot pass through the center of a circular loop",
                    "Earth's gravity bends the current into two unequal physical halves"
                ],
                "answer": 0,
                "hint": "Field lines exit from one face and enter into the opposite face.",
                "explanation": "Because field lines pass through the loop in the same direction, they emerge from one face (acting as a North pole) and enter the opposite face (acting as a South pole), forming a magnetic dipole."
            }
        ]
    }
]

# Validation
forbidden_personas = ["Dr.", "Dr ", "Doctor", "Sir ", "Madam", "Mr.", "Mr ", "Mrs.", "Mrs ", "Prof.", "Professor", "Raghav"]

for s in slides_part1:
    sid = s["id"]
    title = s["title"]
    title_words = len(title.split())
    assert 1 <= title_words <= 3, f"Slide {sid} title '{title}' must be 1 to 3 words, got {title_words}"

    slide_str = json.dumps(s)
    for forb in forbidden_personas:
        assert forb.lower() not in slide_str.lower(), f"Slide {sid} contains forbidden term '{forb}'"

    wc = len(s["speech"].split())
    assert 195 <= wc <= 215, f"Slide {sid} speech word count out of range: {wc} words"
    assert len(s["checkpoints"]) == 2, f"Slide {sid} must have 2 checkpoints"
    for cidx, cp in enumerate(s["checkpoints"]):
        assert len(cp["options"]) == 4, f"Slide {sid} checkpoint {cidx+1} must have 4 options"

with open(".agents/c10s_ch12_part1.json", "w", encoding="utf-8") as f:
    json.dump(slides_part1, f, indent=2, ensure_ascii=False)

print("Part 1 (Slides 1 to 8) validated and saved successfully!")
