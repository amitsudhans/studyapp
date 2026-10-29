# -*- coding: utf-8 -*-
"""
Script to create .agents/class7_math_another_peek_beyond_the_point_data.py
Contains 20 slides, 32 checkpoints, and 40 quiz questions with step-by-step KaTeX solutions.
Chapter: Another Peek Beyond the Point (Decimals - Multiplication, Division & Applications)
Mentor: Acharya Madhava of Sangamagrama (Master of Decimal Precision & Infinite Expansions)
"""

import os
import json

slides_data = [
    {
        "slide_num": 1,
        "section": "4.1 Recap of Decimals",
        "badge": "Indian Place Value & Decimal Fractions",
        "title": "The Decimal Frontier: Tenths, Hundredths & Thousandths",
        "narration": "Namaste, young mathematicians! I am Acharya Madhava of Sangamagrama. In our Kerala school of astronomy, precision is everything. Just as the Indian place value system extends infinitely to the left by tens for whole numbers, it extends symmetrically to the right for fractional parts: tenths, hundredths, thousandths, and beyond! Let us explore how every step to the right divides by ten.",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-amber-500/10 border border-amber-500/30 rounded-xl">
    <h4 class="font-bold text-amber-300 text-sm mb-1">🌟 Symmetrical Extension of the Base-10 Place Value System</h4>
    <p class="text-xs text-slate-300 leading-relaxed">
      In our Indian decimal place-value system, moving one step left multiplies value by $10$. Symmetrically, moving one step to the right of the unit's place divides value by $10$:
    </p>
    <div class="mt-2 text-center text-xs font-mono text-amber-200 bg-slate-900/60 p-2 rounded-lg">
      $\dots \leftarrow \times 10 \quad [\text{Hundreds}] \quad [\text{Tens}] \quad [\text{Ones}] \quad \mathbf{\cdot} \quad [\text{Tenths}] \quad [\text{Hundredths}] \quad [\text{Thousandths}] \quad \div 10 \rightarrow \dots$
    </div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="text-xs font-bold text-teal-400 mb-1">1. Tenths ($\frac{1}{10}$)</div>
      <p class="text-xs text-slate-300">
        Dividing $1$ whole into $10$ equal slices gives tenths. $1 \text{ tenth} = \frac{1}{10} = 0.1$. Ten tenths make $1$ whole unit.
      </p>
    </div>
    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="text-xs font-bold text-cyan-400 mb-1">2. Hundredths ($\frac{1}{100}$)</div>
      <p class="text-xs text-slate-300">
        Dividing each tenth into $10$ equal parts yields hundredths. $1 \text{ hundredth} = \frac{1}{100} = 0.01$. Ten hundredths equal one tenth.
      </p>
    </div>
    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="text-xs font-bold text-emerald-400 mb-1">3. Thousandths ($\frac{1}{1000}$)</div>
      <p class="text-xs text-slate-300">
        Dividing each hundredth into $10$ slices yields thousandths. $1 \text{ thousandth} = \frac{1}{1000} = 0.001$. Essential for delicate astronomical and metric measures.
      </p>
    </div>
  </div>

  <div class="p-3 bg-teal-500/10 border border-teal-500/30 rounded-xl text-xs text-slate-300">
    <span class="font-bold text-teal-300">The Decimal Point Separator:</span> The dot ($\cdot$) serves as an anchor separating whole items on the left from fractional pieces on the right. In metric measures: $1\text{ mm} = 0.1\text{ cm} = 0.001\text{ m}$, and $1\text{ paisa} = \text{Rs. } 0.01$ (₹$0.01$).
  </div>
</div>
""",
        "sim_id": "sim-place-value-matrix",
        "checkpoints": [
            {
                "question": "What is the place value of the digit 7 in the number 45.378?",
                "options": ["7 tens (70)", "7 tenths (0.7)", "7 hundredths (0.07)", "7 thousandths (0.007)"],
                "correct": 2,
                "explanation": "In 45.378, 3 is in the tenths place, 7 is in the hundredths place (value = 7/100 = 0.07), and 8 is in the thousandths place."
            },
            {
                "question": "How many thousandths equal one tenth?",
                "options": ["10 thousandths", "100 thousandths", "1,000 thousandths", "0.01 thousandths"],
                "correct": 1,
                "explanation": "Since 1 tenth = 1/10 and 1 thousandth = 1/1000, we have (1/10) / (1/1000) = 100 thousandths in one tenth."
            }
        ]
    },
    {
        "slide_num": 2,
        "section": "4.1 Recap of Decimals",
        "badge": "Expanded Form & Additive Decomposition",
        "title": "Expanded Decimal Notation: Deconstructing Numbers",
        "narration": "Every decimal number can be unpacked into a magnificent additive sum of whole place values and decimal fractions. When we write 23.456, we reveal 2 tens, 3 ones, 4 tenths, 5 hundredths, and 6 thousandths! Understanding this expanded architecture makes decimal multiplication and division natural and intuitive.",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-indigo-500/10 border border-indigo-500/30 rounded-xl">
    <h4 class="font-bold text-indigo-300 text-sm mb-1">🧩 The Two Forms of Expanded Decimal Notation</h4>
    <p class="text-xs text-slate-300 leading-relaxed">
      A decimal number such as $23.456$ can be expressed either as a sum of <b>fractional parts</b> or as a sum of <b>decimal components</b>:
    </p>
    <div class="mt-2 space-y-1 text-xs font-mono text-cyan-200 bg-slate-900/60 p-2.5 rounded-lg">
      <div><b>Fractional Form:</b> $23.456 = 20 + 3 + \frac{4}{10} + \frac{5}{100} + \frac{6}{1000}$</div>
      <div class="text-teal-300"><b>Decimal Form:</b> $23.456 = 20 + 3 + 0.4 + 0.05 + 0.006$</div>
    </div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-amber-300 mb-1">Beware of Zero Placeholders!</div>
      <p class="text-slate-300 mb-2">
        A zero in a decimal column preserves the position of succeeding digits:
      </p>
      <div class="font-mono text-amber-200 bg-slate-900/60 p-2 rounded">
        $5.07 = 5 + 0\text{ tenths} + \frac{7}{100} = 5 + 0.07$<br>
        <span class="text-red-400 font-bold">Contrast:</span> $5.7 = 5 + 0.7$ (ten times larger!)
      </div>
    </div>
    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-emerald-300 mb-1">Reconstructing Standard Decimals</div>
      <p class="text-slate-300 mb-2">
        To reassemble an expanded sum, align digits to their respective place-value slots:
      </p>
      <div class="font-mono text-emerald-200 bg-slate-900/60 p-2 rounded">
        $700 + 4 + \frac{3}{10} + \frac{9}{1000} = 704.309$<br>
        <span class="text-slate-400 text-[11px]">(Note the hundredths column has 0!)</span>
      </div>
    </div>
  </div>
</div>
""",
        "sim_id": "sim-expanded-deconstructor",
        "checkpoints": [
            {
                "question": "What is the standard decimal number for 80 + 3 + 2/10 + 5/1000?",
                "options": ["83.25", "83.205", "83.025", "832.5"],
                "correct": 1,
                "explanation": "80 + 3 = 83 ones, 2/10 = 0.2 (tenths), hundredths is 0, and 5/1000 = 0.005 (thousandths). So the number is 83.205."
            },
            {
                "question": "Which of the following represents 6.04 in expanded fractional form?",
                "options": ["6 + 4/10", "6 + 4/100", "6 + 4/1000", "60 + 4/10"],
                "correct": 1,
                "explanation": "In 6.04, the digit 0 is in the tenths place and 4 is in the hundredths place. Thus, 6.04 = 6 + 4/100."
            }
        ]
    },
    {
        "slide_num": 3,
        "section": "4.1 Recap of Decimals",
        "badge": "Fractions with Denominators 10, 100, 1000",
        "title": "The Power-of-10 Fraction Bridge",
        "narration": "Converting fractions whose denominators are 10, 100, or 1000 into decimals is sheer elegance! The number of zeroes in the power of ten tells you exactly how many decimal places must follow the decimal point. Three tenths is 0.3, forty-three hundredths is 0.43, and one hundred twenty-five thousandths is 0.125.",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-cyan-500/10 border border-cyan-500/30 rounded-xl">
    <h4 class="font-bold text-cyan-300 text-sm mb-1">🌉 The Direct Denominator Power-of-10 Law</h4>
    <p class="text-xs text-slate-300 leading-relaxed">
      When a fraction has a denominator of $10^n$, write down the numerator digits and place the decimal point $n$ digits counting from the right end:
    </p>
    <div class="mt-2 grid grid-cols-3 gap-2 text-center text-xs font-mono">
      <div class="p-2 bg-slate-900/70 rounded border border-cyan-500/20 text-cyan-200">
        $\frac{7}{10} = 0.7$<br><span class="text-[10px] text-slate-400">1 zero $\to$ 1 place</span>
      </div>
      <div class="p-2 bg-slate-900/70 rounded border border-cyan-500/20 text-cyan-200">
        $\frac{43}{100} = 0.43$<br><span class="text-[10px] text-slate-400">2 zeros $\to$ 2 places</span>
      </div>
      <div class="p-2 bg-slate-900/70 rounded border border-cyan-500/20 text-cyan-200">
        $\frac{389}{1000} = 0.389$<br><span class="text-[10px] text-slate-400">3 zeros $\to$ 3 places</span>
      </div>
    </div>
  </div>

  <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60 text-xs space-y-2">
    <div class="font-bold text-teal-300">Special Cases: Leading Zeroes & Improper Fractions</div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-slate-300">
      <div class="bg-slate-900/60 p-2.5 rounded-lg border border-slate-700/50">
        <b class="text-amber-300">Numerator has Fewer Digits:</b><br>
        Prefix zeroes before the numerator so that digit count matches denominator zeros:<br>
        $\frac{3}{100} = 0.03 \quad (\text{not } 0.3!)$<br>
        $\frac{9}{1000} = 0.009$
      </div>
      <div class="bg-slate-900/60 p-2.5 rounded-lg border border-slate-700/50">
        <b class="text-emerald-300">Numerator Larger than Denominator:</b><br>
        Count places from right, giving a whole number part $\gt 0$:<br>
        $\frac{254}{10} = 25.4$<br>
        $\frac{1485}{100} = 14.85$
      </div>
    </div>
  </div>
</div>
""",
        "sim_id": "sim-fraction-decimal-bridge",
        "checkpoints": [
            {
                "question": "What is the decimal representation of the fraction 17/1000?",
                "options": ["0.17", "0.017", "0.0017", "1.7"],
                "correct": 1,
                "explanation": "The denominator 1000 has 3 zeros, so we need 3 decimal places: prefix one leading zero to 17 to get 0.017."
            },
            {
                "question": "Convert the improper fraction 504/100 to a decimal.",
                "options": ["50.4", "5.04", "0.504", "504.0"],
                "correct": 1,
                "explanation": "With 2 zeros in 100, moving 2 places from the right of 504 gives 5.04."
            }
        ]
    },
    {
        "slide_num": 4,
        "section": "4.1 Recap of Decimals",
        "badge": "Scaling Denominators & Trailing Zeroes",
        "title": "Scaling Denominators: The Friendly Factor Rule",
        "narration": "What if the denominator is not 10, 100, or 1000? If its prime factors are only 2s and 5s, we can scale it to a friendly power of ten using equivalent fractions! One-half becomes five-tenths or 0.5. Three-fourths becomes seventy-five hundredths or 0.75. Furthermore, notice that adding trailing zeroes to a decimal leaves its value completely unchanged!",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-emerald-500/10 border border-emerald-500/30 rounded-xl">
    <h4 class="font-bold text-emerald-300 text-sm mb-1">🎯 The Friendly Factor Scaling Rule ($2 \times 5 = 10$)</h4>
    <p class="text-xs text-slate-300 leading-relaxed">
      Any fraction whose denominator has only $2$s or $5$s as prime factors can be scaled to a power of ten by multiplying numerator and denominator by the complementary factor:
    </p>
    <div class="mt-2 grid grid-cols-2 md:grid-cols-4 gap-2 text-xs font-mono text-center">
      <div class="p-2 bg-slate-900/60 rounded border border-emerald-500/20 text-emerald-200">
        $\frac{1}{2} = \frac{1 \times 5}{2 \times 5} = \frac{5}{10} = \mathbf{0.5}$
      </div>
      <div class="p-2 bg-slate-900/60 rounded border border-emerald-500/20 text-emerald-200">
        $\frac{3}{4} = \frac{3 \times 25}{4 \times 25} = \frac{75}{100} = \mathbf{0.75}$
      </div>
      <div class="p-2 bg-slate-900/60 rounded border border-emerald-500/20 text-emerald-200">
        $\frac{1}{8} = \frac{1 \times 125}{8 \times 125} = \frac{125}{1000} = \mathbf{0.125}$
      </div>
      <div class="p-2 bg-slate-900/60 rounded border border-emerald-500/20 text-emerald-200">
        $\frac{7}{25} = \frac{7 \times 4}{25 \times 4} = \frac{28}{100} = \mathbf{0.28}$
      </div>
    </div>
  </div>

  <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60 text-xs">
    <div class="font-bold text-amber-300 mb-1">Invariance of Trailing Zeroes</div>
    <p class="text-slate-300 leading-relaxed">
      Appending zeroes to the extreme right of a decimal does not alter its value:
      $$0.5 = 0.50 = 0.500 \quad \left(\frac{5}{10} = \frac{50}{100} = \frac{500}{1000}\right)$$
      However, inserting a zero <i>between</i> the decimal point and digits alters the place value drastically: $0.05 = \frac{5}{100}$, which is ten times smaller than $0.5$!
    </p>
  </div>
</div>
""",
        "sim_id": "sim-friendly-multiplier-scaler",
        "checkpoints": [
            {
                "question": "What is 3/5 expressed as a decimal using the scaling rule?",
                "options": ["0.35", "0.6", "0.06", "0.15"],
                "correct": 1,
                "explanation": "Multiply numerator and denominator by 2: (3 × 2) / (5 × 2) = 6/10 = 0.6."
            },
            {
                "question": "Which of the following decimals is NOT equal to 0.4?",
                "options": ["0.40", "0.400", "0.04", "4/10"],
                "correct": 2,
                "explanation": "0.04 is 4 hundredths (4/100), whereas 0.4, 0.40, and 0.400 are all equivalent to 4 tenths (4/10)."
            }
        ]
    },
    {
        "slide_num": 5,
        "section": "4.2 Decimal Multiplication",
        "badge": "Repeated Addition & Decimal Steps",
        "title": "Multiplying Decimals by Whole Numbers",
        "narration": "Multiplication at its heart is repeated addition! When we multiply 0.3 by 4, we take 4 steps of 0.3 along the number line, reaching 1.2. Alternatively, converting to fractions: three-tenths multiplied by 4 gives twelve-tenths, which is 1.2. Notice the single decimal place in the product matching the single decimal place in 0.3!",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-blue-500/10 border border-blue-500/30 rounded-xl">
    <h4 class="font-bold text-blue-300 text-sm mb-1">🚶 Number Line & Repeated Addition Model</h4>
    <p class="text-xs text-slate-300 leading-relaxed">
      Multiplying a decimal by a whole number $k$ means taking $k$ copies of that decimal:
    </p>
    <div class="mt-2 text-center text-xs font-mono text-cyan-200 bg-slate-900/60 p-2 rounded-lg">
      $0.3 \times 4 = 0.3 + 0.3 + 0.3 + 0.3 = 1.2$
    </div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-teal-300 mb-1">Method 1: Fraction Conversion</div>
      <p class="text-slate-300 leading-relaxed">
        Convert the decimal to a fraction over $10, 100,$ or $1000$, multiply, and convert back:
        $$0.25 \times 3 = \frac{25}{100} \times 3 = \frac{75}{100} = \mathbf{0.75}$$
      </p>
    </div>
    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-amber-300 mb-1">Method 2: Whole Number Multiplication</div>
      <p class="text-slate-300 leading-relaxed">
        Ignore the decimal point, multiply as whole numbers, and restore the decimal places:
        $$12 \times 3 = 36 \implies 1.2 \times 3 = \mathbf{3.6}$$
        (1 decimal place in factor $\to$ 1 decimal place in product).
      </p>
    </div>
  </div>
</div>
""",
        "sim_id": "sim-whole-decimal-multiplier",
        "checkpoints": [
            {
                "question": "What is 0.08 × 6?",
                "options": ["0.48", "4.8", "0.048", "0.0048"],
                "correct": 0,
                "explanation": "8 × 6 = 48. Since 0.08 has 2 decimal places, the product must have 2 decimal places: 0.48."
            },
            {
                "question": "If 1 meter of ribbon costs ₹4.50, what is the cost of 5 meters?",
                "options": ["₹20.50", "₹22.50", "₹225.00", "₹2.25"],
                "correct": 1,
                "explanation": "4.5 × 5 = (45 × 5) / 10 = 225 / 10 = ₹22.50."
            }
        ]
    },
    {
        "slide_num": 6,
        "section": "4.2 Decimal Multiplication",
        "badge": "100-Square Area Model",
        "title": "Multiplying Decimals by Decimals: The Unit Square Grid",
        "narration": "What happens when you multiply a decimal by another decimal, like 0.7 by 0.4? Imagine a unit square with area 1, sliced into 100 small hundredth squares. Shade 7 tenths horizontally in blue and 4 tenths vertically in yellow. The overlapping green rectangle covers exactly 28 small hundredths, proving that 0.7 times 0.4 equals 0.28!",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-violet-500/10 border border-violet-500/30 rounded-xl">
    <h4 class="font-bold text-violet-300 text-sm mb-1">🟩 The Geometric Proof: Unit Square Area Model</h4>
    <p class="text-xs text-slate-300 leading-relaxed">
      Consider a square of side $1\text{ unit} \times 1\text{ unit} = 1\text{ sq unit}$, partitioned into a $10 \times 10$ grid of $100$ identical small squares, each of area $\frac{1}{100} = 0.01$.
    </p>
    <div class="mt-2 text-center text-xs font-mono text-emerald-200 bg-slate-900/60 p-2 rounded-lg">
      $\text{Area} = \text{Length} \times \text{Breadth} = 0.7 \times 0.4 = \frac{7}{10} \times \frac{4}{10} = \frac{28}{100} = \mathbf{0.28}$
    </div>
  </div>

  <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60 text-xs space-y-2">
    <div class="font-bold text-cyan-300">Why do the Decimal Places Add Up?</div>
    <p class="text-slate-300 leading-relaxed">
      In fraction form, multiplying denominators creates higher powers of ten:
      $$\frac{a}{10^m} \times \frac{b}{10^n} = \frac{a \times b}{10^{m+n}}$$
      Because $10 \times 10 = 100$, tenths multiplied by tenths yield <b>hundredths</b> (2 decimal places). Tenths multiplied by hundredths yield <b>thousandths</b> ($10 \times 100 = 1000$, 3 decimal places).
    </p>
  </div>
</div>
""",
        "sim_id": "sim-grid-multiplication-area",
        "checkpoints": [
            {
                "question": "In a 10×10 unit grid, multiplying 0.6 by 0.3 overlaps how many hundredth squares?",
                "options": ["9 squares", "18 squares", "63 squares", "1.8 squares"],
                "correct": 1,
                "explanation": "6 rows of tenths overlapping with 3 columns of tenths creates a 6×3 rectangle containing 18 small hundredth squares, representing 0.18."
            },
            {
                "question": "What is 0.5 × 0.5?",
                "options": ["2.5", "0.25", "0.025", "0.5"],
                "correct": 1,
                "explanation": "5 × 5 = 25. With 1 decimal place in each factor (1 + 1 = 2 places), 0.5 × 0.5 = 0.25 (one-quarter of the unit square)."
            }
        ]
    },
    {
        "slide_num": 7,
        "section": "4.2 Decimal Multiplication",
        "badge": "Universal 3-Step Algorithm",
        "title": "The General Multiplication Algorithm",
        "narration": "To multiply any two decimal numbers, follow this universal three-step rule: first, temporarily ignore the decimal points and multiply as whole numbers. Second, count the total number of decimal digits across both factors. Third, place the decimal point that many places from the right of the product, inserting leading zeroes if necessary!",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-fuchsia-500/10 border border-fuchsia-500/30 rounded-xl">
    <h4 class="font-bold text-fuchsia-300 text-sm mb-1">⚙️ The 3-Step Decimal Multiplication Pipeline</h4>
    <div class="space-y-2 mt-2 text-xs text-slate-300">
      <div class="flex items-start gap-2">
        <span class="w-5 h-5 rounded-full bg-fuchsia-500/30 text-fuchsia-300 flex items-center justify-center font-bold shrink-0">1</span>
        <div><b>Strip Points:</b> Multiply both numbers treating them as ordinary integers without decimal points.</div>
      </div>
      <div class="flex items-start gap-2">
        <span class="w-5 h-5 rounded-full bg-fuchsia-500/30 text-fuchsia-300 flex items-center justify-center font-bold shrink-0">2</span>
        <div><b>Sum Decimal Places:</b> Count decimal digits in factor 1 ($m$) and factor 2 ($n$). Total places needed = $m + n$.</div>
      </div>
      <div class="flex items-start gap-2">
        <span class="w-5 h-5 rounded-full bg-fuchsia-500/30 text-fuchsia-300 flex items-center justify-center font-bold shrink-0">3</span>
        <div><b>Insert the Point:</b> Count $m+n$ positions from the right end of the product. If digits run out, prefix leading zeroes!</div>
      </div>
    </div>
  </div>

  <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60 text-xs">
    <div class="font-bold text-amber-300 mb-1">Crucial Trap: Prefixing Leading Zeroes</div>
    <p class="text-slate-300 leading-relaxed mb-2">
      Consider $0.02 \times 0.03$:
    </p>
    <div class="font-mono text-amber-200 bg-slate-900/60 p-2.5 rounded-lg space-y-1">
      <div>Whole product: $2 \times 3 = 6$ (only 1 digit)</div>
      <div>Decimal places required: $2 + 2 = 4$ decimal places!</div>
      <div>Prefix 3 leading zeroes before 6: $\mathbf{0.0006}$</div>
    </div>
  </div>
</div>
""",
        "sim_id": "sim-multiplication-algorithm-stepper",
        "checkpoints": [
            {
                "question": "What is 0.12 × 0.4?",
                "options": ["0.48", "0.048", "4.8", "0.0048"],
                "correct": 1,
                "explanation": "12 × 4 = 48. Total decimal places = 2 (in 0.12) + 1 (in 0.4) = 3 places. Thus, 48 with 3 places = 0.048."
            },
            {
                "question": "Calculate 0.05 × 0.07.",
                "options": ["0.35", "0.035", "0.0035", "0.00035"],
                "correct": 2,
                "explanation": "5 × 7 = 35. Decimal places = 2 + 2 = 4 places. Prefix two zeroes before 35 to make 4 places: 0.0035."
            }
        ]
    },
    {
        "slide_num": 8,
        "section": "4.2 Decimal Multiplication",
        "badge": "Powers of 10 & Magnitude Paradoxes",
        "title": "Shifting Points & Magnitude Paradoxes",
        "narration": "When you multiply by 10, 100, or 1000, the digits shift left, making the decimal point move to the right by the number of zeroes. But here is a wonderful surprise: does multiplication always make numbers bigger? Not at all! When you multiply by a number less than one, the product actually shrinks!",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-amber-500/10 border border-amber-500/30 rounded-xl">
    <h4 class="font-bold text-amber-300 text-sm mb-1">⚡ Multiplying by Powers of 10: The Rightward Shift</h4>
    <p class="text-xs text-slate-300 leading-relaxed">
      Each power of ten increases place value tenfold, shifting the decimal point to the <b>right</b> by the number of zeroes:
    </p>
    <div class="mt-2 grid grid-cols-3 gap-2 text-xs font-mono text-center">
      <div class="p-2 bg-slate-900/60 rounded border border-amber-500/20 text-amber-200">
        $3.456 \times 10 = \mathbf{34.56}$<br><span class="text-[10px] text-slate-400">1 zero $\to$ 1 place right</span>
      </div>
      <div class="p-2 bg-slate-900/60 rounded border border-amber-500/20 text-amber-200">
        $3.456 \times 100 = \mathbf{345.6}$<br><span class="text-[10px] text-slate-400">2 zeros $\to$ 2 places right</span>
      </div>
      <div class="p-2 bg-slate-900/60 rounded border border-amber-500/20 text-amber-200">
        $3.456 \times 1000 = \mathbf{3456}$<br><span class="text-[10px] text-slate-400">3 zeros $\to$ 3 places right</span>
      </div>
    </div>
  </div>

  <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60 text-xs">
    <div class="font-bold text-rose-300 mb-1">⚖️ The Magnitude Paradox: When Multiplication Shrinks!</div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-2 text-slate-300 mt-2">
      <div class="p-2 bg-slate-900/60 rounded border border-slate-700/40">
        <b class="text-emerald-400">Factor &gt; 1:</b><br>
        Product grows larger than the original number:<br>
        $8 \times 1.5 = 12 \gt 8$
      </div>
      <div class="p-2 bg-slate-900/60 rounded border border-slate-700/40">
        <b class="text-amber-400">Factor &lt; 1:</b><br>
        Product shrinks smaller than the original number:<br>
        $8 \times 0.5 = 4 \lt 8$
      </div>
      <div class="p-2 bg-slate-900/60 rounded border border-slate-700/40">
        <b class="text-rose-400">Both Factors &lt; 1:</b><br>
        Product is smaller than <i>both</i> factors!<br>
        $0.4 \times 0.2 = \mathbf{0.08} \lt 0.2 \lt 0.4$
      </div>
    </div>
  </div>
</div>
""",
        "sim_id": "sim-magnitude-paradox-scale",
        "checkpoints": [
            {
                "question": "What is 4.75 × 100?",
                "options": ["0.0475", "47.5", "475", "4750"],
                "correct": 2,
                "explanation": "Multiplying by 100 (2 zeros) shifts the decimal point 2 places to the right: 4.75 becomes 475."
            },
            {
                "question": "Which statement is true regarding the product 0.8 × 0.3?",
                "options": [
                    "The product is greater than 0.8",
                    "The product is between 0.3 and 0.8",
                    "The product (0.24) is smaller than both 0.8 and 0.3",
                    "The product is 2.4"
                ],
                "correct": 2,
                "explanation": "0.8 × 0.3 = 0.24. Since both factors are strictly between 0 and 1, their product is smaller than both factors (0.24 < 0.3 < 0.8)."
            }
        ]
    },
    {
        "slide_num": 9,
        "section": "4.3 Decimal Division",
        "badge": "Dividing by 10, 100, 1000",
        "title": "Dividing Decimals by Powers of 10: The Leftward Drift",
        "narration": "Division is the inverse of multiplication! When dividing a decimal by 10, 100, or 1000, each place value is divided by ten, causing the decimal point to drift to the left by the number of zeroes. Dividing 45.6 by 10 gives 4.56, while dividing by 100 gives 0.456.",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-teal-500/10 border border-teal-500/30 rounded-xl">
    <h4 class="font-bold text-teal-300 text-sm mb-1">⬅️ The Leftward Shift Law of Division</h4>
    <p class="text-xs text-slate-300 leading-relaxed">
      Dividing by $10^k$ is mathematically identical to multiplying by $\frac{1}{10^k}$. Consequently, the decimal point moves $k$ places to the <b>left</b>:
    </p>
    <div class="mt-2 grid grid-cols-3 gap-2 text-xs font-mono text-center">
      <div class="p-2 bg-slate-900/60 rounded border border-teal-500/20 text-teal-200">
        $73.8 \div 10 = \mathbf{7.38}$<br><span class="text-[10px] text-slate-400">1 zero $\to$ 1 place left</span>
      </div>
      <div class="p-2 bg-slate-900/60 rounded border border-teal-500/20 text-teal-200">
        $73.8 \div 100 = \mathbf{0.738}$<br><span class="text-[10px] text-slate-400">2 zeros $\to$ 2 places left</span>
      </div>
      <div class="p-2 bg-slate-900/60 rounded border border-teal-500/20 text-teal-200">
        $73.8 \div 1000 = \mathbf{0.0738}$<br><span class="text-[10px] text-slate-400">3 zeros $\to$ 3 places left</span>
      </div>
    </div>
  </div>

  <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60 text-xs">
    <div class="font-bold text-cyan-300 mb-1">Prefixing Left Leading Zeroes</div>
    <p class="text-slate-300 leading-relaxed">
      If shifting the decimal point to the left exhausts available digits, fill the gap with zeroes before placing the decimal point:
      $$4.5 \div 100 = 0.045 \quad (\text{shifted 2 places left})$$
      $$0.3 \div 10 = 0.03 \quad (\text{shifted 1 place left})$$
    </p>
  </div>
</div>
""",
        "sim_id": "sim-power10-shift-slider",
        "checkpoints": [
            {
                "question": "What is 28.5 ÷ 100?",
                "options": ["2.85", "0.285", "0.0285", "285.0"],
                "correct": 1,
                "explanation": "Dividing by 100 shifts the point 2 places to the left: 28.5 becomes 0.285."
            },
            {
                "question": "What is 0.7 ÷ 100?",
                "options": ["0.07", "0.007", "0.0007", "7.0"],
                "correct": 1,
                "explanation": "Shifting the decimal point 2 places to the left from 0.7 requires inserting leading zeros: 0.007."
            }
        ]
    },
    {
        "slide_num": 10,
        "section": "4.3 Decimal Division",
        "badge": "Place Value Regrouping & Remainders",
        "title": "Long Division via Place Value: Regrouping Remainders",
        "narration": "What actually happens in long division of decimals? It is pure place-value regrouping! When dividing 7 by 2, 2 goes into 7 three times with 1 whole remaining. We break that 1 whole into 10 tenths! Then 2 goes into 10 tenths five times, giving exactly 3.5. When dividing decimals by whole numbers, the decimal point in the quotient aligns directly above the dividend!",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-indigo-500/10 border border-indigo-500/30 rounded-xl">
    <h4 class="font-bold text-indigo-300 text-sm mb-1">🔄 Regrouping Units Across the Decimal Boundary</h4>
    <p class="text-xs text-slate-300 leading-relaxed">
      When a whole number division leaves a remainder, we don't stop! We regroup the remainder into tenths ($\times 10$), hundredths, and thousandths:
    </p>
    <div class="mt-2 text-xs font-mono text-cyan-200 bg-slate-900/60 p-2.5 rounded-lg space-y-1">
      <div><b>Example $15.6 \div 4$:</b></div>
      <div>1. Divide wholes: $15 \div 4 = \mathbf{3}$ with remainder $3\text{ ones}$.</div>
      <div>2. Place decimal point in quotient directly above the dividend point ($\mathbf{3.}$)</div>
      <div>3. Regroup $3\text{ ones} = 30\text{ tenths}$. Add $6\text{ tenths} = 36\text{ tenths}$.</div>
      <div>4. Divide tenths: $36 \div 4 = \mathbf{9}\text{ tenths} \implies \text{Quotient} = \mathbf{3.9}$.</div>
    </div>
  </div>

  <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60 text-xs">
    <div class="font-bold text-emerald-300 mb-1">Golden Rule of Long Division</div>
    <p class="text-slate-300 leading-relaxed">
      Keep dividing until the remainder becomes zero (terminating decimal) or until a repeating pattern emerges. You can append as many trailing zeroes to the dividend as necessary ($15 = 15.0 = 15.00$) without altering its numerical value.
    </p>
  </div>
</div>
""",
        "sim_id": "sim-place-value-regroup-division",
        "checkpoints": [
            {
                "question": "What is 18.6 ÷ 3 using place value division?",
                "options": ["6.2", "0.62", "62.0", "6.02"],
                "correct": 0,
                "explanation": "18 wholes ÷ 3 = 6 wholes. 6 tenths ÷ 3 = 2 tenths. Thus, 18.6 ÷ 3 = 6.2."
            },
            {
                "question": "Divide 7 by 4 using decimal regrouping.",
                "options": ["1.3", "1.75", "1.5", "1.25"],
                "correct": 1,
                "explanation": "7 ÷ 4 = 1 remainder 3. 3 ones = 30 tenths. 30 ÷ 4 = 7 tenths remainder 2 tenths. 2 tenths = 20 hundredths. 20 ÷ 4 = 5 hundredths. Result = 1.75."
            }
        ]
    },
    {
        "slide_num": 11,
        "section": "4.3 Decimal Division",
        "badge": "Clearing Divisor Decimals",
        "title": "Dividing by Decimal Divisors: The Golden Scale Factor",
        "narration": "How do we divide when the divisor itself is a decimal, like 4.5 divided by 0.15? We apply the golden law of equivalent fractions! Multiply both dividend and divisor by the same power of ten until the divisor becomes a whole number. 4.5 divided by 0.15 becomes 450 divided by 15, which is 30! And notice: dividing by a number smaller than one produces a quotient larger than the original dividend!",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-purple-500/10 border border-purple-500/30 rounded-xl">
    <h4 class="font-bold text-purple-300 text-sm mb-1">🔑 The Golden Equivalent Fraction Law: $\frac{a}{b} = \frac{a \times 10^k}{b \times 10^k}$</h4>
    <p class="text-xs text-slate-300 leading-relaxed">
      We never divide by a decimal divisor directly. Instead, shift the decimal point in the divisor to the right until it is an integer, and shift the dividend's decimal point by the <b>exact same number of places</b>:
    </p>
    <div class="mt-2 text-xs font-mono text-fuchsia-200 bg-slate-900/60 p-2.5 rounded-lg">
      $$\frac{4.5}{0.15} = \frac{4.5 \times 100}{0.15 \times 100} = \frac{450}{15} = \mathbf{30}$$
    </div>
  </div>

  <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60 text-xs">
    <div class="font-bold text-amber-300 mb-1">🔍 Magnification Paradox of Division</div>
    <p class="text-slate-300 leading-relaxed">
      Students often assume division always makes numbers smaller. But when the divisor is less than $1$, the quotient is <b>larger</b> than the dividend:
      $$6 \div 0.5 = 6 \div \frac{1}{2} = 6 \times 2 = \mathbf{12} \gt 6$$
      <i>Intuition:</i> "How many 50-paise coins fit inside ₹6?" Twelve coins!
    </p>
  </div>
</div>
""",
        "sim_id": "sim-decimal-divisor-transformer",
        "checkpoints": [
            {
                "question": "What is 2.4 ÷ 0.08?",
                "options": ["0.3", "3", "30", "300"],
                "correct": 2,
                "explanation": "Multiply both by 100 to clear the divisor's decimals: (2.4 × 100) / (0.08 × 100) = 240 / 8 = 30."
            },
            {
                "question": "What is 0.36 ÷ 0.6?",
                "options": ["0.06", "0.6", "6.0", "60.0"],
                "correct": 1,
                "explanation": "Multiply both by 10: 3.6 ÷ 6 = 0.6."
            }
        ]
    },
    {
        "slide_num": 12,
        "section": "4.3 Decimal Division",
        "badge": "Terminating vs Repeating & The Cyclic Wheel",
        "title": "Terminating vs Repeating Decimals & Cyclic Magic: 142857",
        "narration": "Some fractions terminate cleanly, like one-quarter being 0.25, while others repeat endlessly, like one-third being 0.333 recurring. And among recurring decimals lies nature's most enchanting cyclic number: 142857 from one-seventh! When multiplied by 1, 2, 3, 4, 5, or 6, the exact same six digits rotate in a perfect celestial circle!",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-pink-500/10 border border-pink-500/30 rounded-xl">
    <h4 class="font-bold text-pink-300 text-sm mb-1">♾️ Terminating vs Non-Terminating Repeating Decimals</h4>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs text-slate-300 mt-2">
      <div class="p-2.5 bg-slate-900/60 rounded border border-slate-700/50">
        <b class="text-emerald-400">Terminating Decimals:</b><br>
        Denominators whose only prime factors are $2$ and $5$:<br>
        $\frac{1}{4} = 0.25, \quad \frac{3}{8} = 0.375, \quad \frac{7}{20} = 0.35$
      </div>
      <div class="p-2.5 bg-slate-900/60 rounded border border-slate-700/50">
        <b class="text-pink-400">Recurring Decimals:</b><br>
        Denominators containing prime factors other than $2$ or $5$ ($3, 7, 11, \dots$):<br>
        $\frac{1}{3} = 0.333\dots = 0.\overline{3}, \quad \frac{1}{6} = 0.1\overline{6}$
      </div>
    </div>
  </div>

  <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60 text-xs">
    <div class="font-bold text-amber-300 mb-1">🎡 The Marvel of Cyclic 142857 ($\frac{1}{7}$)</div>
    <p class="text-slate-300 leading-relaxed mb-2">
      $\frac{1}{7} = 0.\overline{142857}$. Multiples of $\frac{1}{7}$ cycle through the exact same digit permutation:
    </p>
    <div class="grid grid-cols-2 md:grid-cols-3 gap-2 font-mono text-[11px] text-amber-200">
      <div class="bg-slate-900/70 p-1.5 rounded">$\frac{1}{7} = 0.\overline{\mathbf{1}42857}$</div>
      <div class="bg-slate-900/70 p-1.5 rounded">$\frac{2}{7} = 0.\overline{\mathbf{2}85714}$</div>
      <div class="bg-slate-900/70 p-1.5 rounded">$\frac{3}{7} = 0.\overline{\mathbf{4}28571}$</div>
      <div class="bg-slate-900/70 p-1.5 rounded">$\frac{4}{7} = 0.\overline{\mathbf{5}71428}$</div>
      <div class="bg-slate-900/70 p-1.5 rounded">$\frac{5}{7} = 0.\overline{\mathbf{7}14285}$</div>
      <div class="bg-slate-900/70 p-1.5 rounded">$\frac{6}{7} = 0.\overline{\mathbf{8}57142}$</div>
    </div>
  </div>
</div>
""",
        "sim_id": "sim-cyclic-wheel-142857",
        "checkpoints": [
            {
                "question": "Which of the following fractions produces a terminating decimal?",
                "options": ["1/6", "5/8", "2/9", "4/7"],
                "correct": 1,
                "explanation": "The denominator 8 has prime factorisation 2³, which contains only 2. Thus 5/8 = 0.625 (terminating)."
            },
            {
                "question": "If 1/7 = 0.142857..., what is the first decimal digit of 3/7?",
                "options": ["1", "2", "4", "5"],
                "correct": 2,
                "explanation": "Since 3/7 ≈ 0.428571..., the first digit after the decimal point is 4 (the third smallest digit in the cycle 1, 2, 4, 5, 7, 8)."
            }
        ]
    },
    {
        "slide_num": 13,
        "section": "4.4 Look Before You Leap!",
        "badge": "Tropical Year & Orbital Precision",
        "title": "Look Before You Leap! The Cosmic Decimal: 365.2422 Days",
        "narration": "Look before you leap! Here is where decimal arithmetic governs the very calendar on your wall. Earth does not orbit the Sun in exactly 365 days. The true astronomical tropical year takes approximately 365.2422 days! That tiny decimal remainder of 0.2422 days accumulates silently every year. Without corrections, human seasons would slip away!",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-amber-500/10 border border-amber-500/30 rounded-xl">
    <h4 class="font-bold text-amber-300 text-sm mb-1">🌍 The Astronomical Tropical Year: $365.2422\text{ Days}$</h4>
    <p class="text-xs text-slate-300 leading-relaxed">
      The time taken by Earth to travel from one vernal equinox to the next is approximately:
      $$\text{Tropical Year} = 365\text{ days} + 0.2422\text{ days} \approx 365\text{ days } 5\text{ hours } 48\text{ mins } 46\text{ secs}$$
    </p>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-rose-300 mb-1">What if We Ignored the Decimal?</div>
      <p class="text-slate-300 leading-relaxed">
        If a calendar had only $365$ days:
        $$\text{Annual Error} = -0.2422\text{ days/year}$$
        In $100$ years, the calendar drifts by:
        $$100 \times 0.2422 = \mathbf{24.22\text{ days!}}$$
        In $750$ years, months would drift by half a year—celebrating monsoon festivals in scorching summer!
      </p>
    </div>
    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-cyan-300 mb-1">The 4-Year Accumulation</div>
      <p class="text-slate-300 leading-relaxed">
        In $4$ years, the fractional excess accumulates to:
        $$4 \times 0.2422 = \mathbf{0.9688\text{ days}} \approx 1\text{ full day!}$$
        This near-integer accumulation inspired astronomers to insert one extra day (February 29) every four years.
      </p>
    </div>
  </div>
</div>
""",
        "sim_id": "sim-earth-orbit-drift",
        "checkpoints": [
            {
                "question": "What is the annual fractional excess over 365 days in Earth's orbit?",
                "options": ["0.5 days", "0.25 days exact", "0.2422 days", "0.0078 days"],
                "correct": 2,
                "explanation": "Earth's tropical year is approximately 365.2422 days, so the excess over 365 days is 0.2422 days."
            },
            {
                "question": "How many days of seasonal drift accumulate over 40 years without any leap adjustments?",
                "options": ["~1 day", "~4.8 days", "~9.69 days", "~40 days"],
                "correct": 2,
                "explanation": "40 × 0.2422 = 9.688 days ≈ 9.69 days (nearly 10 full days of calendar drift!)."
            }
        ]
    },
    {
        "slide_num": 14,
        "section": "4.4 Look Before You Leap!",
        "badge": "Divisibility Hierarchy: 4, 100, 400",
        "title": "The Leap Year Rules: Julian to Gregorian Divisibility",
        "narration": "Adding a leap day every 4 years assumes an average year of 365.25 days, which is slightly too long by 0.0078 days each year! In 100 years, this overshoots by nearly a full day. Thus, astronomers established the three-tier rule: a year is a leap year if divisible by 4, unless divisible by 100, except when divisible by 400! That is why 2000 was a leap year, but 1900 was not!",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-cyan-500/10 border border-cyan-500/30 rounded-xl">
    <h4 class="font-bold text-cyan-300 text-sm mb-1">🏛️ The 3-Tier Divisibility Decision Hierarchy</h4>
    <div class="space-y-2 mt-2 text-xs text-slate-300">
      <div class="p-2 bg-slate-900/60 rounded border border-cyan-500/30">
        <b class="text-emerald-400">Rule 1 (Divisible by 4):</b> Most years divisible by $4$ are leap years ($2024, 2028$).
        <span class="text-slate-400">Average = $365 + \frac{1}{4} = 365.25\text{ days}$.</span>
      </div>
      <div class="p-2 bg-slate-900/60 rounded border border-cyan-500/30">
        <b class="text-amber-400">Rule 2 (Century Exception - Divisible by 100):</b> Century years are <i>NOT</i> leap years ($1700, 1800, 1900, 2100$).
        <span class="text-slate-400">Subtracts $\frac{1}{100}$ day $\implies 365.25 - 0.01 = 365.24\text{ days}$.</span>
      </div>
      <div class="p-2 bg-slate-900/60 rounded border border-cyan-500/30">
        <b class="text-cyan-400">Rule 3 (400-Year Override - Divisible by 400):</b> If divisible by $400$, it <i>IS</i> a leap year ($1600, 2000, 2400$).
        <span class="text-slate-400">Adds $\frac{1}{400}$ day $\implies 365.24 + 0.0025 = \mathbf{365.2425\text{ days}}$!</span>
      </div>
    </div>
  </div>

  <div class="p-3 bg-emerald-500/10 border border-emerald-500/30 rounded-xl text-xs text-slate-300">
    <span class="font-bold text-emerald-300">Astronomical Triumph:</span>
    $$365.2425\text{ (Calendar)} - 365.2422\text{ (Tropical)} = \mathbf{+0.0003\text{ days/year}}$$
    This tiny error of $0.0003$ days per year takes more than $3,300\text{ years}$ to accumulate just one day of error!
  </div>
</div>
""",
        "sim_id": "sim-leap-year-decision-tree",
        "checkpoints": [
            {
                "question": "Was the century year 1900 a leap year?",
                "options": ["Yes, because 1900 is divisible by 4", "No, because 1900 is divisible by 100 but not by 400", "Yes, because it ended in 00", "No, because it was an odd century"],
                "correct": 1,
                "explanation": "Century years must be divisible by 400 to be leap years. 1900 / 400 = 4.75 (not divisible), so 1900 was an ordinary 365-day year."
            },
            {
                "question": "Which of the following upcoming years will be a leap year?",
                "options": ["2026", "2030", "2032", "2100"],
                "correct": 2,
                "explanation": "2032 is divisible by 4 and not a century year, so it is a leap year. 2100 is a century year not divisible by 400."
            }
        ]
    },
    {
        "slide_num": 15,
        "section": "Summary & Puzzle Time",
        "badge": "Sequential Grid Navigation",
        "title": "Summary & Puzzle Time: The Hidato Number Path Grid",
        "narration": "To sharpen our mathematical thinking, the syllabus introduces Hidato, the famous number path puzzle! The goal is to fill the grid with consecutive integers forming a continuous unbroken path. Each number must touch the previous number horizontally, vertically, or diagonally. Let us test our logical agility!",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-indigo-500/10 border border-indigo-500/30 rounded-xl">
    <h4 class="font-bold text-indigo-300 text-sm mb-1">🧩 Rules of the Hidato Number Path Puzzle</h4>
    <p class="text-xs text-slate-300 leading-relaxed">
      In Hebrew, <i>Hida</i> means riddle. Hidato requires completing a grid from $1$ to $N$ with strict adjacency rules:
    </p>
    <div class="mt-2 space-y-1 text-xs text-slate-300">
      <div class="p-2 bg-slate-900/60 rounded">
        <b>1. Complete Sequence:</b> Every integer from $1$ to the maximum cell count must appear exactly once.
      </div>
      <div class="p-2 bg-slate-900/60 rounded">
        <b>2. King's Move Adjacency:</b> Consecutive numbers ($k$ and $k+1$) must be immediate neighbors—horizontally, vertically, or diagonally (like a chess King).
      </div>
      <div class="p-2 bg-slate-900/60 rounded">
        <b>3. Given Anchors:</b> Pre-filled clue cells anchor the path; you must deduce the missing link values between them.
      </div>
    </div>
  </div>

  <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60 text-xs">
    <div class="font-bold text-teal-300 mb-1">Mathematical Strategy: Forward & Backward Traversal</div>
    <p class="text-slate-300 leading-relaxed">
      Look at tight constraints: if cell $12$ is fixed and cell $15$ is three squares away, the path between them is rigidly bounded! Work forwards from known low numbers and backwards from known high numbers.
    </p>
  </div>
</div>
""",
        "sim_id": "sim-hidato-grid-puzzle",
        "checkpoints": [
            {
                "question": "In a Hidato puzzle, which moves are permitted between consecutive numbers k and k+1?",
                "options": ["Only horizontal and vertical moves", "Only diagonal moves", "Horizontal, vertical, and diagonal moves (all 8 directions)", "Knight's L-shaped jumps"],
                "correct": 2,
                "explanation": "Hidato allows movement in all 8 adjacent directions (horizontally, vertically, and diagonally), exactly like a King's move in chess."
            },
            {
                "question": "If cell 7 is at coordinate (2, 2), where can cell 8 be located?",
                "options": ["Only at (2, 3)", "Only at (3, 2)", "Any adjacent cell in the 3×3 surrounding box", "Anywhere on row 2"],
                "correct": 2,
                "explanation": "Cell 8 must be an immediate neighbor of cell 7, meaning any of the up to 8 surrounding adjacent squares."
            }
        ]
    },
    {
        "slide_num": 16,
        "section": "Summary & Puzzle Time",
        "badge": "Kerala School of Mathematics",
        "title": "Heritage of Decimal Precision: Madhava & Infinite Expansions",
        "narration": "Our journey through decimals culminates in the heritage of the Kerala School of Astronomy and Mathematics. In the fourteenth century at Sangamagrama, centuries before European calculus, we discovered infinite series that unlocked the decimal digits of pi and trigonometric ratios to extraordinary precision! Mathematics is a timeless bridge between cosmic harmony and human thought.",
        "theory": r"""
<div class="space-y-4">
  <div class="p-3 bg-amber-500/10 border border-amber-500/30 rounded-xl">
    <h4 class="font-bold text-amber-300 text-sm mb-1">📜 Acharya Madhava of Sangamagrama (c. 1340–1425 CE)</h4>
    <p class="text-xs text-slate-300 leading-relaxed">
      Madhava founded the legendary Kerala School of Astronomy and Mathematics. He was the first in world history to formulate infinite series for $\pi$, sine, and cosine:
    </p>
    <div class="mt-2 text-center text-xs font-mono text-amber-200 bg-slate-900/60 p-2 rounded-lg">
      $$\pi = 4 \left( 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} - \dots \right)$$
    </div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-cyan-300 mb-1">Madhava's 11-Decimal Value of $\pi$</div>
      <p class="text-slate-300 leading-relaxed">
        Using fast-converging transformed series, Madhava calculated $\pi$ accurately to $11$ decimal places:
        $$\pi \approx \mathbf{3.14159265359}$$
        recorded in Sanskrit verse encoded via the Katapayadi numeral system.
      </p>
    </div>
    <div class="p-3 bg-slate-800/60 rounded-xl border border-slate-700/60">
      <div class="font-bold text-emerald-300 mb-1">Summary of Decimal Mastery</div>
      <p class="text-slate-300 leading-relaxed">
        • <b>Multiplication:</b> Sum the decimal places and place the point.<br>
        • <b>Division:</b> Scale divisor to a whole number by multiplying $10^k$.<br>
        • <b>Applications:</b> Governing the calendar year ($365.2422$) & scientific measurements.
      </p>
    </div>
  </div>
</div>
""",
        "sim_id": "sim-madhava-decimal-series",
        "checkpoints": [
            {
                "question": "To how many decimal places did Acharya Madhava compute the value of π in the 14th century?",
                "options": ["2 decimal places", "5 decimal places", "11 decimal places", "100 decimal places"],
                "correct": 2,
                "explanation": "Madhava computed π to 11 correct decimal places (3.14159265359) using his rapidly converging infinite series."
            },
            {
                "question": "Which of the following operations shifts decimal digits to higher place values (to the left)?",
                "options": ["Dividing by 10", "Multiplying by 10", "Subtracting 0.1", "Dividing by 100"],
                "correct": 1,
                "explanation": "Multiplying by 10 multiplies each digit by 10, shifting digits one place to the left into higher place-value columns (moving the decimal point to the right)."
            }
        ]
    },
    {
        "slide_num": 17,
        "section": "Mastery Challenge",
        "badge": "Questions 1–10",
        "title": "Mastery Challenge I: Decimal Recap & Place Value",
        "narration": "Welcome to the first Mastery Challenge slide! Test your understanding of place values, decimal expanded forms, fractions with power-of-ten denominators, and friendly scaling factors. Review each question carefully, select your answer, and open the solution modal for complete step-by-step mathematical proofs!",
        "theory": r"""
<div class="p-3 bg-teal-500/10 border border-teal-500/30 rounded-xl mb-4 text-xs text-slate-300">
  <span class="font-bold text-teal-300">Challenge Instructions:</span> Answer questions 1 through 10 below covering decimal place values, expanded notation, and fraction conversions. Click <b>View Step-by-Step Solution</b> on any question to examine full mathematical proofs.
</div>
""",
        "quiz_range": [1, 10]
    },
    {
        "slide_num": 18,
        "section": "Mastery Challenge",
        "badge": "Questions 11–20",
        "title": "Mastery Challenge II: Decimal Multiplication & Area Grids",
        "narration": "Welcome to Mastery Challenge Part Two! Here we test decimal multiplication, unit square grid area models, placing decimal points, multiplying by powers of ten, and the fascinating magnitude paradoxes where multiplication shrinks numbers!",
        "theory": r"""
<div class="p-3 bg-blue-500/10 border border-blue-500/30 rounded-xl mb-4 text-xs text-slate-300">
  <span class="font-bold text-blue-300">Challenge Instructions:</span> Tackle questions 11 through 20 focusing on decimal multiplication rules, grid models, and power-of-10 shifts. Click <b>View Step-by-Step Solution</b> to inspect complete step-by-step workings.
</div>
""",
        "quiz_range": [11, 20]
    },
    {
        "slide_num": 19,
        "section": "Mastery Challenge",
        "badge": "Questions 21–30",
        "title": "Mastery Challenge III: Decimal Division, Regrouping & 142857",
        "narration": "In Mastery Challenge Part Three, prove your skill with decimal division, dividing by powers of ten, place-value long division regrouping, clearing decimal divisors, and the cyclic wonder of 142857!",
        "theory": r"""
<div class="p-3 bg-purple-500/10 border border-purple-500/30 rounded-xl mb-4 text-xs text-slate-300">
  <span class="font-bold text-purple-300">Challenge Instructions:</span> Work through questions 21 to 30 on decimal division procedures, long division regrouping, and repeating decimals. Detailed solutions are available via the solution button.
</div>
""",
        "quiz_range": [21, 30]
    },
    {
        "slide_num": 20,
        "section": "Mastery Challenge",
        "badge": "Questions 31–40",
        "title": "Mastery Challenge IV: Leap Years, Hidato & Grand Finale",
        "narration": "Heartiest congratulations on reaching the final mastery stage! Questions 31 through 40 challenge you on astronomical decimals, leap year divisibility rules, Hidato puzzle strategies, and comprehensive real-world applications. You have mastered Another Peek Beyond the Point!",
        "theory": r"""
<div class="p-3 bg-amber-500/10 border border-amber-500/30 rounded-xl mb-4 text-xs text-slate-300">
  <span class="font-bold text-amber-300">Final Challenge Instructions:</span> Complete the final 10 questions on leap year astronomy (365.2422 days), divisibility rules (4, 100, 400), and Hidato logic puzzles. Celebrate your mastery of Decimals!
</div>
""",
        "quiz_range": [31, 40]
    }
]

# 40 Comprehensive Quiz Questions with detailed KaTeX solutions
quiz_questions = [
    # Q1-Q10: Decimal Recap, Place Value & Expanded Notation
    {
        "id": 1,
        "question": "What is the place value of digit 5 in the number 38.452?",
        "options": ["5 tens", "5 tenths", "5 hundredths", "5 thousandths"],
        "correct": 2,
        "solution": r"""
$$\textbf{Step-by-Step Place Value Determination:}$$
1. Look at the positions of the digits relative to the decimal point in $38.452$:
   - $3$: Tens column ($3 \times 10 = 30$)
   - $8$: Ones column ($8 \times 1 = 8$)
   - $\mathbf{.}$: Decimal point separator
   - $4$: Tenths column ($\frac{4}{10} = 0.4$)
   - $\mathbf{5}$: Hundredths column ($\frac{5}{100} = \mathbf{0.05}$)
   - $2$: Thousandths column ($\frac{2}{1000} = 0.002$)
2. Therefore, the digit $5$ represents $\mathbf{5\text{ hundredths}}$ ($\frac{5}{100}$).
"""
    },
    {
        "id": 2,
        "question": "What is the standard decimal representation of: 70 + 6 + 4/10 + 9/1000?",
        "options": ["76.49", "76.409", "76.049", "764.09"],
        "correct": 1,
        "solution": r"""
$$\textbf{Reconstructing Expanded Notation:}$$
1. Whole number part: $70 + 6 = 76$.
2. Tenths position: $\frac{4}{10} = 0.4 \implies$ digit $4$ in the first decimal place.
3. Hundredths position: Not present in the sum $\implies$ digit $\mathbf{0}$ in the second decimal place.
4. Thousandths position: $\frac{9}{1000} = 0.009 \implies$ digit $9$ in the third decimal place.
5. Combining all slots: $76 + 0.4 + 0.00 + 0.009 = \mathbf{76.409}$.
"""
    },
    {
        "id": 3,
        "question": "Convert 3/8 into a decimal using the friendly factor scaling method.",
        "options": ["0.375", "0.38", "0.35", "0.125"],
        "correct": 0,
        "solution": r"""
$$\textbf{Scaling Denominators by Prime Factors:}$$
1. Denominator $8 = 2 \times 2 \times 2 = 2^3$.
2. To scale to a power of ten ($10^3 = 1000$), multiply numerator and denominator by $5^3 = 125$:
   $$\frac{3}{8} = \frac{3 \times 125}{8 \times 125} = \frac{375}{1000}$$
3. Since the denominator has $3$ zeroes, move the decimal point $3$ places from the right:
   $$\frac{375}{1000} = \mathbf{0.375}$$
"""
    },
    {
        "id": 4,
        "question": "How many paise are in ₹14.05?",
        "options": ["145 paise", "1405 paise", "140.5 paise", "1450 paise"],
        "correct": 1,
        "solution": r"""
$$\textbf{Currency Conversion: Rupees to Paise:}$$
1. $1\text{ Rupee} = 100\text{ paise}$.
2. To convert Rupees to paise, multiply by $100$:
   $$\text{Rs. } 14.05 \times 100 = 1405\text{ paise}$$
3. Notice that $0.05\text{ Rupees} = 5\text{ paise}$, so $14\text{ Rupees} + 5\text{ paise} = 1400 + 5 = \mathbf{1405\text{ paise}}$.
"""
    },
    {
        "id": 5,
        "question": "Which of the following decimals is equivalent to 7/25?",
        "options": ["0.7", "0.28", "0.14", "0.028"],
        "correct": 1,
        "solution": r"""
$$\textbf{Scaling Denominator 25 to 100:}$$
1. Multiply numerator and denominator by $4$:
   $$\frac{7}{25} = \frac{7 \times 4}{25 \times 4} = \frac{28}{100}$$
2. With $2$ zeroes in the denominator:
   $$\frac{28}{100} = \mathbf{0.28}$$
"""
    },
    {
        "id": 6,
        "question": "Express 45 mm in meters using decimals.",
        "options": ["0.45 m", "0.045 m", "4.5 m", "0.0045 m"],
        "correct": 1,
        "solution": r"""
$$\textbf{Metric Conversion: Millimeters to Meters:}$$
1. $1\text{ cm} = 10\text{ mm}$ and $1\text{ m} = 100\text{ cm} = 1000\text{ mm}$.
2. Therefore, $1\text{ mm} = \frac{1}{1000}\text{ m}$.
3. For $45\text{ mm}$:
   $$45\text{ mm} = \frac{45}{1000}\text{ m} = \mathbf{0.045\text{ m}}$$
"""
    },
    {
        "id": 7,
        "question": "Which statement about trailing zeroes in decimals is correct?",
        "options": [
            "0.60 is ten times larger than 0.6",
            "0.6 = 0.60 = 0.600",
            "Appending trailing zeroes always changes the fraction",
            "0.06 is equal to 0.60"
        ],
        "correct": 1,
        "solution": r"""
$$\textbf{Invariance of Trailing Zeroes:}$$
1. $0.6 = \frac{6}{10}$.
2. $0.60 = \frac{60}{100} = \frac{6}{10}$.
3. $0.600 = \frac{600}{1000} = \frac{6}{10}$.
4. Appending zeroes at the extreme right of the fractional part does not alter value: $\mathbf{0.6 = 0.60 = 0.600}$.
"""
    },
    {
        "id": 8,
        "question": "Convert the mixed fraction 5 3/100 to a decimal.",
        "options": ["5.3", "5.03", "5.003", "53.0"],
        "correct": 1,
        "solution": r"""
$$\textbf{Converting Mixed Fractions:}$$
1. Whole number part = $5$.
2. Fractional part = $\frac{3}{100} = 0.03$.
3. Sum = $5 + 0.03 = \mathbf{5.03}$.
"""
    },
    {
        "id": 9,
        "question": "What is the expanded form of 0.804?",
        "options": [
            "8/10 + 4/100",
            "8/10 + 4/1000",
            "8/100 + 4/1000",
            "8 + 4/10"
        ],
        "correct": 1,
        "solution": r"""
$$\textbf{Decomposing 0.804:}$$
1. Tenths digit = $8 \implies \frac{8}{10}$.
2. Hundredths digit = $0 \implies 0$.
3. Thousandths digit = $4 \implies \frac{4}{1000}$.
4. Expanded form = $\mathbf{\frac{8}{10} + \frac{4}{1000}}$.
"""
    },
    {
        "id": 10,
        "question": "Which fraction equals 0.025 in lowest terms?",
        "options": ["1/4", "1/25", "1/40", "1/400"],
        "correct": 2,
        "solution": r"""
$$\textbf{Fraction Reduction to Lowest Terms:}$$
1. $0.025 = \frac{25}{1000}$.
2. Divide numerator and denominator by $\text{GCD}(25, 1000) = 25$:
   $$\frac{25 \div 25}{1000 \div 25} = \mathbf{\frac{1}{40}}$$
"""
    },

    # Q11-Q20: Decimal Multiplication & Area Grids
    {
        "id": 11,
        "question": "What is 0.7 × 8?",
        "options": ["0.56", "5.6", "56.0", "0.056"],
        "correct": 1,
        "solution": r"""
$$\textbf{Decimal by Whole Number Multiplication:}$$
1. Ignore the decimal point: $7 \times 8 = 56$.
2. Count decimal places: $0.7$ has $1$ decimal place, $8$ has $0$ decimal places. Total = $1$ place.
3. Place the decimal point $1$ place from the right:
   $$56 \to \mathbf{5.6}$$
"""
    },
    {
        "id": 12,
        "question": "In a 10×10 unit grid, a shaded rectangle has length 0.8 and width 0.5. How many small hundredth squares are shaded?",
        "options": ["4 squares", "13 squares", "40 squares", "85 squares"],
        "correct": 2,
        "solution": r"""
$$\textbf{Area Model in 10×10 Grid:}$$
1. Length $0.8 = 8\text{ rows of tenths}$.
2. Width $0.5 = 5\text{ columns of tenths}$.
3. Number of small hundredth squares = $8 \times 5 = \mathbf{40\text{ squares}}$.
4. Fraction of total unit area = $\frac{40}{100} = \mathbf{0.40} = 0.4$.
"""
    },
    {
        "id": 13,
        "question": "What is 0.3 × 0.4?",
        "options": ["1.2", "0.12", "0.012", "0.0012"],
        "correct": 1,
        "solution": r"""
$$\textbf{Multiplying Decimals:}$$
1. $3 \times 4 = 12$.
2. Decimal places in factor 1 ($0.3$) = $1$.
3. Decimal places in factor 2 ($0.4$) = $1$.
4. Total decimal places = $1 + 1 = 2$.
5. Placing $2$ places from the right: $12 \to \mathbf{0.12}$.
"""
    },
    {
        "id": 14,
        "question": "Calculate 0.04 × 0.09.",
        "options": ["0.36", "0.036", "0.0036", "0.00036"],
        "correct": 2,
        "solution": r"""
$$\textbf{Multiplication with Leading Zeroes:}$$
1. Multiply whole numbers: $4 \times 9 = 36$.
2. Count decimal places: $0.04$ has $2$ places, $0.09$ has $2$ places. Total = $2 + 2 = 4$ decimal places.
3. Number of digits in $36$ is only $2$. We must prefix $4 - 2 = 2$ leading zeroes:
   $$36 \to \mathbf{0.0036}$$
"""
    },
    {
        "id": 15,
        "question": "What is 2.35 × 1000?",
        "options": ["235", "2350", "23500", "23.5"],
        "correct": 1,
        "solution": r"""
$$\textbf{Multiplying by Powers of 10:}$$
1. $1000$ has $3$ zeroes, so shift the decimal point $3$ places to the right.
2. Starting from $2.35$:
   - 1 place right: $23.5$
   - 2 places right: $235.$
   - 3 places right: append zero $\to \mathbf{2350}$.
"""
    },
    {
        "id": 16,
        "question": "If a car travels 16.5 km on 1 liter of petrol, how far will it travel on 4.5 liters?",
        "options": ["74.25 km", "72.25 km", "66.0 km", "742.5 km"],
        "correct": 0,
        "solution": r"""
$$\textbf{Word Problem: Distance Traveled:}$$
1. Distance = $\text{Mileage} \times \text{Fuel} = 16.5 \times 4.5$.
2. Multiply without points:
   $$165 \times 45 = 165 \times (40 + 5) = 6600 + 825 = 7425$$
3. Total decimal places = $1$ (in 16.5) + $1$ (in 4.5) = $2$ places.
4. Insert decimal point: $7425 \to \mathbf{74.25\text{ km}}$.
"""
    },
    {
        "id": 17,
        "question": "Which of the following products is SMALLER than 0.6?",
        "options": ["0.6 × 1.2", "0.6 × 2.0", "0.6 × 0.8", "0.6 × 10"],
        "correct": 2,
        "solution": r"""
$$\textbf{Magnitude Rules of Multiplication:}$$
1. Multiplying by a factor $> 1$ increases the magnitude: $0.6 \times 1.2 = 0.72 \gt 0.6$.
2. Multiplying by a factor $< 1$ decreases the magnitude:
   $$0.6 \times 0.8 = \mathbf{0.48} \lt 0.6$$
3. Therefore, $0.6 \times 0.8$ is smaller than $0.6$.
"""
    },
    {
        "id": 18,
        "question": "What is 1.1 × 1.1 × 1.1?",
        "options": ["1.331", "13.31", "1.21", "1.111"],
        "correct": 0,
        "solution": r"""
$$\textbf{Repeated Decimal Multiplication:}$$
1. First product: $1.1 \times 1.1 = 1.21$ ($1+1=2$ decimal places).
2. Second product: $1.21 \times 1.1$.
   - Integer multiplication: $121 \times 11 = 1331$.
   - Total decimal places: $2 + 1 = 3$ places.
3. Placing decimal point: $1331 \to \mathbf{1.331}$.
"""
    },
    {
        "id": 19,
        "question": "Find the area of a rectangle with length 7.2 cm and breadth 3.5 cm.",
        "options": ["25.2 sq cm", "252 sq cm", "24.5 sq cm", "21.7 sq cm"],
        "correct": 0,
        "solution": r"""
$$\textbf{Rectangle Area Calculation:}$$
1. $\text{Area} = \text{Length} \times \text{Breadth} = 7.2 \times 3.5$.
2. Multiply without points:
   $$72 \times 35 = 72 \times (30 + 5) = 2160 + 360 = 2520$$
3. Decimal places = $1 + 1 = 2$.
4. Placing point: $2520 \to 25.20 = \mathbf{25.2\text{ sq cm}}$.
"""
    },
    {
        "id": 20,
        "question": "What is 0.002 × 500?",
        "options": ["10", "1", "0.1", "0.01"],
        "correct": 1,
        "solution": r"""
$$\textbf{Product with Trailing Zeroes:}$$
1. Multiply integers: $2 \times 500 = 1000$.
2. Decimal places in $0.002 = 3$, in $500 = 0$. Total = $3$ places.
3. Placing decimal point $3$ places from the right:
   $$1000 \to 1.000 = \mathbf{1}$$
"""
    },

    # Q21-Q30: Decimal Division, Regrouping & 142857
    {
        "id": 21,
        "question": "What is 34.8 ÷ 100?",
        "options": ["3.48", "0.348", "0.0348", "348.0"],
        "correct": 1,
        "solution": r"""
$$\textbf{Division by Powers of 10:}$$
1. Dividing by $100$ ($2$ zeroes) shifts the decimal point $2$ places to the left.
2. $34.8 \to 3.48 \to \mathbf{0.348}$.
"""
    },
    {
        "id": 22,
        "question": "Calculate 15.6 ÷ 4 using place-value division.",
        "options": ["3.9", "39.0", "0.39", "3.4"],
        "correct": 0,
        "solution": r"""
$$\textbf{Place-Value Long Division:}$$
1. Divide ones: $15 \div 4 = \mathbf{3}$ with remainder $3\text{ ones}$.
2. Place decimal point in quotient: $\mathbf{3.}$
3. Regroup $3\text{ ones} = 30\text{ tenths}$.
4. Add $6\text{ tenths} = 36\text{ tenths}$.
5. Divide tenths: $36 \div 4 = \mathbf{9}\text{ tenths}$.
6. Final Quotient = $\mathbf{3.9}$.
"""
    },
    {
        "id": 23,
        "question": "What is 4.8 ÷ 0.12?",
        "options": ["4", "40", "0.4", "400"],
        "correct": 1,
        "solution": r"""
$$\textbf{Clearing Decimal Divisors:}$$
1. Express as fraction: $\frac{4.8}{0.12}$.
2. Multiply numerator and denominator by $100$ to make the divisor an integer:
   $$\frac{4.8 \times 100}{0.12 \times 100} = \frac{480}{12}$$
3. Perform integer division:
   $$\frac{480}{12} = \mathbf{40}$$
"""
    },
    {
        "id": 24,
        "question": "What is 7.5 ÷ 1.5?",
        "options": ["5", "0.5", "50", "0.05"],
        "correct": 0,
        "solution": r"""
$$\textbf{Clearing Decimal Divisor:}$$
1. Multiply numerator and denominator by $10$:
   $$\frac{7.5 \times 10}{1.5 \times 10} = \frac{75}{15}$$
2. Divide:
   $$\frac{75}{15} = \mathbf{5}$$
"""
    },
    {
        "id": 25,
        "question": "Divide 3 by 8 to obtain a terminating decimal.",
        "options": ["0.375", "0.38", "0.35", "0.425"],
        "correct": 0,
        "solution": r"""
$$\textbf{Long Division of 3 by 8:}$$
1. $3 \div 8 = 0$ with remainder $3$.
2. Regroup $3\text{ ones} = 30\text{ tenths}$. $30 \div 8 = \mathbf{3}$ tenths remainder $6$ tenths.
3. Regroup $6\text{ tenths} = 60\text{ hundredths}$. $60 \div 8 = \mathbf{7}$ hundredths remainder $4$ hundredths.
4. Regroup $4\text{ hundredths} = 40\text{ thousandths}$. $40 \div 8 = \mathbf{5}$ thousandths remainder $0$.
5. Quotient = $\mathbf{0.375}$.
"""
    },
    {
        "id": 26,
        "question": "Which of the following divisions yields a quotient LARGER than the dividend?",
        "options": ["12 ÷ 3", "12 ÷ 1.5", "12 ÷ 0.4", "12 ÷ 10"],
        "correct": 2,
        "solution": r"""
$$\textbf{Magnification Paradox in Division:}$$
1. When dividing by a positive number $< 1$, the quotient is strictly greater than the dividend:
   $$12 \div 0.4 = \frac{120}{4} = \mathbf{30} \gt 12$$
2. In all other choices, the divisor $> 1$, so the quotient is smaller than $12$.
"""
    },
    {
        "id": 27,
        "question": "What is the repeating cycle of digits in the decimal expansion of 1/7?",
        "options": ["142857", "285714", "123456", "141414"],
        "correct": 0,
        "solution": r"""
$$\textbf{The Cyclic Wheel of 1/7:}$$
1. Performing long division $1 \div 7$:
   - $10 \div 7 = 1$ rem $3$
   - $30 \div 7 = 4$ rem $2$
   - $20 \div 7 = 2$ rem $6$
   - $60 \div 7 = 8$ rem $4$
   - $40 \div 7 = 5$ rem $5$
   - $50 \div 7 = 7$ rem $1$ (remainder 1 repeats the cycle!)
2. Therefore: $\frac{1}{7} = 0.\overline{\mathbf{142857}}$.
"""
    },
    {
        "id": 28,
        "question": "If 1/7 = 0.142857..., what is the decimal expansion of 2/7?",
        "options": ["0.285714...", "0.246810...", "0.142857...", "0.571428..."],
        "correct": 0,
        "solution": r"""
$$\textbf{Cyclic Permutation for 2/7:}$$
1. Since $2 \div 7 = 0.285714\dots$, the cycle starts at the second-smallest digit in the sequence $\{1, 2, 4, 5, 7, 8\}$, which is $\mathbf{2}$.
2. Following the circle from $2$: $2 \to 8 \to 5 \to 7 \to 1 \to 4$.
3. Thus, $\frac{2}{7} = 0.\overline{\mathbf{285714}}$.
"""
    },
    {
        "id": 29,
        "question": "A rope of length 18.75 meters is cut into 5 equal pieces. What is the length of each piece?",
        "options": ["3.55 m", "3.75 m", "3.65 m", "3.85 m"],
        "correct": 1,
        "solution": r"""
$$\textbf{Word Problem: Rope Slicing:}$$
1. $\text{Piece length} = 18.75 \div 5$.
2. $18 \div 5 = 3$ remainder $3$.
3. $37\text{ tenths} \div 5 = 7$ remainder $2$.
4. $25\text{ hundredths} \div 5 = 5$ remainder $0$.
5. Length of each piece = $\mathbf{3.75\text{ meters}}$.
"""
    },
    {
        "id": 30,
        "question": "Which fraction does NOT produce a terminating decimal?",
        "options": ["7/16", "9/20", "5/12", "11/25"],
        "correct": 2,
        "solution": r"""
$$\textbf{Prime Factorisation Test for Terminating Decimals:}$$
1. A fraction in lowest terms terminates if and only if its denominator's prime factors are strictly $2$ and/or $5$.
   - $16 = 2^4 \implies$ Terminates.
   - $20 = 2^2 \times 5 \implies$ Terminates.
   - $12 = 2^2 \times \mathbf{3} \implies$ Has factor $3$, so it is **recurring/non-terminating**!
   - $25 = 5^2 \implies$ Terminates.
2. Therefore, $\mathbf{5/12}$ does not terminate ($5/12 = 0.41\bar{6}$).
"""
    },

    # Q31-Q40: Leap Years, Hidato & Synthesis
    {
        "id": 31,
        "question": "What is the exact approximate length of the astronomical tropical year?",
        "options": ["365.0000 days", "365.2500 days", "365.2422 days", "366.1250 days"],
        "correct": 2,
        "solution": r"""
$$\textbf{Astronomical Tropical Year:}$$
1. The exact time Earth takes to complete one revolution around the Sun (from equinox to equinox) is approximately:
   $$\mathbf{365.2422\text{ solar days}}$$
2. This is equal to $365\text{ days } 5\text{ hours } 48\text{ minutes } 46\text{ seconds}$.
"""
    },
    {
        "id": 32,
        "question": "Why was the century year 2000 a leap year while 1900 was NOT a leap year?",
        "options": [
            "2000 was an even century while 1900 was odd",
            "2000 is divisible by 400, whereas 1900 is not",
            "1900 had a calendar strike",
            "2000 was the start of a new millennium"
        ],
        "correct": 1,
        "solution": r"""
$$\textbf{The 400-Year Gregorian Leap Rule:}$$
1. A century year (ending in $00$, divisible by $100$) is a leap year **only if** it is divisible by $400$.
2. For $1900$: $\frac{1900}{400} = 4.75 \implies$ Not divisible by $400 \implies$ **Not a leap year**.
3. For $2000$: $\frac{2000}{400} = 5 \implies$ Divisible by $400 \implies$ **Leap year**!
"""
    },
    {
        "id": 33,
        "question": "Under the Julian calendar (1 leap day every 4 years = 365.25 days), what was the annual error compared to 365.2422 days?",
        "options": ["+0.0078 days", "-0.2422 days", "+0.0003 days", "+0.2500 days"],
        "correct": 0,
        "solution": r"""
$$\textbf{Julian Calendar Error Calculation:}$$
1. Julian average year = $365.25\text{ days}$.
2. Actual tropical year = $365.2422\text{ days}$.
3. Annual error:
   $$365.25 - 365.2422 = \mathbf{+0.0078\text{ days/year}}$$
4. In $128$ years, this surplus accumulated to $1$ full day of error ($0.0078 \times 128 \approx 1$).
"""
    },
    {
        "id": 34,
        "question": "Under the complete Gregorian leap rules, what is the average length of a calendar year?",
        "options": ["365.25 days", "365.24 days", "365.2425 days", "365.2422 days"],
        "correct": 2,
        "solution": r"""
$$\textbf{Average Gregorian Calendar Year Length:}$$
1. In any $400$-year block:
   - $400$ base years of $365$ days.
   - Add $100$ leap days ($\div 4$).
   - Subtract $4$ century days ($\div 100$).
   - Add $1$ 400-year day ($\div 400$).
   - Total leap days = $100 - 4 + 1 = 97\text{ leap days}$.
2. Average year:
   $$365 + \frac{97}{400} = 365 + 0.2425 = \mathbf{365.2425\text{ days}}$$
"""
    },
    {
        "id": 35,
        "question": "Will the year 2100 be a leap year?",
        "options": ["Yes, because 2100 is divisible by 4", "No, because 2100 is divisible by 100 but not by 400", "Yes, because it is an even century", "Cannot be determined"],
        "correct": 1,
        "solution": r"""
$$\textbf{Testing Year 2100:}$$
1. $2100$ is divisible by $100$ (it is a century year).
2. Test divisibility by $400$:
   $$\frac{2100}{400} = 5.25 \quad (\text{not an integer!})$$
3. Because century years must be divisible by $400$ to be leap years, $2100$ will be an ordinary year of $365$ days ($\mathbf{No}$).
"""
    },
    {
        "id": 36,
        "question": "In a Hidato number path puzzle, if number 15 is in cell (3, 3), how many potential neighbor cells could hold number 16?",
        "options": ["4 cells", "6 cells", "Up to 8 cells", "16 cells"],
        "correct": 2,
        "solution": r"""
$$\textbf{Hidato Adjacency Geometry:}$$
1. Hidato moves allow horizontal, vertical, and diagonal steps (King's moves).
2. For an interior cell $(r, c)$, its neighbors are:
   $$(r \pm 1, c), \quad (r, c \pm 1), \quad (r \pm 1, c \pm 1)$$
3. This creates a $3 \times 3$ surrounding ring excluding the center cell, giving $\mathbf{\text{up to } 8\text{ cells}}$.
"""
    },
    {
        "id": 37,
        "question": "Evaluate: (0.2 × 0.2) + (0.3 × 0.3).",
        "options": ["0.13", "0.25", "1.3", "0.013"],
        "correct": 0,
        "solution": r"""
$$\textbf{Evaluating Combined Arithmetic Expression:}$$
1. First term: $0.2 \times 0.2 = 0.04$.
2. Second term: $0.3 \times 0.3 = 0.09$.
3. Sum = $0.04 + 0.09 = \mathbf{0.13}$.
"""
    },
    {
        "id": 38,
        "question": "What is 0.5 ÷ 0.05 + 0.5 × 0.05?",
        "options": ["10.025", "1.025", "100.25", "10.25"],
        "correct": 0,
        "solution": r"""
$$\textbf{Step-by-Step Order of Operations:}$$
1. Division term: $0.5 \div 0.05 = \frac{0.5 \times 100}{0.05 \times 100} = \frac{50}{5} = \mathbf{10}$.
2. Multiplication term: $0.5 \times 0.05 = \mathbf{0.025}$.
3. Sum = $10 + 0.025 = \mathbf{10.025}$.
"""
    },
    {
        "id": 39,
        "question": "A container holds 3.75 liters of water. How many 0.25-liter glasses can be completely filled from it?",
        "options": ["12 glasses", "15 glasses", "16 glasses", "25 glasses"],
        "correct": 1,
        "solution": r"""
$$\textbf{Measurement Word Problem:}$$
1. Number of glasses = $\frac{\text{Total volume}}{\text{Glass volume}} = \frac{3.75}{0.25}$.
2. Multiply numerator and denominator by $100$:
   $$\frac{375}{25} = \mathbf{15\text{ glasses}}$$
"""
    },
    {
        "id": 40,
        "question": "Which Indian mathematician from the Kerala School of Astronomy pioneered infinite series for decimal values of π and trigonometry?",
        "options": [
            "Acharya Aryabhata",
            "Acharya Brahmagupta",
            "Acharya Madhava of Sangamagrama",
            "Acharya Bhaskara II"
        ],
        "correct": 2,
        "solution": r"""
$$\textbf{Heritage of Decimal Mathematics:}$$
1. **Acharya Madhava of Sangamagrama** (c. 1340–1425 CE) in Kerala discovered the power series for $\pi$, sine, and cosine centuries before Gregory, Leibniz, and Newton.
2. He used these series to calculate $\pi \approx 3.14159265359$ ($11$ decimal places).
3. Therefore, the correct answer is **Acharya Madhava of Sangamagrama**.
"""
    }
]

output_path = '.agents/class7_math_another_peek_beyond_the_point_data.py'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""\n')
    f.write('Data module for Class 7 Mathematics - Another Peek Beyond the Point\n')
    f.write('Generated automatically.\n')
    f.write('"""\n\n')
    f.write("SLIDES_DATA = " + repr(slides_data) + "\n\n")
    f.write("QUIZ_QUESTIONS = " + repr(quiz_questions) + "\n")

print(f"Generated {output_path} successfully!")
print(f"Total slides: {len(slides_data)}, Total quiz questions: {len(quiz_questions)}")

