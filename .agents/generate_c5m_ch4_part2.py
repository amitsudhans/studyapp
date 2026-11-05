#!/usr/bin/env python3
"""
Generate Slides 9 to 16 data for NCERT Class 5 Mathematics - Chapter 4: We the Travellers - II
"""

slides_9_to_16 = [
    {
        "id": 9,
        "heading": "Mental Math",
        "tagline": "Quick Shortcuts to Powers of Ten and Mental Adjustments",
        "color": "from-teal-600 to-emerald-700",
        "badge": "Mental Calculation Strategies",
        "audio_text": (
            "Speed in calculation is the hallmark of a confident mathematician! "
            "Our textbook introduces powerful mental math shortcuts to calculate sums and differences without pencil and paper. "
            "The first strategy is rounding to the nearest power of ten. "
            "Suppose you need to add 99 to 345. Rather than doing column addition, think: 99 is just 1 less than 100! "
            "First add 100: 345 plus 100 is 445. Then subtract the extra 1: 445 minus 1 is 444! You get the exact answer in a single breath. "
            "What if you need to subtract 9 from 83? 9 is 1 less than 10. Subtract 10 to get 73, then add back 1 to get 74! "
            "The same shortcut applies to 999: add 1,000 and subtract 1. "
            "Another mental technique is making tens and hundreds: to add 68 and 37, take 2 from 37 and give it to 68 to make a friendly 70! "
            "Now add 70 and 35 to get 105 instantly. "
            "Mental math transforms numbers into flexible building blocks."
        ),
        "theory_blocks": [
            {
                "title": "Adding 9, 99, 999 (+100 - 1)",
                "content": "To add 99: Add 100, then subtract 1. Example: 456 + 99 = (456 + 100) - 1 = 556 - 1 = 555.",
                "icon": "⚡"
            },
            {
                "title": "Subtracting 9, 99 (-100 + 1)",
                "content": "To subtract 99: Subtract 100, then add 1. Example: 350 - 99 = (350 - 100) + 1 = 250 + 1 = 251.",
                "icon": "🔄"
            },
            {
                "title": "Friendly Number Transfer",
                "content": "To add 198 + 45: Take 2 from 45 and add to 198 to create 200! Then 200 + 43 = 243 in seconds.",
                "icon": "🤝"
            }
        ],
        "checkpoints": [
            {
                "question": "Using the mental shortcut, what is 267 + 99?",
                "options": [
                    "366 (267 + 100 - 1)",
                    "367",
                    "365",
                    "356"
                ],
                "correct": 0,
                "feedback": "Correct! 267 + 100 = 367, minus 1 = 366."
            },
            {
                "question": "What is 142 - 9 using mental adjustment?",
                "options": [
                    "133 (142 - 10 + 1)",
                    "131",
                    "135",
                    "132"
                ],
                "correct": 0,
                "feedback": "Spot on! 142 - 10 = 132, plus 1 = 133."
            }
        ]
    },
    {
        "id": 10,
        "heading": "Palindrome Numbers",
        "tagline": "Exploring Symmetrical Numbers That Read the Same Forwards and Backwards",
        "color": "from-indigo-600 to-purple-700",
        "badge": "Number Pattern Wonder",
        "audio_text": (
            "Look at the word NOON or the name NITIN: whether you read them from left to right or right to left, they read exactly the same! "
            "In mathematics, numbers with this magical forward-backward symmetry are called palindrome numbers! "
            "A palindrome number reads identically in both directions. "
            "Single-digit numbers like 7 are trivially palindromes. "
            "In two-digit numbers, the palindromes are numbers with identical digits: 11, 22, 33, 44, 55, 66, 77, 88, and 99! "
            "In three-digit numbers, the hundreds digit and the ones digit must match, such as 121, 363, 505, 787, and 999. "
            "In four-digit numbers, the outer two digits match and the inner two digits match, such as 2,442 or 8,558! "
            "Did you know that many ordinary numbers can be turned into palindromes through a reverse-and-add routine? "
            "Take 43: reverse its digits to get 34. Now add: 43 plus 34 equals 77, an instant palindrome! "
            "Palindromic patterns reveal the poetic symmetry hidden within arithmetic."
        ),
        "theory_blocks": [
            {
                "title": "Definition of Palindrome",
                "content": "A number that remains unchanged when its digits are reversed. Examples: 55, 121, 383, 2,332, 54,445.",
                "icon": "🪞"
            },
            {
                "title": "3-Digit Palindrome Structure",
                "content": "A 3-digit palindrome has the form ABA, where the first and last digits (Hundreds and Ones) are identical (A != 0).",
                "icon": "🔢"
            },
            {
                "title": "The Reverse-and-Add Trick",
                "content": "Start with a number: e.g. 52. Reverse digits: 25. Add them: 52 + 25 = 77! 77 is a palindrome.",
                "icon": "🪄"
            }
        ],
        "checkpoints": [
            {
                "question": "Which of the following numbers is a palindrome?",
                "options": [
                    "484",
                    "485",
                    "348",
                    "488"
                ],
                "correct": 0,
                "feedback": "Correct! 484 reversed is 484, reading identically forward and backward."
            },
            {
                "question": "How many 2-digit palindrome numbers exist in total (from 10 to 99)?",
                "options": [
                    "9 (11, 22, 33, 44, 55, 66, 77, 88, 99)",
                    "10",
                    "8",
                    "11"
                ],
                "correct": 0,
                "feedback": "Spot on! There are exactly 9 two-digit palindromes: 11, 22, 33, 44, 55, 66, 77, 88, and 99."
            }
        ]
    },
    {
        "id": 11,
        "heading": "Grid Puzzles",
        "tagline": "Arranging Numbers 1 Through 9 in Monotonic 3×3 Matrices",
        "color": "from-violet-600 to-indigo-700",
        "badge": "Mathematical Logic Puzzle",
        "audio_text": (
            "Here is an intriguing challenge from our textbook: arranging the numbers 1 through 9 inside a 3 by 3 grid! "
            "The rule requires that every single row from left to right must follow an increasing order, and every single column from top to bottom must also follow an increasing order! "
            "No number from 1 to 9 may be repeated. "
            "Where must the smallest number, 1, be placed? "
            "Because 1 is smaller than every other number, it must be smaller than everything to its right and everything below it. "
            "Therefore, 1 must always occupy the top-left corner! "
            "Similarly, where must the largest number, 9, reside? "
            "Because 9 is greater than all other numbers, it must be at the end of its row and the bottom of its column: 9 must occupy the bottom-right corner! "
            "The remaining numbers 2 through 8 can be arranged in several valid configurations as long as both horizontal and vertical increasing conditions are satisfied. "
            "Grid puzzles train your brain to think with spatial constraints and monotonic ordering."
        ),
        "theory_blocks": [
            {
                "title": "The Monotonic Grid Rule",
                "content": "For every cell (r, c): Cell(r, c) < Cell(r, c+1) (increasing across rows) and Cell(r, c) < Cell(r+1, c) (increasing down columns).",
                "icon": "📐"
            },
            {
                "title": "Corner Invariants",
                "content": "Top-Left cell MUST be 1 (global minimum). Bottom-Right cell MUST be 9 (global maximum).",
                "icon": "📌"
            },
            {
                "title": "Valid Solutions",
                "content": "Standard reading grid: Row 1: [1, 2, 3]; Row 2: [4, 5, 6]; Row 3: [7, 8, 9]. Another valid setup: Row 1: [1, 2, 4]; Row 2: [3, 5, 7]; Row 3: [6, 8, 9].",
                "icon": "🧩"
            }
        ],
        "checkpoints": [
            {
                "question": "In a 3×3 grid of numbers 1 to 9 with strictly increasing rows and columns, what number must be in the top-left cell?",
                "options": [
                    "1",
                    "5",
                    "9",
                    "3"
                ],
                "correct": 0,
                "feedback": "Correct! As the smallest number (global minimum), 1 must be placed at the top-left."
            },
            {
                "question": "Which number must be placed in the bottom-right cell of the increasing 3×3 grid?",
                "options": [
                    "9",
                    "8",
                    "7",
                    "5"
                ],
                "correct": 0,
                "feedback": "Spot on! 9 is the largest number and must terminate both the last row and last column."
            }
        ]
    },
    {
        "id": 12,
        "heading": "Even and Odd",
        "tagline": "Paired Dot Arrangements and the Laws of Sum Parity",
        "color": "from-cyan-600 to-blue-700",
        "badge": "Number Parity Principles",
        "audio_text": (
            "What makes a number even or odd? The secret lies in pairing! "
            "An even number can be arranged into complete pairs of two with nothing left over. "
            "Any number ending in 0, 2, 4, 6, or 8 is an even number. "
            "An odd number, when arranged in pairs, always leaves exactly one solitary dot without a partner! "
            "Any number ending in 1, 3, 5, 7, or 9 is an odd number. "
            "Now observe what happens when we add pairs of numbers: "
            "Even plus Even equals Even! Two complete sets of pairs join together to make a larger set of complete pairs. For example, 4 plus 6 equals 10! "
            "Odd plus Odd also equals Even! Why? Because the two lonely leftover dots pair up with each other to form a new complete pair! For example, 3 plus 5 equals 8! "
            "Even plus Odd always equals Odd, because the single leftover dot has nobody to pair with. For example, 4 plus 5 equals 9! "
            "These parity laws allow us to verify sums and predict outcomes instantaneously."
        ),
        "theory_blocks": [
            {
                "title": "The Pairing Test",
                "content": "Even = Divisible by 2, zero remainder (complete pairs). Odd = Leaves a remainder of 1 when divided by 2 (one leftover item).",
                "icon": "👥"
            },
            {
                "title": "The 3 Addition Parity Laws",
                "content": "1. Even + Even = Even (e.g. 6 + 8 = 14); 2. Odd + Odd = Even (e.g. 5 + 7 = 12); 3. Even + Odd = Odd (e.g. 4 + 7 = 11).",
                "icon": "⚖️"
            },
            {
                "title": "Consecutive Parity",
                "content": "Consecutive numbers always alternate: Even, Odd, Even, Odd... Therefore, adding any 2 consecutive numbers always gives an ODD sum (Even + Odd = Odd)!",
                "icon": "🔄"
            }
        ],
        "checkpoints": [
            {
                "question": "What is the parity of the sum when you add two odd numbers (e.g., 7 + 9)?",
                "options": [
                    "Always Even",
                    "Always Odd",
                    "Sometimes Even, Sometimes Odd",
                    "Zero"
                ],
                "correct": 0,
                "feedback": "Correct! The two leftover dots from the odd numbers pair up, making the total sum strictly Even (7 + 9 = 16)."
            },
            {
                "question": "You add an even number and an odd number (e.g., 8 + 5). What is the resulting sum?",
                "options": [
                    "Always Odd",
                    "Always Even",
                    "A negative number",
                    "A multiple of 10"
                ],
                "correct": 0,
                "feedback": "Spot on! Even + Odd is always Odd (8 + 5 = 13)."
            }
        ]
    },
    {
        "id": 13,
        "heading": "Logic Puzzles",
        "tagline": "Mastering Coin Combinations and Torch Switch Parity",
        "color": "from-emerald-600 to-green-700",
        "badge": "Deductive Reasoning",
        "audio_text": (
            "Our textbook presents delightful thinking puzzles involving coin combinations and torch switches! "
            "In the coin puzzle: Suppose you have a total of ₹ 25 made up of 2-rupee and 5-rupee coins. "
            "How many coins of each type could you have? "
            "Notice that ₹ 25 is an odd number. Any number of 2-rupee coins will always give an even sum. "
            "Therefore, the 5-rupee coins must contribute an odd sum, meaning there must be an odd number of 5-rupee coins! "
            "If we take one 5-rupee coin, the remaining ₹ 20 requires ten 2-rupee coins: 10 times 2 plus 5 equals 25! "
            "If we take three 5-rupee coins, that gives ₹ 15, and the remaining ₹ 10 requires five 2-rupee coins! "
            "Now look at the torch switch puzzle: A flashlight switch toggles between ON and OFF. "
            "Starting from OFF, press 1 turns it ON. Press 2 turns it OFF. "
            "Every odd press leaves the torch ON; every even press leaves the torch OFF! "
            "If you press the switch 47 times, 47 is an odd number, so the torch will be ON! "
            "Mathematical parity turns tricky puzzles into crystal-clear logic."
        ),
        "theory_blocks": [
            {
                "title": "Coin Combination Analysis",
                "content": "To get ₹ 25 from ₹ 2 and ₹ 5 coins: 2a + 5b = 25. Since 2a is even and 25 is odd, 5b must be odd. Hence b must be odd (b = 1, 3, or 5).",
                "icon": "🪙"
            },
            {
                "title": "Torch Switch Parity",
                "content": "Starting state: OFF. Press 1 (Odd) = ON; Press 2 (Even) = OFF; Press 3 (Odd) = ON... Press N: Odd N = ON, Even N = OFF.",
                "icon": "🔦"
            },
            {
                "title": "Binary State Logic",
                "content": "Two-state systems (ON/OFF, Open/Closed, Heads/Tails) obey modulo-2 arithmetic: State = Count % 2.",
                "icon": "💡"
            }
        ],
        "checkpoints": [
            {
                "question": "A torch is initially turned OFF. If the button is pressed 35 times, what state is the torch in?",
                "options": [
                    "ON (35 is an odd number)",
                    "OFF (35 is an even number)",
                    "Flickering half-way",
                    "Completely broken"
                ],
                "correct": 0,
                "feedback": "Correct! Starting from OFF, every odd number of presses leaves the torch ON."
            },
            {
                "question": "Can you make exactly ₹ 25 using only 2-rupee coins?",
                "options": [
                    "No, because any number of 2-rupee coins produces an even sum, and 25 is odd",
                    "Yes, using 12 coins",
                    "Yes, using 13 coins",
                    "Yes, using 12.5 coins"
                ],
                "correct": 0,
                "feedback": "Spot on! 2 × any whole number is always even, so ₹ 25 (odd) cannot be made with ₹ 2 coins alone."
            }
        ]
    },
    {
        "id": 14,
        "heading": "Mountain Peaks",
        "tagline": "Statistical Analysis of Indian Mountaineer Priyanka Mohite's Expeditions",
        "color": "from-amber-600 to-orange-700",
        "badge": "Data Analysis & Altitudes",
        "audio_text": (
            "Let us celebrate the extraordinary achievements of Indian mountaineer Priyanka Mohite, featured in our textbook! "
            "Priyanka Mohite is the first Indian woman to climb five peaks above 8,000 metres! "
            "Look at the majestic Himalayan peaks she scaled: "
            "Mount Everest stands at 8,849 metres above sea level. "
            "Kanchenjunga, the third highest peak on Earth located on the India-Nepal border, reaches 8,586 metres. "
            "Makalu rises to 8,485 metres, Lhotse to 8,516 metres, and Annapurna to 8,091 metres. "
            "Comparing these colossal heights gives us rich real-world subtraction practice! "
            "How much taller is Mount Everest than Mount Annapurna? "
            "We subtract: 8,849 minus 8,091! "
            "9 minus 1 is 8 Ones. 4 minus 9 in the Tens requires borrowing from 8 Hundreds, leaving 7 Hundreds: 14 minus 9 is 5 Tens. "
            "7 minus 0 is 7 Hundreds. 8 minus 8 is 0 Thousands. "
            "Everest is 758 metres taller than Annapurna! "
            "Mathematics allows us to measure and appreciate the highest points on our planet."
        ),
        "theory_blocks": [
            {
                "title": "Priyanka Mohite's 8,000m Record",
                "content": "Recipient of the Tenzing Norgay National Adventure Award, she summited Everest (8,849 m), Kanchenjunga (8,586 m), Lhotse (8,516 m), Makalu (8,485 m), and Annapurna (8,091 m).",
                "icon": "🏔️"
            },
            {
                "title": "Elevation Comparison",
                "content": "Height Difference = Peak A - Peak B. Example: Everest (8,849 m) - Kanchenjunga (8,586 m) = 263 metres.",
                "icon": "📊"
            },
            {
                "title": "Ascent Math",
                "content": "Climbers establish high-altitude camps (Base Camp, Camp 1, Camp 2, Camp 3). Each day's elevation gain is calculated using subtraction.",
                "icon": "🧗‍♀️"
            }
        ],
        "checkpoints": [
            {
                "question": "Mount Everest is 8,849 metres and Kanchenjunga is 8,586 metres. What is the difference in height?",
                "options": [
                    "263 metres",
                    "363 metres",
                    "243 metres",
                    "163 metres"
                ],
                "correct": 0,
                "feedback": "Correct! 8,849 - 8,586 = 263 metres. Check: 8,586 + 263 = 8,849 m."
            },
            {
                "question": "A mountaineer climbs from Base Camp at 5,364 m to Camp 1 at 6,065 m. How many vertical metres did they gain?",
                "options": [
                    "701 metres",
                    "601 metres",
                    "801 metres",
                    "711 metres"
                ],
                "correct": 0,
                "feedback": "Spot on! 6,065 - 5,364 = 701 vertical metres."
            }
        ]
    },
    {
        "id": 15,
        "heading": "Math Mela",
        "tagline": "District Competition Data: Certificates, Cricket Runs, and Factory Records",
        "color": "from-teal-600 to-blue-700",
        "badge": "Comprehensive Review",
        "audio_text": (
            "We conclude our chapter's core journey with the grand Math Metric Mela! "
            "A district-level math festival brings together students, teachers, and schools for fun competitions. "
            "Let us examine the festival's event data: "
            "The organizing committee printed 2,500 certificates of participation. "
            "On the day of the Mela, 1,875 students attended and received certificates. "
            "How many surplus certificates were left over? "
            "We subtract: 2,500 minus 1,875! "
            "Borrowing across zeros gives: 2,500 minus 1,875 equals 625 certificates remaining. "
            "In the cricket pavilion, Team A scored 348 runs and Team B scored 295 runs. The total runs scored in the match were 348 plus 295, which equals 643 runs! "
            "And in savings arithmetic: if a student saves ₹ 45 in Week 1, ₹ 60 in Week 2, and ₹ 75 in Week 3, their total savings equal ₹ 180. "
            "Every real-life event, from sports to festivals, runs on solid addition and subtraction."
        ),
        "theory_blocks": [
            {
                "title": "Certificate Inventory Math",
                "content": "Printed (2,500) - Distributed (1,875) = Surplus Remaining (625 certificates). Always verify: 1,875 + 625 = 2,500.",
                "icon": "📜"
            },
            {
                "title": "Cricket Match Aggregate",
                "content": "Match Total Runs = Team A Runs + Team B Runs. Example: 348 + 295 = 643 runs.",
                "icon": "🏏"
            },
            {
                "title": "Cumulative Weekly Savings",
                "content": "Total Savings = Week 1 + Week 2 + Week 3... Tracking personal savings reinforces consistent budgeting and financial literacy.",
                "icon": "💰"
            }
        ],
        "checkpoints": [
            {
                "question": "A school ordered 1,500 medals for sports day. 1,180 medals were awarded to winners. How many medals remained?",
                "options": [
                    "320 medals",
                    "420 medals",
                    "220 medals",
                    "380 medals"
                ],
                "correct": 0,
                "feedback": "Correct! 1,500 - 1,180 = 320 medals."
            },
            {
                "question": "A cricketer scored 136 runs in the first innings and 89 runs in the second innings. What was their total score?",
                "options": [
                    "225 runs",
                    "215 runs",
                    "235 runs",
                    "220 runs"
                ],
                "correct": 0,
                "feedback": "Spot on! 136 + 89 = 225 total runs."
            }
        ]
    },
    {
        "id": 16,
        "heading": "Travel Lab",
        "tagline": "Integrated Multi-Leg Expedition and Fuel Expense Calculator",
        "color": "from-blue-600 to-indigo-700",
        "badge": "Expedition Synthesis Sandbox",
        "audio_text": (
            "Welcome to the ultimate Travel Arithmetic Laboratory! "
            "Here, all the concepts we have mastered come together into an interactive expedition planner. "
            "You can choose a travel route across India, select your transport vehicle—from an eco-friendly bus to an electric train or family car—and dynamically calculate total journey distance, fuel consumed in litres, and total travel cost. "
            "You can also test our palindrome detector by typing any odometer reading to see if it forms a symmetrical palindrome number! "
            "Notice how increasing the number of passengers traveling together in a bus drastically lowers the fuel and carbon footprint per person. "
            "Experiment with multi-leg journeys, verify route subtractions, and test mental math shortcuts. "
            "You now hold the power of mathematical travel planning in your hands!"
        ),
        "theory_blocks": [
            {
                "title": "Multi-Leg Journey Synthesis",
                "content": "Total Distance = Leg 1 + Leg 2 + Leg 3. Total Fuel = Total Distance / Vehicle Mileage. Total Cost = Fuel Litres × Fuel Price.",
                "icon": "🗺️"
            },
            {
                "title": "Per-Capita Fuel Footprint",
                "content": "Fuel per Passenger = Total Fuel / Passengers. Taking a bus with 40 people cuts individual fuel consumption by up to 80% compared to a solo car trip.",
                "icon": "👥"
            },
            {
                "title": "Live Palindrome Checker",
                "content": "Any odometer distance (e.g. 12,321 km) can be verified instantly for front-to-back palindromic symmetry.",
                "icon": "🪞"
            }
        ],
        "checkpoints": [
            {
                "question": "A vehicle travels a total distance of 450 km. If its mileage is 15 km per litre, how many litres of fuel are needed?",
                "options": [
                    "30 litres (450 / 15)",
                    "25 litres",
                    "35 litres",
                    "45 litres"
                ],
                "correct": 0,
                "feedback": "Correct! Fuel needed = 450 km / 15 km/L = 30 litres."
            },
            {
                "question": "If diesel costs ₹ 90 per litre, what is the cost of 30 litres of diesel?",
                "options": [
                    "₹ 2,700",
                    "₹ 2,400",
                    "₹ 3,000",
                    "₹ 2,600"
                ],
                "correct": 0,
                "feedback": "Spot on! 30 litres × ₹ 90 = ₹ 2,700."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Authored Slides 9 to 16. Count: {len(slides_9_to_16)}")

