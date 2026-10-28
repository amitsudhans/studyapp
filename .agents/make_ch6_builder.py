import re

with open('.agents/build_class7_math_parallel_intersecting_lines_lab.py', 'r', encoding='utf-8') as f:
    text = f.read()

replacements = [
    ('class7_math_parallel_intersecting_lines_data', 'class7_math_number_play_data'),
    ('class7_math_parallel_intersecting_lines_sims', 'class7_math_number_play_sims'),
    ('public/animations/class7-math-parallel-intersecting-lines.html', 'public/animations/class7-math-number-play.html'),
    ('Chapter 5: Parallel and Intersecting Lines', 'Chapter 6: Number Play'),
    ('Chapter 5 Parallel and Intersecting Lines', 'Chapter 6 Number Play'),
    ('Acharya Baudhayana', 'Acharya Virahāńka'),
    ('Master of Sulba Sutra Geometry & Cord-Constructions', 'Pioneer of Indian Combinatorics & Rhythmic Number Sequences'),
    ("Baudhayana's Sulba Wisdom:", "Virahāńka's Rhythm Wisdom:"),
    ('Mastery Challenge: Parallel and Intersecting Lines', 'Mastery Challenge: Number Play')
]

for old, new in replacements:
    text = text.replace(old, new)

new_switch = """switch(simId) {
        case 'height_queue_decoder_sim':
          simHeightQueueDecoder();
          break;
        case 'positional_lineup_invariants_sim':
          simPositionalLineupInvariants();
          break;
        case 'parity_pair_matching_sim':
          simParityPairMatching();
          break;
        case 'parity_arithmetic_matrix_sim':
          simParityArithmeticMatrix();
          break;
        case 'grid_squares_parity_sim':
          simGridSquaresParity();
          break;
        case 'algebraic_parity_nth_term_sim':
          simAlgebraicParityNthTerm();
          break;
        case 'magic_square_3x3_sim':
          simMagicSquare3x3();
          break;
        case 'magic_square_center_rule_sim':
          simMagicSquareCenterRule();
          break;
        case 'chautisa_yantra_4x4_sim':
          simChautisaYantra4x4();
          break;
        case 'virahanka_poetic_meter_sim':
          simVirahankaPoeticMeter();
          break;
        case 'fibonacci_virahanka_sequence_sim':
          simFibonacciVirahankaSequence();
          break;
        case 'nature_petals_spirals_sim':
          simNaturePetalsSpirals();
          break;
        case 'virahanka_parity_cycle_sim':
          simVirahankaParityCycle();
          break;
        case 'cryptarithm_single_digit_sim':
          simCryptarithmSingleDigit();
          break;
        case 'classic_alphametic_deduction_sim':
          simClassicAlphameticDeduction();
          break;
        case 'heritage_number_play_sim':
          simHeritageNumberPlay();
          break;
        default:
          simCanvas.innerHTML = '<div style="color:#94a3b8; font-size:0.95rem;">Interactive Simulator Active</div>';
      }"""

text = re.sub(r'switch\(simId\)\s*\{.*?default:.*?\}', new_switch, text, flags=re.DOTALL)

with open('.agents/build_class7_math_number_play_lab.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Successfully generated .agents/build_class7_math_number_play_lab.py')
