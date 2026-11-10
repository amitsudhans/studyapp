#!/usr/bin/env python3
"""
Slide Data Generator for NCERT Class 3 Mathematics - Chapter 8: Fair Share
Part 2: Slides 9 to 16
Strictly 195 - 215 words per spoken text.
1-3 word titles.
No human names (Shabnam, Mukta, Raghav, etc. removed/generalized).
No teacher personas.
"""

import json

slides_part2 = [
    {
        "id": 9,
        "title": "Halves Logic Puzzles",
        "subtitle": "Solving deductive number riddles using clues about doubles and halves",
        "speech": (
            "Let us sharpen our mathematical deduction by playing an exciting detective game called 'Guess Who Am I'. "
            "In this puzzle game, target numbers hide behind clever numerical clues describing halves and doubles. "
            "Consider this riddle: 'I am a mystery number. If you double me, you get the number ten. Who am I?' "
            "To solve this riddle, we reason in reverse: since doubling the mystery number yields ten, the mystery number must be half of ten. "
            "Half of ten is five, so the answer is five! "
            "Let us try another puzzle: 'I am greater than six but less than ten. I am the double of four. Who am I?' "
            "Doubling four means two times four, which equals eight. Eight is indeed between six and ten, so the mystery number is eight! "
            "Now consider a two-step riddle: 'My half is three, and if you add two to me, what number do you reach?' "
            "If the half is three, the whole number is double of three, which is six. Adding two to six brings us to eight. "
            "Solving these riddles trains your brain to fluidly switch between doubling, halving, and comparative logic. "
            "Explore the interactive riddle solver to test mystery number cards, decode clues, and unlock secret target values."
        ),
        "checkpoints": [
            {
                "question": "A riddle says: 'If you double me, you get 12.' What is the number?",
                "options": ["4", "5", "6", "8"],
                "answer": 2,
                "hint": "Find half of 12: 12 ÷ 2.",
                "explanation": "Since 6 doubled is 6 × 2 = 12, the mystery number is 6."
            },
            {
                "question": "A number is half of 16. What is the double of that number?",
                "options": ["8", "12", "16", "20"],
                "answer": 2,
                "hint": "Halving and doubling are inverse operations that return you to the start.",
                "explanation": "Half of 16 is 8, and doubling 8 gives 16 right back."
            }
        ]
    },
    {
        "id": 10,
        "title": "Defining One Quarter",
        "subtitle": "Sharing equally among four people to discover the meaning of a quarter",
        "speech": (
            "What happens when a delicious round watermelon or a large flat paratha needs to be shared among four hungry friends instead of two? "
            "We can begin by cutting the whole paratha down the middle into two equal halves. "
            "Next, we take each half and cut it right down the middle again, creating four pieces in total. "
            "Because every piece is equal in size, shape, and area, each of these four pieces is called one quarter, or one-fourth of the whole. "
            "A quarter represents one part out of four equal parts that make up a complete whole. "
            "Notice how two quarters joined together form exactly one half of the paratha! "
            "If you place two quarter slices side by side on a plate, they match the semicircle of a half paratha perfectly. "
            "Adding a third quarter gives three-quarters, and bringing all four quarters together reconstructs the complete original whole. "
            "In arithmetic, finding a quarter of any quantity means dividing it into four equal shares: one divided by four. "
            "A quarter is smaller than a half, because a whole shared among four people gives smaller portions than when shared between two. "
            "Use the watermelon and paratha cutter to partition wholes into four equal quarters interactively."
        ),
        "checkpoints": [
            {
                "question": "When one whole object is shared equally among 4 people, what is each share called?",
                "options": ["One half", "One quarter (one-fourth)", "One third", "One double"],
                "answer": 1,
                "hint": "1 part out of 4 equal parts is a quarter.",
                "explanation": "When a whole is divided into four equal parts, each portion is called one quarter or one-fourth."
            },
            {
                "question": "How many quarters are needed to make one half of a paratha?",
                "options": ["1 quarter", "2 quarters", "3 quarters", "4 quarters"],
                "answer": 1,
                "hint": "Two quarters put together equal one half.",
                "explanation": "Two quarters equal one half (2/4 = 1/2)."
            }
        ]
    },
    {
        "id": 11,
        "title": "Quarter Geometric Partitions",
        "subtitle": "Dividing geometric shapes into four equal quarters using symmetry lines",
        "speech": (
            "Dividing geometric figures into four equal quarters requires careful alignment to guarantee that all four pieces have identical areas and shapes. "
            "Take a circle, like a tasty round chapati resting upon a cutting board. "
            "We draw one vertical line through the center and one horizontal line through the center, forming a clean perpendicular cross. "
            "These two perpendicular lines divide the circle into four identical quadrants, each representing one quarter of the circle's total area. "
            "Now consider a square sheet of craft paper. "
            "We can divide a square into quarters in several distinct geometric styles! "
            "We can fold it with two perpendicular center creases to produce four smaller equal squares. "
            "Alternatively, we can fold it along both diagonal corner-to-corner creases to create four identical triangles. "
            "We can even fold it into four tall vertical strips like a window shutter. "
            "In every case, as long as the four regions have the exact same surface area, each region is a genuine quarter. "
            "However, if a shape is sliced into four random, uneven pieces, those pieces are not quarters because fairness and equality are missing. "
            "Explore the geometric quarter canvas to test different cutting patterns and verify whether all four pieces represent true quarters."
        ),
        "checkpoints": [
            {
                "question": "Which shape can be formed by cutting a square into 4 quarters along both its diagonals?",
                "options": ["4 equal circles", "4 equal triangles", "4 unequal rectangles", "4 hexagons"],
                "answer": 1,
                "hint": "Cutting corner to corner through the center forms triangles.",
                "explanation": "Cutting a square along both diagonals produces 4 congruent triangles, each being one quarter."
            },
            {
                "question": "If an object is cut into 4 pieces of different sizes, can each piece be called a quarter?",
                "options": ["Yes, because there are 4 pieces", "No, because the pieces must be equal in size", "Yes, if they are colored", "No, only circles have quarters"],
                "answer": 1,
                "hint": "Quarters must be equal portions.",
                "explanation": "To be quarters, all 4 parts must be strictly equal in area and size."
            }
        ]
    },
    {
        "id": 12,
        "title": "Fractions of Collections",
        "subtitle": "Finding halves and quarters across sets of birds, flowers, and garlands",
        "speech": (
            "Just as we divide single objects into quarters, we can also find quarters and halves of countable collections of objects. "
            "Imagine looking into a garden tree where a flock of twelve colorful birds rests upon the branches. "
            "If an artist colors half of the birds in bright blue, how many birds are colored? "
            "To find half of twelve, we divide twelve by two: twelve divided by two equals six birds. "
            "Now suppose the artist decides to color only one quarter of the twelve birds in golden yellow. "
            "To find one quarter of a collection, we divide the total number into four equal groups: twelve divided by four equals three birds. "
            "Therefore, three birds represent one quarter of the flock, while six birds represent one half. "
            "Consider another example with sixteen marigold flowers ready to be tied into garlands. "
            "One quarter of sixteen is sixteen divided by four, which equals four flowers. "
            "One half of sixteen is sixteen divided by two, which equals eight flowers. "
            "Three quarters of sixteen would be three groups of four: four plus four plus four, equaling twelve flowers. "
            "Use the flock and garland collection workbench to group items into halves and quarters with instant visual counters."
        ),
        "checkpoints": [
            {
                "question": "A flock has 12 birds. How many birds make up one quarter of the flock?",
                "options": ["2 birds", "3 birds", "4 birds", "6 birds"],
                "answer": 1,
                "hint": "Divide 12 by 4: 12 ÷ 4.",
                "explanation": "One quarter of 12 is 12 ÷ 4 = 3 birds."
            },
            {
                "question": "Out of 16 flowers, how many flowers are in one half of the collection?",
                "options": ["4 flowers", "6 flowers", "8 flowers", "10 flowers"],
                "answer": 2,
                "hint": "Divide 16 by 2: 16 ÷ 2.",
                "explanation": "Half of 16 is 16 ÷ 2 = 8 flowers."
            }
        ]
    },
    {
        "id": 13,
        "title": "Fraction Circle Progressions",
        "subtitle": "Tracking the progressive accumulation of quarters from one-fourth to a complete whole",
        "speech": (
            "A segmented fraction circle offers a magnificent visual clockwork to watch fractional parts accumulate into a complete whole. "
            "Imagine a round disc divided cleanly into four equal quadrants, like the four quarters of an hour on a clock face. "
            "When we shade just one quadrant, we have one quarter of the circle. "
            "When we shade a second quadrant adjacent to the first, we have two quarters. "
            "Look closely at the disc: two shaded quarters together cover exactly one half of the entire circle! "
            "This gives us a vital mathematical equivalence: two quarters is exactly equal to one half. "
            "Next, when we shade a third quadrant, we have three quarters of the circle, leaving only one unshaded quarter remaining. "
            "Finally, when we shade the fourth quadrant, all four quarters are filled: four quarters make up one complete whole circle! "
            "This progression reveals how fractions build upon one another: one quarter, two quarters or one half, three quarters, and four quarters or one whole. "
            "Understanding this circular progression prepares you to read clock times, measure recipe cups, and calculate proportional quantities effortlessly. "
            "Interact with the circular fraction dial to step through each quadrant and watch the fraction labels transform dynamically."
        ),
        "checkpoints": [
            {
                "question": "Which fraction is exactly equal to 2 quarters of a circle?",
                "options": ["One quarter", "One half", "Three quarters", "The whole circle"],
                "answer": 1,
                "hint": "Two quarters cover half the circle.",
                "explanation": "Two quarters (2/4) cover exactly half of the circle (1/2)."
            },
            {
                "question": "How many quarters are required to form one complete whole circle?",
                "options": ["2 quarters", "3 quarters", "4 quarters", "5 quarters"],
                "answer": 2,
                "hint": "All four parts must be shaded.",
                "explanation": "Four quarters (4/4) combine to make one complete whole."
            }
        ]
    },
    {
        "id": 14,
        "title": "Three Quarters Anatomy",
        "subtitle": "Analyzing three-quarter fractions and calculating remaining complementary quarters",
        "speech": (
            "Now let us examine the fraction known as three-quarters in greater depth across diverse shapes, food portions, and real-world containers. "
            "When an object is split into four equal parts and three of those parts are selected, we describe that portion as three-quarters. "
            "Think of a tall glass measuring cup filled with delicious sweet mango lassi. "
            "If the cup is marked into four equal levels and lassi fills three levels, the cup is three-quarters full. "
            "How much of the cup remains empty? Exactly one quarter is empty! "
            "Because three quarters plus one quarter equals four quarters, or one complete whole, three-quarters and one-quarter are complementary fractions. "
            "We observe the same complementary relationship in geometric tiles and colorful flag designs. "
            "If a square tiled floor has three blue quarters and one white quarter, three-quarters is colored blue while one-quarter is white. "
            "Similarly, if a morning walker has completed three-quarters of a four-kilometer fitness track, they have traveled three kilometers and have one kilometer left to go. "
            "Recognizing three-quarters as 'one quarter away from a whole' strengthens your mental math agility. "
            "Use the three-quarters container lab on screen to fill glasses, color geometric tiles, and calculate remaining complementary fractions."
        ),
        "checkpoints": [
            {
                "question": "If a measuring cup is 3/4 full of juice, what fraction is empty?",
                "options": ["1/4", "1/2", "3/4", "The whole cup"],
                "answer": 0,
                "hint": "Four quarters make a whole: 4/4 - 3/4 = ?",
                "explanation": "1 - 3/4 = 1/4. Exactly one quarter of the cup remains empty."
            },
            {
                "question": "If a 20-kilometer bicycle route is 3/4 completed, how many kilometers have been traveled?",
                "options": ["5 km", "10 km", "15 km", "18 km"],
                "answer": 2,
                "hint": "One quarter is 20 ÷ 4 = 5 km. Three quarters is 3 × 5 km.",
                "explanation": "One quarter of 20 is 5 km. Three quarters is 3 × 5 = 15 km."
            }
        ]
    },
    {
        "id": 15,
        "title": "Grid Fraction Shading",
        "subtitle": "Representing halves and quarters creatively across multi-square grid matrices",
        "speech": (
            "A rectangular grid made of equal square cells provides a versatile canvas to express fractions with creative freedom. "
            "Consider a grid composed of sixteen identical square tiles arranged in four rows of four. "
            "How many tiles must you shade to represent exactly one half of this grid? "
            "Since half of sixteen is eight, you must shade any eight tiles out of the sixteen! "
            "You could shade the top two rows, or the left two columns, or even a checkerboard pattern of alternating squares. "
            "As long as exactly eight squares are colored, the shaded portion represents one half of the grid. "
            "Now, how many squares must you shade to represent one quarter of the sixteen-cell grid? "
            "To find one quarter of sixteen, we divide sixteen by four: sixteen divided by four equals four squares. "
            "Shading any four squares—whether clustered in a single row or scattered diagonally—represents one quarter. "
            "To represent three-quarters, we shade three times four, which equals twelve squares out of sixteen. "
            "Grid shading proves that a fraction describes the total proportional quantity, regardless of whether the shaded squares are grouped together or separated. "
            "Experiment with the interactive grid painter to shade cells and verify fractional proportions dynamically."
        ),
        "checkpoints": [
            {
                "question": "How many cells must be shaded in a 16-cell grid to represent one half?",
                "options": ["4 cells", "6 cells", "8 cells", "10 cells"],
                "answer": 2,
                "hint": "Find half of 16: 16 ÷ 2.",
                "explanation": "Half of 16 cells is 16 ÷ 2 = 8 cells."
            },
            {
                "question": "How many cells must be shaded in a 16-cell grid to represent one quarter?",
                "options": ["2 cells", "4 cells", "6 cells", "8 cells"],
                "answer": 1,
                "hint": "Find one quarter of 16: 16 ÷ 4.",
                "explanation": "One quarter of 16 cells is 16 ÷ 4 = 4 cells."
            }
        ]
    },
    {
        "id": 16,
        "title": "Rebuilding Complete Wholes",
        "subtitle": "Assembling fractional puzzle pieces to reconstruct complete geometric wholes",
        "speech": (
            "We conclude our conceptual exploration with a fascinating reverse puzzle challenge: rebuilding complete wholes from fractional puzzle pieces. "
            "Suppose you are handed a single triangular puzzle piece, and a clue card states: 'This piece is one quarter of a complete shape.' "
            "How many identical pieces are needed to reconstruct the complete whole? "
            "Since one quarter means one part out of four, you need exactly four identical pieces to build the full shape! "
            "By arranging the four triangles together edge to edge, you can construct a large square, a tall rectangle, or even a large triangle. "
            "What if you are handed a rectangular block with the clue: 'This block represents one half of the whole'? "
            "Since one half means one part out of two, you need exactly two identical blocks to restore the original whole. "
            "This reverse assembly reinforces the core definition of fractions: denominators tell us how many equal pieces create one whole. "
            "Two halves make a whole, and four quarters make a whole. "
            "Recognizing how fractional parts join together empowers you to solve advanced fraction problems with total clarity and confidence. "
            "Interact with the fraction puzzle workbench to snap pieces together and reconstruct complete geometric wholes."
        ),
        "checkpoints": [
            {
                "question": "If 1 puzzle piece represents 1/4 of a shape, how many such pieces are needed to make the whole shape?",
                "options": ["2 pieces", "3 pieces", "4 pieces", "5 pieces"],
                "answer": 2,
                "hint": "Four quarters make one whole.",
                "explanation": "Four quarters make a whole, so 4 identical pieces are needed."
            },
            {
                "question": "If 1 piece is 1/2 of a whole shape, how many pieces make the complete whole?",
                "options": ["2 pieces", "3 pieces", "4 pieces", "6 pieces"],
                "answer": 0,
                "hint": "Two halves make a whole.",
                "explanation": "Two halves make a complete whole, so exactly 2 pieces are needed."
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
