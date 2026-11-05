# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 6: Measuring Length
Part 3: Slides 17 to 20 (Mastery Challenges 1 to 4, Questions 1 to 40)
Each question includes id, q, options, ans, hint, exp, and sol.
Zero human names. Clean Unicode throughout.
"""

def make_sol_html(steps, note=None):
    items = "".join([f"<li class='text-xs text-slate-300 leading-relaxed'><span class='font-semibold text-amber-400'>Step {idx+1}:</span> {step}</li>" for idx, step in enumerate(steps)])
    note_html = f"<div class='mt-2 p-2 rounded bg-amber-500/10 border border-amber-500/20 text-[11px] text-amber-300'><strong>Note:</strong> {note}</div>" if note else ""
    return f"<ol class='space-y-1.5 list-none pl-0'>{items}</ol>{note_html}"

quiz_q1_to_10 = [
    {
        "id": 1,
        "q": "Which measuring tool is used to record a student's vertical height during a health checkup?",
        "options": ["Vertical height rod (stadiometer)", "Weighing balance", "Thermometer", "Measuring cup"],
        "ans": 0,
        "hint": "Height is vertical linear length from floor to head.",
        "exp": "A vertical height rod (stadiometer) measures height in centimetres.",
        "sol": make_sol_html([
            "Identify the physical quantity being measured: vertical height.",
            "Height is a linear length measured along a straight vertical axis.",
            "The standard clinical instrument for measuring height is the stadiometer (height rod)."
        ])
    },
    {
        "id": 2,
        "q": "Which of the following is a measure of linear distance?",
        "options": ["Height of a classroom doorway", "Body temperature of a student", "Weight of a school bag", "Capacity of a water bottle"],
        "ans": 0,
        "hint": "Linear distance measures how long, wide, or tall an object is.",
        "exp": "Doorway height measures linear distance between the floor and the door frame.",
        "sol": make_sol_html([
            "Review the physical dimensions:",
            "Temperature measures heat, weight measures mass, and capacity measures volume.",
            "Height is a linear measurement of distance between two points."
        ])
    },
    {
        "id": 3,
        "q": "What is the standard metric base unit for measuring larger lengths, such as rooms and doors?",
        "options": ["Metre (m)", "Centimetre (cm)", "Kilogram (kg)", "Litre (L)"],
        "ans": 0,
        "hint": "Represented by the lowercase letter 'm'.",
        "exp": "The metre (m) is the standard base unit for length in the metric system.",
        "sol": make_sol_html([
            "For measuring rooms, athletic tracks, and building dimensions, we use the metre.",
            "The symbol for metre is 'm'.",
            "1 metre equals 100 centimetres."
        ])
    },
    {
        "id": 4,
        "q": "Which classroom dimension is typically greater than 2 metres?",
        "options": ["Height of a standard doorway", "Length of a pencil box", "Breadth of a notebook", "Thickness of a desk"],
        "ans": 0,
        "hint": "Think about what an adult can walk through without hitting their head.",
        "exp": "Standard doorways are built taller than 2 metres (around 2.1 m) so people can walk through easily.",
        "sol": make_sol_html([
            "Adult human height is typically between 1.5 m and 1.9 m.",
            "A standard doorway must be taller than an adult, typically 2.1 metres (210 cm).",
            "Pencil boxes and books are less than 0.3 metres."
        ])
    },
    {
        "id": 5,
        "q": "How many half-metre (1/2 m) rope segments joined end to end equal 1 full metre?",
        "options": ["2 segments", "4 segments", "1 segment", "3 segments"],
        "ans": 0,
        "hint": "1/2 + 1/2 = 1.",
        "exp": "Two half-metre ropes equal 1 full metre: 1/2 m + 1/2 m = 1 m.",
        "sol": make_sol_html([
            "A half metre is 1/2 m.",
            "Adding two half metres: 1/2 m + 1/2 m = 2/2 m = 1 full metre.",
            "Therefore, exactly 2 segments are required."
        ])
    },
    {
        "id": 6,
        "q": "How many quarter-metre (1/4 m) ropes are needed to equal one half-metre (1/2 m)?",
        "options": ["2 ropes", "4 ropes", "1 rope", "8 ropes"],
        "ans": 0,
        "hint": "1/4 + 1/4 = 2/4 = 1/2.",
        "exp": "Two quarter-metre ropes equal 2/4 m, which simplifies to 1/2 m.",
        "sol": make_sol_html([
            "Each quarter-metre rope = 1/4 m.",
            "Combine two ropes: 1/4 m + 1/4 m = 2/4 m.",
            "Simplify 2/4 m = 1/2 m.",
            "Therefore, 2 quarter-metre ropes equal one half-metre."
        ])
    },
    {
        "id": 7,
        "q": "How many quarter-metre (1/4 m) ropes are needed to equal 1 full metre?",
        "options": ["4 ropes", "2 ropes", "8 ropes", "1 rope"],
        "ans": 0,
        "hint": "Four quarters make one whole.",
        "exp": "4 * (1/4 m) = 4/4 m = 1 m.",
        "sol": make_sol_html([
            "Each rope is 1/4 m.",
            "4 ropes combined: 1/4 + 1/4 + 1/4 + 1/4 = 4/4 = 1 whole metre.",
            "So exactly 4 quarter-metre ropes make 1 metre."
        ])
    },
    {
        "id": 8,
        "q": "If a child takes roughly 2 natural walking steps per metre, how many steps are needed to walk a 5-metre line?",
        "options": ["10 steps", "5 steps", "20 steps", "15 steps"],
        "ans": 0,
        "hint": "Multiply 5 metres by 2 steps per metre.",
        "exp": "5 metres * 2 steps/metre = 10 natural walking steps.",
        "sol": make_sol_html([
            "Rate: 1 metre = 2 walking steps.",
            "Total distance = 5 metres.",
            "Total steps = 5 * 2 = 10 walking steps."
        ])
    },
    {
        "id": 9,
        "q": "How many natural walking steps (at 2 steps per metre) are required to walk a 10-metre line?",
        "options": ["20 steps", "10 steps", "5 steps", "30 steps"],
        "ans": 0,
        "hint": "Multiply 10 metres by 2 steps per metre.",
        "exp": "10 metres * 2 steps/metre = 20 steps.",
        "sol": make_sol_html([
            "Distance = 10 metres.",
            "Step rate = 2 steps per metre.",
            "Total steps = 10 * 2 = 20 steps."
        ])
    },
    {
        "id": 10,
        "q": "Which line distance is exactly half the length of a 10-metre line?",
        "options": ["5 metres", "2 metres", "4 metres", "1 metre"],
        "ans": 0,
        "hint": "Divide 10 by 2.",
        "exp": "10 metres / 2 = 5 metres.",
        "sol": make_sol_html([
            "Starting length = 10 metres.",
            "Half of 10 metres = 10 / 2 = 5 metres."
        ])
    }
]

quiz_q11_to_20 = [
    {
        "id": 11,
        "q": "A student in a long jump contest lands at the end of a 1-metre rope plus a 1/2-metre rope. What is the jump distance?",
        "options": ["1 and 1/2 metres", "2 metres", "1 and 1/4 metres", "3 metres"],
        "ans": 0,
        "hint": "Add 1 m + 1/2 m.",
        "exp": "1 m + 1/2 m = 1 1/2 metres (or 1.5 m / 150 cm).",
        "sol": make_sol_html([
            "First rope segment = 1 m.",
            "Second rope segment = 1/2 m.",
            "Total jump distance = 1 m + 1/2 m = 1 1/2 metres."
        ])
    },
    {
        "id": 12,
        "q": "Another jumper reaches 1 metre plus three 1/4-metre ropes. What is the total jump distance?",
        "options": ["1 and 3/4 metres", "1 and 1/2 metres", "2 metres", "1 and 1/4 metres"],
        "ans": 0,
        "hint": "3 ropes of 1/4 m equal 3/4 m.",
        "exp": "1 m + 3/4 m = 1 3/4 metres.",
        "sol": make_sol_html([
            "Three 1/4 m ropes = 3 * (1/4) = 3/4 m.",
            "Add the 1-metre rope: 1 m + 3/4 m = 1 3/4 metres."
        ])
    },
    {
        "id": 13,
        "q": "An adult blue whale measures 30 metres in length. If a city bus is 10 metres long, how many buses parked end to end equal a blue whale?",
        "options": ["3 buses", "2 buses", "4 buses", "5 buses"],
        "ans": 0,
        "hint": "Divide 30 by 10.",
        "exp": "30 metres / 10 metres per bus = 3 buses.",
        "sol": make_sol_html([
            "Whale length = 30 metres.",
            "Bus length = 10 metres.",
            "Number of buses = 30 / 10 = 3 buses."
        ])
    },
    {
        "id": 14,
        "q": "How many 1-metre cricket bats laid end to end match the length of a 30-metre blue whale?",
        "options": ["30 cricket bats", "15 cricket bats", "10 cricket bats", "3 cricket bats"],
        "ans": 0,
        "hint": "Divide 30 by 1.",
        "exp": "30 metres / 1 metre = 30 cricket bats.",
        "sol": make_sol_html([
            "Whale length = 30 metres.",
            "Cricket bat length = 1 metre.",
            "Number of bats = 30 / 1 = 30 bats."
        ])
    },
    {
        "id": 15,
        "q": "If a crocodile measures 6 metres in length, how many crocodiles laid head to tail equal a 30-metre blue whale?",
        "options": ["5 crocodiles", "4 crocodiles", "6 crocodiles", "3 crocodiles"],
        "ans": 0,
        "hint": "Divide 30 by 6.",
        "exp": "30 metres / 6 metres = 5 crocodiles.",
        "sol": make_sol_html([
            "Whale length = 30 metres.",
            "Crocodile length = 6 metres.",
            "Number of crocodiles = 30 / 6 = 5 crocodiles."
        ])
    },
    {
        "id": 16,
        "q": "What is the combined length of two 30-metre blue whales?",
        "options": ["60 metres", "30 metres", "90 metres", "50 metres"],
        "ans": 0,
        "hint": "Multiply 30 by 2.",
        "exp": "30 metres * 2 = 60 metres.",
        "sol": make_sol_html([
            "Single whale length = 30 metres.",
            "Two whales combined = 30 * 2 = 60 metres."
        ])
    },
    {
        "id": 17,
        "q": "How many 10-metre city buses equal the length of two 30-metre blue whales (60 metres)?",
        "options": ["6 buses", "3 buses", "5 buses", "8 buses"],
        "ans": 0,
        "hint": "Divide 60 by 10.",
        "exp": "60 metres / 10 metres per bus = 6 buses.",
        "sol": make_sol_html([
            "Total length of two whales = 60 metres.",
            "Length of one bus = 10 metres.",
            "Number of buses = 60 / 10 = 6 buses."
        ])
    },
    {
        "id": 18,
        "q": "Three 6-metre crocodiles line up along a riverbank. What is their total combined length?",
        "options": ["18 metres", "12 metres", "24 metres", "15 metres"],
        "ans": 0,
        "hint": "Multiply 6 by 3.",
        "exp": "6 metres * 3 = 18 metres.",
        "sol": make_sol_html([
            "Length per crocodile = 6 metres.",
            "Number of crocodiles = 3.",
            "Total length = 6 * 3 = 18 metres."
        ])
    },
    {
        "id": 19,
        "q": "An ostrich stands 3 metres tall. How many ostriches stacked vertically match the 30-metre length of a blue whale?",
        "options": ["10 ostriches", "5 ostriches", "15 ostriches", "3 ostriches"],
        "ans": 0,
        "hint": "Divide 30 by 3.",
        "exp": "30 metres / 3 metres per ostrich = 10 ostriches.",
        "sol": make_sol_html([
            "Whale length = 30 metres.",
            "Ostrich height = 3 metres.",
            "Number of ostriches = 30 / 3 = 10 ostriches."
        ])
    },
    {
        "id": 20,
        "q": "A giraffe stands 4 metres tall. How many metres taller is a 6-metre crocodile's length compared to a 4-metre giraffe's height?",
        "options": ["2 metres", "1 metre", "3 metres", "10 metres"],
        "ans": 0,
        "hint": "Subtract 6 - 4.",
        "exp": "6 metres - 4 metres = 2 metres.",
        "sol": make_sol_html([
            "Crocodile length = 6 metres.",
            "Giraffe height = 4 metres.",
            "Difference = 6 - 4 = 2 metres."
        ])
    }
]

quiz_q21_to_30 = [
    {
        "id": 21,
        "q": "Which metric unit is most suitable for measuring the length of a small pencil eraser?",
        "options": ["Centimetre (cm)", "Metre (m)", "Kilometre (km)", "Litre (L)"],
        "ans": 0,
        "hint": "A unit smaller than a metre.",
        "exp": "The centimetre (cm) is ideal for small handheld items like erasers.",
        "sol": make_sol_html([
            "Erasers are pocket-sized objects less than 10 cm long.",
            "A metre is too large (1 metre = 100 cm).",
            "Therefore, the centimetre is the most appropriate unit."
        ])
    },
    {
        "id": 22,
        "q": "How many centimetres are there in 1 full metre?",
        "options": ["100 cm", "10 cm", "1000 cm", "50 cm"],
        "ans": 0,
        "hint": "Centi- means one hundredth.",
        "exp": "1 metre = 100 centimetres.",
        "sol": make_sol_html([
            "The metric prefix 'centi' denotes 1/100.",
            "There are 100 centimetres in 1 metre.",
            "1 m = 100 cm."
        ])
    },
    {
        "id": 23,
        "q": "How many centimetres equal a half metre (1/2 m)?",
        "options": ["50 cm", "25 cm", "75 cm", "100 cm"],
        "ans": 0,
        "hint": "Half of 100 is...",
        "exp": "100 cm / 2 = 50 cm.",
        "sol": make_sol_html([
            "1 full metre = 100 cm.",
            "Half metre = 100 / 2 = 50 cm."
        ])
    },
    {
        "id": 24,
        "q": "How many centimetres equal a quarter metre (1/4 m)?",
        "options": ["25 cm", "50 cm", "75 cm", "20 cm"],
        "ans": 0,
        "hint": "Divide 100 by 4.",
        "exp": "100 cm / 4 = 25 cm.",
        "sol": make_sol_html([
            "1 metre = 100 cm.",
            "Quarter metre = 100 / 4 = 25 cm."
        ])
    },
    {
        "id": 25,
        "q": "Which of the following objects typically measures less than 1 centimetre in length?",
        "options": ["A grain of basmati rice", "A standard pencil", "A school eraser", "A classroom notebook"],
        "ans": 0,
        "hint": "A grain of rice is roughly 7 to 8 millimetres.",
        "exp": "A grain of rice is about 8 mm (0.8 cm), which is less than 1 cm.",
        "sol": make_sol_html([
            "1 centimetre = 10 millimetres.",
            "A grain of rice is approximately 7 to 8 mm long.",
            "Since 8 mm < 10 mm, it measures less than 1 cm."
        ])
    },
    {
        "id": 26,
        "q": "In a ramp rolling experiment, Toy Car A travels 142 cm and Toy Car B travels 168 cm. Which car rolled further and by how much?",
        "options": ["Car B by 26 cm", "Car A by 26 cm", "Car B by 16 cm", "Car A by 142 cm"],
        "ans": 0,
        "hint": "Subtract 168 - 142.",
        "exp": "168 cm - 142 cm = 26 cm. Car B rolled further.",
        "sol": make_sol_html([
            "Car A distance = 142 cm.",
            "Car B distance = 168 cm.",
            "Difference = 168 - 142 = 26 cm.",
            "Car B traveled 26 cm further than Car A."
        ])
    },
    {
        "id": 27,
        "q": "A toy car rolls 215 cm. How is this distance expressed in metres and centimetres?",
        "options": ["2 m 15 cm", "21 m 5 cm", "20 m 15 cm", "1 m 115 cm"],
        "ans": 0,
        "hint": "200 cm = 2 m.",
        "exp": "215 cm = 200 cm + 15 cm = 2 m 15 cm.",
        "sol": make_sol_html([
            "Each 100 cm equals 1 m.",
            "215 cm = 200 cm + 15 cm.",
            "200 cm = 2 m.",
            "Total = 2 m 15 cm."
        ])
    },
    {
        "id": 28,
        "q": "On a 1-cm square grid map, a path traverses 24 tile edges. What is the total length of the path?",
        "options": ["24 cm", "12 cm", "48 cm", "20 cm"],
        "ans": 0,
        "hint": "Each grid tile edge equals 1 cm.",
        "exp": "24 edges * 1 cm per edge = 24 cm.",
        "sol": make_sol_html([
            "Each grid unit = 1 cm.",
            "Number of units walked = 24.",
            "Total path length = 24 * 1 cm = 24 cm."
        ])
    },
    {
        "id": 29,
        "q": "Comparing Path A (24 cm) and Path C (18 cm) on a grid map, which path is shorter and by how much?",
        "options": ["Path C is shorter by 6 cm", "Path A is shorter by 6 cm", "Path C is shorter by 4 cm", "Path A is shorter by 8 cm"],
        "ans": 0,
        "hint": "Subtract 24 - 18.",
        "exp": "24 cm - 18 cm = 6 cm. Path C is shorter by 6 cm.",
        "sol": make_sol_html([
            "Path A = 24 cm.",
            "Path C = 18 cm.",
            "Difference = 24 - 18 = 6 cm.",
            "Path C is the shorter route by 6 cm."
        ])
    },
    {
        "id": 30,
        "q": "What is the primary rule when starting a measurement on an ordinary, unbroken ruler?",
        "options": ["Align the starting edge of the object with the 0 mark", "Align with the 1 cm mark", "Align with the plastic edge of the ruler", "Align with the middle mark"],
        "ans": 0,
        "hint": "Measurement originates at zero.",
        "exp": "The zero mark represents zero distance and must align with the object's starting edge.",
        "sol": make_sol_html([
            "Measurement measures distance from an origin.",
            "The 0 line on a ruler marks zero length.",
            "Starting at the physical plastic edge or 1 cm leads to measurement error."
        ])
    }
]

quiz_q31_to_40 = [
    {
        "id": 31,
        "q": "An eraser measured using a broken ruler begins at 2 cm and ends at 9 cm. What is the actual length of the eraser?",
        "options": ["7 cm", "9 cm", "11 cm", "2 cm"],
        "ans": 0,
        "hint": "Subtract the start mark from the end mark: 9 - 2.",
        "exp": "Length = End - Start = 9 cm - 2 cm = 7 cm.",
        "sol": make_sol_html([
            "Starting mark = 2 cm.",
            "Ending mark = 9 cm.",
            "Actual length = Ending mark - Starting mark.",
            "9 cm - 2 cm = 7 cm."
        ])
    },
    {
        "id": 32,
        "q": "A pencil measured with a broken ruler starts at 4 cm and ends at 15 cm. What is its length?",
        "options": ["11 cm", "15 cm", "19 cm", "12 cm"],
        "ans": 0,
        "hint": "Subtract 15 - 4.",
        "exp": "15 cm - 4 cm = 11 cm.",
        "sol": make_sol_html([
            "End coordinate = 15 cm.",
            "Start coordinate = 4 cm.",
            "Length = 15 - 4 = 11 cm."
        ])
    },
    {
        "id": 33,
        "q": "How many 20-cm decorative stickers are needed to cover a 2-metre (200 cm) bulletin board border?",
        "options": ["10 stickers", "20 stickers", "5 stickers", "15 stickers"],
        "ans": 0,
        "hint": "Convert 2 m to 200 cm, then divide by 20 cm.",
        "exp": "200 cm / 20 cm = 10 stickers.",
        "sol": make_sol_html([
            "Total border length = 2 m = 200 cm.",
            "Length of one sticker = 20 cm.",
            "Number of stickers = 200 / 20 = 10 stickers."
        ])
    },
    {
        "id": 34,
        "q": "How many 10-cm stickers are needed to cover an 80-cm greeting card border?",
        "options": ["8 stickers", "10 stickers", "4 stickers", "12 stickers"],
        "ans": 0,
        "hint": "Divide 80 by 10.",
        "exp": "80 cm / 10 cm = 8 stickers.",
        "sol": make_sol_html([
            "Border length = 80 cm.",
            "Sticker length = 10 cm.",
            "Number of stickers = 80 / 10 = 8 stickers."
        ])
    },
    {
        "id": 35,
        "q": "What is 5 metres and 50 centimetres expressed entirely in centimetres?",
        "options": ["550 cm", "505 cm", "5500 cm", "55 cm"],
        "ans": 0,
        "hint": "5 m = 500 cm. Add 50 cm.",
        "exp": "500 cm + 50 cm = 550 cm.",
        "sol": make_sol_html([
            "Convert metres to centimetres: 5 m = 5 * 100 cm = 500 cm.",
            "Add the extra centimetres: 500 cm + 50 cm = 550 cm."
        ])
    },
    {
        "id": 36,
        "q": "How many metres and centimetres are in 325 centimetres?",
        "options": ["3 m 25 cm", "32 m 5 cm", "30 m 25 cm", "2 m 125 cm"],
        "ans": 0,
        "hint": "300 cm = 3 m, with 25 cm remaining.",
        "exp": "325 cm = 300 cm + 25 cm = 3 m 25 cm.",
        "sol": make_sol_html([
            "Separate hundreds: 325 cm = 300 cm + 25 cm.",
            "Convert 300 cm to metres: 300 / 100 = 3 m.",
            "Total = 3 m 25 cm."
        ])
    },
    {
        "id": 37,
        "q": "What is the mathematical definition of perimeter?",
        "options": ["The total length of the continuous boundary around a closed shape", "The area of space inside a shape", "The weight of a boundary fence", "The vertical height of a solid object"],
        "ans": 0,
        "hint": "Perimeter measures the distance all the way around the outside edge.",
        "exp": "Perimeter is the total linear distance along the complete outer boundary of a closed figure.",
        "sol": make_sol_html([
            "In geometry, perimeter refers to boundary length.",
            "It is found by adding the lengths of all outer sides of a closed 2D shape."
        ])
    },
    {
        "id": 38,
        "q": "A rectangular vegetable garden is 5 metres long and 3 metres wide. What is its perimeter?",
        "options": ["16 metres", "15 metres", "8 metres", "10 metres"],
        "ans": 0,
        "hint": "Add all 4 sides: 5 + 3 + 5 + 3.",
        "exp": "Perimeter = 5 m + 3 m + 5 m + 3 m = 16 m.",
        "sol": make_sol_html([
            "A rectangle has two lengths and two breadths.",
            "Lengths = 5 m and 5 m.",
            "Breadths = 3 m and 3 m.",
            "Perimeter = 5 + 3 + 5 + 3 = 16 metres."
        ])
    },
    {
        "id": 39,
        "q": "What is the perimeter of a square garden bed whose sides each measure 5 metres?",
        "options": ["20 metres", "25 metres", "15 metres", "10 metres"],
        "ans": 0,
        "hint": "A square has 4 equal sides: 4 * 5.",
        "exp": "Perimeter = 5 m + 5 m + 5 m + 5 m = 20 m.",
        "sol": make_sol_html([
            "A square has 4 equal sides.",
            "Each side = 5 m.",
            "Perimeter = 4 * 5 m = 20 metres."
        ])
    },
    {
        "id": 40,
        "q": "A rectangle has a length of 7 metres and a breadth of 3 metres. What is its perimeter?",
        "options": ["20 metres", "21 metres", "10 metres", "14 metres"],
        "ans": 0,
        "hint": "Add all four sides: 7 + 3 + 7 + 3.",
        "exp": "Perimeter = 7 m + 3 m + 7 m + 3 m = 20 m. (Notice it equals the 5 m square's perimeter!)",
        "sol": make_sol_html([
            "Sides are 7 m, 3 m, 7 m, and 3 m.",
            "Perimeter = 7 + 3 + 7 + 3 = 20 metres.",
            "Notice that two completely different shapes (a 5m square and a 7m by 3m rectangle) can have the exact same perimeter!"
        ])
    }
]

slides_part3 = [
    {
        "id": 17,
        "title": "Challenge 1",
        "section": "Mastery Challenge",
        "quiz": quiz_q1_to_10
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "section": "Mastery Challenge",
        "quiz": quiz_q11_to_20
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "section": "Mastery Challenge",
        "quiz": quiz_q21_to_30
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "section": "Mastery Challenge",
        "quiz": quiz_q31_to_40
    }
]

if __name__ == "__main__":
    assert len(slides_part3) == 4
    for s in slides_part3:
        assert len(s["quiz"]) == 10
        print(f"Slide {s['id']}: {s['title']} has {len(s['quiz'])} questions.")
    print("Part 3 slides valid!")

