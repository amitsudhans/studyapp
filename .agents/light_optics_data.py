"""
Comprehensive dataset for NCERT Class 10 Science Chapter 9: Light - Reflection and Refraction.
Contains 21 content slides covering all lines, figures, and activities + 4 dedicated quiz challenge slides (40 questions).
"""

CONTENT_SLIDES = [
    {
        "id": 1,
        "title": "Introduction to Light & Rectilinear Propagation",
        "subtitle": "Chapter 9 • Pages 134–135",
        "tag": "Page 134 Foundations",
        "quote": "Light enables us to explore the wonderful universe — from sharp shadows to cosmic rainbows.",
        "lead": "What makes things visible? In a pitch-dark room we see nothing. Light falling on objects is reflected into our eyes, transmitting visual reality.",
        "theory_blocks": [
            {
                "title": "Visibility & Rectilinear Propagation",
                "content": "<p class='mb-2 text-slate-300'>During the day, sunlight illuminates the environment. An opaque object reflects light that falls upon it. When this reflected light enters our eyes, photoreceptors stimulate our optic nerves, enabling vision.</p><p class='text-slate-300'>By observing everyday optical phenomena, we conclude that light travels in <strong>straight lines</strong> in a homogeneous transparent medium. The sharp shadow cast by an opaque object from a small light source directly confirms this rectilinear propagation, conventionally represented as a <strong>ray of light</strong>.</p>"
            },
            {
                "title": "More to Know: Wave-Particle Duality & Diffraction",
                "content": "<p class='mb-2 text-slate-300'>If an obstacle on the path of light is exceptionally minute, light deviates around the edges rather than following a strict geometric line — a phenomenon known as <strong>diffraction</strong>. Geometric optics using simple rays fails at this nanoscale.</p><p class='text-slate-300'>While diffraction requires light to behave as a <strong>wave</strong>, 20th-century photo-electric discoveries revealed light behaving as discrete <strong>particles (photons)</strong>. Modern <strong>Quantum Electrodynamics</strong> resolves this by uniting wave and particle characteristics into quantum duality.</p>"
            }
        ],
        "checkpoints": [
            {
                "q": "What optical evidence demonstrates that light travels along straight lines in a uniform medium?",
                "options": [
                    "Light casting a sharp, crisp shadow of an opaque obstacle",
                    "Light bending into a circular rainbow inside rain droplets",
                    "Light undergoing continuous scattering in atmospheric fog",
                    "Light changing colors through chromatic aberration"
                ],
                "ans": 0,
                "solution": "The formation of sharp geometric shadows behind opaque obstacles directly demonstrates the rectilinear (straight-line) propagation of light rays (NCERT Page 134)."
            },
            {
                "q": "Under what condition does geometric ray optics fail, causing light to bend around edges?",
                "options": [
                    "When light travels through dense optical diamond",
                    "When an opaque obstacle becomes extremely small (comparable to light wavelength)",
                    "When light reflects from a highly polished plane mirror",
                    "When light passes perpendicularly through thick glass"
                ],
                "ans": 1,
                "solution": "When an obstacle in the path of light becomes very small, diffraction occurs and light bends around the edges, requiring wave optics rather than simple rectilinear rays (NCERT Page 134, 'More to Know')."
            }
        ],
        "narration": "Welcome students to Chapter 9: Light - Reflection and Refraction! Why do we see objects? An object reflects the light falling on it into our eyes. Common phenomena prove that light travels in straight lines, casting sharp shadows. However, when obstacles are microscopic, diffraction causes light to bend, revealing its quantum wave-particle nature!"
    },
    {
        "id": 2,
        "title": "Laws of Reflection & Plane Mirrors",
        "subtitle": "Chapter 9 • Pages 134–135",
        "tag": "Section 9.1",
        "quote": "The angle of incidence equals the angle of reflection across every reflecting geometry in nature.",
        "lead": "A highly polished surface, such as a silvered glass mirror, bounces back the majority of incident light according to two universal laws.",
        "theory_blocks": [
            {
                "title": "The Universal Laws of Reflection",
                "content": "<p class='mb-2 text-slate-300'>Regardless of whether a reflecting boundary is flat or curved, two inviolable laws govern reflection:</p><ul class='list-disc pl-5 space-y-1 text-slate-300'><li><strong>First Law:</strong> The angle of incidence ($\\angle i$) is strictly equal to the angle of reflection ($\\angle r$), measured relative to the normal line ($i = r$).</li><li><strong>Second Law:</strong> The incident ray, the normal to the mirror at the point of incidence, and the reflected ray all lie in the same geometric plane.</li></ul>"
            },
            {
                "title": "Characteristics of Plane Mirror Images",
                "content": "<p class='mb-2 text-slate-300'>Images produced by standard flat plane mirrors exhibit five definite properties:</p><ul class='list-disc pl-5 space-y-1 text-slate-300'><li><strong>Virtual & Erect:</strong> Formed behind the mirror where rays appear to diverge; cannot be captured on a physical screen.</li><li><strong>Same Size:</strong> Magnification $m = +1$; image height equals object height ($h' = h$).</li><li><strong>Equidistant:</strong> Image distance behind mirror equals object distance in front ($v = -u$).</li><li><strong>Laterally Inverted:</strong> Right-hand side of object appears as left-hand side of image.</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "Which of the following correctly describes an image formed by a common flat plane mirror?",
                "options": [
                    "Real, inverted, and magnified by 1.5 times",
                    "Virtual, erect, same size as object, and laterally inverted",
                    "Real, erect, diminished, and captured on a screen",
                    "Virtual, inverted, and located at twice the object distance"
                ],
                "ans": 1,
                "solution": "Plane mirror images are always virtual and erect, equal in size to the object ($m = +1$), as far behind the mirror as the object is in front, and laterally inverted (NCERT Page 135)."
            },
            {
                "q": "If a light ray strikes a polished surface at an angle of incidence of 35° with the normal, what is the angle between the incident ray and the reflected ray?",
                "options": [
                    "35°",
                    "55°",
                    "70°",
                    "90°"
                ],
                "ans": 2,
                "solution": "By the first law of reflection, angle of reflection $r = i = 35^\\circ$. The total angle between the incident and reflected rays is $i + r = 35^\\circ + 35^\\circ = 70^\\circ$."
            }
        ],
        "narration": "Let us examine the laws of reflection. The angle of incidence always equals the angle of reflection, and the incident ray, reflected ray, and normal all reside in the same plane. In a plane mirror, images are always virtual, upright, identical in size, equidistant behind the glass, and laterally reversed!"
    },
    {
        "id": 3,
        "title": "Spherical Mirrors: Geometry & Terminology",
        "subtitle": "Chapter 9 • Pages 135–136",
        "tag": "Section 9.2",
        "quote": "Spherical mirrors represent cut segments of a hollow reflective sphere with precise geometric landmarks.",
        "lead": "Curved mirrors are categorized based on their curvature: concave mirrors curve inward toward the centre, while convex mirrors bulge outwards.",
        "theory_blocks": [
            {
                "title": "Concave vs Convex Mirror Anatomy",
                "content": "<p class='mb-2 text-slate-300'>In Activity 9.1, observing a polished steel spoon reveals two curved mirrors: the inward depression acts as a <strong>concave mirror</strong>, while the bulging back acts as a <strong>convex mirror</strong>.</p><p class='text-slate-300'>A spherical mirror whose reflecting surface curves <em>inward</em> (facing the centre of the sphere) is concave. A spherical mirror whose reflecting surface curves <em>outward</em> is convex. The non-reflecting rear surface is silvered and coated with protective opaque paint.</p>"
            },
            {
                "title": "Core Geometric Terminology",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Pole ($P$):</strong> The geometric centre of the spherical reflecting surface. Lies directly on the mirror.</li><li><strong>Centre of Curvature ($C$):</strong> Centre of the sphere from which the mirror was cut. Lies <em>in front</em> of concave mirrors, but <em>behind</em> convex mirrors. Not part of the mirror surface!</li><li><strong>Radius of Curvature ($R$):</strong> Radius of the sphere ($PC = R$).</li><li><strong>Principal Axis:</strong> Straight line passing through $P$ and $C$, normal to the mirror at $P$.</li><li><strong>Aperture ($MN$):</strong> Effective diameter of the circular boundary of the mirror.</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "Where is the centre of curvature ($C$) situated in the case of a convex mirror?",
                "options": [
                    "Directly on the reflecting surface at the pole",
                    "Behind the mirror inside the non-reflecting region",
                    "In front of the reflecting surface at the focus",
                    "At an infinite distance along the vertical axis"
                ],
                "ans": 1,
                "solution": "Because a convex mirror bulges outwards, the centre of the sphere of which it forms a part lies behind its reflecting surface (NCERT Page 136, Figure 9.2b)."
            },
            {
                "q": "What term defines the effective diameter of the circular outline of a spherical mirror?",
                "options": [
                    "Focal length",
                    "Aperture",
                    "Optical axis",
                    "Radius of curvature"
                ],
                "ans": 1,
                "solution": "The diameter of the reflecting surface of a spherical mirror is called its aperture ($MN$). In Class 10, we study mirrors whose aperture is much smaller than $R$ (NCERT Page 137)."
            }
        ],
        "narration": "Notice the anatomy of spherical mirrors! Imagine cutting a slice from a hollow silvered sphere. The pole P is the mirror's physical centre. C is the sphere's centre, lying in front of concave mirrors but behind convex ones. The line connecting P and C is the principal axis, and the mirror's circular diameter is its aperture."
    },
    {
        "id": 4,
        "title": "Principal Focus & Solar Ignition Activity 9.2",
        "subtitle": "Chapter 9 • Pages 136–137",
        "tag": "Focus & Focal Length",
        "quote": "Concentrating distant solar rays at the focal point releases concentrated thermal energy.",
        "lead": "When parallel rays of light strike a spherical mirror, they either converge to a real point or appear to diverge from a virtual point on the principal axis.",
        "theory_blocks": [
            {
                "title": "Activity 9.2: Solar Concentration & Paper Ignition",
                "content": "<p class='mb-2 text-slate-300'>In Activity 9.2, a concave mirror directed toward the sun focuses incident solar rays onto a sheet of paper. As the paper is adjusted, a pinpoint, intensely bright spot appears. Within moments, the paper chars, emits smoke, and bursts into flames!</p><p class='text-slate-300'>This bright spot is the <strong>real image of the sun</strong> formed at the <strong>principal focus ($F$)</strong>. The concentration of radiant energy generates high temperature. The measured distance from mirror to paper gives the approximate <strong>focal length ($f$)</strong>.</p>"
            },
            {
                "title": "Mathematical Relationship: $R = 2f$",
                "content": "<p class='mb-2 text-slate-300'>For concave mirrors, parallel rays converge to a single real focus $F$ in front of the mirror (converging mirror). For convex mirrors, reflected rays diverge and appear to originate from focus $F$ behind the mirror (diverging mirror).</p><p class='text-slate-300'>For all spherical mirrors of small aperture, the principal focus lies precisely halfway between the pole and centre of curvature:<br><span class='text-rose-400 font-mono font-bold text-sm'>$$R = 2f \\quad \\iff \\quad f = \\frac{R}{2}$$</span></p>"
            }
        ],
        "checkpoints": [
            {
                "q": "If a spherical mirror has a radius of curvature of 28 cm, what is its focal length?",
                "options": [
                    "56 cm",
                    "28 cm",
                    "14 cm",
                    "7 cm"
                ],
                "ans": 2,
                "solution": "Using the relation $R = 2f$, the focal length $f = R / 2 = 28 / 2 = 14\\text{ cm}$ (NCERT Page 137)."
            },
            {
                "q": "Why does a piece of paper catch fire when positioned at the focus of a concave mirror facing the sun?",
                "options": [
                    "The mirror creates an electrical spark at the pole",
                    "Parallel solar rays are converged to a tiny point, concentrating immense heat energy",
                    "Reflected UV rays undergo total internal reflection inside the paper fibers",
                    "The paper absorbs blue wavelengths and reflects infrared radiation"
                ],
                "ans": 1,
                "solution": "Sunlight consists of parallel rays. A concave mirror converges these parallel rays to a sharp focal spot, concentrating solar thermal energy sufficiently to ignite the paper (NCERT Page 136, Activity 9.2)."
            }
        ],
        "narration": "Watch closely! In Activity 9.2, when we point a concave mirror at the sun, parallel light rays converge at a single spot on paper. That spot is the principal focus F! The intense concentrated heat soon ignites the paper. For small aperture mirrors, the focal length f is always exactly half the radius of curvature: R equals 2f!"
    },
    {
        "id": 5,
        "title": "Rules for Ray Diagrams of Spherical Mirrors",
        "subtitle": "Chapter 9 • Pages 138–140",
        "tag": "Section 9.2.2 Ray Rules",
        "quote": "Two standard rays are all that is required to pinpoint any image in geometric optics.",
        "lead": "Although countless rays emanate from an illuminated object point, choosing two well-understood rays allows us to construct clean, unambiguous ray diagrams.",
        "theory_blocks": [
            {
                "title": "Rule 1 & Rule 2: Parallel vs Focal Rays",
                "content": "<ul class='list-disc pl-5 space-y-2 text-slate-300'><li><strong>Rule 1 (Parallel Ray):</strong> A ray incident parallel to the principal axis, after reflection, passes through the principal focus $F$ (concave mirror) or appears to diverge from $F$ (convex mirror) [Fig 9.3].</li><li><strong>Rule 2 (Focal Ray):</strong> A ray passing through the principal focus $F$ (concave) or directed toward $F$ (convex), after reflection, emerges strictly <em>parallel</em> to the principal axis [Fig 9.4].</li></ul>"
            },
            {
                "title": "Rule 3 & Rule 4: Centre of Curvature & Oblique Pole Rays",
                "content": "<ul class='list-disc pl-5 space-y-2 text-slate-300'><li><strong>Rule 3 (Normal Ray through $C$):</strong> A ray passing through or directed toward $C$ retraces its exact path backwards after reflection [Fig 9.5]. This occurs because radial lines from $C$ are perpendicular to the sphere surface, meaning $\\angle i = 0^\\circ \\implies \\angle r = 0^\\circ$.</li><li><strong>Rule 4 (Oblique Ray at Pole $P$):</strong> A ray incident obliquely at the pole $P$ reflects symmetrically on the other side such that the principal axis acts as normal ($\\angle i = \\angle r$) [Fig 9.6].</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "Why does a ray of light passing through the centre of curvature ($C$) retrace its original path after reflecting from a concave mirror?",
                "options": [
                    "Because light speed doubles when passing through the centre of curvature",
                    "Because the ray strikes the mirror surface normally along the radius, making $i = r = 0°$",
                    "Because the focus bends the ray backwards through destructive interference",
                    "Because the aperture absorbs half of the wave amplitude at the boundary"
                ],
                "ans": 1,
                "solution": "Any line passing from the centre of curvature to the spherical mirror surface is a radius, and therefore perpendicular (normal) to the mirror at that point. Thus $\\angle i = 0^\\circ$ and the ray reflects straight back (NCERT Page 139, Figure 9.5)."
            },
            {
                "q": "A ray directed toward the principal focus ($F$) of a concave mirror reflects: ",
                "options": [
                    "Back along its own path toward the object",
                    "Obliquely into the centre of curvature",
                    "Parallel to the principal axis",
                    "Perpendicularly away from the pole"
                ],
                "ans": 2,
                "solution": "By the principle of reversibility of light, a ray passing through the principal focus $F$ will reflect parallel to the principal axis (NCERT Page 139, Figure 9.4)."
            }
        ],
        "narration": "To trace images, remember these four golden geometric rules: A parallel ray reflects through the focus F. A ray passing through F emerges parallel. A ray directed through the centre of curvature C hits normally and bounces straight back. And a ray hitting pole P reflects at an equal angle!"
    },
    {
        "id": 6,
        "title": "Concave Mirror: Real Image Formations (Cases 1 to 3)",
        "subtitle": "Chapter 9 • Pages 137–140",
        "tag": "Table 9.1 Positions 1–3",
        "quote": "As an object advances from infinity towards the mirror, its real image recedes and grows in size.",
        "lead": "Exploring the first three object positions for a concave mirror in Activity 9.3: at infinity, beyond C, and directly at the centre of curvature C.",
        "theory_blocks": [
            {
                "title": "Case 1: Object at Infinity & Case 2: Object Beyond C",
                "content": "<ul class='list-disc pl-5 space-y-2 text-slate-300'><li><strong>Case 1 (Object at Infinity):</strong> Parallel incident rays converge at the focus $F$. Image position: <strong>At Focus $F$</strong>. Nature: <strong>Real and Inverted</strong>. Size: <strong>Highly diminished, point-sized</strong>.</li><li><strong>Case 2 (Object Beyond $C$):</strong> Rays from object top cross between $F$ and $C$. Image position: <strong>Between $F$ and $C$</strong>. Nature: <strong>Real and Inverted</strong>. Size: <strong>Diminished</strong> ($|m| < 1$).</li></ul>"
            },
            {
                "title": "Case 3: Object Directly at Centre of Curvature ($C$)",
                "content": "<p class='mb-2 text-slate-300'>When the candle flame is placed at $C$, the ray parallel to axis passes through $F$, while the ray passing through $F$ reflects parallel. They intersect precisely beneath $C$!</p><ul class='list-disc pl-5 space-y-1 text-slate-300'><li><strong>Image Position:</strong> Directly at $C$.</li><li><strong>Image Nature:</strong> Real and Inverted.</li><li><strong>Image Size:</strong> Same size as object ($h' = -h \\implies m = -1$).</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "Where must an object be placed in front of a concave mirror to produce a real, inverted image of the exact same size as the object?",
                "options": [
                    "At the principal focus $F$",
                    "At the centre of curvature $C$",
                    "Beyond the centre of curvature $C$",
                    "Between the pole $P$ and focus $F$"
                ],
                "ans": 1,
                "solution": "When the object is placed at the centre of curvature ($C$), the image is also formed at $C$, is real and inverted, and has the exact same dimensions as the object ($m = -1$) (NCERT Page 138, Table 9.1)."
            },
            {
                "q": "When an object is placed beyond $C$ in front of a concave mirror, where is its image formed?",
                "options": [
                    "Behind the mirror",
                    "Between the pole $P$ and focus $F$",
                    "Between the focus $F$ and centre of curvature $C$",
                    "At infinity"
                ],
                "ans": 2,
                "solution": "For an object beyond $C$, reflected rays converge between $F$ and $C$, producing a real, inverted, and diminished image (NCERT Page 138, Figure 9.7b)."
            }
        ],
        "narration": "Let us trace the first three concave mirror positions! At infinity, the image is a point at focus F. Moving the object closer, beyond C, creates a smaller real image between F and C. But when the object arrives at C, the image forms right at C, inverted, and of the exact same size as the object!"
    },
    {
        "id": 7,
        "title": "Concave Mirror: Magnified Images & Practical Applications",
        "subtitle": "Chapter 9 • Pages 138–140",
        "tag": "Table 9.1 Positions 4–6 & Uses",
        "quote": "Bringing an object closer than the focus unlocks a virtual magnifying effect.",
        "lead": "Studying the remaining three positions (between C and F, at F, and inside F) reveals why concave mirrors power torches, dental tools, and solar furnaces.",
        "theory_blocks": [
            {
                "title": "Cases 4, 5 & 6 (Enlarged & Virtual Images)",
                "content": "<ul class='list-disc pl-5 space-y-2 text-slate-300'><li><strong>Case 4 (Between $C$ and $F$):</strong> Reflected rays cross beyond $C$. Image: <strong>Beyond $C$</strong>, Real, Inverted, and <strong>Enlarged</strong> ($|m| > 1$).</li><li><strong>Case 5 (At Focus $F$):</strong> Reflected rays emerge completely parallel. Image: <strong>At Infinity</strong>, highly magnified. (Reversibility of Case 1!).</li><li><strong>Case 6 (Between $P$ and $F$):</strong> Reflected rays diverge in front of the mirror. Tracing them backward behind the mirror reveals their intersection! Image: <strong>Behind the mirror</strong>, <strong>Virtual and Erect</strong>, <strong>Enlarged</strong> ($m > +1$).</li></ul>"
            },
            {
                "title": "Everyday Applications of Concave Mirrors",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Torches, Searchlights & Car Headlights:</strong> The light bulb is placed at the principal focus $F$ to cast a powerful parallel beam over long distances.</li><li><strong>Dentists & Shaving Mirrors:</strong> Holding the mirror close so the face or tooth lies between $P$ and $F$ produces a magnified, upright virtual image.</li><li><strong>Solar Furnaces:</strong> Massive concave reflector arrays focus vast amounts of parallel sunlight into a single high-temperature focal zone.</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "Why do dentists use a small concave mirror when examining a patient's teeth?",
                "options": [
                    "To invert the image so cavities appear upside down",
                    "To see an erect and magnified virtual image of the tooth by holding it within the focal length",
                    "To converge x-ray radiation directly into the enamel",
                    "To dim excessive bright clinical lighting"
                ],
                "ans": 1,
                "solution": "When a tooth is held close to a concave mirror (between $P$ and $F$), an erect, virtual, and enlarged image is formed, providing a clear magnified view of small dental defects (NCERT Page 140)."
            },
            {
                "q": "Where is the lamp filament placed in automobile headlights to produce a powerful parallel beam?",
                "options": [
                    "At the centre of curvature $C$",
                    "At the principal focus $F$ of the concave reflector",
                    "Between the pole $P$ and focus $F$",
                    "Directly against the glass aperture lens"
                ],
                "ans": 1,
                "solution": "Placing the light source at the principal focus of a concave mirror ensures that reflected rays emerge parallel to the axis, projecting a concentrated beam far ahead (NCERT Page 140)."
            }
        ],
        "narration": "Notice the dramatic shift when the object moves between C and F: the image becomes enlarged beyond C. At focus F, the rays emerge parallel to infinity — perfect for headlights! And when placed inside focus F, a virtual, erect, and magnified image appears behind the mirror — ideal for dentists and shaving!"
    },
    {
        "id": 8,
        "title": "Convex Mirrors: Image Formation & Rear-View Safety",
        "subtitle": "Chapter 9 • Pages 140–142",
        "tag": "Section 9.2 & Table 9.2",
        "quote": "Convex mirrors always provide an upright, diminished view with an expansive visual field.",
        "lead": "Unlike concave mirrors, a convex mirror forms only virtual, erect, and diminished images regardless of object distance, making it the premier choice for automotive mirrors.",
        "theory_blocks": [
            {
                "title": "The Two Image Configurations (Table 9.2)",
                "content": "<ul class='list-disc pl-5 space-y-2 text-slate-300'><li><strong>Position 1 (Object at Infinity):</strong> Reflected rays diverge; their backward extensions meet at $F$ behind mirror. Image: <strong>At Focus $F$ behind mirror</strong>, Virtual & Erect, <strong>Highly diminished (point-sized)</strong>.</li><li><strong>Position 2 (Between Infinity and Pole $P$):</strong> Backward extensions of reflected rays intersect between $P$ and $F$. Image: <strong>Between $P$ and $F$ behind mirror</strong>, Virtual & Erect, <strong>Diminished</strong> ($0 < m < 1$).</li></ul>"
            },
            {
                "title": "Why Convex Mirrors are Superior Rear-View Mirrors",
                "content": "<p class='mb-2 text-slate-300'>In Activity 9.5 and 9.6, a small convex mirror captures a full-length panoramic view of a massive distant tree or monument (such as the famous wall mirror facing the Taj Mahal at Agra Fort!).</p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Always Erect:</strong> Unlike concave mirrors which invert distant traffic, convex mirrors keep vehicles upright.</li><li><strong>Wider Field of View:</strong> Bulging outwards toward the driver, they capture a vastly wider angle than a flat plane mirror of the same dimensions.</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "Why are convex mirrors preferred over flat plane mirrors as rear-view mirrors in automobiles?",
                "options": [
                    "They magnify distant vehicles so they look closer",
                    "They always give an erect image and provide a much wider field of view because they curve outward",
                    "They convert yellow headlight glare into blue polarized light",
                    "They form real images on the windshield"
                ],
                "ans": 1,
                "solution": "Convex mirrors always form an erect (though diminished) image and have an outward curvature that provides a substantially broader field of view than a flat plane mirror (NCERT Page 142)."
            },
            {
                "q": "As an object moves closer to a convex mirror from infinity, what happens to its image?",
                "options": [
                    "It becomes inverted and moves beyond $C$",
                    "It remains virtual and erect, moves from $F$ toward $P$, and increases slightly in size",
                    "It disappears into a point of total darkness",
                    "It turns into a real image captured on a screen"
                ],
                "ans": 1,
                "solution": "As the object moves from infinity toward the pole of a convex mirror, its virtual erect image shifts from the focus $F$ toward the pole $P$, slightly increasing in size while remaining strictly diminished (NCERT Page 141, Activity 9.5)."
            }
        ],
        "narration": "Convex mirrors are automotive lifesavers! No matter where you place an object, a convex mirror always produces an upright, virtual, diminished image behind the glass. Because it curves outwards, it takes in a panoramic field of view, letting drivers monitor traffic behind them with complete safety."
    },
    {
        "id": 9,
        "title": "New Cartesian Sign Convention for Reflection",
        "subtitle": "Chapter 9 • Pages 142–143",
        "tag": "Section 9.2.3 Conventions",
        "quote": "Rigorous algebraic signs prevent optical calculations from descending into chaos.",
        "lead": "To solve numerical mirror problems accurately, we map mirror geometry onto a Cartesian coordinate system with the pole as origin.",
        "theory_blocks": [
            {
                "title": "The 5 New Cartesian Rules (Figure 9.9)",
                "content": "<ol class='list-decimal pl-5 space-y-1.5 text-slate-300'><li>The object is always placed to the <strong>left</strong> of the mirror. Light strikes the mirror traveling left-to-right.</li><li>All distances parallel to the principal axis are measured from the <strong>Pole ($P$)</strong> as coordinate origin $(0, 0)$.</li><li>Distances measured in the direction of incident light (along $+x$-axis, to the <strong>right</strong> of $P$) are taken as <strong>positive ($+$)</strong>.</li><li>Distances measured against incident light (along $-x$-axis, to the <strong>left</strong> of $P$) are taken as <strong>negative ($-$)</strong>.</li><li>Heights measured perpendicular and <strong>above</strong> the principal axis are <strong>positive ($+y$)</strong>; heights <strong>below</strong> are <strong>negative ($-y$)</strong>.</li></ol>"
            },
            {
                "title": "Critical Sign Takeaways for Mirrors",
                "content": "<ul class='list-disc pl-5 space-y-1 text-slate-300'><li><strong>Object Distance ($u$):</strong> Always <strong>negative ($-$)</strong> for all mirrors because the object is in front.</li><li><strong>Focal Length of Concave Mirror:</strong> Focus is in front $\\implies$ <strong>negative ($-f$)</strong>.</li><li><strong>Focal Length of Convex Mirror:</strong> Focus is behind $\\implies$ <strong>positive ($+f$)</strong>.</li><li><strong>Real Image:</strong> Formed in front $\\implies v < 0$; inverted $\\implies h' < 0$.</li><li><strong>Virtual Image:</strong> Formed behind $\\implies v > 0$; erect $\\implies h' > 0$.</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "According to the New Cartesian Sign Convention, what sign must be assigned to the focal length of a concave mirror?",
                "options": [
                    "Always positive ($+$)",
                    "Always negative ($-$)",
                    "Positive when object is at infinity, negative otherwise",
                    "Zero because the pole is at the origin"
                ],
                "ans": 1,
                "solution": "The principal focus of a concave mirror lies in front (to the left of the pole), opposite to incident light, making its focal length strictly negative ($-$) (NCERT Page 143)."
            },
            {
                "q": "If an object is placed 15 cm in front of a mirror, what is its coordinate object distance $u$?",
                "options": [
                    "$u = +15\\text{ cm}$",
                    "$u = -15\\text{ cm}$",
                    "$u = 0\\text{ cm}$",
                    "$u = -30\\text{ cm}$"
                ],
                "ans": 1,
                "solution": "Because the object is always placed to the left of the mirror against the direction of incident light, object distance $u$ is always negative: $u = -15\\text{ cm}$ (NCERT Page 142)."
            }
        ],
        "narration": "Pay close attention to sign conventions! Think of the mirror's pole P as the origin (0,0). Anything to the left is negative; anything to the right is positive. Upward heights are positive; downward heights are negative. Therefore, object distance u is always negative, concave focal length is negative, and convex focal length is positive!"
    },
    {
        "id": 10,
        "title": "Mirror Formula, Magnification & Solved Numericals",
        "subtitle": "Chapter 9 • Pages 143–145",
        "tag": "Section 9.2.4 & Examples 9.1–9.2",
        "quote": "Algebraic optics predicts the exact position and magnification of any reflected image.",
        "lead": "The mirror formula bridges object distance $u$, image distance $v$, and focal length $f$, while linear magnification quantifies scaling.",
        "theory_blocks": [
            {
                "title": "Mirror Formula & Linear Magnification",
                "content": "<p class='mb-2 text-slate-300'>For all spherical mirrors across all object positions:</p><p class='text-rose-400 font-mono font-bold text-sm mb-2'>$$\\frac{1}{v} + \\frac{1}{u} = \\frac{1}{f}$$</p><p class='text-slate-300 mb-2'><strong>Linear Magnification ($m$):</strong> Ratio of image height $h'$ to object height $h$:</p><p class='text-amber-400 font-mono font-bold text-sm'>$$m = \\frac{h'}{h} = -\\frac{v}{u}$$</p><p class='text-xs text-slate-400'>Note the minus sign! Negative $m$ indicates a real inverted image; positive $m$ indicates a virtual erect image.</p>"
            },
            {
                "title": "Walkthrough: Examples 9.1 & 9.2",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300 text-xs sm:text-sm'><li><strong>Example 9.1 (Convex Mirror):</strong> $R = +3.00\\text{ m} \\implies f = +1.50\\text{ m}$, $u = -5.00\\text{ m}$.<br>$\\frac{1}{v} = \\frac{1}{f} - \\frac{1}{u} = \\frac{1}{1.50} - \\frac{1}{-5.00} = \\frac{6.50}{7.50} \\implies v = +1.15\\text{ m}$ (behind mirror).<br>$m = -\\frac{v}{u} = -\\frac{+1.15}{-5.00} = +0.23$ (virtual, erect, diminished by factor 0.23).</li><li><strong>Example 9.2 (Concave Mirror):</strong> $h = +4.0\\text{ cm}, u = -25.0\\text{ cm}, f = -15.0\\text{ cm}$.<br>$\\frac{1}{v} = \\frac{1}{-15} - \\frac{1}{-25} = \\frac{-2}{75} \\implies v = -37.5\\text{ cm}$ (screen placed 37.5 cm in front).<br>$h' = -\\frac{v}{u} h = -\\frac{-37.5}{-25.0} \\times 4.0 = -6.0\\text{ cm}$ (real, inverted, magnified).</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "A concave mirror produces a 3 times magnified real image of an object placed at 10 cm in front of it. Where is the image located?",
                "options": [
                    "$v = -30\\text{ cm}$ (30 cm in front of the mirror)",
                    "$v = +30\\text{ cm}$ (30 cm behind the mirror)",
                    "$v = -3.33\\text{ cm}$ (3.33 cm in front)",
                    "$v = +10\\text{ cm}$ (10 cm behind)"
                ],
                "ans": 0,
                "solution": "For a real image, magnification $m = -3$. Since $m = -v/u$, we have $-3 = -v/(-10) \\implies -3 = v/10 \\implies v = -30\\text{ cm}$. The image is 30 cm in front of the mirror (NCERT Page 145, Intext Q2)."
            },
            {
                "q": "What is the physical interpretation of a magnification value of $m = +1$ for a mirror?",
                "options": [
                    "The image is real, inverted, and diminished",
                    "The image is virtual, erect, and of the exact same size as the object (like a plane mirror)",
                    "The image is formed at the centre of curvature and inverted",
                    "The image is highly magnified at infinity"
                ],
                "ans": 1,
                "solution": "The positive sign indicates a virtual, erect image, while a magnitude of 1 means image height equals object height ($h' = h$), characteristic of a plane mirror (NCERT Page 160, Exercise Q13)."
            }
        ],
        "narration": "Mastering the mirror formula unlocks optical engineering! 1 over v plus 1 over u equals 1 over f. Remember the magnification formula: m equals h-prime over h, which equals minus v over u. If m is negative, your image is real and inverted. If positive, it is virtual and erect!"
    },
    {
        "id": 11,
        "title": "Refraction of Light & Everyday Phenomena",
        "subtitle": "Chapter 9 • Pages 145–146",
        "tag": "Section 9.3 Foundations",
        "quote": "Light alters its directional speed at the boundary separating two transparent optical media.",
        "lead": "Why does a pencil immersed in water look broken? Why does a swimming pool look shallower than it really is? Refraction holds the answer.",
        "theory_blocks": [
            {
                "title": "Everyday Manifestations of Refraction",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Apparent Depth:</strong> The bottom of a water tank or swimming pool appears raised because light rays diverging from the base bend away from the normal upon exiting water into air.</li><li><strong>Bent Pencil:</strong> A pencil partly immersed in water appears displaced or kinked at the air-water interface because light from the submerged portion changes direction at the surface.</li><li><strong>Magnified Lemon:</strong> A lemon immersed in a glass tumbler appears substantially enlarged when viewed from the sides.</li><li><strong>Raised Print:</strong> Printed letters appear raised when viewed through a thick glass slab.</li></ul>"
            },
            {
                "title": "Activities 9.7 & 9.8: The Magic Coin",
                "content": "<p class='mb-2 text-slate-300'>In Activity 9.7, attempting to snatch a coin from a bucket in a single reach fails because the coin's apparent position is shallower than its real depth.</p><p class='text-slate-300'>In Activity 9.8, a coin in a shallow bowl is moved just out of line of sight behind the rim. Pouring water into the bowl causes the coin to magically reappear! Refraction bends rays over the rim into the observer's eye.</p>"
            }
        ],
        "checkpoints": [
            {
                "q": "Why does a coin placed in an empty bowl that has just disappeared from sight become visible again when water is poured into the bowl?",
                "options": [
                    "Water makes the coin float up to the surface",
                    "Light rays coming from the coin refract (bend away from the normal) at the water-air interface into the observer's eye",
                    "Water creates internal reflection that projects a hologram above the rim",
                    "Water dissolves copper particles that illuminate the rim"
                ],
                "ans": 1,
                "solution": "Light originating from the coin bends away from the normal upon exiting water into air, causing the rays to clear the rim of the bowl and enter the observer's eye (NCERT Page 146, Activity 9.8)."
            },
            {
                "q": "What is the fundamental cause of refraction when light passes obliquely from one transparent medium into another?",
                "options": [
                    "A change in the wavelength of sound in the environment",
                    "A change in the speed of light as it transitions between different optical media",
                    "The reflection of electrons by atomic nuclei",
                    "The total absorption of red wavelengths in the medium"
                ],
                "ans": 1,
                "solution": "Refraction is fundamentally caused by the change in the speed of light as it transitions from one transparent medium to another with different optical density (NCERT Page 147)."
            }
        ],
        "narration": "Have you ever wondered why a pencil placed in water appears snapped at the waterline? Or why a coin hidden behind a bowl rim reappears when water is poured in? This is refraction! Because light travels at different speeds in air and water, rays bend at the boundary, shifting their apparent positions."
    },
    {
        "id": 12,
        "title": "Refraction through a Rectangular Glass Slab",
        "subtitle": "Chapter 9 • Pages 146–147",
        "tag": "Activity 9.10 & Figure 9.10",
        "quote": "Bending at the entry face is matched by equal and opposite bending at the exit face.",
        "lead": "Tracing pins across a rectangular glass slab reveals why emergent rays travel strictly parallel to incident rays, offset only by a lateral displacement.",
        "theory_blocks": [
            {
                "title": "Activity 9.10 Protocol & Ray Path",
                "content": "<p class='mb-2 text-slate-300'>Four pins ($E, F, G, H$) are aligned across a glass block $ABCD$ [Figure 9.10]:</p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Interface 1 ($AB$ Air $\\to$ Glass):</strong> Ray travels from an optically rarer medium (air) to an optically denser medium (glass). The ray slows down and bends <strong>towards the normal</strong> ($i_1 > r_1$).</li><li><strong>Interface 2 ($CD$ Glass $\\to$ Air):</strong> Ray travels from an optically denser medium (glass) to an optically rarer medium (air). The ray speeds up and bends <strong>away from the normal</strong> ($i_2 < r_2$).</li></ul>"
            },
            {
                "title": "Lateral Shift & Normal Incidence",
                "content": "<p class='mb-2 text-slate-300'>Because opposite faces $AB$ and $CD$ are strictly parallel, the extent of bending at both boundaries is equal and opposite. Consequently, the <strong>emergent ray is strictly parallel</strong> to the original incident ray path.</p><p class='text-slate-300'>However, the beam is shifted sideways by a perpendicular distance called <strong>lateral displacement</strong> (lateral shift).<br><em>Special Case:</em> If a ray strikes the slab <strong>normally ($i = 0^\\circ$)</strong>, it passes straight through without any deviation!</p>"
            }
        ],
        "checkpoints": [
            {
                "q": "Why does a light ray emerging from a rectangular glass slab travel parallel to its original incident direction?",
                "options": [
                    "Because glass absorbs all oblique photons",
                    "Because the extent of bending at the two parallel opposite interfaces is equal and opposite",
                    "Because light accelerates to infinite speed inside silica",
                    "Because total internal reflection cancels the angle of incidence"
                ],
                "ans": 1,
                "solution": "At the parallel opposite faces $AB$ and $CD$, the bending into glass (towards normal) is exactly neutralized by the equal and opposite bending into air (away from normal), leaving the emergent ray parallel to the incident ray (NCERT Page 147)."
            },
            {
                "q": "What happens to a ray of light that strikes the interface between air and glass normally ($i = 0°$)?",
                "options": [
                    "It bends at 90° along the boundary",
                    "It is totally reflected back into air with 100% loss",
                    "It passes through without any deviation or change in direction",
                    "It splits into rainbow colors"
                ],
                "ans": 2,
                "solution": "When a ray of light strikes an interface perpendicularly ($i = 0^\\circ$), the angle of refraction is also zero ($r = 0^\\circ$), so the ray passes through without bending (NCERT Page 147)."
            }
        ],
        "narration": "Trace the ray in Activity 9.10! Entering the glass slab, light bends toward the normal. Exiting into air, it bends away by the exact same angle! This equal and opposite bending means the emerging beam travels strictly parallel to the incident beam, shifted sideways by a lateral displacement."
    },
    {
        "id": 13,
        "title": "Laws of Refraction & Snell's Law",
        "subtitle": "Chapter 9 • Page 148",
        "tag": "Section 9.3.1 Snell's Law",
        "quote": "Snell's ratio binds the sines of incidence and refraction into an invariant constant.",
        "lead": "Just as reflection follows precise geometric laws, refraction is governed by two fundamental physical principles formulated by Willebrord Snell.",
        "theory_blocks": [
            {
                "title": "The First Law of Refraction",
                "content": "<p class='text-slate-300'>The incident ray, the refracted ray, and the normal to the interface separating two transparent media at the point of incidence, all lie in the <strong>same geometric plane</strong>.</p><p class='text-xs text-slate-400 mt-2'>This coplanar law ensures that refraction never deviates into a third spatial dimension.</p>"
            },
            {
                "title": "The Second Law of Refraction (Snell's Law)",
                "content": "<p class='mb-2 text-slate-300'>For light of a given colour (wavelength) and for a given pair of media, the ratio of the sine of the angle of incidence to the sine of the angle of refraction is a <strong>constant</strong> (for $0^\\circ < i < 90^\\circ$):</p><p class='text-rose-400 font-mono font-bold text-sm mb-2'>$$\\frac{\\sin i}{\\sin r} = \\text{constant} = n_{21}$$</p><p class='text-slate-300'>This constant value $n_{21}$ is called the <strong>refractive index</strong> of the second medium with respect to the first medium.</p>"
            }
        ],
        "checkpoints": [
            {
                "q": "What is the mathematical formulation of Snell's Law of refraction?",
                "options": [
                    "$\\frac{i}{r} = \\text{constant}$",
                    "$\\frac{\\sin i}{\\sin r} = \\text{constant}$",
                    "$\\sin i \\times \\sin r = 1$",
                    "$\\tan i - \\tan r = \\text{constant}$"
                ],
                "ans": 1,
                "solution": "Snell's Law states that the ratio of the sine of the angle of incidence to the sine of the angle of refraction is a constant: $\\frac{\\sin i}{\\sin r} = n_{21}$ (NCERT Page 148, Eq. 9.4)."
            },
            {
                "q": "When a ray of light passes obliquely from air into water, does it bend towards or away from the normal?",
                "options": [
                    "Away from the normal because water is less dense than air",
                    "Towards the normal because water is optically denser than air",
                    "It continues straight without any bending",
                    "It reflects completely at 90 degrees"
                ],
                "ans": 1,
                "solution": "Because water is optically denser than air, light slows down upon entering water and bends towards the normal (NCERT Page 150, Intext Q1)."
            }
        ],
        "narration": "Remember Snell's Law! The sine of angle of incidence divided by the sine of angle of refraction is always constant for any pair of optical media. This constant is the refractive index n21. When entering an optically denser medium like water, light slows down and bends toward the normal!"
    },
    {
        "id": 14,
        "title": "The Refractive Index & Optical Density",
        "subtitle": "Chapter 9 • Pages 148–150",
        "tag": "Section 9.3.2 & Table 9.3",
        "quote": "Refractive index quantifies how substantially a material slows the cosmic speed of light.",
        "lead": "Light travels fastest in a vacuum ($3 \\times 10^8\\text{ m/s}$). In material media, it slows down — the ratio of these velocities defines absolute refractive index.",
        "theory_blocks": [
            {
                "title": "Speed of Light & Absolute Refractive Index",
                "content": "<p class='mb-2 text-slate-300'>Let speed of light in air/vacuum be $c = 3 \\times 10^8\\text{ m/s}$ and in a given medium be $v$. The <strong>absolute refractive index ($n_m$)</strong> is:</p><p class='text-rose-400 font-mono font-bold text-sm mb-2'>$$n_m = \\frac{c}{v}$$</p><p class='text-slate-300 text-xs sm:text-sm'>Relative index: $n_{21} = \\frac{v_1}{v_2}$ and $n_{12} = \\frac{v_2}{v_1} \\implies n_{21} = \\frac{1}{n_{12}}$.<br>For glass with $n = 1.50$: $v = \\frac{c}{n} = \\frac{3 \\times 10^8}{1.50} = 2.0 \\times 10^8\\text{ m/s}$.</p>"
            },
            {
                "title": "Optical Density vs Mass Density (Table 9.3)",
                "content": "<p class='mb-2 text-slate-300'><strong>Crucial distinction:</strong> Optical density is NOT the same as mass density!</p><ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li>Water: $n = 1.33$ | Kerosene: $n = 1.44$ | Crown glass: $n = 1.52$ | Diamond: $n = 2.42$ (highest optical density).</li><li><strong>The Kerosene Paradox:</strong> Kerosene has a higher refractive index than water, making it <em>optically denser</em>. Yet kerosene floats on water because its <em>mass density</em> is lower!</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "Light enters from air into glass having a refractive index of 1.50. What is the speed of light in the glass?",
                "options": [
                    "$3.0 \\times 10^8\\text{ m/s}$",
                    "$2.0 \\times 10^8\\text{ m/s}$",
                    "$1.5 \\times 10^8\\text{ m/s}$",
                    "$4.5 \\times 10^8\\text{ m/s}$"
                ],
                "ans": 1,
                "solution": "Using $n = c / v$, we find $v = c / n = (3 \\times 10^8\\text{ m/s}) / 1.50 = 2.0 \\times 10^8\\text{ m/s}$ (NCERT Page 150, Intext Q2)."
            },
            {
                "q": "Why is kerosene considered optically denser than water, even though it floats on water?",
                "options": [
                    "Because kerosene has greater mass density than water",
                    "Because kerosene has a higher refractive index (1.44) than water (1.33), slowing light more, despite having lower mass density",
                    "Because kerosene evaporates faster than water",
                    "Because kerosene reflects green light while water absorbs infrared"
                ],
                "ans": 1,
                "solution": "Optical density refers to the ability to refract/slow light (measured by refractive index). Kerosene ($n = 1.44$) is optically denser than water ($n = 1.33$), even though its physical mass density is lower (NCERT Page 149)."
            }
        ],
        "narration": "Remember the key formula: n equals c divided by v! Light races through vacuum at 300,000 kilometers per second. In diamond, with a high refractive index of 2.42, light slows to under 124,000 kilometers per second. And don't confuse optical density with mass density: kerosene floats on water, yet it is optically denser!"
    },
    {
        "id": 15,
        "title": "Spherical Lenses: Anatomy, Convergence & Divergence",
        "subtitle": "Chapter 9 • Pages 150–152",
        "tag": "Section 9.3.3 Lenses",
        "quote": "Double-curved transparent boundaries harness refraction to focus or disperse light.",
        "lead": "A lens is a transparent medium bounded by two surfaces, where at least one is spherical. Convex lenses converge light; concave lenses diverge light.",
        "theory_blocks": [
            {
                "title": "Convex vs Concave Lens Anatomy",
                "content": "<ul class='list-disc pl-5 space-y-2 text-slate-300'><li><strong>Convex Lens (Double Convex):</strong> Thicker at the middle than at the edges. Bends incident parallel rays inward to intersect at a real focus $\\implies$ <strong>Converging Lens</strong> [Figure 9.12a].</li><li><strong>Concave Lens (Double Concave):</strong> Thicker at the edges than at the middle. Bends incident parallel rays outward, appearing to diverge from a virtual focus $\\implies$ <strong>Diverging Lens</strong> [Figure 9.12b].</li></ul>"
            },
            {
                "title": "Core Landmarks: Optical Centre & Dual Foci",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300'><li><strong>Optical Centre ($O$):</strong> The central point of the lens. A ray of light passing through $O$ emerges completely undeviated!</li><li><strong>Centres of Curvature ($C_1, C_2$ or $2F_1, 2F_2$):</strong> Centres of the two bounding spheres.</li><li><strong>Dual Principal Foci ($F_1, F_2$):</strong> Because light can enter from either face, every lens possesses two symmetrical principal foci equidistant from $O$.</li><li><strong>Activity 9.11:</strong> Concentrating solar rays through a convex lens burns paper at focus $F$, providing a simple measure of focal length $f$.</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "What happens to a ray of light that passes directly through the optical centre ($O$) of a thin spherical lens?",
                "options": [
                    "It is reflected straight back along the principal axis",
                    "It bends sharply toward the nearest principal focus",
                    "It passes through without suffering any deviation",
                    "It undergoes total dispersion into seven colours"
                ],
                "ans": 2,
                "solution": "A ray of light traveling through the optical centre $O$ of a thin spherical lens passes straight through without any deviation (NCERT Page 151, Figure 9.15)."
            },
            {
                "q": "Why is a double convex lens termed a 'converging lens'?",
                "options": [
                    "Because it reflects incident rays backwards to infinity",
                    "Because it refracts parallel incident rays inwards to meet at a single focal point",
                    "Because it scatters light into a divergent conical beam",
                    "Because it absorbs heat from surrounding air"
                ],
                "ans": 1,
                "solution": "A convex lens is called a converging lens because parallel rays of light passing through it refract inwards to intersect at the principal focus on the opposite side (NCERT Page 150, Figure 9.12a)."
            }
        ],
        "narration": "Meet spherical lenses! A convex lens is thicker in the middle and converges parallel rays to a sharp focus — just like in Activity 9.11 where sunlight ignited the paper! A concave lens is thinner in the middle and diverges rays outward. Most importantly, any ray passing through the optical centre O continues without bending at all!"
    },
    {
        "id": 16,
        "title": "Convex Lens: Image Formation (All 6 Positions)",
        "subtitle": "Chapter 9 • Page 152",
        "tag": "Table 9.4 All 6 Cases",
        "quote": "Moving an object toward a convex lens sweeps its image from the focus to infinity, then into virtual magnification.",
        "lead": "In Activity 9.12, placing a candle along marked chalk lines ($O, F_1, 2F_1$) maps all six possible image positions for a converging lens.",
        "theory_blocks": [
            {
                "title": "Cases 1 to 3: Real Diminished & Same-Size Images",
                "content": "<ul class='list-disc pl-5 space-y-2 text-slate-300'><li><strong>1. At Infinity:</strong> Image at $F_2$, highly diminished (point-sized), Real & Inverted.</li><li><strong>2. Beyond $2F_1$:</strong> Image between $F_2$ and $2F_2$, diminished, Real & Inverted.</li><li><strong>3. At $2F_1$:</strong> Image at $2F_2$, <strong>same size as object</strong>, Real & Inverted ($m = -1$).</li></ul>"
            },
            {
                "title": "Cases 4 to 6: Real Enlarged to Virtual Magnifying Glass",
                "content": "<ul class='list-disc pl-5 space-y-2 text-slate-300'><li><strong>4. Between $F_1$ and $2F_1$:</strong> Image beyond $2F_2$, <strong>enlarged</strong>, Real & Inverted (Cinema projector principle).</li><li><strong>5. At Focus $F_1$:</strong> Rays emerge parallel; Image <strong>at Infinity</strong>, highly magnified.</li><li><strong>6. Between $F_1$ and Optical Centre $O$:</strong> Rays diverge on other side; extending backwards forms a <strong>Virtual, Erect, and Enlarged image on the same side</strong> ($m > +1$, <strong>simple magnifying glass!</strong>).</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "Where should an object be placed in front of a convex lens to obtain a real image of the exact same size as the object?",
                "options": [
                    "At the principal focus $F_1$",
                    "At twice the focal length ($2F_1$)",
                    "At infinity",
                    "Between the optical centre $O$ and focus $F_1$"
                ],
                "ans": 1,
                "solution": "When an object is placed at $2F_1$, a real, inverted image of identical size ($m = -1$) is formed at $2F_2$ on the opposite side of the convex lens (NCERT Page 152, Table 9.4)."
            },
            {
                "q": "To use a convex lens as a simple magnifying glass to read tiny print, where must the text be positioned?",
                "options": [
                    "At infinity",
                    "Beyond $2F_1$",
                    "Between the principal focus $F_1$ and the optical centre $O$",
                    "At the second focus $2F_2$"
                ],
                "ans": 2,
                "solution": "Positioning an object between $F_1$ and $O$ produces an erect, magnified, virtual image on the same side as the object, which is the operational basis of a magnifying glass (NCERT Page 152, Figure 9.16f)."
            }
        ],
        "narration": "Convex lens image formation mirrors our concave mirror rules! Far away at infinity, the image is at focus F2. At 2F1, the image is at 2F2 and identical in size. Move between F1 and 2F1, and you get an enlarged real image. And inside F1, you get a virtual, upright, magnified view — the secret behind watchmakers' magnifying glasses!"
    },
    {
        "id": 17,
        "title": "Concave Lens: Image Formation & Ray Rules",
        "subtitle": "Chapter 9 • Pages 153–155",
        "tag": "Table 9.5 & Figures 9.13–9.17",
        "quote": "Concave lenses are invariant: always virtual, always erect, always diminished.",
        "lead": "In Activity 9.13, moving a candle anywhere in front of a concave lens always yields an upright, shrunken image between the focus and optical centre.",
        "theory_blocks": [
            {
                "title": "The 2 Concave Lens Configurations (Table 9.5)",
                "content": "<ul class='list-disc pl-5 space-y-2 text-slate-300'><li><strong>1. Object at Infinity:</strong> Incident parallel rays diverge; tracing their backward extensions reveals an image formed <strong>at focus $F_1$ on the same side</strong>, highly diminished (point-sized), <strong>Virtual & Erect</strong>.</li><li><strong>2. Between Infinity and Optical Centre $O$:</strong> Backward extensions intersect between $F_1$ and $O$. Image: <strong>Between $F_1$ and $O$ on the same side</strong>, diminished, <strong>Virtual & Erect</strong> ($0 < m < 1$).</li></ul>"
            },
            {
                "title": "Summary of 3 Construction Rays for Lenses",
                "content": "<ol class='list-decimal pl-5 space-y-1.5 text-slate-300'><li>A ray parallel to the principal axis refracts through $F_2$ (convex) or appears to diverge from $F_1$ (concave) [Fig 9.13].</li><li>A ray passing through $F_1$ (convex) or directed toward $F_2$ (concave) emerges parallel to the principal axis [Fig 9.14].</li><li>A ray passing through the optical centre $O$ emerges straight without deviation [Fig 9.15].</li></ol>"
            }
        ],
        "checkpoints": [
            {
                "q": "What is the nature and size of an image formed by a concave lens for any real object placed at a finite distance?",
                "options": [
                    "Real, inverted, and magnified",
                    "Virtual, erect, and diminished",
                    "Real, erect, and same size as object",
                    "Virtual, inverted, and highly magnified"
                ],
                "ans": 1,
                "solution": "A concave lens invariably produces a virtual, erect, and diminished image on the same side as the object, located between the optical centre $O$ and focus $F_1$ (NCERT Page 153, Table 9.5)."
            },
            {
                "q": "A spherical mirror and a thin spherical lens each have a focal length of -15 cm. The mirror and lens are likely to be:",
                "options": [
                    "Both concave",
                    "Both convex",
                    "Mirror is concave, lens is convex",
                    "Mirror is convex, lens is concave"
                ],
                "ans": 0,
                "solution": "By Cartesian sign convention, both a concave mirror and a concave lens have negative focal lengths ($f < 0$). Thus, both are concave (NCERT Page 159, Exercise Q4)."
            }
        ],
        "narration": "Notice how reliable concave lenses are! Regardless of where an object stands, a concave lens always produces an erect, virtual, diminished image between O and F1. Furthermore, remember this essential rule: whenever you see a negative focal length, both the mirror and the lens are concave!"
    },
    {
        "id": 18,
        "title": "Lens Formula, Magnification & Solved Examples 9.3–9.4",
        "subtitle": "Chapter 9 • Pages 155–157",
        "tag": "Section 9.3.7 & Examples",
        "quote": "A subtle sign change distinguishes the lens formula from the mirror formula.",
        "lead": "The lens formula connects $u$, $v$, and $f$. Notice the minus sign: $\\frac{1}{v} - \\frac{1}{u} = \\frac{1}{f}$, while lens magnification is $m = +\\frac{v}{u}$.",
        "theory_blocks": [
            {
                "title": "Lens Formula & Linear Magnification",
                "content": "<p class='mb-2 text-slate-300'>For all spherical lenses with Cartesian signs applied:</p><p class='text-rose-400 font-mono font-bold text-sm mb-2'>$$\\frac{1}{v} - \\frac{1}{u} = \\frac{1}{f}$$</p><p class='text-slate-300 mb-2'><strong>Linear Magnification ($m$):</strong></p><p class='text-amber-400 font-mono font-bold text-sm'>$$m = \\frac{h'}{h} = \\frac{v}{u}$$</p><p class='text-xs text-slate-400'>Note: Unlike mirrors ($m = -v/u$), lenses have a positive ratio ($m = +v/u$)!</p>"
            },
            {
                "title": "Walkthrough: Examples 9.3 & 9.4",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300 text-xs sm:text-sm'><li><strong>Example 9.3 (Concave Lens):</strong> $f = -15\\text{ cm}, v = -10\\text{ cm}, u = ?$<br>$\\frac{1}{u} = \\frac{1}{v} - \\frac{1}{f} = \\frac{1}{-10} - \\frac{1}{-15} = -\\frac{1}{30} \\implies u = -30\\text{ cm}$.<br>$m = \\frac{v}{u} = \\frac{-10}{-30} = +\\frac{1}{3} = +0.33$ (virtual, erect, one-third object size).</li><li><strong>Example 9.4 (Convex Lens):</strong> $h = +2.0\\text{ cm}, f = +10\\text{ cm}, u = -15\\text{ cm}$.<br>$\\frac{1}{v} = \\frac{1}{u} + \\frac{1}{f} = \\frac{1}{-15} + \\frac{1}{10} = \\frac{1}{30} \\implies v = +30\\text{ cm}$ (other side).<br>$m = \\frac{v}{u} = \\frac{+30}{-15} = -2 \\implies h' = m \\times h = (-2)(2.0) = -4.0\\text{ cm}$ (real, inverted, 2x enlarged).</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "An object 5 cm tall is placed 25 cm away from a converging lens of focal length 10 cm. What is the image distance $v$?",
                "options": [
                    "$v = +16.67\\text{ cm}$",
                    "$v = -16.67\\text{ cm}$",
                    "$v = +50.0\\text{ cm}$",
                    "$v = -7.14\\text{ cm}$"
                ],
                "ans": 0,
                "solution": "Here $u = -25\\text{ cm}$ and $f = +10\\text{ cm}$. Using $1/v - 1/u = 1/f \\implies 1/v = 1/f + 1/u = 1/10 - 1/25 = 3/50 \\implies v = 50/3 = +16.67\\text{ cm}$ (NCERT Page 160, Exercise Q10)."
            },
            {
                "q": "What is the key sign difference between the magnification formula for mirrors versus lenses?",
                "options": [
                    "Mirrors use $m = +v/u$, while lenses use $m = -v/u$",
                    "Mirrors use $m = -v/u$, while lenses use $m = +v/u$",
                    "Mirrors have no sign, while lenses are always negative",
                    "There is no difference; both use identical equations"
                ],
                "ans": 1,
                "solution": "For spherical mirrors, $m = -v/u$, whereas for spherical lenses, $m = +v/u$ (NCERT Page 143 vs Page 156)."
            }
        ],
        "narration": "Watch the signs carefully! For mirrors, it is 1 over v PLUS 1 over u equals 1 over f, with magnification MINUS v over u. But for lenses, it is 1 over v MINUS 1 over u equals 1 over f, and magnification is PLUS v over u. Don't swap them on your exams!"
    },
    {
        "id": 19,
        "title": "Power of a Lens & Lens Combinations",
        "subtitle": "Chapter 9 • Pages 157–158",
        "tag": "Section 9.3.8 Dioptres",
        "quote": "Shorter focal lengths bend light through wider angles, yielding greater optical power.",
        "lead": "The degree of convergence or divergence achieved by a lens is quantified by its optical power, defined as the reciprocal of its focal length in metres.",
        "theory_blocks": [
            {
                "title": "Power Formula & The Dioptre Unit",
                "content": "<p class='mb-2 text-slate-300'>A convex lens of short focal length bends light through large angles, focusing it close to $O$. The <strong>power ($P$)</strong> of a lens of focal length $f$ (in metres) is:</p><p class='text-rose-400 font-mono font-bold text-sm mb-2'>$$P = \\frac{1}{f\\text{ (in metres)}}$$</p><p class='text-slate-300'>The SI unit of optical power is the <strong>dioptre (D)</strong>. $1\\text{ D} = 1\\text{ m}^{-1}$.<br>Convex lens ($f > 0$) $\\implies$ <strong>Positive Power ($+$)</strong>.<br>Concave lens ($f < 0$) $\\implies$ <strong>Negative Power ($-$)</strong>.</p>"
            },
            {
                "title": "Combinations of Lenses in Contact",
                "content": "<p class='mb-2 text-slate-300'>When multiple lenses with powers $P_1, P_2, P_3, \\dots$ are placed in direct contact, the net total power $P$ is their direct <strong>algebraic sum</strong>:</p><p class='text-amber-400 font-mono font-bold text-sm mb-2'>$$P = P_1 + P_2 + P_3 + \\dots$$</p><p class='text-xs text-slate-300'>Opticians use this additive property in testing spectacle frames. For example, combining $+2.0\\text{ D}$ and $+0.25\\text{ D}$ yields $+2.25\\text{ D}$. Multi-lens systems eliminate chromatic and spherical aberrations in cameras, microscopes, and telescopes.</p>"
            }
        ],
        "checkpoints": [
            {
                "q": "What is the power of a concave lens having a focal length of 2 metres?",
                "options": [
                    "$+0.5\\text{ D}$",
                    "$-0.5\\text{ D}$",
                    "$-2.0\\text{ D}$",
                    "$+2.0\\text{ D}$"
                ],
                "ans": 1,
                "solution": "For a concave lens, focal length is negative: $f = -2\\text{ m}$. Thus, power $P = 1/f = 1/(-2) = -0.5\\text{ D}$ (NCERT Page 158, Intext Q3)."
            },
            {
                "q": "An optician prescribes a corrective spectacle lens with power $P = +1.5\\text{ D}$. What is its focal length, and what type of lens is it?",
                "options": [
                    "$f = +0.67\\text{ m} (+66.7\\text{ cm})$, converging (convex) lens",
                    "$f = -0.67\\text{ m} (-66.7\\text{ cm})$, diverging (concave) lens",
                    "$f = +1.5\\text{ m} (+150\\text{ cm})$, cylindrical lens",
                    "$f = -1.5\\text{ m} (-150\\text{ cm})$, plane mirror"
                ],
                "ans": 0,
                "solution": "Focal length $f = 1/P = 1/(+1.5) = +0.667\\text{ m} = +66.7\\text{ cm}$. Because the power and focal length are positive, the prescribed lens is a converging (convex) lens (NCERT Page 160, Exercise Q17)."
            }
        ],
        "narration": "Lens power is simply 1 over focal length in metres! The unit is dioptres, D. A positive power means a convex lens; a negative power means a concave lens. When opticians layer lenses together in testing glasses, the total power is just the simple algebraic sum: P1 plus P2 plus P3!"
    },
    {
        "id": 20,
        "title": "NCERT Chapter Summary & Formula Master Sheet",
        "subtitle": "Chapter 9 • Pages 158–159",
        "tag": "Summary Synthesis",
        "quote": "Mastery of sign conventions, mirror laws, and lens equations synthesizes Chapter 9 into pure intuition.",
        "lead": "A unified comparison sheet consolidating mirror formulas, lens formulas, magnification conventions, and optical power.",
        "theory_blocks": [
            {
                "title": "Spherical Mirrors vs Spherical Lenses Comparison",
                "content": "<div class='overflow-x-auto text-xs'><table class='w-full border-collapse border border-slate-700 text-left'><tr class='bg-slate-800 text-slate-200'><th class='p-2 border border-slate-700'>Feature</th><th class='p-2 border border-slate-700'>Spherical Mirror</th><th class='p-2 border border-slate-700'>Spherical Lens</th></tr><tr><td class='p-2 border border-slate-700 font-bold'>Governing Formula</td><td class='p-2 border border-slate-700 font-mono text-rose-300'>1/v + 1/u = 1/f</td><td class='p-2 border border-slate-700 font-mono text-emerald-300'>1/v - 1/u = 1/f</td></tr><tr><td class='p-2 border border-slate-700 font-bold'>Magnification ($m$)</td><td class='p-2 border border-slate-700 font-mono text-rose-300'>m = -v/u = h'/h</td><td class='p-2 border border-slate-700 font-mono text-emerald-300'>m = +v/u = h'/h</td></tr><tr><td class='p-2 border border-slate-700 font-bold'>Focus Sign Rule</td><td class='p-2 border border-slate-700'>Concave: -f | Convex: +f</td><td class='p-2 border border-slate-700'>Concave: -f | Convex: +f</td></tr><tr><td class='p-2 border border-slate-700 font-bold'>Optical Action</td><td class='p-2 border border-slate-700'>Reflection</td><td class='p-2 border border-slate-700'>Refraction</td></tr></table></div>"
            },
            {
                "title": "Snell's Law & Refractive Index Essentials",
                "content": "<ul class='list-disc pl-5 space-y-1.5 text-slate-300 text-xs sm:text-sm'><li><strong>Snell's Law:</strong> $\\frac{\\sin i}{\\sin r} = n_{21} = \\frac{v_1}{v_2}$.</li><li><strong>Absolute Index:</strong> $n_m = \\frac{c}{v}$. Higher $n \\implies$ slower light velocity $\\implies$ optically denser medium.</li><li><strong>Power:</strong> $P = \\frac{1}{f\\text{ (m)}}$ (Dioptres). Combination: $P = P_1 + P_2 + \\dots$</li><li><strong>Always True:</strong> Both concave mirrors and concave lenses have negative focal lengths ($f < 0$). Convex geometries have positive focal lengths ($f > 0$).</li></ul>"
            }
        ],
        "checkpoints": [
            {
                "q": "Which material from the following options cannot be used to manufacture a functional optical lens?",
                "options": [
                    "Water",
                    "Crown Glass",
                    "Transparent Plastic",
                    "Clay"
                ],
                "ans": 3,
                "solution": "A lens must be made of a transparent optical material through which light can transmit and refract. Clay is completely opaque and cannot transmit light (NCERT Page 159, Exercise Q1)."
            },
            {
                "q": "If one-half of a convex lens is covered with black paper, what happens to the image formed of an illuminated object?",
                "options": [
                    "Only the top half of the image is produced",
                    "A complete image is still formed, but its brightness (intensity) is reduced by half",
                    "The entire image vanishes completely",
                    "The image becomes colored due to chromatic distortion"
                ],
                "ans": 1,
                "solution": "Light rays from every point of the object pass through all parts of the lens. Covering half the lens reduces the light-gathering area by half, so a complete image is still formed, but its intensity (brightness) is halved (NCERT Page 160, Exercise Q9)."
            }
        ],
        "narration": "Here is your Chapter 9 formula cheat-sheet! Keep the minus and plus signs in clear view: mirror formula has a plus in the relation, minus in magnification; lens formula has a minus in the relation, plus in magnification. And remember: clay cannot form a lens, and covering half a lens merely dims the image brightness by half!"
    },
    {
        "id": 21,
        "title": "Complete NCERT Exercises & Problem Solutions (Q1–Q17)",
        "subtitle": "Chapter 9 • Pages 159–160",
        "tag": "All Exercises Q1–Q17",
        "quote": "Thorough solutions to every end-of-chapter NCERT exercise guarantee full exam readiness.",
        "lead": "Step-by-step mathematical derivations and analytical reasoning for all 17 textbook exercises covering reflection, mirrors, refraction, lenses, and power.",
        "theory_blocks": [
            {
                "title": "High-Yield Exercise Solutions (Q1 to Q9)",
                "content": "<div class='space-y-1.5 text-xs text-slate-300'><p><strong>Q1:</strong> Clay cannot make a lens (opaque). <strong>Q2:</strong> Concave mirror virtual erect enlarged $\\implies$ between $P$ and $F$. <strong>Q3:</strong> Convex lens real same size $\\implies$ at $2F_1$. <strong>Q4:</strong> $f = -15\\text{ cm} \\implies$ both concave. <strong>Q5:</strong> Always erect $\\implies$ either plane or convex mirror.</p><p><strong>Q6:</strong> Small dictionary letters $\\implies$ convex lens of short focal length ($f = 5\\text{ cm}$) gives higher magnification ($m \\approx 1 + D/f$).</p><p><strong>Q7:</strong> Concave mirror $f = 15\\text{ cm}$ erect image $\\implies$ object distance range: $0 < u < 15\\text{ cm}$, image is virtual, erect, and larger than object.</p><p><strong>Q8:</strong> (a) Headlights $\\implies$ concave mirror (bulb at $F$ casts parallel beam); (b) Rear-view $\\implies$ convex mirror (erect, wide field); (c) Solar furnace $\\implies$ concave mirror (converges sunlight to high heat).</p></div>"
            },
            {
                "title": "Numerical Exercise Solutions (Q10 to Q17)",
                "content": "<div class='space-y-1.5 text-xs text-slate-300'><p><strong>Q10:</strong> Convex lens $h=5\\text{ cm}, u=-25\\text{ cm}, f=+10\\text{ cm} \\implies v=+16.67\\text{ cm}, h'=-3.33\\text{ cm}$ (real, inverted, diminished).</p><p><strong>Q11:</strong> Concave lens $f=-15\\text{ cm}, v=-10\\text{ cm} \\implies 1/u = 1/(-10) - 1/(-15) = -1/30 \\implies u = -30\\text{ cm}$.</p><p><strong>Q12:</strong> Convex mirror $u=-10\\text{ cm}, f=+15\\text{ cm} \\implies 1/v = 1/15 - 1/(-10) = 5/30 \\implies v = +6\\text{ cm}, m = -v/u = +0.6$ (virtual, erect, diminished).</p><p><strong>Q13:</strong> Plane mirror $m = +1$ means image is virtual, erect, and equal in height to the object ($h'=h$).</p><p><strong>Q14:</strong> Convex mirror $h=5\\text{ cm}, u=-20\\text{ cm}, R=+30\\text{ cm} \\implies f=+15\\text{ cm}, v=+8.57\\text{ cm}, m=+0.43, h'=+2.14\\text{ cm}$.</p><p><strong>Q15:</strong> Concave mirror $h=7\\text{ cm}, u=-27\\text{ cm}, f=-18\\text{ cm} \\implies v=-54\\text{ cm}, h'=-14\\text{ cm}$ (screen placed 54 cm in front, image 2x enlarged).</p><p><strong>Q16:</strong> Power $P = -2.0\\text{ D} \\implies f = 1/(-2.0) = -0.5\\text{ m} = -50\\text{ cm}$, concave lens.</p><p><strong>Q17:</strong> Corrective lens $P = +1.5\\text{ D} \\implies f = 1/(+1.5) = +0.67\\text{ m} = +66.7\\text{ cm}$, converging (convex) lens.</p></div>"
            }
        ],
        "checkpoints": [
            {
                "q": "An object 7.0 cm tall is placed 27 cm in front of a concave mirror of focal length 18 cm. At what distance should a screen be placed to capture a sharp focused image?",
                "options": [
                    "54 cm behind the mirror",
                    "54 cm in front of the mirror ($v = -54\\text{ cm}$)",
                    "18 cm in front of the mirror",
                    "36 cm behind the mirror"
                ],
                "ans": 1,
                "solution": "Here $u = -27\\text{ cm}$ and $f = -18\\text{ cm}$. Using $1/v + 1/u = 1/f \\implies 1/v = 1/(-18) - 1/(-27) = -3/54 + 2/54 = -1/54 \\implies v = -54\\text{ cm}$. The screen must be placed 54 cm in front of the mirror (NCERT Page 160, Exercise Q15)."
            },
            {
                "q": "Which lens would you prefer to use when reading tiny dictionary letters?",
                "options": [
                    "A convex lens of focal length 50 cm",
                    "A concave lens of focal length 50 cm",
                    "A convex lens of focal length 5 cm",
                    "A concave lens of focal length 5 cm"
                ],
                "ans": 2,
                "solution": "A convex lens acts as a magnifying glass. Since magnifying power is inversely proportional to focal length ($m \\approx 1 + D/f$), a convex lens with smaller focal length ($f = 5\\text{ cm}$) delivers significantly greater magnification than one with $f = 50\\text{ cm}$ (NCERT Page 160, Exercise Q6)."
            }
        ],
        "narration": "Congratulations on completing all 21 theory slides of Chapter 9! You now possess every formula, ray rule, sign convention, and solved numerical needed to achieve full marks. Proceed into the four mastery challenge quiz slides to test your mastery!"
    }
]

QUIZ_SLIDES = [
    {
        "id": 22,
        "title": "Mastery Challenge: Reflection & Spherical Mirrors",
        "subtitle": "Quiz Challenge 1 • Questions 1 to 10",
        "tag": "Quiz Part 1",
        "questions": [
            {
                "id": 1,
                "q": "The image formed by a concave mirror is observed to be virtual, erect and larger than the object. Where should the object be positioned?",
                "options": [
                    "Between the principal focus and the centre of curvature",
                    "At the centre of curvature",
                    "Beyond the centre of curvature",
                    "Between the pole of the mirror and its principal focus"
                ],
                "ans": 3,
                "solution": "A concave mirror produces a virtual, erect, and magnified image only when the object is placed inside the focal length — between the pole P and principal focus F (NCERT Page 159, Exercise Q2)."
            },
            {
                "id": 2,
                "q": "No matter how far you stand from a mirror, your image appears erect. The mirror is likely to be:",
                "options": [
                    "Only plane",
                    "Only concave",
                    "Only convex",
                    "Either plane or convex"
                ],
                "ans": 3,
                "solution": "Both plane mirrors and convex mirrors always produce virtual, erect images regardless of object distance (NCERT Page 160, Exercise Q5)."
            },
            {
                "id": 3,
                "q": "If the radius of curvature of a spherical mirror is 32 cm, its focal length is:",
                "options": [
                    "64 cm",
                    "32 cm",
                    "16 cm",
                    "8 cm"
                ],
                "ans": 2,
                "solution": "Focal length $f = R / 2 = 32 / 2 = 16\\text{ cm}$ (NCERT Page 145, Intext Q1)."
            },
            {
                "id": 4,
                "q": "A ray parallel to the principal axis of a concave mirror passes through which point after reflection?",
                "options": [
                    "The centre of curvature C",
                    "The principal focus F",
                    "The pole P",
                    "Infinity along the vertical axis"
                ],
                "ans": 1,
                "solution": "By definition, rays parallel to the principal axis of a concave mirror converge at the principal focus F after reflection (NCERT Page 138, Figure 9.3a)."
            },
            {
                "id": 5,
                "q": "Which type of mirror is used as a reflector in solar furnaces to produce intense thermal heat?",
                "options": [
                    "Convex mirror",
                    "Cylindrical mirror",
                    "Large concave mirror",
                    "Plane mirror"
                ],
                "ans": 2,
                "solution": "Large concave mirrors converge parallel solar radiation into a single concentrated focal point, creating extremely high temperatures in solar furnaces (NCERT Page 140)."
            },
            {
                "id": 6,
                "q": "An object is placed at the centre of curvature C of a concave mirror. The magnification produced is:",
                "options": [
                    "+1",
                    "-1",
                    "+0.5",
                    "-2"
                ],
                "ans": 1,
                "solution": "At the centre of curvature C, the image is formed at C, is real and inverted, and has the same size as the object: $m = -v/u = -(-2f)/(-2f) = -1$ (NCERT Page 138)."
            },
            {
                "id": 7,
                "q": "Why does a convex mirror have a wider field of view than a plane mirror of equal aperture?",
                "options": [
                    "Because its glass has higher chromatic dispersion",
                    "Because it bulges outwards, enabling it to collect rays from a wider angular span",
                    "Because it reflects light into the infrared spectrum",
                    "Because it forms real images on the retina"
                ],
                "ans": 1,
                "solution": "Because convex mirrors curve outwards towards the viewer, they capture light from a substantially wider angle than flat mirrors (NCERT Page 142)."
            },
            {
                "id": 8,
                "q": "According to the New Cartesian Sign Convention, object distance $u$ is:",
                "options": [
                    "Always positive",
                    "Always negative",
                    "Positive for concave, negative for convex",
                    "Zero at the focus"
                ],
                "ans": 1,
                "solution": "Because the object is always placed to the left of the mirror against the direction of incident light, $u$ is universally negative (NCERT Page 142)."
            },
            {
                "id": 9,
                "q": "A real image produced by a concave mirror is inverted. Its height $h'$ must be assigned:",
                "options": [
                    "A positive sign",
                    "A negative sign",
                    "A zero value",
                    "An imaginary number"
                ],
                "ans": 1,
                "solution": "Heights measured downward perpendicular to the principal axis are assigned negative signs under Cartesian conventions ($h' < 0$) (NCERT Page 143)."
            },
            {
                "id": 10,
                "q": "In a rearview mirror on an automobile, a convex mirror has $R = 3.0\\text{ m}$. If a bus is located 5.0 m away, the image is formed:",
                "options": [
                    "1.15 m behind the mirror",
                    "1.15 m in front of the mirror",
                    "3.0 m behind the mirror",
                    "0.23 m in front of the mirror"
                ],
                "ans": 0,
                "solution": "$f = R/2 = +1.50\\text{ m}, u = -5.00\\text{ m}$. Using $1/v = 1/f - 1/u = 1/1.50 - 1/(-5.00) = 6.50/7.50 \\implies v = +1.15\\text{ m}$ (behind mirror) (NCERT Page 144, Example 9.1)."
            }
        ]
    },
    {
        "id": 23,
        "title": "Mastery Challenge: Mirror Numericals & Magnification",
        "subtitle": "Quiz Challenge 2 • Questions 11 to 20",
        "tag": "Quiz Part 2",
        "questions": [
            {
                "id": 11,
                "q": "An object 4.0 cm tall is placed 25 cm in front of a concave mirror of focal length 15 cm. The image height is:",
                "options": [
                    "-6.0 cm",
                    "+6.0 cm",
                    "-2.5 cm",
                    "+4.0 cm"
                ],
                "ans": 0,
                "solution": "$1/v = 1/(-15) - 1/(-25) = -2/75 \\implies v = -37.5\\text{ cm}$. $m = -v/u = -(-37.5)/(-25) = -1.5$. $h' = m \\times h = -1.5 \\times 4.0 = -6.0\\text{ cm}$ (real, inverted, enlarged) (NCERT Page 144, Example 9.2)."
            },
            {
                "id": 12,
                "q": "The magnification produced by a plane mirror is +1. What does this indicate?",
                "options": [
                    "The image is real, inverted, and 1 metre away",
                    "The image is virtual, erect, and identical in height to the object",
                    "The image is diminished to a single focal point",
                    "The image is formed at negative infinity"
                ],
                "ans": 1,
                "solution": "The positive sign indicates a virtual, erect image, while a magnitude of 1 means image height equals object height ($h'=h$) (NCERT Page 160, Exercise Q13)."
            },
            {
                "id": 13,
                "q": "An object is placed at a distance of 10 cm from a convex mirror of focal length 15 cm. The image position $v$ is:",
                "options": [
                    "+6.0 cm behind the mirror",
                    "-6.0 cm in front of the mirror",
                    "+30.0 cm behind the mirror",
                    "-15.0 cm at the focus"
                ],
                "ans": 0,
                "solution": "$u = -10\\text{ cm}, f = +15\\text{ cm}$. $1/v = 1/f - 1/u = 1/15 - 1/(-10) = 5/30 \\implies v = +6.0\\text{ cm}$ (NCERT Page 160, Exercise Q12)."
            },
            {
                "id": 14,
                "q": "A 5.0 cm object is placed 20 cm in front of a convex mirror of radius of curvature 30 cm. What is the image size?",
                "options": [
                    "+2.14 cm",
                    "-2.14 cm",
                    "+5.0 cm",
                    "+8.57 cm"
                ],
                "ans": 0,
                "solution": "$f = +15\\text{ cm}, u = -20\\text{ cm} \\implies 1/v = 1/15 + 1/20 = 7/60 \\implies v = 60/7 = +8.57\\text{ cm}$. $m = -v/u = -8.57/(-20) = +0.4285 \\implies h' = 0.4285 \\times 5.0 = +2.14\\text{ cm}$ (NCERT Page 160, Exercise Q14)."
            },
            {
                "id": 15,
                "q": "We wish to obtain an erect image of an object using a concave mirror of focal length 15 cm. What must be the range of object distance?",
                "options": [
                    "Between 15 cm and 30 cm",
                    "At 30 cm exactly",
                    "Between 0 cm and 15 cm from the mirror",
                    "Beyond 30 cm"
                ],
                "ans": 2,
                "solution": "To obtain an erect image with a concave mirror, the object must be positioned between the pole and the focus: $0 < u < 15\\text{ cm}$ (NCERT Page 160, Exercise Q7)."
            },
            {
                "id": 16,
                "q": "An object 7.0 cm tall is placed 27 cm in front of a concave mirror of focal length 18 cm. The size of the sharp image on the screen is:",
                "options": [
                    "-7.0 cm",
                    "-14.0 cm",
                    "+14.0 cm",
                    "-28.0 cm"
                ],
                "ans": 1,
                "solution": "$1/v = 1/(-18) - 1/(-27) = -1/54 \\implies v = -54\\text{ cm}$. $m = -v/u = -(-54)/(-27) = -2$. $h' = -2 \\times 7.0 = -14.0\\text{ cm}$ (NCERT Page 160, Exercise Q15)."
            },
            {
                "id": 17,
                "q": "A concave mirror produces a 2 times magnified virtual image of an object placed at 5 cm in front of it. What is its focal length?",
                "options": [
                    "-10 cm",
                    "-5 cm",
                    "+10 cm",
                    "-15 cm"
                ],
                "ans": 0,
                "solution": "For virtual image, $m = +2 \\implies -v/u = +2 \\implies v = -2u = -2(-5) = +10\\text{ cm}$. Then $1/f = 1/v + 1/u = 1/10 - 1/5 = -1/10 \\implies f = -10\\text{ cm}$."
            },
            {
                "id": 18,
                "q": "Which mirror will always show a full-length image of a large, tall building?",
                "options": [
                    "A concave mirror",
                    "A small convex mirror",
                    "A plane mirror of any size",
                    "A parabolic mirror"
                ],
                "ans": 1,
                "solution": "A small convex mirror can capture the full-length image of a large distant building or monument due to its wide field of view and diminished virtual image formation (NCERT Page 142, Agra Fort Taj Mahal example)."
            },
            {
                "id": 19,
                "q": "What happens to the focal length of a concave mirror when it is submerged in water?",
                "options": [
                    "It increases by a factor of 1.33",
                    "It decreases by a factor of 1.33",
                    "It remains unchanged because reflection does not depend on the surrounding medium",
                    "It drops to zero"
                ],
                "ans": 2,
                "solution": "The focal length of a spherical mirror depends solely on its geometric radius of curvature ($f = R/2$), independent of the surrounding optical medium."
            },
            {
                "id": 20,
                "q": "If the magnification of a mirror is $m = -0.5$, the image is:",
                "options": [
                    "Virtual, erect, and magnified",
                    "Real, inverted, and diminished to half the object size",
                    "Real, erect, and doubled in size",
                    "Formed behind the mirror at $2F$"
                ],
                "ans": 1,
                "solution": "A negative magnification ($m < 0$) indicates a real and inverted image; a magnitude of $0.5 < 1$ indicates it is diminished to half the object's height (NCERT Page 143)."
            }
        ]
    },
    {
        "id": 24,
        "title": "Mastery Challenge: Refraction, Glass Slab & Snell's Law",
        "subtitle": "Quiz Challenge 3 • Questions 21 to 30",
        "tag": "Quiz Part 3",
        "questions": [
            {
                "id": 21,
                "q": "Light enters from air to glass having refractive index 1.50. What is the speed of light in the glass?",
                "options": [
                    "$3.0 \\times 10^8\\text{ m/s}$",
                    "$2.0 \\times 10^8\\text{ m/s}$",
                    "$2.25 \\times 10^8\\text{ m/s}$",
                    "$1.5 \\times 10^8\\text{ m/s}$"
                ],
                "ans": 1,
                "solution": "$v = c / n = (3.0 \\times 10^8\\text{ m/s}) / 1.50 = 2.0 \\times 10^8\\text{ m/s}$ (NCERT Page 150, Intext Q2)."
            },
            {
                "id": 22,
                "q": "The refractive index of diamond is 2.42. What is the physical meaning of this statement?",
                "options": [
                    "Diamond reflects 2.42% of incident rays",
                    "The speed of light in vacuum is 2.42 times the speed of light in diamond",
                    "Light travels 2.42 times faster in diamond than in air",
                    "The angle of refraction is always 2.42 degrees"
                ],
                "ans": 1,
                "solution": "By definition $n = c/v = 2.42$, which means the speed of light in diamond is $1/2.42$ times (or speed in vacuum is 2.42 times) that in diamond (NCERT Page 150, Intext Q5)."
            },
            {
                "id": 23,
                "q": "You are given kerosene ($n = 1.44$), turpentine ($n = 1.47$), and water ($n = 1.33$). In which medium does light travel fastest?",
                "options": [
                    "Kerosene",
                    "Turpentine",
                    "Water",
                    "Light travels at the same speed in all three"
                ],
                "ans": 2,
                "solution": "Since speed of light $v = c/n$, light travels fastest in the medium with the lowest refractive index — which is water ($n = 1.33$) (NCERT Page 150, Intext Q4)."
            },
            {
                "id": 24,
                "q": "From Table 9.3, identify the medium having the highest optical density and the lowest optical density:",
                "options": [
                    "Highest: Water (1.33), Lowest: Crown glass (1.52)",
                    "Highest: Diamond (2.42), Lowest: Air (1.0003)",
                    "Highest: Ruby (1.71), Lowest: Ice (1.31)",
                    "Highest: Dense flint glass (1.65), Lowest: Alcohol (1.36)"
                ],
                "ans": 1,
                "solution": "Diamond has the highest refractive index (2.42) and highest optical density; Air has the lowest refractive index (1.0003) and lowest optical density (NCERT Page 150, Intext Q3)."
            },
            {
                "id": 25,
                "q": "When a ray of light enters obliquely from glass into air, it bends:",
                "options": [
                    "Towards the normal because air is denser",
                    "Away from the normal because air is optically rarer",
                    "At 90 degrees back into the glass",
                    "Without any deviation"
                ],
                "ans": 1,
                "solution": "Passing from an optically denser medium (glass) into an optically rarer medium (air), light accelerates and bends away from the normal (NCERT Page 147)."
            },
            {
                "id": 26,
                "q": "What is the perpendicular distance between the emergent ray and the incident ray produced through a glass slab called?",
                "options": [
                    "Focal dispersion",
                    "Lateral displacement (or lateral shift)",
                    "Aperture offset",
                    "Refractive divergence"
                ],
                "ans": 1,
                "solution": "The sideward shift between the incident ray produced forward and the parallel emergent ray is termed lateral displacement (NCERT Page 147, Figure 9.10)."
            },
            {
                "id": 27,
                "q": "If the refractive index of water with respect to air ($n_{wa}$) is 4/3, what is the refractive index of air with respect to water ($n_{aw}$)?",
                "options": [
                    "4/3",
                    "3/4 (0.75)",
                    "1.0",
                    "16/9"
                ],
                "ans": 1,
                "solution": "By the reciprocal relation, $n_{12} = 1 / n_{21}$. Thus $n_{aw} = 1 / (4/3) = 3/4 = 0.75$ (NCERT Page 148)."
            },
            {
                "id": 28,
                "q": "Which of the following values of angle of incidence $i$ violates Snell's law formulation?",
                "options": [
                    "$i = 30°$",
                    "$i = 45°$",
                    "$i = 0°$ (normal incidence)",
                    "$i = 60°$"
                ],
                "ans": 2,
                "solution": "Snell's Law is valid for $0^\\circ < i < 90^\\circ$. At normal incidence ($i = 0^\\circ$), $\\sin 0^\\circ = 0$, and the ray simply passes without deviation (NCERT Page 148)."
            },
            {
                "id": 29,
                "q": "A thick glass slab is placed over printed text. The letters appear raised by an amount that depends on:",
                "options": [
                    "The atmospheric humidity only",
                    "The thickness of the slab and the refractive index of the glass",
                    "The colour of the ink only",
                    "The temperature of the room only"
                ],
                "ans": 1,
                "solution": "Apparent shift is given by $\\Delta t = t(1 - 1/n)$, which depends directly on the physical thickness of the slab $t$ and its refractive index $n$ (NCERT Page 145)."
            },
            {
                "id": 30,
                "q": "A lemon kept in water in a glass tumbler appears bigger when viewed from the sides due to:",
                "options": [
                    "Scattering of light",
                    "Refraction of light at the curved glass-water interface",
                    "Total internal reflection inside the seeds",
                    "Diffraction around the rind"
                ],
                "ans": 1,
                "solution": "Refraction at the curved cylindrical interface of the glass tumbler bends light outward, magnifying the apparent size of the lemon (NCERT Page 145)."
            }
        ]
    },
    {
        "id": 25,
        "title": "Mastery Challenge: Spherical Lenses, Power & Combinations",
        "subtitle": "Quiz Challenge 4 • Questions 31 to 40",
        "tag": "Quiz Part 4",
        "questions": [
            {
                "id": 31,
                "q": "Where should an object be placed in front of a convex lens to get a real image of the size of the object?",
                "options": [
                    "At the principal focus of the lens",
                    "At twice the focal length ($2F_1$)",
                    "At infinity",
                    "Between the optical centre and principal focus"
                ],
                "ans": 1,
                "solution": "Placing an object at twice the focal length ($2F_1$) of a convex lens produces a real image of identical dimensions at $2F_2$ (NCERT Page 159, Exercise Q3)."
            },
            {
                "id": 32,
                "q": "A concave lens has focal length of 15 cm. At what distance should an object be placed to form an image at 10 cm from the lens?",
                "options": [
                    "-30 cm (30 cm in front of the lens)",
                    "+30 cm",
                    "-15 cm",
                    "-60 cm"
                ],
                "ans": 0,
                "solution": "For a concave lens, $f = -15\\text{ cm}$ and $v = -10\\text{ cm}$. Using $1/v - 1/u = 1/f \\implies 1/u = 1/v - 1/f = 1/(-10) - 1/(-15) = -1/30 \\implies u = -30\\text{ cm}$ (NCERT Page 156, Example 9.3)."
            },
            {
                "id": 33,
                "q": "A 2.0 cm tall object is placed 15 cm in front of a convex lens of focal length 10 cm. The height of the image is:",
                "options": [
                    "+4.0 cm",
                    "-4.0 cm",
                    "+2.0 cm",
                    "-2.0 cm"
                ],
                "ans": 1,
                "solution": "$1/v = 1/u + 1/f = 1/(-15) + 1/10 = 1/30 \\implies v = +30\\text{ cm}$. $m = v/u = 30/(-15) = -2 \\implies h' = -2 \\times 2.0 = -4.0\\text{ cm}$ (real, inverted, 2x enlarged) (NCERT Page 157, Example 9.4)."
            },
            {
                "id": 34,
                "q": "Define 1 dioptre of power of a lens:",
                "options": [
                    "Power of a lens of focal length 1 centimetre",
                    "Power of a lens of focal length 1 metre ($1\\text{ D} = 1\\text{ m}^{-1}$)",
                    "Power of a lens that magnifies an object by 100 times",
                    "Power of a plane glass slab of infinite focal length"
                ],
                "ans": 1,
                "solution": "One dioptre is the optical power of a lens whose focal length is exactly 1 metre ($1\\text{ D} = 1\\text{ m}^{-1}$) (NCERT Page 158, Intext Q1)."
            },
            {
                "id": 35,
                "q": "A convex lens forms a real, inverted image of a needle at 50 cm from it. If the image is equal to the size of the needle, what is the power of the lens?",
                "options": [
                    "+2.0 D",
                    "+4.0 D",
                    "-4.0 D",
                    "+0.25 D"
                ],
                "ans": 1,
                "solution": "Image equal in size means object and image are at $2f$. Since $v = +50\\text{ cm}$, $2f = 50\\text{ cm} \\implies f = 25\\text{ cm} = +0.25\\text{ m}$. Power $P = 1/f = 1/(+0.25) = +4.0\\text{ D}$ (NCERT Page 158, Intext Q2)."
            },
            {
                "id": 36,
                "q": "Find the focal length of a lens of power -2.0 D. What type of lens is this?",
                "options": [
                    "$f = -0.5\\text{ m} (-50\\text{ cm})$, concave lens",
                    "$f = +0.5\\text{ m} (+50\\text{ cm})$, convex lens",
                    "$f = -2.0\\text{ m}$, cylindrical lens",
                    "$f = +2.0\\text{ m}$, plane mirror"
                ],
                "ans": 0,
                "solution": "$f = 1/P = 1/(-2.0\\text{ D}) = -0.5\\text{ m} = -50\\text{ cm}$. Negative focal length indicates a concave (diverging) lens (NCERT Page 160, Exercise Q16)."
            },
            {
                "id": 37,
                "q": "A combination consists of two thin lenses in contact with powers +2.0 D and +0.25 D. What is the equivalent power of the combination?",
                "options": [
                    "+2.25 D",
                    "+1.75 D",
                    "+0.50 D",
                    "+8.0 D"
                ],
                "ans": 0,
                "solution": "Powers add algebraically: $P = P_1 + P_2 = +2.0\\text{ D} + 0.25\\text{ D} = +2.25\\text{ D}$ (NCERT Page 158, 'More to Know')."
            },
            {
                "id": 38,
                "q": "If one-half of a convex lens is covered with black paper, which statement is experimentally true?",
                "options": [
                    "Half of the image disappears from view",
                    "A full complete image is formed, but with reduced brightness",
                    "The image shifts by twice the focal length",
                    "The image becomes erect and virtual"
                ],
                "ans": 1,
                "solution": "Every portion of the lens forms the complete image. Blocking half the lens area simply cuts the transmitted light by 50%, reducing image brightness without cropping the view (NCERT Page 160, Exercise Q9)."
            },
            {
                "id": 39,
                "q": "A doctor prescribes a corrective lens of power +1.5 D. Is the prescribed lens diverging or converging, and what is its focal length?",
                "options": [
                    "Diverging, $f = -1.5\\text{ m}$",
                    "Converging, $f = +0.67\\text{ m} (+66.7\\text{ cm})$",
                    "Diverging, $f = -0.67\\text{ m}$",
                    "Converging, $f = +1.5\\text{ m}$"
                ],
                "ans": 1,
                "solution": "A positive power ($+1.5\\text{ D}$) denotes a converging (convex) lens. Its focal length is $f = 1/P = 1/(+1.5) = +0.667\\text{ m} = +66.7\\text{ cm}$ (NCERT Page 160, Exercise Q17)."
            },
            {
                "id": 40,
                "q": "An object 5 cm in length is placed 25 cm away from a converging lens of focal length 10 cm. What is the nature and size of the image?",
                "options": [
                    "Virtual, erect, height = +3.33 cm",
                    "Real, inverted, height = -3.33 cm, formed at 16.67 cm on the other side",
                    "Real, inverted, height = -10.0 cm, formed at 50 cm",
                    "Virtual, diminished, height = +1.5 cm"
                ],
                "ans": 1,
                "solution": "$1/v = 1/10 - 1/25 = 3/50 \\implies v = +16.67\\text{ cm}$. $m = v/u = 16.67/(-25) = -0.667$. $h' = -0.667 \\times 5 = -3.33\\text{ cm}$. The image is real, inverted, and diminished (NCERT Page 160, Exercise Q10)."
            }
        ]
    }
]

