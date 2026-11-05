# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 9: Equal Groups
Part 2: Slides 9 to 16 Data Generator
Strictly 195 to 215 words per speech lecture.
Zero human names (Gulabo, Anvi, Raghav, etc. replaced with generic roles).
Clean Unicode throughout (×, ÷, +, -, =).
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Table Grid Symmetry",
        "section": "Multiplication Grids & Diagonal Invariants",
        "speech": (
            "A standard ten-by-ten multiplication table grid is not merely a collection of arithmetic facts; it is a magnificent "
            "tapestry of geometric symmetry and hidden numerical patterns! When students fill out the grid by multiplying each row "
            "header by each column header, they immediately discover symmetry across the main diagonal running from the top-left to "
            "the bottom-right. Numbers situated symmetrically opposite this diagonal line are identical: for instance, row three column "
            "seven contains twenty-one, exactly matching row seven column three, reflecting the commutative rule that three times seven "
            "equals seven times three. Investigating parity across rows reveals further wonder: rows with even headers contain exclusively "
            "even products, while rows with odd headers alternate between odd and even products. Even more captivating is the cycling "
            "of the ones digits! Look closely at row eight: eight, sixteen, twenty-four, thirty-two, forty, forty-eight, fifty-six, sixty-four, "
            "seventy-two, and eighty. The ones digits follow a repeating cyclic sequence: eight, six, four, two, zero, and then eight, "
            "six, four, two, zero again! Analyzing multiplication grid symmetry elevates mental math from rote memorization into keen visual "
            "investigation, deepening number sense, strengthening pattern intuition, and preparing young learners for advanced algebra, "
            "matrix theory, and mathematical exploration throughout life."
        ),
        "checkpoints": [
            {
                "q": "Why are the numbers at Row 3, Column 7 and Row 7, Column 3 identical (21)?",
                "options": ["Associative law", "Commutative property (3 × 7 = 7 × 3)", "Random chance", "Rounding rule"],
                "ans": 1,
                "exp": "The commutative property ensures 3 × 7 = 7 × 3 = 21."
            },
            {
                "q": "What repeating pattern appears in the ones digits of the 8 times table?",
                "options": ["1, 3, 5, 7, 9", "8, 6, 4, 2, 0", "2, 4, 6, 8, 0", "5, 0, 5, 0, 5"],
                "ans": 1,
                "exp": "Row 8 ones digits cycle continuously through 8, 6, 4, 2, 0."
            }
        ]
    },
    {
        "id": 10,
        "title": "Scaling Tens Products",
        "section": "Place Value Scaling & Zero Affixing Rules",
        "speech": (
            "One of the most powerful shortcuts in arithmetic involves scaling single-digit multiplication facts by powers of "
            "ten. Consider counting wheels across vehicles parked outside a bustling school. If one tricycle has three wheels, six "
            "tricycles have six times three, equaling eighteen wheels. Now suppose an agricultural warehouse stores sixty large "
            "three-wheeled cargo tricycles. How many wheels are there in total? Instead of computing a complex calculation, notice that "
            "sixty is simply six tens. Multiplying six by three gives eighteen, so sixty times three equals eighteen tens, or one hundred "
            "eighty! Likewise, if six delivery trucks each carry eighty replacement tires, we multiply six by eight to obtain forty-eight, "
            "and affix one zero to reach four hundred eighty tires. The mathematical rule is wonderfully straightforward: when multiplying "
            "by a multiple of ten, calculate the basic single-digit product first, and then shift the result one place value to the left "
            "by appending a zero in the ones place. Scaling by tens connects basic times tables directly with multi-digit calculation, "
            "drastically reducing calculation time, preventing tedious manual addition, and giving young scholars tremendous confidence "
            "when evaluating larger commercial quantities across real-world markets, transportation networks, and modern manufacturing industries."
        ),
        "checkpoints": [
            {
                "q": "If 6 × 8 = 48, what is 60 × 8?",
                "options": ["48", "480", "4800", "540"],
                "ans": 1,
                "exp": "60 × 8 = 6 tens × 8 = 48 tens = 480."
            },
            {
                "q": "How many total wheels are on 50 four-wheeled motor cars?",
                "options": ["100 wheels", "150 wheels", "200 wheels", "250 wheels"],
                "ans": 2,
                "exp": "50 × 4 = (5 × 4) tens = 20 tens = 200 wheels."
            }
        ]
    },
    {
        "id": 11,
        "title": "Tens Breakdown Area",
        "section": "Distributive Decomposition & Partial Products",
        "speech": (
            "When multiplying numbers greater than ten, the area breakdown model provides a transparent visual strategy by "
            "decomposing large multipliers into manageable tens and ones. Suppose a carpenter needs to calculate eighteen times four "
            "to construct four wooden book racks, each requiring eighteen screws. Calculating eighteen times four mentally might seem "
            "daunting at first. However, we can split eighteen into ten plus eight! Now we multiply each part separately by four: ten "
            "times four equals forty, and eight times four equals thirty-two. Adding these two partial products together, forty plus "
            "thirty-two produces seventy-two screws in total! This elegant technique embodies the distributive property of multiplication "
            "over addition. Consider another practical example: an artisan prepares twenty-three bamboo rods for eight bullock carts. "
            "Decomposing twenty-three into twenty and three allows us to multiply each piece by eight. Twenty times eight yields one hundred "
            "sixty, while three times eight yields twenty-four. Adding one hundred sixty and twenty-four gives one hundred eighty-four bamboo "
            "rods! Breaking numbers into tens and ones eliminates guesswork, transforms intimidating multi-digit problems into accessible mental "
            "steps, and establishes foundational algebraic thinking that serves students throughout their ongoing mathematical journey across higher grades and everyday practical calculations."
        ),
        "checkpoints": [
            {
                "q": "Using the breakdown method for 18 × 4, what are the two partial products?",
                "options": ["10 and 8", "40 and 32", "20 and 12", "50 and 22"],
                "ans": 1,
                "exp": "(10 × 4) = 40, and (8 × 4) = 32. 40 + 32 = 72."
            },
            {
                "q": "How is 23 × 8 broken down into tens and ones?",
                "options": ["(20 × 8) + (3 × 8)", "(10 × 8) + (13 × 8)", "(20 × 4) + (3 × 4)", "(25 × 8) - (2 × 8)"],
                "ans": 0,
                "exp": "23 = 20 + 3. Therefore, 23 × 8 = (20 × 8) + (3 × 8) = 160 + 24 = 184."
            }
        ]
    },
    {
        "id": 12,
        "title": "Animal Leg Counts",
        "section": "Multi-Step Word Problems & Composite Sums",
        "speech": (
            "Real-world problem solving often requires combining multiplication and addition across multiple distinct groups. "
            "Consider a lively farm sanctuary housing diverse domestic animals. A visiting student observes twenty geese and fifteen "
            "woolly sheep grazing peacefully in an open green meadow. How many animal legs are on the meadow in total? To solve this "
            "multi-step story, we analyze each species separately. A goose is a bird with two legs, so twenty geese have twenty multiplied "
            "by two, which equals forty legs. A sheep is a four-legged mammal, so fifteen sheep have fifteen multiplied by four, which "
            "equals sixty legs. Finally, adding forty goose legs and sixty sheep legs reveals exactly one hundred legs on the meadow! "
            "Similar logic applies to auditorium seating arrangements: an assembly hall contains fifteen rows with twelve chairs per "
            "row. Decomposing fifteen into ten plus five allows us to calculate ten times twelve as one hundred twenty, plus five times "
            "twelve as sixty, totaling one hundred eighty auditorium seats. Solving composite word problems trains students to extract "
            "relevant facts, identify appropriate operational sequences, manage multi-step calculations methodically, and communicate "
            "clear mathematical justifications with precision, rigor, and enthusiasm across diverse everyday school, agricultural, and community contexts."
        ),
        "checkpoints": [
            {
                "q": "How many total legs do 20 two-legged geese and 15 four-legged sheep have altogether?",
                "options": ["80 legs", "90 legs", "100 legs", "120 legs"],
                "ans": 2,
                "exp": "(20 × 2) + (15 × 4) = 40 + 60 = 100 legs."
            },
            {
                "q": "An auditorium has 15 rows with 12 chairs in each row. How many total chairs are there?",
                "options": ["150 chairs", "160 chairs", "180 chairs", "200 chairs"],
                "ans": 2,
                "exp": "15 × 12 = (10 × 12) + (5 × 12) = 120 + 60 = 180 chairs."
            }
        ]
    },
    {
        "id": 13,
        "title": "Partial Quotient Division",
        "section": "Repeated Chunking & Friendly Multiples",
        "speech": (
            "Division can be intuitively mastered as repeated grouping using friendly chunks of tens, fives, and twos, known "
            "as the partial quotient method. Traditional long division algorithms often seem abstract and mechanical, but chunking "
            "focuses on practical estimation. Imagine a transport garage with forty-eight wheels that must be fitted onto three-wheeled "
            "passenger auto-rickshaws. How many auto-rickshaws can be fully equipped? Instead of dividing blindly, we remove friendly "
            "groups! First, equipping ten auto-rickshaws uses ten times three, which is thirty wheels. Subtracting thirty from forty-eight "
            "leaves eighteen wheels remaining. Next, we ask: how many threes fit into eighteen? Exactly six! Equipping six more rickshaws "
            "uses six times three, which is eighteen wheels, leaving zero wheels remaining. Adding our partial quotients, ten plus six "
            "proves that exactly sixteen auto-rickshaws are equipped! This same friendly chunking method effortlessly solves packaging "
            "stories: distributing sixty-four badminton shuttlecocks into tubes of four, allocating ninety-six rose saplings into rows "
            "of six, or grouping eighty octopus tentacles into creatures of eight. Partial quotient division allows students to use "
            "multiplication facts they already know, demystifying division and fostering remarkable mental agility, procedural confidence, and lasting mathematical arithmetic mastery across all classrooms, homes, and community workshops."
        ),
        "checkpoints": [
            {
                "q": "How many 3-wheeled auto-rickshaws can be equipped using 48 wheels?",
                "options": ["12 rickshaws", "14 rickshaws", "16 rickshaws", "18 rickshaws"],
                "ans": 2,
                "exp": "48 ÷ 3 = (30 ÷ 3) + (18 ÷ 3) = 10 + 6 = 16 rickshaws."
            },
            {
                "q": "If 64 shuttlecocks are packed into tubes holding 4 each, how many tubes are filled?",
                "options": ["14 tubes", "16 tubes", "18 tubes", "20 tubes"],
                "ans": 1,
                "exp": "64 ÷ 4 = (40 ÷ 4) + (24 ÷ 4) = 10 + 6 = 16 tubes."
            }
        ]
    },
    {
        "id": 14,
        "title": "Scaling Hundreds Math",
        "section": "Hundreds Multipliers & Expanded Packaging",
        "speech": (
            "Just as we scaled single-digit facts by multiples of ten, we can naturally expand our mathematical reach to multiples "
            "of one hundred! Suppose a city transportation planner assesses passenger capacity across commuter vehicles. If a compact "
            "car carries four passengers, how many passengers can five hundred cars transport during morning rush hour? We simply multiply "
            "five by four to get twenty, and since we are dealing with hundreds, we affix two zeros to obtain two thousand passengers! "
            "This principle extends to larger multi-digit products using our expanded area breakdown model. Imagine an electric vehicle "
            "fleet consisting of eight shuttle buses, each carrying one hundred twenty-five passengers daily. To find the grand total, we "
            "decompose one hundred twenty-five into one hundred, twenty, and five! Multiplying each component by eight yields: one hundred "
            "times eight equals eight hundred; twenty times eight equals one hundred sixty; and five times eight equals forty. Summing eight "
            "hundred, one hundred sixty, and forty yields exactly one thousand passengers! Similarly, a traditional potter packs one hundred "
            "seventy-four clay tea cups into six delivery crates. Multiplying one hundred seventy-four by six yields one thousand forty-four "
            "cups! Scaling into the hundreds empowers learners to tackle realistic large-scale problems with ease and joy."
        ),
        "checkpoints": [
            {
                "q": "How many passengers can 500 cars carry if each car holds 4 passengers?",
                "options": ["1,000", "1,500", "2,000", "2,500"],
                "ans": 2,
                "exp": "500 × 4 = (5 × 4) hundreds = 20 hundreds = 2,000 passengers."
            },
            {
                "q": "What is 125 × 8 calculated by expanding 100 + 20 + 5?",
                "options": ["800", "960", "1,000", "1,040"],
                "ans": 2,
                "exp": "(100 × 8) + (20 × 8) + (5 × 8) = 800 + 160 + 40 = 1,000."
            }
        ]
    },
    {
        "id": 15,
        "title": "Sharing Measure Division",
        "section": "Equal Sharing vs Measurement Grouping",
        "speech": (
            "In practical life, division appears in two distinct but deeply connected forms: sharing division and measurement "
            "division. In sharing division, a known whole is partitioned equally among a fixed number of recipients to determine each "
            "recipient's share. For example, if seventy-two village travelers must cross a wide river in nine identical wooden boats, "
            "dividing seventy-two by nine gives eight passengers per boat. The number of groups is known, and we seek the group size. "
            "Conversely, in measurement division, the size of each group is known, and we seek the total number of groups created! For "
            "instance, a mechanical repair workshop stocks forty-eight heavy truck tires. If each freight truck requires six tires, dividing "
            "forty-eight by six reveals that exactly eight trucks can be fully outfitted. Here, the group size of six is fixed, and division "
            "measures how many trucks can be served. We observe the same distinction when sharing money: dividing six hundred rupees "
            "equally among three children awards two hundred rupees each. Understanding whether a puzzle represents equal sharing or "
            "measurement grouping sharpens problem-solving clarity, ensures appropriate diagram modeling, and enriches mathematical reasoning "
            "across logistics, finance, manufacturing, agriculture, and daily community collaborations across our shared civilized world."
        ),
        "checkpoints": [
            {
                "q": "If 72 travelers cross a river equally in 9 boats, how many travelers are in each boat?",
                "options": ["6 travelers", "7 travelers", "8 travelers", "9 travelers"],
                "ans": 2,
                "exp": "72 ÷ 9 = 8 travelers per boat (equal sharing division)."
            },
            {
                "q": "A workshop has 48 tires. If each truck needs 6 tires, how many trucks can be outfitted?",
                "options": ["6 trucks", "7 trucks", "8 trucks", "9 trucks"],
                "ans": 2,
                "exp": "48 ÷ 6 = 8 trucks (measurement grouping division)."
            }
        ]
    },
    {
        "id": 16,
        "title": "Logical Reasoning Statements",
        "section": "Mathematical Claims & Counterexample Logic",
        "speech": (
            "As mature young mathematicians, our journey culminates in evaluating mathematical claims critically to determine "
            "whether statements are 'Always True', 'Never True', or 'Sometimes True'. Rigorous reasoning requires testing claims "
            "systematically and searching for counterexamples. Consider the statement: 'The product of two even numbers is always even.' "
            "Testing pairs like two times four equaling eight, or six times eight equaling forty-eight, demonstrates that this statement "
            "is 'Always True'. What about the claim: 'Dividing a number by two always produces an even number'? Testing eight divided "
            "by two yields four, which is even; but dividing ten by two yields five, which is odd! Since a single counterexample disproves "
            "universality, the statement is classified as 'Sometimes True'. Now examine real-world travel math: the Darjeeling Himalayan "
            "Toy Train travels eighty-eight kilometers daily. In one full week of seven days, multiplying eighty-eight by seven reveals "
            "a weekly journey of six hundred sixteen kilometers! In whitewater rafting, if ninety-six adventurers board rafts holding "
            "six rafters each, dividing ninety-six by six proves that sixteen rafts are launched. Evaluating logical statements trains "
            "us to reason soundly, seek proof, reject hasty generalizations, and champion truth through evidence-based mathematical clarity throughout science, commerce, and daily life."
        ),
        "checkpoints": [
            {
                "q": "Is the statement 'The product of any two even numbers is always even' Always, Sometimes, or Never True?",
                "options": ["Always True", "Sometimes True", "Never True", "Cannot be determined"],
                "ans": 0,
                "exp": "Even × Even is Always Even (e.g., 2 × 4 = 8, 6 × 8 = 48)."
            },
            {
                "q": "If a toy train travels 88 km each day, how far does it travel in 1 full week (7 days)?",
                "options": ["566 km", "606 km", "616 km", "626 km"],
                "ans": 2,
                "exp": "88 × 7 = (80 × 7) + (8 × 7) = 560 + 56 = 616 km."
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
