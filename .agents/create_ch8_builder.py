import re

with open('.agents/build_class7_math_tale_of_three_intersecting_lines_lab.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace data, sims, js modules
text = text.replace('class7_math_tale_of_three_intersecting_lines_data', 'class7_math_working_with_fractions_data')
text = text.replace('class7_math_tale_of_three_intersecting_lines_sims', 'class7_math_working_with_fractions_sims')
text = text.replace('class7_math_tale_of_three_intersecting_lines_js', 'class7_math_working_with_fractions_js')

# Output filename
text = text.replace('public/animations/class7-math-tale-of-three-intersecting-lines.html', 'public/animations/class7-math-working-with-fractions.html')

# Chapter title & mentor
text = text.replace('Chapter 7: A Tale of Three Intersecting Lines Master Lab', 'Chapter 8: Working with Fractions Master Lab')
text = text.replace('Chapter 7: A Tale of Three Intersecting Lines', 'Chapter 8: Working with Fractions')
text = text.replace('Chapter 7 A Tale of Three Intersecting Lines', 'Chapter 8 Working with Fractions')
text = text.replace('Acharya Baudhāyana', 'Acharya Brahmagupta')
text = text.replace('Acharya Baudhayana', 'Acharya Brahmagupta')
text = text.replace('Pioneer of Indian Geometry & Śulba Sūtras', 'Master of Mathematical Astronomy & Father of Fraction Laws')
text = text.replace('Master of Sulba Sutra Geometry & Cord-Constructions', 'Master of Mathematical Astronomy & Father of Fraction Laws')
text = text.replace('Baudhāyana\'s Sulba Wisdom:', 'Brahmagupta\'s Fraction Wisdom:')
text = text.replace('Baudhayana\'s Sulba Wisdom:', 'Brahmagupta\'s Fraction Wisdom:')
text = text.replace('Baudhāyana', 'Brahmagupta')
text = text.replace('Baudhayana', 'Brahmagupta')
text = text.replace('📐', '🧮')

# Replace simulator dispatch switch
old_switch = """      // Initialize simulator logic
      switch(simId) {
        case 'sim-triangle-anatomy':
          updateAnatomyApex(250);
          break;
        case 'sim-equilateral-compass':
          stepEquilateral(1);
          break;
        case 'sim-triangle-inequality':
          updateInequality();
          break;
        case 'sim-circle-intersections':
          updateCircleIntersections();
          break;
        case 'sim-sss-construction':
          setSSSPreset('scalene');
          break;
        case 'sim-sas-construction':
          updateSAS();
          break;
        case 'sim-asa-construction':
          updateASA();
          break;
        case 'sim-angle-sum-proof':
          setAngleSumMode('parallel');
          break;
        case 'sim-exterior-angle':
          updateExtAngle(220);
          break;
        case 'sim-altitude-definition':
          updateAltDef(240);
          break;
        case 'sim-set-square-drafting':
          updateSetSquarePos(160);
          break;
        case 'sim-altitude-cases':
          setAltCase('acute');
          break;
        case 'sim-orthocenter-concurrency':
          updateOrthocenter(230);
          break;
        case 'sim-triangle-by-sides':
          setSideFamily('equi');
          break;
        case 'sim-triangle-by-angles':
          setAngleClass('acute');
          break;
        case 'sim-master-matrix-sulba':
          setSulbaTriple(3, 4, 5);
          break;
      }"""

new_switch = """      // Initialize simulator logic
      switch(simId) {
        case 'sim-fraction-visualizer':
          updateFractionVisualizer();
          break;
        case 'sim-repeated-addition':
          updateRepeatedAddition();
          break;
        case 'sim-fraction-of-fraction':
          updateFractionOfFraction();
          break;
        case 'sim-unit-square-grid':
          updateUnitSquareGrid();
          break;
        case 'sim-brahmagupta-product':
          calcBrahmaguptaProduct();
          break;
        case 'sim-cross-cancelling':
          setCcProblem(3, 8, 4, 9);
          break;
        case 'sim-product-size-comparator':
          setPscCase('proper_proper');
          break;
        case 'sim-commutativity-rotator':
          rotateCommutativity();
          break;
        case 'sim-reciprocal-flip':
          setReciprocalFraction(3, 7);
          break;
        case 'sim-division-grouping':
          setDgScenario(2, 0.5, '2 ÷ (1/2)');
          break;
        case 'sim-division-inverter':
          setDiProblem(5, 6, 2, 3);
          break;
        case 'sim-quotient-magnifier':
          updateQuotientMagnifier();
          break;
        case 'sim-milk-sharing-speed':
          updatePrDisplay();
          break;
        case 'sim-sulbasutra-bricks':
          setSbBrick('quarter');
          break;
        case 'sim-cistern-fountain':
          renderCisternLevel(0);
          break;
        case 'sim-lilavati-donation':
          updateLilavatiRiddle();
          break;
      }"""

if old_switch in text:
    text = text.replace(old_switch, new_switch)
    print("Successfully replaced simulator dispatch switch!")
else:
    print("Warning: old_switch was not found directly, performing regex search...")
    # fallback regex replace
    text = re.sub(r'// Initialize simulator logic\s+switch\(simId\)\s*\{[^}]*\}', new_switch, text, flags=re.DOTALL)

with open('.agents/build_class7_math_working_with_fractions_lab.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Created .agents/build_class7_math_working_with_fractions_lab.py successfully!")

