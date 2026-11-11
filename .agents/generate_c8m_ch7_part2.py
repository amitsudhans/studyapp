#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 7: Proportional Reasoning-1
Slides Data Generator - Part 2 (Slides 9 to 16)
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Matching Measurement Units",
        "subtitle": "Section 7.4 Unit Consistency (Hours ↔ Minutes, kg ↔ g) & Non-Proportional Inverse Speed-Time Traps",
        "speech": (
            "Avoid TWO deadly everyday calculation errors inside Section Seven Point Four BEFORE ever setting up Trairāśika cross-multiplication: MIXED MEASUREMENT UNITS and INVERSE NON-PROPORTIONAL RELATIONSHIPS! "
            "Rule One, Strict Unit Consistency: NEVER feed mismatched measurement units directly into a proportion! Suppose a laser printer outputs 45 paper sheets in 3 minutes (Pramāṇa = 3 min), and asks how many sheets print across 2 FULL HOURS! Plugging '2' directly alongside '3' produces total mathematical nonsense! Always convert BOTH matching time quantities into identical minutes first: 2 hours = 2 × 60 = 120 minutes! Now apply Rule of Three cleanly: (45 × 120) ÷ 3 = 1,800 sheets! Likewise ALWAYS convert kilograms into grams (1 kg = 1,000 g), kilometres into metres, and rupees into paise cleanly before setting up any ratios! "
            "Rule Two, Spot Inverse Non-Proportional Contexts: Does doubling car SPEED double TRAVEL TIME across a fixed 120 km highway road trip? NEVER—doubling driving speed actually HALVES total road travel time cleanly (at 40 km/h it takes 3 full hours; at 80 km/h it takes only 1.5 hours)! Because product speed × time stays constant fixed trip distance, NEVER blindly apply direct Rule of Three across inverse situations!"
        ),
        "checkpoints": [
            {
                "question": "A rice mill packs 18 kg in 40 minutes. Before using Trairāśika to find kg packed in 2 hours, what MUST you convert first, and what is the answer?",
                "options": [
                    "Convert 2 hours → 120 minutes first;   pack = (18 × 120) ÷ 40 = 54 kg!",
                    "Keep hours directly: (18 × 2) ÷ 40 = 0.9 kg",
                    "Add 18 + 120 = 138 kg",
                    "Multiply 18 × 40 = 720 kg"
                ],
                "answer": 0,
                "hint": "1 hour = 60 minutes, so 2 hours = 120 minutes (triple of 40 minutes → 3 × 18 kg)!",
                "explanation": "Matching units (120 min vs 40 min) scales cleanly by 3× → 54 kg."
            },
            {
                "question": "In which scenario does DIRECT Rule of Three (Trairāśika) FAIL completely because the quantities vary INVERSELY instead?",
                "options": [
                    "Increasing vehicle speed across a FIXED trip distance (faster speed REDUCES travel time!)",
                    "Buying 9 notebooks when 3 notebooks cost ₹75",
                    "Scaling sugar with water volume in lemonade",
                    "Computing travel distance at constant speed over longer time"
                ],
                "answer": 0,
                "hint": "Check which pair has ONE going UP forcing the OTHER going DOWN (fixed product)! ",
                "explanation": "Speed and time for a fixed distance vary inversely (speed × time = distance), unlike direct ratios."
            }
        ]
    },
    {
        "id": 10,
        "title": "Orbits Bricks Markets",
        "subtitle": "Section 7.4 Figure It Out: Orbital Distance, Wall Bricks, Shampoo Unit Prices & Market Value Ratios",
        "speech": (
            "Practice Section Seven Point Four's rich NCERT Figure It Out problems right now—spanning astronomical planetary space orbits, baked clay brick masonry walls, and smart supermarket unit-price value shopping! "
            "Problem One, Planetary Orbital Distance: Moving steadily along its solar orbit, planet Earth sweeps roughly 2.6 × 10⁶ kilometers every single day (while a deep-space probe travels 1,800 km cleanly in 4 minutes)! How far does that spacecraft cruise across 15 straight minutes? By Trairāśika: (1,800 × 15) ÷ 4 = 6,750 km effortlessly! "
            "Problem Two, Brick Wall Construction: If 450 baked clay bricks build a 5-meter garden wall segment cleanly, how many bricks build a full 18-meter boundary wall of identical height and uniform brick thickness? Compute cleanly: (450 × 18) ÷ 5 = 90 × 18 = 1,620 total masonry bricks! "
            "Problem Three, Market Unit-Price Value: Suppose one 100 mL plastic shampoo bottle costs ₹120 (unit cost ₹1.20 per mL), whereas small individual 5 mL shampoo sachets sell cheaply for just ₹4 each! Check 20 small sachets totaling equal 100 mL liquid volume: 20 × ₹4 = ONLY ₹80 (₹0.80 per mL)—proving exact price-per-millilitre unit comparisons consistently expose genuine supermarket consumer savings every single shopping day!"
        ),
        "checkpoints": [
            {
                "question": "A bricklayer uses 480 bricks to build a 4-meter boundary wall section. At the same height and thickness, how many bricks build an 11-meter wall?",
                "options": [
                    "1,320 bricks   [= (480 × 11) ÷ 4 = 120 × 11]",
                    "960 bricks",
                    "1,200 bricks",
                    "1,920 bricks"
                ],
                "answer": 0,
                "hint": "Compute bricks per meter (480 ÷ 4 = 120 bricks/m), then multiply by 11 meters!",
                "explanation": "120 bricks/meter × 11 meters = 1,320 bricks."
            },
            {
                "question": "Shop A sells a 200 mL liquid pack for ₹180; Shop B sells 50 mL sachets at ₹40 each. Which option is better value per 100 mL?",
                "options": [
                    "Shop B is cheaper: ₹80 per 100 mL (vs Shop A's ₹90 per 100 mL)!",
                    "Shop A is cheaper (₹80 per 100 mL)",
                    "Both charge identical ₹90 per 100 mL",
                    "Shop B charges ₹100 per 100 mL"
                ],
                "answer": 0,
                "hint": "Normalize BOTH to equal 100 mL volume: Shop A = ₹180 ÷ 2; Shop B = ₹40 × 2!",
                "explanation": "Shop A = ₹90/100 mL while Shop B = ₹80/100 mL (saves ₹10 per 100 mL)."
            }
        ]
    },
    {
        "id": 11,
        "title": "Sharing In Ratios",
        "subtitle": "Section 7.5 Sharing, Not Equally!: Total Groups (m + n), Unit Group x/(m+n) & Capital Profit Splits",
        "speech": (
            "Enter Section Seven Point Five: SHARING, BUT NOT EQUALLY! Sometimes dividing ₹4,00,000 straight down the middle fifty-fifty is completely UNFAIR! Imagine two business partners launching an electronics shop: Partner One invests ₹3 lakh starting capital, while Partner Two invests ₹5 lakh starting capital! When annual shop profit reaches ₹4,00,000, fair profit sharing proportional to invested capital divides using ratio 3 : 5! "
            "Master the universal GROUP-BASED PARTITIONING METHOD for dividing ANY total quantity x cleanly in specified ratio m : n in three reliable algebraic steps! Step One: calculate TOTAL EQUAL GROUPS by adding both ratio terms together: m + n (here 3 + 5 = EIGHT equal share groups)! Step Two: compute ONE UNIT GROUP SIZE by dividing total quantity cleanly by total groups: x ÷ (m + n) (here ₹4,00,000 ÷ 8 = ₹50,000 per single unit group)! Step Three: multiply each individual recipient's group count directly by that exact unit size! Partner Share One = m × [x ÷ (m+n)] = 3 × 50,000 = ₹1,50,000; Partner Share Two = n × [x ÷ (m+n)] = 5 × 50,000 = ₹2,50,000 (verifying exact combined sum: 1.5 + 2.5 = exact 4 lakh)!"
        ),
        "checkpoints": [
            {
                "question": "Two partners invest ₹4 lakh and ₹6 lakh in a shop (ratio 2 : 3) and earn ₹2,50,000 annual profit. Find each share cleanly:",
                "options": [
                    "₹1,00,000  and  ₹1,50,000   (total groups = 5; unit size = ₹50,000)",
                    "₹1,25,000  and  ₹1,25,000",
                    "₹80,000  and  ₹1,70,000",
                    "₹1,20,000  and  ₹1,30,000"
                ],
                "answer": 0,
                "hint": "Simplify 4 : 6 → 2 : 3; divide ₹2,50,000 by (2 + 3 = 5) groups, then multiply by 2 and 3!",
                "explanation": "₹2,50,000 ÷ 5 = ₹50,000 per group → 2 parts = ₹1,00,000 and 3 parts = ₹1,50,000."
            },
            {
                "question": "Split ₹720 strictly in the ratio 5 : 4 using the Group-Based Partitioning Method:",
                "options": [
                    "₹400  and  ₹320   (9 groups × ₹80/group)",
                    "₹360  and  ₹360",
                    "₹450  and  ₹270",
                    "₹500  and  ₹220"
                ],
                "answer": 0,
                "hint": "Total groups = 5 + 4 = 9; unit group = 720 ÷ 9 = 80!",
                "explanation": "5 × 80 = ₹400 and 4 × 80 = ₹320 (400 + 320 = 720)."
            }
        ]
    },
    {
        "id": 12,
        "title": "Mixtures Paints Batters",
        "subtitle": "Section 7.5 Partition Exercises: Cement-Sand, Acid-Water Solutions, Paint Shades & Idli Batter Ratios",
        "speech": (
            "Practice Section Seven Point Five's practical real-world mixture, currency, and recipe partitions right now—construction masonry mortar, chemistry acid dilutions, house paint shades, and South Indian kitchen idli batter! "
            "Example One, Cement-to-Sand Mortar Ratio: Strong masonry mortar blends dry cement and river sand strictly in ratio 1 : 4! To prepare 75 kg of total dry mortar mix, count 1 + 4 = FIVE groups; unit group size = 75 ÷ 5 = 15 kg! That requires exact 15 kg cement plus 4 × 15 = 60 kg sand! "
            "Example Two, Acid-Water Chemistry Solution: A laboratory beaker holds 600 mL solution at acid-to-water ratio 2 : 3! Dividing 600 ÷ (2 + 3) = 120 mL per group reveals 240 mL acid and 360 mL water! What if you want to dilute acid-to-water cleanly down to 1 : 2 without discarding acid? Keep 240 mL acid steady, set required water = 2 × 240 = 480 mL → pour in 480 − 360 = 120 mL extra water! "
            "Example Three, Idli Batter & Paint Shades: Mixing white and blue paint 5 : 2 across 3.5 L uses exact 2.5 L white + 1 L blue cleanly, and rice-to-urad 3 : 1 keeps fluffy idlis!"
        ),
        "checkpoints": [
            {
                "question": "A 600 mL laboratory mixture has acid : water = 2 : 3 (240 mL acid, 360 mL water). How much EXTRA water makes the ratio cleanly 1 : 2?",
                "options": [
                    "120 mL extra water   (since 240 mL acid needs 2 × 240 = 480 mL water total; 480 − 360 = 120 mL!)",
                    "240 mL extra water",
                    "60 mL extra water",
                    "480 mL extra water"
                ],
                "answer": 0,
                "hint": "Keep existing 240 mL acid unchanged, compute required total water (2 × 240), and subtract existing 360 mL!",
                "explanation": "480 − 360 = 120 mL added water changes ratio 240 : 480 = 1 : 2."
            },
            {
                "question": "Traditional idli batter uses rice : urad dal in ratio 3 : 1 by volume. For 12 cups of combined dry grains, find cups of rice and urad dal:",
                "options": [
                    "9 cups rice  and  3 cups urad dal   (4 groups × 3 cups each)",
                    "8 cups rice  and  4 cups urad dal",
                    "6 cups rice  and  6 cups urad dal",
                    "10 cups rice  and  2 cups urad dal"
                ],
                "answer": 0,
                "hint": "Total groups = 3 + 1 = 4; divide 12 cups ÷ 4 = 3 cups per group!",
                "explanation": "3 × 3 = 9 cups rice and 1 × 3 = 3 cups urad dal."
            }
        ]
    },
    {
        "id": 13,
        "title": "Length Area Volume",
        "subtitle": "Section 7.6 Unit Conversions: Feet-Metres (3.281), Acres/Hectares (43,560 sq ft / 2.471) & Millilitres-cc",
        "speech": (
            "Enter Section Seven Point Six: UNIT CONVERSIONS! Why are international metric and imperial unit conversions literally proportional Trairāśika rules? Because EVERY matching physical measurement pair scales smoothly by one exact constant multiplier! Let us master ALL reference length, surface area, and liquid volume conversion constants clearly right now! "
            "First, Linear Length: ONE standard METRE equals approximately 3.281 FEET! Test quickly: a 10-metre school corridor measures 10 × 3.281 = 32.81 feet end to end! "
            "Second, Land Surface Area (essential across real estate and agriculture!): Squaring linear factor 3.281 × 3.281 yields ONE SQUARE METRE = 10.764 SQUARE FEET (notice you NEVER reuse plain linear 3.281 for square area)! Meanwhile large agricultural land surveys use two standard farm units: ONE ACRE equals exact 43,560 SQUARE FEET, and ONE HECTARE equals 10,000 SQUARE METRES (an exact 100 metre × 100 metre square plot!), which converts smoothly into 2.471 ACRES! Thus a 5-hectare farm spans 5 × 2.471 = 12.355 acres cleanly! "
            "Third, Fluid & Solid Volume: ONE MILLILITRE (1 mL) equals EXACTLY ONE CUBIC CENTIMETRE (1 cc), so ONE full LITRE equals exact 1,000 mL = 1,000 cc cleanly across chemistry laboratory beakers and hospital syringes worldwide!"
        ),
        "checkpoints": [
            {
                "question": "Using 1 hectare = 10,000 sq m = 2.471 acres, convert a 4-hectare agricultural plot into square metres AND into acres:",
                "options": [
                    "40,000 sq metres   and   9.884 acres",
                    "4,000 sq metres   and   9.884 acres",
                    "40,000 sq metres   and   2.471 acres",
                    "400,000 sq metres   and   98.84 acres"
                ],
                "answer": 0,
                "hint": "Multiply BOTH standard conversions cleanly by 4!",
                "explanation": "4 × 10,000 = 40,000 sq m, and 4 × 2.471 = 9.884 acres."
            },
            {
                "question": "Express 3.5 litres cleanly in millilitres (mL) AND cubic centimetres (cc), plus convert 10 sq m to sq feet (1 sq m = 10.764 sq ft):",
                "options": [
                    "3,500 mL = 3,500 cc;   and   107.64 sq feet",
                    "350 mL = 350 cc;   and   32.81 sq feet",
                    "3,500 mL = 350 cc;   and   107.64 sq feet",
                    "35,000 mL = 35,000 cc;   and   1,076.4 sq feet"
                ],
                "answer": 0,
                "hint": "Remember 1 L = 1,000 mL = 1,000 cc, and multiply 10.764 by 10!",
                "explanation": "3.5 L = 3,500 mL = 3,500 cc; 10 × 10.764 = 107.64 sq ft."
            }
        ]
    },
    {
        "id": 14,
        "title": "Temperature Scale Conversion",
        "subtitle": "Section 7.6 Temperature Formulas: F = (9/5)C + 32 & C = (5/9)(F − 32) Shifted Linear Scaling",
        "speech": (
            "Check Section Seven Point Six's most fascinating scale conversion law right now: CELSIUS (°C) versus FAHRENHEIT (°F) TEMPERATURE! Wait—why can't you simply multiply degrees Celsius by ONE pure constant factor like converting metres straight into feet? Look closely at ZERO ON BOTH THERMOMETERS: pure water freezes at ZERO DEGREES CELSIUS, YET on a Fahrenheit thermometer freezing reads THIRTY TWO DEGREES! Because zero origins do NOT align at the same temperature, Celsius and Fahrenheit convert using BOTH proportional interval scaling (9/5 vs 5/9) AND an additive zero offset (±32)! "
            "Inspect exact water freezing-to-boiling span! From ice to boiling steam, Celsius climbs 0° → 100° (100 degree steps), whereas Fahrenheit climbs 32° → 212° (180 degree steps)! Notice span ratio 180 : 100 simplifies cleanly by HCF 20 to NINE TO FIVE (9/5)! "
            "Lock BOTH exact temperature conversion formulas cleanly! Celsius into Fahrenheit: F = (9/5) × C + 32 (test 25°C comfortable indoor room temperature: 9/5 × 25 + 32 = 45 + 32 = 77°F)! Fahrenheit back into Celsius: subtract 32 FIRST before proportional scaling, then multiply cleanly by 5/9: C = (5/9) × (F − 32) (verifying 98.6°F normal human body temperature equals exact 37°C cleanly)!"
        ),
        "checkpoints": [
            {
                "question": "Convert comfortable room temperature 25°C to Fahrenheit using F = (9/5) × C + 32, and convert 104°F back to Celsius:",
                "options": [
                    "25°C = 77°F   and   104°F = 40°C",
                    "25°C = 45°F   and   104°F = 72°C",
                    "25°C = 64°F   and   104°F = 38°C",
                    "25°C = 82°F   and   104°F = 42°C"
                ],
                "answer": 0,
                "hint": "Compute (9/5)×25 = 45, add +32; for 104°F subtract 32 FIRST (104−32 = 72), then multiply by 5/9!",
                "explanation": "45 + 32 = 77°F; (5/9) × (104 − 32) = (5/9) × 72 = 40°C."
            },
            {
                "question": "Why does temperature conversion between °C and °F include '+32' or '−32' alongside the 9:5 scale factor?",
                "options": [
                    "Because 0°C matches 32°F (non-aligned zero freezing point), adding a 32-degree offset on top of the 180:100 = 9:5 degree-size ratio!",
                    "Because Fahrenheit degrees are negative below 100°C",
                    "Because water boils at 32°F",
                    "Because Celsius and Fahrenheit never satisfy a formula"
                ],
                "answer": 0,
                "hint": "Compare freezing points (0°C vs 32°F) and boiling spans (100° steps vs 180° steps)!",
                "explanation": "Degree intervals scale by 9/5 (180/100) while the freezing zero shifts by 32°F."
            }
        ]
    },
    {
        "id": 15,
        "title": "Density Saffron Alloys",
        "subtitle": "Section 7.6 Figure It Out: Population Density, Līlāvatī Saffron, Gold Density, Manure, Tractor & Coin Metal Costs",
        "speech": (
            "Solve Section Seven Point Six's real-world Figure It Out problems blending urban city density, classic Indian texts, gold physics, agriculture, and coin metal alloys! "
            "Problem One, Urban Population Density (residents ÷ sq km): If City A packs 2 crore residents across 1,500 sq km while City B holds 1.26 crore residents across just 600 sq km, City B (21,000 people/sq km) runs dramatically DENSER than City A (~13,333 people/sq km)! "
            "Problem Two, Bhāskarācārya's Līlāvatī Saffron Spice Problem: Ancient Indian merchants scaled costly saffron cleanly via Trairāśika—for example if one-fourth pala of saffron costs 3 coins, 9 full palas cost (3 × 9) ÷ (1/4) = 108 coins cleanly! "
            "Problem Three, Gold Density & Cupro-Nickel Coins: Pure solid gold weighs ~19.3 times as much as an equal volume of pure liquid water (so 100 cc pure water weighs 100 g while 100 cc solid gold weighs 1,930 g)! Meanwhile a cupro-nickel 75% pure copper + 25% pure nickel (3 : 1 mass ratio) 8-gram coin holds 6 g copper plus 2 g nickel, pricing alloy metal costs cleanly! Also analyze organic agricultural manure spread per acre alongside tractor versus oxen field ploughing speed-time scaling carefully across rural farms!"
        ),
        "checkpoints": [
            {
                "question": "If a cupro-nickel coin weighing 12 grams blends Copper : Nickel strictly in the ratio 3 : 1, how many grams of Copper and Nickel does it contain?",
                "options": [
                    "9 g Copper  and  3 g Nickel",
                    "8 g Copper  and  4 g Nickel",
                    "6 g Copper  and  6 g Nickel",
                    "10 g Copper  and  2 g Nickel"
                ],
                "answer": 0,
                "hint": "Total groups = 3 + 1 = 4; unit group = 12 ÷ 4 = 3 grams!",
                "explanation": "3 × 3 = 9 g Copper and 1 × 3 = 3 g Nickel."
            },
            {
                "question": "In Bhāskarācārya's Līlāvatī saffron problem, if 2/5 of a measure of saffron costs 8 coins, what do 3 full measures cost by Trairāśika?",
                "options": [
                    "60 coins   [= (8 × 3) ÷ (2/5) = 24 × (5/2) = 60]",
                    "9.6 coins",
                    "48 coins",
                    "32 coins"
                ],
                "answer": 0,
                "hint": "Set Pramāṇa = 2/5, Phala = 8, Ichchhā = 3 → compute (8 × 3) ÷ (2/5)!",
                "explanation": "1 full measure costs 8 × 5/2 = 20 coins, so 3 measures cost 60 coins."
            }
        ]
    },
    {
        "id": 16,
        "title": "Binairo Chapter Summary",
        "subtitle": "Chapter Summary Consolidation & Puzzle Time ('Binairo / Takuzu' Three Grid Placement Rules)",
        "speech": (
            "Congratulations on mastering NCERT Class Eight Chapter Seven: Proportional Reasoning Part One! Snapshot ALL core formulas cleanly before playing BINAIRO! "
            "Master Checklist: Multiplicative scaling preserves shape while constant addition distorts; ratio a : b reduces by HCF; a : b :: c : d holds iff ad = bc; Trairāśika computes d = (b × c) ÷ a after matching identical units (avoiding inverse traps like speed vs time); Group Partitioning splits x in m : n as m·x/(m+n) and n·x/(m+n); and international unit/temperature formulas bridge measurement systems smoothly! "
            "Now tackle IT'S PUZZLE TIME—BINAIRO (also known globally as TAKUZU)! Played on an even-sized N × N square logic puzzle grid (such as 4×4 or 6×6) using crisp Horizontal bars (—) and Vertical bars (|), obey ALL THREE STRICT PLACEMENT RULES simultaneously: Rule One, EVERY horizontal row and EVERY vertical column contains an EQUAL balanced count of horizontal and vertical line segments (for 6×6 grids: 3 — and 3 |)! Rule Two, NO MORE THAN TWO identical segments can sit consecutively adjacent in any row or column (forbidding ——— or |||)! Rule Three, NO TWO rows can match identically, and NO TWO vertical columns can match identically!"
        ),
        "checkpoints": [
            {
                "question": "In a 6 × 6 Binairo (Takuzu) logic grid using Horizontal (—) and Vertical (|) bars, which THREE placement rules must hold cleanly?",
                "options": [
                    "Equal counts (3 — & 3 |) per row/col; maximum 2 identical adjacent bars; every row unique & every column unique!",
                    "Four identical adjacent bars allowed in every row",
                    "Two identical rows allowed as long as columns differ",
                    "More horizontal bars than vertical bars per row"
                ],
                "answer": 0,
                "hint": "Check Rule 1 (equal counts), Rule 2 (max 2 consecutive identical), and Rule 3 (all rows unique, all cols unique)!",
                "explanation": "Binairo enforces equal balance per row/col, no 3-in-a-row runs, and unique row/column patterns."
            },
            {
                "question": "If you spot '- - ?' inside a Binairo row, what MUST replace '?' immediately by Rule 2 (maximum 2 identical adjacent bars)?",
                "options": [
                    "Vertical bar (|)   — placing another (−) would violate the max-2-adjacent rule!",
                    "Horizontal bar (−)",
                    "Leave it permanently blank",
                    "Any random symbol"
                ],
                "answer": 0,
                "hint": "Three consecutive horizontal bars (— — —) are strictly forbidden!",
                "explanation": "To avoid three identical adjacent segments, the neighbor right after (— —) MUST switch to (|)."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part2)} slides for Ch7 Class 8 Maths Part 2.")
    for s in slides_part2:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: {s['title']!r} ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Slide {s['id']} title length {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 2 assertions passed cleanly!")
