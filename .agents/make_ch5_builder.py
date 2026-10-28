import re

with open('.agents/build_class7_math_expressions_letter_numbers_lab.py', 'r', encoding='utf-8') as f:
    text = f.read()

replacements = [
    ('class7_math_expressions_letter_numbers_data', 'class7_math_parallel_intersecting_lines_data'),
    ('class7_math_expressions_letter_numbers_sims', 'class7_math_parallel_intersecting_lines_sims'),
    ('public/animations/class7-math-expressions-letter-numbers.html', 'public/animations/class7-math-parallel-intersecting-lines.html'),
    ('Chapter 4: Expressions Using Letter-Numbers', 'Chapter 5: Parallel and Intersecting Lines'),
    ('Chapter 4 Expressions Using Letter-Numbers', 'Chapter 5 Parallel and Intersecting Lines'),
    ('Acharya Bhaskara II', 'Acharya Baudhayana'),
    ('Father of Indian Algebra & Author of Bijaganita', 'Master of Sulba Sutra Geometry & Cord-Constructions'),
    ("Bhaskara's Bijaganita Wisdom:", "Baudhayana's Sulba Wisdom:"),
    ('Mastery Challenge: Expressions Using Letter-Numbers', 'Mastery Challenge: Parallel and Intersecting Lines')
]

for old, new in replacements:
    text = text.replace(old, new)

new_switch = """switch(simId) {
        case 'intersecting_lines_scissors_sim':
          simIntersectingLinesScissors();
          break;
        case 'linear_pair_slider_sim':
          simLinearPairSlider();
          break;
        case 'perpendicular_lines_cross_sim':
          simPerpendicularLinesCross();
          break;
        case 'parallel_railway_tracks_sim':
          simParallelRailwayTracks();
          break;
        case 'paper_folding_perpendicular_sim':
          simPaperFoldingPerpendicular();
          break;
        case 'paper_folding_parallel_sim':
          simPaperFoldingParallel();
          break;
        case 'transversal_eight_angles_sim':
          simTransversalEightAngles();
          break;
        case 'corresponding_angles_f_shape_sim':
          simCorrespondingAnglesFShape();
          break;
        case 'parallelism_detector_sim':
          simParallelismDetector();
          break;
        case 'ruler_set_square_construction_sim':
          simRulerSetSquareConstruction();
          break;
        case 'alternate_interior_z_shape_sim':
          simAlternateInteriorZShape();
          break;
        case 'alternate_exterior_angles_sim':
          simAlternateExteriorAngles();
          break;
        case 'co_interior_c_shape_sim':
          simCoInteriorCShape();
          break;
        case 'cafe_wall_illusion_sim':
          simCafeWallIllusion();
          break;
        case 'hering_zollner_illusions_sim':
          simHeringZollnerIllusions();
          break;
        case 'baudhayana_sulba_ropes_sim':
          simBaudhayanaSulbaRopes();
          break;
        default:
          simCanvas.innerHTML = '<div style="color:#94a3b8; font-size:0.95rem;">Interactive Simulator Active</div>';
      }"""

text = re.sub(r'switch\(simId\)\s*\{.*?default:.*?\}', new_switch, text, flags=re.DOTALL)

with open('.agents/build_class7_math_parallel_intersecting_lines_lab.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Successfully generated .agents/build_class7_math_parallel_intersecting_lines_lab.py')
