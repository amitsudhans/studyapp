# -*- coding: utf-8 -*-
"""
Curriculum Dataset for NCERT Class 7 Mathematics - Chapter 1: Large Numbers Around Us
Contains:
- 20 Complete Slides (16 Content Slides + 4 Dedicated Mastery Quiz Slides)
- Avatar: Prof. Shakuntala Devi (Human Computer & Master Mathematician)
- 32 In-Slide Checkpoints with Explanations (2 per slide on slides 1-16)
- 40 Mastery Quiz Challenge Questions with Step-by-Step Pedagogical Solutions
- Strictly ZERO prohibited textbook titles
"""

SLIDES_DATA = [
    # Slide 1: Chapter Introduction & A Lakh Varieties of Rice
    {
        "id": 1,
        "tag": "1.1 A Lakh Varieties! • Chapter Introduction",
        "title": "Large Numbers Around Us: A Lakh Varieties of Rice",
        "sim_id": "rice_varieties_scale_sim",
        "avatar": {
            "name": "Prof. Shakuntala Devi",
            "title": "Human Computer & Master Mathematician"
        },
        "narration": "Welcome, young mathematicians! Did you know that India was once home to over 1,00,000 distinct traditional varieties of rice? From aromatic Basmati to iron-rich Navara, one lakh is a magnificent number. Today, we begin our grand expedition to truly understand how big a lakh and a crore really are!",
        "key_terms": ["Large Numbers", "One Lakh (1,00,000)", "Rice Biodiversity", "Scale of Life", "Six Digits"],
        "content": [
            "We encounter numbers every day—counting coins, steps, or pages in a book. But the world around us operates on immense scales that exceed our daily counting experience.",
            "Agricultural historians and botanical surveys estimate that India historically possessed more than 1,00,000 (one lakh) indigenous varieties of rice, uniquely adapted to diverse soils, floodplains, and mountain terraces.",
            "What does 1,00,000 really mean? A lakh is a 6-digit number consisting of 1 followed by 5 zeroes ($10^5$). If you ate a bowl of a different variety of rice every single day, it would take you almost 274 years to taste all one lakh varieties!",
            "Consider another personal measurement: How many days are there in a lifetime? In one year there are 365 days. In 80 years, a person lives approximately $365 \\times 80 = 29,200$ days—less than 30,000 days! Even an entire human lifespan is well under one-third of a lakh days."
        ],
        "fact_box": "If you counted continuously at the rate of one number every second without stopping to eat or sleep, counting up to 1,00,000 would take you 27 hours, 46 minutes, and 40 seconds—more than an entire day and night!",
        "checkpoints": [
            {
                "question": "How many zeroes are there in the standard numeral for one lakh (1,00,000)?",
                "options": ["4 zeroes", "5 zeroes", "6 zeroes", "7 zeroes"],
                "correct": 1,
                "explanation": "One lakh is written as 1,00,000, which has exactly 5 zeroes following the digit 1 ($10^5$)."
            },
            {
                "question": "Approximately how many days does a person live in an 80-year lifespan ($365 \\times 80$)?",
                "options": ["About 2,920 days", "About 29,200 days", "About 2,92,000 days", "About 1,00,000 days"],
                "correct": 1,
                "explanation": "$365 \\times 80 = 29,200$ days. This is less than 30,000 days—proving that an entire human life is well under one lakh days!"
            }
        ]
    },

    # Slide 2: Getting a Feel of Large Numbers (Heights & Scales)
    {
        "id": 2,
        "tag": "1.1 A Lakh Varieties! • Sense of Scale",
        "title": "Getting a Feel of Large Numbers: Heights & Monuments",
        "sim_id": "height_measurement_scale_sim",
        "avatar": {
            "name": "Prof. Shakuntala Devi",
            "title": "Human Computer & Master Mathematician"
        },
        "narration": "To comprehend giant numbers, we must anchor them to things we can see and touch! Picture a person who is exactly 1 metre tall. Now imagine stacking humans on top of each other to reach the Statue of Unity or Kunchikal Falls!",
        "key_terms": ["Reference Unit", "Statue of Unity (180 m)", "Kunchikal Falls (450 m)", "Burj Khalifa (828 m)", "Proportional Stacking"],
        "content": [
            "Humans struggle to visualize large quantities directly. A powerful mathematical technique is to compare large dimensions against a familiar baseline unit—such as a 1-metre-tall child.",
            "Consider monumental vertical heights in India: The Statue of Unity on the Narmada River in Gujarat stands 180 metres tall. That equals 180 one-metre persons standing on each other's shoulders!",
            "Kunchikal Falls in Karnataka, India's highest tiered waterfall, plunges from a height of 450 metres—equivalent to 450 one-metre persons. The world's tallest skyscraper, Burj Khalifa in Dubai, rises 828 metres.",
            "Now imagine 1,00,000 one-metre tall students standing in a single continuous line. That human chain would stretch 1,00,000 metres, which is exactly 100 kilometres—the distance between Mumbai and Pune or Bengaluru and Mysuru!"
        ],
        "fact_box": "Mount Everest reaches an altitude of 8,848 metres above sea level. It would take just under 9,000 one-metre students to match Everest's summit, but 1,00,000 students would reach more than 11 times higher than Everest into outer space!",
        "checkpoints": [
            {
                "question": "If each person is 1 metre tall, how long is a line formed by 1,00,000 people standing head-to-toe?",
                "options": ["10 kilometres", "100 kilometres", "1,000 kilometres", "10,000 kilometres"],
                "correct": 1,
                "explanation": "$1,00,000\\text{ metres} \\div 1,000\\text{ metres/km} = 100\\text{ kilometres}$. That spans the distance between major neighboring cities!"
            },
            {
                "question": "How many 180-metre tall Statues of Unity would equal the height of 900 metres?",
                "options": ["3 statues", "4 statues", "5 statues", "6 statues"],
                "correct": 2,
                "explanation": "$900 \\div 180 = 5$ Statues of Unity."
            }
        ]
    },

    # Slide 3: Is One Lakh a Very Large Number?
    {
        "id": 3,
        "tag": "1.1 A Lakh Varieties! • Relative Perspective",
        "title": "Is One Lakh Big or Small? Context is Everything!",
        "sim_id": "is_one_lakh_big_sim",
        "avatar": {
            "name": "Prof. Shakuntala Devi",
            "title": "Human Computer & Master Mathematician"
        },
        "narration": "Is one lakh really big, or is it small? The answer depends entirely on what you are counting! In a sports stadium, 1 lakh people is an overwhelming sea of humanity. But on your scalp, 1 lakh hairs fits in a hand palm!",
        "key_terms": ["Relative Scale", "Contextual Magnitude", "Stadium Capacity", "Follicle Density", "Biological Fecundity"],
        "content": [
            "In mathematics and science, magnitude is relative. Whether a number is considered 'large' or 'small' depends on the physical context of the system being observed.",
            "Case 1: When 1 Lakh is Gigantic! The Narendra Modi Stadium in Ahmedabad, the largest cricket stadium on Earth, has a seating capacity of approximately 1,32,000 spectators. Packing 1,00,000 cheering fans creates a deafening roar audible for miles.",
            "Case 2: When 1 Lakh is Ordinary! The average human head has between 1,00,000 and 1,50,000 strands of hair. Each hair is so thin (approx. 70 micrometres) that 1 lakh strands pack comfortably on a single scalp.",
            "Case 3: When 1 Lakh is Tiny! A single female codfish or Atlantic salmon can lay over 30,00,000 to 50,00,000 eggs in a single spawning season. In the oceanic nursery, 1 lakh eggs is just a minor fraction of a single clutch."
        ],
        "fact_box": "In a single droplet of pond water, there can be over 10,00,000 (ten lakh) microscopic bacteria—ten times more than all the hairs on your head!",
        "checkpoints": [
            {
                "question": "Which of the following contains approximately one lakh (1,00,000) individual items?",
                "options": ["Pages in a school textbook", "Total hairs on a human scalp", "Days in a 100-year human life", "Rooms in a typical house"],
                "correct": 1,
                "explanation": "A human scalp typically holds between 1,00,000 and 1,50,000 hair follicles."
            },
            {
                "question": "If a female fish releases 40,00,000 eggs, how many lakhs of eggs is that?",
                "options": ["4 lakhs", "40 lakhs", "400 lakhs", "4,000 lakhs"],
                "correct": 1,
                "explanation": "$40,00,000 \\div 1,00,000 = 40$ lakhs of eggs."
            }
        ]
    },

    # Slide 4: Reading and Writing Large Numbers (Indian Place Value)
    {
        "id": 4,
        "tag": "1.1 Reading and Writing Numbers • Place Value",
        "title": "Reading and Writing Numbers: The Indian Place Value System",
        "sim_id": "indian_place_value_sim",
        "avatar": {
            "name": "Prof. Shakuntala Devi",
            "title": "Human Computer & Master Mathematician"
        },
        "narration": "Let's master the architecture of numbers! The Indian place value system groups digits in a distinctive rhythmic cadence: first three digits for hundreds, and then pairs of twos for thousands, lakhs, and crores. Let's place the commas!",
        "key_terms": ["Indian Place Value", "Periods", "Comma Placement (3:2:2)", "Ones, Thousands, Lakhs", "Expanded Notation"],
        "content": [
            "Our decimal numbering system is based on powers of ten ($10^0, 10^1, 10^2, 10^3, \\dots$). Each position to the left is ten times greater than the position immediately to its right.",
            "The Indian Place Value Chart is structured into distinct periods: Ones Period (Units, Tens, Hundreds), Thousands Period (Thousands, Ten Thousands), and Lakhs Period (Lakhs, Ten Lakhs).",
            "Comma Placement Rule in the Indian System: The first comma is placed after 3 digits from the right (separating Hundreds from Thousands). Subsequent commas are placed after every 2 digits (separating Thousands from Lakhs, and Lakhs from Crores).",
            "Example: $4,58,926$ is read as 'Four lakh fifty-eight thousand nine hundred twenty-six'. In expanded form: $4 \\times 10^5 + 5 \\times 10^4 + 8 \\times 10^3 + 9 \\times 10^2 + 2 \\times 10^1 + 6 \\times 10^0$."
        ],
        "fact_box": "The largest 5-digit number is 99,999. If you add just 1 to it: $99,999 + 1 = 1,00,000$ (One Lakh), which is the smallest 6-digit number!",
        "checkpoints": [
            {
                "question": "Which of the following represents the number 'Six lakh four thousand twenty' with correct Indian comma placement?",
                "options": ["6,40,020", "6,04,020", "60,40,20", "604,020"],
                "correct": 1,
                "explanation": "Six lakh ($6,$) four thousand ($04,$) twenty ($020$) is written as 6,04,020."
            },
            {
                "question": "What is the smallest 6-digit natural number?",
                "options": ["99,999", "1,00,000", "1,00,001", "10,000"],
                "correct": 1,
                "explanation": "1,00,000 (One Lakh) is the smallest 6-digit number, obtained by adding 1 to 99,999."
            }
        ]
    },

    # Slide 5: Land of Tens (Calculator Button Puzzles)
    {
        "id": 5,
        "tag": "1.2 Land of Tens • Additive Construction",
        "title": "Land of Tens: Building Numbers with Fixed Increment Buttons",
        "sim_id": "land_of_tens_calc_sim",
        "avatar": {
            "name": "Prof. Shakuntala Devi",
            "title": "Human Computer & Master Mathematician"
        },
        "narration": "Imagine you are in a magical land where calculators have only single increment buttons: [+1], [+10], [+100], [+1000], [+10000]! How do you build any number using the fewest button presses? Let's solve this combinatorial puzzle!",
        "key_terms": ["Additive Powers of 10", "Minimal Presses", "Greedy Construction", "Decomposition", "Digit Weight"],
        "content": [
            "In the mathematical realm called the 'Land of Tens', every number can be assembled solely by combining powers of ten: $+1, +10, +100, +1000, +10000, +100000$.",
            "Suppose your screen begins at 0 and you wish to reach the number 3,425. You can achieve this by pressing: $[+1000]$ three times ($3,000$), $[+100]$ four times ($400$), $[+10]$ two times ($20$), and $[+1]$ five times ($5$). Total presses: $3 + 4 + 2 + 5 = 14$ clicks!",
            "Notice that the number of clicks required using this standard greedy method equals the sum of the digits of the number: for 3,425, the sum of digits is $3 + 4 + 2 + 5 = 14$.",
            "What if your calculator also has a 'Reset to 0' or 'Subtract' feature? If you want to reach 999, pressing $[+1000]$ once and $[-1]$ once takes only 2 clicks instead of pressing $[+100]$ nine times, $[+10]$ nine times, and $[+1]$ nine times (27 clicks)!"
        ],
        "fact_box": "To reach 1,00,000 from 0 using only the $[+10]$ button, you would need to press it exactly 10,000 times! But using the $[+100000]$ button takes just 1 press.",
        "checkpoints": [
            {
                "question": "Using only [+1000], [+100], [+10], and [+1] buttons from 0, what is the minimum number of presses to form 5,208?",
                "options": ["10 presses", "12 presses", "15 presses", "20 presses"],
                "correct": 2,
                "explanation": "5 presses of [+1000] + 2 presses of [+100] + 0 presses of [+10] + 8 presses of [+1] = $5 + 2 + 0 + 8 = 15$ presses."
            },
            {
                "question": "How many times must you press the [+100] button to reach exactly 10,000 from 0?",
                "options": ["10 times", "100 times", "1,000 times", "10,000 times"],
                "correct": 1,
                "explanation": "$10,000 \\div 100 = 100$ presses."
            }
        ]
    },

    # Slide 6: Of Crores and Crores!
    {
        "id": 6,
        "tag": "1.3 Of Crores and Crores! • Escalating Scales",
        "title": "Of Crores and Crores: Escalating to Cosmic Scales",
        "sim_id": "crores_and_arabs_sim",
        "avatar": {
            "name": "Prof. Shakuntala Devi",
            "title": "Human Computer & Master Mathematician"
        },
        "narration": "What lies beyond a lakh? Ten lakhs make one million, and one hundred lakhs create a mighty Crore! In ancient India, Sanskrit mathematicians charted numbers all the way to Arab, Kharab, and Shankha!",
        "key_terms": ["Ten Lakhs (10,00,000)", "One Crore (1,00,00,000)", "One Arab (100 Crores)", "Sanskrit Heritage", "Koṭi & Laksha"],
        "content": [
            "As we step beyond six digits, we enter the domain of Crores. When ten one-lakhs assemble, we obtain Ten Lakhs ($10,00,000 = 10^6$), which is a 7-digit number.",
            "When ten 'ten-lakhs' unite, we reach One Crore ($1,00,00,000 = 10^7$). A crore is an 8-digit number with 1 followed by 7 zeroes! One hundred crores is called One Arab ($1,00,00,00,000 = 10^9 = 1\\text{ Billion}$).",
            "Ancient Heritage: The word 'lakh' derives from the Sanskrit root *laksha* (लक्ष), meaning a mark, aim, or a stake of one hundred thousand. The word 'crore' originates from the Sanskrit *koṭi* (कोटि), signifying the highest point or ten million.",
            "India's ancient mathematical texts, including the *Yajurveda Samhita* and the *Lalitavistara Sutra*, describe powers of ten reaching up to $10^{53}$ (*tallakshana*), demonstrating ancient India's mastery of astronomical counting."
        ],
        "fact_box": "India's population is over 140 Crores ($1,40,00,00,000$). That means 1.4 Arab people share our vibrant nation!",
        "checkpoints": [
            {
                "question": "How many lakhs make exactly one crore?",
                "options": ["10 lakhs", "100 lakhs", "1,000 lakhs", "10,000 lakhs"],
                "correct": 1,
                "explanation": "$1\\text{ Crore} = 100\\text{ Lakhs} = 1,00,00,000$. There are 100 lakhs in one crore."
            },
            {
                "question": "How many zeroes are present in one crore ($1,00,00,000$)?",
                "options": ["5 zeroes", "6 zeroes", "7 zeroes", "8 zeroes"],
                "correct": 2,
                "explanation": "One crore is written as 1 followed by 7 zeroes ($10^7$)."
            }
        ]
    },

    # Slide 7: Indian vs. International Place Value Systems
    {
        "id": 7,
        "tag": "1.3 Of Crores and Crores! • Global Comparison",
        "title": "Indian vs. International Place Value System Converter",
        "sim_id": "indian_vs_international_sim",
        "avatar": {
            "name": "Prof. Shakuntala Devi",
            "title": "Human Computer & Master Mathematician"
        },
        "narration": "In India we count in Lakhs and Crores with 3-2-2 grouping; globally, the International system groups digits strictly in triads: 3-3-3 using Thousands, Millions, and Billions! Let's build a bridge between these two great systems!",
        "key_terms": ["Indian System (3:2:2)", "International System (3:3:3)", "Millions & Billions", "Conversion Table", "Comma Syntax"],
        "content": [
            "Around the world, two primary systems are used to group and read large numbers: the Indian Place Value System and the International Place Value System.",
            "Indian System: Commas group the first 3 digits from the right, and then every 2 digits ($3, 2, 2, 2$). The periods are: Ones, Thousands, Lakhs, Crores.",
            "International System: Commas group every 3 digits uniformly from the right ($3, 3, 3$). The periods are: Ones, Thousands, Millions, Billions.",
            "Equivalence Bridge: $100\\text{ Thousand} = 1\\text{ Lakh}$ ($1,00,000$). $1\\text{ Million} = 10\\text{ Lakhs}$ ($10,00,000$). $10\\text{ Million} = 1\\text{ Crore}$ ($1,00,00,000$). $1\\text{ Billion} = 100\\text{ Crores} = 1\\text{ Arab}$ ($1,000,000,000$)."
        ],
        "fact_box": "When global news reports a 'Billionaire', in Indian terminology that person has a net worth exceeding 100 Crores of rupees!",
        "checkpoints": [
            {
                "question": "How many millions are equal to 5 crores?",
                "options": ["5 millions", "50 millions", "500 millions", "5,000 millions"],
                "correct": 1,
                "explanation": "Since $1\\text{ Crore} = 10\\text{ Millions}$, therefore $5\\text{ Crores} = 5 \\times 10 = 50\\text{ Millions}$."
            },
            {
                "question": "How is 25 million written in the Indian place value system?",
                "options": ["25,00,000", "2,50,00,000", "250,00,000", "2,500,000"],
                "correct": 1,
                "explanation": "25 million is $25,000,000$. In the Indian system, grouping from right gives $2,50,00,000$ (Two crore fifty lakhs)."
            }
        ]
    },

    # Slide 8: Exact and Approximate Values in Daily Life
    {
        "id": 8,
        "tag": "1.4 Exact and Approximate Values • Practical Wisdom",
        "title": "Exact vs. Approximate Values: When Do We Estimate?",
        "sim_id": "exact_vs_approx_sim",
        "avatar": {
            "name": "Prof. Shakuntala Devi",
            "title": "Human Computer & Master Mathematician"
        },
        "narration": "In real life, do we always need the exact digit, or is an approximation better? If you ask the population of Delhi, 'about 3 crore' is far more useful than saying 3,29,41,308! Let's learn when to estimate and when to be exact!",
        "key_terms": ["Exact Value", "Approximation", "Estimation", "Practical Utility", "Census vs Transactions"],
        "content": [
            "Mathematics is famous for precision, but practical intelligence requires knowing when exactness is essential and when estimation is superior.",
            "When Exact Values are Essential: Banking transactions, medicine dosages, flight boarding counts, exam scores, and rocket trajectories require exact numbers down to the last decimal digit.",
            "When Approximations are Preferred: Describing national populations, distances between towns, crowd sizes at festivals, and estimating wedding catering quantities.",
            "Why do we estimate? (1) Large quantities fluctuate constantly—births and deaths change a city's population every second; (2) Rounded numbers are far easier to remember, compare, and mentally compute."
        ],
        "fact_box": "If the newspaper printed the exact population of India as 1,42,86,27,663 at 9:00 AM, that number would already be inaccurate by 9:01 AM due to new births!",
        "checkpoints": [
            {
                "question": "In which of the following scenarios is an EXACT number strictly required?",
                "options": ["Crowd size at a football match", "Amount of money deposited in a bank account", "Number of stars in the Milky Way", "Distance between Chennai and Delhi"],
                "correct": 1,
                "explanation": "Banking balances must be exact down to the paisa; rounding off bank accounts would cause severe financial errors."
            },
            {
                "question": "Why are city population counts in newspapers typically reported as approximations?",
                "options": ["Reporters cannot count", "Populations change continuously every minute", "Calculators cannot display large numbers", "Exact numbers are forbidden by law"],
                "correct": 1,
                "explanation": "Continuous births, deaths, and migration mean a city's exact head count changes every minute."
            }
        ]
    },

    # Slide 9: Nearest Neighbours (Rounding Rules)
    {
        "id": 9,
        "tag": "1.4 Exact and Approximate Values • Rounding Rules",
        "title": "Nearest Neighbours: Rounding Off to Tens, Thousands & Lakhs",
        "sim_id": "nearest_neighbours_rounding_sim",
        "avatar": {
            "name": "Prof. Shakuntala Devi",
            "title": "Human Computer & Master Mathematician"
        },
        "narration": "Rounding off is simply finding the nearest landmark neighbor on a number line! If your digit is 5 or greater, round up to the next landmark; if it's less than 5, round down! Let's explore the number line!",
        "key_terms": ["Rounding Off", "Nearest Landmark", "Halfway Rule (5)", "Round Up vs Round Down", "Number Line Distance"],
        "content": [
            "Rounding off means replacing a number with an approximate value that is simpler, shorter, and close to the original number.",
            "The Halfway Rule: Look at the digit immediately to the right of your target rounding place. If that digit is $0, 1, 2, 3,$ or $4$, round down (keep target digit unchanged). If that digit is $5, 6, 7, 8,$ or $9$, round up (increase target digit by 1).",
            "Rounding to Nearest Thousand: Take 47,825. The digit in the hundreds place is 8 (which is $\\ge 5$). The nearest thousands are 47,000 and 48,000. Because 47,825 is closer to 48,000, it rounds UP to 48,000.",
            "Rounding to Nearest Lakh: Take 3,42,900. The ten-thousands digit is 4 ($< 5$). The nearest lakhs are 3,00,000 and 4,00,000. It is closer to 3,00,000, so it rounds DOWN to 3,00,000."
        ],
        "fact_box": "The number 75,000 is exactly halfway between 70,000 and 80,000. By mathematical convention worldwide, halfway numbers with 5 are rounded UP to 80,000.",
        "checkpoints": [
            {
                "question": "What is 8,64,320 rounded to the nearest lakh?",
                "options": ["8,00,000", "8,60,000", "9,00,000", "8,70,000"],
                "correct": 2,
                "explanation": "The ten-thousands digit is 6 (which is $\\ge 5$), so 8,64,320 rounds up to 9,00,000."
            },
            {
                "question": "What is 74,499 rounded to the nearest thousand?",
                "options": ["74,000", "74,500", "75,000", "70,000"],
                "correct": 0,
                "explanation": "Looking at the hundreds digit (4), since $4 < 5$, we round down to 74,000."
            }
        ]
    },

    # Slide 10: Populations of Indian Cities (Data Table Analysis)
    {
        "id": 10,
        "tag": "1.4 Populations of Cities • Census Data",
        "title": "Populations of Indian Cities: 2001 vs. 2011 Census",
        "sim_id": "city_populations_data_sim",
        "avatar": {
            "name": "Prof. Shakuntala Devi",
            "title": "Human Computer & Master Mathematician"
        },
        "narration": "Let's examine official Census data from our great Indian cities! Comparing 2001 and 2011 figures for Mumbai, Delhi, and Bengaluru reveals astounding population surges of tens of lakhs of people!",
        "key_terms": ["Census Data", "Intercensal Growth", "City Population Table", "Difference Calculation", "Urbanization Scale"],
        "content": [
            "Every ten years, the Government of India conducts a nationwide Census, counting every household to plan schools, hospitals, water supplies, and transport.",
            "Census Data Table Analysis:\n• Mumbai: $1,19,78,450$ (2001) grew to $1,24,42,373$ (2011) — an increase of $4,63,923$ citizens.\n• Delhi: $98,17,439$ (2001) surged to $1,10,34,555$ (2011) — jumping by $12,17,116$ people (crossing the 1-crore milestone!).\n• Bengaluru: $43,01,326$ (2001) exploded to $84,43,675$ (2011) — nearly doubling with an increase of $41,42,349$!",
            "Ordering Cities by Size: In 2011, Mumbai ($1.24\\text{ Crore}$) > Delhi ($1.10\\text{ Crore}$) > Bengaluru ($84.4\\text{ Lakhs}$).",
            "Rounding for Media Headlines: Mumbai has 'about 1.25 Crore', Delhi has 'about 1.1 Crore', and Bengaluru has 'about 84 Lakh' residents."
        ],
        "fact_box": "Bengaluru's population grew by over 41 Lakh people in a single decade (2001–2011)—adding roughly 4 Lakh new residents every year!",
        "checkpoints": [
            {
                "question": "Which city crossed the 1-crore (1,00,00,000) population mark between 2001 and 2011?",
                "options": ["Bengaluru", "Delhi", "Kolkata", "Hyderabad"],
                "correct": 1,
                "explanation": "Delhi grew from 98,17,439 (less than 1 crore) in 2001 to 1,10,34,555 (over 1 crore) in 2011."
            },
            {
                "question": "What was the approximate increase in Bengaluru's population between 2001 (43 Lakhs) and 2011 (84 Lakhs)?",
                "options": ["About 21 Lakhs", "About 31 Lakhs", "About 41 Lakhs", "About 51 Lakhs"],
                "correct": 2,
                "explanation": "$84\\text{ Lakhs} - 43\\text{ Lakhs} = 41\\text{ Lakhs}$ increase."
            }
        ]
    },

    # Slide 11: Patterns in Products (Multiplying by 5, 25, 50)
    {
        "id": 11,
        "tag": "1.5 Patterns in Products • Mental Math Shortcuts",
        "title": "Patterns in Products: Multiplying by 5, 25, and 50",
        "sim_id": "multiply_by_five_shortcut_sim",
        "avatar": {
            "name": "Prof. Shakuntala Devi",
            "title": "Human Computer & Master Mathematician"
        },
        "narration": "Here is one of my favorite mental arithmetic secrets! Why multiply by 5 when division by 2 is so much easier? Since $5 = 10 \\div 2$, just cut the number in half and append a zero! Let's master lightning multiplication!",
        "key_terms": ["Mental Math Shortcut", "Multiply by 5", "Divide by 2 & Multiply by 10", "Multiply by 25", "Multiply by 50"],
        "content": [
            "Mathematicians look for patterns to transform cumbersome arithmetic into effortless mental calculations. Multiplying by 5 is a prime example.",
            "The Multiply-by-5 Rule: Notice that $5 = \\frac{10}{2}$. Therefore: $N \\times 5 = \\frac{N}{2} \\times 10 = (N \\div 2) \\times 10$.\nTo multiply any number by 5, halve the number and append a zero (or shift the decimal one place right)!",
            "Example 1: $48 \\times 5 = (48 \\div 2) \\times 10 = 24 \\times 10 = 240$.\nExample 2: $164 \\times 5 = (164 \\div 2) \\times 10 = 82 \\times 10 = 820$.\nExample 3: $73 \\times 5 = (73 \\div 2) \\times 10 = 36.5 \\times 10 = 365$.",
            "The Multiply-by-25 Rule: Since $25 = \\frac{100}{4}$, divide by 4 and multiply by 100! E.g., $64 \\times 25 = (64 \\div 4) \\times 100 = 16 \\times 100 = 1,600$!\nThe Multiply-by-50 Rule: Since $50 = \\frac{100}{2}$, halve the number and multiply by 100! E.g., $86 \\times 50 = 43 \\times 100 = 4,300$!"
        ],
        "fact_box": "You can multiply by 125 using the same logic! Since $125 = \\frac{1,000}{8}$, divide by 8 and multiply by 1,000. For example: $72 \\times 125 = (72 \\div 8) \\times 1000 = 9,000$!",
        "checkpoints": [
            {
                "question": "Using the shortcut $(N \\div 2) \\times 10$, what is $84 \\times 5$?",
                "options": ["410", "420", "430", "440"],
                "correct": 1,
                "explanation": "Half of 84 is 42. Multiplying by 10 gives $42 \\times 10 = 420$."
            },
            {
                "question": "Calculate $36 \\times 25$ using the shortcut $(N \\div 4) \\times 100$:",
                "options": ["800", "900", "1,000", "950"],
                "correct": 1,
                "explanation": "$36 \\div 4 = 9$. Then $9 \\times 100 = 900$."
            }
        ]
    },

    # Slide 12: A Multiplication Shortcut (Grouped Factorisation)
    {
        "id": 12,
        "tag": "1.5 Patterns in Products • Grouped Factorisation",
        "title": "A Multiplication Shortcut: Grouped Factorisation",
        "sim_id": "grouped_factorisation_sim",
        "avatar": {
            "name": "Prof. Shakuntala Devi",
            "title": "Human Computer & Master Mathematician"
        },
        "narration": "When two tricky numbers collide in multiplication, don't rush into long columns! Break them into friendly factors, pair up a 2 and a 5 to make a 10, and watch the answer appear like magic!",
        "key_terms": ["Factorisation", "Associative Property", "Pairing (2 x 5 = 10)", "Mental Grouping", "Friendly Multipliers"],
        "content": [
            "The Associative and Commutative properties of multiplication state that $(a \\times b) \\times c = a \\times (b \\times c)$ and $a \\times b = b \\times a$. We can reorder and regroup factors in any convenient sequence.",
            "Strategic Secret: Whenever you see an even number multiplied by a number ending in 5, pull out factor 2 and factor 5 to create a friendly multiple of 10!",
            "Worked Example 1: Calculate $18 \\times 35$.\n• Step 1: Factorize $18 = 9 \\times 2$ and $35 = 5 \\times 7$.\n• Step 2: Regroup: $(9 \\times 7) \\times (2 \\times 5)$.\n• Step 3: Compute: $63 \\times 10 = 630$! Done mentally in two seconds!",
            "Worked Example 2: Calculate $24 \\times 75$.\n• Step 1: Factorize $24 = 6 \\times 4$ and $75 = 25 \\times 3$.\n• Step 2: Regroup: $(6 \\times 3) \\times (4 \\times 25) = 18 \\times 100 = 1,800$!"
        ],
        "fact_box": "This technique was celebrated by ancient Indian astronomers who simplified complex planetary motion products by regrouping factors mentally before writing down the final result.",
        "checkpoints": [
            {
                "question": "Using grouped factorisation, calculate $16 \\times 45$ by pairing $(2 \\times 5)$:",
                "options": ["620", "720", "820", "920"],
                "correct": 1,
                "explanation": "$16 \\times 45 = (8 \\times 2) \\times (5 \\times 9) = (8 \\times 9) \\times (2 \\times 5) = 72 \\times 10 = 720$."
            },
            {
                "question": "How can $28 \\times 25$ be simplified most effectively?",
                "options": ["$(28 \\times 20) + (28 \\times 5)$", "$(7 \\times 4) \\times 25 = 7 \\times (4 \\times 25) = 7 \\times 100 = 700$", "Long column multiplication with 4 steps", "Adding 28 twenty-five times"],
                "correct": 1,
                "explanation": "Factoring 28 as $7 \\times 4$ gives $7 \\times (4 \\times 25) = 7 \\times 100 = 700$."
            }
        ]
    },

    # Slide 13: How Long is the Product? (Digit Length Invariants)
    {
        "id": 13,
        "tag": "1.5 How Long is the Product? • Number Theory",
        "title": "How Long is the Product? Predicting Digit Lengths",
        "sim_id": "how_long_is_product_sim",
        "avatar": {
            "name": "Prof. Shakuntala Devi",
            "title": "Human Computer & Master Mathematician"
        },
        "narration": "If you multiply a 3-digit number by a 4-digit number, how many digits can the product have? 6 or 7? Can it ever have 8 digits? Let's uncover the elegant mathematical rule that bounds the length of every product!",
        "key_terms": ["Digit Length Rule", "Minimum Digits (m + n - 1)", "Maximum Digits (m + n)", "Bounds", "Product Invariant"],
        "content": [
            "Before performing an extensive multiplication, skilled mathematicians predict the exact digit length of the answer to guard against calculation errors.",
            "The Fundamental Product Length Theorem: If an $m$-digit number is multiplied by an $n$-digit number, the product will have EITHER $(m + n - 1)$ digits OR $(m + n)$ digits. It can NEVER have fewer or more!",
            "Why is this always true? Consider the smallest and largest possible numbers:\n• Smallest 2-digit $\\times$ smallest 3-digit: $10 \\times 100 = 1,000$ (a 4-digit number, which is $2 + 3 - 1 = 4$ digits).\n• Largest 2-digit $\\times$ largest 3-digit: $99 \\times 999 = 98,901$ (a 5-digit number, which is $2 + 3 = 5$ digits).",
            "General Rule: Multiplying a 3-digit number by a 4-digit number ($m=3, n=4$) produces an answer with either $3 + 4 - 1 = 6$ digits, or $3 + 4 = 7$ digits!"
        ],
        "fact_box": "If you multiply two 5-digit numbers together, the product will always contain either 9 or 10 digits. It will NEVER contain 8 or 11 digits!",
        "checkpoints": [
            {
                "question": "What are the possible number of digits when a 2-digit number is multiplied by a 4-digit number?",
                "options": ["4 or 5 digits", "5 or 6 digits", "6 or 7 digits", "7 or 8 digits"],
                "correct": 1,
                "explanation": "Here $m=2$ and $n=4$. The possible digit counts are $m+n-1 = 2+4-1 = 5$ or $m+n = 2+4 = 6$ digits."
            },
            {
                "question": "Can multiplying a 3-digit number by a 3-digit number ever produce an 8-digit answer?",
                "options": ["Yes, if both numbers are greater than 900", "Yes, if both numbers are prime", "No, maximum possible is $3+3=6$ digits", "No, maximum possible is 7 digits"],
                "correct": 2,
                "explanation": "For two 3-digit numbers ($m=3, n=3$), the maximum possible digits is $m+n = 3+3=6$ digits ($999 \\times 999 = 998,001$)."
            }
        ]
    },

    # Slide 14: Fascinating Facts about Large Numbers
    {
        "id": 14,
        "tag": "1.5 Fascinating Facts • Calculations in Nature & History",
        "title": "Fascinating Facts: Calculations in History & Cosmos",
        "sim_id": "large_numbers_trivia_sim",
        "avatar": {
            "name": "Prof. Shakuntala Devi",
            "title": "Human Computer & Master Mathematician"
        },
        "narration": "Large numbers tell breathtaking stories! From the legendary Saint Purandaradāsa's 4.75 lakh kirtanas to the colossal Amazon river discharging 2 lakh cubic metres of water every second—let's do the math!",
        "key_terms": ["Historical Calculations", "Purandaradāsa's Kirtanas", "Amazon River Discharge", "Distance to Sun (15 Crore km)", "Speed of Light"],
        "content": [
            "Purandaradāsa's Musical Marvel: Historical tradition celebrates Karnataka Saint Purandaradāsa for composing 4,75,000 (four lakh seventy-five thousand) devotional kirtanas. If a singer performs 10 kirtanas every day, it would take $4,75,000 \\div 10 = 47,500$ days—over 130 years of non-stop daily singing!",
            "The Amazon River Discharge: The Amazon River in South America pours roughly 2,00,000 cubic metres ($2,00,000\\text{ m}^3$) of fresh water into the Atlantic Ocean every single second! In one minute ($60\\text{ seconds}$), that is $2,00,000 \\times 60 = 1,20,00,000\\text{ m}^3$ (one crore twenty lakh cubic metres)!",
            "Distance to the Sun: The average distance from Earth to the Sun is approximately $14,96,00,000\\text{ km}$ (about 15 Crore kilometres).",
            "Sunlight Travel Time: Light travels at an incredible speed of $3,00,000\\text{ km/second}$. To reach Earth, sunlight takes: $\\frac{15,00,00,000\\text{ km}}{3,00,000\\text{ km/s}} = 500\\text{ seconds} = 8\\text{ minutes and } 20\\text{ seconds}$!"
        ],
        "fact_box": "In a single second, light can travel around the entire Earth's equator ($40,075\\text{ km}$) more than 7.5 times!",
        "checkpoints": [
            {
                "question": "If the Amazon river discharges 2,00,000 m³ of water per second, how much does it discharge in 10 seconds?",
                "options": ["20,000 m³", "2,00,000 m³", "20,00,000 m³ (20 Lakhs)", "2,00,00,000 m³ (2 Crores)"],
                "correct": 2,
                "explanation": "$2,00,000 \\times 10 = 20,00,000\\text{ m}^3$ (Twenty Lakh cubic metres)."
            },
            {
                "question": "Light travels at 3,00,000 km/s. How far does light travel in 5 seconds?",
                "options": ["1,50,000 km", "15,00,000 km (15 Lakhs)", "1,50,00,000 km", "15,000 km"],
                "correct": 1,
                "explanation": "$3,00,000 \\times 5 = 15,00,000\\text{ km}$ (Fifteen Lakh kilometres)."
            }
        ]
    },

    # Slide 15: Thought Experiment: Fitting Mumbai's Population
    {
        "id": 15,
        "tag": "1.6 Did You Ever Wonder...? • Urban Thought Experiment",
        "title": "Thought Experiment: Fitting Mumbai's Population into Buses & Ships",
        "sim_id": "mumbai_population_buses_sim",
        "avatar": {
            "name": "Prof. Shakuntala Devi",
            "title": "Human Computer & Master Mathematician"
        },
        "narration": "Have you ever wondered what happens if we try to fit Mumbai's entire population of 1.25 Crore people into double-decker buses or giant cruise ships? Let's compute the fleet sizes needed for this mind-boggling thought experiment!",
        "key_terms": ["Thought Experiment", "Fleet Estimation", "Double-Decker Bus (80 pax)", "Cruise Liner (3,000 pax)", "Logistical Scale"],
        "content": [
            "Thought experiments allow mathematicians to test the physical meaning of giant numbers through vivid hypothetical scenarios.",
            "Scenario: Suppose Mumbai's population is approximately $1,25,00,000$ (One Crore Twenty-Five Lakhs).",
            "Problem A: How many standard double-decker buses (each seating 80 passengers) would be needed to carry all of Mumbai at once?\n• Calculation: $\\frac{1,25,00,000}{80} = 1,56,250\\text{ buses}$!\n• If each bus is 10 metres long with a 2-metre gap between them (12 metres total), a convoy of 1,56,250 buses bumper-to-bumper would stretch $1,56,250 \\times 12\\text{ m} = 18,75,000\\text{ metres} = 1,875\\text{ km}$—stretching from Mumbai all the way past Delhi to the Himalayas!",
            "Problem B: What if we used mega cruise liners holding 3,000 passengers each?\n• Calculation: $\\frac{1,25,00,000}{3,000} \\approx 4,167\\text{ giant ships}$! That is more cruise liners than exist on the entire planet Earth!"
        ],
        "fact_box": "Mumbai's suburban local train network carries over 75,00,000 (75 Lakh) commuters every single day—more than the entire population of many countries like New Zealand or Norway!",
        "checkpoints": [
            {
                "question": "If each bus holds 50 students, how many buses are needed to transport 1,00,000 (one lakh) students?",
                "options": ["200 buses", "2,000 buses", "20,000 buses", "5,000 buses"],
                "correct": 1,
                "explanation": "$1,00,000 \\div 50 = 2,000$ buses."
            },
            {
                "question": "If a stadium holds 50,000 people, how many such stadiums are needed to seat 1 Crore (1,00,00,000) people?",
                "options": ["20 stadiums", "50 stadiums", "200 stadiums", "2,000 stadiums"],
                "correct": 2,
                "explanation": "$1,00,00,000 \\div 50,000 = 200$ stadiums."
            }
        ]
    },

    # Slide 16: Thought Experiment: Journey to the Moon and Sun
    {
        "id": 16,
        "tag": "1.6 Did You Ever Wonder...? • Cosmic Travel Times",
        "title": "Thought Experiment: Journey to the Moon and Sun at Different Speeds",
        "sim_id": "journey_to_sun_moon_sim",
        "avatar": {
            "name": "Prof. Shakuntala Devi",
            "title": "Human Computer & Master Mathematician"
        },
        "narration": "How long would it take to walk to the Moon? Or drive a car to the Sun? Let's use our formula $\\text{Time} = \\text{Distance} \\div \\text{Speed}$ to calculate travel times across the solar system!",
        "key_terms": ["Time = Distance ÷ Speed", "Lunar Distance (3,84,400 km)", "Solar Distance (15 Crore km)", "Walking vs Rocket Speeds", "Scale of the Cosmos"],
        "content": [
            "The distance to the Moon is $3,84,400\\text{ km}$ (about 3.84 Lakh km). The distance to the Sun is $15,00,00,000\\text{ km}$ (15 Crore km).",
            "Journey to the Moon ($3,84,400\\text{ km}$):\n• Walking non-stop at $5\\text{ km/h}$: $\\frac{3,84,400}{5} = 76,880\\text{ hours} \\approx 3,203\\text{ days} \\approx 8.8\\text{ years}$!\n• High-speed train at $200\\text{ km/h}$: $\\frac{3,84,400}{200} = 1,922\\text{ hours} \\approx 80\\text{ days}$!\n• Apollo Rocket at $11\\text{ km/s}$ ($39,600\\text{ km/h}$): About 3 days!",
            "Journey to the Sun ($15,00,00,000\\text{ km}$):\n• Commercial Jet at $1,000\\text{ km/h}$: $\\frac{15,00,00,000}{1,000} = 1,50,000\\text{ hours} \\approx 6,250\\text{ days} \\approx 17.1\\text{ years}$!\n• Walking at $5\\text{ km/h}$: $3,00,00,000\\text{ hours} \\approx 3,425\\text{ years}$—longer than recorded human history since the Bronze Age!",
            "These astounding numbers demonstrate the profound grandeur of the universe and why large numbers are the language of astronomy."
        ],
        "fact_box": "India's Chandrayaan-3 took approximately 40 days to reach the Moon using a fuel-efficient gravitational slingshot trajectory!",
        "checkpoints": [
            {
                "question": "If an airplane flies at 1,000 km/h, how many hours will it take to cover 10,00,000 km (ten lakh km)?",
                "options": ["100 hours", "1,000 hours", "10,000 hours", "100,000 hours"],
                "correct": 1,
                "explanation": "$\\text{Time} = \\frac{10,00,000\\text{ km}}{1,000\\text{ km/h}} = 1,000\\text{ hours}$."
            },
            {
                "question": "At a speed of 100 km/h, how long would a car take to cover 3,00,000 km?",
                "options": ["300 hours", "3,000 hours", "30,000 hours", "300,000 hours"],
                "correct": 1,
                "explanation": "$\\text{Time} = \\frac{3,00,000\\text{ km}}{100\\text{ km/h}} = 3,000\\text{ hours}$."
            }
        ]
    },

    # Slide 17: Mastery Challenge Part I (Q1 - Q10)
    {
        "id": 17,
        "is_quiz": True,
        "quiz_range": (1, 10),
        "tag": "Chapter Review • Mastery Challenge Part I",
        "title": "Mastery Challenge: Place Value, Lakhs & Land of Tens",
        "avatar": {
            "name": "Prof. Shakuntala Devi",
            "title": "Human Computer & Master Mathematician"
        },
        "narration": "Time for our Mastery Challenge Part I! Test your skills on place value charts, comma conventions, and the Land of Tens button puzzles. Click on the solution button anytime to review the step-by-step mathematical reasoning!",
    },

    # Slide 18: Mastery Challenge Part II (Q11 - Q20)
    {
        "id": 18,
        "is_quiz": True,
        "quiz_range": (11, 20),
        "tag": "Chapter Review • Mastery Challenge Part II",
        "title": "Mastery Challenge: Crores, Arabs & Global Systems",
        "avatar": {
            "name": "Prof. Shakuntala Devi",
            "title": "Human Computer & Master Mathematician"
        },
        "narration": "Mastery Challenge Part II! Here we compare the Indian and International systems, convert Millions to Lakhs, and explore ancient Sanskrit magnitudes. Think carefully and solve with confidence!",
    },

    # Slide 19: Mastery Challenge Part III (Q21 - Q30)
    {
        "id": 19,
        "is_quiz": True,
        "quiz_range": (21, 30),
        "tag": "Chapter Review • Mastery Challenge Part III",
        "title": "Mastery Challenge: Rounding, Nearest Neighbours & Data",
        "avatar": {
            "name": "Prof. Shakuntala Devi",
            "title": "Human Computer & Master Mathematician"
        },
        "narration": "Mastery Challenge Part III! Put your estimation, rounding-off, and Census data analysis skills to the test. Remember the halfway rule on the number line!",
    },

    # Slide 20: Mastery Challenge Part IV (Q31 - Q40)
    {
        "id": 20,
        "is_quiz": True,
        "quiz_range": (31, 40),
        "tag": "Chapter Review • Mastery Challenge Part IV",
        "title": "Mastery Challenge: Product Patterns & Thought Experiments",
        "avatar": {
            "name": "Prof. Shakuntala Devi",
            "title": "Human Computer & Master Mathematician"
        },
        "narration": "The final frontier! Mastery Challenge Part IV tests your mental multiplication shortcuts, product digit lengths, and cosmic travel thought experiments. Complete all 10 questions to earn your Master Mathematician Certificate!",
    }
]


QUIZ_QUESTIONS = [
    # Q1
    {
        "id": 1,
        "question": "How many digits are there in the standard numeral for One Lakh?",
        "options": ["5 digits", "6 digits", "7 digits", "8 digits"],
        "correct": 1,
        "solution": "Step 1: Write out one lakh in figures: 1,00,000.\nStep 2: Count the digits: one digit '1' followed by five zeroes '00000'.\nStep 3: Total number of digits = 1 + 5 = 6 digits.\nTherefore, One Lakh is the smallest 6-digit number."
    },
    # Q2
    {
        "id": 2,
        "question": "What number is obtained by adding 1 to the largest 5-digit number (99,999)?",
        "options": ["10,000", "99,990", "1,00,000 (One Lakh)", "10,00,000 (Ten Lakhs)"],
        "correct": 2,
        "solution": "Step 1: The largest 5-digit number is 99,999.\nStep 2: Add 1: $99,999 + 1 = 1,00,000$.\nStep 3: This yields exactly 1,00,000, known as One Lakh (the smallest 6-digit number)."
    },
    # Q3
    {
        "id": 3,
        "question": "Which of the following numbers shows correct comma placement according to the Indian place value system for 784321?",
        "options": ["784,321", "7,84,321", "78,43,21", "7,8,4,3,2,1"],
        "correct": 1,
        "solution": "Step 1: In the Indian place value system, the first comma is placed after 3 digits from the right (hundreds period).\nStep 2: Subsequent commas are placed after every 2 digits (thousands period, lakhs period).\nStep 3: For 784321, from right to left: '321', then comma, then '84', then comma, then '7'.\nResult: 7,84,321 (Seven lakh eighty-four thousand three hundred twenty-one)."
    },
    # Q4
    {
        "id": 4,
        "question": "What is the expanded form of the number 3,50,420?",
        "options": [
            "3 × 1,00,000 + 5 × 10,000 + 4 × 100 + 2 × 10",
            "3 × 10,000 + 5 × 1,000 + 4 × 100 + 2 × 10",
            "3 × 1,00,000 + 5 × 1,000 + 4 × 100 + 2 × 1",
            "35 × 10,000 + 42 × 10"
        ],
        "correct": 0,
        "solution": "Step 1: Identify place values for each digit in 3,50,420:\n• 3 in Lakhs place = $3 \\times 1,00,000$\n• 5 in Ten-thousands place = $5 \\times 10,000$\n• 0 in Thousands place = 0\n• 4 in Hundreds place = $4 \\times 100$\n• 2 in Tens place = $2 \\times 10$\n• 0 in Ones place = 0.\nStep 2: Combine non-zero terms: $3 \\times 1,00,000 + 5 \\times 10,000 + 4 \\times 100 + 2 \\times 10$."
    },
    # Q5
    {
        "id": 5,
        "question": "In the 'Land of Tens' calculator with only [+1000], [+100], [+10], and [+1] buttons, how many total clicks are needed to make 4,312 from 0?",
        "options": ["8 clicks", "9 clicks", "10 clicks", "12 clicks"],
        "correct": 2,
        "solution": "Step 1: Decompose 4,312 into component powers of ten:\n• 4 thousands = 4 clicks of [+1000]\n• 3 hundreds = 3 clicks of [+100]\n• 1 ten = 1 click of [+10]\n• 2 ones = 2 clicks of [+1]\nStep 2: Sum the clicks: $4 + 3 + 1 + 2 = 10$ clicks."
    },
    # Q6
    {
        "id": 6,
        "question": "How many times must you press a [+1000] button to reach exactly 1,00,000 (one lakh)?",
        "options": ["10 times", "100 times", "1,000 times", "10,000 times"],
        "correct": 1,
        "solution": "Step 1: Divide the target amount by the increment value: $1,00,000 \\div 1,000$.\nStep 2: Simplify: $\\frac{1,00,000}{1,000} = 100$.\nStep 3: Exactly 100 presses of the [+1000] button are required."
    },
    # Q7
    {
        "id": 7,
        "question": "Which ancient Sanskrit word is the linguistic ancestor of our modern Indian word 'lakh'?",
        "options": ["Koti", "Laksha", "Shankha", "Ayuta"],
        "correct": 1,
        "solution": "Step 1: 'Lakh' originates from the classical Sanskrit noun *laksha* (लक्ष), meaning a mark, objective, or one hundred thousand.\nStep 2: *Koti* (कोटि) corresponds to modern 'crore' (ten million)."
    },
    # Q8
    {
        "id": 8,
        "question": "How many days are there in 50 non-leap years ($365 \\times 50$)?",
        "options": ["18,250 days", "1,825 days", "1,82,500 days", "36,500 days"],
        "correct": 0,
        "solution": "Step 1: Multiply: $365 \\times 50$.\nStep 2: Use shortcut: $365 \\times 50 = \\frac{365 \\times 100}{2} = \\frac{36,500}{2} = 18,250$ days.\nStep 3: This confirms that 50 years contains approximately 18,250 days—far less than one lakh days!"
    },
    # Q9
    {
        "id": 9,
        "question": "What is the height of the Statue of Unity in Gujarat?",
        "options": ["93 metres", "180 metres", "450 metres", "828 metres"],
        "correct": 1,
        "solution": "Step 1: The Statue of Unity stands 180 metres tall (or 182 metres to the crown), standing as the world's tallest statue.\nStep 2: In our reference scale, it equals 180 one-metre tall persons stacked head-to-toe."
    },
    # Q10
    {
        "id": 10,
        "question": "If you read the number 5,08,012 aloud in words, what is the correct reading?",
        "options": [
            "Fifty-eight thousand twelve",
            "Five lakh eight thousand twelve",
            "Five lakh eighty thousand twelve",
            "Fifty lakh eight hundred twelve"
        ],
        "correct": 1,
        "solution": "Step 1: Look at the periods of 5,08,012:\n• Lakhs period: 5 = 'Five lakh'\n• Thousands period: 08 = 'eight thousand'\n• Ones period: 012 = 'twelve'\nStep 2: Combine: 'Five lakh eight thousand twelve'."
    },

    # Q11
    {
        "id": 11,
        "question": "How many zeroes are there in One Crore ($1,00,00,000$)?",
        "options": ["5 zeroes", "6 zeroes", "7 zeroes", "8 zeroes"],
        "correct": 2,
        "solution": "Step 1: Write one crore in Indian notation: 1,00,00,000.\nStep 2: Count zeroes from right: 3 in ones period + 2 in thousands period + 2 in lakhs period = 7 zeroes.\nStep 3: $1\\text{ Crore} = 10^7$, which has exactly 7 zeroes."
    },
    # Q12
    {
        "id": 12,
        "question": "One Crore is equal to how many Lakhs?",
        "options": ["10 Lakhs", "100 Lakhs", "1,000 Lakhs", "10,000 Lakhs"],
        "correct": 1,
        "solution": "Step 1: $1\\text{ Crore} = 1,00,00,000$.\nStep 2: $1\\text{ Lakh} = 1,00,000$.\nStep 3: $\\frac{1,00,00,000}{1,00,000} = 100$.\nTherefore, 1 Crore = 100 Lakhs."
    },
    # Q13
    {
        "id": 13,
        "question": "In the International place value system, how is the number 1 Crore ($1,00,00,000$) written and named?",
        "options": ["10,000,000 (10 Million)", "1,000,000 (1 Million)", "100,000,000 (100 Million)", "1,000,000,000 (1 Billion)"],
        "correct": 0,
        "solution": "Step 1: Take 1,00,00,000.\nStep 2: Regroup with commas every 3 digits from the right: 10,000,000.\nStep 3: The thousands period is '000' and millions period is '10'.\nResult: 10 Million."
    },
    # Q14
    {
        "id": 14,
        "question": "How many Lakhs are equal to 1 Million?",
        "options": ["1 Lakh", "10 Lakhs", "100 Lakhs", "1,000 Lakhs"],
        "correct": 1,
        "solution": "Step 1: $1\\text{ Million} = 1,000,000$.\nStep 2: In Indian place value notation: $10,00,000$.\nStep 3: $10,00,000 = 10\\text{ Lakhs}$. Thus, 1 Million = 10 Lakhs."
    },
    # Q15
    {
        "id": 15,
        "question": "What is the Indian system equivalent of 1 Billion ($1,000,000,000$)?",
        "options": ["10 Crores", "100 Crores (1 Arab)", "1,000 Crores", "10 Lakhs"],
        "correct": 1,
        "solution": "Step 1: 1 Billion has 9 zeroes ($10^9 = 1,000,000,000$).\nStep 2: In the Indian system, $1\\text{ Crore} = 10^7$ (7 zeroes).\nStep 3: $10^9 \\div 10^7 = 10^2 = 100$ Crores, which is called One Arab."
    },
    # Q16
    {
        "id": 16,
        "question": "The Sanskrit word 'Koti' refers to which magnitude in the Indian numbering system?",
        "options": ["One Thousand", "One Lakh", "One Crore (Ten Million)", "One Arab"],
        "correct": 2,
        "solution": "Step 1: In classical Sanskrit literature (such as the *Mahabharata* and astronomical treatises), *koṭi* represents the number $10^7$, which is One Crore."
    },
    # Q17
    {
        "id": 17,
        "question": "How should the number 45879320 be punctuated with commas in the International place value system?",
        "options": ["4,58,79,320", "45,879,320", "458,79,320", "4,5,8,7,9,3,2,0"],
        "correct": 1,
        "solution": "Step 1: In the International system, group in triads (groups of 3) from right to left.\nStep 2: Last three digits: 320 -> ',320'. Next three digits: 879 -> ',879'. Remaining digits: 45.\nResult: 45,879,320 (Forty-five million eight hundred seventy-nine thousand three hundred twenty)."
    },
    # Q18
    {
        "id": 18,
        "question": "How many Ten-Thousands make 1 Lakh?",
        "options": ["5", "10", "100", "1,000"],
        "correct": 1,
        "solution": "Step 1: $1\\text{ Lakh} = 1,00,000$.\nStep 2: $1\\text{ Ten-Thousand} = 10,000$.\nStep 3: $\\frac{1,00,00,000}{10,000} = 10$. Exactly 10 ten-thousands make 1 lakh."
    },
    # Q19
    {
        "id": 19,
        "question": "What is the value of 1 Arab in terms of Lakhs?",
        "options": ["1,000 Lakhs", "10,000 Lakhs", "1,00,000 Lakhs", "10,00,000 Lakhs"],
        "correct": 1,
        "solution": "Step 1: $1\\text{ Arab} = 100\\text{ Crores}$.\nStep 2: Since $1\\text{ Crore} = 100\\text{ Lakhs}$, therefore $100\\text{ Crores} = 100 \\times 100 = 10,000\\text{ Lakhs}$."
    },
    # Q20
    {
        "id": 20,
        "question": "Which of the following represents 3 Crore 4 Lakh 7 Thousand 5 in standard Indian numerals?",
        "options": ["3,04,07,005", "3,40,70,005", "3,04,70,050", "30,47,005"],
        "correct": 0,
        "solution": "Step 1: Break into periods:\n• Crores: 3\n• Lakhs: 04\n• Thousands: 07\n• Ones: 005\nStep 2: Combine with commas: 3,04,07,005."
    },

    # Q21
    {
        "id": 21,
        "question": "What is 48,650 rounded off to the nearest thousand?",
        "options": ["48,000", "48,500", "49,000", "50,000"],
        "correct": 2,
        "solution": "Step 1: We want to round to the nearest thousand (thousands digit is 8).\nStep 2: Check the digit to its immediate right (hundreds place): it is 6.\nStep 3: Since $6 \\ge 5$, apply the halfway rule and round UP.\nStep 4: Increase 48,000 by 1,000 to get 49,000."
    },
    # Q22
    {
        "id": 22,
        "question": "What is 7,32,840 rounded off to the nearest lakh?",
        "options": ["7,00,000", "7,30,000", "8,00,000", "7,40,000"],
        "correct": 0,
        "solution": "Step 1: Target place is Lakhs (digit 7).\nStep 2: Inspect digit to immediate right (Ten-thousands place): it is 3.\nStep 3: Since $3 < 5$, round DOWN.\nStep 4: Keep 7 in lakhs place and set remaining digits to zero: 7,00,000."
    },
    # Q23
    {
        "id": 23,
        "question": "A number line shows landmarks at 60,000 and 70,000. Where does 65,000 round by standard convention?",
        "options": ["Down to 60,000", "Up to 70,000", "Stays unchanged as 65,000", "Rounds to 65,500"],
        "correct": 1,
        "solution": "Step 1: 65,000 is equidistant from 60,000 and 70,000 ($|65,000 - 60,000| = 5,000 = |70,000 - 65,000|$).\nStep 2: By standard mathematical rounding convention, exact halfway numbers ending in 5 are rounded UP.\nResult: 70,000."
    },
    # Q24
    {
        "id": 24,
        "question": "According to the 2011 Census, Mumbai's population was 1,24,42,373. What is this number rounded to the nearest lakh?",
        "options": ["1,20,00,000", "1,24,00,000", "1,25,00,000", "1,30,00,000"],
        "correct": 1,
        "solution": "Step 1: Lakhs place digit is 4 (preceded by 12, making 124 lakhs).\nStep 2: The ten-thousands digit is 4.\nStep 3: Since $4 < 5$, round down.\nResult: 1,24,00,000 (One crore twenty-four lakhs)."
    },
    # Q25
    {
        "id": 25,
        "question": "If Delhi's population was 98,17,439 in 2001 and 1,10,34,555 in 2011, by approximately how much did it increase?",
        "options": ["About 2 Lakhs", "About 12 Lakhs", "About 22 Lakhs", "About 32 Lakhs"],
        "correct": 1,
        "solution": "Step 1: Subtract 2001 population from 2011 population:\n$1,10,34,555 - 98,17,439 = 12,17,116$.\nStep 2: Rounding to the nearest lakh gives approximately 12 Lakhs."
    },
    # Q26
    {
        "id": 26,
        "question": "Which of the following numbers when rounded to the nearest hundred gives 5,800?",
        "options": ["5,749", "5,849", "5,851", "5,890"],
        "correct": 1,
        "solution": "Step 1: To round to 5,800, a number must lie between 5,750 and 5,849 inclusive.\nStep 2: Test options:\n• 5,749 rounds down to 5,700\n• 5,849 rounds down to 5,800 (Correct!)\n• 5,851 rounds up to 5,900\n• 5,890 rounds up to 5,900."
    },
    # Q27
    {
        "id": 27,
        "question": "In which daily life situation is an approximation unacceptable?",
        "options": ["Estimating spectators at an IPL cricket game", "Measuring intravenous medicine dosage in a hospital", "Estimating travel time from Pune to Nashik", "Announcing national wheat production estimates"],
        "correct": 1,
        "solution": "Step 1: Medical dosages require exact quantitative measurement (e.g., 5 mg vs 50 mg can be fatal).\nStep 2: Approximations in clinical medicine pose severe health risks."
    },
    # Q28
    {
        "id": 28,
        "question": "What is the smallest natural number that rounds up to 40,000 when rounding to the nearest ten-thousand?",
        "options": ["35,000", "34,999", "35,001", "39,500"],
        "correct": 0,
        "solution": "Step 1: To round up to 40,000, the thousands digit must be at least 5.\nStep 2: The boundary begins at 35,000 ($35,000$ rounds up to $40,000$, whereas $34,999$ rounds down to $30,000$).\nTherefore, 35,000 is the smallest such number."
    },
    # Q29
    {
        "id": 29,
        "question": "What is the largest whole number that rounds down to 40,000 when rounding to the nearest ten-thousand?",
        "options": ["40,499", "44,999", "45,000", "49,999"],
        "correct": 1,
        "solution": "Step 1: Any number from 40,000 to 44,999 has a thousands digit of $0, 1, 2, 3,$ or $4$, and therefore rounds down to 40,000.\nStep 2: At 45,000, the number would round up to 50,000.\nThus, 44,999 is the largest such number."
    },
    # Q30
    {
        "id": 30,
        "question": "Bengaluru's population grew from 43,01,326 in 2001 to 84,43,675 in 2011. What is the approximate percentage increase?",
        "options": ["About 25%", "About 50%", "About 96% (Nearly Doubled)", "About 200%"],
        "correct": 2,
        "solution": "Step 1: Population increased by: $84,43,675 - 43,01,326 = 41,42,349$.\nStep 2: Ratio of increase: $\\frac{41,42,349}{43,01,326} \\approx \\frac{41}{43} \\approx 0.963 = 96.3\\%$.\nStep 3: The city nearly doubled in population within 10 years!"
    },

    # Q31
    {
        "id": 31,
        "question": "Using the mental math shortcut $(N \\div 2) \\times 10$, calculate $68 \\times 5$:",
        "options": ["320", "340", "360", "380"],
        "correct": 1,
        "solution": "Step 1: Divide 68 by 2: $68 \\div 2 = 34$.\nStep 2: Multiply by 10: $34 \\times 10 = 340$.\nStep 3: Verification: $60 \\times 5 + 8 \\times 5 = 300 + 40 = 340$."
    },
    # Q32
    {
        "id": 32,
        "question": "Calculate $44 \\times 25$ using the $(N \\div 4) \\times 100$ shortcut:",
        "options": ["1,000", "1,100", "1,200", "1,400"],
        "correct": 1,
        "solution": "Step 1: Divide 44 by 4: $44 \\div 4 = 11$.\nStep 2: Multiply by 100: $11 \\times 100 = 1,100$.\nQuick, mental, and exact!"
    },
    # Q33
    {
        "id": 33,
        "question": "Simplify $14 \\times 35$ by grouped factorisation:",
        "options": ["$(7 \\times 2) \\times (5 \\times 7) = 49 \\times 10 = 490$", "$14 \\times 30 + 14 \\times 5 = 420 + 70 = 490$", "Both A and B are mathematically valid", "None of the above"],
        "correct": 2,
        "solution": "Step 1: Grouped factorisation: $14 \\times 35 = (7 \\times 2) \\times (5 \\times 7) = (7 \\times 7) \\times (2 \\times 5) = 49 \\times 10 = 490$.\nStep 2: Distributive expansion: $14 \\times (30 + 5) = 420 + 70 = 490$.\nBoth methods yield 490 correctly."
    },
    # Q34
    {
        "id": 34,
        "question": "If an m-digit number is multiplied by an n-digit number, what are the ONLY possible digit counts of the product?",
        "options": [
            "(m + n) only",
            "(m + n - 1) or (m + n)",
            "(m + n - 2) or (m + n - 1)",
            "(m × n) digits"
        ],
        "correct": 1,
        "solution": "Step 1: Let the numbers be $A$ ($m$ digits) and $B$ ($n$ digits).\nStep 2: $10^{m-1} \\le A < 10^m$ and $10^{n-1} \\le B < 10^n$.\nStep 3: Multiplying inequalities: $10^{m+n-2} \\le A \\times B < 10^{m+n}$.\nStep 4: The product has at least $(m + n - 1)$ digits and at most $(m + n)$ digits."
    },
    # Q35
    {
        "id": 35,
        "question": "How many digits will the product of a 3-digit number and a 5-digit number have?",
        "options": ["6 or 7 digits", "7 or 8 digits", "8 or 9 digits", "15 digits"],
        "correct": 1,
        "solution": "Step 1: Here $m = 3$ and $n = 5$.\nStep 2: Minimum digits = $m + n - 1 = 3 + 5 - 1 = 7$ digits.\nStep 3: Maximum digits = $m + n = 3 + 5 = 8$ digits.\nTherefore, the product will have either 7 or 8 digits."
    },
    # Q36
    {
        "id": 36,
        "question": "If the Amazon river discharges 2,00,000 m³ of water every second, how much water does it discharge in one full minute (60 seconds)?",
        "options": ["12,00,000 m³", "1,20,00,000 m³ (1.2 Crore m³)", "12,00,00,000 m³", "2,00,000 m³"],
        "correct": 1,
        "solution": "Step 1: Discharge in 1 second = $2,00,000\\text{ m}^3$.\nStep 2: 1 minute = 60 seconds.\nStep 3: Discharge in 1 minute = $2,00,000 \\times 60 = 1,20,00,000\\text{ m}^3$ (One crore twenty lakh cubic metres)."
    },
    # Q37
    {
        "id": 37,
        "question": "If sunlight traveling at 3,00,000 km/s takes 500 seconds to reach Earth, what is the distance between the Earth and the Sun?",
        "options": ["1,50,000 km", "15,00,000 km", "1,50,00,000 km", "15,00,00,000 km (15 Crore km)"],
        "correct": 3,
        "solution": "Step 1: Formula: $\\text{Distance} = \\text{Speed} \\times \\text{Time}$.\nStep 2: $\\text{Distance} = 3,00,000\\text{ km/s} \\times 500\\text{ s}$.\nStep 3: $3 \\times 5 = 15$; count zeroes: $5 + 2 = 7$ zeroes.\nResult: $15,00,00,000\\text{ km}$ (Fifteen Crore kilometres or 150 Million km)."
    },
    # Q38
    {
        "id": 38,
        "question": "If a double-decker bus seats 80 passengers, how many buses are required to seat 8,00,000 (eight lakh) people at once?",
        "options": ["1,000 buses", "10,000 buses", "100,000 buses", "8,000 buses"],
        "correct": 1,
        "solution": "Step 1: Divide total people by capacity per bus: $\\frac{8,00,000}{80}$.\nStep 2: Cancel zeroes: $\\frac{80,000}{8} = 10,000$ buses."
    },
    # Q39
    {
        "id": 39,
        "question": "The distance from Earth to the Moon is approximately 3,84,400 km. How long would a spacecraft traveling at a constant speed of 38,440 km/h take to reach the Moon?",
        "options": ["1 hour", "10 hours", "100 hours", "24 hours"],
        "correct": 1,
        "solution": "Step 1: Formula: $\\text{Time} = \\frac{\\text{Distance}}{\\text{Speed}}$.\nStep 2: $\\text{Time} = \\frac{3,84,400\\text{ km}}{38,440\\text{ km/h}} = 10\\text{ hours}$."
    },
    # Q40
    {
        "id": 40,
        "question": "If a student saves ₹50 every single day, how many days will it take for her to save ₹1,00,000 (One Lakh)?",
        "options": ["200 days", "2,000 days (approx. 5.5 years)", "20,000 days", "500 days"],
        "correct": 1,
        "solution": "Step 1: Formula: $\\text{Days} = \\frac{\\text{Total Amount}}{\\text{Daily Savings}}$.\nStep 2: $\\text{Days} = \\frac{1,00,000}{50}$.\nStep 3: $\\frac{100,000}{50} = 2,000$ days.\nIn years: $2,000 \\div 365 \\approx 5.48$ years."
    }
]
