#!/usr/bin/env python3
# -*- coding: utf-8 -*-

slides_part2 = [
    {
        "id": 9,
        "title": "Symbols of Elements",
        "subtitle": "Section 8.4: Dalton's Pictorials, Berzelius & IUPAC Rules",
        "speech": (
            "As chemists discovered dozens of elements in the nineteenth century, writing out full names in every "
            "equation became exhausting! In 1803, John Dalton drew small pictorial circles—like a circle with a dot "
            "for hydrogen or a shaded circle for carbon—which were charming but awkward to print! Then in 1813, "
            "Swedish chemist Jöns Jacob Berzelius proposed a brilliant alphabetic system using one or two letters "
            "from each element's name. Today, IUPAC sets the universal rules shown in Table 8.2! Rule one: the "
            "first letter of every chemical symbol MUST be uppercase, and if there is a second letter, it MUST be "
            "lowercase! Never write CO when you mean cobalt—CO is toxic carbon monoxide gas, whereas Co with a "
            "lowercase o is the metal cobalt! Similarly, aluminium is Al, not AL. Rule two: several symbols come "
            "from classical Latin or non-English names rather than modern English! Iron is Fe from ferrum; Gold is "
            "Au from aurum; Sodium is Na from natrium; Potassium is K from kalium; and Tungsten is W from wolfram! "
            "Learning these exact IUPAC symbols lets scientists across every country read chemical equations instantly, "
            "without any confusion between elements and compounds across textbooks and laboratories worldwide!"
        ),
        "checkpoints": [
            {
                "question": "Why is it critically important to write Cobalt as 'Co' rather than 'CO' under IUPAC rules?",
                "options": [
                    "CO means copper",
                    "'Co' is the element Cobalt, whereas 'CO' represents the compound Carbon Monoxide",
                    "IUPAC forbids two-letter symbols",
                    "Uppercase O is reserved for oxygen only in metals"
                ],
                "answer": 1,
                "hint": "Check the capitalization rule: first letter uppercase, second letter lowercase.",
                "explanation": "In IUPAC notation, Co is cobalt while CO (two capitals) means one carbon atom bonded to one oxygen atom."
            },
            {
                "question": "Which pairing of element and non-English symbol origin is completely accurate?",
                "options": [
                    "Iron → Ir; Gold → Gd; Sodium → So",
                    "Iron → Fe (ferrum); Gold → Au (aurum); Sodium → Na (natrium); Tungsten → W (wolfram)",
                    "Sodium → S; Potassium → P; Gold → Ag",
                    "Tungsten → Tu; Iron → Fe; Potassium → Po"
                ],
                "answer": 1,
                "hint": "Recall Berzelius's Latin/European name abbreviations in Table 8.2.",
                "explanation": "Fe (ferrum), Au (aurum), Na (natrium), and W (wolfram) are standard IUPAC symbols."
            }
        ]
    },
    {
        "id": 10,
        "title": "Atomic, Mass Numbers",
        "subtitle": "Sections 8.5 & 8.6: Identity (Z), Nucleons (A) & Nuclide Notation",
        "speech": (
            "What makes a carbon atom carbon, and an oxygen atom oxygen? The answer lies in two foundational numbers: "
            "Atomic Number Z and Mass Number A! In Section 8.5, Atomic Number Z is defined as the total number of "
            "protons present in an atom's nucleus. Z is like an element's unchangeable fingerprint—every single "
            "carbon atom has six protons, so Z equals six; change Z to seven and you no longer have carbon, you "
            "have nitrogen! Because a neutral atom has zero net charge, Z equals the number of protons AND equals "
            "the number of electrons. Now turn to Section 8.6: since electrons have negligible mass, almost all of "
            "an atom's mass sits in the nucleus, inside its protons and neutrons—collectively called nucleons! "
            "Mass Number A equals the total number of nucleons: A equals Z plus n, the number of protons plus "
            "neutrons! We write any atom in standard nuclide notation with A as the top-left superscript and Z as "
            "the bottom-left subscript, such as Carbon-12 written 12-6-C! Look at Table 8.3: Hydrogen has A equals "
            "1, Helium has A equals 4, and Lithium with 3 protons and 4 neutrons has A equals 7! Subtracting Z from "
            "A always reveals the exact neutron count!"
        ),
        "checkpoints": [
            {
                "question": "Which subatomic count uniquely defines the chemical identity of an element?",
                "options": [
                    "Number of neutrons (n)",
                    "Atomic Number Z (number of protons in the nucleus)",
                    "Mass Number A",
                    "Number of inner K-shell electrons"
                ],
                "answer": 1,
                "hint": "Neutron counts can vary among isotopes, and electrons can be lost or gained in ions.",
                "explanation": "Atomic Number Z (proton count) uniquely identifies every element and determines its neutral electron count."
            },
            {
                "question": "In nuclide notation ²³₁₁Na, how many protons, electrons, and neutrons are present in a neutral sodium atom?",
                "options": [
                    "11 protons, 11 electrons, 23 neutrons",
                    "11 protons, 11 electrons, 12 neutrons",
                    "12 protons, 11 electrons, 11 neutrons",
                    "23 protons, 23 electrons, 11 neutrons"
                ],
                "answer": 1,
                "hint": "Use n = A - Z = 23 - 11.",
                "explanation": "Z = 11 gives 11 protons and 11 electrons; neutrons n = A - Z = 23 - 11 = 12."
            }
        ]
    },
    {
        "id": 11,
        "title": "Electron Distribution",
        "subtitle": "Sections 8.7 & 8.7.1: Bohr–Bury Rules (2n²) & First 18 Elements",
        "speech": (
            "Now that we know how many electrons an atom holds, how are they arranged inside Bohr's K, L, M, and N "
            "shells? In Section 8.7, the Bohr-Bury rules give us three crystal-clear guidelines! Rule one: the "
            "maximum number of electrons any shell can hold is given by the formula two n squared, where n is the "
            "shell number! Plugging in n equals 1 for K gives 2 electrons; n equals 2 for L gives 8 electrons; n "
            "equals 3 for M gives 18 electrons; and n equals 4 for N gives 32 electrons! Rule two is a famous "
            "twist: the outermost shell of an atom can hold a maximum of 8 electrons, even if it is the M shell "
            "whose theoretical cap is 18! Rule three: shells fill stepwise from the inside out—you must fill K "
            "before starting L, and fill L before starting M! Let us build atoms from Hydrogen to Argon in Figure "
            "8.11 and Table 8.4: Carbon with 6 electrons arranges as 2, 4; Oxygen with 8 is 2, 6; Neon with 10 is "
            "2, 8; Sodium with 11 is 2, 8, 1; Chlorine with 17 is 2, 8, 7; and Argon with 18 is 2, 8, 8!"
        ),
        "checkpoints": [
            {
                "question": "According to the Bohr–Bury 2n² rule, what are the maximum electron capacities of the K (n=1), L (n=2), M (n=3), and N (n=4) shells?",
                "options": [
                    "2, 4, 8, 16",
                    "2, 8, 18, 32",
                    "2, 8, 8, 8",
                    "1, 2, 3, 4"
                ],
                "answer": 1,
                "hint": "Compute 2(1²), 2(2²), 2(3²), and 2(4²).",
                "explanation": "2(1)² = 2, 2(2)² = 8, 2(3)² = 18, and 2(4)² = 32."
            },
            {
                "question": "What is the electronic configuration of Potassium (Z = 19) considering the outermost shell limit of 8?",
                "options": [
                    "2, 8, 9",
                    "2, 8, 8, 1",
                    "2, 9, 8",
                    "2, 8, 18"
                ],
                "answer": 1,
                "hint": "The outermost shell cannot hold more than 8 electrons, so the 19th electron enters the N shell.",
                "explanation": "Even though M can hold 18, the outermost shell caps at 8, giving Potassium 2, 8, 8, 1."
            }
        ]
    },
    {
        "id": 12,
        "title": "Combining Capacity: Valency",
        "subtitle": "Section 8.8: Valence Electrons, Octet Rule & Valency Calculation",
        "speech": (
            "Why do Helium, Neon, and Argon refuse to react with almost anything, while Sodium and Chlorine react "
            "vigorously? Section 8.8 unlocks the secret of chemical bonding: Valency! The outermost shell of an atom "
            "is called the valence shell, and the electrons sitting in it are called valence electrons. Noble gases "
            "like Neon (2, 8) and Argon (2, 8, 8) already possess 8 valence electrons—a full, ultra-stable octet—or "
            "a full duplet of 2 in Helium! Other atoms lose, gain, or share electrons to achieve that same stable "
            "octet! Valency is an atom's combining capacity, and calculating it takes two easy rules. First, if an "
            "atom has 1, 2, 3, or 4 valence electrons, its valency equals that exact number of valence electrons! "
            "For example, Sodium (2, 8, 1) has 1 valence electron so its valency is 1; Carbon (2, 4) has 4 valence "
            "electrons so its valency is 4. Second, if an atom has 5, 6, or 7 valence electrons, it is easier to "
            "gain electrons to reach 8, so Valency equals 8 minus the number of valence electrons! Thus Oxygen (2, 6) "
            "has valency 8 minus 6 equals 2, and Fluorine (2, 7) has valency 1!"
        ),
        "checkpoints": [
            {
                "question": "Why are noble gases like Helium (2), Neon (2, 8), and Argon (2, 8, 8) chemically inert with zero valency?",
                "options": [
                    "They have no protons",
                    "They already have completely filled outermost shells (duplet of 2 or octet of 8)",
                    "They have 7 valence electrons",
                    "Their nuclei contain no neutrons"
                ],
                "answer": 1,
                "hint": "Atoms react in order to complete a stable duplet or octet.",
                "explanation": "With a full duplet (He) or octet (Ne, Ar), noble gases have zero tendency to lose, gain, or share electrons."
            },
            {
                "question": "Find the valency of Aluminium (Z = 13: 2, 8, 3) and Sulphur (Z = 16: 2, 8, 6).",
                "options": [
                    "Al = 5; S = 6",
                    "Al = 3; S = 2",
                    "Al = 3; S = 6",
                    "Al = 1; S = 2"
                ],
                "answer": 1,
                "hint": "For 1–4 valence electrons, valency = v; for 5–7 valence electrons, valency = 8 - v.",
                "explanation": "Al has 3 valence electrons → valency 3; S has 6 valence electrons → valency = 8 - 6 = 2."
            }
        ]
    },
    {
        "id": 13,
        "title": "Isotopes & Applications",
        "subtitle": "Section 8.9.1: Hydrogen/Carbon Isotopes & Bridging Science and Society",
        "speech": (
            "Wait—must every atom of the same element have the exact same mass? Not always! In Section 8.9.1, meet "
            "Isotopes: atoms of the SAME element having the same atomic number Z, but DIFFERENT mass numbers A due "
            "to different numbers of neutrons! Hydrogen has three famous isotopes: Protium (1-1-H, zero neutrons), "
            "Deuterium (2-1-H, one neutron), and radioactive Tritium (3-1-H, two neutrons). Similarly, Carbon has "
            "Carbon-12, Carbon-13, and Carbon-14—all with 6 protons, but 6, 7, and 8 neutrons! Because isotopes of "
            "an element have the exact same atomic number and electronic configuration, they share identical chemical "
            "properties, while differing in physical properties like mass and density! Now look at Bridging Science "
            "and Society to see how isotopes save lives and power nations! Uranium-235 serves as nuclear fuel in "
            "power plants generating electricity. Cobalt-60 emits controlled gamma radiation for cancer therapy. "
            "Iodine-131 diagnoses and treats goitre and thyroid disorders. And Carbon-14 lets archaeologists perform "
            "radiocarbon dating to measure the age of ancient fossils and wooden artifacts accurately! Isotopes show "
            "how tiny nuclear differences create extraordinary real-world benefits for human society, spanning "
            "clean power generation, life-saving hospital cancer treatments, and historical archaeology across the entire modern world we live in."
        ),
        "checkpoints": [
            {
                "question": "Why do isotopes of the same element (such as ¹²C, ¹³C, and ¹⁴C) have identical chemical properties?",
                "options": [
                    "They have the same number of neutrons",
                    "They have the same atomic number Z and therefore the same electronic configuration",
                    "They have identical mass numbers",
                    "They have zero protons"
                ],
                "answer": 1,
                "hint": "Chemical reactions depend on valence electrons, not nuclear neutrons.",
                "explanation": "Same Z means identical electron distribution and valency, so chemical behavior is identical."
            },
            {
                "question": "Which isotope application pair from Bridging Science and Society is completely correct?",
                "options": [
                    "Iodine-131 for nuclear fuel; Uranium-235 for goitre",
                    "Uranium-235 (nuclear fuel), Cobalt-60 (cancer therapy), Iodine-131 (thyroid/goitre), Carbon-14 (fossil dating)",
                    "Cobalt-60 for fossil dating; Carbon-14 for cancer therapy",
                    "Protium for cancer therapy; Deuterium for thyroid"
                ],
                "answer": 1,
                "hint": "Match U-235 (power), Co-60 (cancer), I-131 (thyroid), and C-14 (dating).",
                "explanation": "U-235 fuels reactors, Co-60 treats cancer, I-131 treats thyroid disorders, and C-14 dates fossils."
            }
        ]
    },
    {
        "id": 14,
        "title": "Average Mass, Isobars",
        "subtitle": "Sections 8.9.1A & 8.9.2: Fractional Mass (35.5 u), Isobars & Quantum Cloud",
        "speech": (
            "If protons and neutrons each weigh about one unified mass unit, why does Chlorine's atomic mass appear "
            "on the periodic table as a fraction—thirty-five point five u? Section 8.9.1A explains! Natural chlorine "
            "is a mixture of two isotopes: seventy-five percent Chlorine-35 and twenty-five percent Chlorine-37. "
            "Taking the weighted average by natural abundance gives thirty-five times seventy-five over one hundred, "
            "plus thirty-seven times twenty-five over one hundred—which equals twenty-six point two five plus nine "
            "point two five, yielding thirty-five point five u! Next, in Section 8.9.2, compare isotopes with "
            "Isobars! Isobars are atoms of DIFFERENT elements having different atomic numbers Z, yet the SAME mass "
            "number A! For instance, Calcium (Z=20), Potassium (Z=19), and Argon (Z=18) all have a mass number of "
            "forty—meaning they have different numbers of protons and different chemical properties, but the exact "
            "same total count of forty nucleons! Finally, remember that science keeps advancing: while Bohr's "
            "circular orbits explain shells and valency wonderfully, modern quantum mechanics replaces fixed flat "
            "rings with three-dimensional probability regions called electron clouds—giving us our deepest picture "
            "of where electrons are most likely to reside inside an atom, replacing simple flat rings with rich three-dimensional spatial quantum orbitals!"
        ),
        "checkpoints": [
            {
                "question": "Natural chlorine contains 75% ³⁵Cl and 25% ³⁷Cl. Why is its average atomic mass 35.5 u?",
                "options": [
                    "Every chlorine atom contains half a neutron",
                    "(35 × 0.75) + (37 × 0.25) = 26.25 + 9.25 = 35.5 u",
                    "(35 + 37) / 2 = 35.5 u",
                    "Chlorine has 35.5 protons"
                ],
                "answer": 1,
                "hint": "Weight each isotopic mass by its fractional natural abundance.",
                "explanation": "Weighted average = 35(75/100) + 37(25/100) = 26.25 + 9.25 = 35.5 u."
            },
            {
                "question": "What makes ⁴⁰₂₀Ca, ⁴⁰₁₉K, and ⁴⁰₁₈Ar a set of ISOBARS?",
                "options": [
                    "Same atomic number Z, different mass numbers A",
                    "Different atomic numbers Z (different elements), but the same mass number A = 40",
                    "Identical chemical properties",
                    "Same number of electrons"
                ],
                "answer": 1,
                "hint": "Isobars share the same total nucleon count A.",
                "explanation": "Isobars have different Z (20, 19, 18) but identical mass number A = 40."
            }
        ]
    },
    {
        "id": 15,
        "title": "Revise & Beyond",
        "subtitle": "Revise, Reflect, Refine & The Journey Beyond: Thought Experiments & PhET",
        "speech": (
            "Before entering our four silent quizzes, let us sharpen our scientific reasoning with Revise, Reflect, "
            "Refine and The Journey Beyond! First, imagine increasing the thickness of Rutherford's gold foil from "
            "one thousand atoms to ten thousand atoms: what happens? Alpha particles encounter ten times as many "
            "nuclei, so large-angle scattering and rebounds increase noticeably! Second, test a fun thought experiment "
            "from the end-of-chapter problems: suppose electrons suddenly became as heavy as protons while keeping "
            "their minus-one charge. Would an atom's mass number A change? Yes, significantly, because electrons "
            "would now contribute half the mass of light atoms! Third, check charge balance in ions: if a magnesium "
            "atom (Z=12) loses two electrons, it has twelve protons and ten electrons, giving a net charge of plus "
            "two! In The Journey Beyond, you can build an Atomic Prediction Board game to challenge friends on "
            "electronic configurations, explore interactive PhET simulations on Rutherford Scattering and Isotopes "
            "and Atomic Mass, and watch documentaries tracing how invisible particles power stars, reactors, and "
            "life itself! Careful reasoning turns memorized facts into genuine scientific mastery, preparing you to "
            "solve any atomic puzzle with complete confidence and accuracy in your school exams and daily life."
        ),
        "checkpoints": [
            {
                "question": "What would happen in Rutherford's gold foil experiment if a much thicker gold sheet were used?",
                "options": [
                    "Scattering would drop to zero",
                    "Alpha particles would encounter more gold nuclei, increasing deflection and back-scattering chances",
                    "All alpha particles would turn into electrons",
                    "The nucleus would expand to fill the atom"
                ],
                "answer": 1,
                "hint": "More layers of atoms mean more nuclei in the beam's path.",
                "explanation": "Thicker foil increases the probability of alpha particles passing close to gold nuclei and scattering."
            },
            {
                "question": "An ion of element X has 17 protons, 18 neutrons, and 18 electrons. What are its mass number A and net charge?",
                "options": [
                    "A = 35; charge = 0",
                    "A = 35; charge = -1 (Cl⁻ ion)",
                    "A = 36; charge = +1",
                    "A = 17; charge = -1"
                ],
                "answer": 1,
                "hint": "A = protons + neutrons; net charge = protons - electrons.",
                "explanation": "A = 17 + 18 = 35; net charge = 17 - 18 = -1."
            }
        ]
    },
    {
        "id": 16,
        "title": "Chapter Summary",
        "subtitle": "At a Glance: Complete Atomic Structure Map",
        "speech": (
            "Let us wrap up Chapter 8 with our complete At a Glance roadmap! First, atomic ideas evolved from "
            "Acharya Kanada's parmanus and Democritus's atomos to John Dalton's 1808 atomic theory. Second, three "
            "subatomic particles build every atom: J. J. Thomson's negative electron (e-minus, charge minus one), "
            "Ernest Rutherford's positive proton (p-plus, charge plus one), and James Chadwick's neutral neutron "
            "(n-zero, charge zero). Third, atomic models progressed from Thomson's neutral watermelon sphere, to "
            "Rutherford's planetary nuclear model revealed by 1911 gold-foil scattering, to Niels Bohr's 1913 "
            "stationary energy shells K, L, M, N, and finally today's quantum electron cloud. Fourth, Berzelius "
            "and IUPAC symbols use a capital first letter and lowercase second letter, including Latin roots like "
            "Fe, Au, and Na. Fifth, Atomic Number Z counts protons, Mass Number A equals Z plus n, Bohr-Bury's "
            "two n squared rule caps the valence shell at 8, and valency measures combining capacity toward an "
            "octet. Finally, isotopes share Z with different A (giving weighted averages like Chlorine 35.5 u), "
            "while isobars share A with different Z. Keep this complete mental map handy as you step into the "
            "four silent mastery quiz challenges ahead, and test every concept you have learned!"
        ),
        "checkpoints": [
            {
                "question": "Which historical pairing of scientist and atomic discovery is 100% accurate?",
                "options": [
                    "Thomson → neutron; Chadwick → electron; Bohr → gold foil",
                    "Thomson → electron (1897); Rutherford → nucleus (1911); Bohr → stationary orbits (1913); Chadwick → neutron (1932)",
                    "Dalton → planetary orbits; Kanada → X-ray K shell",
                    "Rutherford → plum pudding; Bohr → cathode rays"
                ],
                "answer": 1,
                "hint": "Trace the chronological timeline from 1897 to 1932.",
                "explanation": "Thomson (electron, 1897), Rutherford (nucleus, 1911), Bohr (orbits, 1913), Chadwick (neutron, 1932)."
            },
            {
                "question": "Which pair correctly contrasts Isotopes and Isobars?",
                "options": [
                    "Isotopes: same A, different Z; Isobars: same Z, different A",
                    "Isotopes: same Z, different A; Isobars: same A, different Z",
                    "Both have identical proton and neutron counts",
                    "Isotopes belong to different elements"
                ],
                "answer": 1,
                "hint": "Isotopes = same element (same Z); Isobars = same mass number (same A).",
                "explanation": "Isotopes have identical Z and different A; Isobars have identical A and different Z."
            }
        ]
    }
]
