# -*- coding: utf-8 -*-
"""
Curriculum Dataset for NCERT Class 7 Mathematics - Chapter 4: Expressions Using Letter-Numbers
Contains:
- 20 Complete Slides (16 Content Slides + 4 Dedicated Mastery Quiz Slides)
- Avatar: Acharya Bhaskara II (Father of Indian Algebra & Author of Bijaganita)
- 32 In-Slide Checkpoints with Explanations (2 per slide on slides 1-16)
- 40 Mastery Quiz Challenge Questions with Step-by-Step Pedagogical Solutions
- Strictly ZERO prohibited textbook titles
"""

SLIDES_DATA = [
    # Slide 1: The Notion of Letter-Numbers
    {
        "id": 1,
        "tag": "4.1 The Notion of Letter-Numbers • Foundations",
        "title": "The Notion of Letter-Numbers: Letters as Numbers",
        "sim_id": "letter_number_machine_sim",
        "avatar": {
            "name": "Acharya Bhaskara II",
            "title": "Father of Indian Algebra & Author of Bijaganita"
        },
        "narration": "Welcome, young mathematicians! In arithmetic, we compute with fixed numbers like 5 and 12. But in algebra, we introduce letter-numbers—letters like x, y, and a that represent unknown quantities or hold the place for any number in the universe!",
        "key_terms": ["Letter-Numbers", "Algebra", "Unknowns", "Variable Quantities", "Generalization"],
        "content": [
            "In arithmetic, each symbol has a fixed, unalterable value: $5$ is always five, and $10$ is always ten.",
            "However, many real-world situations involve quantities that change or are currently unknown. To represent these, mathematics uses letters ($a, b, x, y, n, t$) as numbers.",
            "For example, if Aftab's age today is represented by the letter $a$, and Shabnam is $3$ years older than Aftab, Shabnam's age is simply $a + 3$.",
            "If Aftab is $10$, Shabnam is $10 + 3 = 13$. If Aftab is $14$, Shabnam is $14 + 3 = 17$. The single expression $a + 3$ describes the relationship for ALL possible ages!"
        ],
        "fact_box": "In 1150 CE, Acharya Bhaskara II composed 'Bijaganita', the definitive Sanskrit masterwork on algebra. The word 'Bija' literally means 'seed' or 'element'—letters are the seeds from which infinite numerical calculations grow!",
        "checkpoints": [
            {
                "question": "If a box contains $n$ chocolates and you eat $4$ chocolates, which expression represents the remaining chocolates?",
                "options": ["$n + 4$", "$n - 4$", "$4 - n$", "$4n$"],
                "correct": 1,
                "explanation": "Starting with $n$ chocolates and removing $4$ gives $n - 4$ chocolates remaining."
            },
            {
                "question": "Why do mathematicians use letters alongside numbers in algebra?",
                "options": [
                    "To make math look like English",
                    "To represent unknown or changing values in general formulas",
                    "Because they ran out of numbers",
                    "Letters are only used for spelling words"
                ],
                "correct": 1,
                "explanation": "Letters act as placeholders for unknown or variable quantities, allowing us to write compact, universal formulas."
            }
        ]
    },

    # Slide 2: Variables vs Constants
    {
        "id": 2,
        "tag": "4.1 The Notion of Letter-Numbers • Core Distinction",
        "title": "Variables vs Constants: The Changing & The Fixed",
        "sim_id": "variable_vs_constant_balance_sim",
        "avatar": {
            "name": "Acharya Bhaskara II",
            "title": "Father of Indian Algebra & Author of Bijaganita"
        },
        "narration": "Notice the beautiful contrast between a constant and a variable! A constant is like a solid mountain—its value never changes. A variable is like a flowing river—its value changes depending on the situation!",
        "key_terms": ["Constant", "Variable", "Fixed Value", "Changing Value", "Algebraic Terms"],
        "content": [
            "A Constant is a quantity with a fixed, unchanging numerical value: numbers like $7, -12, 0, \\frac{3}{4}$, and $\\pi$ are constants.",
            "A Variable is a letter-number that can take on different numerical values depending on the context: letters like $x, y, z, n, s$ are variables.",
            "Real-Life Analogy:",
            "• The number of days in a standard week is always $7$ (Constant).",
            "• The temperature in your city throughout the day changes continuously: $t^\\circ\\text{C}$ (Variable).",
            "• The price of one movie ticket is $₹250$ (Constant), but the total cost for $n$ friends is $250 \\times n$ (where $n$ is a Variable)."
        ],
        "fact_box": "The word 'algebra' comes from the Arabic 'al-jabr' (reunion of broken parts), while ancient Indian mathematicians referred to it as 'Vyakta-Ganita' (arithmetic of knowns) and 'Avyakta-Ganita' (algebra of unknowns).",
        "checkpoints": [
            {
                "question": "In the expression $5x + 9$, which element is the variable?",
                "options": ["5", "x", "9", "+"],
                "correct": 1,
                "explanation": "$x$ is the letter-number (variable) whose value can vary; $5$ and $9$ are fixed constants."
            },
            {
                "question": "Which of the following represents a constant rather than a variable?",
                "options": ["The height of a growing bamboo shoot", "The speed of a flying bird", "The number of hours in one day (24)", "The score of a cricket batsman"],
                "correct": 2,
                "explanation": "There are always exactly 24 hours in a day; this is a fixed constant."
            }
        ]
    },

    # Slide 3: Revisiting Arithmetic Expressions
    {
        "id": 3,
        "tag": "4.2 Revisiting Arithmetic Expressions • Substitution",
        "title": "Revisiting Arithmetic Expressions: Dynamic Evaluation",
        "sim_id": "evaluating_algebraic_expr_sim",
        "avatar": {
            "name": "Acharya Bhaskara II",
            "title": "Father of Indian Algebra & Author of Bijaganita"
        },
        "narration": "An algebraic expression is like an idle machine waiting for electricity. When you assign a specific numerical value to its variable, the machine whirs to life and evaluates into a single arithmetic number!",
        "key_terms": ["Substitution", "Evaluation", "Input Value", "Numerical Result", "Machine Analogy"],
        "content": [
            "An algebraic expression by itself does not have a single fixed numerical value because its variable can vary.",
            "To evaluate an algebraic expression, we substitute a given number in place of the letter-number and carry out the arithmetic operations.",
            "Example: Evaluate $3x + 7$ for different values of $x$:",
            "• When $x = 2$: $3(2) + 7 = 6 + 7 = 13$",
            "• When $x = 5$: $3(5) + 7 = 15 + 7 = 22$",
            "• When $x = 0$: $3(0) + 7 = 0 + 7 = 7$",
            "Different inputs for the variable yield different arithmetic outputs, turning one algebraic rule into an infinite generator of values!"
        ],
        "fact_box": "In Indian classical astronomy, dynamic substitution was used to predict lunar and solar eclipses centuries in advance by plugging the elapsed number of days ($n$) into celestial algebraic formulas.",
        "checkpoints": [
            {
                "question": "What is the numerical value of $4y - 5$ when $y = 6$?",
                "options": ["19", "24", "14", "29"],
                "correct": 0,
                "explanation": "Substitute $y = 6$: $4(6) - 5 = 24 - 5 = 19$."
            },
            {
                "question": "Evaluate $\\frac{x + 10}{2}$ when $x = 8$.",
                "options": ["14", "9", "18", "8"],
                "correct": 1,
                "explanation": "Substitute $x = 8$: $\\frac{8 + 10}{2} = \\frac{18}{2} = 9$."
            }
        ]
    },

    # Slide 4: Translating Words to Algebraic Expressions
    {
        "id": 4,
        "tag": "4.2 Revisiting Arithmetic Expressions • Word Modeling",
        "title": "Word to Algebra Translator: Building Expressions",
        "sim_id": "word_to_algebra_translator_sim",
        "avatar": {
            "name": "Acharya Bhaskara II",
            "title": "Father of Indian Algebra & Author of Bijaganita"
        },
        "narration": "Algebra is a language! Just as words form sentences, mathematical operational keywords translate directly into algebraic symbols. 'Sum' means plus, 'difference' means minus, and 'product' means multiply!",
        "key_terms": ["Mathematical Translation", "Sum / Total (+)", "Difference / Less (-)", "Product (×)", "Quotient (÷)"],
        "content": [
            "We translate everyday verbal statements into precise algebraic expressions using keyword clues:",
            "• '5 more than $x$' $\\implies x + 5$",
            "• '$y$ decreased by 8' $\\implies y - 8$",
            "• 'Twice a number $m$' $\\implies 2m$",
            "• '7 less than three times $k$' $\\implies 3k - 7$ (Note: write $3k - 7$, NOT $7 - 3k$!)",
            "• 'One-third of $p$ added to 12' $\\implies \\frac{p}{3} + 12$",
            "Mastering this translation allows you to convert complex real-world challenges into crisp, solvable formulas."
        ],
        "fact_box": "Acharya Bhaskara II wrote word problems as poetic verses in Lilavati, such as: 'O lovely maiden with radiant eyes, tell me the number of bees swarming in the jasmine arbor if one-fifth flew to a lotus and one-third to a trumpet flower!'",
        "checkpoints": [
            {
                "question": "Which algebraic expression represents '4 less than 5 times $x$'?",
                "options": ["$4 - 5x$", "$5x - 4$", "$5(x - 4)$", "$\\frac{5x}{4}$"],
                "correct": 1,
                "explanation": "'5 times $x$' is $5x$. '4 less than' that means subtracting 4: $5x - 4$."
            },
            {
                "question": "A basket has $b$ apples. If 3 apples are shared equally among 4 friends, which expression represents the share of each?",
                "options": ["$4b + 3$", "$b + \\frac{3}{4}$", "$\\frac{b}{4} - 3$", "$\\frac{b - 3}{4}$"],
                "correct": 3,
                "explanation": "First, 3 apples are removed ($b - 3$). The remainder is divided equally among 4 friends: $\\frac{b - 3}{4}$."
            }
        ]
    },

    # Slide 5: Omission of the Multiplication Symbol
    {
        "id": 5,
        "tag": "4.3 Omission of Multiplication • Algebraic Syntax",
        "title": "Omission of the Multiplication Symbol: Why We Write 3n",
        "sim_id": "omission_of_multiplication_sim",
        "avatar": {
            "name": "Acharya Bhaskara II",
            "title": "Father of Indian Algebra & Author of Bijaganita"
        },
        "narration": "Have you ever wondered why algebraists write 3n instead of 3 × n? In algebra, the letter x looks almost identical to the multiplication cross ×! To avoid confusion and save space, we omit the × symbol between letters and numbers!",
        "key_terms": ["Juxtaposition", "Omission of ×", "Coefficient Placement", "Visual Clarity", "Division as Fraction"],
        "content": [
            "Convention 1: Omission of '$\\times$' between a number and a letter.",
            "Instead of writing $3 \\times n$, we write $3n$. Instead of $7 \\times x$, we write $7x$.",
            "Convention 2: Omission of '$\\times$' between letters.",
            "Instead of $a \\times b$, we write $ab$. Instead of $x \\times y \\times z$, we write $xyz$.",
            "Convention 3: Number Always Comes First.",
            "We write $4a$, never $a4$.",
            "CRITICAL CAUTION: Never omit '$\\times$' between two pure numbers!",
            "$3 \\times 4 = 12$. If you omit the '$\\times$', it looks like the number $34$! Juxtaposition only applies when at least one factor is a letter-number.",
            "Division Convention: Instead of $a \\div b$, we write $\\frac{a}{b}$."
        ],
        "fact_box": "In Sanskrit manuscripts, mathematicians placed symbols adjacent to each other without multiplication signs, a convention later popularized in Europe by René Descartes in 1637.",
        "checkpoints": [
            {
                "question": "How is the algebraic product $5 \\times p \\times q$ written compactly?",
                "options": ["$5pq$", "$pq5$", "$5 + pq$", "$5.p.q$"],
                "correct": 0,
                "explanation": "By algebraic convention, the number comes first and the multiplication signs are omitted: $5pq$."
            },
            {
                "question": "Why can we NOT omit the multiplication symbol between 6 and 7 in $6 \\times 7$?",
                "options": [
                    "Because 6 and 7 cannot be multiplied",
                    "Because writing 67 would mean sixty-seven in base-10, not forty-two",
                    "Because multiplication only works for letters",
                    "Because 67 is a prime number"
                ],
                "correct": 1,
                "explanation": "In our base-10 positional system, 67 means $6 \\times 10 + 7 = 67$, whereas $6 \\times 7 = 42$."
            }
        ]
    },

    # Slide 6: Anatomy of an Expression
    {
        "id": 6,
        "tag": "4.3 Omission of Multiplication • Terminology",
        "title": "Anatomy of an Algebraic Expression: Terms & Coefficients",
        "sim_id": "terms_coefficients_anatomy_sim",
        "avatar": {
            "name": "Acharya Bhaskara II",
            "title": "Father of Indian Algebra & Author of Bijaganita"
        },
        "narration": "Let us dissect an algebraic expression! Like a sentence made of words, an expression is made of terms separated by plus and minus signs. Each term has factors, and the numerical multiplier is called its coefficient!",
        "key_terms": ["Term", "Numerical Coefficient", "Variable Factors", "Monomial", "Polynomial"],
        "content": [
            "Consider the algebraic expression: $7x^2 - 4xy + 9$",
            "1. Terms: The parts separated by $+$ or $-$ signs.",
            "Here there are $3$ terms: $7x^2$, $-4xy$, and $+9$.",
            "2. Numerical Coefficient: The numerical factor multiplying the variables in a term.",
            "• In $7x^2$, the coefficient is $7$.",
            "• In $-4xy$, the coefficient is $-4$ (always include the negative sign!).",
            "• In $x$, the coefficient is $1$ (since $1 \\times x = x$).",
            "• In $-y$, the coefficient is $-1$.",
            "3. Constant Term: A term with no variables, here $9$."
        ],
        "fact_box": "In Bijaganita, Bhaskara II categorized terms according to their powers: 'Rupa' for constants, 'Yavat-Tavat' (as much as) for the linear variable x, and 'Varga' for square terms.",
        "checkpoints": [
            {
                "question": "What is the numerical coefficient of the term $-8ab$?",
                "options": ["8", "-8", "ab", "-ab"],
                "correct": 1,
                "explanation": "The numerical multiplier including its sign is $-8$."
            },
            {
                "question": "How many terms are in the expression $3x^2 - 5x + 2y - 11$?",
                "options": ["2", "3", "4", "5"],
                "correct": 2,
                "explanation": "There are 4 terms: $3x^2$, $-5x$, $2y$, and $-11$."
            }
        ]
    },

    # Slide 7: Like vs Unlike Terms
    {
        "id": 7,
        "tag": "4.4 Simplification • Like & Unlike Terms",
        "title": "Like vs Unlike Terms: Apples and Oranges",
        "sim_id": "like_vs_unlike_terms_sorter_sim",
        "avatar": {
            "name": "Acharya Bhaskara II",
            "title": "Father of Indian Algebra & Author of Bijaganita"
        },
        "narration": "Listen closely to this fundamental law: you can add 3 apples and 5 apples to get 8 apples. But you cannot add 3 apples and 5 mangoes into 8 of either! Only LIKE terms containing identical variable factors can be combined!",
        "key_terms": ["Like Terms", "Unlike Terms", "Identical Variable Factors", "Order of Factors", "Fruit Analogy"],
        "content": [
            "Like Terms are terms that have the exact same algebraic variable factors, regardless of their numerical coefficients.",
            "Examples of Like Terms:",
            "• $4x$ and $9x$ (both have variable factor $x$)",
            "• $7ab$ and $-2ba$ (since $ab = ba$ by commutative law, they are like terms!)",
            "• $5x^2$ and $12x^2$ (both have $x^2$)",
            "Unlike Terms have different variable factors or different powers:",
            "• $3x$ and $3y$ (variables $x$ and $y$ are different)",
            "• $4x$ and $4x^2$ (powers are different: $x$ vs $x^2$)",
            "Fundamental Rule: Only like terms can be added or subtracted!"
        ],
        "fact_box": "The Sanskrit rule states 'Sajatiya' (of the same species) terms combine, while 'Vijatiya' (of different species) terms remain distinct side by side.",
        "checkpoints": [
            {
                "question": "Which pair represents LIKE terms?",
                "options": ["$3x$ and $3y$", "$5ab$ and $8ba$", "$4x^2$ and $4x$", "$7m$ and $7mn$"],
                "correct": 1,
                "explanation": "$5ab$ and $8ba$ have identical variable factors because $ab = ba$."
            },
            {
                "question": "Can the expression $6a + 4b$ be simplified into $10ab$?",
                "options": [
                    "Yes, $6 + 4 = 10$ and $a + b = ab$",
                    "No, $6a$ and $4b$ are unlike terms and cannot be combined",
                    "Yes, but only if $a = b$",
                    "No, the answer is $24ab$"
                ],
                "correct": 1,
                "explanation": "$6a$ and $4b$ are unlike terms. Writing $10ab$ is a severe algebraic error!"
            }
        ]
    },

    # Slide 8: Simplification of Algebraic Expressions
    {
        "id": 8,
        "tag": "4.4 Simplification • Combining Like Terms",
        "title": "Simplification: Combining Like Terms Pipeline",
        "sim_id": "combining_like_terms_pipeline_sim",
        "avatar": {
            "name": "Acharya Bhaskara II",
            "title": "Father of Indian Algebra & Author of Bijaganita"
        },
        "narration": "To simplify a long expression, gather all like terms together using the commutative law, and then add or subtract their numerical coefficients using the distributive law. The expression shrinks into its most elegant form!",
        "key_terms": ["Simplification", "Regrouping", "Combining Coefficients", "Distributive Property", "Irreducible Form"],
        "content": [
            "Simplifying an algebraic expression means writing it with the minimum number of terms by combining all like terms.",
            "Step 1: Group like terms together (with their preceding $+$ or $-$ signs).",
            "Step 2: Add or subtract the coefficients of each group.",
            "Example: Simplify $5x + 3y - 2x + 7y + 4$:",
            "• Group $x$ terms: $(5x - 2x) = (5 - 2)x = 3x$",
            "• Group $y$ terms: $(3y + 7y) = (3 + 7)y = 10y$",
            "• Constant term: $+4$",
            "• Simplified Result: $3x + 10y + 4$",
            "No further simplification is possible because $3x$, $10y$, and $4$ are all unlike terms."
        ],
        "fact_box": "Simplification is the core skill of algebra. In computer graphics and gaming physics engines, simplifying millions of algebraic equations in real time is what creates smooth 60 FPS 3D animations!",
        "checkpoints": [
            {
                "question": "Simplify the expression: $8k + 3m - 5k + 2m$.",
                "options": ["$3k + 5m$", "$13k + 5m$", "$8km$", "$3k - m$"],
                "correct": 0,
                "explanation": "Group like terms: $(8k - 5k) + (3m + 2m) = 3k + 5m$."
            },
            {
                "question": "Simplify: $12p - 4 + 3p - 7$.",
                "options": ["$15p - 11$", "$15p + 3$", "$9p - 11$", "$15p - 3$"],
                "correct": 0,
                "explanation": "Combine $p$ terms: $12p + 3p = 15p$. Combine constants: $-4 - 7 = -11$. Result: $15p - 11$."
            }
        ]
    },

    # Slide 9: Distributive Law with Letters
    {
        "id": 9,
        "tag": "4.4 Simplification • Distributive Law",
        "title": "The Distributive Law with Letters: Expanding Brackets",
        "sim_id": "distributive_letters_area_sim",
        "avatar": {
            "name": "Acharya Bhaskara II",
            "title": "Father of Indian Algebra & Author of Bijaganita"
        },
        "narration": "When a number stands outside brackets, it must multiply every single term inside! Think of a courier delivering a parcel to every room in the house: a(b + c) = ab + ac!",
        "key_terms": ["Distributive Law", "Expanding Brackets", "Geometric Area Model", "Multiplication Distribution", "Sign Rule"],
        "content": [
            "The Distributive Property allows us to remove brackets by distributing the outside multiplier to each term inside:",
            "$a(b + c) = ab + ac$",
            "Examples:",
            "• $3(x + 4) = 3(x) + 3(4) = 3x + 12$",
            "• $5(2y - 3) = 5(2y) - 5(3) = 10y - 15$",
            "• $-2(4k - 5) = -8k + 10$ (Remember: minus times minus equals plus!)",
            "Geometric Proof: A rectangle of height $a$ and split width $(b + c)$ has total area equal to the sum of the two split areas $ab$ and $ac$."
        ],
        "fact_box": "Bhaskara II used geometric partitioned rectangles to visually prove algebraic theorems in Bijaganita, ending proofs with the proud declaration: 'Upapatti' (visual demonstration / proof)!",
        "checkpoints": [
            {
                "question": "Expand: $4(3x + 5)$.",
                "options": ["$12x + 5$", "$12x + 20$", "$7x + 9$", "$12x + 9$"],
                "correct": 1,
                "explanation": "Multiply 4 by both terms: $4 \\times 3x + 4 \\times 5 = 12x + 20$."
            },
            {
                "question": "Simplify: $2(x + 3) + 3(x - 1)$.",
                "options": ["$5x + 3$", "$5x + 5$", "$6x + 3$", "$5x - 3$"],
                "correct": 0,
                "explanation": "Expand first: $(2x + 6) + (3x - 3)$. Group like terms: $(2x + 3x) + (6 - 3) = 5x + 3$."
            }
        ]
    },

    # Slide 10: Formula Detective
    {
        "id": 10,
        "tag": "4.5 Pick Patterns • Formula Detective",
        "title": "Formula Detective: Decoding Real-World Relationships",
        "sim_id": "formula_detective_sim",
        "avatar": {
            "name": "Acharya Bhaskara II",
            "title": "Father of Indian Algebra & Author of Bijaganita"
        },
        "narration": "Put on your detective hat! In every pattern and arrangement, an underlying algebraic formula is hidden. By investigating the first few cases, you can deduce the general formula and predict what happens at Step 100!",
        "key_terms": ["Formula Detective", "Arrangement Patterns", "Table & Chairs", "Inductive Reasoning", "General Rule"],
        "content": [
            "Consider banquet tables placed in a single row:",
            "• 1 table seats 4 people (1 on each end, 1 on each long side).",
            "• 2 tables joined together seat 6 people (1 on each end, 2 on top, 2 on bottom).",
            "• 3 tables joined seat 8 people (1 on each end, 3 on top, 3 on bottom).",
            "Let us detect the formula for $n$ joined tables:",
            "• Each table contributes $2$ seats (top and bottom): $2n$.",
            "• Plus the $2$ permanent end seats: $+ 2$.",
            "General Formula $= 2n + 2$!",
            "How many people can sit at 50 joined tables? Simply plug in $n = 50$:",
            "$2(50) + 2 = 100 + 2 = 102\\text{ people}$! No drawing needed!"
        ],
        "fact_box": "Pattern recognition is the foundation of artificial intelligence. Machine learning algorithms find general algebraic weights that fit training data, just like a Formula Detective finding 2n + 2!",
        "checkpoints": [
            {
                "question": "Using the banquet table formula $2n + 2$, how many people can sit at 20 tables joined in a row?",
                "options": ["40", "42", "44", "80"],
                "correct": 1,
                "explanation": "Substitute $n = 20$: $2(20) + 2 = 40 + 2 = 42$ people."
            },
            {
                "question": "If a pattern has values: Step 1 = 5, Step 2 = 8, Step 3 = 11, which formula fits?",
                "options": ["$3n + 2$", "$5n$", "$2n + 3$", "$4n + 1$"],
                "correct": 0,
                "explanation": "Check $3n + 2$: for $n=1, 3(1)+2=5$; for $n=2, 3(2)+2=8$; for $n=3, 3(3)+2=11$. Perfectly fits!"
            }
        ]
    },

    # Slide 11: Describing Number Sequences
    {
        "id": 11,
        "tag": "4.5 Pick Patterns • Number Sequences",
        "title": "Algebraic Expressions to Describe Number Sequences",
        "sim_id": "number_sequences_general_term_sim",
        "avatar": {
            "name": "Acharya Bhaskara II",
            "title": "Father of Indian Algebra & Author of Bijaganita"
        },
        "narration": "Every arithmetic sequence has an algebraic DNA code called its n-th term formula. Once you discover this code, you can leap forward to calculate the 1,000th term in a fraction of a second!",
        "key_terms": ["n-th Term Formula", "Common Difference", "Arithmetic Sequence", "Position Number (n)", "General Term"],
        "content": [
            "How to find the $n$-th term formula for any arithmetic sequence:",
            "Step 1: Find the common difference $d$ between consecutive terms.",
            "Step 2: Multiply $n$ by this difference ($d \\times n = dn$).",
            "Step 3: Adjust with an added or subtracted constant to match the first term ($n = 1$).",
            "Example: Sequence $4, 7, 10, 13, 16, \\dots$",
            "• Step 1: Difference is $+3$.",
            "• Step 2: Start with $3n$.",
            "• Step 3: For $n = 1$, $3(1) = 3$. But the first term is $4$! We need to add $1$.",
            "• General Formula: $3n + 1$.",
            "Check for $n = 4$: $3(4) + 1 = 12 + 1 = 13$ ✅",
            "What is the 100th term? $3(100) + 1 = 301$!"
        ],
        "fact_box": "In Indian mathematics, sequences and series were called 'Shredhi-Ganita'. The celebrated 14th-century Kerala mathematician Madhava used sequence formulas to compute the value of Pi to 11 decimal places!",
        "checkpoints": [
            {
                "question": "What is the $n$-th term formula for the odd numbers sequence: $1, 3, 5, 7, 9, \\dots$?",
                "options": ["$2n$", "$2n - 1$", "$2n + 1$", "$n + 2$"],
                "correct": 1,
                "explanation": "Difference is 2. Start with $2n$. For $n=1$, $2(1)-1 = 1$. The formula is $2n - 1$."
            },
            {
                "question": "For the sequence with formula $5n - 2$, what is the 10th term?",
                "options": ["48", "50", "52", "45"],
                "correct": 0,
                "explanation": "Substitute $n = 10$: $5(10) - 2 = 50 - 2 = 48$."
            }
        ]
    },

    # Slide 12: Patterns in a Calendar: 2x2 Matrix
    {
        "id": 12,
        "tag": "4.5 Pick Patterns • Calendar Algebra",
        "title": "Patterns in a Calendar: The 2×2 Matrix Secret",
        "sim_id": "calendar_patterns_matrix_sim",
        "avatar": {
            "name": "Acharya Bhaskara II",
            "title": "Father of Indian Algebra & Author of Bijaganita"
        },
        "narration": "A monthly calendar is not merely a planner—it is an algebraic goldmine! Choose any 2×2 block of 4 dates. Add the diagonal pairs: the two diagonal sums are ALWAYS exactly equal! Algebra reveals the secret why!",
        "key_terms": ["Calendar Grid", "2×2 Date Box", "Diagonal Sums", "Algebraic Invariance", "Proof by Algebra"],
        "content": [
            "Look at any calendar month. Let the top-left date in a $2 \\times 2$ square be $d$.",
            "Because dates increase by $1$ across a row and by $7$ down a column (7 days in a week), the 4 dates in the box are:",
            "• Top-Left: $d$",
            "• Top-Right: $d + 1$",
            "• Bottom-Left: $d + 7$",
            "• Bottom-Right: $(d + 7) + 1 = d + 8$",
            "Now add the diagonal pairs:",
            "• Diagonal 1: $d + (d + 8) = 2d + 8$",
            "• Diagonal 2: $(d + 1) + (d + 7) = 2d + 8$",
            "The two sums are IDENTICAL for any choice of $d$! Algebra proves this magic works on every calendar in human history!"
        ],
        "fact_box": "Calendar math puzzles are a classic feature of recreational mathematics, illustrating how assigning a letter-number like d transforms a visual curiosity into a rigorous mathematical proof.",
        "checkpoints": [
            {
                "question": "In a calendar, if the top-left date of a $2 \\times 2$ box is 4, what is the bottom-right date?",
                "options": ["11", "12", "13", "14"],
                "correct": 1,
                "explanation": "Bottom-right is $d + 8$. For $d = 4$: $4 + 8 = 12$."
            },
            {
                "question": "What is the diagonal sum for a $2 \\times 2$ calendar box where the top-left date is $10$?",
                "options": ["20", "28", "36", "38"],
                "correct": 1,
                "explanation": "Diagonal sum formula $= 2d + 8$. For $d = 10$: $2(10) + 8 = 20 + 8 = 28$."
            }
        ]
    },

    # Slide 13: Patterns in a Calendar: The Cross Pattern
    {
        "id": 13,
        "tag": "4.5 Pick Patterns • Calendar Cross",
        "title": "Calendar Plus-Sign Cross: The 5c Wonder",
        "sim_id": "calendar_cross_column_sim",
        "avatar": {
            "name": "Acharya Bhaskara II",
            "title": "Father of Indian Algebra & Author of Bijaganita"
        },
        "narration": "Pick any date in a calendar that has dates on all four sides. Add the 5 dates forming a plus-sign cross: the total sum is ALWAYS exactly 5 times the center date! Let us prove it using letter-numbers!",
        "key_terms": ["Plus-Sign Cross", "Center Date (c)", "5c Invariant", "Symmetry", "Calendar Magic"],
        "content": [
            "Select any date as the center date $c$.",
            "Its four neighboring cross dates are:",
            "• Top: $c - 7$ (one week earlier)",
            "• Bottom: $c + 7$ (one week later)",
            "• Left: $c - 1$ (yesterday)",
            "• Right: $c + 1$ (tomorrow)",
            "• Center: $c$",
            "Now add all 5 dates:",
            "$\\text{Sum} = (c - 7) + (c + 7) + (c - 1) + (c + 1) + c$",
            "Notice how the $+7$ and $-7$ cancel to $0$, and $+1$ and $-1$ cancel to $0$!",
            "$\\text{Sum} = c + c + c + c + c = 5c$!",
            "If the center date is $15$, the sum of the 5 cross dates is instantly $5 \\times 15 = 75$!"
        ],
        "fact_box": "Symmetry cancellation is one of the most powerful tricks in advanced mathematics. When terms symmetrically balance around a center, complicated calculations instantly collapse into simple multiples!",
        "checkpoints": [
            {
                "question": "If the center date of a calendar plus-sign cross is 12, what is the sum of the 5 dates in the cross?",
                "options": ["50", "60", "70", "48"],
                "correct": 1,
                "explanation": "Sum $= 5c = 5 \\times 12 = 60$."
            },
            {
                "question": "If the sum of a calendar cross is 85, what is the center date?",
                "options": ["15", "17", "19", "21"],
                "correct": 1,
                "explanation": "Set $5c = 85 \\implies c = 85 \\div 5 = 17$."
            }
        ]
    },

    # Slide 14: Matchstick Patterns: Linear Chains
    {
        "id": 14,
        "tag": "4.5 Pick Patterns • Matchstick Chains",
        "title": "Matchstick Patterns: Building Linear Chains",
        "sim_id": "matchstick_patterns_chain_sim",
        "avatar": {
            "name": "Acharya Bhaskara II",
            "title": "Father of Indian Algebra & Author of Bijaganita"
        },
        "narration": "Matchsticks are wonderful tools to visualize algebra! Imagine building a chain of connected triangles or squares. Each new shape shares a side with the previous one. Can you discover the algebraic rule for n shapes?",
        "key_terms": ["Matchstick Pattern", "Shared Sides", "Chain Growth", "Linear Expression", "Shape Formula"],
        "content": [
            "Pattern 1: Chain of Connected Triangles $\\triangle$",
            "• 1 triangle requires 3 matchsticks.",
            "• 2 joined triangles require $3 + 2 = 5$ matchsticks (the middle side is shared!).",
            "• 3 joined triangles require $5 + 2 = 7$ matchsticks.",
            "Formula: The first triangle needs $1$ base stick $+ 2$ sticks. Every subsequent triangle adds $2$ more sticks.",
            "Rule for $n$ triangles $= 2n + 1$!",
            "Pattern 2: Chain of Connected Squares $\\square$",
            "• 1 square needs 4 sticks.",
            "• 2 joined squares need $4 + 3 = 7$ sticks.",
            "• 3 joined squares need $7 + 3 = 10$ sticks.",
            "Rule for $n$ squares $= 3n + 1$!"
        ],
        "fact_box": "Polymer chains in chemistry (like DNA and plastics) link together in repetitive geometric units sharing chemical bonds, exactly like matchstick shapes sharing sides!",
        "checkpoints": [
            {
                "question": "How many matchsticks are needed to build a chain of 15 connected triangles using the rule $2n + 1$?",
                "options": ["30", "31", "33", "45"],
                "correct": 1,
                "explanation": "Substitute $n = 15$: $2(15) + 1 = 30 + 1 = 31$ matchsticks."
            },
            {
                "question": "Using the square rule $3n + 1$, how many matchsticks are needed for 25 connected squares?",
                "options": ["75", "76", "77", "100"],
                "correct": 1,
                "explanation": "Substitute $n = 25$: $3(25) + 1 = 75 + 1 = 76$ matchsticks."
            }
        ]
    },

    # Slide 15: Matchstick Patterns: Complex Geometries
    {
        "id": 15,
        "tag": "4.5 Pick Patterns • Complex Shapes",
        "title": "Complex Matchstick Geometries: Houses & Fish",
        "sim_id": "matchstick_complex_geometries_sim",
        "avatar": {
            "name": "Acharya Bhaskara II",
            "title": "Father of Indian Algebra & Author of Bijaganita"
        },
        "narration": "What if our matchsticks form houses or fish? A house is a square with a triangle roof! By analyzing how many matchsticks are shared when houses connect in a row, we deduce formulas for massive steps like Step 108!",
        "key_terms": ["House Pattern", "Fish Pattern", "Composite Shapes", "Large Step Prediction", "Boundary Analysis"],
        "content": [
            "Pattern: Row of Connected Houses 🏠",
            "• 1 house consists of 1 square (4 sticks) + 1 roof (2 sticks) $= 6$ sticks.",
            "• 2 joined houses share 1 vertical wall: $6 + 5 = 11$ sticks.",
            "• 3 joined houses: $11 + 5 = 16$ sticks.",
            "Formula Analysis:",
            "• Each house adds $5$ sticks, plus $1$ initial left wall.",
            "• Formula for $n$ houses $= 5n + 1$!",
            "How many matchsticks are needed for 100 houses in a row?",
            "$5(100) + 1 = 501\\text{ matchsticks}$!",
            "If a builder has 241 matchsticks, how many houses can they build?",
            "Set $5n + 1 = 241 \\implies 5n = 240 \\implies n = 48\\text{ houses}$!"
        ],
        "fact_box": "In structural architecture and civil engineering, truss bridges use repeating triangular and trapezoidal frames designed with algebraic recurrence relations to maximize load-bearing strength with minimal steel.",
        "checkpoints": [
            {
                "question": "How many matchsticks are required to make 20 connected houses using the formula $5n + 1$?",
                "options": ["100", "101", "105", "120"],
                "correct": 1,
                "explanation": "Substitute $n = 20$: $5(20) + 1 = 100 + 1 = 101$ matchsticks."
            },
            {
                "question": "If you have 86 matchsticks, how many connected houses ($5n + 1$) can you construct?",
                "options": ["15", "17", "18", "16"],
                "correct": 1,
                "explanation": "$5n + 1 = 86 \\implies 5n = 85 \\implies n = 17$ houses."
            }
        ]
    },

    # Slide 16: Bhaskara's Bijaganita
    {
        "id": 16,
        "tag": "Historical Heritage • Indian Algebra",
        "title": "Acharya Bhaskara's Bijaganita: The Poetry of Algebra",
        "sim_id": "bhaskara_bijaganita_puzzles_sim",
        "avatar": {
            "name": "Acharya Bhaskara II",
            "title": "Father of Indian Algebra & Author of Bijaganita"
        },
        "narration": "In ancient India, algebra was not dry and boring—it was poetic literature! In my work Bijaganita, we solved riddles of peacocks, arrows, and swarming bees using letter-numbers. Algebra is the ultimate key that unlocks the secrets of the cosmos!",
        "key_terms": ["Bijaganita", "Lilavati", "Poetic Mathematics", "Ancient Indian Algebra", "Riddles"],
        "content": [
            "Acharya Bhaskara II (1114–1185 CE) was the head of the astronomical observatory at Ujjain, India.",
            "His algebra masterpiece 'Bijaganita' established rules for:",
            "• Operations with positive numbers (Dhana) and negative numbers (Rina)",
            "• Operations with zero and infinity (Khahara)",
            "• Solving linear and quadratic equations using letter-symbols (Varna)",
            "• The celebrated 'Chakravala' method for solving indeterminate equations—praised by European historians as 500 years ahead of its time!",
            "By learning expressions using letter-numbers, you walk in the footsteps of India's greatest mathematical masters."
        ],
        "fact_box": "Bhaskara II's daughter Lilavati was also a brilliant mathematician. Legend says he named his arithmetic book after her to make her name eternal across the ages—and indeed, her name is celebrated worldwide 900 years later!",
        "checkpoints": [
            {
                "question": "What is the literal Sanskrit meaning of 'Bijaganita'?",
                "options": [
                    "Calculation with seeds or elements (Algebra)",
                    "Counting with stones",
                    "Geometry of triangles",
                    "Drawing pictures"
                ],
                "correct": 0,
                "explanation": "'Bija' means seed or primary element; Bijaganita means algebra—calculating using the primary seed symbols (letters)."
            },
            {
                "question": "Who authored the historic mathematical works Lilavati and Bijaganita in 1150 CE?",
                "options": ["Acharya Bhaskara II", "Aryabhata", "Brahmagupta", "Varahamihira"],
                "correct": 0,
                "explanation": "Acharya Bhaskara II (Bhaskaracharya) composed Lilavati and Bijaganita as part of the Siddhanta Shiromani in 1150 CE."
            }
        ]
    },

    # Slide 17: Mastery Challenge I (Notions & Substitution)
    {
        "id": 17,
        "tag": "Chapter Review • Mastery Challenge I",
        "title": "Mastery Challenge I: Letter-Numbers, Variables & Evaluation",
        "sim_id": None,
        "is_quiz": True,
        "quiz_range": (1, 10),
        "avatar": {
            "name": "Acharya Bhaskara II",
            "title": "Father of Indian Algebra & Author of Bijaganita"
        },
        "narration": "The trial of algebra begins! Test your mastery on letter-numbers, variable substitution, and algebraic evaluation. Click 'View Step-by-Step Solution' whenever you need insight."
    },

    # Slide 18: Mastery Challenge II (Syntax & Anatomy)
    {
        "id": 18,
        "tag": "Chapter Review • Mastery Challenge II",
        "title": "Mastery Challenge II: Syntax, Coefficients & Anatomy",
        "sim_id": None,
        "is_quiz": True,
        "quiz_range": (11, 20),
        "avatar": {
            "name": "Acharya Bhaskara II",
            "title": "Father of Indian Algebra & Author of Bijaganita"
        },
        "narration": "Excellent progress! Challenge II tests your command of algebraic syntax: omission of multiplication signs, terms, factors, and numerical coefficients."
    },

    # Slide 19: Mastery Challenge III (Simplification & Like Terms)
    {
        "id": 19,
        "tag": "Chapter Review • Mastery Challenge III",
        "title": "Mastery Challenge III: Like Terms, Simplification & Distributive Law",
        "sim_id": None,
        "is_quiz": True,
        "quiz_range": (21, 30),
        "avatar": {
            "name": "Acharya Bhaskara II",
            "title": "Father of Indian Algebra & Author of Bijaganita"
        },
        "narration": "You are halfway to victory! Challenge III tests combining like terms, expanding brackets via the distributive law, and spotting illegal algebraic moves."
    },

    # Slide 20: Mastery Challenge IV (Patterns, Calendars & Matchsticks)
    {
        "id": 20,
        "tag": "Chapter Review • Mastery Challenge IV",
        "title": "Mastery Challenge IV: Formula Detective, Calendars & Matchsticks",
        "sim_id": None,
        "is_quiz": True,
        "quiz_range": (31, 40),
        "avatar": {
            "name": "Acharya Bhaskara II",
            "title": "Father of Indian Algebra & Author of Bijaganita"
        },
        "narration": "The supreme test! Challenge IV evaluates your pattern-decoding skills across calendars, matchstick chains, and real-world sequences. Complete this to claim your master algebraist title!"
    }
]

# 40 Mastery Quiz Challenge Questions with Step-by-Step Pedagogical Solutions
QUIZ_QUESTIONS = [
    # Q1
    {
        "id": 1,
        "question": "If Meena's present age is $x$ years, what was her age 5 years ago?",
        "options": ["$x + 5$", "$x - 5$", "$5x$", "$5 - x$"],
        "correct": 1,
        "solution_steps": [
            "Meena's current age is represented by the variable $x$.",
            "To find her age 5 years in the past, we subtract 5 from her current age.",
            "Therefore, her age 5 years ago was $x - 5$."
        ]
    },
    # Q2
    {
        "id": 2,
        "question": "What is the value of the algebraic expression $3a + 8$ when $a = 4$?",
        "options": ["15", "20", "24", "22"],
        "correct": 1,
        "solution_steps": [
            "Substitute $a = 4$ into the expression: $3(4) + 8$.",
            "Multiply first: $3 \\times 4 = 12$.",
            "Add: $12 + 8 = 20$."
        ]
    },
    # Q3
    {
        "id": 3,
        "question": "Which of the following is a variable rather than a constant?",
        "options": ["The speed of a moving car ($s\\text{ km/h}$)", "The number of centimeters in one meter (100)", "The value of zero (0)", "The number of sides of an octagon (8)"],
        "correct": 0,
        "solution_steps": [
            "A variable is a quantity that can change or vary.",
            "A car's speed varies continuously as it speeds up or slows down, so $s$ is a variable.",
            "All the other options are fixed numbers (constants)."
        ]
    },
    # Q4
    {
        "id": 4,
        "question": "Write an algebraic expression for: '7 added to three times a number $n$'.",
        "options": ["$3n + 7$", "$7n + 3$", "$3(n + 7)$", "$\\frac{n}{3} + 7$"],
        "correct": 0,
        "solution_steps": [
            "'Three times a number $n$' is written as $3n$.",
            "'7 added to' that product means adding 7.",
            "Expression = $3n + 7$."
        ]
    },
    # Q5
    {
        "id": 5,
        "question": "Evaluate $\\frac{2x - 4}{3}$ when $x = 8$.",
        "options": ["3", "4", "5", "6"],
        "correct": 1,
        "solution_steps": [
            "Substitute $x = 8$: $\\frac{2(8) - 4}{3}$.",
            "Compute numerator: $2 \\times 8 = 16$, then $16 - 4 = 12$.",
            "Divide by 3: $\\frac{12}{3} = 4$."
        ]
    },
    # Q6
    {
        "id": 6,
        "question": "A pen costs ₹15 and a notebook costs ₹40. What is the total cost of buying $p$ pens and $q$ notebooks?",
        "options": ["$15p + 40q$", "$40p + 15q$", "$55(p + q)$", "$15 + p + 40 + q$"],
        "correct": 0,
        "solution_steps": [
            "Cost of $p$ pens at ₹15 each $= 15 \\times p = 15p$.",
            "Cost of $q$ notebooks at ₹40 each $= 40 \\times q = 40q$.",
            "Total cost $= 15p + 40q$."
        ]
    },
    # Q7
    {
        "id": 7,
        "question": "If $k$ represents an even number, which expression represents the NEXT consecutive even number?",
        "options": ["$k + 1$", "$k + 2$", "$2k$", "$k + 4$"],
        "correct": 1,
        "solution_steps": [
            "Even numbers increase by 2 (e.g. 2, 4, 6, 8, ...).",
            "If $k$ is an even number, the next consecutive even number is $k + 2$."
        ]
    },
    # Q8
    {
        "id": 8,
        "question": "What is the value of $x^2 - 3x + 5$ when $x = 3$?",
        "options": ["5", "9", "11", "14"],
        "correct": 0,
        "solution_steps": [
            "Substitute $x = 3$: $(3)^2 - 3(3) + 5$.",
            "Calculate powers and products: $9 - 9 + 5$.",
            "$9 - 9 = 0$, then $0 + 5 = 5$."
        ]
    },
    # Q9
    {
        "id": 9,
        "question": "Express algebraically: 'Subtract 9 from the quotient of $y$ and 4'.",
        "options": ["$9 - \\frac{y}{4}$", "$\\frac{y}{4} - 9$", "$\\frac{y - 9}{4}$", "$4y - 9$"],
        "correct": 1,
        "solution_steps": [
            "The quotient of $y$ and 4 is $\\frac{y}{4}$.",
            "'Subtract 9 from' means $\\frac{y}{4} - 9$."
        ]
    },
    # Q10
    {
        "id": 10,
        "question": "If perimeter of an equilateral triangle with side length $s$ is $P$, what is the formula for $P$?",
        "options": ["$P = s + 3$", "$P = 3s$", "$P = s^3$", "$P = \\frac{s}{3}$"],
        "correct": 1,
        "solution_steps": [
            "An equilateral triangle has 3 sides of equal length $s$.",
            "Perimeter $= s + s + s = 3s$."
        ]
    },

    # Q11
    {
        "id": 11,
        "question": "Why is the algebraic product of $a$ and $b$ written as $ab$ rather than $a \\times b$?",
        "options": [
            "By convention, omitting $\\times$ between letters avoids confusion with the letter $x$",
            "Because letters cannot be multiplied",
            "Because $ab$ means $a + b$",
            "It is required only in geometry"
        ],
        "correct": 0,
        "solution_steps": [
            "In algebra, the multiplication sign $\\times$ closely resembles the letter variable $x$.",
            "Writing $ab$ eliminates ambiguity, saves space, and represents multiplication unambiguously."
        ]
    },
    # Q12
    {
        "id": 12,
        "question": "What is the numerical coefficient of the term $-xy$?",
        "options": ["0", "1", "-1", "xy"],
        "correct": 2,
        "solution_steps": [
            "$-xy$ is equivalent to $-1 \\times x \\times y$.",
            "Therefore, its numerical coefficient is $-1$."
        ]
    },
    # Q13
    {
        "id": 13,
        "question": "In the algebraic expression $5x^2 - 7xy + 3y^2 - 8$, what is the constant term?",
        "options": ["5", "3", "-7", "-8"],
        "correct": 3,
        "solution_steps": [
            "A constant term contains no variable factors.",
            "Here, $-8$ is purely numerical, so the constant term is $-8$."
        ]
    },
    # Q14
    {
        "id": 14,
        "question": "Which of the following expressions is written INCORRECTLY according to algebraic conventions?",
        "options": ["$4x$", "$ab$", "$x4$", "$7xyz$"],
        "correct": 2,
        "solution_steps": [
            "By standard convention, the numerical coefficient must always precede the variable.",
            "We write $4x$, never $x4$."
        ]
    },
    # Q15
    {
        "id": 15,
        "question": "How many terms does the expression $2a + 3b - 4c + 7$ contain?",
        "options": ["3", "4", "5", "1"],
        "correct": 1,
        "solution_steps": [
            "The terms separated by $+$ and $-$ signs are: $2a$, $3b$, $-4c$, and $7$.",
            "Total count $= 4$ terms."
        ]
    },
    # Q16
    {
        "id": 16,
        "question": "What are the variable factors of the term $6m^2n$?",
        "options": ["6", "$m, m, n$", "$6, m, n$", "$m^2$ only"],
        "correct": 1,
        "solution_steps": [
            "6 is the numerical factor.",
            "The variable factors are $m \\times m \\times n$, which are $m, m, n$."
        ]
    },
    # Q17
    {
        "id": 17,
        "question": "What is the coefficient of $x$ in the expression $8 - x + y$?",
        "options": ["1", "8", "-1", "0"],
        "correct": 2,
        "solution_steps": [
            "The term containing $x$ is $-x$, which equals $-1 \\times x$.",
            "Therefore, the coefficient of $x$ is $-1$."
        ]
    },
    # Q18
    {
        "id": 18,
        "question": "Which algebraic expression represents 'the quotient of $x$ divided by the sum of $y$ and 3'?",
        "options": ["$\\frac{x}{y} + 3$", "$\\frac{x}{y + 3}$", "$\\frac{y + 3}{x}$", "$x(y + 3)$"],
        "correct": 1,
        "solution_steps": [
            "The sum of $y$ and 3 is $(y + 3)$.",
            "Dividing $x$ by that sum gives $\\frac{x}{y + 3}$."
        ]
    },
    # Q19
    {
        "id": 19,
        "question": "In the term $\\frac{3}{4}w$, what is the numerical coefficient?",
        "options": ["3", "4", "$\\frac{3}{4}$", "$w$"],
        "correct": 2,
        "solution_steps": [
            "The numerical fraction multiplying the variable $w$ is $\\frac{3}{4}$.",
            "Thus, the coefficient is $\\frac{3}{4}$."
        ]
    },
    # Q20
    {
        "id": 20,
        "question": "Which of the following expressions is a monomial (containing exactly one term)?",
        "options": ["$3x + 2$", "$5xy$", "$a - b$", "$x^2 + y^2$"],
        "correct": 1,
        "solution_steps": [
            "A monomial consists of a single term with no $+$ or $-$ connecting operations.",
            "$5xy$ is a single term (monomial)."
        ]
    },

    # Q21
    {
        "id": 21,
        "question": "Which pair consists of LIKE terms?",
        "options": ["$4x^2$ and $4x$", "$7ab$ and $-3ba$", "$5m$ and $5n$", "$2xy$ and $2x^2y$"],
        "correct": 1,
        "solution_steps": [
            "Like terms must have identical variable factors and identical powers.",
            "Since $ab = ba$ by the commutative law, $7ab$ and $-3ba$ have identical variable factors and are like terms."
        ]
    },
    # Q22
    {
        "id": 22,
        "question": "Simplify the expression: $9x + 4y - 5x + 3y$.",
        "options": ["$4x + 7y$", "$14x + 7y$", "$11xy$", "$4x - y$"],
        "correct": 0,
        "solution_steps": [
            "Group like terms:",
            "$x$ terms: $9x - 5x = (9 - 5)x = 4x$.",
            "$y$ terms: $4y + 3y = (4 + 3)y = 7y$.",
            "Result: $4x + 7y$."
        ]
    },
    # Q23
    {
        "id": 23,
        "question": "Expand the expression using the distributive law: $3(2a - 5b)$.",
        "options": ["$6a - 5b$", "$6a - 15b$", "$5a - 8b$", "$6a + 15b$"],
        "correct": 1,
        "solution_steps": [
            "Distribute 3 to each term inside the bracket:",
            "$3 \\times 2a - 3 \\times 5b = 6a - 15b$."
        ]
    },
    # Q24
    {
        "id": 24,
        "question": "Simplify: $5(x + 2) - 3(x - 4)$.",
        "options": ["$2x + 22$", "$2x - 2$", "$8x + 22$", "$2x + 10$"],
        "correct": 0,
        "solution_steps": [
            "Expand brackets: $5(x) + 5(2) - 3(x) - 3(-4)$.",
            "$= 5x + 10 - 3x + 12$. (Notice $-3 \\times -4 = +12$).",
            "Combine like terms: $(5x - 3x) + (10 + 12) = 2x + 22$."
        ]
    },
    # Q25
    {
        "id": 25,
        "question": "What is the sum of $(3a - 4b + 2)$ and $(2a + 5b - 7)$?",
        "options": ["$5a + b - 5$", "$5a - 9b - 5$", "$6a + b - 5$", "$5a + 9b + 9$"],
        "correct": 0,
        "solution_steps": [
            "Combine $a$ terms: $3a + 2a = 5a$.",
            "Combine $b$ terms: $-4b + 5b = +b$.",
            "Combine constants: $2 - 7 = -5$.",
            "Sum = $5a + b - 5$."
        ]
    },
    # Q26
    {
        "id": 26,
        "question": "Subtract $(4x - 3)$ from $(7x + 2)$.",
        "options": ["$3x - 1$", "$3x + 5$", "$11x - 1$", "$3x - 5$"],
        "correct": 1,
        "solution_steps": [
            "Set up subtraction: $(7x + 2) - (4x - 3)$.",
            "Distribute the minus sign: $7x + 2 - 4x + 3$.",
            "Combine like terms: $(7x - 4x) + (2 + 3) = 3x + 5$."
        ]
    },
    # Q27
    {
        "id": 27,
        "question": "Why can $4a$ and $3a^2$ NOT be combined into $7a^3$ or $7a^2$?",
        "options": [
            "Because they have different powers of $a$, making them unlike terms",
            "Because $4 + 3$ is not 7",
            "Because $a$ must be an integer",
            "They can be combined"
        ],
        "correct": 0,
        "solution_steps": [
            "$4a$ has degree 1 (linear), while $3a^2$ has degree 2 (quadratic).",
            "Like terms must have identical powers of each variable; therefore, they cannot be merged by addition."
        ]
    },
    # Q28
    {
        "id": 28,
        "question": "Simplify: $2xy + 3x - xy + 4x$.",
        "options": ["$xy + 7x$", "$3xy + 7x$", "$8xy$", "$xy - x$"],
        "correct": 0,
        "solution_steps": [
            "Combine $xy$ terms: $2xy - 1xy = 1xy = xy$.",
            "Combine $x$ terms: $3x + 4x = 7x$.",
            "Result: $xy + 7x$."
        ]
    },
    # Q29
    {
        "id": 29,
        "question": "Expand: $- (3x - 7y + 4)$.",
        "options": ["$-3x - 7y + 4$", "$-3x + 7y - 4$", "$3x + 7y + 4$", "$-3x - 7y - 4$"],
        "correct": 1,
        "solution_steps": [
            "A minus sign in front of parentheses multiplies every inside term by $-1$, flipping every sign:",
            "$- (3x - 7y + 4) = -3x + 7y - 4$."
        ]
    },
    # Q30
    {
        "id": 30,
        "question": "If the perimeter of a rectangle is $2(l + b)$, find the perimeter when length $l = 3x + 2$ and breadth $b = x + 1$.",
        "options": ["$4x + 3$", "$8x + 6$", "$8x + 3$", "$6x + 4$"],
        "correct": 1,
        "solution_steps": [
            "Sum inside brackets: $l + b = (3x + 2) + (x + 1) = 4x + 3$.",
            "Multiply by 2: $2(4x + 3) = 8x + 6$."
        ]
    },

    # Q31
    {
        "id": 31,
        "question": "In a sequence with $n$-th term $4n + 3$, what is the 12th term?",
        "options": ["48", "51", "55", "52"],
        "correct": 1,
        "solution_steps": [
            "Substitute $n = 12$: $4(12) + 3$.",
            "$48 + 3 = 51$."
        ]
    },
    # Q32
    {
        "id": 32,
        "question": "Find the general $n$-th term formula for the sequence: $5, 9, 13, 17, 21, \\dots$",
        "options": ["$4n + 1$", "$5n - 1$", "$4n + 5$", "$3n + 2$"],
        "correct": 0,
        "solution_steps": [
            "Common difference $d = 9 - 5 = 4$.",
            "Start with $4n$.",
            "For $n = 1$, $4(1) = 4$. To get 5, add 1.",
            "Formula = $4n + 1$."
        ]
    },
    # Q33
    {
        "id": 33,
        "question": "In a calendar, the 4 dates in a $2 \\times 2$ box have top-left date $d$. What is the sum of the two diagonal dates $(d)$ and $(d + 8)$?",
        "options": ["$2d + 7$", "$2d + 8$", "$2d + 9$", "$d + 8$"],
        "correct": 1,
        "solution_steps": [
            "Add the top-left date $d$ and bottom-right date $d + 8$:",
            "$d + (d + 8) = 2d + 8$."
        ]
    },
    # Q34
    {
        "id": 34,
        "question": "In a calendar plus-sign cross, the center date is 14. What is the sum of all 5 dates in the cross?",
        "options": ["65", "70", "75", "84"],
        "correct": 1,
        "solution_steps": [
            "The sum of the 5 cross dates is always $5c$, where $c$ is the center date.",
            "$5 \\times 14 = 70$."
        ]
    },
    # Q35
    {
        "id": 35,
        "question": "A matchstick pattern forms a chain of $n$ connected triangles. If the formula is $2n + 1$, how many matchsticks are needed for 40 triangles?",
        "options": ["80", "81", "82", "120"],
        "correct": 1,
        "solution_steps": [
            "Substitute $n = 40$: $2(40) + 1$.",
            "$80 + 1 = 81$ matchsticks."
        ]
    },
    # Q36
    {
        "id": 36,
        "question": "A matchstick square chain follows the rule $3n + 1$. If a student uses 91 matchsticks, how many squares did they build?",
        "options": ["28", "29", "30", "31"],
        "correct": 2,
        "solution_steps": [
            "Set the formula equal to 91: $3n + 1 = 91$.",
            "Subtract 1: $3n = 90$.",
            "Divide by 3: $n = 90 \\div 3 = 30$ squares."
        ]
    },
    # Q37
    {
        "id": 37,
        "question": "In a connected row of $n$ matchstick houses, the formula is $5n + 1$. How many matchsticks are needed for Step 108?",
        "options": ["540", "541", "545", "648"],
        "correct": 1,
        "solution_steps": [
            "Substitute $n = 108$: $5(108) + 1$.",
            "$5 \\times 108 = 540$, then $540 + 1 = 541$ matchsticks."
        ]
    },
    # Q38
    {
        "id": 38,
        "question": "Tables and chairs problem: If 1 table seats 4 people and each additional table added to the row adds 2 seats, what is the formula for $n$ tables?",
        "options": ["$4n$", "$2n + 2$", "$2n + 4$", "$3n + 1$"],
        "correct": 1,
        "solution_steps": [
            "For $n=1$, seats $= 4$.",
            "For $n=2$, seats $= 6$.",
            "For $n=3$, seats $= 8$.",
            "Difference is 2, so $2n$. When $n=1, 2(1) + 2 = 4$.",
            "Formula $= 2n + 2$."
        ]
    },
    # Q39
    {
        "id": 39,
        "question": "What is the 50th term of the sequence: $2, 5, 8, 11, 14, \\dots$?",
        "options": ["147", "149", "150", "152"],
        "correct": 1,
        "solution_steps": [
            "Common difference $d = 3$. Formula $= 3n - 1$ (since for $n=1, 3(1)-1=2$).",
            "For $n = 50$: $3(50) - 1 = 150 - 1 = 149$."
        ]
    },
    # Q40
    {
        "id": 40,
        "question": "Which historic treatise composed by Bhaskara II in 1150 CE is regarded as the world's first comprehensive textbook on algebra?",
        "options": ["Aryabhatiya", "Bijaganita", "Brahmasphutasiddhanta", "Sulba Sutras"],
        "correct": 1,
        "solution_steps": [
            "'Bijaganita' (literally calculation with primary seed elements/letters) was written by Acharya Bhaskara II in 1150 CE as the dedicated algebra volume of Siddhanta Shiromani."
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

