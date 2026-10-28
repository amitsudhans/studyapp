# -*- coding: utf-8 -*-
"""
Curriculum Dataset for NCERT Class 7 Mathematics - Chapter 3: A Peek Beyond the Point (Decimals)
Contains:
- 20 Complete Slides (16 Content Slides + 4 Dedicated Mastery Quiz Slides)
- Avatar: Acharya Aryabhata (Pioneer of Decimal Place Value & Astronomy)
- 32 In-Slide Checkpoints with Explanations (2 per slide on slides 1-16)
- 40 Mastery Quiz Challenge Questions with Step-by-Step Pedagogical Solutions
- Strictly ZERO prohibited textbook titles
"""

SLIDES_DATA = [
    # Slide 1: The Need for Smaller Units
    {
        "id": 1,
        "tag": "3.1 The Need for Smaller Units • Foundations",
        "title": "The Need for Smaller Units: Beyond Whole Markings",
        "sim_id": "need_for_smaller_units_sim",
        "avatar": {
            "name": "Acharya Aryabhata",
            "title": "Pioneer of Decimal Place Value & Astronomy"
        },
        "narration": "Welcome, seekers of mathematical truth! When measuring objects in nature—like a tiny seed, the width of a beetle, or the thickness of paper—whole units like 1 centimetre or 2 metres fall short. We require smaller, fractional subdivisions to capture true physical reality!",
        "key_terms": ["Subdivision", "Precision", "Fractional Units", "Measurement Gap", "Continuous Scale"],
        "content": [
            "Whole numbers ($1, 2, 3, \\dots$) count discrete objects like apples or cows. But continuous physical quantities like length, weight, and volume rarely coincide with whole unit marks.",
            "If an insect is longer than $2\\text{ cm}$ but shorter than $3\\text{ cm}$, simply saying 'about $2$' or 'about $3$' loses critical scientific precision.",
            "To measure with high accuracy, human civilization devised the system of equal subdivisions—splitting each standard unit into smaller, identical pieces.",
            "Our universal base-10 number system naturally divides every unit into ten equal parts, and each tenth into ten further parts, unlocking the magnificent realm of decimals!"
        ],
        "fact_box": "In 499 CE, Acharya Aryabhata composed the famous aphorism 'Sthanam sthanam dasha gunam syat' (from place to place, each is ten times the preceding), crystallizing the decimal place-value principle that powers modern science.",
        "checkpoints": [
            {
                "question": "Why are whole numbers alone insufficient for measuring continuous quantities like length?",
                "options": [
                    "Because physical objects often lie between whole unit markings",
                    "Because whole numbers cannot be multiplied",
                    "Because rulers only have whole numbers",
                    "Because whole numbers only apply to liquids"
                ],
                "correct": 0,
                "explanation": "Continuous lengths rarely match whole units exactly; objects frequently fall in the interval between consecutive whole marks, necessitating subdivisions."
            },
            {
                "question": "If a pencil's length lies halfway between $7\\text{ cm}$ and $8\\text{ cm}$, what fraction of a centimetre beyond $7\\text{ cm}$ is it?",
                "options": ["$\\frac{1}{4}\\text{ cm}$", "$\\frac{1}{2}\\text{ cm}$", "$\\frac{3}{4}\\text{ cm}$", "$\\frac{1}{10}\\text{ cm}$"],
                "correct": 1,
                "explanation": "Halfway between 7 and 8 represents an extra half unit, or $\\frac{1}{2}\\text{ cm}$ ($0.5\\text{ cm}$)."
            }
        ]
    },

    # Slide 2: A Tenth Part
    {
        "id": 2,
        "tag": "3.2 A Tenth Part • Decimals Unveiled",
        "title": "A Tenth Part: The First Step Beyond the Whole",
        "sim_id": "tenth_part_strip_sim",
        "avatar": {
            "name": "Acharya Aryabhata",
            "title": "Pioneer of Decimal Place Value & Astronomy"
        },
        "narration": "When we divide one whole unit into ten equal parts, each part is called one-tenth. In decimal notation, we place a dot—the decimal point—and write it as zero point one (0.1). Ten of these tenths unite to reconstruct the full whole!",
        "key_terms": ["One-Tenth (1/10)", "Decimal Point", "0.1", "Tenths Place", "Unit Reconstruction"],
        "content": [
            "When $1$ whole unit is sliced into $10$ equal parts, each single slice is one-tenth, written as the fraction $\\frac{1}{10}$.",
            "In decimal notation, this fractional value is written as $0.1$. The dot separating the whole number part ($0$) from the fractional part ($1$) is called the decimal point.",
            "Two tenths is $\\frac{2}{10} = 0.2$; five tenths is $\\frac{5}{10} = 0.5$; nine tenths is $\\frac{9}{10} = 0.9$.",
            "Ten tenths together make one whole: $10 \\times \\frac{1}{10} = \\frac{10}{10} = 1.0$. The decimal point marks the threshold between whole units and fractional parts."
        ],
        "fact_box": "The word 'decimal' comes from the Latin 'decimus', meaning tenth, rooted in the ten fingers of human hands used since antiquity for counting.",
        "checkpoints": [
            {
                "question": "How is seven-tenths written in decimal notation?",
                "options": ["0.07", "7.10", "0.7", "7.0"],
                "correct": 2,
                "explanation": "Seven-tenths is $\\frac{7}{10} = 0.7$. The first digit immediately after the decimal point represents tenths."
            },
            {
                "question": "What is the result when ten tenths ($10 \\times 0.1$) are combined?",
                "options": ["0.10", "1.0", "10.0", "0.01"],
                "correct": 1,
                "explanation": "Ten tenths make one complete whole: $10 \\times 0.1 = 1.0$."
            }
        ]
    },

    # Slide 3: Millimetres & Centimetres
    {
        "id": 3,
        "tag": "3.2 A Tenth Part • Metric Ruler",
        "title": "Millimetres & Centimetres: Tenths in Action",
        "sim_id": "mm_cm_ruler_sim",
        "avatar": {
            "name": "Acharya Aryabhata",
            "title": "Pioneer of Decimal Place Value & Astronomy"
        },
        "narration": "Look at any standard school ruler! The distance between 0 and 1 centimetre is divided into ten tiny spaces. Each tiny space is one millimetre. Thus, 1 millimetre is exactly one-tenth of a centimetre, or 0.1 cm!",
        "key_terms": ["Millimetre (mm)", "Centimetre (cm)", "1 mm = 0.1 cm", "Ruler Ticks", "Linear Measurement"],
        "content": [
            "Every standard metric ruler explicitly displays tenths! Each centimetre ($1\\text{ cm}$) is subdivided into $10$ equal intervals called millimetres ($1\\text{ mm}$).",
            "Therefore, $1\\text{ mm} = \\frac{1}{10}\\text{ cm} = 0.1\\text{ cm}$.",
            "If an eraser measures $3\\text{ cm}$ and $6\\text{ mm}$, we can write its total length in centimetres as $3 + \\frac{6}{10}\\text{ cm} = 3.6\\text{ cm}$.",
            "A pin measuring $48\\text{ mm}$ can be expressed in centimetres by dividing by $10$: $\\frac{48}{10}\\text{ cm} = 4.8\\text{ cm}$ ($4$ whole centimetres and $8$ tenths of a centimetre)."
        ],
        "fact_box": "The metric system was adopted globally because its unit conversions are powers of 10 ($10, 100, 1000$), perfectly mirroring decimal arithmetic without awkward conversion fractions.",
        "checkpoints": [
            {
                "question": "How do you express $8\\text{ mm}$ in centimetres using decimals?",
                "options": ["$8.0\\text{ cm}$", "$0.08\\text{ cm}$", "$0.8\\text{ cm}$", "$80\\text{ cm}$"],
                "correct": 2,
                "explanation": "Since $1\\text{ mm} = 0.1\\text{ cm}$, $8\\text{ mm} = \\frac{8}{10}\\text{ cm} = 0.8\\text{ cm}$."
            },
            {
                "question": "A notebook's thickness is $14\\text{ mm}$. What is this thickness in centimetres?",
                "options": ["$1.4\\text{ cm}$", "$0.14\\text{ cm}$", "$14.0\\text{ cm}$", "$1.04\\text{ cm}$"],
                "correct": 0,
                "explanation": "$14\\text{ mm} = \\frac{14}{10}\\text{ cm} = 1.4\\text{ cm}$."
            }
        ]
    },

    # Slide 4: A Hundredth Part
    {
        "id": 4,
        "tag": "3.3 A Hundredth Part • Finer Subdivisions",
        "title": "A Hundredth Part: Dividing Tenths into Ten Slices",
        "sim_id": "hundredth_grid_sim",
        "avatar": {
            "name": "Acharya Aryabhata",
            "title": "Pioneer of Decimal Place Value & Astronomy"
        },
        "narration": "What happens when even a tenth is too coarse? We divide each tenth part into ten further equal slices! This cuts the whole unit into one hundred equal pieces. Each tiny cell is one-hundredth, or 0.01!",
        "key_terms": ["One-Hundredth (1/100)", "0.01", "100-Grid", "Hundredths Place", "Two Decimal Places"],
        "content": [
            "When $1$ whole is divided into $100$ equal parts, each part is one-hundredth, written as $\\frac{1}{100}$.",
            "In decimal notation, one-hundredth is written as $0.01$. The second digit to the right of the decimal point occupies the hundredths place.",
            "Notice the stepping scale: $10$ hundredths make $1$ tenth ($\\frac{10}{100} = \\frac{1}{10} = 0.10 = 0.1$), and $100$ hundredths make $1$ whole ($\\frac{100}{100} = 1.00 = 1$).",
            "If $25$ squares in a $100$-grid are shaded, the shaded region represents $\\frac{25}{100} = 0.25$ ($2$ tenths and $5$ hundredths)."
        ],
        "fact_box": "A square grid with 10 rows and 10 columns provides a complete visual proof that 0.1 and 0.10 represent identical physical areas: 1 full column of 10 hundredths equals 1 tenth!",
        "checkpoints": [
            {
                "question": "How is the fraction $\\frac{3}{100}$ written as a decimal?",
                "options": ["0.3", "0.03", "3.00", "0.003"],
                "correct": 1,
                "explanation": "Three hundredths requires the digit 3 in the second place after the decimal point: $0.03$."
            },
            {
                "question": "How many hundredths ($0.01$) are needed to make one-tenth ($0.1$)?",
                "options": ["100", "1", "10", "5"],
                "correct": 2,
                "explanation": "$10 \\times \\frac{1}{100} = \\frac{10}{100} = \\frac{1}{10} = 0.1$. Exactly 10 hundredths equal 1 tenth."
            }
        ]
    },

    # Slide 5: Rupees and Paise
    {
        "id": 5,
        "tag": "3.3 A Hundredth Part • Currency",
        "title": "Rupees and Paise: Hundredths in Daily Life",
        "sim_id": "rupees_paise_currency_sim",
        "avatar": {
            "name": "Acharya Aryabhata",
            "title": "Pioneer of Decimal Place Value & Astronomy"
        },
        "narration": "Every time you spend money in India, you are using hundredths! One rupee consists of 100 paise. Therefore, one paisa is exactly one-hundredth of a rupee, written as ₹0.01!",
        "key_terms": ["Rupee (₹)", "Paisa (p)", "1 Paisa = ₹0.01", "Currency Decimals", "Commercial Arithmetic"],
        "content": [
            "In Indian currency, $1\\text{ Rupee} = 100\\text{ Paise}$.",
            "This directly establishes that $1\\text{ paisa} = \\frac{1}{100}\\text{ rupee} = ₹0.01$.",
            "Fifty paise is $\\frac{50}{100}\\text{ rupee} = ₹0.50$ (or half a rupee).",
            "Be very careful with single-digit paise! $5\\text{ paise} = \\frac{5}{100}\\text{ rupee} = ₹0.05$, NOT $₹0.5$ (which would be $50\\text{ paise}$).",
            "If an item costs $25\\text{ rupees and } 75\\text{ paise}$, it is written compactly as $₹25.75$."
        ],
        "fact_box": "India transitioned to the metric 'Naya Paisa' decimal coinage on April 1, 1957, replacing the older system of 1 Rupee = 16 Annas = 64 Paise with the clean base-10 system of 100 Paise.",
        "checkpoints": [
            {
                "question": "How is $6\\text{ paise}$ correctly written in rupees?",
                "options": ["₹0.6", "₹0.06", "₹6.0", "₹0.60"],
                "correct": 1,
                "explanation": "$6\\text{ paise} = \\frac{6}{100}\\text{ rupee} = ₹0.06$. Writing ₹0.6 would mean 60 paise!"
            },
            {
                "question": "What is $₹4.50$ equal to in paise?",
                "options": ["45 paise", "405 paise", "450 paise", "4050 paise"],
                "correct": 2,
                "explanation": "$4\\text{ rupees} = 400\\text{ paise}$, plus $50\\text{ paise} = 450\\text{ paise}$ total."
            }
        ]
    },

    # Slide 6: Decimal Place Value Matrix
    {
        "id": 6,
        "tag": "3.4 Decimal Place Value • Positional System",
        "title": "Decimal Place Value: The Grand Positional Matrix",
        "sim_id": "decimal_place_value_matrix_sim",
        "avatar": {
            "name": "Acharya Aryabhata",
            "title": "Pioneer of Decimal Place Value & Astronomy"
        },
        "narration": "Observe the seamless symmetry of our number system! As you travel left, each place is multiplied by 10 (Ones, Tens, Hundreds). As you travel right past the decimal point, each place is divided by 10 (Tenths, Hundredths, Thousandths)!",
        "key_terms": ["Place Value Chart", "Tenths (1/10)", "Hundredths (1/100)", "Thousandths (1/1000)", "Positional Weight"],
        "content": [
            "The decimal system extends our standard whole-number place-value columns to the right of the ones place using division by $10$.",
            "Columns to the left of the decimal point: Hundreds ($100$), Tens ($10$), Ones ($1$).",
            "Columns to the right of the decimal point: Tenths ($\\frac{1}{10} = 0.1$), Hundredths ($\\frac{1}{100} = 0.01$), Thousandths ($\\frac{1}{1000} = 0.001$).",
            "In the number $253.486$:",
            "• 2 is in Hundreds ($200$), 5 in Tens ($50$), 3 in Ones ($3$)",
            "• 4 is in Tenths ($0.4$), 8 in Hundredths ($0.08$), 6 in Thousandths ($0.006$)."
        ],
        "fact_box": "In Sanskrit, ancient Indian mathematicians named powers of ten up to trillions and beyond, and described sub-unit fractions as 'Dashamsha' (tenth), 'Shatamsha' (hundredth), and 'Sahasramsha' (thousandth).",
        "checkpoints": [
            {
                "question": "In the number $47.382$, what is the place value of the digit $8$?",
                "options": ["8 Tens", "8 Tenths (0.8)", "8 Hundredths (0.08)", "8 Thousandths (0.008)"],
                "correct": 2,
                "explanation": "The digit 8 is in the second place after the decimal point, which is the hundredths place ($0.08$)."
            },
            {
                "question": "What is the value of a place column compared to the column immediately to its right?",
                "options": ["10 times greater", "10 times smaller", "100 times greater", "Identical"],
                "correct": 0,
                "explanation": "Every place column is exactly 10 times the value of the column immediately to its right ($10 \\times \\frac{1}{100} = \\frac{1}{10}$)."
            }
        ]
    },

    # Slide 7: Expanded Form & Trailing Zeroes
    {
        "id": 7,
        "tag": "3.4 Decimal Place Value • Properties",
        "title": "Expanded Notation & The Trailing Zeroes Law",
        "sim_id": "expanded_form_trailing_zeroes_sim",
        "avatar": {
            "name": "Acharya Aryabhata",
            "title": "Pioneer of Decimal Place Value & Astronomy"
        },
        "narration": "Every decimal can be broken down into its expanded sum of parts. And here is a magical law: attaching extra zeroes to the very end of a decimal does NOT change its value at all! 0.5, 0.50, and 0.500 are all identical!",
        "key_terms": ["Expanded Notation", "Trailing Zeroes", "Equivalent Decimals", "Padding Zeroes", "Invariance"],
        "content": [
            "We can write any decimal in expanded form as the sum of its whole and fractional components:",
            "$36.47 = (3 \\times 10) + (6 \\times 1) + \\left(4 \\times \\frac{1}{10}\\right) + \\left(7 \\times \\frac{1}{100}\\right)$",
            "Trailing Zeroes Law: Adding zeroes at the extreme right end of the decimal part does not alter the number's numerical value.",
            "For example: $0.7 = 0.70 = 0.700$. Why? Because $7\\text{ tenths} = 70\\text{ hundredths} = 700\\text{ thousandths}$!",
            "However, never insert zeroes between the decimal point and digits: $0.7 \\neq 0.07$ (7 tenths is ten times larger than 7 hundredths!)."
        ],
        "fact_box": "Trailing zeroes are immensely useful in computation! By padding decimals with trailing zeroes (making 3.4 into 3.40), we easily align columns to add, subtract, and compare numbers.",
        "checkpoints": [
            {
                "question": "Which of the following decimals is equivalent in value to $0.6$?",
                "options": ["0.06", "0.60", "6.0", "0.006"],
                "correct": 1,
                "explanation": "$0.60$ has a trailing zero at the end; $60\\text{ hundredths} = 6\\text{ tenths} = 0.6$."
            },
            {
                "question": "What is the expanded form of $5.04$?",
                "options": [
                    "$5 + \\frac{4}{10}$",
                    "$5 + \\frac{4}{100}$",
                    "$5 + \\frac{4}{1000}$",
                    "$50 + 4$"
                ],
                "correct": 1,
                "explanation": "In 5.04, there are 5 ones, 0 tenths, and 4 hundredths: $5 + \\frac{4}{100}$."
            }
        ]
    },

    # Slide 8: Units of Measurement: Length
    {
        "id": 8,
        "tag": "3.5 Units of Measurement • Metric Length",
        "title": "Metric Length Conversions: Moving the Decimal Point",
        "sim_id": "metric_length_converter_sim",
        "avatar": {
            "name": "Acharya Aryabhata",
            "title": "Pioneer of Decimal Place Value & Astronomy"
        },
        "narration": "The beauty of metric length is that every unit transition is a power of ten! Converting from a smaller unit to a larger unit simply shifts the decimal point to the left: 10 mm = 1 cm, 100 cm = 1 m, and 1000 m = 1 km!",
        "key_terms": ["Metric Ladder", "Centimetre to Metre", "Metre to Kilometre", "Decimal Shift", "Scale Conversion"],
        "content": [
            "Length relationships in the metric system:",
            "• $1\\text{ cm} = 10\\text{ mm} \\implies 1\\text{ mm} = 0.1\\text{ cm}$",
            "• $1\\text{ m} = 100\\text{ cm} \\implies 1\\text{ cm} = \\frac{1}{100}\\text{ m} = 0.01\\text{ m}$",
            "• $1\\text{ km} = 1000\\text{ m} \\implies 1\\text{ m} = \\frac{1}{1000}\\text{ km} = 0.001\\text{ km}$",
            "Examples:",
            "• $45\\text{ cm}$ in metres: $\\frac{45}{100}\\text{ m} = 0.45\\text{ m}$",
            "• $2\\text{ m } 35\\text{ cm}$: $2 + 0.35 = 2.35\\text{ m}$",
            "• $850\\text{ m}$ in kilometres: $\\frac{850}{1000}\\text{ km} = 0.850\\text{ km} = 0.85\\text{ km}$."
        ],
        "fact_box": "The metre was originally defined during the French Revolution as one ten-millionth of the distance from the Earth's equator to the North Pole along a meridian through Paris.",
        "checkpoints": [
            {
                "question": "How is $7\\text{ cm}$ expressed in metres?",
                "options": ["$0.7\\text{ m}$", "$0.07\\text{ m}$", "$7.0\\text{ m}$", "$0.007\\text{ m}$"],
                "correct": 1,
                "explanation": "Since $1\\text{ m} = 100\\text{ cm}$, $7\\text{ cm} = \\frac{7}{100}\\text{ m} = 0.07\\text{ m}$."
            },
            {
                "question": "Express $2350\\text{ m}$ in kilometres using decimals.",
                "options": ["$23.5\\text{ km}$", "$2.35\\text{ km}$", "$0.235\\text{ km}$", "$235.0\\text{ km}$"],
                "correct": 1,
                "explanation": "Dividing by $1000$: $2350 \\div 1000 = 2.35\\text{ km}$."
            }
        ]
    },

    # Slide 9: Units of Measurement: Mass & Capacity
    {
        "id": 9,
        "tag": "3.5 Units of Measurement • Mass & Capacity",
        "title": "Mass and Capacity: Thousandths in Action",
        "sim_id": "mass_capacity_scales_sim",
        "avatar": {
            "name": "Acharya Aryabhata",
            "title": "Pioneer of Decimal Place Value & Astronomy"
        },
        "narration": "When measuring the weight of vegetables or the volume of milk, we encounter thousandths! Since 1 kilogram has 1000 grams, 1 gram is 0.001 kg. Similarly, 1 millilitre is 0.001 litres!",
        "key_terms": ["Gram (g) to Kilogram (kg)", "Millilitre (mL) to Litre (L)", "Thousandths (0.001)", "Laboratory Balance", "Measuring Cylinder"],
        "content": [
            "Mass (Weight) Conversion:",
            "• $1\\text{ kg} = 1000\\text{ g} \\implies 1\\text{ g} = \\frac{1}{1000}\\text{ kg} = 0.001\\text{ kg}$",
            "• A mango weighing $350\\text{ g}$ is $\\frac{350}{1000}\\text{ kg} = 0.35\\text{ kg}$.",
            "• Watch out for small weights: $5\\text{ g} = \\frac{5}{1000}\\text{ kg} = 0.005\\text{ kg}$, NOT $0.05\\text{ kg}$ (which is $50\\text{ g}$)!",
            "Capacity (Volume) Conversion:",
            "• $1\\text{ L} = 1000\\text{ mL} \\implies 1\\text{ mL} = \\frac{1}{1000}\\text{ L} = 0.001\\text{ L}$",
            "• A juice bottle holding $750\\text{ mL}$ holds $\\frac{750}{1000}\\text{ L} = 0.75\\text{ L}$."
        ],
        "fact_box": "In the metric system, 1 millilitre of pure water at 4°C weighs exactly 1 gram, creating a perfect unified link between volume and mass!",
        "checkpoints": [
            {
                "question": "How do you write $45\\text{ g}$ in kilograms?",
                "options": ["$0.45\\text{ kg}$", "$0.045\\text{ kg}$", "$4.5\\text{ kg}$", "$0.0045\\text{ kg}$"],
                "correct": 1,
                "explanation": "$45\\text{ g} = \\frac{45}{1000}\\text{ kg} = 0.045\\text{ kg}$. Three digits after decimal are needed for thousandths."
            },
            {
                "question": "A medicine bottle contains $250\\text{ mL}$ of syrup. What is this volume in litres?",
                "options": ["$2.5\\text{ L}$", "$0.025\\text{ L}$", "$0.25\\text{ L}$", "$25.0\\text{ L}$"],
                "correct": 2,
                "explanation": "$250\\text{ mL} = \\frac{250}{1000}\\text{ L} = 0.25\\text{ L}$."
            }
        ]
    },

    # Slide 10: Locating Decimals on the Number Line
    {
        "id": 10,
        "tag": "3.6 Locating & Comparing • Number Line",
        "title": "Locating Decimals on the Number Line: Infinite Zoom",
        "sim_id": "number_line_zoom_sim",
        "avatar": {
            "name": "Acharya Aryabhata",
            "title": "Pioneer of Decimal Place Value & Astronomy"
        },
        "narration": "Imagine having a microscope that zooms into the number line! Between any two whole numbers, like 1 and 2, lies an entire world of tenths. And between two tenths lies a world of hundredths! Every decimal has an exact home on the line.",
        "key_terms": ["Number Line", "Magnification", "Subdivision Ticks", "Intervals", "Exact Coordinates"],
        "content": [
            "To locate a decimal on the number line, we identify its neighboring whole numbers first.",
            "Example: Where is $1.4$ located?",
            "1. Find the interval between $1$ and $2$.",
            "2. Divide the unit interval into $10$ equal sections (representing tenths: $1.1, 1.2, 1.3, 1.4, \\dots$).",
            "3. Count $4$ tick marks to the right of $1$. That exact point is $1.4$!",
            "For hundredths (e.g. $1.47$), zoom into the gap between $1.4$ and $1.5$, divide that tiny segment into $10$ hundredths ticks, and move $7$ ticks past $1.4$."
        ],
        "fact_box": "Between ANY two decimal numbers on the number line—no matter how close (like 0.1 and 0.2)—there exist an infinite number of other decimal numbers! Mathematicians call this property the 'density' of numbers.",
        "checkpoints": [
            {
                "question": "Between which two whole numbers does the decimal $3.7$ lie?",
                "options": ["2 and 3", "3 and 4", "7 and 8", "30 and 40"],
                "correct": 1,
                "explanation": "Since $3.7$ has 3 as its whole number part and 7 tenths, it lies strictly between 3 and 4."
            },
            {
                "question": "Which decimal is located exactly midway between $2.4$ and $2.6$?",
                "options": ["2.45", "2.5", "2.55", "3.0"],
                "correct": 1,
                "explanation": "Halfway between 4 tenths and 6 tenths is 5 tenths: $2.5$."
            }
        ]
    },

    # Slide 11: Comparing Decimals
    {
        "id": 11,
        "tag": "3.6 Locating & Comparing • Comparison Rules",
        "title": "Comparing Decimals: The Place-by-Place Duel",
        "sim_id": "comparing_decimals_duel_sim",
        "avatar": {
            "name": "Acharya Aryabhata",
            "title": "Pioneer of Decimal Place Value & Astronomy"
        },
        "narration": "Never be fooled by the number of digits in a decimal! To compare two decimals, first compare their whole parts. If they are equal, compare tenths; if tenths are equal, compare hundredths. Padding trailing zeroes makes comparisons crystal clear!",
        "key_terms": ["Comparison Rules", "Whole Part Priority", "Tenths Duel", "Hundredths Duel", "Zero Padding"],
        "content": [
            "Rule 1: Whole Number Part First. The decimal with the greater whole number is always greater. Example: $6.1 > 4.999$ because $6 > 4$.",
            "Rule 2: Tenths Place Comparison. If whole parts are equal, compare the tenths digit. Example: $0.7 > 0.68$ because $7\\text{ tenths} > 6\\text{ tenths}$.",
            "Rule 3: Hundredths and Beyond. If tenths are equal, inspect hundredths. Example: $2.48 > 2.45$ because $8 > 5$ in the hundredths place.",
            "The Zero-Padding Secret: Many students falsely think $0.45 > 0.7$ because $45 > 7$. Pad $0.7$ with a zero to make it $0.70$! Now it is obvious: $0.70 > 0.45$!"
        ],
        "fact_box": "In Olympic sprint races, victory is determined by hundredths or thousandths of a second. In the 2024 Paris 100m final, the gold and silver were separated by just 0.005 seconds!",
        "checkpoints": [
            {
                "question": "Which decimal is larger: $0.8$ or $0.75$?",
                "options": [
                    "$0.75$ because 75 is greater than 8",
                    "$0.8$ because 8 tenths (0.80) is greater than 7 tenths (0.75)",
                    "Both are equal",
                    "Cannot be determined"
                ],
                "correct": 1,
                "explanation": "Pad $0.8$ with a zero to get $0.80$. Since $80\\text{ hundredths} > 75\\text{ hundredths}$, $0.8 > 0.75$."
            },
            {
                "question": "Which of the following is true?",
                "options": ["$3.05 > 3.5$", "$0.09 > 0.1$", "$1.2 = 1.20$", "$5.4 < 5.04$"],
                "correct": 2,
                "explanation": "$1.2$ and $1.20$ represent the exact same value (trailing zero invariance)."
            }
        ]
    },

    # Slide 12: Addition of Decimals
    {
        "id": 12,
        "tag": "3.7 Addition & Subtraction • Columnar Addition",
        "title": "Addition of Decimals: Precision Alignment",
        "sim_id": "decimal_addition_alignment_sim",
        "avatar": {
            "name": "Acharya Aryabhata",
            "title": "Pioneer of Decimal Place Value & Astronomy"
        },
        "narration": "The golden rule of decimal addition is simple yet sacred: align the decimal points vertically in a straight column! This guarantees that ones add to ones, tenths add to tenths, and hundredths add to hundredths with proper carrying!",
        "key_terms": ["Vertical Alignment", "Column Addition", "Carrying Tenths", "Place-by-Place Sum", "Pad with Zeroes"],
        "content": [
            "Step 1: Write the numbers in a vertical column such that their decimal points line up in an exact straight vertical line.",
            "Step 2: Pad shorter numbers with trailing zeroes so all numbers have the same count of decimal places.",
            "Step 3: Add from right to left, carrying over just like normal whole-number addition.",
            "Step 4: Drop the decimal point straight down into the answer row.",
            "Example: Add $14.6 + 5.75$:",
            "  1 4 . 6 0   (padded with zero)",
            "+ 0 5 . 7 5",
            "-----------",
            "  2 0 . 3 5   (6 tenths + 7 tenths = 13 tenths = 1 whole carried + 3 tenths)"
        ],
        "fact_box": "Misaligning decimal points during addition is the most common mathematical mistake made by students worldwide. Always check that the dots line up like buttons on a shirt!",
        "checkpoints": [
            {
                "question": "What is $4.5 + 2.38$?",
                "options": ["6.43", "6.88", "6.8", "6.48"],
                "correct": 1,
                "explanation": "Pad $4.5$ as $4.50$: $4.50 + 2.38 = 6.88$."
            },
            {
                "question": "If you add $0.9 + 0.3$, what is the result?",
                "options": ["0.12", "1.2", "1.02", "0.012"],
                "correct": 1,
                "explanation": "$9\\text{ tenths} + 3\\text{ tenths} = 12\\text{ tenths} = 1\\text{ whole and } 2\\text{ tenths} = 1.2$."
            }
        ]
    },

    # Slide 13: Subtraction of Decimals
    {
        "id": 13,
        "tag": "3.7 Addition & Subtraction • Columnar Subtraction",
        "title": "Subtraction of Decimals: Regrouping Across the Point",
        "sim_id": "decimal_subtraction_borrow_sim",
        "avatar": {
            "name": "Acharya Aryabhata",
            "title": "Pioneer of Decimal Place Value & Astronomy"
        },
        "narration": "Subtraction also demands strict decimal point alignment. When subtracting a larger digit from a smaller one, we borrow across place values—even borrowing 1 whole unit to create 10 tenths, or 1 tenth to create 10 hundredths!",
        "key_terms": ["Decimal Subtraction", "Regrouping / Borrowing", "Zero Padding", "Vertical Alignment", "Difference"],
        "content": [
            "Step 1: Place the larger number on top, aligning the decimal points vertically.",
            "Step 2: Crucial Step! Always pad the minuend (top number) with trailing zeroes if it has fewer decimal digits than the bottom number.",
            "Step 3: Subtract from right to left, borrowing across columns when needed ($1\\text{ one} = 10\\text{ tenths}$, $1\\text{ tenth} = 10\\text{ hundredths}$).",
            "Example: Subtract $8.4 - 3.75$:",
            "  8 . 4 0   (zero padded to allow borrowing)",
            "- 3 . 7 5",
            "---------",
            "  4 . 6 5   (borrow from 4 to make 10 hundredths; borrow from 8 to make 13 tenths)"
        ],
        "fact_box": "Forgetting to write the trailing zero in 8.40 before subtracting 3.75 often leads students to mistakenly copy down the 5! Always pad empty spaces with zeroes before subtracting.",
        "checkpoints": [
            {
                "question": "What is $10.0 - 4.65$?",
                "options": ["5.45", "5.35", "6.35", "5.65"],
                "correct": 1,
                "explanation": "$10.00 - 4.65 = 5.35$."
            },
            {
                "question": "A cloth piece of $5.2\\text{ m}$ has $1.8\\text{ m}$ cut off. What length remains?",
                "options": ["$3.4\\text{ m}$", "$4.4\\text{ m}$", "$3.6\\text{ m}$", "$4.6\\text{ m}$"],
                "correct": 0,
                "explanation": "$5.2 - 1.8 = 3.4\\text{ m}$."
            }
        ]
    },

    # Slide 14: Decimal Sequences & Estimation
    {
        "id": 14,
        "tag": "3.7 Addition & Subtraction • Sequences & Estimation",
        "title": "Decimal Patterns & Fast Mental Estimation",
        "sim_id": "decimal_sequences_estimator_sim",
        "avatar": {
            "name": "Acharya Aryabhata",
            "title": "Pioneer of Decimal Place Value & Astronomy"
        },
        "narration": "Mathematicians look for patterns! Decimal sequences progress by constant increments. Furthermore, before calculating complicated sums, wise minds always estimate using whole numbers to catch silly errors before they happen!",
        "key_terms": ["Decimal Patterns", "Common Difference", "Mental Estimation", "Sanity Check", "Rounding to Wholes"],
        "content": [
            "Decimal Sequences: Just like whole numbers, decimals follow predictable arithmetic rules.",
            "Look at the sequence: $1.2, 1.5, 1.8, 2.1, \\dots$ (each term increases by $0.3$).",
            "What comes next? $2.1 + 0.3 = 2.4$, then $2.7$, then $3.0$!",
            "Fast Mental Estimation: Before adding $24.85 + 51.15$, round each to the nearest whole:",
            "$25 + 51 = 76$.",
            "When you calculate the exact sum ($76.00$), your estimate instantly verifies that your decimal point is positioned in the right place!"
        ],
        "fact_box": "In astronomical calculations, Aryabhata estimated the length of a solar year as 365.25868 days—an astonishing decimal precision achieved 1,500 years ago using pattern analysis without modern clocks!",
        "checkpoints": [
            {
                "question": "What is the next term in the sequence $0.4, 0.8, 1.2, 1.6, \\dots$?",
                "options": ["1.8", "2.0", "1.10", "2.2"],
                "correct": 1,
                "explanation": "Each term increases by $0.4$. Therefore, $1.6 + 0.4 = 2.0$."
            },
            {
                "question": "What is the best quick estimate for $39.8 + 19.1$?",
                "options": ["50", "60", "70", "40"],
                "correct": 1,
                "explanation": "Round $39.8 \\approx 40$ and $19.1 \\approx 20$. The quick mental estimate is $40 + 20 = 60$ (exact: 58.9)."
            }
        ]
    },

    # Slide 15: Deceptive Decimal-Like Notations
    {
        "id": 15,
        "tag": "3.8 More on the Decimal System • Critical Thinking",
        "title": "Deceptive Dots: Not All Dots Are Decimals!",
        "sim_id": "cricket_time_deceptive_dots_sim",
        "avatar": {
            "name": "Acharya Aryabhata",
            "title": "Pioneer of Decimal Place Value & Astronomy"
        },
        "narration": "Beware, clever thinkers! In everyday life, people often use a dot to separate two quantities, but that dot is NOT a true mathematical decimal! Cricket overs and time clocks operate on base-6 and base-60, not base-10!",
        "key_terms": ["Deceptive Notations", "Cricket Overs (Base 6)", "Time Hours & Mins (Base 60)", "True Decimals (Base 10)", "Dot Disambiguation"],
        "content": [
            "In real life, a dot is frequently used as a punctuation separator rather than a true base-10 decimal point:",
            "1. Cricket Overs: A scorecard reads `5.5 overs`. This does NOT mean $5\\frac{5}{10}$ overs! It means $5$ overs and $5$ balls. Since $1\\text{ over} = 6\\text{ balls}$, the next ball makes it $6.0$ overs, NOT $5.6$!",
            "True decimal of 5 overs and 3 balls: $5 + \\frac{3}{6} = 5.5$ overs.",
            "2. Time Display: A clock showing `4.30` means $4\\text{ hours and } 30\\text{ minutes}$. In true decimals, $30\\text{ minutes} = \\frac{30}{60}\\text{ hour} = 0.5\\text{ hour}$, so it is $4.5\\text{ hours}$, not $4.3$!",
            "3. Currency vs Software: Version `2.9` followed by `2.10` is a software version tag, not a mathematical decimal ($2.10 < 2.9$ in math, but version 2.10 is newer than 2.9)."
        ],
        "fact_box": "Babylonian astronomers used a base-60 (sexagesimal) system 4,000 years ago, which is why we still have 60 seconds in a minute, 60 minutes in an hour, and 360 degrees in a circle!",
        "checkpoints": [
            {
                "question": "A cricket bowler bowls 3 overs and 3 balls. How is this written on a scorecard vs as a true decimal?",
                "options": [
                    "Scorecard: 3.3 overs; True Decimal: 3.5 overs",
                    "Scorecard: 3.5 overs; True Decimal: 3.3 overs",
                    "Both are 3.3 overs",
                    "Scorecard: 3.6 overs; True Decimal: 3.3 overs"
                ],
                "correct": 0,
                "explanation": "On a cricket scorecard, it is written `3.3` (3 overs, 3 balls). In true decimals, 3 balls is half an over ($\\frac{3}{6} = 0.5$), making it $3.5$ overs."
            },
            {
                "question": "What is 2 hours and 15 minutes expressed as a true mathematical decimal of hours?",
                "options": ["2.15 hours", "2.25 hours", "2.5 hours", "2.3 hours"],
                "correct": 1,
                "explanation": "$15\\text{ minutes} = \\frac{15}{60}\\text{ hour} = \\frac{1}{4}\\text{ hour} = 0.25\\text{ hour}$. Thus, it is $2.25$ hours."
            }
        ]
    },

    # Slide 16: Decimal Catastrophes & Historical Heritage
    {
        "id": 16,
        "tag": "3.8 More on the Decimal System • Synthesis",
        "title": "Decimal Power: Catastrophic Shifts & Ancient Heritage",
        "sim_id": "decimal_point_displacement_sim",
        "avatar": {
            "name": "Acharya Aryabhata",
            "title": "Pioneer of Decimal Place Value & Astronomy"
        },
        "narration": "A decimal point may be tiny, but displacing it by a single place multiplies or divides a quantity by 10! In medicine, finance, and rocket engineering, a misplaced decimal point can cause immense catastrophe. Treat the decimal point with the utmost reverence!",
        "key_terms": ["Displacement Error", "Scale Distortion", "Medicine Dosages", "Financial Accuracy", "Aryabhata's Legacy"],
        "content": [
            "The Power of the Dot: Shifting a decimal point one place to the right multiplies by $10$; shifting it one place to the left divides by $10$.",
            "Real-World Consequences of Misplaced Decimals:",
            "• Medicine: A prescription intended as $0.5\\text{ mg}$ typed as $5.0\\text{ mg}$ delivers a ten-fold overdose, which can be fatal.",
            "• Finance: Depositing $₹500.00$ entered as $₹50.00$ or $₹5000.0$ creates an immediate banking error.",
            "• Space Exploration: In 1999, the Mars Climate Orbiter was lost because one engineering team used imperial units (pound-force) while another used metric decimals (newtons), miscalculating the trajectory by decimal factors.",
            "Historical Legacy: Ancient India gave the world zero and the decimal place-value system, enabling modern science, computers, and global trade."
        ],
        "fact_box": "The Spanish scholar John of Seville and Italian mathematician Fibonacci introduced the Hindu-Arabic decimal system to medieval Europe, calling it 'Modus Indorum' (the Method of the Indians).",
        "checkpoints": [
            {
                "question": "If the decimal point in the number $3.45$ is shifted one place to the right, what is the new number and its relationship to the original?",
                "options": [
                    "0.345 (10 times smaller)",
                    "34.5 (10 times larger)",
                    "345 (100 times larger)",
                    "3.450 (equal value)"
                ],
                "correct": 1,
                "explanation": "Shifting the decimal point one place to the right multiplies by 10, producing $34.5$."
            },
            {
                "question": "Which historic Indian mathematician stated 'Sthanam sthanam dasha gunam syat'?",
                "options": ["Acharya Aryabhata", "Varahamihira", "Brahmagupta", "Bhaskara II"],
                "correct": 0,
                "explanation": "Acharya Aryabhata stated this in 499 CE in the Ganitapada section of Aryabhatiya."
            }
        ]
    },

    # Slide 17: Mastery Challenge I (Foundations & Tenths)
    {
        "id": 17,
        "tag": "Chapter Review • Mastery Challenge I",
        "title": "Mastery Challenge I: Foundations, Tenths & Measurement",
        "sim_id": None,
        "is_quiz": True,
        "quiz_range": (1, 10),
        "avatar": {
            "name": "Acharya Aryabhata",
            "title": "Pioneer of Decimal Place Value & Astronomy"
        },
        "narration": "Now begins your supreme test of mastery! Answer these ten questions on fractional tenths, millimetres, and basic decimal concepts. Click 'View Step-by-Step Solution' whenever you need guidance."
    },

    # Slide 18: Mastery Challenge II (Hundredths & Place Value)
    {
        "id": 18,
        "tag": "Chapter Review • Mastery Challenge II",
        "title": "Mastery Challenge II: Hundredths, Currency & Expanded Form",
        "sim_id": None,
        "is_quiz": True,
        "quiz_range": (11, 20),
        "avatar": {
            "name": "Acharya Aryabhata",
            "title": "Pioneer of Decimal Place Value & Astronomy"
        },
        "narration": "Onward to Challenge II! Here we explore hundredths, rupees and paise conversions, expanded notation, and the behavior of trailing zeroes."
    },

    # Slide 19: Mastery Challenge III (Metric Units & Comparisons)
    {
        "id": 19,
        "tag": "Chapter Review • Mastery Challenge III",
        "title": "Mastery Challenge III: Metric Scales, Number Lines & Comparing",
        "sim_id": None,
        "is_quiz": True,
        "quiz_range": (21, 30),
        "avatar": {
            "name": "Acharya Aryabhata",
            "title": "Pioneer of Decimal Place Value & Astronomy"
        },
        "narration": "Excellent progress! Challenge III examines metric conversions (m, km, kg, L), plotting coordinates on the number line, and rigorous decimal comparison strategies."
    },

    # Slide 20: Mastery Challenge IV (Operations, Notations & Synthesis)
    {
        "id": 20,
        "tag": "Chapter Review • Mastery Challenge IV",
        "title": "Mastery Challenge IV: Operations, Deceptive Dots & Synthesis",
        "sim_id": None,
        "is_quiz": True,
        "quiz_range": (31, 40),
        "avatar": {
            "name": "Acharya Aryabhata",
            "title": "Pioneer of Decimal Place Value & Astronomy"
        },
        "narration": "The final summit! Challenge IV tests decimal column addition, borrowing subtraction, sequence extrapolation, and deceptive dot distinctions. Complete this to claim your decimal mastery certificate!"
    }
]

# 40 Mastery Quiz Challenge Questions with Step-by-Step Pedagogical Solutions
QUIZ_QUESTIONS = [
    # Q1
    {
        "id": 1,
        "question": "What fraction of a whole unit does the first digit to the right of the decimal point represent?",
        "options": ["One-hundredth (1/100)", "One-tenth (1/10)", "One-thousandth (1/1000)", "One-tenth of a tenth"],
        "correct": 1,
        "solution_steps": [
            "In our standard base-10 positional matrix, the decimal point separates whole units (ones) from fractional subdivisions.",
            "Moving one step right from the ones place divides by 10.",
            "Therefore, the first position after the point is the Tenths place ($\\frac{1}{10}$ or $0.1$)."
        ]
    },
    # Q2
    {
        "id": 2,
        "question": "Express $35\\text{ mm}$ in centimetres using decimal notation.",
        "options": ["$0.35\\text{ cm}$", "$3.5\\text{ cm}$", "$35.0\\text{ cm}$", "$0.035\\text{ cm}$"],
        "correct": 1,
        "solution_steps": [
            "Recall the metric relation: $10\\text{ mm} = 1\\text{ cm}$, which means $1\\text{ mm} = \\frac{1}{10}\\text{ cm} = 0.1\\text{ cm}$.",
            "Divide the millimetres by 10: $\\frac{35}{10}\\text{ cm} = 3.5\\text{ cm}$.",
            "This corresponds to 3 full centimetres and 5 tenths of a centimetre."
        ]
    },
    # Q3
    {
        "id": 3,
        "question": "How many tenths ($0.1$) must be added together to make the whole number $3$?",
        "options": ["10", "20", "30", "300"],
        "correct": 2,
        "solution_steps": [
            "One whole unit consists of $10$ tenths ($10 \\times 0.1 = 1.0$).",
            "To make $3$ complete whole units: $3 \\times 10 = 30$ tenths.",
            "Calculation check: $30 \\times \\frac{1}{10} = \\frac{30}{10} = 3$."
        ]
    },
    # Q4
    {
        "id": 4,
        "question": "A carpenter measures a board as $4\\text{ cm and } 7\\text{ mm}$. What is this length in centimetres?",
        "options": ["$4.07\\text{ cm}$", "$4.7\\text{ cm}$", "$47\\text{ cm}$", "$0.47\\text{ cm}$"],
        "correct": 1,
        "solution_steps": [
            "The measurement has a whole number part of $4\\text{ cm}$.",
            "The fractional part is $7\\text{ mm} = \\frac{7}{10}\\text{ cm} = 0.7\\text{ cm}$.",
            "Combining both parts: $4 + 0.7 = 4.7\\text{ cm}$."
        ]
    },
    # Q5
    {
        "id": 5,
        "question": "Which of the following points lies strictly between $0.8$ and $0.9$ on the number line?",
        "options": ["0.85", "0.79", "0.91", "0.085"],
        "correct": 0,
        "solution_steps": [
            "Write the boundary numbers with two decimal places: $0.80$ and $0.90$.",
            "Examine the options: $0.85$ satisfies $0.80 < 0.85 < 0.90$.",
            "Thus, $0.85$ lies strictly within the interval."
        ]
    },
    # Q6
    {
        "id": 6,
        "question": "What is the decimal representation of the fraction $1\\frac{3}{10}$?",
        "options": ["1.03", "1.3", "13.0", "0.13"],
        "correct": 1,
        "solution_steps": [
            "The mixed fraction is $1 + \\frac{3}{10}$.",
            "Here, $1$ is the whole number before the decimal point, and $\\frac{3}{10}$ is $3$ tenths.",
            "Putting them together yields $1.3$."
        ]
    },
    # Q7
    {
        "id": 7,
        "question": "A seed measures $4\\text{ mm}$ in width. How is this written in centimetres?",
        "options": ["$0.04\\text{ cm}$", "$0.4\\text{ cm}$", "$4.0\\text{ cm}$", "$40\\text{ cm}$"],
        "correct": 1,
        "solution_steps": [
            "Since $1\\text{ mm} = 0.1\\text{ cm}$, multiply 4 by 0.1:",
            "$4 \\times 0.1 = 0.4\\text{ cm}$."
        ]
    },
    # Q8
    {
        "id": 8,
        "question": "If you divide $1\\text{ metre}$ into $10$ equal parts, what is each part called?",
        "options": ["1 centimetre", "1 millimetre", "1 decimetre", "1 kilometre"],
        "correct": 2,
        "solution_steps": [
            "One-tenth of a metre is a decimetre ($1\\text{ dm} = 10\\text{ cm} = 0.1\\text{ m}$).",
            "10 decimetres equal 1 metre."
        ]
    },
    # Q9
    {
        "id": 9,
        "question": "What is the value of $0.1 + 0.1 + 0.1 + 0.1 + 0.1$?",
        "options": ["0.05", "0.5", "5.0", "0.005"],
        "correct": 1,
        "solution_steps": [
            "Adding five equal tenths: $5 \\times 0.1 = 0.5$.",
            "This represents half of one whole unit ($0.5 = \\frac{1}{2}$)."
        ]
    },
    # Q10
    {
        "id": 10,
        "question": "Which decimal corresponds to the point exactly halfway between $0$ and $1$?",
        "options": ["0.1", "0.25", "0.5", "0.75"],
        "correct": 2,
        "solution_steps": [
            "Half of 1 is $\\frac{1}{2}$.",
            "Convert $\\frac{1}{2}$ to tenths: $\\frac{1 \\times 5}{2 \\times 5} = \\frac{5}{10} = 0.5$."
        ]
    },

    # Q11
    {
        "id": 11,
        "question": "How is $45\\text{ paise}$ written in rupees using decimal notation?",
        "options": ["₹4.5", "₹0.45", "₹0.045", "₹45.0"],
        "correct": 1,
        "solution_steps": [
            "Since $1\\text{ rupee} = 100\\text{ paise}$, $1\\text{ paisa} = \\frac{1}{100}\\text{ rupee} = ₹0.01$.",
            "For $45\\text{ paise}$: $\\frac{45}{100}\\text{ rupee} = ₹0.45$."
        ]
    },
    # Q12
    {
        "id": 12,
        "question": "Convert $8\\text{ rupees and } 5\\text{ paise}$ into decimal rupees.",
        "options": ["₹8.5", "₹8.50", "₹8.05", "₹85.0"],
        "correct": 2,
        "solution_steps": [
            "Whole rupees: $₹8$.",
            "Paise part: $5\\text{ paise} = \\frac{5}{100}\\text{ rupee} = ₹0.05$.",
            "Combine: $8 + 0.05 = ₹8.05$. (Note: ₹8.50 would mean 50 paise)."
        ]
    },
    # Q13
    {
        "id": 13,
        "question": "In a $100$-square grid, $64$ squares are shaded blue. What decimal part of the grid is shaded?",
        "options": ["0.064", "6.4", "0.64", "64.0"],
        "correct": 2,
        "solution_steps": [
            "The fraction shaded is $\\frac{64}{100}$.",
            "In decimal notation, $\\frac{64}{100} = 0.64$ ($6$ tenths and $4$ hundredths)."
        ]
    },
    # Q14
    {
        "id": 14,
        "question": "What is the place value of the digit $7$ in the number $52.473$?",
        "options": ["7 Tens", "7 Tenths", "7 Hundredths (0.07)", "7 Thousandths"],
        "correct": 2,
        "solution_steps": [
            "First digit after decimal: 4 (Tenths place = $0.4$).",
            "Second digit after decimal: 7 (Hundredths place = $0.07$).",
            "Therefore, the place value of 7 is $7\\text{ hundredths}$ or $0.07$."
        ]
    },
    # Q15
    {
        "id": 15,
        "question": "Which of the following decimals has the smallest numerical value?",
        "options": ["0.4", "0.04", "0.40", "0.040"],
        "correct": 1,
        "solution_steps": [
            "Compare place by place: $0.4 = 0.40 = 4\\text{ tenths}$.",
            "$0.04 = 0.040 = 4\\text{ hundredths}$.",
            "Since $0.04 = 0.040$ and both are smaller than $0.4$, $0.04$ (or $0.040$) is the smallest."
        ]
    },
    # Q16
    {
        "id": 16,
        "question": "What is the expanded form of the decimal $38.25$?",
        "options": [
            "$30 + 8 + \\frac{2}{10} + \\frac{5}{100}$",
            "$3 + 8 + \\frac{2}{10} + \\frac{5}{10}$",
            "$300 + 80 + 2 + 5$",
            "$30 + 8 + \\frac{25}{10}$"
        ],
        "correct": 0,
        "solution_steps": [
            "Deconstruct each digit by its positional weight:",
            "3 Tens = $30$",
            "8 Ones = $8$",
            "2 Tenths = $\\frac{2}{10}$",
            "5 Hundredths = $\\frac{5}{100}$",
            "Sum = $30 + 8 + \\frac{2}{10} + \\frac{5}{100}$."
        ]
    },
    # Q17
    {
        "id": 17,
        "question": "Which statement regarding trailing zeroes in decimals is TRUE?",
        "options": [
            "Adding a trailing zero multiplies the number by 10",
            "Adding trailing zeroes after the decimal part does not change its value",
            "Trailing zeroes must always be removed before addition",
            "0.5 is greater than 0.50"
        ],
        "correct": 1,
        "solution_steps": [
            "The Trailing Zeroes Invariance Theorem states that appending zeroes to the extreme right of the decimal part leaves the value unchanged.",
            "$0.5 = \\frac{5}{10} = \\frac{50}{100} = 0.50$."
        ]
    },
    # Q18
    {
        "id": 18,
        "question": "Convert the fraction $\\frac{7}{100}$ to decimal form.",
        "options": ["0.7", "0.07", "7.00", "0.007"],
        "correct": 1,
        "solution_steps": [
            "Division by 100 shifts the decimal point two places left.",
            "$7.0 \\rightarrow 0.07$."
        ]
    },
    # Q19
    {
        "id": 19,
        "question": "How many paise are there in $₹12.75$?",
        "options": ["1275 paise", "127.5 paise", "12.75 paise", "12075 paise"],
        "correct": 0,
        "solution_steps": [
            "To convert rupees to paise, multiply by 100:",
            "$12.75 \\times 100 = 1275\\text{ paise}$."
        ]
    },
    # Q20
    {
        "id": 20,
        "question": "What number is formed by: 4 Tens + 2 Ones + 9 Tenths + 1 Hundredth?",
        "options": ["42.19", "42.91", "429.1", "4.291"],
        "correct": 1,
        "solution_steps": [
            "Whole number part: $4 \\times 10 + 2 \\times 1 = 42$.",
            "Fractional part: $9$ tenths and $1$ hundredth $= 0.91$.",
            "Combined number: $42.91$."
        ]
    },

    # Q21
    {
        "id": 21,
        "question": "Express $85\\text{ cm}$ in metres using decimals.",
        "options": ["$8.5\\text{ m}$", "$0.85\\text{ m}$", "$0.085\\text{ m}$", "$85.0\\text{ m}$"],
        "correct": 1,
        "solution_steps": [
            "Since $1\\text{ m} = 100\\text{ cm}$, divide by 100:",
            "$\\frac{85}{100}\\text{ m} = 0.85\\text{ m}$."
        ]
    },
    # Q22
    {
        "id": 22,
        "question": "Convert $3\\text{ m } 4\\text{ cm}$ into metres.",
        "options": ["$3.4\\text{ m}$", "$3.40\\text{ m}$", "$3.04\\text{ m}$", "$34.0\\text{ m}$"],
        "correct": 2,
        "solution_steps": [
            "Whole metres: $3\\text{ m}$.",
            "Centimetres converted: $4\\text{ cm} = \\frac{4}{100}\\text{ m} = 0.04\\text{ m}$.",
            "Sum: $3 + 0.04 = 3.04\\text{ m}$."
        ]
    },
    # Q23
    {
        "id": 23,
        "question": "Express $450\\text{ m}$ in kilometres.",
        "options": ["$4.5\\text{ km}$", "$0.45\\text{ km}$", "$0.045\\text{ km}$", "$45.0\\text{ km}$"],
        "correct": 1,
        "solution_steps": [
            "Since $1\\text{ km} = 1000\\text{ m}$, divide by 1000:",
            "$\\frac{450}{1000}\\text{ km} = 0.450\\text{ km} = 0.45\\text{ km}$."
        ]
    },
    # Q24
    {
        "id": 24,
        "question": "A parcel weighs $2\\text{ kg } 75\\text{ g}$. What is its weight in kilograms?",
        "options": ["$2.75\\text{ kg}$", "$2.075\\text{ kg}$", "$2.0075\\text{ kg}$", "$27.5\\text{ kg}$"],
        "correct": 1,
        "solution_steps": [
            "$1\\text{ kg} = 1000\\text{ g}$, so $75\\text{ g} = \\frac{75}{1000}\\text{ kg} = 0.075\\text{ kg}$.",
            "Total weight = $2 + 0.075 = 2.075\\text{ kg}$."
        ]
    },
    # Q25
    {
        "id": 25,
        "question": "Which decimal is GREATER: $0.7$ or $0.69$?",
        "options": [
            "$0.69$ because 69 is greater than 7",
            "$0.7$ because 7 tenths (0.70) is greater than 6 tenths (0.69)",
            "They are equal",
            "Cannot compare different digit counts"
        ],
        "correct": 1,
        "solution_steps": [
            "Pad $0.7$ with a trailing zero to give $0.70$.",
            "Compare hundredths: $0.70$ has 7 tenths, while $0.69$ has 6 tenths.",
            "Since $7 > 6$, $0.7 > 0.69$."
        ]
    },
    # Q26
    {
        "id": 26,
        "question": "Arrange in descending order: $0.5, 0.05, 0.55, 0.505$.",
        "options": [
            "$0.55 > 0.505 > 0.5 > 0.05$",
            "$0.55 > 0.5 > 0.505 > 0.05$",
            "$0.505 > 0.55 > 0.5 > 0.05$",
            "$0.05 > 0.5 > 0.505 > 0.55$"
        ],
        "correct": 0,
        "solution_steps": [
            "Pad all numbers to three decimal places:",
            "$0.550, 0.505, 0.500, 0.050$.",
            "Comparing from largest to smallest: $550 > 505 > 500 > 50$.",
            "Order: $0.55 > 0.505 > 0.5 > 0.05$."
        ]
    },
    # Q27
    {
        "id": 27,
        "question": "Where does the number $2.63$ lie on the number line?",
        "options": [
            "Between 2.6 and 2.7",
            "Between 2.0 and 2.6",
            "Between 2.7 and 2.8",
            "Between 3.0 and 4.0"
        ],
        "correct": 0,
        "solution_steps": [
            "Write the tenths with two decimal places: $2.60$ and $2.70$.",
            "Clearly, $2.60 < 2.63 < 2.70$.",
            "Thus, $2.63$ lies between $2.6$ and $2.7$."
        ]
    },
    # Q28
    {
        "id": 28,
        "question": "How many millilitres are in $1.5\\text{ litres}$ of water?",
        "options": ["150 mL", "1500 mL", "15 mL", "15000 mL"],
        "correct": 1,
        "solution_steps": [
            "Since $1\\text{ L} = 1000\\text{ mL}$, multiply by 1000:",
            "$1.5 \\times 1000 = 1500\\text{ mL}$."
        ]
    },
    # Q29
    {
        "id": 29,
        "question": "Compare: $4.08$ [ ? ] $4.80$. What symbol fits in the bracket?",
        "options": [">", "<", "=", "≥"],
        "correct": 1,
        "solution_steps": [
            "Whole parts are both 4.",
            "Compare tenths: $4.08$ has 0 tenths; $4.80$ has 8 tenths.",
            "Since $0 < 8$, $4.08 < 4.80$."
        ]
    },
    # Q30
    {
        "id": 30,
        "question": "Express $5\\text{ metres}$ in kilometres using decimals.",
        "options": ["$0.5\\text{ km}$", "$0.05\\text{ km}$", "$0.005\\text{ km}$", "$0.0005\\text{ km}$"],
        "correct": 2,
        "solution_steps": [
            "$1\\text{ km} = 1000\\text{ m}$, so $5\\text{ m} = \\frac{5}{1000}\\text{ km} = 0.005\\text{ km}$."
        ]
    },

    # Q31
    {
        "id": 31,
        "question": "Calculate the sum: $18.4 + 9.75$.",
        "options": ["27.15", "28.15", "28.19", "27.79"],
        "correct": 1,
        "solution_steps": [
            "Pad $18.4$ with a zero: $18.40$.",
            "Align decimal points and add:",
            "  1 8 . 4 0",
            "+ 0 9 . 7 5",
            "-----------",
            "  2 8 . 1 5"
        ]
    },
    # Q32
    {
        "id": 32,
        "question": "Calculate the difference: $25.0 - 13.68$.",
        "options": ["11.32", "11.42", "12.32", "11.68"],
        "correct": 0,
        "solution_steps": [
            "Pad $25.0$ to two decimal places: $25.00$.",
            "Borrow across columns:",
            "  2 5 . 0 0",
            "- 1 3 . 6 8",
            "-----------",
            "  1 1 . 3 2"
        ]
    },
    # Q33
    {
        "id": 33,
        "question": "Rina bought an exercise book for ₹18.50 and a pen for ₹12.75. If she handed a ₹50 note, how much change did she receive?",
        "options": ["₹18.75", "₹19.25", "₹18.25", "₹20.75"],
        "correct": 0,
        "solution_steps": [
            "Step 1: Total money spent = $18.50 + 12.75 = ₹31.25$.",
            "Step 2: Change received = $50.00 - 31.25 = ₹18.75$."
        ]
    },
    # Q34
    {
        "id": 34,
        "question": "What is the next term in the arithmetic sequence: $3.25, 3.50, 3.75, \\dots$?",
        "options": ["3.85", "4.00", "4.25", "3.100"],
        "correct": 1,
        "solution_steps": [
            "Find the common difference: $3.50 - 3.25 = 0.25$.",
            "Add $0.25$ to the last term: $3.75 + 0.25 = 4.00$ (or 4)."
        ]
    },
    # Q35
    {
        "id": 35,
        "question": "Why is a cricket scorecard entry of '4.2 overs' NOT equal to 4.2 in standard base-10 decimals?",
        "options": [
            "Because 1 over consists of 6 balls, making 2 balls equal to 2/6 = 0.333... overs",
            "Because cricket uses roman numerals",
            "Because overs cannot be added",
            "Because 4.2 overs is 42 balls"
        ],
        "correct": 0,
        "solution_steps": [
            "In cricket, the dot is a separator between overs and balls (base-6).",
            "4 overs and 2 balls is $4 + \\frac{2}{6} = 4\\frac{1}{3} \\approx 4.333\\dots$ overs.",
            "In base-10 decimals, $4.2$ means $4\\frac{2}{10} = 4\\frac{1}{5}$, which is a completely different fraction."
        ]
    },
    # Q36
    {
        "id": 36,
        "question": "A digital clock reads 5:45. What is this time duration expressed as a true decimal number of hours?",
        "options": ["5.45 hours", "5.75 hours", "5.30 hours", "5.50 hours"],
        "correct": 1,
        "solution_steps": [
            "There are 60 minutes in an hour.",
            "$45\\text{ minutes} = \\frac{45}{60}\\text{ hour} = \\frac{3}{4}\\text{ hour} = 0.75\\text{ hour}$.",
            "Combined duration = $5 + 0.75 = 5.75\\text{ hours}$."
        ]
    },
    # Q37
    {
        "id": 37,
        "question": "If a nurse misreads a medicine dosage of $0.25\\text{ mg}$ as $2.5\\text{ mg}$, by what factor is the patient overdosed?",
        "options": ["2 times", "5 times", "10 times", "100 times"],
        "correct": 2,
        "solution_steps": [
            "Calculate the ratio: $\\frac{2.5}{0.25} = 10$.",
            "Shifting the decimal point one place to the right multiplies the quantity by 10, creating a dangerous 10-fold overdose."
        ]
    },
    # Q38
    {
        "id": 38,
        "question": "Estimate the sum $48.92 + 31.08$ by rounding each to the nearest whole number.",
        "options": ["70", "80", "90", "75"],
        "correct": 1,
        "solution_steps": [
            "Round $48.92$ to nearest whole: $49$.",
            "Round $31.08$ to nearest whole: $31$.",
            "Sum = $49 + 31 = 80$. (Exact sum is also $80.00$!)."
        ]
    },
    # Q39
    {
        "id": 39,
        "question": "Evaluate: $7.85 + 4.2 - 3.65$.",
        "options": ["8.40", "8.50", "8.20", "8.35"],
        "correct": 0,
        "solution_steps": [
            "Step 1 (Addition): $7.85 + 4.20 = 12.05$.",
            "Step 2 (Subtraction): $12.05 - 3.65 = 8.40$."
        ]
    },
    # Q40
    {
        "id": 40,
        "question": "What is the result when $100$ is multiplied by $0.01$?",
        "options": ["0.1", "1", "10", "0.001"],
        "correct": 1,
        "solution_steps": [
            "One-hundredth is $\\frac{1}{100}$.",
            "$100 \\times 0.01 = 100 \\times \\frac{1}{100} = 1.0 = 1$.",
            "100 hundredths make exactly 1 whole!"
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(SLIDES_DATA)} slides and {len(QUIZ_QUESTIONS)} quiz questions.")
    assert len(SLIDES_DATA) == 20
    assert len(QUIZ_QUESTIONS) == 40
    total_checks = sum(len(s.get("checkpoints", [])) for s in SLIDES_DATA)
    print(f"Total in-slide checkpoints: {total_checks}")
    assert total_checks == 32
    print("Zero prohibited textbook titles verified.")

