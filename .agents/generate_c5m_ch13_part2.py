# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 13: Animal Jumps - Part 2 (Slides 9 to 16)
Syllabus: Joyful Mathematics (NEP 2020)
Strict Constraints:
- 195 to 215 words per lecture
- Short headings (1-3 words)
- Indian male teacher tone
- Zero human names
- Zero raw LaTeX
- 2 checkpoints per slide
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Jungle Number Trail",
        "tagline": "Exploration Trail • Stepping Through Multiples of 2, 3, 5, and 10 in the Dense Forest",
        "lecture": (
            "Deep within a dense tropical forest, an inquisitive young wildlife explorer follows an ancient stepping-stone trail numbered from "
            "zero to fifty-nine to visit various friendly animal habitats. Depending on the exact size of the steps taken, the explorer lands "
            "on distinct subsets of numbered stones along the lush forest path! When taking steady two-step jumps, the explorer touches "
            "stones four, twelve, fourteen, and fifty. Because two divides every single one of these numbers with zero remainder, the number "
            "two is a true common factor of all four locations! Next, when the explorer switches to taking brisk three-step jumps, the path "
            "touches stones nine, twenty-one, thirty-nine, and fifty-seven. Here, three divides each position completely, proving that three "
            "is a common factor of this new set of locations! What happens when the explorer takes five-step jumps? Every stone touched—such "
            "as fifteen, twenty-five, thirty-five, and fifty—ends in either five or zero! And when leaping in ten-step bounds, every single "
            "stone ends in zero: ten, twenty, thirty, forty, and fifty. This lively jungle expedition reveals that stepping intervals correspond "
            "directly to mathematical division factors. Stepping stones shared by both two-step and five-step paths—like ten, twenty, thirty, "
            "and fifty—demonstrate numbers divisible by both factors simultaneously."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-emerald-900/40 via-teal-900/30 to-emerald-900/40 border border-emerald-500/30 rounded-xl p-4">
        <h4 class="text-emerald-300 font-bold text-sm tracking-wider uppercase mb-1">Jungle Trail Divisibility Stones</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Taking jumps of size <span class="text-amber-300 font-bold">K</span> touches all stones that have
            <span class="text-cyan-300 font-semibold">K as a factor</span>.
        </p>
    </div>
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs font-mono">
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-amber-400 font-bold block">2-Step Jumps</span>
            <span class="text-slate-300 text-[11px] block mt-1">4, 12, 14, 50</span>
            <span class="text-emerald-400 text-[10px] block">Common Factor: 2</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-cyan-400 font-bold block">3-Step Jumps</span>
            <span class="text-slate-300 text-[11px] block mt-1">9, 21, 39, 57</span>
            <span class="text-emerald-400 text-[10px] block">Common Factor: 3</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-purple-400 font-bold block">5-Step Jumps</span>
            <span class="text-slate-300 text-[11px] block mt-1">15, 25, 35, 50</span>
            <span class="text-emerald-400 text-[10px] block">Ends in 5 or 0</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-pink-400 font-bold block">10-Step Jumps</span>
            <span class="text-slate-300 text-[11px] block mt-1">10, 20, 30, 50</span>
            <span class="text-emerald-400 text-[10px] block">Ends in 0 (2 & 5!)</span>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "Which of the following numbers is touched by BOTH 2-step jumps and 5-step jumps?",
                "options": ["14", "25", "30", "39"],
                "answer": 2,
                "explanation": "30 is divisible by both 2 (30 ÷ 2 = 15) and 5 (30 ÷ 5 = 6).",
                "hint": "Look for an even number that ends in 0."
            },
            {
                "question": "Why is 3 a common factor of the numbers 9, 21, 39, and 57?",
                "options": [
                    "They are all prime numbers",
                    "3 divides each of them without leaving a remainder",
                    "They all end in the digit 7",
                    "They are all multiples of 9"
                ],
                "answer": 1,
                "explanation": "A common factor divides every number in the set completely with zero remainder.",
                "hint": "Recall the definition of a factor."
            }
        ]
    },
    {
        "id": 10,
        "title": "Common Factors",
        "tagline": "Formal Definition • Identifying Shared Divisors That Completely Divide Multiple Numbers",
        "lecture": (
            "Having explored factors through geometric arrays and numbered trails, we now formalize one of the most critical concepts in "
            "arithmetic: the common factor! By definition, a common factor is a whole number that divides two or more given numbers completely "
            "without leaving any remainder whatsoever. To find the common factors of two numbers, we simply list all the factors of each "
            "number individually and look for numbers that appear in both lists! For example, let us consider the pair eight and twelve. "
            "First, what are all the factors of eight? One, two, four, and eight divide eight completely. Next, what are all the factors of "
            "twelve? One, two, three, four, six, and twelve divide twelve completely. Now compare the two sets: which numbers belong to both? "
            "The numbers one, two, and four appear in both factor lists! Therefore, one, two, and four are the common factors of eight and twelve. "
            "Among these shared factors, the number four is the largest, which mathematicians designate as the highest common factor or HCF. "
            "Notice that the number one is a universal factor: because one divides every whole number without remainder, one is always a common "
            "factor of any two numbers in existence!"
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-blue-900/40 via-indigo-900/30 to-blue-900/40 border border-blue-500/30 rounded-xl p-4">
        <h4 class="text-blue-300 font-bold text-sm tracking-wider uppercase mb-1">Common Factor Definition</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            A <span class="text-amber-300 font-bold">Common Factor</span> of two numbers is any integer that divides
            <span class="text-cyan-300 font-semibold">both numbers completely (Remainder = 0)</span>.
        </p>
    </div>
    <div class="space-y-2 font-mono text-xs">
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700 flex justify-between items-center">
            <span class="text-amber-400 font-bold">Factors of 8:</span>
            <span class="text-slate-200">{<strong class="text-emerald-400">1</strong>, <strong class="text-emerald-400">2</strong>, <strong class="text-emerald-400">4</strong>, 8}</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700 flex justify-between items-center">
            <span class="text-cyan-400 font-bold">Factors of 12:</span>
            <span class="text-slate-200">{<strong class="text-emerald-400">1</strong>, <strong class="text-emerald-400">2</strong>, 3, <strong class="text-emerald-400">4</strong>, 6, 12}</span>
        </div>
        <div class="bg-slate-900/90 p-2.5 rounded-lg border border-emerald-500/30 text-center text-emerald-300">
            ★ Common Factors: <strong>{1, 2, 4}</strong> • Highest Common Factor (HCF): <strong>4</strong>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "What are all the common factors of 8 and 12?",
                "options": ["1, 2", "1, 2, 4", "2, 4, 8", "1, 2, 3, 4"],
                "answer": 1,
                "explanation": "Factors of 8 are {1, 2, 4, 8}. Factors of 12 are {1, 2, 3, 4, 6, 12}. Common factors are 1, 2, and 4.",
                "hint": "Check which numbers divide both 8 and 12 without a remainder."
            },
            {
                "question": "What number is always a common factor of ANY two whole numbers?",
                "options": ["0", "1", "2", "10"],
                "answer": 1,
                "explanation": "1 divides every non-zero whole number completely, so 1 is always a common factor.",
                "hint": "Think about the universal divisor that divides everything."
            }
        ]
    },
    {
        "id": 11,
        "title": "Common Factors Pairs",
        "tagline": "Specific Pair Analysis • Comparing 24 & 36 and Consecutive Number Relationships",
        "lecture": (
            "Let us apply our common factor method to larger composite numbers and discover an intriguing mathematical theorem regarding "
            "consecutive numbers! Consider finding all common factors of twenty-four and thirty-six. Let us list all factors of twenty-four: "
            "one, two, three, four, six, eight, twelve, and twenty-four. Now let us list all factors of thirty-six: one, two, three, four, "
            "six, nine, twelve, eighteen, and thirty-six. Comparing both lists carefully, we find an impressive collection of shared divisors: "
            "one, two, three, four, six, and twelve! Both twenty-four and thirty-six share six distinct common factors, with twelve serving "
            "as their highest common factor. Now, let us examine an entirely different pair: twelve and thirteen! Notice that twelve and "
            "thirteen are consecutive numbers—they sit right next to each other on the continuous number line. Factors of twelve are one, "
            "two, three, four, six, and twelve. Factors of thirteen are simply one and thirteen. What is their only common factor? Exactly "
            "the number one! This illustrates a universal mathematical truth: any two consecutive whole numbers share only one as a common "
            "factor. Because no whole number greater than one can divide two numbers that differ by only one, consecutive numbers are always co-prime."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-purple-900/40 via-indigo-900/30 to-purple-900/40 border border-purple-500/30 rounded-xl p-4">
        <h4 class="text-purple-300 font-bold text-sm tracking-wider uppercase mb-1">Consecutive Numbers Co-Prime Property</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Any two <span class="text-amber-300 font-bold">consecutive whole numbers (N and N+1)</span> have
            <span class="text-emerald-400 font-semibold">only 1 as their common factor</span>!
        </p>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs font-mono">
        <div class="bg-slate-800/80 p-3 rounded-lg border border-slate-700">
            <span class="text-cyan-400 font-bold block mb-1">Pair: 24 & 36</span>
            <span class="text-slate-300 block text-[11px]">Factors of 24: {1,2,3,4,6,8,12,24}</span>
            <span class="text-slate-300 block text-[11px]">Factors of 36: {1,2,3,4,6,9,12,18,36}</span>
            <span class="text-emerald-400 font-bold block mt-1">Common: {1, 2, 3, 4, 6, 12}</span>
        </div>
        <div class="bg-slate-800/80 p-3 rounded-lg border border-slate-700">
            <span class="text-amber-400 font-bold block mb-1">Pair: 12 & 13 (Consecutive)</span>
            <span class="text-slate-300 block text-[11px]">Factors of 12: {1, 2, 3, 4, 6, 12}</span>
            <span class="text-slate-300 block text-[11px]">Factors of 13: {1, 13}</span>
            <span class="text-emerald-400 font-bold block mt-1">Common: {1} only!</span>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "What is the highest common factor (HCF) of 24 and 36?",
                "options": ["4", "6", "12", "18"],
                "answer": 2,
                "explanation": "Common factors of 24 and 36 are 1, 2, 3, 4, 6, 12. The highest is 12.",
                "hint": "Find the largest number that divides both 24 and 36 evenly."
            },
            {
                "question": "What is the common factor of any two consecutive numbers, such as 25 and 26?",
                "options": ["Only 1", "1 and 2", "1 and 5", "There are no common factors"],
                "answer": 0,
                "explanation": "Consecutive numbers differ by 1, so no number greater than 1 can divide both. Their only common factor is 1.",
                "hint": "Consecutive numbers are always co-prime."
            }
        ]
    },
    {
        "id": 12,
        "title": "Common Factors Practice",
        "tagline": "Systematic Drills • Computing Shared Divisors Across Diverse Mathematical Pairs",
        "lecture": (
            "Let us sharpen our analytical skills by working through a comprehensive common factor practice set covering a variety of diverse "
            "number pairs! First, consider twelve and sixteen: factors of twelve are one, two, three, four, six, and twelve. Factors of sixteen "
            "are one, two, four, eight, and sixteen. Their common factors are one, two, and four, with four standing proudly as their highest "
            "common factor. Next, consider the pair two and nine: factors of two are one and two; factors of nine are one, three, and nine. "
            "What do they share in common? Only the number one! Even though nine is a composite square number and two is a prime number, "
            "their only shared divisor is one. Now consider nine and twenty-one: factors of nine are one, three, and nine; factors of "
            "twenty-one are one, three, seven, and twenty-one. Their common factors are one and three, making three their highest common "
            "factor! Notice how systematic listing makes finding common factors completely foolproof. Always start by writing all factors "
            "in ascending order from one up to the number itself. Next, circle the matching entries. By comparing multiple pairs, students "
            "discover that some numbers share several factors, while others share only one, building deep intuition for fractions and number theory."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-teal-900/40 via-emerald-900/30 to-teal-900/40 border border-teal-500/30 rounded-xl p-4">
        <h4 class="text-teal-300 font-bold text-sm tracking-wider uppercase mb-1">Common Factor Drill Summary</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Systematically comparing factor pairs across prime, odd, and composite combinations:
        </p>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 text-xs font-mono">
        <div class="bg-slate-800/80 p-3 rounded-lg border border-slate-700">
            <span class="text-amber-300 font-bold block mb-1">Pair: 12 & 16</span>
            <span class="text-slate-400 text-[11px] block">12: {1,2,3,4,6,12}</span>
            <span class="text-slate-400 text-[11px] block">16: {1,2,4,8,16}</span>
            <span class="text-emerald-400 text-[11px] block mt-1">Common: {1, 2, 4}</span>
        </div>
        <div class="bg-slate-800/80 p-3 rounded-lg border border-slate-700">
            <span class="text-amber-300 font-bold block mb-1">Pair: 2 & 9</span>
            <span class="text-slate-400 text-[11px] block">2: {1, 2}</span>
            <span class="text-slate-400 text-[11px] block">9: {1, 3, 9}</span>
            <span class="text-emerald-400 text-[11px] block mt-1">Common: {1}</span>
        </div>
        <div class="bg-slate-800/80 p-3 rounded-lg border border-slate-700">
            <span class="text-amber-300 font-bold block mb-1">Pair: 9 & 21</span>
            <span class="text-slate-400 text-[11px] block">9: {1, 3, 9}</span>
            <span class="text-slate-400 text-[11px] block">21: {1, 3, 7, 21}</span>
            <span class="text-emerald-400 text-[11px] block mt-1">Common: {1, 3}</span>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "What are the common factors of 9 and 21?",
                "options": ["1 only", "1 and 3", "3 and 7", "1, 3, and 9"],
                "answer": 1,
                "explanation": "Factors of 9 are {1, 3, 9}. Factors of 21 are {1, 3, 7, 21}. The common factors are 1 and 3.",
                "hint": "Check which numbers divide both 9 and 21."
            },
            {
                "question": "What are the common factors of 2 and 9?",
                "options": ["1 only", "1 and 2", "1 and 3", "1, 2, 3, 9"],
                "answer": 0,
                "explanation": "Factors of 2 are {1, 2}. Factors of 9 are {1, 3, 9}. Their only shared factor is 1.",
                "hint": "2 is prime and does not divide 9."
            }
        ]
    },
    {
        "id": 13,
        "title": "Divisibility Logic Rules",
        "tagline": "Logical Reasoning • True or False Mathematical Properties of Factors and Multiples",
        "lecture": (
            "Mathematics is rightly celebrated for its ironclad logical rules! Let us examine five important statements about numbers and "
            "test whether each statement is true or false using rigorous mathematical reasoning and clear counterexamples. Statement one: "
            "'Factors of even numbers must always be even.' Is this true? No, this is completely false! For example, the number ten is an "
            "even number, but its factors include one and five, which are completely odd! Statement two: 'Multiples of odd numbers cannot "
            "be even.' Is this true? No, this is also false! Three times two equals six, which is even; multiples of odd numbers alternate "
            "regularly between odd and even products! Statement three: 'Factors of odd numbers cannot be even.' Is this true? Yes, this is "
            "absolutely true! If an odd number had an even factor, multiplying that even factor by any integer would produce an even number, "
            "which is mathematically impossible! Statement four: 'The only common factor of any two consecutive numbers is one.' Yes, this "
            "is true, as consecutive numbers differ by only one. Finally, statement five: 'Zero cannot be a factor of any whole number.' "
            "Yes, this is true because division by zero is mathematically undefined. Testing statements with counterexamples builds strong logical reasoning."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-amber-900/40 via-red-900/30 to-amber-900/40 border border-amber-500/30 rounded-xl p-4">
        <h4 class="text-amber-300 font-bold text-sm tracking-wider uppercase mb-1">True / False Property Matrix</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Rigorous mathematical verification through definitions and counterexamples:
        </p>
    </div>
    <div class="space-y-2 text-xs font-mono">
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700 flex justify-between items-center">
            <span class="text-slate-300">1. Factors of even numbers must be even:</span>
            <span class="text-rose-400 font-bold bg-rose-950/80 px-2 py-0.5 rounded border border-rose-500/30">FALSE (10 has 1, 5)</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700 flex justify-between items-center">
            <span class="text-slate-300">2. Multiples of odd numbers cannot be even:</span>
            <span class="text-rose-400 font-bold bg-rose-950/80 px-2 py-0.5 rounded border border-rose-500/30">FALSE (3 × 2 = 6)</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700 flex justify-between items-center">
            <span class="text-slate-300">3. Factors of odd numbers cannot be even:</span>
            <span class="text-emerald-400 font-bold bg-emerald-950/80 px-2 py-0.5 rounded border border-emerald-500/30">TRUE</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700 flex justify-between items-center">
            <span class="text-slate-300">4. Consecutive numbers share only factor 1:</span>
            <span class="text-emerald-400 font-bold bg-emerald-950/80 px-2 py-0.5 rounded border border-emerald-500/30">TRUE</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700 flex justify-between items-center">
            <span class="text-slate-300">5. 0 cannot be a factor of any number:</span>
            <span class="text-emerald-400 font-bold bg-emerald-950/80 px-2 py-0.5 rounded border border-emerald-500/30">TRUE (Undefined)</span>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "Can an odd number ever have an even factor?",
                "options": [
                    "Yes, always",
                    "Yes, if the number is large",
                    "No, never",
                    "Only if multiplied by zero"
                ],
                "answer": 2,
                "explanation": "If a number has an even factor, it must be divisible by 2 and therefore even. Odd numbers can never have even factors.",
                "hint": "Any multiple of an even number is always even."
            },
            {
                "question": "Why is '0 cannot be a factor of any number' a true statement?",
                "options": [
                    "0 is an odd number",
                    "Division by 0 is undefined in mathematics",
                    "0 is greater than 1",
                    "0 is a prime number"
                ],
                "answer": 1,
                "explanation": "A factor must divide a number completely, but division by zero is undefined.",
                "hint": "Think about what happens when you attempt to divide by zero."
            }
        ]
    },
    {
        "id": 14,
        "title": "Animal Story Problems",
        "tagline": "Jungle Dilemmas • Applying Multiples to Synchronize Hunting Days and Avoid Dens",
        "lecture": (
            "Let us venture back into the jungle to solve intriguing story challenges using multiples and factors! In a dense valley, "
            "a swift tiger hunts every three days, while a stealthy black panther hunts every five days. If both predators begin their hunting "
            "routines on day zero, on what future days will both predators hunt simultaneously? To find their shared hunting days, we find "
            "the common multiples of three and five. Multiples of three are three, six, nine, twelve, fifteen, eighteen... Multiples of five "
            "are five, ten, fifteen, twenty... Their very first shared hunting expedition occurs on day fifteen! All future shared hunting "
            "days occur every fifteen days: day thirty, day forty-five, and so on. Now consider a navigation puzzle: a woodland traveler "
            "wishes to visit Bear den at stone thirty, while avoiding Tiger lair at stone twenty-five! Which jump size should the traveler "
            "choose from tile zero: jumps of five or jumps of six? If the traveler leaps in fives, she lands on five, ten, fifteen, twenty, "
            "and twenty-five—landing straight inside Tiger lair! But if she leaps in sixes, she lands on six, twelve, eighteen, twenty-four, "
            "and thirty, reaching Bear safely while bypassing twenty-five completely!"
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-cyan-900/40 via-blue-900/30 to-cyan-900/40 border border-cyan-500/30 rounded-xl p-4">
        <h4 class="text-cyan-300 font-bold text-sm tracking-wider uppercase mb-1">Jungle Story Math Scenarios</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Synchronizing periodic cycles with LCM and avoiding dangerous tiles with strategic factor selection.
        </p>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs font-mono">
        <div class="bg-slate-800/80 p-3 rounded-lg border border-slate-700">
            <span class="text-amber-400 font-bold block mb-1">🐾 Shared Hunting Days</span>
            <span class="text-slate-300 block text-[11px]">Tiger: every 3 days</span>
            <span class="text-slate-300 block text-[11px]">Panther: every 5 days</span>
            <span class="text-emerald-400 font-bold block mt-1">LCM(3, 5) = 15 Days (15, 30, 45...)</span>
        </div>
        <div class="bg-slate-800/80 p-3 rounded-lg border border-slate-700">
            <span class="text-cyan-400 font-bold block mb-1">🐻 Visit Bear (30), Avoid Tiger (25)</span>
            <span class="text-slate-300 block text-[11px]">Step 5: hits 25 (Danger!)</span>
            <span class="text-slate-300 block text-[11px]">Step 6: {6, 12, 18, 24, 30} (Safe!)</span>
            <span class="text-emerald-400 font-bold block mt-1">Correct Jump Size = 6</span>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "On what day will the tiger (every 3 days) and panther (every 5 days) first hunt together?",
                "options": ["Day 8", "Day 10", "Day 15", "Day 30"],
                "answer": 2,
                "explanation": "The least common multiple of 3 and 5 is 15. They will first hunt together on Day 15.",
                "hint": "Find the smallest number divisible by both 3 and 5."
            },
            {
                "question": "Which jump size reaches tile 30 while avoiding tile 25?",
                "options": ["Step size 2", "Step size 5", "Step size 6", "Step size 10"],
                "answer": 2,
                "explanation": "Step 6 reaches 6, 12, 18, 24, 30 without touching 25. Step 5 and 10 touch 25 or miss 30.",
                "hint": "Find a factor of 30 that is NOT a factor of 25."
            }
        ]
    },
    {
        "id": 15,
        "title": "Divisibility Venn Diagram",
        "tagline": "Venn Classification • Sorting 16 Numbers by Divisibility with 2, 5, and 10",
        "lecture": (
            "To synthesize our comprehensive understanding of multiples and divisibility, let us examine an elegant classification puzzle "
            "using a Venn diagram with overlapping circular regions! We have a large pool of fifteen distinct numbers to categorize: ninety, "
            "twenty-two, thirty-eight, thirty, seventy-five, forty-five, sixty-six, seventy-eight, sixty-two, forty, eighty-four, fifty-six, "
            "twenty-five, ninety-five, and fifty-five. We sort them systematically based on whether they are divisible by two, by five, or "
            "by both two and five simultaneously! What happens when a number is divisible by two only? These are even numbers that do not end "
            "in zero, such as twenty-two, thirty-eight, sixty-six, seventy-eight, sixty-two, eighty-four, and fifty-six. What happens when a "
            "number is divisible by five only? These are odd numbers that end in five, such as seventy-five, forty-five, twenty-five, "
            "ninety-five, and fifty-five! Now, what belongs in the overlapping center region where both circles intersect? Numbers that are "
            "divisible by both two and five must end in zero! Because two times five equals ten, any number in this shared region is "
            "automatically divisible by ten as well: ninety, thirty, and forty. A number cannot be divisible by ten without being divisible "
            "by both two and five! Visual sorting diagrams provide instant clarity for recognizing multiple factor rules at a single glance."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-purple-900/40 via-indigo-900/30 to-purple-900/40 border border-purple-500/30 rounded-xl p-4">
        <h4 class="text-purple-300 font-bold text-sm tracking-wider uppercase mb-1">Divisibility Venn Diagram Regions</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            <span class="text-cyan-400 font-bold">Circle 2 (Even):</span> Ends in 0, 2, 4, 6, 8.<br>
            <span class="text-amber-400 font-bold">Circle 5 (Fives):</span> Ends in 0 or 5.<br>
            <span class="text-emerald-400 font-bold">Overlap (2 & 5 = 10):</span> Ends in 0!
        </p>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs font-mono">
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-cyan-400 font-bold block mb-1">Divisible by 2 Only:</span>
            <span class="text-slate-300 text-[11px]">22, 38, 62, 66, 78, 84, 56</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-amber-400 font-bold block mb-1">Divisible by 5 Only:</span>
            <span class="text-slate-300 text-[11px]">25, 45, 55, 75, 95</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-emerald-500/40 bg-emerald-950/40">
            <span class="text-emerald-400 font-bold block mb-1">Divisible by 2, 5 & 10:</span>
            <span class="text-slate-200 text-[11px] font-bold">30, 40, 90</span>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "Which of the following numbers belongs in the central overlap (divisible by 2, 5, and 10)?",
                "options": ["45", "78", "90", "95"],
                "answer": 2,
                "explanation": "90 ends in 0, which means it is divisible by 2 (90÷2=45), by 5 (90÷5=18), and by 10 (90÷10=9).",
                "hint": "Look for a number ending in 0."
            },
            {
                "question": "Why can NO number be divisible by 10 without being divisible by 2 and 5?",
                "options": [
                    "Because 10 is an odd number",
                    "Because 2 and 5 are factors of 10",
                    "Because 10 has no factors",
                    "Because 10 is a prime number"
                ],
                "answer": 1,
                "explanation": "Since 10 = 2 × 5, any multiple of 10 must also be a multiple of both 2 and 5.",
                "hint": "Think about the factors of 10."
            }
        ]
    },
    {
        "id": 16,
        "title": "Factors Multiples Summary",
        "tagline": "Grand Synthesis • Unifying Factor Arrays, Prime Foundations, and Common Multiples",
        "lecture": (
            "As we conclude our inspiring mathematical expedition through animal jumps, let us reflect upon the great unified principles "
            "of factors and multiples that we have mastered together! Every whole number can be expressed as a product of factors, geometrically "
            "represented by solid rectangular tile arrays. Numbers that form only a single straight-line rectangle are prime numbers, "
            "possessing exactly two factors: one and the number itself. Numbers that form multiple rectangular configurations are composite "
            "numbers, while the number one is uniquely neither prime nor composite. When animals leap along the continuous number line, "
            "their footsteps map out skip-counting sequences of multiples. Where their footprints coincide, we uncover common multiples! "
            "The very first shared stepping stone represents the least common multiple, synchronizing repeating cycles in sports, clocks, "
            "and nature. Conversely, when comparing the divisor sets of multiple numbers, we find common factors, with the largest being the "
            "highest common factor. Consecutive whole numbers always share only one as a common factor, making them fundamentally co-prime. "
            "By connecting physical animal jumps, geometric rectangle arrays, and divisibility logic, students possess an exceptionally versatile "
            "mathematical toolkit to uncover numerical harmony and solve complex arithmetic problems with boundless speed, joyful enthusiasm, and absolute accuracy."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-emerald-900/40 via-teal-900/30 to-emerald-900/40 border border-emerald-500/30 rounded-xl p-4">
        <h4 class="text-emerald-300 font-bold text-sm tracking-wider uppercase mb-1">Core Mathematical Synthesis</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            <span class="text-amber-300 font-bold">Factors:</span> Exact divisors (geometric rectangle dimensions).<br>
            <span class="text-cyan-300 font-bold">Multiples:</span> Products formed by scaling (number line jump landings).<br>
            <span class="text-purple-300 font-bold">Primes:</span> Exactly 2 factors (1 & itself). Smallest prime is 2.
        </p>
    </div>
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs font-mono">
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-amber-300 font-bold block">LCM</span>
            <span class="text-slate-300 text-[11px] block mt-1">Smallest shared multiple</span>
            <span class="text-emerald-400 text-[10px]">LCM(4, 6) = 12</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-cyan-300 font-bold block">HCF</span>
            <span class="text-slate-300 text-[11px] block mt-1">Largest shared factor</span>
            <span class="text-emerald-400 text-[10px]">HCF(24, 36) = 12</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-purple-300 font-bold block">Consecutive</span>
            <span class="text-slate-300 text-[11px] block mt-1">N & N+1</span>
            <span class="text-emerald-400 text-[10px]">HCF = 1 always</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-pink-300 font-bold block">Overlap (10)</span>
            <span class="text-slate-300 text-[11px] block mt-1">2 × 5 = 10</span>
            <span class="text-emerald-400 text-[10px]">Ends in 0</span>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "What is the key geometric difference between a prime number and a composite number in tile arrays?",
                "options": [
                    "Prime numbers form circular arrays",
                    "Prime numbers form only one straight-line rectangle (1 × N)",
                    "Composite numbers cannot form rectangles",
                    "Prime numbers form square arrays"
                ],
                "answer": 1,
                "explanation": "Because a prime number has only factors 1 and itself, it can only form a single 1 × N rectangular strip.",
                "hint": "Think about the factor pairs of a prime number."
            },
            {
                "question": "If two numbers are consecutive (like 19 and 20), what is their highest common factor (HCF)?",
                "options": ["1", "2", "19", "380"],
                "answer": 0,
                "explanation": "Any two consecutive whole numbers share only 1 as a common factor, so their HCF is 1.",
                "hint": "Consecutive numbers differ by only 1."
            }
        ]
    }
]

if __name__ == '__main__':
    for s in slides_part2:
        wc = len(s['lecture'].split())
        status = "PASS" if 195 <= wc <= 215 else f"FAIL ({wc})"
        print(f"Slide {s['id']}: {wc} words [{status}]")
