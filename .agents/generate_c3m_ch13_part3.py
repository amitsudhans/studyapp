#!/usr/bin/env python3
"""
NCERT Class 3 Mathematics - Chapter 13: Time Goes On
Part 3: Slides 17 to 20 (4 Challenge Slides × 10 Multi-Choice Questions = 40 Questions)
Strict titles: 1 to 3 words.
Each question has:
- question, 4 options, answer (0-3), hint, explanation
- solution_steps: strictly 3 steps
Zero human character names, zero lecturer personas.
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Challenge 1",
        "subtitle": "Mastery Challenge: Calendar Grids & Year Patterns",
        "questions": [
            {
                "question": "If July 1 falls on a Wednesday, what day of the week is July 15?",
                "options": ["Tuesday", "Wednesday", "Thursday", "Friday"],
                "answer": 1,
                "hint": "15 minus 1 is 14 days, which is exactly 2 full weeks.",
                "explanation": "Adding 14 days (2 complete weeks of 7 days) to a Wednesday lands on another Wednesday.",
                "solution_steps": [
                    "Step 1: Calculate the difference in days: 15 - 1 = 14 days.",
                    "Step 2: Divide 14 by 7 days per week: 14 ÷ 7 = 2 full weeks with 0 remainder.",
                    "Step 3: Since there is no remainder, the day of the week remains identical: Wednesday."
                ]
            },
            {
                "question": "How many days are in the month of August?",
                "options": ["28 days", "30 days", "31 days", "29 days"],
                "answer": 2,
                "hint": "August immediately follows July and has the same length.",
                "explanation": "Both July and August have 31 days each in the calendar year.",
                "solution_steps": [
                    "Step 1: Recall the standard calendar month lengths.",
                    "Step 2: July and August are consecutive months that both have 31 days.",
                    "Step 3: Confirm August has exactly 31 days."
                ]
            },
            {
                "question": "Which of the following months has exactly 30 days?",
                "options": ["January", "March", "April", "May"],
                "answer": 2,
                "hint": "Remember the rhyme: Thirty days hath September, April, June, and November.",
                "explanation": "April has exactly 30 days.",
                "solution_steps": [
                    "Step 1: Identify months with 30 days: April, June, September, November.",
                    "Step 2: Check the options against this list; April is listed.",
                    "Step 3: Confirm January, March, and May all have 31 days, leaving April as the correct 30-day month."
                ]
            },
            {
                "question": "A standard non-leap year has how many total weeks and extra days?",
                "options": ["50 weeks and 2 days", "52 weeks and 1 day", "52 weeks and 2 days", "54 weeks and 1 day"],
                "answer": 1,
                "hint": "Divide 365 by 7.",
                "explanation": "365 ÷ 7 = 52 with a remainder of 1 day.",
                "solution_steps": [
                    "Step 1: Set up the division of total annual days by days per week: 365 ÷ 7.",
                    "Step 2: 52 × 7 = 364 days, leaving a remainder of 1 day (365 - 364 = 1).",
                    "Step 3: Thus, a standard year comprises 52 complete weeks plus 1 extra day."
                ]
            },
            {
                "question": "If a date is on Sunday, July 7, what is the date of the very next Sunday?",
                "options": ["July 13", "July 14", "July 15", "July 16"],
                "answer": 1,
                "hint": "Add 7 days to the current date.",
                "explanation": "7 + 7 = 14. The next Sunday is July 14.",
                "solution_steps": [
                    "Step 1: Recognize that the same weekday recurs every 7 days.",
                    "Step 2: Add 7 to the current date: 7 + 7 = 14.",
                    "Step 3: Verify July 14 falls on the following Sunday."
                ]
            },
            {
                "question": "How many months in a single calendar year have 31 days?",
                "options": ["5 months", "6 months", "7 months", "8 months"],
                "answer": 2,
                "hint": "List them: Jan, Mar, May, Jul, Aug, Oct, Dec.",
                "explanation": "There are 7 months with 31 days: January, March, May, July, August, October, December.",
                "solution_steps": [
                    "Step 1: Identify all months containing 31 days: January, March, May, July, August, October, December.",
                    "Step 2: Count the listed months: 1, 2, 3, 4, 5, 6, 7.",
                    "Step 3: Conclude that exactly 7 months have 31 days."
                ]
            },
            {
                "question": "In a leap year, how many days does February contain?",
                "options": ["28 days", "29 days", "30 days", "31 days"],
                "answer": 1,
                "hint": "One extra day is added to February every 4 years.",
                "explanation": "February has 29 days in a leap year and 28 days in a standard year.",
                "solution_steps": [
                    "Step 1: Note that a leap year contains 366 days instead of 365.",
                    "Step 2: The extra day is added to February, increasing its count from 28 to 29.",
                    "Step 3: Confirm February has 29 days in a leap year."
                ]
            },
            {
                "question": "If school holidays begin on June 1 and last for 4 weeks, on what date do they end?",
                "options": ["June 25", "June 28", "June 29", "July 1"],
                "answer": 1,
                "hint": "4 weeks equals 4 × 7 = 28 days.",
                "explanation": "4 weeks = 28 days. Starting June 1, 28 days cover through June 28.",
                "solution_steps": [
                    "Step 1: Convert 4 weeks into days: 4 × 7 = 28 days.",
                    "Step 2: Count 28 days starting from June 1.",
                    "Step 3: 1 + 28 - 1 = 28. The 28-day period ends on June 28."
                ]
            },
            {
                "question": "What is the day of the week if tomorrow is Friday?",
                "options": ["Wednesday", "Thursday", "Saturday", "Sunday"],
                "answer": 1,
                "hint": "Which day comes immediately before Friday?",
                "explanation": "Thursday comes immediately before Friday, so today is Thursday.",
                "solution_steps": [
                    "Step 1: Note the condition that tomorrow is Friday.",
                    "Step 2: Step back one day from Friday in the weekly cycle.",
                    "Step 3: The day immediately preceding Friday is Thursday."
                ]
            },
            {
                "question": "Which national holiday is celebrated on October 2 each year?",
                "options": ["Independence Day", "Republic Day", "Gandhi Jayanti", "Teacher's Day"],
                "answer": 2,
                "hint": "This day honors the birth of Mahatma Gandhi.",
                "explanation": "Gandhi Jayanti is celebrated nationwide on October 2.",
                "solution_steps": [
                    "Step 1: Match October 2 with annual Indian national holidays.",
                    "Step 2: Independence Day is August 15, Republic Day is January 26, Gandhi Jayanti is October 2.",
                    "Step 3: Confirm Gandhi Jayanti is October 2."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "subtitle": "Mastery Challenge: Ages, Timelines & Certificates",
        "questions": [
            {
                "question": "A student is 9 years old today. In what year was the student born if the current year is 2024?",
                "options": ["2013", "2014", "2015", "2016"],
                "answer": 2,
                "hint": "Subtract 9 from 2024.",
                "explanation": "2024 - 9 = 2015. The student was born in 2015.",
                "solution_steps": [
                    "Step 1: Identify current year (2024) and current age (9).",
                    "Step 2: Subtract age from current year: 2024 - 9 = 2015.",
                    "Step 3: Verify: 2015 + 9 = 2024. Birth year is 2015."
                ]
            },
            {
                "question": "A birth certificate lists the birth date as 14/11/2018. In which month was the child born?",
                "options": ["September", "October", "November", "December"],
                "answer": 2,
                "hint": "The 11th month of the year.",
                "explanation": "The 11th month in the calendar is November.",
                "solution_steps": [
                    "Step 1: Identify the date format: DD/MM/YYYY.",
                    "Step 2: The month field is 11.",
                    "Step 3: The 11th month of the year is November."
                ]
            },
            {
                "question": "If a child was born on 14/11/2018, how old will the child be on 14/11/2030?",
                "options": ["10 years", "11 years", "12 years", "14 years"],
                "answer": 2,
                "hint": "Subtract 2018 from 2030.",
                "explanation": "2030 - 2018 = 12 years.",
                "solution_steps": [
                    "Step 1: Compare target year (2030) with birth year (2018).",
                    "Step 2: Perform the subtraction: 2030 - 2018 = 12.",
                    "Step 3: The child will be exactly 12 years old."
                ]
            },
            {
                "question": "Two siblings have an age gap of 4 years. When the older sibling is 18, what is the age gap?",
                "options": ["2 years", "4 years", "6 years", "8 years"],
                "answer": 1,
                "hint": "Both siblings age by 1 year every year.",
                "explanation": "The age gap between two people never changes; it remains 4 years.",
                "solution_steps": [
                    "Step 1: Recall that both individuals age at the identical rate of 1 year per year.",
                    "Step 2: The difference in their ages remains constant over time.",
                    "Step 3: The age gap remains exactly 4 years."
                ]
            },
            {
                "question": "A child was 6 years old when entering Grade 1 in 2021. In what year will the child turn 15?",
                "options": ["2028", "2029", "2030", "2031"],
                "answer": 2,
                "hint": "Age 6 in 2021 means birth year was 2015. Add 15 to 2015.",
                "explanation": "2021 - 6 = 2015 birth year. 2015 + 15 = 2030.",
                "solution_steps": [
                    "Step 1: Find birth year: 2021 - 6 = 2015.",
                    "Step 2: Add 15 years to birth year: 2015 + 15 = 2030.",
                    "Step 3: Verify: in 2030, age is 2030 - 2015 = 15."
                ]
            },
            {
                "question": "A grandmother is 64 years old, and her daughter is 36. How old was the grandmother when her daughter was born?",
                "options": ["26 years", "28 years", "30 years", "32 years"],
                "answer": 1,
                "hint": "Subtract 36 from 64.",
                "explanation": "64 - 36 = 28 years old.",
                "solution_steps": [
                    "Step 1: Formulate equation: grandmother's age minus daughter's age: 64 - 36.",
                    "Step 2: Calculate: 64 - 36 = 28.",
                    "Step 3: The grandmother was 28 years old when her daughter was born."
                ]
            },
            {
                "question": "On a timeline, Event A is in 2012, Event B is in 2018, and Event C is in 2015. What is the chronological order?",
                "options": ["A, B, C", "A, C, B", "C, A, B", "B, C, A"],
                "answer": 1,
                "hint": "Order from smallest year to largest year.",
                "explanation": "2012 (A) comes before 2015 (C), which comes before 2018 (B). Order: A, C, B.",
                "solution_steps": [
                    "Step 1: List the years: 2012, 2018, 2015.",
                    "Step 2: Sort the years in ascending numerical order: 2012 < 2015 < 2018.",
                    "Step 3: Map back to the events: A, C, B."
                ]
            },
            {
                "question": "A certificate was issued on 20/08/2020. How many years passed until 20/08/2024?",
                "options": ["2 years", "3 years", "4 years", "5 years"],
                "answer": 2,
                "hint": "Subtract 2020 from 2024.",
                "explanation": "2024 - 2020 = 4 years.",
                "solution_steps": [
                    "Step 1: Check that day and month match: 20 August in both dates.",
                    "Step 2: Subtract the years: 2024 - 2020 = 4.",
                    "Step 3: Exactly 4 years have passed."
                ]
            },
            {
                "question": "If a child celebrated their 7th birthday in 2023, which birthday will they celebrate in 2027?",
                "options": ["9th birthday", "10th birthday", "11th birthday", "12th birthday"],
                "answer": 2,
                "hint": "2027 is 4 years after 2023. Add 4 to 7.",
                "explanation": "2027 - 2023 = 4 years. 7 + 4 = 11th birthday.",
                "solution_steps": [
                    "Step 1: Calculate years elapsed: 2027 - 2023 = 4 years.",
                    "Step 2: Add 4 years to the age in 2023: 7 + 4 = 11.",
                    "Step 3: The child will celebrate their 11th birthday in 2027."
                ]
            },
            {
                "question": "What information is NOT typically found on a standard birth certificate?",
                "options": ["Date of birth", "Place of birth", "Exam test scores", "Parents' names"],
                "answer": 2,
                "hint": "A birth certificate is issued at birth, before school starts.",
                "explanation": "Exam scores are academic records, not recorded on birth certificates.",
                "solution_steps": [
                    "Step 1: Review components of official birth certificates: name, date, place, parents.",
                    "Step 2: Academic test scores belong to school report cards, not civil birth records.",
                    "Step 3: Confirm exam test scores are not on birth certificates."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "subtitle": "Mastery Challenge: Clock Dial Reading & Hands",
        "questions": [
            {
                "question": "When the hour hand points at 4 and the minute hand points at 12, what time is it?",
                "options": ["12:04", "4:00", "4:12", "4:30"],
                "answer": 1,
                "hint": "Minute hand at 12 indicates an exact o'clock.",
                "explanation": "Hour hand at 4 and minute hand at 12 means exactly 4:00.",
                "solution_steps": [
                    "Step 1: Observe minute hand pointing at 12, indicating 0 minutes past the hour.",
                    "Step 2: Observe hour hand pointing directly at 4.",
                    "Step 3: Read the time as 4:00."
                ]
            },
            {
                "question": "Where does the minute hand point when the time is half past 7?",
                "options": ["At 3", "At 6", "At 9", "At 12"],
                "answer": 1,
                "hint": "Half past means 30 minutes, which is at the bottom of the dial.",
                "explanation": "The minute hand points at 6 for half past (30 minutes).",
                "solution_steps": [
                    "Step 1: 'Half past' means 30 minutes past the hour.",
                    "Step 2: Divide 30 minutes by 5 minutes per number: 30 ÷ 5 = 6.",
                    "Step 3: The minute hand points directly at 6."
                ]
            },
            {
                "question": "What time is shown when the hour hand is between 2 and 3, and the minute hand is at 9?",
                "options": ["2:15", "2:45", "3:45", "9:15"],
                "answer": 1,
                "hint": "Minute hand at 9 means 9 × 5 = 45 minutes past 2.",
                "explanation": "The time is 2:45, also called quarter to three.",
                "solution_steps": [
                    "Step 1: Identify hour: between 2 and 3 means hour is 2.",
                    "Step 2: Calculate minutes: 9 × 5 = 45 minutes.",
                    "Step 3: The time is 2:45 (quarter to 3)."
                ]
            },
            {
                "question": "How many minutes does the minute hand take to complete one full revolution around the dial?",
                "options": ["12 minutes", "30 minutes", "60 minutes", "100 minutes"],
                "answer": 2,
                "hint": "There are 60 tick marks around the entire clock face.",
                "explanation": "One complete revolution of the minute hand equals 60 minutes (1 hour).",
                "solution_steps": [
                    "Step 1: Count the 60 minute marks around the clock dial.",
                    "Step 2: The minute hand touches all 60 marks in one complete rotation.",
                    "Step 3: Thus, one full revolution equals 60 minutes."
                ]
            },
            {
                "question": "How many hours does the hour hand take to make one complete revolution of the dial?",
                "options": ["1 hour", "12 hours", "24 hours", "60 hours"],
                "answer": 1,
                "hint": "The numbers on the dial go from 1 to 12.",
                "explanation": "The hour hand completes a full circle in 12 hours.",
                "solution_steps": [
                    "Step 1: The analog clock face has 12 hour positions.",
                    "Step 2: The hour hand moves from 1 through 12, taking 1 hour per position.",
                    "Step 3: 12 × 1 = 12 hours for one full revolution."
                ]
            },
            {
                "question": "If the minute hand moves from 2 to 5, how many minutes have elapsed?",
                "options": ["3 minutes", "10 minutes", "15 minutes", "20 minutes"],
                "answer": 2,
                "hint": "The hand moves through 3 intervals of 5 minutes.",
                "explanation": "(5 - 2) × 5 = 3 × 5 = 15 minutes.",
                "solution_steps": [
                    "Step 1: Count number of intervals moved: 5 - 2 = 3 intervals.",
                    "Step 2: Each interval represents 5 minutes: 3 × 5 = 15 minutes.",
                    "Step 3: Exactly 15 minutes have elapsed."
                ]
            },
            {
                "question": "Which of the following is equivalent to 'quarter past nine'?",
                "options": ["9:15", "9:30", "9:45", "8:45"],
                "answer": 0,
                "hint": "A quarter of an hour is 15 minutes.",
                "explanation": "Quarter past nine means 15 minutes after 9, written as 9:15.",
                "solution_steps": [
                    "Step 1: A quarter of an hour = 60 ÷ 4 = 15 minutes.",
                    "Step 2: 'Quarter past nine' means 15 minutes after hour 9.",
                    "Step 3: Write numerically as 9:15."
                ]
            },
            {
                "question": "When the clock shows 11:30, where is the hour hand positioned?",
                "options": ["Directly on 11", "Exactly halfway between 11 and 12", "Directly on 12", "Directly on 6"],
                "answer": 1,
                "hint": "At half past, the hour hand has traveled halfway to the next hour.",
                "explanation": "At 11:30, the hour hand is halfway between 11 and 12.",
                "solution_steps": [
                    "Step 1: Observe that 30 minutes is half of the 60-minute hour.",
                    "Step 2: In half an hour, the hour hand travels half the distance between 11 and 12.",
                    "Step 3: The hour hand sits exactly halfway between 11 and 12."
                ]
            },
            {
                "question": "How many total minutes are in 2 and a half hours?",
                "options": ["120 minutes", "130 minutes", "150 minutes", "180 minutes"],
                "answer": 2,
                "hint": "2 hours = 120 minutes, plus half an hour (30 minutes).",
                "explanation": "2 × 60 = 120 minutes, plus 30 minutes = 150 minutes.",
                "solution_steps": [
                    "Step 1: Convert 2 whole hours to minutes: 2 × 60 = 120 minutes.",
                    "Step 2: Convert half an hour to minutes: 60 ÷ 2 = 30 minutes.",
                    "Step 3: Add together: 120 + 30 = 150 minutes."
                ]
            },
            {
                "question": "At what time do the hour hand and minute hand point in opposite directions to form a straight line?",
                "options": ["3:00", "6:00", "9:00", "12:00"],
                "answer": 1,
                "hint": "One hand points straight up at 12 and the other straight down at 6.",
                "explanation": "At 6:00, the hour hand points at 6 and the minute hand points at 12, forming a straight line.",
                "solution_steps": [
                    "Step 1: A straight line means hands are 180 degrees apart.",
                    "Step 2: At 6:00, minute hand is at 12 (top) and hour hand is at 6 (bottom).",
                    "Step 3: This forms a continuous vertical line through the clock center."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "subtitle": "Mastery Challenge: Elapsed Time, Digital & Sand Clocks",
        "questions": [
            {
                "question": "A movie starts at 2:15 PM and ends at 4:45 PM. What is the total running time?",
                "options": ["2 hours", "2 hours 15 minutes", "2 hours 30 minutes", "2 hours 45 minutes"],
                "answer": 2,
                "hint": "Subtract hours and minutes: (4 - 2) hours and (45 - 15) minutes.",
                "explanation": "4:45 - 2:15 = 2 hours and 30 minutes.",
                "solution_steps": [
                    "Step 1: Subtract the minutes: 45 - 15 = 30 minutes.",
                    "Step 2: Subtract the hours: 4 - 2 = 2 hours.",
                    "Step 3: Combine: 2 hours and 30 minutes."
                ]
            },
            {
                "question": "What is 15:45 in standard 12-hour clock format?",
                "options": ["3:45 AM", "3:45 PM", "5:45 PM", "1:45 PM"],
                "answer": 1,
                "hint": "Subtract 12 from 15 to find PM time.",
                "explanation": "15 - 12 = 3, so 15:45 is 3:45 PM.",
                "solution_steps": [
                    "Step 1: Recognize that 15 is greater than 12, indicating post-midday (PM).",
                    "Step 2: Subtract 12: 15 - 12 = 3.",
                    "Step 3: Write in 12-hour format: 3:45 PM."
                ]
            },
            {
                "question": "How is 8:20 PM written in 24-hour railway time?",
                "options": ["08:20", "18:20", "20:20", "22:20"],
                "answer": 2,
                "hint": "Add 12 to the PM hour: 8 + 12 = 20.",
                "explanation": "8 + 12 = 20, so 8:20 PM is written as 20:20.",
                "solution_steps": [
                    "Step 1: Note that the time is in the evening (PM).",
                    "Step 2: Add 12 to the hour: 8 + 12 = 20.",
                    "Step 3: Retain minutes: 20:20."
                ]
            },
            {
                "question": "If a train departs at 09:30 and the journey takes 3 hours 45 minutes, at what time does it arrive?",
                "options": ["12:15", "12:45", "13:15", "13:30"],
                "answer": 2,
                "hint": "9:30 + 3 hours = 12:30. Then add 45 minutes.",
                "explanation": "9:30 + 3 hours = 12:30. 12:30 + 45 minutes = 13:15 (1:15 PM).",
                "solution_steps": [
                    "Step 1: Add 3 hours to 9:30: 9:30 + 3 hours = 12:30.",
                    "Step 2: Add 45 minutes: 12:30 + 30 min = 13:00; plus remaining 15 min = 13:15.",
                    "Step 3: Verify arrival time is 13:15 (or 1:15 PM)."
                ]
            },
            {
                "question": "A student started practicing math at 5:25 PM and finished at 6:10 PM. How long did the student practice?",
                "options": ["35 minutes", "40 minutes", "45 minutes", "50 minutes"],
                "answer": 2,
                "hint": "From 5:25 to 6:00 is 35 minutes, plus 10 minutes to 6:10.",
                "explanation": "35 + 10 = 45 minutes.",
                "solution_steps": [
                    "Step 1: Calculate minutes to the top of the hour (6:00): 60 - 25 = 35 minutes.",
                    "Step 2: Add the minutes past 6:00: 35 + 10 = 45 minutes.",
                    "Step 3: The total elapsed duration is 45 minutes."
                ]
            },
            {
                "question": "Which of the following devices measures elapsed duration without using gears, batteries, or electricity?",
                "options": ["Digital stopwatch", "Sand hourglass", "Quartz wall clock", "Smartwatch"],
                "answer": 1,
                "hint": "It relies solely on flowing sand pulled by gravity.",
                "explanation": "A sand hourglass measures time through gravity-driven sand flow without gears or electricity.",
                "solution_steps": [
                    "Step 1: Identify power sources: stopwatches and quartz clocks use batteries/electronics.",
                    "Step 2: A sand hourglass relies purely on the physical flow of sand under gravity.",
                    "Step 3: Confirm the sand hourglass is the non-electrical, non-mechanical timer."
                ]
            },
            {
                "question": "A sand timer takes 4 minutes for all sand to flow through. To time a 12-minute game, how many times must it be flipped?",
                "options": ["2 times", "3 times", "4 times", "5 times"],
                "answer": 1,
                "hint": "Divide 12 by 4.",
                "explanation": "12 ÷ 4 = 3 flips.",
                "solution_steps": [
                    "Step 1: Target duration = 12 minutes.",
                    "Step 2: Timer duration per flip = 4 minutes.",
                    "Step 3: 12 ÷ 4 = 3 full runs (flips)."
                ]
            },
            {
                "question": "Midnight is represented in 24-hour digital format as:",
                "options": ["12:00 AM", "24:00", "00:00", "01:00"],
                "answer": 2,
                "hint": "The day begins at zero hours and zero minutes.",
                "explanation": "In 24-hour digital time, midnight is written as 00:00.",
                "solution_steps": [
                    "Step 1: Recall that the 24-hour cycle begins at midnight.",
                    "Step 2: Starting time has zero elapsed hours and zero elapsed minutes.",
                    "Step 3: Write as 00:00."
                ]
            },
            {
                "question": "How many seconds are in 5 minutes?",
                "options": ["250 seconds", "300 seconds", "350 seconds", "500 seconds"],
                "answer": 1,
                "hint": "1 minute = 60 seconds. Multiply 5 × 60.",
                "explanation": "5 × 60 = 300 seconds.",
                "solution_steps": [
                    "Step 1: Conversion factor: 1 minute = 60 seconds.",
                    "Step 2: Multiply by 5 minutes: 5 × 60 = 300.",
                    "Step 3: There are 300 seconds in 5 minutes."
                ]
            },
            {
                "question": "Which activity takes approximately 1 hour to complete?",
                "options": ["Blinking an eye", "Brushing teeth", "Cooking a complete family meal", "Growing a mango tree"],
                "answer": 2,
                "hint": "Blinking is seconds, brushing is minutes, growing a tree is years.",
                "explanation": "Cooking a full family meal typically takes about 1 hour (45 to 60 minutes).",
                "solution_steps": [
                    "Step 1: Evaluate durations: blinking takes seconds; brushing takes 2-3 minutes; growing a tree takes years.",
                    "Step 2: Preparing and cooking a complete dinner meal takes about 45 to 60 minutes.",
                    "Step 3: Confirm cooking a family meal is naturally measured in hours (approximately 1 hour)."
                ]
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(slides_part3)} slides for Part 3.")
    for s in slides_part3:
        title_words = len(s["title"].strip().split())
        print(f"Slide {s['id']}: '{s['title']}' ({title_words} words) -> {len(s['questions'])} questions")
        assert 1 <= title_words <= 3, f"Title violation on slide {s['id']}"
        assert len(s["questions"]) == 10, f"Question count mismatch on slide {s['id']}"
        for qidx, q in enumerate(s["questions"]):
            assert len(q["options"]) == 4, f"Slide {s['id']} Q{qidx+1} options count != 4"
            assert q["answer"] in [0, 1, 2, 3], f"Slide {s['id']} Q{qidx+1} answer invalid"
            assert len(q["solution_steps"]) == 3, f"Slide {s['id']} Q{qidx+1} solution steps != 3"
    print("Part 3 passed all strict validation checks!")
