# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 12: Racing Seconds
Part 2 Data: Slides 9 to 16
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Short Durations",
        "tagline": "Micro-Interval Measurements • Timing Rope Skipping, Writing Words, and 100m Sprints",
        "lecture": (
            "While one full minute provides ample time for substantial physical activities, many fascinating everyday events occur in brief "
            "sub-minute fractions of a minute! To explore these lightning-fast intervals with scientific rigor, class five students used "
            "high-precision digital stopwatches to time three distinct short-duration tasks. First, students engaged in an exciting 10-second "
            "rapid rope-skipping challenge: how many clean rope skips can you complete in just 10 seconds? Most students achieved between "
            "15 and 22 brisk skips! Second, students carefully timed how long it takes to write the 6-letter English word 'FRIEND' in neat "
            "cursive handwriting on paper. Stopwatch trials revealed that writing 'FRIEND' carefully takes between 4 and 7 seconds, whereas "
            "scribbling it hurriedly takes about 2 to 3 seconds. Third, students ventured out to the school athletics track for a high-speed "
            "100-metre sprint. While elite Olympic sprinters complete 100 metres in under 10 seconds, enthusiastic fifth-grade school sprinters "
            "crossed the finish line in 16 to 22 seconds! These experiments highlight the vital importance of measuring in seconds: if we only "
            "had whole minutes, a quick 10-second rope skip and a swift 20-second sprint would both be rounded down to zero, completely erasing our actual physical achievements and athletic records!"
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-blue-900/40 via-indigo-900/30 to-blue-900/40 border border-blue-500/30 rounded-xl p-4">
        <h4 class="text-blue-300 font-bold text-sm tracking-wider uppercase mb-1">Sub-Minute Stopwatch Lab</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Short-duration activities that conclude in less than 60 seconds require precise second timing to distinguish performance.
        </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-3 text-center">
            <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">🪢 10-Second Rope Skip</span>
            <div class="my-2 bg-slate-900/80 p-2 rounded border border-slate-700">
                <div class="text-base font-black text-white font-mono">15 to 22 Skips</div>
                <div class="text-xs text-cyan-400 font-mono mt-1">Duration: Exactly 10s</div>
            </div>
            <p class="text-xs text-slate-400">Tests rapid coordination and foot speed.</p>
        </div>

        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-3 text-center">
            <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">✍️ Writing "FRIEND"</span>
            <div class="my-2 bg-slate-900/80 p-2 rounded border border-slate-700">
                <div class="text-base font-black text-white font-mono">4 to 7 Seconds</div>
                <div class="text-xs text-amber-400 font-mono mt-1">6-Letter Word Writing</div>
            </div>
            <p class="text-xs text-slate-400">Measures fine motor handwriting speed.</p>
        </div>

        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-3 text-center">
            <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">🏃 100m School Sprint</span>
            <div class="my-2 bg-slate-900/80 p-2 rounded border border-slate-700">
                <div class="text-base font-black text-white font-mono">16 to 22 Seconds</div>
                <div class="text-xs text-emerald-400 font-mono mt-1">Athletic Track Sprint</div>
            </div>
            <p class="text-xs text-slate-400">Class 5 sprint timing on standard track.</p>
        </div>
    </div>

    <div class="p-3 bg-slate-900/80 border border-slate-700 rounded-xl flex items-center justify-between text-xs">
        <span class="text-slate-400 font-semibold uppercase tracking-wider">Fraction of a Minute:</span>
        <span class="text-amber-300 font-mono">10 sec = 1/6th min • 15 sec = 1/4th min • 30 sec = 1/2 min</span>
    </div>
</div>
""",
        "checkpoints": [
            {
                "id": "cp_9_1",
                "question": "If a student completes 18 skips in 10 seconds, what fraction of a full minute did the skipping challenge last?",
                "options": [
                    "One-sixth of a minute (10/60 = 1/6)",
                    "Half of a minute (1/2)",
                    "One-tenth of a minute (1/10)",
                    "One-fourth of a minute (1/4)"
                ],
                "answer": 0,
                "explanation": "10 seconds out of 60 seconds is 10/60 = 1/6th of a minute.",
                "hint": "Divide 10 seconds by 60 seconds."
            },
            {
                "id": "cp_9_2",
                "question": "If writing the word 'FRIEND' takes 5 seconds, how many times can it be written in 1 full minute at the same steady speed?",
                "options": [
                    "12 times (60 ÷ 5 = 12)",
                    "10 times",
                    "6 times",
                    "20 times"
                ],
                "answer": 0,
                "explanation": "60 seconds in a minute divided by 5 seconds per word = 12 times.",
                "hint": "Divide 60 by 5."
            }
        ]
    },
    {
        "id": 10,
        "title": "Reading Seconds Hand",
        "tagline": "Analog Dial Inspection • Tracking Seconds Hand Movement Across Starting and Ending Clocks",
        "lecture": (
            "Reading an analog clock's slender seconds hand is a wonderful geometric skill that transforms angular clock positions into exact "
            "counts of seconds. On a circular clock face, each major number from 1 to 12 represents a 5-second interval. "
            "When the seconds hand moves from the 12 to the 1, five seconds have passed. When it sweeps from the 12 to the 4, four times five "
            "equals twenty seconds! In our daily lives, many domestic chores take just a handful of seconds. "
            "Consider examining a pair of analog clocks: on clock A, the seconds hand points straight up at 12 when getting out of bed. "
            "On clock B, when walking into the kitchen, the seconds hand points at 4. The elapsed time is 4 times 5, or 20 seconds! "
            "Next, bending down to pick up a fallen paper: the hand starts at 2 (10 seconds) and ends at 5 (25 seconds). "
            "Subtracting 10 from 25 gives exactly 15 seconds! Finally, washing a spoon and plate at the kitchen sink: the hand starts at 12 "
            "and travels all the way to 7 (35 seconds), taking 35 seconds. By counting the 5-second gaps between clock numerals, you can "
            "calculate elapsed seconds instantly without ever needing a digital display."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-purple-900/40 via-indigo-900/30 to-purple-900/40 border border-purple-500/30 rounded-xl p-4">
        <h4 class="text-purple-300 font-bold text-sm tracking-wider uppercase mb-1">Clock Seconds Geometry</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Each numeral gap on the clock dial represents <span class="text-amber-300 font-bold">5 seconds</span> (30° angle).
            Multiply number steps by 5 to find elapsed seconds!
        </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-3">
            <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">🛏️ Walking to Kitchen</span>
            <div class="mt-2 text-xs text-slate-300 font-mono bg-slate-900/80 p-2.5 rounded border border-slate-700 space-y-1">
                <div>Start Hand: at 12 (0s)</div>
                <div>End Hand: at 4 (20s)</div>
                <div class="text-cyan-300 font-bold text-sm">Elapsed = 20 seconds</div>
            </div>
            <p class="text-xs text-slate-400 mt-2">4 steps × 5 sec = 20s.</p>
        </div>

        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-3">
            <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">📄 Picking Up Paper</span>
            <div class="mt-2 text-xs text-slate-300 font-mono bg-slate-900/80 p-2.5 rounded border border-slate-700 space-y-1">
                <div>Start Hand: at 2 (10s)</div>
                <div>End Hand: at 5 (25s)</div>
                <div class="text-amber-300 font-bold text-sm">Elapsed = 15 seconds</div>
            </div>
            <p class="text-xs text-slate-400 mt-2">3 steps × 5 sec = 15s.</p>
        </div>

        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-3">
            <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">🍽️ Washing Spoon & Plate</span>
            <div class="mt-2 text-xs text-slate-300 font-mono bg-slate-900/80 p-2.5 rounded border border-slate-700 space-y-1">
                <div>Start Hand: at 12 (0s)</div>
                <div>End Hand: at 7 (35s)</div>
                <div class="text-emerald-300 font-bold text-sm">Elapsed = 35 seconds</div>
            </div>
            <p class="text-xs text-slate-400 mt-2">7 steps × 5 sec = 35s.</p>
        </div>
    </div>

    <div class="p-3 bg-slate-900/80 border border-slate-700 rounded-xl flex items-center justify-between text-xs">
        <span class="text-slate-400 font-semibold uppercase tracking-wider">Quick Calculation Rule:</span>
        <span class="text-cyan-300 font-mono">Elapsed Seconds = (End Numeral − Start Numeral) × 5</span>
    </div>
</div>
""",
        "checkpoints": [
            {
                "id": "cp_10_1",
                "question": "On an analog clock, the seconds hand moves from the numeral 3 to the numeral 9. How many seconds have elapsed?",
                "options": [
                    "30 seconds ((9 - 3) × 5 = 6 × 5 = 30)",
                    "6 seconds",
                    "45 seconds",
                    "15 seconds"
                ],
                "answer": 0,
                "explanation": "From 3 to 9 is 6 numbers. Each number is 5 seconds: 6 × 5 = 30 seconds (half a minute!).",
                "hint": "Count the number steps from 3 to 9, then multiply by 5."
            },
            {
                "id": "cp_10_2",
                "question": "If the seconds hand starts at 12 and takes 45 seconds to perform a task, which clock numeral will it point to?",
                "options": [
                    "Numeral 9 (since 45 ÷ 5 = 9)",
                    "Numeral 8",
                    "Numeral 10",
                    "Numeral 6"
                ],
                "answer": 0,
                "explanation": "45 seconds divided by 5 seconds per numeral = numeral 9 (three-quarters of a turn).",
                "hint": "Divide 45 by 5."
            }
        ]
    },
    {
        "id": 11,
        "title": "Drawing Seconds Hand",
        "tagline": "Clock Construction • Drawing Final Seconds Hand Positions for Specified Durations",
        "lecture": (
            "Once you can read the seconds hand, the next delightful challenge is drawing where the hand should point after a given duration "
            "has elapsed! To draw the seconds hand accurately on an analog clock face, we use simple division by five. Because each major clock "
            "number mark accounts for five seconds, dividing the target elapsed seconds by 5 reveals the exact number of clock positions to "
            "advance clockwise. Let us practice four common scenarios starting from the top 12 o'clock position (0 seconds). "
            "First, to show an elapsed duration of 20 seconds: divide 20 by 5, which equals 4; draw the slender red seconds hand pointing "
            "directly at numeral 4! Second, for an elapsed time of 30 seconds: divide 30 by 5, which equals 6; draw the hand pointing straight down "
            "at numeral 6, representing half a minute. Third, for 40 seconds: divide 40 by 5, which equals 8; draw the hand pointing at numeral 8! "
            "Finally, for a complete duration of 60 seconds: the hand travels around all sixty marks and completes one full 360-degree rotation, "
            "returning to point straight up at numeral 12 once more! Mastering these four key benchmark positions turns clock drawing into second nature."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-emerald-900/40 via-teal-900/30 to-emerald-900/40 border border-emerald-500/30 rounded-xl p-4">
        <h4 class="text-emerald-300 font-bold text-sm tracking-wider uppercase mb-1">Clock Hand Drawing Rule</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Starting from 12 (0s):
            <span class="text-amber-300 font-bold">Target Clock Numeral = Elapsed Seconds ÷ 5</span>.
        </p>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs font-mono">
        <div class="bg-slate-800/80 p-3 rounded-xl border border-slate-700">
            <span class="text-slate-400">20 Seconds</span>
            <div class="text-cyan-400 font-bold text-base mt-1">Points at 4</div>
            <span class="text-[10px] text-slate-500">20 ÷ 5 = 4</span>
        </div>
        <div class="bg-slate-800/80 p-3 rounded-xl border border-slate-700">
            <span class="text-slate-400">30 Seconds</span>
            <div class="text-emerald-400 font-bold text-base mt-1">Points at 6</div>
            <span class="text-[10px] text-slate-500">30 ÷ 5 = 6 (1/2 Turn)</span>
        </div>
        <div class="bg-slate-800/80 p-3 rounded-xl border border-slate-700">
            <span class="text-slate-400">40 Seconds</span>
            <div class="text-amber-400 font-bold text-base mt-1">Points at 8</div>
            <span class="text-[10px] text-slate-500">40 ÷ 5 = 8</span>
        </div>
        <div class="bg-slate-800/80 p-3 rounded-xl border border-slate-700">
            <span class="text-slate-400">60 Seconds</span>
            <div class="text-rose-400 font-bold text-base mt-1">Points at 12</div>
            <span class="text-[10px] text-slate-500">Full 360° Circuit</span>
        </div>
    </div>

    <div class="p-3 bg-slate-900/80 border border-slate-700 rounded-xl flex items-center justify-between text-xs">
        <span class="text-slate-400 font-semibold uppercase tracking-wider">Clock Angle Check:</span>
        <span class="text-cyan-300">Each second = 6° • Each 5-sec mark = 30° • 60 seconds = 360°</span>
    </div>
</div>
""",
        "checkpoints": [
            {
                "id": "cp_11_1",
                "question": "If the seconds hand starts at 12 and moves forward for 35 seconds, which clock numeral should you draw it pointing to?",
                "options": [
                    "Numeral 7 (35 ÷ 5 = 7)",
                    "Numeral 6",
                    "Numeral 8",
                    "Numeral 5"
                ],
                "answer": 0,
                "explanation": "35 seconds divided by 5 seconds per numeral = numeral 7.",
                "hint": "Divide 35 by 5."
            },
            {
                "id": "cp_11_2",
                "question": "If the seconds hand starts at numeral 4 (20s) and advances for 25 seconds, which numeral does it land on?",
                "options": [
                    "Numeral 9 (20s + 25s = 45s, and 45 ÷ 5 = 9)",
                    "Numeral 8",
                    "Numeral 7",
                    "Numeral 10"
                ],
                "answer": 0,
                "explanation": "Starting at 20s + 25s = 45s. 45 ÷ 5 = numeral 9 (or advance 4 + 5 = 9).",
                "hint": "Add 25 seconds to the starting 20 seconds, then divide by 5."
            }
        ]
    },
    {
        "id": 12,
        "title": "Hours To Minutes",
        "tagline": "Unit Conversions • Multiplying by 60 for Hours-to-Minutes and Dividing for Minutes-to-Hours",
        "lecture": (
            "Time measurement across human civilization relies on a fascinating sexagesimal base-sixty system inherited directly from ancient Mesopotamian astronomers and historical mathematicians. "
            "Because there are exactly sixty minutes in one single hour, converting between hours and minutes involves straightforward multiplication "
            "and division by sixty! To convert hours into minutes, we multiply the number of hours by 60. For example, a 2-hour cinema movie "
            "duration equals 2 times 60, which is 120 minutes. If an event has both hours and minutes, such as a cricket match pause of 1 hour "
            "and 10 minutes, we first convert the hour portion: 1 times 60 is 60 minutes, then add the extra 10 minutes, yielding 70 minutes in "
            "total! Conversely, to convert a large quantity of minutes into hours and minutes, we divide by 60. "
            "Consider a long interstate bus trip lasting 220 minutes: dividing 220 by 60 gives a quotient of 3 with a remainder of 40. "
            "This means 220 minutes equals 3 hours and 40 minutes! Always verify your answer: 3 hours times 60 is 180 minutes, plus 40 minutes "
            "equals 220 minutes! Mastering this two-way conversion enables you to interpret flight durations, study timetables, and train schedules "
            "with flawless mathematical precision."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <!-- Hours to Minutes Card -->
        <div class="bg-gradient-to-br from-indigo-950/60 to-slate-900 border border-indigo-500/40 rounded-xl p-4">
            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">Hours ➔ Minutes</span>
            <h4 class="text-white font-extrabold text-base mt-1">Multiply by 60</h4>
            <div class="my-2 p-2 bg-slate-950/80 rounded border border-indigo-500/30 font-mono text-xs text-amber-300 font-bold">
                Total Min = (Hours × 60) + Extra Min
            </div>
            <p class="text-xs text-slate-300 mt-2 leading-relaxed">
                Example: 1 hr 10 min = (1 × 60) + 10 = <strong class="text-white">70 min</strong>.
            </p>
        </div>

        <!-- Minutes to Hours Card -->
        <div class="bg-gradient-to-br from-teal-950/60 to-slate-900 border border-teal-500/40 rounded-xl p-4">
            <span class="text-xs font-bold text-teal-400 uppercase tracking-wider">Minutes ➔ Hours</span>
            <h4 class="text-white font-extrabold text-base mt-1">Divide by 60</h4>
            <div class="my-2 p-2 bg-slate-950/80 rounded border border-teal-500/30 font-mono text-xs text-emerald-300 font-bold">
                Hours = Min ÷ 60 (Quotient = hr, Remainder = min)
            </div>
            <p class="text-xs text-slate-300 mt-2 leading-relaxed">
                Example: 220 min = 220 ÷ 60 = <strong class="text-white">3 hr 40 min</strong> (180 + 40).
            </p>
        </div>
    </div>

    <!-- Quick Reference Conversion Chart -->
    <div class="bg-slate-900/80 border border-slate-700 rounded-xl p-3">
        <h5 class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-2">Multiples of 60 Reference</h5>
        <div class="grid grid-cols-2 sm:grid-cols-5 gap-2 text-center text-xs font-mono">
            <div class="bg-slate-800 p-2 rounded">
                <div class="text-slate-400">1 Hour</div>
                <div class="text-cyan-400 font-bold mt-1">60 min</div>
            </div>
            <div class="bg-slate-800 p-2 rounded">
                <div class="text-slate-400">2 Hours</div>
                <div class="text-cyan-400 font-bold mt-1">120 min</div>
            </div>
            <div class="bg-slate-800 p-2 rounded">
                <div class="text-slate-400">3 Hours</div>
                <div class="text-cyan-400 font-bold mt-1">180 min</div>
            </div>
            <div class="bg-slate-800 p-2 rounded">
                <div class="text-slate-400">4 Hours</div>
                <div class="text-cyan-400 font-bold mt-1">240 min</div>
            </div>
            <div class="bg-slate-800 p-2 rounded">
                <div class="text-slate-400">5 Hours</div>
                <div class="text-cyan-400 font-bold mt-1">300 min</div>
            </div>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "id": "cp_12_1",
                "question": "How many total minutes are in 2 hours and 25 minutes?",
                "options": [
                    "145 minutes ((2 × 60) + 25 = 120 + 25 = 145)",
                    "125 minutes",
                    "85 minutes",
                    "225 minutes"
                ],
                "answer": 0,
                "explanation": "2 hours = 2 × 60 = 120 minutes. 120 + 25 = 145 minutes.",
                "hint": "Convert the 2 hours into 120 minutes first, then add 25."
            },
            {
                "id": "cp_12_2",
                "question": "A flight duration is listed as 190 minutes. What is this expressed in hours and minutes?",
                "options": [
                    "3 hours 10 minutes (180 min + 10 min)",
                    "2 hours 30 minutes",
                    "3 hours 30 minutes",
                    "1 hour 90 minutes"
                ],
                "answer": 0,
                "explanation": "190 ÷ 60 = 3 with a remainder of 10. 3 × 60 = 180 min, so 190 min = 3 hr 10 min.",
                "hint": "Find the largest multiple of 60 less than 190 (which is 180 = 3 hours)."
            }
        ]
    },
    {
        "id": 13,
        "title": "Double Number Lines",
        "tagline": "Visual Dual Scale • Mapping Hours and Minutes Side-by-Side on Parallel Axes",
        "lecture": (
            "Double number lines provide a crystal-clear visual map that makes unit conversion intuitive, transparent, and completely memorable! "
            "Imagine drawing two straight parallel number lines stacked directly on top of each other. "
            "On the upper number line, we mark time in whole hours: 0, 1, 2, 3, 4, and 5 hours. "
            "On the lower number line, directly below each hour mark, we place its exact numerical equivalent in minutes: 0, 60, 120, 180, 240, "
            "and 300 minutes! Because both scales are perfectly aligned proportionally along the visual grid, finding accurate unit conversions is as simple as sliding a transparent vertical "
            "ruler directly along the lines. Want to know what 2 and a half hours equals in minutes? Look midway between 2 hours and 3 hours on the top "
            "line; look straight down to the bottom line, halfway between 120 and 180, and you instantly read 150 minutes! "
            "What about converting 70 minutes? On the bottom line, 70 is located 10 minutes past the 60 mark; looking upward, it aligns with "
            "1 hour and 10 minutes! Double number lines eliminate abstract guesswork by showing how continuous quantities in two different "
            "measurement systems correspond with absolute proportional symmetry across every single point."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-amber-900/40 via-yellow-900/30 to-amber-900/40 border border-yellow-500/30 rounded-xl p-4">
        <h4 class="text-yellow-300 font-bold text-sm tracking-wider uppercase mb-1">Double Number Line Model</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            Parallel proportional scales align hours directly above their equivalent minute counts:
            <span class="text-amber-300 font-bold">1 hr ↔ 60 min, 2 hr ↔ 120 min, 3 hr ↔ 180 min</span>.
        </p>
    </div>

    <!-- Interactive Visual Representation -->
    <div class="p-4 bg-slate-900/80 border border-slate-700 rounded-xl font-mono text-xs">
        <div class="flex justify-between text-cyan-400 font-bold mb-1 border-b border-cyan-500/30 pb-1">
            <span>Hours (Top Axis):</span>
            <span>0 hr &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1 hr &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2 hr &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3 hr &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4 hr</span>
        </div>
        <div class="flex justify-between text-amber-400 font-bold mt-2 border-t border-amber-500/30 pt-1">
            <span>Minutes (Bottom Axis):</span>
            <span>0 min &nbsp;&nbsp;&nbsp; 60 min &nbsp;&nbsp;&nbsp; 120 min &nbsp;&nbsp;&nbsp; 180 min &nbsp;&nbsp;&nbsp; 240 min</span>
        </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
        <div class="p-3 bg-slate-800/80 rounded-xl border border-slate-700">
            <span class="text-cyan-400 font-bold block mb-1">Reading 2 hr 30 min:</span>
            <p class="text-slate-300">Look between 2 hr and 3 hr ➔ Bottom scale reads 120 + 30 = <strong>150 min</strong>.</p>
        </div>
        <div class="p-3 bg-slate-800/80 rounded-xl border border-slate-700">
            <span class="text-amber-400 font-bold block mb-1">Reading 70 minutes:</span>
            <p class="text-slate-300">10 units past 60 min ➔ Top scale reads <strong>1 hr 10 min</strong>.</p>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "id": "cp_13_1",
                "question": "Using a double number line, what minute value aligns directly underneath 3 hours and 30 minutes?",
                "options": [
                    "210 minutes (180 + 30 = 210)",
                    "190 minutes",
                    "330 minutes",
                    "240 minutes"
                ],
                "answer": 0,
                "explanation": "Under 3 hours is 180 min. Halfway to 4 hours adds 30 min: 180 + 30 = 210 minutes.",
                "hint": "3 hours is 180 minutes, then add 30 minutes."
            },
            {
                "id": "cp_13_2",
                "question": "Which point on the upper hour line corresponds to 300 minutes on the lower line?",
                "options": [
                    "5 hours (300 ÷ 60 = 5)",
                    "4 hours 30 minutes",
                    "6 hours",
                    "5 hours 30 minutes"
                ],
                "answer": 0,
                "explanation": "300 minutes divided by 60 minutes per hour = 5 hours exactly.",
                "hint": "Divide 300 by 60."
            }
        ]
    },
    {
        "id": 14,
        "title": "Minutes To Seconds",
        "tagline": "Minute-Second Scaling • Converting 320 Seconds and Double Number Lines for Sub-Hour Units",
        "lecture": (
            "Just as we mapped hours and minutes on parallel axes, we can construct an identical double number line for minutes and seconds! "
            "On the top horizontal line, we mark minutes: 0, 1, 2, 3, 4, 5, and 6 minutes. "
            "On the bottom line, directly below each minute mark, we record its exact value in seconds: 0, 60, 120, 180, 240, 300, and 360 seconds! "
            "This visual tool makes solving tricky minute-and-second word problems effortless and engaging. "
            "Consider a school swimming championship race where a swimmer's time is recorded as 320 seconds. How many minutes and seconds did "
            "the swimmer take? Look at the bottom seconds scale: 320 lies between 300 seconds (5 minutes) and 360 seconds (6 minutes). "
            "Subtracting 300 from 320 leaves 20 extra seconds! Therefore, 320 seconds equals exactly 5 minutes and 20 seconds! "
            "Now consider the reverse problem: a space rocket launch countdown is set for 10 minutes and 13 seconds. What is this in total "
            "seconds? Multiply the 10 minutes by 60 to get 600 seconds, then add the 13 extra seconds to reach 613 seconds! "
            "Whether calculating marathon splits, cooking soft-boiled eggs, or programming computer animations, minute-to-second fluency ensures "
            "complete mastery over high-precision time."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-teal-900/40 via-cyan-900/30 to-teal-900/40 border border-teal-500/30 rounded-xl p-4">
        <h4 class="text-teal-300 font-bold text-sm tracking-wider uppercase mb-1">Minutes & Seconds Double Scale</h4>
        <div class="text-lg font-black text-white font-mono my-2 text-center">
            320 Seconds = 5 Minutes 20 Seconds &nbsp;•&nbsp; 10 min 13 sec = 613 Seconds
        </div>
    </div>

    <!-- Parallel Line Visualization -->
    <div class="p-4 bg-slate-900/80 border border-slate-700 rounded-xl font-mono text-xs">
        <div class="flex justify-between text-teal-400 font-bold mb-1 border-b border-teal-500/30 pb-1">
            <span>Minutes (Top Axis):</span>
            <span>0m &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1m &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2m &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3m &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4m &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 5m &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 6m</span>
        </div>
        <div class="flex justify-between text-cyan-400 font-bold mt-2 border-t border-cyan-500/30 pt-1">
            <span>Seconds (Bottom Axis):</span>
            <span>0s &nbsp;&nbsp;&nbsp;&nbsp; 60s &nbsp;&nbsp;&nbsp; 120s &nbsp;&nbsp;&nbsp; 180s &nbsp;&nbsp;&nbsp; 240s &nbsp;&nbsp;&nbsp; 300s &nbsp;&nbsp;&nbsp; 360s</span>
        </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
        <div class="p-3 bg-slate-800/80 rounded-xl border border-slate-700">
            <span class="text-amber-400 font-bold block mb-1">Conversion: 320 Seconds</span>
            <p class="text-slate-300 font-mono">320 ÷ 60 = 5 with remainder 20 ➔ <strong>5 min 20 sec</strong>.</p>
        </div>
        <div class="p-3 bg-slate-800/80 rounded-xl border border-slate-700">
            <span class="text-cyan-400 font-bold block mb-1">Conversion: 10 min 13 sec</span>
            <p class="text-slate-300 font-mono">(10 × 60) + 13 = 600 + 13 = <strong>613 seconds</strong>.</p>
        </div>
    </div>
</div>
""",
        "checkpoints": [
            {
                "id": "cp_14_1",
                "question": "How many minutes and seconds are in 250 seconds?",
                "options": [
                    "4 minutes 10 seconds (240s + 10s)",
                    "3 minutes 50 seconds",
                    "4 minutes 50 seconds",
                    "5 minutes 10 seconds"
                ],
                "answer": 0,
                "explanation": "250 ÷ 60 = 4 with remainder 10. 4 × 60 = 240 seconds, so 250s = 4 min 10 sec.",
                "hint": "The largest multiple of 60 less than 250 is 240 (4 minutes)."
            },
            {
                "id": "cp_14_2",
                "question": "A microwave popcorn cycle takes 2 minutes and 45 seconds. How many total seconds is this?",
                "options": [
                    "165 seconds ((2 × 60) + 45 = 120 + 45 = 165)",
                    "145 seconds",
                    "245 seconds",
                    "105 seconds"
                ],
                "answer": 0,
                "explanation": "2 minutes = 2 × 60 = 120 seconds. 120 + 45 = 165 seconds.",
                "hint": "Convert 2 minutes to 120 seconds, then add 45."
            }
        ]
    },
    {
        "id": 15,
        "title": "Elapsed Word Problems",
        "tagline": "Practical Story Scenarios • Study Schedules, Travel Times, and School Picnic Itineraries",
        "lecture": (
            "Mathematics truly shines when we apply our time skills to solve real-world story scenarios that happen in our everyday lives! "
            "Consider a diligent student who sits down at a study desk to work on mathematics at 04:15 p.m. and finishes homework at 05:40 p.m. "
            "How long did the student study? Jump from 04:15 to 05:15, which is 1 full hour. Then jump forward from 05:15 to 05:40, which is 25 minutes. "
            "The student studied for 1 hour and 25 minutes! "
            "Now consider an exciting school picnic story problem: the school bus departed from the school campus at 08:30 a.m. "
            "The journey to the famous botanical gardens took 1 hour and 45 minutes. At what time did the bus arrive? "
            "Add 1 hour to 08:30 a.m. to reach 09:30 a.m. Then add 45 minutes: 30 minutes reaches 10:00 a.m., plus the remaining 15 minutes "
            "reaches 10:15 a.m. The bus arrived at exactly 10:15 a.m.! After 3 hours of exploring the gardens, they began the return journey "
            "at 01:15 p.m. If the return trip took 1 hour and 20 minutes, they arrived safely back at school at 02:35 p.m.! "
            "Always break multi-step word problems into organized jump increments to solve complex time journeys with absolute mathematical certainty."
        ),
        "content_html": """
<div class="space-y-4">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <!-- Problem 1: Study Duration -->
        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-4">
            <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Scenario A: Homework Time</span>
            <h5 class="text-white font-bold text-sm mt-1">Start: 04:15 p.m. ➔ End: 05:40 p.m.</h5>
            <div class="mt-2 text-xs text-slate-300 space-y-1.5 font-mono bg-slate-900/80 p-3 rounded border border-slate-700">
                <p>1. 04:15 p.m. ➔ (+1 hr) ➔ 05:15 p.m.</p>
                <p>2. 05:15 p.m. ➔ (+25 min) ➔ 05:40 p.m.</p>
                <p class="text-amber-300 font-bold">Total Study Time = 1 hr 25 min (85 min)</p>
            </div>
            <p class="text-xs text-slate-400 mt-2">Break into 1 hour jump + remaining minute jump.</p>
        </div>

        <!-- Problem 2: Picnic Travel -->
        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-4">
            <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Scenario B: School Bus Trip</span>
            <h5 class="text-white font-bold text-sm mt-1">Departure: 08:30 a.m. (Trip: 1 hr 45 min)</h5>
            <div class="mt-2 text-xs text-slate-300 space-y-1.5 font-mono bg-slate-900/80 p-3 rounded border border-slate-700">
                <p>1. 08:30 a.m. + 1 hr = 09:30 a.m.</p>
                <p>2. 09:30 a.m. + 30 min = 10:00 a.m.</p>
                <p>3. 10:00 a.m. + 15 min = 10:15 a.m.</p>
                <p class="text-emerald-400 font-bold">Arrival Time = 10:15 a.m.</p>
            </div>
            <p class="text-xs text-slate-400 mt-2">Split 45 min into 30 min to reach hour mark + 15 min.</p>
        </div>
    </div>

    <div class="p-3 bg-indigo-950/40 border border-indigo-500/30 rounded-xl flex items-center justify-between text-xs">
        <span class="text-indigo-300 font-bold uppercase tracking-wider">Problem Strategy:</span>
        <span class="text-slate-300">When adding minutes crosses 60, bridge forward to the next hour and carry over the remainder!</span>
    </div>
</div>
""",
        "checkpoints": [
            {
                "id": "cp_15_1",
                "question": "An afternoon movie starts at 02:45 p.m. and runs for 2 hours and 15 minutes. At what time does the movie end?",
                "options": [
                    "05:00 p.m. (2:45 + 15 min = 3:00, then + 2 hr = 5:00)",
                    "04:45 p.m.",
                    "05:15 p.m.",
                    "04:00 p.m."
                ],
                "answer": 0,
                "explanation": "02:45 + 15 min brings the time to 03:00 p.m. Adding the remaining 2 hours brings the time to 05:00 p.m.",
                "hint": "Add 15 minutes to reach 3:00 p.m. first, then add the 2 hours."
            },
            {
                "id": "cp_15_2",
                "question": "A cricket match started at 09:30 a.m. and finished at 01:10 p.m. What was the total duration of the match?",
                "options": [
                    "3 hours 40 minutes",
                    "3 hours 30 minutes",
                    "4 hours 10 minutes",
                    "4 hours 40 minutes"
                ],
                "answer": 0,
                "explanation": "From 09:30 to 12:30 is 3 hours. From 12:30 to 01:00 is 30 minutes. From 01:00 to 01:10 is 10 minutes. Total = 3 hr 40 min.",
                "hint": "Jump 3 hours to 12:30 p.m., then count minutes to 01:10 p.m."
            }
        ]
    },
    {
        "id": 16,
        "title": "Daily Time Schedules",
        "tagline": "Mastering the Daily Routine • Coordinating School Breaks, Recess, and Future Time Planning",
        "lecture": (
            "Managing a productive, energetic, and joyful school day requires carefully coordinating hours, minutes, and seconds into a harmonious daily learning timetable! "
            "Consider a typical class five school schedule: morning assembly begins at 08:00 a.m. sharp and lasts for 25 minutes until 08:25 a.m. "
            "Academic classes run continuously until the much-awaited lunch recess bell rings at 12:15 p.m. If the lunch recess lasts for "
            "40 minutes, what time does the afternoon study session resume? Adding 40 minutes to 12:15 p.m. gives 12:55 p.m.! "
            "After two more exciting subject periods, school dispatches for home at 02:30 p.m. Students then have 1 hour and 15 minutes of "
            "travel and snack time before evening sports practice commences at 03:45 p.m. On the sports field, coaches time athletic sprints "
            "down to tenths of a second, demonstrating how seconds, minutes, and hours operate together in one seamless, unified continuum. "
            "Understanding how to calculate future times and work backward to determine necessary departure times empowers you to become punctual, "
            "organized, and reliable. Time is truly one of our most precious and irreplaceable lifelong treasures: mastering its measurement allows us to make the most of every "
            "single second, minute, and hour of our wonderful daily lives!"
        ),
        "content_html": """
<div class="space-y-4">
    <div class="bg-gradient-to-r from-emerald-900/40 via-teal-900/30 to-emerald-900/40 border border-emerald-500/30 rounded-xl p-4">
        <h4 class="text-emerald-300 font-bold text-sm tracking-wider uppercase mb-1">Coordinated Daily Schedule</h4>
        <p class="text-slate-200 text-sm leading-relaxed">
            A complete day seamlessly integrates hours (blocks), minutes (periods and breaks), and seconds (sports and quick events).
        </p>
    </div>

    <div class="overflow-hidden border border-slate-700 rounded-xl bg-slate-900/80">
        <table class="w-full text-xs text-left text-slate-300">
            <thead class="bg-slate-800 text-slate-200 font-semibold uppercase tracking-wider">
                <tr>
                    <th class="p-3">Period / Event</th>
                    <th class="p-3">Start Time</th>
                    <th class="p-3">Duration</th>
                    <th class="p-3">Finish Time</th>
                    <th class="p-3">Time Unit</th>
                </tr>
            </thead>
            <tbody class="divide-y divide-slate-800 font-mono">
                <tr class="hover:bg-slate-800/40">
                    <td class="p-3 text-white font-bold">Morning Assembly</td>
                    <td class="p-3">08:00 a.m.</td>
                    <td class="p-3 text-cyan-400">25 min</td>
                    <td class="p-3 text-white font-bold">08:25 a.m.</td>
                    <td class="p-3 text-slate-400">Minutes</td>
                </tr>
                <tr class="hover:bg-slate-800/40">
                    <td class="p-3 text-white font-bold">Morning Lessons</td>
                    <td class="p-3">08:25 a.m.</td>
                    <td class="p-3 text-cyan-400">3 hr 50 min</td>
                    <td class="p-3 text-white font-bold">12:15 p.m.</td>
                    <td class="p-3 text-slate-400">Hours & Min</td>
                </tr>
                <tr class="hover:bg-slate-800/40 bg-amber-950/30">
                    <td class="p-3 text-amber-300 font-bold">Lunch Break</td>
                    <td class="p-3">12:15 p.m.</td>
                    <td class="p-3 text-amber-400 font-bold">40 min</td>
                    <td class="p-3 text-amber-300 font-bold">12:55 p.m.</td>
                    <td class="p-3 text-amber-400">Minutes</td>
                </tr>
                <tr class="hover:bg-slate-800/40">
                    <td class="p-3 text-white font-bold">Sprint Training</td>
                    <td class="p-3">03:45 p.m.</td>
                    <td class="p-3 text-emerald-400 font-bold">20.4 sec</td>
                    <td class="p-3 text-white font-bold">03:45:20 p.m.</td>
                    <td class="p-3 text-emerald-300 font-bold">Seconds!</td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="p-3 bg-slate-900/80 border border-slate-700 rounded-xl flex items-center justify-between text-xs">
        <span class="text-slate-400 font-semibold uppercase tracking-wider">Key Takeaway:</span>
        <span class="text-emerald-300">Punctuality and scheduling build order, discipline, and success in everything we do!</span>
    </div>
</div>
""",
        "checkpoints": [
            {
                "id": "cp_16_1",
                "question": "If school lunch break starts at 12:20 p.m. and lasts 35 minutes, at what time does it finish?",
                "options": [
                    "12:55 p.m. (20 + 35 = 55)",
                    "01:00 p.m.",
                    "12:45 p.m.",
                    "01:05 p.m."
                ],
                "answer": 0,
                "explanation": "12:20 p.m. + 35 minutes = 12:55 p.m.",
                "hint": "Add 35 minutes to 20 minutes past 12."
            },
            {
                "id": "cp_16_2",
                "question": "To reach school by 07:50 a.m., if your walk takes 25 minutes, what is the latest time you must leave home?",
                "options": [
                    "07:25 a.m. (7:50 minus 25 min = 7:25)",
                    "07:30 a.m.",
                    "07:15 a.m.",
                    "07:35 a.m."
                ],
                "answer": 0,
                "explanation": "Work backward: 07:50 a.m. - 25 minutes = 07:25 a.m.",
                "hint": "Subtract 25 minutes from 07:50 a.m."
            }
        ]
    }
]
