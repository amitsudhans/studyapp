#!/usr/bin/env python3
"""
Generate Slides 9 to 16 data for NCERT Class 5 Mathematics - Chapter 5: Far and Near
"""

slides_9_to_16 = [
    {
        "id": 9,
        "heading": "Millimetre Scale",
        "tagline": "The World of Small Things: 1 Centimetre Divided into 10 Millimetres",
        "color": "from-teal-600 to-emerald-700",
        "badge": "Sub-Centimetre Precision",
        "audio_text": (
            "We have explored kilometres and metres; now let us zoom in to the fascinating world of small things! "
            "Take your standard plastic school ruler and look closely at the space between 0 and 1 centimetre. "
            "Notice the tiny little tick marks packed in between: there are exactly 10 equal subdivisions! "
            "Each of these tiny subdivisions is called one millimetre, abbreviated as mm. "
            "Therefore, the golden rule of small measurements is: 1 centimetre equals 10 millimetres! "
            "Half a centimetre is the slightly longer middle mark, representing exactly 5 millimetres. "
            "Think of objects that require millimetres: the thickness of a coin is about 2 millimetres; the lead tip of a mechanical pencil is often 0.5 or 0.7 millimetres; and a tiny black ant is around 3 to 4 millimetres long. "
            "When a line measures 2 centimetres and 6 tiny marks, we write it as 2 centimetres 6 millimetres, or 26 millimetres! "
            "Millimetres give us microscope-level precision in our drawings."
        ),
        "theory_blocks": [
            {
                "title": "The 1 cm = 10 mm Rule",
                "content": "Every centimetre is partitioned into 10 equal millimetres. To convert cm to mm, multiply by 10 (e.g. 4 cm = 40 mm).",
                "icon": "🔬"
            },
            {
                "title": "Reading Ruler Subdivisions",
                "content": "Long mark = 1 cm; Mid mark = 5 mm (half-cm); Short ticks = 1 mm each. 3 cm + 4 ticks = 3 cm 4 mm = 34 mm.",
                "icon": "📏"
            },
            {
                "title": "Everyday Millimetre Objects",
                "content": "Thickness of credit card = ~1 mm; 5-rupee coin = ~2 mm; Grains of rice width = ~2 mm; Mobile phone thickness = ~8 mm.",
                "icon": "🪙"
            }
        ],
        "checkpoints": [
            {
                "question": "How many millimetres are there in 1 centimetre?",
                "options": [
                    "10 millimetres",
                    "100 millimetres",
                    "5 millimetres",
                    "1,000 millimetres"
                ],
                "correct": 0,
                "feedback": "Correct! Each centimetre contains exactly 10 equal millimetres."
            },
            {
                "question": "A line measures 4 centimetres and 7 millimetres. What is its total length in millimetres alone?",
                "options": [
                    "47 millimetres",
                    "407 millimetres",
                    "4.7 metres",
                    "40 millimetres"
                ],
                "correct": 0,
                "feedback": "Spot on! 4 cm = 40 mm, plus 7 mm = 47 mm."
            }
        ]
    },
    {
        "id": 10,
        "heading": "Seed Growth",
        "tagline": "Tracking Sprouted Moong and Chana Growth Over 4 Days",
        "color": "from-emerald-600 to-teal-700",
        "badge": "Biological Measurement Activity",
        "audio_text": (
            "Our textbook invites us to conduct an exciting scientific measuring experiment: observing sprouted seeds! "
            "Take a few dried moong or chana seeds, soak them in water overnight, and wrap them in a moist cotton cloth. "
            "Within twenty-four hours, life begins to stir, and a tiny white radicle sprout pushes out! "
            "Using our ruler's millimetre scale, we record the sprout's growth each morning: "
            "On Day 1, the tiny shoot emerges, measuring about 3 millimetres. "
            "On Day 2, it extends to 8 millimetres: growing by 5 millimetres in a single day! "
            "On Day 3, the vigorous sprout reaches 15 millimetres, which we can also write as 1 centimetre and 5 millimetres. "
            "By Day 4, the sprout stretches to 24 millimetres, or 2 centimetres and 4 millimetres! "
            "By tracking daily growth with millimetre precision, we combine biology, observational recording, and metric measurement. "
            "Notice how rapid growth turns invisible daily increments into visible centimetres."
        ),
        "theory_blocks": [
            {
                "title": "Sprout Growth Journal",
                "content": "Day 1: 3 mm; Day 2: 8 mm (+5 mm); Day 3: 15 mm = 1 cm 5 mm (+7 mm); Day 4: 24 mm = 2 cm 4 mm (+9 mm).",
                "icon": "🌱"
            },
            {
                "title": "Growth Rate Calculation",
                "content": "Daily Growth = Length(Day N) - Length(Day N-1). Example: Day 3 Growth = 15 mm - 8 mm = 7 mm.",
                "icon": "📈"
            },
            {
                "title": "Dual Notation",
                "content": "Lengths can be expressed as single mm (24 mm) or mixed cm and mm (2 cm 4 mm). Both are mathematically equivalent.",
                "icon": "📝"
            }
        ],
        "checkpoints": [
            {
                "question": "A sprouted chana seed measures 18 millimetres. How is this expressed in centimetres and millimetres?",
                "options": [
                    "1 cm 8 mm",
                    "18 cm",
                    "10 cm 8 mm",
                    "1 cm 80 mm"
                ],
                "correct": 0,
                "feedback": "Correct! 18 mm = 10 mm + 8 mm = 1 cm 8 mm."
            },
            {
                "question": "A sprout grew from 6 mm on Monday to 14 mm on Tuesday. How much did it grow in one day?",
                "options": [
                    "8 mm",
                    "20 mm",
                    "6 mm",
                    "14 mm"
                ],
                "correct": 0,
                "feedback": "Spot on! 14 mm - 6 mm = 8 mm of growth."
            }
        ]
    },
    {
        "id": 11,
        "heading": "Precision Lines",
        "tagline": "Drawing Accurate Line Segments and Conversions on Double Number Lines",
        "color": "from-indigo-600 to-purple-700",
        "badge": "Drafting Precision",
        "audio_text": (
            "In engineering, architecture, and art, drawing lines of exact length is an essential skill! "
            "To draw a line segment of 5 centimetres and 5 millimetres: "
            "Place your ruler firmly on the paper. Use a sharp pencil point to mark your starting point at exactly 0. "
            "Draw along the edge past the 5-centimetre mark, counting 5 small millimetre ticks to the half-centimetre line. "
            "Mark the endpoint and lift your pencil. You have created an exact segment of 55 millimetres! "
            "What if you are asked to draw a line of 36 millimetres? "
            "Think: 36 millimetres is 30 millimetres plus 6 millimetres. "
            "Since 30 millimetres equals 3 centimetres, 36 millimetres is exactly 3 centimetres and 6 millimetres! "
            "Double number lines help us verify these conversions effortlessly: matching mm to cm, cm to m, and m to km. "
            "Precision drafting ensures that parts built in different workshops fit together with flawless accuracy."
        ),
        "theory_blocks": [
            {
                "title": "Exact Drawing Steps",
                "content": "Step 1: Anchor at 0 (never at the edge of ruler). Step 2: Draw to the whole cm mark. Step 3: Count small mm ticks. Step 4: Double-check endpoints.",
                "icon": "📐"
            },
            {
                "title": "Conversion: mm to cm",
                "content": "Divide by 10. Example: 36 mm = 3.6 cm = 3 cm 6 mm. 70 mm = 7 cm. 95 mm = 9 cm 5 mm.",
                "icon": "🔄"
            },
            {
                "title": "Architectural Drafting",
                "content": "Blueprints use millimetres as the universal standard so that builders never mistake feet for metres or centimetres.",
                "icon": "🏛️"
            }
        ],
        "checkpoints": [
            {
                "question": "Where should you align the starting point of a line when measuring with a ruler?",
                "options": [
                    "At the 0 mark",
                    "At the physical edge of the wooden or plastic ruler",
                    "At the 1 cm mark",
                    "Anywhere in the middle"
                ],
                "correct": 0,
                "feedback": "Correct! Always start at the 0 mark, as the physical edge of a ruler may be worn or indented."
            },
            {
                "question": "A line is 75 millimetres long. What is this length in centimetres and millimetres?",
                "options": [
                    "7 cm 5 mm",
                    "75 cm",
                    "70 cm 5 mm",
                    "7 cm 50 mm"
                ],
                "correct": 0,
                "feedback": "Spot on! 75 mm = 70 mm + 5 mm = 7 cm 5 mm."
            }
        ]
    },
    {
        "id": 12,
        "heading": "Adding Lengths",
        "tagline": "Column Addition for Mixed Units with Metric Regrouping",
        "color": "from-blue-600 to-indigo-700",
        "badge": "Mixed Unit Addition",
        "audio_text": (
            "When combining ribbons, cables, or highway route legs, we often add mixed units of length! "
            "We can add lengths using two reliable methods: "
            "Method 1 is column addition: create separate columns for each unit, such as Metres and Centimetres, or Kilometres and Metres. "
            "Suppose we add 4 metres 65 centimetres and 3 metres 55 centimetres. "
            "Add the centimetres column first: 65 plus 55 equals 120 centimetres! "
            "Because 100 centimetres equals 1 metre, 120 centimetres is 1 metre and 20 centimetres. "
            "We write 20 in the centimetres column and carry over 1 metre to the metres column! "
            "Now add the metres: 4 plus 3 plus the carried 1 gives 8 metres. The total is 8 metres 20 centimetres! "
            "Method 2 is conversion: convert everything to centimetres first: 465 cm plus 355 cm equals 820 cm, which equals 8 m 20 cm. "
            "Both methods give the exact same answer, giving you complete flexibility."
        ),
        "theory_blocks": [
            {
                "title": "Regrouping Thresholds",
                "content": "For cm to m: 100 cm bundles into 1 m (carry over at 100). For m to km: 1,000 m bundles into 1 km (carry over at 1,000).",
                "icon": "📦"
            },
            {
                "title": "Column Addition Method",
                "content": "Align smaller units on the right. Add smaller units first. If sum >= base, write remainder and carry bundle to the left.",
                "icon": "📊"
            },
            {
                "title": "Conversion Method",
                "content": "Convert both terms to the smallest unit (e.g. 4 m 65 cm = 465 cm). Add as whole numbers, then separate back into mixed units.",
                "icon": "🔄"
            }
        ],
        "checkpoints": [
            {
                "question": "What is the sum of 5 m 45 cm and 2 m 70 cm?",
                "options": [
                    "8 m 15 cm",
                    "7 m 15 cm",
                    "8 m 25 cm",
                    "7 m 115 cm"
                ],
                "correct": 0,
                "feedback": "Correct! cm: 45 + 70 = 115 cm = 1 m 15 cm (write 15, carry 1 m). Metres: 5 + 2 + 1 = 8 m. Total = 8 m 15 cm."
            },
            {
                "question": "Add 3 km 600 m and 4 km 750 m. What is the total distance?",
                "options": [
                    "8 km 350 m",
                    "7 km 350 m",
                    "8 km 450 m",
                    "7 km 1,350 m"
                ],
                "correct": 0,
                "feedback": "Spot on! m: 600 + 750 = 1,350 m = 1 km 350 m. km: 3 + 4 + 1 = 8 km. Total = 8 km 350 m."
            }
        ]
    },
    {
        "id": 13,
        "heading": "Subtracting Lengths",
        "tagline": "Column Subtraction with Borrowing Across Metric Units",
        "color": "from-rose-600 to-red-700",
        "badge": "Mixed Unit Subtraction",
        "audio_text": (
            "Subtracting lengths is essential when calculating remaining distances, leftover fabric, or route differences! "
            "Just like standard subtraction, when the top number in the smaller unit is less than the bottom number, we must borrow from the larger unit. "
            "Consider this: A tailor has a 6-metre roll of silk ribbon and cuts off 2 metres and 45 centimetres for a dress. "
            "How much ribbon remains? "
            "Let us subtract: 6 metres 00 centimetres minus 2 metres 45 centimetres. "
            "In the centimetres column, 0 minus 45 is not possible! "
            "We borrow 1 metre from the 6 metres, leaving 5 metres. "
            "Remember: 1 borrowed metre equals 100 centimetres! "
            "Now subtract centimetres: 100 minus 45 equals 55 centimetres. "
            "Subtract metres: 5 minus 2 equals 3 metres. "
            "The remaining ribbon is 3 metres 55 centimetres! "
            "Let us check by addition: 2 metres 45 cm plus 3 metres 55 cm equals 6 metres 00 cm. Perfectly verified!"
        ),
        "theory_blocks": [
            {
                "title": "Borrowing from Metres",
                "content": "Borrowing 1 metre gives exactly 100 centimetres (not 10!). 0 cm becomes 100 cm; 25 cm becomes 125 cm.",
                "icon": "🔄"
            },
            {
                "title": "Borrowing from Kilometres",
                "content": "Borrowing 1 kilometre gives exactly 1,000 metres! 200 m becomes 1,200 m.",
                "icon": "🛣️"
            },
            {
                "title": "Verification Check",
                "content": "Always check: Remaining Length + Cut Length = Original Roll. 3 m 55 cm + 2 m 45 cm = 6 m.",
                "icon": "✅"
            }
        ],
        "checkpoints": [
            {
                "question": "What is 5 m 20 cm minus 2 m 60 cm?",
                "options": [
                    "2 m 60 cm",
                    "3 m 60 cm",
                    "2 m 40 cm",
                    "3 m 40 cm"
                ],
                "correct": 0,
                "feedback": "Correct! Borrow 1 m (100 cm): 120 cm - 60 cm = 60 cm. Metres: 4 - 2 = 2 m. Result = 2 m 60 cm."
            },
            {
                "question": "A road is 10 km long. Workers have paved 6 km 400 m. How much road remains to be paved?",
                "options": [
                    "3 km 600 m",
                    "4 km 600 m",
                    "3 km 400 m",
                    "4 km 400 m"
                ],
                "correct": 0,
                "feedback": "Spot on! 10 km 000 m - 6 km 400 m: Borrow 1 km (1,000 m): 1,000 - 400 = 600 m. km: 9 - 6 = 3 km. Result = 3 km 600 m."
            }
        ]
    },
    {
        "id": 14,
        "heading": "Scaling Lengths",
        "tagline": "Multiplying and Dividing Lengths for Fabric and Road Laying",
        "color": "from-amber-600 to-orange-700",
        "badge": "Proportional Scaling",
        "audio_text": (
            "When manufacturing clothes, building fences, or laying highway asphalt, we multiply and divide lengths to scale our quantities! "
            "Suppose a tailor needs 2 metres and 25 centimetres of fabric to stitch one school uniform shirt. "
            "How much fabric is required to stitch 4 identical shirts? "
            "We multiply the length by 4! "
            "Multiply the metres: 2 metres times 4 equals 8 metres. "
            "Multiply the centimetres: 25 centimetres times 4 equals 100 centimetres! "
            "Since 100 centimetres equals 1 metre, we add this 1 metre to our 8 metres, giving exactly 9 metres of fabric! "
            "What about division? "
            "Suppose a road construction crew paves 12 kilometres of highway equally over 4 days. "
            "How many kilometres do they pave each day? "
            "We divide: 12 kilometres divided by 4 equals 3 kilometres per day! "
            "Scaling lengths allows planners and builders to calculate materials, costs, and project timelines with absolute accuracy."
        ),
        "theory_blocks": [
            {
                "title": "Multiplying Mixed Units",
                "content": "Multiply metres and centimetres separately, then bundle every 100 cm into 1 m. (2 m 25 cm) × 4 = 8 m + 100 cm = 9 m.",
                "icon": "✖️"
            },
            {
                "title": "Dividing Lengths",
                "content": "Divide total length by number of parts or days: 12 km / 4 = 3 km per day. 5 m / 2 = 2 m 50 cm per piece.",
                "icon": "➗"
            },
            {
                "title": "Double Number Line for Cost",
                "content": "If 1 m of fabric costs ₹ 120, then 2 m costs ₹ 240, and 50 cm (0.5 m) costs ₹ 60. Proportional scaling connects length directly to currency.",
                "icon": "🏷️"
            }
        ],
        "checkpoints": [
            {
                "question": "If 1 pair of trousers requires 1 m 50 cm of cloth, how much cloth is needed for 3 pairs?",
                "options": [
                    "4 m 50 cm",
                    "3 m 50 cm",
                    "4 m",
                    "5 m"
                ],
                "correct": 0,
                "feedback": "Correct! (1 m × 3) + (50 cm × 3) = 3 m + 150 cm = 3 m + 1 m 50 cm = 4 m 50 cm."
            },
            {
                "question": "A 15-metre rope is cut into 5 equal pieces. How long is each piece?",
                "options": [
                    "3 metres",
                    "5 metres",
                    "2.5 metres",
                    "3.5 metres"
                ],
                "correct": 0,
                "feedback": "Spot on! 15 m / 5 = 3 metres."
            }
        ]
    },
    {
        "id": 15,
        "heading": "Height Estimation",
        "tagline": "Developing Real-World Spatial Benchmarks for Buildings and Trees",
        "color": "from-teal-600 to-cyan-700",
        "badge": "Estimation Skills",
        "audio_text": (
            "A skilled mathematician can estimate the height of a towering tree or building without carrying a giant measuring tape! "
            "How do we do this? By using familiar real-world benchmarks! "
            "Here are some reliable height benchmarks to keep in mind: "
            "The height of a standard single storey in a residential building or school is approximately 3 metres. "
            "Therefore, a three-storey school building is about 3 times 3, or approximately 9 to 10 metres tall! "
            "An adult person's height is usually between 1.6 and 1.8 metres. "
            "A standard classroom door is about 2 metres high. "
            "If you look at a mango tree outside your window that appears about twice as tall as the classroom door, you can estimate its height as roughly 4 metres! "
            "A streetlight pole is typically about 6 metres high. "
            "By comparing unfamiliar objects against these trusted mental anchors, you can make fast, reasonable estimations anytime, anywhere."
        ),
        "theory_blocks": [
            {
                "title": "Mental Benchmark Anchors",
                "content": "Classroom Door = ~2 m; Single Building Storey = ~3 m; Adult Person = ~1.7 m; Utility Light Pole = ~6 m; Ceiling Height = ~3 m.",
                "icon": "🧠"
            },
            {
                "title": "Proportional Stacking",
                "content": "To estimate a tall tree: imagine how many classroom doors or people stacked head-to-toe would equal its height.",
                "icon": "🌲"
            },
            {
                "title": "Estimation vs Guessing",
                "content": "Estimation is not random guessing; it is mathematical reasoning based on known real-world reference benchmarks.",
                "icon": "🎯"
            }
        ],
        "checkpoints": [
            {
                "question": "A four-storey apartment building has floors of standard height (~3 m each). What is its estimated total height?",
                "options": [
                    "About 12 metres (4 × 3 m)",
                    "About 4 metres",
                    "About 40 metres",
                    "About 2 metres"
                ],
                "correct": 0,
                "feedback": "Correct! 4 storeys × ~3 metres per storey ≈ 12 metres."
            },
            {
                "question": "A flagpole is approximately three times the height of a 2-metre classroom door. What is its estimated height?",
                "options": [
                    "6 metres",
                    "4 metres",
                    "8 metres",
                    "10 metres"
                ],
                "correct": 0,
                "feedback": "Spot on! 3 × 2 metres = 6 metres."
            }
        ]
    },
    {
        "id": 16,
        "heading": "Feet and Inches",
        "tagline": "Everyday Imperial Units: Converting Inches, Feet, and Centimetres",
        "color": "from-purple-600 to-indigo-700",
        "badge": "Everyday Alternative Units",
        "audio_text": (
            "While the metric system is the universal international scientific standard, you will often hear people describe heights and screens in feet and inches! "
            "Our textbook explores these popular everyday units: "
            "An inch is approximately the length of the top joint of an adult's thumb, or about 2 centimetres and 5 millimetres (2.5 cm). "
            "There are exactly 12 inches in 1 foot! "
            "Since each inch is about 2.5 centimetres, 1 foot (12 inches) equals approximately 30 centimetres: the exact length of your long school ruler! "
            "When doctors and parents measure a child's height against a wall chart, a Grade 5 student might measure 4 feet 4 inches. "
            "Let us convert 4 feet into centimetres: 4 times 30 centimetres gives 120 centimetres! "
            "4 inches is 4 times 2.5 centimetres, which is 10 centimetres. "
            "120 plus 10 gives approximately 130 centimetres! "
            "Understanding both metric units and everyday feet and inches gives you complete mastery over human height and spatial dimensions."
        ),
        "theory_blocks": [
            {
                "title": "The Imperial Conversions",
                "content": "1 foot = 12 inches; 1 inch ≈ 2.5 cm (2 cm 5 mm); 1 foot ≈ 30 cm (standard 30 cm school ruler).",
                "icon": "🦶"
            },
            {
                "title": "Height Measuring Chart",
                "content": "Grade 5 average height = ~4 ft 2 in to 4 ft 6 in (~125 cm to 138 cm). 5 feet = 5 × 30 cm = ~150 cm.",
                "icon": "📏"
            },
            {
                "title": "Screen & Shoe Sizes",
                "content": "Television displays, mobile screens, and laptops are commonly measured in diagonal inches (e.g. 15.6-inch laptop screen).",
                "icon": "📱"
            }
        ],
        "checkpoints": [
            {
                "question": "How many inches are there in 1 foot?",
                "options": [
                    "12 inches",
                    "10 inches",
                    "100 inches",
                    "24 inches"
                ],
                "correct": 0,
                "feedback": "Correct! Exactly 12 inches make up 1 foot."
            },
            {
                "question": "Approximately how many centimetres are in 1 foot?",
                "options": [
                    "About 30 cm (the length of a long school ruler)",
                    "About 10 cm",
                    "About 100 cm",
                    "About 50 cm"
                ],
                "correct": 0,
                "feedback": "Spot on! 1 foot = 12 inches × 2.5 cm ≈ 30 cm."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Authored Slides 9 to 16. Count: {len(slides_9_to_16)}")

