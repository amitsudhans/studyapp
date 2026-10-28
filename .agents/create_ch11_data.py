# -*- coding: utf-8 -*-
"""
Script to create .agents/class7_math_finding_common_ground_data.py
Contains 20 slides, 32 checkpoints, and 40 quiz questions with step-by-step solutions.
"""

import json

SLIDES_DATA = [
    {
        "slide_num": 1,
        "section": "3.1 HCF Foundations",
        "badge": "Floor Tiling & Rice Packing",
        "title": "Finding Common Ground: The Floor Tile & Rice Packing Dilemma",
        "narration": "Welcome, young mathematicians! I am Acharya Mahāvīrācārya. Today we embark on a thrilling quest to discover Common Ground—the harmony of factors and multiples that bridges disparate quantities!",
        "theory": r"""
          <p class="mb-3">
            In everyday life, we constantly seek the <strong>largest common measure</strong> that divides different quantities without waste:
          </p>
          <div class="space-y-2 mb-3 text-xs">
            <div class="p-2.5 rounded bg-amber-950/40 border border-amber-500/30">
              <strong class="text-amber-300 block mb-1">🏠 The Floor Tiler's Dilemma:</strong>
              A courtyard measures $12\text{ m}$ long and $18\text{ m}$ wide. You wish to pave it entirely with identical square tiles with zero cuts. The tile side must divide both $12$ and $18$ perfectly:
              $$\text{Divisors of } 12: \{1, 2, 3, 4, 6, 12\}, \quad \text{Divisors of } 18: \{1, 2, 3, 6, 9, 18\}$$
              Common tile sizes are $1\text{m}, 2\text{m}, 3\text{m},$ or $6\text{m}$. To use the <em>fewest</em> tiles, pick the <strong>largest</strong>: $6\text{ m} \times 6\text{ m}$!
            </div>
            <div class="p-2.5 rounded bg-emerald-950/40 border border-emerald-500/30">
              <strong class="text-emerald-300 block mb-1">🌾 The Rice Packing Challenge:</strong>
              A merchant has $24\text{ kg}$ of Basmati and $36\text{ kg}$ of Sona Masoori rice. To pack all rice into identical bags of equal weight with no mixing:
              $$\text{Maximum bag capacity} = \text{HCF}(24, 36) = 12\text{ kg}$$
            </div>
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Common Divisor</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Highest Common Factor (HCF)</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Tiling Optimization</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">Zero Waste</span>
          </div>
        """,
        "sim_id": "sim-floor-tiler",
        "checkpoints": [
            {
                "id": "1.1",
                "question": "A room of dimensions $15\text{ m} \times 20\text{ m}$ is paved with square tiles. What is the largest possible tile side length without cutting?",
                "options": ["$3\text{ m}$", "$4\text{ m}$", "$5\text{ m}$", "$10\text{ m}$"],
                "correct": 2,
                "explanation": "Factors of 15 are {1, 3, 5, 15}. Factors of 20 are {1, 2, 4, 5, 10, 20}. The greatest common factor is 5 m!"
            },
            {
                "id": "1.2",
                "question": "How many $5\text{ m} \times 5\text{ m}$ square tiles are needed to pave the $15\text{ m} \times 20\text{ m}$ room?",
                "options": ["$7$", "$12$", "$15$", "$35$"],
                "correct": 1,
                "explanation": "Along length: $20 / 5 = 4$ tiles. Along width: $15 / 5 = 3$ tiles. Total tiles $= 4 \times 3 = 12$ tiles!"
            }
        ]
    },
    {
        "slide_num": 2,
        "section": "3.1 Definition of HCF",
        "badge": "Common Divisors & Venn Sets",
        "title": "The Highest Common Factor: Intersection of Factor Sets",
        "narration": "A factor is an exact divisor that leaves zero remainder. When we collect the factor sets of two numbers, their intersection reveals the shared territory. The maximum element in this intersection is crowned the Highest Common Factor!",
        "theory": r"""
          <p class="mb-3">
            The <strong>Highest Common Factor (HCF)</strong>, also called the <strong>Greatest Common Divisor (GCD)</strong>, of two or more numbers is the greatest number that divides each of them without remainder.
          </p>
          <div class="p-3 rounded-lg bg-slate-900/70 border border-slate-700 mb-3 text-xs text-slate-300 space-y-1.5">
            <p><strong>Set-Theoretic Definition:</strong></p>
            <p>• Let $F(a)$ be the set of all positive factors of $a$.</p>
            <p>• Let $F(b)$ be the set of all positive factors of $b$.</p>
            <p>• The set of Common Factors is the intersection: $F(a) \cap F(b)$.</p>
            <p>• The HCF is the maximum element: $\text{HCF}(a, b) = \max(F(a) \cap F(b))$.</p>
          </div>
          <div class="p-3 rounded-lg bg-sky-950/40 border border-sky-500/30 text-xs text-sky-200">
            <strong>Example for 24 and 36:</strong><br>
            $F(24) = \{1, 2, 3, 4, 6, 8, 12, 24\}$<br>
            $F(36) = \{1, 2, 3, 4, 6, 9, 12, 18, 36\}$<br>
            $F(24) \cap F(36) = \{1, 2, 3, 4, 6, 12\} \implies \mathbf{\text{HCF} = 12}$.
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Factor Set $F(n)$</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Set Intersection ($\cap$)</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Max Element</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">Zero Remainder</span>
          </div>
        """,
        "sim_id": "sim-factor-venn",
        "checkpoints": [
            {
                "id": "2.1",
                "question": "What is the complete set of common factors for $18$ and $30$?",
                "options": ["$\{1, 2, 3, 6\}$", "$\{1, 3, 6\}$", "$\{2, 6\}$", "$\{1, 2, 3, 6, 9\}$"],
                "correct": 0,
                "explanation": "Factors of 18 are {1,2,3,6,9,18}. Factors of 30 are {1,2,3,5,6,10,15,30}. Their intersection is {1, 2, 3, 6}!"
            },
            {
                "id": "2.2",
                "question": "What is the HCF of $45$ and $60$?",
                "options": ["$5$", "$9$", "$15$", "$30$"],
                "correct": 2,
                "explanation": "Common factors of 45 and 60 are {1, 3, 5, 15}. The greatest is 15!"
            }
        ]
    },
    {
        "slide_num": 3,
        "section": "3.1 Prime Factorisation",
        "badge": "Atomic Primes & Trees",
        "title": "Prime Factor Trees & The Fundamental Theorem of Arithmetic",
        "narration": "Primes are the indivisible atoms of arithmetic! Just as every molecule is built of elemental atoms, every composite integer can be uniquely disassembled into prime building blocks. This is the bedrock of number theory.",
        "theory": r"""
          <p class="mb-3">
            A <strong>Prime Number</strong> has exactly two distinct positive divisors: $1$ and itself ($\{2, 3, 5, 7, 11, 13, \dots\}$).
          </p>
          <div class="p-3 rounded-lg bg-emerald-950/40 border border-emerald-500/30 mb-3 text-xs text-emerald-200">
            <strong>The Fundamental Theorem of Arithmetic:</strong><br>
            Every integer greater than $1$ either is a prime itself or can be represented as the product of prime numbers uniquely, up to the order of the factors:
            $$n = p_1^{a_1} \times p_2^{a_2} \times \dots \times p_k^{a_k}$$
          </div>
          <div class="p-3 rounded-lg bg-slate-900/70 border border-slate-700 text-xs text-slate-300 space-y-1.5">
            <p><strong>Decomposing $60$ via Factor Tree:</strong></p>
            <p>• Branch 1: $60 = 6 \times 10$</p>
            <p>• Branch 2: $6 = 2 \times 3$, and $10 = 2 \times 5$</p>
            <p>• Prime Leaves: $2 \times 2 \times 3 \times 5 = 2^2 \times 3 \times 5$. No matter how you branch, the prime leaves are always identical!</p>
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Prime Atoms</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Factor Trees</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Unique Factorisation</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">Prime Powers</span>
          </div>
        """,
        "sim_id": "sim-prime-factor-tree",
        "checkpoints": [
            {
                "id": "3.1",
                "question": "What is the unique prime factorisation of $72$?",
                "options": ["$2^3 \\times 3^2$", "$2^2 \\times 3^3$", "$8 \\times 9$", "$2^4 \\times 3$"],
                "correct": 0,
                "explanation": "$72 = 8 \\times 9 = 2 \\times 2 \\times 2 \\times 3 \\times 3 = 2^3 \\times 3^2$."
            },
            {
                "id": "3.2",
                "question": "Can a composite number produce two fundamentally different sets of prime factors depending on how you split the tree?",
                "options": ["Yes, if you choose different branches", "No, the prime factorisation is always unique by the Fundamental Theorem of Arithmetic", "Only for odd numbers", "Only for square numbers"],
                "correct": 1,
                "explanation": "The Fundamental Theorem of Arithmetic proves that the prime decomposition is completely unique!"
            }
        ]
    },
    {
        "slide_num": 4,
        "section": "3.1 HCF via Primes",
        "badge": "Minimum Power Overlap",
        "title": "HCF by Prime Factorisation: Minimum Exponent Overlap",
        "narration": "To find the HCF from prime factorisations, you extract only the common prime bases, each raised to the smallest exponent found in either number. This extracts the exact shared core!",
        "theory": r"""
          <p class="mb-3">
            To find the <strong>HCF</strong> using prime powers:
          </p>
          <div class="p-3 rounded-lg bg-slate-900/70 border border-slate-700 mb-3 text-xs text-slate-300 space-y-2">
            <p>1. Express each number in prime factor power notation:</p>
            $$a = p_1^{x_1} \cdot p_2^{x_2} \cdots \quad \text{and} \quad b = p_1^{y_1} \cdot p_2^{y_2} \cdots$$
            <p>2. For every common prime base, select the <strong>minimum exponent</strong>: $\min(x_i, y_i)$.</p>
            <p>3. Multiply these minimum powers together:</p>
            $$\mathbf{\text{HCF}(a, b) = p_1^{\min(x_1, y_1)} \times p_2^{\min(x_2, y_2)} \times \dots}$$
          </div>
          <div class="p-3 rounded-lg bg-emerald-950/40 border border-emerald-500/30 text-xs text-emerald-200">
            <strong>Worked Example:</strong> Find HCF of $72$ and $120$.<br>
            $72 = 2^3 \times 3^2$<br>
            $120 = 2^3 \times 3^1 \times 5^1$<br>
            • For base $2$: $\min(3, 3) = 3 \implies 2^3 = 8$<br>
            • For base $3$: $\min(2, 1) = 1 \implies 3^1 = 3$<br>
            • For base $5$: Present in 120 ($5^1$) but $0$ in 72 ($5^0$) $\implies 5^{\min(0,1)} = 1$<br>
            $$\text{HCF} = 2^3 \times 3^1 = 8 \times 3 = \mathbf{24}!$$
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Minimum Exponent</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Common Prime Core</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Greatest Subpart</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">Prime Power Alignment</span>
          </div>
        """,
        "sim_id": "sim-hcf-prime-powers",
        "checkpoints": [
            {
                "id": "4.1",
                "question": "If $A = 2^4 \\times 3^2 \\times 5^3$ and $B = 2^3 \\times 3^5 \\times 5^1$, what is their HCF?",
                "options": ["$2^4 \\times 3^5 \\times 5^3$", "$2^3 \\times 3^2 \\times 5^1$", "$2^7 \\times 3^7 \\times 5^4$", "$2 \\times 3 \\times 5$"],
                "correct": 1,
                "explanation": "Take the minimum power for each prime: $2^{\\min(4,3)} \\times 3^{\\min(2,5)} \\times 5^{\\min(3,1)} = 2^3 \\times 3^2 \\times 5^1 = 8 \\times 9 \\times 5 = 360$."
            },
            {
                "id": "4.2",
                "question": "What is the HCF of $40$ and $75$?",
                "options": ["$2$", "$5$", "$10$", "$25$"],
                "correct": 1,
                "explanation": "$40 = 2^3 \\times 5^1$ and $75 = 3^1 \\times 5^2$. The only common prime is 5 with power $\\min(1, 2) = 1$. HCF $= 5$."
            }
        ]
    },
    {
        "slide_num": 5,
        "section": "3.1 Mathematical Logic",
        "badge": "Conjectures & Counterexamples",
        "title": "Conjectures & Counterexamples: Thinking Like a Mathematician",
        "narration": "In mathematics, we do not simply guess—we formulate conjectures and rigorously test them! A conjecture is an unproven claim. If a claim is false, a single counterexample instantly refutes it.",
        "theory": r"""
          <p class="mb-3">
            Rigorous thinking in number theory relies on two pivotal pillars:
          </p>
          <div class="grid grid-cols-2 gap-2.5 mb-3 text-xs">
            <div class="p-2.5 rounded bg-sky-950/40 border border-sky-500/30">
              <strong class="text-sky-300 block mb-1">🔍 Conjecture:</strong>
              A mathematical statement or hypothesis that is believed to be true based on observed patterns, but has not yet been formally proven.
            </div>
            <div class="p-2.5 rounded bg-rose-950/40 border border-rose-500/30">
              <strong class="text-rose-300 block mb-1">💥 Counterexample:</strong>
              A specific case or example that shows a conjecture is FALSE. It takes millions of examples to support a conjecture, but only <strong>one</strong> counterexample to destroy it!
            </div>
          </div>
          <div class="p-3 rounded-lg bg-slate-900/70 border border-slate-700 text-xs text-slate-300 space-y-2">
            <p><strong>Case Study 1:</strong> <em>\"The HCF of any two even numbers is always 2.\"</em><br>
            <span class="text-rose-400 font-bold">Counterexample:</span> Consider $4$ and $8$. Both are even, but $\text{HCF}(4, 8) = 4 \neq 2$! The conjecture is shattered.</p>
            <p><strong>Case Study 2:</strong> <em>\"If two numbers have HCF = 1, both numbers must be prime.\"</em><br>
            <span class="text-rose-400 font-bold">Counterexample:</span> Take $8$ and $9$. $\text{HCF}(8, 9) = 1$. But $8 = 2^3$ is composite, and $9 = 3^2$ is composite! (They are called <strong>Co-prime</strong> numbers).</p>
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Conjecture</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Counterexample</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Co-prime Numbers ($\text{HCF}=1$)</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Mathematical Proof</span>
          </div>
        """,
        "sim_id": "sim-conjecture-tester",
        "checkpoints": [
            {
                "id": "5.1",
                "question": "Which of the following serves as a counterexample to the claim: 'The sum of two odd numbers is always odd'?",
                "options": ["$3 + 5 = 8$ (which is even)", "$2 + 3 = 5$", "$4 + 6 = 10$", "$1 + 1 = 2$ is an exception only"],
                "correct": 0,
                "explanation": "3 and 5 are odd, but their sum 8 is even! This counterexample refutes the claim immediately."
            },
            {
                "id": "5.2",
                "question": "Are $14$ and $15$ co-prime? Why or why not?",
                "options": ["No, because neither is a prime number", "Yes, because their HCF is 1", "No, because 14 is even", "Yes, because their sum is 29"],
                "correct": 1,
                "explanation": "Factors of 14 are {1, 2, 7, 14}. Factors of 15 are {1, 3, 5, 15}. HCF(14, 15) = 1, so they are co-prime!"
            }
        ]
    },
    {
        "slide_num": 6,
        "section": "3.2 LCM Foundations",
        "badge": "Toran Strips & Periodic Sync",
        "title": "Least, but not Last! Syncing Periodic Cycles & Toran Strips",
        "narration": "Now we transition from dividing down to multiplying up! When two rhythmic events repeat at different intervals, when will they strike in unison? The Lowest Common Multiple provides the answer.",
        "theory": r"""
          <p class="mb-3">
            In nature and daily life, cycles with different periods eventually align:
          </p>
          <div class="space-y-2 mb-3 text-xs">
            <div class="p-2.5 rounded bg-sky-950/40 border border-sky-500/30">
              <strong class="text-sky-300 block mb-1">🎊 The Toran Festive Strips Dilemma:</strong>
              Crafting decorative door hangings (torans) from cloth strips. Row A uses strips of length $6\text{ cm}$. Row B uses strips of length $8\text{ cm}$. What is the shortest total length at which both rows end at the exact same point?
              $$\text{Multiples of } 6: 6, 12, 18, \mathbf{24}, 30, \dots \quad \text{Multiples of } 8: 8, 16, \mathbf{24}, 32, \dots$$
              Both rows align perfectly at $24\text{ cm}$!
            </div>
            <div class="p-2.5 rounded bg-amber-950/40 border border-amber-500/30">
              <strong class="text-amber-300 block mb-1">🍬 The Sweet Shop Schedule Dilemma:</strong>
              Dev visits the sweet shop every $10\text{ days}$. Ananya visits every Monday ($7\text{ days}$). If they met today, in how many days will they meet again?
              $$\text{Next Meeting} = \text{LCM}(10, 7) = 70\text{ days}!$$
            </div>
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Lowest Common Multiple (LCM)</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Periodic Synchronization</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Repeated Additive Multiples</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">Toran Craft Alignment</span>
          </div>
        """,
        "sim_id": "sim-toran-strip-aligner",
        "checkpoints": [
            {
                "id": "6.1",
                "question": "Three alarm bells ring at intervals of $4$, $6$, and $8$ minutes. If they ring together now, after how many minutes will they next toll simultaneously?",
                "options": ["$12\text{ min}$", "$16\text{ min}$", "$24\text{ min}$", "$48\text{ min}$"],
                "correct": 2,
                "explanation": "Multiples of 4: 4, 8, 12, 16, 20, 24... Multiples of 6: 6, 12, 18, 24... Multiples of 8: 8, 16, 24... LCM(4,6,8) = 24 minutes!"
            },
            {
                "id": "6.2",
                "question": "How many $6\text{ cm}$ strips and $8\text{ cm}$ strips make up the $24\text{ cm}$ toran?",
                "options": ["4 of $6\text{ cm}$ and 3 of $8\text{ cm}$", "3 of $6\text{ cm}$ and 4 of $8\text{ cm}$", "2 of each", "6 of each"],
                "correct": 0,
                "explanation": "$24 / 6 = 4$ strips of 6 cm, and $24 / 8 = 3$ strips of 8 cm."
            }
        ]
    },
    {
        "slide_num": 7,
        "section": "3.2 Definition of LCM",
        "badge": "Multiples Stepper",
        "title": "The Lowest Common Multiple: Stepping Along the Number Line",
        "narration": "Picture two runners leaping along a track! Runner A takes leaps of four units; Runner B takes leaps of six units. The first shared stepping stone they both land on is their Lowest Common Multiple.",
        "theory": r"""
          <p class="mb-3">
            The <strong>Lowest Common Multiple (LCM)</strong> of two or more non-zero integers is the smallest positive integer that is divisible by all of them.
          </p>
          <div class="p-3 rounded-lg bg-slate-900/70 border border-slate-700 mb-3 text-xs text-slate-300 space-y-1.5">
            <p><strong>Listing Multiples Protocol:</strong></p>
            <p>• Multiples of $4$: $4, 8, \mathbf{12}, 16, 20, \mathbf{24}, 28, 32, \mathbf{36}, \dots$</p>
            <p>• Multiples of $6$: $6, \mathbf{12}, 18, \mathbf{24}, 30, \mathbf{36}, 42, \dots$</p>
            <p>• Common Multiples: $\{12, 24, 36, 48, \dots\}$</p>
            <p>• Smallest element: $\mathbf{\text{LCM}(4, 6) = 12}$.</p>
          </div>
          <div class="p-3 rounded-lg bg-indigo-950/40 border border-indigo-500/30 text-xs text-indigo-200">
            <strong>Key Invariance Property:</strong><br>
            Notice that all common multiples are exact multiples of the LCM!
            $$\text{Common Multiples}(a, b) = \{k \times \text{LCM}(a, b) \mid k = 1, 2, 3, \dots\}$$
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">LCM Definition</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Jump Intervals</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Multiples of LCM</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">First Shared Locus</span>
          </div>
        """,
        "sim_id": "sim-lcm-multiples-stepper",
        "checkpoints": [
            {
                "id": "7.1",
                "question": "What is the LCM of $9$ and $12$?",
                "options": ["$18$", "$24$", "$36$", "$72$"],
                "correct": 2,
                "explanation": "Multiples of 9: 9, 18, 27, 36... Multiples of 12: 12, 24, 36... The lowest common multiple is 36!"
            },
            {
                "id": "7.2",
                "question": "If the LCM of two numbers is $15$, which of the following is guaranteed to be a common multiple?",
                "options": ["$25$", "$45$", "$50$", "$70$"],
                "correct": 1,
                "explanation": "All common multiples must be multiples of the LCM. $45 = 15 \\times 3$, so it is a common multiple!"
            }
        ]
    },
    {
        "slide_num": 8,
        "section": "3.2 LCM via Primes",
        "badge": "Maximum Power Union",
        "title": "LCM by Prime Factorisation: Maximum Exponent Union",
        "narration": "To construct an LCM, our container must be roomy enough to accommodate all prime factors of both numbers. Therefore, instead of the minimum exponent, we choose the maximum exponent of every prime present!",
        "theory": r"""
          <p class="mb-3">
            To find the <strong>LCM</strong> using prime powers:
          </p>
          <div class="p-3 rounded-lg bg-slate-900/70 border border-slate-700 mb-3 text-xs text-slate-300 space-y-2">
            <p>1. Express each number in prime factor power notation.</p>
            <p>2. For every prime base that appears in <em>either</em> number, take the <strong>maximum exponent</strong>: $\max(x_i, y_i)$.</p>
            <p>3. Multiply these maximum powers together:</p>
            $$\mathbf{\text{LCM}(a, b) = p_1^{\max(x_1, y_1)} \times p_2^{\max(x_2, y_2)} \times \dots}$$
          </div>
          <div class="p-3 rounded-lg bg-emerald-950/40 border border-emerald-500/30 text-xs text-emerald-200">
            <strong>Worked Example:</strong> Find LCM of $72$ and $120$.<br>
            $72 = 2^3 \times 3^2$<br>
            $120 = 2^3 \times 3^1 \times 5^1$<br>
            • For base $2$: $\max(3, 3) = 3 \implies 2^3 = 8$<br>
            • For base $3$: $\max(2, 1) = 2 \implies 3^2 = 9$<br>
            • For base $5$: $\max(0, 1) = 1 \implies 5^1 = 5$<br>
            $$\text{LCM} = 2^3 \times 3^2 \times 5^1 = 8 \times 9 \times 5 = \mathbf{360}!$$
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Maximum Exponent</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Union of All Primes</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">HCF vs LCM Duality</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">Smallest Divisible Container</span>
          </div>
        """,
        "sim_id": "sim-lcm-prime-union",
        "checkpoints": [
            {
                "id": "8.1",
                "question": "If $X = 2^2 \\times 3^1 \\times 7^2$ and $Y = 2^3 \\times 3^3 \\times 5^1$, what is their LCM in prime power form?",
                "options": ["$2^2 \\times 3^1$", "$2^3 \\times 3^3 \\times 5^1 \\times 7^2$", "$2^5 \\times 3^4 \\times 5^1 \\times 7^2$", "$2^3 \\times 3^3$"],
                "correct": 1,
                "explanation": "Take the maximum power for each prime: $2^{\\max(2,3)} \\times 3^{\\max(1,3)} \\times 5^{\\max(0,1)} \\times 7^{\\max(2,0)} = 2^3 \\times 3^3 \\times 5^1 \\times 7^2$."
            },
            {
                "id": "8.2",
                "question": "What is the LCM of $18$ ($2 \\times 3^2$) and $24$ ($2^3 \\times 3$)?",
                "options": ["$36$", "$48$", "$72$", "$144$"],
                "correct": 2,
                "explanation": "$\\text{LCM} = 2^3 \\times 3^2 = 8 \\times 9 = 72$."
            }
        ]
    },
    {
        "slide_num": 9,
        "section": "3.3 Patterns",
        "badge": "Algebraic Divisibility",
        "title": "Algebraic Patterns: Generalising Multiples ($n, 5n, 6n$)",
        "narration": "Algebra gives wings to arithmetic! By expressing multiples as formulas like n, 5n, or 6n, we uncover universal divisibility patterns across number grids.",
        "theory": r"""
          <p class="mb-3">
            Using algebraic notation, infinite number patterns collapse into simple symbolic formulas:
          </p>
          <div class="space-y-2 mb-3 text-xs">
            <div class="p-2.5 rounded bg-slate-900/70 border border-slate-700">
              <strong class="text-sky-300 block mb-1">🔢 Algebraic Multiples:</strong>
              • Multiples of $2$: $2n = \{2, 4, 6, 8, \dots\}$ (Even Numbers)<br>
              • Multiples of $5$: $5n = \{5, 10, 15, 20, \dots\}$ (Ending in $0$ or $5$)<br>
              • Multiples of $10$: $10n = \{10, 20, 30, \dots\}$ (Ending in $0$)
            </div>
            <div class="p-2.5 rounded bg-emerald-950/40 border border-emerald-500/30">
              <strong class="text-emerald-300 block mb-1">⚡ The LCM Combination Rule:</strong>
              If a number is divisible by both $a$ and $b$, it MUST be a multiple of their LCM:
              $$n \text{ divisible by } 2 \text{ and } 3 \iff n \text{ is a multiple of } \text{LCM}(2, 3) = 6n$$
              $$n \text{ divisible by } 4 \text{ and } 6 \iff n \text{ is a multiple of } \text{LCM}(4, 6) = 12n \text{ (NOT } 24n!\text{)}$$
            </div>
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Algebraic Form ($kn$)</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Simultaneous Divisibility</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">LCM Multiples Law</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">100-Grid Filter</span>
          </div>
        """,
        "sim_id": "sim-algebraic-multiples-grid",
        "checkpoints": [
            {
                "id": "9.1",
                "question": "A number is divisible by both $3$ and $5$. Which of the following formulas describes all such numbers?",
                "options": ["$8n$", "$15n$", "$3n + 5$", "$30n$"],
                "correct": 1,
                "explanation": "$\\text{LCM}(3, 5) = 15$. Every number divisible by both 3 and 5 is an exact multiple of 15, written algebraically as $15n$."
            },
            {
                "id": "9.2",
                "question": "If an integer is divisible by both $6$ and $8$, it must be divisible by:",
                "options": ["$48$", "$14$", "$24$", "$2$ only"],
                "correct": 2,
                "explanation": "$\\text{LCM}(6, 8) = 24$. All such integers must be divisible by 24!"
            }
        ]
    },
    {
        "slide_num": 10,
        "section": "3.3 Special Relationships",
        "badge": "The Multiple Rule & Co-Primes",
        "title": "Special Relationships: The Multiple Rule & Co-Primes",
        "narration": "Observe these extraordinary shortcuts! If one number is a multiple of the other, you don't even need to calculate: their HCF is the smaller number, and their LCM is the larger. And for co-prime numbers, their LCM is simply their direct product!",
        "theory": r"""
          <p class="mb-3">
            Two golden shortcut theorems that save immense calculation time:
          </p>
          <div class="space-y-2 mb-3 text-xs">
            <div class="p-2.5 rounded bg-amber-950/40 border border-amber-500/30">
              <strong class="text-amber-300 block mb-1">1. The Multiple Rule ($a$ divides $b$):</strong>
              If number $b$ is an exact multiple of $a$ ($a \mid b$):
              $$\mathbf{\text{HCF}(a, b) = a \quad (\text{the smaller number})}$$
              $$\mathbf{\text{LCM}(a, b) = b \quad (\text{the larger number})}$$
              <em>Example:</em> For $6$ and $24$: since $6 \times 4 = 24$, $\text{HCF} = 6$ and $\text{LCM} = 24$.
            </div>
            <div class="p-2.5 rounded bg-emerald-950/40 border border-emerald-500/30">
              <strong class="text-emerald-300 block mb-1">2. The Co-Prime Rule ($\text{HCF} = 1$):</strong>
              If two numbers share no common factor other than $1$:
              $$\mathbf{\text{HCF}(a, b) = 1}$$
              $$\mathbf{\text{LCM}(a, b) = a \times b}$$
              <em>Example:</em> For $8$ and $9$: $\text{HCF}(8, 9) = 1$, so $\text{LCM}(8, 9) = 8 \times 9 = 72$.
            </div>
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Multiple Rule ($a \mid b$)</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Co-Prime Rule ($\text{HCF}=1$)</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Instant Shortcuts</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">Zero Computation</span>
          </div>
        """,
        "sim_id": "sim-nested-multiple-rule",
        "checkpoints": [
            {
                "id": "10.1",
                "question": "What is the HCF and LCM of $7$ and $35$?",
                "options": ["$\text{HCF}=1, \text{LCM}=245$", "$\text{HCF}=7, \text{LCM}=35$", "$\text{HCF}=5, \text{LCM}=35$", "$\text{HCF}=7, \text{LCM}=70$"],
                "correct": 1,
                "explanation": "Since 35 is an exact multiple of 7 ($7 \\times 5 = 35$), the Multiple Rule states HCF = 7 (smaller) and LCM = 35 (larger)!"
            },
            {
                "id": "10.2",
                "question": "Two numbers are co-prime and their product is $143$. What is their LCM?",
                "options": ["$1$", "$11$", "$13$", "$143$"],
                "correct": 3,
                "explanation": "For co-prime numbers, $\\text{LCM} = a \\times b$. Given product is 143, so LCM = 143!"
            }
        ]
    },
    {
        "slide_num": 11,
        "section": "3.3 Scaling Properties",
        "badge": "Magnification Invariance",
        "title": "Scaling Properties: Multiplying Both Numbers by $k$",
        "narration": "What happens when you scale both numbers uniformly by a factor k? Like an image through a magnifying glass, their HCF and LCM scale by that exact same factor k!",
        "theory": r"""
          <p class="mb-3">
            The <strong>Homogeneity / Scaling Theorem</strong> states that multiplying both inputs by any positive integer $k$ scales both the HCF and LCM by $k$:
          </p>
          <div class="p-3 rounded-lg bg-sky-950/40 border border-sky-500/30 mb-3 text-xs text-sky-200 space-y-1.5">
            $$\mathbf{\text{HCF}(k \cdot a, k \cdot b) = k \times \text{HCF}(a, b)}$$
            $$\mathbf{\text{LCM}(k \cdot a, k \cdot b) = k \times \text{LCM}(a, b)}$$
          </div>
          <div class="p-3 rounded-lg bg-slate-900/70 border border-slate-700 text-xs text-slate-300 space-y-2">
            <p><strong>Example Demonstration:</strong></p>
            <p>• Base pair: $a = 6, b = 8$. We know $\text{HCF}(6, 8) = 2$ and $\text{LCM}(6, 8) = 24$.</p>
            <p>• Double both ($k = 2$): $2a = 12, 2b = 16$.<br>
            $\text{HCF}(12, 16) = 4 = \mathbf{2 \times 2}$.<br>
            $\text{LCM}(12, 16) = 48 = \mathbf{2 \times 24}$.</p>
            <p>• Multiply both by $10$ ($k = 10$): $60$ and $80$.<br>
            $\text{HCF}(60, 80) = 20 = \mathbf{10 \times 2}$.<br>
            $\text{LCM}(60, 80) = 240 = \mathbf{10 \times 24}$.</p>
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Scale Factor $k$</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Linear Scaling</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Homogeneous Invariance</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">Mental Scaling Shortcut</span>
          </div>
        """,
        "sim_id": "sim-scaling-magnifier",
        "checkpoints": [
            {
                "id": "11.1",
                "question": "Given $\text{HCF}(15, 25) = 5$. What is $\text{HCF}(150, 250)$?",
                "options": ["$5$", "$50$", "$500$", "$25$"],
                "correct": 1,
                "explanation": "Both numbers are multiplied by $k = 10$. So the new HCF $= 10 \\times 5 = 50$!"
            },
            {
                "id": "11.2",
                "question": "If $\text{LCM}(a, b) = 36$, what is $\text{LCM}(3a, 3b)$?",
                "options": ["$36$", "$72$", "$108$", "$12$"],
                "correct": 2,
                "explanation": "Scaling both numbers by 3 scales the LCM by 3: $36 \\times 3 = 108$."
            }
        ]
    },
    {
        "slide_num": 12,
        "section": "3.3 Division Procedures",
        "badge": "Simultaneous Division",
        "title": "Simultaneous Division: The Famous Ladder (Cake) Method",
        "narration": "Behold the most celebrated and efficient paper-and-pencil procedure in the world: the Ladder, or Layer-Cake Method! In one unified division flow, it extracts both the HCF and the LCM simultaneously.",
        "theory": r"""
          <p class="mb-3">
            The <strong>Simultaneous Division Method</strong> arranges numbers horizontally and repeatedly extracts common prime divisors:
          </p>
          <div class="p-3 rounded-lg bg-slate-900/70 border border-slate-700 mb-3 text-xs text-slate-300 space-y-2 font-mono">
            <div>Step 1: Write numbers in a row: <code>20, 28</code></div>
            <div>Step 2: Divide both by common prime <code>2</code> $\implies$ quotients <code>10, 14</code></div>
            <div>Step 3: Divide both by common prime <code>2</code> $\implies$ quotients <code>5, 7</code></div>
            <div>Step 4: <code>5</code> and <code>7</code> are co-prime (no common divisor $> 1$). STOP!</div>
          </div>
          <div class="grid grid-cols-2 gap-2 text-xs mb-2">
            <div class="p-2.5 rounded bg-amber-950/40 border border-amber-500/30">
              <strong class="text-amber-300 block mb-1">To find HCF:</strong>
              Multiply ONLY the common divisors on the <strong>left column</strong>:
              $$\mathbf{\text{HCF} = 2 \times 2 = 4}$$
            </div>
            <div class="p-2.5 rounded bg-emerald-950/40 border border-emerald-500/30">
              <strong class="text-emerald-300 block mb-1">To find LCM:</strong>
              Multiply the entire <strong>'L-Shape'</strong> (left column $\times$ bottom row):
              $$\mathbf{\text{LCM} = 2 \times 2 \times 5 \times 7 = 140}$$
            </div>
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Ladder Method</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">L-Shape Rule</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Left Column = HCF</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">Dual Output</span>
          </div>
        """,
        "sim_id": "sim-simultaneous-ladder",
        "checkpoints": [
            {
                "id": "12.1",
                "question": "In the simultaneous division of $24$ and $36$, the left column divisors are $2, 2, 3$ and the bottom quotients are $2, 3$. What is the LCM?",
                "options": ["$12$", "$24$", "$36$", "$72$"],
                "correct": 3,
                "explanation": "Multiply the entire 'L' shape: $2 \\times 2 \\times 3 \\times 2 \\times 3 = 12 \\times 6 = 72$!"
            },
            {
                "id": "12.2",
                "question": "In the same calculation above, what is the HCF?",
                "options": ["$6$", "$12$", "$18$", "$24$"],
                "correct": 1,
                "explanation": "HCF is the product of only the left column: $2 \\times 2 \\times 3 = 12$."
            }
        ]
    },
    {
        "slide_num": 13,
        "section": "3.3 Advanced Shortcuts",
        "badge": "Large Factor Slasher",
        "title": "Advanced Shortcuts: Factoring Out Large Multiples Upfront",
        "narration": "Why divide by two three times when you can slash ten, twenty, or fifty in a single stroke? Factoring out obvious large common factors upfront turns intimidating 3-digit problems into lightning-fast mental math!",
        "theory": r"""
          <p class="mb-3">
            Instead of laboriously testing small primes ($2, 3, 5$), look for <strong>obvious large common factors</strong> first:
          </p>
          <div class="p-3 rounded-lg bg-emerald-950/40 border border-emerald-500/30 mb-3 text-xs text-slate-300 space-y-2">
            <p><strong class="text-emerald-300">⚡ Example: Find HCF and LCM of $120$ and $180$</strong></p>
            <p>1. Notice both numbers end in zero $\implies$ common factor $10$. Even better: $60$ divides both!</p>
            <p>2. Factor out $60$:
            $$120 = 60 \times \mathbf{2}, \quad 180 = 60 \times \mathbf{3}$$
            </p>
            <p>3. The remaining parts are $2$ and $3$, which are co-prime ($\text{HCF}(2, 3) = 1$ and $\text{LCM}(2, 3) = 6$).</p>
            <p>4. Re-scale by our extracted factor $60$:
            $$\mathbf{\text{HCF} = 60 \times 1 = 60}$$
            $$\mathbf{\text{LCM} = 60 \times 6 = 360}$$
            </p>
          </div>
          <p class="text-xs text-slate-300">
            This lightning method reduces multi-minute calculations to 5 seconds of effortless mental math!
          </p>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Large Factor Slasher</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Upfront Extraction</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Mental Math Power</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">Instant Co-Prime Reduction</span>
          </div>
        """,
        "sim_id": "sim-shortcut-factor-extractor",
        "checkpoints": [
            {
                "id": "13.1",
                "question": "Find the HCF of $300$ and $450$ by extracting their largest obvious common multiple upfront:",
                "options": ["$50$", "$100$", "$150$", "$200$"],
                "correct": 2,
                "explanation": "$300 = 150 \\times 2$ and $450 = 150 \\times 3$. Since 2 and 3 are co-prime, HCF $= 150$!"
            },
            {
                "id": "13.2",
                "question": "Using the same extraction for $300$ and $450$, what is their LCM?",
                "options": ["$600$", "$900$", "$1350$", "$1500$"],
                "correct": 1,
                "explanation": "$\\text{LCM} = 150 \\times \\text{LCM}(2, 3) = 150 \\times 6 = 900$."
            }
        ]
    },
    {
        "slide_num": 14,
        "section": "3.3 The Master Formula",
        "badge": "Product Balance Law",
        "title": "The Master Formula: $\\text{HCF} \\times \\text{LCM} = a \\times b$",
        "narration": "Now behold the grand master theorem of arithmetic! For any two numbers, their HCF multiplied by their LCM exactly equals the product of the two original numbers. Like a golden mechanical balance, both pans balance in absolute perfection.",
        "theory": r"""
          <p class="mb-3">
            The <strong>Fundamental Product Theorem</strong> connects two numbers, their HCF, and their LCM:
            $$\mathbf{\text{HCF}(a, b) \times \text{LCM}(a, b) = a \times b}$$
          </p>
          <div class="p-3 rounded-lg bg-amber-950/40 border border-amber-500/30 mb-3 text-xs text-amber-200">
            <strong>Why does this identity always hold?</strong><br>
            For any prime factor $p$ with powers $p^x$ in $a$ and $p^y$ in $b$:<br>
            • HCF takes the minimum power: $p^{\min(x, y)}$<br>
            • LCM takes the maximum power: $p^{\max(x, y)}$<br>
            Because $\min(x, y) + \max(x, y) = x + y$, multiplying HCF by LCM gathers $p^{x+y}$, which is the exact prime power in $a \times b$!
          </div>
          <div class="p-3 rounded-lg bg-slate-900/70 border border-slate-700 text-xs text-slate-300 space-y-1.5 font-mono">
            <p><strong>Derived Equation Solvers:</strong></p>
            <div>• To find unknown number: $a = \frac{\text{HCF} \times \text{LCM}}{b}$</div>
            <div>• To find LCM: $\text{LCM} = \frac{a \times b}{\text{HCF}}$</div>
            <div>• To find HCF: $\text{HCF} = \frac{a \times b}{\text{LCM}}$</div>
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">$\text{HCF} \times \text{LCM} = a \times b$</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Min + Max = Sum</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Golden Balance</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">Unknown Value Solver</span>
          </div>
        """,
        "sim_id": "sim-master-product-balance",
        "checkpoints": [
            {
                "id": "14.1",
                "question": "The HCF of two numbers is $6$ and their LCM is $72$. If one number is $18$, what is the other number?",
                "options": ["$12$", "$24$", "$36$", "$48$"],
                "correct": 1,
                "explanation": "Using $b = (\\text{HCF} \\times \\text{LCM}) / a = (6 \\times 72) / 18 = 432 / 18 = 24$!"
            },
            {
                "id": "14.2",
                "question": "The product of two numbers is $1800$ and their HCF is $30$. What is their LCM?",
                "options": ["$30$", "$60$", "$90$", "$180$"],
                "correct": 1,
                "explanation": "$\\text{LCM} = (a \\times b) / \\text{HCF} = 1800 / 30 = 60$."
            }
        ]
    },
    {
        "slide_num": 15,
        "section": "3.3 Three Numbers Lab",
        "badge": "The Three-Number Trap",
        "title": "HCF & LCM of Three Numbers: Beware the Formula Trap!",
        "narration": "A critical warning for young mathematicians: does the Master Formula hold for three numbers? No! Trying to multiply HCF and LCM for three numbers fails because pairwise overlaps duplicate factors. Let us explore the true 3-number rules.",
        "theory": r"""
          <p class="mb-3">
            Finding HCF and LCM for three numbers ($a, b, c$):
          </p>
          <div class="space-y-2 mb-3 text-xs">
            <div class="p-2.5 rounded bg-slate-900/70 border border-slate-700">
              <strong class="text-sky-300 block mb-1">📐 True Definitions for 3 Numbers:</strong>
              • $\text{HCF}(a, b, c)$: Product of primes common to <strong>ALL THREE</strong> numbers with minimum exponents.<br>
              • $\text{LCM}(a, b, c)$: Product of ALL primes appearing in any number with maximum exponents.
            </div>
            <div class="p-2.5 rounded bg-rose-950/40 border border-rose-500/30">
              <strong class="text-rose-300 block mb-1">⚠️ The Famous Three-Number Formula Trap:</strong>
              $$\mathbf{\text{HCF}(a, b, c) \times \text{LCM}(a, b, c) \neq a \times b \times c!}$$
              <span class="text-slate-300">Counterexample with $4, 6, 8$:</span><br>
              • $\text{HCF}(4, 6, 8) = 2$<br>
              • $\text{LCM}(4, 6, 8) = 24$<br>
              • $\text{HCF} \times \text{LCM} = 2 \times 24 = \mathbf{48}$<br>
              • But $a \times b \times c = 4 \times 6 \times 8 = \mathbf{192}$!<br>
              Since $48 \neq 192$, the two-number formula does <strong>NOT</strong> generalize directly to three numbers!
            </div>
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Formula Trap ($\neq abc$)</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">3-Way Prime Intersection</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Pairwise Overlap Duplicate</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">Counterexample Proof</span>
          </div>
        """,
        "sim_id": "sim-three-number-engine",
        "checkpoints": [
            {
                "id": "15.1",
                "question": "Is $\text{HCF}(a, b, c) \times \text{LCM}(a, b, c) = a \times b \times c$ always true for any three positive integers?",
                "options": ["Yes, always", "No, it is generally false", "Only if all three numbers are even", "Only if all three are composite"],
                "correct": 1,
                "explanation": "It is generally false! As proven by the counterexample $4, 6, 8$, pairwise common factors cause the product of the three numbers to exceed HCF $\\times$ LCM."
            },
            {
                "id": "15.2",
                "question": "Find the HCF of $12, 18,$ and $30$:",
                "options": ["$2$", "$3$", "$6$", "$12$"],
                "correct": 2,
                "explanation": "$12 = 2^2 \\times 3$, $18 = 2 \\times 3^2$, $30 = 2 \\times 3 \\times 5$. The common primes are $2^1 \\times 3^1 = 6$."
            }
        ]
    },
    {
        "slide_num": 16,
        "section": "3.3 Heritage",
        "badge": "Kuṭṭaka & Niruddha",
        "title": "Ancient Indian Heritage: Āryabhaṭa's Kuṭṭaka & Mahāvīrācārya's Niruddha",
        "narration": "In ancient India, the study of divisors and multiples reached breathtaking heights! In 499 CE, Acharya Āryabhaṭa created the Kuṭṭaka pulverizer algorithm. In 850 CE, I, Mahāvīrācārya, formalized the Niruddha method for Lowest Common Multiples.",
        "theory": r"""
          <p class="mb-3">
            India's pioneering mathematical traditions laid the global foundations for HCF and LCM algorithms:
          </p>
          <div class="space-y-2 mb-3 text-xs">
            <div class="p-2.5 rounded bg-amber-950/40 border border-amber-500/30">
              <strong class="text-amber-300 block mb-1">📜 Āryabhaṭa's Kuṭṭaka (The Pulverizer, 499 CE):</strong>
              In the <em>Āryabhaṭīya</em>, Āryabhaṭa devised the <strong>Kuṭṭaka</strong> method—a systematic reciprocal division algorithm to solve indeterminate equations of the form $ax - by = c$. This algorithm is identical to the extended Euclidean division algorithm for GCD, pulverizing remainders into smaller and smaller units.
            </div>
            <div class="p-2.5 rounded bg-emerald-950/40 border border-emerald-500/30">
              <strong class="text-emerald-300 block mb-1">📜 Mahāvīrācārya's Niruddha (Gaṇitasārasaṅgraha, c. 850 CE):</strong>
              I, <strong>Mahāvīrācārya</strong>, introduced the term <strong>Niruddha</strong> (meaning \"that which is held or bound\"), which represents the <em>Lowest Common Multiple</em>! I gave the world's first codified rules for adding fractions by reducing denominators to their Niruddha (common denominator):
              $$\frac{a}{p} + \frac{b}{q} \quad \text{via common denominator } \text{Niruddha}(p, q)$$
            </div>
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Āryabhaṭa (499 CE)</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Mahāvīrācārya (850 CE)</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Kuṭṭaka (Pulverizer GCD)</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">Niruddha (LCM)</span>
          </div>
        """,
        "sim_id": "sim-heritage-kuttaka",
        "checkpoints": [
            {
                "id": "16.1",
                "question": "What mathematical concept was termed 'Niruddha' by Mahāvīrācārya in the Gaṇitasārasaṅgraha?",
                "options": ["Highest Common Factor (HCF)", "Lowest Common Multiple (LCM)", "Prime Number", "Square Root"],
                "correct": 1,
                "explanation": "Mahāvīrācārya was the first mathematician to explicitly define and name the Lowest Common Multiple as 'Niruddha'!"
            },
            {
                "id": "16.2",
                "question": "What is the primary function of Āryabhaṭa's Kuṭṭaka algorithm?",
                "options": ["Calculating compound interest", "Systematic reciprocal division to find GCD and solve Diophantine equations", "Geometry of circles", "Trigonometric sine tables"],
                "correct": 1,
                "explanation": "The Kuṭṭaka (pulverizer) is a systematic Euclidean division method to pulverize quotients and find common divisors!"
            }
        ]
    },
    {
        "slide_num": 17,
        "section": "3.4 Mastery Quiz",
        "badge": "Quiz Challenge I",
        "title": "Mastery Challenge I: HCF & Prime Factor Trees",
        "narration": "Welcome to Mastery Challenge Round One! Put your knowledge of floor tiling, common factor intersections, and prime factor trees to the test.",
        "quiz_range": [1, 10]
    },
    {
        "slide_num": 18,
        "section": "3.4 Mastery Quiz",
        "badge": "Quiz Challenge II",
        "title": "Mastery Challenge II: LCM, Torans & Periodic Sync",
        "narration": "Round Two will test your mastery of the Lowest Common Multiple, toran strip alignments, leap cycles, and prime power union constructions.",
        "quiz_range": [11, 20]
    },
    {
        "slide_num": 19,
        "section": "3.4 Mastery Quiz",
        "badge": "Quiz Challenge III",
        "title": "Mastery Challenge III: Patterns, Relationships & The Ladder Method",
        "narration": "Round Three challenges your prowess in algebraic multiples, the Multiple Rule, scaling properties, and the simultaneous division ladder method.",
        "quiz_range": [21, 30]
    },
    {
        "slide_num": 20,
        "section": "3.4 Mastery Quiz",
        "badge": "Quiz Challenge IV",
        "title": "Mastery Challenge IV: The Master Formula & Grand Finale",
        "narration": "Congratulations on reaching the final round! Master the fundamental formula HCF times LCM equals a times b, avoid the three-number trap, and claim your chapter mastery certificate!",
        "quiz_range": [31, 40]
    }
]

# 40 Rigorous Quiz Questions with Detailed Step-by-Step Solutions
QUIZ_QUESTIONS = [
    # Questions 1 to 10 (Slide 17)
    {
        "id": 1,
        "question": "What is the HCF of two distinct prime numbers $p$ and $q$?",
        "options": ["$p \\times q$", "$p + q$", "$1$", "$0$"],
        "correct": 2,
        "solution": "Prime numbers have divisors $\{1, p\}$ and $\{1, q\}$. Since $p \\neq q$, the only common divisor is 1. Thus $\\text{HCF}(p, q) = 1$."
    },
    {
        "id": 2,
        "question": "A courtyard measuring $24\text{ m} \times 36\text{ m}$ is paved with the largest possible square tiles without cutting. What is the side length of each tile?",
        "options": ["$6\text{ m}$", "$8\text{ m}$", "$12\text{ m}$", "$18\text{ m}$"],
        "correct": 2,
        "solution": "The side of the largest square tile is $\\text{HCF}(24, 36) = 12\\text{ m}$."
    },
    {
        "id": 3,
        "question": "How many $12\text{ m} \times 12\text{ m}$ square tiles are needed to pave the $24\text{ m} \times 36\text{ m}$ courtyard?",
        "options": ["$4$", "$6$", "$8$", "$12$"],
        "correct": 1,
        "solution": "Number of tiles $= \\frac{24 \\times 36}{12 \\times 12} = 2 \\times 3 = 6$ tiles."
    },
    {
        "id": 4,
        "question": "What is the prime factorisation of $144$ in exponential form?",
        "options": ["$2^4 \\times 3^2$", "$2^3 \\times 3^3$", "$12^2$", "$2^5 \\times 3$"],
        "correct": 0,
        "solution": "$144 = 16 \\times 9 = 2^4 \\times 3^2$."
    },
    {
        "id": 5,
        "question": "If $P = 2^3 \\times 3^4 \\times 5^2$ and $Q = 2^2 \\times 3^2 \\times 5^3 \\times 7^1$, what is their HCF?",
        "options": ["$2^3 \\times 3^4 \\times 5^3 \\times 7^1$", "$2^2 \\times 3^2 \\times 5^2$", "$2^5 \\times 3^6 \\times 5^5$", "$2 \\times 3 \\times 5$"],
        "correct": 1,
        "solution": "Take the minimum exponent for each common prime base: $2^{\\min(3,2)} \\times 3^{\\min(4,2)} \\times 5^{\\min(2,3)} = 2^2 \\times 3^2 \\times 5^2 = 4 \\times 9 \\times 25 = 900$."
    },
    {
        "id": 6,
        "question": "Which of the following pairs of numbers is co-prime?",
        "options": ["$14$ and $21$", "$15$ and $28$", "$18$ and $27$", "$22$ and $33$"],
        "correct": 1,
        "solution": "Factors of 15 are {1, 3, 5, 15}. Factors of 28 are {1, 2, 4, 7, 14, 28}. Their only common factor is 1, so $\\text{HCF}(15, 28) = 1$ (co-prime)."
    },
    {
        "id": 7,
        "question": "What is the HCF of $48$ and $72$?",
        "options": ["$12$", "$16$", "$24$", "$36$"],
        "correct": 2,
        "solution": "$48 = 24 \\times 2$ and $72 = 24 \\times 3$. The greatest common divisor is 24."
    },
    {
        "id": 8,
        "question": "A milkman has containers holding $40$ litres and $60$ litres of milk. What is the maximum capacity of a measuring cup that can measure milk from both containers in an exact number of pours?",
        "options": ["$5\\text{ L}$", "$10\\text{ L}$", "$20\\text{ L}$", "$30\\text{ L}$"],
        "correct": 2,
        "solution": "Maximum capacity $= \\text{HCF}(40, 60) = 20\\text{ litres}$."
    },
    {
        "id": 9,
        "question": "What does a counterexample do to a mathematical conjecture?",
        "options": ["Proves it for all cases", "Proves that it is FALSE", "Makes it a theorem", "Shows it is true only for even numbers"],
        "correct": 1,
        "solution": "A counterexample is a specific case that violates the conjecture, demonstrating conclusively that the statement is false."
    },
    {
        "id": 10,
        "question": "Find the HCF of $84$ and $126$:",
        "options": ["$14$", "$21$", "$42$", "$84$"],
        "correct": 2,
        "solution": "$84 = 42 \\times 2$ and $126 = 42 \\times 3$. The HCF is 42."
    },

    # Questions 11 to 20 (Slide 18)
    {
        "id": 11,
        "question": "What is the LCM of two co-prime numbers $a$ and $b$?",
        "options": ["$1$", "$a + b$", "$a \\times b$", "$\\frac{a}{b}$"],
        "correct": 2,
        "solution": "For co-prime numbers, $\\text{HCF} = 1$. Since $\\text{HCF} \\times \\text{LCM} = a \\times b$, $\\text{LCM} = a \\times b$."
    },
    {
        "id": 12,
        "question": "Toran strips of lengths $10\text{ cm}$ and $15\text{ cm}$ are aligned end-to-end. What is the shortest total length at which both rows reach the exact same point?",
        "options": ["$25\text{ cm}$", "$30\text{ cm}$", "$45\text{ cm}$", "$60\text{ cm}$"],
        "correct": 1,
        "solution": "Shortest aligned length $= \\text{LCM}(10, 15) = 30\\text{ cm}$."
    },
    {
        "id": 13,
        "question": "How many $10\text{ cm}$ strips and $15\text{ cm}$ strips are in the $30\text{ cm}$ toran?",
        "options": ["3 of $10\text{ cm}$ and 2 of $15\text{ cm}$", "2 of $10\text{ cm}$ and 3 of $15\text{ cm}$", "3 of each", "2 of each"],
        "correct": 0,
        "solution": "$30 / 10 = 3$ strips, and $30 / 15 = 2$ strips."
    },
    {
        "id": 14,
        "question": "Traffic lights at three junctions change after every $48$, $72$, and $108$ seconds respectively. If they change simultaneously at 8:00 AM, when will they change together next?",
        "options": ["8:07:12 AM (432 s)", "8:05:00 AM", "8:10:00 AM", "8:04:32 AM"],
        "correct": 0,
        "solution": "$\\text{LCM}(48, 72, 108) = 2^4 \\times 3^3 = 16 \\times 27 = 432\\text{ seconds} = 7\\text{ min } 12\\text{ s}$. Next sync is at 8:07:12 AM."
    },
    {
        "id": 15,
        "question": "If $X = 2^3 \\times 3^1 \\times 5^2$ and $Y = 2^1 \\times 3^3 \\times 5^1$, what is $\\text{LCM}(X, Y)$?",
        "options": ["$2^1 \\times 3^1 \\times 5^1$", "$2^3 \\times 3^3 \\times 5^2$", "$2^4 \\times 3^4 \\times 5^3$", "$2^3 \\times 3^3$"],
        "correct": 1,
        "solution": "Take the maximum power of each prime base: $2^{\\max(3,1)} \\times 3^{\\max(1,3)} \\times 5^{\\max(2,1)} = 2^3 \\times 3^3 \\times 5^2 = 8 \\times 27 \\times 25 = 5400$."
    },
    {
        "id": 16,
        "question": "Find the smallest number which when divided by $12, 16,$ and $24$ leaves remainder $0$:",
        "options": ["$24$", "$36$", "$48$", "$96$"],
        "correct": 2,
        "solution": "Smallest divisible number $= \\text{LCM}(12, 16, 24) = 48$."
    },
    {
        "id": 17,
        "question": "What is the LCM of $25$ and $30$?",
        "options": ["$75$", "$150$", "$225$", "$300$"],
        "correct": 1,
        "solution": "$25 = 5^2$ and $30 = 2 \\times 3 \\times 5$. $\\text{LCM} = 2 \\times 3 \\times 5^2 = 150$."
    },
    {
        "id": 18,
        "question": "Ravi visits a gym every 4 days, while Sameer visits every 6 days. If both met on June 1st, after how many days will they meet again?",
        "options": ["$10\\text{ days}$", "$12\\text{ days}$", "$24\\text{ days}$", "$2\\text{ days}$"],
        "correct": 1,
        "solution": "$\\text{LCM}(4, 6) = 12\\text{ days}$."
    },
    {
        "id": 19,
        "question": "What is the relationship between the common multiples of two numbers and their LCM?",
        "options": ["Every common multiple is a factor of the LCM", "Every common multiple is an exact multiple of the LCM", "Common multiples have no relation to LCM", "There are only 2 common multiples"],
        "correct": 1,
        "solution": "All common multiples of $a$ and $b$ are exact positive integer multiples of $\\text{LCM}(a, b)$."
    },
    {
        "id": 20,
        "question": "What is the LCM of $11$ and $13$?",
        "options": ["$24$", "$143$", "$1$", "$286$"],
        "correct": 1,
        "solution": "Both 11 and 13 are prime. For co-prime numbers, $\\text{LCM} = 11 \\times 13 = 143$."
    },

    # Questions 21 to 30 (Slide 19)
    {
        "id": 21,
        "question": "If $b$ is a multiple of $a$ (e.g. $a = 8, b = 32$), what is $\\text{HCF}(a, b)$?",
        "options": ["$a$ (the smaller number)", "$b$ (the larger number)", "$1$", "$a \\times b$"],
        "correct": 0,
        "solution": "When $a \\mid b$, the smaller number $a$ divides both numbers completely, so $\\text{HCF}(a, b) = a$."
    },
    {
        "id": 22,
        "question": "If $b$ is a multiple of $a$ (e.g. $a = 8, b = 32$), what is $\\text{LCM}(a, b)$?",
        "options": ["$a$ (the smaller number)", "$b$ (the larger number)", "$a \\times b$", "$2a$"],
        "correct": 1,
        "solution": "When $a \\mid b$, the larger number $b$ is a multiple of both $a$ and $b$, so $\\text{LCM}(a, b) = b$."
    },
    {
        "id": 23,
        "question": "What is the HCF and LCM of $12$ and $60$?",
        "options": ["$\\text{HCF}=12, \\text{LCM}=60$", "$\\text{HCF}=6, \\text{LCM}=120$", "$\\text{HCF}=60, \\text{LCM}=12$", "$\\text{HCF}=1, \\text{LCM}=720$"],
        "correct": 0,
        "solution": "Since $60 = 12 \\times 5$, by the Multiple Rule: $\\text{HCF} = 12$ and $\\text{LCM} = 60$."
    },
    {
        "id": 24,
        "question": "Given $\\text{HCF}(18, 24) = 6$. If both numbers are multiplied by $5$, what is $\\text{HCF}(90, 120)$?",
        "options": ["$6$", "$15$", "$30$", "$60$"],
        "correct": 2,
        "solution": "By the Scaling Property: $\\text{HCF}(5a, 5b) = 5 \\times \\text{HCF}(a, b) = 5 \\times 6 = 30$."
    },
    {
        "id": 25,
        "question": "In the simultaneous division ladder method for two numbers, how do you obtain the LCM?",
        "options": ["Multiply divisors on the left column only", "Multiply divisors on left column by the bottom quotients in an L-shape", "Add all divisors and quotients", "Multiply bottom row only"],
        "correct": 1,
        "solution": "The LCM is obtained by multiplying all common divisors in the left column with all final co-prime quotients in the bottom row (the L-shape)."
    },
    {
        "id": 26,
        "question": "Find the HCF of $160$ and $240$ by factoring out $80$ upfront:",
        "options": ["$40$", "$80$", "$120$", "$160$"],
        "correct": 1,
        "solution": "$160 = 80 \\times 2$ and $240 = 80 \\times 3$. Since $\\text{HCF}(2, 3) = 1$, $\\text{HCF} = 80 \\times 1 = 80$."
    },
    {
        "id": 27,
        "question": "Using the same extraction $160 = 80 \\times 2$ and $240 = 80 \\times 3$, what is their LCM?",
        "options": ["$240$", "$360$", "$480$", "$720$"],
        "correct": 2,
        "solution": "$\\text{LCM} = 80 \\times \\text{LCM}(2, 3) = 80 \\times 6 = 480$."
    },
    {
        "id": 28,
        "question": "Which algebraic expression describes numbers that are divisible by both $4$ and $5$?",
        "options": ["$9n$", "$20n$", "$4n + 5$", "$40n$"],
        "correct": 1,
        "solution": "$\\text{LCM}(4, 5) = 20$. Therefore, all numbers divisible by both 4 and 5 are multiples of 20, represented by $20n$."
    },
    {
        "id": 29,
        "question": "What is the HCF of any two consecutive positive integers $n$ and $n + 1$?",
        "options": ["$1$", "$2$", "$n$", "$n(n+1)$"],
        "correct": 0,
        "solution": "Any divisor of both $n$ and $n+1$ must divide their difference: $(n+1) - n = 1$. Hence $\\text{HCF}(n, n+1) = 1$ always (consecutive integers are always co-prime)!"
    },
    {
        "id": 30,
        "question": "What is the LCM of two consecutive positive integers $n$ and $n + 1$?",
        "options": ["$n + 1$", "$n \\times (n + 1)$", "$2n + 1$", "$1$"],
        "correct": 1,
        "solution": "Since consecutive integers are co-prime, their $\\text{LCM} = n \\times (n + 1)$."
    },

    # Questions 31 to 40 (Slide 20)
    {
        "id": 31,
        "question": "The HCF and LCM of two numbers are $9$ and $270$ respectively. If one number is $45$, what is the other number?",
        "options": ["$36$", "$54$", "$63$", "$90$"],
        "correct": 1,
        "solution": "Using $a \\times b = \\text{HCF} \\times \\text{LCM}$: $b = (9 \\times 270) / 45 = 2430 / 45 = 54$."
    },
    {
        "id": 32,
        "question": "The product of two numbers is $2160$ and their HCF is $12$. What is their LCM?",
        "options": ["$144$", "$180$", "$216$", "$360$"],
        "correct": 1,
        "solution": "$\\text{LCM} = (a \\times b) / \\text{HCF} = 2160 / 12 = 180$."
    },
    {
        "id": 33,
        "question": "Can two numbers have an HCF of $15$ and an LCM of $175$?",
        "options": ["Yes, always", "No, because the HCF must always divide the LCM completely", "Yes, if one is prime", "Only if both are odd"],
        "correct": 1,
        "solution": "The HCF must always be an exact divisor of the LCM. $175 / 15 = 11.666\\dots$ (not an integer). Therefore, no such numbers can exist!"
    },
    {
        "id": 34,
        "question": "For three numbers $a, b, c$, does $\\text{HCF}(a, b, c) \\times \\text{LCM}(a, b, c) = a \\times b \\times c$ hold true?",
        "options": ["Yes, it is the general product theorem", "No, it is generally false due to pairwise prime overlaps", "Only when all three are odd", "Only when all three are prime powers"],
        "correct": 1,
        "solution": "The identity holds strictly for TWO numbers only. For three numbers, pairwise common prime factors lead to duplication, making the equation generally false."
    },
    {
        "id": 35,
        "question": "Find the HCF of $18, 24,$ and $36$:",
        "options": ["$2$", "$3$", "$6$", "$12$"],
        "correct": 2,
        "solution": "Common divisors of 18, 24, 36 are {1, 2, 3, 6}. The greatest is 6."
    },
    {
        "id": 36,
        "question": "Find the LCM of $18, 24,$ and $36$:",
        "options": ["$36$", "$48$", "$72$", "$144$"],
        "correct": 2,
        "solution": "$18 = 2 \\times 3^2$, $24 = 2^3 \\times 3$, $36 = 2^2 \\times 3^2$. $\\text{LCM} = 2^3 \\times 3^2 = 8 \\times 9 = 72$."
    },
    {
        "id": 37,
        "question": "Which ancient Indian mathematician coined the term 'Niruddha' for LCM in the Gaṇitasārasaṅgraha?",
        "options": ["Āryabhaṭa", "Brahmagupta", "Mahāvīrācārya", "Bhāskarācārya"],
        "correct": 2,
        "solution": "Acharya Mahāvīrācārya (c. 850 CE) coined 'Niruddha' and provided the world's first codified LCM rules."
    },
    {
        "id": 38,
        "question": "What was Āryabhaṭa's Kuṭṭaka algorithm primarily used for?",
        "options": ["Finding square roots", "Solving linear indeterminate equations via reciprocal division (Euclidean GCD)", "Finding circle circumference", "Constructing Vedic altars"],
        "correct": 1,
        "solution": "Āryabhaṭa's Kuṭṭaka (pulverizer) algorithm systematically divides remainders to find GCD and solve Diophantine equations."
    },
    {
        "id": 39,
        "question": "The HCF of two numbers is $13$ and their LCM is $1989$. If one number is $117$, find the other number:",
        "options": ["$169$", "$221$", "$247$", "$289$"],
        "correct": 1,
        "solution": "$b = (13 \\times 1989) / 117 = 25857 / 117 = 221$."
    },
    {
        "id": 40,
        "question": "A electronic device beeps every $60$ seconds and another beeps every $62$ seconds. If they beep together at 10:00 AM, at what time will they next beep together?",
        "options": ["10:31 AM (1860 seconds)", "10:15 AM", "10:60 AM", "11:02 AM"],
        "correct": 0,
        "solution": "$\\text{LCM}(60, 62) = \\text{LCM}(2 \\times 30, 2 \\times 31) = 2 \\times 30 \\times 31 = 1860\\text{ seconds} = 31\\text{ minutes}$. Next simultaneous beep is at 10:31 AM!"
    }
]

code = f'''# -*- coding: utf-8 -*-
"""
Class 7 Mathematics - Chapter 11: Finding Common Ground (HCF & LCM) Data File
Generated automatically.
"""

SLIDES_DATA = {json.dumps(SLIDES_DATA, indent=2, ensure_ascii=False)}

QUIZ_QUESTIONS = {json.dumps(QUIZ_QUESTIONS, indent=2, ensure_ascii=False)}
'''

code = code.replace(': null', ': None')

with open('.agents/class7_math_finding_common_ground_data.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Generated .agents/class7_math_finding_common_ground_data.py successfully!")

