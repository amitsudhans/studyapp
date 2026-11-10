# -*- coding: utf-8 -*-
"""
Generate Slides 9 to 16 for Class 3 Mathematics - Chapter 3: Double Century
Strict requirements:
- Titles: Strictly 1-3 words each
- Spoken text: Strictly 195-215 words each
- Pure Indian male teacher sound lecture style
- Zero human character names (no Raghav, Meera, Dhruv, Teji, Jojo, Deba, Deep, Pihu, etc.)
- Zero lecturer personas (no Dr, Sir, Madam, Mr, Mrs, Miss)
- 2 checkpoints per slide with 4 options each
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Flower Petal Puzzles",
        "badge": "Century Petals",
        "sim_id": "sim_flower_petal_puzzles",
        "description": "Solve captivating floral addition puzzles where petal numbers pair up to match the central core total of exactly one hundred.",
        "speech": (
            "Mathematics and nature unite in a delightful arithmetic challenge known as the Flower Petal Puzzle! "
            "Picture a radiant blooming flower where the central golden disc displays the milestone target number: one hundred. "
            "Surrounding this center are colorful petals containing numbers that must pair together to create that exact central sum of one hundred! "
            "For instance, if one petal displays eighty, its corresponding opposite petal must display twenty, because eighty plus twenty equals one hundred. "
            "If another petal shows forty-five, its partner must hold fifty-five, since forty-five plus fifty-five equals one hundred! "
            "Solving petal puzzles trains the mind to break one hundred into varied two-part combinations: "
            "fifty plus fifty, ten plus ninety, thirty plus seventy, and seventy-five plus twenty-five. "
            "Students also explore physical estimations: examining standard matchstick boxes holding about fifty sticks each. "
            "Two full boxes of fifty sticks combine to yield one complete century of one hundred sticks! "
            "Similarly, counting dry tamarind or rajma seeds in handfuls helps students feel what one hundred physical objects look like in their palms. "
            "Every single pair that totals one hundred strengthens mental fluency and prepares young mathematicians for higher operations. "
            "These petal and seed investigations bridge rapid mental calculation agility with tangible, sensory mathematical understanding throughout primary childhood education."
        ),
        "checkpoints": [
            {
                "q": "In a flower petal puzzle with 100 at the center, what number must pair with 45 on the opposite petal?",
                "options": [
                    "55 (45 + 55 = 100)",
                    "65",
                    "50",
                    "45"
                ],
                "ans": "55 (45 + 55 = 100)",
                "explanation": "45 + 55 = 100, so 55 is the correct complementary partner petal."
            },
            {
                "q": "How many full boxes containing 50 matchsticks each are needed to reach a total of 100 matchsticks?",
                "options": [
                    "2 full boxes (50 + 50 = 100)",
                    "5 full boxes",
                    "4 full boxes",
                    "10 full boxes"
                ],
                "ans": "2 full boxes (50 + 50 = 100)",
                "explanation": "Two boxes of 50 sticks each give 50 + 50 = 100 matchsticks."
            }
        ]
    },
    {
        "id": 10,
        "title": "Counting Beyond Hundred",
        "badge": "Three-Digit Sequence",
        "sim_id": "sim_counting_beyond_hundred",
        "description": "Cross the century threshold to read, write, and order three-digit numbers systematically from 101 up to 124.",
        "speech": (
            "Stepping beyond one hundred opens the expansive horizon of three-digit numbers! "
            "Once young learners reach one hundred, how does the numerical journey continue? "
            "The counting pattern follows the exact same logical rules as before, but with one full hundred anchored in the hundreds place. "
            "We say: 'one hundred and one' for one hundred plus one, written as 1-0-1. "
            "Next comes 'one hundred and two' (1-0-2), 'one hundred and three' (1-0-3), and so on, all the way to 'one hundred and ten' (1-1-0)! "
            "Notice how the tens and ones places repeat their familiar sequence from one to nine, "
            "while the digit one stands proudly on the left to show one full hundred. "
            "On a calibrated number line extending past one hundred, each forward step of one unit advances the sequence: "
            "one hundred and eleven, one hundred and twelve, up to one hundred and twenty-four! "
            "If you stand on tile one hundred and nineteen and take one more step forward, "
            "nineteen becomes twenty, landing you precisely on one hundred and twenty! "
            "Understanding this continuous rhythm proves that counting never ends; "
            "it expands predictably across centuries, empowering students to navigate larger three-digit values with complete clarity and confidence."
        ),
        "checkpoints": [
            {
                "q": "What number comes immediately after 119 in the counting sequence?",
                "options": [
                    "120 (One Hundred Twenty)",
                    "118",
                    "130",
                    "121"
                ],
                "ans": "120 (One Hundred Twenty)",
                "explanation": "Adding 1 to 119 gives 119 + 1 = 120."
            },
            {
                "q": "How is the number 'one hundred and eight' correctly written in standard digits?",
                "options": [
                    "108",
                    "180",
                    "18",
                    "1008"
                ],
                "ans": "108",
                "explanation": "One hundred and eight has 1 hundred, 0 tens, and 8 ones, written as 108."
            }
        ]
    },
    {
        "id": 11,
        "title": "Hundred Matchstick Bundles",
        "badge": "Bundle Place Value",
        "sim_id": "sim_matchstick_bundles_150",
        "description": "Model three-digit quantities up to 150 using large bundles of 100, standard bundles of 10, and single loose matchsticks.",
        "speech": (
            "To build concrete physical mastery of three-digit numbers, we use the tactile power of matchstick bundling! "
            "In this modeling system, matchsticks are organized into three distinct hierarchical levels: "
            "single loose sticks representing ones, small bundles of ten sticks tied with thread representing tens, "
            "and a large, thick master bundle containing ten tens tied together, representing one hundred! "
            "Let us construct the number one hundred and thirty-five using our matchstick collection. "
            "First, we place one large hundred-bundle on the table: that gives one hundred. "
            "Next, to represent thirty, we place three bundles of ten: ten, twenty, thirty. "
            "Finally, to represent five, we add five loose single sticks. "
            "Looking across our table from left to right, we see: one hundred, three tens, and five ones! "
            "Combining them together: one hundred plus thirty plus five equals one hundred and thirty-five, written as 1-3-5. "
            "If we add one more ten-bundle, the count becomes one hundred and forty-five (1-4-5). "
            "If we add another ten-bundle, we reach one hundred and fifty! "
            "Notice how ten ones bundle into a ten, and ten tens bundle into a hundred. "
            "This structured nesting reflects the universal decimal architecture that defines modern arithmetic everywhere. "
            "Physical bundling transforms abstract written digits into tangible quantities that children can see, touch, group, and thoroughly comprehend."
        ),
        "checkpoints": [
            {
                "q": "What number is formed by 1 bundle of 100, 4 bundles of 10, and 7 loose matchsticks?",
                "options": [
                    "147",
                    "174",
                    "417",
                    "140"
                ],
                "ans": "147",
                "explanation": "100 + 40 + 7 = 147 (one hundred forty-seven)."
            },
            {
                "q": "How many small bundles of 10 are tied together to create 1 large master bundle of 100?",
                "options": [
                    "10 bundles of 10",
                    "100 bundles",
                    "5 bundles of 10",
                    "20 bundles of 10"
                ],
                "ans": "10 bundles of 10",
                "explanation": "10 bundles of 10 sticks equal 100 sticks (10 x 10 = 100)."
            }
        ]
    },
    {
        "id": 12,
        "title": "Counting To One-Fifty",
        "badge": "Matching Sequences",
        "sim_id": "sim_counting_to_150",
        "description": "Master the number range from 120 to 150 through bundle diagram match-ups, number line points, and Talking Pot chains.",
        "speech": (
            "As we advance deeper into the century journey, let us explore the numbers spanning from one hundred and twenty up to one hundred and fifty! "
            "In this section, students engage in exciting matching activities, pairing illustrated bundle diagrams with their exact three-digit numerals. "
            "For example, a diagram displaying one hundred-bundle, two ten-bundles, and eight loose sticks connects directly to the numeral 1-2-8: one hundred and twenty-eight! "
            "The enchanted Talking Pot returns with advanced sequential challenges. "
            "If the pot receives one hundred and thirty-nine, it announces: 'one hundred and forty'! "
            "If it receives one hundred and forty-nine, it rings out: 'one hundred and fifty'! "
            "Plotting these values on calibrated number lines reinforces proportional spatial reasoning. "
            "On a number line running from one hundred to one hundred and fifty, "
            "the number one hundred and twenty-five sits at the exact midway point between one hundred and one hundred and fifty. "
            "Locating numbers like one hundred and thirty-two or one hundred and forty-seven requires observing ten-unit intervals and counting single units carefully. "
            "Connecting consecutive points creates an orderly visual progression that builds intuitive magnitude sense for expanding three-digit values. "
            "Practicing multiple representations—numerals, word names, number line positions, and visual bundles—cements rock-solid arithmetic understanding up to one hundred and fifty."
        ),
        "checkpoints": [
            {
                "q": "What number sits exactly at the midpoint between 100 and 150 on a calibrated number line?",
                "options": [
                    "125",
                    "120",
                    "130",
                    "140"
                ],
                "ans": "125",
                "explanation": "The difference between 100 and 150 is 50; half of 50 is 25. 100 + 25 = 125."
            },
            {
                "q": "If the Talking Pot is fed the number 149, what number will it speak next?",
                "options": [
                    "150",
                    "148",
                    "160",
                    "151"
                ],
                "ans": "150",
                "explanation": "The successor of 149 is 149 + 1 = 150."
            }
        ]
    },
    {
        "id": 13,
        "title": "Clap Snap Pat",
        "badge": "Rhythmic Place Value",
        "sim_id": "sim_clap_snap_pat",
        "description": "Engage in an auditory multi-sensory game where clapping represents hundreds, snapping represents tens, and patting represents ones.",
        "speech": (
            "Mathematics is not confined to paper and pencil; it can be heard, clapped, snapped, and celebrated through musical rhythm! "
            "In Chapter 3, students play an exhilarating classroom game called 'Clap, Snap, and Pat'. "
            "In this auditory game, physical actions represent mathematical place values: "
            "one loud hand CLAP represents one hundred; "
            "one finger SNAP represents ten; "
            "and one thigh PAT represents one single unit! "
            "Let us test your ears with a secret rhythmic number code! "
            "Listen closely: CLAP! SNAP! SNAP! SNAP! PAT! PAT! "
            "Let us decode the actions systematically: "
            "one CLAP equals one hundred. "
            "Three SNAPS equal three tens, which is thirty. "
            "Two PATS equal two single ones. "
            "Putting the parts together: one hundred plus thirty plus two equals one hundred and thirty-two! "
            "What if a team performs two CLAPS, zero snaps, and five PATS? "
            "Two CLAPS equal two hundred, zero snaps mean zero tens, and five PATS mean five ones, giving two hundred and five! "
            "Every sequence turns listening skills into accurate mental place value calculation while students collaborate enthusiastically together. "
            "By translating abstract place values into distinct body sounds, "
            "the Clap, Snap, and Pat game transforms decimal column alignment into an unforgettable, joyous musical performance for every learner."
        ),
        "checkpoints": [
            {
                "q": "In the game, what number is represented by 1 Clap (100), 4 Snaps (10 each), and 3 Pats (1 each)?",
                "options": [
                    "143",
                    "134",
                    "431",
                    "140"
                ],
                "ans": "143",
                "explanation": "1 Clap = 100, 4 Snaps = 40, 3 Pats = 3. Total = 100 + 40 + 3 = 143."
            },
            {
                "q": "Which sound action represents the tens place in the Clap, Snap, and Pat game?",
                "options": [
                    "A finger snap (10)",
                    "A hand clap",
                    "A thigh pat",
                    "A foot stomp"
                ],
                "ans": "A finger snap (10)",
                "explanation": "Clap = 100 (hundreds), Snap = 10 (tens), and Pat = 1 (ones)."
            }
        ]
    },
    {
        "id": 14,
        "title": "Place Value Breakdowns",
        "badge": "Expanded Forms",
        "sim_id": "sim_place_value_breakdowns",
        "description": "Deconstruct three-digit numbers from 150 to 159 into expanded forms, place value tables, and formal written number names.",
        "speech": (
            "Every three-digit number has an internal architectural blueprint that can be systematically deconstructed into expanded mathematical form! "
            "Let us examine the number sequence from one hundred and fifty up to one hundred and fifty-nine. "
            "Take the number one hundred and fifty-seven (1-5-7). "
            "When we place 1-5-7 into our three-column place value chart, we observe: "
            "the digit one sits in the hundreds place, having a value of one hundred; "
            "the digit five rests in the tens place, having a value of fifty; "
            "and the digit seven sits in the ones place, having a value of seven single units. "
            "Writing this breakdown as an addition sentence creates the expanded form: "
            "one hundred and fifty-seven equals one hundred plus fifty plus seven! "
            "We also write its formal English words: 'one hundred fifty-seven'. "
            "Consider another example: one hundred and fifty. "
            "Here, there is one hundred, five tens, and zero ones: one hundred plus fifty plus zero equals one hundred and fifty! "
            "Expanded notation makes the hidden power and specific positional weight of each digit crystal clear. "
            "Whether reading large totals on price tags or solving written equations, this structural insight guides accurate arithmetic reasoning. "
            "Mastering place value breakdowns guarantees that students never confuse digit values like five tens (fifty) with five ones (five)."
        ),
        "checkpoints": [
            {
                "q": "What is the correct expanded form of the number 158?",
                "options": [
                    "100 + 50 + 8",
                    "10 + 50 + 8",
                    "150 + 80",
                    "1 + 5 + 8"
                ],
                "ans": "100 + 50 + 8",
                "explanation": "158 has 1 hundred (100), 5 tens (50), and 8 ones (8): 100 + 50 + 8."
            },
            {
                "q": "In the number 154, what is the exact place value of the digit 5?",
                "options": [
                    "50 (5 tens)",
                    "5 (5 ones)",
                    "500 (5 hundreds)",
                    "15"
                ],
                "ans": "50 (5 tens)",
                "explanation": "The digit 5 is in the tens column, so its value is 5 tens, which equals 50."
            }
        ]
    },
    {
        "id": 15,
        "title": "Number Line Jumps",
        "badge": "Skip Counting",
        "sim_id": "sim_number_line_jumps",
        "description": "Perform dynamic forward and backward jumps of 5 and 20 along calibrated number lines reaching toward two hundred.",
        "speech": (
            "Let us take to the open trail of the number line to practice athletic mathematical jumps! "
            "A number line is an endless straight highway of numbers, spaced with perfect mathematical precision. "
            "Beyond counting by single steps of one, mathematicians love skip-counting in larger rhythmic leaps. "
            "Let us begin with jumps of five! "
            "Starting at one hundred, leap forward five units: one hundred and five! "
            "Leap five more: one hundred and ten! "
            "Continuing this five-unit rhythm brings us to one hundred and fifteen, one hundred and twenty, and onwards! "
            "Notice how the ones digit alternates gracefully between five and zero on every single leap! "
            "Now let us take giant kangaroo leaps of twenty! "
            "Start at one hundred and leap twenty forward: one hundred and twenty! "
            "Another leap of twenty brings us to one hundred and forty. "
            "Leap again: one hundred and sixty! "
            "Leap again: one hundred and eighty! "
            "And one final magnificent leap of twenty lands us directly on two hundred! "
            "We can also leap backward to explore subtraction: starting at one hundred and sixty and jumping backward twenty lands at one hundred and forty. "
            "Skip-counting along number lines builds deep spatial estimation and prepares young minds for mental multiplication."
        ),
        "checkpoints": [
            {
                "q": "If you start at 120 and make two consecutive forward jumps of 20, what number do you reach?",
                "options": [
                    "160 (120 + 20 + 20)",
                    "140",
                    "180",
                    "150"
                ],
                "ans": "160 (120 + 20 + 20)",
                "explanation": "First jump: 120 + 20 = 140. Second jump: 140 + 20 = 160."
            },
            {
                "q": "What pattern appears in the ones digits when skip-counting forward by 5 starting from 100?",
                "options": [
                    "The ones digit alternates between 0 and 5",
                    "The ones digit is always 2",
                    "The ones digit increases by 3 every time",
                    "The ones digit is always 9"
                ],
                "ans": "The ones digit alternates between 0 and 5",
                "explanation": "Counting by 5s produces: 100, 105, 110, 115, 120... alternating between 0 and 5 in the ones place."
            }
        ]
    },
    {
        "id": 16,
        "title": "Double Century Goal",
        "badge": "Mastery Summit",
        "sim_id": "sim_double_century_goal",
        "description": "Celebrate reaching the double century milestone of 200 through seed estimation, multi-way representations, and grand synthesis.",
        "speech": (
            "Congratulations on climbing the mathematical summit of Chapter 3: the magnificent Double Century! "
            "In cricket history, scoring one hundred runs is a century, while scoring two hundred runs in a single innings is a celebrated 'double century'! "
            "The number two hundred represents two full centuries combined: one hundred plus one hundred equals two hundred, written as 2-0-0. "
            "Let us synthesize all our multi-way representations for this monumental milestone. "
            "In matchstick bundling, two hundred equals two large master hundred-bundles, or twenty small ten-bundles, or two hundred loose single sticks! "
            "On calibrated ginladi bead strings, two hundred spans two complete one-hundred-bead strands. "
            "In home science estimation, a small bowl holding one hundred rajma seeds doubled holds two hundred seeds. "
            "In place value columns, the numeral 2-0-0 displays: two in the hundreds column, zero tens in the middle column, and zero ones in the first column. "
            "From prehistoric bone scratches and cave marks to the Indian invention of base-ten and zero, "
            "you now possess the numerical power to read, write, count, and manipulate quantities all the way to two hundred! "
            "With this double century mastery in your toolkit, the vast world of mathematics is wide open for your exploration."
        ),
        "checkpoints": [
            {
                "q": "What is the numerical meaning of a 'Double Century'?",
                "options": [
                    "Two hundred (200 = 100 + 100)",
                    "One hundred fifty (150)",
                    "Three hundred (300)",
                    "Twenty (20)"
                ],
                "ans": "Two hundred (200 = 100 + 100)",
                "explanation": "A century is 100; a double century is twice that amount: 100 + 100 = 200."
            },
            {
                "q": "How many bundles of 10 matchsticks are needed to make 200 matchsticks?",
                "options": [
                    "20 bundles of 10",
                    "10 bundles of 10",
                    "2 bundles of 10",
                    "200 bundles of 10"
                ],
                "ans": "20 bundles of 10",
                "explanation": "20 bundles x 10 sticks per bundle = 200 sticks."
            }
        ]
    }
]

if __name__ == "__main__":
    print("=== VERIFYING SLIDES 9 TO 16 ===")
    assert len(slides_part2) == 8

    for s in slides_part2:
        sid = s["id"]
        title = s["title"]
        tw = len(title.split())
        assert 1 <= tw <= 3, f"Slide {sid} title '{title}' must be 1-3 words (got {tw})"
        
        speech = s["speech"]
        wc = len(speech.split())
        print(f"Slide {sid}: '{title}' -> {wc} words")
        assert 195 <= wc <= 215, f"Slide {sid} word count {wc} out of range 195-215!"
        
        assert len(s["checkpoints"]) == 2, f"Slide {sid} must have 2 checkpoints"
        for cp in s["checkpoints"]:
            assert len(cp["options"]) == 4, f"Slide {sid} checkpoint options != 4"
            assert cp["ans"] in cp["options"], f"Slide {sid} ans not in options"

    print("Part 2 verified successfully!")
