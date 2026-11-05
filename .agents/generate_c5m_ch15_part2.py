# -*- coding: utf-8 -*-
"""Generate Slides 9 to 16 for Chapter 15: Data Through Pictures"""

import sys
sys.path.append('.agents')
from expand_c5m_ch15_part2 import lectures_part2

slides_part2 = [
    {
        "id": 9,
        "title": "Routine Bar Graph",
        "tagline": "Visualizing Time With Bars • Standard Cartesian Axes and Proportional Heights",
        "lecture": lectures_part2[9],
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed">
            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-700">
                <span class="text-amber-400 font-bold block mb-1">Anatomy of a Vertical Bar Graph</span>
                <p class="text-slate-300">A bar graph represents numerical values using rectangular bars. Key architectural elements include:</p>
                <div class="grid grid-cols-2 gap-2 mt-2 font-mono text-[11px] text-slate-200">
                    <div class="p-1.5 bg-slate-950/80 rounded border border-slate-800">
                        <span class="text-amber-400 font-bold block">Horizontal Axis (X):</span> Discrete Categories (Activities)
                    </div>
                    <div class="p-1.5 bg-slate-950/80 rounded border border-slate-800">
                        <span class="text-cyan-400 font-bold block">Vertical Axis (Y):</span> Numerical Scale (Hours 0–10)
                    </div>
                </div>
            </div>
            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-700">
                <span class="text-cyan-400 font-bold block mb-1">Daily Routine Bar Heights</span>
                <div class="space-y-1 font-mono text-[11px] text-slate-300">
                    <div class="flex justify-between items-center p-1 bg-slate-950/80 rounded border border-slate-800">
                        <span>🛏️ Sleeping</span><span class="text-indigo-400 font-bold">8 Hours (Tallest Bar)</span>
                    </div>
                    <div class="flex justify-between items-center p-1 bg-slate-950/80 rounded border border-slate-800">
                        <span>🏫 School</span><span class="text-amber-400 font-bold">6 Hours</span>
                    </div>
                    <div class="flex justify-between items-center p-1 bg-slate-950/80 rounded border border-slate-800">
                        <span>📖 Self-Study</span><span class="text-cyan-400 font-bold">2 Hours (Shortest Bar)</span>
                    </div>
                    <div class="flex justify-between items-center p-1 bg-slate-950/80 rounded border border-slate-800">
                        <span>⚽ Play & Meals</span><span class="text-emerald-400 font-bold">4 Hours</span>
                    </div>
                    <div class="flex justify-between items-center p-1 bg-slate-950/80 rounded border border-slate-800">
                        <span>⏳ Other Routines</span><span class="text-rose-400 font-bold">4 Hours</span>
                    </div>
                </div>
            </div>
            <div class="p-2.5 rounded-lg bg-emerald-500/10 border border-emerald-500/30 text-emerald-200 text-[11px]">
                <strong>Visual Efficiency:</strong> Heights reveal the tallest bar (sleep) and shortest bar (study) instantaneously.
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "What determines the height of each bar in a vertical bar graph?",
                "options": [
                    "The width of the graph paper",
                    "The numerical value or frequency of the category",
                    "The number of letters in the category name",
                    "The color chosen to paint the column"
                ],
                "answer": 1,
                "explanation": "In a vertical bar graph, the height of each rectangular bar corresponds directly to the numerical quantity it represents.",
                "hint": "Taller bars represent larger numerical values."
            },
            {
                "question": "Which activity corresponds to the tallest bar in the 24-hour routine graph?",
                "options": ["School (6 hours)", "Self-Study (2 hours)", "Sleeping (8 hours)", "Play & Meals (4 hours)"],
                "answer": 2,
                "explanation": "Sleeping has 8 hours, which is the greatest height among all activities on the vertical axis.",
                "hint": "Identify the activity with the highest numerical value."
            }
        ]
    },
    {
        "id": 10,
        "title": "Schedule Balance Analysis",
        "tagline": "Evaluating Routine Equity • Sleep-Study Proportions and Personal Planning",
        "lecture": lectures_part2[10],
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed">
            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-700">
                <span class="text-amber-400 font-bold block mb-1">The Golden Rule of Thirds (8-8-8 Balance)</span>
                <p class="text-slate-300">A healthy 24-hour daily routine often balances three fundamental pillars:</p>
                <div class="grid grid-cols-3 gap-2 mt-2 text-center font-mono text-[11px]">
                    <div class="p-2 bg-indigo-950/60 rounded border border-indigo-500/30 text-indigo-300">
                        <div class="font-bold text-sm">8 Hrs</div>
                        <div class="text-[10px]">Rest / Sleep</div>
                    </div>
                    <div class="p-2 bg-amber-950/60 rounded border border-amber-500/30 text-amber-300">
                        <div class="font-bold text-sm">8 Hrs</div>
                        <div class="text-[10px]">School + Study</div>
                    </div>
                    <div class="p-2 bg-emerald-950/60 rounded border border-emerald-500/30 text-emerald-300">
                        <div class="font-bold text-sm">8 Hrs</div>
                        <div class="text-[10px]">Play, Food & Life</div>
                    </div>
                </div>
            </div>
            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-700">
                <span class="text-cyan-400 font-bold block mb-1">Personal Time Auditing</span>
                <p class="text-slate-300">By plotting their own day on grid paper, students discover whether screen time or unstructured delays eat into vital sleep or physical activity.</p>
            </div>
            <div class="p-2.5 rounded-lg bg-sky-500/10 border border-sky-500/30 text-sky-200 text-[11px]">
                <strong>Mathematical Reflection:</strong> Fraction of day spent sleeping = 8/24 = 1/3 of the day.
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "What is the ratio of sleeping hours (8) to total daily educational hours (6 school + 2 study = 8)?",
                "options": ["8 to 4 (2:1)", "8 to 8 (1:1 equal balance)", "8 to 6", "8 to 12"],
                "answer": 1,
                "explanation": "Both sleep (8 hours) and combined education (8 hours) are equal, creating a 1:1 balance.",
                "hint": "Compare 8 hours of sleep with 8 hours of education."
            },
            {
                "question": "If a student sleeps for 9 hours instead of 8, how many hours remain for waking activities?",
                "options": ["14 hours", "15 hours", "16 hours", "12 hours"],
                "answer": 1,
                "explanation": "Subtract sleep hours from the 24-hour total: 24 - 9 = 15 hours remaining.",
                "hint": "Subtract 9 from 24."
            }
        ]
    },
    {
        "id": 11,
        "title": "Finger Length Measurement",
        "tagline": "Hands-on Physical Data • Cutting and Measuring Paper Strips",
        "lecture": lectures_part2[11],
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed">
            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-700">
                <span class="text-amber-400 font-bold block mb-1">Paper Strip Measurement Protocol</span>
                <p class="text-slate-300">Flexible paper strips mold cleanly along finger contours, avoiding parallax errors caused by stiff rulers:</p>
                <ol class="list-decimal list-inside space-y-1 text-slate-300 mt-2 font-mono text-[11px]">
                    <li>Align strip edge with the finger base crease joint</li>
                    <li>Mark the exact fingertip apex with a fine pencil dot</li>
                    <li>Cut / tear away the excess paper beyond the pencil mark</li>
                    <li>Measure the strip on a millimeter ruler and record length</li>
                </ol>
            </div>
            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-700">
                <span class="text-cyan-400 font-bold block mb-1">Sample Classroom Measurements</span>
                <div class="grid grid-cols-2 gap-2 font-mono text-[11px] text-slate-200 mt-1">
                    <div class="p-1.5 bg-slate-950/80 rounded border border-slate-800">Friend A: 4.5 cm</div>
                    <div class="p-1.5 bg-slate-950/80 rounded border border-slate-800">Friend B: 5.0 cm</div>
                    <div class="p-1.5 bg-slate-950/80 rounded border border-slate-800">Friend C: 5.8 cm</div>
                    <div class="p-1.5 bg-slate-950/80 rounded border border-slate-800">Friend D: 4.2 cm</div>
                </div>
            </div>
            <div class="p-2.5 rounded-lg bg-emerald-500/10 border border-emerald-500/30 text-emerald-200 text-[11px]">
                <strong>Accuracy Tip:</strong> Consistent starting points at the base joint are essential for valid comparisons.
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "Why is a flexible paper strip advantageous when measuring body contours like fingers?",
                "options": [
                    "It cannot be cut with scissors",
                    "It conforms smoothly along curved surfaces without slipping",
                    "It always measures exactly 10 cm automatically",
                    "It makes the finger grow longer"
                ],
                "answer": 1,
                "explanation": "Flexible paper bends along curved anatomical surfaces, ensuring accurate end-to-end measurement.",
                "hint": "Consider how stiff rulers behave on curved skin."
            },
            {
                "question": "If Friend D's finger strip measures 4.2 cm and Friend C's measures 5.8 cm, what is the difference in length?",
                "options": ["1.0 cm", "1.6 cm", "2.0 cm", "0.6 cm"],
                "answer": 1,
                "explanation": "Subtract Friend D's length from Friend C's: 5.8 - 4.2 = 1.6 cm.",
                "hint": "Calculate 5.8 minus 4.2."
            }
        ]
    },
    {
        "id": 12,
        "title": "Strip Bar Graph",
        "tagline": "Constructing Physical Graphs • Pasting Strips onto a Vertical Grid Axis",
        "lecture": lectures_part2[12],
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed">
            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-700">
                <span class="text-amber-400 font-bold block mb-1">Building a Tangible Physical Bar Graph</span>
                <p class="text-slate-300">Pasting physical strips of measured paper onto a common baseline transforms real objects into a live bar graph:</p>
                <div class="mt-2 p-2 rounded bg-amber-500/10 border border-amber-500/30 text-amber-200 font-mono text-[11px] text-center">
                    📏 Common Baseline: All strips start at Height = 0 cm
                </div>
            </div>
            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-700">
                <span class="text-cyan-400 font-bold block mb-1">Cohort Statistical Highlights</span>
                <div class="space-y-1.5 font-mono text-[11px] text-slate-300">
                    <div class="flex justify-between items-center p-1.5 bg-slate-950/80 rounded border border-slate-800">
                        <span>Max Length (Tallest Strip):</span>
                        <span class="text-emerald-400 font-bold">5.8 cm (Friend C)</span>
                    </div>
                    <div class="flex justify-between items-center p-1.5 bg-slate-950/80 rounded border border-slate-800">
                        <span>Min Length (Shortest Strip):</span>
                        <span class="text-rose-400 font-bold">4.2 cm (Friend D)</span>
                    </div>
                    <div class="flex justify-between items-center p-1.5 bg-slate-950/80 rounded border border-slate-800">
                        <span>Variation Range (Spread):</span>
                        <span class="text-amber-400 font-bold">5.8 - 4.2 = 1.6 cm</span>
                    </div>
                </div>
            </div>
            <div class="p-2.5 rounded-lg bg-emerald-500/10 border border-emerald-500/30 text-emerald-200 text-[11px]">
                <strong>Key Insight:</strong> Aligning all strips to a common zero line is mandatory for legitimate visual comparison.
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "What would happen if paper strips were pasted without aligning them to a common zero baseline?",
                "options": [
                    "The graph would become more accurate",
                    "Visual comparison would be invalid because base heights would differ",
                    "The strips would shrink automatically",
                    "The centimeter scale would turn negative"
                ],
                "answer": 1,
                "explanation": "A common baseline is mandatory; otherwise, higher starting points create misleading optical heights.",
                "hint": "Think about whether a runner can start 5 meters ahead in a race."
            },
            {
                "question": "What is the difference between the longest finger (5.8 cm) and shortest finger (4.2 cm)?",
                "options": ["1.2 cm", "1.6 cm", "2.0 cm", "0.8 cm"],
                "answer": 1,
                "explanation": "5.8 cm - 4.2 cm = 1.6 cm.",
                "hint": "Subtract 4.2 from 5.8."
            }
        ]
    },
    {
        "id": 13,
        "title": "Canteen Food Waste",
        "tagline": "Real-World Sustainability Data • Daily Waste Tracking in Kilograms",
        "lecture": lectures_part2[13],
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed">
            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-700">
                <span class="text-amber-400 font-bold block mb-1">School Canteen Waste Audit</span>
                <p class="text-slate-300">Daily kitchen waste recorded across weekdays to evaluate portion sizing and meal popularity:</p>
                <div class="overflow-x-auto mt-2">
                    <table class="w-full text-left font-mono text-[11px] text-slate-300 border-collapse">
                        <thead>
                            <tr class="border-b border-slate-700 text-amber-300">
                                <th class="py-1">Day</th>
                                <th class="py-1">Menu Item</th>
                                <th class="py-1 text-right">Waste (kg)</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-800">
                            <tr><td>Monday</td><td>Sandwich</td><td class="text-right font-bold text-white">4 kg</td></tr>
                            <tr><td>Tuesday</td><td>Paratha</td><td class="text-right font-bold text-white">7 kg</td></tr>
                            <tr><td>Wednesday</td><td>Khichdi</td><td class="text-right font-bold text-emerald-400">3 kg (Lowest)</td></tr>
                            <tr><td>Thursday</td><td>Puri-Sabzi</td><td class="text-right font-bold text-rose-400">8 kg (Highest)</td></tr>
                            <tr><td>Friday</td><td>Idli-Sambar</td><td class="text-right font-bold text-white">5 kg</td></tr>
                            <tr class="border-t border-slate-600 font-bold text-amber-400"><td>Total Week</td><td>All Menus</td><td class="text-right">27 kg</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
            <div class="p-2.5 rounded-lg bg-rose-500/10 border border-rose-500/30 text-rose-200 text-[11px]">
                <strong>Peak Waste Alert:</strong> Thursday (Puri-Sabzi) generated 8 kg of plate waste, requiring immediate portion review.
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "Which weekday generated the highest amount of food waste in the school canteen?",
                "options": ["Monday (4 kg)", "Tuesday (7 kg)", "Thursday (8 kg)", "Friday (5 kg)"],
                "answer": 2,
                "explanation": "Thursday (Puri-Sabzi) had 8 kg of waste, which is the tallest bar on the graph.",
                "hint": "Find the day with the highest recorded kilogram value."
            },
            {
                "question": "How much less food was wasted on Wednesday (3 kg) compared to Thursday (8 kg)?",
                "options": ["3 kg", "5 kg", "6 kg", "8 kg"],
                "answer": 1,
                "explanation": "Subtract Wednesday's waste from Thursday's waste: 8 - 3 = 5 kg less waste.",
                "hint": "Calculate 8 minus 3."
            }
        ]
    },
    {
        "id": 14,
        "title": "Waste Reduction Analysis",
        "tagline": "Quantifying Impact • Converting Waste Kilograms to Meals Saved",
        "lecture": lectures_part2[14],
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed">
            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-700">
                <span class="text-amber-400 font-bold block mb-1">Weekly Waste & Meal Conversion</span>
                <p class="text-slate-300">Converting mass of wasted food into equivalent student meals demonstrates the human dimension of statistics:</p>
                <div class="space-y-1.5 font-mono text-[11px] text-slate-300 mt-2">
                    <div class="p-1.5 bg-slate-950/80 rounded border border-slate-800 flex justify-between">
                        <span>Total Weekly Waste:</span>
                        <span class="text-amber-400 font-bold">4 + 7 + 3 + 8 + 5 = 27 kg</span>
                    </div>
                    <div class="p-1.5 bg-slate-950/80 rounded border border-slate-800 flex justify-between">
                        <span>Conversion Factor:</span>
                        <span class="text-cyan-400 font-bold">1 kg Food = 3 Child Meals</span>
                    </div>
                    <div class="p-1.5 bg-slate-950/80 rounded border border-slate-800 flex justify-between">
                        <span>Potential Meals Wasted:</span>
                        <span class="text-rose-400 font-bold">27 × 3 = 81 Children Fed</span>
                    </div>
                </div>
            </div>
            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-700">
                <span class="text-emerald-400 font-bold block mb-1">Student Council Action Plan</span>
                <ul class="list-disc list-inside space-y-1 text-slate-300 text-[11px]">
                    <li><b>Opt-in Sizing:</b> Serve smaller base portions with free seconds</li>
                    <li><b>Menu Tuning:</b> Adjust seasoning based on student preference feedback</li>
                    <li><b>Daily Notice:</b> Display daily kg tracker in canteen to raise mindfulness</li>
                </ul>
            </div>
            <div class="p-2.5 rounded-lg bg-emerald-500/10 border border-emerald-500/30 text-emerald-200 text-[11px]">
                <strong>Data for Action:</strong> Statistical analysis drives ethical, community-wide solutions.
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "If 1 kg of food feeds 3 children, how many children could be fed with 27 kg of food?",
                "options": ["54 children", "81 children", "90 children", "30 children"],
                "answer": 1,
                "explanation": "Multiply the total kilograms by the conversion rate: 27 × 3 = 81 children.",
                "hint": "Multiply 27 by 3."
            },
            {
                "question": "What is the total food waste over the five school days?",
                "options": ["20 kg", "25 kg", "27 kg", "32 kg"],
                "answer": 2,
                "explanation": "4 + 7 + 3 + 8 + 5 = 27 kg total waste.",
                "hint": "Add 4, 7, 3, 8, and 5."
            }
        ]
    },
    {
        "id": 15,
        "title": "Picture Data Logic",
        "tagline": "Observational Counting • True or False Mathematical Verification",
        "lecture": lectures_part2[15],
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed">
            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-700">
                <span class="text-amber-400 font-bold block mb-1">Visual Observation Matrix (12 Children)</span>
                <p class="text-slate-300">Methodical attribute counting across a cohort of 12 students in a courtyard illustration:</p>
                <div class="grid grid-cols-2 gap-2 mt-2 font-mono text-[11px] text-slate-300">
                    <div class="p-1.5 bg-slate-950/80 rounded border border-slate-800">🧢 Wearing Caps: <b>5</b></div>
                    <div class="p-1.5 bg-slate-950/80 rounded border border-slate-800">👓 Wearing Glasses: <b>4</b></div>
                    <div class="p-1.5 bg-slate-950/80 rounded border border-slate-800">🎒 Wearing Backpacks: <b>6</b></div>
                    <div class="p-1.5 bg-slate-950/80 rounded border border-slate-800">📚 Holding Books: <b>7</b></div>
                </div>
            </div>
            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-700">
                <span class="text-cyan-400 font-bold block mb-1">Logical Statement Verification</span>
                <div class="space-y-1 font-mono text-[10.5px] text-slate-300">
                    <div class="p-1 bg-slate-950/80 rounded border border-slate-800">
                        <span>"5 children wear caps":</span> <span class="text-emerald-400 font-bold ml-1">TRUE (Count = 5)</span>
                    </div>
                    <div class="p-1 bg-slate-950/80 rounded border border-slate-800">
                        <span>"More glasses than backpacks":</span> <span class="text-rose-400 font-bold ml-1">FALSE (4 < 6)</span>
                    </div>
                    <div class="p-1 bg-slate-950/80 rounded border border-slate-800">
                        <span>"Both cap and glasses = 3":</span> <span class="text-rose-400 font-bold ml-1">FALSE (Overlap = 2)</span>
                    </div>
                </div>
            </div>
            <div class="p-2.5 rounded-lg bg-sky-500/10 border border-sky-500/30 text-sky-200 text-[11px]">
                <strong>Scientific Rigor:</strong> Mathematical truth depends entirely on verifiable evidence, not superficial impressions.
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "If 4 children wear glasses and 6 wear backpacks, which statement is mathematically True?",
                "options": [
                    "Glasses count exceeds backpack count",
                    "Backpack count exceeds glasses count by 2",
                    "Both counts are equal",
                    "There are 15 children wearing glasses"
                ],
                "answer": 1,
                "explanation": "6 backpacks - 4 glasses = 2 more children wearing backpacks than glasses.",
                "hint": "Compare 6 with 4."
            },
            {
                "question": "What is the total number of children in the courtyard illustration?",
                "options": ["10 children", "12 children", "15 children", "20 children"],
                "answer": 1,
                "explanation": "The cohort has exactly 12 children in the courtyard group.",
                "hint": "Check the total group size mentioned in the text."
            }
        ]
    },
    {
        "id": 16,
        "title": "Geometric Cutout Solids",
        "tagline": "Spatial Geometry Nets • Constructing Icosahedrons and Dodecahedrons",
        "lecture": lectures_part2[16],
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed">
            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-700">
                <span class="text-amber-400 font-bold block mb-1">What is a Polyhedral Net?</span>
                <p class="text-slate-300">A geometric net is an unfolded flat 2D pattern of connected polygons that can be folded along shared edges to form a closed 3D solid polyhedron.</p>
            </div>
            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-700">
                <span class="text-cyan-400 font-bold block mb-1">Two Classic Regular Polyhedra</span>
                <div class="grid grid-cols-2 gap-2 font-mono text-[11px] text-slate-300 mt-1">
                    <div class="p-2 bg-slate-950/80 rounded border border-slate-800">
                        <span class="text-indigo-400 font-bold block">🔷 Icosahedron</span>
                        <div>• 20 Equilateral Triangles</div>
                        <div>• 12 Vertices, 30 Edges</div>
                    </div>
                    <div class="p-2 bg-slate-950/80 rounded border border-slate-800">
                        <span class="text-emerald-400 font-bold block">⬟ Dodecahedron</span>
                        <div>• 12 Regular Pentagons</div>
                        <div>• 20 Vertices, 30 Edges</div>
                    </div>
                </div>
            </div>
            <div class="p-2.5 rounded-lg bg-amber-500/10 border border-amber-500/30 text-amber-200 text-[11px]">
                <strong>Euler's Formula:</strong> For both solids: Faces - Edges + Vertices = 2 (e.g., 20 - 30 + 12 = 2).
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "How many equilateral triangular faces make up a regular icosahedron?",
                "options": ["12 faces", "20 faces", "30 faces", "8 faces"],
                "answer": 1,
                "explanation": "An icosahedron has exactly 20 congruent equilateral triangular faces (from the Greek 'eikosi' meaning twenty).",
                "hint": "The prefix 'icosa' means twenty."
            },
            {
                "question": "What regular polygon shape forms all 12 faces of a dodecahedron?",
                "options": ["Equilateral triangle", "Square", "Regular pentagon", "Regular hexagon"],
                "answer": 2,
                "explanation": "A dodecahedron has 12 faces that are all congruent regular 5-sided pentagons.",
                "hint": "Think of a 5-sided polygon."
            }
        ]
    }
]

print("=== VERIFYING PART 2 SLIDES ===")
for s in slides_part2:
    wc = len(s['lecture'].split())
    print(f"Slide {s['id']} ('{s['title']}'): {wc} words")
    assert 195 <= wc <= 215, f"Slide {s['id']} lecture word count {wc} out of range 195-215!"
    assert len(s['checkpoints']) == 2
print("Part 2 verified successfully!")
