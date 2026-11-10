# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 14: Data Handling
Part 3: Slides 17 to 20 Data Generator (40 Quiz Questions)
Short headings: Challenge 1, Challenge 2, Challenge 3, Challenge 4.
Zero human names (Rohan, Anjali, etc. replaced with generic roles).
Clean Unicode throughout (×, ÷, ₹, etc.).
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
        "section": "Surveys, Letter Codes & Frequency Tables",
        "speech": "",
        "quizzes": [
            {
                "q": "Why is 'Which single subject is your favorite?' better than 'What do you like in school?' for a data survey?",
                "options": ["It produces exactly one specific, countable response per respondent", "It takes longer to write down", "It only allows math answers", "It forces students to guess"],
                "ans": 0,
                "hint": "Think about what kind of answers make counting straightforward.",
                "exp": "A specific question limits each student to one choice, eliminating ambiguity and overlapping answers.",
                "sol": make_sol_html([
                    "Open-ended questions allow multiple or descriptive responses, making tallying very difficult.",
                    "A specific question ('Which single subject...') yields exactly one categorical data item per student.",
                    "This ensures the number of responses equals the number of participants surveyed."
                ], "Well-defined survey questions lead to clean, organized categorical data.")
            },
            {
                "q": "In a survey of 45 students, responses are recorded using letter codes: M for Mathematics, L for Languages, T for The World Around Us, A for Arts, and P.E. for Physical Education. If 14 chose M and 9 chose L, how many chose either M or L?",
                "options": ["21 students", "23 students", "25 students", "27 students"],
                "ans": 1,
                "hint": "Add the number of students who chose M to those who chose L.",
                "exp": "14 + 9 = 23 students chose either Mathematics or Languages.",
                "sol": make_sol_html([
                    "Identify the count for Mathematics (M): 14 students.",
                    "Identify the count for Languages (L): 9 students.",
                    "Add both frequencies together: 14 + 9 = 23 students."
                ], "Combined frequency is found by summing the individual counts.")
            },
            {
                "q": "If 45 students were surveyed and the frequencies are M = 14, L = 9, T = 7, and A = 5, how many students chose Physical Education (P.E.)?",
                "options": ["8 students", "9 students", "10 students", "12 students"],
                "ans": 2,
                "hint": "Subtract the sum of the known subjects from the total of 45 students.",
                "exp": "45 − (14 + 9 + 7 + 5) = 45 − 35 = 10 students.",
                "sol": make_sol_html([
                    "Sum the frequencies of the other four subjects: 14 + 9 + 7 + 5 = 35.",
                    "Subtract this partial sum from the total class size: 45 − 35 = 10.",
                    "Therefore, 10 students chose Physical Education."
                ], "The sum of all category frequencies must equal the total sample size.")
            },
            {
                "q": "Based on the frequency table (M: 14, L: 9, T: 7, A: 5, P.E.: 10), which subject is the least popular among the students?",
                "options": ["Mathematics", "Languages", "The World Around Us", "Arts"],
                "ans": 3,
                "hint": "Look for the category with the smallest frequency number.",
                "exp": "Arts has only 5 votes, which is the lowest frequency in the table.",
                "sol": make_sol_html([
                    "Compare the frequencies: M = 14, L = 9, T = 7, A = 5, P.E. = 10.",
                    "Identify the minimum value among {14, 9, 7, 5, 10}.",
                    "The smallest number is 5, corresponding to Arts."
                ], "The least popular choice is represented by the lowest frequency count.")
            },
            {
                "q": "By how many votes did Mathematics (14) exceed Arts (5)?",
                "options": ["7 votes", "8 votes", "9 votes", "10 votes"],
                "ans": 2,
                "hint": "Find the difference between 14 and 5.",
                "exp": "14 − 5 = 9 votes.",
                "sol": make_sol_html([
                    "Identify the frequency of Mathematics: 14.",
                    "Identify the frequency of Arts: 5.",
                    "Subtract to find the difference: 14 − 5 = 9."
                ], "Comparing quantities involves subtracting the smaller frequency from the larger.")
            },
            {
                "q": "What fraction of the total 45 students chose Physical Education (10 students)?",
                "options": ["10/45", "10/35", "5/45", "14/45"],
                "ans": 0,
                "hint": "Form a fraction with the category count in the numerator and total students in the denominator.",
                "exp": "10 out of 45 students simplifies to 10/45 (or 2/9).",
                "sol": make_sol_html([
                    "Category frequency = 10.",
                    "Total surveyed students = 45.",
                    "Fractional representation = 10/45, which simplifies by dividing numerator and denominator by 5 to 2/9."
                ], "A proportion is written as part over whole.")
            },
            {
                "q": "A student surveyor recorded 30 responses. If 8 picked blue, 12 picked red, and the rest picked green, how many picked green?",
                "options": ["8 students", "10 students", "12 students", "14 students"],
                "ans": 1,
                "hint": "Add blue and red, then subtract from 30.",
                "exp": "30 − (8 + 12) = 30 − 20 = 10 students.",
                "sol": make_sol_html([
                    "Add the known responses: 8 + 12 = 20.",
                    "Subtract from the total of 30: 30 − 20 = 10 students.",
                    "10 students picked green."
                ], "Unknown frequencies are found by subtracting known counts from the total.")
            },
            {
                "q": "In a data table, what does each row in the first column typically represent?",
                "options": ["A category or option name", "The total sum", "The date of survey", "The student ID"],
                "ans": 0,
                "hint": "Think about what categories like 'Mathematics' or 'Languages' represent.",
                "exp": "The first column lists the categorical labels or survey options being evaluated.",
                "sol": make_sol_html([
                    "Frequency tables organize data into categories and counts.",
                    "The first column contains distinct categorical labels.",
                    "The second column lists the numeric frequency of each category."
                ], "Clear table column headings make data interpretable at a glance.")
            },
            {
                "q": "If a researcher wants to verify that no raw survey data was lost during tabulation, what check should be performed?",
                "options": ["Multiply the frequencies together", "Sum the frequencies and verify it matches the total number of raw responses", "Sort the subjects alphabetically", "Delete duplicate responses"],
                "ans": 1,
                "hint": "Check the relationship between the sum of the table rows and total responses collected.",
                "exp": "The sum of all frequencies in the table must equal the total number of survey respondents.",
                "sol": make_sol_html([
                    "Count the total number of raw responses collected.",
                    "Sum all values in the frequency column.",
                    "Ensure both numbers match exactly; any discrepancy indicates a counting error."
                ], "Summing frequencies is the standard verification step in data auditing.")
            },
            {
                "q": "If 14 students chose Mathematics, 9 chose Languages, and 7 chose The World Around Us, what is the combined total for these three subjects?",
                "options": ["28 students", "30 students", "32 students", "35 students"],
                "ans": 1,
                "hint": "Add 14 + 9 + 7.",
                "exp": "14 + 9 + 7 = 30 students.",
                "sol": make_sol_html([
                    "Add the first two subjects: 14 + 9 = 23.",
                    "Add the third subject: 23 + 7 = 30.",
                    "The combined total is 30 students."
                ], "Cumulative addition groups subcategories for broader analysis.")
            }
        ]
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "section": "Tally Marks, Pictographs & Contingency Tables",
        "speech": "",
        "quizzes": [
            {
                "q": "How is the number 13 represented using standard tally marks?",
                "options": ["Two groups of 5 and 3 single lines", "Three groups of 4 and 1 single line", "One group of 10 and 3 lines", "13 vertical strokes with no grouping"],
                "ans": 0,
                "hint": "Tally marks group by 5s using 4 vertical lines and 1 diagonal slash.",
                "exp": "13 = 5 + 5 + 3, which is 2 completed tally gates of 5 plus 3 single vertical lines.",
                "sol": make_sol_html([
                    "Divide 13 by 5: 13 = (2 × 5) + 3.",
                    "Each group of 5 is drawn as 4 vertical strokes crossed by 1 diagonal slash.",
                    "The remaining 3 are drawn as individual vertical strokes.",
                    "Result: 2 full tally bundles and 3 single strokes."
                ], "Tally bundles of 5 facilitate fast skip-counting.")
            },
            {
                "q": "In an ice gola survey, each cup icon in a pictograph represents 4 ice golas. If the row for Kala Khatta shows 7 cup icons, how many ice golas were sold?",
                "options": ["24 golas", "28 golas", "32 golas", "36 golas"],
                "ans": 1,
                "hint": "Multiply the number of icons by the value of each icon.",
                "exp": "7 × 4 = 28 ice golas.",
                "sol": make_sol_html([
                    "Identify the scale key: 1 cup icon = 4 ice golas.",
                    "Count the number of icons for Kala Khatta: 7 icons.",
                    "Multiply: 7 × 4 = 28 ice golas."
                ], "Pictograph totals equal (number of icons) × (scale key value).")
            },
            {
                "q": "If 36 Orange ice golas were sold and each cup icon represents 4 golas, how many cup icons must be drawn?",
                "options": ["7 icons", "8 icons", "9 icons", "10 icons"],
                "ans": 2,
                "hint": "Divide 36 by 4.",
                "exp": "36 ÷ 4 = 9 cup icons.",
                "sol": make_sol_html([
                    "Total items = 36.",
                    "Scale key = 4 items per icon.",
                    "Divide total by scale key: 36 ÷ 4 = 9 icons."
                ], "Number of icons to draw = (total quantity) ÷ (scale value).")
            },
            {
                "q": "In a two-way sports table: 12 boys play only cricket, 4 boys play only chess, 6 boys play both sports, and 2 boys play neither sport. What is the total number of boys?",
                "options": ["20 boys", "22 boys", "24 boys", "26 boys"],
                "ans": 2,
                "hint": "Add all four categories across the boys' row.",
                "exp": "12 + 4 + 6 + 2 = 24 boys.",
                "sol": make_sol_html([
                    "Sum the components: Only Cricket (12) + Only Chess (4) = 16.",
                    "Add Both (6): 16 + 6 = 22.",
                    "Add Neither (2): 22 + 2 = 24 boys."
                ], "Row totals in contingency tables sum all mutually exclusive subsets.")
            },
            {
                "q": "If 6 boys and 5 girls play both sports, how many total students play both sports?",
                "options": ["9 students", "10 students", "11 students", "12 students"],
                "ans": 2,
                "hint": "Add the boys and girls in the 'Both' column.",
                "exp": "6 + 5 = 11 students play both sports.",
                "sol": make_sol_html([
                    "Boys playing both sports = 6.",
                    "Girls playing both sports = 5.",
                    "Column total = 6 + 5 = 11 students."
                ], "Column totals combine counts across all rows for that specific category.")
            },
            {
                "q": "In the sports table, 12 boys and 8 girls play only cricket. How many total students play only cricket?",
                "options": ["18 students", "20 students", "22 students", "24 students"],
                "ans": 1,
                "hint": "Sum 12 and 8.",
                "exp": "12 + 8 = 20 students.",
                "sol": make_sol_html([
                    "Boys playing only cricket = 12.",
                    "Girls playing only cricket = 8.",
                    "Total = 12 + 8 = 20 students."
                ], "Category totals aggregate across demographic divisions.")
            },
            {
                "q": "If a class has 24 boys and 24 girls, what is the grand total of students surveyed?",
                "options": ["44 students", "46 students", "48 students", "50 students"],
                "ans": 2,
                "hint": "Add 24 and 24.",
                "exp": "24 + 24 = 48 students.",
                "sol": make_sol_html([
                    "Total boys = 24.",
                    "Total girls = 24.",
                    "Grand total = 24 + 24 = 48 students."
                ], "The bottom-right cell in a contingency table is the grand total.")
            },
            {
                "q": "How many total students play NEITHER sport if 2 boys and 4 girls play neither?",
                "options": ["4 students", "5 students", "6 students", "8 students"],
                "ans": 2,
                "hint": "Add 2 and 4.",
                "exp": "2 + 4 = 6 students.",
                "sol": make_sol_html([
                    "Boys playing neither = 2.",
                    "Girls playing neither = 4.",
                    "Total neither = 2 + 4 = 6 students."
                ], "Summing subsets gives the total non-participating count.")
            },
            {
                "q": "In a pictograph, if 1 star icon represents 10 books, what does 3 and a half star icons represent?",
                "options": ["30 books", "35 books", "40 books", "45 books"],
                "ans": 1,
                "hint": "3 whole stars = 3 × 10; half star = 5 books.",
                "exp": "(3 × 10) + 5 = 30 + 5 = 35 books.",
                "sol": make_sol_html([
                    "Value of 1 whole icon = 10 books.",
                    "3 whole icons = 3 × 10 = 30 books.",
                    "Half of an icon = 10 ÷ 2 = 5 books.",
                    "Total books = 30 + 5 = 35 books."
                ], "Half icons represent half the value of the full scale key.")
            },
            {
                "q": "Why is a two-way classification matrix useful for data with two characteristics (like gender and favorite sport)?",
                "options": ["It hides unnecessary facts", "It allows simultaneous viewing of both variables, their intersections, and their row/column totals", "It requires fewer numbers", "It turns numbers into words"],
                "ans": 1,
                "hint": "Think about how two variables like gender and sport preference interact.",
                "exp": "Contingency matrices organize data across two variables at once, showing marginal and joint distributions.",
                "sol": make_sol_html([
                    "One-way tables can only show one property at a time.",
                    "A two-way matrix cross-tabulates two variables (e.g., gender across sport preferences).",
                    "It displays joint categories (boys who play cricket) alongside marginal totals (all boys, all cricket players)."
                ], "Cross-tabulation reveals associations between two variables.")
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "section": "Fair Data, Sales Trends, Dienes Blocks & Nets",
        "speech": "",
        "quizzes": [
            {
                "q": "At the school Bal Mela, a stall sold 20 fruit chaats on Friday, 40 on Saturday, and 30 on Sunday. What were the total fruit chaats sold over all 3 days?",
                "options": ["80 servings", "85 servings", "90 servings", "95 servings"],
                "ans": 2,
                "hint": "Add 20 + 40 + 30.",
                "exp": "20 + 40 + 30 = 90 fruit chaat servings.",
                "sol": make_sol_html([
                    "Friday sales = 20.",
                    "Saturday sales = 40.",
                    "Sunday sales = 30.",
                    "Total = 20 + 40 + 30 = 90 servings."
                ], "Multi-day totals combine individual daily sales.")
            },
            {
                "q": "If the stall sold 30 sandwiches on Friday, 50 on Saturday, and 40 on Sunday, how many total sandwiches were sold?",
                "options": ["110 sandwiches", "120 sandwiches", "130 sandwiches", "140 sandwiches"],
                "ans": 1,
                "hint": "Add 30 + 50 + 40.",
                "exp": "30 + 50 + 40 = 120 sandwiches.",
                "sol": make_sol_html([
                    "Friday sandwiches = 30.",
                    "Saturday sandwiches = 50.",
                    "Sunday sandwiches = 40.",
                    "Total = 30 + 50 + 40 = 120 sandwiches."
                ], "Add daily components systematically to find total weekend volume.")
            },
            {
                "q": "On Saturday, 40 fruit chaats and 50 sandwiches were sold. What was the total snack volume sold on Saturday?",
                "options": ["80 portions", "85 portions", "90 portions", "95 portions"],
                "ans": 2,
                "hint": "Add Saturday's fruit chaat and sandwich sales.",
                "exp": "40 + 50 = 90 snack portions.",
                "sol": make_sol_html([
                    "Fruit chaat portions = 40.",
                    "Sandwich portions = 50.",
                    "Total Saturday portions = 40 + 50 = 90 portions."
                ], "Daily item totals sum all categories sold on that particular day.")
            },
            {
                "q": "How many more sandwiches (120 total) were sold than fruit chaats (90 total) over the entire weekend?",
                "options": ["20 more", "25 more", "30 more", "35 more"],
                "ans": 2,
                "hint": "Subtract 90 from 120.",
                "exp": "120 − 90 = 30 more sandwiches.",
                "sol": make_sol_html([
                    "Total sandwiches = 120.",
                    "Total fruit chaat = 90.",
                    "Difference = 120 − 90 = 30 sandwiches."
                ], "Comparative difference highlights relative product demand.")
            },
            {
                "q": "In base-ten Dienes blocks, how many unit cubes are contained in 3 hundreds flats?",
                "options": ["30 cubes", "100 cubes", "300 cubes", "3,000 cubes"],
                "ans": 2,
                "hint": "Each flat contains 100 unit cubes. Multiply 3 by 100.",
                "exp": "3 × 100 = 300 unit cubes.",
                "sol": make_sol_html([
                    "1 hundreds flat = 100 unit cubes.",
                    "3 hundreds flats = 3 × 100 = 300 unit cubes."
                ], "Dienes flats represent groups of one hundred units.")
            },
            {
                "q": "What number is represented by 2 thousands cubes, 4 hundreds flats, 5 tens rods, and 7 unit cubes?",
                "options": ["2,457", "2,547", "2,475", "2,754"],
                "ans": 0,
                "hint": "Combine the place values: 2,000 + 400 + 50 + 7.",
                "exp": "2,000 + 400 + 50 + 7 = 2,457.",
                "sol": make_sol_html([
                    "Thousands: 2 × 1,000 = 2,000.",
                    "Hundreds: 4 × 100 = 400.",
                    "Tens: 5 × 10 = 50.",
                    "Ones: 7 × 1 = 7.",
                    "Total = 2,000 + 400 + 50 + 7 = 2,457."
                ], "Base-ten blocks map directly to the digits of standard decimal notation.")
            },
            {
                "q": "How many faces does the net of a rectangular cuboid have?",
                "options": ["4 faces", "5 faces", "6 faces", "8 faces"],
                "ans": 2,
                "hint": "Think of a cardboard shoe box or cereal box unfolded flat.",
                "exp": "A cuboid has 6 rectangular faces (top, bottom, and 4 sides).",
                "sol": make_sol_html([
                    "A cuboid has 3 pairs of opposite identical rectangular faces.",
                    "Pair 1: top and bottom (2 faces).",
                    "Pair 2: front and back (2 faces).",
                    "Pair 3: left and right sides (2 faces).",
                    "Total = 2 + 2 + 2 = 6 faces."
                ], "A 3D box unfolds into a 2D net of 6 connected rectangles.")
            },
            {
                "q": "Which 3D solid is formed by folding a net consisting of 2 identical triangular bases and 3 rectangular faces?",
                "options": ["Square pyramid", "Triangular prism", "Cone", "Cube"],
                "ans": 1,
                "hint": "The two triangular ends are connected by three rectangular sides.",
                "exp": "A triangular prism has 2 triangular bases and 3 rectangular sides.",
                "sol": make_sol_html([
                    "Identify the base polygons: 2 triangles.",
                    "Identify the lateral connecting faces: 3 rectangles.",
                    "When folded, this creates a triangular prism."
                ], "Prisms have identical parallel bases joined by rectangular lateral faces.")
            },
            {
                "q": "What 3D shape is formed when a net with 1 square center and 4 triangular flaps is folded upward?",
                "options": ["Triangular prism", "Cuboid", "Square pyramid", "Cylinder"],
                "ans": 2,
                "hint": "The triangular flaps meet at a single top vertex above the square base.",
                "exp": "A square base with 4 triangular faces folding to an apex forms a square pyramid.",
                "sol": make_sol_html([
                    "Base = 1 square.",
                    "Surrounding faces = 4 triangles.",
                    "When folded up, the triangular vertices meet at a single point (apex).",
                    "This solid is a square pyramid."
                ], "Pyramids have a polygon base and triangular sides meeting at a point.")
            },
            {
                "q": "If a food stall earned ₹10 for each fruit chaat and ₹15 for each sandwich, how much money was earned on Friday (20 chaats, 30 sandwiches)?",
                "options": ["₹550", "₹600", "₹650", "₹700"],
                "ans": 2,
                "hint": "Calculate (20 × 10) + (30 × 15).",
                "exp": "(20 × 10) + (30 × 15) = ₹200 + ₹450 = ₹650.",
                "sol": make_sol_html([
                    "Earnings from fruit chaat: 20 × ₹10 = ₹200.",
                    "Earnings from sandwiches: 30 × ₹15 = ₹450.",
                    "Total earnings: ₹200 + ₹450 = ₹650."
                ], "Multiplying item counts by unit prices gives total sales revenue.")
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "section": "Arrow Cards, Fraction Strips & Box Models",
        "speech": "",
        "quizzes": [
            {
                "q": "Which arrow cards are needed to compose the number 5,842?",
                "options": ["5,000, 800, 40, and 2", "500, 80, 4, and 2", "5,000, 840, and 2", "5,800, 40, and 2"],
                "ans": 0,
                "hint": "Decompose 5,842 into standard place values: thousands, hundreds, tens, and ones.",
                "exp": "5,842 = 5,000 + 800 + 40 + 2.",
                "sol": make_sol_html([
                    "Thousands place: 5 × 1,000 = 5,000.",
                    "Hundreds place: 8 × 100 = 800.",
                    "Tens place: 4 × 10 = 40.",
                    "Ones place: 2 × 1 = 2.",
                    "Arrow cards needed: 5,000, 800, 40, and 2."
                ], "Arrow cards visually represent expanded notation.")
            },
            {
                "q": "When arrow cards 7,000, 30, and 5 are stacked with tips aligned, what number is displayed?",
                "options": ["7,350", "7,035", "7,305", "735"],
                "ans": 1,
                "hint": "Notice there is no hundreds card (0 hundreds).",
                "exp": "7,000 + 30 + 5 = 7,035.",
                "sol": make_sol_html([
                    "Thousands: 7,000.",
                    "Hundreds: 0 (no hundreds card present).",
                    "Tens: 30.",
                    "Ones: 5.",
                    "Combined numeral: 7,035."
                ], "Zero serves as a crucial place holder when a place value card is missing.")
            },
            {
                "q": "Using a fraction strip kit, how many 1/8 strips are equal to 1/2 strip?",
                "options": ["2 strips", "3 strips", "4 strips", "6 strips"],
                "ans": 2,
                "hint": "Divide 1/2 by 1/8: (1/2) ÷ (1/8) = 4.",
                "exp": "4 × 1/8 = 4/8 = 1/2. Exactly 4 one-eighth strips equal one-half strip.",
                "sol": make_sol_html([
                    "Compare 1/8 with 1/2.",
                    "Find equivalent fraction with denominator 8: 1/2 = 4/8.",
                    "Therefore, 4 pieces of 1/8 are needed to equal 1/2."
                ], "Equivalent fractions cover the exact same physical length on fraction strips.")
            },
            {
                "q": "If the full fraction strip is 24 cm long, what is the length of a 1/4 segment?",
                "options": ["4 cm", "6 cm", "8 cm", "12 cm"],
                "ans": 1,
                "hint": "Divide 24 cm by 4.",
                "exp": "24 cm ÷ 4 = 6 cm.",
                "sol": make_sol_html([
                    "Total benchmark strip length = 24 cm.",
                    "A 1/4 segment represents one of four equal parts.",
                    "Length = 24 ÷ 4 = 6 cm."
                ], "Fractional parts represent equal division of a linear measure.")
            },
            {
                "q": "Which fraction is larger: 1/3 or 1/4?",
                "options": ["1/3 is larger", "1/4 is larger", "They are equal", "Cannot be determined"],
                "ans": 0,
                "hint": "When dividing the same whole into fewer equal parts, each part is bigger.",
                "exp": "1/3 is larger than 1/4 because 1/3 of 24 cm is 8 cm, while 1/4 is 6 cm.",
                "sol": make_sol_html([
                    "Divide whole into 3 parts: each part = 1/3 (8 cm on a 24 cm strip).",
                    "Divide whole into 4 parts: each part = 1/4 (6 cm on a 24 cm strip).",
                    "Since 8 cm > 6 cm, 1/3 > 1/4."
                ], "For unit fractions with numerator 1, smaller denominators mean larger parts.")
            },
            {
                "q": "In a combine word problem model, a sports coordinator has 18 badminton rackets and receives 14 new rackets. What is the total count?",
                "options": ["28 rackets", "30 rackets", "32 rackets", "34 rackets"],
                "ans": 2,
                "hint": "Add the initial part and the incoming part: 18 + 14.",
                "exp": "18 + 14 = 32 rackets.",
                "sol": make_sol_html([
                    "Part 1 = 18 rackets.",
                    "Part 2 = 14 rackets.",
                    "Combine model: Whole = Part 1 + Part 2.",
                    "Whole = 18 + 14 = 32 rackets."
                ], "Combine models join parts together to compute the unknown whole.")
            },
            {
                "q": "In a compare word problem model, Bar A represents 48 students and Bar B represents 31 students. What is the difference between Bar A and Bar B?",
                "options": ["15 students", "17 students", "19 students", "21 students"],
                "ans": 1,
                "hint": "Subtract 31 from 48.",
                "exp": "48 − 31 = 17 students.",
                "sol": make_sol_html([
                    "Length of Bar A = 48.",
                    "Length of Bar B = 31.",
                    "Difference = Bar A − Bar B = 48 − 31 = 17."
                ], "Compare models calculate the gap or difference between two quantities.")
            },
            {
                "q": "In a change model, a school library started with 85 books. After students borrowed some books, 58 books remained on the shelf. How many books were borrowed?",
                "options": ["25 books", "27 books", "29 books", "31 books"],
                "ans": 1,
                "hint": "Subtract the remaining books from the starting amount: 85 − 58.",
                "exp": "85 − 58 = 27 books were borrowed.",
                "sol": make_sol_html([
                    "Initial quantity = 85.",
                    "Final quantity = 58.",
                    "Change (decrease) = Initial − Final = 85 − 58 = 27 books."
                ], "Change models track an increase or decrease from an initial state.")
            },
            {
                "q": "How does drawing a box or bar diagram help in solving multi-step word problems?",
                "options": ["It decorates the notebook page", "It visually clarifies which parts are known and whether to add or subtract to find the unknown", "It replaces the need for calculations", "It gives the answer immediately without arithmetic"],
                "ans": 1,
                "hint": "Think about how visualizing parts and wholes helps identify arithmetic operations.",
                "exp": "Bar diagrams translate words into spatial relationships, making it obvious whether addition or subtraction is needed.",
                "sol": make_sol_html([
                    "Word problems contain narrative descriptions that can feel overwhelming.",
                    "Bar diagrams abstract the story into parts and wholes.",
                    "Visualizing the unknown block clarifies the required arithmetic operation."
                ], "Bar modeling bridges language comprehension and mathematical calculation.")
            },
            {
                "q": "What is the ultimate goal of data handling in school mathematics?",
                "options": ["To memorize long lists of numbers", "To collect, organize, represent, and interpret information to understand patterns and make informed decisions", "To draw pictures instead of doing arithmetic", "To avoid answering questions"],
                "ans": 1,
                "hint": "Consider the full journey from collecting evidence to drawing valid conclusions.",
                "exp": "Data handling equips students with the scientific skill to collect evidence, spot patterns, and draw valid conclusions.",
                "sol": make_sol_html([
                    "Step 1: Frame thoughtful survey questions.",
                    "Step 2: Collect and record raw data accurately.",
                    "Step 3: Organize into tables, tallies, and pictographs.",
                    "Step 4: Interpret the findings to answer real-world questions."
                ], "Data handling turns raw numbers into meaningful insights for decision making.")
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(slides_part3)} slides for Part 3.")
    total_q = sum(len(s.get("quizzes", [])) for s in slides_part3)
    print(f"Total quizzes: {total_q}")
    for s in slides_part3:
        tw = len(s["title"].split())
        assert 1 <= tw <= 3, f"Title '{s['title']}' must be 1 to 3 words"
        assert len(s["quizzes"]) == 10, f"Slide {s['id']} must have 10 quizzes"
        for q in s["quizzes"]:
            assert len(q["options"]) == 4, f"Question must have 4 options: {q['q']}"
            assert 0 <= q["ans"] <= 3, f"Invalid answer index: {q['ans']}"
            assert "sol" in q and "<ol" in q["sol"], "Solution HTML must be valid"
    print("All Part 3 slide constraints validated successfully!")
