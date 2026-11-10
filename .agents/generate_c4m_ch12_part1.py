# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 12: Ticking Clocks and Turning Calendar
Part 1: Slides 1 to 8 Data Generator
Strictly 195 to 215 words per speech lecture.
Zero human names (Parv, Raghav, Raghu, Rani, etc. replaced with generic roles).
Clean Unicode throughout (×, ÷, °, +, -, =).
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Leap Year Calendar",
        "section": "Solar Orbit & February Twenty-Ninth",
        "speech": (
            "Welcome to the fascinating study of time and calendars, where planetary motions dictate our daily clocks and yearly seasons! "
            "Under our standard Gregorian solar calendar, an ordinary year contains precisely three hundred sixty-five days. However, the Earth "
            "takes approximately three hundred sixty-five days and six hours to complete one full revolution around the Sun. Because an ordinary "
            "calendar counts only full days, those extra six hours accumulate silently year after year. Over four consecutive years, four times "
            "six hours equals twenty-four extra hours, which creates exactly one full additional day! To keep our calendar perfectly synchronized "
            "with the astronomical seasons, this extra day is added to the shortest month of the year, February. While February normally has "
            "twenty-eight days, during a leap year it gains an extra day, giving it twenty-nine days, and making the entire year three hundred "
            "sixty-six days long! A child born on February twenty-ninth is lovingly called a leapling, celebrating an official calendar birthday "
            "once every four years! Notice that leap years are divisible by four: twenty-twenty, twenty-twenty-four, and twenty-twenty-eight are "
            "all leap years. Regularly understanding leap years reveals how astronomers and mathematicians harmonize human timekeeping with "
            "cosmic planetary cycles across generations."
        ),
        "checkpoints": [
            {
                "q": "How many days are there in a standard leap year?",
                "options": ["364 days", "365 days", "366 days", "368 days"],
                "ans": 2,
                "exp": "A leap year has 366 days because February receives an extra 29th day."
            },
            {
                "q": "Which of the following years is a leap year?",
                "options": ["2022", "2023", "2024", "2025"],
                "ans": 2,
                "exp": "2024 is evenly divisible by 4 (2024 ÷ 4 = 506 with remainder 0), making it a leap year."
            }
        ]
    },
    {
        "id": 2,
        "title": "Date Formats Math",
        "section": "Standard Notation & Calendar Intervals",
        "speech": (
            "Dates allow us to record historical milestones, schedule school events, and celebrate birthdays with orderly precision. In India and "
            "many parts of the world, dates are officially written using the day-month-year format, abbreviated as DD-MM-YYYY. In this layout, "
            "the first two digits represent the calendar day, the middle two digits signify the month of the year, and the final four digits denote "
            "the calendar year. For instance, the fifteenth of August nineteen forty-seven is written as fifteen-zero-eight-nineteen-forty-seven. "
            "Translating between month numbers and names requires remembering their calendar order: zero-one represents January, zero-two represents "
            "February, and twelve represents December. Calculating age differences from birth dates is another valuable mathematical skill. For "
            "example, if an energetic young learner was born on the tenth of March twenty-fourteen, how old will that student be on the tenth of "
            "March twenty-twenty-four? Because the day and month match, we simply subtract the birth year from the target year: twenty-twenty-four "
            "minus twenty-fourteen equals exactly ten years of age! Regularly tracking consecutive calendar days, yesterday, today, and tomorrow, "
            "reinforces cyclic modular arithmetic base-seven, proving that standard date formatting transforms flowing chronological time into "
            "organized, calculable mathematical records for civil society and school documentation."
        ),
        "checkpoints": [
            {
                "q": "In the standard date format DD/MM/YYYY, what does the date 05/09/2026 represent?",
                "options": ["May 9, 2026", "5 September 2026", "9 May 2026", "5 October 2026"],
                "ans": 1,
                "exp": "DD is 05 (fifth day), MM is 09 (ninth month, September), and YYYY is 2026."
            },
            {
                "q": "If a person was born on 12/04/2012, how old will they be on 12/04/2024?",
                "options": ["10 years", "11 years", "12 years", "14 years"],
                "ans": 2,
                "exp": "2024 - 2012 = 12 years."
            }
        ]
    },
    {
        "id": 3,
        "title": "Product Expiry Dates",
        "section": "Consumer Protection & Shelf Life Calculations",
        "speech": (
            "Whenever you visit a grocery store or bakery, inspecting package labels is an essential consumer safety habit grounded in practical "
            "date arithmetic. Commercial food products, dairy cartons, medicine bottles, and packaged snacks display two vital dates: the manufacturing "
            "date, abbreviated as M-F-G, and the expiry or best-before date, often abbreviated as E-X-P. The manufacturing date tells us precisely "
            "when the item was produced in the factory, while the expiry date indicates the final date until which the product remains fresh, safe, "
            "and wholesome to consume. The duration between these two critical dates is called the product shelf life. Suppose a box of wholesome "
            "butter cookies displays a manufacturing date of zero-five-zero-one-twenty-twenty-four, and the commercial package label clearly specifies "
            "best before six months from manufacture. When does this product expire? Adding six full calendar months to January brings us to the fifth "
            "of July twenty-twenty-four! If an alert customer inspects the package on the tenth of August, the cookies are past their expiry date "
            "and should never be purchased. Carefully calculating product shelf life in months and days protects public community health, effectively "
            "prevents accidental food waste, and vividly illustrates how practical calendar math directly safeguards our everyday physical wellbeing."
        ),
        "checkpoints": [
            {
                "q": "If milk is packed on 14/07/2024 with a shelf life of 3 days, by what date must it be consumed?",
                "options": ["15/07/2024", "16/07/2024", "17/07/2024", "20/07/2024"],
                "ans": 2,
                "exp": "14 + 3 = 17, so the milk must be consumed by 17/07/2024."
            },
            {
                "q": "A packet of biscuits manufactured in March 2024 states 'Best before 6 months'. Which is the last safe consumption month?",
                "options": ["July 2024", "August 2024", "September 2024", "October 2024"],
                "ans": 2,
                "exp": "Month 3 (March) + 6 months = Month 9 (September 2024)."
            }
        ]
    },
    {
        "id": 4,
        "title": "Community Lunar Calendars",
        "section": "Cultural Astronomy & Lunar Month Cycles",
        "speech": (
            "While the solar Gregorian calendar governs international civic commerce, rich community calendars celebrate cultural heritage and "
            "astronomical traditions across diverse civilizations. India has a vibrant tradition of lunisolar calendars, such as the Saka and "
            "Vikram Samvat calendars, alongside the Islamic Hijri calendar, the Sikh Nanakshahi calendar, and regional harvesting calendars. Unlike "
            "solar calendars that track only the Earth's orbit around the Sun, lunar calendars track the recurring phases of the Moon! A complete "
            "lunar cycle lasts approximately twenty-nine and a half days, moving from the invisible new moon, called Amavasya, to the glowing full "
            "moon, called Purnima. In traditional Indian calendars, each month is divided into two fortnights or pakshes of fifteen lunar days each: "
            "Shukla Paksha, the waxing fortnight of growing moonlight, and Krishna Paksha, the waning fortnight of fading light. Celebrated community "
            "festivals like Diwali, Eid, Gurpurab, and Holi are all determined by these celestial lunar positions! Traditional calendars also feature "
            "poetic month names like Chaitra, Vaisakha, Kartika, and Ramadan. Exploring community calendars deepens our cultural appreciation, showing "
            "that time can be measured through changing shadows of the Moon just as meaningfully as by the ticking hands of mechanical clocks everywhere in daily life."
        ),
        "checkpoints": [
            {
                "q": "How long does a complete lunar phase cycle (from one new moon to the next) last approximately?",
                "options": ["7 days", "15 days", "29.5 days", "365 days"],
                "ans": 2,
                "exp": "A synodic lunar month lasts approximately 29.5 days."
            },
            {
                "q": "In the Indian lunar calendar, what is the fortnight of the waxing (brightening) moon called?",
                "options": ["Krishna Paksha", "Shukla Paksha", "Amavasya", "Purnima"],
                "ans": 1,
                "exp": "Shukla Paksha is the bright waxing fortnight leading up to the full moon (Purnima)."
            }
        ]
    },
    {
        "id": 5,
        "title": "Daily Routine Wheel",
        "section": "Daily Routine Cycles & Elapsed Durations",
        "speech": (
            "Have you ever wondered how many hours comprise one full natural day on Earth? One complete planetary rotation of the Earth upon its "
            "axis takes exactly twenty-four hours! To visualize this uninterrupted cycle, mathematicians and medical planners use a circular twenty-four-hour "
            "routine wheel. Imagine a large wheel divided into twenty-four equal wedges, with each wedge representing one sixty-minute hour. Let us "
            "examine a hospital doctor's busy daily routine plotted on this wheel. The doctor sleeps soundly from eleven o'clock at night until six "
            "o'clock in the morning. Counting the hourly sectors between eleven PM and six AM reveals exactly seven hours of restful sleep! During the "
            "day, the doctor consults patients at the clinic from nine AM until one PM, which totals four hours of medical service. Following lunch, "
            "hospital rounds continue from three PM to seven PM, adding another four hours of healthcare work. The remaining hours are spent cooking "
            "fresh meals, reading, exercising, and enjoying family conversation. Summing all the segments: seven hours sleeping, eight hours working, "
            "and nine hours of meals and relaxation equals exactly twenty-four hours! The twenty-four-hour wheel teaches us how to budget time "
            "wisely, balance responsibilities, and calculate elapsed durations effortlessly."
        ),
        "checkpoints": [
            {
                "q": "How many total hours are there in one complete day and night cycle?",
                "options": ["12 hours", "18 hours", "24 hours", "30 hours"],
                "ans": 2,
                "exp": "One full rotation of Earth on its axis takes exactly 24 hours."
            },
            {
                "q": "If a doctor sleeps from 11:00 PM to 6:00 AM, how many hours of sleep did the doctor get?",
                "options": ["6 hours", "7 hours", "8 hours", "9 hours"],
                "ans": 1,
                "exp": "From 11 PM to midnight is 1 hour; from midnight to 6 AM is 6 hours. 1 + 6 = 7 hours."
            }
        ]
    },
    {
        "id": 6,
        "title": "Twelve Hour Clocks",
        "section": "Ante Meridiem & Post Meridiem Notation",
        "speech": (
            "Most standard analog wall clocks and household wristwatches feature a circular dial numbered sequentially from one through twelve. "
            "Because a full day contains twenty-four hours, the short hour hand must travel around the clock face twice every day! This creates an "
            "interesting ambiguity: when a clock displays eight o'clock, is it time for morning school assembly, or time for evening bedtime? To "
            "resolve this confusion, timekeepers use two Latin designations: AM and PM. AM stands for Ante Meridiem, which translates to before "
            "midday, while PM stands for Post Meridiem, meaning after midday! The critical dividing line occurs precisely at twelve noon, when the "
            "radiant Sun reaches its highest point in the sky. Midnight, the moment the new calendar day begins, is designated as twelve midnight "
            "or twelve AM. From twelve midnight until twelve noon, all times are labeled AM: seven AM is breakfast time, and ten AM is morning class. "
            "At twelve noon, the label shifts to PM. From twelve noon until midnight, times are labeled PM: five PM is playground playtime, and eight "
            "PM is evening dinner! AM and PM notation ensures clear, unambiguous communication across school timetables, television schedules, train "
            "timetables, flight rosters, and everyday social appointments."
        ),
        "checkpoints": [
            {
                "q": "What does the Latin abbreviation 'AM' stand for in 12-hour time?",
                "options": ["After Midnight", "Ante Meridiem (before midday)", "All Morning", "Annual Meeting"],
                "ans": 1,
                "exp": "AM stands for Ante Meridiem, meaning before midday (the period from midnight to noon)."
            },
            {
                "q": "Which time notation correctly describes having dinner at 8 o'clock in the evening?",
                "options": ["8:00 AM", "8:00 PM", "8:00 Noon", "8:00 Midnight"],
                "ans": 1,
                "exp": "Evening hours following midday are designated with PM (Post Meridiem)."
            }
        ]
    },
    {
        "id": 7,
        "title": "Digital Clock Formats",
        "section": "Converting 12-Hour to 24-Hour Formats",
        "speech": (
            "While home wall clocks use twelve-hour AM and PM notation, global transportation networks, airlines, railways, and military operations "
            "rely on the twenty-four-hour digital clock format to eliminate any possibility of AM and PM confusion. In a standard twenty-four-hour "
            "digital clock, each day starts officially at midnight as zero-zero-zero-zero hours, and counts continuously upwards to twenty-three-fifty-nine! "
            "Morning times from one AM to twelve noon look almost identical in both systems: seven AM is written as zero-seven-hundred hours, and "
            "eleven-thirty AM is written as eleven-thirty hours. However, once the clock passes twelve noon, the hours do not reset back to one! "
            "Instead, they continue counting upwards: one PM becomes thirteen-hundred hours, two PM becomes fourteen-hundred hours, and eight PM "
            "becomes twenty-hundred hours! The universal rule for converting any PM time to twenty-four-hour time is simple: just add twelve to the "
            "hour! For example, six-fifteen PM plus twelve hours equals eighteen-fifteen hours on the digital display! Conversely, to convert a "
            "twenty-four-hour time back to PM notation, simply subtract twelve hours: twenty-one-thirty minus twelve equals nine-thirty PM! Mastering "
            "twenty-four-hour digital time enables observant young scholars to read train tickets, airport departure boards, and international broadcast "
            "schedules with absolute confidence and mathematical clarity."
        ),
        "checkpoints": [
            {
                "q": "How is 8:00 PM represented on a 24-hour digital railway clock?",
                "options": ["08:00 hours", "18:00 hours", "20:00 hours", "22:00 hours"],
                "ans": 2,
                "exp": "8:00 PM + 12:00 = 20:00 hours."
            },
            {
                "q": "What 12-hour AM/PM time corresponds to 17:30 hours on a train ticket?",
                "options": ["5:30 AM", "5:30 PM", "7:30 PM", "3:30 PM"],
                "ans": 1,
                "exp": "17:30 - 12:00 = 5:30 PM."
            }
        ]
    },
    {
        "id": 8,
        "title": "Elapsed Time Intervals",
        "section": "Analog Clocks & Duration Subtraction",
        "speech": (
            "Calculating elapsed time, the exact duration that elapses between a starting moment and an ending moment, is one of the most practical "
            "skills in elementary mathematics. Consider a diligent dairy courier who starts delivering fresh milk packets to neighborhood homes at "
            "six-fifteen in the morning. When the final crate is delivered and the courier returns to the depot, the analog clock displays seven-forty "
            "AM. How long did the delivery route take? To calculate elapsed time on an analog clock, we break the interval into manageable benchmark "
            "steps. From six-fifteen AM, advancing forty-five minutes brings us to the friendly top of the hour: seven o'clock! From seven o'clock to "
            "seven-forty AM is another forty minutes. Adding both chunks together: forty-five minutes plus forty minutes equals eighty-five minutes! "
            "Because sixty minutes make one full hour, eighty-five minutes is equal to one hour and twenty-five minutes! Alternatively, we can "
            "subtract the starting time from the ending time: seven hours and forty minutes minus six hours and fifteen minutes yields one hour and "
            "twenty-five minutes. Tracking analog clock hands and decomposing intervals into round-hour benchmarks transforms elapsed time calculations "
            "into joyful mental agility across our daily routines and chores."
        ),
        "checkpoints": [
            {
                "q": "A delivery courier starts at 6:15 AM and finishes at 7:40 AM. How long did the delivery route take?",
                "options": ["1 hour 15 minutes", "1 hour 25 minutes", "1 hour 35 minutes", "2 hours 05 minutes"],
                "ans": 1,
                "exp": "From 6:15 to 7:15 is 1 hour. From 7:15 to 7:40 is 25 minutes. Total = 1 hour 25 minutes."
            },
            {
                "q": "If a bus departs at 10:30 AM and arrives at 1:15 PM, what is the travel duration?",
                "options": ["2 hours 15 minutes", "2 hours 45 minutes", "3 hours 15 minutes", "3 hours 45 minutes"],
                "ans": 1,
                "exp": "10:30 AM to 12:30 PM is 2 hours; 12:30 PM to 1:15 PM is 45 minutes. Total = 2 hours 45 minutes."
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
        assert 195 <= wc <= 215, f"Word count {wc} out of bounds for slide {s['id']}!"
        assert len(s["checkpoints"]) == 2, f"Slide {s['id']} must have 2 checkpoints"
    print("All Part 1 slide constraints validated successfully!")
