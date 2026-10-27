# Class 8 Mathematics - Chapter 8: Percentages and Their Applications

slides_data = [
    {
        "id": 1,
        "title": "Hidden Fractions",
        "subtitle": "Uncovering Fractional Parts in Shaded Grids, Ratios & Everyday Measures",
        "content": "<p>In our daily world, quantities are often partitioned into parts of a whole. Before we can master percentages, we must learn to recognize <strong>hidden fractions</strong> embedded in shapes, collections, and continuous measurements.</p><ul><li><strong>The Whole as Unity (1):</strong> The entire region, group, or quantity represents the number 1.</li><li><strong>Equal Partitioning:</strong> If a unit square is sliced into $n$ congruent pieces and $k$ pieces are shaded, the shaded portion represents the fraction:$$\\text{Fraction} = \\frac{k}{n} = \\frac{\\text{Number of Selected Parts}}{\\text{Total Number of Equal Parts}}$$</li><li><strong>Hidden Combinations:</strong> A shape may be partitioned unevenly at first glance. By subdividing all sections into the smallest common unit, the true fractional value is unmasked!</li></ul><p>For example, if half of a square is divided into 2 equal parts and the other half into 4 equal parts, one small piece is not $\\frac{1}{6}$; it is $\\frac{1}{8}$ of the whole square!</p>",
        "sim_type": "hidden_fractions_grid_scanner",
        "voice": "Welcome to our laboratory on percentages and their real-world applications! We begin by uncovering hidden fractions. Every fraction tells the story of parts compared to an unbroken whole.",
        "checkpoints": [
            {
                "q": "A rectangular garden is divided into 8 equal flowerbeds. If 3 flowerbeds are planted with roses and 2 with marigolds, what fraction of the garden remains unplanted?",
                "options": [
                    "5/8",
                    "3/8",
                    "1/2",
                    "1/4"
                ],
                "ans": 1,
                "feedback": "Correct! Planted flowerbeds = 3 + 2 = 5 out of 8. The unplanted fraction is 1 - 5/8 = 3/8."
            },
            {
                "q": "A pizza is cut into 12 equal slices. Kabir eats 3 slices and Priya eats 1 slice. What fraction of the pizza was consumed in simplest form?",
                "options": [
                    "4/12",
                    "1/3",
                    "1/4",
                    "2/3"
                ],
                "ans": 1,
                "feedback": "Correct! Total slices eaten = 3 + 1 = 4 slices out of 12. In simplest form, 4/12 = 1/3."
            }
        ]
    },
    {
        "id": 2,
        "title": "Fractions into Percentages & Conversion",
        "subtitle": "The Concept of Parts Per Hundred & The Universal Multiplier",
        "content": "<p>The word <strong>percent</strong> originates from the Latin phrase <em>per centum</em>, meaning <strong>'per hundred'</strong> or <strong>'out of every hundred'</strong>. It is denoted by the symbol %.</p>$$\\mathbf{P\\% = \\frac{P}{100}}$$<p>A percentage is simply a fraction whose denominator is fixed at 100. This standardization makes comparisons effortless!</p><h4>How to Convert Any Fraction into a Percentage:</h4><ol><li><strong>Method 1 (Equivalent Denominator 100):</strong> If the denominator divides 100 evenly, multiply both numerator and denominator:$$\\frac{3}{5} = \\frac{3 \\times 20}{5 \\times 20} = \\frac{60}{100} = \\mathbf{60\\%}$$</li><li><strong>Method 2 (The Universal 100% Multiplier):</strong> Because $100\\% = \\frac{100}{100} = 1$, multiplying any number by 100% changes its form without changing its value:$$\\text{Percentage} = \\left(\\frac{a}{b} \\times 100\\right)\\%$$$$\\frac{5}{8} \\times 100\\% = \\frac{500}{8}\\% = \\mathbf{62.5\\%}$$</li></ol>",
        "sim_type": "fraction_to_percent_morpher",
        "voice": "Percent literally means per hundred. By expressing any fractional quantity as a fraction with denominator one hundred, we gain an instant, universal standard of comparison.",
        "checkpoints": [
            {
                "q": "Convert the fraction 7/20 into an equivalent percentage.",
                "options": [
                    "28%",
                    "35%",
                    "40%",
                    "70%"
                ],
                "ans": 1,
                "feedback": "Correct! (7/20) × 100% = 7 × 5% = 35%."
            },
            {
                "q": "Convert 3/8 into a percentage.",
                "options": [
                    "37.5%",
                    "38%",
                    "35%",
                    "42.5%"
                ],
                "ans": 0,
                "feedback": "Correct! (3/8) × 100% = 300/8% = 37.5%."
            }
        ]
    },
    {
        "id": 3,
        "title": "Everyday Percentages",
        "subtitle": "Battery Gauges, Test Scores, Discount Badges & Storage Quotas",
        "content": "<p>Percentages are the lingua franca of modern technology, commerce, and media because they convey relative scale instantaneously, regardless of total capacity.</p><ul><li><strong>Smartphone Battery Indicator:</strong> When your phone displays 42%, it means 42 out of 100 equal energy units remain. A 5000 mAh battery at 42% holds 2100 mAh, whereas a 3000 mAh battery at 42% holds 1260 mAh—both are at the same relative fullness!</li><li><strong>Examination Scores:</strong> Scoring 45 out of 50 (90%) represents a higher academic performance than scoring 72 out of 90 (80%).</li><li><strong>Retail Discounts:</strong> A '25% Off' sticker immediately communicates that one-fourth of the price will be deducted at checkout.</li><li><strong>Nutritional Values:</strong> A juice packet stating '10% Added Sugar' implies that exactly 10 g in every 100 g of beverage is sugar.</li></ul>",
        "sim_type": "everyday_percentages_dashboard",
        "voice": "Look around you! From the battery indicator on your smartphone to retail discounts and test scores, percentages provide a universal language of relative proportion.",
        "checkpoints": [
            {
                "q": "Student A scores 36 out of 40 in Math. Student B scores 63 out of 75 in Science. Who achieved the higher percentage score?",
                "options": [
                    "Student B (63 is greater than 36)",
                    "Student A (90% vs. 84% for Student B)",
                    "Both scored exactly the same percentage",
                    "Cannot be compared because maximum marks are different"
                ],
                "ans": 1,
                "feedback": "Correct! Student A: (36/40) × 100% = 90%. Student B: (63/75) × 100% = 84%. Student A performed better relatively."
            },
            {
                "q": "A laptop battery of capacity 60 Watt-hours is at 65% charge. How much energy remains in the battery?",
                "options": [
                    "36 Wh",
                    "39 Wh",
                    "42 Wh",
                    "45 Wh"
                ],
                "ans": 1,
                "feedback": "Correct! Energy = 65% of 60 = 0.65 × 60 = 39 Watt-hours."
            }
        ]
    },
    {
        "id": 4,
        "title": "Percent of a Value & Quick Mental Math",
        "subtitle": "Benchmark Decomposition: The 10%, 1%, 5%, and 50% Rule",
        "content": "<p>To compute $P\\%$ of a given quantity $Q$, we use the foundational formula:</p>$$\\mathbf{\\text{Value} = \\frac{P}{100} \\times Q}$$<h4>Rapid Mental Math Shortcuts (Benchmark Method):</h4><p>Calculators are rarely needed if you decompose percentages into familiar anchor benchmarks:</p><ul><li><strong>50% of Q:</strong> Divide by 2 (1/2).</li><li><strong>25% of Q:</strong> Half of 50%, or divide by 4 (1/4).</li><li><strong>10% of Q:</strong> Shift the decimal point one place to the left (divide by 10).</li><li><strong>1% of Q:</strong> Shift the decimal point two places to the left (divide by 100).</li><li><strong>5% of Q:</strong> Exactly half of 10%.</li></ul><p><strong>Example: Calculate 35% of ₹480 mentally:</strong></p>$$\\text{Anchor: } 10\\% \\text{ of } 480 = 48$$$$30\\% = 3 \\times 48 = 144$$$$5\\% = \\text{half of } 48 = 24$$$$35\\% = 144 + 24 = \\mathbf{\\text{₹}168}$$",
        "sim_type": "mental_benchmark_decomposer",
        "voice": "You do not need a calculator to find percentages! Master the benchmark anchors: 10 percent is shifting one decimal, 1 percent is shifting two decimals, and 5 percent is half of 10 percent.",
        "checkpoints": [
            {
                "q": "Find 15% of ₹640 using the benchmark method.",
                "options": [
                    "₹86",
                    "₹92",
                    "₹96",
                    "₹104"
                ],
                "ans": 2,
                "feedback": "Correct! 10% of 640 = 64. 5% of 640 = 32. 15% = 64 + 32 = ₹96."
            },
            {
                "q": "What is 25% of 360?",
                "options": [
                    "80",
                    "90",
                    "95",
                    "100"
                ],
                "ans": 1,
                "feedback": "Correct! 25% is one-fourth: 360 / 4 = 90."
            }
        ]
    },
    {
        "id": 5,
        "title": "The FDP Trio: Fractions, Decimals & Percentages",
        "subtitle": "The Holy Trinity of Rational Representations",
        "content": "<p>Every rational number can wear three different hats: a <strong>Fraction</strong>, a <strong>Decimal</strong>, or a <strong>Percentage</strong>. Fluency in switching between these representations is one of the most powerful skills in mathematics.</p>$$\\mathbf{\\text{Fraction } \\left(\\frac{a}{b}\\right) \\iff \\text{Decimal } (0.xx) \\iff \\text{Percentage } (P\\%)}$$<table style=\"width:100%; border-collapse:collapse; margin-top:8px; font-size:13px; text-align:center;\"><thead><tr style=\"background:#1e293b; color:#38bdf8;\"><th style=\"padding:6px; border:1px solid #334155;\">Fraction</th><th style=\"padding:6px; border:1px solid #334155;\">Decimal</th><th style=\"padding:6px; border:1px solid #334155;\">Percentage</th><th style=\"padding:6px; border:1px solid #334155;\">Anchor Role</th></tr></thead><tbody><tr><td style=\"padding:6px; border:1px solid #334155;\">1/2</td><td>0.50</td><td>50%</td><td>Half</td></tr><tr><td style=\"padding:6px; border:1px solid #334155;\">1/4</td><td>0.25</td><td>25%</td><td>Quarter</td></tr><tr><td style=\"padding:6px; border:1px solid #334155;\">3/4</td><td>0.75</td><td>75%</td><td>Three Quarters</td></tr><tr><td style=\"padding:6px; border:1px solid #334155;\">1/5</td><td>0.20</td><td>20%</td><td>One Fifth</td></tr><tr><td style=\"padding:6px; border:1px solid #334155;\">1/10</td><td>0.10</td><td>10%</td><td>One Tenth</td></tr><tr><td style=\"padding:6px; border:1px solid #334155;\">1/8</td><td>0.125</td><td>12.5%</td><td>One Eighth</td></tr><tr><td style=\"padding:6px; border:1px solid #334155;\">1/3</td><td>0.333...</td><td>33 1/3%</td><td>One Third</td></tr></tbody></table>",
        "sim_type": "fdp_trinity_converter",
        "voice": "Fractions, decimals, and percentages are three different ways of writing the exact same mathematical value. Transitioning seamlessly between them empowers your problem solving.",
        "checkpoints": [
            {
                "q": "Express the decimal 0.08 as a percentage and as a fraction in simplest form.",
                "options": [
                    "80% and 4/5",
                    "8% and 2/25",
                    "0.8% and 1/125",
                    "8% and 8/10"
                ],
                "ans": 1,
                "feedback": "Correct! 0.08 = 8/100 = 8%. In simplest form: 8/100 = 2/25."
            },
            {
                "q": "Which fraction represents 12.5%?",
                "options": [
                    "1/4",
                    "1/5",
                    "1/8",
                    "1/12"
                ],
                "ans": 2,
                "feedback": "Correct! 12.5% = 12.5/100 = 125/1000 = 1/8."
            }
        ]
    },
    {
        "id": 6,
        "title": "Percentages Beyond 100%",
        "subtitle": "Quantities Exceeding Unity: Growth Factors & Multiples",
        "content": "<p>Can a percentage be greater than 100%? <strong>Absolutely!</strong></p><p>While an object cannot be more than 100% of <em>itself</em> (you cannot eat 120% of a single pizza), when comparing an outcome to an original baseline, values frequently exceed 100%:</p><ul><li>100% represents the <strong>entire original whole</strong> ($1 \\times \\text{Base}$).</li><li>200% represents <strong>twice the original whole</strong> ($2 \\times \\text{Base}$).</li><li>350% represents <strong>three and a half times the original whole</strong> ($3.5 \\times \\text{Base}$).</li></ul><p><strong>Example in Agriculture:</strong> A farmer harvests 250 quintals of wheat this season compared to an expected target of 200 quintals. What percentage of the target was achieved?</p>$$\\text{Percentage Achieved} = \\frac{250}{200} \\times 100\\% = \\frac{5}{4} \\times 100\\% = \\mathbf{125\\%}$$<p>This means the harvest was 25% <em>above</em> the target ($100\\% + 25\\% = 125\\%$).</p>",
        "sim_type": "beyond_hundred_stack_visualizer",
        "voice": "Percentages can indeed exceed 100 percent! Whenever a new amount is greater than the original base quantity, the percentage will be greater than 100 percent.",
        "checkpoints": [
            {
                "q": "A factory produced 15,000 toys against its monthly target of 12,000 toys. What percentage of its target did it achieve?",
                "options": [
                    "115%",
                    "120%",
                    "125%",
                    "130%"
                ],
                "ans": 2,
                "feedback": "Correct! (15000 / 12000) × 100% = (5/4) × 100% = 125%."
            },
            {
                "q": "What decimal multiplier corresponds to 275%?",
                "options": [
                    "0.275",
                    "2.75",
                    "27.5",
                    "275"
                ],
                "ans": 1,
                "feedback": "Correct! 275% = 275 / 100 = 2.75."
            }
        ]
    },
    {
        "id": 7,
        "title": "Comparing Proportions by Percent",
        "subtitle": "Normalizing Unequal Denominators onto a Universal Scale of 100",
        "content": "<p>How do we compare two disparate ratios when their total bases are unequal? Percentages act as the great leveler by projecting both fractions onto a common denominator of 100.</p><p><strong>The School Cricket Match Dilemma:</strong></p><ul><li>Batter A scored 42 runs off 50 balls (Strike Rate = 42/50).</li><li>Batter B scored 63 runs off 70 balls (Strike Rate = 63/70).</li></ul><p>Who scored at a faster pace? Direct comparison of 42 and 63 is misleading because Batter B faced more deliveries!</p>$$\\text{Batter A: } \\frac{42}{50} \\times 100\\% = 42 \\times 2\\% = \\mathbf{84\\%}$$$$\\text{Batter B: } \\frac{63}{70} \\times 100\\% = \\frac{9}{10} \\times 100\\% = \\mathbf{90\\%}$$<p>Because $90\\% > 84\\%$, Batter B scored at a significantly higher scoring rate!</p>",
        "sim_type": "proportion_normalizer_scale",
        "voice": "Percentages are the great leveler of comparison. By converting unequal fractions to a common base of 100, we reveal the true relative performance instantly.",
        "checkpoints": [
            {
                "q": "Class 8A had 28 students pass out of 35. Class 8B had 33 students pass out of 40. Which class had the higher pass percentage?",
                "options": [
                    "Class 8A (80% vs 82.5% for 8B)",
                    "Class 8B (82.5% vs 80% for 8A)",
                    "Both classes had identical pass rates",
                    "Cannot be determined without knowing failed count"
                ],
                "ans": 1,
                "feedback": "Correct! Class 8A: 28/35 = 4/5 = 80%. Class 8B: 33/40 = 82.5%. Class 8B had the higher pass percentage."
            },
            {
                "q": "Which is a higher success rate: 19 out of 25, or 37 out of 50?",
                "options": [
                    "19 out of 25 (76% vs 74%)",
                    "37 out of 50 (74% vs 76%)",
                    "Both are exactly equal",
                    "Cannot be compared"
                ],
                "ans": 0,
                "feedback": "Correct! 19/25 = 76/100 = 76%. 37/50 = 74/100 = 74%. 19 out of 25 is higher."
            }
        ]
    },
    {
        "id": 8,
        "title": "Content Purity & Analysis (KYC)",
        "subtitle": "Know Your Contents: Gold Karats, Food Labels & Alloy Compositions",
        "content": "<p>Consumer literacy requires understanding <strong>Know Your Contents (KYC)</strong> labels on jewelry, food packaging, and industrial chemicals. Purity is universally quantified as a percentage.</p><h4>Gold Purity & The 24-Karat Standard:</h4><p>Pure elemental gold is designated as 24 Karats (100% pure gold). However, pure gold is too malleable for durable jewelry, so copper or silver is alloyed with it:</p>$$\\mathbf{\\text{Purity \\%} = \\frac{\\text{Karat Rating}}{24} \\times 100\\%}$$<ul><li><strong>24 Karat Gold:</strong> $\\frac{24}{24} \\times 100\\% = \\mathbf{100\\%}$ pure gold.</li><li><strong>22 Karat Gold (Standard Hallmark 916):</strong>$$\\text{Purity} = \\frac{22}{24} \\times 100\\% = \\frac{11}{12} \\times 100\\% = \\mathbf{91.67\\%} \\approx 916\\text{ parts per 1000}$$</li><li><strong>18 Karat Gold:</strong> $\\frac{18}{24} \\times 100\\% = \\frac{3}{4} \\times 100\\% = \\mathbf{75\\%}$ gold (25% alloy metals).</li></ul><p><strong>Food Composition:</strong> A chocolate bar weighing 150 g has 70% cocoa. The mass of pure cocoa is $0.70 \\times 150 = \\mathbf{105\\text{ g}}$.</p>",
        "sim_type": "gold_purity_kyc_scanner",
        "voice": "Know Your Contents! The karat system in gold is a prime example of percentages. 22 karat gold means 22 parts out of 24 are pure gold, yielding 91.6 percent purity, hallmarked as 916.",
        "checkpoints": [
            {
                "q": "What is the percentage purity of 14 Karat gold?",
                "options": [
                    "50.0%",
                    "58.33%",
                    "62.5%",
                    "70.0%"
                ],
                "ans": 1,
                "feedback": "Correct! Purity = (14 / 24) × 100% = (7/12) × 100% ≈ 58.33%."
            },
            {
                "q": "A packet of butter weighs 500 grams and contains 82% milk fat. What is the mass of milk fat in the packet?",
                "options": [
                    "390 g",
                    "410 g",
                    "420 g",
                    "440 g"
                ],
                "ans": 1,
                "feedback": "Correct! Mass = 82% of 500 g = (82 / 100) × 500 = 82 × 5 = 410 grams."
            }
        ]
    },
    {
        "id": 9,
        "title": "Percentage Change: Increase & Decrease",
        "subtitle": "Measuring Relative Growth & Reduction via The Baseline Ratio",
        "content": "<p>When a quantity changes from an initial value to a new value, the change must ALWAYS be evaluated relative to the <strong>ORIGINAL (INITIAL) BASE</strong>, never the new value!</p>$$\\mathbf{\\text{Percentage Change} = \\frac{\\text{Absolute Change}}{\\text{Original Initial Value}} \\times 100\\%}$$<ul><li><strong>Percentage Increase:</strong> $\\frac{\\text{New Value} - \\text{Original Value}}{\\text{Original Value}} \\times 100\\%$<br><em>Multiplication Factor:</em> $\\text{New Value} = \\text{Original} \\times \\left(1 + \\frac{r}{100}\\right)$</li><li><strong>Percentage Decrease:</strong> $\\frac{\\text{Original Value} - \\text{New Value}}{\\text{Original Value}} \\times 100\\%$<br><em>Multiplication Factor:</em> $\\text{New Value} = \\text{Original} \\times \\left(1 - \\frac{r}{100}\\right)$</li></ul><p><em>Example:</em> A bicycle price rises from ₹4,000 to ₹4,600. Find the percentage increase.</p>$$\\text{Increase} = 4600 - 4000 = \\text{₹}600$$$$\\text{Percentage Increase} = \\frac{600}{4000} \\times 100\\% = \\frac{60}{4}\\% = \\mathbf{15\\%}$$",
        "sim_type": "percentage_change_elevator",
        "voice": "The golden rule of percentage change: always divide the change by the original starting value. Dividing by the final value is the most common error in mathematics!",
        "checkpoints": [
            {
                "q": "The population of a village decreased from 5,000 to 4,600 due to migration. What is the percentage decrease?",
                "options": [
                    "6%",
                    "8%",
                    "9.2%",
                    "10%"
                ],
                "ans": 1,
                "feedback": "Correct! Decrease = 5000 - 4600 = 400. Percentage decrease = (400 / 5000) × 100% = 8%."
            },
            {
                "q": "An item priced at ₹800 is increased by 20%. What is its new price?",
                "options": [
                    "₹920",
                    "₹960",
                    "₹980",
                    "₹1,000"
                ],
                "ans": 1,
                "feedback": "Correct! Increase = 20% of 800 = 160. New price = 800 + 160 = ₹960."
            }
        ]
    },
    {
        "id": 10,
        "title": "Profit and Loss Arithmetic",
        "subtitle": "Cost Price, Selling Price, Markups & Profit/Loss Percentages",
        "content": "<p>Commercial arithmetic revolves around the exchange of goods. Every financial transaction is evaluated relative to the <strong>Cost Price (CP)</strong>—the investment made by the seller:</p><ul><li><strong>Cost Price (CP):</strong> The total amount paid to acquire or manufacture the article (including overheads like transport and repairs).</li><li><strong>Selling Price (SP):</strong> The price at which the article is sold to the consumer.</li><li><strong>Profit (Gain):</strong> Occurs when $SP > CP$:$$\\text{Profit} = SP - CP \\quad \\implies \\quad \\mathbf{\\text{Profit \\%} = \\frac{\\text{Profit}}{CP} \\times 100\\%}$$</li><li><strong>Loss:</strong> Occurs when $SP < CP$:$$\\text{Loss} = CP - SP \\quad \\implies \\quad \\mathbf{\\text{Loss \\%} = \\frac{\\text{Loss}}{CP} \\times 100\\%}$$</li></ul><p><strong>Crucial Law:</strong> Profit percentage and Loss percentage are <strong>ALWAYS calculated on the Cost Price (CP)</strong> unless stated otherwise!</p>$$SP = CP \\times \\left(1 + \\frac{\\text{Profit \\%}}{100}\\right) \\quad \\text{or} \\quad SP = CP \\times \\left(1 - \\frac{\\text{Loss \\%}}{100}\\right)$$",
        "sim_type": "profit_loss_trading_counter",
        "voice": "In commerce, profit or loss is always judged on your cost price, not what you sell it for. Selling price equals cost price plus profit, or cost price minus loss.",
        "checkpoints": [
            {
                "q": "A shopkeeper buys an article for ₹500 and sells it for ₹625. What is the profit percentage?",
                "options": [
                    "20%",
                    "25%",
                    "30%",
                    "125%"
                ],
                "ans": 1,
                "feedback": "Correct! Profit = 625 - 500 = ₹125. Profit % = (125 / 500) × 100% = 25%."
            },
            {
                "q": "A trader purchases a watch for ₹1,200 and incurs a 10% loss on selling it. Find the selling price.",
                "options": [
                    "₹1,000",
                    "₹1,080",
                    "₹1,100",
                    "₹1,120"
                ],
                "ans": 1,
                "feedback": "Correct! Loss = 10% of 1200 = ₹120. SP = 1200 - 120 = ₹1,080."
            }
        ]
    },
    {
        "id": 11,
        "title": "Sales Tax & GST Calculations",
        "subtitle": "Marked Price, Trade Discounts & Goods and Services Tax",
        "content": "<p>Modern billing combines commercial trade discounts with statutory government taxes:</p><ol><li><strong>Marked Price (MP / List Price):</strong> The printed sticker price on the product.</li><li><strong>Discount:</strong> A reduction offered on the Marked Price to incentivize buyers:$$\\text{Discount} = MP - SP \\quad \\implies \\quad \\mathbf{\\text{Discount \\%} = \\frac{\\text{Discount}}{MP} \\times 100\\%}$$</li><li><strong>Goods and Services Tax (GST):</strong> An indirect tax charged by the government on the sale of goods and services. GST is calculated on the <strong>discounted Selling Price (SP)</strong>, NOT the original Marked Price!$$\\mathbf{\\text{GST Amount} = \\frac{\\text{GST \\%}}{100} \\times SP}$$$$\\mathbf{\\text{Total Bill Amount} = SP + \\text{GST Amount}}$$</li></ol><p><em>Example:</em> An appliance marked at ₹2,000 has a 10% discount and 18% GST.</p>$$\\text{Discount} = 10\\% \\text{ of } 2000 = \\text{₹}200 \\implies SP = \\text{₹}1,800$$$$\\text{GST Amount} = 18\\% \\text{ of } 1800 = \\text{₹}324$$$$\\text{Final Bill} = 1800 + 324 = \\mathbf{\\text{₹}2,124}$$",
        "sim_type": "invoice_gst_generator",
        "voice": "Keep your financial receipts sharp! Discounts are deducted from the marked sticker price, while Goods and Services Tax is added onto that discounted selling price.",
        "checkpoints": [
            {
                "q": "A jacket marked at ₹3,000 is offered at a 20% discount. What is the selling price before tax?",
                "options": [
                    "₹2,200",
                    "₹2,400",
                    "₹2,500",
                    "₹2,600"
                ],
                "ans": 1,
                "feedback": "Correct! Discount = 20% of 3000 = ₹600. SP = 3000 - 600 = ₹2,400."
            },
            {
                "q": "If the discounted price of a gadget is ₹1,500 and GST is 12%, what is the final bill amount?",
                "options": [
                    "₹1,620",
                    "₹1,650",
                    "₹1,680",
                    "₹1,720"
                ],
                "ans": 2,
                "feedback": "Correct! GST = 12% of 1500 = ₹180. Final bill = 1500 + 180 = ₹1,680."
            }
        ]
    },
    {
        "id": 12,
        "title": "Compounding & Successive Growth",
        "subtitle": "Interest on Interest, Population Expansion & Compounding Cycles",
        "content": "<p>When a quantity grows, and in each subsequent interval the growth rate applies not only to the initial base but also to the accumulated growth, we have <strong>compounding</strong>!</p><ul><li><strong>Simple Interest (SI):</strong> Growth calculated strictly on the original principal $P$:$$SI = \\frac{P \\times R \\times T}{100}, \\quad A = P + SI$$</li><li><strong>Compound Interest (CI):</strong> In year 2, you earn interest on your year 1 interest!$$\\mathbf{A = P \\left(1 + \\frac{R}{100}\\right)^n}, \\quad CI = A - P$$Here $P$ is Principal, $R$ is annual rate of interest, $n$ is time periods (years).</li></ul><p><strong>Successive Percentage Growth:</strong> If a city's population of 100,000 grows by 10% in Year 1 and 10% in Year 2:</p>$$\\text{Year 1: } 100,000 \\times 1.10 = 110,000$$$$\\text{Year 2: } 110,000 \\times 1.10 = \\mathbf{121,000} \\quad (\\text{Net } 21\\% \\text{ growth, NOT } 20\\%!)$$",
        "sim_type": "compounding_exponential_growth_tree",
        "voice": "Compounding is often called the eighth wonder of the world. Because growth in each period earns its own growth, compound interest rapidly outpaces simple linear interest.",
        "checkpoints": [
            {
                "q": "Find the compound amount on ₹10,000 at 10% per annum compounded annually for 2 years.",
                "options": [
                    "₹12,000",
                    "₹12,100",
                    "₹12,200",
                    "₹12,500"
                ],
                "ans": 1,
                "feedback": "Correct! A = 10000 × (1 + 10/100)² = 10000 × 1.1 × 1.1 = ₹12,100."
            },
            {
                "q": "The population of a town is 50,000. It increases by 10% each year. What will be the population after 2 years?",
                "options": [
                    "55,000",
                    "60,000",
                    "60,500",
                    "61,000"
                ],
                "ans": 2,
                "feedback": "Correct! After Year 1: 50000 × 1.1 = 55,000. After Year 2: 55000 × 1.1 = 60,500."
            }
        ]
    },
    {
        "id": 13,
        "title": "Depreciation & Decay",
        "subtitle": "Asset Value Depletion, Machine Wear & Bacterial Decay",
        "content": "<p>While investments compound upward, physical assets like motor vehicles, computers, and factory machinery lose monetary value over time through wear, tear, and obsolescence. This process is called <strong>depreciation</strong>.</p>$$\\mathbf{V_n = V_0 \\left(1 - \\frac{R}{100}\\right)^n}$$<ul><li>$V_0$: Initial original purchase cost.</li><li>$V_n$: Depreciated value after $n$ intervals.</li><li>$R$: Annual rate of depreciation.</li><li>$n$: Number of elapsed years.</li></ul><p><em>Example:</em> A motorcycle purchased for ₹80,000 depreciates at 10% per annum. Find its value after 2 years.</p>$$\\text{End of Year 1: } 80,000 \\times (1 - 0.10) = 80,000 \\times 0.90 = \\text{₹}72,000$$$$\\text{End of Year 2: } 72,000 \\times 0.90 = \\mathbf{\\text{₹}64,800}$$<p>Notice that the drop in year 1 was ₹8,000, but in year 2 it was only ₹7,200, because the base has reduced!</p>",
        "sim_type": "asset_depreciation_decay_curve",
        "voice": "Just as savings compound upwards, physical assets depreciate downwards. Each year, the depreciation percentage applies to the newly diminished value.",
        "checkpoints": [
            {
                "q": "A computer bought for ₹40,000 depreciates at 20% per year. What is its value after 1 year?",
                "options": [
                    "₹30,000",
                    "₹32,000",
                    "₹34,000",
                    "₹36,000"
                ],
                "ans": 1,
                "feedback": "Correct! Depreciation = 20% of 40,000 = ₹8,000. Value after 1 year = 40000 - 8000 = ₹32,000."
            },
            {
                "q": "A machinery valued at ₹1,00,000 depreciates at 10% per annum. What will be its book value after 2 years?",
                "options": [
                    "₹80,000",
                    "₹81,000",
                    "₹82,000",
                    "₹85,000"
                ],
                "ans": 1,
                "feedback": "Correct! V₂ = 100000 × (1 - 0.1)² = 100000 × 0.81 = ₹81,000."
            }
        ]
    },
    {
        "id": 14,
        "title": "Percentage Traps & Paradoxes",
        "subtitle": "Symmetry Tricks (x% of y = y% of x) & The Reversibility Illusion",
        "content": "<p>Percentages harbor subtle mathematical traps that mislead even professional analysts. Let us inspect two classic paradoxes:</p><h4>Paradox 1: The Up-and-Down Trap (Asymmetric Base Shift)</h4><p>If you increase an amount by 20%, and then decrease the new amount by 20%, do you return to where you started?</p>$$\\text{Start with } 100 \\xrightarrow{+20\\%} 120 \\xrightarrow{-20\\% \\text{ of } 120} 120 - 24 = \\mathbf{96}$$<p>You did NOT break even; you lost 4%! Why? The 20% increase was calculated on base 100, but the 20% decrease was calculated on the larger base 120!</p><h4>Paradox 2: The Reversibility Law ($x\\%$ of $y = y\\%$ of $x$)</h4>$$\\frac{x}{100} \\times y = \\frac{x \\cdot y}{100} = \\frac{y}{100} \\times x = y\\% \\text{ of } x$$<p><em>Mental Math Super-Weapon:</em> Finding 16% of 50 seems difficult. But flip it: 50% of 16 = <strong>8</strong>! Instantaneous!</p>",
        "sim_type": "percentage_paradox_investigator",
        "voice": "Beware of percentage traps! Increasing by 20 percent and then decreasing by 20 percent leaves you with less than you started. But remember the reversibility secret: x percent of y is always equal to y percent of x.",
        "checkpoints": [
            {
                "q": "Calculate 8% of 25 using the reversibility law (x% of y = y% of x).",
                "options": [
                    "1.5",
                    "2",
                    "2.5",
                    "4"
                ],
                "ans": 1,
                "feedback": "Correct! 8% of 25 = 25% of 8 = one-fourth of 8 = 2! Fast and effortless."
            },
            {
                "q": "The price of a share rises by 50% on Monday and drops by 50% on Tuesday. If its initial price was ₹100, what is its final price?",
                "options": [
                    "₹100 (breaks even)",
                    "₹75 (a net loss of 25%)",
                    "₹50",
                    "₹80"
                ],
                "ans": 1,
                "feedback": "Correct! 100 + 50% = 150. Then 150 - 50% of 150 = 150 - 75 = ₹75. Net loss is 25%!"
            }
        ]
    },
    {
        "id": 15,
        "title": "Base Value Blunders & Chapter Summary Formulas",
        "subtitle": "Debugging Wrong-Base Errors & Master Formula Matrix",
        "content": "<p>The single greatest cause of errors in percentage problems is <strong>Base Value Confusion</strong>. Always ask: <em>Percentage OF WHAT?</em></p><table style=\"width:100%; border-collapse:collapse; margin-top:8px; font-size:12.5px; text-align:left;\"><thead><tr style=\"background:#1e293b; color:#38bdf8; border-bottom:2px solid #334155;\"><th style=\"padding:6px;\">Concept</th><th style=\"padding:6px;\">Standard Base</th><th style=\"padding:6px;\">Master Formula</th></tr></thead><tbody><tr style=\"border-bottom:1px solid #334155;\"><td style=\"padding:6px; font-weight:bold; color:#f8fafc;\">Percent Value</td><td style=\"padding:6px;\">Total Quantity Q</td><td style=\"padding:6px;\">$\\text{Value} = \\frac{P}{100} \\times Q$</td></tr><tr style=\"border-bottom:1px solid #334155;\"><td style=\"padding:6px; font-weight:bold; color:#f8fafc;\">Percentage Change</td><td style=\"padding:6px;\">Original Value (Before)</td><td style=\"padding:6px;\">$\\frac{\\text{Change}}{\\text{Original}} \\times 100\\%$</td></tr><tr style=\"border-bottom:1px solid #334155;\"><td style=\"padding:6px; font-weight:bold; color:#f8fafc;\">Profit or Loss %</td><td style=\"padding:6px;\">Cost Price (CP)</td><td style=\"padding:6px;\">$\\frac{\\text{Profit or Loss}}{CP} \\times 100\\%$</td></tr><tr style=\"border-bottom:1px solid #334155;\"><td style=\"padding:6px; font-weight:bold; color:#f8fafc;\">Discount %</td><td style=\"padding:6px;\">Marked Price (MP)</td><td style=\"padding:6px;\">$\\frac{\\text{Discount}}{MP} \\times 100\\%$</td></tr><tr style=\"border-bottom:1px solid #334155;\"><td style=\"padding:6px; font-weight:bold; color:#f8fafc;\">Sales Tax / GST</td><td style=\"padding:6px;\">Selling Price (SP)</td><td style=\"padding:6px;\">$\\text{Tax} = \\frac{\\text{GST \\%}}{100} \\times SP$</td></tr><tr style=\"border-bottom:1px solid #334155;\"><td style=\"padding:6px; font-weight:bold; color:#f8fafc;\">Compound Interest</td><td style=\"padding:6px;\">Previous Balance</td><td style=\"padding:6px;\">$A = P\\left(1 + \\frac{R}{100}\\right)^n$</td></tr></tbody></table>",
        "sim_type": "base_blunder_debugger_matrix",
        "voice": "Always ask: percentage of what? Profit is on cost price, discount is on marked price, and percentage change is on the original starting value. This master table keeps you clear.",
        "checkpoints": [
            {
                "q": "A merchant calculates profit percentage on the Selling Price instead of Cost Price. If an article bought for ₹80 is sold for ₹100, what is the TRUE profit percentage?",
                "options": [
                    "20%",
                    "25%",
                    "15%",
                    "30%"
                ],
                "ans": 1,
                "feedback": "Correct! Profit = 100 - 80 = 20. The merchant erroneously thought 20/100 = 20%. But the TRUE profit % is on CP: (20/80) × 100% = 25%!"
            },
            {
                "q": "On which price is a trade discount calculated?",
                "options": [
                    "Cost Price (CP)",
                    "Selling Price (SP)",
                    "Marked Price (MP / List Price)",
                    "Total Bill Amount after tax"
                ],
                "ans": 2,
                "feedback": "Correct! Discounts are always deducted from the sticker Marked Price (MP)."
            }
        ]
    },
    {
        "id": 16,
        "title": "Percentage Riddles & Peaceful Knights",
        "subtitle": "Recreational Combinatorics: Knights on a Chessboard & Puzzles",
        "content": "<p>To conclude our journey into percentages, let us explore the famous mathematical recreational puzzle: <strong>The Peaceful Knights Problem</strong>.</p><h4>The Peaceful Knights Challenge:</h4><p>What is the maximum percentage of squares on an 8 × 8 chessboard (64 squares) that can be occupied by knights such that <strong>no two knights attack each other</strong>?</p><ul><li><strong>The Bipartite Color Invariance:</strong> A knight moves in an 'L-shape' (two squares in one direction, one square perpendicular). A knight on a <em>white</em> square can ONLY attack <em>black</em> squares, and vice versa!</li><li><strong>The Peaceful Solution:</strong> Place all knights exclusively on squares of the <strong>same color</strong> (e.g., all on white squares)!</li><li>Since every square attacked by a white-square knight is black, no two white-square knights can ever attack each other!</li><li>A chessboard has exactly 32 white squares and 32 black squares:$$\\mathbf{\\text{Maximum Coverage} = \\frac{32}{64} \\times 100\\% = \\mathbf{50\\%}}$$</li></ul><p>Exactly half (50%) of the chessboard can be filled peacefully!</p>",
        "sim_type": "peaceful_knights_chessboard_lab",
        "voice": "Welcome to the Peaceful Knights puzzle! Because a knight always leaps from a white square to a black square, placing knights only on white squares guarantees that none can attack another. Exactly 50 percent of the board can be peacefully occupied!",
        "checkpoints": [
            {
                "q": "In the Peaceful Knights puzzle on a 6 × 6 mini chessboard (36 total squares), what is the maximum number of non-attacking knights that can be placed?",
                "options": [
                    "12 knights",
                    "18 knights",
                    "20 knights",
                    "24 knights"
                ],
                "ans": 1,
                "feedback": "Correct! Exactly 50% of 36 = 18 squares of one color."
            },
            {
                "q": "Why can knights on the same color squares never attack one another?",
                "options": [
                    "Because knights can only attack pieces of the opposite color",
                    "Because every valid knight leap moves from a white square to a black square (or vice versa)",
                    "Because the board is rotated by 90 degrees",
                    "Because knights are blocked by pawns"
                ],
                "ans": 1,
                "feedback": "Correct! The L-shaped move alters square parity every single turn: white to black, or black to white."
            }
        ]
    },
    {
        "id": 17,
        "title": "Mastery Challenge — Part I (Questions 1 to 10)",
        "subtitle": "Foundations: Fractions into Percentages, FDP Conversions & Benchmarks",
        "content": "<p class='lead'>Welcome to Part I of the Mastery Assessment. Test your fluency with fractional conversions, anchor percentages, and benchmark mental arithmetic. Click <strong>💡 View Solution</strong> for full mathematical proofs.</p>",
        "sim_type": "quiz_slide",
        "quiz_range": [
            1,
            10
        ],
        "voice": "Welcome to Mastery Challenge 1. Solve the first ten questions testing foundations of fractions, percentages, and benchmark conversions. Click View Solution to examine the step-by-step mathematical reasoning.",
        "checkpoints": []
    },
    {
        "id": 18,
        "title": "Mastery Challenge — Part II (Questions 11 to 20)",
        "subtitle": "Applications: Percent of Values, Comparing Proportions & KYC Purity",
        "content": "<p class='lead'>In Part II, solve applied problems comparing disparate performance ratios, content purity standards (KYC), and percentage increases and decreases.</p>",
        "sim_type": "quiz_slide",
        "quiz_range": [
            11,
            20
        ],
        "voice": "In Part 2, we tackle practical real-world problems: comparing proportions, examining gold purity standards, and calculating percentage changes. Take your time and verify your deductions.",
        "checkpoints": []
    },
    {
        "id": 19,
        "title": "Mastery Challenge — Part III (Questions 21 to 30)",
        "subtitle": "Commerce: Cost Price, Selling Price, Profit/Loss, Discounts & GST",
        "content": "<p class='lead'>Part III tests your mastery of commercial mathematics: trading profits and losses, trade discount deductions, and Goods and Services Tax (GST) invoicing.</p>",
        "sim_type": "quiz_slide",
        "quiz_range": [
            21,
            30
        ],
        "voice": "Welcome to Part 3 on commercial arithmetic. Remember the cardinal rules: profit and loss are calculated on cost price, while discounts apply to the marked sticker price.",
        "checkpoints": []
    },
    {
        "id": 20,
        "title": "Mastery Challenge — Part IV (Questions 31 to 40)",
        "subtitle": "Advanced: Compounding, Depreciation, Paradoxes & Peaceful Knights",
        "content": "<p class='lead'>Congratulations on reaching the final frontier! Part IV features compound interest, asset depreciation, percentage traps, and chessboard combinatorial puzzles.</p>",
        "sim_type": "quiz_slide",
        "quiz_range": [
            31,
            40
        ],
        "voice": "Congratulations on reaching the final challenge! Part 4 covers compound growth, depreciation, percentage paradoxes, and the famous Peaceful Knights puzzle. Finish strong!",
        "checkpoints": []
    }
]



quiz_questions = [
    {
        "num": 1,
        "slide": 17,
        "question": "What is $\frac{7}{25}$ converted into a percentage?",
        "options": [
            "14%",
            "28%",
            "35%",
            "25%"
        ],
        "correct": 1,
        "solution": "To convert any fraction to a percentage, multiply by 00\\%$:\n34\frac{7}{25} \times 100\\% = 7 \times 4\\% = 28\\%34\nAlternatively, make the denominator 00$:\n34\frac{7 \times 4}{25 \times 4} = \frac{28}{100} = 28\\%34\nHence, the correct answer is $\\mathbf{28\\%}$."
    },
    {
        "num": 2,
        "slide": 17,
        "question": "If a student scores 6$ marks out of 0$ on a test, what percentage did they achieve?",
        "options": [
            "80%",
            "85%",
            "90%",
            "92%"
        ],
        "correct": 2,
        "solution": "Form the fraction of marks scored to total marks:\n34\text{Fraction} = \frac{36}{40} = \frac{9}{10}34\n\nMultiply by 00\\%$:\n34\frac{9}{10} \times 100\\% = 90\\%34\n\nThus, the score is $\\mathbf{90\\%}$."
    },
    {
        "num": 3,
        "slide": 17,
        "question": "Which decimal number is strictly equivalent to 2.5\\%0",
        "options": [
            "0.0125",
            "0.125",
            "1.25",
            "0.00125"
        ],
        "correct": 1,
        "solution": "To convert a percentage to a decimal, divide by 00$ (shift the decimal point $ places to the left):\n3412.5\\% = \frac{12.5}{100} = 0.12534\n\nAlso note that bash.125 = \frac{1}{8}$. Thus, the equivalent decimal is $\\mathbf{0.125}$."
    },
    {
        "num": 4,
        "slide": 17,
        "question": "Using mental benchmark decomposition, what is 5\\%$ of $\text{₹}4800",
        "options": [
            "₹48",
            "₹64",
            "₹72",
            "₹80"
        ],
        "correct": 2,
        "solution": "Decompose 5\\%$ into 0\\% + 5\\%$:\n3410\\% \text{ of } 480 = 480 \\div 10 = \text{₹}4834\n345\\% \text{ of } 480 = \text{half of } 10\\% = 48 \\div 2 = \text{₹}2434\n\nAdd the benchmarks together:\n3415\\% = 48 + 24 = \\mathbf{\text{₹}72}34."
    },
    {
        "num": 5,
        "slide": 17,
        "question": "What is $\frac{9}{4}$ expressed as a percentage?",
        "options": [
            "175%",
            "225%",
            "250%",
            "300%"
        ],
        "correct": 1,
        "solution": "Since the numerator exceeds the denominator, this improper fraction represents a value greater than 00\\%$:\n34\frac{9}{4} = 2\frac{1}{4} = 2 + 0.2534\n\nMultiplying by 00\\%$:\n34\frac{9}{4} \times 100\\% = 9 \times 25\\% = 225\\%34\n\nTherefore, $\frac{9}{4} = \\mathbf{225\\%}$."
    },
    {
        "num": 6,
        "slide": 17,
        "question": "A water bottle contains 50\text{ mL}$ when filled to 5\\%$ of its capacity. What is its full capacity?",
        "options": [
            "900 mL",
            "1000 mL",
            "1100 mL",
            "1250 mL"
        ],
        "correct": 1,
        "solution": "Let total capacity be \text{ mL}$.\n3475\\% \text{ of } C = 75034\n34\frac{3}{4}C = 750 \\implies C = 750 \times \frac{4}{3} = 250 \times 4 = 1000\text{ mL}34\n\nThe total capacity is $\\mathbf{1000\text{ mL}}$ (or \text{ litre}$)."
    },
    {
        "num": 7,
        "slide": 17,
        "question": "What is 50\\%$ of 00",
        "options": [
            "160",
            "200",
            "240",
            "280"
        ],
        "correct": 1,
        "solution": "Recall that 50\\% = 200\\% + 50\\% = 2 + 0.5 = 2.5$:\n34250\\% \text{ of } 80 = 2.5 \times 8034\n342 \times 80 = 16034\n340.5 \times 80 = 4034\n34160 + 40 = 20034\n\nOr via fraction: $\frac{5}{2} \times 80 = 5 \times 40 = \\mathbf{200}$."
    },
    {
        "num": 8,
        "slide": 17,
        "question": "If 5\\%$ of a number is 40$, what is 0\\%$ of that same number?",
        "options": [
            "200",
            "240",
            "280",
            "320"
        ],
        "correct": 1,
        "solution": "First find \\%$ or the full number:\n3435\\% \to 140 \\implies 1\\% = \frac{140}{35} = 434\n\nNow compute 0\\%$:\n3460\\% = 60 \times 4 = \\mathbf{240}34\n\n(The original number is 00 \times 4 = 400$, and 0\\% \text{ of } 400 = 240$.)"
    },
    {
        "num": 9,
        "slide": 17,
        "question": "A phone battery drops from 0\\%$ to 0\\%$. What percentage of its remaining charge was lost?",
        "options": [
            "60%",
            "75%",
            "66.67%",
            "50%"
        ],
        "correct": 1,
        "solution": "Read carefully: the drop in battery percentage points is 0 - 20 = 60\\%$.\n\nTo find the percentage *of its initial charge* (0\\%$) that was drained:\n34\text{Fraction drained} = \frac{60}{80} = \frac{3}{4} = 75\\%34\n\nSo $\\mathbf{75\\%}$ of its starting charge was consumed."
    },
    {
        "num": 10,
        "slide": 17,
        "question": "Which of the following is the largest quantity?",
        "options": [
            "30% of 120",
            "25% of 160",
            "50% of 75",
            "40% of 95"
        ],
        "correct": 1,
        "solution": "Calculate each value:\n1. 0\\% \text{ of } 120 = 0.3 \times 120 = 36$\n2. 5\\% \text{ of } 160 = \frac{1}{4} \times 160 = 40$\n3. 0\\% \text{ of } 75 = 37.5$\n4. 0\\% \text{ of } 95 = 0.4 \times 95 = 38$\n\nComparing the values: 0 > 38 > 37.5 > 36$. Thus, $\\mathbf{25\\% \text{ of } 160}$ is the largest."
    },
    {
        "num": 11,
        "slide": 18,
        "question": "Class 8A had 8$ students out of 5$ score an A, while Class 8B had 1$ students out of 0$ score an A. Which class had a higher success rate?",
        "options": [
            "Class 8A (72%)",
            "Class 8B (70%)",
            "Both had exactly equal rates",
            "Cannot be compared"
        ],
        "correct": 0,
        "solution": "Normalize both fractions to percentages:\n34\text{Class 8A} = \frac{18}{25} \times 100\\% = 18 \times 4\\% = 72\\%34\n34\text{Class 8B} = \frac{21}{30} \times 100\\% = \frac{7}{10} \times 100\\% = 70\\%34\n\nSince 2\\% > 70\\%$, $\\mathbf{\text{Class 8A}}$ had the higher proportion."
    },
    {
        "num": 12,
        "slide": 18,
        "question": "An ornament is made of 8\text{-karat}$ gold. Given that pure gold is 4\text{ karats}$, what is the gold purity percentage?",
        "options": [
            "70%",
            "75%",
            "80%",
            "82.5%"
        ],
        "correct": 1,
        "solution": "Gold purity is calculated as:\n34\text{Purity } \\% = \frac{\text{Karats}}{24} \times 100\\%34\n34\text{Purity} = \frac{18}{24} \times 100\\% = \frac{3}{4} \times 100\\% = \\mathbf{75\\%}34\n\nThe remaining 5\\%$ consists of alloy metals (copper, silver)."
    },
    {
        "num": 13,
        "slide": 18,
        "question": "The price of petrol increased from $\text{₹}80$ to $\text{₹}100$ per litre. What is the percentage increase?",
        "options": [
            "20%",
            "25%",
            "15%",
            "22.5%"
        ],
        "correct": 1,
        "solution": "The percentage change formula always divides by the **initial (base) value**:\n34\\Delta = 100 - 80 = \text{₹}2034\n34\text{Percentage Increase} = \frac{\\Delta}{\text{Original Base}} \times 100\\% = \frac{20}{80} \times 100\\% = \frac{1}{4} \times 100\\% = \\mathbf{25\\%}34."
    },
    {
        "num": 14,
        "slide": 18,
        "question": "A shopkeeper bought a book for $\text{₹}400$ and sold it for $\text{₹}500$. Find the profit percentage.",
        "options": [
            "20%",
            "25%",
            "22.5%",
            "30%"
        ],
        "correct": 1,
        "solution": "Cost Price ($\text{CP}$) = $\text{₹}400$, Selling Price ($\text{SP}$) = $\text{₹}500$.\n34\text{Profit} = \text{SP} - \text{CP} = 500 - 400 = \text{₹}10034\n\nProfit percentage is always computed over the Cost Price:\n34\text{Profit } \\% = \frac{\text{Profit}}{\text{CP}} \times 100\\% = \frac{100}{400} \times 100\\% = \\mathbf{25\\%}34."
    },
    {
        "num": 15,
        "slide": 18,
        "question": "A cycle purchased for $\text{₹}2500$ was sold at a loss of 2\\%$. What was the selling price?",
        "options": [
            "₹2100",
            "₹2200",
            "₹2250",
            "₹2300"
        ],
        "correct": 1,
        "solution": "34\text{Loss} = 12\\% \text{ of } \text{₹}2500 = \frac{12}{100} \times 2500 = 12 \times 25 = \text{₹}30034\n\n34\text{SP} = \text{CP} - \text{Loss} = 2500 - 300 = \\mathbf{\text{₹}2200}34\n\nAlternatively: $\text{SP} = (100\\% - 12\\%) \times 2500 = 88\\% \times 2500 = 0.88 \times 2500 = \text{₹}2200$."
    },
    {
        "num": 16,
        "slide": 18,
        "question": "By selling a jacket for $\text{₹}1440$, a merchant makes a 0\\%$ profit. What was the cost price of the jacket?",
        "options": [
            "₹1152",
            "₹1200",
            "₹1240",
            "₹1250"
        ],
        "correct": 1,
        "solution": "Since $\text{Profit} = 20\\%$, the selling price represents 20\\%$ of the cost price:\n34\text{SP} = 1.20 \times \text{CP}34\n341440 = 1.20 \times \text{CP} \\implies \text{CP} = \frac{1440}{1.2} = \frac{14400}{12} = \\mathbf{\text{₹}1200}34\n\n*Common Blunder Alert*: Do NOT subtract 0\\%$ from 440$; 0\\%$ was gained on the *cost price*, not the selling price!"
    },
    {
        "num": 17,
        "slide": 18,
        "question": "A sample of 00\text{ g}$ of cereal contains 5\text{ g}$ of sugar. What is the sugar percentage on the nutrition label?",
        "options": [
            "4.5%",
            "9%",
            "10%",
            "11.5%"
        ],
        "correct": 1,
        "solution": "34\text{Percentage} = \frac{\text{Mass of sugar}}{\text{Total mass}} \times 100\\%34\n34\text{Percentage} = \frac{45}{500} \times 100\\% = \frac{45}{5} = \\mathbf{9\\%}34."
    },
    {
        "num": 18,
        "slide": 18,
        "question": "The population of a village decreased from 2,500$ to 1,000$. What was the percentage decrease?",
        "options": [
            "10%",
            "12%",
            "14%",
            "15%"
        ],
        "correct": 1,
        "solution": "34\text{Decrease} = 12500 - 11000 = 150034\n34\text{Percentage Decrease} = \frac{1500}{12500} \times 100\\% = \frac{15}{125} \times 100\\% = \frac{3}{25} \times 100\\% = \\mathbf{12\\%}34."
    },
    {
        "num": 19,
        "slide": 18,
        "question": "If an item bought for $\text{₹}600$ is sold for $\text{₹}540$, what is the loss percentage?",
        "options": [
            "5%",
            "10%",
            "12%",
            "15%"
        ],
        "correct": 1,
        "solution": "34\text{Loss} = \text{CP} - \text{SP} = 600 - 540 = \text{₹}6034\n34\text{Loss } \\% = \frac{60}{600} \times 100\\% = \\mathbf{10\\%}34."
    },
    {
        "num": 20,
        "slide": 18,
        "question": "A baker sells a cake at a 5\\%$ profit. If the profit earned is $\text{₹}75$, what is the selling price?",
        "options": [
            "₹300",
            "₹350",
            "₹375",
            "₹400"
        ],
        "correct": 2,
        "solution": "3425\\% \text{ of } \text{CP} = 75 \\implies \frac{1}{4} \times \text{CP} = 75 \\implies \text{CP} = 75 \times 4 = \text{₹}30034\n\nNow compute Selling Price:\n34\text{SP} = \text{CP} + \text{Profit} = 300 + 75 = \\mathbf{\text{₹}375}34."
    },
    {
        "num": 21,
        "slide": 19,
        "question": "A shirt has a Marked Price (MP) of $\text{₹}800$. The store offers a 5\\%$ discount. What is the selling price?",
        "options": [
            "₹660",
            "₹680",
            "₹700",
            "₹720"
        ],
        "correct": 1,
        "solution": "Discount is always calculated on the **Marked Price**:\n34\text{Discount} = 15\\% \text{ of } 800 = \frac{15}{100} \times 800 = \text{₹}12034\n34\text{Selling Price (SP)} = \text{MP} - \text{Discount} = 800 - 120 = \\mathbf{\text{₹}680}34."
    },
    {
        "num": 22,
        "slide": 19,
        "question": "An electronic gadget priced at $\text{₹}5000$ attracts an 8\\%$ Goods and Services Tax (GST). What is the total bill amount?",
        "options": [
            "₹5800",
            "₹5900",
            "₹6000",
            "₹6200"
        ],
        "correct": 1,
        "solution": "34\text{GST Amount} = 18\\% \text{ of } 5000 = \frac{18}{100} \times 5000 = 18 \times 50 = \text{₹}90034\n34\text{Total Invoice Bill} = \text{Price} + \text{GST} = 5000 + 900 = \\mathbf{\text{₹}5900}34."
    },
    {
        "num": 23,
        "slide": 19,
        "question": "A customer bought a tennis racket for $\text{₹}1770$ including 8\\%$ GST. What was the base price before tax?",
        "options": [
            "₹1450",
            "₹1500",
            "₹1550",
            "₹1600"
        ],
        "correct": 1,
        "solution": "Let the base pre-tax price be $.\n34\text{Total} = B + 0.18 B = 1.18 B = 177034\n34B = \frac{1770}{1.18} = \frac{177000}{118} = \\mathbf{\text{₹}1500}34\n\nVerify: 8\\% \text{ of } 1500 = 270$, and 500 + 270 = 1770$."
    },
    {
        "num": 24,
        "slide": 19,
        "question": "A principal of $\text{₹}10,000$ is invested at 0\\%$ per annum compounded annually for $ years. Find the compounded amount $.",
        "options": [
            "₹12,000",
            "₹12,100",
            "₹12,200",
            "₹12,500"
        ],
        "correct": 1,
        "solution": "Using the compound interest formula  = P\\left(1 + \frac{r}{100}\right)^n$:\n34A = 10000\\left(1 + \frac{10}{100}\right)^2 = 10000(1.1)^2 = 10000 \times 1.21 = \\mathbf{\text{₹}12,100}34\n\nNotice the compound interest is 2100 - 10000 = \text{₹}2100$, which includes $\text{₹}100$ interest-on-interest."
    },
    {
        "num": 25,
        "slide": 19,
        "question": "What is the Compound Interest (CI) earned on $\text{₹}8000$ at \\%$ per annum for $ years compounded annually?",
        "options": [
            "₹800",
            "₹820",
            "₹840",
            "₹850"
        ],
        "correct": 1,
        "solution": "34A = 8000\\left(1 + \frac{5}{100}\right)^2 = 8000 \times \\left(\frac{21}{20}\right)^2 = 8000 \times \frac{441}{400} = 20 \times 441 = \text{₹}882034\n34\text{CI} = A - P = 8820 - 8000 = \\mathbf{\text{₹}820}34\n\n(Simple interest would have been 000 \times 0.05 \times 2 = \text{₹}800$; the extra $\text{₹}20$ is \\%$ of Year 1 interest $\text{₹}400$.)"
    },
    {
        "num": 26,
        "slide": 19,
        "question": "A new motorcycle bought for $\text{₹}80,000$ depreciates at 0\\%$ per year. What is its value after $ years?",
        "options": [
            "₹64,000",
            "₹64,800",
            "₹65,000",
            "₹72,000"
        ],
        "correct": 1,
        "solution": "Depreciation formula:  = P\\left(1 - \frac{r}{100}\right)^n$:\n34V = 80000\\left(1 - \frac{10}{100}\right)^2 = 80000 \times (0.9)^2 = 80000 \times 0.81 = \\mathbf{\text{₹}64,800}34\n\nStep-by-step: After Year 1: 0000 - 8000 = 72000$. After Year 2: 2000 - 7200 = \text{₹}64,800$."
    },
    {
        "num": 27,
        "slide": 19,
        "question": "The population of a city is 00,000$ and grows at \\%$ annually. What will the population be after $ year?",
        "options": [
            "205,000",
            "210,000",
            "215,000",
            "220,000"
        ],
        "correct": 1,
        "solution": "Growth amount $= 5\\% \text{ of } 200,000 = \frac{5}{100} \times 200,000 = 10,000$.\n34\text{New Population} = 200,000 + 10,000 = \\mathbf{210,000}34."
    },
    {
        "num": 28,
        "slide": 19,
        "question": "A refrigerator marked at $\text{₹}20,000$ is sold with successive discounts of 0\\%$ and \\%$. What is the final selling price?",
        "options": [
            "₹17,000",
            "₹17,100",
            "₹17,200",
            "₹17,500"
        ],
        "correct": 1,
        "solution": "Apply successive multipliers:\n34\text{SP} = 20000 \times (1 - 0.10) \times (1 - 0.05) = 20000 \times 0.90 \times 0.9534\n3420000 \times 0.90 = 1800034\n3418000 \times 0.95 = 18000 - 900 = \\mathbf{\text{₹}17,100}34\n\n*Note*: Successive discounts are NOT simply added (0\\% + 5\\% \ne 15\\%$, the effective discount is 4.5\\%$)."
    },
    {
        "num": 29,
        "slide": 19,
        "question": "In a laboratory culture, bacteria count increases by 0\\%$ every hour. If initial count is 0,000$, what is the count after $ hours?",
        "options": [
            "55,000",
            "60,000",
            "60,500",
            "61,000"
        ],
        "correct": 2,
        "solution": "Using exponential growth:\n34N_2 = N_0(1 + 0.10)^2 = 50000 \times 1.21 = \\mathbf{60,500}34\n\nHour 1: 0000 + 5000 = 55000$.\nHour 2: 5000 + 5500 = 60500$."
    },
    {
        "num": 30,
        "slide": 19,
        "question": "A pair of shoes with marked price $\text{₹}1200$ is sold at a 0\\%$ discount. If sales tax of \\%$ is levied on the discounted price, what is the final cash paid?",
        "options": [
            "₹1120",
            "₹1134",
            "₹1140",
            "₹1150"
        ],
        "correct": 1,
        "solution": "Step 1: Calculate discounted price (taxable value):\n34\text{Discounted Price} = 1200 - (10\\% \text{ of } 1200) = 1200 - 120 = \text{₹}108034\nStep 2: Add \\%$ sales tax on the discounted price:\n34\text{Tax} = 5\\% \text{ of } 1080 = 0.05 \times 1080 = \text{₹}5434\n34\text{Final Cash} = 1080 + 54 = \\mathbf{\text{₹}1134}34."
    },
    {
        "num": 31,
        "slide": 20,
        "question": "A share price increases by 0\\%$ on Monday, but falls by 0\\%$ on Tuesday. Compared to the original price, the final price is:",
        "options": [
            "Equal to original",
            "4% higher",
            "4% lower",
            "2% lower"
        ],
        "correct": 2,
        "solution": "Let initial price be 00$:\n- Monday (+20%): 00 \times 1.20 = 120$\n- Tuesday (-20% of 120): 20 \times 0.80 = 96$\n\nNet change: 6 - 100 = -4$, which represents a **4% decrease**!\n34\text{Multiplier} = (1 + 0.20)(1 - 0.20) = 1 - 0.04 = 0.96 \\implies \\mathbf{4\\% \text{ lower}}34."
    },
    {
        "num": 32,
        "slide": 20,
        "question": "According to the percentage reversibility principle, which of the following is equivalent to 6\\%$ of 50",
        "options": [
            "25% of 16",
            "16% of 50",
            "8% of 25",
            "32% of 50"
        ],
        "correct": 0,
        "solution": "The percentage reversibility law states:\n34x\\% \text{ of } y = \frac{x \times y}{100} = \frac{y \times x}{100} = y\\% \text{ of } x34\n\nThus, 6\\% \text{ of } 25 = 25\\% \text{ of } 16 = \frac{1}{4} \times 16 = \\mathbf{4}$.\n\nHence, it is identically $\\mathbf{25\\% \text{ of } 16}$."
    },
    {
        "num": 33,
        "slide": 20,
        "question": "Salary of an employee is reduced by 5\\%$. By what percentage must the new reduced salary be increased to restore the original salary?",
        "options": [
            "25%",
            "30%",
            "33.33%",
            "50%"
        ],
        "correct": 2,
        "solution": "Let original salary be 00$.\nReduced salary $= 100 - 25 = 75$.\n\nTo return from 5$ back to 00$, an increment of 5$ is needed on the NEW base of 5$:\n34\text{Required Increase} = \frac{25}{75} \times 100\\% = \frac{1}{3} \times 100\\% = \\mathbf{33.33\\%}34\n\nBecause the base has shrunk, a larger percentage is required to recover!"
    },
    {
        "num": 34,
        "slide": 20,
        "question": "In the Peaceful Knights chess problem, what is the maximum percentage of squares on an  \times 8$ board that can be occupied without any two knights attacking each other?",
        "options": [
            "25%",
            "32%",
            "50%",
            "64%"
        ],
        "correct": 2,
        "solution": "An  \times 8$ chessboard contains 4$ squares (2$ light, 2$ dark).\nA knight always moves from a light square to a dark square, and vice versa.\n\nIf all knights are placed strictly on squares of the same colour (e.g. all 32 on light squares), **no knight can attack another knight**!\n34\text{Maximum Peaceful Knights} = 3234\n34\text{Percentage coverage} = \frac{32}{64} \times 100\\% = \\mathbf{50\\%}34."
    },
    {
        "num": 35,
        "slide": 20,
        "question": "If $ earns 5\\%$ more than $, by what percentage does $ earn less than 0",
        "options": [
            "25%",
            "20%",
            "15%",
            "18.5%"
        ],
        "correct": 1,
        "solution": "Let  = 100$. Then  = 125$.\nDifference $= 125 - 100 = 25$.\n\nTo calculate how much less $ is relative to $, use $ as the base:\n34\text{Percentage less} = \frac{25}{A} \times 100\\% = \frac{25}{125} \times 100\\% = \frac{1}{5} \times 100\\% = \\mathbf{20\\%}34."
    },
    {
        "num": 36,
        "slide": 20,
        "question": "What single discount is equivalent to two successive discounts of 0\\%$ and 0\\%0",
        "options": [
            "30%",
            "28%",
            "26%",
            "25%"
        ],
        "correct": 1,
        "solution": "Net multiplier for successive discounts:\n34(1 - 0.20)(1 - 0.10) = 0.80 \times 0.90 = 0.7234\n34\text{Equivalent Single Discount} = (1 - 0.72) \times 100\\% = \\mathbf{28\\%}34\n\nOr formula:  + d_2 - \frac{d_1 d_2}{100} = 20 + 10 - \frac{200}{100} = 30 - 2 = 28\\%$."
    },
    {
        "num": 37,
        "slide": 20,
        "question": "If the length of a rectangle increases by 0\\%$ and its breadth decreases by 0\\%$, how does its area change?",
        "options": [
            "Remains unchanged",
            "Decreases by 4%",
            "Increases by 4%",
            "Decreases by 2%"
        ],
        "correct": 1,
        "solution": "Let initial dimensions be $ and $, initial area  = LB$.\n34L_{new} = 1.20 L, \\quad B_{new} = 0.80 B34\n34A_{new} = 1.20 L \times 0.80 B = 0.96 LB = 0.96 A_034\n\nChange $= 0.96 - 1.00 = -0.04$, meaning the area **decreases by 4%**."
    },
    {
        "num": 38,
        "slide": 20,
        "question": "A merchant falsely marks up an item by 0\\%$ and then announces a discount of 0\\%$. Does he break even?",
        "options": [
            "Yes, he breaks even",
            "No, he suffers a 16% loss",
            "No, he makes a 16% gain",
            "No, he suffers an 8% loss"
        ],
        "correct": 1,
        "solution": "Let Cost Price be $\text{₹}100$.\nMarked Price $= 100 + 40 = \text{₹}140$.\nDiscount $= 40\\% \text{ of } 140 = 0.40 \times 140 = \text{₹}56$.\nSelling Price $= 140 - 56 = \text{₹}84$.\n\n34\text{Loss} = 100 - 84 = \text{₹}16 \\implies \\mathbf{16\\% \text{ loss}}34.\nMultiplier: .40 \times 0.60 = 0.84 = 1 - 0.16$."
    },
    {
        "num": 39,
        "slide": 20,
        "question": "On an  \times n$ chessboard, what is the maximum number of peaceful knights (where no two knights can attack one another)?",
        "options": [
            "n",
            "2n",
            "n²/2 (rounded up)",
            "n² - 1"
        ],
        "correct": 2,
        "solution": "Since every move of a knight changes the square colour, all squares of one colour form an independent set.\n\nFor an  \times n$ board with ^2$ squares:\n34\text{Maximum Knights} = \\left\\lceil \frac{n^2}{2} \right\rceil34\nFor even =8$: $\frac{64}{2} = 32$ knights (0\\%$ coverage).\nFor odd =5$: $\\lceil 25/2 \rceil = 13$ knights."
    },
    {
        "num": 40,
        "slide": 20,
        "question": "A vessel has 0\text{ L}$ of a solution containing 0\\%$ alcohol. How many litres of pure alcohol must be added to make it a 6\\%$ solution?",
        "options": [
            "10 L",
            "12 L",
            "15 L",
            "18 L"
        ],
        "correct": 2,
        "solution": "Initial alcohol $= 20\\% \text{ of } 60 = 12\text{ L}$. Water $= 48\text{ L}$.\n\nLet \text{ L}$ of pure alcohol be added.\nNew total volume $= 60 + x$, and total alcohol $= 12 + x$.\n34\frac{12 + x}{60 + x} = \frac{36}{100} = \frac{9}{25}34\n3425(12 + x) = 9(60 + x)34\n34300 + 25x = 540 + 9x34\n3416x = 240 \\implies x = \frac{240}{16} = \\mathbf{15\text{ L}}34.\n\nCheck: Total alcohol $= 12 + 15 = 27\text{ L}$. Total volume $= 75\text{ L}$. $\frac{27}{75} = \frac{9}{25} = 36\\%$."
    }
]
