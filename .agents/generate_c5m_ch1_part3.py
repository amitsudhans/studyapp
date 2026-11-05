"""
Generate 40 Mastery Challenge Quiz Questions for NCERT Class 5 Mathematics Chapter 1: We the Travellers - I
Joyful Mathematics curriculum (NEP 2020).
Zero raw LaTeX! Clean Unicode symbols.
10 questions per challenge slide:
- Challenge 1 (Slide 17): Questions 1 to 10
- Challenge 2 (Slide 18): Questions 11 to 20
- Challenge 3 (Slide 19): Questions 21 to 30
- Challenge 4 (Slide 20): Questions 31 to 40
"""

QUIZ_QUESTIONS = [
    # Challenge 1 (Questions 1 to 10): Large Numbers & Place Value
    {
        "id": 1,
        "question": "What is the smallest 5-digit number?",
        "options": [
            "1,000",
            "9,999",
            "10,000 (Ten Thousand)",
            "100,000"
        ],
        "answer": 2,
        "explanation": "10,000 is the smallest 5-digit number. It is formed by adding 1 to 9,999 (the largest 4-digit number).",
        "solution_html": "<strong>Step-by-Step Analysis:</strong><br>1. The largest 4-digit number is 9,999.<br>2. 9,999 + 1 = 10,000.<br>3. 10,000 has 5 digits (1, 0, 0, 0, 0), making it the smallest 5-digit number."
    },
    {
        "id": 2,
        "question": "In the number 84,392, what is the place value of the digit 8?",
        "options": [
            "80",
            "800",
            "8,000",
            "80,000 (Eighty Thousand)"
        ],
        "answer": 3,
        "explanation": "The digit 8 is in the Ten Thousands (TTh) place, so its place value is 8 × 10,000 = 80,000.",
        "solution_html": "<strong>Step-by-Step Analysis:</strong><br>Place value columns: TTh (8) | Th (4) | H (3) | T (9) | O (2).<br>8 × 10,000 = 80,000."
    },
    {
        "id": 3,
        "question": "Which of the following correctly shows the Indian comma placement for 74025?",
        "options": [
            "7,4025",
            "74,025",
            "740,25",
            "7402,5"
        ],
        "answer": 1,
        "explanation": "In the Indian system, the first comma is placed after 3 digits from the right, giving 74,025.",
        "solution_html": "<strong>Comma Rule:</strong><br>Count 3 digits from right (5, 2, 0) and place the first comma: 74,025. It separates the Thousands period (74) from the Ones period (025)."
    },
    {
        "id": 4,
        "question": "What is the expanded form of 52,408?",
        "options": [
            "50,000 + 2,000 + 400 + 8",
            "5,000 + 200 + 40 + 8",
            "50,000 + 200 + 40 + 8",
            "50,000 + 2,000 + 40 + 8"
        ],
        "answer": 0,
        "explanation": "5 Ten Thousands (50,000) + 2 Thousands (2,000) + 4 Hundreds (400) + 0 Tens (0) + 8 Ones (8) = 50,000 + 2,000 + 400 + 8.",
        "solution_html": "<strong>Step-by-Step Expansion:</strong><br>5 × 10,000 = 50,000<br>2 × 1,000 = 2,000<br>4 × 100 = 400<br>0 × 10 = 0<br>8 × 1 = 8<br>Sum = 50,000 + 2,000 + 400 + 8."
    },
    {
        "id": 5,
        "question": "Which number is 'Sixty thousand, four hundred five' written in standard numerals?",
        "options": [
            "6,405",
            "60,450",
            "60,405",
            "604,005"
        ],
        "answer": 2,
        "explanation": "Thousands period = 60. Ones period = 405 (4 hundreds, 0 tens, 5 ones). So the numeral is 60,405.",
        "solution_html": "<strong>Breakdown:</strong><br>Sixty thousand = 60,000<br>Four hundred five = 405<br>60,000 + 405 = 60,405."
    },
    {
        "id": 6,
        "question": "Which of the following is the greatest 5-digit number?",
        "options": [
            "90,000",
            "99,990",
            "99,999",
            "100,000"
        ],
        "answer": 2,
        "explanation": "99,999 is the largest 5-digit number. Adding 1 to it yields 100,000, which has 6 digits (One Lakh).",
        "solution_html": "<strong>Analysis:</strong><br>Highest digit in every place: 9 in TTh, 9 in Th, 9 in H, 9 in T, 9 in O = 99,999."
    },
    {
        "id": 7,
        "question": "Using the digits 5, 1, 8, 3, and 0 each once, what is the smallest 5-digit number you can make?",
        "options": [
            "01,358",
            "10,358",
            "13,058",
            "10,538"
        ],
        "answer": 1,
        "explanation": "0 cannot be the leading digit. The smallest non-zero digit is 1, followed by 0, then 3, 5, 8. So the smallest number is 10,358.",
        "solution_html": "<strong>Step-by-Step Rule:</strong><br>1. Lowest non-zero digit for highest place (TTh) = 1.<br>2. Place 0 in second position (Th) = 0.<br>3. Arrange remaining digits in ascending order: 3, 5, 8.<br>4. Result = 10,358."
    },
    {
        "id": 8,
        "question": "If you swap the digits in the Thousands and Tens places of 43,875, what is the new number?",
        "options": [
            "47,835",
            "34,875",
            "43,785",
            "48,375"
        ],
        "answer": 0,
        "explanation": "In 43,875, Thousands digit is 3 and Tens digit is 7. Swapping 3 and 7 gives 47,835.",
        "solution_html": "<strong>Swap Trace:</strong><br>Original: 4 [3] 8 [7] 5<br>Swap 3 and 7:<br>New: 4 [7] 8 [3] 5 = 47,835."
    },
    {
        "id": 9,
        "question": "Which of these numbers is strictly greater than 67,420?",
        "options": [
            "67,399",
            "66,999",
            "67,419",
            "67,425"
        ],
        "answer": 3,
        "explanation": "67,425 has 5 in the Ones place compared to 0 in 67,420, making 67,425 > 67,420.",
        "solution_html": "<strong>Digit Comparison:</strong><br>Both have 67,42x. Comparing Ones digits: 5 > 0, so 67,425 > 67,420."
    },
    {
        "id": 10,
        "question": "What is the value of 10 bundles of Ten Thousand (10 × 10,000)?",
        "options": [
            "10,000",
            "100,000 (One Lakh)",
            "1,000,000",
            "50,000"
        ],
        "answer": 1,
        "explanation": "10 × 10,000 = 100,000, which is One Lakh in the Indian place value system.",
        "solution_html": "<strong>Base-10 Progression:</strong><br>10 × 10 = 100<br>10 × 100 = 1,000<br>10 × 1,000 = 10,000<br>10 × 10,000 = 100,000 (One Lakh)."
    },

    # Challenge 2 (Questions 11 to 20): Rounding Off (10s, 100s, 1,000s)
    {
        "id": 11,
        "question": "What is 83 rounded to the nearest ten (10)?",
        "options": [
            "80",
            "85",
            "90",
            "100"
        ],
        "answer": 0,
        "explanation": "The Ones digit is 3 (less than 5), so 83 is closer to 80 than to 90. It rounds down to 80.",
        "solution_html": "<strong>Number Line Hop:</strong><br>83 is 3 steps away from 80 and 7 steps away from 90. 80 is the nearest ten."
    },
    {
        "id": 12,
        "question": "What is 265 rounded to the nearest ten (10)?",
        "options": [
            "260",
            "265",
            "270",
            "300"
        ],
        "answer": 2,
        "explanation": "The Ones digit is 5. By the halfway rule, 5 always rounds UP to the next multiple of ten: 270.",
        "solution_html": "<strong>Halfway Rule:</strong><br>265 is midway between 260 and 270. Halfway numbers round UP to 270."
    },
    {
        "id": 13,
        "question": "What is 649 rounded to the nearest hundred (100)?",
        "options": [
            "600",
            "640",
            "650",
            "700"
        ],
        "answer": 0,
        "explanation": "Look at the Tens digit: it is 4 (which is less than 5). Since 49 is less than the halfway mark of 50, 649 rounds down to 600.",
        "solution_html": "<strong>Nearest 100 Check:</strong><br>Between 600 and 700, the midpoint is 650.<br>649 < 650, so it rounds down to 600."
    },
    {
        "id": 14,
        "question": "What is 1,850 rounded to the nearest hundred (100)?",
        "options": [
            "1,800",
            "1,850",
            "1,900",
            "2,000"
        ],
        "answer": 2,
        "explanation": "The Tens digit is 5 (halfway mark 50). By convention, halfway numbers round UP to the higher hundred: 1,900.",
        "solution_html": "<strong>Calculation:</strong><br>1,850 is midway between 1,800 and 1,900. Rounding up gives 1,900."
    },
    {
        "id": 15,
        "question": "What is 7,346 rounded to the nearest thousand (1,000)?",
        "options": [
            "7,000",
            "7,300",
            "7,400",
            "8,000"
        ],
        "answer": 0,
        "explanation": "The Hundreds digit is 3 (less than 5). 346 is less than 500, so 7,346 rounds down to 7,000.",
        "solution_html": "<strong>Thousands Rounding:</strong><br>Midpoint between 7,000 and 8,000 is 7,500.<br>7,346 < 7,500 → rounds down to 7,000."
    },
    {
        "id": 16,
        "question": "What is 5,780 rounded to the nearest thousand (1,000)?",
        "options": [
            "5,000",
            "5,700",
            "5,800",
            "6,000"
        ],
        "answer": 3,
        "explanation": "The Hundreds digit is 7 (5 or more). 780 is greater than 500, so 5,780 rounds up to 6,000.",
        "solution_html": "<strong>Thousands Rounding:</strong><br>780 ≥ 500 → rounds UP to 6,000."
    },
    {
        "id": 17,
        "question": "Which of the following numbers rounds to 5,000 when rounded to the nearest 100 AND also to 5,000 when rounded to the nearest 1,000?",
        "options": [
            "4,960",
            "4,200",
            "5,400",
            "5,800"
        ],
        "answer": 0,
        "explanation": "For 4,960: Rounded to nearest 100 gives 5,000 (rounds up from 4,900). Rounded to nearest 1,000 also gives 5,000 (960 ≥ 500).",
        "solution_html": "<strong>Dual-Rounding Check:</strong><br>1. Nearest 100 of 4,960: Tens digit is 6 ≥ 5 → rounds up to 5,000.<br>2. Nearest 1,000 of 4,960: Hundreds digit is 9 ≥ 5 → rounds up to 5,000.<br>Both match!"
    },
    {
        "id": 18,
        "question": "What is the smallest whole number that rounds up to 300 when rounded to the nearest hundred?",
        "options": [
            "249",
            "250",
            "299",
            "301"
        ],
        "answer": 1,
        "explanation": "250 is the very first number whose tens digit is 5, which rounds UP to 300.",
        "solution_html": "<strong>Range for 300:</strong><br>Numbers that round to 300 are from 250 to 349.<br>Smallest = 250; Largest = 349."
    },
    {
        "id": 19,
        "question": "What is the largest whole number that rounds down to 600 when rounded to the nearest hundred?",
        "options": [
            "649",
            "650",
            "699",
            "640"
        ],
        "answer": 0,
        "explanation": "649 has a tens digit of 4, so it rounds down to 600. 650 would round up to 700.",
        "solution_html": "<strong>Boundary Analysis:</strong><br>649 has tens digit 4 (< 5) → rounds to 600.<br>650 has tens digit 5 (≥ 5) → rounds to 700.<br>So 649 is the maximum."
    },
    {
        "id": 20,
        "question": "A village road odometer reading is 14,892 km. What is this distance rounded to the nearest thousand kilometres?",
        "options": [
            "14,000 km",
            "14,800 km",
            "15,000 km",
            "20,000 km"
        ],
        "answer": 2,
        "explanation": "In 14,892, the Hundreds digit is 8 (≥ 5). Rounding to the nearest thousand rounds 14,892 up to 15,000 km.",
        "solution_html": "<strong>Rounding Check:</strong><br>Hundreds digit is 8 ≥ 5 → 14 Thousands rounds UP to 15 Thousands = 15,000 km."
    },

    # Challenge 3 (Questions 21 to 30): Speeds, Distance & Trip Planning
    {
        "id": 21,
        "question": "A car travels along a highway at an average speed of 65 km/h. How far will it travel in 4 hours?",
        "options": [
            "240 km",
            "250 km",
            "260 km",
            "270 km"
        ],
        "answer": 2,
        "explanation": "Distance = Speed × Time = 65 km/h × 4 h = 260 km.",
        "solution_html": "<strong>Step-by-Step Calculation:</strong><br>65 × 4 = (60 × 4) + (5 × 4) = 240 + 20 = 260 km."
    },
    {
        "id": 22,
        "question": "A train covers a journey of 450 km in 5 hours at uniform speed. What is the speed of the train?",
        "options": [
            "80 km/h",
            "90 km/h",
            "95 km/h",
            "100 km/h"
        ],
        "answer": 1,
        "explanation": "Speed = Distance ÷ Time = 450 km ÷ 5 h = 90 km/h.",
        "solution_html": "<strong>Calculation:</strong><br>450 ÷ 5 = 90 km/h."
    },
    {
        "id": 23,
        "question": "How long will it take a person walking at 4 km/h to cover a total distance of 28 km?",
        "options": [
            "5 hours",
            "6 hours",
            "7 hours",
            "8 hours"
        ],
        "answer": 2,
        "explanation": "Time = Distance ÷ Speed = 28 km ÷ 4 km/h = 7 hours.",
        "solution_html": "<strong>Calculation:</strong><br>28 ÷ 4 = 7 hours."
    },
    {
        "id": 24,
        "question": "A school has 185 students going on an educational tour. Each bus has 50 seats. How many buses are needed so every student gets a seat?",
        "options": [
            "3 buses",
            "4 buses",
            "5 buses",
            "6 buses"
        ],
        "answer": 1,
        "explanation": "185 ÷ 50 = 3 with a remainder of 35 students. 3 buses seat only 150 students, leaving 35 without seats. So 4 buses are required.",
        "solution_html": "<strong>Fleet Math:</strong><br>3 buses × 50 = 150 seats (35 students left behind).<br>4 buses × 50 = 200 seats (enough for all 185 students with 15 spare seats)."
    },
    {
        "id": 25,
        "question": "If hiring one bus costs ₹3,500, what is the total cost of hiring 4 buses for the school excursion?",
        "options": [
            "₹12,000",
            "₹13,500",
            "₹14,000",
            "₹15,000"
        ],
        "answer": 2,
        "explanation": "Total cost = 4 buses × ₹3,500 = ₹14,000.",
        "solution_html": "<strong>Calculation:</strong><br>4 × 3,500 = 4 × 35 × 100 = 140 × 100 = ₹14,000."
    },
    {
        "id": 26,
        "question": "An orchard has 40 rows of orange trees, with 35 trees in each row. How many total orange trees are in the orchard?",
        "options": [
            "140 trees",
            "1,200 trees",
            "1,400 trees",
            "14,000 trees"
        ],
        "answer": 2,
        "explanation": "Total trees = 40 rows × 35 trees/row = 1,400 trees.",
        "solution_html": "<strong>Calculation:</strong><br>40 × 35 = 4 × 35 × 10 = 140 × 10 = 1,400 trees."
    },
    {
        "id": 27,
        "question": "A library has 80 shelves, each holding 125 storybooks. How many total books are on the shelves?",
        "options": [
            "1,000 books",
            "10,000 books",
            "12,500 books",
            "100,000 books"
        ],
        "answer": 1,
        "explanation": "Total books = 80 × 125 = 10,000 books (Ten Thousand books!).",
        "solution_html": "<strong>Calculation:</strong><br>8 × 125 = 1,000.<br>80 × 125 = 10,000 books."
    },
    {
        "id": 28,
        "question": "A bullet train travels at 320 km/h. How far does it travel in 2 hours and 30 minutes (2.5 hours)?",
        "options": [
            "640 km",
            "720 km",
            "800 km",
            "960 km"
        ],
        "answer": 2,
        "explanation": "Distance = 320 km/h × 2.5 h = (320 × 2) + (320 × 0.5) = 640 + 160 = 800 km.",
        "solution_html": "<strong>Calculation:</strong><br>320 × 2 = 640 km<br>320 × 0.5 = 160 km<br>640 + 160 = 800 km."
    },
    {
        "id": 29,
        "question": "A spacecraft travels at 28,000 km/h. How far does it travel in 3 hours of orbital flight?",
        "options": [
            "56,000 km",
            "84,000 km",
            "100,000 km",
            "840,000 km"
        ],
        "answer": 1,
        "explanation": "Distance = 28,000 × 3 = 84,000 km.",
        "solution_html": "<strong>Calculation:</strong><br>28 × 3 = 84.<br>28,000 × 3 = 84,000 km."
    },
    {
        "id": 30,
        "question": "A small town has a population of 24,650. Over one year, 1,350 new residents move in. What is the new population?",
        "options": [
            "25,000",
            "26,000",
            "26,500",
            "25,900"
        ],
        "answer": 1,
        "explanation": "24,650 + 1,350 = 26,000.",
        "solution_html": "<strong>Sum:</strong><br>24,650 + 1,350 = 24,000 + 1,000 + 650 + 350 = 25,000 + 1,000 = 26,000."
    },

    # Challenge 4 (Questions 31 to 40): Pastime Mathematics Puzzles
    {
        "id": 31,
        "question": "In the river crossing puzzle, why can the boatman NOT leave the lion and the sheep alone together?",
        "options": [
            "The sheep will tease the lion",
            "The lion will eat the sheep",
            "The lion will jump into the river",
            "The boat will sink"
        ],
        "answer": 1,
        "explanation": "Being a carnivore, the lion will prey upon the sheep if the boatman is not there to protect it.",
        "solution_html": "<strong>Predator-Prey Constraint:</strong><br>Lion + Sheep without human presence = Lion eats Sheep."
    },
    {
        "id": 32,
        "question": "In the river crossing puzzle, why is it safe to leave the lion and the bundle of grass alone on the riverbank?",
        "options": [
            "Lions are strictly carnivorous and do not eat grass",
            "The grass is too heavy for the lion",
            "The lion is afraid of green grass",
            "The boatman ties the grass to the lion"
        ],
        "answer": 0,
        "explanation": "Lions do not eat grass! Therefore, leaving the lion and the grass bundle together on either bank is completely safe.",
        "solution_html": "<strong>Compatibility Insight:</strong><br>Lion + Grass = Safe combination! This allows the boatman to transport the sheep first."
    },
    {
        "id": 33,
        "question": "In the 2-player pebble game (take 1, 2, or 3 pebbles per turn), what is the key number that forms the winning strategy?",
        "options": [
            "Multiples of 2",
            "Multiples of 3",
            "Multiples of 4",
            "Multiples of 5"
        ],
        "answer": 2,
        "explanation": "Multiples of 4! Because 1 + 3 = 4 and 2 + 2 = 4, a player can always complement whatever the opponent takes to reach a total of 4.",
        "solution_html": "<strong>Complement Strategy:</strong><br>Opponent takes 1 → You take 3 (Total = 4)<br>Opponent takes 2 → You take 2 (Total = 4)<br>Opponent takes 3 → You take 1 (Total = 4)<br>Every full round eliminates exactly 4 pebbles."
    },
    {
        "id": 34,
        "question": "If you are playing the pebble game with 16 pebbles where taking the last pebble wins, should you go first or second to guarantee a win?",
        "options": [
            "Go first and take 2 pebbles",
            "Go second, because 16 is already a multiple of 4, so Player 2 can mirror Player 1 to maintain multiples of 4",
            "It does not matter, the game is purely luck",
            "Go first and take 4 pebbles"
        ],
        "answer": 1,
        "explanation": "16 is already a multiple of 4 (4 × 4 = 16). Player 2 can always complement Player 1's moves to 4, guaranteeing Player 2 takes the last pebble.",
        "solution_html": "<strong>Mathematical Proof:</strong><br>Since 16 is a multiple of 4, the second player has the winning strategy by maintaining the multiple-of-4 invariant."
    },
    {
        "id": 35,
        "question": "Pick digits 9 and 4. Form 94 and 49. What is 94 − 49?",
        "options": [
            "35",
            "45",
            "54",
            "49"
        ],
        "answer": 1,
        "explanation": "94 − 49 = 45. Notice that 45 is 9 × 5, where 5 is the difference between digits 9 and 4!",
        "solution_html": "<strong>Proof:</strong><br>94 − 49 = 45 = 9 × (9 − 4) = 9 × 5 = 45."
    },
    {
        "id": 36,
        "question": "In the digit-difference puzzle, why does the difference between any 2-digit number and its reversal always equal a multiple of 9?",
        "options": [
            "Because 9 is the largest single-digit number",
            "Because (10a + b) − (10b + a) = 9a − 9b = 9 × (a − b)",
            "Because all odd numbers are multiples of 9",
            "It only works on Tuesdays"
        ],
        "answer": 1,
        "explanation": "Algebraic proof: (10a + b) − (10b + a) = 9a − 9b = 9(a − b). In base-10, shifting place values by 1 always produces multiples of 9.",
        "solution_html": "<strong>Algebraic Proof:</strong><br>Let number = 10a + b.<br>Reversed number = 10b + a.<br>Difference = (10a + b) − (10b + a) = 9a − 9b = 9(a − b)."
    },
    {
        "id": 37,
        "question": "In the King's Horses puzzle, how many rooms are along each side of the square 3×3 stable?",
        "options": [
            "2 rooms",
            "3 rooms (Corner, Middle, Corner)",
            "4 rooms",
            "5 rooms"
        ],
        "answer": 1,
        "explanation": "A 3×3 grid has 3 rooms along each of its 4 sides: two corner rooms and one middle room.",
        "solution_html": "<strong>Stable Geometry:</strong><br>Top side: Top-Left Corner + Top Middle + Top-Right Corner = 3 rooms."
    },
    {
        "id": 38,
        "question": "Why did moving horses from the middle rooms into the corner rooms allow the caretaker to steal horses while keeping 5 horses on each side?",
        "options": [
            "Corner horses eat less hay",
            "Each corner room is counted as part of two sides at the same time",
            "The king forgot how to count to five",
            "The horses changed colour"
        ],
        "answer": 1,
        "explanation": "Corner rooms are shared by two adjacent sides. Each horse placed in a corner contributes to the count of both sides simultaneously.",
        "solution_html": "<strong>Corner-Sharing Logic:</strong><br>A horse in a corner room is counted twice—once when counting the horizontal side and once when counting the vertical side!"
    },
    {
        "id": 39,
        "question": "In the original stable arrangement, each of the 4 middle rooms had 5 horses and corners had 0 horses. What was the total count of horses?",
        "options": [
            "10 horses",
            "15 horses",
            "20 horses (4 × 5 = 20)",
            "25 horses"
        ],
        "answer": 2,
        "explanation": "4 middle rooms × 5 horses each = 20 horses. Each side had 0 + 5 + 0 = 5 horses.",
        "solution_html": "<strong>Original Verification:</strong><br>Side sum = 0 + 5 + 0 = 5.<br>Total horses = 4 middles × 5 = 20 horses."
    },
    {
        "id": 40,
        "question": "If each side of a 3×3 square stable must sum to 5 horses, and a caretaker places a total of 4 horses in the corners (1 in each of the 4 corners), what is the total number of horses in the stable?",
        "options": [
            "12 horses",
            "14 horses",
            "16 horses (20 − 4 = 16)",
            "20 horses"
        ],
        "answer": 2,
        "explanation": "Each side has 1 in corner + 3 in middle + 1 in corner = 5 horses. Total horses = 4 corners × 1 + 4 middles × 3 = 4 + 12 = 16 horses (which equals 20 − 4 = 16)!",
        "solution_html": "<strong>Formula Verification:</strong><br>Total Horses = 20 − C (where C is corner horses).<br>With C = 4 (1 in each corner):<br>Each middle needs 5 − (1 + 1) = 3 horses.<br>Total = 4(1) + 4(3) = 4 + 12 = 16 horses!"
    }
]

print("Mastery Quiz Questions (40 questions) authored successfully.")
