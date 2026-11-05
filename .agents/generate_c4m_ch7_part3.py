# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 7: The Cleanest Village
Part 3: Slides 17 to 20 (Mastery Challenges 1 to 4)
40 Comprehensive Multiple Choice Questions (10 per challenge)
Zero human names.
Clean Unicode throughout (₹, ×, +, -, =).
"""

def make_sol_html(step1, step2, step3):
    return f"""
    <ol class="space-y-1.5 list-none pl-0">
        <li class="text-xs text-slate-300 leading-relaxed"><span class="font-semibold text-amber-400">Step 1:</span> {step1}</li>
        <li class="text-xs text-slate-300 leading-relaxed"><span class="font-semibold text-amber-400">Step 2:</span> {step2}</li>
        <li class="text-xs text-slate-300 leading-relaxed"><span class="font-semibold text-amber-400">Step 3:</span> {step3}</li>
    </ol>
    """

quiz_slide_17 = [
    {
        "id": 1,
        "q": "A school bus departs for the village at 7:00 AM and arrives at 4:00 PM. How many hours did the journey take?",
        "options": ["7 hours", "8 hours", "9 hours", "10 hours"],
        "ans": 2,
        "hint": "Count from 7:00 AM to 12:00 noon, then add the hours until 4:00 PM.",
        "exp": "7:00 AM to 12:00 noon is 5 hours, and 12:00 noon to 4:00 PM is 4 hours; 5 + 4 = 9 hours.",
        "sol": make_sol_html("From 7:00 AM to 12:00 noon is 5 hours.", "From 12:00 noon to 4:00 PM is 4 additional hours.", "5 + 4 = 9 hours total travel time.")
    },
    {
        "id": 2,
        "q": "The field trip ticket costs ₹500 per child. How much do tickets for 3 children cost in total?",
        "options": ["₹1,000", "₹1,200", "₹1,500", "₹1,800"],
        "ans": 2,
        "hint": "Multiply 3 by 500, or add 500 three times.",
        "exp": "3 × ₹500 = ₹1,500 total cost.",
        "sol": make_sol_html("Identify the single ticket price: ₹500.", "Multiply by 3 tickets: 3 × 500.", "3 × 500 = ₹1,500.")
    },
    {
        "id": 3,
        "q": "If fresh green beans cost ₹95 per kg, what is the cost of 2 kg of green beans?",
        "options": ["₹180", "₹185", "₹190", "₹195"],
        "ans": 2,
        "hint": "Double 95 by adding 95 + 95.",
        "exp": "₹95 + ₹95 = ₹190 (or 2 × 95 = ₹190).",
        "sol": make_sol_html("Identify unit rate: ₹95 per kg.", "Compute for 2 kg: 95 × 2 = (90 × 2) + (5 × 2).", "180 + 10 = ₹190.")
    },
    {
        "id": 4,
        "q": "A shopper buys 1 kg onions at ₹32 and 1 kg potatoes at ₹37. What is the total bill?",
        "options": ["₹67", "₹69", "₹71", "₹79"],
        "ans": 1,
        "hint": "Add the Ones digits (2 + 7) and Tens digits (3 + 3).",
        "exp": "32 + 37 = 69 rupees.",
        "sol": make_sol_html("Identify costs: ₹32 and ₹37.", "Add Ones: 2 + 7 = 9; add Tens: 30 + 30 = 60.", "60 + 9 = ₹69 total.")
    },
    {
        "id": 5,
        "q": "A shopper has a ₹100 note and spends ₹64 at the grocery stall. How much change is returned?",
        "options": ["₹26", "₹34", "₹36", "₹46"],
        "ans": 2,
        "hint": "Subtract 64 from 100, or count up from 64 to 100.",
        "exp": "₹100 - ₹64 = ₹36 change.",
        "sol": make_sol_html("Note amount handed over: ₹100.", "Subtract bill: 100 - 64.", "100 - 60 = 40; 40 - 4 = ₹36.")
    },
    {
        "id": 6,
        "q": "Two oranges cost ₹21 each. What is their combined cost?",
        "options": ["₹32", "₹40", "₹42", "₹44"],
        "ans": 2,
        "hint": "Double 21.",
        "exp": "21 + 21 = 42 rupees.",
        "sol": make_sol_html("Each orange costs ₹21.", "For 2 oranges: 21 × 2.", "21 × 2 = ₹42.")
    },
    {
        "id": 7,
        "q": "If a shopper buys ₹42 worth of oranges and pays with a ₹50 note, what is the change?",
        "options": ["₹6", "₹8", "₹12", "₹18"],
        "ans": 1,
        "hint": "Subtract 42 from 50.",
        "exp": "₹50 - ₹42 = ₹8.",
        "sol": make_sol_html("Cash paid: ₹50.", "Bill amount: ₹42.", "50 - 42 = ₹8 change.")
    },
    {
        "id": 8,
        "q": "If a shopper pays ₹42 using a ₹100 note, how much change is returned?",
        "options": ["₹48", "₹52", "₹58", "₹68"],
        "ans": 2,
        "hint": "Subtract 42 from 100.",
        "exp": "₹100 - ₹42 = ₹58.",
        "sol": make_sol_html("Amount paid: ₹100.", "Subtract 42: 100 - 40 = 60; 60 - 2 = 58.", "Exact balance is ₹58.")
    },
    {
        "id": 9,
        "q": "If a shopper pays ₹42 with a ₹500 note, how much balance is returned?",
        "options": ["₹448", "₹458", "₹468", "₹478"],
        "ans": 1,
        "hint": "Subtract 42 from 500.",
        "exp": "₹500 - ₹42 = ₹458.",
        "sol": make_sol_html("Amount paid: ₹500.", "Subtract 42: 500 - 40 = 460; 460 - 2 = 458.", "Exact balance is ₹458.")
    },
    {
        "id": 10,
        "q": "In a magic triangle using numbers 1 to 6 with side sum 9, what are the three corner vertex numbers?",
        "options": ["4, 5, 6", "1, 2, 3", "2, 4, 6", "1, 3, 5"],
        "ans": 1,
        "hint": "To keep side sums low, place the smallest numbers at the shared corners.",
        "exp": "The three smallest numbers 1, 2, 3 must be at the vertices to achieve side sum 9.",
        "sol": make_sol_html("Corners are shared by two sides and counted twice.", "To minimize side sums to 9, place smallest numbers at corners.", "Corners are 1, 2, and 3.")
    }
]

quiz_slide_18 = [
    {
        "id": 11,
        "q": "When adding 8 Ones and 6 Ones using base-ten blocks, how are the 14 cubes regrouped?",
        "options": ["14 remain in Ones", "1 Ten rod and 4 Ones cubes", "2 Ten rods and 4 Ones cubes", "1 Hundred flat and 4 Ones"],
        "ans": 1,
        "hint": "Every 10 single cubes bundle into 1 Ten rod.",
        "exp": "14 = 10 + 4, which is 1 Ten and 4 Ones.",
        "sol": make_sol_html("14 Ones exceeds 9, requiring regrouping.", "Bundle 10 Ones into 1 Ten rod.", "Leaves 4 Ones; result is 1 Ten and 4 Ones.")
    },
    {
        "id": 12,
        "q": "What is the sum of 24 teachers and 28 teachers?",
        "options": ["42", "50", "52", "62"],
        "ans": 2,
        "hint": "Add Ones: 4 + 8 = 12 (write 2, carry 1).",
        "exp": "24 + 28 = 52.",
        "sol": make_sol_html("Ones column: 4 + 8 = 12 (write 2, carry 1 Ten).", "Tens column: 1 (carried) + 2 + 2 = 5 Tens.", "Total sum is 52 teachers.")
    },
    {
        "id": 13,
        "q": "Adding 438 girls and 476 boys gives what total student attendance?",
        "options": ["814", "904", "914", "924"],
        "ans": 2,
        "hint": "8 + 6 = 14 (carry 1); 1 + 3 + 7 = 11 (carry 1); 1 + 4 + 4 = 9.",
        "exp": "438 + 476 = 914 students.",
        "sol": make_sol_html("Ones: 8 + 6 = 14 (write 4, carry 1 Ten).", "Tens: 1 + 3 + 7 = 11 (write 1, carry 1 Hundred).", "Hundreds: 1 + 4 + 4 = 9 Hundreds -> 914.")
    },
    {
        "id": 14,
        "q": "A traveler orders pusaw cake for ₹38 and spiced tea for ₹16. What is the total snack bill?",
        "options": ["₹48", "₹52", "₹54", "₹56"],
        "ans": 2,
        "hint": "Add 38 and 16 with regrouping in the Ones.",
        "exp": "38 + 16 = 54 rupees.",
        "sol": make_sol_html("Ones: 8 + 6 = 14 (write 4, carry 1 Ten).", "Tens: 1 + 3 + 1 = 5 Tens.", "Total bill is ₹54.")
    },
    {
        "id": 15,
        "q": "Combining savings of ₹185 and ₹125 yields what total sum?",
        "options": ["₹300", "₹310", "₹320", "₹410"],
        "ans": 1,
        "hint": "185 + 125: 5+5=10 (carry 1); 1+8+2=11 (carry 1).",
        "exp": "185 + 125 = 310 rupees.",
        "sol": make_sol_html("Ones: 5 + 5 = 10 (write 0, carry 1 Ten).", "Tens: 1 + 8 + 2 = 11 (write 1, carry 1 Hundred).", "Hundreds: 1 + 1 + 1 = 3 Hundreds -> ₹310.")
    },
    {
        "id": 16,
        "q": "At lunch, 83 children choose pusaw cakes and 46 choose fruit plates. How many more chose pusaw?",
        "options": ["27", "33", "37", "43"],
        "ans": 2,
        "hint": "Subtract 46 from 83 by borrowing 1 Ten.",
        "exp": "83 - 46 = 37.",
        "sol": make_sol_html("Ones: Borrow 1 Ten to make 13; 13 - 6 = 7 Ones.", "Tens: 7 Tens remaining minus 4 Tens = 3 Tens.", "Difference is 37 children.")
    },
    {
        "id": 17,
        "q": "What is 324 - 176?",
        "options": ["138", "148", "158", "248"],
        "ans": 1,
        "hint": "Borrow 1 Ten for Ones (14 - 6 = 8), then borrow 1 Hundred for Tens (11 - 7 = 4).",
        "exp": "324 - 176 = 148.",
        "sol": make_sol_html("Ones: 14 - 6 = 8 (borrowed 1 Ten).", "Tens: 11 - 7 = 4 (borrowed 1 Hundred).", "Hundreds: 2 - 1 = 1 -> Result is 148.")
    },
    {
        "id": 18,
        "q": "A traveler starts with ₹310 and has ₹179 remaining at the end of the day. How much was spent?",
        "options": ["₹121", "₹131", "₹141", "₹231"],
        "ans": 1,
        "hint": "Subtract remaining cash (179) from initial cash (310).",
        "exp": "310 - 179 = 131 rupees spent.",
        "sol": make_sol_html("Initial cash: ₹310; Remaining: ₹179.", "Subtract: 310 - 179.", "10 - 9 = 1; 10 - 7 = 3; 2 - 1 = 1 -> ₹131 spent.")
    },
    {
        "id": 19,
        "q": "An orchard produced 520 kg mangoes last year and 415 kg this year. What is the decrease?",
        "options": ["95 kg", "105 kg", "115 kg", "205 kg"],
        "ans": 1,
        "hint": "Subtract 415 from 520.",
        "exp": "520 - 415 = 105 kg decrease.",
        "sol": make_sol_html("Last year: 520 kg; This year: 415 kg.", "Subtract 415 from 520.", "10 - 5 = 5; 1 - 1 = 0; 5 - 4 = 1 -> 105 kg.")
    },
    {
        "id": 20,
        "q": "A train starts with 642 passengers; 85 alight and 114 board at a junction. How many passengers are on board?",
        "options": ["661", "671", "681", "691"],
        "ans": 1,
        "hint": "642 - 85 + 114.",
        "exp": "642 - 85 = 557; 557 + 114 = 671.",
        "sol": make_sol_html("Subtract alighting passengers: 642 - 85 = 557.", "Add boarding passengers: 557 + 114.", "557 + 114 = 671 passengers.")
    }
]

quiz_slide_19 = [
    {
        "id": 21,
        "q": "From 671 passengers on a train, 96 alight and 62 board. What is the updated passenger count?",
        "options": ["627", "635", "637", "647"],
        "ans": 2,
        "hint": "671 - 96 + 62.",
        "exp": "671 - 96 = 575; 575 + 62 = 637.",
        "sol": make_sol_html("Subtract departing passengers: 671 - 96 = 575.", "Add new passengers: 575 + 62.", "575 + 62 = 637 passengers.")
    },
    {
        "id": 22,
        "q": "What mental math strategy quickly adds 99 to 356?",
        "options": ["Add 100, then add 1", "Add 100, then subtract 1", "Add 90, then add 9", "Subtract 100, then add 1"],
        "ans": 1,
        "hint": "99 is 1 less than 100.",
        "exp": "356 + 100 = 456; 456 - 1 = 455.",
        "sol": make_sol_html("Round 99 to nearest hundred: 100.", "Add 100 to 356: 356 + 100 = 456.", "Compensate by subtracting 1: 456 - 1 = 455.")
    },
    {
        "id": 23,
        "q": "Using mental compensation, what is 280 - 49?",
        "options": ["229", "230", "231", "241"],
        "ans": 2,
        "hint": "Subtract 50 (gives 230), then add 1 back because 49 is 1 less than 50.",
        "exp": "280 - 50 = 230; 230 + 1 = 231.",
        "sol": make_sol_html("Round 49 up to 50.", "Subtract 50: 280 - 50 = 230.", "Add 1 back: 230 + 1 = 231.")
    },
    {
        "id": 24,
        "q": "Which pair of numbers produces the target sum of 856?",
        "options": ["500 + 356", "600 + 246", "700 + 166", "800 + 46"],
        "ans": 0,
        "hint": "500 + 300 = 800; add 56 = 856.",
        "exp": "500 + 356 = 856.",
        "sol": make_sol_html("Check options: 500 + 356.", "500 + 300 = 800; 800 + 56 = 856.", "Matches target sum exactly.")
    },
    {
        "id": 25,
        "q": "Which subtraction expression equals the target difference of 563?",
        "options": ["763 - 100", "763 - 200", "863 - 200", "663 - 200"],
        "ans": 1,
        "hint": "763 - 200.",
        "exp": "763 - 200 = 563.",
        "sol": make_sol_html("Look for a subtrahend of hundreds: 763 - 200.", "7 Hundreds - 2 Hundreds = 5 Hundreds.", "Result is 563.")
    },
    {
        "id": 26,
        "q": "In a number grid, neighboring cells contain 87 and 94. What is their sum?",
        "options": ["171", "181", "191", "201"],
        "ans": 1,
        "hint": "87 + 94: 7 + 4 = 11; 80 + 90 = 170.",
        "exp": "170 + 11 = 181.",
        "sol": make_sol_html("Ones: 7 + 4 = 11.", "Tens: 80 + 90 = 170.", "170 + 11 = 181.")
    },
    {
        "id": 27,
        "q": "Two adjacent grid cells hold 55 and 52. What is their difference?",
        "options": ["2", "3", "7", "107"],
        "ans": 1,
        "hint": "Subtract 52 from 55.",
        "exp": "55 - 52 = 3.",
        "sol": make_sol_html("Larger value: 55; Smaller value: 52.", "Subtract: 55 - 52.", "Difference is 3.")
    },
    {
        "id": 28,
        "q": "If 1 kg yams costs ₹45 and 1 kg bananas costs ₹55, what is their combined cost?",
        "options": ["₹90", "₹95", "₹100", "₹105"],
        "ans": 2,
        "hint": "45 + 55.",
        "exp": "45 + 55 = 100 rupees.",
        "sol": make_sol_html("Costs: ₹45 and ₹55.", "Ones: 5 + 5 = 10; Tens: 40 + 50 = 90.", "90 + 10 = ₹100.")
    },
    {
        "id": 29,
        "q": "What is the cost of 3 kg radishes at ₹23 per kg?",
        "options": ["₹59", "₹66", "₹69", "₹72"],
        "ans": 2,
        "hint": "3 × 23 = (3 × 20) + (3 × 3).",
        "exp": "60 + 9 = 69 rupees.",
        "sol": make_sol_html("Unit price: ₹23.", "Multiply by 3: 3 × 20 = 60, and 3 × 3 = 9.", "60 + 9 = ₹69.")
    },
    {
        "id": 30,
        "q": "In a magic triangle with numbers 1 to 6 and side sum 12, which numbers must occupy the three corner vertices?",
        "options": ["1, 2, 3", "4, 5, 6", "2, 3, 4", "1, 3, 5"],
        "ans": 1,
        "hint": "To maximize side sums to 12, place the largest numbers at the shared corners.",
        "exp": "Placing the largest numbers 4, 5, 6 at the corners allows each side to reach sum 12.",
        "sol": make_sol_html("Corners are counted twice across two intersecting sides.", "To achieve the maximum possible side sum (12), place 4, 5, 6 at corners.", "Corners are 4, 5, and 6.")
    }
]

quiz_slide_20 = [
    {
        "id": 31,
        "q": "What is 456 + 199 using the near-hundreds shortcut?",
        "options": ["645", "654", "655", "656"],
        "ans": 2,
        "hint": "Add 200 (gives 656), then subtract 1.",
        "exp": "456 + 200 = 656; 656 - 1 = 655.",
        "sol": make_sol_html("199 = 200 - 1.", "Add 200: 456 + 200 = 656.", "Compensate: 656 - 1 = 655.")
    },
    {
        "id": 32,
        "q": "What is 500 - 148?",
        "options": ["342", "352", "362", "452"],
        "ans": 1,
        "hint": "Subtract 100 (400), subtract 40 (360), subtract 8 (352).",
        "exp": "500 - 148 = 352.",
        "sol": make_sol_html("500 - 100 = 400.", "400 - 40 = 360.", "360 - 8 = 352.")
    },
    {
        "id": 33,
        "q": "A book has 248 pages. A reader finishes 165 pages. How many pages remain?",
        "options": ["73", "83", "93", "103"],
        "ans": 1,
        "hint": "248 - 165.",
        "exp": "248 - 165 = 83 pages.",
        "sol": make_sol_html("Total pages: 248; Pages read: 165.", "Subtract: 248 - 165.", "8 - 5 = 3; 14 - 6 = 8; 1 - 1 = 0 -> 83 pages remaining.")
    },
    {
        "id": 34,
        "q": "Fill in the missing digit: 3 _ 5 + 142 = 497. What digit belongs in the Tens place?",
        "options": ["3", "4", "5", "6"],
        "ans": 2,
        "hint": "What plus 4 equals 9?",
        "exp": "5 + 4 = 9, so the missing digit is 5 (355 + 142 = 497).",
        "sol": make_sol_html("Examine the Tens column: _ + 4 = 9.", "Subtract 4 from 9: 9 - 4 = 5.", "Missing digit is 5.")
    },
    {
        "id": 35,
        "q": "Fill in the missing digit: 684 - 2 _ 1 = 433. What digit belongs in the Tens place?",
        "options": ["3", "4", "5", "6"],
        "ans": 2,
        "hint": "8 minus what equals 3?",
        "exp": "8 - 5 = 3, so the missing digit is 5 (684 - 251 = 433).",
        "sol": make_sol_html("Look at Tens column: 8 - _ = 3.", "8 - 3 = 5.", "Missing digit is 5.")
    },
    {
        "id": 36,
        "q": "Which property states that (a + b) + c = a + (b + c)?",
        "options": ["Commutative property", "Associative property", "Identity property", "Subtraction property"],
        "ans": 1,
        "hint": "Grouping numbers differently does not change their sum.",
        "exp": "The associative property states that grouping addends differently yields the same sum.",
        "sol": make_sol_html("Notice how brackets group numbers.", "Grouping property is the Associative Property of Addition.", "Total sum remains invariant.")
    },
    {
        "id": 37,
        "q": "If 150 + 250 = 400, what is 400 - 250?",
        "options": ["100", "150", "200", "250"],
        "ans": 1,
        "hint": "Addition and subtraction are inverse operations.",
        "exp": "Because 150 + 250 = 400, subtracting 250 leaves 150.",
        "sol": make_sol_html("Recognize inverse relationship between addition and subtraction.", "If Part 1 + Part 2 = Whole, then Whole - Part 2 = Part 1.", "400 - 250 = 150.")
    },
    {
        "id": 38,
        "q": "A school library receives 315 new storybooks and 185 puzzle books. How many total books arrived?",
        "options": ["490", "500", "510", "600"],
        "ans": 1,
        "hint": "315 + 185: 15 + 85 = 100; 300 + 100 + 100 = 500.",
        "exp": "315 + 185 = 500 books.",
        "sol": make_sol_html("Ones: 5 + 5 = 10 (carry 1).", "Tens: 1 + 1 + 8 = 10 (carry 1).", "Hundreds: 1 + 3 + 1 = 5 Hundreds -> 500 books.")
    },
    {
        "id": 39,
        "q": "A traveler spends ₹72 on lunch and ₹28 on fruit juice. How much was spent in total?",
        "options": ["₹90", "₹98", "₹100", "₹110"],
        "ans": 2,
        "hint": "72 + 28.",
        "exp": "72 + 28 = 100 rupees.",
        "sol": make_sol_html("Ones: 2 + 8 = 10.", "Tens: 70 + 20 = 90.", "90 + 10 = ₹100 total.")
    },
    {
        "id": 40,
        "q": "In a magic triangle with numbers 1 to 6 and side sum 10, what is the sum of the three vertex numbers?",
        "options": ["6", "9", "12", "15"],
        "ans": 1,
        "hint": "3 × 10 = 30. The numbers 1 to 6 sum to 21. 30 - 21 = 9.",
        "exp": "The three sides total 30. Since vertices are counted twice, vertex sum = 30 - 21 = 9 (e.g. vertices 1, 3, 5).",
        "sol": make_sol_html("Sum of three sides: 3 × 10 = 30.", "Sum of all numbers 1 to 6: 1+2+3+4+5+6 = 21.", "Vertices are counted twice, so sum of vertices = 30 - 21 = 9.")
    }
]

slides_part3 = [
    {
        "id": 17,
        "title": "Challenge 1",
        "section": "Mastery Assessment: Questions 1 to 10",
        "quiz": quiz_slide_17
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "section": "Mastery Assessment: Questions 11 to 20",
        "quiz": quiz_slide_18
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "section": "Mastery Assessment: Questions 21 to 30",
        "quiz": quiz_slide_19
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "section": "Mastery Assessment: Questions 31 to 40",
        "quiz": quiz_slide_20
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(slides_part3)} slides for Part 3.")
    for s in slides_part3:
        print(f"Slide {s['id']}: {s['title']} -> {len(s['quiz'])} questions (Title: {len(s['title'].split())} words)")
        assert len(s['quiz']) == 10
        assert 1 <= len(s['title'].split()) <= 3

