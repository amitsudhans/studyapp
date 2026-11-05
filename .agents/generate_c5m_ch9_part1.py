# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 9: Coconut Farm
Part 1: Slides 1 to 8
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Division Foundations",
        "tagline": "The Coconut Farm • Inverse Operations & Core Terminology",
        "lecture": (
            "Welcome to the lush green coconut farm! Imagine harvesting fresh green coconuts and arranging them into neat rectangular arrays on the farm grass. If you plant six rows of coconut palms with eight palms in each row, multiplication tells us that six times eight equals forty-eight coconut palms in total. Division is the direct mathematical inverse or reverse operation of multiplication. If a farmer collects forty-eight coconuts and packs them equally into six burlap sacks, how many coconuts go into each sack? We divide forty-eight by six, which gives exactly eight coconuts per sack! In every division problem, three essential terms establish the relationship. The total quantity being divided is called the Dividend, symbolized by the letter N. The number of equal groups we are dividing into is called the Divisor, symbolized by the letter D. The resulting answer, showing the size of each individual share, is called the Quotient, symbolized by the letter Q. When there are no leftovers, the fundamental relationship is expressed as: Dividend equals Divisor multiplied by Quotient. That is, forty-eight equals six multiplied by eight. If you know any multiplication fact, you instantly hold the master key to two related division facts, establishing numerical harmony across arithmetic."
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>🥥</span> The Coconut Farm Array Model
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    Multiplication builds arrays by grouping rows and columns; division partitions the total back into equal rows:
                </p>
                <div class="p-3 rounded-lg bg-slate-900/60 border border-slate-700/60 font-mono text-xs space-y-2">
                    <div class="flex justify-between items-center text-slate-300 border-b border-slate-700 pb-1">
                        <span>Multiplication Fact:</span>
                        <span class="text-emerald-400 font-bold">6 rows × 8 palms = 48 Palms</span>
                    </div>
                    <div class="flex justify-between items-center text-slate-300 border-b border-slate-700 pb-1">
                        <span>Division Fact 1:</span>
                        <span class="text-cyan-300 font-bold">48 ÷ 6 = 8 palms per row</span>
                    </div>
                    <div class="flex justify-between items-center text-slate-300">
                        <span>Division Fact 2:</span>
                        <span class="text-cyan-300 font-bold">48 ÷ 8 = 6 rows of palms</span>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>📐</span> Core Mathematical Terminology
                    </h4>
                    <div class="p-3 rounded-xl bg-gradient-to-r from-amber-500/10 via-cyan-500/10 to-emerald-500/10 border border-amber-500/30 text-center my-2">
                        <div class="text-lg font-black text-amber-300 font-mono">Dividend (N) = Divisor (D) × Quotient (Q)</div>
                        <div class="text-[11px] text-slate-400 mt-1">48 (N) = 6 (D) × 8 (Q)</div>
                    </div>
                    <ul class="text-xs text-slate-300 space-y-1.5 leading-relaxed">
                        <li><strong>• Dividend (N):</strong> The grand total amount being shared or partitioned.</li>
                        <li><strong>• Divisor (D):</strong> The number of groups being created or the size of each part.</li>
                        <li><strong>• Quotient (Q):</strong> The resulting number of items allocated to each equal share.</li>
                    </ul>
                </div>
                <div class="p-2.5 rounded-lg bg-indigo-950/40 border border-indigo-800/40 text-[11px] text-indigo-200 mt-3">
                    💡 <strong>Inverse Principle:</strong> Division undoes multiplication. If A × B = C, then C ÷ A = B and C ÷ B = A!
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c1_1",
                "question": "A coconut farmer harvests 72 coconuts and packs them equally into 9 wooden crates. In the equation 72 ÷ 9 = 8, what is the mathematical term for 72?",
                "options": [
                    "Quotient",
                    "Divisor",
                    "Dividend",
                    "Remainder"
                ],
                "answer": 2,
                "hint": "Identify the total number being divided.",
                "explanation": "In 72 ÷ 9 = 8, the total quantity being divided (72) is called the Dividend. The divisor is 9, and the quotient is 8."
            },
            {
                "id": "c1_2",
                "question": "If 7 × 12 = 84, which of the following is a valid related division statement?",
                "options": [
                    "84 ÷ 12 = 7",
                    "84 ÷ 7 = 14",
                    "12 ÷ 7 = 84",
                    "84 × 7 = 12"
                ],
                "answer": 0,
                "hint": "Divide the product (84) by one of the factors to get the other factor.",
                "explanation": "From 7 × 12 = 84, we can derive two division facts: 84 ÷ 7 = 12, and 84 ÷ 12 = 7."
            }
        ]
    },
    {
        "id": 2,
        "title": "Fact Triangles",
        "tagline": "Let Us Play • Number Fact Triangles & Related Division Statements",
        "lecture": (
            "Mathematical operations are deeply interconnected through family relationships. To visualize and master table fluency, we use an engaging tool called the Number Fact Triangle. Picture a triangle with three circular nodes at its vertices and a square value box at its peak. The two bottom corner nodes contain two factors, while the top peak box contains their product. For example, if the bottom corners contain thirty and thirty, multiplying thirty by thirty yields nine hundred at the top. Because multiplication and division are inverse operations, this single triangle immediately produces two complementary division facts: nine hundred divided by thirty equals thirty, and nine hundred divided by the other thirty also equals thirty. Now consider another triangle with twenty and forty at the bottom. Their product at the peak is eight hundred. From this, we read two division pathways: eight hundred divided by twenty equals forty, and eight hundred divided by forty equals twenty. Fact triangles turn division into a logical game of finding the missing family member. If the peak is six hundred and thirty and one bottom corner is seventy, dividing six hundred and thirty by seventy reveals nine in the missing corner. Connecting operations strengthens mental flexibility."
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>🔺</span> The Fact Triangle Family Structure
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    A single fact triangle generates one multiplication fact and two inverse division facts:
                </p>
                <div class="p-3 rounded-lg bg-slate-900/60 border border-slate-700/60 space-y-2 text-xs font-mono">
                    <div class="text-center p-2 rounded bg-slate-950 border border-slate-800">
                        <span class="text-amber-400 font-bold block text-sm">PEAK = 900</span>
                        <span class="text-slate-400 text-[10px]">Product Box</span>
                    </div>
                    <div class="flex justify-between px-4 text-cyan-300 font-bold">
                        <span>Node A: 30</span>
                        <span>Node B: 30</span>
                    </div>
                    <div class="border-t border-slate-700 pt-2 space-y-1 text-slate-300 text-[11px]">
                        <div>• 30 × 30 = 900 (Multiplication)</div>
                        <div>• 900 ÷ 30 = 30 (Division Fact 1)</div>
                        <div>• 900 ÷ 30 = 30 (Division Fact 2)</div>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>🧩</span> Missing Node Fact Triangle Logic
                    </h4>
                    <p class="text-xs text-slate-300 leading-relaxed mb-3">
                        When one node is missing, choose the correct inverse operation to solve:
                    </p>
                    <div class="space-y-2 text-xs">
                        <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60">
                            <div class="font-bold text-emerald-400">Peak = 630, Bottom Left = 70:</div>
                            <div class="text-slate-300 mt-1 font-mono">Missing Node = 630 ÷ 70 = <strong class="text-cyan-300">9</strong></div>
                        </div>
                        <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60">
                            <div class="font-bold text-amber-400">Peak = 480, Bottom Right = 6:</div>
                            <div class="text-slate-300 mt-1 font-mono">Missing Node = 480 ÷ 6 = <strong class="text-cyan-300">80</strong></div>
                        </div>
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-cyan-950/40 border border-cyan-800/40 text-[11px] text-cyan-200 mt-3">
                    🔍 <strong>Rule of Thumb:</strong> To find the peak, multiply the bottom corners. To find a bottom corner, divide the peak by the known corner!
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c2_1",
                "question": "In a fact triangle, the peak product box displays 720 and the bottom-left node contains 80. What number belongs in the bottom-right node?",
                "options": [
                    "9",
                    "90",
                    "8",
                    "640"
                ],
                "answer": 0,
                "hint": "Divide the top number by the bottom-left node: 720 ÷ 80.",
                "explanation": "720 ÷ 80 = (72 ÷ 8) = 9. So the missing factor is 9."
            },
            {
                "id": "c2_2",
                "question": "Which two division statements can be derived from the multiplication fact 25 × 40 = 1,000?",
                "options": [
                    "1,000 ÷ 25 = 40 and 1,000 ÷ 40 = 25",
                    "1,000 ÷ 20 = 50 and 1,000 ÷ 50 = 20",
                    "1,000 ÷ 4 = 250 and 1,000 ÷ 250 = 4",
                    "1,000 ÷ 10 = 100 and 1,000 ÷ 100 = 10"
                ],
                "answer": 0,
                "hint": "The product 1,000 divided by either factor gives the other factor.",
                "explanation": "From 25 × 40 = 1,000, dividing 1,000 by 25 yields 40, and dividing 1,000 by 40 yields 25."
            }
        ]
    },
    {
        "id": 3,
        "title": "Trailing Zeros",
        "tagline": "Patterns in Division & Place Value • Powers of 10 & Zero Cancellation",
        "lecture": (
            "Dividing numbers that end in trailing zeros reveals one of the most powerful shortcuts in arithmetic. The decimal number system is organized around base ten, where moving one column to the left multiplies a digit by ten, and moving one column to the right divides it by ten. When dividing a number by ten, every digit shifts one place value to the right, which cancels out one trailing zero. For example, six hundred divided by ten equals sixty. Dividing by one hundred shifts every digit two places to the right, canceling two trailing zeros—so six hundred divided by one hundred equals six. When both the dividend and the divisor end in trailing zeros, we can cancel an equal number of zeros from both sides before dividing. Consider seven thousand two hundred divided by ninety. Both numbers share at least one trailing zero. We cancel one zero from ninety and one zero from seven thousand two hundred, turning the problem into seven hundred and twenty divided by nine. We know seventy-two divided by nine is eight, so seven hundred and twenty divided by nine is eighty! Remember the balance rule: you must cancel the exact same number of trailing zeros from both the dividend and divisor."
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>⚡</span> The Zero Cancellation Shortcut
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    Cancel an equal number of trailing zeros from both the dividend and the divisor:
                </p>
                <div class="space-y-2 text-xs font-mono">
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60">
                        <div class="flex justify-between font-bold text-slate-200">
                            <span>7,200 ÷ 90</span>
                            <span class="text-emerald-400">= 80</span>
                        </div>
                        <div class="text-[11px] text-slate-400 mt-1">Cancel 1 zero: 720 ÷ 9 = 80</div>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60">
                        <div class="flex justify-between font-bold text-slate-200">
                            <span>4,500 ÷ 500</span>
                            <span class="text-emerald-400">= 9</span>
                        </div>
                        <div class="text-[11px] text-slate-400 mt-1">Cancel 2 zeros: 45 ÷ 5 = 9</div>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60">
                        <div class="flex justify-between font-bold text-slate-200">
                            <span>28,000 ÷ 70</span>
                            <span class="text-emerald-400">= 400</span>
                        </div>
                        <div class="text-[11px] text-slate-400 mt-1">Cancel 1 zero: 2,800 ÷ 7 = 400</div>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>📊</span> Place-Value Shift Grid
                    </h4>
                    <p class="text-xs text-slate-300 leading-relaxed mb-2">
                        Dividing by powers of 10 shifts digits to the right across standard place values:
                    </p>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 text-xs font-mono space-y-1">
                        <div class="flex justify-between text-slate-400 border-b border-slate-700 pb-1">
                            <span>OPERATION</span>
                            <span>SHIFT</span>
                            <span class="text-emerald-400">RESULT</span>
                        </div>
                        <div class="flex justify-between text-slate-300">
                            <span>5,000 ÷ 10</span>
                            <span>1 Place Right</span>
                            <span class="font-bold text-cyan-300">500</span>
                        </div>
                        <div class="flex justify-between text-slate-300">
                            <span>5,000 ÷ 100</span>
                            <span>2 Places Right</span>
                            <span class="font-bold text-cyan-300">50</span>
                        </div>
                        <div class="flex justify-between text-slate-300">
                            <span>5,000 ÷ 1,000</span>
                            <span>3 Places Right</span>
                            <span class="font-bold text-cyan-300">5</span>
                        </div>
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-rose-950/40 border border-rose-800/40 text-[11px] text-rose-200 mt-3">
                    ⚠️ <strong>Common Trap:</strong> Never cancel more zeros than the divisor possesses! In 3,000 ÷ 50, cancel only ONE zero: 300 ÷ 5 = 60 (not 6).
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c3_1",
                "question": "What is the value of 5,600 ÷ 70?",
                "options": [
                    "8",
                    "80",
                    "800",
                    "8,000"
                ],
                "answer": 1,
                "hint": "Cancel one zero from both numbers: 560 ÷ 7.",
                "explanation": "5,600 ÷ 70 = (5,600 ÷ 10) ÷ (70 ÷ 10) = 560 ÷ 7 = 80."
            },
            {
                "id": "c3_2",
                "question": "A shopkeeper has ₹4,200 and wants to convert the entire amount into ₹100 currency notes. How many ₹100 notes will he receive?",
                "options": [
                    "420 notes",
                    "42 notes",
                    "402 notes",
                    "4,200 notes"
                ],
                "answer": 1,
                "hint": "Divide ₹4,200 by 100 by canceling two trailing zeros.",
                "explanation": "4,200 ÷ 100 = 42 notes. Dividing by 100 cancels two trailing zeros."
            }
        ]
    },
    {
        "id": 4,
        "title": "Place Value Division",
        "tagline": "Real-World Problem Solving • Rate Calculations & Bonus Distribution",
        "lecture": (
            "Division with multiples of ten and hundred plays a vital role in everyday planning, sports journeys, and commercial farm accounts. Consider a long-distance cyclist embarking on an adventurous coastal journey across the Western Ghats. The cyclist covers a total distance of one hundred and sixty kilometres in twenty days, pedaling the exact same distance every single day. How many kilometres does the cyclist travel daily? We divide one hundred and sixty by twenty. By canceling one trailing zero from both numbers, one hundred and sixty divided by twenty simplifies to sixteen divided by two, which equals eight kilometres per day! Now imagine a prosperous coconut farming cooperative that earns a seasonal surplus and decides to distribute an equal cash bonus among its thirty dedicated farm workers. If the total bonus fund is twenty-one thousand rupees, how much money does each worker take home? We divide twenty-one thousand by thirty. Canceling one zero from each side transforms the expression into twenty-one hundred divided by three. Since twenty-one divided by three is seven, twenty-one hundred divided by three yields seven hundred rupees per worker. Place value shifts allow us to manage community resources and solve real-world logistical challenges with speed and precision."
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>🚴</span> Coastal Cycling Tour Rate
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    Calculate daily distance: Total Distance ÷ Total Days:
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/80 font-mono text-xs space-y-1.5">
                    <div class="flex justify-between text-slate-300">
                        <span>Total Journey:</span>
                        <span class="text-cyan-300 font-bold">160 km</span>
                    </div>
                    <div class="flex justify-between text-slate-300">
                        <span>Duration:</span>
                        <span class="text-amber-300 font-bold">20 days</span>
                    </div>
                    <div class="flex justify-between border-t border-slate-700 pt-1 text-emerald-400 font-black text-sm">
                        <span>Daily Rate:</span>
                        <span>160 ÷ 20 = 8 km/day</span>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>💰</span> Equal Bonus Allocation
                    </h4>
                    <p class="text-xs text-slate-300 leading-relaxed mb-2">
                        Sharing a ₹21,000 profit bonus among 30 farm workers:
                    </p>
                    <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700/80 font-mono text-xs space-y-1.5">
                        <div class="flex justify-between text-slate-300">
                            <span>Bonus Fund:</span>
                            <span class="text-cyan-300 font-bold">₹21,000</span>
                        </div>
                        <div class="flex justify-between text-slate-300">
                            <span>Workers:</span>
                            <span class="text-amber-300 font-bold">30 workers</span>
                        </div>
                        <div class="flex justify-between border-t border-slate-700 pt-1 text-emerald-400 font-black text-sm">
                            <span>Per Worker:</span>
                            <span>21,000 ÷ 30 = ₹700</span>
                        </div>
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-800/40 text-[11px] text-emerald-200 mt-3">
                    💡 <strong>Mental Step:</strong> Cancel 1 zero: 2,100 ÷ 3. Since 21 ÷ 3 = 7, append the two remaining zeros to get 700!
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c4_1",
                "question": "A wholesale grain dealer has 3,500 kg of wheat to pack into bags holding 50 kg each. How many bags does the dealer need?",
                "options": [
                    "70 bags",
                    "700 bags",
                    "50 bags",
                    "35 bags"
                ],
                "answer": 0,
                "hint": "Cancel one zero from 3,500 and 50: 350 ÷ 5.",
                "explanation": "3,500 ÷ 50 = 350 ÷ 5 = 70 bags."
            },
            {
                "id": "c4_2",
                "question": "A school library receives 1,800 new books and distributes them equally among 60 classrooms. How many books does each classroom receive?",
                "options": [
                    "300 books",
                    "30 books",
                    "18 books",
                    "60 books"
                ],
                "answer": 1,
                "hint": "Cancel one zero from 1,800 and 60: 180 ÷ 6.",
                "explanation": "1,800 ÷ 60 = 180 ÷ 6 = 30 books per classroom."
            }
        ]
    },
    {
        "id": 5,
        "title": "Convenient Splitting",
        "tagline": "Mental Strategies for Division • Additive & Subtractive Dividend Partitioning",
        "lecture": (
            "When faced with multi-digit division problems, mental mathematicians rarely perform vertical long division on paper. Instead, they use convenient splitting, which applies the distributive property of division over addition and subtraction. To divide a complex dividend, we decompose it into friendly numbers that are readily recognized multiples of the divisor. Let us solve one thousand two hundred and forty-eight divided by six. Twelve hundred and forty-eight easily splits into twelve hundred plus forty-eight. Both parts are exact multiples of six! Twelve hundred divided by six equals two hundred, and forty-eight divided by six equals eight. Adding two hundred and eight yields two hundred and eight! Splitting also works brilliantly using subtraction when a number is just below a friendly round benchmark. Consider one thousand nine hundred and ninety-two divided by four. Notice that one thousand nine hundred and ninety-two is only eight less than two thousand! We express it as two thousand minus eight. Now divide each part by four: two thousand divided by four equals five hundred, and eight divided by four equals two. Subtracting two from five hundred gives four hundred and ninety-eight! Convenient splitting turns intimidating calculations into fast, elegant mental solutions."
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>➕</span> Additive Splitting: 1,248 ÷ 6
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    Split 1,248 into two friendly multiples of 6: 1,200 and 48:
                </p>
                <div class="p-3 rounded-lg bg-slate-900/60 border border-slate-700/60 font-mono text-xs space-y-2">
                    <div class="text-cyan-300">1,248 ÷ 6 = (1,200 ÷ 6) + (48 ÷ 6)</div>
                    <div class="flex justify-between text-slate-300 border-t border-slate-700 pt-1">
                        <span>Part 1: 1,200 ÷ 6</span>
                        <span class="text-amber-300 font-bold">= 200</span>
                    </div>
                    <div class="flex justify-between text-slate-300">
                        <span>Part 2: 48 ÷ 6</span>
                        <span class="text-amber-300 font-bold">= 8</span>
                    </div>
                    <div class="flex justify-between border-t border-slate-700 pt-1 text-emerald-400 font-black text-sm">
                        <span>Combine: 200 + 8</span>
                        <span>= 208</span>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>➖</span> Subtractive Splitting: 1,992 ÷ 4
                    </h4>
                    <p class="text-xs text-slate-300 leading-relaxed mb-2">
                        When close to a round thousand, round up and subtract the excess:
                    </p>
                    <div class="p-3 rounded-lg bg-slate-900/60 border border-slate-700/60 font-mono text-xs space-y-2">
                        <div class="text-cyan-300">1,992 ÷ 4 = (2,000 ÷ 4) - (8 ÷ 4)</div>
                        <div class="flex justify-between text-slate-300 border-t border-slate-700 pt-1">
                            <span>Part 1: 2,000 ÷ 4</span>
                            <span class="text-amber-300 font-bold">= 500</span>
                        </div>
                        <div class="flex justify-between text-slate-300">
                            <span>Part 2: 8 ÷ 4</span>
                            <span class="text-amber-300 font-bold">= 2</span>
                        </div>
                        <div class="flex justify-between border-t border-slate-700 pt-1 text-emerald-400 font-black text-sm">
                            <span>Subtract: 500 - 2</span>
                            <span>= 498</span>
                        </div>
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-indigo-950/40 border border-indigo-800/40 text-[11px] text-indigo-200 mt-3">
                    💡 <strong>Selection Key:</strong> Choose multiples ending in zeros (like 1,200 or 2,000) so mental division takes only a split second!
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c5_1",
                "question": "Using additive convenient splitting, what is the fastest way to calculate 1,535 ÷ 5 mentally?",
                "options": [
                    "(1,500 ÷ 5) + (35 ÷ 5) = 300 + 7 = 307",
                    "(1,000 ÷ 5) + (535 ÷ 5) = 200 + 107 = 307",
                    "(1,500 ÷ 5) + (35 ÷ 5) = 30 + 7 = 37",
                    "(2,000 ÷ 5) - (465 ÷ 5) = 400 - 93 = 307"
                ],
                "answer": 0,
                "hint": "Split 1,535 into 1,500 and 35.",
                "explanation": "1,535 splits into 1,500 + 35. 1,500 ÷ 5 = 300, and 35 ÷ 5 = 7. Sum = 300 + 7 = 307."
            },
            {
                "id": "c5_2",
                "question": "Use subtractive splitting to find 2,991 ÷ 3:",
                "options": [
                    "(3,000 ÷ 3) - (9 ÷ 3) = 1,000 - 3 = 997",
                    "(3,000 ÷ 3) - (1 ÷ 3) = 1,000 - 1 = 999",
                    "(2,700 ÷ 3) + (291 ÷ 3) = 900 + 97 = 997",
                    "(3,000 ÷ 3) - (9 ÷ 3) = 100 - 3 = 97"
                ],
                "answer": 0,
                "hint": "2,991 is 9 less than 3,000. Write as (3,000 - 9) ÷ 3.",
                "explanation": "2,991 = 3,000 - 9. (3,000 ÷ 3) - (9 ÷ 3) = 1,000 - 3 = 997."
            }
        ]
    },
    {
        "id": 6,
        "title": "Repeated Halving",
        "tagline": "Mental Strategies for Division • Powers of 2 (÷4 and ÷8) Shortcuts",
        "lecture": (
            "Dividing by numbers that are powers of two—specifically four and eight—can be accomplished rapidly without standard long division by using repeated halving. The number four is two times two, which means that dividing any quantity by four is mathematically identical to finding half of the number, and then finding half of that result again! Let us test this with five hundred and twenty-eight divided by four. Step one: find half of five hundred and twenty-eight. Half of five hundred is two hundred and fifty, and half of twenty-eight is fourteen, giving two hundred and sixty-four. Step two: find half of two hundred and sixty-four. Half of two hundred is one hundred, and half of sixty-four is thirty-two, yielding one hundred and thirty-two! Therefore, five hundred and twenty-eight divided by four equals one hundred and thirty-two. What about dividing by eight? Since eight equals two times two times two, dividing by eight simply requires halving three times in succession! For instance, to divide nine hundred and sixty by eight: first half gives four hundred and eighty, second half gives two hundred and forty, and third half gives one hundred and twenty. Repeated halving bypasses bulky calculations with lightning-fast mental steps."
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>✂️</span> Dividing by 4: Two Halves
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    Dividing by 4 = Halving twice: (N ÷ 2) ÷ 2:
                </p>
                <div class="p-3 rounded-lg bg-slate-900/60 border border-slate-700/60 font-mono text-xs space-y-2">
                    <div class="text-cyan-300 font-bold">Calculate: 528 ÷ 4</div>
                    <div class="flex justify-between text-slate-300 border-t border-slate-700 pt-1">
                        <span>First Half (÷ 2):</span>
                        <span class="text-amber-300 font-bold">528 ÷ 2 = 264</span>
                    </div>
                    <div class="flex justify-between text-slate-300 border-t border-slate-700 pt-1">
                        <span>Second Half (÷ 2):</span>
                        <span class="text-emerald-400 font-bold">264 ÷ 2 = 132</span>
                    </div>
                    <div class="text-[11px] text-slate-400 mt-1">Result: 528 ÷ 4 = 132</div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>✂️✂️</span> Dividing by 8: Three Halves
                    </h4>
                    <p class="text-xs text-slate-300 leading-relaxed mb-2">
                        Dividing by 8 = Halving three times: ((N ÷ 2) ÷ 2) ÷ 2:
                    </p>
                    <div class="p-3 rounded-lg bg-slate-900/60 border border-slate-700/60 font-mono text-xs space-y-1.5">
                        <div class="text-cyan-300 font-bold">Calculate: 960 ÷ 8</div>
                        <div class="flex justify-between text-slate-300">
                            <span>1st Half:</span>
                            <span class="text-amber-300">960 ÷ 2 = 480</span>
                        </div>
                        <div class="flex justify-between text-slate-300">
                            <span>2nd Half:</span>
                            <span class="text-amber-300">480 ÷ 2 = 240</span>
                        </div>
                        <div class="flex justify-between text-slate-300">
                            <span>3rd Half:</span>
                            <span class="text-emerald-400 font-bold">240 ÷ 2 = 120</span>
                        </div>
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-800/40 text-[11px] text-emerald-200 mt-3">
                    💡 <strong>Summary Axiom:</strong> ÷ 4 = Half of Half. ÷ 8 = Half of Half of Half. Halving even numbers is naturally intuitive!
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c6_1",
                "question": "Use repeated halving to calculate 744 ÷ 4:",
                "options": [
                    "186",
                    "184",
                    "196",
                    "372"
                ],
                "answer": 0,
                "hint": "Half of 744 is 372. Half of 372 is 186.",
                "explanation": "First half: 744 ÷ 2 = 372. Second half: 372 ÷ 2 = 186. So 744 ÷ 4 = 186."
            },
            {
                "id": "c6_2",
                "question": "What is 1,280 ÷ 8 using three successive halves?",
                "options": [
                    "320",
                    "160",
                    "80",
                    "640"
                ],
                "answer": 1,
                "hint": "Half 1 = 640. Half 2 = 320. Half 3 = 160.",
                "explanation": "1,280 ÷ 2 = 640. 640 ÷ 2 = 320. 320 ÷ 2 = 160. So 1,280 ÷ 8 = 160."
            }
        ]
    },
    {
        "id": 7,
        "title": "Partial Quotients",
        "tagline": "Susie's Farm in Kerala • Repeated Subtraction vs Optimized Partial Quotients",
        "lecture": (
            "On Susie's coconut farm in Kerala, workers collect five hundred and eighty-two coconuts that must be bundled into sets of six for transportation to the wholesale market. How can we divide five hundred and eighty-two by six? Susie and her cousin Sunitha use two different partial quotient strategies. Susie uses small, cautious chunks: she subtracts fifty bundles of six, which is three hundred coconuts, leaving two hundred and eighty-two. Then she subtracts twenty bundles of six, which is one hundred and twenty, leaving one hundred and sixty-two. She continues chipping away until all coconuts are bundled. Sunitha, however, is an optimization master! Sunitha looks at five hundred and eighty-two and asks: what is the largest friendly multiple of six close to five hundred and eighty-two? She knows ninety times six is five hundred and forty! So Sunitha takes a giant leap of ninety bundles at once. Five hundred and eighty-two minus five hundred and forty leaves only forty-two coconuts! From table facts, seven times six is forty-two. Adding her two partial quotients—ninety plus seven—Sunitha finishes the division in just two clean steps, reaching ninety-seven bundles! Taking larger partial quotient leaps saves time and prevents computational errors."
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>🌴</span> Sunitha's Optimized Partial Quotients (582 ÷ 6)
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    Take large, confident multiples of 6 to reach the answer in two steps:
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/80 font-mono text-xs space-y-1.5">
                    <div class="flex justify-between text-slate-300">
                        <span>Total Coconuts:</span>
                        <span class="text-cyan-300 font-bold">582</span>
                    </div>
                    <div class="flex justify-between text-amber-300">
                        <span>Leap 1 (90 bundles × 6):</span>
                        <span>- 540 (Partial Q: 90)</span>
                    </div>
                    <div class="flex justify-between border-t border-slate-700 pt-1 text-slate-300">
                        <span>Remainder to bundle:</span>
                        <span class="text-cyan-300 font-bold">42</span>
                    </div>
                    <div class="flex justify-between text-amber-300">
                        <span>Leap 2 (7 bundles × 6):</span>
                        <span>- 42 (Partial Q: 7)</span>
                    </div>
                    <div class="flex justify-between border-t border-slate-700 pt-1 text-emerald-400 font-black text-sm">
                        <span>Total Quotient (90 + 7):</span>
                        <span>= 97 Bundles</span>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>⚖️</span> Susie's vs Sunitha's Methods
                    </h4>
                    <p class="text-xs text-slate-300 leading-relaxed mb-2">
                        Both methods are mathematically sound, but larger partial quotients are much more efficient:
                    </p>
                    <div class="space-y-1.5 text-xs">
                        <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-700/60">
                            <span class="font-bold text-slate-300">Susie's Cautious Chunks:</span>
                            <div class="text-slate-400 text-[11px] mt-0.5">Subtracts 50 × 6, then 20 × 6, then 20 × 6, then 7 × 6 (4 steps).</div>
                        </div>
                        <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-700/60">
                            <span class="font-bold text-emerald-400">Sunitha's Optimized Leaps:</span>
                            <div class="text-slate-300 text-[11px] mt-0.5">Subtracts 90 × 6 = 540, then 7 × 6 = 42 (2 fast steps!).</div>
                        </div>
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-cyan-950/40 border border-cyan-800/40 text-[11px] text-cyan-200 mt-3">
                    💡 <strong>Strategy:</strong> Look for the largest tens multiple first (10×, 20×, 50×, 100×) to make the biggest dent in the dividend.
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c7_1",
                "question": "To solve 438 ÷ 6 using partial quotients, what is the largest convenient tens multiple of 6 to subtract first?",
                "options": [
                    "70 × 6 = 420",
                    "60 × 6 = 360",
                    "50 × 6 = 300",
                    "80 × 6 = 480"
                ],
                "answer": 0,
                "hint": "Find a multiple of 6 close to 43 without exceeding it: 6 × 7 = 42, so 6 × 70 = 420.",
                "explanation": "6 × 70 = 420, which is close to 438 without exceeding it. 80 × 6 = 480 is too large. So 70 is the optimal first leap."
            },
            {
                "id": "c7_2",
                "question": "After subtracting 70 × 6 = 420 from 438, 18 remains. What is the final quotient of 438 ÷ 6?",
                "options": [
                    "73",
                    "72",
                    "74",
                    "68"
                ],
                "answer": 0,
                "hint": "18 ÷ 6 = 3. Add 70 + 3.",
                "explanation": "18 ÷ 6 = 3. Total quotient = 70 + 3 = 73."
            }
        ]
    },
    {
        "id": 8,
        "title": "Division Algorithm",
        "tagline": "Let Us Learn to Divide • Remainders & The Fundamental Division Equation",
        "lecture": (
            "In real life, harvested items cannot always be divided into perfectly equal shares without something left over. When forty-seven tender coconuts are distributed equally among five eager school children, each child receives nine coconuts, but two coconuts remain in the basket because two is smaller than five and cannot be shared equally. This leftover quantity is called the Remainder, symbolized by the letter R. This observation leads directly to the celebrated Fundamental Division Algorithm of arithmetic: Dividend equals Divisor multiplied by Quotient plus Remainder. In mathematical symbols: N equals D times Q plus R. In our coconut example: forty-seven equals five times nine plus two, because five times nine is forty-five, and forty-five plus two is forty-seven. Notice the unbreakable mathematical condition governing all remainders: the remainder must always be strictly less than the divisor, and greater than or equal to zero! In symbols, zero is less than or equal to R, which is strictly less than D. If your remainder is ever equal to or greater than the divisor, it means you can form at least one more full group, proving your quotient was too small. The division algorithm provides an airtight algebraic equation to verify whether your long division calculation is completely correct."
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>🥥</span> Sharing 47 Coconuts Among 5 Children
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    Each child receives an equal share, leaving a leftover remainder:
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/80 font-mono text-xs space-y-2">
                    <div class="flex justify-between text-slate-300 border-b border-slate-700 pb-1">
                        <span>Dividend (N):</span>
                        <span class="text-cyan-300 font-bold">47 Coconuts</span>
                    </div>
                    <div class="flex justify-between text-slate-300 border-b border-slate-700 pb-1">
                        <span>Divisor (D):</span>
                        <span class="text-amber-300 font-bold">5 Children</span>
                    </div>
                    <div class="flex justify-between text-slate-300 border-b border-slate-700 pb-1">
                        <span>Quotient (Q):</span>
                        <span class="text-emerald-400 font-bold">9 Coconuts each</span>
                    </div>
                    <div class="flex justify-between text-slate-300">
                        <span>Remainder (R):</span>
                        <span class="text-rose-400 font-bold">2 Coconuts left over</span>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>⚖️</span> The Fundamental Division Equation
                    </h4>
                    <div class="p-3 rounded-xl bg-gradient-to-r from-cyan-500/10 via-emerald-500/10 to-amber-500/10 border border-cyan-500/30 text-center my-2 font-mono">
                        <div class="text-base font-black text-emerald-300">N = (D × Q) + R</div>
                        <div class="text-[11px] text-amber-300 mt-1">47 = (5 × 9) + 2 = 45 + 2</div>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 text-xs text-slate-300 space-y-1">
                        <div class="font-bold text-amber-300">The Golden Remainder Condition:</div>
                        <div class="font-mono text-cyan-300">0 ≤ R < D</div>
                        <div class="text-[11px] text-slate-400">The remainder must be strictly smaller than the divisor!</div>
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-indigo-950/40 border border-indigo-800/40 text-[11px] text-indigo-200 mt-3">
                    🔍 <strong>Verification Rule:</strong> Always check: Divisor × Quotient + Remainder MUST equal Dividend. If it does not match, re-check your subtraction!
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c8_1",
                "question": "When dividing a whole number by 7, which of the following could NEVER be the remainder?",
                "options": [
                    "0",
                    "3",
                    "6",
                    "7"
                ],
                "answer": 3,
                "hint": "The remainder must always be strictly less than the divisor (R < 7).",
                "explanation": "Because 0 ≤ R < D, dividing by 7 can only produce remainders of 0, 1, 2, 3, 4, 5, or 6. A remainder of 7 means you can make another group of 7!"
            },
            {
                "id": "c8_2",
                "question": "A student performs division and finds Divisor = 8, Quotient = 15, Remainder = 5. What was the Dividend?",
                "options": [
                    "120",
                    "125",
                    "115",
                    "128"
                ],
                "answer": 1,
                "hint": "Use the division equation: Dividend = (Divisor × Quotient) + Remainder.",
                "explanation": "Dividend = (8 × 15) + 5 = 120 + 5 = 125."
            }
        ]
    }
]
