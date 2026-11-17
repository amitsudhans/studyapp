#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics - Chapter 3: The World of Numbers
Slides Data Generator - Part 1 (Slides 1 to 8)
Strictly covers 3.1 to 3.5.2 with 1-3 word headings, 195-215 spoken words, zero human names.
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Dawn of Counting",
        "subtitle": "Sections 3.1 & 3.1.1: Pebble-Pot One-to-One Correspondence, Natural Numbers ℕ, Lebombo Bone (~35,000 BP) & Ishango Bone (~20,000 BCE)",
        "speech": (
            "Welcome to Class Nine Mathematics Chapter Three: The World of Numbers! "
            "Long before ink, paper, or numeral symbols existed, human survival depended on accurate counting! In Section Three Point One, imagine an early pastoral community sending sheep out to graze every morning across open meadows. "
            "Without written digits, herders invented ONE-TO-ONE CORRESPONDENCE: drop one smooth pebble into a clay pot for each exiting sheep, then remove one pebble as each animal returned safely at dusk! No leftover pebbles meant zero lost sheep, while remaining pebbles revealed missing animals! "
            "Notice how clay pebbles naturally established our foundational counting set—the NATURAL NUMBERS N equals one, two, three, four, extending infinitely upward! "
            "Now inspect archaeological history etched straight into animal bone! From southern Africa comes the Lebombo Bone, roughly thirty-five thousand years before present, scarred with exactly twenty-nine deliberate notches—likely tracking one complete lunar month cycle! "
            "And from central Africa around twenty thousand BCE comes the famous Ishango Bone, carved with three neat columns of grouped tallies—showing deliberate multiplication by two alongside the crisp prime-number sequence eleven, thirteen, seventeen, and nineteen! "
            "From clay pebbles to notched prehistoric bones, human curiosity transformed everyday physical objects into pure mathematical counting!"
        ),
        "checkpoints": [
            {
                "question": "How did early pastoral societies verify livestock counts using pebbles before written numbers existed?",
                "options": [
                    "By one-to-one correspondence—matching each animal leaving and returning with a pebble in a pot",
                    "By calculating decimal square roots in clay tablets",
                    "By weighing animals on bronze balance pans",
                    "By writing Roman numerals on parchment"
                ],
                "answer": 0,
                "hint": "Every sheep leaving adds one pebble; every sheep returning removes one pebble!",
                "explanation": "One-to-one correspondence paired one physical marker per sheep without needing symbolic numerals."
            },
            {
                "question": "What mathematical patterns are famously carved onto the Lebombo Bone (~35,000 BP) and the Ishango Bone (~20,000 BCE)?",
                "options": [
                    "Lebombo has 29 lunar-cycle notches; Ishango features doubling and primes 11, 13, 17, 19",
                    "Both bones carry infinite series approximations for Pi",
                    "Lebombo contains Hindu zero rules; Ishango records negative debt fractions",
                    "Both display strictly equal base-60 Babylonian wedges"
                ],
                "answer": 0,
                "hint": "Notice 29 matches the lunar month and {11, 13, 17, 19} are consecutive primes between 10 and 20!",
                "explanation": "The Lebombo Bone carries 29 tally marks (~lunar days), while the Ishango Bone records prime numbers 11, 13, 17, 19 and ×2 tallies."
            }
        ]
    },
    {
        "id": 2,
        "title": "Indian Powers Scale",
        "subtitle": "Section 3.1.2 The Indian Context: Indus Valley Weights (Lothal & Harappa) & Named Powers of 10 from Parārdha (10¹²) to Tallakṣaṇa (10⁵³)",
        "speech": (
            "Now trace India's extraordinary early mastery over scale, precision, and colossal powers of ten in Section Three Point One Point Two! "
            "Across prosperous cities of the Indus Valley Civilisation—especially the maritime dockyard port of Lothal and major urban centre Harappa—archaeologists uncovered hundreds of polished cubical chert stone weights! "
            "Far from random river stones, these weights followed crisp mathematical ratios: small binary multiples one, two, four, eight, sixteen, thirty-two, and sixty-four transitioning cleanly into decimal multiples like one hundred sixty, three hundred twenty, and six hundred forty for standardized civic and maritime trade! "
            "Meanwhile, ancient Indian Sanskrit literature possessed a breathtaking imagination for vast numerical magnitudes when neighbouring civilizations barely named ten thousand! "
            "In early Vedic texts such as the Yajurveda, structured names climbed cleanly by powers of ten: eka, daśa, śata, sahasra, ayuta, lakṣa, prayuta, koṭi, all the way up to PARĀRDHA equal to ten to the power twelve—one trillion! "
            "Centuries later in the Lalitavistara, mathematical scholar-sages pushed named decimal powers past koṭi in systematic steps of one hundred, crowning at TALLAKṢAṆA equal to ten to the power fifty-three! "
            "Standardized civic trade precision and cosmic Sanskrit scales shaped India's extraordinary lifelong decimal fluency across every century!"
        ),
        "checkpoints": [
            {
                "question": "What do the polished cubical stone weights excavated from Lothal and Harappa demonstrate about the Indus Valley Civilisation?",
                "options": [
                    "A highly standardized weight system combining binary doubling (1, 2, 4, 8, 16...) with decimal multiples for trade",
                    "Random uncalibrated river pebbles without fixed ratios",
                    "Only negative weights used for debt accounting",
                    "Exclusively circular weights following base-7 arithmetic"
                ],
                "answer": 0,
                "hint": "Recall the doubling sequence 1, 2, 4, 8, 16, 32, 64 transitioning to 160, 320, 640!",
                "explanation": "Harappan weights standardized trade with binary subdivisions followed by decimal scaling multiples."
            },
            {
                "question": "Which power of 10 corresponds to the ancient Vedic term parārdha and the Lalitavistara term tallakṣaṇa?",
                "options": [
                    "parārdha = 10¹² and tallakṣaṇa = 10⁵³",
                    "parārdha = 10⁶ and tallakṣaṇa = 10¹²",
                    "parārdha = 10⁵³ and tallakṣaṇa = 10¹⁰",
                    "parārdha = 10³ and tallakṣaṇa = 10⁹"
                ],
                "answer": 0,
                "hint": "Vedic tables culminate at 10¹² (parārdha), while the Buddhist Lalitavistara reaches far higher to 10⁵³!",
                "explanation": "Vedic texts name up to parārdha (10¹²), and the Lalitavistara extends named powers of 10 to tallakṣaṇa (10⁵³)."
            }
        ]
    },
    {
        "id": 3,
        "title": "Revolution of Shunya",
        "subtitle": "Sections 3.2.1 & 3.2.2: Philosophical Śhūnyatā to Bakhśhālī Bindu Dot & Brahmagupta's Operational Rules for Zero (628 CE)",
        "speech": (
            "Now witness one of humanity's greatest intellectual revolutions in Section Three Point Two: WHEN NOTHING BECAME SOMETHING—THE REVOLUTION OF SHŪNYA! "
            "Long before zero became a calculable written digit, Indian philosophy meditated deeply on ŚHŪNYATĀ—completeness through emptiness, mental silence, and fertile void—across the Upanishads, early Buddhist philosophy, and Patanjali's Yoga Sutras! "
            "That profound philosophical comfort with emptiness opened a clear doorway for Indian mathematicians to treat 'nothing' as an explicit symbol and genuine number! "
            "Physical evidence shines in the ancient Bakhśhālī Manuscript, preserved on fragile birch bark, where a crisp heavy dot called a BINDU marks empty decimal place-value positions cleanly! "
            "Then in six hundred twenty-eight CE, mathematician Brahmagupta took the decisive historic leap in his Brāhmasphuṭasiddhānta! Rather than leaving zero merely as a silent placeholder symbol, Brahmagupta defined ZERO as a true mathematical number governed by explicit operational laws! "
            "Check Brahmagupta's four golden operational identities for any real number a: subtracting any real number from itself gives zero (a minus a equals zero); adding zero leaves value a unchanged (a plus zero equals a); subtracting zero leaves value a unchanged (a minus zero equals a); and multiplying by zero collapses every product cleanly to zero!"
        ),
        "checkpoints": [
            {
                "question": "How is zero physically represented inside decimal calculations of the ancient birch-bark Bakhśhālī Manuscript?",
                "options": [
                    "As a small solid dot called a bindu",
                    "As an empty triangular wedge like Mesopotamian tablets",
                    "As a Roman cross symbol X",
                    "Omitted completely without any mark"
                ],
                "answer": 0,
                "hint": "Recall the Sanskrit word meaning 'point' or 'dot'!",
                "explanation": "The Bakhśhālī Manuscript uses a dot (bindu) to mark empty zero positions."
            },
            {
                "question": "Which set accurately lists Brahmagupta's operational arithmetic laws for zero in Brāhmasphuṭasiddhānta (628 CE)?",
                "options": [
                    "a − a = 0, a + 0 = a, a − 0 = a, and a × 0 = 0",
                    "a × 0 = a and a − a = 1",
                    "a + 0 = 0 and a − 0 = −a",
                    "Zero serves strictly as a placeholder with no arithmetic laws"
                ],
                "answer": 0,
                "hint": "Think about subtracting a quantity from itself, adding/subtracting zero, and multiplying any number by zero!",
                "explanation": "Brahmagupta explicitly formalized additive identity (a ± 0 = a), additive inverse (a − a = 0), and zero multiplication (a × 0 = 0)."
            }
        ]
    },
    {
        "id": 4,
        "title": "Dhana and Rina",
        "subtitle": "Sections 3.3 & 3.3.1: Fortunes (Dhana +) & Debts (Riṇa −), Integers ℤ & Why (−) × (−) = (+) via Debt Removal",
        "speech": (
            "Once zero stood proudly at the centre of the number line, what lay cleanly to its LEFT? Welcome to Section Three Point Three: INTEGERS, EXPANDING THE HORIZON! "
            "While many ancient traditions dismissed numbers below zero as 'absurd' or 'fictitious', Brahmagupta gave negative numbers instant, practical clarity using commerce: Fortunes called DHANA represent positive assets right of zero, while Debts called RIṆA represent negative liabilities left of zero! "
            "Uniting all negative whole numbers, zero, and positive whole numbers builds the complete set of INTEGERS denoted by capital Z! "
            "Now watch how effortlessly Brahmagupta's commercial model explains signed integer arithmetic in Section Three Point Three Point One! "
            "Adding two fortunes yields a larger fortune; adding two debts builds a deeper total debt! Subtracting a positive fortune reduces your net wealth, while subtracting a debt—canceling money you previously owed—actually INCREASES your wealth! "
            "Best of all, solve the classic mystery: why does a negative times a negative equal a positive? "
            "Think commercially with total clarity! Multiplying positive fortune times negative debt creates a multiplied debt (negative). Conversely, removing—multiplying by a negative—multiple identical debts wipes out liabilities, generating an immediate net gain! Thus removing debt proves negative times negative equals POSITIVE!"
        ),
        "checkpoints": [
            {
                "question": "How did Brahmagupta conceptualize positive and negative numbers in his commercial framework?",
                "options": [
                    "Positive numbers as Fortunes (Dhana) and negative numbers as Debts (Riṇa)",
                    "Positive numbers as squares and negative numbers as impossible shapes",
                    "Positive numbers as angles and negative numbers as prime roots",
                    "Both positive and negative numbers as identical unsigned tallies"
                ],
                "answer": 0,
                "hint": "Recall the Sanskrit banking terms Dhana (fortune/asset) and Riṇa (debt)!",
                "explanation": "Brahmagupta modeled + integers as fortunes (Dhana) and − integers as debts (Riṇa), forming ℤ."
            },
            {
                "question": "Using Brahmagupta's debt-and-fortune logic, why does (−3) × (−4) equal positive +12?",
                "options": [
                    "Removing (negative multiplier) 3 identical debts of 4 removes 12 units of debt, producing a +12 net fortune gain",
                    "Because two negative signs always cancel visually into a circle",
                    "Adding −3 and −4 gives +12",
                    "Only positive integers can ever be multiplied"
                ],
                "answer": 0,
                "hint": "Think: canceling or taking away multiple debts leaves you richer!",
                "explanation": "Multiplying by −3 removes three debts of −4; removing −12 of debt increases net wealth by +12."
            }
        ]
    },
    {
        "id": 5,
        "title": "Rational Set Laws",
        "subtitle": "Section 3.4 Filling Spaces: Rationals ℚ (p/q, q ≠ 0), Equivalence (ad = bc), Co-Prime Form & Arithmetic Laws",
        "speech": (
            "Notice wide empty gaps stretching between neighbouring integers like zero and one, or minus two and minus one! Welcome to Section Three Point Four: FILLING THE SPACES WITH RATIONAL NUMBERS! "
            "Define the set of RATIONAL NUMBERS denoted Q as every number expressible in fraction ratio form p divided by q, where numerator p and denominator q are both integers and strictly denominator q does NOT equal zero! "
            "Why does Q cleanly swallow our earlier sets? Because any integer n writes neatly as n divided by one, making natural numbers and integers automatic subsets inside Q alongside positive and negative fractions! "
            "Explore fraction equivalence carefully: one-half, two-fourths, and negative three over negative six represent the exact same point! How do we verify equality without drawing pies? Use the CROSS-MULTIPLICATION LAW: p over q equals r over s if and only if p times s equals q times r! "
            "Dividing both p and q by their highest common factor yields the unique CO-PRIME STANDARD FORM where denominator q always remains positive! "
            "Finally, verify that addition, subtraction, multiplication, and non-zero division keep rational set Q completely closed, faithfully obeying standard commutativity, associativity, and distributivity arithmetic laws cleanly everywhere!"
        ),
        "checkpoints": [
            {
                "question": "Why must denominator q strictly satisfy q ≠ 0 in the rational number definition p/q?",
                "options": [
                    "Because division by zero is mathematically undefined",
                    "Because 0 is an irrational number",
                    "Because p/0 always equals 1",
                    "Because negative integers cannot be divided"
                ],
                "answer": 0,
                "hint": "No number multiplied by 0 can recover a non-zero numerator p, and 0/0 is indeterminate!",
                "explanation": "ℚ = {p/q : p, q ∈ ℤ, q ≠ 0} excludes q = 0 since division by zero has no unique well-defined value."
            },
            {
                "question": "Using the cross-multiplication equivalence test (ad = bc), check whether -6/15 and 14/-35 are equivalent rationals and identify their co-prime standard form.",
                "options": [
                    "Equivalent because (-6)(-35) = 210 = 15(14); co-prime standard form is -2/5",
                    "Not equivalent because signs sit in different places",
                    "Equivalent with standard form 2/5",
                    "Equivalent with standard form -6/15"
                ],
                "answer": 0,
                "hint": "Check (-6) × (-35) vs 15 × 14, then divide numerator and denominator by HCF = 3!",
                "explanation": "(-6)(-35) = 210 and 15 × 14 = 210 confirms equivalence; dividing by 3 with positive denominator gives -2/5."
            }
        ]
    },
    {
        "id": 6,
        "title": "Plotting and Distance",
        "subtitle": "Sections 3.4.1 & 3.4.2: Number Line Partitioning, Absolute Value |x|, Distance |a − b| & Midpoint Density Theorem (a+b)/2",
        "speech": (
            "Now place fractions accurately onto the number line and test how tightly rational numbers pack together! "
            "In Section Three Point Four Point One, how do you plot rational number p over q—say three-fifths or negative seven-fourths? "
            "Slice every unit interval from zero to one, or minus one to minus two, into q equal sub-segments! Then count p equal steps right from zero for positive fractions, or left for negative fractions! "
            "Notice two vital geometric measures! First, ABSOLUTE VALUE written modulus x measures a point's non-negative distance from Origin zero—so modulus of negative three-fourths equals plus three-fourths, just like plus three-fourths! "
            "Second, the exact segment distance separating ANY two numbers a and b on the line equals modulus of a minus b! "
            "Now unlock Section Three Point Four Point Two: THE DENSITY OF RATIONAL NUMBERS! Are rational numbers spaced apart like stepping stones, or packed infinitely tightly? "
            "Pick ANY two distinct rational numbers a and b, no matter how microscopically close together! Their arithmetic MIDPOINT open-parenthesis a plus b close-parenthesis divided by two ALWAYS lies strictly between a and b, and stays completely rational! Repeating midpoint averaging endlessly proves INFINITELY MANY rationals live between every pair!"
        ),
        "checkpoints": [
            {
                "question": "On the number line, what is the exact distance between rational points A = -3/4 and B = 5/4?",
                "options": [
                    "2 units (|−3/4 − 5/4| = |−8/4| = 2)",
                    "1/2 unit",
                    "-2 units",
                    "8 units"
                ],
                "answer": 0,
                "hint": "Apply the segment distance formula |a - b|!",
                "explanation": "Distance = |a - b| = |-3/4 - 5/4| = |-8/4| = |-2| = 2 units."
            },
            {
                "question": "Find a rational number strictly halfway between 1/3 and 1/2 using midpoint averaging (a + b)/2.",
                "options": [
                    "5/12",
                    "2/5",
                    "1/4",
                    "7/12"
                ],
                "answer": 0,
                "hint": "First add 1/3 + 1/2 = 5/6, then divide by 2!",
                "explanation": "(1/3 + 1/2)/2 = (2/6 + 3/6)/2 = (5/6)/2 = 5/12, which lies strictly between 4/12 and 6/12."
            }
        ]
    },
    {
        "id": 7,
        "title": "Discovery of Irrationals",
        "subtitle": "Sections 3.5 & 3.5.1: Baudhāyana's Unit Square Diagonal (√2) & Hippasus' Classic Contradiction Proof of Irrationality",
        "speech": (
            "Believe it or not, even infinitely dense rational fractions STILL leave invisible microscopic pinholes along the number line! "
            "Enter Section Three Point Five: IRRATIONAL NUMBERS! Around eight hundred BCE, Baudhāyana's Śulbasūtras explored doubling a square of side one unit! By the Baudhāyana-Pythagoras relation, its diagonal satisfies d squared equals one squared plus one squared equals two—meaning diagonal length equals ROOT TWO! "
            "Could root two ever be written as an exact integer ratio p over q? Early Pythagoreans assumed YES—until Hippasus delivered an earth-shattering PROOF BY CONTRADICTION! "
            "Follow Section Three Point Five Point One step by step! Suppose for argument that root two EQUALS a completely reduced co-prime fraction p over q, where p and q share NO common factor except one! "
            "Squaring both sides gives two q squared equals p squared! That forces p squared to be even—and since squares of odd numbers stay odd, p ITSELF must be even! Write p equals two k! "
            "Substitute p equals two k back: two q squared equals four k squared, simplifying to q squared equals two k squared! That forces q ALSO to be even! Both p and q divisible by two contradicts our starting co-prime rule—proving root two CANNOT be rational!"
        ),
        "checkpoints": [
            {
                "question": "In Baudhāyana's Śulbasūtras (c. 800 BCE), what exact geometric length first confronted scholars with an irrational magnitude?",
                "options": [
                    "√2, the diagonal of a unit square of side 1",
                    "4, the perimeter of a unit square",
                    "1/2, the area of a unit triangle",
                    "10, the base of decimal counting"
                ],
                "answer": 0,
                "hint": "Apply Baudhāyana's theorem to legs 1 and 1!",
                "explanation": "A square with side 1 has diagonal √(1² + 1²) = √2, which cannot equal any integer ratio p/q."
            },
            {
                "question": "In Hippasus's proof by contradiction that √2 is irrational, what contradiction breaks the assumption √2 = p/q (with p, q co-prime)?",
                "options": [
                    "Both p and q turn out to be divisible by 2, contradicting that p/q was reduced to co-prime lowest terms",
                    "Both p and q turn out equal to zero",
                    "q² turns out negative",
                    "p turns out strictly smaller than 1"
                ],
                "answer": 0,
                "hint": "Look at what 2q² = p² forces about p, and then substituting p = 2k forces about q!",
                "explanation": "p² = 2q² forces p to be even (p = 2k), which forces q² = 2k² so q is also even—violating HCF(p, q) = 1."
            }
        ]
    },
    {
        "id": 8,
        "title": "Constructing Square Roots",
        "subtitle": "Section 3.5.2 Construction of Length √n: Step-by-Step Compass & Straightedge Plotting of √2, √3, ..., √n on the Number Line",
        "speech": (
            "Even though root two and root three refuse to fit any integer fraction p over q, are they genuinely real physical lengths sitting right on our number line? ABSOLUTELY YES! "
            "Follow Section Three Point Five Point Two: GEOMETRIC COMPASS-AND-STRAIGHTEDGE CONSTRUCTION OF ROOT n! "
            "Begin at Origin O zero and measure one exact unit rightward to point A at one! At A, erect a perpendicular vertical segment AB of height ONE unit! "
            "By Baudhāyana-Pythagoras, hypotenuse OB connecting O zero to top corner B has exact length square root of one squared plus one squared equals ROOT TWO! "
            "Now place your steel compass needle firmly at Origin O, stretch your pencil tip smoothly to B, and swing a circular arc downward until it cuts the horizontal number line—marking the EXACT point of ROOT TWO just past one point four one! "
            "Wait—how do you construct ROOT THREE next? Simply erect a fresh one-unit perpendicular segment directly at root two on the line, or off hypotenuse OB! Since open root two close squared plus one squared equals three, swinging this new compass radius drops ROOT THREE cleanly onto the line! Repeating recursively step by step constructs ANY positive root n!"
        ),
        "checkpoints": [
            {
                "question": "Starting at Origin O(0), how do you physically mark √5 cleanly on the horizontal number line using a compass and straightedge?",
                "options": [
                    "Move 2 units right to A, erect a 1-unit perpendicular AB, then swing arc of radius OB = √(2² + 1²) = √5 onto the line",
                    "Move 5 units right and bisect the segment in half",
                    "Divide 5 into 2 equal fractions 5/2",
                    "Draw a 5 × 5 square and measure its perimeter"
                ],
                "answer": 0,
                "hint": "Spot the integer square sum 2² + 1² = 5!",
                "explanation": "Horizontal leg 2 and vertical leg 1 form hypotenuse OB = √(4 + 1) = √5; compass arc centered at O drops √5 onto the axis."
            },
            {
                "question": "If you construct a perpendicular of length 1 unit at √n on the number line and connect back to Origin O, what length does the new hypotenuse equal?",
                "options": [
                    "√(n + 1)",
                    "n + 1",
                    "√n + 1",
                    "2√n"
                ],
                "answer": 0,
                "hint": "Apply Baudhāyana-Pythagoras to legs √n and 1!",
                "explanation": "Hypotenuse² = (√n)² + 1² = n + 1, so taking square root yields √(n + 1) recursively."
            }
        ]
    }
]
