#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 10: Proportional Reasoning-2
Slides Data Generator - Part 1 (Slides 1 to 8)
Strictly matches NCERT Class 8 Maths Ch 10 syllabus with 1-3 word headings,
195-215 spoken words per slide, zero fictional characters/personas.
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Proportional Scaling Recap",
        "subtitle": "Section 3.1 Proportionality Recap: Common Scaling Factor (Idli Batter) & Cross-Multiplication (ad = bc)",
        "speech": (
            "Welcome to Class Eight Mathematics Chapter Ten: Proportional Reasoning Part Two! Begin in Section Three Point One with a quick foundational recap of proportional change! Remember how true proportionality works in everyday recipes such as south Indian idli batter? Suppose an authentic recipe blends 3 cups of soaked rice with 1 cup of urad dal—forming the exact ratio 3 : 1! Whenever a kitchen scales up for a larger gathering, BOTH ingredients must multiply by the exact same common scaling factor! Multiply cleanly by factor 4: 12 cups of rice pair with 4 cups of urad dal, preserving identical batter texture! "
            "How do we verify mathematically whether two separate ratios a : b and c : d truly stand in proportion? Recall crisp CROSS-MULTIPLICATION VERIFICATION! Two ratios a : b and c : d are proportional if and only if the product of extremes equals the product of means: a × d = b × c, equivalently written as equal fractions a/c = b/d! Test 6 : 15 against 10 : 25 immediately right now: check 6 × 25 = 150 and 15 × 10 = 150! Identical cross-products instantly confirm an exact proportional match!"
        ),
        "checkpoints": [
            {
                "question": "An idli batter recipe uses rice and urad dal in the ratio 3 : 1. Which scaled batch preserves the exact same batter consistency?",
                "options": [
                    "15 cups rice and 5 cups urad dal   (both scaled × 5)",
                    "8 cups rice and 6 cups urad dal   (+5 added to both)",
                    "15 cups rice and 3 cups urad dal",
                    "12 cups rice and 6 cups urad dal"
                ],
                "answer": 0,
                "hint": "Multiply BOTH 3 and 1 by the exact same scaling factor!",
                "explanation": "Multiplying both 3 and 1 by 5 gives 15 : 5, which reduces cleanly back to 3 : 1."
            },
            {
                "question": "Use cross-multiplication (a × d = b × c) to test which ratio pair forms a true proportion with 8 : 12:",
                "options": [
                    "14 : 21   (8 × 21 = 168 and 12 × 14 = 168)",
                    "10 : 14   (8 × 14 = 112 ≠ 120)",
                    "16 : 20   (8 × 20 = 160 ≠ 192)",
                    "12 : 16   (8 × 16 = 128 ≠ 144)"
                ],
                "answer": 0,
                "hint": "Check a × d = b × c for each option!",
                "explanation": "8 × 21 = 168 equals 12 × 14 = 168 (both reduce cleanly to 2 : 3)."
            }
        ]
    },
    {
        "id": 2,
        "title": "Map Scale Ratios",
        "subtitle": "Section 3.2 Ratios in Maps: Representative Fraction (RF), Indian City Distances & 1:50 Classroom Plans",
        "speech": (
            "Explore Section Three Point Two: Ratios in Maps! How does an entire state or country shrink accurately onto a single classroom atlas page without warping geography? Through a special ratio called the REPRESENTATIVE FRACTION, written RF! Representative Fraction defines the exact ratio comparing measured distance on a map directly to actual geographical ground distance, stated in matching units! "
            "Take an Indian road atlas with Representative Fraction 1 : 60,00,000! That means 1 centimetre measured on paper equals 60,00,000 centimetres on Earth! Divide by 100,000 centimetres per kilometre cleanly: 1 map centimetre represents EXACTLY 60 kilometres on the ground! Measure straight aerial lines between Bengaluru, Chennai, and Mangaluru using a ruler right on your atlas: if Bengaluru to Chennai measures 5 centimetres on this 1 : 60,00,000 map, multiply 5 × 60 = 300 kilometres! Similarly, if Bengaluru to Mangaluru measures 4.5 centimetres, aerial distance equals 4.5 × 60 = 270 kilometres! "
            "Now scale down your own classroom onto graph paper at exact RF 1 : 50! At 1 : 50 scale, every 1 centimetre drawn represents 50 centimetres (0.5 metres) in reality—so a 6-metre wall draws cleanly as 12 centimetres using standardized blueprint symbols for desks, doors, and furniture fixtures!"
        ),
        "checkpoints": [
            {
                "question": "A map uses a Representative Fraction (RF) of 1 : 60,00,000 (where 1 cm = 60 km). If the aerial distance on the map between Bengaluru and Chennai measures 5 cm, what is the actual ground distance?",
                "options": [
                    "300 km",
                    "60 km",
                    "12 km",
                    "3,000 km"
                ],
                "answer": 0,
                "hint": "Each 1 cm on the map equals 60 km on the ground!",
                "explanation": "5 cm × 60 km/cm = 300 km actual straight-line distance."
            },
            {
                "question": "A classroom floor plan is drawn to a 1 : 50 scale. How long should a teacher's desk measuring 150 cm (1.5 m) in reality appear on the drawing?",
                "options": [
                    "3 cm   (150 ÷ 50 = 3 cm)",
                    "50 cm",
                    "7.5 cm",
                    "30 cm"
                ],
                "answer": 0,
                "hint": "Divide real dimension 150 cm by scale factor 50!",
                "explanation": "At 1 : 50 scale, map length = 150 cm ÷ 50 = 3 cm."
            }
        ]
    },
    {
        "id": 3,
        "title": "Multi Term Ratios",
        "subtitle": "Section 3.3 Ratios with >2 Terms: Multi-Term Proportions, Spice Mixes, Paint Shades (2:3:5) & Concrete (1:1.5:3)",
        "speech": (
            "Real recipes and engineering blueprints rarely mix just two items! Enter Section Three Point Three: Ratios with More than Two Terms! Whenever three, four, or more ingredients scale simultaneously by ONE identical multiplier, we express their balanced relationship as a continuous multi-term ratio such as a : b : c : d! Consider an aromatic spice blend combining coriander, cumin, pepper, and cloves in ratio 8 : 4 : 2 : 1! Double the entire batch cleanly by multiplying every term by 2 to get 16 : 8 : 4 : 2! "
            "Formulate multi-term proportionality cleanly in algebra: two multi-term sequences a : b : c : d and p : q : r : s stand in proportion—written a : b : c : d :: p : q : r : s—if and only if every pair shares one common multiplier: a/p = b/q = c/r = d/s! "
            "Test structural reinforced concrete mixing cement, sand, and gravel in ratio 1 : 1.5 : 3! First clear the decimal by doubling every term: 2 : 3 : 6! If builders pour 6 bags of cement (×6 factor from 1), they mix 9 bags sand and 18 bags gravel—just like 2 : 3 : 5 paint shades!"
        ),
        "checkpoints": [
            {
                "question": "Structural reinforced concrete mixes cement, sand, and gravel in ratio 1 : 1.5 : 3. If a builder uses 8 buckets of cement, how many buckets of sand and gravel are required?",
                "options": [
                    "12 buckets sand and 24 buckets gravel",
                    "9.5 buckets sand and 11 buckets gravel",
                    "16 buckets sand and 24 buckets gravel",
                    "12 buckets sand and 18 buckets gravel"
                ],
                "answer": 0,
                "hint": "Common scaling factor is 8 ÷ 1 = 8! Multiply BOTH 1.5 and 3 by 8!",
                "explanation": "1×8 = 8 cement; 1.5×8 = 12 sand; 3×8 = 24 gravel → ratio 8 : 12 : 24 = 1 : 1.5 : 3."
            },
            {
                "question": "A paint shade blends red, blue, and white pigments in ratio 2 : 3 : 5. If 15 mL of white pigment is used, how much red and blue pigment match proportionally?",
                "options": [
                    "6 mL red and 9 mL blue",
                    "10 mL red and 15 mL blue",
                    "4 mL red and 6 mL blue",
                    "12 mL red and 13 mL blue"
                ],
                "answer": 0,
                "hint": "Find multiplier from white: 15 ÷ 5 = 3! Multiply 2 and 3 by 3!",
                "explanation": "Multiplier = 15 ÷ 5 = 3 → red = 2×3 = 6 mL, blue = 3×3 = 9 mL."
            }
        ]
    },
    {
        "id": 4,
        "title": "Whole Share Partitioning",
        "subtitle": "Section 3.4 Dividing a Whole in a Given Ratio: Partitioning Formula, Concrete, Paint & 1:3:5 Angles",
        "speech": (
            "Flip Section Three Point Three around in Section Three Point Four: instead of knowing one ingredient, what if you already know the TOTAL whole quantity x and must divide it fairly across multi-term ratio a : b : c? Use the universal PARTITIONING FORMULA! First sum ALL ratio terms together to find total equal groups: S = a + b + c! Then each component share equals total x multiplied by Component Term divided by Sum of All Terms: Component Share = x × (Component Term ÷ Sum of All Terms)! "
            "Apply this cleanly to three NCERT examples! Example One: prepare 110 units of concrete in ratio 1 : 1.5 : 3 (sum = 5.5 parts → 20 units per part → 20 cement, 30 sand, 60 gravel)! "
            "Example Two: mix 50 mL of purple shade paint in ratio 2 : 3 : 5 (sum = 10 parts → 5 mL each → 10 mL red, 15 mL blue, 25 mL white)! Example Three: divide a triangle's 180° interior angle sum cleanly in ratio 1 : 3 : 5 (sum = 9 parts → 20° per part → exact angles 20°, 60°, and 100° totaling 180°)!"
        ),
        "checkpoints": [
            {
                "question": "A triangle's interior angles sum to 180° and stand in the ratio 1 : 3 : 5. What are the three angle measures?",
                "options": [
                    "20°, 60°, 100°",
                    "30°, 60°, 90°",
                    "18°, 54°, 108°",
                    "25°, 75°, 80°"
                ],
                "answer": 0,
                "hint": "Sum of terms = 1 + 3 + 5 = 9; each part = 180° ÷ 9 = 20°!",
                "explanation": "1×20° = 20°, 3×20° = 60°, 5×20° = 100° (sum = 180°)."
            },
            {
                "question": "Divide 110 total units of concrete mixture into cement, sand, and gravel in the ratio 1 : 1.5 : 3:",
                "options": [
                    "20 units cement, 30 units sand, 60 units gravel",
                    "10 units cement, 15 units sand, 30 units gravel",
                    "25 units cement, 35 units sand, 50 units gravel",
                    "22 units cement, 33 units sand, 55 units gravel"
                ],
                "answer": 0,
                "hint": "Total ratio sum = 1 + 1.5 + 3 = 5.5 parts; compute 110 ÷ 5.5!",
                "explanation": "One part = 110 ÷ 5.5 = 20 → shares are 20, 30, and 60 (totaling 110)."
            }
        ]
    },
    {
        "id": 5,
        "title": "Schedules Books Coins",
        "subtitle": "Section 3.4 Figure it Out: Cricket Schedules, Library Books, Coin Value Ratios & Triangle Inequality",
        "speech": (
            "Practice Section Three Point Four's diverse Figure it Out applications right now! Application One: CRICKET TRAINING SCHEDULES! If a 120-minute practice session splits between batting, bowling, and fielding in ratio 3 : 2 : 1 (sum = 6 parts → 20 min each), athletes spend 60 minutes batting, 40 minutes bowling, and 20 minutes fielding! "
            "Application Two: LIBRARY BOOK DISTRIBUTIONS! If 450 library books split among English, Hindi, and Kannada in ratio 4 : 3 : 2 (sum = 9 parts → 50 books per part), shelves hold 200 English, 150 Hindi, and 100 Kannada books! "
            "Application Three: COIN VALUE TOTALS FROM COIN COUNT RATIOS! Careful—NEVER confuse coin counts with rupee values! Suppose a piggy bank holds ₹1, ₹2, and ₹5 coins whose COUNTS stand in ratio 3 : 2 : 1, totaling ₹120! Let counts equal 3k, 2k, and 1k! Multiply each count by its rupee coin denomination: Total Value = 1(3k) + 2(2k) + 5(1k) = 3k + 4k + 5k = 12k = ₹120 → k = 10 → 30, 20, and 10 coins! "
            "Application Four: TRIANGLE SIDE RATIOS! Check whether side ratio 1 : 2 : 4 can EVER construct a valid triangle: 1 + 2 = 3 < 4 violates the triangle inequality—no triangle forms!"
        ),
        "checkpoints": [
            {
                "question": "A pouch contains ₹1, ₹2, and ₹5 coins in the count ratio 3 : 2 : 1, with a total monetary value of ₹72. How many ₹5 coins are inside?",
                "options": [
                    "6 coins of ₹5   (value = 3k + 4k + 5k = 12k = 72 → k = 6)",
                    "12 coins of ₹5",
                    "18 coins of ₹5",
                    "3 coins of ₹5"
                ],
                "answer": 0,
                "hint": "Let counts be 3k, 2k, 1k; total rupee value = (1×3k) + (2×2k) + (5×1k)!",
                "explanation": "12k = ₹72 gives k = 6, so there are 18 (₹1), 12 (₹2), and 6 (₹5) coins."
            },
            {
                "question": "Can three wooden sticks whose lengths lie in the ratio 2 : 3 : 6 be joined to form a closed triangle?",
                "options": [
                    "No — because 2 + 3 = 5 is strictly less than longest side 6 (violates triangle inequality!)",
                    "Yes — because all ratio terms are positive integers",
                    "Yes — forming a right-angled triangle",
                    "Only if total perimeter exceeds 100 cm"
                ],
                "answer": 0,
                "hint": "Check if the sum of the two shorter parts exceeds the longest part!",
                "explanation": "In any triangle, two sides combined must exceed the third side; 2k + 3k = 5k < 6k fails."
            }
        ]
    },
    {
        "id": 6,
        "title": "Pie Chart Angles",
        "subtitle": "Section 3.5 A Slice of the Pie: Simplest Ratios via HCF & Central Angles (Grades A–E Worked Example)",
        "speech": (
            "Visualize partitioned wholes effortlessly in Section Three Point Five: A Slice of the Pie! A pie chart represents proportional categorical data as wedge-shaped sectors slicing one full 360° circle! Why 360°? Because one complete turn around any circle center always measures exactly 360 degrees! "
            "Construct any pie chart cleanly in two systematic steps! Step One: simplify category frequencies by dividing out their Highest Common Factor (HCF) so numbers become tiny! Step Two: compute each sector's CENTRAL ANGLE using the proportional formula: Central Angle = (Category Frequency ÷ Total Frequency) × 360°! "
            "Follow NCERT's classic assessment grades example cleanly! Suppose 40 students earn Grades A through E with frequencies 12, 10, 8, 6, and 4! First spot HCF(12, 10, 8, 6, 4) = 2—reducing ratio cleanly to 6 : 5 : 4 : 3 : 2 (sum = 20)! Now multiply every slice fraction by 360° (each single simplified unit equals 360° ÷ 20 = 18°)! Instantly compute all five central angles: Grade A = 6 × 18° = 108°; Grade B = 5 × 18° = 90°; Grade C = 4 × 18° = 72°; Grade D = 3 × 18° = 54°; Grade E = 2 × 18° = 36°! Check total: 108 + 90 + 72 + 54 + 36 = EXACT 360°!"
        ),
        "checkpoints": [
            {
                "question": "In a class of 40 students, 10 students scored Grade B. Using Central Angle = (Frequency ÷ Total) × 360°, what central angle represents Grade B?",
                "options": [
                    "90°   ((10 / 40) × 360° = 90°)",
                    "72°",
                    "108°",
                    "36°"
                ],
                "answer": 0,
                "hint": "10 out of 40 is 1/4 of the circle!",
                "explanation": "(10 / 40) × 360° = (1/4) × 360° = 90°."
            },
            {
                "question": "Grades A–E have frequencies 12, 10, 8, 6, 4. Dividing by HCF = 2 simplifies them to 6 : 5 : 4 : 3 : 2. What angle does each single simplified unit represent?",
                "options": [
                    "18° per unit   (360° ÷ 20 = 18°)",
                    "9° per unit",
                    "20° per unit",
                    "36° per unit"
                ],
                "answer": 0,
                "hint": "Sum of simplified terms = 6 + 5 + 4 + 3 + 2 = 20; divide 360° by 20!",
                "explanation": "Total simplified units = 20, so 1 unit = 360° ÷ 20 = 18°, making angles 108°, 90°, 72°, 54°, 36°."
            }
        ]
    },
    {
        "id": 7,
        "title": "Surveys Viewership Charts",
        "subtitle": "Section 3.5 Figure it Out: Seasonal Surveys, TV Channel Viewership Percentages & Subject Popularity Pies",
        "speech": (
            "Apply pie chart engineering cleanly across three Figure it Out survey types inside Section Three Point Five! Survey One: SEASONAL PREFERENCE SURVEYS! Suppose 180 residents pick Winter, Monsoon, or Summer in counts 90, 60, and 30! Simplify immediately via HCF = 30 to ratio 3 : 2 : 1 (sum = 6 parts → 360° ÷ 6 = 60° per part): Winter spans 180° (half circle!), Monsoon spans 120°, and Summer spans 60°! "
            "Survey Two: TV CHANNEL CATEGORY VIEWERSHIP PERCENTAGES! When survey data arrives directly as percentages (say Sports 25%, News 15%, Entertainment 45%, Science 15%), remember percentages simply mean parts out of 100! Each 1% of any pie chart equals 360° ÷ 100 = 3.6°! Multiply directly: Sports = 25 × 3.6° = 90°; News = 15 × 3.6° = 54°; Entertainment = 45 × 3.6° = 162°; Science = 54°—summing cleanly to 360°! "
            "Survey Three: READING POPULARITY PIE CHARTS IN REVERSE! Given a classroom subject popularity sector spanning 108° out of 120 surveyed school students, recover the exact student count directly by computing the circle fraction of 360°: (108° ÷ 360°) × 120 = (3/10) × 120 = 36 students choosing that favorite classroom subject!"
        ),
        "checkpoints": [
            {
                "question": "A TV viewership survey reports 35% of households prefer Science & Documentaries. What exact central angle represents this slice on a pie chart?",
                "options": [
                    "126°   (35% × 360° = 126°)",
                    "35°",
                    "108°",
                    "144°"
                ],
                "answer": 0,
                "hint": "Every 1% of a full circle equals 3.6°, so compute 35 × 3.6° (or 7/20 × 360°)!",
                "explanation": "(35 / 100) × 360° = 126°."
            },
            {
                "question": "In a school subject popularity pie chart representing 120 students, the Mathematics sector measures 108°. How many students chose Mathematics?",
                "options": [
                    "36 students",
                    "30 students",
                    "42 students",
                    "108 students"
                ],
                "answer": 0,
                "hint": "Compute (108° / 360°) × 120! Notice 108/360 simplifies cleanly to 3/10!",
                "explanation": "(108 / 360) × 120 = (3 / 10) × 120 = 36 students."
            }
        ]
    },
    {
        "id": 8,
        "title": "Direct Versus Inverse",
        "subtitle": "Section 3.6 Inverse Proportions: Contrasting Constant Quotient (x/y = k) vs Constant Product (x·y = k)",
        "speech": (
            "Welcome to the centerpiece of Chapter Ten—Section Three Point Six: INVERSE PROPORTIONS! Until now, every proportion scaled quantities TOGETHER in the same direction: double recipe flour, double recipe sugar—keeping their QUOTIENT constant (x/y = k), known as DIRECT PROPORTION! "
            "Now discover the opposite mathematical universe! What happens when INCREASING one quantity causes its partner quantity to DECREASE proportionately? Suppose a fixed amount of physical work waits to be finished, or a fixed road distance waits to be driven: hiring TWICE as many painters HALVES painting time; tripling driving speed cuts travel duration cleanly down to ONE-THIRD! Whenever multiplying variable x by scaling factor n forces partner variable y to multiply by reciprocal factor 1/n, x and y stand in INVERSE PROPORTION! "
            "Spot the crystal-clear algebraic signature distinguishing both mathematical worlds! In DIRECT proportion, the QUOTIENT stays locked constant forever: x/y = k (equivalently x₁/y₁ = x₂/y₂)! In INVERSE proportion, the PRODUCT stays locked constant forever: x · y = k (equivalently x₁ y₁ = x₂ y₂)! Checking carefully whether row products stay completely equal versus row quotients across numerical data tables immediately reveals which proportionality law truly governs every single quantitative real-world problem and data table!"
        ),
        "checkpoints": [
            {
                "question": "Variables x and y vary INVERSELY. When x = 12, y = 5. If x is tripled to 36 (factor n = 3), what happens to y?",
                "options": [
                    "y scales by 1/3 to 5/3   (keeping product 36 × 5/3 = 60 constant)",
                    "y also triples to 15",
                    "y decreases by 3 to 2",
                    "y remains 5 unchanged"
                ],
                "answer": 0,
                "hint": "When x multiplies by n = 3, inverse variable y multiplies by reciprocal 1/3 so x · y = 60 stays constant!",
                "explanation": "Product k = 12 × 5 = 60. When x = 36, y = 60 ÷ 36 = 5/3 (scaled by 1/3)."
            },
            {
                "question": "Which algebraic invariant cleanly distinguishes INVERSE proportion from DIRECT proportion across a data table (x₁, y₁) and (x₂, y₂)?",
                "options": [
                    "Inverse keeps PRODUCT constant (x₁y₁ = x₂y₂ = k); Direct keeps QUOTIENT constant (x₁/y₁ = x₂/y₂ = k)",
                    "Inverse keeps DIFFERENCE constant (x − y = k); Direct keeps SUM constant",
                    "Inverse keeps SUM constant (x + y = k)",
                    "Both always satisfy x₁y₁ = x₂y₂"
                ],
                "answer": 0,
                "hint": "Check what stays unchanged when one quantity scales by n and the other by 1/n!",
                "explanation": "(n·x)(y/n) = x·y = k proves constant product governs inverse proportion, whereas constant ratio x/y governs direct proportion."
            }
        ]
    }
]
