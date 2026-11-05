# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 9: Coconut Farm
Part 2: Slides 9 to 16
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Group Allocation",
        "tagline": "Application Word Problems • Trip Buses, Catering Logistics & Note Combos",
        "lecture": (
            "Division with remainders is not merely an abstract classroom exercise; it is an indispensable tool for managing real-world community events, transport systems, and trip logistics. Suppose a school plans an excursion to a botanical garden for two hundred and forty-eight students and teachers. If each chartered bus has a seating capacity of fifty passengers, how many buses must the principal book? Dividing two hundred and forty-eight by fifty gives a quotient of four buses with a remainder of forty-eight passengers! If the school booked only four buses, forty-eight students would be left behind crying at the school gate! In logistics, when a remainder occurs, we must round up to the next whole bus. The school must book five buses, even though the fifth bus will have two empty seats. Another practical scenario involves currency note combinations. Suppose you need to pay five hundred and twenty rupees using only fifty-rupee and twenty-rupee notes. Dividing five hundred and twenty by fifty gives ten fifty-rupee notes with a remainder of twenty rupees. That remaining twenty rupees is paid with exactly one twenty-rupee note! In group allocation, interpreting the remainder correctly makes the critical difference between seamless organization and logistical chaos."
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>🚌</span> School Excursion Bus Logistics
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    248 passengers divided into 50-seater buses requires remainder rounding up:
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/80 font-mono text-xs space-y-1.5">
                    <div class="flex justify-between text-slate-300">
                        <span>Total Passengers:</span>
                        <span class="text-cyan-300 font-bold">248</span>
                    </div>
                    <div class="flex justify-between text-slate-300">
                        <span>Bus Capacity:</span>
                        <span class="text-amber-300 font-bold">50 seats</span>
                    </div>
                    <div class="flex justify-between border-t border-slate-700 pt-1 text-slate-300">
                        <span>Mathematical Division:</span>
                        <span>248 ÷ 50 = 4 R 48</span>
                    </div>
                    <div class="flex justify-between border-t border-slate-700 pt-1 text-emerald-400 font-black text-sm">
                        <span>Buses to Book:</span>
                        <span>5 Buses (Ceiling Rounding)</span>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>💵</span> Note Combination: Pay ₹520
                    </h4>
                    <p class="text-xs text-slate-300 leading-relaxed mb-2">
                        Decompose using ₹50 and ₹20 notes systematically:
                    </p>
                    <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700/80 font-mono text-xs space-y-1.5">
                        <div class="flex justify-between text-slate-300">
                            <span>Primary Notes (₹50):</span>
                            <span class="text-cyan-300 font-bold">10 notes = ₹500</span>
                        </div>
                        <div class="flex justify-between text-slate-300">
                            <span>Remainder:</span>
                            <span class="text-amber-300 font-bold">₹520 - ₹500 = ₹20</span>
                        </div>
                        <div class="flex justify-between border-t border-slate-700 pt-1 text-emerald-400 font-bold">
                            <span>Secondary Notes (₹20):</span>
                            <span>1 note = ₹20</span>
                        </div>
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-indigo-950/40 border border-indigo-800/40 text-[11px] text-indigo-200 mt-3">
                    💡 <strong>Logistics Golden Rule:</strong> When transporting people or fragile goods, any non-zero remainder requires adding one extra container or vehicle!
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c9_1",
                "question": "A caterer has 175 samosas for a party. If each serving tray holds 24 samosas, how many trays are required to serve all 175 samosas?",
                "options": [
                    "7 trays",
                    "8 trays",
                    "9 trays",
                    "6 trays"
                ],
                "answer": 1,
                "hint": "175 ÷ 24 = 7 with a remainder of 7 samosas. Can we leave 7 samosas off the table?",
                "explanation": "175 ÷ 24 = 7 with remainder 7. 7 trays hold 168 samosas. To accommodate the remaining 7 samosas, an 8th tray is required."
            },
            {
                "id": "c9_2",
                "question": "Five friends share the cost of a restaurant dinner totaling ₹1,284 equally. If the bill cannot be split into paise, how much does each pay, and what is the small excess remainder?",
                "options": [
                    "₹256 each with ₹4 remainder",
                    "₹250 each with ₹34 remainder",
                    "₹255 each with ₹9 remainder",
                    "₹257 each with ₹0 remainder"
                ],
                "answer": 0,
                "hint": "Divide 1,284 by 5.",
                "explanation": "1,284 ÷ 5 = 256 with a remainder of 4. Each friend pays ₹256, leaving ₹4 to be covered."
            }
        ]
    },
    {
        "id": 10,
        "title": "Coconut Oil Math",
        "tagline": "Kalpavruksha Coconut Oil • Bulk Oil Extraction Yields & Revenue",
        "lecture": (
            "On the Kalpavruksha farm in south India, dry mature coconuts called copra are processed in an oil mill to produce pure coconut oil. The farm records show that exactly eight coconuts yield one litre of rich, fragrant oil. During the peak harvest season, the farm workers bring in four thousand three hundred and seventy-six coconuts for oil processing. How many litres of coconut oil will be extracted? We must divide four thousand three hundred and seventy-six by eight. Let us use place value division: forty-three divided by eight gives five with a remainder of three. Bring down seven to make thirty-seven; thirty-seven divided by eight gives four with a remainder of five. Bring down six to make fifty-six; fifty-six divided by eight gives seven with zero remainder! The mill extracts exactly five hundred and forty-seven litres of coconut oil. Next, the farm sells this oil in sealed tin containers at two hundred and forty rupees per litre. To calculate the total farm revenue, we multiply five hundred and forty-seven litres by two hundred and forty rupees, yielding one hundred and thirty-one thousand two hundred and eighty rupees! Dividing large numbers allows farmers to monitor processing efficiency and project seasonal income."
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>🥥</span> Copra Oil Extraction (4,376 ÷ 8)
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    8 coconuts = 1 litre of cold-pressed oil:
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/80 font-mono text-xs space-y-1.5">
                    <div class="flex justify-between text-slate-300">
                        <span>Total Coconuts:</span>
                        <span class="text-cyan-300 font-bold">4,376</span>
                    </div>
                    <div class="flex justify-between text-slate-300">
                        <span>Rate of Extraction:</span>
                        <span class="text-amber-300 font-bold">8 coconuts / Litre</span>
                    </div>
                    <div class="flex justify-between border-t border-slate-700 pt-1 text-slate-300">
                        <span>Division:</span>
                        <span>4,376 ÷ 8</span>
                    </div>
                    <div class="flex justify-between border-t border-slate-700 pt-1 text-emerald-400 font-black text-sm">
                        <span>Total Oil Yield:</span>
                        <span>547 Litres</span>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>💰</span> Commercial Farm Revenue Ledger
                    </h4>
                    <p class="text-xs text-slate-300 leading-relaxed mb-2">
                        Selling 547 litres of oil at ₹240 per litre:
                    </p>
                    <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700/80 font-mono text-xs space-y-1.5">
                        <div class="flex justify-between text-slate-300">
                            <span>Volume Sold:</span>
                            <span class="text-cyan-300 font-bold">547 Litres</span>
                        </div>
                        <div class="flex justify-between text-slate-300">
                            <span>Selling Price:</span>
                            <span class="text-amber-300 font-bold">₹240 / Litre</span>
                        </div>
                        <div class="flex justify-between border-t border-slate-700 pt-1 text-emerald-400 font-black text-sm">
                            <span>Total Farm Revenue:</span>
                            <span>₹1,31,280</span>
                        </div>
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-800/40 text-[11px] text-emerald-200 mt-3">
                    💡 <strong>Step Check:</strong> 547 × 8 = 4,376 coconuts. 547 × ₹240 = ₹1,31,280. The division and multiplication verify each other perfectly!
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c10_1",
                "question": "A smaller organic farm uses 6 coconuts to produce 1 litre of virgin coconut oil. How many litres of oil will they extract from 2,832 coconuts?",
                "options": [
                    "472 Litres",
                    "462 Litres",
                    "482 Litres",
                    "452 Litres"
                ],
                "answer": 0,
                "hint": "Divide 2,832 by 6: 28 ÷ 6 = 4 R 4; 43 ÷ 6 = 7 R 1; 12 ÷ 6 = 2.",
                "explanation": "2,832 ÷ 6 = 472 litres of oil."
            },
            {
                "id": "c10_2",
                "question": "If 472 litres of virgin oil is sold at ₹300 per litre, what is the gross earnings of the organic farm?",
                "options": [
                    "₹1,41,600",
                    "₹1,40,000",
                    "₹1,42,600",
                    "₹1,38,600"
                ],
                "answer": 0,
                "hint": "Multiply 472 by 300: 472 × 3 = 1,416. Append two zeros.",
                "explanation": "472 × ₹300 = ₹1,41,600."
            }
        ]
    },
    {
        "id": 11,
        "title": "Two-Digit Divisors",
        "tagline": "Kalpavruksha Farm Sales • Dividing by 23 and 35 via Estimation",
        "lecture": (
            "When dealing with wholesale agricultural sales and cargo transport, the divisor is frequently a two-digit number. Dividing by a two-digit divisor, such as twenty-three or thirty-five, requires rounding to estimate trial quotient digits with confidence. Consider the Kalpavruksha coir processing unit, where shredded coconut husk is pressed into uniform export bales weighing twenty-three kilograms each. If the farm workers accumulate nine thousand nine hundred and thirteen kilograms of dry husk, how many complete bales can they press? We must divide nine thousand nine hundred and thirteen by twenty-three. Let us estimate: twenty-three is close to twenty. To divide ninety-nine by twenty-three, think of ninety divided by twenty, which suggests four. Multiplying twenty-three by four gives ninety-two. Ninety-nine minus ninety-two leaves seven. Bring down one to make seventy-one. Seventy-one divided by twenty-three suggests three; twenty-three times three is sixty-nine. Seventy-one minus sixty-nine leaves two. Bring down three to make twenty-three; twenty-three divided by twenty-three is exactly one! The workers press exactly four hundred and thirty-one bales with zero husk left over. Similarly, dividing eight thousand eight hundred and ninety tender coconuts into crates of thirty-five yields two hundred and fifty-four full crates. Rounding the two-digit divisor to the nearest friendly ten helps you choose trial quotient digits accurately without tedious trial-and-error guessing."
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>🌾</span> Coconut Husk Bales (9,913 ÷ 23)
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    Round divisor 23 to 20 to estimate trial quotient digits:
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/80 font-mono text-xs space-y-1.5">
                    <div class="flex justify-between text-slate-300">
                        <span>Total Husk:</span>
                        <span class="text-cyan-300 font-bold">9,913 kg</span>
                    </div>
                    <div class="flex justify-between text-slate-300">
                        <span>Bale Weight:</span>
                        <span class="text-amber-300 font-bold">23 kg / bale</span>
                    </div>
                    <div class="border-t border-slate-700 pt-1 text-slate-300 space-y-0.5 text-[11px]">
                        <div>• 99 ÷ 23 ➔ 4 (4 × 23 = 92; Rem = 7)</div>
                        <div>• 71 ÷ 23 ➔ 3 (3 × 23 = 69; Rem = 2)</div>
                        <div>• 23 ÷ 23 ➔ 1 (1 × 23 = 23; Rem = 0)</div>
                    </div>
                    <div class="flex justify-between border-t border-slate-700 pt-1 text-emerald-400 font-black text-sm">
                        <span>Total Bales Pressed:</span>
                        <span>431 Bales</span>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>🥥</span> Tender Coconut Crates (8,890 ÷ 35)
                    </h4>
                    <p class="text-xs text-slate-300 leading-relaxed mb-2">
                        Packing 8,890 tender coconuts into crates of 35 each:
                    </p>
                    <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700/80 font-mono text-xs space-y-1.5">
                        <div class="flex justify-between text-slate-300">
                            <span>88 ÷ 35:</span>
                            <span class="text-cyan-300">2 (2 × 35 = 70; Rem = 18)</span>
                        </div>
                        <div class="flex justify-between text-slate-300">
                            <span>189 ÷ 35:</span>
                            <span class="text-cyan-300">5 (5 × 35 = 175; Rem = 14)</span>
                        </div>
                        <div class="flex justify-between text-slate-300">
                            <span>140 ÷ 35:</span>
                            <span class="text-cyan-300">4 (4 × 35 = 140; Rem = 0)</span>
                        </div>
                        <div class="flex justify-between border-t border-slate-700 pt-1 text-emerald-400 font-black text-sm">
                            <span>Total Crates:</span>
                            <span>254 Crates</span>
                        </div>
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-indigo-950/40 border border-indigo-800/40 text-[11px] text-indigo-200 mt-3">
                    💡 <strong>Trial Digit Rule:</strong> If trial digit × divisor exceeds the working dividend, reduce the trial digit by 1 and re-multiply!
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c11_1",
                "question": "When dividing 7,560 by 24, what is the best estimated trial digit for the first step (75 ÷ 24)?",
                "options": [
                    "3 (since 24 × 3 = 72)",
                    "4 (since 24 × 4 = 96)",
                    "2 (since 24 × 2 = 48)",
                    "5 (since 24 × 5 = 120)"
                ],
                "answer": 0,
                "hint": "Think of 75 ÷ 25 ≈ 3. Check 24 × 3 = 72.",
                "explanation": "24 × 3 = 72, which fits inside 75 with remainder 3. 24 × 4 = 96 is too large. So 3 is the correct first quotient digit."
            },
            {
                "id": "c11_2",
                "question": "What is the complete quotient of 7,560 ÷ 24?",
                "options": [
                    "315",
                    "325",
                    "310",
                    "305"
                ],
                "answer": 0,
                "hint": "75 ÷ 24 = 3 R 3; 36 ÷ 24 = 1 R 12; 120 ÷ 24 = 5.",
                "explanation": "75 ÷ 24 = 3 (rem 3); 36 ÷ 24 = 1 (rem 12); 120 ÷ 24 = 5 (rem 0). Total = 315."
            }
        ]
    },
    {
        "id": 12,
        "title": "Standard Algorithm",
        "tagline": "Division Using Place Value • The 4-Step Cycle: Divide, Multiply, Subtract, Bring Down",
        "lecture": (
            "The traditional vertical long division method is an algorithm celebrated worldwide for its compact efficiency. It breaks the division of a massive multi-digit number into an organized, repeating four-step cycle: Divide, Multiply, Subtract, and Bring Down! A popular memory rhyme for these four steps is: Daddy, Mommy, Sister, Brother. Let us trace this cycle by dividing seven thousand and thirty-two by six. Step one, Divide: divide seven by six, which gives one. Step two, Multiply: multiply one by six to get six. Step three, Subtract: subtract six from seven to leave one. Step four, Bring Down: bring down zero from the hundreds place to form ten. Now the cycle repeats! Divide ten by six to get one. Multiply one by six to get six. Subtract six from ten to get four. Bring down three from the tens place to form forty-three. Repeat again! Forty-three divided by six gives seven. Multiply seven by six to get forty-two. Subtract forty-two from forty-three to get one. Finally, bring down two to make twelve; twelve divided by six is two with zero remainder. The quotient is exactly one thousand one hundred and seventy-two. Following the four-step rhythm guarantees complete accuracy."
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>🔁</span> The 4-Step Long Division Cycle
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    Repeat this 4-step sequence for every digit brought down from the dividend:
                </p>
                <div class="grid grid-cols-2 gap-2 text-xs font-mono">
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 text-center">
                        <span class="text-cyan-400 font-bold block text-sm">1. DIVIDE (D)</span>
                        <span class="text-slate-400 text-[10px]">How many times does it fit?</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 text-center">
                        <span class="text-amber-400 font-bold block text-sm">2. MULTIPLY (M)</span>
                        <span class="text-slate-400 text-[10px]">Quotient digit × Divisor</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 text-center">
                        <span class="text-rose-400 font-bold block text-sm">3. SUBTRACT (S)</span>
                        <span class="text-slate-400 text-[10px]">Find remaining difference</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 text-center">
                        <span class="text-emerald-400 font-bold block text-sm">4. BRING DOWN (B)</span>
                        <span class="text-slate-400 text-[10px]">Next place value digit</span>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>📝</span> Vertical Work: 7,032 ÷ 6 = 1,172
                    </h4>
                    <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700/80 font-mono text-xs space-y-1">
                        <div class="text-emerald-400 font-bold text-right">Quotient: 1,172</div>
                        <div class="border-t border-slate-700 pt-1">
                            <div>6 ) 7 0 3 2</div>
                            <div class="text-slate-400">- 6 ➔ (7 - 6 = 1)</div>
                            <div>  1 0 ➔ (bring down 0)</div>
                            <div class="text-slate-400">-   6 ➔ (10 - 6 = 4)</div>
                            <div>    4 3 ➔ (bring down 3)</div>
                            <div class="text-slate-400">-   4 2 ➔ (43 - 42 = 1)</div>
                            <div>      1 2 ➔ (bring down 2)</div>
                            <div class="text-emerald-400">-     1 2 ➔ (Remainder = 0)</div>
                        </div>
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-cyan-950/40 border border-cyan-800/40 text-[11px] text-cyan-200 mt-3">
                    💡 <strong>Memory Rhyme:</strong> <strong>D</strong>ivide, <strong>M</strong>ultiply, <strong>S</strong>ubtract, <strong>B</strong>ring down (Daddy, Mommy, Sister, Brother)!
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c12_1",
                "question": "What is the third step in the standard 4-step vertical division algorithm?",
                "options": [
                    "Bring Down",
                    "Subtract",
                    "Multiply",
                    "Divide"
                ],
                "answer": 1,
                "hint": "Divide (1), Multiply (2), Subtract (3), Bring Down (4).",
                "explanation": "The four steps in order are: 1. Divide, 2. Multiply, 3. Subtract, 4. Bring Down. The third step is Subtract."
            },
            {
                "id": "c12_2",
                "question": "In vertical long division, immediately after you subtract and find the difference, what must you do next?",
                "options": [
                    "Multiply by the quotient",
                    "Bring down the next digit from the dividend",
                    "Stop the calculation",
                    "Add the divisor"
                ],
                "answer": 1,
                "hint": "After subtracting, bring down the next place-value digit to form the new working dividend.",
                "explanation": "After subtracting to find the local remainder, the next operation in the cycle is Bring Down."
            }
        ]
    },
    {
        "id": 13,
        "title": "Zero Quotient Traps",
        "tagline": "Division Using Place Value • Handling Internal Zero Quotients",
        "lecture": (
            "One of the most frequent errors made by primary school students in long division is the famous zero quotient trap! When a student brings down a digit from the dividend, and that new working number is strictly smaller than the divisor, many students mistakenly bring down another digit immediately without writing a zero in the quotient. This omission shrinks the answer by a factor of ten! Consider three thousand and five divided by five. Let us follow the steps carefully: three thousand divided by five gives six in the hundreds place, because six times five is thirty. Thirty minus thirty leaves zero. Now, bring down zero from the tens place. How many times does five go into zero? Exactly zero times! You must write zero in the tens place of the quotient. Next, bring down five from the ones place. Five goes into five exactly one time, giving six hundred and one. If a student forgets the placeholder zero, they write sixty-one instead of six hundred and one! To see how ridiculous sixty-one is, simply multiply back: sixty-one times five is only three hundred and five, not three thousand and five! Never forget: whenever you bring down a digit, you must record a quotient digit, even if that digit is zero."
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>⚠️</span> The Fatal Zero-Omission Trap
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    Compare the catastrophic error versus the correct place-value division:
                </p>
                <div class="space-y-2 text-xs">
                    <div class="p-2.5 rounded-lg bg-rose-950/40 border border-rose-800/40">
                        <div class="font-bold text-rose-300">❌ Fatal Trap: 3,005 ÷ 5 = 61</div>
                        <p class="text-[11px] text-slate-300 mt-1">
                            The student brought down 0, saw it didn't fit, and brought down 5 without writing 0 in the quotient! Verification: 61 × 5 = 305 (WRONG by 2,700!).
                        </p>
                    </div>
                    <div class="p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-800/40">
                        <div class="font-bold text-emerald-300">✓ Correct Method: 3,005 ÷ 5 = 601</div>
                        <p class="text-[11px] text-slate-300 mt-1">
                            0 tens ÷ 5 = 0 tens in quotient. Verification: 601 × 5 = 3,005 (PERFECT MATCH!).
                        </p>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>🛡️</span> The 1-to-1 Bring Down Rule
                    </h4>
                    <p class="text-xs text-slate-300 leading-relaxed mb-2">
                        Every single digit brought down from the dividend DEMANDS a digit in the quotient:
                    </p>
                    <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700/80 font-mono text-xs space-y-1">
                        <div>4 ) 8 0 2 4</div>
                        <div>• 8 ÷ 4 = 2 (Hundreds)</div>
                        <div class="text-amber-300">• Bring down 0 ➔ 0 ÷ 4 = 0 (Tens)</div>
                        <div class="text-amber-300">• Bring down 2 ➔ 2 ÷ 4 = 0 (Ones)</div>
                        <div>• Wait: 24 ÷ 4 = 6</div>
                        <div class="text-emerald-400 font-bold border-t border-slate-700 pt-1">Result: 8,024 ÷ 4 = 2,006</div>
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-cyan-950/40 border border-cyan-800/40 text-[11px] text-cyan-200 mt-3">
                    🔍 <strong>Quick Sanity Check:</strong> 8,000 ÷ 4 is roughly 2,000. So the quotient must have four digits (around 2,000), never three!
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c13_1",
                "question": "What is the quotient when 4,016 is divided by 4?",
                "options": [
                    "1,004",
                    "104",
                    "1,040",
                    "14"
                ],
                "answer": 0,
                "hint": "4 ÷ 4 = 1. Bring down 0 ➔ 0. Bring down 1 ➔ 0. Bring down 6 ➔ 16 ÷ 4 = 4.",
                "explanation": "4,016 ÷ 4: 4 ÷ 4 = 1; 0 ÷ 4 = 0; 1 ÷ 4 = 0; 16 ÷ 4 = 4. Quotient = 1,004. Notice the two placeholder zeros!"
            },
            {
                "id": "c13_2",
                "question": "A student calculates 6,036 ÷ 6 and writes 16. Why is this answer clearly incorrect?",
                "options": [
                    "Because 16 × 6 = 96, which is nowhere near 6,036!",
                    "Because 6,036 is an odd number",
                    "Because 6 cannot divide 36",
                    "Because 6,000 ÷ 6 is 100"
                ],
                "answer": 0,
                "hint": "Multiply the student's answer by the divisor to check reasonableness.",
                "explanation": "6,000 ÷ 6 is 1,000, so the quotient must be around 1,006. 16 is smaller by a factor of over 60 times because the student dropped two zeros!"
            }
        ]
    },
    {
        "id": 14,
        "title": "Resource Bottlenecks",
        "tagline": "Resource Optimization & Tour Logistics • Identifying Limiting Constraints",
        "lecture": (
            "In modern engineering, furniture manufacturing, and sports tour planning, multi-step division is used to identify bottlenecks—the single limiting resource that caps total production. Consider a village carpenter who manufactures wooden bookshelves for rural school libraries. Each bookshelf requires four wooden panels, six joining clips, and sixteen steel screws. In his workshop inventory, the carpenter counts twenty-six panels, thirty-three clips, and eighty screws. How many complete bookshelves can he build? Let us analyze each component separately using division. For panels: twenty-six divided by four equals six bookshelves with a remainder of two panels. For clips: thirty-three divided by six equals five bookshelves with a remainder of three clips. For screws: eighty divided by sixteen equals exactly five bookshelves! Comparing the three division results: the panels allow six shelves, but the clips and screws allow only five. Even though there are two leftover panels, the carpenter cannot build a sixth shelf because he has completely run out of clips and screws! The limiting resources are the clips and screws, restricting production to five complete bookshelves. Likewise, on a five hundred and eighty-five kilometre cycle rally, nine equal daily stages require riding sixty-five kilometres per day. Identifying bottlenecks through division prevents over-ordering redundant parts and optimizes commercial workshop productivity."
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>🪚</span> The Carpenter's Stock Bottleneck
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    Each bookshelf needs: 4 panels, 6 clips, 16 screws:
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/80 font-mono text-xs space-y-2">
                    <div class="flex justify-between text-slate-300">
                        <span>Panels (26 in stock):</span>
                        <span class="text-cyan-300">26 ÷ 4 = <strong>6 Shelves</strong> (R 2)</span>
                    </div>
                    <div class="flex justify-between text-slate-300">
                        <span>Clips (33 in stock):</span>
                        <span class="text-amber-300">33 ÷ 6 = <strong>5 Shelves</strong> (R 3)</span>
                    </div>
                    <div class="flex justify-between text-slate-300">
                        <span>Screws (80 in stock):</span>
                        <span class="text-amber-300">80 ÷ 16 = <strong>5 Shelves</strong> (R 0)</span>
                    </div>
                    <div class="flex justify-between border-t border-slate-700 pt-1 text-emerald-400 font-black text-sm">
                        <span>Max Bookshelves Built:</span>
                        <span>5 Shelves (Bottleneck = Clips & Screws)</span>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>🚴</span> Mumbai to Goa Cycle Rally Route
                    </h4>
                    <p class="text-xs text-slate-300 leading-relaxed mb-2">
                        Planning 585 km route via Ratnagiri over uniform daily riding stages:
                    </p>
                    <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700/80 font-mono text-xs space-y-1.5">
                        <div class="flex justify-between text-slate-300">
                            <span>Total Distance:</span>
                            <span class="text-cyan-300 font-bold">585 km</span>
                        </div>
                        <div class="flex justify-between text-slate-300">
                            <span>Stage Plan:</span>
                            <span class="text-amber-300 font-bold">9 Riding Days</span>
                        </div>
                        <div class="flex justify-between border-t border-slate-700 pt-1 text-emerald-400 font-black text-sm">
                            <span>Daily Stage Target:</span>
                            <span>585 ÷ 9 = 65 km/day</span>
                        </div>
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-indigo-950/40 border border-indigo-800/40 text-[11px] text-indigo-200 mt-3">
                    💡 <strong>Bottleneck Principle:</strong> The overall capacity of any manufacturing system is determined by its most scarce component—the minimum of all quotient limits!
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c14_1",
                "question": "A toy car factory requires 4 wheels and 2 seats to assemble 1 toy car. If their stock contains 50 wheels and 22 seats, what is the maximum number of toy cars they can complete?",
                "options": [
                    "11 cars",
                    "12 cars",
                    "10 cars",
                    "22 cars"
                ],
                "answer": 0,
                "hint": "Wheels allow: 50 ÷ 4 = 12 cars. Seats allow: 22 ÷ 2 = 11 cars. Take the smaller limit.",
                "explanation": "50 wheels can make 12 cars (with 2 wheels left). But 22 seats can make only 11 cars. When 11 cars are built, all seats are exhausted. Max cars = 11."
            },
            {
                "id": "c14_2",
                "question": "A coastal cycle rally of 672 km is scheduled across 8 equal daily stages. What distance must riders complete each day?",
                "options": [
                    "84 km",
                    "82 km",
                    "86 km",
                    "74 km"
                ],
                "answer": 0,
                "hint": "Divide 672 by 8: 67 ÷ 8 = 8 R 3; 32 ÷ 8 = 4.",
                "explanation": "672 ÷ 8 = 84 km per day."
            }
        ]
    },
    {
        "id": 15,
        "title": "Market Invoices",
        "tagline": "Vegetable Market • Record Keeping & Unit Rate Calculation",
        "lecture": (
            "At a bustling rural sabzi mandi or agricultural produce market, farmers sell harvested vegetables in bulk crates and maintain transparent accounting ledgers. The fundamental business formula governing every authentic commercial invoice connects three key quantities: Total Cost equals Rate per Kilogram multiplied by Quantity in Kilograms. Whenever a column in the ledger is missing, division provides the exact missing value! If a vegetable vendor sells seventy-two kilograms of fresh farm potatoes for one thousand four hundred and forty rupees, what was the rate per kilogram? Dividing one thousand four hundred and forty by seventy-two yields twenty rupees per kilogram. Conversely, if a restaurant chef spends eight hundred and seventy-five rupees on fresh green peas sold at thirty-five rupees per kilogram, how many kilograms of green peas did the chef purchase? We divide eight hundred and seventy-five by thirty-five. By estimating eighty-seven divided by thirty-five, which gives two with a remainder of seventeen, and bringing down five to make one hundred and seventy-five, thirty-five times five is one hundred and seventy-five. The chef bought exactly twenty-five kilograms of green peas! Every farmer checks their records carefully to prevent accounting errors and maintain honest trade across markets. Auditing farm invoice tables builds practical financial literacy and sharpens everyday mental arithmetic."
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>🥦</span> Sabzi Mandi Sales Ledger
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    Use division to find missing rates or quantities: Rate = Total ÷ Quantity:
                </p>
                <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700/80 font-mono text-xs space-y-2">
                    <div class="grid grid-cols-4 text-slate-400 border-b border-slate-700 pb-1 text-[11px]">
                        <span>ITEM</span>
                        <span class="text-right">WEIGHT</span>
                        <span class="text-right">RATE/KG</span>
                        <span class="text-right">TOTAL</span>
                    </div>
                    <div class="grid grid-cols-4 text-slate-200 py-1">
                        <span>🥔 Potato</span>
                        <span class="text-right">72 kg</span>
                        <span class="text-right text-cyan-300 font-bold">₹20</span>
                        <span class="text-right">₹1,440</span>
                    </div>
                    <div class="grid grid-cols-4 text-slate-200 py-1 border-b border-slate-700">
                        <span>🌱 Green Peas</span>
                        <span class="text-right text-cyan-300 font-bold">25 kg</span>
                        <span class="text-right">₹35</span>
                        <span class="text-right">₹875</span>
                    </div>
                    <div class="flex justify-between pt-1 text-emerald-400 font-black text-xs">
                        <span>Combined Sales:</span>
                        <span>₹2,315</span>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>📐</span> The Commercial Invoice Formulas
                    </h4>
                    <div class="space-y-2 text-xs">
                        <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60">
                            <span class="font-bold text-amber-300">To Find Rate per Kilogram:</span>
                            <div class="font-mono text-cyan-300 mt-0.5">Rate = Total Cost ÷ Weight (kg)</div>
                        </div>
                        <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60">
                            <span class="font-bold text-amber-300">To Find Weight Purchased:</span>
                            <div class="font-mono text-cyan-300 mt-0.5">Weight (kg) = Total Cost ÷ Rate per kg</div>
                        </div>
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-800/40 text-[11px] text-emerald-200 mt-3">
                    💡 <strong>Verification:</strong> Rate × Quantity MUST equal Total Amount on every authentic grocery invoice!
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c15_1",
                "question": "A vegetable vendor sells 48 kg of cabbages and earns ₹1,200. What was the unit price per kilogram of cabbage?",
                "options": [
                    "₹25 / kg",
                    "₹24 / kg",
                    "₹20 / kg",
                    "₹30 / kg"
                ],
                "answer": 0,
                "hint": "Divide ₹1,200 by 48 kg: 1,200 ÷ 48.",
                "explanation": "Rate per kg = Total ÷ Weight = 1,200 ÷ 48 = ₹25 per kg."
            },
            {
                "id": "c15_2",
                "question": "Radishes are priced at ₹18 per kg. If a hotel chef spends ₹648 on radishes, how many kilograms were bought?",
                "options": [
                    "36 kg",
                    "34 kg",
                    "38 kg",
                    "32 kg"
                ],
                "answer": 0,
                "hint": "Divide ₹648 by 18: 64 ÷ 18 = 3 R 10; 108 ÷ 18 = 6.",
                "explanation": "Weight = 648 ÷ 18 = 36 kg."
            }
        ]
    },
    {
        "id": 16,
        "title": "Mathematical Truth",
        "tagline": "Mathematical Statements • Equality Balance & Truth Value Classification",
        "lecture": (
            "In mathematics, an equation represents an exact and unyielding balance of numerical values across the equal sign. The equal sign does not simply mean calculate the answer; it acts as a balanced weighing beam declaring that the total value on the left-hand side is identically equal to the value on the right-hand side. Consider the statement: eight multiplied by nine equals seventy plus two. Let us evaluate both sides independently: eight times nine is seventy-two. On the right side, seventy plus two is also seventy-two. Because seventy-two equals seventy-two, the statement is declared mathematically True! Beyond simple arithmetic equations, mathematicians classify general mathematical statements into three categories: Always True, Sometimes True, and Never True. For example, the statement: dividing an even number by two produces an exact integer with zero remainder is Always True, because that is the very definition of an even number! In contrast, the statement: dividing an even number by two produces an odd number is Sometimes True—for instance, six divided by two is three, which is odd, but eight divided by two is four, which is even. Testing open equations and discovering single counterexamples enables mathematicians to establish universal truth across geometry and arithmetic. Rigorous evaluation of truth values develops sharp critical thinking."
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>⚖️</span> Equation Equality Balance
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    Evaluate both sides independently to verify mathematical truth:
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/80 font-mono text-xs space-y-2">
                    <div class="text-center font-bold text-amber-300 text-sm">8 × 9 = 70 + 2</div>
                    <div class="flex justify-between text-slate-300 border-t border-slate-700 pt-1">
                        <span>Left Side (LHS):</span>
                        <span class="text-cyan-300 font-bold">8 × 9 = 72</span>
                    </div>
                    <div class="flex justify-between text-slate-300">
                        <span>Right Side (RHS):</span>
                        <span class="text-cyan-300 font-bold">70 + 2 = 72</span>
                    </div>
                    <div class="flex justify-between border-t border-slate-700 pt-1 text-emerald-400 font-black text-sm">
                        <span>Verdict: LHS = RHS</span>
                        <span>✅ TRUE STATEMENT</span>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>🧭</span> Truth Value Classification
                    </h4>
                    <div class="space-y-1.5 text-xs">
                        <div class="p-2 rounded-lg bg-emerald-950/40 border border-emerald-800/40">
                            <span class="font-bold text-emerald-300">Always True:</span>
                            <div class="text-slate-300 text-[11px]">"Any even number divided by 2 leaves remainder 0."</div>
                        </div>
                        <div class="p-2 rounded-lg bg-amber-950/40 border border-amber-800/40">
                            <span class="font-bold text-amber-300">Sometimes True:</span>
                            <div class="text-slate-300 text-[11px]">"Dividing an even number by 2 gives an odd quotient." (6÷2=3 Odd, but 8÷2=4 Even!)</div>
                        </div>
                        <div class="p-2 rounded-lg bg-rose-950/40 border border-rose-800/40">
                            <span class="font-bold text-rose-300">Never True:</span>
                            <div class="text-slate-300 text-[11px]">"A remainder can be strictly greater than its divisor." (Defies division law!)</div>
                        </div>
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-indigo-950/40 border border-indigo-800/40 text-[11px] text-indigo-200 mt-3">
                    💡 <strong>Counterexample Rule:</strong> To prove a statement is NOT always true, you only need to discover a single counterexample!
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c16_1",
                "question": "Which of the following equations represents a TRUE mathematical statement?",
                "options": [
                    "6 × 7 = 40 + 2",
                    "9 × 4 = 30 + 5",
                    "8 × 8 = 60 + 5",
                    "7 × 5 = 40 - 2"
                ],
                "answer": 0,
                "hint": "Calculate 6 × 7 and compare with 40 + 2.",
                "explanation": "6 × 7 = 42, and 40 + 2 = 42. Since 42 = 42, it is a True statement. In B, 36 ≠ 35. In C, 64 ≠ 65. In D, 35 ≠ 38."
            },
            {
                "id": "c16_2",
                "question": "Classify the statement: 'When a number ending in 0 is divided by 5, the remainder is 0.'",
                "options": [
                    "Always True",
                    "Sometimes True",
                    "Never True",
                    "Cannot be determined"
                ],
                "answer": 0,
                "hint": "Think of multiples of 5: 5, 10, 15, 20, 25, 30. Any number ending in 0 is a multiple of 10, hence divisible by 5.",
                "explanation": "Every number ending in 0 is divisible by 10, and since 10 is a multiple of 5, every number ending in 0 is always exactly divisible by 5 with remainder 0. It is Always True."
            }
        ]
    }
]
