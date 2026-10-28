# -*- coding: utf-8 -*-
"""
Script to create .agents/class7_math_operations_with_integers_data.py
Contains 20 slides, 32 checkpoints, and 40 quiz questions with step-by-step solutions.
"""

import json

SLIDES_DATA = [
    {
        "slide_num": 1,
        "section": "2.1 Foundations",
        "badge": "Integer Recap & Puzzles",
        "title": "A Quick Recap: The World of Integers & Number Puzzles",
        "narration": "Welcome, curious thinkers! I am Acharya Brahmagupta. Today we explore the magnificent realm of integers! Integers include whole numbers and their negative counterparts. Let us unravel how numbers balance each other through exciting sum and difference puzzles.",
        "theory": r"""
          <p class="mb-3">
            The set of <strong>Integers</strong> ($\mathbb{Z}$) extends whole numbers indefinitely in both positive and negative directions:
            $$\mathbb{Z} = \{\dots, -4, -3, -2, -1, 0, 1, 2, 3, 4, \dots\}$$
            Every non-zero integer possesses both a <strong>magnitude</strong> (distance from origin $0$) and a <strong>direction</strong> ($+$ for positive/right/up, $-$ for negative/left/down).
          </p>
          <div class="p-3 rounded-lg bg-sky-950/40 border border-sky-500/30 mb-3">
            <h4 class="font-bold text-sky-300 text-sm mb-1">🧩 Integer Pair Detective Puzzles:</h4>
            <p class="text-xs text-slate-300 mb-1">
              • <em>Sum Condition:</em> Find two integers whose sum is $-5$. Possible pairs: $(-2) + (-3) = -5$, or $(+1) + (-6) = -5$, or $(+5) + (-10) = -5$.
            </p>
            <p class="text-xs text-slate-300">
              • <em>Difference Condition:</em> Find two integers whose difference is $-4$. Pair: $(+1) - (+5) = -4$, or $(-6) - (-2) = -4$.
            </p>
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Integers ($\mathbb{Z}$)</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Magnitude & Direction</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Zero Origin</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">Sum & Difference Pairs</span>
          </div>
        """,
        "sim_id": "sim-integer-puzzle",
        "checkpoints": [
            {
                "id": "1.1",
                "question": "Which of the following pairs of integers has a sum of $-7$ and a difference of $3$?",
                "options": ["$-2$ and $-5$", "$-5$ and $-2$", "$2$ and $-9$", "$-4$ and $-3$"],
                "correct": 0,
                "explanation": "Checking $(-2) + (-5) = -7$, and $(-2) - (-5) = -2 + 5 = 3$. Hence $(-2, -5)$ satisfies both conditions!"
            },
            {
                "id": "1.2",
                "question": "If the sum of two integers is $0$, what must be true about the two integers?",
                "options": ["Both must be zero", "They must be additive inverses (e.g. $a$ and $-a$)", "Both must be negative", "One must be double the other"],
                "correct": 1,
                "explanation": "When $a + b = 0$, $b = -a$. The numbers are opposites (additive inverses) equidistant from zero on opposite sides!"
            }
        ]
    },
    {
        "slide_num": 2,
        "section": "2.1 Number Line",
        "badge": "Carrom Coin Model",
        "title": "Carrom Coin Integers: Movements on the Number Line",
        "narration": "Picture striking a carrom coin along a linear track! Sliding forward to the right represents positive displacement. Sliding backward to the left represents negative displacement. Adding a signed number means performing vector translation along this track.",
        "theory": r"""
          <p class="mb-3">
            On a horizontal number line, the origin $0$ acts as our reference center:
          </p>
          <ul class="list-disc pl-5 space-y-1.5 text-xs text-slate-300 mb-3">
            <li><strong>Positive Integer ($+a$):</strong> Movement of $a$ units to the <em>right</em> (forward direction).</li>
            <li><strong>Negative Integer ($-a$):</strong> Movement of $a$ units to the <em>left</em> (backward direction).</li>
            <li><strong>Addition $x + y$:</strong> Start at position $x$, then move according to the sign and magnitude of $y$.</li>
          </ul>
          <div class="p-3 rounded-lg bg-emerald-950/40 border border-emerald-500/30 mb-3 text-xs text-emerald-200">
            <strong>Carrom Striker Rule:</strong> Striking from $0$ with $+4$ moves to position $+4$. Striking from $+4$ with $-7$ moves $7$ steps left, landing at $4 + (-7) = -3$!
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Number Line Track</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Rightward Vector (+)</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Leftward Vector (-)</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Displacement Resultant</span>
          </div>
        """,
        "sim_id": "sim-carrom-number-line",
        "checkpoints": [
            {
                "id": "2.1",
                "question": "A carrom coin at $-2$ on the number line receives a strike of $+6$, followed by a strike of $-9$. What is its final position?",
                "options": ["$-5$", "$-3$", "$+4$", "$-7$"],
                "correct": 0,
                "explanation": "Starting at $-2$: $-2 + (+6) = +4$. Then $+4 + (-9) = 4 - 9 = -5$!"
            },
            {
                "id": "2.2",
                "question": "Moving 8 units left from $+3$ on the number line lands at:",
                "options": ["$-11$", "$-5$", "$+5$", "$-8$"],
                "correct": 1,
                "explanation": "Moving left means subtracting: $3 - 8 = -5$."
            }
        ]
    },
    {
        "slide_num": 3,
        "section": "2.1 Token Model",
        "badge": "Zero Pairs (±1)",
        "title": "The Token Model: Green Gains & Red Debts",
        "narration": "In ancient Indian commerce, wealth and debts were balanced using physical counters. In our token laboratory, green tokens represent positive one, and red tokens represent negative one. Together, one green and one red annihilate to form a neutral Zero Pair!",
        "theory": r"""
          <p class="mb-3">
            The <strong>Token Model</strong> provides a concrete physical representation of signed numbers:
          </p>
          <div class="grid grid-cols-2 gap-2 mb-3 text-xs">
            <div class="p-2.5 rounded bg-emerald-900/30 border border-emerald-500/30 flex items-center gap-2">
              <span class="w-4 h-4 rounded-full bg-emerald-500 flex items-center justify-center font-bold text-black text-[10px]">+</span>
              <span><strong>Green Token:</strong> $+1$ (Gain / Fortune)</span>
            </div>
            <div class="p-2.5 rounded bg-rose-900/30 border border-rose-500/30 flex items-center gap-2">
              <span class="w-4 h-4 rounded-full bg-rose-500 flex items-center justify-center font-bold text-white text-[10px]">-</span>
              <span><strong>Red Token:</strong> $-1$ (Loss / Debt)</span>
            </div>
          </div>
          <div class="p-3 rounded-lg bg-indigo-950/50 border border-indigo-500/30 text-xs text-slate-200 mb-3">
            <strong>The Zero Pair Principle:</strong>
            $$(+1) + (-1) = 0$$
            Whenever a green and red token meet, they neutralize each other! You can add or remove any number of Zero Pairs to a collection without changing its net value.
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Green Token (+1)</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Red Token (-1)</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Zero Pair = 0</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Neutral Cancellation</span>
          </div>
        """,
        "sim_id": "sim-zero-pair-tokens",
        "checkpoints": [
            {
                "id": "3.1",
                "question": "A bag contains 7 green tokens and 11 red tokens. After all possible zero pairs cancel out, what is the net value?",
                "options": ["$-4$", "$+4$", "$-18$", "$+18$"],
                "correct": 0,
                "explanation": "7 green pairs with 7 red tokens to form 7 zero pairs ($0$). The remaining $11 - 7 = 4$ red tokens have a value of $-4$!"
            },
            {
                "id": "3.2",
                "question": "If you add 5 zero pairs to a collection with a value of $-3$, what is the new total value?",
                "options": ["$+2$", "$-8$", "$-3$", "$0$"],
                "correct": 2,
                "explanation": "Each zero pair has value $0$. Adding $5 \\times 0 = 0$ leaves the net value unchanged at $-3$!"
            }
        ]
    },
    {
        "slide_num": 4,
        "section": "2.1 Subtraction",
        "badge": "Additive Inverse",
        "title": "Subtraction of Integers & The Additive Inverse",
        "narration": "What does subtraction truly mean? It means taking away tokens. But if you don't have enough to remove, you simply introduce zero pairs! Through this, we discover the golden law: Subtracting an integer is identical to adding its opposite.",
        "theory": r"""
          <p class="mb-3">
            To subtract $b$ from $a$ ($a - b$), we seek to remove $b$ tokens from our pile of $a$ tokens:
          </p>
          <div class="p-3 rounded-lg bg-slate-900/70 border border-slate-700 mb-3 text-xs text-slate-300 space-y-2">
            <p>
              • <strong>Example $(+2) - (+5)$:</strong> We have $2$ green tokens. To remove $5$ green tokens, we introduce $3$ Zero Pairs ($3$ green $+ 3$ red). Now we have $5$ green and $3$ red. Removing $5$ green leaves $3$ red $\implies -3$!
            </p>
            <p>
              • <strong>Example $(+3) - (-4)$:</strong> We have $3$ green tokens. To remove $4$ red tokens, introduce $4$ Zero Pairs. Remove the $4$ red tokens, leaving $3 + 4 = 7$ green tokens $\implies +7$!
            </p>
          </div>
          <div class="p-3 rounded-lg bg-amber-950/40 border border-amber-500/30 text-xs text-amber-200">
            <strong>The Fundamental Theorem of Subtraction:</strong>
            $$a - b = a + (-b) \quad \text{and} \quad a - (-b) = a + b$$
            <em>Subtracting an integer is the exact same operation as adding its Additive Inverse!</em>
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Subtraction = Take Away</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">Additive Inverse</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">$a - (-b) = a + b$</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Zero-Pair Insertion</span>
          </div>
        """,
        "sim_id": "sim-subtraction-inverse",
        "checkpoints": [
            {
                "id": "4.1",
                "question": "Evaluate: $(-8) - (-15)$",
                "options": ["$-23$", "$+7$", "$-7$", "$+23$"],
                "correct": 1,
                "explanation": "Subtracting $-15$ is adding $+15$: $(-8) - (-15) = -8 + 15 = +7$!"
            },
            {
                "id": "4.2",
                "question": "What is the additive inverse of $-42$?",
                "options": ["$-42$", "$+42$", "$0$", "$1/42$"],
                "correct": 1,
                "explanation": "The additive inverse of $-42$ is $+42$ because $(-42) + (+42) = 0$."
            }
        ]
    },
    {
        "slide_num": 5,
        "section": "2.2 Multiplication",
        "badge": "Repeated Addition",
        "title": "Positive × Negative: Adding Groups of Debts",
        "narration": "When a positive integer multiplies a negative integer, multiplication behaves as good old repeated addition! Three times negative four means placing three groups of negative four tokens into our tray, yielding negative twelve.",
        "theory": r"""
          <p class="mb-3">
            In arithmetic, multiplication by a positive whole number represents <strong>repeated addition</strong>:
            $$a \times (-b) = \underbrace{(-b) + (-b) + \dots + (-b)}_{a \text{ times}}$$
          </p>
          <div class="p-3 rounded-lg bg-sky-950/40 border border-sky-500/30 mb-3 text-xs text-slate-300 space-y-1.5">
            <p><strong>Example: $4 \times (-3)$</strong></p>
            <p>• <em>Token Model:</em> Place $4$ groups of $3$ red tokens into a tray $\implies 12$ red tokens $= -12$.</p>
            <p>• <em>Number Line:</em> Starting from $0$, take $4$ consecutive backward leaps of length $3$:
            $$0 \xrightarrow{-3} -3 \xrightarrow{-3} -6 \xrightarrow{-3} -9 \xrightarrow{-3} -12$$
            </p>
          </div>
          <div class="p-3 rounded-lg bg-rose-950/40 border border-rose-500/30 text-xs text-rose-200">
            <strong>Universal Rule 1:</strong>
            $$\text{Positive} \times \text{Negative} = \text{Negative}$$
            $$a \times (-b) = -(a \times b)$$
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Repeated Addition</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Negative Groups</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Backward Jump Vector</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Product Sign (-)</span>
          </div>
        """,
        "sim_id": "sim-pos-times-neg",
        "checkpoints": [
            {
                "id": "5.1",
                "question": "Which repeated addition expression is equivalent to $5 \times (-6)$?",
                "options": ["$(-5) + (-5) + (-5) + (-5) + (-5) + (-5)$", "$(-6) + (-6) + (-6) + (-6) + (-6)$", "$6 + 6 + 6 + 6 + 6$", "$(-6) \\times (-6) \\times (-6) \\times (-6) \\times (-6)$"],
                "correct": 1,
                "explanation": "$5 \\times (-6)$ represents 5 groups of $(-6)$ added together: $(-6) + (-6) + (-6) + (-6) + (-6) = -30$."
            },
            {
                "id": "5.2",
                "question": "Calculate $8 \\times (-7)$:",
                "options": ["$+56$", "$-56$", "$-15$", "$+1$"],
                "correct": 1,
                "explanation": "Positive $\\times$ Negative = Negative. $8 \\times 7 = 56$, so $8 \\times (-7) = -56$."
            }
        ]
    },
    {
        "slide_num": 6,
        "section": "2.2 Multiplication",
        "badge": "Removing Tokens",
        "title": "Negative × Positive: Removing Positive Tokens",
        "narration": "What does a negative multiplier signify? A positive multiplier meant adding groups; so a negative multiplier means removing groups! To remove positive tokens from an empty table, we pull them from a neutral bank of zero pairs, leaving negative tokens behind.",
        "theory": r"""
          <p class="mb-3">
            If multiplying by $+3$ means <em>putting in</em> $3$ groups, then multiplying by $-3$ means <strong>taking away</strong> $3$ groups:
          </p>
          <div class="p-3 rounded-lg bg-slate-900/70 border border-slate-700 mb-3 text-xs text-slate-300 space-y-2">
            <p><strong>Investigating $(-3) \times (+4)$ with Tokens:</strong></p>
            <p>1. Start with a neutral bank containing $12$ Zero Pairs (12 green, 12 red; total net value $= 0$).</p>
            <p>2. The instruction $(-3) \times (+4)$ orders us: <em>\"Remove $3$ groups of $+4$ (i.e. remove 12 green tokens).\"</em></p>
            <p>3. After removing the 12 green tokens, what remains on the table? Exactly <strong>12 red tokens</strong>!</p>
            <p>4. Net value remaining: $-12$. Therefore, $(-3) \times (+4) = -12$.</p>
          </div>
          <div class="p-3 rounded-lg bg-rose-950/40 border border-rose-500/30 text-xs text-rose-200">
            <strong>Universal Rule 2:</strong>
            $$\text{Negative} \times \text{Positive} = \text{Negative}$$
            $$(-a) \times b = -(a \times b)$$
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Negative Multiplier</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Neutral Bank</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">Token Extraction</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Result: Negative</span>
          </div>
        """,
        "sim_id": "sim-neg-times-pos",
        "checkpoints": [
            {
                "id": "6.1",
                "question": "In the token model for $(-4) \\times (+3)$, how many zero pairs must initially be placed in the bank?",
                "options": ["$3$", "$4$", "$7$", "$12$"],
                "correct": 3,
                "explanation": "To remove $4$ groups of $+3$, we need $4 \\times 3 = 12$ positive tokens, so we create $12$ zero pairs!"
            },
            {
                "id": "6.2",
                "question": "What is $(-9) \\times 6$?",
                "options": ["$-54$", "$+54$", "$-15$", "$+3$"],
                "correct": 0,
                "explanation": "Negative $\\times$ Positive = Negative. $9 \\times 6 = 54$, so $(-9) \\times 6 = -54$."
            }
        ]
    },
    {
        "slide_num": 7,
        "section": "2.2 Multiplication",
        "badge": "Double Negative",
        "title": "Negative × Negative: Removing Debts Creates Wealth",
        "narration": "Now behold the grand mystery of mathematics! Why does a negative times a negative equal a positive? In business, removing a debt increases your net worth. In our token bank, taking away red negative tokens leaves bright green positive tokens behind!",
        "theory": r"""
          <p class="mb-3">
            Consider the expression:
            $$(-3) \times (-4)$$
            Using the token interpretation:
          </p>
          <div class="p-3 rounded-lg bg-emerald-950/40 border border-emerald-500/30 mb-3 text-xs text-slate-300 space-y-2">
            <p>1. Start with a neutral bank of $12$ Zero Pairs ($12$ green $+ 12$ red $= 0$).</p>
            <p>2. The multiplier $-3$ commands us to <em>\"Remove $3$ groups of $(-4)$ (i.e. remove 12 red debt tokens).\"</em></p>
            <p>3. When we extract all 12 red tokens from the table, what remains?</p>
            <p class="text-emerald-300 font-bold">4. All 12 green positive tokens shine alone! Net value $= +12$!</p>
          </div>
          <div class="p-3 rounded-lg bg-indigo-950/40 border border-indigo-500/30 text-xs text-indigo-200">
            <strong>The Commercial Analogy of Brahmagupta:</strong>
            <em>\"Removing a debt (taking away negative value) is equivalent to bestowing a fortune!\"</em>
            $$(-a) \times (-b) = +(a \times b)$$
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">(-) × (-) = (+)</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Debt Cancellation</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Net Wealth Increase</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">Positive Remainder</span>
          </div>
        """,
        "sim_id": "sim-neg-times-neg-tokens",
        "checkpoints": [
            {
                "id": "7.1",
                "question": "What happens when you remove 8 red tokens ($-8$) from a neutral bank of 8 zero pairs?",
                "options": ["$8$ red tokens remain ($-8$)", "$8$ green tokens remain ($+8$)", "Zero tokens remain ($0$)", "$16$ red tokens appear"],
                "correct": 1,
                "explanation": "Removing the 8 red tokens leaves the 8 green tokens uncancelled, producing a net value of $+8$!"
            },
            {
                "id": "7.2",
                "question": "Evaluate: $(-7) \\times (-8)$",
                "options": ["$-56$", "$+56$", "$-15$", "$+1$"],
                "correct": 1,
                "explanation": "Negative $\\times$ Negative = Positive! $(-7) \\times (-8) = +56$."
            }
        ]
    },
    {
        "slide_num": 8,
        "section": "2.2 Patterns",
        "badge": "Pattern Invariance",
        "title": "Patterns in Multiplication: Unit Decrease Sequences",
        "narration": "Mathematics craves harmony and continuity! By starting with known positive multiplication and stepping our multiplier down by one at each stage, an unbroken arithmetic sequence unfolds, compelling negative times negative to be positive.",
        "theory": r"""
          <p class="mb-3">
            Observe what happens as the multiplier decreases by $1$ unit at each step while multiplying by $-3$:
          </p>
          <div class="p-3 rounded-lg bg-slate-900/80 border border-slate-700 font-mono text-xs text-slate-200 mb-3 space-y-1">
            <div class="flex justify-between"><span>$3 \\times (-3) = -9$</span> <span class="text-sky-400">(adds $+3$)</span></div>
            <div class="flex justify-between"><span>$2 \\times (-3) = -6$</span> <span class="text-sky-400">(adds $+3$)</span></div>
            <div class="flex justify-between"><span>$1 \\times (-3) = -3$</span> <span class="text-sky-400">(adds $+3$)</span></div>
            <div class="flex justify-between font-bold text-amber-300"><span>$0 \\times (-3) = 0$</span> <span class="text-sky-400">(adds $+3$)</span></div>
            <div class="flex justify-between text-emerald-300 font-bold"><span>$(-1) \\times (-3) = +3$</span> <span class="text-sky-400">(pattern MUST add $+3$)</span></div>
            <div class="flex justify-between text-emerald-300 font-bold"><span>$(-2) \\times (-3) = +6$</span> <span class="text-sky-400">(adds $+3$)</span></div>
            <div class="flex justify-between text-emerald-300 font-bold"><span>$(-3) \\times (-3) = +9$</span> <span class="text-sky-400">(adds $+3$)</span></div>
          </div>
          <p class="text-xs text-slate-300">
            To maintain the constant difference of $+3$ across the boundary of zero, the product of two negative numbers <strong>must</strong> be positive!
          </p>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Number Sequence</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Unit Decrement</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Constant Step Difference</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">Structural Consistency</span>
          </div>
        """,
        "sim_id": "sim-multiplication-patterns",
        "checkpoints": [
            {
                "id": "8.1",
                "question": "In the sequence $3 \\times (-5) = -15, 2 \\times (-5) = -10, 1 \\times (-5) = -5$, each step increases by:",
                "options": ["$-5$", "$+5$", "$-10$", "$+1$"],
                "correct": 1,
                "explanation": "$-10 - (-15) = +5$, and $-5 - (-10) = +5$. The product increases by $+5$ at every step!"
            },
            {
                "id": "8.2",
                "question": "Following the pattern above, what comes immediately after $0 \\times (-5) = 0$?",
                "options": ["$(-1) \\times (-5) = -5$", "$(-1) \\times (-5) = 0$", "$(-1) \\times (-5) = +5$", "$(-1) \\times (-5) = +10$"],
                "correct": 2,
                "explanation": "Continuing the pattern: $0 + 5 = +5$. Therefore, $(-1) \\times (-5) = +5$!"
            }
        ]
    },
    {
        "slide_num": 9,
        "section": "2.2 Sign Laws",
        "badge": "Rules & Special Multipliers",
        "title": "The Master Rules of Signs & Special Multipliers",
        "narration": "Let us codify the Four Master Laws of Sign Multiplication! Notice the elegant symmetry: like signs multiply to positive, while unlike signs multiply to negative. Pay close attention to one and negative one, which act as mirror inverters.",
        "theory": r"""
          <p class="mb-3">
            The fundamental rules for multiplying two integers:
          </p>
          <div class="grid grid-cols-2 gap-2 mb-3 text-xs">
            <div class="p-2.5 rounded bg-emerald-950/40 border border-emerald-500/30">
              <span class="text-emerald-400 font-bold block mb-1">✓ Like Signs $\implies$ Positive</span>
              $$(+) \times (+) = (+)$$
              $$(-) \times (-) = (+)$$
            </div>
            <div class="p-2.5 rounded bg-rose-950/40 border border-rose-500/30">
              <span class="text-rose-400 font-bold block mb-1">✗ Unlike Signs $\implies$ Negative</span>
              $$(+) \times (-) = (-)$$
              $$(-) \times (+) = (-)$$
            </div>
          </div>
          <div class="p-3 rounded-lg bg-indigo-950/50 border border-indigo-500/30 text-xs text-slate-300 space-y-1.5 mb-2">
            <p><strong>Special Multipliers:</strong></p>
            <p>• <strong>Multiplicative Identity ($1$):</strong> $a \times 1 = 1 \times a = a$. (Preserves value and sign).</p>
            <p>• <strong>The Inverter ($-1$):</strong> $a \times (-1) = -a$. Multiplying any integer by $-1$ flips its sign to produce its <em>Additive Inverse</em>!</p>
            <p>• <strong>Multiplication by Zero ($0$):</strong> $a \times 0 = 0 \times a = 0$.</p>
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Like Signs $\implies$ (+)</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Unlike Signs $\implies$ (-)</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Identity ($1$)</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">Inverter ($-1$)</span>
          </div>
        """,
        "sim_id": "sim-sign-rules-matrix",
        "checkpoints": [
            {
                "id": "9.1",
                "question": "What is the product of $(-1) \\times (-1) \\times (-1)$?",
                "options": ["$+1$", "$-1$", "$0$", "$-3$"],
                "correct": 1,
                "explanation": "$(-1) \\times (-1) = +1$. Then $(+1) \\times (-1) = -1$."
            },
            {
                "id": "9.2",
                "question": "If an unknown integer $x$ satisfies $x \\times (-1) = 35$, what is $x$?",
                "options": ["$35$", "$-35$", "$1/35$", "$0$"],
                "correct": 1,
                "explanation": "Multiplying by $-1$ flips the sign. Since $-x = 35$, $x = -35$!"
            }
        ]
    },
    {
        "slide_num": 10,
        "section": "2.2 Heritage",
        "badge": "Brāhmasphuṭasiddhānta",
        "title": "Brahmagupta's Heritage: Fortunes (Dhana) & Debts (Ṛṇa)",
        "narration": "In the year 628 CE, right here in ancient India, in my treatise the Brāhmasphuṭasiddhānta, I codified the first formal laws of zero, positive fortunes, and negative debts. Let us read the timeless shlokas that enlightened global mathematics.",
        "theory": r"""
          <p class="mb-3">
            In Chapter 18 of the <strong>Brāhmasphuṭasiddhānta</strong> (628 CE), <strong>Acharya Brahmagupta</strong> established the arithmetic foundations of signed numbers:
          </p>
          <div class="p-3 rounded-lg bg-amber-950/40 border border-amber-500/30 mb-3 text-xs text-amber-200 space-y-2">
            <p class="font-serif italic text-sm text-amber-300">
              \"ऋणयोर्धनयोर्घातो धनं भवति निश्चितम्।<br>
              ऋणधनयोर्घातोऽवश्यमृणं स्यात् परस्परम्॥\"
            </p>
            <p><strong>Translation & Canonical Rules:</strong></p>
            <p>1. <em>Dhana</em> $\times$ <em>Dhana</em> = <em>Dhana</em>: The product of two fortunes is a fortune.</p>
            <p>2. <em>Ṛṇa</em> $\times$ <em>Ṛṇa</em> = <em>Dhana</em>: The product of two debts is a fortune!</p>
            <p>3. <em>Dhana</em> $\times$ <em>Ṛṇa</em> = <em>Ṛṇa</em>: The product of a fortune and a debt is a debt.</p>
            <p>4. <em>Kha</em> (Zero) multiplied by debt or fortune is zero.</p>
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Brahmagupta (628 CE)</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Dhana (Fortune)</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Ṛṇa (Debt)</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Śūnya / Kha (Zero)</span>
          </div>
        """,
        "sim_id": "sim-brahmagupta-scroll",
        "checkpoints": [
            {
                "id": "10.1",
                "question": "According to Brahmagupta's Sanskrit terminology, what is the product of two debts (Ṛṇa)?",
                "options": ["A debt (Ṛṇa)", "A fortune (Dhana)", "Zero (Kha)", "Undefined"],
                "correct": 1,
                "explanation": "Brahmagupta explicitly stated: 'The product of two debts is a fortune' (ऋणयोर्घातो धनं)!"
            },
            {
                "id": "10.2",
                "question": "What is the ancient Sanskrit mathematical term used by Brahmagupta for zero?",
                "options": ["Dhana", "Ṛṇa", "Kha or Śūnya", "Viparīta"],
                "correct": 2,
                "explanation": "Zero was termed 'Kha' (void/sky) or 'Śūnya' (empty) in ancient Indian mathematics."
            }
        ]
    },
    {
        "slide_num": 11,
        "section": "2.2 Applications",
        "badge": "Everyday Integers",
        "title": "Real-Life Applications: Elevators, Exams & Temperatures",
        "narration": "Integers are not mere abstract symbols; they govern our physical world! From mining elevators descending hundreds of meters underground, to penalty scoring in entrance exams and freezing sub-zero weather, signed arithmetic solves real-life challenges.",
        "theory": r"""
          <p class="mb-3">
            Real-world phenomena requiring signed integer arithmetic:
          </p>
          <div class="space-y-2 mb-3 text-xs">
            <div class="p-2.5 rounded bg-slate-900/60 border border-slate-700">
              <strong class="text-amber-300 block mb-1">🏗️ Mine Shaft Elevator:</strong>
              An elevator starts $10\\text{ m}$ above ground level ($+10$) and descends at $6\\text{ m/min}$ (velocity $=-6\\text{ m/min}$). Where is it after $35\\text{ minutes}$?
              $$\\text{Position} = 10 + [35 \\times (-6)] = 10 - 210 = -200\\text{ m (i.e. } 200\\text{ m underground)}$$
            </div>
            <div class="p-2.5 rounded bg-slate-900/60 border border-slate-700">
              <strong class="text-emerald-300 block mb-1">📝 Competitive Scoring System:</strong>
              $+4$ marks for every correct answer, $-2$ marks for every incorrect answer. If Rohan gets $10$ correct and $5$ incorrect:
              $$\\text{Score} = (10 \\times 4) + [5 \\times (-2)] = 40 - 10 = 30\\text{ marks}$$
            </div>
            <div class="p-2.5 rounded bg-slate-900/60 border border-slate-700">
              <strong class="text-sky-300 block mb-1">❄️ Temperature Drops:</strong>
              Freezer room temperature drops by $3^\\circ\\text{C}$ per hour from $12^\\circ\\text{C}$. In $6\\text{ hours}$:
              $$\\text{Temp} = 12 + [6 \\times (-3)] = 12 - 18 = -6^\\circ\\text{C}$$
            </div>
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Mine Shaft Descent</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Negative Marking</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Sub-Zero Temperature</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Profit and Loss</span>
          </div>
        """,
        "sim_id": "sim-real-world-integers",
        "checkpoints": [
            {
                "id": "11.1",
                "question": "An elevator descends at $5\\text{ m/min}$. Starting from $15\\text{ m}$ above ground, how long will it take to reach $-350\\text{ m}$?",
                "options": ["$67\\text{ min}$", "$70\\text{ min}$", "$73\\text{ min}$", "$80\\text{ min}$"],
                "correct": 2,
                "explanation": "Total distance to descend $= 15 - (-350) = 365\\text{ m}$. Time taken $= 365 \\div 5 = 73\\text{ minutes}$!"
            },
            {
                "id": "11.2",
                "question": "In a quiz, $+5$ is awarded for correct answers and $-3$ for wrong ones. Priya answered 6 correct and 4 wrong. Her score is:",
                "options": ["$18$", "$22$", "$30$", "$42$"],
                "correct": 0,
                "explanation": "Score $= (6 \\times 5) + (4 \\times -3) = 30 - 12 = 18$."
            }
        ]
    },
    {
        "slide_num": 12,
        "section": "2.2 Properties",
        "badge": "Commutative & Associative",
        "title": "Properties: Commutative & Associative Laws",
        "narration": "Integers possess wonderful algebraic symmetries! The Commutative Property allows you to swap factor order without penalty, while the Associative Property grants complete freedom in grouping factors. Let us verify these universal truths.",
        "theory": r"""
          <p class="mb-3">
            Two foundational structural laws for integer multiplication:
          </p>
          <div class="space-y-2.5 mb-3 text-xs">
            <div class="p-3 rounded-lg bg-indigo-950/40 border border-indigo-500/30">
              <strong class="text-indigo-300 block mb-1">1. Commutative Property:</strong>
              $$a \\times b = b \\times a \\quad \\text{for any integers } a, b$$
              <em>Example:</em> $(-6) \\times 4 = -24$ and $4 \\times (-6) = -24$. Swapping order never changes the product!
            </div>
            <div class="p-3 rounded-lg bg-sky-950/40 border border-sky-500/30">
              <strong class="text-sky-300 block mb-1">2. Associative Property:</strong>
              $$(a \\times b) \\times c = a \\times (b \\times c) \\quad \\text{for any integers } a, b, c$$
              <em>Example:</em> Evaluate $[(-3) \\times 4] \\times (-5)$:
              $$[(-3) \\times 4] \\times (-5) = (-12) \\times (-5) = +60$$
              $$(-3) \\times [4 \\times (-5)] = (-3) \\times (-20) = +60$$
              Grouping brackets can be rearranged freely!
            </div>
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Commutative ($a \\times b = b \\times a$)</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Associative ($(ab)c = a(bc)$)</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Order Independence</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Grouping Invariance</span>
          </div>
        """,
        "sim_id": "sim-comm-assoc-engine",
        "checkpoints": [
            {
                "id": "12.1",
                "question": "Which property is demonstrated by $(-7) \\times [(-2) \\times 5] = [(-7) \\times (-2)] \\times 5$?",
                "options": ["Commutative Property", "Associative Property", "Distributive Property", "Closure Property"],
                "correct": 1,
                "explanation": "Rearranging the grouping parentheses among three multiplying factors demonstrates the Associative Property!"
            },
            {
                "id": "12.2",
                "question": "Evaluate mentally by clever grouping: $25 \\times (-17) \\times (-4)$",
                "options": ["$-1700$", "$+1700$", "$-170$", "$+170$"],
                "correct": 1,
                "explanation": "Group $25 \\times (-4) = -100$. Then $(-100) \\times (-17) = +1700$!"
            }
        ]
    },
    {
        "slide_num": 13,
        "section": "2.2 Properties",
        "badge": "Distributive Law",
        "title": "The Distributive Property: Multiplication over Addition",
        "narration": "The Distributive Property is the undisputed workhorse of arithmetic and algebra! It connects multiplication with addition, allowing you to split difficult products into simple mental chunks or factor out common terms.",
        "theory": r"""
          <p class="mb-3">
            The <strong>Distributive Property of Multiplication over Addition</strong> states:
            $$a \\times (b + c) = (a \\times b) + (a \\times c)$$
            $$a \\times (b - c) = (a \\times b) - (a \\times c)$$
          </p>
          <div class="p-3 rounded-lg bg-emerald-950/40 border border-emerald-500/30 mb-3 text-xs text-slate-300 space-y-2">
            <p><strong class="text-emerald-300">💡 Superpower 1: Mental Math Shortcut</strong></p>
            <p>Compute $(-25) \\times 98$ without long multiplication:</p>
            <p>Write $98$ as $(100 - 2)$:</p>
            $$(-25) \\times (100 - 2) = [(-25) \\times 100] - [(-25) \\times 2] = -2500 - (-50) = -2500 + 50 = -2450!$$
            <p><strong class="text-emerald-300">💡 Superpower 2: Common Factor Extraction</strong></p>
            $$(-48) \\times 65 + (-48) \\times 35 = (-48) \\times (65 + 35) = (-48) \\times 100 = -4800!$$
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Distributive Law</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">$a(b+c) = ab + ac$</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Factor Extraction</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">Mental Decomposition</span>
          </div>
        """,
        "sim_id": "sim-distributive-grid",
        "checkpoints": [
            {
                "id": "13.1",
                "question": "Simplify: $73 \\times (-18) + 73 \\times (-82)$",
                "options": ["$-7300$", "$+7300$", "$-730$", "$-1460$"],
                "correct": 0,
                "explanation": "Extract common factor $73$: $73 \\times [(-18) + (-82)] = 73 \\times (-100) = -7300$!"
            },
            {
                "id": "13.2",
                "question": "Using the distributive property, $(-35) \\times 102$ equals:",
                "options": ["$(-35 \\times 100) + (-35 \\times 2)$", "$(-35 \\times 100) \\times (-35 \\times 2)$", "$(-35 \\times 100) - 2$", "$3500 + 70$"],
                "correct": 0,
                "explanation": "$102 = 100 + 2$. Distributing gives $(-35 \\times 100) + (-35 \\times 2) = -3500 - 70 = -3570$."
            }
        ]
    },
    {
        "slide_num": 14,
        "section": "2.2 Multiple Integers",
        "badge": "Sign Parity Rule",
        "title": "Products of Multiple Integers: The Parity of Negatives",
        "narration": "What happens when you multiply three, four, or ten signed numbers together? You don't need to guess! Simply count the negative factors. Since every pair of negatives cancels into a positive, the parity of negative signs determines everything.",
        "theory": r"""
          <p class="mb-3">
            When multiplying three or more non-zero integers:
          </p>
          <div class="p-3 rounded-lg bg-slate-900/70 border border-slate-700 mb-3 text-xs text-slate-300 space-y-2">
            <p>Every pair of negative factors multiplies to positive: $(-) \\times (-) = (+)$.</p>
            <div class="grid grid-cols-2 gap-2 mt-2">
              <div class="p-2 rounded bg-emerald-950/40 border border-emerald-500/30">
                <span class="font-bold text-emerald-300 block mb-1">EVEN Count of Negatives:</span>
                Product is <strong>POSITIVE (+)</strong><br>
                <em>Example:</em> $(-2) \\times (-3) \\times (-4) \\times (-5) = +120$ ($4$ negatives $\implies +$).
              </div>
              <div class="p-2 rounded bg-rose-950/40 border border-rose-500/30">
                <span class="font-bold text-rose-300 block mb-1">ODD Count of Negatives:</span>
                Product is <strong>NEGATIVE (-)</strong><br>
                <em>Example:</em> $(-2) \\times (-3) \\times (-4) = -24$ ($3$ negatives $\implies -$).
              </div>
            </div>
          </div>
          <div class="p-3 rounded-lg bg-sky-950/40 border border-sky-500/30 text-xs text-sky-200">
            <strong>Rule of Thumb:</strong> Positive factors do not affect the sign of the product! The sign is governed purely by whether the tally of negative signs is Even ($+$) or Odd ($-$).
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Sign Parity Rule</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Even Count $\implies (+)$</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Odd Count $\implies (-)$</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">Pairwise Neutralization</span>
          </div>
        """,
        "sim_id": "sim-multiple-integers-parity",
        "checkpoints": [
            {
                "id": "14.1",
                "question": "What is the sign of the product if you multiply $18$ negative integers and $5$ positive integers?",
                "options": ["Positive (+)", "Negative (-)", "Zero", "Cannot be determined"],
                "correct": 0,
                "explanation": "There are 18 negative integers. Since 18 is an EVEN number, all negative signs pair up to positive. The product is Positive (+)!"
            },
            {
                "id": "14.2",
                "question": "Evaluate: $(-1)^{99}$",
                "options": ["$+1$", "$-1$", "$+99$", "$-99$"],
                "correct": 1,
                "explanation": "$(-1)^{99}$ is a product of 99 negative factors. 99 is ODD, so the answer is $-1$!"
            }
        ]
    },
    {
        "slide_num": 15,
        "section": "2.3 Division",
        "badge": "Missing Factor",
        "title": "Division of Integers as Missing-Factor Multiplication",
        "narration": "Division is not a separate mysterious realm—it is simply multiplication running in reverse! When we ask what negative twelve divided by three is, we are asking: what number multiplied by three equals negative twelve?",
        "theory": r"""
          <p class="mb-3">
            <strong>Division is the inverse operation of multiplication.</strong>
            For any integers $a$ and $b$ ($b \\neq 0$):
            $$a \\div b = ? \\iff b \\times ? = a$$
          </p>
          <div class="p-3 rounded-lg bg-slate-900/70 border border-slate-700 mb-3 text-xs text-slate-300 space-y-2">
            <p>• <strong>Case 1: $(-20) \\div 4 = ?$</strong> $\implies 4 \\times ? = -20$. We know $4 \\times (-5) = -20$, so $? = -5$.</p>
            <p>• <strong>Case 2: $(-20) \\div (-5) = ?$</strong> $\implies (-5) \\times ? = -20$. We know $(-5) \\times (+4) = -20$, so $? = +4$.</p>
            <p>• <strong>Case 3: $20 \\div (-4) = ?$</strong> $\implies (-4) \\times ? = 20$. We know $(-4) \\times (-5) = 20$, so $? = -5$.</p>
          </div>
          <div class="p-3 rounded-lg bg-rose-950/40 border border-rose-500/30 text-xs text-rose-200">
            <strong>⚠️ Division by Zero is Undefined:</strong>
            $a \\div 0 = ?$ would mean $0 \\times ? = a$. If $a \\neq 0$, no number exists (since $0 \\times \\text{anything} = 0$). Hence, <strong>division by zero is strictly forbidden / undefined!</strong><br>
            However, $0 \\div a = 0$ (for $a \\neq 0$) because $a \\times 0 = 0$.
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Inverse Operation</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Missing Factor ($b \\times ? = a$)</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">$a \\div 0$ Undefined</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">$0 \\div a = 0$</span>
          </div>
        """,
        "sim_id": "sim-division-missing-factor",
        "checkpoints": [
            {
                "id": "15.1",
                "question": "Solve the missing factor problem: $(-7) \\times ? = 56$",
                "options": ["$+8$", "$-8$", "$+7$", "$-7$"],
                "correct": 1,
                "explanation": "Since $(-7) \\times (-8) = +56$, the missing factor is $-8$. Thus $56 \\div (-7) = -8$!"
            },
            {
                "id": "15.2",
                "question": "What is the value of $(-45) \\div 0$?",
                "options": ["$0$", "$-45$", "$+1$", "Not Defined"],
                "correct": 3,
                "explanation": "Division by zero is mathematically not defined!"
            }
        ]
    },
    {
        "slide_num": 16,
        "section": "2.3 Division Rules",
        "badge": "Quotient Laws",
        "title": "Rules of Signs for Division & Properties",
        "narration": "Division inherits the exact same sign laws as multiplication! Dividing like signs yields a positive quotient; dividing unlike signs yields a negative quotient. But beware: division does not obey the commutative or associative laws!",
        "theory": r"""
          <p class="mb-3">
            Because division is the inverse of multiplication, its sign rules are identical:
          </p>
          <div class="grid grid-cols-2 gap-2 mb-3 text-xs">
            <div class="p-2.5 rounded bg-emerald-950/40 border border-emerald-500/30">
              <span class="text-emerald-400 font-bold block mb-1">Like Signs $\implies (+)$</span>
              $$(+) \\div (+) = (+)$$
              $$(-) \\div (-) = (+)$$
            </div>
            <div class="p-2.5 rounded bg-rose-950/40 border border-rose-500/30">
              <span class="text-rose-400 font-bold block mb-1">Unlike Signs $\implies (-)$</span>
              $$(+) \\div (-) = (-)$$
              $$(-) \\div (+) = (-)$$
            </div>
          </div>
          <div class="p-3 rounded-lg bg-amber-950/40 border border-amber-500/30 mb-2 text-xs text-amber-200 space-y-1.5">
            <p><strong>Crucial Non-Properties of Division:</strong></p>
            <p>• <strong>NOT Commutative:</strong> $a \\div b \\neq b \\div a$. Example: $(-8) \\div 2 = -4$, but $2 \\div (-8) = -1/4$.</p>
            <p>• <strong>NOT Associative:</strong> $(a \\div b) \\div c \\neq a \\div (b \\div c)$. Example: $[(-16) \\div 4] \\div (-2) = (-4) \\div (-2) = +2$, whereas $(-16) \\div [4 \\div (-2)] = (-16) \\div (-2) = +8$.</p>
            <p>• <strong>Fractional Equivalence:</strong> $\\frac{-a}{b} = \\frac{a}{-b} = -\\left(\\frac{a}{b}\\right)$.</p>
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Quotient Signs</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Non-Commutative</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Non-Associative</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Fraction Sign Position</span>
          </div>
        """,
        "sim_id": "sim-division-rules-lab",
        "checkpoints": [
            {
                "id": "16.1",
                "question": "Evaluate: $(-72) \\div (-9)$",
                "options": ["$-8$", "$+8$", "$-9$", "$+9$"],
                "correct": 1,
                "explanation": "Negative $\\div$ Negative = Positive! $72 \\div 9 = 8$, so $(-72) \\div (-9) = +8$."
            },
            {
                "id": "16.2",
                "question": "Is $(-20) \\div 5$ equal to $5 \\div (-20)$?",
                "options": ["Yes, because division is commutative", "No, division of integers is not commutative", "Yes, both equal $-4$", "Yes, both equal $-0.25$"],
                "correct": 1,
                "explanation": "$(-20) \\div 5 = -4$, while $5 \\div (-20) = -1/4 = -0.25$. Division is NOT commutative!"
            }
        ]
    },
    {
        "slide_num": 17,
        "section": "2.4 Mastery Quiz",
        "badge": "Quiz Challenge I",
        "title": "Mastery Challenge I: Foundations & Token Multiplication",
        "narration": "Welcome to Mastery Challenge Round One! Test your firm grasp of number puzzles, zero pairs, additive inverses, and basic integer multiplication.",
        "quiz_range": [1, 10]
    },
    {
        "slide_num": 18,
        "section": "2.4 Mastery Quiz",
        "badge": "Quiz Challenge II",
        "title": "Mastery Challenge II: Patterns, Sign Laws & Brahmagupta",
        "narration": "Round Two will test your mastery of multiplication patterns, the four sign laws, Brahmagupta's ancient heritage, and real-life elevator and scoring word problems.",
        "quiz_range": [11, 20]
    },
    {
        "slide_num": 19,
        "section": "2.4 Mastery Quiz",
        "badge": "Quiz Challenge III",
        "title": "Mastery Challenge III: Algebraic Properties & Multiple Factors",
        "narration": "Round Three challenges your prowess in the Commutative, Associative, and Distributive properties, plus sign determination for chains of multiple signed numbers.",
        "quiz_range": [21, 30]
    },
    {
        "slide_num": 20,
        "section": "2.4 Mastery Quiz",
        "badge": "Quiz Challenge IV",
        "title": "Mastery Challenge IV: Division of Integers & Grand Finale",
        "narration": "Congratulations on reaching the final round! Master division of integers, inverse operations, missing factors, zero division constraints, and multi-step mixed operations.",
        "quiz_range": [31, 40]
    }
]

# 40 Rigorous Quiz Questions with Detailed Solutions
QUIZ_QUESTIONS = [
    # Questions 1 to 10 (Slide 17)
    {
        "id": 1,
        "question": "What is the sum of an integer and its additive inverse?",
        "options": ["$1$", "$0$", "$-1$", "The square of the integer"],
        "correct": 1,
        "solution": "By definition, the additive inverse of $a$ is $-a$, and their sum is always zero: $a + (-a) = 0$."
    },
    {
        "id": 2,
        "question": "Which pair of integers has a sum of $-10$ and a difference of $6$?",
        "options": ["$-2$ and $-8$", "$-5$ and $-5$", "$-2$ and $-12$", "$-8$ and $-2$"],
        "correct": 0,
        "solution": "Check: $(-2) + (-8) = -10$, and $(-2) - (-8) = -2 + 8 = 6$. Both conditions are satisfied!"
    },
    {
        "id": 3,
        "question": "On a number line, starting at $+5$ and moving $12$ units to the left brings you to:",
        "options": ["$+17$", "$-7$", "$-17$", "$-5$"],
        "correct": 1,
        "solution": "Moving left corresponds to subtraction: $5 - 12 = -7$."
    },
    {
        "id": 4,
        "question": "In the token model, 15 green tokens and 22 red tokens are combined. What is the net value?",
        "options": ["$+7$", "$-7$", "$+37$", "$-37$"],
        "correct": 1,
        "solution": "15 green tokens pair with 15 red tokens to form 15 zero pairs ($0$). The remaining $22 - 15 = 7$ red tokens equal $-7$."
    },
    {
        "id": 5,
        "question": "Evaluate: $(-14) - (-20)$",
        "options": ["$-34$", "$+6$", "$-6$", "$+34$"],
        "correct": 1,
        "solution": "Subtracting a negative is adding its opposite: $(-14) - (-20) = -14 + 20 = +6$."
    },
    {
        "id": 6,
        "question": "Which multiplication expression represents $(-4) + (-4) + (-4) + (-4) + (-4)$?",
        "options": ["$4 \\times (-5)$", "$5 \\times (-4)$", "$(-4) \\times (-4)$", "$(-5) \\times (-4)$"],
        "correct": 1,
        "solution": "There are 5 groups of $(-4)$ being added, which is written as $5 \\times (-4)$."
    },
    {
        "id": 7,
        "question": "Compute: $6 \\times (-9)$",
        "options": ["$+54$", "$-54$", "$-15$", "$+3$"],
        "correct": 1,
        "solution": "Positive $\\times$ Negative = Negative. $6 \\times 9 = 54$, so $6 \\times (-9) = -54$."
    },
    {
        "id": 8,
        "question": "What is $(-12) \\times 0$?",
        "options": ["$-12$", "$+12$", "$0$", "Undefined"],
        "correct": 2,
        "solution": "Any integer multiplied by zero equals zero: $a \\times 0 = 0$."
    },
    {
        "id": 9,
        "question": "In the token model for $(-2) \\times (+5)$, what action is performed on the neutral bank?",
        "options": ["Adding 2 groups of $+5$", "Removing 2 groups of $+5$", "Adding 5 groups of $-2$", "Removing 5 groups of $-2$"],
        "correct": 1,
        "solution": "A negative multiplier ($-2$) indicates removing groups. So we remove $2$ groups of $+5$ from the neutral bank of zero pairs."
    },
    {
        "id": 10,
        "question": "Which of the following is equivalent to $a - (-b)$?",
        "options": ["$a - b$", "$a + b$", "$-(a + b)$", "$-a - b$"],
        "correct": 1,
        "solution": "Subtracting the negative of $b$ is equivalent to adding positive $b$: $a - (-b) = a + b$."
    },

    # Questions 11 to 20 (Slide 18)
    {
        "id": 11,
        "question": "Evaluate: $(-8) \\times (-11)$",
        "options": ["$-88$", "$+88$", "$-19$", "$+19$"],
        "correct": 1,
        "solution": "Negative $\\times$ Negative = Positive! $8 \\times 11 = 88$, so $(-8) \\times (-11) = +88$."
    },
    {
        "id": 12,
        "question": "In the arithmetic pattern $2 \\times (-4) = -8, 1 \\times (-4) = -4, 0 \\times (-4) = 0$, what is the next line?",
        "options": ["$(-1) \\times (-4) = -4$", "$(-1) \\times (-4) = +4$", "$(-1) \\times (-4) = 0$", "$(-1) \\times (-4) = +8$"],
        "correct": 1,
        "solution": "The sequence increases by $+4$ at each step. After $0$, the next term is $0 + 4 = +4$, so $(-1) \\times (-4) = +4$."
    },
    {
        "id": 13,
        "question": "What is the product when $-1$ is multiplied by $-1$?",
        "options": ["$-1$", "$+1$", "$0$", "$-2$"],
        "correct": 1,
        "solution": "Like signs multiply to positive: $(-1) \\times (-1) = +1$."
    },
    {
        "id": 14,
        "question": "In ancient Indian mathematics, Acharya Brahmagupta called negative quantities:",
        "options": ["Dhana", "Ṛṇa", "Kha", "Rūpa"],
        "correct": 1,
        "solution": "Brahmagupta termed debts or negative quantities 'Ṛṇa' (and positive wealth 'Dhana')."
    },
    {
        "id": 15,
        "question": "According to Brahmagupta's Brāhmasphuṭasiddhānta, the product of a fortune (Dhana) and a debt (Ṛṇa) is:",
        "options": ["A fortune (Dhana)", "A debt (Ṛṇa)", "Zero (Kha)", "Undefined"],
        "correct": 1,
        "solution": "Brahmagupta stated that positive times negative is always negative: Fortune $\\times$ Debt = Debt (Ṛṇa)."
    },
    {
        "id": 16,
        "question": "An elevator starts at ground level ($0\\text{ m}$) and descends into a mine at a rate of $4\\text{ m/min}$. Where will it be after $25\\text{ minutes}$?",
        "options": ["$+100\\text{ m}$", "$-100\\text{ m}$", "$-29\\text{ m}$", "$-120\\text{ m}$"],
        "correct": 1,
        "solution": "Descent is represented by negative velocity: Position $= 25 \\times (-4) = -100\\text{ m}$ ($100\\text{ m}$ below ground)."
    },
    {
        "id": 17,
        "question": "In a test, $+3$ marks are given for every correct answer and $-1$ for every incorrect answer. If a student gets 14 correct and 6 incorrect, what is the final score?",
        "options": ["$42$", "$36$", "$48$", "$30$"],
        "correct": 1,
        "solution": "Score $= (14 \\times 3) + [6 \\times (-1)] = 42 - 6 = 36$ marks."
    },
    {
        "id": 18,
        "question": "The temperature of a city at 6 PM was $5^\\circ\\text{C}$. It dropped by $2^\\circ\\text{C}$ every hour for the next 7 hours. What was the temperature at 1 AM?",
        "options": ["$-9^\\circ\\text{C}$", "$-7^\\circ\\text{C}$", "$+19^\\circ\\text{C}$", "$-14^\\circ\\text{C}$"],
        "correct": 0,
        "solution": "Total temperature change $= 7 \\times (-2) = -14^\\circ\\text{C}$. New temperature $= 5 + (-14) = 5 - 14 = -9^\\circ\\text{C}$."
    },
    {
        "id": 19,
        "question": "Which integer multiplied by $-1$ gives $73$?",
        "options": ["$73$", "$-73$", "$0$", "$1/73$"],
        "correct": 1,
        "solution": "Let the integer be $x$. $x \\times (-1) = 73 \\implies -x = 73 \\implies x = -73$."
    },
    {
        "id": 20,
        "question": "A shopkeeper earns ₹1 profit on each pen sold and incurs a loss of 40 paise (₹0.40) on each pencil. In a day, she sells 70 pens and 100 pencils. What is her net profit or loss?",
        "options": ["₹30 profit", "₹30 loss", "₹110 profit", "No profit no loss"],
        "correct": 0,
        "solution": "Profit on pens $= 70 \\times (+1) = +₹70$. Loss on pencils $= 100 \\times (-0.40) = -₹40$. Net profit $= 70 - 40 = +₹30$ profit."
    },

    # Questions 21 to 30 (Slide 19)
    {
        "id": 21,
        "question": "Which property states that $a \\times b = b \\times a$ for all integers?",
        "options": ["Associative Property", "Commutative Property", "Distributive Property", "Identity Property"],
        "correct": 1,
        "solution": "The Commutative Property of multiplication states that changing the order of factors does not alter the product."
    },
    {
        "id": 22,
        "question": "Verify: $[(-5) \\times (-2)] \\times 3 = (-5) \\times [(-2) \\times 3]$. What property is this?",
        "options": ["Commutative Property", "Associative Property", "Distributive Property", "Closure Property"],
        "correct": 1,
        "solution": "This is the Associative Property of multiplication: $(a \\times b) \\times c = a \\times (b \\times c)$."
    },
    {
        "id": 23,
        "question": "Evaluate using the distributive property: $(-26) \\times 72 + (-26) \\times 28$",
        "options": ["$-2600$", "$+2600$", "$-260$", "$+260$"],
        "correct": 0,
        "solution": "Take out common factor $(-26)$: $(-26) \\times (72 + 28) = (-26) \\times 100 = -2600$."
    },
    {
        "id": 24,
        "question": "Evaluate: $15 \\times (-99)$ using the distributive property:",
        "options": ["$15 \\times (-100 + 1) = -1500 + 15 = -1485$", "$15 \\times (-100 - 1) = -1515$", "$15 \\times 100 - 99 = 1401$", "$-1350$"],
        "correct": 0,
        "solution": "Write $-99$ as $(-100 + 1)$: $15 \\times (-100 + 1) = (15 \\times -100) + (15 \\times 1) = -1500 + 15 = -1485$."
    },
    {
        "id": 25,
        "question": "What is the sign of the product of $7$ negative integers and $4$ positive integers?",
        "options": ["Positive (+)", "Negative (-)", "Zero", "Depends on values"],
        "correct": 1,
        "solution": "Count the negative factors: there are 7. Since 7 is ODD, the product is Negative (-)."
    },
    {
        "id": 26,
        "question": "What is the sign of the product of $10$ negative integers?",
        "options": ["Positive (+)", "Negative (-)", "Zero", "Undefined"],
        "correct": 0,
        "solution": "There are 10 negative factors. Since 10 is an EVEN number, the negative signs all pair up into positive, yielding Positive (+)."
    },
    {
        "id": 27,
        "question": "Calculate: $(-3) \\times (-4) \\times (-5)$",
        "options": ["$+60$", "$-60$", "$+12$", "$-20$"],
        "correct": 1,
        "solution": "$(-3) \\times (-4) = +12$. Then $(+12) \\times (-5) = -60$ (3 negative factors $\implies$ negative product)."
    },
    {
        "id": 28,
        "question": "Calculate: $(-2) \\times (-3) \\times (-4) \\times (-5)$",
        "options": ["$+120$", "$-120$", "$+24$", "$-24$"],
        "correct": 0,
        "solution": "There are 4 negative factors (even count $\implies$ positive). Product $= 2 \\times 3 \\times 4 \\times 5 = +120$."
    },
    {
        "id": 29,
        "question": "What is the value of $(-1)^{100}$?",
        "options": ["$-1$", "$+1$", "$-100$", "$+100$"],
        "correct": 1,
        "solution": "100 is an even number, so $(-1)^{100} = +1$."
    },
    {
        "id": 30,
        "question": "Is subtraction of integers commutative? (i.e. is $a - b = b - a$ for all integers?)",
        "options": ["Yes, always", "No, subtraction is not commutative", "Only when both numbers are positive", "Only when both numbers are negative"],
        "correct": 1,
        "solution": "Subtraction is NOT commutative! For example, $5 - 3 = 2$, but $3 - 5 = -2$. $2 \\neq -2$."
    },

    # Questions 31 to 40 (Slide 20)
    {
        "id": 31,
        "question": "Evaluate: $(-63) \\div 9$",
        "options": ["$+7$", "$-7$", "$+8$", "$-8$"],
        "correct": 1,
        "solution": "Negative $\\div$ Positive = Negative. $63 \\div 9 = 7$, so $(-63) \\div 9 = -7$."
    },
    {
        "id": 32,
        "question": "Evaluate: $(-80) \\div (-16)$",
        "options": ["$-5$", "$+5$", "$-4$", "$+4$"],
        "correct": 1,
        "solution": "Negative $\\div$ Negative = Positive. $80 \\div 16 = 5$, so $(-80) \\div (-16) = +5$."
    },
    {
        "id": 33,
        "question": "Solve the missing factor division: $? \\div (-4) = 12$",
        "options": ["$-48$", "$+48$", "$-3$", "$+3$"],
        "correct": 0,
        "solution": "Multiply both sides by $-4$: $? = 12 \\times (-4) = -48$."
    },
    {
        "id": 34,
        "question": "Which of the following operations is NOT defined in mathematics?",
        "options": ["$0 \\div (-8)$", "$(-8) \\div 1$", "$(-8) \\div 0$", "$(-8) \\div (-8)$"],
        "correct": 2,
        "solution": "Division by zero is strictly undefined: $(-8) \\div 0$ is not defined."
    },
    {
        "id": 35,
        "question": "Evaluate: $0 \\div (-15)$",
        "options": ["$-15$", "$+15$", "$0$", "Undefined"],
        "correct": 2,
        "solution": "Zero divided by any non-zero integer is always zero: $0 \\div (-15) = 0$."
    },
    {
        "id": 36,
        "question": "Evaluate: $[(-36) \\div 12] \\div 3$",
        "options": ["$+1$", "$-1$", "$+9$", "$-9$"],
        "correct": 1,
        "solution": "Inside brackets: $(-36) \\div 12 = -3$. Then $(-3) \\div 3 = -1$."
    },
    {
        "id": 37,
        "question": "Is division of integers associative? Test $[(-16) \\div 4] \\div (-2)$ vs $(-16) \\div [4 \\div (-2)]$.",
        "options": ["Yes, both equal $+2$", "No, first equals $+2$ while second equals $+8$", "Yes, both equal $-4$", "No, first equals $-2$ while second equals $-8$"],
        "correct": 1,
        "solution": "$[(-16) \\div 4] \\div (-2) = (-4) \\div (-2) = +2$. But $(-16) \\div [4 \\div (-2)] = (-16) \\div (-2) = +8$. Since $+2 \\neq +8$, division is NOT associative!"
    },
    {
        "id": 38,
        "question": "For any integer $a$, what is $a \\div (-1)$?",
        "options": ["$a$", "$-a$", "$1$", "$-1$"],
        "correct": 1,
        "solution": "Dividing by $-1$ flips the sign, yielding the additive inverse: $a \\div (-1) = -a$."
    },
    {
        "id": 39,
        "question": "Evaluate: $[(-6) + 5] \\div [(-2) + 1]$",
        "options": ["$+1$", "$-1$", "$+2$", "$-2$"],
        "correct": 0,
        "solution": "First bracket: $(-6) + 5 = -1$. Second bracket: $(-2) + 1 = -1$. Now $(-1) \\div (-1) = +1$."
    },
    {
        "id": 40,
        "question": "A deep sea diver descends at $3\\text{ m/s}$ for $40\\text{ seconds}$, then ascends at $2\\text{ m/s}$ for $25\\text{ seconds}$. What is the diver's final depth?",
        "options": ["$-120\\text{ m}$", "$-70\\text{ m}$", "$-50\\text{ m}$", "$-170\\text{ m}$"],
        "correct": 1,
        "solution": "Descent: $40 \\times (-3) = -120\\text{ m}$. Ascent: $25 \\times (+2) = +50\\text{ m}$. Final depth $= -120 + 50 = -70\\text{ m}$ (70 meters below sea level)."
    }
]

code = f'''# -*- coding: utf-8 -*-
"""
Class 7 Mathematics - Chapter 10: Operations with Integers Data File
Generated automatically.
"""

SLIDES_DATA = {json.dumps(SLIDES_DATA, indent=2, ensure_ascii=False)}

QUIZ_QUESTIONS = {json.dumps(QUIZ_QUESTIONS, indent=2, ensure_ascii=False)}
'''

# Replace null with None in python file
code = code.replace(': null', ': None')

with open('.agents/class7_math_operations_with_integers_data.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Generated .agents/class7_math_operations_with_integers_data.py successfully!")
