# -*- coding: utf-8 -*-
"""
Generate Slides 1 to 8 for Class 3 Mathematics - Chapter 1: What's in a Name?
Strict requirements:
- Titles: 1 to 3 words each
- Spoken text: strictly 195 to 215 words each
- Tone: Pure Indian male teacher academic, encouraging, didactic narration
- Zero human character names (no Raghav, Deba, Deep, Teji, Jojo, Meera, Dhruv, etc.)
- Zero lecturer personas (no Dr., Sir, Madam, Mr., Mrs., Miss)
- 2 checkpoints per slide with 4 options each, correct answer, and explanation
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Pre-Numerical Counting",
        "badge": "Historical Counting",
        "sim_id": "sim_prenum_cattle",
        "description": "Discover how ancient pastoral communities kept track of livestock herds through one-to-one correspondence before written numerals existed.",
        "speech": (
            "Welcome young mathematicians to our exciting journey through the origins of counting and data. "
            "Long before ancient human civilizations invented written number symbols such as one, two, or three, "
            "early pastoral communities needed dependable practical methods to keep track of their valuable domestic animals. "
            "Imagine a humble cowherd family residing near a quiet countryside village. Every morning at sunrise, "
            "the village cowherds opened the sturdy wooden corral gates to lead their herd of cows out into the lush green pastures. "
            "Because these ancient cowherds had not yet learned formal counting words or modern arithmetic symbols, "
            "they relied upon a brilliant foundational mathematical principle known as one-to-one correspondence. "
            "Before departing into the open meadows, the cowherd placed a single smooth river pebble into a clay pot "
            "for each cow that stepped through the gate. If twelve cows walked past, exactly twelve pebbles rested inside the pot. "
            "In the evening, as each cow returned through the gate, the cowherd removed one pebble from the pot. "
            "If the pot was completely empty at dusk, the cowherd knew with absolute certainty that every single animal had returned safely. "
            "This ingenious physical matching strategy demonstrates how human beings intuitively organized mathematical quantities thousands of years ago."
        ),
        "checkpoints": [
            {
                "q": "What fundamental mathematical principle allowed early pastoral cowherds to track cattle without numerals?",
                "options": [
                    "One-to-one correspondence between animals and physical markers",
                    "Memorizing multi-digit numerical formulas",
                    "Measuring the total weight of the cattle herd on a platform",
                    "Counting the footsteps made by cows in the mud"
                ],
                "ans": "One-to-one correspondence between animals and physical markers",
                "explanation": "One-to-one correspondence pairs each individual object with exactly one token, allowing quantity verification without number words."
            },
            {
                "q": "If all pebbles were removed from the clay pot upon the herd's evening return, what did it signify?",
                "options": [
                    "All cattle had returned safely from the pasture",
                    "Several cattle were still lost in the forest",
                    "Extra stray animals had joined the herd",
                    "The clay pot was broken and unusable"
                ],
                "ans": "All cattle had returned safely from the pasture",
                "explanation": "An empty pot proved that every cow that walked out in the morning had returned through the corral gate."
            }
        ]
    },
    {
        "id": 2,
        "title": "Wall Mark Tallying",
        "badge": "Tally Mark Origins",
        "sim_id": "sim_wall_tally",
        "description": "Explore how scratching vertical marks on a clay wall created durable visual records of outgoing and returning livestock.",
        "speech": (
            "As pastoral communities continued tending livestock across changing seasons, carrying heavy bags of river pebbles became inconvenient. "
            "A creative village friend proposed a far more durable recording strategy using the smooth clay walls of the cattle shed. "
            "Early in the morning, as the young cowherds prepared to guide the cattle into the grazing fields, "
            "one cowherd stood vigilantly beside the corral boundary holding a piece of sharp white chalk or charcoal. "
            "Each time a cow walked through the wooden gateway toward the meadow, the cowherd scratched a distinct vertical tally mark on the wall. "
            "Ten cows passing through the doorway resulted in ten neat vertical strokes drawn side by side upon the earthen surface. "
            "When evening shadows lengthened and the grazing herd returned from the pasture, the recording process reversed systematically. "
            "For every cow that re-entered the shed, the cowherd drew a single diagonal strike through one vertical mark on the wall. "
            "By pairing each arriving animal with an existing tally line, the cowherds created a permanent visual record that could not spill or get lost. "
            "This simple yet brilliant wall-marking technique marks the earliest invention of tally charts in the history of human mathematics."
        ),
        "checkpoints": [
            {
                "q": "How did the cowherds record each cow leaving the shed in the morning?",
                "options": [
                    "By drawing a single vertical mark on the clay wall",
                    "By carving a complex geometric picture of a cow",
                    "By writing the spoken name of each cow in ink",
                    "By tying a knot in a long silk thread"
                ],
                "ans": "By drawing a single vertical mark on the clay wall",
                "explanation": "Each departing cow was quickly and reliably represented by a single vertical stroke made with chalk or charcoal."
            },
            {
                "q": "What action was taken on the wall as each cow re-entered the shed in the evening?",
                "options": [
                    "Striking through one vertical mark to cancel it",
                    "Erasing the entire clay wall with water",
                    "Drawing two additional vertical marks beside it",
                    "Painting the entire wall with bright yellow dye"
                ],
                "ans": "Striking through one vertical mark to cancel it",
                "explanation": "Drawing a diagonal line through a vertical stroke visually cancelled it, confirming that one animal had returned."
            }
        ]
    },
    {
        "id": 3,
        "title": "Tracking Missing Cattle",
        "badge": "Problem Solving",
        "sim_id": "sim_missing_cattle",
        "description": "Learn how uncrossed tally marks immediately alerted cowherds to missing animals, prompting targeted search and rescue.",
        "speech": (
            "The true practical power of any mathematical recording system appears when unexpected real-world problems arise during daily work. "
            "Consider a dramatic evening when sunset cast long purple shadows across the Tarakeshwar village fields and farmland. "
            "The young cowherds had guided the cattle back from the distant riverside pasture and carefully cancelled marks on the shed wall. "
            "However, after all the cows inside the corral had been settled, the cowherds noticed something very important on the clay surface: "
            "two vertical marks remained completely uncrossed! Even without modern subtraction arithmetic, the physical evidence was unmistakable and urgent. "
            "Two uncancelled marks meant that exactly two cows had failed to return through the gate and remained somewhere out in the darkening pastures. "
            "Immediately realizing the danger, the village cowherds alerted the elders and organized a targeted search party carrying bright lanterns. "
            "They traced the grazing path back toward the riverbank, where they discovered two gentle cows grazing quietly near a thick grove of bamboo trees. "
            "The cowherds safely escorted the missing animals home, crossed out the final two wall marks, and rested peacefully. "
            "This real-life scenario proves how physical tally systems provide instant error detection and safeguard valuable resources without writing complex numerical equations."
        ),
        "checkpoints": [
            {
                "q": "What did two uncrossed vertical marks on the wall indicate at the end of the day?",
                "options": [
                    "Exactly two cows were missing and still out in the pasture",
                    "Two extra cows had entered the village shed",
                    "The cowherds needed to feed the cattle twice as much grass",
                    "The chalk was completely worn out"
                ],
                "ans": "Exactly two cows were missing and still out in the pasture",
                "explanation": "Because every returned cow cancelled one mark, any remaining uncrossed marks represented unreturned, missing animals."
            },
            {
                "q": "Why is the tally cancellation method an effective mathematical monitoring tool?",
                "options": [
                    "It reveals discrepancies immediately without needing complex calculations",
                    "It changes the physical color of the animals in the dark",
                    "It prevents rain from falling on the cattle shed",
                    "It makes the cattle walk much faster towards the gate"
                ],
                "ans": "It reveals discrepancies immediately without needing complex calculations",
                "explanation": "Visual tally matching instantly exposes differences between departing and arriving quantities at a glance."
            }
        ]
    },
    {
        "id": 4,
        "title": "Modern Tally Marks",
        "badge": "Grouping & Bundling",
        "sim_id": "sim_five_bundle_tally",
        "description": "Understand how grouping loose vertical marks into bundles of five revolutionized rapid counting and quantity recognition.",
        "speech": (
            "While individual vertical marks worked wonderfully for small herds of eight or nine cows, "
            "managing larger quantities soon created a serious optical challenge for the observers. "
            "When thirty or forty identical vertical lines were drawn close together across an earthen wall, "
            "the human eye struggled to count them rapidly without losing place or making accidental recounting mistakes. "
            "To overcome this visual confusion, ancient mathematicians developed the brilliant convention of grouping tallies into standardized bundles of five units each. "
            "In this modern tally system, we draw four upright vertical lines side by side: one, two, three, and four. "
            "When the fifth item arrives, instead of drawing a fifth loose vertical line, "
            "we draw a prominent diagonal slash that crosses through all four previous strokes from top-left to bottom-right! "
            "This completed bundle instantly represents a closed group of five units. "
            "Counting large numbers now becomes completely effortless because our minds can swiftly skip-count by fives: "
            "five, ten, fifteen, twenty, twenty-five, thirty, and beyond! "
            "If we observe three completed bundles alongside two single vertical strokes, we immediately calculate five plus five plus five plus two, "
            "which totals seventeen items in a mere second. Bundling transforms messy counting into organized, efficient mathematical thinking."
        ),
        "checkpoints": [
            {
                "q": "How is the number five represented in the standard modern tally mark system?",
                "options": [
                    "Four vertical lines crossed diagonally by a fifth slash",
                    "Five separate vertical lines drawn with wide gaps",
                    "A square box with a small circle inside it",
                    "Five horizontal lines stacked on top of each other"
                ],
                "ans": "Four vertical lines crossed diagonally by a fifth slash",
                "explanation": "A complete tally bundle consists of four upright vertical strokes locked together by one diagonal fifth slash."
            },
            {
                "q": "What is the primary advantage of bundling tally marks into groups of five?",
                "options": [
                    "It enables rapid skip-counting by fives without recounting individual marks",
                    "It uses less chalk on the surface of the blackboard",
                    "It makes the lines appear invisible in bright sunlight",
                    "It turns the marks into letters of the English alphabet"
                ],
                "ans": "It enables rapid skip-counting by fives without recounting individual marks",
                "explanation": "Bundling allows our brains to skip-count by fives (5, 10, 15...) which is vastly faster and less error-prone than single counting."
            }
        ]
    },
    {
        "id": 5,
        "title": "Letter Count Teams",
        "badge": "Data Sorting",
        "sim_id": "sim_animal_letter_teams",
        "description": "Classify animals into balanced sports teams by calculating the exact letter lengths of their written common names.",
        "speech": (
            "Let us now apply our growing mathematical counting skills to an entertaining forest tournament called the Team Selection Game! "
            "Imagine ten diverse animal friends gathering in an open forest clearing to play an exciting game of ball. "
            "The animals include an ox, a rat, a dog, a lion, a deer, a goat, a tiger, a snake, a monkey, and a grand elephant. "
            "To divide themselves fairly into two equal teams, the forest animals decide to use the letter counts of their written English names. "
            "First, the animals count the exact number of letters in each name: "
            "ox has two letters; rat and dog each possess three letters; lion, deer, and goat contain four letters each; "
            "tiger and snake have five letters; monkey contains six letters; and elephant boasts eight letters! "
            "The animals then establish a clear classification rule: "
            "creatures with short names containing four or fewer letters form Team A, "
            "while creatures with long names containing five or more letters join Team B. "
            "Team A proudly gathers ox, rat, dog, lion, deer, and goat, giving them six members, "
            "while Team B assembles tiger, snake, monkey, and elephant, totaling four members. "
            "Counting letters transforms everyday words into measurable numerical data for fair logical sorting."
        ),
        "checkpoints": [
            {
                "q": "How many letters are in the animal name 'ELEPHANT'?",
                "options": [
                    "8 letters",
                    "7 letters",
                    "6 letters",
                    "9 letters"
                ],
                "ans": "8 letters",
                "explanation": "Counting the individual letters E-L-E-P-H-A-N-T reveals a total of exactly eight letters."
            },
            {
                "q": "If animals with 4 or fewer letters join Team A, which animal correctly belongs to Team A?",
                "options": [
                    "GOAT (4 letters)",
                    "MONKEY (6 letters)",
                    "TIGER (5 letters)",
                    "SNAKE (5 letters)"
                ],
                "ans": "GOAT (4 letters)",
                "explanation": "G-O-A-T has 4 letters, satisfying the condition of having four or fewer letters for Team A."
            }
        ]
    },
    {
        "id": 6,
        "title": "Name Length Analysis",
        "badge": "Comparative Measurement",
        "sim_id": "sim_name_length_ruler",
        "description": "Analyze classmate names using character length rulers to determine minimum, maximum, and average letter counts.",
        "speech": (
            "When young learners examine the names of their classmates and friends, they uncover delightful mathematical patterns hidden in plain sight. "
            "Every person's name is constructed from a specific sequence of alphabet letters, "
            "and counting these letters allows us to compare name lengths just like measuring physical objects with a sturdy wooden ruler. "
            "Suppose a classroom teacher asks a group of children to write down five common Indian names on neat display cards: "
            "Om, Joy, Aman, Priya, and Shrinathan. "
            "Looking closely at each name card, the observant students count the alphabet letters systematically one by one. "
            "The shortest name in the classroom sample is Om, consisting of just two letters: O and M. "
            "Next comes Joy with three letters, followed by Aman with four letters, and Priya with five letters. "
            "At the opposite end of the spectrum, the longest name in the group is Shrinathan, containing ten complete letters! "
            "By arranging these names in ascending order of letter count, children observe a clear mathematical progression: "
            "two, three, four, five, and ten. "
            "Comparing name lengths teaches children how qualitative text can be converted into quantitative numerical data, "
            "enabling them to calculate differences, identify extremes, and understand statistical range in primary school mathematics."
        ),
        "checkpoints": [
            {
                "q": "Between the names 'OM' (2 letters) and 'SHRINATHAN' (10 letters), what is the difference in letter count?",
                "options": [
                    "8 letters",
                    "6 letters",
                    "12 letters",
                    "5 letters"
                ],
                "ans": "8 letters",
                "explanation": "Subtracting the shorter name length from the longer gives: 10 - 2 = 8 letters difference."
            },
            {
                "q": "Which of the following names has exactly five letters?",
                "options": [
                    "PRIYA",
                    "JOY",
                    "AMAN",
                    "OM"
                ],
                "ans": "PRIYA",
                "explanation": "P-R-I-Y-A contains exactly five alphabet letters."
            }
        ]
    },
    {
        "id": 7,
        "title": "Alphabet Letter Frequencies",
        "badge": "Letter Distribution",
        "sim_id": "sim_letter_frequency_sorter",
        "description": "Investigate starting letters, terminal endings, and repeating vowels across classroom name registries.",
        "speech": (
            "Beyond simply measuring overall name lengths, young statisticians can explore the internal distribution of individual alphabet characters. "
            "In every classroom attendance register across India, certain letters appear with remarkable frequency at the start or end of names. "
            "For instance, when examining a list of twenty students, children often discover that several names begin with the same initial letter, "
            "such as the letter A in Aarav, Ananya, Amit, and Anvi. "
            "Similarly, the letter S frequently introduces popular names like Sanjay, Sunil, Simran, and Shreya. "
            "By categorizing names according to their starting letter, students can create an initial-letter frequency tally chart. "
            "Furthermore, examining terminal ending letters reveals intriguing linguistic and mathematical tendencies in our regional languages: "
            "many Indian feminine names conclude with the vowel letter A or I, as seen in Priya, Neha, Pooja, and Anjali, "
            "whereas many masculine names conclude with consonants like N, R, or L, such as in Rohan, Karan, and Rahul. "
            "Students can count the frequency of each vowel—A, E, I, O, and U—across their complete friend list. "
            "Discovering which letter appears most often provides young minds with their very first introduction to the fundamental statistical concept of mode in primary data analysis."
        ),
        "checkpoints": [
            {
                "q": "What initial letter is shared by the names 'AARAV', 'ANANYA', and 'AMIT'?",
                "options": [
                    "The letter A",
                    "The letter S",
                    "The letter M",
                    "The letter R"
                ],
                "ans": "The letter A",
                "explanation": "All three names begin with the capital alphabet letter A."
            },
            {
                "q": "In statistics, what term describes the letter or item that appears with the highest frequency in a data set?",
                "options": [
                    "The mode",
                    "The perimeter",
                    "The denominator",
                    "The quotient"
                ],
                "ans": "The mode",
                "explanation": "The mode is the statistical value or category that occurs most frequently within an observed data set."
            }
        ]
    },
    {
        "id": 8,
        "title": "Number Name Cards",
        "badge": "Word Lengths",
        "sim_id": "sim_number_name_cards",
        "description": "Construct number word cards and discover the fascinating mathematical contrast between numerical value and letter count.",
        "speech": (
            "A captivating mathematical puzzle emerges when children compare the numerical value of a number with the letter count of its written name. "
            "Imagine two curious classroom students constructing colorful flashcards to represent quantities using English words and tally strokes. "
            "They write the word 'ten' on one card, 'seventeen' on another card, and 'forty-three' on a third card. "
            "At first glance, young children might intuitively expect that a bigger numerical value always requires a longer word. "
            "However, careful counting reveals surprising mathematical exceptions that spark lively classroom inquiry and logical discussions among learners! "
            "For example, consider the number ten: its numerical value is a two-digit quantity, yet its written name T-E-N has only three letters. "
            "Now consider the number seventeen: its value is seventeen, and its written name S-E-V-E-N-T-E-E-N contains nine distinct letters. "
            "Now examine seventy: its value is seventy, yet its word S-E-V-E-N-T-Y has only seven letters, which is fewer letters than seventeen! "
            "Even more remarkably, the number one hundred has an impressive value, but its written name contains ten letters, "
            "whereas ninety-eight has eleven letters. Analyzing number names proves that language word structure follows phonetic spelling rules distinct from numerical magnitudes in primary mathematics."
        ),
        "checkpoints": [
            {
                "q": "How many letters are in the written English word for the number 'SEVENTEEN'?",
                "options": [
                    "9 letters",
                    "7 letters",
                    "10 letters",
                    "8 letters"
                ],
                "ans": "9 letters",
                "explanation": "Counting S-E-V-E-N-T-E-E-N gives exactly 9 alphabet letters."
            },
            {
                "q": "Does a larger numerical value always have more letters in its written name than a smaller number?",
                "options": [
                    "No, word length depends on language spelling rather than numerical magnitude",
                    "Yes, every larger number always has more letters",
                    "Yes, every tens number has exactly 20 letters",
                    "No, all number words have exactly four letters"
                ],
                "ans": "No, word length depends on language spelling rather than numerical magnitude",
                "explanation": "For example, 70 (seventy = 7 letters) has a greater numerical value than 17 (seventeen = 9 letters), but fewer letters."
            }
        ]
    }
]

if __name__ == "__main__":
    print("=== VERIFYING SLIDES 1 TO 8 ===")
    assert len(slides_part1) == 8

    for s in slides_part1:
        sid = s["id"]
        title = s["title"]
        tw = len(title.split())
        assert 1 <= tw <= 3, f"Slide {sid} title '{title}' must be 1-3 words (got {tw})"
        
        speech = s["speech"]
        wc = len(speech.split())
        print(f"Slide {sid}: '{title}' -> {wc} words")
        assert 195 <= wc <= 215, f"Slide {sid} word count {wc} out of range 195-215!"
        
        assert len(s["checkpoints"]) == 2, f"Slide {sid} must have 2 checkpoints"
        for cp in s["checkpoints"]:
            assert len(cp["options"]) == 4, f"Slide {sid} checkpoint options != 4"
            assert cp["ans"] in cp["options"], f"Slide {sid} ans not in options"

    print("Part 1 verified successfully!")
