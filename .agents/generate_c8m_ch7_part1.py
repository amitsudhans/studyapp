#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 7: Proportional Reasoning-1
Slides Data Generator - Part 1 (Slides 1 to 8)
Strictly matches NCERT Class 8 Maths Ch 7 syllabus with 1-3 word headings,
195-215 spoken words per slide, zero fictional characters/personas.
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Image Scaling Similarity",
        "subtitle": "Section 7.1 Observing Similarity in Change: Tiger Photo Resizing (Images A–E) & Aspect Preservation",
        "speech": (
            "Welcome to Class Eight Mathematics Chapter Seven: Proportional Reasoning Part One! Open Section Seven Point One by looking closely at digital photographs on mobile phones and computer screens! Suppose an original crisp tiger wildlife photograph measures width 6 centimeters by height 4 centimeters, and five resized versions labeled Images A through E appear side by side! "
            "Why do some resized tiger pictures look sharp, natural, and perfectly proportioned, whereas others look weirdly stretched like tall giraffes or squashed flat like pancakes? Let us test visual similarity systematically! "
            "Compare doubling BOTH width AND height cleanly right away: 6 × 2 = 12 centimeters wide by 4 × 2 = 8 centimeters tall! Look closely—every tiger stripe, pointed ear, and whisker scales harmoniously because relative shape stays completely identical! Even shrinking BOTH photo dimensions equally by half (3 cm wide by 2 cm tall) keeps the tiger completely recognizable and distortion-free! "
            "Now inspect distorted photo Images! Whenever someone stretches ONLY photo width (say 12 cm wide by 4 cm tall) OR adds mismatched constant amounts across edges, faces warp painfully tall or wide out of natural shape! True visual similarity demands balanced scaling across BOTH dimensions together every single time!"
        ),
        "checkpoints": [
            {
                "question": "An original 6 cm × 4 cm tiger photograph is resized into four options (A–D). Which resized copy maintains exact visual similarity without distortion?",
                "options": [
                    "Image B: 9 cm × 6 cm   (both width and height scaled cleanly by exact factor 1.5!)",
                    "Image A: 12 cm × 4 cm   (width doubled, height unchanged)",
                    "Image C: 8 cm × 6 cm   (+2 cm added to both sides)",
                    "Image D: 6 cm × 8 cm   (height doubled, width unchanged)"
                ],
                "answer": 0,
                "hint": "Check which image keeps width ÷ height equal to original 6 ÷ 4 = 1.5!",
                "explanation": "Multiplying both 6 cm and 4 cm by 1.5 yields 9 cm × 6 cm (9/6 = 6/4), keeping shape identical."
            },
            {
                "question": "What visual distortion occurs if an editor triples the WIDTH of a photograph while leaving its HEIGHT completely unchanged?",
                "options": [
                    "Horizontal elongation / squashed-height distortion (losing original aspect ratio)",
                    "Perfect proportional similarity",
                    "Vertical tall stretching only",
                    "Both dimensions scale identically"
                ],
                "answer": 0,
                "hint": "Width stretches 3× wider while vertical height fails to grow!",
                "explanation": "Changing width without scaling height by the same factor warps circles into ovals and stretches faces horizontally."
            }
        ]
    },
    {
        "id": 2,
        "title": "Multiplicative Additive Change",
        "subtitle": "Section 7.1: Why Scaling by Common Factor Preserves Similarity While Adding Constant Causes Distortion",
        "speech": (
            "Discover the golden mathematical distinction powering all of Section Seven Point One: MULTIPLICATIVE CHANGE versus ADDITIVE CHANGE! Why does multiplying width and height by the exact same factor preserve visual similarity, whereas adding the same constant centimeter amount breaks proportions every single time? "
            "Test right now with crisp numbers! Start with a compact 4 cm wide by 2 cm tall rectangular frame (notice width is TWICE height: 2 to 1)! First apply ADDITIVE change: add +4 cm equally onto BOTH dimensions! New width becomes 4 + 4 = 8 cm, and new height becomes 2 + 4 = 6 cm! Check new shape quickly: 8 is NO LONGER twice 6—the rectangle swelled much closer to a square! Why? Adding 4 to tiny height 2 TRIPLED height, while adding 4 to width 4 only DOUBLED width! "
            "Now apply MULTIPLICATIVE scaling change instead: multiply BOTH width 4 cm and height 2 cm cleanly by common scale factor THREE! New width = 12 cm, new height = 6 cm—checking ratio 12 ÷ 6 = EXACT TWO still unchanged! Remember permanently: visual geometric similarity ALWAYS lives cleanly inside uniform multiplication and division, NEVER inside constant additive or subtractive jumps!"
        ),
        "checkpoints": [
            {
                "question": "Start with a 5 cm × 3 cm rectangle. Which operation preserves EXACT geometric similarity?",
                "options": [
                    "Multiplying (or dividing) BOTH width and height by the SAME positive factor (e.g., ×4 → 20 cm × 12 cm)",
                    "Adding +5 cm to both width and height (→ 10 cm × 8 cm)",
                    "Subtracting −2 cm from both dimensions (→ 3 cm × 1 cm)",
                    "Adding +6 cm to width and +4 cm to height (→ 11 cm × 7 cm)"
                ],
                "answer": 0,
                "hint": "Multiplicative scaling multiplies BOTH dimensions by one shared factor k!",
                "explanation": "Multiplying both 5 and 3 by k scales dimensions proportionally (5k : 3k); adding constants (+5 or −2) distorts ratios."
            },
            {
                "question": "Why does adding +6 cm to BOTH dimensions of a 6 cm × 2 cm rectangle distort its shape?",
                "options": [
                    "Width grows ×2 (6 → 12) while shorter height grows ×4 (2 → 8), breaking the 3:1 aspect ratio into 3:2!",
                    "Because addition always keeps angles unequal",
                    "Because 6 + 6 equals 12",
                    "Because rectangles cannot grow larger than 10 cm"
                ],
                "answer": 0,
                "hint": "Compare proportional growth factors: 12/6 = 2× versus 8/2 = 4×!",
                "explanation": "Equal additive changes produce unequal relative multipliers whenever original dimensions differ."
            }
        ]
    },
    {
        "id": 3,
        "title": "Ratios And Terms",
        "subtitle": "Section 7.2 Ratios: Expressing Comparisons (a : b), First/Second Terms & Factor-Based Proportionality",
        "speech": (
            "Enter Section Seven Point Two: RATIOS! Whenever we compare two quantities multiplicatively—like tiger photo width to height, lemonade sugar to water, or cement to sand—we write a RATIO using a colon: a is to b (written cleanly as a : b)! "
            "Learn exact terminology cleanly right away! The two numbers 'a' and 'b' inside a : b are called the TERMS OF THE RATIO! Remember order matters strictly: first term 'a' compares directly against second term 'b', telling us how many units of the first quantity correspond to every matching block of the second quantity (for example, ratio 3 : 2 means 3 parts of first quantity accompany every 2 parts of second quantity)! Notice reversing 3 : 2 into 2 : 3 flips the comparison upside down completely! "
            "When are two ratios—say a : b and c : d—mathematically PROPORTIONAL? By Factor-Based Proportionality: TWO RATIOS ARE PROPORTIONAL IF BOTH TERMS OF THE FIRST RATIO CAN BE MULTIPLIED (OR DIVIDED) BY THE EXACT SAME NON-ZERO FACTOR 'k' TO PRODUCE THE EXACT CORRESPONDING TERMS OF THE SECOND RATIO! Test 4 : 6 vs 12 : 18: multiply both 4 and 6 by k = 3 cleanly → strictly proportional!"
        ),
        "checkpoints": [
            {
                "question": "Identify BOTH terms in the ratio 5 : 8, and test which ratio is factor-proportional to 5 : 8:",
                "options": [
                    "First term = 5, second term = 8;   proportional match is 15 : 24 (both terms multiplied by k = 3!)",
                    "First term = 8, second term = 5;   match 15 : 24",
                    "Terms 5 and 8;   match 8 : 5",
                    "Terms 5 and 8;   match 10 : 13 (+5 added to both!)"
                ],
                "answer": 0,
                "hint": "Order matters (first term 5, second 8), and proportionality requires multiplying BOTH terms by one identical factor!",
                "explanation": "Multiplying both 5 and 8 by k = 3 produces 15 : 24 proportionally (adding +5 breaks it)."
            },
            {
                "question": "If ratio 24 : 36 is proportional to 4 : y, find the common division factor and missing term y cleanly:",
                "options": [
                    "Dividing both terms by factor 6 gives 4 : 6, so y = 6!",
                    "Dividing by 4 gives y = 9",
                    "Subtracting 20 gives y = 16",
                    "y = 12"
                ],
                "answer": 0,
                "hint": "Notice 24 ÷ 6 = 4; apply that exact same factor ÷6 to 36!",
                "explanation": "Dividing both 24 and 36 by factor 6 yields proportional ratio 4 : 6."
            }
        ]
    },
    {
        "id": 4,
        "title": "Simplest Form Proportion",
        "subtitle": "Section 7.3 Simplifying Ratios via HCF & Four-Dot Proportion Notation (a : b :: c : d)",
        "speech": (
            "Now master Section Seven Point Three: RATIOS IN THEIR SIMPLEST FORM! Imagine comparing batch A mixed at 18 : 24 against batch B mixed at 12 : 16! Trying to multiply 18 straight into 12 hits an awkward fractional factor two-thirds! How do mathematicians compare ANY two ratios effortlessly in two seconds? REDUCE BOTH TO SIMPLEST FORM! "
            "Learn the exact HCF reduction method: find the HIGHEST COMMON FACTOR (HCF) shared by BOTH terms of a ratio, then DIVIDE BOTH TERMS BY THAT HCF until no common factor greater than one remains! Test batch A (18 : 24): HCF(18, 24) = 6; dividing both by 6 gives 3 : 4! Test batch B (12 : 16): HCF(12, 16) = 4; dividing both by 4 ALSO gives exact 3 : 4! "
            "Because BOTH mixtures reduce cleanly to the exact IDENTICAL SIMPLEST FORM (3 : 4), we prove 18 : 24 and 12 : 16 stand together cleanly in PROPORTION! Record all such mathematical proportions formally using NCERT's crisp four-dot PROPORTION SYMBOL (::): write 18 : 24 :: 12 : 16 (read aloud cleanly inside class as '18 is to 24 AS 12 is to 16'—confirming identical relative comparison forever)!"
        ),
        "checkpoints": [
            {
                "question": "Reduce ratio 42 : 56 to its simplest form by dividing by HCF(42, 56), and match which ratio forms a valid proportion (::):",
                "options": [
                    "Simplest form = 3 : 4 (HCF = 14);   forms proportion 42 : 56 :: 15 : 20",
                    "Simplest form = 6 : 8;   42 : 56 :: 6 : 9",
                    "Simplest form = 21 : 28;   42 : 56 :: 21 : 24",
                    "Simplest form = 2 : 3;   42 : 56 :: 10 : 15"
                ],
                "answer": 0,
                "hint": "Find HCF(42, 56) = 14 (42÷14 = 3, 56÷14 = 4), then check which option also reduces to 3 : 4!",
                "explanation": "42:56 reduces to 3:4, and 15:20 (÷5) also reduces to 3:4 → 42:56 :: 15:20."
            },
            {
                "question": "What mathematical condition does the four-dot notation (a : b :: c : d) signify?",
                "options": [
                    "Ratios a : b and c : d share the IDENTICAL simplest form (representing equal proportional relationship)",
                    "a + b equals c + d",
                    "b and c must be prime numbers",
                    "Ratio a : b is greater than c : d"
                ],
                "answer": 0,
                "hint": "Recall Section 7.3's definition: 'a is to b as c is to d' when reduced simplest forms match!",
                "explanation": "a : b :: c : d means both ratios reduce to one common simplest form (equivalently ad = bc)."
            }
        ]
    },
    {
        "id": 5,
        "title": "Lemonade Cement Mixtures",
        "subtitle": "Section 7.4 Practical Proportionality: Scaling Lemonade Sweetness & Wall Cement-to-Length Ratios",
        "speech": (
            "Apply proportional reasoning straight into kitchens and civil engineering construction inside Section Seven Point Four! Look at two classic everyday proportionality decisions where keeping ratios steady controls taste and safety! "
            "Scenario One, Maintaining Lemonade Sweetness: A crisp recipe mixes 2 tablespoons of sugar into 3 glasses of lemon water (ratio 2 : 3)! Today a picnic host needs a giant batch using 15 glasses of water—how much sugar maintains that EXACT SAME sweetness? Set up proportion 2 : 3 :: s : 15! Since water scaled from 3 up to 15 by factor FIVE (15 ÷ 3 = 5), multiply sugar 2 by that identical factor FIVE: 2 × 5 = TEN tablespoons of sugar! Adding only +12 instead would ruin sweetness watery! "
            "Scenario Two, Construction Structural Wall Strength: Suppose 4 full bags of cement reinforce a 6-meter garden wall (simplest ratio 2 : 3), while a second contractor mixes 6 bags cleanly across a 9-meter wall (ratio 6 : 9 reduces by 3 to 2 : 3)! Since BOTH share 2 : 3, both walls achieve EQUAL structural cement density—whereas pouring only 5 bags across 10 meters (1 : 2) runs noticeably weaker in real buildings!"
        ),
        "checkpoints": [
            {
                "question": "A recipe uses 3 spoons of sugar for 4 glasses of lemonade. How many spoons keep IDENTICAL sweetness across 20 glasses?",
                "options": [
                    "15 spoons   [scaling factor = 20 ÷ 4 = 5 → 3 × 5 = 15]",
                    "19 spoons   [adding +16 to 3!]",
                    "12 spoons",
                    "24 spoons"
                ],
                "answer": 0,
                "hint": "Multiply sugar 3 by the exact scaling multiplier (20 ÷ 4 = 5)!",
                "explanation": "3 : 4 :: 15 : 20 preserves sweetness identically (multiplier ×5)."
            },
            {
                "question": "Wall A uses 8 cement bags for 12 meters; Wall B uses 10 bags for 15 meters; Wall C uses 9 bags for 18 meters. Which two walls share equal cement-to-length strength?",
                "options": [
                    "Wall A (8:12 = 2:3) and Wall B (10:15 = 2:3) share identical 2:3 strength!",
                    "Wall A and Wall C",
                    "Wall B and Wall C",
                    "All three walls have identical strength"
                ],
                "answer": 0,
                "hint": "Reduce all three ratios cleanly by their HCF (8:12, 10:15, 9:18)!",
                "explanation": "8:12 = 2:3 and 10:15 = 2:3 match proportionally (Wall C is weaker at 1:2)."
            }
        ]
    },
    {
        "id": 6,
        "title": "Age Additive Fallacy",
        "subtitle": "Section 7.4 Additive Non-Proportionality: Why Parent-Child Age Ratios Always Change Over Time",
        "speech": (
            "Catch one of mathematics' most famous real-life traps inside Section Seven Point Four: ADDITIVE NON-PROPORTIONALITY OVER TIME! Imagine a parent aged 30 years and a child aged 10 years right now! What is the parent-to-child age ratio today? Divide 30 : 10 by HCF 10 cleanly—exact THREE TO ONE (the parent is THREE TIMES as old as the child)! "
            "Wait ten calendar years! Both parent and child grow older by adding the EXACT SAME additive constant +10 years! Does the parent STAY three times older forever?! Test cleanly! Ten years later, parent becomes 30 + 10 = 40 years old, and child becomes 10 + 10 = 20 years old! Reduce 40 : 20 by HCF 20: NOW the ratio drops sharply to TWO TO ONE! Wait another twenty years (ages 60 and 40): ratio shrinks again to 3 : 2! "
            "Why did proportionality break completely right before our eyes? Because passing calendar time advances ADDITIVELY (+k years added equally to each person) rather than MULTIPLICATIVELY (×k factor)! Remember forever across word problems: adding ANY non-zero constant equally onto two unequal ratio terms ALWAYS shifts that ratio steadily closer toward equal balance 1 : 1—never keeping initial proportionality intact!"
        ),
        "checkpoints": [
            {
                "question": "Today a mother is 36 and her child is 12 (ratio 3 : 1). What happens to their age ratio 12 years later?",
                "options": [
                    "It shifts to 48 : 24 = 2 : 1 (NOT proportional, because age increases additively by +12 rather than multiplicatively!)",
                    "It stays 3 : 1 forever",
                    "It increases to 4 : 1",
                    "It drops immediately to 1 : 1"
                ],
                "answer": 0,
                "hint": "Add +12 to BOTH ages cleanly (36+12 = 48, 12+12 = 24), then simplify 48 : 24!",
                "explanation": "48 : 24 simplifies to 2 : 1 ≠ 3 : 1, proving uniform addition breaks proportionality."
            },
            {
                "question": "As decades pass for any parent and child, what happens mathematically to the parent-to-child age ratio over many years?",
                "options": [
                    "It steadily decreases closer toward 1 : 1 (without ever reaching 1 : 1)",
                    "It stays constant forever",
                    "It grows infinitely larger",
                    "It flips below 1 : 1"
                ],
                "answer": 0,
                "hint": "Track 3:1 (30:10) → 2:1 (40:20) → 1.5:1 (60:40) → 1.2:1 (120:100)!",
                "explanation": "Adding constant k pulls any unequal ratio (a+k)/(b+k) closer toward 1."
            }
        ]
    },
    {
        "id": 7,
        "title": "Filter Coffee Strength",
        "subtitle": "Section 7.4 Filter Coffee Activity: Decoction-to-Milk Mixture Ratios & Stronger vs Lighter Taste",
        "speech": (
            "Brew crisp South Indian morning filter coffee inside Section Seven Point Four's hands-on FILTER COFFEE ACTIVITY to master mixture strength comparisons completely! Suppose two bustling neighborhood cafés prepare rich morning filter coffee from two ingredients: dark roasted COFFEE DECOCTION and creamy warm MILK! "
            "Compare Cafe Cup One mixed at 20 mL coffee decoction to 80 mL milk (ratio 20 : 80 = 1 : 4) against Cafe Cup Two mixed at 30 mL coffee decoction to 90 mL milk (ratio 30 : 90 = 1 : 3)! Which cup tastes noticeably STRONGER (more concentrated coffee flavor), and which tastes LIGHTER (milkier)? "
            "Use TWO crisp proportional comparison tricks! Trick One, Equalize Decoction (first term = 1): Cup One packs 1 part decoction per 4 parts milk; Cup Two packs 1 part decoction per ONLY 3 parts milk! Less milk per spoon of rich decoction makes Cup Two unmistakably STRONGER! "
            "Trick Two, Compare Fraction of Total Mixture (part-to-whole percentage): Cup One = 20 / 100 = 20% pure coffee decoction; Cup Two = 30 / 120 = 1/4 = 25% pure coffee decoction! Equalizing first terms, second terms, or part-to-whole fractions settles beverage recipe concentrations cleanly every single time!"
        ),
        "checkpoints": [
            {
                "question": "Cup X mixes 20 mL coffee decoction with 60 mL milk (20:60). Cup Y mixes 30 mL decoction with 120 mL milk (30:120). Which cup is STRONGER?",
                "options": [
                    "Cup X is STRONGER  (1 : 3 decoction-to-milk = 25% vs Cup Y's 1 : 4 = 20%!)",
                    "Cup Y is STRONGER because 30 mL > 20 mL",
                    "Both cups taste identically strong",
                    "Cup Y has 50% decoction"
                ],
                "answer": 0,
                "hint": "Don't compare raw decoction 30 vs 20 alone — simplify BOTH ratios 20:60 and 30:120!",
                "explanation": "Cup X (1:3, 1/4 total) packs higher decoction concentration per drop of milk than Cup Y (1:4, 1/5 total)."
            },
            {
                "question": "A barista blends 24 mL decoction with 72 mL milk. How much decoction blended into 120 mL milk produces the EXACT SAME coffee strength?",
                "options": [
                    "40 mL decoction   [ratio 24:72 simplifies cleanly to 1:3 → 120 ÷ 3 = 40 mL!]",
                    "72 mL decoction",
                    "30 mL decoction",
                    "48 mL decoction"
                ],
                "answer": 0,
                "hint": "Simplify 24 : 72 by HCF 24 first (= 1 : 3), then match d : 120 :: 1 : 3!",
                "explanation": "1 : 3 :: 40 : 120 preserves identical 25% coffee concentration."
            }
        ]
    },
    {
        "id": 8,
        "title": "Trairasika Cross Rule",
        "subtitle": "Section 7.4 Trairāśika (Rule of Three): Āryabhaṭa (499 CE) Pramāṇa, Phala, Ichchhā & ad = bc",
        "speech": (
            "Unlock Section Seven Point Four's jewel of Indian and global mathematics: TRAIRĀŚIKA—THE RULE OF THREE! Whenever three proportional numbers are known and the FOURTH unknown value must be discovered (a : b :: c : d), cross-multiplication solves it in one crisp step! "
            "Derive cross-multiplication step by step cleanly! Whenever a : b :: c : d holds, BOTH ratios equal the EXACT identical fraction value a/b = c/d! Multiply both sides smoothly by common denominator product (b × d): a × d ALWAYS EQUALS b × c (product of outer extremes equals product of inner means)! Solving directly for unknown fourth value d yields exact formula: d = (b × c) ÷ a! "
            "Celebrate ĀRYABHAṬA'S 499 Common Era Sanskrit formulation of Trairāśika inside his classic treatise Āryabhaṭīya! Āryabhaṭa named the three known quantities with unforgettable precision: PRAMĀṆA (standard reference measure = a), PHALA (resulting fruit/yield = b), and ICHCHHĀ (desired requisition = c)! Always multiply Phala times Ichchhā first, then divide cleanly by Pramāṇa to compute unknown ICHCHHĀPHALA (d): (Phala × Ichchhā) ÷ Pramāṇa! Test immediately: if 5 notebooks (Pramāṇa) cost 120 rupees (Phala), 8 notebooks (Ichchhā) cost (120 × 8) ÷ 5 = 192 rupees cleanly every single time!"
        ),
        "checkpoints": [
            {
                "question": "In Āryabhaṭa's (499 CE) Trairāśika (Rule of Three), match the four classical Sanskrit terms cleanly to proportion (a : b :: c : d):",
                "options": [
                    "a = pramāṇa (measure),   b = phala (fruit),   c = ichchhā (requisition),   unknown d = ichchhāphala = (phala × ichchhā) ÷ pramāṇa",
                    "a = phala,   b = pramāṇa,   d = (a × c) ÷ b",
                    "d = (pramāṇa × phala) ÷ ichchhā",
                    "d = a + b + c"
                ],
                "answer": 0,
                "hint": "Recall: multiply Phala (b) by Ichchhā (c), then divide by Pramāṇa (a)!",
                "explanation": "Āryabhaṭa defined ichchhāphala = (phala × ichchhā) / pramāṇa, matching ad = bc → d = bc/a."
            },
            {
                "question": "Solve proportion 12 : 18 :: 20 : d using cross-multiplication (ad = bc):",
                "options": [
                    "d = 30   [= (18 × 20) ÷ 12 = 360 ÷ 12]",
                    "d = 26   [added +8]",
                    "d = 13.33",
                    "d = 24"
                ],
                "answer": 0,
                "hint": "Set 12 × d = 18 × 20 cleanly and divide 360 by 12!",
                "explanation": "12d = 360 → d = 30 (check: both 12:18 and 20:30 simplify cleanly to 2:3!)."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part1)} slides for Ch7 Class 8 Maths Part 1.")
    for s in slides_part1:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: {s['title']!r} ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Slide {s['id']} title length {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 1 assertions passed cleanly!")
