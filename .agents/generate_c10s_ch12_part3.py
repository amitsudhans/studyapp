# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 12: Part 3 (Slides 17 to 20)
Review Quiz Slides (40 Comprehensive Challenge Questions)
"""

import json

slides_part3 = [
    {
        "id": 17,
        "title": "Field Properties Review",
        "subtitle": "Mastery Review 1: Oersted Experiment, Field Line Curves & Vector Laws",
        "speech": "",
        "questions": [
            {
                "question": "A compass needle placed near a straight wire carrying steady direct current deflects. What fundamental physical principle does this demonstration prove?",
                "options": [
                    "Electric current in a conductor produces an active magnetic field in surrounding space",
                    "The wire gains net electrostatic charge that exerts Coulomb force on the needle",
                    "The compass needle transfers its permanent magnetism into the flowing electrons",
                    "Atmospheric air molecules are ionized into permanent magnetic dipoles around the wire"
                ],
                "answer": 0,
                "hint": "Recall Hans Christian Oersted's seminal 1820 experiment.",
                "explanation": "Oersted proved that an electric current (moving electric charge) produces a magnetic field in the surrounding medium, which exerts a magnetic torque on a magnetic compass needle.",
                "solution": [
                    "Step 1: In 1820, Hans Christian Oersted observed that an electric current passing through a conductor deflected an adjacent compass needle.",
                    "Step 2: A compass needle is a magnetic dipole that only experiences mechanical torque from an external magnetic field.",
                    "Step 3: Hence, the deflection conclusively proves that moving electric charges (current) generate a magnetic field."
                ]
            },
            {
                "question": "Outside a permanent bar magnet, what is the standardized convention for the direction of magnetic field lines?",
                "options": [
                    "From the North-seeking pole to the South-seeking pole",
                    "From the South-seeking pole to the North-seeking pole",
                    "Radially outward from both poles toward infinity",
                    "Circularly clockwise around the magnetic equator"
                ],
                "answer": 0,
                "hint": "Consider the path taken by an imaginary isolated North magnetic pole.",
                "explanation": "By scientific convention, external magnetic field lines emerge from the North pole and curve through space to enter the South pole.",
                "solution": [
                    "Step 1: Magnetic field line direction is defined by the direction in which a free north-seeking pole would move.",
                    "Step 2: A north pole is repelled by the magnet's North pole and attracted to the South pole.",
                    "Step 3: Therefore, outside the magnet, field lines emerge from North and enter South."
                ]
            },
            {
                "question": "Inside the body of a permanent bar magnet, in which direction do magnetic field lines travel?",
                "options": [
                    "From the South pole to the North pole, forming continuous closed curves",
                    "From the North pole to the South pole, terminating at the center",
                    "Field lines do not exist inside ferromagnetic materials",
                    "In random turbulent eddies with zero net orientation"
                ],
                "answer": 0,
                "hint": "Magnetic field lines never begin or end abruptly; they form complete loops.",
                "explanation": "Inside a magnet, field lines travel from the South pole back to the North pole, completing continuous, unbroken closed loops.",
                "solution": [
                    "Step 1: Unlike electrostatic field lines which start on positive charges and end on negative charges, magnetic monopoles do not exist.",
                    "Step 2: Magnetic field lines must form continuous closed loops without start or end points.",
                    "Step 3: Since external lines go North to South, internal lines must continue from South to North."
                ]
            },
            {
                "question": "Why can two magnetic field lines never cross or intersect each other in physical space?",
                "options": [
                    "At the intersection point, a compass needle cannot simultaneously indicate two different directions",
                    "Intersecting lines would create infinite electrostatic repulsion between field vectors",
                    "Magnetic lines carry identical electric charges that repel each other to infinite distance",
                    "The magnetic permeability of air drops to zero wherever two fields overlap"
                ],
                "answer": 0,
                "hint": "Think about what direction a compass needle would point if placed at the intersection point.",
                "explanation": "If two field lines crossed, a compass needle placed at that point would have to point in two different directions at the same instant, which is physically impossible.",
                "solution": [
                    "Step 1: The tangent to a magnetic field line at any point specifies the unique direction of the magnetic field vector.",
                    "Step 2: If two lines intersected, there would be two distinct tangents and two distinct field directions at that single coordinate.",
                    "Step 3: A compass needle cannot point in two directions simultaneously; hence, field lines can never cross."
                ]
            },
            {
                "question": "How is the magnitude or relative strength of a magnetic field depicted in a field line diagram?",
                "options": [
                    "By the degree of crowding or closeness of the magnetic field lines",
                    "By the thickness and darkness of the line strokes drawn on paper",
                    "By the length of the arrows marked along each continuous curve",
                    "By the total geographic area covered by the outer field perimeter"
                ],
                "answer": 0,
                "hint": "Regions where lines are densely packed correspond to stronger magnetic forces.",
                "explanation": "Magnetic field strength is directly indicated by the spatial density of field lines: crowded lines denote a strong field, while sparse lines represent a weak field.",
                "solution": [
                    "Step 1: Magnetic flux density (B) represents the number of magnetic field lines passing per unit normal area.",
                    "Step 2: In regions where lines are close together (such as near the poles), flux density B is large.",
                    "Step 3: Thus, relative closeness and crowding of field lines visually represents field strength."
                ]
            },
            {
                "question": "When iron filings are sprinkled on a cardboard around a bar magnet and tapped, why do they form distinct curved lines?",
                "options": [
                    "Each filing becomes an induced magnetic dipole and aligns tangentially along lines of force",
                    "The cardboard vibrates and mechanically channels filings into pre-existing surface grooves",
                    "Static electrical friction between the cardboard and iron creates electrostatic tracks",
                    "Gravity acts in curved parabolic vectors across the cardboard surface"
                ],
                "answer": 0,
                "hint": "Iron is a ferromagnetic substance that magnetizes by induction in an external field.",
                "explanation": "In the magnetic field, each tiny iron filing is magnetized by induction into a dipole and experiences torque, aligning parallel to the local magnetic field line.",
                "solution": [
                    "Step 1: Iron is a ferromagnetic material that becomes temporarily magnetized in the presence of an external field.",
                    "Step 2: Each filing develops induced North and South poles and experiences a magnetic torque.",
                    "Step 3: Tapping overcomes friction, allowing the filings to align end-to-end along the local field lines."
                ]
            },
            {
                "question": "Which of the following statements regarding magnetic field lines is scientifically FALSE?",
                "options": [
                    "Magnetic field lines can originate from isolated magnetic North monopoles",
                    "Magnetic field lines form continuous closed curves traversing inside the magnet",
                    "The tangent at any point on a field line points in the direction of the magnetic field",
                    "Magnetic field lines are crowded near the poles where the magnetic field is strongest"
                ],
                "answer": 0,
                "hint": "Can isolated single magnetic poles exist in nature?",
                "explanation": "Isolated magnetic monopoles do not exist in nature; magnets always exist as dipoles, so field lines never originate from isolated monopoles.",
                "solution": [
                    "Step 1: Gauss's law for magnetism states that isolated magnetic monopoles do not exist.",
                    "Step 2: Every magnet possesses both North and South poles, regardless of how small it is divided.",
                    "Step 3: Therefore, the claim that lines originate from isolated monopoles is completely false."
                ]
            },
            {
                "question": "What is the historical CGS unit of magnetic field strength named in honor of Oersted's discovery?",
                "options": [
                    "Oersted",
                    "Tesla",
                    "Gauss",
                    "Weber"
                ],
                "answer": 0,
                "hint": "Check the textbook biographical sidebar on Hans Christian Oersted.",
                "explanation": "In honor of Hans Christian Oersted's 1820 discovery linking electricity and magnetism, the CGS unit of magnetic field strength was named the oersted.",
                "solution": [
                    "Step 1: Hans Christian Oersted discovered electromagnetic deflection in 1820.",
                    "Step 2: In the CGS electromagnetic system, magnetic field strength H is quantified in oersteds.",
                    "Step 3: (In the modern SI system, magnetic flux density is measured in tesla)."
                ]
            },
            {
                "question": "A freely suspended horizontal compass needle points approximately along which planetary axis?",
                "options": [
                    "Along the geographic North-South direction of Earth",
                    "Along the geographic East-West equator of Earth",
                    "Toward the Sun's instantaneous astronomical position",
                    "Perpendicularly upward toward the local zenith"
                ],
                "answer": 0,
                "hint": "Earth itself acts as an enormous permanent magnet.",
                "explanation": "Because planet Earth acts as a giant magnet with magnetic poles near geographic poles, a freely suspended magnetic needle aligns along Earth's North-South magnetic meridian.",
                "solution": [
                    "Step 1: Earth behaves like an enormous bar magnet with a magnetic South pole located near geographic North.",
                    "Step 2: The north-seeking pole of a compass is attracted toward Earth's magnetic South pole (near geographic North).",
                    "Step 3: Thus, the compass needle naturally aligns along the North-South axis."
                ]
            },
            {
                "question": "If a bar magnet is cut transversally into two equal halves, what is the resulting magnetic outcome?",
                "options": [
                    "Two complete, independent bar magnets are formed, each having its own North and South poles",
                    "One half becomes an isolated North pole while the other becomes an isolated South pole",
                    "Both halves lose their magnetism completely and become unmagnetized iron",
                    "One half remains magnetized while the second half reverses polarity spontaneously"
                ],
                "answer": 0,
                "hint": "Every newly exposed face creates an opposing pole; monopoles cannot be created.",
                "explanation": "Breaking a magnet produces two smaller magnets, each possessing a complete North and South pole pair because atomic magnetic dipoles remain aligned.",
                "solution": [
                    "Step 1: Magnetism arises from aligned microscopic atomic electron spin dipoles throughout the material.",
                    "Step 2: Cutting the magnet exposes new boundary faces where internal dipoles terminate.",
                    "Step 3: Each broken piece retains complete dipolar alignment, resulting in two fully functional magnets."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Conductor Solenoid Review",
        "subtitle": "Mastery Review 2: Straight Wires, Circular Loops & Solenoids",
        "speech": "",
        "questions": [
            {
                "question": "What geometric shape do magnetic field lines form around a long, straight current-carrying vertical wire?",
                "options": [
                    "Concentric circles lying in horizontal planes centered on the wire axis",
                    "Straight lines radiating perpendicularly outward from the conductor surface",
                    "Parallel vertical lines running along the direction of current flow",
                    "Helical spirals expanding upwards into the upper atmosphere"
                ],
                "answer": 0,
                "hint": "Recall Activity 12.5 where iron filings form circular rings around the copper wire.",
                "explanation": "The magnetic field lines around a straight current-carrying wire form concentric circles centered on the wire in planes perpendicular to the wire axis.",
                "solution": [
                    "Step 1: In Activity 12.5, passing current through a vertical wire creates a concentric ring pattern in iron filings.",
                    "Step 2: The field vectors are tangential to circles centered on the wire axis.",
                    "Step 3: Hence, the field lines form concentric circles in planes perpendicular to the wire."
                ]
            },
            {
                "question": "According to the Right-Hand Thumb Rule, what do the thumb and curled fingers represent?",
                "options": [
                    "Thumb = Direction of conventional current; Curled fingers = Direction of magnetic field lines",
                    "Thumb = Direction of magnetic field; Curled fingers = Direction of conventional current",
                    "Thumb = Direction of mechanical force; Curled fingers = Direction of electron velocity",
                    "Thumb = Geographic North pole; Curled fingers = Gravitational acceleration"
                ],
                "answer": 0,
                "hint": "Imagine grasping the conductor with your right hand with thumb along the current.",
                "explanation": "The Right-Hand Thumb Rule states that if the outstretched thumb points in the direction of conventional current, the curled fingers indicate the direction of magnetic field lines.",
                "solution": [
                    "Step 1: Grasp the conductor mentally using your right hand.",
                    "Step 2: Point your extended right thumb along the conventional current direction.",
                    "Step 3: Your fingers curl naturally in the direction of the concentric magnetic field lines."
                ]
            },
            {
                "question": "In NCERT Example 12.1, a horizontal wire carries current from East to West. What is the direction of the magnetic field at a point directly below the wire?",
                "options": [
                    "Directed toward the North",
                    "Directed toward the South",
                    "Directed toward the East",
                    "Directed vertically downward"
                ],
                "answer": 0,
                "hint": "Point your right thumb West: your fingers sweep northward under the wire.",
                "explanation": "Applying the Right-Hand Thumb Rule with the thumb pointing West, looking from the East end the field circulates clockwise, pointing North at points directly below the wire.",
                "solution": [
                    "Step 1: Align the right thumb toward the West along the direction of electric current.",
                    "Step 2: Observe the circulation of the fingers underneath the horizontal wire.",
                    "Step 3: Below the wire, the curled fingers point toward the North."
                ]
            },
            {
                "question": "How does the magnetic field strength B at a perpendicular distance r from a long straight wire vary with current I and distance r?",
                "options": [
                    "B is directly proportional to current I and inversely proportional to distance r (B ∝ I / r)",
                    "B is proportional to r² and inversely proportional to current I",
                    "B is directly proportional to both I² and r² simultaneously",
                    "B depends strictly on atmospheric air temperature, independent of I and r"
                ],
                "answer": 0,
                "hint": "More current strengthens the field, while greater distance weakens it linearly.",
                "explanation": "The magnetic field of a straight conductor is directly proportional to the electric current (B ∝ I) and inversely proportional to the radial distance (B ∝ 1/r).",
                "solution": [
                    "Step 1: Ampere's circuital law gives B = (μ₀ · I) / (2π · r).",
                    "Step 2: B increases directly as current I increases.",
                    "Step 3: B decreases inversely as distance r increases, giving B ∝ I / r."
                ]
            },
            {
                "question": "Why does a circular coil of n turns produce a magnetic field that is n times as strong as that of a single turn?",
                "options": [
                    "Current in each turn flows in the same direction, so the fields of all turns add up constructively",
                    "The electrical resistance of the wire drops by a factor of n when tightly coiled",
                    "The wire material changes into a permanent magnet during the winding process",
                    "Self-inductance eliminates all counter-electromotive force in the circuit"
                ],
                "answer": 0,
                "hint": "Consider the vector addition of magnetic fields produced by each individual turn.",
                "explanation": "Because current flows in the same direction through every turn of the coil, the individual magnetic fields generated by each turn superimpose and add together constructively.",
                "solution": [
                    "Step 1: Each turn carries the same current I in the same rotational sense.",
                    "Step 2: By the principle of superposition, B_total = B₁ + B₂ + ... + B_n.",
                    "Step 3: Since all n contributions are identical in direction, B_total = n · B_single."
                ]
            },
            {
                "question": "What is the spatial appearance of magnetic field lines near the exact center of a circular current-carrying loop?",
                "options": [
                    "Straight and parallel lines perpendicular to the plane of the loop",
                    "Tiny circular vortices spinning around the geometric center",
                    "Diverging radial spokes extending outwards to infinity",
                    "Zero field lines because opposing segments cancel each other completely"
                ],
                "answer": 0,
                "hint": "As the concentric circles expand near the center, their arcs straighten out.",
                "explanation": "At the center of a circular loop, the expanding concentric field lines from all wire segments become so large that their arcs straighten into parallel lines perpendicular to the loop.",
                "solution": [
                    "Step 1: Every segment of the loop generates concentric circular field lines.",
                    "Step 2: Toward the center, the radius of curvature becomes very large.",
                    "Step 3: At the center, the field lines appear as straight, parallel lines perpendicular to the coil's plane."
                ]
            },
            {
                "question": "What physical device consists of a cylindrical coil of many tight turns of insulated copper wire?",
                "options": [
                    "A solenoid",
                    "A rheostat",
                    "A potentiometer",
                    "An ammeter shunt"
                ],
                "answer": 0,
                "hint": "Recall the definition from Section 12.2.4 (Figure 12.10).",
                "explanation": "A coil of many circular turns of insulated copper wire wrapped closely in the shape of a cylinder is defined as a solenoid.",
                "solution": [
                    "Step 1: A solenoid is constructed by winding insulated copper wire helically around a cylindrical form.",
                    "Step 2: When current flows, each turn contributes a magnetic field resembling a bar magnet.",
                    "Step 3: Hence, this helical cylindrical coil is formally termed a solenoid."
                ]
            },
            {
                "question": "What does the parallel straight-line pattern of magnetic field lines inside a solenoid signify?",
                "options": [
                    "The magnetic field is completely uniform at all points inside the core",
                    "The magnetic field is rapidly fluctuating and non-existent at the center",
                    "The core is experiencing zero magnetic flux density",
                    "The magnetic field direction flips every millisecond"
                ],
                "answer": 0,
                "hint": "Parallel, equally spaced field lines always indicate uniform field strength and direction.",
                "explanation": "Parallel straight field lines inside a solenoid demonstrate that the magnetic field is uniform throughout its interior, having identical magnitude and direction everywhere.",
                "solution": [
                    "Step 1: Field lines inside a solenoid are parallel and uniformly spaced.",
                    "Step 2: Uniform spacing implies constant line density and therefore constant magnitude.",
                    "Step 3: Parallel straight lines imply invariant direction; hence, the field is completely uniform."
                ]
            },
            {
                "question": "How can a current-carrying solenoid be converted into an electromagnet?",
                "options": [
                    "By inserting a soft iron rod inside the core of the energized solenoid",
                    "By dipping the copper wire into a liquid insulating dielectric bath",
                    "By replacing the copper wire with a pure rubber elastic cord",
                    "By connecting the coil to an uncharged capacitor without a battery"
                ],
                "answer": 0,
                "hint": "A magnetic material with high permeability placed in the core becomes strongly magnetized.",
                "explanation": "Inserting a soft iron core into the uniform internal magnetic field of a current-carrying solenoid magnetizes the iron strongly, forming an electromagnet.",
                "solution": [
                    "Step 1: The interior of a solenoid has a strong, uniform magnetic field.",
                    "Step 2: Soft iron placed in this field has its magnetic domains aligned, dramatically enhancing the field.",
                    "Step 3: This combination of coil and temporary soft iron core constitutes an electromagnet."
                ]
            },
            {
                "question": "Why is soft iron preferred over hard carbon steel for the core of an electromagnet?",
                "options": [
                    "Soft iron loses its magnetism immediately when current is switched off, avoiding residual field",
                    "Soft iron has zero electrical conductivity so no eddy currents can ever flow",
                    "Soft iron is substantially lighter than all other known metallic elements",
                    "Soft iron permanently retains its magnetic field even when melted into liquid"
                ],
                "answer": 0,
                "hint": "Electromagnets must be able to switch off completely when the circuit opens.",
                "explanation": "Soft iron has high permeability and low retentivity, meaning it magnetizes strongly when current flows but demagnetizes immediately when current is disconnected.",
                "solution": [
                    "Step 1: An electromagnet requires rapid switching capability.",
                    "Step 2: Soft iron readily loses its magnetization once the magnetizing current ceases (low retentivity).",
                    "Step 3: Hard steel would retain permanent magnetism, making it unsuitable for switchable electromagnets."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Magnetic Force Review",
        "subtitle": "Mastery Review 3: Conductor Deflection, Fleming's Rule & Medical Biomagnetism",
        "speech": "",
        "questions": [
            {
                "question": "In Activity 12.7, an aluminium rod AB is suspended between the poles of a horseshoe magnet. What happens when electric current flows through the rod?",
                "options": [
                    "The rod is mechanically deflected (kicks) perpendicularly to both current and magnetic field",
                    "The rod spins continuously on its own longitudinal axis without moving sideways",
                    "The rod melts instantly due to electrostatic neutralization of magnetic charges",
                    "The rod experiences zero mechanical force because aluminium is non-magnetic"
                ],
                "answer": 0,
                "hint": "Ampere's principle: a magnetic field exerts a mechanical force on a current-carrying conductor.",
                "explanation": "A current-carrying conductor in a magnetic field experiences a Lorentz magnetic force that causes it to deflect perpendicular to both the conductor length and the field lines.",
                "solution": [
                    "Step 1: Moving electrons in the conductor experience a magnetic Lorentz force (F = I · L × B).",
                    "Step 2: This microscopic force transfers to the metal lattice of the aluminium rod.",
                    "Step 3: The rod physically displaces (deflects) perpendicular to both current and field directions."
                ]
            },
            {
                "question": "Under what orientation between a current-carrying conductor and an external magnetic field is the magnetic force zero?",
                "options": [
                    "When the conductor is aligned parallel (0° or 180°) to the magnetic field",
                    "When the conductor is aligned perpendicular (90°) to the magnetic field",
                    "When the conductor is tilted at exactly 45° to the magnetic field",
                    "When the conductor carries an alternating current of exactly 50 Hz"
                ],
                "answer": 0,
                "hint": "Recall F = I L B sin θ; for what angle θ does sin θ equal zero?",
                "explanation": "When a conductor is parallel to the magnetic field (angle θ = 0° or 180°), the magnetic force is zero because sin(0°) = sin(180°) = 0.",
                "solution": [
                    "Step 1: The magnitude of magnetic force on a conductor is given by F = I · L · B · sin θ.",
                    "Step 2: When the conductor is parallel to the field, θ = 0° or 180°.",
                    "Step 3: Since sin 0° = 0, the magnetic force is identically zero."
                ]
            },
            {
                "question": "In Fleming's Left-Hand Rule, what do the thumb, forefinger, and middle finger represent respectively?",
                "options": [
                    "Thumb = Motion/Force; Forefinger = Magnetic Field; Middle finger = Current",
                    "Thumb = Magnetic Field; Forefinger = Current; Middle finger = Force",
                    "Thumb = Current; Forefinger = Force; Middle finger = Magnetic Field",
                    "Thumb = Electric Potential; Forefinger = Resistance; Middle finger = Charge"
                ],
                "answer": 0,
                "hint": "Remember the FBI mnemonic: Force (Thumb), B-Field (Forefinger), I-Current (Middle finger).",
                "explanation": "In Fleming's Left-Hand Rule, the forefinger represents the magnetic Field, middle finger represents Current, and thumb represents the resulting Force (or motion).",
                "solution": [
                    "Step 1: Stretch the left hand thumb, forefinger, and middle finger mutually perpendicular.",
                    "Step 2: Forefinger points along the magnetic Field (B).",
                    "Step 3: Middle finger points along Current (I), and the Thumb points along Force/Motion (F)."
                ]
            },
            {
                "question": "A beam of electrons moving horizontally toward the right enters a uniform magnetic field directed vertically downwards. What is the direction of force acting on the electrons?",
                "options": [
                    "Into the page (away from the observer)",
                    "Out of the page (toward the observer)",
                    "Directly toward the right, accelerating speed",
                    "Vertically upward toward the sky"
                ],
                "answer": 0,
                "hint": "Electrons carry negative charge, so conventional current flows in the opposite direction (to the left).",
                "explanation": "Conventional current flows left (opposite electron motion). With forefinger pointing down (field) and middle finger left (current), Fleming's Left-Hand Rule directs the thumb into the page.",
                "solution": [
                    "Step 1: Electron velocity is to the right; therefore, conventional current I is to the left.",
                    "Step 2: The magnetic field B is directed vertically downwards.",
                    "Step 3: Applying Fleming's Left-Hand Rule (Forefinger down, Middle finger left), the Thumb points into the page."
                ]
            },
            {
                "question": "Which of the following electrical devices operates fundamentally based on the magnetic force on a current-carrying conductor?",
                "options": [
                    "An electric motor",
                    "An electric water heater",
                    "An incandescent light bulb",
                    "A chemical lead-acid battery"
                ],
                "answer": 0,
                "hint": "Which device converts electrical energy into mechanical rotational motion?",
                "explanation": "Electric motors utilize the magnetic force exerted on a current-carrying coil placed in a magnetic field to generate continuous rotational mechanical motion.",
                "solution": [
                    "Step 1: An electric motor consists of a rectangular current-carrying coil placed in a magnetic field.",
                    "Step 2: Fleming's Left-Hand Rule shows opposing forces act on opposite arms of the coil.",
                    "Step 3: These forces produce a continuous torque that drives mechanical rotation."
                ]
            },
            {
                "question": "A positively charged alpha-particle projected toward the West is deflected toward the North by a magnetic field. What is the direction of the magnetic field?",
                "options": [
                    "Directed vertically upward",
                    "Directed vertically downward",
                    "Directed toward the South",
                    "Directed toward the East"
                ],
                "answer": 0,
                "hint": "Alpha particles are positive (current is Westward); Force is Northward. Use Fleming's Left-Hand Rule.",
                "explanation": "With conventional current directed West (Middle finger) and force directed North (Thumb), Fleming's Left-Hand Rule requires the Forefinger (field) to point vertically upward.",
                "solution": [
                    "Step 1: Alpha particles are positive ions, so current direction is identical to motion: West.",
                    "Step 2: The observed deflection force is directed North.",
                    "Step 3: Orienting left Thumb North and Middle finger West, the Forefinger points vertically upward."
                ]
            },
            {
                "question": "Which physical property of a proton changes when it enters and moves freely in a uniform magnetic field?",
                "options": [
                    "Both velocity and momentum change (while speed remains constant)",
                    "Only its rest mass changes, while velocity remains strictly constant",
                    "Its electric charge is neutralized to become zero",
                    "Neither velocity nor momentum changes under any circumstance"
                ],
                "answer": 0,
                "hint": "Magnetic force is always perpendicular to velocity: it changes direction without changing speed.",
                "explanation": "Because magnetic force is perpendicular to velocity, it alters the direction of motion without changing speed; hence velocity (a vector) and momentum (p = mv) change.",
                "solution": [
                    "Step 1: Magnetic force on a charged particle is F = q(v × B), which is perpendicular to velocity v.",
                    "Step 2: Since work done by magnetic force is zero, kinetic energy and speed remain constant.",
                    "Step 3: However, the direction of motion bends, so velocity and momentum (vectors) continuously change."
                ]
            },
            {
                "question": "What is the primary physical cause of tiny biomagnetic fields generated inside the human body?",
                "options": [
                    "Ionic currents flowing along nerves during transmission of electrical impulses",
                    "Static electrostatic friction generated between bones and cartilage joints",
                    "Gravitational tides caused by the orbital motion of the Moon",
                    "Chemical oxidation of iron in red hemoglobin blood cells"
                ],
                "answer": 0,
                "hint": "Moving electric charges generate magnetic fields: nerve impulses are ionic charge flows.",
                "explanation": "Nerve impulses are electrical currents carried by moving sodium and potassium ions across cell membranes, inevitably creating weak surrounding biomagnetic fields.",
                "solution": [
                    "Step 1: In living organisms, neurological signaling occurs via action potentials (flow of charged ions).",
                    "Step 2: In accordance with Oersted's law, any movement of electric charge produces a magnetic field.",
                    "Step 3: These ionic currents generate biomagnetic fields, particularly in the heart and brain."
                ]
            },
            {
                "question": "What medical diagnostic technique utilizes body biomagnetism and external magnetic fields to produce detailed tissue images?",
                "options": [
                    "Magnetic Resonance Imaging (MRI)",
                    "Electrocardiogram (ECG)",
                    "X-ray Computed Tomography (CT)",
                    "Positron Emission Tomography (PET)"
                ],
                "answer": 0,
                "hint": "Check Section 12.3 'More to Know!' sidebar on Magnetism in Medicine.",
                "explanation": "Magnetic Resonance Imaging (MRI) uses powerful magnetic fields and radio waves to generate high-resolution cross-sectional images of internal body organs and tissues.",
                "solution": [
                    "Step 1: MRI aligns hydrogen nuclei in water molecules of body tissues using a strong magnetic field.",
                    "Step 2: Radio-frequency pulses temporarily perturb this alignment, causing nuclei to emit signals.",
                    "Step 3: Sensors detect these signals to construct extraordinarily detailed anatomical cross-sections."
                ]
            },
            {
                "question": "Approximately what fraction of Earth's magnetic field is the biomagnetic field produced by the human body?",
                "options": [
                    "About one-billionth of Earth's magnetic field (10⁻⁹)",
                    "About one-tenth of Earth's magnetic field (10⁻¹)",
                    "About ten times stronger than Earth's magnetic field",
                    "Exactly equal in magnitude to Earth's magnetic field"
                ],
                "answer": 0,
                "hint": "Human biomagnetic fields are extraordinarily weak, requiring ultra-sensitive detectors.",
                "explanation": "According to the NCERT textbook, the magnetic field produced inside the human body is extremely weak, measuring roughly one-billionth of Earth's geomagnetic field.",
                "solution": [
                    "Step 1: Earth's magnetic field at the surface is approximately 0.5 × 10⁻⁴ Tesla (0.5 Gauss).",
                    "Step 2: Biological fields produced by heart and brain currents are roughly 10⁻¹³ to 10⁻¹⁴ Tesla.",
                    "Step 3: This corresponds to approximately one-billionth of Earth's magnetic field."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Domestic Safety Review",
        "subtitle": "Mastery Review 4: Domestic Wiring, Short-Circuiting & Safety Fuses",
        "speech": "",
        "questions": [
            {
                "question": "In standard Indian domestic electric supply, what is the color coding of the insulation for Live, Neutral, and Earth wires?",
                "options": [
                    "Live: Red; Neutral: Black; Earth: Green",
                    "Live: Green; Neutral: Red; Earth: Black",
                    "Live: Black; Neutral: Green; Earth: Red",
                    "Live: Yellow; Neutral: Blue; Earth: White"
                ],
                "answer": 0,
                "hint": "Red for positive/live, Black for negative/neutral, Green for safety ground.",
                "explanation": "Conventionally in Indian domestic installations, the Live wire has red insulation, the Neutral wire has black insulation, and the Earth wire has green insulation.",
                "solution": [
                    "Step 1: Live wire carries high potential (220 V) and is color-coded Red.",
                    "Step 2: Neutral wire returns current at zero potential and is color-coded Black.",
                    "Step 3: Earth wire provides safety grounding and is color-coded Green."
                ]
            },
            {
                "question": "What is the nominal potential difference between the Live wire and the Neutral wire in Indian domestic power supply?",
                "options": [
                    "220 Volts (50 Hz alternating current)",
                    "110 Volts (60 Hz alternating current)",
                    "440 Volts (50 Hz three-phase current)",
                    "12 Volts (zero Hz direct current)"
                ],
                "answer": 0,
                "hint": "Standard household utility specification in India.",
                "explanation": "In India, domestic alternating current (AC) is delivered with a potential difference of 220 V between the live and neutral conductors at a frequency of 50 Hz.",
                "solution": [
                    "Step 1: The regional electricity distribution delivers single-phase AC power to homes.",
                    "Step 2: The root-mean-square potential difference between live and neutral is 220 V.",
                    "Step 3: The standard frequency of AC polarity reversal in India is 50 cycles per second (50 Hz)."
                ]
            },
            {
                "question": "What is the primary function of the green earth wire in domestic electrical appliances with metallic bodies?",
                "options": [
                    "It provides a low-resistance path to discharge leakage current into ground, preventing severe electric shocks",
                    "It supplies return current when the neutral wire breaks unexpectedly",
                    "It balances voltage fluctuations to maintain a constant 220 V during power cuts",
                    "It acts as a cooling duct that absorbs thermal energy from the motor windings"
                ],
                "answer": 0,
                "hint": "Metallic appliance bodies must be grounded to prevent live chassis shock hazards.",
                "explanation": "The earth wire connects the metal casing of an appliance directly to ground so that any leakage current flows harmlessly into Earth, keeping the casing at zero potential.",
                "solution": [
                    "Step 1: High-power appliances like irons and refrigerators have conductive metal casings.",
                    "Step 2: If live insulation fails and touches the casing, the earth wire provides an ultra-low resistance ground path.",
                    "Step 3: The surge current flows to ground rather than through a user's body, tripping the fuse safely."
                ]
            },
            {
                "question": "What physical event defines a short-circuit in an electric circuit?",
                "options": [
                    "Direct physical contact between the live wire and the neutral wire with negligible resistance",
                    "Opening of a plug key that completely interrupts current flow in a circuit",
                    "Connecting an excessively long extension cord to a low-power lamp",
                    "A momentary drop in voltage caused by lightning in a distant city"
                ],
                "answer": 0,
                "hint": "Live and neutral touch directly with near-zero resistance, causing massive current surge.",
                "explanation": "A short-circuit occurs when faulty or damaged insulation allows the live wire and neutral wire to touch directly, causing circuit resistance to drop to near zero and current to surge dangerously.",
                "solution": [
                    "Step 1: Live and neutral conductors normally remain separated by appliance load resistance.",
                    "Step 2: If insulation fails, they touch directly, bypassing the load.",
                    "Step 3: By Ohm's law (I = V/R), as R approaches zero, electric current surges massively."
                ]
            },
            {
                "question": "What is the effect on electric current in a domestic circuit during a severe short-circuit?",
                "options": [
                    "The current increases enormously and abruptly",
                    "The current drops to zero and stops immediately",
                    "The current alternates between positive and negative DC",
                    "The current remains completely unchanged"
                ],
                "answer": 0,
                "hint": "With resistance virtually eliminated, current surges to very high values.",
                "explanation": "During a short-circuit, the direct touching of live and neutral wires eliminates load resistance, causing the electric current to increase enormously, risking fire.",
                "solution": [
                    "Step 1: Total circuit resistance drops drastically to near zero.",
                    "Step 2: According to Ohm's Law, I = V / R.",
                    "Step 3: As R becomes extremely small, current I increases abruptly and massively."
                ]
            },
            {
                "question": "An electric oven rated 2 kW (220 V) is connected to a 5 A domestic circuit. What will be the immediate physical consequence?",
                "options": [
                    "The oven draws 9.09 A, exceeding the 5 A rating and causing the safety fuse to melt and break the circuit",
                    "The oven functions normally because electrical power automatically drops to 1 kW",
                    "The 5 A fuse cools down and doubles its electrical conductance permanently",
                    "The supply voltage automatically doubles to 440 V to prevent fuse meltdown"
                ],
                "answer": 0,
                "hint": "Calculate current: I = P / V = 2000 W / 220 V ≈ 9.09 A.",
                "explanation": "The oven draws I = 2000 W / 220 V ≈ 9.09 A. Since this current exceeds the 5 A fuse rating, excessive Joule heating melts the fuse wire, breaking the circuit.",
                "solution": [
                    "Step 1: Use the electric power relation: P = V · I ⇒ I = P / V.",
                    "Step 2: Calculate current: I = 2000 W / 220 V = 9.09 A.",
                    "Step 3: Because 9.09 A is greater than the 5 A fuse rating, the fuse wire melts and opens the circuit."
                ]
            },
            {
                "question": "Which of the following conditions causes electrical overloading in a domestic installation?",
                "options": [
                    "Connecting too many high-power appliances to a single electrical socket simultaneously",
                    "Operating a low-power LED night bulb continuously throughout the night",
                    "Connecting an earth wire to a metal plate buried deep in moist earth",
                    "Turning off appliances before disconnecting their wall plugs"
                ],
                "answer": 0,
                "hint": "Plugging many appliances into one socket draws excessive cumulative current from the line.",
                "explanation": "Overloading occurs when total current drawn exceeds safe wire ratings, typically caused by connecting too many appliances to one socket, accidental line surges, or short-circuits.",
                "solution": [
                    "Step 1: Each appliance in parallel draws its own rated branch current.",
                    "Step 2: Connecting multiple appliances to one multi-plug socket sums their currents (I_total = Σ I_i).",
                    "Step 3: When I_total exceeds the socket or cable rating, dangerous overloading occurs."
                ]
            },
            {
                "question": "How is an electric safety fuse always installed in a domestic branch circuit?",
                "options": [
                    "Connected in series with the Live wire before the appliance",
                    "Connected in parallel across the Live and Neutral wires",
                    "Connected in series with the Green earth wire only",
                    "Connected in parallel across the main water drainage pipe"
                ],
                "answer": 0,
                "hint": "A fuse must be in series with the live wire so melting isolates the high-voltage supply.",
                "explanation": "A fuse must be connected in series with the live wire so that when it melts during an overcurrent event, it completely disconnects the high-voltage live supply from the appliance.",
                "solution": [
                    "Step 1: The fuse protects against overcurrent by melting via Joule heating.",
                    "Step 2: It is installed in series with the Live wire carrying 220 V.",
                    "Step 3: When the fuse wire melts, the live connection is broken, leaving the downstream circuit de-energized and safe."
                ]
            },
            {
                "question": "Why are domestic circuits divided into two separate lines of 15 A and 5 A ratings?",
                "options": [
                    "To safely separate high-power appliances from low-power lighting circuits with appropriately rated wiring",
                    "To supply direct current to fans and alternating current to refrigerators",
                    "Because 15 A lines are grounded whereas 5 A lines cannot be grounded",
                    "To allow the electricity utility company to bill appliances at two different frequencies"
                ],
                "answer": 0,
                "hint": "Different devices consume vastly different amounts of current.",
                "explanation": "Separating domestic power into a 15 A circuit (heavy loads like heaters and ACs) and a 5 A circuit (lights and fans) ensures appropriate wire thickness and fuse ratings for safety.",
                "solution": [
                    "Step 1: High-power appliances draw large currents (6 A to 12 A) requiring thicker wires and 15 A fuses.",
                    "Step 2: Low-power appliances (bulbs, fans) draw less than 2 A and use thinner wires protected by 5 A fuses.",
                    "Step 3: Segregation prevents fire hazards and optimizes domestic electrical infrastructure."
                ]
            },
            {
                "question": "Which physical law governs the melting of a safety fuse wire when excessive current flows through it?",
                "options": [
                    "Joule's Law of Heating (H = I² · R · t)",
                    "Ohm's Law of Electrical Resistance (V = I · R)",
                    "Faraday's Law of Electromagnetic Induction",
                    "Coulomb's Law of Electrostatic Attraction"
                ],
                "answer": 0,
                "hint": "Heat generated is directly proportional to the square of current (I²).",
                "explanation": "Under Joule's Law of Heating (H = I²Rt), excessive current produces rapid thermal energy in the fuse wire, exceeding its low melting point and breaking the circuit.",
                "solution": [
                    "Step 1: Joule heating produces thermal energy at rate P = I² · R.",
                    "Step 2: When current I exceeds the safe threshold, the rate of heat generation surges quadratically.",
                    "Step 3: The fuse wire (lead-tin alloy) rapidly reaches its melting point and melts, severing the circuit."
                ]
            }
        ]
    }
]

# Validation
forbidden_personas = ["Dr.", "Dr ", "Doctor", "Sir ", "Madam", "Mr.", "Mr ", "Mrs.", "Mrs ", "Prof.", "Professor", "Raghav"]

for s in slides_part3:
    sid = s["id"]
    title = s["title"]
    title_words = len(title.split())
    assert 1 <= title_words <= 3, f"Slide {sid} title '{title}' must be 1 to 3 words, got {title_words}"

    slide_str = json.dumps(s)
    for forb in forbidden_personas:
        assert forb.lower() not in slide_str.lower(), f"Slide {sid} contains forbidden term '{forb}'"

    assert s["speech"] == "", f"Slide {sid} speech must be empty (silent exercise slide)"
    assert len(s["questions"]) == 10, f"Slide {sid} must have 10 challenge questions, got {len(s['questions'])}"

    for qidx, q in enumerate(s["questions"]):
        assert len(q["options"]) == 4, f"Slide {sid} question {qidx+1} must have 4 options"
        assert len(q["solution"]) == 3, f"Slide {sid} question {qidx+1} must have 3 solution steps"
        assert "hint" in q and "explanation" in q, f"Slide {sid} question {qidx+1} missing hint or explanation"

with open(".agents/c10s_ch12_part3.json", "w", encoding="utf-8") as f:
    json.dump(slides_part3, f, indent=2, ensure_ascii=False)

print("Part 3 (Slides 17 to 20) validated and saved successfully!")
