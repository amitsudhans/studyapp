#!/usr/bin/env python3
"""
Slide Data Generator for NCERT Class 3 Mathematics - Chapter 7: Raksha Bandhan
Part 1: Slides 1 to 8
Strictly 195 - 215 words per spoken text.
1-3 word titles.
No human names (Gopal, Dhara, Atya, etc. removed/generalized).
No teacher personas.
"""

import json

slides_part1 = [
    {
        "id": 1,
        "title": "Festival Item Counting",
        "subtitle": "Discovering quantities across festive celebration decor",
        "speech": (
            "Welcome to our mathematics laboratory where festive preparations bring numbers to vibrant life! "
            "When decorating a joyful courtyard for a special festival, items are gathered in distinct groups across every doorway. "
            "Look at the colourful entrance adorned with mango leaves strung across doorways, sparkling decorative drinking glasses on silver trays, fresh sweet pomegranates, and bright marigold garlands. "
            "Instead of counting items haphazardly one by one, organizing them into identifiable groups helps us count quickly and accurately. "
            "For instance, we can count mango leaves in pairs, arrange glasses in neat rows of three, and place pomegranates in clusters of four. "
            "This structured approach introduces the fundamental foundation of arithmetic: seeing quantities as groups of equal size. "
            "Observe the central display table where twenty decorative leaves hang along the border, six water glasses stand in two rows of three, and eight pomegranates rest in two baskets of four. "
            "By identifying these structured groupings, our minds transition from slow single-item counting toward efficient pattern recognition. "
            "Every festive decoration provides a practical opportunity to tally, group, and compare quantities with precision. "
            "Explore the interactive counting display to inspect each decorative collection, adjust group filters, and verify total sums through visual highlights."
        ),
        "checkpoints": [
            {
                "question": "If 4 doorway garlands each contain 5 bright marigold flowers, what is the total flower count?",
                "options": ["15 flowers", "20 flowers", "24 flowers", "18 flowers"],
                "answer": 1,
                "hint": "Count 4 equal groups of 5 flowers: 5 + 5 + 5 + 5.",
                "explanation": "Four garlands with 5 flowers each make 4 groups of 5. Adding 5 four times gives exactly 20 flowers in total."
            },
            {
                "question": "Which counting method is fastest and most reliable for large decorative arrangements?",
                "options": ["Counting items haphazardly one by one", "Arranging items in equal groups and counting by clusters", "Guessing the total amount by size", "Ignoring small items completely"],
                "answer": 1,
                "hint": "Grouping items equally allows skip counting and multiplication.",
                "explanation": "Organizing items into equal groups and counting by clusters allows fast, error-free calculation through repeated addition."
            }
        ]
    },
    {
        "id": 2,
        "title": "Craft Material Groups",
        "subtitle": "Calculating materials needed for handmade decorative wristbands",
        "speech": (
            "Crafting handmade festive wristbands called rakhis requires assembling specific decorative craft components in exact proportions. "
            "To build one single beautiful wristband, a craftsperson needs exactly one central silk flower, two coloured satin threads, and four sparkling golden beads. "
            "When we decide to craft five identical wristbands for our friends, how many of each component must we gather beforehand? "
            "We calculate the total requirements by scaling each craft item according to the number of wristbands. "
            "For five wristbands, we need five groups of one flower, which equals five flowers altogether. "
            "Next, each wristband takes two satin threads, so five wristbands require five groups of two threads: two plus two plus two plus two plus two, yielding ten threads in total. "
            "Finally, each wristband needs four golden beads. Five wristbands take five groups of four beads: four plus four plus four plus four plus four, totaling twenty shiny beads. "
            "Notice how calculating materials for multiple craft units naturally leads us to combine equal groups repeatedly and methodically. "
            "This systematic inventory calculation prevents material shortages and ensures every handmade wristband is crafted with uniform beauty. "
            "Use the craft material simulator to assemble wristbands and see how material totals scale smoothly across your workbench."
        ),
        "checkpoints": [
            {
                "question": "How many satin threads are required to assemble 5 wristbands if each takes 2 threads?",
                "options": ["8 threads", "10 threads", "12 threads", "15 threads"],
                "answer": 1,
                "hint": "Add 2 five times: 2 + 2 + 2 + 2 + 2.",
                "explanation": "Five wristbands needing 2 threads each require 5 × 2 = 10 satin threads."
            },
            {
                "question": "How many golden beads are needed for 5 wristbands when each wristband uses 4 beads?",
                "options": ["16 beads", "25 beads", "20 beads", "24 beads"],
                "answer": 2,
                "hint": "Multiply 5 wristbands by 4 beads per wristband.",
                "explanation": "Five groups of 4 beads equal 4 + 4 + 4 + 4 + 4 = 20 golden beads."
            }
        ]
    },
    {
        "id": 3,
        "title": "Repeated Addition Models",
        "subtitle": "Transforming successive additions into multiplication equations",
        "speech": (
            "In mathematics, we frequently encounter situations where the exact same number is added together multiple times in succession. "
            "When we compute two plus two plus two plus two plus two, we are adding the number two five times consecutively. "
            "Writing out long chains of addition can be tedious and time-consuming, especially when working with many groups of items. "
            "Mathematicians created multiplication as a brilliant shortcut to express repeated additions with clarity, precision, and speed. "
            "The multiplication symbol, written as a cross, represents the phrase 'groups of' or 'times'. "
            "Therefore, adding five groups of two is written succinctly as five times two equals ten. "
            "In this mathematical sentence, the number five tells us the number of equal groups, while the number two tells us how many items belong in each group. "
            "The resulting product, ten, represents the combined total across all groups. "
            "Similarly, four plus four plus four plus four plus four is simply five groups of four, written as five times four equals twenty. "
            "Understanding that multiplication is fundamentally repeated addition gives you the conceptual power to master all multiplication tables with confidence. "
            "Experiment with the interactive converter to transform repeated addition chains into compact multiplication formulas."
        ),
        "checkpoints": [
            {
                "question": "Which multiplication expression represents the repeated addition 3 + 3 + 3 + 3 + 3 + 3?",
                "options": ["3 × 5", "6 × 3", "6 + 3", "3 × 3"],
                "answer": 1,
                "hint": "Count how many times the number 3 is added.",
                "explanation": "The number 3 is added 6 times consecutively, so it is written as 6 × 3 = 18."
            },
            {
                "question": "In the multiplication sentence 4 × 7 = 28, what does the number 4 represent?",
                "options": ["The total number of items", "The number of equal groups", "The number of items in each group", "The difference between numbers"],
                "answer": 1,
                "hint": "The first factor specifies how many groups are being multiplied.",
                "explanation": "In 4 × 7 = 28, 4 indicates the number of equal groups, 7 is the size of each group, and 28 is the total product."
            }
        ]
    },
    {
        "id": 4,
        "title": "Scaling Craft Units",
        "subtitle": "Extending production requirements and solving reverse material puzzles",
        "speech": (
            "Now let us extend our craft planning to larger batches and explore fascinating reverse reasoning challenges together. "
            "Suppose our community festive workshop decides to craft ten wristbands instead of five for an upcoming festival gathering. "
            "Because ten is exactly double five, every single material requirement doubles in perfect, predictable proportion. "
            "Ten wristbands requiring two satin threads each will need ten times two, which equals twenty threads in total. "
            "Similarly, ten wristbands requiring four beads each will demand ten times four, yielding forty sparkling beads altogether. "
            "Now consider an intriguing reverse problem: if our craft box contains twenty-four sparkling beads, how many complete wristbands can we assemble? "
            "Since each wristband requires four beads, we ask ourselves: how many groups of four make twenty-four? "
            "We can count by fours systematically: four, eight, twelve, sixteen, twenty, twenty-four. That gives six equal groups of four. "
            "Therefore, twenty-four beads are sufficient to construct exactly six complete wristbands without any shortage. "
            "This reverse thinking is the direct conceptual bridge connecting multiplication to division in everyday practical math. "
            "Multiplication scales up our unit groups to find a total, whereas reverse division breaks a known total into equal unit portions. "
            "Use the craft inventory workbench to adjust batch sliders, test material constraints, and solve reverse assembly puzzles."
        ),
        "checkpoints": [
            {
                "question": "How many wristbands can be made using 32 beads if each wristband requires 4 beads?",
                "options": ["6 wristbands", "7 wristbands", "8 wristbands", "9 wristbands"],
                "answer": 2,
                "hint": "Determine how many 4s are needed to reach 32: 32 ÷ 4.",
                "explanation": "Since 8 × 4 = 32, thirty-two beads can produce exactly 8 complete wristbands."
            },
            {
                "question": "If you need to make 10 wristbands and each takes 1 flower, 2 threads, and 4 beads, what is the total items count?",
                "options": ["50 items", "60 items", "70 items", "80 items"],
                "answer": 2,
                "hint": "Each wristband takes 1 + 2 + 4 = 7 items. Multiply 10 by 7.",
                "explanation": "One wristband requires 1 + 2 + 4 = 7 items. For 10 wristbands, 10 × 7 = 70 total craft items."
            }
        ]
    },
    {
        "id": 5,
        "title": "Rectangular Sweet Boxes",
        "subtitle": "Arranging festive confections in structured rows and columns",
        "speech": (
            "During joyful festive celebrations, sweet shops prepare delightful treats called laddoos packed in elegant rectangular gift boxes. "
            "When fresh sweets are placed inside a gift box, they are organized in regular rows and columns rather than piled in messy heaps. "
            "A confectioner packs a square box with three rows of laddoos, placing three laddoos in each row. "
            "To count the total, we multiply three rows by three columns: three times three equals nine laddoos. "
            "In another box, eighteen laddoos are arranged in two long rows with nine laddoos in each row, giving two times nine equals eighteen sweets. "
            "A third box holds the same eighteen laddoos in six shorter rows with three confections per row: six times three equals eighteen. "
            "Notice something truly remarkable here: the exact same quantity of eighteen sweets can be structured into completely different rectangular arrays! "
            "Whether arranged as two rows of nine or six rows of three, the total quantity of sweets remains perfectly unchanged. "
            "Rectangular arrays provide an intuitive visual representation of multiplication factors, showing clearly how different factor pairs produce identical products. "
            "Interact with the sweet shop array simulator to adjust rows and columns, packing delicious confections into various rectangular formats."
        ),
        "checkpoints": [
            {
                "question": "A sweet box contains 4 rows of pedas with 5 pedas in each row. How many pedas are in the box?",
                "options": ["16 pedas", "20 pedas", "24 pedas", "25 pedas"],
                "answer": 1,
                "hint": "Multiply the number of rows by the number of columns: 4 × 5.",
                "explanation": "Four rows with 5 pedas in each row give 4 × 5 = 20 pedas in total."
            },
            {
                "question": "Which two factor pairs both produce an array of 18 laddoos?",
                "options": ["2 × 9 and 6 × 3", "3 × 5 and 4 × 4", "2 × 8 and 3 × 7", "5 × 3 and 6 × 2"],
                "answer": 0,
                "hint": "Calculate the products: 2 × 9 = 18 and 6 × 3 = 18.",
                "explanation": "Both 2 × 9 and 6 × 3 equal 18, showing different ways to arrange 18 objects in a rectangular grid."
            }
        ]
    },
    {
        "id": 6,
        "title": "Equal Fair Sharing",
        "subtitle": "Introducing division through equal distribution among family and friends",
        "speech": (
            "Festivals are celebrations of joy, generosity, and thoughtful sharing among beloved family members and visiting neighbors. "
            "Imagine eighteen delicious laddoos freshly packed in a platter waiting to be distributed equally among nine eager guests. "
            "To ensure fairness, every single guest must receive the exact same number of sweets without any remaining leftovers. "
            "We begin sharing by placing one laddoo on each guest's plate, using up nine laddoos. "
            "Because nine laddoos still remain on the platter, we distribute a second laddoo to each person. "
            "Now all eighteen sweets are gone, and every one of the nine guests has received exactly two laddoos. "
            "In mathematics, this process of equal distribution is called division. "
            "We write this sharing event as eighteen divided by nine equals two, using the division symbol of a horizontal bar with dots. "
            "The number eighteen represents the total dividend being shared, nine represents the divisor indicating the number of equal shares, and two is the quotient representing the size of each share. "
            "Division is the exact inverse operation of multiplication, since nine groups of two bring us right back to eighteen. "
            "Use the fair sharing simulator to distribute sweets equally across plates and watch the division equation form dynamically."
        ),
        "checkpoints": [
            {
                "question": "If 18 laddoos are shared equally among 9 people, how many laddoos does each person get?",
                "options": ["1 laddoo", "2 laddoos", "3 laddoos", "4 laddoos"],
                "answer": 1,
                "hint": "Divide 18 by 9: 18 ÷ 9.",
                "explanation": "Eighteen divided equally among 9 people gives 18 ÷ 9 = 2 laddoos per person."
            },
            {
                "question": "What is the mathematical term for the total number being divided in a sharing problem?",
                "options": ["Divisor", "Dividend", "Quotient", "Remainder"],
                "answer": 1,
                "hint": "In 18 ÷ 9 = 2, 18 is the number being split.",
                "explanation": "The total amount being divided is called the dividend (in this example, 18)."
            }
        ]
    },
    {
        "id": 7,
        "title": "Sharing on Plates",
        "subtitle": "Distributing diamond sweets and milk pedas through step-by-step subtraction",
        "speech": (
            "Let us deepen our understanding of equal distribution with other traditional festive confections like diamond-cut kaju katlis and milk pedas. "
            "Suppose a decorative serving platter contains twenty delicate diamond-shaped sweets that must be shared equally among five friends. "
            "How can we distribute them methodically? We can think of fair sharing as repeated subtraction in successive rounds. "
            "First, we give one sweet to each of the five friends, subtracting five from twenty, leaving fifteen sweets on the platter. "
            "We give a second round of five sweets, leaving ten. A third round leaves five, and a fourth round leaves zero sweets remaining. "
            "Because we completed four full rounds of distribution, each friend receives four diamond sweets: twenty divided by five equals four. "
            "Now consider fifteen round milk pedas distributed equally among the same five friends. "
            "Giving one peda each uses five, leaving ten. Giving a second round uses five, leaving five. Giving a third round leaves zero. "
            "Each friend receives three milk pedas: fifteen divided by five equals three. "
            "Drawing plates and placing one treat on each plate sequentially demonstrates that division is repeated equal sharing. "
            "Practice distributing sweets onto interactive plates, tracking each round of subtraction until the platter is happily and cleanly cleared."
        ),
        "checkpoints": [
            {
                "question": "When 20 diamond sweets are shared equally among 5 plates, how many sweets rest on each plate?",
                "options": ["3 sweets", "4 sweets", "5 sweets", "6 sweets"],
                "answer": 1,
                "hint": "Calculate 20 ÷ 5 or determine what number multiplied by 5 gives 20.",
                "explanation": "Twenty divided by 5 equals 4, so each plate holds 4 sweets."
            },
            {
                "question": "How many rounds of distribution take place when sharing 15 pedas equally among 5 people?",
                "options": ["2 rounds", "3 rounds", "4 rounds", "5 rounds"],
                "answer": 1,
                "hint": "Subtract 5 repeatedly from 15: 15 - 5 - 5 - 5 = 0.",
                "explanation": "Subtracting 5 three times reduces 15 to 0, which corresponds to 3 rounds of distribution (15 ÷ 5 = 3)."
            }
        ]
    },
    {
        "id": 8,
        "title": "Pair Division Puzzles",
        "subtitle": "Solving division challenges with bicycle wheels and coiled sweet groups",
        "speech": (
            "Everyday objects provide wonderful opportunities to solve practical division and grouping puzzles all around us. "
            "Consider a festive bicycle repair workshop that has twelve brand new rubber tyres ready to be fitted onto bicycles. "
            "Since every standard bicycle requires exactly two wheels to roll properly, how many complete bicycles can be fitted? "
            "To solve this, we divide the twelve wheels into equal groups of two: twelve divided by two equals six bicycles. "
            "Each bicycle takes one pair of wheels, so twelve wheels furnish exactly six bicycles. "
            "Next, think of a confectioner preparing golden coiled jalebis fried in swirling groups of four. "
            "If a customer orders twenty-four jalebis, how many clusters of four must the confectioner scoop from the frying pan? "
            "Dividing twenty-four by four gives six clusters, because six times four equals twenty-four. "
            "Notice how both problems involve dividing a known total into groups of a fixed size to determine how many groups exist. "
            "This is another vital aspect of division called measurement or quotative division. "
            "Whether pairing wheels on bicycles or grouping sweet spirals on trays, grouping logic makes arithmetic intuitive and practical. "
            "Explore the bicycle wheel and jalebi pairing simulator to group items into sets and observe division rules in action."
        ),
        "checkpoints": [
            {
                "question": "A mechanic has 14 wheels. How many two-wheeled bicycles can be assembled?",
                "options": ["5 bicycles", "6 bicycles", "7 bicycles", "8 bicycles"],
                "answer": 2,
                "hint": "Divide the total wheels by 2: 14 ÷ 2.",
                "explanation": "Fourteen wheels divided by 2 wheels per bicycle equals 7 complete bicycles."
            },
            {
                "question": "If sweet jalebis are packed in boxes of 4, how many boxes are filled by 28 jalebis?",
                "options": ["6 boxes", "7 boxes", "8 boxes", "9 boxes"],
                "answer": 1,
                "hint": "Find how many 4s are in 28: 28 ÷ 4.",
                "explanation": "Twenty-eight divided by 4 equals 7, so 28 jalebis fill exactly 7 boxes."
            }
        ]
    }
]

if __name__ == "__main__":
    for s in slides_part1:
        wc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({len(s['title'].split())} words) -> Speech: {wc} words")
        assert 195 <= wc <= 215, f"Slide {s['id']} speech out of range: {wc}"
        assert len(s["title"].split()) <= 3, f"Slide {s['id']} title too long"
        assert len(s["checkpoints"]) == 2, f"Slide {s['id']} must have 2 checkpoints"
    print("Part 1 verified successfully!")
