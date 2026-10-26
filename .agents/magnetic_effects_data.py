"""
Comprehensive dataset for NCERT Class 10 Science Chapter 12: Magnetic Effects of Electric Current.
Contains 16 content slides covering all lines, figures, activities, and exercises + 4 dedicated quiz challenge slides (40 questions).
"""

CONTENT_SLIDES = [
    {
        "id": 1,
        "title": "Oersted’s Discovery & The Electro-Magnetic Link",
        "subtitle": "Chapter 12 • Page 195",
        "tag": "Section 12.1 Historical Discovery",
        "quote": "In 1820, a dancing compass needle unveiled the profound unity between electricity and magnetism.",
        "lead": "Hans Christian Oersted proved that an electric current in a metallic wire generates a magnetic field in the surrounding space.",
        "narration": "Welcome to Chapter 12: Magnetic Effects of Electric Current! In the previous chapter, we explored the heating effect of electric current. But electric current produces another fundamental effect: an electric current-carrying wire behaves like a magnet. In 1820, Danish physicist Hans Christian Oersted accidentally discovered that a compass needle placed near a current-carrying wire gets deflected, establishing for the first time that electricity and magnetism are intimately linked.",
        "theory_blocks": [
            {
                "title": "Activity 12.1: The Deflected Compass Needle",
                "content": "<p class='mb-2 text-slate-300'>In Activity 12.1, a straight thick copper wire $XY$ is placed in an electric circuit with a compass positioned horizontally below it:</p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li>When the key is open (no current), the compass needle aligns strictly along the Earth's magnetic North-South direction.</li><li>When current flows through the copper wire, the <strong>compass needle is immediately deflected</strong>!</li><li><strong>Conclusion:</strong> The flow of electric charges in a metallic conductor produces a <strong>magnetic field</strong> in the surrounding space.</li></ul>"
            },
            {
                "title": "Hans Christian Oersted (1777–1851)",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li>Hans Christian Oersted was a Danish scientist whose 1820 discovery established the field of <strong>electromagnetism</strong>.</li><li>His insight paved the way for modern electrical technologies including radios, televisions, electric motors, and fiber optics.</li><li>In his honour, the CGS unit of magnetic field strength is named the <strong>oersted</strong>.</li><li>This discovery raised the reciprocal question: if electric currents create magnetic fields, can moving magnets create electric currents? Yes, as explored in electromagnetic induction!</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "What phenomenon was observed by Hans Christian Oersted in 1820 near a current-carrying conductor?",
                "options": [
                    "A chemical color change occurred in the copper wire",
                    "A compass needle placed near the wire was deflected from its North-South alignment",
                    "The wire became completely weightless",
                    "Sparks of static electricity jumped continuously from the wire"
                ],
                "ans": 1,
                "solution": "Oersted observed that a magnetic compass needle deflected whenever an electric current passed through a nearby wire, proving current produces a magnetic field (NCERT Page 195)."
            },
            {
                "q": "The unit of magnetic field strength named in honour of Hans Christian Oersted is the:",
                "options": [
                    "Tesla",
                    "Oersted",
                    "Ampere",
                    "Coulomb"
                ],
                "ans": 1,
                "solution": "The unit of magnetic field strength in the CGS system is named the oersted in honor of Hans Christian Oersted (NCERT Page 195)."
            }
        ]
    },
    {
        "id": 2,
        "title": "Magnetic Field & Iron Filings Pattern",
        "subtitle": "Chapter 12 • Page 196",
        "tag": "Section 12.1 Field & Pattern",
        "quote": "A magnetic field is the region of unseen magnetic influence; iron filings render its invisible force lines visible.",
        "lead": "A compass needle is a small bar magnet whose north-seeking pole aligns with external magnetic forces.",
        "narration": "What is a magnetic field? A compass needle is simply a small bar magnet. Its north-seeking end points towards geographic north, and its south-seeking end points south. Like poles repel each other, while unlike poles attract. When iron filings are sprinkled around a bar magnet in Activity 12.2 and gently tapped, they arrange themselves into graceful curved lines representing the magnetic field lines.",
        "theory_blocks": [
            {
                "title": "Compass Needle & Pole Properties",
                "content": "<p class='mb-2 text-slate-300'>A compass needle is a miniature pivot-mounted bar magnet:</p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li>The end pointing approximately towards the geographic north is called the <strong>north-seeking</strong> or <strong>north pole</strong>.</li><li>The opposite end is called the <strong>south-seeking</strong> or <strong>south pole</strong>.</li><li><strong>Fundamental Law of Magnetism:</strong> <strong>Like poles repel</strong> each other (North repels North, South repels South), while <strong>unlike poles attract</strong> (North attracts South).</li><li><strong>Intext Q1:</strong> A compass needle deflects near a bar magnet because both possess magnetic fields; the magnet exerts magnetic forces of attraction and repulsion on the needle's poles.</li></ul>"
            },
            {
                "title": "Activity 12.2: Iron Filings Alignment Pattern",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Procedure:</strong> Fix paper on a drawing board, place a bar magnet in the center, sprinkle iron filings uniformly using a salt-sprinkler, and tap the board gently.</li><li><strong>Observation (Fig 12.2):</strong> The iron filings rearrange themselves into a striking pattern of smooth concentric curves converging at the poles!</li><li><strong>Definition of Magnetic Field:</strong> The region surrounding a magnet in which the force of the magnet can be detected is said to have a <strong>magnetic field</strong>.</li><li>The lines along which the iron filings align themselves represent <strong>magnetic field lines</strong>.</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "Why does a compass needle get deflected when brought near a bar magnet?",
                "options": [
                    "Due to electrostatic friction between the glass case and the magnet",
                    "Because the compass needle is itself a small bar magnet experiencing magnetic forces from the external magnet",
                    "Because gravitational pull from the magnet tilts the needle pivot",
                    "Because air currents are displaced around the magnetic poles"
                ],
                "ans": 1,
                "solution": "A compass needle is a small permanent magnet. When placed in the magnetic field of a bar magnet, its poles experience magnetic forces that cause it to rotate and align with the field lines (NCERT Page 196, Intext Q1)."
            },
            {
                "q": "What physical entity do the aligned curved patterns of iron filings around a bar magnet represent?",
                "options": [
                    "Lines of gravitational force",
                    "Magnetic field lines outlining the magnetic field",
                    "Electric charge contours leaking from the poles",
                    "Thermal convection pathways"
                ],
                "ans": 1,
                "solution": "The iron filings align themselves along the magnetic field lines, visually demonstrating the direction and geometry of the magnetic field surrounding the bar magnet (NCERT Page 196)."
            }
        ]
    },
    {
        "id": 3,
        "title": "Plotting Field Lines & Closed Curve Geometry",
        "subtitle": "Chapter 12 • Pages 196–197",
        "tag": "Activity 12.3 Field Lines",
        "quote": "Magnetic field lines emerge from the North pole, enter the South pole, and return within the magnet to form unbroken closed loops.",
        "lead": "Activity 12.3 details the step-by-step compass plotting method that maps the continuous closed loops of a bar magnet.",
        "narration": "Let us trace magnetic field lines with a compass needle in Activity 12.3. Starting near the north pole of a bar magnet, we mark the positions of the needle tips, move the compass so its south pole occupies the previous north dot, and repeat until reaching the south pole. Joining these dots yields smooth curves. Notice that magnetic field lines are continuous closed curves: outside the magnet they run from North to South, but inside the magnet they run from South to North!",
        "theory_blocks": [
            {
                "title": "Activity 12.3: Compass Plotting Procedure",
                "content": "<p class='mb-2 text-slate-300'>Step-by-step field line mapping (Fig 12.3):</p><ol class='list-decimal pl-5 space-y-1.5 text-slate-300'><li>Place a compass near the north pole of a bar magnet. The south pole of the needle points toward the magnet's north pole; the north pole points away.</li><li>Mark the position of both ends with fine pencil dots.</li><li>Move the compass so its south pole occupies the dot previously occupied by its north pole.</li><li>Repeat until reaching the south pole of the magnet.</li><li>Join the dots with a smooth curve. Repeating this from various starting points produces the complete field map of <strong>Fig 12.4</strong>!</li></ol>"
            },
            {
                "title": "Direction & Closed Loop Characteristic",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Conventional Direction:</strong> The direction of the magnetic field is taken to be the direction in which a <strong>hypothetical free north pole would move</strong>.</li><li><strong>Outside the Magnet:</strong> Field lines <strong>emerge from the North pole and merge at the South pole</strong>.</li><li><strong>Inside the Magnet:</strong> Field lines continue <strong>from the South pole to the North pole</strong>.</li><li><strong>Continuous Closed Loops:</strong> Unlike electrostatic field lines (which start on positive charges and terminate on negative charges), magnetic field lines have no free monopole ends—they form <strong>continuous, unbroken closed loops</strong>!</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "What is the direction of magnetic field lines inside a permanent bar magnet?",
                "options": [
                    "From North pole to South pole",
                    "From South pole to North pole",
                    "Radially outward in all directions",
                    "Zero, because magnetic fields cannot penetrate solid iron"
                ],
                "ans": 1,
                "solution": "Inside the magnet, the direction of field lines is from its south pole to its north pole, completing unbroken closed continuous curves (NCERT Page 197)."
            },
            {
                "q": "How does the deflection of a plotting compass needle change as it is moved closer to the poles of a magnet along a field line?",
                "options": [
                    "The deflection drops to zero",
                    "The deflection increases as the needle approaches the poles",
                    "The deflection reverses direction every 2 centimeters",
                    "The needle spins uncontrollably"
                ],
                "ans": 1,
                "solution": "The deflection in the compass needle increases as it is moved toward the poles, because the magnetic field is strongest and field lines are most crowded near the poles (NCERT Page 197, Activity 12.3)."
            }
        ]
    },
    {
        "id": 4,
        "title": "Properties of Field Lines & The Non-Intersection Law",
        "subtitle": "Chapter 12 • Page 197",
        "tag": "Section 12.1 Properties & Proof",
        "quote": "No two magnetic field lines can ever intersect—for at an intersection, a compass would face the physical impossibility of pointing in two directions at once.",
        "lead": "Magnetic field is a vector quantity; line density indicates magnitude while tangent arrows denote field direction.",
        "narration": "What are the key properties of magnetic field lines? First, the magnetic field is a vector quantity possessing both magnitude and direction. Second, the relative strength of the field is shown by the degree of closeness of the field lines: where lines are crowded together near the poles, the field is strongest. Third, and most importantly, no two field lines can ever intersect! If they did, a compass placed at the intersection point would have to point in two different directions at the same time, which is physically impossible.",
        "theory_blocks": [
            {
                "title": "Vector Nature & Degree of Closeness",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Vector Quantity:</strong> Magnetic field has both <strong>magnitude</strong> (strength) and <strong>direction</strong>.</li><li><strong>Tangent Direction:</strong> The tangent to a field line at any point gives the direction of the magnetic field vector $\\vec{B}$ at that point.</li><li><strong>Degree of Closeness:</strong> The relative strength of the magnetic field is shown by how crowded the field lines are.<br>• <strong>Near the Poles:</strong> Field lines are densely packed $\\implies$ <strong>Field is strongest</strong>.<br>• <strong>Far from the Magnet:</strong> Field lines spread wide apart $\\implies$ <strong>Field is weak</strong>.</li><li><strong>Uniform Field:</strong> Represented by <strong>equidistant, parallel straight lines</strong>.</li></ul>"
            },
            {
                "title": "The Non-Intersection Proof (Board Favorite!)",
                "content": "<p class='mb-2 text-slate-300'><strong>Why do two magnetic field lines never cross each other?</strong></p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li>Assume for contradiction that two field lines could intersect at point $P$.</li><li>The compass needle always points along the net resultant magnetic field at any point.</li><li>At an intersection point $P$, there would be two tangents, meaning <strong>two distinct directions of magnetic field at the same single point</strong>!</li><li>Consequently, a compass needle placed at $P$ would have to point in <strong>two different directions simultaneously</strong>.</li><li>Since this is physically impossible, <strong>no two magnetic field lines can ever intersect</strong>!</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "Why is it physically impossible for two magnetic field lines to cross or intersect each other?",
                "options": [
                    "Because field lines possess mass and would physically collide and bounce",
                    "Because at the point of intersection, a compass needle would have to point in two different directions simultaneously, which is impossible",
                    "Because crossing lines would trigger an electrical short circuit in the air",
                    "Because magnetic fields only exist in two dimensions"
                ],
                "ans": 1,
                "solution": "If two field lines intersected, it would mean that at that point the magnetic field has two directions, so a compass needle would have to point in two directions at once, which is impossible (NCERT Page 197 & Page 200, Intext Q3)."
            },
            {
                "q": "How is a region of uniform magnetic field represented diagrammatically?",
                "options": [
                    "By concentric circles of varying radii",
                    "By diverging radial arrows",
                    "By a set of equidistant, parallel straight lines",
                    "By random zigzag lines"
                ],
                "ans": 2,
                "solution": "A uniform magnetic field has constant magnitude and direction at all points and is represented by parallel, equidistant straight lines (NCERT Page 201, Intext Q2)."
            }
        ]
    },
    {
        "id": 5,
        "title": "Magnetic Field of a Straight Conductor & Current Reversal",
        "subtitle": "Chapter 12 • Pages 197–198",
        "tag": "Section 12.2 Activity 12.4",
        "quote": "Reversing the flow of electric current reverses the magnetic field polarity in surrounding space.",
        "lead": "Activity 12.4 demonstrates how compass needle deflection flips when the battery polarity is inverted.",
        "narration": "Now let us examine how electric current produces a magnetic field around a straight conductor. In Activity 12.4, a straight copper wire is placed parallel to and above a compass needle. When current flows from North to South, the compass north pole deflects towards the East. But when we reverse the battery connections so that current flows from South to North, the needle deflects towards the West! This proves that reversing the current reverses the direction of the magnetic field.",
        "theory_blocks": [
            {
                "title": "Activity 12.4: Circuit Setup & Deflection Test",
                "content": "<p class='mb-2 text-slate-300'>Testing current direction vs field deflection (Fig 12.5):</p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li>A straight copper wire is placed parallel to and positioned directly over a magnetic compass needle aligned in the magnetic meridian.</li><li><strong>Case (a) Current from North to South:</strong> When the key is plugged, the north pole of the compass needle deflects <strong>towards the EAST</strong>!</li><li><strong>Case (b) Current Reversed (South to North):</strong> When cell connections are flipped, the north pole deflects in the opposite direction, <strong>towards the WEST</strong>!</li><li><strong>SNOW Rule:</strong> If current flows from <strong>S</strong>outh to <strong>N</strong>orth <strong>O</strong>ver the needle, the north pole deflects towards <strong>W</strong>est!</li></ul>"
            },
            {
                "title": "Physical Implications of Current Reversal",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li>The magnetic field surrounding a conductor is intimately tied to the velocity vector of the drifting charge carriers.</li><li>Inverting the direction of current reverses the magnetic field vectors at every point in space.</li><li>The magnitude of deflection also depends on current magnitude: increasing the current by adding more cells increases the deflection angle.</li><li>Moving the compass farther above or below the wire reduces the deflection angle.</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "According to Activity 12.4, when electric current flows from South to North in a wire placed directly over a compass, which way does the north pole deflect?",
                "options": [
                    "Towards the East",
                    "Towards the West",
                    "Directly upward toward the ceiling",
                    "It shows no deflection at all"
                ],
                "ans": 1,
                "solution": "When current flows from South to North over the needle, the north pole of the compass needle moves towards the West (SNOW rule) (NCERT Page 198, Activity 12.4 & Fig 12.5b)."
            },
            {
                "q": "What happens to the magnetic field around a conductor when the direction of electric current through it is reversed?",
                "options": [
                    "The magnetic field collapses permanently to zero",
                    "The direction of the magnetic field is also completely reversed",
                    "The magnetic field doubles in strength without changing direction",
                    "The magnetic field converts into an electrostatic charge"
                ],
                "ans": 1,
                "solution": "Reversing the direction of electric current reverses the direction of the magnetic field produced by it (NCERT Page 198)."
            }
        ]
    },
    {
        "id": 6,
        "title": "Concentric Circular Field Lines & The Inverse Distance Law",
        "subtitle": "Chapter 12 • Pages 198–199",
        "tag": "Section 12.2.1 Activity 12.5",
        "quote": "Around a straight current-carrying wire, magnetic field lines form concentric circles whose spacing widens with distance.",
        "lead": "Activity 12.5 uses iron filings on cardboard to reveal concentric circular field lines governed by B ∝ I and B ∝ 1/r.",
        "narration": "What is the geometric pattern of the magnetic field generated by a straight current-carrying wire? In Activity 12.5, a thick copper wire passes vertically through a cardboard sheet. Sprinkling iron filings and gently tapping reveals that the field lines form concentric circles centered directly on the wire. If we increase the current, the compass deflection increases, proving that the magnetic field B is directly proportional to current I. If we move the compass farther away, deflection decreases, proving B is inversely proportional to distance r.",
        "theory_blocks": [
            {
                "title": "Activity 12.5: Cardboard & Concentric Circles",
                "content": "<p class='mb-2 text-slate-300'>Setup with vertical thick copper wire $XY$ through horizontal cardboard (Fig 12.6):</p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li>Sprinkling iron filings and passing current through the wire causes the filings to align in <strong>concentric circles</strong> centered on the wire.</li><li>These concentric circles represent the <strong>magnetic field lines</strong> around a straight current-carrying conductor.</li><li>Placing a plotting compass at point $P$ indicates the tangential direction of the field lines.</li><li>Reversing current reverses the circular arrow directions from clockwise to anticlockwise or vice versa.</li></ul>"
            },
            {
                "title": "The Two Fundamental Proportionalities: B ∝ I and B ∝ 1/r",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>1. Direct Dependence on Current ($B \\propto I$):</strong> Increasing current via a rheostat increases compass needle deflection. Magnetic field strength is directly proportional to current.</li><li><strong>2. Inverse Dependence on Distance ($B \\propto 1/r$):</strong> Moving the compass to point $Q$ farther from the wire decreases deflection. Magnetic field decreases as distance increases.</li><li><strong>Visual Pattern:</strong> As distance $r$ increases, the concentric circular field lines become <strong>larger and larger</strong> and are spaced <strong>farther and farther apart</strong>!</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "Which of the following correctly describes the magnetic field lines near a long straight current-carrying wire?",
                "options": [
                    "The field consists of straight lines perpendicular to the wire",
                    "The field consists of radial lines originating from the wire",
                    "The field consists of concentric circles centred on the wire",
                    "The field consists of straight lines parallel to the wire"
                ],
                "ans": 2,
                "solution": "The magnetic field lines around a long straight current-carrying conductor form a pattern of concentric circles centered on the wire (NCERT Page 199 & Page 207, Exercise Q1)."
            },
            {
                "q": "If the electric current in a straight wire is doubled while the distance from the wire is doubled, what happens to the magnetic field strength?",
                "options": [
                    "It quadruples (4B)",
                    "It doubles (2B)",
                    "It remains unchanged (B)",
                    "It decreases to one-fourth (B/4)"
                ],
                "ans": 2,
                "solution": "Since B ∝ I / r, doubling current (2I) and doubling distance (2r) gives B' ∝ (2I)/(2r) = I/r = B (remains unchanged)."
            }
        ]
    },
    {
        "id": 7,
        "title": "The Right-Hand Thumb Rule & Maxwell’s Corkscrew Rule",
        "subtitle": "Chapter 12 • Pages 199–200",
        "tag": "Section 12.2.2 Right-Hand Rule",
        "quote": "Point your right thumb along the current, and your curled fingers declare the circular sweep of the magnetic field.",
        "lead": "The Right-Hand Thumb Rule provides an intuitive spatial guide for finding the direction of circular magnetic field lines.",
        "narration": "To determine the circular direction of magnetic field lines around a straight conductor, we use the Right-Hand Thumb Rule. Imagine grasping the conductor in your right hand with your thumb pointing in the direction of current flow. Your curled fingers wrapping around the conductor point in the direction of the magnetic field lines! This is also known as Maxwell's Corkscrew Rule: driving a right-handed corkscrew in the direction of current rotates the handle in the direction of the magnetic field.",
        "theory_blocks": [
            {
                "title": "Rule Statement & Visualization (Fig 12.7)",
                "content": "<p class='mb-2 text-slate-300'><strong>Right-Hand Thumb Rule Statement:</strong></p><p class='text-amber-400 font-mono font-bold text-xs sm:text-sm p-3 rounded-xl bg-slate-950 border border-slate-800 mb-2'>\"Imagine holding a current-carrying straight conductor in your right hand such that your thumb points in the direction of current. Then your curled fingers wrap around the conductor in the direction of the magnetic field lines.\"</p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Upward Current:</strong> Curled fingers wrap <strong>anticlockwise</strong> (when viewed from above).</li><li><strong>Downward Current:</strong> Curled fingers wrap <strong>clockwise</strong> (when viewed from above).</li><li><strong>Maxwell's Corkscrew Rule:</strong> Driving a corkscrew forward along current rotates the handle in the magnetic field direction.</li></ul>"
            },
            {
                "title": "Worked Example 12.1 (Horizontal Power Line)",
                "content": "<p class='mb-2 text-slate-300'><strong>Example 12.1:</strong> Current through a horizontal overhead power line flows from <strong>East to West</strong>. What is the direction of the magnetic field at a point directly below it and directly above it?</p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li>Point your right thumb towards the West (direction of current).</li><li>Your fingers curl over the top from South to North and loop underneath from North to South.</li><li><strong>At a point directly below:</strong> Field is directed towards the <strong>North</strong> (turns clockwise when viewed from the East end).</li><li><strong>At a point directly above:</strong> Field is directed towards the <strong>South</strong> (anti-clockwise when viewed from the West end).</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "A vertical wire carries current directed straight upward towards the ceiling. When viewed from above, what is the direction of the circular magnetic field lines?",
                "options": [
                    "Clockwise",
                    "Anticlockwise",
                    "Radially outward like spokes on a wheel",
                    "Vertically downward"
                ],
                "ans": 1,
                "solution": "Pointing the right thumb upward towards the ceiling causes the fingers to curl in an anticlockwise direction when viewed from above (NCERT Page 200, Fig 12.7)."
            },
            {
                "q": "In Example 12.1, a horizontal wire carries current from East to West. What is the direction of the magnetic field at a point directly below the wire?",
                "options": [
                    "Towards the East",
                    "Towards the West",
                    "Towards the North",
                    "Towards the South"
                ],
                "ans": 2,
                "solution": "Applying the right-hand thumb rule with the thumb pointing West, the fingers curl under the wire pointing towards the North (NCERT Page 200, Example 12.1)."
            }
        ]
    },
    {
        "id": 8,
        "title": "Magnetic Field of a Circular Current Loop",
        "subtitle": "Chapter 12 • Page 200",
        "tag": "Section 12.2.3 Circular Loop",
        "quote": "Bending a wire into a loop focuses the magnetic field—every wire segment joins forces to create a straight, intense beam at the centre.",
        "lead": "At every point of a circular loop, concentric circles expand until at the very center, the field lines become parallel straight lines.",
        "narration": "What happens if we bend a straight current-carrying wire into a circular loop? Near the wire, the field lines are still concentric circles. But as we move towards the centre of the loop, the circles become larger and larger. At the centre of the loop, the arcs of these large circles appear as straight lines perpendicular to the plane of the loop! Because every section of the loop carries current in a coordinated circle, all segments contribute magnetic field lines in the exact same direction within the loop.",
        "theory_blocks": [
            {
                "title": "Field Geometry of a Circular Loop (Fig 12.8)",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li>Near the wire, field lines form tight <strong>concentric circles</strong> around each wire segment.</li><li>Moving away from the wire into the interior of the loop, the concentric circles expand into wide arcs.</li><li><strong>At the Centre of the Loop:</strong> The arcs flatten out completely and appear as <strong>uniform parallel straight lines perpendicular to the plane of the loop</strong>!</li><li><strong>Additive Contribution:</strong> Applying the right-hand thumb rule to any segment reveals that every segment pushes field lines in the <strong>same direction</strong> through the inside of the loop!</li></ul>"
            },
            {
                "title": "Clock Face Rule for Loop Magnetic Polarity",
                "content": "<p class='mb-2 text-slate-300'>A current-carrying loop behaves like a thin magnetic disc with North and South faces:</p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>South Pole (Clockwise):</strong> If looking at a face of the loop, the current flows in a <strong>clockwise</strong> direction, that face behaves as a <strong>South pole (S)</strong>. Field lines enter the face!</li><li><strong>North Pole (Anticlockwise):</strong> If current flows in an <strong>anticlockwise</strong> direction, that face behaves as a <strong>North pole (N)</strong>. Field lines emerge from the face!</li><li><strong>Intext Q1:</strong> A loop lying on a table carries clockwise current $\\implies$ Field lines point <strong>downward into the table inside the loop</strong>, and point <strong>upward outside the loop</strong>!</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "Consider a circular wire loop lying flat on a table with current flowing clockwise. What is the direction of the magnetic field inside the loop?",
                "options": [
                    "Directed vertically upward out of the table",
                    "Directed vertically downward into the table",
                    "Flowing circularly in the clockwise direction",
                    "Zero, because circular loops cancel their own field"
                ],
                "ans": 1,
                "solution": "By the right-hand thumb rule (or clock rule), a clockwise current produces a South magnetic face where field lines point perpendicularly downward into the table inside the loop (NCERT Page 201, Intext Q1)."
            },
            {
                "q": "At the exact centre of a current-carrying circular loop, what shape do the magnetic field lines take?",
                "options": [
                    "Tight concentric ellipses",
                    "Straight lines perpendicular to the plane of the loop",
                    "Spirals collapsing into the wire",
                    "Hyperbolic curves parallel to the loop"
                ],
                "ans": 1,
                "solution": "At the center of a circular loop, the field arcs from opposite sides combine so that the field lines appear as parallel straight lines perpendicular to the plane of the loop (NCERT Page 200, Fig 12.8)."
            }
        ]
    },
    {
        "id": 9,
        "title": "Circular Coil with N Turns: Field Multiplication",
        "subtitle": "Chapter 12 • Page 201",
        "tag": "Activity 12.6 N-Turn Multiplier",
        "quote": "A coil of N turns multiplies magnetic field strength by N—the current in every loop marches in unison to sum the magnetic output.",
        "lead": "Activity 12.6 proves that winding a wire into N identical turns increases magnetic field strength by exactly N times: B ∝ n · I.",
        "narration": "What if instead of a single circular turn, we wind a coil with N turns? The magnetic field produced by a current-carrying wire at any point depends directly on the current. In a circular coil having N turns, the current in each turn flows in the exact same direction. Therefore, the magnetic field produced by each turn simply adds up arithmeticallly! A coil with N turns produces a magnetic field N times as strong as that of a single turn.",
        "theory_blocks": [
            {
                "title": "The N-Fold Multiplier Law: B ∝ n · I",
                "content": "<p class='mb-2 text-slate-300'>Why does an $N$-turn coil produce an $N$-times stronger field?</p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li>Each turn carries the exact same current $I$ in the same rotational sense.</li><li>Because magnetic fields obey the principle of superposition, the field vector at the center is the algebraic sum of the fields of each individual turn:</li></ul><p class='text-cyan-400 font-mono font-bold text-xs sm:text-sm my-2'>$$B_{\\text{total}} = B_1 + B_2 + \\dots + B_n = n \\times B_{\\text{single turn}}$$</p><ul class='list-disc pl-5 space-y-1 text-slate-300'><li>A coil of 100 turns generates a magnetic field <strong>100 times stronger</strong> than a single loop carrying the same current!</li><li>This linear multiplication is the foundation of powerful electromagnets, electric motors, and transformers.</li></ul>"
            },
            {
                "title": "Activity 12.6: Multi-Turn Circular Coil on Cardboard",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li>In Activity 12.6, a circular coil with a large number of turns is inserted through two holes in a cardboard sheet (Fig 12.9).</li><li>Sprinkling iron filings and connecting to a battery and rheostat reveals dense magnetic field lines entering one hole and emerging from the other.</li><li>Near the center between the two holes, the field lines are closely spaced and nearly parallel, demonstrating strong and uniform magnetic flux.</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "If a single-turn circular loop produces a magnetic field B at its center, what field will be produced by a coil of 50 identical turns carrying the same current?",
                "options": [
                    "B / 50",
                    "B",
                    "50 B",
                    "2500 B"
                ],
                "ans": 2,
                "solution": "In an n-turn coil, the current in each turn flows in the same direction and their magnetic fields add up directly, producing a field n times as large: 50 B (NCERT Page 201)."
            },
            {
                "q": "Why do the magnetic fields of multiple turns in a compact coil add together rather than cancelling out?",
                "options": [
                    "Because alternate turns carry alternating current",
                    "Because current in every turn flows in the exact same rotational direction",
                    "Because insulation between the wires creates electrostatic attraction",
                    "Because copper turns repel earth's magnetic field"
                ],
                "ans": 1,
                "solution": "Current in each circular turn flows in the same direction; hence, the magnetic field vectors produced by every turn point in identical directions and add together (NCERT Page 201)."
            }
        ]
    },
    {
        "id": 10,
        "title": "The Solenoid & Electromagnet Architecture",
        "subtitle": "Chapter 12 • Pages 201–202",
        "tag": "Section 12.2.4 Solenoid & Magnet",
        "quote": "A solenoid mimics a bar magnet with uncanny precision—creating a completely uniform magnetic field inside its cylindrical core.",
        "lead": "A long cylindrical coil of insulated wire forms a solenoid whose internal field lines are uniform parallel straight lines.",
        "narration": "What is a solenoid? A coil of many circular turns of insulated copper wire wrapped closely in the shape of a cylinder is called a solenoid. Remarkably, the magnetic field lines around a current-carrying solenoid look almost identical to those around a bar magnet! One end acts as a magnetic north pole, and the other end acts as a south pole. Inside the solenoid, the field lines are parallel straight lines, proving that the magnetic field is completely uniform. Placing a soft iron core inside produces an electromagnet.",
        "theory_blocks": [
            {
                "title": "Solenoid Definition & Field Pattern (Fig 12.10)",
                "content": "<p class='mb-2 text-slate-300'><strong>Definition:</strong> A coil of many circular turns of insulated copper wire wrapped closely in the shape of a cylinder is called a <strong>solenoid</strong>.</p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Bar Magnet Analogy:</strong> The magnetic field pattern outside a solenoid is <strong>identical to that of a bar magnet</strong> (Fig 12.10)! One end behaves as a North pole, the other as a South pole.</li><li><strong>Uniform Internal Field:</strong> The field lines <strong>inside the solenoid are parallel straight lines</strong>. This indicates that the magnetic field is the <strong>same at all points inside</strong> the solenoid (completely uniform!).</li><li><strong>Intext Q3:</strong> The magnetic field inside a long straight current-carrying solenoid is <strong>the same at all points</strong>!</li></ul>"
            },
            {
                "title": "Electromagnet Construction (Fig 12.11)",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>How an Electromagnet is Made:</strong> A strong magnetic field produced inside a solenoid is used to magnetise a piece of magnetic material, like a <strong>soft iron core</strong>, placed inside the coil.</li><li><strong>Why Soft Iron?</strong> Soft iron has high magnetic permeability and low retentivity: it magnetises strongly when current is ON, and demagnetises almost completely when current is switched OFF.</li><li><strong>Advantages of Electromagnets:</strong><br>• Magnetism can be switched ON and OFF instantly.<br>• Magnetic strength can be varied by adjusting current ($I$) or number of turns ($n$).<br>• Polarity can be reversed by reversing current direction.</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "How does the magnetic field behave inside a long straight current-carrying solenoid?",
                "options": [
                    "It is zero everywhere",
                    "It decreases steadily towards the ends",
                    "It increases towards the ends",
                    "It is uniform and the same at all points"
                ],
                "ans": 3,
                "solution": "The field lines inside a solenoid are parallel straight lines, indicating that the magnetic field is uniform and identical at all points inside (NCERT Page 201 & Page 202, Question 3)."
            },
            {
                "q": "Why is soft iron preferred over steel for making the temporary core of an electromagnet?",
                "options": [
                    "Soft iron becomes a permanent magnet that cannot be demagnetized",
                    "Soft iron magnetises strongly when current is ON and loses its magnetism readily when current is OFF",
                    "Soft iron has zero electrical resistance at room temperature",
                    "Soft iron prevents the copper wire from heating up"
                ],
                "ans": 1,
                "solution": "Soft iron easily gains magnetism when current passes through the solenoid and loses it immediately when current stops, making it ideal for temporary electromagnets (NCERT Page 201)."
            }
        ]
    },
    {
        "id": 11,
        "title": "Magnetic Force on a Conductor: Ampère’s Reciprocal Law",
        "subtitle": "Chapter 12 • Pages 202–203",
        "tag": "Section 12.3 Force on Conductor",
        "quote": "If a current-carrying wire exerts a force on a magnet, Newton's third law demands the magnet exert an equal and opposite force on the wire.",
        "lead": "Activity 12.7 demonstrates that a current-carrying aluminium rod placed in a magnetic field experiences a mechanical kick.",
        "narration": "In Section 12.3, French scientist André-Marie Ampère suggested that if an electric current exerts a force on a magnet, the magnet must exert an equal and opposite force on the current-carrying conductor. In Activity 12.7, an aluminium rod suspended between the poles of a strong horseshoe magnet experiences a strong mechanical displacement! Reversing the current reverses the direction of the force, and flipping the magnetic poles also reverses the force.",
        "theory_blocks": [
            {
                "title": "Activity 12.7: The Kicking Aluminium Rod (Fig 12.12)",
                "content": "<p class='mb-2 text-slate-300'>Experimental setup with suspended aluminium rod $AB$:</p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li>A $5\\text{ cm}$ aluminium rod $AB$ is suspended horizontally between the poles of a strong horseshoe magnet (North pole below, South pole above $\\implies$ magnetic field directed vertically upward).</li><li>When current flows from $B$ to $A$, the rod is <strong>displaced towards the left</strong>!</li><li><strong>Reversing Current ($A$ to $B$):</strong> The displacement flips <strong>towards the right</strong>!</li><li><strong>Reversing Magnetic Field (Poles swapped):</strong> The displacement also reverses!</li><li><strong>Conclusion:</strong> A mechanical force acts on a current-carrying conductor in a magnetic field, perpendicular to both current and magnetic field!</li></ul>"
            },
            {
                "title": "Factors Governing the Magnetic Force (F = B I l sin θ)",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li>The displacement of the rod (magnitude of force) increases when:<br>1. <strong>Current ($I$) is increased</strong> in the rod.<br>2. A <strong>stronger magnet (higher $B$)</strong> is used.<br>3. <strong>Length ($l$)</strong> of the conductor inside the field is increased.</li><li><strong>Angular Condition:</strong> The force is <strong>maximum when current is at right angles ($90^\\circ$)</strong> to the magnetic field lines.</li><li>If the conductor is parallel to the magnetic field ($0^\\circ$ or $180^\\circ$), the force is <strong>zero</strong>!</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "When is the mechanical force experienced by a current-carrying conductor in a magnetic field largest?",
                "options": [
                    "When the conductor is parallel to the magnetic field lines (0°)",
                    "When the conductor is perpendicular to the magnetic field lines (90°)",
                    "When the conductor is inclined at exactly 45°",
                    "When the electric current is switched off"
                ],
                "ans": 1,
                "solution": "The force on a current-carrying conductor is highest when the direction of current is at right angles (90°) to the direction of the magnetic field (NCERT Page 203 & Page 207, Exercise Q5)."
            },
            {
                "q": "In Activity 12.7, what will happen to the displacement of rod AB if a stronger horseshoe magnet is used?",
                "options": [
                    "The displacement decreases to zero",
                    "The displacement increases",
                    "The displacement reverses direction without changing magnitude",
                    "The rod begins to rotate continuously in a circle"
                ],
                "ans": 1,
                "solution": "Magnetic force is directly proportional to magnetic field strength (F ∝ B). Using a stronger magnet increases the force, thereby increasing the rod's displacement (NCERT Page 204, Intext Q2)."
            }
        ]
    },
    {
        "id": 12,
        "title": "Fleming’s Left-Hand Rule & Particle Deflections",
        "subtitle": "Chapter 12 • Pages 203–204",
        "tag": "Section 12.3 Fleming's Rule",
        "quote": "Stretch your thumb, forefinger, and middle finger at right angles: Forefinger is Field, Middle finger is Current, Thumb is Force.",
        "lead": "Fleming's Left-Hand Rule predicts the mechanical thrust on conductors, motors, and drifting charged particles.",
        "narration": "To find the direction of force on a current-carrying conductor or charged particle, we use Fleming's Left-Hand Rule. Stretch the thumb, forefinger, and middle finger of your left hand mutually perpendicular to each other. If the Forefinger points in the direction of the magnetic Field, and the Middle finger in the direction of Current, then the Thumb points in the direction of Motion or Force! Remember: for negative electrons, current is opposite to electron motion.",
        "theory_blocks": [
            {
                "title": "Fleming's Left-Hand Rule (Fig 12.13)",
                "content": "<p class='mb-2 text-slate-300'>Stretch thumb, forefinger, and middle finger of the left hand mutually perpendicular:</p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>First finger (Forefinger):</strong> Points in direction of <strong>Magnetic Field</strong> ($B$).</li><li><strong>Second finger (Middle finger):</strong> Points in direction of <strong>Current</strong> ($I$).</li><li><strong>Thumb:</strong> Points in direction of <strong>Motion / Force</strong> ($F$) acting on conductor!</li><li><strong>Mnemonic:</strong> <strong>F-B-I</strong> (Thumb = Force, Forefinger = B-Field, Middle = I-Current) or <strong>Father-Mother-Child</strong> (Force, Magnetic field, Current).</li><li><strong>Practical Applications:</strong> Electric motors, loudspeakers, microphones, and galvanometers.</li></ul>"
            },
            {
                "title": "Charged Particles: Examples 12.2 & Intext Q3",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300 text-xs sm:text-sm'><li><strong>Example 12.2 (Electron Entering Magnetic Field Fig 12.14):</strong><br>Electron moves downward; hence conventional current points <strong>upward</strong>! Magnetic field is to the <strong>right</strong>. Applying Fleming's Left-Hand Rule gives force directed <strong>into the page</strong> (Option d)!</li><li><strong>Intext Q1 (Proton in Magnetic Field):</strong> A proton's <strong>velocity and momentum</strong> change because magnetic force curves its trajectory, altering direction even though speed remains constant!</li><li><strong>Intext Q3 (Alpha Particle Projected West Deflected North):</strong><br>Positive particle moves West $\\implies$ Current is West. Force is North. By Fleming's left hand rule, magnetic field must be directed <strong>upward</strong> (Option d)!</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "An electron enters a magnetic field pointing to the right, with the electron moving towards the bottom of the page. What is the direction of force on the electron?",
                "options": [
                    "To the right",
                    "To the left",
                    "Out of the page",
                    "Into the page"
                ],
                "ans": 3,
                "solution": "Current direction is opposite to electron motion (upward). Field is to the right. By Fleming's left-hand rule, thumb points into the page (NCERT Page 203, Example 12.2)."
            },
            {
                "q": "A positively charged alpha particle projected towards the West is deflected towards the North by a magnetic field. What is the direction of the magnetic field?",
                "options": [
                    "Towards the South",
                    "Towards the East",
                    "Downward towards the ground",
                    "Upward towards the sky"
                ],
                "ans": 3,
                "solution": "Current is West (same as positive alpha motion), force is North. Pointing middle finger West and thumb North makes forefinger point upward (NCERT Page 204, Intext Q3)."
            }
        ]
    },
    {
        "id": 13,
        "title": "Magnetism in Medicine & Human Bio-Magnetic Fields",
        "subtitle": "Chapter 12 • Page 204",
        "tag": "More to Know: MRI & Medicine",
        "quote": "Nerve impulses generate faint magnetic whispers in our brain and heart—unlocking non-invasive Magnetic Resonance Imaging.",
        "lead": "Weak ionic currents travelling along nerve cells generate minute bio-magnetic fields that enable MRI medical diagnosis.",
        "narration": "Did you know that human biology generates magnetism? In the 'More to Know' box on Page 204, we learn that whenever nerve cells transmit electrical impulses to muscles, weak ionic currents flow. These ionic currents produce extremely faint magnetic fields—about one-billionth the strength of the Earth's magnetic field! The two main organs where these fields are most significant are the heart and the brain. This bio-magnetism forms the basis of Magnetic Resonance Imaging, or MRI, creating detailed diagnostic cross-sections of human organs.",
        "theory_blocks": [
            {
                "title": "Bio-Magnetic Origin: Ionic Nerve Currents",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li>An electric current always produces a magnetic field—even in biological tissues!</li><li>When we touch an object, nerves carry an electrical impulse ($Na^+ / K^+$ ion flow) along axons to muscles and the central nervous system.</li><li>These ionic currents produce transient, microscopic magnetic fields.</li><li><strong>Magnitude:</strong> Bio-magnetic fields are exceptionally weak—approximately <strong>one-billionth ($10^{-9}$) of the Earth's magnetic field</strong>!</li></ul>"
            },
            {
                "title": "The Heart, The Brain & Magnetic Resonance Imaging (MRI)",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Two Main Organs:</strong> The two human organs where bio-magnetic fields are most significant are the <strong>heart</strong> and the <strong>brain</strong>.</li><li><strong>MRI (Magnetic Resonance Imaging):</strong><br>• Uses powerful magnetic fields and radiofrequency pulses to interact with hydrogen nuclei (protons) in body water and fats.<br>• Generates high-resolution cross-sectional slices of soft tissues without harmful ionizing X-ray radiation.<br>• Revolutionized detection of tumors, brain disorders, spinal cord trauma, and cardiovascular disease.</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "Which two organs in the human body produce the most significant bio-magnetic fields?",
                "options": [
                    "The liver and the kidneys",
                    "The heart and the brain",
                    "The lungs and the stomach",
                    "The bones and the skin"
                ],
                "ans": 1,
                "solution": "Two main organs in the human body where the magnetic field produced by nerve impulses is significant are the heart and the brain (NCERT Page 204, More to Know)."
            },
            {
                "q": "What medical diagnostic technique relies on magnetic fields interacting with hydrogen nuclei inside human tissues to produce detailed body images?",
                "options": [
                    "X-ray Radiography",
                    "Ultrasound Sonography",
                    "Magnetic Resonance Imaging (MRI)",
                    "Electrocardiogram (ECG)"
                ],
                "ans": 2,
                "solution": "Magnetic Resonance Imaging (MRI) uses magnetism inside the human body to obtain detailed anatomical images for medical diagnosis (NCERT Page 204)."
            }
        ]
    },
    {
        "id": 14,
        "title": "Domestic Electric Circuits: Live, Neutral & Safety Earthing",
        "subtitle": "Chapter 12 • Pages 204–205",
        "tag": "Section 12.4 Domestic Circuits",
        "quote": "In our homes, 220 V AC arrives via Live and Neutral wires, while the green Earth wire guards against fatal electrical shocks.",
        "lead": "Domestic power is distributed across parallel 15 A and 5 A circuits with color-coded insulation and dedicated safety earthing.",
        "narration": "Let us explore domestic electric circuits. In India, mains electricity is supplied at 220 volts alternating current with a frequency of 50 hertz. The supply enters through three wires: the Live wire with red insulation, the Neutral wire with black insulation, and the Earth wire with green insulation. Two separate parallel circuits are wired in homes: a 15-ampere line for heavy appliances like geysers and air coolers, and a 5-ampere line for lights and fans. The green earth wire provides a safe low-resistance path to ground, preventing electric shocks.",
        "theory_blocks": [
            {
                "title": "Color Codes & Domestic Supply Parameters",
                "content": "<p class='mb-2 text-slate-300'>Standard domestic supply in India (220 V AC, 50 Hz):</p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Live Wire (Positive, L):</strong> <strong>Red insulation</strong>. Carries high potential (220 V relative to ground).</li><li><strong>Neutral Wire (Negative, N):</strong> <strong>Black insulation</strong>. Maintained at zero potential (0 V).</li><li><strong>Potential Difference:</strong> $V = 220\\text{ V} - 0\\text{ V} = \\mathbf{220\\text{ V}}$ AC at $50\\text{ Hz}$.</li><li><strong>Two Domestic Circuits:</strong><br>• <strong>15 A Rating:</strong> For heavy appliances with high power consumption (geysers, air coolers, room heaters).<br>• <strong>5 A Rating:</strong> For lower-power appliances (bulbs, fans, televisions, chargers).</li></ul>"
            },
            {
                "title": "The Safety Earth Wire (Green Insulation)",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Earth Wire (E):</strong> Has <strong>green insulation</strong> and is connected to a thick copper plate buried deep in moist earth near the building.</li><li><strong>Connection:</strong> Firmly bonded to the <strong>metallic outer body</strong> of appliances (electric press, toaster, refrigerator).</li><li><strong>How Earthing Prevents Fatal Shock:</strong> If a damaged live wire touches the metal casing, current immediately rushes through the low-resistance earth wire into the ground rather than through a user's body!</li><li>This heavy fault current instantly blows the circuit fuse, isolating the faulty appliance safely!</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "What is the primary function of the green earth wire connected to metallic household appliances?",
                "options": [
                    "To supply extra current during peak hours",
                    "To provide a low-resistance path to ground, preventing severe electric shocks if live wire touches the metal casing",
                    "To cool down the appliance by conducting heat into the soil",
                    "To increase the supply voltage to 440 V"
                ],
                "ans": 1,
                "solution": "The earth wire provides a low-resistance conducting path to ground, ensuring any leakage current keeps the metal casing at zero potential, protecting users from electric shocks (NCERT Page 204 & Page 207, Exercise Q9)."
            },
            {
                "q": "What is the potential difference and frequency of domestic alternating current (AC) power supplied in India?",
                "options": [
                    "110 V at 60 Hz",
                    "220 V at 50 Hz",
                    "440 V at 50 Hz",
                    "220 V direct current (DC)"
                ],
                "ans": 1,
                "solution": "In India, domestic electric power is supplied at 220 V alternating current with a frequency of 50 Hz (NCERT Page 204 & Page 206)."
            }
        ]
    },
    {
        "id": 15,
        "title": "Short-Circuiting, Overloading & The Safety Fuse",
        "subtitle": "Chapter 12 • Page 205",
        "tag": "Section 12.4 Safety Mechanisms",
        "quote": "When live and neutral wires touch, current explodes in a short circuit—stopped only by the sacrificial melting of a safety fuse.",
        "lead": "Domestic circuits are connected in parallel with individual switches, while fuses prevent destructive thermal fires.",
        "narration": "What causes electrical hazards in homes? Overloading occurs when total current exceeds the safe rating of the circuit cables. This happens when too many appliances are connected to a single socket, or during an accidental supply voltage spike. Short-circuiting happens when the live and neutral wires come into direct contact due to faulty or damaged insulation, causing circuit resistance to drop near zero and current to surge enormously. An electric fuse stops this dangerous surge by melting via Joule heating, saving lives and preventing fires.",
        "theory_blocks": [
            {
                "title": "Short-Circuiting vs Overloading Defined",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Short-Circuiting:</strong> Occurs when the <strong>live wire and neutral wire come into direct physical contact</strong> (due to damaged insulation or internal appliance fault).<br>• Resistance drops to near zero $\\implies$ Current surges violently to hundreds of amperes!<br>• Can produce sparks, explosions, and catastrophic building fires.</li><li><strong>Overloading:</strong> Occurs when the total current drawn exceeds the safe carrying capacity of the circuit.<br>• <strong>Causes:</strong> (1) Connecting too many high-power appliances to a single socket, (2) Accidental spike in supply mains voltage.</li></ul>"
            },
            {
                "title": "The Safety Fuse & Domestic 2 kW Oven Problem",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300 text-xs sm:text-sm'><li><strong>Working Principle of Fuse:</strong> The fuse wire has a low melting point. An excessive current produces intense Joule heating ($H = I^2Rt$), melting the wire and cleanly breaking the circuit.</li><li><strong>Intext Q2: 2 kW Electric Oven on a 5 A Line (220 V):</strong><br>Power $P = 2\\text{ kW} = 2000\\text{ W}, V = 220\\text{ V}$.<br>Current drawn: $I = \\frac{P}{V} = \\frac{2000}{220} = \\mathbf{9.09\\text{ A}}$.<br><em>Result:</em> Since $9.09\\text{ A}$ greatly exceeds the $5\\text{ A}$ circuit rating, the <strong>fuse wire will immediately heat up, melt, and break the circuit</strong>!</li><li><strong>Precautions:</strong> Never plug multiple heavy appliances into one multi-plug adapter; use appropriately rated fuses and MCBs.</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "At the moment of a short circuit, what happens to the electric current flowing through the circuit?",
                "options": [
                    "It reduces substantially to zero",
                    "It does not change at all",
                    "It increases heavily",
                    "It fluctuates between positive and negative infinity"
                ],
                "ans": 2,
                "solution": "During a short circuit, the live and neutral wires touch with zero resistance between them, causing the current to increase heavily (NCERT Page 205 & Page 207, Exercise Q2)."
            },
            {
                "q": "An electric oven of 2 kW power rating is operated in a 220 V circuit having a 5 A fuse rating. What will happen?",
                "options": [
                    "The oven operates normally without issues",
                    "Current drawn is 9.09 A; the fuse wire will melt and break the circuit",
                    "The oven voltage drops to 110 V automatically",
                    "The earth wire melts while the fuse stays intact"
                ],
                "ans": 1,
                "solution": "The oven draws I = P/V = 2000/220 ≈ 9.09 A. Since this exceeds the 5 A fuse rating, excessive Joule heating melts the fuse wire and interrupts the circuit (NCERT Page 205, Intext Q2)."
            }
        ]
    },
    {
        "id": 16,
        "title": "Complete NCERT Exercises Solutions (Q1 to Q9)",
        "subtitle": "Chapter 12 • Page 207",
        "tag": "All Exercises Q1 to Q9",
        "quote": "Mastery of magnetic fields, Oersted’s principle, Fleming's rule, and domestic safety completes Chapter 12.",
        "lead": "Official verified solutions and justifications for textbook Exercises 1 through 9.",
        "narration": "To complete our study of Chapter 12, let us review the official NCERT exercises. In Question 1, the magnetic field near a long straight wire consists of concentric circles centered on the wire. In Question 2, current increases heavily during a short circuit. Question 6 uses Fleming's Left-Hand Rule to determine that an electron beam moving from back to front wall and deflected right implies a downward magnetic field. Review each verified answer in this interactive solution hub.",
        "theory_blocks": [
            {
                "title": "Exercises Questions 1 to 5 Solutions",
                "content": "<div class='space-y-2 text-xs text-slate-300'><p><strong>Q1: Magnetic Field Near Long Straight Wire:</strong><br><strong>(d) The field consists of concentric circles centred on the wire</strong> (NCERT Page 199).</p><p><strong>Q2: Current at the Time of Short Circuit:</strong><br><strong>(c) Increases heavily</strong> due to near-zero resistance between live and neutral wires.</p><p><strong>Q3: State True or False:</strong><br>(a) The field at the centre of a long circular coil carrying current will be parallel straight lines: <strong>TRUE</strong>.<br>(b) A wire with a green insulation is usually the live wire of an electric supply: <strong>FALSE</strong> (Green is Earth wire; Live wire is Red).</p><p><strong>Q4: Two Methods of Producing Magnetic Fields:</strong><br>1. Using a permanent magnet (e.g. bar magnet, horseshoe magnet).<br>2. Passing an electric current through a conductor (straight wire, circular loop, or solenoid).</p><p><strong>Q5: When Force on Current-Carrying Conductor is Largest:</strong><br>When the direction of current is <strong>perpendicular ($90^\\circ$)</strong> to the direction of the magnetic field.</p></div>"
            },
            {
                "title": "Exercises Questions 6 to 9 Solutions",
                "content": "<div class='space-y-2 text-xs text-slate-300'><p><strong>Q6: Electron Beam Deflection in Chamber:</strong><br>Electron moves back $\\to$ front $\\implies$ Current flows front $\\to$ back. Deflection (Force) is to the right. Applying Fleming's Left-Hand Rule, the <strong>magnetic field is directed vertically DOWNWARD</strong>.</p><p><strong>Q7: State Rules to Determine Directions:</strong><br>(i) Field around straight wire: <strong>Right-hand thumb rule</strong>.<br>(ii) Force on conductor: <strong>Fleming's left-hand rule</strong>.<br>(iii) Induced current in rotating coil: <strong>Fleming's right-hand rule</strong>.</p><p><strong>Q8: When Does Short Circuit Occur?</strong><br>When the live wire and neutral wire come in direct contact due to worn insulation or appliance fault, causing circuit resistance to drop to zero and current to surge dangerously.</p><p><strong>Q9: Function of Earth Wire:</strong><br>Provides a low-resistance path to ground for any leakage current from metal-bodied appliances, keeping the casing at zero potential and preventing lethal electric shocks.</p></div>"
            }
        ],
        "checkpoints": [
            {
                "q": "An electron beam moving horizontally from the back wall towards the front wall is deflected to your right. What is the direction of the magnetic field?",
                "options": [
                    "Vertically upward",
                    "Vertically downward",
                    "Towards the left wall",
                    "Towards the front wall"
                ],
                "ans": 1,
                "solution": "Current is opposite to electron motion (directed towards back wall). Force is to the right. By Fleming's left hand rule (middle finger toward back, thumb to the right), the forefinger points vertically DOWNWARD (NCERT Page 207, Exercise Q6)."
            },
            {
                "q": "Which rule determines the direction of force experienced by a current-carrying straight conductor placed perpendicularly in a magnetic field?",
                "options": [
                    "Right-hand thumb rule",
                    "Fleming's left-hand rule",
                    "Fleming's right-hand rule",
                    "Ohm's law rule"
                ],
                "ans": 1,
                "solution": "Fleming's left-hand rule is used to determine the direction of force (motion) acting on a current-carrying conductor in a magnetic field (NCERT Page 203 & Page 207, Exercise Q7ii)."
            }
        ]
    }
]

QUIZ_SLIDES = [
    {
        "id": 17,
        "title": "Mastery Challenge: Magnetic Field, Field Lines & Oersted's Discovery",
        "subtitle": "Challenge Quiz 1 of 4 • 10 Board-Level Questions",
        "tag": "Quiz 1: Field & Field Lines",
        "narration": "Welcome to Quiz Challenge 1! Test your foundational understanding of magnetic fields, compass needle behaviors, field line properties, and Oersted's discovery. Click View Solution on any card for full step-by-step teacher explanations.",
        "questions": [
            {
                "id": 1,
                "q": "In 1820, who accidentally discovered the magnetic effect of electric current using a compass needle?",
                "options": ["Michael Faraday", "Hans Christian Oersted", "James Clerk Maxwell", "André-Marie Ampère"],
                "ans": 1,
                "solution": "Hans Christian Oersted discovered in 1820 that an electric current in a metallic wire deflects a nearby compass needle (NCERT Page 195)."
            },
            {
                "id": 2,
                "q": "The North-seeking pole of a compass needle points approximately towards which geographic direction of the Earth?",
                "options": ["Geographic South", "Geographic North", "Geographic East", "Geographic West"],
                "ans": 1,
                "solution": "A compass needle is a small bar magnet whose north-seeking end points towards the Earth's geographic North (NCERT Page 196)."
            },
            {
                "id": 3,
                "q": "Outside a permanent bar magnet, the magnetic field lines emerge from the:",
                "options": ["South pole and merge at North pole", "North pole and merge at South pole", "Center and radiate spherically", "Negative terminal to positive terminal"],
                "ans": 1,
                "solution": "By convention, magnetic field lines emerge from the North pole and merge at the South pole outside the magnet (NCERT Page 197)."
            },
            {
                "id": 4,
                "q": "Inside a bar magnet, what is the direction of magnetic field lines?",
                "options": ["From North pole to South pole", "From South pole to North pole", "They terminate at the center", "They do not exist inside a solid magnet"],
                "ans": 1,
                "solution": "Inside the magnet, field lines run from South pole to North pole, forming continuous closed loops (NCERT Page 197)."
            },
            {
                "id": 5,
                "q": "The relative strength of a magnetic field in any region is indicated by:",
                "options": ["The color of the iron filings", "The degree of closeness (crowding) of the field lines", "The temperature of the bar magnet", "The speed of the plotting compass"],
                "ans": 1,
                "solution": "The field is stronger where field lines are crowded together, such as near the poles (NCERT Page 197)."
            },
            {
                "id": 6,
                "q": "Why can two magnetic field lines never intersect each other?",
                "options": [
                    "Because they would spark and ignite",
                    "Because a compass needle at the intersection would have to point in two directions at once, which is impossible",
                    "Because magnetic lines repel each other electrostatically",
                    "Because iron filings dissolve if lines cross"
                ],
                "ans": 1,
                "solution": "If field lines intersected, the compass needle would have to point in two directions simultaneously at the intersection point, which is physically impossible (NCERT Page 197)."
            },
            {
                "id": 7,
                "q": "Magnetic field is a physical quantity having:",
                "options": ["Only magnitude", "Only direction", "Both magnitude and direction (vector quantity)", "Neither magnitude nor direction"],
                "ans": 2,
                "solution": "Magnetic field is a vector quantity possessing both magnitude and direction (NCERT Page 197)."
            },
            {
                "id": 8,
                "q": "A uniform magnetic field is represented graphically by:",
                "options": [
                    "Concentric expanding circles",
                    "Equidistant, parallel straight lines",
                    "Diverging curved rays",
                    "Closed concentric ellipses"
                ],
                "ans": 1,
                "solution": "A uniform magnetic field is represented by parallel, equidistant straight lines (NCERT Page 201)."
            },
            {
                "id": 9,
                "q": "When iron filings are sprinkled around a bar magnet and tapped, they align along:",
                "options": [
                    "Concentric squares",
                    "Magnetic field lines",
                    "Random chaotic clumps",
                    "Horizontal parallel bars"
                ],
                "ans": 1,
                "solution": "The magnetic force exerted by the magnet aligns the filings into smooth curves representing magnetic field lines (NCERT Page 196)."
            },
            {
                "id": 10,
                "q": "Like magnetic poles _______, while unlike magnetic poles _______ each other.",
                "options": ["Attract; repel", "Repel; attract", "Neutralize; destroy", "Rotate; freeze"],
                "ans": 1,
                "solution": "Like magnetic poles repel each other, while unlike magnetic poles attract each other (NCERT Page 196)."
            }
        ]
    },
    {
        "id": 18,
        "title": "Mastery Challenge: Straight Conductors, Loops & Solenoids",
        "subtitle": "Challenge Quiz 2 of 4 • 10 Board-Level Questions",
        "tag": "Quiz 2: Conductors & Coils",
        "narration": "Quiz Challenge 2 tests your mastery of magnetic fields around straight wires, the Right-Hand Thumb Rule, circular loops, and solenoids. Click View Solution on any card for full mathematical and conceptual solutions.",
        "questions": [
            {
                "id": 11,
                "q": "The magnetic field lines produced around a straight current-carrying metallic conductor are:",
                "options": [
                    "Straight lines parallel to the conductor",
                    "Concentric circles centered on the wire",
                    "Radial rays pointing outwards",
                    "Helical spirals around the wire"
                ],
                "ans": 1,
                "solution": "Around a straight current-carrying wire, magnetic field lines form a series of concentric circles centered on the wire (NCERT Page 199)."
            },
            {
                "id": 12,
                "q": "If the electric current in a long straight wire is increased, what happens to the deflection of a compass needle at a fixed distance?",
                "options": [
                    "The deflection increases",
                    "The deflection decreases",
                    "The deflection remains unchanged",
                    "The needle stops deflecting entirely"
                ],
                "ans": 0,
                "solution": "Magnetic field strength B is directly proportional to current I. Increasing current increases the magnetic field and compass deflection (NCERT Page 199)."
            },
            {
                "id": 13,
                "q": "As distance from a current-carrying straight wire increases, the magnetic field strength:",
                "options": ["Increases linearly", "Decreases inversely with distance", "Remains constant", "Drops to zero instantly"],
                "ans": 1,
                "solution": "Magnetic field B is inversely proportional to distance r (B ∝ 1/r). It decreases as distance increases (NCERT Page 199)."
            },
            {
                "id": 14,
                "q": "Which rule is commonly used to find the direction of magnetic field lines around a straight current-carrying wire?",
                "options": ["Fleming's left-hand rule", "Right-hand thumb rule", "Fleming's right-hand rule", "Lenz's rule"],
                "ans": 1,
                "solution": "The Right-Hand Thumb Rule (or Maxwell's corkscrew rule) gives the direction of circular field lines around a straight wire (NCERT Page 200)."
            },
            {
                "id": 15,
                "q": "A horizontal power line carries current from East to West. What is the direction of the magnetic field at a point directly above it?",
                "options": ["Towards East", "Towards West", "Towards North", "Towards South"],
                "ans": 3,
                "solution": "By the right-hand thumb rule with thumb pointing West, fingers curl over the top pointing towards South (NCERT Page 200, Example 12.1)."
            },
            {
                "id": 16,
                "q": "A circular coil has 100 turns. The magnetic field produced at its center compared to a single-turn coil of the same radius carrying the same current is:",
                "options": ["100 times as large", "One-hundredth as large", "The same", "10,000 times as large"],
                "ans": 0,
                "solution": "Because current in all turns flows in the same direction, field contributions add up directly: B = n × B_single = 100 B (NCERT Page 201)."
            },
            {
                "id": 17,
                "q": "What is the nature of the magnetic field lines inside a current-carrying solenoid?",
                "options": [
                    "Concentric ellipses",
                    "Parallel straight lines indicating a uniform field",
                    "Radial lines diverging from the center",
                    "Chaotic turbulent curves"
                ],
                "ans": 1,
                "solution": "Inside a solenoid, field lines are parallel straight lines, showing that the magnetic field is uniform and identical at all internal points (NCERT Page 201)."
            },
            {
                "id": 18,
                "q": "The magnetic field pattern outside a current-carrying solenoid is remarkably similar to that of a:",
                "options": ["Single electric point charge", "Bar magnet", "Horseshoe electromagnet", "Spherical capacitor"],
                "ans": 1,
                "solution": "The external field pattern of a current-carrying solenoid is identical to that of a permanent bar magnet (NCERT Page 201, Fig 12.10)."
            },
            {
                "id": 19,
                "q": "An electromagnet is constructed by placing which material core inside a current-carrying solenoid?",
                "options": ["A copper rod", "A soft iron core", "A wooden cylinder", "An aluminium bar"],
                "ans": 1,
                "solution": "A soft iron core is placed inside the solenoid because soft iron easily magnetises and demagnetises when current is toggled (NCERT Page 201)."
            },
            {
                "id": 20,
                "q": "If current flows clockwise when viewing a circular loop face-on, that face acts as a:",
                "options": ["North magnetic pole", "South magnetic pole", "Neutral ground", "Electrostatic anode"],
                "ans": 1,
                "solution": "By the clock face rule, clockwise current corresponds to a South magnetic pole (field lines enter), while anticlockwise current corresponds to a North magnetic pole (NCERT Page 200)."
            }
        ]
    },
    {
        "id": 19,
        "title": "Mastery Challenge: Magnetic Force, Fleming's Rule & Medicine",
        "subtitle": "Challenge Quiz 3 of 4 • 10 Board-Level Questions",
        "tag": "Quiz 3: Force & Medicine",
        "narration": "Quiz Challenge 3 focuses on the magnetic force on conductors, Fleming's Left-Hand Rule, charged particle trajectories, and bio-magnetism in medicine. Click View Solution for complete explanations.",
        "questions": [
            {
                "id": 21,
                "q": "Who first suggested that a magnet must exert an equal and opposite force on a current-carrying conductor?",
                "options": ["Hans Christian Oersted", "André-Marie Ampère", "Michael Faraday", "Alessandro Volta"],
                "ans": 1,
                "solution": "French scientist André-Marie Ampère suggested that a magnet must exert an equal and opposite force on a current-carrying conductor (NCERT Page 202)."
            },
            {
                "id": 22,
                "q": "The mechanical force on a current-carrying conductor in a magnetic field is zero when the angle between current and field is:",
                "options": ["90°", "45°", "0° (parallel)", "60°"],
                "ans": 2,
                "solution": "When a conductor is placed parallel (0° or 180°) to the magnetic field, it experiences zero magnetic force (NCERT Page 203)."
            },
            {
                "id": 23,
                "q": "In Fleming's Left-Hand Rule, what does the Forefinger (first finger) represent?",
                "options": ["Motion or Force", "Direction of Magnetic Field", "Direction of Current", "Electrostatic Potential"],
                "ans": 1,
                "solution": "In Fleming's Left-Hand Rule, the forefinger points in the direction of the Magnetic Field (NCERT Page 203, Fig 12.13)."
            },
            {
                "id": 24,
                "q": "In Fleming's Left-Hand Rule, what does the Thumb represent?",
                "options": ["Direction of Motion or Force", "Direction of Magnetic Field", "Direction of Electric Current", "Resistance"],
                "ans": 0,
                "solution": "The thumb points in the direction of motion or force acting on the conductor (NCERT Page 203)."
            },
            {
                "id": 25,
                "q": "Which of the following devices relies on the force exerted on a current-carrying conductor in a magnetic field?",
                "options": ["Electric motor", "Loudspeakers", "Microphones and measuring meters", "All of the above"],
                "ans": 3,
                "solution": "Electric motors, loudspeakers, microphones, and measuring galvanometers all operate based on magnetic force on current-carrying conductors (NCERT Page 203)."
            },
            {
                "id": 26,
                "q": "Which property of a proton changes as it moves freely through a transverse magnetic field?",
                "options": ["Mass only", "Speed only", "Velocity and momentum", "Electric charge"],
                "ans": 2,
                "solution": "Magnetic force is perpendicular to motion, altering direction without changing speed. Since direction changes, both velocity and momentum change (NCERT Page 203, Intext Q1)."
            },
            {
                "id": 27,
                "q": "A positively charged alpha particle projected towards West is deflected North by a magnetic field. The magnetic field points:",
                "options": ["Towards South", "Towards East", "Downward", "Upward"],
                "ans": 3,
                "solution": "Current is West, Force is North. By Fleming's Left-Hand Rule, the magnetic field points upward (NCERT Page 204, Intext Q3)."
            },
            {
                "id": 28,
                "q": "Bio-magnetic fields produced by human nerve cells are approximately what fraction of the Earth's magnetic field?",
                "options": ["One-tenth", "One-thousandth", "One-millionth", "One-billionth (10⁻⁹)"],
                "ans": 3,
                "solution": "Human bio-magnetic fields are extremely weak, approximately one-billionth of the Earth's magnetic field (NCERT Page 204, More to Know)."
            },
            {
                "id": 29,
                "q": "What diagnostic imaging technique utilizes the magnetic fields produced inside the human body for medical diagnosis?",
                "options": ["Electrocardiogram (ECG)", "Magnetic Resonance Imaging (MRI)", "Positron Emission Tomography", "Computed Tomography (CT)"],
                "ans": 1,
                "solution": "Magnetic Resonance Imaging (MRI) maps bio-magnetic signals and proton resonance in human tissues for medical diagnosis (NCERT Page 204)."
            },
            {
                "id": 30,
                "q": "In which two organs of the human body is the magnetic field produced by nerve impulses most significant?",
                "options": ["Heart and Brain", "Lungs and Stomach", "Liver and Kidneys", "Skin and Bones"],
                "ans": 0,
                "solution": "The heart and the brain are the two primary human organs where bio-magnetic fields are most significant (NCERT Page 204)."
            }
        ]
    },
    {
        "id": 20,
        "title": "Mastery Challenge: Domestic Circuits, Safety Earthing & Fuses",
        "subtitle": "Challenge Quiz 4 of 4 • 10 Board-Level Questions",
        "tag": "Quiz 4: Domestic Circuits & Safety",
        "narration": "Welcome to the final Mastery Challenge Quiz! Test your knowledge on domestic wiring, color codes, safety earthing, short circuits, overloading, and safety fuses. Click View Solution on any card for full step-by-step teacher explanations.",
        "questions": [
            {
                "id": 31,
                "q": "In Indian domestic electric supply, what is the color of the insulation on the Live wire and Neutral wire respectively?",
                "options": [
                    "Green and Black",
                    "Red and Black",
                    "Red and Green",
                    "Black and White"
                ],
                "ans": 1,
                "solution": "In Indian domestic circuits, the Live wire has red insulation and the Neutral wire has black insulation (NCERT Page 204)."
            },
            {
                "id": 32,
                "q": "What color insulation is used for the safety Earth wire in domestic wiring?",
                "options": ["Red", "Black", "Green", "Blue"],
                "ans": 2,
                "solution": "The Earth wire has green insulation and connects appliance metallic casings to ground (NCERT Page 204)."
            },
            {
                "id": 33,
                "q": "What is the potential difference between the Live wire and Neutral wire in domestic supply in India?",
                "options": ["110 V", "220 V", "440 V", "12 V"],
                "ans": 1,
                "solution": "The potential difference between live wire (220 V) and neutral wire (0 V) in India is 220 V (NCERT Page 204)."
            },
            {
                "id": 34,
                "q": "What are the two common current ratings of domestic circuits used in households?",
                "options": ["1 A and 2 A", "5 A and 15 A", "10 A and 50 A", "15 A and 30 A"],
                "ans": 1,
                "solution": "Two separate circuits are used: 5 A rating for lights/fans, and 15 A rating for high-power appliances like geysers and coolers (NCERT Page 204)."
            },
            {
                "id": 35,
                "q": "Why are domestic electrical appliances connected in parallel rather than in series?",
                "options": [
                    "To ensure every appliance gets the full 220 V and can be operated independently",
                    "To increase the overall circuit resistance and reduce current",
                    "Because alternating current cannot flow through series circuits",
                    "To make all appliances turn off when any one is switched off"
                ],
                "ans": 0,
                "solution": "Parallel wiring ensures each appliance receives full line voltage (220 V) and has an independent switch, so one failure does not affect others (NCERT Page 205)."
            },
            {
                "id": 36,
                "q": "When does an electrical short-circuit occur in a domestic circuit?",
                "options": [
                    "When the earth wire is disconnected from the ground",
                    "When the live wire and neutral wire come in direct contact",
                    "When a low-wattage bulb is switched off",
                    "When the supply frequency drops below 50 Hz"
                ],
                "ans": 1,
                "solution": "Short-circuiting occurs when the live wire and neutral wire come into direct contact due to faulty insulation, causing current to surge dangerously (NCERT Page 205)."
            },
            {
                "id": 37,
                "q": "At the time of a short-circuit, the electric current in the circuit:",
                "options": ["Reduces substantially", "Does not change", "Increases heavily", "Fluctuates randomly"],
                "ans": 2,
                "solution": "At the time of short-circuit, circuit resistance drops near zero and current increases heavily (NCERT Page 205 & Page 207, Exercise Q2)."
            },
            {
                "id": 38,
                "q": "What causes overloading in a domestic electric circuit?",
                "options": [
                    "Connecting too many appliances to a single socket",
                    "An accidental hike in the supply voltage",
                    "Direct contact of live and neutral wires",
                    "All of the above"
                ],
                "ans": 3,
                "solution": "Overloading can occur from connecting too many appliances to one socket, accidental supply voltage spikes, or short-circuits (NCERT Page 205)."
            },
            {
                "id": 39,
                "q": "An electric oven of 2 kW is connected to a 220 V, 5 A domestic circuit line. What will be the outcome?",
                "options": [
                    "The oven will draw 9.09 A, causing the 5 A fuse to melt and break the circuit",
                    "The oven will function safely without issues",
                    "The oven will consume only 500 W",
                    "The voltage will double to 440 V"
                ],
                "ans": 0,
                "solution": "I = P/V = 2000/220 = 9.09 A. Since this exceeds the 5 A rating, the fuse wire will melt and break the circuit (NCERT Page 205, Intext Q2)."
            },
            {
                "id": 40,
                "q": "Which safety device protects domestic circuits from damage caused by overloading and short-circuiting?",
                "options": ["Voltmeter", "Electric fuse (or MCB)", "Ammeter", "Rheostat"],
                "ans": 1,
                "solution": "An electric fuse (or miniature circuit breaker) melts or trips on excessive current, protecting circuits and preventing fires (NCERT Page 205 & 206)."
            }
        ]
    }
]

