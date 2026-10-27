# Data for Class 8 Mathematics Chapter 10: Advanced Proportional Reasoning & Inverse Variation

slides_data = [
    {
        "id": 1,
        "title": "Proportional Reasoning: Core Fundamentals",
        "subtitle": "Multiplicative Scaling & The Logic of Covariation",
        "sim_type": "proportional_reasoning_foundations",
        "voice": "Welcome to our laboratory on Advanced Proportional Reasoning and Inverse Proportions. Proportional reasoning is the mathematical ability to analyze how two or more changing quantities scale together.",
        "content": "\n<h4>The Nature of Proportional Reasoning</h4>\n<p>Proportional reasoning is the cornerstone of advanced mathematics, science, engineering, and everyday economics. It moves beyond simple addition and subtraction into the realm of <strong>multiplicative relationships</strong>.</p>\n<ul>\n  <li><strong>Additive Thinking:</strong> Focuses on absolute differences ($B - A = \\text{constant}$).</li>\n  <li><strong>Multiplicative (Proportional) Thinking:</strong> Focuses on constant ratios or products ($\\\\frac{y}{x} = k$ or $x \\times y = k$).</li>\n</ul>\n<div style=\"background:#0f172a; border-left:4px solid #6366f1; padding:12px; margin:12px 0; border-radius:6px;\">\n  $$\\mathbf{\\text{Direct Variation: } \\frac{y}{x} = k} \\quad \\Longleftrightarrow \\quad \\mathbf{\\text{Inverse Variation: } x \\times y = k}$$\n</div>\n<p>In this chapter, we extend proportional reasoning into multi-term ratios ($a : b : c$), architectural map scales, pie chart sector distributions (\"A Slice of the Pie\"), and the vital physics of inverse proportions.</p>\n",
        "checkpoints": [
            {
                "q": "What distinguishes proportional thinking from additive thinking?",
                "options": [
                    "Proportional thinking analyzes constant multiplicative factors and ratios rather than fixed differences",
                    "Proportional thinking only works for negative numbers",
                    "Proportional thinking avoids all fractions",
                    "Proportional thinking is limited to geometry"
                ],
                "ans": 0,
                "feedback": "Proportional reasoning focuses on multiplicative invariance—constant scaling factors and ratios between quantities."
            },
            {
                "q": "If 4 pens cost ₹60, what is the unit price of one pen?",
                "options": [
                    "₹12",
                    "₹15",
                    "₹16",
                    "₹20"
                ],
                "ans": 1,
                "feedback": "Unit rate $k = \\frac{60}{4} = \\mathbf{₹15}$ per pen."
            }
        ]
    },
    {
        "id": 2,
        "title": "Proportionality Recap: Direct Variation",
        "subtitle": "The Constant Ratio Law: y / x = k",
        "sim_type": "proportionality_direct_variation_recap",
        "voice": "In direct proportionality, two quantities increase or decrease together such that their ratio remains constant. When graphed, direct variation forms a straight line passing through the origin.",
        "content": "\n<h4>The Law of Direct Proportionality</h4>\n<p>Two quantities $x$ and $y$ are said to be in <strong>direct proportion</strong> (written as $x \\propto y$) if an increase in $x$ causes a proportional increase in $y$, and vice versa, such that:</p>\n<div style=\"background:#0f172a; border-left:4px solid #10b981; padding:12px; margin:12px 0; border-radius:6px;\">\n  $$\\mathbf{\\frac{y}{x} = k \\quad \\text{or} \\quad y = kx \\quad (k > 0)}$$\n</div>\n<p>Here, $k$ is called the <strong>constant of proportionality</strong> (or the constant unit rate).</p>\n<h4>Two-Point Equivalence Formula</h4>\n<p>If $x_1$ corresponds to $y_1$, and $x_2$ corresponds to $y_2$, then:</p>\n$$\\mathbf{\\frac{x_1}{y_1} = \\frac{x_2}{y_2}} \\quad \\Longleftrightarrow \\quad \\mathbf{x_1 y_2 = x_2 y_1}$$\n<h4>Everyday Examples</h4>\n<ul>\n  <li>Distance covered at constant speed vs time elapsed ($d = v \\cdot t$).</li>\n  <li>Total cost of identical grocery items vs quantity purchased.</li>\n  <li>Amount of petrol consumed vs distance traveled by a vehicle.</li>\n</ul>\n",
        "checkpoints": [
            {
                "q": "If $x$ and $y$ vary directly, and $y = 36$ when $x = 4$, what is the constant of proportionality $k$?",
                "options": [
                    "6",
                    "8",
                    "9",
                    "12"
                ],
                "ans": 2,
                "feedback": "$k = \\frac{y}{x} = \\frac{36}{4} = \\mathbf{9}$."
            },
            {
                "q": "A car travels $150\\text{ km}$ on $10\\text{ litres}$ of petrol. How far will it travel on $25\\text{ litres}$ at the same rate?",
                "options": [
                    "300 km",
                    "350 km",
                    "375 km",
                    "400 km"
                ],
                "ans": 2,
                "feedback": "$\\frac{150}{10} = \\frac{D}{25} \\implies 15 \\times 25 = \\mathbf{375\\text{ km}}$."
            }
        ]
    },
    {
        "id": 3,
        "title": "Ratios in Maps: Scale & Representation",
        "subtitle": "The Representative Fraction (R.F.) & Ground Distances",
        "sim_type": "map_scale_rf_navigator",
        "voice": "Maps represent vast landscapes on a compact sheet of paper. The map scale tells us exactly how much a real-world distance has been scaled down.",
        "content": "\n<h4>Understanding Map Scales</h4>\n<p>A <strong>map scale</strong> is the ratio of a distance measured on the map to the actual physical distance on the ground.</p>\n$$\\mathbf{\\text{Scale}} = \\frac{\\text{Distance on Map}}{\\text{Actual Distance on Ground}}$$\n<h4>The Representative Fraction (R.F.)</h4>\n<p>When the ratio is expressed in identical units (with a numerator of $1$ and no physical unit attached), it is called the <strong>Representative Fraction (R.F.)</strong>:</p>\n<div style=\"background:#0f172a; border-left:4px solid #38bdf8; padding:12px; margin:12px 0; border-radius:6px;\">\n  $$\\mathbf{\\text{R.F.} = \\frac{1}{n} \\quad \\text{or} \\quad 1 : n}$$\n</div>\n<p>For example, a scale of $1\\text{ cm} = 5\\text{ km}$:</p>\n$$5\\text{ km} = 5 \\times 1000\\text{ m} = 5000 \\times 100\\text{ cm} = 500,000\\text{ cm}$$\n$$\\mathbf{\\text{R.F.} = \\frac{1\\text{ cm}}{500,000\\text{ cm}} = 1 : 500,000}$$\n<p>Every $1\\text{ cm}$ measured on the map corresponds to five hundred thousand centimeters ($5\\text{ km}$) in the real world.</p>\n",
        "checkpoints": [
            {
                "q": "On a city map with scale $1\\text{ cm} = 2\\text{ km}$, two metro stations are $4.5\\text{ cm}$ apart. What is the real distance between them?",
                "options": [
                    "6.5 km",
                    "8 km",
                    "9 km",
                    "10 km"
                ],
                "ans": 2,
                "feedback": "$\\text{Actual distance} = 4.5 \\times 2\\text{ km} = \\mathbf{9\\text{ km}}$."
            },
            {
                "q": "What is the Representative Fraction (R.F.) for a scale of $2\\text{ cm} = 1\\text{ km}$?",
                "options": [
                    "1 : 50,000",
                    "1 : 100,000",
                    "1 : 200,000",
                    "1 : 500,000"
                ],
                "ans": 0,
                "feedback": "$1\\text{ km} = 100,000\\text{ cm}$. R.F. $= \\frac{2\\text{ cm}}{100,000\\text{ cm}} = \\mathbf{1 : 50,000}$."
            }
        ]
    },
    {
        "id": 4,
        "title": "Scale Models & Architectural Blueprints",
        "subtitle": "Engineering Drawings, Reductions & Enlargements",
        "sim_type": "blueprint_scale_model_studio",
        "voice": "Architects and engineers use proportional scaling to design buildings, bridges, and microscopic components. Every single dimension must scale by the exact same multiplier.",
        "content": "\n<h4>Proportions in Architectural Blueprints</h4>\n<p>A blueprint is a precision technical drawing where every physical dimension of a building is proportionally reduced by a constant scale factor.</p>\n<ul>\n  <li><strong>Reduction Scale:</strong> Scale $< 1$ (e.g. $1 : 50$, $1 : 100$ for houses and buildings).</li>\n  <li><strong>Enlargement Scale:</strong> Scale $> 1$ (e.g. $10 : 1$, $50 : 1$ for microchips and watch gears).</li>\n</ul>\n<h4>Linear Dimensions vs Area Scaling</h4>\n<p>A crucial rule in proportional geometry:</p>\n<div style=\"background:#0f172a; border-left:4px solid #f59e0b; padding:12px; margin:12px 0; border-radius:6px;\">\n  $$\\text{If Linear Dimensions scale as } \\mathbf{1 : k}, \\quad \\text{then Geometric Areas scale as } \\mathbf{1 : k^2}$$\n</div>\n<p>If a room's blueprint scale is $1 : 50$ (lengths are $1/50$th of actual size), then the area on paper is $\\left(\\frac{1}{50}\\right)^2 = \\frac{1}{2500}$th of the real floor area!</p>\n",
        "checkpoints": [
            {
                "q": "On a blueprint with scale $1 : 100$, a bedroom measures $5\\text{ cm} \\times 4\\text{ cm}$. What are the real dimensions of the room?",
                "options": [
                    "5 m × 4 m",
                    "50 m × 40 m",
                    "2.5 m × 2 m",
                    "10 m × 8 m"
                ],
                "ans": 0,
                "feedback": "$5\\text{ cm} \\times 100 = 500\\text{ cm} = 5\\text{ m}$, and $4\\text{ cm} \\times 100 = 400\\text{ cm} = 4\\text{ m}$. Real size is $\\mathbf{5\\text{ m} \\times 4\\text{ m}}$."
            },
            {
                "q": "If the length of a model car is scaled at $1 : 20$, by what factor is the surface area of the model reduced compared to the actual car?",
                "options": [
                    "1 / 20",
                    "1 / 40",
                    "1 / 400",
                    "1 / 8000"
                ],
                "ans": 2,
                "feedback": "Area scales quadratically: $\\left(\\frac{1}{20}\\right)^2 = \\mathbf{\\frac{1}{400}}$."
            }
        ]
    },
    {
        "id": 5,
        "title": "Ratios with More than 2 Terms",
        "subtitle": "Three-Way Extended Ratios: a : b : c",
        "sim_type": "multi_term_triplet_ratio_mixer",
        "voice": "In many practical recipes and chemical mixtures, we compare three or more ingredients simultaneously. A three-term ratio compares all parts in a single unified relationship.",
        "content": "\n<h4>Definition of Extended Multi-Term Ratios</h4>\n<p>When three quantities $A$, $B$, and $C$ are compared simultaneously in fixed proportions, their relationship is written as an <strong>extended ratio</strong>:</p>\n<div style=\"background:#0f172a; border-left:4px solid #a855f7; padding:12px; margin:12px 0; border-radius:6px;\">\n  $$\\mathbf{A : B : C = a : b : c}$$\n</div>\n<h4>Concrete Mixture Example</h4>\n<p>Standard construction mortar is mixed in the ratio <strong>1 : 2 : 4</strong> (Cement : Sand : Gravel):</p>\n<ul>\n  <li>For every $1\\text{ bag}$ of cement, you need $2\\text{ bags}$ of sand and $4\\text{ bags}$ of gravel.</li>\n  <li>Total parts $= 1 + 2 + 4 = 7\\text{ parts}$.</li>\n  <li>Fraction of cement $= \\frac{1}{7}$, Sand $= \\frac{2}{7}$, Gravel $= \\frac{4}{7}$.</li>\n</ul>\n<h4>The Triangle Angle Ratio</h4>\n<p>If the angles of a triangle are in the ratio $2 : 3 : 4$, their sum must be $180^\\circ$:</p>\n$$2x + 3x + 4x = 180^\\circ \\implies 9x = 180^\\circ \\implies x = 20^\\circ$$\n$$\\text{Angles are: } 40^\\circ, \\; 60^\\circ, \\; 80^\\circ$$\n",
        "checkpoints": [
            {
                "q": "The angles of a triangle are in the ratio $1 : 2 : 3$. What is the measure of the largest angle?",
                "options": [
                    "60°",
                    "75°",
                    "90°",
                    "120°"
                ],
                "ans": 2,
                "feedback": "Total parts $= 1 + 2 + 3 = 6$. $180^\\circ / 6 = 30^\\circ$. The largest angle is $3 \\times 30^\\circ = \\mathbf{90^\\circ}$ (a right triangle!)."
            },
            {
                "q": "Can an extended ratio $a : b : c$ be written as a single fraction like $a/b/c$?",
                "options": [
                    "No, an extended ratio compares 3 terms simultaneously and cannot be written as a single binary fraction",
                    "Yes, it always equals a ÷ b ÷ c",
                    "Yes, it equals (a+b)/c",
                    "It only applies to integers"
                ],
                "ans": 0,
                "feedback": "An extended ratio is not a single quotient; it denotes simultaneous pairwise proportionalities $A/B = a/b$, $B/C = b/c$, and $A/C = a/c$."
            }
        ]
    },
    {
        "id": 6,
        "title": "Compound Ratios & Equivalence Chains",
        "subtitle": "Linking Pairwise Ratios: Combining a:b and b:c into a:b:c",
        "sim_type": "compound_ratio_chain_linker",
        "voice": "If you know the ratio of A to B and the ratio of B to C, how do you find the unified ratio of A to B to C? You equalize the common linking term.",
        "content": "\n<h4>The Linking Bridge Technique</h4>\n<p>Suppose you are given two separate ratios sharing a common variable $B$:</p>\n$$A : B = 2 : 3 \\quad \\text{and} \\quad B : C = 4 : 5$$\n<p>Notice that $B$ is represented by $3$ in the first ratio, but by $4$ in the second ratio!</p>\n<h4>Step-by-Step Unification Method</h4>\n<ol>\n  <li>Find the Least Common Multiple (LCM) of the two values of the common bridge $B$:\n  $$\\text{LCM}(3, 4) = 12$$</li>\n  <li>Scale the first ratio so that $B$ becomes $12$:\n  $$A : B = (2 \\times 4) : (3 \\times 4) = 8 : 12$$</li>\n  <li>Scale the second ratio so that $B$ becomes $12$:\n  $$B : C = (4 \\times 3) : (5 \\times 3) = 12 : 15$$</li>\n  <li>Combine directly into one continuous extended chain:</li>\n</ol>\n<div style=\"background:#0f172a; border-left:4px solid #10b981; padding:12px; margin:12px 0; border-radius:6px;\">\n  $$\\mathbf{A : B : C = 8 : 12 : 15}$$\n</div>\n<p>This fundamental technique allows multi-party partnerships, business profits, and chemical solutions to be reconciled seamlessly.</p>\n",
        "checkpoints": [
            {
                "q": "If $A : B = 3 : 4$ and $B : C = 8 : 9$, what is $A : B : C$?",
                "options": [
                    "3 : 8 : 9",
                    "6 : 8 : 9",
                    "12 : 16 : 18",
                    "3 : 4 : 9"
                ],
                "ans": 1,
                "feedback": "Multiply $A : B$ by $2$: $3 \\times 2 : 4 \\times 2 = 6 : 8$. Combine with $B : C = 8 : 9$ to get $\\mathbf{6 : 8 : 9}$."
            },
            {
                "q": "If $X : Y = 1 : 2$ and $Y : Z = 3 : 5$, what is $X : Z$?",
                "options": [
                    "1 : 5",
                    "3 : 10",
                    "2 : 5",
                    "3 : 5"
                ],
                "ans": 1,
                "feedback": "Multiply $X : Y$ by $3$ ($3 : 6$) and $Y : Z$ by $2$ ($6 : 10$). $X : Y : Z = 3 : 6 : 10$, so $X : Z = \\mathbf{3 : 10}$."
            }
        ]
    },
    {
        "id": 7,
        "title": "Dividing a Whole in a Given Ratio",
        "subtitle": "Proportional Partitioning & Asset Allocation",
        "sim_type": "whole_partitioning_ratio_allocator",
        "voice": "To divide a total quantity in a given ratio, we add the ratio parts together to find the unit part, and then multiply each term by this common unit value.",
        "content": "\n<h4>The Master Partitioning Formula</h4>\n<p>Suppose a total quantity $Q$ is to be divided among two or more recipients in the ratio $a : b$:</p>\n<ol>\n  <li><strong>Total Parts:</strong> $T = a + b$</li>\n  <li><strong>Value of One Part:</strong> $\\text{Unit Part} = \\frac{Q}{T} = \\frac{Q}{a + b}$</li>\n  <li><strong>Each Share:</strong>\n  $$\\mathbf{\\text{Share}_A = \\frac{a}{a+b} \\times Q, \\qquad \\text{Share}_B = \\frac{b}{a+b} \\times Q}$$</li>\n</ol>\n<h4>Example: Dividing an Inheritance of ₹1,20,000 in Ratio 3 : 5</h4>\n<ul>\n  <li>Total Parts $= 3 + 5 = 8\\text{ parts}$.</li>\n  <li>Value of $1\\text{ part} = \\frac{120,000}{8} = \\text{₹}15,000$.</li>\n  <li>First Share $= 3 \\times 15,000 = \\mathbf{\\text{₹}45,000}$.</li>\n  <li>Second Share $= 5 \\times 15,000 = \\mathbf{\\text{₹}75,000}$.</li>\n</ul>\n<p>Check: $45,000 + 75,000 = \\text{₹}1,20,000$ (entire whole conserved!).</p>\n",
        "checkpoints": [
            {
                "q": "A sum of ₹750 is shared between Rohit and Priya in the ratio $2 : 3$. How much does Priya receive?",
                "options": [
                    "₹300",
                    "₹375",
                    "₹450",
                    "₹500"
                ],
                "ans": 2,
                "feedback": "Total parts $= 2 + 3 = 5$. One part $= 750 / 5 = ₹150$. Priya receives $3 \\times 150 = \\mathbf{₹450}$."
            },
            {
                "q": "A $72\\text{ cm}$ rope is cut in the ratio $1 : 3 : 4$. What is the length of the shortest piece?",
                "options": [
                    "8 cm",
                    "9 cm",
                    "12 cm",
                    "18 cm"
                ],
                "ans": 1,
                "feedback": "Total parts $= 1 + 3 + 4 = 8$. Shortest piece $= \\frac{1}{8} \\times 72 = \\mathbf{9\\text{ cm}}$."
            }
        ]
    },
    {
        "id": 8,
        "title": "A Slice of the Pie: Circle Graphs",
        "subtitle": "Connecting Ratios, Percentages & Central Angles (360°)",
        "sim_type": "slice_of_pie_circle_graph_lab",
        "voice": "A pie chart represents parts of a whole through circular sectors. Because the entire circle encompasses 360 degrees, every sector angle is directly proportional to its fractional share.",
        "content": "\n<h4>The Geometry of Pie Charts</h2>\n<p>A circle graph (or <strong>pie chart</strong>) visualizes proportions as wedge-shaped slices (sectors) of a complete $360^\\circ$ circle.</p>\n<h4>The Master Sector Angle Formula</h4>\n<p>If a component has a frequency or value $v$ out of a total sum $V$:</p>\n<div style=\"background:#0f172a; border-left:4px solid #f59e0b; padding:12px; margin:12px 0; border-radius:6px;\">\n  $$\\mathbf{\\text{Central Angle } \\theta = \\frac{v}{V} \\times 360^\\circ}$$\n</div>\n<p>Equivalently, if expressed as a percentage $P\\%$:</p>\n$$\\mathbf{\\theta = \\frac{P}{100} \\times 360^\\circ = 3.6 \\times P^\\circ}$$\n<h4>Common Benchmark Angles</h4>\n<ul>\n  <li>$\\frac{1}{2}$ of total ($50\\%$) $\\implies \\frac{1}{2} \\times 360^\\circ = \\mathbf{180^\\circ}$ (Straight Semicircle).</li>\n  <li>$\\frac{1}{4}$ of total ($25\\%$) $\\implies \\frac{1}{4} \\times 360^\\circ = \\mathbf{90^\\circ}$ (Right-Angle Sector).</li>\n  <li>$\\frac{1}{3}$ of total ($33.3\\%$) $\\implies \\frac{1}{3} \\times 360^\\circ = \\mathbf{120^\\circ}$.</li>\n  <li>$\\frac{1}{10}$ of total ($10\\%$) $\\implies 36^\\circ$.</li>\n</ul>\n",
        "checkpoints": [
            {
                "q": "In a school survey, $40\\%$ of students walk to school. What is the central angle for this category on a pie chart?",
                "options": [
                    "40°",
                    "120°",
                    "144°",
                    "160°"
                ],
                "ans": 2,
                "feedback": "$\\theta = \\frac{40}{100} \\times 360^\\circ = 40 \\times 3.6^\\circ = \\mathbf{144^\\circ}$."
            },
            {
                "q": "If a slice in a pie chart has a central angle of $72^\\circ$, what fraction of the whole does it represent?",
                "options": [
                    "1 / 4",
                    "1 / 5",
                    "1 / 6",
                    "1 / 8"
                ],
                "ans": 1,
                "feedback": "$\\text{Fraction} = \\frac{72^\\circ}{360^\\circ} = \\mathbf{\\frac{1}{5}}$ (or $20\\%$)."
            }
        ]
    },
    {
        "id": 9,
        "title": "Sector Angle Calculations & Budgeting",
        "subtitle": "Interactive Budget Allocation & Sector Construction",
        "sim_type": "pie_chart_sector_angle_calculator",
        "voice": "When drawing a pie chart, calculate the central angle for each item and ensure the sum of all angles equals exactly 360 degrees.",
        "content": "\n<h4>Building a Household Budget Pie Chart</h4>\n<p>Consider a monthly family income of ₹60,000 allocated across four sectors:</p>\n<div style=\"background:#0f172a; border:1px solid #334155; border-radius:10px; padding:12px; margin:12px 0; font-size:13.5px;\">\n  <table style=\"width:100%; border-collapse:collapse; color:#cbd5e1;\">\n    <tr style=\"border-bottom:1px solid #475569; color:#fcd34d;\">\n      <th style=\"padding:6px; text-align:left;\">Category</th>\n      <th style=\"padding:6px; text-align:left;\">Monthly Spend</th>\n      <th style=\"padding:6px; text-align:left;\">Proportion</th>\n      <th style=\"padding:6px; text-align:left;\">Central Angle (θ)</th>\n    </tr>\n    <tr style=\"border-bottom:1px solid #334155;\">\n      <td style=\"padding:6px;\">Food & Groceries</td>\n      <td style=\"padding:6px;\">₹24,000</td>\n      <td style=\"padding:6px;\">24k / 60k = 2/5</td>\n      <td style=\"padding:6px; color:#38bdf8;\">(2/5) × 360° = <strong>144°</strong></td>\n    </tr>\n    <tr style=\"border-bottom:1px solid #334155;\">\n      <td style=\"padding:6px;\">House Rent</td>\n      <td style=\"padding:6px;\">₹15,000</td>\n      <td style=\"padding:6px;\">15k / 60k = 1/4</td>\n      <td style=\"padding:6px; color:#38bdf8;\">(1/4) × 360° = <strong>90°</strong></td>\n    </tr>\n    <tr style=\"border-bottom:1px solid #334155;\">\n      <td style=\"padding:6px;\">Education</td>\n      <td style=\"padding:6px;\">₹12,000</td>\n      <td style=\"padding:6px;\">12k / 60k = 1/5</td>\n      <td style=\"padding:6px; color:#38bdf8;\">(1/5) × 360° = <strong>72°</strong></td>\n    </tr>\n    <tr>\n      <td style=\"padding:6px;\">Savings & Misc</td>\n      <td style=\"padding:6px;\">₹9,000</td>\n      <td style=\"padding:6px;\">9k / 60k = 3/20</td>\n      <td style=\"padding:6px; color:#38bdf8;\">(3/20) × 360° = <strong>54°</strong></td>\n    </tr>\n  </table>\n</div>\n<p><strong>Sanity Check:</strong> $144^\\circ + 90^\\circ + 72^\\circ + 54^\\circ = \\mathbf{360^\\circ}$. The entire disc is completely and accurately accounted for.</p>\n",
        "checkpoints": [
            {
                "q": "If monthly savings is ₹9,000 out of ₹60,000, what is the central angle for savings?",
                "options": [
                    "45°",
                    "54°",
                    "60°",
                    "72°"
                ],
                "ans": 1,
                "feedback": "$\\theta = \\frac{9,000}{60,000} \\times 360^\\circ = \\frac{3}{20} \\times 360^\\circ = \\mathbf{54^\\circ}$."
            },
            {
                "q": "What must the sum of all central angles in any valid pie chart always equal?",
                "options": [
                    "100°",
                    "180°",
                    "360°",
                    "Dependent on the radius"
                ],
                "ans": 2,
                "feedback": "A complete revolution around the center of a circle is always identically $\\mathbf{360^\\circ}$."
            }
        ]
    },
    {
        "id": 10,
        "title": "Inverse Proportions: Constant Product Law",
        "subtitle": "The Fundamental Law: x · y = k (Hyperbolic Decay)",
        "sim_type": "inverse_proportions_hyperbola_engine",
        "voice": "Now we enter the fascinating domain of Inverse Proportions. When one quantity increases, the other decreases in such a way that their product remains strictly constant.",
        "content": "\n<h4>The Definition of Inverse Proportion</h4>\n<p>Two quantities $x$ and $y$ are said to be in <strong>inverse proportion</strong> (or inverse variation, written $y \\propto \\frac{1}{x}$) if an increase in $x$ leads to a proportional decrease in $y$, such that their <strong>product remains constant</strong>:</p>\n<div style=\"background:#0f172a; border-left:4px solid #f43f5e; padding:12px; margin:12px 0; border-radius:6px;\">\n  $$\\mathbf{x \\times y = k \\quad \\text{or} \\quad y = \\frac{k}{x} \\quad (k = \\text{constant})}$$\n</div>\n<h4>Two-Point Product Equivalence Rule</h4>\n<p>If $(x_1, y_1)$ and $(x_2, y_2)$ are corresponding values:</p>\n$$\\mathbf{x_1 \\cdot y_1 = x_2 \\cdot y_2} \\quad \\Longleftrightarrow \\quad \\mathbf{\\frac{x_1}{x_2} = \\frac{y_2}{y_1}}$$\n<p>Notice the inverted order on the right side: $\\frac{x_1}{x_2} = \\frac{y_2}{y_1}$!</p>\n<h4>Contrasting with Direct Proportion</h4>\n<ul>\n  <li><strong>Direct:</strong> Ratio is constant ($\\\\frac{y}{x} = k$). When $x$ doubles, $y$ doubles.</li>\n  <li><strong>Inverse:</strong> Product is constant ($x \\cdot y = k$). When $x$ doubles, $y$ is <strong>halved</strong>!</li>\n</ul>\n",
        "checkpoints": [
            {
                "q": "If $x$ and $y$ are in inverse proportion, and $y = 10$ when $x = 6$, what is $y$ when $x = 15$?",
                "options": [
                    "4",
                    "5",
                    "8",
                    "25"
                ],
                "ans": 0,
                "feedback": "Constant product $k = 6 \\times 10 = 60$. When $x = 15$, $y = \\frac{60}{15} = \\mathbf{4}$."
            },
            {
                "q": "If speed is doubled while traveling a fixed distance, what happens to the travel time?",
                "options": [
                    "Time doubles",
                    "Time is halved",
                    "Time remains unchanged",
                    "Time quadruples"
                ],
                "ans": 1,
                "feedback": "Speed and time are inversely proportional: doubling speed cuts travel time in half."
            }
        ]
    },
    {
        "id": 11,
        "title": "Speed, Distance & Time: Reciprocal Laws",
        "subtitle": "Fixed Journey Distance: Speed × Time = Constant",
        "sim_type": "speed_time_distance_gearbox",
        "voice": "For any fixed journey distance, speed and travel time are inversely proportional. Drive twice as fast, and you arrive in half the time.",
        "content": "\n<h4>The Speed-Time Inverse Relationship</h4>\n<p>From physics, the distance $D$ traveled at uniform speed $S$ over time $T$ is given by:</p>\n$$D = S \\times T$$\n<p>If the journey distance $D$ is <strong>fixed</strong> (e.g. from Delhi to Jaipur, $300\\text{ km}$):</p>\n<div style=\"background:#0f172a; border-left:4px solid #06b6d4; padding:12px; margin:12px 0; border-radius:6px;\">\n  $$\\mathbf{S \\times T = 300\\text{ km (constant)} \\implies T = \\frac{300}{S}}$$\n</div>\n<h4>Comparative Journey Table</h4>\n<ul>\n  <li>At $30\\text{ km/h}$: Time $= 300 / 30 = \\mathbf{10\\text{ hours}}$</li>\n  <li>At $60\\text{ km/h}$ (speed doubled): Time $= 300 / 60 = \\mathbf{5\\text{ hours}}$ (time halved!)</li>\n  <li>At $100\\text{ km/h}$: Time $= 300 / 100 = \\mathbf{3\\text{ hours}}$</li>\n</ul>\n<p>Notice that in every case, $\\text{Speed} \\times \\text{Time} = 300$. When plotted on a coordinate grid, the graph is a smooth curve known as a <strong>rectangular hyperbola</strong>.</p>\n",
        "checkpoints": [
            {
                "q": "A car traveling at $60\\text{ km/h}$ completes a journey in $4\\text{ hours}$. How fast must it travel to complete the same journey in $3\\text{ hours}$?",
                "options": [
                    "70 km/h",
                    "75 km/h",
                    "80 km/h",
                    "90 km/h"
                ],
                "ans": 2,
                "feedback": "Distance $= 60 \\times 4 = 240\\text{ km}$. Required speed $= \\frac{240}{3} = \\mathbf{80\\text{ km/h}}$."
            },
            {
                "q": "If a train reduces its speed to $3/4$ of its normal speed, how does its travel time change?",
                "options": [
                    "Time becomes 3/4 of normal",
                    "Time becomes 4/3 of normal (increases by 33.3%)",
                    "Time remains equal",
                    "Time doubles"
                ],
                "ans": 1,
                "feedback": "Because speed and time are reciprocal, scaling speed by $\\frac{3}{4}$ scales time by its inverse: $\\mathbf{\\frac{4}{3}}$."
            }
        ]
    },
    {
        "id": 12,
        "title": "Work, Workers & Days: The Invariant Workload",
        "subtitle": "The Total Worker-Day Invariant: W₁ · D₁ = W₂ · D₂",
        "sim_type": "workers_time_workload_balance",
        "voice": "More workers mean fewer days required to complete a project. The total volume of work, measured in worker-days, remains completely unchanged.",
        "content": "\n<h4>The Worker-Day Constant</h4>\n<p>In construction, harvesting, and project planning, a specific project requires a fixed total quantity of effort called <strong>worker-days (or man-hours)</strong>:</p>\n<div style=\"background:#0f172a; border-left:4px solid #10b981; padding:12px; margin:12px 0; border-radius:6px;\">\n  $$\\mathbf{\\text{Total Workload} = \\text{Number of Workers } (W) \\times \\text{Number of Days } (D) = \\text{constant}}$$\n</div>\n<h4>The Working Formula</h4>\n$$W_1 \\times D_1 = W_2 \\times D_2$$\n<h4>Example: Building a Boundary Wall</h4>\n<p>If $12$ masons can construct a wall in $10\\text{ days}$:</p>\n$$\\text{Total Work} = 12 \\times 10 = 120\\text{ mason-days}$$\n<p>If $8$ masons are employed instead, how long will it take?</p>\n$$8 \\times D_2 = 120 \\implies D_2 = \\frac{120}{8} = \\mathbf{15\\text{ days}}$$\n<p>Fewer workers naturally require more days to complete the exact same workload.</p>\n",
        "checkpoints": [
            {
                "q": "If 15 workers can build a shed in 48 hours, how many workers are needed to do the same job in 30 hours?",
                "options": [
                    "20",
                    "24",
                    "25",
                    "30"
                ],
                "ans": 1,
                "feedback": "$15 \\times 48 = W_2 \\times 30 \\implies 720 = 30 W_2 \\implies W_2 = \\mathbf{24\\text{ workers}}$."
            },
            {
                "q": "A hostel has food provisions for 200 students for 50 days. If 50 more students join, how long will the provisions last?",
                "options": [
                    "35 days",
                    "40 days",
                    "42 days",
                    "45 days"
                ],
                "ans": 1,
                "feedback": "Total student-days $= 200 \\times 50 = 10,000$. New total students $= 250$. Days $= \\frac{10,000}{250} = \\mathbf{40\\text{ days}}$."
            }
        ]
    },
    {
        "id": 13,
        "title": "Pipes, Cisterns & Flow Rates",
        "subtitle": "Reciprocal Addition: Filling Time vs Combined Inflow",
        "sim_type": "pipes_cisterns_fill_drain_lab",
        "voice": "When multiple pipes fill a tank together, their filling rates add together. The total time taken to fill the tank is the reciprocal of the combined rate.",
        "content": "\n<h4>Pipes and Cisterns: Rate of Work</h4>\n<p>If a water tap can fill a reservoir completely in $T\\text{ hours}$, then in $1\\text{ hour}$, it fills:</p>\n$$\\mathbf{\\text{Hourly Rate} = \\frac{1}{T} \\text{ of the tank}}$$\n<h4>Combining Multiple Taps</h4>\n<p>Suppose Tap A fills a tank in $6\\text{ hours}$ and Tap B fills it in $3\\text{ hours}$:</p>\n<ul>\n  <li>In $1\\text{ hour}$, Tap A fills $\\frac{1}{6}$th of the tank.</li>\n  <li>In $1\\text{ hour}$, Tap B fills $\\frac{1}{3} = \\frac{2}{6}$th of the tank.</li>\n  <li>Combined rate in $1\\text{ hour}$:\n  $$\\frac{1}{6} + \\frac{2}{6} = \\frac{3}{6} = \\frac{1}{2} \\text{ of the tank}$$</li>\n</ul>\n<div style=\"background:#0f172a; border-left:4px solid #38bdf8; padding:12px; margin:12px 0; border-radius:6px;\">\n  $$\\mathbf{\\text{Total Time Taken Together } T = \\frac{1}{1/2} = 2\\text{ hours}}$$\n</div>\n<p>Notice: Combined time ($2\\text{ hrs}$) is less than the fastest individual pipe ($3\\text{ hrs}$)!</p>\n",
        "checkpoints": [
            {
                "q": "Pipe A fills a cistern in 12 hours and Pipe B fills it in 6 hours. Working together, how long will they take to fill the cistern?",
                "options": [
                    "4 hours",
                    "6 hours",
                    "8 hours",
                    "9 hours"
                ],
                "ans": 0,
                "feedback": "Combined rate $= \\frac{1}{12} + \\frac{1}{6} = \\frac{1 + 2}{12} = \\frac{3}{12} = \\frac{1}{4}$. Time $= \\mathbf{4\\text{ hours}}$."
            },
            {
                "q": "If tap A fills at rate 1/T₁ and drain B empties at rate 1/T₂, what is the net filling rate?",
                "options": [
                    "1/T₁ + 1/T₂",
                    "1/T₁ - 1/T₂",
                    "T₁ · T₂",
                    "T₁ - T₂"
                ],
                "ans": 1,
                "feedback": "Drainage removes water, so its rate subtracts from the inflow: $\\mathbf{1/T_1 - 1/T_2}$."
            }
        ]
    },
    {
        "id": 14,
        "title": "Direct vs. Inverse Proportions: Dual Classifier",
        "subtitle": "How to Determine the Relationship Instantly",
        "sim_type": "direct_vs_inverse_dual_comparator",
        "voice": "The most common blunder is treating an inverse proportion as direct, or vice versa. Always ask: when one increases, does the other grow or shrink?",
        "content": "\n<h4>The Golden Decision Tree</h4>\n<p>Whenever you encounter a word problem involving changing quantities, ask yourself the fundamental question:</p>\n<blockquote style=\"font-style:italic; color:#fcd34d; border-left:3px solid #f59e0b; padding-left:10px; margin:10px 0;\">\n  \"If I double the first quantity, does the second quantity double, or does it get cut in half?\"\n</blockquote>\n<div style=\"display:grid; grid-template-columns:1fr 1fr; gap:12px; margin:14px 0;\">\n  <div style=\"background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:8px; padding:12px;\">\n    <h5 style=\"color:#34d399; margin-bottom:6px;\">DIRECT PROPORTION</h5>\n    <ul style=\"font-size:12.5px; margin-left:16px;\">\n      <li>More $x$ means <strong>MORE</strong> $y$</li>\n      <li>Constant: $\\mathbf{y / x = k}$ (Ratio)</li>\n      <li>Formula: $\\frac{x_1}{y_1} = \\frac{x_2}{y_2}$</li>\n      <li>Graph: Straight line through (0,0)</li>\n    </ul>\n  </div>\n  <div style=\"background:rgba(244,63,94,0.15); border:1px solid #f43f5e; border-radius:8px; padding:12px;\">\n    <h5 style=\"color:#fda4af; margin-bottom:6px;\">INVERSE PROPORTION</h5>\n    <ul style=\"font-size:12.5px; margin-left:16px;\">\n      <li>More $x$ means <strong>LESS</strong> $y$</li>\n      <li>Constant: $\\mathbf{x \\cdot y = k}$ (Product)</li>\n      <li>Formula: $x_1 y_1 = x_2 y_2$</li>\n      <li>Graph: Curved hyperbola</li>\n    </ul>\n  </div>\n</div>\n",
        "checkpoints": [
            {
                "q": "Which of the following pairs represents an INVERSE proportion?",
                "options": [
                    "Number of notebooks purchased and total cost",
                    "Speed of a train and time taken for a fixed distance",
                    "Distance traveled and petrol consumed",
                    "Hours worked and wage earned at fixed hourly pay"
                ],
                "ans": 1,
                "feedback": "For a fixed journey distance, higher speed results in less time ($S \\cdot T = D$)."
            },
            {
                "q": "Number of workers and time taken to complete a job is:",
                "options": [
                    "Direct proportion",
                    "Inverse proportion",
                    "Additive relation",
                    "Exponential growth"
                ],
                "ans": 1,
                "feedback": "More workers finish the job in less time: an inverse proportion."
            }
        ]
    },
    {
        "id": 15,
        "title": "Trairāśika in Inverse Variation",
        "subtitle": "Vyastatrairāśika: The Ancient Inverse Rule of Three",
        "sim_type": "trairasika_inverse_rule_of_three",
        "voice": "In Indian mathematical heritage, the Rule of Three was split into Direct Trairāśika and Inverse Trairāśika, called Vyasta-trairāśika. It solved commercial and labor problems with effortless clarity.",
        "content": "\n<h4>Ancient Indian Heritage: Vyastatrairāśika</h4>\n<p>The great mathematician <strong>Āryabhaṭa</strong> (499 CE) and <strong>Bhāskarācārya</strong> (1150 CE in <em>Līlāvatī</em>) formulated the exact rule for inverse proportions, termed <strong>Vyastatrairāśika</strong> (The Inverse Rule of Three):</p>\n<blockquote style=\"font-style:italic; color:#93c5fd; border-left:3px solid #38bdf8; padding-left:10px; margin:10px 0;\">\n  \"vyaste vidhir viparītaḥ syāt...\"<br>\n  — <em>In the inverse case, the operation is inverted: multiply the argument (Pramāṇa) by the fruit (Phala), and divide by the requisition (Icchā).</em>\n</blockquote>\n<h4>The Four Classical Terms</h4>\n<ol>\n  <li><strong>Pramāṇa ($x_1$):</strong> The known argument (e.g. 10 workers).</li>\n  <li><strong>Phala ($y_1$):</strong> The known fruit/result (e.g. 12 days).</li>\n  <li><strong>Icchā ($x_2$):</strong> The desired requisition (e.g. 15 workers).</li>\n  <li><strong>Icchā-phala ($y_2$):</strong> The unknown fruit sought:</li>\n</ol>\n<div style=\"background:#0f172a; border-left:4px solid #fcd34d; padding:12px; margin:12px 0; border-radius:6px;\">\n  $$\\mathbf{\\text{Direct Trairāśika: } y_2 = \\frac{y_1 \\times x_2}{x_1}} \\qquad \\mathbf{\\text{Vyastatrairāśika (Inverse): } y_2 = \\frac{x_1 \\times y_1}{x_2}}$$\n</div>\n<p>Notice how modern algebra $x_1 y_1 = x_2 y_2 \\implies y_2 = \\frac{x_1 y_1}{x_2}$ is identical to Bhāskarācārya's verse!</p>\n",
        "checkpoints": [
            {
                "q": "What is the formula for Icchā-phala (y₂) in Vyastatrairāśika (Inverse Rule of Three)?",
                "options": [
                    "y₂ = (x₁ · y₁) / x₂",
                    "y₂ = (y₁ · x₂) / x₁",
                    "y₂ = x₁ + y₁ - x₂",
                    "y₂ = (x₁ + x₂) / y₁"
                ],
                "ans": 0,
                "feedback": "In inverse variation, the product of Pramāṇa and Phala is divided by Icchā: $\\mathbf{y_2 = \\frac{x_1 y_1}{x_2}}$."
            },
            {
                "q": "If 12 cows graze a pasture in 14 days, how many days will 21 cows take using Vyastatrairāśika?",
                "options": [
                    "6 days",
                    "8 days",
                    "10 days",
                    "12 days"
                ],
                "ans": 1,
                "feedback": "$y_2 = \\frac{12 \\times 14}{21} = \\frac{168}{21} = \\mathbf{8\\text{ days}}$."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter Summary & Master Formulas",
        "subtitle": "The Comprehensive Proportionality Knowledge Base",
        "sim_type": "chapter_summary_master_matrix",
        "voice": "Here is our comprehensive summary of all mathematical models, extended ratios, pie chart formulas, and inverse variation principles from this chapter.",
        "content": "\n<h4>The Unified Knowledge Repository</h4>\n<div style=\"background:#0f172a; border:1px solid #334155; border-radius:10px; padding:14px; font-size:13px;\">\n  <table style=\"width:100%; border-collapse:collapse; color:#cbd5e1;\">\n    <tr style=\"border-bottom:1px solid #475569; color:#fcd34d;\">\n      <th style=\"padding:6px; text-align:left;\">Topic / Model</th>\n      <th style=\"padding:6px; text-align:left;\">Governing Equation</th>\n    </tr>\n    <tr style=\"border-bottom:1px solid #334155;\">\n      <td style=\"padding:6px;\">Direct Proportionality</td>\n      <td style=\"padding:6px; color:#34d399;\">$\\frac{y}{x} = k \\implies \\frac{x_1}{y_1} = \\frac{x_2}{y_2}$</td>\n    </tr>\n    <tr style=\"border-bottom:1px solid #334155;\">\n      <td style=\"padding:6px;\">Inverse Proportionality</td>\n      <td style=\"padding:6px; color:#fda4af;\">$x \\cdot y = k \\implies x_1 y_1 = x_2 y_2$</td>\n    </tr>\n    <tr style=\"border-bottom:1px solid #334155;\">\n      <td style=\"padding:6px;\">Map Representative Fraction (R.F.)</td>\n      <td style=\"padding:6px; color:#38bdf8;\">$\\text{R.F.} = \\frac{\\text{Map Distance (cm)}}{\\text{Ground Distance (cm)}}$</td>\n    </tr>\n    <tr style=\"border-bottom:1px solid #334155;\">\n      <td style=\"padding:6px;\">Multi-Term Ratio Chain</td>\n      <td style=\"padding:6px; color:#a5b4fc;\">$A:B = a:b, B:C = b:c \\implies A:B:C$</td>\n    </tr>\n    <tr style=\"border-bottom:1px solid #334155;\">\n      <td style=\"padding:6px;\">Pie Chart Sector Angle (θ)</td>\n      <td style=\"padding:6px; color:#fcd34d;\">$\\theta = \\frac{v}{V} \\times 360^\\circ = 3.6 \\times P^\\circ$</td>\n    </tr>\n    <tr style=\"border-bottom:1px solid #334155;\">\n      <td style=\"padding:6px;\">Work & Labor Invariant</td>\n      <td style=\"padding:6px; color:#6ee7b7;\">$W_1 \\times D_1 = W_2 \\times D_2$</td>\n    </tr>\n    <tr>\n      <td style=\"padding:6px;\">Vyastatrairāśika (Inverse Rule of 3)</td>\n      <td style=\"padding:6px; color:#f59e0b;\">$y_2 = \\frac{x_1 \\times y_1}{x_2}$</td>\n    </tr>\n  </table>\n</div>\n",
        "checkpoints": [
            {
                "q": "What is the central angle for a category that takes 25% of a pie chart?",
                "options": [
                    "45°",
                    "60°",
                    "90°",
                    "120°"
                ],
                "ans": 2,
                "feedback": "$\\theta = 0.25 \\times 360^\\circ = \\mathbf{90^\\circ}$."
            },
            {
                "q": "If $x$ and $y$ vary inversely, the graph of $y$ versus $x$ is a:",
                "options": [
                    "Straight line through origin",
                    "Circle",
                    "Rectangular hyperbola",
                    "Parabola"
                ],
                "ans": 2,
                "feedback": "$y = k/x$ produces a smooth inverse curve called a $\\mathbf{rectangular\\ hyperbola}$."
            }
        ]
    },
    {
        "id": 17,
        "title": "Mastery Challenge — Part I (Questions 1 to 10)",
        "subtitle": "Direct Variation Recap, Map Scales & Multi-Term Ratios",
        "sim_type": "quiz_slide",
        "voice": "Begin Part One of the Mastery Challenge. Test your skills on direct proportionality, representative fractions in maps, blueprints, and multi-term ratios.",
        "quiz_range": [
            1,
            10
        ]
    },
    {
        "id": 18,
        "title": "Mastery Challenge — Part II (Questions 11 to 20)",
        "subtitle": "Dividing a Whole & A Slice of the Pie (Pie Charts)",
        "sim_type": "quiz_slide",
        "voice": "Welcome to Part Two. Solve problems on partitioning quantities in given ratios and calculating central sector angles in pie charts.",
        "quiz_range": [
            11,
            20
        ]
    },
    {
        "id": 19,
        "title": "Mastery Challenge — Part III (Questions 21 to 30)",
        "subtitle": "Inverse Proportions, Speed-Time & Worker-Days",
        "sim_type": "quiz_slide",
        "voice": "Proceed to Part Three. Master inverse variation equations, speed-time reciprocity, and worker-day workload constants.",
        "quiz_range": [
            21,
            30
        ]
    },
    {
        "id": 20,
        "title": "Mastery Challenge — Part IV (Questions 31 to 40)",
        "subtitle": "Pipes, Vyastatrairāśika & Comprehensive Mastery",
        "sim_type": "quiz_slide",
        "voice": "Final sprint! Complete the challenge with pipe flow rates, ancient Vyastatrairāśika problems, and synthesis questions.",
        "quiz_range": [
            31,
            40
        ]
    }
]

quiz_questions = [
    {
        "num": 1,
        "slide": 17,
        "question": "If $x$ and $y$ are directly proportional, and $y = 45$ when $x = 5$, what is $y$ when $x = 8$?",
        "options": [
            "56",
            "64",
            "72",
            "80"
        ],
        "correct": 2,
        "solution": "In direct proportion, the ratio is constant:\\n$$k = \\frac{y_1}{x_1} = \\frac{45}{5} = 9$$\\nWhen $x = 8$:\\n$$y = k \\times x = 9 \\times 8 = \\mathbf{72}$$\\n\\nAlternatively: $\\frac{5}{45} = \\frac{8}{y} \\implies y = \\frac{45 \\times 8}{5} = 72$."
    },
    {
        "num": 2,
        "slide": 17,
        "question": "On a map, $2.5\\text{ cm}$ represents an actual ground distance of $10\\text{ km}$. What is the Representative Fraction (R.F.) of the map?",
        "options": [
            "1 : 40,000",
            "1 : 100,000",
            "1 : 400,000",
            "1 : 1,000,000"
        ],
        "correct": 2,
        "solution": "Express both quantities in identical units (centimeters):\\n$$10\\text{ km} = 10 \\times 1,000\\text{ m} = 10,000 \\times 100\\text{ cm} = 1,000,000\\text{ cm}$$\\n$$\\text{R.F.} = \\frac{2.5\\text{ cm}}{1,000,000\\text{ cm}} = \\frac{1}{\\frac{1,000,000}{2.5}} = \\mathbf{\\frac{1}{400,000}} \\; (\\text{or } 1 : 400,000)$$."
    },
    {
        "num": 3,
        "slide": 17,
        "question": "If $A : B = 2 : 3$ and $B : C = 6 : 7$, find the combined ratio $A : B : C$.",
        "options": [
            "2 : 6 : 7",
            "4 : 6 : 7",
            "4 : 9 : 7",
            "2 : 3 : 7"
        ],
        "correct": 1,
        "solution": "Equalize the common bridging term $B$:\\n$$A : B = 2 : 3 = (2 \\times 2) : (3 \\times 2) = 4 : 6$$\\n$$B : C = 6 : 7$$\\nSince the term $B$ is now identical ($6$), combine directly:\\n$$\\mathbf{A : B : C = 4 : 6 : 7}$$."
    },
    {
        "num": 4,
        "slide": 17,
        "question": "The dimensions of a rectangular hall on an architect's blueprint with scale $1 : 50$ are $8\\text{ cm} \\times 6\\text{ cm}$. What is the actual floor area of the hall in square meters?",
        "options": [
            "12 m²",
            "24 m²",
            "48 m²",
            "120 m²"
        ],
        "correct": 0,
        "solution": "Actual length $= 8\\text{ cm} \\times 50 = 400\\text{ cm} = 4\\text{ m}$.\\nActual width $= 6\\text{ cm} \\times 50 = 300\\text{ cm} = 3\\text{ m}$.\\n$$\\text{Actual Floor Area} = 4\\text{ m} \\times 3\\text{ m} = \\mathbf{12\\text{ m}^2}$$\\n\\nNotice area scaled by $50^2 = 2500$ ($48\\text{ cm}^2 \\times 2500 = 120,000\\text{ cm}^2 = 12\\text{ m}^2$)."
    },
    {
        "num": 5,
        "slide": 17,
        "question": "The three angles of a triangle are in the ratio $2 : 3 : 5$. What is the measure of the smallest angle?",
        "options": [
            "18°",
            "36°",
            "54°",
            "90°"
        ],
        "correct": 1,
        "solution": "Sum of angles in any triangle $= 180^\\circ$.\\nTotal parts $= 2 + 3 + 5 = 10\\text{ parts}$.\\n$$\\text{Value of 1 part} = \\frac{180^\\circ}{10} = 18^\\circ$$\\n$$\\text{Smallest angle} = 2 \\times 18^\\circ = \\mathbf{36^\\circ}$$."
    },
    {
        "num": 6,
        "slide": 17,
        "question": "If $X : Y = 3 : 5$ and $Y : Z = 2 : 3$, what is the ratio $X : Z$?",
        "options": [
            "1 : 2",
            "2 : 5",
            "3 : 5",
            "6 : 15"
        ],
        "correct": 1,
        "solution": "$$\\frac{X}{Z} = \\frac{X}{Y} \\times \\frac{Y}{Z} = \\frac{3}{5} \\times \\frac{2}{3} = \\frac{2}{5}$$\\n\\nThus, $X : Z = \\mathbf{2 : 5}$."
    },
    {
        "num": 7,
        "slide": 17,
        "question": "On a world map with scale $1 : 25,000,000$, the distance between two capital cities is $8\\text{ cm}$. What is the real-world flight distance in kilometers?",
        "options": [
            "1000 km",
            "1600 km",
            "2000 km",
            "2500 km"
        ],
        "correct": 2,
        "solution": "$$\\text{Ground distance} = 8\\text{ cm} \\times 25,000,000 = 200,000,000\\text{ cm}$$\\nConvert to kilometers:\\n$$200,000,000\\text{ cm} = 2,000,000\\text{ m} = \\mathbf{2000\\text{ km}}$$"
    },
    {
        "num": 8,
        "slide": 17,
        "question": "A photograph of a bacteria enlarged 50,000 times attains a length of $5\\text{ cm}$. What is the actual length of the bacteria in centimeters?",
        "options": [
            "10⁻⁴ cm",
            "10⁻⁵ cm",
            "10⁻⁶ cm",
            "10⁻³ cm"
        ],
        "correct": 0,
        "solution": "$$\\text{Scale} = \\frac{\\text{Image Length}}{\\text{Actual Length}} = 50,000$$\\n$$\\text{Actual Length} = \\frac{5\\text{ cm}}{50,000} = \\frac{1}{10,000}\\text{ cm} = \\mathbf{10^{-4}\\text{ cm}}$$ (or $10^{-6}\\text{ m} = 1\\;\\mu\\text{m}$)."
    },
    {
        "num": 9,
        "slide": 17,
        "question": "If $A : B = 1 : 2$, $B : C = 3 : 4$, and $C : D = 5 : 6$, find $A : D$.",
        "options": [
            "5 : 16",
            "5 : 12",
            "1 : 4",
            "5 : 8"
        ],
        "correct": 0,
        "solution": "Multiply the consecutive ratios:\\n$$\\frac{A}{D} = \\frac{A}{B} \\times \\frac{B}{C} \\times \\frac{C}{D} = \\frac{1}{2} \\times \\frac{3}{4} \\times \\frac{5}{6} = \\frac{15}{48} = \\mathbf{\\frac{5}{16}}$$\\n\\nSo $A : D = \\mathbf{5 : 16}$."
    },
    {
        "num": 10,
        "slide": 17,
        "question": "In a mixture of $60\\text{ kg}$, cement, sand, and gravel are mixed in the ratio $1 : 2 : 3$. How many kilograms of sand are in the mixture?",
        "options": [
            "10 kg",
            "20 kg",
            "30 kg",
            "40 kg"
        ],
        "correct": 1,
        "solution": "Total parts $= 1 + 2 + 3 = 6\\text{ parts}$.\\n$$\\text{Sand fraction} = \\frac{2}{6} = \\frac{1}{3}$$\\n$$\\text{Weight of sand} = \\frac{1}{3} \\times 60\\text{ kg} = \\mathbf{20\\text{ kg}}$$."
    },
    {
        "num": 11,
        "slide": 18,
        "question": "Divide ₹1800 among Amit, Bina, and Charu in the ratio $2 : 3 : 4$. How much does Bina get?",
        "options": [
            "₹400",
            "₹600",
            "₹800",
            "₹900"
        ],
        "correct": 1,
        "solution": "Total parts $= 2 + 3 + 4 = 9\\text{ parts}$.\\n$$\\text{Value of 1 part} = \\frac{1800}{9} = \\text{₹}200$$\\n$$\\text{Bina's share} = 3 \\times 200 = \\mathbf{\\text{₹}600}$$."
    },
    {
        "num": 12,
        "slide": 18,
        "question": "A line segment of length $84\\text{ cm}$ is divided into three parts in the ratio $3 : 4 : 5$. What is the length of the longest part?",
        "options": [
            "21 cm",
            "28 cm",
            "35 cm",
            "40 cm"
        ],
        "correct": 2,
        "solution": "Total parts $= 3 + 4 + 5 = 12\\text{ parts}$.\\n$$\\text{Unit length} = \\frac{84}{12} = 7\\text{ cm}$$\\n$$\\text{Longest part} = 5 \\times 7 = \\mathbf{35\\text{ cm}}$$."
    },
    {
        "num": 13,
        "slide": 18,
        "question": "In a pie chart representing student grades, $15\\%$ of students scored an A. What is the central angle for the grade A sector?",
        "options": [
            "36°",
            "54°",
            "60°",
            "72°"
        ],
        "correct": 1,
        "solution": "$$\\text{Central angle } \\theta = \\frac{15}{100} \\times 360^\\circ = 15 \\times 3.6^\\circ = \\mathbf{54^\\circ}$$."
    },
    {
        "num": 14,
        "slide": 18,
        "question": "In a pie chart, the sector angle for 'Transport Expenses' is $108^\\circ$. What percentage of the total budget does transport represent?",
        "options": [
            "25%",
            "30%",
            "33.3%",
            "36%"
        ],
        "correct": 1,
        "solution": "$$\\text{Percentage} = \\frac{\\text{Sector Angle}}{360^\\circ} \\times 100\\% = \\frac{108^\\circ}{360^\\circ} \\times 100\\% = \\frac{3}{10} \\times 100\\% = \\mathbf{30\\%}$$."
    },
    {
        "num": 15,
        "slide": 18,
        "question": "A monthly family budget allocates ₹18,000 out of a total income of ₹72,000 for rent. What angle should represent rent on a pie chart?",
        "options": [
            "60°",
            "75°",
            "90°",
            "120°"
        ],
        "correct": 2,
        "solution": "$$\\text{Fraction} = \\frac{18,000}{72,000} = \\frac{1}{4}$$\\n$$\\theta = \\frac{1}{4} \\times 360^\\circ = \\mathbf{90^\\circ}$$."
    },
    {
        "num": 16,
        "slide": 18,
        "question": "Two numbers are in the ratio $5 : 7$. If their sum is $144$, what is the difference between the two numbers?",
        "options": [
            "12",
            "24",
            "36",
            "48"
        ],
        "correct": 1,
        "solution": "Total parts $= 5 + 7 = 12$.\\n$$\\text{1 part} = \\frac{144}{12} = 12$$\\nNumbers are $5 \\times 12 = 60$ and $7 \\times 12 = 84$.\\n$$\\text{Difference} = 84 - 60 = 24$$ (or $(7 - 5) \\times 12 = \\mathbf{24}$)."
    },
    {
        "num": 17,
        "slide": 18,
        "question": "A school library has books in English, Hindi, and Science in the ratio $4 : 5 : 6$. If there are $400$ English books, how many Science books are there?",
        "options": [
            "500",
            "600",
            "700",
            "800"
        ],
        "correct": 1,
        "solution": "$$\\text{English parts} = 4 \\implies 1\\text{ part} = \\frac{400}{4} = 100$$\\n$$\\text{Science parts} = 6 \\implies \\text{Science books} = 6 \\times 100 = \\mathbf{600}$$."
    },
    {
        "num": 18,
        "slide": 18,
        "question": "In a pie chart, three sectors have angles $120^\\circ, 80^\\circ,$ and $60^\\circ$. What is the angle of the fourth sector?",
        "options": [
            "80°",
            "90°",
            "100°",
            "110°"
        ],
        "correct": 2,
        "solution": "The sum of all central angles in a circle is $360^\\circ$:\\n$$\\theta_4 = 360^\\circ - (120^\\circ + 80^\\circ + 60^\\circ) = 360^\\circ - 260^\\circ = \\mathbf{100^\\circ}$$."
    },
    {
        "num": 19,
        "slide": 18,
        "question": "An estate of ₹5,60,000 is distributed among a widow and two sons in the ratio $2 : 1 : 1$. What is the share of the widow?",
        "options": [
            "₹1,40,000",
            "₹2,40,000",
            "₹2,80,000",
            "₹3,20,000"
        ],
        "correct": 2,
        "solution": "Total parts $= 2 + 1 + 1 = 4\\text{ parts}$.\\n$$\\text{Widow's share} = \\frac{2}{4} \\times 560,000 = \\frac{1}{2} \\times 560,000 = \\mathbf{\\text{₹}2,80,000}$$."
    },
    {
        "num": 20,
        "slide": 18,
        "question": "A metal alloy weighing $250\\text{ g}$ contains copper, zinc, and nickel in the ratio $5 : 3 : 2$. What is the mass of zinc in the alloy?",
        "options": [
            "50 g",
            "75 g",
            "100 g",
            "125 g"
        ],
        "correct": 1,
        "solution": "Total parts $= 5 + 3 + 2 = 10\\text{ parts}$.\\n$$\\text{1 part} = \\frac{250}{10} = 25\\text{ g}$$\\n$$\\text{Zinc mass} = 3 \\times 25\\text{ g} = \\mathbf{75\\text{ g}}$$."
    },
    {
        "num": 21,
        "slide": 19,
        "question": "If $x$ and $y$ vary inversely, and $x = 12$ when $y = 8$, find the value of $x$ when $y = 16$.",
        "options": [
            "4",
            "6",
            "8",
            "9"
        ],
        "correct": 1,
        "solution": "For inverse proportion, the product is constant:\\n$$x_1 y_1 = x_2 y_2$$\\n$$12 \\times 8 = x_2 \\times 16$$\\n$$96 = 16 x_2 \\implies x_2 = \\frac{96}{16} = \\mathbf{6}$$."
    },
    {
        "num": 22,
        "slide": 19,
        "question": "A car travels at $45\\text{ km/h}$ and takes $4\\text{ hours}$ to complete a trip. How long will the trip take if the speed is increased to $60\\text{ km/h}$?",
        "options": [
            "2.5 hours",
            "3 hours",
            "3.2 hours",
            "3.5 hours"
        ],
        "correct": 1,
        "solution": "$$\\text{Distance} = 45 \\times 4 = 180\\text{ km}$$\\n$$\\text{New time} = \\frac{180}{60} = \\mathbf{3\\text{ hours}}$$."
    },
    {
        "num": 23,
        "slide": 19,
        "question": "If 24 workers can complete a road repair in 15 days, how many workers would be needed to complete the same work in 10 days?",
        "options": [
            "30",
            "32",
            "36",
            "40"
        ],
        "correct": 2,
        "solution": "Using $W_1 D_1 = W_2 D_2$:\\n$$24 \\times 15 = W_2 \\times 10$$\\n$$360 = 10 W_2 \\implies W_2 = \\mathbf{36\\text{ workers}}$$."
    },
    {
        "num": 24,
        "slide": 19,
        "question": "A garrison of 120 soldiers has food provisions for 30 days. If 30 more soldiers arrive, for how many days will the provisions last?",
        "options": [
            "20 days",
            "24 days",
            "25 days",
            "27 days"
        ],
        "correct": 1,
        "solution": "Total soldier-days $= 120 \\times 30 = 3600$.\\nNew soldier count $= 120 + 30 = 150$.\\n$$\\text{Days} = \\frac{3600}{150} = \\mathbf{24\\text{ days}}$$."
    },
    {
        "num": 25,
        "slide": 19,
        "question": "A water tank is filled by 6 identical pumps in 1 hour 20 minutes (80 minutes). How long will it take to fill if only 4 pumps are working?",
        "options": [
            "100 minutes",
            "120 minutes",
            "140 minutes",
            "160 minutes"
        ],
        "correct": 1,
        "solution": "$$\\text{Total pump-minutes} = 6 \\times 80 = 480$$\\n$$\\text{Time for 4 pumps} = \\frac{480}{4} = \\mathbf{120\\text{ minutes}} \\; (\\text{or } 2\\text{ hours})$$."
    },
    {
        "num": 26,
        "slide": 19,
        "question": "If 8 taps can fill a pool in 27 hours, how many taps of the same capacity are needed to fill it in 18 hours?",
        "options": [
            "10",
            "11",
            "12",
            "14"
        ],
        "correct": 2,
        "solution": "$$8 \\times 27 = N \\times 18$$\\n$$216 = 18N \\implies N = \\frac{216}{18} = \\mathbf{12\\text{ taps}}$$."
    },
    {
        "num": 27,
        "slide": 19,
        "question": "Which of the following variables are in DIRECT proportion?",
        "options": [
            "Speed and travel time for a fixed distance",
            "Number of workers and time taken to complete a fixed task",
            "Total distance covered and time taken at constant speed",
            "Length of a book's pages and number of pages for fixed thickness"
        ],
        "correct": 2,
        "solution": "At constant speed, distance and time vary directly: $d = v \\cdot t \\implies \\frac{d}{t} = v$ (constant)."
    },
    {
        "num": 28,
        "slide": 19,
        "question": "A farmer has enough grain to feed 28 animals for 9 days. If he buys 8 more animals, how long will the food last?",
        "options": [
            "6 days",
            "7 days",
            "8 days",
            "8.5 days"
        ],
        "correct": 1,
        "solution": "Total animal-days $= 28 \\times 9 = 252$.\\nNew number of animals $= 28 + 8 = 36$.\\n$$\\text{Days} = \\frac{252}{36} = \\mathbf{7\\text{ days}}$$."
    },
    {
        "num": 29,
        "slide": 19,
        "question": "If 18 men can reap a field in 35 days, how many men are needed to reap it in 15 days?",
        "options": [
            "36",
            "40",
            "42",
            "45"
        ],
        "correct": 2,
        "solution": "$$18 \\times 35 = M \\times 15$$\\n$$630 = 15 M \\implies M = \\frac{630}{15} = \\mathbf{42\\text{ men}}$$."
    },
    {
        "num": 30,
        "slide": 19,
        "question": "In an inverse proportion $x \\cdot y = 144$, what is $y$ when $x = 18$?",
        "options": [
            "6",
            "8",
            "9",
            "12"
        ],
        "correct": 1,
        "solution": "$$y = \\frac{144}{18} = \\mathbf{8}$$."
    },
    {
        "num": 31,
        "slide": 20,
        "question": "Tap A fills a tank in 10 hours and Tap B fills it in 15 hours. How long will both taps take working together?",
        "options": [
            "5 hours",
            "6 hours",
            "7.5 hours",
            "8 hours"
        ],
        "correct": 1,
        "solution": "Combined rate in 1 hour:\\n$$\\text{Rate} = \\frac{1}{10} + \\frac{1}{15} = \\frac{3 + 2}{30} = \\frac{5}{30} = \\frac{1}{6}$$\\n$$\\text{Total time} = \\mathbf{6\\text{ hours}}$$."
    },
    {
        "num": 32,
        "slide": 20,
        "question": "In ancient Indian mathematics, what is the inverse rule of three called?",
        "options": [
            "Trairāśika",
            "Vyastatrairāśika",
            "Pañcarāśika",
            "Saptarāśika"
        ],
        "correct": 1,
        "solution": "Inverse rule of three is specifically termed **Vyastatrairāśika** ('vyasta' meaning inverted or reverse)."
    },
    {
        "num": 33,
        "slide": 20,
        "question": "Using Vyastatrairāśika: 16 weavers take 21 days to weave an order. How many days will 24 weavers take?",
        "options": [
            "12 days",
            "14 days",
            "15 days",
            "18 days"
        ],
        "correct": 1,
        "solution": "$$y_2 = \\frac{x_1 \\times y_1}{x_2} = \\frac{16 \\times 21}{24} = \\frac{336}{24} = \\mathbf{14\\text{ days}}$$."
    },
    {
        "num": 34,
        "slide": 20,
        "question": "Pipe A fills a tank in 8 hours, while drain pipe B empties it in 12 hours. If both are opened together, how long does it take to fill the empty tank?",
        "options": [
            "16 hours",
            "20 hours",
            "24 hours",
            "28 hours"
        ],
        "correct": 2,
        "solution": "Net filling rate in 1 hour:\\n$$\\frac{1}{8} - \\frac{1}{12} = \\frac{3 - 2}{24} = \\frac{1}{24}$$\\n$$\\text{Time to fill} = \\mathbf{24\\text{ hours}}$$."
    },
    {
        "num": 35,
        "slide": 20,
        "question": "A car covers a distance in 5 hours at a speed of $60\\text{ km/h}$. By how much must its speed be increased to cover the same distance in 4 hours?",
        "options": [
            "12 km/h",
            "15 km/h",
            "20 km/h",
            "25 km/h"
        ],
        "correct": 1,
        "solution": "$$\\text{Distance} = 60 \\times 5 = 300\\text{ km}$$\\n$$\\text{Required speed} = \\frac{300}{4} = 75\\text{ km/h}$$\\n$$\\text{Speed increase} = 75 - 60 = \\mathbf{15\\text{ km/h}}$$."
    },
    {
        "num": 36,
        "slide": 20,
        "question": "If 45 men can complete a project in 16 days, how many MORE men must be hired to finish it in 12 days?",
        "options": [
            "10",
            "15",
            "20",
            "25"
        ],
        "correct": 1,
        "solution": "$$45 \\times 16 = M_2 \\times 12 \\implies 720 = 12 M_2 \\implies M_2 = 60\\text{ men}$$\\n$$\\text{Additional men needed} = 60 - 45 = \\mathbf{15\\text{ men}}$$."
    },
    {
        "num": 37,
        "slide": 20,
        "question": "A gear with 30 teeth drives a smaller gear with 12 teeth. If the large gear rotates at 40 RPM, what is the speed of the small gear?",
        "options": [
            "80 RPM",
            "100 RPM",
            "120 RPM",
            "150 RPM"
        ],
        "correct": 1,
        "solution": "Gear teeth and rotation speed are inversely proportional:\\n$$T_1 \\times S_1 = T_2 \\times S_2$$\\n$$30 \\times 40 = 12 \\times S_2 \\implies 1200 = 12 S_2 \\implies S_2 = \\mathbf{100\\text{ RPM}}$$."
    },
    {
        "num": 38,
        "slide": 20,
        "question": "If $a$ and $b$ vary inversely, and $a$ increases by $25\\%$, by what percentage does $b$ decrease?",
        "options": [
            "20%",
            "25%",
            "33.3%",
            "50%"
        ],
        "correct": 0,
        "solution": "$$a_{\\text{new}} = 1.25 a = \\frac{5}{4}a$$\\nSince $a \\cdot b = \\text{constant}$, $b_{\\text{new}} = \\frac{4}{5} b = 0.80 b$.\\n$$\\text{Decrease} = (1 - 0.80) \\times 100\\% = \\mathbf{20\\%}$$."
    },
    {
        "num": 39,
        "slide": 20,
        "question": "Three pipes of diameters $1\\text{ cm}, 2\\text{ cm},$ and $3\\text{ cm}$ discharge water. Since discharge is proportional to the square of diameter, what is the ratio of their flow rates?",
        "options": [
            "1 : 2 : 3",
            "1 : 4 : 9",
            "1 : 8 : 27",
            "2 : 4 : 6"
        ],
        "correct": 1,
        "solution": "Flow rate varies as area of cross-section (diameter squared):\\n$$1^2 : 2^2 : 3^2 = \\mathbf{1 : 4 : 9}$$."
    },
    {
        "num": 40,
        "slide": 20,
        "question": "A garrison had provisions for 1500 men for 45 days. After 15 days, 500 men left the fort. How long will the remaining food last for the remaining men?",
        "options": [
            "40 days",
            "45 days",
            "50 days",
            "60 days"
        ],
        "correct": 1,
        "solution": "After 15 days, remaining food would last $1500$ men for $45 - 15 = 30\\text{ days}$.\\nRemaining men $= 1500 - 500 = 1000\\text{ men}$.\\n$$1500 \\times 30 = 1000 \\times D$$\\n$$45000 = 1000 D \\implies D = \\mathbf{45\\text{ days}}$$."
    }
]
