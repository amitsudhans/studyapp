import json
import sys

def build_data():
    CHAPTER_META = {
        "chapter_num": 5,
        "title": "Primes",
        "subtitle": "NCERT Class 6 Mathematics • Chapter 5 Interactive Master Laboratory",
        "mentors": "Eratosthenes of Cyrene & Euclid of Alexandria",
        "mentors_title": "Pioneers of Prime Sifting & The Fundamental Theorem of Arithmetic",
        "badge": "Ganita Prakash • Number Theory & Divisibility",
        "total_slides": 20,
        "checkpoints_count": 32,
        "quiz_questions_count": 40
    }

    SLIDES = [
        # Slide 1: 5.1 Multiples & The Idli-Vada Game
        {
            "id": 1,
            "slide_num": 1,
            "title": "Multiples",
            "subtitle": "Counting Steps, Multiples & Common Multiples",
            "badge": "5.1 Common Multiples",
            "summary": "Multiples arise when we multiply a number by whole counting numbers 1, 2, 3, ... In the classic classroom game, counting numbers divisible by 3 call 'Idli', numbers divisible by 5 call 'Vada', and numbers divisible by both (common multiples like 15, 30, 45) call 'Idli-Vada'!",
            "theory": """
                <h4 class="text-sm font-bold text-amber-300 mb-1">What is a Multiple?</h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-2">
                    A <strong>multiple</strong> of a number is formed by multiplying that number by natural counting numbers: 1, 2, 3, 4, 5, ...
                    For instance:
                </p>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs mb-3">
                    <div class="p-2.5 rounded-lg bg-amber-950/40 border border-amber-500/30">
                        <span class="font-bold text-amber-300 block mb-0.5">Multiples of 3 ('Idli'):</span>
                        <span class="font-mono text-slate-200">3, 6, 9, 12, 15, 18, 21, 24, 27, 30, ...</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-cyan-950/40 border border-cyan-500/30">
                        <span class="font-bold text-cyan-300 block mb-0.5">Multiples of 5 ('Vada'):</span>
                        <span class="font-mono text-slate-200">5, 10, 15, 20, 25, 30, 35, 40, ...</span>
                    </div>
                </div>
                <h4 class="text-sm font-bold text-emerald-300 mb-1">Common Multiples: The 'Idli-Vada' Moments</h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-2">
                    When a number appears in <em>both</em> lists simultaneously, it is a <strong>common multiple</strong>.
                    For 3 and 5, the first common multiple is <strong>15</strong>. The subsequent ones are exact multiples of 15:
                    <span class="font-mono text-emerald-300 font-bold">15, 30, 45, 60, 75, ...</span>
                </p>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-700/80 text-xs text-slate-300">
                    <strong class="text-amber-400">Lowest Common Multiple (LCM):</strong>
                    The smallest non-zero common multiple between two numbers is called their LCM. For 3 and 5, <strong>LCM(3, 5) = 15</strong>.
                </div>
            """,
            "checkpoints": [
                {
                    "id": "cp_1_1",
                    "question": "In the Idli-Vada game (3 = Idli, 5 = Vada), what call must a student make on reaching number 45?",
                    "options": [
                        "Idli",
                        "Vada",
                        "Idli-Vada",
                        "Silent Pass"
                    ],
                    "correct": 2,
                    "explanation": "Since 45 is divisible by both 3 (3 × 15 = 45) and 5 (5 × 9 = 45), 45 is a common multiple and triggers 'Idli-Vada'!"
                },
                {
                    "id": "cp_1_2",
                    "question": "What is the smallest non-zero common multiple of 4 and 6?",
                    "options": [
                        "24",
                        "12",
                        "2",
                        "16"
                    ],
                    "correct": 1,
                    "explanation": "Multiples of 4 are 4, 8, 12, 16... Multiples of 6 are 6, 12, 18... The very first common number is 12, so LCM(4, 6) = 12."
                }
            ]
        },

        # Slide 2: 5.1 Venn Diagrams & Common Multiples
        {
            "id": 2,
            "slide_num": 2,
            "title": "Venn Multiples",
            "subtitle": "Venn Diagrams & Intersection of Multiples",
            "badge": "5.1 Visualising Sets",
            "summary": "Overlapping circles (Venn diagrams) provide a geometric window into commonality. Placing multiples of one number in circle A and multiples of another in circle B reveals that the shared overlapping football region contains their common multiples.",
            "theory": """
                <h4 class="text-sm font-bold text-amber-300 mb-1">Visualizing Shared Membership</h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-2">
                    Imagine two large circular hoops placed on the floor:
                </p>
                <ul class="list-disc list-inside text-xs text-slate-300 space-y-1 mb-3">
                    <li><strong class="text-cyan-300">Left Circle (A):</strong> Holds numbers divisible by 4 (4, 8, 16, 20, 28, ...).</li>
                    <li><strong class="text-amber-300">Right Circle (B):</strong> Holds numbers divisible by 6 (6, 18, 30, 42, ...).</li>
                    <li><strong class="text-emerald-300">Intersection (Overlap A ∩ B):</strong> Holds numbers divisible by <em>both</em> 4 and 6!</li>
                </ul>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80 mb-2">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">Numbers in the Overlap Region:</span>
                    <p class="text-xs font-mono text-slate-200">
                        12, 24, 36, 48, 60, 72, ...
                    </p>
                    <p class="text-[11px] text-slate-400 mt-1">
                        Notice how the numbers in the intersection are themselves multiples of 12! The smallest element in this intersection is the <strong>LCM</strong>.
                    </p>
                </div>
            """,
            "checkpoints": [
                {
                    "id": "cp_2_1",
                    "question": "If circle X contains multiples of 2 and circle Y contains multiples of 3, which numbers belong strictly in the overlapping center?",
                    "options": [
                        "All odd numbers",
                        "Multiples of 6 (6, 12, 18, 24...)",
                        "Multiples of 5",
                        "Only the number 1"
                    ],
                    "correct": 1,
                    "explanation": "Any number divisible by both 2 and 3 must be a multiple of 2 × 3 = 6. They belong in the intersection."
                },
                {
                    "id": "cp_2_2",
                    "question": "Can an odd number ever appear in the overlap between multiples of 4 and multiples of 7?",
                    "options": [
                        "Yes, every alternate multiple is odd",
                        "No, because any multiple of 4 is inherently even",
                        "Yes, 28 is odd",
                        "Only if the number is greater than 100"
                    ],
                    "correct": 1,
                    "explanation": "Because 4 is even, every multiple of 4 is even. Therefore, every common multiple of 4 and 7 must be even (28, 56, 84...)."
                }
            ]
        },

        # Slide 3: 5.1 Factors & Jump Jackpot
        {
            "id": 3,
            "slide_num": 3,
            "title": "Factors",
            "subtitle": "Exact Divisors & Common Jump Sizes",
            "badge": "5.1 Factors",
            "summary": "A factor is an exact divisor that divides a number completely with zero remainder. In the Jump Jackpot game, jumping in step sizes of k lands on target number N if and only if k is a factor of N! Common factors are step sizes that land on two targets simultaneously.",
            "theory": """
                <h4 class="text-sm font-bold text-amber-300 mb-1">What is a Factor?</h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-2">
                    A number <strong>k</strong> is a <strong>factor</strong> of <strong>N</strong> if <strong>N ÷ k</strong> leaves no remainder.
                    In other words, you can multiply <em>k</em> by another whole number to obtain <em>N</em>.
                </p>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs mb-3">
                    <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-700">
                        <span class="font-bold text-amber-300 block mb-0.5">Factors of 12 (Target A):</span>
                        <span class="font-mono text-slate-200">1, 2, 3, 4, 6, 12</span>
                        <span class="text-[10px] text-slate-400 block mt-1">(Total 6 factors)</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-700">
                        <span class="font-bold text-cyan-300 block mb-0.5">Factors of 18 (Target B):</span>
                        <span class="font-mono text-slate-200">1, 2, 3, 6, 9, 18</span>
                        <span class="text-[10px] text-slate-400 block mt-1">(Total 6 factors)</span>
                    </div>
                </div>
                <h4 class="text-sm font-bold text-emerald-300 mb-1">Common Factors & Highest Common Factor (HCF)</h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-2">
                    The jump sizes that land successfully on <em>both</em> 12 and 18 are:
                    <span class="font-mono text-emerald-300 font-bold">1, 2, 3, 6</span>.
                    The greatest of these common jump sizes is <strong>6</strong>, known as the <strong>Highest Common Factor (HCF)</strong> or <strong>Greatest Common Divisor (GCD)</strong>:
                    <strong>HCF(12, 18) = 6</strong>.
                </p>
            """,
            "checkpoints": [
                {
                    "id": "cp_3_1",
                    "question": "Which of the following step sizes will land on both 20 and 30 starting from 0?",
                    "options": [
                        "Jump size 4",
                        "Jump size 6",
                        "Jump size 5",
                        "Jump size 15"
                    ],
                    "correct": 2,
                    "explanation": "5 divides both 20 (5 × 4 = 20) and 30 (5 × 6 = 30) exactly with zero remainder. 4 divides 20 but not 30; 6 and 15 divide 30 but not 20."
                },
                {
                    "id": "cp_3_2",
                    "question": "What is the Highest Common Factor (HCF) of 15 and 25?",
                    "options": [
                        "1",
                        "3",
                        "5",
                        "75"
                    ],
                    "correct": 2,
                    "explanation": "Factors of 15 are {1, 3, 5, 15}. Factors of 25 are {1, 5, 25}. The common factors are {1, 5}, and the greatest is 5."
                }
            ]
        },

        # Slide 4: 5.1 Perfect Numbers
        {
            "id": 4,
            "slide_num": 4,
            "title": "Perfect Numbers",
            "subtitle": "When Proper Divisors Sum to the Whole",
            "badge": "5.1 Special Numbers",
            "summary": "A perfect number is a positive integer whose proper positive factors (all factors excluding the number itself) add up exactly to the number. Equivalently, the sum of all its factors equals twice the number!",
            "theory": """
                <h4 class="text-sm font-bold text-amber-300 mb-1">The Magic of 6 and 28</h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-2">
                    In ancient Greek mathematics, numbers whose parts add up harmoniously to themselves were celebrated as <strong>Perfect Numbers</strong>:
                </p>
                <div class="space-y-2 text-xs mb-3">
                    <div class="p-2.5 rounded-lg bg-amber-950/40 border border-amber-500/30">
                        <span class="font-bold text-amber-300 block mb-0.5">The First Perfect Number: 6</span>
                        <span class="font-mono text-slate-200">Factors of 6: 1, 2, 3, 6</span><br>
                        <span class="text-slate-300">Sum of proper factors: 1 + 2 + 3 = <strong>6</strong>!</span><br>
                        <span class="text-emerald-400 font-bold">Sum of all factors: 1 + 2 + 3 + 6 = 12 = 2 × 6.</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-cyan-950/40 border border-cyan-500/30">
                        <span class="font-bold text-cyan-300 block mb-0.5">The Second Perfect Number: 28</span>
                        <span class="font-mono text-slate-200">Factors of 28: 1, 2, 4, 7, 14, 28</span><br>
                        <span class="text-slate-300">Sum of proper factors: 1 + 2 + 4 + 7 + 14 = <strong>28</strong>!</span><br>
                        <span class="text-emerald-400 font-bold">Sum of all factors: 28 + 28 = 56 = 2 × 28.</span>
                    </div>
                </div>
                <p class="text-xs text-slate-400">
                    The next perfect number is <strong>496</strong>, followed by <strong>8128</strong>! All known perfect numbers are even.
                </p>
            """,
            "checkpoints": [
                {
                    "id": "cp_4_1",
                    "question": "What is the sum of all the factors of the perfect number 6?",
                    "options": [
                        "6",
                        "12",
                        "10",
                        "18"
                    ],
                    "correct": 1,
                    "explanation": "Factors of 6 are 1, 2, 3, and 6. Their sum is 1 + 2 + 3 + 6 = 12, which is exactly 2 × 6!"
                },
                {
                    "id": "cp_4_2",
                    "question": "Is the number 10 a perfect number? (Proper factors: 1, 2, 5)",
                    "options": [
                        "Yes, because 1 + 2 + 5 = 10",
                        "No, because 1 + 2 + 5 = 8 (which is less than 10)",
                        "Yes, because 10 is an even number",
                        "No, because 10 is prime"
                    ],
                    "correct": 1,
                    "explanation": "The proper divisors of 10 are 1, 2, and 5. Their sum is 1 + 2 + 5 = 8, not 10. Therefore, 10 is deficient, not perfect."
                }
            ]
        },

        # Slide 5: 5.2 Prime vs Composite (Fig Packing)
        {
            "id": 5,
            "slide_num": 5,
            "title": "Primes & Composites",
            "subtitle": "Rectangular Arrays & Fig Packing",
            "badge": "5.2 Building Blocks",
            "summary": "If you have N objects (such as freshly picked figs), can you arrange them in a filled rectangular array with more than 1 row? If the only possible arrangement is a single long line of 1 × N, the number is Prime! If multiple rectangles can be formed, it is Composite.",
            "theory": """
                <h4 class="text-sm font-bold text-amber-300 mb-1">Arranging Objects into Rectangles</h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-2">
                    Every factor pair (a × b = N) corresponds to a rectangular grid of width <em>a</em> and height <em>b</em>:
                </p>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs mb-3">
                    <div class="p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-500/30">
                        <span class="font-bold text-emerald-300 block mb-0.5">Prime: Only 1 Rectangle</span>
                        <p class="text-slate-300 mb-1">Try packing <strong>7 figs</strong>:</p>
                        <p class="font-mono text-slate-200">Only 1 × 7 (or 7 × 1) possible!</p>
                        <span class="text-[11px] text-emerald-400">Primes have EXACTLY two factors: 1 and itself.</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-cyan-950/40 border border-cyan-500/30">
                        <span class="font-bold text-cyan-300 block mb-0.5">Composite: Multiple Rectangles</span>
                        <p class="text-slate-300 mb-1">Try packing <strong>6 figs</strong>:</p>
                        <p class="font-mono text-slate-200">1 × 6 or 2 × 3 grids!</p>
                        <span class="text-[11px] text-cyan-400">Composites have MORE than two factors.</span>
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-rose-950/40 border border-rose-500/30 text-xs">
                    <strong class="text-rose-400">Crucial Rule for the Number 1:</strong>
                    The number <strong>1</strong> has only 1 factor (itself). A prime must have <em>strictly two distinct factors</em>.
                    Therefore, <strong>1 is neither prime nor composite</strong>!
                </div>
            """,
            "checkpoints": [
                {
                    "id": "cp_5_1",
                    "question": "How many factors does a prime number have?",
                    "options": [
                        "Only 1 factor",
                        "Exactly 2 factors (1 and itself)",
                        "3 or more factors",
                        "An infinite number of factors"
                    ],
                    "correct": 1,
                    "explanation": "By definition, a prime number has exactly two positive factors: 1 and the number itself."
                },
                {
                    "id": "cp_5_2",
                    "question": "Why is the number 1 classified as neither prime nor composite?",
                    "options": [
                        "Because it is an odd number",
                        "Because it has only one positive factor (itself), failing the definition of both",
                        "Because it is the largest number",
                        "Because it cannot be multiplied"
                    ],
                    "correct": 1,
                    "explanation": "Primes must have exactly two distinct factors; composites must have more than two factors. 1 has only one factor (1), so it belongs to neither group."
                }
            ]
        },

        # Slide 6: 5.2 The Sieve of Eratosthenes
        {
            "id": 6,
            "slide_num": 6,
            "title": "Prime Sieve",
            "subtitle": "The Ancient Grid Filter for Primes up to 100",
            "badge": "5.2 Sifting Primes",
            "summary": "Around 240 BCE, Greek mathematician Eratosthenes created a systematic algorithm to filter out all composite numbers up to 100. By crossing out 1, then circling 2 and crossing its multiples, circling 3 and crossing its multiples, and repeating for 5 and 7, exactly 25 primes emerge untouched!",
            "theory": """
                <h4 class="text-sm font-bold text-amber-300 mb-1">How the Ancient Sieve Works</h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-2">
                    Write all numbers from 1 to 100 in a 10 × 10 grid:
                </p>
                <ol class="list-decimal list-inside text-xs text-slate-300 space-y-1 mb-3">
                    <li>Cross out <strong>1</strong> (neither prime nor composite).</li>
                    <li>Circle <strong>2</strong> (the only even prime!), cross out all other multiples of 2 (4, 6, 8, ...).</li>
                    <li>Circle <strong>3</strong>, cross out all remaining multiples of 3 (9, 15, 21, ...).</li>
                    <li>Circle <strong>5</strong>, cross out all remaining multiples of 5 (25, 35, 55, ...).</li>
                    <li>Circle <strong>7</strong>, cross out all remaining multiples of 7 (49, 77, 91).</li>
                </ol>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80 text-xs text-slate-200">
                    <span class="text-amber-400 font-bold block mb-1">Stop Criterion: √100 = 10!</span>
                    Since every composite up to 100 must have at least one prime factor ≤ 10 (namely 2, 3, 5, or 7),
                    all uncrossed numbers remaining on the grid are guaranteed to be <strong>Primes</strong>!
                    There are exactly <strong>25 primes</strong> between 1 and 100.
                </div>
            """,
            "checkpoints": [
                {
                    "id": "cp_6_1",
                    "question": "How many prime numbers exist between 1 and 100?",
                    "options": [
                        "20 primes",
                        "25 primes",
                        "30 primes",
                        "50 primes"
                    ],
                    "correct": 1,
                    "explanation": "There are exactly 25 prime numbers between 1 and 100: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97."
                },
                {
                    "id": "cp_6_2",
                    "question": "What is the only even prime number in the entire universe of numbers?",
                    "options": [
                        "0",
                        "2",
                        "4",
                        "6"
                    ],
                    "correct": 1,
                    "explanation": "2 is the only even prime number. Every other even number is divisible by 2 and therefore composite."
                }
            ]
        },

        # Slide 7: 5.2 Twin Primes & Variations
        {
            "id": 7,
            "slide_num": 7,
            "title": "Twin Primes",
            "subtitle": "Prime Neighbors with a Difference of 2",
            "badge": "5.2 Prime Families",
            "summary": "Twin primes are pairs of prime numbers that differ by exactly 2. Famous pairs like (3, 5), (11, 13), and (17, 19) sit on either side of an even number. Patterns like Sophie Germain primes (doubling a prime and adding 1) open windows into modern cryptography.",
            "theory": """
                <h4 class="text-sm font-bold text-amber-300 mb-1">What are Twin Primes?</h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-2">
                    Two prime numbers are called <strong>Twin Primes</strong> if their difference is exactly 2:
                    <span class="font-mono text-amber-300 font-bold">p₂ − p₁ = 2</span>.
                </p>
                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs mb-3 font-mono text-center">
                    <div class="p-2 rounded bg-slate-900 border border-slate-700">(3, 5)</div>
                    <div class="p-2 rounded bg-slate-900 border border-slate-700">(5, 7)</div>
                    <div class="p-2 rounded bg-slate-900 border border-slate-700">(11, 13)</div>
                    <div class="p-2 rounded bg-slate-900 border border-slate-700">(17, 19)</div>
                    <div class="p-2 rounded bg-slate-900 border border-slate-700">(29, 31)</div>
                    <div class="p-2 rounded bg-slate-900 border border-slate-700">(41, 43)</div>
                    <div class="p-2 rounded bg-slate-900 border border-slate-700">(59, 61)</div>
                    <div class="p-2 rounded bg-slate-900 border border-slate-700">(71, 73)</div>
                </div>
                <h4 class="text-sm font-bold text-cyan-300 mb-1">Doubling a Prime and Adding 1 (2p + 1)</h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-2">
                    If <em>p</em> is prime and <strong>2p + 1</strong> is also prime, <em>p</em> is called a <strong>Sophie Germain prime</strong>:
                </p>
                <p class="text-xs font-mono text-slate-200">
                    p = 2 → 2(2) + 1 = 5 (Prime!)<br>
                    p = 3 → 2(3) + 1 = 7 (Prime!)<br>
                    p = 5 → 2(5) + 1 = 11 (Prime!)
                </p>
            """,
            "checkpoints": [
                {
                    "id": "cp_7_1",
                    "question": "Which of the following pairs is NOT a pair of twin primes?",
                    "options": [
                        "(11, 13)",
                        "(17, 19)",
                        "(7, 9)",
                        "(41, 43)"
                    ],
                    "correct": 2,
                    "explanation": "Although 9 − 7 = 2, 9 is not a prime number (9 = 3 × 3 is composite). Both numbers must be prime!"
                },
                {
                    "id": "cp_7_2",
                    "question": "Notice that between any twin prime pair (except (3,5)), the middle number is always divisible by:",
                    "options": [
                        "4",
                        "6",
                        "8",
                        "10"
                    ],
                    "correct": 1,
                    "explanation": "For twin primes like (5, 6, 7), (11, 12, 13), (17, 18, 19), (29, 30, 31), the sandwiched number between them is always a multiple of 6!"
                }
            ]
        },

        # Slide 8: 5.3 Co-prime Numbers for Safekeeping Treasures
        {
            "id": 8,
            "slide_num": 8,
            "title": "Co-primes",
            "subtitle": "Safekeeping Treasures & Mutual Independence",
            "badge": "5.3 Co-primes",
            "summary": "Two numbers are co-prime (or relatively prime) if their ONLY common factor is 1. Neither number has to be prime on its own! For instance, 4 and 9 are both composite, yet they share no common factor other than 1, making them co-prime partners.",
            "theory": """
                <h4 class="text-sm font-bold text-amber-300 mb-1">Definition of Co-prime Numbers</h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-2">
                    Two whole numbers <strong>a</strong> and <strong>b</strong> are called <strong>co-prime</strong> if:
                    <span class="font-mono text-emerald-300 font-bold block my-1">HCF(a, b) = 1</span>
                    They share no common divisors greater than 1.
                </p>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80 mb-3 text-xs">
                    <span class="font-bold text-cyan-300 block mb-1">Surprising Fact: Both Can Be Composite!</span>
                    <p class="text-slate-300 mb-1">Consider <strong>4</strong> and <strong>9</strong>:</p>
                    <ul class="list-disc list-inside text-slate-300 space-y-0.5">
                        <li>Factors of 4: {1, 2, 4} (Composite)</li>
                        <li>Factors of 9: {1, 3, 9} (Composite)</li>
                        <li>Common Factors: <strong>{1}</strong> only!</li>
                    </ul>
                    <span class="text-emerald-400 font-bold block mt-1">Therefore, 4 and 9 are CO-PRIME!</span>
                </div>
                <div class="p-2.5 rounded-lg bg-amber-950/40 border border-amber-500/30 text-xs">
                    <strong class="text-amber-300">Consecutive Numbers Rule:</strong>
                    Any two consecutive counting numbers (like 14 and 15, or 99 and 100) are ALWAYS co-prime!
                </div>
            """,
            "checkpoints": [
                {
                    "id": "cp_8_1",
                    "question": "Which of the following pairs of numbers is co-prime?",
                    "options": [
                        "6 and 9",
                        "8 and 15",
                        "14 and 21",
                        "10 and 25"
                    ],
                    "correct": 1,
                    "explanation": "Factors of 8 are {1, 2, 4, 8}; factors of 15 are {1, 3, 5, 15}. Their only common factor is 1, so 8 and 15 are co-prime."
                },
                {
                    "id": "cp_8_2",
                    "question": "Can two composite numbers be co-prime to each other?",
                    "options": [
                        "Never, composite numbers always share prime factors",
                        "Yes, as long as they don't share any prime factors (e.g., 8 and 9)",
                        "Only if one of them is 1",
                        "Only if their sum is 100"
                    ],
                    "correct": 1,
                    "explanation": "Yes! 8 (2×2×2) and 9 (3×3) are both composite, but they share no common prime factor, so HCF(8, 9) = 1."
                }
            ]
        },

        # Slide 9: 5.3 Thread-Art Peg Star Patterns
        {
            "id": 9,
            "slide_num": 9,
            "title": "Peg Stars",
            "subtitle": "Geometry of Co-primes & Continuous Star Polygons",
            "badge": "5.3 Geometric Patterns",
            "summary": "Arrange N pegs around a circular board and connect them with thread jumping by a gap of k pegs each time. If N and k are co-prime, the thread visits every single peg in one unbroken continuous loop! If they share a common factor, the thread closes prematurely into a subset polygon.",
            "theory": """
                <h4 class="text-sm font-bold text-amber-300 mb-1">The Thread-and-Peg Experiment</h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-2">
                    Imagine <strong>N = 8 pegs</strong> numbered 0 to 7 around a circular ring:
                </p>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs mb-3">
                    <div class="p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-500/30">
                        <span class="font-bold text-emerald-300 block mb-0.5">Step k = 3: Co-prime! (HCF(8, 3) = 1)</span>
                        <p class="text-slate-300 mb-1">Path: 0 → 3 → 6 → 1 → 4 → 7 → 2 → 5 → 0.</p>
                        <span class="text-[11px] text-emerald-400 font-bold">All 8 pegs visited in ONE continuous 8-pointed star!</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-rose-950/40 border border-rose-500/30">
                        <span class="font-bold text-rose-300 block mb-0.5">Step k = 2: Not Co-prime! (HCF(8, 2) = 2)</span>
                        <p class="text-slate-300 mb-1">Path: 0 → 2 → 4 → 6 → 0.</p>
                        <span class="text-[11px] text-rose-400 font-bold">Trapped in a 4-peg square! Only visits 4 pegs.</span>
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-700/80 text-xs text-slate-300">
                    <strong class="text-amber-400">Mathematical Principle:</strong>
                    A thread wraps through all <em>N</em> pegs in a single cycle if and only if the step size <em>k</em> is <strong>co-prime to N</strong>.
                </div>
            """,
            "checkpoints": [
                {
                    "id": "cp_9_1",
                    "question": "On a circular board with 10 pegs, connecting every 3rd peg (k = 3) will:",
                    "options": [
                        "Get stuck after 3 pegs",
                        "Form a triangle",
                        "Visit all 10 pegs in a single continuous star because HCF(10, 3) = 1",
                        "Visit only the even pegs"
                    ],
                    "correct": 2,
                    "explanation": "Since 10 and 3 are co-prime (HCF = 1), the thread will cycle through all 10 pegs before returning to the start peg."
                },
                {
                    "id": "cp_9_2",
                    "question": "If you have 12 pegs and jump with step size k = 4, how many pegs will be visited before returning to peg 0?",
                    "options": [
                        "12 pegs",
                        "3 pegs (0, 4, 8, then back to 0)",
                        "4 pegs",
                        "6 pegs"
                    ],
                    "correct": 1,
                    "explanation": "Since HCF(12, 4) = 4, the loop length is 12 ÷ 4 = 3 pegs (an equilateral triangle: pegs 0, 4, and 8)."
                }
            ]
        },

        # Slide 10: 5.3 First Common Multiple Theorem
        {
            "id": 10,
            "slide_num": 10,
            "title": "Co-prime LCM",
            "subtitle": "The Direct Product Property of Co-prime Numbers",
            "badge": "5.3 Multiples of Co-primes",
            "summary": "When two numbers are co-prime, they share no internal prime factors. As a consequence, their very first common multiple (LCM) is equal to their direct product: LCM(a, b) = a × b. This rule provides a vital shortcut in algebra and fractions.",
            "theory": """
                <h4 class="text-sm font-bold text-amber-300 mb-1">Direct Product Theorem</h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-2">
                    For any two co-prime numbers <em>a</em> and <em>b</em>:
                    <span class="font-mono text-emerald-300 font-bold block my-1">LCM(a, b) = a × b</span>
                </p>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs mb-3">
                    <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-700">
                        <span class="font-bold text-amber-300 block mb-0.5">Example 1: 5 and 7</span>
                        <p class="text-slate-300">5 and 7 are co-prime.</p>
                        <p class="font-mono text-slate-200">LCM(5, 7) = 5 × 7 = <strong>35</strong>.</p>
                        <span class="text-[10px] text-slate-400">No smaller positive number is divisible by both.</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-700">
                        <span class="font-bold text-cyan-300 block mb-0.5">Example 2: 4 and 9</span>
                        <p class="text-slate-300">4 and 9 are co-prime.</p>
                        <p class="font-mono text-slate-200">LCM(4, 9) = 4 × 9 = <strong>36</strong>.</p>
                        <span class="text-[10px] text-slate-400">Smallest number in both multiple lists.</span>
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-amber-950/40 border border-amber-500/30 text-xs text-slate-300">
                    <strong class="text-amber-400">General Product Formula:</strong>
                    For any two positive numbers: <span class="font-mono font-bold text-slate-100">HCF(a, b) × LCM(a, b) = a × b</span>.
                    When HCF = 1, this simplifies directly to <span class="font-mono text-emerald-300">LCM = a × b</span>!
                </div>
            """,
            "checkpoints": [
                {
                    "id": "cp_10_1",
                    "question": "What is the lowest common multiple (LCM) of the co-prime pair 8 and 9?",
                    "options": [
                        "17",
                        "36",
                        "72",
                        "1"
                    ],
                    "correct": 2,
                    "explanation": "Since 8 and 9 are co-prime (HCF = 1), their LCM is simply their direct product: 8 × 9 = 72."
                },
                {
                    "id": "cp_10_2",
                    "question": "If two numbers have HCF = 5 and product = 150, what is their LCM?",
                    "options": [
                        "15",
                        "30",
                        "50",
                        "750"
                    ],
                    "correct": 1,
                    "explanation": "Using HCF × LCM = Product, we have 5 × LCM = 150, so LCM = 150 ÷ 5 = 30."
                }
            ]
        },

        # Slide 11: 5.4 Prime Factorisation Trees
        {
            "id": 11,
            "slide_num": 11,
            "title": "Factor Trees",
            "subtitle": "Breaking Down Composites to Prime Leaves",
            "badge": "5.4 Factorisation",
            "summary": "Every composite number can be broken down step-by-step into smaller factors until every branch ends in an indivisible prime leaf. Whether you break 56 as 7 × 8 or 2 × 28, the final prime leaves are always identical: 2 × 2 × 2 × 7!",
            "theory": """
                <h4 class="text-sm font-bold text-amber-300 mb-1">Constructing a Factor Tree</h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-2">
                    To find the prime factorisation of <strong>56</strong>, pick any two factors to start:
                </p>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs mb-3">
                    <div class="p-2.5 rounded-lg bg-amber-950/40 border border-amber-500/30">
                        <span class="font-bold text-amber-300 block mb-0.5">Path 1: Starting with 7 × 8</span>
                        <p class="font-mono text-slate-200">56 = 7 × 8</p>
                        <p class="font-mono text-slate-300">8 = 2 × 4 = 2 × 2 × 2</p>
                        <span class="text-emerald-400 font-bold block mt-1">Leaves: 2 × 2 × 2 × 7</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-cyan-950/40 border border-cyan-500/30">
                        <span class="font-bold text-cyan-300 block mb-0.5">Path 2: Starting with 2 × 28</span>
                        <p class="font-mono text-slate-200">56 = 2 × 28</p>
                        <p class="font-mono text-slate-300">28 = 2 × 14 = 2 × 2 × 7</p>
                        <span class="text-emerald-400 font-bold block mt-1">Leaves: 2 × 2 × 2 × 7</span>
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-700/80 text-xs text-slate-300">
                    <strong class="text-amber-400">Exponential Notation:</strong>
                    We write repeated prime factors compactly using powers:
                    <span class="font-mono font-bold text-emerald-300">56 = 2³ × 7</span>.
                </div>
            """,
            "checkpoints": [
                {
                    "id": "cp_11_1",
                    "question": "What is the prime factorisation of 36?",
                    "options": [
                        "4 × 9",
                        "2 × 18",
                        "2 × 2 × 3 × 3 (or 2² × 3²)",
                        "6 × 6"
                    ],
                    "correct": 2,
                    "explanation": "Prime factorisation requires ALL factors to be prime numbers. 4, 9, 18, and 6 are composite. Only 2² × 3² consists solely of primes."
                },
                {
                    "id": "cp_11_2",
                    "question": "If a factor tree for 60 branches into 6 × 10, what are the final prime leaves?",
                    "options": [
                        "6 and 10",
                        "2, 3, 2, 5 (or 2² × 3 × 5)",
                        "2, 3, 10",
                        "5, 12"
                    ],
                    "correct": 1,
                    "explanation": "6 breaks into 2 × 3, and 10 breaks into 2 × 5. Gathering all leaves gives 2 × 2 × 3 × 5 = 2² × 3 × 5 = 60."
                }
            ]
        },

        # Slide 12: 5.4 Fundamental Theorem of Arithmetic
        {
            "id": 12,
            "slide_num": 12,
            "title": "Prime DNA",
            "subtitle": "Uniqueness of Prime Factorisation",
            "badge": "5.4 Prime DNA",
            "summary": "The Fundamental Theorem of Arithmetic states that every whole number greater than 1 can be represented as a product of prime numbers in EXACTLY one way, apart from the order in which the factors are written. Primes are the unique atomic DNA of numbers!",
            "theory": """
                <h4 class="text-sm font-bold text-amber-300 mb-1">Euclid's Master Theorem</h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-2">
                    In ancient Alexandria, Euclid proved that prime factorisation is <strong>unique</strong>:
                </p>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80 mb-3 text-xs">
                    <p class="text-slate-200 leading-relaxed">
                        <em>Every integer n > 1 can be factored into primes uniquely, up to the rearrangement of terms.</em>
                    </p>
                    <p class="text-amber-400 font-mono mt-1 font-bold">
                        12 = 2 × 2 × 3 = 2 × 3 × 2 = 3 × 2 × 2
                    </p>
                    <p class="text-[11px] text-slate-400 mt-1">
                        Due to the commutative and associative laws of multiplication, the order does not matter: it always contains exactly two 2s and one 3!
                    </p>
                </div>
                <h4 class="text-sm font-bold text-emerald-300 mb-1">Co-primes Through Prime Factorisation</h4>
                <p class="text-xs text-slate-300 leading-relaxed">
                    Two numbers are co-prime <strong>if and only if</strong> they share zero common prime factors in their prime factorisations!
                    For example, 15 = 3 × 5 and 28 = 2² × 7 share no common prime, so they are co-prime.
                </p>
            """,
            "checkpoints": [
                {
                    "id": "cp_12_1",
                    "question": "Can a composite number possess two fundamentally different sets of prime factors?",
                    "options": [
                        "Yes, depending on whether you start with big or small numbers",
                        "No, the Fundamental Theorem guarantees the prime factors are always unique",
                        "Only if the number is greater than 1,000",
                        "Yes, even numbers have multiple factor sets"
                    ],
                    "correct": 1,
                    "explanation": "No matter which factorisation route or tree you follow, the final collection of prime factors is strictly unique (The Fundamental Theorem of Arithmetic)."
                },
                {
                    "id": "cp_12_2",
                    "question": "Using prime factorisation, determine if 20 (2² × 5) and 21 (3 × 7) are co-prime:",
                    "options": [
                        "No, because both are composite",
                        "Yes, because their prime factor sets {2, 5} and {3, 7} share no common primes",
                        "No, because 20 is even and 21 is odd",
                        "Cannot be determined without division"
                    ],
                    "correct": 1,
                    "explanation": "Since 20 has prime factors {2, 5} and 21 has {3, 7}, their intersection is empty. Hence HCF = 1 and they are co-prime!"
                }
            ]
        },

        # Slide 13: 5.4 Divisibility via Factor Containment
        {
            "id": 13,
            "slide_num": 13,
            "title": "Factor Subsets",
            "subtitle": "Testing Divisibility via Prime Subsets",
            "badge": "5.4 Divisibility Insights",
            "summary": "A number A is divisible by another number B if and only if the complete prime factorisation of B is entirely contained within the prime factorisation of A. If B requires factors that A lacks, A cannot be divisible by B!",
            "theory": """
                <h4 class="text-sm font-bold text-amber-300 mb-1">The Prime Ingredient Test</h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-2">
                    Think of prime factors as ingredients needed to bake a number.
                    To divide <strong>A by B</strong>, the pantry of <strong>A</strong> must contain all the prime ingredients of <strong>B</strong>:
                </p>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs mb-3">
                    <div class="p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-500/30">
                        <span class="font-bold text-emerald-300 block mb-0.5">Case 1: Divisible!</span>
                        <p class="text-slate-300">Is <strong>84</strong> divisible by <strong>14</strong>?</p>
                        <p class="font-mono text-slate-200">84 = 2 × 2 × 3 × 7</p>
                        <p class="font-mono text-slate-200">14 = 2 × 7</p>
                        <span class="text-emerald-400 font-bold block mt-1">Both '2' and '7' are inside 84! ✓</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-rose-950/40 border border-rose-500/30">
                        <span class="font-bold text-rose-300 block mb-0.5">Case 2: NOT Divisible!</span>
                        <p class="text-slate-300">Is <strong>84</strong> divisible by <strong>8</strong>?</p>
                        <p class="font-mono text-slate-200">84 = 2 × 2 × 3 × 7 (only two 2s)</p>
                        <p class="font-mono text-slate-200">8 = 2 × 2 × 2 (needs three 2s)</p>
                        <span class="text-rose-400 font-bold block mt-1">84 is missing one '2'! ✗</span>
                    </div>
                </div>
            """,
            "checkpoints": [
                {
                    "id": "cp_13_1",
                    "question": "If N = 2³ × 3² × 5, is N divisible by 12 (2² × 3)?",
                    "options": [
                        "Yes, because N has at least two 2s and at least one 3",
                        "No, because N has a 5",
                        "No, because 12 is larger than 5",
                        "Cannot be determined without computing N"
                    ],
                    "correct": 0,
                    "explanation": "12 requires 2² and 3¹. Since N contains 2³ and 3², all prime ingredients of 12 are fully contained within N."
                },
                {
                    "id": "cp_13_2",
                    "question": "Can a number whose prime factorisation has no '5' ever be divisible by 10?",
                    "options": [
                        "Yes, if it has lots of 2s",
                        "No, because 10 requires both a 2 and a 5 in its prime factorisation",
                        "Yes, if it ends in 0",
                        "Only if it is greater than 100"
                    ],
                    "correct": 1,
                    "explanation": "10 = 2 × 5. To be divisible by 10, the prime factorisation must contain at least one factor of 5 and one factor of 2."
                }
            ]
        },

        # Slide 14: 5.5 Divisibility Rules for 2, 5, and 10
        {
            "id": 14,
            "slide_num": 14,
            "title": "Rules: 2, 5, 10",
            "subtitle": "Last Digit Shortcuts & Decimal Place Value",
            "badge": "5.5 Divisibility Tests",
            "summary": "Because our number system is based on powers of 10, testing divisibility by factors of 10 (2, 5, and 10) requires checking ONLY the very last unit digit! This eliminates long division for even billion-digit numbers.",
            "theory": """
                <h4 class="text-sm font-bold text-amber-300 mb-1">The Unit Digit Shortcuts</h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-2">
                    Every whole number can be split into its tens part plus its unit digit:
                    <span class="font-mono text-slate-200 font-bold">Number = (Tens × 10) + Unit Digit</span>.
                    Since any multiple of 10 is already divisible by 2, 5, and 10, divisibility depends solely on the <strong>unit digit</strong>:
                </p>
                <div class="space-y-2 text-xs mb-3">
                    <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-700">
                        <strong class="text-amber-400">Divisible by 10:</strong>
                        Unit digit must be strictly <strong>0</strong> (e.g., 40, 190, 4580).
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-700">
                        <strong class="text-cyan-400">Divisible by 5:</strong>
                        Unit digit must be either <strong>0 or 5</strong> (e.g., 35, 80, 7925).
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-700">
                        <strong class="text-emerald-400">Divisible by 2:</strong>
                        Unit digit must be an even digit: <strong>0, 2, 4, 6, or 8</strong> (e.g., 14, 58, 936).
                    </div>
                </div>
            """,
            "checkpoints": [
                {
                    "id": "cp_14_1",
                    "question": "Which of the following numbers is divisible by both 2 and 5?",
                    "options": [
                        "345",
                        "248",
                        "590",
                        "773"
                    ],
                    "correct": 2,
                    "explanation": "To be divisible by both 2 (even) and 5 (ends in 0 or 5), the number must end in 0 (divisible by 10). 590 ends in 0."
                },
                {
                    "id": "cp_14_2",
                    "question": "What is the remainder when 4,897 is divided by 5?",
                    "options": [
                        "0",
                        "2",
                        "3",
                        "7"
                    ],
                    "correct": 1,
                    "explanation": "The last digit is 7. Since 7 ÷ 5 gives remainder 2, the entire number 4,897 leaves remainder 2 when divided by 5."
                }
            ]
        },

        # Slide 15: 5.5 Divisibility Rules for 4 and 8
        {
            "id": 15,
            "slide_num": 15,
            "title": "Rules: 4 & 8",
            "subtitle": "Inspecting the Last 2 and Last 3 Digits",
            "badge": "5.5 Powers of 2",
            "summary": "Since 100 is divisible by 4, any hundreds, thousands, and higher digits contribute nothing to the remainder when dividing by 4! Hence, divisibility by 4 depends ONLY on the last 2 digits. Similarly, since 1000 is divisible by 8, divisibility by 8 depends ONLY on the last 3 digits.",
            "theory": """
                <h4 class="text-sm font-bold text-amber-300 mb-1">Divisibility by 4 (Last 2 Digits)</h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-2">
                    Because <strong>100 = 4 × 25</strong>, any number of hundreds is automatically divisible by 4.
                    Therefore, test only the number formed by its <strong>last two digits</strong>:
                </p>
                <div class="p-2.5 rounded-lg bg-amber-950/40 border border-amber-500/30 text-xs mb-3">
                    <p class="text-slate-200">Is <strong>7,536</strong> divisible by 4?</p>
                    <p class="text-slate-300">Look at last two digits: <strong>36</strong>.</p>
                    <p class="font-mono text-emerald-300 font-bold">36 ÷ 4 = 9 (Zero remainder!). So 7,536 is divisible by 4! ✓</p>
                </div>
                <h4 class="text-sm font-bold text-cyan-300 mb-1">Divisibility by 8 (Last 3 Digits)</h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-2">
                    Because <strong>1000 = 8 × 125</strong>, any number of thousands is automatically divisible by 8.
                    Test only the number formed by its <strong>last three digits</strong>:
                </p>
                <div class="p-2.5 rounded-lg bg-cyan-950/40 border border-cyan-500/30 text-xs">
                    <p class="text-slate-200">Is <strong>98,128</strong> divisible by 8?</p>
                    <p class="text-slate-300">Look at last three digits: <strong>128</strong>.</p>
                    <p class="font-mono text-emerald-300 font-bold">128 ÷ 8 = 16 (Zero remainder!). So 98,128 is divisible by 8! ✓</p>
                </div>
            """,
            "checkpoints": [
                {
                    "id": "cp_15_1",
                    "question": "Is the year 2028 a leap year (divisible by 4)?",
                    "options": [
                        "Yes, because the last two digits '28' are divisible by 4 (4 × 7 = 28)",
                        "No, because 2028 ends in 8",
                        "No, leap years must end in 00",
                        "Only if it is divisible by 8"
                    ],
                    "correct": 0,
                    "explanation": "28 is divisible by 4 (4 × 7 = 28), so 2028 is a leap year!"
                },
                {
                    "id": "cp_15_2",
                    "question": "Which of the following numbers is divisible by 8?",
                    "options": [
                        "5,114",
                        "12,048",
                        "7,210",
                        "3,502"
                    ],
                    "correct": 1,
                    "explanation": "In 12,048, the last 3 digits are '048' = 48. Since 48 ÷ 8 = 6 (exact), 12,048 is divisible by 8."
                }
            ]
        },

        # Slide 16: 5.6 Fun with Numbers & Prime Puzzles
        {
            "id": 16,
            "slide_num": 16,
            "title": "Prime Puzzles",
            "subtitle": "Odd-One-Out & Cross-Product Grids",
            "badge": "5.6 Mathematical Puzzles",
            "summary": "Mathematical reasoning flourishes when applying factor and prime concepts to solve puzzles: finding the 'odd-one-out' based on prime properties, and filling cross-number grids where intersecting row and column products determine the unique primes in each cell.",
            "theory": """
                <h4 class="text-sm font-bold text-amber-300 mb-1">Odd-One-Out Mathematical Detective</h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-2">
                    Consider the set: <span class="font-mono text-amber-300 font-bold">{2, 9, 15, 25}</span>. Which is the odd one out?
                </p>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-700/80 mb-3 text-xs">
                    <ul class="list-disc list-inside text-slate-300 space-y-1">
                        <li><strong>2</strong> is the only <em>Prime number</em> (and the only even number)!</li>
                        <li><strong>9</strong> is the only <em>Single-digit composite</em>!</li>
                        <li><strong>25</strong> is the only multiple of 25!</li>
                    </ul>
                    <span class="text-emerald-400 block mt-1">Different valid mathematical properties can defend different choices!</span>
                </div>
                <h4 class="text-sm font-bold text-cyan-300 mb-1">Prime Cross-Product Puzzles</h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-2">
                    In a 2 × 2 grid, cells are filled with prime numbers. The products of each row and column are given along the edges:
                </p>
                <div class="p-2.5 rounded-lg bg-cyan-950/40 border border-cyan-500/30 text-xs font-mono">
                    Row 1 Product = 15 (Primes: 3 and 5)<br>
                    Col 1 Product = 21 (Primes: 3 and 7)<br>
                    <span class="text-emerald-300 font-bold">Intersection Cell must be HCF(15, 21) = 3!</span>
                </div>
            """,
            "checkpoints": [
                {
                    "id": "cp_16_1",
                    "question": "In the set {3, 5, 7, 9}, which number is the odd-one-out from the perspective of prime numbers?",
                    "options": [
                        "3, because it is the smallest",
                        "9, because it is composite (3 × 3) while 3, 5, and 7 are all primes",
                        "7, because it is lucky",
                        "5, because it ends in 5"
                    ],
                    "correct": 1,
                    "explanation": "3, 5, and 7 are all prime numbers, whereas 9 is composite (divisible by 1, 3, and 9)."
                },
                {
                    "id": "cp_16_2",
                    "question": "If a cell is at the intersection of a row with product 35 (5 × 7) and a column with product 14 (2 × 7), which prime must occupy that cell?",
                    "options": [
                        "2",
                        "5",
                        "7",
                        "1"
                    ],
                    "correct": 2,
                    "explanation": "The prime must divide both 35 and 14. HCF(35, 14) = 7, so 7 is the unique prime that satisfies both conditions."
                }
            ]
        },

        # Slide 17: Quiz Challenge 1 (Q1 to Q10: Multiples, Factors, Venn Diagrams & Perfect Numbers)
        {
            "id": 17,
            "slide_num": 17,
            "title": "Quiz 1",
            "subtitle": "Multiples, Factors, Venn Diagrams & Perfect Numbers • Questions 1 to 10",
            "badge": "Quiz 1 • Foundations",
            "is_quiz": True,
            "quiz_range": [1, 10]
        },

        # Slide 18: Quiz Challenge 2 (Q11 to Q20: Primes, Rectangular Arrays, Sieve & Twin Primes)
        {
            "id": 18,
            "slide_num": 18,
            "title": "Quiz 2",
            "subtitle": "Primes, Arrays, Sieve of Eratosthenes & Twin Primes • Questions 11 to 20",
            "badge": "Quiz 2 • Prime Sifting",
            "is_quiz": True,
            "quiz_range": [11, 20]
        },

        # Slide 19: Quiz Challenge 3 (Q21 to Q30: Co-primes, Peg Patterns, Factor Trees & Fundamental Theorem)
        {
            "id": 19,
            "slide_num": 19,
            "title": "Quiz 3",
            "subtitle": "Co-primes, Thread Art, Factor Trees & Fundamental Theorem • Questions 21 to 30",
            "badge": "Quiz 3 • Prime Factorisation",
            "is_quiz": True,
            "quiz_range": [21, 30]
        },

        # Slide 20: Quiz Challenge 4 (Q31 to Q40: Divisibility Rules for 2, 4, 5, 8, 10 & Prime Puzzles)
        {
            "id": 20,
            "slide_num": 20,
            "title": "Quiz 4",
            "subtitle": "Divisibility Shortcuts, Powers of 2 & Number Logic • Questions 31 to 40",
            "badge": "Quiz 4 • Divisibility Mastery",
            "is_quiz": True,
            "quiz_range": [31, 40]
        }
    ]

    QUIZ_QUESTIONS = [
        # Questions 1 to 10: Multiples, Factors, Venn Diagrams & Perfect Numbers
        {
            "id": 1,
            "question": "What is the third common multiple of 4 and 5?",
            "options": [
                "20",
                "40",
                "60",
                "80"
            ],
            "correct": 2,
            "explanation": "Since LCM(4, 5) = 20, the common multiples are multiples of 20: 1st is 20, 2nd is 40, and the 3rd common multiple is 3 × 20 = 60."
        },
        {
            "id": 2,
            "question": "Which of the following numbers is a factor of every whole counting number?",
            "options": [
                "0",
                "1",
                "2",
                "10"
            ],
            "correct": 1,
            "explanation": "1 divides every natural number exactly with zero remainder (N ÷ 1 = N), making 1 a universal factor."
        },
        {
            "id": 3,
            "question": "How many total factors does the number 24 have?",
            "options": [
                "6 factors",
                "7 factors",
                "8 factors",
                "10 factors"
            ],
            "correct": 2,
            "explanation": "The factors of 24 are 1, 2, 3, 4, 6, 8, 12, and 24. There are exactly 8 factors."
        },
        {
            "id": 4,
            "question": "In a Venn diagram with Circle A (multiples of 6) and Circle B (multiples of 8), which is the smallest positive number in their intersection?",
            "options": [
                "48",
                "24",
                "12",
                "14"
            ],
            "correct": 1,
            "explanation": "Multiples of 6 are 6, 12, 18, 24, 30... Multiples of 8 are 8, 16, 24, 32... The smallest common multiple is 24."
        },
        {
            "id": 5,
            "question": "What is the Highest Common Factor (HCF) of 36 and 48?",
            "options": [
                "6",
                "12",
                "18",
                "24"
            ],
            "correct": 1,
            "explanation": "Common factors of 36 and 48 are {1, 2, 3, 4, 6, 12}. The highest common factor is 12."
        },
        {
            "id": 6,
            "question": "Which of the following is the proper definition of a perfect number?",
            "options": [
                "A number with an odd number of factors",
                "A number that equals the sum of its proper factors (excluding itself)",
                "A number divisible by both 2 and 3",
                "A number ending in 6 or 8"
            ],
            "correct": 1,
            "explanation": "A perfect number equals the sum of all its positive divisors strictly less than itself (e.g., 6 = 1 + 2 + 3, and 28 = 1 + 2 + 4 + 7 + 14)."
        },
        {
            "id": 7,
            "question": "What is the sum of all factors of the second perfect number, 28?",
            "options": [
                "28",
                "56",
                "14",
                "64"
            ],
            "correct": 1,
            "explanation": "The factors of 28 are 1, 2, 4, 7, 14, and 28. Their sum is 1 + 2 + 4 + 7 + 14 + 28 = 56, which is exactly 2 × 28."
        },
        {
            "id": 8,
            "question": "In the Idli-Vada game (3 = Idli, 5 = Vada), what is the first number above 50 that triggers 'Idli-Vada'?",
            "options": [
                "55",
                "60",
                "65",
                "75"
            ],
            "correct": 1,
            "explanation": "'Idli-Vada' triggers on common multiples of 15. The multiples of 15 are 15, 30, 45, 60... The first one above 50 is 60."
        },
        {
            "id": 9,
            "question": "If a number N has exactly 3 factors, what kind of number must N be?",
            "options": [
                "A prime number",
                "The square of a prime number (such as 4, 9, 25, 49)",
                "An even number",
                "A perfect number"
            ],
            "correct": 1,
            "explanation": "If p is prime, p² has exactly three factors: 1, p, and p² (for example, 9 has factors 1, 3, 9; 25 has 1, 5, 25)."
        },
        {
            "id": 10,
            "question": "What is the HCF of two numbers where one number is a factor of the other (e.g., 7 and 21)?",
            "options": [
                "The larger number (21)",
                "The smaller number (7)",
                "1",
                "Their product (147)"
            ],
            "correct": 1,
            "explanation": "When a divides b, the greatest divisor shared by both is a itself: HCF(7, 21) = 7."
        },

        # Questions 11 to 20: Primes, Rectangular Arrays, Sieve & Twin Primes
        {
            "id": 11,
            "question": "Which of the following numbers can be arranged into more than one rectangular array of dots?",
            "options": [
                "2",
                "3",
                "5",
                "9"
            ],
            "correct": 3,
            "explanation": "9 can be arranged as a 1 × 9 row or a 3 × 3 square grid. Primes (2, 3, 5) can only be arranged as a single line (1 × p)."
        },
        {
            "id": 12,
            "question": "What is the smallest two-digit prime number?",
            "options": [
                "10",
                "11",
                "13",
                "17"
            ],
            "correct": 1,
            "explanation": "10 is composite (2 × 5). 11 has only factors 1 and 11, making it the smallest two-digit prime."
        },
        {
            "id": 13,
            "question": "In the Sieve of Eratosthenes up to 100, which prime's multiples cross out the number 49?",
            "options": [
                "2",
                "3",
                "5",
                "7"
            ],
            "correct": 3,
            "explanation": "49 = 7 × 7, so it is filtered out when circling 7 and crossing out multiples of 7."
        },
        {
            "id": 14,
            "question": "What is the largest prime number less than 100?",
            "options": [
                "91",
                "93",
                "97",
                "99"
            ],
            "correct": 2,
            "explanation": "91 = 7 × 13 (composite), 93 = 3 × 31 (composite), 99 = 9 × 11 (composite). 97 has no divisors other than 1 and 97."
        },
        {
            "id": 15,
            "question": "Which of the following is a pair of twin primes?",
            "options": [
                "(13, 17)",
                "(29, 31)",
                "(23, 25)",
                "(37, 41)"
            ],
            "correct": 1,
            "explanation": "Both 29 and 31 are prime numbers, and their difference is 31 − 29 = 2. In (23, 25), 25 is composite; the others have differences greater than 2."
        },
        {
            "id": 16,
            "question": "How many even prime numbers exist among the natural numbers?",
            "options": [
                "Zero",
                "Exactly 1 (the number 2)",
                "25",
                "Infinitely many"
            ],
            "correct": 1,
            "explanation": "2 is the only even prime. All other even numbers are divisible by 2 and thus composite."
        },
        {
            "id": 17,
            "question": "If p = 11, what is the value of the Sophie Germain candidate 2p + 1?",
            "options": [
                "21 (Composite)",
                "23 (Prime)",
                "25 (Composite)",
                "22 (Even)"
            ],
            "correct": 1,
            "explanation": "2(11) + 1 = 22 + 1 = 23. Since 23 is a prime number, 11 is a Sophie Germain prime!"
        },
        {
            "id": 18,
            "question": "Between 90 and 100, how many prime numbers exist?",
            "options": [
                "None",
                "Only 1 (the number 97)",
                "2 primes (91 and 97)",
                "3 primes (91, 93, 97)"
            ],
            "correct": 1,
            "explanation": "91 = 7×13, 92 even, 93 = 3×31, 94 even, 95 = 5×19, 96 even, 98 even, 99 = 9×11, 100 even. 97 is the solitary prime in the 90s."
        },
        {
            "id": 19,
            "question": "Goldbach's famous conjecture states that every even number greater than 2 can be written as:",
            "options": [
                "The product of three primes",
                "The sum of two prime numbers",
                "The difference of two squares",
                "A power of 2"
            ],
            "correct": 1,
            "explanation": "Goldbach conjectured in 1742 that every even number > 2 is the sum of two primes (e.g., 4 = 2+2, 6 = 3+3, 8 = 3+5, 10 = 5+5 or 3+7)."
        },
        {
            "id": 20,
            "question": "What is the only set of three prime numbers that are triplets with difference 2: (p, p+2, p+4)?",
            "options": [
                "(1, 3, 5)",
                "(3, 5, 7)",
                "(5, 7, 9)",
                "(11, 13, 15)"
            ],
            "correct": 1,
            "explanation": "(3, 5, 7) is the only prime triplet. For any other triplet (p, p+2, p+4), one of the three numbers must be a multiple of 3!"
        },

        # Questions 21 to 30: Co-primes, Peg Patterns, Factor Trees & Fundamental Theorem
        {
            "id": 21,
            "question": "Two numbers are co-prime if their Highest Common Factor is:",
            "options": [
                "0",
                "1",
                "Equal to their sum",
                "An even prime"
            ],
            "correct": 1,
            "explanation": "By definition, two numbers are co-prime if their only positive common divisor is 1: HCF(a, b) = 1."
        },
        {
            "id": 22,
            "question": "Which of the following pairs of consecutive numbers is ALWAYS co-prime?",
            "options": [
                "Any pair of consecutive numbers n and n + 1",
                "Only if both are prime",
                "Only if both are odd",
                "Only when n is less than 10"
            ],
            "correct": 0,
            "explanation": "Any factor dividing both n and n + 1 must divide their difference (n + 1) − n = 1. Therefore, HCF(n, n + 1) = 1 always!"
        },
        {
            "id": 23,
            "question": "On an 8-peg circular thread-art board, which jump step k produces a single continuous 8-pointed star?",
            "options": [
                "k = 2",
                "k = 3",
                "k = 4",
                "k = 6"
            ],
            "correct": 1,
            "explanation": "A continuous star requires k to be co-prime to 8. HCF(8, 2) = 2, HCF(8, 4) = 4, HCF(8, 6) = 2. Only HCF(8, 3) = 1."
        },
        {
            "id": 24,
            "question": "If two numbers are co-prime, what is their Least Common Multiple (LCM)?",
            "options": [
                "1",
                "Their direct product (a × b)",
                "Their sum (a + b)",
                "Their difference (b − a)"
            ],
            "correct": 1,
            "explanation": "Since HCF(a, b) × LCM(a, b) = a × b, when HCF = 1, LCM = a × b."
        },
        {
            "id": 25,
            "question": "What is the prime factorisation of 72?",
            "options": [
                "8 × 9",
                "2 × 36",
                "2³ × 3² (2 × 2 × 2 × 3 × 3)",
                "4 × 18"
            ],
            "correct": 2,
            "explanation": "Prime factorisation requires strictly prime factors. 72 = 8 × 9 = (2 × 2 × 2) × (3 × 3) = 2³ × 3²."
        },
        {
            "id": 26,
            "question": "What does the Fundamental Theorem of Arithmetic assert about prime factorisation?",
            "options": [
                "Every number has at least four factors",
                "Prime factorisation of any integer > 1 is unique, apart from the order of factors",
                "All primes are odd numbers",
                "Every prime factor is smaller than 10"
            ],
            "correct": 1,
            "explanation": "The Fundamental Theorem of Arithmetic guarantees that each integer > 1 has a unique prime factorization up to the order of factors."
        },
        {
            "id": 27,
            "question": "Using prime factorisation, what is the HCF of 60 (2² × 3 × 5) and 90 (2 × 3² × 5)?",
            "options": [
                "10",
                "15",
                "30 (2 × 3 × 5)",
                "180"
            ],
            "correct": 2,
            "explanation": "Take the lowest power of each common prime factor: 2¹ × 3¹ × 5¹ = 30."
        },
        {
            "id": 28,
            "question": "Using prime factorisation, what is the LCM of 12 (2² × 3) and 18 (2 × 3²)?",
            "options": [
                "6",
                "36 (2² × 3²)",
                "72",
                "216"
            ],
            "correct": 1,
            "explanation": "Take the highest power of each prime factor present: 2² × 3² = 4 × 9 = 36."
        },
        {
            "id": 29,
            "question": "If number A = 2⁴ × 3² × 7, is A divisible by 28 (2² × 7)?",
            "options": [
                "Yes, because A contains 2² and 7",
                "No, because A has a 3",
                "No, 28 does not divide 7",
                "Only if A is less than 500"
            ],
            "correct": 0,
            "explanation": "28 = 2² × 7. Since A contains 2⁴ and 7¹, all prime factors of 28 are contained in A with equal or greater powers."
        },
        {
            "id": 30,
            "question": "If two positive numbers have HCF = 6 and LCM = 72, and one number is 18, what is the other number?",
            "options": [
                "12",
                "24",
                "36",
                "48"
            ],
            "correct": 1,
            "explanation": "Product of numbers = HCF × LCM = 6 × 72 = 432. The other number is 432 ÷ 18 = 24."
        },

        # Questions 31 to 40: Divisibility Rules for 2, 4, 5, 8, 10 & Prime Puzzles
        {
            "id": 31,
            "question": "A number is divisible by 10 if and only if its last digit is:",
            "options": [
                "5",
                "0",
                "Any even number",
                "1"
            ],
            "correct": 1,
            "explanation": "Every multiple of 10 ends in 0."
        },
        {
            "id": 32,
            "question": "Which of the following numbers is divisible by 5 but NOT by 10?",
            "options": [
                "120",
                "435",
                "680",
                "900"
            ],
            "correct": 1,
            "explanation": "A number divisible by 5 but not 10 must end in 5. 435 ends in 5."
        },
        {
            "id": 33,
            "question": "To test whether 583,924 is divisible by 4, which part of the number do you inspect?",
            "options": [
                "Only the last digit (4)",
                "The last two digits (24)",
                "The last three digits (924)",
                "The sum of all digits"
            ],
            "correct": 1,
            "explanation": "Since 100 is divisible by 4, divisibility by 4 depends entirely on the last two digits: 24 ÷ 4 = 6, so it is divisible by 4."
        },
        {
            "id": 34,
            "question": "Which of the following numbers is divisible by 8?",
            "options": [
                "7,124",
                "15,816",
                "9,302",
                "4,114"
            ],
            "correct": 1,
            "explanation": "Check the last 3 digits: 816 ÷ 8 = 102 (exact with no remainder). Therefore, 15,816 is divisible by 8."
        },
        {
            "id": 35,
            "question": "What is the smallest digit you can place in the blank to make 7,5_2 divisible by 4?",
            "options": [
                "0",
                "1",
                "2",
                "3"
            ],
            "correct": 1,
            "explanation": "If the blank is 0, the last two digits are 02 (not divisible by 4). If the blank is 1, the last two digits are 12 (12 ÷ 4 = 3, divisible!). Thus 1 is the smallest valid digit."
        },
        {
            "id": 36,
            "question": "Why is the test for divisibility by 8 based on the last 3 digits?",
            "options": [
                "Because 8 has 3 factors",
                "Because 1,000 = 8 × 125, so any thousands part is already divisible by 8",
                "Because 8 = 2³",
                "Because 3 is a prime number"
            ],
            "correct": 1,
            "explanation": "Since 1,000 is an exact multiple of 8 (8 × 125 = 1000), any thousands, ten-thousands, etc., contribute 0 to the remainder when divided by 8."
        },
        {
            "id": 37,
            "question": "In a prime cross-grid puzzle, Row 1 has product 10 (2 × 5) and Column 1 has product 14 (2 × 7). What prime number goes in their intersection cell?",
            "options": [
                "5",
                "7",
                "2",
                "10"
            ],
            "correct": 2,
            "explanation": "The intersection must divide both 10 and 14. HCF(10, 14) = 2, so the cell must contain 2."
        },
        {
            "id": 38,
            "question": "Which number is the 'odd-one-out' in the set {11, 13, 15, 17}?",
            "options": [
                "11",
                "13",
                "15 (it is composite: 3 × 5, while the rest are primes)",
                "17"
            ],
            "correct": 2,
            "explanation": "11, 13, and 17 are all prime numbers; 15 is composite because it has factors 1, 3, 5, and 15."
        },
        {
            "id": 39,
            "question": "If a number is divisible by both 4 and 6, must it always be divisible by 24 (4 × 6)?",
            "options": [
                "Yes, always",
                "No, not necessarily, because 4 and 6 are NOT co-prime (e.g., 12 is divisible by both 4 and 6, but not by 24)",
                "Only if the number is odd",
                "Only if it ends in 4"
            ],
            "correct": 1,
            "explanation": "Because 4 and 6 share a factor of 2 (HCF = 2), their LCM is 12, not 24. A number divisible by both 4 and 6 is guaranteed to be divisible by 12, but not necessarily 24 (e.g., 12, 36, 60)."
        },
        {
            "id": 40,
            "question": "If a number is divisible by two CO-PRIME numbers a and b, is it guaranteed to be divisible by their product a × b?",
            "options": [
                "Yes, always, because LCM(a, b) = a × b when HCF(a, b) = 1",
                "No, never",
                "Only if a and b are both prime",
                "Only for single digit numbers"
            ],
            "correct": 0,
            "explanation": "Yes! When a and b are co-prime, LCM(a, b) = a × b. Any multiple of both a and b is therefore an exact multiple of a × b."
        }
    ]

    # Quick check for question 35
    # For question 35, let's verify options: [0, 1, 2, 3]. 02 not div by 4. 12 div by 4. So option index 1 is correct!

    # Serialization with Python True/False
    slides_json = json.dumps(SLIDES, indent=4, ensure_ascii=False).replace(': true', ': True').replace(': false', ': False')
    meta_json = json.dumps(CHAPTER_META, indent=4, ensure_ascii=False).replace(': true', ': True').replace(': false', ': False')
    quiz_json = json.dumps(QUIZ_QUESTIONS, indent=4, ensure_ascii=False).replace(': true', ': True').replace(': false', ': False')

    code = f'''"""NCERT Class 6 Mathematics Chapter 5: Prime Time Data Module."""

CHAPTER_META = {meta_json}

SLIDES = {slides_json}

QUIZ_QUESTIONS = {quiz_json}
'''

    # Strict check for raw LaTeX
    forbidden = ["\\text", "\\frac", "\\circ", "\\angle", "\\overleftrightarrow", "\\overline", "\\vec", "\\approx", "\\dots", "\\sqrt"]
    for word in forbidden:
        if word in code:
            raise ValueError(f"CRITICAL ERROR: Found raw LaTeX '{word}' in data module!")

    # Check for surrogates
    clean_chars = [ch for ch in code if not (0xD800 <= ord(ch) <= 0xDFFF)]
    clean_code = ''.join(clean_chars)

    with open(".agents/class6_math_prime_time_data.py", "w", encoding="utf-8") as f:
        f.write(clean_code)

    print("Successfully generated .agents/class6_math_prime_time_data.py with 20 slides and 40 questions.")
    print("VERIFIED PASS: Zero raw LaTeX and zero surrogates in data module!")

if __name__ == "__main__":
    build_data()
