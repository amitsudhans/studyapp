# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 10: Elephants, Tigers, and Leopards
Part 2: Slides 9 to 16 Data Generator
Strictly 195 to 215 words per speech lecture.
Zero human names (Raju, Rani, Roja, Raghav, etc. replaced with generic roles).
Clean Unicode throughout (₹, ×, ÷, +, -, =).
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Regrouping Subtraction Math",
        "section": "Multi-Digit Subtraction & Token Unbundling",
        "speech": (
            "Just as addition bundles smaller units into larger place values, subtraction performs the reverse operation: "
            "unbundling higher-order units whenever the top digit is smaller than the bottom digit. Let us examine how wildlife "
            "biologists calculate population differences between regional wildlife reserves. According to census records, Assam shelters "
            "five thousand seven hundred nineteen wild elephants, while Meghalaya shelters one thousand seven hundred fifty-four elephants. "
            "To determine how many more elephants inhabit Assam, we subtract one thousand seven hundred fifty-four from five thousand seven "
            "hundred nineteen. Aligning the numbers by place value columns, we begin in the ones place: nine minus four leaves five ones. "
            "Moving to the tens place, we encounter one ten minus five tens. Because we cannot subtract five from one, we unbundle one hundred "
            "from the hundreds place, reducing seven hundreds to six hundreds and converting the unbundled hundred into ten tens! Adding these "
            "ten tens to our existing one ten gives eleven tens. Now, eleven tens minus five tens equals six tens! In the hundreds place, six "
            "hundreds minus seven hundreds requires another unbundling: unbundling one thousand gives sixteen hundreds, and sixteen minus seven "
            "leaves nine hundreds. Finally, four thousands minus one thousand leaves three thousands, yielding three thousand nine hundred "
            "sixty-five elephants! Unbundling tokens ensures mathematical transparency and computational precision everywhere."
        ),
        "checkpoints": [
            {
                "q": "What is 5,719 - 1,754 calculated using column subtraction with regrouping?",
                "options": ["3,865", "3,955", "3,965", "4,065"],
                "ans": 2,
                "exp": "5,719 - 1,754 = 3,965."
            },
            {
                "q": "When you unbundle 1 hundred in the column algorithm, how many tens do you obtain?",
                "options": ["5 tens", "10 tens", "50 tens", "100 tens"],
                "ans": 1,
                "exp": "1 hundred equals exactly 10 tens."
            }
        ]
    },
    {
        "id": 10,
        "title": "Park Attendance Records",
        "section": "Tourism Data & Comparative Visitor Audits",
        "speech": (
            "National parks and tiger reserves maintain meticulous attendance registries to monitor seasonal tourism flows "
            "and protect delicate forest habitats from overcrowding. Consider visitor records from Kaziranga National Park, celebrated "
            "globally for its magnificent one-horned rhinoceroses. During the festive month of December, the park welcomed eight thousand "
            "four hundred twenty-six visitors. In the cooler month of January, attendance surged to nine thousand one hundred fifteen "
            "visitors. How many additional tourists explored the park in January compared to December? To find this difference, we subtract "
            "eight thousand four hundred twenty-six from nine thousand one hundred fifteen. In the ones place, five minus six requires "
            "borrowing one ten: fifteen minus six equals nine ones. In the tens place, zero tens minus two tens requires unbundling one "
            "hundred: ten tens minus two tens equals eight tens. In the hundreds place, zero hundreds minus four hundreds requires unbundling "
            "one thousand: ten hundreds minus four hundreds equals six hundreds. Finally, eight thousands minus eight thousands leaves zero! "
            "The difference is exactly six hundred eighty-nine visitors. Comparing seasonal park attendance allows forestry authorities "
            "to allocate security rangers, schedule safari jeeps responsibly, manage eco-tourism facilities sustainably, and ensure visitors "
            "experience nature safely without disturbing resting wild fauna across protected sanctums."
        ),
        "checkpoints": [
            {
                "q": "How many more visitors came in January (9,115) than December (8,426)?",
                "options": ["589 visitors", "679 visitors", "689 visitors", "711 visitors"],
                "ans": 2,
                "exp": "9,115 - 8,426 = 689 visitors."
            },
            {
                "q": "Why do forest rangers track visitor numbers using precise multi-digit subtraction?",
                "options": ["To buy more tourist binoculars", "To manage safari jeeps and safeguard forest wildlife", "To feed wild animals", "To close roads forever"],
                "ans": 1,
                "exp": "Tracking tourist attendance helps park rangers deploy resources sustainably and protect animal habitats."
            }
        ]
    },
    {
        "id": 11,
        "title": "Production Vehicle Counts",
        "section": "Industrial Manufacturing & Fleet Registrations",
        "speech": (
            "Multi-digit addition and subtraction govern practical operations across modern manufacturing plants and municipal "
            "transportation departments. Consider a cooperative fruit beverage factory producing pure bottled juices from regional harvests. "
            "In a single working shift, the bottling line produces three thousand four hundred fifty bottles of pineapple juice, two "
            "thousand eight hundred seventy bottles of guava nectar, and one thousand six hundred eighty bottles of passion fruit juice. "
            "What is the total beverage production? Aligning these three quantities in vertical columns, we add the ones: zero plus zero plus "
            "zero gives zero ones. In the tens column, five plus seven plus eight equals twenty tens, writing zero and carrying two hundreds! "
            "In the hundreds column, two plus four plus eight plus six equals twenty hundreds, writing zero and carrying two thousands! In the "
            "thousands column, two plus three plus two plus one equals eight thousands, yielding exactly eight thousand bottles produced! In "
            "another civic department, transport officials audit registered motor vehicles across a district: four thousand five hundred "
            "sixty jeeps, two thousand three hundred forty tractors, and one thousand ninety taxis. Adding and subtracting vehicle registries "
            "enables municipal planners to assess fuel logistics, design road expansions, and optimize public transportation routes effectively."
        ),
        "checkpoints": [
            {
                "q": "What is 3,450 + 2,870 + 1,680 juice bottles combined?",
                "options": ["7,800 bottles", "7,900 bottles", "8,000 bottles", "8,100 bottles"],
                "ans": 2,
                "exp": "3,450 + 2,870 + 1,680 = 8,000 bottles."
            },
            {
                "q": "A district registers 4,560 jeeps and 2,340 tractors. How many vehicles are these two types together?",
                "options": ["6,800", "6,900", "7,000", "7,100"],
                "ans": 1,
                "exp": "4,560 + 2,340 = 6,900 vehicles."
            }
        ]
    },
    {
        "id": 12,
        "title": "Bank Deposit Slips",
        "section": "Financial Denominations & Cash Breakdown",
        "speech": (
            "During a vibrant school community mela, student organizers manage financial accounts by depositing collected stall "
            "earnings into the local school savings bank. Filling out an authentic bank deposit slip requires translating a grand total "
            "into specific currency note denominations: five-hundred-rupee notes, one-hundred-rupee notes, fifty-rupee notes, ten-rupee "
            "notes, and coins. Suppose an industrious young depositor visits the bank counter with an official cash total of two thousand "
            "eight hundred fifty rupees. How is this amount broken down accurately on the deposit slip? Five five-hundred-rupee notes equal "
            "two thousand five hundred rupees. Three one-hundred-rupee notes equal three hundred rupees, bringing our subtotal to two "
            "thousand eight hundred. Finally, one fifty-rupee note supplies the remaining fifty rupees! On the official deposit slip table, "
            "the young saver writes: five under five-hundreds, three under hundreds, one under fifties, and verifies that the sum of all "
            "individual products equals two thousand eight hundred fifty rupees. Another organized student depositor deposits one thousand "
            "four hundred twenty rupees using two five-hundred-rupee notes, four one-hundred-rupee notes, and two ten-rupee notes. Financial "
            "mathematics bridges abstract place-value columns with physical currency banknotes, instilling meticulous accounting accuracy, "
            "verifying transaction integrity, and preparing young minds for responsible personal financial management throughout adulthood."
        ),
        "checkpoints": [
            {
                "q": "Which combination of currency notes equals exactly ₹2,850?",
                "options": ["5 × ₹500 + 3 × ₹100 + 1 × ₹50", "4 × ₹500 + 8 × ₹100 + 1 × ₹50", "6 × ₹500", "2 × ₹500 + 18 × ₹100"],
                "ans": 0,
                "exp": "(5 × 500 = 2500) + (3 × 100 = 300) + (1 × 50 = 50) = ₹2,850."
            },
            {
                "q": "If a student deposits two ₹500 notes, four ₹100 notes, and two ₹10 notes, what is the total deposit?",
                "options": ["₹1,240", "₹1,320", "₹1,420", "₹1,500"],
                "ans": 2,
                "exp": "(2 × 500 = 1000) + (4 × 100 = 400) + (2 × 10 = 20) = ₹1,420."
            }
        ]
    },
    {
        "id": 13,
        "title": "Four Digit Columns",
        "section": "Standard Multi-Digit Operational Algorithms",
        "speech": (
            "Mastering standard column addition and subtraction across four-digit numbers builds speed, structural accuracy, "
            "and computational confidence. Let us practice formal column calculation with multiple regroupings. Consider the addition "
            "problem: four thousand seven hundred eighty-six plus three thousand eight hundred forty-seven. Aligning columns meticulously, "
            "we begin with the ones: six plus seven equals thirteen, writing three and carrying one ten. In the tens column, one plus "
            "eight plus four equals thirteen tens, writing three and carrying one hundred. In the hundreds column, one plus seven plus "
            "eight equals sixteen hundreds, writing six and carrying one thousand. Finally, in the thousands column, one plus four plus "
            "three equals eight thousands, producing eight thousand six hundred thirty-three! Now let us practice four-digit subtraction: "
            "seven thousand two hundred fifteen minus three thousand six hundred forty-eight. In the ones place, fifteen minus eight equals "
            "seven. In the tens place, zero tens minus four tens requires borrowing, giving ten minus four equaling six. In the hundreds "
            "place, one hundred minus six hundreds requires borrowing from thousands, giving eleven minus six equaling five. Finally, six "
            "thousands minus three thousands leaves three, yielding three thousand five hundred sixty-seven! Daily practice of standard algorithms "
            "cements operational fluency across mathematics."
        ),
        "checkpoints": [
            {
                "q": "What is 4,786 + 3,847 calculated column by column?",
                "options": ["8,533", "8,623", "8,633", "8,733"],
                "ans": 2,
                "exp": "4,786 + 3,847 = 8,633."
            },
            {
                "q": "What is 7,215 - 3,648 calculated using standard column subtraction?",
                "options": ["3,557", "3,567", "3,667", "4,567"],
                "ans": 1,
                "exp": "7,215 - 3,648 = 3,567."
            }
        ]
    },
    {
        "id": 14,
        "title": "Mental Math Strategies",
        "section": "Compensation Tricks & Near-Hundred Adjustments",
        "speech": (
            "While standard paper algorithms provide dependable precision, ingenious mental math shortcuts allow us to calculate large "
            "sums and differences in mere seconds without using pencil and paper! The most celebrated mental strategy is compensation, which "
            "utilizes friendly landmark numbers like one hundred or one thousand. Suppose we must calculate five hundred forty-six minus "
            "ninety-nine. Instead of tedious column borrowing, notice that ninety-nine is just one less than one hundred! We subtract one "
            "hundred first: five hundred forty-six minus one hundred equals four hundred forty-six. Since we subtracted one unit too many, "
            "we simply add one back: four hundred forty-six plus one equals four hundred forty-seven! What if we need to add ninety-nine "
            "instead? To calculate three hundred seventy-two plus ninety-nine, add one hundred first to reach four hundred seventy-two, then "
            "subtract one to obtain four hundred seventy-one! The same compensation logic applies to nine hundred ninety-nine: to subtract "
            "nine hundred ninety-nine, subtract one thousand and add one! Similarly, to add nine hundred ninety-nine, add one thousand and "
            "subtract one! Mastering these practical compensation methods transforms cumbersome multi-digit arithmetic into joyful mental agility, "
            "proving that understanding number relationships makes computation effortless, fast, and remarkably satisfying across everyday real-world problem-solving situations."
        ),
        "checkpoints": [
            {
                "q": "How can you mentally compute 546 - 99 using compensation?",
                "options": ["Subtract 100 then add 1 (546 - 100 + 1 = 447)", "Subtract 90 then subtract 9", "Add 100 then subtract 1", "Divide by 99"],
                "ans": 0,
                "exp": "546 - 100 = 446; 446 + 1 = 447."
            },
            {
                "q": "What is 372 + 99 calculated mentally?",
                "options": ["461", "471", "472", "481"],
                "ans": 1,
                "exp": "372 + 100 = 472; 472 - 1 = 471."
            }
        ]
    },
    {
        "id": 15,
        "title": "Inequality Logic Puzzles",
        "section": "Expression Comparison & Relational Thinking",
        "speech": (
            "Expert mathematicians frequently compare the values of two arithmetic expressions without calculating their exact sums "
            "or differences. This profound skill, known as relational thinking, relies on comparing corresponding terms directly. For "
            "example, consider comparing the expression two thousand four hundred fifty plus three hundred twenty against two thousand four "
            "hundred fifty plus three hundred ten. Notice that both expressions contain the common term two thousand four hundred fifty! "
            "Because three hundred twenty is greater than three hundred ten, the first expression must be strictly greater than the second, "
            "allowing us to place the greater-than symbol immediately without performing addition! What about comparing differences? Consider "
            "four thousand five hundred minus two hundred against four thousand five hundred minus two hundred fifty. When subtracting from "
            "identical totals, removing a smaller amount leaves a noticeably larger remainder! Since two hundred is clearly smaller than two "
            "hundred fifty, subtracting two hundred leaves a larger balance behind, making four thousand five hundred minus two hundred "
            "greater! This logical relational comparison replaces brute-force calculation with keen structural deduction, enabling observant "
            "young scholars to analyze algebraic inequalities, verify commercial invoice estimates, and solve mathematical reasoning puzzles with "
            "speed, elegance, and profound confidence across diverse academic disciplines."
        ),
        "checkpoints": [
            {
                "q": "Which symbol correctly compares 2,450 + 320 ___ 2,450 + 310 without adding?",
                "options": ["<", "=", ">", "Cannot tell"],
                "ans": 2,
                "exp": "Both expressions share 2,450. Since 320 > 310, the left side is strictly greater (>)."
            },
            {
                "q": "Which expression is larger: (4,500 - 200) or (4,500 - 250)?",
                "options": ["4,500 - 200 is larger", "4,500 - 250 is larger", "Both are equal", "Cannot be compared"],
                "ans": 0,
                "exp": "Subtracting a smaller number (200 < 250) leaves a larger result: 4,300 > 4,250."
            }
        ]
    },
    {
        "id": 16,
        "title": "Neighbouring Square Grids",
        "section": "Grid Parity Puzzles & Combinatorial Logic",
        "speech": (
            "We conclude our chapter with an ingenious combinatorial logic puzzle known as the neighbouring square grid! In "
            "a three-by-three grid containing nine square cells, a mathematician must place the digits one through nine, using each digit "
            "exactly once, such that the difference between any two adjacent, connected squares is always an odd number. Let us analyze the "
            "parity rules governing differences! The difference between two numbers is odd if and only if one number is even and the other "
            "number is odd: an even minus an odd, or an odd minus an even, always produces an odd difference. Conversely, the difference "
            "between two even numbers, or between two odd numbers, is always an even number! Therefore, for every adjacent pair of squares "
            "to have an odd difference, every even square must be bordered exclusively by odd squares, and every odd square must be bordered "
            "exclusively by even squares! This produces an alternating chessboard pattern. Counting our available digits, from one to nine "
            "there are five odd numbers (one, three, five, seven, nine) and four even numbers (two, four, six, eight). Placing the five odd "
            "digits on the corners and center, and the four even digits on the edges, solves the puzzle flawlessly!"
        ),
        "checkpoints": [
            {
                "q": "When is the difference between two numbers an ODD number?",
                "options": ["When both are even", "When both are odd", "When one is even and the other is odd", "Never"],
                "ans": 2,
                "exp": "Even - Odd = Odd, and Odd - Even = Odd. Differing parity always produces an odd difference."
            },
            {
                "q": "How many odd digits and even digits are there in the numbers 1 through 9?",
                "options": ["4 odd, 5 even", "5 odd, 4 even", "3 odd, 6 even", "5 odd, 5 even"],
                "ans": 1,
                "exp": "Odd digits: 1, 3, 5, 7, 9 (5 digits). Even digits: 2, 4, 6, 8 (4 digits)."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(slides_part2)} slides for Part 2.")
    for s in slides_part2:
        wc = len(s["speech"].split())
        print(f"Slide {s['id']}: {s['title']} -> {wc} words (Title: {len(s['title'].split())} words)")
        assert 195 <= wc <= 215, f"Word count {wc} out of bounds for slide {s['id']}!"
        assert 1 <= len(s['title'].split()) <= 3, f"Title length out of bounds for slide {s['id']}!"
