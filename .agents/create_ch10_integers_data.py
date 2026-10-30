import re
import json

CHAPTER_META = {
    "chapter_num": 10,
    "title": "The Other Side of Zero (Integers)",
    "subtitle": "Bela's Fun Elevator, Zero Pairs & Brahmagupta's Laws",
    "mentors": "Brahmagupta & Bela",
    "mentors_title": "Father of Zero & Negative Numbers and The Elevator Explorer",
    "class": "Class 6",
    "subject": "Mathematics",
    "curriculum": "NCERT Ganita Prakash (NEP 2020)"
}

# 20 Slides (16 Core Concept Slides with 32 Checkpoints + 4 Quiz Slides)
SLIDES = [
    {
        "id": 1,
        "badge": "Intro • Number Systems",
        "title": "Number Evolution",
        "subtitle": "From Counting Sheaves to the Infinite Two-Sided Line",
        "theory": """
            <p>Humanity began with natural counting numbers: 1, 2, 3, 4, ... to count animals, trees, and coins. Later, zero (0) arrived to represent an empty basket or the absence of items, giving us Whole Numbers (0, 1, 2, 3, ...).</p>
            <p class="mt-2">To share chikkis and measure fractional lengths, we created Fractions (1/2, 3/4, 2/5). These all rested on a one-directional <strong>Number Ray</strong> pointing to the right starting from 0.</p>
            <p class="mt-2">What lies to the left of zero? If you owe money, or dive beneath sea level, or take an elevator underground, we need numbers less than zero! Extending the ray symmetrically to the left completes the infinite, two-sided <strong>Number Line</strong>.</p>
        """,
        "summary": "Acharya Brahmagupta smiles: For centuries scholars stopped at zero. But just as an empty purse can turn into a debt, our numbers naturally extend into the mirror realm to the left of zero!",
        "checkpoints": [
            {
                "id": "1-1",
                "question": "Which of the following numbers lies to the left of 0 on the complete number line?",
                "options": ["+3", "0", "1/2", "−4"],
                "correct": 3,
                "explanation": "Negative numbers such as −4 are strictly less than 0 and lie to the left of 0 on the horizontal number line."
            },
            {
                "id": "1-2",
                "question": "How does the complete number line differ from the original whole number ray?",
                "options": [
                    "It extends infinitely in both directions (left and right of 0)",
                    "It only contains fractions",
                    "It stops at zero",
                    "It has no negative numbers"
                ],
                "correct": 0,
                "explanation": "A ray has an endpoint at 0 and goes right. The complete number line extends infinitely to the left (negative numbers) and to the right (positive numbers)."
            }
        ]
    },
    {
        "id": 2,
        "badge": "10.1 • Lift Analogy",
        "title": "The Fun Elevator",
        "subtitle": "Bela's Ice Cream Building Above and Below Ground",
        "theory": """
            <p>Welcome to Bela's multi-storied ice cream building! The ground floor, where visitors enter from the street, is labeled <strong>Floor 0</strong>.</p>
            <p class="mt-2">Floors above ground house delicious toppings and dining terraces: Floor 1, Floor 2, Floor 3, and so on. But the deep refrigeration freezers and secret chocolate vaults are underground!</p>
            <p class="mt-2">To reach the underground basements, the elevator buttons are marked with minus signs: Floor −1 (first basement), Floor −2 (second basement), and Floor −3 (deep freeze vault).</p>
        """,
        "summary": "Bela announces: Ding! Ground level is Floor 0. Every level above ground is positive (+), and every cool underground freezer is negative (−).",
        "checkpoints": [
            {
                "id": "2-1",
                "question": "In Bela's building, what floor represents the street ground entrance?",
                "options": ["Floor 1", "Floor 0", "Floor −1", "Floor 10"],
                "correct": 1,
                "explanation": "Floor 0 represents the street ground entrance, serving as the neutral reference baseline."
            },
            {
                "id": "2-2",
                "question": "If the ice cream freezer is 2 levels below the ground floor, which button must Bela press?",
                "options": ["+2", "0", "−2", "−1"],
                "correct": 2,
                "explanation": "Two levels below Floor 0 is Floor −2 (the second basement level)."
            }
        ]
    },
    {
        "id": 3,
        "badge": "10.1 • Definitions",
        "title": "Signs & Direction",
        "subtitle": "Positive (+), Negative (−), and the Neutral Origin Zero",
        "theory": """
            <p>Numbers with a plus sign (+) are called <strong>Positive Numbers</strong> (+1, +2, +3, ...). When writing positive numbers, the plus sign is often omitted (so 5 means +5).</p>
            <p class="mt-2">Numbers with a minus sign (−) are called <strong>Negative Numbers</strong> (−1, −2, −3, ...). The minus sign is mandatory!</p>
            <p class="mt-2"><strong>Zero (0)</strong> is neither positive nor negative. It acts as the grand mirror pivot and dividing origin between both realms.</p>
            <p class="mt-2">Together, all negative whole numbers, zero, and positive whole numbers form the set of <strong>Integers</strong>: {..., −3, −2, −1, 0, +1, +2, +3, ...}.</p>
        """,
        "summary": "Acharya Brahmagupta notes: Zero is neither wealth nor debt. It is the steady boundary that balances fortune (+) and obligation (−).",
        "checkpoints": [
            {
                "id": "3-1",
                "question": "Which statement about the integer 0 is true?",
                "options": [
                    "0 is positive",
                    "0 is negative",
                    "0 is neither positive nor negative",
                    "0 is smaller than all negative numbers"
                ],
                "correct": 2,
                "explanation": "Zero is the neutral origin; it is neither positive nor negative."
            },
            {
                "id": "3-2",
                "question": "Which of the following is an integer?",
                "options": ["−7", "2.5", "3/4", "√2"],
                "correct": 0,
                "explanation": "Integers consist of whole counting numbers, zero, and their negative counterparts. −7 is an integer."
            }
        ]
    },
    {
        "id": 4,
        "badge": "10.1 • Addition",
        "title": "Tracking Movement",
        "subtitle": "Starting Floor + Movement = Target Floor",
        "theory": """
            <p>When Bela rides the elevator, upward movement is represented by adding a positive integer, while downward movement is represented by adding a negative integer.</p>
            <p class="mt-2">The fundamental motion equation is:<br>
            <span class="text-amber-300 font-semibold">Starting Floor + Movement = Target Floor</span></p>
            <p class="mt-2">For instance, if Bela starts at Floor +2 and moves down 3 floors: (+2) + (−3) = −1. She lands on the first basement level!</p>
            <p class="mt-2">Similarly, starting at Floor −2 and moving up 5 floors: (−2) + (+5) = +3.</p>
        """,
        "summary": "Bela smiles: Up is positive, down is negative! Just add the movement to your starting floor to see exactly where the elevator doors open.",
        "checkpoints": [
            {
                "id": "4-1",
                "question": "If you start at Floor −1 and move up 4 floors, where do you arrive?",
                "options": ["Floor −5", "Floor +3", "Floor +4", "Floor +5"],
                "correct": 1,
                "explanation": "(−1) + (+4) = +3. Moving up 4 floors from basement 1 takes you to Floor 3."
            },
            {
                "id": "4-2",
                "question": "What is the result of (+3) + (−5)?",
                "options": ["+2", "−2", "+8", "−8"],
                "correct": 1,
                "explanation": "(+3) + (−5) = −2. Moving down 5 from +3 brings you to −2."
            }
        ]
    },
    {
        "id": 5,
        "badge": "10.1 • Additive Inverses",
        "title": "Additive Inverses",
        "subtitle": "Opposite Pairs that Cancel Exactly Back to Zero",
        "theory": """
            <p>What happens if Bela goes up 3 floors from the ground (+3) and then immediately goes down 3 floors (−3)?</p>
            <p class="mt-2 font-mono text-cyan-300">(+3) + (−3) = 0</p>
            <p class="mt-2">Two numbers whose sum is zero are called <strong>Additive Inverses</strong> (or opposites) of each other. For every positive integer +a, there exists an exact negative twin −a such that:<br>
            <span class="text-amber-300 font-bold">(+a) + (−a) = 0</span></p>
            <p class="mt-2">The additive inverse of +7 is −7. The additive inverse of −12 is +12. And the additive inverse of 0 is simply 0!</p>
        """,
        "summary": "Acharya Brahmagupta states: Equal fortune combined with equal debt yields empty hands: 0. Every positive integer possesses an exact negative cancelling twin.",
        "checkpoints": [
            {
                "id": "5-1",
                "question": "What is the additive inverse of −9?",
                "options": ["−9", "0", "+9", "1/9"],
                "correct": 2,
                "explanation": "The additive inverse of −9 is +9 because (−9) + (+9) = 0."
            },
            {
                "id": "5-2",
                "question": "What is (+15) + (−15)?",
                "options": ["+30", "−30", "0", "+1"],
                "correct": 2,
                "explanation": "Adding an integer and its additive inverse always equals 0."
            }
        ]
    },
    {
        "id": 6,
        "badge": "10.1 • Ordering",
        "title": "Comparing Depths",
        "subtitle": "Higher Floors Are Greater; Lower Floors Are Smaller",
        "theory": """
            <p>In Bela's tower, higher floors are physically higher up, and lower floors are deeper underground. In mathematics, this vertical ordering defines the inequality relationship:</p>
            <ul class="list-disc pl-5 mt-2 space-y-1 text-slate-300">
                <li>Any positive number is greater than 0: +5 > 0.</li>
                <li>Any negative number is smaller than 0: −3 < 0.</li>
                <li>Every positive number is greater than every negative number: +1 > −100!</li>
                <li>Between two negative numbers, the one deeper underground is smaller: −5 < −2.</li>
            </ul>
            <p class="mt-2">Think of temperature or depth: −10 °C is much colder (lower) than −2 °C!</p>
        """,
        "summary": "Bela remarks: Even though 100 sounds huge, Floor −100 is far down in the dark earth compared to Floor −1. Therefore, −100 < −1!",
        "checkpoints": [
            {
                "id": "6-1",
                "question": "Which of the following inequality statements is true?",
                "options": ["−8 > −3", "−8 < −3", "−8 = −3", "0 < −8"],
                "correct": 1,
                "explanation": "Floor −8 is deeper underground than Floor −3, so −8 < −3."
            },
            {
                "id": "6-2",
                "question": "Which integer is the largest among −15, −2, 0, and −20?",
                "options": ["−20", "−15", "−2", "0"],
                "correct": 3,
                "explanation": "Zero is greater than all negative numbers, so 0 is the largest."
            }
        ]
    },
    {
        "id": 7,
        "badge": "10.1 • Subtraction",
        "title": "Finding the Shift",
        "subtitle": "Target Floor − Starting Floor = Movement Needed",
        "theory": """
            <p>Instead of thinking of subtraction merely as 'taking away', integer subtraction asks: <em>'What movement is required to travel from a starting floor to a target floor?'</em></p>
            <p class="mt-2 font-mono text-cyan-300">Target Floor − Starting Floor = Movement Needed</p>
            <p class="mt-2">Suppose Bela is on Floor −2 and wants to reach Floor +3. What button must she press?<br>
            (+3) − (−2) = +5 (she must move UP 5 floors!).</p>
            <p class="mt-2">Suppose she is on Floor +4 and wants to reach Floor −1:<br>
            (−1) − (+4) = −5 (she must move DOWN 5 floors!).</p>
        """,
        "summary": "Acharya Brahmagupta explains: Subtraction measures the directed gap between two positions. From −2 up to +3 is a jump of +5!",
        "checkpoints": [
            {
                "id": "7-1",
                "question": "If you are at Floor +1 and wish to reach Floor −3, what movement is needed?",
                "options": ["+4 floors", "−4 floors", "+2 floors", "−2 floors"],
                "correct": 1,
                "explanation": "Target − Start = (−3) − (+1) = −4 floors (downward shift of 4 floors)."
            },
            {
                "id": "7-2",
                "question": "Calculate: (+2) − (−4)",
                "options": ["−2", "+2", "−6", "+6"],
                "correct": 3,
                "explanation": "(+2) − (−4) = (+2) + (+4) = +6."
            }
        ]
    },
    {
        "id": 8,
        "badge": "10.1 • Scale",
        "title": "Mine Shafts & Scales",
        "subtitle": "Venturing Hundreds of Meters Above and Below Ground",
        "theory": """
            <p>Real-world engineering uses integers to track massive vertical elevations. Consider an iron mine:</p>
            <ul class="list-disc pl-5 mt-2 space-y-1 text-slate-300">
                <li>Mountain look-out tower: +350 m above ground level.</li>
                <li>Ground processing plant: 0 m.</li>
                <li>Main mining shaft: −180 m underground.</li>
                <li>Deep drainage cavern: −450 m underground.</li>
            </ul>
            <p class="mt-2">The total vertical distance between the mountain tower (+350 m) and the deep drainage cavern (−450 m) is:<br>
            (+350) − (−450) = 350 + 450 = 800 meters!</p>
        """,
        "summary": "Bela marvels: When mining elevators plunge deep underground, negative numbers keep everyone safe by measuring exact depths below zero level.",
        "checkpoints": [
            {
                "id": "8-1",
                "question": "A miner descends from −50 m to −200 m. How much did the miner descend?",
                "options": ["50 m", "150 m", "200 m", "250 m"],
                "correct": 1,
                "explanation": "(−200) − (−50) = −150 m, which is a descent of 150 meters."
            },
            {
                "id": "8-2",
                "question": "What is the vertical distance between +120 m and −80 m?",
                "options": ["40 m", "80 m", "120 m", "200 m"],
                "correct": 3,
                "explanation": "Distance = 120 − (−80) = 120 + 80 = 200 meters."
            }
        ]
    },
    {
        "id": 9,
        "badge": "10.1 • Core Law",
        "title": "Double Negatives",
        "subtitle": "Subtracting a Negative Number is Adding a Positive",
        "theory": """
            <p>One of the most powerful laws in mathematics is:<br>
            <span class="text-amber-300 font-bold text-base">Subtracting a negative number is exactly equivalent to adding its positive twin!</span></p>
            <p class="mt-2 font-mono text-cyan-300">a − (−b) = a + b</p>
            <p class="mt-2">Why does this make total sense?</p>
            <ul class="list-disc pl-5 mt-2 space-y-1 text-slate-300">
                <li><strong>In Banking:</strong> If the bank removes (−) a debt of 500 rupees (−500) from your account, your wealth increases by +500!</li>
                <li><strong>In Bela's Lift:</strong> Finding the movement from −200 up to +2000 is (+2000) − (−200) = 2000 + 200 = +2200 floors up.</li>
                <li><strong>Taking away cold</strong> makes things warmer!</li>
            </ul>
        """,
        "summary": "Acharya Brahmagupta reveals: Removing a debt is identical to receiving a fortune! Two minuses acting together reverse direction into a positive leap.",
        "checkpoints": [
            {
                "id": "9-1",
                "question": "What is the value of (+8) − (−5)?",
                "options": ["+3", "−3", "+13", "−13"],
                "correct": 2,
                "explanation": "(+8) − (−5) = 8 + 5 = +13."
            },
            {
                "id": "9-2",
                "question": "If your account has −200 rupees and a penalty of −200 rupees is cancelled (subtracted), what is your new balance?",
                "options": ["−400", "0", "+200", "−200"],
                "correct": 1,
                "explanation": "(−200) − (−200) = −200 + 200 = 0 rupees."
            }
        ]
    },
    {
        "id": 10,
        "badge": "10.1 • Number Line",
        "title": "Horizontal Shift",
        "subtitle": "Rotating the Vertical Elevator 90° onto the Number Line",
        "theory": """
            <p>Take Bela's vertical elevator shaft and rotate it 90° counter-clockwise. What happens?</p>
            <ul class="list-disc pl-5 mt-2 space-y-1 text-slate-300">
                <li>The ground floor (0) becomes the central <strong>Origin (0)</strong>.</li>
                <li>Upward positive floors (+1, +2, +3, ...) swing into the <strong>Right side</strong>.</li>
                <li>Downward negative floors (−1, −2, −3, ...) swing into the <strong>Left side</strong>.</li>
            </ul>
            <p class="mt-2">Thus, walking <strong>Right</strong> means moving in the positive direction (adding positive or subtracting negative). Walking <strong>Left</strong> means moving in the negative direction (adding negative or subtracting positive).</p>
        """,
        "summary": "Bela exclaims: Look! Up becomes Right, and Down becomes Left! The vertical elevator and the horizontal number line are identical twin models.",
        "checkpoints": [
            {
                "id": "10-1",
                "question": "On a horizontal number line, which direction represents increasing value?",
                "options": ["Left", "Right", "Downwards", "Diagonal"],
                "correct": 1,
                "explanation": "Moving to the right increases value; numbers get larger as you move right."
            },
            {
                "id": "10-2",
                "question": "Starting at −2 on the number line, if you walk 5 units to the right, where do you land?",
                "options": ["−7", "+3", "+5", "+7"],
                "correct": 1,
                "explanation": "(−2) + 5 = +3. Walking 5 units right from −2 lands at +3."
            }
        ]
    },
    {
        "id": 11,
        "badge": "10.1 • Unmarked Line",
        "title": "The Unmarked Line",
        "subtitle": "Mental Arithmetic with Relative Distance Arcs",
        "theory": """
            <p>When working with large numbers like (+45) + (−70) or (−120) − (−150), drawing dozens of individual tick marks is impractical.</p>
            <p class="mt-2">Instead, mathematicians use an <strong>Unmarked Number Line</strong> with only 0 marked as an anchor.</p>
            <p class="mt-2">To solve (−35) + (+50):</p>
            <ol class="list-decimal pl-5 mt-1 space-y-1 text-slate-300">
                <li>Place −35 to the left of 0.</li>
                <li>Jump right by +35 to reach 0.</li>
                <li>You still have 50 − 35 = 15 left to jump to the right of 0.</li>
                <li>You land at +15!</li>
            </ol>
        """,
        "summary": "Acharya Brahmagupta approves: The unmarked line trains the mind to see relative magnitude. Zero is the bridge you cross when switching signs!",
        "checkpoints": [
            {
                "id": "11-1",
                "question": "Using zero as a bridge, what is (−40) + (+65)?",
                "options": ["−25", "+25", "+105", "−105"],
                "correct": 1,
                "explanation": "From −40, jumping right 40 reaches 0. The remaining jump is 65 − 40 = 25 right of 0, landing at +25."
            },
            {
                "id": "11-2",
                "question": "What is (+18) + (−30)?",
                "options": ["+12", "−12", "+48", "−48"],
                "correct": 1,
                "explanation": "From +18, jumping 18 left reaches 0. The remaining jump is 30 − 18 = 12 left of 0, landing at −12."
            }
        ]
    },
    {
        "id": 12,
        "badge": "10.2 • Tokens",
        "title": "The Token Model",
        "subtitle": "Green Positive (+), Red Negative (−), and Zero Pairs",
        "theory": """
            <p>Integers can be physically visualized using colored circular counters:</p>
            <div class="flex items-center space-x-4 my-2">
                <span class="px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 text-xs font-bold">+1 Token (Green)</span>
                <span class="px-3 py-1 rounded-full bg-rose-500/20 text-rose-300 border border-rose-500/30 text-xs font-bold">−1 Token (Red)</span>
            </div>
            <p class="mt-2">When one green token (+1) meets one red token (−1), they cancel each other out completely: <strong>(+1) + (−1) = 0</strong>. This pair is called a <strong>Zero Pair</strong>.</p>
            <p class="mt-2">To find (+4) + (−2): take 4 green tokens and 2 red tokens. Pair up 2 green with 2 red (they vanish as zero pairs). You are left with 2 green tokens: +2!</p>
        """,
        "summary": "Bela laughs: It is like matter and antimatter! One green token touches one red token and POOF — they vanish into zero!",
        "checkpoints": [
            {
                "id": "12-1",
                "question": "What is a zero pair in the token model?",
                "options": [
                    "Two green tokens",
                    "Two red tokens",
                    "One green token (+1) and one red token (−1)",
                    "A token with zero written on it"
                ],
                "correct": 2,
                "explanation": "A zero pair consists of one positive token (+1) and one negative token (−1) which sum to 0."
            },
            {
                "id": "12-2",
                "question": "If you have 5 red tokens (−5) and 3 green tokens (+3), what is the net value?",
                "options": ["−2", "+2", "−8", "+8"],
                "correct": 0,
                "explanation": "3 red and 3 green form zero pairs and vanish, leaving 2 red tokens: −2."
            }
        ]
    },
    {
        "id": 13,
        "badge": "10.2 • Zero Pairs",
        "title": "Token Subtraction",
        "subtitle": "Injecting Zero Pairs When Tokens Are Missing",
        "theory": """
            <p>How do you compute <span class="text-cyan-300 font-mono">(+2) − (−3)</span> using tokens? You have 2 green tokens, but you need to take away 3 red tokens — and there are no red tokens on the table!</p>
            <p class="mt-2">The brilliant secret: <strong>Add 3 Zero Pairs</strong> (3 green + 3 red). Since zero pairs equal 0, adding them does not change the total value of the set!</p>
            <ul class="list-disc pl-5 mt-2 space-y-1 text-slate-300">
                <li>Initial state: 2 green (+2).</li>
                <li>Add 3 zero pairs: Now you have (2 + 3 = 5 green) and 3 red. (Net value is still +2).</li>
                <li>Now take away the 3 red tokens!</li>
                <li>You are left with 5 green tokens: <strong>+5</strong>!</li>
            </ul>
        """,
        "summary": "Acharya Brahmagupta praises: Introducing zero pairs from the void changes nothing, yet unlocks everything. It proves visually why subtracting negative 3 adds positive 3!",
        "checkpoints": [
            {
                "id": "13-1",
                "question": "Why does adding zero pairs to a collection of tokens not change its overall value?",
                "options": [
                    "Because each zero pair equals 0, and adding 0 changes nothing",
                    "Because tokens change color",
                    "Because all tokens become positive",
                    "Because red tokens are heavier"
                ],
                "correct": 0,
                "explanation": "Each zero pair has net value (+1) + (−1) = 0. Adding 0 preserves the original sum."
            },
            {
                "id": "13-2",
                "question": "To compute (−3) − (+2) using tokens, what should you add to the 3 red tokens?",
                "options": [
                    "2 green tokens",
                    "2 zero pairs (2 green and 2 red)",
                    "3 red tokens",
                    "Nothing"
                ],
                "correct": 1,
                "explanation": "To take away 2 green tokens when none exist, introduce 2 zero pairs so you can remove the 2 green tokens, leaving 5 red tokens (−5)."
            }
        ]
    },
    {
        "id": 14,
        "badge": "10.3 • Real World",
        "title": "Real-World Balances",
        "subtitle": "Banking Ledgers, Sea Level Altitudes & Freezing Thermometers",
        "theory": """
            <p>Integers govern measurements in science, commerce, and geography every day:</p>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 my-3">
                <div class="p-2.5 rounded-xl bg-slate-800/80 border border-slate-700/60 text-xs">
                    <span class="font-bold text-amber-400 block mb-1">🏦 Finance</span>
                    Deposit / Credit = <strong>+₹</strong><br>
                    Withdrawal / Debt = <strong>−₹</strong>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-800/80 border border-slate-700/60 text-xs">
                    <span class="font-bold text-cyan-400 block mb-1">🌊 Geography</span>
                    Mt. Everest: <strong>+8848 m</strong><br>
                    Dead Sea: <strong>−430 m</strong>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-800/80 border border-slate-700/60 text-xs">
                    <span class="font-bold text-emerald-400 block mb-1">🌡️ Temperature</span>
                    Freezing point: <strong>0 °C</strong><br>
                    Siachen Glacier: <strong>−40 °C</strong>
                </div>
            </div>
            <p class="text-xs text-slate-300">If the temperature in Leh rises from −8 °C to +4 °C, the temperature increase is (+4) − (−8) = 12 °C!</p>
        """,
        "summary": "Bela notes: Look around! Whether checking your bank balance, reading a weather app in Kashmir, or measuring ocean depths, integers are everywhere.",
        "checkpoints": [
            {
                "id": "14-1",
                "question": "A merchant starts with a debt of ₹300 (−300) and earns a profit of ₹800 (+800). What is the merchant's net balance?",
                "options": ["−₹500", "+₹500", "+₹1100", "−₹1100"],
                "correct": 1,
                "explanation": "(−300) + (+800) = +₹500."
            },
            {
                "id": "14-2",
                "question": "The night temperature in Dras is −14 °C and daytime temperature is −2 °C. What was the rise in temperature?",
                "options": ["12 °C", "−12 °C", "16 °C", "−16 °C"],
                "correct": 0,
                "explanation": "(−2) − (−14) = −2 + 14 = 12 °C rise."
            }
        ]
    },
    {
        "id": 15,
        "badge": "10.4 • Puzzles",
        "title": "Magic Border Grids",
        "subtitle": "3×3 Hollow Boundary Grids & Matrix Sum Constants",
        "theory": """
            <p>Mathematicians love exploring integer symmetries! A <strong>Hollow 3×3 Grid</strong> consists of the 8 perimeter cells surrounding an empty center.</p>
            <p class="mt-2">Can we place positive and negative integers along the border so that the top row, bottom row, left column, and right column all add up to the exact same <strong>Border Sum</strong>?</p>
            <p class="mt-2">Because positive and negative numbers cancel each other, we can create astonishing grids where every line sums to 0, +6, or −4 by placing additive inverses in strategic corner and edge slots!</p>
        """,
        "summary": "Acharya Brahmagupta smiles: By balancing positive fortunes with negative debts across the perimeter, harmony is achieved in every direction.",
        "checkpoints": [
            {
                "id": "15-1",
                "question": "In a 3-cell line, if two cells contain +5 and −8, what must the third cell contain to make the sum 0?",
                "options": ["−3", "+3", "+13", "0"],
                "correct": 1,
                "explanation": "(+5) + (−8) = −3. To reach a sum of 0, the third cell must be +3."
            },
            {
                "id": "15-2",
                "question": "If all 4 sides of a hollow square have an identical line sum S, what happens if every number in the grid is replaced by its additive inverse?",
                "options": [
                    "The new line sum becomes −S",
                    "The line sum becomes 0",
                    "The line sum doubles",
                    "The grid breaks"
                ],
                "correct": 0,
                "explanation": "Replacing each integer with its additive inverse negates the total sum, making the new side sum −S."
            }
        ]
    },
    {
        "id": 16,
        "badge": "10.5 • History",
        "title": "Brahmagupta's Laws",
        "subtitle": "Brāhmasphuṭasiddhānta (628 CE) and Global Mathematical Heritage",
        "theory": """
            <p>In 628 CE, the legendary Indian astronomer-mathematician <strong>Acharya Brahmagupta</strong> composed the <em>Brāhmasphuṭasiddhānta</em>, writing the world's first complete, rigorous rules for negative numbers (ṛṇa - debt), positive numbers (dhana - fortune), and zero (kha):</p>
            <ul class="list-disc pl-5 mt-2 space-y-1 text-slate-300 text-xs sm:text-sm">
                <li><em>'The sum of two fortunes is a fortune; the sum of two debts is a debt.'</em> ((+a)+(+b)=+(a+b); (−a)+(−b)=−(a+b)).</li>
                <li><em>'The sum of a fortune and a debt is their difference.'</em></li>
                <li><em>'A debt subtracted from zero becomes a fortune.'</em> (0 − (−a) = +a).</li>
                <li><em>'A fortune subtracted from zero becomes a debt.'</em> (0 − (+a) = −a).</li>
            </ul>
            <p class="mt-2 text-xs text-slate-400">These profound Indian rules spread to Baghdad via Al-Khwarizmi, entered Europe centuries later through Fibonacci, and form the cornerstone of modern algebra today.</p>
        """,
        "summary": "Acharya Brahmagupta concludes: Over 1,400 years ago, we recognized that debt and fortune are symmetric reflections around zero. Mathematics embraces both sides of the mirror!",
        "checkpoints": [
            {
                "id": "16-1",
                "question": "What did Acharya Brahmagupta call negative numbers in 628 CE?",
                "options": ["Dhana (Fortune)", "Ṛṇa (Debt)", "Kha (Zero)", "Rūpa (Form)"],
                "correct": 1,
                "explanation": "Brahmagupta used the Sanskrit term ṛṇa (debt) for negative numbers and dhana (fortune) for positive numbers."
            },
            {
                "id": "16-2",
                "question": "According to Brahmagupta's rule, what is a debt subtracted from zero: 0 − (−x)?",
                "options": ["A debt (−x)", "A fortune (+x)", "Zero (0)", "Undefined"],
                "correct": 1,
                "explanation": "0 − (−x) = +x. A debt subtracted from zero becomes a fortune!"
            }
        ]
    },
    # Quiz Slides 17 to 20
    {
        "id": 17,
        "badge": "Quiz 1 • Fundamentals",
        "title": "Mastery Challenge I",
        "subtitle": "Questions 1 – 10: Definitions, Number Line & Basic Addition",
        "is_quiz": True,
        "quiz_range": [1, 10]
    },
    {
        "id": 18,
        "badge": "Quiz 2 • Motion & Signs",
        "title": "Mastery Challenge II",
        "subtitle": "Questions 11 – 20: Elevator Shifts, Inverses & Ordering",
        "is_quiz": True,
        "quiz_range": [11, 20]
    },
    {
        "id": 19,
        "badge": "Quiz 3 • Tokens & Rules",
        "title": "Mastery Challenge III",
        "subtitle": "Questions 21 – 30: Zero Pairs, Subtraction & Brahmagupta's Laws",
        "is_quiz": True,
        "quiz_range": [21, 30]
    },
    {
        "id": 20,
        "badge": "Quiz 4 • Advanced Mastery",
        "title": "Mastery Challenge IV",
        "subtitle": "Questions 31 – 40: Multi-Step Problems, Deep Real-World Scales & Grids",
        "is_quiz": True,
        "quiz_range": [31, 40]
    }
]

# 40 Comprehensive Mastery Quiz Questions (Zero raw LaTeX, clean Unicode)
QUIZ_QUESTIONS = [
    # Q1 - Q10 (Slide 17)
    {
        "id": 1,
        "question": "Which of the following numbers is an integer?",
        "options": ["−14", "+3.8", "5/8", "√7"],
        "correct": 0,
        "solution": "Integers consist of whole counting numbers, zero, and their negative counterparts. −14 is an integer, whereas 3.8 and 5/8 are non-integer decimals/fractions."
    },
    {
        "id": 2,
        "question": "Where does the integer −6 lie on a standard horizontal number line relative to 0?",
        "options": ["6 units to the right of 0", "6 units to the left of 0", "Directly at 0", "Above 0"],
        "correct": 1,
        "solution": "Negative integers lie strictly to the left of 0 on the horizontal number line. Thus, −6 is 6 units to the left of 0."
    },
    {
        "id": 3,
        "question": "What is the additive inverse of +24?",
        "options": ["+24", "0", "−24", "1/24"],
        "correct": 2,
        "solution": "The additive inverse of any number x is −x such that x + (−x) = 0. Therefore, the additive inverse of +24 is −24."
    },
    {
        "id": 4,
        "question": "Evaluate: (+7) + (−12)",
        "options": ["+5", "−5", "+19", "−19"],
        "correct": 1,
        "solution": "Starting at +7 and adding −12 means moving 12 units to the left: 7 − 12 = −5."
    },
    {
        "id": 5,
        "question": "Which of the following is true regarding zero?",
        "options": ["0 is a positive integer", "0 is a negative integer", "0 is neither positive nor negative", "0 is smaller than −10"],
        "correct": 2,
        "solution": "Zero is the neutral origin of the integer number line; it is neither positive nor negative."
    },
    {
        "id": 6,
        "question": "Which integer is smaller: −15 or −8?",
        "options": ["−15", "−8", "They are equal", "Cannot be determined"],
        "correct": 0,
        "solution": "On the number line, −15 lies further to the left than −8. In terms of depth or temperature, −15 is lower/colder than −8. Thus, −15 < −8."
    },
    {
        "id": 7,
        "question": "In Bela's elevator, if she starts at Floor −3 and goes up 7 floors, what floor does she reach?",
        "options": ["Floor −10", "Floor +4", "Floor +10", "Floor −4"],
        "correct": 1,
        "solution": "Starting Floor + Movement = Target Floor: (−3) + (+7) = +4. She arrives at Floor +4."
    },
    {
        "id": 8,
        "question": "What is the value of (−9) + (+9)?",
        "options": ["+18", "−18", "0", "+1"],
        "correct": 2,
        "solution": "Adding any integer to its additive inverse produces 0: (−9) + (+9) = 0."
    },
    {
        "id": 9,
        "question": "Which of the following numbers is the greatest?",
        "options": ["−25", "−2", "−100", "−1"],
        "correct": 3,
        "solution": "Among negative numbers, the one closest to 0 (furthest to the right) is the largest. −1 > −2 > −25 > −100."
    },
    {
        "id": 10,
        "question": "What is the result of (−4) + (−6)?",
        "options": ["+10", "−10", "+2", "−2"],
        "correct": 1,
        "solution": "Adding two negative numbers increases the total negative magnitude: (−4) + (−6) = −(4 + 6) = −10."
    },

    # Q11 - Q20 (Slide 18)
    {
        "id": 11,
        "question": "Evaluate: (+10) − (+15)",
        "options": ["+5", "−5", "+25", "−25"],
        "correct": 1,
        "solution": "(+10) − (+15) = 10 − 15 = −5."
    },
    {
        "id": 12,
        "question": "Calculate: (+6) − (−4)",
        "options": ["+2", "−2", "+10", "−10"],
        "correct": 2,
        "solution": "Subtracting a negative is equivalent to adding its positive: (+6) − (−4) = 6 + 4 = +10."
    },
    {
        "id": 13,
        "question": "Bela's elevator is on Floor +2. She needs to reach the ice cream vault on Floor −3. What movement is needed?",
        "options": ["+5 floors (up)", "−5 floors (down)", "+1 floor (up)", "−1 floor (down)"],
        "correct": 1,
        "solution": "Movement Needed = Target − Start = (−3) − (+2) = −5 floors. She must travel down 5 floors."
    },
    {
        "id": 14,
        "question": "Evaluate: (−8) − (−5)",
        "options": ["−13", "+13", "−3", "+3"],
        "correct": 2,
        "solution": "(−8) − (−5) = −8 + 5 = −3."
    },
    {
        "id": 15,
        "question": "Which integer is neither positive nor negative?",
        "options": ["−1", "+1", "0", "10"],
        "correct": 2,
        "solution": "Zero is the unique integer that is neither positive nor negative."
    },
    {
        "id": 16,
        "question": "What is the predecessor of −7 on the number line (the number immediately to its left)?",
        "options": ["−6", "−8", "+7", "0"],
        "correct": 1,
        "solution": "The predecessor of an integer n is n − 1. For −7: (−7) − 1 = −8."
    },
    {
        "id": 17,
        "question": "What is the successor of −10 on the number line (the number immediately to its right)?",
        "options": ["−11", "−9", "+10", "0"],
        "correct": 1,
        "solution": "The successor of an integer n is n + 1. For −10: (−10) + 1 = −9."
    },
    {
        "id": 18,
        "question": "Arrange in ascending order: −5, +3, 0, −8, +1",
        "options": [
            "−8, −5, 0, +1, +3",
            "+3, +1, 0, −5, −8",
            "0, +1, +3, −5, −8",
            "−5, −8, 0, +1, +3"
        ],
        "correct": 0,
        "solution": "From smallest (furthest left) to largest (furthest right): −8 < −5 < 0 < +1 < +3."
    },
    {
        "id": 19,
        "question": "Evaluate: 0 − (+18)",
        "options": ["+18", "−18", "0", "Undefined"],
        "correct": 1,
        "solution": "0 − (+18) = −18. Subtracting a positive fortune from zero leaves a debt."
    },
    {
        "id": 20,
        "question": "Evaluate: 0 − (−25)",
        "options": ["−25", "+25", "0", "+50"],
        "correct": 1,
        "solution": "0 − (−25) = 0 + 25 = +25. Subtracting a debt from zero produces a fortune!"
    },

    # Q21 - Q30 (Slide 19)
    {
        "id": 21,
        "question": "In the token model, what do 6 green tokens (+6) combined with 9 red tokens (−9) yield?",
        "options": ["+3", "−3", "+15", "−15"],
        "correct": 1,
        "solution": "6 green and 6 red form zero pairs and disappear. 3 red tokens remain, representing −3."
    },
    {
        "id": 22,
        "question": "To subtract (−4) from (+1) using tokens when you have only 1 green token, what step must you take?",
        "options": [
            "Add 4 zero pairs (4 green and 4 red), then take away the 4 red tokens",
            "Throw away the green token",
            "Turn the green token red",
            "Add 1 red token"
        ],
        "correct": 0,
        "solution": "Add 4 zero pairs to make 4 red tokens available. Then remove the 4 red tokens, leaving 1 + 4 = 5 green tokens (+5)."
    },
    {
        "id": 23,
        "question": "A submarine is at −120 m. It rises 45 m. What is its new depth?",
        "options": ["−165 m", "−75 m", "+75 m", "+165 m"],
        "correct": 1,
        "solution": "(−120) + (+45) = −75 m."
    },
    {
        "id": 24,
        "question": "The temperature in Srinagar dropped from +3 °C to −6 °C. What was the temperature change?",
        "options": ["A drop of 3 °C", "A drop of 9 °C", "A rise of 9 °C", "A drop of 6 °C"],
        "correct": 1,
        "solution": "Change = Final − Initial = (−6) − (+3) = −9 °C (a drop of 9 °C)."
    },
    {
        "id": 25,
        "question": "A bank account has a balance of −₹450 (overdrawn). The customer deposits ₹1,000. What is the new balance?",
        "options": ["+₹550", "−₹550", "+₹1,450", "−₹1,450"],
        "correct": 0,
        "solution": "(−450) + 1000 = +₹550."
    },
    {
        "id": 26,
        "question": "According to Acharya Brahmagupta's Brāhmasphuṭasiddhānta (628 CE), what is the sum of two debts?",
        "options": ["A fortune", "A debt", "Zero", "Positive infinity"],
        "correct": 1,
        "solution": "Brahmagupta stated: 'The sum of two debts is a debt.' Formally: (−a) + (−b) = −(a + b)."
    },
    {
        "id": 27,
        "question": "Evaluate: (−15) + (+8) + (−5)",
        "options": ["−12", "+12", "−28", "+28"],
        "correct": 0,
        "solution": "(−15) + (−5) = −20. Then (−20) + 8 = −12."
    },
    {
        "id": 28,
        "question": "Evaluate: (+30) − (−20) + (−15)",
        "options": ["−5", "+35", "+65", "+25"],
        "correct": 1,
        "solution": "(+30) − (−20) = 30 + 20 = 50. Then 50 + (−15) = 35."
    },
    {
        "id": 29,
        "question": "What is the distance on the number line between −9 and +7?",
        "options": ["2 units", "14 units", "16 units", "63 units"],
        "correct": 2,
        "solution": "Distance = (+7) − (−9) = 7 + 9 = 16 units."
    },
    {
        "id": 30,
        "question": "If x is a negative integer, what sign does −x have?",
        "options": ["Negative", "Positive", "Zero", "Cannot be determined"],
        "correct": 1,
        "solution": "The negative of a negative integer is positive: −(−k) = +k."
    },

    # Q31 - Q40 (Slide 20)
    {
        "id": 31,
        "question": "Evaluate the expression: (−12) − (+8) − (−20)",
        "options": ["0", "−40", "+40", "−16"],
        "correct": 0,
        "solution": "(−12) − (+8) = −20. Then (−20) − (−20) = −20 + 20 = 0."
    },
    {
        "id": 32,
        "question": "In a 3-cell puzzle line, the numbers are −7, x, and +11. If their sum is +2, what is x?",
        "options": ["−2", "+2", "+6", "−6"],
        "correct": 0,
        "solution": "(−7) + (+11) = +4. To have a sum of +2: 4 + x = 2, so x = 2 − 4 = −2."
    },
    {
        "id": 33,
        "question": "A bird flies at +40 m above sea level and a fish swims at −15 m below sea level. What is their vertical separation?",
        "options": ["25 m", "40 m", "55 m", "600 m"],
        "correct": 2,
        "solution": "Separation = (+40) − (−15) = 40 + 15 = 55 meters."
    },
    {
        "id": 34,
        "question": "Which of the following expressions equals −8?",
        "options": [
            "(−12) + (+4)",
            "(−5) − (−3)",
            "(+10) + (−18)",
            "Both A and C"
        ],
        "correct": 3,
        "solution": "(−12) + 4 = −8, and 10 + (−18) = −8. Both A and C evaluate to −8."
    },
    {
        "id": 35,
        "question": "What is the sum of all integers from −5 to +5 inclusive?",
        "options": ["0", "+5", "−5", "+15"],
        "correct": 0,
        "solution": "Each positive integer pairs with its additive inverse: (−5+5) + (−4+4) + (−3+3) + (−2+2) + (−1+1) + 0 = 0."
    },
    {
        "id": 36,
        "question": "In the Integers Snakes and Ladders game, Bela is on square −12. She rolls a +5 and then a −8. What is her new square?",
        "options": ["−15", "−9", "−25", "+1"],
        "correct": 0,
        "solution": "(−12) + (+5) = −7. Then (−7) + (−8) = −15."
    },
    {
        "id": 37,
        "question": "If a = −6 and b = −9, evaluate (a − b) − (b − a):",
        "options": ["0", "+6", "−6", "+18"],
        "correct": 1,
        "solution": "a − b = (−6) − (−9) = +3. b − a = (−9) − (−6) = −3. Then (a − b) − (b − a) = (+3) − (−3) = 3 + 3 = +6."
    },
    {
        "id": 38,
        "question": "A Roman emperor was born in 25 BCE (−25) and died in 40 CE (+40). How many years elapsed between his birth and death? (Assuming year 0 is counted mathematically)",
        "options": ["15 years", "25 years", "40 years", "65 years"],
        "correct": 3,
        "solution": "(+40) − (−25) = 40 + 25 = 65 years."
    },
    {
        "id": 39,
        "question": "Fill in the blank: (−18) + [___] = −30",
        "options": ["+12", "−12", "+48", "−48"],
        "correct": 1,
        "solution": "[___] = −30 − (−18) = −30 + 18 = −12."
    },
    {
        "id": 40,
        "question": "Which of the following statements is ALWAYS true for any two negative integers x and y?",
        "options": [
            "x + y is always negative",
            "x − y is always negative",
            "x + y is always positive",
            "x + y = 0"
        ],
        "correct": 0,
        "solution": "Adding two negative quantities always sums their magnitudes in the negative direction, so x + y is strictly negative."
    }
]

# Verify zero raw LaTeX and zero surrogates
raw_latex_pattern = re.compile(r'\\[a-zA-Z]+')

def verify_text(text, ctx):
    matches = raw_latex_pattern.findall(text)
    if matches:
        raise ValueError(f"Found raw LaTeX in {ctx}: {set(matches)}")
    surrogates = [c for c in text if 0xD800 <= ord(c) <= 0xDFFF]
    if surrogates:
        raise ValueError(f"Found surrogates in {ctx}")

verify_text(CHAPTER_META['title'], "CHAPTER_META title")
for s in SLIDES:
    verify_text(s['title'], f"Slide {s['id']} title")
    if 'theory' in s:
        verify_text(s['theory'], f"Slide {s['id']} theory")
    if 'summary' in s:
        verify_text(s['summary'], f"Slide {s['id']} summary")
    for cp in s.get('checkpoints', []):
        verify_text(cp['question'], f"Slide {s['id']} cp question")
        verify_text(cp['explanation'], f"Slide {s['id']} cp explanation")

for q in QUIZ_QUESTIONS:
    verify_text(q['question'], f"Quiz Q{q['id']} question")
    verify_text(q['solution'], f"Quiz Q{q['id']} solution")

print("VERIFIED PASS: Zero raw LaTeX and zero surrogates in all 20 Slides and 40 Quiz Questions!")

with open(".agents/class6_math_integers_data.py", "w", encoding="utf-8") as f:
    f.write('"""\nNCERT Class 6 Mathematics Chapter 10: The Other Side of Zero (Integers) Data Module\n"""\n\n')
    f.write('CHAPTER_META = ' + repr(CHAPTER_META) + '\n\n')
    f.write('SLIDES = ' + repr(SLIDES) + '\n\n')
    f.write('QUIZ_QUESTIONS = ' + repr(QUIZ_QUESTIONS) + '\n')

print("Successfully wrote .agents/class6_math_integers_data.py")
