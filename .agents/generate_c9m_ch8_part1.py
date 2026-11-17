#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics - Chapter 8: Predicting What Comes Next: Exploring Sequences and Progressions
Slides Data Generator - Part 1 (Slides 1 to 8)
Strictly covers 8.1 to 8.4.1 with 1-3 word headings, 195-215 spoken words, zero human names.
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Sequence Basics",
        "subtitle": "Section 8.1 Introduction to Sequences: Ordered Terms (t₁, t₂, ...), Finite vs Infinite & Familiar Number Patterns",
        "speech": (
            "Welcome to Class Nine Mathematics Chapter Eight: Predicting What Comes Next—Exploring Sequences and Progressions! "
            "Whenever astronomers track periodic comet returns, civil engineers space bridge support pillars evenly, or computer scientists analyze growing algorithmic patterns, mathematics begins by organizing numbers in strict order! In Section Eight Point One, a SEQUENCE is simply an ordered list of numbers arranged according to a definite pattern or rule, where every single number occupies a fixed numbered position called a TERM—written cleanly as t one, t two, t three, and onward! "
            "Notice TWO critical classifications right away! A FINITE SEQUENCE stops cleanly at a last final term—like all two-digit multiples of five starting at ten and ending at ninety-five! By contrast, an INFINITE SEQUENCE continues forever without end, marked cleanly by three trailing dots—such as the counting Natural Numbers one, two, three, four, continuing endlessly, or the Odd Numbers one, three, five, seven, or even numbers two, four, six, eight! "
            "Order ALWAYS matters inside every sequence: swapping terms two and five creates a completely different sequence! Throughout Chapter Eight, unlock crisp algebraic rules letting you jump straight ahead to any future term instantly and predict growing number patterns reliably without guessing!"
        ),
        "checkpoints": [
            {
                "question": "In sequence notation t₁, t₂, t₃, ..., what distinguishes a FINITE sequence from an INFINITE sequence?",
                "options": [
                    "A finite sequence terminates at a specific last term, whereas an infinite sequence continues endlessly",
                    "A finite sequence contains only odd numbers",
                    "An infinite sequence has zero pattern",
                    "Finite sequences cannot use negative numbers"
                ],
                "answer": 0,
                "hint": "Look for whether the ordered list has a final stopping term or trails onward with '...'!",
                "explanation": "Finite sequences have a fixed countable number of terms; infinite sequences continue without a last term."
            },
            {
                "question": "If a sequence begins 4, 9, 14, 19, ..., what are terms t₁ and t₄?",
                "options": [
                    "t₁ = 4 and t₄ = 19",
                    "t₁ = 1 and t₄ = 4",
                    "t₁ = 19 and t₄ = 4",
                    "t₁ = 5 and t₄ = 20"
                ],
                "answer": 0,
                "hint": "The subscript index tells the exact position from left to right!",
                "explanation": "Position 1 holds t₁ = 4, position 2 holds 9, position 3 holds 14, and position 4 holds t₄ = 19."
            }
        ]
    },
    {
        "id": 2,
        "title": "Triangular Square Sums",
        "subtitle": "Section 8.1 Familiar Sequences & Sum Relationships: Triangular Numbers (1, 3, 6, 10...) & Square Numbers (1, 4, 9, 16...)",
        "speech": (
            "Now inspect two breathtaking geometric dot patterns inside Section Eight Point One: TRIANGULAR NUMBERS and SQUARE NUMBERS! "
            "First stack bowling pins or glass marbles cleanly into equilateral triangular rows! Row one holds one dot; add two dots underneath giving three; add three more giving six; add four more giving ten; add five more giving fifteen! That iconic list—one, three, six, ten, fifteen, twenty-one—forms the TRIANGULAR NUMBERS! Look closely at WHY they grow that way: the nth triangular number EQUALS the exact sum of the first n consecutive natural numbers: one plus two plus three up to n! "
            "Now stack square grids of ceramic floor tiles cleanly! One by one uses one tile; two by two uses four tiles; three by three uses nine tiles; four by four uses sixteen tiles! Observe how each new L-shaped corner border wraps tightly around the previous smaller square! Adding one, then plus three, then plus five, then plus seven reveals a stunning hidden arithmetic law: EVERY SQUARE NUMBER n SQUARED EQUALS THE EXACT SUM OF THE FIRST n CONSECUTIVE ODD NUMBERS! Notice too that adding any two consecutive triangular numbers together always produces a perfect square number cleanly, such as six plus ten equalling sixteen!"
        ),
        "checkpoints": [
            {
                "question": "Which sum produces the 5th triangular number T₅?",
                "options": [
                    "1 + 2 + 3 + 4 + 5 = 15",
                    "1 + 3 + 5 + 7 + 9 = 25",
                    "2 + 4 + 6 + 8 + 10 = 30",
                    "5 × 5 = 25"
                ],
                "answer": 0,
                "hint": "Triangular numbers sum consecutive natural numbers starting from 1!",
                "explanation": "T₅ = 1 + 2 + 3 + 4 + 5 = 15."
            },
            {
                "question": "What exact sum of consecutive odd numbers equals the square number 6² = 36?",
                "options": [
                    "1 + 3 + 5 + 7 + 9 + 11 = 36 (first 6 odd numbers)",
                    "1 + 2 + 3 + 4 + 5 + 6 = 21",
                    "3 + 5 + 7 + 9 + 11 = 35",
                    "1 + 3 + 5 + 7 + 9 = 25"
                ],
                "answer": 0,
                "hint": "Sum the first n = 6 odd numbers starting at 1!",
                "explanation": "The sum of the first n odd numbers always equals n², so 1 + 3 + 5 + 7 + 9 + 11 = 6² = 36."
            }
        ]
    },
    {
        "id": 3,
        "title": "Explicit Position Rules",
        "subtitle": "Section 8.2 Explicit Rule for a Sequence: Direct Position Formulas (uₙ = 2n − 1), Jumping to t₅₃ / t₃₀₀ & Membership Testing",
        "speech": (
            "Suppose someone asks you for the THREE-HUNDREDTH odd number right now! Would you patiently write out two hundred ninety-nine earlier numbers one by one? Of course NOT! Section Eight Point Two unlocks our express highway: AN EXPLICIT RULE! "
            "An EXPLICIT FORMULA (written t sub n, u sub n, or S sub n) expresses ANY term directly as an algebraic expression using ONLY its position index n! Look at the odd numbers: position one gives one, position two gives three, position three gives five! Plugging position n directly into u sub n equals two n minus one generates ANY term immediately! Want the fifty-third odd number? Compute two times fifty-three minus one equals ONE HUNDRED FIVE instantaneously! Want the three-hundredth? Compute two times three hundred minus one equals FIVE HUNDRED NINETY-NINE in one second! "
            "Even better, explicit rules act like precision membership detectors! Does the number eighty-four belong anywhere inside the sequence t sub n equals three n plus two? Solve three n plus two equals eighty-four giving three n equals eighty-two—which is NOT divisible cleanly by three! Because n equals twenty-seven point three three is NOT a positive whole integer, eighty-four definitely does NOT belong!"
        ),
        "checkpoints": [
            {
                "question": "Using the explicit rule tₙ = 4n − 3, what is the 50th term t₅₀?",
                "options": ["197", "200", "203", "193"],
                "answer": 0,
                "hint": "Substitute n = 50 directly into 4n − 3!",
                "explanation": "t₅₀ = 4(50) − 3 = 200 − 3 = 197."
            },
            {
                "question": "Is 73 a member of the sequence defined by tₙ = 5n + 2 (for positive integers n ≥ 1)?",
                "options": [
                    "No, because 5n + 2 = 73 gives n = 71/5 = 14.2, which is NOT a whole position integer",
                    "Yes, at position n = 14",
                    "Yes, at position n = 15",
                    "Cannot be tested without listing all earlier terms"
                ],
                "answer": 0,
                "hint": "Set 5n + 2 = 73 and check if n is a positive integer!",
                "explanation": "5n = 71 ⇒ n = 14.2 ∉ ℕ, proving 73 is not in this sequence."
            }
        ]
    },
    {
        "id": 4,
        "title": "Recursive Sequence Rules",
        "subtitle": "Section 8.3 Recursive Rule for a Sequence: Previous-Term Relationships (t₁ = 1, tₙ = tₙ₋₁ + 3) vs Explicit Rules",
        "speech": (
            "Now explore a completely different style of mathematical recipe inside Section Eight Point Three: THE RECURSIVE RULE! "
            "While an explicit rule calculates term t sub n directly from position number n alone, a RECURSIVE RULE builds each brand-new term step by step straight from ONE OR MORE PRECEDING TERMS! "
            "Examine a simple recursive definition: start with initial anchor term t one equals one, and follow step rule t sub n equals t sub n minus one PLUS THREE for every position n greater than or equal to two! Watch it unfold like climbing stairs: t one equals one; t two equals one plus three equals four; t three equals four plus three equals seven; t four equals seven plus three equals ten! "
            "Notice TWO crucial requirements for EVERY recursive rule! First, you MUST specify starting base value(s) like t one—without a starting anchor, the entire chain floats in mid-air! Second, recursive rules wonderfully mirror step-by-step natural growth, compound savings account balances, and computer programming loops, yet jumping straight ahead to t three hundred requires computing all two hundred ninety-nine earlier terms unless converted cleanly into an explicit algebraic position formula, which lets you leap straight ahead to any distant term in one single calculation!"
        ),
        "checkpoints": [
            {
                "question": "A sequence is defined recursively by t₁ = 5 and tₙ = 2·tₙ₋₁ − 1 for n ≥ 2. What is the 4th term t₄?",
                "options": ["33 (sequence: 5, 9, 17, 33)", "17", "65", "11"],
                "answer": 0,
                "hint": "Step forward one term at a time: t₂ = 2(5)−1 = 9, then t₃, then t₄!",
                "explanation": "t₁ = 5, t₂ = 9, t₃ = 2(9)−1 = 17, t₄ = 2(17)−1 = 33."
            },
            {
                "question": "Why must EVERY recursive rule specify at least one initial starting term (such as t₁)?",
                "options": [
                    "Because without a starting anchor value, the step-by-step chain cannot begin calculating subsequent terms",
                    "Because n = 1 always equals zero otherwise",
                    "Because recursive rules only generate 3 terms",
                    "To prevent negative numbers"
                ],
                "answer": 0,
                "hint": "Think: if t₂ = t₁ + 3, how can you evaluate t₂ if t₁ is unknown?",
                "explanation": "Base/anchor values initialize the recurrence relation so every later term becomes uniquely determined."
            }
        ]
    },
    {
        "id": 5,
        "title": "Virahānka Fibonacci History",
        "subtitle": "Section 8.3 Virahānka-Fibonacci Sequence: V₁ = 1, V₂ = 2, Vₙ = Vₙ₋₁ + Vₙ₋₂ (Virahānka, Gopāla, Hemachandra & Fibonacci)",
        "speech": (
            "Celebrate one of India's greatest mathematical contributions to world science inside Section Eight Point Three: THE VIRAHĀNKA-FIBONACCI SEQUENCE! "
            "Over five hundred years BEFORE Italian mathematician Fibonacci wrote about rabbit populations in twelve hundred two CE, seventh-century Indian prosodist VIRAHĀNKA—followed cleanly by scholars Gopāla and Hemachandra—discovered this exact sequence while analyzing Sanskrit poetic meters! Poets arranged short one-beat syllables and long two-beat syllables! How many rhythmic combinations total n beats? "
            "Check small beat counts systematically! For one beat: one way (short). For two beats: two ways (short-short, or one long). For three beats: three rhythmic ways! For four beats: five ways! For five beats: eight ways! Look closely at the underlying mathematical pattern: V one equals one, V two equals two, and EVERY subsequent term sums the TWO IMMEDIATELY PRECEDING TERMS: V sub n equals V sub n minus one PLUS V sub n minus two! "
            "Adding consecutive pairs together steadily builds one, two, three, five, eight, thirteen, twenty-one, thirty-four, fifty-five, eighty-nine! Today, Virahānka-Fibonacci numbers appear everywhere from sunflower seed spirals, tree branching, leaf arrangements, and pinecone scales across nature to modern computer algorithms, golden ratio geometry, botanical spirals, digital search techniques, and classical architectural proportions across our entire natural world!"
        ),
        "checkpoints": [
            {
                "question": "In the Virahānka-Fibonacci sequence V₁ = 1, V₂ = 2, Vₙ = Vₙ₋₁ + Vₙ₋₂, what are the 6th and 7th terms (V₆ and V₇)?",
                "options": [
                    "V₆ = 13 and V₇ = 21",
                    "V₆ = 8 and V₇ = 13",
                    "V₆ = 12 and V₇ = 20",
                    "V₆ = 21 and V₇ = 34"
                ],
                "answer": 0,
                "hint": "List carefully from V₁ = 1, V₂ = 2: 1, 2, 3, 5, 8, ...!",
                "explanation": "V₁=1, V₂=2, V₃=3, V₄=5, V₅=8, V₆=5+8=13, V₇=8+13=21."
            },
            {
                "question": "What real-world cultural domain led Virahānka (7th century CE), Gopāla, and Hemachandra to discover this sequence centuries before Fibonacci?",
                "options": [
                    "Counting rhythmic combinations of short (1-beat) and long (2-beat) syllables in Sanskrit poetic meters",
                    "Measuring ocean tidal heights",
                    "Building circular athletic running tracks",
                    "Solving quadratic equations for gold coins"
                ],
                "answer": 0,
                "hint": "Recall Indian prosody (chandas) combining 1-beat laghu and 2-beat guru syllables!",
                "explanation": "Indian prosodists counted n-beat rhythmic patterns formed from 1-beat and 2-beat syllables, yielding Vₙ = Vₙ₋₁ + Vₙ₋₂."
            }
        ]
    },
    {
        "id": 6,
        "title": "Arithmetic Progression Basics",
        "subtitle": "Section 8.4 Arithmetic Progressions: Constant Common Difference (d) & General Form a, a + d, a + 2d, ...",
        "speech": (
            "Now step into the workhorse sequence of algebra, finance, and physics inside Section Eight Point Four: ARITHMETIC PROGRESSIONS, abbreviated simply as APs! "
            "Suppose a mountain climber climbs three hundred metres higher every single hour, or a savings jar adds fifty rupees every week, or a hot oven cools by four degrees every minute! Look closely at the exact gap between any two consecutive terms: always subtract the earlier term from the very next term, and the difference stays COMPLETELY CONSTANT! "
            "An ARITHMETIC PROGRESSION is a sequence in which every term after the first is obtained by ADDING a fixed constant number—called the COMMON DIFFERENCE d—to the preceding term! Denote the first term by letter a! Then the general form of EVERY AP reads smoothly: a, a plus d, a plus two d, a plus three d, continuing endlessly! "
            "Watch out for negative and zero differences too! When terms decrease steadily like twenty, sixteen, twelve, eight, compute d equals sixteen minus twenty equals NEGATIVE FOUR—never reverse the subtraction order! When every term stays completely identical like seven, seven, seven, seven, common difference d equals ZERO, giving a completely flat constant horizontal arithmetic progression whose terms never rise or fall at any position!"
        ),
        "checkpoints": [
            {
                "question": "Which of the following sequences is a valid Arithmetic Progression (AP), and what is its common difference d?",
                "options": [
                    "17, 13, 9, 5, ... (AP with d = −4)",
                    "2, 4, 8, 16, ... (d = 2)",
                    "1, 4, 9, 16, ... (d = 3)",
                    "1, 2, 3, 5, 8, ... (d = 1)"
                ],
                "answer": 0,
                "hint": "Subtract consecutive pairs (t₂ − t₁, t₃ − t₂, t₄ − t₃) and check whether the difference stays identical!",
                "explanation": "13−17 = −4, 9−13 = −4, 5−9 = −4; constant difference confirms an AP with d = −4."
            },
            {
                "question": "In an AP with first term a = −6 and common difference d = 2.5, what are the first four terms?",
                "options": [
                    "−6, −3.5, −1, 1.5",
                    "−6, −8.5, −11, −13.5",
                    "−6, −15, −37.5, −93.75",
                    "2.5, −3.5, −9.5, −15.5"
                ],
                "answer": 0,
                "hint": "Add d = +2.5 repeatedly starting from a = −6!",
                "explanation": "−6, −6 + 2.5 = −3.5, −3.5 + 2.5 = −1, −1 + 2.5 = 1.5."
            }
        ]
    },
    {
        "id": 7,
        "title": "AP Nth Term",
        "subtitle": "Section 8.4 General Formula: Explicit nth Term tₙ = a + (n − 1)d & Recursive Formulation t₁ = a, tₙ = tₙ₋₁ + d",
        "speech": (
            "Now derive the golden explicit formula for ANY Arithmetic Progression inside Section Eight Point Four! "
            "Look closely at how many steps of common difference d it takes to reach position n starting from first term a! Term one adds ZERO d's: a plus zero d! Term two adds ONE d: a plus one d! Term three adds TWO d's: a plus two d! Term ten adds NINE d's! "
            "Notice the universal pattern every single time: the coefficient multiplying common difference d is ALWAYS ONE LESS than position number n! That immediately proves our famous AP nth-term explicit formula: t sub n EQUALS a PLUS open n minus one close TIMES d! Meanwhile, its twin recursive form reads t one equals a and t sub n equals t sub n minus one plus d! "
            "Test this powerhouse equation right now! Given AP five, nine, thirteen, seventeen, ..., find the thirty-fifth term t thirty-five! Identify first term a equals five and common difference d equals nine minus five equals four! Plug n equals thirty-five straight in: five plus open thirty-five minus one close times four equals five plus thirty-four times four equals ONE HUNDRED FORTY-ONE instantaneously without listing thirty-four earlier terms!"
        ),
        "checkpoints": [
            {
                "question": "Find the 25th term t₂₅ of the Arithmetic Progression 7, 12, 17, 22, ...",
                "options": ["127", "132", "122", "125"],
                "answer": 0,
                "hint": "Here a = 7, d = 5, and n = 25; compute 7 + (25 − 1) × 5!",
                "explanation": "t₂₅ = 7 + 24 × 5 = 7 + 120 = 127."
            },
            {
                "question": "Which position n in the AP 3, 8, 13, 18, ... equals 98?",
                "options": ["n = 20 (20th term)", "n = 19", "n = 21", "n = 25"],
                "answer": 0,
                "hint": "Solve 3 + (n − 1)(5) = 98 ⇒ 5(n − 1) = 95!",
                "explanation": "5(n − 1) = 95 ⇒ n − 1 = 19 ⇒ n = 20."
            }
        ]
    },
    {
        "id": 8,
        "title": "Visualising Linear APs",
        "subtitle": "Section 8.4.1 Visualising an AP: Plotting Ordered Pairs (n, tₙ) Yields Collinear Points Along a Straight Line",
        "speech": (
            "Connect sequences seamlessly back to Coordinate Geometry inside Section Eight Point Four Point One: VISUALISING AN AP! "
            "What picture appears if we treat each position number n as an x-coordinate and its term value t sub n as a y-coordinate, plotting every ordered pair open n comma t sub n close cleanly onto a Cartesian coordinate grid? "
            "Test an example right now! Take AP two, five, eight, eleven, fourteen, ... where a equals two and d equals three! Plot points one-comma-two, two-comma-five, three-comma-eight, four-comma-eleven, and five-comma-fourteen! Lay a straight wooden ruler across those dots—EVERY SINGLE POINT LIES PERFECTLY ALONG ONE STRAIGHT LINE! "
            "Why does EVERY Arithmetic Progression form a straight line? Rewrite t sub n equals a plus open n minus one close d neatly as t sub n equals d TIMES n PLUS open a minus d close! Notice that matches linear coordinate equation y equals m x plus c! Stepping right horizontally by one unit ALWAYS climbs vertically by exact constant slope d—rising steadily upward for positive d, sloping downward for negative d, and lying completely flat horizontally across the coordinate grid when d equals zero, matching a constant horizontal line whose vertical height never changes!"
        ),
        "checkpoints": [
            {
                "question": "When ordered pairs (n, tₙ) of any Arithmetic Progression are plotted on a coordinate plane, what geometric shape do the points ALWAYS trace?",
                "options": [
                    "Points lying strictly along a single straight line (with slope equal to common difference d)",
                    "A steeply curving exponential arc",
                    "A closed circle",
                    "A zigzagging parabola"
                ],
                "answer": 0,
                "hint": "Every +1 step in n produces a constant vertical shift +d in tₙ!",
                "explanation": "tₙ = d·n + (a − d) is linear in n, so all plotted points (n, tₙ) are collinear with slope d."
            },
            {
                "question": "If plotting (n, tₙ) of an AP produces a straight line sloping DOWNWARD from left to right, what must be true about its common difference d?",
                "options": [
                    "d < 0 (negative common difference)",
                    "d > 0 (positive common difference)",
                    "d = 0",
                    "d must equal a"
                ],
                "answer": 0,
                "hint": "Downward slope means term values decrease as position n increases!",
                "explanation": "Decreasing terms tₙ₊₁ < tₙ mean d = tₙ₊₁ − tₙ < 0."
            }
        ]
    }
]
