# -*- coding: utf-8 -*-
"""
Data module for Class 9 Mathematics Chapter 15: Introduction to Probability
Syllabus Competencies: CG-6, C-6.2, CG-9
Contains 16 content slides (with 2 checkpoints each = 32 checkpoints)
and 4 quiz challenge slides (with 10 questions each = 40 quiz questions with full step-by-step solutions).
"""

SLIDES = [
    {
        "id": 1,
        "title": "Chance, Uncertainty & The Concept of Randomness",
        "subtitle": "From 17th Century Gambling Puzzles to Modern Mathematical Foundations of Uncertainty",
        "category": "Foundations of Probability",
        "badge": "CG-6 • Random Experiments",
        "summary": "Probability is the mathematical quantification of uncertainty and likelihood. In daily life, we constantly encounter unpredictable events—'It will probably rain today', 'India has a high chance of winning the match', or 'I doubt he will pass'. A Deterministic Experiment is one where all conditions are fully known and the outcome is strictly predictable (e.g., heating pure water to 100°C at sea level always causes boiling). In contrast, a Random Experiment satisfies two cardinal criteria: (1) It has more than one possible outcome; and (2) It is impossible to predict the exact specific outcome in advance, even when performed under identical conditions. A single performance of a random experiment is called a Trial, and the result obtained is an Outcome. Elementary events are the simplest possible individual results of a trial.",
        "key_points": [
            "Random Experiment Criteria: Has multiple possible outcomes, and the specific outcome cannot be predicted in advance.",
            "Deterministic vs Random: Deterministic yields a fixed certain outcome; random produces stochastic variation.",
            "Trial & Outcome: A Trial is a single execution of the experiment; an Outcome is the specific result observed.",
            "Historical Roots: Founded in 1654 through correspondence between Blaise Pascal and Pierre de Fermat regarding gambling puzzles.",
            "Elementary Events: The atomic, indivisible outcomes of a single trial (e.g., getting a '4' on a rolled die)."
        ],
        "narration": "Welcome to Introduction to Probability! In life, nothing is more constant than uncertainty. When a scientist heats water to one hundred degrees Celsius, it will definitely boil—that is a deterministic experiment. But when you flip a coin or roll a die, you cannot predict the exact outcome in advance—that is a random experiment. In 1654, two brilliant mathematicians, Blaise Pascal and Pierre de Fermat, created the mathematical laws of chance. Try our interactive experiment to explore the clear contrast between deterministic laws and genuine randomness!",
        "sim_title": "Interactive Randomness vs Determinism Lab & Streak Tester",
        "checkpoints": [
            {
                "q": "Which of the following is the defining characteristic of a random experiment?",
                "options": [
                    "It always produces the exact same outcome every time",
                    "It has more than one possible outcome and the specific outcome cannot be predicted beforehand",
                    "It can only be performed once in a laboratory",
                    "The outcomes are always numbers"
                ],
                "ans": 1,
                "exp": "A random experiment must have more than one possible outcome, and its specific outcome cannot be predicted in advance even under identical experimental conditions."
            },
            {
                "q": "Which of the following is a deterministic experiment?",
                "options": [
                    "Tossing an unbiased coin",
                    "Drawing a card from a shuffled deck",
                    "Dropping an iron ball in a vacuum to measure its gravitational acceleration",
                    "Rolling a pair of standard dice"
                ],
                "ans": 2,
                "exp": "Dropping a ball in a vacuum follows deterministic physics (g = 9.8 m/s²), producing a completely predictable result, unlike coin tosses, dice rolls, or card draws which are random experiments."
            }
        ]
    },
    {
        "id": 2,
        "title": "The Universal Probability Scale: From Impossible to Certain",
        "subtitle": "Mapping Likelihood from Absolute Impossibility (0) to Inevitable Certainty (1)",
        "category": "Foundations of Probability",
        "badge": "C-6.2 • Probability Scale",
        "summary": "The probability of any event E, denoted by P(E), is a real number strictly bounded on the closed interval between 0 and 1: 0 ≤ P(E) ≤ 1 (or equivalently 0% ≤ P(E) ≤ 100%). Key Landmarks on the Probability Scale: (1) Impossible Event: An event that can never occur under any circumstance has P(E) = 0 (e.g., rolling an 8 on a standard 6-sided die, or the sun rising in the west); (2) Certain (or Sure) Event: An event that is guaranteed to occur in every single trial has P(E) = 1 (e.g., rolling a number less than 7 on a standard die); (3) Even Chance: An event with P(E) = 0.5 (or 1/2, 50%), where occurrence and non-occurrence are equally likely (e.g., getting Heads on a fair coin). Qualitative likelihood terms map systematically to this continuum: Impossible (0.0) → Highly Unlikely (0.1) → Unlikely (0.25) → Even Chance (0.5) → Likely (0.75) → Highly Likely (0.9) → Certain (1.0). A probability can NEVER be negative, nor can it ever exceed 1.",
        "key_points": [
            "The Fundamental Inequality: 0 ≤ P(E) ≤ 1; probability is never negative and never greater than 1.",
            "Impossible Event: P(E) = 0; the event cannot occur under the defined experiment.",
            "Certain / Sure Event: P(E) = 1; the event is guaranteed to happen in every trial.",
            "Even Chance: P(E) = 0.5 (1/2 or 50%); equal likelihood of happening versus not happening.",
            "Equivalent Expressions: Can be represented interchangeably as fractions (3/4), decimals (0.75), or percentages (75%)."
        ],
        "narration": "Every probability in the universe lives on a scale between zero and one! Zero means impossible—like rolling an eight on a six-sided die. One means absolute certainty—like rolling a number less than seven. Right in the center sits zero point five, an even fifty-fifty chance, like tossing heads on a fair coin. Notice that a probability can never be negative, and it can never be greater than one! Drag different real-world scenarios on our interactive probability scale to see how everyday language maps directly into mathematical values.",
        "sim_title": "The Interactive Probability Spectrum Slider & Verbal Mapper",
        "checkpoints": [
            {
                "q": "Which of the following numbers CANNOT represent the probability of an event?",
                "options": ["2/3", "-1.5", "15%", "0.7"],
                "ans": 1,
                "exp": "By the fundamental probability axiom, 0 ≤ P(E) ≤ 1. A probability can never be negative (-1.5 < 0) or greater than 1."
            },
            {
                "q": "What is the probability of an impossible event?",
                "options": ["-1", "0", "0.5", "1"],
                "ans": 1,
                "exp": "An impossible event can never occur under any circumstances; hence its probability is identically 0."
            }
        ]
    },
    {
        "id": 3,
        "title": "Empirical (Experimental) Probability: Real-World Trials",
        "subtitle": "Estimating Probabilities from Observed Relative Frequencies in Actual Experiments",
        "category": "Empirical Probability",
        "badge": "C-6.2 • Empirical Trials",
        "summary": "Empirical Probability (also known as Experimental Probability) is determined by conducting actual physical trials and recording observed outcomes. It is defined as the relative frequency of the event: P_n(E) = (Number of trials in which event E occurred) / (Total number of trials conducted) = f_n / n. Unlike theoretical probability which relies on idealized symmetry, empirical probability reflects real-world data collection. Celebrated Historical Experiments: (1) Comte de Buffon (18th century): Tossed a coin 4,040 times, recording 2,048 Heads (Empirical P(H) = 2,048 / 4,040 ≈ 0.5069); (2) John Edmund Kerrich (1940s): While interned in Denmark during WWII, tossed a coin 10,000 times, recording 5,067 Heads (Empirical P(H) = 5,067 / 10,000 = 0.5067); (3) Karl Pearson: Tossed a coin 24,000 times, recording 12,012 Heads (Empirical P(H) = 12,012 / 24,000 = 0.5005). As the number of trials increases, empirical probability converges toward the true theoretical value.",
        "key_points": [
            "Empirical Probability Formula: P(E) = (Number of trials in which E happened) / (Total trials n).",
            "Data-Driven: Based strictly on recorded historical data, observations, or laboratory experiments.",
            "Sample Size Dependency: In small samples (e.g. n = 10), empirical probability can deviate significantly from 0.5.",
            "Historical Milestones: Buffon (4,040 tosses → 0.5069), Kerrich (10,000 tosses → 0.5067), Pearson (24,000 tosses → 0.5005).",
            "Practical Application: Indispensable when theoretical symmetry is absent (e.g., weather forecasting, medical drug trials)."
        ],
        "narration": "How do we find probabilities when we cannot calculate them purely from geometry or symmetry? We perform experiments! Empirical probability is the relative frequency: the number of times an event actually happened divided by the total number of trials. During World War Two, the mathematician John Kerrich was trapped in an internment camp. To pass the time, he tossed a coin ten thousand times, recording five thousand and sixty-seven heads! Watch his famous experiment come alive in our simulator as you flip coins and watch the empirical ratio update in real time.",
        "sim_title": "Live Kerrich & Buffon Coin Tossing Experiment & Relative Frequency Tracker",
        "checkpoints": [
            {
                "q": "A coin is tossed 500 times with the following frequencies: Head: 245, Tail: 255. What is the empirical probability of getting a Head?",
                "options": ["0.49", "0.50", "0.51", "0.52"],
                "ans": 0,
                "exp": "Empirical P(Head) = Number of Heads / Total Tosses = 245 / 500 = 49 / 100 = 0.49."
            },
            {
                "q": "In a medical study, 160 out of 200 patients recovered after taking a new medication. What is the empirical probability that a patient will recover?",
                "options": ["0.60", "0.75", "0.80", "0.85"],
                "ans": 2,
                "exp": "Empirical P(Recovery) = Number of recoveries / Total patients = 160 / 200 = 16 / 20 = 4 / 5 = 0.80 (or 80%)."
            }
        ]
    },
    {
        "id": 4,
        "title": "The Law of Large Numbers: Convergence to Theoretical Truth",
        "subtitle": "Jacob Bernoulli’s 1713 Masterpiece — Why Randomness Becomes Orderly at Scale",
        "category": "Empirical Probability",
        "badge": "CG-9 • Law of Large Numbers",
        "summary": "The Law of Large Numbers (LLN), first rigorously proven by Swiss mathematician Jacob Bernoulli in his 1713 treatise Ars Conjectandi, establishes the bridge between empirical observation and theoretical truth. The Theorem: As the number of independent repetitions of a random experiment approaches infinity (n → ∞), the empirical relative frequency of an event approaches its theoretical probability: lim_{n → ∞} P_n(E) = P(E). In a small sample (say, n = 6 coin tosses), getting 5 Heads and 1 Tail (P_n(H) = 0.833) is not uncommon. However, over 10,000 tosses, random fluctuations cancel each other out, squeezing the relative frequency into an infinitesimally narrow band around 0.500. Crucial Warning — The Gambler's Fallacy: The LLN operates through dilution of past anomalies, NOT compensation. A coin has no memory; tossing 5 consecutive Heads does NOT increase the probability of getting Tails on the 6th toss!",
        "key_points": [
            "Bernoulli's Theorem (1713): Relative frequency converges to theoretical probability as sample size n grows large.",
            "Short-Term Chaos vs Long-Term Order: Small samples exhibit high variance; large samples demonstrate stable consistency.",
            "Dilution, Not Compensation: Rare streaks are diluted by thousands of future trials, not corrected by 'due' outcomes.",
            "The Gambler's Fallacy: Falsely believing past random independent outcomes influence future independent trials.",
            "Foundation of Actuarial Science: Enables insurance firms and casinos to operate with near-deterministic financial security."
        ],
        "narration": "Here is the great wonder of probability: individual trials are unpredictable chaos, but millions of trials produce mathematical certainty! This is Jacob Bernoulli's Law of Large Numbers. If you flip a coin four times, you might easily get four heads. But if you flip it ten thousand times, the percentage of heads will stay within a whisker of fifty percent! Beware the gambler's fallacy: the coin has no brain or memory. A streak of heads doesn't mean tails is due next! Watch our convergence graph smooth out into a razor-thin line as you increase the trial count.",
        "sim_title": "Interactive Law of Large Numbers Oscillation & Convergence Graph",
        "checkpoints": [
            {
                "q": "A gambler tosses a fair coin 6 times and gets Heads every single time. What is the probability that the 7th toss will land on Tails?",
                "options": ["1/7", "1/2", "6/7", "Almost 1.0 (Tails is 'due')"],
                "ans": 1,
                "exp": "Each coin toss is an independent event. The coin has no memory of past outcomes. The probability of getting Tails on the 7th toss remains strictly 1/2 (the belief that Tails is 'due' is the Gambler's Fallacy)."
            },
            {
                "q": "According to the Law of Large Numbers, what happens to the difference between empirical relative frequency and theoretical probability as trials n increase?",
                "options": [
                    "The difference increases indefinitely",
                    "The difference remains constant",
                    "The difference approaches zero",
                    "The difference oscillates wildly between 0 and 1"
                ],
                "ans": 2,
                "exp": "As the number of trials n approaches infinity, the empirical relative frequency converges toward the theoretical probability, so their difference approaches 0."
            }
        ]
    },
    {
        "id": 5,
        "title": "Sample Space & Equally Likely Outcomes",
        "subtitle": "Enumerating the Universe of Possibilities (S) and Verifying Physical Symmetry",
        "category": "Theoretical Probability",
        "badge": "C-6.2 • Sample Space",
        "summary": "The Sample Space (denoted by S or Ω) of a random experiment is the complete set of all possible distinct outcomes. The total number of outcomes is denoted by n(S). An Event E is any subset of the sample space (E ⊆ S). Outcomes are said to be Equally Likely if, given the physical symmetry and conditions of the experiment, no outcome has any preference or greater likelihood of occurring over any other. Examples of Equally Likely Outcomes: (1) Tossing a balanced, symmetrical coin: S = {H, T}, with n(S) = 2, where P(H) = P(T) = 1/2; (2) Rolling a fair 6-sided die: S = {1, 2, 3, 4, 5, 6}, with n(S) = 6, where each face has probability 1/6. Counter-Examples (Non-Equally Likely): (a) Dropping a thumbtack: landing point-up vs point-down are not equally likely due to asymmetrical center of mass; (b) A basketball player attempting a free throw (Success vs Failure) depends on skill, not 50/50 symmetry.",
        "key_points": [
            "Sample Space (S): The set containing every possible distinct outcome of a random experiment.",
            "Event Definition: Any subset E ⊆ S; an event occurs if the realized outcome belongs to E.",
            "Equally Likely Condition: All elementary outcomes possess identical probability due to geometric/physical symmetry.",
            "Fair vs Biased: Symmetrical coins/dice yield equally likely outcomes; weighted or asymmetric objects do not.",
            "Prerequisite for Classical Probability: Laplace's theoretical probability formula ONLY applies when outcomes are equally likely!"
        ],
        "narration": "Before we calculate any probability, we must map out the entire universe of what can happen—this set is called the Sample Space, S. For a single coin, S is Heads and Tails. For a six-sided die, S has the numbers one through six. When a die is fair and symmetrical, every single face has the exact same chance of appearing—we say these outcomes are equally likely. But be careful: dropping a thumbtack or shooting a basketball does NOT have equally likely outcomes! Test fair dice against loaded dice in our sample space lab to see the difference.",
        "sim_title": "Interactive Sample Space Visualizer & Symmetry / Fairness Tester",
        "checkpoints": [
            {
                "q": "Which of the following random experiments produces equally likely outcomes?",
                "options": [
                    "Tossing a fair, balanced, unbiased coin",
                    "A student attempting a true/false exam question without studying",
                    "Dropping a thumbtack to see if it lands point-up or point-down",
                    "A bowler taking a wicket on the next delivery"
                ],
                "ans": 0,
                "exp": "A fair, balanced coin possesses physical and geometric symmetry, ensuring that landing on Heads or Tails has the exact same likelihood (1/2 each)."
            },
            {
                "q": "What is the sample space S when rolling a standard fair six-sided die?",
                "options": [
                    "S = {0, 1, 2, 3, 4, 5, 6}",
                    "S = {1, 2, 3, 4, 5, 6}",
                    "S = {even, odd}",
                    "S = {prime, composite}"
                ],
                "ans": 1,
                "exp": "A standard die has six faces numbered 1, 2, 3, 4, 5, and 6. The complete sample space is S = {1, 2, 3, 4, 5, 6}, with n(S) = 6."
            }
        ]
    },
    {
        "id": 6,
        "title": "Theoretical (Classical) Probability: The Laplace Model",
        "subtitle": "Pierre-Simon Laplace's 1812 Ratio Formulation for Symmetrical Random Systems",
        "category": "Theoretical Probability",
        "badge": "C-6.2 • Classical Probability",
        "summary": "The Theoretical Probability (or Classical Probability) of an event E, formulated by Pierre-Simon Laplace in 1812, is defined as the ratio of the number of outcomes favorable to E to the total number of equally likely outcomes in the sample space S: P(E) = n(E) / n(S) = (Number of outcomes favorable to E) / (Total number of possible equally likely outcomes). Standard Computation Algorithm: (1) Step 1: Write down the complete sample space S and count total outcomes n(S); (2) Step 2: Identify and list all elementary outcomes that satisfy event E and count them: n(E); (3) Step 3: Compute the fraction P(E) = n(E) / n(S) and simplify to lowest terms. Example: When rolling a single fair die (n(S) = 6): (a) Event of getting a prime number E = {2, 3, 5} → n(E) = 3 → P(Prime) = 3/6 = 1/2; (b) Event of getting a number greater than 4 E = {5, 6} → n(E) = 2 → P(X > 4) = 2/6 = 1/3; (c) Event of getting an odd number E = {1, 3, 5} → n(E) = 3 → P(Odd) = 3/6 = 1/2.",
        "key_points": [
            "Laplace's Formula: P(E) = n(E) / n(S); valid ONLY when all outcomes in S are equally likely.",
            "Favorable Outcomes n(E): The count of elementary outcomes that satisfy the defining criteria of event E.",
            "Total Sample Space Size n(S): The total count of all elementary outcomes in the experiment.",
            "Fraction Simplification: Probabilities should be expressed as reduced fractions (e.g., 3/6 → 1/2) or exact decimals.",
            "No Empirical Data Needed: Computed entirely a priori using mathematical reasoning and symmetry before any trial occurs."
        ],
        "narration": "In 1812, the French mathematician Pierre-Simon Laplace gave us the classical formula for probability: P of E equals n of E divided by n of S. That is simply the number of winning outcomes divided by the total number of possible outcomes! Take rolling a die: the total outcomes are six. How many are prime numbers? Two, three, and five—that's three winning outcomes! So the probability is three over six, which simplifies to one half. Use our classical probability tool to select any event on a die or spinner and watch the favorable fraction calculate instantly!",
        "sim_title": "Classical Probability Calculator & Venn Diagram Circle Engine",
        "checkpoints": [
            {
                "q": "A standard fair die is rolled once. What is the theoretical probability of obtaining a prime number?",
                "options": ["1/6", "1/3", "1/2", "2/3"],
                "ans": 2,
                "exp": "Sample space S = {1, 2, 3, 4, 5, 6} (n(S) = 6). Prime numbers in S are {2, 3, 5} (n(E) = 3). Notice 1 is NOT prime! P(Prime) = 3 / 6 = 1/2."
            },
            {
                "q": "A box contains 5 red balls, 3 green balls, and 2 blue balls. A ball is drawn at random. What is the probability that the ball drawn is green?",
                "options": ["3/10", "1/3", "3/8", "1/2"],
                "ans": 0,
                "exp": "Total balls n(S) = 5 + 3 + 2 = 10. Favorable green balls n(E) = 3. Therefore, P(Green) = n(E) / n(S) = 3/10 (or 0.3)."
            }
        ]
    },
    {
        "id": 7,
        "title": "Complementary Events & The Fundamental Sum Property",
        "subtitle": "Event E and 'Not E' (Ē) — The Invariant Conservation Rule P(E) + P(Ē) = 1",
        "category": "Theoretical Probability",
        "badge": "C-6.2 • Complementary Events",
        "summary": "For every event E defined on a sample space S, there exists a unique Complementary Event, denoted by Ē, E', or 'not E'. The complement Ē consists of all outcomes in S that do NOT belong to E. Because an outcome must either belong to E or belong to Ē, but cannot belong to both, E and Ē are mutually exclusive (E ∩ Ē = ∅) and collectively exhaustive (E ∪ Ē = S). The Fundamental Complement Theorem: P(E) + P(Ē) = 1, which provides the indispensable working formulas: P(Ē) = 1 - P(E) and P(E) = 1 - P(Ē). The Power of Complementary Thinking: In many complex multi-stage problems, computing the probability of 'at least one success' directly requires calculating and summing dozens of combinations. By using the complement rule, P(At least one) = 1 - P(None), the problem reduces to a single trivial multiplication! Sum of All Elementary Events: If e_1, e_2, ..., e_k are all the elementary events of a trial, then ∑_{i=1}^k P(e_i) = 1.",
        "key_points": [
            "Complementary Event Definition: Ē ('not E') contains all outcomes in sample space S that are not in E.",
            "The Fundamental Identity: P(E) + P(Ē) = 1; the sum of probabilities of an event and its complement is always 1.",
            "Subtraction Rule: P(Ē) = 1 - P(E); allows instantaneous computation of negative events.",
            "The 'At Least One' Strategy: P(At least one success) = 1 - P(Zero successes); simplifies complex problems.",
            "Elementary Exhaustion: The sum of the probabilities of all elementary outcomes in a sample space equals exactly 1."
        ],
        "narration": "Here is one of the most powerful shortcuts in all of mathematics: the Complement Rule! For any event E, 'not E' is its exact opposite. Either E happens, or not E happens—there is no third option! Therefore, P of E plus P of not E always equals exactly one. If the probability that it rains today is zero point seven, the probability that it does NOT rain is one minus zero point seven, which is zero point three. When faced with a complicated problem like 'at least one', always flip it upside down and find the complement! Test this balance in our complementary pie engine.",
        "sim_title": "Interactive Pie Slice & Complementary Balance Engine",
        "checkpoints": [
            {
                "q": "If the probability of winning a game is 0.68, what is the probability of losing the game (assuming no ties)?",
                "options": ["0.22", "0.32", "0.42", "0.52"],
                "ans": 1,
                "exp": "Losing is the complementary event of winning. P(Losing) = 1 - P(Winning) = 1 - 0.68 = 0.32."
            },
            {
                "q": "A bag contains letters spelling the word 'PROBABILITY'. A letter is chosen at random. What is the probability that the letter chosen is NOT a vowel?",
                "options": ["4/11", "7/11", "5/11", "6/11"],
                "ans": 1,
                "exp": "Total letters in 'PROBABILITY' = 11. Vowels are O, A, I, I (4 vowels). P(Vowel) = 4/11. P(Not a vowel) = 1 - P(Vowel) = 1 - 4/11 = 7/11."
            }
        ]
    },
    {
        "id": 8,
        "title": "Compound Experiments & Two-Way Contingency Tables",
        "subtitle": "Cross-Tabulating Multi-Attribute Categorical Data to Compute Joint and Marginal Chances",
        "category": "Compound Probability",
        "badge": "CG-6 • Contingency Tables",
        "summary": "When an experiment or observational study involves two distinct categorical variables simultaneously, a Two-Way Contingency Table (Cross-Tabulation Table) organizes data into rows and columns. Rows represent levels of Attribute A (e.g., Grade 9 vs Grade 10), columns represent levels of Attribute B (e.g., Preferred Activity: Sports, Music, Coding), and internal cells hold joint frequencies f_{ij}. Key Structural Features: (1) Marginal Totals: The sum of each row represents the marginal total for that row category, and the sum of each column represents the marginal total for that column category; (2) Grand Total (N): The sum of all cell frequencies (or the sum of all row marginals) equals the total population N; (3) Probability Calculations: (a) Joint Probability (both A_i and B_j occur): P(A_i ∩ B_j) = f_{ij} / N; (b) Marginal Probability (any outcome in row A_i): P(A_i) = Row Total / N. Contingency tables are universally used in public health (clinical trials, disease vs exposure) and demographic analytics.",
        "key_points": [
            "Contingency Table Architecture: Rows and columns cross-classify experimental units across two attributes simultaneously.",
            "Joint Frequency Cells: Each internal cell (i, j) represents the count of units possessing BOTH characteristics.",
            "Marginal Totals: Row totals and column totals yield the overall distribution of each single variable independently.",
            "Joint Probability Formula: P(Row i AND Column j) = Cell Count f_{ij} / Grand Total N.",
            "Marginal Probability Formula: P(Row i) = Row Total / Grand Total N; P(Column j) = Column Total / Grand Total N."
        ],
        "narration": "What happens when an experiment has two characteristics at the same time? We use a Two-Way Contingency Table! Imagine surveying two hundred students across Grade Nine and Grade Ten about their favorite activity: Sports, Music, or Coding. Rows show the grades, columns show the activities, and each cell shows how many students fit both criteria. Want to know the probability of picking a Grade Nine student who loves Coding? Just take that specific cell and divide by the grand total! Try editing cell numbers in our interactive studio to see joint and marginal probabilities update live.",
        "sim_title": "Interactive Two-Way Contingency Table Studio & Joint Probability Calculator",
        "checkpoints": [
            {
                "q": "In a school of 100 students, 60 are in Grade 9 (of which 25 play football) and 40 are in Grade 10 (of which 15 play football). If a student is picked at random, what is the probability of selecting a Grade 9 student who plays football?",
                "options": ["0.15", "0.25", "0.40", "0.60"],
                "ans": 1,
                "exp": "Grand total N = 100. Favorable joint count for (Grade 9 AND plays football) = 25. Therefore, Joint P = 25 / 100 = 0.25 (or 1/4)."
            },
            {
                "q": "Referring to the same table of 100 students (25 Grade 9 football players + 15 Grade 10 football players = 40 total football players), what is the probability that a randomly chosen student plays football?",
                "options": ["0.25", "0.35", "0.40", "0.50"],
                "ans": 2,
                "exp": "Total football players (marginal column total) = 25 + 15 = 40. P(Football) = Column Total / Grand Total = 40 / 100 = 0.40."
            }
        ]
    },
    {
        "id": 9,
        "title": "Rolling Two Dice: The 6×6 Grid & Sum Distributions",
        "subtitle": "The 36 Equally Likely Ordered Pairs and the Symmetrical Sum Probability Pyramid",
        "category": "Compound Probability",
        "badge": "C-6.2 • Dice Distributions",
        "summary": "When two standard fair six-sided dice (e.g., a Blue die and a Red die) are rolled simultaneously, the compound sample space S consists of ordered pairs (x, y), where x is the outcome on the first die and y on the second die: S = {(1,1), (1,2), ..., (6,6)}. By the Fundamental Counting Principle, total possible outcomes are n(S) = 6 × 6 = 36. Crucial Distinction: The ordered pair (1, 2) is distinct from (2, 1); order matters! The Sum of the Two Dice (X = x + y) can take any integer value from 2 (minimum: 1+1) to 12 (maximum: 6+6). The Sum Frequency Pyramid: Sum 2: {(1,1)} → 1/36; Sum 3: {(1,2),(2,1)} → 2/36; Sum 4: {(1,3),(2,2),(3,1)} → 3/36; Sum 5: {(1,4),(2,3),(3,2),(4,1)} → 4/36; Sum 6: {(1,5),(2,4),(3,3),(4,2),(5,1)} → 5/36; Sum 7 (Apex Peak): {(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)} → 6/36 = 1/6; Sum 8: 5/36; Sum 9: 4/36; Sum 10: 3/36; Sum 11: 2/36; Sum 12: 1/36. Doublets (identical faces): {(1,1),(2,2),(3,3),(4,4),(5,5),(6,6)} → 6/36 = 1/6.",
        "key_points": [
            "Total Sample Space: n(S) = 6 × 6 = 36 equally likely ordered pairs (x, y).",
            "Order Matters: (1, 5) and (5, 1) are distinct outcomes; treating them as one is a classic error.",
            "Range of Sums: Sum can vary from 2 to 12; distribution is perfectly symmetric around 7.",
            "Most Probable Sum: Sum = 7 has 6 favorable outcomes, giving maximum probability P(Sum 7) = 6/36 = 1/6.",
            "Doublets Probability: Six possible doublets {(1,1), ..., (6,6)}, giving P(Doublet) = 6/36 = 1/6."
        ],
        "narration": "When you roll two dice together, how many outcomes are possible? Six times six equals thirty-six! Always remember: rolling a one on the first die and a six on the second is completely distinct from rolling a six first and a one second. Look at the thirty-six cells in our grid. If you sum the two numbers, seven is the champion! There are six different ways to roll a seven, making it the most likely sum with a probability of one in six. Click any sum in our six-by-six matrix to light up its diagonal line and view its exact probability!",
        "sim_title": "Interactive 6×6 Dual Dice Matrix & Symmetrical Sum Pyramid",
        "checkpoints": [
            {
                "q": "Two fair dice are rolled simultaneously. What is the probability of getting a doublet (both dice showing the same number)?",
                "options": ["1/36", "1/12", "1/6", "1/4"],
                "ans": 2,
                "exp": "Doublets are {(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)}, giving 6 favorable outcomes out of 36. P(Doublet) = 6/36 = 1/6."
            },
            {
                "q": "What is the probability of obtaining a sum of 9 when rolling two fair dice?",
                "options": ["1/9", "1/12", "5/36", "1/6"],
                "ans": 0,
                "exp": "Favorable outcomes for sum 9 are: (3,6), (4,5), (5,4), (6,3) → 4 outcomes. P(Sum 9) = 4 / 36 = 1/9."
            }
        ]
    },
    {
        "id": 10,
        "title": "Tossing Multiple Coins: Systematic Encodings & Binomial Trees",
        "subtitle": "Binary Exponential Growth 2^k and Overcoming D'Alembert's Historical Fallacy",
        "category": "Compound Probability",
        "badge": "CG-9 • Binary Trees",
        "summary": "When multiple coins are tossed (or one coin is tossed repeatedly k times), the total number of outcomes grows exponentially as n(S) = 2^k. (1) One Coin (k=1): S = {H, T}, n(S) = 2^1 = 2; (2) Two Coins (k=2): S = {HH, HT, TH, TT}, n(S) = 2^2 = 4. Notice that HT (Head first, Tail second) and TH (Tail first, Head second) are two distinct outcomes! D'Alembert's Famous Mistake (1754): The French encyclopedist Jean le Rond d'Alembert argued that tossing two coins has only 3 outcomes (Two Heads, Two Tails, One of Each) and claimed each had probability 1/3. He failed to see that 'One of Each' encompasses TWO distinct ordered outcomes {HT, TH}, making its true probability 2/4 = 1/2!; (3) Three Coins (k=3): S = {HHH, HHT, HTH, HTT, THH, THT, TTH, TTT}, n(S) = 2^3 = 8. The distribution of heads follows Pascal's triangle coefficients: 0 Heads (1), 1 Head (3), 2 Heads (3), 3 Heads (1).",
        "key_points": [
            "Exponential Sample Space: For k coins, total sample space size is n(S) = 2^k.",
            "Two Coins: S = {HH, HT, TH, TT} (4 outcomes). P(Exactly 1 Head) = 2/4 = 1/2.",
            "Three Coins: S = {HHH, HHT, HTH, HTT, THH, THT, TTH, TTT} (8 outcomes).",
            "D'Alembert's Error (1754): Erroneously treated {HT, TH} as a single outcome, claiming P = 1/3 instead of 1/2.",
            "Pascal's Triangle Connection: Outcome combinations for k coins match row k of Pascal's triangle (e.g. 1, 3, 3, 1 for k=3)."
        ],
        "narration": "Flip one coin: two outcomes. Flip two coins: four outcomes. Flip three coins: eight outcomes! Every coin doubles the possibilities—two to the power of k. In 1754, the famous French philosopher Jean d'Alembert made a legendary blunder: he claimed that tossing two coins had only three outcomes: two heads, two tails, or one of each, so each was one-third. But he forgot that 'one of each' can happen two ways: head-tail OR tail-head! So the true probability is two out of four, or one half! Explore all two to the k branches in our coin permutation tree.",
        "sim_title": "Multi-Coin Permutation Explorer & Pascal Pyramid Visualizer",
        "checkpoints": [
            {
                "q": "Three unbiased coins are tossed together. What is the probability of getting exactly two Heads?",
                "options": ["1/8", "1/4", "3/8", "1/2"],
                "ans": 2,
                "exp": "Total outcomes n(S) = 2³ = 8. Favorable outcomes with exactly 2 Heads are: {HHT, HTH, THH} (3 outcomes). P(Exactly 2 Heads) = 3/8."
            },
            {
                "q": "Two coins are tossed simultaneously. What is the probability of getting at least one Head?",
                "options": ["1/4", "1/2", "3/4", "1"],
                "ans": 2,
                "exp": "Sample space S = {HH, HT, TH, TT} (4 outcomes). Favorable outcomes with at least one Head are {HH, HT, TH} (3 outcomes). Alternatively: P(At least 1 H) = 1 - P(0 H) = 1 - P(TT) = 1 - 1/4 = 3/4."
            }
        ]
    },
    {
        "id": 11,
        "title": "Tree Diagrams: Multi-Stage Sequential Pathways",
        "subtitle": "Visualising Successive Stages with Branch Multiplication and Terminal Path Addition",
        "category": "Compound Probability",
        "badge": "C-6.2 • Tree Diagrams",
        "summary": "A Tree Diagram is a powerful graphic tool used to systematically break down and calculate probabilities for multi-stage sequential random experiments. It begins at a single root node and branches outward into chronological decision or chance stages. Foundational Principles of Tree Diagrams: (1) Branch Probabilities: Each branch emanating from a node is labeled with its respective conditional probability; the sum of probabilities of all branches leaving any single node MUST equal exactly 1; (2) The Multiplication Principle (Along a Branch Pathway): The probability of traversing a complete path from root to a specific terminal leaf node equals the product of the probabilities along all segments of that branch pathway: P(Path) = P(Stage 1) × P(Stage 2 | Stage 1); (3) The Addition Principle (Across Alternative Terminal Pathways): To find the probability of a compound event comprising multiple distinct terminal leaf nodes, sum the individual probabilities of those pathways: P(E) = ∑ P(Path_i); (4) The Sum of All Terminal Leaf Probabilities across the entire tree is always identically 1.0.",
        "key_points": [
            "Structure: Root node branches outward sequentially through successive temporal stages.",
            "Node Conservation: Probabilities on all branches exiting any single junction must sum to 1.",
            "Multiplication Along Paths: P(Branch 1 AND Branch 2) = P(Branch 1) × P(Branch 2).",
            "Addition Across Paths: P(Event E) = Sum of all individual path probabilities that satisfy E.",
            "Total Tree Conservation: The sum of all terminal pathway probabilities across the tree equals 1.000."
        ],
        "narration": "When an experiment happens in steps—like weather today followed by the outcome of tomorrow's soccer match—a Tree Diagram is your best friend! Start at the root and trace each possibility along its branches. Here is the golden rule: multiply along the path to find the probability of that sequence, and add across the endpoints to combine different paths! Notice that the probabilities leaving any branch point must sum to one. Use our interactive tree builder to adjust branch odds and watch terminal probabilities compute automatically!",
        "sim_title": "Interactive Multi-Stage Tree Diagram Builder & Path Multiplier",
        "checkpoints": [
            {
                "q": "On a tree diagram, if Stage 1 branches into Path A with probability 0.4, and from Path A Stage 2 branches into Path B with probability 0.3, what is the probability of the combined path (A and B)?",
                "options": ["0.12", "0.70", "0.35", "0.012"],
                "ans": 0,
                "exp": "By the multiplication principle along a path: P(A and B) = P(A) × P(B) = 0.4 × 0.3 = 0.12."
            },
            {
                "q": "What must the sum of probabilities on all branches emanating from any single node in a valid probability tree equal?",
                "options": ["0", "0.5", "1.0", "Depends on the number of branches"],
                "ans": 2,
                "exp": "The branches leaving any single node represent a complete, mutually exclusive and exhaustive set of outcomes for that stage; hence their probabilities must sum to exactly 1.0."
            }
        ]
    },
    {
        "id": 12,
        "title": "Sampling With vs Without Replacement",
        "subtitle": "Independent Stationary Trials vs Dependent Dynamic Depletion in Finite Populations",
        "category": "Compound Probability",
        "badge": "CG-9 • Replacement Dynamics",
        "summary": "When selecting multiple items sequentially from a finite population (such as drawing marbles from an urn or cards from a deck), the experimental protocol fundamentally dictates whether successive trials are independent or dependent: (1) Sampling WITH Replacement: After each draw, the selected item is inspected, recorded, and returned to the container before the next draw. Characteristics: (a) The total population size N and composition remain identical on every draw; (b) Successive draws are strictly Independent Events: P(2nd draw) is completely unaffected by the 1st draw; (2) Sampling WITHOUT Replacement: Once an item is drawn, it is set aside and NOT returned. Characteristics: (a) Both the total population count (N decreases to N - 1) and the count of the chosen category decrease by 1; (b) Successive draws are Dependent Events. Classical Urn Example: An urn contains 5 Red and 3 Blue marbles (Total N = 8): (i) With Replacement: P(Two Reds) = (5/8) × (5/8) = 25/64 ≈ 0.3906; (ii) Without Replacement: P(Two Reds) = (5/8) × (4/7) = 20/56 = 5/14 ≈ 0.3571.",
        "key_points": [
            "With Replacement (Independent): Item is returned; sample size N and category proportions stay constant.",
            "Without Replacement (Dependent): Item is removed; both total size N and category count decrease by 1.",
            "Urn Formula (With): P(Red then Red) = (R / N) × (R / N).",
            "Urn Formula (Without): P(Red then Red) = (R / N) × ((R - 1) / (N - 1)).",
            "Industrial Application: Quality control batch testing (testing a fuse destroys it, mandating without-replacement sampling)."
        ],
        "narration": "Pay close attention to these three words: 'with' or 'without' replacement! If you pull a marble from a bag, look at it, and put it back, the bag stays unchanged for the next turn—that's independent sampling with replacement. But if you keep the marble in your pocket, the bag now has one fewer marble! The odds for the next turn have changed. In quality control testing, if testing a light bulb destroys it, you can never put it back! Toggle between with and without replacement in our urn simulator to watch the fractions update dynamically.",
        "sim_title": "Interactive Marbles Urn: Replacement Switcher & Dependency Engine",
        "checkpoints": [
            {
                "q": "A bag contains 6 red balls and 4 blue balls (total 10). Two balls are drawn successively WITHOUT replacement. What is the probability that both balls drawn are red?",
                "options": ["36/100 (9/25)", "30/100 (3/10)", "30/90 (1/3)", "24/90 (4/15)"],
                "ans": 2,
                "exp": "First draw: P(1st Red) = 6/10. Since it is NOT replaced, 9 balls remain with 5 red balls. Second draw: P(2nd Red) = 5/9. Combined P = (6/10) × (5/9) = 30/90 = 1/3."
            },
            {
                "q": "If the same two balls are drawn WITH replacement (each ball returned before the next draw), what is the probability that both balls are red?",
                "options": ["9/25", "1/3", "4/15", "1/2"],
                "ans": 0,
                "exp": "With replacement, both draws are independent with 6 red out of 10 total. P = (6/10) × (6/10) = 36/100 = 9/25 (or 0.36)."
            }
        ]
    },
    {
        "id": 13,
        "title": "Standard 52-Card Deck: Anatomy & Combinatorial Chances",
        "subtitle": "Deconstructing Suits, Ranks, Court Face Cards, and Compound Selection Rules",
        "category": "Compound Probability",
        "badge": "C-6.2 • Playing Cards",
        "summary": "A standard deck of playing cards contains exactly 52 cards divided into 4 suits of 13 cards each, providing a rich, symmetrical discrete sample space (n(S) = 52). Complete Anatomical Breakdown: (1) Colors: 26 Red Cards (13 Hearts ♥, 13 Diamonds ♦) and 26 Black Cards (13 Spades ♠, 13 Clubs ♣); (2) Ranks per Suit: Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King; (3) Face Cards (Court Cards): Kings, Queens, and Jacks possess illustrated human faces: 3 per suit × 4 suits = 12 Face Cards total (6 Red Face Cards, 6 Black Face Cards); (4) Number (Pip) Cards: 2 through 10 = 9 ranks × 4 suits = 36 Number Cards total; (5) Aces: Exactly 4 Aces in the deck (2 Red Aces, 2 Black Aces; an Ace is NOT a face card); (6) Key Probability Landmarks: (a) P(Ace) = 4/52 = 1/13; (b) P(Face Card) = 12/52 = 3/13; (c) P(Red King) = 2/52 = 1/26; (d) P(Black Card or a Queen) = (26 + 2) / 52 = 28/52 = 7/13.",
        "key_points": [
            "Deck Total: n(S) = 52 cards; partitioned into 26 Red (Hearts, Diamonds) and 26 Black (Spades, Clubs).",
            "Suits: 4 suits (Spades ♠, Clubs ♣, Hearts ♥, Diamonds ♦), each containing exactly 13 cards.",
            "Face Cards (Court Cards): Exactly 12 cards (4 Kings, 4 Queens, 4 Jacks); 6 are red and 6 are black.",
            "Aces: Exactly 4 Aces in the deck (not classified as face cards).",
            "Non-Face Cards: 52 - 12 = 40 cards (36 number cards + 4 aces)."
        ],
        "narration": "Playing cards have been the mathematician's favorite playground for centuries! A standard deck has exactly fifty-two cards, split fifty-fifty into twenty-six red cards and twenty-six black cards. There are four suits: hearts, diamonds, spades, and clubs. Each suit has thirteen cards. The twelve cards with human pictures—kings, queens, and jacks—are called Face Cards. Note that an ace is NOT a face card! If you draw one card at random, the chance of a face card is twelve out of fifty-two, or three in thirteen. Explore our full fifty-two card interactive table to illuminate any card combination!",
        "sim_title": "Interactive 52-Card Deck Grid & Probability Filter Engine",
        "checkpoints": [
            {
                "q": "One card is drawn from a well-shuffled deck of 52 cards. What is the probability of getting a face card?",
                "options": ["1/13", "3/13", "4/13", "12/52"],
                "ans": 1,
                "exp": "There are 12 face cards (4 Jacks, 4 Queens, 4 Kings) in a 52-card deck. P(Face Card) = 12 / 52 = 3/13."
            },
            {
                "q": "What is the probability of drawing either a King or a Queen from a standard deck of 52 cards?",
                "options": ["1/13", "2/13", "1/26", "4/13"],
                "ans": 1,
                "exp": "There are 4 Kings and 4 Queens in the deck, giving 4 + 4 = 8 favorable cards. P(King or Queen) = 8 / 52 = 2/13."
            }
        ]
    },
    {
        "id": 14,
        "title": "Geometric (Continuous) Probability: Length & Area Models",
        "subtitle": "Extending Probability from Discrete Counting to Continuous Metric Spaces",
        "category": "Continuous Probability",
        "badge": "CG-9 • Geometric Probability",
        "summary": "In many physical scenarios, outcomes cannot be counted discretely because the sample space is an uncountably infinite continuum of points in space or time. In such cases, we use Geometric (Continuous) Probability, where probability is proportional to geometric measure (length, area, or volume): (1) 1-Dimensional Length Model: For a point chosen uniformly at random along a line segment L, the probability that it falls inside sub-segment l is: P(E) = Length(l) / Length(L); (2) 2-Dimensional Area Model: For a point landing uniformly at random inside a planar region of total area A, the probability that it lands inside a specific target sub-region of area a is: P(E) = Area(a) / Area(A). Classical Target Example: A circular dartboard has radius R (Area = πR²). A circular bullseye at the center has radius r (Area = πr²). If a dart hits the board at random, P(Hitting Bullseye) = (πr²) / (πR²) = (r / R)². Notice that the constant π cancels out, leaving pure quadratic scaling of the radius ratio!",
        "key_points": [
            "Continuous Measure: Used when outcomes form an uncountably infinite continuum (time intervals, spatial areas).",
            "1D Length Formula: P(E) = Length of favorable interval / Total length of sample space interval.",
            "2D Area Formula: P(E) = Area of target region / Total area of sample space region.",
            "Dartboard Principle: P(Bullseye) = (πr²) / (πR²) = (r/R)²; independent of units or scaling.",
            "Uniform Density Assumption: Assumes points land with uniform, equal likelihood across every unit of area."
        ],
        "narration": "What if you are throwing a dart at a circular target? You can't count individual points because there are infinite points on the board! This brings us to Geometric Probability. Instead of counting outcomes, we measure lengths and areas! The probability of hitting the bullseye is simply the area of the small bullseye circle divided by the total area of the entire board. Notice that pi cancels out completely—the probability depends purely on the square of the radius ratio! Try throwing virtual darts in our interactive archery simulator to watch continuous geometric probability in action.",
        "sim_title": "Interactive Archery Dartboard & Geometric Area Calculator",
        "checkpoints": [
            {
                "q": "A dart is thrown at a square board of side 20 cm. Inside the board is a circular bullseye of radius 7 cm. What is the probability that the dart lands inside the circular bullseye? (Use π = 22/7)",
                "options": ["0.250", "0.385", "0.450", "0.500"],
                "ans": 1,
                "exp": "Area of square board = 20 × 20 = 400 cm². Area of circular bullseye = πr² = (22/7) × 7 × 7 = 154 cm². P(Bullseye) = 154 / 400 = 0.385 (or 38.5%)."
            },
            {
                "q": "A phone call arrives uniformly at random between 2:00 PM and 3:00 PM (a 60-minute window). What is the probability that the call arrives between 2:15 PM and 2:35 PM?",
                "options": ["1/4", "1/3", "1/2", "2/5"],
                "ans": 1,
                "exp": "Total interval length = 60 minutes. Favorable interval length = 2:35 - 2:15 = 20 minutes. P = 20 / 60 = 1/3."
            }
        ]
    },
    {
        "id": 15,
        "title": "Computational Thinking: Monte Carlo Simulations & Random Seeds",
        "subtitle": "Stanislaw Ulam & John von Neumann’s Algorithmic Revolution — Solving Equations by Chance",
        "category": "Computational Thinking",
        "badge": "CG-9 • Monte Carlo",
        "summary": "In computational science, Monte Carlo Methods are algorithms that solve deterministic mathematical and physical problems through massive repeated pseudo-random sampling. Invented during the Manhattan Project by Stanislaw Ulam and John von Neumann (named after the Monte Carlo Casino in Monaco), these methods harness computational thinking: (1) Estimating Pi (π) by Chance: Inscribe a quarter circle of radius r inside a square of side r. Area of quarter circle = (π r²) / 4; Area of square = r². The theoretical ratio of areas is π / 4. A computer generates N pairs of random coordinates (x, y) uniformly distributed between 0 and 1. By the Pythagorean theorem, a point lies inside the circle if x² + y² ≤ 1. If N_in points land inside the curve, then N_in / N ≈ π / 4, yielding the computational formula: π ≈ 4 × (N_in / N); (2) Pseudo-Random Number Generators (PRNGs): Computers generate deterministic sequences of numbers that mimic statistical randomness using algorithmic seeds.",
        "key_points": [
            "Monte Carlo Concept: Solving complex deterministic problems through massive repeated random computational sampling.",
            "Estimating Pi Formula: π ≈ 4 × (Points inside quarter circle N_in) / (Total random points N).",
            "Pythagorean In-Circle Test: An (x, y) coordinate pair lies inside the quarter circle if and only if x² + y² ≤ 1.",
            "Algorithmic Convergence: Accuracy improves proportional to 1 / √N; running 100,000 trials yields high precision.",
            "Modern Applications: Spacecraft orbital modeling, climate change projections, financial portfolio risk analysis."
        ],
        "narration": "Can you calculate the digits of Pi just by throwing thousands of random darts? Yes! During the Manhattan Project, mathematicians Stanislaw Ulam and John von Neumann invented the Monte Carlo method. Imagine a square with a quarter circle inside it. The ratio of their areas is pi over four! A computer tosses thousands of random points into the square. Test whether each point falls inside the curve using x squared plus y squared less than or equal to one. Four times the inside fraction gives you pi! Click our simulator to fire thousands of random points and watch pi emerge before your eyes.",
        "sim_title": "Interactive Monte Carlo Pi Estimator & Dartboard Simulation",
        "checkpoints": [
            {
                "q": "In a Monte Carlo simulation to estimate π, 1,000 random points are generated inside a unit square. Exactly 785 points fall inside the quarter circle (x² + y² ≤ 1). What is the estimated value of π?",
                "options": ["3.00", "3.14", "3.20", "3.28"],
                "ans": 1,
                "exp": "Monte Carlo formula: π ≈ 4 × (N_in / N_total) = 4 × (785 / 1000) = 4 × 0.785 = 3.14."
            },
            {
                "q": "Why do computers use 'Pseudo-Random' Number Generators (PRNGs) rather than purely physical random generators for scientific simulations?",
                "options": [
                    "They are slower than physical coin tossing",
                    "They allow simulations to be precisely reproduced and debugged using the same random seed",
                    "They always produce the number 0",
                    "They cannot handle decimal numbers"
                ],
                "ans": 1,
                "exp": "PRNGs use mathematical algorithms with a seed value, ensuring that scientific simulations can be identically reproduced, verified, and debugged by other researchers."
            }
        ]
    },
    {
        "id": 16,
        "title": "Probability in Real Life: Risk Analysis, Weather & Decision Trees",
        "subtitle": "Navigating Atmospheric Forecasting, Medical Diagnostics, and Expected Monetary Value",
        "category": "Decision-Making Strategy",
        "badge": "C-6.2 • Real-World Risk",
        "summary": "Probability is the premier decision-making instrument used by actuaries, meteorologists, doctors, and financial analysts to evaluate risk under uncertainty: (1) Weather Forecasting: A '70% chance of rain' does not mean it will rain over 70% of the city, nor that it will rain for 70% of the day. It means that given identical atmospheric pressure and humidity measurements in historical records, precipitation occurred on 70 out of 100 occasions; (2) Medical Diagnostics & False Positives: A diagnostic test with 99% accuracy can still yield surprising results in rare diseases due to base-rate probabilities; (3) Expected Monetary Value (EMV): In business investments, Expected Value represents the long-run average outcome: EV = ∑ (P_i × V_i), where P_i is the probability and V_i is the financial payoff of outcome i; (4) Insurance Actuarial Science: Premiums are calculated by multiplying probability of damage by repair costs plus administrative margins.",
        "key_points": [
            "Meteorology Definition: '70% probability of rain' means rain occurred in 70 of 100 historically identical atmospheric states.",
            "Expected Value Formula: EV = ∑ (Probability P_i × Monetary Value V_i); guides rational risk-reward decisions.",
            "Insurance Pricing: Actuaries price premiums by matching expected payout liabilities: Premium = P(Accident) × Claim Cost.",
            "Medical Diagnostic Risk: Evaluating test sensitivity vs disease prevalence to prevent misinterpreting false positives.",
            "Synthesis of Unit: Probability equips citizens to replace emotional superstition with rigorous, evidence-based reasoning."
        ],
        "narration": "When the morning news says there is a seventy percent chance of rain, what does that actually mean? It means out of one hundred days in history with the exact same temperature, pressure, and humidity, it rained seventy times! Insurance companies use probability to set car policy prices, doctors use it to interpret diagnostic tests, and financial investors use it to calculate Expected Value. Probability is not just an exam topic—it is your intellectual armor against superstition and misleading claims! Explore our real-world decision tree in the simulator.",
        "sim_title": "Interactive Real-World Decision Tree & Risk Payoff Analyzer",
        "checkpoints": [
            {
                "q": "An investor faces a venture with two possible outcomes: a 60% chance of making ₹50,000 profit and a 40% chance of losing ₹20,000. What is the Expected Monetary Value (EV) of this venture?",
                "options": ["₹18,000", "₹22,000", "₹26,000", "₹30,000"],
                "ans": 1,
                "exp": "EV = (P_1 × V_1) + (P_2 × V_2) = (0.60 × ₹50,000) + (0.40 × -₹20,000) = ₹30,000 - ₹8,000 = ₹22,000."
            },
            {
                "q": "What does a weather meteorologist mean when stating an '80% Probability of Precipitation'?",
                "options": [
                    "It will rain continuously for 80% of the day",
                    "80% of the geographic area will be covered in water",
                    "In 100 historical days with identical atmospheric indicators, rain was recorded on 80 days",
                    "There is an 80% chance the meteorologist made a mistake"
                ],
                "ans": 2,
                "exp": "Probability of precipitation reflects historical frequency: under the exact atmospheric conditions observed today, rain occurred on 80 out of 100 occasions in meteorological records."
            }
        ]
    }
]

QUIZZES = [
    {
        "id": 1,
        "title": "Mastery Challenge 1: Probability Scale, Empirical Trials & LLN",
        "badge": "Quiz 1 • Foundations & Scale",
        "questions": [
            {
                "q": "1. Which of the following values can NEVER be the probability of an event?",
                "options": ["0.001", "4/5", "-0.2", "1.0"],
                "ans": 2,
                "solution": "Step 1: By the fundamental probability axiom, the probability of any event E satisfies 0 ≤ P(E) ≤ 1.\nStep 2: A negative number such as -0.2 violates this rule.\nStep 3: Therefore, -0.2 cannot represent a probability."
            },
            {
                "q": "2. In a statistical experiment, a tire manufacturing company tracked 1,000 tires before they needed replacement: 20 tires lasted < 4,000 km, 210 lasted 4,000 to 9,000 km, 325 lasted 9,001 to 14,000 km, and 445 lasted > 14,000 km. What is the empirical probability that a tire will last more than 9,000 km?",
                "options": ["0.445", "0.535", "0.770", "0.980"],
                "ans": 2,
                "solution": "Step 1: Tires lasting > 9,000 km include the (9,001 to 14,000 km) bracket and the (> 14,000 km) bracket.\nStep 2: Favorable count = 325 + 445 = 770 tires.\nStep 3: Total tires = 1,000.\nStep 4: Empirical P = 770 / 1,000 = 0.770 (or 77%)."
            },
            {
                "q": "3. The probability of an event that is certain to occur is:",
                "options": ["0", "0.5", "1", "Infinity"],
                "ans": 2,
                "solution": "Step 1: A certain (or sure) event is guaranteed to happen in every single trial.\nStep 2: Its favorable outcomes equal the entire sample space: n(E) = n(S).\nStep 3: P(E) = n(S) / n(S) = 1."
            },
            {
                "q": "4. A coin is tossed 1,000 times and Head occurs 455 times. What is the empirical probability of getting a Tail?",
                "options": ["0.455", "0.500", "0.545", "0.555"],
                "ans": 2,
                "solution": "Step 1: Number of Tails = Total tosses - Number of Heads = 1,000 - 455 = 545.\nStep 2: Empirical P(Tail) = 545 / 1,000 = 0.545."
            },
            {
                "q": "5. According to the Law of Large Numbers, as the number of trials in a coin-tossing experiment increases toward infinity, the relative frequency of heads:",
                "options": [
                    "Approaches 1.0",
                    "Approaches 0.5",
                    "Oscillates uncontrollably",
                    "Approaches 0"
                ],
                "ans": 1,
                "solution": "Step 1: The Law of Large Numbers states that empirical relative frequency converges to theoretical probability as n → ∞.\nStep 2: For a fair coin, theoretical P(Head) = 0.5.\nStep 3: Hence, the relative frequency converges to 0.5."
            },
            {
                "q": "6. A player rolls a fair six-sided die 5 times and gets a '6' on every single roll. What is the probability of getting a '6' on the 6th roll?",
                "options": ["1/6", "1/36", "5/6", "(1/6)⁶"],
                "ans": 0,
                "solution": "Step 1: Each roll of a fair die is an independent event.\nStep 2: The die has no physical mechanism or memory of prior outcomes.\nStep 3: The probability on the 6th roll remains exactly 1/6."
            },
            {
                "q": "7. In a survey of 364 children aged 19-36 months, 91 were found to be receiving supplementary nutrition. What is the empirical probability that a randomly chosen child is NOT receiving supplementary nutrition?",
                "options": ["0.25", "0.50", "0.75", "0.80"],
                "ans": 2,
                "solution": "Step 1: Children receiving nutrition = 91. P(Receiving) = 91 / 364 = 1/4 = 0.25.\nStep 2: Children NOT receiving nutrition = 364 - 91 = 273.\nStep 3: P(Not receiving) = 273 / 364 = 3/4 = 0.75."
            },
            {
                "q": "8. If an event has a probability of 0.005, its likelihood is best described qualitatively as:",
                "options": ["Impossible", "Highly Unlikely", "Even Chance", "Likely"],
                "ans": 1,
                "solution": "Step 1: P = 0 corresponds to Impossible.\nStep 2: P = 0.005 is strictly greater than 0 but extremely close to 0 (0.5% chance).\nStep 3: It is best described as 'Highly Unlikely'."
            },
            {
                "q": "9. In John Kerrich's famous 10,000 coin tosses during WWII, he recorded 5,067 Heads. What was his observed empirical probability of Heads?",
                "options": ["0.5000", "0.5067", "0.5670", "0.4933"],
                "ans": 1,
                "solution": "Step 1: Empirical P = Favorable outcomes / Total trials.\nStep 2: P = 5,067 / 10,000 = 0.5067."
            },
            {
                "q": "10. An experiment has only two possible outcomes, A and B. If P(A) = 0.63, what is P(B)?",
                "options": ["0.27", "0.37", "0.47", "0.63"],
                "ans": 1,
                "solution": "Step 1: Since A and B are the only outcomes, they are complementary: P(A) + P(B) = 1.\nStep 2: P(B) = 1 - P(A) = 1 - 0.63 = 0.37."
            }
        ]
    },
    {
        "id": 2,
        "title": "Mastery Challenge 2: Theoretical Probability, Sample Spaces & Complements",
        "badge": "Quiz 2 • Theoretical & Complements",
        "questions": [
            {
                "q": "11. A single fair die is rolled. What is the theoretical probability of getting a number strictly greater than 2?",
                "options": ["1/3", "1/2", "2/3", "5/6"],
                "ans": 2,
                "solution": "Step 1: Sample space S = {1, 2, 3, 4, 5, 6} (n(S) = 6).\nStep 2: Favorable outcomes strictly > 2 are {3, 4, 5, 6} (4 outcomes).\nStep 3: P(X > 2) = 4/6 = 2/3."
            },
            {
                "q": "12. In a lottery, there are 10 prizes and 25 blank tickets. What is the probability of winning a prize when drawing one ticket at random?",
                "options": ["10/25", "2/7", "5/7", "10/35"],
                "ans": 1,
                "solution": "Step 1: Total tickets n(S) = 10 (prizes) + 25 (blanks) = 35.\nStep 2: Favorable winning tickets n(E) = 10.\nStep 3: P(Winning) = 10 / 35 = 2/7."
            },
            {
                "q": "13. If P(E) = 0.05, what is the probability of the complementary event 'not E' (P(Ē))?",
                "options": ["0.05", "0.50", "0.90", "0.95"],
                "ans": 3,
                "solution": "Step 1: Complement rule: P(Ē) = 1 - P(E).\nStep 2: P(Ē) = 1 - 0.05 = 0.95."
            },
            {
                "q": "14. A bag contains 3 red balls, 5 black balls, and 4 white balls. A ball is drawn at random. What is the probability that the ball drawn is NOT black?",
                "options": ["5/12", "7/12", "1/2", "3/4"],
                "ans": 1,
                "solution": "Step 1: Total balls n(S) = 3 + 5 + 4 = 12.\nStep 2: Black balls = 5 → P(Black) = 5/12.\nStep 3: P(Not black) = 1 - P(Black) = 1 - 5/12 = 7/12 (or (3 red + 4 white)/12 = 7/12)."
            },
            {
                "q": "15. A number x is chosen at random from the numbers -3, -2, -1, 0, 1, 2, 3. What is the probability that |x| < 2?",
                "options": ["2/7", "3/7", "4/7", "5/7"],
                "ans": 1,
                "solution": "Step 1: Sample space has 7 numbers: {-3, -2, -1, 0, 1, 2, 3} (n(S) = 7).\nStep 2: |x| < 2 means -2 < x < 2.\nStep 3: Favorable values are {-1, 0, 1} (3 numbers).\nStep 4: P(|x| < 2) = 3/7."
            },
            {
                "q": "16. Which of the following conditions is required for Laplace's classical formula P(E) = n(E) / n(S) to be valid?",
                "options": [
                    "The number of trials must be greater than 1,000",
                    "All outcomes in the sample space must be equally likely",
                    "The sample space must be infinite",
                    "The probability of E must equal 0.5"
                ],
                "ans": 1,
                "solution": "Step 1: Laplace's ratio definition relies fundamentally on symmetry.\nStep 2: It is mathematically valid if and only if all elementary outcomes in S are equally likely."
            },
            {
                "q": "17. A letter is chosen at random from the word 'MATHEMATICS'. What is the probability that the letter chosen is 'M'?",
                "options": ["1/11", "2/11", "3/11", "4/11"],
                "ans": 1,
                "solution": "Step 1: Total letters in 'MATHEMATICS' = 11 (M-A-T-H-E-M-A-T-I-C-S).\nStep 2: The letter 'M' appears 2 times.\nStep 3: P('M') = 2/11."
            },
            {
                "q": "18. A box contains 90 discs numbered 1 to 90. If one disc is drawn at random, what is the probability that it bears a perfect square number?",
                "options": ["1/10", "9/90", "1/9", "8/90"],
                "ans": 0,
                "solution": "Step 1: Total discs n(S) = 90.\nStep 2: Perfect squares from 1 to 90 are: 1, 4, 9, 16, 25, 36, 49, 64, 81 (9 numbers: 1² through 9²).\nStep 3: P(Perfect Square) = 9 / 90 = 1/10 (or 0.1)."
            },
            {
                "q": "19. The sum of the probabilities of all elementary events of an experiment is:",
                "options": ["0", "0.5", "1", "Depends on the number of events"],
                "ans": 2,
                "solution": "Step 1: Elementary events partition the sample space completely without overlap.\nStep 2: By the axiom of total probability, ∑ P(e_i) = P(S) = 1."
            },
            {
                "q": "20. What is the probability of rolling a number less than or equal to 6 on a standard six-sided die?",
                "options": ["5/6", "1", "0", "6/5"],
                "ans": 1,
                "solution": "Step 1: All faces on a die are {1, 2, 3, 4, 5, 6}.\nStep 2: Every single face satisfies 'less than or equal to 6' (6 favorable outcomes).\nStep 3: P = 6/6 = 1 (this is a Certain Event)."
            }
        ]
    },
    {
        "id": 3,
        "title": "Mastery Challenge 3: Dice, Coins, Tree Diagrams & Cards",
        "badge": "Quiz 3 • Compound Systems",
        "questions": [
            {
                "q": "21. Two fair dice are rolled simultaneously. What is the probability that the sum of the numbers appearing on the two dice is 7?",
                "options": ["1/12", "1/6", "5/36", "7/36"],
                "ans": 1,
                "solution": "Step 1: Total outcomes for two dice n(S) = 6 × 6 = 36.\nStep 2: Outcomes with sum 7 are: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) → 6 outcomes.\nStep 3: P(Sum 7) = 6/36 = 1/6."
            },
            {
                "q": "22. Two fair dice are rolled. What is the probability that the sum of the numbers is at least 10?",
                "options": ["1/6", "1/12", "5/36", "1/4"],
                "ans": 0,
                "solution": "Step 1: 'At least 10' means sum = 10, 11, or 12.\nStep 2: Sum 10: (4,6), (5,5), (6,4) [3]; Sum 11: (5,6), (6,5) [2]; Sum 12: (6,6) [1].\nStep 3: Total favorable = 3 + 2 + 1 = 6 outcomes.\nStep 4: P(Sum ≥ 10) = 6/36 = 1/6."
            },
            {
                "q": "23. Three fair coins are tossed simultaneously. What is the probability of getting at most two Heads?",
                "options": ["3/8", "1/2", "5/8", "7/8"],
                "ans": 3,
                "solution": "Step 1: Total outcomes for 3 coins n(S) = 2³ = 8.\nStep 2: 'At most 2 Heads' means 0, 1, or 2 Heads (all outcomes except 3 Heads {HHH}).\nStep 3: Using complement rule: P(At most 2 H) = 1 - P(3 H) = 1 - 1/8 = 7/8."
            },
            {
                "q": "24. One card is drawn at random from a standard 52-card deck. What is the probability of drawing a black face card?",
                "options": ["3/52", "6/52 (3/26)", "12/52 (3/13)", "1/2"],
                "ans": 1,
                "solution": "Step 1: Total face cards = 12 (6 red, 6 black).\nStep 2: Black face cards are Jack, Queen, King of Spades, and Jack, Queen, King of Clubs (6 cards).\nStep 3: P(Black Face Card) = 6/52 = 3/26."
            },
            {
                "q": "25. From a standard pack of 52 cards, all four Kings are removed. A card is then drawn at random from the remaining cards. What is the probability of drawing an Ace?",
                "options": ["4/52", "4/48 (1/12)", "1/13", "3/48"],
                "ans": 1,
                "solution": "Step 1: After removing 4 Kings, remaining cards n(S') = 52 - 4 = 48 cards.\nStep 2: All 4 Aces remain intact in the deck.\nStep 3: P(Ace) = 4 / 48 = 1/12."
            },
            {
                "q": "26. What was Jean le Rond d'Alembert's famous 1754 error when analyzing the toss of two coins?",
                "options": [
                    "He believed coin tosses were deterministic",
                    "He treated {HT, TH} as a single outcome, falsely claiming P(one head, one tail) was 1/3 instead of 1/2",
                    "He claimed tails was impossible",
                    "He thought two coins had 8 outcomes"
                ],
                "ans": 1,
                "solution": "Step 1: D'Alembert listed only 3 outcomes: two heads, two tails, and one of each.\nStep 2: He failed to realize that 'one of each' comprises two distinct ordered outcomes (HT and TH).\nStep 3: This caused him to incorrectly claim the probability was 1/3 instead of 2/4 = 1/2."
            },
            {
                "q": "27. In a 2-stage tree diagram, the probability of rain on Day 1 is 0.6. If it rains, the probability of school closing is 0.8. If it does not rain, school closing is 0.1. What is the probability that it rains AND school closes?",
                "options": ["0.48", "0.56", "0.14", "0.08"],
                "ans": 0,
                "solution": "Step 1: Along the branch (Rain → Closes), multiply the probabilities.\nStep 2: P(Rain AND Closes) = P(Rain) × P(Closes | Rain) = 0.6 × 0.8 = 0.48."
            },
            {
                "q": "28. An urn contains 4 red and 6 green marbles (total 10). Two marbles are drawn one after another WITHOUT replacement. What is the probability that the first is red and the second is green?",
                "options": ["24/100", "24/90 (4/15)", "20/90", "16/90"],
                "ans": 1,
                "solution": "Step 1: First draw: P(1st Red) = 4/10.\nStep 2: Since it is NOT replaced, 9 marbles remain, of which 6 are green. P(2nd Green) = 6/9.\nStep 3: Joint P = (4/10) × (6/9) = 24/90 = 4/15."
            },
            {
                "q": "29. Two dice are rolled. What is the probability that the product of the two numbers is 12?",
                "options": ["1/9", "4/36", "1/6", "5/36"],
                "ans": 0,
                "solution": "Step 1: Pairs (x, y) with product x × y = 12 are: (2,6), (3,4), (4,3), (6,2) → 4 pairs.\nStep 2: P(Product 12) = 4/36 = 1/9."
            },
            {
                "q": "30. A card is drawn from a 52-card deck. What is the probability that it is a Spade OR an Ace?",
                "options": ["13/52", "16/52 (4/13)", "17/52", "1/4"],
                "ans": 1,
                "solution": "Step 1: There are 13 Spades and 4 Aces.\nStep 2: The Ace of Spades is shared by both (counted twice).\nStep 3: Favorable cards = 13 (Spades) + 3 (other Aces) = 16 cards.\nStep 4: P(Spade or Ace) = 16/52 = 4/13."
            }
        ]
    },
    {
        "id": 4,
        "title": "Mastery Challenge 4: Two-Way Tables, Geometric Probability & Monte Carlo",
        "badge": "Quiz 4 • Advanced Synthesis",
        "questions": [
            {
                "q": "31. A rectangular field has dimensions 60 m × 40 m. Inside the field is a circular pond of radius 7 m. A model airplane crashes randomly into the field. What is the probability that it crashes into the pond? (Use π = 22/7)",
                "options": ["154/2400 ≈ 0.064", "154/1200 ≈ 0.128", "49/2400", "77/1200"],
                "ans": 0,
                "solution": "Step 1: Total area of rectangular field = 60 × 40 = 2,400 m².\nStep 2: Area of circular pond = πr² = (22/7) × 7 × 7 = 154 m².\nStep 3: Geometric P(Pond) = 154 / 2,400 = 77 / 1,200 ≈ 0.0642 (or 6.42%)."
            },
            {
                "q": "32. In a Monte Carlo experiment to estimate π, 10,000 random points are generated in a unit square. 7,854 points satisfy x² + y² ≤ 1. What is the resulting estimate of π?",
                "options": ["3.1400", "3.1416", "3.1450", "3.1500"],
                "ans": 1,
                "solution": "Step 1: Monte Carlo ratio: π ≈ 4 × (N_in / N_total).\nStep 2: π ≈ 4 × (7,854 / 10,000) = 4 × 0.7854 = 3.1416."
            },
            {
                "q": "33. A 2-way table records 200 patients: 120 received Treatment A (80 cured, 40 uncured) and 80 received Treatment B (60 cured, 20 uncured). What is the probability that a randomly chosen patient received Treatment A AND was cured?",
                "options": ["0.40", "0.60", "0.70", "0.80"],
                "ans": 0,
                "solution": "Step 1: Grand total N = 200.\nStep 2: Favorable cell (Treatment A AND cured) = 80.\nStep 3: Joint P = 80 / 200 = 4/10 = 0.40 (or 40%)."
            },
            {
                "q": "34. Referring to the same 200 patients (80 cured under A + 60 cured under B = 140 total cured), what is the probability that a randomly selected patient was cured?",
                "options": ["0.60", "0.70", "0.75", "0.80"],
                "ans": 1,
                "solution": "Step 1: Total cured patients (marginal sum) = 80 + 60 = 140.\nStep 2: Grand total = 200.\nStep 3: Marginal P(Cured) = 140 / 200 = 7/10 = 0.70."
            },
            {
                "q": "35. A square dartboard has side length 2R. An inscribed circle touches all four edges of the square. If a dart hits the square at random, what is the probability that it lands INSIDE the inscribed circle?",
                "options": ["π / 2", "π / 4", "π / 6", "1 / π"],
                "ans": 1,
                "solution": "Step 1: Side of square = 2R → Area of square = (2R)² = 4R².\nStep 2: Radius of inscribed circle = R → Area of circle = πR².\nStep 3: P(Inside circle) = (πR²) / (4R²) = π / 4 ≈ 0.7854 (or 78.5%)."
            },
            {
                "q": "36. A bus arrives at a stop at a random time between 8:00 AM and 8:30 AM. A commuter arrives at 8:10 AM and can wait at most 10 minutes (until 8:20 AM). What is the probability that the commuter catches the bus?",
                "options": ["1/6", "1/4", "1/3", "1/2"],
                "ans": 2,
                "solution": "Step 1: Total arrival window = 30 minutes (8:00 to 8:30 AM).\nStep 2: Favorable window when commuter is waiting = 8:10 to 8:20 AM (10 minutes).\nStep 3: P = 10 / 30 = 1/3."
            },
            {
                "q": "37. An insurance company determines that a driver has a 0.04 (4%) probability of an accident causing ₹50,000 in damage, and a 0.96 probability of no accident. What is the actuarial expected payout per driver?",
                "options": ["₹1,500", "₹2,000", "₹2,500", "₹3,000"],
                "ans": 1,
                "solution": "Step 1: Expected Payout = (P_accident × Damage) + (P_none × 0).\nStep 2: Expected Payout = (0.04 × ₹50,000) + 0 = ₹2,000."
            },
            {
                "q": "38. In a circular target of outer radius 10 cm, an inner bullseye has radius 2 cm. What is the probability that a randomly landing dart hits the bullseye?",
                "options": ["2/10 = 0.20", "(2/10)² = 0.04", "1/5 = 0.20", "4/10 = 0.40"],
                "ans": 1,
                "solution": "Step 1: Geometric probability for concentric circles: P = (π r²) / (π R²) = (r / R)².\nStep 2: P = (2 / 10)² = (1/5)² = 1/25 = 0.04 (or 4%)."
            },
            {
                "q": "39. Why was the Monte Carlo algorithm named after the city of Monte Carlo in Monaco?",
                "options": [
                    "Stanislaw Ulam was born in Monaco",
                    "The algorithms rely on repeated random chance, evoking the famous Monte Carlo Casino",
                    "Monaco funded the research",
                    "The first supercomputer was built in Monte Carlo"
                ],
                "ans": 1,
                "solution": "Step 1: Stanislaw Ulam's uncle frequently gambled at the Monte Carlo Casino.\nStep 2: Because the algorithm solved complex equations through random sampling, Nicholas Metropolis proposed the code-name 'Monte Carlo'."
            },
            {
                "q": "40. If an event E satisfies P(E) = P(Ē), what is the value of P(E)?",
                "options": ["0", "0.25", "0.50", "1.0"],
                "ans": 2,
                "solution": "Step 1: Complement theorem: P(E) + P(Ē) = 1.\nStep 2: Since P(Ē) = P(E), substitute: P(E) + P(E) = 1 ⇒ 2 P(E) = 1.\nStep 3: P(E) = 1/2 = 0.50 (an Even Chance)."
            }
        ]
    }
]

if __name__ == '__main__':
    print(f"Loaded {len(SLIDES)} slides, {len(QUIZZES)} quiz challenge slides.")
    total_cp = sum(len(s['checkpoints']) for s in SLIDES)
    print(f"Total Checkpoints: {total_cp}")
    total_qz = sum(len(q['questions']) for q in QUIZZES)
    print(f"Total Quiz Questions: {total_qz}")
    assert len(SLIDES) == 16, f"Expected 16 content slides, got {len(SLIDES)}"
    assert total_cp == 32, f"Expected 32 checkpoints, got {total_cp}"
    assert len(QUIZZES) == 4, f"Expected 4 quiz challenge slides, got {len(QUIZZES)}"
    assert total_qz == 40, f"Expected 40 quiz questions, got {total_qz}"
    print("All probability data assertions passed cleanly!")

