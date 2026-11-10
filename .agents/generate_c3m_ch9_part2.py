#!/usr/bin/env python3
"""
Slide Data Generator for NCERT Class 3 Mathematics - Chapter 9: House of Hundreds - II
Part 2: Slides 9 to 16
Strictly 195 - 215 words per spoken text.
1-3 word titles.
No human names (Akbar, Birbal, Raghav, etc. removed/generalized).
No teacher personas.
"""

import json

slides_part2 = [
    {
        "id": 9,
        "title": "Equation Condition Balancers",
        "subtitle": "Balancing equations and inequalities around central mathematical target values",
        "speech": (
            "Mathematics operates like an exquisite balance scale where equations maintain perfect equality between opposing expressions. "
            "Consider a central target value like four hundred resting upon our balance platform. "
            "How many different balanced number sentences can we construct that equal exactly four hundred? "
            "We could write two hundred plus two hundred, or three hundred and fifty plus fifty, or five hundred minus one hundred. "
            "We could even combine multiple terms: three hundred plus seventy plus thirty equals four hundred! "
            "Now consider another target value: seven hundred and seventy-five. "
            "We can balance it with seven hundred plus seventy-five, or eight hundred minus twenty-five, or seven hundred and fifty plus twenty-five. "
            "In addition to equations, we also explore inequalities using the greater-than and less-than relational symbols. "
            "For example, seven hundred plus sixty is seven hundred sixty, which is strictly less than seven hundred and seventy-five. "
            "Conversely, eight hundred minus ten is seven hundred ninety, which is strictly greater than seven hundred seventy-five. "
            "Practicing with balancing conditions sharpens your ability to manipulate numbers flexibly and evaluate relational constraints with speed and confidence. "
            "Interact with the equation balancer simulator to place terms on opposing balance pans and verify arithmetic equality across diverse equations."
        ),
        "checkpoints": [
            {
                "question": "Which of these expressions balances to exactly 400?",
                "options": ["350 + 40", "300 + 70 + 30", "500 - 150", "200 + 150"],
                "answer": 1,
                "hint": "Add the terms: 300 + 70 + 30 = 300 + 100 = 400.",
                "explanation": "300 + 70 + 30 = 400, perfectly matching the target value."
            },
            {
                "question": "Which statement is true regarding the number 775?",
                "options": ["700 + 60 > 775", "800 - 25 = 775", "750 + 30 = 775", "775 < 700 + 50"],
                "answer": 1,
                "hint": "Compute 800 - 25.",
                "explanation": "800 - 25 = 775, forming a true balanced equation."
            }
        ]
    },
    {
        "id": 10,
        "title": "Magnitude Estimation Ranges",
        "subtitle": "Categorizing real-world quantities into logarithmic orders of magnitude",
        "speech": (
            "Numbers describe real-world phenomena across vastly different scales of magnitude, from a few pebbles to thousands of stars in the night sky. "
            "A seasoned mathematician develops a keen intuitive sense of scale, knowing which numerical range best fits a given everyday situation. "
            "Let us categorize real-world quantities into four broad magnitude ranges: zero to ten, ten to one hundred, one hundred to one thousand, and over one thousand. "
            "How many pencils are typically held inside a student's personal pencil box? "
            "That count comfortably belongs in the range of zero to ten. "
            "How many storybooks are stored on a single classroom library shelf? "
            "That collection fits naturally in the range of ten to one hundred books. "
            "Now think of the total number of students enrolled across a large primary school building: that count spans between one hundred and one thousand students! "
            "What about the total number of footsteps taken during a long morning hike, or the population of an entire township? "
            "Those vast counts easily exceed one thousand units. "
            "Estimating appropriate magnitude ranges prevents ridiculous calculation errors and connects textbook numbers with physical reality and daily experiences. "
            "Use the magnitude scale workbench to drag real-world scenarios into their proper order-of-magnitude category bins."
        ),
        "checkpoints": [
            {
                "question": "Which magnitude range best fits the number of students in a large school?",
                "options": ["0 to 10", "10 to 100", "100 to 1,000", "Over 1,000,000"],
                "answer": 2,
                "hint": "Most schools have several hundred students.",
                "explanation": "A typical school has a few hundred students, fitting into the 100 to 1,000 range."
            },
            {
                "question": "Which of these quantities belongs in the range '0 to 10'?",
                "options": ["Number of fingers on one hand", "Number of days in a year", "Number of pages in an encyclopedia", "Number of trees in a forest"],
                "answer": 0,
                "hint": "One hand has 5 fingers, which is between 0 and 10.",
                "explanation": "5 fingers on a hand fits squarely into the 0 to 10 range."
            }
        ]
    },
    {
        "id": 11,
        "title": "Descriptive Number Riddles",
        "subtitle": "Translating cultural idioms and landmark clues into precise numerical values",
        "speech": (
            "Numbers often hide behind poetic descriptions and cultural idioms in traditional mathematical riddles. "
            "Let us decode several classic descriptive clues together! "
            "Consider this riddle: 'I am one century plus one half century. What number am I?' "
            "In sports and mathematics, one century represents one hundred units, while a half century represents fifty units. "
            "Adding one hundred and fifty produces the number one hundred and fifty! "
            "Now consider another riddle: 'I am a three-digit milestone. I have two zeroes, and I am the very next number after ninety-nine.' "
            "Counting one step forward from ninety-nine brings us to one hundred! "
            "Here is a trickier riddle: 'I am double of a century minus ten.' "
            "A century is one hundred, so double of a century is two hundred. Subtracting ten from two hundred gives one hundred and ninety. "
            "Look at this clue: 'I have seven hundreds, and my tens and ones digits are identical twins that sum to eight.' "
            "Since four plus four equals eight, the twin digits are forty-four, forming seven hundred and forty-four! "
            "Translating descriptive language into arithmetic builds deep linguistic and numerical fluency simultaneously. "
            "Interact with the riddle decoding desk to match descriptive clue cards with their exact numbers."
        ),
        "checkpoints": [
            {
                "question": "What number is described as 'one century plus one half century'?",
                "options": ["120", "150", "175", "200"],
                "answer": 1,
                "hint": "100 + 50 = ?",
                "explanation": "One century is 100, and a half century is 50. 100 + 50 = 150."
            },
            {
                "question": "Which number is 'double of a century minus 10'?",
                "options": ["180", "190", "200", "210"],
                "answer": 1,
                "hint": "Double of 100 is 200. Subtract 10: 200 - 10.",
                "explanation": "(2 × 100) - 10 = 200 - 10 = 190."
            }
        ]
    },
    {
        "id": 12,
        "title": "Number Pattern Sequences",
        "subtitle": "Investigating step-up, step-down, twin, triplet, and palindromic number families",
        "speech": (
            "Welcome to the detective bureau of special numbers, where numbers with curious structural properties are investigated and classified with precision! "
            "First, we observe stepping sequences where digits march in strict consecutive order. "
            "In a step-up sequence like three hundred and forty-five, or seven hundred and eighty-nine, each digit increases by one as you move from left to right. "
            "In reverse, a step-down sequence like eight hundred and seventy-six, or three hundred and twenty-one, sees each digit decrease by one. "
            "Next, we examine twin-digit numbers like twenty-two, seventy-seven, and eighty-eight, where two identical digits stand side by side. "
            "When all three digits in a number are identical, like one hundred eleven, two hundred twenty-two, or seven hundred seventy-seven, we call them triplet numbers. "
            "Even more fascinating are palindromic numbers! "
            "A palindromic number reads identically whether read forward from left to right or backward from right to left, like three hundred fifty-three, or eight hundred sixty-eight. "
            "Notice how the outer hundreds and ones digits are twins, flanking a central pivot digit in the tens place. "
            "Recognizing these visual patterns transforms dry numerals into delightful geometric structures and unforgettable puzzles. "
            "Use the pattern detective lab to filter numbers, highlight palindromes, and discover structural beauty across digits."
        ),
        "checkpoints": [
            {
                "question": "Which of the following numbers is a palindromic number?",
                "options": ["354", "353", "533", "335"],
                "answer": 1,
                "hint": "A palindrome reads the same backwards and forwards.",
                "explanation": "353 reads as 3-5-3 both forward and backward, making it a palindrome."
            },
            {
                "question": "What kind of number sequence is 789?",
                "options": ["A triplet sequence", "A step-down sequence", "A step-up sequence", "A palindrome"],
                "answer": 2,
                "hint": "Digits 7, 8, 9 increase consecutively by 1.",
                "explanation": "789 is a step-up sequence because each consecutive digit increases by one."
            }
        ]
    },
    {
        "id": 13,
        "title": "Place Value Slips",
        "subtitle": "Constructing diverse multi-century numbers using constrained sets of paper slips",
        "speech": (
            "Can you construct a vast range of three-digit numbers using only a handful of labeled paper slips? "
            "Imagine holding a small envelope containing exactly six blank paper slips. "
            "Each slip can be stamped with one of three values: one hundred, ten, or one. "
            "Our challenge is to explore what numbers can be built using all six slips simultaneously. "
            "Suppose we choose four slips of one hundred, one slip of ten, and one slip of one. "
            "Adding their values: four hundreds make four hundred, plus ten, plus one, gives four hundred and eleven! "
            "What if we use two slips of one hundred, three slips of ten, and one slip of one? "
            "Two hundreds make two hundred, three tens make thirty, and one makes one: two hundred and thirty-one! "
            "What is the largest possible number we can construct using six slips? "
            "To maximize the value, we should choose all six slips as one hundreds, yielding six times one hundred equals six hundred! "
            "What is the smallest three-digit number we can make? "
            "We must use at least one hundred slip, four ten slips, and one unit slip to make one hundred forty-one. "
            "Experiment with the slip construction workbench to test slip combinations and discover mathematical constraints."
        ),
        "checkpoints": [
            {
                "question": "What number is formed by 4 slips of 100, 1 slip of 10, and 1 slip of 1?",
                "options": ["401", "410", "411", "414"],
                "answer": 2,
                "hint": "(4 × 100) + (1 × 10) + (1 × 1) = 400 + 10 + 1.",
                "explanation": "400 + 10 + 1 = 411."
            },
            {
                "question": "What is the maximum number you can make using 6 slips labeled 100, 10, or 1?",
                "options": ["500", "550", "600", "660"],
                "answer": 2,
                "hint": "Choose the largest value (100) for all 6 slips: 6 × 100.",
                "explanation": "Six slips of 100 give the maximum possible total: 6 × 100 = 600."
            }
        ]
    },
    {
        "id": 14,
        "title": "Digit Permutation Ordering",
        "subtitle": "Generating all combinations from restricted digits and ordering them systematically",
        "speech": (
            "Combinatorics is the branch of mathematics that explores how elements can be arranged, combined, and permuted systematically. "
            "Suppose we are given only two digit cards: the digit three and the digit eight. "
            "If repetition of digits is allowed, how many different two-digit numbers can we construct? "
            "We can place three in the tens place to form thirty-three and thirty-eight. "
            "We can place eight in the tens place to form eighty-three and eighty-eight. "
            "That gives exactly four distinct two-digit numbers: thirty-three, thirty-eight, eighty-three, and eighty-eight! "
            "Now let us expand our challenge to three-digit numbers using only the digits three and eight. "
            "With two choices for the hundreds place, two choices for the tens place, and two choices for the ones place, there are two times two times two, which equals eight distinct combinations! "
            "The numbers generated are: three hundred thirty-three, three hundred thirty-eight, three hundred eighty-three, three hundred eighty-eight, eight hundred thirty-three, eight hundred thirty-eight, eight hundred eighty-three, and eight hundred eighty-eight. "
            "Arranging these numbers in ascending order from smallest to largest demonstrates how place value governs magnitude: numbers starting with three are always smaller than those starting with eight. "
            "Use the permutation generator to build combinations and sort them dynamically."
        ),
        "checkpoints": [
            {
                "question": "How many 2-digit numbers can be made using the digits 3 and 8 with repetition allowed?",
                "options": ["2 numbers", "3 numbers", "4 numbers", "6 numbers"],
                "answer": 2,
                "hint": "Combinations: 33, 38, 83, 88.",
                "explanation": "There are 2 × 2 = 4 possible two-digit numbers (33, 38, 83, 88)."
            },
            {
                "question": "Which is the smallest 3-digit number formed using only the digits 3 and 8?",
                "options": ["338", "383", "333", "833"],
                "answer": 2,
                "hint": "Choose the smallest digit (3) for all three positions.",
                "explanation": "333 has the smallest possible digit in the hundreds, tens, and ones places."
            }
        ]
    },
    {
        "id": 15,
        "title": "Bhutasankhya Word Numerals",
        "subtitle": "Exploring the ancient Indian tradition of encoding numbers through natural concepts",
        "speech": (
            "Did you know that ancient Indian mathematicians and poets created a brilliant system to write numbers using words drawn from nature, astronomy, and the human body? "
            "This celebrated tradition is known as Bhutasankhya, which literally means 'numeral words of the elements'. "
            "In this poetic system, every number is represented by a familiar concept that exists uniquely in that exact quantity. "
            "For example, the number one is symbolized by the Moon or the Earth, because there is only one Moon shining in our night sky. "
            "The number two is represented by Eyes or Hands, because human beings have a natural pair of eyes and hands. "
            "The number three is symbolized by Trikala, representing the three divisions of time: past, present, and future, or the three sacred fires. "
            "The number four is represented by the four directions: north, south, east, and west, or the four seasons. "
            "The number five is symbolized by the Palm, because each palm holds five fingers, or the five senses. "
            "The number seven is represented by Saptasvara, the seven classical musical notes: Sa, Re, Ga, Ma, Pa, Dha, Ni! "
            "Explore the Bhutasankhya concept gallery to inspect ancient word symbols and decode their numerical values."
        ),
        "checkpoints": [
            {
                "question": "In the Bhutasankhya tradition, which number is symbolized by 'Moon'?",
                "options": ["0", "1", "2", "5"],
                "answer": 1,
                "hint": "There is only one single moon in the sky.",
                "explanation": "Because there is only one Moon, 'Moon' represents the numeral 1."
            },
            {
                "question": "Which cultural concept represents the number 7 in Bhutasankhya?",
                "options": ["Eyes", "Palm", "Saptasvara (7 musical notes)", "Trikala (3 times)"],
                "answer": 2,
                "hint": "Saptasvara refers to the seven musical notes.",
                "explanation": "Saptasvara stands for the seven classical musical notes, representing the number 7."
            }
        ]
    },
    {
        "id": 16,
        "title": "Word Numeral Cards",
        "subtitle": "Assembling and decoding compound multi-digit numbers from word numeral tokens",
        "speech": (
            "Now let us combine ancient word symbols to construct and decode fascinating multi-digit compound numbers together! "
            "In the classical Indian tradition, word numerals were arranged in poetic verses following a strict rule called 'ankanam vamato gatih', which means 'numbers move from right to left'. "
            "This means the units place is stated first, followed by the tens place, and then the hundreds place! "
            "Let us decode a traditional word phrase: 'Eyes and Palm'. "
            "Eyes represents two, and Palm represents five. "
            "Reading from right to left, five is in the tens place and two is in the units place, forming the number fifty-two! "
            "Now consider forming the number twenty-seven: seven is Saptasvara, and two is Eyes. "
            "In modern classroom cards, we can also match cards directly from left to right for intuitive and clear practice. "
            "For the number fifteen, we can pair a card for one ten and five fingers. "
            "For ninety-four, we can pair nine planets with four directions. "
            "This rich integration of culture, linguistics, and arithmetic reveals how ancient civilizations wove mathematics into poetry, architecture, astronomy, and song. "
            "Interact with the word numeral card assembly workbench to pair cultural symbols, decode historical inscriptions, and build three-digit numbers."
        ),
        "checkpoints": [
            {
                "question": "If 'Eyes' = 2 and 'Palm' = 5, what two-digit number has Palm in the tens place and Eyes in the ones place?",
                "options": ["25", "52", "22", "55"],
                "answer": 1,
                "hint": "Tens digit is 5, ones digit is 2.",
                "explanation": "5 tens and 2 ones make 52."
            },
            {
                "question": "Why did ancient scholars use Bhutasankhya word numerals in poetic verses?",
                "options": ["Because they forgot how to write numbers", "To fit numbers smoothly into poetic rhythm and musical meters", "Because numbers were illegal", "To make math confusing on purpose"],
                "answer": 1,
                "hint": "Words fit poetry rhythm and meters far better than bare numerals.",
                "explanation": "Word numerals allowed mathematical rules and astronomical tables to be memorized effortlessly as rhythmic poetic verses."
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
