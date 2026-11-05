# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 6: The Dairy Farm - Part 1 (Slides 1 to 8)
NEP 2020 / Joyful Mathematics
"""

SLIDES_PART1 = [
    {
        "id": 1,
        "title": "Grouping Puzzles",
        "tag": "Let Us Think • Number Puzzles & Array Grouping",
        "lecture": (
            "Welcome to our mathematics laboratory on The Dairy Farm! On a vibrant dairy farm, thousands of fresh buttermilk "
            "pouches, butter bricks, and milk cans are packed and dispatched every single morning. To handle this efficiently, "
            "dairy workers arrange items into neat rectangular crates and arrays. Mathematics begins with recognizing hidden "
            "patterns. Consider a logic puzzle where geometric shapes stand for secret numbers. If Circle multiplied by Circle "
            "equals 36, what must Circle be? Since 6 times 6 is 36, Circle must be 6. If Circle times Triangle equals 48, then "
            "6 times Triangle is 48, revealing Triangle is 8! Next, look at buttermilk pouches packed in flat trays. If 4 trays "
            "each have 6 rows of 5 pouches, we compute 6 times 5 equals 30 pouches per tray, and 4 times 30 gives 120 pouches in "
            "total. We also explore digit placement challenges: choosing digits to make a product as close to 100 as possible. For "
            "example, 32 multiplied by 3 gives 96, which is only 4 away from 100! Multiplying arrays and cracking shape puzzles "
            "trains our mind to see multiplication as structured grouping."
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    At a dairy farm, goods are packed into orderly rows and columns. Multiplication provides the quickest tool to count structured arrays and solve algebraic shape puzzles.
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-emerald-500/30">
                        <h4 class="font-bold text-emerald-400 mb-2 flex items-center gap-2">
                            <span>🧩</span> Shape-Based Algebraic Puzzles
                        </h4>
                        <ul class="text-xs space-y-2 text-slate-300">
                            <li>• If <strong>◯ × ◯ = 36</strong>, then <strong>◯ = 6</strong> (since 6 × 6 = 36).</li>
                            <li>• If <strong>◯ × △ = 48</strong>, then <strong>6 × △ = 48</strong>, so <strong>△ = 8</strong>.</li>
                            <li>• If <strong>△ × ▢ = 80</strong>, then <strong>8 × ▢ = 80</strong>, so <strong>▢ = 10</strong>.</li>
                            <li>• Finding unknown values using inverse division: <strong>△ = 48 ÷ 6 = 8</strong>.</li>
                        </ul>
                    </div>
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-cyan-500/30">
                        <h4 class="font-bold text-cyan-400 mb-2 flex items-center gap-2">
                            <span>📦</span> Buttermilk Pouch Arrays
                        </h4>
                        <ul class="text-xs space-y-2 text-slate-300">
                            <li>• <strong>1 Tray</strong>: 6 rows of 5 pouches = <strong>6 × 5 = 30 pouches</strong>.</li>
                            <li>• <strong>4 Trays</strong>: 4 × 30 = <strong>120 total pouches</strong>.</li>
                            <li>• <strong>Targeting 100</strong>: With digits 1, 2, 3, 4:
                                <ul class="pl-4 mt-1 space-y-1">
                                    <li>- 24 × 4 = 96 (difference of 4 from 100)</li>
                                    <li>- 32 × 3 = 96 (difference of 4 from 100)</li>
                                    <li>- 21 × 5 = 105 (difference of 5 from 100)</li>
                                </ul>
                            </li>
                        </ul>
                    </div>
                </div>
                <div class="p-3 bg-amber-950/40 border border-amber-500/30 rounded-lg text-xs text-amber-200">
                    <strong>Key Insight:</strong> Multiplication represents repeated addition of equal groups: <em>Total = (Number of Groups) × (Items per Group)</em>.
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_1",
        "checkpoints": [
            {
                "question": "If ▢ × ▢ = 49 and ▢ × ◯ = 35, what is the value of ◯?",
                "options": ["5", "7", "6", "8"],
                "correct": 0,
                "explanation": "Since ▢ × ▢ = 49, ▢ must be 7 (7 × 7 = 49). Substituting ▢ = 7 into 7 × ◯ = 35 gives ◯ = 35 ÷ 7 = 5."
            },
            {
                "question": "A dairy worker packs 5 crates, each holding 8 rows with 6 bottles of milk. How many bottles are packed in total?",
                "options": ["240 bottles", "48 bottles", "190 bottles", "300 bottles"],
                "correct": 0,
                "explanation": "Each crate holds 8 × 6 = 48 bottles. For 5 crates, total bottles = 5 × 48 = 240 bottles."
            }
        ]
    },
    {
        "id": 2,
        "title": "Multiplication Order",
        "tag": "Commutative Property • Zero & Identity Rules",
        "lecture": (
            "Let us discover a fundamental rule of arithmetic: the order of numbers in multiplication does not change the result! "
            "Imagine a dairy farm where milk packets are organized. Suppose we have 3 boxes, and each box contains 2 packets of "
            "fresh milk. Total packets equal 3 times 2, which is 6. Now turn the crate sideways: we see 2 rows of 3 packets each! "
            "That is 2 times 3, which is also 6 packets. Whether we calculate 3 times 2 or 2 times 3, the total remains exactly 6! "
            "This universal truth is known as the Commutative Property of Multiplication. For any numbers, a times b equals b times a. "
            "This property is immensely helpful when multiplying three numbers: 4 times 5 times 7 can be grouped as 4 times 5 equals "
            "20, and 20 times 7 equals 140. Or we can multiply 5 times 7 first to get 35, and 4 times 35 also equals 140! Finally, "
            "consider multiplying by zero. If a dairy has 5 crates but each crate is empty with 0 bottles, there are 5 times 0 equals "
            "0 bottles. Any number multiplied by zero always yields zero!"
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    The arrangement of items in rows and columns proves that the order of factors does not alter the product.
                </p>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
                    <div class="bg-slate-800/80 p-3.5 rounded-xl border border-indigo-500/30">
                        <h4 class="font-bold text-indigo-400 mb-2 flex items-center gap-1.5">
                            <span>🔄</span> Commutative Rule
                        </h4>
                        <div class="text-xs space-y-1.5 text-slate-300">
                            <p class="font-semibold text-emerald-300 text-sm">a × b = b × a</p>
                            <p>• 3 crates of 2 bottles = 3 × 2 = <strong>6</strong></p>
                            <p>• 2 crates of 3 bottles = 2 × 3 = <strong>6</strong></p>
                            <p>• 15 × 8 = 8 × 15 = <strong>120</strong></p>
                        </div>
                    </div>
                    <div class="bg-slate-800/80 p-3.5 rounded-xl border border-violet-500/30">
                        <h4 class="font-bold text-violet-400 mb-2 flex items-center gap-1.5">
                            <span>🔗</span> Associative Rule
                        </h4>
                        <div class="text-xs space-y-1.5 text-slate-300">
                            <p class="font-semibold text-purple-300 text-sm">(a × b) × c = a × (b × c)</p>
                            <p>• (4 × 5) × 7 = 20 × 7 = <strong>140</strong></p>
                            <p>• 4 × (5 × 7) = 4 × 35 = <strong>140</strong></p>
                            <p>• Choose groupings that yield friendly tens!</p>
                        </div>
                    </div>
                    <div class="bg-slate-800/80 p-3.5 rounded-xl border border-rose-500/30">
                        <h4 class="font-bold text-rose-400 mb-2 flex items-center gap-1.5">
                            <span>⭕</span> Zero & Identity Rules
                        </h4>
                        <div class="text-xs space-y-1.5 text-slate-300">
                            <p class="font-semibold text-amber-300 text-sm">a × 0 = 0 &nbsp;|&nbsp; a × 1 = a</p>
                            <p>• 8 crates with 0 cans = 8 × 0 = <strong>0</strong></p>
                            <p>• 0 crates of 15 cans = 0 × 15 = <strong>0</strong></p>
                            <p>• 25 × 1 = <strong>25</strong> (Identity Element)</p>
                        </div>
                    </div>
                </div>
                <div class="p-3 bg-emerald-950/40 border border-emerald-500/30 rounded-lg text-xs text-emerald-200">
                    <strong>Mental Math Strategy:</strong> When multiplying <strong>25 × 17 × 4</strong>, rearrange using the commutative property: <em>(25 × 4) × 17 = 100 × 17 = 1,700</em>.
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_2",
        "checkpoints": [
            {
                "question": "Which mental rearrangement makes calculating 8 × 19 × 5 the fastest?",
                "options": [
                    "(8 × 5) × 19 = 40 × 19",
                    "(8 × 19) × 5 = 152 × 5",
                    "8 × (19 + 5) = 8 × 24",
                    "(19 × 8) ÷ 5"
                ],
                "correct": 0,
                "explanation": "Multiplying 8 × 5 gives 40 (a friendly ten). Then 40 × 19 = 40 × (20 - 1) = 800 - 40 = 760, which is simple to compute mentally!"
            },
            {
                "question": "What is the value of 47 × 0 × 85?",
                "options": ["0", "47", "85", "3,995"],
                "correct": 0,
                "explanation": "By the Zero Property of Multiplication, any product containing 0 as a factor equals 0."
            }
        ]
    },
    {
        "id": 3,
        "title": "Place Value Shifts",
        "tag": "Multiplying by 10, 100, and 1,000 • Zero Patterns",
        "lecture": (
            "When a dairy farm expands deliveries from local families to city supermarkets, orders grow tenfold, a hundredfold, and "
            "a thousandfold! How does multiplying by powers of ten affect a number? In our base ten place value system, every step to "
            "the left is worth ten times more. When we multiply 25 cans of milk by 10, every digit shifts one place to the left: 2 tens "
            "become 2 hundreds, and 5 ones become 5 tens. An empty place appears in the units column, filled by a zero, giving 250! "
            "When we multiply 25 by 100, digits shift two places left, appending two zeros to give 2,500. Multiplying by 1,000 shifts "
            "digits three places left, appending three zeros to give 25,000! What if we multiply numbers like 60 by 400? We first "
            "multiply the non-zero leading digits: 6 times 4 equals 24. Then count the total zeros: one zero in 60 plus two zeros "
            "in 400 equals three zeros in all. Attaching three zeros gives 24,000! Tracking place value shifts makes multiplying by "
            "multiples of ten effortless."
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    Multiplying by 10, 100, or 1,000 shifts every digit into a higher place-value column and places zero placeholders in the vacated positions.
                </p>
                <div class="overflow-x-auto">
                    <table class="w-full text-xs text-left bg-slate-800/80 rounded-xl border border-slate-700">
                        <thead class="bg-slate-700/60 text-emerald-300">
                            <tr>
                                <th class="p-2.5">Original</th>
                                <th class="p-2.5">Multiplier</th>
                                <th class="p-2.5">Place Value Shift</th>
                                <th class="p-2.5">Product</th>
                                <th class="p-2.5">Rule</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-700/60 text-slate-200">
                            <tr>
                                <td class="p-2 font-mono font-bold">34</td>
                                <td class="p-2">× 10</td>
                                <td class="p-2">1 place left (O → T, T → H)</td>
                                <td class="p-2 font-mono font-bold text-amber-300">340</td>
                                <td class="p-2">Append one 0</td>
                            </tr>
                            <tr>
                                <td class="p-2 font-mono font-bold">34</td>
                                <td class="p-2">× 100</td>
                                <td class="p-2">2 places left (O → H, T → Th)</td>
                                <td class="p-2 font-mono font-bold text-amber-300">3,400</td>
                                <td class="p-2">Append two 0s</td>
                            </tr>
                            <tr>
                                <td class="p-2 font-mono font-bold">34</td>
                                <td class="p-2">× 1,000</td>
                                <td class="p-2">3 places left (O → Th, T → TTh)</td>
                                <td class="p-2 font-mono font-bold text-amber-300">34,000</td>
                                <td class="p-2">Append three 0s</td>
                            </tr>
                            <tr>
                                <td class="p-2 font-mono font-bold">70 × 800</td>
                                <td class="p-2">Multiples of 10 & 100</td>
                                <td class="p-2">(7 × 8) × (10 × 100)</td>
                                <td class="p-2 font-mono font-bold text-cyan-300">56,000</td>
                                <td class="p-2">7 × 8 = 56 + three 0s</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="p-3 bg-blue-950/40 border border-blue-500/30 rounded-lg text-xs text-blue-200">
                    <strong>Trailing Zero Rule:</strong> When multiplying numbers with trailing zeros, multiply non-zero digits first, then count and append the sum of all trailing zeros.
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_3",
        "checkpoints": [
            {
                "question": "What is the product of 500 × 60?",
                "options": ["30,000", "3,000", "300,000", "300"],
                "correct": 0,
                "explanation": "Multiply non-zero digits: 5 × 6 = 30. Then count zeros: 500 has two zeros, 60 has one zero (total 3 zeros). 30 with three zeros appended is 30,000."
            },
            {
                "question": "A dairy cooperative sells 42 cans of ghee every day for 100 days. How many cans are sold in total?",
                "options": ["4,200 cans", "420 cans", "42,000 cans", "8,400 cans"],
                "correct": 0,
                "explanation": "42 × 100 shifts the digits 4 and 2 two places to the left, appending two zeros: 4,200 cans."
            }
        ]
    },
    {
        "id": 4,
        "title": "Mental Strategies",
        "tag": "Alternative Strategies • Student-Devised Methods",
        "lecture": (
            "Mathematics is celebrated for offering multiple pathways to the exact same truth! Consider multiplying 18 by 5. In a "
            "dairy classroom, different students devised clever mental strategies. Student A uses the Halving and Doubling method: "
            "halve 18 to get 9, and double 5 to get 10; then 9 times 10 is effortlessly 90! Student B uses the Partitioning or "
            "Distributive method: split 18 into 10 plus 8; 10 times 5 is 50, and 8 times 5 is 40; adding 50 plus 40 gives 90! "
            "Student C uses the Compensation method: round 18 up to the friendly ten 20; 20 times 5 is 100; but since we took 2 "
            "extra groups of 5, we subtract 2 times 5, which is 10, leaving 100 minus 10 equals 90! Student D calculates 18 times "
            "10 equals 180, and since 5 is half of 10, divides 180 by 2 to get 90. Notice how every method bypasses pencil-and-paper "
            "carrying. When we understand number properties, mental multiplication becomes fast, creative, and joyful!"
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    Compare the four brilliant student strategies to calculate <strong>18 × 5</strong> mentally:
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
                    <div class="p-3 bg-slate-800/80 rounded-xl border border-teal-500/30">
                        <span class="font-bold text-teal-400 block mb-1 text-sm">Method 1: Halving & Doubling</span>
                        <p class="text-slate-300 mb-1.5">• Halve the even factor: 18 ÷ 2 = <strong>9</strong></p>
                        <p class="text-slate-300 mb-1.5">• Double the other factor: 5 × 2 = <strong>10</strong></p>
                        <p class="font-mono text-emerald-300 font-bold">• 9 × 10 = 90</p>
                    </div>
                    <div class="p-3 bg-slate-800/80 rounded-xl border border-cyan-500/30">
                        <span class="font-bold text-cyan-400 block mb-1 text-sm">Method 2: Partitioning (Distributive)</span>
                        <p class="text-slate-300 mb-1.5">• Split 18 into tens and ones: <strong>(10 + 8)</strong></p>
                        <p class="text-slate-300 mb-1.5">• Multiply each part: (10 × 5) + (8 × 5)</p>
                        <p class="font-mono text-emerald-300 font-bold">• 50 + 40 = 90</p>
                    </div>
                    <div class="p-3 bg-slate-800/80 rounded-xl border border-amber-500/30">
                        <span class="font-bold text-amber-400 block mb-1 text-sm">Method 3: Compensation</span>
                        <p class="text-slate-300 mb-1.5">• Round 18 to friendly 20: <strong>(20 × 5)</strong> = 100</p>
                        <p class="text-slate-300 mb-1.5">• Subtract 2 extra groups of 5: 2 × 5 = <strong>10</strong></p>
                        <p class="font-mono text-emerald-300 font-bold">• 100 - 10 = 90</p>
                    </div>
                    <div class="p-3 bg-slate-800/80 rounded-xl border border-purple-500/30">
                        <span class="font-bold text-purple-400 block mb-1 text-sm">Method 4: Multiply by 10 & Halve</span>
                        <p class="text-slate-300 mb-1.5">• Since 5 = 10 ÷ 2, multiply by 10 first: 18 × 10 = <strong>180</strong></p>
                        <p class="text-slate-300 mb-1.5">• Take half of the result: 180 ÷ 2</p>
                        <p class="font-mono text-emerald-300 font-bold">• 180 ÷ 2 = 90</p>
                    </div>
                </div>
                <div class="p-3 bg-slate-800/80 border border-slate-600 rounded-lg text-xs text-slate-300">
                    <strong>Rule of Flexibility:</strong> Choose the strategy that best exploits the special structure of the numbers involved!
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_4",
        "checkpoints": [
            {
                "question": "Using partitioning, what is the best way to compute 24 × 6 mentally?",
                "options": [
                    "(20 × 6) + (4 × 6) = 120 + 24 = 144",
                    "(24 × 10) - (24 × 6) = 240 - 144",
                    "(24 ÷ 6) × (6 ÷ 6) = 4",
                    "(20 + 4) × (20 + 6)"
                ],
                "correct": 0,
                "explanation": "Partitioning 24 into 20 + 4 allows mental multiplication: 20 × 6 = 120 and 4 × 6 = 24; 120 + 24 = 144."
            },
            {
                "question": "To calculate 36 × 5 by multiplying by 10 and halving, what are the steps?",
                "options": [
                    "36 × 10 = 360, then 360 ÷ 2 = 180",
                    "36 ÷ 10 = 3.6, then 3.6 × 2 = 7.2",
                    "36 × 2 = 72, then 72 × 10 = 720",
                    "36 × 5 = 30 × 5 = 150"
                ],
                "correct": 0,
                "explanation": "Since 5 is half of 10, compute 36 × 10 = 360, then divide by 2: 360 ÷ 2 = 180."
            }
        ]
    },
    {
        "id": 5,
        "title": "Doubling and Halving",
        "tag": "Area Models • Simplifying Multiplications with 5, 25, and 50",
        "lecture": (
            "One of the most elegant geometric techniques in mathematics is the Doubling and Halving strategy. Picture a large "
            "rectangular pasture on the dairy farm that is 16 metres wide and 25 metres long. The total area is 16 times 25. "
            "Now imagine slicing the pasture right down the middle into two 8-metre strips. Take one 8-metre strip and paste it to "
            "the far end of the other strip! The width is now halved to 8 metres, but the length is doubled to 50 metres. The total "
            "area has not changed at all! We can halve and double again: halve 8 to 4, and double 50 to 100 metres! Now look at the "
            "calculation: 4 times 100 equals 400 square metres. Instead of struggling with 16 times 25, we simply multiplied 4 by 100! "
            "This strategy is especially powerful when multiplying by numbers ending in 5, 25, or 50. For 28 times 50: halve 28 to "
            "14, double 50 to 100; 14 times 100 equals 1,400! In general, dividing one factor by 2 while multiplying the other by 2 "
            "keeps the total product perfectly preserved."
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    Halving one factor while doubling the other leaves the area (product) completely invariant:
                    <span class="font-mono text-emerald-300 font-bold">(a ÷ 2) × (b × 2) = a × b</span>.
                </p>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
                    <div class="bg-slate-800/80 p-3.5 rounded-xl border border-emerald-500/30">
                        <h4 class="font-bold text-emerald-400 mb-1.5 text-sm">Multiplying by 5</h4>
                        <p class="text-slate-300 mb-1">Halve even factor, double 5 to <strong>10</strong>:</p>
                        <p class="font-mono text-slate-200">• 48 × 5</p>
                        <p class="font-mono text-slate-200">• = (48 ÷ 2) × (5 × 2)</p>
                        <p class="font-mono text-emerald-300 font-bold">• = 24 × 10 = 240</p>
                    </div>
                    <div class="bg-slate-800/80 p-3.5 rounded-xl border border-cyan-500/30">
                        <h4 class="font-bold text-cyan-400 mb-1.5 text-sm">Multiplying by 25</h4>
                        <p class="text-slate-300 mb-1">Halve twice (÷ 4), double 25 twice to <strong>100</strong>:</p>
                        <p class="font-mono text-slate-200">• 36 × 25</p>
                        <p class="font-mono text-slate-200">• = (36 ÷ 4) × (25 × 4)</p>
                        <p class="font-mono text-cyan-300 font-bold">• = 9 × 100 = 900</p>
                    </div>
                    <div class="bg-slate-800/80 p-3.5 rounded-xl border border-amber-500/30">
                        <h4 class="font-bold text-amber-400 mb-1.5 text-sm">Multiplying by 50</h4>
                        <p class="text-slate-300 mb-1">Halve even factor, double 50 to <strong>100</strong>:</p>
                        <p class="font-mono text-slate-200">• 46 × 50</p>
                        <p class="font-mono text-slate-200">• = (46 ÷ 2) × (50 × 2)</p>
                        <p class="font-mono text-amber-300 font-bold">• = 23 × 100 = 2,300</p>
                    </div>
                </div>
                <div class="p-3 bg-violet-950/40 border border-violet-500/30 rounded-lg text-xs text-violet-200">
                    <strong>Geometric Principle:</strong> Cutting a shape and rearranging its pieces preserves its total area. Slicing height in half and doubling width creates an identical area with friendly multiples of 10 or 100!
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_5",
        "checkpoints": [
            {
                "question": "Using the doubling and halving method, what is 24 × 25?",
                "options": [
                    "6 × 100 = 600",
                    "12 × 50 = 700",
                    "48 × 12.5 = 650",
                    "24 × 100 = 2,400"
                ],
                "correct": 0,
                "explanation": "Halving 24 twice gives 24 ÷ 4 = 6. Doubling 25 twice gives 25 × 4 = 100. Thus 6 × 100 = 600."
            },
            {
                "question": "Calculate 64 × 50 using doubling and halving:",
                "options": ["3,200", "3,000", "3,400", "2,800"],
                "correct": 0,
                "explanation": "Halve 64 to 32, double 50 to 100. Then 32 × 100 = 3,200."
            }
        ]
    },
    {
        "id": 6,
        "title": "Nearest Multiple",
        "tag": "Compensation Strategy • Adjusting Over-Counting & Under-Counting",
        "lecture": (
            "What if a factor is not a round multiple of ten, but sits just one or two units away? For example, consider multiplying "
            "4 by 19. A dairy van delivers 4 cartons, with 19 bottles of toned milk in each carton. 19 is difficult to multiply directly "
            "in your head, but 20 is remarkably easy! Imagine each carton had 20 bottles. Then 4 times 20 equals 80 bottles. But wait! "
            "We added 1 extra bottle per carton, so across 4 cartons we over-counted by 4 times 1, which is 4 bottles. To compensate, "
            "we subtract that extra 4 from 80: 80 minus 4 equals 76 bottles! This is the Nearest Multiple Compensation Strategy. "
            "Let us test it on 6 times 29: round 29 to 30; 6 times 30 is 180; subtract 6 times 1, leaving 180 minus 6 equals 174! "
            "What if a number is just above a multiple of ten, such as 5 times 42? Round down to 40: 5 times 40 is 200; then add "
            "the extra 5 times 2, which is 10, giving 200 plus 10 equals 210! By rounding to the nearest ten and adjusting the "
            "difference, tricky numbers become swift mental calculations."
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    The compensation strategy rounds a factor to the nearest friendly ten, multiplies, and compensates for over- or under-counting.
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-rose-500/30">
                        <h4 class="font-bold text-rose-400 mb-2 flex items-center gap-2">
                            <span>🔻</span> Over-Counting Adjustment (Subtract)
                        </h4>
                        <p class="text-slate-300 mb-2">When a factor ends in 8 or 9, round UP to the nearest ten and subtract the excess:</p>
                        <div class="space-y-2 font-mono text-slate-200 bg-slate-900/60 p-2.5 rounded-lg">
                            <p><strong>4 × 19:</strong> 4 × (20 - 1) = (4 × 20) - (4 × 1) = 80 - 4 = <span class="text-emerald-400 font-bold">76</span></p>
                            <p><strong>7 × 39:</strong> 7 × (40 - 1) = (7 × 40) - (7 × 1) = 280 - 7 = <span class="text-emerald-400 font-bold">273</span></p>
                            <p><strong>6 × 48:</strong> 6 × (50 - 2) = (6 × 50) - (6 × 2) = 300 - 12 = <span class="text-emerald-400 font-bold">288</span></p>
                        </div>
                    </div>
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-teal-500/30">
                        <h4 class="font-bold text-teal-400 mb-2 flex items-center gap-2">
                            <span>🔺</span> Under-Counting Adjustment (Add)
                        </h4>
                        <p class="text-slate-300 mb-2">When a factor ends in 1 or 2, round DOWN to the nearest ten and add the remainder:</p>
                        <div class="space-y-2 font-mono text-slate-200 bg-slate-900/60 p-2.5 rounded-lg">
                            <p><strong>5 × 42:</strong> 5 × (40 + 2) = (5 × 40) + (5 × 2) = 200 + 10 = <span class="text-teal-400 font-bold">210</span></p>
                            <p><strong>8 × 31:</strong> 8 × (30 + 1) = (8 × 30) + (8 × 1) = 240 + 8 = <span class="text-teal-400 font-bold">248</span></p>
                            <p><strong>9 × 62:</strong> 9 × (60 + 2) = (9 × 60) + (9 × 2) = 540 + 18 = <span class="text-teal-400 font-bold">558</span></p>
                        </div>
                    </div>
                </div>
                <div class="p-3 bg-amber-950/40 border border-amber-500/30 rounded-lg text-xs text-amber-200">
                    <strong>General Algebraic Form:</strong> <em>k × (N ± d) = (k × N) ± (k × d)</em> (The Distributive Law over Addition and Subtraction).
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_6",
        "checkpoints": [
            {
                "question": "What is 8 × 49 using the nearest multiple compensation strategy?",
                "options": [
                    "(8 × 50) - 8 = 400 - 8 = 392",
                    "(8 × 40) + 9 = 320 + 9 = 329",
                    "(8 × 50) + 8 = 408",
                    "(8 × 45) + 4 = 364"
                ],
                "correct": 0,
                "explanation": "49 is 50 - 1. So 8 × 49 = 8 × (50 - 1) = (8 × 50) - (8 × 1) = 400 - 8 = 392."
            },
            {
                "question": "Calculate 6 × 52 using the under-counting adjustment strategy:",
                "options": ["312", "300", "320", "292"],
                "correct": 0,
                "explanation": "6 × 52 = 6 × (50 + 2) = (6 × 50) + (6 × 2) = 300 + 12 = 312."
            }
        ]
    },
    {
        "id": 7,
        "title": "Application Problems",
        "tag": "Let Us Solve • Word Problems in Real-World Contexts",
        "lecture": (
            "Multiplication is the engine of daily commerce, agriculture, and construction. Let us visit the village dairy and community "
            "centre to solve real-world problems. First, in the village auditorium where dairy cooperative meetings take place, there "
            "are 24 rows of chairs, and each row has 18 chairs. How many people can attend? Using partitioning: 24 times 18 equals "
            "24 times 20 minus 24 times 2; 480 minus 48 equals 432 seats! Next, consider the dairy farm's prize herd of 14 Sahiwal cows. "
            "If each cow yields an average of 12 litres of milk every day, how much milk is collected daily? 14 times 12: 14 times 10 is "
            "140, plus 14 times 2 is 28, giving 168 litres every day! In a week of 7 days, the herd produces 7 times 168: 7 times 100 "
            "is 700, 7 times 60 is 420, and 7 times 8 is 56; summing these gives 1,176 litres! Finally, the cooperative tailors uniform "
            "kurtas for its 8 dairy staff. Each kurta requires 2 metres 25 centimetres of cloth. 8 times 2 metres is 16 metres, and "
            "8 times 25 centimetres is 200 centimetres, which is exactly 2 metres. Total cloth required is 18 metres!"
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    Step-by-step mathematical reasoning transforms word descriptions into clean multiplicative models:
                </p>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
                    <div class="bg-slate-800/80 p-3.5 rounded-xl border border-indigo-500/30">
                        <h4 class="font-bold text-indigo-400 mb-1.5 flex items-center gap-1.5">
                            <span>🪑</span> Auditorium Seating
                        </h4>
                        <p class="text-slate-300">• 24 rows with 18 seats each</p>
                        <p class="text-slate-300 font-mono">• 24 × 18 = 24 × (20 - 2)</p>
                        <p class="text-slate-300 font-mono">• = 480 - 48</p>
                        <p class="font-mono text-emerald-300 font-bold text-sm mt-1">• = 432 seats</p>
                    </div>
                    <div class="bg-slate-800/80 p-3.5 rounded-xl border border-cyan-500/30">
                        <h4 class="font-bold text-cyan-400 mb-1.5 flex items-center gap-1.5">
                            <span>🥛</span> Herd Milk Production
                        </h4>
                        <p class="text-slate-300">• 14 cows × 12 L/day</p>
                        <p class="text-slate-300 font-mono">• Daily = 14 × 12 = 168 L</p>
                        <p class="text-slate-300 font-mono">• 7 days = 168 × 7</p>
                        <p class="font-mono text-cyan-300 font-bold text-sm mt-1">• = 1,176 litres/week</p>
                    </div>
                    <div class="bg-slate-800/80 p-3.5 rounded-xl border border-amber-500/30">
                        <h4 class="font-bold text-amber-400 mb-1.5 flex items-center gap-1.5">
                            <span>🧵</span> Uniform Kurta Fabric
                        </h4>
                        <p class="text-slate-300">• 8 kurtas × 2 m 25 cm</p>
                        <p class="text-slate-300 font-mono">• Metres: 8 × 2 m = 16 m</p>
                        <p class="text-slate-300 font-mono">• Centimetres: 8 × 25 cm = 200 cm = 2 m</p>
                        <p class="font-mono text-amber-300 font-bold text-sm mt-1">• Total = 18 metres</p>
                    </div>
                </div>
                <div class="p-3 bg-emerald-950/40 border border-emerald-500/30 rounded-lg text-xs text-emerald-200">
                    <strong>Problem-Solving Heuristic:</strong> Identify the <em>Rate per Unit</em> (e.g., litres per cow, metres per garment) and multiply by the <em>Number of Units</em>.
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_7",
        "checkpoints": [
            {
                "question": "A dairy worker packs 15 boxes of cheese blocks. If each box contains 24 blocks, how many blocks are packed in total?",
                "options": ["360 blocks", "340 blocks", "380 blocks", "300 blocks"],
                "correct": 0,
                "explanation": "15 × 24 = 15 × (20 + 4) = 300 + 60 = 360 blocks."
            },
            {
                "question": "A jogging track around the dairy farm pasture is 450 metres long. If Kabir jogs 8 full laps every morning, what total distance does he cover?",
                "options": ["3,600 metres (3.6 km)", "3,200 metres", "4,000 metres", "3,800 metres"],
                "correct": 0,
                "explanation": "8 × 450 m = 8 × (400 + 50) = 3,200 + 400 = 3,600 m = 3.6 km."
            }
        ]
    },
    {
        "id": 8,
        "title": "Compost Savings",
        "tag": "Waste and Composting • Ecological Arithmetic & Household Savings",
        "lecture": (
            "At the dairy farm, sustainability and mathematics go hand in hand! Cows produce dung, and dairy households generate "
            "organic vegetable peels and kitchen waste. Instead of discarding this waste into landfills, the farm converts it into "
            "nutrient-rich organic compost. Let us examine the numbers. A typical dairy family produces 350 grams of organic kitchen "
            "waste each day. How much waste is generated in a 30-day month? 350 multiplied by 30: 35 times 3 is 105, plus two zeros "
            "gives 10,500 grams, which is 10.5 kilograms! Over a full year of 365 days, Kanti and John calculate the waste generated. "
            "Kanti breaks 365 into 300 plus 60 plus 5 and multiplies each by 350 grams: 350 times 300 is 105,000 grams; 350 times 60 "
            "is 21,000 grams; and 350 times 5 is 1,750 grams. Summing these gives 127,750 grams, which is over 127 kilograms of waste! "
            "When turned into compost, the family saves money. If a 5-kilogram bag of commercial compost costs 120 rupees, producing "
            "25 bags of homemade compost saves 25 times 120 rupees. 25 times 100 is 2,500, and 25 times 20 is 500; total savings "
            "equal 3,000 rupees a year!"
        ),
        "theory_html": """
            <div class="space-y-4 text-slate-200">
                <p class="text-base leading-relaxed">
                    Ecological arithmetic proves how converting organic waste into compost creates environmental health and substantial household financial savings.
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-emerald-500/30">
                        <h4 class="font-bold text-emerald-400 mb-2 flex items-center gap-2">
                            <span>🌱</span> Kitchen Waste Computation
                        </h4>
                        <p class="text-slate-300 mb-1">• Daily household organic waste: <strong>350 g</strong></p>
                        <p class="text-slate-300 mb-1">• In 1 Month (30 days): 350 × 30 = <strong>10,500 g = 10.5 kg</strong></p>
                        <p class="text-slate-300 mb-1">• In 1 Year (365 days) via Kanti's expansion:</p>
                        <div class="pl-3 py-1 font-mono text-slate-200 space-y-0.5 border-l-2 border-emerald-500/40">
                            <p>350 × 300 = 105,000 g</p>
                            <p>350 × 60 = 21,000 g</p>
                            <p>350 × 5 = 1,750 g</p>
                            <p class="text-emerald-300 font-bold">Sum = 127,750 g = 127.75 kg</p>
                        </div>
                    </div>
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-amber-500/30">
                        <h4 class="font-bold text-amber-400 mb-2 flex items-center gap-2">
                            <span>💰</span> Financial Compost Savings
                        </h4>
                        <p class="text-slate-300 mb-1">• Home Compost Produced: <strong>25 bags (5 kg each)</strong></p>
                        <p class="text-slate-300 mb-1">• Market price of 1 commercial bag: <strong>₹ 120</strong></p>
                        <p class="text-slate-300 mb-1">• Annual Savings = 25 × ₹ 120:</p>
                        <div class="pl-3 py-1 font-mono text-slate-200 space-y-0.5 border-l-2 border-amber-500/40">
                            <p>25 × 100 = ₹ 2,500</p>
                            <p>25 × 20 = ₹ 500</p>
                            <p class="text-amber-300 font-bold">Total Annual Savings = ₹ 3,000</p>
                        </div>
                        <p class="mt-2 text-slate-400 italic">Zero waste to landfill + ₹ 3,000 retained in family budget!</p>
                    </div>
                </div>
                <div class="p-3 bg-emerald-950/40 border border-emerald-500/30 rounded-lg text-xs text-emerald-200">
                    <strong>Green Mathematics:</strong> Math enables communities to quantify waste reduction, energy conservation, and ecological savings with exact precision.
                </div>
            </div>
        """,
        "simulator_id": "sim_slide_8",
        "checkpoints": [
            {
                "question": "If a dairy school canteen produces 450 g of food scraps daily, how much waste is generated in 20 days?",
                "options": ["9,000 g (9 kg)", "8,000 g", "900 g", "90,000 g"],
                "correct": 0,
                "explanation": "450 × 20 = 45 × 2 × 100 = 90 × 100 = 9,000 g = 9 kg."
            },
            {
                "question": "A village cooperative makes 40 bags of vermicompost. If each bag saves ₹ 150 compared to chemical fertilizer, what are the total savings?",
                "options": ["₹ 6,000", "₹ 5,500", "₹ 6,500", "₹ 4,000"],
                "correct": 0,
                "explanation": "40 × ₹ 150 = 4 × 15 × 100 = 60 × 100 = ₹ 6,000."
            }
        ]
    }
]

