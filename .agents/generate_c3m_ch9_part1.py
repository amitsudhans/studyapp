#!/usr/bin/env python3
"""
Slide Data Generator for NCERT Class 3 Mathematics - Chapter 9: House of Hundreds - II
Part 1: Slides 1 to 8
Strictly 195 - 215 words per spoken text.
1-3 word titles.
No human names (Akbar, Birbal, Raghav, etc. removed/generalized).
No teacher personas.
"""

import json

slides_part1 = [
    {
        "id": 1,
        "title": "Counting Royal Flocks",
        "subtitle": "Discovering large three-digit quantities through a royal estimation riddle",
        "speech": (
            "Welcome enthusiastic scholars to our second advanced house of hundreds laboratory exploring numbers approaching one thousand! "
            "Our journey begins in a magnificent royal courtyard where a grand monarch once gazed into the twilight sky and wondered how many black crows lived across the royal city. "
            "A wise court mathematician bowed and announced with calm certainty that exactly nine hundred and sixty-three crows inhabited the rooftops. "
            "When asked how such an exact count was possible, the scholar explained that if fewer birds were seen, the rest were visiting cousins across neighboring provinces, and if more appeared, distant relatives had flown in for a festival. "
            "Beyond its wit, this famous tale invites us to inspect large three-digit numbers like nine hundred and sixty-three. "
            "In this impressive number, the hundreds place contains nine groups of one hundred, representing nine hundred units. "
            "The tens place contains six groups of ten, representing sixty units, while the ones place holds three loose single units. "
            "Together, nine hundreds, six tens, and three ones compose the numeral nine hundred and sixty-three. "
            "Visualizing such vast quantities helps us appreciate how base-ten place value effortlessly scales to describe hundreds of items. "
            "Explore the royal flock simulator to toggle digit place values and assemble three-digit quantities up to the nine-hundreds with precision."
        ),
        "checkpoints": [
            {
                "question": "In the number 963, what is the place value of the digit 9?",
                "options": ["9 ones (9)", "9 tens (90)", "9 hundreds (900)", "9 thousands (9000)"],
                "answer": 2,
                "hint": "The digit 9 sits in the hundreds column.",
                "explanation": "In 963, the digit 9 occupies the hundreds place, so its place value is 9 × 100 = 900."
            },
            {
                "question": "How many tens are in the number 963?",
                "options": ["3 tens", "6 tens", "9 tens", "60 tens"],
                "answer": 1,
                "hint": "Look at the middle digit in the tens position.",
                "explanation": "The digit in the tens place is 6, which represents 6 tens (60)."
            }
        ]
    },
    {
        "id": 2,
        "title": "Rice Sack Tiles",
        "subtitle": "Modeling large three-digit cargo loads with concrete place value tiles",
        "speech": (
            "When commercial cargo trucks deliver heavy shipments of grain across city markets, warehouse managers need swift ways to record hundreds of rice sacks. "
            "A clever transport supervisor uses a standardized visual tile code to represent sack inventories with clarity. "
            "A large square tile represents one flat crate of one hundred rice sacks. "
            "A tall slender rectangular rod represents one bundle of ten rice sacks, while a tiny square tile represents one single loose rice sack. "
            "Suppose a grain truck arrives carrying eight hundred and thirty-two rice sacks. "
            "To model this shipment, the supervisor displays eight large square tiles for eight hundred, three slender rods for thirty, and two small unit tiles for two loose sacks. "
            "Now consider another delivery of five hundred and four sacks. "
            "This shipment requires five large hundred tiles, zero ten rods because the tens digit is zero, and four tiny unit tiles. "
            "Notice how the zero acts as an indispensable placeholder, ensuring that five hundred and four is never confused with fifty-four! "
            "Representing quantities through concrete visual tiles grounds our understanding of expanded notation: eight hundred plus thirty plus two equals eight hundred thirty-two. "
            "Interact with the rice sack warehouse workbench to drag hundred flats, ten rods, and unit tiles to represent inventory loads."
        ),
        "checkpoints": [
            {
                "question": "Which combination of tiles correctly represents 504 rice sacks?",
                "options": ["5 hundred tiles and 4 ten rods", "5 hundred tiles, 0 ten rods, and 4 unit tiles", "50 ten rods and 4 unit tiles", "5 hundred tiles and 40 unit tiles"],
                "answer": 1,
                "hint": "504 has 5 hundreds, 0 tens, and 4 ones.",
                "explanation": "504 consists of 5 hundreds (5 square tiles), 0 tens, and 4 units (4 small tiles)."
            },
            {
                "question": "What number is formed by 7 hundred tiles, 2 ten rods, and 6 unit tiles?",
                "options": ["762", "726", "276", "627"],
                "answer": 1,
                "hint": "7 hundreds = 700, 2 tens = 20, 6 units = 6.",
                "explanation": "700 + 20 + 6 = 726."
            }
        ]
    },
    {
        "id": 3,
        "title": "Extended Line Landmarks",
        "subtitle": "Locating high-magnitude three-digit numbers along extended number coordinates",
        "speech": (
            "A number line provides a continuous spatial highway to navigate high-magnitude numbers stretching between five hundred and one thousand. "
            "Imagine an extended coordinate track clearly marked with major hundred milestones: five hundred, six hundred, seven hundred, eight hundred, and nine hundred. "
            "To locate a specific three-digit number with precision, we first identify the two surrounding hundred landmarks. "
            "Consider the number six hundred and twenty-eight. "
            "Because six hundred and twenty-eight is greater than six hundred but less than seven hundred, it must lie between those two milestones. "
            "Next, we inspect the middle decade marker at six hundred and fifty. "
            "Since six hundred and twenty-eight is less than six hundred and fifty, it sits in the first half of that hundred interval, closer to six hundred. "
            "Now consider locating eight hundred and fifty-five. "
            "It sits between eight hundred and nine hundred, just slightly past the midway benchmark of eight hundred and fifty. "
            "Placing numbers on an extended track trains your spatial intuition to judge relative distances and magnitudes accurately. "
            "You can immediately see that eight hundred and fifty-five is substantially larger than six hundred and twenty-eight because it lies further to the right. "
            "Guide the interactive zoom marker along the extended number track to place values accurately."
        ),
        "checkpoints": [
            {
                "question": "Between which two consecutive hundred markers does the number 703 lie?",
                "options": ["Between 600 and 700", "Between 700 and 800", "Between 800 and 900", "Between 500 and 600"],
                "answer": 1,
                "hint": "703 is slightly larger than 700.",
                "explanation": "703 is greater than 700 and less than 800, so it lies between 700 and 800."
            },
            {
                "question": "Which of these numbers lies closest to the landmark 850 on a number line?",
                "options": ["810", "835", "855", "890"],
                "answer": 2,
                "hint": "Calculate the difference from 850: 855 is only 5 units away.",
                "explanation": "|855 - 850| = 5, which is closer to 850 than any other option."
            }
        ]
    },
    {
        "id": 4,
        "title": "Neighbouring Boundary Benchmarks",
        "subtitle": "Identifying bounding tens, fifties, and hundreds for multi-century values",
        "speech": (
            "In practical arithmetic and mental estimation, knowing the nearest neighboring benchmarks of a number is an essential mathematical superpower. "
            "When we analyze a number like four hundred and sixty-eight, we can identify its boundaries across different scales of rounding. "
            "First, let us find its neighboring tens: forty-six tens equals four hundred sixty, while forty-seven tens equals four hundred seventy. "
            "Four hundred and sixty-eight is bounded between four hundred sixty and four hundred seventy, sitting closer to four hundred seventy. "
            "Next, let us look at neighboring fifties: four hundred and fifty and five hundred. "
            "Four hundred sixty-eight lies between four hundred fifty and five hundred, sitting closer to five hundred. "
            "Finally, what are its neighboring hundreds? The bounding hundreds are four hundred and five hundred. "
            "Since sixty-eight is greater than fifty, four hundred sixty-eight rounds up toward five hundred. "
            "Now consider eight hundred and ninety-nine: its neighboring tens are eight hundred ninety and nine hundred, its neighboring fifties are eight hundred fifty and nine hundred, and its neighboring hundreds are eight hundred and nine hundred. "
            "Bounding numbers within these hierarchical intervals provides the conceptual foundation for rounding and swift mental approximations. "
            "Interact with the boundary benchmark analyzer to test numbers and reveal their bounding tens, fifties, and hundreds."
        ),
        "checkpoints": [
            {
                "question": "What are the neighboring tens for the number 468?",
                "options": ["450 and 460", "460 and 470", "470 and 480", "400 and 500"],
                "answer": 1,
                "hint": "468 ends between 60 and 70.",
                "explanation": "The multiple of ten immediately below 468 is 460, and immediately above is 470."
            },
            {
                "question": "Which hundred is 899 closest to?",
                "options": ["800", "850", "900", "1000"],
                "answer": 2,
                "hint": "899 is only 1 unit away from 900.",
                "explanation": "899 is just 1 unit away from 900, so 900 is its closest neighboring hundred."
            }
        ]
    },
    {
        "id": 5,
        "title": "Crane Jump Pathways",
        "subtitle": "Guiding river cranes across step intervals to catch food along number tracks",
        "speech": (
            "Along quiet riverbanks, elegant white cranes step carefully between smooth stones to hunt for small fish and water insects. "
            "We can model their foraging journeys as fascinating step-jump puzzles along extended number tracks! "
            "Imagine a crane standing at stone six hundred and fifty who wants to reach a tasty fish resting at stone seven hundred. "
            "The crane moves by leaping in equal strides of ten units per hop. "
            "How many leaps of ten must the crane take to travel from six hundred fifty to seven hundred? "
            "The total distance between six hundred fifty and seven hundred is fifty units. "
            "Dividing fifty by ten gives exactly five leaps: six hundred sixty, six hundred seventy, six hundred eighty, six hundred ninety, and seven hundred! "
            "Now suppose another crane stands at seven hundred and fifty, aiming for food at eight hundred, but leaps in longer strides of twenty-five units. "
            "From seven hundred fifty, the first leap of twenty-five lands on seven hundred seventy-five, and the second leap reaches eight hundred. "
            "The crane completes the fifty-unit journey in just two leaps because twenty-five times two equals fifty. "
            "Use the crane jump simulator to select stride lengths, trace leap trajectories, and solve target interval puzzles."
        ),
        "checkpoints": [
            {
                "question": "A crane hops by 10s from 650 to 700. How many hops does it take?",
                "options": ["3 hops", "4 hops", "5 hops", "6 hops"],
                "answer": 2,
                "hint": "Total distance is 700 - 650 = 50. Divide 50 by 10.",
                "explanation": "50 units divided into steps of 10 equals 5 hops."
            },
            {
                "question": "Starting at 750, if a crane takes 2 hops of 25 units, on what stone does it land?",
                "options": ["775", "800", "825", "850"],
                "answer": 1,
                "hint": "750 + 25 + 25 = ?",
                "explanation": "750 + 25 = 775, and 775 + 25 = 800."
            }
        ]
    },
    {
        "id": 6,
        "title": "Tambola Grid Clues",
        "subtitle": "Solving place value riddles across a structured five-hundred to six-hundred matrix",
        "speech": (
            "Games make mathematical exploration exciting, and the classic grid game of Tambola is a wonderful arena to test our number sense! "
            "Imagine a classroom game board displaying a grid of numbers between five hundred and seventy and six hundred and thirty. "
            "A caller reads out clever mathematical clues, and players must scan the grid to identify and strike out the matching number. "
            "Listen to this clue: 'I have six hundreds, zero tens, and five loose ones. Who am I?' "
            "We assemble the digits: six hundreds, zero tens, and five ones make the number six hundred and five. "
            "Next clue: 'I am five more than five hundred and ninety.' "
            "We calculate: five hundred ninety plus five equals five hundred and ninety-five! "
            "Another clue challenges us: 'I am exactly ten less than six hundred and twenty.' "
            "Subtracting ten from six hundred twenty gives six hundred and ten. "
            "Notice how every clue requires you to translate descriptive phrases into precise arithmetic operations or place value structures. "
            "Playing on a focused grid reinforces mental addition, subtraction of tens, and swift pattern recognition across the six-hundred century boundary. "
            "Interact with the digital Tambola game board to read caller clues, cross out matching grid cells, and shout winning streaks."
        ),
        "checkpoints": [
            {
                "question": "Which number matches the clue: '6 hundreds, 0 tens, and 5 ones'?",
                "options": ["650", "605", "560", "506"],
                "answer": 1,
                "hint": "Write the digits in order: Hundreds=6, Tens=0, Ones=5.",
                "explanation": "6 hundreds, 0 tens, and 5 ones forms the number 605."
            },
            {
                "question": "What number is 10 less than 620?",
                "options": ["600", "610", "615", "630"],
                "answer": 1,
                "hint": "Subtract 10 from 620: 620 - 10.",
                "explanation": "620 - 10 = 610."
            }
        ]
    },
    {
        "id": 7,
        "title": "Multiple Number Expressions",
        "subtitle": "Decomposing three-digit values into diverse additive, subtractive, and grouped sentences",
        "speech": (
            "A single number can wear many different mathematical costumes without ever changing its core numerical identity! "
            "Consider the three-digit number three hundred and sixty-eight. "
            "Its standard expanded place value notation is three hundred plus sixty plus eight. "
            "However, we can also express three hundred sixty-eight as three hundred and fifty plus eighteen, or as two hundred plus one hundred sixty-eight. "
            "We can even use subtraction: four hundred minus thirty-two equals three hundred sixty-eight! "
            "Now examine another number: nine hundred and five. "
            "In place value terms, it is nine hundreds plus zero tens plus five ones. "
            "We can also write it as nine hundred plus five, or eight hundred and fifty plus fifty-five, or even one thousand minus ninety-five. "
            "Consider the symmetrical number five hundred and fifty-five: it can be written as five hundred plus fifty plus five, or five hundred plus fifty-five, or six hundred minus forty-five. "
            "This wonderful flexibility in representing numbers is known as additive and subtractive decomposition. "
            "Being able to break numbers apart into convenient friendly chunks is the secret key to effortless mental arithmetic and advanced problem solving. "
            "Use the multi-expression equation generator on screen to build diverse addition and subtraction sentences for target values."
        ),
        "checkpoints": [
            {
                "question": "Which of these expressions equals 905?",
                "options": ["900 + 50", "900 + 5", "800 + 15", "1000 - 5"],
                "answer": 1,
                "hint": "905 has 9 hundreds and 5 units: 900 + 5.",
                "explanation": "900 + 5 = 905."
            },
            {
                "question": "Which subtraction sentence produces 368?",
                "options": ["400 - 32", "400 - 28", "400 - 42", "400 - 18"],
                "answer": 0,
                "hint": "Compute 400 - 32.",
                "explanation": "400 - 32 = 368."
            }
        ]
    },
    {
        "id": 8,
        "title": "Stepping Pattern Trails",
        "subtitle": "Cracking multi-century skip-counting sequences and identifying rule intervals",
        "speech": (
            "Mathematics is the science of patterns, and number trails provide an adventurous landscape to discover hidden arithmetic rules. "
            "Imagine stepping across a trail of stones where numbers advance in predictable leaps. "
            "Look at this sequence: five hundred and ten, five hundred and twenty, five hundred and thirty, blank, five hundred and fifty. "
            "By comparing consecutive stones, we notice that each number is ten units greater than the previous stone: the rule is add ten! "
            "The missing number is five hundred and forty. "
            "Now inspect a steeper climbing sequence: three hundred, four hundred, five hundred, blank, seven hundred. "
            "Here the trail advances by one hundred units at every step, so the missing milestone is six hundred. "
            "Trails can also skip by different friendly intervals, such as skips of twenty-five: six hundred, six hundred twenty-five, six hundred fifty, six hundred seventy-five, seven hundred. "
            "Or skips of fifteen: seven hundred, seven hundred fifteen, seven hundred thirty, seven hundred forty-five. "
            "Whenever you encounter an unfamiliar sequence, subtract any two neighboring numbers to discover the constant leap size. "
            "Once you know the step size, you can extend the trail forward or backward indefinitely. "
            "Explore the stepping pattern trail puzzle to determine step intervals and fill missing stepping stones."
        ),
        "checkpoints": [
            {
                "question": "What is the missing number in the sequence: 600, 625, 650, __, 700?",
                "options": ["660", "670", "675", "680"],
                "answer": 2,
                "hint": "The sequence skips forward by 25: 650 + 25.",
                "explanation": "The step size is +25. 650 + 25 = 675."
            },
            {
                "question": "What is the constant rule for the sequence: 700, 715, 730, 745?",
                "options": ["Add 10", "Add 15", "Add 20", "Add 25"],
                "answer": 1,
                "hint": "Find the difference: 715 - 700 = 15.",
                "explanation": "Each consecutive term increases by exactly 15."
            }
        ]
    }
]

if __name__ == "__main__":
    for s in slides_part1:
        wc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({len(s['title'].split())} words) -> Speech: {wc} words")
        assert 195 <= wc <= 215, f"Slide {s['id']} speech out of range: {wc}"
        assert len(s["title"].split()) <= 3, f"Slide {s['id']} title too long"
        assert len(s["checkpoints"]) == 2, f"Slide {s['id']} must have 2 checkpoints"
    print("Part 1 verified successfully!")
