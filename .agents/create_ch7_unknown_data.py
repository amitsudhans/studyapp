# -*- coding: utf-8 -*-
"""
Generator script for NCERT Class 7 Mathematics: Chapter 7 - Finding the Unknown
SLIDES_DATA containing 20 slides, 32 checkpoints, and 40 mastery quiz questions with detailed step-by-step solutions.
Strictly zero occurrences of prohibited textbook titles.
"""

SLIDES_DATA = [
    {
        "id": 1,
        "title": "What is an Unknown? Mystery Sacks & Balance Scales",
        "subtitle": "Discovering Unknown Values through Physical Equilibrium",
        "content": (
            "<p>Imagine a merchant's two-pan weighing scale in perfect horizontal balance. On the left pan sits a mysterious sealed bag of gold coins labeled $x$, along with a $3\\text{ kg}$ brass weight. On the right pan sit brass weights totaling $8\\text{ kg}$.</p>"
            "<p class='mt-2'>Because the pointer rests exactly in the center, the total weight on the left pan equals the total weight on the right pan:</p>"
            "<div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>"
            "$$x + 3 = 8$$"
            "</div>"
            "<p class='mt-2'>An <strong>unknown</strong> (or <em>variable</em>) is a quantity whose numerical value is not yet known, represented by a letter like $x, y, n,$ or $a$. In ancient India, this unknown quantity was called <em>yāvattāvat</em> (meaning 'as much as') or simply represented by the color black (<em>kālaka</em>).</p>"
            "<p class='mt-2'>By observing that removing $3\\text{ kg}$ from both pans keeps the scale balanced, we instantly reveal the secret inside the sack: $x = 8 - 3 = 5\\text{ kg}$!</p>"
        ),
        "key_takeaways": [
            "An unknown (variable) represents an unspecified quantity that satisfies a mathematical condition.",
            "A balanced two-pan scale is the perfect physical model of an algebraic equation.",
            "The equal sign ($=$) acts like a fulcrum: both sides hold identical mathematical value.",
            "Removing identical quantities from both sides leaves the equilibrium completely undisturbed."
        ],
        "formula": "$$\\text{Left Pan} = \\text{Right Pan} \\iff x + 3 = 8 \\implies x = 8 - 3 = 5$$",
        "simulator_type": "mystery_sack_scale_sim",
        "checkpoints": [
            {
                "question": "If a balance scale has a sack x and a 5 kg weight on the left pan, balancing a 12 kg weight on the right pan, what is the weight of sack x?",
                "options": ["5 kg", "7 kg", "12 kg", "17 kg"],
                "correct": 1,
                "explanation": "Since the scale is balanced, x + 5 = 12. Removing 5 kg from both sides gives x = 12 - 5 = 7 kg."
            },
            {
                "question": "In algebra, what is a variable (or unknown)?",
                "options": [
                    "A fixed number that never changes like 10",
                    "A letter or symbol that represents an unknown or changeable quantity",
                    "A drawing of a balance scale",
                    "The unit of measurement like kilograms"
                ],
                "correct": 1,
                "explanation": "A variable is a letter or symbol (like x, y, or n) used to represent a number whose value is unknown or can vary."
            }
        ]
    },
    {
        "id": 2,
        "title": "Equal Operations on Scales: The Balance Invariant",
        "subtitle": "The Fundamental Law of Algebraic Equality",
        "content": (
            "<p>The foundational principle governing all of algebra is the <strong>Balance Invariant</strong>:</p>"
            "<p class='mt-2 text-amber-300 font-semibold'>An equation remains strictly true if you perform the EXACT same arithmetic operation on BOTH sides of the equal sign!</p>"
            "<ul class='list-disc pl-5 mt-2 space-y-1'>"
            "<li><strong>Addition Invariant:</strong> If $a = b$, then $a + c = b + c$. (Adding identical weights to both pans maintains balance).</li>"
            "<li><strong>Subtraction Invariant:</strong> If $a = b$, then $a - c = b - c$. (Removing identical weights keeps balance).</li>"
            "<li><strong>Multiplication Invariant:</strong> If $a = b$, then $a \\times c = b \\times c$. (Doubling or tripling both pans preserves balance).</li>"
            "<li><strong>Division Invariant:</strong> If $a = b$ and $c \\ne 0$, then $\\frac{a}{c} = \\frac{b}{c}$. (Halving the contents of both pans preserves balance).</li>"
            "</ul>"
            "<p class='mt-2'>Any one-sided change destroys the equality instantly. Balancing an equation is like navigating a tightrope—both sides must move in perfect unison!</p>"
        ),
        "key_takeaways": [
            "Equality is invariant under identical additions, subtractions, multiplications, and divisions.",
            "You cannot add or subtract a quantity from only one side without destroying equality.",
            "Division by zero is strictly forbidden because $\\frac{a}{0}$ is mathematically undefined.",
            "Solving an equation means applying equal operations strategically until the unknown $x$ stands completely isolated on one side."
        ],
        "formula": "$$a = b \\iff a \\pm c = b \\pm c \\quad \\text{and} \\quad a \\cdot c = b \\cdot c \\quad \\text{and} \\quad \\frac{a}{c} = \\frac{b}{c} \\; (c \\ne 0)$$",
        "simulator_type": "balance_operations_sim",
        "checkpoints": [
            {
                "question": "If you subtract 9 from the left side of an equation, what must you do to the right side to keep it balanced?",
                "options": [
                    "Add 9 to the right side",
                    "Multiply the right side by 9",
                    "Subtract 9 from the right side",
                    "Do nothing"
                ],
                "correct": 2,
                "explanation": "To maintain balance, whatever operation is performed on one side must be performed identically on the other side. Subtracting 9 from both sides preserves equality."
            },
            {
                "question": "Which operation is NEVER permitted on an equation?",
                "options": [
                    "Adding a negative number to both sides",
                    "Dividing both sides by zero",
                    "Multiplying both sides by 100",
                    "Subtracting a variable from both sides"
                ],
                "correct": 1,
                "explanation": "Division by zero is mathematically undefined and strictly prohibited in arithmetic and algebra."
            }
        ]
    },
    {
        "id": 3,
        "title": "Matchstick Patterns & Linear Modeling: 2n + 1",
        "subtitle": "Discovering Algebraic Formulas from Geometric Sequences",
        "content": (
            "<p>Consider making a repeating chain of triangles using wooden matchsticks:</p>"
            "<ul class='list-disc pl-5 mt-1 space-y-1'>"
            "<li>For $1$ triangle, you need $3$ matchsticks ($1$ base $+ 2$ sides).</li>"
            "<li>For $2$ connected triangles, you add $2$ more matchsticks: $3 + 2 = 5$ sticks.</li>"
            "<li>For $3$ connected triangles, you add $2$ more: $5 + 2 = 7$ sticks.</li>"
            "<li>For $n$ connected triangles, you need: $2n + 1$ matchsticks!</li>"
            "</ul>"
            "<p class='mt-2'>Here, $n$ represents the <strong>number of triangles</strong> (an independent variable), and $2n + 1$ is the <strong>algebraic expression</strong> modeling the total matchsticks required.</p>"
            "<p class='mt-2'>Now, suppose a teacher hands you a box containing exactly $51$ matchsticks and asks: <em>'How many triangles can you construct in this chain?'</em></p>"
            "<div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>"
            "$$2n + 1 = 51$$"
            "</div>"
            "<p class='mt-2'>The question has transformed into an <strong>equation</strong>! Solving it reveals $2n = 50 \\implies n = 25$ triangles!</p>"
        ),
        "key_takeaways": [
            "Matchstick sequences provide a visual, hands-on bridge between arithmetic patterns and algebra.",
            "The constant difference between successive terms ($+2$) becomes the coefficient of $n$ ($2n$).",
            "The initial offset ($+1$) accounts for the starting matchstick.",
            "Setting a pattern expression equal to a specific target value turns a geometric pattern into a solvable equation."
        ],
        "formula": "$$\\text{Total Sticks } S = 2n + 1 \\quad \\implies \\quad 2n + 1 = 51 \\iff n = 25$$",
        "simulator_type": "matchstick_pattern_sim",
        "checkpoints": [
            {
                "question": "Using the matchstick rule 2n + 1, how many matchsticks are needed to build a chain of 15 triangles?",
                "options": ["30", "31", "32", "33"],
                "correct": 1,
                "explanation": "Substitute n = 15 into the expression: 2(15) + 1 = 30 + 1 = 31 matchsticks."
            },
            {
                "question": "If a matchstick pattern follows the formula 3n + 1, and you have 40 matchsticks, how many pattern units n can you form?",
                "options": ["10", "12", "13", "14"],
                "correct": 2,
                "explanation": "Set up the equation: 3n + 1 = 40. Subtract 1: 3n = 39. Divide by 3: n = 13."
            }
        ]
    },
    {
        "id": 4,
        "title": "Anatomy of an Equation: LHS, RHS & The Equal Sign",
        "subtitle": "Distinguishing Expressions from Equations",
        "content": (
            "<p>What is the precise difference between an <strong>algebraic expression</strong> and an <strong>algebraic equation</strong>?</p>"
            "<ul class='list-disc pl-5 mt-2 space-y-1'>"
            "<li><strong>Algebraic Expression:</strong> A mathematical phrase combining numbers, variables, and operations, but with <em>no equal sign</em>. Examples: $3x + 4$, $5n - 2$, $\\frac{y}{3}$. An expression cannot be 'solved'; it can only be evaluated when a value is given for the variable.</li>"
            "<li><strong>Algebraic Equation:</strong> A mathematical sentence stating that two expressions have identical value, connected by an equal sign ($=$). Example: $3x + 4 = 19$.</li>"
            "</ul>"
            "<p class='mt-2'>An equation consists of two distinct regions:</p>"
            "<div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>"
            "$$\\underbrace{3x + 4}_{\\text{LHS (Left-Hand Side)}} \\; = \\; \\underbrace{19}_{\\text{RHS (Right-Hand Side)}}$$"
            "</div>"
            "<p class='mt-2'>A <strong>solution</strong> (or <em>root</em>) of an equation is a specific number that, when substituted for the variable, makes the Left-Hand Side exactly equal to the Right-Hand Side ($LHS = RHS$). For $3x + 4 = 19$, the only number that satisfies this is $x = 5$!</p>"
        ),
        "key_takeaways": [
            "An expression is a phrase ($2x + 7$); an equation is a complete relational sentence with an equal sign ($2x + 7 = 15$).",
            "LHS denotes the expression to the left of '$=$'; RHS denotes the expression to the right of '$='$.",
            "The equal sign ($=$) asserts that both expressions evaluate to the identical numerical value.",
            "A solution is a value of the unknown that produces true numerical equality ($LHS = RHS$)."
        ],
        "formula": "$$\\text{Equation: } \\text{LHS} = \\text{RHS} \\quad \\text{Solution } x_0: \\text{LHS}(x_0) = \\text{RHS}(x_0)$$",
        "simulator_type": "equation_anatomy_sim",
        "checkpoints": [
            {
                "question": "Which of the following is an equation rather than an algebraic expression?",
                "options": ["4x - 7", "2y + 3z", "5n + 2 = 17", "8m / 3"],
                "correct": 2,
                "explanation": "5n + 2 = 17 contains an equal sign connecting two sides (LHS and RHS), making it an equation. The others are merely expressions."
            },
            {
                "question": "Is x = 4 a solution to the equation 3x - 2 = 10?",
                "options": [
                    "Yes, because LHS = 3(4) - 2 = 12 - 2 = 10 = RHS",
                    "No, because 3 × 4 = 12 which is greater than 10",
                    "No, x must always be an odd number",
                    "Cannot be determined without a graph"
                ],
                "correct": 0,
                "explanation": "Substituting x = 4 into LHS gives 3(4) - 2 = 12 - 2 = 10. Since LHS = RHS, x = 4 is indeed the valid solution!"
            }
        ]
    },
    {
        "id": 5,
        "title": "The Trial and Error Method: Guess, Check & Narrow Down",
        "subtitle": "Testing Successive Values & Understanding Its Limits",
        "content": (
            "<p>The most intuitive way to solve an equation like $4x - 3 = 13$ is the <strong>Trial and Error Method</strong> (or systematic guessing):</p>"
            "<p class='mt-2'>We construct a substitution table and test candidate values for $x$ one by one:</p>"
            "<div class='overflow-x-auto mt-2'>"
            "<table class='w-full text-xs text-left border border-slate-700 bg-slate-950/60 rounded'>"
            "<thead class='bg-slate-800 text-amber-300'><tr><th class='p-2'>Trial $x$</th><th class='p-2'>LHS $= 4x - 3$</th><th class='p-2'>RHS</th><th class='p-2'>Does LHS = RHS?</th></tr></thead>"
            "<tbody class='divide-y divide-slate-800 text-slate-300'>"
            "<tr><td class='p-2'>$x = 1$</td><td class='p-2'>$4(1) - 3 = 1$</td><td class='p-2'>$13$</td><td class='p-2 text-rose-400'>No (Too Small)</td></tr>"
            "<tr><td class='p-2'>$x = 2$</td><td class='p-2'>$4(2) - 3 = 5$</td><td class='p-2'>$13$</td><td class='p-2 text-rose-400'>No (Too Small)</td></tr>"
            "<tr><td class='p-2'>$x = 3$</td><td class='p-2'>$4(3) - 3 = 9$</td><td class='p-2'>$13$</td><td class='p-2 text-rose-400'>No (Closer!)</td></tr>"
            "<tr class='bg-emerald-950/40'><td class='p-2 font-bold text-emerald-400'>$x = 4$</td><td class='p-2 font-bold text-emerald-400'>$4(4) - 3 = 13$</td><td class='p-2 font-bold text-emerald-400'>$13$</td><td class='p-2 font-bold text-emerald-400'>YES! ✓ Solution Found</td></tr>"
            "</tbody></table></div>"
            "<p class='mt-2'><strong>The Limitation:</strong> While trial and error develops number sense for simple equations, what if the solution is negative ($-17$), a fraction ($\\frac{23}{7}$), or a decimal ($4.85$)? Guessing would take days! That is why mathematicians developed <strong>systematic algebraic methods</strong>.</p>"
        ),
        "key_takeaways": [
            "Trial and error tests sequential values until $LHS$ evaluates to $RHS$.",
            "It reinforces the fundamental concept of what a solution truly means.",
            "It is highly inefficient and often fails when solutions are fractions, large numbers, or negative values.",
            "Recognizing its limitations motivates the necessity of rigorous inverse operations."
        ],
        "formula": "$$\\text{Trial } x_k \\to \\text{Evaluate } \\text{LHS}(x_k) \\to \\text{Compare with } \\text{RHS} \\to \\text{Adjust}$$",
        "simulator_type": "trial_error_tester_sim",
        "checkpoints": [
            {
                "question": "Using trial and error for 5x + 3 = 23, what is the value of LHS when x = 3?",
                "options": ["15", "18", "23", "28"],
                "correct": 1,
                "explanation": "LHS = 5(3) + 3 = 15 + 3 = 18. Since 18 < 23, x = 3 is too small."
            },
            {
                "question": "Why is the trial and error method considered impractical for complex real-world equations?",
                "options": [
                    "Because letters cannot be replaced by numbers",
                    "Because guessing takes an enormous amount of time if the root is a fraction, decimal, or large negative number",
                    "Because calculators explode during guessing",
                    "Because it violates the rules of grammar"
                ],
                "correct": 1,
                "explanation": "Trial and error relies on fortunate guessing. If the root is a fraction like 17/23 or a negative decimal, finding it by random trial is nearly impossible."
            }
        ]
    },
    {
        "id": 6,
        "title": "Systematic Operations: Inverse of Addition & Subtraction",
        "subtitle": "Undoing Shifts to Isolate the Variable",
        "content": (
            "<p>To solve an equation systematically, our overarching goal is to <strong>isolate the variable</strong>—leaving $x$ completely alone on one side of the equal sign ($x = \\text{value}$).</p>"
            "<p class='mt-2'>We achieve this using <strong>inverse operations</strong> (operations that undo each other):</p>"
            "<ul class='list-disc pl-5 mt-2 space-y-1'>"
            "<li><strong>Addition and Subtraction are Inverses:</strong>"
            "<ul class='list-circle pl-5 mt-1 space-y-1'>"
            "<li>To undo $+c$, <strong>subtract $c$</strong> from both sides.</li>"
            "<li>To undo $-c$, <strong>add $c$</strong> to both sides.</li>"
            "</ul></li>"
            "</ul>"
            "<p class='mt-2'><strong>Example 1: Undoing Addition</strong></p>"
            "<div class='p-1.5 bg-slate-950 rounded border border-slate-800 text-center font-mono text-xs'>"
            "$$x + 7 = 19 \\xrightarrow{\\text{Subtract 7 from both sides}} x + 7 - 7 = 19 - 7 \\implies x = 12$$"
            "</div>"
            "<p class='mt-2'><strong>Example 2: Undoing Subtraction</strong></p>"
            "<div class='p-1.5 bg-slate-950 rounded border border-slate-800 text-center font-mono text-xs'>"
            "$$y - 9 = 15 \\xrightarrow{\\text{Add 9 to both sides}} y - 9 + 9 = 15 + 9 \\implies y = 24$$"
            "</div>"
            "<p class='mt-2'>Notice how $+7 - 7 = 0$ and $-9 + 9 = 0$. The additive inverse neutralizes the constant cleanly!</p>"
        ),
        "key_takeaways": [
            "Inverse operations undo each other, leaving the variable isolated.",
            "The inverse of addition is subtraction; the inverse of subtraction is addition.",
            "Adding zero ($x + 0 = x$) is the mathematical reason why $+c - c$ isolates $x$.",
            "Always verify your answer by substituting it back into the original equation!"
        ],
        "formula": "$$x + c = d \\iff x = d - c, \\qquad x - c = d \\iff x = d + c$$",
        "simulator_type": "add_subtract_machine_sim",
        "checkpoints": [
            {
                "question": "What is the systematic step to solve the equation m + 14 = 30?",
                "options": [
                    "Multiply both sides by 14",
                    "Add 14 to both sides",
                    "Subtract 14 from both sides",
                    "Divide both sides by 30"
                ],
                "correct": 2,
                "explanation": "To undo +14, subtract 14 from both sides: m + 14 - 14 = 30 - 14, which gives m = 16."
            },
            {
                "question": "Solve for p: p - 8 = -3",
                "options": ["-11", "-5", "5", "11"],
                "correct": 2,
                "explanation": "Add 8 to both sides: p = -3 + 8 = 5."
            }
        ]
    },
    {
        "id": 7,
        "title": "Systematic Operations: Inverse of Multiplication & Division",
        "subtitle": "Neutralizing Coefficients and Scaling Variables",
        "content": (
            "<p>When an unknown is multiplied by a coefficient (like $5x$) or divided by a divisor (like $\\frac{x}{4}$), we use multiplicative inverses to isolate it:</p>"
            "<ul class='list-disc pl-5 mt-2 space-y-1'>"
            "<li><strong>Multiplication and Division are Inverses:</strong>"
            "<ul class='list-circle pl-5 mt-1 space-y-1'>"
            "<li>To undo multiplication by $k$ ($k \\ne 0$), <strong>divide both sides by $k$</strong>.</li>"
            "<li>To undo division by $k$, <strong>multiply both sides by $k$</strong>.</li>"
            "</ul></li>"
            "</ul>"
            "<p class='mt-2'><strong>Example 1: Undoing Multiplication</strong></p>"
            "<div class='p-1.5 bg-slate-950 rounded border border-slate-800 text-center font-mono text-xs'>"
            "$$6x = 42 \\xrightarrow{\\text{Divide both sides by 6}} \\frac{6x}{6} = \\frac{42}{6} \\implies 1 \\cdot x = 7 \\implies x = 7$$"
            "</div>"
            "<p class='mt-2'><strong>Example 2: Undoing Division</strong></p>"
            "<div class='p-1.5 bg-slate-950 rounded border border-slate-800 text-center font-mono text-xs'>"
            "$$\\frac{m}{5} = 9 \\xrightarrow{\\text{Multiply both sides by 5}} \\frac{m}{5} \\times 5 = 9 \\times 5 \\implies m = 45$$"
            "</div>"
            "<p class='mt-2'>Multiplying $\\frac{1}{k} \\times k = 1$ produces the multiplicative identity ($1 \\cdot x = x$), leaving the variable purely isolated!</p>"
        ),
        "key_takeaways": [
            "The inverse of multiplying by $k$ is dividing by $k$.",
            "The inverse of dividing by $k$ is multiplying by $k$.",
            "Dividing a term by its own coefficient yields $1 \\cdot x$, successfully isolating $x$.",
            "Remember: whatever factor you multiply or divide by, every single term must be treated equally."
        ],
        "formula": "$$k \\cdot x = d \\iff x = \\frac{d}{k} \\; (k \\ne 0), \\qquad \\frac{x}{k} = d \\iff x = k \\cdot d$$",
        "simulator_type": "multiply_divide_isolator_sim",
        "checkpoints": [
            {
                "question": "What is the systematic step to solve 7x = 56?",
                "options": [
                    "Subtract 7 from both sides",
                    "Divide both sides by 7",
                    "Multiply both sides by 7",
                    "Add 56 to both sides"
                ],
                "correct": 1,
                "explanation": "Since x is multiplied by 7, divide both sides by 7: (7x)/7 = 56/7, which gives x = 8."
            },
            {
                "question": "Solve for y: y / 4 = -6",
                "options": ["-24", "-10", "-1.5", "24"],
                "correct": 0,
                "explanation": "Multiply both sides by 4: y = -6 * 4 = -24."
            }
        ]
    },
    {
        "id": 8,
        "title": "Two-Step Linear Equations: ax + b = c",
        "subtitle": "The Unwrapping Strategy & Reverse Order of Operations",
        "content": (
            "<p>What happens when an equation combines multiple operations, such as $3x + 5 = 26$? We have both multiplication ($\\times 3$) and addition ($+ 5$). Which operation do we undo first?</p>"
            "<p class='mt-2'>Think of how you wrap a gift: First you put the toy in a box (multiply), then you wrap it with wrapping paper (add). When unwrapping, you must remove the <strong>wrapping paper first</strong>, and then open the box!</p>"
            "<p class='mt-2'>In algebra, we undo operations in <strong>reverse order of operations</strong> (reverse PEMDAS/BODMAS):</p>"
            "<ol class='list-decimal pl-5 mt-1 space-y-1'>"
            "<li><strong>Step 1: Undo Addition / Subtraction first.</strong>"
            "<div class='p-1 bg-slate-950 rounded border border-slate-800 text-center font-mono text-xs my-1'>"
            "$$3x + 5 = 26 \\implies 3x + 5 - 5 = 26 - 5 \\implies 3x = 21$$"
            "</div></li>"
            "<li><strong>Step 2: Undo Multiplication / Division second.</strong>"
            "<div class='p-1 bg-slate-950 rounded border border-slate-800 text-center font-mono text-xs my-1'>"
            "$$3x = 21 \\implies \\frac{3x}{3} = \\frac{21}{3} \\implies x = 7$$"
            "</div></li>"
            "</ol>"
            "<p class='mt-2'>Check: $3(7) + 5 = 21 + 5 = 26 = RHS$. Perfect!</p>"
        ),
        "key_takeaways": [
            "Two-step equations combine multiplication/division with addition/subtraction: $ax + b = c$.",
            "Undo the operations in reverse order: eliminate the constant term $+b$ or $-b$ first.",
            "Then eliminate the coefficient $a$ by division or multiplication.",
            "Unwrapping step by step prevents messy fractional calculations early in the problem."
        ],
        "formula": "$$ax + b = c \\xrightarrow{-b} ax = c - b \\xrightarrow{\\div a} x = \\frac{c - b}{a} \\; (a \\ne 0)$$",
        "simulator_type": "two_step_unwrapper_sim",
        "checkpoints": [
            {
                "question": "In solving 4x - 7 = 17, which operation should you perform first?",
                "options": [
                    "Divide both sides by 4",
                    "Add 7 to both sides",
                    "Subtract 17 from both sides",
                    "Multiply both sides by 4"
                ],
                "correct": 1,
                "explanation": "Undo addition/subtraction first! Adding 7 to both sides eliminates -7, leaving 4x = 24. Then divide by 4 to get x = 6."
            },
            {
                "question": "Solve the two-step equation: 5x + 8 = 38",
                "options": ["x = 5", "x = 6", "x = 7", "x = 8"],
                "correct": 1,
                "explanation": "Step 1: 5x = 38 - 8 = 30. Step 2: x = 30 / 5 = 6."
            }
        ]
    },
    {
        "id": 9,
        "title": "The Power of Transposition: Crossing the Bridge",
        "subtitle": "Fast Algebraic Moving with Inverted Signs",
        "content": (
            "<p>As you gain algebraic fluency, writing out $+7 - 7$ on both sides becomes tedious. Mathematicians use a streamlined shortcut called <strong>Transposition</strong>.</p>"
            "<p class='mt-2'>Think of the equal sign ($=$) as a <strong>magic bridge</strong>:</p>"
            "<div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>"
            "$$\\text{When a term crosses the equal sign bridge, its operation INVERTS!}$$"
            "</div>"
            "<ul class='list-disc pl-5 mt-2 space-y-1'>"
            "<li>A positive term $+b$ transposes to the other side as <strong>$-b$</strong>."
            "<br><span class='font-mono text-emerald-400'>$x + 5 = 12 \\implies x = 12 - 5 = 7$</span></li>"
            "<li>A negative term $-b$ transposes to the other side as <strong>$+b$</strong>."
            "<br><span class='font-mono text-emerald-400'>$x - 8 = 10 \\implies x = 10 + 8 = 18$</span></li>"
            "<li>A multiplying factor $\\times a$ transposes to the other side as a <strong>divisor $\\div a$</strong>."
            "<br><span class='font-mono text-emerald-400'>$4x = 28 \\implies x = \\frac{28}{4} = 7$</span></li>"
            "<li>A dividing term $\\div a$ transposes to the other side as a <strong>multiplier $\\times a$</strong>."
            "<br><span class='font-mono text-emerald-400'>$\\frac{x}{3} = 5 \\implies x = 5 \\times 3 = 15$</span></li>"
            "</ul>"
            "<p class='mt-2'>Transposition is simply performing identical operations on both sides, compressed into one rapid, elegant motion!</p>"
        ),
        "key_takeaways": [
            "Transposition shifts a term across the '$=$' sign while inverting its operational sign.",
            "$+$ becomes $-$; $-$ becomes $+$; $\\times$ becomes $\\div$; $\\div$ becomes $\\times$.",
            "It is mathematically identical to applying inverse operations to both sides.",
            "Be vigilant: ONLY terms crossing the '$=$' sign change signs; terms staying on their own side keep their signs!"
        ],
        "formula": "$$x + b = c \\implies x = c - b, \\qquad a \\cdot x = c \\implies x = \\frac{c}{a}$$",
        "simulator_type": "transposition_bridge_sim",
        "checkpoints": [
            {
                "question": "When transposing the term -11 in the equation x - 11 = 25 to the right-hand side, what does it become?",
                "options": ["-11", "+11", "× 11", "÷ 11"],
                "correct": 1,
                "explanation": "Crossing the equal sign inverts the sign: -11 becomes +11 on the RHS, yielding x = 25 + 11 = 36."
            },
            {
                "question": "In the equation 2x + 9 = 21, what is the resulting equation after transposing +9 to the RHS?",
                "options": ["2x = 21 + 9", "2x = 21 - 9", "x = 21 - 9", "2x = 9 - 21"],
                "correct": 1,
                "explanation": "+9 transposes to the RHS as -9, yielding 2x = 21 - 9 (which simplifies to 2x = 12)."
            }
        ]
    },
    {
        "id": 10,
        "title": "Variables on Both Sides: ax + b = cx + d",
        "subtitle": "Unifying Variables on One Side and Constants on the Other",
        "content": (
            "<p>What if unknown mystery sacks sit on <em>both</em> pans of our balance scale? For example:</p>"
            "<div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>"
            "$$5x + 3 = 2x + 18$$"
            "</div>"
            "<p class='mt-2'>On the left pan: $5$ sacks and a $3\\text{ kg}$ weight. On the right pan: $2$ sacks and an $18\\text{ kg}$ weight.</p>"
            "<p class='mt-2'><strong>The Strategy: Collect Like Terms!</strong></p>"
            "<ol class='list-decimal pl-5 mt-1 space-y-1'>"
            "<li><strong>Step 1: Collect variable terms on one side.</strong> Remove $2x$ from both sides (transpose $2x$ to the LHS):"
            "<div class='p-1 bg-slate-950 rounded border border-slate-800 text-center font-mono text-xs my-1'>"
            "$$5x - 2x + 3 = 18 \\implies 3x + 3 = 18$$"
            "</div></li>"
            "<li><strong>Step 2: Collect constants on the opposite side.</strong> Transpose $+3$ to the RHS as $-3$:"
            "<div class='p-1 bg-slate-950 rounded border border-slate-800 text-center font-mono text-xs my-1'>"
            "$$3x = 18 - 3 \\implies 3x = 15$$"
            "</div></li>"
            "<li><strong>Step 3: Isolate the unknown.</strong> Divide by $3$:"
            "<div class='p-1 bg-slate-950 rounded border border-slate-800 text-center font-mono text-xs my-1'>"
            "$$x = \\frac{15}{3} = 5$$"
            "</div></li>"
            "</ol>"
            "<p class='mt-2'>Check: LHS $= 5(5)+3 = 28$; RHS $= 2(5)+18 = 28$. Balance verified!</p>"
        ),
        "key_takeaways": [
            "Equations with variables on both sides represent balance scales with mystery sacks on both pans.",
            "Transpose the smaller variable term to the side with the larger variable term to keep coefficients positive.",
            "Transpose all numerical constants to the opposite side.",
            "This reduces any general linear equation to the familiar one-step form: $Ax = B$."
        ],
        "formula": "$$ax + b = cx + d \\implies (a - c)x = d - b \\implies x = \\frac{d - b}{a - c} \\; (a \\ne c)$$",
        "simulator_type": "dual_pan_variables_sim",
        "checkpoints": [
            {
                "question": "What is the first recommended step in solving 7x - 4 = 3x + 16?",
                "options": [
                    "Multiply all terms by 4",
                    "Transpose 3x to the LHS by subtracting 3x from both sides (7x - 3x = 4x)",
                    "Divide 16 by 7",
                    "Add 3x to 7x"
                ],
                "correct": 1,
                "explanation": "Subtracting 3x from both sides brings all variables to the LHS: 7x - 3x - 4 = 16 ⟹ 4x - 4 = 16."
            },
            {
                "question": "Solve for x: 6x + 2 = 2x + 22",
                "options": ["x = 4", "x = 5", "x = 6", "x = 7"],
                "correct": 1,
                "explanation": "Subtract 2x: 4x + 2 = 22. Subtract 2: 4x = 20. Divide by 4: x = 5."
            }
        ]
    },
    {
        "id": 11,
        "title": "Real-World Problems: Tile Patterns & Geometry Constraints",
        "subtitle": "Translating Verbal Sentences into Mathematical Equations",
        "content": (
            "<p>The real superpower of algebra is solving practical, everyday challenges by translating verbal word puzzles into equations:</p>"
            "<p class='mt-2'><strong>The Rectangle Perimeter Problem:</strong></p>"
            "<p class='text-xs text-slate-300 italic pl-3 border-l-2 border-amber-400'>'A garden plot has a perimeter of $40\\text{ m}$. Its length is $4\\text{ m}$ more than its width. What are its dimensions?'</p>"
            "<ol class='list-decimal pl-5 mt-1 space-y-1'>"
            "<li><strong>Step 1: Identify the Unknown.</strong> Let the width be $w$ meters.</li>"
            "<li><strong>Step 2: Express other quantities.</strong> Length $= w + 4$ meters.</li>"
            "<li><strong>Step 3: Build the Equation.</strong> Perimeter $= 2(\\text{length} + \\text{width}) = 40$:"
            "<div class='p-1 bg-slate-950 rounded border border-slate-800 text-center font-mono text-xs my-1'>"
            "$$2[(w + 4) + w] = 40 \\implies 2(2w + 4) = 40 \\implies 4w + 8 = 40$$"
            "</div></li>"
            "<li><strong>Step 4: Solve!</strong> Transpose $+8$: $4w = 40 - 8 = 32$. Divide by $4$: $w = 8\\text{ m}$!</li>"
            "</ol>"
            "<p class='mt-2'>The width is $8\\text{ m}$, and the length is $w + 4 = 12\\text{ m}$. Check: $2(12 + 8) = 2(20) = 40\\text{ m}$. Exactly as stated!</p>"
        ),
        "key_takeaways": [
            "Follow the 4-step blueprint: Define Unknown $\\to$ Express Relationships $\\to$ Build Equation $\\to$ Solve & Verify.",
            "Look for keywords: 'is / equals' ($=$), 'more than' ($+$), 'less than' ($-$), 'times / of' ($\\times$), 'ratio / divided' ($\\div$).",
            "In geometric problems, use standard formulas (Perimeter $P = 2(l+w)$, Area $A = lw$, Angle sums).",
            "Always include proper physical units (meters, kg, rupees) in your final solution statement."
        ],
        "formula": "$$\\text{Perimeter: } P = 2(l + w) = 40, \\quad l = w + 4 \\implies 4w + 8 = 40 \\implies w = 8\\text{ m}, \\; l = 12\\text{ m}$$",
        "simulator_type": "geometry_word_problem_sim",
        "checkpoints": [
            {
                "question": "The sum of three consecutive integers is 48. If the smallest integer is n, what is the equation?",
                "options": [
                    "3n = 48",
                    "n + (n + 1) + (n + 2) = 48 (or 3n + 3 = 48)",
                    "n + 2n + 3n = 48",
                    "n × (n + 1) × (n + 2) = 48"
                ],
                "correct": 1,
                "explanation": "Consecutive integers differ by 1: n, n+1, n+2. Their sum is n + (n+1) + (n+2) = 3n + 3 = 48 (which solves to n = 15)."
            },
            {
                "question": "A father is 3 times as old as his son. If the sum of their ages is 44 years, what is the son's age s?",
                "options": ["9 years", "11 years", "14 years", "15 years"],
                "correct": 1,
                "explanation": "Son = s, Father = 3s. Equation: s + 3s = 44 ⟹ 4s = 44 ⟹ s = 11 years."
            }
        ]
    },
    {
        "id": 12,
        "title": "Party Budgets, Savings Growth & Number Magic",
        "subtitle": "Practical Consumer Math & The Secret Behind Mind-Reading Tricks",
        "content": (
            "<p>Linear equations govern commercial budgets and illuminate popular party tricks!</p>"
            "<ul class='list-disc pl-5 mt-1 space-y-1'>"
            "<li><strong>Party Budget Modeling:</strong> A birthday banquet hall charges a fixed room rental of $\\text{Rs } 1,500$ plus $\\text{Rs } 250$ per guest for dinner. If the total family budget is $\\text{Rs } 9,000$, how many guests $g$ can be invited?"
            "<div class='p-1 bg-slate-950 rounded border border-slate-800 text-center font-mono text-xs my-1'>"
            "$$1500 + 250g = 9000 \\implies 250g = 7500 \\implies g = \\frac{7500}{250} = 30\\text{ guests!}$$"
            "</div></li>"
            "<li><strong>The 'Think of a Number' Mind-Reading Trick:</strong>"
            "<ol class='list-decimal pl-5 mt-1 space-y-0.5 text-xs'>"
            "<li>Think of any secret number ($x$).</li>"
            "<li>Double it ($2x$).</li>"
            "<li>Add $10$ ($2x + 10$).</li>"
            "<li>Divide the total by $2$ ($\\frac{2x + 10}{2} = x + 5$).</li>"
            "<li>Subtract your original secret number: $(x + 5) - x = 5$!</li>"
            "</ol>"
            "The magician shouts: <em>'Your final answer is 5!'</em> The secret? The variable $x$ cancels out completely, leaving an invariant constant!"
            "</li></ul>"
        ),
        "key_takeaways": [
            "Fixed cost + (Variable rate $\\times$ count) = Total Budget is the universal linear billing formula.",
            "Savings comparisons ($S_1 + r_1 t = S_2 + r_2 t$) calculate the exact time $t$ when two funds equalize.",
            "Mind-reading number games are algebraic identities where the chosen variable $x - x = 0$ is secretly eliminated.",
            "Algebra turns mysterious magic into transparent, predictable mathematics!"
        ],
        "formula": "$$\\text{Fixed} + \\text{Rate} \\cdot g = \\text{Budget} \\implies F + r \\cdot g = B, \\qquad \\frac{2x + 2k}{2} - x = k \\text{ (Invariant)}$$",
        "simulator_type": "budget_magic_trick_sim",
        "checkpoints": [
            {
                "question": "A taxi charges a flat booking fee of Rs 50 plus Rs 15 per kilometer. If Priya pays Rs 260, how many kilometers d did she travel?",
                "options": ["12 km", "14 km", "16 km", "18 km"],
                "correct": 1,
                "explanation": "Equation: 50 + 15d = 260. Transpose 50: 15d = 210. Divide by 15: d = 210 / 15 = 14 km."
            },
            {
                "question": "In a number trick, you think of x, triple it (3x), add 12 (3x + 12), and divide by 3. What is the resulting expression?",
                "options": ["x + 12", "x + 4", "3x + 4", "x + 3"],
                "correct": 1,
                "explanation": "(3x + 12) / 3 = 3x/3 + 12/3 = x + 4. If you then subtract your original number x, the result is always 4!"
            }
        ]
    },
    {
        "id": 13,
        "title": "Mind the Mistake, Mend the Mistake: Transposition Traps",
        "subtitle": "Diagnostic Clinic: Catching and Repairing Common Sign Errors",
        "content": (
            "<p>Every mathematician makes mistakes—the master mathematician learns to diagnose and repair them! Let us examine the most notorious algebra traps:</p>"
            "<p class='mt-2'><strong>Trap 1: The Sign-Preservation Trap (Forgetting to Invert)</strong></p>"
            "<div class='p-2 bg-rose-950/40 rounded border border-rose-500/40 text-xs'>"
            "<span class='text-rose-400 font-bold'>Incorrect Student Work:</span><br>"
            "$$4x - 9 = 15 \\implies 4x = 15 - 9 \\implies 4x = 6 \\implies x = 1.5 \\quad \\text{❌}$$"
            "<span class='text-emerald-400 font-bold mt-1 block'>Mend the Mistake (The Fix):</span>"
            "When $-9$ crosses the equal sign, it MUST invert to $+9$!<br>"
            "$$4x = 15 + 9 = 24 \\implies x = \\frac{24}{4} = 6 \\quad \\text{✔}$$"
            "</div>"
            "<p class='mt-2'><strong>Trap 2: Transposing to the Wrong Side without Removing</strong></p>"
            "<div class='p-2 bg-rose-950/40 rounded border border-rose-500/40 text-xs'>"
            "<span class='text-rose-400 font-bold'>Incorrect Student Work:</span><br>"
            "$$x + 5 = 12 \\implies x + 5 = 12 - 5 \\quad \\text{❌ (Duplicate 5!)}$$"
            "<span class='text-emerald-400 font-bold mt-1 block'>Mend the Mistake (The Fix):</span>"
            "A term leaves its original side when transposed: $x = 12 - 5 = 7$."
            "</div>"
        ),
        "key_takeaways": [
            "Whenever a term moves across the '$=$' sign, its sign MUST flip ($+$ to $-$, or $-$ to $+$).",
            "Terms that remain on their original side never change their signs.",
            "Never leave the original term behind when transposing—it disappears from the source side.",
            "Substituting your answer back into the original equation catches 100% of arithmetic errors!"
        ],
        "formula": "$$\\text{Rule: } A - B = C \\implies A = C + B \\; (\\text{NOT } C - B!)$$",
        "simulator_type": "transposition_trap_sim",
        "checkpoints": [
            {
                "question": "Identify the error in this step: 5x - 7 = 18 ⟹ 5x = 18 - 7 = 11.",
                "options": [
                    "5x was not divided by 2",
                    "The -7 on the LHS was incorrectly transposed as -7 instead of +7 on the RHS",
                    "18 should have been multiplied by 5",
                    "There is no error"
                ],
                "correct": 1,
                "explanation": "When -7 crosses to the RHS, it must become +7. The correct step is 5x = 18 + 7 = 25, which yields x = 5."
            },
            {
                "question": "What is the correct solution to 3x - 12 = 15?",
                "options": ["x = 1", "x = 3", "x = 9", "x = 27"],
                "correct": 2,
                "explanation": "Transpose -12 as +12: 3x = 15 + 12 = 27. Divide by 3: x = 27 / 3 = 9."
            }
        ]
    },
    {
        "id": 14,
        "title": "Mind the Mistake, Mend the Mistake: Distributive & Division Traps",
        "subtitle": "Whole-Side Division & Negative Distribution Watchdogs",
        "content": (
            "<p>Two more classical traps frequently deceive algebra beginners:</p>"
            "<p class='mt-2'><strong>Trap 3: The Partial Division Trap</strong></p>"
            "<div class='p-2 bg-rose-950/40 rounded border border-rose-500/40 text-xs'>"
            "<span class='text-rose-400 font-bold'>Incorrect Student Work:</span><br>"
            "$$2x + 6 = 14 \\xrightarrow{\\text{Divide by 2}} x + 6 = 7 \\quad \\text{❌ (Only 2x was divided!)}$$"
            "<span class='text-emerald-400 font-bold mt-1 block'>Mend the Mistake (The Fix):</span>"
            "Division applies to the <em>entire side</em>, meaning EVERY term must be divided by $2$!<br>"
            "$$\\frac{2x + 6}{2} = \\frac{14}{2} \\implies x + 3 = 7 \\implies x = 4 \\quad \\text{✔}$$"
            "</div>"
            "<p class='mt-2'><strong>Trap 4: The Negative Distribution Blunder</strong></p>"
            "<div class='p-2 bg-rose-950/40 rounded border border-rose-500/40 text-xs'>"
            "<span class='text-rose-400 font-bold'>Incorrect Student Work:</span><br>"
            "$$4 - (x - 3) = 11 \\implies 4 - x - 3 = 11 \\quad \\text{❌ (Sign inside brackets not flipped!)}$$"
            "<span class='text-emerald-400 font-bold mt-1 block'>Mend the Mistake (The Fix):</span>"
            "Distributing a negative sign changes ALL signs inside: $-(x - 3) = -x + 3$!<br>"
            "$$4 - x + 3 = 11 \\implies 7 - x = 11 \\implies -x = 4 \\implies x = -4 \\quad \\text{✔}$$"
            "</div>"
        ),
        "key_takeaways": [
            "Division of a polynomial by a number requires dividing EVERY single term on that side.",
            "Distributing a minus sign outside parentheses reverses every sign inside: $-(a - b) = -a + b$.",
            "To avoid fractional division traps, ALWAYS eliminate constant additions/subtractions first!",
            "Treat parentheses like sealed rooms: multipliers or negative signs outside must visit every resident inside."
        ],
        "formula": "$$\\frac{ax + b}{a} = x + \\frac{b}{a}, \\qquad -(x - c) = -x + c$$",
        "simulator_type": "distributive_division_trap_sim",
        "checkpoints": [
            {
                "question": "If you divide both sides of 3x + 12 = 21 by 3, what is the correct resulting equation?",
                "options": [
                    "x + 12 = 7",
                    "x + 4 = 7",
                    "3x + 4 = 7",
                    "x + 4 = 21"
                ],
                "correct": 1,
                "explanation": "Every term on the LHS must be divided by 3: (3x)/3 + 12/3 = 21/3, which gives x + 4 = 7 (so x = 3)."
            },
            {
                "question": "Expand the expression correctly: 5 - 2(x - 4)",
                "options": [
                    "5 - 2x - 8 = -3 - 2x",
                    "5 - 2x + 8 = 13 - 2x",
                    "3(x - 4) = 3x - 12",
                    "5 - 2x - 4 = 1 - 2x"
                ],
                "correct": 1,
                "explanation": "Distribute -2 to both terms inside: -2 * x = -2x, and -2 * (-4) = +8. So 5 - 2x + 8 = 13 - 2x."
            }
        ]
    },
    {
        "id": 15,
        "title": "A Pinch of History: Bījagaṇita in Ancient India",
        "subtitle": "From Āryabhaṭa and Brahmagupta to Al-Khwarizmi and the World",
        "content": (
            "<p>Algebra is not a modern European invention—its deepest mathematical roots blossomed over $1,500$ years ago on the Indian subcontinent under the Sanskrit name <strong>Bījagaṇita</strong> (<em>bīja</em> = 'seed' or 'element', <em>gaṇita</em> = 'calculation'—literally, 'calculation using primary seeds/unknowns')!</p>"
            "<ul class='list-disc pl-5 mt-2 space-y-1'>"
            "<li><strong>Āryabhaṭa (476 CE):</strong> In the <em>Āryabhaṭīya</em>, he developed linear indeterminate equation algorithms (*Kuṭṭaka* - the pulverizer) and used phonetic letter-numerals.</li>"
            "<li><strong>Brahmagupta (598–668 CE):</strong> Working at the astronomical observatory of Ujjain, he authored the landmark <em>Brāhmasphuṭasiddhānta</em> (628 CE). Chapter 18 (*Kuṭṭakādhyāya*) codifies the world's first complete rules for negative numbers (*ṛṇa* = debt), positive numbers (*dhana* = fortune), zero (*kha*), and general linear equations!</li>"
            "<li><strong>Bhāskarāchārya (1114–1185 CE):</strong> Authored the master mathematical texts <em>Līlāvatī</em> and <em>Bījagaṇita</em>, framing complex algebraic equations through poetic riddles about swarms of bees, pearls, and peacocks.</li>"
            "<li><strong>Global Transmission:</strong> In the 8th century, Indian mathematical texts were translated into Arabic at Baghdad's House of Wisdom (*Bayt al-Hikma*). Mathematician <strong>Muhammad ibn Musa al-Khwarizmi</strong> synthesized these Indian methods in his celebrated book <em>Kitab al-Jabr wa-l-Muqabala</em> (from which the word <strong>Algebra</strong> is derived)!</li>"
            "</ul>"
        ),
        "key_takeaways": [
            "Bījagaṇita is the ancient Sanskrit term for algebra, meaning computation with unknown elements.",
            "Brahmagupta (628 CE) established foundational sign laws for negative numbers and linear equations.",
            "Ancient Indian algebra denoted unknowns using abbreviations of colors: kā (kālaka = black), nī (nīlaka = blue), pī (pītaka = yellow).",
            "Indian algebra traveled to Baghdad, inspiring Al-Khwarizmi's book Al-Jabr, which gave algebra its modern worldwide name."
        ],
        "formula": "$$\\text{Heritage Chain: } \\text{Āryabhaṭa (499 CE)} \\to \\text{Brahmagupta (628 CE)} \\to \\text{Al-Khwarizmi (825 CE)} \\to \\text{Modern Algebra}$$",
        "simulator_type": "bijaganita_timeline_sim",
        "checkpoints": [
            {
                "question": "What does the ancient Sanskrit mathematical term 'Bījagaṇita' literally translate to?",
                "options": [
                    "Calculation using geometry and circles",
                    "Computation with primary seeds or unknown elements (Algebra)",
                    "Counting with pebbles",
                    "Measurement of stars"
                ],
                "correct": 1,
                "explanation": "'Bīja' means seed, root, or primary element, and 'gaṇita' means calculation. Bījagaṇita is the science of computing with unknown seeds/elements."
            },
            {
                "question": "From which historic Arabic mathematical treatise did the modern word 'Algebra' originate?",
                "options": [
                    "The Elements by Euclid",
                    "Kitab al-Jabr wa-l-Muqabala by Al-Khwarizmi (translating Indian algebraic methods)",
                    "Brāhmasphuṭasiddhānta",
                    "Līlāvatī"
                ],
                "correct": 1,
                "explanation": "The word 'Algebra' comes from 'al-Jabr' (meaning restoration or transposing negative terms) in Al-Khwarizmi's 9th-century Baghdad treatise."
            }
        ]
    },
    {
        "id": 16,
        "title": "Brahmagupta's General Formula & Classification Matrix",
        "subtitle": "The Universal Solution for Ax + B = Cx + D from 628 CE",
        "content": (
            "<p>In Chapter 18 of the <em>Brāhmasphuṭasiddhānta</em>, Acharya Brahmagupta codified the universal formula for solving any linear equation with unknowns on both sides:</p>"
            "<div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>"
            "$$Ax + B = Cx + D \\implies x = \\frac{D - B}{A - C} \\quad (A \\ne C)$$"
            "</div>"
            "<p class='mt-2'>Brahmagupta's ancient verse translates poetically as:</p>"
            "<p class='text-xs text-slate-300 italic pl-3 border-l-2 border-amber-400'>'Subtract the constant term of the first side from the constant term of the second side; divide this remainder by the difference of the unknown coefficients of the two sides. The quotient is the measure of the unknown.'</p>"
            "<p class='mt-2'><strong>Master Summary Matrix:</strong></p>"
            "<ul class='list-disc pl-5 mt-1 space-y-1 text-xs'>"
            "<li><strong>One-Step Shift ($x + b = c$):</strong> $x = c - b$ (Additive inverse).</li>"
            "<li><strong>One-Step Scale ($ax = c$):</strong> $x = \\frac{c}{a}$ (Multiplicative inverse).</li>"
            "<li><strong>Two-Step Form ($ax + b = c$):</strong> $x = \\frac{c - b}{a}$ (Reverse order of operations).</li>"
            "<li><strong>Full Brahmagupta Form ($ax + b = cx + d$):</strong> $x = \\frac{d - b}{a - c}$ (Universal linear solver).</li>"
            "</ul>"
        ),
        "key_takeaways": [
            "Brahmagupta's formula solves all linear equations in a single universal algebraic step.",
            "Subtract constants across sides: $D - B$; subtract coefficients across sides: $A - C$.",
            "The quotient $\\frac{D - B}{A - C}$ directly yields the unknown without intermediate trial-and-error.",
            "If $A = C$ and $B \\ne D$, the equation has NO solution (e.g., $2x + 3 = 2x + 7$ is impossible); if $A = C$ and $B = D$, it is an identity true for ALL numbers."
        ],
        "formula": "$$\\text{Brahmagupta's Law (628 CE): } x = \\frac{\\text{Difference of Constants}}{\\text{Difference of Coefficients}} = \\frac{D - B}{A - C}$$",
        "simulator_type": "brahmagupta_solver_sim",
        "checkpoints": [
            {
                "question": "Using Brahmagupta's formula x = (D - B)/(A - C) to solve 7x + 5 = 2x + 25, what is the value of x?",
                "options": ["x = 2", "x = 3", "x = 4", "x = 5"],
                "correct": 2,
                "explanation": "Here A = 7, B = 5, C = 2, D = 25. x = (25 - 5) / (7 - 2) = 20 / 5 = 4."
            },
            {
                "question": "What happens if A = C in the equation Ax + B = Cx + D with B ≠ D (for example, 3x + 4 = 3x + 10)?",
                "options": [
                    "x = 0",
                    "x = 1",
                    "There is NO solution, because subtracting 3x gives 4 = 10, which is an impossible contradiction",
                    "x can be any number"
                ],
                "correct": 2,
                "explanation": "Subtracting 3x from both sides yields 4 = 10, an impossible statement. The equation has no solution!"
            }
        ]
    },
    {
        "id": 17,
        "title": "Mastery Challenge • Part I",
        "subtitle": "Unknown Weights, Balance Invariant, Matchsticks & Equation Anatomy",
        "type": "quiz_slide",
        "questions": [
            {
                "id": "q1",
                "question": "On a balance scale, two identical mystery sacks 2x balance brass weights totaling 18 kg. What is the weight of one sack x?",
                "options": ["6 kg", "8 kg", "9 kg", "36 kg"],
                "correct": 2,
                "solution": "Step 1: Set up the equation: $2x = 18$.<br>Step 2: Divide both sides by 2: $x = \\frac{18}{2} = 9\\text{ kg}$."
            },
            {
                "id": "q2",
                "question": "Which mathematical symbol acts like the physical balance fulcrum between two algebraic expressions?",
                "options": ["Plus sign (+)", "Greater than (>)", "Equal sign (=)", "Multiplication sign (×)"],
                "correct": 2,
                "solution": "Step 1: The equal sign ($=$) establishes that both sides hold the exact same numerical quantity, functioning like the balance pointer at equilibrium."
            },
            {
                "id": "q3",
                "question": "In a matchstick pattern of houses where the number of sticks S follows S = 5n + 1, how many sticks are needed for n = 8 houses?",
                "options": ["39 sticks", "40 sticks", "41 sticks", "45 sticks"],
                "correct": 2,
                "solution": "Step 1: Substitute $n = 8$ into $S = 5n + 1$.<br>Step 2: $S = 5(8) + 1 = 40 + 1 = 41\\text{ sticks}$."
            },
            {
                "id": "q4",
                "question": "If you have 61 matchsticks and the formula is S = 4n + 1, how many pattern units n can you construct?",
                "options": ["14 units", "15 units", "16 units", "20 units"],
                "correct": 1,
                "solution": "Step 1: Equation: $4n + 1 = 61$.<br>Step 2: Subtract 1: $4n = 60$.<br>Step 3: Divide by 4: $n = 15\\text{ units}$."
            },
            {
                "id": "q5",
                "question": "What is the Left-Hand Side (LHS) of the equation 7y - 5 = 3y + 11?",
                "options": ["3y + 11", "7y", "7y - 5", "11"],
                "correct": 2,
                "solution": "Step 1: The LHS is the complete algebraic expression situated to the left of the equal sign: $7y - 5$."
            },
            {
                "id": "q6",
                "question": "What is the fundamental difference between an algebraic expression and an algebraic equation?",
                "options": [
                    "Expressions contain letters; equations contain only numbers",
                    "An equation contains an equal sign relating two expressions; an expression does not",
                    "Expressions are always true; equations are always false",
                    "There is no difference"
                ],
                "correct": 1,
                "solution": "Step 1: An algebraic expression is a phrase with no relational symbol (e.g., $3x + 2$).<br>Step 2: An equation is a complete relational sentence featuring an equal sign (e.g., $3x + 2 = 14$)."
            },
            {
                "id": "q7",
                "question": "If x + a = b, what is the value of x obtained by applying the subtraction invariant?",
                "options": ["x = b + a", "x = b - a", "x = a - b", "x = ab"],
                "correct": 1,
                "solution": "Step 1: Subtract $a$ from both sides: $x + a - a = b - a \\implies x = b - a$."
            },
            {
                "id": "q8",
                "question": "Which of the following values of x satisfies the equation 4x - 6 = 14?",
                "options": ["x = 3", "x = 4", "x = 5", "x = 6"],
                "correct": 2,
                "solution": "Step 1: For $x = 5$: $\\text{LHS} = 4(5) - 6 = 20 - 6 = 14 = \\text{RHS}$.<br>Step 2: Thus, $x = 5$ is the valid root."
            },
            {
                "id": "q9",
                "question": "If 3 sacks and a 4 kg weight balance a 25 kg weight (3x + 4 = 25), what is the weight of one sack x?",
                "options": ["5 kg", "6 kg", "7 kg", "8 kg"],
                "correct": 2,
                "solution": "Step 1: $3x + 4 = 25$.<br>Step 2: $3x = 25 - 4 = 21$.<br>Step 3: $x = \\frac{21}{3} = 7\\text{ kg}$."
            },
            {
                "id": "q10",
                "question": "If you multiply both sides of the equation x/4 = 5 by 4, what is the resulting statement?",
                "options": ["x = 9", "x = 20", "x/16 = 5", "4x = 20"],
                "correct": 1,
                "solution": "Step 1: $(x / 4) \\times 4 = 5 \\times 4 \\implies x = 20$."
            }
        ]
    },
    {
        "id": 18,
        "title": "Mastery Challenge • Part II",
        "subtitle": "Trial & Error, Inverse Operations, One-Step & Two-Step Equations",
        "type": "quiz_slide",
        "questions": [
            {
                "id": "q11",
                "question": "Solve the one-step equation: y - 17 = 28",
                "options": ["y = 11", "y = 35", "y = 45", "y = 55"],
                "correct": 2,
                "solution": "Step 1: Add 17 to both sides: $y = 28 + 17 = 45$."
            },
            {
                "id": "q12",
                "question": "Solve the equation: 8m = -56",
                "options": ["m = -7", "m = 7", "m = -8", "m = -48"],
                "correct": 0,
                "solution": "Step 1: Divide both sides by 8: $m = \\frac{-56}{8} = -7$."
            },
            {
                "id": "q13",
                "question": "Solve the equation: p / 7 = 9",
                "options": ["p = 16", "p = 54", "p = 63", "p = 72"],
                "correct": 2,
                "solution": "Step 1: Multiply both sides by 7: $p = 9 \\times 7 = 63$."
            },
            {
                "id": "q14",
                "question": "Solve the two-step equation: 3x + 7 = 31",
                "options": ["x = 6", "x = 7", "x = 8", "x = 9"],
                "correct": 2,
                "solution": "Step 1: Subtract 7: $3x = 31 - 7 = 24$.<br>Step 2: Divide by 3: $x = \\frac{24}{3} = 8$."
            },
            {
                "id": "q15",
                "question": "Solve the two-step equation: 5k - 9 = 26",
                "options": ["k = 5", "k = 7", "k = 8", "k = 9"],
                "correct": 1,
                "solution": "Step 1: Add 9: $5k = 26 + 9 = 35$.<br>Step 2: Divide by 5: $k = \\frac{35}{5} = 7$."
            },
            {
                "id": "q16",
                "question": "Solve the equation: x / 3 - 4 = 5",
                "options": ["x = 3", "x = 9", "x = 27", "x = 36"],
                "correct": 2,
                "solution": "Step 1: Add 4: $\\frac{x}{3} = 5 + 4 = 9$.<br>Step 2: Multiply by 3: $x = 9 \\times 3 = 27$."
            },
            {
                "id": "q17",
                "question": "In the trial and error method for 2x + 5 = 19, what is the value of LHS when x = 6?",
                "options": ["12", "17", "19", "21"],
                "correct": 1,
                "solution": "Step 1: $\\text{LHS} = 2(6) + 5 = 12 + 5 = 17$. (Close, but $17 \\ne 19$; testing $x = 7$ yields $2(7)+5 = 19$)."
            },
            {
                "id": "q18",
                "question": "Solve the equation: 14 - 2x = 6",
                "options": ["x = 4", "x = 5", "x = 8", "x = 10"],
                "correct": 0,
                "solution": "Step 1: Subtract 14: $-2x = 6 - 14 = -8$.<br>Step 2: Divide by $-2$: $x = \\frac{-8}{-2} = 4$."
            },
            {
                "id": "q19",
                "question": "Solve for t: 4(t + 2) = 28",
                "options": ["t = 3", "t = 5", "t = 7", "t = 9"],
                "correct": 1,
                "solution": "Step 1: Divide both sides by 4: $t + 2 = \\frac{28}{4} = 7$.<br>Step 2: Subtract 2: $t = 7 - 2 = 5$."
            },
            {
                "id": "q20",
                "question": "Which operation is the inverse of subtracting 15?",
                "options": ["Multiplying by 15", "Adding 15", "Dividing by 15", "Subtracting 15 again"],
                "correct": 1,
                "solution": "Step 1: Addition and subtraction are mutual inverse operations. The inverse of $-15$ is $+15$."
            }
        ]
    },
    {
        "id": 19,
        "title": "Mastery Challenge • Part III",
        "subtitle": "Transposition, Variables on Both Sides, Geometry & Number Tricks",
        "type": "quiz_slide",
        "questions": [
            {
                "id": "q21",
                "question": "Solve the equation with variables on both sides: 7x - 5 = 4x + 16",
                "options": ["x = 5", "x = 7", "x = 8", "x = 9"],
                "correct": 1,
                "solution": "Step 1: Transpose $4x$ to LHS: $7x - 4x - 5 = 16 \\implies 3x - 5 = 16$.<br>Step 2: Transpose $-5$ to RHS: $3x = 16 + 5 = 21$.<br>Step 3: Divide by 3: $x = \\frac{21}{3} = 7$."
            },
            {
                "id": "q22",
                "question": "Solve for y: 9y + 4 = 5y + 36",
                "options": ["y = 6", "y = 7", "y = 8", "y = 9"],
                "correct": 2,
                "solution": "Step 1: Subtract $5y$: $4y + 4 = 36$.<br>Step 2: Subtract 4: $4y = 32$.<br>Step 3: Divide by 4: $y = 8$."
            },
            {
                "id": "q23",
                "question": "The perimeter of a rectangular swimming pool is 64 m. Its length is 6 m more than its width. What is the width w?",
                "options": ["11 m", "13 m", "15 m", "19 m"],
                "correct": 1,
                "solution": "Step 1: Let width $= w$, length $= w + 6$.<br>Step 2: Perimeter $= 2(w + w + 6) = 64 \\implies 2(2w + 6) = 64 \\implies 4w + 12 = 64$.<br>Step 3: $4w = 52 \\implies w = 13\\text{ m}$."
            },
            {
                "id": "q24",
                "question": "Rohan thinks of a number x. He multiplies it by 5 and subtracts 7. The result is 28. What was his number?",
                "options": ["5", "6", "7", "8"],
                "correct": 2,
                "solution": "Step 1: Equation: $5x - 7 = 28$.<br>Step 2: $5x = 28 + 7 = 35$.<br>Step 3: $x = \\frac{35}{5} = 7$."
            },
            {
                "id": "q25",
                "question": "In a number trick, you think of x, double it (2x), add 16 (2x + 16), divide by 2 (x + 8), and subtract x. What is always the final answer?",
                "options": ["4", "8", "16", "32"],
                "correct": 1,
                "solution": "Step 1: $\\frac{2x + 16}{2} - x = (x + 8) - x = 8$. The result is unconditionally 8."
            },
            {
                "id": "q26",
                "question": "A catering service charges a fixed fee of Rs 2,000 plus Rs 300 per plate. If the total bill is Rs 14,000, how many plates p were ordered?",
                "options": ["30 plates", "35 plates", "40 plates", "45 plates"],
                "correct": 2,
                "solution": "Step 1: $2000 + 300p = 14000$.<br>Step 2: $300p = 12000$.<br>Step 3: $p = \\frac{12000}{300} = 40\\text{ plates}$."
            },
            {
                "id": "q27",
                "question": "Solve the equation: 3(2x - 1) = 4x + 11",
                "options": ["x = 5", "x = 6", "x = 7", "x = 8"],
                "correct": 2,
                "solution": "Step 1: Expand brackets: $6x - 3 = 4x + 11$.<br>Step 2: Subtract $4x$: $2x - 3 = 11$.<br>Step 3: Add 3: $2x = 14 \\implies x = 7$."
            },
            {
                "id": "q28",
                "question": "Two friends start saving money. Ananya has Rs 500 and saves Rs 50 per week. Bharat has Rs 200 and saves Rs 80 per week. After how many weeks w will their savings be equal?",
                "options": ["8 weeks", "10 weeks", "12 weeks", "15 weeks"],
                "correct": 1,
                "solution": "Step 1: $500 + 50w = 200 + 80w$.<br>Step 2: $500 - 200 = 80w - 50w \\implies 300 = 30w$.<br>Step 3: $w = \\frac{300}{30} = 10\\text{ weeks}$."
            },
            {
                "id": "q29",
                "question": "When transposing a multiplying factor 5 across the equal sign, what operation does it perform on the other side?",
                "options": ["Multiplies by 5", "Subtracts 5", "Divides by 5", "Adds 5"],
                "correct": 2,
                "solution": "Step 1: The inverse of multiplication is division. A multiplying factor transposes as a divisor on the opposite side."
            },
            {
                "id": "q30",
                "question": "Solve the equation: 8 - 3x = 2x - 12",
                "options": ["x = 2", "x = 3", "x = 4", "x = 5"],
                "correct": 2,
                "solution": "Step 1: Transpose $-3x$ to RHS: $8 = 5x - 12$.<br>Step 2: Transpose $-12$ to LHS: $8 + 12 = 5x \\implies 20 = 5x$.<br>Step 3: $x = \\frac{20}{5} = 4$."
            }
        ]
    },
    {
        "id": 20,
        "title": "Mastery Challenge • Part IV",
        "subtitle": "Diagnostic Error Clinic, Bījagaṇita History & Brahmagupta's Formula",
        "type": "quiz_slide",
        "questions": [
            {
                "id": "q31",
                "question": "Identify the diagnostic error in this student's solution: 2x + 8 = 20 ⟹ x + 8 = 10.",
                "options": [
                    "20 was divided by 2 incorrectly",
                    "The student divided 2x and 20 by 2, but forgot to divide the term 8 by 2",
                    "The student should have multiplied by 2",
                    "There is no error"
                ],
                "correct": 1,
                "solution": "Step 1: Dividing an entire side by 2 requires dividing every term: $\\frac{2x + 8}{2} = x + 4$.<br>Step 2: The correct step is $x + 4 = 10 \\implies x = 6$."
            },
            {
                "id": "q32",
                "question": "What is the correct expansion of -(3x - 5)?",
                "options": ["-3x - 5", "-3x + 5", "3x - 5", "3x + 5"],
                "correct": 1,
                "solution": "Step 1: A negative sign outside parentheses changes every sign inside: $-(3x - 5) = -3x + 5$."
            },
            {
                "id": "q33",
                "question": "Which Indian mathematician authored the Brāhmasphuṭasiddhānta (628 CE), codifying general linear equation formulas and rules of positive and negative numbers?",
                "options": ["Varāhamihira", "Brahmagupta", "Bhāskara I", "Mādhava"],
                "correct": 1,
                "solution": "Step 1: Acharya Brahmagupta authored the Brāhmasphuṭasiddhānta in 628 CE, presenting the first systematic treatment of algebra, zero, and negative quantities."
            },
            {
                "id": "q34",
                "question": "Using Brahmagupta's formula x = (D - B)/(A - C), solve 8x + 3 = 3x + 28.",
                "options": ["x = 4", "x = 5", "x = 6", "x = 7"],
                "correct": 1,
                "solution": "Step 1: Here $A = 8, B = 3, C = 3, D = 28$.<br>Step 2: $x = \\frac{28 - 3}{8 - 3} = \\frac{25}{5} = 5$."
            },
            {
                "id": "q35",
                "question": "In ancient Indian Bījagaṇita notation, what did the abbreviation 'kā' (from kālaka) represent?",
                "options": ["The constant number 10", "A second unknown quantity represented by the color black", "The equal sign", "A division operation"],
                "correct": 1,
                "solution": "Step 1: Ancient Indian algebraists used color names for multiple unknowns: yā (yāvattāvat = 1st unknown), kā (kālaka = black for 2nd unknown), nī (nīlaka = blue for 3rd unknown)."
            },
            {
                "id": "q36",
                "question": "Which 12th-century Indian mathematical masterpiece contains poetic word problems involving swarms of bees and peacocks?",
                "options": ["Līlāvatī by Bhāskarāchārya", "Śulba-Sūtras", "Āryabhaṭīya", "Gaṇita Sāra Saṅgraha"],
                "correct": 0,
                "solution": "Step 1: Bhāskarāchārya's Līlāvatī (1150 CE) is celebrated for its lyrical, poetic algebra puzzles addressed to his daughter Līlāvatī."
            },
            {
                "id": "q37",
                "question": "What is the solution to the equation 5x + 7 = 5x + 12?",
                "options": [
                    "x = 0",
                    "x = 5",
                    "No solution exists, because subtracting 5x yields 7 = 12, an impossible contradiction",
                    "x = 19"
                ],
                "correct": 2,
                "solution": "Step 1: Subtract $5x$ from both sides: $7 = 12$.<br>Step 2: Since $7 \\ne 12$, no number $x$ can ever satisfy this equation. There is NO solution."
            },
            {
                "id": "q38",
                "question": "What type of equation is 4x + 6 = 2(2x + 3)?",
                "options": [
                    "An equation with no solution",
                    "An identity that is true for ALL values of x",
                    "An equation with exactly one solution x = 6",
                    "A quadratic equation"
                ],
                "correct": 1,
                "solution": "Step 1: Expand RHS: $2(2x + 3) = 4x + 6$.<br>Step 2: Since $\\text{LHS} = \\text{RHS}$ identically for any number $x$, it is an algebraic identity with infinitely many solutions."
            },
            {
                "id": "q39",
                "question": "What ancient Indian algorithm developed by Āryabhaṭa was used to solve linear indeterminate equations?",
                "options": ["Kuṭṭaka (The Pulverizer)", "Vakra", "Manojava", "Trairāśika"],
                "correct": 0,
                "solution": "Step 1: Āryabhaṭa invented the Kuṭṭaka ('pulverizer') algorithm in 499 CE to solve linear Diophantine equations of the form $ax - by = c$."
            },
            {
                "id": "q40",
                "question": "Solve the equation: 5(x - 2) - 2(x + 1) = 6",
                "options": ["x = 4", "x = 5", "x = 6", "x = 7"],
                "correct": 2,
                "solution": "Step 1: Expand brackets: $5x - 10 - 2x - 2 = 6$.<br>Step 2: Combine like terms: $3x - 12 = 6$.<br>Step 3: Add 12: $3x = 18 \\implies x = 6$."
            }
        ]
    }
]

if __name__ == "__main__":
    with open(".agents/class7_math_finding_the_unknown_data.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""Class 7 Mathematics Chapter 7: Finding the Unknown Data File"""\n\n')
        f.write("SLIDES_DATA = " + repr(SLIDES_DATA) + "\n")
    print(f"Successfully generated .agents/class7_math_finding_the_unknown_data.py with {len(SLIDES_DATA)} slides.")
