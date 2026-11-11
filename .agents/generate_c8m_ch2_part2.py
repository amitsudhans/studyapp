#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 2: Power Play
Data Generator - Part 2 (Slides 9 to 16)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each (spoken-friendly plain math phrasing)
- Checkpoints: Exactly 2 per slide with 4 options each
- Zero fictional human character names, zero lecturer personas
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Power Lines Scale",
        "subtitle": "Section 2.3 ('Power Lines'): Visualizing Positive & Negative Powers of 4 and 7 on Scale Lines",
        "speech": (
            "Meet NCERT's ultra-clever visual tool inside Section Two Point Three: POWER LINES! Instead of cramming 1, 7, 49, and 343 onto an ordinary uniform number line where giant jumps squash tiny fractions together, draw evenly spaced tick marks labeled ONLY with consecutive exponents of a single fixed base—like powers of 4 or powers of 7! "
            "Inspect a Base-7 Power Line from left to right: tick −2 holds 7⁻² (1/49), tick −1 holds 7⁻¹ (1/7), center tick 0 holds 7⁰ equals 1, tick +1 holds 7¹ = 7, tick +2 holds 7² = 49, tick +3 holds 7³ = 343! "
            "Watch what magical visual arithmetic unlocks instantaneously on this Power Line! Moving ONE tick step RIGHT ALWAYS multiplies your number cleanly by 7! Moving ONE tick step LEFT ALWAYS divides your number cleanly by 7! Want to multiply 7² × 7³? Start at tick +2 and walk 3 steps RIGHT to land straight onto tick +5 (= 7⁵)! Want to divide 4⁵ ÷ 4⁻²? Count separation jumps from tick −2 up to tick +5: 5 − (−2) = SEVEN jumps right → 4⁷! Similarly on a Base-4 Power Line, multiplying by 16 (which equals 4²) steps 2 ticks right!"
        ),
        "checkpoints": [
            {
                "question": "On a Base-4 Power Line (ticks labeled 4⁻², 4⁻¹, 4⁰, 4¹, 4², 4³, ...), what single movement represents multiplying by 16 and dividing by 64?",
                "options": [
                    "Multiplying by 16 moves 2 steps RIGHT (+2, since 16=4²); dividing by 64 moves 3 steps LEFT (−3, since 64=4³)",
                    "Moving 16 steps right and 64 steps left",
                    "Moving 4 steps right and 4 steps left",
                    "Staying fixed at 4⁰"
                ],
                "answer": 0,
                "hint": "Rewrite 16 = 4² and 64 = 4³ to read exact step counts!",
                "explanation": "Every tick right multiplies by 4 (so ×4² = +2 steps right); every tick left divides by 4 (so ÷4³ = −3 steps left)."
            },
            {
                "question": "Compare positions on a Power Line: How many times larger is 7³ than 7⁻¹?",
                "options": [
                    "7⁴ = 2,401 times larger   (4 steps apart: 3 − (−1) = 4!)",
                    "7² = 49 times larger",
                    "4 times larger",
                    "7⁻⁴ times larger"
                ],
                "answer": 0,
                "hint": "Compute ratio 7³ ÷ 7⁻¹ = 7^(3 − (−1))!",
                "explanation": "7³ ÷ 7⁻¹ = 7^(3+1) = 7⁴ = 2,401."
            }
        ]
    },
    {
        "id": 10,
        "title": "Decimal Place Powers",
        "subtitle": "Section 2.4: Expanding Whole & Decimal Numbers Using Positive, Zero & Negative Powers of 10",
        "speech": (
            "Step directly into Section Two Point Four: Powers of Ten! Our entire base-ten Hindu-Arabic decimal place-value system runs cleanly on positive, zero, and negative powers of ten! "
            "Examine NCERT's exact landmark example: 561.903! Split every single digit cleanly around the decimal point! Look left of the decimal point: units place 1 multiplies by 10⁰ (= 1); tens place 6 multiplies by 10¹ (= 10); and hundreds place 5 multiplies by 10² (= 100)! Now look right of the decimal point: tenths place 9 multiplies by 10⁻¹ (= 1/10 = 0.1); hundredths zero placeholder 0 multiplies by 10⁻² (= 0.01); and thousandths place 3 multiplies cleanly by 10⁻³ (= 0.001)! "
            "Assemble all six weighted terms into one unbroken unified expansion: 5×10² + 6×10¹ + 1×10⁰ + 9×10⁻¹ + 0×10⁻² + 3×10⁻³! Notice how cleanly the powers step downward in unbroken integer sequence +2, +1, 0, −1, −2, −3! Beware the classic units place trap carefully: units digit ALWAYS pairs with 10⁰ (= 1), NEVER 10¹! Practice reversing expansions like 4×10² + 7×10⁰ + 2×10⁻¹ + 9×10⁻³ cleanly back into exact decimal 407.209 by carefully filling every single missing empty place value position completely with digit zero!"
        ),
        "checkpoints": [
            {
                "question": "In the expanded exponential form of 561.903, which exact powers of 10 multiply the units digit (1) and the thousandths digit (3)?",
                "options": [
                    "1 × 10⁰   and   3 × 10⁻³",
                    "1 × 10¹   and   3 × 10⁻²",
                    "1 × 10⁰   and   3 × 10³",
                    "1 × 10⁻¹   and   3 × 10⁻³"
                ],
                "answer": 0,
                "hint": "Ones place = 10⁰ (1), tenths = 10⁻¹, hundredths = 10⁻², thousandths = 10⁻³!",
                "explanation": "561.903 = 5×10² + 6×10¹ + 1×10⁰ + 9×10⁻¹ + 0×10⁻² + 3×10⁻³."
            },
            {
                "question": "Which decimal number equals the exponential expansion 4×10² + 7×10⁰ + 2×10⁻¹ + 9×10⁻³?",
                "options": [
                    "407.209",
                    "47.29",
                    "407.29",
                    "470.029"
                ],
                "answer": 0,
                "hint": "Watch missing zero placeholders: 10¹ (tens) = 0, and 10⁻² (hundredths) = 0!",
                "explanation": "400 + 0(10) + 7 + 0.2 + 0(0.01) + 0.009 = 407.209."
            }
        ]
    },
    {
        "id": 11,
        "title": "Scientific Notation Form",
        "subtitle": "Section 2.4: Standard Form (x × 10ʸ, 1 ≤ x < 10) for Astronomical & Microscopic Scales",
        "speech": (
            "How do astronomers record the giant mass of Earth (5,970,000,000,000,000,000,000,000 kg) or biologists record the tiny width of a single microscopic virus (0.000000085 m) without ever losing count of twenty-four zeros? Welcome to SCIENTIFIC NOTATION (also called Standard Form)! "
            "Every number written in strict Scientific Notation looks like x × 10ʸ, obeying TWO golden rules: First, coefficient x MUST satisfy ONE ≤ x < TEN (meaning EXACTLY ONE non-zero digit sits left of the decimal point)! Second, exponent y MUST be an integer! "
            "Count decimal shifts carefully step by step! For HUGE astronomical numbers (≥ 10), move the decimal point LEFT giving POSITIVE exponent y: 5,970,000,000,000,000,000,000,000 shifts 24 places left to give 5.97 × 10²⁴ kilograms (mass of planet Earth)! For TINY microscopic numbers (< 1), move the decimal point RIGHT giving NEGATIVE exponent y: 0.000000085 shifts 8 places right to give 8.5 × 10⁻⁸ meters! Caution alert: 42 × 10⁵ is NOT standard scientific form (because 42 ≥ 10)—always normalize it cleanly into 4.2 × 10⁶! Always compare exponent y FIRST when ordering very large or very small scientific magnitudes from smallest to largest, then compare leading decimal digits x cleanly, carefully, systematically, and accurately!"
        ),
        "checkpoints": [
            {
                "question": "Which expression is properly written in STRICT Scientific Notation (x × 10ʸ with 1 ≤ x < 10)?",
                "options": [
                    "1.496 × 10¹¹   (Earth–Sun distance in meters)",
                    "14.96 × 10¹⁰",
                    "0.1496 × 10¹²",
                    "1496 × 10⁸"
                ],
                "answer": 0,
                "hint": "Check coefficient x: strictly 1 ≤ x < 10 (exact single non-zero digit left of decimal)!",
                "explanation": "1.496 sits cleanly in [1, 10), whereas 14.96 ≥ 10, 0.1496 < 1, and 1496 ≥ 10."
            },
            {
                "question": "Convert both tiny virus size 0.0000072 m AND improper expression 45 × 10⁸ into strict Scientific Notation:",
                "options": [
                    "7.2 × 10⁻⁶ m   and   4.5 × 10⁹",
                    "7.2 × 10⁶ m   and   4.5 × 10⁷",
                    "72 × 10⁻⁷ m   and   4.5 × 10⁹",
                    "0.72 × 10⁻⁵ m   and   4.5 × 10⁸"
                ],
                "answer": 0,
                "hint": "0.0000072 moves decimal 6 spots right (y = −6); 45 × 10⁸ = (4.5 × 10¹) × 10⁸ = 4.5 × 10⁹!",
                "explanation": "Rightward shifts give negative exponents (−6), while splitting 45 = 4.5 × 10 increments exponent 8 → 9."
            }
        ]
    },
    {
        "id": 12,
        "title": "Linear vs Exponential",
        "subtitle": "Section 2.5 ('Did You Ever Wonder?'): 1.92-Billion-Step Moon Ladder vs 46 Paper Folds",
        "speech": (
            "Enter Section Two Point Five: Did You Ever Wonder? Let us pit ADDITIVE LINEAR GROWTH head to head against MULTIPLICATIVE EXPONENTIAL GROWTH in an unforgettable cosmic race straight from Earth to the Moon! "
            "Our Moon orbits approximately 3,84,000 kilometers (3.84 × 10⁸ meters) away from Earth! Imagine climbing a giant vertical ladder where EVERY single wooden rung steps up by a constant 20 centimeters (0.2 meters) linearly! How many ladder steps must you climb just to reach the Moon? Divide 3,84,000,000 meters by 0.2 meters per step = 1,920,000,000 steps—nearly TWO BILLION LADDER STEPS (1.92 × 10⁹)! Climbing one rung every second nonstop without rest would take over SIXTY YEARS straight! "
            "Now contrast EXPONENTIAL DOUBLING: begin with that razor-thin 0.001 cm paper sheet! Instead of adding constant 20 cm, every single fold MULTIPLIES thickness cleanly by factor TWO! How many total folds cross that entire Moon distance? JUST FORTY SIX FOLDS—easily completed cleanly in under one single minute! Always recognize this golden mathematical rule of growth: linear growth slowly adds fixed equal amounts step after step, whereas exponential growth repeatedly multiplies and rapidly explodes skyward far past ordinary human cosmic intuition every single time without fail!"
        ),
        "checkpoints": [
            {
                "question": "Why does climbing a 20-cm-per-step ladder to the Moon take ~1.92 billion steps, whereas folding 0.001 cm paper takes only ~46 folds?",
                "options": [
                    "The ladder uses slow ADDITIVE (linear) growth (+0.2 m each step), whereas paper folding uses fast MULTIPLICATIVE (exponential) growth (×2 each fold)!",
                    "Paper folds add 10 km every single fold",
                    "Ladder steps shrink over distance",
                    "Moon distance equals 46 meters"
                ],
                "answer": 0,
                "hint": "Contrast adding a constant (+c) vs multiplying by a constant (×r)!",
                "explanation": "Linear additive steps scale slowly as n × 0.2 m, whereas exponential multiplicative steps explode as 2ⁿ × 0.001 cm."
            },
            {
                "question": "If a savings jar starts at ₹100 and ADDS ₹100 daily (linear) vs a magic coin starting at ₹1 and DOUBLING daily (exponential), which grows larger by Day 15?",
                "options": [
                    "Exponential doubling (2¹⁴ = ₹16,384) easily beats Linear addition (15 × 100 = ₹1,500)!",
                    "Linear addition (₹1,500) stays ahead forever",
                    "Both equal ₹1,500 on Day 15",
                    "Both reach zero"
                ],
                "answer": 0,
                "hint": "Compare 15 × 100 = 1,500 against 2¹⁴ = 16,384!",
                "explanation": "By Day 15, linear totals ₹1,500 while exponential doubling explodes to ₹16,384."
            }
        ]
    },
    {
        "id": 13,
        "title": "Orders Of Magnitude",
        "subtitle": "Section 2.5 Scale: From 10⁰ Species & 10⁹s Age (~31.7 yr) to 10¹⁷s Universe Age & 10²⁵ Water Drops",
        "speech": (
            "Now take a cosmic elevator ride across POWERS OF TEN inside Section Two Point Five: 'Getting a Sense for Large Numbers' and 'A different way to say your age!' "
            "Check physical counts in nature first: critically endangered wild species on Earth count around 10⁰ to 10³ (single digits to thousands); total human population climbs past 8 × 10⁹ (eight billion people); estimated stars shining across the observable universe span roughly 10²³; and individual drops of water across ALL of Earth's oceans total roughly 10²⁵ drops! "
            "Now measure TIME cleanly in SECONDS! How many seconds live inside ONE calendar year? Multiply 365 × 24 × 3,600 ≈ 3.15 × 10⁷ seconds! Watch what magic milestone hits ONE BILLION SECONDS (10⁹ s): divide 10⁹ by 3.15 × 10⁷ ≈ THIRTY ONE POINT SEVEN YEARS! That means a 32-year-old adult has already lived roughly 10⁹ seconds! Recorded human historical civilizations span 10¹⁰ seconds, biological evolutionary milestones span 10¹² to 10¹⁵ seconds, and the entire age of our observable Universe (~13.8 billion years) equals roughly 4 × 10¹⁷ seconds—showing clearly how simple powers of ten help us compare gigantic cosmic and natural timescales effortlessly across modern observational physical science!"
        ),
        "checkpoints": [
            {
                "question": "Approximately what order of magnitude in SECONDS matches a ~32-year-old human age, vs the ~13.8-billion-year age of the Universe?",
                "options": [
                    "Human ~32 yrs ≈ 10⁹ seconds;   Universe age ≈ 10¹⁷ seconds",
                    "Human age ≈ 10⁵ seconds;   Universe ≈ 10⁹ seconds",
                    "Human age ≈ 10¹² seconds;   Universe ≈ 10¹⁰ seconds",
                    "Both equal 10⁶ seconds"
                ],
                "answer": 0,
                "hint": "1 year ≈ 3.15 × 10⁷ seconds; multiply 32 × 3.15 × 10⁷ ≈ 10⁹ s!",
                "explanation": "1 billion seconds (10⁹ s) is ~31.7 years; 13.8 × 10⁹ yrs × 3.15 × 10⁷ s/yr ≈ 4.3 × 10¹⁷ s (order 10¹⁷)."
            },
            {
                "question": "Which scale matches estimated stars in the observable universe (~10²³) and water drops on Earth (~10²⁵)?",
                "options": [
                    "10²⁵ drops is 100 times (10²) larger than 10²³ stars",
                    "10²³ stars is larger than 10²⁵ drops",
                    "10²⁵ is only 2 times larger than 10²³",
                    "Both lie below 10⁹"
                ],
                "answer": 0,
                "hint": "Divide powers cleanly using Quotient Rule: 10²⁵ ÷ 10²³ = 10^(25−23) = 10²!",
                "explanation": "10²⁵ / 10²³ = 10² = 100× more drops of water on Earth than stars in the observable universe."
            }
        ]
    },
    {
        "id": 14,
        "title": "Units Digit Cycles",
        "subtitle": "Section 2.5 Figure It Out: Units-Digit Cycles (2ⁿ, 3ⁿ, 4ⁿ, 9ⁿ) & Comparing Huge Powers (2¹⁰⁰ vs 3⁷⁵)",
        "speech": (
            "Master two elite Section Two Point Five 'Figure it Out' problem-solving weapons right now: CYCLIC UNITS DIGITS and COMPARING GIANT EXPONENTIAL POWERS! "
            "Weapon One, Units-Digit Cycles: Find the rightmost last digit of 2⁵⁰ without multiplying fifty times! Track powers 2¹, 2², 2³, 2⁴, 2⁵: last digits run 2, 4, 8, 6, then repeat cleanly 2, 4, 8, 6 in an unbroken CYCLE OF LENGTH FOUR! Divide exponent 50 by cycle length 4: 50 = 4 × 12 + REMAINDER 2! Remainder 2 picks the 2nd cycle entry (matching 2²) = FOUR! Test 3ⁿ similarly: {3, 9, 7, 1} repeats every 4! Meanwhile 5ⁿ ALWAYS ends in 5, 6ⁿ ALWAYS ends in 6, 4ᵒᵈᵈ ends 4 while 4ᵉᵛᵉⁿ ends 6, and 9ᵒᵈᵈ ends 9 while 9ᵉᵛᵉⁿ ends 1! "
            "Weapon Two, Comparing Giant Powers: Compare 2¹⁰⁰ versus 3⁷⁵ instantly without multiplying! Rewrite BOTH large numbers cleanly with matching outer exponent 25 (using HCF of 100 and 75): 2¹⁰⁰ equals (2⁴)²⁵ equals 16²⁵, while 3⁷⁵ equals (3³)²⁵ equals 27²⁵! Instantly notice 27²⁵ > 16²⁵, proving cleanly beyond any possible doubt that 3⁷⁵ always wins easily without ever having to expand or calculate a single giant digit manually on paper!"
        ),
        "checkpoints": [
            {
                "question": "Find the units (ones) digit of 2⁵⁰ + 5⁹⁹ + 6²⁰ without expanding:",
                "options": [
                    "5   (since 2⁵⁰ ends in 4, 5⁹⁹ ends in 5, 6²⁰ ends in 6; 4 + 5 + 6 = 15 → 5!)",
                    "1",
                    "7",
                    "0"
                ],
                "answer": 0,
                "hint": "50 = 4×12 + 2 gives 2² → 4; powers of 5 always end 5; powers of 6 always end 6!",
                "explanation": "Units digits: 4 + 5 + 6 = 15, leaving units digit 5."
            },
            {
                "question": "Which number is larger between 2¹⁰⁰ and 3⁷⁵, and why?",
                "options": [
                    "3⁷⁵ is larger, because 2¹⁰⁰ = (2⁴)²⁵ = 16²⁵ whereas 3⁷⁵ = (3³)²⁵ = 27²⁵!",
                    "2¹⁰⁰ is larger because exponent 100 > 75",
                    "Both are equal",
                    "2¹⁰⁰ = 8²⁵ < 3⁷⁵ = 9²⁵"
                ],
                "answer": 0,
                "hint": "Find HCF(100, 75) = 25 and match outside exponent 25 on both!",
                "explanation": "Rewriting 2¹⁰⁰ = 16²⁵ and 3⁷⁵ = 27²⁵ immediately proves 3⁷⁵ > 2¹⁰⁰."
            }
        ]
    },
    {
        "id": 15,
        "title": "Ancient Large Powers",
        "subtitle": "Section 2.5 History: Lalitavistara (10⁵³), Amalasiddhi (10⁹⁶), Indian vs International & Googol",
        "speech": (
            "Journey deep into Section Two Point Five: A Pinch of History! Thousands of years before Western pocket calculators existed, ancient Indian scholars invented specific poetic Sanskrit names for astonishingly gigantic powers of ten! "
            "Check these mind-blowing classical historical records carefully: Mahaviracharya's Ganita-sara-sangraha (850 CE) named powers cleanly up to 10²³! The ancient Buddhist text LALITAVISTARA scaled up cleanly to Tallakshana equal to 10⁵³! Jaina mathematical treatises like Amalasiddhi reached 10⁹⁶, and ancient Pali works climbed all the way up to 10¹⁴⁰ (Asankhyeya)! "
            "Compare Indian versus International naming grids cleanly side by side! Indian place values group every 2 digits past thousands cleanly: Lakh = 10⁵, Crore = 10⁷, Arab = 10⁹, Kharab = 10¹¹, Neel = 10¹³, Padma = 10¹⁵, and Shankh = 10¹⁷! International places jump strictly by 3 zeros (10³): Million = 10⁶, Billion = 10⁹ (equal to 1 Arab!), Trillion = 10¹², Quadrillion = 10¹⁵, all the way up to Decillion = 10³³! Also meet famous modern named exponential giants: GOOGOL equals 10¹⁰⁰ (digit one followed cleanly by 100 zeros), GOOGOLPLEX equals 10^(googol) (meaning one followed by a googol trailing zeros!), and Hungary's historic 1946 one-sextillion (10²¹) pengő hyper-inflation national paper currency banknote!"
        ),
        "checkpoints": [
            {
                "question": "Match the Indian place-value system powers cleanly: 1 Lakh, 1 Crore, and 1 Arab equal which exact powers of 10?",
                "options": [
                    "1 Lakh = 10⁵,   1 Crore = 10⁷,   1 Arab = 10⁹ (= 1 Billion)",
                    "1 Lakh = 10⁶,   1 Crore = 10⁸,   1 Arab = 10¹⁰",
                    "1 Lakh = 10⁵,   1 Crore = 10⁶,   1 Arab = 10⁹",
                    "1 Lakh = 10⁴,   1 Crore = 10⁷,   1 Arab = 10¹²"
                ],
                "answer": 0,
                "hint": "Indian system increments by 10² after thousands: 10³, 10⁵, 10⁷, 10⁹, 10¹¹, 10¹³, 10¹⁵, 10¹⁷!",
                "explanation": "Lakh = 10⁵ (100,000), Crore = 10⁷ (10 million), Arab = 10⁹ (1 billion)."
            },
            {
                "question": "Which ancient Indian text listed powers of 10 up to Tallakshana (10⁵³), and what does one Googol equal?",
                "options": [
                    "Buddhist text Lalitavistara (10⁵³);   and 1 Googol = 10¹⁰⁰",
                    "Lalitavistara (10²³);   and 1 Googol = 10¹⁰",
                    "Pali text (10⁵);   and 1 Googol = 10¹⁰⁰⁰",
                    "Ganita-sara-sangraha (10⁵³);   and 1 Googol = 10⁵³"
                ],
                "answer": 0,
                "hint": "Lalitavistara reached 10⁵³ (Jaina Amalasiddhi 10⁹⁶, Pali 10¹⁴⁰), and Googol is 1 followed by 100 zeros!",
                "explanation": "Lalitavistara names powers up to 10⁵³; Googol = 10¹⁰⁰ (and Googolplex = 10^googol)."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter Two Summary",
        "subtitle": "Chapter Recap & Puzzle Time: 'Tremendous in Ten!' Arithmetic + Exponent Maximization Game",
        "speech": (
            "Congratulations on mastering NCERT Class Eight Chapter Two: Power Play! Snapshot ALL core exponent formulas before solving forty Quiz Questions and playing 'Tremendous in Ten!' "
            "Master Law Checklist (assuming x, m, n ≠ 0): Product same-base nᵃ × nᵇ = n^(a+b); Quotient same-base nᵃ ÷ nᵇ = n^(a−b); Nested Power (nᵃ)ᵇ = nᵃᵇ; Same-exponent mᵃ × nᵃ = (mn)ᵃ and mᵃ ÷ nᵃ = (m/n)ᵃ; Zero exponent x⁰ = 1; Negative reciprocal n⁻ᵃ = 1 / nᵃ; Decimal expansions using powers of 10; and Scientific Notation x × 10ʸ with 1 ≤ x < 10! "
            "Now tackle IT'S PUZZLE TIME—Tremendous in Ten! Using given digits like 2, 3, and 4 with arithmetic operations and exponents inside 10 rapid countdown seconds, how do you construct the LARGEST POSSIBLE VALUE? Strategy of Champions: ALWAYS stack your BIGGEST available digits HIGH up as top-heavy EXPONENTS rather than adding or multiplying! Compare every single option carefully: 2+3+4 = 9; 2×3×4 = 24; 4^(3²) = 2¹⁸ = 2,62,144; whereas 2^(3⁴) = 2⁸¹ explodes straight upward into a massive 25-digit astronomical colossus exceeding 2.4 × 10²⁴! Never waste valuable high digits on simple multiplication, subtraction, integer division, or slow plain daily addition!"
        ),
        "checkpoints": [
            {
                "question": "In 'Tremendous in Ten!' using numbers {2, 3, 4} once each, which nested exponent tower creates the LARGEST number?",
                "options": [
                    "2^(3⁴) = 2⁸¹   (approx. 2.4 × 10²⁴!)",
                    "4^(3²) = 4⁹ = 2¹⁸ = 2,62,144",
                    "(2³)⁴ = 2¹² = 4,096",
                    "4 × 3 × 2 = 24"
                ],
                "answer": 0,
                "hint": "Put the largest digits HIGH up inside the exponent of an exponent so the top tower explodes first: 3⁴ = 81!",
                "explanation": "Top-heavy tower 2^(3⁴) = 2⁸¹ ≈ 2.4 × 10²⁴ dwarfs 4⁹ (262,144) and 3^(4²) = 3¹⁶ (43,046,721)!"
            },
            {
                "question": "Which summary statement across ALL Chapter 2 exponent laws is 100% accurate?",
                "options": [
                    "nᵃ×nᵇ = n^(a+b); nᵃ÷nᵇ = n^(a−b); (nᵃ)ᵇ = nᵃᵇ; mᵃ×nᵃ = (mn)ᵃ; x⁰ = 1 (x≠0); n⁻ᵃ = 1/nᵃ",
                    "nᵃ + nᵇ = n^(a+b) always holds",
                    "x⁰ equals 0 for all numbers",
                    "Scientific notation allows 42 × 10⁵ cleanly"
                ],
                "answer": 0,
                "hint": "Verify every law excludes addition traps, sets x⁰ = 1, and enforces 1 ≤ x < 10!",
                "explanation": "Option 1 states every Section 2.2–2.4 formula accurately."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part2)} slides for Ch2 Class 8 Maths Part 2.")
    for s in slides_part2:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 2 assertions passed cleanly!")
