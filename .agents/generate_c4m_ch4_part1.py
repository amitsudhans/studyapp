# -*- coding: utf-8 -*-
"""
Generate Slides 1 to 8 for Class 4 Maths Chapter 4: Thousands Around Us
Calibrated strictly to 195-215 words per speech.
"""

def get_part1_slides():
    return [
        {
            "id": 1,
            "title": "Community Kitchen Numbers",
            "section": "Introductory Narrative & Community Service",
            "speech": (
                "Welcome to our mathematics laboratory. Today we explore the world of large numbers, focusing on one thousand and beyond. "
                "Consider a vibrant community kitchen where caring volunteers gather at a community Gurudwara to prepare a free communal lunch. "
                "The organizers plan to serve nourishing hot meals to approximately one thousand visitors, supported by fifty-five dedicated volunteers. "
                "To prepare such a grand feast, generous donations of raw food supplies arrive at the pantry. Volunteers record each delivery "
                "using two-digit and three-digit numbers. For example, the storekeeper logs forty-five kilograms of whole wheat flour, sixty-eight kilograms "
                "of fragrant rice, thirty-two liters of mustard cooking oil, and two hundred forty kilograms of fresh seasonal vegetables. "
                "We represent these quantities using place value columns: Ones, Tens, and Hundreds. In the number two hundred forty, the digit two "
                "represents two hundreds, four represents four tens, and zero represents zero ones. Expanded addition expresses this as two hundred "
                "plus forty plus zero. Tracking ingredient weights reinforces our understanding of place value while managing massive community cooking efforts. "
                "Every bag of grain and container of oil connects arithmetic to community service. "
                "Use the interactive pantry inventory below to inspect donation sacks and practice writing expanded place-value expressions."
            ),
            "checkpoints": [
                {
                    "q": "What is the expanded addition form of 240 kilograms of vegetables?",
                    "options": ["20 + 40 + 0", "200 + 4 + 0", "200 + 40 + 0", "200 + 40 + 4"],
                    "ans": 2,
                    "exp": "In 240, there are 2 Hundreds (200), 4 Tens (40), and 0 Ones (0). Thus, 200 + 40 + 0 = 240."
                },
                {
                    "q": "If 55 volunteers are joined by 38 more helpers, what is the new total volunteer count?",
                    "options": ["83 volunteers", "93 volunteers", "95 volunteers", "103 volunteers"],
                    "ans": 1,
                    "exp": "55 + 38 = (50 + 30) + (5 + 8) = 80 + 13 = 93 volunteers."
                }
            ]
        },
        {
            "id": 2,
            "title": "Attendance Block Tracker",
            "section": "Time Slots & Attendance Tracking",
            "speech": (
                "Managing a large community event requires monitoring visitor flow across various time intervals. In our community dining hall, "
                "volunteers track attendance using Hundreds, Tens, and Ones block diagrams across four distinct service shifts. "
                "During the opening morning slot from eleven to twelve, fifty-two guests arrive. The attendance tracker represents this using zero hundreds, "
                "five ten-rods, and two single unit cubes. During the peak afternoon shift from twelve to one, a large crowd of three hundred twenty-five "
                "people are seated. Here, three flat hundred-squares, two ten-rods, and five unit cubes visually model the crowd. "
                "In the late afternoon shift from one to two, attendance reaches its absolute peak with five hundred eight diners. "
                "Notice that five hundred eight has five hundreds, zero tens, and eight ones. The zero tens digit must never be skipped, because it holds "
                "the tens place and keeps the five in the hundreds column. Finally, during the evening slot, one hundred forty-five guests visit. "
                "Comparing the slots reveals that the one to two afternoon shift had peak attendance, while the morning shift had lowest turnout. "
                "Explore the interactive attendance monitor below to toggle between time slots and construct three-digit place value block models."
            ),
            "checkpoints": [
                {
                    "q": "How is the number 508 represented in Hundreds, Tens, and Ones blocks?",
                    "options": ["5 Hundreds, 8 Tens, 0 Ones", "5 Hundreds, 0 Tens, 8 Ones", "50 Hundreds, 8 Ones", "5 Tens, 8 Ones"],
                    "ans": 1,
                    "exp": "508 has 5 in the Hundreds place, 0 in the Tens place, and 8 in the Ones place."
                },
                {
                    "q": "Which attendance count is greater: the afternoon crowd of 325 or the late shift of 508?",
                    "options": ["325 is greater", "508 is greater", "Both are equal", "Cannot be determined"],
                    "ans": 1,
                    "exp": "Comparing the Hundreds digits, 5 Hundreds (508) is greater than 3 Hundreds (325). Thus, 508 > 325."
                }
            ]
        },
        {
            "id": 3,
            "title": "Creating Ordering Numbers",
            "section": "Digit Manipulation & Skip Counting",
            "speech": (
                "Let us now explore digit manipulation puzzles to understand how place-value positioning dramatically alters numerical magnitude. "
                "Suppose you are given five number cards displaying the digits: three, seven, five, zero, and eight. Your challenge is to select "
                "any three cards to construct distinct three-digit numbers. To assemble the largest possible three-digit value, we must place "
                "the greatest available digit in the highest place-value position. Choosing eight for the hundreds place, seven for the tens place, "
                "and five for the ones place yields eight hundred seventy-five. To assemble the smallest valid three-digit value, zero cannot "
                "occupy the hundreds place because that would create a two-digit number. Therefore, we place the smallest non-zero digit, three, "
                "in the hundreds place, followed by zero in the tens place, and five in the ones place, producing three hundred five. "
                "Now consider a special condition: build three-digit numbers that remain strictly under five hundred fifty. "
                "Valid examples include three hundred seventy-eight, three hundred eighty-seven, and five hundred thirty-seven. "
                "Changing the position of digits reshapes value while reinforcing the critical power of positional place notation. "
                "Experiment with the interactive digit card builder below to assemble, order, and filter three-digit numbers under specified conditions."
            ),
            "checkpoints": [
                {
                    "q": "Using the digits 4, 9, and 1 without repetition, what is the largest 3-digit number you can form?",
                    "options": ["491", "914", "941", "194"],
                    "ans": 2,
                    "exp": "Place digits in descending order: 9 in Hundreds, 4 in Tens, and 1 in Ones gives 941."
                },
                {
                    "q": "Which of the following 3-digit numbers formed from digits 3, 7, 5 is strictly under 550?",
                    "options": ["735", "753", "573", "537"],
                    "ans": 3,
                    "exp": "537 is less than 550, whereas 573, 735, and 753 are all greater than 550."
                }
            ]
        },
        {
            "id": 4,
            "title": "Number Line Skips",
            "section": "Digit Manipulation & Skip Counting",
            "speech": (
                "The number line is an essential geometric tool that visualizes relative distance, magnitude, and arithmetic sequences. "
                "Imagine a segmented number line stretching from two hundred to six hundred, marked with major milestone intervals of fifty units. "
                "When we plot three-digit numbers on this line, their physical positions correspond directly to their numerical values. "
                "For instance, three hundred five sits just past the three hundred mark, while three hundred seventy-five sits midway between "
                "three hundred fifty and four hundred. Number lines also help us master skip-counting forward and backward by ones, tens, and hundreds. "
                "When skip-counting forward by tens starting from three hundred forty, only the tens digit increases by one while the ones digit stays constant: "
                "three hundred forty, three hundred fifty, three hundred sixty, three hundred seventy, and three hundred eighty. "
                "If we skip-count backward by tens from five hundred twenty, the tens column decreases step by step: five hundred ten, five hundred, "
                "four hundred ninety, and four hundred eighty. Notice the transition from five hundred to four hundred ninety, where regrouping across hundreds occurs. "
                "Visualizing numbers as progressive steps along an ordered track strengthens our intuitive feel for distances between quantities. "
                "Step into the interactive number line simulator below to slide markers and practice rhythmic skip-counting forward and backward."
            ),
            "checkpoints": [
                {
                    "q": "What is the next number in the skip-counting sequence: 460, 470, 480, 490, ___?",
                    "options": ["491", "495", "500", "510"],
                    "ans": 2,
                    "exp": "Adding 10 to 490 gives: 490 + 10 = 500."
                },
                {
                    "q": "If you skip-count backward by 10s starting from 310, what is the third number you recite?",
                    "options": ["300", "290", "280", "270"],
                    "ans": 1,
                    "exp": "Starting at 310: first step backward is 300, second step is 290."
                }
            ]
        },
        {
            "id": 5,
            "title": "Indian System History",
            "section": "Indian Number System & Counting Beyond 1000",
            "speech": (
                "The base-ten positional number system used worldwide today is one of India's greatest historical gifts to human civilization. "
                "Developed by ancient Indian scholars over two thousand years ago, this revolutionary mathematical invention relies on just ten distinct symbols: "
                "zero, one, two, three, four, five, six, seven, eight, and nine. Before this breakthrough, ancient civilizations used cumbersome numeral tallies "
                "where writing large numbers required endless repetitive marks. The Indian system introduced two fundamental concepts working together: "
                "place value and zero as an active placeholder. In this system, the value of every digit depends entirely on its position within the number. "
                "Each step to the left increases a digit's value by a multiple of ten. A digit five in the ones place represents five single units, "
                "in the tens place it represents fifty, in the hundreds place five hundred, and in the thousands place five thousand. "
                "Because of this multiplicative structure, these ten humble symbols can express numbers of any magnitude, from tiny fractions to astronomical cosmic distances. "
                "Global commerce, modern science, and digital computing all trace their foundational numerical language to this elegant Indian discovery. "
                "Explore the historical timeline and interactive base-ten symbol matrix below to observe how positional notation unlocked universal arithmetic power."
            ),
            "checkpoints": [
                {
                    "q": "How many fundamental symbols (digits) are used in the Indian base-10 place-value system?",
                    "options": ["5 symbols", "9 symbols", "10 symbols (0 to 9)", "100 symbols"],
                    "ans": 2,
                    "exp": "The base-10 decimal system uses exactly 10 symbols: 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9."
                },
                {
                    "q": "What happens to the value of a digit each time it moves one place to the left?",
                    "options": ["It increases by 1", "It multiplies by 10", "It divides by 10", "It stays the same"],
                    "ans": 1,
                    "exp": "In a base-10 positional system, moving one column to the left multiplies the digit's place value by 10."
                }
            ]
        },
        {
            "id": 6,
            "title": "Entering Four Digits",
            "section": "Indian Number System & Counting Beyond 1000",
            "speech": (
                "What happens when we count past nine hundred ninety-nine? Let us trace visitor counts entering our community hall as they cross "
                "this historic threshold. Imagine a counter tracking guests sequentially: nine hundred ninety-six, nine hundred ninety-seven, "
                "nine hundred ninety-eight, and nine hundred ninety-nine. At nine hundred ninety-nine, every available column is maxed out: "
                "nine hundreds, nine tens, and nine ones. When the very next visitor enters, we add one more unit. Nine ones plus one unit equals ten ones, "
                "which bundles into one ten. Nine tens plus that one ten equals ten tens, which bundles into one hundred. "
                "Nine hundreds plus that one hundred equals ten hundreds. Ten hundreds cannot fit in the three-digit frame! "
                "A brand-new fourth column is born on the left: the Thousands column! We write this milestone number as one, zero, zero, zero: one thousand. "
                "The count continues seamlessly into four digits: one thousand one, one thousand two, up through one thousand one hundred. "
                "One thousand is the smallest four-digit number, standing as the grand gateway to a wider mathematical universe. "
                "Crossing into four digits opens vast horizons for measuring town populations, factory outputs, and historical eras. "
                "Use the interactive tally counter below to click from 995 to 1005 and watch the fourth digit column unlock."
            ),
            "checkpoints": [
                {
                    "q": "What is the smallest 4-digit whole number?",
                    "options": ["999", "1000", "1001", "1100"],
                    "ans": 1,
                    "exp": "1000 is the smallest 4-digit number. 999 is the largest 3-digit number."
                },
                {
                    "q": "What number comes immediately after 1009 in sequential counting?",
                    "options": ["1010", "1019", "1090", "1100"],
                    "ans": 0,
                    "exp": "Adding 1 to 1009 gives: 1009 + 1 = 1010 (one thousand ten)."
                }
            ]
        },
        {
            "id": 7,
            "title": "Real World Thousands",
            "section": "1000s Around Us & Did You Know?",
            "speech": (
                "Numbers in the thousands surround us in history, nature, geography, and Indian culture. Once we recognize four-digit numbers, "
                "we begin seeing them everywhere. Consider magnificent Indian architecture: in Moodubidiri, Karnataka, stands the celebrated "
                "Saavira Kambada Basadi, a temple built in the fifteen hundreds famously supported by exactly one thousand intricately carved granite pillars! "
                "In wildlife conservation, four-digit numbers measure remarkable ecological recoveries. The Indian one-horned rhinoceros population in Assam "
                "grew from a critically low two hundred animals to over four thousand majestic rhinos today. An adult male rhino weighs between "
                "one thousand eight hundred and two thousand seven hundred kilograms! Across Indian geography, four-digit numbers capture massive scale: "
                "India possesses over seven thousand five hundred kilometers of scenic ocean coastline, more than five thousand years of continuous civilizational heritage, "
                "and celebrates over one thousand cultural festivals across seven hundred eighty-eight administrative districts. "
                "Developing scale estimation helps us judge magnitude: a classroom has tens of chairs, a textbook has hundreds of pages, "
                "while an ancient banyan tree shelters thousands of green leaves. "
                "Connecting mathematics to geographic landmarks and living creatures makes large numbers vivid, relatable, and deeply memorable. "
                "Explore the interactive map of Indian heritage below to discover four-digit facts across wildlife sanctuaries and historic monuments."
            ),
            "checkpoints": [
                {
                    "q": "Which of the following real-world quantities is best measured in the thousands?",
                    "options": ["Teachers in a single classroom", "Pencils in a pencil box", "Pages in a small comic", "Leaves on a large banyan tree"],
                    "ans": 3,
                    "exp": "A large banyan tree easily has tens of thousands of leaves, well within the thousands scale."
                },
                {
                    "q": "The Saavira Kambada Basadi temple in Karnataka is famous for having how many pillars?",
                    "options": ["100 pillars", "500 pillars", "1000 pillars", "5000 pillars"],
                    "ans": 2,
                    "exp": "The temple is renowned as the 'Thousand Pillars Temple' because it contains exactly 1000 stone pillars."
                }
            ]
        },
        {
            "id": 8,
            "title": "Base Ten Blocks",
            "section": "One Thousand (1000)",
            "speech": (
                "To truly understand the physical magnitude of one thousand, we turn to base-ten blocks, an elegant visual model developed "
                "by mathematics educators. This tactile model builds understanding step by step using physical geometry. "
                "We begin with a single tiny cube called a unit, representing one. When we line up ten units side by side, they snap together into a rod, "
                "representing one ten. When we take ten rods and place them side by side, they form a flat square mat containing one hundred units, "
                "representing one hundred. Finally, when we stack ten flat hundred-mats on top of each other, they assemble into a massive three-dimensional cube! "
                "This large cube contains ten hundred-flats, which equals one hundred ten-rods, which equals exactly one thousand individual unit cubes! "
                "Notice the beautiful power of ten progression: ten ones make one ten, ten tens make one hundred, and ten hundreds make one thousand. "
                "Each new dimension expands tenfold: point to line, line to square, square to solid cube. "
                "Physical block models ground abstract place-value columns into tangible spatial volumes that every young learner can visualize clearly. "
                "Use the interactive 3D block laboratory below to stack ten flat hundred-sheets and watch them fuse into a solid one-thousand block."
            ),
            "checkpoints": [
                {
                    "q": "How many flat hundred-blocks are stacked together to form 1 thousand-cube?",
                    "options": ["5 flats", "10 flats", "50 flats", "100 flats"],
                    "ans": 1,
                    "exp": "10 hundred-flats stacked vertically form 1 thousand-cube (10 × 100 = 1000)."
                },
                {
                    "q": "How many ten-rods are contained within a complete one-thousand cube?",
                    "options": ["10 ten-rods", "50 ten-rods", "100 ten-rods", "1000 ten-rods"],
                    "ans": 2,
                    "exp": "Since 1 hundred = 10 ten-rods, 10 hundreds = 10 × 10 = 100 ten-rods in 1 thousand."
                }
            ]
        }
    ]

if __name__ == '__main__':
    slides = get_part1_slides()
    for s in slides:
        words = len(s['speech'].split())
        print(f"Slide {s['id']}: {s['title']} -> Word count: {words}")
        assert 195 <= words <= 215, f"Slide {s['id']} word count {words} outside 195-215 range!"
    print("All slides 1-8 pass word count validation!")
