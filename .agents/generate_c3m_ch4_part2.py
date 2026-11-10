# -*- coding: utf-8 -*-
"""Part 2 (Slides 9-16) for Class 3 Mathematics Chapter 4: Vacation with My Nani Maa."""

import json
import re

slides_part2 = [
    {
        "id": 9,
        "title": "Decade Hop Jumps",
        "badge": "Frog & Grasshopper Leaps",
        "sim_id": "sim_decade_hop_jumps",
        "description": "Master forward and backward jumps of ten on open number lines inspired by leaping garden creatures.",
        "speech": (
            "In lush vacation gardens, nimble green frogs and lively grasshoppers perform marvelous leaping feats across moist earth and river stones. "
            "Mathematicians take inspiration from these graceful creatures to master decade hops of ten on the number line! When a frog begins "
            "at stone twenty-four and leaps forward by ten, notice what happens: twenty-four plus ten lands directly on thirty-four. If it leaps "
            "forward by another ten, it reaches forty-four, and another leap brings it to fifty-four! Observe the fascinating numerical pattern: "
            "the ones digit four remains entirely constant and undisturbed, while the tens digit smoothly increments by one with each forward hop. "
            "Now imagine a startled grasshopper hopping backward from seventy-eight! One backward leap of ten lands on sixty-eight, the next "
            "backward leap lands on fifty-eight, and a third backward leap lands cleanly on forty-eight. Once again, the ones digit eight never "
            "shifts, while the tens digit counts steadily downward. Practicing these decade hops trains your mind to navigate the number line with "
            "effortless agility. Whether you are adding fifty, subtracting thirty, or calculating change during shopping trips, thinking in leaps "
            "of ten gives your mathematical reasoning unmatched speed, clarity, deep precision, and joyful confidence on every problem you solve!"
        ),
        "checkpoints": [
            {
                "q": "Starting at 36, where do two forward leaps of 10 land?",
                "options": ["56", "46", "66", "38"],
                "ans": "56",
                "explanation": "36 + 10 = 46, and 46 + 10 = 56."
            },
            {
                "q": "Starting at 83, what is the result after three backward leaps of 10?",
                "options": ["53", "63", "73", "43"],
                "ans": "53",
                "explanation": "83 - 10 = 73, 73 - 10 = 63, and 63 - 10 = 53."
            }
        ]
    },
    {
        "id": 10,
        "title": "Hidden Leaf Puzzles",
        "badge": "Garden Estimation",
        "sim_id": "sim_hidden_leaf_puzzles",
        "description": "Estimate and calculate hidden ant colonies and garden creatures sheltered beneath broad fallen leaves.",
        "speech": (
            "Underneath broad fallen mango leaves in peaceful country gardens, industrious ant colonies scurry about their daily work with amazing "
            "organization. Suppose we observe thirty-five tiny ants actively marching across the sandy garden pathway in a disciplined line. "
            "Nearby, a wide green leaf shelters an unseen group of their foraging nest mates. If an investigator knows with absolute certainty "
            "that fifty ants belong to this specific foraging team in total, how many industrious ants are sheltered beneath the leaf? Once "
            "again, our powerful subtraction strategy solves the hidden mystery! Subtracting the thirty-five visible marching ants from the known "
            "total of fifty uncovers the hidden colony: fifty minus thirty-five leaves exactly fifteen ants resting quietly in the cool shade! "
            "Before calculating exact numbers, sharp thinkers always make a sensible estimation. Since thirty-five is clearly more than half of "
            "fifty, we know immediately that the hidden group must be smaller than twenty-five. Estimation acts as a trusty intellectual compass, "
            "guiding your thoughts and guarding against careless errors. Combining smart estimation with precise subtraction allows you to observe "
            "natural phenomena, verify mathematical hypotheses, and uncover hidden numerical truths across the living world with elegance, grace, "
            "and total accuracy in every inquiry!"
        ),
        "checkpoints": [
            {
                "q": "If 50 ants are in a group and 35 are visible outside, how many are under the leaf?",
                "options": ["15 ants", "25 ants", "12 ants", "20 ants"],
                "ans": "15 ants",
                "explanation": "50 - 35 = 15 ants hidden beneath the broad leaf."
            },
            {
                "q": "Why is estimating before calculating useful in mathematical investigations?",
                "options": [
                    "It provides a sensible benchmark to check the exact result",
                    "It replaces the need to calculate",
                    "It always makes the answer zero",
                    "It changes addition to division"
                ],
                "ans": "It provides a sensible benchmark to check the exact result",
                "explanation": "Estimation sets an expected range, helping identify and prevent calculation mistakes."
            }
        ]
    },
    {
        "id": 11,
        "title": "Hundred Grid Navigation",
        "badge": "Directional Arrow Steps",
        "sim_id": "sim_hundred_grid_navigation",
        "description": "Navigate a 1-to-100 number square using cardinal directional arrows for decade jumps and single steps.",
        "speech": (
            "A standard hundred grid arranges the numbers from one to one hundred into ten tidy horizontal rows of ten numbers each. This "
            "brilliant grid layout transforms complex arithmetic operations into intuitive spatial movements across a geometric board! Imagine "
            "your game counter rests on number forty-five. Moving one cell to the right represents adding one, landing directly on forty-six. "
            "Moving one cell to the left represents subtracting one, landing on forty-four. Now look at the vertical movements, which are truly "
            "magical! Moving one cell straight down drops you into the exact same column in the row below, which adds exactly ten, landing on "
            "fifty-five! Conversely, moving one cell straight up lifts you into the row above, subtracting ten and landing cleanly on thirty-five. "
            "Mathematicians encode these movements using simple directional arrow codes! For example, starting at forty-five, the code "
            "Down-Down-Right tells you to add ten, add ten, and add one: forty-five plus twenty-one equals sixty-six! Navigating the number grid "
            "with arrow paths builds strong spatial intuition for our base-ten decimal system, proving that adding and subtracting are joyful, "
            "visual journeys across structured mathematical terrain that anyone can master with ongoing practice, lively enthusiasm, and clear logic!"
        ),
        "checkpoints": [
            {
                "q": "On a 100-grid, what mathematical operation does moving one cell straight down represent?",
                "options": ["Add 10 (+10)", "Subtract 10 (-10)", "Add 1 (+1)", "Multiply by 10"],
                "ans": "Add 10 (+10)",
                "explanation": "Each row below contains numbers exactly 10 greater, so moving down adds 10."
            },
            {
                "q": "Starting at 54, if you follow arrows [Up, Right], on which number do you land?",
                "options": ["45", "43", "65", "64"],
                "ans": "45",
                "explanation": "Starting at 54, Up subtracts 10 (54 - 10 = 44), and Right adds 1 (44 + 1 = 45)."
            }
        ]
    },
    {
        "id": 12,
        "title": "Grid Race Game",
        "badge": "Strategic Number Racing",
        "sim_id": "sim_grid_race_game",
        "description": "Compete in a strategic 1-to-100 grid board race using dice combinations and tactical forward/backward moves.",
        "speech": (
            "Board games played with friends and family turn mathematical calculation into thrilling, memorable adventures full of laughter! "
            "In the Grid Race Game, two players begin at cell number one on the hundred chart, competing eagerly to be the first to reach the "
            "victory zone between ninety-one and one hundred. On each turn, a player rolls two dice, displaying numbers like three and five. "
            "The player can choose to form either thirty-five or fifty-three, and then decide whether to add or subtract that two-digit number "
            "from their current position! This freedom introduces rich tactical strategy. If you are sitting on cell forty-two and roll three "
            "and five, forming thirty-five and adding it propels you forward to cell seventy-seven! But be careful: if a move would push you past "
            "one hundred, you cannot take it, requiring you to subtract or choose the alternate digit order instead. Playing the grid race sharpens "
            "mental addition and subtraction of two-digit numbers while developing long-range foresight and probabilistic reasoning. Every turn "
            "presents meaningful numerical choices that make arithmetic come alive as an exciting, friendly contest of intellect, calculation speed, "
            "tactical ingenuity, and lasting strategic mastery for all participants and observers alike!"
        ),
        "checkpoints": [
            {
                "q": "If you are on cell 42 and add 35, what is your new board position?",
                "options": ["77", "67", "87", "75"],
                "ans": "77",
                "explanation": "42 + 35 = 77 (42 + 30 = 72, and 72 + 5 = 77)."
            },
            {
                "q": "Rolling digits 2 and 6 lets you form either 26 or 62. Which move advances you further forward?",
                "options": [
                    "Adding 62, because 62 is 36 greater than 26",
                    "Adding 26, because smaller numbers are faster",
                    "Both moves advance the same distance",
                    "Neither move advances forward"
                ],
                "ans": "Adding 62, because 62 is 36 greater than 26",
                "explanation": "Adding 62 provides a much larger forward leap than adding 26, advancing you 36 cells further."
            }
        ]
    },
    {
        "id": 13,
        "title": "Magic Square Matrix",
        "badge": "Equal Sum Symmetry",
        "sim_id": "sim_magic_square_matrix",
        "description": "Investigate the mysterious balanced symmetry of a classic three-by-three magic square summing to fifteen.",
        "speech": (
            "Ancient mathematicians across India and Asia were captivated by harmonious numerical grids called magic squares! A classic three-by-three "
            "magic square arranges the nine digits from one through nine in a square grid so that every horizontal row, every vertical column, "
            "and both corner diagonals add up to the exact same magic constant: fifteen! Let us explore how this marvel works. The number five sits "
            "peacefully at the very center of the grid, acting as the master balancing anchor. Along the top row, we place eight, one, and six: "
            "eight plus one plus six equals fifteen! In the middle row, three, five, and seven add up to fifteen. In the bottom row, four, nine, "
            "and two also add up to fifteen! Now check the columns: eight plus three plus four equals fifteen! Check the main diagonal: eight plus "
            "five plus two equals fifteen! Every single pathway through this grid balances perfectly. Magic squares demonstrate that numbers "
            "possess profound structural symmetries and hidden mathematical beauty. Solving missing cells in a magic square requires finding "
            "complementary addends that satisfy multiple equations simultaneously, turning arithmetic into an exquisite puzzle of pure balance, "
            "unbroken symmetry, logic, and enduring intellectual delight for every thinker!"
        ),
        "checkpoints": [
            {
                "q": "What is the constant magic sum of every row, column, and diagonal in a standard 1-9 magic square?",
                "options": ["15", "18", "12", "20"],
                "ans": "15",
                "explanation": "In a 3x3 magic square with numbers 1 to 9, every line adds up to exactly 15."
            },
            {
                "q": "Which number must occupy the central cell to maintain balanced symmetry in a 1-9 magic square?",
                "options": ["5", "1", "9", "3"],
                "ans": "5",
                "explanation": "5 is the exact median of digits 1 through 9, so it must sit at the center to balance all lines."
            }
        ]
    },
    {
        "id": 14,
        "title": "Radish Harvest Bundles",
        "badge": "Two-Digit Bundle Addition",
        "sim_id": "sim_radish_harvest_bundles",
        "description": "Harvest crisp red and white radishes, combining twenty-five and thirty-six using tens bundles and ones sticks.",
        "speech": (
            "Harvesting fresh vegetables from country garden soil is a delightful morning activity filled with healthy mathematical discoveries! "
            "Imagine harvesting twenty-five crisp red radishes and thirty-six crunchy white radishes from adjoining garden plots. To find the grand "
            "harvest total, we must compute twenty-five plus thirty-six. Let us represent these numbers using bundles of ten and single loose radishes! "
            "Twenty-five decomposes into two bundles of ten and five loose radishes. Thirty-six decomposes into three bundles of ten and six loose "
            "radishes. First, combine all the bundles: two tens plus three tens give five tens, representing fifty radishes. Next, look at the loose "
            "radishes: five plus six equals eleven loose radishes! Notice what happens: eleven is greater than nine, meaning we can tie ten loose "
            "radishes together with string to form a brand new bundle of ten, leaving just one single loose radish! Adding this new bundle to our "
            "five bundles gives six full tens, and combining that with our one loose radish produces sixty-one! Regrouping ten ones into a new ten "
            "is the heartbeat of multi-digit addition, ensuring your calculations stay organized, visual, logical, dependable, and completely error-free "
            "in every practical task you undertake across your mathematical learning journey!"
        ),
        "checkpoints": [
            {
                "q": "What is the total harvest when combining 25 red radishes and 36 white radishes?",
                "options": ["61 radishes", "51 radishes", "60 radishes", "71 radishes"],
                "ans": "61 radishes",
                "explanation": "25 + 36 = 61 (20 + 30 = 50, and 5 + 6 = 11, giving 50 + 11 = 61)."
            },
            {
                "q": "Why does adding 5 loose radishes and 6 loose radishes trigger regrouping?",
                "options": [
                    "Because 5 + 6 = 11, which forms 1 ten bundle and 1 loose stick",
                    "Because 11 is less than 10",
                    "Because radishes cannot be added",
                    "Because tens bundles must always be untied"
                ],
                "ans": "Because 5 + 6 = 11, which forms 1 ten bundle and 1 loose stick",
                "explanation": "Whenever ones total 10 or more, 10 ones are bundled into a new ten, leaving the remainder in the ones place."
            }
        ]
    },
    {
        "id": 15,
        "title": "Vegetable Crate Complements",
        "badge": "Target 100 Complement",
        "sim_id": "sim_vegetable_crate_complements",
        "description": "Fill a hundred-capacity vegetable storage crate, finding how many carrots complete a crate holding sixty-five tomatoes.",
        "speech": (
            "Proper vegetable storage requires organized wooden crates designed to hold exactly one hundred farm items in ten neat compartments. "
            "Suppose a grower loads sixty-five ripe red tomatoes into a crate, and wishes to fill all remaining spaces with fresh orange carrots. "
            "How many carrots are needed to fill the hundred-item crate to the brim? Mathematically, we are solving: sixty-five plus what unknown "
            "number equals one hundred? Finding complements to one hundred is a master skill in mental arithmetic! We can solve this with a two-step "
            "mental jump. Start at sixty-five. First, take five steps forward to reach the friendly benchmark of seventy: sixty-five plus five "
            "is seventy. Now, observe the remaining distance from seventy to one hundred: it is three full tens, or thirty! Combining our two "
            "jumps, five plus thirty equals thirty-five. Therefore, exactly thirty-five carrots are required to complete the crate! You can check "
            "this by adding tens and ones: sixty plus thirty is ninety, and five plus five is ten; ninety plus ten equals one hundred. Thinking in "
            "friendly complements to one hundred makes commercial transactions, inventory tracking, and mental calculations swift, effortless, "
            "deeply satisfying, and profoundly empowering in all real-world applications!"
        ),
        "checkpoints": [
            {
                "q": "How many carrots are needed to complete a 100-item crate holding 65 tomatoes (65 + ? = 100)?",
                "options": ["35 carrots", "45 carrots", "25 carrots", "30 carrots"],
                "ans": "35 carrots",
                "explanation": "65 + 5 = 70, and 70 + 30 = 100, so 5 + 30 = 35 carrots."
            },
            {
                "q": "Which pair of numbers are complementary partners that add up to 100?",
                "options": ["65 and 35", "65 and 45", "75 and 35", "60 and 30"],
                "ans": "65 and 35",
                "explanation": "65 + 35 = 100, making them complementary partners to 100."
            }
        ]
    },
    {
        "id": 16,
        "title": "Apple Harvest Comparison",
        "badge": "Three-Digit Addition & Margin",
        "sim_id": "sim_apple_harvest_comparison",
        "description": "Calculate total orchard apples plucked and determine the exact comparative margin between two collection baskets.",
        "speech": (
            "In fruit orchards during late vacation harvest, red apples hang heavy from leafy branches, ready for collection. Suppose two "
            "diligent orchard helpers pluck sweet apples into wicker baskets: one basket holds eighty-five crisp apples, while a second basket "
            "holds sixty-seven apples. To discover the combined bounty, we add eighty-five and sixty-seven. Decompose by place value: eighty "
            "plus sixty gives one hundred forty, and five plus seven gives twelve! Adding one hundred forty and twelve yields a grand harvest "
            "total of one hundred fifty-two apples! Now consider a comparative question: who collected more apples, and by what exact margin? "
            "Comparing eighty-five and sixty-seven requires subtraction: eighty-five minus sixty-seven. We can jump back from eighty-five: "
            "subtract sixty to reach twenty-five, then subtract seven to land on eighteen! The first basket holds exactly eighteen more apples "
            "than the second basket. Notice how the same numbers yield two completely different insights depending on whether you combine "
            "them through addition or contrast them through subtraction. Mastering both operations gives you total command over real-world data, "
            "completing your vacation mathematics journey with brilliance, pride, and supreme mathematical confidence for all future adventures "
            "in learning and wondrous mathematical discovery with joyful mastery!"
        ),
        "checkpoints": [
            {
                "q": "What is the combined total of 85 apples and 67 apples (85 + 67)?",
                "options": ["152 apples", "142 apples", "162 apples", "150 apples"],
                "ans": "152 apples",
                "explanation": "80 + 60 = 140, and 5 + 7 = 12. 140 + 12 = 152 apples."
            },
            {
                "q": "By how many apples does a basket of 85 exceed a basket of 67 (85 - 67)?",
                "options": ["18 apples", "16 apples", "22 apples", "12 apples"],
                "ans": "18 apples",
                "explanation": "85 - 67 = 18 apples is the difference margin."
            }
        ]
    }
]

FORBIDDEN_CHARACTERS = ['Deba', 'Deep', 'Teji', 'Jojo', 'Raghav', 'Meera', 'Dhruv', 'Pihu', 'Chirag', 'Nandini', 'Nani Maa', 'Nani']
FORBIDDEN_PERSONAS = [r'\bDr\b', r'\bDr\.\b', r'\bSir\b', r'\bMadam\b', r'\bMr\b', r'\bMr\.\b', r'\bMrs\b', r'\bMrs\.\b', r'\bMiss\b']

if __name__ == "__main__":
    print("=== VERIFYING SLIDES 9 TO 16 (PART 2) ===")
    for s in slides_part2:
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
            if name.lower() == 'deep':
                assert not re.search(r'\bDeep\b', s_str), f"Slide {sid} contains character name '{name}'"
            else:
                assert not re.search(r'\b' + re.escape(name) + r"'?s?\b", s_str, re.IGNORECASE), f"Slide {sid} contains character name '{name}'"
        for persona in FORBIDDEN_PERSONAS:
            assert not re.search(persona, s_str, re.IGNORECASE), f"Slide {sid} contains persona '{persona}'"

    print("All slides 9 to 16 passed verification perfectly!")
