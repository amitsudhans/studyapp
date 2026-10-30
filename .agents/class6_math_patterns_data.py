# -*- coding: utf-8 -*-
"""NCERT Class 6 Mathematics Chapter 1: Patterns in Mathematics Data Module."""

CHAPTER_META = {
    "chapter_num": 1,
    "title": "Patterns",
    "subtitle": "NCERT Class 6 Mathematics • Chapter 1 Interactive Master Laboratory",
    "mentors": "Acharya Virahānka & Srinivasa Ramanujan",
    "mentors_title": "Pioneers of Poetic Recursion, Number Theory & Mathematical Patterns",
    "badge": "Ganita Prakash • Foundations of Mathematics",
    "total_slides": 20,
    "checkpoints_count": 32,
    "quiz_questions_count": 40
}

SLIDES = [
    {
        "id": 1,
        "slide_num": 1,
        "title": "Patterns",
        "subtitle": "The Search for Patterns & Reasons",
        "badge": "Foundations",
        "summary": "What is mathematics really about? While many believe it is merely calculating with numbers, mathematicians define mathematics largely as the search for patterns and the explanation of why those patterns exist. Patterns surround us everywhere in nature, human culture, games, and modern science.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        When you look at the seeds spiraling outward in a sunflower head, the hexagonal tiles of a honeybee comb, the alternating stripes of a zebra, or the predictable rhythm of day and night, you are witnessing <strong class=\"text-amber-400\">patterns</strong>.\n    </p>\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3\">\n        <div class=\"p-3.5 rounded-xl bg-amber-950/40 border border-amber-500/30\">\n            <h4 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🔍</span> The Core Definition of Mathematics\n            </h4>\n            <p class=\"text-xs text-slate-300 leading-relaxed mb-2\">\n                <strong>Mathematics is the search for patterns, and the explanation of why they exist.</strong>\n            </p>\n            <ul class=\"text-xs text-slate-300 space-y-1 list-disc list-inside\">\n                <li><strong class=\"text-slate-100\">Spotting Patterns:</strong> Observing regularity, symmetry, or repeated structures in numbers, shapes, and events.</li>\n                <li><strong class=\"text-slate-100\">Seeking Reasons:</strong> Asking <em>\"Why does this always happen?\"</em> and finding logical proofs.</li>\n            </ul>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-cyan-950/40 border border-cyan-500/30\">\n            <h4 class=\"font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🎨</span> Both an Art and a Science\n            </h4>\n            <p class=\"text-xs text-slate-300 leading-relaxed mb-2\">\n                Mathematicians view mathematics as both an exact science and a beautiful, creative art.\n            </p>\n            <ul class=\"text-xs text-slate-300 space-y-1 list-disc list-inside\">\n                <li><strong class=\"text-slate-100\">Playful Creativity:</strong> Discovering patterns is fun, imaginative, and deeply satisfying.</li>\n                <li><strong class=\"text-slate-100\">Rigorous Science:</strong> Mathematical patterns remain universally true forever, regardless of time or location!</li>\n            </ul>\n        </div>\n    </div>\n    <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70 text-xs text-slate-300 space-y-1.5\">\n        <strong class=\"text-emerald-300 text-sm block\">🚀 Propelling Humanity Forward:</strong>\n        <p class=\"leading-relaxed\">\n            Understanding why patterns exist has driven human progress throughout history. Isaac Newton identified the mathematical pattern of falling apples and planetary orbits, creating the universal theory of gravitation. In modern biology, decoding repeating patterns in human DNA genomes allows scientists to cure genetic diseases and design life-saving medicines!\n        </p>\n    </div>\n</div>\n",
        "takeaways": [
            "Mathematics is fundamentally the search for patterns and the explanation of why those patterns hold true.",
            "Patterns exist everywhere around us in nature, art, technology, music, and daily life.",
            "Discovering and proving patterns propels human civilization forward, from space travel to genetic medicine."
        ],
        "checkpoints": [
            {
                "id": "cp1_1",
                "question": "How do modern mathematicians primarily define the discipline of mathematics?",
                "options": [
                    "A mechanical chore of doing boring arithmetic calculations",
                    "The search for patterns and the explanations for why those patterns exist",
                    "Memorizing multiplication tables up to 100",
                    "Only measuring the weight of heavy rocks"
                ],
                "correct": 1,
                "explanation": "Mathematics is defined largely as the exploration of patterns in numbers, shapes, and nature, and the logical reasoning explaining why those patterns occur."
            },
            {
                "id": "cp1_2",
                "question": "Which of the following is an example of a mathematical pattern propelling human scientific progress?",
                "options": [
                    "Discovering the gravitational orbit pattern to guide spacecraft to the Moon",
                    "Guessing answers on an exam without reading",
                    "Ignoring the laws of physics",
                    "Forgetting how to count"
                ],
                "correct": 0,
                "explanation": "Recognizing mathematical patterns in gravity enabled humanity to calculate orbital paths for satellites and Apollo spacecraft landing on the Moon."
            }
        ]
    },
    {
        "id": 2,
        "slide_num": 2,
        "title": "Patterns in Numbers",
        "subtitle": "Whole Numbers & Sequences",
        "badge": "Number Theory",
        "summary": "Numbers are among the most versatile tools invented by humanity. When we study patterns formed by whole numbers (0, 1, 2, 3, 4, ...), we enter the realm of Number Theory. An ordered list of numbers following a definite rule is called a number sequence.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Let us begin our exploration with the most familiar numbers of all: the <strong class=\"text-amber-400\">Whole Numbers</strong>.\n    </p>\n    <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70 space-y-2\">\n        <h4 class=\"font-bold text-amber-300 text-sm flex items-center gap-2\">\n            <span>🔢</span> Whole Numbers: {0, 1, 2, 3, 4, 5, ...}\n        </h4>\n        <p class=\"text-xs text-slate-300 leading-relaxed\">\n            The collection of whole numbers begins at 0 and extends onward infinitely: <code class=\"text-emerald-400 font-mono\">0, 1, 2, 3, 4, 5, ...</code>. The branch of mathematics devoted exclusively to discovering patterns, relationships, and symmetries in whole numbers is called <strong class=\"text-cyan-300\">Number Theory</strong> (often celebrated as the <em>'Queen of Mathematics'</em>).\n        </p>\n    </div>\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3 text-xs text-slate-300\">\n        <div class=\"p-3.5 rounded-xl bg-cyan-950/40 border border-cyan-500/30\">\n            <h5 class=\"font-bold text-cyan-300 text-xs mb-1.5 flex items-center gap-1.5\">\n                <span>📋</span> What is a Number Sequence?\n            </h5>\n            <p class=\"leading-relaxed mb-2\">\n                A <strong>number sequence</strong> is an ordered list of numbers that follows a specific, consistent mathematical rule.\n            </p>\n            <ul class=\"space-y-1 list-disc list-inside\">\n                <li>Each number in the sequence is called a <strong class=\"text-slate-100\">term</strong>.</li>\n                <li>The first number is the 1st term, followed by the 2nd term, 3rd term, and so on.</li>\n                <li>The three dots (<strong class=\"text-amber-400 font-mono font-bold\">...</strong>), called an <em>ellipsis</em>, indicate that the pattern continues forever!</li>\n            </ul>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70\">\n            <h5 class=\"font-bold text-emerald-300 text-xs mb-1.5 flex items-center gap-1.5\">\n                <span>💡</span> Rule-Finding Strategy\n            </h5>\n            <p class=\"leading-relaxed mb-1.5\">\n                To uncover the hidden rule of any number sequence, ask two questions:\n            </p>\n            <ol class=\"space-y-1 list-decimal list-inside\">\n                <li>What is the starting term?</li>\n                <li>How do I get from one term to the next term? (Adding a fixed number? Multiplying? Adding consecutive numbers?)</li>\n            </ol>\n        </div>\n    </div>\n</div>\n",
        "takeaways": [
            "Whole numbers start from 0 and go on forever: 0, 1, 2, 3, 4, ...",
            "Number Theory is the mathematical branch that explores patterns and properties of whole numbers.",
            "A number sequence is an ordered list of terms generated by a consistent mathematical rule."
        ],
        "checkpoints": [
            {
                "id": "cp2_1",
                "question": "What is the specialized branch of mathematics that studies patterns and secrets of whole numbers called?",
                "options": [
                    "Geometry",
                    "Number Theory",
                    "Astronomy",
                    "Trigonometry"
                ],
                "correct": 1,
                "explanation": "Number Theory is the branch of pure mathematics devoted specifically to the study of whole numbers and their patterns."
            },
            {
                "id": "cp2_2",
                "question": "What do the three dots (...) at the end of a sequence like 2, 4, 6, 8, ... signify?",
                "options": [
                    "The pattern has stopped and made a mistake",
                    "The sequence continues forever in the same established pattern (infinity)",
                    "Subtract 10 from the last number",
                    "Multiply the last number by zero"
                ],
                "correct": 1,
                "explanation": "An ellipsis (...) indicates that the sequence extends infinitely following the same rule."
            }
        ]
    },
    {
        "id": 3,
        "slide_num": 3,
        "title": "Fundamental Sequences",
        "subtitle": "Core Sequences & Rules",
        "badge": "Core Sequences",
        "summary": "Table 1 in our textbook presents fundamental number sequences that form the building blocks of mathematics: the constant All 1's sequence, the Natural Counting numbers (1, 2, 3, 4, ...), Even numbers (2, 4, 6, 8, ...), and Odd numbers (1, 3, 5, 7, ...). Each sequence exhibits distinct step differences and divisibility rules.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Let us examine the foundational sequences listed in <strong class=\"text-amber-400\">Table 1</strong> of the NCERT textbook.\n    </p>\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3 text-xs text-slate-300\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70\">\n            <div class=\"flex items-center gap-2 mb-1.5\">\n                <span class=\"w-2.5 h-2.5 rounded-full bg-slate-400\"></span>\n                <h5 class=\"font-bold text-slate-200 text-sm\">1. All 1's Sequence</h5>\n            </div>\n            <code class=\"text-amber-300 font-mono font-bold block mb-1\">1, 1, 1, 1, 1, 1, ...</code>\n            <p class=\"leading-relaxed\">\n                The simplest sequence possible. The difference between any two terms is 0. It serves as the steady baseline unit in mathematics.\n            </p>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70\">\n            <div class=\"flex items-center gap-2 mb-1.5\">\n                <span class=\"w-2.5 h-2.5 rounded-full bg-cyan-400\"></span>\n                <h5 class=\"font-bold text-cyan-300 text-sm\">2. Counting Numbers (Natural Numbers)</h5>\n            </div>\n            <code class=\"text-cyan-300 font-mono font-bold block mb-1\">1, 2, 3, 4, 5, 6, 7, ...</code>\n            <p class=\"leading-relaxed\">\n                Starts at 1, step rule: <strong class=\"text-emerald-400\">+1 each time</strong>. The n-th term is simply <strong class=\"text-slate-100 font-mono\">n</strong>. Used universally for tallying objects.\n            </p>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70\">\n            <div class=\"flex items-center gap-2 mb-1.5\">\n                <span class=\"w-2.5 h-2.5 rounded-full bg-emerald-400\"></span>\n                <h5 class=\"font-bold text-emerald-300 text-sm\">3. Even Numbers</h5>\n            </div>\n            <code class=\"text-emerald-300 font-mono font-bold block mb-1\">2, 4, 6, 8, 10, 12, ...</code>\n            <p class=\"leading-relaxed\">\n                Starts at 2, step rule: <strong class=\"text-emerald-400\">+2 each time</strong>. Formula for the n-th term = <strong class=\"text-slate-100 font-mono\">2 × n</strong>. Every even number can be split into two equal whole halves without any remainder!\n            </p>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70\">\n            <div class=\"flex items-center gap-2 mb-1.5\">\n                <span class=\"w-2.5 h-2.5 rounded-full bg-amber-400\"></span>\n                <h5 class=\"font-bold text-amber-300 text-sm\">4. Odd Numbers</h5>\n            </div>\n            <code class=\"text-amber-300 font-mono font-bold block mb-1\">1, 3, 5, 7, 9, 11, ...</code>\n            <p class=\"leading-relaxed\">\n                Starts at 1, step rule: <strong class=\"text-emerald-400\">+2 each time</strong>. Formula for the n-th term = <strong class=\"text-slate-100 font-mono\">2n − 1</strong>. When divided by 2, every odd number leaves an odd leftover remainder of 1!\n            </p>\n        </div>\n    </div>\n</div>\n",
        "takeaways": [
            "Counting numbers (natural numbers) increase by +1 each step: 1, 2, 3, 4, 5, ...",
            "Even numbers are multiples of 2 (2n) and can be grouped into exact pairs: 2, 4, 6, 8, ...",
            "Odd numbers increase by +2 starting at 1 (2n − 1), always leaving 1 leftover dot when paired."
        ],
        "checkpoints": [
            {
                "id": "cp3_1",
                "question": "What is the 10th term in the sequence of even numbers (2, 4, 6, 8, ...)?",
                "options": [
                    "18",
                    "20",
                    "22",
                    "10"
                ],
                "correct": 1,
                "explanation": "The n-th even number is given by 2 × n. For the 10th term, 2 × 10 = 20."
            },
            {
                "id": "cp3_2",
                "question": "What is the 7th term in the sequence of odd numbers (1, 3, 5, 7, 9, ...)?",
                "options": [
                    "11",
                    "13",
                    "15",
                    "17"
                ],
                "correct": 1,
                "explanation": "The n-th odd number is given by 2n − 1. For n = 7, (2 × 7) − 1 = 14 − 1 = 13."
            }
        ]
    },
    {
        "id": 4,
        "slide_num": 4,
        "title": "Triangular Numbers",
        "subtitle": "Triangular Dot Arrays",
        "badge": "Figurate Geometry",
        "summary": "Triangular numbers are numbers of dots that can be arranged in the shape of an equilateral triangle. Starting with 1, each successive triangular number is formed by adding a new bottom row containing one more dot than the previous row: 1, 3, 6, 10, 15, 21, 28, 36, ... The formula for the n-th triangular number is n(n+1)/2.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Ancient Greek and Indian mathematicians loved playing with pebbles on sand. When pebbles could be arranged into neat geometric shapes, they called them <strong class=\"text-amber-400\">Figurate Numbers</strong>!\n    </p>\n    <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70 space-y-2\">\n        <h4 class=\"font-bold text-amber-300 text-sm flex items-center gap-2\">\n            <span>🔺</span> Building Triangular Numbers Step-by-Step\n        </h4>\n        <div class=\"grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs font-mono text-center\">\n            <div class=\"p-2 rounded bg-slate-950 border border-slate-800\">\n                <span class=\"text-slate-400 block text-[10px]\">T₁: Row 1</span>\n                <span class=\"text-amber-300 text-sm font-bold\">1</span>\n            </div>\n            <div class=\"p-2 rounded bg-slate-950 border border-slate-800\">\n                <span class=\"text-slate-400 block text-[10px]\">T₂: 1 + 2</span>\n                <span class=\"text-amber-300 text-sm font-bold\">3</span>\n            </div>\n            <div class=\"p-2 rounded bg-slate-950 border border-slate-800\">\n                <span class=\"text-slate-400 block text-[10px]\">T₃: 1 + 2 + 3</span>\n                <span class=\"text-amber-300 text-sm font-bold\">6</span>\n            </div>\n            <div class=\"p-2 rounded bg-slate-950 border border-slate-800\">\n                <span class=\"text-slate-400 block text-[10px]\">T₄: 1 + 2 + 3 + 4</span>\n                <span class=\"text-amber-300 text-sm font-bold\">10</span>\n            </div>\n        </div>\n        <p class=\"text-xs text-slate-300 leading-relaxed mt-2\">\n            The sequence continues: <code class=\"text-emerald-400 font-mono font-bold\">1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...</code>\n        </p>\n    </div>\n    <div class=\"p-3.5 rounded-xl bg-gradient-to-r from-emerald-950/40 via-slate-900 to-cyan-950/40 border border-emerald-500/30 text-xs text-slate-300 space-y-1.5\">\n        <h5 class=\"font-bold text-emerald-300 text-xs flex items-center gap-1.5\">\n            <span>✨</span> Real-World Occurrences of Triangular Numbers\n        </h5>\n        <ul class=\"space-y-1 list-disc list-inside\">\n            <li><strong class=\"text-slate-100\">Ten-Pin Bowling:</strong> The 10 bowling pins at the end of an alley are arranged in an equilateral triangle of 4 rows: 1 + 2 + 3 + 4 = 10 (<code class=\"text-cyan-300 font-mono\">T₄</code>).</li>\n            <li><strong class=\"text-slate-100\">Billiard / Snooker Ball Rack:</strong> 15 pool balls are packed into a triangular wooden rack of 5 rows: 1 + 2 + 3 + 4 + 5 = 15 (<code class=\"text-cyan-300 font-mono\">T₅</code>).</li>\n        </ul>\n    </div>\n</div>\n",
        "takeaways": [
            "Triangular numbers represent dots that form equilateral triangles: 1, 3, 6, 10, 15, 21, 28, 36, ...",
            "The n-th triangular number equals the sum of the first n counting numbers: 1 + 2 + 3 + ... + n.",
            "Real-world arrangements include 10 bowling pins (T₄) and 15 billiard balls in a rack (T₅)."
        ],
        "checkpoints": [
            {
                "id": "cp4_1",
                "question": "What is the 5th triangular number (T₅)?",
                "options": [
                    "12",
                    "15",
                    "20",
                    "25"
                ],
                "correct": 1,
                "explanation": "T₅ = 1 + 2 + 3 + 4 + 5 = 15 dots."
            },
            {
                "id": "cp4_2",
                "question": "How many pins are arranged in a standard 4-row ten-pin bowling formation?",
                "options": [
                    "8 pins",
                    "10 pins (the 4th triangular number T₄)",
                    "12 pins",
                    "16 pins"
                ],
                "correct": 1,
                "explanation": "The 10 bowling pins form T₄: 1 pin in row 1, 2 in row 2, 3 in row 3, and 4 in row 4 (1 + 2 + 3 + 4 = 10)."
            }
        ]
    },
    {
        "id": 5,
        "slide_num": 5,
        "title": "Square Numbers",
        "subtitle": "Square Dot Arrays",
        "badge": "Square Numbers",
        "summary": "Square numbers are numbers that can be arranged in a square dot array with equal numbers of rows and columns. They are generated by multiplying a whole number by itself: n × n = n². The sequence is 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, ... Remarkably, the difference between consecutive square numbers produces the sequence of odd numbers!",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        When an arrangement of dots has an equal number of rows and columns, it forms a geometric square. The total count of dots in such an array is called a <strong class=\"text-amber-400\">Square Number</strong> (or <em>perfect square</em>).\n    </p>\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3 text-xs text-slate-300\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70\">\n            <h4 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>⬛</span> The Square Sequence\n            </h4>\n            <div class=\"space-y-1 font-mono text-cyan-300\">\n                <div>1² = 1 × 1 = <strong>1</strong></div>\n                <div>2² = 2 × 2 = <strong>4</strong></div>\n                <div>3² = 3 × 3 = <strong>9</strong></div>\n                <div>4² = 4 × 4 = <strong>16</strong></div>\n                <div>5² = 5 × 5 = <strong>25</strong></div>\n                <div>6² = 6 × 6 = <strong>36</strong></div>\n            </div>\n            <p class=\"text-slate-400 text-[11px] mt-2\">\n                Sequence: <code>1, 4, 9, 16, 25, 36, 49, 64, 81, 100, ...</code>\n            </p>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70\">\n            <h4 class=\"font-bold text-emerald-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🔎</span> A Stunning Difference Pattern!\n            </h4>\n            <p class=\"leading-relaxed mb-2\">\n                Subtract consecutive squares from one another:\n            </p>\n            <div class=\"space-y-1 font-mono text-amber-300\">\n                <div>4 − 1 = <strong class=\"text-emerald-400\">3</strong></div>\n                <div>9 − 4 = <strong class=\"text-emerald-400\">5</strong></div>\n                <div>16 − 9 = <strong class=\"text-emerald-400\">7</strong></div>\n                <div>25 − 16 = <strong class=\"text-emerald-400\">9</strong></div>\n                <div>36 − 25 = <strong class=\"text-emerald-400\">11</strong></div>\n            </div>\n            <p class=\"text-emerald-300 text-[11px] mt-2 font-semibold\">\n                The differences between consecutive square numbers are the consecutive odd numbers (3, 5, 7, 9, 11, ...)!\n            </p>\n        </div>\n    </div>\n</div>\n",
        "takeaways": [
            "Square numbers represent dots arranged in an n × n square grid: n² = n × n.",
            "The square number sequence begins: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, ...",
            "The difference between two consecutive square numbers is always an odd number."
        ],
        "checkpoints": [
            {
                "id": "cp5_1",
                "question": "What is the 8th square number (8²)?",
                "options": [
                    "16",
                    "56",
                    "64",
                    "72"
                ],
                "correct": 2,
                "explanation": "The 8th square number is 8 × 8 = 64."
            },
            {
                "id": "cp5_2",
                "question": "What is the difference between 7² (49) and 6² (36)?",
                "options": [
                    "11",
                    "13",
                    "15",
                    "7"
                ],
                "correct": 1,
                "explanation": "49 − 36 = 13, which is the consecutive odd number following 11."
            }
        ]
    },
    {
        "id": 6,
        "slide_num": 6,
        "title": "Cube Numbers",
        "subtitle": "Spatial 3D Dot Arrays",
        "badge": "3D Geometry",
        "summary": "Stepping from 2D into 3D space, we encounter cube numbers. A cube number represents the number of unit cubes required to build a solid 3D cube of dimensions n × n × n = n³. The sequence begins: 1, 8, 27, 64, 125, 216, ...",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        While square numbers live on a flat 2D sheet of paper, <strong class=\"text-amber-400\">Cube Numbers</strong> leap outward into 3D physical space!\n    </p>\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3 text-xs text-slate-300\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70\">\n            <h4 class=\"font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🧊</span> The Cube Sequence\n            </h4>\n            <div class=\"space-y-1 font-mono text-amber-300\">\n                <div>1³ = 1 × 1 × 1 = <strong>1</strong></div>\n                <div>2³ = 2 × 2 × 2 = <strong>8</strong></div>\n                <div>3³ = 3 × 3 × 3 = <strong>27</strong></div>\n                <div>4³ = 4 × 4 × 4 = <strong>64</strong></div>\n                <div>5³ = 5 × 5 × 5 = <strong>125</strong></div>\n            </div>\n            <p class=\"text-slate-400 text-[11px] mt-2\">\n                Sequence: <code>1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, ...</code>\n            </p>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70\">\n            <h4 class=\"font-bold text-emerald-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🧩</span> Spatial Building Blocks\n            </h4>\n            <p class=\"leading-relaxed mb-2\">\n                Imagine stacking children's wooden toy building blocks:\n            </p>\n            <ul class=\"space-y-1 list-disc list-inside\">\n                <li>A <strong class=\"text-slate-100\">2 × 2 × 2</strong> cube has 2 layers, each containing 4 blocks: 2 × 4 = <strong class=\"text-cyan-300\">8 blocks</strong>.</li>\n                <li>A <strong class=\"text-slate-100\">3 × 3 × 3</strong> Rubik's cube has 3 layers, each containing 9 mini-cubes: 3 × 9 = <strong class=\"text-cyan-300\">27 mini-cubes</strong>.</li>\n            </ul>\n        </div>\n    </div>\n</div>\n",
        "takeaways": [
            "Cube numbers represent the count of unit blocks in a 3D solid cube: n³ = n × n × n.",
            "The cube sequence begins: 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, ...",
            "A standard Rubik's cube has 3 × 3 × 3 = 27 mini-cubes (3³)."
        ],
        "checkpoints": [
            {
                "id": "cp6_1",
                "question": "What is the 4th cube number (4³)?",
                "options": [
                    "12",
                    "16",
                    "64",
                    "128"
                ],
                "correct": 2,
                "explanation": "4³ = 4 × 4 × 4 = 16 × 4 = 64."
            },
            {
                "id": "cp6_2",
                "question": "How many unit cubes are needed to build a solid cube measuring 5 units on every edge?",
                "options": [
                    "15",
                    "25",
                    "75",
                    "125"
                ],
                "correct": 3,
                "explanation": "5 × 5 × 5 = 125 unit cubes."
            }
        ]
    },
    {
        "id": 7,
        "slide_num": 7,
        "title": "Virahānka Numbers",
        "subtitle": "Recursion & Sanskrit Prosody",
        "badge": "Heritage & Nature",
        "summary": "Around 600 CE, the ancient Indian scholar Acharya Virahānka discovered a magical sequence while analyzing poetic meters composed of short (laghu = 1 beat) and long (guru = 2 beats) syllables: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Each term is the sum of the preceding two terms! Over 600 years later, this was reintroduced in Europe as the Fibonacci sequence.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        One of the most celebrated number sequences in all of world science was first discovered right here in ancient India by the scholar-poet <strong class=\"text-amber-400\">Acharya Virahānka</strong> (c. 600 CE), and later elaborated by Gopala (c. 1135 CE) and Acharya Hemachandra (1150 CE).\n    </p>\n    <div class=\"p-3.5 rounded-xl bg-gradient-to-r from-amber-950/40 via-slate-900 to-emerald-950/40 border border-amber-500/30 space-y-2\">\n        <h4 class=\"font-bold text-amber-300 text-sm flex items-center gap-2\">\n            <span>📜</span> The Rhythmic Meter Discovery\n        </h4>\n        <p class=\"text-xs text-slate-300 leading-relaxed\">\n            In Sanskrit prosody, poetry is recited with two syllable durations:\n        </p>\n        <div class=\"grid grid-cols-2 gap-2 text-xs font-mono text-center\">\n            <div class=\"p-2 rounded bg-slate-950 border border-slate-800\">\n                <span class=\"text-cyan-300 font-bold\">Laghu (Short)</span> = 1 beat (•)\n            </div>\n            <div class=\"p-2 rounded bg-slate-950 border border-slate-800\">\n                <span class=\"text-amber-300 font-bold\">Guru (Long)</span> = 2 beats (—)\n            </div>\n        </div>\n        <p class=\"text-xs text-slate-300 leading-relaxed mt-1\">\n            Virahānka asked: <em>\"How many rhythmic poetic patterns can be created with n total beats?\"</em>\n        </p>\n        <div class=\"p-2.5 rounded bg-slate-950 text-xs font-mono text-emerald-300 space-y-0.5\">\n            <div>1 beat: [•] ➔ <strong>1 pattern</strong></div>\n            <div>2 beats: [••], [—] ➔ <strong>2 patterns</strong></div>\n            <div>3 beats: [•••], [•—], [—•] ➔ <strong>3 patterns</strong></div>\n            <div>4 beats: [••••], [••—], [•—•], [—••], [——] ➔ <strong>5 patterns</strong></div>\n            <div>5 beats: ➔ <strong>8 patterns</strong> (3 + 5 = 8)</div>\n        </div>\n    </div>\n    <div class=\"p-3 rounded-lg bg-slate-900/80 border border-slate-700/70 text-xs text-slate-300 space-y-1\">\n        <strong class=\"text-cyan-300 block font-bold\">The Recurrence Rule:</strong>\n        <p>\n            Start with <code class=\"text-amber-300 font-mono\">1, 1</code>. Every subsequent term is calculated by <strong class=\"text-emerald-400\">adding the previous two terms</strong>:\n        </p>\n        <p class=\"font-mono text-cyan-300\">\n            1 + 1 = 2 &nbsp;|&nbsp; 1 + 2 = 3 &nbsp;|&nbsp; 2 + 3 = 5 &nbsp;|&nbsp; 3 + 5 = 8 &nbsp;|&nbsp; 5 + 8 = 13 &nbsp;|&nbsp; 8 + 13 = 21 &nbsp;|&nbsp; 13 + 21 = 34 ...\n        </p>\n    </div>\n</div>\n",
        "takeaways": [
            "Acharya Virahānka (~600 CE) discovered the Virahānka numbers (Fibonacci sequence) through poetic rhythms.",
            "Rule: Each number is the sum of the preceding two numbers (1, 1, 2, 3, 5, 8, 13, 21, 34, ...).",
            "Virahānka numbers appear universally in nature: sunflower seed spirals, pinecone scales, and pineapple skins."
        ],
        "checkpoints": [
            {
                "id": "cp7_1",
                "question": "What is the next term in the Virahānka sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34, ...?",
                "options": [
                    "45",
                    "50",
                    "55",
                    "68"
                ],
                "correct": 2,
                "explanation": "In the Virahānka sequence, each term is the sum of the previous two: 21 + 34 = 55."
            },
            {
                "id": "cp7_2",
                "question": "Who was the ancient Indian scholar who discovered this sequence around 600 CE while studying poetic meters?",
                "options": [
                    "Acharya Virahānka",
                    "Fibonacci",
                    "Pythagoras",
                    "Euclid"
                ],
                "correct": 0,
                "explanation": "Acharya Virahānka discovered this sequence in approximately 600 CE, centuries before Leonardo Fibonacci wrote about it in 1202 CE."
            }
        ]
    },
    {
        "id": 8,
        "slide_num": 8,
        "title": "Powers of 2 and 3",
        "subtitle": "Doubling & Tripling Growth",
        "badge": "Exponential Powers",
        "summary": "When a number is repeatedly multiplied by itself, it generates a sequence of powers. Powers of 2 represent continuous doubling (1, 2, 4, 8, 16, 32, 64, 128, ...), as seen in paper folding and computer memory chips. Powers of 3 represent continuous tripling (1, 3, 9, 27, 81, 243, ...).",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Addition makes numbers grow steadily by a fixed amount. But <strong class=\"text-amber-400\">Multiplication</strong> makes numbers explode at an astonishing, exponential pace!\n    </p>\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3 text-xs text-slate-300\">\n        <div class=\"p-3.5 rounded-xl bg-cyan-950/40 border border-cyan-500/30\">\n            <h4 class=\"font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>⚡</span> Powers of 2 (Continuous Doubling)\n            </h4>\n            <div class=\"space-y-0.5 font-mono text-cyan-200\">\n                <div>2⁰ = <strong>1</strong></div>\n                <div>2¹ = 1 × 2 = <strong>2</strong></div>\n                <div>2² = 2 × 2 = <strong>4</strong></div>\n                <div>2³ = 4 × 2 = <strong>8</strong></div>\n                <div>2⁴ = 8 × 2 = <strong>16</strong></div>\n                <div>2⁵ = 16 × 2 = <strong>32</strong></div>\n                <div>2⁶ = 32 × 2 = <strong>64</strong></div>\n            </div>\n            <p class=\"text-slate-300 text-[11px] mt-2\">\n                <strong class=\"text-slate-100\">Paper Folding:</strong> Fold a sheet of paper once ➔ 2 layers. Fold twice ➔ 4 layers. Fold 7 times ➔ 128 layers!\n            </p>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-amber-950/40 border border-amber-500/30\">\n            <h4 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>💥</span> Powers of 3 (Continuous Tripling)\n            </h4>\n            <div class=\"space-y-0.5 font-mono text-amber-200\">\n                <div>3⁰ = <strong>1</strong></div>\n                <div>3¹ = 1 × 3 = <strong>3</strong></div>\n                <div>3² = 3 × 3 = <strong>9</strong></div>\n                <div>3³ = 9 × 3 = <strong>27</strong></div>\n                <div>3⁴ = 27 × 3 = <strong>81</strong></div>\n                <div>3⁵ = 81 × 3 = <strong>243</strong></div>\n            </div>\n            <p class=\"text-slate-300 text-[11px] mt-2\">\n                <strong class=\"text-slate-100\">Branching Trees:</strong> If a tree branch splits into 3 new twigs, and each twig splits into 3 smaller twigs, the growth follows powers of 3!\n            </p>\n        </div>\n    </div>\n</div>\n",
        "takeaways": [
            "Powers of 2 double at every step: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, ...",
            "Powers of 3 triple at every step: 1, 3, 9, 27, 81, 243, 729, ...",
            "Exponential sequences grow far faster than addition sequences."
        ],
        "checkpoints": [
            {
                "id": "cp8_1",
                "question": "What is the value of 2⁶ (the 7th power of 2 starting from 2⁰ = 1)?",
                "options": [
                    "12",
                    "32",
                    "64",
                    "128"
                ],
                "correct": 2,
                "explanation": "2⁶ = 2 × 2 × 2 × 2 × 2 × 2 = 64."
            },
            {
                "id": "cp8_2",
                "question": "If you fold a large newspaper in half 6 times consecutively, how many layers of paper thickness are created?",
                "options": [
                    "12 layers",
                    "36 layers",
                    "64 layers",
                    "128 layers"
                ],
                "correct": 2,
                "explanation": "Each fold doubles the previous layer count: 2⁶ = 64 layers."
            }
        ]
    },
    {
        "id": 9,
        "slide_num": 9,
        "title": "The Chameleon Number 36",
        "subtitle": "Square & Triangular Dual Roles",
        "badge": "Visualisations",
        "summary": "Numbers are not rigid; they can play completely different roles depending on the geometric context in which they appear! For example, the number 36 can be arranged as an 8-row triangular number (1+2+3+4+5+6+7+8 = 36) and as a 6 × 6 square number (6² = 36). Numbers that are simultaneously triangular and square are called square-triangular numbers.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Can a single number be both a triangle and a square? In mathematics, the answer is a resounding <strong class=\"text-amber-400 font-bold\">YES</strong>!\n    </p>\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3 text-xs text-slate-300\">\n        <div class=\"p-3.5 rounded-xl bg-amber-950/40 border border-amber-500/30\">\n            <h4 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🔺</span> 36 as a Triangular Number (T₈)\n            </h4>\n            <p class=\"leading-relaxed mb-2\">\n                Arrange 36 dots into an 8-row triangle:\n            </p>\n            <div class=\"p-2 rounded bg-slate-950 font-mono text-amber-200 text-center\">\n                1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = <strong>36</strong>\n            </div>\n            <p class=\"mt-2 text-slate-300\">\n                Formula check: <code class=\"text-cyan-300 font-mono\">(8 × 9) ÷ 2 = 72 ÷ 2 = 36</code>. It forms a perfect equilateral triangle!\n            </p>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-cyan-950/40 border border-cyan-500/30\">\n            <h4 class=\"font-bold text-cyan-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>⬛</span> 36 as a Square Number (6²)\n            </h4>\n            <p class=\"leading-relaxed mb-2\">\n                Take those exact same 36 dots and rearrange them into a grid of 6 rows and 6 columns:\n            </p>\n            <div class=\"p-2 rounded bg-slate-950 font-mono text-cyan-200 text-center\">\n                6 × 6 = 6² = <strong>36</strong>\n            </div>\n            <p class=\"mt-2 text-slate-300\">\n                Formula check: 6 rows × 6 columns = 36 dots. It forms a perfect flat square!\n            </p>\n        </div>\n    </div>\n    <div class=\"p-3 rounded-lg bg-emerald-950/40 border border-emerald-500/30 text-xs text-slate-300\">\n        <strong class=\"text-emerald-300\">Square-Triangular Numbers:</strong> Numbers that can be represented as both triangular and square are exceptionally rare and fascinating: <code class=\"text-amber-300 font-mono font-bold\">1, 36, 1225, 41616, ...</code>\n    </div>\n</div>\n",
        "takeaways": [
            "Numbers play different roles depending on the geometric arrangement of their dots.",
            "36 is both the 8th triangular number (1+2+...+8 = 36) and the 6th square number (6 × 6 = 36).",
            "Numbers that are simultaneously square and triangular are called square-triangular numbers (1, 36, 1225, ...)."
        ],
        "checkpoints": [
            {
                "id": "cp9_1",
                "question": "Which of the following numbers can be arranged both as a triangular number and as a square number?",
                "options": [
                    "16",
                    "25",
                    "36",
                    "49"
                ],
                "correct": 2,
                "explanation": "36 = 1+2+3+4+5+6+7+8 (T₈) and 36 = 6 × 6 (6²)."
            },
            {
                "id": "cp9_2",
                "question": "Which triangular number equals 36?",
                "options": [
                    "T₆ (the 6th triangular number)",
                    "T₇ (the 7th triangular number)",
                    "T₈ (the 8th triangular number)",
                    "T₁₀ (the 10th triangular number)"
                ],
                "correct": 2,
                "explanation": "T₈ = (8 × 9) / 2 = 72 / 2 = 36."
            }
        ]
    },
    {
        "id": 10,
        "slide_num": 10,
        "title": "Centered Hexagonal Numbers",
        "subtitle": "Concentric Honeycomb Rings",
        "badge": "Hexagonal Patterns",
        "summary": "When dots are arranged in concentric regular hexagons around a single central dot, they form the sequence of centered hexagonal numbers: 1, 7, 19, 37, 61, 91, ... Each new ring adds an extra multiple of 6 dots (+6, +12, +18, +24, ...). This pattern is nature's chosen blueprint for honeybee comb construction.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Why do honeybees always build their combs using six-sided <strong class=\"text-amber-400\">hexagons</strong> instead of circles, squares, or triangles? Because hexagons tile a surface perfectly with the minimal amount of wax boundary, maximizing honey storage!\n    </p>\n    <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70 space-y-2\">\n        <h4 class=\"font-bold text-amber-300 text-sm flex items-center gap-2\">\n            <span>🐝</span> The Concentric Hexagonal Ring Rule\n        </h4>\n        <div class=\"grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs font-mono text-center\">\n            <div class=\"p-2 rounded bg-slate-950 border border-slate-800\">\n                <span class=\"text-slate-400 block text-[10px]\">Center</span>\n                <span class=\"text-amber-300 text-sm font-bold\">1</span>\n            </div>\n            <div class=\"p-2 rounded bg-slate-950 border border-slate-800\">\n                <span class=\"text-slate-400 block text-[10px]\">Ring 1: +6</span>\n                <span class=\"text-amber-300 text-sm font-bold\">7</span>\n            </div>\n            <div class=\"p-2 rounded bg-slate-950 border border-slate-800\">\n                <span class=\"text-slate-400 block text-[10px]\">Ring 2: +12</span>\n                <span class=\"text-amber-300 text-sm font-bold\">19</span>\n            </div>\n            <div class=\"p-2 rounded bg-slate-950 border border-slate-800\">\n                <span class=\"text-slate-400 block text-[10px]\">Ring 3: +18</span>\n                <span class=\"text-amber-300 text-sm font-bold\">37</span>\n            </div>\n        </div>\n        <p class=\"text-xs text-slate-300 leading-relaxed mt-2\">\n            Notice the additions between rings: <strong class=\"text-cyan-300 font-mono\">+6, +12, +18, +24, +30, ...</strong> (multiples of 6)!\n        </p>\n        <p class=\"text-xs text-slate-300 leading-relaxed\">\n            The sequence continues: <code class=\"text-emerald-400 font-mono font-bold\">1, 7, 19, 37, 61, 91, 127, 169, ...</code>\n        </p>\n    </div>\n</div>\n",
        "takeaways": [
            "Centered hexagonal numbers grow by adding concentric hexagonal rings of dots: 1, 7, 19, 37, 61, 91, ...",
            "The differences between successive terms are consecutive multiples of 6 (+6, +12, +18, +24, ...).",
            "Honeybees utilize hexagonal tiling to achieve maximum volume with minimal wax boundary."
        ],
        "checkpoints": [
            {
                "id": "cp10_1",
                "question": "What is the 4th centered hexagonal number (Ring 3)?",
                "options": [
                    "25",
                    "31",
                    "37",
                    "43"
                ],
                "correct": 2,
                "explanation": "1 + 6 = 7; 7 + 12 = 19; 19 + 18 = 37."
            },
            {
                "id": "cp10_2",
                "question": "How many dots are added to go from 37 to the 5th hexagonal number (Ring 4)?",
                "options": [
                    "18 dots",
                    "20 dots",
                    "24 dots (4 × 6)",
                    "30 dots"
                ],
                "correct": 2,
                "explanation": "The successive ring additions are +6, +12, +18, +24. Thus, 37 + 24 = 61."
            }
        ]
    },
    {
        "id": 11,
        "slide_num": 11,
        "title": "Sum of Odd Numbers",
        "subtitle": "Odd Numbers Forming Squares",
        "badge": "Visual Proofs",
        "summary": "One of the most astonishing relations in mathematics links odd numbers directly to square numbers: adding consecutive odd numbers starting from 1 always yields a perfect square! 1 = 1², 1+3 = 2², 1+3+5 = 3², 1+3+5+7 = 4². A visual proof using L-shaped borders (gnomons) makes the reason immediately obvious without algebra.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Mathematics becomes pure poetry when two seemingly unrelated number sequences suddenly shake hands. Consider what happens when you sum the odd numbers in order:\n    </p>\n    <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70 space-y-1.5 font-mono text-xs\">\n        <div class=\"text-amber-300\">1 = 1 = <strong>1²</strong></div>\n        <div class=\"text-cyan-300\">1 + 3 = 4 = <strong>2²</strong></div>\n        <div class=\"text-emerald-300\">1 + 3 + 5 = 9 = <strong>3²</strong></div>\n        <div class=\"text-purple-300\">1 + 3 + 5 + 7 = 16 = <strong>4²</strong></div>\n        <div class=\"text-rose-300\">1 + 3 + 5 + 7 + 9 = 25 = <strong>5²</strong></div>\n        <div class=\"text-yellow-300\">1 + 3 + 5 + 7 + 9 + 11 = 36 = <strong>6²</strong></div>\n    </div>\n    <div class=\"p-3.5 rounded-xl bg-gradient-to-r from-cyan-950/40 to-slate-900 border border-cyan-500/30 text-xs text-slate-300 space-y-2\">\n        <h4 class=\"font-bold text-cyan-300 text-sm flex items-center gap-2\">\n            <span>📐</span> The L-Shaped Gnomon Visual Proof\n        </h4>\n        <p class=\"leading-relaxed\">\n            Why does this work? Imagine a single dot in the top-left corner (<code class=\"text-amber-300 font-mono\">1</code>).\n        </p>\n        <ul class=\"space-y-1 list-disc list-inside\">\n            <li>To expand this 1×1 square to a 2×2 square, wrap an L-shaped corner strip of <strong class=\"text-cyan-300 font-bold\">3 dots</strong> around it (1 + 3 = 4 = 2²).</li>\n            <li>To expand the 2×2 square to a 3×3 square, wrap a new outer L-shaped strip of <strong class=\"text-emerald-300 font-bold\">5 dots</strong> around it (4 + 5 = 9 = 3²).</li>\n            <li>Each successive L-shaped border requires exactly 2 more dots than the previous one: 1, 3, 5, 7, 9, ...</li>\n        </ul>\n        <p class=\"text-emerald-300 font-semibold pt-1\">\n            The sum of the first n consecutive odd numbers ALWAYS equals n²!\n        </p>\n    </div>\n</div>\n",
        "takeaways": [
            "Adding consecutive odd numbers starting from 1 always produces a square number: 1+3+...+ (2n-1) = n².",
            "The L-shaped gnomon visual proof demonstrates that adding 2k+1 dots around a k × k square produces a (k+1) × (k+1) square.",
            "The sum of the first 10 odd numbers is 10² = 100."
        ],
        "checkpoints": [
            {
                "id": "cp11_1",
                "question": "What is the sum of the first 6 odd numbers: 1 + 3 + 5 + 7 + 9 + 11?",
                "options": [
                    "30",
                    "36 (6²)",
                    "42",
                    "49"
                ],
                "correct": 1,
                "explanation": "The sum of the first n odd numbers is n². For n = 6, 6² = 36."
            },
            {
                "id": "cp11_2",
                "question": "Without adding them manually, what is the sum of the first 10 odd numbers?",
                "options": [
                    "50",
                    "90",
                    "100 (10²)",
                    "110"
                ],
                "correct": 2,
                "explanation": "Using the theorem, the sum of the first 10 odd numbers is 10² = 100."
            }
        ]
    },
    {
        "id": 12,
        "slide_num": 12,
        "title": "Counting Pyramids & Triangles",
        "subtitle": "Mountain Sums & Paired Triangles",
        "badge": "Algebraic Harmony",
        "summary": "Another magical connection appears when we add counting numbers up to a peak and back down: 1+2+1 = 4 = 2², 1+2+3+2+1 = 9 = 3², 1+2+3+4+3+2+1 = 16 = 4². Furthermore, adding any two consecutive triangular numbers always yields a perfect square: T_{n-1} + T_n = n²!",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Let us explore two more miraculous relationships hidden between counting numbers, triangular numbers, and squares.\n    </p>\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3 text-xs text-slate-300\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70\">\n            <h4 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>⛰️</span> 1. Adding Up and Down (Mountain Sums)\n            </h4>\n            <div class=\"space-y-1 font-mono text-cyan-300\">\n                <div>1 = <strong>1²</strong></div>\n                <div>1 + 2 + 1 = 4 = <strong>2²</strong></div>\n                <div>1 + 2 + 3 + 2 + 1 = 9 = <strong>3²</strong></div>\n                <div>1 + 2 + 3 + 4 + 3 + 2 + 1 = 16 = <strong>4²</strong></div>\n                <div>1 + 2 + 3 + 4 + 5 + 4 + 3 + 2 + 1 = 25 = <strong>5²</strong></div>\n            </div>\n            <p class=\"text-slate-300 mt-2\">\n                <strong class=\"text-slate-100\">Visual Proof:</strong> Slice a square grid of dots diagonally! The diagonal columns contain 1, 2, 3, 4, 3, 2, 1 dots, which sum up to the total area of the square!\n            </p>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70\">\n            <h4 class=\"font-bold text-emerald-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🧩</span> 2. Merging Two Consecutive Triangles\n            </h4>\n            <p class=\"leading-relaxed mb-2\">\n                Take two consecutive triangular numbers and add them together:\n            </p>\n            <div class=\"space-y-1 font-mono text-emerald-300\">\n                <div>T₁ + T₂ = 1 + 3 = 4 = <strong>2²</strong></div>\n                <div>T₂ + T₃ = 3 + 6 = 9 = <strong>3²</strong></div>\n                <div>T₃ + T₄ = 6 + 10 = 16 = <strong>4²</strong></div>\n                <div>T₄ + T₅ = 10 + 15 = 25 = <strong>5²</strong></div>\n                <div>T₅ + T₆ = 15 + 21 = 36 = <strong>6²</strong></div>\n            </div>\n            <p class=\"text-slate-300 mt-2\">\n                <strong class=\"text-slate-100\">Visual Proof:</strong> Two identical triangles fit together along their diagonal hypotenuse like puzzle pieces to form a square!\n            </p>\n        </div>\n    </div>\n</div>\n",
        "takeaways": [
            "Counting up to n and back down to 1 always equals n²: 1 + 2 + ... + n + ... + 2 + 1 = n².",
            "The sum of any two consecutive triangular numbers equals a square number: T_{n-1} + T_n = n².",
            "Visual geometric proofs explain why algebraic identities work without memorizing formulas."
        ],
        "checkpoints": [
            {
                "id": "cp12_1",
                "question": "What is the sum of: 1 + 2 + 3 + 4 + 5 + 6 + 5 + 4 + 3 + 2 + 1?",
                "options": [
                    "30",
                    "36 (6²)",
                    "40",
                    "42"
                ],
                "correct": 1,
                "explanation": "When counting up to peak n and back down to 1, the sum is n². Here peak n = 6, so 6² = 36."
            },
            {
                "id": "cp12_2",
                "question": "If T₄ = 10 and T₅ = 15, what is their sum (T₄ + T₅)?",
                "options": [
                    "20",
                    "24",
                    "25 (5²)",
                    "30"
                ],
                "correct": 2,
                "explanation": "T₄ + T₅ = 10 + 15 = 25 = 5² (the 5th square number)."
            }
        ]
    },
    {
        "id": 13,
        "slide_num": 13,
        "title": "Patterns in Shapes",
        "subtitle": "Dimensions & Regular Polygons",
        "badge": "Geometry & Polygons",
        "summary": "Geometry is the mathematical branch dedicated to studying patterns of shapes across dimensions: 1D (lines), 2D (polygons), and 3D (solids). In Table 3, the sequence of regular polygons begins with an equilateral triangle (3 sides), square (4 sides), regular pentagon (5 sides), and regular hexagon (6 sides), connecting shape corners directly to counting numbers starting from 3.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Just as Number Theory investigates patterns in numbers, <strong class=\"text-amber-400\">Geometry</strong> explores patterns in shapes, sizes, dimensions, and space!\n    </p>\n    <div class=\"grid grid-cols-1 md:grid-cols-3 gap-2.5 text-xs text-slate-300\">\n        <div class=\"p-3 rounded-xl bg-slate-900/80 border border-slate-700/70\">\n            <strong class=\"text-cyan-300 block mb-1\">1D: One-Dimensional</strong>\n            <p>Line segments, rays, curves. Has length, but zero width or thickness.</p>\n        </div>\n        <div class=\"p-3 rounded-xl bg-slate-900/80 border border-slate-700/70\">\n            <strong class=\"text-emerald-300 block mb-1\">2D: Two-Dimensional</strong>\n            <p>Flat plane figures: polygons, circles. Has length and width, enclosing an area.</p>\n        </div>\n        <div class=\"p-3 rounded-xl bg-slate-900/80 border border-slate-700/70\">\n            <strong class=\"text-amber-300 block mb-1\">3D: Three-Dimensional</strong>\n            <p>Solid bodies: cubes, spheres, pyramids. Has length, width, and height (volume).</p>\n        </div>\n    </div>\n    <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70 space-y-2\">\n        <h4 class=\"font-bold text-amber-300 text-sm flex items-center gap-2\">\n            <span>🔷</span> The Regular Polygons Sequence (Table 3)\n        </h4>\n        <p class=\"text-xs text-slate-300 leading-relaxed\">\n            A <strong>regular polygon</strong> has all sides equal in length and all interior angles equal:\n        </p>\n        <div class=\"grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs font-mono text-center\">\n            <div class=\"p-2 rounded bg-slate-950 border border-slate-800\">\n                <span class=\"text-slate-400 block text-[10px]\">3 Sides</span>\n                <span class=\"text-amber-300 font-bold\">Triangle</span>\n            </div>\n            <div class=\"p-2 rounded bg-slate-950 border border-slate-800\">\n                <span class=\"text-slate-400 block text-[10px]\">4 Sides</span>\n                <span class=\"text-amber-300 font-bold\">Square</span>\n            </div>\n            <div class=\"p-2 rounded bg-slate-950 border border-slate-800\">\n                <span class=\"text-slate-400 block text-[10px]\">5 Sides</span>\n                <span class=\"text-amber-300 font-bold\">Pentagon</span>\n            </div>\n            <div class=\"p-2 rounded bg-slate-950 border border-slate-800\">\n                <span class=\"text-slate-400 block text-[10px]\">6 Sides</span>\n                <span class=\"text-amber-300 font-bold\">Hexagon</span>\n            </div>\n        </div>\n        <p class=\"text-xs text-slate-300 leading-relaxed mt-1\">\n            The number of sides or corners forms the counting sequence starting from 3: <code class=\"text-cyan-300 font-mono\">3, 4, 5, 6, 7, 8, ...</code>\n        </p>\n    </div>\n</div>\n",
        "takeaways": [
            "Geometry studies patterns in shapes across 1D (length), 2D (area), and 3D (volume).",
            "Regular polygons have all sides and all interior angles equal.",
            "The sequence of corners in regular polygons corresponds to counting numbers starting from 3: 3, 4, 5, 6, 7, 8, ..."
        ],
        "checkpoints": [
            {
                "id": "cp13_1",
                "question": "What is the minimum number of straight sides required to enclose a 2D polygon?",
                "options": [
                    "1 side",
                    "2 sides",
                    "3 sides (Triangle)",
                    "4 sides"
                ],
                "correct": 2,
                "explanation": "A polygon requires at least 3 straight line segments to enclose a 2D surface area (a triangle)."
            },
            {
                "id": "cp13_2",
                "question": "How many corners (vertices) does a regular octagon have?",
                "options": [
                    "6",
                    "7",
                    "8",
                    "10"
                ],
                "correct": 2,
                "explanation": "An octagon is an 8-sided polygon with 8 corners."
            }
        ]
    },
    {
        "id": 14,
        "slide_num": 14,
        "title": "Complete Graphs & Handshakes",
        "subtitle": "Network Nodes & Chords",
        "badge": "Network Graphs",
        "summary": "In Table 3, complete graphs (denoted K₂, K₃, K₄, K₅, ...) are shapes formed by placing n dots on a circle and connecting every pair of dots with a straight line. Counting the number of lines (edges) reveals a breathtaking surprise: the edge counts are exactly the Triangular Numbers! 1, 3, 6, 10, 15, ... This also solves the famous Handshake Problem.",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Place <strong class=\"text-cyan-300\">n dots</strong> around a circle and connect every dot to every other dot with a straight chord. In modern mathematics, this network is called a <strong class=\"text-amber-400\">Complete Graph</strong> (<code class=\"text-amber-300 font-mono\">Kₙ</code>).\n    </p>\n    <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70 space-y-2\">\n        <h4 class=\"font-bold text-amber-300 text-sm flex items-center gap-2\">\n            <span>🕸️</span> Counting the Edges in Complete Graphs\n        </h4>\n        <div class=\"grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs font-mono text-center\">\n            <div class=\"p-2 rounded bg-slate-950 border border-slate-800\">\n                <span class=\"text-slate-400 block text-[10px]\">K₂: 2 Dots</span>\n                <span class=\"text-emerald-400 font-bold\">1 Line (T₁)</span>\n            </div>\n            <div class=\"p-2 rounded bg-slate-950 border border-slate-800\">\n                <span class=\"text-slate-400 block text-[10px]\">K₃: 3 Dots</span>\n                <span class=\"text-emerald-400 font-bold\">3 Lines (T₂)</span>\n            </div>\n            <div class=\"p-2 rounded bg-slate-950 border border-slate-800\">\n                <span class=\"text-slate-400 block text-[10px]\">K₄: 4 Dots</span>\n                <span class=\"text-emerald-400 font-bold\">6 Lines (T₃)</span>\n            </div>\n            <div class=\"p-2 rounded bg-slate-950 border border-slate-800\">\n                <span class=\"text-slate-400 block text-[10px]\">K₅: 5 Dots</span>\n                <span class=\"text-emerald-400 font-bold\">10 Lines (T₄)</span>\n            </div>\n        </div>\n        <p class=\"text-xs text-slate-300 leading-relaxed mt-2\">\n            The number of edges in Kₙ matches the sequence of triangular numbers: <code class=\"text-emerald-400 font-mono font-bold\">1, 3, 6, 10, 15, 21, ...</code>\n        </p>\n    </div>\n    <div class=\"p-3.5 rounded-xl bg-cyan-950/40 border border-cyan-500/30 text-xs text-slate-300 space-y-1.5\">\n        <h5 class=\"font-bold text-cyan-300 text-xs flex items-center gap-1.5\">\n            <span>🤝</span> The Famous Handshake Problem\n        </h5>\n        <p class=\"leading-relaxed\">\n            Suppose <strong>5 friends</strong> attend a birthday party and everyone shakes hands with every other person exactly once. How many total handshakes occur?\n        </p>\n        <p class=\"font-mono text-emerald-300\">\n            Total Handshakes = K₅ edges = (5 × 4) ÷ 2 = 10 handshakes!\n        </p>\n        <p class=\"text-[11px] text-slate-400\">\n            Formula: For n people, total handshakes = <code class=\"text-slate-200\">n(n − 1) ÷ 2</code> (the (n−1)-th triangular number)!\n        </p>\n    </div>\n</div>\n",
        "takeaways": [
            "A complete graph Kₙ connects n vertices such that every pair shares an edge.",
            "The number of edges in complete graphs forms the sequence of triangular numbers: 1, 3, 6, 10, 15, ...",
            "The Handshake Problem for n people is mathematically identical to counting the edges in Kₙ: n(n−1)/2."
        ],
        "checkpoints": [
            {
                "id": "cp14_1",
                "question": "How many connecting edges are there in a complete graph with 4 vertices (K₄)?",
                "options": [
                    "4 edges",
                    "6 edges (T₃)",
                    "8 edges",
                    "12 edges"
                ],
                "correct": 1,
                "explanation": "In K₄, connecting all pairs of 4 points produces (4 × 3) / 2 = 6 edges."
            },
            {
                "id": "cp14_2",
                "question": "If 6 chess players in a tournament each play a match against every other player once, how many matches are played in total?",
                "options": [
                    "12 matches",
                    "15 matches (T₅)",
                    "20 matches",
                    "30 matches"
                ],
                "correct": 1,
                "explanation": "Total matches = K₆ edges = (6 × 5) / 2 = 15 matches (the 5th triangular number T₅)."
            }
        ]
    },
    {
        "id": 15,
        "slide_num": 15,
        "title": "Stacked Shape Pyramids",
        "subtitle": "Layered 3D Pyramids",
        "badge": "3D Stacking",
        "summary": "In Table 3, shapes can be stacked layer-by-layer into three-dimensional pyramids. Stacking square grids produces square pyramidal numbers: 1, 1+4=5, 1+4+9=14, 1+4+9+16=30, ... Stacking triangular layers produces tetrahedral numbers: 1, 1+3=4, 1+3+6=10, 1+3+6+10=20, ...",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Ancient Egyptian architects built colossal pyramids by stacking blocks in diminishing tiers. In mathematics, stacking 2D figurate shapes creates fascinating 3D accumulation patterns!\n    </p>\n    <div class=\"grid grid-cols-1 md:grid-cols-2 gap-3 text-xs text-slate-300\">\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70\">\n            <h4 class=\"font-bold text-amber-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>🏛️</span> Stacked Squares (Pyramids)\n            </h4>\n            <p class=\"leading-relaxed mb-2\">\n                Each layer is a square number:\n            </p>\n            <div class=\"space-y-1 font-mono text-cyan-300\">\n                <div>Level 1: 1² = <strong>1</strong></div>\n                <div>Level 2: 1 + 4 = <strong>5</strong></div>\n                <div>Level 3: 1 + 4 + 9 = <strong>14</strong></div>\n                <div>Level 4: 1 + 4 + 9 + 16 = <strong>30</strong></div>\n                <div>Level 5: 1 + 4 + 9 + 16 + 25 = <strong>55</strong></div>\n            </div>\n            <p class=\"text-slate-400 text-[11px] mt-2\">\n                Sequence: <code>1, 5, 14, 30, 55, 91, 140, ...</code>\n            </p>\n        </div>\n        <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70\">\n            <h4 class=\"font-bold text-emerald-300 text-sm mb-1.5 flex items-center gap-2\">\n                <span>⛺</span> Stacked Triangles (Tetrahedrons)\n            </h4>\n            <p class=\"leading-relaxed mb-2\">\n                Each layer is a triangular number:\n            </p>\n            <div class=\"space-y-1 font-mono text-emerald-300\">\n                <div>Level 1: T₁ = <strong>1</strong></div>\n                <div>Level 2: 1 + 3 = <strong>4</strong></div>\n                <div>Level 3: 1 + 3 + 6 = <strong>10</strong></div>\n                <div>Level 4: 1 + 3 + 6 + 10 = <strong>20</strong></div>\n                <div>Level 5: 1 + 3 + 6 + 10 + 15 = <strong>35</strong></div>\n            </div>\n            <p class=\"text-slate-400 text-[11px] mt-2\">\n                Sequence: <code>1, 4, 10, 20, 35, 56, 84, ...</code>\n            </p>\n        </div>\n    </div>\n</div>\n",
        "takeaways": [
            "Stacked squares accumulate sums of consecutive square numbers: 1, 5, 14, 30, 55, ...",
            "Stacked triangles accumulate sums of triangular numbers to form tetrahedral numbers: 1, 4, 10, 20, 35, ...",
            "3D stacked shapes link 2D area patterns directly to 3D volume accumulation."
        ],
        "checkpoints": [
            {
                "id": "cp15_1",
                "question": "How many total unit blocks are in a 3-level stacked square pyramid (1² + 2² + 3²)?",
                "options": [
                    "9 blocks",
                    "12 blocks",
                    "14 blocks",
                    "16 blocks"
                ],
                "correct": 2,
                "explanation": "1² + 2² + 3² = 1 + 4 + 9 = 14 blocks."
            },
            {
                "id": "cp15_2",
                "question": "What is the 3rd tetrahedral number formed by stacking the first 3 triangular numbers (1 + 3 + 6)?",
                "options": [
                    "8",
                    "10",
                    "12",
                    "15"
                ],
                "correct": 1,
                "explanation": "1 + 3 + 6 = 10."
            }
        ]
    },
    {
        "id": 16,
        "slide_num": 16,
        "title": "The Koch Snowflake",
        "subtitle": "Fractal Perimeter & Area",
        "badge": "Fractals & Powers",
        "summary": "One of the most mind-bending shape sequences in mathematics is the Koch Snowflake. Starting with an equilateral triangle (3 edges), each straight segment is replaced by 4 smaller segments in successive iterations. The number of outer edges follows the sequence of powers of 4 multiplied by 3: 3, 12, 48, 192, 768, ... As iterations continue, its perimeter becomes infinitely long while enclosing a finite area!",
        "theory": "\n<div class=\"space-y-4 text-slate-200\">\n    <p class=\"leading-relaxed\">\n        Can a shape have an <strong class=\"text-amber-400 font-bold\">infinitely long boundary perimeter</strong>, yet fit comfortably inside a small circle on your notebook page? Enter the world of <strong class=\"text-cyan-300\">Fractals</strong>!\n    </p>\n    <div class=\"p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/70 space-y-2\">\n        <h4 class=\"font-bold text-amber-300 text-sm flex items-center gap-2\">\n            <span>❄️</span> Construction Rule of the Koch Snowflake\n        </h4>\n        <ul class=\"text-xs text-slate-300 space-y-1.5 list-disc list-inside\">\n            <li><strong class=\"text-slate-100\">Iteration 0:</strong> Start with an equilateral triangle (3 sides).</li>\n            <li><strong class=\"text-slate-100\">Step Rule:</strong> Divide every edge into 3 equal thirds. Replace the middle third with two sides of a smaller equilateral triangle pointing outward.</li>\n            <li>Each single segment is thereby replaced by <strong class=\"text-emerald-400 font-bold\">4 segments</strong>!</li>\n        </ul>\n        <div class=\"grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs font-mono text-center mt-2\">\n            <div class=\"p-2 rounded bg-slate-950 border border-slate-800\">\n                <span class=\"text-slate-400 block text-[10px]\">Iter 0: 3 × 4⁰</span>\n                <span class=\"text-cyan-300 font-bold\">3 Edges</span>\n            </div>\n            <div class=\"p-2 rounded bg-slate-950 border border-slate-800\">\n                <span class=\"text-slate-400 block text-[10px]\">Iter 1: 3 × 4¹</span>\n                <span class=\"text-cyan-300 font-bold\">12 Edges</span>\n            </div>\n            <div class=\"p-2 rounded bg-slate-950 border border-slate-800\">\n                <span class=\"text-slate-400 block text-[10px]\">Iter 2: 3 × 4²</span>\n                <span class=\"text-cyan-300 font-bold\">48 Edges</span>\n            </div>\n            <div class=\"p-2 rounded bg-slate-950 border border-slate-800\">\n                <span class=\"text-slate-400 block text-[10px]\">Iter 3: 3 × 4³</span>\n                <span class=\"text-cyan-300 font-bold\">192 Edges</span>\n            </div>\n        </div>\n        <p class=\"text-xs text-slate-300 leading-relaxed mt-2\">\n            Edge sequence: <code class=\"text-emerald-400 font-mono font-bold\">3, 12, 48, 192, 768, 3072, ...</code> (each term multiplied by 4, generating powers of 4)!\n        </p>\n    </div>\n    <div class=\"p-3 rounded-lg bg-emerald-950/40 border border-emerald-500/30 text-xs text-slate-300\">\n        <strong class=\"text-emerald-300\">Fractal Paradox:</strong> Because the number of segments multiplies by 4 while shrinking in length by only 1/3, the total perimeter multiplies by 4/3 at every single step! If you continued forever, the perimeter would become infinitely long, yet the snowflake never expands beyond a small bounded circle!\n    </div>\n</div>\n",
        "takeaways": [
            "The Koch Snowflake is constructed by repeatedly replacing the middle third of every edge with two outward triangular segments.",
            "The edge count multiplies by 4 at every iteration: 3, 12, 48, 192, 768, ... (3 × 4ⁿ).",
            "It demonstrates the fractal paradox: an infinitely long perimeter enclosing a finite bounded area."
        ],
        "checkpoints": [
            {
                "id": "cp16_1",
                "question": "How many outer edges does the Koch snowflake have at Iteration 2?",
                "options": [
                    "24 edges",
                    "36 edges",
                    "48 edges",
                    "64 edges"
                ],
                "correct": 2,
                "explanation": "Iteration 0 has 3 edges; Iteration 1 has 3 × 4 = 12 edges; Iteration 2 has 12 × 4 = 48 edges."
            },
            {
                "id": "cp16_2",
                "question": "What number sequence governs the multiplication factor of edge counts in the Koch snowflake iterations?",
                "options": [
                    "Powers of 2",
                    "Powers of 3",
                    "Powers of 4 (4, 16, 64, 256, ...)",
                    "Odd numbers"
                ],
                "correct": 2,
                "explanation": "Every single segment is replaced by 4 smaller segments, causing the total segment count to multiply by powers of 4."
            }
        ]
    },
    {
        "id": 17,
        "slide_num": 17,
        "title": "Mastery Challenge 1",
        "subtitle": "Questions 1 to 10 with Solutions",
        "badge": "Challenge 1",
        "summary": "Test your mastery of number theory definitions, counting numbers, evens, odds, stepping rules, and sequence notation across 10 challenging questions.",
        "quiz_questions": [
            {
                "id": "q17_1",
                "question": "What is the primary definition of mathematics according to modern educators and mathematicians?",
                "options": [
                    "The search for patterns and the explanations of why they exist",
                    "Simply memorizing multiplication tables",
                    "Counting coins in a bank",
                    "Drawing circles with a compass"
                ],
                "correct": 0,
                "solution": "Mathematics is broadly defined as the study and search for patterns in numbers, shapes, and nature, along with the reasoning explaining why those patterns occur."
            },
            {
                "id": "q17_2",
                "question": "What is the 12th term in the sequence of counting numbers (1, 2, 3, 4, ...)?",
                "options": [
                    "10",
                    "11",
                    "12",
                    "24"
                ],
                "correct": 2,
                "solution": "The n-th term of the counting sequence is simply n. For the 12th term, it is 12."
            },
            {
                "id": "q17_3",
                "question": "What is the 15th term in the sequence of even numbers (2, 4, 6, 8, ...)?",
                "options": [
                    "28",
                    "30",
                    "32",
                    "34"
                ],
                "correct": 1,
                "solution": "The n-th even number is 2 × n. For n = 15, 2 × 15 = 30."
            },
            {
                "id": "q17_4",
                "question": "What is the 11th term in the sequence of odd numbers (1, 3, 5, 7, ...)?",
                "options": [
                    "19",
                    "21",
                    "23",
                    "25"
                ],
                "correct": 1,
                "solution": "The n-th odd number is given by 2n − 1. For n = 11, (2 × 11) − 1 = 22 − 1 = 21."
            },
            {
                "id": "q17_5",
                "question": "What is the common step difference between consecutive terms in the sequence of odd numbers?",
                "options": [
                    "+1",
                    "+2",
                    "+3",
                    "+4"
                ],
                "correct": 1,
                "solution": "In both even and odd sequences, consecutive terms differ by exactly +2 (e.g., 3 − 1 = 2, 5 − 3 = 2)."
            },
            {
                "id": "q17_6",
                "question": "What is the next term in the sequence: 5, 10, 15, 20, 25, ...?",
                "options": [
                    "28",
                    "30",
                    "35",
                    "40"
                ],
                "correct": 1,
                "solution": "The sequence consists of multiples of 5, increasing by +5 each time. 25 + 5 = 30."
            },
            {
                "id": "q17_7",
                "question": "Which branch of mathematics specializes in studying patterns among whole numbers?",
                "options": [
                    "Geometry",
                    "Number Theory",
                    "Calculus",
                    "Topology"
                ],
                "correct": 1,
                "solution": "Number Theory is the mathematical discipline dedicated to the study of whole numbers, primes, divisibility, and integer sequences."
            },
            {
                "id": "q17_8",
                "question": "What are the first five terms of the sequence given by the rule 'Start at 3 and add 4 each time'?",
                "options": [
                    "3, 7, 11, 15, 19",
                    "3, 6, 9, 12, 15",
                    "4, 7, 10, 13, 16",
                    "3, 4, 5, 6, 7"
                ],
                "correct": 0,
                "solution": "Starting at 3: 3, 3+4=7, 7+4=11, 11+4=15, 15+4=19."
            },
            {
                "id": "q17_9",
                "question": "Which of the following numbers is an even number?",
                "options": [
                    "1,357",
                    "4,892",
                    "9,999",
                    "7,653"
                ],
                "correct": 1,
                "solution": "An integer is even if its last digit is 0, 2, 4, 6, or 8. 4,892 ends in 2, so it is an even number."
            },
            {
                "id": "q17_10",
                "question": "What does the mathematical term 'ellipsis' (...) indicate in a sequence?",
                "options": [
                    "The pattern is incomplete and cannot be solved",
                    "The sequence continues forever following the established rule",
                    "Divide all terms by 3",
                    "Stop writing numbers immediately"
                ],
                "correct": 1,
                "solution": "An ellipsis (...) signifies that the sequence extends infinitely according to the same pattern."
            }
        ]
    },
    {
        "id": 18,
        "slide_num": 18,
        "title": "Mastery Challenge 2",
        "subtitle": "Questions 11 to 20 with Solutions",
        "badge": "Challenge 2",
        "summary": "Assess your skills with triangular numbers, square arrays, 3D cubes, Virahānka recurrence, and exponential doubling and tripling.",
        "quiz_questions": [
            {
                "id": "q18_1",
                "question": "What is the 6th triangular number (T₆)?",
                "options": [
                    "15",
                    "18",
                    "21",
                    "24"
                ],
                "correct": 2,
                "solution": "T₆ = 1 + 2 + 3 + 4 + 5 + 6 = 21 (or (6 × 7) / 2 = 42 / 2 = 21)."
            },
            {
                "id": "q18_2",
                "question": "What is the 9th square number (9²)?",
                "options": [
                    "18",
                    "72",
                    "81",
                    "90"
                ],
                "correct": 2,
                "solution": "9² = 9 × 9 = 81."
            },
            {
                "id": "q18_3",
                "question": "What is the 5th cube number (5³)?",
                "options": [
                    "25",
                    "75",
                    "100",
                    "125"
                ],
                "correct": 3,
                "solution": "5³ = 5 × 5 × 5 = 25 × 5 = 125."
            },
            {
                "id": "q18_4",
                "question": "What is the rule that generates the Virahānka sequence (1, 1, 2, 3, 5, 8, ...)?",
                "options": [
                    "Multiply each term by 2",
                    "Add the previous two terms together to get the next term",
                    "Add 3 each time",
                    "Multiply the previous two terms"
                ],
                "correct": 1,
                "solution": "Each term in the Virahānka sequence is the sum of the two immediately preceding terms: V_n = V_{n-1} + V_{n-2}."
            },
            {
                "id": "q18_5",
                "question": "What is the 7th term in the Virahānka sequence: 1, 1, 2, 3, 5, 8, ...?",
                "options": [
                    "11",
                    "12",
                    "13",
                    "15"
                ],
                "correct": 2,
                "solution": "5 + 8 = 13 (the 7th term is 13)."
            },
            {
                "id": "q18_6",
                "question": "What is the value of 2⁵ in the powers of 2 sequence?",
                "options": [
                    "10",
                    "16",
                    "32",
                    "64"
                ],
                "correct": 2,
                "solution": "2⁵ = 2 × 2 × 2 × 2 × 2 = 32."
            },
            {
                "id": "q18_7",
                "question": "What is the value of 3⁴ in the powers of 3 sequence?",
                "options": [
                    "12",
                    "27",
                    "81",
                    "243"
                ],
                "correct": 2,
                "solution": "3⁴ = 3 × 3 × 3 × 3 = 81."
            },
            {
                "id": "q18_8",
                "question": "Which number is both a triangular number and a square number?",
                "options": [
                    "16",
                    "25",
                    "36",
                    "49"
                ],
                "correct": 2,
                "solution": "36 is both the 8th triangular number (T₈ = 36) and the 6th square number (6² = 36)."
            },
            {
                "id": "q18_9",
                "question": "How many total pins are in a standard bowling triangular setup?",
                "options": [
                    "6",
                    "10",
                    "15",
                    "20"
                ],
                "correct": 1,
                "explanation": "A bowling pin triangle has 4 rows: 1 + 2 + 3 + 4 = 10 pins (T₄).",
                "solution": "A bowling pin triangle has 4 rows: 1 + 2 + 3 + 4 = 10 pins (T₄)."
            },
            {
                "id": "q18_10",
                "question": "What is the 3rd centered hexagonal number in the honeycomb sequence (1, 7, ...)?",
                "options": [
                    "13",
                    "15",
                    "19",
                    "21"
                ],
                "correct": 2,
                "solution": "Starting with 1, add 6 to get 7, then add 12 to get 19."
            }
        ]
    },
    {
        "id": 19,
        "slide_num": 19,
        "title": "Mastery Challenge 3",
        "subtitle": "Questions 21 to 30 with Solutions",
        "badge": "Challenge 3",
        "summary": "Verify your understanding of gnomon proofs, sums of odd numbers, mountain sums, and triangular-square mergers.",
        "quiz_questions": [
            {
                "id": "q19_1",
                "question": "What is the sum of the first 5 odd numbers: 1 + 3 + 5 + 7 + 9?",
                "options": [
                    "20",
                    "25",
                    "30",
                    "35"
                ],
                "correct": 1,
                "solution": "The sum of the first n odd numbers is n². For n = 5, 5² = 25."
            },
            {
                "id": "q19_2",
                "question": "What is the sum of the first 8 consecutive odd numbers?",
                "options": [
                    "56",
                    "64",
                    "72",
                    "80"
                ],
                "correct": 1,
                "solution": "Sum of first 8 odd numbers = 8² = 64."
            },
            {
                "id": "q19_3",
                "question": "What shape wraps around a k × k square to expand it into a (k+1) × (k+1) square?",
                "options": [
                    "A straight line",
                    "An L-shaped gnomon strip of dots",
                    "A full circle",
                    "A solid cube"
                ],
                "correct": 1,
                "solution": "An L-shaped gnomon containing 2k+1 dots wraps around a k × k square to enlarge it to (k+1) × (k+1)."
            },
            {
                "id": "q19_4",
                "question": "What is the sum of the mountain sequence: 1 + 2 + 3 + 4 + 3 + 2 + 1?",
                "options": [
                    "12",
                    "15",
                    "16 (4²)",
                    "20"
                ],
                "correct": 2,
                "solution": "A mountain sum reaching peak n equals n². Here peak is 4, so 4² = 16."
            },
            {
                "id": "q19_5",
                "question": "What is the sum of: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 6 + 5 + 4 + 3 + 2 + 1?",
                "options": [
                    "42",
                    "48",
                    "49 (7²)",
                    "56"
                ],
                "correct": 2,
                "solution": "The peak number is 7, so the sum equals 7² = 49."
            },
            {
                "id": "q19_6",
                "question": "What is always produced when you add two consecutive triangular numbers, T_{n-1} + T_n?",
                "options": [
                    "A prime number",
                    "A square number (n²)",
                    "A cube number",
                    "An odd number"
                ],
                "correct": 1,
                "solution": "Two consecutive triangular numbers always add up to a perfect square: T_{n-1} + T_n = n²."
            },
            {
                "id": "q19_7",
                "question": "If T₂ = 3 and T₃ = 6, what is their sum (T₂ + T₃)?",
                "options": [
                    "8",
                    "9 (3²)",
                    "10",
                    "12"
                ],
                "correct": 1,
                "solution": "3 + 6 = 9 = 3²."
            },
            {
                "id": "q19_8",
                "question": "If T₅ = 15 and T₆ = 21, what is their sum (T₅ + T₆)?",
                "options": [
                    "30",
                    "35",
                    "36 (6²)",
                    "42"
                ],
                "correct": 2,
                "solution": "15 + 21 = 36 = 6²."
            },
            {
                "id": "q19_9",
                "question": "How many consecutive odd numbers must be added together starting from 1 to obtain 81?",
                "options": [
                    "8 odd numbers",
                    "9 odd numbers",
                    "10 odd numbers",
                    "11 odd numbers"
                ],
                "correct": 1,
                "solution": "Since 81 = 9², exactly 9 consecutive odd numbers must be added."
            },
            {
                "id": "q19_10",
                "question": "What is 100 − 81, and what type of number is this difference?",
                "options": [
                    "19 (an odd number representing the gnomon between 9² and 10²)",
                    "20 (an even number)",
                    "17 (a prime number)",
                    "21"
                ],
                "correct": 0,
                "solution": "100 − 81 = 19, which is the 10th odd number (2 × 10 − 1 = 19)."
            }
        ]
    },
    {
        "id": 20,
        "slide_num": 20,
        "title": "Mastery Challenge 4",
        "subtitle": "Questions 31 to 40 with Solutions",
        "badge": "Challenge 4",
        "summary": "Master the final frontier: polygon dimensions, edge counts in complete graphs, handshake combinatorics, stacked pyramidal blocks, and Koch snowflake fractal powers.",
        "quiz_questions": [
            {
                "id": "q20_1",
                "question": "What is the name of a regular polygon with 6 equal sides and 6 equal interior angles?",
                "options": [
                    "Pentagon",
                    "Hexagon",
                    "Heptagon",
                    "Octagon"
                ],
                "correct": 1,
                "solution": "A 6-sided regular polygon is called a regular hexagon."
            },
            {
                "id": "q20_2",
                "question": "How many edges are in a complete graph with 3 vertices (K₃)?",
                "options": [
                    "2",
                    "3 (T₂)",
                    "4",
                    "6"
                ],
                "correct": 1,
                "solution": "Connecting all pairs of 3 vertices forms an equilateral triangle with 3 edges."
            },
            {
                "id": "q20_3",
                "question": "How many edges are in a complete graph with 5 vertices (K₅)?",
                "options": [
                    "5",
                    "8",
                    "10 (T₄)",
                    "15"
                ],
                "correct": 2,
                "solution": "In K₅, number of edges = (5 × 4) / 2 = 10 edges."
            },
            {
                "id": "q20_4",
                "question": "If 8 friends at a party all shake hands with each other once, how many handshakes take place?",
                "options": [
                    "16",
                    "24",
                    "28 (T₇)",
                    "36"
                ],
                "correct": 2,
                "solution": "Total handshakes = (8 × 7) / 2 = 56 / 2 = 28 handshakes."
            },
            {
                "id": "q20_5",
                "question": "How many total blocks are in a 4-level stacked square pyramid (1² + 2² + 3² + 4²)?",
                "options": [
                    "20",
                    "25",
                    "30",
                    "35"
                ],
                "correct": 2,
                "solution": "1 + 4 + 9 + 16 = 30 blocks."
            },
            {
                "id": "q20_6",
                "question": "How many outer edges does the Koch snowflake have at Iteration 0 (the starting equilateral triangle)?",
                "options": [
                    "1",
                    "3",
                    "4",
                    "12"
                ],
                "correct": 1,
                "solution": "Iteration 0 is a simple equilateral triangle, which has 3 edges."
            },
            {
                "id": "q20_7",
                "question": "How many outer edges does the Koch snowflake have at Iteration 1?",
                "options": [
                    "6",
                    "9",
                    "12 (3 × 4)",
                    "16"
                ],
                "correct": 2,
                "solution": "Each of the 3 edges is replaced by 4 smaller segments: 3 × 4 = 12 edges."
            },
            {
                "id": "q20_8",
                "question": "What is the edge count of the Koch snowflake at Iteration 3?",
                "options": [
                    "48",
                    "96",
                    "192 (3 × 4³)",
                    "256"
                ],
                "correct": 2,
                "solution": "3 × 4³ = 3 × 64 = 192 edges."
            },
            {
                "id": "q20_9",
                "question": "What mathematical paradox is demonstrated by the Koch snowflake fractal?",
                "options": [
                    "An infinitely long perimeter enclosing a finite area",
                    "A shape with no angles",
                    "A circle that becomes a square",
                    "Zero perimeter with infinite area"
                ],
                "correct": 0,
                "solution": "The Koch snowflake's perimeter multiplies by 4/3 at every step, growing to infinity, while remaining enclosed within a finite circle."
            },
            {
                "id": "q20_10",
                "question": "Which number sequence corresponds to the number of edges in complete graphs K₂, K₃, K₄, K₅, ...?",
                "options": [
                    "Square numbers (1, 4, 9, 16, ...)",
                    "Triangular numbers (1, 3, 6, 10, 15, ...)",
                    "Cube numbers (1, 8, 27, 64, ...)",
                    "Powers of 2 (2, 4, 8, 16, ...)"
                ],
                "correct": 1,
                "solution": "The edge counts of complete graphs are exactly the triangular numbers: 1, 3, 6, 10, 15, ..."
            }
        ]
    }
]
