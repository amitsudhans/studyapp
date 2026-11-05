# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 13: Animal Jumps - Part 1 (Slides 1 to 8)
Syllabus: Joyful Mathematics (NEP 2020)
Strict Constraints:
- 195 to 215 words per lecture
- Short headings (1-3 words)
- Indian male teacher tone
- Zero human names
- Zero raw LaTeX
- 2 checkpoints per slide
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Multiplier Magic Box",
        "tagline": "Discovery Puzzle • Uncovering the Secret Multiplier Inside the Mathematical Machine",
        "lecture": (
            "Step right inside our curious mathematical workshop and observe an astonishing device known as the multiplier magic box! "
            "When numerical tokens enter through the top funnel, the machine applies a hidden rule and outputs completely new numbers. "
            "Let us investigate what happens: when the number seven enters the machine, twenty-eight rolls out smoothly at the bottom. "
            "When the number nine enters, thirty-six emerges. When twelve enters, forty-eight pops out. And when eighteen enters, the "
            "machine produces seventy-two! What secret mathematical transformation is taking place inside this marvelous brass chamber? "
            "By comparing each input number with its corresponding output, we notice an unmistakable pattern: twenty-eight divided by seven "
            "is four; thirty-six divided by nine is four; forty-eight divided by twelve is four; and seventy-two divided by eighteen is "
            "also four! Every single input number is being multiplied by the constant hidden factor of four. The magic box demonstrates "
            "the core relationship of multiplication: an input number combined with a multiplier generates an exact product called a "
            "multiple. Whenever we scale an initial quantity by a whole number, we produce multiples. By testing different inputs, students "
            "uncover hidden factors and experience the thrill of reverse engineering mathematical operations with clear geometric and logical thinking."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-purple-900/40 via-indigo-900/30 to-purple-900/40 border border-purple-500/30 rounded-xl p-4">
        <h4 class="text-purple-300 font-bold text-sm tracking-wider uppercase mb-1">The Magic Box Multiplier Rule</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Inside the magic machine, every input token is multiplied by a secret constant number:
            <span class="text-amber-300 font-bold">Input × Hidden Factor = Output Multiple</span>.
        </p>
    </div>
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs font-mono">
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-slate-400 block">7 enters ➔</span>
            <span class="text-emerald-400 font-bold text-sm">28 exits</span>
            <span class="text-[10px] text-amber-300 block mt-0.5">(7 × 4 = 28)</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-slate-400 block">9 enters ➔</span>
            <span class="text-emerald-400 font-bold text-sm">36 exits</span>
            <span class="text-[10px] text-amber-300 block mt-0.5">(9 × 4 = 36)</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-slate-400 block">12 enters ➔</span>
            <span class="text-emerald-400 font-bold text-sm">48 exits</span>
            <span class="text-[10px] text-amber-300 block mt-0.5">(12 × 4 = 48)</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-slate-400 block">18 enters ➔</span>
            <span class="text-emerald-400 font-bold text-sm">72 exits</span>
            <span class="text-[10px] text-amber-300 block mt-0.5">(18 × 4 = 72)</span>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "What is the secret hidden multiplier inside the magic box when input 7 yields 28?",
                "options": ["3", "4", "5", "6"],
                "answer": 1,
                "explanation": "28 ÷ 7 = 4, 36 ÷ 9 = 4, 48 ÷ 12 = 4. The secret multiplier is 4.",
                "hint": "Divide the output 28 by the input 7."
            },
            {
                "question": "If the number 15 enters this same magic box, what output number will roll out?",
                "options": ["45", "50", "60", "75"],
                "answer": 2,
                "explanation": "Multiply the input 15 by the secret factor 4: 15 × 4 = 60.",
                "hint": "Calculate 15 × 4."
            }
        ]
    },
    {
        "id": 2,
        "title": "Factors And Multiples",
        "tagline": "Fundamental Definitions • Connecting Multiplication Facts to Factor Arrays",
        "lecture": (
            "Now let us establish the exact mathematical definitions of factors and multiples, which form the bedrock of arithmetic. "
            "When two whole numbers are multiplied together, their resulting product is called a multiple of each individual number. "
            "Conversely, the numbers that multiply together to give that product are called its factors! For example, taking the multiplication "
            "fact three times five equals fifteen, fifteen is a multiple of both three and five. In turn, both three and five are "
            "factors of fifteen. To visualize this concept geometrically, imagine arranging unit square tiles into solid rectangular carpets. "
            "If you have twelve square tiles, how many different complete rectangles can you build without leaving any leftover gaps? "
            "You can arrange them as one single row of twelve tiles, written as one by twelve. You can arrange them as two rows of six, "
            "written as two by six. Or you can build three rows of four tiles, written as three by four! Each dimension represents an exact "
            "divisor. Listing all unique dimensions gives one, two, three, four, six, and twelve. These six numbers are all the factors of "
            "twelve! A factor divides a number completely with zero remainder, while multiples represent repeated skip jumps along the number line."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-blue-900/40 via-cyan-900/30 to-blue-900/40 border border-blue-500/30 rounded-xl p-4">
        <h4 class="text-cyan-300 font-bold text-sm tracking-wider uppercase mb-1">Dual Relationship: Factors & Multiples</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            In the multiplication sentence <span class="text-amber-300 font-bold">3 × 5 = 15</span>:
            <span class="text-emerald-400 font-semibold">3 and 5 are factors</span>, while
            <span class="text-cyan-400 font-semibold">15 is a multiple</span> of both 3 and 5.
        </p>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 text-center text-xs font-mono">
        <div class="bg-slate-800/80 p-3 rounded-lg border border-slate-700">
            <span class="text-amber-300 font-bold block mb-1">1 × 12 = 12</span>
            <span class="text-slate-400 block text-[11px]">1 row of 12 tiles</span>
            <span class="text-emerald-400 text-[10px] mt-1 block">Factors: 1, 12</span>
        </div>
        <div class="bg-slate-800/80 p-3 rounded-lg border border-slate-700">
            <span class="text-amber-300 font-bold block mb-1">2 × 6 = 12</span>
            <span class="text-slate-400 block text-[11px]">2 rows of 6 tiles</span>
            <span class="text-emerald-400 text-[10px] mt-1 block">Factors: 2, 6</span>
        </div>
        <div class="bg-slate-800/80 p-3 rounded-lg border border-slate-700">
            <span class="text-amber-300 font-bold block mb-1">3 × 4 = 12</span>
            <span class="text-slate-400 block text-[11px]">3 rows of 4 tiles</span>
            <span class="text-emerald-400 text-[10px] mt-1 block">Factors: 3, 4</span>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "Which of the following complete sets lists all the factors of 12?",
                "options": ["1, 2, 3, 4, 6, 12", "2, 3, 4, 6", "1, 2, 4, 12", "3, 4, 6, 12"],
                "answer": 0,
                "explanation": "12 can be formed by 1×12, 2×6, and 3×4. All factors are 1, 2, 3, 4, 6, and 12.",
                "hint": "Check all dimensions of rectangles that enclose 12 square tiles."
            },
            {
                "question": "In the multiplication equation 4 × 7 = 28, what is the number 28 called?",
                "options": ["A factor of 4", "A factor of 7", "A multiple of both 4 and 7", "A prime number"],
                "answer": 2,
                "explanation": "The product 28 is a multiple of both its factors, 4 and 7.",
                "hint": "The product formed by multiplying two numbers is their multiple."
            }
        ]
    },
    {
        "id": 3,
        "title": "Array Configurations",
        "tagline": "Geometric Arrays • Building Rectangles to Systematically Discover All Factors",
        "lecture": (
            "Building geometric arrays is a marvelous hands-on method to discover all factor pairs of any given number without missing any. "
            "Whenever we arrange square counters into unbroken rectangular grids with equal rows and equal columns, the length and breadth "
            "directly reveal a valid factor pair! Consider investigating the number ten: we can arrange ten square tiles as one long row "
            "of ten tiles, or as two rows of five tiles. Thus, the complete factors of ten are one, two, five, and ten. Now consider the "
            "number sixteen: we can form one by sixteen, two by eight, and four by four! Notice that four times four is a perfect square array. "
            "Because four is paired with itself, the factors of sixteen are one, two, four, eight, and sixteen. What about twenty-five? "
            "Twenty-five forms one by twenty-five, and five by five, giving factors one, five, and twenty-five. Numbers with an odd count of "
            "factors are always perfect square numbers! Conversely, what happens when we try to form rectangles with thirteen tiles? "
            "No matter how hard you attempt to make two equal rows, three rows, or four rows, there is always an uneven leftover tile! "
            "Thirteen can only form a single straight line of one by thirteen, giving only two factors."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-emerald-900/40 via-teal-900/30 to-emerald-900/40 border border-emerald-500/30 rounded-xl p-4">
        <h4 class="text-emerald-300 font-bold text-sm tracking-wider uppercase mb-1">Rectangular Array Rule</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Every distinct rectangle formed by <span class="text-amber-300 font-bold">N tiles</span> reveals a factor pair
            <span class="text-cyan-300 font-semibold">(Rows × Columns = N)</span>. Square arrays occur when factors are equal.
        </p>
    </div>
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs font-mono">
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-amber-300 font-bold block">10 Tiles</span>
            <span class="text-slate-300 text-[11px] block">1×10, 2×5</span>
            <span class="text-emerald-400 text-[10px]">4 factors</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-amber-300 font-bold block">16 Tiles</span>
            <span class="text-slate-300 text-[11px] block">1×16, 2×8, 4×4</span>
            <span class="text-emerald-400 text-[10px]">5 factors (Square!)</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-amber-300 font-bold block">25 Tiles</span>
            <span class="text-slate-300 text-[11px] block">1×25, 5×5</span>
            <span class="text-emerald-400 text-[10px]">3 factors (Square!)</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
            <span class="text-amber-300 font-bold block">13 Tiles</span>
            <span class="text-slate-300 text-[11px] block">1×13 only</span>
            <span class="text-purple-400 text-[10px]">2 factors (Prime!)</span>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "How many distinct rectangles can be formed using 16 square tiles?",
                "options": ["1 rectangle", "2 rectangles", "3 rectangles", "4 rectangles"],
                "answer": 2,
                "explanation": "16 can form 1×16, 2×8, and 4×4. That makes 3 distinct rectangles (including the square).",
                "hint": "Count the factor pairs: (1,16), (2,8), and (4,4)."
            },
            {
                "question": "Which of the following numbers forms a square array because of an identical factor pair?",
                "options": ["14", "20", "25", "32"],
                "answer": 2,
                "explanation": "25 forms a 5×5 square array because 5 × 5 = 25.",
                "hint": "Find the number that can be expressed as a number multiplied by itself."
            }
        ]
    },
    {
        "id": 4,
        "title": "Prime Numbers",
        "tagline": "Special Numbers • Numbers with Exactly Two Unique Factors: 1 and Themselves",
        "lecture": (
            "When we experimented with building tile rectangles, we noticed something extraordinary about numbers like thirteen: they "
            "could never be broken into multiple equal rows! Numbers that have exactly two distinct factors—namely one and the number "
            "itself—are called prime numbers. If you take nineteen square tiles, you can only arrange them as one single row of nineteen, "
            "or nineteen rows of one. You cannot make two rows, three rows, or any other rectangular shape without tiles sticking out awkwardly. "
            "Therefore, nineteen is a prime number! Similarly, thirty-seven is a prime number because its only factors are one and thirty-seven. "
            "On the other hand, numbers that have more than two factors are called composite numbers. For instance, twenty-four has eight "
            "factors: one, two, three, four, six, eight, twelve, and twenty-four, making it composite. But what about the number one? "
            "This is a classic mathematical question: the number one has only one single factor, which is one itself! Because a prime number "
            "must have exactly two distinct factors, the number one is neither prime nor composite. The smallest prime number in mathematics "
            "is two, and it is the only even prime number because every subsequent even number is divisible by two."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-amber-900/40 via-orange-900/30 to-amber-900/40 border border-amber-500/30 rounded-xl p-4">
        <h4 class="text-amber-300 font-bold text-sm tracking-wider uppercase mb-1">Prime vs Composite Definition</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            <span class="text-emerald-400 font-bold">Prime Number:</span> Exactly 2 factors (1 and itself). Example: 2, 3, 5, 7, 11, 13, 37.<br>
            <span class="text-cyan-400 font-bold">Composite Number:</span> More than 2 factors. Example: 4, 6, 8, 9, 12, 24.<br>
            <span class="text-rose-300 font-semibold">Special Case:</span> 1 is neither prime nor composite (only 1 factor).
        </p>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs font-mono">
        <div class="bg-slate-800/80 p-3 rounded-lg border border-slate-700">
            <span class="text-emerald-400 font-bold block mb-1">Number 13 (Prime)</span>
            <span class="text-slate-300 block">Factors: {1, 13}</span>
            <span class="text-slate-400 text-[11px] block mt-1">Cannot form rectangles other than 1 × 13.</span>
        </div>
        <div class="bg-slate-800/80 p-3 rounded-lg border border-slate-700">
            <span class="text-cyan-400 font-bold block mb-1">Number 14 (Composite)</span>
            <span class="text-slate-300 block">Factors: {1, 2, 7, 14}</span>
            <span class="text-slate-400 text-[11px] block mt-1">Forms rectangles: 1 × 14 and 2 × 7.</span>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "Why is the number 37 classified as a prime number?",
                "options": [
                    "It is an odd number",
                    "It has exactly two factors: 1 and 37",
                    "It can be divided by 3",
                    "It can form multiple rectangles"
                ],
                "answer": 1,
                "explanation": "A prime number has exactly two factors: 1 and the number itself. 37 only has factors 1 and 37.",
                "hint": "Think about the definition of a prime number regarding its total factors."
            },
            {
                "question": "Which of the following statements about the number 2 is correct?",
                "options": [
                    "2 is a composite number",
                    "2 is the only even prime number",
                    "2 is neither prime nor composite",
                    "2 has three factors"
                ],
                "answer": 1,
                "explanation": "2 has exactly two factors (1 and 2), making it prime, and it is the only even prime number.",
                "hint": "Check how many factors the number 2 has."
            }
        ]
    },
    {
        "id": 5,
        "title": "Number Line Jumps",
        "tagline": "Animal Jumps • Tracking Rabbit and Frog Step Sequences on a Common Number Line",
        "lecture": (
            "Imagine standing on a lush green meadow where two lively animal friends—a rabbit and a frog—are ready to leap along a straight "
            "numbered pathway marked from zero onwards. Both animals begin their energetic journey together at position zero. The swift rabbit "
            "takes powerful leaps of four units at a time, while the nimble frog hops along in steps of three units at a time! Where will "
            "their footprints land? Let us trace the rabbit first: leaping in fours, the rabbit lands on four, eight, twelve, sixteen, twenty, "
            "twenty-four, twenty-eight, and thirty-two. These numbers are the multiples of four! Now let us follow the frog: hopping in threes, "
            "the frog touches three, six, nine, twelve, fifteen, eighteen, twenty-one, twenty-four, and twenty-seven. These numbers are the "
            "multiples of three! As we observe the numbered tiles, we discover something marvelous: both the rabbit and the frog land on the "
            "exact same tile at twelve, and again at twenty-four! A number that appears in the skip-counting sequences of two different numbers "
            "is called a common multiple. Twelve is the very first shared stepping stone where both animals meet, making it their least "
            "common multiple, while subsequent meetings occur at twenty-four, thirty-six, and forty-eight."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-emerald-900/40 via-teal-900/30 to-emerald-900/40 border border-emerald-500/30 rounded-xl p-4">
        <h4 class="text-emerald-300 font-bold text-sm tracking-wider uppercase mb-1">Common Multiples on the Number Line</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            When animals take regular jumps from 0, the tiles where <span class="text-amber-300 font-bold">both footprints overlap</span>
            are called <span class="text-cyan-300 font-semibold">Common Multiples</span>.
        </p>
    </div>
    <div class="space-y-2 font-mono text-xs">
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700 flex justify-between items-center">
            <span class="text-amber-400 font-bold">🐰 Rabbit Jumps (Steps of 4):</span>
            <span class="text-slate-200">0, 4, 8, <strong class="text-emerald-400 bg-emerald-950/80 px-1.5 py-0.5 rounded border border-emerald-500/40">12</strong>, 16, 20, <strong class="text-emerald-400 bg-emerald-950/80 px-1.5 py-0.5 rounded border border-emerald-500/40">24</strong>, 28...</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700 flex justify-between items-center">
            <span class="text-cyan-400 font-bold">🐸 Frog Jumps (Steps of 3):</span>
            <span class="text-slate-200">0, 3, 6, 9, <strong class="text-emerald-400 bg-emerald-950/80 px-1.5 py-0.5 rounded border border-emerald-500/40">12</strong>, 15, 18, 21, <strong class="text-emerald-400 bg-emerald-950/80 px-1.5 py-0.5 rounded border border-emerald-500/40">24</strong>...</span>
        </div>
        <div class="bg-slate-900/90 p-2.5 rounded-lg border border-emerald-500/30 text-center text-emerald-300">
            ★ Shared Footprint Tiles (Common Multiples): <strong>12, 24, 36, 48...</strong>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "What is the very first number greater than 0 where both the rabbit (step 4) and frog (step 3) land?",
                "options": ["7", "12", "16", "24"],
                "answer": 1,
                "explanation": "Multiples of 4 are 4, 8, 12... Multiples of 3 are 3, 6, 9, 12... The first common number is 12.",
                "hint": "Find the smallest number that appears in both 3-times and 4-times multiplication tables."
            },
            {
                "question": "If both animals continue leaping past 24, what will be their next common landing tile?",
                "options": ["28", "30", "36", "40"],
                "answer": 2,
                "explanation": "Common multiples of 3 and 4 increase by multiples of 12: 12, 24, 36, 48. The next is 36.",
                "hint": "Add 12 to the previous common multiple 24."
            }
        ]
    },
    {
        "id": 6,
        "title": "Common Multiples",
        "tagline": "Spider & Grasshopper • Investigating Shared Multiples with Step Multipliers",
        "lecture": (
            "Let us observe another fascinating pair of garden jumpers: a tiny spider and an agile grasshopper embarking on the number trail. "
            "Starting side by side at tile zero, the spider scuttles forward in jumps of three units, while the grasshopper leaps ahead in "
            "large strides of six units! Let us record where their paths cross. The spider touches three, six, nine, twelve, fifteen, eighteen, "
            "twenty-one, and twenty-four. The grasshopper touches six, twelve, eighteen, twenty-four, and thirty. What do you observe? "
            "Because six is already a multiple of three, every single tile touched by the grasshopper is also touched by the spider! "
            "Their shared common multiples are six, twelve, eighteen, twenty-four, and so forth. Notice that whenever one jump size divides "
            "the other jump size completely, the larger jump size itself becomes the smallest common multiple! Now consider finding common "
            "multiples for other pairs, such as six and eight. Multiples of six are six, twelve, eighteen, twenty-four, thirty, thirty-six, "
            "and forty-two. Multiples of eight are eight, sixteen, twenty-four, thirty-two, and forty. The smallest number they share is "
            "twenty-four! Their next common multiple is forty-eight. Identifying common multiples allows mathematicians to synchronize gears, "
            "schedule rotating bus routes, and solve dynamic rhythm cycles."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-cyan-900/40 via-blue-900/30 to-cyan-900/40 border border-cyan-500/30 rounded-xl p-4">
        <h4 class="text-cyan-300 font-bold text-sm tracking-wider uppercase mb-1">Factor-Multiple Pair Principle</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            When one number divides another (like 3 dividing 6), the <span class="text-amber-300 font-bold">least common multiple</span>
            is simply the <span class="text-emerald-400 font-semibold">larger number itself (6)</span>!
        </p>
    </div>
    <div class="space-y-2 font-mono text-xs">
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700 flex justify-between items-center">
            <span class="text-purple-400 font-bold">🕷️ Spider (Steps of 3):</span>
            <span class="text-slate-200">3, <strong class="text-emerald-400">6</strong>, 9, <strong class="text-emerald-400">12</strong>, 15, <strong class="text-emerald-400">18</strong>, 21, <strong class="text-emerald-400">24</strong>...</span>
        </div>
        <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700 flex justify-between items-center">
            <span class="text-emerald-400 font-bold">🦗 Grasshopper (Steps of 6):</span>
            <span class="text-slate-200"><strong class="text-emerald-400">6</strong>, <strong class="text-emerald-400">12</strong>, <strong class="text-emerald-400">18</strong>, <strong class="text-emerald-400">24</strong>, 30...</span>
        </div>
        <div class="bg-slate-900/90 p-2.5 rounded-lg border border-cyan-500/30 text-center text-cyan-300">
            ★ Common Multiples of 3 and 6: <strong>6, 12, 18, 24, 30...</strong>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "What is the smallest common multiple of the spider (step 3) and grasshopper (step 6)?",
                "options": ["3", "6", "9", "18"],
                "answer": 1,
                "explanation": "Since 6 is a multiple of 3 (3 × 2 = 6), 6 is the smallest number touched by both.",
                "hint": "Check the very first multiple of 6 and whether 3 divides it."
            },
            {
                "question": "What is the smallest common multiple of 6 and 8?",
                "options": ["14", "18", "24", "48"],
                "answer": 2,
                "explanation": "Multiples of 6: 6, 12, 18, 24... Multiples of 8: 8, 16, 24... The smallest shared multiple is 24.",
                "hint": "Look for the first common number in the 6 and 8 multiplication tables."
            }
        ]
    },
    {
        "id": 7,
        "title": "Multiples Practice Set",
        "tagline": "Skill Mastery • Systematically Computing Common Multiples for Diverse Number Pairs",
        "lecture": (
            "Now that we understand how common multiples emerge from overlapping skip-counting tracks, let us sharpen our mental math fluency "
            "with a structured practice set! Consider finding common multiples for the pair four and six. Listing multiples of four gives "
            "four, eight, twelve, sixteen, twenty, twenty-four, twenty-eight, thirty-two, and thirty-six. Listing multiples of six yields "
            "six, twelve, eighteen, twenty-four, thirty, and thirty-six. Looking closely at both lists, we immediately circle twelve, "
            "twenty-four, and thirty-six as common multiples. Notice that every common multiple is an exact multiple of the smallest one, "
            "twelve! Next, let us test eight and twelve: multiples of eight are eight, sixteen, twenty-four, thirty-two, forty, and forty-eight. "
            "Multiples of twelve are twelve, twenty-four, thirty-six, and forty-eight. Their common multiples are twenty-four and forty-eight! "
            "What about nine and twelve? Multiples of nine are nine, eighteen, twenty-seven, thirty-six, forty-five, and fifty-four. "
            "Multiples of twelve include twelve, twenty-four, thirty-six, and forty-eight. Their first common meeting point is thirty-six! "
            "Notice the universal systematic rule: once you identify the least common multiple of any pair of numbers, all subsequent "
            "common multiples are simply repeated multiples of that very first shared number. This elegant property saves immense calculation "
            "effort in all branches of arithmetic and mathematics."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-indigo-900/40 via-purple-900/30 to-indigo-900/40 border border-indigo-500/30 rounded-xl p-4">
        <h4 class="text-indigo-300 font-bold text-sm tracking-wider uppercase mb-1">Common Multiples Table</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Finding common multiples by listing and spotting the lowest shared value:
        </p>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 text-xs font-mono">
        <div class="bg-slate-800/80 p-3 rounded-lg border border-slate-700">
            <span class="text-amber-300 font-bold block mb-1">Pair: 4 & 6</span>
            <span class="text-slate-400 text-[11px] block">LCM = 12</span>
            <span class="text-emerald-400 text-[11px] block mt-1">Multiples: 12, 24, 36...</span>
        </div>
        <div class="bg-slate-800/80 p-3 rounded-lg border border-slate-700">
            <span class="text-amber-300 font-bold block mb-1">Pair: 8 & 12</span>
            <span class="text-slate-400 text-[11px] block">LCM = 24</span>
            <span class="text-emerald-400 text-[11px] block mt-1">Multiples: 24, 48, 72...</span>
        </div>
        <div class="bg-slate-800/80 p-3 rounded-lg border border-slate-700">
            <span class="text-amber-300 font-bold block mb-1">Pair: 9 & 12</span>
            <span class="text-slate-400 text-[11px] block">LCM = 36</span>
            <span class="text-emerald-400 text-[11px] block mt-1">Multiples: 36, 72, 108...</span>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "What is the least common multiple (LCM) of 8 and 12?",
                "options": ["16", "24", "32", "48"],
                "answer": 1,
                "explanation": "Multiples of 8: 8, 16, 24... Multiples of 12: 12, 24... The least common multiple is 24.",
                "hint": "Check the smallest multiple of 12 that is divisible by 8."
            },
            {
                "question": "If the least common multiple of two numbers is 15, what will their third common multiple be?",
                "options": ["30", "45", "60", "75"],
                "answer": 1,
                "explanation": "Common multiples are multiples of the LCM: 1st is 15, 2nd is 30, 3rd is 45.",
                "hint": "Multiply the LCM 15 by 3."
            }
        ]
    },
    {
        "id": 8,
        "title": "Cobbled Road Race",
        "tagline": "Story Trail Puzzle • Analyzing Step Trajectories to a Target Food Tile at 64",
        "lecture": (
            "Along a winding cobbled forest road numbered from tile zero all the way to tile sixty-four, two animal racers are competing "
            "to reach a basket of crunchy vegetables placed at tile sixty-four! Racer A, a nimble rabbit, leaps forward in steady steps of "
            "four tiles. Racer B, a graceful deer, leaps forward in swift bounds of six tiles. Let us investigate who will reach the basket "
            "and who gets there first! To find out if an animal can land exactly on tile sixty-four, we must check if sixty-four is a multiple "
            "of that animal's jump size. For Racer A: dividing sixty-four by four gives exactly sixteen with zero remainder! Yes, Racer A "
            "lands directly on tile sixty-four after exactly sixteen jumps. For Racer B: dividing sixty-four by six gives ten with a remainder "
            "of four! Racer B lands on tile sixty (ten jumps) and then leaps ahead to tile sixty-six (eleven jumps), completely overshooting "
            "tile sixty-four! The deer never touches tile sixty-four at all! This delightful story highlights divisibility in action: a target "
            "tile is reached only if it is an exact multiple of the leap distance. Racer A wins the treat with sixteen precise leaps."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-amber-900/40 via-red-900/30 to-amber-900/40 border border-amber-500/30 rounded-xl p-4">
        <h4 class="text-amber-300 font-bold text-sm tracking-wider uppercase mb-1">Target Tile Divisibility Test</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            An animal reaches target tile <span class="text-amber-300 font-bold">64</span> only if
            <span class="text-emerald-400 font-semibold">64 is an exact multiple of its jump size</span>.
        </p>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs font-mono">
        <div class="bg-slate-800/80 p-3 rounded-lg border border-slate-700">
            <span class="text-emerald-400 font-bold block mb-1">🐰 Racer A (Step 4)</span>
            <span class="text-slate-300 block">64 ÷ 4 = 16 (Remainder 0)</span>
            <span class="text-emerald-300 text-[11px] block mt-1">✓ Lands exactly on tile 64 in 16 leaps!</span>
        </div>
        <div class="bg-slate-800/80 p-3 rounded-lg border border-slate-700">
            <span class="text-rose-400 font-bold block mb-1">🦌 Racer B (Step 6)</span>
            <span class="text-slate-300 block">64 ÷ 6 = 10 (Remainder 4)</span>
            <span class="text-rose-300 text-[11px] block mt-1">✗ Lands on 60, then 66 (Overshoots!)</span>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "question": "Can Racer B (jumping in steps of 6) land exactly on tile 64?",
                "options": [
                    "Yes, in 10 jumps",
                    "Yes, in 11 jumps",
                    "No, because 64 is not a multiple of 6",
                    "Yes, in 16 jumps"
                ],
                "answer": 2,
                "explanation": "64 ÷ 6 = 10 with remainder 4. 64 is not divisible by 6, so Racer B overshoots it.",
                "hint": "Check if 6 divides 64 without leaving a remainder."
            },
            {
                "question": "How many total leaps does Racer A (step 4) require to reach tile 64 from 0?",
                "options": ["12 leaps", "14 leaps", "16 leaps", "18 leaps"],
                "answer": 2,
                "explanation": "64 ÷ 4 = 16. Racer A reaches tile 64 in exactly 16 leaps.",
                "hint": "Divide 64 by 4."
            }
        ]
    }
]

if __name__ == '__main__':
    for s in slides_part1:
        wc = len(s['lecture'].split())
        status = "PASS" if 195 <= wc <= 215 else f"FAIL ({wc})"
        print(f"Slide {s['id']}: {wc} words [{status}]")
