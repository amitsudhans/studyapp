#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics Chapter 9: Propositions and their Converses
Part 1: Slides 1 to 8 (with Indian Male Teacher Lecture, 195-215 words per slide)
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Proposition Truth Value",
        "subtitle": "Section 9.1 Proposition Fundamentals: Statements That Are Strictly True or False",
        "speech": (
            "Welcome to Chapter Nine: Propositions and Their Converses! Every mathematical proof, computer algorithm, and scientific law stands on clear logical statements! "
            "Inside Section Nine Point One, begin with the fundamental building block of mathematical reasoning: a PROPOSITION! "
            "A PROPOSITION is a formal declarative sentence that can be evaluated as EITHER STRICTLY TRUE OR STRICTLY FALSE—never both simultaneously, and never vague or ambiguous! "
            "Test several everyday and mathematical sentences right now! Statement A: Seven is a prime number. That is definitely TRUE, so it IS a proposition! Statement B: Every rectangle has five sides. That is definitely FALSE, so it STILL counts as a valid proposition! "
            "Now compare sentences that are NOT propositions! First, questions like What time is it? carry no true-or-false value! Second, commands like Close the door! cannot be judged true or false! Third, subjective opinions like Vanilla tastes better than chocolate depend on personal taste rather than objective truth! Fourth, open sentences with unspecified variables like x plus three equals seven depend on what number x represents! Once you fix x equals four, it becomes a true proposition; fix x equals five, and it becomes a clearly false proposition with zero ambiguity!"
        ),
        "checkpoints": [
            {
                "question": "Which of the following is a valid mathematical PROPOSITION?",
                "options": [
                    "\"The sum of the interior angles of every triangle is 180°.\" (Strictly True)",
                    "\"Please solve Exercise 9.1 before tomorrow!\"",
                    "\"Is 91 a prime number?\"",
                    "\"x + 5 = 12\" (with x completely unspecified)"
                ],
                "answer": 0,
                "hint": "A proposition must be a declarative statement that is unambiguously either True or False!",
                "explanation": "A geometric theorem statement is objectively true, whereas commands, questions, and open equations with free variables have no fixed truth value."
            },
            {
                "question": "If someone writes \"2 + 2 = 5\", is this sentence still considered a proposition in logic?",
                "options": [
                    "Yes — it is a valid proposition whose truth value is strictly FALSE",
                    "No — only true sentences are propositions",
                    "No — because it contains an equals sign",
                    "Only if we change 5 to 4 first"
                ],
                "answer": 0,
                "hint": "Check the definition: a proposition can be EITHER true OR false, just not ambiguous!",
                "explanation": "Being a proposition means having a definite truth value (True or False). \"2 + 2 = 5\" is unambiguously False, so it is a false proposition."
            }
        ]
    },
    {
        "id": 2,
        "title": "If-Then Implication Structure",
        "subtitle": "Section 9.1 Conditional Statements: 'If X, then Y' (X ⇒ Y), Premise & Conclusion",
        "speech": (
            "Now inspect the most powerful sentence blueprint in all of mathematics inside Section Nine Point One: THE IF-THEN CONDITIONAL PROPOSITION! "
            "Most mathematical theorems connect two smaller claims using the standard implication structure: IF X, THEN Y, written symbolically with a double arrow as X IMPLIES Y! "
            "Learn both technical roles inside every conditional statement carefully! The first part X, standing immediately after the word IF, is called the PREMISE or HYPOTHESIS—it states the starting condition we assume or are given! The second part Y, standing after the word THEN, is called the CONCLUSION—it states the guaranteed result that follows whenever X holds! "
            "Examine a crisp geometric example: If a polygon is a square, then it has four equal sides! Here, Premise X is 'the polygon is a square', and Conclusion Y is 'it has four equal sides'! "
            "Notice what X implies Y actually promises! It promises that EVERY single case satisfying X MUST also satisfy Y—there are NO exceptions allowed where X happens while Y fails! However, notice carefully: X implies Y makes NO promise whatsoever about situations where starting condition X is false! A rhombus also has four equal sides without being a square, yet the original statement remains completely true!"
        ),
        "checkpoints": [
            {
                "question": "In the proposition \"If a number ends in 0, then it is divisible by 5\", what is the PREMISE (X)?",
                "options": [
                    "A number ends in 0",
                    "It is divisible by 5",
                    "Every multiple of 5 ends in 0",
                    "The word 'then'"
                ],
                "answer": 0,
                "hint": "Look immediately after the word 'If' to locate the starting assumption X!",
                "explanation": "In \"If X, then Y\", X (\"a number ends in 0\") is the premise/hypothesis and Y (\"it is divisible by 5\") is the conclusion."
            },
            {
                "question": "When is the conditional statement \"If X, then Y\" (X ⇒ Y) guaranteed to be FALSE?",
                "options": [
                    "Whenever there exists a case where Premise X is TRUE, yet Conclusion Y is FALSE",
                    "Whenever Premise X is FALSE",
                    "Whenever Conclusion Y is TRUE",
                    "Whenever X and Y are both FALSE"
                ],
                "answer": 0,
                "hint": "An implication breaks its promise only when the starting condition holds, yet the promised outcome fails!",
                "explanation": "X ⇒ Y is false only when X is true and Y is false simultaneously."
            }
        ]
    },
    {
        "id": 3,
        "title": "Converse Statement Flip",
        "subtitle": "Section 9.1 Definition of Converse: Flipping 'If X, then Y' into 'If Y, then X'",
        "speech": (
            "Now master the central transformation of Chapter Nine: FORMING THE CONVERSE OF A PROPOSITION! "
            "Given any conditional proposition in standard form 'If X, then Y', its CONVERSE is constructed by simply SWAPPING the premise and the conclusion, producing 'If Y, then X'! In symbolic notation, flipping X implies Y gives Y implies X! "
            "Test this reversal immediately on a clear number example! Original proposition: If a whole number is a multiple of ten, then its units digit is zero! Now swap X and Y to write the converse: If a whole number's units digit is zero, then it is a multiple of ten! Here, BOTH the original proposition AND its converse happen to be TRUE! "
            "Now test a second example! Original proposition: If an animal is a Bengal tiger, then it is a mammal! Clearly TRUE! Flip it to form the converse: If an animal is a mammal, then it is a Bengal tiger! Instantly FALSE—elephants, whales, and bats are mammals too! "
            "This reveals the golden rule of logical converses: KNOWING A PROPOSITION IS TRUE NEVER AUTOMATICALLY PROVES ITS CONVERSE IS TRUE! A proposition and its converse are logically independent—both can be true, one true and one false, or even both false!"
        ),
        "checkpoints": [
            {
                "question": "What is the exact CONVERSE of the proposition: \"If a triangle is equilateral, then all three of its angles equal 60°\"?",
                "options": [
                    "\"If all three angles of a triangle equal 60°, then the triangle is equilateral.\"",
                    "\"If a triangle is not equilateral, then its angles are not 60°.\"",
                    "\"If all three angles are not 60°, then the triangle is not equilateral.\"",
                    "\"A triangle is equilateral and has 60° angles.\""
                ],
                "answer": 0,
                "hint": "Swap the 'If' part (X) and the 'then' part (Y) without negating either clause!",
                "explanation": "The converse of 'If X, then Y' is strictly 'If Y, then X' — swapping premise and conclusion."
            },
            {
                "question": "If a conditional proposition 'If X, then Y' is proven TRUE, what can we conclude about its converse 'If Y, then X'?",
                "options": [
                    "Nothing automatically — the converse must be tested separately and may be either true or false",
                    "The converse is automatically true as well",
                    "The converse is automatically false",
                    "The converse is not a proposition"
                ],
                "answer": 0,
                "hint": "Compare 'Bengal tiger ⇒ mammal' (True) with 'mammal ⇒ Bengal tiger' (False)!",
                "explanation": "Truth of an implication does not guarantee truth of its converse; each direction requires independent evaluation."
            }
        ]
    },
    {
        "id": 4,
        "title": "Counterexamples Disprove Claims",
        "subtitle": "Section 9.1 Role of Counterexamples & Euler's 1732 Disproof of Fermat's Formula 2^(2^n) + 1",
        "speech": (
            "How do mathematicians disprove a universal proposition quickly, cleanly, and beyond any shadow of a doubt? With ONE SINGLE COUNTEREXAMPLE! "
            "A COUNTEREXAMPLE to a proposition 'If X, then Y' is any specific valid instance where Premise X IS COMPLETELY SATISFIED, yet Conclusion Y FAILS! Even if a formula or pattern works for ten thousand numbers in a row, finding JUST ONE counterexample shatters the universal claim forever! "
            "Witness one of the most famous counterexamples in mathematical history! In sixteen forty, French mathematician Pierre de Fermat studied numbers of the form F sub n equals two raised to the power two to the n, PLUS ONE! Check small values of n! At n equals zero: three (prime)! At n equals one: five (prime)! At n equals two: seventeen (prime)! At n equals three: two hundred fifty-seven (prime)! At n equals four: sixty-five thousand five hundred thirty-seven (prime)! Fermat conjectured that EVERY F sub n is prime! "
            "Almost a century later, in seventeen thirty-two, Swiss mathematician Leonhard Euler tested n equals FIVE: two to the thirty-second power plus one equals four billion two hundred ninety-four million nine hundred sixty-seven thousand two hundred ninety-seven, and proved it divides evenly by SIX HUNDRED FORTY-ONE—one single counterexample disproved Fermat's conjecture forever!"
        ),
        "checkpoints": [
            {
                "question": "What must a valid COUNTEREXAMPLE to \"If X, then Y\" satisfy?",
                "options": [
                    "Premise X is TRUE for that example, while Conclusion Y is FALSE",
                    "Both X and Y are FALSE",
                    "Premise X is FALSE while Conclusion Y is TRUE",
                    "It must work for at least 100 cases"
                ],
                "answer": 0,
                "hint": "To break a promise 'If X, then Y', you need a case where X happened, yet Y did not!",
                "explanation": "A single instance where X holds and Y fails proves 'If X, then Y' is false."
            },
            {
                "question": "How did Leonhard Euler (1732) disprove Fermat's conjecture that Fₙ = 2^(2^n) + 1 is ALWAYS prime for every whole number n ≥ 0?",
                "options": [
                    "He showed F₅ = 2³² + 1 = 4,294,967,297 is divisible by 641 (hence composite), providing one decisive counterexample",
                    "He proved F₀ = 3 is composite",
                    "He showed F₄ = 65,537 is divisible by 17",
                    "He proved no primes exist above 1000"
                ],
                "answer": 0,
                "hint": "F₀ through F₄ are all prime, so Euler had to check the very next index n = 5!",
                "explanation": "At n = 5, 2^(2^5) + 1 = 4,294,967,297 = 641 × 6,700,417, disproving Fermat's universal prime claim."
            }
        ]
    },
    {
        "id": 5,
        "title": "Rain Wet Roads",
        "subtitle": "Section 9.2 Example 1: True Conditional ('If it rains, road is wet') vs False Converse",
        "speech": (
            "Now analyze five classic textbook examples inside Section Nine Point Two comparing propositions against their converses! Begin with Example One: RAIN AND WET ROADS! "
            "Consider the everyday conditional proposition: If it rains heavily outside, then the open road becomes completely wet! Under normal outdoor conditions with no overhead roof, whenever rain falls onto the asphalt, the road surface undeniably gets wet—so this forward conditional proposition is unquestionably TRUE! "
            "Now flip the premise and conclusion to examine its CONVERSE: If the open road is wet, then it has rained! Pause and ask critically: Is rain the ONLY possible cause of a wet road? "
            "Immediately imagine counterexamples! Perhaps a municipal water tanker leaked water across the street! Perhaps a street-cleaning truck hosed down the pavement! Perhaps an underground water pipe burst, or morning dew settled overnight, or someone washed a parked car beside the curb! In every single one of those counterexamples, the premise 'the road is wet' is completely TRUE, while the conclusion 'it has rained' is FALSE! "
            "Therefore, Example One proves cleanly: a TRUE forward proposition can easily have a FALSE converse whenever multiple different real-world causes can independently produce the exact same observed effect!"
        ),
        "checkpoints": [
            {
                "question": "For Example 1, why is the converse \"If the road is wet, then it has rained\" FALSE?",
                "options": [
                    "Because a road can be wet from other causes (such as a water tanker spill or street washing) without any rain",
                    "Because rain never wets roads",
                    "Because 'wet' is not an English adjective",
                    "Because the original statement was also false"
                ],
                "answer": 0,
                "hint": "Look for a situation where the road IS wet, yet no rain fell!",
                "explanation": "A water tanker spill or pipe leak makes 'road is wet' true and 'it has rained' false, serving as a valid counterexample."
            },
            {
                "question": "Which logical pattern does Example 1 (Rain and Wet Roads) illustrate?",
                "options": [
                    "Forward proposition TRUE, Converse FALSE",
                    "Forward proposition FALSE, Converse TRUE",
                    "Both TRUE",
                    "Both FALSE"
                ],
                "answer": 0,
                "hint": "Rain guarantees a wet road, but a wet road does not guarantee rain!",
                "explanation": "Rain ⇒ Wet road is True, while Wet road ⇒ Rain is False."
            }
        ]
    },
    {
        "id": 6,
        "title": "Divisibility Six Three",
        "subtitle": "Section 9.2 Example 2: Multiples of 6 vs Multiples of 3 & Numerical Counterexamples",
        "speech": (
            "Now examine Example Two inside Section Nine Point Two: DIVISIBILITY BY SIX AND THREE! "
            "Read the forward proposition carefully: If a whole number is a multiple of six, then it is a multiple of three! Let us PROVE whether this forward statement is always true! Suppose integer n is any multiple of six. By definition, n equals six times k for some integer k! Rewrite six neatly as three times two: n equals three times open two k close! Since two k is an integer, n is AUTOMATICALLY a multiple of three! Every multiple of six—six, twelve, eighteen, twenty-four, thirty—divides cleanly by three! Forward proposition: PROVEN TRUE! "
            "Now flip premise and conclusion to form the CONVERSE: If a whole number is a multiple of three, then it is a multiple of six! Test multiples of three systematically: three, six, nine, twelve, fifteen, eighteen! "
            "Look at NINE right there! Nine is a multiple of three (three times three), satisfying the premise—yet nine divided by six leaves remainder three, so nine is NOT a multiple of six! Fifteen and twenty-one fail too! Just ONE counterexample—such as nine—instantly proves the converse FALSE! Notice why: all multiples of six sit INSIDE the larger circle of multiples of three!"
        ),
        "checkpoints": [
            {
                "question": "Which number is a valid COUNTEREXAMPLE disproving the converse \"If a number is a multiple of 3, then it is a multiple of 6\"?",
                "options": ["9 (multiple of 3, NOT a multiple of 6)", "12", "18", "7"],
                "answer": 0,
                "hint": "The counterexample must BE a multiple of 3, and FAIL to be a multiple of 6!",
                "explanation": "9 = 3 × 3 is a multiple of 3, but 9 is odd and not divisible by 6. (12 and 18 are multiples of 6; 7 is not a multiple of 3.)"
            },
            {
                "question": "Why is the forward proposition \"Every multiple of 6 is a multiple of 3\" ALWAYS true?",
                "options": [
                    "Because any multiple of 6 has the form 6k = 3(2k), which is always 3 times an integer",
                    "Because 6 + 3 = 9",
                    "Because every odd number is a multiple of 3",
                    "Because 6 is smaller than 3"
                ],
                "answer": 0,
                "hint": "Factor 6 as 3 × 2 in n = 6k!",
                "explanation": "Since 3 is a factor of 6, every multiple of 6 (6k = 3 · 2k) is automatically a multiple of 3."
            }
        ]
    },
    {
        "id": 7,
        "title": "Perfect Squares Factors",
        "subtitle": "Section 9.2 Example 3: Perfect Squares ↔ Odd Number of Factors (Biconditional Proof)",
        "speech": (
            "Now witness a breathtaking two-way equivalence inside Section Nine Point Two, Example Three: PERFECT SQUARES AND ODD FACTOR COUNTS! "
            "Examine the proposition: If a positive integer N is a perfect square, then N has an ODD number of positive factors! Let us prove BOTH directions using FACTOR-PARTNER PAIRING! "
            "Take any positive integer N. Every factor d of N pairs naturally with a partner N divided by d! For a non-square like twelve, the pairs are one-and-twelve, two-and-six, three-and-four—three distinct pairs giving SIX factors (an EVEN number)! Why? Because for a non-square, d NEVER equals N divided by d, so every factor has a distinct twin! "
            "Now check a PERFECT SQUARE like thirty-six! Pairs are one-and-thirty-six, two-and-eighteen, three-and-twelve, four-and-nine, PLUS SIX PAIRING WITH ITSELF! That solo square root six contributes ONE lone factor alongside pairs of two, yielding two times k plus one—AN ODD NUMBER OF FACTORS (nine factors)! "
            "Now flip it for the CONVERSE: If N has an odd number of factors, then N must be a perfect square! Since non-squares only form distinct two-factor pairs (always even), an odd total FORCES one factor d to equal its own partner N over d, meaning d squared equals N! BOTH proposition AND converse are TRUE!"
        ),
        "checkpoints": [
            {
                "question": "How many positive factors does 49 (7²) have, and why is that count odd?",
                "options": [
                    "3 factors (1, 7, 49) — odd because partner pair {1, 49} is joined by solo self-paired √49 = 7",
                    "2 factors (1, 49)",
                    "4 factors (1, 7, 14, 49)",
                    "1 factor (7)"
                ],
                "answer": 0,
                "hint": "List every positive integer that divides 49 evenly!",
                "explanation": "49's factors are 1, 7, and 49 (3 factors — odd), because 7 × 7 = 49 pairs 7 with itself."
            },
            {
                "question": "For Example 3 ('N is a perfect square' vs 'N has an odd number of factors'), what are the truth values of the proposition and its converse?",
                "options": [
                    "BOTH the proposition and its converse are TRUE (they imply each other)",
                    "Proposition True, Converse False",
                    "Proposition False, Converse True",
                    "Both False"
                ],
                "answer": 0,
                "hint": "Can a non-square ever have a factor equal to N/d?",
                "explanation": "Distinct factor pairs {d, N/d} always contribute 2 factors each, so an odd total occurs if and only if N = d² for some integer d."
            }
        ]
    },
    {
        "id": 8,
        "title": "Congruence Versus Area",
        "subtitle": "Section 9.2 Example 4: Congruent Triangles ⇒ Equal Area (True), Equal Area ⇒ Congruent (False)",
        "speech": (
            "Now connect logic directly to geometry inside Section Nine Point Two, Example Four: TRIANGLE CONGRUENCE AND EQUAL AREA! "
            "Test the forward proposition first: If two triangles are congruent, then they have equal areas! Recall what congruence means: two triangles are exact copies with identical side lengths and angles, so one can be placed right on top of the other with complete overlap! Identical shapes obviously enclose the exact same surface area! Thus, the forward proposition is unquestionably TRUE! "
            "Now flip premise and conclusion to test the CONVERSE: If two triangles have equal areas, then they must be congruent! Pause and test whether different shapes can hold identical area! "
            "Construct a quick numerical counterexample using area formula half times base times height! Take Triangle One as a right triangle with base six centimetres and height four centimetres: area equals half times six times four equals TWELVE square centimetres! Now take Triangle Two as a right triangle with base twelve centimetres and height two centimetres: area equals half times twelve times two equals TWELVE square centimetres! "
            "Both triangles enclose TWELVE square centimetres, yet their side lengths are completely different—they are NOT congruent! One single counterexample proves the converse FALSE!"
        ),
        "checkpoints": [
            {
                "question": "Which pair of triangles serves as a valid COUNTEREXAMPLE to \"If two triangles have equal areas, then they are congruent\"?",
                "options": [
                    "Right triangle with legs 6 cm, 4 cm (Area = 12 cm²) and right triangle with legs 12 cm, 2 cm (Area = 12 cm²)",
                    "Two triangles both having sides 3 cm, 4 cm, 5 cm",
                    "A triangle with area 12 cm² and another with area 20 cm²",
                    "Two equilateral triangles each of side 5 cm"
                ],
                "answer": 0,
                "hint": "Both triangles must have EQUAL areas while having DIFFERENT side lengths!",
                "explanation": "½(6)(4) = 12 and ½(12)(2) = 12 give equal areas, yet their side lengths (6, 4, √52 vs 12, 2, √148) are not equal, so they are non-congruent."
            },
            {
                "question": "Why is the forward proposition \"If two triangles are congruent, then they have equal areas\" ALWAYS true?",
                "options": [
                    "Congruent triangles have identical side lengths and angles, so they cover the exact same region when superimposed",
                    "Because all triangles have area 12 cm²",
                    "Because congruence only checks perimeter",
                    "Because every triangle is a right triangle"
                ],
                "answer": 0,
                "hint": "Think about Euclid's superposition: identical figures enclose identical space!",
                "explanation": "Congruence is a rigid isometry preserving all lengths and areas."
            }
        ]
    }
]
