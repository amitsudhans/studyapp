# -*- coding: utf-8 -*-
"""
Generate Slides 9 to 16 for Class 3 Mathematics - Chapter 1: What's in a Name?
Strict requirements:
- Titles: 1 to 3 words each
- Spoken text: strictly 195 to 215 words each
- Tone: Pure Indian male teacher academic, encouraging, didactic narration
- Zero human character names (no Raghav, Deba, Deep, Teji, Jojo, Meera, Dhruv, etc.)
- Zero lecturer personas (no Dr., Sir, Madam, Mr., Mrs., Miss)
- 2 checkpoints per slide with 4 options each, correct answer, and explanation
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Extreme Place Names",
        "badge": "Geographical Extremes",
        "sim_id": "sim_extreme_names_map",
        "description": "Explore India's geographical extremes by investigating the railway station with the longest name and towns with the shortest names.",
        "speech": (
            "Our vast and diverse nation of India holds breathtaking geographical wonders across every state, "
            "including astonishing extremes in the letter lengths of its official railway station and town names. "
            "Young geographers and mathematicians will be thrilled to learn about an extraordinary railway station located in Andhra Pradesh, "
            "nestled near the southern border of Tamil Nadu: Venkatanarasimharajuvaripeta! "
            "When inquisitive students count every individual alphabet character in this magnificent railway board name, "
            "they discover that it contains an astounding twenty-eight letters, making it the longest railway station name in all of India. "
            "At the opposite end of our country's geographical spectrum lie two remarkable railway stations with the shortest names in India: "
            "the famous railway station of Ib, situated in the eastern state of Odisha beside the scenic Ib River, "
            "and the peaceful town of Od, located in the western state of Gujarat. "
            "Both Ib and Od contain just two alphabet letters each! "
            "Comparing these real-world extremes offers an exciting mathematical subtraction exercise for young minds: "
            "subtracting two letters from twenty-eight letters reveals an immense difference of twenty-six letters between India's longest and shortest place names. "
            "Investigating national geography through letter counting proves how mathematical data collection connects directly to our vibrant homeland."
        ),
        "checkpoints": [
            {
                "q": "What is the longest railway station name in India, containing 28 letters?",
                "options": [
                    "Venkatanarasimharajuvaripeta",
                    "Thiruvananthapuram",
                    "Chhatrapati Shivaji Maharaj Terminus",
                    "Visakhapatnam"
                ],
                "ans": "Venkatanarasimharajuvaripeta",
                "explanation": "Venkatanarasimharajuvaripeta in Andhra Pradesh has 28 letters, making it the longest railway station name in India."
            },
            {
                "q": "Which of the following represents one of the shortest place names in India with only 2 letters?",
                "options": [
                    "Ib (in Odisha)",
                    "Goa",
                    "Puri",
                    "Diu"
                ],
                "ans": "Ib (in Odisha)",
                "explanation": "Ib in Odisha and Od in Gujarat have only two letters each, representing the shortest place names in India."
            }
        ]
    },
    {
        "id": 10,
        "title": "Number Word Riddles",
        "badge": "Logical Deduction",
        "sim_id": "sim_number_word_riddles",
        "description": "Solve clever mathematical riddles that combine linguistic letter counts with place value arithmetic clues.",
        "speech": (
            "Mathematical deduction becomes truly thrilling when we combine place value arithmetic clues with word and letter quantities. "
            "Let us examine an intriguing number puzzle frequently solved in primary classrooms: "
            "'I am a two-digit number. My written English name consists of exactly two separate words. "
            "My first word has five letters, my second word has five letters, and my digits add up to seven. What number am I?' "
            "To solve this riddle, a young mathematician works like a brilliant scientific detective. "
            "First, the student analyzes the tens word: forty has five letters, and fifty has five letters. "
            "Next, the student examines the ones word: three has five letters, seven has five letters, and eight has five letters. "
            "Now let us test the digit sum condition where tens digit plus ones digit must equal seven. "
            "Consider fifty-two: two has three letters, so it cannot be fifty-two. "
            "Now consider forty-three: the tens digit is four, and the ones digit is three. "
            "Adding four plus three gives exactly seven! "
            "Furthermore, forty has five letters, and three has five letters, matching every single condition of the puzzle perfectly. "
            "Solving number riddles sharpens analytical problem-solving skills across mathematics and linguistics in joyful learning."
        ),
        "checkpoints": [
            {
                "q": "How many letters are in the tens word 'FORTY'?",
                "options": [
                    "5 letters",
                    "6 letters",
                    "4 letters",
                    "7 letters"
                ],
                "ans": "5 letters",
                "explanation": "Counting the letters F-O-R-T-Y confirms exactly 5 letters."
            },
            {
                "q": "In the number 'FORTY-THREE', what is the sum of its two digits (4 and 3)?",
                "options": [
                    "7",
                    "6",
                    "8",
                    "9"
                ],
                "ans": "7",
                "explanation": "Adding the tens digit 4 and ones digit 3 gives: 4 + 3 = 7."
            }
        ]
    },
    {
        "id": 11,
        "title": "Proximity To Hundred",
        "badge": "Number Line Intervals",
        "sim_id": "sim_hundred_proximity_line",
        "description": "Investigate number line intervals and symmetrical distances from the landmark century baseline of one hundred.",
        "speech": (
            "In primary arithmetic, the number one hundred serves as a magnificent psychological and mathematical milestone. "
            "Children love solving proximity riddles that challenge them to deduce secret numbers based on their distance from one hundred. "
            "Imagine a mathematical riddle that asks: "
            "'I am an even number less than one hundred. If you take four steps forward from me on the number line, "
            "you will land precisely on one hundred. What number am I?' "
            "To solve this mystery, the student visualizes a horizontal number line ending at one hundred. "
            "Walking four steps forward means that our mystery number is exactly four units less than one hundred. "
            "Calculating one hundred minus four immediately reveals the answer: ninety-six! "
            "Now consider a companion riddle: "
            "'I am greater than one hundred, and my distance from one hundred is identical to the distance between ninety-six and one hundred.' "
            "Since ninety-six is four units below one hundred, our new number must be four units above one hundred, "
            "which gives one hundred plus four, equaling one hundred and four! "
            "Notice how ninety-six and one hundred and four form a perfectly balanced, symmetrical pair around one hundred on the number line. "
            "Exploring distance from benchmark numbers develops strong mental subtraction and visual estimation abilities."
        ),
        "checkpoints": [
            {
                "q": "Which number is located exactly 4 units before 100 on the number line?",
                "options": [
                    "96",
                    "94",
                    "98",
                    "92"
                ],
                "ans": "96",
                "explanation": "Subtracting 4 from 100 gives: 100 - 4 = 96."
            },
            {
                "q": "What number is located at the same distance above 100 as 96 is below 100?",
                "options": [
                    "104",
                    "106",
                    "102",
                    "108"
                ],
                "ans": "104",
                "explanation": "Because 96 is 4 units below 100, the symmetrical number 4 units above 100 is: 100 + 4 = 104."
            }
        ]
    },
    {
        "id": 12,
        "title": "Living Things Classification",
        "badge": "Categorical Logic",
        "sim_id": "sim_living_eats_sorter",
        "description": "Classify diverse illustrated objects into mutually exclusive groups based on whether they require biological food to survive.",
        "speech": (
            "Data handling in primary mathematics begins with the essential scientific skill of classification and categorical sorting. "
            "Before we can count, tally, or construct visual charts, we must first sort objects into clear, well-defined groups. "
            "Suppose a classroom teacher presents children with eight colorful picture cards showing diverse everyday items from nature and home: "
            "a cow, a wooden chair, a sparrow, a clay pot, an elephant, a school bag, a goldfish, and a plastic pencil box. "
            "The teacher asks the students to sort these picture cards into two distinct categories: "
            "living organisms that eat food and grow, versus non-living objects that do not eat food. "
            "The students examine each card with logical precision and scientific observation: "
            "the cow eats fresh grass, the sparrow pecks grain seeds, the elephant consumes sugarcane and leaves, and the goldfish eats water plants. "
            "All four of these living creatures belong together in Category A: Things That Eat Food! "
            "In contrast, the wooden chair, clay pot, school bag, and plastic pencil box are non-living human-made artifacts. "
            "They do not breathe, eat food, or grow, placing them squarely in Category B. "
            "Each group contains exactly four items, demonstrating how logical categorization creates balanced, orderly data sets ready for numerical analysis."
        ),
        "checkpoints": [
            {
                "q": "Which of the following items belongs in the category 'Things That Eat Food'?",
                "options": [
                    "SPARROW",
                    "WOODEN CHAIR",
                    "CLAY POT",
                    "SCHOOL BAG"
                ],
                "ans": "SPARROW",
                "explanation": "A sparrow is a living bird that consumes grains and seeds for nutrition."
            },
            {
                "q": "Why is sorting items into clear categories an important first step in mathematical data handling?",
                "options": [
                    "It organizes unstructured items into distinct groups that can be counted and compared",
                    "It changes the physical shape of the objects permanently",
                    "It makes all the objects completely weightless",
                    "It turns pictures into sound vibrations"
                ],
                "ans": "It organizes unstructured items into distinct groups that can be counted and compared",
                "explanation": "Categorization creates well-defined subsets, which is the foundational basis for tallying and statistical analysis."
            }
        ]
    },
    {
        "id": 13,
        "title": "Electric Appliance Sorting",
        "badge": "Technology Sorting",
        "sim_id": "sim_electric_manual_sorter",
        "description": "Sort household devices into electrical appliances versus manual tools to practice multi-attribute data classification.",
        "speech": (
            "Let us deepen our classification expertise by exploring modern technological objects found inside our homes and school classrooms. "
            "Consider another exciting sorting task where students examine a collection of eight common household instruments and appliances: "
            "a ceiling fan, a manual wooden broom, a refrigerator, a stainless steel hand spoon, "
            "a television set, a plastic water bucket, a table lamp, and an iron claw hammer. "
            "The mathematical challenge is to classify these items into two mutually exclusive sets: "
            "devices that require electrical energy from a wall socket or chemical battery to function, "
            "versus manual mechanical tools that operate solely through human physical effort and muscle power. "
            "The students test each device thoughtfully: "
            "the ceiling fan requires electricity to spin its blades; the refrigerator needs electrical power to run its cooling compressor; "
            "the television relies on electric currents to display pictures; and the table lamp needs electricity to light its bulb. "
            "These four items form the Electrical Appliances set. "
            "Meanwhile, the broom, hand spoon, water bucket, and claw hammer require zero electric current, "
            "relying entirely on human muscle power to sweep, scoop, carry, and strike. "
            "Grouping items by functional properties reinforces how binary classification organizes real-world technology into clean mathematical subsets."
        ),
        "checkpoints": [
            {
                "q": "Which of the following household items belongs to the 'Requires Electricity' group?",
                "options": [
                    "REFRIGERATOR",
                    "WOODEN BROOM",
                    "CLAW HAMMER",
                    "WATER BUCKET"
                ],
                "ans": "REFRIGERATOR",
                "explanation": "A refrigerator requires electrical energy to power its motor and cool food."
            },
            {
                "q": "How many items belong to the manual mechanical group if 4 out of 8 items require electricity?",
                "options": [
                    "4 items",
                    "2 items",
                    "6 items",
                    "8 items"
                ],
                "ans": "4 items",
                "explanation": "Subtracting 4 electrical items from 8 total items leaves exactly 4 manual items."
            }
        ]
    },
    {
        "id": 14,
        "title": "Hairstyle Data Collection",
        "badge": "Observational Data",
        "sim_id": "sim_hairstyle_collector",
        "description": "Gather live classroom data by observing and tallying the diverse hairstyles worn by students in a class.",
        "speech": (
            "Now that our young mathematicians understand tallying, letter counting, and categorical sorting, "
            "they are fully prepared to conduct a genuine statistical survey right inside their own bustling classroom! "
            "In Chapter 1, students conduct a delightful observational study focused on their classmates' diverse and charming hairstyles. "
            "Looking around the lively classroom, the observant students notice that hair can be styled in several distinct, recognizable ways: "
            "some children wear two perky ponytails tied neatly with colorful ribbons; "
            "others wear a single sleek ponytail hanging down their back; "
            "some children have traditionally braided hair; "
            "many students sport short cropped haircuts; and some display naturally curly locks of hair. "
            "To record this real-world information systematically without making errors, the student surveyor creates an observational tally sheet. "
            "As the surveyor observes each classmate one by one, a tally stroke is immediately recorded in the corresponding hairstyle column. "
            "If five students wear two ponytails, the student draws four vertical lines crossed by one diagonal slash. "
            "Collecting live observational data teaches children that mathematics is not just abstract arithmetic written in notebooks, "
            "but a dynamic, joyful, and creative tool for observing, recording, and celebrating the wonderful diversity of the human world around them."
        ),
        "checkpoints": [
            {
                "q": "What is the primary purpose of conducting a classroom hairstyle survey?",
                "options": [
                    "To collect, tally, and organize real-world observational data",
                    "To force all children to have the same haircut",
                    "To measure the height of the classroom walls",
                    "To test the speed of running in the playground"
                ],
                "ans": "To collect, tally, and organize real-world observational data",
                "explanation": "A survey allows students to practice gathering empirical data from their immediate environment using tally marks."
            },
            {
                "q": "If an observer spots 5 children with braided hair, how is that quantity recorded with tallies?",
                "options": [
                    "Four vertical lines crossed by one diagonal slash",
                    "Five separate circles drawn in a row",
                    "Five long horizontal strokes",
                    "A single large cross"
                ],
                "ans": "Four vertical lines crossed by one diagonal slash",
                "explanation": "A quantity of five is always represented as a closed five-bundle: four upright lines with one diagonal strike."
            }
        ]
    },
    {
        "id": 15,
        "title": "Hairstyle Frequency Table",
        "badge": "Tabular Synthesis",
        "sim_id": "sim_hairstyle_tally_table",
        "description": "Convert raw observational tallies into a structured two-column frequency table to discover statistical insights.",
        "speech": (
            "Once all observational tally marks have been carefully recorded across the classroom, "
            "the next vital step in statistical analysis is summarizing raw data into a structured frequency table. "
            "A frequency table is an organized grid containing two primary columns: "
            "the descriptive category name on the left side, and the total numerical count, called the frequency, on the right side. "
            "Suppose a classroom survey of twenty-five students yields the following tally counts: "
            "eight students have short hair, represented by one full five-bundle plus three vertical strokes; "
            "six students wear two ponytails, represented by one five-bundle plus one single stroke; "
            "five students wear neat braids, represented by one complete five-bundle; "
            "four students wear a single ponytail, represented by four vertical strokes; "
            "and two students have curly hair, represented by two neat strokes. "
            "By translating each set of tally bundles into clear numerical digits, "
            "students instantly observe that short hair is the most common hairstyle with a frequency of eight, "
            "while curly hair is the least common hairstyle with a frequency of two. "
            "Summing the frequencies confirms that eight plus six plus five plus four plus two equals twenty-five total students, "
            "proving that no child was accidentally missed or counted twice in the survey."
        ),
        "checkpoints": [
            {
                "q": "In the survey, which hairstyle had the highest frequency with 8 students?",
                "options": [
                    "Short hair",
                    "Two ponytails",
                    "Braids",
                    "Curly hair"
                ],
                "ans": "Short hair",
                "explanation": "Short hair had 8 students, making it the most frequent hairstyle in the classroom survey."
            },
            {
                "q": "What is the total number of students surveyed if frequencies are 8, 6, 5, 4, and 2?",
                "options": [
                    "25 students",
                    "20 students",
                    "30 students",
                    "22 students"
                ],
                "ans": "25 students",
                "explanation": "Adding all frequencies together: 8 + 6 + 5 + 4 + 2 = 25 total students."
            }
        ]
    },
    {
        "id": 16,
        "title": "Pictograph Data Displays",
        "badge": "Visual Charts",
        "sim_id": "sim_pictograph_chart_builder",
        "description": "Transform numerical frequency tables into vibrant visual pictographs where illustrated icons represent quantities.",
        "speech": (
            "To communicate statistical findings clearly and engagingly to others, mathematicians transform numbers into visual charts called pictographs! "
            "A pictograph is a delightful graphical display where small pictures or illustrated symbols represent numerical quantities in rows or columns. "
            "In our classroom hairstyle study, we can design a friendly smiling face icon to represent individual student counts. "
            "First, every successful pictograph requires a clear key or scale: "
            "let one smiling face symbol represent exactly one student. "
            "Beside the 'Short Hair' label, we draw a neat horizontal row of eight smiling face symbols. "
            "Beside 'Two Ponytails', we line up six smiling faces. "
            "Beside 'Braids', we place five smiling faces. "
            "Beside 'Single Ponytail', we draw four smiling faces. "
            "And beside 'Curly Hair', we display two smiling faces. "
            "Looking at the completed pictograph, even a young child who has not yet learned to read numbers can instantly understand the survey results! "
            "The longest horizontal row of faces immediately identifies the most popular hairstyle, "
            "while the shortest row highlights the least frequent style at a quick glance. "
            "Pictographs bridge the gap between abstract numbers and intuitive visual understanding, "
            "empowering young learners to present scientific and mathematical data with genuine confidence, clarity, and creative joy."
        ),
        "checkpoints": [
            {
                "q": "What is a pictograph?",
                "options": [
                    "A chart that uses pictures or symbols to represent numerical data",
                    "A machine that takes photographs of distant stars",
                    "A musical instrument played in an orchestra",
                    "A special pen used for writing upside down"
                ],
                "ans": "A chart that uses pictures or symbols to represent numerical data",
                "explanation": "A pictograph uses repeatable picture symbols or icons to visually represent numerical quantities."
            },
            {
                "q": "If one smiling face icon represents 1 student, how many face icons are drawn for 6 students with two ponytails?",
                "options": [
                    "6 face icons",
                    "3 face icons",
                    "12 face icons",
                    "1 face icon"
                ],
                "ans": "6 face icons",
                "explanation": "With a 1-to-1 scale key, 6 students require exactly 6 smiling face icons."
            }
        ]
    }
]

if __name__ == "__main__":
    print("=== VERIFYING SLIDES 9 TO 16 ===")
    assert len(slides_part2) == 8

    for s in slides_part2:
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

    print("Part 2 verified successfully!")
