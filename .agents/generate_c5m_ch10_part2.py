# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 10: Symmetrical Designs
Part 2: Slides 9 to 16 (Theory, Narration 195-215 words, 16 Checkpoints)
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Digit Symmetry",
        "tagline": "Single Digit Analysis • Reflection & Rotational Properties of Digits 0 to 9",
        "lecture": (
            "Just as we explored English alphabets, we can examine mathematical numerals from 0 to 9 for symmetrical properties. "
            "Write the ten digits neatly using standard digital or sans-serif forms: 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9. Notice digit 0. "
            "Digit 0 is an oval ellipse with both vertical and horizontal lines of reflection symmetry, and it also possesses rotational "
            "symmetry of order 2 because rotating it by a 1/2 turn of 180 degrees leaves it completely unchanged. Digit 8 is equally "
            "remarkable: when drawn with equal top and bottom loops, digit 8 has both vertical and horizontal mirror symmetry, as well "
            "as rotational symmetry of order 2. In contrast, digit 3 drawn with identical rounded arcs has only a horizontal line of reflection "
            "symmetry, but no rotational symmetry, because turning 3 upside down makes it point backwards. What about digits 6 and 9? "
            "Neither 6 nor 9 has reflection symmetry on its own, but they form a magical rotational pair: rotating digit 6 by a 1/2 turn "
            "transforms it exactly into digit 9, and rotating digit 9 by a 1/2 turn yields digit 6! Digits 2, 4, 5, and 7 possess neither "
            "line nor rotational symmetry. Analyzing numbers mathematically connects arithmetic directly to geometric art."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed text-slate-300">
            <div class="overflow-x-auto">
                <table class="w-full text-left font-mono text-[11px] border border-slate-700">
                    <thead class="bg-slate-800 text-slate-300">
                        <tr>
                            <th class="p-1.5 border-b border-slate-700">Digit</th>
                            <th class="p-1.5 border-b border-slate-700">Reflection Lines</th>
                            <th class="p-1.5 border-b border-slate-700">1/2 Turn (180°) Rotation?</th>
                            <th class="p-1.5 border-b border-slate-700">Classification</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800">
                        <tr>
                            <td class="p-1.5 text-amber-300 font-bold">0</td>
                            <td class="p-1.5 text-emerald-400">Vertical + Horizontal (2)</td>
                            <td class="p-1.5 text-emerald-400">Yes (looks like 0)</td>
                            <td class="p-1.5 text-slate-300">Both symmetries</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 text-amber-300 font-bold">8</td>
                            <td class="p-1.5 text-emerald-400">Vertical + Horizontal (2)</td>
                            <td class="p-1.5 text-emerald-400">Yes (looks like 8)</td>
                            <td class="p-1.5 text-slate-300">Both symmetries</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 text-cyan-300 font-bold">1 (straight bar)</td>
                            <td class="p-1.5 text-emerald-400">Vertical + Horizontal (2)</td>
                            <td class="p-1.5 text-emerald-400">Yes (looks like 1)</td>
                            <td class="p-1.5 text-slate-300">Both (as simple bar |)</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 text-cyan-300 font-bold">3</td>
                            <td class="p-1.5 text-amber-400">Horizontal only (1)</td>
                            <td class="p-1.5 text-rose-400">No (inverts backwards)</td>
                            <td class="p-1.5 text-slate-300">Reflection only</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 text-purple-400 font-bold">6 and 9</td>
                            <td class="p-1.5 text-rose-400">None (0)</td>
                            <td class="p-1.5 text-emerald-400">Yes (swap: 6 ↔ 9)</td>
                            <td class="p-1.5 text-slate-300">Rotational pair</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 text-rose-400 font-bold">2, 4, 5, 7</td>
                            <td class="p-1.5 text-rose-400">None (0)</td>
                            <td class="p-1.5 text-rose-400">No</td>
                            <td class="p-1.5 text-slate-400">Asymmetrical</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="p-2 rounded bg-slate-900/60 border border-slate-800 text-[11px] text-slate-300">
                💡 <strong>Font Dependency:</strong> In standard sans-serif math font, digits 0 and 8 remain the undisputed champions having both reflection axes and 180° rotational invariance.
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "cp9_1",
                "question": "Which two single digits possess BOTH reflection symmetry and 1/2 turn rotational symmetry?",
                "options": [
                    "Digits 0 and 8",
                    "Digits 3 and 7",
                    "Digits 4 and 5",
                    "Digits 6 and 9"
                ],
                "answer": 0,
                "explanation": "Digits 0 and 8 can be folded horizontally and vertically, and rotating them by 180° leaves them identical."
            },
            {
                "id": "cp9_2",
                "question": "What happens when you rotate digit 6 by a 1/2 turn (180 degrees)?",
                "options": [
                    "It transforms into digit 9",
                    "It stays exactly as digit 6",
                    "It becomes a plus sign",
                    "It turns into digit 8"
                ],
                "answer": 0,
                "explanation": "A 180-degree rotation of 6 places its loop at the top and stem curving down, matching digit 9."
            }
        ]
    },

    {
        "id": 10,
        "title": "Symmetrical Numbers",
        "tagline": "Numerical Symmetries • Constructing 2-, 3- & 4-Digit Rotational Palindromes",
        "lecture": (
            "When we combine symmetrical digits into multi-digit numbers, fascinating mathematical patterns emerge. There are two "
            "distinct types of symmetrical numbers to investigate: reflection-symmetrical numbers, often called numerical palindromes, "
            "and rotation-symmetrical numbers, which look identical when viewed upside down. Consider the two-digit numbers. Number 11 "
            "and number 88 read the same backwards and forwards, and rotating number 88 upside down by a 1/2 turn still displays 88! "
            "Furthermore, number 69 has a thrilling property: although 6 and 9 are different digits, turning 69 upside down by 180 degrees "
            "swaps their positions and inverts each digit, producing 69 again. Now let us build three-digit rotational numbers. Think about "
            "placing digits that match themselves under a 1/2 turn at the ends, with a self-matching digit in the middle. Numbers like 101, "
            "181, 808, and 888 look identical whether held upright or upside down! In four digits, numbers such as 1001, 8008, 8888, "
            "and 6996 maintain complete rotational invariance under a 180-degree turn. Creating these numbers challenges our fluency with "
            "both place value and rotational symmetry, proving how numbers can possess geometric harmony just like visual designs, giving "
            "our mathematical thinking both numerical accuracy and profound artistic elegance across every calculation we perform."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed text-slate-300">
            <div class="grid grid-cols-3 gap-2 font-mono text-center">
                <div class="p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-amber-400 font-bold block text-xs">2-Digit Invariants</span>
                    <span class="text-emerald-400 font-bold text-sm block my-1">11, 88, 69, 96</span>
                    <span class="text-[10px] text-slate-400">180° rotation preserves reading</span>
                </div>
                <div class="p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-cyan-400 font-bold block text-xs">3-Digit Invariants</span>
                    <span class="text-emerald-400 font-bold text-sm block my-1">101, 181, 808, 888</span>
                    <span class="text-[10px] text-slate-400">Symmetric ends + center core</span>
                </div>
                <div class="p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-indigo-400 font-bold block text-xs">4-Digit Invariants</span>
                    <span class="text-emerald-400 font-bold text-sm block my-1">1001, 8008, 8888, 6996</span>
                    <span class="text-[10px] text-slate-400">Nested rotational symmetry</span>
                </div>
            </div>
            <div class="p-2.5 rounded-xl bg-slate-900/80 border border-slate-700 text-[11px] leading-relaxed">
                🔍 <strong>Upside-Down Test:</strong> If you write <strong>181</strong> or <strong>808</strong> on a card and rotate the card by 180°, an observer sitting opposite to you reads the exact same number without any ambiguity!
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "cp10_1",
                "question": "Which of the following 2-digit numbers looks identical after a 1/2 turn (180 degrees)?",
                "options": [
                    "Number 88 (and also 69)",
                    "Number 24",
                    "Number 75",
                    "Number 33"
                ],
                "answer": 0,
                "explanation": "Rotating 88 by 180° leaves each 8 as an 8 in the same position; 69 also rotates into 69."
            },
            {
                "id": "cp10_2",
                "question": "What happens to the 3-digit number 808 when turned upside down?",
                "options": [
                    "It remains exactly 808",
                    "It becomes 303",
                    "It becomes 888",
                    "It vanishes completely"
                ],
                "answer": 0,
                "explanation": "Each digit (8, 0, 8) matches itself under a 180° rotation, and the end digits swap into identical positions."
            }
        ]
    },

    {
        "id": 11,
        "title": "Modifying Designs",
        "tagline": "Geometric Transformation • Adding Shapes to Achieve 1/2 or 1/4 Turn Balance",
        "lecture": (
            "Symmetry is not just something we observe passively; it is an active design tool that artists and engineers use every day. "
            "Suppose you are given an incomplete or asymmetrical design composed of basic shapes like circles, triangles, or squares. "
            "How can you modify it so that it achieves perfect rotational symmetry? To give a pattern 1/2 turn rotational symmetry, "
            "every shape placed on one side must have an identical partner placed diametrically opposite across the center point, rotated "
            "by 180 degrees. For example, if you place a triangle pointing upward in the top-right quadrant, you must add an identical triangle "
            "pointing downward in the bottom-left quadrant. To elevate the design into 1/4 turn rotational symmetry, every shape must repeat "
            "in all four quadrants at 90-degree angular intervals. That means four identical triangles pointing outward in four cardinal "
            "directions! By systematically copying and rotating elements around a central anchor, you can transform simple doodles into "
            "mesmerizing circular mandalas, rangoli floor designs, and spinning ceiling fan rosettes. Practicing design modification trains "
            "our mathematical mind to foresee balance and rotational equilibrium before placing a single mark, unlocking the full creative "
            "potential of geometric transformation in artwork, architectural layouts, and textile patterns."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed text-slate-300">
            <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700">
                <h3 class="text-sm font-bold text-amber-400 mb-1">Rules for Symmetrical Modification</h3>
                <p>To upgrade any basic graphic layout into a rotationally balanced design:</p>
            </div>
            <div class="grid grid-cols-2 gap-2 font-mono">
                <div class="p-2.5 rounded-lg bg-indigo-950/30 border border-indigo-800/40">
                    <span class="text-cyan-300 font-bold block mb-1">Rule for 1/2 Turn (180° Balance):</span>
                    <p class="text-[11px] text-slate-300">Every element at coordinates (x, y) must have a twin at (-x, -y). Requires pairs of shapes diametrically opposite.</p>
                </div>
                <div class="p-2.5 rounded-lg bg-emerald-950/30 border border-emerald-800/40">
                    <span class="text-emerald-300 font-bold block mb-1">Rule for 1/4 Turn (90° Balance):</span>
                    <p class="text-[11px] text-slate-300">Every element must repeat in all 4 quadrants rotated by 90°. Requires shapes in sets of four around the center.</p>
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "cp11_1",
                "question": "To achieve 1/4 turn (order 4) rotational symmetry, how many copies of an added shape are needed around the center?",
                "options": [
                    "4 identical copies placed at 90° intervals",
                    "Only 2 copies placed opposite each other",
                    "3 copies placed in a straight line",
                    "1 copy anywhere on the page"
                ],
                "answer": 0,
                "explanation": "A 1/4 turn is 90 degrees. A full circle of 360 degrees requires 360 ÷ 90 = 4 identical copies distributed evenly."
            },
            {
                "id": "cp11_2",
                "question": "If a triangle points upward in the top-left quadrant, where must its partner point for 1/2 turn symmetry?",
                "options": [
                    "It must point downward in the bottom-right quadrant",
                    "It must point upward in the top-right quadrant",
                    "It must point to the left in the center",
                    "No partner is required"
                ],
                "answer": 0,
                "explanation": "A 1/2 turn rotates both the position (top-left to bottom-right) and orientation (upward to downward) by 180 degrees."
            }
        ]
    },

    {
        "id": 12,
        "title": "Grid Coloring",
        "tagline": "Two-Color Tiling • Coloring Quadrant Grids for 1/4 Turn Invariance",
        "lecture": (
            "One of the most engaging activities in NCERT Class 5 Mathematics is grid coloring puzzles. Imagine a square grid divided "
            "into four equal quadrants, like a 2 by 2 or 4 by 4 checkerboard. Your challenge is to color the small grid squares using "
            "only two colors—say, sunny yellow and deep navy blue—such that the entire square pattern looks completely identical after every "
            "1/4 turn of 90 degrees. If you color one square in the top-left quadrant yellow, which other squares must be colored yellow? "
            "Because a 1/4 turn rotates the top-left quadrant into the top-right quadrant, that corresponding square must also be yellow. "
            "A second 1/4 turn rotates it into the bottom-right quadrant, so that square must be yellow too. A third 1/4 turn rotates it into "
            "the bottom-left quadrant, requiring yellow as well. Thus, to maintain 1/4 turn rotational symmetry, colored cells must always "
            "appear in cyclic sets of four, or reside precisely at the central point where the rotation does not displace them! Grid coloring "
            "teaches us the mathematical foundation of tessellation and periodic tiling used in palace floors across Rajasthan and Mughal architecture, "
            "demonstrating how algebraic constraints govern geometric patterns and bring structured balance to colorful artistic creations."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed text-slate-300">
            <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700">
                <h3 class="text-sm font-bold text-amber-400 mb-1">The 4-Quadrant Orbit Rule</h3>
                <p>When creating a 1/4 turn (order 4) symmetrical grid with two colors:</p>
            </div>
            <div class="grid grid-cols-4 gap-1.5 font-mono text-center">
                <div class="p-2 rounded bg-amber-950/40 border border-amber-800/40">
                    <span class="text-amber-300 font-bold block text-xs">Orbit 1</span>
                    <span class="text-[10px] text-slate-400">Top-Left Cell (Q1)</span>
                </div>
                <div class="p-2 rounded bg-amber-950/40 border border-amber-800/40">
                    <span class="text-amber-300 font-bold block text-xs">Orbit 2</span>
                    <span class="text-[10px] text-slate-400">Top-Right Cell (Q2)</span>
                </div>
                <div class="p-2 rounded bg-amber-950/40 border border-amber-800/40">
                    <span class="text-amber-300 font-bold block text-xs">Orbit 3</span>
                    <span class="text-[10px] text-slate-400">Bottom-Right (Q3)</span>
                </div>
                <div class="p-2 rounded bg-amber-950/40 border border-amber-800/40">
                    <span class="text-amber-300 font-bold block text-xs">Orbit 4</span>
                    <span class="text-[10px] text-slate-400">Bottom-Left (Q4)</span>
                </div>
            </div>
            <div class="p-2.5 rounded bg-slate-900/60 border border-slate-800 text-[11px] text-slate-300">
                🎨 <strong>Golden Tiling Axiom:</strong> All 4 cells belonging to the same rotational orbit must share the exact same color. If even one cell differs in color, 1/4 turn symmetry is instantly broken!
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "cp12_1",
                "question": "If one corner cell of a 4x4 grid is colored blue, how many other corner cells must be colored blue for 1/4 turn symmetry?",
                "options": [
                    "All 3 remaining corner cells (total 4 blue corners)",
                    "Only 1 diagonally opposite corner cell",
                    "Zero other cells",
                    "Every cell in the entire grid"
                ],
                "answer": 0,
                "explanation": "A 1/4 turn rotates corners consecutively into all 4 positions; all 4 must share the same color to look identical."
            },
            {
                "id": "cp12_2",
                "question": "What happens if three quadrants have blue corners but the fourth quadrant has a red corner?",
                "options": [
                    "The pattern loses 1/4 turn rotational symmetry",
                    "The pattern gains 1/8 turn rotational symmetry",
                    "The symmetry remains completely unchanged",
                    "The grid turns into a circle"
                ],
                "answer": 0,
                "explanation": "Because one quadrant differs in color, a 90° rotation places red where blue was, so the view no longer matches."
            }
        ]
    },

    {
        "id": 13,
        "title": "Composite Polygons",
        "tagline": "Pattern Blocks • Combining Squares & Equilateral Triangles into Symmetrical Polyforms",
        "lecture": (
            "We can also construct rich symmetrical designs by assembling physical polygon blocks, such as squares, equilateral triangles, "
            "and regular hexagons. Let us examine what happens when these regular tiles join together into unified composite figures. "
            "An equilateral triangle by itself has 3 lines of reflection symmetry and rotational symmetry of order 3, matching at 120-degree "
            "turns. A square has 4 lines of reflection symmetry and rotational symmetry of order 4, matching at 90-degree turns. When you "
            "assemble a central square and attach four identical equilateral triangles to each of its four exterior edges, you form an 8-pointed "
            "star polygon. How much symmetry does this composite star possess? Because the underlying square has 4-fold rotational symmetry "
            "and the four attached triangles are completely identical, the composite star inherits order 4 rotational symmetry, matching "
            "its outline at 90, 180, 270, and 360 degrees! Furthermore, it possesses 4 reflection lines: two passing through opposite "
            "triangle points, and two cutting between adjoining triangles. Combining regular polygons allows mathematicians to synthesize "
            "higher orders of symmetry from simple foundational units, creating intricate geometric tessellations that captivate our eyes "
            "and deepen our appreciation of spatial structure across architecture, crystallography, and ornamental art."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed text-slate-300">
            <div class="overflow-x-auto">
                <table class="w-full text-left font-mono text-[11px] border border-slate-700">
                    <thead class="bg-slate-800 text-slate-300">
                        <tr>
                            <th class="p-1.5 border-b border-slate-700">Polygon / Composite</th>
                            <th class="p-1.5 border-b border-slate-700">Reflection Lines</th>
                            <th class="p-1.5 border-b border-slate-700">Rotational Order</th>
                            <th class="p-1.5 border-b border-slate-700">Smallest Turn Angle</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800">
                        <tr>
                            <td class="p-1.5 text-amber-300 font-bold">Equilateral Triangle</td>
                            <td class="p-1.5 text-slate-200">3 lines</td>
                            <td class="p-1.5 text-cyan-300 font-bold">Order 3</td>
                            <td class="p-1.5 text-emerald-400">120° (1/3 turn)</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 text-amber-300 font-bold">Square</td>
                            <td class="p-1.5 text-slate-200">4 lines</td>
                            <td class="p-1.5 text-cyan-300 font-bold">Order 4</td>
                            <td class="p-1.5 text-emerald-400">90° (1/4 turn)</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 text-amber-300 font-bold">Regular Hexagon</td>
                            <td class="p-1.5 text-slate-200">6 lines</td>
                            <td class="p-1.5 text-cyan-300 font-bold">Order 6</td>
                            <td class="p-1.5 text-emerald-400">60° (1/6 turn)</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 text-purple-300 font-bold">Square + 4 Triangles Star</td>
                            <td class="p-1.5 text-slate-200">4 lines</td>
                            <td class="p-1.5 text-cyan-300 font-bold">Order 4</td>
                            <td class="p-1.5 text-emerald-400">90° (1/4 turn)</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="p-2 rounded bg-slate-900/60 border border-slate-800 text-[11px] text-slate-300">
                ⭐ <strong>Regular Polygon Rule:</strong> A regular polygon with n equal sides always has exactly n lines of reflection symmetry and rotational symmetry of order n (smallest angle = 360° ÷ n).
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "cp13_1",
                "question": "What is the smallest angle of rotation that leaves an equilateral triangle unchanged?",
                "options": [
                    "120 degrees (1/3 of a full turn)",
                    "90 degrees (1/4 of a full turn)",
                    "180 degrees (1/2 of a full turn)",
                    "45 degrees (1/8 of a full turn)"
                ],
                "answer": 0,
                "explanation": "An equilateral triangle has 3 equal sides and angles: 360° ÷ 3 = 120°."
            },
            {
                "id": "cp13_2",
                "question": "How many lines of reflection symmetry does a composite star made of a square with four triangles have?",
                "options": [
                    "4 lines of symmetry",
                    "Only 1 line of symmetry",
                    "12 lines of symmetry",
                    "Zero lines of symmetry"
                ],
                "answer": 0,
                "explanation": "The 4-pointed star has 2 diagonal axes and 2 edge-bisecting axes, giving 4 lines of reflection symmetry."
            }
        ]
    },

    {
        "id": 14,
        "title": "Block Printing",
        "tagline": "Heritage Craft of Rajasthan • Hand-Carved Teak Blocks & Textile Repetition",
        "lecture": (
            "One of India's most celebrated cultural treasures is the traditional art of wooden block printing, practiced with mastery "
            "for centuries in heritage craft centers of Rajasthan like Bagru and Sanganer near Jaipur. Master artisans, known as Chippas, "
            "carve intricate floral motifs, paisleys, dancing peacocks, and geometric borders onto seasoned teak and shisham wood blocks. "
            "Each carved block has a sturdy wooden handle on the back and tiny air escape holes so dye spreads evenly across the cloth. "
            "To print fabric, the artisan presses the carved face into a tray of natural herbal dye—such as indigo blue, madder red, or turmeric "
            "yellow—and stamps it firmly onto stretched cotton fabric with a swift strike of the fist. By stamping the block repeatedly along "
            "a straight guideline, a continuous rhythmic border emerges. Understanding the symmetry of the carved block is crucial: if a block "
            "has reflection symmetry, stamping it directly produces a mirror-balanced motif, while asymmetrical blocks require careful "
            "flipping or rotation to align adjoining panels seamlessly across multi-meter saree lengths. This living craft proves how mathematical "
            "principles of translation, reflection, and precise spacing have guided rural Indian textile artists for countless generations, "
            "blending everyday utilitarian fabrics with breathtaking geometric perfection."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed text-slate-300">
            <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700">
                <h3 class="text-sm font-bold text-amber-400 mb-1">Traditional Rajasthani Hand-Block Printing</h3>
                <p>Bagru and Sanganer block printing uses the mathematics of translation, reflection, and rotation on handloom cotton:</p>
            </div>
            <div class="grid grid-cols-3 gap-2 text-center font-mono">
                <div class="p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-amber-400 font-bold block text-xs">1. Carved Teak Block</span>
                    <p class="text-[10px] text-slate-400">Artisan carves relief motif with symmetry guides.</p>
                </div>
                <div class="p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-cyan-400 font-bold block text-xs">2. Natural Dye Dip</span>
                    <p class="text-[10px] text-slate-400">Pad dipped in indigo, madder, or harda dyes.</p>
                </div>
                <div class="p-2 rounded bg-emerald-950/40 border border-emerald-800/40">
                    <span class="text-emerald-400 font-bold block text-xs">3. Repetitive Stamping</span>
                    <p class="text-[10px] text-slate-300">Grid alignment creates continuous saree patterns!</p>
                </div>
            </div>
            <div class="p-2.5 rounded bg-slate-900/60 border border-slate-800 text-[11px] text-slate-300">
                🌿 <strong>Living Mathematical Heritage:</strong> Chippa artisans calculate precise millimeter repeat intervals entirely by eye, ensuring that neighboring block impressions merge into seamless geometric tessellations.
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "cp14_1",
                "question": "Which historic Indian state is world-renowned for traditional wooden block printing crafts like Bagru and Sanganer?",
                "options": [
                    "Rajasthan",
                    "Kerala",
                    "Assam",
                    "Punjab"
                ],
                "answer": 0,
                "explanation": "Rajasthan, especially centers like Bagru and Sanganer near Jaipur, is the historic heartland of hand-carved wooden block printing."
            },
            {
                "id": "cp14_2",
                "question": "How does repeated stamping of a single carved block generate an extensive saree border?",
                "options": [
                    "Through linear translation and repetitive geometric alignment along a guide",
                    "By melting the wooden block with boiling water",
                    "By cutting the cloth into tiny squares",
                    "By painting each flower freehand with a brush"
                ],
                "answer": 0,
                "explanation": "Repetitive stamping translates the identical block along a straight guideline, creating an evenly spaced decorative pattern."
            }
        ]
    },

    {
        "id": 15,
        "title": "Rotating Blocks",
        "tagline": "Circular Medallions • Stamping a Single Block 4 Times with 1/4 Turn (90°) Steps",
        "lecture": (
            "Artisans in Rajasthan use an ingenious geometric technique to create magnificent circular medallions and floral rosettes "
            "using just one single corner block! Instead of carving a massive, heavy circular block, the craftsman carves a single triangular "
            "or quadrant block that represents exactly 1/4 of the intended rosette. To print the full medallion, the artisan stamps the block "
            "once in the top-left position. Then, the artisan rotates the wooden block clockwise by a 1/4 turn of 90 degrees and stamps it "
            "in the top-right position. Turning the block by another 1/4 turn of 90 degrees produces the bottom-right quadrant, and a final "
            "1/4 turn completes the bottom-left quadrant. When the four prints meet at the center, an exquisite, perfectly unified 4-fold "
            "symmetrical medallion appears on the fabric! By rotating a single block four times, the printer generates order 4 rotational "
            "symmetry with unmatched efficiency. Alternating 1/2 turns can similarly produce zigzag borders and wave motifs. Rotational "
            "stamping proves how mathematics multiplies artistic creativity while conserving precious craftsmanship resources, turning a "
            "quarter-motif into a breathtaking whole through the elegant power of angular repetition, delighting viewers across the globe "
            "with seamless symmetry, rhythmic harmony, and enduring cultural beauty."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed text-slate-300">
            <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700">
                <h3 class="text-sm font-bold text-amber-400 mb-1">Creating a 4-Fold Rosette with 1 Block</h3>
                <p>Follow the 4-step rotational stamping cycle around a central registration point:</p>
            </div>
            <div class="grid grid-cols-4 gap-1.5 font-mono text-center">
                <div class="p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-amber-400 font-bold block text-xs">Stamp 1 (0°)</span>
                    <span class="text-[10px] text-slate-400">Top-Left Quadrant</span>
                </div>
                <div class="p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-cyan-400 font-bold block text-xs">Stamp 2 (90°)</span>
                    <span class="text-[10px] text-slate-400">Top-Right (+ 1/4 turn)</span>
                </div>
                <div class="p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-indigo-400 font-bold block text-xs">Stamp 3 (180°)</span>
                    <span class="text-[10px] text-slate-400">Bottom-Right (+ 1/4 turn)</span>
                </div>
                <div class="p-2 rounded bg-emerald-950/60 border border-emerald-800/40">
                    <span class="text-emerald-400 font-bold block text-xs">Stamp 4 (270°)</span>
                    <span class="text-[10px] text-slate-300">Bottom-Left (Complete!)</span>
                </div>
            </div>
            <div class="p-2.5 rounded bg-slate-900/60 border border-slate-800 text-[11px] text-slate-300">
                ✨ <strong>Efficiency in Craft:</strong> The woodcarver spends time carving only one small 90° sector block, yet the printer generates a lavish, perfectly centered circular mandala!
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "cp15_1",
                "question": "How many times must a 90° quadrant block be stamped to complete a full circular medallion?",
                "options": [
                    "Exactly 4 times (each turned by 90°)",
                    "Only 2 times",
                    "6 times",
                    "10 times"
                ],
                "answer": 0,
                "explanation": "A full circle is 360°. Stamping with 90° turns requires 360 ÷ 90 = 4 stamps to fill all four quadrants."
            },
            {
                "id": "cp15_2",
                "question": "What kind of symmetry does the resulting 4-quadrant stamped rosette possess?",
                "options": [
                    "Rotational symmetry of order 4 (invariance at every 1/4 turn)",
                    "Only reflection symmetry with 1 vertical line",
                    "No symmetry whatsoever",
                    "Rotational symmetry of order 2 only"
                ],
                "answer": 0,
                "explanation": "Because the same motif is repeated at 90-degree intervals in all 4 quadrants, it has order 4 rotational symmetry."
            }
        ]
    },

    {
        "id": 16,
        "title": "Vegetable Stamping",
        "tagline": "Botanical Symmetry • Ladyfinger (Okra) 5-Fold Stars & Concentric Onion Prints",
        "lecture": (
            "Nature is the greatest geometric artist of all, and we can explore its wonders right in our home kitchens through vegetable "
            "stamping projects. Take a fresh ladyfinger, known across India as bhindi or okra. When you slice it crosswise with a kitchen "
            "knife, examine its cut cross-section. The cross-section reveals five seed chambers arranged evenly around the central axis, "
            "forming a natural five-pointed pentagonal star! An okra cross-section possesses rotational symmetry of order 5, matching its "
            "own outline after every 1/5 turn, which equals a rotation of 72 degrees. Dip the cut face of the ladyfinger into green, yellow, "
            "or red poster paint and stamp it onto paper to create stunning star-flowered cards. Next, slice an onion in half crosswise: "
            "the concentric rings display circular reflection symmetry radiating from the core. Carving simple notches into a halved potato "
            "lets you build custom printing blocks for geometric triangles and chevrons. Exploring vegetable stamps connects botanical biology "
            "to mathematics, proving that rotational and reflection symmetry are written into the very architecture of living plants, "
            "nourishing both our physical bodies and our creative artistic imaginations through everyday organic geometry and vibrant botanical patterns, "
            "celebrating the endless harmony found throughout our natural world."
        ),
        "content_html": """
        <div class="space-y-3 text-xs leading-relaxed text-slate-300">
            <div class="overflow-x-auto">
                <table class="w-full text-left font-mono text-[11px] border border-slate-700">
                    <thead class="bg-slate-800 text-slate-300">
                        <tr>
                            <th class="p-1.5 border-b border-slate-700">Vegetable Stamp</th>
                            <th class="p-1.5 border-b border-slate-700">Cross-Section Shape</th>
                            <th class="p-1.5 border-b border-slate-700">Rotational Symmetry</th>
                            <th class="p-1.5 border-b border-slate-700">Smallest Turn Angle</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800">
                        <tr>
                            <td class="p-1.5 text-amber-300 font-bold">Ladyfinger (Okra / Bhindi)</td>
                            <td class="p-1.5 text-slate-200">5-pointed star (5 seed pods)</td>
                            <td class="p-1.5 text-emerald-400 font-bold">Order 5</td>
                            <td class="p-1.5 text-cyan-300">72° (1/5 of a turn)</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 text-amber-300 font-bold">Sliced Onion</td>
                            <td class="p-1.5 text-slate-200">Concentric circular rings</td>
                            <td class="p-1.5 text-emerald-400 font-bold">Infinite circular</td>
                            <td class="p-1.5 text-cyan-300">Continuous rotation</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 text-amber-300 font-bold">Carved Potato Triangle</td>
                            <td class="p-1.5 text-slate-200">Equilateral triangle stamp</td>
                            <td class="p-1.5 text-emerald-400 font-bold">Order 3</td>
                            <td class="p-1.5 text-cyan-300">120° (1/3 of a turn)</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 text-amber-300 font-bold">Carved Potato Diamond</td>
                            <td class="p-1.5 text-slate-200">Rhombus stamp</td>
                            <td class="p-1.5 text-emerald-400 font-bold">Order 2</td>
                            <td class="p-1.5 text-cyan-300">180° (1/2 of a turn)</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="p-2.5 rounded bg-emerald-950/30 border border-emerald-800/40 text-[11px] text-emerald-300">
                🌿 <strong>Nature's Mathematics:</strong> Flowers, starfruits, and okra pods grow with rotational symmetry so that seeds, sunlight absorption, and petals are distributed with maximum efficiency around their stem axis.
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "cp16_1",
                "question": "What order of rotational symmetry is typically displayed by the cross-section of a ladyfinger (okra)?",
                "options": [
                    "Order 5 (5-pointed star matching every 72°)",
                    "Order 2 (180° only)",
                    "Order 4 (90° only)",
                    "Order 1 (no rotational symmetry)"
                ],
                "answer": 0,
                "explanation": "A typical okra pod cross-section has 5 seed compartments radiating symmetrically, giving order 5 rotational symmetry (360° ÷ 5 = 72°)."
            },
            {
                "id": "cp16_2",
                "question": "Why do artisans and students use carved potatoes for stamping?",
                "options": [
                    "Potatoes are firm and easily carved into precise geometric shapes like triangles or stars",
                    "Potatoes change color when heated",
                    "Potatoes dissolve in water immediately",
                    "Potatoes only stamp squares"
                ],
                "answer": 0,
                "explanation": "The smooth, dense flesh of a raw potato allows easy carving of custom relief motifs that hold poster paint well."
            }
        ]
    }
]
