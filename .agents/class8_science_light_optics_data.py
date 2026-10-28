# -*- coding: utf-8 -*-
"""
Class 8 Science - Chapter 10: Light and Optics (Spherical Mirrors, Laws of Reflection, Lenses & Scientific Heritage)
Comprehensive Dataset:
- 20 Slides (16 Interactive Theory/Sim Slides + 4 Dedicated Mastery Challenge Slides)
- 32 In-Slide Checkpoints (2 per content slide) with instant feedback
- 40 Mastery Quiz Questions with full step-by-step solutions
- Key Technical Vocabulary for every slide
- Teacher Avatar Narration (Acharya Bhāskara II)
"""

SLIDES = [
    {
        "id": 1,
        "tag": "Mirror Foundations",
        "title": "Spherical Mirrors Anatomy",
        "sim_id": "spherical_mirror_anatomy_sim",
        "avatar_dialogue": "Welcome to the Light & Optics Laboratory! Spherical mirrors are curved mirrors shaped like a slice of an imaginary hollow sphere, crafted by precision grinding and polishing of flat glass.",
        "vocabulary": [
            {"word": "Spherical Mirror", "definition": "A curved mirror whose reflecting surface forms part of an imaginary hollow sphere."},
            {"word": "Concave Mirror", "definition": "A spherical mirror with a reflecting surface that curves inwards toward the center of the sphere (non-reflecting back is shaded)."},
            {"word": "Convex Mirror", "definition": "A spherical mirror with a reflecting surface that curves outwards away from the center of the sphere."},
            {"word": "Precision Polishing", "definition": "The manufacturing technique where flat glass is ground and polished into precise spherical curvatures rather than slicing real hollow glass balls."}
        ],
        "theory": r"""
          <p>Unlike flat plane mirrors, <strong>spherical mirrors</strong> possess curved reflecting surfaces that manipulate light rays in remarkable ways:</p>
          <ul>
            <li><strong>Geometric Origin:</strong> Think of an imaginary hollow glass sphere. If a portion of this curved sphere is polished with a reflecting silver or aluminum coating, it forms a spherical mirror. In actual manufacturing, optical technicians carefully grind and polish flat glass discs to achieve this precise spherical curve.</li>
            <li><strong>Concave Mirror (Converging):</strong>
              <ul>
                <li>The reflecting surface curves <strong>inwards</strong> (like the inner bowl of a shiny stainless steel spoon or a dark cave).</li>
                <li>In schematic diagrams, the non-reflecting back surface is represented with short angled shading lines.</li>
              </ul>
            </li>
            <li><strong>Convex Mirror (Diverging):</strong>
              <ul>
                <li>The reflecting surface curves <strong>outwards</strong> (like the back outer surface of a shiny spoon or a polished sphere).</li>
                <li>The non-reflecting inner surface is shaded in optical diagrams.</li>
              </ul>
            </li>
          </ul>
        """,
        "checkpoints": [
            {
                "question": "Which of the following describes a concave mirror?",
                "options": [
                    "A. A mirror whose reflecting surface curves outwards",
                    "B. A mirror whose reflecting surface curves inwards",
                    "C. A flat mirror with zero curvature",
                    "D. A transparent lens that transmits light rays"
                ],
                "correct": 1,
                "explanation": "A concave mirror has its reflecting surface curved inwards, like the inner bowl of a shiny spoon."
            },
            {
                "question": "How are spherical mirrors practically manufactured in modern optical workshops?",
                "options": [
                    "A. By slicing actual thin hollow glass bubbles with scissors",
                    "B. By grinding and polishing flat glass pieces into precise spherical curves",
                    "C. By melting plastic sheets over open wood fires",
                    "D. By folding aluminum foil into curved shapes"
                ],
                "correct": 1,
                "explanation": "Spherical mirrors are fabricated by precision grinding and optical polishing of solid flat glass blanks into exact spherical curvatures."
            }
        ]
    },
    {
        "id": 2,
        "tag": "Image Formation",
        "title": "Concave Mirror Image Dynamics",
        "sim_id": "concave_mirror_image_sim",
        "avatar_dialogue": "Hold a shiny steel spoon close to your nose: your face appears upright and giant! Pull it away, and suddenly your face flips completely upside-down! That is the dynamic magic of a concave mirror.",
        "vocabulary": [
            {"word": "Erect Image", "definition": "An image that appears right-side up with the same vertical orientation as the object."},
            {"word": "Inverted Image", "definition": "An image that is flipped upside-down relative to the object."},
            {"word": "Enlarged (Magnified)", "definition": "An image that appears physically larger than the actual object."},
            {"word": "Diminished", "definition": "An image that appears physically smaller than the actual object."}
        ],
        "theory": r"""
          <p>The image formed by a <strong>concave mirror</strong> changes dramatically depending on the distance between the object and the mirror surface:</p>
          <ul>
            <li><strong>Object Placed Close to the Mirror (Inside Focus):</strong>
              <ul>
                <li>The image formed is <strong>erect (upright)</strong> and <strong>enlarged (magnified)</strong>.</li>
                <li>This is why dentists use concave mirrors to inspect teeth and why people use them as shaving and makeup mirrors.</li>
              </ul>
            </li>
            <li><strong>Object Moved Farther Away:</strong>
              <ul>
                <li>As you withdraw the object past the focal point, the image flips into an <strong>inverted (upside-down)</strong> image!</li>
                <li>At moderate distances, the inverted image remains enlarged; as the object moves very far away, the inverted image shrinks and becomes <strong>diminished (smaller than the object)</strong>.</li>
              </ul>
            </li>
          </ul>
        """,
        "checkpoints": [
            {
                "question": "What type of image is formed when your face is positioned very close to a concave mirror?",
                "options": [
                    "A. Inverted and diminished",
                    "B. Erect and enlarged (magnified)",
                    "C. Inverted and identical in size",
                    "D. No image is formed at all"
                ],
                "correct": 1,
                "explanation": "When an object is close to a concave mirror (inside its focal point), the image is erect and enlarged, which is why dentists use it."
            },
            {
                "question": "What happens to the image of a candle flame in a concave mirror when the candle is moved far away from the mirror?",
                "options": [
                    "A. It remains erect and grows ten times larger",
                    "B. It becomes inverted (upside down) and diminished in size",
                    "C. It disappears into complete darkness",
                    "D. It turns into a convex lens"
                ],
                "correct": 1,
                "explanation": "Moving the object far away from a concave mirror produces an inverted, diminished real image."
            }
        ]
    },
    {
        "id": 3,
        "tag": "Field of View",
        "title": "Convex Mirror Field of View",
        "sim_id": "convex_mirror_fov_sim",
        "avatar_dialogue": "Look into the back of a shiny spoon or a car side-view mirror: everything is always upright and compact! A convex mirror curves outward, squeezing a wide horizon into a compact reflection.",
        "vocabulary": [
            {"word": "Field of View", "definition": "The observable world that is visible through an optical device or mirror at a particular position and orientation."},
            {"word": "Always Diminished", "definition": "Convex mirrors exclusively produce images that are smaller than the actual object, regardless of object distance."},
            {"word": "Driver's Side-View Mirror", "definition": "A convex mirror fitted on automobiles to give drivers a wide, erect perspective of trailing traffic."}
        ],
        "theory": r"""
          <p>Unlike concave mirrors, a <strong>convex mirror</strong> behaves with absolute consistency across all distances:</p>
          <ul>
            <li><strong>Invariant Image Characteristics:</strong>
              <ul>
                <li>The image formed by a convex mirror is <strong>always erect (upright)</strong>.</li>
                <li>The image is <strong>always diminished (smaller than the object)</strong>.</li>
                <li>The image appears to be located behind the mirror surface.</li>
              </ul>
            </li>
            <li><strong>Expansive Field of View:</strong>
              <ul>
                <li>Because the reflecting surface bulges outwards, light rays striking from broad peripheral angles reflect into the viewer's eye.</li>
                <li>A convex mirror provides a vastly <strong>wider field of view</strong> than a flat plane mirror of the same size, allowing drivers to monitor multiple lanes of traffic simultaneously.</li>
              </ul>
            </li>
          </ul>
        """,
        "checkpoints": [
            {
                "question": "Which of the following is an invariant property of the image formed by a convex mirror?",
                "options": [
                    "A. It is always inverted and magnified",
                    "B. It is always erect and diminished (smaller than the object)",
                    "C. It flips upside-down when moved far away",
                    "D. It is always larger than the object"
                ],
                "correct": 1,
                "explanation": "A convex mirror always forms an erect, diminished image regardless of how close or far the object is placed."
            },
            {
                "question": "Why are convex mirrors preferred over flat plane mirrors as vehicle side-view (wing) mirrors?",
                "options": [
                    "A. They make cars look upside down",
                    "B. They provide a much wider field of view while always keeping images upright",
                    "C. They absorb all headlight glare completely",
                    "D. They are made of solid steel without glass"
                ],
                "correct": 1,
                "explanation": "The outward bulge allows convex mirrors to capture a broader angular field of view, presenting an erect, compact panoramic view of road traffic."
            }
        ]
    },
    {
        "id": 4,
        "tag": "Mirror Optics",
        "title": "Lateral Inversion in Mirrors",
        "sim_id": "lateral_inversion_sim",
        "avatar_dialogue": "Raise your right hand before any mirror—your reflection raises its left hand! This left-right reversal is called lateral inversion, and it occurs in plane, concave, and convex mirrors alike.",
        "vocabulary": [
            {"word": "Lateral Inversion", "definition": "The apparent reversal of the horizontal axis where the left side of the object appears as the right side in the image."},
            {"word": "Symmetry Plane", "definition": "The geometric plane where rays reflect perpendicularly, preserving top-bottom orientation while swapping perceived left and right."},
            {"word": "Ambulance Lettering", "definition": "The practice of writing 'AMBULANCE' backward on vehicle hoods so leading drivers read it correctly in rear-view mirrors."}
        ],
        "theory": r"""
          <p>When light reflects from any mirror surface, it undergoes a spatial transformation known as <strong>lateral inversion</strong>:</p>
          <ul>
            <li><strong>The Phenomenon:</strong> Stand in front of a mirror and touch your right ear. In the reflection, the figure appears to touch its left ear! The vertical axis (top and bottom) remains unchanged, but the perceived left and right sides are interchanged.</li>
            <li><strong>Universality:</strong> Lateral inversion is <strong>not unique to plane mirrors</strong>; it occurs equally across <em>plane mirrors, concave mirrors, and convex mirrors</em> whenever an upright image is reflected.</li>
            <li><strong>Practical Engineering:</strong> Emergency vehicles have the word <strong>"AMBULANCE"</strong> painted in lateral reverse ($\text{ƎƆИA⅃UBMA}$) on their front hoods. When a driver ahead checks their rear-view or side-view mirror, lateral inversion flips the text right-way around, enabling instant recognition!</li>
          </ul>
        """,
        "checkpoints": [
            {
                "question": "In which types of mirrors can lateral inversion be observed?",
                "options": [
                    "A. Only in flat plane mirrors",
                    "B. In plane, concave, and convex mirrors alike",
                    "C. Only in transparent glass lenses",
                    "D. Only in solar water heaters"
                ],
                "correct": 1,
                "explanation": "Lateral inversion is a universal property of reflection that occurs across plane, concave, and convex mirrors."
            },
            {
                "question": "Why is the word 'AMBULANCE' printed in reverse lettering on the front of emergency hospital vehicles?",
                "options": [
                    "A. It is a traditional code from ancient printing presses",
                    "B. So that drivers ahead see it right-side around through their rear-view mirrors due to lateral inversion",
                    "C. To prevent pedestrians from reading it",
                    "D. It saves paint during manufacturing"
                ],
                "correct": 1,
                "explanation": "The rear-view mirror laterally inverts the reversed lettering so the leading driver reads 'AMBULANCE' correctly and yields the right-of-way."
            }
        ]
    },
    {
        "id": 5,
        "tag": "Applied Optics",
        "title": "Concave Mirror Practical Uses",
        "sim_id": "concave_uses_sim",
        "avatar_dialogue": "Concave mirrors are optical marvels! In vehicle headlights, they turn a tiny bulb into a powerful straight beam. In dental clinics, they give dentists a razor-sharp, magnified view of tiny teeth.",
        "vocabulary": [
            {"word": "Headlight Reflector", "definition": "A concave parabolic mirror placed behind a bulb to project light into a parallel, concentrated forward beam."},
            {"word": "Dental Mirror", "definition": "A small concave mirror on a slender handle used by dentists to produce an erect, enlarged view of teeth and gums."},
            {"word": "Reflecting Telescope", "definition": "An astronomical telescope (such as the Isaac Newton design) using a large concave mirror to gather and focus starlight."}
        ],
        "theory": r"""
          <p>Because concave mirrors can both magnify nearby objects and collimate or converge light rays, they serve indispensable practical roles:</p>
          <ul>
            <li><strong>Torches and Vehicle Headlights:</strong> The light bulb is positioned at the mirror's focus point. The concave reflector captures diverging light rays emitted by the bulb and reflects them forward as a <strong>powerful, parallel beam</strong> that illuminates distant roads.</li>
            <li><strong>Dental and Shaving Mirrors:</strong> When held close to the face or mouth, the concave mirror produces an <strong>erect, enlarged (magnified) image</strong>, enabling dentists to detect microscopic cavities and barbers to see fine facial hair.</li>
            <li><strong>Reflecting Astronomical Telescopes:</strong> Huge primary concave mirrors (often several meters in diameter) collect faint parallel light rays from distant stars and galaxies, converging them to a bright focal point to reveal deep-space wonders without chromatic aberration.</li>
          </ul>
        """,
        "checkpoints": [
            {
                "question": "Where is the filament bulb positioned in a vehicle headlight reflector to produce a powerful parallel beam of light?",
                "options": [
                    "A. Behind the mirror casing",
                    "B. At the focal point of the concave mirror reflector",
                    "C. Several meters in front of the vehicle hood",
                    "D. Underneath the wheels"
                ],
                "correct": 1,
                "explanation": "Placing the bulb at the focus of a concave reflector causes all reflected rays to emerge parallel to each other, forming a penetrating forward beam."
            },
            {
                "question": "Why do dental practitioners use concave mirrors during dental examinations?",
                "options": [
                    "A. To make teeth appear smaller and darker",
                    "B. To form an erect and enlarged (magnified) image of teeth",
                    "C. To heat up dental fillings with focused sunlight",
                    "D. To invert the patient's face upside down"
                ],
                "correct": 1,
                "explanation": "When held close to a tooth, a concave mirror forms an erect, magnified virtual image that reveals fine details."
            }
        ]
    },
    {
        "id": 6,
        "tag": "Road & Store Safety",
        "title": "Surveillance & Safety Mirrors",
        "sim_id": "convex_safety_mirrors_sim",
        "avatar_dialogue": "Driving around a sharp mountain hairpin bend? Look up at the giant round mirror on the pole! Convex mirrors reveal oncoming vehicles around blind corners, preventing deadly collisions.",
        "vocabulary": [
            {"word": "Blind Corner Mirror", "definition": "A large outdoor convex mirror mounted at sharp road intersections, hairpins, and driveways to reveal unseen oncoming traffic."},
            {"word": "Surveillance Mirror", "definition": "A ceiling- or wall-mounted convex mirror in retail stores and banks that allows staff to monitor broad floor aisles and deter theft."},
            {"word": "Divergent Panoramic View", "definition": "The expansive viewing angle created by an outward curved mirror reflecting rays from wide peripheral angles."}
        ],
        "theory": r"""
          <p>Convex mirrors provide unparalleled situational awareness in public safety and surveillance:</p>
          <ul>
            <li><strong>Blind Mountain Corners & Intersections:</strong>
              <ul>
                <li>At hairpin bends in hilly terrains or narrow parking garage exits, drivers cannot see around the corner.</li>
                <li>A weatherproof convex mirror mounted high at the intersection reflects light from both crossing roadways, presenting an <strong>erect, wide-angle image</strong> of approaching vehicles and preventing head-on collisions.</li>
              </ul>
            </li>
            <li><strong>Store and Supermarket Surveillance:</strong>
              <ul>
                <li>Large retail department stores and metro stations install convex mirrors near ceiling corners.</li>
                <li>A single convex mirror enables store managers or security personnel to observe entire aisles and checkout lines from a single vantage point, deterring shoplifting.</li>
              </ul>
            </li>
          </ul>
        """,
        "checkpoints": [
            {
                "question": "Why are convex mirrors installed at sharp road bends and hidden parking garage exits?",
                "options": [
                    "A. To magnify the license plates of cars",
                    "B. To provide a wide panoramic view of oncoming traffic around blind corners and prevent accidents",
                    "C. To burn dry fallen leaves with focused sunlight",
                    "D. To project headlight beams into the sky"
                ],
                "correct": 1,
                "explanation": "The bulging geometry of convex mirrors provides an expansive field of view, revealing oncoming vehicles hidden by blind corners."
            },
            {
                "question": "What optical feature allows a store manager to monitor entire store aisles using a ceiling-mounted convex mirror?",
                "options": [
                    "A. It inverts images upside down",
                    "B. It forms an erect, compact (diminished) image covering a vastly wider field of view than a plane mirror",
                    "C. It shines laser beams onto shoppers",
                    "D. It works only in total darkness"
                ],
                "correct": 1,
                "explanation": "Convex mirrors squeeze a wide viewing angle into a compact, erect reflection, enabling panoramic surveillance."
            }
        ]
    },
    {
        "id": 7,
        "tag": "Fundamental Laws",
        "title": "The Laws of Reflection",
        "sim_id": "laws_of_reflection_sim",
        "avatar_dialogue": "Whenever light bounces, it obeys strict geometric laws! The angle of incidence equals the angle of reflection, and both rays lie in the exact same plane as the normal line.",
        "vocabulary": [
            {"word": "Incident Ray", "definition": "The light ray traveling toward and striking the reflecting mirror surface."},
            {"word": "Reflected Ray", "definition": "The light ray that bounces off and travels away from the mirror surface."},
            {"word": "Normal", "definition": "An imaginary line drawn perpendicular (at exactly 90°) to the mirror surface at the point of incidence."},
            {"word": "Angle of Incidence (i)", "definition": "The angle between the incident ray and the normal line: $\\angle i$."},
            {"word": "Angle of Reflection (r)", "definition": "The angle between the reflected ray and the normal line: $\\angle r$."}
        ],
        "theory": r"""
          <p>Reflection of light is governed by two fundamental, immutable physical laws:</p>
          <div style="background: rgba(14, 165, 233, 0.1); border-left: 3px solid #38bdf8; padding: 0.6rem 0.85rem; border-radius: 4px; margin-bottom: 0.75rem;">
            <strong>The Two Universal Laws of Reflection:</strong>
            <ol style="margin-top: 0.35rem; padding-left: 1.2rem;">
              <li><strong>Law of Equal Angles:</strong> The angle of incidence is always equal to the angle of reflection:
                $$\angle i = \angle r$$
              </li>
              <li><strong>Coplanar Law:</strong> The incident ray, the normal drawn at the point of incidence, and the reflected ray all lie in the <strong>same geometric plane</strong>.</li>
            </ol>
          </div>
          <ul>
            <li><strong>Universal Validity:</strong> These laws hold true for <strong>all types of reflecting surfaces</strong>—including flat plane mirrors, concave spherical mirrors, convex spherical mirrors, and rough surfaces!</li>
            <li><strong>On Curved Surfaces:</strong> The normal at any point on a spherical mirror is simply the radius line connecting that point directly to the sphere's center of curvature ($C$).</li>
          </ul>
        """,
        "checkpoints": [
            {
                "question": "A light ray strikes a reflective mirror surface at an angle of 35° to the normal line. What is its angle of reflection?",
                "options": [
                    "A. 17.5°",
                    "B. 35°",
                    "C. 55°",
                    "D. 70°"
                ],
                "correct": 1,
                "explanation": "According to the First Law of Reflection, the angle of reflection equals the angle of incidence (∠i = ∠r = 35°)."
            },
            {
                "question": "Do the Laws of Reflection apply to curved spherical mirrors (concave and convex) or only to flat plane mirrors?",
                "options": [
                    "A. Only to flat plane mirrors",
                    "B. To all types of mirrors, both plane and spherical",
                    "C. Only to lenses in eyeglasses",
                    "D. Only in outer space"
                ],
                "correct": 1,
                "explanation": "The Laws of Reflection are universal physical laws that apply to all reflecting surfaces, including flat and curved spherical mirrors."
            }
        ]
    },
    {
        "id": 8,
        "tag": "Ray Behaviors",
        "title": "Parallel Beams on Mirrors",
        "sim_id": "parallel_beams_mirrors_sim",
        "avatar_dialogue": "Shine a laser rake of parallel beams at three mirrors: on a plane mirror they stay parallel, on a concave mirror they converge together, and on a convex mirror they diverge outwards!",
        "vocabulary": [
            {"word": "Parallel Light Beam", "definition": "A bundle of light rays traveling alongside each other in the same direction without converging or diverging."},
            {"word": "Converging Rays", "definition": "Light rays that get closer together as they travel and intersect at a common point (Focus)."},
            {"word": "Diverging Rays", "definition": "Light rays that spread apart and travel away from each other after reflection or refraction."},
            {"word": "Principal Focus (F)", "definition": "The focal point on the principal axis where rays parallel to the axis converge after reflecting from a concave mirror."}
        ],
        "theory": r"""
          <p>When multiple parallel beams of light strike different mirror geometries, their reflections follow distinct trajectories:</p>
          <ul>
            <li><strong>Plane Mirror:</strong>
              <ul>
                <li>Every point on the flat mirror has parallel normals.</li>
                <li>Reflected beams bounce off at identical angles, remaining <strong>strictly parallel</strong> to one another.</li>
              </ul>
            </li>
            <li><strong>Concave Mirror (Converging Mirror):</strong>
              <ul>
                <li>Because the mirror curves inwards, normals tilt toward the central principal axis.</li>
                <li>Reflected beams get closer together and <strong>converge</strong>, meeting at a single bright, sharp spot known as the <strong>principal focus ($F$)</strong>.</li>
              </ul>
            </li>
            <li><strong>Convex Mirror (Diverging Mirror):</strong>
              <ul>
                <li>Because the mirror curves outwards, normals point away from the central axis.</li>
                <li>Reflected beams spread apart and <strong>diverge</strong>, appearing to originate from an imaginary focal point hidden behind the mirror.</li>
              </ul>
            </li>
          </ul>
        """,
        "checkpoints": [
            {
                "question": "What happens to a set of parallel light beams after reflecting from a concave mirror?",
                "options": [
                    "A. They remain parallel",
                    "B. They converge (come closer together to meet at a focus point)",
                    "C. They spread out and diverge",
                    "D. They turn into sound waves"
                ],
                "correct": 1,
                "explanation": "A concave mirror is a converging mirror; it bends parallel incoming rays inward toward a common focal point."
            },
            {
                "question": "Why is a convex mirror called a diverging mirror?",
                "options": [
                    "A. Because it focuses light into a burning hot spot",
                    "B. Because it causes parallel incoming light rays to spread apart (diverge) after reflection",
                    "C. Because it stops light from traveling",
                    "D. Because it absorbs all light without reflecting"
                ],
                "correct": 1,
                "explanation": "The outward curvature of a convex mirror reflects parallel rays outward away from each other (divergence)."
            }
        ]
    },
    {
        "id": 9,
        "tag": "Solar Technology",
        "title": "Solar Concentrators & Furnaces",
        "sim_id": "solar_concentrator_sim",
        "avatar_dialogue": "Sunlight carrying energy across 150 million kilometers can be concentrated by a concave mirror onto a single spot, generating temperatures hot enough to boil water, cook food, or melt steel!",
        "vocabulary": [
            {"word": "Solar Concentrator", "definition": "An optical device using large concave or parabolic mirrors to focus incoming solar radiation onto a small receiver area."},
            {"word": "Solar Furnace", "definition": "An industrial facility using an array of concave mirrors to produce extreme temperatures (over 3,000°C) for metallurgical smelting and clean electricity."},
            {"word": "Thermal Focal Spot", "definition": "The concentrated focal point where immense radiant thermal energy ignites combustible materials or boils liquids into steam."}
        ],
        "theory": r"""
          <p>The converging power of concave mirrors is harnessed in renewable solar thermal engineering:</p>
          <ul>
            <li><strong>Solar Cookers & Water Heaters:</strong>
              <ul>
                <li>A parabolic concave dish gathers sunlight falling over its wide surface area and concentrates it onto a cooking pot placed at the focal point.</li>
                <li>Water boils and food cooks quickly with zero wood, coal, or gas fuel emissions!</li>
              </ul>
            </li>
            <li><strong>Solar Steam Power Plants:</strong>
              <ul>
                <li>Curved concave parabolic troughs track the sun and focus solar energy onto central fluid pipes.</li>
                <li>The fluid heats to several hundred degrees Celsius, boiling water into high-pressure steam that drives turbine generators to produce clean electricity.</li>
              </ul>
            </li>
            <li><strong>Ultra-High Temperature Solar Furnaces:</strong>
              <ul>
                <li>Industrial solar furnaces (such as the Odeillo solar furnace in France or India's solar research centers) concentrate sunlight by thousands of times, exceeding $3,000^\circ\text{C}$ to melt iron and steel without carbon pollution.</li>
              </ul>
            </li>
          </ul>
        """,
        "checkpoints": [
            {
                "question": "What type of mirror is utilized in solar cookers to concentrate sunlight onto the cooking pot?",
                "options": [
                    "A. Convex mirror",
                    "B. Concave mirror",
                    "C. Plane mirror with frosted glass",
                    "D. Diverging lens"
                ],
                "correct": 1,
                "explanation": "A concave mirror converges parallel rays of sunlight to a single focal point, generating intense cooking heat."
            },
            {
                "question": "What environmental and technological benefit is provided by industrial solar furnaces using concave mirror arrays?",
                "options": [
                    "A. They generate extreme heat (>3,000°C) to melt metals and generate power without burning fossil fuels",
                    "B. They create artificial rainfall inside factories",
                    "C. They cool metal into ice blocks",
                    "D. They operate only on cloudy nights"
                ],
                "correct": 0,
                "explanation": "Solar furnaces concentrate clean solar radiation to reach thousands of degrees Celsius, enabling metallurgical smelting with zero carbon emissions."
            }
        ]
    },
    {
        "id": 10,
        "tag": "Lens Basics",
        "title": "Introduction to Lenses",
        "sim_id": "lens_basics_sim",
        "avatar_dialogue": "Unlike mirrors that bounce light backward, lenses are transparent pieces of glass or plastic that allow light to pass right through, bending rays via refraction to sharpen human vision.",
        "vocabulary": [
            {"word": "Lens", "definition": "A piece of transparent material (glass or optical plastic) bounded by two surfaces, at least one of which is curved, that refracts light."},
            {"word": "Refraction", "definition": "The bending of a light ray as it passes from one transparent medium (like air) into another (like glass) of different optical density."},
            {"word": "Convex Lens", "definition": "A lens that is thicker in the middle than at the edges; it converges light rays (converging lens)."},
            {"word": "Concave Lens", "definition": "A lens that is thicker at the edges than in the middle; it diverges light rays (diverging lens)."}
        ],
        "theory": r"""
          <p><strong>Lenses</strong> are fundamental optical tools found everywhere from reading glasses to giant observatory telescopes:</p>
          <ul>
            <li><strong>Mirrors vs. Lenses:</strong>
              <ul>
                <li><strong>Mirrors:</strong> Opaque, polished surfaces that form images by <em>reflection</em> (bouncing light off).</li>
                <li><strong>Lenses:</strong> Transparent media that form images by <em>refraction</em> (bending light as it travels through).</li>
              </ul>
            </li>
            <li><strong>The Two Primary Types:</strong>
              <ul>
                <li><strong>Convex Lens (Converging):</strong> Bulges outward in the center. It is thicker at the middle and thinner at the perimeter edges. It converges light rays passing through it.</li>
                <li><strong>Concave Lens (Diverging):</strong> Curves inward in the center. It is thinner at the middle and thicker at the perimeter edges. It diverges light rays passing through it.</li>
              </ul>
            </li>
          </ul>
        """,
        "checkpoints": [
            {
                "question": "How can you physically distinguish a convex lens from a concave lens simply by touching their surfaces?",
                "options": [
                    "A. A convex lens is thicker at the middle; a concave lens is thicker at the edges",
                    "B. A convex lens is completely flat; a concave lens is shaped like a cube",
                    "C. A convex lens is made of wood; a concave lens is made of metal",
                    "D. Both have identical thicknesses across all points"
                ],
                "correct": 0,
                "explanation": "A convex lens bulges out and is thicker at the center than at the edges; a concave lens caves in and is thicker at the edges."
            },
            {
                "question": "What is the primary physical process by which lenses form images of objects?",
                "options": [
                    "A. Magnetic attraction",
                    "B. Refraction (bending of light passing through transparent material)",
                    "C. Surface reflection like a metal mirror",
                    "D. Nuclear fusion"
                ],
                "correct": 1,
                "explanation": "Lenses are transparent optical components that transmit and bend light rays through refraction."
            }
        ]
    },
    {
        "id": 11,
        "tag": "Converging Optics",
        "title": "Convex Converging Lenses",
        "sim_id": "convex_lens_converging_sim",
        "avatar_dialogue": "Watch parallel light rays enter a convex lens: the curved glass bends every ray inward, bringing them together at a single point called the principal focus!",
        "vocabulary": [
            {"word": "Converging Lens", "definition": "Another name for a convex lens, because it brings parallel incoming light rays closer together."},
            {"word": "Principal Axis", "definition": "The straight imaginary line passing through the optical center and centers of curvature of both curved surfaces of a lens."},
            {"word": "Optical Center (O)", "definition": "The central geometric point of a lens through which light rays pass without undergoing any angular deviation."},
            {"word": "Focal Length (f)", "definition": "The distance between the optical center of the lens and its principal focus ($F$)."}
        ],
        "theory": r"""
          <p>A <strong>convex lens</strong> acts as a light gatherer and concentrator:</p>
          <ul>
            <li><strong>Ray Refraction Pattern:</strong>
              <ul>
                <li>When parallel beams of sunlight strike the front surface of a convex lens, rays passing through the top and bottom sections bend toward the thicker middle region.</li>
                <li>Upon exiting the glass, all parallel rays intersect at a single real focal point on the other side of the lens: the <strong>principal focus ($F$)</strong>.</li>
              </ul>
            </li>
            <li><strong>Magnifying Glass Effect:</strong>
              <ul>
                <li>If you hold a convex lens in the sun and place a dry leaf or paper at its focal spot, the concentrated radiant solar energy can ignite the paper into smoke and flames!</li>
              </ul>
            </li>
            <li><strong>Dual Foci:</strong> Because light can pass through a lens from either the left or the right side, every lens has two symmetrical focal points ($F_1$ and $F_2$).</li>
          </ul>
        """,
        "checkpoints": [
            {
                "question": "Why is a convex lens classified as a converging lens?",
                "options": [
                    "A. Because it bends parallel incoming rays inwards to meet at a focus point",
                    "B. Because it causes rays to diverge apart into the sky",
                    "C. Because it reflects all rays back toward the sun",
                    "D. Because it absorbs all light and produces darkness"
                ],
                "correct": 0,
                "explanation": "A convex lens bends parallel rays inward toward its thicker central axis, converging them at a focal point."
            },
            {
                "question": "What happens if you focus the sunlight through a magnifying glass (convex lens) onto a small piece of dry paper for several minutes?",
                "options": [
                    "A. The paper freezes into solid ice",
                    "B. The concentrated solar energy heats the focal spot and can cause the paper to char or ignite",
                    "C. The paper turns into transparent glass",
                    "D. The paper becomes magnetic"
                ],
                "correct": 1,
                "explanation": "A convex lens concentrates solar radiation onto a pinpoint focus, concentrating enough heat energy to ignite dry paper."
            }
        ]
    },
    {
        "id": 12,
        "tag": "Diverging Optics",
        "title": "Concave Diverging Lenses",
        "sim_id": "concave_lens_diverging_sim",
        "avatar_dialogue": "Now look at a concave lens: thin in the center and thick at the edges. When parallel beams pass through, they spread outward, diverging like a flashlight beam in fog.",
        "vocabulary": [
            {"word": "Diverging Lens", "definition": "Another name for a concave lens, because it causes parallel incoming light rays to spread apart (diverge)."},
            {"word": "Virtual Focus", "definition": "The focal point from which diverging rays appear to emerge when traced backward along imaginary dashed lines."},
            {"word": "Myopia Correction", "definition": "The use of concave lenses in eyeglasses to diverge light rays slightly before entering the eye, correcting near-sightedness."}
        ],
        "theory": r"""
          <p>A <strong>concave lens</strong> behaves in the exact opposite manner to a convex lens:</p>
          <ul>
            <li><strong>Ray Refraction Pattern:</strong>
              <ul>
                <li>When parallel beams of light enter a concave lens, they bend toward the thicker outer rims.</li>
                <li>Upon exiting, the rays <strong>diverge (spread apart)</strong> and never meet on the far side of the lens.</li>
              </ul>
            </li>
            <li><strong>Virtual Focal Point:</strong>
              <ul>
                <li>If you trace these spreading rays backward as straight dashed lines, they appear to emanate from a single point located on the incident side of the lens.</li>
                <li>This is called a <strong>virtual focus</strong>, because light rays do not actually intersect there in physical reality.</li>
              </ul>
            </li>
            <li><strong>Correction of Near-Sightedness (Myopia):</strong>
              <ul>
                <li>Students who cannot clearly see the school blackboard suffer from myopia. Concave lenses in their spectacles diverge incoming light slightly, allowing the eye's natural lens to focus the image crisply on the retina!</li>
              </ul>
            </li>
          </ul>
        """,
        "checkpoints": [
            {
                "question": "What behavior do parallel light rays exhibit after passing through a concave lens?",
                "options": [
                    "A. They come together and intersect at a bright focal point",
                    "B. They spread apart (diverge) away from each other",
                    "C. They bounce straight backward into the flashlight",
                    "D. They turn into radio waves"
                ],
                "correct": 1,
                "explanation": "A concave lens is a diverging lens; its geometry bends light rays outward away from the central axis."
            },
            {
                "question": "Which type of lens is prescribed in eyeglasses to correct myopia (near-sightedness)?",
                "options": [
                    "A. Concave lens",
                    "B. Convex lens",
                    "C. Flat mirror",
                    "D. Shaded sunglasses only"
                ],
                "correct": 0,
                "explanation": "Concave lenses diverge incoming light rays slightly, allowing near-sighted eyes to focus distant objects accurately onto the retina."
            }
        ]
    },
    {
        "id": 13,
        "tag": "Convex Imaging",
        "title": "Convex Lens Image Dynamics",
        "sim_id": "convex_lens_imaging_sim",
        "avatar_dialogue": "Hold a magnifying glass close to printed text: the letters look enormous and upright! Move it toward the window, and you can project an upside-down image of trees onto a white sheet of paper!",
        "vocabulary": [
            {"word": "Magnifying Glass", "definition": "A convex lens used at close distance to produce an erect, enlarged virtual image of tiny objects."},
            {"word": "Real Image", "definition": "An image formed by the actual intersection of light rays, which can be captured and projected onto a screen."},
            {"word": "Virtual Image", "definition": "An image formed where rays only appear to diverge from, which cannot be captured on a physical screen."}
        ],
        "theory": r"""
          <p>The image characteristics of a <strong>convex lens</strong> change dramatically based on the distance between the object and the lens:</p>
          <ul>
            <li><strong>Object Placed Close to the Lens (Inside Focus $F$):</strong>
              <ul>
                <li>The image appears <strong>erect (upright)</strong> and <strong>enlarged (magnified)</strong> on the same side as the object.</li>
                <li>This is how a standard hand magnifying glass functions when reading fine book print or inspecting insect wings.</li>
              </ul>
            </li>
            <li><strong>Object Moved Farther Away (Beyond Focus $F$):</strong>
              <ul>
                <li>The image immediately flips into an <strong>inverted (upside-down)</strong> image.</li>
                <li>Because light rays physically pass through and intersect, this is a <strong>real image</strong> that can be projected onto a paper screen or digital camera sensor!</li>
                <li>At intermediate distances, the image is inverted and enlarged; at large distances, it becomes inverted and <strong>diminished (smaller than the object)</strong>.</li>
              </ul>
            </li>
          </ul>
        """,
        "checkpoints": [
            {
                "question": "When reading fine text using a handheld magnifying glass (convex lens) close to the page, what are the image characteristics?",
                "options": [
                    "A. Inverted and diminished",
                    "B. Erect and enlarged (magnified)",
                    "C. Inverted and blurred completely black",
                    "D. No image is formed"
                ],
                "correct": 1,
                "explanation": "When the object is within the focal distance of a convex lens, it forms an erect, magnified virtual image."
            },
            {
                "question": "Can a real image formed by a convex lens when looking at a distant illuminated window be captured onto a piece of white paper?",
                "options": [
                    "A. No, lenses cannot form real images",
                    "B. Yes, real images are formed by intersecting light rays and can be projected onto a screen",
                    "C. Only if the paper is painted black",
                    "D. Only in outer space"
                ],
                "correct": 1,
                "explanation": "Beyond the focal point, a convex lens produces a real, inverted image that can be projected directly onto a screen."
            }
        ]
    },
    {
        "id": 14,
        "tag": "Concave Imaging",
        "title": "Concave Lens Image Dynamics",
        "sim_id": "concave_lens_imaging_sim",
        "avatar_dialogue": "Look through a concave lens at any room object: no matter how near or far you move, the view is always right-side up and distinctly smaller! That is why hotel peepholes use concave lenses.",
        "vocabulary": [
            {"word": "Door Peephole", "definition": "A wide-angle optical peephole installed in front doors using a concave lens to show a miniature erect view of visitors outside."},
            {"word": "Invariant Erect Image", "definition": "The property of concave lenses always forming right-side-up images regardless of object position."},
            {"word": "Always Virtual", "definition": "The image formed by a concave lens cannot be captured on a screen because the refracted rays diverge physically."}
        ],
        "theory": r"""
          <p>In stark contrast to the multi-state convex lens, a <strong>concave lens</strong> behaves with absolute geometric uniformity:</p>
          <ul>
            <li><strong>Invariant Image Characteristics:</strong>
              <ul>
                <li>An object viewed through a concave lens <strong>always appears erect (upright)</strong>.</li>
                <li>The image is <strong>always diminished (smaller in size than the actual object)</strong>.</li>
                <li>The image is <strong>always virtual</strong>; it cannot be projected onto a physical screen.</li>
              </ul>
            </li>
            <li><strong>Why Concave Lenses Are Used in Door Peepholes:</strong>
              <ul>
                <li>Because the image is diminished and formed by diverging rays, a concave lens captures a vast, panoramic field of view outside the door.</li>
                <li>A homeowner standing inside can see a visitor from head to toe in an upright, compact view while remaining completely invisible from the outside!</li>
              </ul>
            </li>
          </ul>
        """,
        "checkpoints": [
            {
                "question": "What type of image is always formed when an object is viewed through a concave lens?",
                "options": [
                    "A. Inverted and enlarged",
                    "B. Erect and diminished (smaller than the object)",
                    "C. Inverted and diminished",
                    "D. Erect and five times larger"
                ],
                "correct": 1,
                "explanation": "A concave lens always forms an erect, diminished virtual image, regardless of the object's distance."
            },
            {
                "question": "Can the image formed by a concave lens ever be projected onto a white wall or screen?",
                "options": [
                    "A. Yes, at any distance",
                    "B. No, because the image is virtual and refracted rays diverge away from each other",
                    "C. Yes, but only in bright sunlight",
                    "D. Only if the screen is made of glass"
                ],
                "correct": 1,
                "explanation": "Concave lenses form virtual images through diverging rays that cannot physically intersect on a screen."
            }
        ]
    },
    {
        "id": 15,
        "tag": "Optical Technology",
        "title": "Optical Instruments & The Eye",
        "sim_id": "eye_optical_instruments_sim",
        "avatar_dialogue": "Did you know you carry living convex lenses inside your own head? The human eye contains a natural flexible convex lens that focuses living light directly onto your retina!",
        "vocabulary": [
            {"word": "Crystalline Eye Lens", "definition": "A flexible, living convex lens in the human eye composed of transparent proteins that adjusts its focal length to focus near and far objects."},
            {"word": "Retina", "definition": "The light-sensitive sensory layer at the back of the eyeball where real, inverted optical images are focused."},
            {"word": "Compound Microscope", "definition": "An optical device utilizing two convex lenses (objective and eyepiece) to achieve high magnification of microscopic cells."},
            {"word": "Refracting Telescope", "definition": "An astronomical instrument using a large convex objective lens to collect light and an eyepiece to view distant celestial bodies."}
        ],
        "theory": r"""
          <p>Lenses form the core foundation of vision biology and modern scientific instrumentation:</p>
          <ul>
            <li><strong>The Human Eye:</strong>
              <ul>
                <li>Contains a natural, transparent <strong>flexible convex lens</strong> held by ciliary muscles.</li>
                <li>Light enters through the cornea and pupil, passes through the convex lens, and focuses a real, inverted image onto the <strong>retina</strong>.</li>
                <li>The optic nerve transmits electrical impulses to the brain, which automatically flips the perception upright!</li>
              </ul>
            </li>
            <li><strong>Compound Microscopes:</strong>
              <ul>
                <li>Employs an <em>objective convex lens</em> close to the slide to create an enlarged real image, and an <em>eyepiece convex lens</em> to magnify that image further, revealing bacteria and plant cells!</li>
              </ul>
            </li>
            <li><strong>Telescopes & Cameras:</strong>
              <ul>
                <li>Cameras use multi-element convex lens systems to project sharp images onto digital image sensors, recording precious moments in high resolution.</li>
              </ul>
            </li>
          </ul>
        """,
        "checkpoints": [
            {
                "question": "What type of lens is naturally present inside the human eye to focus light onto the retina?",
                "options": [
                    "A. A flat glass mirror",
                    "B. A flexible convex lens",
                    "C. A rigid concave lens",
                    "D. A prism"
                ],
                "correct": 1,
                "explanation": "The human eye contains a natural, flexible biconvex lens that adjusts curvature to focus light from near and far objects."
            },
            {
                "question": "Which combination of optical components is utilized in high-magnification compound laboratory microscopes?",
                "options": [
                    "A. Two convex lenses (objective and eyepiece)",
                    "B. Two flat plane mirrors only",
                    "C. Two concave lenses that shrink the cells",
                    "D. Wood and paper tubes"
                ],
                "correct": 0,
                "explanation": "Compound microscopes combine a convex objective lens and a convex eyepiece lens to produce compound magnification of cellular specimens."
            }
        ]
    },
    {
        "id": 16,
        "tag": "Indian Scientific Heritage",
        "title": "Bhāskara II & Ancient Astronomy",
        "sim_id": "bhaskara_water_optics_sim",
        "avatar_dialogue": "Over 800 years ago in medieval India, the great mathematician-astronomer Bhāskara II used shallow bowls of water and sighting tubes to measure star positions using reflected light!",
        "vocabulary": [
            {"word": "Bhāskara II (Bhāskarācārya)", "definition": "Celebrated 12th-century Indian mathematician and astronomer (1114–1185 CE), author of the legendary treatise Siddhānta Śiromaṇi."},
            {"word": "Water Basin Reflection", "definition": "The ancient astronomical method of using a calm, shallow bowl of water as an optically flat, horizontal liquid mirror to observe celestial bodies."},
            {"word": "Nālikā Yantra", "definition": "A calibrated hollow observation sighting tube used by Indian astronomers to align celestial angles and track stars."},
            {"word": "Siddhānta Śiromaṇi", "definition": "Bhāskara II's masterpiece text covering arithmetic (Līlāvatī), algebra (Bījagaṇita), and planetary astronomical mechanics."}
        ],
        "theory": r"""
          <p>India possesses a glorious scientific heritage in observational optics and celestial mechanics:</p>
          <ul>
            <li><strong>Bhāskara II (1114–1185 CE):</strong> One of the greatest mathematical geniuses in human history, serving as head of the astronomical observatory at Ujjain. In his monumental work <em>Siddhānta Śiromaṇi</em>, he detailed sophisticated observational astronomy.</li>
            <li><strong>Water as an Optically Flat Liquid Mirror:</strong>
              <ul>
                <li>Over 800 years ago, ancient Indian astronomers filled wide, shallow dark stone or bronze basins with calm water.</li>
                <li>Earth's gravity levels a still water surface into an <strong>optically flat plane mirror</strong> that reflects the nocturnal sky with remarkable clarity.</li>
                <li>By observing the reflected coordinates of stars and planets in water basins using calibrated sighting tubes (<em>Nālikā Yantras</em>), astronomers measured celestial altitudes and planetary orbits with extraordinary accuracy!</li>
              </ul>
            </li>
          </ul>
        """,
        "checkpoints": [
            {
                "question": "How did Indian astronomers during the era of Bhāskara II utilize shallow bowls of calm water in astronomy over 800 years ago?",
                "options": [
                    "A. To boil drinking tea during night shifts",
                    "B. As flat liquid reflecting mirrors to observe and measure celestial coordinates of stars and planets",
                    "C. To wash metallic telescopes",
                    "D. To produce steam for flying air balloons"
                ],
                "correct": 1,
                "explanation": "Shallow water basins provided an optically level liquid mirror reflecting celestial bodies for precise angular measurement."
            },
            {
                "question": "Which celebrated 12th-century Indian mathematical treatise was authored by the astronomer Bhāskara II?",
                "options": [
                    "A. Siddhānta Śiromaṇi (including Līlāvatī and Bījagaṇita)",
                    "B. Principia Mathematica",
                    "C. Opticks",
                    "D. Elements of Geometry"
                ],
                "correct": 0,
                "explanation": "Bhāskara II authored the Siddhānta Śiromaṇi, featuring the famous sections Līlāvatī and Bījagaṇita."
            }
        ]
    },
    {
        "id": 17,
        "is_quiz_slide": True,
        "quiz_start_idx": 1,
        "quiz_count": 10,
        "title": "Mastery Challenge • Part I",
        "tag": "Mastery Quiz",
        "avatar_dialogue": "Welcome to Mastery Challenge Part I! Test your mastery of spherical mirrors, concave vs convex geometries, and lateral inversion."
    },
    {
        "id": 18,
        "is_quiz_slide": True,
        "quiz_start_idx": 11,
        "quiz_count": 10,
        "title": "Mastery Challenge • Part II",
        "tag": "Mastery Quiz",
        "avatar_dialogue": "Superb progress! Now enter Mastery Challenge Part II, tackling the universal Laws of Reflection, parallel beam behavior, and solar furnaces."
    },
    {
        "id": 19,
        "is_quiz_slide": True,
        "quiz_start_idx": 21,
        "quiz_count": 10,
        "title": "Mastery Challenge • Part III",
        "tag": "Mastery Quiz",
        "avatar_dialogue": "Brilliant momentum! In Mastery Challenge Part III, we explore lenses, converging convex optics, and diverging concave spectacles."
    },
    {
        "id": 20,
        "is_quiz_slide": True,
        "quiz_start_idx": 31,
        "quiz_count": 10,
        "title": "Mastery Challenge • Part IV",
        "tag": "Mastery Quiz",
        "avatar_dialogue": "The final summit! Complete inquiries on image dynamics, the human eye, compound microscopes, and Bhāskara II's heritage astronomy."
    }
]

QUIZ_QUESTIONS = [
    {
        "id": 1,
        "concept": "Spherical Mirror Definition",
        "question": "What is the defining geometric feature of a spherical mirror?",
        "options": [
            "A. Its reflecting surface forms part of an imaginary hollow sphere",
            "B. It is a flat plane of polished wood",
            "C. It is an equilateral triangular glass prism",
            "D. It has zero curvature across its entire area"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Definition:</strong> A spherical mirror is a curved mirror whose reflective surface forms a portion of an imaginary hollow sphere.<br><strong>Step 2: Geometries:</strong> Curving inwards forms a concave mirror; curving outwards forms a convex mirror.<br><strong>Step 3: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 2,
        "concept": "Concave Reflecting Surface",
        "question": "Which part of a shiny stainless steel eating spoon corresponds optically to a concave mirror?",
        "options": [
            "A. The inner curved surface (the bowl where food is scooped)",
            "B. The outer bulging back surface",
            "C. The narrow flat handle tip",
            "D. A spoon does not reflect light"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Spoon Analogy:</strong> The inner scooped-in bowl of a spoon curves inward, functioning optically as a concave mirror.<br><strong>Step 2: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 3,
        "concept": "Convex Reflecting Surface",
        "question": "Which surface of a curved spherical mirror forms a convex mirror?",
        "options": [
            "A. The surface that curves inwards toward the center of curvature",
            "B. The surface that curves outwards away from the center of curvature",
            "C. The shaded non-reflecting backing",
            "D. The flat edge rim"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Convex Geometry:</strong> When the reflecting surface bulges outwards away from the center of the sphere, it is a convex mirror.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 4,
        "concept": "Close Concave Mirror Image",
        "question": "A dentist holds a small concave mirror close to a patient's molar tooth. What kind of image is produced?",
        "options": [
            "A. Inverted and diminished",
            "B. Erect and enlarged (magnified)",
            "C. Inverted and enlarged",
            "D. Completely black"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Position:</strong> When the object is close to a concave mirror (inside focal length), the image formed is virtual, erect, and magnified.<br><strong>Step 2: Practical Utility:</strong> This magnification allows dentists to examine tiny cracks and cavities clearly.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 5,
        "concept": "Distant Concave Mirror Image",
        "question": "What happens to the image of an object in a concave mirror as the object is moved farther and farther away?",
        "options": [
            "A. It remains erect and doubles in size every second",
            "B. It becomes inverted (upside down) and changes from enlarged to diminished (smaller)",
            "C. It disappears and never reflects light again",
            "D. It turns into a convex lens"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Focal Transition:</strong> Beyond the focus, a concave mirror forms an inverted real image.<br><strong>Step 2: Distance Scaling:</strong> At larger distances, the inverted image shrinks and becomes diminished.<br><strong>Step 3: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 6,
        "concept": "Convex Mirror Image Invariance",
        "question": "What are the universal characteristics of the image formed by a convex mirror at any object distance?",
        "options": [
            "A. Always erect and diminished (smaller than the object)",
            "B. Always inverted and enlarged",
            "C. Erect when close, inverted when far",
            "D. Diminished and upside down"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Invariant Optics:</strong> A convex mirror always produces an image that is virtual, erect, and smaller (diminished) than the object, regardless of distance.<br><strong>Step 2: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 7,
        "concept": "Lateral Inversion Occurrence",
        "question": "Lateral inversion (left-right reversal of reflection) can be observed in:",
        "options": [
            "A. Plane mirrors only",
            "B. Concave mirrors only",
            "C. Convex mirrors only",
            "D. Plane, concave, and convex mirrors alike"
        ],
        "correct": 3,
        "solution": r"<p><strong>Step 1: Universal Reflection Rule:</strong> Lateral inversion occurs across all reflecting mirror surfaces—plane, concave, and convex mirrors alike.<br><strong>Step 2: Conclusion:</strong> Option D is correct.</p>"
    },
    {
        "id": 8,
        "concept": "Torch Reflector Optics",
        "question": "Why do electric torches and vehicle headlights feature a concave reflector behind the bulb?",
        "options": [
            "A. To absorb light and save battery energy",
            "B. To reflect light rays originating from the focus into a powerful, straight parallel beam",
            "C. To spread light in all directions into the sky",
            "D. To invert the light beam upside down"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Focus Placement:</strong> When a bulb is located at the focal point of a concave mirror reflector, the reflected rays emerge parallel to each other, creating a high-intensity forward beam.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 9,
        "concept": "Vehicle Side-View Mirrors",
        "question": "Why are convex mirrors universally chosen as rear-view and side-view wing mirrors in cars, trucks, and buses?",
        "options": [
            "A. They make distant vehicles look gigantic",
            "B. They always form an erect image and provide a much wider field of view of trailing traffic",
            "C. They allow the driver to see through the engine",
            "D. They are made of cheap plastic without glass"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Panoramic Coverage:</strong> Convex mirrors curve outwards, capturing light from a broader angle and producing an erect, diminished view of the whole roadway.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 10,
        "concept": "Reflecting Telescopes",
        "question": "What type of optical mirror serves as the primary light-gathering objective in modern reflecting astronomical telescopes?",
        "options": [
            "A. Convex mirror",
            "B. Concave mirror",
            "C. Flat window pane",
            "D. Prismatic lens"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Light Gathering:</strong> A large concave mirror collects faint parallel light from celestial bodies and converges it to a focal point to reveal distant stars.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 11,
        "concept": "Normal Line Definition",
        "question": "What is the 'normal' in the study of light reflection?",
        "options": [
            "A. An ordinary light ray that carries green light",
            "B. An imaginary line drawn perpendicular (at exactly 90°) to the mirror surface at the point of incidence",
            "C. The glass thickness of the mirror frame",
            "D. The horizontal tabletop"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Normal Definition:</strong> The normal is the perpendicular reference line ($90^\circ$) constructed at the point where the incident ray strikes the mirror surface.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 12,
        "concept": "Angle of Incidence",
        "question": "The angle of incidence (i) is measured between:",
        "options": [
            "A. The incident ray and the mirror surface",
            "B. The incident ray and the normal line",
            "C. The incident ray and the reflected ray",
            "D. The reflected ray and the ceiling"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Standard Definition:</strong> The angle of incidence ($\angle i$) is strictly the angle between the incoming incident ray and the normal at the point of incidence.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 13,
        "concept": "First Law of Reflection",
        "question": "If a beam of light strikes a flat mirror such that the angle between the incident ray and the normal is 48°, what is the angle of reflection?",
        "options": [
            "A. 24°",
            "B. 42°",
            "C. 48°",
            "D. 96°"
        ],
        "correct": 2,
        "solution": r"<p><strong>Step 1: Law:</strong> The First Law of Reflection states $\angle i = \angle r$.<br><strong>Step 2: Calculation:</strong> Given $\angle i = 48^\circ$, then $\angle r = 48^\circ$.<br><strong>Step 3: Conclusion:</strong> Option C is correct.</p>"
    },
    {
        "id": 14,
        "concept": "Second Law of Reflection",
        "question": "What is asserted by the Second Law of Reflection regarding the incident ray, normal, and reflected ray?",
        "options": [
            "A. They all travel at different speeds",
            "B. They all lie in the exact same geometric plane",
            "C. They form an equilateral triangle",
            "D. They bend around corners without reflecting"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Coplanar Rule:</strong> The Second Law states that the incident ray, the normal to the mirror at the point of incidence, and the reflected ray all lie in the same plane.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 15,
        "concept": "Parallel Beams on Plane Mirror",
        "question": "When a bundle of multiple parallel light beams falls upon a flat plane mirror, how do the reflected beams behave?",
        "options": [
            "A. They converge to a burning point",
            "B. They remain parallel to one another",
            "C. They spread out in all directions randomly",
            "D. They disappear into the glass"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Regular Reflection:</strong> Because the plane mirror surface is uniformly flat with parallel normals everywhere, equal angles of reflection ensure the reflected beams remain parallel.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 16,
        "concept": "Parallel Beams on Concave Mirror",
        "question": "When parallel light beams strike a concave spherical mirror, the reflected beams:",
        "options": [
            "A. Spread apart and diverge",
            "B. Get closer together and converge at a focal point",
            "C. Remain parallel forever",
            "D. Turn around and reflect backwards into the source"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Inward Normals:</strong> The inward curvature of a concave mirror directs normals toward the principal axis, forcing reflected rays to converge at the principal focus.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 17,
        "concept": "Parallel Beams on Convex Mirror",
        "question": "When parallel light beams strike an outward-curving convex mirror, the reflected beams:",
        "options": [
            "A. Converge to heat up a kettle",
            "B. Spread apart and diverge",
            "C. Meet at a real point in front of the mirror",
            "D. Become completely absorbed"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Outward Curvature:</strong> Normals tilt away from the central axis on a convex mirror, causing reflected rays to diverge outward.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 18,
        "concept": "Solar Furnace Mechanics",
        "question": "How do large solar furnaces achieve extreme temperatures exceeding 3,000°C for melting steel?",
        "options": [
            "A. By burning underground petroleum oil",
            "B. By using vast arrays of concave mirrors to concentrate sunlight onto a small focal area",
            "C. By using flat glass plates that trap humidity",
            "D. By using convex mirrors to disperse light into the sky"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Thermal Concentration:</strong> Large concave/parabolic mirrors collect sunlight over hundreds of square meters and converge it onto a tiny focal spot, concentrating thermal flux to exceed 3,000°C.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 19,
        "concept": "Blind Intersection Safety",
        "question": "A mountain road has a sharp 90-degree blind curve. What device should highway engineers install to prevent collisions?",
        "options": [
            "A. A large concave mirror that inverts approaching trucks",
            "B. A large convex mirror that provides an erect, wide-angle view of oncoming traffic around the corner",
            "C. A sheet of clear window glass",
            "D. A dark black curtain"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Wide View Application:</strong> A convex mirror provides a wide-angle, erect reflection that lets drivers see around blind turns, preventing accidents.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 20,
        "concept": "Supermarket Surveillance",
        "question": "Why do retail store owners mount convex mirrors in store corners rather than flat plane mirrors?",
        "options": [
            "A. Plane mirrors are too heavy to hang",
            "B. Convex mirrors provide an extensive field of view, allowing observation of multiple aisles from a single spot",
            "C. Convex mirrors make merchandise look ten times larger",
            "D. Convex mirrors work without light"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Wide Field Coverage:</strong> The diverging outward curve of convex mirrors captures an expansive panoramic view, allowing surveillance of wide aisles.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 21,
        "concept": "Lens Definition",
        "question": "What is the fundamental optical distinction between a mirror and a lens?",
        "options": [
            "A. A mirror reflects light off an opaque polished surface, while a transparent lens refracts light as it passes through",
            "B. A mirror transmits light; a lens reflects light",
            "C. A mirror is made of water; a lens is made of wood",
            "D. There is no physical difference"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Mechanism:</strong> Mirrors are opaque reflectors (reflection); lenses are transparent refractors that bend light transmitting through them (refraction).<br><strong>Step 2: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 22,
        "concept": "Convex Lens Shape",
        "question": "Which of the following describes the cross-sectional shape of a convex lens?",
        "options": [
            "A. Thicker at the middle compared to its perimeter edges",
            "B. Thicker at the edges compared to its middle",
            "C. Perfectly flat with uniform thickness throughout",
            "D. Hollow with empty air inside"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Convex Geometry:</strong> A convex lens bulges outward, making it thicker at the center than at the outer edges.<br><strong>Step 2: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 23,
        "concept": "Concave Lens Shape",
        "question": "Which of the following describes the cross-sectional shape of a concave lens?",
        "options": [
            "A. Thicker at the middle than at the edges",
            "B. Thicker at the perimeter edges compared to its middle",
            "C. Shaped like a sphere with zero flat boundaries",
            "D. A solid cube of plastic"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Concave Geometry:</strong> A concave lens curves inward, making it thinner at the center and thicker at the perimeter edges.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 24,
        "concept": "Convex Lens Convergence",
        "question": "Why is a convex lens designated as a converging lens?",
        "options": [
            "A. Because it brings parallel light beams together at a focal point",
            "B. Because it scatters light rays into darkness",
            "C. Because it turns light into sound waves",
            "D. Because it reflects light back toward the light source"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Optical Action:</strong> Refraction through the curved surfaces bends parallel rays inward, converging them to intersect at the focal point.<br><strong>Step 2: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 25,
        "concept": "Concave Lens Divergence",
        "question": "Why is a concave lens designated as a diverging lens?",
        "options": [
            "A. Because it focuses light onto a small bright spot",
            "B. Because it causes incoming parallel light beams to spread apart (diverge)",
            "C. Because it magnifies tiny objects by 1,000 times",
            "D. Because it creates a real image on a screen"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Divergence:</strong> Bending toward the thicker perimeter edges causes parallel light rays to spread apart upon exiting a concave lens.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 26,
        "concept": "Magnifying Glass Close Object",
        "question": "When a postage stamp is viewed through a convex lens placed very close to it, how does the stamp appear?",
        "options": [
            "A. Inverted and diminished",
            "B. Erect and enlarged (magnified)",
            "C. Exactly identical in size",
            "D. Upside down and blurred black"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Virtual Magnification:</strong> When an object is within the focal distance of a convex lens, it forms an erect, magnified virtual image.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 27,
        "concept": "Convex Lens Far Object",
        "question": "When a convex lens is used to view a distant outdoor tree, what type of image can be projected onto a sheet of paper behind the lens?",
        "options": [
            "A. An erect, enlarged virtual image",
            "B. An inverted (upside down), diminished real image",
            "C. A completely dark shadow with no details",
            "D. No image can be formed on paper"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Distant Object Imaging:</strong> For distant objects, a convex lens forms an inverted, diminished real image that can be captured on a screen.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 28,
        "concept": "Concave Lens Invariance",
        "question": "What type of image is observed through a concave lens at all object distances?",
        "options": [
            "A. Inverted and magnified",
            "B. Always erect and diminished (smaller)",
            "C. Real and projected onto a wall",
            "D. Upside down and identical in size"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Invariant Concave Optics:</strong> A concave lens consistently produces virtual, erect, and diminished images regardless of object distance.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 29,
        "concept": "Door Peephole Lens",
        "question": "Why is a concave lens used in entrance door security peepholes?",
        "options": [
            "A. It gives an erect, diminished view with a wide field of view, showing a visitor from head to toe",
            "B. It burns visitors with concentrated light",
            "C. It magnifies the visitor's nose to 10 feet wide",
            "D. It inverts the visitor upside down"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Wide Angle:</strong> A concave lens provides an erect, wide-angle diminished view, allowing residents to view visitors from head to toe.<br><strong>Step 2: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 30,
        "concept": "Myopia Glasses",
        "question": "A student struggling to read the school blackboard clearly from the back row is prescribed spectacles. What type of lens do these spectacles contain?",
        "options": [
            "A. Concave lenses to diverge incoming rays and correct myopia (near-sightedness)",
            "B. Convex lenses that magnify nearby books",
            "C. Flat window glass plates",
            "D. Dark sunglasses"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Myopia Correction:</strong> Near-sightedness (myopia) is corrected using concave lenses, which diverge incoming rays so the eye lens focuses them sharply onto the retina.<br><strong>Step 2: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 31,
        "concept": "Human Eye Lens",
        "question": "What kind of lens does the human biological eye naturally contain?",
        "options": [
            "A. A rigid concave lens",
            "B. A flexible, living convex lens",
            "C. A flat plane glass mirror",
            "D. A triangular quartz prism"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Eye Anatomy:</strong> The human eye contains a transparent, flexible biconvex crystalline lens controlled by ciliary muscles.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 32,
        "concept": "Retina Image Formation",
        "question": "What type of optical image is formed by the eye's convex lens on the light-sensitive retina?",
        "options": [
            "A. Virtual, erect, and magnified",
            "B. Real, inverted, and diminished",
            "C. A hollow shadow",
            "D. An electric spark"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Real Image on Retina:</strong> The eye's convex lens forms a real, inverted image on the retina; the brain processes the optic nerve signals to perceive it upright.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 33,
        "concept": "Compound Microscope",
        "question": "How does a compound laboratory microscope achieve extraordinary magnification of biological cells?",
        "options": [
            "A. By combining two convex lenses (an objective lens and an eyepiece lens)",
            "B. By using two flat mirrors",
            "C. By using two concave lenses that shrink the specimen",
            "D. By heating the slide with fire"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Dual Convex System:</strong> A compound microscope uses a convex objective to produce an enlarged real image, and a convex eyepiece to magnify that image further into a virtual image.<br><strong>Step 2: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 34,
        "concept": "Camera Optics",
        "question": "Which optical component inside a photographic camera focuses incoming light rays onto the digital sensor?",
        "options": [
            "A. A convex lens system",
            "B. A flat wooden board",
            "C. A concave mirror that scatters light",
            "D. A magnet"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Camera Mechanism:</strong> Cameras use convex lens groups to converge light rays into sharp real images on the digital CMOS/CCD sensor.<br><strong>Step 2: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 35,
        "concept": "Bhāskara II Time Period",
        "question": "Approximately when did the celebrated Indian mathematician and astronomer Bhāskara II live and conduct astronomical research?",
        "options": [
            "A. Over 800 years ago (12th century CE)",
            "B. 50 years ago (20th century CE)",
            "C. 5,000 years ago (Stone Age)",
            "D. In 1999 CE"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Historical Timeline:</strong> Bhāskara II (Bhāskarācārya) lived from 1114 to 1185 CE, over 800 years ago during the 12th century.<br><strong>Step 2: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 36,
        "concept": "Water Basin Optical Function",
        "question": "In ancient Indian astronomy, why was a shallow bowl of still water utilized to observe celestial stars?",
        "options": [
            "A. Calm water forms an optically level plane mirror reflecting celestial light",
            "B. Water cools the astronomer's eyes",
            "C. Water magnifies stars by 10,000 times",
            "D. Water generates laser beams"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Liquid Plane Mirror:</strong> Gravity pulls calm water into a perfectly level horizontal plane, creating an optically flat reflecting mirror for celestial observation.<br><strong>Step 2: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 37,
        "concept": "Nālikā Sighting Tube",
        "question": "What instrument was paired with the reflective water basin by Bhāskara II's contemporaries to measure planetary positions?",
        "options": [
            "A. Calibrated sighting tubes (Nālikā Yantras) to measure reflection angles",
            "B. Plastic binoculars",
            "C. Electric infrared sensors",
            "D. Radio antennas"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Classical Instrument:</strong> Ancient Indian astronomers used sighting tubes (Nālikā) aligned with water basin reflections to determine celestial angular elevations.<br><strong>Step 2: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 38,
        "concept": "Real vs Virtual Image",
        "question": "What fundamental property distinguishes a real image from a virtual image?",
        "options": [
            "A. A real image can be captured on a physical screen because rays actually intersect; a virtual image cannot",
            "B. A real image is always formed by mirrors; a virtual image is always formed by lenses",
            "C. A real image is invisible to the human eye",
            "D. Real images only exist in computers"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Real vs Virtual:</strong> Real images are formed by the actual convergence and intersection of light rays, allowing them to be projected onto a screen. Virtual images are formed where rays only appear to diverge from.<br><strong>Step 2: Conclusion:</strong> Option A is correct.</p>"
    },
    {
        "id": 39,
        "concept": "Focusing Sunlight Hazard",
        "question": "Why is it strictly forbidden to look directly at the Sun through a convex lens or a concave mirror?",
        "options": [
            "A. The lens will turn into liquid glass",
            "B. The concentrated solar energy can burn and permanently damage the retina, causing irreversible blindness",
            "C. It causes the Sun to extinguish",
            "D. The mirror will shatter into dust"
        ],
        "correct": 1,
        "solution": r"<p><strong>Step 1: Retinal Hazard:</strong> A converging optical system focuses intense solar radiation onto a microscopic retinal spot, burning light-sensitive cells and causing instant, permanent blindness.<br><strong>Step 2: Conclusion:</strong> Option B is correct.</p>"
    },
    {
        "id": 40,
        "concept": "Siddhānta Śiromaṇi Sections",
        "question": "Which of the following famous mathematical and astronomical works was written by Bhāskara II?",
        "options": [
            "A. Siddhānta Śiromaṇi (comprising Līlāvatī and Bījagaṇita)",
            "B. De Revolutionibus",
            "C. Dialogue Concerning the Two Chief World Systems",
            "D. The Origin of Species"
        ],
        "correct": 0,
        "solution": r"<p><strong>Step 1: Authorship:</strong> Bhāskara II wrote the legendary <em>Siddhānta Śiromaṇi</em> (1150 CE), encompassing the arithmetic masterpiece <em>Līlāvatī</em>, <em>Bījagaṇita</em>, and planetary mechanics.<br><strong>Step 2: Conclusion:</strong> Option A is correct.</p>"
    }
]

