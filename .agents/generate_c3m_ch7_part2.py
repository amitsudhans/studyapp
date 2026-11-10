#!/usr/bin/env python3
"""
Slide Data Generator for NCERT Class 3 Mathematics - Chapter 7: Raksha Bandhan
Part 2: Slides 9 to 16
Strictly 195 - 215 words per spoken text.
1-3 word titles.
No human names (Gopal, Dhara, Atya, Jagannath, Mithu, Dhruv, Roro, Toto, etc. removed/generalized).
No teacher personas.
"""

import json

slides_part2 = [
    {
        "id": 9,
        "title": "Array Commutative Law",
        "subtitle": "Discovering that changing multiplication order preserves the identical product",
        "speech": (
            "Step into a sunlit botanical garden where blooming flower beds reveal an extraordinary mathematical secret. "
            "Observe an organized flower bed where saplings are planted in an orderly rectangular grid. "
            "If you stand at the front end, you see eight long rows with six blooming marigolds in each row. "
            "To calculate the total flowers, you compute eight times six, which equals forty-eight blossoms. "
            "Now walk around to the side of the garden bed and view the exact same plants from a different angle. "
            "From your new vantage point, you observe six horizontal rows with eight marigolds in each row. "
            "Calculating the total now gives six times eight, which also equals forty-eight blossoms! "
            "Even though our visual perspective shifted, the actual number of plants in the bed did not change by a single petal. "
            "This fundamental mathematical truth is called the commutative property of multiplication. "
            "It states that for any two numbers, changing the order of the factors never changes the final product: eight times six is always identical to six times eight. "
            "Representing groups on dot grids makes this symmetry crystal clear, whether viewing rows or columns. "
            "Use the garden array simulator to rotate grids and witness the commutative property visually."
        ),
        "checkpoints": [
            {
                "question": "According to the commutative property, if 4 × 7 = 28, what does 7 × 4 equal?",
                "options": ["24", "28", "32", "35"],
                "answer": 1,
                "hint": "Swapping the order of factors does not change the product.",
                "explanation": "Because multiplication is commutative, 7 × 4 produces the exact same product as 4 × 7, which is 28."
            },
            {
                "question": "How many total plants are in a garden bed of 5 rows with 9 plants in each row?",
                "options": ["40 plants", "45 plants", "50 plants", "54 plants"],
                "answer": 1,
                "hint": "Multiply 5 by 9 (or 9 by 5): 5 × 9.",
                "explanation": "Five rows of 9 plants equal 5 × 9 = 45 total plants."
            }
        ]
    },
    {
        "id": 10,
        "title": "Chicks Times Two",
        "subtitle": "Constructing the foundational times-two multiplication table using pairs of chicks",
        "speech": (
            "Imagine visiting a lively farm where fluffy little chicks hop around happily in cheerful, adorable pairs. "
            "Every single pair consists of exactly two baby chicks following each other across the lush green grass. "
            "We can use these adorable pairs to build the foundational two-times multiplication table step by step. "
            "When one pair hops past, we have one group of two: one times two equals two chicks. "
            "When a second pair joins in, we have two groups of two: two times two equals four chicks. "
            "With three pairs, we count three groups of two: three times two equals six chicks altogether. "
            "As each new pair enters the farmyard, the total chick count increases by two: eight, ten, twelve, fourteen, sixteen, eighteen, and finally twenty chicks for ten pairs. "
            "Notice how the two-times table is constructed by adding two repeatedly to each previous result in orderly steps. "
            "Every product in the two-times table ends in an even digit: zero, two, four, six, or eight. "
            "This table serves as our prime launching pad for understanding how all multiplication tables are built through equal incremental steps. "
            "Interact with the farmyard chicks simulator to assemble pairs and watch the times-two table generate dynamically."
        ),
        "checkpoints": [
            {
                "question": "What is the total number of chicks in 7 pairs of chicks?",
                "options": ["12 chicks", "14 chicks", "16 chicks", "18 chicks"],
                "answer": 1,
                "hint": "Multiply 7 pairs by 2 chicks per pair: 7 × 2.",
                "explanation": "Seven pairs of chicks equal 7 × 2 = 14 chicks in total."
            },
            {
                "question": "Every product in the 2-times table always ends in which kind of digit?",
                "options": ["An odd digit (1, 3, 5, 7, 9)", "An even digit (0, 2, 4, 6, 8)", "Only the digit zero", "Only the digit five"],
                "answer": 1,
                "hint": "Multiples of 2 are always even numbers.",
                "explanation": "Every product in the 2-times table is an even number, ending in 0, 2, 4, 6, or 8."
            }
        ]
    },
    {
        "id": 11,
        "title": "Skip Jump Tracks",
        "subtitle": "Hopping along winding number tracks to master multiples of three",
        "speech": (
            "Outdoor games make arithmetic an energetic adventure on winding chalk tracks drawn across the schoolyard ground. "
            "Imagine a numbered track starting at zero and winding smoothly past thirty with clearly marked circular stepping stones. "
            "A lively jumping game begins where a player must always leap forward by exactly three stones on every single jump. "
            "The player starts at zero. On the first leap of three, the player lands squarely on stone three: one times three equals three. "
            "On the second leap, the player advances three more stones and lands on stone six: two times three equals six. "
            "The third leap carries the player to stone nine, the fourth to twelve, and the fifth to fifteen stones. "
            "Continuing this rhythmic cadence of three-stone leaps produces the sequence: eighteen, twenty-one, twenty-four, twenty-seven, and thirty. "
            "Notice how each landing spot on the track matches an exact step of the three-times multiplication table. "
            "Skip jumping connects spatial movement directly with repeated addition and multiplication equations in everyday math. "
            "You can predict any landing position simply by multiplying the jump count by the jump length of three. "
            "Guide the interactive hopper along the curvy track to trace leap trajectories and master multiples of three."
        ),
        "checkpoints": [
            {
                "question": "If you take 6 jumps of 3 steps each starting from 0, on which number stone do you land?",
                "options": ["15", "18", "21", "24"],
                "answer": 1,
                "hint": "Multiply 6 jumps by 3 steps: 6 × 3.",
                "explanation": "Six jumps of 3 steps lead to 6 × 3 = 18."
            },
            {
                "question": "Starting at 0, how many jumps of 3 are required to reach the target stone 27?",
                "options": ["7 jumps", "8 jumps", "9 jumps", "10 jumps"],
                "answer": 2,
                "hint": "Divide 27 by 3: 27 ÷ 3.",
                "explanation": "Since 9 × 3 = 27, exactly 9 leaps of 3 steps are needed to reach 27."
            }
        ]
    },
    {
        "id": 12,
        "title": "Multiplication Track Jumps",
        "subtitle": "Constructing four-times and six-times tables through multi-step jumping challenges",
        "speech": (
            "Having mastered three-step hops, we can expand our number track to construct higher multiplication tables with equal confidence. "
            "Imagine extending our jumping track to test strides of four steps and strides of six steps across the yard. "
            "When we leap by fours, the sequence of footprints traces the four-times table: four, eight, twelve, sixteen, twenty, twenty-four, twenty-eight, thirty-two, thirty-six, and forty. "
            "Each jump lands on a multiple of four, matching the formula: number of jumps multiplied by four equals the destination stone. "
            "Now test longer strides of six steps per leap. Starting at zero, our first landing is six, followed by twelve, eighteen, twenty-four, thirty, thirty-six, and beyond. "
            "Notice how certain special numbers, like twelve, twenty-four, and thirty-six, are landed upon by both the four-hopper and the six-hopper! "
            "These shared landing stones are common multiples of four and six. "
            "We can also play a minimum-jump target game: if your target is thirty-six, jumping by sixes takes only six leaps, whereas jumping by fours requires nine leaps. "
            "Comparing different jump sizes deepens your strategic number sense and strengthens mental multiplication speed significantly. "
            "Use the dual-track jump simulator to compare leap lengths, race against target markers, and uncover shared multiples."
        ),
        "checkpoints": [
            {
                "question": "How many jumps of 6 are needed to reach stone 42 starting from 0?",
                "options": ["6 jumps", "7 jumps", "8 jumps", "9 jumps"],
                "answer": 1,
                "hint": "Calculate 42 ÷ 6 or find what multiplied by 6 equals 42.",
                "explanation": "Seven jumps of 6 steps reach 7 × 6 = 42."
            },
            {
                "question": "Which of these numbers is landed on by BOTH a 4-step jumper and a 6-step jumper?",
                "options": ["16", "20", "24", "28"],
                "answer": 2,
                "hint": "Check which number is a multiple of both 4 and 6.",
                "explanation": "24 is divisible by both 4 (4 × 6 = 24) and 6 (6 × 4 = 24), making it a shared landing stone."
            }
        ]
    },
    {
        "id": 13,
        "title": "Stick Cross Intersections",
        "subtitle": "Building multiplication tables visually by counting intersection points of overlapping sticks",
        "speech": (
            "Did you know you can construct complete multiplication tables using simple wooden craft sticks without doing any mental addition at all? "
            "This ingenious visual method uses intersecting sticks laid completely flat upon a table surface. "
            "To build the five-times table, lay down five horizontal craft sticks parallel to one another in neat rows. "
            "Now take one vertical stick and place it across all five horizontal sticks. "
            "Look closely where the sticks cross each other: there are five red crossing dots or intersection points: one times five equals five! "
            "Lay down a second vertical stick across the five horizontal sticks. "
            "Counting the new intersection points adds five more dots, giving ten dots in total: two times five equals ten dots. "
            "Adding a third vertical stick yields fifteen dots, a fourth gives twenty dots, and a fifth gives twenty-five dots. "
            "Every additional vertical stick placed creates another row of five intersections. "
            "This geometric method turns abstract numbers into tangible, countable physical points. "
            "You can build any table from times-one to times-ten by simply varying the number of horizontal and vertical crossing sticks. "
            "Interact with the digital stick intersection simulator to place sticks, count crossing nodes, and construct multiplication tables interactively."
        ),
        "checkpoints": [
            {
                "question": "If you lay 5 horizontal sticks and cross them with 4 vertical sticks, how many intersection dots are formed?",
                "options": ["15 dots", "20 dots", "24 dots", "25 dots"],
                "answer": 1,
                "hint": "Multiply the number of horizontal sticks by vertical sticks: 5 × 4.",
                "explanation": "Five horizontal sticks crossed by 4 vertical sticks produce 5 × 4 = 20 intersection points."
            },
            {
                "question": "How many vertical sticks must cross 6 horizontal sticks to produce 42 intersection dots?",
                "options": ["6 sticks", "7 sticks", "8 sticks", "9 sticks"],
                "answer": 1,
                "hint": "Find what number multiplied by 6 gives 42: 42 ÷ 6.",
                "explanation": "Since 6 × 7 = 42, exactly 7 vertical sticks are needed."
            }
        ]
    },
    {
        "id": 14,
        "title": "Table Addition Patterns",
        "subtitle": "Uncovering digit rhythms and combining smaller tables to form larger tables",
        "speech": (
            "Multiplication tables are not isolated lists of facts; they are filled with beautiful patterns and deeply interconnected mathematical relationships. "
            "Examine the five-times table carefully: five, ten, fifteen, twenty, twenty-five, thirty, thirty-five, forty, forty-five, fifty. "
            "Look at the units digit of every product: it alternates rhythmically between five and zero in an endless, predictable pattern! "
            "Even more wondrous is how different multiplication tables can be combined together using straightforward addition to create completely new tables. "
            "Consider the two-times table and the three-times table side by side. "
            "If we take two times four, which is eight, and add three times four, which is twelve, the sum is eight plus twelve equals twenty. "
            "Notice that twenty is exactly five times four! "
            "Because two plus three equals five, adding the corresponding products of the two-times table and the three-times table gives the complete five-times table. "
            "Similarly, combining the four-times table and the three-times table produces the seven-times table because four plus three equals seven. "
            "This additive property of multiplication allows you to construct challenging higher tables simply by adding familiar, friendly smaller tables together. "
            "Explore the pattern analyzer to visualize alternating digits and blend smaller multiplication tables into composite master tables."
        ),
        "checkpoints": [
            {
                "question": "What pattern do the units digits follow in the 5-times table?",
                "options": ["Always ending in 2 or 4", "Alternating between 5 and 0", "Always ending in 1 or 3", "Increasing by 1 every step"],
                "answer": 1,
                "hint": "Look at the ending digits: 5, 10, 15, 20, 25...",
                "explanation": "The units digits of products in the 5-times table always alternate between 5 and 0."
            },
            {
                "question": "If you add the 3-times table and the 4-times table together, which table do you get?",
                "options": ["The 6-times table", "The 7-times table", "The 8-times table", "The 12-times table"],
                "answer": 1,
                "hint": "Add the base factors: 3 + 4 = 7.",
                "explanation": "Because 3 + 4 = 7, adding corresponding values from the 3-times and 4-times tables produces the 7-times table."
            }
        ]
    },
    {
        "id": 15,
        "title": "Repeated Subtraction Chains",
        "subtitle": "Solving practical large-scale division problems with sea-shells and currency",
        "speech": (
            "Division reveals its full practical power when solving real-world challenges with larger collections of items. "
            "Imagine collecting one hundred and twelve shiny sea-shells along a sunny ocean beach to craft decorative souvenir necklaces. "
            "If each craft necklace requires exactly twenty-eight sea-shells, how many complete necklaces can be assembled? "
            "We can solve this division challenge through repeated subtraction. "
            "Starting with one hundred and twelve shells, subtracting twenty-eight for the first necklace leaves eighty-four shells. "
            "Subtracting twenty-eight for a second necklace leaves fifty-six shells. "
            "A third subtraction of twenty-eight leaves twenty-eight shells, and subtracting twenty-eight for the fourth necklace leaves exactly zero shells. "
            "Because twenty-eight was subtracted four times consecutively, one hundred and twelve divided by twenty-eight equals four necklaces! "
            "We apply the exact same repeated subtraction logic when exchanging currency notes. "
            "If you hold a five-hundred rupee note and wish to exchange it entirely for fifty-rupee notes, you divide five hundred by fifty. "
            "Since fifty times ten equals five hundred, the bank teller hands you exactly ten fifty-rupee notes. "
            "Whether crafting necklaces or managing currency denominations, repeated subtraction provides an unfailing method for solving division problems. "
            "Use the sea-shell and currency simulator to track step-by-step subtraction chains dynamically."
        ),
        "checkpoints": [
            {
                "question": "How many 28-shell necklaces can be made from 112 sea-shells?",
                "options": ["3 necklaces", "4 necklaces", "5 necklaces", "6 necklaces"],
                "answer": 1,
                "hint": "Calculate 112 ÷ 28 or subtract 28 repeatedly until reaching 0.",
                "explanation": "112 - 28 - 28 - 28 - 28 = 0. Subtracting 4 times means 112 ÷ 28 = 4 complete necklaces."
            },
            {
                "question": "How many 50-rupee notes are needed to equal a 500-rupee note?",
                "options": ["5 notes", "8 notes", "10 notes", "20 notes"],
                "answer": 2,
                "hint": "Divide 500 by 50: 500 ÷ 50.",
                "explanation": "Five hundred divided by 50 equals 10, so ten 50-rupee notes equal 500 rupees."
            }
        ]
    },
    {
        "id": 16,
        "title": "Mystery Factor Envelopes",
        "subtitle": "Deducing hidden multiplier pairs to unlock secret product envelopes",
        "speech": (
            "Let us conclude our conceptual journey with an exhilarating mathematical logic puzzle involving mystery product envelopes. "
            "Imagine a set of ten number cards labeled with the digits one through ten placed face up on a puzzle table. "
            "Before us sit several sealed envelopes, each stamped on the outside with a target product value. "
            "Our challenge is to find which two number cards from our deck multiply together to equal the target value printed on each envelope. "
            "Suppose an envelope is stamped with the product thirty-two. "
            "We examine our cards and search for two numbers whose product is thirty-two. "
            "We quickly realize that four times eight equals thirty-two, so cards four and eight unlock that envelope! "
            "Another envelope displays the number forty-five: choosing cards five and nine unlocks it because five times nine equals forty-five. "
            "For an envelope showing eighteen, we could pair two and nine, or three and six. "
            "For an envelope showing seven, only cards one and seven will work, because seven is a prime number. "
            "This mystery envelope puzzle exercises your algebraic deduction, factor recognition, and mental multiplication fluency simultaneously. "
            "Interact with the mystery envelope puzzle workbench to drag number cards into factor slots and unlock every secret envelope."
        ),
        "checkpoints": [
            {
                "question": "Which two number cards from 1 to 10 multiply to unlock an envelope stamped with 32?",
                "options": ["3 and 9", "4 and 8", "5 and 6", "2 and 14"],
                "answer": 1,
                "hint": "Check the multiplication table: 4 × 8 = ?",
                "explanation": "The cards 4 and 8 multiply to 4 × 8 = 32, unlocking the envelope."
            },
            {
                "question": "Which card pair unlocks an envelope stamped with the target product 45?",
                "options": ["4 and 9", "5 and 9", "6 and 7", "3 and 12"],
                "answer": 1,
                "hint": "5 times 9 equals 45.",
                "explanation": "The number cards 5 and 9 multiply to 5 × 9 = 45."
            }
        ]
    }
]

if __name__ == "__main__":
    for s in slides_part2:
        wc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({len(s['title'].split())} words) -> Speech: {wc} words")
        assert 195 <= wc <= 215, f"Slide {s['id']} speech out of range: {wc}"
        assert len(s["title"].split()) <= 3, f"Slide {s['id']} title too long"
        assert len(s["checkpoints"]) == 2, f"Slide {s['id']} must have 2 checkpoints"
    print("Part 2 verified successfully!")
