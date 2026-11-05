# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 6: The Dairy Farm - Part 2 (Slides 9 to 16)
NEP 2020 / Joyful Mathematics
"""

SLIDES_PART2 = [
    {
        "id": 9,
        "title": "Expanded Methods",
        "tag": "Let Us Multiply • Nida's and John's Box & Grid Algorithms",
        "lecture": (
            "When multiplying larger multi-digit numbers, breaking numbers apart by place value ensures no cross-multiplication is "
            "missed. In the dairy farm accounts office, students learn Nida's and John's expanded grid methods. Suppose we need to "
            "multiply 69 by 45 to calculate the cost of 45 feed sacks priced at 69 rupees each. First, decompose both numbers into "
            "tens and ones: 69 becomes 60 plus 9, and 45 becomes 40 plus 5. Draw a two-by-two grid with four rectangular cells. "
            "In cell one, multiply 60 by 40: 6 times 4 is 24, plus two zeros gives 2,400. In cell two, multiply 9 by 40 to get 360. "
            "In cell three, multiply 60 by 5 to get 300. In cell four, multiply 9 by 5 to get 45. Now sum these four partial products! "
            "Add the top row: 2,400 plus 360 equals 2,760. Add the bottom row: 300 plus 45 equals 345. Finally, combine the two rows: "
            "2,760 plus 345 gives 3,105 rupees! John's box method provides complete visual clarity, guaranteeing that every single "
            "place-value interaction is accurately tracked before final addition."
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    The expanded box/grid method decomposes multi-digit factors by place value, computing individual partial products before summing them.
                </p>
                <div class="bg-slate-800/80 p-4 rounded-xl border border-cyan-500/30">
                    <h4 class="font-bold text-cyan-400 mb-2 flex items-center justify-between">
                        <span>📦 Calculating 69 × 45 via 2×2 Partial Product Grid</span>
                        <span class="text-xs font-mono bg-cyan-950 px-2 py-0.5 rounded text-cyan-300">69 = 60 + 9 | 45 = 40 + 5</span>
                    </h4>
                    <div class="grid grid-cols-3 gap-2 text-center text-xs font-mono my-3 max-w-md mx-auto">
                        <div class="p-2 bg-slate-900/60 rounded font-bold text-slate-400 flex items-center justify-center">×</div>
                        <div class="p-2 bg-indigo-900/40 rounded font-bold text-indigo-300 border border-indigo-500/30">60</div>
                        <div class="p-2 bg-indigo-900/40 rounded font-bold text-indigo-300 border border-indigo-500/30">9</div>

                        <div class="p-2 bg-emerald-900/40 rounded font-bold text-emerald-300 border border-emerald-500/30 flex items-center justify-center">40</div>
                        <div class="p-3 bg-slate-900/80 rounded border border-slate-700">
                            <span class="text-slate-400 block text-[10px]">60 × 40</span>
                            <span class="text-amber-300 font-bold text-sm">2,400</span>
                        </div>
                        <div class="p-3 bg-slate-900/80 rounded border border-slate-700">
                            <span class="text-slate-400 block text-[10px]">9 × 40</span>
                            <span class="text-amber-300 font-bold text-sm">360</span>
                        </div>

                        <div class="p-2 bg-emerald-900/40 rounded font-bold text-emerald-300 border border-emerald-500/30 flex items-center justify-center">5</div>
                        <div class="p-3 bg-slate-900/80 rounded border border-slate-700">
                            <span class="text-slate-400 block text-[10px]">60 × 5</span>
                            <span class="text-amber-300 font-bold text-sm">300</span>
                        </div>
                        <div class="p-3 bg-slate-900/80 rounded border border-slate-700">
                            <span class="text-slate-400 block text-[10px]">9 × 5</span>
                            <span class="text-amber-300 font-bold text-sm">45</span>
                        </div>
                    </div>
                    <div class="flex flex-wrap items-center justify-center gap-3 text-xs font-mono pt-2 border-t border-slate-700">
                        <span>Row 1: 2,400 + 360 = <strong>2,760</strong></span>
                        <span class="text-slate-500">+</span>
                        <span>Row 2: 300 + 45 = <strong>345</strong></span>
                        <span class="text-slate-500">=</span>
                        <span class="text-emerald-400 font-bold text-sm bg-emerald-950/60 px-3 py-1 rounded-lg border border-emerald-500/40">Total: 3,105</span>
                    </div>
                </div>
                <div class="p-3 bg-emerald-950/40 border border-emerald-500/30 rounded-lg text-xs text-emerald-200">
                    <strong>Algorithmic Guarantee:</strong> Decomposing into <em>(a + b) × (c + d) = ac + ad + bc + bd</em> prevents place-value omission errors.
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_9",
        "checkpoints": [
            {
                "question": "In the box multiplication of 48 × 35, what are the four partial products?",
                "options": [
                    "1,200, 240, 200, 40",
                    "1,200, 240, 200, 50",
                    "1,400, 200, 200, 40",
                    "1,200, 280, 160, 40"
                ],
                "correct": 0,
                "explanation": "48 = 40 + 8 and 35 = 30 + 5. The partial products are: 40 × 30 = 1,200; 8 × 30 = 240; 40 × 5 = 200; 8 × 5 = 40. Sum = 1,200 + 240 + 200 + 40 = 1,680."
            },
            {
                "question": "What is 32 × 8 using Nida's expanded method?",
                "options": [
                    "(30 × 8) + (2 × 8) = 240 + 16 = 256",
                    "(30 × 8) + (2 × 8) = 240 + 8 = 248",
                    "(30 + 2) × (8 + 8) = 32 × 16 = 512",
                    "240 - 16 = 224"
                ],
                "correct": 0,
                "explanation": "32 = 30 + 2. Multiply each part by 8: (30 × 8) = 240, (2 × 8) = 16. Sum = 240 + 16 = 256."
            }
        ]
    },
    {
        "id": 10,
        "title": "Everyday Arithmetic",
        "tag": "Let Us Do • Cinema Seating, Cricket Statistics & Bulk Procurement",
        "lecture": (
            "Everyday life presents rich scenarios where multi-step arithmetic guides decisions. Consider a cricket match attended by the "
            "dairy village youth club. A star batter plays a magnificent innings consisting of 14 boundaries of 4 runs each, 8 towering "
            "sixes, and 32 singles ran between the wickets. Let us compute her total score: 14 boundaries times 4 runs equals 56 runs; "
            "8 sixes times 6 runs equals 48 runs; and 32 singles times 1 run equals 32 runs. Adding them together: 56 plus 48 is 104, "
            "and 104 plus 32 gives 136 total runs scored! Next, let us visit the district cinema hall, which features 28 rows with "
            "35 seats in every row. How many tickets can be sold for a houseful show? 28 times 35: using doubling and halving, halve "
            "28 to 14 and double 35 to 70; then 14 times 70 equals 980 seats! Finally, in the grain market, the cooperative purchases "
            "45 bags of cattle feed at 620 rupees per bag. 45 times 600 is 27,000, and 45 times 20 is 900; total cost is 27,900 rupees! "
            "Mathematics empowers us to tally, manage, and verify real transactions instantly."
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    Composite arithmetic problems require calculating sub-products for distinct categories and combining them into a final total:
                </p>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
                    <div class="bg-slate-800/80 p-3.5 rounded-xl border border-amber-500/30">
                        <h4 class="font-bold text-amber-400 mb-1.5 flex items-center gap-1.5">
                            <span>🏏</span> Cricket Match Breakdown
                        </h4>
                        <p class="text-slate-300">• 14 Fours: 14 × 4 = <strong>56 runs</strong></p>
                        <p class="text-slate-300">• 8 Sixes: 8 × 6 = <strong>48 runs</strong></p>
                        <p class="text-slate-300">• 32 Singles: 32 × 1 = <strong>32 runs</strong></p>
                        <p class="font-mono text-amber-300 font-bold text-sm mt-1 pt-1 border-t border-slate-700">Total = 136 runs</p>
                    </div>
                    <div class="bg-slate-800/80 p-3.5 rounded-xl border border-indigo-500/30">
                        <h4 class="font-bold text-indigo-400 mb-1.5 flex items-center gap-1.5">
                            <span>🎬</span> Cinema Seating Capacity
                        </h4>
                        <p class="text-slate-300">• 28 rows × 35 seats/row</p>
                        <p class="text-slate-300 font-mono">• Doubling & Halving:</p>
                        <p class="text-slate-300 font-mono">• = 14 × 70</p>
                        <p class="font-mono text-indigo-300 font-bold text-sm mt-1 pt-1 border-t border-slate-700">Total = 980 seats</p>
                    </div>
                    <div class="bg-slate-800/80 p-3.5 rounded-xl border border-emerald-500/30">
                        <h4 class="font-bold text-emerald-400 mb-1.5 flex items-center gap-1.5">
                            <span>🌾</span> Cattle Feed Procurement
                        </h4>
                        <p class="text-slate-300">• 45 bags × ₹ 620/bag</p>
                        <p class="text-slate-300 font-mono">• 45 × 600 = ₹ 27,000</p>
                        <p class="text-slate-300 font-mono">• 45 × 20 = ₹ 900</p>
                        <p class="font-mono text-emerald-300 font-bold text-sm mt-1 pt-1 border-t border-slate-700">Total = ₹ 27,900</p>
                    </div>
                </div>
                <div class="p-3 bg-slate-800/80 border border-slate-600 rounded-lg text-xs text-slate-300">
                    <strong>Multi-Step Checklist:</strong> 1. Segment the problem into clear categories. 2. Multiply unit rates by quantities. 3. Sum the partial components.
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_10",
        "checkpoints": [
            {
                "question": "A school library has 16 cupboards, each with 5 shelves, and each shelf contains 25 books. How many books are there in total?",
                "options": ["2,000 books", "1,800 books", "2,400 books", "1,600 books"],
                "correct": 0,
                "explanation": "Total books = 16 × 5 × 25. Grouping: 16 × (5 × 25) = 16 × 125, or (16 × 5) × 25 = 80 × 25. 80 × 25 = (80 ÷ 4) × (25 × 4) = 20 × 100 = 2,000 books!"
            },
            {
                "question": "A village merchant sells 35 bags of basmati rice at ₹ 840 per bag. What is the total sale value?",
                "options": ["₹ 29,400", "₹ 28,400", "₹ 30,200", "₹ 26,800"],
                "correct": 0,
                "explanation": "35 × 840 = 35 × (800 + 40) = (35 × 800) + (35 × 40) = 28,000 + 1,400 = ₹ 29,400."
            }
        ]
    },
    {
        "id": 11,
        "title": "Dairy Cooperative",
        "tag": "Advanced Column Multiplication • Multi-Digit Standard Algorithm",
        "lecture": (
            "Now let us examine the crown jewel of written arithmetic: the standard vertical column multiplication algorithm, used "
            "by accountants at the dairy cooperative. Mili's father manages milk collection from 453 high-yielding indigenous Gir cows. "
            "If each cow produces an average of 13 litres of milk in a day, how many litres does the cooperative collect? We set up 453 "
            "multiplied by 13 vertically. Step one: multiply 453 by the 3 units: 3 times 3 is 9; 3 times 5 tens is 15 tens, write 5 "
            "and carry 1; 3 times 4 hundreds is 12 hundreds plus 1 carry is 13 hundreds. The first partial product is 1,359. Step two: "
            "multiply 453 by the 1 in the tens place, which has a value of 10. Crucially, place a zero in the units column as a place "
            "holder! Then 1 times 453 gives 4,530. Step three: add the two partial products: 1,359 plus 4,530 equals 5,889 litres of "
            "milk! For three-digit by three-digit numbers, such as 574 tins of ghee sold at 125 rupees each, we generate three partial "
            "products: multiplying by 5 ones, by 2 tens (20), and by 1 hundred (100). Adding 2,870 plus 11,480 plus 57,400 yields "
            "71,750 rupees. Mastering column multiplication empowers us to handle numbers of any magnitude!"
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    The standard column algorithm streamlines multi-digit multiplication by recording unit carries and aligning partial products using place-value zeros.
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-indigo-500/30">
                        <h4 class="font-bold text-indigo-400 mb-2 font-mono">Gir Cow Milk: 453 × 13</h4>
                        <div class="font-mono text-sm space-y-1 bg-slate-900/60 p-3 rounded-lg">
                            <p class="text-right text-slate-400">453</p>
                            <p class="text-right text-slate-400">× &nbsp;13</p>
                            <div class="border-b border-slate-600 my-1"></div>
                            <p class="text-right text-cyan-300">1359 &nbsp;<span class="text-[10px] text-slate-400">(453 × 3)</span></p>
                            <p class="text-right text-amber-300">+ 4530 &nbsp;<span class="text-[10px] text-slate-400">(453 × 10)</span></p>
                            <div class="border-b border-slate-600 my-1"></div>
                            <p class="text-right text-emerald-400 font-bold text-base">5889</p>
                        </div>
                        <p class="text-[11px] text-slate-300 mt-2">• Place value zero in 4,530 is mandatory because 1 represents 1 Ten (10)!</p>
                    </div>
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-violet-500/30">
                        <h4 class="font-bold text-violet-400 mb-2 font-mono">Ghee Sales: 574 × 125</h4>
                        <div class="font-mono text-xs space-y-1 bg-slate-900/60 p-3 rounded-lg">
                            <p class="text-right text-slate-400">574</p>
                            <p class="text-right text-slate-400">× 125</p>
                            <div class="border-b border-slate-600 my-1"></div>
                            <p class="text-right text-cyan-300">2870 &nbsp;<span class="text-[10px] text-slate-400">(574 × 5)</span></p>
                            <p class="text-right text-amber-300">11480 &nbsp;<span class="text-[10px] text-slate-400">(574 × 20)</span></p>
                            <p class="text-right text-purple-300">+ 57400 &nbsp;<span class="text-[10px] text-slate-400">(574 × 100)</span></p>
                            <div class="border-b border-slate-600 my-1"></div>
                            <p class="text-right text-emerald-400 font-bold text-sm">71750</p>
                        </div>
                        <p class="text-[11px] text-slate-300 mt-2">• 3-digit multiplier generates 3 partial products aligned with 0, 1, and 2 zeros.</p>
                    </div>
                </div>
                <div class="p-3 bg-blue-950/40 border border-blue-500/30 rounded-lg text-xs text-blue-200">
                    <strong>The Zero Invariant:</strong> When multiplying by the tens digit, append one zero; by the hundreds digit, append two zeros; by the thousands digit, append three zeros.
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_11",
        "checkpoints": [
            {
                "question": "What is the product of 324 × 26 using the standard column algorithm?",
                "options": ["8,424", "7,824", "8,224", "8,624"],
                "correct": 0,
                "explanation": "First partial product: 324 × 6 = 1,944. Second partial product: 324 × 20 = 6,480. Sum = 1,944 + 6,480 = 8,424."
            },
            {
                "question": "In the multiplication of 615 × 42, why do we write 24,600 as the second partial product?",
                "options": [
                    "Because 4 is in the tens place, so we are multiplying 615 by 40",
                    "Because 615 × 4 = 2,460 and we add a random zero",
                    "Because we must always round numbers to the hundreds",
                    "Because the product must end with 00"
                ],
                "correct": 0,
                "explanation": "The digit 4 in 42 has a place value of 40 (4 tens). 615 × 40 = 24,600."
            }
        ]
    },
    {
        "id": 12,
        "title": "Error Analysis",
        "tag": "Check, Check! • Diagnosing Common Computational Bugs",
        "lecture": (
            "A true mathematician is not just someone who solves problems, but someone who can inspect mathematical work, spot mistakes, "
            "and explain why they happened. In our 'Check, Check!' clinic, students analyze common errors in multiplication. Let us look "
            "at the most famous bug: The Missing Zero Trap. Suppose a student multiplies 54 by 23. In the first line, 54 times 3 gives 162. "
            "In the second line, the student multiplies 54 by 2 and writes 108 directly beneath 162 without shifting! Adding 162 plus 108 "
            "gives 270. Is 270 reasonable? Quick estimation: 50 times 20 is 1,000! How could 54 times 23 be only 270? The mistake is clear: "
            "the student multiplied by 2 instead of 20! The second line should be 1,080, giving 162 plus 1,080 equals 1,242. Another common "
            "trap is Premature Carry Addition: when multiplying 47 by 3, a student multiplies 3 times 7 to get 21, writes 1 and carries 2; "
            "then adds the carried 2 to 4 to make 6, and multiplies 3 times 6 to get 18, writing 181! That is wrong: you must multiply "
            "first: 3 times 4 is 12, then add the carried 2 to get 14, giving 141. By checking place values and estimating products, "
            "we safeguard our work against errors."
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    Diagnosing computational errors reveals the underlying structure of algorithms and strengthens mathematical rigor:
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-rose-500/30">
                        <h4 class="font-bold text-rose-400 mb-2 flex items-center gap-2">
                            <span>❌</span> Trap 1: The Missing Zero Placeholder
                        </h4>
                        <div class="font-mono bg-slate-900/60 p-2.5 rounded-lg space-y-1 mb-2">
                            <p class="text-slate-400">54 × 23</p>
                            <p class="text-slate-300">&nbsp; 162 &nbsp;<span class="text-emerald-400">✓ (54 × 3)</span></p>
                            <p class="text-rose-400 font-bold">+ 108 &nbsp;❌ Missing tens zero!</p>
                            <p class="text-slate-400">-----</p>
                            <p class="text-rose-400 font-bold">&nbsp; 270 &nbsp;❌ Nonsensical (50 × 20 = 1,000!)</p>
                        </div>
                        <p class="text-emerald-300 font-semibold">• Correction: Second row must be <strong>1,080</strong> (54 × 20). Correct sum = <strong>1,242</strong>.</p>
                    </div>
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-amber-500/30">
                        <h4 class="font-bold text-amber-400 mb-2 flex items-center gap-2">
                            <span>❌</span> Trap 2: Premature Carry Addition
                        </h4>
                        <div class="font-mono bg-slate-900/60 p-2.5 rounded-lg space-y-1 mb-2">
                            <p class="text-slate-400">47 × 3 (carry 2 from 3 × 7 = 21)</p>
                            <p class="text-rose-400 font-bold">• Wrong: (4 + 2) × 3 = 6 × 3 = 18 → 181 ❌</p>
                            <p class="text-emerald-300 font-bold">• Right: (4 × 3) + 2 = 12 + 2 = 14 → 141 ✓</p>
                        </div>
                        <p class="text-slate-300">• Always multiply the place value first, then add the carried amount!</p>
                    </div>
                </div>
                <div class="p-3 bg-amber-950/40 border border-amber-500/30 rounded-lg text-xs text-amber-200">
                    <strong>Sanity Check Heuristic:</strong> Before finalizing any multi-digit product, perform a quick <em>Rough Estimate</em> by rounding both numbers to their highest place value.
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_12",
        "checkpoints": [
            {
                "question": "A student calculates 38 × 42 and gets 304. By rough estimation, why is this answer impossible?",
                "options": [
                    "38 is near 40 and 42 is near 40, so 40 × 40 = 1,600; 304 is far too small",
                    "Because 38 × 42 must be an odd number",
                    "Because 38 × 42 must end with 8",
                    "Because 38 + 42 = 80"
                ],
                "correct": 0,
                "explanation": "Rough estimation: 40 × 40 = 1,600. An answer of 304 means the student forgot the tens place value zero in the second partial product (actual product is 1,596)."
            },
            {
                "question": "In the multiplication 65 × 14, the student writes partial products 260 and 65, getting 325. What was the exact error?",
                "options": [
                    "Wrote 65 instead of 650 (failed to multiply by 10)",
                    "Multiplied 65 by 4 incorrectly",
                    "Subtracted instead of adding partial products",
                    "Forgot to carry 2"
                ],
                "correct": 0,
                "explanation": "In 65 × 14, the 1 represents 10. The second partial product should be 65 × 10 = 650, not 65. The correct answer is 260 + 650 = 910."
            }
        ]
    },
    {
        "id": 13,
        "title": "Derivative Facts",
        "tag": "Flexible Strategies • Fact Family Derivations & Special Endings",
        "lecture": (
            "Suppose an accountant discovers that 17 times 23 equals 391. Do you need to set up a long column calculation to find "
            "17 times 46? Absolutely not! Look closely at the numbers: 46 is exactly double 23. Therefore, 17 times 46 must be exactly "
            "double 391! 391 doubled is 782. What about 34 times 23? Here, 34 is double 17, while 23 stays unchanged. So 34 times 23 "
            "is also 391 times 2, which equals 782! What about 17 times 24? 24 is just one more group of 17 than 23! So simply add 17 "
            "to 391: 391 plus 17 equals 408. What about 17 times 22? Subtract one group of 17: 391 minus 17 equals 374! Knowing a "
            "single anchor fact unlocks a whole constellation of derivative facts. We also exploit numbers ending in 25, 75, or 125: "
            "since 25 is 100 divided by 4, 32 times 25 is 32 divided by 4 times 100, which is 8 times 100 equals 800. Since 125 is "
            "1,000 divided by 8, 48 times 125 is 48 divided by 8 times 1,000, which is 6,000! Flexible thinking turns complex facts "
            "into child's play."
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    A single known multiplication fact serves as a powerful anchor to derive neighboring and scaled products algebraically:
                </p>
                <div class="bg-slate-800/80 p-4 rounded-xl border border-teal-500/30">
                    <h4 class="font-bold text-teal-400 mb-3 text-center">
                        Anchor Fact: <span class="font-mono text-amber-300 text-base bg-slate-900/80 px-3 py-1 rounded-lg border border-amber-500/30">17 × 23 = 391</span>
                    </h4>
                    <div class="grid grid-cols-2 md:grid-cols-4 gap-2.5 text-xs font-mono text-center">
                        <div class="p-2.5 bg-slate-900/60 rounded-lg border border-slate-700">
                            <span class="text-slate-400 block text-[10px]">Double Factor 2</span>
                            <span class="font-bold text-slate-200">17 × 46</span>
                            <span class="text-emerald-400 block font-bold text-sm mt-1">391 × 2 = 782</span>
                        </div>
                        <div class="p-2.5 bg-slate-900/60 rounded-lg border border-slate-700">
                            <span class="text-slate-400 block text-[10px]">Double Factor 1</span>
                            <span class="font-bold text-slate-200">34 × 23</span>
                            <span class="text-emerald-400 block font-bold text-sm mt-1">391 × 2 = 782</span>
                        </div>
                        <div class="p-2.5 bg-slate-900/60 rounded-lg border border-slate-700">
                            <span class="text-slate-400 block text-[10px]">+1 Group of 17</span>
                            <span class="font-bold text-slate-200">17 × 24</span>
                            <span class="text-cyan-400 block font-bold text-sm mt-1">391 + 17 = 408</span>
                        </div>
                        <div class="p-2.5 bg-slate-900/60 rounded-lg border border-slate-700">
                            <span class="text-slate-400 block text-[10px]">-1 Group of 17</span>
                            <span class="font-bold text-slate-200">17 × 22</span>
                            <span class="text-cyan-400 block font-bold text-sm mt-1">391 - 17 = 374</span>
                        </div>
                    </div>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
                    <div class="bg-slate-800/80 p-3 rounded-xl border border-indigo-500/30">
                        <h4 class="font-bold text-indigo-400 mb-1">Shortcut for × 25</h4>
                        <p class="text-slate-300">• Since 25 = 100 ÷ 4, divide factor by 4 and append two 0s:</p>
                        <p class="font-mono text-emerald-300 font-bold mt-1">• 44 × 25 = (44 ÷ 4) × 100 = 11 × 100 = 1,100</p>
                    </div>
                    <div class="bg-slate-800/80 p-3 rounded-xl border border-purple-500/30">
                        <h4 class="font-bold text-purple-400 mb-1">Shortcut for × 125</h4>
                        <p class="text-slate-300">• Since 125 = 1,000 ÷ 8, divide factor by 8 and append three 0s:</p>
                        <p class="font-mono text-purple-300 font-bold mt-1">• 56 × 125 = (56 ÷ 8) × 1,000 = 7 × 1,000 = 7,000</p>
                    </div>
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_13",
        "checkpoints": [
            {
                "question": "Given that 19 × 21 = 399, what is 19 × 22 without performing full multiplication?",
                "options": [
                    "399 + 19 = 418",
                    "399 + 21 = 420",
                    "399 × 2 = 798",
                    "399 + 1 = 400"
                ],
                "correct": 0,
                "explanation": "19 × 22 is one more group of 19 than 19 × 21. Therefore, 399 + 19 = 418."
            },
            {
                "question": "Compute 64 × 125 using the fractional power shortcut:",
                "options": ["8,000", "7,800", "8,200", "6,400"],
                "correct": 0,
                "explanation": "125 = 1,000 ÷ 8. So 64 × 125 = (64 ÷ 8) × 1,000 = 8 × 1,000 = 8,000."
            }
        ]
    },
    {
        "id": 14,
        "title": "King's Reward",
        "tag": "The King's Reward • Exponential Growth Puzzle",
        "lecture": (
            "Prepare to be astonished by the sheer power of repeated multiplication! In an ancient kingdom, a clever dairy farmer "
            "solved a royal crisis and was offered a reward by the king for seven days. The king gave three options. Choice A: Receive "
            "a handsome flat sum of 100,000 gold coins every single day. Over seven days, that equals 7 times 100,000, which is "
            "700,000 gold coins. Choice B: Receive 2 coins on day one, and have the amount double each day! On day one, 2 coins; day "
            "two, 4; day three, 8; day four, 16; day five, 32; day six, 64; and day seven, 128 coins. The total is only 254 coins. "
            "Choice C: Start with just 1 coin on day one, but multiply the daily amount by 5 every single day! Day one gives 1 coin; "
            "day two gives 5; day three gives 25; day four gives 125; day five gives 625; day six gives 3,125; and on day seven, "
            "gives 15,625 coins! The total for seven days is 19,531 coins. While Choice A wins for seven days, see what happens if the "
            "reward continues for just ten days! Under Choice C, day eight is 78,125; day nine is 390,625; and day ten is nearly two "
            "million coins! Repeated multiplication expands with explosive, unstoppable speed."
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    Comparing linear addition against exponential multiplication reveals how multiplicative growth rapidly overtakes additive amounts over time:
                </p>
                <div class="overflow-x-auto">
                    <table class="w-full text-xs text-left bg-slate-800/80 rounded-xl border border-slate-700">
                        <thead class="bg-slate-700/60 text-emerald-300">
                            <tr>
                                <th class="p-2">Day</th>
                                <th class="p-2">Choice A (₹ 100k Daily)</th>
                                <th class="p-2">Choice B (Doubling × 2)</th>
                                <th class="p-2">Choice C (Quintupling × 5)</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-700/60 text-slate-200 font-mono">
                            <tr>
                                <td class="p-1.5 font-bold">Day 1</td>
                                <td class="p-1.5">100,000</td>
                                <td class="p-1.5">2</td>
                                <td class="p-1.5 text-amber-300">1</td>
                            </tr>
                            <tr>
                                <td class="p-1.5 font-bold">Day 3</td>
                                <td class="p-1.5">100,000</td>
                                <td class="p-1.5">8</td>
                                <td class="p-1.5 text-amber-300">25</td>
                            </tr>
                            <tr>
                                <td class="p-1.5 font-bold">Day 5</td>
                                <td class="p-1.5">100,000</td>
                                <td class="p-1.5">32</td>
                                <td class="p-1.5 text-amber-300">625</td>
                            </tr>
                            <tr>
                                <td class="p-1.5 font-bold">Day 7</td>
                                <td class="p-1.5">100,000</td>
                                <td class="p-1.5">128</td>
                                <td class="p-1.5 text-amber-300 font-bold">15,625</td>
                            </tr>
                            <tr class="bg-slate-900/60 font-bold">
                                <td class="p-2 text-emerald-400">7-Day Total</td>
                                <td class="p-2 text-emerald-400">₹ 700,000 (Winner for 7 days)</td>
                                <td class="p-2 text-slate-400">₹ 254</td>
                                <td class="p-2 text-amber-400">₹ 19,531</td>
                            </tr>
                            <tr class="bg-emerald-950/40 font-bold">
                                <td class="p-2 text-cyan-300">Day 10 Single Day</td>
                                <td class="p-2 text-slate-400">₹ 100,000</td>
                                <td class="p-2 text-slate-400">₹ 1,024</td>
                                <td class="p-2 text-cyan-300">₹ 1,953,125 (Multiplication explodes!)</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="p-3 bg-amber-950/40 border border-amber-500/30 rounded-lg text-xs text-amber-200">
                    <strong>Exponential Insight:</strong> While addition adds constant amounts, multiplication scales the existing quantity by a factor, compounding into astronomical figures.
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_14",
        "checkpoints": [
            {
                "question": "In Choice B, if day 1 is 2 coins and it doubles each day, how many coins are received on Day 6?",
                "options": ["64 coins", "32 coins", "128 coins", "12 coins"],
                "correct": 0,
                "explanation": "Day 1 = 2; Day 2 = 4; Day 3 = 8; Day 4 = 16; Day 5 = 32; Day 6 = 64 coins."
            },
            {
                "question": "In Choice C (multiplying by 5 daily), how many coins are received on Day 5 starting with 1 coin on Day 1?",
                "options": ["625 coins", "125 coins", "3,125 coins", "25 coins"],
                "correct": 0,
                "explanation": "Day 1 = 1; Day 2 = 5; Day 3 = 25; Day 4 = 125; Day 5 = 125 × 5 = 625 coins."
            }
        ]
    },
    {
        "id": 15,
        "title": "Number Patterns",
        "tag": "Multiplication Patterns • Palindromic Mountains & Grid Extremes",
        "lecture": (
            "Mathematics is the study of visual and numerical harmony. When we multiply special sequences, breathtaking patterns "
            "emerge. Consider multiplying numbers composed only of the digit 1, known as repunits. Look at this symmetry: 1 times 1 "
            "is 1. 11 times 11 is 121. 111 times 111 is 12,321. 1,111 times 1,111 is 1,234,321! The digits count up to the number "
            "of ones in the factor, then count symmetrically back down to 1. They form a numerical palindrome, reading identically "
            "forwards and backwards! Next, examine the famous pattern multiplying sequences by 9 and adding consecutive numbers: "
            "1 times 9 plus 2 equals 11; 12 times 9 plus 3 equals 111; 123 times 9 plus 4 equals 1,111; and 1,234 times 9 plus 5 "
            "equals 11,111! Finally, on a 100-number grid, what adjacent pair produces the highest product? The pair with the highest "
            "magnitudes: 99 times 100 equals 9,900. When comparing pairs that have the exact same sum, the product is always greatest "
            "when the two numbers are as close to each other as possible. Pattern recognition lets us predict products without calculation."
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    Discover the fascinating mathematical architecture behind palindromic repunits, digit staircases, and number grid boundaries:
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs font-mono">
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-indigo-500/30">
                        <h4 class="font-bold text-indigo-400 mb-2 font-sans flex items-center gap-1.5">
                            <span>🏔️</span> Repunit Palindrome Mountains
                        </h4>
                        <div class="space-y-1 bg-slate-900/60 p-3 rounded-lg text-slate-200">
                            <p>1 × 1 = <span class="text-emerald-400 font-bold">1</span></p>
                            <p>11 × 11 = <span class="text-emerald-400 font-bold">121</span></p>
                            <p>111 × 111 = <span class="text-emerald-400 font-bold">12321</span></p>
                            <p>1111 × 1111 = <span class="text-emerald-400 font-bold">1234321</span></p>
                            <p>11111 × 11111 = <span class="text-emerald-400 font-bold">123454321</span></p>
                        </div>
                        <p class="text-[11px] text-slate-400 font-sans mt-2">The peak digit equals the number of ones in each factor!</p>
                    </div>
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-violet-500/30">
                        <h4 class="font-bold text-violet-400 mb-2 font-sans flex items-center gap-1.5">
                            <span>🪜</span> The 9s Staircase of Ones
                        </h4>
                        <div class="space-y-1 bg-slate-900/60 p-3 rounded-lg text-slate-200">
                            <p>1 × 9 + 2 = <span class="text-amber-400 font-bold">11</span></p>
                            <p>12 × 9 + 3 = <span class="text-amber-400 font-bold">111</span></p>
                            <p>123 × 9 + 4 = <span class="text-amber-400 font-bold">1111</span></p>
                            <p>1234 × 9 + 5 = <span class="text-amber-400 font-bold">11111</span></p>
                            <p>12345 × 9 + 6 = <span class="text-amber-400 font-bold">111111</span></p>
                        </div>
                        <p class="text-[11px] text-slate-400 font-sans mt-2">Each step adds one more 1 to the repunit answer!</p>
                    </div>
                </div>
                <div class="p-3 bg-indigo-950/40 border border-indigo-500/30 rounded-lg text-xs text-indigo-200">
                    <strong>Grid Product Law:</strong> Between two numbers with constant sum <em>S</em> (e.g. 10 + 10 = 20 vs 1 + 19 = 20), product is maximized when numbers are equal: <em>10 × 10 = 100 > 1 × 19 = 19</em>.
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_15",
        "checkpoints": [
            {
                "question": "Following the repunit pattern, what is the value of 1,111,111 × 1,111,111?",
                "options": [
                    "1234567654321",
                    "123456787654321",
                    "12345654321",
                    "1111111111111"
                ],
                "correct": 0,
                "explanation": "Since there are 7 ones, the product peaks at 7: 1234567654321."
            },
            {
                "question": "What is 123,456 × 9 + 7?",
                "options": ["1,111,111", "1,111,110", "111,111", "11,111,111"],
                "correct": 0,
                "explanation": "Following the 9s staircase pattern, 123,456 × 9 + 7 produces seven 1s: 1,111,111."
            }
        ]
    },
    {
        "id": 16,
        "title": "Algebraic Products",
        "tag": "Let Us Solve Final Review • Algebraic Relationships & Adjacent Products",
        "lecture": (
            "In our final synthesis of The Dairy Farm, we bridge arithmetic and algebra! Suppose you are told that 67 times 67 "
            "equals 4,489. Can you compute 67 times 68 in less than five seconds without writing down a long multiplication? Yes! "
            "Observe that 68 is simply 67 plus 1. Therefore, 67 times 68 equals 67 times 67 plus 67! We simply add 67 to 4,489: "
            "4,489 plus 67 equals 4,556! What if you needed 67 times 66? Subtract 67 from 4,489 to get 4,422! This algebraic rule "
            "states that n times n plus 1 equals n squared plus n. Next, consider the financial ledger of the dairy village's Women's "
            "Football Tournament. 16 teams participate with 18 players each, giving 16 times 18 equals 288 registered players. The "
            "organizers sold 450 spectator tickets at 65 rupees each. 450 times 65: 450 times 60 is 27,000, and 450 times 5 is "
            "2,250, totaling 29,250 rupees in ticket revenue. After paying 12,000 rupees for stadium lights and field preparation, "
            "the net surplus is 17,250 rupees! Multiplication equips us to model complex events, manage enterprise finances, and see "
            "the beauty of algebra in everyday life."
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    Algebraic relationships connect consecutive products, while multi-step budgeting orchestrates community events:
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-teal-500/30">
                        <h4 class="font-bold text-teal-400 mb-2 flex items-center gap-1.5 font-mono">
                            <span>⚡</span> Adjacent Square Product Rule
                        </h4>
                        <p class="text-slate-300 mb-2">Given that <span class="font-mono text-amber-300 font-bold">67 × 67 = 4,489</span>:</p>
                        <div class="space-y-2 font-mono bg-slate-900/60 p-3 rounded-lg text-slate-200">
                            <p>• 67 × 68 = 67 × (67 + 1)</p>
                            <p>&nbsp; = (67 × 67) + 67</p>
                            <p>&nbsp; = 4,489 + 67 = <span class="text-emerald-400 font-bold">4,556</span></p>
                            <div class="border-t border-slate-700 pt-1"></div>
                            <p>• 67 × 66 = 67 × (67 - 1)</p>
                            <p>&nbsp; = 4,489 - 67 = <span class="text-cyan-400 font-bold">4,422</span></p>
                        </div>
                    </div>
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-indigo-500/30">
                        <h4 class="font-bold text-indigo-400 mb-2 flex items-center gap-1.5">
                            <span>⚽</span> Women's Football Tournament Ledger
                        </h4>
                        <div class="space-y-1.5 text-slate-300">
                            <p>• <strong>Athletes:</strong> 16 teams × 18 players = <strong>288 players</strong></p>
                            <p>• <strong>Ticket Revenue:</strong> 450 tickets × ₹ 65/ticket</p>
                            <p class="font-mono pl-3 text-slate-400">= (450 × 60) + (450 × 5) = ₹ 27,000 + ₹ 2,250 = ₹ 29,250</p>
                            <p>• <strong>Expenses:</strong> Ground lighting & logistics = <strong>₹ 12,000</strong></p>
                            <p class="font-mono text-emerald-300 font-bold pt-1 border-t border-slate-700">Net Surplus = ₹ 29,250 - ₹ 12,000 = ₹ 17,250</p>
                        </div>
                    </div>
                </div>
                <div class="p-3 bg-emerald-950/40 border border-emerald-500/30 rounded-lg text-xs text-emerald-200">
                    <strong>Algebraic Principle:</strong> <em>n × (n + 1) = n² + n</em> and <em>n × (n - 1) = n² - n</em>. Understanding algebraic structure eliminates repetitive computation!
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_16",
        "checkpoints": [
            {
                "question": "If 45 × 45 = 2,025, what is 45 × 46?",
                "options": [
                    "2,025 + 45 = 2,070",
                    "2,025 + 46 = 2,071",
                    "2,025 + 1 = 2,026",
                    "2,025 × 2 = 4,050"
                ],
                "correct": 0,
                "explanation": "45 × 46 = 45 × (45 + 1) = (45 × 45) + 45 = 2,025 + 45 = 2,070."
            },
            {
                "question": "If 50 × 50 = 2,500, what is 50 × 49?",
                "options": [
                    "2,500 - 50 = 2,450",
                    "2,500 - 49 = 2,451",
                    "2,500 - 1 = 2,499",
                    "2,400"
                ],
                "correct": 0,
                "explanation": "50 × 49 = 50 × (50 - 1) = (50 × 50) - 50 = 2,500 - 50 = 2,450."
            }
        ]
    }
]

