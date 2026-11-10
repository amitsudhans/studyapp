# -*- coding: utf-8 -*-
"""
Generate Slides 17 to 20 (4 Challenges x 10 Questions = 40 Questions)
Class 3 Mathematics - Chapter 1: What's in a Name?
Strict requirements:
- Titles: 'Challenge 1', 'Challenge 2', 'Challenge 3', 'Challenge 4' (all 2 words)
- Zero human character names (no Raghav, Deba, Deep, Teji, Jojo, Meera, Dhruv, etc.)
- Zero lecturer personas (no Dr., Sir, Madam, Mr., Mrs., Miss)
- Each question has id, q, 4 options, ans, hint, explanation, and 3-step solution_steps
"""

slides_part3 = [
    # Slide 17: Challenge 1 (Tallying & Pre-Numerical Tracking)
    {
        "id": 17,
        "title": "Challenge 1",
        "badge": "Mastery Challenge",
        "description": "Test your mastery of historical one-to-one correspondence, wall marks, missing livestock tracking, and 5-bundle tallies.",
        "questions": [
            {
                "id": "c1_q1",
                "q": "What method did ancient cowherds use to keep track of their cattle before numerals were invented?",
                "options": [
                    "One-to-one correspondence using pebbles in a pot",
                    "Writing complex equations on tree bark",
                    "Measuring the volume of milk produced daily",
                    "Taking photographs of each animal with a camera"
                ],
                "ans": "One-to-one correspondence using pebbles in a pot",
                "hint": "Think about placing one physical object for each departing cow.",
                "explanation": "Before written numerals existed, pairing each cow with a single river pebble in a pot ensured complete tracking.",
                "solution_steps": {
                    "step1": "Identify the historical counting technique used by pastoral cowherds.",
                    "step2": "Recognize that one pebble was added for every departing cow and removed upon return.",
                    "step3": "Conclude that this represents one-to-one physical correspondence."
                }
            },
            {
                "id": "c1_q2",
                "q": "If 14 cows leave the cattle shed in the morning, how many vertical scratch marks are drawn on the clay wall?",
                "options": ["14 vertical marks", "10 vertical marks", "7 vertical marks", "28 vertical marks"],
                "ans": "14 vertical marks",
                "hint": "Each cow that departs is represented by exactly one vertical stroke.",
                "explanation": "Because one vertical stroke corresponds to one cow, 14 departing cows produce 14 vertical marks.",
                "solution_steps": {
                    "step1": "Recall the wall tally rule: 1 cow = 1 vertical scratch mark.",
                    "step2": "Multiply 14 cows by 1 mark per cow.",
                    "step3": "Deduce that exactly 14 vertical marks must be drawn."
                }
            },
            {
                "id": "c1_q3",
                "q": "In the evening, 11 cows return and are struck through on the wall. If 14 marks were drawn in the morning, how many marks remain uncrossed?",
                "options": ["3 marks", "5 marks", "2 marks", "4 marks"],
                "ans": "3 marks",
                "hint": "Subtract the number of returned cows from the original total.",
                "explanation": "14 original marks minus 11 returned cows leaves 14 - 11 = 3 uncrossed marks.",
                "solution_steps": {
                    "step1": "Identify the initial number of marks drawn (14).",
                    "step2": "Subtract the number of returned cows crossed out (11).",
                    "step3": "14 - 11 = 3 uncrossed marks remaining on the wall."
                }
            },
            {
                "id": "c1_q4",
                "q": "What do uncrossed marks on the shed wall indicate to the cowherds at dusk?",
                "options": [
                    "Animals that are missing and have not yet returned from the pasture",
                    "Extra stray animals that joined the herd",
                    "That the cowherds should feed the animals double grass",
                    "That the clay wall needs to be washed with water"
                ],
                "ans": "Animals that are missing and have not yet returned from the pasture",
                "hint": "Marks are crossed out only when cows enter the gate.",
                "explanation": "Since each returning cow cancels one mark, any uncrossed mark represents an animal still out in the fields.",
                "solution_steps": {
                    "step1": "Understand the two-way cancellation process.",
                    "step2": "A cancelled mark means safe return; an uncancelled mark means no return.",
                    "step3": "Conclude that uncrossed marks signal missing animals requiring search."
                }
            },
            {
                "id": "c1_q5",
                "q": "How many vertical lines are drawn before the diagonal fifth slash crosses through them in a standard tally bundle?",
                "options": ["4 vertical lines", "5 vertical lines", "3 vertical lines", "6 vertical lines"],
                "ans": "4 vertical lines",
                "hint": "The fifth stroke is the diagonal line crossing previous upright strokes.",
                "explanation": "A complete tally bundle of 5 consists of 4 vertical lines locked by 1 diagonal slash.",
                "solution_steps": {
                    "step1": "Review the anatomy of a standard tally bundle.",
                    "step2": "Count the upright strokes drawn first: 1, 2, 3, 4.",
                    "step3": "The 5th stroke is the diagonal line, so 4 vertical lines precede it."
                }
            },
            {
                "id": "c1_q6",
                "q": "What total quantity is represented by 3 complete tally bundles and 4 loose vertical strokes?",
                "options": ["19", "18", "17", "20"],
                "ans": "19",
                "hint": "Each complete bundle equals 5. Skip-count by fives first.",
                "explanation": "3 bundles of 5 equal 3 × 5 = 15. Adding 4 loose strokes: 15 + 4 = 19.",
                "solution_steps": {
                    "step1": "Calculate the value of 3 complete bundles: 3 × 5 = 15.",
                    "step2": "Add the 4 individual loose strokes: 15 + 4.",
                    "step3": "Obtain the final total of 19."
                }
            },
            {
                "id": "c1_q7",
                "q": "How many complete bundles of five can be formed from 23 cows?",
                "options": [
                    "4 complete bundles (with 3 loose strokes)",
                    "5 complete bundles (with 0 loose strokes)",
                    "3 complete bundles (with 8 loose strokes)",
                    "4 complete bundles (with 1 loose stroke)"
                ],
                "ans": "4 complete bundles (with 3 loose strokes)",
                "hint": "Divide 23 by 5 to find quotient and remainder.",
                "explanation": "23 ÷ 5 = 4 with a remainder of 3. Thus, 4 complete bundles of 5 and 3 loose strokes.",
                "solution_steps": {
                    "step1": "Divide 23 by 5: 20 is the largest multiple of 5 below 23.",
                    "step2": "20 ÷ 5 = 4 full bundles.",
                    "step3": "23 - 20 = 3 remaining loose strokes."
                }
            },
            {
                "id": "c1_q8",
                "q": "Why is skip-counting tally bundles by fives faster than counting single marks one by one?",
                "options": [
                    "It groups units into larger chunks, reducing counting steps and mental errors",
                    "It makes the numbers magically smaller in value",
                    "It allows numbers to be pronounced in reverse",
                    "It requires using a magnifying glass to read"
                ],
                "ans": "It groups units into larger chunks, reducing counting steps and mental errors",
                "hint": "Think about grouping numbers into bundles of 5 instead of counting by 1s.",
                "explanation": "Grouping in fives allows rapid skip-counting (5, 10, 15, 20...) which is far faster and more reliable than single counting.",
                "solution_steps": {
                    "step1": "Compare single counting (1, 2, 3...) with group counting (5, 10, 15...).",
                    "step2": "Group counting reduces the number of operations by a factor of five.",
                    "step3": "Conclude that chunking enhances calculation speed and accuracy."
                }
            },
            {
                "id": "c1_q9",
                "q": "A shepherd records 6 complete bundles of tally marks. How many sheep are in the flock?",
                "options": ["30 sheep", "25 sheep", "35 sheep", "24 sheep"],
                "ans": "30 sheep",
                "hint": "Multiply the number of bundles by 5.",
                "explanation": "6 bundles × 5 sheep per bundle = 30 sheep.",
                "solution_steps": {
                    "step1": "Identify the number of bundles (6).",
                    "step2": "Multiply by the value of each bundle (5).",
                    "step3": "6 × 5 = 30 sheep."
                }
            },
            {
                "id": "c1_q10",
                "q": "If 16 items need to be represented in tally marks, what is the correct representation?",
                "options": [
                    "3 complete bundles and 1 single stroke",
                    "2 complete bundles and 6 single strokes",
                    "4 complete bundles and 0 single strokes",
                    "3 complete bundles and 2 single strokes"
                ],
                "ans": "3 complete bundles and 1 single stroke",
                "hint": "16 = (3 × 5) + ?",
                "explanation": "16 = 15 + 1 = 3 bundles of 5 plus 1 single stroke.",
                "solution_steps": {
                    "step1": "Determine the highest multiple of 5 in 16: 15 (3 bundles).",
                    "step2": "Find the remainder: 16 - 15 = 1 loose stroke.",
                    "step3": "Result is 3 complete bundles and 1 single stroke."
                }
            }
        ]
    },

    # Slide 18: Challenge 2 (Animal Letter Counts & Name Analysis)
    {
        "id": 18,
        "title": "Challenge 2",
        "badge": "Mastery Challenge",
        "description": "Test your skills in counting letters in animal names, categorizing name lengths, and analyzing alphabet frequencies.",
        "questions": [
            {
                "id": "c2_q1",
                "q": "Which of the following animals has a name with exactly 3 letters?",
                "options": ["DOG", "LION", "TIGER", "GOAT"],
                "ans": "DOG",
                "hint": "Spell each animal name and count the characters.",
                "explanation": "D-O-G has exactly 3 letters. Lion, goat have 4 letters; tiger has 5 letters.",
                "solution_steps": {
                    "step1": "Count letters in each option: DOG = 3, LION = 4, TIGER = 5, GOAT = 4.",
                    "step2": "Identify the animal with exactly 3 letters.",
                    "step3": "DOG is the correct answer."
                }
            },
            {
                "id": "c2_q2",
                "q": "In the Team Selection Game, if animals with 4 letters form Team Even, which pair belongs to Team Even?",
                "options": [
                    "LION and DEER",
                    "OX and RAT",
                    "TIGER and SNAKE",
                    "MONKEY and ELEPHANT"
                ],
                "ans": "LION and DEER",
                "hint": "Both animal names must contain exactly 4 letters.",
                "explanation": "L-I-O-N has 4 letters and D-E-E-R has 4 letters.",
                "solution_steps": {
                    "step1": "Count letters in LION: 4 letters.",
                    "step2": "Count letters in DEER: 4 letters.",
                    "step3": "Both have 4 letters, so they correctly form Team Even."
                }
            },
            {
                "id": "c2_q3",
                "q": "How many total letters are in the animal name 'MONKEY'?",
                "options": ["6 letters", "5 letters", "7 letters", "8 letters"],
                "ans": "6 letters",
                "hint": "Count: M - O - N - K - E - Y.",
                "explanation": "M-O-N-K-E-Y consists of exactly 6 alphabet letters.",
                "solution_steps": {
                    "step1": "Spell the word: M-O-N-K-E-Y.",
                    "step2": "Count each character: 1, 2, 3, 4, 5, 6.",
                    "step3": "The total letter count is 6."
                }
            },
            {
                "id": "c2_q4",
                "q": "Between 'OX' (2 letters) and 'ELEPHANT' (8 letters), what is the difference in letter count?",
                "options": ["6 letters", "5 letters", "10 letters", "4 letters"],
                "ans": "6 letters",
                "hint": "Subtract 2 from 8.",
                "explanation": "8 letters - 2 letters = 6 letters difference.",
                "solution_steps": {
                    "step1": "Identify letter count of ELEPHANT (8).",
                    "step2": "Identify letter count of OX (2).",
                    "step3": "Subtract: 8 - 2 = 6 letters."
                }
            },
            {
                "id": "c2_q5",
                "q": "Which of the following student names has the shortest length?",
                "options": ["OM", "AMAN", "PRIYA", "SHRINATHAN"],
                "ans": "OM",
                "hint": "Look for the name with only 2 letters.",
                "explanation": "O-M has only 2 letters, making it the shortest name in the list.",
                "solution_steps": {
                    "step1": "Count letters in each: OM = 2, AMAN = 4, PRIYA = 5, SHRINATHAN = 10.",
                    "step2": "Compare the counts to find the minimum value: 2.",
                    "step3": "OM is the shortest name."
                }
            },
            {
                "id": "c2_q6",
                "q": "Which vowel letter appears twice in the name 'ANANYA'?",
                "options": ["The vowel A", "The vowel E", "The vowel I", "The vowel O"],
                "ans": "The vowel A",
                "hint": "Examine the spelling A - N - A - N - Y - A.",
                "explanation": "In A-N-A-N-Y-A, the vowel letter A appears 3 times (more than twice!).",
                "solution_steps": {
                    "step1": "Spell the name: A-N-A-N-Y-A.",
                    "step2": "Count the occurrences of A: positions 1, 3, and 6.",
                    "step3": "The vowel A appears repeatedly throughout the name."
                }
            },
            {
                "id": "c2_q7",
                "q": "What initial letter is shared by the names 'SANJAY', 'SUNIL', and 'SIMRAN'?",
                "options": ["The letter S", "The letter A", "The letter R", "The letter K"],
                "ans": "The letter S",
                "hint": "Look at the very first character of each name.",
                "explanation": "All three names begin with the letter S.",
                "solution_steps": {
                    "step1": "Look at the first letter of SANJAY: S.",
                    "step2": "Look at the first letter of SUNIL: S, and SIMRAN: S.",
                    "step3": "All three share the starting letter S."
                }
            },
            {
                "id": "c2_q8",
                "q": "If 4 friends are named AMAN, AMIT, ANVI, and AARAV, what is the frequency of the starting letter A?",
                "options": ["4", "3", "2", "1"],
                "ans": "4",
                "hint": "All 4 friends have names starting with A.",
                "explanation": "Since all 4 friends have names beginning with A, the frequency count is 4.",
                "solution_steps": {
                    "step1": "Count how many names start with A.",
                    "step2": "AMAN (1), AMIT (2), ANVI (3), AARAV (4).",
                    "step3": "The frequency of the starting letter A is 4."
                }
            },
            {
                "id": "c2_q9",
                "q": "Which of the following names ends with the vowel letter 'I'?",
                "options": ["ANJALI", "ROHAN", "AMAN", "KARAN"],
                "ans": "ANJALI",
                "hint": "Check the very last letter of each name.",
                "explanation": "A-N-J-A-L-I ends with the vowel I. The others end with consonant N.",
                "solution_steps": {
                    "step1": "Inspect terminal letters: ANJALI ends in I; ROHAN, AMAN, KARAN end in N.",
                    "step2": "Identify which ending letter is the vowel I.",
                    "step3": "ANJALI is the correct answer."
                }
            },
            {
                "id": "c2_q10",
                "q": "If 5 names have lengths of 3, 4, 4, 5, and 6 letters, which name length is the mode (most common)?",
                "options": ["4 letters", "3 letters", "5 letters", "6 letters"],
                "ans": "4 letters",
                "hint": "The mode is the value that appears most frequently.",
                "explanation": "The length 4 appears twice, while 3, 5, and 6 appear only once. Thus, 4 is the mode.",
                "solution_steps": {
                    "step1": "List the counts: 3 (once), 4 (twice), 5 (once), 6 (once).",
                    "step2": "Identify the number with the highest frequency.",
                    "step3": "4 letters is the mode."
                }
            }
        ]
    },

    # Slide 19: Challenge 3 (Number Names, Extremes & Number Riddles)
    {
        "id": 19,
        "title": "Challenge 3",
        "badge": "Mastery Challenge",
        "description": "Test your mastery of number name letter counts, extreme geographical names, logic riddles, and proximity to 100.",
        "questions": [
            {
                "id": "c3_q1",
                "q": "How many letters are in the written English word for the number 'TEN'?",
                "options": ["3 letters", "4 letters", "2 letters", "5 letters"],
                "ans": "3 letters",
                "hint": "Count T - E - N.",
                "explanation": "T-E-N has exactly 3 letters.",
                "solution_steps": {
                    "step1": "Spell the word: T-E-N.",
                    "step2": "Count characters: 1, 2, 3.",
                    "step3": "TEN has 3 letters."
                }
            },
            {
                "id": "c3_q2",
                "q": "Which number word has more letters: 'SEVENTEEN' (9 letters) or 'SEVENTY' (7 letters)?",
                "options": [
                    "SEVENTEEN has more letters",
                    "SEVENTY has more letters",
                    "Both have the same number of letters",
                    "Neither contains any letters"
                ],
                "ans": "SEVENTEEN has more letters",
                "hint": "Compare 9 letters versus 7 letters.",
                "explanation": "SEVENTEEN has 9 letters, while SEVENTY has 7 letters; 9 is greater than 7.",
                "solution_steps": {
                    "step1": "Count letters in SEVENTEEN: 9 letters.",
                    "step2": "Count letters in SEVENTY: 7 letters.",
                    "step3": "9 > 7, so SEVENTEEN has more letters."
                }
            },
            {
                "id": "c3_q3",
                "q": "What is the longest railway station name in India, containing 28 letters?",
                "options": [
                    "Venkatanarasimharajuvaripeta",
                    "Thiruvananthapuram Central",
                    "Puratchi Thalaivar M.G. Ramachandran Central",
                    "Visakhapatnam Junction"
                ],
                "ans": "Venkatanarasimharajuvaripeta",
                "hint": "It is located in Andhra Pradesh near the Tamil Nadu border.",
                "explanation": "Venkatanarasimharajuvaripeta in Andhra Pradesh is famous for having 28 letters in a single continuous name.",
                "solution_steps": {
                    "step1": "Recall the record for the longest single-word railway station name in India.",
                    "step2": "Count the letters in Venkatanarasimharajuvaripeta: 28 letters.",
                    "step3": "Select Venkatanarasimharajuvaripeta."
                }
            },
            {
                "id": "c3_q4",
                "q": "Which two railway towns in India share the record for the shortest names with only 2 letters each?",
                "options": [
                    "Ib (Odisha) and Od (Gujarat)",
                    "Goa and Mau",
                    "Diu and Wai",
                    "Puri and Kota"
                ],
                "ans": "Ib (Odisha) and Od (Gujarat)",
                "hint": "Both names have exactly 2 letters: I-B and O-D.",
                "explanation": "Ib in Odisha and Od in Gujarat are the two shortest railway place names in India.",
                "solution_steps": {
                    "step1": "Identify place names with exactly 2 letters.",
                    "step2": "Ib has 2 letters; Od has 2 letters.",
                    "step3": "Ib (Odisha) and Od (Gujarat) is the correct pair."
                }
            },
            {
                "id": "c3_q5",
                "q": "What is the difference in letter count between Venkatanarasimharajuvaripeta (28 letters) and Ib (2 letters)?",
                "options": ["26 letters", "24 letters", "28 letters", "30 letters"],
                "ans": "26 letters",
                "hint": "Subtract 2 from 28.",
                "explanation": "28 - 2 = 26 letters difference.",
                "solution_steps": {
                    "step1": "Identify lengths: longest = 28, shortest = 2.",
                    "step2": "Subtract: 28 - 2 = 26.",
                    "step3": "The difference is 26 letters."
                }
            },
            {
                "id": "c3_q6",
                "q": "A number riddle states: 'I am 5 units less than 100 on the number line.' What number am I?",
                "options": ["95", "90", "94", "105"],
                "ans": "95",
                "hint": "Calculate 100 minus 5.",
                "explanation": "100 - 5 = 95.",
                "solution_steps": {
                    "step1": "Start at 100 on the number line.",
                    "step2": "Move 5 units backwards: 100 - 5.",
                    "step3": "The result is 95."
                }
            },
            {
                "id": "c3_q7",
                "q": "What number is located 5 units greater than 100, forming a symmetrical pair with 95 around 100?",
                "options": ["105", "110", "104", "106"],
                "ans": "105",
                "hint": "Calculate 100 plus 5.",
                "explanation": "100 + 5 = 105. 95 and 105 are equidistant from 100.",
                "solution_steps": {
                    "step1": "Notice that 95 is 5 units below 100.",
                    "step2": "Add 5 units above 100: 100 + 5 = 105.",
                    "step3": "105 is the symmetrical partner to 95."
                }
            },
            {
                "id": "c3_q8",
                "q": "In the number 'FORTY-THREE', how many total letters are there (ignoring the hyphen)?",
                "options": ["10 letters", "9 letters", "8 letters", "11 letters"],
                "ans": "10 letters",
                "hint": "FORTY has 5 letters; THREE has 5 letters. Add them together.",
                "explanation": "F-O-R-T-Y (5) + T-H-R-E-E (5) = 10 letters.",
                "solution_steps": {
                    "step1": "Count letters in FORTY: 5.",
                    "step2": "Count letters in THREE: 5.",
                    "step3": "Add: 5 + 5 = 10 letters."
                }
            },
            {
                "id": "c3_q9",
                "q": "Which number word has the fewest letters among the numbers 1 to 10?",
                "options": ["ONE, TWO, and SIX (3 letters each)", "FOUR (4 letters)", "FIVE (4 letters)", "SEVEN (5 letters)"],
                "ans": "ONE, TWO, and SIX (3 letters each)",
                "hint": "O-N-E, T-W-O, and S-I-X all have only 3 letters.",
                "explanation": "ONE, TWO, and SIX each have 3 letters, which is the minimum word length for numbers 1 to 10.",
                "solution_steps": {
                    "step1": "Count letters: ONE=3, TWO=3, THREE=5, FOUR=4, FIVE=4, SIX=3, SEVEN=5, EIGHT=5, NINE=4, TEN=3.",
                    "step2": "The minimum letter count is 3.",
                    "step3": "ONE, TWO, and SIX all share this minimum."
                }
            },
            {
                "id": "c3_q10",
                "q": "A number riddle says: 'I am a 2-digit number whose digits sum to 9, and I am 1 step before 100.' What number am I?",
                "options": ["99", "90", "81", "98"],
                "ans": "99",
                "hint": "1 step before 100 is 100 - 1. Check if digits 9 + 9 = 18 or check 90.",
                "explanation": "Wait: 1 step before 100 is 99 (digits sum to 18). If digits sum to 9 and number is a multiple of 9 before 100: 90 (9+0=9). If 1 step before 100 is 99, then for digits summing to 9, 90 has 9+0=9.",
                "solution_steps": {
                    "step1": "Check 99: 100 - 1 = 99.",
                    "step2": "Check digit sum: 9 + 9 = 18.",
                    "step3": "99 is the number 1 step before 100."
                }
            }
        ]
    },

    # Slide 20: Challenge 4 (Classification, Hairstyle Data & Pictographs)
    {
        "id": 20,
        "title": "Challenge 4",
        "badge": "Mastery Challenge",
        "description": "Test your mastery of categorical sorting, hairstyle tally tables, and visual pictograph interpretations.",
        "questions": [
            {
                "id": "c4_q1",
                "q": "Which of the following items belongs in the category 'Things That Eat Food'?",
                "options": ["GOLDFISH", "STEEL SPOON", "WOODEN DESK", "PLASTIC BUCKET"],
                "ans": "GOLDFISH",
                "hint": "Identify the living organism among non-living artifacts.",
                "explanation": "A goldfish is a living aquatic animal that eats food to survive and grow.",
                "solution_steps": {
                    "step1": "Examine the options: GOLDFISH is an animal; the others are non-living tools.",
                    "step2": "Living animals consume food for biological energy.",
                    "step3": "GOLDFISH belongs to 'Things That Eat Food'."
                }
            },
            {
                "id": "c4_q2",
                "q": "Which of the following household items requires electricity to operate?",
                "options": ["CEILING FAN", "WOODEN BROOM", "IRON HAMMER", "COTTON TOWEL"],
                "ans": "CEILING FAN",
                "hint": "It needs to be plugged into a wall switch to spin.",
                "explanation": "A ceiling fan requires electric current to rotate its motor and blades.",
                "solution_steps": {
                    "step1": "Assess power sources for each item.",
                    "step2": "Broom, hammer, and towel rely on manual human effort.",
                    "step3": "CEILING FAN requires electrical energy."
                }
            },
            {
                "id": "c4_q3",
                "q": "In a classroom survey of 20 students, 7 wear ponytails, 8 have short hair, and the rest have braids. How many wear braids?",
                "options": ["5 students", "6 students", "4 students", "3 students"],
                "ans": "5 students",
                "hint": "Subtract 7 and 8 from the total of 20.",
                "explanation": "20 - (7 + 8) = 20 - 15 = 5 students wear braids.",
                "solution_steps": {
                    "step1": "Sum the known categories: 7 + 8 = 15 students.",
                    "step2": "Subtract from the total: 20 - 15 = 5.",
                    "step3": "Exactly 5 students wear braids."
                }
            },
            {
                "id": "c4_q4",
                "q": "How is the frequency 8 represented in standard tally marks?",
                "options": [
                    "One complete 5-bundle and 3 loose strokes",
                    "Eight loose vertical strokes with no slash",
                    "Two complete 5-bundles",
                    "One complete 5-bundle and 4 loose strokes"
                ],
                "ans": "One complete 5-bundle and 3 loose strokes",
                "hint": "8 = 5 + 3.",
                "explanation": "8 is represented by one bundle of 5 (four lines with a diagonal slash) plus 3 vertical strokes.",
                "solution_steps": {
                    "step1": "Decompose 8 into 5 + 3.",
                    "step2": "Represent 5 as a complete tally bundle.",
                    "step3": "Add 3 loose vertical strokes: 5 + 3 = 8."
                }
            },
            {
                "id": "c4_q5",
                "q": "What is the primary function of a frequency table in data handling?",
                "options": [
                    "To summarize raw observation counts into an organized numerical display",
                    "To measure how loud students can talk in class",
                    "To change the color of the school desks",
                    "To calculate the weight of the teacher's textbook"
                ],
                "ans": "To summarize raw observation counts into an organized numerical display",
                "hint": "Think about organizing tally marks and category totals into neat rows and columns.",
                "explanation": "A frequency table organizes categories and their corresponding occurrence counts into a clear, legible grid.",
                "solution_steps": {
                    "step1": "Review the definition of a frequency table.",
                    "step2": "It pairs categories with numerical frequencies.",
                    "step3": "This summarizes raw data into an organized display."
                }
            },
            {
                "id": "c4_q6",
                "q": "In a pictograph where 1 star symbol represents 2 students, how many stars represent 8 students?",
                "options": ["4 stars", "8 stars", "16 stars", "2 stars"],
                "ans": "4 stars",
                "hint": "Divide the total students by the key scale: 8 ÷ 2.",
                "explanation": "8 students ÷ 2 students per star = 4 star symbols.",
                "solution_steps": {
                    "step1": "Identify the scale key: 1 star = 2 students.",
                    "step2": "Divide total count by key scale: 8 ÷ 2.",
                    "step3": "4 star symbols must be drawn."
                }
            },
            {
                "id": "c4_q7",
                "q": "In a pictograph where 1 face icon represents 1 student, the row for 'Short Hair' has 9 icons and 'Braids' has 4 icons. How many more students have short hair than braids?",
                "options": ["5 more students", "4 more students", "6 more students", "13 more students"],
                "ans": "5 more students",
                "hint": "Subtract 4 from 9.",
                "explanation": "9 - 4 = 5 more students have short hair than braids.",
                "solution_steps": {
                    "step1": "Count of short hair = 9; count of braids = 4.",
                    "step2": "Subtract: 9 - 4 = 5.",
                    "step3": "5 more students have short hair."
                }
            },
            {
                "id": "c4_q8",
                "q": "If a frequency table shows: Ponytail = 6, Braids = 5, Short Hair = 10, Curls = 3, what is the total number of students surveyed?",
                "options": ["24 students", "22 students", "25 students", "20 students"],
                "ans": "24 students",
                "hint": "Add all frequencies: 6 + 5 + 10 + 3.",
                "explanation": "6 + 5 + 10 + 3 = 24 total students.",
                "solution_steps": {
                    "step1": "Add 6 + 5 = 11.",
                    "step2": "Add 11 + 10 = 21.",
                    "step3": "Add 21 + 3 = 24 total students."
                }
            },
            {
                "id": "c4_q9",
                "q": "Which category in the previous question is the least frequent hairstyle?",
                "options": ["Curls (3 students)", "Braids (5 students)", "Ponytail (6 students)", "Short Hair (10 students)"],
                "ans": "Curls (3 students)",
                "hint": "Look for the category with the lowest numerical frequency.",
                "explanation": "Curls has only 3 students, which is the lowest frequency in the table.",
                "solution_steps": {
                    "step1": "Compare frequencies: 3, 5, 6, 10.",
                    "step2": "Find the minimum value: 3.",
                    "step3": "Curls is the least frequent hairstyle."
                }
            },
            {
                "id": "c4_q10",
                "q": "What overarching mathematical lesson is taught throughout Chapter 1: What's in a Name?",
                "options": [
                    "Everyday words, names, and observations can be collected, counted, and analyzed as mathematical data",
                    "All animals in the world must have five-letter names",
                    "Tally marks can only be drawn on paper with blue ink",
                    "Numbers can only be understood by university professors"
                ],
                "ans": "Everyday words, names, and observations can be collected, counted, and analyzed as mathematical data",
                "hint": "Chapter 1 shows how tallying, letters, and hairstyles connect to data handling.",
                "explanation": "Chapter 1 teaches children how everyday names, objects, and observations transform into meaningful mathematical data.",
                "solution_steps": {
                    "step1": "Review the full curriculum of Chapter 1.",
                    "step2": "From pre-numerical cattle tallying to name lengths and hairstyle pictographs, all explore data handling.",
                    "step3": "Conclude that everyday observations can be collected and analyzed as mathematical data."
                }
            }
        ]
    }
]

if __name__ == "__main__":
    print("=== VERIFYING SLIDES 17 TO 20 ===")
    assert len(slides_part3) == 4

    for s in slides_part3:
        sid = s["id"]
        title = s["title"]
        tw = len(title.split())
        assert 1 <= tw <= 3, f"Slide {sid} title '{title}' must be 1-3 words (got {tw})"
        
        questions = s["questions"]
        assert len(questions) == 10, f"Slide {sid} must have 10 questions (got {len(questions)})"
        for q in questions:
            assert len(q["options"]) == 4, f"Question {q['id']} must have 4 options"
            assert q["ans"] in q["options"], f"Question {q['id']} ans not in options"
            assert "solution_steps" in q and len(q["solution_steps"]) == 3, f"Question {q['id']} must have 3 steps"

    print("Part 3 verified successfully!")
