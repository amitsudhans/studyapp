# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 11: Electricity
Part 3: Slides 17 to 20 Generator (40 Comprehensive Challenge Questions)
Strictly silent (speech = ""). Titles strictly 1-3 words. Zero persona titles or forbidden names.
"""

import json

slides_part3 = [
    {
        "id": 17,
        "title": "Current Potential Review",
        "subtitle": "Current, Charge, Potential Difference, and Circuit Fundamentals",
        "badge": "Review Set 1",
        "speech": "",
        "theory": """
            <div class="space-y-2 text-slate-300 text-xs leading-relaxed">
                <p><strong class="text-amber-400">Section Focus:</strong> Review of electric current ($I = Q/t$), charge quantization ($Q = ne$), potential difference ($V = W/Q$), ammeter series connection, and voltmeter parallel connection.</p>
            </div>
        """,
        "questions": [
            {
                "id": "c11_q1",
                "question": "What is the continuous rate of flow of electric charge through a conductor called?",
                "options": ["Electric current", "Electric potential", "Electrical resistance", "Electric power"],
                "answer": 0,
                "hint": "Expressed mathematically as I = Q / t.",
                "explanation": "Electric current is defined as the amount of electric charge flowing across a cross-section of a conductor per unit time.",
                "steps": [
                    "Step 1: Identify that the rate of flow of charge Q through a conductor in time t is I = Q/t.",
                    "Step 2: In the SI system, 1 Coulomb per second is defined as 1 Ampere.",
                    "Step 3: This physical quantity is called electric current."
                ]
            },
            {
                "id": "c11_q2",
                "question": "How many electrons constitute a net charge of one coulomb (1 C)?",
                "options": ["6.25 × 10¹⁸ electrons", "1.6 × 10⁻¹⁹ electrons", "6.02 × 10²³ electrons", "9.1 × 10⁻³¹ electrons"],
                "answer": 0,
                "hint": "Use n = Q / e where e = 1.6 × 10⁻¹⁹ C.",
                "explanation": "Since Q = n × e, n = 1 / (1.6 × 10⁻¹⁹) = 6.25 × 10¹⁸ electrons.",
                "steps": [
                    "Step 1: Charge on a single electron is e = 1.6 × 10⁻¹⁹ C.",
                    "Step 2: The total number of electrons n in charge Q is n = Q / e.",
                    "Step 3: For Q = 1 C, n = 1 / (1.6 × 10⁻¹⁹) = 6.25 × 10¹⁸ electrons."
                ]
            },
            {
                "id": "c11_q3",
                "question": "A current of 0.75 A is drawn by a filament of an electric bulb for 20 minutes. What total charge flows through the circuit?",
                "options": ["900 C", "15 C", "45 C", "1800 C"],
                "answer": 0,
                "hint": "Convert 20 minutes to seconds: t = 20 × 60 = 1200 s, then apply Q = I × t.",
                "explanation": "Q = I × t = 0.75 A × (20 × 60 s) = 0.75 A × 1200 s = 900 C.",
                "steps": [
                    "Step 1: Convert time duration to SI units: t = 20 minutes = 20 × 60 = 1200 seconds.",
                    "Step 2: Apply the electric current formula: Q = I × t.",
                    "Step 3: Calculate: Q = 0.75 A × 1200 s = 900 Coulombs."
                ]
            },
            {
                "id": "c11_q4",
                "question": "What is the work done in moving a unit positive charge from one point to another in an electric circuit called?",
                "options": ["Electric potential difference", "Electric conductance", "Electromotive current", "Capacitive reactance"],
                "answer": 0,
                "hint": "Formula: V = W / Q.",
                "explanation": "Electric potential difference between two points is defined as the work done per unit charge in moving a charge between them.",
                "steps": [
                    "Step 1: Consider work W performed to move charge Q between two circuit points.",
                    "Step 2: The work done per unit charge is expressed as V = W/Q.",
                    "Step 3: This physical quantity is defined as electric potential difference, measured in volts."
                ]
            },
            {
                "id": "c11_q5",
                "question": "How much work is required to move a charge of 3 C across two points having a potential difference of 15 V?",
                "options": ["45 J", "5 J", "0.2 J", "18 J"],
                "answer": 0,
                "hint": "Apply W = V × Q.",
                "explanation": "Work done W = V × Q = 15 V × 3 C = 45 Joules.",
                "steps": [
                    "Step 1: Identify given parameters: potential difference V = 15 V and charge Q = 3 C.",
                    "Step 2: From the potential difference formula, work done is W = V × Q.",
                    "Step 3: Multiply: W = 15 V × 3 C = 45 Joules."
                ]
            },
            {
                "id": "c11_q6",
                "question": "How are an ammeter and a voltmeter connected in a standard test circuit?",
                "options": [
                    "Ammeter in series, voltmeter in parallel",
                    "Ammeter in parallel, voltmeter in series",
                    "Both connected in series",
                    "Both connected in parallel"
                ],
                "answer": 0,
                "hint": "An ammeter measures through-current; a voltmeter measures across-voltage.",
                "explanation": "An ammeter has low resistance and is connected in series; a voltmeter has high resistance and is connected in parallel.",
                "steps": [
                    "Step 1: Current must pass entirely through the ammeter, requiring a series connection with low resistance.",
                    "Step 2: Potential difference is measured across two nodes, requiring a parallel connection with high resistance.",
                    "Step 3: Therefore, the ammeter is in series and the voltmeter is in parallel."
                ]
            },
            {
                "id": "c11_q7",
                "question": "What device is commonly used to maintain a potential difference across an external circuit?",
                "options": ["Chemical cell or battery", "Ammeter", "Rheostat alone", "Voltmeter"],
                "answer": 0,
                "hint": "Chemical reactions maintain the voltage difference across its terminals.",
                "explanation": "A chemical cell or battery maintains a constant potential difference between its terminals by chemical action.",
                "steps": [
                    "Step 1: Charges require an electric pressure difference to flow through conductors.",
                    "Step 2: Chemical reactions inside a cell continuously generate electromotive potential across its terminals.",
                    "Step 3: Thus, an electric cell or battery maintains the potential difference."
                ]
            },
            {
                "id": "c11_q8",
                "question": "How much energy is given to each coulomb of charge passing through a 6 V battery?",
                "options": ["6 J", "1 J", "36 J", "0.16 J"],
                "answer": 0,
                "hint": "Each coulomb means Q = 1 C. Work done W = V × Q.",
                "explanation": "Work done W = V × Q = 6 V × 1 C = 6 Joules of energy per coulomb.",
                "steps": [
                    "Step 1: Identify that 'each coulomb' corresponds to a charge Q = 1 C.",
                    "Step 2: The battery maintains a potential difference of V = 6 V.",
                    "Step 3: Energy delivered W = V × Q = 6 V × 1 C = 6 Joules."
                ]
            },
            {
                "id": "c11_q9",
                "question": "What is the conventional graphical symbol for an open plug key in an electrical schematic?",
                "options": ["Parentheses with no center dot ()", "Parentheses with center dot (·)", "A zig-zag line", "A circle with letter A"],
                "answer": 0,
                "hint": "A central dot indicates conducting contact (closed key).",
                "explanation": "According to NCERT Table 11.1, an open plug key is symbolized by empty parentheses (), while a closed key contains a center dot (·).",
                "steps": [
                    "Step 1: Standard circuit notation represents a switch via parentheses.",
                    "Step 2: When open, no conduction occurs and the space inside remains blank ().",
                    "Step 3: When closed, a central dot is inserted (·) to denote electrical continuity."
                ]
            },
            {
                "id": "c11_q10",
                "question": "If 1 microampere (1 μA) of current flows in a wire, how many amperes does this represent?",
                "options": ["10⁻⁶ A", "10⁻³ A", "10⁶ A", "10⁻⁹ A"],
                "answer": 0,
                "hint": "Micro denotes the metric prefix for one-millionth (10⁻⁶).",
                "explanation": "1 microampere = 1 μA = 10⁻⁶ A (one-millionth of an ampere).",
                "steps": [
                    "Step 1: Recall the standard metric prefixes: milli = 10⁻³ and micro = 10⁻⁶.",
                    "Step 2: Apply the prefix to amperes: 1 μA = 1 × 10⁻⁶ A.",
                    "Step 3: Therefore, 1 microampere represents 10⁻⁶ amperes."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Resistor Geometry Review",
        "subtitle": "Ohm's Law, V-I Graphs, Geometric Factors, and Resistivity",
        "badge": "Review Set 2",
        "speech": "",
        "theory": """
            <div class="space-y-2 text-slate-300 text-xs leading-relaxed">
                <p><strong class="text-amber-400">Section Focus:</strong> Review of Ohm's law ($V = IR$), linear $V\\text{--}I$ characteristics, geometric resistance dependencies ($R = \\rho l/A$), wire stretching/cutting, and resistivity comparisons.</p>
            </div>
        """,
        "questions": [
            {
                "id": "c11_q11",
                "question": "What mathematical relationship constitutes Ohm's law at constant temperature?",
                "options": ["V = IR", "V = I / R", "V = I²R", "V = R / I"],
                "answer": 0,
                "hint": "Potential difference is directly proportional to current (V ∝ I).",
                "explanation": "Ohm's law states that V ∝ I at constant temperature, giving the equation V = IR.",
                "steps": [
                    "Step 1: Ohm's law establishes direct proportionality between potential difference and current: V ∝ I.",
                    "Step 2: Introducing the constant of proportionality R (resistance) gives V = IR.",
                    "Step 3: Therefore, V = IR is the definitive mathematical formulation."
                ]
            },
            {
                "id": "c11_q12",
                "question": "A piece of wire of resistance R is cut into 5 equal parts. These parts are then connected in parallel. If the equivalent resistance of this combination is R', what is the ratio R/R'?",
                "options": ["25", "1/25", "5", "1/5"],
                "answer": 0,
                "hint": "Each piece has resistance r = R/5. Combining 5 equal resistors in parallel gives R' = r/5 = R/25.",
                "explanation": "Each of the 5 pieces has resistance r = R/5. When connected in parallel, 1/R' = 5 × (1/r) = 5 × (5/R) = 25/R. Thus R' = R/25, giving R/R' = 25 (NCERT Exercise Q1).",
                "steps": [
                    "Step 1: Cutting wire of resistance R into 5 equal lengths gives each part a resistance r = R/5 (since R ∝ l).",
                    "Step 2: Connecting 5 such parts in parallel gives 1/R' = 1/r + 1/r + 1/r + 1/r + 1/r = 5/r = 5 / (R/5) = 25/R.",
                    "Step 3: Taking the reciprocal gives R' = R/25. Thus, the ratio R / R' = 25."
                ]
            },
            {
                "id": "c11_q13",
                "question": "How does the resistance of a cylindrical conductor change if its length is doubled and its cross-sectional area is halved?",
                "options": ["It increases by a factor of 4", "It remains unchanged", "It doubles", "It is halved"],
                "answer": 0,
                "hint": "Apply R = ρ l / A with l' = 2l and A' = A/2.",
                "explanation": "R' = ρ (2l) / (A/2) = 4 × (ρ l / A) = 4R. Resistance quadruples.",
                "steps": [
                    "Step 1: The original resistance is R = ρ l / A.",
                    "Step 2: When length doubles (l' = 2l) and area is halved (A' = A/2), the new resistance is R' = ρ (2l) / (A/2).",
                    "Step 3: Simplifying gives R' = 4 (ρ l / A) = 4R. Thus, resistance increases four-fold."
                ]
            },
            {
                "id": "c11_q14",
                "question": "An electric heater draws 4 A current from a 60 V source. What current will it draw if the potential difference is increased to 120 V?",
                "options": ["8 A", "2 A", "16 A", "4 A"],
                "answer": 0,
                "hint": "First find resistance R = V / I = 60 / 4 = 15 Ω, then find I' = 120 / 15.",
                "explanation": "Resistance R = 60 V / 4 A = 15 Ω. At 120 V, new current I' = 120 V / 15 Ω = 8 A (NCERT Example 11.4).",
                "steps": [
                    "Step 1: Calculate the heater resistance: R = V / I = 60 V / 4 A = 15 Ω.",
                    "Step 2: When potential difference increases to 120 V, apply Ohm's law: I' = V' / R.",
                    "Step 3: Compute: I' = 120 V / 15 Ω = 8 A."
                ]
            },
            {
                "id": "c11_q15",
                "question": "Which of the following materials has the lowest electrical resistivity at 20°C?",
                "options": ["Silver (1.60 × 10⁻⁸ Ω·m)", "Copper (1.62 × 10⁻⁸ Ω·m)", "Nichrome (100 × 10⁻⁶ Ω·m)", "Glass (10¹⁰ to 10¹⁴ Ω·m)"],
                "answer": 0,
                "hint": "Refer to Table 11.2 for the best known electrical conductor.",
                "explanation": "Silver has the lowest resistivity (1.60 × 10⁻⁸ Ω·m) among all known metals at 20°C, making it the best conductor.",
                "steps": [
                    "Step 1: Check NCERT Table 11.2 for conductor resistivity values.",
                    "Step 2: Silver has ρ = 1.60 × 10⁻⁸ Ω·m, copper has 1.62 × 10⁻⁸ Ω·m, nichrome has 100 × 10⁻⁶ Ω·m, and glass is an insulator.",
                    "Step 3: Therefore, silver possesses the lowest electrical resistivity."
                ]
            },
            {
                "id": "c11_q16",
                "question": "A cylindrical copper wire has radius r and length l with resistance R. If stretched to radius r/2 while keeping volume constant, what is its new resistance?",
                "options": ["16 R", "4 R", "2 R", "8 R"],
                "answer": 0,
                "hint": "Volume V = A × l = constant. Halving radius reduces area to A/4, which increases length to 4l. Then R' = ρ (4l)/(A/4).",
                "explanation": "When radius is halved, area becomes A' = A/4. Because volume is conserved, length quadruples (l' = 4l). R' = ρ (4l) / (A/4) = 16 R.",
                "steps": [
                    "Step 1: Volume of wire is V = A × l = π r² l = constant.",
                    "Step 2: When radius becomes r/2, cross-sectional area becomes A' = π(r/2)² = A/4, so length becomes l' = 4l.",
                    "Step 3: New resistance R' = ρ l' / A' = ρ (4l) / (A/4) = 16 (ρ l / A) = 16 R."
                ]
            },
            {
                "id": "c11_q17",
                "question": "Why does the cord of an electric heater not glow while the heating element glows red-hot?",
                "options": [
                    "Cord has very low resistance copper wire, while element has high resistance nichrome",
                    "Cord is insulated with rubber which reflects light",
                    "Current flows through the element but bypasses the cord",
                    "The element contains active chemical combustible gases"
                ],
                "answer": 0,
                "hint": "Joule heating H = I²Rt depends directly on resistance R.",
                "explanation": "The copper connecting cord has very low resistance so heat generated is negligible; the nichrome element has high resistance so H = I²Rt produces high temperature and glowing.",
                "steps": [
                    "Step 1: The cord and the heating element are connected in series, carrying the identical current I.",
                    "Step 2: From Joule's law (H = I²Rt), heat produced is directly proportional to resistance R.",
                    "Step 3: The copper cord has very low resistance (stays cool), while the nichrome coil has high resistance (glows red-hot)."
                ]
            },
            {
                "id": "c11_q18",
                "question": "A 1 m long wire of radius 0.15 mm has a resistance of 26 Ω at 20°C. What is its resistivity?",
                "options": ["1.84 × 10⁻⁶ Ω·m", "1.84 × 10⁻⁸ Ω·m", "2.6 × 10⁻⁵ Ω·m", "5.2 × 10⁻⁶ Ω·m"],
                "answer": 0,
                "hint": "Area A = π r² = 3.14 × (1.5 × 10⁻⁴)². Apply ρ = R × A / l.",
                "explanation": "A = π × (0.15 × 10⁻³)² ≈ 7.07 × 10⁻⁸ m². ρ = R × A / l = 26 × 7.07 × 10⁻⁸ / 1 ≈ 1.84 × 10⁻⁶ Ω·m (NCERT Example 11.5).",
                "steps": [
                    "Step 1: Convert radius to metres: r = 0.15 mm = 1.5 × 10⁻⁴ m. Cross-sectional area A = π r² ≈ 7.069 × 10⁻⁸ m².",
                    "Step 2: Use the resistivity formula: ρ = R × A / l.",
                    "Step 3: Calculate: ρ = 26 Ω × 7.069 × 10⁻⁸ m² / 1 m = 1.84 × 10⁻⁶ Ω·m (manganin)."
                ]
            },
            {
                "id": "c11_q19",
                "question": "How does electrical resistivity vary when a metal is heated to a higher temperature?",
                "options": [
                    "Resistivity of pure metals increases with temperature",
                    "Resistivity drops to zero at high temperature",
                    "Resistivity is completely independent of temperature",
                    "Resistivity alternates periodically between positive and negative"
                ],
                "answer": 0,
                "hint": "Higher temperature increases lattice ion vibrations, scattering electrons more frequently.",
                "explanation": "In pure metals, thermal energy increases lattice ion vibrations, increasing electron collisions and causing electrical resistivity to increase with temperature.",
                "steps": [
                    "Step 1: Heating a metal imparts kinetic energy to the positive metallic crystal ions.",
                    "Step 2: Increased amplitude of ionic vibrations enhances the collision cross-section for drifting electrons.",
                    "Step 3: Consequently, electron mobility decreases and resistivity increases with temperature."
                ]
            },
            {
                "id": "c11_q20",
                "question": "What is the equivalent resistance of a conductor through which a current of 2 A flows under a potential difference of 8 V?",
                "options": ["4 Ω", "16 Ω", "0.25 Ω", "10 Ω"],
                "answer": 0,
                "hint": "Use Ohm's law R = V / I.",
                "explanation": "R = V / I = 8 V / 2 A = 4 Ω.",
                "steps": [
                    "Step 1: Identify given parameters: voltage V = 8 V and current I = 2 A.",
                    "Step 2: Apply Ohm's law: R = V / I.",
                    "Step 3: Calculate: R = 8 V / 2 A = 4 Ω."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Resistor Networks Review",
        "subtitle": "Series, Parallel, and Complex Equivalent Network Analysis",
        "badge": "Review Set 3",
        "speech": "",
        "theory": """
            <div class="space-y-2 text-slate-300 text-xs leading-relaxed">
                <p><strong class="text-amber-400">Section Focus:</strong> Review of series resistor formulas ($R_s = R_1 + R_2 + R_3$), parallel resistor formulas ($1/R_p = 1/R_1 + 1/R_2 + 1/R_3$), branch current division, and complex series-parallel equivalent circuits.</p>
            </div>
        """,
        "questions": [
            {
                "id": "c11_q21",
                "question": "How can three resistors of 2 Ω, 3 Ω, and 6 Ω be connected to give a total equivalent resistance of 4 Ω?",
                "options": [
                    "3 Ω and 6 Ω in parallel, connected in series with 2 Ω",
                    "All three in series",
                    "All three in parallel",
                    "2 Ω and 3 Ω in parallel, in series with 6 Ω"
                ],
                "answer": 0,
                "hint": "Parallel combination of 3 Ω and 6 Ω gives (3×6)/(3+6) = 2 Ω. Then add 2 Ω in series: 2 + 2 = 4 Ω.",
                "explanation": "Connecting 3 Ω and 6 Ω in parallel gives Rp = (3×6)/(3+6) = 2 Ω. Placing this in series with 2 Ω gives R_total = 2 + 2 = 4 Ω (NCERT In-text Q1).",
                "steps": [
                    "Step 1: Test parallel combination of 3 Ω and 6 Ω: 1/Rp = 1/3 + 1/6 = 3/6 = 1/2, so Rp = 2 Ω.",
                    "Step 2: Connect the remaining 2 Ω resistor in series with this parallel pair.",
                    "Step 3: Total equivalent resistance R_total = Rp + 2 Ω = 2 + 2 = 4 Ω."
                ]
            },
            {
                "id": "c11_q22",
                "question": "How can the same three resistors of 2 Ω, 3 Ω, and 6 Ω be connected to give a total equivalent resistance of 1 Ω?",
                "options": [
                    "All three connected in parallel",
                    "All three connected in series",
                    "2 Ω and 6 Ω in series, in parallel with 3 Ω",
                    "3 Ω and 6 Ω in series, in parallel with 2 Ω"
                ],
                "answer": 0,
                "hint": "Calculate 1/Rp = 1/2 + 1/3 + 1/6.",
                "explanation": "1/Rp = 1/2 + 1/3 + 1/6 = 3/6 + 2/6 + 1/6 = 6/6 = 1 Ω⁻¹. Thus Rp = 1 Ω (NCERT In-text Q2).",
                "steps": [
                    "Step 1: Connect all three resistors in parallel across two common junction nodes.",
                    "Step 2: Apply the parallel formula: 1/Rp = 1/2 + 1/3 + 1/6 = (3 + 2 + 1) / 6 = 6/6 = 1 Ω⁻¹.",
                    "Step 3: Taking the reciprocal gives Rp = 1 Ω."
                ]
            },
            {
                "id": "c11_q23",
                "question": "What is the highest equivalent resistance that can be obtained by combining four coils of resistances 4 Ω, 8 Ω, 12 Ω, and 24 Ω?",
                "options": ["48 Ω", "2 Ω", "24 Ω", "96 Ω"],
                "answer": 0,
                "hint": "Highest resistance is always obtained by connecting all resistors in series.",
                "explanation": "The highest resistance is obtained in series: Rs = 4 + 8 + 12 + 24 = 48 Ω (NCERT In-text Q3).",
                "steps": [
                    "Step 1: The maximum possible resistance of any resistor set is achieved in a series configuration.",
                    "Step 2: Sum the individual resistance values: Rs = R1 + R2 + R3 + R4.",
                    "Step 3: Calculate: Rs = 4 + 8 + 12 + 24 = 48 Ω."
                ]
            },
            {
                "id": "c11_q24",
                "question": "What is the lowest equivalent resistance that can be obtained from the same four coils (4 Ω, 8 Ω, 12 Ω, and 24 Ω)?",
                "options": ["2 Ω", "48 Ω", "1 Ω", "4 Ω"],
                "answer": 0,
                "hint": "Lowest resistance is always obtained by connecting all resistors in parallel.",
                "explanation": "1/Rp = 1/4 + 1/8 + 1/12 + 1/24 = (6 + 3 + 2 + 1) / 24 = 12/24 = 1/2. Thus Rp = 2 Ω (NCERT In-text Q4).",
                "steps": [
                    "Step 1: The minimum possible resistance is achieved by connecting all resistors in parallel.",
                    "Step 2: 1/Rp = 1/4 + 1/8 + 1/12 + 1/24 = (6 + 3 + 2 + 1) / 24 = 12/24 = 1/2 Ω⁻¹.",
                    "Step 3: Taking the reciprocal gives Rp = 2 Ω."
                ]
            },
            {
                "id": "c11_q25",
                "question": "In a parallel circuit with resistors R1 = 5 Ω, R2 = 10 Ω, and R3 = 30 Ω connected to a 12 V battery, what is the total circuit current?",
                "options": ["4 A", "0.4 A", "2.4 A", "1.2 A"],
                "answer": 0,
                "hint": "Find branch currents: I1 = 12/5 = 2.4 A, I2 = 12/10 = 1.2 A, I3 = 12/30 = 0.4 A. Sum them.",
                "explanation": "I1 = 2.4 A, I2 = 1.2 A, I3 = 0.4 A. Total current I = 2.4 + 1.2 + 0.4 = 4.0 A (NCERT Example 11.8).",
                "steps": [
                    "Step 1: Voltage across each branch is V = 12 V.",
                    "Step 2: Branch currents are I1 = 12/5 = 2.4 A, I2 = 12/10 = 1.2 A, and I3 = 12/30 = 0.4 A.",
                    "Step 3: Total current I = I1 + I2 + I3 = 2.4 + 1.2 + 0.4 = 4.0 A."
                ]
            },
            {
                "id": "c11_q26",
                "question": "What is the equivalent resistance of the parallel combination of 5 Ω, 10 Ω, and 30 Ω?",
                "options": ["3 Ω", "45 Ω", "15 Ω", "5 Ω"],
                "answer": 0,
                "hint": "1/Rp = 1/5 + 1/10 + 1/30 = (6 + 3 + 1)/30 = 10/30 = 1/3.",
                "explanation": "1/Rp = 1/5 + 1/10 + 1/30 = 10/30 = 1/3 Ω⁻¹. Rp = 3 Ω (NCERT Example 11.8).",
                "steps": [
                    "Step 1: Write the reciprocal parallel formula: 1/Rp = 1/5 + 1/10 + 1/30.",
                    "Step 2: Find common denominator 30: 1/Rp = (6 + 3 + 1) / 30 = 10/30 = 1/3 Ω⁻¹.",
                    "Step 3: Invert to find Rp: Rp = 3 Ω."
                ]
            },
            {
                "id": "c11_q27",
                "question": "Two identical resistors of resistance R each are connected first in series and then in parallel. What is the ratio of series to parallel equivalent resistance (Rs / Rp)?",
                "options": ["4", "1/4", "2", "1/2"],
                "answer": 0,
                "hint": "Rs = 2R, Rp = R/2. Ratio Rs / Rp = (2R) / (R/2) = 4.",
                "explanation": "Rs = R + R = 2R. Rp = (R × R) / (R + R) = R/2. Ratio Rs / Rp = 2R / (R/2) = 4.",
                "steps": [
                    "Step 1: Equivalent resistance in series is Rs = R + R = 2R.",
                    "Step 2: Equivalent resistance in parallel is Rp = R / 2.",
                    "Step 3: Compute the ratio: Rs / Rp = (2R) / (R/2) = 4."
                ]
            },
            {
                "id": "c11_q28",
                "question": "In a series circuit containing an 8 Ω resistor and a 12 Ω resistor powered by a 10 V battery, what is the voltage drop across the 12 Ω resistor?",
                "options": ["6 V", "4 V", "10 V", "2.4 V"],
                "answer": 0,
                "hint": "Total Rs = 8 + 12 = 20 Ω. Current I = 10 / 20 = 0.5 A. Voltage across 12 Ω is V = 0.5 × 12 = 6 V.",
                "explanation": "Rs = 8 + 12 = 20 Ω. Current I = 10 V / 20 Ω = 0.5 A. V₂ = I × R₂ = 0.5 A × 12 Ω = 6 V.",
                "steps": [
                    "Step 1: Total series resistance is Rs = 8 + 12 = 20 Ω.",
                    "Step 2: Circuit current is I = V / Rs = 10 V / 20 Ω = 0.5 A.",
                    "Step 3: Voltage drop across the 12 Ω resistor is V2 = I × R2 = 0.5 A × 12 Ω = 6 V."
                ]
            },
            {
                "id": "c11_q29",
                "question": "How many 176 Ω resistors connected in parallel are required to carry a total current of 5 A on a 220 V line?",
                "options": ["4 resistors", "5 resistors", "2 resistors", "8 resistors"],
                "answer": 0,
                "hint": "Required equivalent resistance Rp = V / I = 220 / 5 = 44 Ω. Since Rp = R / n, n = R / Rp = 176 / 44.",
                "explanation": "Target resistance Rp = 220 V / 5 A = 44 Ω. For n identical resistors in parallel, Rp = 176 / n. Thus n = 176 / 44 = 4 resistors (NCERT Exercise Q10).",
                "steps": [
                    "Step 1: Calculate the required total circuit resistance: Rp = V / I = 220 V / 5 A = 44 Ω.",
                    "Step 2: For n parallel resistors of value R, the equivalent resistance is Rp = R / n.",
                    "Step 3: Solve for n: n = R / Rp = 176 Ω / 44 Ω = 4 resistors."
                ]
            },
            {
                "id": "c11_q30",
                "question": "Why is an ammeter never connected in parallel across a power source?",
                "options": [
                    "Its extremely low resistance would cause a dangerous short circuit and burn out the meter",
                    "It has infinite resistance and would prevent all current flow",
                    "It would reverse the chemical polarity of the battery cells",
                    "Voltmeters and ammeters must always be installed in pairs"
                ],
                "answer": 0,
                "hint": "A low-resistance device placed directly across a voltage source draws enormous current.",
                "explanation": "Because an ammeter has virtually zero internal resistance, connecting it in parallel across a voltage source creates a dead short circuit, resulting in massive current that destroys the instrument.",
                "steps": [
                    "Step 1: Ammeters are engineered with minimal internal resistance (R ≈ 0) to avoid disturbing series circuits.",
                    "Step 2: Placing an ammeter in parallel connects near-zero resistance directly across the battery terminals.",
                    "Step 3: By Ohm's law (I = V/R), a catastrophic surge of current occurs, blowing the meter or circuit."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Power Heating Review",
        "subtitle": "Joule's Law, Bulb Filaments, Fuse Ratings, and Commercial kWh Billing",
        "badge": "Review Set 4",
        "speech": "",
        "theory": """
            <div class="space-y-2 text-slate-300 text-xs leading-relaxed">
                <p><strong class="text-amber-400">Section Focus:</strong> Review of Joule's heating law ($H = I^2 Rt$), tungsten filaments, fuse protection, power ratings ($P = VI = I^2 R = V^2/R$), commercial energy units ($1\\text{ kWh} = 3.6 \\times 10^6\\text{ J}$), and electricity cost calculations.</p>
            </div>
        """,
        "questions": [
            {
                "id": "c11_q31",
                "question": "Which of the following is NOT an expression for electrical power in a circuit?",
                "options": ["IR²", "I²R", "VI", "V²/R"],
                "answer": 0,
                "hint": "Power is VI, I²R, or V²/R. Notice the placement of the square.",
                "explanation": "P = VI = I²R = V²/R. The expression IR² has no physical meaning in electrical power (NCERT Exercise Q2).",
                "steps": [
                    "Step 1: Electric power is defined as P = V × I.",
                    "Step 2: Substituting V = IR gives P = (IR) × I = I²R.",
                    "Step 3: Substituting I = V/R gives P = V × (V/R) = V²/R. The expression IR² is incorrect."
                ]
            },
            {
                "id": "c11_q32",
                "question": "An electric bulb is rated 220 V and 100 W. When operated on 110 V, what power will it consume?",
                "options": ["25 W", "50 W", "75 W", "100 W"],
                "answer": 0,
                "hint": "Resistance R = V² / P = 220² / 100 = 484 Ω. At 110 V, P' = V'² / R = 110² / 484.",
                "explanation": "Bulb resistance R = V² / P = 220² / 100 = 484 Ω. When operated at 110 V: P' = V'² / R = 110² / 484 = 12100 / 484 = 25 W (NCERT Exercise Q3).",
                "steps": [
                    "Step 1: Filament resistance is R = V² / P = (220)² / 100 = 484 Ω.",
                    "Step 2: When supply voltage is halved to V' = 110 V, power consumed is P' = (V')² / R.",
                    "Step 3: Calculate: P' = (110)² / 484 = 12,100 / 484 = 25 W (power drops to one-fourth)."
                ]
            },
            {
                "id": "c11_q33",
                "question": "Two conducting wires of the same material, equal length, and equal diameter are connected first in series and then in parallel across the same potential difference. What is the ratio of heat produced in series to parallel (Hs / Hp)?",
                "options": ["1 : 4", "1 : 2", "2 : 1", "4 : 1"],
                "answer": 0,
                "hint": "At constant V, H = (V²/R) × t. Rs = 2R, Rp = R/2. Hs / Hp = (V²/2R) / (V²/(R/2)) = (1/2) / 2 = 1/4.",
                "explanation": "Since voltage V is constant across both setups, H ∝ 1/R. Hs / Hp = Rp / Rs = (R/2) / (2R) = 1/4 = 1:4 (NCERT Exercise Q4).",
                "steps": [
                    "Step 1: When connected to the same voltage source V, heat produced is H = (V² / R_eq) × t.",
                    "Step 2: Series equivalent is Rs = 2R; parallel equivalent is Rp = R/2.",
                    "Step 3: Ratio Hs / Hp = (V² / Rs) / (V² / Rp) = Rp / Rs = (R/2) / (2R) = 1/4 = 1 : 4."
                ]
            },
            {
                "id": "c11_q34",
                "question": "An electric refrigerator rated 400 W operates 8 hours/day for 30 days. What is the cost of energy at Rs 3.00 per kWh?",
                "options": ["Rs 288.00", "Rs 96.00", "Rs 576.00", "Rs 144.00"],
                "answer": 0,
                "hint": "Energy E = 400 W × 8 h/day × 30 days = 96,000 Wh = 96 kWh. Cost = 96 × 3.00.",
                "explanation": "Total energy = 400 W × 8 h × 30 = 96,000 Wh = 96 kWh. Total cost = 96 kWh × Rs 3.00 = Rs 288.00 (NCERT Example 11.13).",
                "steps": [
                    "Step 1: Total operating hours in 30 days = 8 hours/day × 30 days = 240 hours.",
                    "Step 2: Total electrical energy consumed = 400 W × 240 h = 96,000 Watt-hours = 96 kWh.",
                    "Step 3: Cost = 96 kWh × Rs 3.00/kWh = Rs 288.00."
                ]
            },
            {
                "id": "c11_q35",
                "question": "Which uses more energy: a 250 W TV set in 1 hour, or a 1200 W toaster in 10 minutes?",
                "options": [
                    "The TV set uses more energy (250 Wh vs 200 Wh)",
                    "The toaster uses more energy (1200 Wh vs 250 Wh)",
                    "Both appliances use exactly identical energy",
                    "Neither appliance consumes any electrical energy"
                ],
                "answer": 0,
                "hint": "E(TV) = 250 W × 1 h = 250 Wh. E(toaster) = 1200 W × (10/60) h = 200 Wh.",
                "explanation": "Energy for TV = 250 W × 1 h = 250 Wh. Energy for toaster = 1200 W × (1/6 h) = 200 Wh. The TV set uses more energy (NCERT Exercise Q16).",
                "steps": [
                    "Step 1: Calculate energy used by TV: E₁ = 250 W × 1 hour = 250 Watt-hours (Wh).",
                    "Step 2: Calculate energy used by toaster: E₂ = 1200 W × (10/60) hours = 200 Watt-hours (Wh).",
                    "Step 3: Comparing E₁ = 250 Wh and E₂ = 200 Wh shows that the TV set consumes more energy."
                ]
            },
            {
                "id": "c11_q36",
                "question": "An electric lamp is marked 100 W, 220 V. What is the current drawn by the lamp under rated conditions?",
                "options": ["0.45 A", "2.2 A", "4.5 A", "0.22 A"],
                "answer": 0,
                "hint": "Use I = P / V = 100 / 220.",
                "explanation": "I = P / V = 100 W / 220 V = 5/11 A ≈ 0.45 A.",
                "steps": [
                    "Step 1: Identify rated power P = 100 W and rated voltage V = 220 V.",
                    "Step 2: Apply the power formula: P = V × I, which rearranges to I = P / V.",
                    "Step 3: Calculate: I = 100 W / 220 V = 0.454 A ≈ 0.45 A."
                ]
            },
            {
                "id": "c11_q37",
                "question": "What is the primary physical reason for filling inactive nitrogen and argon gases into incandescent light bulbs?",
                "options": [
                    "To prevent oxidation and evaporation of the hot tungsten filament",
                    "To cause chemical fluorescence emitting blue light",
                    "To conduct electrical current directly across the glass bulb",
                    "To absorb all infrared heat radiation"
                ],
                "answer": 0,
                "hint": "Oxygen at high temperatures would burn the glowing metallic filament instantly.",
                "explanation": "Nitrogen and argon are chemically inert gases that prevent oxidation and thermal evaporation of the tungsten filament, extending its lifespan.",
                "steps": [
                    "Step 1: The tungsten filament operates at temperatures exceeding 2500°C.",
                    "Step 2: In the presence of oxygen, tungsten would oxidize and vaporize rapidly, burning out the bulb.",
                    "Step 3: Inert nitrogen and argon do not react with tungsten and retard evaporation, prolonging filament life."
                ]
            },
            {
                "id": "c11_q38",
                "question": "An electric iron draws 3.82 A current from a 220 V source. What is its power rating?",
                "options": ["840 W", "57.6 W", "360 W", "1200 W"],
                "answer": 0,
                "hint": "Apply P = V × I = 220 × 3.82.",
                "explanation": "P = V × I = 220 V × 3.82 A ≈ 840 W (NCERT Example 11.10).",
                "steps": [
                    "Step 1: Identify potential difference V = 220 V and current I = 3.82 A.",
                    "Step 2: Use the electric power equation: P = V × I.",
                    "Step 3: Calculate: P = 220 V × 3.82 A = 840.4 W ≈ 840 W."
                ]
            },
            {
                "id": "c11_q39",
                "question": "What is the equivalent resistance of an electric iron that produces 100 J of heat per second when connected across a 20 V supply?",
                "options": ["4 Ω", "20 Ω", "5 Ω", "100 Ω"],
                "answer": 0,
                "hint": "Heat per second is power P = 100 W. Use R = V² / P = 20² / 100.",
                "explanation": "P = 100 J/s = 100 W. R = V² / P = 20² / 100 = 400 / 100 = 4 Ω (NCERT Example 11.11).",
                "steps": [
                    "Step 1: 100 Joules of heat per second corresponds to an electrical power P = 100 W.",
                    "Step 2: From the power formula P = V² / R, isolate resistance: R = V² / P.",
                    "Step 3: Calculate: R = (20 V)² / 100 W = 400 / 100 = 4 Ω."
                ]
            },
            {
                "id": "c11_q40",
                "question": "If an appliance of 2 kW power operates for 3 hours daily for 10 days, how many commercial units of electricity are consumed?",
                "options": ["60 units (60 kWh)", "6 units", "180 units", "20 units"],
                "answer": 0,
                "hint": "Energy = Power (kW) × Total Hours = 2 kW × (3 × 10) h = 2 × 30 = 60 kWh.",
                "explanation": "Total hours = 3 h/day × 10 days = 30 h. Total energy = 2 kW × 30 h = 60 kWh = 60 commercial units.",
                "steps": [
                    "Step 1: 1 commercial unit of electricity = 1 kilowatt-hour (1 kWh).",
                    "Step 2: Total operating time = 3 hours/day × 10 days = 30 hours.",
                    "Step 3: Energy consumed = 2 kW × 30 hours = 60 kWh = 60 units."
                ]
            }
        ]
    }
]

with open(".agents/c10s_ch11_part3.json", "w", encoding="utf-8") as f:
    json.dump(slides_part3, f, indent=2)

print(f"Generated {len(slides_part3)} review slides in Part 3.")
total_qs = 0
for s in slides_part3:
    tc = len(s["title"].split())
    qs = len(s["questions"])
    total_qs += qs
    print(f"Slide {s['id']}: '{s['title']}' ({tc} words) | Questions: {qs} | Speech: '{s['speech']}'")
    assert s["speech"] == "", f"Slide {s['id']} must have empty speech"
    assert 1 <= tc <= 3, f"Slide {s['id']} title out of range: {tc}"
    assert qs == 10, f"Slide {s['id']} must have 10 questions"
    for q in s["questions"]:
        assert len(q["options"]) == 4, f"Question {q['id']} must have 4 options"
        assert len(q["steps"]) == 3, f"Question {q['id']} must have 3 steps"
print(f"Total review challenge questions: {total_qs}")
