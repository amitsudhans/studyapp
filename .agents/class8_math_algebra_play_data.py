# Class 8 Mathematics Chapter 13: Algebra Play
# Complete 20-slide dataset: 16 lesson slides with bespoke simulators & 32 checkpoints + 4 mastery challenge slides (40 questions with detailed step-by-step solutions)

SLIDES_DATA = [
  {
    "id": 1,
    "title": "Algebra Play",
    "subtitle": "The Art of Generalized Arithmetic & Variables",
    "content": "<p>In arithmetic, we work with specific numerical facts: $5 + 3 = 8$, $12 \\times 2 = 24$. But arithmetic only tells the story of one number at a time. <strong>Algebra</strong> is the superpower of <em>generalized arithmetic</em>—it allows us to discover and prove truths that hold for <strong>every number in the universe simultaneously</strong>!</p><p class='mt-2'>By using a letter (a <strong>variable</strong> such as $n$ or $x$) to represent an unknown or arbitrary number, a single algebraic expression captures an infinite collection of arithmetic calculations. What looks like 'magic' in number games is simply algebra quietly operating behind the curtain.</p>",
    "key_takeaways": [
      "Algebra generalises arithmetic by replacing specific numbers with variables that represent any value.",
      "An algebraic expression like $2n + 4$ represents a universal recipe, not just a single outcome.",
      "Number puzzles and tricks are concrete manifestations of algebraic identities and cancellations."
    ],
    "formula": "$$\\text{Arithmetic: } 2(7) + 6 = 20 \\quad \\Longleftrightarrow \\quad \\text{Algebra: } 2(n) + 6 = 2n + 6 \\quad (\\forall n \\in \\mathbb{R})$$",
    "simulator_type": "algebra_play_pattern_machine",
    "checkpoints": [
      {
        "question": "What is the key difference between a numerical constant (like 7) and an algebraic variable (like n)?",
        "options": [
          "A constant can change its value at any moment, while a variable is fixed forever",
          "A constant has a single fixed numerical value, while a variable represents any number from a given set",
          "Constants only exist in geometry, while variables only exist in physics",
          "Variables cannot be multiplied or added"
        ],
        "correct": 1,
        "explanation": "A constant holds a specific unchanging quantity (e.g., $7, -3, \\pi$), whereas a variable is a placeholder that can represent any arbitrary number from a domain."
      },
      {
        "question": "If you perform the operations 'take any number $n$, double it, add 10, then divide by 2', what simplified algebraic expression results?",
        "options": [
          "$2n + 5$",
          "$n + 10$",
          "$n + 5$",
          "$n + 20$"
        ],
        "correct": 2,
        "explanation": "Translating step-by-step: $\\frac{2n + 10}{2} = \\frac{2(n + 5)}{2} = n + 5$. The output is always exactly 5 greater than your starting number."
      }
    ]
  },
  {
    "id": 2,
    "title": "Number Tricks",
    "subtitle": "Thinking about 'Think of a Number' Tricks",
    "content": "<p>You have likely encountered a classic 'mind-reading' trick: <em>'Think of any number. Add 5. Multiply by 2. Add 10. Divide by 2. Subtract your original secret number... Your answer is 10!'</em></p><p class='mt-2'>How could the magician possibly know the answer without knowing your secret number? The secret is <strong>variable cancellation</strong>! Let your secret number be $x$:</p><div class='p-3 bg-indigo-950/40 rounded border border-indigo-700/40 my-2 font-mono text-sm text-indigo-200'>$$\\text{Start: } x \\longrightarrow x + 5 \\longrightarrow 2(x + 5) = 2x + 10 \\longrightarrow 2x + 20 \\longrightarrow \\frac{2x + 20}{2} = x + 10 \\longrightarrow (x + 10) - x = 10$$</div><p class='mt-2'>Because $x - x = 0$, the starting number vanishes completely, leaving only a constant guaranteed result.</p>",
    "key_takeaways": [
      "'Think of a number' tricks work because the algebraic sequence eliminates the secret variable $x$.",
      "Multiplying and later dividing by the same factor scales the variable back to $1x$, which is then subtracted away ($x - x = 0$).",
      "Any trick ending with 'subtract your original number' guarantees a constant result independent of the initial choice."
    ],
    "formula": "$$\\text{Trick: } \\frac{2(x + a) + b}{2} - x = \\frac{2x + 2a + b}{2} - x = x + a + \\frac{b}{2} - x = a + \\frac{b}{2}$$",
    "simulator_type": "think_of_number_trick_revealer",
    "checkpoints": [
      {
        "question": "A magician instructs: 'Think of a number $x$, add 8, multiply by 3, subtract 6, divide by 3, then subtract your original number.' What is the final result?",
        "options": [
          "8",
          "6",
          "7",
          "12"
        ],
        "correct": 1,
        "explanation": "Algebraic steps: $\\frac{3(x + 8) - 6}{3} - x = \\frac{3x + 24 - 6}{3} - x = \\frac{3x + 18}{3} - x = (x + 6) - x = 6$."
      },
      {
        "question": "Why does the magician's trick work for negative numbers and fractions just as well as positive integers?",
        "options": [
          "Because magic spells only work on non-zero numbers",
          "Because algebraic cancellation $x - x = 0$ is an identity valid for all real numbers $x$",
          "Because fractions cannot be multiplied by 2",
          "Because negative numbers become positive when divided"
        ],
        "correct": 1,
        "explanation": "Algebraic identities are universal: for every real number $x$, $x - x = 0$, regardless of whether $x$ is positive, negative, zero, or a fraction."
      }
    ]
  },
  {
    "id": 3,
    "title": "Reversing Steps",
    "subtitle": "Inverse Operations & Mind-Reading Equations",
    "content": "<p>In another type of number trick, the magician does <em>not</em> ask you to subtract your secret number. Instead, you announce your final number $R$, and the magician instantly deduces your secret starting number $x$!</p><p class='mt-2'>This is not telepathy—it is the systematic execution of <strong>inverse operations</strong>. If the operations performed on $x$ are:</p><div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>$$\\text{Multiply by } a \\longrightarrow \\text{Add } b = R \\quad \\implies \\quad ax + b = R$$</div><p class='mt-2'>To recover $x$, the magician simply runs the film in reverse using opposite operations in reverse order: subtract $b$ first, then divide by $a$:</p><div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>$$x = \\frac{R - b}{a}$$</div>",
    "key_takeaways": [
      "Linear operations forward: $x \\to ax + b = R$. Reverse operations: $x = \\frac{R - b}{a}$.",
      "Inverse operations undo each other: addition is undone by subtraction, multiplication by division.",
      "Order matters: reversing a sequence requires reversing both the operations and their order of application."
    ],
    "formula": "$$f(x) = ax + b = R \\iff x = f^{-1}(R) = \\frac{R - b}{a}$$",
    "simulator_type": "reverse_engineering_solver",
    "checkpoints": [
      {
        "question": "A student multiplies a secret number by 4 and adds 15, ending up with 47. What was the starting secret number?",
        "options": [
          "6",
          "7",
          "8",
          "9"
        ],
        "correct": 2,
        "explanation": "Equation: $4x + 15 = 47 \\implies 4x = 47 - 15 = 32 \\implies x = 32 / 4 = 8$."
      },
      {
        "question": "If the forward sequence is 'Divide by 3, then subtract 7', what is the exact reverse sequence to restore the initial number?",
        "options": [
          "Multiply by 3, then add 7",
          "Subtract 7, then divide by 3",
          "Add 7, then multiply by 3",
          "Add 21, then divide by 3"
        ],
        "correct": 2,
        "explanation": "To invert $y = \\frac{x}{3} - 7$, reverse the steps and order: first add 7 ($y + 7 = \\frac{x}{3}$), then multiply the whole sum by 3: $x = 3(y + 7)$."
      }
    ]
  },
  {
    "id": 4,
    "title": "Number Pyramids",
    "subtitle": "Additive Invariants in 3-Tier Stacks",
    "content": "<p>In an <strong>addition pyramid</strong>, each brick contains the sum of the two bricks directly beneath it. Suppose the bottom row of a 3-tier pyramid contains three numbers: $a, b, c$.</p><div class='p-3 bg-slate-900/60 rounded border border-indigo-500/30 my-2 text-center'><div class='text-amber-300 font-bold'>Top Apex: $(a + b) + (b + c) = a + 2b + c$</div><div class='text-cyan-300 text-sm mt-1'>Middle Tier: $(a + b) \\quad \\text{and} \\quad (b + c)$</div><div class='text-emerald-300 text-sm mt-1'>Base Tier: $a \\quad b \\quad c$</div></div><p class='mt-2'>Notice the extraordinary algebraic discovery: the central base brick $b$ contributes to <strong>both</strong> intermediate bricks, so it is counted <strong>twice</strong> in the apex sum! The outer bricks $a$ and $c$ are only counted once.</p>",
    "key_takeaways": [
      "In a 3-tier addition pyramid with base $[a, b, c]$, the top apex is always $a + 2b + c$.",
      "The central block $b$ has twice the weighting of the flanking edge blocks $a$ and $c$.",
      "To maximize the apex sum using a fixed set of three numbers, place the largest number in the center position $b$!"
    ],
    "formula": "$$\\text{Apex}(a, b, c) = a + 2b + c = (a + b + c) + b$$",
    "simulator_type": "number_pyramid_3tier_builder",
    "checkpoints": [
      {
        "question": "You are given the numbers 3, 5, and 8 to place in the base of a 3-tier pyramid. Which base arrangement produces the largest possible apex number?",
        "options": [
          "[8, 3, 5] with apex 19",
          "[3, 5, 8] with apex 21",
          "[3, 8, 5] with apex 24",
          "[5, 3, 8] with apex 19"
        ],
        "correct": 2,
        "explanation": "Apex formula is $a + 2b + c$. To maximize, put the largest value 8 in the center $b$: $\\text{Apex} = 3 + 2(8) + 5 = 3 + 16 + 5 = 24$."
      },
      {
        "question": "In a 3-tier pyramid, the base numbers are $a = 4$, $c = 10$, and the apex number is 32. What is the value of the center brick $b$?",
        "options": [
          "7",
          "8",
          "9",
          "11"
        ],
        "correct": 2,
        "explanation": "Equation: $a + 2b + c = 32 \\implies 4 + 2b + 10 = 32 \\implies 2b + 14 = 32 \\implies 2b = 18 \\implies b = 9$."
      }
    ]
  },
  {
    "id": 5,
    "title": "Higher Pyramids",
    "subtitle": "4-Tier Pyramids, Pascal's Coefficients & Solving for Missing Bricks",
    "content": "<p>What happens when we build a 4-tier pyramid with base numbers $a, b, c, d$? Let us trace the algebra up layer by layer:</p><ul><li><strong>Tier 2 (3 bricks):</strong> $a + b, \\quad b + c, \\quad c + d$</li><li><strong>Tier 3 (2 bricks):</strong> $(a + 2b + c), \\quad (b + 2c + d)$</li><li><strong>Apex (1 brick):</strong> $(a + 2b + c) + (b + 2c + d) = \\mathbf{a + 3b + 3c + d}$</li></ul><p class='mt-2'>The coefficients of the base bricks are $\\mathbf{1, 3, 3, 1}$—the exact 3rd row of <strong>Pascal's Triangle</strong> (coefficients of $(x + y)^3$)! This algebraic formula lets us solve for any missing base brick directly with a single linear equation.</p>",
    "key_takeaways": [
      "In a 4-tier addition pyramid, the apex value is $a + 3b + 3c + d$.",
      "The coefficients match Pascal's Triangle: Tier 1 has (1), Tier 2 has (1,1), Tier 3 has (1,2,1), Tier 4 has (1,3,3,1).",
      "Inner base bricks $b$ and $c$ contribute three times as much to the apex as the corner bricks $a$ and $d$."
    ],
    "formula": "$$\\text{Apex}_4(a, b, c, d) = \\binom{3}{0}a + \\binom{3}{1}b + \\binom{3}{2}c + \\binom{3}{3}d = a + 3b + 3c + d$$",
    "simulator_type": "number_pyramid_4tier_solver",
    "checkpoints": [
      {
        "question": "What is the apex value of a 4-tier pyramid with base row [1, 2, 4, 3]?",
        "options": [
          "20",
          "22",
          "25",
          "30"
        ],
        "correct": 1,
        "explanation": "Formula: $\\text{Apex} = a + 3b + 3c + d = 1 + 3(2) + 3(4) + 3 = 1 + 6 + 12 + 3 = 22$."
      },
      {
        "question": "In a 5-tier addition pyramid with base $[a, b, c, d, e]$, what will be the algebraic coefficient of the middle brick $c$ in the apex?",
        "options": [
          "4",
          "6",
          "8",
          "10"
        ],
        "correct": 1,
        "explanation": "For a 5-tier pyramid, apex coefficients follow row 4 of Pascal's triangle: $\\binom{4}{0}=1, \\binom{4}{1}=4, \\binom{4}{2}=6, \\binom{4}{3}=4, \\binom{4}{4}=1$. Thus the coefficient of $c$ is 6."
      }
    ]
  },
  {
    "id": 6,
    "title": "Grid Fun",
    "subtitle": "Fun with $2 \\times 2$ Number Grids & Cross Differences",
    "content": "<p>Consider a 100-square grid where numbers run consecutively in rows of 10. If we highlight any $2 \\times 2$ window of four numbers:</p><div class='p-3 bg-slate-900/60 rounded border border-indigo-500/30 my-2 text-center font-mono'><div class='text-cyan-300'>[ n ] &nbsp; [ n + 1 ]</div><div class='text-amber-300 mt-1'>[ n + 10 ] &nbsp; [ n + 11 ]</div></div><p class='mt-2'>Let us test two cross-operations:</p><ol class='list-decimal pl-5 space-y-1'><li><strong>Cross Diagonal Sums:</strong> $n + (n + 11) = 2n + 11$, and $(n + 1) + (n + 10) = 2n + 11$. The cross sums are <em>identical</em>!</li><li><strong>Cross Diagonal Products:</strong> $n(n + 11) = n^2 + 11n$, while $(n + 1)(n + 10) = n^2 + 11n + 10$.</li></ol><p class='mt-2'>Subtract the two products: $(n^2 + 11n + 10) - (n^2 + 11n) = \\mathbf{10}$. The difference is <strong>always strictly 10</strong>, no matter where you position the window on the entire grid!</p>",
    "key_takeaways": [
      "In any $2 \\times 2$ grid with row step $d$, the top-left to bottom-right product is $n(n + d + 1) = n^2 + dn + n$.",
      "The top-right to bottom-left product is $(n + 1)(n + d) = n^2 + dn + n + d$.",
      "The difference of diagonal products is always identically the row step $d$, independent of $n$!"
    ],
    "formula": "$$(n+1)(n+d) - n(n+d+1) = (n^2 + nd + n + d) - (n^2 + nd + n) = d$$",
    "simulator_type": "grid_diagonal_product_lab",
    "checkpoints": [
      {
        "question": "On a grid with 8 columns (row step $d = 8$), what is the difference between the diagonal products in any $2 \\times 2$ window?",
        "options": [
          "1",
          "8",
          "16",
          "Depends on the starting number $n$"
        ],
        "correct": 1,
        "explanation": "By the invariant theorem: $(n+1)(n+8) - n(n+9) = (n^2 + 9n + 8) - (n^2 + 9n) = 8$. The difference is always equal to the row step $d = 8$."
      },
      {
        "question": "Why do the cross-diagonal sums in any $2 \\times 2$ grid always equal each other?",
        "options": [
          "Because both equal $2n + d + 1$",
          "Because multiplication is associative",
          "Because all grids are magic squares",
          "Only when $n$ is an even number"
        ],
        "correct": 0,
        "explanation": "Diagonal 1 sum is $n + (n + d + 1) = 2n + d + 1$. Diagonal 2 sum is $(n + 1) + (n + d) = 2n + d + 1$. Both algebraic expressions are identical."
      }
    ]
  },
  {
    "id": 7,
    "title": "3x3 Grids",
    "subtitle": "Symmetry, Centroid Invariants & Magic Squares",
    "content": "<p>Now examine a $3 \\times 3$ block of nine numbers on a grid with row step $d$. Let the central number be $c$:</p><div class='p-3 bg-slate-900/60 rounded border border-indigo-500/30 my-2 font-mono text-center text-sm'><div class='text-slate-300'>c - d - 1 &nbsp; c - d &nbsp; c - d + 1</div><div class='text-amber-300 my-1'>c - 1 &nbsp; [ c ] &nbsp; c + 1</div><div class='text-slate-300'>c + d - 1 &nbsp; c + d &nbsp; c + d + 1</div></div><p class='mt-2'>Look at the opposite pairs across the center $c$:</p><ul><li>$(c - d - 1) + (c + d + 1) = 2c$</li><li>$(c - d) + (c + d) = 2c$</li><li>$(c - 1) + (c + 1) = 2c$</li><li>$(c - d + 1) + (c + d - 1) = 2c$</li></ul><p class='mt-2'>Every pair across the center sums to $2c$. Adding all 4 pairs plus the center $c$ gives: $\\text{Total Sum} = 4(2c) + c = \\mathbf{9c}$! The sum of all nine numbers is always strictly <strong>9 times the center number</strong>.</p>",
    "key_takeaways": [
      "In any $3 \\times 3$ grid with arithmetic step symmetry, opposite cells balance each other around center $c$.",
      "The sum of all 9 numbers in the block is identically $9c$.",
      "The center number $c$ is the exact arithmetic mean of all 9 numbers in the block!"
    ],
    "formula": "$$\\sum_{i=1}^9 x_i = 9c \\iff c = \\frac{1}{9}\\sum_{i=1}^9 x_i = \\bar{x}$$",
    "simulator_type": "magic_grid_3x3_explorer",
    "checkpoints": [
      {
        "question": "A student adds all 9 numbers in a $3 \\times 3$ grid square and obtains 225. What is the center number $c$?",
        "options": [
          "20",
          "25",
          "27",
          "30"
        ],
        "correct": 1,
        "explanation": "Since $\\text{Total Sum} = 9c$, we have $9c = 225 \\implies c = 225 / 9 = 25$."
      },
      {
        "question": "If the center of a $3 \\times 3$ block on a 10-column grid is 45, what is the sum of the four corner numbers?",
        "options": [
          "90",
          "135",
          "180",
          "225"
        ],
        "correct": 2,
        "explanation": "The two diagonal pairs each sum to $2c = 2(45) = 90$. Together, the four corners sum to $2c + 2c = 4c = 4(45) = 180$."
      }
    ]
  },
  {
    "id": 8,
    "title": "Calendar Magic",
    "subtitle": "Monthly Grid Step d=7 & Equal Diagonal Sums",
    "content": "<p>A calendar page is a natural mathematical grid with a row step of $d = 7$ (because there are 7 days in a week). If you frame any $2 \\times 2$ box of 4 dates:</p><div class='p-3 bg-slate-900/60 rounded border border-indigo-500/30 my-2 font-mono text-center'><div class='text-cyan-300'>[ n ] &nbsp; [ n + 1 ]</div><div class='text-amber-300 mt-1'>[ n + 7 ] &nbsp; [ n + 8 ]</div></div><p class='mt-2'>Let us calculate the diagonal sums:</p><ul><li><strong>Main Diagonal:</strong> $n + (n + 8) = 2n + 8$</li><li><strong>Anti-Diagonal:</strong> $(n + 1) + (n + 7) = 2n + 8$</li></ul><p class='mt-2'>The two diagonal sums are <strong>always identical</strong>! Furthermore, the difference between the diagonal products is: $(n + 1)(n + 7) - n(n + 8) = (n^2 + 8n + 7) - (n^2 + 8n) = \\mathbf{7}$. The product difference on every calendar is always 7!</p>",
    "key_takeaways": [
      "In a calendar, row step is $d = 7$, so the dates in a $2 \\times 2$ block are $n, n+1, n+7, n+8$.",
      "Both diagonal sums equal $2n + 8$, meaning their difference is always 0.",
      "The cross-diagonal product difference $(n+1)(n+7) - n(n+8)$ is always exactly 7."
    ],
    "formula": "$$\\text{Diag}_1 = n + (n+8) = 2n+8 = (n+1) + (n+7) = \\text{Diag}_2$$",
    "simulator_type": "calendar_magic_2x2_window",
    "checkpoints": [
      {
        "question": "In a $2 \\times 2$ calendar block, the top-left date is the 11th. What is the sum of the two numbers on either diagonal?",
        "options": [
          "28",
          "30",
          "31",
          "32"
        ],
        "correct": 1,
        "explanation": "Here $n = 11$. The dates are 11, 12, 18, 19. The diagonal sum is $11 + 19 = 30$, and $12 + 18 = 30$ ($2n + 8 = 2(11) + 8 = 30$)."
      },
      {
        "question": "What is the difference of diagonal products $(n+1)(n+7) - n(n+8)$ for a $2 \\times 2$ calendar block starting at the 5th of the month?",
        "options": [
          "0",
          "7",
          "14",
          "49"
        ],
        "correct": 1,
        "explanation": "The product difference is identically $d = 7$ for all calendar $2 \\times 2$ blocks, regardless of which date $n$ starts the box."
      }
    ]
  },
  {
    "id": 9,
    "title": "3x3 Calendar Magic",
    "subtitle": "The 3x3 Date Square: Total Sum = 9 x Center",
    "content": "<p>Here is one of the most celebrated mental math parlor tricks: Ask a volunteer to draw a square around any 9 dates ($3 \\times 3$) on a calendar, add them up, and tell you the sum. In a fraction of a second, you name the <strong>exact center date</strong>, and instantly list all other 8 dates!</p><p class='mt-2'>How does it work? On a calendar with row step $d = 7$, the 9 dates around center $c$ are:</p><div class='p-3 bg-slate-900/60 rounded border border-indigo-500/30 my-2 font-mono text-center text-sm'><div class='text-slate-300'>c - 8 &nbsp; c - 7 &nbsp; c - 6</div><div class='text-amber-300 my-1'>c - 1 &nbsp; [ c ] &nbsp; c + 1</div><div class='text-slate-300'>c + 6 &nbsp; c + 7 &nbsp; c + 8</div></div><p class='mt-2'>Notice the symmetric cancellations: $(-8 + 8 = 0)$, $(-7 + 7 = 0)$, $(-6 + 6 = 0)$, $(-1 + 1 = 0)$. The sum of all deviations from center $c$ is exactly zero!</p><div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>$$\\text{Total Sum} = 9c \\iff c = \\frac{\\text{Total Sum}}{9}$$</div>",
    "key_takeaways": [
      "The sum of all 9 dates in a $3 \\times 3$ calendar square is always $9 \\times \\text{center date}$.",
      "To find the center date, simply divide the volunteer's total sum by 9.",
      "Once you know the center $c$, the smallest (top-left) date is $c - 8$ and the largest (bottom-right) date is $c + 8$."
    ],
    "formula": "$$\\text{Sum} = 9c \\implies c = \\frac{\\text{Sum}}{9}, \\quad \\text{Min} = c - 8, \\quad \\text{Max} = c + 8$$",
    "simulator_type": "calendar_magic_3x3_revealer",
    "checkpoints": [
      {
        "question": "A volunteer adds 9 dates in a $3 \\times 3$ calendar square and announces a total sum of 135. What is the center date?",
        "options": [
          "13",
          "14",
          "15",
          "16"
        ],
        "correct": 2,
        "explanation": "Divide the total sum by 9: $c = 135 / 9 = 15$. The center date is the 15th."
      },
      {
        "question": "If the sum of a $3 \\times 3$ calendar square is 162, what is the smallest (top-left) date in that square?",
        "options": [
          "8th",
          "10th",
          "12th",
          "18th"
        ],
        "correct": 1,
        "explanation": "Center $c = 162 / 9 = 18$. The top-left date is $c - 8 = 18 - 8 = 10$th."
      }
    ]
  },
  {
    "id": 10,
    "title": "Calendar Crosses",
    "subtitle": "The 5-Square '+' Pattern & Centroid Invariant",
    "content": "<p>Calendar magic is not limited to squares! Consider a <strong>plus-shaped cross</strong> ($+$) of 5 dates on a calendar: one central date, plus its four immediate neighbors (top, bottom, left, right).</p><div class='p-3 bg-slate-900/60 rounded border border-indigo-500/30 my-2 font-mono text-center text-sm'><div class='text-cyan-300'>Top: c - 7</div><div class='text-amber-300 my-1'>Left: c - 1 &nbsp; [ Center: c ] &nbsp; Right: c + 1</div><div class='text-cyan-300'>Bottom: c + 7</div></div><p class='mt-2'>Let us add the 5 dates algebraically:</p><div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>$$\\text{Sum} = (c - 7) + (c + 7) + (c - 1) + (c + 1) + c = 5c$$</div><p class='mt-2'>The vertical offset cancels $(-7 + 7 = 0)$, and the horizontal offset cancels $(-1 + 1 = 0)$, leaving exactly $5c$! A magician can reveal the center date of any calendar cross by simply dividing the sum by 5.</p>",
    "key_takeaways": [
      "In any 5-date '+' cross on a calendar, the sum of all 5 dates is strictly $5 \\times \\text{center date}$.",
      "The horizontal and vertical deviations from the center sum to zero: $(-1 + 1) + (-7 + 7) = 0$.",
      "Similarly, an 'X' shaped cross (center plus 4 diagonal corners) also sums to $5c$."
    ],
    "formula": "$$\\text{Sum}_{\\text{cross}} = (c - 7) + (c + 7) + (c - 1) + (c + 1) + c = 5c \\iff c = \\frac{\\text{Sum}_{\\text{cross}}}{5}$$",
    "simulator_type": "calendar_cross_plus_shape",
    "checkpoints": [
      {
        "question": "A student chooses a plus-shaped cross of 5 dates on a calendar with a total sum of 85. What date sits at the center of the cross?",
        "options": [
          "15th",
          "16th",
          "17th",
          "19th"
        ],
        "correct": 2,
        "explanation": "Equation: $5c = 85 \\implies c = 85 / 5 = 17$. The center date is the 17th."
      },
      {
        "question": "If the center of a calendar cross is the 14th, what are the top and bottom dates of the cross?",
        "options": [
          "Top: 13th, Bottom: 15th",
          "Top: 7th, Bottom: 21st",
          "Top: 6th, Bottom: 22nd",
          "Top: 8th, Bottom: 20th"
        ],
        "correct": 1,
        "explanation": "Top date is $c - 7 = 14 - 7 = 7$th. Bottom date is $c + 7 = 14 + 7 = 21$st."
      }
    ]
  },
  {
    "id": 11,
    "title": "Algebra Grids",
    "subtitle": "Visual Area Models & Multiplying (x+a)(x+b)",
    "content": "<p>How can we multiply algebraic binomials like $(x + 3)(x + 4)$ without relying on rote memorization? We use an <strong>algebra grid</strong> (or geometric area model)!</p><p class='mt-2'>Construct a large rectangle whose width is $(x + a)$ and height is $(x + b)$. By partitioning each dimension, the big rectangle splits cleanly into four smaller quadrants:</p><ul class='space-y-1 mt-2'><li>Top-Left: $x \\times x = \\mathbf{x^2}$</li><li>Top-Right: $x \\times a = \\mathbf{ax}$</li><li>Bottom-Left: $x \\times b = \\mathbf{bx}$</li><li>Bottom-Right: $a \\times b = \\mathbf{ab}$</li></ul><p class='mt-2'>Summing the four sub-areas gives the total area:</p><div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>$$(x + a)(x + b) = x^2 + ax + bx + ab = x^2 + (a + b)x + ab$$</div>",
    "key_takeaways": [
      "The product of two linear binomials corresponds to the total geometric area of a partitioned rectangle.",
      "The four sub-rectangles have areas $x^2$, $ax$, $bx$, and $ab$.",
      "Combining the like terms gives $(x + a)(x + b) = x^2 + (a + b)x + ab$."
    ],
    "formula": "$$\\text{Area} = (x + a)(x + b) = x^2 + (a + b)x + ab$$",
    "simulator_type": "algebra_grid_area_multiplication",
    "checkpoints": [
      {
        "question": "What is the expanded form of $(x + 5)(x + 3)$ using the algebra grid area model?",
        "options": [
          "$x^2 + 8x + 15$",
          "$x^2 + 15x + 8$",
          "$x^2 + 8x + 8$",
          "$2x + 15$"
        ],
        "correct": 0,
        "explanation": "Formula: $x^2 + (5 + 3)x + (5 \\times 3) = x^2 + 8x + 15$."
      },
      {
        "question": "In the algebra grid for $(x + 6)(x + 2)$, what is the coefficient of the linear $x$ term?",
        "options": [
          "4",
          "8",
          "12",
          "16"
        ],
        "correct": 1,
        "explanation": "The linear term comes from adding the two rectangular areas $6x + 2x = (6 + 2)x = 8x$, so the coefficient is 8."
      }
    ]
  },
  {
    "id": 12,
    "title": "Visual Identities",
    "subtitle": "Geometric Proofs of (a+b)^2 and (a-b)^2",
    "content": "<p>Algebraic identities are not just strings of symbols—they are <strong>geometric truths</strong> carved into space! Let us examine a square of side length $(a + b)$:</p><p class='mt-2'>Dividing each side into segments $a$ and $b$ dissects the total square into:</p><ul><li>One large square of area $a^2$</li><li>One small square of area $b^2$</li><li>Two identical rectangles of area $ab$ each</li></ul><div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>$$(a + b)^2 = a^2 + 2ab + b^2$$</div><p class='mt-2'>Similarly, to visualize $(a - b)^2$, take a square of area $a^2$, subtract two rectangles of area $ab$, and notice that the corner $b^2$ was subtracted twice and must be added back (inclusion-exclusion): $(a - b)^2 = a^2 - 2ab + b^2$!</p>",
    "key_takeaways": [
      "The identity $(a + b)^2 = a^2 + 2ab + b^2$ is geometrically verified by dissecting a square into 4 sections.",
      "The cross term $2ab$ represents the two symmetrical rectangles flanking the main $a^2$ square.",
      "The difference of squares $(a + b)(a - b) = a^2 - b^2$ can be visualised by rearranging an L-shaped region."
    ],
    "formula": "$$(a + b)^2 = a^2 + 2ab + b^2 \\quad \\text{and} \\quad (a - b)^2 = a^2 - 2ab + b^2$$",
    "simulator_type": "visual_identities_square_geometry",
    "checkpoints": [
      {
        "question": "Why is $(a + b)^2$ not equal to $a^2 + b^2$?",
        "options": [
          "Because squares can never be added together",
          "Because the expansion misses the two rectangular regions of area $ab$ each (the $2ab$ term)",
          "Because $a$ and $b$ must always be equal",
          "Because $(a + b)^2$ only applies to negative numbers"
        ],
        "correct": 1,
        "explanation": "A square of side $(a + b)$ contains an $a^2$ region, a $b^2$ region, and two $ab$ rectangles. Omitting $2ab$ neglects a major portion of the geometric area."
      },
      {
        "question": "Use the identity $(a+b)^2 = a^2 + 2ab + b^2$ to mentally calculate $52^2$ ($50 + 2$):",
        "options": [
          "2504",
          "2604",
          "2704",
          "2804"
        ],
        "correct": 2,
        "explanation": "$52^2 = (50 + 2)^2 = 50^2 + 2(50)(2) + 2^2 = 2500 + 200 + 4 = 2704$."
      }
    ]
  },
  {
    "id": 13,
    "title": "Largest Product",
    "subtitle": "Fixed Sum Optimization & The Square Maximizer",
    "content": "<p>Suppose you have a fixed sum $S$ (for example, $S = 20$) to split into two non-negative numbers: $x$ and $y$, where $x + y = 20$. <strong>How should you choose $x$ and $y$ to make their product $P = x \\cdot y$ as large as possible?</strong></p><p class='mt-2'>Let us test some integer pairs:</p><ul><li>$1 + 19 = 20 \\implies 1 \\times 19 = 19$</li><li>$5 + 15 = 20 \\implies 5 \\times 15 = 75$</li><li>$8 + 12 = 20 \\implies 8 \\times 12 = 96$</li><li>$10 + 10 = 20 \\implies 10 \\times 10 = \\mathbf{100}$!</li></ul><p class='mt-2'>Algebraically: $P(x) = x(S - x) = Sx - x^2$. Completing the square reveals:</p><div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>$$P(x) = \\left(\\frac{S}{2}\\right)^2 - \\left(x - \\frac{S}{2}\\right)^2$$</div><p class='mt-2'>Since the subtracted square is always $\\ge 0$, the maximum occurs when $x = \\frac{S}{2}$ (a perfect square)!</p>",
    "key_takeaways": [
      "For a fixed sum $x + y = S$, the product $xy$ is maximized when the numbers are as close together as possible: $x = y = S/2$.",
      "Among all rectangles with a given fixed perimeter, the square encloses the greatest possible area.",
      "Algebraically, $x(S - x) = (S/2)^2 - (x - S/2)^2$, which reaches its global peak at $x = S/2$."
    ],
    "formula": "$$\\max(x \\cdot y) \\quad \\text{subject to } x + y = S \\implies x = y = \\frac{S}{2}, \\quad P_{\\max} = \\frac{S^2}{4}$$",
    "simulator_type": "largest_product_fixed_sum_slider",
    "checkpoints": [
      {
        "question": "A farmer has 40 meters of fencing to enclose a rectangular garden. What dimensions produce the largest possible garden area?",
        "options": [
          "Length 15 m, Width 5 m (Area 75 m²)",
          "Length 12 m, Width 8 m (Area 96 m²)",
          "Length 10 m, Width 10 m (Area 100 m²)",
          "Length 18 m, Width 2 m (Area 36 m²)"
        ],
        "correct": 2,
        "explanation": "Perimeter $2(L + W) = 40 \\implies L + W = 20$. The product $L \\times W$ is maximized when $L = W = 10$ m, giving area $10 \\times 10 = 100$ m²."
      },
      {
        "question": "Two positive numbers sum to 16. What is the maximum possible product of these two numbers?",
        "options": [
          "56",
          "60",
          "63",
          "64"
        ],
        "correct": 3,
        "explanation": "The maximum product occurs when both numbers are equal: $x = y = 16 / 2 = 8$. Product is $8 \\times 8 = 64$."
      }
    ]
  },
  {
    "id": 14,
    "title": "Optimal Partitions",
    "subtitle": "Partitioning a Sum to Maximize the Product (The Rule of 3s)",
    "content": "<p>Now consider a deeper mathematical puzzle: <em>Suppose you can split a positive integer $N$ into any number of positive integer parts that sum to $N$. What partition produces the maximum possible product of all parts?</em></p><p class='mt-2'>Let us test for $N = 10$:</p><ul><li>$5 + 5 = 10 \\implies 5 \\times 5 = 25$</li><li>$2 + 2 + 2 + 2 + 2 = 10 \\implies 2^5 = 32$</li><li>$3 + 3 + 4 = 10 \\implies 3 \\times 3 \\times 4 = \\mathbf{36}$!</li><li>$1 + 1 + \\dots = 10 \\implies 1^{10} = 1$ (1 is useless in products)</li></ul><p class='mt-2'><strong>The Theorem of 3s:</strong> In calculus, the optimal base for maximizing $x^{N/x}$ is Euler's number $e \\approx 2.718$. Since we are restricted to integers, the closest integer to $e$ is <strong>3</strong>! Therefore, we should break $N$ into as many 3s as possible, with at most two 2s to handle remainders.</p>",
    "key_takeaways": [
      "To maximize the product of integers summing to $N$, break $N$ into parts of 3 as much as possible.",
      "Never use 1s, because $1 \\times (k - 1) < k$.",
      "If remainder modulo 3 is 1 (e.g. $N=10 \\implies 3+3+3+1$), combine $3 + 1 = 4 = 2 \\times 2$ (since $2 \\times 2 = 4 > 3 \\times 1 = 3$)."
    ],
    "formula": "$$\\text{Max Product for } N: \\quad P_{\\max} = \\begin{cases} 3^{N/3} & N \\equiv 0 \\pmod 3 \\\\ 4 \\cdot 3^{(N-4)/3} = 2^2 \\cdot 3^{(N-4)/3} & N \\equiv 1 \\pmod 3 \\\\ 2 \\cdot 3^{(N-2)/3} & N \\equiv 2 \\pmod 3 \\end{cases}$$",
    "simulator_type": "partitioning_product_optimizer",
    "checkpoints": [
      {
        "question": "What is the maximum product attainable by partitioning the number 12 into positive integers?",
        "options": [
          "36",
          "64",
          "81",
          "144"
        ],
        "correct": 2,
        "explanation": "$12 = 3 + 3 + 3 + 3$. Maximum product is $3^4 = 81$."
      },
      {
        "question": "Why should you never include the number 1 when maximizing the product of a partition?",
        "options": [
          "Because 1 is an odd number",
          "Because 1 does not increase the product at all ($k \\times 1 = k$), but merging it into another part $(k+1)$ increases the product",
          "Because 1 is not a prime number",
          "Because division by 1 is undefined"
        ],
        "correct": 1,
        "explanation": "Multiplying by 1 contributes nothing to the product ($1 \\cdot x = x$). Merging 1 with any factor $x \\ge 2$ gives $(x+1) > x \\cdot 1$, increasing the total product."
      }
    ]
  },
  {
    "id": 15,
    "title": "Divisibility Tricks",
    "subtitle": "Decoding Decimal Place Expansion: 10^k = 99...9 + 1",
    "content": "<p>In elementary school, we learned the magical rule: <em>A number is divisible by 9 if and only if the sum of its digits is divisible by 9.</em> But <strong>why</strong> does this rule work? Algebra reveals the truth through place value expansion!</p><p class='mt-2'>Any 3-digit number $N$ with digits $a, b, c$ equals: $N = 100a + 10b + c$. Now rewrite powers of 10 as multiples of 9 plus 1:</p><div class='p-3 bg-slate-900/60 rounded border border-indigo-500/30 my-2 font-mono text-sm'>$$N = (99 + 1)a + (9 + 1)b + c = (99a + 9b) + (a + b + c)$$</div><p class='mt-2'>Factoring out 9 from the first group gives:</p><div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>$$N = 9(11a + b) + (a + b + c)$$</div><p class='mt-2'>Since $9(11a + b)$ is obviously always divisible by 9, the whole number $N$ is divisible by 9 if and only if the leftover remainder $(a + b + c)$ is divisible by 9!</p>",
    "key_takeaways": [
      "Every power of 10 is one more than a multiple of 9: $10^k = 99\\dots9 + 1 = 9M + 1$.",
      "Expanding $N = \\sum d_k 10^k$ separates $N$ into $9(\\text{integer}) + \\sum d_k$.",
      "Since 9 is a multiple of 3, the exact same digital root rule applies to divisibility by 3."
    ],
    "formula": "$$N = 9K + \\sum_{i=0}^n d_i \\implies N \\equiv \\sum_{i=0}^n d_i \\pmod 9$$",
    "simulator_type": "divisibility_9_decimal_expander",
    "checkpoints": [
      {
        "question": "What is the remainder when the number 7,458 is divided by 9?",
        "options": [
          "3",
          "5",
          "6",
          "0 (it is divisible)"
        ],
        "correct": 2,
        "explanation": "Sum of digits: $7 + 4 + 5 + 8 = 24$. Then $2 + 4 = 6$. Since $24 = 2 \\times 9 + 6$, the remainder when divided by 9 is 6."
      },
      {
        "question": "Which algebraic property explains why the divisibility rule for 9 also works for 3?",
        "options": [
          "Because 3 is a prime number",
          "Because any multiple of 9 is automatically a multiple of 3 ($9 = 3 \\times 3$)",
          "Because 3 and 9 are consecutive odd numbers",
          "Because $10 + 3 = 13$"
        ],
        "correct": 1,
        "explanation": "Since $9(11a + b) = 3[3(11a + b)]$, the term is also divisible by 3. Hence $N$ is divisible by 3 if and only if its digit sum $(a + b + c)$ is divisible by 3."
      }
    ]
  },
  {
    "id": 16,
    "title": "Divisibility: 11",
    "subtitle": "Alternating Sums: 10^k = 11m + (-1)^k & Modular Cancelling",
    "content": "<p>Why is a number divisible by 11 if the <strong>alternating sum of its digits</strong> (units - tens + hundreds - thousands...) is divisible by 11? Once again, algebra provides the proof!</p><p class='mt-2'>Let us inspect powers of 10 compared to multiples of 11:</p><ul><li>$1 = 11(0) + 1 = 11m + 1$</li><li>$10 = 11(1) - 1 = 11m - 1$</li><li>$100 = 99 + 1 = 11(9) + 1 = 11m + 1$</li><li>$1000 = 1001 - 1 = 11(91) - 1 = 11m - 1$</li></ul><p class='mt-2'>Powers of 10 alternate between $(11m + 1)$ and $(11m - 1)$! For a 4-digit number $N = 1000a + 100b + 10c + d$:</p><div class='p-2 bg-indigo-950/40 rounded border border-indigo-700/40 text-center font-bold text-indigo-200'>$$N = 11(91a + 9b + c) + (-a + b - c + d)$$</div><p class='mt-2'>$N$ is divisible by 11 if and only if $(d - c + b - a)$ is a multiple of 11 (including 0)!</p>",
    "key_takeaways": [
      "Powers of 10 modulo 11 alternate: $10^k \\equiv (-1)^k \\pmod{11}$.",
      "Even powers ($10^0, 10^2, 10^4$) have remainder $+1$; odd powers ($10^1, 10^3, 10^5$) have remainder $-1$.",
      "A number is divisible by 11 if and only if the difference between the sum of digits at odd places and even places is a multiple of 11."
    ],
    "formula": "$$N \\equiv d_0 - d_1 + d_2 - d_3 + \\dots + (-1)^n d_n \\pmod{11}$$",
    "simulator_type": "divisibility_11_alternating_canceller",
    "checkpoints": [
      {
        "question": "Is the number 85,976 divisible by 11?",
        "options": [
          "Yes, because the alternating sum $(6 - 7 + 9 - 5 + 8) = 11$",
          "No, because the last digit is 6",
          "Yes, because the sum of all digits is 35",
          "No, because it has an odd number of digits"
        ],
        "correct": 0,
        "explanation": "Alternating sum from right to left: $6 - 7 + 9 - 5 + 8 = 11$. Since 11 is divisible by 11, the number 85,976 is divisible by 11 ($85,976 = 11 \\times 7,816$)."
      },
      {
        "question": "What single digit $d$ makes the number $7d81$ divisible by 11?",
        "options": [
          "1",
          "3",
          "5",
          "8"
        ],
        "correct": 1,
        "explanation": "Alternating sum from right to left: $(1 + d) - (8 + 7) = d + 1 - 15 = d - 14$. For $d - 14$ to be a multiple of 11 with $d \\in \\{0..9\\}$, we have $d - 14 = -11 \\implies d = 3$. Checking: $7381 = 11 \\times 671$."
      }
    ]
  },
  {
    "id": 17,
    "title": "Mastery Challenge • Part I",
    "subtitle": "Questions 1–10: Variables, Number Tricks & Linear Inversion",
    "questions": [
      {
        "id": 1,
        "question": "A magician asks: 'Think of a number $x$, add 6, multiply by 4, subtract 8, divide by 4, and subtract your original number.' What is the final answer?",
        "options": ["2", "4", "6", "8"],
        "correct": 1,
        "solution": "Algebraic translation:<br>Step 1: $x$<br>Step 2: $x + 6$<br>Step 3: $4(x + 6) = 4x + 24$<br>Step 4: $4x + 24 - 8 = 4x + 16$<br>Step 5: $\\frac{4x + 16}{4} = x + 4$<br>Step 6: $(x + 4) - x = 4$.<br>The final result is always 4."
      },
      {
        "id": 2,
        "question": "If the sequence of operations is 'Multiply by 5, add 12, divide by 2', which expression represents the outcome for input $n$?",
        "options": ["$\\frac{5n + 12}{2}$", "$\\frac{5(n + 12)}{2}$", "$5n + 6$", "$10n + 24$"],
        "correct": 0,
        "solution": "Applying operations in order:<br>1. Multiply by 5: $5n$<br>2. Add 12: $5n + 12$<br>3. Divide by 2: $\\frac{5n + 12}{2} = 2.5n + 6$."
      },
      {
        "id": 3,
        "question": "A friend thinks of a secret number, doubles it, adds 18, and announces the answer is 50. What was the secret number?",
        "options": ["14", "16", "18", "20"],
        "correct": 1,
        "solution": "Equation: $2x + 18 = 50$<br>Subtract 18: $2x = 50 - 18 = 32$<br>Divide by 2: $x = 32 / 2 = 16$."
      },
      {
        "id": 4,
        "question": "Which of the following operations, when performed on secret number $x$, CANNOT be inverted uniquely if arithmetic is restricted to real numbers?",
        "options": ["Adding 10", "Multiplying by 0", "Subtracting 4", "Dividing by 3"],
        "correct": 1,
        "solution": "Multiplying by 0 produces $0 \\times x = 0$ for every number $x$. Division by 0 is undefined, so the original value of $x$ is irrevocably lost."
      },
      {
        "id": 5,
        "question": "Consider the trick: 'Think of $x$, multiply by 3, add $k$, divide by 3, subtract $x$'. If the final answer is always 7, what is the value of $k$?",
        "options": ["7", "14", "21", "28"],
        "correct": 2,
        "solution": "Algebraic steps: $\\frac{3x + k}{3} - x = x + \\frac{k}{3} - x = \\frac{k}{3}$.<br>We are given $\\frac{k}{3} = 7 \\implies k = 7 \\times 3 = 21$."
      },
      {
        "id": 6,
        "question": "If $f(x) = 3x - 5 = 28$, what is $x$?",
        "options": ["9", "10", "11", "12"],
        "correct": 2,
        "solution": "$3x - 5 = 28 \\implies 3x = 28 + 5 = 33 \\implies x = 33 / 3 = 11$."
      },
      {
        "id": 7,
        "question": "A trick says: 'Think of a 2-digit number $10a + b$. Reverse the digits to get $10b + a$. Subtract the smaller from the larger.' What number is the difference ALWAYS divisible by?",
        "options": ["7", "9", "11", "13"],
        "correct": 1,
        "solution": "Difference: $(10a + b) - (10b + a) = 9a - 9b = 9(a - b)$.<br>Since 9 is factored out, the difference between any 2-digit number and its reverse is always a multiple of 9."
      },
      {
        "id": 8,
        "question": "Continuing from the previous question, if you ADD a 2-digit number to its reverse, what number is the sum ALWAYS divisible by?",
        "options": ["9", "10", "11", "12"],
        "correct": 2,
        "solution": "Sum: $(10a + b) + (10b + a) = 11a + 11b = 11(a + b)$.<br>Since 11 is factored out, the sum is always a multiple of 11."
      },
      {
        "id": 9,
        "question": "A magician asks you to think of a number $n$, add 10, multiply by 2, subtract 4, divide by 2, and then asks: 'Tell me your final result $Y$'. The magician calculates $Y - 8$. What does this yield?",
        "options": ["$n$", "$2n$", "$n + 8$", "8"],
        "correct": 0,
        "solution": "Steps: $\\frac{2(n + 10) - 4}{2} = \\frac{2n + 20 - 4}{2} = \\frac{2n + 16}{2} = n + 8 = Y$.<br>Subtracting 8 gives $Y - 8 = (n + 8) - 8 = n$, revealing your secret number!"
      },
      {
        "id": 10,
        "question": "If you multiply any integer by 6, add 8, and divide by 2, the result is:",
        "options": ["Always odd", "Always even", "Always prime", "Can be either even or odd"],
        "correct": 3,
        "solution": "Expression: $\\frac{6n + 8}{2} = 3n + 4$.<br>If $n$ is even (e.g. 2): $3(2) + 4 = 10$ (even).<br>If $n$ is odd (e.g. 1): $3(1) + 4 = 7$ (odd).<br>Thus it can be either even or odd depending on the parity of $n$."
      }
    ]
  },
  {
    "id": 18,
    "title": "Mastery Challenge • Part II",
    "subtitle": "Questions 11–20: Number Pyramids, Grid Invariants & Diagonal Laws",
    "questions": [
      {
        "id": 11,
        "question": "In a 3-tier pyramid with base row $[x, 7, 4]$, the top apex is 26. What is the value of $x$?",
        "options": ["6", "7", "8", "9"],
        "correct": 2,
        "solution": "Apex formula: $a + 2b + c = \\text{Apex}$.<br>Here $x + 2(7) + 4 = 26 \\implies x + 14 + 4 = 26 \\implies x + 18 = 26 \\implies x = 8$."
      },
      {
        "id": 12,
        "question": "If the base of a 4-tier pyramid is $[2, 1, 3, 5]$, what is the value at the top apex?",
        "options": ["19", "21", "24", "27"],
        "correct": 0,
        "solution": "Apex formula: $a + 3b + 3c + d$.<br>$\\text{Apex} = 2 + 3(1) + 3(3) + 5 = 2 + 3 + 9 + 5 = 19$.<br>Verifying layer by layer:<br>Tier 2: $[2+1, 1+3, 3+5] = [3, 4, 8]$<br>Tier 3: $[3+4, 4+8] = [7, 12]$<br>Tier 4 (Apex): $7 + 12 = 19$."
      },
      {
        "id": 13,
        "question": "In a 3-tier pyramid, you are given the numbers 2, 4, 6 to arrange in the base. What is the MINIMUM possible apex value?",
        "options": ["14", "16", "18", "20"],
        "correct": 0,
        "solution": "Formula: $a + 2b + c$. To minimize, place the smallest number 2 in the center position $b$:<br>$\\text{Apex} = 4 + 2(2) + 6 = 4 + 4 + 6 = 14$."
      },
      {
        "id": 14,
        "question": "In any $2 \\times 2$ window on a calendar ($d = 7$), what is the value of the cross product difference $(n+1)(n+7) - n(n+8)$?",
        "options": ["0", "1", "7", "14"],
        "correct": 2,
        "solution": "Expansion: $(n^2 + 8n + 7) - (n^2 + 8n) = 7$.<br>The product difference is always identically equal to the row step $d = 7$."
      },
      {
        "id": 15,
        "question": "On a grid with row step $d = 6$, the numbers in a $2 \\times 2$ block are $n, n+1, n+6, n+7$. What is the sum of the four numbers in terms of $n$?",
        "options": ["$4n + 7$", "$4n + 12$", "$4n + 14$", "$4n + 20$"],
        "correct": 2,
        "solution": "Sum = $n + (n + 1) + (n + 6) + (n + 7) = 4n + 14$."
      },
      {
        "id": 16,
        "question": "In a $3 \\times 3$ grid block with row step $d=10$, the center number is 50. What is the sum of all 9 numbers in the block?",
        "options": ["350", "400", "450", "500"],
        "correct": 2,
        "solution": "By the centroid invariant theorem, the sum of all 9 numbers in a $3 \\times 3$ grid is $9 \\times \\text{center} = 9 \\times 50 = 450$."
      },
      {
        "id": 17,
        "question": "In a 4-tier pyramid, the base is $[a, b, c, d]$. What is the sum of the coefficients of all base bricks in the apex expression?",
        "options": ["4", "6", "8", "16"],
        "correct": 2,
        "solution": "Coefficients: $1 + 3 + 3 + 1 = 8 = 2^3$.<br>In general, for an $n$-tier pyramid, the sum of the base coefficients is $2^{n-1}$. For $n=4$, $2^{4-1} = 2^3 = 8$."
      },
      {
        "id": 18,
        "question": "In a $2 \\times 2$ grid block, Diagonal 1 has numbers 14 and 25, while Diagonal 2 has numbers 15 and $x$. What is $x$?",
        "options": ["22", "23", "24", "26"],
        "correct": 2,
        "solution": "Since diagonal sums must be equal: $14 + 25 = 39$.<br>Therefore, $15 + x = 39 \\implies x = 39 - 15 = 24$."
      },
      {
        "id": 19,
        "question": "If a 3-tier pyramid has base $[x, x+1, x+2]$, what is the apex value in terms of $x$?",
        "options": ["$3x + 3$", "$4x + 4$", "$4x + 6$", "$3x + 6$"],
        "correct": 1,
        "solution": "Apex = $a + 2b + c = x + 2(x + 1) + (x + 2) = x + 2x + 2 + x + 2 = 4x + 4$."
      },
      {
        "id": 20,
        "question": "In a grid with column width 9, what is the difference between diagonal products $(n+1)(n+9) - n(n+10)$?",
        "options": ["1", "9", "10", "18"],
        "correct": 1,
        "solution": "$(n^2 + 10n + 9) - (n^2 + 10n) = 9$. The difference is strictly equal to the column width $d = 9$."
      }
    ]
  },
  {
    "id": 19,
    "title": "Mastery Challenge • Part III",
    "subtitle": "Questions 21–30: Calendar Magic, Plus Shapes & Algebra Grids",
    "questions": [
      {
        "id": 21,
        "question": "A friend encloses a $3 \\times 3$ block of dates on a calendar and says the sum is 180. What date is at the bottom-right corner?",
        "options": ["20th", "26th", "27th", "28th"],
        "correct": 3,
        "solution": "Total sum = $9c = 180 \\implies c = 180 / 9 = 20$.<br>The bottom-right corner is $c + 8 = 20 + 8 = 28$th."
      },
      {
        "id": 22,
        "question": "In a calendar '+' shape cross of 5 dates, the sum is 105. What date is at the top of the cross?",
        "options": ["7th", "14th", "21st", "28th"],
        "correct": 1,
        "solution": "Cross sum = $5c = 105 \\implies c = 105 / 5 = 21$.<br>The top date is one week earlier: $c - 7 = 21 - 7 = 14$th."
      },
      {
        "id": 23,
        "question": "What is the product of $(x + 7)(x - 3)$ expanded via an algebra grid?",
        "options": ["$x^2 + 4x - 21$", "$x^2 - 4x - 21$", "$x^2 + 10x - 21$", "$x^2 - 21$"],
        "correct": 0,
        "solution": "Formula: $x^2 + (a + b)x + ab$.<br>Here $a = 7, b = -3$:<br>$x^2 + (7 - 3)x + 7(-3) = x^2 + 4x - 21$."
      },
      {
        "id": 24,
        "question": "In the algebra grid for $(2x + 3)(x + 4)$, what is the total area expression?",
        "options": ["$2x^2 + 11x + 12$", "$2x^2 + 7x + 12$", "$2x^2 + 14x + 12$", "$3x^2 + 11x + 12$"],
        "correct": 0,
        "solution": "Quadrant areas:<br>$(2x)(x) = 2x^2$<br>$(2x)(4) = 8x$<br>$(3)(x) = 3x$<br>$(3)(4) = 12$<br>Sum: $2x^2 + (8x + 3x) + 12 = 2x^2 + 11x + 12$."
      },
      {
        "id": 25,
        "question": "An 'X' shape on a calendar consists of center $c$ and its four diagonal neighbors ($c-8, c-6, c+6, c+8$). What is the sum of these 5 dates?",
        "options": ["$4c$", "$5c$", "$9c$", "$5c + 14$"],
        "correct": 1,
        "solution": "Sum = $(c - 8) + (c - 6) + (c + 6) + (c + 8) + c$.<br>Notice $(-8 + 8 = 0)$ and $(-6 + 6 = 0)$.<br>Sum = $5c$."
      },
      {
        "id": 26,
        "question": "If $(x + k)^2 = x^2 + 14x + 49$, what is the value of $k$?",
        "options": ["5", "7", "14", "49"],
        "correct": 1,
        "solution": "Identity: $(x + k)^2 = x^2 + 2kx + k^2$.<br>Comparing linear coefficients: $2k = 14 \\implies k = 7$.<br>Checking constant term: $7^2 = 49$ (consistent)."
      },
      {
        "id": 27,
        "question": "Calculate $98^2$ using the algebraic identity $(a - b)^2 = a^2 - 2ab + b^2$ with $a = 100, b = 2$:",
        "options": ["9404", "9604", "9804", "9904"],
        "correct": 1,
        "solution": "$98^2 = (100 - 2)^2 = 100^2 - 2(100)(2) + 2^2 = 10,000 - 400 + 4 = 9,604$."
      },
      {
        "id": 28,
        "question": "A $3 \\times 3$ calendar square has top-left date 3. What is the sum of all 9 dates?",
        "options": ["90", "99", "108", "117"],
        "correct": 1,
        "solution": "Top-left date is $c - 8 = 3 \\implies c = 11$.<br>Sum of all 9 dates = $9c = 9 \\times 11 = 99$."
      },
      {
        "id": 29,
        "question": "Which algebraic identity represents the factorization of $x^2 - y^2$?",
        "options": ["$(x - y)^2$", "$(x + y)(x - y)$", "$(x + y)^2$", "$x(x - y) + y^2$"],
        "correct": 1,
        "solution": "Difference of squares identity: $x^2 - y^2 = (x + y)(x - y)$. Geometrically, cutting a small square of area $y^2$ from a large square of area $x^2$ leaves an L-shaped region that rearranges into a rectangle of dimensions $(x + y)$ by $(x - y)$."
      },
      {
        "id": 30,
        "question": "What is the area of a square of side $(2x + 5)$ expanded as an algebraic polynomial?",
        "options": ["$4x^2 + 25$", "$4x^2 + 10x + 25$", "$4x^2 + 20x + 25$", "$2x^2 + 20x + 25$"],
        "correct": 2,
        "solution": "$(2x + 5)^2 = (2x)^2 + 2(2x)(5) + 5^2 = 4x^2 + 20x + 25$."
      }
    ]
  },
  {
    "id": 20,
    "title": "Mastery Challenge • Part IV",
    "subtitle": "Questions 31–40: Optimization, Partition Theorems & Divisibility Proofs",
    "questions": [
      {
        "id": 31,
        "question": "You have 60 cm of wire to bend into a rectangle. What is the maximum possible area you can enclose?",
        "options": ["200 cm²", "215 cm²", "225 cm²", "250 cm²"],
        "correct": 2,
        "solution": "Perimeter $2(L + W) = 60 \\implies L + W = 30$.<br>The area $L \\times W$ is maximized when $L = W = 30 / 2 = 15$ cm.<br>Maximum area = $15 \\times 15 = 225$ cm²."
      },
      {
        "id": 32,
        "question": "What is the maximum product of positive integers whose sum is 9?",
        "options": ["20", "24", "27", "30"],
        "correct": 2,
        "solution": "By the Rule of 3s: partition 9 as $3 + 3 + 3$.<br>Product = $3 \\times 3 \\times 3 = 27$."
      },
      {
        "id": 33,
        "question": "What is the maximum product of positive integers whose sum is 8?",
        "options": ["16", "18", "20", "24"],
        "correct": 1,
        "solution": "Splitting 8 into 3s gives remainder 2: $3 + 3 + 2 = 8$.<br>Product = $3 \\times 3 \\times 2 = 18$."
      },
      {
        "id": 34,
        "question": "What is the maximum product of positive integers whose sum is 11?",
        "options": ["48", "54", "56", "64"],
        "correct": 1,
        "solution": "Dividing 11 by 3 gives quotient 3 with remainder 2: $3 + 3 + 3 + 2 = 11$.<br>Product = $3^3 \\times 2 = 27 \\times 2 = 54$."
      },
      {
        "id": 35,
        "question": "Why is the number 43,623 divisible by 9?",
        "options": [
          "Because its last digit is 3",
          "Because the sum of its digits is $4 + 3 + 6 + 2 + 3 = 18$, which is divisible by 9",
          "Because it is an odd number",
          "Because $43,623$ ends in 23"
        ],
        "correct": 1,
        "solution": "Digit sum: $4 + 3 + 6 + 2 + 3 = 18$. Since $18 = 9 \\times 2$, 18 is divisible by 9, meaning 43,623 is divisible by 9 ($43,623 = 9 \\times 4,847$)."
      },
      {
        "id": 36,
        "question": "What single digit $A$ makes the 5-digit number $72A41$ divisible by 9?",
        "options": ["2", "4", "5", "7"],
        "correct": 1,
        "solution": "Sum of existing digits: $7 + 2 + 4 + 1 = 14$.<br>Total sum: $14 + A$.<br>The next multiple of 9 is 18.<br>$14 + A = 18 \\implies A = 4$."
      },
      {
        "id": 37,
        "question": "Test the number 91,828 for divisibility by 11 using the alternating sum of digits:",
        "options": [
          "Divisible, because alternating sum is 22 (a multiple of 11)",
          "Not divisible, because alternating sum is 6",
          "Divisible, because alternating sum is 0",
          "Not divisible, because alternating sum is 14"
        ],
        "correct": 0,
        "solution": "Alternating sum from right to left: $8 - 2 + 8 - 1 + 9 = 22$.<br>Since 22 is an exact multiple of 11 ($11 \\times 2$), the number 91,828 is divisible by 11 ($91,828 = 11 \\times 8,348$)."
      },
      {
        "id": 38,
        "question": "What is the algebraic reason that divisibility by 4 depends ONLY on the last two digits of a number?",
        "options": [
          "Because 4 is an even number",
          "Because 100 and all higher powers of 10 are exact multiples of 4 ($100 = 4 \\times 25$)",
          "Because $4 = 2^2$",
          "Because $10 / 4 = 2.5$"
        ],
        "correct": 1,
        "solution": "Any number can be written as $100K + (10a + b)$. Since $100 = 4 \\times 25$, $100K$ is always divisible by 4. Thus the remainder depends solely on the last two digits $(10a + b)$."
      },
      {
        "id": 39,
        "question": "What digit $B$ makes the number $8B43$ divisible by 11?",
        "options": ["3", "6", "7", "9"],
        "correct": 3,
        "solution": "Alternating sum from right to left: $(3 + B) - (4 + 8) = B + 3 - 12 = B - 9$.<br>For $B - 9$ to be a multiple of 11 with $B \\in \\{0..9\\}$, we must have $B - 9 = 0 \\implies B = 9$.<br>Checking: $8943 = 11 \\times 813$."
      },
      {
        "id": 40,
        "question": "Two positive numbers have a constant product $x \\cdot y = 36$. When is their sum $x + y$ at its MINIMUM?",
        "options": [
          "When $x = 1, y = 36$ (Sum 37)",
          "When $x = 2, y = 18$ (Sum 20)",
          "When $x = 4, y = 9$ (Sum 13)",
          "When $x = 6, y = 6$ (Sum 12)"
        ],
        "correct": 3,
        "solution": "By the AM-GM inequality, for a fixed product $P$, the sum is minimized when the numbers are equal: $x = y = \\sqrt{P} = \\sqrt{36} = 6$. The minimum sum is $6 + 6 = 12$."
      }
    ]
  }
]
