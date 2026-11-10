# -*- coding: utf-8 -*-
"""Part 1 (Slides 1-8) for Class 3 Mathematics Chapter 4: Vacation with My Nani Maa."""

import json
import re

slides_part1 = [
    {
        "id": 1,
        "title": "Hidden Marble Trick",
        "badge": "Missing Part Subtraction",
        "sim_id": "sim_hidden_marble_trick",
        "description": "Discover how subtraction reveals unknown hidden quantities when total and visible amounts are known.",
        "speech": (
            "Welcome young mathematicians to our vacation laboratory! Imagine a fascinating guessing trick performed with smooth glass "
            "marbles and a patterned handkerchief spread across a table. A total of fifteen shiny marbles are carefully counted onto the "
            "smooth wooden surface. When a cloth suddenly covers some of them, exactly nine marbles remain visible in the open daylight. "
            "How can we determine how many marbles lie concealed underneath without peeking at all? Subtraction is our trusted secret key! "
            "When we know the entire total collection and one visible part, subtracting that visible part instantly uncovers the hidden "
            "remainder. Fifteen minus nine equals six, proving beyond doubt that exactly six marbles lie quietly concealed beneath the cloth. "
            "We can immediately verify this mathematical thinking through addition, because nine visible marbles plus six hidden marbles "
            "reconstitute our complete original set of fifteen. This fundamental mathematical principle applies across all counting tasks. "
            "Whether tracking tamarind seeds, river pebbles, wooden buttons, or shiny metal coins, subtraction always helps us find missing "
            "complementary parts up to sums of twenty, thirty, or beyond. Notice how addition and subtraction are two complementary sides of "
            "the very same numerical coin. By observing what is openly present, your sharp mathematical reasoning effortlessly solves the "
            "intriguing mystery of what remains unseen!"
        ),
        "checkpoints": [
            {
                "q": "If there are 20 seeds in total and 13 are visible on the table, how many are hidden?",
                "options": ["7 seeds", "6 seeds", "8 seeds", "13 seeds"],
                "ans": "7 seeds",
                "explanation": "Subtracting the visible seeds from the total (20 - 13 = 7) gives exactly 7 hidden seeds."
            },
            {
                "q": "Which addition fact proves that 15 minus 9 leaves 6 hidden marbles?",
                "options": ["9 + 6 = 15", "15 + 9 = 24", "9 - 6 = 3", "15 + 6 = 21"],
                "ans": "9 + 6 = 15",
                "explanation": "Because 9 visible marbles plus 6 hidden marbles equal the original 15 marbles, 9 + 6 = 15 verifies the subtraction."
            }
        ]
    },
    {
        "id": 2,
        "title": "Balushahi Sweet Counts",
        "badge": "Combining & Eating Sweets",
        "sim_id": "sim_balushahi_sweet_counts",
        "description": "Calculate total sweets brought for a celebration and track remaining portions after tasting.",
        "speech": (
            "During joyful holiday visits, traditional sweet delicacies called balushahi bring warm smiles to everyone around the busy "
            "family dining table. Imagine one small cardboard box holds seven fresh, flaky balushahis, while a second box contains five "
            "more golden sweets. To discover the combined bounty of delicious treats, we perform straightforward addition: seven plus five "
            "gives twelve delectable sweets in total! We can visualize this clearly by starting at seven and making five forward steps along a "
            "counting path, landing precisely on twelve. But what happens later in the afternoon when family members enjoy four of these "
            "golden sweets during teatime? Whenever items are eaten, shared, or removed, the overall quantity decreases, requiring direct "
            "subtraction. Twelve minus four leaves exactly eight balushahis safely resting in the ceramic serving platter. Notice how these "
            "two operations mirror real-world actions in daily life. Combining separate batches creates a larger sum through addition, "
            "whereas sharing or consuming portions reduces the total through subtraction. You can always double-check your calculation backward "
            "by adding the four consumed sweets back to the eight remaining sweets, which neatly restores our twelve original sweets. Practice "
            "combining different tasty treat quantities and calculating what remains with total confidence!"
        ),
        "checkpoints": [
            {
                "q": "If you combine 8 golden balushahis with 6 fresh ones, what is the total count?",
                "options": ["14 sweets", "12 sweets", "15 sweets", "13 sweets"],
                "ans": "14 sweets",
                "explanation": "Adding 8 and 6 gives 14 sweets (8 + 6 = 14)."
            },
            {
                "q": "Out of 14 sweets, if 5 sweets are eaten during afternoon tea, how many remain?",
                "options": ["9 sweets", "8 sweets", "10 sweets", "11 sweets"],
                "ans": "9 sweets",
                "explanation": "Subtracting the 5 consumed sweets from 14 leaves 9 sweets (14 - 5 = 9)."
            }
        ]
    },
    {
        "id": 3,
        "title": "Story Books Total",
        "badge": "Ten Frame Bridging",
        "sim_id": "sim_story_books_total",
        "description": "Combine storybooks and puzzle books using a ten-frame visual grid to make friendly decade totals.",
        "speech": (
            "Reading books during quiet vacation afternoons offers wonderful adventures and stimulating brain puzzles for curious young minds. "
            "Suppose a traveler packs nine engaging storybooks alongside seven intriguing puzzle books into a sturdy cloth travel satchel. "
            "How many splendid books are there altogether? While we could slowly count each book one by one, mathematicians love using a "
            "clever visual tool called a ten-frame grid! A ten-frame organizes items into two balanced rows of five spaces each. Place the "
            "nine storybooks into the first ten-frame. Notice immediately that only one single empty slot is needed to complete a full ten! "
            "We can borrow one puzzle book from our group of seven to fill that empty slot, leaving six puzzle books outside. Now the "
            "calculation becomes crystal clear: ten plus six equals sixteen! Making a benchmark ten is one of the most powerful mental "
            "arithmetic strategies you will ever learn. Instead of struggling with difficult finger counting, borrowing a small amount to "
            "complete ten transforms addition into an effortless mental reflex. The total sixteen is now decomposed into one ten and six "
            "ones, matching our base-ten number system perfectly and setting you up for larger calculations across all branches of learning!"
        ),
        "checkpoints": [
            {
                "q": "How does decomposing 7 into 1 and 6 help add 9 + 7 on a ten-frame?",
                "options": [
                    "9 + 1 makes a full 10, then 10 + 6 = 16",
                    "It subtracts 1 from 9 to leave 8",
                    "It turns 7 into 70",
                    "It replaces 9 with 0"
                ],
                "ans": "9 + 1 makes a full 10, then 10 + 6 = 16",
                "explanation": "Giving 1 from 7 to 9 completes a full ten-frame (10), and adding the remaining 6 gives 16."
            },
            {
                "q": "If a collection has 8 adventure books and 5 science books, what is the sum using make-a-ten?",
                "options": ["13 books", "12 books", "14 books", "15 books"],
                "ans": "13 books",
                "explanation": "8 needs 2 to make 10. Taking 2 from 5 leaves 3, so 10 + 3 = 13 books."
            }
        ]
    },
    {
        "id": 4,
        "title": "Card Equation Triplets",
        "badge": "Fact Family Triangles",
        "sim_id": "sim_card_equation_triplets",
        "description": "Group number cards into connected triplets that unlock four related addition and subtraction facts.",
        "speech": (
            "Playing card games on a quiet holiday evening reveals rich numerical harmony and pattern beauty. Consider three numbered cards "
            "bearing the numerals seven, eight, and fifteen. These three numbers are not random strangers; they form an inseparable mathematical "
            "family called a fact family triplet! From these three numbers alone, we can construct four distinct true equations. First, adding "
            "seven and eight produces fifteen. Second, by the commutative property of addition, changing the order so eight comes first still "
            "produces the exact same sum of fifteen. Now observe the reverse direction using subtraction! Starting from the total of fifteen, "
            "subtracting seven leaves eight. Likewise, starting from fifteen and subtracting eight leaves seven. Every addition fact carries its "
            "exact subtraction partners within it. Understanding number triplets empowers you to solve missing-number puzzles in a flash. If "
            "you see a problem asking what number added to eight yields fifteen, you instantly remember your triplet partner seven! Card games "
            "teach us that numbers are interconnected webs of relationships, where knowing one single fact instantly hands you three others "
            "for free, making mental arithmetic exciting, highly reliable, and richly rewarding whenever you calculate in everyday situations with friends and family members!"
        ),
        "checkpoints": [
            {
                "q": "Which number card completes the fact family triplet with 6 and 14?",
                "options": ["8", "7", "9", "20"],
                "ans": "8",
                "explanation": "6 + 8 = 14, so 8 is the missing complementary member of this fact family triplet."
            },
            {
                "q": "Which subtraction sentence belongs to the fact family of 7, 8, and 15?",
                "options": ["15 - 8 = 7", "15 - 5 = 10", "8 - 7 = 1", "15 + 7 = 22"],
                "ans": "15 - 8 = 7",
                "explanation": "15 - 8 = 7 directly connects the three family members: total 15 minus part 8 equals part 7."
            }
        ]
    },
    {
        "id": 5,
        "title": "Bead String Strategies",
        "badge": "Ginladi Addition Paths",
        "sim_id": "sim_bead_string_strategies",
        "description": "Explore three flexible mental paths to add fifteen and seven along a traditional bead string.",
        "speech": (
            "A ginladi is a traditional hundred-bead string with alternating groups of ten red and ten white beads. It serves as an open "
            "playground for exploring different mental math pathways! Let us solve fifteen plus seven using three distinct strategies. The "
            "first approach is stepping by single units: begin at bead fifteen, then count forward seven individual beads, landing right at "
            "twenty-two. While dependable, counting by ones can be slow. The second strategy is friendly bridging: notice that fifteen needs "
            "five more beads to reach the decade landmark of twenty. Split seven into five and two. First jump five forward to land cleanly "
            "on twenty, then jump the remaining two to arrive at twenty-two! The third approach is the compensation leap: seven is very close "
            "to ten, just three less. So leap forward by a whole ten from fifteen to land at twenty-five, then step backward by three to correct "
            "the overshoot, landing squarely at twenty-two! All three routes reach the identical destination, showing that mathematics celebrates "
            "creative, flexible thinking. Choose the path that feels most natural, swift, and comfortable for your personal thinking style, "
            "as having multiple reliable strategies is the true mark of a master mathematical investigator!"
        ),
        "checkpoints": [
            {
                "q": "In the friendly bridging strategy for 15 + 7, how is the number 7 split?",
                "options": [
                    "Into 5 and 2 (to reach 20 first)",
                    "Into 3 and 4",
                    "Into 6 and 1",
                    "Into 7 and 0"
                ],
                "ans": "Into 5 and 2 (to reach 20 first)",
                "explanation": "Splitting 7 into 5 and 2 lets us jump 15 + 5 = 20, then 20 + 2 = 22."
            },
            {
                "q": "In the compensation strategy, jumping +10 from 15 gives 25. How much must you step back to add 7?",
                "options": ["3 steps back", "2 steps back", "4 steps back", "1 step back"],
                "ans": "3 steps back",
                "explanation": "Because 10 is 3 greater than 7, jumping +10 overshoots by 3, so we subtract 3 (25 - 3 = 22)."
            }
        ]
    },
    {
        "id": 6,
        "title": "Adding Larger Bundles",
        "badge": "Tens Jumps to Fifty-Two",
        "sim_id": "sim_adding_larger_bundles",
        "description": "Add substantial decade bundles of thirty to twenty-two using tens-place jumps and matchstick bundles.",
        "speech": (
            "Collecting postal stamps from different historical eras and faraway places is an inspiring hobby that sparks our curiosity. "
            "Imagine an album already contains twenty-two precious stamps carefully pasted in neat rows. A visiting relative presents a "
            "generous gift packet holding thirty brand new stamps! How many stamps are in the growing collection now? We need to calculate "
            "twenty-two plus thirty. Look closely at the digits: thirty consists of three full tens and zero ones. Because there are no loose "
            "ones to add, our ones digit two remains completely untouched! All we must do is add the tens: two tens plus three tens equal "
            "five tens. Combining five tens with our two ones gives fifty-two! On a bead string or open number line, this looks like three "
            "joyful leaps of ten starting from twenty-two: twenty-two plus ten is thirty-two, plus ten is forty-two, plus ten is fifty-two! "
            "Understanding that decade numbers only modify the tens column allows you to compute additions of twenty, thirty, or forty almost "
            "instantly in your head without paper. Large additions become simple, confident leaps across the open number line every single time "
            "you encounter clean round decades in your everyday mathematical investigations and practical calculations!"
        ),
        "checkpoints": [
            {
                "q": "What is 22 + 30 computed by jumping in three tens?",
                "options": ["52", "42", "62", "50"],
                "ans": "52",
                "explanation": "Starting at 22 and jumping three tens gives 32, 42, and 52."
            },
            {
                "q": "Why does adding 30 to 22 leave the ones digit 2 unchanged?",
                "options": [
                    "Because 30 has 0 in the ones place",
                    "Because 2 cannot be changed",
                    "Because 30 is smaller than 22",
                    "Because addition always ignores ones"
                ],
                "ans": "Because 30 has 0 in the ones place",
                "explanation": "Since 30 has zero ones, adding 0 to 2 ones leaves the ones digit as 2."
            }
        ]
    },
    {
        "id": 7,
        "title": "Backward Line Jumps",
        "badge": "Two-Digit Subtraction",
        "sim_id": "sim_backward_line_jumps",
        "description": "Subtract thirty-seven from fifty-two using strategic backward jumps across decade milestones.",
        "speech": (
            "Now let us examine the fifty-two stamps in the album more closely and discover their distinct categories. Suppose thirty-seven "
            "of these stamps display portraits of celebrated historical personalities, while all the remaining stamps feature architectural "
            "monuments. How many monument stamps are there? To uncover the answer, we must calculate fifty-two minus thirty-seven. An open "
            "number line provides the clearest path through backward leaps! First, decompose thirty-seven into three tens and seven ones. "
            "Start at fifty-two at the far right. Make three backward jumps of ten: fifty-two minus ten is forty-two, minus ten is thirty-two, "
            "and minus ten lands on twenty-two. Now we only need to subtract the remaining seven ones from twenty-two. We can split seven "
            "into two and five! Jump back two to reach the clean decade marker twenty, then jump back five more to land triumphantly on fifteen! "
            "Fifty-two minus thirty-seven equals fifteen monument stamps. Decomposing subtractions into tens leaps followed by friendly ones "
            "steps eliminates confusion and keeps your mental arithmetic grounded and accurate. Every backward jump moves you closer to "
            "mathematical clarity, confidence, and complete mastery over multi-digit subtraction, making challenging problems feel simple, "
            "orderly, transparent, and thoroughly engaging for every learner!"
        ),
        "checkpoints": [
            {
                "q": "What is the result of fifty-two minus thirty-seven (52 - 37)?",
                "options": ["15", "17", "25", "14"],
                "ans": "15",
                "explanation": "52 - 30 = 22, and 22 - 7 = 15."
            },
            {
                "q": "When subtracting 7 from 22, why is splitting 7 into 2 and 5 helpful?",
                "options": [
                    "Jumping back 2 lands on benchmark 20, then 20 - 5 = 15",
                    "It makes the answer bigger than 22",
                    "It changes subtraction into multiplication",
                    "It eliminates the need to subtract"
                ],
                "ans": "Jumping back 2 lands on benchmark 20, then 20 - 5 = 15",
                "explanation": "Subtracting 2 first hits the friendly decade marker 20, making the final step 20 - 5 = 15 easy to calculate."
            }
        ]
    },
    {
        "id": 8,
        "title": "Target Jump Projections",
        "badge": "Distance to Milestone",
        "sim_id": "sim_target_jump_projections",
        "description": "Calculate how many more stamps are required to advance from fifty-two to a target milestone of seventy-five.",
        "speech": (
            "Every enthusiastic collector sets ambitious goals for their growing treasury of items. With fifty-two stamps currently gathered, "
            "the next big milestone target is reaching seventy-five stamps! How many more stamps must be collected to achieve this goal? "
            "Mathematically, this question asks: fifty-two plus what unknown number equals seventy-five? We can solve this either as a "
            "missing-addend problem or as subtraction: seventy-five minus fifty-two. Let us journey forward from fifty-two on our open number line. "
            "First, take a solid leap of twenty forward: fifty-two plus twenty brings us directly to seventy-two. Now look at the remaining gap "
            "between seventy-two and our goal of seventy-five: it is just three single steps! Adding our forward leaps together, twenty plus "
            "three equals twenty-three. Therefore, exactly twenty-three more stamps are needed to reach seventy-five! Notice how breaking "
            "the distance into decade jumps followed by ones steps makes calculating differences between two-digit numbers delightfully "
            "straightforward, fast, and enjoyable. Whether planning personal savings, tracking sports scores, or measuring garden plant growth, "
            "calculating the distance to a future target is an essential lifelong mathematical skill you will happily use every single day of your life with "
            "utmost confidence, joy, satisfaction, and great pride!"
        ),
        "checkpoints": [
            {
                "q": "How many more are needed to reach 75 from 52 (52 + ? = 75)?",
                "options": ["23", "25", "22", "33"],
                "ans": "23",
                "explanation": "75 - 52 = 23. A jump of 20 reaches 72, and 3 more reaches 75 (20 + 3 = 23)."
            },
            {
                "q": "If you have 40 marbles and your goal is 68, what is the gap?",
                "options": ["28 marbles", "18 marbles", "38 marbles", "24 marbles"],
                "ans": "28 marbles",
                "explanation": "68 - 40 = 28 marbles needed to reach the target."
            }
        ]
    }
]

FORBIDDEN_CHARACTERS = ['Deba', 'Deep', 'Teji', 'Jojo', 'Raghav', 'Meera', 'Dhruv', 'Pihu', 'Chirag', 'Nandini', 'Nani Maa', 'Nani']
FORBIDDEN_PERSONAS = [r'\bDr\b', r'\bDr\.\b', r'\bSir\b', r'\bMadam\b', r'\bMr\b', r'\bMr\.\b', r'\bMrs\b', r'\bMrs\.\b', r'\bMiss\b']

if __name__ == "__main__":
    print("=== VERIFYING SLIDES 1 TO 8 (PART 1) ===")
    for s in slides_part1:
        sid = s['id']
        title = s['title']
        tw = len(title.split())
        assert 1 <= tw <= 3, f"Slide {sid} title '{title}' must be 1-3 words (got {tw})"
        
        words = s['speech'].split()
        wc = len(words)
        print(f"Slide {sid}: '{title}' -> {wc} words")
        assert 195 <= wc <= 215, f"Slide {sid} speech word count out of range: {wc} words"
        assert len(s['checkpoints']) == 2, f"Slide {sid} must have 2 checkpoints"
        
        s_str = json.dumps(s)
        for name in FORBIDDEN_CHARACTERS:
            assert not re.search(r'\b' + re.escape(name) + r"'?s?\b", s_str, re.IGNORECASE), f"Slide {sid} contains character name '{name}'"
        for persona in FORBIDDEN_PERSONAS:
            assert not re.search(persona, s_str, re.IGNORECASE), f"Slide {sid} contains persona '{persona}'"

    print("All slides 1 to 8 passed verification perfectly!")
