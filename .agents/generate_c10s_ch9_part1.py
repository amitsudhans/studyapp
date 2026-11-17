#!/usr/bin/env python3
"""
Generate Part 1 (Slides 1 to 8) for NCERT Class 10 Science Chapter 9: Light - Reflection and Refraction.
Strict requirements:
- Short title: strictly 1-3 words.
- Spoken lecture: strictly 195-215 words per slide.
- No persona titles (Dr, Sir, Madam, Mr, Mrs, Prof) and no character names (Raghav, etc.).
- Deeply pedagogical, aligned with NCERT Class 10 Science Chapter 9 syllabus.
"""

import json

SLIDES_PART1 = [
    {
        "id": 1,
        "title": "Light Nature Overview",
        "subtitle": "Visibility, Rectilinear Ray Propagation & Quantum Wave-Particle Duality",
        "speech": (
            "Light is a fundamental form of radiant electromagnetic energy that enables vision by reflecting off surrounding objects and entering "
            "our eyes. In everyday optical phenomena such as sharp shadow formation, beam projection, and reflections, light behaves as though "
            "it travels along straight lines, conceptually modeled as light rays. However, when light encounters an extremely tiny opaque obstacle "
            "comparable in size to its wavelength, it exhibits a fascinating bending phenomenon known as diffraction. In diffraction, light bends "
            "subtly around sharp geometric edges into the geometrical shadow region, where simple straight-line ray optics fails to explain the "
            "observed illumination. This bending demonstrated the wave nature of light, leading nineteenth-century physicists to model light as "
            "continuous transverse electromagnetic waves. Yet in the early twentieth century, discoveries like the photoelectric effect revealed "
            "that light also interacts with matter as discrete packets of energy called photons or particles. Modern quantum electrodynamics "
            "reconciles these two contrasting descriptions through quantum duality. Depending on the experimental scale, light exhibits either "
            "wave properties during propagation and interference, or particle properties during emission and absorption. In macroscopic optical "
            "systems involving mirrors and lenses, straight-line ray approximation remains exceptionally accurate and powerful for predicting "
            "image formation pathways."
        ),
        "objectives": [
            "Explain how straight-line ray propagation enables visibility and sharp shadow formation.",
            "Understand diffraction and why straight-line optics fails around nanoscale obstacles.",
            "Describe how modern quantum physics reconciles wave-particle duality in light propagation."
        ],
        "key_takeaways": [
            "Light travels in straight lines in uniform macroscopic media, forming rays and sharp shadows.",
            "Diffraction occurs when light bends around obstacles comparable to its wavelength.",
            "Quantum theory reconciles the wave-particle duality of radiant optical energy."
        ],
        "checkpoints": [
            {
                "question": "What optical phenomenon occurs when light bends around an opaque obstacle of microscopic size?",
                "options": [
                    "Total internal reflection",
                    "Diffraction",
                    "Electrostatic dispersion",
                    "Nuclear fission"
                ],
                "answer": 1,
                "hint": "Think of wave bending around tiny edges where straight ray optics breaks down.",
                "explanation": "Diffraction is the slight bending of light around the edges of tiny obstacles comparable to the wavelength of light."
            },
            {
                "question": "How does modern quantum theory resolve the controversy between the wave and particle models of light?",
                "options": [
                    "By proving light is exclusively a stationary mechanical wave",
                    "By reconciling both behaviors through wave-particle quantum duality",
                    "By proving light has neither speed nor wavelength",
                    "By demonstrating that light only travels through solid metals"
                ],
                "answer": 1,
                "hint": "Consider how light behaves as both continuous waves and discrete photons.",
                "explanation": "Modern quantum theory recognizes that light exhibits wave-particle duality, acting as waves during propagation and particles during emission/absorption."
            }
        ]
    },
    {
        "id": 2,
        "title": "Reflection Fundamental Laws",
        "subtitle": "Universal Laws of Reflection & Plane Mirror Virtual Image Properties",
        "speech": (
            "When a beam of light strikes a smooth, polished boundary between two media, it bounces back into the original medium according "
            "to two universal laws of reflection. First, the angle of incidence, denoted as angle i, is strictly equal to the angle of reflection, "
            "denoted as angle r. Second, the incident ray, the normal drawn perpendicular to the reflecting boundary at the point of incidence, "
            "and the reflected ray all lie within the same mathematical plane. These fundamental laws apply universally to all reflecting surfaces, "
            "including flat plane mirrors and curved spherical mirrors. When an object is placed in front of a flat plane mirror, reflection "
            "produces a distinct virtual image. Because the reflected rays diverge and never actually intersect, they only appear to originate "
            "from behind the mirror surface when extended backward. The image formed by a plane mirror is always virtual, upright or erect, "
            "and identical in dimensions to the physical object. Furthermore, the perpendicular distance of the image behind the mirror equals "
            "the perpendicular distance of the object in front of the mirror. A distinctive feature of plane mirror reflection is lateral "
            "inversion, where the right side of the object appears as the left side of the reflected image."
        ),
        "objectives": [
            "State the two fundamental laws of reflection applicable to all reflecting surfaces.",
            "Characterize plane mirror images: virtual, erect, equal size, and equal distance.",
            "Explain lateral inversion and why plane mirror images cannot be focused onto a physical screen."
        ],
        "key_takeaways": [
            "Angle of incidence always equals angle of reflection (i = r).",
            "Incident ray, normal, and reflected ray are coplanar at the point of incidence.",
            "Plane mirror images are virtual, erect, laterally inverted, and situated at equal distance behind the mirror."
        ],
        "checkpoints": [
            {
                "question": "If a ray of light strikes a plane reflecting surface at an angle of incidence of 35 degrees, what is the angle of reflection?",
                "options": [
                    "55 degrees",
                    "35 degrees",
                    "70 degrees",
                    "0 degrees"
                ],
                "answer": 1,
                "hint": "Recall the first law of reflection relating angle i to angle r.",
                "explanation": "According to the first law of reflection, the angle of reflection strictly equals the angle of incidence (r = i = 35°)."
            },
            {
                "question": "Which of the following characteristics correctly describes the image formed by a flat plane mirror?",
                "options": [
                    "Real, inverted, and magnified",
                    "Virtual, erect, laterally inverted, and of the same size as the object",
                    "Real, erect, and highly diminished",
                    "Virtual, inverted, and located infinitely behind the mirror"
                ],
                "answer": 1,
                "hint": "Consider your daily reflection in a bathroom dressing mirror.",
                "explanation": "Images in plane mirrors are virtual (cannot be captured on a screen), erect, laterally inverted, and equal in size to the object."
            }
        ]
    },
    {
        "id": 3,
        "title": "Spherical Mirror Anatomy",
        "subtitle": "Concave vs Convex Geometries, Curvature Center, Focal Point & R = 2f",
        "speech": (
            "A spherical mirror is an optical reflector whose curved reflecting boundary forms part of the surface of a hollow glass sphere. "
            "Spherical mirrors are classified into two structural types based on their curvature direction. A concave mirror possesses a reflecting "
            "surface curved inward toward the center of the sphere, functioning as a converging mirror. A convex mirror possesses a reflecting "
            "surface curved outward away from the center, functioning as a diverging mirror. Several anatomical reference terms define these "
            "mirrors. The geometric center of the reflecting surface is the pole, denoted as capital P. The center of the sphere from which the "
            "mirror is sliced is the center of curvature, capital C, which lies in front of a concave mirror and behind a convex mirror. The straight "
            "reference line passing through pole P and center C is the principal axis. When paraxial rays parallel to the principal axis strike "
            "a concave mirror, they converge at a single point called the principal focus, capital F. The distance between pole P and focus F "
            "is the focal length, small f. For spherical mirrors with small apertures, the radius of curvature R equals twice the focal length, "
            "meaning capital F lies exactly midway between P and C."
        ),
        "objectives": [
            "Distinguish between inward-curving concave and outward-curving convex mirrors.",
            "Define optical landmarks: Pole (P), Center of Curvature (C), Principal Axis, and Focus (F).",
            "Apply the mathematical relationship R = 2f for spherical mirrors of small aperture."
        ],
        "key_takeaways": [
            "Concave mirrors curve inward (converging); convex mirrors curve outward (diverging).",
            "Pole P is on the mirror surface; Center C is the center of the originating sphere.",
            "For mirrors of small aperture, the focal length f is half the radius of curvature (R = 2f)."
        ],
        "checkpoints": [
            {
                "question": "If the radius of curvature of a spherical mirror is 30 centimeters, what is its focal length?",
                "options": [
                    "60 cm",
                    "15 cm",
                    "30 cm",
                    "7.5 cm"
                ],
                "answer": 1,
                "hint": "Use the formula relating radius of curvature R to focal length f (R = 2f).",
                "explanation": "For a spherical mirror of small aperture, f = R / 2. Here, f = 30 cm / 2 = 15 cm."
            },
            {
                "question": "Where does the center of curvature (C) lie for a convex spherical mirror?",
                "options": [
                    "In front of the reflecting surface",
                    "Behind the reflecting surface",
                    "Directly on the surface of the mirror at the pole",
                    "At infinity along the vertical axis"
                ],
                "answer": 1,
                "hint": "Recall that a convex mirror curves outwards, so the hollow sphere center lies within.",
                "explanation": "In a convex mirror, the reflecting surface curves outwards, so its center of curvature lies behind the mirror surface."
            }
        ]
    },
    {
        "id": 4,
        "title": "Concave Mirror Raytracing",
        "subtitle": "The 4 Standard Ray Tracing Rules for Precision Image Construction",
        "speech": (
            "To construct accurate geometric images formed by spherical mirrors, optical physics relies on four standardized ray tracing rules "
            "derived directly from the laws of reflection. The first rule states that any incident ray traveling parallel to the principal axis "
            "will, after reflecting from a concave mirror, pass directly through the principal focus F. The second rule is the optical converse "
            "of the first: any incident ray that passes through the principal focus F strikes the mirror and reflects outward parallel to the "
            "principal axis. The third rule states that an incident ray passing through the center of curvature C strikes the mirror surface "
            "normally along the local radius of curvature; consequently, its angle of incidence is zero, and it reflects directly back along "
            "its own incoming path. The fourth rule states that an incident ray directed obliquely at the pole P reflects obliquely at an identical "
            "angle relative to the principal axis, strictly satisfying the law of reflection where angle i equals angle r. Because an image point "
            "is formed wherever at least two reflected rays intersect or appear to intersect, choosing any two of these four convenient rays allows "
            "us to pinpoint the exact location, size, and orientation of any optical image."
        ),
        "objectives": [
            "Master the 4 standard ray tracing rules for concave spherical mirrors.",
            "Understand why a ray passing through C retraces its path upon reflection.",
            "Combine any two characteristic rays to locate the intersection forming an image."
        ],
        "key_takeaways": [
            "Ray parallel to principal axis reflects through focus F.",
            "Ray through focus F reflects parallel to principal axis.",
            "Ray through center C reflects back along its own path (normal incidence, i = 0).",
            "Ray incident at pole P reflects symmetrically with angle i = angle r."
        ],
        "checkpoints": [
            {
                "question": "Why does a light ray passing through the center of curvature (C) of a concave mirror retrace its path after reflection?",
                "options": [
                    "It gets absorbed completely by the glass molecules",
                    "It strikes the mirror surface normally along the radius, so angle i = 0",
                    "It bends due to high air pressure near the center",
                    "The focal point pulls the ray backward magnetically"
                ],
                "answer": 1,
                "hint": "A line from the sphere center to the surface is a radius, which is normal to the surface.",
                "explanation": "The radius of curvature is perpendicular to the mirror surface at every point; hence, incidence is normal (i = 0°), causing the ray to retrace its path."
            },
            {
                "question": "How many reflected rays are minimally required to locate the position of an image point in geometric optics?",
                "options": [
                    "Only one ray",
                    "At least two intersecting rays",
                    "Exactly four rays",
                    "An infinite number of rays"
                ],
                "answer": 1,
                "hint": "Two intersecting lines uniquely define a point in space.",
                "explanation": "The intersection of at least two reflected rays is necessary and sufficient to geometrically fix the position of an image point."
            }
        ]
    },
    {
        "id": 5,
        "title": "Concave Image Formation",
        "subtitle": "Analysis of the 6 Object Placement Scenarios & Image Inversion Shifts",
        "speech": (
            "A concave mirror exhibits rich optical versatility, forming dramatically different images depending on the distance of the object "
            "from the pole. When an object is at infinity, incoming parallel rays converge at the focus F, forming a real, inverted, and point-sized "
            "diminished image. Moving the object closer to a position beyond C produces a real, inverted, and diminished image located between F "
            "and C. When the object is placed exactly at the center of curvature C, the reflected rays converge precisely at C, forming a real, "
            "inverted image of identical size to the object. Moving the object further inward between C and F shifts the image position outward "
            "beyond C, producing a real, inverted, and magnified image. When the object is placed directly at the principal focus F, the reflected "
            "rays emerge parallel to each other, forming a real, inverted, and highly enlarged image at infinity. Finally, when the object is placed "
            "very close to the mirror between the pole P and focus F, the reflected rays diverge. When projected backward behind the mirror, they "
            "converge virtually, producing an upright, virtual, and highly magnified image. This unique sixth scenario makes concave mirrors "
            "invaluable for close-up magnification."
        ),
        "objectives": [
            "Analyze the 6 object positions for a concave mirror (Table 9.1).",
            "Trace the progression of image size from point-sized at F to magnified at infinity.",
            "Identify the unique scenario (object between P and F) yielding a virtual erect enlarged image."
        ],
        "key_takeaways": [
            "Object at infinity -> image at F (point-sized, real, inverted).",
            "Object at C -> image at C (same size, real, inverted).",
            "Object between P and F -> image behind mirror (virtual, erect, magnified)."
        ],
        "checkpoints": [
            {
                "question": "Where should an object be placed in front of a concave mirror to obtain an image of the same size as the object?",
                "options": [
                    "At the principal focus (F)",
                    "Between the pole (P) and focus (F)",
                    "At the center of curvature (C)",
                    "At infinity"
                ],
                "answer": 2,
                "hint": "Recall the symmetric configuration where object distance equals image distance.",
                "explanation": "When an object is placed at the center of curvature (C) of a concave mirror, a real, inverted image of the same size is formed at C."
            },
            {
                "question": "In which position does a concave mirror produce a virtual, erect, and magnified image?",
                "options": [
                    "When the object is placed beyond C",
                    "When the object is placed between the pole (P) and focus (F)",
                    "When the object is placed at the center of curvature (C)",
                    "When the object is placed at infinity"
                ],
                "answer": 1,
                "hint": "This is the only configuration where reflected rays diverge in front and meet virtually behind.",
                "explanation": "Placing an object between P and F produces diverging reflected rays whose backward extensions form an erect, magnified virtual image behind the mirror."
            }
        ]
    },
    {
        "id": 6,
        "title": "Concave Mirror Applications",
        "subtitle": "Headlights, Shaving Optics, Dental Mirrors & High-Heat Solar Furnaces",
        "speech": (
            "The optical properties of concave mirrors make them essential across diverse modern technological and everyday applications. In vehicle "
            "headlights, torches, and searchlights, a high-intensity light bulb is placed precisely at the principal focus F of a concave reflector. "
            "Because light rays originating from the focus reflect parallel to the principal axis, the mirror projects a powerful, parallel beam "
            "of light that travels vast distances without spreading out or losing intensity. In personal grooming, concave mirrors are widely "
            "utilized as shaving and makeup mirrors. When an individual positions their face within the focal distance, between the pole P and "
            "focus F, the mirror produces an erect, highly magnified virtual image, allowing clear inspection of skin and facial details. Dentists "
            "routinely rely on compact concave mirrors mounted on slender angled handles to view enlarged, erect images of back molars and cavities inside "
            "a patient's mouth with precision. Furthermore, large industrial concave mirrors are deployed in clean solar furnaces. Because parallel rays of sunlight "
            "converge at the principal focus, placing a thermal crucible or boiler at the focal point concentrates solar radiant energy onto "
            "a tiny area, generating extreme temperatures exceeding thousands of degrees Celsius without burning any fossil fuels."
        ),
        "objectives": [
            "Explain how placing bulbs at focus F produces intense parallel beams in searchlights and headlights.",
            "Describe how placing facial features between P and F yields enlarged virtual views for shaving and dentists.",
            "Illustrate how solar furnaces concentrate parallel solar rays at focus F to generate extreme temperatures."
        ],
        "key_takeaways": [
            "Source at focus F -> parallel beam output (torches, searchlights, headlights).",
            "Object between P and F -> erect magnified virtual image (dentist mirrors, shaving mirrors).",
            "Sunlight focused at F -> intense thermal concentration (solar furnaces)."
        ],
        "checkpoints": [
            {
                "question": "Why is the light bulb in automobile headlights placed precisely at the principal focus of the concave reflector?",
                "options": [
                    "To create a virtual diminished image of the road",
                    "To project a powerful beam of parallel light rays ahead",
                    "To make the light change into different rainbow colors",
                    "To heat the engine block during winter driving"
                ],
                "answer": 1,
                "hint": "Rays originating from the focus reflect parallel to the principal axis.",
                "explanation": "Placing the light source at the focus of a concave mirror ensures that reflected rays emerge parallel, projecting a powerful directional beam."
            },
            {
                "question": "Why do dentists use small concave mirrors to inspect patient teeth?",
                "options": [
                    "They invert the tooth image to read serial numbers",
                    "They produce an erect, enlarged virtual image when held close to the tooth",
                    "They absorb dental saliva using infrared rays",
                    "They emit laser light to cure tooth fillings"
                ],
                "answer": 1,
                "hint": "Holding the tooth between pole P and focus F magnifies the view upright.",
                "explanation": "When held within the focal length, a concave mirror forms an erect and magnified virtual image of the tooth for precise examination."
            }
        ]
    },
    {
        "id": 7,
        "title": "Convex Mirror Optics",
        "subtitle": "Diverging Ray Geometry, Virtual Diminished Images & Automotive Safety",
        "speech": (
            "A convex mirror possesses a reflecting boundary that curves outward, causing all incident parallel light rays to diverge away from "
            "the principal axis upon reflection. When these diverging rays are extended backward behind the mirror surface, they appear to intersect "
            "at the virtual principal focus F. Consequently, the focal point and center of curvature of a convex mirror both lie behind the "
            "mirror surface. Regardless of where an object is placed in front of a convex mirror, it consistently forms a virtual, erect, and "
            "diminished image located behind the mirror between the pole P and focus F. If the object is at infinity, the image is formed at focus "
            "F as a virtual, erect, point-sized dot. Because convex mirrors always produce upright images and curve outwards toward the viewer, they provide a much "
            "wider panoramic field of view than flat plane mirrors of equal aperture. This optical property makes convex mirrors the universal "
            "standard for automotive rear-view mirrors and driver side-mirrors, enabling motorists to view large expanses of trailing highway "
            "traffic safely. Convex mirrors are also mounted at blind roadway corners, parking garage ramps, and large retail store ceilings for reliable surveillance "
            "and collision prevention in busy corridors."
        ),
        "objectives": [
            "Understand why convex mirrors act as diverging reflectors with virtual foci behind the mirror.",
            "Verify that convex mirrors invariably produce virtual, erect, and diminished images.",
            "Explain why automotive rear-view mirrors utilize convex mirrors for an expanded field of view."
        ],
        "key_takeaways": [
            "Convex mirrors diverge light; focus F and center C lie behind the mirror.",
            "Always forms virtual, erect, and diminished images regardless of object distance.",
            "Curved outward shape provides an expanded panoramic field of view for vehicle safety."
        ],
        "checkpoints": [
            {
                "question": "What type of image is always produced by a convex spherical mirror for any real object placed in front of it?",
                "options": [
                    "Real, inverted, and magnified",
                    "Virtual, erect, and diminished",
                    "Real, erect, and of the same size",
                    "Virtual, inverted, and magnified"
                ],
                "answer": 1,
                "hint": "Think of what you see in a car side-view mirror.",
                "explanation": "Convex mirrors always form virtual, erect, and diminished images situated behind the mirror between pole P and focus F."
            },
            {
                "question": "Why are convex mirrors universally preferred as rear-view mirrors in automobiles?",
                "options": [
                    "They show objects upside down to alert the driver",
                    "They provide an erect image and a much wider field of view than plane mirrors",
                    "They absorb glare by turning all headlights green",
                    "They magnify distant vehicles to make them appear closer"
                ],
                "answer": 1,
                "hint": "Consider the outward curvature allowing drivers to see multi-lane traffic.",
                "explanation": "Because they curve outwards, convex mirrors provide a wider panoramic field of view while always maintaining erect images of trailing traffic."
            }
        ]
    },
    {
        "id": 8,
        "title": "Cartesian Sign Convention",
        "subtitle": "Coordinate Frame, Negative Object Distances & Focal Sign Rules",
        "speech": (
            "To apply mathematical formulas to spherical mirrors and lenses without ambiguity, optical physicists adhere strictly to the "
            "New Cartesian Sign Convention. In this coordinate system, the pole P of the mirror serves as the geometric origin, while the principal "
            "axis serves as the horizontal X-axis. By convention, the object is always placed to the left of the mirror, meaning incident light "
            "travels from left to right. All distances measured parallel to the principal axis from the pole P in the direction of incident light "
            "(to the right, along the positive X-axis) are assigned positive values. Conversely, all distances measured against the direction "
            "of incident light (to the left of pole P, along the negative X-axis) are assigned negative values. Because the physical object is "
            "always placed to the left, the object distance u is always negative in mirror calculations. Heights measured perpendicularly above "
            "the principal axis (along the positive Y-axis) are positive, while heights measured below (along the negative Y-axis) are negative. "
            "Consequently, because the focus of a concave mirror lies in front to the left, its focal length f is always negative. In contrast, "
            "because the focus of a convex mirror lies behind to the right, its focal length f is always positive."
        ),
        "objectives": [
            "Master the New Cartesian Sign Convention rules for spherical mirrors.",
            "Understand why object distance u is universally negative.",
            "Identify the sign rules for focal lengths: negative for concave, positive for convex."
        ],
        "key_takeaways": [
            "Pole P is the origin; principal axis is the X-axis; light travels from left to right.",
            "Distances to the left of P are negative; distances to the right are positive.",
            "Object distance u is always negative; concave focal length f is negative; convex focal length f is positive."
        ],
        "checkpoints": [
            {
                "question": "According to the New Cartesian Sign Convention, what is the sign of the focal length of a concave mirror?",
                "options": [
                    "Always positive",
                    "Always negative",
                    "Positive only if the object is large",
                    "Zero at all times"
                ],
                "answer": 1,
                "hint": "The focus of a concave mirror lies in front to the left of the pole.",
                "explanation": "Since the focus of a concave mirror lies to the left of the pole (against incident light), its focal length f is always negative."
            },
            {
                "question": "Why is the object distance (u) always assigned a negative sign in spherical mirror calculations?",
                "options": [
                    "Because objects only emit negative energy",
                    "Because the object is conventionally placed to the left of the mirror, opposite to incident ray direction",
                    "Because mirrors destroy optical rays",
                    "Because all objects must be virtual"
                ],
                "answer": 1,
                "hint": "Review the convention that objects are placed on the left side of the origin P.",
                "explanation": "By convention, objects are placed to the left of the pole; measuring from P to the object goes against incident light, making u negative."
            }
        ]
    }
]

if __name__ == "__main__":
    print("=== CHECKING SLIDES 1 TO 8 DATA ===")
    for s in SLIDES_PART1:
        title_words = len(s["title"].split())
        speech_words = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' | Title words: {title_words} | Speech words: {speech_words}")
        assert title_words <= 3, f"Title has >3 words: {s['title']}"
        assert 195 <= speech_words <= 215, f"Speech words out of range: {speech_words} in Slide {s['id']}"

    with open(".agents/c10s_ch9_part1.json", "w", encoding="utf-8") as f:
        json.dump(SLIDES_PART1, f, indent=2)
    print("Saved .agents/c10s_ch9_part1.json successfully!")
