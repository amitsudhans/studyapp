# -*- coding: utf-8 -*-
"""
Generate Slides 9 to 16 for Class 4 Maths Chapter 3: Patterns Around Us
Calibrated strictly to 195-215 words per speech.
"""

def get_part2_slides():
    return [
        {
            "id": 9,
            "title": "Odd Number Remainder",
            "section": "Two Ways",
            "speech": (
                "Having explored even numbers, let us examine the complementary family: odd numbers. Any whole quantity that leaves exactly "
                "one unpaired item when divided into groups of two is called an odd number. Consider seven ripe mangoes. If we pair them up, "
                "we get three complete pairs of two mangoes each, but one solitary mango remains without a partner. Because of this leftover item, "
                "seven is an odd number. Now consider nine pebbles. Nine pebbles form four complete pairs, with one extra pebble left on the side. "
                "Therefore, nine is an odd number. Notice the characteristic visual shape of an odd number when arranged in two parallel rows. "
                "One row will always be exactly one unit longer than the other row. This creates a distinct protruding step or ledge at the end of the line. "
                "Because of this extra unit, odd numbers can never be split into two equal whole numbers. If you try to share an odd number equally "
                "between two friends without cutting, one friend will always receive one more item, or one item must be set aside. "
                "Odd numbers possess dynamic energy and an unmistakable signature remainder of one. "
                "Use the interactive odd pairing tool below to test numbers like five, nine, and fifteen, observing the lonely remainder dot."
            ),
            "checkpoints": [
                {
                    "q": "What is the remainder when an odd number is divided by 2?",
                    "options": ["Always 0", "Always 1", "Always 2", "Depends on the number"],
                    "ans": 1,
                    "exp": "By definition, dividing any odd number by 2 leaves a remainder of exactly 1."
                },
                {
                    "q": "If 13 marbles are paired up, how many complete pairs and leftover marbles are obtained?",
                    "options": ["5 pairs and 3 leftovers", "6 pairs and 0 leftovers", "6 pairs and 1 leftover", "7 pairs and 1 leftover"],
                    "ans": 2,
                    "exp": "13 ÷ 2 = 6 complete pairs (12 marbles) with exactly 1 leftover marble."
                }
            ]
        },
        {
            "id": 10,
            "title": "Numbers One Twenty",
            "section": "Two Ways",
            "speech": (
                "Let us systematically investigate the numbers from one to twenty to observe how even and odd quantities behave in sequence. "
                "Beginning with one, a single item cannot form a pair, so one is odd. Adding another gives two, which forms one complete pair, so two is even. "
                "Three leaves one remainder, making it odd. Four forms two complete pairs, making it even. Continuing this check reveals a remarkable pattern: "
                "one, three, five, seven, nine, eleven, thirteen, fifteen, seventeen, and nineteen are odd. Meanwhile, two, four, six, eight, ten, twelve, "
                "fourteen, sixteen, eighteen, and twenty are even. Notice that every number in the two-times multiplication table is an even number. "
                "When we recite two, four, six, eight, ten, twelve, fourteen, sixteen, eighteen, and twenty, we are counting exclusively by even numbers. "
                "This occurs because every multiple of two is formed by taking groups of two, ensuring complete pairing by its very definition. "
                "Even and odd numbers alternate in a strict, unbroken rhythmic cycle: odd, even, odd, even, repeating endlessly across the number line. "
                "Take a moment to test this pairing progression in the interactive number classifier below to see dots pair up dynamically from one to twenty."
            ),
            "checkpoints": [
                {
                    "q": "Are all numbers in the 2-times multiplication table even numbers?",
                    "options": ["No, some are odd", "Yes, every multiple of 2 is an even number", "Only numbers greater than 10", "Only numbers ending in 0"],
                    "ans": 1,
                    "exp": "Yes, every multiple of 2 is formed by complete pairs of 2, so every product in the 2-times table is even."
                },
                {
                    "q": "Between 1 and 20 inclusive, how many numbers are odd and how many are even?",
                    "options": ["8 odd and 12 even", "9 odd and 11 even", "10 odd and 10 even", "11 odd and 9 even"],
                    "ans": 2,
                    "exp": "From 1 to 20, there are exactly 10 odd numbers and 10 even numbers, perfectly balanced."
                }
            ]
        },
        {
            "id": 11,
            "title": "Crayon Number Grid",
            "section": "Crayons Arrangement",
            "speech": (
                "Visual charts help us spot numerical patterns effortlessly. Imagine a large classroom chart displaying numbers from one to fifty, "
                "arranged like orderly boxes of colorful drawing crayons in rows of ten. Let us practice a visual classification exercise on this grid. "
                "We place a circle around every odd number and draw a square box around every even number. As you complete the chart, observe the columns. "
                "All the numbers in the first column end in one: one, eleven, twenty-one, thirty-one, forty-one. Every single one is circled because they are all odd. "
                "The second column contains numbers ending in two: two, twelve, twenty-two, thirty-two, forty-two. Every number in this column is boxed with a square "
                "because they are all even. Moving across the grid reveals that columns one, three, five, seven, and nine consist entirely of circled odd numbers. "
                "Conversely, columns two, four, six, eight, and ten consist entirely of boxed even numbers. The grid splits into alternating vertical stripes "
                "of odd and even numbers. This visual striping confirms that the ending digit alone dictates whether any number is odd or even. "
                "Step into the interactive crayon grid below and toggle markers to highlight vertical parity stripes from one to fifty."
            ),
            "checkpoints": [
                {
                    "q": "In a 1–50 number grid with rows of 10, which column contains only even numbers?",
                    "options": ["Column ending in 3", "Column ending in 5", "Column ending in 6", "Column ending in 7"],
                    "ans": 2,
                    "exp": "The column ending in 6 (6, 16, 26, 36, 46) contains only even numbers."
                },
                {
                    "q": "What shape marker would you place on number 37 in the crayon grid?",
                    "options": ["A square box (even)", "A circle (odd)", "A triangle", "No marker"],
                    "ans": 1,
                    "exp": "37 ends in 7, which is an odd digit, so 37 is odd and receives a circle marker."
                }
            ]
        },
        {
            "id": 12,
            "title": "Book Page Parity",
            "section": "Crayons Arrangement",
            "speech": (
                "A wonderful real-world example of alternating number parity can be observed simply by opening any printed textbook or storybook. "
                "Pick up a mathematics book and open it flat on your reading desk. Look at the two facing pages in front of you. In standard book publishing, "
                "the left-hand page always bears an even page number, such as twenty-four, forty-six, or eighty-eight. Meanwhile, the right-hand page directly "
                "opposite always displays an odd page number, such as twenty-five, forty-seven, or eighty-nine. Why does this invariant structure occur? "
                "Because a book begins with page one on the right-hand front side of the opening leaf. Flipping each printed sheet advances the reading count "
                "by two pages: an even back page on the left and a new odd page on the right. Therefore, every two-page spread consists of an even page followed "
                "immediately by an odd page. The sum of the two facing page numbers is always an odd number, because an even number plus an odd number always "
                "yields an odd total. For example, page fourteen plus page fifteen equals twenty-nine. "
                "Use the interactive virtual book below to flip through spreads, inspecting page numbers and verifying their alternating parity."
            ),
            "checkpoints": [
                {
                    "q": "If the left page of an open book is page 42, what is the number of the facing right page?",
                    "options": ["Page 41", "Page 43", "Page 44", "Page 40"],
                    "ans": 1,
                    "exp": "The facing right page directly follows the left page, so it is 42 + 1 = 43, which is an odd number."
                },
                {
                    "q": "What is the parity of the sum of two facing page numbers (an even page plus an odd page)?",
                    "options": ["Always even", "Always odd", "Sometimes even, sometimes odd", "Always a multiple of 10"],
                    "ans": 1,
                    "exp": "An even number plus an odd number always equals an odd number (e.g., 20 + 21 = 41)."
                }
            ]
        },
        {
            "id": 13,
            "title": "Multi-Digit Parity Rule",
            "section": "Even and Odd Number Exploration & Properties",
            "speech": (
                "How do we determine if very large numbers, like three hundred, four hundred fifteen, or seven hundred eighty-eight, are even or odd? "
                "Do we need to divide the entire large number by two, or draw hundreds of pairing dots? The delightful answer is no! "
                "We only need to look at a single digit: the digit in the ones place. Every bundle of ten, hundred, or thousand is formed by multiplying by ten. "
                "Since ten is an even number, ten, twenty, one hundred, and one thousand are always completely divisible into pairs of two. "
                "Therefore, all the tens, hundreds, and thousands digits pair up with zero remainder. Parity depends entirely on the leftover ones digit. "
                "Here is the universal rule: if a number ends in zero, two, four, six, or eight, the entire number is even. "
                "If a number ends in one, three, five, seven, or nine, the entire number is odd. Look at forty-six: it ends in six, so it is even. "
                "Look at sixty-seven: it ends in seven, so it is odd. Three hundred ends in zero, making it even. Four hundred fifteen ends in five, making it odd. "
                "Try testing massive multi-digit numbers in the interactive parity scanner below to witness this fast rule in action."
            ),
            "checkpoints": [
                {
                    "q": "Which of the following numbers is an odd number: 154, 300, 415, 78?",
                    "options": ["154", "300", "415", "78"],
                    "ans": 2,
                    "exp": "415 ends in 5, which is an odd digit, making 415 an odd number."
                },
                {
                    "q": "A 4-digit number ends in 8. Is the number even or odd?",
                    "options": ["Odd", "Even", "Cannot tell without knowing all digits", "Both even and odd"],
                    "ans": 1,
                    "exp": "Any number ending in 8 is an even number, regardless of how many digits precede it."
                }
            ]
        },
        {
            "id": 14,
            "title": "Digit Permutation Parity",
            "section": "Even and Odd Number Exploration & Properties",
            "speech": (
                "Let us explore how rearranging digits alters the parity of formed numbers. Suppose you are given two number cards: the digit one "
                "and the digit six. What two-digit numbers can you assemble using both digits without repeating? You can form sixteen, or you can reverse "
                "the digits to form sixty-one. Now examine their parity. In the number sixteen, six is placed in the ones position. Because six is an even digit, "
                "sixteen is an even number. However, when we reverse the digits to make sixty-one, the digit one occupies the ones position. "
                "Because one is an odd digit, sixty-one is an odd number. Notice that changing the position of digits completely flips the parity. "
                "The tens digit has zero influence on whether the number is even or odd; only the final digit in the ones place matters. "
                "Now consider the digits three and five. Reversing them produces thirty-five and fifty-three. Since both three and five are odd digits, "
                "both assembled numbers are odd. If you choose two even digits, like four and eight, both forty-eight and eighty-four remain even. "
                "Experiment on the interactive digit permutation table below to drag digits into place and observe how position alters parity."
            ),
            "checkpoints": [
                {
                    "q": "Using the digits 2 and 7, what is the even number that can be formed?",
                    "options": ["72", "27", "Both 72 and 27", "Neither is even"],
                    "ans": 0,
                    "exp": "72 ends in 2 (an even digit), so 72 is even. 27 ends in 7 (an odd digit), so 27 is odd."
                },
                {
                    "q": "If you are given the digits 4 and 8, how many odd 2-digit numbers can you form using both digits?",
                    "options": ["0 numbers", "1 number", "2 numbers", "4 numbers"],
                    "ans": 0,
                    "exp": "Both digits (4 and 8) are even, so both possible numbers (48 and 84) are even. 0 odd numbers can be formed."
                }
            ]
        },
        {
            "id": 15,
            "title": "Consecutive Number Alternation",
            "section": "Even and Odd Number Exploration & Properties",
            "speech": (
                "Whenever we count in order along the number line, numbers alternate between even and odd with perfect mathematical regularity. "
                "Let us observe any ten consecutive numbers, such as forty-one through fifty. Forty-one is odd, forty-two is even, forty-three is odd, "
                "forty-four is even, forty-five is odd, forty-six is even, forty-seven is odd, forty-eight is even, forty-nine is odd, and fifty is even. "
                "Why does this strict alternating pattern never fail? Because adding one to any number changes its pairing balance. "
                "If you start with an even number where all items are paired, adding one extra item creates an unpaired remainder, producing an odd number. "
                "Conversely, if you start with an odd number containing an unpaired remainder, adding one extra item completes the pair, producing an even number. "
                "This principle leads to a fundamental neighbor rule: the numbers immediately preceding and directly following any odd number are always even. "
                "Similarly, the numbers immediately preceding and following any even number are always odd. Every odd number is cushioned between two even neighbors, "
                "and every even number is cushioned between two odd neighbors. "
                "Explore the interactive consecutive number tracker below to slide across the number line and observe this rhythmic neighbor heartbeat."
            ),
            "checkpoints": [
                {
                    "q": "What can be said about the two numbers directly neighboring an odd number on the number line?",
                    "options": ["Both neighbors are odd", "Both neighbors are even", "One neighbor is odd, one is even", "It depends on the number"],
                    "ans": 1,
                    "exp": "The predecessor (number - 1) and successor (number + 1) of any odd number are both even numbers."
                },
                {
                    "q": "In any sequence of 5 consecutive whole numbers, what is the minimum number of even numbers?",
                    "options": ["1", "2", "3", "4"],
                    "ans": 1,
                    "exp": "A sequence of 5 numbers can be either (Odd, Even, Odd, Even, Odd) with 2 even numbers, or (Even, Odd, Even, Odd, Even) with 3 even numbers. The minimum is 2."
                }
            ]
        },
        {
            "id": 16,
            "title": "Range Parity Balance",
            "section": "Even and Odd Number Exploration & Properties",
            "speech": (
                "To conclude our investigation of number patterns, let us examine parity balance across broad numerical intervals. "
                "Consider all the counting numbers from one to one hundred. How many of these one hundred numbers are even, and how many are odd? "
                "Because whole numbers alternate strictly between odd and even in continuous pairs, every two consecutive numbers contain exactly one odd number "
                "and one even number. In the first ten numbers, there are five odd numbers and five even numbers. In the next ten numbers, from eleven to twenty, "
                "there are again five odd and five even numbers. Since one hundred consists of ten equal decades of ten numbers each, we multiply ten decades "
                "by five. This reveals that between one and one hundred, there are exactly fifty odd numbers and fifty even numbers. "
                "The two families divide the entire century of numbers into two perfectly equal halves. Furthermore, the sum of any two even numbers is always even, "
                "and the sum of any two odd numbers is also always even, because their two solitary remainders pair together to make another complete pair. "
                "Use the interactive range balance simulator below to inspect intervals and visualize the harmonious fifty-fifty split."
            ),
            "checkpoints": [
                {
                    "q": "Between 1 and 100 inclusive, how many odd numbers are there?",
                    "options": ["45", "49", "50", "51"],
                    "ans": 2,
                    "exp": "Exactly half of the first 100 counting numbers are odd (50 odd numbers) and half are even (50 even numbers)."
                },
                {
                    "q": "What is the parity of the sum of two odd numbers (for example, 7 + 5 = 12)?",
                    "options": ["Always odd", "Always even", "Sometimes odd, sometimes even", "Zero"],
                    "ans": 1,
                    "exp": "Odd + Odd is always Even, because the two leftover remainders of 1 combine to form a complete pair of 2."
                }
            ]
        }
    ]

if __name__ == '__main__':
    slides = get_part2_slides()
    for s in slides:
        words = len(s['speech'].split())
        print(f"Slide {s['id']}: {s['title']} -> Word count: {words}")
        assert 195 <= words <= 215, f"Slide {s['id']} word count {words} outside 195-215 range!"
    print("All slides 9-16 pass word count validation!")
