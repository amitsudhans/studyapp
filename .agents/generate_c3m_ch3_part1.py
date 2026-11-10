# -*- coding: utf-8 -*-
"""
Generate Slides 1 to 8 for Class 3 Mathematics - Chapter 3: Double Century
Strict requirements:
- Titles: Strictly 1-3 words each
- Spoken text: Strictly 195-215 words each
- Pure Indian male teacher sound lecture style
- Zero human character names (no Raghav, Meera, Dhruv, Teji, Jojo, Deba, Deep, Pihu, etc.)
- Zero lecturer personas (no Dr, Sir, Madam, Mr, Mrs, Miss)
- 2 checkpoints per slide with 4 options each
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Prehistoric Counting Marks",
        "badge": "Ancient Origins",
        "sim_id": "sim_prehistoric_tally",
        "description": "Discover how ancient humans recorded quantities tens of thousands of years ago using bone notches, cave scratches, and grouping systems.",
        "speech": (
            "Welcome to the captivating mathematical chronicle of our numbers! "
            "Long before schools, textbooks, and electronic calculators existed, ancient humans needed practical ways to keep count of their worldly possessions. "
            "Tens of thousands of years ago, early hunters and pastoral tribes tracked passing days, seasonal moon cycles, and animal herds "
            "by carving straight notches into animal bones, chipping scratch marks onto stone cave walls, and carving grooves into tree trunks. "
            "Initially, each single notch represented exactly one physical object, following strict one-to-one correspondence. "
            "However, as herds expanded and days accumulated, counting hundreds of individual single marks became exceedingly tedious and confusing! "
            "To solve this problem, creative prehistoric thinkers invented the revolutionary technique of numerical grouping. "
            "Some ancient civilizations grouped tally marks by fives, mirroring the five fingers of a human hand. "
            "Other cultures grouped quantities by tens, using all fingers on both hands, while others grouped by twenties, counting fingers and toes combined! "
            "Certain advanced ancient astronomers even organized calculations in groups of sixty to track celestial planetary movements. "
            "These early grouping breakthroughs laid the structural groundwork for our modern decimal number system. "
            "Understanding how our ancestors counted helps us appreciate the brilliance behind every number we write today."
        ),
        "checkpoints": [
            {
                "q": "Why did ancient people begin grouping tally marks into sets of 5, 10, or 20 instead of counting single marks?",
                "options": [
                    "Counting hundreds of single marks was tedious and prone to errors",
                    "They were running out of ink on cave walls",
                    "Single marks were strictly forbidden by ancient laws",
                    "Because bones could only hold three marks total"
                ],
                "ans": "Counting hundreds of single marks was tedious and prone to errors",
                "explanation": "Grouping tally marks into bundles of 5, 10, or 20 allowed ancient humans to count larger numbers rapidly and accurately."
            },
            {
                "q": "Which anatomical feature of the human body directly inspired ancient cultures to group numbers by ten?",
                "options": [
                    "The ten fingers on both hands",
                    "The number of teeth in the mouth",
                    "The two eyes on a human face",
                    "The four chambers of the heart"
                ],
                "ans": "The ten fingers on both hands",
                "explanation": "Having ten fingers across two hands naturally led humans across ancient civilizations to group quantities into tens."
            }
        ]
    },
    {
        "id": 2,
        "title": "Indian Base Ten",
        "badge": "World Heritage",
        "sim_id": "sim_base_ten_system",
        "description": "Explore the ancient Indian creation of the decimal place-value system using only ten digits to express any numerical quantity.",
        "speech": (
            "Among all intellectual achievements in world history, one of humanity's greatest mathematical gifts came from ancient India: the decimal base-ten place value system! "
            "Before this invention, ancient civilizations struggled with cumbersome numeral notations. "
            "For instance, Roman numerals required creating ever-new cumbersome letters like X, C, and M, making large arithmetic calculations remarkably difficult. "
            "Ancient Indian mathematicians devised an astonishingly elegant solution: "
            "they established that every possible number in the universe—from tiny counts to millions—can be written using only ten fundamental symbols: "
            "zero, one, two, three, four, five, six, seven, eight, and nine! "
            "The magic of this base-ten system lies in the principle of place value. "
            "When a digit moves one position to the left, its mathematical worth multiplies tenfold! "
            "For example, the digit four in the ones place means four single units; "
            "placed in the tens place, it means forty; and placed in the hundreds place, it represents four hundred! "
            "Today, this profound Indian invention powers the modern technological world: "
            "every computer program, mobile smartphone, digital wristwatch, scientific research laboratory, and global space exploration mission operates on these exact ten mathematical symbols. "
            "Mastering base-ten place value connects every young student directly to centuries of magnificent mathematical heritage."
        ),
        "checkpoints": [
            {
                "q": "How many fundamental digit symbols are used in the Indian decimal base-ten number system?",
                "options": [
                    "Ten symbols (0 through 9)",
                    "Twenty-six alphabet letters",
                    "One hundred separate symbols",
                    "Five counting tallies"
                ],
                "ans": "Ten symbols (0 through 9)",
                "explanation": "The decimal system uses exactly ten digits (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) combined with place value."
            },
            {
                "q": "What happens to the value of a digit when it moves one position to the left in a number?",
                "options": [
                    "Its value multiplies by 10",
                    "Its value stays exactly the same",
                    "Its value is cut in half",
                    "Its value decreases by 1"
                ],
                "ans": "Its value multiplies by 10",
                "explanation": "In our base-10 system, each column to the left is ten times greater than the column immediately to its right."
            }
        ]
    },
    {
        "id": 3,
        "title": "Power Of Zero",
        "badge": "Essential Placeholder",
        "sim_id": "sim_zero_placeholder",
        "description": "Understand the revolutionary mathematical role of zero as both an absence of quantity and an indispensable column placeholder.",
        "speech": (
            "While counting objects like fruits or cattle seems natural, conceptualizing and writing 'nothing' required a stroke of pure mathematical genius: the discovery of zero! "
            "Ancient Indian scholars formalized zero, named 'shunya', meaning empty or void, and represented it with a circular dot or ring. "
            "Zero serves two fundamentally vital roles in mathematics. "
            "First, as a numerical quantity, zero represents the complete absence of items. "
            "If a fruit basket holds five mangoes and you eat all five, zero mangoes remain in the basket! "
            "Second, and even more critically, zero acts as an indispensable column placeholder in multi-digit numbers. "
            "Consider the number one hundred and five. "
            "This quantity contains one hundred, zero tens, and five ones. "
            "Without the placeholder digit zero in the middle tens column, writing one and five together would produce fifteen instead of one hundred and five! "
            "That would cause a catastrophic arithmetic error of ninety units! "
            "Zero holds the empty column open, ensuring that the digit one remains securely in the hundreds place. "
            "Without zero, modern decimal arithmetic, place-value calculation, algebraic reasoning, and computer binary software coding would be completely impossible. "
            "The concept of zero proves undeniably that a humble symbol representing absolute emptiness holds immense transformative mathematical power throughout human civilization."
        ),
        "checkpoints": [
            {
                "q": "What critical role does zero play in the number 105?",
                "options": [
                    "It acts as a placeholder showing there are 0 tens",
                    "It makes the number negative",
                    "It divides the number into two parts",
                    "It indicates that 105 is smaller than 15"
                ],
                "ans": "It acts as a placeholder showing there are 0 tens",
                "explanation": "Zero holds the tens place empty, keeping the 1 in the hundreds place so 105 is not confused with 15."
            },
            {
                "q": "What ancient Indian word was originally used for zero, signifying emptiness or void?",
                "options": [
                    "Shunya",
                    "Rupa",
                    "Gana",
                    "Dhan"
                ],
                "ans": "Shunya",
                "explanation": "Ancient Indian mathematicians used the word 'shunya', meaning void or empty, for zero."
            }
        ]
    },
    {
        "id": 4,
        "title": "Marketplace Estimation Counting",
        "badge": "Real-World Counting",
        "sim_id": "sim_marketplace_counting",
        "description": "Practice visual estimation and systematic grouping by tens to count fruits, sweets, and bangles in a bustling marketplace scene.",
        "speech": (
            "Step into the vibrant village marketplace, where sweet aromas and colorful displays offer a feast for numerical estimation! "
            "A bustling bazaar stall displays piles of golden oranges, rows of sparkling glass bangles, trays of round laddoos, and diamond-shaped barfis. "
            "When confronted with a large, scattered collection of items, counting them one by one is slow and easily interrupted. "
            "A skilled mathematician uses two powerful strategies: first visual estimation, followed by systematic grouping! "
            "Estimation means making a thoughtful, sensible judgment of quantity without immediate exact counting. "
            "Looking at a tray of delicious laddoos, you might estimate around fifty pieces based on how tightly they are packed. "
            "To verify your estimate accurately, you organize the laddoos into neat rows of ten. "
            "Counting by tens is remarkably fast: ten, twenty, thirty, forty, fifty! "
            "If five loose laddoos remain after forming five full tens, the exact total is fifty plus five, which equals fifty-five. "
            "The same practical technique applies to bunches of sweet yellow bananas and packets of circular forehead bindis. "
            "Grouping everyday goods into packets of ten transforms chaotic heaps into organized, easily tallyable collections that save time and eliminate guesswork. "
            "Regular estimation combined with decimal grouping sharpens number intuition and boosts real-world mathematical confidence during shopping and counting tasks."
        ),
        "checkpoints": [
            {
                "q": "If a sweet shop vendor arranges laddoos into 6 full plates of 10 and has 4 loose laddoos, what is the total count?",
                "options": [
                    "64 laddoos (60 + 4)",
                    "46 laddoos",
                    "24 laddoos",
                    "604 laddoos"
                ],
                "ans": "64 laddoos (60 + 4)",
                "explanation": "6 plates of 10 equal 60 laddoos; adding the 4 loose laddoos gives 60 + 4 = 64."
            },
            {
                "q": "Why is estimating and grouping by tens more effective than counting scattered items one by one?",
                "options": [
                    "It organizes messy heaps into rapid skip-counting groups of ten",
                    "It changes the actual number of items",
                    "It makes the fruits weigh less",
                    "It is the only method permitted in markets"
                ],
                "ans": "It organizes messy heaps into rapid skip-counting groups of ten",
                "explanation": "Grouping by tens allows rapid skip-counting (10, 20, 30...) and drastically reduces counting mistakes."
            }
        ]
    },
    {
        "id": 5,
        "title": "Snakes Ladders Grid",
        "badge": "Century Board",
        "sim_id": "sim_snakes_ladders_grid",
        "description": "Analyze the classic 1 to 100 hundred-square board game grid to trace numerical paths, ladders, snakes, and coordinate increments.",
        "speech": (
            "One of the most beloved board games in history, Snakes and Ladders, was invented in ancient India as 'Moksha Patam' to teach mathematics and ethics! "
            "The game board is a magnificent ten-by-ten square grid containing exactly one hundred numbered tiles, running from one up to one hundred. "
            "The board is structured in alternating rows of ten numbers: "
            "row one progresses from one to ten; row two snakes backward from eleven to twenty; row three advances from twenty-one to thirty, and so forth! "
            "This grid layout provides a perfect visual representation of our decimal base-ten place-value system. "
            "Moving one tile directly to the right adds one single unit; "
            "jumping directly one square vertically upward adds ten units, representing a full ten-bundle jump! "
            "For instance, stepping from tile twenty-four directly up to thirty-four increases the count by exactly ten. "
            "When a player lands on the bottom of a helpful ladder at tile twenty-eight, they might climb swiftly to eighty-four! "
            "Conversely, sliding down a coiled snake from tile ninety-eight drops the token down to seventy-nine. "
            "Every roll of the die presents a new calculation, helping learners estimate distances and plan winning turns. "
            "Navigating this classic century board actively reinforces mental addition, subtraction, place-value coordination, and rapid pattern recognition across one hundred numbers."
        ),
        "checkpoints": [
            {
                "q": "On a standard 1 to 100 hundred-grid board, what arithmetic change occurs when moving one square vertically upward?",
                "options": [
                    "The number increases by 10",
                    "The number increases by 1",
                    "The number is doubled",
                    "The number decreases by 5"
                ],
                "ans": "The number increases by 10",
                "explanation": "Each row contains 10 numbers, so moving straight up to the next row adds exactly 10."
            },
            {
                "q": "If your playing token is resting on square 45, what square will you reach after a direct jump of 10 more?",
                "options": [
                    "Square 55 (45 + 10)",
                    "Square 46",
                    "Square 50",
                    "Square 35"
                ],
                "ans": "Square 55 (45 + 10)",
                "explanation": "Adding 10 to 45 results in 45 + 10 = 55."
            }
        ]
    },
    {
        "id": 6,
        "title": "The Talking Pot",
        "badge": "Sequential Increment",
        "sim_id": "sim_talking_pot_increment",
        "description": "Interact with the magical Talking Pot to explore successive increment rules, number neighbors, and immediate successors.",
        "speech": (
            "Let us now play an enchanting mathematical thinking game featuring a mystical clay vessel known as the Talking Pot! "
            "In this lively classroom activity, the Talking Pot possesses a magical mathematical rule: "
            "whenever a number is dropped into its enchanted spout, the pot immediately speaks out the exact successor number: 'plus one'! "
            "For example, if you whisper the number thirty-four into the pot, it rings out with a chime: 'thirty-five'! "
            "If you drop seventy-nine into the pot, it announces: 'eighty'! "
            "This sequential incrementing teaches young learners the foundational arithmetic concept of consecutive numbers and successors. "
            "Every whole number has an immediate predecessor, which is one less, and an immediate successor, which is one more. "
            "The Talking Pot becomes particularly exciting when approaching milestone numbers. "
            "What happens when you whisper ninety-nine into the vessel? "
            "Ninety-nine consists of nine tens and nine ones. "
            "When the Talking Pot adds one more single unit, nine ones become ten ones, which bundle together into a brand-new ten! "
            "Now we have ten full tens, which form a magnificent milestone: one hundred! "
            "The Talking Pot joyfully announces: 'one hundred'! "
            "Playing with numerical successors trains rapid mental addition and illuminates how multi-digit transitions occur smoothly."
        ),
        "checkpoints": [
            {
                "q": "What successor number will the Talking Pot announce when the number 99 is dropped into it?",
                "options": [
                    "100 (One Hundred)",
                    "90",
                    "101",
                    "98"
                ],
                "ans": "100 (One Hundred)",
                "explanation": "The Talking Pot adds 1: 99 + 1 = 100."
            },
            {
                "q": "What is the relationship between any whole number and its successor?",
                "options": [
                    "The successor is exactly 1 greater than the number",
                    "The successor is 10 times larger",
                    "The successor is 1 less than the number",
                    "The successor is always an even number"
                ],
                "ans": "The successor is exactly 1 greater than the number",
                "explanation": "By definition, the successor of any whole number n is n + 1 (exactly one more)."
            }
        ]
    },
    {
        "id": 7,
        "title": "Defining One Hundred",
        "badge": "Century Milestone",
        "sim_id": "sim_defining_hundred",
        "description": "Examine multiple physical and cultural representations of 100: cricket centuries, matchstick bundles, and currency notes.",
        "speech": (
            "Reaching the milestone of one hundred is a glorious celebration in mathematics, sports, and daily life! "
            "In cricket, when a batsman scores one hundred runs, the stadium erupts in cheers to celebrate a magnificent 'century'! "
            "The very word 'century' comes from the Latin root 'centum', meaning exactly one hundred. "
            "Let us explore how one hundred can be defined and visualized through diverse physical models. "
            "First, arithmetic: one hundred is exactly one more than ninety-nine. "
            "Second, place-value bundles: take ten wooden matchsticks and tie them with a rubber band to form one ten-bundle. "
            "Assemble ten of these bundles together: ten, twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety, one hundred! "
            "Ten bundles of ten make one solid hundred! "
            "Third, marketplace goods: ten packets containing ten circular forehead bindis each contain one hundred bindis in total. "
            "Fourth, currency: a crisp one-hundred-rupee banknote equals ten ten-rupee notes or one hundred single one-rupee coins. "
            "In written numerals, one hundred is written as a three-digit figure: 1-0-0. "
            "This notation explicitly records: one hundred in the third column, zero tens in the middle column, and zero ones in the first column! "
            "Recognizing 100 across varied real-world representations solidifies foundational number sense."
        ),
        "checkpoints": [
            {
                "q": "How many bundles of 10 matchsticks are required to make exactly 100 matchsticks?",
                "options": [
                    "10 bundles of 10",
                    "5 bundles of 10",
                    "100 bundles of 10",
                    "20 bundles of 10"
                ],
                "ans": "10 bundles of 10",
                "explanation": "10 bundles multiplied by 10 sticks per bundle equals 100 sticks (10 x 10 = 100)."
            },
            {
                "q": "What does the digit 1 in the three-digit number 100 represent?",
                "options": [
                    "1 group of one hundred",
                    "1 single loose unit",
                    "1 group of ten",
                    "1 zero"
                ],
                "ans": "1 group of one hundred",
                "explanation": "In 100, the 1 is in the hundreds column, representing 1 group of 100."
            }
        ]
    },
    {
        "id": 8,
        "title": "Making One Hundred",
        "badge": "Additive Pairs",
        "sim_id": "sim_making_hundred_pairs",
        "description": "Construct additive combinations totaling 100 using bead strings, number line jumps, and complementary number sentences.",
        "speech": (
            "Now that we understand the landmark value of one hundred, let us discover the many beautiful ways to assemble it! "
            "In mathematics, pairs of numbers that join together to equal a target total are called complementary pairs. "
            "Finding number pairs that total one hundred is an essential mental arithmetic skill that unlocks rapid problem solving. "
            "Consider a calibrated bead string called a 'ginladi', which contains one hundred beads arranged in alternating red and white groups of ten. "
            "If you slide sixty beads to the left side, how many beads remain on the right side? "
            "Forty beads! Therefore, sixty plus forty equals one hundred! "
            "Let us test another split: slide seventy-five beads to the left. "
            "To reach one hundred, you need twenty-five more: seventy-five plus twenty-five equals one hundred! "
            "We can also visualize making one hundred using two-stage hops along a number line. "
            "Imagine taking a long jump from zero up to sixty-five. "
            "How many units must you hop forward to land precisely on one hundred? "
            "First jump five units to reach seventy, then jump thirty more units to arrive at one hundred! "
            "Thirty plus five equals thirty-five, proving that sixty-five plus thirty-five equals one hundred! "
            "Practicing complementary pairs to one hundred builds effortless mental calculation dexterity."
        ),
        "checkpoints": [
            {
                "q": "What number must be added to 65 to make exactly 100 (65 + ___ = 100)?",
                "options": [
                    "35",
                    "45",
                    "25",
                    "30"
                ],
                "ans": "35",
                "explanation": "65 + 5 = 70, and 70 + 30 = 100. Adding the two jumps: 30 + 5 = 35."
            },
            {
                "q": "Which of the following number pairs sums to exactly 100?",
                "options": [
                    "70 and 30",
                    "60 and 50",
                    "80 and 30",
                    "40 and 50"
                ],
                "ans": "70 and 30",
                "explanation": "70 + 30 = 100. The others sum to 110, 110, and 90."
            }
        ]
    }
]

if __name__ == "__main__":
    print("=== VERIFYING SLIDES 1 TO 8 ===")
    assert len(slides_part1) == 8

    for s in slides_part1:
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

    print("Part 1 verified successfully!")
