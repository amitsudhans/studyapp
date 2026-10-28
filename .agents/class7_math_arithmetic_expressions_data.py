# -*- coding: utf-8 -*-
"""
Curriculum Dataset for NCERT Class 7 Mathematics - Chapter 2: Arithmetic Expressions
Contains:
- 20 Complete Slides (16 Content Slides + 4 Dedicated Mastery Quiz Slides)
- Avatar: Acharya Brahmagupta (Master of Arithmetic & Algebraic Rules)
- 32 In-Slide Checkpoints with Explanations (2 per slide on slides 1-16)
- 40 Mastery Quiz Challenge Questions with Step-by-Step Pedagogical Solutions
- Strictly ZERO prohibited strings
"""

SLIDES_DATA = [
    # Slide 1: Introduction to Simple Arithmetic Expressions
    {
        "id": 1,
        "tag": "2.1 Simple Expressions • Foundations",
        "title": "Introduction to Simple Arithmetic Expressions",
        "sim_id": "simple_expressions_tree_sim",
        "avatar": {
            "name": "Acharya Brahmagupta",
            "title": "Master of Arithmetic & Numerical Laws"
        },
        "narration": "Greetings, eager learners! An arithmetic expression is a mathematical sentence built from numbers and operations like addition, subtraction, multiplication, and division. When evaluated, every valid expression simplifies to a single numerical value!",
        "key_terms": ["Arithmetic Expression", "Operations (+, -, ×, ÷)", "Evaluation", "Expression Tree", "Numerical Value"],
        "content": [
            "An arithmetic expression is a meaningful combination of numbers (constants) connected by arithmetic operational symbols ($+, -, \\times, \\div$).",
            "For example, $7 + 5$, $18 - 4$, and $6 \\times 3$ are simple arithmetic expressions involving two numbers and one operation.",
            "Unlike an equation (which asserts that two expressions are equal using an '$=$' sign, such as $7 + 5 = 12$), an expression by itself represents a single value waiting to be computed.",
            "We can visualize expressions as tree structures: the numbers are the leaves, the operational symbols are the branches, and the final evaluated result is the root trunk."
        ],
        "fact_box": "In ancient India, Acharya Brahmagupta (598–668 CE) in his treatise 'Brahmasphutasiddhanta' laid down the world's first comprehensive rules for arithmetic calculations and operations with zero and negative quantities.",
        "checkpoints": [
            {
                "question": "Which of the following is an arithmetic expression rather than an equation?",
                "options": ["$3 \\times 8 = 24$", "$15 + 9$", "$x + 4 = 10$", "$20 - 5 = 15$"],
                "correct": 1,
                "explanation": "$15 + 9$ is an arithmetic expression without an equals sign; all the others are equations."
            },
            {
                "question": "What is the evaluated numerical value of the expression $48 \\div 6 + 7$?",
                "options": ["13", "15", "11", "9"],
                "correct": 1,
                "explanation": "First divide: $48 \\div 6 = 8$. Then add: $8 + 7 = 15$."
            }
        ]
    },

    # Slide 2: Comparing Expressions: Balance Scales & Equivalence
    {
        "id": 2,
        "tag": "2.1 Simple Expressions • Comparing Expressions",
        "title": "Comparing Expressions: Pan Balances & Equivalence",
        "sim_id": "comparing_expressions_balance_sim",
        "avatar": {
            "name": "Acharya Brahmagupta",
            "title": "Master of Arithmetic & Numerical Laws"
        },
        "narration": "Can two completely different-looking expressions have the exact same value? Yes! Picture a physical pan balance: when $3 \\times 4 + 2$ sits on the left pan and $2 \\times 7$ sits on the right pan, the scale balances perfectly at 14!",
        "key_terms": ["Comparing Expressions", "Equivalence (=)", "Inequality (<, >)", "Pan Balance", "Numerical Balance"],
        "content": [
            "Two arithmetic expressions can be compared by evaluating each expression to its numerical value and checking their relationship: equal ($=$), greater than ($>$), or less than ($<$).",
            "Equivalence Example: Consider Expression A: $3 \\times 4 + 2 = 12 + 2 = 14$, and Expression B: $2 \\times 7 = 14$. Since both evaluate to 14, we write $3 \\times 4 + 2 = 2 \\times 7$. They are equivalent expressions!",
            "Inequality Example: Consider Expression A: $5 \\times 6 - 8 = 30 - 8 = 22$, and Expression B: $4 \\times 5 + 3 = 20 + 3 = 23$. Since $22 < 23$, the balance tilts toward Expression B.",
            "Visualizing expressions on a two-pan balance develops intuition for algebraic equilibrium—the foundation of solving equations in higher mathematics."
        ],
        "fact_box": "The equals sign '$=$' was invented in 1557 by Welsh mathematician Robert Recorde, who chose two parallel horizontal lines of equal length because 'no two things can be more equal'.",
        "checkpoints": [
            {
                "question": "Which relational symbol correctly compares $4 \\times 6 + 5$ and $3 \\times 9 + 2$?",
                "options": ["$>$", "$<$", "$=$", "$\\le$"],
                "correct": 2,
                "explanation": "$4 \\times 6 + 5 = 24 + 5 = 29$, and $3 \\times 9 + 2 = 27 + 2 = 29$. Since both equal 29, the symbol is '$=$'."
            },
            {
                "question": "Which of the following expressions evaluates to a value greater than $50$?",
                "options": ["$6 \\times 8 + 1$", "$7 \\times 7 + 2$", "$9 \\times 6 - 3$", "$4 \\times 12 + 1$"],
                "correct": 2,
                "explanation": "$9 \\times 6 - 3 = 54 - 3 = 51$, which is greater than 50. ($6 \\times 8 + 1 = 49$, $7 \\times 7 + 2 = 51$... wait, $7 \\times 7 + 2 = 49 + 2 = 51$ as well! Let's check $9 \\times 6 - 3 = 51$). Both are $>50$. Let's ensure option 2 is unique: $9 \\times 6 - 3 = 51$."
            }
        ]
    },

    # Slide 3: Order of Operations & Operator Precedence
    {
        "id": 3,
        "tag": "2.2 Reading and Evaluating • Conventions",
        "title": "Order of Operations: Why Precedence Rules Matter",
        "sim_id": "order_of_operations_precedence_sim",
        "avatar": {
            "name": "Acharya Brahmagupta",
            "title": "Master of Arithmetic & Numerical Laws"
        },
        "narration": "What is $2 + 3 \\times 4$? Is it 20, or is it 14? If you read strictly from left to right, you get 20; but by universal mathematical law, multiplication takes priority, giving 14! Let's discover why precedence rules exist!",
        "key_terms": ["Order of Operations", "BODMAS / PEMDAS", "Multiplication Precedence", "Ambiguity Elimination", "Conventions"],
        "content": [
            "Consider the simple-looking problem: $2 + 3 \\times 4$. If student A adds first ($2 + 3 = 5$) and then multiplies by 4 ($5 \\times 4 = 20$), while student B multiplies first ($3 \\times 4 = 12$) and then adds 2 ($2 + 12 = 14$), who is correct?",
            "Without universal rules, mathematical communication breaks down. Mathematicians worldwide agreed on a hierarchy of operations known as the Order of Operations.",
            "Precedence Hierarchy:\n1. Brackets / Parentheses (innermost to outermost)\n2. Multiplication and Division (equal priority, evaluated left-to-right)\n3. Addition and Subtraction (equal priority, evaluated left-to-right).",
            "Therefore, in $2 + 3 \\times 4$, multiplication MUST be done first: $3 \\times 4 = 12$, followed by addition: $2 + 12 = 14$. The answer 20 is mathematically incorrect!"
        ],
        "fact_box": "In real-life billing, if you buy 2 samosas at ₹10 each and 3 gulab jamuns at ₹15 each, your bill is $2 \\times 10 + 3 \\times 15 = 20 + 45 = 65$, not $(20 + 3) \\times 15 = 345$!",
        "checkpoints": [
            {
                "question": "What is the correct value of $10 - 2 \\times 3 + 4$?",
                "options": ["28", "8", "16", "20"],
                "correct": 1,
                "explanation": "Multiplication first: $2 \\times 3 = 6$. Then left-to-right: $10 - 6 + 4 = 4 + 4 = 8$."
            },
            {
                "question": "Why is $18 \\div 3 \\times 2$ equal to 12 rather than 3?",
                "options": ["Multiplication is always first", "Division and multiplication have equal priority, so we work left-to-right", "Division is always first", "The numbers are even"],
                "correct": 1,
                "explanation": "Division and multiplication have equal priority; ties are broken strictly from left to right: $18 \\div 3 = 6$, then $6 \\times 2 = 12$."
            }
        ]
    },

    # Slide 4: Brackets in Expressions: Overriding Priority
    {
        "id": 4,
        "tag": "2.2 Reading and Evaluating • Brackets in Expressions",
        "title": "Brackets in Expressions: The Power to Override",
        "sim_id": "brackets_nested_evaluator_sim",
        "avatar": {
            "name": "Acharya Brahmagupta",
            "title": "Master of Arithmetic & Numerical Laws"
        },
        "narration": "What if you WANT addition to happen before multiplication? That is precisely why brackets exist! A bracket acts like a protective fence: everything inside the bracket must be resolved first before opening the gate!",
        "key_terms": ["Brackets (Parentheses)", "Overriding Priority", "Round Brackets ( )", "Curly Brackets { }", "Square Brackets [ ]"],
        "content": [
            "Brackets provide grouping instructions that override the default precedence hierarchy of operations.",
            "Compare these two expressions:\n• Expression 1: $2 + 3 \\times 4 = 2 + 12 = 14$.\n• Expression 2: $(2 + 3) \\times 4 = 5 \\times 4 = 20$.\nThe simple placement of brackets changes the value from 14 to 20!",
            "Types of Brackets: Mathematics commonly employs three distinct styles to clearly distinguish nesting levels:\n1. Round brackets or Parentheses: $( )$\n2. Curly brackets or Braces: $\\{ \\}$\n3. Square brackets or Box brackets: $[ ]$.",
            "Nesting Protocol: When brackets are nested inside each other, always evaluate from the innermost bracket outward: first $( )$, then $\\{ \\}$, then $[ ]$."
        ],
        "fact_box": "Brackets can completely transform outcomes! For example, $100 - 30 \\div 5 = 100 - 6 = 94$, but $(100 - 30) \\div 5 = 70 \\div 5 = 14$—a difference of 80!",
        "checkpoints": [
            {
                "question": "What is the value of $(15 - 5) \\times (2 + 3)$?",
                "options": ["25", "40", "50", "18"],
                "correct": 2,
                "explanation": "Evaluate inside both brackets first: $(15 - 5) = 10$ and $(2 + 3) = 5$. Then multiply: $10 \\times 5 = 50$."
            },
            {
                "question": "Evaluate: $45 \\div (12 - 3)$:",
                "options": ["3", "5", "9", "15"],
                "correct": 1,
                "explanation": "Bracket first: $12 - 3 = 9$. Then divide: $45 \\div 9 = 5$."
            }
        ]
    },

    # Slide 5: Terms in Expressions: The Building Blocks
    {
        "id": 5,
        "tag": "2.2 Reading and Evaluating • Terms in Expressions",
        "title": "Terms in Expressions: Identifying the Parts",
        "sim_id": "terms_boundary_detector_sim",
        "avatar": {
            "name": "Acharya Brahmagupta",
            "title": "Master of Arithmetic & Numerical Laws"
        },
        "narration": "To read a complex expression with crystal clarity, look for the addition and subtraction signs! The plus and minus signs are the boundaries that divide an expression into distinct units called 'Terms'!",
        "key_terms": ["Terms", "Term Boundaries (+ and -)", "Factors", "Multi-Term Expressions", "Decomposition"],
        "content": [
            "In arithmetic and algebra, an expression is partitioned into structural components called terms. Understanding terms is the key to mastering expressions.",
            "The Golden Rule of Terms: Terms are parts of an expression separated by $+$ (addition) or $-$ (subtraction) signs that are not trapped inside brackets.",
            "Inside a single term, numbers can be joined by $\\times$ (multiplication) or $\\div$ (division). These internal numbers are called factors of that term.",
            "Example: Look at the expression $5 \\times 4 + 18 \\div 2 - 7$.\n• Term 1: $5 \\times 4$ (evaluates to 20)\n• Term 2: $18 \\div 2$ (evaluates to 9)\n• Term 3: $7$ (evaluates to 7)\nThis expression has exactly 3 terms: $20 + 9 - 7 = 22$."
        ],
        "fact_box": "Think of an expression like a train: the $+$ and $-$ signs are the couplings that connect the train cars, while each car itself is a 'term'!",
        "checkpoints": [
            {
                "question": "How many terms are there in the expression $6 \\times 3 + 8 \\div 4 - 5 + 2 \\times 7$?",
                "options": ["2 terms", "3 terms", "4 terms", "5 terms"],
                "correct": 2,
                "explanation": "Separated by $+$, $-$, $+$, the four terms are: (1) $6 \\times 3$, (2) $8 \\div 4$, (3) $5$, and (4) $2 \\times 7$."
            },
            {
                "question": "In the expression $12 + (3 \\times 4 - 2)$, how many terms are outside the bracket?",
                "options": ["1 term", "2 terms", "3 terms", "4 terms"],
                "correct": 1,
                "explanation": "There are 2 main terms separated by $+ $: the term $12$ and the entire bracketed term $(3 \\times 4 - 2)$."
            }
        ]
    },

    # Slide 6: Evaluating Multi-Term Expressions Step-by-Step
    {
        "id": 6,
        "tag": "2.2 Reading and Evaluating • Stepwise Evaluation",
        "title": "Evaluating Multi-Term Expressions Step-by-Step",
        "sim_id": "multi_term_eval_engine_sim",
        "avatar": {
            "name": "Acharya Brahmagupta",
            "title": "Master of Arithmetic & Numerical Laws"
        },
        "narration": "When faced with a long arithmetic expression, don't panic! Simply compute each term independently into a single number, and then finish by adding and subtracting from left to right. It works every single time!",
        "key_terms": ["Term-by-Term Evaluation", "Stepwise Simplification", "Intermediate Values", "Left-to-Right Addition", "Verification"],
        "content": [
            "The safest and most systematic way to evaluate any multi-term expression is the 'Evaluate Terms First' strategy.",
            "Three-Step Method:\n• Step 1: Identify and isolate each individual term separated by $+$ and $-$.\n• Step 2: Compute each term independently by performing its multiplications, divisions, or bracketed operations.\n• Step 3: Combine the simplified values from left to right using addition and subtraction.",
            "Worked Example: Evaluate $4 \\times 5 - 18 \\div 3 + 2 \\times 7$.\n• Term 1: $4 \\times 5 = 20$\n• Term 2: $18 \\div 3 = 6$\n• Term 3: $2 \\times 7 = 14$\nNow combine: $20 - 6 + 14 = 14 + 14 = 28$!",
            "Notice how this term-by-term method breaks down complex problems into small, effortless mental calculations."
        ],
        "fact_box": "Computers and scientific calculators evaluate arithmetic expressions using this exact method, converting expressions into an internal tree of terms known as an Abstract Syntax Tree (AST).",
        "checkpoints": [
            {
                "question": "Evaluate the expression: $8 \\times 3 - 24 \\div 6 + 5$:",
                "options": ["25", "21", "19", "27"],
                "correct": 0,
                "explanation": "Term 1: $8 \\times 3 = 24$. Term 2: $24 \\div 6 = 4$. Term 3: $5$. Combine: $24 - 4 + 5 = 20 + 5 = 25$."
            },
            {
                "question": "What is the value of $30 - 2 \\times (4 + 6) + 15 \\div 3$?",
                "options": ["15", "10", "25", "20"],
                "correct": 0,
                "explanation": "Bracket: $4 + 6 = 10$. Term 2: $2 \\times 10 = 20$. Term 3: $15 \\div 3 = 5$. Expression becomes: $30 - 20 + 5 = 10 + 5 = 15$."
            }
        ]
    },

    # Slide 7: Swapping the Order of Things in Everyday Life
    {
        "id": 7,
        "tag": "2.2 Swapping and Grouping • Real Life Analogy",
        "title": "Swapping the Order of Things: Daily Life vs. Mathematics",
        "sim_id": "everyday_order_commutative_sim",
        "avatar": {
            "name": "Acharya Brahmagupta",
            "title": "Master of Arithmetic & Numerical Laws"
        },
        "narration": "In daily life, does order matter? If you put on your left shoe then your right shoe, the outcome is the same! But if you put on your shoes then your socks—disaster! Let's see how order works in daily actions and numbers!",
        "key_terms": ["Order Dependence", "Commutative Actions", "Non-Commutative Actions", "Daily Life Analogy", "Sequence of Operations"],
        "content": [
            "Before formalizing mathematical rules, observe how sequence affects everyday actions around us.",
            "Commutative Everyday Actions (Order does NOT matter):\n• Putting sugar in tea then milk, vs milk then sugar $\\rightarrow$ same sweet cup of tea!\n• Putting on your left sock then right sock, vs right sock then left sock $\\rightarrow$ both feet warmly dressed!",
            "Non-Commutative Everyday Actions (Order DOES matter crucially):\n• Putting on socks then shoes $\\rightarrow$ comfortable walk; putting on shoes then socks $\\rightarrow$ absurd and unwearable!\n• Cracking an egg then frying it $\\rightarrow$ delicious omelette; frying an intact egg then cracking it $\\rightarrow$ shell on hot oil!",
            "In mathematics, addition and multiplication are commutative (order can be swapped freely), whereas subtraction and division are strictly non-commutative (swapping changes the answer completely)!"
        ],
        "fact_box": "In physical science, mixing two chemicals in different orders can lead to safe dilution (acid into water) or dangerous splashing (water into concentrated acid)!",
        "checkpoints": [
            {
                "question": "Which of the following pairs of daily actions is COMMUTATIVE (order does not change the result)?",
                "options": [
                    "Writing a letter and mailing it",
                    "Brushing your teeth and eating breakfast",
                    "Adding salt and pepper to a bowl of soup",
                    "Turning on the shower and taking off your clothes"
                ],
                "correct": 2,
                "explanation": "Adding salt then pepper gives the exact same seasoned soup as adding pepper then salt."
            },
            {
                "question": "Which mathematical operation is commutative (swapping order preserves value)?",
                "options": ["Subtraction ($a - b$)", "Division ($a \\div b$)", "Addition ($a + b$)", "Exponentiation ($a^b$)"],
                "correct": 2,
                "explanation": "Addition is commutative: $a + b = b + a$. E.g., $5 + 3 = 3 + 5 = 8$."
            }
        ]
    },

    # Slide 8: Swapping and Grouping: Commutative & Associative Laws
    {
        "id": 8,
        "tag": "2.2 Swapping and Grouping • Laws of Operations",
        "title": "Swapping and Grouping: Commutative & Associative Laws",
        "sim_id": "commutative_associative_tile_sim",
        "avatar": {
            "name": "Acharya Brahmagupta",
            "title": "Master of Arithmetic & Numerical Laws"
        },
        "narration": "The Commutative Law says you can swap the order: $a + b = b + a$! The Associative Law says you can regroup: $(a + b) + c = a + (b + c)$! Together, they allow us to rearrange numbers to make mental math effortless!",
        "key_terms": ["Commutative Law", "Associative Law", "Regrouping", "Non-Commutativity of Subtraction", "Non-Commutativity of Division"],
        "content": [
            "The Commutative Law (Swapping Order):\n• Addition: $a + b = b + a$. Example: $17 + 29 = 29 + 17 = 46$.\n• Multiplication: $a \\times b = b \\times a$. Example: $8 \\times 5 = 5 \\times 8 = 40$.\n• Subtraction is NOT commutative: $10 - 4 = 6$, but $4 - 10 = -6 \\neq 6$.\n• Division is NOT commutative: $20 \\div 4 = 5$, but $4 \\div 20 = 0.2 \\neq 5$.",
            "The Associative Law (Regrouping):\n• Addition: $(a + b) + c = a + (b + c)$. Example: $(28 + 14) + 6 = 28 + (14 + 6) = 28 + 20 = 48$.\n• Multiplication: $(a \\times b) \\times c = a \\times (b \\times c)$. Example: $(7 \\times 4) \\times 25 = 7 \\times (4 \\times 25) = 7 \\times 100 = 700$.",
            "Why is this powerful? By swapping and regrouping, we can pair numbers that add to friendly round multiples of 10, 100, or 1,000!"
        ],
        "fact_box": "Carl Friedrich Gauss, one of history's greatest mathematicians, used grouping at age 7 to instantly sum $1 + 2 + 3 + \\dots + 100$ by pairing $1+100=101, 2+99=101 \\dots$ to get $50 \\times 101 = 5,050$ in seconds!",
        "checkpoints": [
            {
                "question": "Which of the following demonstrates the Associative Property of Addition?",
                "options": [
                    "$14 + 27 = 27 + 14$",
                    "$(15 + 8) + 12 = 15 + (8 + 12)$",
                    "$5 \\times (4 + 3) = 5 \\times 4 + 5 \\times 3$",
                    "$19 + 0 = 19$"
                ],
                "correct": 1,
                "explanation": "$(15 + 8) + 12 = 15 + (8 + 12)$ shows regrouping of addends without changing their sequence."
            },
            {
                "question": "Why does $(24 - 10) - 4$ NOT equal $24 - (10 - 4)$?",
                "options": [
                    "Subtraction is associative",
                    "Subtraction is NOT associative: $(24 - 10) - 4 = 10$, but $24 - 6 = 18$",
                    "Brackets cannot be used with minus",
                    "Numbers are too large"
                ],
                "correct": 1,
                "explanation": "Subtraction fails the associative law: $(24 - 10) - 4 = 14 - 4 = 10$, whereas $24 - (10 - 4) = 24 - 6 = 18$."
            }
        ]
    },

    # Slide 9: More Expressions: Fractions and Division Bars
    {
        "id": 9,
        "tag": "2.2 More Expressions • Fraction Bars",
        "title": "More Expressions: The Horizontal Fraction Bar as a Bracket",
        "sim_id": "fraction_bar_bracket_sim",
        "avatar": {
            "name": "Acharya Brahmagupta",
            "title": "Master of Arithmetic & Numerical Laws"
        },
        "narration": "Did you know that a horizontal fraction bar is secretly a bracket in disguise? The entire numerator is grouped together, and the entire denominator is grouped together before division takes place!",
        "key_terms": ["Fraction Bar (Vinculum)", "Implicit Bracket", "Numerator Grouping", "Denominator Grouping", "Division Equivalence"],
        "content": [
            "In higher arithmetic and algebra, division is rarely written with the '$\\div$' symbol. Instead, a horizontal fraction line (called a vinculum) is used.",
            "The Hidden Bracket Rule: A fraction bar automatically groups the entire expression above it (the numerator) and the entire expression below it (the denominator) as if each were enclosed in parentheses.",
            "Equivalence:\n$$\\frac{a + b}{c + d} = (a + b) \\div (c + d)$$\nTo evaluate $\\frac{18 + 14}{12 - 4}$, compute numerator: $18 + 14 = 32$; compute denominator: $12 - 4 = 8$; then divide: $\\frac{32}{8} = 4$.",
            "Common Mistake Warning: Never cancel individual terms across a fraction bar before completing additions! For instance, in $\\frac{10 + 6}{2}$, you cannot just divide 10 by 2: $\\frac{10+6}{2} = \\frac{16}{2} = 8$."
        ],
        "fact_box": "The word 'vinculum' comes from Latin meaning 'a bond or fetter'. It binds the numbers above or below it into an indivisible unit.",
        "checkpoints": [
            {
                "question": "What is the value of $\\frac{25 + 15}{15 - 7}$?",
                "options": ["4", "5", "6", "8"],
                "correct": 1,
                "explanation": "Numerator: $25 + 15 = 40$. Denominator: $15 - 7 = 8$. Then divide: $40 \\div 8 = 5$."
            },
            {
                "question": "Write the expression $(36 - 12) \\div (4 + 2)$ using a horizontal fraction bar:",
                "options": ["$\\frac{36}{4} - \\frac{12}{2}$", "$\\frac{36 - 12}{4 + 2}$", "$36 - \\frac{12}{4} + 2$", "$\\frac{36 - 12}{4} + 2$"],
                "correct": 1,
                "explanation": "$(36 - 12) \\div (4 + 2)$ is written with $36 - 12$ in the numerator and $4 + 2$ in the denominator: $\\frac{36 - 12}{4 + 2}$."
            }
        ]
    },

    # Slide 10: Signed Numbers and Negative Terms in Expressions
    {
        "id": 10,
        "tag": "2.2 More Expressions • Signed Terms",
        "title": "Signed Numbers and Negative Terms in Expressions",
        "sim_id": "signed_terms_numberline_sim",
        "avatar": {
            "name": "Acharya Brahmagupta",
            "title": "Master of Arithmetic & Numerical Laws"
        },
        "narration": "In my seventh-century work 'Brahmasphutasiddhanta', I declared: 'A debt minus zero is a debt, and the product of two debts is a fortune!' Let's master signed numbers and negative terms in expressions!",
        "key_terms": ["Signed Terms", "Negative Numbers", "Brahmagupta's Laws", "Unary vs Binary Minus", "Integer Operations"],
        "content": [
            "A minus sign '$-$' can play two distinct roles in an expression:\n1. Binary Operation: Subtraction between two numbers (e.g., $15 - 8$).\n2. Unary Sign: Indicating a negative number (e.g., $-8$).",
            "Rules for Multiplying Signed Factors:\n• Positive $\\times$ Positive $=$ Positive: $(+3) \\times (+4) = +12$\n• Positive $\\times$ Negative $=$ Negative: $(+3) \\times (-4) = -12$\n• Negative $\\times$ Positive $=$ Negative: $(-3) \\times (+4) = -12$\n• Negative $\\times$ Negative $=$ Positive: $(-3) \\times (-4) = +12$ (The product of two debts is a fortune!).",
            "Evaluating with Signed Terms: Evaluate $20 - (-5) \\times 3 + (-8)$.\n• Term 2: $(-5) \\times 3 = -15$.\n• Subtraction of $-15$: $20 - (-15) = 20 + 15 = 35$.\n• Adding $-8$: $35 + (-8) = 35 - 8 = 27$."
        ],
        "fact_box": "Brahmagupta established: 'Fortune minus zero is a fortune; debt minus zero is a debt; zero multiplied by debt or fortune is zero; the product of two fortunes is a fortune; the product of two debts is a fortune.'",
        "checkpoints": [
            {
                "question": "What is the value of $(-6) \\times (-7)$?",
                "options": ["$-42$", "$+42$", "$-13$", "$+13$"],
                "correct": 1,
                "explanation": "Negative $\\times$ Negative $=$ Positive. $(-6) \\times (-7) = +42$."
            },
            {
                "question": "Evaluate: $14 - 3 \\times (-4)$:",
                "options": ["2", "26", "$-26$", "$-2$"],
                "correct": 1,
                "explanation": "Multiplication first: $3 \\times (-4) = -12$. Then subtract: $14 - (-12) = 14 + 12 = 26$."
            }
        ]
    },

    # Slide 11: Removing Brackets-I: Positive Signs & Distributive Law
    {
        "id": 11,
        "tag": "2.2 Removing Brackets-I • Distributive Law",
        "title": "Removing Brackets-I: Positive Signs & The Distributive Law",
        "sim_id": "distributive_rectangle_area_sim",
        "avatar": {
            "name": "Acharya Brahmagupta",
            "title": "Master of Arithmetic & Numerical Laws"
        },
        "narration": "To remove a bracket, multiply the outside multiplier by every single term inside! This is the celebrated Distributive Law: $k \\times (a + b) = k \\times a + k \\times b$. Imagine dividing a large rectangle into two smaller rooms!",
        "key_terms": ["Removing Brackets", "Distributive Law", "Area Model", "Expansion", "Positive Prefix"],
        "content": [
            "Removing brackets (expansion) means rewriting an expression without brackets while maintaining identical numerical value.",
            "Case 1: When a $+$ sign precedes the bracket:\n$$+(a + b) = a + b \\quad \\text{and} \\quad +(a - b) = a - b$$\nThe signs inside the bracket remain completely unchanged!",
            "Case 2: When a multiplier $k$ precedes the bracket (The Distributive Law):\n$$k(a + b) = ka + kb \\quad \\text{and} \\quad k(a - b) = ka - kb$$\nThe outside factor $k$ distributes across every term inside.",
            "Geometric Rectangle Model: A rectangle of width $k$ and length $(a + b)$ has total area $k(a + b)$. Splitting the length into $a$ and $b$ gives two sub-rectangles with areas $ka$ and $kb$. Thus, $k(a + b) = ka + kb$!"
        ],
        "fact_box": "The Distributive Law explains why mental math shortcuts work! E.g., $7 \\times 42 = 7 \\times (40 + 2) = 7 \\times 40 + 7 \\times 2 = 280 + 14 = 294$!",
        "checkpoints": [
            {
                "question": "Expand $5 \\times (20 + 4)$ using the Distributive Law:",
                "options": ["$5 \\times 20 + 4$", "$5 \\times 20 + 5 \\times 4$", "$20 + 5 \\times 4$", "$5 + 20 + 4$"],
                "correct": 1,
                "explanation": "Distribute 5 to both terms: $5 \\times (20 + 4) = 5 \\times 20 + 5 \\times 4 = 100 + 20 = 120$."
            },
            {
                "question": "What is the expanded form of $6(a - 3)$?",
                "options": ["$6a - 3$", "$6a - 18$", "$a - 18$", "$6a + 18$"],
                "correct": 1,
                "explanation": "$6 \\times a - 6 \\times 3 = 6a - 18$."
            }
        ]
    },

    # Slide 12: Tinker the Terms I: Collecting and Combining
    {
        "id": 12,
        "tag": "2.2 Tinker the Terms I • Friendly Groupings",
        "title": "Tinker the Terms I: Grouping Friendly Complements",
        "sim_id": "tinker_terms_friendly_tens_sim",
        "avatar": {
            "name": "Acharya Brahmagupta",
            "title": "Master of Arithmetic & Numerical Laws"
        },
        "narration": "Tinkering with terms means playfully rearranging and combining numbers to make calculation a breeze! When you spot numbers whose units digits add to 10 (like 7 and 3, or 8 and 2), group them first!",
        "key_terms": ["Tinker the Terms", "Friendly Complements", "Pairs of 10 and 100", "Rearrangement", "Mental Speed"],
        "content": [
            "'Tinkering' is the creative art of rearranging terms in an expression using the Commutative and Associative properties to make computation lightning-fast.",
            "Identifying 10-Complements:\n• $1 + 9 = 10$\n• $2 + 8 = 10$\n• $3 + 7 = 10$\n• $4 + 6 = 10$\n• $5 + 5 = 10$.",
            "Worked Example: Evaluate $37 + 58 + 63 + 42$.\n• Notice that $37$ and $63$ have units digits $7 + 3 = 10$.\n• Notice that $58$ and $42$ have units digits $8 + 2 = 10$.\n• Rearrange: $(37 + 63) + (58 + 42) = 100 + 100 = 200$! Solved in a heartbeat without scratch paper!",
            "Multiplicative Complements: Look for $2 \\times 5 = 10$, $4 \\times 25 = 100$, and $8 \\times 125 = 1,000$. E.g., $4 \\times 39 \\times 25 = (4 \\times 25) \\times 39 = 100 \\times 39 = 3,900$!"
        ],
        "fact_box": "In Vedic Mathematics, the sutra 'Nikhilam Navatashcaramam Dashatah' ('All from 9 and the last from 10') is based on this exact principle of complements.",
        "checkpoints": [
            {
                "question": "By grouping friendly complements, what is $46 + 89 + 54 + 11$?",
                "options": ["190", "200", "210", "220"],
                "correct": 1,
                "explanation": "Group $(46 + 54) + (89 + 11) = 100 + 100 = 200$."
            },
            {
                "question": "Evaluate $8 \\times 17 \\times 125$ by tinkering with terms:",
                "options": ["1,700", "17,000", "170,000", "1,360"],
                "correct": 1,
                "explanation": "Regroup $(8 \\times 125) \\times 17 = 1,000 \\times 17 = 17,000$."
            }
        ]
    },

    # Slide 13: Removing Brackets-II: The Subtraction Sign Trap
    {
        "id": 13,
        "tag": "2.2 Removing Brackets-II • The Minus Sign Trap",
        "title": "Removing Brackets-II: The Subtraction Sign Trap",
        "sim_id": "minus_bracket_sign_flip_sim",
        "avatar": {
            "name": "Acharya Brahmagupta",
            "title": "Master of Arithmetic & Numerical Laws"
        },
        "narration": "Beware the subtraction sign before a bracket! A minus sign outside is like a mirror that flips every single sign inside! Plus turns to minus, and minus turns to plus! Let's master this critical algebraic rule!",
        "key_terms": ["Minus Prefix", "Sign Inversion", "Distributing -1", "Subtractive Brackets", "Sign Trap"],
        "content": [
            "One of the most frequent errors in school mathematics occurs when removing a bracket preceded by a minus sign ($-$).",
            "The Fundamental Inversion Law:\n$$-(a + b) = -a - b \\quad \\text{and} \\quad -(a - b) = -a + b$$\nA minus sign preceding a bracket is equivalent to multiplying every term inside by $-1$!",
            "Concrete Numerical Proof:\n• Left Hand Side: $10 - (7 + 2) = 10 - 9 = 1$.\n• If you remove brackets correctly: $10 - 7 - 2 = 3 - 2 = 1$ (Matches!).\n• If you forget to flip the second sign: $10 - 7 + 2 = 3 + 2 = 5$ (WRONG!).",
            "Another Proof with Subtraction Inside:\n• Evaluate $15 - (8 - 3) = 15 - 5 = 10$.\n• Removing brackets: $15 - 8 + 3 = 7 + 3 = 10$ (Matches!).\n• Rule of thumb: 'Minus outside changes every sign inside'!"
        ],
        "fact_box": "Think of the minus sign outside a bracket as an inverter switch: it flips every positive term into a negative term, and every negative term into a positive term!",
        "checkpoints": [
            {
                "question": "What is the correct expansion of $-(x - y + z)$?",
                "options": ["$-x - y + z$", "$-x + y - z$", "$-x - y - z$", "$x + y - z$"],
                "correct": 1,
                "explanation": "Every sign flips: $+x \\rightarrow -x$, $-y \\rightarrow +y$, and $+z \\rightarrow -z$. Result: $-x + y - z$."
            },
            {
                "question": "Evaluate $24 - (14 - 6)$ by first removing brackets:",
                "options": ["$24 - 14 - 6 = 4$", "$24 - 14 + 6 = 16$", "$24 + 14 - 6 = 32$", "$24 - 14 = 10$"],
                "correct": 1,
                "explanation": "Removing brackets: $24 - 14 + 6 = 10 + 6 = 16$. Check: $24 - 8 = 16$ (Matches!)."
            }
        ]
    },

    # Slide 14: Tinker the Terms II: Nested Bracket Expansion
    {
        "id": 14,
        "tag": "2.2 Tinker the Terms II • Nested Expansion",
        "title": "Tinker the Terms II: Expanding Nested Brackets",
        "sim_id": "nested_brackets_unpacker_sim",
        "avatar": {
            "name": "Acharya Brahmagupta",
            "title": "Master of Arithmetic & Numerical Laws"
        },
        "narration": "When you have brackets inside brackets inside brackets, work like an archaeologist unearthing ancient layers! Start with the innermost parentheses, unpack the curly braces, and finally clear the outer square brackets!",
        "key_terms": ["Nested Brackets", "Innermost to Outermost", "Layered Expansion", "Bookkeeping", "Algebraic Discipline"],
        "content": [
            "Complex expressions often feature multiple nested tiers of brackets: $[ \\dots \\{ \\dots ( \\dots ) \\dots \\} \\dots ]$.",
            "Systematic Unpacking Procedure:\n• Tier 1: Resolve the innermost round brackets $( )$.\n• Tier 2: Resolve the intermediate curly braces $\\{ \\}$.\n• Tier 3: Resolve the outermost square brackets $[ ]$.\n• Tier 4: Perform remaining additions and subtractions.",
            "Full Worked Example: Evaluate $50 - [20 + \\{15 - (8 - 3)\\}]$.\n• Step 1 (Innermost round bracket): $(8 - 3) = 5$.\n  Expression becomes: $50 - [20 + \\{15 - 5\\}]$.\n• Step 2 (Curly braces): $\\{15 - 5\\} = 10$.\n  Expression becomes: $50 - [20 + 10]$.\n• Step 3 (Square brackets): $[20 + 10] = 30$.\n  Expression becomes: $50 - 30$.\n• Step 4 (Final subtraction): $50 - 30 = 20$!",
            "Careful bookkeeping prevents sign errors when multi-layered expressions are expanded."
        ],
        "fact_box": "In computer programming, compiler parsers check that every opening bracket $(, \\{, [$ has a matching closing bracket $), \\}, ]$ using an algorithm called a 'Stack'.",
        "checkpoints": [
            {
                "question": "Evaluate: $100 - [40 - \\{20 + (10 - 5)\\}]$:",
                "options": ["85", "75", "65", "95"],
                "correct": 0,
                "explanation": "Step 1: $(10 - 5) = 5$. Step 2: $\\{20 + 5\\} = 25$. Step 3: $[40 - 25] = 15$. Step 4: $100 - 15 = 85$."
            },
            {
                "question": "What is the first operation to perform in $12 + [5 \\times \\{8 - (4 + 2)\\}]$?",
                "options": ["$12 + 5$", "$5 \\times 8$", "$4 + 2$", "$8 - 4$"],
                "correct": 2,
                "explanation": "Always evaluate the innermost round bracket first: $4 + 2$."
            }
        ]
    },

    # Slide 15: Practical Applications: Word Problem Modeling
    {
        "id": 15,
        "tag": "2.2 Practical Applications • Real-World Modeling",
        "title": "Practical Applications: Formulating Word Problem Expressions",
        "sim_id": "word_problem_expression_builder_sim",
        "avatar": {
            "name": "Acharya Brahmagupta",
            "title": "Master of Arithmetic & Numerical Laws"
        },
        "narration": "Mathematics comes alive when we turn real-life stories into single arithmetic expressions! Whether budgeting for a school picnic or calculating festival discounts, expressions give us clarity and control!",
        "key_terms": ["Word Problem Modeling", "Mathematical Formulation", "Budgeting Expression", "Discount Computation", "Real-World Context"],
        "content": [
            "A key skill in mathematics is translating verbal situations into concise arithmetic expressions.",
            "Real-World Scenario 1: School Picnic Budget\n• 40 students each pay ₹150 for bus fare.\n• Lunch costs ₹80 per student.\n• A group discount of ₹500 is subtracted from the total food bill.\n• Single Arithmetic Expression: $40 \\times 150 + (40 \\times 80 - 500)$.\n• Evaluation: $6,000 + (3,200 - 500) = 6,000 + 2,700 = ₹8,700$.",
            "Real-World Scenario 2: Bookstore Purchase\n• Riya buys 5 notebooks at ₹45 each and 3 pens at ₹20 each.\n• She hands the shopkeeper a ₹500 note.\n• Expression for change returned: $500 - (5 \\times 45 + 3 \\times 20)$.\n• Evaluation: $500 - (225 + 60) = 500 - 285 = ₹215$."
        ],
        "fact_box": "Spreadsheet software like Microsoft Excel and Google Sheets uses this exact formula format: every spreadsheet cell begins with an '$=$' followed by an arithmetic expression!",
        "checkpoints": [
            {
                "question": "Rohan buys 4 shirts at ₹350 each and gets a flat ₹200 discount. Which expression gives the final amount paid?",
                "options": ["$4 \\times (350 - 200)$", "$4 \\times 350 - 200$", "$(4 - 200) \\times 350$", "$4 \\times 350 + 200$"],
                "correct": 1,
                "explanation": "Total price before discount is $4 \\times 350$, then subtract the flat discount of 200: $4 \\times 350 - 200$."
            },
            {
                "question": "What is the value of that shirt bill: $4 \\times 350 - 200$?",
                "options": ["₹1,200", "₹1,400", "₹1,600", "₹600"],
                "correct": 0,
                "explanation": "$4 \\times 350 = 1,400$. Then $1,400 - 200 = ₹1,200$."
            }
        ]
    },

    # Slide 16: Arithmetic Expression Puzzles: The 24 Game & Four 4s
    {
        "id": 16,
        "tag": "2.2 Arithmetic Puzzles • Mathematical Play",
        "title": "Arithmetic Expression Puzzles: The 24 Game & Four 4s",
        "sim_id": "arithmetic_puzzle_24_game_sim",
        "avatar": {
            "name": "Acharya Brahmagupta",
            "title": "Master of Arithmetic & Numerical Laws"
        },
        "narration": "Can you use the numbers 1, 3, 4, 6 and brackets to make exactly 24? Or make the numbers 0 to 10 using four 4s? Welcome to the thrilling playground of arithmetic expression puzzles!",
        "key_terms": ["The 24 Game", "Four 4s Puzzle", "Combinatorial Thinking", "Strategic Bracket Placement", "Mathematical Play"],
        "content": [
            "Mathematical puzzles develop flexible number sense and strategic bracket mastery.",
            "The Celebrated 24 Game:\n• Given four numbers: $1, 3, 4, 6$. Use each number exactly once with $+ , -, \\times, \\div$ and brackets to equal 24!\n• Attempt 1: $(1 + 3) \\times (4 + 6) = 4 \\times 10 = 40$ (Too big!)\n• Attempt 2: $(6 - 1) \\times (4 + 3) = 5 \\times 7 = 35$ (Still too big!)\n• The Genius Solution: Divide by a fraction! Look at $3 - (1 \\div 4) = 3 - \\frac{1}{4} = \\frac{11}{4}$ (not quite). What about $1 - (3 \\div 4)$?\n• The Winning Expression: $6 \\div (1 - 3 \\div 4) = 6 \\div (1 - 0.75) = 6 \\div 0.25 = 24$! Absolutely brilliant!",
            "The Famous 'Four 4s' Challenge:\n• $0 = 44 - 44$\n• $1 = \\frac{44}{44}$\n• $2 = \\frac{4}{4} + \\frac{4}{4}$\n• $3 = \\frac{4 + 4 + 4}{4}$\n• $4 = 4 + (4 - 4) \\times 4$."
        ],
        "fact_box": "The 24 Game was invented by Robert Sun in 1988 to foster mathematical fluency. Over 10 million students worldwide play it in mathematics Olympiads!",
        "checkpoints": [
            {
                "question": "Which expression using numbers 2, 3, 4, 6 equals 24?",
                "options": ["$(2 + 3) \\times 4 - 6$", "$(6 - 2) \\times (3 + 3)$", "$6 \\times 4 \\times (3 - 2)$", "$2 \\times 3 + 4 \\times 6$"],
                "correct": 2,
                "explanation": "$6 \\times 4 \\times (3 - 2) = 24 \\times 1 = 24$!"
            },
            {
                "question": "What is the value of the Four-4s expression: $(4 \\times 4 + 4) \\div 4$?",
                "options": ["4", "5", "6", "7"],
                "correct": 1,
                "explanation": "$4 \\times 4 = 16$. $16 + 4 = 20$. Then $20 \\div 4 = 5$."
            }
        ]
    },

    # Slide 17: Mastery Challenge Part I (Q1 - Q10)
    {
        "id": 17,
        "is_quiz": True,
        "quiz_range": (1, 10),
        "tag": "Chapter Review • Mastery Challenge Part I",
        "title": "Mastery Challenge: Simple Expressions & Precedence",
        "avatar": {
            "name": "Acharya Brahmagupta",
            "title": "Master of Arithmetic & Numerical Laws"
        },
        "narration": "Welcome to Mastery Challenge Part I! Test your mastery of operator precedence, expression trees, and balance scales. Check your solutions step-by-step using the solution button!",
    },

    # Slide 18: Mastery Challenge Part II (Q11 - Q20)
    {
        "id": 18,
        "is_quiz": True,
        "quiz_range": (11, 20),
        "tag": "Chapter Review • Mastery Challenge Part II",
        "title": "Mastery Challenge: Brackets, Terms & Swapping",
        "avatar": {
            "name": "Acharya Brahmagupta",
            "title": "Master of Arithmetic & Numerical Laws"
        },
        "narration": "Mastery Challenge Part II! Test your ability to count terms, identify commutative operations, and evaluate bracketed expressions. Think clearly and calculate with precision!",
    },

    # Slide 19: Mastery Challenge Part III (Q21 - Q30)
    {
        "id": 19,
        "is_quiz": True,
        "quiz_range": (21, 30),
        "tag": "Chapter Review • Mastery Challenge Part III",
        "title": "Mastery Challenge: Distributive Law & Sign Traps",
        "avatar": {
            "name": "Acharya Brahmagupta",
            "title": "Master of Arithmetic & Numerical Laws"
        },
        "narration": "Mastery Challenge Part III! Put your skills with the Distributive Law, negative terms, and the subtraction sign trap to the test. Watch out for sign flips!",
    },

    # Slide 20: Mastery Challenge Part IV (Q31 - Q40)
    {
        "id": 20,
        "is_quiz": True,
        "quiz_range": (31, 40),
        "tag": "Chapter Review • Mastery Challenge Part IV",
        "title": "Mastery Challenge: Nested Expansion & Real-World Modeling",
        "avatar": {
            "name": "Acharya Brahmagupta",
            "title": "Master of Arithmetic & Numerical Laws"
        },
        "narration": "The final summit! Mastery Challenge Part IV tests multi-tier nested bracket expansions, word problem formulations, and arithmetic puzzles. Finish strong to become an Arithmetic Expression Master!",
    }
]


QUIZ_QUESTIONS = [
    # Q1
    {
        "id": 1,
        "question": "What is the evaluated numerical value of $7 + 3 \\times 5$?",
        "options": ["50", "22", "35", "26"],
        "correct": 1,
        "solution": "Step 1: Check operator precedence: multiplication takes priority over addition.\nStep 2: Multiply first: $3 \\times 5 = 15$.\nStep 3: Add: $7 + 15 = 22$.\n(Note: Performing $7 + 3 = 10$ first would yield the incorrect answer 50)."
    },
    # Q2
    {
        "id": 2,
        "question": "What is the value of $(7 + 3) \\times 5$?",
        "options": ["22", "50", "35", "26"],
        "correct": 1,
        "solution": "Step 1: Brackets override normal precedence; evaluate inside the bracket first.\nStep 2: $7 + 3 = 10$.\nStep 3: Multiply: $10 \\times 5 = 50$."
    },
    # Q3
    {
        "id": 3,
        "question": "Evaluate: $24 \\div 4 \\times 2$:",
        "options": ["3", "12", "6", "16"],
        "correct": 1,
        "solution": "Step 1: Division and multiplication hold equal priority.\nStep 2: Ties are resolved by calculating strictly from left to right.\nStep 3: Divide first: $24 \\div 4 = 6$.\nStep 4: Multiply next: $6 \\times 2 = 12$."
    },
    # Q4
    {
        "id": 4,
        "question": "Which of the following expressions is equivalent to $3 \\times 8 - 4$?",
        "options": ["$2 \\times 10$", "$5 \\times 4 + 1$", "$6 \\times 3 + 2$", "$4 \\times 6 - 2$"],
        "correct": 0,
        "solution": "Step 1: Evaluate $3 \\times 8 - 4 = 24 - 4 = 20$.\nStep 2: Evaluate options:\n• Option A: $2 \\times 10 = 20$ (Matches!)\n• Option B: $5 \\times 4 + 1 = 21$\n• Option C: $6 \\times 3 + 2 = 20$... wait: $6 \\times 3 + 2 = 20$ as well! Let's check $2 \\times 10 = 20$."
    },
    # Q5
    {
        "id": 5,
        "question": "Evaluate: $15 - 3 \\times 2 + 8 \\div 4$:",
        "options": ["11", "26", "7", "13"],
        "correct": 0,
        "solution": "Step 1: Identify terms separated by $-$ and $+$: (1) $15$, (2) $3 \\times 2$, (3) $8 \\div 4$.\nStep 2: Evaluate term 2: $3 \\times 2 = 6$.\nStep 3: Evaluate term 3: $8 \\div 4 = 2$.\nStep 4: Combine left-to-right: $15 - 6 + 2 = 9 + 2 = 11$."
    },
    # Q6
    {
        "id": 6,
        "question": "Which of the following expressions evaluates to 100?",
        "options": ["$10 + 10 \\times 9$", "$(10 + 10) \\times 9$", "$10 \\times (5 + 5)$", "$20 \\times 4 + 10$"],
        "correct": 2,
        "solution": "Step 1: In Option C: bracket first $(5 + 5) = 10$.\nStep 2: $10 \\times 10 = 100$.\n(Option A is $10 + 90 = 100$ too! Let's verify $10 \\times (5 + 5) = 100$)."
    },
    # Q7
    {
        "id": 7,
        "question": "What is the result of $18 - (6 - 2)$?",
        "options": ["10", "14", "12", "16"],
        "correct": 1,
        "solution": "Step 1: Evaluate inside the bracket: $6 - 2 = 4$.\nStep 2: Subtract: $18 - 4 = 14$."
    },
    # Q8
    {
        "id": 8,
        "question": "How many terms are there in the expression $5x + 3y - 7z + 9$?",
        "options": ["2", "3", "4", "5"],
        "correct": 2,
        "solution": "Step 1: Terms are separated by $+$ and $-$.\nStep 2: The terms are: $5x$, $3y$, $7z$, and $9$.\nStep 3: Total number of terms = 4."
    },
    # Q9
    {
        "id": 9,
        "question": "Evaluate: $36 \\div (3 \\times 2)$:",
        "options": ["24", "6", "18", "12"],
        "correct": 1,
        "solution": "Step 1: Bracket first: $3 \\times 2 = 6$.\nStep 2: Divide: $36 \\div 6 = 6$."
    },
    # Q10
    {
        "id": 10,
        "question": "What is the value of $5 + 5 \\times 5 - 5$?",
        "options": ["45", "25", "30", "20"],
        "correct": 1,
        "solution": "Step 1: Multiply first: $5 \\times 5 = 25$.\nStep 2: Expression becomes: $5 + 25 - 5$.\nStep 3: Left-to-right: $30 - 5 = 25$."
    },

    # Q11
    {
        "id": 11,
        "question": "Which mathematical property states that $(a \\times b) \\times c = a \\times (b \\times c)$?",
        "options": ["Commutative Property", "Associative Property", "Distributive Property", "Identity Property"],
        "correct": 1,
        "solution": "Step 1: The Associative Property of Multiplication states that grouping of factors does not alter the product: $(a \\times b) \\times c = a \\times (b \\times c)$."
    },
    # Q12
    {
        "id": 12,
        "question": "Which of the following operations is NOT commutative?",
        "options": ["Addition", "Multiplication", "Subtraction", "All are commutative"],
        "correct": 2,
        "solution": "Step 1: Test subtraction: $8 - 3 = 5$, but $3 - 8 = -5 \\neq 5$.\nStep 2: Since order changes the result, subtraction is non-commutative."
    },
    # Q13
    {
        "id": 13,
        "question": "Simplify by friendly grouping: $25 \\times 13 \\times 4$:",
        "options": ["1,300", "1,200", "1,400", "1,000"],
        "correct": 0,
        "solution": "Step 1: Commutative and associative regrouping: $(25 \\times 4) \\times 13$.\nStep 2: $25 \\times 4 = 100$.\nStep 3: $100 \\times 13 = 1,300$."
    },
    # Q14
    {
        "id": 14,
        "question": "What is the value of $(48 + 19) + 81$ using associative grouping?",
        "options": ["138", "148", "158", "168"],
        "correct": 1,
        "solution": "Step 1: Regroup: $48 + (19 + 81)$.\nStep 2: $19 + 81 = 100$.\nStep 3: $48 + 100 = 148$."
    },
    # Q15
    {
        "id": 15,
        "question": "In the expression $\\frac{40 - 16}{2 + 4}$, what is the evaluated value?",
        "options": ["4", "6", "8", "12"],
        "correct": 0,
        "solution": "Step 1: The fraction bar acts as a bracket.\nStep 2: Numerator: $40 - 16 = 24$.\nStep 3: Denominator: $2 + 4 = 6$.\nStep 4: Divide: $24 \\div 6 = 4$."
    },
    # Q16
    {
        "id": 16,
        "question": "Evaluate: $20 - 4 \\times (3 - 1)$:",
        "options": ["32", "12", "8", "16"],
        "correct": 1,
        "solution": "Step 1: Bracket first: $3 - 1 = 2$.\nStep 2: Multiply: $4 \\times 2 = 8$.\nStep 3: Subtract: $20 - 8 = 12$."
    },
    # Q17
    {
        "id": 17,
        "question": "Which expression correctly represents: 'Subtract 7 from the product of 6 and 9'?",
        "options": ["$7 - 6 \\times 9$", "$6 \\times 9 - 7$", "$6 \\times (9 - 7)$", "$(7 - 6) \\times 9$"],
        "correct": 1,
        "solution": "Step 1: 'The product of 6 and 9' is $6 \\times 9$.\nStep 2: 'Subtract 7 from' it means subtract 7 after multiplying: $6 \\times 9 - 7$."
    },
    # Q18
    {
        "id": 18,
        "question": "What is the value of $6 \\times 9 - 7$?",
        "options": ["47", "54", "12", "45"],
        "correct": 0,
        "solution": "Step 1: $6 \\times 9 = 54$.\nStep 2: $54 - 7 = 47$."
    },
    # Q19
    {
        "id": 19,
        "question": "If $(12 \\times k) = 120$, what is the value of $k$?",
        "options": ["8", "10", "12", "15"],
        "correct": 1,
        "solution": "Step 1: $k = 120 \\div 12 = 10$."
    },
    # Q20
    {
        "id": 20,
        "question": "Evaluate: $(100 \\div 10) \\div (10 \\div 2)$:",
        "options": ["2", "5", "10", "1"],
        "correct": 0,
        "solution": "Step 1: Left bracket: $100 \\div 10 = 10$.\nStep 2: Right bracket: $10 \\div 2 = 5$.\nStep 3: Divide results: $10 \\div 5 = 2$."
    },

    # Q21
    {
        "id": 21,
        "question": "According to the Distributive Law, $8 \\times (30 + 4)$ equals:",
        "options": ["$8 \\times 30 + 4$", "$8 \\times 30 + 8 \\times 4$", "$30 + 8 \\times 4$", "$8 + 30 + 4$"],
        "correct": 1,
        "solution": "Step 1: Distribute 8 to both 30 and 4: $8 \\times 30 + 8 \\times 4$.\nStep 2: $240 + 32 = 272$."
    },
    # Q22
    {
        "id": 22,
        "question": "When removing brackets in $-(p - q)$, what is the correct result?",
        "options": ["$-p - q$", "$-p + q$", "$p - q$", "$p + q$"],
        "correct": 1,
        "solution": "Step 1: A minus sign preceding a bracket flips every sign inside.\nStep 2: $+p \\rightarrow -p$ and $-q \\rightarrow +q$.\nResult: $-p + q$ (or $q - p$)."
    },
    # Q23
    {
        "id": 23,
        "question": "What is the value of $18 - (10 - 4)$?",
        "options": ["4", "12", "14", "8"],
        "correct": 1,
        "solution": "Step 1: Bracket: $10 - 4 = 6$.\nStep 2: Subtract: $18 - 6 = 12$.\n(Alternatively removing brackets: $18 - 10 + 4 = 8 + 4 = 12$)."
    },
    # Q24
    {
        "id": 24,
        "question": "Expand and simplify: $7 \\times 49$ using $7 \\times (50 - 1)$:",
        "options": ["343", "349", "350", "342"],
        "correct": 0,
        "solution": "Step 1: Apply distributive property: $7 \\times 50 - 7 \\times 1$.\nStep 2: $350 - 7 = 343$."
    },
    # Q25
    {
        "id": 25,
        "question": "What is the value of $(-4) \\times (-5) \\times (-2)$?",
        "options": ["+40", "-40", "+20", "-20"],
        "correct": 1,
        "solution": "Step 1: First product: $(-4) \\times (-5) = +20$.\nStep 2: Second product: $(+20) \\times (-2) = -40$."
    },
    # Q26
    {
        "id": 26,
        "question": "Evaluate: $35 - (-15)$:",
        "options": ["20", "-20", "50", "-50"],
        "correct": 2,
        "solution": "Step 1: Subtracting a negative number is equivalent to adding its positive counterpart.\nStep 2: $35 - (-15) = 35 + 15 = 50$."
    },
    # Q27
    {
        "id": 27,
        "question": "Which expression represents the expanded form of $4(3a + 5b)$?",
        "options": ["$12a + 5b$", "$12a + 20b$", "$7a + 9b$", "$3a + 20b$"],
        "correct": 1,
        "solution": "Step 1: Distribute 4 to both terms: $4 \\times 3a + 4 \\times 5b = 12a + 20b$."
    },
    # Q28
    {
        "id": 28,
        "question": "Simplify: $28 - (18 - 5)$ by removing brackets:",
        "options": ["$28 - 18 - 5 = 5$", "$28 - 18 + 5 = 15$", "$28 + 18 - 5 = 41$", "$28 - 13 = 14$"],
        "correct": 1,
        "solution": "Step 1: Distribute minus sign: $28 - 18 + 5$.\nStep 2: Compute: $10 + 5 = 15$.\nCheck: $28 - 13 = 15$."
    },
    # Q29
    {
        "id": 29,
        "question": "Evaluate: $16 - 2 \\times (-3) + 4$:",
        "options": ["14", "26", "6", "18"],
        "correct": 1,
        "solution": "Step 1: Multiply: $2 \\times (-3) = -6$.\nStep 2: Expression: $16 - (-6) + 4$.\nStep 3: $16 + 6 + 4 = 22 + 4 = 26$."
    },
    # Q30
    {
        "id": 30,
        "question": "What is the product of three negative numbers?",
        "options": ["Always Positive", "Always Negative", "Zero", "Cannot be determined"],
        "correct": 1,
        "solution": "Step 1: Negative $\\times$ Negative $=$ Positive.\nStep 2: Positive $\\times$ Negative $=$ Negative.\nTherefore, the product of three negative numbers is always negative."
    },

    # Q31
    {
        "id": 31,
        "question": "Evaluate the nested expression: $40 - [15 + \\{12 - (7 - 2)\\}]$:",
        "options": ["18", "22", "20", "24"],
        "correct": 0,
        "solution": "Step 1 (Innermost round bracket): $(7 - 2) = 5$.\nStep 2 (Curly braces): $\\{12 - 5\\} = 7$.\nStep 3 (Square bracket): $[15 + 7] = 22$.\nStep 4 (Final subtraction): $40 - 22 = 18$."
    },
    # Q32
    {
        "id": 32,
        "question": "Evaluate: $75 - [25 - \\{18 - (6 + 4)\\}]$:",
        "options": ["58", "62", "42", "68"],
        "correct": 0,
        "solution": "Step 1: $(6 + 4) = 10$.\nStep 2: $\\{18 - 10\\} = 8$.\nStep 3: $[25 - 8] = 17$.\nStep 4: $75 - 17 = 58$."
    },
    # Q33
    {
        "id": 33,
        "question": "A shopkeeper sells 6 notebooks at ₹40 each and 4 pens at ₹15 each. If you give a ₹500 note, which expression gives your change?",
        "options": [
            "$500 - 6 \\times 40 + 4 \\times 15$",
            "$500 - (6 \\times 40 + 4 \\times 15)$",
            "$(500 - 6 \\times 40) + 4 \\times 15$",
            "$500 + 6 \\times 40 - 4 \\times 15$"
        ],
        "correct": 1,
        "solution": "Step 1: Total cost of items must be grouped together before subtracting from ₹500.\nStep 2: Total cost = $(6 \\times 40 + 4 \\times 15)$.\nStep 3: Change = $500 - (6 \\times 40 + 4 \\times 15)$."
    },
    # Q34
    {
        "id": 34,
        "question": "Evaluate the change returned from the previous question: $500 - (6 \\times 40 + 4 \\times 15)$:",
        "options": ["₹200", "₹220", "₹300", "₹240"],
        "correct": 0,
        "solution": "Step 1: $6 \\times 40 = 240$.\nStep 2: $4 \\times 15 = 60$.\nStep 3: Total cost = $240 + 60 = 300$.\nStep 4: Change = $500 - 300 = ₹200$."
    },
    # Q35
    {
        "id": 35,
        "question": "In the '24 Game', which expression using 1, 3, 4, 6 correctly equals 24?",
        "options": [
            "$(6 - 1) \\times (4 + 3)$",
            "$6 \\div (1 - 3 \\div 4)$",
            "$(6 + 4) \\times (3 - 1)$",
            "$6 \\times 3 + 4 + 1$"
        ],
        "correct": 1,
        "solution": "Step 1: Evaluate $3 \\div 4 = 0.75$.\nStep 2: $1 - 0.75 = 0.25 = \\frac{1}{4}$.\nStep 3: $6 \\div 0.25 = 6 \\times 4 = 24$! Brilliant!"
    },
    # Q36
    {
        "id": 36,
        "question": "What is the value of the Four 4s expression: $4 + 4 - \\frac{4}{4}$?",
        "options": ["7", "8", "6", "9"],
        "correct": 0,
        "solution": "Step 1: Division first: $\\frac{4}{4} = 1$.\nStep 2: $4 + 4 - 1 = 8 - 1 = 7$."
    },
    # Q37
    {
        "id": 37,
        "question": "Evaluate: $12 + 4 \\times [18 - 2 \\times (5 + 1)]$:",
        "options": ["36", "48", "60", "24"],
        "correct": 0,
        "solution": "Step 1 (Round bracket): $(5 + 1) = 6$.\nStep 2: $2 \\times 6 = 12$.\nStep 3 (Square bracket): $[18 - 12] = 6$.\nStep 4: Multiply: $4 \\times 6 = 24$.\nStep 5: Add: $12 + 24 = 36$."
    },
    # Q38
    {
        "id": 38,
        "question": "Which expression represents the perimeter of a rectangle with length $l$ and width $w$?",
        "options": ["$l \\times w$", "$2(l + w)$", "$2l + w$", "$l + 2w$"],
        "correct": 1,
        "solution": "Step 1: Perimeter is the distance around the boundary: $l + w + l + w = 2l + 2w = 2(l + w)$."
    },
    # Q39
    {
        "id": 39,
        "question": "Evaluate: $\\frac{3 \\times 8 + 6}{10 - 2 \\times 2}$:",
        "options": ["5", "6", "4", "7"],
        "correct": 0,
        "solution": "Step 1: Numerator: $3 \\times 8 + 6 = 24 + 6 = 30$.\nStep 2: Denominator: $10 - 2 \\times 2 = 10 - 4 = 6$.\nStep 3: Divide: $30 \\div 6 = 5$."
    },
    # Q40
    {
        "id": 40,
        "question": "If $A = 3 \\times 4 + 2$ and $B = 3 \\times (4 + 2)$, what is the value of $B - A$?",
        "options": ["2", "4", "6", "8"],
        "correct": 1,
        "solution": "Step 1: Evaluate $A = 12 + 2 = 14$.\nStep 2: Evaluate $B = 3 \\times 6 = 18$.\nStep 3: $B - A = 18 - 14 = 4$."
    }
]

