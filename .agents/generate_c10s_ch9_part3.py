#!/usr/bin/env python3
"""
Generate Part 3 (Slides 17 to 20: Review & Exercises) for NCERT Class 10 Science Chapter 9: Light - Reflection and Refraction.
Strict requirements:
- Short title: strictly 1-3 words.
- Strictly silent: speech = ""
- 10 comprehensive questions per slide (total 40 questions), each with 4 options, answer index, hint, explanation, and 3 step-by-step solution steps.
- Topics covered:
  - Slide 17: Reflection Mirrors Review (Reflection laws, plane mirrors, concave/convex geometries, ray rules, applications)
  - Slide 18: Mirror Formula Review (Mirror formula 1/v + 1/u = 1/f, sign convention, magnification m = -v/u, numerical calculations)
  - Slide 19: Refraction Lenses Review (Refraction, glass slab lateral shift, Snell's law, refractive index, lens types & image cases)
  - Slide 20: Lens Power Review (Lens formula 1/v - 1/u = 1/f, lens magnification, lens power P = 1/f in dioptres, lens combinations)
"""

import json

SLIDES_PART3 = [
    {
        "id": 17,
        "title": "Reflection Mirrors Review",
        "subtitle": "Comprehensive Review • Reflection Laws, Spherical Mirror Geometries & Ray Tracing",
        "speech": "",
        "objectives": [
            "Test knowledge of the universal laws of reflection and plane mirror image properties.",
            "Assess understanding of spherical mirror anatomical parameters and R = 2f.",
            "Evaluate comprehension of standard ray tracing rules and practical mirror applications."
        ],
        "key_takeaways": [
            "Angle of incidence equals angle of reflection (i = r) for all reflecting surfaces.",
            "For spherical mirrors of small aperture, focal length f equals half the radius of curvature (R = 2f).",
            "Concave mirrors project parallel beams (headlights) and magnify close objects; convex mirrors provide wide rear views."
        ],
        "questions": [
            {
                "question": "A ray of light strikes a spherical concave mirror along the normal to the reflecting surface. What is the angle of reflection?",
                "options": [
                    "90 degrees",
                    "45 degrees",
                    "0 degrees",
                    "180 degrees"
                ],
                "answer": 2,
                "hint": "Normal incidence means the ray travels along the normal line where angle of incidence is zero.",
                "explanation": "At normal incidence, the angle of incidence i is 0°. By the law of reflection (r = i), the angle of reflection is also 0°, causing the ray to retrace its path.",
                "steps": [
                    "Identify that a ray incident along the normal strikes perpendicular to the mirror surface.",
                    "Determine that the angle of incidence i measured relative to the normal is 0°.",
                    "Apply the first law of reflection (r = i = 0°) to find that the angle of reflection is 0°."
                ]
            },
            {
                "question": "The radius of curvature of a spherical mirror is 24 cm. What is the focal length of this mirror?",
                "options": [
                    "48 cm",
                    "12 cm",
                    "24 cm",
                    "6 cm"
                ],
                "answer": 1,
                "hint": "Apply the relationship R = 2f.",
                "explanation": "For mirrors of small aperture, the focal length is half the radius of curvature: f = R / 2 = 24 cm / 2 = 12 cm.",
                "steps": [
                    "Given radius of curvature R = 24 cm.",
                    "Recall the relationship f = R / 2 for spherical mirrors.",
                    "Calculate f = 24 / 2 = 12 cm."
                ]
            },
            {
                "question": "An optical device forms an erect, virtual, and identical-sized image of an object regardless of distance. What is this device?",
                "options": [
                    "Concave mirror",
                    "Plane mirror",
                    "Convex mirror",
                    "Double convex lens"
                ],
                "answer": 1,
                "hint": "Which mirror always yields magnification m = +1?",
                "explanation": "A flat plane mirror always produces an erect, virtual image that is the exact same size as the object (magnification m = +1) at all distances.",
                "steps": [
                    "Note the image characteristics: virtual, erect, and identical size at all distances.",
                    "Convex mirrors always diminish images (m < 1); concave mirrors change size with distance.",
                    "Conclude that only a plane mirror forms an erect image with magnification exactly equal to +1."
                ]
            },
            {
                "question": "In which of the following devices is a concave mirror used to project a powerful parallel beam of light?",
                "options": [
                    "Automobile rear-view mirror",
                    "Searchlights and vehicle headlights",
                    "Street-lighting divergence lamps",
                    "Solar panel photovoltaic cells"
                ],
                "answer": 1,
                "hint": "Placing the bulb at the principal focus of a concave reflector produces parallel reflected rays.",
                "explanation": "When a light source is placed at the focus of a concave mirror, the reflected rays emerge parallel to the principal axis, creating an intense, long-distance beam.",
                "steps": [
                    "Recall the ray tracing rule: rays originating from the focus reflect parallel to the principal axis.",
                    "Identify searchlights, vehicle headlights, and torches as devices requiring parallel light beams.",
                    "Confirm that concave mirrors provide this parallel beam projection."
                ]
            },
            {
                "question": "Where must a dentist hold a concave inspection mirror relative to a patient's tooth to view an enlarged upright image?",
                "options": [
                    "At the center of curvature (C)",
                    "Between the pole (P) and principal focus (F)",
                    "Beyond the center of curvature",
                    "At the principal focus (F)"
                ],
                "answer": 1,
                "hint": "Recall the only object placement for a concave mirror that yields an erect, magnified virtual image.",
                "explanation": "When an object is placed within the focal length (between P and F), a concave mirror forms a virtual, erect, and magnified image behind the mirror.",
                "steps": [
                    "Identify the desired image properties: erect and enlarged (magnified).",
                    "Recall that for a concave mirror, real images are inverted; only the virtual image formed when the object is between P and F is erect.",
                    "Conclude that the mirror must be held such that the tooth lies between the pole and focus."
                ]
            },
            {
                "question": "Why are convex mirrors chosen as driver side-view mirrors on automobiles instead of flat plane mirrors?",
                "options": [
                    "They magnify trailing cars to make them appear very large",
                    "They provide an erect image and a significantly wider panoramic field of view",
                    "They turn incoming headlight beams into laser pulses",
                    "They show images on the screen in reverse black and white"
                ],
                "answer": 1,
                "hint": "Because they curve outward, convex mirrors capture a broader angle of sight.",
                "explanation": "Convex mirrors always produce erect (though diminished) images and curve outwards, giving the driver a much wider field of view than a flat mirror.",
                "steps": [
                    "Identify the safety requirement for driving: observing multiple traffic lanes behind.",
                    "Recognize that outward curvature captures divergent rays from a wide angle.",
                    "Conclude that convex mirrors provide a wider field of view with erect images."
                ]
            },
            {
                "question": "A light ray approaches a concave mirror along a line passing through the principal focus (F). How will it reflect?",
                "options": [
                    "It will retrace its path back through the focus",
                    "It will reflect parallel to the principal axis",
                    "It will reflect through the center of curvature",
                    "It will emerge along the vertical Y-axis"
                ],
                "answer": 1,
                "hint": "This is the optical converse of a ray traveling parallel to the principal axis.",
                "explanation": "According to standard ray tracing rules, an incident ray passing through the principal focus reflects parallel to the principal axis.",
                "steps": [
                    "Recall the second standard ray tracing rule for concave mirrors.",
                    "Any ray passing through or directed toward F strikes the mirror surface and reflects parallel to the principal axis.",
                    "Select the parallel reflection option."
                ]
            },
            {
                "question": "What happens to the focal point of a concave mirror if it is completely submerged in water?",
                "options": [
                    "Its focal length doubles",
                    "Its focal length remains unchanged",
                    "Its focal length becomes negative infinity",
                    "The mirror turns into a plane mirror"
                ],
                "answer": 1,
                "hint": "Does reflection depend on the refractive index of the surrounding medium?",
                "explanation": "The focal length of a spherical mirror depends solely on its geometric radius of curvature (f = R / 2) and the law of reflection (i = r), which does not depend on medium refractive index.",
                "steps": [
                    "Recall that mirror focal length is determined by geometry: f = R / 2.",
                    "The law of reflection (i = r) is independent of the surrounding medium's optical density.",
                    "Conclude that the focal length of a mirror remains unchanged when submerged."
                ]
            },
            {
                "question": "An object is placed at the center of curvature (C) of a concave mirror. Where is the image formed, and what are its properties?",
                "options": [
                    "At infinity, virtual and enlarged",
                    "At C, real, inverted, and of the same size as the object",
                    "Between P and F, erect and magnified",
                    "Behind the mirror, virtual and diminished"
                ],
                "answer": 1,
                "hint": "At C, object distance u = -2f and image distance v = -2f.",
                "explanation": "When an object is placed at the center of curvature C, its real, inverted image forms at C with magnification m = -1 (identical size).",
                "steps": [
                    "Object position: at center of curvature C (u = -2f).",
                    "Using mirror formula: 1/v = 1/f - 1/u = 1/(-f) - 1/(-2f) = -1/2f, giving v = -2f (at C).",
                    "Magnification m = -v/u = -(-2f)/(-2f) = -1, meaning real, inverted, and same size."
                ]
            },
            {
                "question": "In a solar furnace, large concave mirrors focus sunlight to melt metals. Why is the crucible placed at the principal focus?",
                "options": [
                    "Because sunlight rays from infinity are parallel and converge at the principal focus",
                    "Because the focus is the coldest spot on the mirror",
                    "Because the focus absorbs all ultraviolet radiation",
                    "Because light stops moving at the focus"
                ],
                "answer": 0,
                "hint": "Sun rays are parallel incident rays that converge at point F.",
                "explanation": "Solar rays from the distant sun arrive as a parallel beam; upon reflection from a concave mirror, they converge at the principal focus, concentrating intense thermal energy.",
                "steps": [
                    "Sun is at optical infinity, so incoming solar rays are parallel to the principal axis.",
                    "A concave mirror converges all parallel incident rays to its principal focus F.",
                    "Placing the crucible at F concentrates maximum radiant heat energy."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Mirror Formula Review",
        "subtitle": "Comprehensive Review • Mirror Formula, Sign Convention & Numerical Problems",
        "speech": "",
        "objectives": [
            "Apply the mirror formula 1/v + 1/u = 1/f with Cartesian signs.",
            "Calculate image position, height, and magnification (m = -v/u).",
            "Solve worked numerical problems from NCERT Class 10 Chapter 9."
        ],
        "key_takeaways": [
            "Mirror formula: 1/v + 1/u = 1/f.",
            "Linear magnification m = h'/h = -v/u.",
            "Concave focal length is negative; convex focal length is positive; object distance is always negative."
        ],
        "questions": [
            {
                "question": "A convex mirror used for rear-view on an automobile has a radius of curvature of 3.00 m. If a bus is located at 5.00 m from this mirror, where is the image formed?",
                "options": [
                    "+1.15 m behind the mirror",
                    "-1.15 m in front of the mirror",
                    "+3.00 m behind the mirror",
                    "-2.50 m in front of the mirror"
                ],
                "answer": 0,
                "hint": "Recall NCERT Example 9.1: R = +3.00 m -> f = +1.50 m, u = -5.00 m.",
                "explanation": "f = +R/2 = +1.50 m; u = -5.00 m. Using 1/v = 1/f - 1/u = 1/1.50 - 1/(-5.00) = (10/15) + (1/5) = 13/15. Thus v = +15/13 = +1.15 m behind the mirror.",
                "steps": [
                    "Identify given values: R = +3.00 m -> f = +1.50 m; u = -5.00 m.",
                    "Apply mirror formula: 1/v = 1/f - 1/u = 1/(1.5) - 1/(-5) = 1/1.5 + 1/5 = 13/15.",
                    "Calculate v = 15/13 ≈ +1.15 m; positive sign indicates the image is virtual and behind the mirror."
                ]
            },
            {
                "question": "In the previous problem of the convex rear-view mirror (u = -5.00 m, v = +1.15 m), what is the magnification and nature of the bus image?",
                "options": [
                    "m = -0.23, real and inverted",
                    "m = +0.23, virtual and erect",
                    "m = +1.50, virtual and magnified",
                    "m = -2.30, real and enlarged"
                ],
                "answer": 1,
                "hint": "Use magnification m = -v / u.",
                "explanation": "m = -v / u = -(+1.15 m) / (-5.00 m) = +0.23. The positive sign indicates a virtual and erect image; magnitude 0.23 means diminished.",
                "steps": [
                    "Given image distance v = +1.15 m and object distance u = -5.00 m.",
                    "Calculate magnification: m = -v / u = -(1.15) / (-5.00) = +0.23.",
                    "Positive m means virtual and erect; |m| < 1 means diminished in size."
                ]
            },
            {
                "question": "An object 4.0 cm in size is placed at 25.0 cm in front of a concave mirror of focal length 15.0 cm (Example 9.2). At what distance from the mirror should a screen be placed to obtain a sharp image?",
                "options": [
                    "-37.5 cm (37.5 cm in front of the mirror)",
                    "+37.5 cm (37.5 cm behind the mirror)",
                    "-15.0 cm (at the focal point)",
                    "-50.0 cm (at twice the distance)"
                ],
                "answer": 0,
                "hint": "Concave mirror: f = -15.0 cm, u = -25.0 cm. Solve 1/v = 1/f - 1/u.",
                "explanation": "1/v = 1/(-15) - 1/(-25) = -1/15 + 1/25 = -2/75. Therefore, v = -75/2 = -37.5 cm. The screen should be placed 37.5 cm in front of the mirror.",
                "steps": [
                    "Identify values with Cartesian signs: h = +4.0 cm, u = -25.0 cm, f = -15.0 cm.",
                    "Apply mirror formula: 1/v = 1/f - 1/u = -1/15 - (-1/25) = -1/15 + 1/25 = -2/75.",
                    "Invert to solve: v = -75/2 = -37.5 cm; negative sign indicates real image on the same side."
                ]
            },
            {
                "question": "For the object in the previous question (h = +4.0 cm, u = -25.0 cm, v = -37.5 cm), what is the height of the formed image?",
                "options": [
                    "+6.0 cm",
                    "-6.0 cm",
                    "-2.5 cm",
                    "+8.0 cm"
                ],
                "answer": 1,
                "hint": "Use m = h' / h = -v / u, so h' = - (v / u) * h.",
                "explanation": "m = -v / u = -(-37.5) / (-25.0) = -1.5. Then h' = m * h = -1.5 * (+4.0 cm) = -6.0 cm. The negative sign denotes an inverted real image.",
                "steps": [
                    "Calculate magnification: m = -v / u = -(-37.5) / (-25) = -1.5.",
                    "Calculate image height: h' = m × h = -1.5 × 4.0 cm = -6.0 cm.",
                    "Interpret the result: -6.0 cm indicates an inverted, real image of height 6.0 cm."
                ]
            },
            {
                "question": "A concave mirror produces three times magnified (enlarged) real image of an object placed at 10 cm in front of it. Where is the image located?",
                "options": [
                    "-30 cm (30 cm in front of the mirror)",
                    "+30 cm (30 cm behind the mirror)",
                    "-10 cm (at the object point)",
                    "+3.33 cm"
                ],
                "answer": 0,
                "hint": "A real image has negative magnification: m = -3. Apply m = -v / u.",
                "explanation": "Since the image is real, m = -3. Object distance u = -10 cm. Using m = -v/u, we have -3 = -v / (-10) => v = -30 cm.",
                "steps": [
                    "Identify real image magnification: m = -3; object distance u = -10 cm.",
                    "Apply magnification formula: m = -v / u => -3 = -v / (-10).",
                    "Solve for v: -3 = v / 10 => v = -30 cm (30 cm in front of mirror)."
                ]
            },
            {
                "question": "What is the focal length of a concave mirror that forms a real image at 30 cm for an object placed at 10 cm?",
                "options": [
                    "-7.5 cm",
                    "+7.5 cm",
                    "-15.0 cm",
                    "-20.0 cm"
                ],
                "answer": 0,
                "hint": "Use 1/f = 1/v + 1/u with v = -30 cm and u = -10 cm.",
                "explanation": "1/f = 1/(-30) + 1/(-10) = -1/30 - 3/30 = -4/30 = -2/15. Therefore, f = -15/2 = -7.5 cm.",
                "steps": [
                    "Given u = -10 cm and v = -30 cm.",
                    "Apply mirror formula: 1/f = 1/v + 1/u = -1/30 - 1/10 = -4/30.",
                    "Solve for f: f = -30/4 = -7.5 cm."
                ]
            },
            {
                "question": "The magnification produced by a plane mirror is +1. What does this statement mean physically?",
                "options": [
                    "The image is real, inverted, and 1 meter tall",
                    "The image is virtual, erect, and the same size as the object",
                    "The object is moving at 1 meter per second",
                    "The mirror absorbs 100% of incident light"
                ],
                "answer": 1,
                "hint": "Break down the sign (+) and the magnitude (1).",
                "explanation": "The positive sign indicates a virtual and erect image. The numerical value 1 means the size of the image is exactly equal to the size of the object.",
                "steps": [
                    "Analyze the sign: m > 0 indicates an erect, virtual image.",
                    "Analyze the magnitude: |m| = 1 indicates h' = h (identical size).",
                    "Conclude that the image is virtual, erect, and of the same size as the object."
                ]
            },
            {
                "question": "An object is placed at a distance of 10 cm from a convex mirror of focal length 15 cm. Where is the image formed?",
                "options": [
                    "+6 cm behind the mirror",
                    "-6 cm in front of the mirror",
                    "+30 cm behind the mirror",
                    "-30 cm in front of the mirror"
                ],
                "answer": 0,
                "hint": "Convex mirror: f = +15 cm, u = -10 cm. Solve 1/v = 1/f - 1/u.",
                "explanation": "1/v = 1/f - 1/u = 1/(+15) - 1/(-10) = 1/15 + 1/10 = 2/30 + 3/30 = 5/30 = 1/6. Thus v = +6 cm behind the mirror.",
                "steps": [
                    "Assign signs: u = -10 cm, f = +15 cm (convex mirror).",
                    "Apply mirror formula: 1/v = 1/f - 1/u = 1/15 - (-1/10) = 1/15 + 1/10 = 5/30 = 1/6.",
                    "Solve for v: v = +6 cm (virtual image located 6 cm behind the mirror)."
                ]
            },
            {
                "question": "What is the linear magnification for the image in the previous question (u = -10 cm, v = +6 cm)?",
                "options": [
                    "+0.6",
                    "-0.6",
                    "+1.67",
                    "-1.67"
                ],
                "answer": 0,
                "hint": "Apply m = -v / u.",
                "explanation": "m = -v / u = -(+6 cm) / (-10 cm) = +0.6. The positive sign denotes a virtual erect image, diminished to 0.6 of original size.",
                "steps": [
                    "Given v = +6 cm and u = -10 cm.",
                    "Calculate m = -v / u = -(6) / (-10) = +0.6.",
                    "Confirm that the image is virtual, erect, and diminished."
                ]
            },
            {
                "question": "Under what condition will a concave mirror form a virtual image?",
                "options": [
                    "When the object is placed at infinity",
                    "When the object distance (u) is less than the focal length (f)",
                    "When the object is placed beyond the center of curvature (C)",
                    "When the object is placed at the center of curvature (C)"
                ],
                "answer": 1,
                "hint": "Think of the only case where the object is between pole P and focus F.",
                "explanation": "A concave mirror produces a virtual image only when the object is placed between the pole and focus, meaning the object distance u is smaller than the focal length f.",
                "steps": [
                    "Review all six concave mirror image positions.",
                    "For u > f, reflected rays converge in front to form real images.",
                    "For u < f (between P and F), reflected rays diverge, forming a virtual image behind the mirror."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Refraction Lenses Review",
        "subtitle": "Comprehensive Review • Refractive Index, Snell's Law & Spherical Lens Ray Tracing",
        "speech": "",
        "objectives": [
            "Test comprehension of refraction principles, Snell's Law, and refractive index (n = c/v).",
            "Assess understanding of double convex and double concave lens parameters.",
            "Evaluate ray tracing and image formation across convex and concave lenses."
        ],
        "key_takeaways": [
            "Snell's Law: sin i / sin r = constant = n21.",
            "Absolute refractive index n = c/v relates light speed in vacuum to medium.",
            "Convex lens forms real inverted images for u > f, and an erect magnified virtual image for u < f."
        ],
        "questions": [
            {
                "question": "Light enters from air into a glass plate having a refractive index of 1.50. If the speed of light in vacuum is 3 × 10^8 m/s, what is the speed of light in glass?",
                "options": [
                    "1.5 × 10^8 m/s",
                    "2.0 × 10^8 m/s",
                    "2.25 × 10^8 m/s",
                    "3.0 × 10^8 m/s"
                ],
                "answer": 1,
                "hint": "Apply the definition of absolute refractive index: n = c / v.",
                "explanation": "v = c / n = (3.0 × 10^8 m/s) / 1.50 = 2.0 × 10^8 m/s.",
                "steps": [
                    "Given c = 3.0 × 10^8 m/s and n = 1.50.",
                    "Recall formula: n = c / v => v = c / n.",
                    "Calculate v = 3.0 × 10^8 / 1.50 = 2.0 × 10^8 m/s."
                ]
            },
            {
                "question": "The refractive index of water is 1.33 and that of diamond is 2.42. In which medium does light travel faster, and by what factor?",
                "options": [
                    "In diamond, because it has higher optical density",
                    "In water, because lower refractive index corresponds to higher light speed",
                    "At the exact same speed in both substances",
                    "Light cannot travel through diamond at all"
                ],
                "answer": 1,
                "hint": "Speed of light is inversely proportional to refractive index (v = c / n).",
                "explanation": "Since v = c / n, the speed of light is inversely proportional to refractive index. Water has a lower refractive index (1.33 < 2.42), so light travels significantly faster in water.",
                "steps": [
                    "Recall v = c / n: higher n means slower light speed.",
                    "Compare: n(water) = 1.33, n(diamond) = 2.42.",
                    "Conclude that light travels faster in water due to its lower refractive index."
                ]
            },
            {
                "question": "Why does a lemon kept in water in a glass tumbler appear larger than its actual size when viewed from the sides?",
                "options": [
                    "Water chemically reacts with the lemon skin to expand it",
                    "Refraction of light at the curved glass-water interface magnifies the image",
                    "The lemon absorbs all blue light wavelengths",
                    "Total internal reflection duplicates the lemon"
                ],
                "answer": 1,
                "hint": "The curved glass tumbler acts like a magnifying cylindrical lens.",
                "explanation": "Light rays exiting from the denser water-glass medium into air bend away from the normal, creating an enlarged virtual image of the lemon.",
                "steps": [
                    "Identify the medium transition: light travels from water/glass (denser) into air (rarer).",
                    "The rays refract away from the normal at the curved cylindrical boundary.",
                    "The diverged rays reach the eye, which perceives an enlarged virtual image."
                ]
            },
            {
                "question": "A ray of light traveling in water enters obliquely into crown glass (n = 1.52). Does the light ray bend toward or away from the normal?",
                "options": [
                    "Away from the normal",
                    "Toward the normal",
                    "It continues without any deviation",
                    "It reflects backward at 90 degrees"
                ],
                "answer": 1,
                "hint": "Compare the refractive index of water (1.33) with crown glass (1.52).",
                "explanation": "Crown glass (n = 1.52) is optically denser than water (n = 1.33). When light passes from a rarer to a denser medium, it slows down and bends toward the normal.",
                "steps": [
                    "Compare optical densities: n(glass) = 1.52 > n(water) = 1.33.",
                    "Light enters an optically denser medium from an optically rarer medium.",
                    "Recall the rule: rarer to denser -> ray bends toward the normal."
                ]
            },
            {
                "question": "Where should an illuminated object be placed in front of a convex lens to produce a real image of the same size as the object?",
                "options": [
                    "At the principal focus (F1)",
                    "At twice the focal length (2F1)",
                    "At infinity",
                    "Between the optical center and focus"
                ],
                "answer": 1,
                "hint": "Check Table 9.4 for symmetric real image formation at 2F2.",
                "explanation": "When an object is placed at twice the focal length (2F1) of a convex lens, refracted rays converge at 2F2 to form a real, inverted image of the same size.",
                "steps": [
                    "Recall the 6 image formation scenarios for a convex lens.",
                    "Placing object at 2F1 yields image at 2F2.",
                    "Image properties: real, inverted, same size (magnification m = -1)."
                ]
            },
            {
                "question": "Which of the following optical materials cannot be used to make a functional spherical lens?",
                "options": [
                    "Water",
                    "Glass",
                    "Clear transparent plastic",
                    "Clay"
                ],
                "answer": 3,
                "hint": "A lens must be made of a transparent optical material.",
                "explanation": "Clay is completely opaque and does not transmit light rays; therefore, it cannot be used to fabricate an optical lens.",
                "steps": [
                    "Define a lens: a transparent optical medium bounded by at least one spherical surface.",
                    "Water, glass, and clear plastic are transparent to visible light.",
                    "Clay is opaque, absorbing and blocking light, so it cannot form a lens."
                ]
            },
            {
                "question": "A ray of light traveling parallel to the principal axis strikes a double concave lens. How does it emerge after refraction?",
                "options": [
                    "It passes directly through the second focus F2",
                    "It appears to diverge from the first principal focus F1",
                    "It turns back into the incident beam",
                    "It travels straight down along the normal"
                ],
                "answer": 1,
                "hint": "A concave lens is a diverging lens.",
                "explanation": "In a concave lens, incident rays parallel to the principal axis diverge outward such that their backward extensions appear to emanate from the principal focus F1.",
                "steps": [
                    "Identify the lens: double concave (diverging lens).",
                    "Recall ray tracing rule 1 for concave lenses.",
                    "Incident parallel rays diverge away, appearing to originate from focus F1."
                ]
            },
            {
                "question": "You wish to observe a magnified, upright virtual image of small print in a dictionary. Which lens should you select?",
                "options": [
                    "A convex lens of focal length 5 cm",
                    "A concave lens of focal length 5 cm",
                    "A convex lens of focal length 50 cm",
                    "A concave lens of focal length 50 cm"
                ],
                "answer": 0,
                "hint": "A magnifying glass requires a convex lens with short focal length for higher power and magnification.",
                "explanation": "A convex lens of short focal length (f = 5 cm) provides high magnifying power (P = 1/f = 20 D) and produces an enlarged upright virtual image when held close to print.",
                "steps": [
                    "Magnification requires a convex lens (concave lenses always diminish images).",
                    "Shorter focal length gives higher optical power (P = 1/f) and greater angular magnification.",
                    "Therefore, choose a convex lens with the shorter focal length (5 cm)."
                ]
            },
            {
                "question": "In an experiment with a rectangular glass slab, if the angle of incidence is 45 degrees, what can be deduced about the angle of emergence?",
                "options": [
                    "Angle of emergence is 0 degrees",
                    "Angle of emergence equals 45 degrees",
                    "Angle of emergence is 90 degrees",
                    "Angle of emergence is 22.5 degrees"
                ],
                "answer": 1,
                "hint": "The emergent ray is parallel to the incident ray across parallel slab boundaries.",
                "explanation": "Because opposite faces of the rectangular glass slab are parallel, the angle of emergence strictly equals the angle of incidence: angle e = angle i = 45°.",
                "steps": [
                    "Opposite faces of the glass slab are parallel.",
                    "The deviation at the first interface is canceled by equal and opposite deviation at the second interface.",
                    "Thus, the angle of emergence e equals the angle of incidence i = 45°."
                ]
            },
            {
                "question": "What is the nature of the image formed by a convex lens when an illuminated candle is placed between its optical center (O) and principal focus (F1)?",
                "options": [
                    "Real, inverted, and magnified",
                    "Virtual, erect, and magnified on the same side as the object",
                    "Real, inverted, and diminished",
                    "Virtual, inverted, and point-sized"
                ],
                "answer": 1,
                "hint": "This is the classic magnifying glass configuration.",
                "explanation": "When the object distance is less than the focal length (u < f), refracted rays diverge on the opposite side; their backward projections form an erect, magnified virtual image on the same side.",
                "steps": [
                    "Object placement: between O and F1 (u < f).",
                    "Refracted rays emerge diverging, so they cannot intersect to form a real image.",
                    "Backward ray extensions intersect on the same side of the lens, creating an erect, magnified virtual image."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Lens Power Review",
        "subtitle": "Comprehensive Review • Lens Formula, Dioptres, Corrective Eyewear & Net Power",
        "speech": "",
        "objectives": [
            "Calculate object and image parameters using 1/v - 1/u = 1/f.",
            "Determine optical power of thin lenses using P = 1 / f (in meters).",
            "Calculate net optical power for combinations of thin lenses in contact."
        ],
        "key_takeaways": [
            "Lens formula: 1/v - 1/u = 1/f; Lens magnification: m = +v/u.",
            "Optical power P = 1/f (in meters); unit is Dioptre (D).",
            "Net power of lenses in contact is the algebraic sum: P = P1 + P2 + P3 + ..."
        ],
        "questions": [
            {
                "question": "A concave lens has a focal length of 15 cm. At what distance should an object be placed from the lens so that it forms an image at 10 cm from the lens?",
                "options": [
                    "-30 cm (30 cm in front of the lens)",
                    "+30 cm (30 cm behind the lens)",
                    "-20 cm",
                    "-50 cm"
                ],
                "answer": 0,
                "hint": "Concave lens: f = -15 cm, v = -10 cm. Apply 1/v - 1/u = 1/f.",
                "explanation": "1/u = 1/v - 1/f = 1/(-10) - 1/(-15) = -1/10 + 1/15 = -3/30 + 2/30 = -1/30. Thus u = -30 cm (30 cm in front of the lens).",
                "steps": [
                    "Assign signs: f = -15 cm, v = -10 cm (concave lens forms virtual image on the same side).",
                    "Apply lens formula: 1/v - 1/u = 1/f => 1/u = 1/v - 1/f = -1/10 - (-1/15) = -1/10 + 1/15.",
                    "Solve for u: 1/u = -1/30 => u = -30 cm."
                ]
            },
            {
                "question": "What is the magnification produced by the concave lens in the previous question (u = -30 cm, v = -10 cm)?",
                "options": [
                    "+0.33",
                    "-0.33",
                    "+3.00",
                    "-3.00"
                ],
                "answer": 0,
                "hint": "For lenses, magnification m = +v / u.",
                "explanation": "m = v / u = (-10 cm) / (-30 cm) = +1/3 ≈ +0.33. The positive sign indicates a virtual erect image, one-third the size of the object.",
                "steps": [
                    "Given image distance v = -10 cm and object distance u = -30 cm.",
                    "Apply lens magnification formula: m = +v / u = (-10) / (-30) = +1/3 ≈ +0.33.",
                    "Positive m confirms the image is virtual, erect, and diminished."
                ]
            },
            {
                "question": "A 2.0 cm tall object is placed perpendicular to the principal axis of a convex lens of focal length 10 cm at a distance of 15 cm. Where is the image formed?",
                "options": [
                    "+30 cm behind the lens",
                    "-30 cm in front of the lens",
                    "+10 cm",
                    "-15 cm"
                ],
                "answer": 0,
                "hint": "Convex lens: f = +10 cm, u = -15 cm. Solve 1/v = 1/f + 1/u.",
                "explanation": "1/v = 1/f + 1/u = 1/(+10) + 1/(-15) = 1/10 - 1/15 = 3/30 - 2/30 = 1/30. Therefore, v = +30 cm (30 cm on the other side of the lens).",
                "steps": [
                    "Assign signs: h = +2.0 cm, f = +10 cm, u = -15 cm.",
                    "Apply lens formula: 1/v - 1/u = 1/f => 1/v = 1/f + 1/u = 1/10 - 1/15 = 1/30.",
                    "Solve for v: v = +30 cm (real image formed 30 cm behind the lens)."
                ]
            },
            {
                "question": "What is the size and nature of the image formed in the previous question (h = +2.0 cm, u = -15 cm, v = +30 cm)?",
                "options": [
                    "h' = -4.0 cm, real and inverted",
                    "h' = +4.0 cm, virtual and erect",
                    "h' = -1.0 cm, real and diminished",
                    "h' = +2.0 cm, virtual and same size"
                ],
                "answer": 0,
                "hint": "m = v / u = h' / h.",
                "explanation": "m = v / u = (+30) / (-15) = -2. Then h' = m * h = -2 * 2.0 cm = -4.0 cm. The negative sign denotes a real, inverted, magnified image.",
                "steps": [
                    "Calculate magnification: m = v / u = 30 / (-15) = -2.",
                    "Calculate image height: h' = m × h = -2 × 2.0 cm = -4.0 cm.",
                    "Conclude that the image is real, inverted, and magnified (4.0 cm tall)."
                ]
            },
            {
                "question": "Define the SI unit of power of a lens (1 dioptre).",
                "options": [
                    "The power of a lens having a focal length of 1 centimeter",
                    "The power of a lens having a focal length of 1 meter",
                    "The power of a lens having a focal length of 100 meters",
                    "The power of a flat glass plate with infinite focal length"
                ],
                "answer": 1,
                "hint": "Use P = 1 / f with f = 1 meter.",
                "explanation": "One dioptre is formally defined as the power of a lens whose focal length is exactly 1 meter (1 D = 1 m⁻¹).",
                "steps": [
                    "Recall formula: P = 1 / f, where f is in meters.",
                    "Substitute f = 1 meter: P = 1 / 1 m = 1 m⁻¹ = 1 Dioptre (1 D).",
                    "Select the 1 meter focal length definition."
                ]
            },
            {
                "question": "A doctor prescribes a corrective lens of power -2.5 D. What is the focal length and type of this lens?",
                "options": [
                    "f = -40 cm, concave (diverging) lens",
                    "f = +40 cm, convex (converging) lens",
                    "f = -25 cm, concave lens",
                    "f = +25 cm, convex lens"
                ],
                "answer": 0,
                "hint": "f = 1 / P. Negative power means a concave lens.",
                "explanation": "f = 1 / P = 1 / (-2.5 D) = -0.40 m = -40 cm. The negative sign confirms that this is a diverging concave lens (used to correct myopia).",
                "steps": [
                    "Given P = -2.5 D.",
                    "Calculate focal length in meters: f = 1 / P = 1 / (-2.5) = -0.40 m.",
                    "Convert to centimeters: -0.40 m = -40 cm; negative sign indicates a concave lens."
                ]
            },
            {
                "question": "Find the focal length of a lens of power +2.0 D. What type of lens is it?",
                "options": [
                    "+0.5 m (+50 cm), convex lens",
                    "-0.5 m (-50 cm), concave lens",
                    "+2.0 m (+200 cm), convex lens",
                    "-2.0 m (-200 cm), concave lens"
                ],
                "answer": 0,
                "hint": "f = 1 / P with P = +2.0 D.",
                "explanation": "f = 1 / P = 1 / (+2.0 D) = +0.5 m = +50 cm. Positive focal length and power designate a converging convex lens (used to correct hypermetropia).",
                "steps": [
                    "Given P = +2.0 D.",
                    "Calculate f = 1 / P = 1 / 2.0 = +0.5 m = +50 cm.",
                    "Positive power indicates a convex (converging) lens."
                ]
            },
            {
                "question": "An optician places two thin lenses in close contact with powers +3.0 D and -1.0 D. What is the net focal length of the combination?",
                "options": [
                    "+50 cm (+0.5 m)",
                    "-50 cm (-0.5 m)",
                    "+25 cm (+0.25 m)",
                    "+20 cm (+0.2 m)"
                ],
                "answer": 0,
                "hint": "Calculate net power P = P1 + P2, then find f = 1 / P.",
                "explanation": "Total power P = P1 + P2 = +3.0 D + (-1.0 D) = +2.0 D. Net focal length f = 1 / P = 1 / 2.0 = +0.5 m = +50 cm.",
                "steps": [
                    "Add individual lens powers: P = P1 + P2 = +3.0 D + (-1.0 D) = +2.0 D.",
                    "Calculate net focal length: f = 1 / P = 1 / (+2.0) = +0.5 m.",
                    "Convert to centimeters: +0.5 m = +50 cm."
                ]
            },
            {
                "question": "A convex lens of focal length 20 cm is placed in contact with a concave lens of focal length 25 cm. What is the net power of the combination?",
                "options": [
                    "+1.0 D",
                    "-1.0 D",
                    "+9.0 D",
                    "-9.0 D"
                ],
                "answer": 0,
                "hint": "Convert focal lengths to meters: f1 = +0.20 m, f2 = -0.25 m. Find P1, P2 and sum them.",
                "explanation": "P1 = 1 / (+0.20 m) = +5.0 D; P2 = 1 / (-0.25 m) = -4.0 D. Combined power P = P1 + P2 = +5.0 D - 4.0 D = +1.0 D.",
                "steps": [
                    "Find power of convex lens: f1 = +20 cm = +0.2 m => P1 = 1 / 0.2 = +5.0 D.",
                    "Find power of concave lens: f2 = -25 cm = -0.25 m => P2 = 1 / (-0.25) = -4.0 D.",
                    "Calculate total power: P = P1 + P2 = +5.0 D + (-4.0 D) = +1.0 D."
                ]
            },
            {
                "question": "A student projects the real image of a distant tree onto a white screen using a convex lens. What does the measured distance between the screen and the lens represent?",
                "options": [
                    "The diameter of the lens aperture",
                    "The approximate focal length of the convex lens",
                    "Twice the focal length of the convex lens",
                    "The height of the distant tree"
                ],
                "answer": 1,
                "hint": "Light from distant objects (infinity) converges at the focal point.",
                "explanation": "Light rays from a distant tree arrive parallel to the principal axis and converge at the principal focus F2 on the screen; therefore, the lens-to-screen distance is the focal length f.",
                "steps": [
                    "Distant object is at optical infinity (u ≈ ∞).",
                    "Refracted parallel rays converge to form a sharp real image at the principal focus F2.",
                    "The distance between the optical center of the lens and the screen is the focal length f."
                ]
            }
        ]
    }
]

if __name__ == "__main__":
    print("=== CHECKING SLIDES 17 TO 20 DATA ===")
    for s in SLIDES_PART3:
        title_words = len(s["title"].split())
        print(f"Slide {s['id']}: '{s['title']}' | Title words: {title_words} | Questions: {len(s['questions'])} | Speech: '{s['speech']}'")
        assert title_words <= 3, f"Title has >3 words: {s['title']}"
        assert s["speech"] == "", f"Slide {s['id']} should be silent!"
        assert len(s["questions"]) == 10, f"Slide {s['id']} must have exactly 10 questions!"
        for q in s["questions"]:
            assert len(q["options"]) == 4, f"Question options != 4: {q['question']}"
            assert 0 <= q["answer"] <= 3, f"Invalid answer index: {q['answer']}"
            assert len(q["steps"]) == 3, f"Steps count != 3: {q['question']}"

    with open(".agents/c10s_ch9_part3.json", "w", encoding="utf-8") as f:
        json.dump(SLIDES_PART3, f, indent=2)
    print("Saved .agents/c10s_ch9_part3.json successfully!")
