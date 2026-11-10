# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 12: Ticking Clocks and Turning Calendar
Part 3: Slides 17 to 20 Data Generator (40 Quiz Questions)
Short headings: Challenge 1, Challenge 2, Challenge 3, Challenge 4.
Zero human names replaced with generic roles.
Clean Unicode throughout (×, ÷, °, +, -, =).
"""

def make_sol_html(steps, note=None):
    items = "".join(f"<li class='mb-2 text-slate-700 leading-relaxed'>{s}</li>" for s in steps)
    html = f"<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside space-y-1.5 text-sm'>{items}</ol></div>"
    if note:
        html += f"<div class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> {note}</div>"
    html += "</div>"
    return html

slides_part3 = [
    {
        "id": 17,
        "title": "Challenge 1",
        "section": "Leap Years, Calendars & Date Formats",
        "speech": "",
        "quizzes": [
            {
                "q": "How many days does an ordinary non-leap year contain?",
                "options": ["360 days", "364 days", "365 days", "366 days"],
                "ans": 2,
                "hint": "February has 28 days in an ordinary year.",
                "exp": "An ordinary year has 365 days, while a leap year has 366 days.",
                "sol": make_sol_html([
                    "The Earth takes about 365 days and 6 hours to orbit the Sun.",
                    "An ordinary calendar year rounds this to 365 full days.",
                    "The remaining 6 hours are accumulated over four years to form a leap year."
                ], "Ordinary years have 365 days; leap years have 366 days.")
            },
            {
                "q": "Why does a leap year occur every 4 years in our calendar system?",
                "options": ["To match the 4 seasons", "Because 4 extra six-hour periods accumulate into 1 full 24-hour day", "Because clocks have 4 quadrants", "By royal decree"],
                "ans": 1,
                "hint": "Earth's orbit takes 365 days plus 6 extra hours each year.",
                "exp": "4 years × 6 hours = 24 hours = 1 extra calendar day added to February.",
                "sol": make_sol_html([
                    "Each solar year has an excess of approximately 6 hours over 365 days.",
                    "Over 4 years: 4 × 6 hours = 24 hours.",
                    "24 hours equals exactly 1 full day.",
                    "This day is added to February as February 29th."
                ], "Four 6-hour orbital surpluses combine into one full leap day.")
            },
            {
                "q": "Which of the following years is a leap year?",
                "options": ["2018", "2021", "2024", "2026"],
                "ans": 2,
                "hint": "Check which year is evenly divisible by 4.",
                "exp": "2024 ÷ 4 = 506 remainder 0. 2024 is a leap year.",
                "sol": make_sol_html([
                    "To determine if a year is a leap year, check divisibility by 4.",
                    "2018 ÷ 4 = 504 remainder 2 (not a leap year).",
                    "2021 ÷ 4 = 505 remainder 1 (not a leap year).",
                    "2024 ÷ 4 = 506 remainder 0 (leap year!).",
                    "2026 ÷ 4 = 506 remainder 2 (not a leap year)."
                ], "Years divisible by 4 (except non-400 century years) are leap years.")
            },
            {
                "q": "A child is born on February 29, 2020. In which year will the child celebrate their next official calendar birthday?",
                "options": ["2021", "2022", "2023", "2024"],
                "ans": 3,
                "hint": "February 29 only appears in leap years, which occur every 4 years.",
                "exp": "2020 + 4 = 2024, the next leap year.",
                "sol": make_sol_html([
                    "February 29 occurs exclusively in leap years.",
                    "Leap years occur every 4 years.",
                    "2020 was a leap year; the next leap year is 2020 + 4 = 2024."
                ], "Leapling birthdays on February 29 occur once every four years.")
            },
            {
                "q": "In the standard date format DD/MM/YYYY, what month is indicated by 14/11/2025?",
                "options": ["January", "September", "November", "December"],
                "ans": 2,
                "hint": "Look at the middle number MM in DD/MM/YYYY.",
                "exp": "Month number 11 corresponds to November.",
                "sol": make_sol_html([
                    "In DD/MM/YYYY, MM represents the two-digit month number.",
                    "Here, MM is 11.",
                    "The 11th month of the Gregorian calendar is November."
                ], "Month numbers 01 to 12 correspond sequentially from January to December.")
            },
            {
                "q": "If an official government document is dated 15/08/1947, what historic event does it mark in words?",
                "options": ["15 August 1947 (Indian Independence Day)", "8 November 1947", "15 October 1947", "1 January 1947"],
                "ans": 0,
                "hint": "DD is 15, MM is 08 (August), YYYY is 1947.",
                "exp": "15/08/1947 translates to 15 August 1947.",
                "sol": make_sol_html([
                    "DD = 15 (fifteenth day).",
                    "MM = 08 (eighth month, August).",
                    "YYYY = 1947.",
                    "In words, this is 15 August 1947, India's Independence Day."
                ], "Standard DD/MM/YYYY records day, month, and year with clarity.")
            },
            {
                "q": "A student was born on 20/06/2014. How old will this student be on 20/06/2026?",
                "options": ["10 years old", "11 years old", "12 years old", "14 years old"],
                "ans": 2,
                "hint": "Subtract the birth year from the target year when day and month match.",
                "exp": "2026 - 2014 = 12 years old.",
                "sol": make_sol_html([
                    "Both dates share the exact same day and month: 20 June.",
                    "Birth year = 2014; Target year = 2026.",
                    "Age = 2026 - 2014 = 12 years."
                ], "Subtract birth year from target year when day and month are identical.")
            },
            {
                "q": "If today is Tuesday, what day of the week was yesterday?",
                "options": ["Sunday", "Monday", "Wednesday", "Thursday"],
                "ans": 1,
                "hint": "Yesterday is the day immediately preceding today.",
                "exp": "Monday comes directly before Tuesday.",
                "sol": make_sol_html([
                    "The days of the week in order are: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday.",
                    "Yesterday means 1 day in the past.",
                    "One day before Tuesday is Monday."
                ], "Yesterday represents the previous day in the 7-day calendar cycle.")
            },
            {
                "q": "If today is Friday, what day of the week will it be the day after tomorrow?",
                "options": ["Saturday", "Sunday", "Monday", "Tuesday"],
                "ans": 1,
                "hint": "Tomorrow is Saturday; the day after tomorrow is +2 days.",
                "exp": "Friday + 1 day = Saturday (tomorrow); + 2 days = Sunday.",
                "sol": make_sol_html([
                    "Today is Friday.",
                    "Tomorrow is Saturday (+1 day).",
                    "The day after tomorrow is Sunday (+2 days)."
                ], "The day after tomorrow represents +2 days from the present day.")
            },
            {
                "q": "How many days are in the month of February during a leap year?",
                "options": ["28 days", "29 days", "30 days", "31 days"],
                "ans": 1,
                "hint": "February receives one additional day during a leap year.",
                "exp": "February has 29 days in a leap year and 28 days in an ordinary year.",
                "sol": make_sol_html([
                    "In an ordinary year, February has 28 days.",
                    "In a leap year, an extra leap day is added, giving February 29 days."
                ], "February has 29 days during leap years.")
            }
        ]
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "section": "Expiry Dates & Community Lunar Calendars",
        "speech": "",
        "quizzes": [
            {
                "q": "A carton of milk has MFG: 12/05/2024 and EXP: 15/05/2024. What is its shelf life?",
                "options": ["2 days", "3 days", "4 days", "5 days"],
                "ans": 1,
                "hint": "Subtract the manufacturing day from the expiry day.",
                "exp": "15 - 12 = 3 days.",
                "sol": make_sol_html([
                    "Manufacturing date = 12 May 2024.",
                    "Expiry date = 15 May 2024.",
                    "Shelf life = 15 - 12 = 3 days."
                ], "Shelf life is the time difference between manufacturing and expiry dates.")
            },
            {
                "q": "A packet of potato wafers manufactured on 10/01/2024 states 'Best before 4 months'. What is the expiry date?",
                "options": ["10/03/2024", "10/04/2024", "10/05/2024", "10/06/2024"],
                "ans": 2,
                "hint": "Add 4 months to January (month 01).",
                "exp": "Month 1 (January) + 4 months = Month 5 (May). Expiry date is 10/05/2024.",
                "sol": make_sol_html([
                    "Manufacturing month = 01 (January).",
                    "Shelf life = 4 months.",
                    "Expiry month = 01 + 4 = 05 (May).",
                    "Expiry date is 10/05/2024."
                ], "Add shelf life duration in months directly to the manufacturing month.")
            },
            {
                "q": "If today's date is 25/08/2024 and a jar of jam has EXP: 15/08/2024, is it safe to consume?",
                "options": ["Yes, it is fresh", "No, it expired 10 days ago and should not be eaten", "Yes, if heated", "Cannot be determined"],
                "ans": 1,
                "hint": "Compare today's date with the expiry date printed on the label.",
                "exp": "Today's date is after the expiry date, meaning the product is expired.",
                "sol": make_sol_html([
                    "Expiry date = 15 August 2024.",
                    "Current date = 25 August 2024.",
                    "Since 25 August is 10 days past 15 August, the jam has expired.",
                    "Consuming expired food poses health risks."
                ], "Products past their expiration date must not be consumed.")
            },
            {
                "q": "A cough syrup bottle has MFG: 08/2023 and EXP: 08/2025. What is its shelf life in years?",
                "options": ["1 year", "2 years", "3 years", "4 years"],
                "ans": 1,
                "hint": "Subtract 2023 from 2025.",
                "exp": "2025 - 2023 = 2 years.",
                "sol": make_sol_html([
                    "Manufactured = August 2023.",
                    "Expires = August 2025.",
                    "Shelf life = 2025 - 2023 = 2 years (24 months)."
                ], "Shelf life can be expressed in years when month remains the same.")
            },
            {
                "q": "In the traditional Indian lunar calendar, what is the new moon day (night of no moon) called?",
                "options": ["Purnima", "Amavasya", "Ekadashi", "Sankranti"],
                "ans": 1,
                "hint": "Recall the Sanskrit word for the dark moonless night.",
                "exp": "Amavasya is the new moon day when the Moon is completely dark.",
                "sol": make_sol_html([
                    "In the lunar cycle, the day the Moon is between the Earth and Sun and invisible from Earth is Amavasya.",
                    "Purnima is the night of the full, glowing moon."
                ], "Amavasya = New Moon (dark night); Purnima = Full Moon (bright night).")
            },
            {
                "q": "What is the glowing full moon night called in traditional Indian community calendars?",
                "options": ["Amavasya", "Purnima", "Pratipada", "Chaturthi"],
                "ans": 1,
                "hint": "Recall the Sanskrit word meaning full or complete illumination.",
                "exp": "Purnima is the full moon night.",
                "sol": make_sol_html([
                    "When the Moon is fully illuminated as seen from Earth, the night is celebrated as Purnima.",
                    "Many Indian festivals like Raksha Bandhan and Guru Purnima fall on Purnima."
                ], "Purnima marks the peak of the bright waxing fortnight.")
            },
            {
                "q": "What is the fortnight of the waning (fading) moon called in the Indian lunar calendar?",
                "options": ["Shukla Paksha", "Krishna Paksha", "Chaitra", "Samvat"],
                "ans": 1,
                "hint": "This fortnight is named after darkness or darkening phase.",
                "exp": "Krishna Paksha is the dark waning fortnight from full moon to new moon.",
                "sol": make_sol_html([
                    "The lunar month is split into two halves of 15 days each.",
                    "Shukla Paksha is the waxing fortnight (growing brighter towards Purnima).",
                    "Krishna Paksha is the waning fortnight (growing darker towards Amavasya)."
                ], "Krishna Paksha = waning dark fortnight; Shukla Paksha = waxing bright fortnight.")
            },
            {
                "q": "Which Islamic calendar month is famous for the holy period of fasting from dawn to sunset?",
                "options": ["Muharram", "Ramadan", "Shawwal", "Safar"],
                "ans": 1,
                "hint": "This ninth month is followed by Eid al-Fitr.",
                "exp": "Ramadan is the ninth month of the Islamic lunar calendar.",
                "sol": make_sol_html([
                    "The Islamic Hijri calendar is a purely lunar calendar.",
                    "Ramadan is the sacred month of fasting observed by Muslims worldwide.",
                    "The sighting of the new crescent moon marks the start and end of Ramadan."
                ], "The Islamic calendar follows pure lunar cycles of 354 or 355 days per year.")
            },
            {
                "q": "How many days are in a typical lunar year (12 lunar months of ~29.5 days)?",
                "options": ["354 days", "365 days", "366 days", "370 days"],
                "ans": 0,
                "hint": "Multiply 12 by 29.5 to find the total lunar days.",
                "exp": "12 × 29.5 = 354 days, about 11 days shorter than a solar year.",
                "sol": make_sol_html([
                    "Each lunar month is about 29.5 days.",
                    "For 12 lunar months: 12 × 29.5 = 354 days.",
                    "This is approximately 11 days shorter than the 365-day solar year."
                ], "A lunar year of 354 days is about 11 days shorter than a solar year.")
            },
            {
                "q": "Why do festivals based on pure lunar calendars (like Eid) shift by about 11 days each year on the solar Gregorian calendar?",
                "options": ["Because clocks stop", "Because the lunar year (354 days) is 11 days shorter than the solar year (365 days)", "Because of leap years", "By international vote"],
                "ans": 1,
                "hint": "Find the difference between 365 days and 354 days.",
                "exp": "The 11-day difference causes lunar events to rotate forward through the solar seasons.",
                "sol": make_sol_html([
                    "Solar year = 365 days.",
                    "Lunar year = 354 days.",
                    "Difference = 365 - 354 = 11 days.",
                    "Because of this 11-day shortfall, lunar calendar dates occur 11 days earlier in each successive solar year."
                ], "The 11-day annual gap causes pure lunar festivals to cycle through all four seasons.")
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "section": "24-Hour Clocks, AM/PM & Fractional Hours",
        "speech": "",
        "quizzes": [
            {
                "q": "How is 7:30 PM written in the 24-hour digital clock format?",
                "options": ["07:30 hours", "17:30 hours", "19:30 hours", "21:30 hours"],
                "ans": 2,
                "hint": "Add 12 to PM hours: 7 + 12 = 19.",
                "exp": "7:30 PM + 12:00 = 19:30 hours.",
                "sol": make_sol_html([
                    "To convert PM times to 24-hour time, add 12 to the hour.",
                    "7 + 12 = 19.",
                    "The minutes remain unchanged: 30.",
                    "Result = 19:30 hours."
                ], "Rule: Add 12 to the hours for any time between 1:00 PM and 11:59 PM.")
            },
            {
                "q": "A railway departure board shows a train leaving at 23:45 hours. What time is this in 12-hour AM/PM format?",
                "options": ["11:45 AM", "11:45 PM", "10:45 PM", "9:45 PM"],
                "ans": 1,
                "hint": "Subtract 12 from hours greater than 12: 23 - 12 = 11.",
                "exp": "23:45 - 12:00 = 11:45 PM.",
                "sol": make_sol_html([
                    "The hour is 23, which is greater than 12.",
                    "Subtract 12: 23 - 12 = 11.",
                    "Because the original time was after 12:00 noon, it is PM.",
                    "Result = 11:45 PM."
                ], "Rule: Subtract 12 from hours greater than 12 to find PM time.")
            },
            {
                "q": "What is 12:00 midnight in 24-hour digital time notation?",
                "options": ["12:00 hours", "24:00 hours (or 00:00 hours)", "01:00 hours", "00:12 hours"],
                "ans": 1,
                "hint": "Midnight resets the hours back to zero to begin the day.",
                "exp": "Midnight marks both the end of one day (24:00) and the start of the next (00:00).",
                "sol": make_sol_html([
                    "Midnight marks the start of a new calendar day.",
                    "In 24-hour format, it is written as 00:00 hours (or 24:00 hours at the conclusion of a schedule)."
                ], "00:00 hours represents the start of a brand new day.")
            },
            {
                "q": "How many minutes are in 3/4 (three-quarters) of an hour?",
                "options": ["30 minutes", "40 minutes", "45 minutes", "50 minutes"],
                "ans": 2,
                "hint": "1/4 hour = 15 minutes; 3 × 15 = 45 minutes.",
                "exp": "3/4 × 60 minutes = 45 minutes.",
                "sol": make_sol_html([
                    "1 full hour = 60 minutes.",
                    "1/4 of an hour = 60 ÷ 4 = 15 minutes.",
                    "3/4 of an hour = 3 × 15 = 45 minutes."
                ], "Three-quarters of an hour equals 45 minutes.")
            },
            {
                "q": "What fraction of an hour is represented by 30 minutes?",
                "options": ["1/4", "1/3", "1/2", "3/4"],
                "ans": 2,
                "hint": "30 is half of 60.",
                "exp": "30 ÷ 60 = 1/2 of an hour.",
                "sol": make_sol_html([
                    "Total minutes in an hour = 60.",
                    "Fraction = 30/60.",
                    "Simplifying: 30 ÷ 30 = 1, 60 ÷ 30 = 2.",
                    "Fraction = 1/2 (half an hour)."
                ], "30 minutes is exactly half of an hour (1/2 hour).")
            },
            {
                "q": "A school sports period begins at 2:15 PM and ends at 3:00 PM. How long was the period?",
                "options": ["30 minutes", "40 minutes", "45 minutes", "1 hour"],
                "ans": 2,
                "hint": "Count from 2:15 to 3:00.",
                "exp": "From 2:15 to 3:00 is 45 minutes (three-quarters of an hour).",
                "sol": make_sol_html([
                    "Start time = 2:15 PM.",
                    "End time = 3:00 PM.",
                    "From 2:15 to 3:00 is 60 - 15 = 45 minutes."
                ], "From 15 minutes past the hour to the next hour is 45 minutes.")
            },
            {
                "q": "If a movie starts at 6:45 PM and runs for 2 hours and 15 minutes, at what time does it finish?",
                "options": ["8:45 PM", "9:00 PM", "9:15 PM", "9:30 PM"],
                "ans": 1,
                "hint": "Add 2 hours first (8:45 PM), then add 15 minutes.",
                "exp": "6:45 PM + 2 hours = 8:45 PM; 8:45 PM + 15 min = 9:00 PM.",
                "sol": make_sol_html([
                    "Start = 6:45 PM.",
                    "Add 2 hours: 6:45 + 2h = 8:45 PM.",
                    "Add remaining 15 minutes: 8:45 + 15m = 9:00 PM."
                ], "Add hours first, then advance the remaining minutes to the next hour.")
            },
            {
                "q": "On a 24-hour daily routine wheel, if a student spends 8 hours sleeping, 6 hours at school, and 2 hours studying, how many hours remain for other activities?",
                "options": ["6 hours", "8 hours", "10 hours", "12 hours"],
                "ans": 1,
                "hint": "Total day = 24 hours. Subtract 8 + 6 + 2 = 16.",
                "exp": "24 - (8 + 6 + 2) = 24 - 16 = 8 hours remaining.",
                "sol": make_sol_html([
                    "Total hours in a day = 24.",
                    "Allocated hours = 8 (sleep) + 6 (school) + 2 (study) = 16 hours.",
                    "Remaining hours = 24 - 16 = 8 hours."
                ], "All daily activities must sum to exactly 24 hours on a complete day wheel.")
            },
            {
                "q": "What does 'half past 9' mean in digital time notation?",
                "options": ["9:15", "9:30", "9:45", "10:30"],
                "ans": 1,
                "hint": "Half of 60 minutes is 30 minutes.",
                "exp": "'Half past 9' means 30 minutes after 9:00, which is 9:30.",
                "sol": make_sol_html([
                    "'Half past' signifies that half an hour (30 minutes) has elapsed after the hour.",
                    "Half past 9 = 9:30."
                ], "'Half past' always indicates 30 minutes past the designated hour.")
            },
            {
                "q": "How many degrees does the minute hand turn in 15 minutes (a quarter hour)?",
                "options": ["45°", "60°", "90°", "180°"],
                "ans": 2,
                "hint": "A full circle is 360°. One quarter is 360° ÷ 4.",
                "exp": "360° ÷ 4 = 90° (a right angle).",
                "sol": make_sol_html([
                    "A full clock face circle = 360 degrees.",
                    "15 minutes is 1/4 of a full circle (60 minutes).",
                    "360° ÷ 4 = 90 degrees.",
                    "The hands form a perfect right angle at quarter hours."
                ], "A quarter-turn of the minute hand traverses exactly 90 degrees.")
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "section": "Clock Errors, Midnight Trains & Base-60 Math",
        "speech": "",
        "quizzes": [
            {
                "q": "A clock shows the short hour hand pointing just past 3 and the long minute hand pointing to 6. What time is it?",
                "options": ["6:03", "3:06", "3:30", "6:15"],
                "ans": 2,
                "hint": "The short hand shows the hour (3), and the long hand at 6 shows minutes: 6 × 5 = 30.",
                "exp": "Hour is 3, minute is 6 × 5 = 30. Time is 3:30.",
                "sol": make_sol_html([
                    "The short hand is the hour hand; it is between 3 and 4, indicating hour 3.",
                    "The long hand is the minute hand; it points to 6.",
                    "Each number on the dial represents 5 minutes: 6 × 5 = 30 minutes.",
                    "The correct time is 3:30."
                ], "Never confuse the hour hand with the minute hand; multiply minute hand number by 5.")
            },
            {
                "q": "Why is it an error to say a clock reads '4:08' when the minute hand points to 8?",
                "options": ["Because 8 means 40 minutes (8 × 5 = 40)", "Because 8 means 80 minutes", "Because 4:08 is impossible", "Because clocks don't have 8"],
                "ans": 0,
                "hint": "Remember each clock number represents 5 minutes for the minute hand.",
                "exp": "Numbers on a clock represent 5-minute increments: 8 × 5 = 40 minutes.",
                "sol": make_sol_html([
                    "The numbers 1 to 12 on a clock dial represent 5-minute chunks for the minute hand.",
                    "When the minute hand points to 8, elapsed minutes = 8 × 5 = 40 minutes.",
                    "The time is 4:40, not 4:08."
                ], "Minute hand at N represents N × 5 minutes.")
            },
            {
                "q": "A passenger train departs city A at 21:30 and arrives at city B at 05:15 the following morning. What is the total travel duration?",
                "options": ["7 hours 15 minutes", "7 hours 45 minutes", "8 hours 15 minutes", "8 hours 45 minutes"],
                "ans": 1,
                "hint": "Calculate time before midnight (21:30 to 24:00) + time after midnight (00:00 to 05:15).",
                "exp": "Before midnight = 2h 30m; After midnight = 5h 15m. Total = 7 hours 45 minutes.",
                "sol": make_sol_html([
                    "Before midnight: from 21:30 to 24:00 is 2 hours and 30 minutes.",
                    "After midnight: from 00:00 to 05:15 is 5 hours and 15 minutes.",
                    "Add both parts: 2h 30m + 5h 15m = 7 hours and 45 minutes."
                ], "For overnight journeys, split the calculation at midnight (24:00).")
            },
            {
                "q": "If the 1st of May is a Friday, what day of the week will the 22nd of May be?",
                "options": ["Thursday", "Friday", "Saturday", "Sunday"],
                "ans": 1,
                "hint": "22 - 1 = 21 days. 21 is a multiple of 7 (3 weeks).",
                "exp": "21 ÷ 7 = 3 full weeks with 0 remainder. The day remains Friday.",
                "sol": make_sol_html([
                    "Start date = 1 May (Friday).",
                    "Target date = 22 May.",
                    "Days elapsed = 22 - 1 = 21 days.",
                    "21 ÷ 7 = exactly 3 weeks with 0 days remainder.",
                    "Since the remainder is 0, the day of the week is still Friday."
                ], "Adding any exact multiple of 7 days lands on the identical day of the week.")
            },
            {
                "q": "Why was the century year 1900 NOT a leap year, even though 1900 is divisible by 4?",
                "options": ["Because century years must be divisible by 400 to be leap years, and 1900 is not", "Because February had 30 days", "Because 1900 was an odd number", "It was a leap year"],
                "ans": 0,
                "hint": "Recall the special rule for century years ending in two zeros.",
                "exp": "Century years ending in 00 must be divisible by 400. 1900 ÷ 400 = 4 remainder 300.",
                "sol": make_sol_html([
                    "The Gregorian calendar rule states: century years ending in '00' are leap years only if divisible by 400.",
                    "1900 ÷ 400 = 4 with a remainder of 300.",
                    "Because 1900 is not divisible by 400, it was an ordinary year with 28 days in February."
                ], "Century years must be divisible by 400 to qualify as leap years.")
            },
            {
                "q": "Add the time durations: 3 hours 40 minutes + 2 hours 50 minutes.",
                "options": ["5 hours 90 minutes", "6 hours 10 minutes", "6 hours 30 minutes", "6 hours 40 minutes"],
                "ans": 2,
                "hint": "40m + 50m = 90m = 1h 30m. 3h + 2h + 1h = 6h 30m.",
                "exp": "3h 40m + 2h 50m = 5h 90m = 6 hours 30 minutes.",
                "sol": make_sol_html([
                    "Add the minutes: 40 + 50 = 90 minutes.",
                    "Since 90 ≥ 60, convert 60 minutes into 1 hour: 90 - 60 = 30 minutes remaining, with 1 hour carried.",
                    "Add the hours: 3 + 2 + 1 (carried) = 6 hours.",
                    "Total = 6 hours and 30 minutes."
                ], "Regroup 60 minutes as 1 hour whenever the minute sum reaches or exceeds 60.")
            },
            {
                "q": "Subtract: 5 hours 15 minutes - 2 hours 45 minutes.",
                "options": ["2 hours 15 minutes", "2 hours 30 minutes", "2 hours 45 minutes", "3 hours 30 minutes"],
                "ans": 1,
                "hint": "Borrow 1 hour (60 min) from 5 hours: 4 hours 75 minutes - 2 hours 45 minutes.",
                "exp": "4h 75m - 2h 45m = 2 hours 30 minutes.",
                "sol": make_sol_html([
                    "We cannot subtract 45 minutes from 15 minutes.",
                    "Borrow 1 hour from 5 hours: 5 hours becomes 4 hours.",
                    "Convert the borrowed hour into 60 minutes and add to 15: 15 + 60 = 75 minutes.",
                    "Now subtract: 75m - 45m = 30 minutes; 4h - 2h = 2 hours.",
                    "Result = 2 hours and 30 minutes."
                ], "When borrowing in time subtraction, 1 borrowed hour equals 60 minutes.")
            },
            {
                "q": "How many days are there altogether in the months of July and August combined?",
                "options": ["60 days", "61 days", "62 days", "63 days"],
                "ans": 2,
                "hint": "Both July and August have 31 days.",
                "exp": "July (31 days) + August (31 days) = 62 days.",
                "sol": make_sol_html([
                    "July has 31 days.",
                    "August is the consecutive month and also has 31 days.",
                    "31 + 31 = 62 days."
                ], "July and August are consecutive months that both have 31 days.")
            },
            {
                "q": "A bakery bakes bread at 06:30 hours. The bread remains fresh for 48 hours. By what time and date should it be consumed if baked on 10 October?",
                "options": ["06:30 hours on 11 October", "06:30 hours on 12 October", "12:00 hours on 12 October", "06:30 hours on 13 October"],
                "ans": 1,
                "hint": "48 hours = 2 full days (24 × 2 = 48).",
                "exp": "10 October + 2 days = 12 October at 06:30 hours.",
                "sol": make_sol_html([
                    "48 hours ÷ 24 hours/day = 2 full days.",
                    "Start = 06:30 hours on 10 October.",
                    "Add 2 days = 06:30 hours on 12 October."
                ], "48 hours corresponds to exactly two full 24-hour days.")
            },
            {
                "q": "Why is time measured using base 60 (60 seconds = 1 minute, 60 minutes = 1 hour) instead of base 10?",
                "options": ["It is an ancient astronomical tradition from Babylonians because 60 is divisible by 2, 3, 4, 5, 6, 10, 12, 15, 20, 30", "Because clocks have 60 gears", "Because humans have 60 fingers", "By random accident"],
                "ans": 0,
                "hint": "Think about how easily 60 divides into halves, thirds, and quarters.",
                "exp": "60 is a highly composite number that divides evenly into many fractions (halves, thirds, quarters, fifths, sixths).",
                "sol": make_sol_html([
                    "Ancient Babylonian astronomers chose 60 because it has 12 factors: 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, and 60.",
                    "This makes it remarkably easy to calculate halves (30 min), thirds (20 min), quarters (15 min), fifths (12 min), and sixths (10 min) without fractions or decimals."
                ], "Base 60 allows convenient fractional divisions of time without messy decimals.")
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(slides_part3)} challenge slides.")
    total_q = sum(len(s['quizzes']) for s in slides_part3)
    print(f"Total quiz questions: {total_q}")
    assert len(slides_part3) == 4, "Must have exactly 4 slides"
    assert total_q == 40, "Must have exactly 40 quiz questions"
    for s in slides_part3:
        assert len(s["title"].split()) <= 3, f"Title {s['title']} has too many words"
        assert len(s["quizzes"]) == 10, f"Slide {s['id']} must have 10 questions"
        for q in s["quizzes"]:
            assert 0 <= q["ans"] < len(q["options"]), f"Invalid answer index in {q['q']}"
    print("All Part 3 challenge assertions passed successfully!")
