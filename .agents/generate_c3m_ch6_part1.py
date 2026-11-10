# -*- coding: utf-8 -*-
"""Part 1 (Slides 1-8) for Class 3 Mathematics Chapter 6: House of Hundreds - 1."""

import json
import re

slides_part1 = [
    {
        "id": 1,
        "title": "Counting Festival Torans",
        "badge": "Counting Beyond 200",
        "sim_id": "sim_counting_festival_torans",
        "description": "Group festive decorative triangular torans into sets of ten to count smoothly past two hundred up to two-fifty.",
        "speech": (
            "Welcome enthusiastic mathematicians to our vibrant house of hundreds laboratory exploring numbers across our everyday world! Imagine "
            "entering a festive village fair where colorful strings of triangular decorations, known as torans, stretch gracefully across fairground stalls. "
            "When counting such extensive decorations, tallying each individual flag one by one would take far too long. Instead, smart mathematicians "
            "organize items into tidy, manageable groups of ten flags each! We already know that two hundred consists of twenty full groups of ten. "
            "Now look at the festive line continuing right past that landmark. Adding one more ten-string brings our total count to two hundred and ten. "
            "Another string adds ten more, climbing smoothly to two hundred and twenty. Continuing this rhythmic decade counting—two hundred thirty, two "
            "hundred forty, and finally two hundred fifty—we discover exactly twenty-five complete strings of ten flags each! Notice how our familiar counting "
            "patterns from one to fifty simply repeat themselves with the proud prefix of two hundred. Grouping quantities into structured tens creates visual "
            "clarity, prevents counting errors, and makes estimating grand festival displays both swift and enjoyable. Practice toggling the decorative "
            "toran strings on screen to master decade counting beyond two hundred with confidence and speed!"
        ),
        "checkpoints": [
            {
                "q": "How many groups of 10 triangular torans are needed to make 250 torans in total?",
                "options": ["25 groups of 10", "20 groups of 10", "15 groups of 10", "30 groups of 10"],
                "ans": "25 groups of 10",
                "explanation": "Since 25 × 10 = 250, exactly 25 groups of 10 make up 250 torans."
            },
            {
                "q": "What number comes immediately next when counting forward by tens from 230?",
                "options": ["240", "231", "250", "220"],
                "ans": "240",
                "explanation": "Counting forward in steps of ten from 230 leads directly to 230 + 10 = 240."
            }
        ]
    },
    {
        "id": 2,
        "title": "Reaching Three Hundred",
        "badge": "The 300 Milestone",
        "sim_id": "sim_reaching_three_hundred",
        "description": "Track rows of glass bangles and boxes of sweet toffees to cross the critical century threshold of three hundred.",
        "speech": (
            "Let us continue through the fairground stalls to inspect rows of shimmering glass bangles and boxes of sweet toffees. At a busy bangle "
            "stall, twenty-eight velvet display rods hold ten bangles each, giving an impressive total of two hundred and eighty bangles. Nearby, "
            "a sweet vendor arranges boxes of delicious fruit toffees. His large crates hold two hundred and ninety-eight sweet candies. Watch closely "
            "what happens when a friendly customer adds just two more single toffees to the open crate on the counter! Adding one single toffee takes "
            "us from two hundred ninety-eight to two hundred ninety-nine. Now, adding one final single toffee triggers a magnificent mathematical "
            "milestone: two hundred ninety-nine plus one equals exactly three hundred! Think about what just happened across our place value columns. "
            "The ones column reached ten, triggering an immediate regrouping into the neighboring tens column. The tens column now held ten tens, which "
            "regrouped once again into the hundreds column to form three full hundreds! Three hundred represents thirty complete bundles of ten, or three "
            "hundred individual loose units gathered together. Click the toffee counter on your screen to add single sweets one by one and celebrate "
            "reaching the majestic three hundred milestone today!"
        ),
        "checkpoints": [
            {
                "q": "What is 299 + 1?",
                "options": ["300", "2910", "200", "301"],
                "ans": "300",
                "explanation": "Adding 1 to 299 completes the third hundred, giving exactly 300."
            },
            {
                "q": "How many bundles of 10 make up the milestone number 300?",
                "options": ["30 bundles of 10", "20 bundles of 10", "10 bundles of 10", "300 bundles of 10"],
                "ans": "30 bundles of 10",
                "explanation": "Since 30 × 10 = 300, exactly 30 bundles of ten equal 300."
            }
        ]
    },
    {
        "id": 3,
        "title": "Tiled Number Paths",
        "badge": "Missing Number Sequences",
        "sim_id": "sim_tiled_number_paths",
        "description": "Fill in missing stepping stone numerals across consecutive three-digit pathways navigating between 211 and 310.",
        "speech": (
            "Winding through the lush fairground garden is an ancient stone pathway where every single paving stone is carved with a distinct three-digit "
            "numeral. However, heavy morning footsteps and colorful fallen autumn leaves have completely obscured several numbers along the stone path! "
            "To restore the sequence, we rely on consecutive number order and place value consistency. Consider the stone sequence beginning at two hundred "
            "and eleven. The next stone is two hundred and twelve, followed by two hundred and thirteen. If an empty stone lies blank immediately before "
            "two hundred and fifteen, our deductive logic instantly restores two hundred and fourteen without hesitation! Further down the garden path, "
            "near the three hundred milestone, stepping stones read two hundred ninety-eight, two hundred ninety-nine, and three hundred. Continuing forward "
            "into the fourth century, the path advances seamlessly: three hundred and one, three hundred and two, all the way to three hundred and ten. "
            "Notice that moving one step forward along the path always means adding one, while stepping backward always means subtracting one single unit. "
            "Inspect the interactive tiled path in our simulator, identify the hidden sequence gaps, and stamp the correct numerals into place to complete "
            "the garden trail successfully!"
        ),
        "checkpoints": [
            {
                "q": "Which number belongs in the blank space: 213, ____, 215?",
                "options": ["214", "216", "224", "204"],
                "ans": "214",
                "explanation": "The consecutive number immediately following 213 and preceding 215 is 214."
            },
            {
                "q": "What number comes immediately after 309 on a consecutive stone path?",
                "options": ["310", "308", "400", "320"],
                "ans": "310",
                "explanation": "Adding 1 to 309 gives 310."
            }
        ]
    },
    {
        "id": 4,
        "title": "Matchstick Bundle Sentences",
        "badge": "Verbal Place Value",
        "sim_id": "sim_matchstick_bundle_sentences",
        "description": "Translate concrete matchstick bundles of hundreds, tens, and singles into expressive mathematical sentences.",
        "speech": (
            "Matchsticks provide a wonderful concrete physical model for visualizing and manipulating three-digit numbers in foundational arithmetic. "
            "Imagine large tied bundles containing one hundred sticks each, smaller tied bundles containing ten sticks each, and loose individual sticks. "
            "When we observe two large bundles of one hundred alongside three bundles of ten and five loose sticks resting on a table, what total number "
            "does this represent? Two hundreds plus thirty plus five gives two hundred and thirty-five! In mathematics, we can express this exact same "
            "quantity in varied descriptive verbal sentences that highlight different numerical relationships. We can describe it as 'two hundred and thirty-five "
            "more', or analyze it relative to nearby landmarks by saying it is 'fifteen less than two hundred and fifty'. Expressing numbers through flexible "
            "word sentences deepens our mental number sense. For instance, 'twenty more than two hundred' immediately identifies two hundred and twenty, while "
            "'five less than three hundred' points unerringly to two hundred and ninety-five on any number chart. By linking visual bundle groups with spoken "
            "language and algebraic expressions, we transform static numerals into dynamic mathematical concepts. Build custom matchstick combinations on "
            "screen and discover all their matching mathematical sentences with complete ease!"
        ),
        "checkpoints": [
            {
                "q": "What number is represented by '200 and 35 more'?",
                "options": ["235", "253", "2035", "230"],
                "ans": "235",
                "explanation": "200 + 35 = 235."
            },
            {
                "q": "Which number is described as '15 less than 250'?",
                "options": ["235", "245", "265", "225"],
                "ans": "235",
                "explanation": "Subtracting 15 from 250 gives 250 - 15 = 235."
            }
        ]
    },
    {
        "id": 5,
        "title": "Extended Number Line",
        "badge": "Number Line 0 to 350",
        "sim_id": "sim_extended_number_line",
        "description": "Calibrate and locate three-digit numbers across a continuous number line extending from zero to three-fifty.",
        "speech": (
            "A number line is an endless mathematical highway where every single number occupies an exact, immutable geometric position along the path. "
            "Look at this beautifully calibrated extended number line stretching smoothly from zero all the way to three hundred and fifty units. Major century "
            "milestones—one hundred, two hundred, and three hundred—stand like tall, illuminated highway towers spaced at equal intervals. Between two hundred "
            "and three hundred lies a crucial midway anchor checkpoint: two hundred and fifty. Where would you plot two hundred and seventy-five? Because "
            "seventy-five is halfway between fifty and one hundred, the value two hundred seventy-five sits precisely midway between two hundred fifty and "
            "three hundred! Similarly, the value two hundred and twenty-five rests exactly halfway between two hundred and two hundred fifty. Using these "
            "major benchmark landmarks allows us to estimate the geometric location of any three-digit value with remarkable precision and confidence. "
            "A number line also visualizes relative distance: we can clearly see that two hundred ninety is much closer to three hundred than it is to the "
            "distant milestone of two hundred. Drag the interactive pointer along our calibrated number line to plot target values and observe their spatial relationships right now!"
        ),
        "checkpoints": [
            {
                "q": "Which number sits exactly halfway between 200 and 300 on a number line?",
                "options": ["250", "225", "275", "260"],
                "ans": "250",
                "explanation": "The midpoint between 200 and 300 is 200 + 50 = 250."
            },
            {
                "q": "Is the number 290 closer to 200 or to 300 on the number line?",
                "options": ["Closer to 300", "Closer to 200", "Exactly in the middle", "Cannot be determined"],
                "ans": "Closer to 300",
                "explanation": "290 is only 10 units away from 300, but 90 units away from 200, so it is much closer to 300."
            }
        ]
    },
    {
        "id": 6,
        "title": "Number Slider Hops",
        "badge": "Mental Arithmetic Sliders",
        "sim_id": "sim_number_slider_hops",
        "description": "Perform rapid mental additions and subtractions of ones, tens, and twenties using calibrated slider mechanisms.",
        "speech": (
            "Mental agility with three-digit numbers flourishes rapidly when we learn to execute controlled jumps along calibrated virtual number tracks. "
            "Imagine an interactive mechanical slider handle resting comfortably at the baseline value of two hundred and forty. If we push the slider "
            "forward by a single unit, it advances immediately to two hundred forty-one on our track. If we pull it backward by a single unit, it retreats smoothly "
            "to two hundred thirty-nine. But we can also make much larger strides! Jumping forward by a full ten increases only the central tens digit, moving our "
            "position swiftly from two hundred forty to two hundred fifty. What exciting transformation occurs if we leap forward by twenty units? Adding "
            "twenty to two hundred forty propels us forward by two tens, landing squarely at two hundred and sixty! Conversely, leaping backward by twenty "
            "from two hundred sixty returns us smoothly and unerringly to two hundred forty. Notice how these multi-step slider jumps allow us to navigate "
            "swiftly and accurately across the vast three-digit number landscape without tedious one-by-one counting. Practice executing jumps of plus ten, minus ten, plus twenty, and minus twenty "
            "on our interactive track to develop lightning-fast mental arithmetic skills today!"
        ),
        "checkpoints": [
            {
                "q": "Starting at 240, what is the resulting number after jumping forward by 20?",
                "options": ["260", "250", "270", "220"],
                "ans": "260",
                "explanation": "240 + 20 = 260."
            },
            {
                "q": "What number do you reach if you jump backward by 10 from 275?",
                "options": ["265", "285", "255", "270"],
                "ans": "265",
                "explanation": "275 - 10 = 265."
            }
        ]
    },
    {
        "id": 7,
        "title": "The Flag Game",
        "badge": "Binary Search Deduction",
        "sim_id": "sim_the_flag_game",
        "description": "Deduce secret numbers between 200 and 210 using higher or lower feedback clues along a flagged number line.",
        "speech": (
            "Step up to our festival game arena for a thrilling mathematical guessing challenge known as The Flag Game! A mystery number lies secretly "
            "concealed somewhere along the calibrated number line between two hundred and two hundred and ten. Your task is to deduce this hidden value "
            "using the fewest possible guesses. Suppose your very first test guess is the midpoint value: two hundred and five. If the game raises a golden "
            "flag indicating 'Higher', you instantly learn that the mystery number must be greater than two hundred and five! In a single clever move, you "
            "have eliminated two hundred, two hundred one, two, three, four, and five. The secret number must now be two hundred six, two hundred seven, "
            "eight, nine, or ten. Next, you strategically guess two hundred and eight. If a crimson flag signals 'Lower', the target must lie strictly "
            "between two hundred five and two hundred eight! That leaves only two hundred six or two hundred seven. This powerful mathematical deductive "
            "method of systematically halving remaining possibilities is called binary search in modern computer science. Play The Flag Game in our interactive "
            "simulator and test your logical deduction skills against the computer right now!"
        ),
        "checkpoints": [
            {
                "q": "If the mystery number is between 200 and 210, and 205 receives a 'Higher' clue, which numbers are eliminated?",
                "options": ["200 to 205 are eliminated", "206 to 210 are eliminated", "Only 205 is eliminated", "No numbers are eliminated"],
                "ans": "200 to 205 are eliminated",
                "explanation": "A 'Higher' clue means the target is strictly greater than 205, eliminating 200 through 205."
            },
            {
                "q": "Between 205 and 208, what are the only possible integer candidates?",
                "options": ["206 and 207", "205 and 206", "207 and 208", "204 and 209"],
                "ans": "206 and 207",
                "explanation": "The integers strictly between 205 and 208 are 206 and 207."
            }
        ]
    },
    {
        "id": 8,
        "title": "Four Convergence Chain",
        "badge": "Linguistic Number Chain",
        "sim_id": "sim_four_convergence_chain",
        "description": "Explore the fascinating linguistic math puzzle where letter-counting chains invariably converge on the number four.",
        "speech": (
            "Prepare to witness a truly enchanting mathematical mystery connecting our everyday spoken language with foundational numerical values! "
            "Choose absolutely any counting number in the entire English language, large or small. Let us start together with the grand festival number "
            "two hundred and fifty. Carefully spell out the words: T-W-O H-U-N-D-R-E-D F-I-F-T-Y. Now count the total individual letters in this phrase. "
            "There are exactly sixteen letters! Next, write down the word for that count: S-I-X-T-E-E-N. Count the letters in sixteen: there are exactly "
            "seven letters! Write down the word S-E-V-E-N, which contains five letters: F-I-V-E in sequence. Now count the letters in five: there are four "
            "letters! Write down the word F-O-U-R on your page. Count the letters in four: one, two, three, four! Exactly four letters! Four points directly "
            "back to itself, creating an unbreakable infinite loop. No matter which number you begin with—whether forty, eighty-five, three hundred, or even "
            "one million—following this letter-counting chain always leads invariably to the number four! In mathematics, this fascinating phenomenon is known "
            "as an attractive fixed point. Test any starting number on our interactive word chain machine to watch it spiral gracefully into the magical "
            "number four every single time!"
        ),
        "checkpoints": [
            {
                "q": "Why is the number FOUR called a fixed point in the letter-counting word chain?",
                "options": ["Because the word 'FOUR' has exactly 4 letters", "Because 4 is an even number", "Because 4 + 4 = 8", "Because it is smaller than five"],
                "ans": "Because the word 'FOUR' has exactly 4 letters",
                "explanation": "Counting the letters in F-O-U-R gives 4, so it maps directly back onto itself in an endless loop."
            },
            {
                "q": "How many letters are in the English word 'SEVEN'?",
                "options": ["5 letters", "7 letters", "4 letters", "6 letters"],
                "ans": "5 letters",
                "explanation": "S-E-V-E-N has 5 letters (S, E, V, E, N)."
            }
        ]
    }
]

if __name__ == "__main__":
    FORBIDDEN_CHARACTERS = ['Ajji', 'Teji', 'Jojo', 'Farooq', 'Arvind', 'Raghav', 'Amma', 'Chirag', 'Nandini', 'Nani Maa', 'Nani', 'Deba', 'Deep', 'Meera', 'Dhruv', 'Pihu']
    FORBIDDEN_PERSONAS = [r'\bDr\b', r'\bDr\.\b', r'\bSir\b', r'\bMadam\b', r'\bMr\b', r'\bMr\.\b', r'\bMrs\b', r'\bMrs\.\b', r'\bMiss\b']
    
    print("Validating Part 1 (Slides 1-8)...")
    for s in slides_part1:
        sid = s["id"]
        title = s["title"]
        words = len(title.split())
        assert 1 <= words <= 3, f"Slide {sid} title '{title}' must be 1-3 words (got {words})"
        
        slide_str = json.dumps(s)
        for name in FORBIDDEN_CHARACTERS:
            if name.lower() == 'deep':
                assert not re.search(r'\bDeep\b', slide_str), f"Slide {sid} contains character name '{name}'"
            else:
                assert not re.search(r'\b' + re.escape(name) + r"'?s?\b", slide_str, re.IGNORECASE), f"Slide {sid} contains character name '{name}'"
        for persona in FORBIDDEN_PERSONAS:
            assert not re.search(persona, slide_str, re.IGNORECASE), f"Slide {sid} contains persona '{persona}'"
        
        wc = len(s["speech"].split())
        print(f"Slide {sid}: '{title}' -> Speech Word Count: {wc}")
        assert 195 <= wc <= 215, f"Slide {sid} word count out of range: {wc} (must be 195-215)"
        assert len(s["checkpoints"]) == 2, f"Slide {sid} must have 2 checkpoints"
        for cp in s["checkpoints"]:
            assert len(cp["options"]) == 4, f"Slide {sid} checkpoint must have 4 options"
            assert cp["ans"] in cp["options"], f"Slide {sid} checkpoint answer '{cp['ans']}' not in options"
    print("Part 1 validation successful!")
