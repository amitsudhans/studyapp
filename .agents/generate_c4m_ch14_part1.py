# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 14: Data Handling
Part 1: Slides 1 to 8 Data Generator
Short headings (1 to 3 words each)
Zero human names (Rohan, Anjali, etc. replaced with generic roles)
Speech strictly 195 to 215 words per slide
Clean Unicode throughout (×, ÷, ₹, etc.)
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Framing Survey Questions",
        "section": "Data Collection & Question Design",
        "speech": (
            "Welcome young statisticians to our exploration of data handling, beginning with the crucial art of framing effective survey questions. "
            "When we want to understand the preferences and habits of a group, such as our classroom peers, the way we ask questions determines the quality of our findings. "
            "Consider a student investigator who asks an open-ended question such as, which subjects do you like in school? "
            "One classmate might answer that they like art, mathematics, and sports, while another mentions languages and music. "
            "Because students can list several different subjects or give broad general descriptions, the resulting responses become tangled and difficult to tally. "
            "Now consider refining the inquiry into a precise, targeted question: which single subject do you like the most? "
            "By asking for their one favorite subject, every respondent provides exactly one distinct, unambiguous choice. "
            "Specific questions generate clear categorical data that can be counted, compared, and organized without confusion. "
            "Good survey questions avoid bias, provide clear options, and ensure that every participant interprets the prompt in the exact same manner. "
            "Framing thoughtful questions is the essential first step of scientific investigation, laying a solid foundation for trustworthy data collection and insightful mathematical analysis in our classroom."
        ),
        "checkpoints": [
            {
                "q": "Why is 'Which subject do you like the most?' better than 'Which subjects do you like?' for a survey?",
                "options": ["It is shorter to read", "It gives exactly one clear choice per student", "It only allows math", "It takes longer to answer"],
                "ans": 1,
                "exp": "Asking for the single most favorite subject ensures one clean response per participant."
            },
            {
                "q": "What is the primary goal of framing clear survey questions?",
                "options": ["To confuse the respondents", "To gather clear, measurable, and organized data", "To write long essays", "To avoid collecting numbers"],
                "ans": 1,
                "exp": "Well-designed questions produce structured data that can be counted and compared accurately."
            }
        ]
    },
    {
        "id": 2,
        "title": "Recording Student Responses",
        "section": "Raw Data & Letter Codes",
        "speech": (
            "Once our survey question is framed, we must record the responses of our forty-five classmates quickly and systematically. "
            "Writing down full subject names repeatedly, such as Mathematics or Physical Education, takes far too much time and clutters our notepad. "
            "Smart researchers use standardized letter abbreviations to record raw responses efficiently during a live classroom survey. "
            "In our study, we designate letter codes for each subject option: M stands for Mathematics, L represents Languages, "
            "T signifies The World Around Us, A denotes Visual Arts, and P.E. indicates Physical Education in our record log. "
            "As we interview each of the forty-five students across the room, we record their choice in an observational log sheet. "
            "The resulting raw data stream appears as a continuous sequence of letters: M, L, T, P.E., M, A, M, L, and so forth. "
            "While this letter sequence accurately captures every student's voice, looking at forty-five mixed letters makes it hard to tell which subject is the class favorite at a glance. "
            "Raw data is simply unorganized information collected straight from the field. "
            "To extract meaningful patterns from our letter codes, we must transition from raw records to structured tables, tally marks, and frequency counts that anyone can understand immediately."
        ),
        "checkpoints": [
            {
                "q": "Why do researchers use letter abbreviations like M, L, and A when recording survey data?",
                "options": ["To hide the results", "To record responses quickly and neatly without writing full words", "Because paper is too expensive", "To change the students' minds"],
                "ans": 1,
                "exp": "Letter codes save time and keep raw observational data compact during active polling."
            },
            {
                "q": "If a raw data log contains 45 letters in total, what does this number represent?",
                "options": ["The number of subjects", "The total number of students surveyed", "The number of teachers", "The class test score"],
                "ans": 1,
                "exp": "Each letter corresponds to one student response, so 45 letters represent 45 surveyed students."
            }
        ]
    },
    {
        "id": 3,
        "title": "Tabulating Raw Data",
        "section": "Frequency Tables & Data Organization",
        "speech": (
            "Now let us transform our raw stream of forty-five letter codes into an organized, professional frequency table. "
            "A data table structures information into clearly labeled rows and columns, making numerical patterns instantly recognizable to any observer. "
            "We construct a two-column table with the first column titled Favorite Subject and the second column titled Number of Children. "
            "To tally our data without missing any entry, we read through our raw response list systematically from left to right, "
            "marking each appearance with a tally mark before totaling the final numerical counts. "
            "When we count the responses, we discover that fourteen children chose Mathematics, nine selected Languages, "
            "seven picked The World Around Us, five chose Arts, and ten preferred Physical Education. "
            "To verify that no student was accidentally skipped or double-counted, we sum the numbers in our second column: "
            "fourteen plus nine is twenty-three; adding seven gives thirty; adding five gives thirty-five; adding ten equals exactly forty-five. "
            "The sum of our frequencies matches our total survey size perfectly. "
            "Tabulating raw data eliminates guesswork, structures raw chaos into clean order, and prepares us to answer analytical questions with total mathematical confidence and structural clarity. "
            "Learning to construct structured tables provides students with a foundational life skill for organizing facts in science and mathematics."
        ),
        "checkpoints": [
            {
                "q": "What is the purpose of summing the frequency column in a data table?",
                "options": ["To find the largest number", "To verify that the total matches the number of surveyed participants", "To calculate the average age", "To create a new subject"],
                "ans": 1,
                "exp": "Summing the frequencies confirms that every single surveyed response has been accounted for."
            },
            {
                "q": "If Mathematics has 14 votes and Languages has 9 votes, what is the combined count for both?",
                "options": ["21", "23", "25", "27"],
                "ans": 1,
                "exp": "14 + 9 = 23 students."
            }
        ]
    },
    {
        "id": 4,
        "title": "Interpreting Data Tables",
        "section": "Table Analysis & Comparative Metrics",
        "speech": (
            "With our data neatly arranged in a frequency table, we can now interpret the findings to answer important analytical questions about our class. "
            "Interpreting a table means examining the numbers to identify highs, lows, differences, and overall trends across categories. "
            "Looking down the frequency column, we easily identify the most popular subject among our peers. "
            "With fourteen student votes, Mathematics holds the highest frequency, making it the most favored subject in our classroom survey. "
            "Conversely, we find the least common favorite subject by locating the smallest count. "
            "Visual Arts received five votes, which is the lowest frequency in the table. "
            "We can also make direct comparisons between categories using basic subtraction. "
            "For instance, how many more students prefer Mathematics over Arts? "
            "Subtracting five from fourteen reveals that nine more students chose Mathematics than Arts. "
            "Similarly, comparing Physical Education with ten votes to Languages with nine votes shows a close margin of just one student. "
            "Data interpretation allows teachers, school administrators, and students to understand group interests objectively. "
            "Tables turn raw counts into meaningful stories, helping us make evidence-based decisions rather than relying on casual guesses or subjective personal opinions. "
            "Analyzing trends and comparing frequencies forms the cornerstone of critical statistical thinking for young learners."
        ),
        "checkpoints": [
            {
                "q": "Based on the survey (Math: 14, Arts: 5), how many more students prefer Math than Arts?",
                "options": ["7 students", "8 students", "9 students", "10 students"],
                "ans": 2,
                "exp": "14 - 5 = 9 students."
            },
            {
                "q": "Which category in a frequency table represents the 'most popular' choice?",
                "options": ["The category with the lowest number", "The category with the highest frequency count", "The first row in the table", "The category with zero votes"],
                "ans": 1,
                "exp": "The highest numerical frequency indicates the most common or popular choice."
            }
        ]
    },
    {
        "id": 5,
        "title": "Ice Gola Tallies",
        "section": "Tally Marks & Grouping by Fives",
        "speech": (
            "During a warm school lunch break, children visit a colorful refreshment cart to enjoy sweet, icy golas. "
            "To track which flavors are being ordered in real time, a student data collector uses a rapid recording method called tally marks. "
            "Tally marks are simple vertical strokes drawn as each item is observed by the researcher. "
            "When we count, we draw one vertical line for each of the first four items: one, two, three, four. "
            "To represent the fifth item, we draw a diagonal slash across the four vertical lines to bundle them into a complete group of five. "
            "Bundling by fives is a brilliant mathematical technique because human eyes can count groups of five effortlessly using skip counting. "
            "Instead of counting twenty individual sticks one by one, we simply count by fives: five, ten, fifteen, twenty! "
            "At the gola stand, our tally chart records eight tallies for red strawberry, twelve tallies for green khus, "
            "six tallies for yellow mango, and four tallies for purple kala khatta. "
            "Tally marks bridge the gap between fleeting live events and permanent data tables, ensuring that fast-paced counts remain accurate without losing track of individual observations during busy school hours in every lively school event."
        ),
        "checkpoints": [
            {
                "q": "How is the number 5 represented in standard tally marks?",
                "options": ["5 vertical lines", "4 vertical lines with 1 diagonal cross-slash", "A square with a dot", "A circle with 5 spokes"],
                "ans": 1,
                "exp": "Four vertical strokes crossed by a diagonal line form a bundle of 5."
            },
            {
                "q": "What total is represented by two bundles of 5 tallies plus 3 single strokes?",
                "options": ["11", "12", "13", "14"],
                "ans": 2,
                "exp": "(5 + 5) + 3 = 10 + 3 = 13."
            }
        ]
    },
    {
        "id": 6,
        "title": "Pictorial Data Charts",
        "section": "Pictographs & Icon Visualizations",
        "speech": (
            "We can make our flavor data even more engaging and visually communicative by creating a colorful pictorial chart. "
            "A pictograph uses pictures, icons, or stick figures to represent quantities of items rather than plain numerical digits. "
            "In our ice gola pictograph, each drawn gola icon represents exactly one child's treat. "
            "Beside the green khus label, we draw a row of twelve green gola icons. "
            "Beside red strawberry, we display eight red icons; beside yellow mango, six yellow icons; and beside purple kala khatta, four purple icons. "
            "Looking at the pictograph, visual comparison becomes instantaneous because the length of each row directly reflects its numerical frequency. "
            "The longest row belongs to green khus, showing at a glance that it was the most popular flavor of the day. "
            "The shortest row belongs to purple kala khatta, confirming it was the least ordered flavor. "
            "Pictographs are widely used in newspapers, school magazines, and public reports because people of all ages can interpret visual symbols rapidly and enjoyably. "
            "However, every good pictograph must include a clear key that explains the value of each symbol, especially when icons represent larger groups. "
            "Understanding the key ensures that symbols communicate statistical information truthfully without misleading readers or distorting quantities."
        ),
        "checkpoints": [
            {
                "q": "In a pictograph where 1 icon = 1 gola, how many icons are needed to represent 8 strawberry golas?",
                "options": ["4 icons", "6 icons", "8 icons", "10 icons"],
                "ans": 2,
                "exp": "Since 1 icon = 1 gola, 8 golas require 8 icons."
            },
            {
                "q": "What visual feature of a pictograph allows you to spot the most popular category instantly?",
                "options": ["The color of the title", "The row with the longest line of icons", "The thickness of the border", "The page number"],
                "ans": 1,
                "exp": "The longest row of identical icons corresponds to the highest numerical count."
            }
        ]
    },
    {
        "id": 7,
        "title": "Two Variable Data",
        "section": "Two-Way Tables & Multi-Category Sorting",
        "speech": (
            "So far we have examined single-variable data, but real-world investigations often involve analyzing two different characteristics simultaneously. "
            "Let us consider a class activity investigating sports preferences for chess and cricket across boys and girls in our school. "
            "Here, our two variables are student gender and sports participation type. "
            "To capture the complete picture, we must categorize students into four mutually exclusive groups: "
            "those who play only chess, those who play only cricket, those who play both sports, and those who play neither sport. "
            "A two-way classification table provides the perfect mathematical structure to display this two-variable information cleanly and systematically. "
            "The table rows represent boys and girls, while the table columns display the four sporting categories, followed by a total column on the right. "
            "Each intersection cell reveals the exact count for that specific combination, such as girls who play both sports or boys who play only cricket. "
            "Two-way tables allow us to analyze row totals, column totals, and grand totals all on a single compact sheet. "
            "Sorting data across two dimensions sharpens our classification skills and reveals subtle patterns that simple single-column lists could never capture in practice. "
            "Two-way contingency tables demonstrate how multiple categories interact seamlessly within a unified statistical framework."
        ),
        "checkpoints": [
            {
                "q": "What are the four participation categories when studying two sports like chess and cricket?",
                "options": ["Indoor, Outdoor, Water, Air", "Only Chess, Only Cricket, Both, Neither", "Morning, Afternoon, Evening, Night", "Winners, Losers, Referees, Coaches"],
                "ans": 1,
                "exp": "Two sports yield four logical states: sport A only, sport B only, both sports, or neither sport."
            },
            {
                "q": "What does an intersection cell in a two-way table represent?",
                "options": ["A random number", "The count of items sharing both the row and column attributes", "The sum of the whole table", "The title of the experiment"],
                "ans": 1,
                "exp": "Each cell reflects the specific conjunction of its row category and column category."
            }
        ]
    },
    {
        "id": 8,
        "title": "Sports Preference Tables",
        "section": "Contingency Table Analysis & Row Totals",
        "speech": (
            "Let us examine the data collected in our sports preference contingency table to discover how our peers spend their recreation time. "
            "Our table reveals that among the boys, four play only chess, twelve play only cricket, six play both sports, and two play neither sport. "
            "Summing across this row: four plus twelve is sixteen; plus six is twenty-two; plus two gives a total of twenty-four boys. "
            "Among the girls, seven play only chess, eight play only cricket, five play both sports, and four play neither sport. "
            "Summing the girls' row: seven plus eight is fifteen; plus five is twenty; plus four gives a total of twenty-four girls. "
            "Now let us examine the column totals to analyze overall sport popularity across the whole class. "
            "Students playing only chess total four plus seven, which equals eleven. "
            "Students playing only cricket total twelve plus eight, which equals twenty. "
            "Students playing both sports total six plus five, which equals eleven, while six students play neither sport. "
            "The grand total of all students equals twenty-four boys plus twenty-four girls, giving forty-eight participants. "
            "Two-way tables provide complete mathematical balance, ensuring every subset adds up harmoniously horizontally and vertically for complete clarity."
        ),
        "checkpoints": [
            {
                "q": "How many total students play ONLY cricket (12 boys + 8 girls)?",
                "options": ["18 students", "20 students", "22 students", "24 students"],
                "ans": 1,
                "exp": "12 + 8 = 20 students play only cricket."
            },
            {
                "q": "If 24 boys and 24 girls participated in the survey, what is the grand total of students?",
                "options": ["44", "46", "48", "50"],
                "ans": 2,
                "exp": "24 + 24 = 48 students in total."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(slides_part1)} slides for Part 1.")
    for s in slides_part1:
        wc = len(s["speech"].split())
        tw = len(s["title"].split())
        print(f"Slide {s['id']}: {s['title']} -> {wc} words (Title: {tw} words)")
        assert 1 <= tw <= 3, f"Title '{s['title']}' must be 1 to 3 words"
        assert 195 <= wc <= 215, f"Slide {s['id']} speech {wc} words out of range (195-215)"
        assert len(s["checkpoints"]) == 2, f"Slide {s['id']} must have 2 checkpoints"
    print("All Part 1 slide constraints validated successfully!")
