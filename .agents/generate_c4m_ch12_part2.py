# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 12: Ticking Clocks and Turning Calendar
Part 2: Slides 9 to 16 Data Generator
Strictly 195 to 215 words per speech lecture.
Zero human names (Parv, Raghav, Raghu, Rani, etc. replaced with generic roles).
Clean Unicode throughout (×, ÷, °, +, -, =).
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Fractions Of Time",
        "section": "Circular Clock Sectors & Fractional Hours",
        "speech": (
            "Connecting traditional circular clock faces with geometric fractions reveals how circular geometry naturally represents parts of "
            "an hour. A standard clock dial forms a complete circle of three hundred sixty degrees, containing sixty individual minute tick marks. "
            "When the long minute hand travels half-way around the dial from twelve down to six, it sweeps across exactly thirty minutes. Because "
            "thirty minutes is half of sixty minutes, we call this duration half an hour, written as the fraction one-half! If the minute hand "
            "travels one-quarter of the way around the dial from twelve to three, it sweeps across fifteen minutes, which is one-quarter of an hour! "
            "When fifteen minutes have passed after an hour, timekeepers say quarter past the hour, such as quarter past four for four-fifteen. "
            "When the minute hand sweeps three-quarters of the circle from twelve to nine, it covers forty-five minutes, representing three-quarters "
            "of an hour! Because only fifteen minutes remain until the next hour, we say quarter to the upcoming hour, such as quarter to five for "
            "four-forty-five! Clearly visualizing shaded sectors on clock dials reinforces fraction concepts, proving that sixty-minute intervals "
            "partition smoothly into halves, quarters, and three-quarters during our daily study schedules and routines."
        ),
        "checkpoints": [
            {
                "q": "How many minutes are in one-quarter (1/4) of an hour?",
                "options": ["10 minutes", "15 minutes", "20 minutes", "30 minutes"],
                "ans": 1,
                "exp": "60 minutes ÷ 4 = 15 minutes."
            },
            {
                "q": "What time is represented by 'quarter to 6'?",
                "options": ["5:15", "5:30", "5:45", "6:15"],
                "ans": 2,
                "exp": "'Quarter to 6' means 15 minutes before 6:00, which is 5:45."
            }
        ]
    },
    {
        "id": 10,
        "title": "Clock Reading Errors",
        "section": "Hand Discrimination & Diagnostic Analysis",
        "speech": (
            "Learning to read an analog clock accurately requires careful visual discrimination between the short hour hand and the long minute hand. "
            "Beginner timekeepers often make common diagnostic errors that teachers love to explore and clarify. The most frequent mistake happens "
            "when a student reads the minute hand as if it were an hour hand! For example, when the minute hand points directly at the numeral seven, "
            "an untrained student might mistakenly announce that it is seven minutes. But each number on the clock dial represents a five-minute jump! "
            "Counting by fives: seven times five equals thirty-five minutes! Another tricky trap occurs when reading the hour hand as it approaches "
            "the next number. At eight-fifty, the minute hand points to ten, and the hour hand has crept very close to the nine. Looking quickly, an "
            "inattentive observer might incorrectly call the time nine-fifty! But because the minute hand has not yet reached twelve, the hour is still "
            "eight, making the correct time eight-fifty! Recognizing that the short hand measures completed hours while the long hand counts elapsed "
            "five-minute steps prevents common reading blunders, instilling lasting precision and confidence whenever reading traditional ticking wall clocks at school."
        ),
        "checkpoints": [
            {
                "q": "When the long minute hand points to 7 on the clock face, how many minutes have passed?",
                "options": ["7 minutes", "25 minutes", "35 minutes", "42 minutes"],
                "ans": 2,
                "exp": "Each clock number equals 5 minutes. 7 × 5 = 35 minutes."
            },
            {
                "q": "If the hour hand is between 4 and 5 (close to 5) and the minute hand points to 10, what time is it?",
                "options": ["5:50", "4:50", "4:10", "5:10"],
                "ans": 1,
                "exp": "The hour hand has not reached 5 yet; it is 10 minutes before 5, which is 4:50."
            }
        ]
    },
    {
        "id": 11,
        "title": "Time Duration Tracking",
        "section": "Study Schedules & Activity Log Intervals",
        "speech": (
            "Managing daily study timetables, athletic sports practice sessions, and creative recreational hobbies requires tracking how long "
            "activities last across our busy afternoons. For example, suppose an organized fourth-grade student sits down to complete mathematics "
            "homework at five-fifteen PM. The student works with steady concentration until six o'clock PM, and then switches immediately to reading "
            "an adventure storybook until six-forty-five PM. How much total time did this diligent student spend studying altogether? Let us break "
            "the session into two distinct chronological intervals. First, from five-fifteen PM to six o'clock PM is exactly forty-five minutes of "
            "mathematics problem-solving. Next, from six o'clock PM to six-forty-five PM is another dedicated forty-five minutes of literature "
            "reading. Adding both individual durations together: forty-five minutes plus forty-five minutes equals ninety minutes! Since sixty minutes "
            "constitute one full hour, ninety minutes can be expressed as one hour and thirty minutes, or one and a half hours! Keeping an active "
            "daily time log encourages responsible time budgeting, helping young learners balance school assignments with outdoor playground games, "
            "evening household chores, and restful sleep. Regularly practicing duration tracking strengthens mental addition, builds self-discipline, "
            "and proves that every minute invested in focused learning yields rewarding intellectual growth and life skills."
        ),
        "checkpoints": [
            {
                "q": "A student does math homework for 45 minutes and reads for 45 minutes. What is the total study time?",
                "options": ["1 hour 15 minutes", "1 hour 30 minutes", "1 hour 45 minutes", "2 hours 00 minutes"],
                "ans": 1,
                "exp": "45 min + 45 min = 90 min = 1 hour 30 minutes."
            },
            {
                "q": "If soccer practice begins at 4:20 PM and ends at 5:50 PM, how long did the practice last?",
                "options": ["1 hour 10 minutes", "1 hour 20 minutes", "1 hour 30 minutes", "1 hour 40 minutes"],
                "ans": 2,
                "exp": "4:20 PM to 5:20 PM is 1 hour; 5:20 PM to 5:50 PM is 30 minutes. Total = 1 hour 30 minutes."
            }
        ]
    },
    {
        "id": 12,
        "title": "Railway Time Schedules",
        "section": "Midnight Crossing & Long-Distance Journeys",
        "speech": (
            "Indian Railways operates one of the largest passenger train networks in the world, running thousands of express trains day and night "
            "across our vast subcontinent. To ensure flawless operational coordination across multiple states, railway timetables exclusively "
            "use the twenty-four-hour system. Many popular express trains embark on overnight journeys that cross midnight, introducing an exciting "
            "mathematical duration puzzle! Suppose the famous Rajdhani Express departs from New Delhi railway station at twenty-hundred-fifteen hours, "
            "which corresponds to eight-fifteen PM in the evening. The train arrives at its destination station the following morning at zero-eight-forty-five "
            "hours, or eight-forty-five AM. How long was the entire overnight journey? To solve this, we split the calculation at midnight, which is "
            "twenty-four-hundred hours. From twenty-hundred-fifteen hours to midnight is three hours and forty-five minutes. From midnight to zero-eight-forty-five "
            "hours the next morning is eight hours and forty-five minutes. Adding these two segments: three hours plus eight hours equals eleven hours, "
            "while forty-five minutes plus forty-five minutes equals ninety minutes! Regrouping sixty minutes as one hour gives twelve hours and thirty "
            "minutes! Railway schedule arithmetic connects classroom time measurement with cross-country travel, illustrating how twenty-four-hour "
            "clocks keep millions of passengers moving safely and punctually every single day."
        ),
        "checkpoints": [
            {
                "q": "A train departs at 20:15 (8:15 PM) and arrives at midnight (24:00). How long was this first segment?",
                "options": ["3 hours 15 minutes", "3 hours 45 minutes", "4 hours 15 minutes", "4 hours 45 minutes"],
                "ans": 1,
                "exp": "24:00 - 20:15 = 3 hours 45 minutes."
            },
            {
                "q": "An overnight train travels 3 hours 45 minutes before midnight and 8 hours 45 minutes after midnight. What is the total duration?",
                "options": ["11 hours 30 minutes", "12 hours 00 minutes", "12 hours 30 minutes", "13 hours 15 minutes"],
                "ans": 2,
                "exp": "3h 45m + 8h 45m = 11h 90m = 12 hours 30 minutes."
            }
        ]
    },
    {
        "id": 13,
        "title": "Shelf Life Inspection",
        "section": "Commercial Label Audits & Quality Control",
        "speech": (
            "Professional food inspectors, store accountants, and conscientious shoppers conduct careful shelf life audits on packaged goods to "
            "ensure that families consume only fresh, safe, and wholesome groceries. Let us examine how calendar arithmetic verifies product safety "
            "across various common household food items. Consider a carton of fresh pasteurized milk with a manufacturing date of twelve-zero-eight-twenty-twenty-four "
            "and a declared shelf life of four days. Simply adding four days to the twelfth gives sixteen-zero-eight-twenty-twenty-four as the official "
            "final expiry date. Next, consider a sealed tin of nutritious baby cereal manufactured on twenty-five-zero-three-twenty-twenty-four, bearing "
            "a clear best-before label of twelve months. Adding twelve full calendar months advances the year by one, setting the expiry date at "
            "twenty-five-zero-three-twenty-twenty-five! Furthermore, what if an antiseptic medical ointment tube is manufactured on fifteen-eleven-twenty-twenty-three "
            "with a verified shelf life of eighteen months? Twelve months brings us to fifteen November twenty-twenty-four, and the remaining six months "
            "advance the date to fifteen May twenty-twenty-five! If an observant store clerk discovers an expired product on display shelves, it must "
            "be removed immediately without delay. Regularly practicing commercial shelf life audits reinforces multi-month addition, leap year awareness, "
            "and real-world consumer safety vigilance across local neighborhood markets, supermarkets, and grocery stores."
        ),
        "checkpoints": [
            {
                "q": "A food product manufactured on 15/11/2023 has a shelf life of 18 months. What is its expiry date?",
                "options": ["15/05/2024", "15/11/2024", "15/05/2025", "15/11/2025"],
                "ans": 2,
                "exp": "15/11/2023 + 12 months = 15/11/2024; + 6 months = 15/05/2025."
            },
            {
                "q": "If yoghurt made on 02/09/2024 has an expiry date of 09/09/2024, what is its shelf life?",
                "options": ["5 days", "7 days", "10 days", "14 days"],
                "ans": 1,
                "exp": "9 - 2 = 7 days (1 week)."
            }
        ]
    },
    {
        "id": 14,
        "title": "Days And Weeks",
        "section": "Modular Seven Calendar Sequences & Cycles",
        "speech": (
            "The calendar week is an ancient, unbroken seven-day cycle that governs school timetables, public holidays, and weekend rest periods. "
            "The seven days of the week, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, and Sunday, repeat endlessly in predictable succession. "
            "Because a week contains exactly seven days, any future date that is an exact multiple of seven days away will fall on the exact same day "
            "of the week! For instance, if the third day of October is a Wednesday, adding seven days tells us that the tenth of October must also be "
            "a Wednesday! Adding another seven days reveals that the seventeenth and twenty-fourth of October are Wednesdays as well. This cyclic property "
            "is based on modular arithmetic base-seven. How many weeks and days are in an ordinary month of thirty-one days? Dividing thirty-one by seven "
            "yields four weeks with three days remaining, since four times seven equals twenty-eight, and twenty-eight plus three equals thirty-one! "
            "In an ordinary year of three hundred sixty-five days, dividing by seven reveals fifty-two full weeks plus one odd day! This is why ordinary "
            "years begin and end on the exact same day of the week, demonstrating the elegant mathematical structure linking days, weeks, and calendar cycles."
        ),
        "checkpoints": [
            {
                "q": "If the 3rd of a month is a Wednesday, what day of the week will the 17th of the same month be?",
                "options": ["Tuesday", "Wednesday", "Thursday", "Friday"],
                "ans": 1,
                "exp": "17 - 3 = 14 days, which is exactly 2 full weeks (2 × 7 = 14). So it is also Wednesday."
            },
            {
                "q": "How many full weeks and leftover days are in an ordinary year of 365 days?",
                "options": ["50 weeks and 5 days", "51 weeks and 2 days", "52 weeks and 1 day", "52 weeks and 2 days"],
                "ans": 2,
                "exp": "365 ÷ 7 = 52 weeks with a remainder of 1 day (52 × 7 = 364; 364 + 1 = 365)."
            }
        ]
    },
    {
        "id": 15,
        "title": "Century Leap Rules",
        "section": "Solar Calibration & Four-Hundred Year Cycles",
        "speech": (
            "While most students know that leap years occur every four years, advanced calendar mathematics includes an ingenious fine-tuning rule "
            "created by sixteenth-century astronomers. If the Earth's orbit took exactly three hundred sixty-five days and six hours, adding one leap "
            "day every four years would be completely perfect. But precise astronomical measurements reveal that Earth actually takes three hundred "
            "sixty-five days, five hours, forty-eight minutes, and forty-five seconds to orbit the Sun. That is about eleven minutes less than six hours! "
            "Adding a leap day every four years slightly overcompensates, adding about three extra days every four hundred years! To correct this subtle "
            "error, the Gregorian calendar introduced the century leap year rule: century years ending in double zeros are leap years only if they are "
            "divisible by four hundred! Under this rule, the century year sixteen hundred was a leap year, and the year two thousand was a leap year "
            "because two thousand is divisible by four hundred. However, the century years seventeen hundred, eighteen hundred, and nineteen hundred were "
            "ordinary years, and twenty-one hundred will not be a leap year! This brilliant mathematical adjustment keeps our calendar accurate to within "
            "one day every three thousand years."
        ),
        "checkpoints": [
            {
                "q": "According to the century leap rule, which of the following century years was a leap year?",
                "options": ["1700", "1800", "1900", "2000"],
                "ans": 3,
                "exp": "2000 ÷ 400 = 5 with remainder 0, so 2000 was a leap year."
            },
            {
                "q": "Will the upcoming century year 2100 be a leap year?",
                "options": ["Yes, because it is divisible by 4", "No, because century years must be divisible by 400, and 2100 is not", "Yes, because all century years are leap years", "Cannot be determined"],
                "ans": 1,
                "exp": "2100 ÷ 400 = 5 with remainder 100, so 2100 will be an ordinary year with 28 days in February."
            }
        ]
    },
    {
        "id": 16,
        "title": "Time Arithmetic Logic",
        "section": "Base-Sixty Regrouping & Minute Borrowing",
        "speech": (
            "Adding and subtracting time requires mastering a unique mathematical base called the sexagesimal system, or base-sixty arithmetic, "
            "inherited from ancient Babylonian astronomers. Unlike our standard base-ten decimal system where we bundle ten units into one ten and ten "
            "tens into one hundred, time arithmetic bundles sixty seconds into one minute, and sixty minutes into one hour! Suppose we must add two "
            "hours and forty-five minutes to three hours and thirty-five minutes. Adding the minutes first: forty-five plus thirty-five equals eighty "
            "minutes. Because eighty exceeds sixty, we unbundle sixty minutes into one full hour, leaving twenty minutes behind! Adding the hours: two "
            "plus three plus our carried one hour equals six hours, giving a total of six hours and twenty minutes! Subtraction requires the inverse "
            "regrouping. Suppose we subtract one hour and fifty minutes from four hours and twenty minutes. Because we cannot subtract fifty minutes "
            "from twenty minutes, we borrow one hour from the four hours, leaving three hours. When that borrowed hour enters the minute column, it "
            "transforms into sixty minutes! Adding sixty to twenty gives eighty minutes, and eighty minus fifty leaves thirty minutes! Base-sixty "
            "arithmetic provides the universal foundation for global navigation, astronomical calculations, and everyday timekeeping."
        ),
        "checkpoints": [
            {
                "q": "What is the sum of 2 hours 45 minutes and 3 hours 35 minutes?",
                "options": ["5 hours 80 minutes", "6 hours 10 minutes", "6 hours 20 minutes", "6 hours 30 minutes"],
                "ans": 2,
                "exp": "45m + 35m = 80m = 1h 20m. 2h + 3h + 1h = 6 hours 20 minutes."
            },
            {
                "q": "In subtracting time, when you borrow 1 hour into the minutes column, how many minutes do you add?",
                "options": ["10 minutes", "50 minutes", "60 minutes", "100 minutes"],
                "ans": 2,
                "exp": "1 hour equals 60 minutes in base-60 time arithmetic."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(slides_part2)} slides for Part 2.")
    for s in slides_part2:
        wc = len(s["speech"].split())
        tw = len(s["title"].split())
        print(f"Slide {s['id']}: {s['title']} -> {wc} words (Title: {tw} words)")
        assert 1 <= tw <= 3, f"Title '{s['title']}' must be 1 to 3 words"
        assert 195 <= wc <= 215, f"Word count {wc} out of bounds for slide {s['id']}!"
        assert len(s["checkpoints"]) == 2, f"Slide {s['id']} must have 2 checkpoints"
    print("All Part 2 slide constraints validated successfully!")
