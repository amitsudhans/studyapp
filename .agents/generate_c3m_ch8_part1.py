#!/usr/bin/env python3
"""
Slide Data Generator for NCERT Class 3 Mathematics - Chapter 8: Fair Share
Part 1: Slides 1 to 8
Strictly 195 - 215 words per spoken text.
1-3 word titles.
No human names (Shabnam, Mukta, Raghav, etc. removed/generalized).
No teacher personas.
"""

import json

slides_part1 = [
    {
        "id": 1,
        "title": "Sharing Equal Halves",
        "subtitle": "Discovering fair sharing and the mathematical meaning of one half",
        "speech": (
            "Welcome young mathematicians to our interactive arithmetic laboratory exploring the joyful concept of fair sharing! "
            "Imagine opening a warm lunchbox during a school break to share a fresh, round paratha and a crisp chocolate bar between two close friends. "
            "If one friend receives a tiny crumb while the other takes nearly the whole portion, everyone immediately recognizes that the division is unfair. "
            "How can we ensure that both portions are genuinely equal and fair? "
            "We can fold the round paratha directly across its center so that the two opposite curved edges match each other perfectly. "
            "When one complete object is divided into exactly two equal parts, each identical portion is known mathematically as one half. "
            "Both pieces must have the exact same shape, area, and size so that neither person receives more or less. "
            "Similarly, a chocolate bar with eight equal segments can be broken cleanly down the middle into two groups of four segments each. "
            "Four pieces out of eight make up exactly one half of the entire chocolate bar. "
            "Fair sharing means that every participant receives an identical share without any leftover remainder. "
            "Explore the interactive paratha and chocolate folding workbench to divide wholesome items into perfectly equal halves."
        ),
        "checkpoints": [
            {
                "question": "When an object is divided into two parts to make halves, what condition MUST be true?",
                "options": ["The two parts must be completely equal in size", "One part must be larger than the other", "The parts can be any random size", "There must be at least three parts"],
                "answer": 0,
                "hint": "Halves only exist when both pieces are identical in size.",
                "explanation": "To be called halves, the whole must be divided into exactly two equal parts."
            },
            {
                "question": "A chocolate bar has 8 equal blocks. How many blocks make up one half of the bar?",
                "options": ["2 blocks", "3 blocks", "4 blocks", "5 blocks"],
                "answer": 2,
                "hint": "Divide 8 blocks equally between 2 people: 8 ÷ 2.",
                "explanation": "Eight divided into two equal parts gives 8 ÷ 2 = 4 blocks for each half."
            }
        ]
    },
    {
        "id": 2,
        "title": "Identifying Half Shapes",
        "subtitle": "Distinguishing equal halves from unequal geometric slices",
        "speech": (
            "Not every cut through a shape creates equal halves; mathematical precision requires verifying whether the dividing boundary splits the area symmetrically and fairly. "
            "Consider a round pancake sliced with a straight line. "
            "If the cutting line passes directly through the exact center point, it creates two identical semicircles that match each other like mirror reflections. "
            "However, if the cut is made near the outer crust, it produces one tiny sliver and one oversized portion, which are not true halves at all. "
            "We observe the same geometric rule across rectangles, triangles, and squares. "
            "A rectangle cut by a vertical line down its midpoint produces two congruent smaller rectangles, each representing one half of the original area. "
            "Similarly, cutting a square diagonally from one corner to the opposite corner creates two identical triangles, each having half the square's surface. "
            "When evaluating whether a shaded region represents half of a shape, examine whether the colored area equals the uncolored area. "
            "If folding along the dividing line causes both regions to overlap completely, the shape is accurately divided in half. "
            "Interact with the shape inspector on screen to test various slicing angles and classify cuts as genuine halves or unequal slices."
        ),
        "checkpoints": [
            {
                "question": "Which cut divides a circle into two equal halves?",
                "options": ["A line passing directly through the center", "A curved line near the outer edge", "A short line near the top rim", "Any arbitrary diagonal scratch"],
                "answer": 0,
                "hint": "A cut through the center divides a circle into equal semicircles.",
                "explanation": "A straight cut passing through the exact center (the diameter) splits a circle into two equal halves."
            },
            {
                "question": "If a square is cut along its diagonal from corner to corner, what shapes form the two halves?",
                "options": ["Two equal circles", "Two equal triangles", "Two unequal rectangles", "Four tiny squares"],
                "answer": 1,
                "hint": "Cutting a square corner-to-corner produces triangular halves.",
                "explanation": "A diagonal cut through a square produces two congruent right-angled triangles, each being half the square."
            }
        ]
    },
    {
        "id": 3,
        "title": "Symmetry Half Reflections",
        "subtitle": "Completing mirror images and calculating remaining portions of crunchy treats",
        "speech": (
            "Halves possess a magical connection to symmetry, where one half acts as a faithful mirror image of the other half in nature and geometry. "
            "Imagine seeing a drawing of a butterfly or a festive kite where only the left half is sketched upon the page. "
            "Because butterflies have symmetrical bodies, we can complete the entire picture by drawing an exact mirror reflection across the central vertical line. "
            "Every antenna, wing pattern, and colorful spot on the left side is mirrored identically on the right side to build a complete whole. "
            "Now consider a crisp rectangular peanut brittle treat called chikki. "
            "Suppose a snack is divided into four equal vertical strips. "
            "If someone nibbles away one strip from the left side and one strip from the right side, two strips have been eaten out of four. "
            "Since two is half of four, exactly one half of the chikki has been consumed, leaving one half remaining in the center! "
            "Whether portions are eaten from opposite sides, the top, or the bottom, we count the total equal units to determine the fractional share. "
            "Use the mirror canvas simulator to draw symmetrical reflections and calculate the remaining fractions of delicious crispy snacks."
        ),
        "checkpoints": [
            {
                "question": "A butterfly drawing has 3 dots on its left wing. How many dots must be on the right wing for symmetry?",
                "options": ["1 dot", "2 dots", "3 dots", "6 dots"],
                "answer": 2,
                "hint": "Symmetrical mirror halves must have identical counts and features.",
                "explanation": "In bilateral symmetry, the right half mirrors the left half exactly, so it must also have 3 dots."
            },
            {
                "question": "A snack bar is divided into 4 equal pieces. If 2 pieces are eaten, what fraction remains?",
                "options": ["One quarter", "One half", "The whole bar", "Zero"],
                "answer": 1,
                "hint": "4 pieces minus 2 pieces leaves 2 pieces. Compare 2 to 4.",
                "explanation": "Two pieces remain out of four. Since 2 is half of 4, exactly one half of the bar remains."
            }
        ]
    },
    {
        "id": 4,
        "title": "Paper Folding Halves",
        "subtitle": "Exploring multiple geometric folding paths to create equal halves on square sheets",
        "speech": (
            "Can a single sheet of paper be divided into two equal halves in more than one way? Let us investigate through hands-on paper folding! "
            "Take a clean square sheet of origami craft paper resting flat upon your desk. "
            "First, fold the paper horizontally by bringing the bottom edge up to meet the top edge, creating a sharp crease across the middle. "
            "Unfolding reveals two identical horizontal rectangles, each representing one half of the square. "
            "Now unfold the paper and fold it vertically by bringing the left edge over to meet the right edge. "
            "This produces two tall vertical rectangles, which are also equal halves of the same square! "
            "Next, try folding diagonally by bringing the bottom-left corner across to meet the top-right corner. "
            "Creasing and unfolding now reveals two large congruent triangles, each having the exact same area as the rectangular halves! "
            "We can even fold along the opposite diagonal to find yet another pair of triangular halves. "
            "This proves a profound geometric principle: the halves of a shape do not have to look like identical shapes as long as their surface areas are strictly equal. "
            "Experiment with the digital origami simulator to fold sheets along horizontal, vertical, and diagonal crease lines."
        ),
        "checkpoints": [
            {
                "question": "How many different straight crease lines can divide a square into two identical halves?",
                "options": ["Only 1 line", "Only 2 lines", "At least 4 lines (horizontal, vertical, and two diagonals)", "Zero lines"],
                "answer": 2,
                "hint": "Count the folding ways: across, down, and two corner-to-corner folds.",
                "explanation": "A square can be folded in half horizontally, vertically, and along either of its two diagonals (4 primary lines of symmetry)."
            },
            {
                "question": "Do two halves of a square always have to be rectangles?",
                "options": ["Yes, halves can only be rectangles", "No, diagonal folds create two equal triangular halves", "Yes, circles are the only other option", "No, halves must always be squares"],
                "answer": 1,
                "hint": "Folding a square from corner to corner forms triangles.",
                "explanation": "Diagonal folds produce two equal right-angled triangles, each covering exactly half the square's area."
            }
        ]
    },
    {
        "id": 5,
        "title": "Fair Distribution Dilemma",
        "subtitle": "Evaluating fairness in seasonal and time-based resource sharing challenges",
        "speech": (
            "Mathematics helps us evaluate fairness not only in physical food portions but also in complex real-world resource sharing dilemmas. "
            "Consider a famous village fable about an elderly father who divided three precious family possessions between two quarreling brothers. "
            "The father offered the first brother the top canopy of a mango tree with its sweet fruits, while the second brother received the roots. "
            "For a warm woolen blanket, one brother was allowed to use it during the hot daytime, while the other held it during freezing cold nights. "
            "For a shared solar lantern, one brother kept it outdoors under the bright noon sun, while the other brother used it in the dark night. "
            "At first glance, each brother received one half of every item, but was the distribution truly fair? "
            "The brother with the tree canopy enjoyed delicious mangoes while the roots required hard watering without any fruit. "
            "A blanket is useless in the scorching day but vital at night; a lantern is useless in broad daylight but essential after sunset. "
            "True fairness requires that both shares offer equal benefit, value, and utility, not just a superficial division of parts. "
            "Use the dilemma analyzer to examine resource conditions, test sharing arrangements, and propose genuine fair solutions."
        ),
        "checkpoints": [
            {
                "question": "Why is sharing a blanket only during the day while another uses it at night unfair?",
                "options": ["Because a blanket is only needed for warmth at night", "Because daytime is longer than nighttime", "Because blankets cannot be shared", "Because wool shrinks in the sun"],
                "answer": 0,
                "hint": "Consider when a blanket provides actual utility and comfort.",
                "explanation": "A blanket is essential during cold nights but useless in the warm day, making the division unequal in practical value."
            },
            {
                "question": "What is required for a division of resources to be genuinely fair?",
                "options": ["Giving all valuable parts to one person", "Both shares must provide equal value, benefit, and fairness", "Dividing things randomly without discussion", "Only sharing items that can be eaten"],
                "answer": 1,
                "hint": "Fairness means equal benefit and utility for all participants.",
                "explanation": "True fair sharing ensures that all parties receive equal practical value and utility from their shares."
            }
        ]
    },
    {
        "id": 6,
        "title": "Sharing Discrete Objects",
        "subtitle": "Distributing discrete collections of mangoes equally between two groups",
        "speech": (
            "So far we have explored dividing continuous single objects like pancakes, but fair sharing also applies to collections of separate individual items. "
            "Imagine a wicker basket filled with eight ripe, fragrant yellow mangoes gathered fresh from an orchard tree. "
            "Two children wish to share this entire basket of mangoes completely and fairly between themselves. "
            "How do we divide a collection of separate items into two equal halves? "
            "We distribute the mangoes one by one, placing one mango in the first basket and one in the second basket repeatedly. "
            "When all eight mangoes are distributed, each child holds four mangoes in their basket. "
            "We say that four mangoes represent one half of the collection of eight mangoes. "
            "In arithmetic, finding half of a group is identical to dividing the total count by two: eight divided by two equals four. "
            "If the basket had twelve mangoes, sharing them equally would give six mangoes to each child, because twelve divided by two equals six. "
            "Whenever we divide a countable quantity into two equal groups, each group contains half of the original total. "
            "Use the mango basket simulator to drag fruits into sharing bowls and observe how division by two creates equal halves."
        ),
        "checkpoints": [
            {
                "question": "If 10 juicy mangoes are shared equally between 2 children, how many mangoes does each child receive?",
                "options": ["4 mangoes", "5 mangoes", "6 mangoes", "8 mangoes"],
                "answer": 1,
                "hint": "Divide 10 by 2: 10 ÷ 2.",
                "explanation": "Ten mangoes divided equally into two groups gives 10 ÷ 2 = 5 mangoes each."
            },
            {
                "question": "What mathematical operation finds half of any countable collection of objects?",
                "options": ["Multiplying by 2", "Dividing by 2", "Adding 2", "Subtracting 4"],
                "answer": 1,
                "hint": "Splitting into 2 equal parts is division by 2.",
                "explanation": "Dividing the total quantity by 2 calculates the exact size of one half."
            }
        ]
    },
    {
        "id": 7,
        "title": "Halves and Doubles",
        "subtitle": "Understanding the reciprocal mathematical relationship between doubling and halving",
        "speech": (
            "In arithmetic, halving and doubling are two sides of the exact same mathematical coin, working as inverse operations of each other. "
            "Let us explore this reciprocal relationship using shiny glass marbles scattered across a playing circle. "
            "Suppose one child has three marbles, and another child has double that amount. "
            "To double a quantity, we take two identical groups of that number: three plus three, or two times three, which equals six marbles. "
            "Now look at the relationship in reverse: if six marbles are shared equally into two groups, each group contains three marbles. "
            "Therefore, we can state with absolute mathematical certainty: three is half of six, and six is double of three! "
            "Consider another example: if you hold four marbles, doubling them gives eight marbles. "
            "In reverse, four marbles are half of eight marbles. "
            "Whenever you know the half of a number, you can immediately double it to find the original whole. "
            "Conversely, whenever you double a number, dividing the product by two returns you right back to your starting value. "
            "Mastering this reciprocal bridge between halves and doubles accelerates your mental math calculation skills dramatically. "
            "Practice pairing marble jars on screen to see how doubling and halving balance each other in perfect harmony."
        ),
        "checkpoints": [
            {
                "question": "If 5 is half of a secret number, what is the secret number?",
                "options": ["8", "10", "12", "15"],
                "answer": 1,
                "hint": "Double the number 5: 5 + 5 or 2 × 5.",
                "explanation": "If 5 is half, then the whole is double of 5, which is 5 × 2 = 10."
            },
            {
                "question": "What is the relationship between the numbers 7 and 14?",
                "options": ["7 is double of 14", "7 is half of 14, and 14 is double of 7", "14 is half of 7", "7 and 14 have no relationship"],
                "answer": 1,
                "hint": "7 × 2 = 14, and 14 ÷ 2 = 7.",
                "explanation": "Seven is half of 14, and 14 is double of 7, demonstrating the inverse relationship."
            }
        ]
    },
    {
        "id": 8,
        "title": "Number Line Proportions",
        "subtitle": "Locating halves and doubles visually along an extended coordinate track",
        "speech": (
            "A number line provides a wonderful visual pathway to see how halves and doubles relate to distance and spatial coordinates. "
            "Imagine an extended number track starting at zero and stretching smoothly forward past sixteen units. "
            "If a marker starts at zero and travels a distance of eight units, where is the halfway mark of that journey? "
            "We divide eight by two: eight divided by two equals four. "
            "Looking at our number line, the number four sits precisely midway between zero and eight! "
            "The distance from zero to four is four units, and the distance from four to eight is also four units. "
            "Now look in the opposite direction: if you are standing at stone six, what is double that distance from zero? "
            "We double six by leaping forward another six units: six plus six equals twelve. "
            "The marker lands squarely on twelve, showing that twelve is double of six, and six is half of twelve. "
            "We can test any even number along the track: half of fourteen is seven, half of sixteen is eight, and half of ten is five. "
            "The number line proves that halving cuts distance exactly into two equal segments. "
            "Use the interactive number line hopper to test midpoints, double your strides, and locate proportional landmarks."
        ),
        "checkpoints": [
            {
                "question": "On a number line from 0 to 16, which number marks the exact halfway point of the entire distance?",
                "options": ["6", "7", "8", "9"],
                "answer": 2,
                "hint": "Find half of 16: 16 ÷ 2.",
                "explanation": "Half of 16 is 16 ÷ 2 = 8, which sits exactly midway between 0 and 16."
            },
            {
                "question": "Starting at 0, if you take a jump of 7 units and then double your distance, where do you land?",
                "options": ["12", "14", "15", "16"],
                "answer": 1,
                "hint": "Double 7: 7 × 2 = 14.",
                "explanation": "Doubling a distance of 7 units leads to 7 + 7 = 14 on the number line."
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
