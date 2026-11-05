#!/usr/bin/env python3
"""
Generate Slides 17 to 20 (4 Mastery Challenges = 40 Quiz Questions)
for NCERT Class 5 Mathematics - Chapter 3: Angles as Turns
"""

slides_17_to_20 = [
    {
        "id": 17,
        "heading": "Challenge 1",
        "tagline": "Mastery Quiz: Turns, Rays, Vertices, and Angle Classifications",
        "color": "from-indigo-600 to-purple-700",
        "badge": "Mastery Challenge • Part 1",
        "audio_text": (
            "Welcome to Challenge 1! Test your foundational mastery of turns, rays, vertices, and angle classifications. "
            "Examine each question carefully, choose the correct answer, and review the detailed step-by-step solution modal for complete mathematical clarity."
        ),
        "quizzes": [
            {
                "question": "What is an angle formed by two rays meeting at a common point called?",
                "options": ["A Vertex and its Arms", "A Linear Segment", "A Perimeter", "A Circumference"],
                "correct": 0,
                "solution_html": "An angle is formed when two rays (arms) share a common endpoint called the vertex. The opening between the arms measures the amount of turning."
            },
            {
                "question": "How many degrees are in one complete full turn?",
                "options": ["360°", "180°", "90°", "270°"],
                "correct": 0,
                "solution_html": "One complete full turn around a circular pivot sweeps out 360°."
            },
            {
                "question": "A right angle is created by which fraction of a full turn?",
                "options": ["1/4 turn", "1/2 turn", "1/8 turn", "3/4 turn"],
                "correct": 0,
                "solution_html": "A right angle is formed by exactly a quarter turn (1/4 turn = 360° / 4 = 90°)."
            },
            {
                "question": "Which angle has an opening strictly less than a quarter turn (between 0° and 90°)?",
                "options": ["Acute angle", "Obtuse angle", "Right angle", "Straight angle"],
                "correct": 0,
                "solution_html": "An acute angle is defined as any angle whose turn is strictly less than 1/4 turn (< 90°)."
            },
            {
                "question": "An angle with an opening greater than 1/4 turn but less than 1/2 turn is classified as:",
                "options": ["Obtuse angle", "Acute angle", "Right angle", "Straight angle"],
                "correct": 0,
                "solution_html": "An obtuse angle lies strictly between 1/4 turn (90°) and 1/2 turn (180°)."
            },
            {
                "question": "A straight angle is created by two quarter turns. What is its measure in degrees?",
                "options": ["180°", "90°", "360°", "270°"],
                "correct": 0,
                "solution_html": "Two quarter turns equal 1/4 + 1/4 = 1/2 turn = 90° + 90° = 180°, forming a straight angle."
            },
            {
                "question": "If you double the length of the lines drawn for an angle, how does the angle measure change?",
                "options": ["It remains unchanged", "It doubles in size", "It is halved", "It becomes 90°"],
                "correct": 0,
                "solution_html": "The size of an angle depends purely on the degree of turning between its arms, not the physical length of the drawn line segments."
            },
            {
                "question": "Which of the following geometric corners is a classic right angle?",
                "options": ["The corner of a rectangular postcard", "The sharp tip of a sewing needle", "An open book lying almost flat", "A slice of 8-piece pizza"],
                "correct": 0,
                "solution_html": "Every corner of a rectangular postcard forms an exact perpendicular L-shape (90° right angle)."
            },
            {
                "question": "How many right angles combine to make a straight angle?",
                "options": ["2 right angles", "1 right angle", "3 right angles", "4 right angles"],
                "correct": 0,
                "solution_html": "Two 90° right angles combine to make 90° + 90° = 180°, which is a straight angle."
            },
            {
                "question": "How many right angles are needed to make one complete full turn?",
                "options": ["4 right angles", "2 right angles", "3 right angles", "8 right angles"],
                "correct": 0,
                "solution_html": "Four quarter turns (4 × 90° = 360°) complete one whole circular rotation."
            }
        ]
    },
    {
        "id": 18,
        "heading": "Challenge 2",
        "tagline": "Mastery Quiz: Paper Tools, Real-World Hinges, and Sector Testers",
        "color": "from-teal-600 to-emerald-700",
        "badge": "Mastery Challenge • Part 2",
        "audio_text": (
            "Welcome to Challenge 2! Test your practical understanding of paper folding testers, sector calculations, and real-world angle structures. "
            "Work through each scenario systematically and click on any question to inspect its complete solution."
        ),
        "quizzes": [
            {
                "question": "In an 8-part folded circular angle tester, what is the angle measure of each wedge?",
                "options": ["45° (1/8 turn)", "60° (1/6 turn)", "90° (1/4 turn)", "30° (1/12 turn)"],
                "correct": 0,
                "solution_html": "A full circle has 360°. Folding into 8 equal parts gives 360° / 8 = 45° (1/8 of a turn) per wedge."
            },
            {
                "question": "How many 1/8 sectors of an 8-part tester are required to match an obtuse angle of 135°?",
                "options": ["3 sectors (3 × 45° = 135°)", "2 sectors (90°)", "4 sectors (180°)", "1 sector (45°)"],
                "correct": 0,
                "solution_html": "Each sector is 45°. 3 sectors × 45° = 135°, which is an obtuse angle (3/8 turn)."
            },
            {
                "question": "In a 6-part tester with a straw pointer, what is the angle size of each sector?",
                "options": ["60° (1/6 turn)", "45° (1/8 turn)", "90° (1/4 turn)", "120° (1/3 turn)"],
                "correct": 0,
                "solution_html": "Dividing 360° into 6 equal parts gives 360° / 6 = 60° (1/6 of a full turn) per sector."
            },
            {
                "question": "In a regular hexagon, each interior angle measures 120°. How many 1/6 sectors is this?",
                "options": ["2 sectors (2 × 60° = 120°)", "1 sector (60°)", "3 sectors (180°)", "4 sectors (240°)"],
                "correct": 0,
                "solution_html": "Each sector in a 6-part tester is 60°. 120° / 60° = 2 sectors (2/6 = 1/3 of a full turn)."
            },
            {
                "question": "When an accordion paper fan is opened completely flat across the base, what angle is formed?",
                "options": ["Straight angle (180°)", "Right angle (90°)", "Acute angle (< 90°)", "Full turn (360°)"],
                "correct": 0,
                "solution_html": "Opening the fan flat across both opposite sides spreads it into a semicircle, forming a 180° straight angle."
            },
            {
                "question": "What angle is formed between two covers of an open laptop tilted back at 110°?",
                "options": ["Obtuse angle", "Acute angle", "Right angle", "Straight angle"],
                "correct": 0,
                "solution_html": "110° is greater than 90° and less than 180°, so it is classified as an obtuse angle."
            },
            {
                "question": "A pair of scissors is opened slightly so the blades form a 35° opening. What type of angle is this?",
                "options": ["Acute angle", "Right angle", "Obtuse angle", "Straight angle"],
                "correct": 0,
                "solution_html": "35° is strictly less than 90°, making it a sharp acute angle."
            },
            {
                "question": "If an angle tester made of two cardboard strips pinned at the centre is set to a right angle, which shape fits snugly into it?",
                "options": ["The square corner of a book cover", "A sharp pencil point", "A wide reclining beach chair", "A circular coin edge"],
                "correct": 0,
                "solution_html": "The square corner of a book cover is exactly 90°, so it fits perfectly against a right-angle tester."
            },
            {
                "question": "How many folds in half of a circular paper are needed to produce an 8-part tester?",
                "options": ["3 folds (2 → 4 → 8)", "2 folds (2 → 4)", "4 folds (2 → 4 → 8 → 16)", "1 fold (2)"],
                "correct": 0,
                "solution_html": "Fold 1 gives 2 parts; fold 2 gives 4 parts; fold 3 gives 8 equal parts."
            },
            {
                "question": "In an equilateral triangle, all three angles are equal to 60°. What type of angles are they?",
                "options": ["Acute angles", "Right angles", "Obtuse angles", "Straight angles"],
                "correct": 0,
                "solution_html": "Because 60° is less than 90°, all three angles of an equilateral triangle are acute angles."
            }
        ]
    },
    {
        "id": 19,
        "heading": "Challenge 3",
        "tagline": "Mastery Quiz: Fraction Turn Arithmetic and Clock Dial Angles",
        "color": "from-cyan-600 to-blue-700",
        "badge": "Mastery Challenge • Part 3",
        "audio_text": (
            "Welcome to Challenge 3! Dive into turn arithmetic, fractional additions, and clock-face angles. "
            "Calculate each rotational fraction methodically, submit your answer, and verify your logic with the step-by-step solution modal."
        ),
        "quizzes": [
            {
                "question": "What is the result of combining a 1/4 turn and a 1/8 turn in the same direction?",
                "options": ["3/8 turn (135°)", "2/8 turn (90°)", "1/2 turn (180°)", "5/8 turn (225°)"],
                "correct": 0,
                "solution_html": "1/4 turn = 2/8 turn. Adding 2/8 + 1/8 = 3/8 turn. In degrees: 90° + 45° = 135° (obtuse angle)."
            },
            {
                "question": "If you turn 1/2 of a turn and then turn back 1/8 of a turn, what fraction of a turn remains?",
                "options": ["3/8 turn", "1/4 turn", "1/8 turn", "5/8 turn"],
                "correct": 0,
                "solution_html": "1/2 turn = 4/8 turn. Subtracting the reverse turn: 4/8 - 1/8 = 3/8 turn."
            },
            {
                "question": "What is the angle between the hour and minute hands of a clock at 3:00?",
                "options": ["90° (Right angle)", "60° (Acute angle)", "120° (Obtuse angle)", "180° (Straight angle)"],
                "correct": 0,
                "solution_html": "At 3:00, the minute hand is at 12 and the hour hand is at 3, spanning 3 hours: 3 × 30° = 90° (a right angle)."
            },
            {
                "question": "What angle is formed between the hands of a clock at 6:00?",
                "options": ["180° (Straight angle)", "90° (Right angle)", "120° (Obtuse angle)", "360° (Full turn)"],
                "correct": 0,
                "solution_html": "At 6:00, the hands point directly in opposite directions (12 and 6), forming a 180° straight angle."
            },
            {
                "question": "How many degrees does the minute hand turn in 15 minutes?",
                "options": ["90° (1/4 turn)", "180° (1/2 turn)", "45° (1/8 turn)", "60° (1/6 turn)"],
                "correct": 0,
                "solution_html": "15 minutes out of 60 minutes is 15/60 = 1/4 of a full turn: 1/4 × 360° = 90°."
            },
            {
                "question": "How many degrees does the minute hand turn in 5 minutes?",
                "options": ["30° (1/12 turn)", "15°", "45°", "60°"],
                "correct": 0,
                "solution_html": "5 minutes out of 60 is 5/60 = 1/12 turn. 360° / 12 = 30°."
            },
            {
                "question": "At 5:00, what type of angle is formed between the clock hands?",
                "options": ["Obtuse angle (150°)", "Acute angle (60°)", "Right angle (90°)", "Straight angle (180°)"],
                "correct": 0,
                "solution_html": "At 5:00, the hands span 5 hour spaces: 5 × 30° = 150°. Since 150° is between 90° and 180°, it is an obtuse angle."
            },
            {
                "question": "What fraction of a full turn does the minute hand complete in 45 minutes?",
                "options": ["3/4 turn (270°)", "1/2 turn (180°)", "1/4 turn (90°)", "2/3 turn (240°)"],
                "correct": 0,
                "solution_html": "45 out of 60 minutes = 45/60 = 3/4 turn (270°)."
            },
            {
                "question": "What is 1/4 turn + 1/4 turn + 1/4 turn equal to?",
                "options": ["3/4 turn (270°)", "1/2 turn (180°)", "1 whole turn (360°)", "5/8 turn (225°)"],
                "correct": 0,
                "solution_html": "Adding three quarter turns gives 3 × (1/4) = 3/4 turn = 270°."
            },
            {
                "question": "At 1:00, what type of angle is formed between the clock hands?",
                "options": ["Acute angle (30°)", "Right angle (90°)", "Obtuse angle (120°)", "Straight angle (180°)"],
                "correct": 0,
                "solution_html": "At 1:00, the hands span 1 hour mark, which is 30°. Since 30° is less than 90°, it is an acute angle."
            }
        ]
    },
    {
        "id": 20,
        "heading": "Challenge 4",
        "tagline": "Mastery Quiz: Directional Navigation, Clockwise & Anti-Clockwise Rotations",
        "color": "from-emerald-600 to-teal-700",
        "badge": "Mastery Challenge • Part 4",
        "audio_text": (
            "Welcome to the final challenge! Test your advanced mastery of clockwise and anti-clockwise navigation across cardinal compass headings. "
            "Solve each directional puzzle, check your score, and celebrate your mastery of Angles as Turns!"
        ),
        "quizzes": [
            {
                "question": "Which direction of turning follows the natural path of clock hands?",
                "options": ["Clockwise", "Anti-clockwise", "Straight line", "Perpendicular"],
                "correct": 0,
                "solution_html": "Rotation that moves in the direction of clock hands (12 → 3 → 6 → 9) is called clockwise."
            },
            {
                "question": "In which direction do you turn a standard screw to tighten it into wood?",
                "options": ["Clockwise ('righty-tighty')", "Anti-clockwise ('lefty-loosey')", "Upward vertically", "Downward linearly"],
                "correct": 0,
                "solution_html": "Standard screw threads tighten when turned clockwise ('righty-tighty')."
            },
            {
                "question": "In which direction do you twist a jar lid to unscrew and loosen it?",
                "options": ["Anti-clockwise ('lefty-loosey')", "Clockwise ('righty-tighty')", "Straight upward without twisting", "Clockwise then push down"],
                "correct": 0,
                "solution_html": "Twisting anti-clockwise loosens the lid threads ('lefty-loosey')."
            },
            {
                "question": "You are facing North. You make a 1/4 turn clockwise. Which direction do you now face?",
                "options": ["East", "West", "South", "North"],
                "correct": 0,
                "solution_html": "Starting at North, a 1/4 turn clockwise (90° right) leads directly to East."
            },
            {
                "question": "You are facing North. You make a 1/4 turn anti-clockwise. Which direction do you now face?",
                "options": ["West", "East", "South", "North"],
                "correct": 0,
                "solution_html": "Starting at North, a 1/4 turn anti-clockwise (90° left) leads directly to West."
            },
            {
                "question": "You are facing East. You execute a 1/2 turn. Which direction do you face?",
                "options": ["West", "North", "South", "East"],
                "correct": 0,
                "solution_html": "A 1/2 turn (180°) points to the exact opposite direction: opposite of East is West."
            },
            {
                "question": "You are facing South. You make a 1/4 turn clockwise. Which direction do you face?",
                "options": ["West", "East", "North", "South"],
                "correct": 0,
                "solution_html": "From South, turning 1/4 turn clockwise (90° towards the clock's 9 position) leads to West."
            },
            {
                "question": "You are facing West. You make a 3/4 turn clockwise. Which direction do you face?",
                "options": ["South", "North", "East", "West"],
                "correct": 0,
                "solution_html": "From West: 1/4 turn CW = North; 2/4 turn CW = East; 3/4 turn CW = South."
            },
            {
                "question": "Starting at North, how many quarter turns clockwise are needed to face West?",
                "options": ["3 quarter turns (3/4 turn)", "1 quarter turn (1/4 turn)", "2 quarter turns (1/2 turn)", "4 quarter turns (1 full turn)"],
                "correct": 0,
                "solution_html": "From North: 1 quarter turn CW = East, 2 = South, 3 = West. Thus, 3 quarter turns (3/4 turn CW)."
            },
            {
                "question": "If you make a 1/4 turn clockwise and then immediately make a 1/4 turn anti-clockwise, what is your net turn?",
                "options": ["0 turns (Back to original facing direction)", "1/2 turn", "1/4 turn", "1 full turn"],
                "correct": 0,
                "solution_html": "A clockwise turn followed by an equal anti-clockwise turn cancels out: +1/4 - 1/4 = 0 net turn, returning you to the starting heading."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Authored Slides 17 to 20. Count: {len(slides_17_to_20)}")
    total_q = sum(len(s.get("quizzes", [])) for s in slides_17_to_20)
    print(f"Total Quiz Questions: {total_q}")

