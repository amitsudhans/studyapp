#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 9: Some Applications of Trigonometry
Data Generator - Part 1 (Slides 1 to 8)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each (spoken-friendly plain math phrasing)
- Checkpoints: Exactly 2 per slide with 4 options each
- Zero fictional human character names (no Raghav, Raj, Sonia, etc.), zero lecturer personas
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Line Of Sight",
        "subtitle": "Indirect Measurement Principles, Horizontal Eye Level & Straight Ray of Observation (Section 9.1)",
        "speech": (
            "Welcome, curious math explorers, to NCERT Class Ten Mathematics Chapter Nine: Some Applications of Trigonometry! Now we take every sine, cosine, and tangent ratio you mastered earlier in Chapter Eight outdoors into the open sky, towering monuments, wide river bridges, and distant ships at sea! "
            "How do skilled land surveyors measure towering skyscrapers or ocean ships safely without physically climbing tall walls or swimming across water with measuring tapes? By sketching crystal clear right angled triangles built strictly around ONE foundational geometry concept called the LINE OF SIGHT! "
            "Let us define the Line of Sight accurately: it is the straight geometric ray drawn directly from an observer's eye cleanly to the exact target point on the object being viewed! "
            "Whenever you measure ANY viewing angle in field trigonometry, pause and trace ONE golden reference line first right away: the HORIZONTAL LEVEL stretching straight forward parallel to the flat ground right at the observer's exact eye height! "
            "Warning, never measure elevation or depression against a vertical tower wall by mistake! EVERY elevation and depression angle is ALWAYS measured directly between that horizontal eye line and the slanted line of sight! Master this visual geometry rule completely first!"
        ),
        "checkpoints": [
            {
                "question": "In Chapter 9 Heights and Distances, what is the exact definition of the 'Line of Sight'?",
                "options": [
                    "The straight line drawn from the eye of an observer to the point in the object viewed by the observer",
                    "The vertical height of a building",
                    "The horizontal ground shadow cast by a tree",
                    "The curved arc connecting two ships"
                ],
                "answer": 0,
                "hint": "Trace the straight ray running directly from the viewer's eye to the target point!",
                "explanation": "Line of sight connects the observer's eye directly to the viewed point along a straight ray."
            },
            {
                "question": "Against which reference direction are BOTH the angle of elevation and angle of depression ALWAYS measured?",
                "options": [
                    "The horizontal level passing through the observer's eye",
                    "The vertical tower axis directly upward",
                    "The slanted ladder only",
                    "South-west compass direction"
                ],
                "answer": 0,
                "hint": "Look straight ahead level with the ground first before tilting your gaze up or down!",
                "explanation": "Both angles lie strictly between the horizontal eye-level line and the oblique line of sight."
            }
        ]
    },
    {
        "id": 2,
        "title": "Angle Of Elevation",
        "subtitle": "Looking Upward Above Horizontal Level & Solving Tower Heights (Textbook Example 1)",
        "speech": (
            "Now tilt your gaze cleanly UPWARD above horizontal eye level! Whenever the viewed object sits strictly ABOVE the observer's horizontal eye level, forcing the observer to tilt their head upward and look up at the sky, the angle formed smoothly between the horizontal level and the upward line of sight is called the ANGLE OF ELEVATION! "
            "Watch Textbook Example One unfold cleanly step by step! A tall vertical tower stands upright on flat level ground. From an observation point marked directly on flat ground sitting exactly fifteen meters away from the foot of the tower, the angle of elevation measured up to the top of the tower equals sixty degrees! Find the full vertical height of the tower! "
            "Ask yourself immediately right away: which trigonometric ratio connects our KNOWN horizontal adjacent ground distance fifteen meters cleanly to our UNKNOWN vertical opposite height h? Tangent! "
            "Write tangent sixty degrees equals vertical height h divided by adjacent ground base fifteen! Recall directly from Chapter Eight Table Eight Point One that tangent sixty equals exact root three! Multiplying both sides cleanly yields exact tower height h equals fifteen root three meters, approximately twenty five point nine eight meters in total!"
        ),
        "checkpoints": [
            {
                "question": "When is the angle formed by a line of sight with the horizontal called an 'Angle of Elevation'?",
                "options": [
                    "When the viewed object lies ABOVE the horizontal level, requiring the observer to look upward",
                    "When the viewed object lies BELOW the horizontal level",
                    "When looking straight downward from a cliff",
                    "Only when the angle equals 90°"
                ],
                "answer": 0,
                "hint": "Think of the word 'elevate' — lifting your gaze upward above eye level!",
                "explanation": "Looking upward toward an elevated object above horizontal eye level forms an Angle of Elevation."
            },
            {
                "question": "A tower stands vertically on the ground. From a point 15 m away from its foot, the angle of elevation of its top is 60° (Example 1). Find the tower height:",
                "options": [
                    "15√3 m",
                    "15 / √3 m",
                    "30 m",
                    "15 m"
                ],
                "answer": 0,
                "hint": "Use tan 60° = Opposite Height / Adjacent Base = h / 15!",
                "explanation": "tan 60° = √3 = h / 15 ⟹ h = 15√3 m (≈ 25.98 m)."
            }
        ]
    },
    {
        "id": 3,
        "title": "Angle Of Depression",
        "subtitle": "Looking Downward Below Horizontal Level & Applying Alternate Interior Angles",
        "speech": (
            "Now climb straight up onto a high building balcony, tall sea lighthouse, or river bridge and tilt your eyes DOWNWARD! Whenever the viewed target object sits strictly BELOW the observer's horizontal eye level, requiring the observer to look downward, the angle formed between the horizontal ray at the top and the downward line of sight is called the ANGLE OF DEPRESSION! "
            "Watch out carefully for the classic Angle of Depression exam trap! Students frequently draw the angle of depression INSIDE the vertical wall instead of touching the horizontal sky line at the top! Remember strictly: BOTH elevation and depression angles ALWAYS touch HORIZONTAL lines! "
            "How do you safely transfer that top angle of depression straight down inside your bottom ground right triangle cleanly? By using parallel horizontal lines and Class Nine ALTERNATE INTERIOR ANGLES! Because the top horizontal eye line runs strictly parallel to the flat bottom ground, the downward line of sight cuts straight across both horizontal lines like a clean Z transversal! "
            "Therefore, the Angle of Depression measured downward from the top ALWAYS equals the corresponding Angle of Elevation looking right back up from the bottom ground object! Zero confusion, total geometric accuracy!"
        ),
        "checkpoints": [
            {
                "question": "How is the Angle of Depression safely transferred into the right triangle resting on the ground below?",
                "options": [
                    "Using Alternate Interior Angles between the upper horizontal eye line and the parallel ground line",
                    "Subtracting the depression angle from 360°",
                    "Doubling the angle of depression",
                    "Adding 90° to the depression angle"
                ],
                "answer": 0,
                "hint": "Remember Class 9 parallel lines cut by a transversal (Z-angles are equal)!",
                "explanation": "Upper horizontal ∥ ground level makes the depression angle from top equal to the elevation angle at the object."
            },
            {
                "question": "Which statement describes an Angle of Depression accurately?",
                "options": [
                    "Angle between the upper horizontal level and downward line of sight when viewing an object BELOW horizontal level",
                    "Angle between a vertical lighthouse wall and the line of sight",
                    "Angle formed when looking straight upward at an airplane",
                    "Angle inside an obtuse triangle only"
                ],
                "answer": 0,
                "hint": "Every viewing angle starts from the horizontal line at the observer's eye!",
                "explanation": "Depression occurs when looking downward below horizontal eye level, measured from the upper horizontal line."
            }
        ]
    },
    {
        "id": 4,
        "title": "Observer Height Offset",
        "subtitle": "Subtracting & Adding Eye Height (1.5 m) in Chimney (Example 3) & Walking Building (Ex 9.1 Q6)",
        "speech": (
            "Never forget real human observers standing on flat ground always have non zero eye height above ground level! Unless a problem explicitly treats the observer as a zero height point right on the ground floor, you MUST account cleanly for Observer Eye Height! "
            "Study Textbook Example Three closely: An observer measuring exactly one point five meters tall stands twenty eight point five meters away from a vertical chimney! The angle of elevation measured from the observer's eyes straight up to the top of the chimney equals forty five degrees! "
            "Wait, does our trigonometry right triangle reach all the way down to the ground? NO! Its horizontal base sits at eye level one point five meters ABOVE flat ground! Tangent forty five equals one, making vertical rise above eye level equal twenty eight point five meters! "
            "Always add observer eye height back cleanly at the end: total chimney height equals twenty eight point five plus one point five equals exact thirty meters! "
            "The exact same rule crushes Exercise Nine Point One Question Six cleanly: subtract eye height one point five meters first from thirty meters to get net vertical tower rise twenty eight point five meters!"
        ),
        "checkpoints": [
            {
                "question": "An observer 1.5 m tall stands 28.5 m away from a chimney. Angle of elevation from eye level to the top is 45° (Example 3). Find full chimney height:",
                "options": [
                    "30 m   (28.5 m above eye level + 1.5 m observer height)",
                    "28.5 m",
                    "27 m",
                    "31.5 m"
                ],
                "answer": 0,
                "hint": "Compute vertical rise = 28.5 × tan 45° = 28.5 m, then DON'T forget observer eye height 1.5 m!",
                "explanation": "Total height = 28.5 tan 45° + 1.5 = 28.5 + 1.5 = 30 m."
            },
            {
                "question": "A 1.5 m tall student walks toward a 30 m tall building as elevation from eyes changes from 30° to 60° (Ex 9.1 Q6). What vertical height forms the right triangles?",
                "options": [
                    "28.5 m   (= 30 m − 1.5 m)",
                    "30 m",
                    "31.5 m",
                    "15 m"
                ],
                "answer": 0,
                "hint": "Subtract eye height (1.5 m) from full building height (30 m)!",
                "explanation": "Horizontal eye line sits 1.5 m above ground, leaving net vertical height 30 − 1.5 = 28.5 m."
            }
        ]
    },
    {
        "id": 5,
        "title": "Pole And Ladder",
        "subtitle": "Solving Hypotenuse Lengths Using sin & cos (Example 2 Electrician & Ex 9.1 Q1 Circus Rope)",
        "speech": (
            "Notice so far tangent worked great when connecting opposite vertical height and adjacent horizontal distance! Yet what happens when an exercise asks directly for the slanted HYPOTENUSE, like a tilted climbing ladder or a tightly stretched circus rope? Immediately switch cleanly to SINE or COSINE! "
            "Test Textbook Example Two first: an electrician must repair an electrical fault on a tall five meter electric pole, climbing a ladder placed to reach a point one point three meters BELOW the very top of the pole! "
            "First subtract carefully from top: vertical climbing height equals five minus one point three equals exact three point seven meters! Inclined at sixty degrees to horizontal ground, what ladder length does the worker need? Because we know Opposite three point seven and want Hypotenuse ladder length L, pick SINE sixty degrees! "
            "Write root three over two equals three point seven over L, solving cleanly to L equals seven point four divided by one point seven three equals four point two eight meters, while foot distance uses cot sixty equals two point one four meters! "
            "Similarly in Exercise Question One, solving a twenty meter circus rope inclined at exact thirty degrees gives pole height ten meters!"
        ),
        "checkpoints": [
            {
                "question": "A circus artist climbs a 20 m long tightly stretched rope tied from ground to top of a vertical pole making 30° with ground (Ex 9.1 Q1). Find pole height:",
                "options": [
                    "10 m",
                    "10√3 m",
                    "20√3 m",
                    "40 m"
                ],
                "answer": 0,
                "hint": "Link vertical pole height (Opposite) with rope length 20 m (Hypotenuse) via sin 30°!",
                "explanation": "sin 30° = h / 20 ⟹ 1/2 = h / 20 ⟹ h = 10 m."
            },
            {
                "question": "An electrician needs to reach 1.3 m below the top of a 5 m pole using a ladder inclined at 60° (Example 2). What exact vertical opposite side enters sin 60°?",
                "options": [
                    "3.7 m   (= 5 m − 1.3 m)",
                    "5 m",
                    "6.3 m",
                    "1.3 m"
                ],
                "answer": 0,
                "hint": "The ladder stops 1.3 m below the top of the 5 m pole!",
                "explanation": "Vertical height reached = 5 − 1.3 = 3.7 m; ladder length = 3.7 / sin 60° ≈ 4.28 m."
            }
        ]
    },
    {
        "id": 6,
        "title": "Broken Storm Tree",
        "subtitle": "Finding Original Full Tree Height by Adding Standing Opposite + Bent Hypotenuse (Ex 9.1 Q2)",
        "speech": (
            "Now inspect one of Exercise Nine Point One's all time favorite puzzles where students lose half marks from stopping halfway: Question Two, the Storm Broken Tree Problem! "
            "During a fierce monsoon windstorm, a tall upright tree snaps partway up its wooden trunk, and the broken upper section bends cleanly downward without detaching, touching the flat ground eight meters away from the tree foot at an elevation angle of thirty degrees! Find the ORIGINAL total height of the living tree before the storm! "
            "Pause and visualize BOTH pieces that once stood vertically straight! Piece One is the unbroken standing bottom stump BD sitting opposite thirty degrees! Piece Two is the snapped upper trunk segment AD leaning diagonally across as the slanted HYPOTENUSE! "
            "Never stop after finding ONLY Piece One! Compute standing leg BD using tangent thirty equals BD over eight, giving BD equals eight divided by root three meters! Next compute bent hypotenuse AD using cosine thirty equals eight divided by AD, giving AD equals sixteen divided by root three meters! "
            "Add BOTH pieces cleanly: eight over root three plus sixteen over root three equals twenty four over root three equals eight root three meters total!"
        ),
        "checkpoints": [
            {
                "question": "A tree breaks due to storm and the broken top touches the ground 8 m from the foot making 30° with ground (Ex 9.1 Q2). What is the ORIGINAL tree height?",
                "options": [
                    "8√3 m   [Standing 8/√3 + Bent Hypotenuse 16/√3 = 24/√3]",
                    "8 / √3 m",
                    "16 / √3 m",
                    "16 m"
                ],
                "answer": 0,
                "hint": "Full original height = vertical stump BD + bent hypotenuse AD!",
                "explanation": "BD = 8 tan 30° = 8/√3 and AD = 8 / cos 30° = 16/√3; sum = 24/√3 = 8√3 m."
            },
            {
                "question": "In the broken-tree triangle, why is cosine 30° = 8 / Hypotenuse needed in addition to tangent 30°?",
                "options": [
                    "Because the upper part of the original vertical tree became the slanted hypotenuse AD after snapping",
                    "Because the tree grew sideways",
                    "Because ground distance 8 m equals tree height",
                    "Because tangent includes hypotenuse"
                ],
                "answer": 0,
                "hint": "Imagine lifting the broken slanted piece AD straight back up on top of stump BD!",
                "explanation": "Before breaking, total tree height was standing stump BD plus broken upper section AD (the hypotenuse)."
            }
        ]
    },
    {
        "id": 7,
        "title": "Two Slides Park",
        "subtitle": "Applying Sine Ratio to Contractor Park Slides (Ex 9.1 Q3) & Kite String Lengths (Ex 9.1 Q5)",
        "speech": (
            "Practice applying SINE ratio directly across two crisp real world engineering designs from Exercise Nine Point One Questions Three and Five! "
            "Design One in Question Three covers Park Playground Slides: a park contractor plans to construct TWO different slides for local park children! For younger children below age five, the slide top stands cleanly at vertical height one point five meters inclined gently at thirty degrees to flat ground! Since vertical height is Opposite and slide ramp length is Hypotenuse, sine thirty equals one point five over Length One, giving one half equals one point five over Length One, so slide length equals exact three meters! "
            "For elder children, the slide rises steeper up to vertical height three meters inclined cleanly at sixty degrees! Write sine sixty equals three over Length Two, so root three over two equals three over Length Two, rationalizing six over root three smoothly into two root three meters cleanly in total! "
            "Design Two in Question Five tracks a flying paper kite hovering sixty meters high vertically above flat ground with a taut string tied down tightly making exact angle sixty degrees, giving exact taut string length equal to forty root three meters!"
        ),
        "checkpoints": [
            {
                "question": "A park contractor builds a 3 m high slide inclined at 60° to the ground for elder children (Ex 9.1 Q3). Find the length of the slide:",
                "options": [
                    "2√3 m",
                    "3√3 m",
                    "6 m",
                    "3/2 m"
                ],
                "answer": 0,
                "hint": "Use sin 60° = 3 / L ⟹ √3/2 = 3 / L ⟹ L = 6 / √3!",
                "explanation": "L = 6 / √3 = (6√3)/3 = 2√3 m (while the 1.5 m, 30° slide has length 3 m)."
            },
            {
                "question": "A kite flies at height 60 m above ground with its string tied to ground making an angle of 60° (Ex 9.1 Q5). Find the taut string length:",
                "options": [
                    "40√3 m",
                    "20√3 m",
                    "120 m",
                    "30√3 m"
                ],
                "answer": 0,
                "hint": "Apply sin 60° = 60 / String Length ⟹ √3/2 = 60 / L!",
                "explanation": "L = 120 / √3 = (120√3)/3 = 40√3 m."
            }
        ]
    },
    {
        "id": 8,
        "title": "Flagstaff And Building",
        "subtitle": "Solving Two Stacked Right Triangles Sharing One Horizontal Base AP (Textbook Example 4)",
        "speech": (
            "Now advance from single triangles into TWO-ANGLE Trigonometry—the heart of high scoring board exam questions! Watch Textbook Example Four carefully: "
            "From a point P on flat ground, the angle of elevation to the roof top of a ten meter tall building equals thirty degrees! Hoisted straight vertically on top of that building roof stands a flagstaff! From that SAME point P, the angle of elevation to the top of the flagstaff measures forty five degrees! Find BOTH the length of the flagstaff AND the distance of building foot A from point P! "
            "Spot the shared secret linking BOTH right triangles PAB (short) and PAD (tall): they share the EXACT SAME HORIZONTAL GROUND BASE AP! "
            "Step One: Solve small triangle PAB using known ten meter height and thirty degrees: tangent thirty equals ten over AP, giving base AP equals ten root three, or seventeen point three two meters! "
            "Step Two: Solve tall triangle PAD cleanly using shared base AP and angle forty five degrees: vertical side AD over AP equals tangent forty five equals ONE, making total height AD equal seventeen point three two meters, so flagstaff length equals AD minus ten, or seven point three two meters!"
        ),
        "checkpoints": [
            {
                "question": "From point P, elevation to top of a 10 m building is 30° and to top of flagstaff above it is 45° (Example 4, take √3 = 1.732). Find flagstaff length:",
                "options": [
                    "7.32 m   (= 10(√3 − 1) m)",
                    "17.32 m",
                    "10√3 m",
                    "10 m"
                ],
                "answer": 0,
                "hint": "Find shared base AP = 10 / tan 30° = 10√3 m, then full height AD = AP × tan 45° = 10√3 m, and subtract 10 m!",
                "explanation": "AP = 10√3 ≈ 17.32 m; AD = 17.32 m; flagstaff BD = AD − AB = 17.32 − 10 = 7.32 m."
            },
            {
                "question": "Why are triangles △PAB (30°) and △PAD (45°) easily linked together in two-elevation rooftop problems?",
                "options": [
                    "They share the exact same horizontal ground distance AP from observer to building foot",
                    "They share the same hypotenuse length",
                    "Both triangles have identical height",
                    "Angles 30° and 45° are complementary"
                ],
                "answer": 0,
                "hint": "Check which edge belongs to BOTH right triangle PAB and right triangle PAD!",
                "explanation": "Horizontal base AP stays identical for both triangles, letting one solve AP and pass it into the second triangle."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part1)} slides for Ch9 Class 10 Maths Part 1.")
    for s in slides_part1:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 1 assertions passed cleanly!")
