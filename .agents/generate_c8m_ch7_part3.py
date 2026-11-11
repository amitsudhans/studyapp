#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 7: Proportional Reasoning-1
Slides Data Generator - Part 3 (Exercise & Mastery Challenge Slides 17 to 20: 40 Questions)
Zero speech narration on quiz slides, zero fictional human names, 3-step breakdown per question.
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Scaling Ratios Quiz",
        "subtitle": "Challenge Arena 1 (10 MCQs): Image Resizing, Multiplicative vs Additive Change, Terms, Simplest Form & :: Proportions",
        "questions": [
            {
                "question": "An artist's tiger photo measures 8 cm wide by 6 cm tall. Which resized banner preserves true proportional similarity without distortion?",
                "options": [
                    "20 cm wide × 15 cm tall   (both scaled cleanly by ×2.5)",
                    "16 cm wide × 14 cm tall   (+8 cm added to both!)",
                    "16 cm wide × 6 cm tall",
                    "20 cm wide × 12 cm tall"
                ],
                "answer": 0,
                "hint": "Check which pair shares original simplest ratio 8 : 6 = 4 : 3!",
                "explanation": "20 : 15 reduces cleanly (÷5) to 4 : 3 matching original 8 : 6 = 4 : 3.",
                "solution_steps": [
                    "Reduce original dimensions by HCF(8, 6) = 2: ratio = 4 : 3.",
                    "Test Option 1 (20 : 15) ÷ 5 = 4 : 3 (exact match!).",
                    "Reject additive 16:14 (8:7) and unequal scaling."
                ]
            },
            {
                "question": "A 10 cm × 4 cm photo is enlarged by ADDING +6 cm to BOTH width and height (becoming 16 cm × 10 cm). Why does this distort the picture?",
                "options": [
                    "The original 5 : 2 ratio (2.5× wide) alters to 8 : 5 (1.6× wide) — additive change breaks multiplicative aspect similarity!",
                    "Because addition always makes width smaller than height",
                    "Because 16 × 10 = 160",
                    "Adding +6 always keeps exact similarity"
                ],
                "answer": 0,
                "hint": "Compare original aspect 10 ÷ 4 = 2.5 against new aspect 16 ÷ 10 = 1.6!",
                "explanation": "Height multiplied ×2.5 (4 → 10) while width only multiplied ×1.6 (10 → 16), squashing proportions horizontally.",
                "solution_steps": [
                    "Compute original ratio 10 : 4 = 5 : 2 (2.5).",
                    "Compute new ratio 16 : 10 = 8 : 5 (1.6).",
                    "Since 5 : 2 ≠ 8 : 5, equal additive growth breaks visual similarity."
                ]
            },
            {
                "question": "Reduce ratio 84 : 126 completely to its simplest form using HCF(84, 126):",
                "options": [
                    "2 : 3   (dividing both by HCF = 42)",
                    "4 : 6",
                    "14 : 21",
                    "3 : 2"
                ],
                "answer": 0,
                "hint": "Divide both 84 and 126 cleanly by 42 (notice 84 = 2 × 42 and 126 = 3 × 42)!",
                "explanation": "HCF(84, 126) = 42; 84÷42 = 2 and 126÷42 = 3 → simplest form 2 : 3.",
                "solution_steps": [
                    "Factorize 84 = 42 × 2 and 126 = 42 × 3 (HCF = 42).",
                    "Divide both terms cleanly by 42.",
                    "Obtain simplest coprime ratio 2 : 3."
                ]
            },
            {
                "question": "Which pair of ratios forms a TRUE four-dot proportion (a : b :: c : d)?",
                "options": [
                    "14 : 21 :: 26 : 39   (both simplify cleanly to 2 : 3!)",
                    "14 : 21 :: 20 : 27",
                    "12 : 18 :: 16 : 20",
                    "9 : 12 :: 12 : 15"
                ],
                "answer": 0,
                "hint": "Simplify BOTH ratios in each pair by their respective HCFs until simplest forms match!",
                "explanation": "14:21 (÷7) = 2:3 and 26:39 (÷13) = 2:3 — identical simplest forms.",
                "solution_steps": [
                    "Reduce 14 : 21 by HCF 7 → 2 : 3.",
                    "Reduce 26 : 39 by HCF 13 → 2 : 3.",
                    "Identical simplest form confirms 14 : 21 :: 26 : 39."
                ]
            },
            {
                "question": "Find missing value x in proportion 15 : x :: 25 : 40:",
                "options": [
                    "x = 24",
                    "x = 30",
                    "x = 16",
                    "x = 20"
                ],
                "answer": 0,
                "hint": "Reduce 25 : 40 to 5 : 8 first (÷5), OR cross-multiply 25 × x = 15 × 40!",
                "explanation": "25x = 600 → x = 24 (15:24 and 25:40 both simplify to 5:8!).",
                "solution_steps": [
                    "Reduce right ratio 25 : 40 by HCF 5 → 5 : 8.",
                    "Match 15 : x :: 5 : 8 (15 = 5 × 3).",
                    "Multiply second term by 3: x = 8 × 3 = 24."
                ]
            },
            {
                "question": "Which statement accurately describes the FIRST and SECOND terms of ratio 7 : 3?",
                "options": [
                    "First term = 7, second term = 3; for every 7 units of the first quantity, there are 3 units of the second (reversing to 3 : 7 changes the meaning completely!)",
                    "7 : 3 equals 3 : 7 identically",
                    "Both terms equal 10",
                    "Second term must always be larger than first term"
                ],
                "answer": 0,
                "hint": "Order inside ratio notation a : b cannot be swapped without reversing the quantities!",
                "explanation": "Order defines meaning strictly: 7 parts first quantity per 3 parts second quantity.",
                "solution_steps": [
                    "Identify position 1 (7) and position 2 (3).",
                    "Notice 7 : 3 > 1 whereas 3 : 7 < 1.",
                    "Confirm order sensitivity and unit-pair interpretation."
                ]
            },
            {
                "question": "In a school mural, width : height = 7 : 5. If the painted height measures 35 cm, what width preserves true proportional similarity?",
                "options": [
                    "49 cm   [factor = 35 ÷ 5 = 7 → 7 × 7 = 49 cm]",
                    "37 cm   [adding +30 to both!]",
                    "25 cm",
                    "42 cm"
                ],
                "answer": 0,
                "hint": "Multiply width term 7 by scaling factor 35 ÷ 5 = 7!",
                "explanation": "Height multiplied ×7 (5 → 35), so width multiplies ×7 (7 → 49 cm).",
                "solution_steps": [
                    "Compute scale multiplier from height: k = 35 ÷ 5 = 7.",
                    "Apply identical multiplier to width: 7 × 7 = 49 cm.",
                    "Check simplest form 49 : 35 (÷7) = 7 : 5."
                ]
            },
            {
                "question": "Why are 18 : 24 and 27 : 36 proportional even though neither 18 divides 27 cleanly as a whole number?",
                "options": [
                    "Because dividing 18:24 by HCF 6 gives 3:4, and dividing 27:36 by HCF 9 ALSO gives 3:4 (equivalently ×1.5 scale factor!)",
                    "Because 27 − 18 equals 36 − 24",
                    "Because both numbers end in even digits",
                    "They are NOT proportional"
                ],
                "answer": 0,
                "hint": "Reduce BOTH ratios to simplest form (or check 18 × 1.5 = 27 and 24 × 1.5 = 36)!",
                "explanation": "Shared simplest form 3 : 4 (and factor k = 3/2 = 1.5) establishes exact proportion 18 : 24 :: 27 : 36.",
                "solution_steps": [
                    "Simplify 18 : 24 by HCF 6 → 3 : 4.",
                    "Simplify 27 : 36 by HCF 9 → 3 : 4.",
                    "Confirm factor 1.5 (3/2) scales both terms equally."
                ]
            },
            {
                "question": "Express 750 g : 2 kg in its true simplest form:",
                "options": [
                    "3 : 8   (convert 2 kg → 2,000 g first; divide 750 : 2,000 by HCF = 250!)",
                    "375 : 1",
                    "75 : 2",
                    "15 : 4"
                ],
                "answer": 0,
                "hint": "Convert kilograms to grams (1 kg = 1,000 g → 2,000 g) BEFORE simplifying!",
                "explanation": "750 g : 2,000 g ÷ 250 = 3 : 8 cleanly.",
                "solution_steps": [
                    "Convert units consistently: 2 kg = 2,000 g.",
                    "Form matching-unit ratio 750 : 2,000.",
                    "Divide both terms by HCF 250 → 3 : 8."
                ]
            },
            {
                "question": "Which digital photo crop scales 1,200 px × 800 px down by constant factor 1/4 while preserving exact shape?",
                "options": [
                    "300 px × 200 px",
                    "900 px × 500 px   (subtracted 300 px from both!)",
                    "400 px × 200 px",
                    "300 px × 400 px"
                ],
                "answer": 0,
                "hint": "Divide BOTH 1,200 and 800 by 4!",
                "explanation": "1,200 ÷ 4 = 300 px and 800 ÷ 4 = 200 px (maintaining exact 3 : 2 aspect ratio).",
                "solution_steps": [
                    "Compute scaled width: 1,200 × (1/4) = 300 px.",
                    "Compute scaled height: 800 × (1/4) = 200 px.",
                    "Check aspect: 300 : 200 = 3 : 2 matches 1,200 : 800 = 3 : 2."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Trairasika Mixture Quiz",
        "subtitle": "Challenge Arena 2 (10 MCQs): Trairāśika Rule of Three, Age Non-Proportionality, Coffee Mixtures, Orbits & Markets",
        "questions": [
            {
                "question": "In Trairāśika, if 9 bricks weigh 27 kg (actually say 9 kg for 4 bricks: pramāṇa = 4 bricks, phala = 9 kg), what do 16 bricks weigh?",
                "options": [
                    "36 kg   [ichchhāphala = (9 × 16) ÷ 4 = 36 kg]",
                    "21 kg",
                    "72 kg",
                    "40 kg"
                ],
                "answer": 0,
                "hint": "Multiply phala (9) by ichchhā (16), then divide cleanly by pramāṇa (4)!",
                "explanation": "(9 × 16) ÷ 4 = 144 ÷ 4 = 36 kg.",
                "solution_steps": [
                    "Set Trairāśika: pramāṇa = 4 bricks, phala = 9 kg, ichchhā = 16 bricks.",
                    "Compute ichchhāphala = (phala × ichchhā) ÷ pramāṇa = (9 × 16) ÷ 4.",
                    "Divide 144 ÷ 4 = 36 kg."
                ]
            },
            {
                "question": "A parent is 40 years old and a child is 8 years old (5 : 1 ratio). After 8 years, what is the NEW age ratio?",
                "options": [
                    "3 : 1   (ages become 48 and 16 → 48 ÷ 16 = 3 : 1, breaking proportionality!)",
                    "5 : 1",
                    "6 : 1",
                    "2 : 1"
                ],
                "answer": 0,
                "hint": "Add +8 years to BOTH ages cleanly (40+8 = 48, 8+8 = 16), then simplify 48 : 16!",
                "explanation": "8 years later ages are 48 and 16, changing the ratio from 5:1 down to 3:1.",
                "solution_steps": [
                    "Add 8 years to both: parent = 48, child = 16.",
                    "Form new ratio 48 : 16.",
                    "Reduce by HCF 16 → 3 : 1 (proving additive changes alter ratios)."
                ]
            },
            {
                "question": "Compare two filter coffee jugs: Jug P blends 45 mL decoction with 135 mL milk; Jug Q blends 40 mL decoction with 160 mL milk. Which jug is STRONGER?",
                "options": [
                    "Jug P   (45:135 = 1 : 3 → 25% decoction, stronger than Jug Q's 40:160 = 1 : 4 → 20%!)",
                    "Jug Q   (1 : 4 is stronger than 1 : 3)",
                    "Both are identically strong",
                    "Jug P has 33.3% milk"
                ],
                "answer": 0,
                "hint": "Reduce BOTH ratios (45 : 135 and 40 : 160) to 1 : m and compare milk per 1 unit decoction!",
                "explanation": "Jug P (1 : 3) packs less milk per unit decoction (stronger coffee) than Jug Q (1 : 4).",
                "solution_steps": [
                    "Simplify Jug P: 45 : 135 ÷ 45 = 1 : 3 (1/4 = 25% decoction).",
                    "Simplify Jug Q: 40 : 160 ÷ 40 = 1 : 4 (1/5 = 20% decoction).",
                    "Compare: 25% > 20% → Jug P tastes stronger."
                ]
            },
            {
                "question": "A car moving at steady speed covers 150 km in 2 hours 30 minutes. Using consistent units, how far does it travel in 4 hours?",
                "options": [
                    "240 km   (2 h 30 min = 150 min → 1 km/min; 4 h = 240 min → 240 km!)",
                    "200 km",
                    "300 km",
                    "180 km"
                ],
                "answer": 0,
                "hint": "Convert BOTH times cleanly into minutes (150 min vs 240 min) before setting up Trairāśika!",
                "explanation": "150 km / 150 min = 1 km/min; across 240 min = 240 km.",
                "solution_steps": [
                    "Convert 2 h 30 min = 150 minutes, and 4 h = 240 minutes.",
                    "Apply Trairāśika: (150 × 240) ÷ 150.",
                    "Cancel 150 cleanly → 240 km."
                ]
            },
            {
                "question": "Wait—if a cyclist rides a FIXED 60 km trail at 15 km/h taking 4 hours, can we use direct Rule of Three to claim riding at 30 km/h takes 8 hours?",
                "options": [
                    "NO — doubling speed over a fixed distance HALVES travel time to 2 hours (inverse relationship, NOT direct proportion!)",
                    "YES — double speed always doubles travel time",
                    "YES — if distance stays 60 km",
                    "Riding at 30 km/h takes 6 hours"
                ],
                "answer": 0,
                "hint": "Compute actual travel time = Distance ÷ Speed = 60 ÷ 30!",
                "explanation": "Speed and time for a fixed distance are inversely proportional (15×4 = 30×2 = 60 km).",
                "solution_steps": [
                    "Notice distance 60 km stays constant (speed × time = 60).",
                    "Compute new time at 30 km/h: 60 ÷ 30 = 2 hours (dropped by half!).",
                    "Confirm direct Rule of Three fails whenever two quantities vary inversely."
                ]
            },
            {
                "question": "An artificial satellite sweeps 27,000 km along its orbit in 6 minutes. At uniform speed, how far does it sweep in 10 minutes?",
                "options": [
                    "45,000 km   [= (27,000 × 10) ÷ 6]",
                    "31,000 km",
                    "40,500 km",
                    "54,000 km"
                ],
                "answer": 0,
                "hint": "Divide 27,000 ÷ 6 = 4,500 km/minute, then multiply by 10 minutes!",
                "explanation": "4,500 km/min × 10 min = 45,000 km.",
                "solution_steps": [
                    "Find distance per minute: 27,000 ÷ 6 = 4,500 km/min.",
                    "Multiply by 10 minutes: 4,500 × 10.",
                    "Obtain 45,000 km."
                ]
            },
            {
                "question": "A supermarket offers 3 shampoo packaging options:\n• Pack A: 50 mL for ₹45\n• Pack B: 180 mL for ₹144\n• Pack C: 250 mL for ₹225.\nWhich option gives the LOWEST price per millilitre?",
                "options": [
                    "Pack B   (₹144 ÷ 180 = ₹0.80/mL, cheaper than ₹0.90/mL in A & C!)",
                    "Pack A   (₹0.90/mL)",
                    "Pack C   (₹0.90/mL)",
                    "All three cost ₹0.85/mL"
                ],
                "answer": 0,
                "hint": "Compute price ÷ mL cleanly for each package!",
                "explanation": "Pack A: 45/50 = ₹0.90/mL; Pack B: 144/180 = ₹0.80/mL; Pack C: 225/250 = ₹0.90/mL.",
                "solution_steps": [
                    "Unit rate A: ₹45 ÷ 50 mL = ₹0.90/mL.",
                    "Unit rate B: ₹144 ÷ 180 mL = ₹0.80/mL.",
                    "Unit rate C: ₹225 ÷ 250 mL = ₹0.90/mL → Pack B wins lowest unit cost!"
                ]
            },
            {
                "question": "To keep lemonade sweetness identical across 3 litres of water (if 200 mL water uses 25 g sugar), how much sugar is needed? (1 L = 1,000 mL)",
                "options": [
                    "375 g sugar   (convert 3 L → 3,000 mL = 15 × 200 mL → 15 × 25 g = 375 g!)",
                    "37.5 g sugar",
                    "75 g sugar",
                    "500 g sugar"
                ],
                "answer": 0,
                "hint": "Convert 3 L = 3,000 mL first; find scale factor 3,000 ÷ 200 = 15!",
                "explanation": "15 batches of 200 mL require 15 × 25 g = 375 g sugar.",
                "solution_steps": [
                    "Match units: 3 L = 3,000 mL.",
                    "Scale factor: 3,000 ÷ 200 = 15×.",
                    "Compute sugar: 15 × 25 g = 375 g."
                ]
            },
            {
                "question": "If 7 cement bags reinforce 10.5 metres of retaining wall, how many bags maintain identical wall strength across 18 metres?",
                "options": [
                    "12 bags   [= (7 × 18) ÷ 10.5 = 126 ÷ 10.5]",
                    "14.5 bags",
                    "10 bags",
                    "15 bags"
                ],
                "answer": 0,
                "hint": "Notice 7 : 10.5 simplifies to 2 : 3 (10.5 = 1.5 × 7); solve 18 ÷ 1.5!",
                "explanation": "(7 × 18) ÷ 10.5 = 126 ÷ 10.5 = 12 bags (12 : 18 = 2 : 3).",
                "solution_steps": [
                    "Notice ratio 7 : 10.5 = 1 : 1.5 = 2 : 3.",
                    "Apply Trairāśika: (7 × 18) ÷ 10.5 = 126 ÷ 10.5.",
                    "Simplify cleanly: 12 cement bags."
                ]
            },
            {
                "question": "Solve for pramāṇa 'a' if a : 15 :: 28 : 35:",
                "options": [
                    "a = 12",
                    "a = 10",
                    "a = 14",
                    "a = 8"
                ],
                "answer": 0,
                "hint": "Reduce 28 : 35 by HCF 7 first (= 4 : 5), then match a : 15 :: 4 : 5!",
                "explanation": "28:35 = 4:5; multiplying by 3 gives 12:15 → a = 12.",
                "solution_steps": [
                    "Simplify 28 : 35 by dividing both by 7 → 4 : 5.",
                    "Set a : 15 :: 4 : 5 (15 = 5 × 3).",
                    "Compute a = 4 × 3 = 12 (check 12×35 = 420 = 15×28!)."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Sharing Conversions Quiz",
        "subtitle": "Challenge Arena 3 (10 MCQs): Group Partitioning Method, Mixture Adjustments, Length/Area/Volume & Temperature Scales",
        "questions": [
            {
                "question": "Split ₹2,400 between two school clubs in the ratio 3 : 5 using the Group-Based Partitioning Method:",
                "options": [
                    "₹900  and  ₹1,500   (total groups = 8; unit size = ₹300)",
                    "₹1,000  and  ₹1,400",
                    "₹800  and  ₹1,600",
                    "₹1,200  and  ₹1,200"
                ],
                "answer": 0,
                "hint": "Compute total groups (3 + 5 = 8), divide 2,400 ÷ 8 = 300, then multiply by 3 and 5!",
                "explanation": "3 × 300 = ₹900 and 5 × 300 = ₹1,500 (900 + 1,500 = 2,400).",
                "solution_steps": [
                    "Determine total equal groups: 3 + 5 = 8.",
                    "Compute unit group size: ₹2,400 ÷ 8 = ₹300.",
                    "Allocate shares: 3 × 300 = ₹900 and 5 × 300 = ₹1,500."
                ]
            },
            {
                "question": "A decorator mixes green paint using Yellow : Blue = 4 : 3. To prepare 35 litres of paint, how many litres of Blue paint are required?",
                "options": [
                    "15 litres Blue   (total 7 groups × 5 L/group → 3 × 5 = 15 L Blue, 20 L Yellow)",
                    "20 litres Blue",
                    "12 litres Blue",
                    "18 litres Blue"
                ],
                "answer": 0,
                "hint": "Notice 4 + 3 = 7 total groups; 35 ÷ 7 = 5 litres per group; Blue takes 3 groups!",
                "explanation": "Unit group = 5 L; Blue share = 3 × 5 = 15 L.",
                "solution_steps": [
                    "Add ratio parts: 4 + 3 = 7 total groups.",
                    "Unit group size: 35 ÷ 7 = 5 litres.",
                    "Blue share = 3 × 5 = 15 litres."
                ]
            },
            {
                "question": "Convert a room floor area of 20 square metres into square feet (using 1 sq m = 10.764 sq ft):",
                "options": [
                    "215.28 sq feet",
                    "65.62 sq feet   (used linear factor 3.281 instead of squared 10.764!)",
                    "200 sq feet",
                    "107.64 sq feet"
                ],
                "answer": 0,
                "hint": "Multiply 20 directly by area factor 10.764 sq ft/sq m!",
                "explanation": "20 × 10.764 = 215.28 sq feet (note 3.281² = 10.764).",
                "solution_steps": [
                    "Select area conversion factor: 1 sq m = 10.764 sq ft.",
                    "Multiply cleanly: 20 × 10.764.",
                    "Obtain 215.28 sq feet."
                ]
            },
            {
                "question": "A rectangular sports complex covers 2 acres. Using 1 acre = 43,560 sq ft, how many total square feet does it span?",
                "options": [
                    "87,120 sq feet",
                    "20,000 sq feet",
                    "43,560 sq feet",
                    "8,712 sq feet"
                ],
                "answer": 0,
                "hint": "Double 43,560 sq ft carefully!",
                "explanation": "2 × 43,560 = 87,120 sq feet.",
                "solution_steps": [
                    "Recall 1 acre = 43,560 sq ft.",
                    "Multiply by 2 acres: 2 × 43,560.",
                    "Result: 87,120 sq feet."
                ]
            },
            {
                "question": "Convert fever reading 102.2°F cleanly into degrees Celsius using C = (5/9) × (F − 32):",
                "options": [
                    "39°C   [= (5/9) × (102.2 − 32) = (5/9) × 70.2 = 39]",
                    "37°C",
                    "41°C",
                    "38°C"
                ],
                "answer": 0,
                "hint": "Subtract 32 first: 102.2 − 32 = 70.2, then multiply by 5 and divide by 9!",
                "explanation": "70.2 ÷ 9 = 7.8; 7.8 × 5 = 39°C.",
                "solution_steps": [
                    "Subtract 32: 102.2 − 32 = 70.2.",
                    "Divide by 9: 70.2 ÷ 9 = 7.8.",
                    "Multiply by 5: 7.8 × 5 = 39°C."
                ]
            },
            {
                "question": "Convert outdoor summer temperature 45°C into Fahrenheit using F = (9/5) × C + 32:",
                "options": [
                    "113°F   [= (9/5) × 45 + 32 = 81 + 32]",
                    "98.6°F",
                    "104°F",
                    "122°F"
                ],
                "answer": 0,
                "hint": "Compute (9/5) × 45 = 9 × 9 = 81, then add 32!",
                "explanation": "81 + 32 = 113°F.",
                "solution_steps": [
                    "Multiply 45 × (9/5) = 9 × 9 = 81.",
                    "Add freezing offset +32.",
                    "81 + 32 = 113°F."
                ]
            },
            {
                "question": "Which volume equality is 100% EXACT across medical syringes and cubic centimetres (cc)?",
                "options": [
                    "2.4 litres = 2,400 mL = 2,400 cc   (since 1 mL = 1 cc and 1 L = 1,000 mL)",
                    "2.4 litres = 240 cc",
                    "1 mL = 1,000 cc",
                    "1 litre = 100 cc"
                ],
                "answer": 0,
                "hint": "Apply 1 mL = 1 cc and 1 L = 1,000 mL cleanly to 2.4 litres!",
                "explanation": "2.4 × 1,000 = 2,400 mL = 2,400 cc.",
                "solution_steps": [
                    "Convert litres to millilitres: 2.4 × 1,000 = 2,400 mL.",
                    "Use exact equivalence 1 mL = 1 cc.",
                    "Confirm 2,400 mL = 2,400 cc."
                ]
            },
            {
                "question": "A 60-metre running track converts to how many feet using 1 metre = 3.281 feet?",
                "options": [
                    "196.86 feet",
                    "180 feet",
                    "645.84 feet",
                    "19.686 feet"
                ],
                "answer": 0,
                "hint": "Multiply 60 × 3.281 carefully!",
                "explanation": "60 × 3.281 = 6 × 32.81 = 196.86 feet.",
                "solution_steps": [
                    "Recall length factor: 1 m = 3.281 ft.",
                    "Multiply 60 × 3.281 = 6 × 32.81.",
                    "Obtain 196.86 feet."
                ]
            },
            {
                "question": "Three brothers share an inheritance of ₹9,00,000 in the extended ratio 2 : 3 : 4. Find the largest brother's share:",
                "options": [
                    "₹4,00,000   (total groups = 2+3+4 = 9; unit size = ₹1,00,000 × 4)",
                    "₹3,00,000",
                    "₹4,50,000",
                    "₹5,00,000"
                ],
                "answer": 0,
                "hint": "Total groups = 2 + 3 + 4 = 9; unit group = ₹9,00,000 ÷ 9!",
                "explanation": "9 groups of ₹1,00,000 give shares ₹2L, ₹3L, and ₹4L.",
                "solution_steps": [
                    "Sum ratio terms: 2 + 3 + 4 = 9 groups.",
                    "Unit group = ₹9,00,000 ÷ 9 = ₹1,00,000.",
                    "Largest share (4 groups) = ₹4,00,000."
                ]
            },
            {
                "question": "A 40 kg dry cement-sand mortar mix blends cement : sand = 1 : 3 (10 kg cement, 30 kg sand). How many kg of EXTRA cement shift the ratio cleanly to 1 : 2?",
                "options": [
                    "5 kg extra cement   (since 30 kg sand ÷ 2 = 15 kg cement needed; 15 − 10 = 5 kg!)",
                    "10 kg extra cement",
                    "15 kg extra cement",
                    "2.5 kg extra cement"
                ],
                "answer": 0,
                "hint": "Keep existing 30 kg sand steady; for 1 : 2 ratio, cement must be half of 30 kg (= 15 kg)!",
                "explanation": "Total cement needed = 15 kg; adding 5 kg onto existing 10 kg achieves 15 : 30 = 1 : 2.",
                "solution_steps": [
                    "Find current quantities in 40 kg (1:3): 10 kg cement and 30 kg sand.",
                    "Keep 30 kg sand unchanged; target ratio 1:2 needs 30 ÷ 2 = 15 kg cement.",
                    "Subtract existing cement: 15 − 10 = 5 kg extra cement."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Mastery Challenge Quiz",
        "subtitle": "Challenge Arena 4 (10 MCQs): Density, Līlāvatī Saffron, Alloys, Farm Ploughing, Tap Rates & Binairo Puzzles",
        "questions": [
            {
                "question": "Delhi holds ~2,00,00,000 residents across 1,500 sq km, while Mumbai holds ~1,26,00,000 across 600 sq km. Compare population densities (people / sq km):",
                "options": [
                    "Mumbai (~21,000/sq km) is significantly denser than Delhi (~13,333/sq km)!",
                    "Delhi (~21,000/sq km) is denser than Mumbai",
                    "Both have identical density",
                    "Mumbai density is 1,260/sq km"
                ],
                "answer": 0,
                "hint": "Divide population cleanly by area for BOTH cities: 20,000,000 ÷ 1,500 vs 12,600,000 ÷ 600!",
                "explanation": "Mumbai = 12,600,000 / 600 = 21,000 people/sq km vs Delhi = 20,000,000 / 1,500 ≈ 13,333 people/sq km.",
                "solution_steps": [
                    "Compute Delhi density: 2,00,00,000 ÷ 1,500 = 2,00,000 ÷ 15 ≈ 13,333/sq km.",
                    "Compute Mumbai density: 1,26,00,000 ÷ 600 = 1,26,000 ÷ 6 = 21,000/sq km.",
                    "Conclude Mumbai carries higher population density per sq km."
                ]
            },
            {
                "question": "If gold has 19.3 times the mass of an equal volume of water (and silver has 10.5 times water's mass), what does a 200 cc solid bar of pure gold weigh? (1 cc water = 1 g)",
                "options": [
                    "3,860 g (= 3.86 kg)   [since 200 g × 19.3 = 3,860 g!]",
                    "1,930 g",
                    "2,100 g",
                    "386 g"
                ],
                "answer": 0,
                "hint": "First note 200 cc water weighs 200 g, then scale proportionally by ×19.3!",
                "explanation": "200 cc × 1 g/cc × 19.3 = 3,860 g = 3.86 kg.",
                "solution_steps": [
                    "Equal volume of water (200 cc) weighs 200 g.",
                    "Scale by gold's relative density factor 19.3: 200 × 19.3.",
                    "Compute cleanly: 20 × 193 = 3,860 g = 3.86 kg."
                ]
            },
            {
                "question": "A farmer spreads 400 kg of organic manure evenly per 0.5 acre. Using 1 hectare = 2.471 acres, how much manure covers 1 full hectare?",
                "options": [
                    "1,976.8 kg   (since 800 kg/acre × 2.471 acres = 1,976.8 kg)",
                    "988.4 kg",
                    "800 kg",
                    "4,942 kg"
                ],
                "answer": 0,
                "hint": "Find rate per 1 full acre first (400 × 2 = 800 kg/acre), then multiply by 2.471 acres!",
                "explanation": "800 kg/acre × 2.471 acres = 1,976.8 kg per hectare.",
                "solution_steps": [
                    "Compute rate per whole acre: 400 ÷ 0.5 = 800 kg/acre.",
                    "Convert 1 hectare = 2.471 acres.",
                    "Multiply: 800 × 2.471 = 1,976.8 kg."
                ]
            },
            {
                "question": "A cupro-nickel 5-gram coin contains 75% Copper (3 parts) and 25% Nickel (1 part). If Copper costs ₹800/kg and Nickel costs ₹1,600/kg, find the metal cost of 1,000 coins (5 kg total):",
                "options": [
                    "₹5,000   (3.75 kg Copper × ₹800 = ₹3,000   +   1.25 kg Nickel × ₹1,600 = ₹2,000!)",
                    "₹4,000",
                    "₹6,000",
                    "₹4,800"
                ],
                "answer": 0,
                "hint": "Split 5 kg alloy cleanly in 3 : 1 ratio (3.75 kg Copper, 1.25 kg Nickel), then multiply by kg prices!",
                "explanation": "3.75 × 800 = ₹3,000 Copper + 1.25 × 1,600 = ₹2,000 Nickel = ₹5,000 total.",
                "solution_steps": [
                    "Total coin batch mass = 1,000 × 5 g = 5,000 g = 5 kg.",
                    "Split 5 kg in 3 : 1 (÷4 = 1.25 kg): Copper = 3.75 kg, Nickel = 1.25 kg.",
                    "Compute metal cost: (3.75 × 800) + (1.25 × 1,600) = 3,000 + 2,000 = ₹5,000."
                ]
            },
            {
                "question": "A tractor ploughs a field 4 times faster than a pair of oxen. If the oxen take 12 hours to finish the field, how long does the tractor take (and why can't direct Rule of Three say 48 hours)?",
                "options": [
                    "3 hours (= 12 ÷ 4) — ploughing speed and completion time are INVERSELY proportional!",
                    "48 hours (= 12 × 4)",
                    "6 hours",
                    "4 hours"
                ],
                "answer": 0,
                "hint": "Working 4× FASTER divides total completion time by 4 (never multiplies time by 4!)",
                "explanation": "Inverse relationship: 4× higher speed reduces time from 12 hours to 12 ÷ 4 = 3 hours.",
                "solution_steps": [
                    "Identify inverse variation: Speed × Time = Fixed Field Area.",
                    "Scale speed by ×4 → divide time by 4: 12 ÷ 4 = 3 hours.",
                    "Reject direct Trairāśika 12 × 4 = 48 hours (which would mean faster machines take longer!)."
                ]
            },
            {
                "question": "In Bhāskarācārya's Līlāvatī saffron example, if 3/8 pala of saffron costs 6 coins, how much saffron can be bought for 16 coins?",
                "options": [
                    "1 full pala   [ichchhā = (3/8 × 16) ÷ 6 = 6 ÷ 6 = 1!]",
                    "2 palas",
                    "3/4 pala",
                    "1.5 palas"
                ],
                "answer": 0,
                "hint": "Set up 3/8 : 6 :: d : 16 and solve 6d = (3/8) × 16!",
                "explanation": "(3/8) × 16 = 6; dividing by 6 coins yields exact 1 pala.",
                "solution_steps": [
                    "Write proportion: (3/8 pala) : 6 coins :: d palas : 16 coins.",
                    "Cross-multiply: 6 × d = (3/8) × 16 = 6.",
                    "Solve cleanly: d = 6 ÷ 6 = 1 pala."
                ]
            },
            {
                "question": "A tap fills a 30-litre bucket in 2 minutes 30 seconds. At the same flow rate, how many litres fill a tank in 10 minutes?",
                "options": [
                    "120 litres   (10 min = 4 × 2.5 min → 4 × 30 L = 120 L!)",
                    "150 litres",
                    "90 litres",
                    "75 litres"
                ],
                "answer": 0,
                "hint": "Convert 2 min 30 s = 2.5 min (150 s) vs 10 min (600 s); factor = 4×!",
                "explanation": "Flow rate = 30 L ÷ 2.5 min = 12 L/min; across 10 min = 120 litres.",
                "solution_steps": [
                    "Convert consistent time: 2 min 30 s = 2.5 min.",
                    "Find flow rate: 30 L ÷ 2.5 min = 12 L/min.",
                    "Multiply by 10 min: 12 × 10 = 120 litres."
                ]
            },
            {
                "question": "In a 4 × 4 Binairo (Takuzu) row currently showing [ —  |  ?  ? ], if column 3 already has TWO vertical bars (| |) above row 4, what MUST complete [ —  |  ?  ? ]?",
                "options": [
                    "[ —  |  —  | ]   (col 3 forces — to avoid 3 vertical bars; row 4 needs two — and two |!)",
                    "[ —  |  |  — ]",
                    "[ —  |  —  — ]   (gives three — bars in total, breaking equal count!)",
                    "[ —  |  |  | ]   (three adjacent | bars!)"
                ],
                "answer": 0,
                "hint": "First force col 3's empty spot to be (—) to prevent 3 vertical bars in col 3; then balance row 4 (2 — and 2 |)!",
                "explanation": "Row 4 already holds one — and one |, so placing — at slot 3 forces | at slot 4 → [ — | — | ].",
                "solution_steps": [
                    "Check Rule 2 on column 3 (two | above): slot 3 MUST be (—) to avoid |||.",
                    "Row 4 now has [ —  |  —  ? ], holding two — and one |.",
                    "Apply Rule 1 (equal 2 — & 2 | in 4×4): slot 4 MUST be (|) → [ — | — | ]."
                ]
            },
            {
                "question": "If land sells at ₹3,500 per square foot, compute the total valuation of a 100 sq metre residential plot using 1 sq m = 10.764 sq ft:",
                "options": [
                    "₹37,67,400   [= 100 × 10.764 × 3,500 = 1,076.4 × 3,500]",
                    "₹3,50,000",
                    "₹11,48,350   (used linear feet 3.281!)",
                    "₹37,674"
                ],
                "answer": 0,
                "hint": "First convert 100 sq m → 1,076.4 sq ft, then multiply by ₹3,500/sq ft!",
                "explanation": "1,076.4 sq ft × ₹3,500 = ₹37,67,400.",
                "solution_steps": [
                    "Convert plot area to square feet: 100 × 10.764 = 1,076.4 sq ft.",
                    "Multiply area by rate: 1,076.4 × 3,500.",
                    "Compute 10,764 × 350 = ₹37,67,400."
                ]
            },
            {
                "question": "Which grand summary captures ALL of Chapter 7: Proportional Reasoning Part One?",
                "options": [
                    "Proportional similarity relies on multiplicative scaling (ad = bc); ratio reduction via HCF, Āryabhaṭa's Trairāśika, group partitioning m·x/(m+n), unit consistency, and inverse-trap awareness solve real problems cleanly!",
                    "Adding the exact same number to both terms of any ratio always preserves proportionality",
                    "Direct Rule of Three applies equally to speed vs travel time for fixed trips",
                    "Celsius and Fahrenheit multiply purely by 9/5 with zero offset"
                ],
                "answer": 0,
                "hint": "Synthesize Sections 7.1 through 7.6 accurately!",
                "explanation": "Multiplicative scaling, HCF proportion checks, Trairāśika, group partitioning, and unit consistency anchor proportional reasoning.",
                "solution_steps": [
                    "7.1–7.3: Multiplicative similarity, ratio terms a : b, HCF reduction, and a : b :: c : d ⇔ ad = bc.",
                    "7.4–7.5: Trairāśika (phala × ichchhā) ÷ pramāṇa, unit matching, additive/inverse cautions, and m/(m+n) sharing.",
                    "7.6 & Puzzle: Metric/Imperial/Area/Volume/Temp conversions and 3-rule Binairo logic grids."
                ]
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part3)} exercise/challenge slides for Ch7 Class 8 Maths Part 3.")
    total_q = 0
    for s in slides_part3:
        twc = len(s["title"].split())
        assert 1 <= twc <= 3, f"Slide {s['id']} title {s['title']!r} not 1-3 words"
        assert len(s["questions"]) == 10, f"Slide {s['id']} needs 10 questions"
        for idx, q in enumerate(s["questions"]):
            assert len(q["options"]) == 4
            assert len(q["solution_steps"]) == 3
            assert "hint" in q and q["hint"]
            total_q += 1
        print(f"Slide {s['id']}: {s['title']!r} ({twc} words) | Questions: {len(s['questions'])}")
    assert total_q == 40
    print("All 40 exercise & challenge questions verified successfully!")
