# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 12: Racing Seconds
Part 3 Data: Slides 17 to 20 (40 Mastery Quiz Questions)
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Challenge 1",
        "tagline": "Mastery Challenge 1 • Elapsed Time & 24-Hour Clock Systems",
        "lecture": "Welcome to Mastery Challenge 1. In this interactive session, you will test your understanding of start and finish times, interval elapsed durations, and converting between 12-hour and 24-hour clocks.",
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-blue-900/40 to-indigo-900/40 border border-blue-500/30 rounded-xl p-4">
        <h4 class="text-blue-300 font-bold text-sm tracking-wider uppercase mb-1">Challenge Overview</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Test your skills on finding elapsed time between clock intervals, comparing task durations, and converting between a.m./p.m. and 24-hour railway formats. Solve all 10 questions to unlock the next level!
        </p>
    </div>
</div>
""",
        "questions": [
            {
                "id": 1,
                "question": "A student started morning yoga at 06:15 a.m. and finished at 07:05 a.m. How long was the yoga practice?",
                "options": [
                    "50 minutes",
                    "40 minutes",
                    "1 hour 10 minutes",
                    "45 minutes"
                ],
                "answer": 0,
                "hint": "Count from 06:15 to 07:00 (45 min), then add 5 min to reach 07:05.",
                "explanation": "From 06:15 to 07:00 is 45 minutes, plus 5 minutes to 07:05 = 50 minutes.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Start Time = 06:15 a.m., Finish Time = 07:05 a.m.</p>
    <p>2. Milestone jump: 06:15 a.m. ➔ 07:00 a.m. = 45 minutes.</p>
    <p>3. Remaining jump: 07:00 a.m. ➔ 07:05 a.m. = 5 minutes.</p>
    <p>4. Total Elapsed Time = 45 + 5 = <strong>50 minutes</strong>.</p>
</div>
"""
            },
            {
                "id": 2,
                "question": "How much time elapses between 01:15 p.m. and 01:42 p.m.?",
                "options": [
                    "27 minutes",
                    "37 minutes",
                    "17 minutes",
                    "32 minutes"
                ],
                "answer": 0,
                "hint": "Both times share the 1 o'clock hour: subtract 15 from 42.",
                "explanation": "42 - 15 = 27 minutes.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Both times are in the same hour (1 p.m.).</p>
    <p>2. Elapsed Time = 42 − 15.</p>
    <p>3. 42 − 15 = <strong>27 minutes</strong>.</p>
</div>
"""
            },
            {
                "id": 3,
                "question": "How many hours pass from 03:18 p.m. to 08:18 p.m.?",
                "options": [
                    "5 hours",
                    "4 hours",
                    "6 hours",
                    "5 hours 18 minutes"
                ],
                "answer": 0,
                "hint": "The minutes match (:18). Subtract 3 from 8.",
                "explanation": "Since the minutes are identical, 8 - 3 = 5 hours.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Start Time = 03:18 p.m., End Time = 08:18 p.m.</p>
    <p>2. Minute digits match exactly (:18).</p>
    <p>3. Elapsed Hours = 8 − 3 = <strong>5 hours</strong>.</p>
</div>
"""
            },
            {
                "id": 4,
                "question": "How much time elapses between 09:15 a.m. and 11:30 a.m.?",
                "options": [
                    "2 hours 15 minutes",
                    "2 hours 30 minutes",
                    "1 hour 45 minutes",
                    "3 hours 15 minutes"
                ],
                "answer": 0,
                "hint": "Jump 2 hours to 11:15 a.m., then count minutes to 11:30 a.m.",
                "explanation": "09:15 to 11:15 = 2 hours. 11:15 to 11:30 = 15 minutes. Total = 2 hr 15 min.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. 09:15 a.m. ➔ (+2 hours) ➔ 11:15 a.m.</p>
    <p>2. 11:15 a.m. ➔ (+15 minutes) ➔ 11:30 a.m.</p>
    <p>3. Total Duration = <strong>2 hours 15 minutes</strong>.</p>
</div>
"""
            },
            {
                "id": 5,
                "question": "In a painting contest, Student 3 painted for 1 hr 30 min while Student 4 painted for 40 min. Who took longer and by how much?",
                "options": [
                    "Student 3 took longer by 50 minutes",
                    "Student 4 took longer by 10 minutes",
                    "Student 3 took longer by 30 minutes",
                    "Both took the exact same time"
                ],
                "answer": 0,
                "hint": "Convert 1 hr 30 min to 90 min, then subtract 40 min.",
                "explanation": "Student 3: 90 min. Student 4: 40 min. 90 - 40 = 50 min difference.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Student 3's Duration = 1 hr 30 min = 60 + 30 = 90 minutes.</p>
    <p>2. Student 4's Duration = 40 minutes.</p>
    <p>3. 90 − 40 = <strong>50 minutes</strong> (Student 3 took longer).</p>
</div>
"""
            },
            {
                "id": 6,
                "question": "What is 04:30 p.m. in 24-hour railway time?",
                "options": [
                    "16:30 hours (4 + 12 = 16)",
                    "04:30 hours",
                    "14:30 hours",
                    "18:30 hours"
                ],
                "answer": 0,
                "hint": "Add 12 to the hour for p.m. times.",
                "explanation": "4 + 12 = 16, so 04:30 p.m. is 16:30 hours.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Rule: To convert p.m. time after noon to 24-hour time, add 12 to hours.</p>
    <p>2. 4 + 12 = 16.</p>
    <p>3. 04:30 p.m. = <strong>16:30 hours</strong>.</p>
</div>
"""
            },
            {
                "id": 7,
                "question": "A digital clock reads 21:45 hours. What is this in 12-hour format?",
                "options": [
                    "09:45 p.m. (21 - 12 = 9)",
                    "09:45 a.m.",
                    "11:45 p.m.",
                    "07:45 p.m."
                ],
                "answer": 0,
                "hint": "Subtract 12 from 21: 21 - 12 = 9.",
                "explanation": "21 - 12 = 9. Since it is greater than 12, it is 09:45 p.m.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. 21:45 is greater than 12:00, indicating post meridiem (p.m.).</p>
    <p>2. 21 − 12 = 9.</p>
    <p>3. 21:45 hours = <strong>09:45 p.m.</strong></p>
</div>
"""
            },
            {
                "id": 8,
                "question": "What is 12:00 midnight in 24-hour clock notation?",
                "options": [
                    "00:00 hours",
                    "12:00 hours",
                    "24:60 hours",
                    "01:00 hours"
                ],
                "answer": 0,
                "hint": "The new 24-hour day begins at zero hours.",
                "explanation": "Midnight marks the beginning of the 24-hour day and is written as 00:00 hours.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. A standard day consists of 24 hours.</p>
    <p>2. Midnight resets the cycle and begins at <strong>00:00 hours</strong>.</p>
    <p>3. (12:00 hours represents midday noon).</p>
</div>
"""
            },
            {
                "id": 9,
                "question": "How is 11:20 a.m. written in 24-hour time?",
                "options": [
                    "11:20 hours",
                    "23:20 hours",
                    "01:20 hours",
                    "12:20 hours"
                ],
                "answer": 0,
                "hint": "Only p.m. hours have 12 added to them.",
                "explanation": "Morning hours before noon do not change in 24-hour time: 11:20 a.m. = 11:20 hours.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. 11:20 a.m. is in the morning before midday noon.</p>
    <p>2. In 24-hour time, hours before noon remain identical: <strong>11:20 hours</strong>.</p>
    <p>3. (We only add 12 to post-meridiem p.m. hours).</p>
</div>
"""
            },
            {
                "id": 10,
                "question": "A bus leaves at 13:10 hours and reaches its destination at 15:40 hours. What is the journey duration?",
                "options": [
                    "2 hours 30 minutes",
                    "1 hour 30 minutes",
                    "3 hours 10 minutes",
                    "2 hours 10 minutes"
                ],
                "answer": 0,
                "hint": "Subtract 13:10 from 15:40: (15 - 13) hours and (40 - 10) minutes.",
                "explanation": "15 - 13 = 2 hours; 40 - 10 = 30 minutes. Duration = 2 hr 30 min.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Hours elapsed = 15 − 13 = 2 hours.</p>
    <p>2. Minutes elapsed = 40 − 10 = 30 minutes.</p>
    <p>3. Total Duration = <strong>2 hours 30 minutes</strong>.</p>
</div>
"""
            }
        ]
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "tagline": "Mastery Challenge 2 • Seconds & Time Unit Estimation",
        "lecture": "Welcome to Mastery Challenge 2. In this round, you will test your knowledge of seconds as precision units, one-minute activity verifications, and estimating whether actions take seconds or minutes.",
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-teal-900/40 to-emerald-900/40 border border-teal-500/30 rounded-xl p-4">
        <h4 class="text-teal-300 font-bold text-sm tracking-wider uppercase mb-1">Challenge Overview</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Test your understanding of the 1 min = 60 seconds relationship, sub-minute sprints, time estimation for everyday actions, and 60-second physical activity benchmarks.
        </p>
    </div>
</div>
""",
        "questions": [
            {
                "id": 1,
                "question": "How many seconds are in 1 complete minute?",
                "options": [
                    "60 seconds",
                    "100 seconds",
                    "10 seconds",
                    "360 seconds"
                ],
                "answer": 0,
                "hint": "The slender seconds hand makes one full 360-degree sweep.",
                "explanation": "1 minute is defined as exactly 60 seconds.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. The standard definition of time links minutes to seconds.</p>
    <p>2. <strong>1 Minute = 60 Seconds</strong>.</p>
</div>
"""
            },
            {
                "id": 2,
                "question": "In the 200m walking race, Runner A finished in 2 min 14 sec, while Runner C finished in 2 min 18 sec. Who won and by how many seconds?",
                "options": [
                    "Runner A won by 4 seconds",
                    "Runner C won by 4 seconds",
                    "Runner A won by 14 seconds",
                    "Both tied because both took 2 minutes"
                ],
                "answer": 0,
                "hint": "In a race, the person with the smaller time wins.",
                "explanation": "Runner A took less time: 2 min 18 sec - 2 min 14 sec = 4 seconds lead.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Runner A's time = 2 min 14 sec (134s).</p>
    <p>2. Runner C's time = 2 min 18 sec (138s).</p>
    <p>3. 138 − 134 = 4 seconds. <strong>Runner A won by 4 seconds</strong>.</p>
</div>
"""
            },
            {
                "id": 3,
                "question": "Which of the following activities takes approximately seconds rather than minutes?",
                "options": [
                    "Flipping on a light switch or blinking an eye",
                    "Baking a tray of cookies",
                    "Taking a math exam",
                    "Watching a feature film"
                ],
                "answer": 0,
                "hint": "Look for an action that happens almost instantly.",
                "explanation": "Blinking or flipping a switch takes under 1 second.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Blinking an eye takes ~0.3 seconds.</p>
    <p>2. Baking, exams, and movies take many minutes or hours.</p>
    <p>3. Correct choice: <strong>Flipping a light switch or blinking</strong>.</p>
</div>
"""
            },
            {
                "id": 4,
                "question": "How many seconds are in 3 minutes?",
                "options": [
                    "180 seconds (3 × 60 = 180)",
                    "150 seconds",
                    "300 seconds",
                    "90 seconds"
                ],
                "answer": 0,
                "hint": "Multiply 3 by 60.",
                "explanation": "3 × 60 = 180 seconds.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. 1 minute = 60 seconds.</p>
    <p>2. 3 minutes = 3 × 60 = <strong>180 seconds</strong>.</p>
</div>
"""
            },
            {
                "id": 5,
                "question": "A fifth-grade student can sprint 100 metres in approximately which duration?",
                "options": [
                    "16 to 22 seconds",
                    "1 to 2 seconds",
                    "5 minutes",
                    "60 seconds"
                ],
                "answer": 0,
                "hint": "World record is ~9.6 sec; fifth graders typically take around 18-20 sec.",
                "explanation": "A realistic 100m sprint time for a 10-year-old child is between 16 and 22 seconds.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. 100m sprint is a high-speed athletic sprint.</p>
    <p>2. Fifth graders average <strong>16 to 22 seconds</strong>.</p>
</div>
"""
            },
            {
                "id": 6,
                "question": "Writing the word 'FRIEND' in neat cursive handwriting typically takes approximately:",
                "options": [
                    "5 seconds",
                    "5 minutes",
                    "1 hour",
                    "60 seconds"
                ],
                "answer": 0,
                "hint": "Writing 6 letters takes just a few quick seconds.",
                "explanation": "Writing a short 6-letter word takes roughly 4 to 7 seconds.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. The word 'FRIEND' has 6 letters.</p>
    <p>2. Handwriting speed tests show it takes approximately <strong>5 seconds</strong>.</p>
</div>
"""
            },
            {
                "id": 7,
                "question": "How many seconds are in half of a minute plus 15 seconds?",
                "options": [
                    "45 seconds (30 + 15 = 45)",
                    "35 seconds",
                    "50 seconds",
                    "60 seconds"
                ],
                "answer": 0,
                "hint": "Half of a minute is 30 seconds. Then add 15.",
                "explanation": "1/2 min = 30s. 30 + 15 = 45 seconds.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Half a minute = 60 ÷ 2 = 30 seconds.</p>
    <p>2. 30 + 15 = <strong>45 seconds</strong>.</p>
</div>
"""
            },
            {
                "id": 8,
                "question": "Which of the following activities is best measured in minutes rather than seconds?",
                "options": [
                    "Brushing your teeth thoroughly",
                    "Snapping your fingers",
                    "Sneezing",
                    "Dropping an eraser to the floor"
                ],
                "answer": 0,
                "hint": "Dentists recommend taking at least 2 minutes.",
                "explanation": "Brushing teeth takes about 2 to 3 minutes.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Sneezing, snapping, and dropping an object take under 1 second.</p>
    <p>2. Brushing teeth takes 2 to 3 <strong>minutes</strong>.</p>
</div>
"""
            },
            {
                "id": 9,
                "question": "If you take 18 breaths in 1 minute, how many breaths do you take in 5 minutes at that same resting rate?",
                "options": [
                    "90 breaths (18 × 5 = 90)",
                    "80 breaths",
                    "100 breaths",
                    "72 breaths"
                ],
                "answer": 0,
                "hint": "Multiply 18 by 5.",
                "explanation": "18 × 5 = 90 breaths in 5 minutes.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Breaths per minute = 18.</p>
    <p>2. In 5 minutes = 18 × 5 = <strong>90 breaths</strong>.</p>
</div>
"""
            },
            {
                "id": 10,
                "question": "Why do sports stopwatches display seconds and hundredths of seconds?",
                "options": [
                    "To accurately separate competitors whose race times differ by tiny fractions",
                    "Because numbers smaller than 60 cannot be counted",
                    "To make the watch run faster",
                    "Because minutes do not exist in athletic sports"
                ],
                "answer": 0,
                "hint": "Think about ties in Olympic sprint races.",
                "explanation": "Fractions of seconds provide the fine resolution required to break ties in fast athletic contests.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Athletes can finish separated by fractions of a second.</p>
    <p>2. Stopwatches display hundredths of seconds to ensure fair, unambiguous ranking.</p>
</div>
"""
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "tagline": "Mastery Challenge 3 • Analog Seconds Hands & Double Number Lines",
        "lecture": "Welcome to Mastery Challenge 3. In this section, you will evaluate the geometric movement of the clock seconds hand and practice unit conversions using double number lines.",
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-purple-900/40 to-pink-900/40 border border-purple-500/30 rounded-xl p-4">
        <h4 class="text-purple-300 font-bold text-sm tracking-wider uppercase mb-1">Challenge Overview</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Test your mastery of clock dial number gaps, drawing seconds hand positions, converting hours to minutes, and navigating double number lines.
        </p>
    </div>
</div>
""",
        "questions": [
            {
                "id": 1,
                "question": "On an analog clock, how many seconds are represented by the gap between two consecutive numbers (e.g., from 1 to 2)?",
                "options": [
                    "5 seconds",
                    "1 second",
                    "10 seconds",
                    "12 seconds"
                ],
                "answer": 0,
                "hint": "There are 60 seconds divided among 12 numbers: 60 ÷ 12.",
                "explanation": "60 seconds ÷ 12 numbers = 5 seconds per number gap.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Clock dial perimeter = 60 seconds.</p>
    <p>2. 12 major numeral divisions.</p>
    <p>3. 60 ÷ 12 = <strong>5 seconds per numeral gap</strong>.</p>
</div>
"""
            },
            {
                "id": 2,
                "question": "If the seconds hand starts at 12 and takes 25 seconds to complete an activity, which numeral will it point to?",
                "options": [
                    "Numeral 5 (25 ÷ 5 = 5)",
                    "Numeral 4",
                    "Numeral 6",
                    "Numeral 3"
                ],
                "answer": 0,
                "hint": "Divide 25 by 5.",
                "explanation": "25 seconds ÷ 5 seconds/numeral = numeral 5.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Starting position = 12 (0s).</p>
    <p>2. Target seconds = 25s.</p>
    <p>3. 25 ÷ 5 = <strong>Numeral 5</strong>.</p>
</div>
"""
            },
            {
                "id": 3,
                "question": "The seconds hand starts at numeral 1 (5s) and moves to numeral 8 (40s). How many seconds have elapsed?",
                "options": [
                    "35 seconds ((8 - 1) × 5 = 7 × 5 = 35)",
                    "40 seconds",
                    "30 seconds",
                    "45 seconds"
                ],
                "answer": 0,
                "hint": "Subtract 1 from 8 (7 steps), then multiply by 5.",
                "explanation": "40s - 5s = 35 seconds (or 7 steps × 5 = 35s).",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Start = 1 (5s), End = 8 (40s).</p>
    <p>2. 40 − 5 = <strong>35 seconds</strong>.</p>
</div>
"""
            },
            {
                "id": 4,
                "question": "To represent an elapsed time of 40 seconds starting from 12, where should the seconds hand point?",
                "options": [
                    "Numeral 8 (40 ÷ 5 = 8)",
                    "Numeral 7",
                    "Numeral 9",
                    "Numeral 6"
                ],
                "answer": 0,
                "hint": "Divide 40 by 5.",
                "explanation": "40 ÷ 5 = 8. It points directly at numeral 8.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Elapsed seconds = 40.</p>
    <p>2. Position = 40 ÷ 5 = <strong>Numeral 8</strong>.</p>
</div>
"""
            },
            {
                "id": 5,
                "question": "Convert 1 hour and 10 minutes into total minutes.",
                "options": [
                    "70 minutes ((1 × 60) + 10 = 70)",
                    "60 minutes",
                    "110 minutes",
                    "80 minutes"
                ],
                "answer": 0,
                "hint": "1 hour = 60 minutes. 60 + 10 = 70.",
                "explanation": "1 hr = 60 min. 60 + 10 = 70 minutes.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. 1 hour = 60 minutes.</p>
    <p>2. 60 + 10 = <strong>70 minutes</strong>.</p>
</div>
"""
            },
            {
                "id": 6,
                "question": "Convert 220 minutes into hours and minutes.",
                "options": [
                    "3 hours 40 minutes (180 min + 40 min)",
                    "2 hours 40 minutes",
                    "3 hours 20 minutes",
                    "4 hours 10 minutes"
                ],
                "answer": 0,
                "hint": "Divide 220 by 60: 3 × 60 = 180, remainder is 40.",
                "explanation": "220 ÷ 60 = 3 with remainder 40, which is 3 hr 40 min.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. 220 ÷ 60 = 3 (hours).</p>
    <p>2. 3 × 60 = 180 minutes.</p>
    <p>3. Remainder = 220 − 180 = 40 minutes.</p>
    <p>4. Result = <strong>3 hours 40 minutes</strong>.</p>
</div>
"""
            },
            {
                "id": 7,
                "question": "On an hours-and-minutes double number line, what minute value lies directly under 4 hours?",
                "options": [
                    "240 minutes (4 × 60 = 240)",
                    "200 minutes",
                    "180 minutes",
                    "300 minutes"
                ],
                "answer": 0,
                "hint": "Multiply 4 by 60.",
                "explanation": "4 × 60 = 240 minutes.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. 1 hour = 60 minutes.</p>
    <p>2. 4 hours = 4 × 60 = <strong>240 minutes</strong>.</p>
</div>
"""
            },
            {
                "id": 8,
                "question": "Convert 320 seconds into minutes and seconds.",
                "options": [
                    "5 minutes 20 seconds (300s + 20s)",
                    "5 minutes 10 seconds",
                    "6 minutes 20 seconds",
                    "4 minutes 40 seconds"
                ],
                "answer": 0,
                "hint": "Divide 320 by 60: 5 × 60 = 300, remainder is 20.",
                "explanation": "320 ÷ 60 = 5 with remainder 20. 5 min 20 sec.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. 5 minutes = 5 × 60 = 300 seconds.</p>
    <p>2. 320 − 300 = 20 seconds.</p>
    <p>3. Result = <strong>5 minutes 20 seconds</strong>.</p>
</div>
"""
            },
            {
                "id": 9,
                "question": "How many total seconds are in 10 minutes and 13 seconds?",
                "options": [
                    "613 seconds ((10 × 60) + 13 = 600 + 13 = 613)",
                    "113 seconds",
                    "630 seconds",
                    "700 seconds"
                ],
                "answer": 0,
                "hint": "10 minutes = 600 seconds, then add 13.",
                "explanation": "10 × 60 = 600 seconds. 600 + 13 = 613 seconds.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. 10 minutes = 10 × 60 = 600 seconds.</p>
    <p>2. 600 + 13 = <strong>613 seconds</strong>.</p>
</div>
"""
            },
            {
                "id": 10,
                "question": "What is the angle through which the seconds hand turns in 15 seconds?",
                "options": [
                    "90 degrees (quarter turn)",
                    "180 degrees (half turn)",
                    "45 degrees",
                    "60 degrees"
                ],
                "answer": 0,
                "hint": "15 seconds is 1/4 of 60 seconds. 360° ÷ 4 = 90°.",
                "explanation": "15/60 = 1/4 of a circle. 360° × 1/4 = 90° (a right angle quarter turn).",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Full circle = 60 seconds = 360°.</p>
    <p>2. 15 seconds = 15/60 = 1/4 turn.</p>
    <p>3. 360° ÷ 4 = <strong>90°</strong> (right angle).</p>
</div>
"""
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "tagline": "Mastery Challenge 4 • Applied Word Problems & Daily Schedules",
        "lecture": "Welcome to Mastery Challenge 4. In this final challenge, you will prove your mastery of travel itineraries, homework start and end calculations, and coordinating complex daily schedules.",
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-amber-900/40 to-rose-900/40 border border-amber-500/30 rounded-xl p-4">
        <h4 class="text-amber-300 font-bold text-sm tracking-wider uppercase mb-1">Final Challenge Overview</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Apply your time calculation skills to multi-step real-world problems: picnic departure and arrival times, study intervals, future time offsets, and working backward to meet deadlines.
        </p>
    </div>
</div>
""",
        "questions": [
            {
                "id": 1,
                "question": "A school bus departs for a picnic at 08:30 a.m. The journey takes 1 hour and 45 minutes. At what time does the bus arrive?",
                "options": [
                    "10:15 a.m.",
                    "10:30 a.m.",
                    "09:45 a.m.",
                    "10:00 a.m."
                ],
                "answer": 0,
                "hint": "08:30 + 1 hr = 09:30. 09:30 + 30 min = 10:00. 10:00 + 15 min = 10:15.",
                "explanation": "08:30 + 1 hr 45 min = 10:15 a.m.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. 08:30 a.m. + 1 hour = 09:30 a.m.</p>
    <p>2. 09:30 a.m. + 30 minutes = 10:00 a.m.</p>
    <p>3. 10:00 a.m. + 15 minutes = <strong>10:15 a.m.</strong></p>
</div>
"""
            },
            {
                "id": 2,
                "question": "A student started studying at 04:15 p.m. and finished at 05:40 p.m. How long was the study session?",
                "options": [
                    "1 hour 25 minutes",
                    "1 hour 35 minutes",
                    "1 hour 15 minutes",
                    "2 hours"
                ],
                "answer": 0,
                "hint": "From 04:15 to 05:15 is 1 hour. From 05:15 to 05:40 is 25 minutes.",
                "explanation": "1 hr + 25 min = 1 hour 25 minutes.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. 04:15 p.m. ➔ (+1 hour) ➔ 05:15 p.m.</p>
    <p>2. 05:15 p.m. ➔ (+25 minutes) ➔ 05:40 p.m.</p>
    <p>3. Total Study Time = <strong>1 hour 25 minutes</strong>.</p>
</div>
"""
            },
            {
                "id": 3,
                "question": "A lunch break starts at 12:15 p.m. and ends 40 minutes later. What time does afternoon school resume?",
                "options": [
                    "12:55 p.m.",
                    "01:00 p.m.",
                    "12:45 p.m.",
                    "01:15 p.m."
                ],
                "answer": 0,
                "hint": "Add 40 minutes to 15 minutes past 12.",
                "explanation": "15 + 40 = 55 minutes past 12 = 12:55 p.m.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Start = 12:15 p.m.</p>
    <p>2. Minutes = 15 + 40 = 55.</p>
    <p>3. Finish Time = <strong>12:55 p.m.</strong></p>
</div>
"""
            },
            {
                "id": 4,
                "question": "An evening football match began at 04:30 p.m. and ended at 06:10 p.m. What was the total match duration?",
                "options": [
                    "1 hour 40 minutes",
                    "1 hour 30 minutes",
                    "2 hours 10 minutes",
                    "1 hour 50 minutes"
                ],
                "answer": 0,
                "hint": "04:30 to 05:30 is 1 hour. 05:30 to 06:00 is 30 min. 06:00 to 06:10 is 10 min.",
                "explanation": "1 hr + 30 min + 10 min = 1 hr 40 min.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. 04:30 p.m. ➔ (+1 hour) ➔ 05:30 p.m.</p>
    <p>2. 05:30 p.m. ➔ (+30 minutes) ➔ 06:00 p.m.</p>
    <p>3. 06:00 p.m. ➔ (+10 minutes) ➔ 06:10 p.m.</p>
    <p>4. Total Duration = 1 hr + 30 min + 10 min = <strong>1 hour 40 minutes</strong>.</p>
</div>
"""
            },
            {
                "id": 5,
                "question": "You must arrive at the examination hall by 08:45 a.m. If traveling takes 35 minutes, what is the latest time you should depart from home?",
                "options": [
                    "08:10 a.m. (8:45 minus 35 min)",
                    "08:15 a.m.",
                    "08:20 a.m.",
                    "08:00 a.m."
                ],
                "answer": 0,
                "hint": "Subtract 35 minutes from 45 minutes past 8.",
                "explanation": "45 - 35 = 10. The departure time is 08:10 a.m.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. Arrival Deadline = 08:45 a.m.</p>
    <p>2. Travel Time = 35 minutes.</p>
    <p>3. Departure = 08:45 − 0:35 = <strong>08:10 a.m.</strong></p>
</div>
"""
            },
            {
                "id": 6,
                "question": "A train journey takes 4 hours and 50 minutes. If the train leaves at 06:20 a.m., when does it arrive?",
                "options": [
                    "11:10 a.m.",
                    "11:20 a.m.",
                    "10:50 a.m.",
                    "11:00 a.m."
                ],
                "answer": 0,
                "hint": "06:20 + 4 hr = 10:20. 10:20 + 40 min = 11:00. 11:00 + 10 min = 11:10.",
                "explanation": "06:20 + 4 hr = 10:20 a.m. Adding 50 min: 10:20 + 40 min = 11:00, + 10 min = 11:10 a.m.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. 06:20 a.m. + 4 hours = 10:20 a.m.</p>
    <p>2. 10:20 a.m. + 40 min = 11:00 a.m.</p>
    <p>3. 11:00 a.m. + 10 min = <strong>11:10 a.m.</strong></p>
</div>
"""
            },
            {
                "id": 7,
                "question": "A music concert is 150 minutes long. If it starts at 07:00 p.m., at what time does it conclude?",
                "options": [
                    "09:30 p.m. (150 min = 2 hr 30 min)",
                    "09:00 p.m.",
                    "08:30 p.m.",
                    "10:00 p.m."
                ],
                "answer": 0,
                "hint": "Convert 150 minutes to 2 hours 30 minutes, then add to 7:00 p.m.",
                "explanation": "150 min = 2 hr 30 min. 07:00 p.m. + 2 hr 30 min = 09:30 p.m.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. 150 minutes = 120 min + 30 min = 2 hours 30 minutes.</p>
    <p>2. 07:00 p.m. + 2 hr 30 min = <strong>09:30 p.m.</strong></p>
</div>
"""
            },
            {
                "id": 8,
                "question": "Runner A walks 1 kilometre in 14 minutes and 30 seconds. How many seconds is this in total?",
                "options": [
                    "870 seconds ((14 × 60) + 30 = 840 + 30 = 870)",
                    "840 seconds",
                    "750 seconds",
                    "900 seconds"
                ],
                "answer": 0,
                "hint": "14 × 60 = 840 seconds. Then add 30 seconds.",
                "explanation": "14 × 60 = 840s. 840 + 30 = 870 seconds.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. 14 minutes = 14 × 60 = 840 seconds.</p>
    <p>2. 840 + 30 = <strong>870 seconds</strong>.</p>
</div>
"""
            },
            {
                "id": 9,
                "question": "A school day starts at 08:00 a.m. and ends at 02:15 p.m. How long is the total school day?",
                "options": [
                    "6 hours 15 minutes",
                    "5 hours 15 minutes",
                    "6 hours 45 minutes",
                    "7 hours 15 minutes"
                ],
                "answer": 0,
                "hint": "08:00 to 12:00 is 4 hours. 12:00 to 02:15 is 2 hours 15 minutes.",
                "explanation": "4 hours + 2 hours 15 minutes = 6 hours 15 minutes.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. 08:00 a.m. ➔ 12:00 noon = 4 hours.</p>
    <p>2. 12:00 noon ➔ 02:15 p.m. = 2 hours 15 minutes.</p>
    <p>3. Total School Day = 4 hr + 2 hr 15 min = <strong>6 hours 15 minutes</strong>.</p>
</div>
"""
            },
            {
                "id": 10,
                "question": "Which of the following time statements is mathematically true?",
                "options": [
                    "1 hour = 60 minutes, 1 minute = 60 seconds, and 1 hour = 3,600 seconds",
                    "1 hour contains 100 minutes",
                    "1 minute contains 100 seconds",
                    "24-hour time resets to 01:00 at midday noon"
                ],
                "answer": 0,
                "hint": "60 minutes × 60 seconds = 3,600 seconds in an hour.",
                "explanation": "1 hr = 60 min; 1 min = 60 sec; 1 hr = 60 × 60 = 3,600 seconds.",
                "solution_html": """
<div class='space-y-2 text-sm'>
    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>
    <p>1. 1 Hour = 60 Minutes.</p>
    <p>2. 1 Minute = 60 Seconds.</p>
    <p>3. 1 Hour = 60 × 60 = <strong>3,600 Seconds</strong>.</p>
</div>
"""
            }
        ]
    }
]
