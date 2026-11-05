# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 5: Sharing and Measuring
Part 3: Slides 17 to 20 (Mastery Challenges 1 to 4, Questions 1 to 40)
Each question includes id, q, options, ans, hint, exp, and solution_steps.
Zero human names. Clean Unicode throughout.
"""

def make_sol_html(steps, note=None):
    items = "".join([f"<li class='text-xs text-slate-300 leading-relaxed'><span class='font-semibold text-amber-400'>Step {idx+1}:</span> {step}</li>" for idx, step in enumerate(steps)])
    note_html = f"<div class='mt-2 p-2 rounded bg-amber-500/10 border border-amber-500/20 text-[11px] text-amber-300'><strong>Note:</strong> {note}</div>" if note else ""
    return f"<ol class='space-y-1.5 list-none pl-0'>{items}</ol>{note_html}"

quiz_q1_to_10 = [
    {
        "id": 1,
        "q": "When a single sheet of paper is folded into two strictly equal pieces, what fraction does each piece represent?",
        "options": ["1/2", "1/4", "2/1", "1/3"],
        "ans": 0,
        "hint": "Think about splitting into two equal parts.",
        "exp": "Each equal piece is one out of two total parts, written as 1/2.",
        "sol": make_sol_html([
            "A whole sheet represents 1 complete unit.",
            "Dividing it into 2 equal parts gives each part a value of 1 divided by 2.",
            "In fractional notation, this is written as 1/2 (one half)."
        ])
    },
    {
        "id": 2,
        "q": "How many quarters (1/4 pieces) of a rectangular sheet are needed to equal one half (1/2)?",
        "options": ["2 quarters", "4 quarters", "1 quarter", "3 quarters"],
        "ans": 0,
        "hint": "Add 1/4 + 1/4.",
        "exp": "Two quarters equal 2/4, which simplifies to 1/2.",
        "sol": make_sol_html([
            "Each quarter represents 1/4 of the sheet.",
            "Adding two quarters gives 1/4 + 1/4 = 2/4.",
            "Dividing numerator and denominator by 2 gives 2/4 = 1/2.",
            "Therefore, exactly 2 quarters equal one half."
        ])
    },
    {
        "id": 3,
        "q": "What is the mathematical term for the bottom number in a fraction that shows the total number of equal parts?",
        "options": ["Denominator", "Numerator", "Quotient", "Divisor"],
        "ans": 0,
        "hint": "The top number is the numerator, the bottom number is...",
        "exp": "The denominator indicates into how many equal parts the whole is partitioned.",
        "sol": make_sol_html([
            "A fraction is written as Numerator / Denominator.",
            "The top number (Numerator) counts the parts considered.",
            "The bottom number (Denominator) denotes the total number of equal parts in the whole."
        ])
    },
    {
        "id": 4,
        "q": "If a rectangle is folded diagonally from one corner to the opposite corner, what shapes are formed?",
        "options": ["Two congruent right-angled triangles", "Two squares", "Two semicircles", "Four triangles"],
        "ans": 0,
        "hint": "A diagonal cut through a rectangle splits it into two equal triangular halves.",
        "exp": "The diagonal crease cuts the rectangle into two identical right-angled triangles of equal area.",
        "sol": make_sol_html([
            "Draw a diagonal line across opposite vertices of a rectangle.",
            "The line divides the interior into two triangles sharing the hypotenuse.",
            "Both triangles have equal base and height, meaning their areas are each 1/2 of the rectangle."
        ])
    },
    {
        "id": 5,
        "q": "A steamed dhokla is divided equally among 3 guests. What fractional portion does each guest receive?",
        "options": ["1/3", "1/2", "1/4", "3/1"],
        "ans": 0,
        "hint": "The whole snack is split into 3 equal portions.",
        "exp": "Each guest receives one out of three equal portions: 1/3.",
        "sol": make_sol_html([
            "Total whole dhokla = 1.",
            "Total guests = 3.",
            "Each share = 1 / 3 (one third)."
        ])
    },
    {
        "id": 6,
        "q": "When a dhokla is shared among 5 guests, each receives 1/5. If one guest gives their share to another, what is that recipient's total share?",
        "options": ["2/5", "2/10", "1/10", "3/5"],
        "ans": 0,
        "hint": "Add 1/5 + 1/5.",
        "exp": "1/5 + 1/5 = 2/5 of the total dhokla.",
        "sol": make_sol_html([
            "The recipient already holds 1/5 share.",
            "Receiving another 1/5 share adds the two pieces: 1/5 + 1/5.",
            "With the common denominator 5, add numerators: 1 + 1 = 2.",
            "Total portion = 2/5."
        ])
    },
    {
        "id": 7,
        "q": "Which fraction represents the smallest single portion of an identical whole?",
        "options": ["1/5", "1/2", "1/3", "1/4"],
        "ans": 0,
        "hint": "As the denominator gets larger, the unit piece gets smaller.",
        "exp": "1/5 is the smallest portion because the whole is split into 5 pieces instead of 2, 3, or 4.",
        "sol": make_sol_html([
            "Compare the unit fractions: 1/2, 1/3, 1/4, 1/5.",
            "When a whole is divided into more pieces, each individual piece becomes smaller.",
            "Since 5 is the largest denominator, 1/5 is the smallest portion.",
            "Order from largest to smallest: 1/2 > 1/3 > 1/4 > 1/5."
        ])
    },
    {
        "id": 8,
        "q": "Why does a piece of size 1/2 have a larger area than a piece of size 1/4 of the same shape?",
        "options": ["Because dividing into 2 parts creates larger pieces than dividing into 4 parts", "Because 4 is greater than 2", "Because the numerator is smaller", "Because halves are always circles"],
        "ans": 0,
        "hint": "Fewer shares mean more for each share.",
        "exp": "Dividing an object into fewer equal parts leaves larger individual pieces.",
        "sol": make_sol_html([
            "When sharing an item between 2 people, each gets half.",
            "When sharing the same item among 4 people, each gets half of a half (a quarter).",
            "Therefore, 1/2 is twice as large as 1/4."
        ])
    },
    {
        "id": 9,
        "q": "Can a shape cut into two uneven pieces be called divided into halves?",
        "options": ["No, halves must strictly be equal in area", "Yes, any two pieces are halves", "Yes, as long as both pieces are painted", "Only if it is a triangle"],
        "ans": 0,
        "hint": "Equality of parts is the fundamental rule of fractions.",
        "exp": "Halves strictly require equal areas. Unequal pieces cannot be called halves.",
        "sol": make_sol_html([
            "The definition of a fraction requires partitioning into equal parts.",
            "If one piece is larger than the other, neither piece is 1/2.",
            "Equality of area is mandatory."
        ])
    },
    {
        "id": 10,
        "q": "How many equal parts are created when a sheet is folded into quarters both horizontally and vertically?",
        "options": ["4 equal parts", "2 equal parts", "8 equal parts", "6 equal parts"],
        "ans": 0,
        "hint": "Quarters always mean four parts.",
        "exp": "Quarters divide the whole into 4 equal sections.",
        "sol": make_sol_html([
            "A horizontal midline fold gives 2 halves.",
            "A vertical midline fold cuts each half in two, giving 2 * 2 = 4 equal rectangles.",
            "Each rectangle is 1/4 of the sheet."
        ])
    }
]

quiz_q11_to_20 = [
    {
        "id": 11,
        "q": "A garden plot is partitioned into 5 equal beds. If 2 beds are planted with roses and 1 bed with lilies, what fraction is planted?",
        "options": ["3/5", "2/5", "1/5", "4/5"],
        "ans": 0,
        "hint": "Add the beds: 2/5 + 1/5.",
        "exp": "2/5 + 1/5 = 3/5 of the garden.",
        "sol": make_sol_html([
            "Roses take 2 out of 5 beds: 2/5.",
            "Lilies take 1 out of 5 beds: 1/5.",
            "Total planted fraction = 2/5 + 1/5 = 3/5."
        ])
    },
    {
        "id": 12,
        "q": "What fraction represents the unplanted section of a 5-bed garden if 4 beds are planted?",
        "options": ["1/5", "2/5", "3/5", "5/5"],
        "ans": 0,
        "hint": "Subtract 5/5 - 4/5.",
        "exp": "The unplanted fraction is 5/5 - 4/5 = 1/5.",
        "sol": make_sol_html([
            "The whole garden is 5/5.",
            "Planted area = 4/5.",
            "Unplanted area = 5/5 - 4/5 = 1/5."
        ])
    },
    {
        "id": 13,
        "q": "If a garden layout is divided into 7 equal strips, what fraction does each single strip represent?",
        "options": ["1/7", "7/1", "1/5", "2/7"],
        "ans": 0,
        "hint": "1 strip out of 7 total strips.",
        "exp": "Each unit strip represents 1/7 of the entire garden.",
        "sol": make_sol_html([
            "Total equal strips = 7 (denominator).",
            "Single strip considered = 1 (numerator).",
            "Fraction = 1/7."
        ])
    },
    {
        "id": 14,
        "q": "In a 7-bed garden, 3 beds have sunflowers, 2 have lavender, and 2 have jasmine. What is the total fraction planted?",
        "options": ["7/7 (one complete whole)", "6/7", "5/7", "4/7"],
        "ans": 0,
        "hint": "Add 3/7 + 2/7 + 2/7.",
        "exp": "3/7 + 2/7 + 2/7 = 7/7 = 1 complete whole garden.",
        "sol": make_sol_html([
            "Sunflowers: 3/7.",
            "Lavender: 2/7.",
            "Jasmine: 2/7.",
            "Combined sum: 3/7 + 2/7 + 2/7 = (3 + 2 + 2) / 7 = 7/7 = 1 whole."
        ])
    },
    {
        "id": 15,
        "q": "A circular dosa is cut into 3 equal slices. If 2 slices are covered with spicy onion, what fraction has spicy onion?",
        "options": ["2/3", "1/3", "3/2", "2/1"],
        "ans": 0,
        "hint": "2 slices out of 3 total slices.",
        "exp": "2 slices out of 3 equal slices is written as 2/3.",
        "sol": make_sol_html([
            "Total slices = 3.",
            "Onion slices = 2.",
            "Fraction with spicy onion = 2/3."
        ])
    },
    {
        "id": 16,
        "q": "A circular dosa is cut into 8 equal slices. 3 slices have paneer, 1 has tomato, and the rest have cheese. What fraction has cheese?",
        "options": ["4/8", "3/8", "2/8", "5/8"],
        "ans": 0,
        "hint": "Subtract paneer and tomato from 8/8.",
        "exp": "8/8 - (3/8 + 1/8) = 8/8 - 4/8 = 4/8.",
        "sol": make_sol_html([
            "Total dosa = 8/8.",
            "Paneer + Tomato = 3/8 + 1/8 = 4/8.",
            "Remaining cheese slices = 8/8 - 4/8 = 4/8 (or 1/2)."
        ])
    },
    {
        "id": 17,
        "q": "What is 1/4 of a collection of 8 oil lamps?",
        "options": ["2 lamps", "4 lamps", "1 lamp", "3 lamps"],
        "ans": 0,
        "hint": "Divide 8 by 4.",
        "exp": "8 divided by 4 equals 2 lamps.",
        "sol": make_sol_html([
            "Total lamps = 8.",
            "To find 1/4, partition the collection into 4 equal groups.",
            "8 / 4 = 2 lamps per group.",
            "Therefore, 1/4 of 8 lamps is 2 lamps."
        ])
    },
    {
        "id": 18,
        "q": "If 12 cookies are shared equally among 4 children, what fraction of the cookies does each child receive?",
        "options": ["1/4 (which is 3 cookies)", "1/3 (which is 4 cookies)", "1/2 (which is 6 cookies)", "1/6 (which is 2 cookies)"],
        "ans": 0,
        "hint": "Sharing among 4 children means each receives one fourth.",
        "exp": "Each child gets 1/4 of the cookies: 12 / 4 = 3 cookies.",
        "sol": make_sol_html([
            "Total cookies = 12.",
            "Number of children = 4.",
            "Fraction per child = 1/4.",
            "Number of cookies per child = 12 / 4 = 3 cookies."
        ])
    },
    {
        "id": 19,
        "q": "What is 1/2 of a box of 12 cookies?",
        "options": ["6 cookies", "4 cookies", "3 cookies", "8 cookies"],
        "ans": 0,
        "hint": "Divide 12 by 2.",
        "exp": "12 divided by 2 equals 6 cookies.",
        "sol": make_sol_html([
            "Half of 12 is found by dividing by 2.",
            "12 / 2 = 6 cookies.",
            "So 1/2 of 12 is 6 cookies."
        ])
    },
    {
        "id": 20,
        "q": "If 12 cookies are divided equally among 6 children, how many cookies does each child get?",
        "options": ["2 cookies (1/6 of 12)", "3 cookies (1/4 of 12)", "4 cookies (1/3 of 12)", "1 cookie"],
        "ans": 0,
        "hint": "Divide 12 by 6.",
        "exp": "12 divided by 6 equals 2 cookies per child (1/6).",
        "sol": make_sol_html([
            "Total cookies = 12.",
            "Total children = 6.",
            "Each child receives 1/6 of 12 = 12 / 6 = 2 cookies."
        ])
    }
]

quiz_q21_to_30 = [
    {
        "id": 21,
        "q": "A host has 18 return gift hairbands. If 1/3 of them are silver, how many hairbands are silver?",
        "options": ["6 hairbands", "3 hairbands", "9 hairbands", "12 hairbands"],
        "ans": 0,
        "hint": "Divide 18 by 3.",
        "exp": "18 divided by 3 equals 6 silver hairbands.",
        "sol": make_sol_html([
            "Total hairbands = 18.",
            "Fraction of silver hairbands = 1/3.",
            "Silver count = 18 / 3 = 6 hairbands."
        ])
    },
    {
        "id": 22,
        "q": "In the same set of 18 hairbands where 1/3 are silver, the remaining 2/3 are golden. How many are golden?",
        "options": ["12 hairbands", "6 hairbands", "15 hairbands", "9 hairbands"],
        "ans": 0,
        "hint": "Multiply 6 by 2, or subtract 18 - 6.",
        "exp": "18 - 6 = 12 golden hairbands (2/3 of 18 = 12).",
        "sol": make_sol_html([
            "Total hairbands = 18.",
            "Silver hairbands = 6.",
            "Golden hairbands = 18 - 6 = 12 hairbands.",
            "Alternatively, 2/3 of 18 = 2 * (18 / 3) = 2 * 6 = 12."
        ])
    },
    {
        "id": 23,
        "q": "An artisan has 24 clay pots. If 1/4 of the pots are filled with marigolds, how many pots have marigolds?",
        "options": ["6 pots", "4 pots", "8 pots", "12 pots"],
        "ans": 0,
        "hint": "Divide 24 by 4.",
        "exp": "24 divided by 4 equals 6 pots.",
        "sol": make_sol_html([
            "Total pots = 24.",
            "Fraction with marigolds = 1/4.",
            "Count = 24 / 4 = 6 pots."
        ])
    },
    {
        "id": 24,
        "q": "If 2/4 of the 24 clay pots are planted with roses, how many pots have roses?",
        "options": ["12 pots", "6 pots", "8 pots", "16 pots"],
        "ans": 0,
        "hint": "2/4 of 24 is equal to 1/2 of 24.",
        "exp": "2/4 simplifies to 1/2, and 1/2 of 24 is 12 pots.",
        "sol": make_sol_html([
            "1/4 of 24 = 6 pots.",
            "2/4 of 24 = 2 * 6 = 12 pots.",
            "Notice that 2/4 is equivalent to 1/2, and half of 24 is 12."
        ])
    },
    {
        "id": 25,
        "q": "A square box holds 16 cashew barfis. If it is divided equally among 4 family members, how many barfis does each person receive?",
        "options": ["4 barfis (1/4 of 16)", "2 barfis", "8 barfis", "6 barfis"],
        "ans": 0,
        "hint": "Divide 16 by 4.",
        "exp": "16 divided by 4 equals 4 barfis.",
        "sol": make_sol_html([
            "Total barfis = 16.",
            "Total people = 4.",
            "Share per person = 16 / 4 = 4 barfis."
        ])
    },
    {
        "id": 26,
        "q": "A tailor cuts 1/5 from a 20-centimeter ribbon. What is the length of the piece cut off?",
        "options": ["4 cm", "5 cm", "10 cm", "2 cm"],
        "ans": 0,
        "hint": "Divide 20 by 5.",
        "exp": "20 divided by 5 equals 4 cm.",
        "sol": make_sol_html([
            "Total ribbon length = 20 cm.",
            "Cut fraction = 1/5.",
            "Cut length = 20 / 5 = 4 cm."
        ])
    },
    {
        "id": 27,
        "q": "In the same 20 cm ribbon, what is the length of the remaining ribbon after cutting off 1/5 (4 cm)?",
        "options": ["16 cm (4/5 of 20 cm)", "15 cm", "18 cm", "12 cm"],
        "ans": 0,
        "hint": "Subtract 20 - 4.",
        "exp": "20 cm - 4 cm = 16 cm (which is 4/5 of 20 cm).",
        "sol": make_sol_html([
            "Total ribbon = 20 cm.",
            "Piece cut off = 4 cm.",
            "Remaining length = 20 - 4 = 16 cm.",
            "In fractions: 5/5 - 1/5 = 4/5, and 4/5 of 20 = 4 * 4 = 16 cm."
        ])
    },
    {
        "id": 28,
        "q": "When a paper strip showing 1/3 shaded is folded in half, what equivalent fraction does the shaded area show?",
        "options": ["2/6", "3/6", "1/6", "4/6"],
        "ans": 0,
        "hint": "Multiply numerator and denominator by 2.",
        "exp": "1/3 is equivalent to 2/6.",
        "sol": make_sol_html([
            "The initial fraction is 1/3.",
            "Folding the whole strip in half doubles the total parts from 3 to 6.",
            "The shaded section now contains 2 parts out of 6.",
            "Therefore, 1/3 = 2/6."
        ])
    },
    {
        "id": 29,
        "q": "Which of the following is equivalent to 1/2?",
        "options": ["2/4", "1/4", "3/4", "2/2"],
        "ans": 0,
        "hint": "Multiply both top and bottom of 1/2 by 2.",
        "exp": "(1 * 2) / (2 * 2) = 2/4.",
        "sol": make_sol_html([
            "Take the fraction 1/2.",
            "Multiply numerator by 2: 1 * 2 = 2.",
            "Multiply denominator by 2: 2 * 2 = 4.",
            "Equivalent fraction = 2/4."
        ])
    },
    {
        "id": 30,
        "q": "If you multiply the numerator and denominator of 1/2 by 4, what equivalent fraction do you get?",
        "options": ["4/8", "2/8", "4/4", "1/8"],
        "ans": 0,
        "hint": "1 * 4 = 4 and 2 * 4 = 8.",
        "exp": "Multiplying both numerator and denominator by 4 gives 4/8.",
        "sol": make_sol_html([
            "Start with 1/2.",
            "Numerator: 1 * 4 = 4.",
            "Denominator: 2 * 4 = 8.",
            "Equivalent fraction = 4/8."
        ])
    }
]

quiz_q31_to_40 = [
    {
        "id": 31,
        "q": "On a fraction wall, how many 1/10 strips are required to equal 1 complete whole bar?",
        "options": ["10 strips", "5 strips", "1 strip", "20 strips"],
        "ans": 0,
        "hint": "The denominator tells you how many parts make the whole.",
        "exp": "Ten 1/10 pieces equal 10/10, which matches 1 whole.",
        "sol": make_sol_html([
            "Each piece is 1/10.",
            "To reach 1 whole (10/10), we need ten 1/10 pieces.",
            "10 * (1/10) = 10/10 = 1."
        ])
    },
    {
        "id": 32,
        "q": "According to the fraction chart, which two unit fraction pieces combine to exactly equal 1/3?",
        "options": ["Two pieces of 1/6", "Two pieces of 1/4", "Two pieces of 1/8", "Two pieces of 1/10"],
        "ans": 0,
        "hint": "1/6 + 1/6 = 2/6 = 1/3.",
        "exp": "Two 1/6 pieces equal 2/6, which simplifies to 1/3.",
        "sol": make_sol_html([
            "1/6 + 1/6 = 2/6.",
            "Dividing numerator and denominator by 2 gives 2/6 = 1/3.",
            "Therefore, two pieces of 1/6 equal 1/3."
        ])
    },
    {
        "id": 33,
        "q": "In a square grid of 12 equal boxes, a student shades 4 boxes. What fraction of the grid is shaded?",
        "options": ["1/3 (since 4/12 = 1/3)", "1/4", "1/2", "1/6"],
        "ans": 0,
        "hint": "4 out of 12 boxes.",
        "exp": "4/12 simplifies to 1/3 by dividing numerator and denominator by 4.",
        "sol": make_sol_html([
            "Total grid boxes = 12.",
            "Shaded boxes = 4.",
            "Fraction = 4/12.",
            "Divide numerator and denominator by 4: 4/12 = 1/3."
        ])
    },
    {
        "id": 34,
        "q": "In a 12-box grid, a student shades 3 boxes and claims that 1/3 is shaded. Is the claim correct?",
        "options": ["No, 3/12 simplifies to 1/4, not 1/3", "Yes, 3 boxes always represent 1/3", "Yes, because 12 - 3 = 9", "No, the shaded fraction is 1/2"],
        "ans": 0,
        "hint": "Check 3/12 in lowest terms.",
        "exp": "3/12 = 1/4. To shade 1/3 of 12, 4 boxes must be shaded.",
        "sol": make_sol_html([
            "Total boxes = 12.",
            "1/3 of 12 = 12 / 3 = 4 boxes.",
            "The student only shaded 3 boxes, which is 3/12 = 1/4.",
            "Therefore, the claim is incorrect."
        ])
    },
    {
        "id": 35,
        "q": "If 4 out of 16 identical triangles in a rangoli design are colored green, what fraction of the design is green?",
        "options": ["1/4", "1/2", "1/8", "1/16"],
        "ans": 0,
        "hint": "Simplify 4/16.",
        "exp": "4/16 simplifies to 1/4.",
        "sol": make_sol_html([
            "Total triangles = 16.",
            "Green triangles = 4.",
            "Fraction = 4/16.",
            "Divide by 4: 4/16 = 1/4."
        ])
    },
    {
        "id": 36,
        "q": "In a mosaic square made of 16 identical triangles, 8 triangles form a central shaded diamond. What fraction is shaded?",
        "options": ["1/2", "1/4", "3/4", "2/16"],
        "ans": 0,
        "hint": "Simplify 8/16.",
        "exp": "8/16 simplifies to 1/2.",
        "sol": make_sol_html([
            "Total triangles = 16.",
            "Shaded diamond triangles = 8.",
            "Fraction = 8/16.",
            "Divide by 8: 8/16 = 1/2."
        ])
    },
    {
        "id": 37,
        "q": "How many cells must you shade to color 2/3 of a grid containing 18 cells?",
        "options": ["12 cells", "6 cells", "9 cells", "15 cells"],
        "ans": 0,
        "hint": "Find 1/3 of 18 (which is 6), then multiply by 2.",
        "exp": "1/3 of 18 = 6. 2/3 of 18 = 2 * 6 = 12 cells.",
        "sol": make_sol_html([
            "Total cells = 18.",
            "Find 1/3: 18 / 3 = 6 cells.",
            "Find 2/3: 2 * 6 = 12 cells.",
            "Shading 12 cells represents 2/3 of the grid."
        ])
    },
    {
        "id": 38,
        "q": "How many cells must you shade to color 4/6 of a grid containing 18 cells?",
        "options": ["12 cells (which is equivalent to 2/3)", "8 cells", "6 cells", "14 cells"],
        "ans": 0,
        "hint": "Find 1/6 of 18 (which is 3), then multiply by 4.",
        "exp": "1/6 of 18 = 3. 4/6 of 18 = 4 * 3 = 12 cells.",
        "sol": make_sol_html([
            "Total cells = 18.",
            "Find 1/6: 18 / 6 = 3 cells.",
            "Find 4/6: 4 * 3 = 12 cells.",
            "Notice that 4/6 of 18 is 12 cells, exactly the same as 2/3 of 18!"
        ])
    },
    {
        "id": 39,
        "q": "To shade 3/4 of a 12-cell rectangular grid, how many cells should be colored?",
        "options": ["9 cells", "3 cells", "6 cells", "10 cells"],
        "ans": 0,
        "hint": "Find 1/4 of 12 (which is 3), then multiply by 3.",
        "exp": "1/4 of 12 = 3. 3/4 of 12 = 3 * 3 = 9 cells.",
        "sol": make_sol_html([
            "Total cells = 12.",
            "1/4 of 12 = 12 / 4 = 3 cells.",
            "3/4 of 12 = 3 * 3 = 9 cells.",
            "Shading 9 cells covers three quarters of the grid."
        ])
    },
    {
        "id": 40,
        "q": "To shade 5/8 of a 16-box grid, how many boxes must be filled with color?",
        "options": ["10 boxes", "8 boxes", "5 boxes", "12 boxes"],
        "ans": 0,
        "hint": "Find 1/8 of 16 (which is 2), then multiply by 5.",
        "exp": "1/8 of 16 = 2. 5/8 of 16 = 5 * 2 = 10 boxes.",
        "sol": make_sol_html([
            "Total boxes = 16.",
            "1/8 of 16 = 16 / 8 = 2 boxes.",
            "5/8 of 16 = 5 * 2 = 10 boxes.",
            "Shading 10 boxes represents 5/8 of the grid."
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
