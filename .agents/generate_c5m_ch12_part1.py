# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 12: Racing Seconds
Part 1 Data: Slides 1 to 8
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Yoga Elapsed Time",
        "tagline": "Morning Routine • Start Times, End Times, and Finding Total Elapsed Duration",
        "lecture": (
            "Every single morning, a dedicated student begins the day with a rejuvenating sequence of traditional yoga asanas to keep mind "
            "and body active, flexible, and healthy. When unrolling the colorful yoga mat on the cool veranda floor, the household wall clock "
            "clearly shows a start time of 06:15 a.m. After completing disciplined sun salutations, breathing pranayama exercises, and "
            "calming relaxation poses, the student checks the clock once more: the time now reads 07:05 a.m. How long did the student spend "
            "practicing yoga? To calculate the total elapsed duration of any activity, we find the mathematical difference between the finishing "
            "time and the starting time. From 06:15 a.m., moving forward 45 minutes brings the clock hands to the friendly milestone of 07:00 a.m. "
            "Then, moving forward an additional 5 minutes reaches the final time of 07:05 a.m. Adding these two simple intervals together, "
            "45 minutes plus 5 minutes gives a total elapsed duration of exactly 50 minutes! Breaking down continuous time into friendly "
            "milestone intervals—such as jumping forward to the nearest full hour—is a powerful mental math technique. Whether timing morning "
            "exercises, preparing breakfast, or catching the school bus, understanding elapsed time helps us organize our daily lives with clarity."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-amber-900/40 via-orange-900/30 to-amber-900/40 border border-amber-500/30 rounded-xl p-4">
        <h4 class="text-amber-300 font-bold text-sm tracking-wider uppercase mb-1">Elapsed Time Principle</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Elapsed duration represents the total time that passes from the start of an event to its completion:
            <span class="text-amber-300 font-bold">Elapsed Time = End Time − Start Time</span>.
        </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
        <div class="bg-slate-800/80 border border-slate-700/70 rounded-xl p-3 text-center">
            <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Start Time</span>
            <div class="my-2 bg-slate-900/80 p-2 rounded border border-slate-700">
                <div class="text-lg font-black text-white font-mono">06:15 a.m.</div>
                <div class="text-xs text-slate-400 mt-1">Veranda Clock</div>
            </div>
            <p class="text-xs text-slate-400">The student begins morning yoga asanas.</p>
        </div>

        <div class="bg-slate-800/80 border border-slate-700/70 rounded-xl p-3 text-center">
            <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Friendly Milestone</span>
            <div class="my-2 bg-slate-900/80 p-2 rounded border border-slate-700">
                <div class="text-lg font-black text-amber-300 font-mono">+45 min ➔ 07:00</div>
                <div class="text-xs text-slate-400 mt-1">Jump to Nearest Hour</div>
            </div>
            <p class="text-xs text-slate-400">Bridge forward to the next full hour mark.</p>
        </div>

        <div class="bg-slate-800/80 border border-slate-700/70 rounded-xl p-3 text-center">
            <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">Finish Time</span>
            <div class="my-2 bg-slate-900/80 p-2 rounded border border-slate-700">
                <div class="text-lg font-black text-emerald-300 font-mono">07:05 a.m.</div>
                <div class="text-xs text-emerald-400 font-mono mt-1">+5 min = 50 min total</div>
            </div>
            <p class="text-xs text-slate-400">Total duration = 45 min + 5 min = 50 min.</p>
        </div>
    </div>

    <div class="bg-slate-900/80 border border-slate-700 rounded-xl p-3 flex items-center justify-between text-xs">
        <span class="text-slate-400 font-semibold uppercase tracking-wider">Elapsed Time Equation:</span>
        <span class="text-cyan-300 font-mono font-bold">06:15 a.m. ➔ (+45 min) ➔ 07:00 a.m. ➔ (+5 min) ➔ 07:05 a.m. (Total = 50 min)</span>
    </div>
</div>
""",
        "checkpoints": [
            {
                "id": "cp_1_1",
                "question": "If an online yoga class starts at 06:20 a.m. and finishes at 07:05 a.m., what is the total elapsed time?",
                "options": [
                    "45 minutes (40 min to 7:00 + 5 min)",
                    "35 minutes",
                    "55 minutes",
                    "1 hour 15 minutes"
                ],
                "answer": 0,
                "explanation": "From 06:20 to 07:00 is 40 minutes. From 07:00 to 07:05 is 5 minutes. 40 + 5 = 45 minutes total.",
                "hint": "Count minutes forward to 7:00 a.m. first, then add the remaining minutes."
            },
            {
                "id": "cp_1_2",
                "question": "Which mathematical operation is used to find the elapsed duration between a start time and an end time?",
                "options": [
                    "Subtraction (End Time minus Start Time)",
                    "Addition (Start Time plus End Time)",
                    "Multiplication of hours and minutes",
                    "Division of time by 60"
                ],
                "answer": 0,
                "explanation": "Elapsed duration is the difference between finish time and start time, calculated using subtraction.",
                "hint": "Think about finding the gap or difference between two clock readings."
            }
        ]
    },
    {
        "id": 2,
        "title": "Interval Durations",
        "tagline": "Time Intervals • Calculating Elapsed Gaps Across Hours and Minutes",
        "lecture": (
            "Calculating the exact duration that passes between two clock events becomes effortless once you master the step-by-step "
            "timeline jump method. Let us explore three practical everyday examples. First, consider an afternoon music practice session that "
            "begins at 01:15 p.m. and ends at 01:42 p.m. Here, both times fall within the exact same hour of 1 o'clock. We simply subtract the "
            "starting minutes from the ending minutes: 42 minus 15 equals 27 minutes of elapsed practice! Next, examine a longer gap: an evening "
            "homework study session starting at 03:18 p.m. and wrapping up at 08:18 p.m. Because the minute readings are identical at 18 minutes "
            "past the hour, we simply calculate the whole hour difference: 8 minus 3 equals exactly 5 hours of focused study! "
            "Finally, let us solve a mixed morning interval from 09:15 a.m. to 11:30 a.m. Step one: jump forward 2 full hours from 09:15 a.m. "
            "to 11:15 a.m. Step two: jump forward from 11:15 a.m. to 11:30 a.m., which is an additional 15 minutes. Combining these two jumps "
            "gives a grand total of 2 hours and 15 minutes! Splitting calculations into distinct hour jumps and minute jumps eliminates confusion "
            "and prevents calculation errors, making time arithmetic simple, logical, and reliable."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
        <!-- Interval 1 -->
        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-3">
            <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Same Hour Interval</span>
            <h5 class="text-white font-bold text-sm mt-1">01:15 p.m. ➔ 01:42 p.m.</h5>
            <div class="mt-2 text-xs text-slate-300 font-mono bg-slate-900/80 p-2.5 rounded border border-slate-700 space-y-1">
                <div>Hours are identical (1 p.m.)</div>
                <div>Elapsed = 42 − 15</div>
                <div class="text-cyan-300 font-bold text-sm">= 27 minutes</div>
            </div>
            <p class="text-xs text-slate-400 mt-2">Direct minute subtraction.</p>
        </div>

        <!-- Interval 2 -->
        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-3">
            <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Same Minute Interval</span>
            <h5 class="text-white font-bold text-sm mt-1">03:18 p.m. ➔ 08:18 p.m.</h5>
            <div class="mt-2 text-xs text-slate-300 font-mono bg-slate-900/80 p-2.5 rounded border border-slate-700 space-y-1">
                <div>Minutes match (:18)</div>
                <div>Elapsed = 8 − 3</div>
                <div class="text-amber-300 font-bold text-sm">= 5 hours</div>
            </div>
            <p class="text-xs text-slate-400 mt-2">Direct hour subtraction.</p>
        </div>

        <!-- Interval 3 -->
        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-3">
            <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">Mixed Interval</span>
            <h5 class="text-white font-bold text-sm mt-1">09:15 a.m. ➔ 11:30 a.m.</h5>
            <div class="mt-2 text-xs text-slate-300 font-mono bg-slate-900/80 p-2.5 rounded border border-slate-700 space-y-1">
                <div>09:15 ➔ 11:15 = 2 hr</div>
                <div>11:15 ➔ 11:30 = 15 min</div>
                <div class="text-emerald-300 font-bold text-sm">= 2 hr 15 min</div>
            </div>
            <p class="text-xs text-slate-400 mt-2">Two-step jump method.</p>
        </div>
    </div>

    <div class="p-3 bg-indigo-950/40 border border-indigo-500/30 rounded-xl flex items-center justify-between text-xs">
        <span class="text-indigo-300 font-bold uppercase tracking-wider">Golden Rule:</span>
        <span class="text-slate-300">Always jump whole hours first, then calculate the leftover minutes!</span>
    </div>
</div>
""",
        "checkpoints": [
            {
                "id": "cp_2_1",
                "question": "How much time elapses between 04:20 p.m. and 07:50 p.m.?",
                "options": [
                    "3 hours 30 minutes",
                    "3 hours 20 minutes",
                    "2 hours 30 minutes",
                    "4 hours 10 minutes"
                ],
                "answer": 0,
                "explanation": "From 04:20 to 07:20 is 3 hours. From 07:20 to 07:50 is 30 minutes. Total = 3 hours 30 minutes.",
                "hint": "Jump 3 hours to 07:20, then subtract 20 from 50."
            },
            {
                "id": "cp_2_2",
                "question": "A train departs at 10:10 a.m. and arrives at 10:55 a.m. What is the journey duration?",
                "options": [
                    "45 minutes (55 - 10 = 45)",
                    "35 minutes",
                    "1 hour 15 minutes",
                    "55 minutes"
                ],
                "answer": 0,
                "explanation": "Since both times are in the 10 o'clock hour, subtract 10 from 55 to get 45 minutes.",
                "hint": "Both times share the same hour."
            }
        ]
    },
    {
        "id": 3,
        "title": "Comparing Durations",
        "tagline": "Duration Analysis • Ranking Longest and Shortest Time Taken Among Painters",
        "lecture": (
            "Inside our creative school art studio, several enthusiastic students participated in a vibrant painting competition where each "
            "child created an intricate watercolor landscape. The art instructor carefully recorded their exact start times and finish times in "
            "a structured data table to determine who spent the longest and shortest duration painting. Student 1 started at 10:00 a.m. and "
            "completed painting at 11:15 a.m., taking 1 hour and 15 minutes, which equals 75 minutes in total. Student 2 began painting at "
            "10:10 a.m. and finished at 11:00 a.m., working steadily for 50 minutes. Student 3 worked with great detail from 10:15 a.m. to "
            "11:45 a.m., spending 1 hour and 30 minutes, which equals 90 minutes. Finally, energetic Student 4 painted from 10:30 a.m. to "
            "11:10 a.m., finishing the artwork in just 40 minutes! To compare these four diverse durations accurately, we convert each duration "
            "into a single uniform unit: total minutes. Comparing 75 minutes, 50 minutes, 90 minutes, and 40 minutes, we observe that Student 3 "
            "took the longest time at 90 minutes, while Student 4 took the least time at 40 minutes! Standardizing mixed hour-and-minute "
            "measurements into total minutes enables effortless numerical ranking and clear comparisons across sports, science experiments, and "
            "creative classroom workshops."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="overflow-hidden border border-slate-700 rounded-xl bg-slate-900/80">
        <table class="w-full text-xs text-left text-slate-300">
            <thead class="bg-slate-800 text-slate-200 font-semibold uppercase tracking-wider">
                <tr>
                    <th class="p-3">Student</th>
                    <th class="p-3">Start Time</th>
                    <th class="p-3">Finish Time</th>
                    <th class="p-3">Duration (hr & min)</th>
                    <th class="p-3">Total Minutes</th>
                    <th class="p-3">Rank</th>
                </tr>
            </thead>
            <tbody class="divide-y divide-slate-800 font-mono">
                <tr class="hover:bg-slate-800/40">
                    <td class="p-3 text-white font-bold">Student 1</td>
                    <td class="p-3">10:00 a.m.</td>
                    <td class="p-3">11:15 a.m.</td>
                    <td class="p-3 text-cyan-400">1 hr 15 min</td>
                    <td class="p-3 text-cyan-300 font-bold">75 min</td>
                    <td class="p-3 text-slate-400">Rank 2</td>
                </tr>
                <tr class="hover:bg-slate-800/40">
                    <td class="p-3 text-white font-bold">Student 2</td>
                    <td class="p-3">10:10 a.m.</td>
                    <td class="p-3">11:00 a.m.</td>
                    <td class="p-3 text-amber-400">0 hr 50 min</td>
                    <td class="p-3 text-amber-300 font-bold">50 min</td>
                    <td class="p-3 text-slate-400">Rank 3</td>
                </tr>
                <tr class="hover:bg-slate-800/40 bg-indigo-950/30">
                    <td class="p-3 text-indigo-300 font-bold">Student 3</td>
                    <td class="p-3">10:15 a.m.</td>
                    <td class="p-3">11:45 a.m.</td>
                    <td class="p-3 text-indigo-400 font-bold">1 hr 30 min</td>
                    <td class="p-3 text-indigo-300 font-bold">90 min</td>
                    <td class="p-3 text-indigo-300 font-bold">★ Longest (Rank 1)</td>
                </tr>
                <tr class="hover:bg-slate-800/40 bg-emerald-950/30">
                    <td class="p-3 text-emerald-300 font-bold">Student 4</td>
                    <td class="p-3">10:30 a.m.</td>
                    <td class="p-3">11:10 a.m.</td>
                    <td class="p-3 text-emerald-400 font-bold">0 hr 40 min</td>
                    <td class="p-3 text-emerald-300 font-bold">40 min</td>
                    <td class="p-3 text-emerald-300 font-bold">⚡ Least (Rank 4)</td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="p-3 bg-slate-900/80 border border-slate-700 rounded-xl flex items-center justify-between text-xs">
        <span class="text-slate-400 font-semibold uppercase tracking-wider">Comparison Key:</span>
        <span class="text-cyan-300 font-mono">Convert 1 hr = 60 min, then add extra minutes: (1 × 60) + 15 = 75 min!</span>
    </div>
</div>
""",
        "checkpoints": [
            {
                "id": "cp_3_1",
                "question": "Which student spent the greatest amount of time painting their picture?",
                "options": [
                    "Student 3 (90 minutes)",
                    "Student 1 (75 minutes)",
                    "Student 2 (50 minutes)",
                    "Student 4 (40 minutes)"
                ],
                "answer": 0,
                "explanation": "Student 3 spent 1 hour 30 minutes, which equals 90 minutes, the longest of all four students.",
                "hint": "Check who has the highest total minute count in the table."
            },
            {
                "id": "cp_3_2",
                "question": "How much longer did Student 3 paint than Student 4?",
                "options": [
                    "50 minutes (90 min - 40 min)",
                    "30 minutes",
                    "10 minutes",
                    "1 hour"
                ],
                "answer": 0,
                "explanation": "Student 3 took 90 minutes and Student 4 took 40 minutes. 90 - 40 = 50 minutes difference.",
                "hint": "Subtract Student 4's 40 minutes from Student 3's 90 minutes."
            }
        ]
    },
    {
        "id": 4,
        "title": "24-Hour Clock",
        "tagline": "Military & Railway Notation • Eliminating A.M. and P.M. Confusion with 24 Hours",
        "lecture": (
            "Have you ever looked closely at an Indian Railways train ticket or an airport boarding pass and noticed departure times like "
            "16:30 or 21:15? These official transportation schedules use the continuous 24-hour clock format! In everyday conversation, we use "
            "a standard 12-hour clock with a.m. for ante meridiem before noon and p.m. for post meridiem after noon. However, to completely "
            "eliminate confusion between morning and evening departures, railways, airlines, emergency hospitals, and military units worldwide "
            "rely strictly on 24-hour time notation. Under the 24-hour clock system, midnight begins at 00:00 hours. The morning hours from "
            "01:00 to 11:59 remain almost identical to 12-hour time. Midday noon is 12:00 hours. But after 12:00 noon, instead of resetting to "
            "1:00 p.m., the hours keep counting upward continuously! To convert any p.m. time to 24-hour time, simply add 12 to the hour value: "
            "01:00 p.m. becomes 1 plus 12, or 13:00 hours; 04:30 p.m. becomes 4 plus 12, or 16:30 hours; and 09:15 p.m. becomes 9 plus 12, "
            "or 21:15 hours! Conversely, to convert from 24-hour time back to 12-hour p.m. time, subtract 12 from hours greater than 12. "
            "Mastering both time systems ensures you will navigate train stations, bus terminals, and flight journeys like a confident traveler."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="bg-gradient-to-br from-indigo-950/60 to-slate-900 border border-indigo-500/40 rounded-xl p-4">
            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">12-Hour System</span>
            <h4 class="text-white font-extrabold text-base mt-1">A.M. & P.M. Cycles</h4>
            <p class="text-xs text-slate-300 mt-2 leading-relaxed">
                Splits the 24-hour solar day into two 12-hour halves:
            </p>
            <div class="mt-3 space-y-1.5 font-mono text-xs text-slate-300 bg-slate-950/80 p-2.5 rounded border border-indigo-500/30">
                <div>• a.m. (ante meridiem): Midnight to Noon</div>
                <div>• p.m. (post meridiem): Noon to Midnight</div>
            </div>
        </div>

        <div class="bg-gradient-to-br from-emerald-950/60 to-slate-900 border border-emerald-500/40 rounded-xl p-4">
            <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">24-Hour Railway Clock</span>
            <h4 class="text-white font-extrabold text-base mt-1">Continuous 00:00 to 24:00</h4>
            <p class="text-xs text-slate-300 mt-2 leading-relaxed">
                Hours count continuously from 00:00 to 24:00 without a.m. or p.m.:
            </p>
            <div class="mt-3 space-y-1.5 font-mono text-xs text-emerald-300 bg-slate-950/80 p-2.5 rounded border border-emerald-500/30 font-bold">
                <div>Conversion Rule: P.M. Time + 12 Hours</div>
                <div>05:30 p.m. ➔ 5 + 12 = 17:30 Hours</div>
            </div>
        </div>
    </div>

    <!-- Quick Reference Conversion Chart -->
    <div class="bg-slate-900/80 border border-slate-700 rounded-xl p-3">
        <h5 class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-2">Common Daily Conversions</h5>
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs font-mono">
            <div class="bg-slate-800 p-2 rounded border border-slate-700">
                <div class="text-slate-400">06:00 a.m.</div>
                <div class="text-cyan-400 font-bold mt-1">06:00 Hours</div>
            </div>
            <div class="bg-slate-800 p-2 rounded border border-slate-700">
                <div class="text-slate-400">12:00 Noon</div>
                <div class="text-amber-400 font-bold mt-1">12:00 Hours</div>
            </div>
            <div class="bg-slate-800 p-2 rounded border border-slate-700">
                <div class="text-slate-400">03:45 p.m.</div>
                <div class="text-emerald-400 font-bold mt-1">15:45 Hours</div>
            </div>
            <div class="bg-slate-800 p-2 rounded border border-slate-700">
                <div class="text-slate-400">10:30 p.m.</div>
                <div class="text-rose-400 font-bold mt-1">22:30 Hours</div>
            </div>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "id": "cp_4_1",
                "question": "What is 07:45 p.m. expressed in 24-hour railway time?",
                "options": [
                    "19:45 hours (7 + 12 = 19)",
                    "07:45 hours",
                    "17:45 hours",
                    "21:45 hours"
                ],
                "answer": 0,
                "explanation": "For p.m. times after noon, add 12 to the hour: 7 + 12 = 19. So 07:45 p.m. = 19:45 hours.",
                "hint": "Add 12 to the hour value for p.m. time."
            },
            {
                "id": "cp_4_2",
                "question": "A train departure is listed as 20:15 hours on an electronic board. What is this in 12-hour time?",
                "options": [
                    "08:15 p.m. (20 - 12 = 8)",
                    "08:15 a.m.",
                    "10:15 p.m.",
                    "02:15 p.m."
                ],
                "answer": 0,
                "explanation": "Subtract 12 from hours exceeding 12: 20 - 12 = 8. Since 20 > 12, it is 08:15 p.m.",
                "hint": "Subtract 12 from 20."
            }
        ]
    },
    {
        "id": 5,
        "title": "School Race Seconds",
        "tagline": "Introducing Seconds • High-Precision Timing in a 200m School Walking Race",
        "lecture": (
            "During our annual sports day celebration at school, students gathered eagerly along the grassy track to cheer for the exciting "
            "200-metre walking race. Three swift competitors—Runner A, Runner B, and Runner C—stepped up proudly to the starting line. When the "
            "starter whistle blew, the sports coach clicked an accurate digital stopwatch. As the racers sped toward the bright finish ribbon, "
            "their times were recorded with extreme precision: Runner A finished in 2 minutes and 14 seconds; Runner B crossed the line in 2 "
            "minutes and 22 seconds; and Runner C completed the race in 2 minutes and 18 seconds! Notice something critically important: if the "
            "coach had only measured their times in whole minutes, all three racers would have appeared completely tied at 2 minutes! We would "
            "have had no fair way of knowing who won the gold medal! This demonstrates that minutes alone are not small enough to capture rapid "
            "physical events. To record swift races, heartbeats, and laboratory reactions, we need a smaller, more refined unit of time: the "
            "second! One single minute is divided into exactly sixty equal units called seconds. Thanks to seconds, Runner A was crowned champion "
            "with absolute fairness, finishing 4 seconds ahead of Runner C and 8 seconds ahead of Runner B."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-cyan-900/40 via-blue-900/30 to-cyan-900/40 border border-cyan-500/30 rounded-xl p-4">
        <h4 class="text-cyan-300 font-bold text-sm tracking-wider uppercase mb-1">Why We Need Seconds</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            In fast-paced races and quick activities, minutes are too large to separate winners from runners-up.
            <span class="text-amber-300 font-bold">Seconds provide the high precision needed for sports and science!</span>
        </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-3 text-center">
            <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">🥇 1st Place: Runner A</span>
            <div class="my-2 bg-slate-900/80 p-2 rounded border border-slate-700">
                <div class="text-base font-black text-white font-mono">2 min 14 sec</div>
                <div class="text-xs text-emerald-400 font-mono mt-1">134 Total Seconds</div>
            </div>
            <p class="text-xs text-slate-400">Winner of the 200m walking race!</p>
        </div>

        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-3 text-center">
            <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">🥈 2nd Place: Runner C</span>
            <div class="my-2 bg-slate-900/80 p-2 rounded border border-slate-700">
                <div class="text-base font-black text-white font-mono">2 min 18 sec</div>
                <div class="text-xs text-cyan-400 font-mono mt-1">138 Total Seconds (+4s)</div>
            </div>
            <p class="text-xs text-slate-400">Finished just 4 seconds behind Runner A.</p>
        </div>

        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-3 text-center">
            <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">🥉 3rd Place: Runner B</span>
            <div class="my-2 bg-slate-900/80 p-2 rounded border border-slate-700">
                <div class="text-base font-black text-white font-mono">2 min 22 sec</div>
                <div class="text-xs text-amber-400 font-mono mt-1">142 Total Seconds (+8s)</div>
            </div>
            <p class="text-xs text-slate-400">Finished 8 seconds behind the winner.</p>
        </div>
    </div>

    <div class="p-3 bg-slate-900/80 border border-slate-700 rounded-xl flex items-center justify-between text-xs">
        <span class="text-slate-400 font-semibold uppercase tracking-wider">Time Hierarchy:</span>
        <span class="text-amber-300 font-mono font-bold">1 Day = 24 Hours • 1 Hour = 60 Minutes • 1 Minute = 60 Seconds</span>
    </div>
</div>
""",
        "checkpoints": [
            {
                "id": "cp_5_1",
                "question": "By how many seconds did Runner A beat Runner B in the 200m walking race?",
                "options": [
                    "8 seconds (2 min 22 sec minus 2 min 14 sec)",
                    "4 seconds",
                    "12 seconds",
                    "2 seconds"
                ],
                "answer": 0,
                "explanation": "2 min 22 sec - 2 min 14 sec = 22 - 14 = 8 seconds.",
                "hint": "Subtract Runner A's 14 seconds from Runner B's 22 seconds."
            },
            {
                "id": "cp_5_2",
                "question": "Why is the second an essential unit of measurement in sports competitions?",
                "options": [
                    "Because events finish quickly and competitors differ by fractions or small counts of seconds",
                    "Because stopwatches cannot display minutes",
                    "Because runners are not allowed to run longer than one minute",
                    "Because seconds are larger than hours"
                ],
                "answer": 0,
                "explanation": "Seconds provide the high precision needed to separate fast race results where minutes are too coarse.",
                "hint": "Think about what happens if multiple athletes finish in the same minute."
            }
        ]
    },
    {
        "id": 6,
        "title": "Seconds Precision",
        "tagline": "The Fundamental Equivalence • 1 Minute = 60 Seconds and Sub-Minute Timing",
        "lecture": (
            "Now let us examine the fundamental mathematical equivalence that connects minutes and seconds: exactly sixty seconds make up "
            "one complete minute! When you look closely at a traditional analog clock face, you will notice a slender, swiftly sweeping hand "
            "that ticks continuously around the dial. This is the seconds hand. As this seconds hand sweeps past each of the sixty tiny hash marks "
            "along the circular clock perimeter, one second elapses with each audible tick. When the seconds hand completes one full 360-degree "
            "circuit around all sixty marks, the thicker minute hand clicks forward by exactly one minute mark! Therefore: 1 minute equals "
            "60 seconds. This beautiful ratio of sixty to one perfectly echoes the relationship between hours and minutes, where 1 hour equals "
            "60 minutes. Because 1 minute contains 60 seconds, 2 minutes equal 2 times 60, or 120 seconds; 3 minutes equal 3 times 60, or "
            "180 seconds; and half a minute equals half of 60, which is 30 seconds! Understanding that a minute comprises sixty distinct seconds "
            "allows us to transition smoothly between everyday timekeeping and high-precision scientific measurement, opening the door to calculating "
            "athletic race splits, musical rhythms, and technological processing speeds."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-amber-900/40 via-yellow-900/30 to-amber-900/40 border border-yellow-500/30 rounded-xl p-4">
        <h4 class="text-yellow-300 font-bold text-sm tracking-wider uppercase mb-1">Foundational Equivalence</h4>
        <div class="text-2xl font-black text-white font-mono my-2 text-center">
            1 Minute = 60 Seconds &nbsp;•&nbsp; 1/2 Minute = 30 Seconds
        </div>
        <p class="text-slate-200 text-xs text-center leading-relaxed">
            Every full 360° revolution of the slender seconds hand advances the minute hand by exactly 1 tick.
        </p>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs font-mono">
        <div class="bg-slate-800/80 p-3 rounded-xl border border-slate-700">
            <span class="text-slate-400">1 Minute</span>
            <div class="text-cyan-400 font-bold text-sm mt-1">60 Seconds</div>
            <span class="text-[10px] text-slate-500">1 × 60</span>
        </div>
        <div class="bg-slate-800/80 p-3 rounded-xl border border-slate-700">
            <span class="text-slate-400">2 Minutes</span>
            <div class="text-emerald-400 font-bold text-sm mt-1">120 Seconds</div>
            <span class="text-[10px] text-slate-500">2 × 60</span>
        </div>
        <div class="bg-slate-800/80 p-3 rounded-xl border border-slate-700">
            <span class="text-slate-400">3 Minutes</span>
            <div class="text-amber-400 font-bold text-sm mt-1">180 Seconds</div>
            <span class="text-[10px] text-slate-500">3 × 60</span>
        </div>
        <div class="bg-slate-800/80 p-3 rounded-xl border border-slate-700">
            <span class="text-slate-400">5 Minutes</span>
            <div class="text-rose-400 font-bold text-sm mt-1">300 Seconds</div>
            <span class="text-[10px] text-slate-500">5 × 60</span>
        </div>
    </div>

    <div class="p-3 bg-slate-900/80 border border-slate-700 rounded-xl flex items-center justify-between text-xs">
        <span class="text-slate-400 font-semibold uppercase tracking-wider">Clockwork Connection:</span>
        <span class="text-cyan-300">60 Seconds Hands Ticks = 1 Minute Hand Step = 1/60th Hour Hand Step</span>
    </div>
</div>
""",
        "checkpoints": [
            {
                "id": "cp_6_1",
                "question": "How many seconds are there in 4 complete minutes?",
                "options": [
                    "240 seconds (4 × 60 = 240)",
                    "100 seconds",
                    "400 seconds",
                    "180 seconds"
                ],
                "answer": 0,
                "explanation": "Since 1 minute = 60 seconds, 4 minutes = 4 × 60 = 240 seconds.",
                "hint": "Multiply 4 by 60."
            },
            {
                "id": "cp_6_2",
                "question": "How many seconds are in half of a minute (1/2 min)?",
                "options": [
                    "30 seconds (60 ÷ 2 = 30)",
                    "50 seconds",
                    "15 seconds",
                    "45 seconds"
                ],
                "answer": 0,
                "explanation": "Half of 60 seconds is 60 ÷ 2 = 30 seconds.",
                "hint": "Divide 60 seconds into two equal parts."
            }
        ]
    },
    {
        "id": 7,
        "title": "Unit Estimation",
        "tagline": "Sense of Time • Classifying Everyday Actions into Seconds or Minutes",
        "lecture": (
            "Developing an intuitive sense of time means knowing without a stopwatch whether an action takes seconds, minutes, or hours! "
            "Let us test our estimation skills on familiar daily activities. Think about blinking your eyelids or snapping your fingers: "
            "these happen in the blink of an eye, taking less than a single second! Switching on a classroom light, dropping an eraser to the floor, "
            "or swallowing a sip of water also take only a few brief seconds. Counting out loud from 1 to 20 at a steady pace takes about "
            "10 to 15 seconds. Filling a drinking glass with water from a kitchen tap takes roughly 5 to 8 seconds. "
            "All of these are rapid events that we measure in seconds. "
            "On the other hand, activities that involve multiple steps require minutes! Tying your shoelaces, eating a bowl of hot cereal, "
            "making a thoughtful phone call to a friend, or brushing your teeth carefully all take several minutes. "
            "Learning to match the appropriate unit to each activity is a vital life skill: if you tell someone you will return in a second, "
            "you mean instantly; if you say a few minutes, you mean a short, relaxed wait!"
        ),
        "content_html": """
<div class="space-y-4">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <!-- Seconds Category -->
        <div class="bg-gradient-to-br from-cyan-950/60 to-slate-900 border border-cyan-500/40 rounded-xl p-4">
            <div class="flex items-center justify-between mb-2">
                <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Fast Events (Seconds)</span>
                <span class="text-xs bg-cyan-500/20 text-cyan-300 px-2 py-0.5 rounded font-mono">< 60 sec</span>
            </div>
            <ul class="text-xs text-slate-300 space-y-2 mt-2">
                <li class="flex items-center gap-2"><span>👀</span> Blinking your eyes (~0.3 sec)</li>
                <li class="flex items-center gap-2"><span>💡</span> Flipping a light switch (~1 sec)</li>
                <li class="flex items-center gap-2"><span>🫰</span> Snapping fingers (~0.5 sec)</li>
                <li class="flex items-center gap-2"><span>🔢</span> Counting numbers 1 to 20 (~15 sec)</li>
                <li class="flex items-center gap-2"><span>💧</span> Filling a glass of water (~6 sec)</li>
            </ul>
        </div>

        <!-- Minutes Category -->
        <div class="bg-gradient-to-br from-amber-950/60 to-slate-900 border border-amber-500/40 rounded-xl p-4">
            <div class="flex items-center justify-between mb-2">
                <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Extended Events (Minutes)</span>
                <span class="text-xs bg-amber-500/20 text-amber-300 px-2 py-0.5 rounded font-mono">1 to 60 min</span>
            </div>
            <ul class="text-xs text-slate-300 space-y-2 mt-2">
                <li class="flex items-center gap-2"><span>🪥</span> Brushing teeth thoroughly (~2 to 3 min)</li>
                <li class="flex items-center gap-2"><span>👟</span> Tying shoelaces neatly (~1 to 2 min)</li>
                <li class="flex items-center gap-2"><span>📞</span> Calling a grandparent (~5 to 10 min)</li>
                <li class="flex items-center gap-2"><span>🍲</span> Eating lunch or dinner (~15 to 25 min)</li>
                <li class="flex items-center gap-2"><span>🚿</span> Taking a refreshing bath (~10 to 15 min)</li>
            </ul>
        </div>
    </div>

    <div class="p-3 bg-slate-900/80 border border-slate-700 rounded-xl flex items-center justify-between text-xs">
        <span class="text-slate-400 font-semibold uppercase tracking-wider">Estimation Guideline:</span>
        <span class="text-indigo-300">If it happens almost instantly or in one breath, measure in <strong>seconds</strong>!</span>
    </div>
</div>
""",
        "checkpoints": [
            {
                "id": "cp_7_1",
                "question": "Which of the following actions is best measured in seconds rather than minutes?",
                "options": [
                    "Snapping your fingers or clapping once",
                    "Baking a chocolate cake in an oven",
                    "Walking 1 kilometre to the school gate",
                    "Watching an educational cartoon episode"
                ],
                "answer": 0,
                "explanation": "Snapping your fingers takes less than a single second. Walking, baking, and watching cartoons take many minutes.",
                "hint": "Identify which activity happens in a single split second."
            },
            {
                "id": "cp_7_2",
                "question": "Which unit of time would you choose to measure the time taken to boil a pot of potatoes?",
                "options": [
                    "Minutes (approx. 15 to 20 minutes)",
                    "Seconds (potatoes cook instantly)",
                    "Days (potatoes take days to boil)",
                    "Months"
                ],
                "answer": 0,
                "explanation": "Boiling potatoes takes about 15 to 20 minutes, making minutes the appropriate standard unit.",
                "hint": "Cooking a vegetable dish takes multiple minutes on a kitchen stove."
            }
        ]
    },
    {
        "id": 8,
        "title": "One-Minute Challenges",
        "tagline": "Classroom Activity Verification • Estimating vs Counting Physical Feats in 60 Seconds",
        "lecture": (
            "How much can you truly accomplish in exactly one minute? Sixty seconds might feel very brief when you are enjoying a fun video, "
            "yet it feels remarkably long and challenging when you are performing intense physical exercise! In our mathematics class, students "
            "conducted an exciting series of one-minute verification challenges to test their personal estimation accuracy. Before starting each "
            "challenge, students carefully wrote down an estimate of how many repetitions they believed they could achieve in 60 seconds. "
            "Then, with a classmate holding a digital stopwatch, they performed the activity and recorded their actual verified counts! "
            "For instance, students estimated how many times they could blow up and tie a balloon: typical estimates were 5 balloons, while actual "
            "verified counts averaged 2 to 3 balloons. For physical floor push-ups, estimates ranged from 20 to 30, with actual counts around "
            "15 to 22 repetitions. For natural breathing cycles, students discovered a relaxed human body takes about 16 to 20 breaths per minute. "
            "And for hopping on one leg, students sustained an impressive 60 to 85 continuous hops! Comparing pre-activity estimates with verified "
            "stopwatch measurements trains our minds to perceive the true physical duration of sixty seconds with confidence."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-teal-900/40 via-emerald-900/30 to-teal-900/40 border border-teal-500/30 rounded-xl p-4">
        <h4 class="text-teal-300 font-bold text-sm tracking-wider uppercase mb-1">Stopwatch Verification Lab</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Record pre-challenge estimates, start the 60-second timer, and discover your real physical performance!
        </p>
    </div>

    <div class="overflow-hidden border border-slate-700 rounded-xl bg-slate-900/80">
        <table class="w-full text-xs text-left text-slate-300">
            <thead class="bg-slate-800 text-slate-200 font-semibold uppercase tracking-wider">
                <tr>
                    <th class="p-3">Activity (in 60 Seconds)</th>
                    <th class="p-3">Estimated Reps</th>
                    <th class="p-3">Actual Verified Count</th>
                    <th class="p-3">Scientific Observation</th>
                </tr>
            </thead>
            <tbody class="divide-y divide-slate-800 font-mono">
                <tr class="hover:bg-slate-800/40">
                    <td class="p-3 text-white font-bold">🎈 Balloons Blown & Tied</td>
                    <td class="p-3 text-slate-400">5 balloons</td>
                    <td class="p-3 text-amber-300 font-bold">2 to 3 balloons</td>
                    <td class="p-3 text-slate-400">Tying knots requires delicate fine motor time</td>
                </tr>
                <tr class="hover:bg-slate-800/40">
                    <td class="p-3 text-white font-bold">💪 Floor Push-Ups</td>
                    <td class="p-3 text-slate-400">30 push-ups</td>
                    <td class="p-3 text-cyan-300 font-bold">15 to 22 reps</td>
                    <td class="p-3 text-slate-400">Muscular fatigue slows repetition pace</td>
                </tr>
                <tr class="hover:bg-slate-800/40">
                    <td class="p-3 text-white font-bold">🫁 Natural Breaths Taken</td>
                    <td class="p-3 text-slate-400">30 breaths</td>
                    <td class="p-3 text-emerald-300 font-bold">16 to 20 breaths</td>
                    <td class="p-3 text-slate-400">Healthy resting respiratory rhythm</td>
                </tr>
                <tr class="hover:bg-slate-800/40">
                    <td class="p-3 text-white font-bold">🦿 One-Leg Hops</td>
                    <td class="p-3 text-slate-400">50 hops</td>
                    <td class="p-3 text-indigo-300 font-bold">60 to 85 hops</td>
                    <td class="p-3 text-slate-400">Exceeds estimate due to rapid spring rhythm</td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="p-3 bg-slate-900/80 border border-slate-700 rounded-xl flex items-center justify-between text-xs">
        <span class="text-slate-400 font-semibold uppercase tracking-wider">Estimation Insight:</span>
        <span class="text-emerald-300">Repeated measurement bridges intuitive guessing and empirical scientific reality!</span>
    </div>
</div>
""",
        "checkpoints": [
            {
                "id": "cp_8_1",
                "question": "A healthy child at rest takes approximately how many normal breaths in 1 minute (60 seconds)?",
                "options": [
                    "About 16 to 20 breaths",
                    "Over 100 breaths",
                    "Exactly 1 breath",
                    "60 breaths (one every single second)"
                ],
                "answer": 0,
                "explanation": "A normal resting breathing rate for children is about 16 to 20 breaths per minute.",
                "hint": "Count how many times your chest rises and falls in 10 seconds, then multiply by 6."
            },
            {
                "id": "cp_8_2",
                "question": "If you can hop 20 times in 15 seconds, approximately how many hops can you achieve in 1 full minute at that same pace?",
                "options": [
                    "80 hops (20 × 4 = 80, since 60 ÷ 15 = 4)",
                    "40 hops",
                    "35 hops",
                    "100 hops"
                ],
                "answer": 0,
                "explanation": "60 seconds contains 4 blocks of 15 seconds. 20 hops × 4 = 80 hops.",
                "hint": "There are four 15-second intervals in one 60-second minute."
            }
        ]
    }
]
