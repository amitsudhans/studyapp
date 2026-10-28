import re

with open('.agents/build_class7_math_arithmetic_expressions_lab.py', 'r', encoding='utf-8') as f:
    text = f.read()

replacements = [
    ('class7_math_arithmetic_expressions_data', 'class7_math_expressions_letter_numbers_data'),
    ('class7_math_arithmetic_expressions_sims', 'class7_math_expressions_letter_numbers_sims'),
    ('public/animations/class7-math-arithmetic-expressions.html', 'public/animations/class7-math-expressions-letter-numbers.html'),
    ('Chapter 2: Arithmetic Expressions', 'Chapter 4: Expressions Using Letter-Numbers'),
    ('Chapter 2 Arithmetic Expressions', 'Chapter 4 Expressions Using Letter-Numbers'),
    ('Acharya Brahmagupta', 'Acharya Bhaskara II'),
    ('Master of Arithmetic & Numerical Laws', 'Father of Indian Algebra & Author of Bijaganita'),
    ("Brahmagupta's Wisdom:", "Bhaskara's Bijaganita Wisdom:"),
    ('Mastery Challenge: Arithmetic Expressions', 'Mastery Challenge: Expressions Using Letter-Numbers')
]

for old, new in replacements:
    text = text.replace(old, new)

new_switch = """switch(simId) {
        case 'letter_number_machine_sim':
          simLetterNumberMachine();
          break;
        case 'variable_vs_constant_balance_sim':
          simVariableVsConstantBalance();
          break;
        case 'evaluating_algebraic_expr_sim':
          simEvaluatingAlgebraicExpr();
          break;
        case 'word_to_algebra_translator_sim':
          simWordToAlgebraTranslator();
          break;
        case 'omission_of_multiplication_sim':
          simOmissionOfMultiplication();
          break;
        case 'terms_coefficients_anatomy_sim':
          simTermsCoefficientsAnatomy();
          break;
        case 'like_vs_unlike_terms_sorter_sim':
          simLikeVsUnlikeTermsSorter();
          break;
        case 'combining_like_terms_pipeline_sim':
          simCombiningLikeTermsPipeline();
          break;
        case 'distributive_letters_area_sim':
          simDistributiveLettersArea();
          break;
        case 'formula_detective_sim':
          simFormulaDetective();
          break;
        case 'number_sequences_general_term_sim':
          simNumberSequencesGeneralTerm();
          break;
        case 'calendar_patterns_matrix_sim':
          simCalendarPatternsMatrix();
          break;
        case 'calendar_cross_column_sim':
          simCalendarCrossColumn();
          break;
        case 'matchstick_patterns_chain_sim':
          simMatchstickPatternsChain();
          break;
        case 'matchstick_complex_geometries_sim':
          simMatchstickComplexGeometries();
          break;
        case 'bhaskara_bijaganita_puzzles_sim':
          simBhaskaraBijaganitaPuzzles();
          break;
        default:
          simCanvas.innerHTML = '<div style="color:#94a3b8; font-size:0.95rem;">Interactive Simulator Active</div>';
      }"""

text = re.sub(r'switch\(simId\)\s*\{.*?default:.*?\}', new_switch, text, flags=re.DOTALL)

with open('.agents/build_class7_math_expressions_letter_numbers_lab.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Successfully generated .agents/build_class7_math_expressions_letter_numbers_lab.py')
