#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 8: Fractions in Disguise
Slides Data Generator - Part 1 (Slides 1 to 8)
Strictly matches NCERT Class 8 Maths Ch 8 syllabus with 1-3 word headings,
195-215 spoken words per slide, zero fictional characters/personas.
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Per Cent Meaning",
        "subtitle": "Section 1.1 Fractions as Percentages: Latin Etymology 'Per Centum' & Denominator 100 (z% = z/100)",
        "speech": (
            "Welcome to Class Eight Mathematics Chapter Eight: Fractions in Disguise! Look closely at the title—every percentage is truly an ordinary fraction wearing a smart hundred-grid costume! Start in Section One Point One with the phrase 'per cent'. It comes directly from the Latin expression 'per centum', meaning 'out of every hundred'! Whenever we write z percent using the percent symbol %, it simply means the exact fraction z divided by 100! "
            "Picture a crisp 10 by 10 square grid divided into 100 tiny equal unit squares. If you shade 35 squares out of 100, you shaded 35/100 of the whole square—or directly 35%! Shade exactly half the grid (50 squares out of 100), and you hold 50/100 = 50%! Even shading a single tiny square out of 100 represents 1/100, or 1%! "
            "Why call percentages 'fractions in disguise'? Because fractions with denominators like 4, 5, 20, or 25 wear completely different clothes until we dress them all over a matching denominator of 100! Once every fraction wears denominator 100, comparing different quantities becomes instant and visual! Remember that 100% represents one full complete whole—100 parts out of 100 equals 1—while smaller percentages represent clean portions out of 100 equal pieces!"
        ),
        "checkpoints": [
            {
                "question": "From which Latin phrase does the mathematical term 'per cent' originate, and what does z% literally equal?",
                "options": [
                    "'per centum' ('out of hundred'); z% = z / 100",
                    "'per decem' ('out of ten'); z% = z / 10",
                    "'per mille' ('out of thousand'); z% = z / 1000",
                    "'per unitas' ('out of one'); z% = z × 100"
                ],
                "answer": 0,
                "hint": "Recall the century connection—'centum' means one hundred!",
                "explanation": "Latin 'per centum' translates to 'out of hundred', so any z% equals the fraction z/100."
            },
            {
                "question": "On a 10 × 10 square grid (100 equal small squares), 42 squares are shaded blue. How is this shaded region expressed as both a fraction and a percentage?",
                "options": [
                    "42/100 and 42%",
                    "42/10 and 4.2%",
                    "58/100 and 42%",
                    "100/42 and 42%"
                ],
                "answer": 0,
                "hint": "Count shaded parts over total 100 squares directly!",
                "explanation": "42 shaded squares out of 100 equal squares equal the fraction 42/100, which is 42%."
            }
        ]
    },
    {
        "id": 2,
        "title": "Converting To Percent",
        "subtitle": "Section 1.1 Converting Fractions to Percentages (Scaling & ×100 Methods) & Why Base-10 Favors 100",
        "speech": (
            "Now learn the two reliable mathematical paths for unmasking any ordinary fraction into a clear percentage! Path One scales the denominator directly to 100 using equivalent fractions! Take 3/4: which whole factor multiplies 4 to reach 100? Twenty-five! Multiply both numerator 3 and denominator 4 cleanly by 25 to obtain 75/100, which instantly reveals 75%! Similarly, 7/20 multiplies numerator and denominator by 5 to yield 35/100 = 35%! "
            "Wait—what happens for fractions whose denominators do not divide 100 evenly, such as 3/8 or 2/3? Path Two solves EVERY fraction effortlessly: multiply the entire fraction directly by 100 and attach the % sign! Compute 3/8 × 100 = 300/8 = 37.5%! And compute 2/3 × 100 = 200/3 = 66.67%! "
            "Pause and ask a deep number-sense question: WHY did humanity choose 100 instead of 60, 12, or 80 as our universal standard? Because modern arithmetic counts in BASE TEN! Since 100 equals 10 squared, any percentage converts smoothly into a decimal simply by jumping two decimal places left: 45% = 0.45, and 7.5% = 0.075! Base-10 alignment gives fine one-percent precision while making rapid mental calculations, retail pricing, and global comparisons remarkably fast and intuitive for students!"
        ),
        "checkpoints": [
            {
                "question": "Which calculation correctly converts the fraction 3/8 into a percentage?",
                "options": [
                    "(3/8) × 100% = 300/8% = 37.5%",
                    "(3/8) ÷ 100 = 0.00375%",
                    "(8/3) × 100% = 266.67%",
                    "Add 92 to numerator and denominator = 95/100 = 95%"
                ],
                "answer": 0,
                "hint": "Multiply the fraction by 100 to reveal how many parts out of 100 it represents!",
                "explanation": "Multiplying 3/8 by 100 gives 300/8 = 37.5%, showing 3/8 equals 37.5 out of 100."
            },
            {
                "question": "Why did mathematics standardize on 100 ('per cent') rather than 12 or 60 for universal proportion comparisons?",
                "options": [
                    "Our decimal system is base-10, and 100 = 10² allows effortless mental decimal shifts and 1/100 precision",
                    "Because 100 is the largest number usable in commerce",
                    "Because 100 is divisible by every prime number like 3 and 7",
                    "Because decimals cannot work with powers of 10"
                ],
                "answer": 0,
                "hint": "Think how easily 42% turns into 0.42 just by shifting the decimal point!",
                "explanation": "In a base-10 number system, 100 = 10² pairs one-to-one with two decimal places, making mental math fast."
            }
        ]
    },
    {
        "id": 3,
        "title": "History Around Us",
        "subtitle": "Section 1.1 Historical Roots (Kautilya's Arthashastra, Rome, Italy), World Stats & Track Positions",
        "speech": (
            "Did percentages appear only in modern financial calculators? Not at all—their fascinating historical roots stretch back well over two thousand years! In India during the fourth century BCE, Kautilya's celebrated economic treatise, the Arthashastra, explicitly recorded monthly interest rules expressed per hundred! Centuries later, ancient Roman taxation introduced a one-per-hundred transaction levy on public auctions, known as centesima rerum venalium! By the fifteenth century, Italian commercial accounting manuscripts shortened 'per cento' into a slanted shorthand loop that gradually evolved into today's familiar % symbol! "
            "Look around our planet and human biology right now to spot meaningful real-world percentages everywhere! Roughly 60% of an adult human body's weight consists of water! Look far skyward—our Sun alone holds over 99.8% of the entire mass of our Solar System, leaving less than 0.2% combined for all eight planets, moons, and asteroids! Back on Earth, soil scientists warn that global soil degradation now affects roughly one-third of all productive agricultural farmland worldwide! "
            "Finally, visualize fractions directly along a 0% to 100% running track! Halfway stands cleanly at 1/2 = 50%! Three-quarters stands cleanly at 75%, beating 7/10 = 70% effortlessly once both runners wear clear matching percentage distance tags!"
        ),
        "checkpoints": [
            {
                "question": "Which ancient Indian work from the 4th century BCE recorded monthly interest rates expressed 'per hundred'?",
                "options": [
                    "Kautilya's Arthashastra",
                    "Euclid's Elements",
                    "Fibonacci's Liber Abaci",
                    "Magna Carta"
                ],
                "answer": 0,
                "hint": "This ancient treatise on statecraft and economics stems from 4th-century BCE India!",
                "explanation": "Kautilya's Arthashastra (4th century BCE) specified monthly credit interest rules measured per hundred."
            },
            {
                "question": "Along a 0% to 100% running track, Runner P reaches 7/10 of the lap while Runner Q reaches 3/4 of the lap. Who is ahead and by what percentage points?",
                "options": [
                    "Runner Q (75%) leads Runner P (70%) by 5 percentage points",
                    "Runner P (70%) leads Runner Q (75%)",
                    "Runner Q (72%) leads Runner P (70%) by 2 points",
                    "Both runners stand at identical track positions"
                ],
                "answer": 0,
                "hint": "Convert both 7/10 and 3/4 into denominator-100 percentages first!",
                "explanation": "7/10 = 70/100 = 70% while 3/4 = 75/100 = 75%, placing 3/4 five percentage points ahead."
            }
        ]
    },
    {
        "id": 4,
        "title": "Same Whole Base",
        "subtitle": "Section 1.2 Contextual Whole: Why Comparing Percentages Demands Knowing the Reference Base",
        "speech": (
            "Enter Section One Point Two with one foundational principle every mathematical thinker must guard carefully: a percentage NEVER floats in meaningless isolation—it ALWAYS belongs to a CONTEXTUAL WHOLE! Can we blindly conclude that 50% automatically beats 20%? Careful! Never compare raw percentages without carefully checking what exact base whole each percentage refers to! "
            "Test this classic trap with two fruit crates right now! Suppose Crate A holds 10 oranges total, and 50% of Crate A is ripe—computing 50% of 10 yields only 5 ripe oranges! Meanwhile, Crate B holds 100 oranges total, and ONLY 20% of Crate B is ripe—computing 20% of 100 yields 20 ripe oranges! Look closely: 20% of the larger hundred-orange crate delivers FOUR TIMES as many ripe oranges as 50% of the small ten-orange crate! "
            "This identical contextual trap appears constantly in school attendance reports, city budgets, and nutrition labels! Claiming 'Village School attendance jumped 10%' means 5 students at a tiny 50-student school, versus 200 students at a large 2,000-student urban campus! Direct raw percentage comparisons carry exact mathematical meaning ONLY when both percentages share the exact SAME reference whole, or right after converting each share cleanly back into actual physical quantities!"
        ),
        "checkpoints": [
            {
                "question": "Shop A discounts 40% on a ₹500 jacket, while Shop B discounts 25% on a ₹1,200 jacket. Which shop offers a larger rupee discount?",
                "options": [
                    "Shop B saves ₹300, beating Shop A's ₹200 saving because Shop B's base whole is larger!",
                    "Shop A saves ₹300, beating Shop B's ₹200",
                    "Shop A always saves more because 40% > 25%",
                    "Both discounts equal ₹250"
                ],
                "answer": 0,
                "hint": "Compute 40% of ₹500 and 25% of ₹1,200 separately before comparing!",
                "explanation": "40% of ₹500 = ₹200, while 25% of ₹1,200 = ₹300. Comparing percentages without bases misleads."
            },
            {
                "question": "When is directly comparing two percentage figures (e.g., 68% vs 74%) completely meaningful without knowing raw totals?",
                "options": [
                    "When both percentages describe shares of the SAME reference whole or equal-sized standardized base",
                    "Whenever one percentage exceeds 50%",
                    "Only when denominators are prime numbers",
                    "Always, regardless of total size"
                ],
                "answer": 0,
                "hint": "Think about test percentages vs percentages of completely different total weights!",
                "explanation": "Comparing raw % values directly is valid only when they refer to the same base quantity or standardized scale."
            }
        ]
    },
    {
        "id": 5,
        "title": "Bar Unit Methods",
        "subtitle": "Section 1.2 Computing Percentage of a Quantity: Visual Bar Models, Proportions (a/100 = s/total) & Unit Scaling",
        "speech": (
            "Now master the three rock-solid strategies in Section One Point Two for computing any percentage of a concrete quantity! Suppose a school library stocks 400 books, and we want exactly 35% of those 400 books! "
            "Method One draws a VISUAL BAR MODEL! Sketch one complete 100% bar representing all 400 books, then partition it neatly into ten equal 10% blocks! Each 10% block immediately equals 400 ÷ 10 = 40 books! Cutting one block in half forms 5% = 20 books! Combine three full 10% blocks plus one 5% half-block: 40 + 40 + 40 + 20 = 140 books! Visual bars build reliable intuition! "
            "Method Two writes a clean PROPORTIONAL RELATIONSHIP equating percentage ratio to actual share over total: a/100 = s/total! Plug in numbers directly: 35/100 = s/400! Cross-multiply cleanly or scale ×4 to find s = 35 × 4 = 140 books! "
            "Method Three applies UNIT-RATE SCALING! First compute the exact value of 1% by dividing the entire base whole by 100: 400 ÷ 100 = 4 books per 1%! Then multiply cleanly by the target percentage: 35 × 4 = 140 books! All three independent calculation methods smoothly confirm 140 books!"
        ),
        "checkpoints": [
            {
                "question": "Using the proportional setup a/100 = s/total, find 24% of 250 metres:",
                "options": [
                    "60 metres   (24/100 × 250 = 60)",
                    "6 metres",
                    "48 metres",
                    "120 metres"
                ],
                "answer": 0,
                "hint": "Find 1% of 250 first (2.5 m), then multiply by 24!",
                "explanation": "1% of 250 = 2.5 m; 24 × 2.5 = 60 m (or 24/100 × 250 = 60)."
            },
            {
                "question": "A 100% bar model representing ₹600 is split into 10 equal segments. What value do 3 segments plus half a segment represent?",
                "options": [
                    "35% of ₹600 = ₹210",
                    "30% of ₹600 = ₹180",
                    "3.5% of ₹600 = ₹21",
                    "45% of ₹600 = ₹270"
                ],
                "answer": 0,
                "hint": "Each 10% segment equals ₹600 ÷ 10 = ₹60, and half a segment (5%) equals ₹30!",
                "explanation": "3 × ₹60 + ₹30 = ₹210, which equals 35% of ₹600."
            }
        ]
    },
    {
        "id": 6,
        "title": "Mental Math Benchmarks",
        "subtitle": "Section 1.2 Free-Hand Mental Computation: Benchmark Decomposition (50%, 25%, 10%, 5%, 1%)",
        "speech": (
            "Leave slow long multiplication behind on everyday mental estimates! Section One Point Two sharpens FREE-HAND MENTAL COMPUTATIONS by slicing unfamiliar percentages into crystal-clear BENCHMARK BUILDING BLOCKS! Lock five anchor keys permanently into memory: 50% equals exactly half (divide by 2); 25% equals one-quarter (divide by 4); 10% simply divides by 10; 5% equals half of 10%; and 1% shifts the decimal point two places left (divide by 100)! "
            "Watch mental decomposition solve shop discounts effortlessly! Need 25% of ₹360? Spot 25% = 1/4 immediately: divide 360 by 4 cleanly to land on ₹90! Prefer building upward from tens? Take 10% of 360 = 36, double it to obtain 20% = 2 × 36 = 72, take half of 36 for 5% = 18, and sum 72 + 18 = ₹90! Notice how the syllabus teaches 20% = 2 × 10% and 25% = 20% + 5%! "
            "Test another practical example right away: compute 15% of ₹480 mentally without touching paper! Instantly find 10% = 48, halve it cleanly for 5% = 24, and add 48 + 24 = ₹72! Or calculate 99% of ₹500 quickly via clean subtraction: 100% minus 1% gives 500 − 5 = ₹495 effortlessly!"
        ),
        "checkpoints": [
            {
                "question": "Which mental benchmark decomposition computes 35% of ₹400 fastest without paper?",
                "options": [
                    "25% (400 ÷ 4 = 100) + 10% (400 ÷ 10 = 40) = ₹140",
                    "35 × 400 = ₹14,000",
                    "50% (200) − 25% (100) = ₹100",
                    "10% (40) + 5% (20) = ₹60"
                ],
                "answer": 0,
                "hint": "Notice 35% splits cleanly into 25% + 10% (or 3 × 10% + 5%)!",
                "explanation": "25% of 400 is 100 and 10% of 400 is 40, adding directly to ₹140."
            },
            {
                "question": "Find 15% of 640 mentally by combining 10% and 5%:",
                "options": [
                    "96   (10% = 64, plus half = 32)",
                    "80",
                    "104",
                    "64"
                ],
                "answer": 0,
                "hint": "First take 10% of 640 (= 64), then halve that number for 5%!",
                "explanation": "10% of 640 is 64; 5% is half of 64 = 32; 64 + 32 = 96."
            }
        ]
    },
    {
        "id": 7,
        "title": "FDP Trio Game",
        "subtitle": "Section 1.2 The FDP Trio (Fractions-Decimals-Percentages), Estimation & Percentages Greater Than 100%",
        "speech": (
            "Meet the tightly connected mathematical family called THE FDP TRIO: Fractions, Decimals, and Percentages! Never view them as three isolated school topics—they are three fluent languages describing the exact same relative proportion! Take 3/5: written as a decimal, 0.6; written as a percentage, 60%! Play the syllabus estimation challenge 'How Close Can You Get?' before touching pen to paper: to estimate 48% of 252, round immediately to 50% of 250 = 125! When exact arithmetic yields 120.96, smart estimation confirms instantly that our decimal point sits safely in the proper column! "
            "Now shatter a classic student misconception: can a real-world percentage EVER exceed 100%? ABSOLUTELY YES—whenever an observed quantity climbs BEYOND its baseline 100% reference target! Suppose a workshop sets a daily sales target of 40 bicycles (that baseline target represents 100%). If production surges and sells 60 bicycles today, compute (60/40) × 100 = 150%! That represents one full 100% target PLUS another half! Selling 80 bicycles achieves 200%—exact double! "
            "Remember this simple mathematical rule forever: percentage values strictly below 100% represent partial fractional sub-parts, 100% represents one complete intact whole, and percentages GREATER than 100% cleanly measure multiples exceeding the original baseline reference quantity!"
        ),
        "checkpoints": [
            {
                "question": "Express the improper fraction 7/4 in the other two members of the FDP Trio (Decimal and Percentage):",
                "options": [
                    "Decimal 1.75 and Percentage 175%",
                    "Decimal 0.74 and Percentage 74%",
                    "Decimal 1.40 and Percentage 140%",
                    "Decimal 7.40 and Percentage 740%"
                ],
                "answer": 0,
                "hint": "7/4 = 1 whole + 3/4! Multiply 7/4 by 100%!",
                "explanation": "7 ÷ 4 = 1.75, and 1.75 × 100% = 175%, which correctly exceeds 100% because 7 > 4."
            },
            {
                "question": "A bookstore's daily sales target is 80 books. Today it sold 120 books. What percentage of the daily target did it achieve?",
                "options": [
                    "150%   ((120 / 80) × 100 = 150%)",
                    "66.7%",
                    "120%",
                    "40%"
                ],
                "answer": 0,
                "hint": "Compare actual 120 books against the 80-book target whole: 120 ÷ 80!",
                "explanation": "120/80 = 3/2 = 1.5, which translates to 150% of the daily target."
            }
        ]
    },
    {
        "id": 8,
        "title": "Comparing Unequal Totals",
        "subtitle": "Section 1.3 Comparing Test Scores Across Unequal Totals & 'Know Your Contents' Food Percentages",
        "speech": (
            "Enter Section One Point Three: Using Percentages to make sharp, fair real-life comparisons! Imagine evaluating two classroom quizzes: Test One carried 25 maximum marks with 21 earned, whereas Test Two carried 40 maximum marks with 32 earned! Which test demonstrates stronger academic mastery? Judging purely by raw marks 32 versus 21 deceives us completely because their maximum totals differ! "
            "Percentages solve unequal-total comparisons effortlessly by converting every score onto ONE universal 100-mark scale! Convert Test One cleanly: (21/25) × 100 = 84%! Convert Test Two cleanly: (32/40) × 100 = 80%! Immediately transparent: 84% outperforms 80%, even though raw number 21 originally looked smaller than 32! "
            "Apply this exact standardization lens to packaged food labels in the NCERT 'Know Your Contents' activity! Suppose Biscuit Pack A weighs 120 grams total and lists 30 grams of sugar, while Biscuit Pack B weighs 200 grams total and lists 44 grams of sugar! Which biscuit recipe actually carries higher sugar concentration per single gram? Compute exact percentages! Pack A: (30/120) × 100 = 25% sugar! Pack B: (44/200) × 100 = 22% sugar! Although Pack B holds heavier total grams of sugar overall, Pack A clearly concentrates MORE sugar percentage-wise!"
        ),
        "checkpoints": [
            {
                "question": "Compare two exam scores: Score X = 18 out of 24; Score Y = 36 out of 50. Which score reflects a higher percentage?",
                "options": [
                    "Score X (75%) beats Score Y (72%)",
                    "Score Y (75%) beats Score X (72%)",
                    "Score Y beats Score X because 36 > 18",
                    "Both represent equal percentages"
                ],
                "answer": 0,
                "hint": "Simplify 18/24 = 3/4 first, then convert 36/50 to /100!",
                "explanation": "18/24 = 3/4 = 75%, whereas 36/50 = 72/100 = 72%."
            },
            {
                "question": "Juice Carton A (250 mL) contains 40 mL pure fruit pulp; Carton B (400 mL) contains 60 mL fruit pulp. Which carton has a higher concentration percentage of pulp?",
                "options": [
                    "Carton A (16% pulp) is more concentrated than Carton B (15% pulp)",
                    "Carton B (20% pulp) is more concentrated than Carton A (16% pulp)",
                    "Carton B is always more concentrated because 60 mL > 40 mL",
                    "Both contain 15% pulp"
                ],
                "answer": 0,
                "hint": "Divide pulp by total carton volume and multiply by 100% for each carton!",
                "explanation": "Carton A: (40/250) × 100 = 16%; Carton B: (60/400) × 100 = 15%."
            }
        ]
    }
]
