# -*- coding: utf-8 -*-
"""
Generate Slides 1 to 8 for Class 4 Maths Chapter 3: Patterns Around Us
Calibrated strictly to 195-215 words per speech.
"""

def get_part1_slides():
    return [
        {
            "id": 1,
            "title": "Coconut Tree Grids",
            "section": "Let Us Count",
            "speech": (
                "Welcome to our mathematics laboratory. Today we explore fascinating patterns in counting, grouping, and number properties. "
                "Observe this orchard where a farmer has planted coconut trees in neat, uniform rows and columns. When items are arranged "
                "in a rectangular array, we do not need to count each tree one by one. Instead, we can observe the structure. "
                "Notice that there are four horizontal rows and six vertical columns of coconut trees. To determine the total number of trees, "
                "we multiply the number of rows by the number of columns. Multiplying four by six yields twenty-four trees in total. "
                "This grid structure allows quick mental calculations. Now consider plucking coconuts from these trees. Suppose five ripe coconuts "
                "are harvested from every single tree in this orchard. To find the overall harvest, we multiply the twenty-four trees by five coconuts. "
                "Breaking twenty-four into twenty and four makes mental multiplication simple: twenty times five equals one hundred, and four times five "
                "equals twenty. Combining them gives one hundred twenty coconuts harvested in total. Grid arrangements turn repetitive addition into fast multiplication. "
                "Try adjusting the rows and columns in the interactive orchard to observe how array patterns transform counting tasks."
            ),
            "checkpoints": [
                {
                    "q": "An orchard has 5 rows with 7 coconut trees in each row. How many trees are there in total?",
                    "options": ["30 trees", "35 trees", "40 trees", "42 trees"],
                    "ans": 1,
                    "exp": "Using array multiplication, 5 rows × 7 trees per row = 35 trees in total."
                },
                {
                    "q": "If 4 coconuts are harvested from each of the 35 trees, what is the total coconut harvest?",
                    "options": ["120 coconuts", "140 coconuts", "150 coconuts", "160 coconuts"],
                    "ans": 1,
                    "exp": "Multiplying 35 trees × 4 coconuts gives: (30 × 4) + (5 × 4) = 120 + 20 = 140 coconuts."
                }
            ]
        },
        {
            "id": 2,
            "title": "Stacked Cups Columns",
            "section": "Let Us Count",
            "speech": (
                "Let us now visit a traditional pottery workshop. Here, a skilled potter has organized freshly baked clay cups and plates "
                "into orderly vertical stacks. Stacking items vertically in equal columns creates an excellent visual pattern for multiplication. "
                "Observe the workbench layout. There are five separate stacks of clay tea cups standing side by side. Each vertical stack contains "
                "exactly six cups nested securely. Instead of counting every cup individually from left to right, we identify the repeated group size. "
                "Here, we have five groups of six cups. Multiplying five by six gives thirty clay cups in total. Beside the cups, we see stacks "
                "of circular dining plates. There are four vertical stacks, and each stack contains eight plates. Multiplying four stacks by eight plates "
                "reveals that thirty-two plates are organized on the pottery bench. Grouping identical stacks into columns and rows is a powerful spatial habit "
                "used across many daily professions. It eliminates counting errors, speeds up inventory audits, and prevents accidental breakage on busy production floors. "
                "Whether stacking ceramic bowls, storage boxes, or metal containers, column multiplication remains the fastest counting strategy. "
                "Use the interactive stack builder below to vary the number of columns and items per stack, observing how total counts scale dynamically."
            ),
            "checkpoints": [
                {
                    "q": "A potter arranges 6 vertical stacks with 7 clay cups in each stack. What is the total count of cups?",
                    "options": ["36 cups", "42 cups", "48 cups", "49 cups"],
                    "ans": 1,
                    "exp": "Multiply 6 stacks × 7 cups per stack = 42 cups in total."
                },
                {
                    "q": "If 3 cups are removed from each of the 6 stacks, how many cups remain on the workbench?",
                    "options": ["20 cups", "24 cups", "28 cups", "30 cups"],
                    "ans": 1,
                    "exp": "Each stack now has 7 - 3 = 4 cups. Total remaining cups = 6 × 4 = 24 cups."
                }
            ]
        },
        {
            "id": 3,
            "title": "Layered Sweet Trays",
            "section": "Let Us Count",
            "speech": (
                "In sweet shops across India, festive confectioners arrange mouth-watering coconut laddoos and milk pedas in beautiful symmetrical patterns. "
                "Examine this square display tray closely. The confectioner has arranged the sweets in a distinctive cross-shaped geometric layout. "
                "Coconut laddoos form the central cross arms, with five laddoos placed in a central horizontal row and four more completing the vertical arm. "
                "This makes nine coconut laddoos per tray. In the four outer corner quadrants, delicate milk pedas are arranged in clusters of four. "
                "Four corner clusters of four milk pedas each equal sixteen pedas on each single tray. When trays are stacked in multiple identical tiers, "
                "the total quantity of each confection scales systematically. For example, if three identical trays are prepared for a wedding celebration, "
                "we multiply the contents of one tray by three. Three trays will hold three times nine, which equals twenty-seven coconut laddoos, and "
                "three times sixteen, which equals forty-eight milk pedas. Symmetrical geometric packaging ensures equal portioning, neat artistic presentation, "
                "and rapid visual accounting for large festival orders. Combining shape symmetry with multiplication makes complex catering inventories effortless. "
                "Explore the multi-tiered sweet tray simulator below to inspect individual trays or calculate combined batch totals for large festive gatherings."
            ),
            "checkpoints": [
                {
                    "q": "A sweet tray contains 9 coconut laddoos and 16 milk pedas. How many total sweets are on one tray?",
                    "options": ["23 sweets", "25 sweets", "27 sweets", "30 sweets"],
                    "ans": 1,
                    "exp": "Total sweets on one tray = 9 laddoos + 16 pedas = 25 sweets."
                },
                {
                    "q": "How many total milk pedas are packed across 4 identical sweet trays?",
                    "options": ["48 pedas", "56 pedas", "64 pedas", "72 pedas"],
                    "ans": 2,
                    "exp": "Each tray holds 16 pedas. For 4 trays: 4 × 16 = 64 milk pedas in total."
                }
            ]
        },
        {
            "id": 4,
            "title": "Banknote Coin Patterns",
            "section": "Patterns with Money",
            "speech": (
                "Money systems provide fascinating patterns combining numerical values with geometric symmetry. Young learners often practice organizing coins "
                "and banknotes into radial mandalas and balanced arrays. Observe the pattern on our virtual cash table. At the center sits a neat stack "
                "of four ten-rupee currency notes. Around this central core, coins are placed symmetrically: four five-rupee coins in the cardinal compass directions, "
                "eight two-rupee coins at the intermediate diagonals, and an outer circular ring of eight one-rupee coins. To calculate the total monetary value, "
                "we group by denomination carefully. Four ten-rupee notes equal forty rupees. Four five-rupee coins equal twenty rupees. Eight two-rupee coins equal "
                "sixteen rupees. Finally, eight one-rupee coins equal eight rupees. Adding these partial sums step by step reveals the full amount: forty plus twenty "
                "is sixty, plus sixteen is seventy-six, plus eight gives eighty-four rupees. Notice that grouping identical denominations makes money calculation "
                "both orderly, reliable, and completely foolproof. Symmetrical money arrangements also demonstrate clearly that physical coin count does not directly match "
                "monetary value, because higher-denomination coins carry greater buying power. "
                "Step forward and use the interactive money board below to arrange coins into symmetrical geometric rosettes and verify denomination totals instantly."
            ),
            "checkpoints": [
                {
                    "q": "A money pattern contains 5 ten-rupee notes, 4 five-rupee coins, and 6 two-rupee coins. What is the total value?",
                    "options": ["₹76", "₹82", "₹86", "₹92"],
                    "ans": 1,
                    "exp": "Value = (5 × 10) + (4 × 5) + (6 × 2) = 50 + 20 + 12 = ₹82."
                },
                {
                    "q": "Which coin collection has a greater monetary value: 7 five-rupee coins or 16 two-rupee coins?",
                    "options": ["7 five-rupee coins", "16 two-rupee coins", "Both are equal", "Cannot be determined"],
                    "ans": 0,
                    "exp": "7 × ₹5 = ₹35, while 16 × ₹2 = ₹32. Therefore, 7 five-rupee coins represent a greater monetary value."
                }
            ]
        },
        {
            "id": 5,
            "title": "Building Target Amounts",
            "section": "Patterns with Money",
            "speech": (
                "In everyday transactions, we frequently combine different currency denominations to pay exact prices without needing change. "
                "Suppose we must assemble a target amount of thirty-six rupees. We can use three ten-rupee notes to make thirty rupees, one five-rupee coin "
                "to reach thirty-five, and one single one-rupee coin to reach thirty-six rupees. Notice how we start with the largest practical denomination "
                "to minimize the total number of physical tokens needed. Now consider a larger target of one hundred twenty-five rupees. We can select "
                "one hundred-rupee note, one twenty-rupee note, and one five-rupee coin, using just three currency items. Alternatively, if no hundred-rupee note "
                "is available, we could use twelve ten-rupee notes and one five-rupee coin. For one hundred eighty-three rupees, we can combine one hundred-rupee note, "
                "one fifty-rupee note, three ten-rupee notes, one two-rupee coin, and one one-rupee coin. Understanding multiple combinations of notes and coins develops "
                "strong number sense and flexible place-value thinking. Large denominations represent bundles of tens and hundreds, directly mirroring our decimal place-value system. "
                "Mastering currency combinations ensures confidence in local markets, banks, and grocery billing. "
                "Experiment on the interactive currency builder to assemble target monetary amounts using the fewest possible coins and notes."
            ),
            "checkpoints": [
                {
                    "q": "What is the minimum number of notes and coins needed to form ₹87 using standard Indian denominations (₹50, ₹20, ₹10, ₹5, ₹2, ₹1)?",
                    "options": ["4 items", "5 items", "6 items", "7 items"],
                    "ans": 1,
                    "exp": "Optimal combination: 1 × ₹50 + 1 × ₹20 + 1 × ₹10 + 1 × ₹5 + 1 × ₹2 = ₹87 (5 items)."
                },
                {
                    "q": "Can ₹36 be formed using only ₹5 coins and ₹2 coins?",
                    "options": ["No, impossible", "Yes, with 6 five-rupee coins and 3 two-rupee coins", "Yes, with 7 five-rupee coins and 1 two-rupee coin", "Yes, with 4 five-rupee coins and 7 two-rupee coins"],
                    "ans": 1,
                    "exp": "6 × ₹5 = ₹30, and 3 × ₹2 = ₹6. 30 + 6 = ₹36."
                }
            ]
        },
        {
            "id": 6,
            "title": "Visualizing Quantity Distributions",
            "section": "Two Ways",
            "speech": (
                "A given quantity of objects can often be arranged in more than one distinct geometric pattern. Examining these alternative arrangements "
                "helps us uncover hidden mathematical properties such as symmetry, divisibility, and pairing. Consider twelve shiny brass coins placed on a mat. "
                "One young explorer arranges these twelve coins into two neat horizontal rows of six coins each. In this layout, every coin in the upper row "
                "has an exact partner directly beneath it in the lower row. It looks like a balanced parade of two-by-two marchers. Another young explorer takes "
                "the very same twelve coins and arranges them into three columns of four coins each, forming a compact rectangular block. Both arrangements represent "
                "the exact same quantity of twelve, yet each highlights a different mathematical relationship. The two-row arrangement demonstrates that twelve "
                "splits evenly into two equal halves of six, with no leftover coins. The three-column arrangement demonstrates that twelve is a multiple of three and four. "
                "Whenever we distribute quantities into geometric patterns, we visually prove arithmetic truths and foster spatial reasoning. "
                "Observing numbers in multiple shapes strengthens our conceptual grasp of factors and fair sharing. "
                "Use the interactive distribution canvas below to drag coins into pairs, triangular pyramids, or rectangular arrays, comparing two distinct perspectives side by side."
            ),
            "checkpoints": [
                {
                    "q": "Which of the following geometric rectangular arrays CANNOT be formed using exactly 14 coins without leftovers?",
                    "options": ["2 rows of 7 coins", "7 rows of 2 coins", "3 rows of 4 coins", "1 row of 14 coins"],
                    "ans": 2,
                    "exp": "3 rows of 4 coins equals 12 coins, leaving 2 coins left over. 14 is not divisible by 3."
                },
                {
                    "q": "If 16 coins are arranged into 2 equal rows, how many coins are in each row?",
                    "options": ["6 coins", "7 coins", "8 coins", "9 coins"],
                    "ans": 2,
                    "exp": "Dividing 16 coins evenly into 2 rows yields 16 ÷ 2 = 8 coins per row."
                }
            ]
        },
        {
            "id": 7,
            "title": "Concept of Pairs",
            "section": "Two Ways",
            "speech": (
                "In nature, daily life, and mathematics, the concept of a pair is fundamental. A pair always consists of exactly two matching items "
                "working together. Think of familiar examples from your home and classroom: a pair of shoes, a pair of socks, a pair of gloves, or a pair "
                "of eyes. When children line up for school assembly in pairs, they walk side by side in twos. This pairing process gives us a powerful method "
                "for testing any collection of items. Imagine placing a collection of buttons on your desk. To test the collection, you begin grouping the buttons "
                "two by two. You take two buttons and push them together into a pair. You take another two buttons and form a second pair. You continue this "
                "two-by-two grouping repeatedly until all buttons have been examined. Two possible outcomes can occur. Either every single button finds a partner "
                "and forms a complete pair, or exactly one solitary button is left over without a partner. This universal test divides all whole numbers into "
                "two great families: even numbers and odd numbers. "
                "Step into the pairing laboratory below, tap the group button, and watch items automatically couple into pairs to discover the remaining balance."
            ),
            "checkpoints": [
                {
                    "q": "How many items are there in 6 complete pairs of socks?",
                    "options": ["8 socks", "10 socks", "12 socks", "14 socks"],
                    "ans": 2,
                    "exp": "Each pair has 2 socks. Therefore, 6 pairs × 2 socks per pair = 12 socks."
                },
                {
                    "q": "If you have 11 pencils and group them into pairs, how many pencils will be left without a partner?",
                    "options": ["0 pencils", "1 pencil", "2 pencils", "3 pencils"],
                    "ans": 1,
                    "exp": "11 pencils form 5 complete pairs (10 pencils) with exactly 1 pencil left unpaired."
                }
            ]
        },
        {
            "id": 8,
            "title": "Even Number Pairing",
            "section": "Two Ways",
            "speech": (
                "Now let us formalize the mathematical definition of an even number. Any whole quantity that can be divided completely into pairs "
                "of two without leaving any leftover item is called an even number. Consider the number eight. If we take eight marbles and pair them up, "
                "we get four complete pairs. Not a single marble is left alone. Therefore, eight is an even number. Now look at the number ten. Ten marbles "
                "form five complete pairs with zero remainder. Thus, ten is an even number. Notice an important visual feature: when an even number of dots "
                "is arranged in two parallel rows, both rows have the exact same length. The structure is completely symmetrical, like a solid two-lane road. "
                "Because every item has a partner, even numbers can always be split into two equal whole halves. Half of eight is four, and half of ten is five. "
                "Zero is also classified as an even number, because zero items leave zero remainder when grouped by two. "
                "Even numbers represent harmony, balance, and complete pairing in arithmetic. "
                "Use the interactive parity tester below to test numbers like six, twelve, and eighteen, observing how every dot locks securely into a matching partner."
            ),
            "checkpoints": [
                {
                    "q": "Which of the following numbers can be divided into pairs of 2 with zero remainder?",
                    "options": ["7", "11", "14", "17"],
                    "ans": 2,
                    "exp": "14 can be divided into 7 complete pairs (14 ÷ 2 = 7) with 0 remainder, making 14 an even number."
                },
                {
                    "q": "If an even number of children are arranged into pairs, what can be said about the remaining unpaired children?",
                    "options": ["There is always 1 child left", "There are always 2 children left", "There are exactly 0 children left", "It varies depending on the number"],
                    "ans": 2,
                    "exp": "By definition, an even number leaves exactly 0 unpaired items when grouped in twos."
                }
            ]
        }
    ]

if __name__ == '__main__':
    slides = get_part1_slides()
    for s in slides:
        words = len(s['speech'].split())
        print(f"Slide {s['id']}: {s['title']} -> Word count: {words}")
        assert 195 <= words <= 215, f"Slide {s['id']} word count {words} outside 195-215 range!"
    print("All slides 1-8 pass word count validation!")
