# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 8: Weigh It, Pour It
Part 3: Slides 17 to 20 Data Generator (40 Quiz Questions)
Short headings: Challenge 1, Challenge 2, Challenge 3, Challenge 4.
Zero human names (Shrinathan, Mirabai, Raghav, etc. replaced with generic roles).
Clean Unicode throughout (kg, g, L, ml, ₹, ×, +, -, =).
"""

def make_sol_html(steps, note=None):
    items = "".join(f"<li class='mb-2 text-slate-700 leading-relaxed'>{s}</li>" for s in steps)
    html = f"<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside space-y-1.5 text-sm'>{items}</ol></div>"
    if note:
        html += f"<div class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> {note}</div>"
    html += "</div>"
    return html

slides_part3 = [
    {
        "id": 17,
        "title": "Challenge 1",
        "section": "Mass Foundations & Scale Balancing",
        "speech": "",
        "quizzes": [
            {
                "q": "How many grams are there in 1 kilogram?",
                "options": ["100 g", "500 g", "1000 g", "10,000 g"],
                "ans": 2,
                "hint": "Recall the metric definition: kilo means one thousand.",
                "exp": "1 kilogram (kg) equals exactly 1000 grams (g).",
                "sol": make_sol_html([
                    "The prefix 'kilo' comes from the Greek word for thousand.",
                    "Therefore, 1 kilogram = 1000 grams.",
                    "This metric identity applies universally across science and commerce."
                ], "Always remember: 1 kg = 1000 g.")
            },
            {
                "q": "What is the weight in grams of half a kilogram (1/2 kg)?",
                "options": ["250 g", "500 g", "750 g", "100 g"],
                "ans": 1,
                "hint": "Divide 1000 grams into 2 equal parts.",
                "exp": "1000 g ÷ 2 = 500 g, so half a kilogram is 500 g.",
                "sol": make_sol_html([
                    "1 full kilogram = 1000 g.",
                    "Half of 1 kilogram = 1000 g ÷ 2 = 500 g.",
                    "Two 500 g weights together balance 1 kg."
                ], "1/2 kg = 500 g.")
            },
            {
                "q": "What is the weight in grams of one-quarter of a kilogram (1/4 kg)?",
                "options": ["200 g", "250 g", "300 g", "400 g"],
                "ans": 1,
                "hint": "Divide 1000 grams by 4.",
                "exp": "1000 g ÷ 4 = 250 g, so one-quarter kilogram is 250 g.",
                "sol": make_sol_html([
                    "1 full kilogram = 1000 g.",
                    "One-quarter of a kilogram = 1000 g ÷ 4 = 250 g.",
                    "Four 250 g packets equal 1 kg."
                ], "1/4 kg = 250 g.")
            },
            {
                "q": "If half a pumpkin balances two 500 g weights, what is the weight of the entire pumpkin?",
                "options": ["1 kg", "1.5 kg", "2 kg", "4 kg"],
                "ans": 2,
                "hint": "Find the weight of one half first, then multiply by 2.",
                "exp": "Half a pumpkin = 500 g + 500 g = 1000 g = 1 kg. Whole pumpkin = 1 kg × 2 = 2 kg.",
                "sol": make_sol_html([
                    "Weight of half pumpkin = 500 g + 500 g = 1000 g.",
                    "1000 g = 1 kg.",
                    "Since half is 1 kg, the whole pumpkin = 1 kg × 2 = 2 kg."
                ], "Half = 1 kg, therefore whole = 2 kg.")
            },
            {
                "q": "How many 250 g packets of tea are needed to balance a 1 kg counterweight on a beam scale?",
                "options": ["2 packets", "3 packets", "4 packets", "5 packets"],
                "ans": 2,
                "hint": "Divide 1000 g by 250 g.",
                "exp": "1000 g ÷ 250 g = 4 packets.",
                "sol": make_sol_html([
                    "Target weight = 1 kg = 1000 g.",
                    "Each tea packet = 250 g.",
                    "Number of packets needed = 1000 ÷ 250 = 4 packets."
                ], "4 × 250 g = 1000 g = 1 kg.")
            },
            {
                "q": "A customer buys three 250 g packets of butter. What is the total mass in grams?",
                "options": ["500 g", "650 g", "750 g", "1000 g"],
                "ans": 2,
                "hint": "Multiply 250 g by 3.",
                "exp": "3 × 250 g = 750 g (or 3/4 kg).",
                "sol": make_sol_html([
                    "Each packet = 250 g.",
                    "Three packets = 250 g + 250 g + 250 g = 750 g.",
                    "750 g is also known as three-quarters of a kilogram (3/4 kg)."
                ], "3 × 250 g = 750 g = 3/4 kg.")
            },
            {
                "q": "On a two-pan beam balance, the left pan holds 800 g of apples and the right pan holds 1 kg of weights. Which pan tilts downward?",
                "options": ["The left pan (apples)", "The right pan (weights)", "Neither, they stay level", "Both tilt up"],
                "ans": 1,
                "hint": "Compare 800 g with 1 kg (1000 g). Heavier side tilts down.",
                "exp": "1 kg = 1000 g, which is heavier than 800 g. Gravity pulls the heavier right pan downward.",
                "sol": make_sol_html([
                    "Left pan weight = 800 g.",
                    "Right pan weight = 1 kg = 1000 g.",
                    "Since 1000 g > 800 g, the right pan is heavier.",
                    "The heavier pan tilts downward due to gravitational pull."
                ], "Heavier side always tilts downward on a beam scale.")
            },
            {
                "q": "How many grams must be added to 650 g to make a full 1 kilogram?",
                "options": ["250 g", "350 g", "450 g", "550 g"],
                "ans": 1,
                "hint": "Subtract 650 g from 1000 g.",
                "exp": "1000 g - 650 g = 350 g.",
                "sol": make_sol_html([
                    "Target weight = 1 kg = 1000 g.",
                    "Current weight = 650 g.",
                    "Additional weight required = 1000 g - 650 g = 350 g."
                ], "650 g + 350 g = 1000 g = 1 kg.")
            },
            {
                "q": "Which of the following equals three-quarters of a kilogram?",
                "options": ["500 g", "700 g", "750 g", "850 g"],
                "ans": 2,
                "hint": "Calculate 3/4 of 1000 grams.",
                "exp": "(3/4) × 1000 g = 750 g.",
                "sol": make_sol_html([
                    "1/4 kg = 250 g.",
                    "3/4 kg = 3 × 250 g = 750 g."
                ], "3/4 kg = 750 g.")
            },
            {
                "q": "A vendor balances a 1 kg pumpkin using one 500 g weight and two identical small packets. What does each small packet weigh?",
                "options": ["150 g", "200 g", "250 g", "300 g"],
                "ans": 2,
                "hint": "Subtract 500 g from 1000 g, then divide by 2.",
                "exp": "1000 g - 500 g = 500 g. 500 g ÷ 2 = 250 g for each small packet.",
                "sol": make_sol_html([
                    "Total weight = 1 kg = 1000 g.",
                    "Remaining weight for two packets = 1000 g - 500 g = 500 g.",
                    "Weight of each small packet = 500 g ÷ 2 = 250 g."
                ], "Each small packet weighs 250 g.")
            }
        ]
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "section": "Packaging, Scales & Heavy Multiples",
        "speech": "",
        "quizzes": [
            {
                "q": "How many 100 g gift boxes can be packed from 1 kilogram of cashew sweets?",
                "options": ["5 boxes", "8 boxes", "10 boxes", "12 boxes"],
                "ans": 2,
                "hint": "Divide 1000 g by 100 g.",
                "exp": "1000 g ÷ 100 g = 10 boxes.",
                "sol": make_sol_html([
                    "Total mass = 1 kg = 1000 g.",
                    "Box capacity = 100 g.",
                    "Number of boxes = 1000 ÷ 100 = 10 boxes."
                ], "10 boxes of 100 g each equal 1 kg.")
            },
            {
                "q": "If 2 identical erasers balance a 10 g packet of turmeric, how many erasers are needed to balance a 30 g spice jar?",
                "options": ["4 erasers", "5 erasers", "6 erasers", "8 erasers"],
                "ans": 2,
                "hint": "Find weight of 1 eraser first (10 ÷ 2 = 5 g), then divide 30 g by 5 g.",
                "exp": "1 eraser = 10 g ÷ 2 = 5 g. For 30 g: 30 g ÷ 5 g = 6 erasers.",
                "sol": make_sol_html([
                    "Step 1: Weight of one eraser = 10 g ÷ 2 = 5 g.",
                    "Step 2: Number of erasers for 30 g = 30 g ÷ 5 g = 6 erasers."
                ], "6 erasers × 5 g = 30 g.")
            },
            {
                "q": "Which type of scale is commonly suspended and uses an internal coiled spring to weigh gas cylinders?",
                "options": ["Two-pan beam scale", "Spring balance", "Digital micro scale", "Graduated cylinder"],
                "ans": 1,
                "hint": "Think of the scale with a hanging hook and a stretching spring.",
                "exp": "A spring balance measures suspended loads using the extension of an internal spring.",
                "sol": make_sol_html([
                    "Spring balances operate on Hooke's elastic principle.",
                    "As weight pulls on the lower hook, the internal coiled spring extends proportionally.",
                    "The pointer indicates the weight on a vertical calibrated scale."
                ], "Spring balance is ideal for hanging loads like gas cylinders.")
            },
            {
                "q": "A family consumes 15 kg of wheat flour, 10 kg of rice, and 5 kg of lentils in a month. What is the total mass of grains consumed?",
                "options": ["25 kg", "28 kg", "30 kg", "35 kg"],
                "ans": 2,
                "hint": "Add all three quantities together.",
                "exp": "15 kg + 10 kg + 5 kg = 30 kg.",
                "sol": make_sol_html([
                    "Flour = 15 kg.",
                    "Rice = 10 kg.",
                    "Lentils = 5 kg.",
                    "Total = 15 + 10 + 5 = 30 kg."
                ], "Total monthly grain mass = 30 kg.")
            },
            {
                "q": "How many 1 kg packets are equivalent to two 25-kilogram sacks of basmati rice?",
                "options": ["25 packets", "40 packets", "50 packets", "75 packets"],
                "ans": 2,
                "hint": "Multiply 25 kg by 2.",
                "exp": "2 × 25 kg = 50 kg = 50 packets of 1 kg each.",
                "sol": make_sol_html([
                    "Weight of 1 sack = 25 kg.",
                    "Weight of 2 sacks = 25 kg × 2 = 50 kg.",
                    "Each packet is 1 kg, so 50 packets are needed."
                ], "2 × 25 kg = 50 kg = 50 packets.")
            },
            {
                "q": "An empty domestic LPG cooking gas cylinder weighs about 14 kg. When filled with 14 kg of gas, what is its total weight?",
                "options": ["14 kg", "24 kg", "28 kg", "32 kg"],
                "ans": 2,
                "hint": "Add the empty metal weight to the gas weight.",
                "exp": "14 kg + 14 kg = 28 kg.",
                "sol": make_sol_html([
                    "Tare weight (empty cylinder) = 14 kg.",
                    "Net gas contents = 14 kg.",
                    "Gross total weight = 14 kg + 14 kg = 28 kg."
                ], "Gross weight = tare + net = 28 kg.")
            },
            {
                "q": "At the Tokyo Olympics, a weightlifter weighing 49 kg lifted a total of 202 kg. What is 202 rounded to the nearest ten?",
                "options": ["190 kg", "200 kg", "205 kg", "210 kg"],
                "ans": 1,
                "hint": "Check the ones digit of 202 (it is 2, less than 5).",
                "exp": "The ones digit is 2, so 202 rounds down to 200 kg.",
                "sol": make_sol_html([
                    "Number to round: 202.",
                    "The ones digit is 2, which is less than 5.",
                    "Therefore, round down to 200."
                ], "202 rounds to 200.")
            },
            {
                "q": "If 4 bags of cement weigh 200 kg altogether, how much does one bag of cement weigh?",
                "options": ["40 kg", "45 kg", "50 kg", "60 kg"],
                "ans": 2,
                "hint": "Divide 200 kg by 4.",
                "exp": "200 kg ÷ 4 = 50 kg per bag.",
                "sol": make_sol_html([
                    "Total mass = 200 kg.",
                    "Number of bags = 4.",
                    "Weight per bag = 200 kg ÷ 4 = 50 kg."
                ], "Standard industrial cement bags weigh 50 kg.")
            },
            {
                "q": "A confectionery vendor needs to pack 1 kg of sweets into miniature 50 g sample pouches. How many pouches are required?",
                "options": ["10 pouches", "15 pouches", "20 pouches", "25 pouches"],
                "ans": 2,
                "hint": "Divide 1000 g by 50 g.",
                "exp": "1000 g ÷ 50 g = 20 pouches.",
                "sol": make_sol_html([
                    "Total weight = 1 kg = 1000 g.",
                    "Each pouch = 50 g.",
                    "Number of pouches = 1000 ÷ 50 = 20 pouches."
                ], "1000 g ÷ 50 g = 20 pouches.")
            },
            {
                "q": "Which of the following items is most realistically measured in grams rather than kilograms?",
                "options": ["A bag of wheat", "A school desk", "A gold wedding ring", "A bicycle"],
                "ans": 2,
                "hint": "Which item is very light and small?",
                "exp": "A gold ring is very light (usually 3 to 10 grams) and is measured in grams.",
                "sol": make_sol_html([
                    "Heavy items like bags of wheat, desks, and bicycles are measured in kilograms.",
                    "Very small, precious items like gold jewelry weigh just a few grams.",
                    "Therefore, a gold wedding ring is measured in grams."
                ], "Light items are measured in grams.")
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "section": "Liquid Capacity & Fractional Litres",
        "speech": "",
        "quizzes": [
            {
                "q": "How many millilitres (ml) are in 1 standard litre (L)?",
                "options": ["10 ml", "100 ml", "1000 ml", "10,000 ml"],
                "ans": 2,
                "hint": "The prefix 'milli' means one-thousandth of a unit.",
                "exp": "1 L = 1000 ml.",
                "sol": make_sol_html([
                    "Capacity measures liquid volume.",
                    "1 litre = 1000 millilitres.",
                    "This is the core metric identity for liquids."
                ], "1 L = 1000 ml.")
            },
            {
                "q": "How many millilitres equal half a litre (1/2 L)?",
                "options": ["200 ml", "250 ml", "500 ml", "750 ml"],
                "ans": 2,
                "hint": "Divide 1000 ml by 2.",
                "exp": "1000 ml ÷ 2 = 500 ml.",
                "sol": make_sol_html([
                    "1 L = 1000 ml.",
                    "1/2 L = 1000 ml ÷ 2 = 500 ml."
                ], "1/2 L = 500 ml.")
            },
            {
                "q": "How many millilitres equal one-quarter of a litre (1/4 L)?",
                "options": ["150 ml", "200 ml", "250 ml", "300 ml"],
                "ans": 2,
                "hint": "Divide 1000 ml by 4.",
                "exp": "1000 ml ÷ 4 = 250 ml.",
                "sol": make_sol_html([
                    "1 L = 1000 ml.",
                    "1/4 L = 1000 ml ÷ 4 = 250 ml."
                ], "1/4 L = 250 ml.")
            },
            {
                "q": "How many 250 ml juice tetra packs are needed to make 1 litre?",
                "options": ["2 packs", "3 packs", "4 packs", "5 packs"],
                "ans": 2,
                "hint": "Divide 1000 ml by 250 ml.",
                "exp": "1000 ml ÷ 250 ml = 4 packs.",
                "sol": make_sol_html([
                    "1 litre = 1000 ml.",
                    "Each pack = 250 ml.",
                    "Number of packs = 1000 ÷ 250 = 4 packs."
                ], "4 × 250 ml = 1000 ml = 1 L.")
            },
            {
                "q": "A bottle contains 750 ml of fruit juice. What fraction of a litre is this?",
                "options": ["1/4 L", "1/2 L", "3/4 L", "1 L"],
                "ans": 2,
                "hint": "750 ml = 3 × 250 ml.",
                "exp": "750 ml ÷ 1000 ml = 3/4 L.",
                "sol": make_sol_html([
                    "1/4 L = 250 ml.",
                    "3 × 250 ml = 750 ml.",
                    "Therefore, 750 ml is three-quarters of a litre (3/4 L)."
                ], "750 ml = 3/4 L.")
            },
            {
                "q": "An artisan perfumer has 1 litre of rose oil. How many 100 ml vials can be filled from it?",
                "options": ["5 vials", "8 vials", "10 vials", "12 vials"],
                "ans": 2,
                "hint": "Convert 1 L to 1000 ml, then divide by 100 ml.",
                "exp": "1000 ml ÷ 100 ml = 10 vials.",
                "sol": make_sol_html([
                    "1 L = 1000 ml.",
                    "Capacity per vial = 100 ml.",
                    "Number of vials = 1000 ÷ 100 = 10 vials."
                ], "1000 ml ÷ 100 ml = 10 vials.")
            },
            {
                "q": "If 50 ml travel bottles are filled from 1 litre of hair oil, how many bottles are produced?",
                "options": ["10 bottles", "15 bottles", "20 bottles", "25 bottles"],
                "ans": 2,
                "hint": "Divide 1000 ml by 50 ml.",
                "exp": "1000 ml ÷ 50 ml = 20 bottles.",
                "sol": make_sol_html([
                    "1 L = 1000 ml.",
                    "Volume per bottle = 50 ml.",
                    "Total bottles = 1000 ÷ 50 = 20 bottles."
                ], "1000 ml ÷ 50 ml = 20 bottles.")
            },
            {
                "q": "A doctor prescribes 5 ml of medicine syrup three times a day. How much syrup is taken in one day?",
                "options": ["10 ml", "15 ml", "20 ml", "25 ml"],
                "ans": 1,
                "hint": "Multiply 5 ml by 3.",
                "exp": "5 ml × 3 = 15 ml per day.",
                "sol": make_sol_html([
                    "Dose per intake = 5 ml.",
                    "Number of intakes per day = 3.",
                    "Daily total = 5 ml × 3 = 15 ml."
                ], "Daily dose = 15 ml.")
            },
            {
                "q": "If a full bottle of medicine syrup contains 150 ml, how many days will a 15 ml daily dose last?",
                "options": ["8 days", "10 days", "12 days", "15 days"],
                "ans": 1,
                "hint": "Divide 150 ml by 15 ml.",
                "exp": "150 ml ÷ 15 ml/day = 10 days.",
                "sol": make_sol_html([
                    "Total bottle volume = 150 ml.",
                    "Daily consumption = 15 ml.",
                    "Number of days = 150 ÷ 15 = 10 days."
                ], "The bottle will last exactly 10 days.")
            },
            {
                "q": "Which tool is best suited to measure 2 ml of liquid medicine for an infant?",
                "options": ["A large water bucket", "A 1-litre milk can", "A graduated medical dropper", "A kitchen mixing bowl"],
                "ans": 2,
                "hint": "Which tool measures tiny amounts accurately?",
                "exp": "A medical dropper is designed to dispense and measure small volumes like 1 to 2 ml.",
                "sol": make_sol_html([
                    "Infant medicine doses are tiny (1 to 2 ml).",
                    "Buckets, bowls, and large cans lack fine markings.",
                    "A calibrated eyedropper or syringe provides precise millilitre markings."
                ], "Use a calibrated dropper for miniature liquid doses.")
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "section": "Dairy Scoops, Tap Leakage & Conservation",
        "speech": "",
        "quizzes": [
            {
                "q": "A milk vendor uses one 500 ml can and one 200 ml can to serve a customer. What is the total volume poured?",
                "options": ["600 ml", "700 ml", "750 ml", "800 ml"],
                "ans": 1,
                "hint": "Add 500 ml and 200 ml.",
                "exp": "500 ml + 200 ml = 700 ml.",
                "sol": make_sol_html([
                    "First scoop = 500 ml.",
                    "Second scoop = 200 ml.",
                    "Total = 500 + 200 = 700 ml."
                ], "Total milk poured = 700 ml.")
            },
            {
                "q": "Which combination of standard cans pours exactly 850 ml of milk?",
                "options": ["500 ml + 200 ml + 100 ml + 50 ml", "500 ml + 250 ml + 50 ml", "500 ml + 200 ml + 200 ml", "500 ml + 300 ml + 50 ml"],
                "ans": 0,
                "hint": "Check which option sums to 850 ml using valid standard dairy cans (50, 100, 200, 500).",
                "exp": "500 ml + 200 ml + 100 ml + 50 ml = 850 ml.",
                "sol": make_sol_html([
                    "Standard dairy cans are: 50 ml, 100 ml, 200 ml, 500 ml, 1000 ml.",
                    "500 + 200 + 100 + 50 = 850 ml.",
                    "All used can sizes are standard."
                ], "500 + 200 + 100 + 50 = 850 ml.")
            },
            {
                "q": "If a leaking tap drips 1 litre of water every hour, how many litres of water are wasted in one full day (24 hours)?",
                "options": ["12 L", "24 L", "48 L", "60 L"],
                "ans": 1,
                "hint": "Multiply 1 L by 24 hours.",
                "exp": "1 L/hour × 24 hours = 24 L.",
                "sol": make_sol_html([
                    "Hourly loss = 1 litre.",
                    "Hours in a day = 24.",
                    "Daily loss = 1 L × 24 = 24 litres."
                ], "24 litres wasted per day.")
            },
            {
                "q": "How many litres of water are wasted by that same dripping tap in a week (7 days)?",
                "options": ["140 L", "154 L", "168 L", "175 L"],
                "ans": 2,
                "hint": "Multiply 24 L/day by 7 days.",
                "exp": "24 L × 7 = 168 L.",
                "sol": make_sol_html([
                    "Daily loss = 24 litres.",
                    "Days in a week = 7.",
                    "Weekly loss = 24 × 7 = 168 litres."
                ], "24 × 7 = 168 litres per week.")
            },
            {
                "q": "In a 30-day month, how much water does the leaking tap squander?",
                "options": ["600 L", "680 L", "720 L", "750 L"],
                "ans": 2,
                "hint": "Multiply 24 L/day by 30 days.",
                "exp": "24 L × 30 = 720 L.",
                "sol": make_sol_html([
                    "Daily loss = 24 litres.",
                    "Days in month = 30.",
                    "Monthly loss = 24 × 30 = 720 litres."
                ], "24 × 30 = 720 litres per month.")
            },
            {
                "q": "Leaving a tap running while brushing teeth wastes about 10 litres. Using a tumbler uses only 0.5 litre (500 ml). How much water is saved per brushing?",
                "options": ["5 L", "8.5 L", "9.5 L", "10.5 L"],
                "ans": 2,
                "hint": "Subtract 0.5 L from 10 L.",
                "exp": "10 L - 0.5 L = 9.5 L.",
                "sol": make_sol_html([
                    "Running tap usage = 10 L.",
                    "Tumbler usage = 0.5 L (500 ml).",
                    "Water saved = 10 - 0.5 = 9.5 litres."
                ], "9.5 litres saved per brushing session.")
            },
            {
                "q": "If one child saves 19 litres of water per day by turning off the tap while brushing, how much water do 100 children save daily?",
                "options": ["190 L", "1900 L", "9500 L", "19,000 L"],
                "ans": 1,
                "hint": "Multiply 19 L by 100.",
                "exp": "19 L × 100 = 1900 L.",
                "sol": make_sol_html([
                    "Savings per child = 19 litres per day.",
                    "Total children = 100.",
                    "Total savings = 19 × 100 = 1900 litres daily."
                ], "Collective conservation: 1900 L saved each day.")
            },
            {
                "q": "A school installs a 5000-litre rainwater harvesting tank. If the school garden uses 250 litres per day, how many days will the water last?",
                "options": ["15 days", "20 days", "25 days", "30 days"],
                "ans": 1,
                "hint": "Divide 5000 L by 250 L.",
                "exp": "5000 L ÷ 250 L/day = 20 days.",
                "sol": make_sol_html([
                    "Total tank capacity = 5000 litres.",
                    "Daily consumption = 250 litres.",
                    "Number of days = 5000 ÷ 250 = 20 days."
                ], "The tank will provide water for 20 days.")
            },
            {
                "q": "A family uses 120 L for bathing, 30 L for cooking, and 50 L for washing clothes daily. What is their total daily water consumption for these activities?",
                "options": ["180 L", "200 L", "220 L", "250 L"],
                "ans": 1,
                "hint": "Sum 120 + 30 + 50.",
                "exp": "120 L + 30 L + 50 L = 200 L.",
                "sol": make_sol_html([
                    "Bathing = 120 L.",
                    "Cooking = 30 L.",
                    "Washing clothes = 50 L.",
                    "Total = 120 + 30 + 50 = 200 litres."
                ], "Total daily consumption = 200 litres.")
            },
            {
                "q": "Which of the following is equivalent to 1 litre and 450 millilitres?",
                "options": ["145 ml", "1045 ml", "1450 ml", "14,500 ml"],
                "ans": 2,
                "hint": "1 L = 1000 ml. Add 450 ml to 1000 ml.",
                "exp": "1000 ml + 450 ml = 1450 ml.",
                "sol": make_sol_html([
                    "Convert litres to millilitres: 1 L = 1000 ml.",
                    "Add the remaining millilitres: 1000 ml + 450 ml = 1450 ml.",
                    "Therefore, 1 L 450 ml = 1450 ml."
                ], "1 L 450 ml = 1450 ml.")
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(slides_part3)} slides for Part 3.")
    total_q = 0
    for s in slides_part3:
        n_q = len(s.get("quizzes", []))
        total_q += n_q
        print(f"Slide {s['id']}: {s['title']} -> {n_q} questions (Title: {len(s['title'].split())} words)")
        assert 1 <= len(s['title'].split()) <= 3, f"Title length out of bounds for slide {s['id']}!"
        assert n_q == 10, f"Expected 10 questions in slide {s['id']}, found {n_q}!"
    print(f"Total quizzes in Part 3: {total_q}")
    assert total_q == 40, f"Expected 40 questions total, found {total_q}!"

