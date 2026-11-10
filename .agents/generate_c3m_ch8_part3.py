#!/usr/bin/env python3
"""
Slide Data Generator for NCERT Class 3 Mathematics - Chapter 8: Fair Share
Part 3: Slides 17 to 20 (Mastery Challenges 1 to 4)
Each Challenge contains 10 rigorous, curriculum-aligned questions (40 questions total).
Zero human character names.
Includes options, hint, explanation, and 3-step structured solutions.
"""

challenges = [
    {
        "id": 17,
        "title": "Challenge 1",
        "subtitle": "Mastery Challenge on Halves, Fair Sharing & Paper Folding Symmetry",
        "questions": [
            {
                "question": "A round paratha is folded exactly across its center. What fraction of the paratha is each folded part?",
                "options": ["One quarter", "One half", "One third", "Two wholes"],
                "answer": 1,
                "hint": "Folding a whole into 2 equal parts creates halves.",
                "explanation": "When an object is divided into 2 equal parts, each part is called one half.",
                "solution_steps": [
                    "Step 1: Identify that the whole paratha is split into 2 equal parts.",
                    "Step 2: Understand that 1 part out of 2 equal parts is 1/2.",
                    "Step 3: Therefore, each piece represents one half."
                ]
            },
            {
                "question": "A chocolate bar has 12 equal squares. How many squares make up half of the chocolate bar?",
                "options": ["4 squares", "5 squares", "6 squares", "8 squares"],
                "answer": 2,
                "hint": "Divide 12 by 2: 12 ÷ 2.",
                "explanation": "Half of 12 is 12 ÷ 2 = 6 squares.",
                "solution_steps": [
                    "Step 1: Total squares in the chocolate bar = 12.",
                    "Step 2: Divide by 2 to find one half: 12 ÷ 2.",
                    "Step 3: 12 ÷ 2 = 6. Exactly 6 squares make up one half."
                ]
            },
            {
                "question": "Which of these cuts creates two equal halves in a square sheet of paper?",
                "options": ["A corner-to-corner diagonal fold", "A cut 1 cm from the left edge", "A jagged wavy scratch", "A tiny triangular corner cut"],
                "answer": 0,
                "hint": "A diagonal cut through a square splits it into two equal triangles.",
                "explanation": "Cutting a square along its diagonal splits it into two congruent triangles of identical area.",
                "solution_steps": [
                    "Step 1: Observe that a diagonal connects opposite corners through the center.",
                    "Step 2: Folding along the diagonal makes the two triangles overlap perfectly.",
                    "Step 3: Since both triangles have equal areas, each is one half."
                ]
            },
            {
                "question": "If a symmetrical kite drawing has 4 ribbons on its left tail, how many ribbons must be on the right tail?",
                "options": ["2 ribbons", "3 ribbons", "4 ribbons", "8 ribbons"],
                "answer": 2,
                "hint": "Symmetry means both halves are exact mirror reflections.",
                "explanation": "In a symmetrical drawing, both halves have identical counts and shapes. The right tail must have 4 ribbons.",
                "solution_steps": [
                    "Step 1: Identify that the kite is bilaterally symmetrical.",
                    "Step 2: Mirror symmetry requires identical features on both sides.",
                    "Step 3: 4 ribbons on the left requires 4 ribbons on the right."
                ]
            },
            {
                "question": "A chikki bar has 6 equal pieces. If 3 pieces are eaten, what fraction of the chikki is eaten?",
                "options": ["One quarter", "One half", "One third", "Three quarters"],
                "answer": 1,
                "hint": "Compare 3 pieces to the total 6 pieces: 3/6.",
                "explanation": "3 pieces out of 6 is 3/6, which simplifies to exactly one half.",
                "solution_steps": [
                    "Step 1: Total pieces = 6; pieces eaten = 3.",
                    "Step 2: Check the ratio: 3 is half of 6.",
                    "Step 3: Therefore, one half of the chikki has been eaten."
                ]
            },
            {
                "question": "A basket holds 14 ripe mangoes. If they are shared equally between 2 children, how many does each child get?",
                "options": ["6 mangoes", "7 mangoes", "8 mangoes", "9 mangoes"],
                "answer": 1,
                "hint": "Divide 14 by 2: 14 ÷ 2.",
                "explanation": "14 shared equally between 2 children gives 14 ÷ 2 = 7 mangoes each.",
                "solution_steps": [
                    "Step 1: Total mangoes = 14.",
                    "Step 2: Number of equal shares = 2.",
                    "Step 3: Compute 14 ÷ 2 = 7 mangoes per share."
                ]
            },
            {
                "question": "Which of the following is NOT a line of symmetry that divides a square into equal halves?",
                "options": ["Vertical center line", "Horizontal center line", "Diagonal line", "A line parallel to an edge at 1/4 width"],
                "answer": 3,
                "hint": "A cut at 1/4 width creates unequal portions (1/4 and 3/4).",
                "explanation": "A line at 1/4 width divides the square into 1/4 and 3/4, which are unequal parts and not halves.",
                "solution_steps": [
                    "Step 1: Test center lines: vertical, horizontal, and diagonal all pass through center.",
                    "Step 2: A cut at 1/4 width splits the square into 25% and 75%.",
                    "Step 3: Unequal parts cannot be halves. Option D is correct."
                ]
            },
            {
                "question": "Two friends share a paratha, but one piece is three times bigger than the other. Is this a fair share of halves?",
                "options": ["Yes, because there are 2 pieces", "No, because the pieces are unequal in size", "Yes, if both friends agree", "No, because parathas cannot be cut"],
                "answer": 1,
                "hint": "Halves must be equal in area and size.",
                "explanation": "Halves must be strictly equal. If one piece is bigger, they are not halves and the share is unfair.",
                "solution_steps": [
                    "Step 1: Recall the definition of one half: one of two strictly equal parts.",
                    "Step 2: If one piece is three times larger, the pieces are unequal.",
                    "Step 3: Therefore, it is not a fair share of halves."
                ]
            },
            {
                "question": "How many halves make up one complete whole?",
                "options": ["1 half", "2 halves", "3 halves", "4 halves"],
                "answer": 1,
                "hint": "1/2 + 1/2 = 1.",
                "explanation": "Two halves combine to make one complete whole (1/2 + 1/2 = 1).",
                "solution_steps": [
                    "Step 1: Understand that a half is 1 part out of 2.",
                    "Step 2: Combining both equal parts gives 2/2.",
                    "Step 3: 2/2 = 1 complete whole."
                ]
            },
            {
                "question": "If half of a circular cake has 5 cherries, how many cherries are on the entire cake?",
                "options": ["8 cherries", "10 cherries", "12 cherries", "15 cherries"],
                "answer": 1,
                "hint": "Double the cherries on half the cake: 5 × 2.",
                "explanation": "If half has 5 cherries, the whole cake has 5 × 2 = 10 cherries.",
                "solution_steps": [
                    "Step 1: Cherries on one half = 5.",
                    "Step 2: A whole contains 2 halves: 5 + 5 or 5 × 2.",
                    "Step 3: 5 × 2 = 10 cherries in total."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "subtitle": "Mastery Challenge on Halves, Doubles & Number Line Relationships",
        "questions": [
            {
                "question": "If 6 is half of a number, what is that number?",
                "options": ["10", "12", "14", "16"],
                "answer": 1,
                "hint": "Double 6: 6 × 2.",
                "explanation": "If 6 is half, the whole number is 6 × 2 = 12.",
                "solution_steps": [
                    "Step 1: Given: half = 6.",
                    "Step 2: To find the whole, double the half: 6 × 2.",
                    "Step 3: 6 × 2 = 12."
                ]
            },
            {
                "question": "What is half of 18?",
                "options": ["7", "8", "9", "10"],
                "answer": 2,
                "hint": "Divide 18 by 2: 18 ÷ 2.",
                "explanation": "18 ÷ 2 = 9.",
                "solution_steps": [
                    "Step 1: Start with total = 18.",
                    "Step 2: Divide by 2: 18 ÷ 2.",
                    "Step 3: 18 ÷ 2 = 9."
                ]
            },
            {
                "question": "On a number line from 0 to 14, what number marks the exact halfway point?",
                "options": ["6", "7", "8", "9"],
                "answer": 1,
                "hint": "Find half of 14: 14 ÷ 2.",
                "explanation": "Half of 14 is 7, so 7 is the exact midpoint between 0 and 14.",
                "solution_steps": [
                    "Step 1: Total distance = 14 units.",
                    "Step 2: Halfway distance = 14 ÷ 2.",
                    "Step 3: 14 ÷ 2 = 7."
                ]
            },
            {
                "question": "A riddle states: 'I am the double of 5, and if you take half of me, you get 5.' What number am I?",
                "options": ["8", "10", "12", "15"],
                "answer": 1,
                "hint": "Double of 5 is 5 × 2.",
                "explanation": "Double of 5 is 10, and half of 10 is 5.",
                "solution_steps": [
                    "Step 1: Double the number 5: 5 × 2 = 10.",
                    "Step 2: Check half: half of 10 is 5.",
                    "Step 3: The number is 10."
                ]
            },
            {
                "question": "If you have 8 marbles and your friend has double your marbles, how many marbles does your friend have?",
                "options": ["12 marbles", "14 marbles", "16 marbles", "18 marbles"],
                "answer": 2,
                "hint": "Double 8: 8 × 2.",
                "explanation": "8 × 2 = 16 marbles.",
                "solution_steps": [
                    "Step 1: Initial marbles = 8.",
                    "Step 2: Double the quantity: 8 × 2.",
                    "Step 3: 8 × 2 = 16 marbles."
                ]
            },
            {
                "question": "Which statement correctly describes the relationship between 8 and 16?",
                "options": ["8 is double of 16", "8 is half of 16, and 16 is double of 8", "16 is half of 8", "8 and 16 have no proportional relation"],
                "answer": 1,
                "hint": "8 is half of 16; 16 is double of 8.",
                "explanation": "8 is half of 16 (16 ÷ 2 = 8), and 16 is double of 8 (8 × 2 = 16).",
                "solution_steps": [
                    "Step 1: Check halving: 16 ÷ 2 = 8.",
                    "Step 2: Check doubling: 8 × 2 = 16.",
                    "Step 3: Both statements in Option B are mathematically true."
                ]
            },
            {
                "question": "A runner completes a 12-kilometer race. At what kilometer mark was the runner exactly halfway?",
                "options": ["4 km", "5 km", "6 km", "7 km"],
                "answer": 2,
                "hint": "Calculate 12 ÷ 2.",
                "explanation": "Half of 12 km is 12 ÷ 2 = 6 km.",
                "solution_steps": [
                    "Step 1: Total race distance = 12 km.",
                    "Step 2: Halfway point = 12 ÷ 2.",
                    "Step 3: 12 ÷ 2 = 6 km."
                ]
            },
            {
                "question": "A riddle asks: 'I am greater than 10 but less than 15. I am double of 6.' Who am I?",
                "options": ["11", "12", "13", "14"],
                "answer": 1,
                "hint": "Calculate 6 × 2 and verify it is between 10 and 15.",
                "explanation": "Double of 6 is 12, which lies between 10 and 15.",
                "solution_steps": [
                    "Step 1: Double 6: 6 × 2 = 12.",
                    "Step 2: Check range: 10 < 12 < 15 (true).",
                    "Step 3: The mystery number is 12."
                ]
            },
            {
                "question": "If half of a group of buttons is 9, how many buttons are in the entire group?",
                "options": ["16 buttons", "18 buttons", "20 buttons", "22 buttons"],
                "answer": 1,
                "hint": "Double 9: 9 × 2.",
                "explanation": "9 × 2 = 18 buttons in the whole group.",
                "solution_steps": [
                    "Step 1: Half of group = 9.",
                    "Step 2: Whole group = 9 × 2.",
                    "Step 3: 9 × 2 = 18 buttons."
                ]
            },
            {
                "question": "What is the result when you take half of 20 and then double that result?",
                "options": ["10", "15", "20", "40"],
                "answer": 2,
                "hint": "Halving then doubling returns you to the original number.",
                "explanation": "Half of 20 is 10. Doubling 10 gives 20 right back.",
                "solution_steps": [
                    "Step 1: Half of 20 = 20 ÷ 2 = 10.",
                    "Step 2: Double of 10 = 10 × 2 = 20.",
                    "Step 3: The final result is 20."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "subtitle": "Mastery Challenge on Quarters, Circles & Fractions of Collections",
        "questions": [
            {
                "question": "When an apple is cut into 4 equal pieces, what is each piece called?",
                "options": ["One half", "One quarter (one-fourth)", "One third", "Two quarters"],
                "answer": 1,
                "hint": "1 out of 4 equal parts is a quarter.",
                "explanation": "Each of the 4 equal parts is called one quarter or one-fourth.",
                "solution_steps": [
                    "Step 1: Total equal parts = 4.",
                    "Step 2: 1 part out of 4 is written as 1/4.",
                    "Step 3: In words, 1/4 is called one quarter."
                ]
            },
            {
                "question": "How many quarters are in one half of a watermelon?",
                "options": ["1 quarter", "2 quarters", "3 quarters", "4 quarters"],
                "answer": 1,
                "hint": "2/4 is equal to 1/2.",
                "explanation": "Two quarters make one half (2/4 = 1/2).",
                "solution_steps": [
                    "Step 1: Understand that 1 whole = 4 quarters.",
                    "Step 2: Half of 4 quarters is 4 ÷ 2 = 2 quarters.",
                    "Step 3: Therefore, one half equals 2 quarters."
                ]
            },
            {
                "question": "A flock has 20 birds. How many birds make up one quarter of the flock?",
                "options": ["4 birds", "5 birds", "6 birds", "10 birds"],
                "answer": 1,
                "hint": "Divide 20 by 4: 20 ÷ 4.",
                "explanation": "One quarter of 20 is 20 ÷ 4 = 5 birds.",
                "solution_steps": [
                    "Step 1: Total birds = 20.",
                    "Step 2: One quarter means dividing into 4 equal groups: 20 ÷ 4.",
                    "Step 3: 20 ÷ 4 = 5 birds."
                ]
            },
            {
                "question": "Out of 20 birds, how many birds make up one half of the flock?",
                "options": ["5 birds", "8 birds", "10 birds", "12 birds"],
                "answer": 2,
                "hint": "Divide 20 by 2: 20 ÷ 2.",
                "explanation": "One half of 20 is 20 ÷ 2 = 10 birds.",
                "solution_steps": [
                    "Step 1: Total birds = 20.",
                    "Step 2: One half means dividing into 2 equal groups: 20 ÷ 2.",
                    "Step 3: 20 ÷ 2 = 10 birds."
                ]
            },
            {
                "question": "A fraction circle has 4 equal quadrants. If 3 quadrants are colored, what fraction is colored?",
                "options": ["1/4", "1/2", "3/4", "4/4"],
                "answer": 2,
                "hint": "3 parts out of 4 are colored.",
                "explanation": "Three shaded quadrants out of four make three-quarters (3/4).",
                "solution_steps": [
                    "Step 1: Shaded parts = 3.",
                    "Step 2: Total equal parts = 4.",
                    "Step 3: The fraction is 3/4 (three-quarters)."
                ]
            },
            {
                "question": "How many quarters make up one complete whole circle?",
                "options": ["2 quarters", "3 quarters", "4 quarters", "8 quarters"],
                "answer": 2,
                "hint": "4/4 = 1.",
                "explanation": "Four quarters equal one complete whole (4/4 = 1).",
                "solution_steps": [
                    "Step 1: 1 quarter = 1/4.",
                    "Step 2: To make 1 whole, all 4 parts must be combined: 4 × 1/4 = 4/4.",
                    "Step 3: 4 quarters make 1 whole."
                ]
            },
            {
                "question": "A garland maker has 24 marigold flowers. If one quarter of them are tied, how many are tied?",
                "options": ["4 flowers", "6 flowers", "8 flowers", "12 flowers"],
                "answer": 1,
                "hint": "Divide 24 by 4: 24 ÷ 4.",
                "explanation": "24 ÷ 4 = 6 flowers.",
                "solution_steps": [
                    "Step 1: Total flowers = 24.",
                    "Step 2: Divide by 4: 24 ÷ 4.",
                    "Step 3: 24 ÷ 4 = 6 flowers tied."
                ]
            },
            {
                "question": "Which fraction is larger: one half or one quarter?",
                "options": ["One half is larger", "One quarter is larger", "Both are equal", "Cannot be determined"],
                "answer": 0,
                "hint": "Sharing between 2 people gives larger pieces than sharing among 4.",
                "explanation": "One half (1/2) is larger than one quarter (1/4). In fact, 1/2 is double 1/4.",
                "solution_steps": [
                    "Step 1: Compare shares: 1/2 is 2 quarters.",
                    "Step 2: 2 quarters is greater than 1 quarter.",
                    "Step 3: Therefore, one half is larger."
                ]
            },
            {
                "question": "If a pizza has 8 slices, how many slices make up one quarter of the pizza?",
                "options": ["1 slice", "2 slices", "3 slices", "4 slices"],
                "answer": 1,
                "hint": "Divide 8 slices by 4: 8 ÷ 4.",
                "explanation": "8 ÷ 4 = 2 slices make one quarter.",
                "solution_steps": [
                    "Step 1: Total slices = 8.",
                    "Step 2: One quarter = 8 ÷ 4.",
                    "Step 3: 8 ÷ 4 = 2 slices."
                ]
            },
            {
                "question": "If you color 2 quadrants of a 4-quadrant circle, what fraction of the circle is UNCOLORED?",
                "options": ["1/4", "1/2", "3/4", "0"],
                "answer": 1,
                "hint": "4 quadrants minus 2 leaves 2 quadrants uncolored.",
                "explanation": "2 quadrants remain uncolored out of 4, which is 2/4 = 1/2.",
                "solution_steps": [
                    "Step 1: Total quadrants = 4; colored = 2.",
                    "Step 2: Uncolored quadrants = 4 - 2 = 2.",
                    "Step 3: 2 out of 4 is 2/4 = 1/2."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "subtitle": "Mastery Challenge on Three-Quarters, Grid Shading & Rebuilding Wholes",
        "questions": [
            {
                "question": "A water bottle is 3/4 full. What fraction of the bottle is empty?",
                "options": ["1/4", "1/2", "3/4", "Empty"],
                "answer": 0,
                "hint": "1 whole minus 3/4 equals 1/4.",
                "explanation": "1 - 3/4 = 1/4. Exactly one quarter of the bottle is empty.",
                "solution_steps": [
                    "Step 1: A whole bottle = 4/4.",
                    "Step 2: Subtract the full portion: 4/4 - 3/4.",
                    "Step 3: 4/4 - 3/4 = 1/4 empty."
                ]
            },
            {
                "question": "How many cells must be shaded in a 16-cell grid to represent 3/4 of the grid?",
                "options": ["8 cells", "10 cells", "12 cells", "14 cells"],
                "answer": 2,
                "hint": "1/4 of 16 is 4. Multiply 4 by 3.",
                "explanation": "1/4 of 16 is 4. Therefore, 3/4 of 16 is 3 × 4 = 12 cells.",
                "solution_steps": [
                    "Step 1: Find one quarter of 16: 16 ÷ 4 = 4 cells.",
                    "Step 2: Multiply by 3 for three-quarters: 3 × 4.",
                    "Step 3: 3 × 4 = 12 cells."
                ]
            },
            {
                "question": "If 1 puzzle block represents 1/4 of a square, how many such blocks are needed to assemble the complete square?",
                "options": ["2 blocks", "3 blocks", "4 blocks", "6 blocks"],
                "answer": 2,
                "hint": "Four quarters make one whole.",
                "explanation": "Since each block is 1/4, exactly 4 blocks make 4/4 = 1 complete square.",
                "solution_steps": [
                    "Step 1: Value of 1 block = 1/4.",
                    "Step 2: Number of 1/4 pieces to make 1 whole = 4.",
                    "Step 3: Exactly 4 blocks are required."
                ]
            },
            {
                "question": "In an 8-cell strip, 4 cells are shaded blue. What fraction of the strip is shaded blue?",
                "options": ["1/4", "1/2", "3/4", "All"],
                "answer": 1,
                "hint": "Compare 4 to 8: 4/8.",
                "explanation": "4 out of 8 cells is 4/8, which equals 1/2 (one half).",
                "solution_steps": [
                    "Step 1: Shaded cells = 4; total cells = 8.",
                    "Step 2: Fraction = 4/8.",
                    "Step 3: Simplify: 4/8 = 1/2."
                ]
            },
            {
                "question": "A cyclist has to travel 24 kilometers. If the cyclist has traveled 3/4 of the journey, how many kilometers are completed?",
                "options": ["12 km", "16 km", "18 km", "20 km"],
                "answer": 2,
                "hint": "One quarter is 24 ÷ 4 = 6 km. Multiply 6 by 3.",
                "explanation": "24 ÷ 4 = 6 km per quarter. 3 × 6 = 18 km.",
                "solution_steps": [
                    "Step 1: Find 1/4 of 24 km: 24 ÷ 4 = 6 km.",
                    "Step 2: Find 3/4 by multiplying by 3: 3 × 6 km.",
                    "Step 3: 3 × 6 = 18 km."
                ]
            },
            {
                "question": "If 2 puzzle blocks each represent 1/2 of a circle, what do they form when joined together?",
                "options": ["One quarter of a circle", "One complete whole circle", "Two circles", "Half a circle"],
                "answer": 1,
                "hint": "1/2 + 1/2 = 1 whole.",
                "explanation": "Two halves make 1 complete whole circle.",
                "solution_steps": [
                    "Step 1: Two pieces each of size 1/2.",
                    "Step 2: Add them: 1/2 + 1/2 = 2/2.",
                    "Step 3: 2/2 = 1 complete whole circle."
                ]
            },
            {
                "question": "A recipe calls for 3/4 cup of milk. If you only add 1/4 cup of milk, how much more milk is needed?",
                "options": ["1/4 cup", "1/2 cup (2/4 cup)", "3/4 cup", "1 full cup"],
                "answer": 1,
                "hint": "3/4 minus 1/4 equals 2/4, which simplifies to 1/2.",
                "explanation": "3/4 - 1/4 = 2/4 cup, which equals 1/2 cup.",
                "solution_steps": [
                    "Step 1: Target amount = 3/4 cup.",
                    "Step 2: Subtract added amount: 3/4 - 1/4 = 2/4 cup.",
                    "Step 3: 2/4 simplifies to 1/2 cup."
                ]
            },
            {
                "question": "In a box of 32 crayons, one quarter are red. How many red crayons are in the box?",
                "options": ["6 crayons", "8 crayons", "12 crayons", "16 crayons"],
                "answer": 1,
                "hint": "Divide 32 by 4: 32 ÷ 4.",
                "explanation": "One quarter of 32 is 32 ÷ 4 = 8 red crayons.",
                "solution_steps": [
                    "Step 1: Total crayons = 32.",
                    "Step 2: Divide by 4: 32 ÷ 4.",
                    "Step 3: 32 ÷ 4 = 8 red crayons."
                ]
            },
            {
                "question": "Which of these fractions is the largest?",
                "options": ["1/4", "2/4", "3/4", "All are equal"],
                "answer": 2,
                "hint": "Compare numerators: 1 < 2 < 3.",
                "explanation": "3/4 is greater than 2/4 (which is 1/2) and 1/4.",
                "solution_steps": [
                    "Step 1: Compare fractions with the same denominator: 1/4, 2/4, 3/4.",
                    "Step 2: Since 3 > 2 > 1, 3/4 has the largest numerator.",
                    "Step 3: Therefore, 3/4 is the largest fraction."
                ]
            },
            {
                "question": "If you have 3 quarters of a rupee (75 paise), how many more quarters do you need to make one full rupee (100 paise)?",
                "options": ["1 quarter (25 paise)", "2 quarters (50 paise)", "3 quarters (75 paise)", "0 quarters"],
                "answer": 0,
                "hint": "4 quarters make 1 whole. 4 - 3 = 1.",
                "explanation": "You need 1 more quarter (25 paise) to complete 4 quarters (1 whole rupee).",
                "solution_steps": [
                    "Step 1: 1 whole rupee = 4 quarters (100 paise).",
                    "Step 2: Current amount = 3 quarters (75 paise).",
                    "Step 3: 4 - 3 = 1 quarter (25 paise) needed."
                ]
            }
        ]
    }
]

if __name__ == "__main__":
    for c in challenges:
        print(f"Slide {c['id']}: '{c['title']}' ({len(c['title'].split())} words) -> Questions: {len(c['questions'])}")
        assert len(c["title"].split()) <= 3
        assert len(c["questions"]) == 10
        for i, q in enumerate(c["questions"]):
            assert len(q["options"]) == 4, f"Slide {c['id']} Q{i+1} options count != 4"
            assert 0 <= q["answer"] <= 3, f"Slide {c['id']} Q{i+1} answer out of range"
            assert "hint" in q and len(q["hint"]) > 0
            assert "explanation" in q and len(q["explanation"]) > 0
            assert "solution_steps" in q and len(q["solution_steps"]) == 3
    print("Part 3 (Challenges 1-4) verified successfully!")
