# -*- coding: utf-8 -*-
"""NCERT Class 7 Mathematics - Chapter 9: Geometric Twins (Congruence) Dataset"""

SLIDES_DATA = [
    {
        "id": "slide-1",
        "slide_num": 1,
        "section": "9.1",
        "title": "Geometric Twins: Introduction to Superposition & Congruence",
        "badge": "Foundations",
        "narration": "Welcome, seekers of geometry! I am Acharya Varāhamihira. In nature and temple architecture, we often behold figures that are exact twins: identical in shape and identical in size. In mathematics, this magnificent relationship is called Congruence!",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>What are Geometric Twins?</h4>\n                <p class='text-slate-300 text-sm mb-3'>\n                    Two geometric figures are said to be <strong>congruent</strong> (symbol: $\\cong$) if they have the <strong>exact same shape</strong> and the <strong>exact same size</strong>.\n                </p>\n                <div class='grid grid-cols-1 md:grid-cols-3 gap-3 my-3 text-xs'>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-amber-500/30'>\n                        <span class='text-amber-300 font-bold text-sm block mb-1'>1. Exact Same Shape</span>\n                        <p class='text-slate-300'>All corresponding angles and proportions match identically without distortion.</p>\n                    </div>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-cyan-500/30'>\n                        <span class='text-cyan-300 font-bold text-sm block mb-1'>2. Exact Same Size</span>\n                        <p class='text-slate-300'>All boundary lengths, perimeters, and enclosed areas are mathematically identical.</p>\n                    </div>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-emerald-500/30'>\n                        <span class='text-emerald-300 font-bold text-sm block mb-1'>3. Superposition Test</span>\n                        <p class='text-slate-300'>One figure can be placed directly over the other to cover it completely and precisely.</p>\n                    </div>\n                </div>\n                <div class='p-2.5 bg-slate-900 rounded-lg border border-slate-700 text-xs text-slate-300 mt-2'>\n                    <strong>The Congruence Symbol:</strong> Written as $\\cong$. It combines $=$ (equal size) with $\\sim$ (same shape). We write: $F_1 \\cong F_2$.\n                </div>\n            </div>\n        ",
        "sim_id": "sim-superposition-flipper",
        "checkpoints": [
            {
                "id": "cp1_1",
                "question": "What two conditions must hold for two geometric figures to be congruent?",
                "options": [
                    "Same shape only",
                    "Same size only",
                    "Exact same shape and exact same size",
                    "Different shapes with equal areas"
                ],
                "correct": 2,
                "explanation": "Congruence requires both identical shape (similarity) and identical size (equality of dimensions)."
            },
            {
                "id": "cp1_2",
                "question": "If figure A can be rotated and flipped to cover figure B exactly, what is true?",
                "options": [
                    "Figure A is larger than B",
                    "Figures A and B are congruent ($A \\cong B$)",
                    "Figure A has greater perimeter",
                    "They have different areas"
                ],
                "correct": 1,
                "explanation": "Rigid motions (translations, rotations, and reflections) preserve distance and angle, proving congruence by superposition."
            }
        ]
    },
    {
        "id": "slide-2",
        "slide_num": 2,
        "section": "9.1",
        "title": "Congruence of Simple Figures: Lines, Angles, Circles & Rectangles",
        "badge": "Simple Figures",
        "narration": "Before tackling triangles, observe how simple geometric figures achieve congruence. Two line segments are congruent if their lengths match. Two angles are congruent if their measures match. Circles depend solely on radii!",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Testing Congruence in Elementary Figures</h4>\n                <div class='grid grid-cols-1 md:grid-cols-2 gap-3 my-3 text-xs'>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-cyan-500/30'>\n                        <h5 class='text-cyan-300 font-bold mb-1'>Line Segments</h5>\n                        <p class='text-slate-300 mb-1'>$\\overline{AB} \\cong \\overline{CD} \\iff \\text{Length}(AB) = \\text{Length}(CD)$.</p>\n                        <p class='text-slate-400 text-[11px]'>Orientation in space does not matter; only the straight distance counts.</p>\n                    </div>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-amber-500/30'>\n                        <h5 class='text-amber-300 font-bold mb-1'>Angles</h5>\n                        <p class='text-slate-300 mb-1'>$\\angle ABC \\cong \\angle PQR \\iff m\\angle ABC = m\\angle PQR$.</p>\n                        <p class='text-slate-400 text-[11px]'>The length of the drawing arms does not affect angle measure.</p>\n                    </div>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-emerald-500/30'>\n                        <h5 class='text-emerald-300 font-bold mb-1'>Circles</h5>\n                        <p class='text-slate-300 mb-1'>$C_1 \\cong C_2 \\iff r_1 = r_2$.</p>\n                        <p class='text-slate-400 text-[11px]'>Two circles with equal radii can be superimposed to coincide completely.</p>\n                    </div>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-purple-500/30'>\n                        <h5 class='text-purple-300 font-bold mb-1'>Rectangles</h5>\n                        <p class='text-slate-300 mb-1'>$R_1 \\cong R_2 \\iff \\text{Length}_1 = \\text{Length}_2 \\text{ and } \\text{Breadth}_1 = \\text{Breadth}_2$.</p>\n                        <p class='text-slate-400 text-[11px]'>Both length and breadth must match pairwise.</p>\n                    </div>\n                </div>\n            </div>\n        ",
        "sim_id": "sim-simple-figures-congruence",
        "checkpoints": [
            {
                "id": "cp2_1",
                "question": "Two line segments are congruent if and only if they have:",
                "options": [
                    "The same slope",
                    "The same length",
                    "Parallel directions",
                    "The same starting point"
                ],
                "correct": 1,
                "explanation": "Two line segments are congruent when they have identical lengths, regardless of position or angle."
            },
            {
                "id": "cp2_2",
                "question": "Two circles are congruent if:",
                "options": [
                    "Their centers coincide",
                    "Their diameters are unequal",
                    "Their radii are equal ($r_1 = r_2$)",
                    "One circle is inside the other"
                ],
                "correct": 2,
                "explanation": "Equal radii guarantee identical circumference and enclosed area, making circles congruent."
            }
        ]
    },
    {
        "id": "slide-3",
        "slide_num": 3,
        "section": "9.2",
        "title": "Congruence of Triangles: 6 Parts & Vertex Correspondence",
        "badge": "Correspondence",
        "narration": "A triangle possesses 6 fundamental elements: 3 sides and 3 interior angles. When two triangles are congruent, all 6 pairs of corresponding parts are equal! Correct notation requires matching corresponding vertices in order.",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Vertex Correspondence & CPCTC</h4>\n                <p class='text-slate-300 text-sm mb-3'>\n                    When $\\triangle ABC \\cong \\triangle PQR$, the order of letters specifies which vertices map to which:\n                </p>\n                <div class='p-3 bg-slate-900 border border-amber-500/40 rounded-xl text-center my-3'>\n                    <span class='text-amber-300 font-bold text-base tracking-wide font-mono'>\n                        $$A \\leftrightarrow P, \\quad B \\leftrightarrow Q, \\quad C \\leftrightarrow R$$\n                    </span>\n                </div>\n                <div class='grid grid-cols-1 md:grid-cols-2 gap-3 my-3 text-xs'>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-cyan-500/30'>\n                        <h5 class='text-cyan-300 font-bold mb-1'>3 Corresponding Equal Sides:</h5>\n                        <p class='text-slate-300'>$AB = PQ, \\quad BC = QR, \\quad CA = RP$.</p>\n                    </div>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-emerald-500/30'>\n                        <h5 class='text-emerald-300 font-bold mb-1'>3 Corresponding Equal Angles:</h5>\n                        <p class='text-slate-300'>$\\angle A = \\angle P, \\quad \\angle B = \\angle Q, \\quad \\angle C = \\angle R$.</p>\n                    </div>\n                </div>\n                <div class='p-2 bg-slate-900 rounded border border-slate-700 text-xs text-slate-300'>\n                    <strong>CPCTC Principle:</strong> <em>Corresponding Parts of Congruent Triangles are Congruent</em>.\n                </div>\n            </div>\n        ",
        "sim_id": "sim-triangle-correspondence",
        "checkpoints": [
            {
                "id": "cp3_1",
                "question": "If $\\triangle ABC \\cong \\triangle FED$, which side corresponds to $BC$?",
                "options": [
                    "$FE$",
                    "$ED$",
                    "$FD$",
                    "$EF$"
                ],
                "correct": 1,
                "explanation": "Looking at vertex positions: $B$ is 2nd and $C$ is 3rd, corresponding to 2nd and 3rd letters $E$ and $D$, so $BC = ED$."
            },
            {
                "id": "cp3_2",
                "question": "What does CPCTC stand for?",
                "options": [
                    "Circular Parts of Congruent Triangles are Constant",
                    "Corresponding Parts of Congruent Triangles are Congruent",
                    "Congruent Points Cannot Touch Coordinates",
                    "Center Points Create Two Circles"
                ],
                "correct": 1,
                "explanation": "CPCTC is the foundational theorem allowing us to deduce unknown sides and angles once congruence is established."
            }
        ]
    },
    {
        "id": "slide-4",
        "slide_num": 4,
        "section": "9.2",
        "title": "SSS Congruence Criterion: Side-Side-Side Rigidity",
        "badge": "Criterion I",
        "narration": "Do we truly need to measure all 6 parts? No! The ancient builders knew that triangles are rigid. If three sides of one triangle equal three sides of another, the triangles are locked into congruence!",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>The SSS (Side-Side-Side) Criterion</h4>\n                <p class='text-slate-300 text-sm mb-3'>\n                    <strong>Theorem:</strong> If the three sides of one triangle are equal to the three corresponding sides of another triangle, then the two triangles are congruent.\n                </p>\n                <div class='p-3 bg-slate-900 border border-amber-500/40 rounded-xl text-center my-3'>\n                    <span class='text-amber-300 font-bold text-base font-mono'>\n                        $$AB = DE, \\quad BC = EF, \\quad AC = DF \\implies \\triangle ABC \\cong \\triangle DEF$$\n                    </span>\n                </div>\n                <div class='grid grid-cols-1 md:grid-cols-2 gap-3 my-3 text-xs'>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-amber-500/30'>\n                        <span class='text-amber-300 font-bold block mb-1'>Why Triangles are Structurally Rigid:</span>\n                        <p class='text-slate-300'>Unlike quadrilaterals which can flex into parallelograms, a 3-bar linkage cannot flex without altering side lengths. This makes SSS the principle of truss bridges!</p>\n                    </div>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-cyan-500/30'>\n                        <span class='text-cyan-300 font-bold block mb-1'>Automatic Angle Locking:</span>\n                        <p class='text-slate-300'>Once the 3 sides are pinned, the 3 interior angles are mathematically fixed and forced to match.</p>\n                    </div>\n                </div>\n            </div>\n        ",
        "sim_id": "sim-sss-congruence",
        "checkpoints": [
            {
                "id": "cp4_1",
                "question": "In $\\triangle ABC$ and $\\triangle XYZ$, $AB=5\\text{ cm}, BC=6\\text{ cm}, AC=7\\text{ cm}$ and $XY=5\\text{ cm}, YZ=6\\text{ cm}, XZ=7\\text{ cm}$. Are they congruent?",
                "options": [
                    "No, because angles are unknown",
                    "Yes, by SSS criterion ($\\triangle ABC \\cong \\triangle XYZ$)",
                    "Only if they have the same perimeter",
                    "Only if they are right-angled"
                ],
                "correct": 1,
                "explanation": "All three pairs of corresponding sides are equal, so the triangles are congruent by the SSS criterion."
            },
            {
                "id": "cp4_2",
                "question": "Why are triangular frameworks widely used in bicycle frames and bridges?",
                "options": [
                    "Triangles use less paint",
                    "SSS rigidity guarantees a triangle cannot change shape without changing side lengths",
                    "Triangles have 4 right angles",
                    "They roll faster"
                ],
                "correct": 1,
                "explanation": "SSS rigidity means a triangle is mechanically locked; no angle can flex once the sides are fixed."
            }
        ]
    },
    {
        "id": "slide-5",
        "slide_num": 5,
        "section": "9.2",
        "title": "SAS Congruence Criterion: The Included Angle Law",
        "badge": "Criterion II",
        "narration": "Now imagine holding two wooden rods of known lengths. If you fix the opening angle between them, the distance between their ends is permanently locked! This is the Side-Angle-Side criterion.",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>The SAS (Side-Angle-Side) Criterion</h4>\n                <p class='text-slate-300 text-sm mb-3'>\n                    <strong>Theorem:</strong> If two sides and the <strong>included angle</strong> of one triangle are equal to the corresponding two sides and the included angle of another triangle, the triangles are congruent.\n                </p>\n                <div class='p-3 bg-slate-900 border border-amber-500/40 rounded-xl text-center my-3'>\n                    <span class='text-amber-300 font-bold text-base font-mono'>\n                        $$AB = PQ, \\quad \\angle B = \\angle Q, \\quad BC = QR \\implies \\triangle ABC \\cong \\triangle PQR$$\n                    </span>\n                </div>\n                <div class='p-3 bg-rose-950/40 border border-rose-500/40 rounded-xl text-xs text-rose-200 my-2'>\n                    <strong>Crucial Condition: The Included Angle!</strong><br>\n                    The angle $\\angle B$ MUST be sandwiched directly between side $AB$ and side $BC$. An angle elsewhere does NOT guarantee congruence!\n                </div>\n            </div>\n        ",
        "sim_id": "sim-sas-congruence",
        "checkpoints": [
            {
                "id": "cp5_1",
                "question": "Which angle is the included angle between sides $PQ$ and $QR$ in $\\triangle PQR$?",
                "options": [
                    "$\\angle P$",
                    "$\\angle Q$",
                    "$\\angle R$",
                    "$\\angle PQR$ and $\\angle QPR$"
                ],
                "correct": 1,
                "explanation": "The vertex common to sides $PQ$ and $QR$ is $Q$, so the included angle is $\\angle Q$."
            },
            {
                "id": "cp5_2",
                "question": "If $AB = DE, BC = EF$ and $\\angle A = \\angle D$, can we apply SAS directly?",
                "options": [
                    "Yes, any angle works",
                    "No, because $\\angle A$ is not the included angle between sides $AB$ and $BC$",
                    "Yes, because all triangles are congruent",
                    "No, because $BC$ is larger"
                ],
                "correct": 1,
                "explanation": "SAS requires the included angle between the two known sides (which would be $\\angle B$, not $\\angle A$)."
            }
        ]
    },
    {
        "id": "slide-6",
        "slide_num": 6,
        "section": "9.2",
        "title": "The Included Angle Trap: Why Position Matters",
        "badge": "Caution Trap",
        "narration": "Beware this classic geometric trap! If the equal angle is not strictly included between the two equal sides, two entirely different triangles can be formed. Let us inspect this visually in our laboratory.",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Why the Angle Must Be Included</h4>\n                <p class='text-slate-300 text-sm mb-3'>\n                    Consider sides $a = 6\\text{ cm}$ and $b = 4\\text{ cm}$. If the angle between them is $50^\\circ$, only one unique third side can close the gap.\n                </p>\n                <div class='grid grid-cols-1 md:grid-cols-2 gap-3 my-3 text-xs'>\n                    <div class='p-3 bg-emerald-950/30 border border-emerald-500/30 rounded-xl'>\n                        <span class='text-emerald-300 font-bold block mb-1'>Included Angle (SAS &check;):</span>\n                        <p class='text-slate-300'>Angle $\\theta$ is clamped between the two arms. The third side has no freedom to swing; its length and directions are uniquely determined.</p>\n                    </div>\n                    <div class='p-3 bg-rose-950/30 border border-rose-500/30 rounded-xl'>\n                        <span class='text-rose-300 font-bold block mb-1'>Non-Included Angle (SSA &cross;):</span>\n                        <p class='text-slate-300'>The opposite side can swing like a pendulum, hitting the base line at two different points to create two non-congruent triangles!</p>\n                    </div>\n                </div>\n            </div>\n        ",
        "sim_id": "sim-included-angle-trap",
        "checkpoints": [
            {
                "id": "cp6_1",
                "question": "For sides $XY$ and $XZ$, which angle must be equal to apply SAS?",
                "options": [
                    "$\\angle Y$",
                    "$\\angle Z$",
                    "$\\angle X$",
                    "Any interior angle"
                ],
                "correct": 2,
                "explanation": "Vertex $X$ is shared by $XY$ and $XZ$, so $\\angle X$ is the included angle."
            },
            {
                "id": "cp6_2",
                "question": "What can happen when an angle is not included between two given sides?",
                "options": [
                    "The triangle always becomes equilateral",
                    "Two completely different non-congruent triangles may be formed (ambiguous case)",
                    "The perimeter becomes zero",
                    "The angles sum to $360^\\circ$"
                ],
                "correct": 1,
                "explanation": "The non-included side can pivot and strike the base in two distinct locations, producing two non-congruent triangles."
            }
        ]
    },
    {
        "id": "slide-7",
        "slide_num": 7,
        "section": "9.2",
        "title": "ASA Congruence Criterion: Angle-Side-Angle Baseline",
        "badge": "Criterion III",
        "narration": "Suppose two surveyors establish a baseline of fixed length. From either end, they aim telescopes at two specific angles. The lines of sight must meet at a single, unique point in the sky! This is the Angle-Side-Angle criterion.",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>The ASA (Angle-Side-Angle) Criterion</h4>\n                <p class='text-slate-300 text-sm mb-3'>\n                    <strong>Theorem:</strong> If two angles and the <strong>included side</strong> of one triangle are equal to the corresponding two angles and included side of another triangle, the two triangles are congruent.\n                </p>\n                <div class='p-3 bg-slate-900 border border-amber-500/40 rounded-xl text-center my-3'>\n                    <span class='text-amber-300 font-bold text-base font-mono'>\n                        $$\\angle B = \\angle Q, \\quad BC = QR, \\quad \\angle C = \\angle R \\implies \\triangle ABC \\cong \\triangle PQR$$\n                    </span>\n                </div>\n                <div class='grid grid-cols-1 md:grid-cols-2 gap-3 my-3 text-xs'>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-cyan-500/30'>\n                        <h5 class='text-cyan-300 font-bold mb-1'>Ray Convergence:</h5>\n                        <p class='text-slate-300'>Because $\\angle B + \\angle C < 180^\\circ$, the two rays launched from the endpoints of $BC$ converge at an exact single point $A$.</p>\n                    </div>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-emerald-500/30'>\n                        <h5 class='text-emerald-300 font-bold mb-1'>Included Side Requirement:</h5>\n                        <p class='text-slate-300'>The side $BC$ is the bridge between the two known angle vertices $B$ and $C$.</p>\n                    </div>\n                </div>\n            </div>\n        ",
        "sim_id": "sim-asa-congruence",
        "checkpoints": [
            {
                "id": "cp7_1",
                "question": "In $\\triangle LMN$, which side is included between $\\angle L$ and $\\angle M$?",
                "options": [
                    "$MN$",
                    "$LN$",
                    "$LM$",
                    "All three sides"
                ],
                "correct": 2,
                "explanation": "The side connecting vertices $L$ and $M$ is side $LM$."
            },
            {
                "id": "cp7_2",
                "question": "If $\\angle B = 60^\\circ, \\angle C = 40^\\circ$ and $BC = 8\\text{ cm}$ in $\\triangle ABC$, and $\\angle E = 60^\\circ, \\angle F = 40^\\circ, EF = 8\\text{ cm}$ in $\\triangle DEF$, are they congruent?",
                "options": [
                    "No, because sides $AB$ and $DE$ are unknown",
                    "Yes, by ASA criterion ($\\triangle ABC \\cong \\triangle DEF$)",
                    "Only if they are right triangles",
                    "No, angles must sum to $90^\\circ$"
                ],
                "correct": 1,
                "explanation": "Two angles and their included side match identically, guaranteeing congruence by ASA."
            }
        ]
    },
    {
        "id": "slide-8",
        "slide_num": 8,
        "section": "9.2",
        "title": "AAS Congruence Criterion: The Angle-Sum Consequence",
        "badge": "Criterion IV",
        "narration": "What if the known side is NOT included between the two angles? Do not despair! Because the angles of any triangle always add up to 180 degrees, knowing any two angles immediately hands you the third angle for free!",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>The AAS (Angle-Angle-Side) Criterion</h4>\n                <p class='text-slate-300 text-sm mb-3'>\n                    <strong>Theorem:</strong> If two angles and any non-included side of one triangle are equal to the corresponding parts of another triangle, the triangles are congruent.\n                </p>\n                <div class='p-3 bg-slate-900 border border-amber-500/40 rounded-xl text-center my-3'>\n                    <span class='text-amber-300 font-bold text-base font-mono'>\n                        $$\\angle A = \\angle D, \\quad \\angle B = \\angle E, \\quad BC = EF \\implies \\triangle ABC \\cong \\triangle DEF$$\n                    </span>\n                </div>\n                <div class='p-3 bg-slate-800/80 rounded-xl border border-cyan-500/30 text-xs text-slate-300'>\n                    <strong>Proof by Angle-Sum:</strong><br>\n                    $$\\angle C = 180^\\circ - (\\angle A + \\angle B) = 180^\\circ - (\\angle D + \\angle E) = \\angle F$$\n                    Now we have $\\angle B = \\angle E$, included side $BC = EF$, and $\\angle C = \\angle F$. This reduces immediately to <strong>ASA</strong>!\n                </div>\n            </div>\n        ",
        "sim_id": "sim-aas-congruence",
        "checkpoints": [
            {
                "id": "cp8_1",
                "question": "Why is AAS a valid congruence criterion?",
                "options": [
                    "Because all triangles are equilateral",
                    "Because the Angle Sum Property ($180^\\circ$) automatically determines the 3rd angle, reducing AAS to ASA",
                    "Because side lengths do not matter",
                    "Because triangles have 4 vertices"
                ],
                "correct": 1,
                "explanation": "Knowing two angles fixed the third angle ($180^\\circ - \\angle 1 - \\angle 2$), converting the non-included side into an included side."
            },
            {
                "id": "cp8_2",
                "question": "If $\\angle A = 50^\\circ, \\angle B = 70^\\circ, BC = 6\\text{ cm}$ in $\\triangle ABC$, what is the measure of $\\angle C$?",
                "options": [
                    "$50^\\circ$",
                    "$60^\\circ$",
                    "$70^\\circ$",
                    "$120^\\circ$"
                ],
                "correct": 1,
                "explanation": "$\\angle C = 180^\\circ - (50^\\circ + 70^\\circ) = 180^\\circ - 120^\\circ = 60^\\circ$."
            }
        ]
    },
    {
        "id": "slide-9",
        "slide_num": 9,
        "section": "9.2",
        "title": "RHS Congruence Criterion: Right Angle-Hypotenuse-Side",
        "badge": "Criterion V",
        "narration": "In right-angled triangles, we receive a grand gift: one angle is already locked at exactly 90 degrees! If the hypotenuse and one leg match, Baudhāyana's cord theorem proves the remaining side is identical.",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>The RHS (Right-Hypotenuse-Side) Criterion</h4>\n                <p class='text-slate-300 text-sm mb-3'>\n                    <strong>Theorem:</strong> In two right-angled triangles, if the <strong>hypotenuse</strong> and <strong>one side</strong> of one triangle are equal to the hypotenuse and one side of the other, the triangles are congruent.\n                </p>\n                <div class='p-3 bg-slate-900 border border-amber-500/40 rounded-xl text-center my-3'>\n                    <span class='text-amber-300 font-bold text-base font-mono'>\n                        $$\\angle B = \\angle Q = 90^\\circ, \\quad AC = PR \\text{ (hyp)}, \\quad AB = PQ \\implies \\triangle ABC \\cong \\triangle PQR$$\n                    </span>\n                </div>\n                <div class='p-3 bg-slate-800/80 rounded-xl border border-amber-500/30 text-xs text-slate-300'>\n                    <strong>Baudhāyana / Pythagorean Proof:</strong><br>\n                    $$BC = \\sqrt{AC^2 - AB^2} = \\sqrt{PR^2 - PQ^2} = QR$$\n                    The third sides are automatically equal, proving congruence via <strong>SSS</strong>!\n                </div>\n            </div>\n        ",
        "sim_id": "sim-rhs-congruence",
        "checkpoints": [
            {
                "id": "cp9_1",
                "question": "What does 'RHS' stand for in triangle congruence?",
                "options": [
                    "Right Hand Side",
                    "Right angle, Hypotenuse, Side",
                    "Regular Hexagon Symmetry",
                    "Ratio Height Slope"
                ],
                "correct": 1,
                "explanation": "In geometric congruence, RHS stands for Right-angle ($90^\\circ$), Hypotenuse (longest side opposite $90^\\circ$), and one other Side."
            },
            {
                "id": "cp9_2",
                "question": "In right $\\triangle ABC$ and $\\triangle PQR$, $\\angle B = \\angle Q = 90^\\circ$, hypotenuse $AC = 10\\text{ cm}, PR = 10\\text{ cm}$, and side $AB = 6\\text{ cm}, PQ = 6\\text{ cm}$. Are they congruent?",
                "options": [
                    "No, need all three angles",
                    "Yes, by the RHS criterion",
                    "Only if $BC = 10\\text{ cm}$",
                    "No, right triangles cannot be congruent"
                ],
                "correct": 1,
                "explanation": "Both have $90^\\circ$ angles, equal hypotenuses ($10\\text{ cm}$), and one pair of equal legs ($6\\text{ cm}$), satisfying RHS."
            }
        ]
    },
    {
        "id": "slide-10",
        "slide_num": 10,
        "section": "9.2",
        "title": "Non-Criteria I: Why AAA Guarantees Similarity, NOT Congruence",
        "badge": "Counterexample I",
        "narration": "Many students wonder: if all three angles match, aren't the triangles twins? Not necessarily! Think of zooming a photograph on a screen: the angles do not change, but the size expands! They are similar, but NOT congruent.",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Why AAA is NOT a Congruence Criterion</h4>\n                <p class='text-slate-300 text-sm mb-3'>\n                    Equality of three angles ($AAA$) establishes <strong>similarity</strong> (same shape), but provides <strong>zero information about scale or size</strong>.\n                </p>\n                <div class='grid grid-cols-1 md:grid-cols-2 gap-3 my-3 text-xs'>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-rose-500/30'>\n                        <span class='text-rose-300 font-bold block mb-1'>Equilateral Triangles Example:</span>\n                        <p class='text-slate-300'>An equilateral triangle with side $2\\text{ cm}$ has angles $60^\\circ, 60^\\circ, 60^\\circ$. Another with side $10\\text{ cm}$ ALSO has angles $60^\\circ, 60^\\circ, 60^\\circ$. They cannot superimpose!</p>\n                    </div>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-cyan-500/30'>\n                        <span class='text-cyan-300 font-bold block mb-1'>Magnification / Dilation:</span>\n                        <p class='text-slate-300'>Magnifying a triangle changes its side lengths while leaving every angle completely untouched.</p>\n                    </div>\n                </div>\n            </div>\n        ",
        "sim_id": "sim-aaa-counterexample",
        "checkpoints": [
            {
                "id": "cp10_1",
                "question": "Two triangles have interior angles $30^\\circ, 60^\\circ, 90^\\circ$. Are they necessarily congruent?",
                "options": [
                    "Yes, AAA proves congruence",
                    "No! They have the same shape (similar) but one can be much larger than the other",
                    "Yes, right triangles are always identical",
                    "No, their angles must sum to $360^\\circ$"
                ],
                "correct": 1,
                "explanation": "AAA guarantees similarity (same shape), but without at least one equal side length, size is completely unbounded."
            },
            {
                "id": "cp10_2",
                "question": "What is the minimum condition needed alongside equal angles to prove congruence?",
                "options": [
                    "A fourth angle",
                    "At least one corresponding side length must be equal",
                    "The triangle must be drawn in blue ink",
                    "The perimeter must be odd"
                ],
                "correct": 1,
                "explanation": "If two triangles have equal angles AND at least one corresponding side is equal, they are congruent by ASA or AAS."
            }
        ]
    },
    {
        "id": "slide-11",
        "slide_num": 11,
        "section": "9.2",
        "title": "Non-Criteria II: The SSA Ambiguous Case (Swinging Pendulum)",
        "badge": "Counterexample II",
        "narration": "What about Side-Side-Angle where the angle is not included? This is the famous Ambiguous Case! Like a pendulum swinging from a clock, the opposite side can strike the base in two distinct locations.",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>The Ambiguous Case (SSA / ASS)</h4>\n                <p class='text-slate-300 text-sm mb-3'>\n                    Given two sides and a <strong>non-included angle</strong>, there is no guarantee of a unique triangle.\n                </p>\n                <div class='grid grid-cols-1 md:grid-cols-2 gap-3 my-3 text-xs'>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-amber-500/30'>\n                        <span class='text-amber-300 font-bold block mb-1'>Acute Angle $\\triangle$:</span>\n                        <p class='text-slate-300'>Side $a$ pivots at vertex $A$. It can strike the opposite ray at point $B_1$ (acute $\\triangle$) OR at point $B_2$ (obtuse $\\triangle$). Both satisfy the exact same SSA data!</p>\n                    </div>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-rose-500/30'>\n                        <span class='text-rose-300 font-bold block mb-1'>Conclusion:</span>\n                        <p class='text-slate-300'>Because SSA can produce <strong>two completely different non-congruent triangles</strong>, SSA is NOT a valid congruence criterion.</p>\n                    </div>\n                </div>\n            </div>\n        ",
        "sim_id": "sim-ssa-ambiguous-case",
        "checkpoints": [
            {
                "id": "cp11_1",
                "question": "Why is SSA (Side-Side-Angle) rejected as a congruence criterion?",
                "options": [
                    "Because it has too many letters",
                    "Because it can produce two different, non-congruent triangles (ambiguous case)",
                    "Because angles cannot be measured",
                    "Because it only works on circles"
                ],
                "correct": 1,
                "explanation": "The swinging side can intersect the baseline twice, forming an acute triangle and an obtuse triangle with the exact same SSA measurements."
            },
            {
                "id": "cp11_2",
                "question": "In which special triangle does SSA actually work safely?",
                "options": [
                    "Equilateral triangles only",
                    "Right-angled triangles (where it becomes the RHS criterion!)",
                    "Scalene triangles",
                    "No triangle ever"
                ],
                "correct": 1,
                "explanation": "In right triangles, the $90^\\circ$ angle is opposite the hypotenuse; by Baudhāyana's theorem the third side is unique, yielding RHS."
            }
        ]
    },
    {
        "id": "slide-12",
        "slide_num": 12,
        "section": "9.3",
        "title": "Angles of Isosceles Triangles: Proving Base Angles Equal",
        "badge": "Isosceles Proof",
        "narration": "An isosceles triangle has two equal sides. By dropping a perpendicular from the apex to the base, we split the triangle into two congruent geometric twins! This elegantly proves that base angles opposite equal sides are equal.",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Theorem: Base Angles of an Isosceles Triangle</h4>\n                <p class='text-slate-300 text-sm mb-3'>\n                    <strong>Statement:</strong> In an isosceles triangle, the angles opposite to the equal sides are equal.\n                </p>\n                <div class='p-3 bg-slate-900 border border-amber-500/40 rounded-xl text-center my-3'>\n                    <span class='text-amber-300 font-bold text-base font-mono'>\n                        $$AB = AC \\implies \\angle B = \\angle C$$\n                    </span>\n                </div>\n                <div class='p-3 bg-slate-800/80 rounded-xl border border-emerald-500/30 text-xs text-slate-300 space-y-1.5'>\n                    <p><strong>Proof via Congruence:</strong></p>\n                    <p>1. In $\\triangle ABC$, let $AB = AC$. Draw altitude $AD \\perp BC$.</p>\n                    <p>2. In right $\\triangle ABD$ and right $\\triangle ACD$:</p>\n                    <p>&nbsp;&nbsp;&bull; $\\angle ADB = \\angle ADC = 90^\\circ$ (Right angle)</p>\n                    <p>&nbsp;&nbsp;&bull; Hypotenuse $AB = AC$ (Given equal sides)</p>\n                    <p>&nbsp;&nbsp;&bull; Side $AD = AD$ (Common shared side)</p>\n                    <p>3. $\\therefore \\triangle ABD \\cong \\triangle ACD$ by the <strong>RHS criterion</strong>!</p>\n                    <p>4. By CPCTC, $\\angle B = \\angle C$. <span class='text-emerald-400 font-bold'>Q.E.D.</span></p>\n                </div>\n            </div>\n        ",
        "sim_id": "sim-isosceles-base-angles",
        "checkpoints": [
            {
                "id": "cp12_1",
                "question": "In $\\triangle ABC$, side $AB = AC$ and apex $\\angle A = 40^\\circ$. What is the measure of base angle $\\angle B$?",
                "options": [
                    "$40^\\circ$",
                    "$70^\\circ$",
                    "$80^\\circ$",
                    "$140^\\circ$"
                ],
                "correct": 1,
                "explanation": "Sum of angles $= 180^\\circ$. The two base angles sum to $180^\\circ - 40^\\circ = 140^\\circ$. Since $\\angle B = \\angle C$, each is $140^\\circ / 2 = 70^\\circ$."
            },
            {
                "id": "cp12_2",
                "question": "What auxiliary line was constructed to split the isosceles triangle into congruent twins?",
                "options": [
                    "A line parallel to $AB$",
                    "An altitude $AD \\perp BC$ from apex $A$",
                    "A circle around vertex $C$",
                    "A tangent line"
                ],
                "correct": 1,
                "explanation": "Drawing altitude $AD \\perp BC$ creates two right triangles sharing side $AD$, allowing RHS congruence."
            }
        ]
    },
    {
        "id": "slide-13",
        "slide_num": 13,
        "section": "9.3",
        "title": "Equilateral Triangles: The Universal 60-Degree Harmony",
        "badge": "Equilateral Harmony",
        "narration": "An equilateral triangle has all three sides equal. Applying our isosceles theorem twice reveals that all three angles must be identical! Since the sum of angles is 180 degrees, each angle is locked at 60 degrees.",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Theorem: Equiangular Property of Equilateral Triangles</h4>\n                <p class='text-slate-300 text-sm mb-3'>\n                    <strong>Statement:</strong> All three interior angles of an equilateral triangle are equal, and each measures exactly $60^\\circ$.\n                </p>\n                <div class='p-3 bg-slate-900 border border-amber-500/40 rounded-xl text-center my-3'>\n                    <span class='text-amber-300 font-bold text-base font-mono'>\n                        $$AB = BC = CA \\implies \\angle A = \\angle B = \\angle C = \\frac{180^\\circ}{3} = 60^\\circ$$\n                    </span>\n                </div>\n                <div class='p-3 bg-slate-800/80 rounded-xl border border-cyan-500/30 text-xs text-slate-300 space-y-1.5'>\n                    <p><strong>Step-by-Step Deduction:</strong></p>\n                    <p>• Since $AB = AC$, by the isosceles theorem, $\\angle B = \\angle C$.</p>\n                    <p>• Since $AB = BC$, by the isosceles theorem, $\\angle A = \\angle C$.</p>\n                    <p>• Therefore, $\\angle A = \\angle B = \\angle C$.</p>\n                    <p>• Since $\\angle A + \\angle B + \\angle C = 180^\\circ \\implies 3\\angle A = 180^\\circ \\implies \\angle A = 60^\\circ$.</p>\n                </div>\n            </div>\n        ",
        "sim_id": "sim-equilateral-60deg",
        "checkpoints": [
            {
                "id": "cp13_1",
                "question": "Can an equilateral triangle ever have an obtuse angle ($> 90^\\circ$)?",
                "options": [
                    "Yes, if it is very large",
                    "No! Every equilateral triangle must have exactly three $60^\\circ$ acute angles",
                    "Yes, in spherical geometry only",
                    "Only if drawn upside down"
                ],
                "correct": 1,
                "explanation": "Because all three angles are equal and sum to $180^\\circ$, each angle is invariant at exactly $60^\\circ$."
            },
            {
                "id": "cp13_2",
                "question": "Every equilateral triangle is also:",
                "options": [
                    "A scalene triangle",
                    "An isosceles triangle (having at least two equal sides)",
                    "A right triangle",
                    "An obtuse triangle"
                ],
                "correct": 1,
                "explanation": "An equilateral triangle has all three sides equal, which satisfies the condition of having at least two sides equal (isosceles)."
            }
        ]
    },
    {
        "id": "slide-14",
        "slide_num": 14,
        "section": "9.4",
        "title": "Master Criteria Decision Tree: SSS, SAS, ASA, AAS & RHS",
        "badge": "Decision Matrix",
        "narration": "When presented with two mystery triangles, how do you instantly identify which criterion to apply? Follow our Master Decision Tree! Check for right angles, count given sides, and examine angle inclusion.",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>The 5 Valid Criteria vs 2 False Criteria</h4>\n                <div class='overflow-x-auto my-3'>\n                    <table class='w-full text-xs text-left border-collapse'>\n                        <thead>\n                            <tr class='border-b border-slate-700 bg-slate-800/80 text-amber-300'>\n                                <th class='p-2 font-bold'>Criterion</th>\n                                <th class='p-2 font-bold'>Given Elements</th>\n                                <th class='p-2 font-bold'>Critical Requirement</th>\n                                <th class='p-2 font-bold'>Validity</th>\n                            </tr>\n                        </thead>\n                        <tbody class='divide-y divide-slate-800 text-slate-300'>\n                            <tr><td class='p-2 font-mono text-cyan-300 font-bold'>SSS</td><td class='p-2'>3 Sides</td><td class='p-2'>All 3 pairs equal</td><td class='p-2 text-emerald-400 font-bold'>&check; VALID</td></tr>\n                            <tr><td class='p-2 font-mono text-cyan-300 font-bold'>SAS</td><td class='p-2'>2 Sides, 1 Angle</td><td class='p-2'>Angle MUST be included</td><td class='p-2 text-emerald-400 font-bold'>&check; VALID</td></tr>\n                            <tr><td class='p-2 font-mono text-cyan-300 font-bold'>ASA</td><td class='p-2'>2 Angles, 1 Side</td><td class='p-2'>Side MUST be included</td><td class='p-2 text-emerald-400 font-bold'>&check; VALID</td></tr>\n                            <tr><td class='p-2 font-mono text-cyan-300 font-bold'>AAS</td><td class='p-2'>2 Angles, 1 Side</td><td class='p-2'>Side is non-included</td><td class='p-2 text-emerald-400 font-bold'>&check; VALID</td></tr>\n                            <tr><td class='p-2 font-mono text-cyan-300 font-bold'>RHS</td><td class='p-2'>Right $\\triangle$, Hyp, Leg</td><td class='p-2'>One angle $90^\\circ$ + hypotenuse</td><td class='p-2 text-emerald-400 font-bold'>&check; VALID</td></tr>\n                            <tr class='bg-rose-950/20'><td class='p-2 font-mono text-rose-400 font-bold'>AAA</td><td class='p-2'>3 Angles</td><td class='p-2'>No size information</td><td class='p-2 text-rose-400 font-bold'>&cross; INVALID (Similar only)</td></tr>\n                            <tr class='bg-rose-950/20'><td class='p-2 font-mono text-rose-400 font-bold'>SSA</td><td class='p-2'>2 Sides, Non-inc Angle</td><td class='p-2'>Ambiguous pendulum case</td><td class='p-2 text-rose-400 font-bold'>&cross; INVALID (2 Triangles)</td></tr>\n                        </tbody>\n                    </table>\n                </div>\n            </div>\n        ",
        "sim_id": "sim-congruence-criteria-sorter",
        "checkpoints": [
            {
                "id": "cp14_1",
                "question": "Which of the following is NOT a valid congruence criterion for triangles?",
                "options": [
                    "SSS",
                    "RHS",
                    "AAA",
                    "SAS"
                ],
                "correct": 2,
                "explanation": "AAA guarantees identical shape (similarity), but does not guarantee identical size."
            },
            {
                "id": "cp14_2",
                "question": "You are given a right triangle with hypotenuse and one leg matching another right triangle. Which criterion is used?",
                "options": [
                    "SSS",
                    "RHS",
                    "AAA",
                    "SSA"
                ],
                "correct": 1,
                "explanation": "Right angle + Hypotenuse + Side is precisely the RHS congruence criterion."
            }
        ]
    },
    {
        "id": "slide-15",
        "slide_num": 15,
        "section": "9.4",
        "title": "Real-World Congruence: Architecture, Wings & Tessellations",
        "badge": "Heritage & Real World",
        "narration": "Congruent twins are not mere textbook exercises. From the bilateral symmetry of a butterfly's wings to the repeated triangular trusses supporting bridge decks and ancient Indian temple domes, congruence creates structural balance and beauty!",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Where Geometric Twins Live in Our World</h4>\n                <div class='grid grid-cols-1 md:grid-cols-3 gap-3 my-3 text-xs'>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-amber-500/30'>\n                        <h5 class='text-amber-300 font-bold mb-1'>1. Structural Engineering</h5>\n                        <p class='text-slate-300'>Steel bridge trusses use congruent triangles so tension and compression are distributed evenly across identical prefabricated parts.</p>\n                    </div>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-cyan-500/30'>\n                        <h5 class='text-cyan-300 font-bold mb-1'>2. Biological Symmetry</h5>\n                        <p class='text-slate-300'>Butterfly wings, lotus petals, and human facial features exhibit bilateral reflectional congruence along a central axis.</p>\n                    </div>\n                    <div class='p-3 bg-slate-800/80 rounded-xl border border-emerald-500/30'>\n                        <h5 class='text-emerald-300 font-bold mb-1'>3. Temple Mandapas & Tilings</h5>\n                        <p class='text-slate-300'>Indian temple ceiling coffers and Islamic jali screens tile space without gaps using congruent polygons (regular tessellations).</p>\n                    </div>\n                </div>\n            </div>\n        ",
        "sim_id": "sim-real-world-twins",
        "checkpoints": [
            {
                "id": "cp15_1",
                "question": "Why do factory engineers mass-produce machine components in congruent shapes?",
                "options": [
                    "So components look colorful",
                    "Interchangeability: any part can replace another without custom resizing",
                    "Because circles cannot be manufactured",
                    "To increase friction"
                ],
                "correct": 1,
                "explanation": "Mass manufacturing relies on congruence so identical parts fit interchangeably into assemblies."
            },
            {
                "id": "cp15_2",
                "question": "What is a tiling (tessellation) of congruent triangles?",
                "options": [
                    "Covering a plane completely with identical triangles without gaps or overlaps",
                    "Drawing circles on paper",
                    "Measuring the perimeter of a circle",
                    "A 3D cube"
                ],
                "correct": 0,
                "explanation": "Tessellations tile a 2D plane seamlessly using congruent tiles fitted edge-to-edge."
            }
        ]
    },
    {
        "id": "slide-16",
        "slide_num": 16,
        "section": "9.4",
        "title": "Congruence Detective: Deducing Unknowns via CPCTC",
        "badge": "Detective Studio",
        "narration": "Now become a true mathematical detective! Once you establish congruence between two triangles using one of our 5 criteria, CPCTC unlocks all remaining unknown sides and angles with absolute certainty.",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>The 2-Step Detective Strategy</h4>\n                <div class='space-y-2 text-xs'>\n                    <div class='p-2.5 bg-slate-800/80 rounded-lg border border-cyan-500/30'>\n                        <span class='text-cyan-300 font-bold block mb-1'>Step 1: Prove Congruence</span>\n                        <p class='text-slate-300'>Identify 3 matching parts that satisfy one of the 5 criteria (SSS, SAS, ASA, AAS, RHS). State the congruence with strict vertex correspondence.</p>\n                    </div>\n                    <div class='p-2.5 bg-slate-800/80 rounded-lg border border-emerald-500/30'>\n                        <span class='text-emerald-300 font-bold block mb-1'>Step 2: Harvest Unknowns via CPCTC</span>\n                        <p class='text-slate-300'>Equate corresponding parts: if $AB = 2x - 3$ and corresponding $PQ = 15$, set $2x - 3 = 15 \\implies 2x = 18 \\implies x = 9$!</p>\n                    </div>\n                </div>\n            </div>\n        ",
        "sim_id": "sim-congruence-puzzle-lab",
        "checkpoints": [
            {
                "id": "cp16_1",
                "question": "If $\\triangle ABC \\cong \\triangle PQR$ and $AB = 3x - 5, PQ = 16$, what is the value of $x$?",
                "options": [
                    "$x = 5$",
                    "$x = 7$",
                    "$x = 9$",
                    "$x = 11$"
                ],
                "correct": 1,
                "explanation": "By CPCTC, $AB = PQ \\implies 3x - 5 = 16 \\implies 3x = 21 \\implies x = 7$."
            },
            {
                "id": "cp16_2",
                "question": "If $\\triangle DEF \\cong \\triangle KLM$ with $\\angle D = 45^\\circ$ and $\\angle E = 85^\\circ$, what is $\\angle M$?",
                "options": [
                    "$45^\\circ$",
                    "$85^\\circ$",
                    "$50^\\circ$",
                    "$90^\\circ$"
                ],
                "correct": 2,
                "explanation": "In $\\triangle DEF$, $\\angle F = 180^\\circ - (45^\\circ + 85^\\circ) = 50^\\circ$. By CPCTC, $\\angle M = \\angle F = 50^\\circ$."
            }
        ]
    },
    {
        "id": "slide-17",
        "slide_num": 17,
        "section": "Review",
        "title": "Mastery Challenge Part 1: Concepts, Simple Figures & SSS",
        "badge": "Mastery Challenge I",
        "narration": "Magnificent work reaching the examination arena! Test your intellect against 10 rigorous challenges examining congruence definitions, simple figures, and the SSS criterion.",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Examination Arena — Part 1</h4>\n                <p class='text-slate-300 text-sm mb-2'>\n                    Select your answers below and click <strong>Submit Answer</strong>. Click <strong>💡 View Step-by-Step Solution</strong> to see complete geometric proofs.\n                </p>\n            </div>\n        ",
        "sim_id": None,
        "quiz_range": [
            1,
            10
        ]
    },
    {
        "id": "slide-18",
        "slide_num": 18,
        "section": "Review",
        "title": "Mastery Challenge Part 2: SAS, Included Angle & ASA",
        "badge": "Mastery Challenge II",
        "narration": "Onward! These 10 questions challenge your discernment of the included angle in SAS and ray convergence in ASA.",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Examination Arena — Part 2</h4>\n                <p class='text-slate-300 text-sm mb-2'>\n                    Pay strict attention to vertex correspondence and angle placement!\n                </p>\n            </div>\n        ",
        "sim_id": None,
        "quiz_range": [
            11,
            20
        ]
    },
    {
        "id": "slide-19",
        "slide_num": 19,
        "section": "Review",
        "title": "Mastery Challenge Part 3: AAS, RHS & The Counterexamples",
        "badge": "Mastery Challenge III",
        "narration": "Now we examine AAS, RHS right-angle mechanics, and why AAA and SSA fail as congruence criteria!",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Examination Arena — Part 3</h4>\n                <p class='text-slate-300 text-sm mb-2'>\n                    Remember: AAA guarantees identical shape, not identical size!\n                </p>\n            </div>\n        ",
        "sim_id": None,
        "quiz_range": [
            21,
            30
        ]
    },
    {
        "id": "slide-20",
        "slide_num": 20,
        "section": "Review",
        "title": "Mastery Challenge Part 4: Isosceles, Equilateral & CPCTC Puzzles",
        "badge": "Mastery Challenge IV",
        "narration": "The final capstone challenge! Solve base angle deductions, equilateral 60-degree theorems, and algebraic CPCTC problems to complete your mastery of Geometric Twins!",
        "theory": "\n            <div class='theory-box'>\n                <h4 class='text-amber-400 font-bold mb-2 text-lg'>Final Capstone Examination</h4>\n                <p class='text-slate-300 text-sm mb-2'>\n                    Complete the final 10 questions to achieve full certification in Congruence of Triangles!\n                </p>\n            </div>\n        ",
        "sim_id": None,
        "quiz_range": [
            31,
            40
        ]
    }
]

QUIZ_QUESTIONS = [
    {
        "id": 1,
        "question": "Which mathematical symbol designates that two figures are congruent?",
        "options": [
            "=",
            "\\approx",
            "\\cong",
            "\\sim"
        ],
        "correct": 2,
        "explanation": "The symbol for congruence is $\\cong$, which merges $\\sim$ (similar shape) with $=$ (equal size).",
        "solution": "1. Understand the symbols:<br>• $=$ means equal numerical value.<br>• $\\sim$ means similar shape.<br>• $\\cong$ combines both to signify identical shape and identical size.<br>2. Therefore, $\\cong$ is the congruence symbol."
    },
    {
        "id": 2,
        "question": "Two line segments $\\overline{AB}$ and $\\overline{CD}$ are congruent if:",
        "options": [
            "They are parallel",
            "They have equal lengths ($AB = CD$)",
            "They intersect at $90^\\circ$",
            "They lie on the same horizontal line"
        ],
        "correct": 1,
        "explanation": "Congruence of line segments depends solely on length: $\\overline{AB} \\cong \\overline{CD} \\iff AB = CD$.",
        "solution": "1. Superposition of line segments: place point $A$ on $C$.<br>2. If $AB = CD$, then point $B$ will fall exactly on $D$.<br>3. Hence, equality of length guarantees congruence."
    },
    {
        "id": 3,
        "question": "If $\\angle PQR \\cong \\angle XYZ$ and $m\\angle PQR = 74^\\circ$, what is $m\\angle XYZ$?",
        "options": [
            "$16^\\circ$",
            "$74^\\circ$",
            "$106^\\circ$",
            "$148^\\circ$"
        ],
        "correct": 1,
        "explanation": "Congruent angles have identical degree measures.",
        "solution": "1. By definition, $\\angle PQR \\cong \\angle XYZ \\iff m\\angle PQR = m\\angle XYZ$.<br>2. Given $m\\angle PQR = 74^\\circ$, we have $m\\angle XYZ = 74^\\circ$."
    },
    {
        "id": 4,
        "question": "Circle $C_1$ has radius $5\\text{ cm}$ and Circle $C_2$ has radius $5\\text{ cm}$. Are they congruent?",
        "options": [
            "No, circles can never be congruent",
            "Yes, because their radii are equal",
            "Only if their centers are at the origin",
            "Only if they are concentric"
        ],
        "correct": 1,
        "explanation": "Two circles are congruent if and only if their radii are equal.",
        "solution": "1. Area of circle is $\\pi r^2$ and perimeter is $2\\pi r$.<br>2. Since $r_1 = r_2 = 5\\text{ cm}$, both have identical area ($25\\pi\\text{ cm}^2$) and perimeter ($10\\pi\\text{ cm}$).<br>3. Superimposing centers makes the boundaries coincide completely."
    },
    {
        "id": 5,
        "question": "Rectangle $ABCD$ has length $8\\text{ cm}$ and breadth $5\\text{ cm}$. Which rectangle is congruent to it?",
        "options": [
            "Rectangle with sides $8\\text{ cm}$ and $6\\text{ cm}$",
            "Rectangle with sides $5\\text{ cm}$ and $8\\text{ cm}$",
            "Square of side $8\\text{ cm}$",
            "Rectangle with perimeter $26\\text{ cm}$ and sides $10\\text{ cm}, 3\\text{ cm}$"
        ],
        "correct": 1,
        "explanation": "A rectangle with dimensions $5\\text{ cm} \\times 8\\text{ cm}$ is congruent after a $90^\\circ$ rotation.",
        "solution": "1. Congruence allows rigid rotations.<br>2. A rectangle of $5\\text{ cm} \\times 8\\text{ cm}$ rotated by $90^\\circ$ has length $8\\text{ cm}$ and breadth $5\\text{ cm}$.<br>3. It superimposes exactly over $ABCD$."
    },
    {
        "id": 6,
        "question": "If $\\triangle ABC \\cong \\triangle XYZ$, which vertex corresponds to vertex $B$?",
        "options": [
            "Vertex $X$",
            "Vertex $Y$",
            "Vertex $Z$",
            "Cannot be determined"
        ],
        "correct": 1,
        "explanation": "In congruence notation, the second letter of $\\triangle ABC$ corresponds to the second letter of $\\triangle XYZ$, which is $Y$.",
        "solution": "1. Align vertices in order:<br>• 1st: $A \\leftrightarrow X$<br>• 2nd: $B \\leftrightarrow Y$<br>• 3rd: $C \\leftrightarrow Z$<br>2. Therefore, vertex $B$ corresponds to vertex $Y$."
    },
    {
        "id": 7,
        "question": "In $\\triangle ABC$ and $\\triangle DEF$, $AB=4\\text{ cm}, BC=7\\text{ cm}, AC=6\\text{ cm}$, and $DE=4\\text{ cm}, EF=7\\text{ cm}, DF=6\\text{ cm}$. Which criterion proves congruence?",
        "options": [
            "SAS",
            "ASA",
            "SSS",
            "RHS"
        ],
        "correct": 2,
        "explanation": "Three pairs of corresponding sides are equal, satisfying the SSS criterion.",
        "solution": "1. Check matching pairs:<br>• $AB = DE = 4\\text{ cm}$ (Side)<br>• $BC = EF = 7\\text{ cm}$ (Side)<br>• $AC = DF = 6\\text{ cm}$ (Side)<br>2. All 3 sides are equal $\\implies \\triangle ABC \\cong \\triangle DEF$ by SSS."
    },
    {
        "id": 8,
        "question": "If $\\triangle PQR \\cong \\triangle BCA$, which of the following statements is FALSE?",
        "options": [
            "$PQ = BC$",
            "$QR = CA$",
            "$PR = BA$",
            "$PR = BC$"
        ],
        "correct": 3,
        "explanation": "$PR$ corresponds to $BA$, not $BC$. Thus $PR = BC$ is false.",
        "solution": "1. Matching pairs from letter positions:<br>• $PQ \\leftrightarrow BC$<br>• $QR \\leftrightarrow CA$<br>• $PR \\leftrightarrow BA$<br>2. Therefore, statement $PR = BC$ is false."
    },
    {
        "id": 9,
        "question": "Why does a triangular truss bridge not collapse under load compared to a rectangular frame?",
        "options": [
            "Triangles have more steel",
            "The SSS criterion ensures a triangle cannot change shape without changing its side lengths",
            "Gravity pulls less on triangles",
            "Rectangles have too many angles"
        ],
        "correct": 1,
        "explanation": "Triangles are structurally rigid because SSS fixes all angles once the three side lengths are fixed.",
        "solution": "1. A quadrilateral can deform into a parallelogram without altering side lengths.<br>2. A triangle cannot deform without altering at least one side length (SSS rigidity).<br>3. This makes triangles the premier structural unit in engineering."
    },
    {
        "id": 10,
        "question": "If $\\triangle ABC \\cong \\triangle PQR$, and the perimeter of $\\triangle ABC$ is $24\\text{ cm}$, what is the perimeter of $\\triangle PQR$?",
        "options": [
            "$12\\text{ cm}$",
            "$24\\text{ cm}$",
            "$48\\text{ cm}$",
            "Cannot be determined without side lengths"
        ],
        "correct": 1,
        "explanation": "Congruent triangles have identical side lengths, so their perimeters are equal ($24\\text{ cm}$).",
        "solution": "1. $\\text{Perimeter}(\\triangle ABC) = AB + BC + CA = 24\\text{ cm}$.<br>2. By CPCTC, $PQ = AB, QR = BC, RP = CA$.<br>3. $\\text{Perimeter}(\\triangle PQR) = PQ + QR + RP = AB + BC + CA = 24\\text{ cm}$."
    },
    {
        "id": 11,
        "question": "In $\\triangle ABC$, which angle is the included angle between sides $AB$ and $AC$?",
        "options": [
            "$\\angle B$",
            "$\\angle C$",
            "$\\angle A$",
            "Both $\\angle B$ and $\\angle C$"
        ],
        "correct": 2,
        "explanation": "The vertex shared by sides $AB$ and $AC$ is $A$, so the included angle is $\\angle A$.",
        "solution": "1. Sides are $AB$ and $AC$.<br>2. The vertex where both segments meet is $A$.<br>3. Thus, the included angle is $\\angle A$ (or $\\angle BAC$)."
    },
    {
        "id": 12,
        "question": "In $\\triangle DEF$ and $\\triangle PQR$, $DE = PQ = 6\\text{ cm}$, $EF = QR = 8\\text{ cm}$. What additional piece of information is needed to prove congruence by SAS?",
        "options": [
            "$\\angle D = \\angle P$",
            "$\\angle E = \\angle Q$",
            "$\\angle F = \\angle R$",
            "$DF = 10\\text{ cm}$"
        ],
        "correct": 1,
        "explanation": "$\\angle E$ is included between $DE$ and $EF$, and $\\angle Q$ is included between $PQ$ and $QR$.",
        "solution": "1. Sides are $DE$ and $EF$; their included angle is $\\angle E$.<br>2. Sides are $PQ$ and $QR$; their included angle is $\\angle Q$.<br>3. SAS requires the included angles to be equal: $\\angle E = \\angle Q$."
    },
    {
        "id": 13,
        "question": "If in $\\triangle ABC$ and $\\triangle XYZ$, $AB = XY, BC = YZ$ and $\\angle A = \\angle X = 50^\\circ$, can we conclude congruence by SAS?",
        "options": [
            "Yes, because two sides and an angle are equal",
            "No, because $\\angle A$ is not the included angle between $AB$ and $BC$",
            "Yes, by SSS",
            "No, angles must be $90^\\circ$"
        ],
        "correct": 1,
        "explanation": "The included angle between $AB$ and $BC$ is $\\angle B$, not $\\angle A$. This is SSA, not SAS.",
        "solution": "1. For sides $AB$ and $BC$, the included angle is $\\angle B$.<br>2. The given angle is $\\angle A$, which is non-included.<br>3. SAS does not apply."
    },
    {
        "id": 14,
        "question": "In $\\triangle ABC$ and $\\triangle DEF$, $AB = DE = 5\\text{ cm}$, $\\angle B = \\angle E = 45^\\circ$, and $BC = EF = 7\\text{ cm}$. By which criterion are they congruent?",
        "options": [
            "SSS",
            "SAS",
            "ASA",
            "RHS"
        ],
        "correct": 1,
        "explanation": "Two sides and the included angle ($45^\\circ$) match, satisfying SAS.",
        "solution": "1. $AB = DE$ (Side)<br>2. $\\angle B = \\angle E = 45^\\circ$ (Included Angle)<br>3. $BC = EF$ (Side)<br>4. Therefore, $\\triangle ABC \\cong \\triangle DEF$ by SAS."
    },
    {
        "id": 15,
        "question": "In $\\triangle KLM$, which side is the included side between $\\angle K$ and $\\angle M$?",
        "options": [
            "$KL$",
            "$LM$",
            "$KM$",
            "No side is included"
        ],
        "correct": 2,
        "explanation": "The segment directly joining vertex $K$ and vertex $M$ is side $KM$.",
        "solution": "1. The two angles have vertices $K$ and $M$.<br>2. The segment connecting these two vertices is $KM$.<br>3. Hence, $KM$ is the included side."
    },
    {
        "id": 16,
        "question": "In $\\triangle ABC$ and $\\triangle PQR$, $\\angle B = \\angle Q = 60^\\circ$, $BC = QR = 9\\text{ cm}$, and $\\angle C = \\angle R = 50^\\circ$. By which criterion are they congruent?",
        "options": [
            "SAS",
            "ASA",
            "SSS",
            "AAA"
        ],
        "correct": 1,
        "explanation": "Two angles and their included side ($BC = QR$) match, satisfying ASA.",
        "solution": "1. $\\angle B = \\angle Q = 60^\\circ$ (Angle)<br>2. $BC = QR = 9\\text{ cm}$ (Included Side)<br>3. $\\angle C = \\angle R = 50^\\circ$ (Angle)<br>4. Therefore, $\\triangle ABC \\cong \\triangle PQR$ by ASA."
    },
    {
        "id": 17,
        "question": "If $\\triangle ABC \\cong \\triangle PQR$ by ASA, with $\\angle B = 70^\\circ, \\angle C = 40^\\circ, BC = 12\\text{ cm}$, what is the measure of $\\angle P$?",
        "options": [
            "$40^\\circ$",
            "$70^\\circ$",
            "$80^\\circ$",
            "$70^\\circ$"
        ],
        "correct": 1,
        "explanation": "In $\\triangle ABC$, $\\angle A = 180^\\circ - (70^\\circ + 40^\\circ) = 70^\\circ$. By CPCTC, $\\angle P = \\angle A = 70^\\circ$.",
        "solution": "1. Calculate third angle of $\\triangle ABC$:<br>$$\\angle A = 180^\\circ - (\\angle B + \\angle C) = 180^\\circ - 110^\\circ = 70^\\circ$$<br>2. By CPCTC, $\\angle P = \\angle A = 70^\\circ$."
    },
    {
        "id": 18,
        "question": "Two triangles have 2 sides of $6\\text{ cm}$ and $8\\text{ cm}$, and an angle of $30^\\circ$. Can they be non-congruent?",
        "options": [
            "Never, SAS always guarantees congruence",
            "Yes, if the $30^\\circ$ angle is included in one but non-included in the other",
            "No, side lengths force equality",
            "Only if drawn on different days"
        ],
        "correct": 1,
        "explanation": "If the angle is included in one triangle but non-included in the other, they have different configurations and are not congruent.",
        "solution": "1. Triangle 1: $30^\\circ$ is included $\\implies$ unique third side.<br>2. Triangle 2: $30^\\circ$ is opposite the $6\\text{ cm}$ side $\\implies$ ambiguous pendulum case.<br>3. They are not congruent."
    },
    {
        "id": 19,
        "question": "In a parallelogram $ABCD$, diagonal $AC$ splits it into $\\triangle ABC$ and $\\triangle CDA$. Why are they congruent?",
        "options": [
            "By AAA",
            "By SSS or ASA (alternate interior angles and shared side $AC$)",
            "They are not congruent",
            "Only if $ABCD$ is a square"
        ],
        "correct": 1,
        "explanation": "Opposite sides of a parallelogram are equal, and $AC$ is shared, proving congruence by SSS (or ASA via parallel lines).",
        "solution": "1. $AB = CD$ (Opposite sides of parallelogram)<br>2. $BC = DA$ (Opposite sides of parallelogram)<br>3. $AC = CA$ (Common shared side)<br>4. Therefore, $\\triangle ABC \\cong \\triangle CDA$ by SSS."
    },
    {
        "id": 20,
        "question": "If $\\triangle ABC \\cong \\triangle DEF$, which of the following ensures that $AC = DF$?",
        "options": [
            "CPCTC",
            "Pythagoras Theorem",
            "Angle Sum Property",
            "Euler's Formula"
        ],
        "correct": 0,
        "explanation": "$AC$ and $DF$ are corresponding sides of congruent triangles, so CPCTC guarantees their equality.",
        "solution": "1. $\\triangle ABC \\cong \\triangle DEF$.<br>2. Vertices $A, C$ correspond to $D, F$.<br>3. By CPCTC (Corresponding Parts of Congruent Triangles are Congruent), $AC = DF$."
    },
    {
        "id": 21,
        "question": "In $\\triangle ABC$ and $\\triangle DEF$, $\\angle A = \\angle D = 55^\\circ, \\angle B = \\angle E = 65^\\circ$, and non-included side $BC = EF = 8\\text{ cm}$. Are they congruent?",
        "options": [
            "No, ASA requires the included side",
            "Yes, by the AAS criterion",
            "No, need side $AB$",
            "Only if they are right triangles"
        ],
        "correct": 1,
        "explanation": "AAS is a valid criterion: two angles and a non-included side guarantee congruence.",
        "solution": "1. Given: $\\angle A = \\angle D, \\angle B = \\angle E$ and $BC = EF$.<br>2. The third angle is $\\angle C = 180^\\circ - (55^\\circ + 65^\\circ) = 60^\\circ$, and $\\angle F = 60^\\circ$.<br>3. This reduces to ASA with included side $BC = EF$.<br>4. Therefore, congruent by AAS."
    },
    {
        "id": 22,
        "question": "What is the key difference between ASA and AAS?",
        "options": [
            "ASA has 3 angles, AAS has 2 angles",
            "In ASA the side is between the two angles; in AAS the side is not between them",
            "AAS only works on right triangles",
            "ASA is invalid"
        ],
        "correct": 1,
        "explanation": "In ASA, the given side is included between the two angles; in AAS, the side is opposite one of the angles.",
        "solution": "1. ASA: $\\angle - \\text{Side} - \\angle$ (Side is flanked by both angles).<br>2. AAS: $\\angle - \\angle - \\text{Side}$ (Side is non-included).<br>3. Both are mathematically valid criteria."
    },
    {
        "id": 23,
        "question": "In right $\\triangle ABC$ ($\\angle B = 90^\\circ$) and right $\\triangle PQR$ ($\\angle Q = 90^\\circ$), hypotenuse $AC = PR = 13\\text{ cm}$, and leg $AB = PQ = 5\\text{ cm}$. What is the length of $QR$?",
        "options": [
            "$8\\text{ cm}$",
            "$12\\text{ cm}$",
            "$14\\text{ cm}$",
            "$18\\text{ cm}$"
        ],
        "correct": 1,
        "explanation": "By Baudhāyana's theorem, $BC = \\sqrt{13^2 - 5^2} = \\sqrt{144} = 12\\text{ cm}$. By CPCTC, $QR = 12\\text{ cm}$.",
        "solution": "1. By RHS criterion, $\\triangle ABC \\cong \\triangle PQR$.<br>2. Calculate leg $BC$ using Baudhāyana/Pythagoras:<br>$$BC = \\sqrt{AC^2 - AB^2} = \\sqrt{13^2 - 5^2} = \\sqrt{169 - 25} = \\sqrt{144} = 12\\text{ cm}$$<br>3. By CPCTC, $QR = BC = 12\\text{ cm}$."
    },
    {
        "id": 24,
        "question": "Can two right-angled triangles be congruent by the SAS criterion?",
        "options": [
            "No, right triangles can only use RHS",
            "Yes, if the two legs (which include the $90^\\circ$ angle) are equal",
            "Only if the hypotenuse is $10\\text{ cm}$",
            "Right triangles cannot be congruent"
        ],
        "correct": 1,
        "explanation": "Yes! The two legs include the $90^\\circ$ right angle, so matching two legs is an exact application of SAS.",
        "solution": "1. In any right triangle, the two perpendicular legs meet at the $90^\\circ$ angle.<br>2. Therefore, the right angle IS the included angle between the two legs.<br>3. Matching the two legs proves congruence via SAS."
    },
    {
        "id": 25,
        "question": "Why is AAA (Angle-Angle-Angle) NOT a valid congruence criterion?",
        "options": [
            "Angles cannot be equal in different triangles",
            "It guarantees the same shape (similarity), but scale/size is completely unrestricted",
            "Sum of angles is not $180^\\circ$",
            "It only works for right angles"
        ],
        "correct": 1,
        "explanation": "Dilation expands side lengths while preserving all angles, so AAA triangles can have completely different sizes.",
        "solution": "1. Consider an equilateral triangle with sides $1\\text{ cm}, 1\\text{ cm}, 1\\text{ cm}$ (angles $60^\\circ, 60^\\circ, 60^\\circ$).<br>2. Consider another equilateral triangle with sides $5\\text{ cm}, 5\\text{ cm}, 5\\text{ cm}$ (angles $60^\\circ, 60^\\circ, 60^\\circ$).<br>3. All 3 angles match, yet one has area 25 times larger!<br>4. Thus AAA does not prove congruence."
    },
    {
        "id": 26,
        "question": "What is the 'ambiguous case' in triangle construction?",
        "options": [
            "When all angles are obtuse",
            "SSA: two sides and a non-included acute angle, which can produce two different triangles",
            "SSS with equal sides",
            "A triangle with zero area"
        ],
        "correct": 1,
        "explanation": "SSA is called ambiguous because the swinging opposite side can strike the base in two distinct locations.",
        "solution": "1. Given side $b$, base ray, and non-included side $a$.<br>2. If $a$ is longer than the perpendicular height but shorter than $b$, an arc centered at apex strikes the base twice.<br>3. This produces two non-congruent triangles: one acute and one obtuse."
    },
    {
        "id": 27,
        "question": "In $\\triangle ABC$ and $\\triangle PQR$, $AB = PQ, BC = QR$, and $\\angle C = \\angle R = 40^\\circ$. Are they guaranteed to be congruent?",
        "options": [
            "Yes, by SAS",
            "Yes, by SSS",
            "No, because $\\angle C$ is not included between $AB$ and $BC$ (SSA trap)",
            "Yes, by RHS"
        ],
        "correct": 2,
        "explanation": "Sides are $AB$ and $BC$, but the angle given is $\\angle C$ (non-included). This is SSA and not guaranteed.",
        "solution": "1. The sides are $AB$ and $BC$.<br>2. The included angle would be $\\angle B$.<br>3. Given is $\\angle C$, which is non-included (SSA).<br>4. Therefore, congruence is NOT guaranteed."
    },
    {
        "id": 28,
        "question": "Which of the following sets of conditions guarantees congruence of two triangles?",
        "options": [
            "$AAA$",
            "$SSA$",
            "$ASS$",
            "$RHS$"
        ],
        "correct": 3,
        "explanation": "RHS is an official, valid criterion for right-angled triangles. AAA, SSA, and ASS are not valid.",
        "solution": "1. SSS, SAS, ASA, AAS, and RHS are the 5 valid criteria.<br>2. AAA and SSA/ASS are invalid counterexamples.<br>3. Hence, only RHS guarantees congruence."
    },
    {
        "id": 29,
        "question": "In right $\\triangle DEF$, $\\angle D = 90^\\circ$. What is the hypotenuse?",
        "options": [
            "Side $DE$",
            "Side $DF$",
            "Side $EF$",
            "Altitude from $D$"
        ],
        "correct": 2,
        "explanation": "The hypotenuse is always the side opposite the $90^\\circ$ right angle. Opposite vertex $D$ is side $EF$.",
        "solution": "1. The right angle is at vertex $D$.<br>2. The side lying directly opposite vertex $D$ is side $EF$.<br>3. Therefore, $EF$ is the hypotenuse."
    },
    {
        "id": 30,
        "question": "If $\\triangle ABC \\cong \\triangle DEF$ by RHS, with hypotenuse $15\\text{ cm}$ and leg $9\\text{ cm}$, what is the area of $\\triangle DEF$?",
        "options": [
            "$135\\text{ cm}^2$",
            "$54\\text{ cm}^2$",
            "$67.5\\text{ cm}^2$",
            "$108\\text{ cm}^2$"
        ],
        "correct": 1,
        "explanation": "Other leg $= \\sqrt{15^2 - 9^2} = \\sqrt{144} = 12\\text{ cm}$. $\\text{Area} = \\frac{1}{2} \\times 9 \\times 12 = 54\\text{ cm}^2$.",
        "solution": "1. Find second leg using Baudhāyana/Pythagoras:<br>$$b = \\sqrt{15^2 - 9^2} = \\sqrt{225 - 81} = \\sqrt{144} = 12\\text{ cm}$$<br>2. Area of right triangle $= \\frac{1}{2} \\times \\text{base} \\times \\text{height}$:<br>$$\\text{Area} = \\frac{1}{2} \\times 9 \\times 12 = 54\\text{ cm}^2$$<br>3. By CPCTC, $\\triangle DEF$ has identical area $= 54\\text{ cm}^2$."
    },
    {
        "id": 31,
        "question": "In an isosceles triangle $\\triangle ABC$ with $AB = AC$, if $\\angle B = 55^\\circ$, what is $\\angle A$?",
        "options": [
            "$55^\\circ$",
            "$70^\\circ$",
            "$110^\\circ$",
            "$125^\\circ$"
        ],
        "correct": 1,
        "explanation": "Base angles are equal $\\implies \\angle C = 55^\\circ$. $\\angle A = 180^\\circ - (55^\\circ + 55^\\circ) = 70^\\circ$.",
        "solution": "1. In an isosceles triangle, angles opposite equal sides are equal $\\implies \\angle C = \\angle B = 55^\\circ$.<br>2. Angle Sum Property: $\\angle A + \\angle B + \\angle C = 180^\\circ$.<br>3. $\\angle A = 180^\\circ - (55^\\circ + 55^\\circ) = 180^\\circ - 110^\\circ = 70^\\circ$."
    },
    {
        "id": 32,
        "question": "What is the measure of each interior angle in any equilateral triangle?",
        "options": [
            "$45^\\circ$",
            "$60^\\circ$",
            "$90^\\circ$",
            "$120^\\circ$"
        ],
        "correct": 1,
        "explanation": "All 3 sides equal $\\implies$ all 3 angles equal. $180^\\circ / 3 = 60^\\circ$.",
        "solution": "1. All three sides are equal ($a = b = c$).<br>2. By the isosceles theorem, all three interior angles are equal ($\\angle A = \\angle B = \\angle C$).<br>3. $3\\angle A = 180^\\circ \\implies \\angle A = 60^\\circ$."
    },
    {
        "id": 33,
        "question": "In isosceles $\\triangle ABC$, $AB = AC$. The altitude $AD$ is drawn to $BC$. What does $AD$ do to the base $BC$?",
        "options": [
            "It triples $BC$",
            "It bisects $BC$ ($BD = DC$)",
            "It has no relationship to $BC$",
            "It makes $BC = AD$"
        ],
        "correct": 1,
        "explanation": "Because $\\triangle ABD \\cong \\triangle ACD$ by RHS, CPCTC proves $BD = DC$, so $AD$ bisects the base.",
        "solution": "1. $\\triangle ABD \\cong \\triangle ACD$ by RHS criterion.<br>2. By CPCTC, corresponding sides $BD$ and $DC$ must be equal.<br>3. Therefore, altitude $AD$ also serves as the median, bisecting $BC$."
    },
    {
        "id": 34,
        "question": "If $\\triangle ABC \\cong \\triangle PQR$, with $AB = 2x + 4$ and $PQ = 20\\text{ cm}$, what is the value of $x$?",
        "options": [
            "$x = 6$",
            "$x = 8$",
            "$x = 10$",
            "$x = 12$"
        ],
        "correct": 1,
        "explanation": "By CPCTC, $AB = PQ \\implies 2x + 4 = 20 \\implies 2x = 16 \\implies x = 8$.",
        "solution": "1. Vertices $A, B$ correspond to $P, Q$.<br>2. By CPCTC, $AB = PQ$.<br>3. Set up the equation: $2x + 4 = 20$.<br>4. $2x = 16 \\implies x = 8$."
    },
    {
        "id": 35,
        "question": "If $\\triangle ABC \\cong \\triangle DEF$, and $\\angle A = 3y + 10^\\circ$, $\\angle D = 70^\\circ$, what is the value of $y$?",
        "options": [
            "$y = 15$",
            "$y = 20$",
            "$y = 25$",
            "$y = 30$"
        ],
        "correct": 1,
        "explanation": "By CPCTC, $\\angle A = \\angle D \\implies 3y + 10 = 70 \\implies 3y = 60 \\implies y = 20$.",
        "solution": "1. Corresponding angles are equal by CPCTC: $\\angle A = \\angle D$.<br>2. $3y + 10 = 70$.<br>3. $3y = 60 \\implies y = 20$."
    },
    {
        "id": 36,
        "question": "Can an isosceles triangle also be an obtuse triangle?",
        "options": [
            "No, isosceles triangles must have all acute angles",
            "Yes, having an obtuse apex angle (e.g., $120^\\circ$) with two equal acute base angles ($30^\\circ, 30^\\circ$)",
            "Only if it has 4 sides",
            "No, obtuse triangles must be scalene"
        ],
        "correct": 1,
        "explanation": "Yes, an apex angle can be obtuse (e.g. $120^\\circ$), leaving $30^\\circ$ for each of the two equal base angles.",
        "solution": "1. Example: Apex $\\angle A = 120^\\circ$ (obtuse).<br>2. Base angles: $\\angle B = \\angle C = (180^\\circ - 120^\\circ)/2 = 30^\\circ$.<br>3. Sides $AB = AC$. This is an obtuse isosceles triangle."
    },
    {
        "id": 37,
        "question": "In $\\triangle ABC$, the bisector of $\\angle A$ is perpendicular to $BC$. What kind of triangle is $\\triangle ABC$?",
        "options": [
            "Scalene",
            "Isosceles ($AB = AC$)",
            "Right-angled only",
            "It cannot exist"
        ],
        "correct": 1,
        "explanation": "Let $AD$ be the bisector and altitude. $\\triangle ABD \\cong \\triangle ACD$ by ASA $\\implies AB = AC$, so it is isosceles.",
        "solution": "1. In $\\triangle ABD$ and $\\triangle ACD$:<br>• $\\angle BAD = \\angle CAD$ (Given $AD$ bisects $\\angle A$)<br>• $AD = AD$ (Common side)<br>• $\\angle ADB = \\angle ADC = 90^\\circ$ (Given $AD \\perp BC$)<br>2. $\\triangle ABD \\cong \\triangle ACD$ by ASA.<br>3. By CPCTC, $AB = AC$, proving the triangle is isosceles."
    },
    {
        "id": 38,
        "question": "A diagonal of a square divides it into two triangles. These triangles are:",
        "options": [
            "Congruent isosceles right triangles",
            "Non-congruent scalene triangles",
            "Equilateral triangles",
            "Obtuse triangles"
        ],
        "correct": 0,
        "explanation": "All 4 sides of a square are equal and each angle is $90^\\circ$. The diagonal forms two congruent isosceles right triangles ($45^\\circ - 45^\\circ - 90^\\circ$).",
        "solution": "1. In square $ABCD$, $AB = BC = CD = DA$, and all angles $= 90^\\circ$.<br>2. Diagonal $AC$ creates $\\triangle ABC$ and $\\triangle CDA$.<br>3. Both have legs of side length $s$ and hypotenuse $s\\sqrt{2}$.<br>4. Therefore, they are congruent isosceles right triangles."
    },
    {
        "id": 39,
        "question": "In $\\triangle PQR$, $PQ = PR$. A point $S$ on $QR$ is such that $PS \\perp QR$. If $QR = 14\\text{ cm}$, what is the length of $QS$?",
        "options": [
            "$5\\text{ cm}$",
            "$7\\text{ cm}$",
            "$10\\text{ cm}$",
            "$14\\text{ cm}$"
        ],
        "correct": 1,
        "explanation": "Altitude to base of isosceles triangle bisects base $\\implies QS = QR / 2 = 14 / 2 = 7\\text{ cm}$.",
        "solution": "1. $\\triangle PSQ \\cong \\triangle PSR$ by RHS criterion.<br>2. By CPCTC, $QS = SR$.<br>3. Since $QS + SR = QR = 14\\text{ cm}$, we have $QS = 14 / 2 = 7\\text{ cm}$."
    },
    {
        "id": 40,
        "question": "Two triangles are congruent. Which of the following properties do they share?",
        "options": [
            "Identical perimeter only",
            "Identical area only",
            "Identical shape, size, perimeter, and area",
            "Different angle measures"
        ],
        "correct": 2,
        "explanation": "Congruence implies complete geometric identity: identical angles, sides, perimeter, and area.",
        "solution": "1. Congruence means one triangle can superimpose exactly over the other.<br>2. All corresponding sides are equal $\\implies$ equal perimeter.<br>3. All corresponding angles are equal $\\implies$ same shape.<br>4. Base and height match $\\implies$ equal area.<br>5. Therefore, they share identical shape, size, perimeter, and area."
    }
]
