#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 9 Mathematics Chapter 11: The World of Algorithms
Part 1: Slides 1 to 8 (with Indian Male Teacher Lecture, 195-215 words per slide)
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Adding Numbers Efficiency",
        "subtitle": "Section 11.1 Adding Numbers: Primitive Dot Counting vs Indian Place-Value Column Addition",
        "speech": (
            "Welcome to Chapter Eleven: The World of Algorithms! Every smartphone app, calculator, search engine, and banking system runs on carefully designed step-by-step recipes called ALGORITHMS! "
            "Begin inside Section Eleven Point One with an everyday task you already know: ADDING TWO NUMBERS! Suppose you want to add forty-seven and thirty-five! A primitive method draws forty-seven dots in one group, draws thirty-five dots in a second group, and counts every single dot one by one until reaching eighty-two! "
            "Now imagine adding two ten-digit numbers—say five billion plus three billion! Drawing and counting eight billion individual dots would take a human lifetime! Why? Because dot counting scales with the MAGNITUDE of the numbers! "
            "Now compare that primitive method with India's base-ten PLACE-VALUE COLUMN ADDITION! You align ones under ones, tens under tens, and add just TWO digits at a time from right to left! Adding two ten-digit numbers takes only TEN tiny single-digit additions—finished in seconds! That massive leap in speed illustrates why designing smart algorithms matters: a great algorithm scales with the NUMBER OF DIGITS, not the sheer size of the numbers! This single insight separates slow primitive counting from lightning-fast modern arithmetic across every digital computer!"
        ),
        "checkpoints": [
            {
                "question": "Why does place-value column addition outperform dot counting so dramatically for large numbers?",
                "options": [
                    "Column addition scales with the number of digits (e.g., 10 steps for 10-digit numbers), whereas dot counting scales with the numerical magnitude (billions of steps)",
                    "Because dot counting cannot add numbers above 100",
                    "Because column addition skips the ones place",
                    "Because base-10 only uses 2 digits"
                ],
                "answer": 0,
                "hint": "Compare counting 1,000,000,000 dots versus adding 10 digit columns!",
                "explanation": "Place-value representation compresses exponentially large quantities into compact digit strings, making column addition linear in digit count."
            },
            {
                "question": "In computing, what is an 'algorithm'?",
                "options": [
                    "A precise, finite, step-by-step procedure that transforms valid inputs into the guaranteed correct output",
                    "A random guess at an arithmetic answer",
                    "Only a list of prime numbers",
                    "A geometric drawing without measurements"
                ],
                "answer": 0,
                "hint": "Think of a clear recipe with unambiguous steps and a guaranteed stopping point!",
                "explanation": "An algorithm is a well-defined finite sequence of instructions solving a class of problems reliably."
            }
        ]
    },
    {
        "id": 2,
        "title": "Digit Addition Algorithm",
        "subtitle": "Section 11.1.1 Adding Numbers Digit by Digit: Formal 5-Step Algorithm, Carrying & Scaling",
        "speech": (
            "Now formalize place-value addition into a crystal-clear FIVE-STEP COMPUTER-READY ALGORITHM inside Section Eleven Point One Point One! "
            "Step One: ALIGN both numbers cleanly by their rightmost ones digits, padding any shorter number on the left with leading zeros so both have equal digit length d! Step Two: INITIALIZE a carry variable c equals zero, and set your column pointer i to the rightmost units column! "
            "Step Three: ADD the two digits in column i together with incoming carry c, producing column sum s! Step Four: WRITE DOWN the units digit of s (s modulo ten) as the answer digit for column i, and UPDATE carry c to one if s is ten or more, or zero otherwise! "
            "Step Five: MOVE the column pointer one position left and REPEAT Steps Three and Four until every column is processed—writing a final leading one if carry c equals one at the very end! "
            "Notice our basic execution assumption: a human or processor already knows single-digit addition facts up to nine plus nine plus one equals nineteen! With that small lookup table, adding ANY two d-digit numbers requires at most d repetitions—clean, predictable, and blazingly fast even on thousand-digit numbers!"
        ),
        "checkpoints": [
            {
                "question": "During Step 3–4 of the digit-by-digit addition algorithm, suppose column digits are 7 and 8 with incoming carry c = 1. What digit is written and what is the new carry?",
                "options": [
                    "Sum s = 16 → write digit 6 and update carry c = 1",
                    "Sum s = 15 → write digit 5 and carry c = 1",
                    "Write digit 1 and carry c = 6",
                    "Write digit 16 in the single column"
                ],
                "answer": 0,
                "hint": "Add 7 + 8 + 1 = 16; take units digit (16 mod 10) and tens digit for carry!",
                "explanation": "7 + 8 + 1 = 16 gives output digit 6 and new carry c = 1 for the next column left."
            },
            {
                "question": "What is the largest possible column sum s in base-10 addition of two numbers (including incoming carry c)?",
                "options": [
                    "19 (9 + 9 + 1), which guarantees the outgoing carry is always 0 or 1",
                    "18 (9 + 9)",
                    "20 (9 + 9 + 2)",
                    "99"
                ],
                "answer": 0,
                "hint": "Each digit is at most 9 and incoming carry is at most 1!",
                "explanation": "9 + 9 + 1 = 19, so the carry passed to the next column never exceeds 1."
            }
        ]
    },
    {
        "id": 3,
        "title": "Greatest Common Divisor",
        "subtitle": "Section 11.2 Greatest Common Divisor: Breaking Down GCD / HCF into Sub-Problems",
        "speech": (
            "Now shift from addition to one of the most celebrated problems in both number theory and computer science inside Section Eleven Point Two: COMPUTING THE GREATEST COMMON DIVISOR (GCD), also called Highest Common Factor (HCF)! "
            "Given two positive integers m and n—say twenty-four and thirty-six—what is the largest positive integer that divides BOTH m and n evenly with zero remainder? "
            "Before jumping straight to code, master a golden algorithmic habit: PROBLEM DECOMPOSITION! Instead of tackling one messy goal all at once, break GCD cleanly into THREE smaller, crystal-clear sub-problems! "
            "Sub-Problem One: Generate an ordered list of ALL positive divisors of m, and a second ordered list of ALL positive divisors of n! Sub-Problem Two: Compare those two divisor lists to collect every number appearing in BOTH lists—the COMMON DIVISORS! Sub-Problem Three: Identify the MAXIMUM (largest) value inside that common divisor list! "
            "For twenty-four and thirty-six, common divisors are one, two, three, four, six, and twelve—so GCD equals TWELVE! Breaking big tasks into modular sub-problems makes algorithms easy to design, test, and prove correct! Every single sub-problem becomes an independent, cleanly testable building block you can reuse across many different mathematical computer programs and software engineering projects!"
        ),
        "checkpoints": [
            {
                "question": "In Section 11.2, into which three sub-problems is finding gcd(m, n) first decomposed?",
                "options": [
                    "(1) Compute divisor lists of m and n, (2) compare lists to find common divisors, (3) pick the largest common divisor",
                    "(1) Multiply m and n, (2) add digits, (3) subtract 1",
                    "(1) Factor into decimals, (2) round up, (3) average",
                    "(1) Count dots, (2) square both numbers, (3) divide by 2"
                ],
                "answer": 0,
                "hint": "Follow the exact three words in 'Greatest Common Divisor' from right to left: Divisor → Common → Greatest!",
                "explanation": "Decomposing into divisor generation, list comparison for common divisors, and maximum selection builds the naive GCD algorithm."
            },
            {
                "question": "What is gcd(28, 42)?",
                "options": ["14", "7", "28", "6"],
                "answer": 0,
                "hint": "Divisors of 28: {1, 2, 4, 7, 14, 28}; Divisors of 42: {1, 2, 3, 6, 7, 14, 21, 42}!",
                "explanation": "The common divisors are 1, 2, 7, and 14, so the greatest common divisor is 14."
            }
        ]
    },
    {
        "id": 4,
        "title": "Divisor List Algorithm",
        "subtitle": "Section 11.2.1 Computing the Divisors of a Number: Sequential Check from 1 to n",
        "speech": (
            "Now write out Sub-Problem One as an explicit loop algorithm inside Section Eleven Point Two Point One: COMPUTING ALL DIVISORS OF A POSITIVE INTEGER n! "
            "How do we guarantee we find EVERY positive divisor of n in neat increasing order without missing a single one? Start with an empty list D! Initialize a loop counter i equals one! "
            "Repeat while i is less than or equal to n: test whether i divides n evenly—meaning n modulo i equals zero (remainder is zero)! If YES, append i onto the end of list D! Then increment i by one (i becomes i plus one) and continue the loop! When i exceeds n, stop and return list D! "
            "Trace this algorithm on n equals twelve! Test i equals one (remainder zero, append one); two (append two); three (append three); four (append four); five (remainder two, skip!); six (append six); seven through eleven (skip!); twelve (append twelve)! Output list D equals one, two, three, four, six, twelve! Notice: checking one up to n automatically produces list D in strictly ascending order, guaranteeing that no divisor is ever skipped or duplicated anywhere between one and n during the entire loop execution!"
        ),
        "checkpoints": [
            {
                "question": "In the sequential divisor-listing algorithm for n = 18, how many divisibility checks (i = 1 to n) are performed?",
                "options": [
                    "18 checks (testing every integer i from 1 up to 18)",
                    "6 checks (only the 6 divisors)",
                    "9 checks",
                    "1 check"
                ],
                "answer": 0,
                "hint": "The loop checks EVERY integer i from 1 to n inclusive!",
                "explanation": "Even though 18 has only 6 divisors {1, 2, 3, 6, 9, 18}, the basic 1-to-n loop performs all 18 remainder checks."
            },
            {
                "question": "Why does the list D returned by checking i = 1, 2, ..., n automatically appear in increasing sorted order?",
                "options": [
                    "Because candidate divisors i are tested in strictly increasing order from 1 up to n and appended as found",
                    "Because a separate sorting step runs afterward",
                    "Because all divisors are prime",
                    "Because n is always even"
                ],
                "answer": 0,
                "hint": "Each appended value is strictly larger than all previously appended values!",
                "explanation": "Since i increases by +1 on each iteration, appending qualifying i values preserves ascending order automatically."
            }
        ]
    },
    {
        "id": 5,
        "title": "Comparing Divisor Lists",
        "subtitle": "Section 11.2.2 Finding the Greatest Common Divisor: Comparing Two Divisor Lists",
        "speech": (
            "Now tackle Sub-Problems Two and Three inside Section Eleven Point Two Point Two: COMPARING TWO ORDERED DIVISOR LISTS TO FIND THE GREATEST COMMON DIVISOR! "
            "Suppose our divisor algorithm produced List A for m equals eighteen: one, two, three, six, nine, eighteen; and List B for n equals twenty-four: one, two, three, four, six, eight, twelve, twenty-four! "
            "How does an algorithm systematically extract common divisors? Create an empty Common List C! Take each element x from List A one by one and scan List B to check if x appears inside List B! If x is found in both lists, append x into Common List C! "
            "Even smarter: because List A and List B are ALREADY SORTED in ascending order, we can either scan List A from left to right and simply take the VERY LAST element appended to C, OR scan List A from RIGHT TO LEFT (largest to smallest) and stop immediately at the FIRST match! Wait—that early-exit trick returns SIX immediately on eighteen and twenty-four without scanning smaller factors! Sorted lists turn messy trial-and-error comparisons into clean, systematic scans from either left to right or right to left across large factor collections with complete precision!"
        ),
        "checkpoints": [
            {
                "question": "Given ordered divisor lists A = [1, 2, 3, 6, 9, 18] and B = [1, 2, 3, 4, 6, 8, 12, 24], what is the common divisor list C and the GCD?",
                "options": [
                    "C = [1, 2, 3, 6], so GCD = 6",
                    "C = [1, 2, 3], so GCD = 3",
                    "C = [6, 12, 18], so GCD = 18",
                    "C = [1, 2, 4, 6], so GCD = 6"
                ],
                "answer": 0,
                "hint": "Pick every number present in BOTH A and B, then choose the maximum!",
                "explanation": "The shared elements are 1, 2, 3, and 6, making the largest common divisor 6."
            },
            {
                "question": "If List A is sorted in ascending order and we scan A from right to left (largest to smallest) checking membership in B, when can we stop?",
                "options": [
                    "Immediately at the very first element of A that also appears in B, since it is guaranteed to be the largest!",
                    "Only after checking every element down to 1",
                    "At the second match",
                    "Never — we must always reach 1"
                ],
                "answer": 0,
                "hint": "If we test 18, 9, 6 in descending order, the first match 6 is automatically the greatest!",
                "explanation": "Scanning from largest to smallest means the first common element encountered is the maximum possible."
            }
        ]
    },
    {
        "id": 6,
        "title": "Naive GCD Algorithm",
        "subtitle": "Section 11.2.3 First Algorithm for gcd: Combining Divisor Listing & List Matching",
        "speech": (
            "Now assemble all three sub-problems into our FIRST COMPLETE GCD ALGORITHM inside Section Eleven Point Two Point Three! "
            "Input: two positive integers m and n! Step One: Run the divisor-listing loop from one to m to build ordered List D sub m! Step Two: Run the divisor-listing loop from one to n to build ordered List D sub n! Step Three: Compare D sub m and D sub n to construct Common List C containing every divisor present in both lists! Step Four: Return the last (largest) element in C—which is guaranteed to exist because ONE always divides both m and n! "
            "Let us verify CORRECTNESS! Can this algorithm ever fail or enter an infinite loop? Never! Every loop runs a finite number of steps (m steps, n steps, then list comparison), and one is ALWAYS in both lists so C is never empty! "
            "Now ask the crucial computer-science question: IT IS CORRECT, BUT IS IT FAST? For m equals one million and n equals two million, building both lists performs THREE MILLION remainder checks and stores huge lists in memory! Can we do much better? Yes—by redesigning both our intermediate storage and our search range!"
        ),
        "checkpoints": [
            {
                "question": "Why is the common divisor list C in the naive GCD algorithm GUARANTEED to be non-empty for ANY positive integers m and n?",
                "options": [
                    "Because 1 divides every positive integer, so 1 is always present in both divisor lists",
                    "Because m and n are always even",
                    "Because 2 always divides both m and n",
                    "Because C always contains m × n"
                ],
                "answer": 0,
                "hint": "Which positive integer divides every integer without exception?",
                "explanation": "1 is a universal divisor of all positive integers, ensuring gcd(m, n) ≥ 1 always exists."
            },
            {
                "question": "For m = 1,000,000 and n = 2,000,000, approximately how many division checks does the naive two-list GCD algorithm perform just to build D_m and D_n?",
                "options": [
                    "3,000,000 checks (1,000,000 + 2,000,000)",
                    "20 checks",
                    "1,000 checks",
                    "2 checks"
                ],
                "answer": 0,
                "hint": "Building D_m takes m checks and building D_n takes n checks!",
                "explanation": "Separate 1-to-m and 1-to-n scans perform m + n = 3,000,000 checks."
            }
        ]
    },
    {
        "id": 7,
        "title": "Intermediate Data Structures",
        "subtitle": "Section 11.3 Data Structures: Using Ordered Lists & Variables to Organize Computation",
        "speech": (
            "Pause and notice what made our naive GCD algorithm clean and modular inside Section Eleven Point Three: DATA STRUCTURES! "
            "A DATA STRUCTURE is a systematic way of storing, organizing, and managing intermediate values in memory so an algorithm can access and update them cleanly! In our first GCD algorithm, we used THREE ordered lists—D sub m, D sub n, and Common List C! "
            "Lists are wonderfully expressive: they let us inspect all factors of a number, print them, or reuse them across multiple queries! However, every data structure carries a MEMORY COST and a TIME COST! Storing giant lists of thousands of factors consumes computer memory, and searching through two separate lists wastes extra comparison steps! "
            "As algorithm designers, we constantly ask two sharp engineering questions! Question One: Do we actually NEED to store all intermediate values in a list, or can a smaller structure—even a SINGLE VARIABLE—hold everything we need? Question Two: Can we combine separate loops into ONE single pass? Answering both questions unlocks dramatic optimizations next! Every skilled programmer chooses the lightest data structure that still preserves all required information without wasting precious computer memory, storage space, or extra loop execution cycles!"
        ),
        "checkpoints": [
            {
                "question": "In Section 11.3, what is the primary purpose of a 'data structure' inside an algorithm?",
                "options": [
                    "To systematically store, organize, and manage intermediate values cleanly during execution",
                    "To replace all mathematical formulas with guesses",
                    "To increase the number of steps an algorithm takes",
                    "To convert decimal numbers into Roman numerals"
                ],
                "answer": 0,
                "hint": "Think about how ordered lists D_m, D_n, and C organized divisors between steps!",
                "explanation": "Data structures organize intermediate state (such as lists, arrays, or single variables) for efficient algorithmic processing."
            },
            {
                "question": "What trade-off must an algorithm designer watch for when storing large intermediate lists?",
                "options": [
                    "Lists consume extra memory space and require extra traversal/search time",
                    "Lists always produce wrong answers",
                    "Lists cannot store integers",
                    "Lists can only hold 2 items"
                ],
                "answer": 0,
                "hint": "Think about memory usage and comparison steps when lists grow large!",
                "explanation": "Reducing or eliminating unnecessary intermediate lists saves both memory and runtime."
            }
        ]
    },
    {
        "id": 8,
        "title": "Three GCD Optimizations",
        "subtitle": "Section 11.3.1 Improving the Algorithm: Scanning to max(m,n), min(m,n) & Eliminating Lists",
        "speech": (
            "Watch our GCD algorithm transform through THREE brilliant optimization stages inside Section Eleven Point Three Point One! "
            "Stage One: Instead of running two separate loops for m and n, run ONE single loop i from one up to MAX(m, n)! Inside each step, if i divides m, append to D sub m; if i divides n, append to D sub n! That cuts separate loops down, though it still builds two lists! "
            "Stage Two: Wait a second! Can ANY common divisor of m and n EVER be larger than the SMALLER number, MIN(m, n)? Impossible—no divisor of twelve can exceed twelve! So why scan up to max(m, n) at all? Scan i ONLY from one up to MIN(m, n), and whenever i divides BOTH m AND n simultaneously, append i directly into ONE single Common List C! "
            "Stage Three: Why even keep Common List C when we ONLY want the LARGEST common divisor?! Eliminate EVERY list completely! Keep ONE single integer variable best_gcd initialized to one! As i scans from one to min(m, n), whenever i divides both m and n, simply overwrite best_gcd equals i! Zero lists, minimal memory, and a far cleaner single-loop GCD implementation!"
        ),
        "checkpoints": [
            {
                "question": "Why can Stage 2 of the GCD optimization safely stop scanning at min(m, n) instead of max(m, n)?",
                "options": [
                    "Because no positive divisor of the smaller number can exceed min(m, n), so no common divisor can exceed min(m, n)",
                    "Because all common divisors are less than 10",
                    "Because max(m, n) has no divisors",
                    "Because min(m, n) is always prime"
                ],
                "answer": 0,
                "hint": "Can a factor of 18 ever be larger than 18?",
                "explanation": "Every common divisor must divide min(m, n), so gcd(m, n) ≤ min(m, n)."
            },
            {
                "question": "How does Stage 3 eliminate ALL lists from the 1-to-min(m, n) GCD algorithm?",
                "options": [
                    "By storing only a single variable 'best_gcd' (initialized to 1) and updating it whenever a larger common divisor i is found",
                    "By sorting the lists twice",
                    "By skipping divisibility checks",
                    "By storing 100 lists instead of 3"
                ],
                "answer": 0,
                "hint": "Since i increases from 1 to min(m, n), the most recent common divisor is always the largest so far!",
                "explanation": "Tracking a single variable 'best_gcd' reduces memory from O(min(m, n)) lists to O(1) constant space."
            }
        ]
    }
]
