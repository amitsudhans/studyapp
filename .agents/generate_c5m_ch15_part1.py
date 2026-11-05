# -*- coding: utf-8 -*-
"""Generate Slides 1 to 8 for Chapter 15: Data Through Pictures"""

import re

slides_part1 = [
    {
        "id": 1,
        "title": "Raw Data Collection",
        "tagline": "Systematic Field Inquiry • Gathering TV Viewing Hours Across Thirty-Five Friends",
        "lecture": (
            "Welcome to our mathematical investigation of data collection, systematic organization, and visual interpretation. "
            "When curious young researchers set out to understand everyday human habits, they begin with a direct inquiry. "
            "In this school survey, two student reporters interviewed thirty-five classmates to measure daily television viewing duration. "
            "As each classmate answered, the raw individual responses were written down directly into a handheld field notebook. "
            "Some friends reported watching television for only half an hour each afternoon after completing homework and outdoor chores. "
            "Other children recorded one full hour, while several engaged for one and a half hours or two hours. "
            "A few classmates admitted spending more than two hours glued to the television screen every single evening. "
            "At first glance, a notebook filled with scattered numbers, varied scribbles, and handwritten notes looks overwhelming and disordered. "
            "Without proper organization, it is impossible to quickly answer fundamental questions, such as which viewing duration is most common. "
            "Raw data represents unorganized factual numbers collected directly from the original source before any mathematical sorting occurs. "
            "To transform these scattered observations into meaningful mathematical knowledge, we must structure the findings into clear categories. "
            "Careful data collection provides the empirical bedrock upon which all statistical reasoning, logical deductions, and sound conclusions are built."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed">
            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-700">
                <span class="text-amber-400 font-bold block mb-1">What is Raw Data?</span>
                <p class="text-slate-300">Raw data consists of initial, unprocessed numbers and facts collected directly through field surveys, observations, or measurements before grouping or statistical analysis.</p>
            </div>
            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-700">
                <span class="text-cyan-400 font-bold block mb-1">The 35-Friend TV Viewing Survey</span>
                <p class="text-slate-300">Two student investigators surveyed 35 classmates regarding their daily television screen time. Raw notebook responses included:</p>
                <div class="grid grid-cols-2 gap-2 mt-2 font-mono text-[11px] text-slate-200">
                    <div class="p-2 bg-slate-950/80 rounded border border-slate-800">½ hr, 1 hr, 1½ hrs, 2 hrs, >2 hrs</div>
                    <div class="p-2 bg-slate-950/80 rounded border border-slate-800">Total Surveyed = 35 Children</div>
                </div>
            </div>
            <div class="p-2.5 rounded-lg bg-amber-500/10 border border-amber-500/30 text-amber-200 text-[11px]">
                <strong>Key Takeaway:</strong> Raw data requires systematic categorization into time intervals before meaningful patterns can emerge.
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "What is the primary defining characteristic of raw data in mathematical statistics?",
                "options": [
                    "It is already organized into a finished visual graph",
                    "It consists of initial unorganized numbers collected directly from observation",
                    "It must always equal exactly one hundred data points",
                    "It only contains numbers that have been multiplied together"
                ],
                "answer": 1,
                "explanation": "Raw data represents initial unorganized facts and figures collected directly from source observations before any grouping or analysis.",
                "hint": "Think about what a notebook looks like before you create tables or charts."
            },
            {
                "question": "If 35 friends are surveyed in total, what must the sum of all response frequencies equal?",
                "options": ["Exactly 35", "Fewer than 30", "Always 50", "Exactly 100"],
                "answer": 0,
                "explanation": "Every surveyed classmate contributes exactly one response, so the total sum across all frequency categories must equal the survey sample size of 35.",
                "hint": "No responses are lost or duplicated when tallying the full group."
            }
        ]
    },
    {
        "id": 2,
        "title": "Frequency Distribution Table",
        "tagline": "Organizing Observations • Tally Marks and Mutually Exclusive Time Intervals",
        "lecture": (
            "Now let us examine how to structure raw notebook responses into an organized frequency distribution table. "
            "A frequency table groups scattered observations into clear, mutually exclusive intervals so that every single data point belongs somewhere. "
            "For our television survey, we establish five distinct categories of daily screen time across the cohort. "
            "The first category is half an hour, followed by one hour, one and a half hours, two hours, and finally more than two hours. "
            "To count accurately without skipping or double-counting, we record each response using standardized tally marks. "
            "Four vertical lines are drawn one by one, and every fifth entry is recorded as a diagonal slash across the four lines. "
            "This bundle of five allows our eyes to quickly count large totals in convenient groups of five. "
            "When all thirty-five children are tallied, we write the final numerical frequency beside each time category. "
            "For instance, five children watch half an hour, twelve children watch one hour, eight watch one and a half hours, six watch two hours, and four watch more than two hours. "
            "Adding five, twelve, eight, six, and four yields exactly thirty-five, verifying our complete survey tally. "
            "Frequency distribution tables transform raw chaotic lists into clear, readable, and highly informative mathematical structures."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed">
            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-700">
                <span class="text-amber-400 font-bold block mb-1">Standard Tally Marks Grouping</span>
                <p class="text-slate-300">Tally marks count occurrences in bundles of 5: four vertical strokes (||||) crossed by a diagonal line (<s>||||</s> = 5). This makes large totals rapid to count.</p>
            </div>
            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-700">
                <span class="text-cyan-400 font-bold block mb-1">Frequency Table of Daily TV Viewing</span>
                <div class="overflow-x-auto mt-1">
                    <table class="w-full text-left font-mono text-[11px] text-slate-300 border-collapse">
                        <thead>
                            <tr class="border-b border-slate-700 text-amber-300">
                                <th class="py-1">Duration</th>
                                <th class="py-1">Tally Marks</th>
                                <th class="py-1 text-right">Frequency</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-800">
                            <tr><td>½ hour</td><td><s>||||</s></td><td class="text-right font-bold text-white">5</td></tr>
                            <tr><td>1 hour</td><td><s>||||</s> <s>||||</s> ||</td><td class="text-right font-bold text-white">12</td></tr>
                            <tr><td>1½ hours</td><td><s>||||</s> |||</td><td class="text-right font-bold text-white">8</td></tr>
                            <tr><td>2 hours</td><td><s>||||</s> |</td><td class="text-right font-bold text-white">6</td></tr>
                            <tr><td>> 2 hours</td><td>||||</td><td class="text-right font-bold text-white">4</td></tr>
                            <tr class="border-t border-slate-600 font-bold text-emerald-400"><td>Total</td><td>35 Tallies</td><td class="text-right">35</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
            <div class="p-2.5 rounded-lg bg-emerald-500/10 border border-emerald-500/30 text-emerald-200 text-[11px]">
                <strong>Check Sum:</strong> 5 + 12 + 8 + 6 + 4 = 35 total classmates surveyed.
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "How many items are represented by two full tally bundles followed by three single marks (<s>||||</s> <s>||||</s> |||)?",
                "options": ["10", "13", "15", "8"],
                "answer": 1,
                "explanation": "Each bundle of five equals 5. Two bundles equal 10, plus 3 individual strokes equals 13 items.",
                "hint": "Count by 5s: 5, 10, then add the three extra marks."
            },
            {
                "question": "Which time duration had the highest frequency of viewers in our 35-classmate survey?",
                "options": ["½ hour (5 children)", "1 hour (12 children)", "2 hours (6 children)", "More than 2 hours (4 children)"],
                "answer": 1,
                "explanation": "1 hour had 12 viewers, which is the highest frequency in the distribution table.",
                "hint": "Look for the category with the largest numerical tally."
            }
        ]
    },
    {
        "id": 3,
        "title": "TV Survey Analysis",
        "tagline": "Interpreting Statistical Tables • Evaluating Healthy Screen Habits",
        "lecture": (
            "Once our frequency table is assembled, we can extract profound insights regarding daily lifestyle patterns and screen habits. "
            "Data analysis involves comparing categories, calculating combined subgroups, and evaluating health recommendations against actual recorded behavior. "
            "Looking closely at our television viewing table, we immediately observe that one hour is the most frequent choice, chosen by twelve children. "
            "Next, let us determine how many classmates spend one hour or less watching television each day. "
            "We combine the five children watching half an hour with the twelve children watching one hour, giving seventeen children in total. "
            "Conversely, how many children watch television for more than one hour daily? "
            "We sum eight children at one and a half hours, six at two hours, and four at more than two hours, giving eighteen children. "
            "Notice that seventeen plus eighteen equals our complete sample of thirty-five friends without any missing entries. "
            "Health guidelines generally recommend limiting recreational screen time to no more than one hour daily to safeguard eyesight and physical activity. "
            "Our data reveals that eighteen out of thirty-five children exceed this recommended threshold. "
            "Statistical tables empower students to transition from vague guesses to factual evidence, illuminating real-world habits with mathematical precision."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed">
            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-700">
                <span class="text-amber-400 font-bold block mb-1">Subgroup Cumulative Calculations</span>
                <div class="space-y-1.5 text-slate-300 font-mono text-[11px]">
                    <div class="p-1.5 bg-slate-950/80 rounded border border-slate-800">
                        <span class="text-emerald-400 font-bold">1 Hour or Less:</span> 5 (½ hr) + 12 (1 hr) = 17 children
                    </div>
                    <div class="p-1.5 bg-slate-950/80 rounded border border-slate-800">
                        <span class="text-rose-400 font-bold">More than 1 Hour:</span> 8 (1½ hrs) + 6 (2 hrs) + 4 (>2 hrs) = 18 children
                    </div>
                    <div class="text-slate-400 text-[10px] mt-1 text-center">Sum: 17 + 18 = 35 children (100% of surveyed cohort)</div>
                </div>
            </div>
            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-700">
                <span class="text-cyan-400 font-bold block mb-1">Evaluating Health Recommendations</span>
                <p class="text-slate-300">Health experts recommend no more than 1 hour of daily leisure screen time. In our cohort, 18 out of 35 children (over 51%) exceed this limit, highlighting an important lifestyle consideration.</p>
            </div>
            <div class="p-2.5 rounded-lg bg-sky-500/10 border border-sky-500/30 text-sky-200 text-[11px]">
                <strong>Analytical Power:</strong> Tables allow combining multiple intervals to evaluate broader societal questions.
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "How many children watch television for one hour or less per day in the survey?",
                "options": ["12 children", "17 children", "18 children", "5 children"],
                "answer": 1,
                "explanation": "5 children watch ½ hour and 12 watch 1 hour. Combined: 5 + 12 = 17 children watch one hour or less.",
                "hint": "Add the counts for the ½ hour and 1 hour categories together."
            },
            {
                "question": "What fraction of the 35 surveyed children watch television for more than two hours daily?",
                "options": ["4 out of 35", "12 out of 35", "18 out of 35", "6 out of 35"],
                "answer": 0,
                "explanation": "The table records exactly 4 children in the category of more than two hours, which is 4/35 of the cohort.",
                "hint": "Check the last row of the frequency table."
            }
        ]
    },
    {
        "id": 4,
        "title": "Stock Pictograph Scaling",
        "tagline": "Visual Data Encoding • One Icon Represents Five Physical Play Items",
        "lecture": (
            "Now let us explore pictographs, where numerical quantities are represented visually using scaled symbols and meaningful icons. "
            "Consider a neighbourhood toy shop preparing its inventory stock before summer vacation begins for schoolchildren. "
            "The shopkeeper counts hundreds of play items, including stuffed teddy bears, traditional board games, and various sports equipment. "
            "Drawing dozens of individual pictures on an inventory sheet would take far too long and clutter the paper. "
            "Instead, cartographers and mathematicians define a key or scale factor to represent multiple physical objects compactly. "
            "In this toy shop inventory pictograph, the shopkeeper decides that one single icon represents five physical items. "
            "Therefore, if we see four toy icons in the toys row, we calculate four multiplied by five, which equals twenty toys in stock. "
            "If the board games row displays six game icons, the total quantity equals six multiplied by five, giving thirty board games. "
            "If the sports equipment row displays eight ball icons, we multiply eight by five, yielding forty sports items. "
            "By establishing a clear scale, a small number of icons compactly represents substantial inventory quantities. "
            "Always inspect the key at the bottom or corner of a pictograph before counting, because the scale determines the true values."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed">
            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-700">
                <span class="text-amber-400 font-bold block mb-1">The Essential Role of the Scale / Key</span>
                <p class="text-slate-300">A pictograph represents data through pictures. The <b>Key</b> tells the viewer the numerical value represented by each icon symbol.</p>
                <div class="mt-2 p-2 rounded bg-amber-500/10 border border-amber-500/30 text-amber-200 font-mono text-[11px] text-center">
                    🔑 Scale: 1 Icon (⭐) = 5 Physical Items
                </div>
            </div>
            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-700">
                <span class="text-cyan-400 font-bold block mb-1">Toy Shop Inventory Calculations</span>
                <div class="space-y-1.5 font-mono text-[11px] text-slate-300">
                    <div class="flex justify-between items-center p-1.5 bg-slate-950/80 rounded border border-slate-800">
                        <span>🧸 Toys: 4 icons × 5</span>
                        <span class="text-amber-400 font-bold">20 Toys</span>
                    </div>
                    <div class="flex justify-between items-center p-1.5 bg-slate-950/80 rounded border border-slate-800">
                        <span>🎲 Board Games: 6 icons × 5</span>
                        <span class="text-cyan-400 font-bold">30 Games</span>
                    </div>
                    <div class="flex justify-between items-center p-1.5 bg-slate-950/80 rounded border border-slate-800">
                        <span>⚽ Sports Gear: 8 icons × 5</span>
                        <span class="text-emerald-400 font-bold">40 Sports Items</span>
                    </div>
                </div>
            </div>
            <div class="p-2.5 rounded-lg bg-emerald-500/10 border border-emerald-500/30 text-emerald-200 text-[11px]">
                <strong>Total Stock:</strong> 20 + 30 + 40 = 90 total play items in the shop inventory.
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "If 1 icon represents 5 items, how many total items are represented by 7 icons?",
                "options": ["12 items", "25 items", "35 items", "70 items"],
                "answer": 2,
                "explanation": "Multiply the number of icons by the scale value: 7 × 5 = 35 items.",
                "hint": "Calculate 7 groups of 5."
            },
            {
                "question": "How many icons must be drawn to represent 40 sports equipment items when 1 icon = 5 items?",
                "options": ["8 icons", "5 icons", "10 icons", "4 icons"],
                "answer": 0,
                "explanation": "Divide total items by the scale factor: 40 ÷ 5 = 8 icons.",
                "hint": "Divide 40 by 5."
            }
        ]
    },
    {
        "id": 5,
        "title": "Custom Scale Pictograph",
        "tagline": "Modifying Representation Scale • Converting Between Scale Factors",
        "lecture": (
            "An essential mathematical skill is choosing and adapting the scale factor of a pictograph to suit our analytical needs. "
            "In the previous scenario, our shopkeeper used a scale where one icon represented five physical play items. "
            "Under that scale, ninety total items required eighteen separate icons across the three inventory rows on the page. "
            "What happens if our paper is smaller, and we wish to use fewer icons for faster drawing and clearer presentation? "
            "We can choose an alternative scale factor, such as letting one icon represent ten physical items. "
            "Let us recalculate our inventory quantities using this new scale of ten items per icon. "
            "For toys, twenty items divided by ten means we need to draw only two icons. "
            "For board games, thirty items divided by ten requires exactly three icons. "
            "For sports equipment, forty items divided by ten yields four icons. "
            "Under a scale of ten, our entire shop inventory is shown using just two plus three plus four, which equals nine icons. "
            "Notice that changing the scale does not alter the underlying real-world quantities in the slightest. "
            "Twenty toys, thirty games, and forty sports gear items remain identical whether we draw eighteen icons or nine icons. "
            "Choosing an appropriate scale balances visual clarity with drafting efficiency."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed">
            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-700">
                <span class="text-amber-400 font-bold block mb-1">Comparing Scales for the Same Inventory</span>
                <p class="text-slate-300">The underlying data remains constant. Increasing the scale factor reduces the number of icons needed to display the same quantities.</p>
                <div class="overflow-x-auto mt-2">
                    <table class="w-full text-left font-mono text-[11px] text-slate-300 border-collapse">
                        <thead>
                            <tr class="border-b border-slate-700 text-amber-300">
                                <th class="py-1">Category</th>
                                <th class="py-1">Count</th>
                                <th class="py-1 text-center">Scale: 1 = 5</th>
                                <th class="py-1 text-right">Scale: 1 = 10</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-800">
                            <tr><td>Toys</td><td>20</td><td class="text-center font-bold text-sky-400">4 icons</td><td class="text-right font-bold text-emerald-400">2 icons</td></tr>
                            <tr><td>Board Games</td><td>30</td><td class="text-center font-bold text-sky-400">6 icons</td><td class="text-right font-bold text-emerald-400">3 icons</td></tr>
                            <tr><td>Sports Gear</td><td>40</td><td class="text-center font-bold text-sky-400">8 icons</td><td class="text-right font-bold text-emerald-400">4 icons</td></tr>
                            <tr class="border-t border-slate-600 font-bold"><td>Total Icons</td><td>90</td><td class="text-center text-sky-300">18 icons</td><td class="text-right text-emerald-300">9 icons</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
            <div class="p-2.5 rounded-lg bg-sky-500/10 border border-sky-500/30 text-sky-200 text-[11px]">
                <strong>Scaling Principle:</strong> When scale doubles (from 5 to 10), the number of required icons is cut in half (from 18 to 9).
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "If a shop has 50 balls and the scale is 1 icon = 10 balls, how many icons must be drawn?",
                "options": ["5 icons", "10 icons", "50 icons", "2 icons"],
                "answer": 0,
                "explanation": "Divide the total count by the scale factor: 50 ÷ 10 = 5 icons.",
                "hint": "Divide 50 by 10."
            },
            {
                "question": "What happens to the total number of drawn icons if the scale factor of each icon is doubled?",
                "options": [
                    "The number of icons doubles",
                    "The number of icons is halved",
                    "The number of icons stays exactly the same",
                    "The number of icons increases by ten"
                ],
                "answer": 1,
                "explanation": "Because each icon now represents twice as many physical items, only half as many icons are needed to represent the same total.",
                "hint": "If one coin buys double the candy, you need half as many coins."
            }
        ]
    },
    {
        "id": 6,
        "title": "Traffic Tally Pictograph",
        "tagline": "Roadside Vehicle Observation • One Scooter Symbol Represents Three Two-Wheelers",
        "lecture": (
            "Let us apply pictographs to real-world transportation tracking by observing street traffic passing outside a home during rush hour. "
            "A student monitored the flow of two-wheelers, such as scooters and motorcycles, during one morning hour on three different days. "
            "Observations were systematically conducted on Monday, Wednesday, and Friday along the neighborhood main road. "
            "To record the traffic cleanly, the student created a pictograph where one scooter symbol represents three actual two-wheelers. "
            "On Monday, the pictograph displays five scooter symbols. "
            "Multiplying five by three reveals that fifteen two-wheelers passed along the road on Monday morning. "
            "On Wednesday, the road was quieter, and only three scooter symbols were recorded in the observation tally. "
            "Three symbols multiplied by three means nine two-wheelers passed on Wednesday. "
            "On Friday, traffic surged as commuters hurried for weekend errands, resulting in eight scooter symbols. "
            "Eight symbols multiplied by three yields twenty-four two-wheelers on Friday. "
            "By scanning the visual symbols, we instantly spot that Friday experienced the heaviest road traffic of all three days. "
            "The total number of two-wheelers observed across all three days equals fifteen plus nine plus twenty-four, which totals forty-eight vehicles. "
            "Scaled pictographs allow rapid comparison across different observation periods while preserving accurate mathematical data."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed">
            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-700">
                <span class="text-amber-400 font-bold block mb-1">Roadside Traffic Observation Data</span>
                <p class="text-slate-300">A student observed two-wheelers on a street during morning commute hours on three weekdays.</p>
                <div class="mt-2 p-2 rounded bg-amber-500/10 border border-amber-500/30 text-amber-200 font-mono text-[11px] text-center">
                    🛵 Key: 1 Scooter Symbol = 3 Two-Wheelers
                </div>
            </div>
            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-700">
                <span class="text-cyan-400 font-bold block mb-1">Three-Day Traffic Count</span>
                <div class="space-y-1.5 font-mono text-[11px] text-slate-300">
                    <div class="flex justify-between items-center p-1.5 bg-slate-950/80 rounded border border-slate-800">
                        <span>Monday: 5 symbols × 3</span>
                        <span class="text-amber-400 font-bold">15 Two-Wheelers</span>
                    </div>
                    <div class="flex justify-between items-center p-1.5 bg-slate-950/80 rounded border border-slate-800">
                        <span>Wednesday: 3 symbols × 3</span>
                        <span class="text-cyan-400 font-bold">9 Two-Wheelers</span>
                    </div>
                    <div class="flex justify-between items-center p-1.5 bg-slate-950/80 rounded border border-slate-800">
                        <span>Friday: 8 symbols × 3</span>
                        <span class="text-emerald-400 font-bold">24 Two-Wheelers</span>
                    </div>
                </div>
            </div>
            <div class="p-2.5 rounded-lg bg-emerald-500/10 border border-emerald-500/30 text-emerald-200 text-[11px]">
                <strong>Total Observed:</strong> 15 + 9 + 24 = 48 two-wheelers over three morning observation sessions.
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "How many actual two-wheelers passed on Friday if 8 scooter symbols are displayed and 1 symbol = 3 vehicles?",
                "options": ["11 vehicles", "24 vehicles", "16 vehicles", "27 vehicles"],
                "answer": 1,
                "explanation": "Multiply the number of symbols by the scale value: 8 × 3 = 24 vehicles.",
                "hint": "Multiply 8 by 3."
            },
            {
                "question": "How many more two-wheelers passed on Friday (24) than on Wednesday (9)?",
                "options": ["15 vehicles", "12 vehicles", "18 vehicles", "9 vehicles"],
                "answer": 0,
                "explanation": "Subtract Wednesday's count from Friday's count: 24 - 9 = 15 vehicles.",
                "hint": "Calculate 24 minus 9."
            }
        ]
    },
    {
        "id": 7,
        "title": "Road Traffic Comparison",
        "tagline": "Comparative Traffic Analysis • Re-scaling and Fraction Icons",
        "lecture": (
            "Let us deepen our comparative analysis of the traffic pictograph and explore re-scaling with fraction symbols. "
            "We previously determined that fifteen vehicles passed on Monday, nine on Wednesday, and twenty-four on Friday. "
            "Subtracting nine from twenty-four shows that Friday had fifteen more vehicles than Wednesday, which was the quietest day. "
            "What if we choose to redraw this pictograph using a larger scale factor, where one icon represents six two-wheelers? "
            "For Friday's twenty-four vehicles, dividing twenty-four by six gives four complete icons. "
            "For Monday's fifteen vehicles, fifteen divided by six equals two with a remainder of three vehicles. "
            "Since three is exactly half of six, we represent Monday with two full icons plus one half-icon. "
            "For Wednesday's nine vehicles, nine divided by six equals one with a remainder of three vehicles. "
            "Thus Wednesday requires one full icon plus one half-icon to display its traffic accurately. "
            "Half-icons are a standard cartographic convention in pictographs whenever quantities fall halfway between whole multiples. "
            "Using a scale of six requires only four icons for Friday, two and a half for Monday, and one and a half for Wednesday. "
            "Understanding fractional symbols enables accurate visual representation of numbers that do not divide evenly by the chosen scale."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed">
            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-700">
                <span class="text-amber-400 font-bold block mb-1">Re-scaling with a Larger Unit (Scale = 6)</span>
                <p class="text-slate-300">When data counts do not divide evenly by the scale factor, fractional icons represent the remainder.</p>
                <div class="mt-2 p-2 rounded bg-amber-500/10 border border-amber-500/30 text-amber-200 font-mono text-[11px] text-center">
                    🛵 Full Icon = 6 Vehicles | 🛺 Half Icon = 3 Vehicles
                </div>
            </div>
            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-700">
                <span class="text-cyan-400 font-bold block mb-1">Re-scaled Pictograph Representation</span>
                <div class="space-y-1.5 font-mono text-[11px] text-slate-300">
                    <div class="flex justify-between items-center p-1.5 bg-slate-950/80 rounded border border-slate-800">
                        <span>Monday (15): 15 ÷ 6</span>
                        <span class="text-amber-400 font-bold">2½ Icons (6 + 6 + 3)</span>
                    </div>
                    <div class="flex justify-between items-center p-1.5 bg-slate-950/80 rounded border border-slate-800">
                        <span>Wednesday (9): 9 ÷ 6</span>
                        <span class="text-cyan-400 font-bold">1½ Icons (6 + 3)</span>
                    </div>
                    <div class="flex justify-between items-center p-1.5 bg-slate-950/80 rounded border border-slate-800">
                        <span>Friday (24): 24 ÷ 6</span>
                        <span class="text-emerald-400 font-bold">4 Full Icons</span>
                    </div>
                </div>
            </div>
            <div class="p-2.5 rounded-lg bg-sky-500/10 border border-sky-500/30 text-sky-200 text-[11px]">
                <strong>Fractional Principle:</strong> Half of an icon representing 6 equals exactly 3 units.
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "If 1 icon represents 6 vehicles, what quantity does a half-icon represent?",
                "options": ["1 vehicle", "2 vehicles", "3 vehicles", "6 vehicles"],
                "answer": 2,
                "explanation": "Half of the scale value is 6 ÷ 2 = 3 vehicles.",
                "hint": "Divide the full scale value by 2."
            },
            {
                "question": "How many icons represent 18 vehicles when 1 icon = 6 vehicles?",
                "options": ["2 icons", "3 icons", "4 icons", "6 icons"],
                "answer": 1,
                "explanation": "Divide 18 by 6: 18 ÷ 6 = 3 full icons.",
                "hint": "Calculate 18 divided by 6."
            }
        ]
    },
    {
        "id": 8,
        "title": "Icon Daily Schedule",
        "tagline": "Tracking a 24-Hour Day • The One-Icon-Per-Hour Method",
        "lecture": (
            "Every child has exactly twenty-four hours in a day, but how we allocate those hours across activities varies greatly. "
            "To understand time management, students can record their daily routines across standard activities: sleeping, school, studying, playing, eating, and chores. "
            "One student recorded their daily routine using a direct pictorial list, where each icon represents exactly one hour. "
            "For sleeping, the student drew eight bed icons, representing eight hours of restful sleep at night. "
            "For school, six book icons were drawn, accounting for six hours spent in the classroom and morning assembly. "
            "For personal study and homework at home, two pencil icons were recorded, totaling two hours of focused learning. "
            "For eating meals and outdoor play, four ball and plate icons were drawn, representing four hours of nourishment and recreation. "
            "Finally, four clock icons accounted for other routine activities like getting dressed, commuting, and family conversations. "
            "Summing these hours yields eight plus six plus two plus four plus four, which equals exactly twenty-four hours. "
            "This icon method makes it easy to visualize individual hours as tangible blocks across the entire day. "
            "However, counting long rows of identical icons can become tedious when comparing multiple categories quickly."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed">
            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-700">
                <span class="text-amber-400 font-bold block mb-1">The 24-Hour Time Budget Principle</span>
                <p class="text-slate-300">Every single day contains exactly 24 hours. All activities must sum to exactly 24 hours with no unaccounted gaps.</p>
                <div class="mt-2 p-2 rounded bg-amber-500/10 border border-amber-500/30 text-amber-200 font-mono text-[11px] text-center">
                    ⏰ Total Daily Budget: 24 Hours
                </div>
            </div>
            <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-700">
                <span class="text-cyan-400 font-bold block mb-1">The Icon Schedule Method (1 Icon = 1 Hour)</span>
                <div class="space-y-1.5 font-mono text-[11px] text-slate-300">
                    <div class="flex justify-between items-center p-1.5 bg-slate-950/80 rounded border border-slate-800">
                        <span>🛏️ Sleeping: 8 icons</span>
                        <span class="text-indigo-400 font-bold">8 Hours</span>
                    </div>
                    <div class="flex justify-between items-center p-1.5 bg-slate-950/80 rounded border border-slate-800">
                        <span>🏫 School: 6 icons</span>
                        <span class="text-amber-400 font-bold">6 Hours</span>
                    </div>
                    <div class="flex justify-between items-center p-1.5 bg-slate-950/80 rounded border border-slate-800">
                        <span>📖 Self-Study: 2 icons</span>
                        <span class="text-cyan-400 font-bold">2 Hours</span>
                    </div>
                    <div class="flex justify-between items-center p-1.5 bg-slate-950/80 rounded border border-slate-800">
                        <span>⚽ Play & Meals: 4 icons</span>
                        <span class="text-emerald-400 font-bold">4 Hours</span>
                    </div>
                    <div class="flex justify-between items-center p-1.5 bg-slate-950/80 rounded border border-slate-800">
                        <span>⏳ Other Routines: 4 icons</span>
                        <span class="text-rose-400 font-bold">4 Hours</span>
                    </div>
                </div>
            </div>
            <div class="p-2.5 rounded-lg bg-emerald-500/10 border border-emerald-500/30 text-emerald-200 text-[11px]">
                <strong>Check Sum:</strong> 8 + 6 + 2 + 4 + 4 = 24 hours complete.
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "question": "What fraction of the 24-hour day does 8 hours of sleep represent?",
                "options": ["8/24 (or 1/3 of the day)", "8/12 (or 2/3 of the day)", "8/20", "1/4 of the day"],
                "answer": 0,
                "explanation": "8 hours divided by the 24 hours in a full day equals 8/24, which simplifies to 1/3 of the day.",
                "hint": "Divide 8 by 24 and reduce the fraction."
            },
            {
                "question": "If a student spends 6 hours at school and 2 hours on self-study, how many total hours are dedicated to education?",
                "options": ["4 hours", "8 hours", "10 hours", "12 hours"],
                "answer": 1,
                "explanation": "Add school time and study time: 6 + 2 = 8 total educational hours.",
                "hint": "Add 6 and 2."
            }
        ]
    }
]

print("=== VERIFYING PART 1 SLIDES ===")
for s in slides_part1:
    wc = len(s['lecture'].split())
    print(f"Slide {s['id']} ('{s['title']}'): {wc} words")
    assert 195 <= wc <= 215, f"Slide {s['id']} lecture word count {wc} out of range 195-215!"
    assert len(s['checkpoints']) == 2
print("Part 1 verified successfully!")
