# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 10: Elephants, Tigers, and Leopards
Part 1: Slides 1 to 8 Data Generator
Strictly 195 to 215 words per speech lecture.
Zero human names (Raju, Rani, Roja, Raghav, etc. replaced with generic roles).
Clean Unicode throughout (₹, ×, ÷, +, -, =).
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Nim Addition Strategy",
        "section": "Two-Player Strategic Running Sums",
        "speech": (
            "Welcome young scholars to an exhilarating mathematical journey into numbers, wildlife data, and strategic "
            "game theory! We begin our exploration with a classic two-player strategy game known as the Nim addition game. "
            "Two players alternate turns adding either one or two to a shared running total, starting at zero. The player who "
            "first reaches the exact target number of ten wins the game! Let us observe a sample match. The first player calls out "
            "two, setting the total to two. The second player adds one, bringing the total to three. The first player adds two, making "
            "it five. The second player adds two, raising the total to seven! Now consider the first player's dilemma: adding one makes "
            "eight, allowing the second player to add two and reach ten; adding two makes nine, allowing the second player to add one "
            "and reach ten! Whichever move the first player chooses from seven, the second player claims the victory. This game proves "
            "that arithmetic is not just mechanical calculation; it involves forward planning, backward deduction, and controlling critical "
            "numerical thresholds. Understanding how smaller additions accumulate toward a target unlocks strategic thinking, transforming "
            "simple addition into an exciting intellectual contest of wit and mathematical foresight."
        ),
        "checkpoints": [
            {
                "q": "In the target-10 Nim addition game, what are the allowed numbers a player can add on their turn?",
                "options": ["1 or 2", "1, 2, or 3", "Any number up to 5", "Only 2"],
                "ans": 0,
                "exp": "Each player can only add either 1 or 2 to the running total."
            },
            {
                "q": "If the running total is 7, can the next player reach 10 on that immediate turn?",
                "options": ["Yes, by adding 3", "No, max addition is 2 (reaches 9)", "Yes, by adding 1", "Game is tied"],
                "ans": 1,
                "exp": "The maximum allowed addition is 2, which only reaches 7 + 2 = 9."
            }
        ]
    },
    {
        "id": 2,
        "title": "Winning Position Analysis",
        "section": "Backward Induction & Modulo 3 Invariants",
        "speech": (
            "To consistently master the Nim addition game, mathematicians utilize backward reasoning to identify winning "
            "and losing positions. If our ultimate goal is to say ten, what number must we reach on the turn before? The answer is "
            "seven! From seven, if your opponent adds one to reach eight, you add two to claim ten; if your opponent adds two to reach "
            "nine, you add one to claim ten. Therefore, reaching seven guarantees victory! Now we ask: what prior milestone guarantees "
            "reaching seven? By subtracting three, we discover that controlling four ensures victory! From four, if the opponent adds "
            "one to make five, you add two to reach seven; if they add two to make six, you add one to reach seven. Working backward one "
            "step further, subtracting three from four yields one. If the first player begins by calling one, and subsequently claims "
            "four, seven, and ten, they can never be defeated! The sequence one, four, seven, and ten represents the invariant winning "
            "positions, differing by three on every step. Backward induction teaches us to begin with the desired outcome and trace logical "
            "steps backward, a profound problem-solving principle applied across computer science, economics, logistics, and competitive mathematical games."
        ),
        "checkpoints": [
            {
                "q": "What is the key winning threshold number right before target 10?",
                "options": ["6", "7", "8", "9"],
                "ans": 1,
                "exp": "Controlling 7 guarantees winning 10, because 7 + 1 = 8 (add 2) and 7 + 2 = 9 (add 1)."
            },
            {
                "q": "What is the complete sequence of winning milestones in target-10 Nim?",
                "options": ["2, 4, 6, 8, 10", "1, 4, 7, 10", "3, 6, 9, 10", "1, 3, 5, 7, 10"],
                "ans": 1,
                "exp": "The winning positions differ by 3: 1, 4, 7, and 10."
            }
        ]
    },
    {
        "id": 3,
        "title": "Addition Chart Patterns",
        "section": "13×13 Grid Explorations & Sum Frequencies",
        "speech": (
            "Now let us examine an expansive addition chart spanning thirteen rows and thirteen columns, representing all "
            "sums of whole numbers from zero through twelve. Constructing this comprehensive grid reveals an astonishing tapestry of "
            "symmetry, repeating patterns, and frequency distributions. Notice the diagonals running from bottom-left to top-right: "
            "every cell along a single diagonal displays the exact same sum! For example, the number nine appears across ten distinct "
            "cells: zero plus nine, one plus eight, two plus seven, three plus six, four plus five, five plus four, six plus three, "
            "seven plus two, eight plus one, and nine plus zero. The frequency of each sum increases steadily from zero up to twelve, "
            "reaching its maximum frequency at twelve with thirteen occurrences, and then decreases symmetrically down to twenty-four. "
            "Investigating row and column parity reveals further order: even rows alternate between even and odd sums, while adding two "
            "even numbers always yields an even sum. Exploring addition charts shifts computational thinking from isolated addition "
            "drills into holistic structural understanding. Recognizing how numbers partition into diverse addends deepens mental flexibility, "
            "strengthens number bonds, and forms the mathematical bedrock for algebraic decomposition and combinatorial probability analysis across advanced branches of science and mathematics."
        ),
        "checkpoints": [
            {
                "q": "Along which direction on an addition chart are all numbers identical?",
                "options": ["Vertical columns", "Horizontal rows", "Bottom-left to top-right diagonals", "Main diagonal"],
                "ans": 2,
                "exp": "Diagonals sloping from bottom-left to top-right contain identical sums (e.g., all 9s)."
            },
            {
                "q": "How many different addition pairs on the 0-12 grid sum to exactly 9?",
                "options": ["8 pairs", "9 pairs", "10 pairs", "12 pairs"],
                "ans": 2,
                "exp": "From 0+9 to 9+0, there are exactly 10 pairs totaling 9."
            }
        ]
    },
    {
        "id": 4,
        "title": "Window Frame Sums",
        "section": "Sub-Grid Magic & Centroid Multiples",
        "speech": (
            "Within our grand thirteen-by-thirteen addition chart, placing a highlighted three-by-three window frame reveals "
            "a delightful hidden relationship known as the centroid multiple theorem. Suppose we frame nine adjacent cells centered "
            "on the number ten. The middle row reads nine, ten, and eleven. The top row reads eight, nine, and ten, while the bottom "
            "row reads ten, eleven, and twelve. Let us compute the sums across various directions! The horizontal middle row sums to "
            "nine plus ten plus eleven, equaling thirty. The vertical central column sums to nine plus ten plus eleven, which also equals "
            "thirty! Now look at the diagonals: eight plus ten plus twelve equals thirty, and ten plus ten plus ten equals thirty! Every "
            "line passing through the central cell sums to exactly three times the central number! Furthermore, adding all nine numbers "
            "within the window frame yields exactly ninety, which is nine times the central number ten! This remarkable property holds "
            "true wherever the three-by-three frame is placed on the chart. Window frame puzzles illuminate spatial balance, prove that "
            "arithmetic sequences balance around their midpoint, and demonstrate how geometric symmetry governs numerical structures across matrices, computational grids, and algebraic number patterns throughout our world."
        ),
        "checkpoints": [
            {
                "q": "In a 3×3 window on the addition chart with center 10, what is the sum of any line passing through the center?",
                "options": ["20", "25", "30", "40"],
                "ans": 2,
                "exp": "Each line of 3 numbers equals 3 × central number = 3 × 10 = 30."
            },
            {
                "q": "What is the sum of all 9 numbers in a 3×3 window with central number 10?",
                "options": ["60", "80", "90", "100"],
                "ans": 2,
                "exp": "Total sum = 9 × central number = 9 × 10 = 90."
            }
        ]
    },
    {
        "id": 5,
        "title": "Reverse And Add",
        "section": "Digit Palindromes & Multiples of Eleven",
        "speech": (
            "A fascinating arithmetic pattern emerges when we take two-digit numbers, reverse their digits, and add the two "
            "values together. Suppose we select the number twenty-seven. Reversing its digits yields seventy-two. Adding twenty-seven "
            "and seventy-two produces ninety-nine! What if we select thirty-four? Its reverse is forty-three, and thirty-four plus forty-three "
            "equals seventy-seven! Notice something extraordinary about all these sums: ninety-nine, seventy-seven, fifty-five, and eighty-eight "
            "are all multiples of eleven! Why does this always occur? Let us examine the algebra of place value. Any two-digit number "
            "consisting of tens digit A and ones digit B equals ten A plus B. Its reverse equals ten B plus A. Adding them produces eleven A "
            "plus eleven B, which factors into eleven times the sum of A and B! Therefore, reversing and adding any two-digit number always "
            "generates an exact multiple of eleven. If the sum of the digits exceeds nine, the result produces a three-digit multiple: for "
            "instance, eighty-four plus forty-eight equals one hundred thirty-two, which equals eleven times twelve! Reverse-and-add patterns "
            "demystify place value mechanics, reveal beautiful algebraic palindromes, and show how underlying decimal structures produce elegant invariants, fostering deep mathematical curiosity, confidence, and deep mathematical joy, and lifelong numerical appreciation."
        ),
        "checkpoints": [
            {
                "q": "What do you get when you reverse and add 27 (27 + 72)?",
                "options": ["89", "99", "109", "110"],
                "ans": 1,
                "exp": "27 + 72 = 99."
            },
            {
                "q": "The sum of any 2-digit number and its reverse is always an exact multiple of which number?",
                "options": ["9", "10", "11", "12"],
                "ans": 2,
                "exp": "(10a + b) + (10b + a) = 11(a + b), which is always a multiple of 11."
            }
        ]
    },
    {
        "id": 6,
        "title": "Wildlife Census Data",
        "section": "Biodiversity Conservation & Large Figures",
        "speech": (
            "Mathematics serves as an indispensable tool for environmental science, particularly when tracking endangered "
            "wildlife populations across India's magnificent national parks and forest reserves. Wildlife biologists conduct comprehensive "
            "census surveys to monitor majestic apex species including Asian elephants, royal Bengal tigers, and Indian leopards. These "
            "census reports present large four-digit numbers requiring precise quantitative analysis. According to national survey records, "
            "the elephant population in Karnataka stands at approximately six thousand forty-nine, while neighboring Kerala shelters three "
            "thousand fifty-four elephants. Meanwhile, India's tiger population has rebounded remarkably, with Madhya Pradesh recording "
            "seven hundred eighty-five tigers and Uttarakhand recording five hundred sixty tigers. For leopards, central and southern "
            "states shelter robust numbers, with Karnataka hosting nearly three thousand nine hundred leopards and Madhya Pradesh hosting "
            "over three thousand nine hundred. Analyzing wildlife census data connects mathematical learning with conservation stewardship. "
            "By comparing, adding, and subtracting real-world population metrics, young scholars appreciate how mathematics empowers forestry "
            "officials to safeguard delicate ecosystems, prevent habitat fragmentation, and ensure that our nation's rich biodiversity thrives "
            "for future generations to cherish, establishing sustainable wildlife reserves, comprehensive census databases, active animal tracking, and rigorous ecological protection policies safely across our magnificent, biologically diverse nation."
        ),
        "checkpoints": [
            {
                "q": "Which state hosts over 6,000 Asian elephants according to national wildlife census records?",
                "options": ["Goa", "Karnataka", "Punjab", "Haryana"],
                "ans": 1,
                "exp": "Karnataka hosts approximately 6,049 Asian elephants, the highest in the southern corridor."
            },
            {
                "q": "Why do wildlife scientists rely on accurate multi-digit arithmetic?",
                "options": ["To design animal cages", "To monitor endangered populations and protect habitats", "To guess forest trees", "To paint tigers"],
                "ans": 1,
                "exp": "Accurate census counts help conservationists monitor population trends and protect natural habitats."
            }
        ]
    },
    {
        "id": 7,
        "title": "Place Value Addition",
        "section": "Thousands Regrouping & Concrete Tokens",
        "speech": (
            "When combining large four-digit populations, we employ the standard column addition algorithm supported by "
            "concrete place-value tokens. Imagine representing numbers using color-coded tokens: yellow thousand cubes, green hundred "
            "flats, blue ten rods, and red one units. Let us calculate the combined elephant population of Karnataka and Kerala by adding "
            "six thousand forty-nine and three thousand fifty-four. We align the two quantities meticulously by place value columns: "
            "Thousands, Hundreds, Tens, and Ones. Starting in the ones column, nine plus four equals thirteen. Thirteen ones cannot remain "
            "in the ones column, so we regroup ten ones into one ten rod, leaving three units and carrying one ten to the tens column! "
            "In the tens column, our carried one plus four plus five equals ten tens. Regrouping ten tens creates one hundred flat, leaving "
            "zero in the tens place and carrying one to the hundreds column! In the hundreds column, one plus zero plus zero equals one. "
            "Finally, in the thousands column, six plus three equals nine thousands. Combining our columns yields nine thousand one hundred "
            "three elephants! Regrouping tokens provides an unshakeable conceptual foundation, demonstrating that column carries are physical "
            "re-bundlings in our base-ten decimal place-value system."
        ),
        "checkpoints": [
            {
                "q": "What is 6,049 + 3,054 calculated column by column?",
                "options": ["9,093", "9,103", "9,113", "9,203"],
                "ans": 1,
                "exp": "6,049 + 3,054 = 9,103 (with regrouping in ones and tens columns)."
            },
            {
                "q": "What happens when 10 ones units are bundled together?",
                "options": ["They disappear", "They regroup into 1 ten rod", "They become 100", "They form a thousand"],
                "ans": 1,
                "exp": "In base-ten place value, 10 ones regroup into 1 ten rod."
            }
        ]
    },
    {
        "id": 8,
        "title": "Tiger Population Word",
        "section": "Multi-State Comparisons & Two-Step Sums",
        "speech": (
            "Let us apply our multi-digit addition skills to solve compelling comparative word problems about regional tiger "
            "populations. Suppose national census records report that Maharashtra shelters four hundred forty-four wild tigers. In "
            "Uttarakhand, the tiger population exceeds Maharashtra's count by one hundred sixteen tigers. In Madhya Pradesh, the "
            "tiger population exceeds Maharashtra's count by three hundred forty-one tigers. How many tigers inhabit Madhya Pradesh and "
            "Uttarakhand combined? To solve this two-step inquiry, we first determine each state's individual total. For Uttarakhand, "
            "four hundred forty-four plus one hundred sixteen equals five hundred sixty tigers. For Madhya Pradesh, four hundred forty-four "
            "plus three hundred forty-one equals seven hundred eighty-five tigers! Now, we sum the two regional populations: five hundred "
            "sixty plus seven hundred eighty-five. Adding column by column, zero plus five gives five ones; six plus eight gives fourteen "
            "tens, carrying one hundred; and one plus five plus seven gives thirteen hundreds! The grand total is one thousand three hundred "
            "forty-five tigers! Methodically translating word descriptions into sequential addition sentences prevents confusion, trains "
            "analytical thinking, and provides clear quantitative answers for complex ecological conservation reports, regional forestry assessments, and governmental biodiversity management plans across all conservation areas throughout our nation."
        ),
        "checkpoints": [
            {
                "q": "If Maharashtra has 444 tigers and Uttarakhand has 116 more, how many tigers are in Uttarakhand?",
                "options": ["540 tigers", "550 tigers", "560 tigers", "570 tigers"],
                "ans": 2,
                "exp": "444 + 116 = 560 tigers."
            },
            {
                "q": "What is the combined tiger population of Uttarakhand (560) and Madhya Pradesh (785)?",
                "options": ["1,245", "1,345", "1,355", "1,445"],
                "ans": 1,
                "exp": "560 + 785 = 1,345 tigers."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(slides_part1)} slides for Part 1.")
    for s in slides_part1:
        wc = len(s["speech"].split())
        print(f"Slide {s['id']}: {s['title']} -> {wc} words (Title: {len(s['title'].split())} words)")
        assert 195 <= wc <= 215, f"Word count {wc} out of bounds for slide {s['id']}!"
        assert 1 <= len(s['title'].split()) <= 3, f"Title length out of bounds for slide {s['id']}!"
