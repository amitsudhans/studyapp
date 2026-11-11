#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 3: A Story of Numbers
Slides Data Generator - Part 2 (Slides 9 to 16)
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Idea Of Base",
        "subtitle": "Section 3.3 (II): Base-n Landmark Powers (1, n, n², n³...) & Custom Base-5 / Base-4 Systems",
        "speech": (
            "Now unlock Section Three Point Three's grand unifying insight: THE IDEA OF A BASE! Why was the Egyptian scheme mathematically cleaner than Roman I, V, X, L, C, D, M? Because EVERY Egyptian landmark belongs strictly to successive powers of ONE fixed anchor number TEN! "
            "Generalize cleanly into mathematics! In ANY BASE-n NUMBER SYSTEM, landmark numbers ALWAYS start at n⁰ = ONE and scale uniformly upward by multiplying by base n cleanly: n⁰ = 1, n¹ = n, n², n³, n⁴, and so onward forever! Notice every time n identical landmark tokens collect inside any group, they trade neatly upward for ONE token of the very next higher landmark! "
            "Test constructing a custom BASE-5 LANDMARK SYSTEM right now! List its first five powers of five: 5⁰ = 1, 5¹ = 5, 5² = 25, 5³ = 125, and 5⁴ = 625! Represent everyday decimal 43 inside base-5 landmarks using greedy division: pick one 25 (leaving remainder 18), pick three 5s equaling 15 (leaving remainder 3), and three single 1s! Verify total sum cleanly: (1 × 25) + (3 × 5) + (3 × 1) = 43 = 133₅ cleanly! Try converting decimal 27 into Base-4 landmarks (1, 4, 16, 64) identically: 1×16 + 2×4 + 3×1 = 123₄!"
        ),
        "checkpoints": [
            {
                "question": "In a pure Base-5 landmark number system (5⁰, 5¹, 5², 5³, 5⁴...), what are the first five landmark values?",
                "options": [
                    "1, 5, 25, 125, 625",
                    "1, 5, 10, 50, 100",
                    "5, 10, 15, 20, 25",
                    "1, 4, 16, 64, 256"
                ],
                "answer": 0,
                "hint": "Compute consecutive powers starting at 5⁰ = 1 and multiplying by 5 at each step!",
                "explanation": "Base-5 landmarks are powers of 5: 5⁰=1, 5¹=5, 5²=25, 5³=125, 5⁴=625."
            },
            {
                "question": "How is decimal 43 written using greedy grouping in Base-5 landmarks (25s, 5s, 1s)?",
                "options": [
                    "One 25, three 5s, and three 1s  (133₅ = 25 + 15 + 3)",
                    "Two 25s and three 1s  (203₅)",
                    "Four 10s and three 1s",
                    "Eight 5s and three 1s  (83₅)"
                ],
                "answer": 0,
                "hint": "Remember each digit in Base-5 must stay strictly under 5 (0, 1, 2, 3, or 4)!",
                "explanation": "43 = 1×25 + 3×5 + 3×1 → base-5 representation 133₅."
            }
        ]
    },
    {
        "id": 10,
        "title": "Base System Advantages",
        "subtitle": "Section 3.3: Why Exponent Laws Simplify Arithmetic & The 11th-Century Decimal Abacus",
        "speech": (
            "Discover WHY every base-n power landmark transforms sluggish arithmetic into effortless lightning speed inside Section Three Point Three! Suppose you attempt multiplying Roman XL (40) directly by L (50): awkward letter combinations immediately block column alignment and force tedious mental conversion! Contrast this hurdle cleanly against ANY UNIFORM POWER-BASED NUMBER SYSTEM! "
            "Whenever two landmark powers multiply together, Chapter Two's EXPONENT PRODUCT LAW guarantees you ALWAYS land cleanly back inside ANOTHER EXACT LANDMARK POWER: nᵃ × nᵇ = n^(a+b)! For example inside base five, multiplying landmark 5¹ (5) by landmark 5² (25) instantaneously yields exact landmark 5³ (125)! Combined cleanly with the DISTRIBUTIVE PROPERTY of multiplication over addition, ANY giant multi-digit product breaks directly into tiny single-digit multiplications plus neat carries upward to the very next landmark column! "
            "Look how eleventh-century medieval European merchants bridged ancient Roman tallies into true decimal arithmetic using the DECIMAL ABACUS! Rather than consuming expensive parchment sheets and ink, wooden counting boards ruled neat parallel vertical lines representing consecutive powers of ten (1, 10, 100, 1,000, ...)! Placing numbered stone counters smoothly along those lines turned carrying ten-for-one completely effortless—visually practicing true place-value grouping centuries before printed Hindu ink numerals conquered all of Europe!"
        ),
        "checkpoints": [
            {
                "question": "Why does using pure powers of a base n (n⁰, n¹, n², n³...) vastly simplify multiplication compared to mixed landmarks like Roman 1, 5, 10, 50, 100?",
                "options": [
                    "Because multiplying any two base landmarks nᵃ × nᵇ ALWAYS produces another landmark n^(a+b), pairing cleanly with the distributive law!",
                    "Because base-n forbids numbers greater than 100",
                    "Because 5 × 10 equals 100 in base-10",
                    "Because abacus boards have no zero"
                ],
                "answer": 0,
                "hint": "Think of why 10² × 10³ immediately lands on landmark 10⁵ without inventing odd irregular factors!",
                "explanation": "Uniform powers satisfy nᵃ × nᵇ = n^(a+b), keeping every partial product cleanly aligned on exact base landmarks."
            },
            {
                "question": "In an 11th-century decimal abacus counting board, what do parallel counting lines represent?",
                "options": [
                    "Successive powers of 10 (1, 10, 100, 1,000, ...) where 10 tokens on any line carry upward to 1 token on the next line",
                    "Mayan calendar weeks",
                    "Stone Age sheep footprints only",
                    "Random primes"
                ],
                "answer": 0,
                "hint": "Each parallel column/line moves upward cleanly by ×10!",
                "explanation": "Parallel lines represent consecutive powers of 10 (10⁰, 10¹, 10², ...), making addition, subtraction, and carries mechanical."
            }
        ]
    },
    {
        "id": 11,
        "title": "Egyptian System Limits",
        "subtitle": "Section 3.3 (III): Symbol Repetition Bloat & Why Non-Positional Base Systems Fail Large Numbers",
        "speech": (
            "Wait—if ancient Egyptian powers of ten worked so logically for building early granary and temple records, WHY aren't modern engineers still sketching lotus flowers and tiny tadpoles inside school math notebooks today? Examine Section Three Point Three Part Three closely: Shortcomings of the Egyptian Additive Number System! "
            "Spot TWO fatal historical design flaws cleanly! First, SYMBOL REPETITION BLOAT: without fixed positional columns or digit multipliers, writing digit nine inside ANY landmark demands carving NINE IDENTICAL GLYPHS side by side! Test writing simple 999 in ancient Egyptian: scribes had to painstakingly chisel NINE coiled ropes, NINE heel bones, and NINE vertical staffs—TWENTY SEVEN SEPARATE PICTURE DRAWINGS just for three ordinary digits! Even writing 9,99,999 requires carving FIFTY FOUR tiring repeated symbols across stone! "
            "Second—discover the FATAL MATHEMATICAL WALL: a purely additive non-positional base system COMPLETELY FAILS FOR ARBITRARILY LARGE COSMIC NUMBERS! Why? Reaching ten million, one hundred million, or astronomical trillions forces scribes to keep inventing an INFINITE NEW SEQUENCE of brand-new picture pictograms forever once astonished men quickly run out! Only ONE true mathematical breakthrough solves cosmic astronomical infinity forever using a finite compact set of just ten tiny printed digits: POSITIONAL PLACE VALUE NOTATION!"
        ),
        "checkpoints": [
            {
                "question": "How many total Egyptian hieroglyphs are needed just to write the ordinary 3-digit number 999?",
                "options": [
                    "27 hieroglyphs  (9 coiled ropes + 9 heel bones + 9 vertical staffs)",
                    "3 hieroglyphs",
                    "10 hieroglyphs",
                    "999 hieroglyphs"
                ],
                "answer": 0,
                "hint": "Add 9 copies of 100 + 9 copies of 10 + 9 copies of 1!",
                "explanation": "Non-positional additive systems repeat each glyph up to 9 times per place: 9 + 9 + 9 = 27 symbols for 999."
            },
            {
                "question": "What is the fundamental mathematical flaw preventing Egyptian hieroglyphic numerals from representing arbitrarily huge cosmic numbers cleanly?",
                "options": [
                    "Every new higher power of 10 forces inventing a brand-new symbol forever, requiring an infinite alphabet of pictograms",
                    "Egyptians did not know the value 10",
                    "Coiled ropes always mean negative fractions",
                    "Egyptian systems used base 2"
                ],
                "answer": 0,
                "hint": "After 10⁶ (astonished man), how would you write 10²³ or 10¹⁰⁰ without place value?",
                "explanation": "Without positional columns, representing arbitrary powers requires endlessly inventing new symbols forever."
            }
        ]
    },
    {
        "id": 12,
        "title": "Mesopotamian Base Sixty",
        "subtitle": "Section 3.4 (I): Earliest Place Value in Sexagesimal Base 60 (Y=1, <=10) & Blank-Space Ambiguity",
        "speech": (
            "Enter Section Three Point Four: Place Value Representation—truly humankind's crowning arithmetic breakthrough! Inside a POSITIONAL PLACE VALUE SYSTEM, a symbol's true numeric contribution depends simultaneously BOTH on WHICH digit symbol appears AND WHICH POSITION (column) it occupies! Moving one column leftward cleanly multiplies weight by exact base n every time! "
            "Look back four thousand years to ancient MESOPOTAMIA (Babylon) for history's earliest true positional system: SEXAGESIMAL BASE SIXTY! Using sharp reed styluses pressed into wet clay tablets, scribes combined JUST TWO tiny wedge shapes—upright vertical wedge Y = ONE and corner wedge < = TEN—to build every sub-value from one up to fifty nine cleanly inside each column! Then columns stepped upward by powers of sixty: 60⁰ (ones), 60¹ (sixties), 60² (3,600s), and upward forever! "
            "Why did ancient Babylonians pick sixty as their base? Because sixty divides evenly by twelve integers—1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, and 60—still ticking cleanly inside our 60 seconds per minute, 60 minutes per hour, and 360-degree circles worldwide today! Yet early Babylon left EMPTY BLANK SPACES for missing intermediate powers—causing severe confusion between 62 and 3,602 until slanted double-wedge marks later arrived as internal placeholders!"
        ),
        "checkpoints": [
            {
                "question": "In the Mesopotamian Base-60 cuneiform system (Y = 1, < = 10), what decimal number is represented by two columns: [ << YYY ] in the 60¹ place and [ < YY ] in the 60⁰ place?",
                "options": [
                    "1,392   (= 23 × 60 + 12 × 1)",
                    "35   (= 23 + 12)",
                    "743",
                    "2,312"
                ],
                "answer": 0,
                "hint": "Decode each column (<< YYY = 23, < YY = 12), then multiply left column by 60¹ = 60!",
                "explanation": "23 × 60 + 12 × 1 = 1,380 + 12 = 1,392."
            },
            {
                "question": "What major flaw plagued EARLY Mesopotamian clay tablets before a slanted placeholder wedge was introduced?",
                "options": [
                    "Leaving an empty blank space for a zero column made numbers like (1×60 + 5) look nearly identical to (1×60² + 0×60 + 5)!",
                    "Base 60 cannot write numbers larger than 59",
                    "Clay tablets used lotus flowers for 1,000",
                    "Wedge marks meant negative division"
                ],
                "answer": 0,
                "hint": "Without a visible zero symbol inside empty columns, spacing widths became ambiguous!",
                "explanation": "Blank spaces caused positional ambiguity (and never appeared cleanly at trailing ends) until a placeholder mark emerged."
            }
        ]
    },
    {
        "id": 13,
        "title": "Mayan Vertical Scale",
        "subtitle": "Section 3.4 (II): Mayan Dots (1), Bars (5), Seashell Zero (0) & Calendar Scale (1, 20, 360, 7200...)",
        "speech": (
            "Fly cleanly across the vast Atlantic Ocean to ancient Central America (c. third to tenth century Common Era) inside Section Three Point Four Part Two: THE MAYAN PLACE VALUE NUMBER SYSTEM! Completely independently from Asia and Europe, brilliant Mayan astronomer-priests invented a vertical positional system featuring an unmistakable graphic ZERO glyph! "
            "Watch how cleanly three simple carved Mayan elements stack vertically from BOTTOM TO TOP! Inside any horizontal level, one crisp DOT equals ONE, and one sturdy horizontal BAR equals FIVE—letting astronomer-scribes build every quantity zero through nineteen effortlessly (for example, two horizontal bars plus three dots equals thirteen)! Above nineteen sits an iconic carved SEASHELL SYMBOL standing explicitly for ZERO as a crystal-clear empty-level placeholder! "
            "Check Mayan vertical place multipliers carefully—and spot one fascinating ancient astronomical calendar quirk! Rather than pure uninterrupted powers of twenty (1, 20, 400, 8,000), the classical Mayan civil calendar scale deliberately modified its third vertical tier upward to 18 × 20 = THREE HUNDRED SIXTY (matching Earth's approximate 360-day yearly solar cycle closely!), before continuing cleanly upward by exact factors of twenty again: bottom = 1, second = 20, third = 360, fourth = 7,200, and fifth = 1,44,000 cleanly!"
        ),
        "checkpoints": [
            {
                "question": "In Mayan vertical notation (dot = 1, bar = 5, seashell = 0; multipliers bottom-up: 1, 20, 360), decode: top [ 2 dots ], middle [ seashell (0) ], bottom [ 1 bar + 3 dots ]:",
                "options": [
                    "728   (= 2 × 360 + 0 × 20 + 8 × 1)",
                    "808   (= 2 × 400 + 8)",
                    "48   (= 2 × 20 + 8)",
                    "10"
                ],
                "answer": 0,
                "hint": "Multiply top level by 360, middle seashell by 20 (= 0), and bottom (5+3=8) by 1!",
                "explanation": "2 × 360 + 0 × 20 + 8 × 1 = 720 + 0 + 8 = 728."
            },
            {
                "question": "Which symbol did the ancient Mayan civilization carve inside vertical columns to prevent blank-space positional confusion?",
                "options": [
                    "A carved seashell symbol representing zero (0)",
                    "An astonished human figure",
                    "An alternating vertical rod",
                    "A slanted Mesopotamian corner wedge"
                ],
                "answer": 0,
                "hint": "Think of the marine shell icon placed cleanly on empty rows!",
                "explanation": "Mayan inscriptions used a distinctive seashell glyph cleanly as a visible positional zero."
            }
        ]
    },
    {
        "id": 14,
        "title": "Chinese Rod Numerals",
        "subtitle": "Section 3.4 (III): Base-10 Alternating Vertical (Zong) & Horizontal (Heng) Rod Positions",
        "speech": (
            "Travel eastward next to ancient China (developed cleanly by the third century Common Era) inside Section Three Point Four Part Three: THE CHINESE ROD NUMERAL SYSTEM! Long before printed paper textbooks existed, skilled Chinese mathematicians arranged thin carved bamboo, bone, or ivory counting rods across checkered wooden calculating boards—operating strictly cleanly inside BASE TEN! "
            "Digits one through five laid down matching numbers of straight parallel rods cleanly, while digits six through nine placed ONE perpendicular five-bar resting across one to four unit rods! Yet notice an ingenious design problem: if both tens digit 2 and ones digit 1 used identical upright vertical sticks right side by side, 21 could easily blur carelessly into single digit 3! "
            "Ancient Chinese mathematicians solved adjacent-column blurring brilliantly WITHOUT inventing confusing extra glyphs: they STRICTLY ALTERNATED ROD ORIENTATIONS across all adjacent counting board squares! Units (10⁰), hundreds (10²), and ten-thousands (10⁴) stood strictly upright in VERTICAL ZONG orientation; whereas tens (10¹), thousands (10³), and hundred-thousands (10⁵) lay neatly sideways in HORIZONTAL HENG orientation, always leaving zero squares empty blank! Additionally, crisp red rods tracked positive asset sums while dark black rods represented negative subtractive debts—creating brilliant century-ahead algebraic calculation grid boards!"
        ),
        "checkpoints": [
            {
                "question": "Why did the ancient Chinese Base-10 rod system strictly alternate vertical (Zong) and horizontal (Heng) orientations across adjacent place columns?",
                "options": [
                    "To prevent sticks from adjacent digits blurring into one combined digit (e.g. separating tens and ones visually!)",
                    "Because horizontal sticks meant base 60",
                    "Only for decorative border frames",
                    "To replace division completely"
                ],
                "answer": 0,
                "hint": "Imagine putting two vertical rods (2) right next to three vertical rods (3) without any spacing box!",
                "explanation": "Alternating vertical (Zong) for 10⁰, 10², ... and horizontal (Heng) for 10¹, 10³, ... separated neighboring place values cleanly."
            },
            {
                "question": "In Chinese rod numerals, which orientation (Zong vertical or Heng horizontal) represents the TENS (10¹) and THOUSANDS (10³) places?",
                "options": [
                    "Horizontal (Heng), alternating cleanly with Vertical (Zong) for units (10⁰) and hundreds (10²)",
                    "Both always stay Vertical (Zong)",
                    "Only seashell icons",
                    "Circular dots"
                ],
                "answer": 0,
                "hint": "Even powers of 10 (10⁰, 10²) use Zong vertical; odd powers (10¹, 10³) use Heng horizontal!",
                "explanation": "Units (10⁰) and hundreds (10²) use Zong (vertical), while tens (10¹) and thousands (10³) alternate to Heng (horizontal)."
            }
        ]
    },
    {
        "id": 15,
        "title": "Hindu Decimal Zero",
        "subtitle": "Section 3.4 (IV): Ultimate 10-Digit Place Value System — Zero as Both Placeholder & Number (Brahmagupta 628 CE)",
        "speech": (
            "Now crown our entire global mathematical journey inside Section Three Point Four Part Four: THE HINDU NUMBER SYSTEM! Why did ancient India's compact ten-digit decimal place value system outlast Roman letters, Egyptian lotus glyphs, Mesopotamian sixties, Mayan calendar tiers, and bamboo rods to unite all modern world science and arithmetic today? "
            "Two monumental conceptual breakthroughs united right inside ancient India! First, ONE UNIFIED COMPACT ALPHABET of just ten crisp, unforgettable digits (0 through 9) writes EVERY NUMBER IN THE UNIVERSE—no matter how unimaginably gigantic or microscopically tiny—cleanly using strictly uniform Base Ten powers of ten (1, 10, 100, 1,000, ...), with ZERO need to alternate rod directions or invent new symbols forever! "
            "Second—the greatest single intellectual leap in human mathematical history: treating ZERO (0 / Sunya) BOTH as a rock-solid positional placeholder separating 502 cleanly from 52 AND AS AN ACTUAL COMPLETE ARITHMETIC NUMBER IN ITS OWN RIGHT! After ARYABHATA formalized systematic place-value arithmetic in 499 Common Era, BRAHMAGUPTA's landmark 628 CE Sanskrit treatise Brahmasphutasiddhanta systematically codified zero's explicit algebraic addition, subtraction, and zero-multiplication laws alongside negative integers—forever birthing modern algebra, decimal fractions, astrophysics, science, global banking commerce, and modern binary electronic digital computer hardware worldwide!"
        ),
        "checkpoints": [
            {
                "question": "What dual conceptual role elevated India's 0 (Sunya), formalized by Aryabhata (499 CE) and Brahmagupta (628 CE), above every earlier placeholder system?",
                "options": [
                    "Treating 0 BOTH as a positional placeholder digit (eliminating ambiguity in 502 vs 52) AND as a full arithmetic number obeying explicit laws!",
                    "Using 0 only at the start of years",
                    "Making 0 represent 60 in Mesopotamian wedges",
                    "Forbidding decimals permanently"
                ],
                "answer": 0,
                "hint": "Compare Babylon's blank space (placeholder only) against Brahmagupta's a + 0 = a, a − 0 = a, a × 0 = 0!",
                "explanation": "Indian mathematics treated 0 simultaneously as an unambiguous place-value digit AND a genuine number with algebraic rules."
            },
            {
                "question": "Who authored Brahmasphutasiddhanta in 628 CE, codifying formal arithmetic laws for zero and negative numbers?",
                "options": [
                    "Brahmagupta",
                    "Fibonacci",
                    "Hammurabi",
                    "Al-Kindi"
                ],
                "answer": 0,
                "hint": "Look carefully at the year 628 CE and book title Brahmasphutasiddhanta!",
                "explanation": "Brahmagupta (628 CE) systematically formulated operations with zero and negative numbers in Brahmasphutasiddhanta."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter Three Summary",
        "subtitle": "Base Conversions (Base 10 → Base 8, Base 5, Base 2), Finger Bases & Historical Number System Recap",
        "speech": (
            "Congratulations on completing NCERT Class Eight Chapter Three: A Story of Numbers! Before tackling forty Challenge Quiz questions, practice converting between bases cleanly! "
            "Remember the universal REPEATED DIVISION METHOD converting decimal numbers cleanly into ANY target base b (such as base-8 octal, base-5 quinary, or computer base-2 binary): divide repeatedly by base b, record each integer remainder strictly from RIGHT TO LEFT (units upward to highest power), and stop cleanly once your quotient reaches zero! Test converting decimal 29 into base-2 binary step by step: 29÷2 = 14 remainder 1; 14÷2 = 7 remainder 0; 7÷2 = 3 remainder 1; 3÷2 = 1 remainder 1; 1÷2 = 0 remainder 1 → reading upward gives 11101₂ (check: 16 + 8 + 4 + 0 + 1 = 29)! Convert 29 into base-5: 29÷5 = 5 remainder 4, 5÷5 = 1 remainder 0, 1÷5 = 0 remainder 1 → 104₅! Convert 29 into base-8: 29÷8 = 3 remainder 5 → 35₈! Notice also how counting three finger joints per four fingers yields natural base 12! "
            "From sticks and bones through Roman, Egyptian, Mesopotamian, Mayan, and Chinese landmarks to Indian decimal zero—humanity turned infinity into simple everyday arithmetic!"
        ),
        "checkpoints": [
            {
                "question": "Convert decimal number 29 cleanly into Base-2 (Binary), Base-5, and Base-8 (Octal):",
                "options": [
                    "11101₂   |   104₅   |   35₈",
                    "10111₂   |   140₅   |   53₈",
                    "11100₂   |   105₅   |   34₈",
                    "11011₂   |   114₅   |   36₈"
                ],
                "answer": 0,
                "hint": "Check expanded sums cleanly: 16+8+4+1 = 29; 1×25+0×5+4 = 29; 3×8+5 = 29!",
                "explanation": "29 = 11101₂ = 104₅ = 35₈."
            },
            {
                "question": "Why does modern computing rely heavily on Base-2 (Binary: bits 0 and 1), using the exact same place-value idea pioneered in Base-10?",
                "options": [
                    "Because electronic switches easily represent two clear states (OFF = 0, ON = 1) aligned cleanly along consecutive powers of 2 (1, 2, 4, 8, 16, ...)",
                    "Because computers use Roman numerals internally",
                    "Because base-2 needs 60 distinct wedge icons",
                    "Because binary omits zero completely"
                ],
                "answer": 0,
                "hint": "Match OFF/ON electrical states to digits 0/1 inside positional powers of 2!",
                "explanation": "Binary positional notation stores numbers with just {0, 1} (ON/OFF states) scaled by powers 2⁰, 2¹, 2², ..."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part2)} slides for Ch3 Class 8 Maths Part 2.")
    for s in slides_part2:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: {s['title']!r} ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Slide {s['id']} title length {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 2 assertions passed cleanly!")
