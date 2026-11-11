#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 8: Fractions in Disguise
Slides Data Generator - Part 2 (Slides 9 to 16)
Strictly matches NCERT Class 8 Maths Ch 8 syllabus with 1-3 word headings,
195-215 spoken words per slide, zero fictional characters/personas.
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Relative Percent Change",
        "subtitle": "Section 1.3 Percentage Increase or Decrease: Change ÷ Original Base × 100 vs Percentage of Base",
        "speech": (
            "Whenever retail prices, town populations, or test scores rise or fall, how do we measure relative change accurately? Welcome to Section One Point Three: Percentage Increase and Percentage Decrease! Memorize the universal change formula carefully: Percentage Increase or Decrease equals Amount of Change divided by the ORIGINAL BASE, multiplied by 100! Notice which denominator ALWAYS stands on the bottom—the ORIGINAL starting value BEFORE the change occurred, NEVER the new ending value! "
            "Walk carefully through an increase example! Suppose a bicycle price climbs from ₹4,000 up to ₹4,600! First find the exact Amount of Change: 4,600 − 4,000 = +₹600! Now divide by the ORIGINAL base ₹4,000: (600 / 4,000) × 100 = 15% increase! Notice the crucial wording distinction highlighted in NCERT: the new price ₹4,600 equals 115% OF the original base, representing a +15% INCREASE! "
            "Test a price decrease next! Suppose a tablet drops from ₹10,000 down to ₹8,500! Amount of Change = 10,000 − 8,500 = ₹1,500 drop! Divide by ORIGINAL ₹10,000: (1,500 / 10,000) × 100 = 15% decrease! Here the new price equals 85% OF the original base (100% − 15%)! Always check carefully whether a problem asks 'percentage OF base' or 'percentage INCREASE over base'!"
        ),
        "checkpoints": [
            {
                "question": "A city's rainfall rose from 80 cm last year to 100 cm this year. What is the percentage increase in rainfall?",
                "options": [
                    "25% increase   ((20 / 80) × 100 = 25%)",
                    "20% increase",
                    "125% increase",
                    "80% increase"
                ],
                "answer": 0,
                "hint": "Divide the +20 cm change by the ORIGINAL 80 cm base, not 100 cm!",
                "explanation": "Change = 100 − 80 = 20 cm. Percentage increase = (20 / 80) × 100 = 25% (new rainfall is 125% of original)."
            },
            {
                "question": "When a number increases by 20%, what percentage OF the original base does the new value represent?",
                "options": [
                    "120% of the original base",
                    "20% of the original base",
                    "80% of the original base",
                    "102% of the original base"
                ],
                "answer": 0,
                "hint": "Start with 100% (original) and add the +20% increase!",
                "explanation": "Percentage of base = 100% + 20% = 120%, whereas the percentage increase itself is 20%."
            }
        ]
    },
    {
        "id": 10,
        "title": "Profit Loss GST",
        "subtitle": "Section 1.3 Profit & Loss (CP, MP, SP), Supply Chain, Gross vs Net Profit & Commercial CGST + SGST",
        "speech": (
            "Follow any everyday notebook from factory floor to retail shelf along the commercial supply chain: Manufacturer to Wholesaler to Retailer to Customer! Three crucial price terms govern commerce in Section One Point Three: Cost Price (CP) is what the seller originally pays; Marked Price (MP) is the printed tag price before any discount; and Selling Price (SP) is the actual price paid by the buyer! Whenever SP exceeds CP, the seller earns a PROFIT (SP − CP)! Whenever SP drops below CP, the seller suffers a LOSS (CP − SP)! Both Profit% and Loss% are ALWAYS calculated over Cost Price: (Profit or Loss ÷ CP) × 100! "
            "Business accounting goes one smart step deeper! GROSS PROFIT equals total Sales Revenue minus Cost of Goods Sold—before counting shop rent, electricity, or worker salaries! Subtracting all those everyday operating expenses from Gross Profit reveals the true NET PROFIT! "
            "Finally, inspect any retail sales receipt for Goods and Services Tax (GST)! Suppose a buyer purchases an item at ₹1,000 Selling Price carrying 18% GST! In intra-state transactions, GST splits cleanly into 9% Central GST (CGST = ₹90) plus 9% State GST (SGST = ₹90), producing a final bill of ₹1,180!"
        ),
        "checkpoints": [
            {
                "question": "A retailer buys a backpack for Cost Price ₹800 and sells it for ₹960. What is the profit percentage earned?",
                "options": [
                    "20% profit   ((160 / 800) × 100 = 20%)",
                    "16% profit",
                    "16.67% profit",
                    "25% profit"
                ],
                "answer": 0,
                "hint": "Find Profit = SP − CP = ₹160, then divide by CP ₹800 (always base profit% on CP)!",
                "explanation": "Profit = ₹960 − ₹800 = ₹160. Profit% = (160 / 800) × 100 = 20%."
            },
            {
                "question": "A shop records Sales Revenue ₹50,000, Cost of Goods ₹35,000, and Operating Expenses (rent & electricity) ₹6,000. Compare Gross Profit against Net Profit, and check a ₹2,000 bill with 12% GST:",
                "options": [
                    "Gross Profit = ₹15,000; Net Profit = ₹9,000; GST adds 6% CGST (₹120) + 6% SGST (₹120) = ₹2,240",
                    "Gross Profit = ₹9,000; Net Profit = ₹15,000; GST total = ₹2,120",
                    "Gross Profit = ₹15,000; Net Profit = ₹15,000; GST splits 12% CGST + 12% SGST",
                    "Gross Profit = ₹41,000; Net Profit = ₹9,000"
                ],
                "answer": 0,
                "hint": "Gross Profit = Sales − Cost of Goods; Net Profit = Gross Profit − Operating Expenses; 12% GST splits 6% + 6%!",
                "explanation": "Gross = 50,000 − 35,000 = ₹15,000; Net = 15,000 − 6,000 = ₹9,000; 12% GST splits cleanly into ₹120 CGST + ₹120 SGST."
            }
        ]
    },
    {
        "id": 11,
        "title": "Simple Compound Growth",
        "subtitle": "Section 1.3 Linear Growth p(1 + rt) vs Compounding Growth p(1 + r)^t in Finance & Biology",
        "speech": (
            "Discover why growth repeated over multiple time periods behaves dramatically differently under COMPOUNDING versus NON-COMPOUNDING! Suppose we begin with initial principal amount p and steady percentage growth rate r per period (written as decimal r, such as 10% = 0.10) across t equal time periods! "
            "Without compounding (linear simple growth), ONLY the original principal p generates new growth during every single period! After t periods, cumulative gain equals p × r × t, producing Total Amount = p(1 + rt)! Invest ₹1,000 at 10% simple annual growth for 3 years: each passing year adds an identical +₹100, reaching exactly ₹1,300! "
            "Now activate COMPOUNDING! Under compounding exponential growth, each completed period's gain merges directly INTO the new base before calculating the NEXT period's increase—so previous growth itself earns further growth! Year One reaches p(1 + r)! Year Two multiplies THAT updated total by (1 + r) again, producing p(1 + r)²! After t periods, Total Amount = p(1 + r)^t! Test ₹1,000 at 10% compounded annually for 3 full years: ₹1,000 → ₹1,100 → ₹1,210 → ₹1,331! That extra +₹31 compounding snowball accelerates dramatically over many years in growing human populations and rapidly multiplying bacterial cultures!"
        ),
        "checkpoints": [
            {
                "question": "Compare ₹2,000 growing at 10% per year for 2 years WITHOUT compounding p(1 + rt) versus WITH compounding p(1 + r)^t:",
                "options": [
                    "Without compounding = ₹2,400; With compounding = ₹2,420 (₹20 extra interest-on-interest!)",
                    "Without compounding = ₹2,420; With compounding = ₹2,400",
                    "Both equal ₹2,400 for 2 years",
                    "Without compounding = ₹2,200; With compounding = ₹2,440"
                ],
                "answer": 0,
                "hint": "Simple: 2000 × (1 + 0.10 × 2). Compound: 2000 × (1.10)² = 2000 × 1.21!",
                "explanation": "Simple adds ₹200 twice → ₹2,400. Compound multiplies 2000 × 1.1 × 1.1 → ₹2,420 because Year 1's ₹200 earns 10% (₹20) in Year 2."
            },
            {
                "question": "A bacterial culture starts with 5,000 cells and compounds at 20% every hour. Which formula gives the count after t = 3 hours?",
                "options": [
                    "5,000 × (1.20)³ = 8,640 cells",
                    "5,000 × (1 + 0.20 × 3) = 8,000 cells",
                    "5,000 × (0.80)³ = 2,560 cells",
                    "5,000 × 1.20 = 6,000 cells"
                ],
                "answer": 0,
                "hint": "Each new generation reproduces, so apply p(1 + r)^t with r = 0.20 and t = 3!",
                "explanation": "5,000 × 1.2³ = 5,000 × 1.728 = 8,640 bacterial cells."
            }
        ]
    },
    {
        "id": 12,
        "title": "Asset Value Decay",
        "subtitle": "Section 1.3 Decline & Depreciation: Vehicles, Electronics & Exponential Decay p(1 - r)^t",
        "speech": (
            "Percentage compounding also operates cleanly in reverse! Everyday manufactured assets such as motor vehicles, smartphones, laptops, and even shrinking town populations steadily lose value or size over time—an important downward process called DEPRECIATION or DECLINE! Notice how identical multiplicative mathematics mirrors compounding growth, simply replacing +r with −r! Starting from initial asset value p and constant annual depreciation rate r (expressed as a decimal), each year preserves fraction (1 − r) of the previous year's remaining worth, giving Value V = p(1 − r)^t after t years! "
            "Test a brand-new laptop or scooter purchased for ₹50,000 depreciating at 20% annually! After Year One, it retains 80% (factor 0.80): 50,000 × 0.80 = ₹40,000 (dropping ₹10,000)! After Year Two, apply 20% decay directly TO ₹40,000, NEVER ₹50,000: 40,000 × 0.80 = ₹32,000 (dropping only ₹8,000)! After Year Three: 32,000 × 0.80 = ₹25,600! "
            "Spot this vital mathematical distinction clearly: whereas naive linear subtraction (20% × 3 = 60%) crashes straight down to just ₹20,000, realistic exponential annual depreciation p(1 − r)^t shrinks by progressively smaller rupee amounts during each consecutive year and smoothly approaches zero without ever touching zero for real assets across finite time periods!"
        ),
        "checkpoints": [
            {
                "question": "A motorbike costing ₹80,000 depreciates at 10% every year using p(1 − r)^t. What is its value after 2 years?",
                "options": [
                    "₹64,800   (80,000 × 0.90² = 80,000 × 0.81)",
                    "₹64,000   (linear 20% drop)",
                    "₹72,000",
                    "₹96,800"
                ],
                "answer": 0,
                "hint": "After Year 1 value is ₹72,000; take 90% of ₹72,000 for Year 2!",
                "explanation": "Year 1: 80,000 × 0.9 = ₹72,000. Year 2: 72,000 × 0.9 = ₹64,800."
            },
            {
                "question": "Why does an electronics gadget depreciating at 25% per year retain ₹5,625 instead of ₹5,000 after 2 years from ₹10,000?",
                "options": [
                    "Year 2's 25% drop applies to the smaller Year 1 value (₹7,500), dropping ₹1,875 instead of ₹2,500",
                    "Because depreciation stops completely after the first year",
                    "Because 25% × 25% = 56.25%",
                    "Because taxes increase the Year 2 price"
                ],
                "answer": 0,
                "hint": "Notice 75% of ₹10,000 is ₹7,500, and 75% of ₹7,500 is ₹5,625!",
                "explanation": "Compounded depreciation reduces the base each year: 10,000 × 0.75 × 0.75 = ₹5,625."
            }
        ]
    },
    {
        "id": 13,
        "title": "Successive Percent Traps",
        "subtitle": "Section 1.3 Tricky Percentages: Base-Size Fallacy, 30%+20% Successive Discounts & ±50% Asymmetry",
        "speech": (
            "Advertisements and headlines overflow with TRICKY PERCENTAGES cleverly designed to fool uncritical readers! Expose three classic traps from Section One Point Three permanently! "
            "Trap One: THE BASE-SIZE FALLACY behind 'fastest growing' headlines! If Chess Club A grows from 2 members to 6 (+200% growth!), while Reading Club B grows from 500 to 600 (+20% growth), Club A celebrates ten times the percentage rate—yet welcomed ONLY 4 newcomers versus Club B's 100 newcomers! Always inspect the starting base! "
            "Trap Two: SUCCESSIVE COMPOUNDING DISCOUNTS! A flashy store banner promising '30% off PLUS extra 20% off!' does NOT grant 50% off! Trace ₹100 carefully: take 30% off first → ₹70 remains! Next apply 20% off THAT reduced ₹70 (20% of 70 = ₹14 saved), landing at ₹56! True single net discount equals ONLY 44%, NEVER 50% (since 0.70 × 0.80 = 0.56)! "
            "Trap Three: ASYMMETRIC GAINS VERSUS LOSSES! Raise a ₹100 price tag UP by +50% → ₹150! Then slash that higher ₹150 price DOWN by −50% → ₹75! Equal +50% and −50% steps end cleanly in a surprising 25% NET LOSS (1.5 × 0.5 = 0.75), simply because that second −50% cut struck a MUCH larger base!"
        ),
        "checkpoints": [
            {
                "question": "A jacket priced at ₹1,000 offers '30% off + an extra 20% off'. What final price do you pay, and what is the true effective single discount?",
                "options": [
                    "₹560; effective discount is 44% (not 50%)",
                    "₹500; effective discount is 50%",
                    "₹600; effective discount is 40%",
                    "₹540; effective discount is 46%"
                ],
                "answer": 0,
                "hint": "Compute 1,000 × 0.70 = ₹700 first, then multiply ₹700 × 0.80!",
                "explanation": "1000 × 0.70 = ₹700; 700 × 0.80 = ₹560, which saves ₹440 out of ₹1,000 = 44%."
            },
            {
                "question": "A trader increases an item's price by 50% and later gives a 50% discount on the new price. What is the net percentage change?",
                "options": [
                    "25% net loss   (1.50 × 0.50 = 0.75)",
                    "0% net change (returns to original)",
                    "25% net profit",
                    "10% net loss"
                ],
                "answer": 0,
                "hint": "Test starting at ₹100: +50% turns ₹100 into ₹150; now subtract 50% of ₹150!",
                "explanation": "50% of ₹150 is ₹75, dropping price to ₹75 — a 25% loss below ₹100."
            }
        ]
    },
    {
        "id": 14,
        "title": "Targets Ratios Geometry",
        "subtitle": "Sections 1.2 & 1.3 Figure It Out: Recipes, Geometry Area % Change & Promotional 'Buy X Get Y Free'",
        "speech": (
            "Apply percentage reasoning across four high-utility NCERT 'Figure it Out' applications! First, RECIPE AND TIME SCALING: if a biscuit recipe blends 60% flour, 25% butter, and 15% sugar, doubling or tripling total batch weight keeps every ingredient's exact percentage constant while scaling gram weights cleanly! "
            "Second, POPULATION PROJECTIONS AND DEMOGRAPHICS: knowing 38% of a town's 50,000 residents are young adults lets planners forecast exactly 19,000 residents via 0.38 × 50,000! "
            "Third, GEOMETRY AND RECTANGLE AREA PERCENTAGE CHANGE! Suppose a rectangle increases length by +20% (factor 1.2) and width by +10% (factor 1.1)! Does total area expand by 20 + 10 = 30%? Look closely! Area = L × W scales multiplicatively: 1.2 × 1.1 = 1.32—a FULL +32% jump, because the extra 20% length ALSO picks up 10% extra width! Conversely, if length grows +20% while breadth shrinks −20%, Area multiplies 1.2 × 0.8 = 0.96, losing 4% area! "
            "Fourth, PROMOTIONAL STORE DEALS like 'Buy 2 Get 1 Free'! Shoppers walk out the store carrying 3 identical products while paying for ONLY 2! Since 1 item out of all 3 received items is completely free, the true effective percentage discount equals (1/3) × 100 = 33.33% off!"
        ),
        "checkpoints": [
            {
                "question": "A retail offer advertises 'Buy 3 Shirts, Get 1 Shirt Free' (all shirts equally priced). What true percentage discount does the shopper receive?",
                "options": [
                    "25% discount   (1 free out of 4 total shirts)",
                    "33.33% discount",
                    "20% discount",
                    "50% discount"
                ],
                "answer": 0,
                "hint": "Count TOTAL shirts carried out (3 + 1 = 4) and how many were free (1)!",
                "explanation": "You take home 4 shirts and get 1 free: 1/4 = 25% true discount."
            },
            {
                "question": "If a rectangle's length increases by 20% and its breadth decreases by 20%, what happens to its total area?",
                "options": [
                    "Area decreases by 4%   (1.20 × 0.80 = 0.96)",
                    "Area remains 0% unchanged",
                    "Area increases by 4%",
                    "Area decreases by 20%"
                ],
                "answer": 0,
                "hint": "Multiply the new scaling factors cleanly: 1.2 × 0.8!",
                "explanation": "New Area = (1.2 L) × (0.8 W) = 0.96 LW, representing a 4% decrease."
            }
        ]
    },
    {
        "id": 15,
        "title": "Chapter Formula Summary",
        "subtitle": "Chapter Summary Consolidation: Fractions/Decimals (x/100), Change, Profit/GST, Linear vs Compound & Estimates",
        "speech": (
            "Pause cleanly here to consolidate our complete mathematical toolkit from Fractions in Disguise onto one crystal-clear reference dashboard! First, DEFINITIONS AND FDP CONVERSIONS: any X% literally equals fraction X/100; convert fractions or decimals into percentages by multiplying by 100, and shift decimals two places left to revert back! Always remember: raw percentage comparisons remain valid ONLY across matching reference wholes! "
            "Second, QUANTITIES AND BENCHMARK ESTIMATION: compute a% of any whole using (a/100) × total, visual bar models, or crisp mental anchor blocks (50%, 25%, 10%, 5%, 1%) backed by smart estimation checks! "
            "Third, RELATIVE CHANGE: Percentage Increase or Decrease equals (Amount of Change ÷ Original Base) × 100—always anchor that denominator to the original starting value! "
            "Fourth, COMMERCE AND TAXES: Profit occurs when SP > CP, Loss when SP < CP (computed over CP); Net Profit deducts operating expenses from Gross Profit; intra-state GST adds equal CGST + SGST halves onto retail receipts! "
            "Fifth, GROWTH AND TRAPS: Simple linear growth follows A = p(1 + rt), whereas compounding growth multiplies A = p(1 + r)^t, asset depreciation multiplies V = p(1 − r)^t, and successive percentage changes combine cleanly via (1 ± r₁)(1 ± r₂) without ever blindly adding percentages!"
        ),
        "checkpoints": [
            {
                "question": "Which formula pair accurately contrasts non-compounding (simple) growth against compounding growth over t periods at decimal rate r?",
                "options": [
                    "Simple: p(1 + rt)   vs   Compound: p(1 + r)^t",
                    "Simple: p(1 + r)^t   vs   Compound: p(1 + rt)",
                    "Simple: p(1 − rt)   vs   Compound: p(1 − r)^t",
                    "Simple: p + r   vs   Compound: p × t"
                ],
                "answer": 0,
                "hint": "Compound growth multiplies repeatedly by (1 + r) for t periods!",
                "explanation": "Simple growth adds linear interest p×r×t → p(1 + rt); compound growth multiplies by (1 + r) each period → p(1 + r)^t."
            },
            {
                "question": "What golden denominator rule prevents blunders in BOTH Profit/Loss percentages and Percentage Increase/Decrease?",
                "options": [
                    "Always divide by the ORIGINAL starting value (CP for profit/loss; Original Base for % change)",
                    "Always divide by whichever value is larger",
                    "Always divide by Selling Price SP",
                    "Add both values together before dividing"
                ],
                "answer": 0,
                "hint": "Every percentage change measures growth or drop relative to where you STARTED!",
                "explanation": "Dividing change by the original base (or CP) ensures consistent, accurate percentage measurement."
            }
        ]
    },
    {
        "id": 16,
        "title": "Peaceful Knights Puzzle",
        "subtitle": "It's Puzzle Time! Peaceful Knights on 8×8 Chessboard: Valid L-Shaped Moves & Parity Placement Logic",
        "speech": (
            "Conclude Chapter Eight with the classic chessboard reasoning challenge: IT'S PUZZLE TIME—PEACEFUL KNIGHTS! Picture a standard 8 by 8 chessboard holding 64 alternating light and dark squares! Recall carefully how a chess knight moves: every legal knight jump makes an exact 'L-shaped' hop moving 2 squares along one rank or file plus 1 square perpendicular! Our opening puzzle challenges players to place 8 Peaceful Knights on an 8 × 8 chessboard so NO knight attacks any other! Wait—can 8 knights sit safely? Easily—just line 8 knights cleanly along one edge column, or spread them safely apart! "
            "Now uncover the gorgeous mathematical parity principle connecting chess directly to percentages! Watch square colors closely whenever ANY knight makes an L-shaped hop: stepping 2 squares lands on the same square color, then stepping 1 perpendicular square ALWAYS FLIPS color! Therefore, ANY knight resting on a DARK square can ONLY attack LIGHT squares—it can NEVER threaten another dark square! "
            "What happens if you place one knight on EVERY dark square across all eight ranks? You achieve an astonishing 32 Peaceful Knights—exactly 50% of the entire 64-square board—completely peaceful with zero possible attacks! Explore interactive placements right now on the chessboard!"
        ),
        "checkpoints": [
            {
                "question": "A knight stands on a dark square of a standard 8 × 8 chessboard. Which squares can that knight legally attack in one 'L-shaped' move?",
                "options": [
                    "ONLY light squares (every L-move switches square color!)",
                    "ONLY dark squares",
                    "Squares of the same column only",
                    "Equal numbers of light and dark squares"
                ],
                "answer": 0,
                "hint": "Move 2 steps (same color) + 1 perpendicular step (flips color)!",
                "explanation": "A knight always jumps from dark to light or light to dark; thus knights on dark squares never attack each other."
            },
            {
                "question": "Placing a Peaceful Knight on EVERY dark square of an 8 × 8 chessboard yields how many non-attacking knights, and what percentage of the 64 squares do they occupy?",
                "options": [
                    "32 Peaceful Knights occupying 50% of the chessboard",
                    "8 Peaceful Knights occupying 12.5% of the chessboard",
                    "16 Peaceful Knights occupying 25% of the chessboard",
                    "64 Peaceful Knights occupying 100% of the chessboard"
                ],
                "answer": 0,
                "hint": "Half of a standard 8 × 8 board's 64 squares are dark!",
                "explanation": "Since 32 of 64 squares share one color, all 32 knights coexist peacefully, filling 32/64 = 50% of the board."
            }
        ]
    }
]
