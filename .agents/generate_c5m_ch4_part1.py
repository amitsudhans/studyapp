#!/usr/bin/env python3
"""
Generate Slides 1 to 8 data for NCERT Class 5 Mathematics - Chapter 4: We the Travellers - II
"""

slides_1_to_8 = [
    {
        "id": 1,
        "heading": "Equal Sums",
        "tagline": "Balancing Number Groups with Minimal Swaps",
        "color": "from-amber-500 to-orange-600",
        "badge": "Class 5 Maths • Chapter 4",
        "audio_text": (
            "Welcome, young travellers and mathematicians! Today we begin our journey into We the Travellers - II. "
            "We start with a fascinating balancing puzzle from our textbook: making sums equal. "
            "Imagine you have two groups of number cards. Group A has numbers whose sum is larger than Group B. "
            "Our goal is to make the sum of both groups exactly equal by swapping pairs of numbers with the fewest moves possible! "
            "To solve this scientifically, first calculate the sum of each group and find their difference. "
            "If the difference between Group A and Group B is D, then swapping a card from Group A with a card from Group B must have a difference of exactly D divided by 2! "
            "For example, if Group A sums to 48 and Group B sums to 40, the difference is 8. "
            "We must find a card in Group A that is 8 divided by 2, or 4 units larger than a card in Group B. "
            "When we swap these two cards, both groups balance perfectly at 44! "
            "This algebraic secret helps us balance loads on transport vehicles, cargo ships, and airplane cargo holds every single day."
        ),
        "theory_blocks": [
            {
                "title": "The Balancing Rule",
                "content": "To balance two groups with difference D in a single swap, find a number in the larger group that exceeds a number in the smaller group by exactly D / 2.",
                "icon": "⚖️"
            },
            {
                "title": "Target Equilibrium Sum",
                "content": "The balanced target sum is always the total combined sum of all cards divided by 2. Total Sum = Sum(A) + Sum(B); Target = Total / 2.",
                "icon": "🎯"
            },
            {
                "title": "Real-World Balance",
                "content": "Aircraft luggage loaders and ship captains use this exact logic to distribute cargo evenly between left and right holds to ensure safe travel.",
                "icon": "✈️"
            }
        ],
        "checkpoints": [
            {
                "question": "Group A sums to 50 and Group B sums to 40. What must be the difference between the two swapped numbers to balance both groups?",
                "options": [
                    "5 (Difference of 10 divided by 2)",
                    "10",
                    "20",
                    "2"
                ],
                "correct": 0,
                "feedback": "Correct! Total difference is 50 - 40 = 10. The swapped numbers must differ by 10 / 2 = 5 to make both groups equal to 45."
            },
            {
                "question": "If Group A has 25 and Group B has 17, and all other cards are identical, how much larger is Group A's sum?",
                "options": [
                    "8",
                    "4",
                    "16",
                    "12"
                ],
                "correct": 0,
                "feedback": "Spot on! 25 - 17 = 8. Swapping them changes the group balance by 8."
            }
        ]
    },
    {
        "id": 2,
        "heading": "Fuel Mileage",
        "tagline": "Comparing Fuel Needs and Eco-Friendly Travel",
        "color": "from-emerald-600 to-teal-700",
        "badge": "Fuel & Conservation Arithmetic",
        "audio_text": (
            "Every vehicle that carries travellers requires energy, usually in the form of petrol, diesel, or electricity. "
            "Different vehicles consume vastly different amounts of fuel depending on their engine power, weight, and the number of passengers they carry. "
            "A lightweight motorcycle can travel up to 50 kilometres on a single litre of petrol! "
            "A family car might travel 15 kilometres per litre, while a school bus or large truck might travel only 4 to 6 kilometres per litre of diesel. "
            "However, notice something crucial: although a bus consumes more fuel than a motorcycle, it carries 50 students at once! "
            "When we divide the fuel consumed by the number of travellers, public transport like buses and electric trains is far more efficient per passenger than single-occupant cars. "
            "Conserving fuel saves money, reduces harmful exhaust emissions, and keeps our air clean for everyone. "
            "Let us calculate vehicle fuel consumption and explore eco-wise choices."
        ),
        "theory_blocks": [
            {
                "title": "Fuel Consumption Comparison",
                "content": "Motorbike: ~50 km/L (1-2 persons); Car: ~15 km/L (4-5 persons); Minibus: ~8 km/L (15-20 persons); Diesel Bus: ~4 km/L (50 persons).",
                "icon": "⛽"
            },
            {
                "title": "Per-Passenger Efficiency",
                "content": "A bus using 10 litres to travel 40 km carries 50 people. That is 0.2 litres per student! Cars carry far fewer passengers for the fuel burned.",
                "icon": "🚌"
            },
            {
                "title": "Eco-Friendly Driving",
                "content": "Smooth driving, proper tire pressure, turning off engines at traffic signals, and using public transit minimize pollution and conserve petroleum.",
                "icon": "🌱"
            }
        ],
        "checkpoints": [
            {
                "question": "If a car travels 15 kilometres on 1 litre of petrol, how many kilometres can it travel on 6 litres?",
                "options": [
                    "90 km",
                    "60 km",
                    "75 km",
                    "120 km"
                ],
                "correct": 0,
                "feedback": "Correct! Distance = Fuel × Mileage = 6 litres × 15 km/L = 90 km."
            },
            {
                "question": "Why is travelling by public bus more fuel-efficient per person than driving multiple cars?",
                "options": [
                    "One bus carries up to 50 passengers, reducing per-person fuel used",
                    "Buses do not consume any fuel at all",
                    "Buses travel at the speed of light",
                    "Buses only travel downhill"
                ],
                "correct": 0,
                "feedback": "Spot on! Spreading the fuel consumption over 50 passengers dramatically cuts fuel use per traveller."
            }
        ]
    },
    {
        "id": 3,
        "heading": "Place Value",
        "tagline": "Adding 2-Digit and 3-Digit Numbers with Column Regrouping",
        "color": "from-blue-600 to-indigo-700",
        "badge": "Addition with Regrouping",
        "audio_text": (
            "When calculating travel distances and fuel bills, we frequently add 2-digit and 3-digit numbers using place value tables! "
            "In our base-ten number system, every column has a strict capacity of nine units. "
            "The moment we gather 10 Ones, they bundle together into 1 Ten, which carries over into the Tens column! "
            "Similarly, when 10 Tens accumulate, they bundle into 1 Hundred and carry over into the Hundreds column. "
            "Let us add 258 and 175. First, align the digits strictly in their columns: Hundreds, Tens, and Ones. "
            "Add the Ones: 8 plus 5 equals 13 Ones. We write 3 in the Ones column and carry over 1 Ten to the Tens column. "
            "Now add the Tens: 5 plus 7 equals 12, plus the carried 1 Ten gives 13 Tens! We write 3 in the Tens column and carry over 1 Hundred. "
            "Finally, add the Hundreds: 2 plus 1 equals 3, plus the carried 1 gives 4 Hundreds. "
            "The total sum is 433! Column alignment and systematic carrying make large additions error-free."
        ),
        "theory_blocks": [
            {
                "title": "The Regrouping Law",
                "content": "10 Ones bundle into 1 Ten (carries left); 10 Tens bundle into 1 Hundred; 10 Hundreds bundle into 1 Thousand.",
                "icon": "📦"
            },
            {
                "title": "Strict Column Alignment",
                "content": "Always align digits from right to left starting at the Ones place: Ones under Ones, Tens under Tens, Hundreds under Hundreds.",
                "icon": "📊"
            },
            {
                "title": "Step-by-Step Addition",
                "content": "Step 1: Add Ones, carry over any 10s. Step 2: Add Tens including carried ten. Step 3: Add Hundreds including carried hundred.",
                "icon": "✍️"
            }
        ],
        "checkpoints": [
            {
                "question": "What is the sum of 348 and 275?",
                "options": [
                    "623",
                    "613",
                    "523",
                    "633"
                ],
                "correct": 0,
                "feedback": "Correct! Ones: 8+5=13 (write 3, carry 1); Tens: 4+7+1=12 (write 2, carry 1); Hundreds: 3+2+1=6. Result = 623."
            },
            {
                "question": "When adding the Ones column, you get 16. What digit is written in the Ones place, and what is carried over?",
                "options": [
                    "Write 6, carry over 1 Ten",
                    "Write 1, carry over 6 Tens",
                    "Write 16 in the Ones place",
                    "Carry over 16 to Hundreds"
                ],
                "correct": 0,
                "feedback": "Spot on! 16 Ones = 1 Ten and 6 Ones. Write 6, carry 1."
            }
        ]
    },
    {
        "id": 4,
        "heading": "Inverse Operations",
        "tagline": "Connecting Addition and Subtraction Fact Families",
        "color": "from-teal-600 to-cyan-700",
        "badge": "Inverse Relationship",
        "audio_text": (
            "Addition and subtraction are inverse operations: they are two sides of the very same mathematical coin! "
            "Addition puts groups together to find the whole, while subtraction takes a part away from the whole to find the other part. "
            "Whenever you know an addition fact, you instantly get two related subtraction facts for free! "
            "For instance, consider the addition fact: 125 plus 75 equals 200. "
            "From this single fact, we immediately know that: 200 minus 75 equals 125, and 200 minus 125 equals 75! "
            "This relationship is an invaluable tool for every traveller and engineer. "
            "Whenever you solve a subtraction problem, you can verify your answer with 100% certainty by adding your difference back to the smaller number. "
            "If the sum equals the original starting number, your calculation is proven correct! "
            "Inverse thinking transforms arithmetic into self-checking magic."
        ),
        "theory_blocks": [
            {
                "title": "The Fact Family Triangle",
                "content": "Three related numbers form a fact family: Part 1 + Part 2 = Whole; Whole - Part 1 = Part 2; Whole - Part 2 = Part 1.",
                "icon": "🔺"
            },
            {
                "title": "Verification by Addition",
                "content": "To check subtraction: Difference + Subtrahend = Minuend. If 450 - 180 = 270, then check: 270 + 180 = 450!",
                "icon": "✅"
            },
            {
                "title": "Missing Addend Problems",
                "content": "If a vehicle needs 50 litres and currently has 28 litres: 28 + ? = 50. We solve it using subtraction: 50 - 28 = 22 litres.",
                "icon": "❓"
            }
        ],
        "checkpoints": [
            {
                "question": "Which subtraction sentence is directly derived from the addition fact 140 + 85 = 225?",
                "options": [
                    "225 - 85 = 140",
                    "225 + 85 = 310",
                    "140 - 85 = 55",
                    "225 - 140 = 225"
                ],
                "correct": 0,
                "feedback": "Correct! Whole (225) minus Part (85) equals Part (140)."
            },
            {
                "question": "You calculate 500 - 320 = 180. Which addition confirms your answer is correct?",
                "options": [
                    "180 + 320 = 500",
                    "500 + 320 = 820",
                    "180 + 500 = 680",
                    "320 - 180 = 140"
                ],
                "correct": 0,
                "feedback": "Spot on! Difference (180) + Subtrahend (320) = Minuend (500)."
            }
        ]
    },
    {
        "id": 5,
        "heading": "Fuel Problems",
        "tagline": "Practical Word Problems, Regrouping, and Verification",
        "color": "from-purple-600 to-indigo-700",
        "badge": "Applied Arithmetic",
        "audio_text": (
            "Let us apply our skills to real-world travel word problems from our textbook! "
            "Consider this practical scenario: A school tour minibus starts the morning with 38 litres of diesel in its fuel tank. "
            "At a highway fuel pump, the driver fills the tank completely until it reaches its full capacity of 65 litres. "
            "How many litres of diesel were added at the fuel pump? "
            "This is a classic missing-part problem: 38 litres plus the added fuel equals 65 litres. "
            "To find the added fuel, we subtract: 65 minus 38! "
            "In the Ones column, we have 5 minus 8. Since 5 is smaller than 8, we regroup: borrow 1 Ten from the 6 Tens, leaving 5 Tens. "
            "The borrowed 1 Ten equals 10 Ones, making 10 plus 5 equal to 15 Ones! "
            "Now subtract: 15 minus 8 equals 7 Ones. In the Tens column, 5 minus 3 equals 2 Tens. "
            "The answer is 27 litres! Let us check: 38 plus 27 equals 65 litres. Perfectly verified!"
        ),
        "theory_blocks": [
            {
                "title": "Analyzing Word Problems",
                "content": "Step 1: Identify given quantities (Initial = 38 L, Final = 65 L). Step 2: Determine operation (Final - Initial = Added). Step 3: Calculate with regrouping.",
                "icon": "📝"
            },
            {
                "title": "Subtraction Regrouping (Borrowing)",
                "content": "When the top digit is smaller than the bottom digit, borrow 1 from the next higher place value: 1 Ten becomes 10 Ones.",
                "icon": "🔄"
            },
            {
                "title": "Always Verify",
                "content": "Check your answer: Initial Fuel (38) + Added Fuel (27) = 65. Verification gives 100% confidence.",
                "icon": "🔍"
            }
        ],
        "checkpoints": [
            {
                "question": "A truck's fuel tank has a capacity of 120 litres. It currently contains 74 litres. How much fuel is needed to fill it completely?",
                "options": [
                    "46 litres",
                    "56 litres",
                    "36 litres",
                    "54 litres"
                ],
                "correct": 0,
                "feedback": "Correct! 120 - 74 = 46 litres. Check: 74 + 46 = 120."
            },
            {
                "question": "A traveller started with ₹ 850 and spent ₹ 365 on vehicle fuel. How much money remains?",
                "options": [
                    "₹ 485",
                    "₹ 495",
                    "₹ 515",
                    "₹ 385"
                ],
                "correct": 0,
                "feedback": "Spot on! 850 - 365 = 485. Check: 485 + 365 = 850."
            }
        ]
    },
    {
        "id": 6,
        "heading": "Consecutive Numbers",
        "tagline": "Discovering Sums, Symmetries, and Middle-Number Multipliers",
        "color": "from-rose-600 to-pink-700",
        "badge": "Number Pattern Investigation",
        "audio_text": (
            "Now let us examine a captivating pattern from our textbook: sums of consecutive numbers! "
            "Consecutive numbers are whole numbers that follow one after another in order without skipping, such as 4, 5, and 6, or 21, 22, and 23. "
            "Look what happens when we add 3 consecutive numbers: "
            "Take 1, 2, and 3: their sum is 1 plus 2 plus 3, which equals 6. Notice that 6 is exactly 3 times the middle number, 2! "
            "Try 4, 5, and 6: their sum is 4 plus 5 plus 6, which equals 15. 15 is exactly 3 times the middle number, 5! "
            "Why does this always happen? Because 4 is 1 less than 5, and 6 is 1 more than 5. The minus 1 and plus 1 cancel out perfectly! "
            "Therefore, the sum of any 3 consecutive numbers is always 3 times the middle number. "
            "What about consecutive groups of 4 numbers, such as 1, 2, 3, and 4? Their sum is 10, an even number. "
            "For any 4 consecutive numbers, the sum is always an even number, and consecutive 4-number sums increase by 4 each step! "
            "These mathematical symmetries make mental calculation effortless."
        ),
        "theory_blocks": [
            {
                "title": "3 Consecutive Numbers Rule",
                "content": "For numbers (n-1), n, (n+1): Sum = 3 × Middle Number (n). Example: 10 + 11 + 12 = 3 × 11 = 33.",
                "icon": "🔢"
            },
            {
                "title": "4 Consecutive Numbers Rule",
                "content": "Sum of 4 consecutive numbers is always an even number! Example: 1+2+3+4 = 10; 2+3+4+5 = 14; 3+4+5+6 = 18. Each step increases by 4.",
                "icon": "➕"
            },
            {
                "title": "Symmetry & Balance",
                "content": "Numbers equidistant from the centre pair up to equal sums. In 1, 2, 3, 4, 5: 1+5 = 6, 2+4 = 6, middle is 3. Total = 5 × 3 = 15.",
                "icon": "✨"
            }
        ],
        "checkpoints": [
            {
                "question": "What is the sum of 3 consecutive numbers whose middle number is 25?",
                "options": [
                    "75 (3 × 25)",
                    "70",
                    "80",
                    "50"
                ],
                "correct": 0,
                "feedback": "Correct! Sum = 3 × Middle Number = 3 × 25 = 75 (24 + 25 + 26 = 75)."
            },
            {
                "question": "The sum of 3 consecutive numbers is 90. What is the middle number?",
                "options": [
                    "30 (90 / 3)",
                    "29",
                    "31",
                    "28"
                ],
                "correct": 0,
                "feedback": "Spot on! Middle number = 90 / 3 = 30. The numbers are 29, 30, and 31."
            }
        ]
    },
    {
        "id": 7,
        "heading": "Longest Route",
        "tagline": "Adding 4-Digit and 5-Digit Highway Corridor Distances",
        "color": "from-amber-600 to-yellow-600",
        "badge": "Large Number Addition",
        "audio_text": (
            "India is a vast and magnificent land with some of the longest highway networks in the world! "
            "Our textbook highlights the famous North-South Corridor, stretching all the way from Srinagar in Jammu and Kashmir in the north down to Kanyakumari at the southern tip of Tamil Nadu. "
            "This historic route spans approximately 4,000 kilometres! "
            "When adding multi-leg travel journeys with 4-digit and 5-digit numbers, we expand our place value chart to include Thousands and Ten Thousands. "
            "Suppose a fleet vehicle travels 1,284 kilometres in Leg 1, 2,476 kilometres in Leg 2, and 1,850 kilometres in Leg 3. "
            "To find the total distance, align the digits in the Th, H, T, and O columns. "
            "Add Ones: 4 + 6 + 0 = 10 (write 0, carry 1 Ten). "
            "Add Tens: 8 + 7 + 5 + 1 = 21 (write 1, carry 2 Hundreds). "
            "Add Hundreds: 2 + 4 + 8 + 2 = 16 (write 6, carry 1 Thousand). "
            "Add Thousands: 1 + 2 + 1 + 1 = 5 Thousands. "
            "The grand total is 5,610 kilometres! Regrouping across thousands follows the exact same systematic rule."
        ),
        "theory_blocks": [
            {
                "title": "North-South Corridor",
                "content": "Connecting Srinagar (J&K) to Kanyakumari (TN), National Highway 44 (NH 44) spans 4,112 km, forming the backbone of Indian road transport.",
                "icon": "🛣️"
            },
            {
                "title": "Multi-Digit Column Carrying",
                "content": "Carry-overs occur when sum >= 10: 10 Tens = 1 Hundred; 10 Hundreds = 1 Thousand; 10 Thousands = 1 Ten Thousand.",
                "icon": "📈"
            },
            {
                "title": "Route Leg Summation",
                "content": "Total Expedition Distance = Leg 1 + Leg 2 + Leg 3. Always double-check by adding columns in reverse order (bottom to top).",
                "icon": "🗺️"
            }
        ],
        "checkpoints": [
            {
                "question": "What is 3,425 km + 2,780 km?",
                "options": [
                    "6,205 km",
                    "6,105 km",
                    "5,205 km",
                    "6,215 km"
                ],
                "correct": 0,
                "feedback": "Correct! Ones: 5+0=5; Tens: 2+8=10 (carry 1); Hundreds: 4+7+1=12 (carry 1); Thousands: 3+2+1=6. Result = 6,205 km."
            },
            {
                "question": "A truck travels 4,500 km in Week 1 and 3,650 km in Week 2. What is the total distance?",
                "options": [
                    "8,150 km",
                    "7,150 km",
                    "8,250 km",
                    "8,050 km"
                ],
                "correct": 0,
                "feedback": "Spot on! 4,500 + 3,650 = 8,150 km."
            }
        ]
    },
    {
        "id": 8,
        "heading": "Route Distances",
        "tagline": "Subtracting Large Distances Across Sea Ports and Highways",
        "color": "from-blue-600 to-indigo-700",
        "badge": "Large Number Subtraction",
        "audio_text": (
            "Just as we add route legs to calculate total journeys, we subtract large distances to compare different travel options! "
            "Consider India's major maritime shipping ports: Mumbai on the western coast, Cochin in the south, and Chennai on the eastern coast. "
            "Suppose a cargo ship route from Port A to Port B is 3,240 nautical miles, while a modern direct coastal route is 2,165 nautical miles. "
            "How much distance does the direct coastal route save? "
            "We calculate: 3,240 minus 2,165! "
            "Look at the Ones column: 0 minus 5 is not possible, so we borrow 1 Ten from 4 Tens, leaving 3 Tens. The 0 becomes 10 Ones. 10 minus 5 equals 5 Ones. "
            "In Tens: 3 minus 6 is not possible, so borrow 1 Hundred from 2 Hundreds, leaving 1 Hundred. 13 minus 6 equals 7 Tens. "
            "In Hundreds: 1 minus 1 equals 0. "
            "In Thousands: 3 minus 2 equals 1 Thousand. "
            "The direct route saves 1,075 nautical miles! "
            "Borrowing across multiple place value columns follows the exact same logical chain."
        ),
        "theory_blocks": [
            {
                "title": "Coastal Sea Routes",
                "content": "India has a 7,516 km coastline. Comparing nautical distances between Mumbai, Cochin, Chennai, and Kolkata reveals huge fuel savings.",
                "icon": "⚓"
            },
            {
                "title": "Multi-Column Borrowing",
                "content": "When borrowing cascades across zeros (e.g. 5,000 - 2,345), borrow from the nearest non-zero column to the left, turning intermediate zeros into 9s.",
                "icon": "⛓️"
            },
            {
                "title": "Distance Comparison",
                "content": "Difference = Longer Route - Shorter Route. The difference represents saved kilometres, reduced travel hours, and conserved fuel.",
                "icon": "📏"
            }
        ],
        "checkpoints": [
            {
                "question": "What is 5,000 km - 3,240 km?",
                "options": [
                    "1,760 km",
                    "1,860 km",
                    "2,760 km",
                    "1,740 km"
                ],
                "correct": 0,
                "feedback": "Correct! 5,000 - 3,240 = 1,760 km. Check: 1,760 + 3,240 = 5,000 km."
            },
            {
                "question": "Route 1 is 8,450 km and Route 2 is 6,800 km. How much longer is Route 1?",
                "options": [
                    "1,650 km",
                    "1,550 km",
                    "2,650 km",
                    "1,600 km"
                ],
                "correct": 0,
                "feedback": "Spot on! 8,450 - 6,800 = 1,650 km."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Authored Slides 1 to 8. Count: {len(slides_1_to_8)}")

