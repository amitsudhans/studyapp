#!/usr/bin/env python3
"""
NCERT Class 3 Mathematics - Chapter 13: Time Goes On
Part 1: Slides 1 to 8 (Teaching Content + Checkpoints)
Strict spoken word count: 195 to 215 words per slide.
Strict titles: 1 to 3 words.
Zero human character names, zero lecturer personas.
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Calendar Grid Building",
        "subtitle": "Monthly Layout & Day-Date Grid Construction",
        "speech": (
            "Welcome young learners to our wonderful exploration of time. Look closely at a monthly wall calendar grid. "
            "A calendar organizes dates into neat seven-day columns corresponding to the days of the week: Monday, "
            "Tuesday, Wednesday, Thursday, Friday, Saturday, and Sunday. When constructing the month of July, we first "
            "identify the exact day of the week on which the first day falls. July always contains exactly thirty-one days. "
            "If the first of July begins on a Monday, then the second is Tuesday, and the seventh is Sunday, completing our first "
            "full weekly row. Notice how each subsequent row adds seven days to each day's column. Every date in the same column "
            "shares the same day of the week. Therefore, adding seven to any date brings you directly to the identical weekday in "
            "the next row. This mathematical symmetry allows us to locate any date effortlessly. When we assemble July 2024, "
            "we observe that July starts on Monday and ends on Wednesday after thirty-one days. By carefully placing each "
            "consecutive integer from one to thirty-one across the columns, our complete monthly grid comes alive, providing "
            "a reliable roadmap for every planned family celebration, community festival, and joyful school activity."
        ),
        "checkpoints": [
            {
                "question": "How many total days are there in the month of July?",
                "options": ["28 days", "30 days", "31 days", "29 days"],
                "answer": 2,
                "hint": "July is one of the longer months that follows June.",
                "explanation": "July always has 31 days in the standard calendar."
            },
            {
                "question": "If July 1 is a Monday, what day of the week is July 8?",
                "options": ["Sunday", "Monday", "Tuesday", "Wednesday"],
                "answer": 1,
                "hint": "Add 7 days to any date to find the identical day of the week.",
                "explanation": "Adding 7 days to Monday (July 1 + 7) brings us directly to Monday, July 8."
            }
        ]
    },
    {
        "id": 2,
        "title": "Calendar Date Analysis",
        "subtitle": "Extracting Weekday Patterns & Event Queries",
        "speech": (
            "Now that our monthly calendar grid is assembled, let us analyze its mathematical patterns with close observation. "
            "A monthly grid allows us to answer precise time queries instantly and accurately. First, let us count the total number "
            "of Sundays in July 2024. Scanning down the Sunday column reveals the dates: July seventh, fourteenth, twenty-first, "
            "and twenty-eighth. That gives four complete Sundays. Next, examine the Thursday column to locate its dates: fourth, "
            "eleventh, eighteenth, and twenty-fifth. Notice again the constant numerical jump of seven between successive Thursdays. "
            "Furthermore, calendars help us calculate forward and backward timelines effortlessly. If a family plans a joyful garden picnic "
            "three days after July twenty-second, we simply add three to twenty-two, landing directly on July twenty-fifth. If school "
            "reopens on the first Monday after summer holidays end on July thirty-first, we locate the next week's starting day in August. "
            "Every date tells an orderly story of sequential progression. Tracking dates teaches us that time never pauses; it flows forward "
            "in predictable seven-day cycles. Mastering calendar reading empowers you to organize study schedules, remember memorable family "
            "celebrations, and anticipate school holidays with great joy and complete mathematical confidence throughout every season of the year."
        ),
        "checkpoints": [
            {
                "question": "Which date is exactly three days after July 22?",
                "options": ["July 24", "July 25", "July 26", "July 23"],
                "answer": 1,
                "hint": "Calculate 22 + 3.",
                "explanation": "Adding 3 days to 22 gives July 25 (22 + 3 = 25)."
            },
            {
                "question": "What is the constant numerical difference between dates in the same weekday column?",
                "options": ["5 days", "6 days", "7 days", "10 days"],
                "answer": 2,
                "hint": "Think about how many days are in one complete week.",
                "explanation": "Since a week has 7 days, dates directly below each other in the same column increase by 7."
            }
        ]
    },
    {
        "id": 3,
        "title": "Annual Festival Tracking",
        "subtitle": "Recording Dates & Multi-Year Calendar Constancy",
        "speech": (
            "Across the twelve months of each year, diverse cultural festivals bring communities together in harmonious celebration. "
            "We can record these meaningful occasions in a standardized date format consisting of day, month, and year. For example, "
            "national celebrations such as Independence Day fall on the fifteenth of August every year, written as fifteen August. "
            "Republic Day consistently occurs on the twenty-sixth of January, written formally as twenty-six January. Notice that national holidays "
            "remain fixed on identical solar dates every single year. In contrast, lunar festivals such as Eid-al-Fitr, Deepawali, and "
            "Ganesh Chaturthi follow traditional lunar calendars, so their solar calendar dates shift gradually from year to year. When "
            "we compare calendars across consecutive years, we discover fascinating mathematical constants. The twelve month names always appear "
            "in the exact same order, starting with January and concluding with December. A standard week always maintains seven consecutive days. "
            "However, because three hundred sixty-five is not an exact multiple of seven, each calendar date usually shifts forward by one "
            "day of the week in the following standard year. Tracking festival dates across annual calendars reinforces our appreciation of "
            "both fixed civic markers and shifting cultural celebrations throughout our vibrant nation."
        ),
        "checkpoints": [
            {
                "question": "Which national festival occurs on the fixed date of 15 August every year?",
                "options": ["Republic Day", "Independence Day", "Gandhi Jayanti", "Children's Day"],
                "answer": 1,
                "hint": "This day commemorates India's independence in 1947.",
                "explanation": "Independence Day is celebrated annually on 15 August."
            },
            {
                "question": "What remains constant when comparing calendars across different years?",
                "options": ["The weekday for each date", "The sequence of the twelve months", "The exact start day of January", "The dates of lunar festivals"],
                "answer": 1,
                "hint": "Does January always come before February?",
                "explanation": "The order and names of the twelve months (January through December) always remain identical."
            }
        ]
    },
    {
        "id": 4,
        "title": "Yearly Calendar Statistics",
        "subtitle": "Months, Leap Years & Weekly Partitioning",
        "speech": (
            "Let us explore the statistical structure of a full annual calendar with deep mathematical curiosity. Every standard year "
            "is divided into exactly twelve months. But have you noticed that different months contain different numbers of days? Seven months "
            "contain thirty-one days: January, March, May, July, August, October, and December. Four months contain thirty days: April, "
            "June, September, and November. That leaves February, which is uniquely special because it holds only twenty-eight days in a standard "
            "year. However, every fourth year is a leap year, adding an extra day so February has twenty-nine days. When we sum the days across "
            "all twelve months, a standard year yields three hundred sixty-five days, whereas a leap year contains three hundred sixty-six "
            "days. Furthermore, if we divide three hundred sixty-five days by seven days per week, we get fifty-two complete weeks plus "
            "one additional day. In a leap year, there are fifty-two weeks plus two extra days. This mathematical breakdown explains why "
            "the calendar shifts forward by one weekday each standard year. Understanding these yearly quantities gives us a complete "
            "panoramic grasp of how our planet's solar orbit defines the mathematical rhythm of our daily calendar year after year."
        ),
        "checkpoints": [
            {
                "question": "How many days are in a standard, non-leap year?",
                "options": ["360 days", "364 days", "365 days", "366 days"],
                "answer": 2,
                "hint": "52 weeks of 7 days equals 364 days, plus 1 extra day.",
                "explanation": "A standard year has 365 days, whereas a leap year has 366 days."
            },
            {
                "question": "Which month has fewer than 30 days in a standard calendar?",
                "options": ["April", "February", "June", "September"],
                "answer": 1,
                "hint": "This second month has 28 or 29 days.",
                "explanation": "February has 28 days in a standard year and 29 days in a leap year."
            }
        ]
    },
    {
        "id": 5,
        "title": "Generational Age Puzzles",
        "subtitle": "Age Differences & Lifespan Calculations",
        "speech": (
            "Time also measures human growth and generational spans across family lineages. Let us explore age calculations through clear "
            "mathematical logic. Suppose a young student is currently eight years old, while the mother is thirty-two years old, and the "
            "grandmother is sixty years old. We can ask interesting deductive questions. How old was the mother when the student was born? "
            "To solve this, we subtract the student's current age of eight from the mother's current age of thirty-two. Thirty-two minus eight "
            "gives twenty-four. Thus, the mother was twenty-four years old at the student's birth. Now consider a vital truth: the age gap "
            "between any two people never changes over time. When the student grows ten years older to reach age eighteen, the mother will "
            "also grow ten years older, reaching forty-two years. The difference between forty-two and eighteen remains twenty-four years. "
            "Similarly, the age difference between the grandmother and mother is sixty minus thirty-two, which equals twenty-eight years. "
            "Whether ten years pass or fifty years pass, that gap remains exactly twenty-eight years. Solving generational puzzles helps us see "
            "that while individual ages increase continuously every year, the numerical difference between family members stays eternally constant and unchanged."
        ),
        "checkpoints": [
            {
                "question": "If a child is 8 and the mother is 32, how old was the mother when the child was born?",
                "options": ["22 years", "24 years", "26 years", "28 years"],
                "answer": 1,
                "hint": "Calculate 32 minus 8.",
                "explanation": "32 - 8 = 24. The mother was 24 years old when the child was born."
            },
            {
                "question": "What happens to the age difference between two siblings as years pass?",
                "options": ["It increases", "It decreases", "It stays exactly the same", "It doubles every five years"],
                "answer": 2,
                "hint": "Both siblings grow older by 1 year every single year.",
                "explanation": "Because both individuals age at the identical rate, their age gap never changes."
            }
        ]
    },
    {
        "id": 6,
        "title": "Birth Certificate Reading",
        "subtitle": "Interpreting Official Records & Milestone Dates",
        "speech": (
            "An official government birth certificate is a legal document recording the exact moment a child enters the world. "
            "Let us examine the key pieces of information recorded on a standard village panchayat or municipal birth certificate with careful "
            "attention. The certificate prominently displays the child's full registered name, gender, registration number, and the exact "
            "date of birth written in both numbers and formal words. For instance, a certificate might state the date of birth as second of May, "
            "two thousand sixteen, written numerically as zero two slash zero five slash two thousand sixteen. The document also records the "
            "place of birth, parental names, and the formal registration date. By examining this birth date, we can calculate important future "
            "milestones. For example, to find how old this child will be on second May two thousand twenty-six, we subtract two thousand "
            "sixteen from two thousand twenty-six, discovering the child will celebrate their tenth birthday. To determine when the child turned "
            "five years old, we add five to two thousand sixteen, arriving at two thousand twenty-one. Learning to interpret official birth "
            "records teaches children how real civic administration uses mathematics to maintain vital societal records across our nation."
        ),
        "checkpoints": [
            {
                "question": "If a child was born on 02/05/2016, how old will the child be on 02/05/2026?",
                "options": ["8 years", "9 years", "10 years", "12 years"],
                "answer": 2,
                "hint": "Calculate 2026 minus 2016.",
                "explanation": "2026 - 2016 = 10. The child will be exactly 10 years old."
            },
            {
                "question": "What is the birth month represented by the number 05 in the date 02/05/2016?",
                "options": ["March", "April", "May", "June"],
                "answer": 2,
                "hint": "Count the fifth month of the calendar year.",
                "explanation": "The fifth month of the calendar year is May."
            }
        ]
    },
    {
        "id": 7,
        "title": "Milestone School Timelines",
        "subtitle": "Chronological Progression & Grade Milestones",
        "speech": (
            "Our educational journey is filled with memorable milestones arranged along an ordered timeline of continuous time. Consider a typical "
            "student's timeline through early school years. A child born in the year two thousand sixteen joins nursery school at age three in "
            "the year two thousand nineteen. The child enters kindergarten in two thousand twenty, and reaches Grade One at age six in the "
            "year two thousand twenty-two. Continuing this steady progression, the child enters Grade Two in two thousand twenty-three and "
            "reaches Grade Three in two thousand twenty-four at age eight. We can represent these events on a horizontal timeline line, "
            "where equal distances represent equal intervals of one year. Notice how chronological order requires earlier events to appear "
            "on the left, progressing steadily toward current and future events on the right. If a certificate of merit was awarded two years "
            "after joining Grade One, we jump two steps forward from two thousand twenty-two to two thousand twenty-four. Organizing milestones "
            "chronologically helps us see how past accomplishments build upon each other, allowing us to plan future academic goals with "
            "clarity, structure, and a deep appreciation for steady personal growth over time throughout our school years."
        ),
        "checkpoints": [
            {
                "question": "If a child enters Grade 1 in 2022, in what year will the child enter Grade 3?",
                "options": ["2023", "2024", "2025", "2026"],
                "answer": 1,
                "hint": "Grade 3 is 2 years after Grade 1.",
                "explanation": "2022 + 2 = 2024. The child enters Grade 3 in 2024."
            },
            {
                "question": "On a horizontal historical timeline, where do earlier events appear relative to later events?",
                "options": ["To the right", "To the left", "In random positions", "Only at the very top"],
                "answer": 1,
                "hint": "Standard timelines read from left to right like text.",
                "explanation": "Earlier events are placed on the left, progressing toward later events on the right."
            }
        ]
    },
    {
        "id": 8,
        "title": "Analog Clock Anatomy",
        "subtitle": "Clock Face Geometry, Hands & Tick Marks",
        "speech": (
            "Let us step from days and years into hours and minutes by studying the anatomy of an analog clock with focused attention. "
            "An analog clock face is a circle divided into twelve equal large intervals, marked by the numbers one through twelve. Inside "
            "this dial, two primary hands rotate clockwise around the center point. The shorter, thicker hand is the hour hand, while the longer "
            "hand is the minute hand. Around the outer circumference, there are sixty small tick marks, each representing one individual minute. "
            "The distance between any two consecutive large numbers represents five minutes because sixty divided by twelve equals five. When "
            "the minute hand points directly at twelve, it indicates zero minutes past the hour, or an exact o'clock. As the minute hand travels "
            "from twelve to one, five minutes have elapsed. When it reaches six, thirty minutes have elapsed, which is half of sixty minutes. "
            "Meanwhile, the hour hand moves much more slowly, taking one full hour just to crawl from one number to the next. Learning how these "
            "two hands move together at different speeds is the essential mathematical foundation for reading time accurately and punctually throughout your entire life."
        ),
        "checkpoints": [
            {
                "question": "How many minutes are represented between two consecutive numbers on a clock dial?",
                "options": ["1 minute", "5 minutes", "10 minutes", "12 minutes"],
                "answer": 1,
                "hint": "Divide 60 total dial minutes by 12 hour numbers.",
                "explanation": "60 divided by 12 equals 5 minutes between each consecutive number."
            },
            {
                "question": "Which hand on an analog clock moves faster?",
                "options": ["The shorter hour hand", "The longer minute hand", "Both hands move at identical speed", "Neither hand moves"],
                "answer": 1,
                "hint": "One hand completes a full circle in 60 minutes, while the other takes 12 hours.",
                "explanation": "The minute hand completes a full rotation every 60 minutes, moving 12 times faster than the hour hand."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(slides_part1)} slides for Part 1.")
    for s in slides_part1:
        words = len(s["speech"].strip().split())
        title_words = len(s["title"].strip().split())
        print(f"Slide {s['id']}: '{s['title']}' ({title_words} words) -> Speech: {words} words")
        assert 1 <= title_words <= 3, f"Title length violation on slide {s['id']}"
        assert 195 <= words <= 215, f"Speech word count {words} out of range (195-215) on slide {s['id']}"
    print("Part 1 passed all strict validation checks!")
