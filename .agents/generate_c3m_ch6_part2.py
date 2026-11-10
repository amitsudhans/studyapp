# -*- coding: utf-8 -*-
"""Part 2 (Slides 9-16) for Class 3 Mathematics Chapter 6: House of Hundreds - 1."""

import json
import re

slides_part2 = [
    {
        "id": 9,
        "title": "Advancing Four Hundred",
        "badge": "Century Distances",
        "sim_id": "sim_advancing_four_hundred",
        "description": "Plot three-digit values on an extended number line toward four hundred and calculate the exact distance to the next century milestone.",
        "speech": (
            "As our mathematical exploration expands, we journey boldly into the fourth century of numbers, marching steadily toward the milestone of four hundred. "
            "Consider specific numbers positioned along this advancing highway, such as two hundred and sixteen, two hundred and forty-three, three hundred "
            "and twenty-nine, and three hundred and eighty-seven. Locating three hundred eighty-seven on our line reveals an intriguing question: how far "
            "is this number from the upcoming milestone of four hundred? By analyzing place value, we can calculate the distance in two smooth mental steps! "
            "First, jump three units forward from three hundred eighty-seven to reach the neat decade anchor landmark of three hundred and ninety. Next, leap from "
            "three hundred ninety to four hundred, which requires exactly ten more units. Combining both jumps—three plus ten—proves that three hundred "
            "eighty-seven is precisely thirteen units away from four hundred! This powerful complement calculation technique is immensely useful in everyday commerce, "
            "measuring physical travel distances, and tracking personal goals. Every three-digit number has an exact mathematical gap separating it from the "
            "next hundred milestone. Interact with the distance gauge in our simulator to plot numbers like three hundred twenty-nine and calculate their gaps to four hundred right now!"
        ),
        "checkpoints": [
            {
                "q": "How far is the number 387 from the next hundred milestone of 400?",
                "options": ["13 units", "23 units", "17 units", "3 units"],
                "ans": "13 units",
                "explanation": "387 + 13 = 400, so the distance is 13 units."
            },
            {
                "q": "Which landmark hundred comes immediately after 399?",
                "options": ["400", "300", "500", "390"],
                "ans": "400",
                "explanation": "Adding 1 to 399 gives 400, the fourth hundred milestone."
            }
        ]
    },
    {
        "id": 10,
        "title": "Sweet Shop Inventory",
        "badge": "Counting Past 400",
        "sim_id": "sim_sweet_shop_inventory",
        "description": "Manage bakery trays grouped in hundreds of mysore pak, laddoos, and dhoklas to count past four hundred up to five hundred.",
        "speech": (
            "Step inside a bustling traditional sweet shop where grand trays of golden mysore pak, round besan laddoos, and steamed savory dhoklas "
            "stand arranged in mouthwatering festive displays! To manage this massive culinary inventory, the confectioners pack sweets into standardized trays "
            "holding exactly one hundred pieces each. When we count four large trays of laddoos resting together, we have four hundred laddoos. Add two boxes of ten "
            "and three loose sweets, and the inventory reaches four hundred and twenty-three sweets! Nearby, a fresh hot delivery of savory dhoklas brings four full "
            "trays plus eight boxes of ten and seven singles, totaling four hundred and eighty-seven items. By grouping items into hundreds, tens, and ones, the "
            "shop easily tracks inventory past four hundred and thirty-eight, four hundred and seventy-six, and onwards toward larger goals. Finally, when five full "
            "master trays of sweets sit side by side on the main counter, we cross the magnificent threshold of five hundred sweets! Five hundred represents five hundred "
            "individual loose pieces, fifty bundles of ten, or five full hundreds united together. Practice packing sweet trays in our interactive bakery simulator "
            "to master counting toward five hundred with absolute confidence and speed today!"
        ),
        "checkpoints": [
            {
                "q": "What total number of sweets is represented by 4 trays of 100, 8 boxes of 10, and 7 loose sweets?",
                "options": ["487 sweets", "478 sweets", "480 sweets", "587 sweets"],
                "ans": "487 sweets",
                "explanation": "400 + 80 + 7 = 487 sweets."
            },
            {
                "q": "How many full trays of 100 sweets are needed to make 500 sweets in total?",
                "options": ["5 trays", "4 trays", "50 trays", "10 trays"],
                "ans": "5 trays",
                "explanation": "5 × 100 = 500 sweets."
            }
        ]
    },
    {
        "id": 11,
        "title": "Apartment Grid Navigation",
        "badge": "10-Column Multi-Floor Grid",
        "sim_id": "sim_apartment_grid_navigation",
        "description": "Navigate a 10-column multi-floor residential building grid to discover that moving one floor up adds 10, while one floor down subtracts 10.",
        "speech": (
            "Welcome to Hop Hundreds Home, a modern ten-story apartment building where residential house numbers are laid out across a structured ten-column grid. "
            "Each horizontal row represents one residential floor, and each vertical column aligns apartments ending in the exact same unit digit. On the ground "
            "floor, apartments are numbered sequentially from one hundred and one to one hundred and ten. Look closely at what happens when you take the elevator "
            "up to the next floor directly above apartment one hundred and five! You land at apartment one hundred and fifteen. Going one floor higher brings you "
            "to apartment one hundred and twenty-five. Moving exactly one floor upward always adds ten to the house number, because each floor holds ten homes! "
            "Conversely, moving one floor downward always subtracts ten from the house number. Moving one door to the right adds one unit, while moving one door to "
            "the left subtracts one unit. Understanding this two-dimensional coordinate structure allows postal delivery workers to locate any apartment swiftly "
            "without manual counting. Test your grid navigation skills in our simulator by plotting delivery routes to apartments like two hundred and nine, two "
            "hundred twenty-eight, and two hundred forty-two right now!"
        ),
        "checkpoints": [
            {
                "q": "In a 10-column apartment grid, what house number is located exactly one floor above apartment 105?",
                "options": ["115", "106", "125", "104"],
                "ans": "115",
                "explanation": "Moving one floor up in a 10-column grid adds 10: 105 + 10 = 115."
            },
            {
                "q": "What mathematical operation corresponds to moving one floor directly downward on the building grid?",
                "options": ["Subtracting 10", "Adding 10", "Subtracting 1", "Adding 100"],
                "ans": "Subtracting 10",
                "explanation": "Each lower floor is 10 units less, so moving down one floor subtracts 10."
            }
        ]
    },
    {
        "id": 12,
        "title": "Mystery House Clues",
        "badge": "Structural Coordinate Deduction",
        "sim_id": "sim_mystery_house_clues",
        "description": "Deduce secret 3-digit house numbers from multi-floor building grid clues using floor numbers, column digits, and adjacent neighbors.",
        "speech": (
            "Step into the role of a master building detective to solve intriguing structural coordinate riddles known as Mystery House Clues in our apartment complex! "
            "Consider this riddle: 'I am located on the fourth floor of Jump Joy Residency. My column ends in the digit seven. What apartment am I?' Since the "
            "fourth floor houses the forty-decade, and the vertical column specifies seven ones, you are definitely apartment two hundred and forty-seven on that level! Let us try another "
            "challenging riddle together: 'I am located exactly between apartment two hundred thirty-one and two hundred thirty-three, directly below apartment "
            "two hundred forty-two on the grid. Who am I?' Being situated directly between two hundred thirty-one and two hundred thirty-three points unerringly to two hundred "
            "thirty-two. We can double check this using the vertical column clue: two hundred forty-two minus ten equals two hundred thirty-two, confirming our deduction "
            "flawlessly without any doubt! By synthesizing clues from horizontal floor neighbors and vertical column alignments, we solve complex three-digit spatial puzzles with "
            "logical confidence and great mathematical joy. Play the mystery house deduction game in our simulator to uncover all secret resident numbers across the "
            "entire building grid with complete mastery and fun!"
        ),
        "checkpoints": [
            {
                "q": "Which apartment is located directly between 231 and 233 on the same floor?",
                "options": ["232", "230", "242", "222"],
                "ans": "232",
                "explanation": "The consecutive integer between 231 and 233 is 232."
            },
            {
                "q": "If an apartment is on the 200s block, 5th floor (50s decade), and column 8, what is its number?",
                "options": ["258", "285", "250", "268"],
                "ans": "258",
                "explanation": "2 hundreds + 5 tens + 8 ones = 258."
            }
        ]
    },
    {
        "id": 13,
        "title": "Dienes Block Models",
        "badge": "Base-10 Concrete Models",
        "sim_id": "sim_dienes_block_models",
        "description": "Construct three-digit numbers using Dienes base-10 blocks: hundred flats, ten rods, and unit cubes across H-T-O columns.",
        "speech": (
            "In mathematics, Dienes blocks provide a crystal-clear concrete physical representation of our base-ten decimal system in action. A small individual wooden "
            "cube represents one single unit, or one in the primary ones column. When ten unit cubes are glued together in a straight row, they form a ten-rod "
            "representing ten. When ten rods are joined side by side, they form a broad square flat representing one hundred units! Now, let us build the "
            "number three hundred and forty-two together using these modular blocks. We place three large hundred flats in the hundreds column, four slender rods "
            "in the tens column, and two tiny unit cubes in the ones column. Look closely at the expanded numerical sentence: three hundred plus forty plus two "
            "equals three hundred and forty-two! If we add one more flat, the number becomes four hundred and forty-two. If we remove two rods, the quantity becomes "
            "four hundred and twenty-two. Dienes blocks make abstract place value tangible, proving that every digit in a three-digit number indicates how "
            "many flats, rods, or units are present. Use our interactive Dienes block workshop on screen to build, modify, and inspect three-digit numbers with "
            "complete confidence and skill today!"
        ),
        "checkpoints": [
            {
                "q": "What number is modeled by 3 hundred flats, 4 ten rods, and 2 unit cubes?",
                "options": ["342", "324", "432", "340"],
                "ans": "342",
                "explanation": "3 flats (300) + 4 rods (40) + 2 units (2) = 342."
            },
            {
                "q": "How many ten rods are needed to make a single hundred flat?",
                "options": ["10 rods", "5 rods", "100 rods", "20 rods"],
                "ans": "10 rods",
                "explanation": "Ten rods of ten units each form one hundred flat: 10 × 10 = 100."
            }
        ]
    },
    {
        "id": 14,
        "title": "Number Hunt Patterns",
        "badge": "Digit Pattern Search",
        "sim_id": "sim_number_hunt_patterns",
        "description": "Scan three-digit ranges between 200 and 300 to discover numbers containing specific digits in ones, tens, or hundreds places.",
        "speech": (
            "Welcome to the exciting Number Hunt challenge, where we search through wide number ranges to identify values that satisfy specific digit criteria! "
            "Suppose we examine all numbers between two hundred and three hundred to find every single number that contains the digit five. Where across our "
            "place value columns can the digit five appear? First, it can appear in the ones column: two hundred and five, two hundred and fifteen, two hundred twenty-five, thirty-five, "
            "forty-five, and so on, all the way to two hundred and ninety-five. That gives ten numbers ending in five! Next, look at the central tens column: the "
            "entire decade of the fifties—two hundred fifty, two hundred fifty-one, through two hundred fifty-nine—contains five in the tens place! Notice that "
            "two hundred and fifty-five contains a five in both the tens and ones places. Conducting structured number hunts strengthens our intuitive understanding "
            "of digit positions and place value independence across three-digit integers. A digit's true quantitative meaning is entirely determined by whether it sits in the hundreds, "
            "tens, or ones column. Engage with our interactive number search board to filter numbers by digit rules and uncover fascinating mathematical patterns "
            "in our digital studio right now with sharp eyes!"
        ),
        "checkpoints": [
            {
                "q": "In the number 254, which place value column holds the digit 5?",
                "options": ["Tens column (value 50)", "Hundreds column (value 500)", "Ones column (value 5)", "Thousands column"],
                "ans": "Tens column (value 50)",
                "explanation": "In 254, 2 is in hundreds, 5 is in tens (value 50), and 4 is in ones."
            },
            {
                "q": "Which of these numbers between 200 and 300 has the digit 5 in both tens and ones places?",
                "options": ["255", "250", "205", "215"],
                "ans": "255",
                "explanation": "255 has a 5 in the tens column (50) and a 5 in the ones column (5)."
            }
        ]
    },
    {
        "id": 15,
        "title": "Place Value Comparisons",
        "badge": "Greater Than & Less Than",
        "sim_id": "sim_place_value_comparisons",
        "description": "Compare three-digit numbers using greater than (>) and less than (<) symbols through systematic place value hierarchy analysis.",
        "speech": (
            "When comparing two three-digit numbers to determine which is greater or smaller, we follow a strict mathematical hierarchy starting always from the "
            "largest place value column. Always compare the leftmost hundreds column first! Consider the numbers four hundred and eighty-seven and four hundred "
            "and twenty-three. Both numbers have four in the hundreds column, representing four hundred units each. Because their hundreds digits are equal, we move "
            "directly to the next column: the tens place! Here, four hundred eighty-seven has eight tens, while four hundred twenty-three has only two tens in total. "
            "Since eight tens is greater than two tens, four hundred eighty-seven is greater than four hundred twenty-three! We write this mathematically as 487 > 423. "
            "Now consider two hundred and nine compared directly with two hundred and ninety. Both have two hundreds, but two hundred and nine has zero tens, while "
            "two hundred and ninety has nine tens. Therefore, two hundred and nine is strictly less than two hundred ninety: 209 is less than 290. Remember, the "
            "comparison symbol always opens its wide jaws toward the larger numerical value on either side. Use our interactive balance scale to compare three-digit "
            "pairs with ease and master inequality relationships right now!"
        ),
        "checkpoints": [
            {
                "q": "Which comparison statement is mathematically correct?",
                "options": ["487 > 423", "487 < 423", "487 = 423", "423 > 487"],
                "ans": "487 > 423",
                "explanation": "487 has 8 tens while 423 has only 2 tens, so 487 is greater than 423."
            },
            {
                "q": "Compare 209 and 290 using the correct symbol:",
                "options": ["209 < 290", "209 > 290", "209 = 290", "290 < 209"],
                "ans": "209 < 290",
                "explanation": "209 has 0 tens while 290 has 9 tens, so 209 is less than 290."
            }
        ]
    },
    {
        "id": 16,
        "title": "Ordering Three Digits",
        "badge": "Permutations & Ordering",
        "sim_id": "sim_ordering_three_digits",
        "description": "Form all possible three-digit combinations from given digits, identify minimum and maximum values, and arrange sets in order.",
        "speech": (
            "To complete our foundational mastery of three-digit numbers, let us explore digit combinations, permutations, and sequence ordering! Suppose you are "
            "given three single digit cards on a table: three, seven, and five. What is the greatest possible three-digit number you can create using each digit once? "
            "To maximize overall value, place the largest digit in the highest place value column! Placing seven in the hundreds, five in the tens, and three in the "
            "ones yields seven hundred and fifty-three, the absolute maximum possible number. Conversely, to form the smallest possible number, place the smallest "
            "digit in the hundreds place: three in the hundreds, five in the tens, and seven in the ones gives three hundred and fifty-seven! In total, these three "
            "non-zero digits can form six distinct three-digit numbers: 357, 375, 537, 573, 735, and 753. We can then arrange these values in ascending order from "
            "smallest to biggest, or descending order from biggest to smallest with ease. Ordering numbers accurately requires systematic place value comparison at "
            "every single step of the sequential process. Experiment with our interactive digit arranger in the simulator to generate combinations and master min-max number ordering "
            "with absolute mastery and confidence today!"
        ),
        "checkpoints": [
            {
                "q": "Using the digits 3, 7, and 5 once each, what is the greatest 3-digit number you can form?",
                "options": ["753", "735", "573", "375"],
                "ans": "753",
                "explanation": "Placing the largest digit 7 in hundreds, then 5 in tens, and 3 in ones gives 753."
            },
            {
                "q": "What is the smallest 3-digit number formed using digits 3, 7, and 5 once each?",
                "options": ["357", "375", "537", "735"],
                "ans": "357",
                "explanation": "Placing the smallest digit 3 in hundreds, then 5 in tens, and 7 in ones gives 357."
            }
        ]
    }
]

if __name__ == "__main__":
    FORBIDDEN_CHARACTERS = ['Ajji', 'Teji', 'Jojo', 'Farooq', 'Arvind', 'Raghav', 'Amma', 'Chirag', 'Nandini', 'Nani Maa', 'Nani', 'Deba', 'Deep', 'Meera', 'Dhruv', 'Pihu']
    FORBIDDEN_PERSONAS = [r'\bDr\b', r'\bDr\.\b', r'\bSir\b', r'\bMadam\b', r'\bMr\b', r'\bMr\.\b', r'\bMrs\b', r'\bMrs\.\b', r'\bMiss\b']
    
    print("Validating Part 2 (Slides 9-16)...")
    for s in slides_part2:
        sid = s["id"]
        title = s["title"]
        words = len(title.split())
        assert 1 <= words <= 3, f"Slide {sid} title '{title}' must be 1-3 words (got {words})"
        
        slide_str = json.dumps(s)
        for name in FORBIDDEN_CHARACTERS:
            if name.lower() == 'deep':
                assert not re.search(r'\bDeep\b', slide_str), f"Slide {sid} contains character name '{name}'"
            else:
                assert not re.search(r'\b' + re.escape(name) + r"'?s?\b", slide_str, re.IGNORECASE), f"Slide {sid} contains character name '{name}'"
        for persona in FORBIDDEN_PERSONAS:
            assert not re.search(persona, slide_str, re.IGNORECASE), f"Slide {sid} contains persona '{persona}'"
        
        wc = len(s["speech"].split())
        print(f"Slide {sid}: '{title}' -> Speech Word Count: {wc}")
        assert 195 <= wc <= 215, f"Slide {sid} word count out of range: {wc} (must be 195-215)"
        assert len(s["checkpoints"]) == 2, f"Slide {sid} must have 2 checkpoints"
        for cp in s["checkpoints"]:
            assert len(cp["options"]) == 4, f"Slide {sid} checkpoint must have 4 options"
            assert cp["ans"] in cp["options"], f"Slide {sid} checkpoint answer '{cp['ans']}' not in options"
    print("Part 2 validation successful!")
