# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 8: Weight and Capacity
Part 1: Slides 1 to 8
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Weight Estimation",
        "tagline": "Check! Check! • Estimating Real-World Masses & Reading Scales",
        "lecture": (
            "Welcome to the study of weight and capacity! In daily life, we constantly interact with objects of very different masses, from a light spoon to a heavy steel wardrobe. Estimation is our mental superpower for evaluating whether a measured quantity makes practical physical sense before we even touch a scale. Consider the common items found in a home: a sturdy steel almirah weighs around 80 kilograms, a solid wooden bed weighs about 40 kilograms, a standard sack of basmati rice weighs 25 kilograms, and a two-seater sofa weighs close to 35 kilograms. In contrast, smaller everyday items are much lighter: an empty plastic bucket weighs approximately 1 kilogram, while a full one-litre water bottle also weighs roughly 1 kilogram because one litre of water has a mass of exactly one thousand grams. A large double-door refrigerator weighs around 60 kilograms. If someone claims a water bottle weighs 50 kilograms or an almirah weighs only 200 grams, our estimation alarm immediately rings! To measure mass precisely, we use weighing instruments. Analog scales use internal springs that stretch under load, rotating a needle across a circular dial marked with kilogram graduations and fine gram subdivisions. Digital scales rely on electronic strain-gauge load cells that convert mechanical pressure into crisp digital numbers. By checking estimation first, we avoid costly measurement blunders."
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>🏠</span> Household Mass Benchmarks
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    Developing an intuitive sense of mass prevents gross calculation errors. Compare typical real-world items against standard metric values:
                </p>
                <div class="grid grid-cols-2 gap-2 text-xs">
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-300">🚪 Steel Almirah</span>
                        <span class="font-bold text-emerald-400">~80 kg</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-300">🛏️ Wooden Bed</span>
                        <span class="font-bold text-emerald-400">~40 kg</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-300">🌾 Rice Bag</span>
                        <span class="font-bold text-emerald-400">25 kg</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-300">🛋️ Living Room Sofa</span>
                        <span class="font-bold text-emerald-400">~35 kg</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-300">🧊 Refrigerator</span>
                        <span class="font-bold text-emerald-400">~60 kg</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-300">🪣 Empty Plastic Bucket</span>
                        <span class="font-bold text-amber-400">~1 kg</span>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>⚖️</span> Analog vs Digital Weighing Scales
                    </h4>
                    <ul class="text-xs text-slate-300 space-y-2 leading-relaxed">
                        <li class="flex items-start gap-2">
                            <span class="text-cyan-400 font-bold">•</span>
                            <span><strong>Analog Dial Scale:</strong> An internal spring expands under gravitational force. A pointer needle rotates clockwise along dial tick marks (major intervals of 1 kg, minor tick marks of 100 g or 50 g).</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <span class="text-cyan-400 font-bold">•</span>
                            <span><strong>Digital Load Cell:</strong> Piezo-resistive strain gauges detect minuscule bending and convert physical compression directly into an electronic LCD readout with 1 g precision.</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <span class="text-cyan-400 font-bold">•</span>
                            <span><strong>Zero-Tare Function:</strong> Always verify that an empty pan indicates exactly 0 kg / 0 g before loading any objects to eliminate container weight bias.</span>
                        </li>
                    </ul>
                </div>
                <div class="mt-3 p-2.5 rounded-lg bg-cyan-950/40 border border-cyan-800/40 text-[11px] text-cyan-200">
                    💡 <strong>Reasonableness Rule:</strong> If an answer seems wildly too light or too heavy for an object's physical volume, re-check the unit immediately!
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c1_1",
                "question": "Which of the following recorded masses for a household object is completely UNREASONABLE and incorrect?",
                "options": [
                    "A family refrigerator weighing 62 kg",
                    "A standard school water bottle weighing 55 kg",
                    "A sack of whole wheat flour weighing 10 kg",
                    "An empty plastic bucket weighing 850 g"
                ],
                "answer": 1,
                "hint": "Think about whether a ten-year-old child could lift a school water bottle filled with drinking water.",
                "explanation": "A school water bottle holds around 750 mL to 1 L of water, giving it a total mass of roughly 1 kg. A recorded mass of 55 kg equals the weight of a grown adult, which is physically impossible for a handheld water bottle!"
            },
            {
                "id": "c1_2",
                "question": "An analog spring scale has dial markings where 0 kg to 1 kg is divided into 10 equal divisions. If the pointer rests on the 7th tick mark past 3 kg, what is the weight?",
                "options": [
                    "3 kg 7 g",
                    "3 kg 70 g",
                    "3 kg 700 g",
                    "37 kg"
                ],
                "answer": 2,
                "hint": "1 kg = 1,000 g. Find the value of one division: 1,000 g ÷ 10.",
                "explanation": "Since 1 kg = 1,000 g, each of the 10 divisions represents 1,000 ÷ 10 = 100 g. The 7th tick mark past 3 kg represents 3 kg + (7 × 100 g) = 3 kg 700 g (or 3,700 g)."
            }
        ]
    },
    {
        "id": 2,
        "title": "Weight Equivalence",
        "tagline": "Different Units but Same Measure • Double Number Lines for kg and g",
        "lecture": (
            "In the international metric system, the prefix kilo originates from the Greek word chilioi, which means exactly one thousand. Therefore, one kilogram is precisely equivalent to one thousand grams. This decimal relationship makes metric conversions remarkably systematic and predictable. To visualize this continuous equivalence, mathematicians use a double number line. On a double number line, two parallel calibrated number axes run side by side. The upper axis tracks mass in kilograms, while the lower axis tracks the exact same mass in grams. When the top marker points to zero kilograms, the bottom points to zero grams. When the top advances halfway to zero point five kilograms, which is half a kilogram, the bottom marker points directly to five hundred grams. Similarly, one quarter of a kilogram equals two hundred and fifty grams, three quarters of a kilogram aligns with seven hundred and fifty grams, and one full kilogram lines up perfectly with one thousand grams. Extending further, one and a half kilograms equals one thousand five hundred grams, two kilograms equals two thousand grams, and two and a quarter kilograms equals two thousand two hundred and fifty grams. Even though the numbers and unit symbols change, the physical measure remains identical. Double number lines clarify fraction and decimal relationships intuitively."
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>📏</span> The Double Number Line Principle
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    A double number line maps equivalent quantities on two synchronized axes. Notice how standard fractional kilogram benchmarks match specific gram totals:
                </p>
                <div class="space-y-2 text-xs">
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-300 font-medium">1/4 kg (Quarter kg)</span>
                        <span class="text-cyan-400">➔</span>
                        <span class="font-bold text-emerald-400">250 g</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-300 font-medium">1/2 kg (Half kg)</span>
                        <span class="text-cyan-400">➔</span>
                        <span class="font-bold text-emerald-400">500 g</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-300 font-medium">3/4 kg (Three-quarter kg)</span>
                        <span class="text-cyan-400">➔</span>
                        <span class="font-bold text-emerald-400">750 g</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-300 font-medium">1 kg (One Whole kg)</span>
                        <span class="text-cyan-400">➔</span>
                        <span class="font-bold text-emerald-400">1,000 g</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-300 font-medium">1 1/2 kg (One and a half kg)</span>
                        <span class="text-cyan-400">➔</span>
                        <span class="font-bold text-emerald-400">1,500 g</span>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>⚖️</span> Golden Equivalence Axiom
                    </h4>
                    <div class="p-4 rounded-xl bg-gradient-to-r from-amber-500/10 via-cyan-500/10 to-indigo-500/10 border border-amber-500/30 text-center my-3">
                        <div class="text-2xl font-black text-amber-300 tracking-wide">1 kg = 1,000 g</div>
                        <div class="text-[11px] text-slate-400 mt-1">1 g = 1/1,000 kg = 0.001 kg</div>
                    </div>
                    <ul class="text-xs text-slate-300 space-y-2 leading-relaxed">
                        <li class="flex items-start gap-2">
                            <span class="text-emerald-400 font-bold">✓</span>
                            <span><strong>Multiply by 1,000:</strong> To convert pure kilograms into grams, multiply the kilogram figure by 1,000 (shift decimal 3 places right).</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <span class="text-emerald-400 font-bold">✓</span>
                            <span><strong>Divide by 1,000:</strong> To convert pure grams into kilograms, divide the gram figure by 1,000 (shift decimal 3 places left).</span>
                        </li>
                    </ul>
                </div>
                <div class="p-2.5 rounded-lg bg-indigo-950/40 border border-indigo-800/40 text-[11px] text-indigo-200 mt-3">
                    📌 <strong>Memory Key:</strong> 1 kilogram is a thousand times heavier than 1 gram. Think of a 1 kg bag of sugar balanced by 1,000 individual 1-gram plastic counters!
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c2_1",
                "question": "A fruit vendor places a 3/4 kg iron weight on one pan of a balance beam. How many grams of grapes must be placed on the other pan to make it perfectly level?",
                "options": [
                    "340 g",
                    "750 g",
                    "500 g",
                    "1,750 g"
                ],
                "answer": 1,
                "hint": "1 kg = 1,000 g. What is 3/4 of 1,000 g?",
                "explanation": "3/4 of 1,000 g is calculated as (1,000 ÷ 4) × 3 = 250 × 3 = 750 g. So 3/4 kg is exactly equivalent to 750 g."
            },
            {
                "id": "c2_2",
                "question": "On a double number line connecting kilograms and grams, which point aligns directly underneath 2 1/4 kg?",
                "options": [
                    "2,140 g",
                    "2,250 g",
                    "2,500 g",
                    "2,750 g"
                ],
                "answer": 1,
                "hint": "2 1/4 kg = 2 kg + 1/4 kg. Convert both parts to grams.",
                "explanation": "2 kg = 2,000 g and 1/4 kg = 250 g. Adding them gives 2,000 g + 250 g = 2,250 g."
            }
        ]
    },
    {
        "id": 3,
        "title": "Weight Conversions",
        "tagline": "Let Us Find • Decomposing Compound Units & The 3-Digit Gram Rule",
        "lecture": (
            "When dealing with compound units like kilograms and grams together, precision in place value is essential. A common practical task is converting a mixed measurement such as three kilograms five hundred grams into total grams. We know that three kilograms equals three times one thousand, which is three thousand grams. Adding the five hundred grams yields three thousand five hundred grams. But beware of the famous place-value trap! Consider four kilograms seventy-five grams. A student might hastily write four thousand seven hundred and fifty grams. That is incorrect! Seventy-five grams has zero hundreds. Because one kilogram contains one thousand grams, the gram portion must always occupy three full decimal places. Therefore, four kilograms seventy-five grams is written as four thousand and seventy-five grams, with a zero in the hundreds column. Conversely, when converting a large gram number back into kilograms and grams, the thousands digit represents whole kilograms, while the remaining three digits represent grams. For example, six thousand and eighty grams splits into six kilograms and eighty grams. Eight thousand and five grams splits into eight kilograms and five grams. Remembering the three-digit gram placeholder rule guarantees that you will never misplace a zero during conversion."
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>🔄</span> Converting Compound Units to Total Grams
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    Multiply the kilogram number by 1,000 and add the gram number. Always pad grams with leading zeros if fewer than 3 digits:
                </p>
                <div class="space-y-2 text-xs">
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60">
                        <div class="flex justify-between font-bold text-slate-200">
                            <span>3 kg 500 g</span>
                            <span class="text-emerald-400">3,500 g</span>
                        </div>
                        <div class="text-[11px] text-slate-400 mt-1">3 × 1,000 g + 500 g = 3,000 g + 500 g</div>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60">
                        <div class="flex justify-between font-bold text-slate-200">
                            <span>5 kg 40 g</span>
                            <span class="text-emerald-400">5,040 g <span class="text-amber-400 text-[10px]">(not 5,400 g!)</span></span>
                        </div>
                        <div class="text-[11px] text-slate-400 mt-1">5 × 1,000 g + 040 g = 5,000 g + 40 g</div>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60">
                        <div class="flex justify-between font-bold text-slate-200">
                            <span>7 kg 6 g</span>
                            <span class="text-emerald-400">7,006 g <span class="text-amber-400 text-[10px]">(not 7,600 g!)</span></span>
                        </div>
                        <div class="text-[11px] text-slate-400 mt-1">7 × 1,000 g + 006 g = 7,000 g + 6 g</div>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>🔍</span> Converting Grams to Kilograms & Grams
                    </h4>
                    <p class="text-xs text-slate-300 leading-relaxed mb-3">
                        Split the number at the thousands place: the thousands part gives whole kilograms, and the last 3 digits give remaining grams.
                    </p>
                    <div class="space-y-2 text-xs">
                        <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                            <span class="font-mono text-cyan-300 font-bold">4,825 g</span>
                            <span class="text-slate-400">➔</span>
                            <span class="font-bold text-slate-200">4 kg 825 g</span>
                        </div>
                        <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                            <span class="font-mono text-cyan-300 font-bold">9,070 g</span>
                            <span class="text-slate-400">➔</span>
                            <span class="font-bold text-slate-200">9 kg 70 g</span>
                        </div>
                        <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                            <span class="font-mono text-cyan-300 font-bold">6,008 g</span>
                            <span class="text-slate-400">➔</span>
                            <span class="font-bold text-slate-200">6 kg 8 g</span>
                        </div>
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-amber-950/40 border border-amber-800/40 text-[11px] text-amber-200 mt-3">
                    ⚠️ <strong>Trap Alert:</strong> 4 kg 50 g is NOT 4,500 g! 4,500 g is 4 kg 500 g. 50 grams must be written as 050, yielding 4,050 g.
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c3_1",
                "question": "Anika buys a watermelon weighing 4 kg 65 g. What is the total mass of the watermelon in grams?",
                "options": [
                    "4,650 g",
                    "4,065 g",
                    "465 g",
                    "40,065 g"
                ],
                "answer": 1,
                "hint": "4 kg = 4,000 g. Add 65 g: 4,000 + 65.",
                "explanation": "4 kg = 4,000 g. Adding 65 g gives 4,000 + 65 = 4,065 g. 65 grams requires a leading zero in the hundreds place."
            },
            {
                "id": "c3_2",
                "question": "A parcel at the post office weighs exactly 8,040 grams. Express this weight in kilograms and grams.",
                "options": [
                    "80 kg 40 g",
                    "8 kg 400 g",
                    "8 kg 40 g",
                    "80 kg 4 g"
                ],
                "answer": 2,
                "hint": "Divide by 1,000. The quotient is kilograms, and the remainder is grams.",
                "explanation": "8,040 ÷ 1,000 = 8 with a remainder of 40. Therefore, 8,040 g = 8 kg 40 g."
            }
        ]
    },
    {
        "id": 4,
        "title": "Comparing Weights",
        "tagline": "Ordering & Inequality • Picnic Fruit Basket Analysis & Relational Signs",
        "lecture": (
            "When comparing different masses, especially when quantities are expressed in mixed units, we must adopt a structured comparison strategy. Imagine a school picnic basket containing four fresh fruits: a heavy watermelon weighing three kilograms two hundred grams, a pineapple weighing one kilogram eight hundred grams, a bag of crisp apples weighing two kilograms five hundred grams, and a box of ripe mangoes weighing one kilogram two hundred and fifty grams. Which fruit is the heaviest, and which is the lightest? The most reliable mathematical method is to convert every single quantity into a single common unit—grams. Let us convert: the watermelon is three thousand two hundred grams, the pineapple is one thousand eight hundred grams, the apples are two thousand five hundred grams, and the mangoes are one thousand two hundred and fifty grams. Now, comparing these four whole numbers is straightforward! Three thousand two hundred is the greatest, so the watermelon is the heaviest. One thousand two hundred and fifty is the smallest, so the mangoes are the lightest. Arranging them in descending order gives: watermelon greater than apples, greater than pineapple, greater than mangoes. In symbols: 3,200 g > 2,500 g > 1,800 g > 1,250 g. Always convert to identical units before applying inequality signs."
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>🧺</span> The Picnic Fruit Basket
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    Compare the four fruits by converting each to grams before sorting:
                </p>
                <div class="space-y-2 text-xs">
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-200 font-medium">🍉 Watermelon</span>
                        <span class="text-slate-400">3 kg 200 g</span>
                        <span class="font-mono font-bold text-emerald-400">3,200 g (Rank 1 - Heaviest)</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-200 font-medium">🍎 Apples</span>
                        <span class="text-slate-400">2 kg 500 g</span>
                        <span class="font-mono font-bold text-cyan-400">2,500 g (Rank 2)</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-200 font-medium">🍍 Pineapple</span>
                        <span class="text-slate-400">1 kg 800 g</span>
                        <span class="font-mono font-bold text-amber-400">1,800 g (Rank 3)</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-200 font-medium">🥭 Mangoes</span>
                        <span class="text-slate-400">1 kg 250 g</span>
                        <span class="font-mono font-bold text-rose-400">1,250 g (Rank 4 - Lightest)</span>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>⚖️</span> Inequality Comparisons (<, =, >)
                    </h4>
                    <p class="text-xs text-slate-300 leading-relaxed mb-3">
                        Always evaluate expressions by converting both sides to grams before comparing:
                    </p>
                    <div class="space-y-2 text-xs">
                        <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between font-mono">
                            <span class="text-slate-200">2 kg 400 g</span>
                            <span class="font-bold text-amber-400">></span>
                            <span class="text-slate-200">2,040 g</span>
                            <span class="text-[10px] text-slate-400">(2,400 g > 2,040 g)</span>
                        </div>
                        <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between font-mono">
                            <span class="text-slate-200">5 kg 80 g</span>
                            <span class="font-bold text-cyan-400"><</span>
                            <span class="text-slate-200">5,800 g</span>
                            <span class="text-[10px] text-slate-400">(5,080 g < 5,800 g)</span>
                        </div>
                        <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between font-mono">
                            <span class="text-slate-200">3 1/2 kg</span>
                            <span class="font-bold text-emerald-400">=</span>
                            <span class="text-slate-200">3,500 g</span>
                            <span class="text-[10px] text-slate-400">(3,500 g = 3,500 g)</span>
                        </div>
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-800/40 text-[11px] text-emerald-200 mt-3">
                    💡 <strong>Descending Order Chain:</strong> 3,200 g > 2,500 g > 1,800 g > 1,250 g (Watermelon > Apples > Pineapple > Mangoes).
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c4_1",
                "question": "Which relational symbol correctly completes the mathematical statement: 4 kg 90 g ____ 4,900 g?",
                "options": [
                    "> (greater than)",
                    "< (less than)",
                    "= (equal to)",
                    "≈ (approximately equal)"
                ],
                "answer": 1,
                "hint": "Convert 4 kg 90 g into grams first.",
                "explanation": "4 kg 90 g = 4,000 g + 90 g = 4,090 g. Comparing 4,090 g with 4,900 g gives 4,090 g < 4,900 g. Therefore, '<' is correct."
            },
            {
                "id": "c4_2",
                "question": "Four packages weigh: Package A = 2 kg 50 g, Package B = 2,500 g, Package C = 2 kg 450 g, Package D = 2,005 g. Which package is the lightest?",
                "options": [
                    "Package A",
                    "Package B",
                    "Package C",
                    "Package D"
                ],
                "answer": 3,
                "hint": "Convert all packages to grams: A = 2,050 g, B = 2,500 g, C = 2,450 g, D = 2,005 g.",
                "explanation": "In grams: A = 2,050 g, B = 2,500 g, C = 2,450 g, D = 2,005 g. 2,005 g is the smallest quantity, making Package D the lightest."
            }
        ]
    },
    {
        "id": 5,
        "title": "Milligram Measures",
        "tagline": "Smaller Units of Weight • The 1 g = 1,000 mg Micro-Scale",
        "lecture": (
            "While kilograms and grams are suitable for vegetables, groceries, and luggage, certain tiny objects require a vastly more sensitive unit of measurement: the milligram, abbreviated as mg. The prefix milli means one-thousandth. Therefore, exactly one thousand milligrams make up one single gram, and one milligram is one-thousandth of a gram. Where do we encounter milligrams in everyday life? Look closely at a tiny black worker ant scurrying across a garden path: its total mass is approximately five milligrams! A single grain of fine table salt weighs around one milligram. When you examine a paracetamol or vitamin tablet, the active medicinal ingredient is formulated in milligrams—such as five hundred milligrams of paracetamol, which equals exactly zero point five grams or half a gram. In jewelry, master goldsmiths measure gold and precious gemstones with milligram precision because even a fraction of a gram has significant monetary value. A small sugar sachet provided with tea contains five grams, which is equal to five thousand milligrams. A light gold nose-pin weighing zero point two grams equals two hundred milligrams. Just as one thousand grams make a kilogram, one thousand milligrams make a gram. This metric symmetry makes calculations intuitive and elegant."
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>🐜</span> Micro-Scale Real-World Benchmarks
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    Milligrams measure microscopic and ultra-light masses where grams are too coarse:
                </p>
                <div class="grid grid-cols-2 gap-2 text-xs">
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-300">🐜 Worker Ant</span>
                        <span class="font-bold text-emerald-400">~5 mg</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-300">🧂 Grain of Salt</span>
                        <span class="font-bold text-emerald-400">~1 mg</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-300">💊 Paracetamol Pill</span>
                        <span class="font-bold text-cyan-400">500 mg (0.5 g)</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-300">💍 Gold Ring</span>
                        <span class="font-bold text-amber-400">4,000 mg (4 g)</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-300">🪶 Pigeon Feather</span>
                        <span class="font-bold text-emerald-400">~15 mg</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-300">☕ Sugar Sachet</span>
                        <span class="font-bold text-cyan-400">5,000 mg (5 g)</span>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>🔬</span> The Milligram Conversion Rule
                    </h4>
                    <div class="p-4 rounded-xl bg-gradient-to-r from-emerald-500/10 via-cyan-500/10 to-indigo-500/10 border border-emerald-500/30 text-center my-3">
                        <div class="text-2xl font-black text-emerald-300 tracking-wide">1 g = 1,000 mg</div>
                        <div class="text-[11px] text-slate-400 mt-1">1 mg = 1/1,000 g = 0.001 g</div>
                    </div>
                    <ul class="text-xs text-slate-300 space-y-2 leading-relaxed">
                        <li class="flex items-start gap-2">
                            <span class="text-emerald-400 font-bold">•</span>
                            <span><strong>Grams to Milligrams:</strong> Multiply grams by 1,000 (e.g., 2.5 g × 1,000 = 2,500 mg).</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <span class="text-emerald-400 font-bold">•</span>
                            <span><strong>Milligrams to Grams:</strong> Divide milligrams by 1,000 (e.g., 750 mg ÷ 1,000 = 0.75 g = 3/4 g).</span>
                        </li>
                    </ul>
                </div>
                <div class="p-2.5 rounded-lg bg-cyan-950/40 border border-cyan-800/40 text-[11px] text-cyan-200 mt-3">
                    🏥 <strong>Medical Accuracy:</strong> Pharmaceutical prescriptions are strictly calculated in mg. Misplacing a single zero could deliver ten times the required medicine!
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c5_1",
                "question": "A doctor prescribes two 250 mg tablets of calcium twice every day. How many grams of calcium does the patient consume in one full day?",
                "options": [
                    "0.5 g",
                    "1 g",
                    "2 g",
                    "1,000 g"
                ],
                "answer": 1,
                "hint": "Calculate total milligrams first: 2 tablets × 250 mg = 500 mg per dose. 2 doses per day.",
                "explanation": "Each dose is 2 × 250 mg = 500 mg. With 2 doses per day, the daily total is 500 mg × 2 = 1,000 mg. Since 1,000 mg = 1 g, the patient takes exactly 1 g of calcium daily."
            },
            {
                "id": "c5_2",
                "question": "A goldsmith melts three small gold flakes weighing 350 mg, 450 mg, and 200 mg together. What is the total mass of the melted gold in grams?",
                "options": [
                    "1 g",
                    "10 g",
                    "0.1 g",
                    "100 g"
                ],
                "answer": 0,
                "hint": "Add the milligrams together: 350 + 450 + 200 mg.",
                "explanation": "350 mg + 450 mg + 200 mg = 1,000 mg. Since 1,000 mg = 1 g, the melted gold weighs exactly 1 g."
            }
        ]
    },
    {
        "id": 6,
        "title": "Heavy Metric Units",
        "tagline": "Did You Know? • Quintals, Metric Tonnes & The Elephant Boat Puzzle",
        "lecture": (
            "When agricultural grain harvests or massive animals like elephants and blue whales are weighed, kilograms become too small and cumbersome. To handle these heavy masses, commercial commerce and logistics introduce two larger metric units: the quintal and the metric tonne. One quintal equals exactly one hundred kilograms. A mandi wholesale farmer measures wheat, rice, and mustard harvests in quintals. Ten quintals equal one thousand kilograms, which defines exactly one metric tonne! In international shipping and transport, cargo containers and freight trains are rated in tonnes. An adult Asian elephant weighs approximately four metric tonnes, which equals four thousand kilograms or forty quintals! The blue whale, the largest animal on Earth, can reach an astonishing one hundred and fifty tonnes—that is one hundred and fifty thousand kilograms! How did ancient people weigh massive creatures without gigantic modern scales? An ingenious legend tells of an Indian king who vowed to donate gold equal to an elephant's weight. A wise minister loaded the royal elephant onto a large boat and painted a line along the water level on the hull. When the elephant stepped off, the boat floated higher. The minister then filled the boat with heavy stones until the water reached the painted line again, and weighed the stones individually on small balances. This brilliant Archimedean displacement solved the challenge!"
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>🚜</span> The Heavy Metric Hierarchy
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    Notice how base-100 and base-1,000 relationships connect kilograms to quintals and tonnes:
                </p>
                <div class="space-y-2 text-xs">
                    <div class="p-3 rounded-lg bg-slate-900/60 border border-slate-700/60">
                        <div class="flex justify-between font-bold text-amber-300 text-sm">
                            <span>1 Quintal (q)</span>
                            <span class="text-emerald-400">= 100 kg</span>
                        </div>
                        <p class="text-[11px] text-slate-400 mt-1">Used for mandi wholesale grain trading: wheat, mustard, cotton, onions.</p>
                    </div>
                    <div class="p-3 rounded-lg bg-slate-900/60 border border-slate-700/60">
                        <div class="flex justify-between font-bold text-cyan-300 text-sm">
                            <span>1 Metric Tonne (t)</span>
                            <span class="text-emerald-400">= 10 Quintals = 1,000 kg</span>
                        </div>
                        <p class="text-[11px] text-slate-400 mt-1">Used for cargo trucks, steel girders, ships, airplanes, and heavy machinery.</p>
                    </div>
                    <div class="p-3 rounded-lg bg-slate-900/60 border border-slate-700/60">
                        <div class="flex justify-between font-bold text-indigo-300 text-sm">
                            <span>🐘 Asian Elephant</span>
                            <span class="text-emerald-400">~4 Tonnes (4,000 kg = 40 q)</span>
                        </div>
                        <p class="text-[11px] text-slate-400 mt-1">A blue whale weighs ~150 tonnes = 150,000 kg = 1,500 quintals!</p>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>🚢</span> The King's Elephant Boat Puzzle
                    </h4>
                    <p class="text-xs text-slate-300 leading-relaxed mb-2">
                        Ancient Indian engineers utilized water buoyancy to weigh massive creatures without large scales:
                    </p>
                    <ol class="text-xs text-slate-300 space-y-1.5 list-decimal list-inside leading-relaxed">
                        <li><strong>Step 1:</strong> Walk the elephant onto a large flat-bottomed boat in a calm river.</li>
                        <li><strong>Step 2:</strong> Mark the exact waterline on the wooden hull with chalk or paint.</li>
                        <li><strong>Step 3:</strong> Lead the elephant off; the boat rises as displaced water drops.</li>
                        <li><strong>Step 4:</strong> Fill the boat with stones until it sinks back exactly to the chalk line.</li>
                        <li><strong>Step 5:</strong> Weigh the stones in small 50 kg sacks using standard balances!</li>
                    </ol>
                </div>
                <div class="p-2.5 rounded-lg bg-amber-950/40 border border-amber-800/40 text-[11px] text-amber-200 mt-3">
                    💡 <strong>Physical Law:</strong> A floating boat displaces an amount of water whose weight exactly equals the total mass placed inside the boat!
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c6_1",
                "question": "A farmer harvests 35 quintals of wheat from his field. How many metric tonnes and kilograms is this harvest equivalent to?",
                "options": [
                    "3.5 tonnes (3,500 kg)",
                    "35 tonnes (35,000 kg)",
                    "0.35 tonnes (350 kg)",
                    "350 tonnes (3,500 kg)"
                ],
                "answer": 0,
                "hint": "1 quintal = 100 kg. Multiply 35 by 100 to get kg, then divide by 1,000 to get tonnes.",
                "explanation": "35 quintals × 100 kg/quintal = 3,500 kg. Since 1,000 kg = 1 tonne, 3,500 kg ÷ 1,000 = 3.5 metric tonnes."
            },
            {
                "id": "c6_2",
                "question": "A transport truck is permitted to carry a maximum payload of 8 metric tonnes. If it is already loaded with 55 quintals of cement, how many more kilograms of cargo can it carry?",
                "options": [
                    "2,500 kg",
                    "3,500 kg",
                    "5,500 kg",
                    "1,500 kg"
                ],
                "answer": 0,
                "hint": "Convert everything to kilograms: 8 tonnes = 8,000 kg, 55 quintals = 5,500 kg.",
                "explanation": "Maximum limit = 8 tonnes = 8,000 kg. Current load = 55 quintals = 5,500 kg. Remaining capacity = 8,000 kg - 5,500 kg = 2,500 kg (or 25 quintals / 2.5 tonnes)."
            }
        ]
    },
    {
        "id": 7,
        "title": "Adding Weights",
        "tagline": "The Grocery Store • Column Addition & Base-1,000 Regrouping",
        "lecture": (
            "When shopping for family festivals or managing restaurant inventory, we often need to add multiple quantities of mixed weights together. The golden rule of adding compound units is to keep kilograms and grams in distinct, well-aligned vertical columns, just like place values in standard addition. Always start your addition from the rightmost column—the grams. If the sum of the grams column reaches or exceeds one thousand grams, regrouping is required because one thousand grams equals one whole kilogram! For instance, consider a wedding caterer who purchases forty-five kilograms seven hundred and fifty grams of basmati rice and thirty-eight kilograms six hundred and fifty grams of whole wheat flour. Setting them in columns: first, add the grams: seven hundred and fifty plus six hundred and fifty equals one thousand four hundred grams. We decompose one thousand four hundred grams into one thousand grams plus four hundred grams. The one thousand grams converts into one kilogram and is carried over to the kilograms column, leaving four hundred grams written in the grams total. Next, add the kilograms column: forty-five plus thirty-eight plus the one carried-over kilogram equals eighty-four kilograms. The total combined mass is eighty-four kilograms four hundred grams. Master column alignment and carry-over to add weights with complete confidence."
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>🛒</span> Wedding Caterer Grocery Addition
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    Study the vertical column algorithm. Notice how 1,400 g splits into 1 kg carry and 400 g remainder:
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/80 font-mono text-xs">
                    <div class="flex justify-between text-slate-400 border-b border-slate-700 pb-1 mb-2">
                        <span>ITEM</span>
                        <span class="w-16 text-right">KG</span>
                        <span class="w-20 text-right">GRAMS</span>
                    </div>
                    <div class="flex justify-between text-amber-400 text-[11px] mb-1">
                        <span>Regrouping Carry:</span>
                        <span class="w-16 text-right font-bold">(+1)</span>
                        <span class="w-20 text-right">-</span>
                    </div>
                    <div class="flex justify-between text-slate-200 py-1">
                        <span>Basmati Rice:</span>
                        <span class="w-16 text-right font-bold">45</span>
                        <span class="w-20 text-right font-bold">750</span>
                    </div>
                    <div class="flex justify-between text-slate-200 py-1 border-b border-slate-700">
                        <span>Wheat Flour:</span>
                        <span class="w-16 text-right font-bold">38</span>
                        <span class="w-20 text-right font-bold">650</span>
                    </div>
                    <div class="flex justify-between text-emerald-400 font-black text-sm pt-2">
                        <span>TOTAL:</span>
                        <span class="w-16 text-right">84 kg</span>
                        <span class="w-20 text-right">400 g</span>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>⚙️</span> The 3-Step Column Addition Algorithm
                    </h4>
                    <ol class="text-xs text-slate-300 space-y-2 list-decimal list-inside leading-relaxed">
                        <li>
                            <strong>Column Alignment:</strong> Separate kilograms into the left column and grams into the right column. Ensure grams have 3-digit representation.
                        </li>
                        <li>
                            <strong>Sum Grams First:</strong> Add the grams column. If the total is less than 1,000, write it down directly.
                        </li>
                        <li>
                            <strong>Base-1,000 Regrouping:</strong> If grams ≥ 1,000, divide by 1,000. Carry the whole quotient to the kg column and write the remainder in the grams column.
                        </li>
                        <li>
                            <strong>Sum Kilograms:</strong> Add all numbers in the kilograms column, including any carry-over.
                        </li>
                    </ol>
                </div>
                <div class="p-2.5 rounded-lg bg-indigo-950/40 border border-indigo-800/40 text-[11px] text-indigo-200 mt-3">
                    💡 <strong>Quick Check:</strong> 750 g + 650 g = 1,400 g = 1 kg 400 g. 45 kg + 38 kg + 1 kg = 84 kg. Final Answer: 84 kg 400 g.
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c7_1",
                "question": "A vegetable seller sells 16 kg 450 g of potatoes in the morning and 23 kg 800 g of potatoes in the evening. What is the total weight of potatoes sold?",
                "options": [
                    "39 kg 250 g",
                    "40 kg 250 g",
                    "40 kg 1,250 g",
                    "39 kg 1,250 g"
                ],
                "answer": 1,
                "hint": "Add the grams first: 450 + 800 = 1,250 g. Regroup 1,000 g as 1 kg.",
                "explanation": "Grams: 450 + 800 = 1,250 g = 1 kg 250 g. Kilograms: 16 + 23 + 1 (carried) = 40 kg. Total = 40 kg 250 g."
            },
            {
                "id": "c7_2",
                "question": "A dry fruit gift box contains 1 kg 250 g of almonds, 850 g of cashews, and 1 kg 400 g of walnuts. What is the total mass of the dry fruits?",
                "options": [
                    "3 kg 500 g",
                    "3 kg 50 g",
                    "2 kg 500 g",
                    "3,050 g"
                ],
                "answer": 0,
                "hint": "Add all grams together: 1,250 g + 850 g + 1,400 g.",
                "explanation": "Total in grams = 1,250 g + 850 g + 1,400 g = 3,500 g. Converting to compound units gives 3 kg 500 g (or 3 1/2 kg)."
            }
        ]
    },
    {
        "id": 8,
        "title": "Subtracting Weights",
        "tagline": "The Grocery Store • Column Subtraction with Base-1,000 Borrowing",
        "lecture": (
            "Subtracting mixed weights requires special care whenever the gram value in the top quantity is smaller than the gram value being subtracted. In ordinary base-ten arithmetic, borrowing brings over ten units from the next column. But in compound weight measurement, borrowing one unit from the kilogram column brings over exactly one thousand grams into the grams column! Let us examine a real-world story from a bustling restaurant. The kitchen starts the week with a fresh sack containing fifty kilograms two hundred grams of red onions. By Friday night, the chef has cooked twenty-seven kilograms six hundred and fifty grams of onions for gravies and curries. How many onions remain? Aligning columns: in the grams column, we must subtract six hundred and fifty grams from two hundred grams. That is impossible without borrowing. We borrow one kilogram from the fifty kilograms, reducing it to forty-nine kilograms. That one borrowed kilogram transforms into one thousand grams, which we immediately add to the existing two hundred grams, giving one thousand two hundred grams. Now, subtract the grams: one thousand two hundred minus six hundred and fifty equals five hundred and fifty grams. Next, subtract the kilograms: forty-nine minus twenty-seven equals twenty-two kilograms. Exactly twenty-two kilograms five hundred and fifty grams of onions remain in the kitchen."
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>🧅</span> Restaurant Onion Inventory Subtraction
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    Watch how 1 kg is borrowed and converted into +1,000 g in the grams column:
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/80 font-mono text-xs">
                    <div class="flex justify-between text-slate-400 border-b border-slate-700 pb-1 mb-2">
                        <span>STAGE</span>
                        <span class="w-16 text-right">KG</span>
                        <span class="w-20 text-right">GRAMS</span>
                    </div>
                    <div class="flex justify-between text-amber-400 text-[11px] mb-1">
                        <span>After Borrowing 1 kg:</span>
                        <span class="w-16 text-right font-bold">49</span>
                        <span class="w-20 text-right font-bold">(1,200)</span>
                    </div>
                    <div class="flex justify-between text-slate-200 py-1">
                        <span>Original Stock:</span>
                        <span class="w-16 text-right font-bold">50</span>
                        <span class="w-20 text-right font-bold">200</span>
                    </div>
                    <div class="flex justify-between text-slate-200 py-1 border-b border-slate-700">
                        <span>Consumed Onions:</span>
                        <span class="w-16 text-right font-bold">- 27</span>
                        <span class="w-20 text-right font-bold">- 650</span>
                    </div>
                    <div class="flex justify-between text-emerald-400 font-black text-sm pt-2">
                        <span>REMAINING:</span>
                        <span class="w-16 text-right">22 kg</span>
                        <span class="w-20 text-right">550 g</span>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>⚠️</span> The Base-1,000 Borrowing Trap
                    </h4>
                    <p class="text-xs text-slate-300 leading-relaxed mb-2">
                        Never borrow "10" or "100" from kilograms! Because 1 kg = 1,000 g, every borrowed kilogram adds exactly 1,000 to the existing grams:
                    </p>
                    <div class="p-3 rounded-lg bg-rose-950/40 border border-rose-800/40 text-xs text-rose-200 mb-2">
                        <span class="font-bold text-rose-300">❌ Common Mistake:</span> Turning 200 g into 300 g or 120 g by borrowing 1 or 10.
                    </div>
                    <div class="p-3 rounded-lg bg-emerald-950/40 border border-emerald-800/40 text-xs text-emerald-200">
                        <span class="font-bold text-emerald-300">✓ Correct Rule:</span> Borrowed 1 kg = +1,000 g. So 200 g + 1,000 g = 1,200 g. Then 1,200 g - 650 g = 550 g.
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-cyan-950/40 border border-cyan-800/40 text-[11px] text-cyan-200 mt-3">
                    🔍 <strong>Verification by Addition:</strong> Check your answer by adding: 22 kg 550 g + 27 kg 650 g = 50 kg 200 g. It matches perfectly!
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c8_1",
                "question": "A sandbag originally weighed 15 kg 100 g. Due to a small tear, 3 kg 750 g of sand leaked out. What is the remaining mass of the sandbag?",
                "options": [
                    "12 kg 350 g",
                    "11 kg 350 g",
                    "11 kg 650 g",
                    "12 kg 650 g"
                ],
                "answer": 1,
                "hint": "Borrow 1 kg (1,000 g) from 15 kg to make 1,100 g. Then subtract 750 g.",
                "explanation": "Borrow 1 kg from 15 kg, leaving 14 kg. Grams become 100 + 1,000 = 1,100 g. Grams: 1,100 - 750 = 350 g. Kilograms: 14 - 3 = 11 kg. Remaining sand = 11 kg 350 g."
            },
            {
                "id": "c8_2",
                "question": "A community kitchen has a container with 10 kg of sugar. After baking halwa, 4 kg 325 g of sugar is left. How much sugar was used in cooking?",
                "options": [
                    "5 kg 675 g",
                    "6 kg 675 g",
                    "5 kg 325 g",
                    "6 kg 775 g"
                ],
                "answer": 0,
                "hint": "Write 10 kg as 10 kg 000 g. Borrow 1 kg to make 9 kg 1,000 g.",
                "explanation": "10 kg 000 g - 4 kg 325 g: Borrow 1 kg from 10 kg to get 9 kg 1,000 g. Grams: 1,000 - 325 = 675 g. Kilograms: 9 - 4 = 5 kg. Used sugar = 5 kg 675 g."
            }
        ]
    }
]

