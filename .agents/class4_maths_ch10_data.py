# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 10: Elephants, Tigers, and Leopards
Full 20-slide structured curriculum dataset.
"""

SLIDES_DATA = [   {   'checkpoints': [   {   'ans': 0,
                               'exp': 'Each player can only add either 1 or 2 to the running total.',
                               'options': ['1 or 2', '1, 2, or 3', 'Any number up to 5', 'Only 2'],
                               'q': 'In the target-10 Nim addition game, what are the allowed numbers a player can add '
                                    'on their turn?'},
                           {   'ans': 1,
                               'exp': 'The maximum allowed addition is 2, which only reaches 7 + 2 = 9.',
                               'options': [   'Yes, by adding 3',
                                              'No, max addition is 2 (reaches 9)',
                                              'Yes, by adding 1',
                                              'Game is tied'],
                               'q': 'If the running total is 7, can the next player reach 10 on that immediate turn?'}],
        'id': 1,
        'section': 'Two-Player Strategic Running Sums',
        'speech': 'Welcome young scholars to an exhilarating mathematical journey into numbers, wildlife data, and '
                  'strategic game theory! We begin our exploration with a classic two-player strategy game known as '
                  'the Nim addition game. Two players alternate turns adding either one or two to a shared running '
                  'total, starting at zero. The player who first reaches the exact target number of ten wins the game! '
                  'Let us observe a sample match. The first player calls out two, setting the total to two. The second '
                  'player adds one, bringing the total to three. The first player adds two, making it five. The second '
                  "player adds two, raising the total to seven! Now consider the first player's dilemma: adding one "
                  'makes eight, allowing the second player to add two and reach ten; adding two makes nine, allowing '
                  'the second player to add one and reach ten! Whichever move the first player chooses from seven, the '
                  'second player claims the victory. This game proves that arithmetic is not just mechanical '
                  'calculation; it involves forward planning, backward deduction, and controlling critical numerical '
                  'thresholds. Understanding how smaller additions accumulate toward a target unlocks strategic '
                  'thinking, transforming simple addition into an exciting intellectual contest of wit and '
                  'mathematical foresight.',
        'title': 'Nim Addition Strategy'},
    {   'checkpoints': [   {   'ans': 1,
                               'exp': 'Controlling 7 guarantees winning 10, because 7 + 1 = 8 (add 2) and 7 + 2 = 9 '
                                      '(add 1).',
                               'options': ['6', '7', '8', '9'],
                               'q': 'What is the key winning threshold number right before target 10?'},
                           {   'ans': 1,
                               'exp': 'The winning positions differ by 3: 1, 4, 7, and 10.',
                               'options': ['2, 4, 6, 8, 10', '1, 4, 7, 10', '3, 6, 9, 10', '1, 3, 5, 7, 10'],
                               'q': 'What is the complete sequence of winning milestones in target-10 Nim?'}],
        'id': 2,
        'section': 'Backward Induction & Modulo 3 Invariants',
        'speech': 'To consistently master the Nim addition game, mathematicians utilize backward reasoning to identify '
                  'winning and losing positions. If our ultimate goal is to say ten, what number must we reach on the '
                  'turn before? The answer is seven! From seven, if your opponent adds one to reach eight, you add two '
                  'to claim ten; if your opponent adds two to reach nine, you add one to claim ten. Therefore, '
                  'reaching seven guarantees victory! Now we ask: what prior milestone guarantees reaching seven? By '
                  'subtracting three, we discover that controlling four ensures victory! From four, if the opponent '
                  'adds one to make five, you add two to reach seven; if they add two to make six, you add one to '
                  'reach seven. Working backward one step further, subtracting three from four yields one. If the '
                  'first player begins by calling one, and subsequently claims four, seven, and ten, they can never be '
                  'defeated! The sequence one, four, seven, and ten represents the invariant winning positions, '
                  'differing by three on every step. Backward induction teaches us to begin with the desired outcome '
                  'and trace logical steps backward, a profound problem-solving principle applied across computer '
                  'science, economics, logistics, and competitive mathematical games.',
        'title': 'Winning Position Analysis'},
    {   'checkpoints': [   {   'ans': 2,
                               'exp': 'Diagonals sloping from bottom-left to top-right contain identical sums (e.g., '
                                      'all 9s).',
                               'options': [   'Vertical columns',
                                              'Horizontal rows',
                                              'Bottom-left to top-right diagonals',
                                              'Main diagonal'],
                               'q': 'Along which direction on an addition chart are all numbers identical?'},
                           {   'ans': 2,
                               'exp': 'From 0+9 to 9+0, there are exactly 10 pairs totaling 9.',
                               'options': ['8 pairs', '9 pairs', '10 pairs', '12 pairs'],
                               'q': 'How many different addition pairs on the 0-12 grid sum to exactly 9?'}],
        'id': 3,
        'section': '13×13 Grid Explorations & Sum Frequencies',
        'speech': 'Now let us examine an expansive addition chart spanning thirteen rows and thirteen columns, '
                  'representing all sums of whole numbers from zero through twelve. Constructing this comprehensive '
                  'grid reveals an astonishing tapestry of symmetry, repeating patterns, and frequency distributions. '
                  'Notice the diagonals running from bottom-left to top-right: every cell along a single diagonal '
                  'displays the exact same sum! For example, the number nine appears across ten distinct cells: zero '
                  'plus nine, one plus eight, two plus seven, three plus six, four plus five, five plus four, six plus '
                  'three, seven plus two, eight plus one, and nine plus zero. The frequency of each sum increases '
                  'steadily from zero up to twelve, reaching its maximum frequency at twelve with thirteen '
                  'occurrences, and then decreases symmetrically down to twenty-four. Investigating row and column '
                  'parity reveals further order: even rows alternate between even and odd sums, while adding two even '
                  'numbers always yields an even sum. Exploring addition charts shifts computational thinking from '
                  'isolated addition drills into holistic structural understanding. Recognizing how numbers partition '
                  'into diverse addends deepens mental flexibility, strengthens number bonds, and forms the '
                  'mathematical bedrock for algebraic decomposition and combinatorial probability analysis across '
                  'advanced branches of science and mathematics.',
        'title': 'Addition Chart Patterns'},
    {   'checkpoints': [   {   'ans': 2,
                               'exp': 'Each line of 3 numbers equals 3 × central number = 3 × 10 = 30.',
                               'options': ['20', '25', '30', '40'],
                               'q': 'In a 3×3 window on the addition chart with center 10, what is the sum of any line '
                                    'passing through the center?'},
                           {   'ans': 2,
                               'exp': 'Total sum = 9 × central number = 9 × 10 = 90.',
                               'options': ['60', '80', '90', '100'],
                               'q': 'What is the sum of all 9 numbers in a 3×3 window with central number 10?'}],
        'id': 4,
        'section': 'Sub-Grid Magic & Centroid Multiples',
        'speech': 'Within our grand thirteen-by-thirteen addition chart, placing a highlighted three-by-three window '
                  'frame reveals a delightful hidden relationship known as the centroid multiple theorem. Suppose we '
                  'frame nine adjacent cells centered on the number ten. The middle row reads nine, ten, and eleven. '
                  'The top row reads eight, nine, and ten, while the bottom row reads ten, eleven, and twelve. Let us '
                  'compute the sums across various directions! The horizontal middle row sums to nine plus ten plus '
                  'eleven, equaling thirty. The vertical central column sums to nine plus ten plus eleven, which also '
                  'equals thirty! Now look at the diagonals: eight plus ten plus twelve equals thirty, and ten plus '
                  'ten plus ten equals thirty! Every line passing through the central cell sums to exactly three times '
                  'the central number! Furthermore, adding all nine numbers within the window frame yields exactly '
                  'ninety, which is nine times the central number ten! This remarkable property holds true wherever '
                  'the three-by-three frame is placed on the chart. Window frame puzzles illuminate spatial balance, '
                  'prove that arithmetic sequences balance around their midpoint, and demonstrate how geometric '
                  'symmetry governs numerical structures across matrices, computational grids, and algebraic number '
                  'patterns throughout our world.',
        'title': 'Window Frame Sums'},
    {   'checkpoints': [   {   'ans': 1,
                               'exp': '27 + 72 = 99.',
                               'options': ['89', '99', '109', '110'],
                               'q': 'What do you get when you reverse and add 27 (27 + 72)?'},
                           {   'ans': 2,
                               'exp': '(10a + b) + (10b + a) = 11(a + b), which is always a multiple of 11.',
                               'options': ['9', '10', '11', '12'],
                               'q': 'The sum of any 2-digit number and its reverse is always an exact multiple of '
                                    'which number?'}],
        'id': 5,
        'section': 'Digit Palindromes & Multiples of Eleven',
        'speech': 'A fascinating arithmetic pattern emerges when we take two-digit numbers, reverse their digits, and '
                  'add the two values together. Suppose we select the number twenty-seven. Reversing its digits yields '
                  'seventy-two. Adding twenty-seven and seventy-two produces ninety-nine! What if we select '
                  'thirty-four? Its reverse is forty-three, and thirty-four plus forty-three equals seventy-seven! '
                  'Notice something extraordinary about all these sums: ninety-nine, seventy-seven, fifty-five, and '
                  'eighty-eight are all multiples of eleven! Why does this always occur? Let us examine the algebra of '
                  'place value. Any two-digit number consisting of tens digit A and ones digit B equals ten A plus B. '
                  'Its reverse equals ten B plus A. Adding them produces eleven A plus eleven B, which factors into '
                  'eleven times the sum of A and B! Therefore, reversing and adding any two-digit number always '
                  'generates an exact multiple of eleven. If the sum of the digits exceeds nine, the result produces a '
                  'three-digit multiple: for instance, eighty-four plus forty-eight equals one hundred thirty-two, '
                  'which equals eleven times twelve! Reverse-and-add patterns demystify place value mechanics, reveal '
                  'beautiful algebraic palindromes, and show how underlying decimal structures produce elegant '
                  'invariants, fostering deep mathematical curiosity, confidence, and deep mathematical joy, and '
                  'lifelong numerical appreciation.',
        'title': 'Reverse And Add'},
    {   'checkpoints': [   {   'ans': 1,
                               'exp': 'Karnataka hosts approximately 6,049 Asian elephants, the highest in the '
                                      'southern corridor.',
                               'options': ['Goa', 'Karnataka', 'Punjab', 'Haryana'],
                               'q': 'Which state hosts over 6,000 Asian elephants according to national wildlife '
                                    'census records?'},
                           {   'ans': 1,
                               'exp': 'Accurate census counts help conservationists monitor population trends and '
                                      'protect natural habitats.',
                               'options': [   'To design animal cages',
                                              'To monitor endangered populations and protect habitats',
                                              'To guess forest trees',
                                              'To paint tigers'],
                               'q': 'Why do wildlife scientists rely on accurate multi-digit arithmetic?'}],
        'id': 6,
        'section': 'Biodiversity Conservation & Large Figures',
        'speech': 'Mathematics serves as an indispensable tool for environmental science, particularly when tracking '
                  "endangered wildlife populations across India's magnificent national parks and forest reserves. "
                  'Wildlife biologists conduct comprehensive census surveys to monitor majestic apex species including '
                  'Asian elephants, royal Bengal tigers, and Indian leopards. These census reports present large '
                  'four-digit numbers requiring precise quantitative analysis. According to national survey records, '
                  'the elephant population in Karnataka stands at approximately six thousand forty-nine, while '
                  "neighboring Kerala shelters three thousand fifty-four elephants. Meanwhile, India's tiger "
                  'population has rebounded remarkably, with Madhya Pradesh recording seven hundred eighty-five tigers '
                  'and Uttarakhand recording five hundred sixty tigers. For leopards, central and southern states '
                  'shelter robust numbers, with Karnataka hosting nearly three thousand nine hundred leopards and '
                  'Madhya Pradesh hosting over three thousand nine hundred. Analyzing wildlife census data connects '
                  'mathematical learning with conservation stewardship. By comparing, adding, and subtracting '
                  'real-world population metrics, young scholars appreciate how mathematics empowers forestry '
                  'officials to safeguard delicate ecosystems, prevent habitat fragmentation, and ensure that our '
                  "nation's rich biodiversity thrives for future generations to cherish, establishing sustainable "
                  'wildlife reserves, comprehensive census databases, active animal tracking, and rigorous ecological '
                  'protection policies safely across our magnificent, biologically diverse nation.',
        'title': 'Wildlife Census Data'},
    {   'checkpoints': [   {   'ans': 1,
                               'exp': '6,049 + 3,054 = 9,103 (with regrouping in ones and tens columns).',
                               'options': ['9,093', '9,103', '9,113', '9,203'],
                               'q': 'What is 6,049 + 3,054 calculated column by column?'},
                           {   'ans': 1,
                               'exp': 'In base-ten place value, 10 ones regroup into 1 ten rod.',
                               'options': [   'They disappear',
                                              'They regroup into 1 ten rod',
                                              'They become 100',
                                              'They form a thousand'],
                               'q': 'What happens when 10 ones units are bundled together?'}],
        'id': 7,
        'section': 'Thousands Regrouping & Concrete Tokens',
        'speech': 'When combining large four-digit populations, we employ the standard column addition algorithm '
                  'supported by concrete place-value tokens. Imagine representing numbers using color-coded tokens: '
                  'yellow thousand cubes, green hundred flats, blue ten rods, and red one units. Let us calculate the '
                  'combined elephant population of Karnataka and Kerala by adding six thousand forty-nine and three '
                  'thousand fifty-four. We align the two quantities meticulously by place value columns: Thousands, '
                  'Hundreds, Tens, and Ones. Starting in the ones column, nine plus four equals thirteen. Thirteen '
                  'ones cannot remain in the ones column, so we regroup ten ones into one ten rod, leaving three units '
                  'and carrying one ten to the tens column! In the tens column, our carried one plus four plus five '
                  'equals ten tens. Regrouping ten tens creates one hundred flat, leaving zero in the tens place and '
                  'carrying one to the hundreds column! In the hundreds column, one plus zero plus zero equals one. '
                  'Finally, in the thousands column, six plus three equals nine thousands. Combining our columns '
                  'yields nine thousand one hundred three elephants! Regrouping tokens provides an unshakeable '
                  'conceptual foundation, demonstrating that column carries are physical re-bundlings in our base-ten '
                  'decimal place-value system.',
        'title': 'Place Value Addition'},
    {   'checkpoints': [   {   'ans': 2,
                               'exp': '444 + 116 = 560 tigers.',
                               'options': ['540 tigers', '550 tigers', '560 tigers', '570 tigers'],
                               'q': 'If Maharashtra has 444 tigers and Uttarakhand has 116 more, how many tigers are '
                                    'in Uttarakhand?'},
                           {   'ans': 1,
                               'exp': '560 + 785 = 1,345 tigers.',
                               'options': ['1,245', '1,345', '1,355', '1,445'],
                               'q': 'What is the combined tiger population of Uttarakhand (560) and Madhya Pradesh '
                                    '(785)?'}],
        'id': 8,
        'section': 'Multi-State Comparisons & Two-Step Sums',
        'speech': 'Let us apply our multi-digit addition skills to solve compelling comparative word problems about '
                  'regional tiger populations. Suppose national census records report that Maharashtra shelters four '
                  "hundred forty-four wild tigers. In Uttarakhand, the tiger population exceeds Maharashtra's count by "
                  "one hundred sixteen tigers. In Madhya Pradesh, the tiger population exceeds Maharashtra's count by "
                  'three hundred forty-one tigers. How many tigers inhabit Madhya Pradesh and Uttarakhand combined? To '
                  "solve this two-step inquiry, we first determine each state's individual total. For Uttarakhand, "
                  'four hundred forty-four plus one hundred sixteen equals five hundred sixty tigers. For Madhya '
                  'Pradesh, four hundred forty-four plus three hundred forty-one equals seven hundred eighty-five '
                  'tigers! Now, we sum the two regional populations: five hundred sixty plus seven hundred '
                  'eighty-five. Adding column by column, zero plus five gives five ones; six plus eight gives fourteen '
                  'tens, carrying one hundred; and one plus five plus seven gives thirteen hundreds! The grand total '
                  'is one thousand three hundred forty-five tigers! Methodically translating word descriptions into '
                  'sequential addition sentences prevents confusion, trains analytical thinking, and provides clear '
                  'quantitative answers for complex ecological conservation reports, regional forestry assessments, '
                  'and governmental biodiversity management plans across all conservation areas throughout our nation.',
        'title': 'Tiger Population Word'},
    {   'checkpoints': [   {   'ans': 2,
                               'exp': '5,719 - 1,754 = 3,965.',
                               'options': ['3,865', '3,955', '3,965', '4,065'],
                               'q': 'What is 5,719 - 1,754 calculated using column subtraction with regrouping?'},
                           {   'ans': 1,
                               'exp': '1 hundred equals exactly 10 tens.',
                               'options': ['5 tens', '10 tens', '50 tens', '100 tens'],
                               'q': 'When you unbundle 1 hundred in the column algorithm, how many tens do you '
                                    'obtain?'}],
        'id': 9,
        'section': 'Multi-Digit Subtraction & Token Unbundling',
        'speech': 'Just as addition bundles smaller units into larger place values, subtraction performs the reverse '
                  'operation: unbundling higher-order units whenever the top digit is smaller than the bottom digit. '
                  'Let us examine how wildlife biologists calculate population differences between regional wildlife '
                  'reserves. According to census records, Assam shelters five thousand seven hundred nineteen wild '
                  'elephants, while Meghalaya shelters one thousand seven hundred fifty-four elephants. To determine '
                  'how many more elephants inhabit Assam, we subtract one thousand seven hundred fifty-four from five '
                  'thousand seven hundred nineteen. Aligning the numbers by place value columns, we begin in the ones '
                  'place: nine minus four leaves five ones. Moving to the tens place, we encounter one ten minus five '
                  'tens. Because we cannot subtract five from one, we unbundle one hundred from the hundreds place, '
                  'reducing seven hundreds to six hundreds and converting the unbundled hundred into ten tens! Adding '
                  'these ten tens to our existing one ten gives eleven tens. Now, eleven tens minus five tens equals '
                  'six tens! In the hundreds place, six hundreds minus seven hundreds requires another unbundling: '
                  'unbundling one thousand gives sixteen hundreds, and sixteen minus seven leaves nine hundreds. '
                  'Finally, four thousands minus one thousand leaves three thousands, yielding three thousand nine '
                  'hundred sixty-five elephants! Unbundling tokens ensures mathematical transparency and computational '
                  'precision everywhere.',
        'title': 'Regrouping Subtraction Math'},
    {   'checkpoints': [   {   'ans': 2,
                               'exp': '9,115 - 8,426 = 689 visitors.',
                               'options': ['589 visitors', '679 visitors', '689 visitors', '711 visitors'],
                               'q': 'How many more visitors came in January (9,115) than December (8,426)?'},
                           {   'ans': 1,
                               'exp': 'Tracking tourist attendance helps park rangers deploy resources sustainably and '
                                      'protect animal habitats.',
                               'options': [   'To buy more tourist binoculars',
                                              'To manage safari jeeps and safeguard forest wildlife',
                                              'To feed wild animals',
                                              'To close roads forever'],
                               'q': 'Why do forest rangers track visitor numbers using precise multi-digit '
                                    'subtraction?'}],
        'id': 10,
        'section': 'Tourism Data & Comparative Visitor Audits',
        'speech': 'National parks and tiger reserves maintain meticulous attendance registries to monitor seasonal '
                  'tourism flows and protect delicate forest habitats from overcrowding. Consider visitor records from '
                  'Kaziranga National Park, celebrated globally for its magnificent one-horned rhinoceroses. During '
                  'the festive month of December, the park welcomed eight thousand four hundred twenty-six visitors. '
                  'In the cooler month of January, attendance surged to nine thousand one hundred fifteen visitors. '
                  'How many additional tourists explored the park in January compared to December? To find this '
                  'difference, we subtract eight thousand four hundred twenty-six from nine thousand one hundred '
                  'fifteen. In the ones place, five minus six requires borrowing one ten: fifteen minus six equals '
                  'nine ones. In the tens place, zero tens minus two tens requires unbundling one hundred: ten tens '
                  'minus two tens equals eight tens. In the hundreds place, zero hundreds minus four hundreds requires '
                  'unbundling one thousand: ten hundreds minus four hundreds equals six hundreds. Finally, eight '
                  'thousands minus eight thousands leaves zero! The difference is exactly six hundred eighty-nine '
                  'visitors. Comparing seasonal park attendance allows forestry authorities to allocate security '
                  'rangers, schedule safari jeeps responsibly, manage eco-tourism facilities sustainably, and ensure '
                  'visitors experience nature safely without disturbing resting wild fauna across protected sanctums.',
        'title': 'Park Attendance Records'},
    {   'checkpoints': [   {   'ans': 2,
                               'exp': '3,450 + 2,870 + 1,680 = 8,000 bottles.',
                               'options': ['7,800 bottles', '7,900 bottles', '8,000 bottles', '8,100 bottles'],
                               'q': 'What is 3,450 + 2,870 + 1,680 juice bottles combined?'},
                           {   'ans': 1,
                               'exp': '4,560 + 2,340 = 6,900 vehicles.',
                               'options': ['6,800', '6,900', '7,000', '7,100'],
                               'q': 'A district registers 4,560 jeeps and 2,340 tractors. How many vehicles are these '
                                    'two types together?'}],
        'id': 11,
        'section': 'Industrial Manufacturing & Fleet Registrations',
        'speech': 'Multi-digit addition and subtraction govern practical operations across modern manufacturing plants '
                  'and municipal transportation departments. Consider a cooperative fruit beverage factory producing '
                  'pure bottled juices from regional harvests. In a single working shift, the bottling line produces '
                  'three thousand four hundred fifty bottles of pineapple juice, two thousand eight hundred seventy '
                  'bottles of guava nectar, and one thousand six hundred eighty bottles of passion fruit juice. What '
                  'is the total beverage production? Aligning these three quantities in vertical columns, we add the '
                  'ones: zero plus zero plus zero gives zero ones. In the tens column, five plus seven plus eight '
                  'equals twenty tens, writing zero and carrying two hundreds! In the hundreds column, two plus four '
                  'plus eight plus six equals twenty hundreds, writing zero and carrying two thousands! In the '
                  'thousands column, two plus three plus two plus one equals eight thousands, yielding exactly eight '
                  'thousand bottles produced! In another civic department, transport officials audit registered motor '
                  'vehicles across a district: four thousand five hundred sixty jeeps, two thousand three hundred '
                  'forty tractors, and one thousand ninety taxis. Adding and subtracting vehicle registries enables '
                  'municipal planners to assess fuel logistics, design road expansions, and optimize public '
                  'transportation routes effectively.',
        'title': 'Production Vehicle Counts'},
    {   'checkpoints': [   {   'ans': 0,
                               'exp': '(5 × 500 = 2500) + (3 × 100 = 300) + (1 × 50 = 50) = ₹2,850.',
                               'options': [   '5 × ₹500 + 3 × ₹100 + 1 × ₹50',
                                              '4 × ₹500 + 8 × ₹100 + 1 × ₹50',
                                              '6 × ₹500',
                                              '2 × ₹500 + 18 × ₹100'],
                               'q': 'Which combination of currency notes equals exactly ₹2,850?'},
                           {   'ans': 2,
                               'exp': '(2 × 500 = 1000) + (4 × 100 = 400) + (2 × 10 = 20) = ₹1,420.',
                               'options': ['₹1,240', '₹1,320', '₹1,420', '₹1,500'],
                               'q': 'If a student deposits two ₹500 notes, four ₹100 notes, and two ₹10 notes, what is '
                                    'the total deposit?'}],
        'id': 12,
        'section': 'Financial Denominations & Cash Breakdown',
        'speech': 'During a vibrant school community mela, student organizers manage financial accounts by depositing '
                  'collected stall earnings into the local school savings bank. Filling out an authentic bank deposit '
                  'slip requires translating a grand total into specific currency note denominations: '
                  'five-hundred-rupee notes, one-hundred-rupee notes, fifty-rupee notes, ten-rupee notes, and coins. '
                  'Suppose an industrious young depositor visits the bank counter with an official cash total of two '
                  'thousand eight hundred fifty rupees. How is this amount broken down accurately on the deposit slip? '
                  'Five five-hundred-rupee notes equal two thousand five hundred rupees. Three one-hundred-rupee notes '
                  'equal three hundred rupees, bringing our subtotal to two thousand eight hundred. Finally, one '
                  'fifty-rupee note supplies the remaining fifty rupees! On the official deposit slip table, the young '
                  'saver writes: five under five-hundreds, three under hundreds, one under fifties, and verifies that '
                  'the sum of all individual products equals two thousand eight hundred fifty rupees. Another '
                  'organized student depositor deposits one thousand four hundred twenty rupees using two '
                  'five-hundred-rupee notes, four one-hundred-rupee notes, and two ten-rupee notes. Financial '
                  'mathematics bridges abstract place-value columns with physical currency banknotes, instilling '
                  'meticulous accounting accuracy, verifying transaction integrity, and preparing young minds for '
                  'responsible personal financial management throughout adulthood.',
        'title': 'Bank Deposit Slips'},
    {   'checkpoints': [   {   'ans': 2,
                               'exp': '4,786 + 3,847 = 8,633.',
                               'options': ['8,533', '8,623', '8,633', '8,733'],
                               'q': 'What is 4,786 + 3,847 calculated column by column?'},
                           {   'ans': 1,
                               'exp': '7,215 - 3,648 = 3,567.',
                               'options': ['3,557', '3,567', '3,667', '4,567'],
                               'q': 'What is 7,215 - 3,648 calculated using standard column subtraction?'}],
        'id': 13,
        'section': 'Standard Multi-Digit Operational Algorithms',
        'speech': 'Mastering standard column addition and subtraction across four-digit numbers builds speed, '
                  'structural accuracy, and computational confidence. Let us practice formal column calculation with '
                  'multiple regroupings. Consider the addition problem: four thousand seven hundred eighty-six plus '
                  'three thousand eight hundred forty-seven. Aligning columns meticulously, we begin with the ones: '
                  'six plus seven equals thirteen, writing three and carrying one ten. In the tens column, one plus '
                  'eight plus four equals thirteen tens, writing three and carrying one hundred. In the hundreds '
                  'column, one plus seven plus eight equals sixteen hundreds, writing six and carrying one thousand. '
                  'Finally, in the thousands column, one plus four plus three equals eight thousands, producing eight '
                  'thousand six hundred thirty-three! Now let us practice four-digit subtraction: seven thousand two '
                  'hundred fifteen minus three thousand six hundred forty-eight. In the ones place, fifteen minus '
                  'eight equals seven. In the tens place, zero tens minus four tens requires borrowing, giving ten '
                  'minus four equaling six. In the hundreds place, one hundred minus six hundreds requires borrowing '
                  'from thousands, giving eleven minus six equaling five. Finally, six thousands minus three thousands '
                  'leaves three, yielding three thousand five hundred sixty-seven! Daily practice of standard '
                  'algorithms cements operational fluency across mathematics.',
        'title': 'Four Digit Columns'},
    {   'checkpoints': [   {   'ans': 0,
                               'exp': '546 - 100 = 446; 446 + 1 = 447.',
                               'options': [   'Subtract 100 then add 1 (546 - 100 + 1 = 447)',
                                              'Subtract 90 then subtract 9',
                                              'Add 100 then subtract 1',
                                              'Divide by 99'],
                               'q': 'How can you mentally compute 546 - 99 using compensation?'},
                           {   'ans': 1,
                               'exp': '372 + 100 = 472; 472 - 1 = 471.',
                               'options': ['461', '471', '472', '481'],
                               'q': 'What is 372 + 99 calculated mentally?'}],
        'id': 14,
        'section': 'Compensation Tricks & Near-Hundred Adjustments',
        'speech': 'While standard paper algorithms provide dependable precision, ingenious mental math shortcuts allow '
                  'us to calculate large sums and differences in mere seconds without using pencil and paper! The most '
                  'celebrated mental strategy is compensation, which utilizes friendly landmark numbers like one '
                  'hundred or one thousand. Suppose we must calculate five hundred forty-six minus ninety-nine. '
                  'Instead of tedious column borrowing, notice that ninety-nine is just one less than one hundred! We '
                  'subtract one hundred first: five hundred forty-six minus one hundred equals four hundred forty-six. '
                  'Since we subtracted one unit too many, we simply add one back: four hundred forty-six plus one '
                  'equals four hundred forty-seven! What if we need to add ninety-nine instead? To calculate three '
                  'hundred seventy-two plus ninety-nine, add one hundred first to reach four hundred seventy-two, then '
                  'subtract one to obtain four hundred seventy-one! The same compensation logic applies to nine '
                  'hundred ninety-nine: to subtract nine hundred ninety-nine, subtract one thousand and add one! '
                  'Similarly, to add nine hundred ninety-nine, add one thousand and subtract one! Mastering these '
                  'practical compensation methods transforms cumbersome multi-digit arithmetic into joyful mental '
                  'agility, proving that understanding number relationships makes computation effortless, fast, and '
                  'remarkably satisfying across everyday real-world problem-solving situations.',
        'title': 'Mental Math Strategies'},
    {   'checkpoints': [   {   'ans': 2,
                               'exp': 'Both expressions share 2,450. Since 320 > 310, the left side is strictly '
                                      'greater (>).',
                               'options': ['<', '=', '>', 'Cannot tell'],
                               'q': 'Which symbol correctly compares 2,450 + 320 ___ 2,450 + 310 without adding?'},
                           {   'ans': 0,
                               'exp': 'Subtracting a smaller number (200 < 250) leaves a larger result: 4,300 > 4,250.',
                               'options': [   '4,500 - 200 is larger',
                                              '4,500 - 250 is larger',
                                              'Both are equal',
                                              'Cannot be compared'],
                               'q': 'Which expression is larger: (4,500 - 200) or (4,500 - 250)?'}],
        'id': 15,
        'section': 'Expression Comparison & Relational Thinking',
        'speech': 'Expert mathematicians frequently compare the values of two arithmetic expressions without '
                  'calculating their exact sums or differences. This profound skill, known as relational thinking, '
                  'relies on comparing corresponding terms directly. For example, consider comparing the expression '
                  'two thousand four hundred fifty plus three hundred twenty against two thousand four hundred fifty '
                  'plus three hundred ten. Notice that both expressions contain the common term two thousand four '
                  'hundred fifty! Because three hundred twenty is greater than three hundred ten, the first expression '
                  'must be strictly greater than the second, allowing us to place the greater-than symbol immediately '
                  'without performing addition! What about comparing differences? Consider four thousand five hundred '
                  'minus two hundred against four thousand five hundred minus two hundred fifty. When subtracting from '
                  'identical totals, removing a smaller amount leaves a noticeably larger remainder! Since two hundred '
                  'is clearly smaller than two hundred fifty, subtracting two hundred leaves a larger balance behind, '
                  'making four thousand five hundred minus two hundred greater! This logical relational comparison '
                  'replaces brute-force calculation with keen structural deduction, enabling observant young scholars '
                  'to analyze algebraic inequalities, verify commercial invoice estimates, and solve mathematical '
                  'reasoning puzzles with speed, elegance, and profound confidence across diverse academic '
                  'disciplines.',
        'title': 'Inequality Logic Puzzles'},
    {   'checkpoints': [   {   'ans': 2,
                               'exp': 'Even - Odd = Odd, and Odd - Even = Odd. Differing parity always produces an odd '
                                      'difference.',
                               'options': [   'When both are even',
                                              'When both are odd',
                                              'When one is even and the other is odd',
                                              'Never'],
                               'q': 'When is the difference between two numbers an ODD number?'},
                           {   'ans': 1,
                               'exp': 'Odd digits: 1, 3, 5, 7, 9 (5 digits). Even digits: 2, 4, 6, 8 (4 digits).',
                               'options': ['4 odd, 5 even', '5 odd, 4 even', '3 odd, 6 even', '5 odd, 5 even'],
                               'q': 'How many odd digits and even digits are there in the numbers 1 through 9?'}],
        'id': 16,
        'section': 'Grid Parity Puzzles & Combinatorial Logic',
        'speech': 'We conclude our chapter with an ingenious combinatorial logic puzzle known as the neighbouring '
                  'square grid! In a three-by-three grid containing nine square cells, a mathematician must place the '
                  'digits one through nine, using each digit exactly once, such that the difference between any two '
                  'adjacent, connected squares is always an odd number. Let us analyze the parity rules governing '
                  'differences! The difference between two numbers is odd if and only if one number is even and the '
                  'other number is odd: an even minus an odd, or an odd minus an even, always produces an odd '
                  'difference. Conversely, the difference between two even numbers, or between two odd numbers, is '
                  'always an even number! Therefore, for every adjacent pair of squares to have an odd difference, '
                  'every even square must be bordered exclusively by odd squares, and every odd square must be '
                  'bordered exclusively by even squares! This produces an alternating chessboard pattern. Counting our '
                  'available digits, from one to nine there are five odd numbers (one, three, five, seven, nine) and '
                  'four even numbers (two, four, six, eight). Placing the five odd digits on the corners and center, '
                  'and the four even digits on the edges, solves the puzzle flawlessly!',
        'title': 'Neighbouring Square Grids'},
    {   'id': 17,
        'quizzes': [   {   'ans': 0,
                           'exp': '1 + 1 = 2, and 1 + 2 = 3.',
                           'hint': 'The second player adds either 1 or 2 to the running total 1.',
                           'options': ['2 or 3', '3 or 4', '4 or 5', '0 or 1'],
                           'q': 'In the 2-player Nim Game to 10 starting at 0 (adding 1 or 2), if the first player '
                                'says 1, what numbers can the second player choose?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>The running "
                                  "total is currently 1.</li><li class='mb-2 text-slate-700 leading-relaxed'>The rules "
                                  "allow adding either 1 or 2.</li><li class='mb-2 text-slate-700 leading-relaxed'>If "
                                  "the second player adds 1: 1 + 1 = 2.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>If the second player adds 2: 1 + 2 = 3.</li></ol></div><div "
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Each turn advances "
                                  'the running total by 1 or 2.</div></div>'},
                       {   'ans': 1,
                           'exp': 'From 7, opponent can only reach 8 or 9; you immediately reach 10 on the next move.',
                           'hint': 'From 7, the opponent can only say 8 or 9.',
                           'options': ['9', '7', '8', '6'],
                           'q': 'To guarantee reaching the winning number 10, which key target number should you '
                                'secure on your turn before?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Target is 10. "
                                  'To prevent opponent from reaching 10, determine the threshold before 10.</li><li '
                                  "class='mb-2 text-slate-700 leading-relaxed'>If you claim 7, the opponent can only "
                                  "add 1 (reaching 8) or 2 (reaching 9).</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>From 8, you add 2 to reach 10! From 9, you add 1 to reach "
                                  "10!</li><li class='mb-2 text-slate-700 leading-relaxed'>Therefore, securing 7 "
                                  "guarantees a win.</li></ol></div><div class='bg-amber-50 border-l-4 "
                                  'border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> Backward induction reveals winning "
                                  'milestones: 10, 7, 4, 1.</div></div>'},
                       {   'ans': 0,
                           'exp': '10 - 3 = 7; 7 - 3 = 4; 4 - 3 = 1.',
                           'hint': 'Subtract 3 from 10 repeatedly.',
                           'options': ['1, 4, 7, 10', '2, 4, 6, 8, 10', '3, 6, 9', '1, 3, 5, 7, 9'],
                           'q': 'What is the complete sequence of winning milestone numbers for Nim Game to 10?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Working "
                                  "backwards from target 10: 10 - 3 = 7.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>From 7: 7 - 3 = 4.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>From 4: 4 - 3 = 1.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>The first player who says 1 can secure 4, then 7, and finally "
                                  "10!</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'Controlling milestones differing by (max move + 1 = 3) guarantees '
                                  'victory.</div></div>'},
                       {   'ans': 0,
                           'exp': '21 ÷ 3 = 7 with remainder 0. The second player controls multiples of 3!',
                           'hint': 'Find the remainder when 21 is divided by (1 + 2 = 3).',
                           'options': ['0', '1', '2', '3'],
                           'q': 'If extending the Nim addition game to target 21 (adding 1 or 2), what is the first '
                                'winning number?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Step size is 1 "
                                  "or 2, so the cycle period is 1 + 2 = 3.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Dividing target by cycle length: 21 ÷ 3 = 7 remainder 0.</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>Because 21 is a multiple of 3, the "
                                  "second player can always complete a sum of 3.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Winning targets for player 2 are: 3, 6, 9, 12, 15, 18, "
                                  "21.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'When the target is a multiple of 3, the second player has the winning '
                                  'strategy.</div></div>'},
                       {   'ans': 1,
                           'exp': 'The maximum entry is 12 + 12 = 24.',
                           'hint': 'Add the largest row header and largest column header.',
                           'options': ['22', '24', '25', '26'],
                           'q': 'In a 13 × 13 addition chart (numbers 0 to 12 along rows and columns), what is the '
                                'maximum sum?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Row headers "
                                  "range from 0 to 12.</li><li class='mb-2 text-slate-700 leading-relaxed'>Column "
                                  "headers range from 0 to 12.</li><li class='mb-2 text-slate-700 leading-relaxed'>The "
                                  'largest cell is at row 12, column 12: 12 + 12 = 24.</li></ol></div><div '
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> The extreme "
                                  'bottom-right cell holds the maximum sum.</div></div>'},
                       {   'ans': 2,
                           'exp': 'Anti-diagonals (slanted /) connect cells where (r + 1) + (c - 1) = r + c.',
                           'hint': 'If row increases by 1 and column decreases by 1, the sum remains constant.',
                           'options': [   'Horizontal rows',
                                          'Vertical columns',
                                          'Top-right to bottom-left diagonals',
                                          'Top-left to bottom-right diagonals'],
                           'q': 'In the addition chart, along which lines do identical sums always appear?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Consider cells "
                                  "with sum 5: (0,5), (1,4), (2,3), (3,2), (4,1), (5,0).</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>Moving down 1 row increases the row by 1.</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>Moving left 1 column decreases the "
                                  "column by 1.</li><li class='mb-2 text-slate-700 leading-relaxed'>The net change in "
                                  'sum is +1 - 1 = 0, creating a top-right to bottom-left diagonal of identical '
                                  "values.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'Anti-diagonals in addition tables represent constant-sum contours.</div></div>'},
                       {   'ans': 2,
                           'exp': 'The pairs are (0,9), (1,8), (2,7), (3,6), (4,5), (5,4), (6,3), (7,2), (8,1), (9,0) '
                                  '= 10 times.',
                           'hint': 'Count pairs (a, b) such that a + b = 9 where 0 ≤ a, b ≤ 12.',
                           'options': ['8 times', '9 times', '10 times', '11 times'],
                           'q': 'How many times does the number 9 appear in the 13 × 13 addition table (0 to 12)?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Any sum 9 is "
                                  "formed by a + b = 9.</li><li class='mb-2 text-slate-700 leading-relaxed'>Possible "
                                  "values of a are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>For each value of a, b = 9 - a is between 0 and 9 (which is ≤ "
                                  "12).</li><li class='mb-2 text-slate-700 leading-relaxed'>Counting from a = 0 to a = "
                                  "9 gives exactly 10 pairs.</li></ol></div><div class='bg-amber-50 border-l-4 "
                                  'border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> For any sum S ≤ max header, S "
                                  'appears S + 1 times in a 0-indexed table.</div></div>'},
                       {   'ans': 2,
                           'exp': '9 + 10 + 11 = 30.',
                           'hint': 'The numbers are 9, 10, and 11.',
                           'options': ['20', '25', '30', '35'],
                           'q': 'A 3 × 3 window frame placed over an addition grid has center cell 10. What is the sum '
                                'of its horizontal row (9 + 10 + 11)?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Row contains: "
                                  "9, 10, 11.</li><li class='mb-2 text-slate-700 leading-relaxed'>Notice 9 = 10 - 1 "
                                  "and 11 = 10 + 1.</li><li class='mb-2 text-slate-700 leading-relaxed'>(10 - 1) + 10 "
                                  "+ (10 + 1) = 3 × 10 = 30.</li></ol></div><div class='bg-amber-50 border-l-4 "
                                  'border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> Symmetrical entries balance around "
                                  'the central centroid.</div></div>'},
                       {   'ans': 1,
                           'exp': '9 cells × 10 = 90.',
                           'hint': 'Multiply the central number by the total number of cells (9).',
                           'options': ['80', '90', '100', '110'],
                           'q': 'What is the total sum of all 9 numbers inside a 3 × 3 window frame with center number '
                                '10?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>In an addition "
                                  'table, each of the 4 symmetric pairs around center C sums to 2 × C.</li><li '
                                  "class='mb-2 text-slate-700 leading-relaxed'>4 pairs × (2 × 10) = 80.</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>Adding the central cell: 80 + 10 = "
                                  "90.</li><li class='mb-2 text-slate-700 leading-relaxed'>Alternatively, average of "
                                  "the 9 cells is 10: 9 × 10 = 90.</li></ol></div><div class='bg-amber-50 border-l-4 "
                                  'border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> Total sum of a 3 × 3 window on an "
                                  'addition table is always 9 × Center.</div></div>'},
                       {   'ans': 1,
                           'exp': '8 + 12 = 20 = 2 × 10.',
                           'hint': 'The two cells form a diagonal passing through center 10.',
                           'options': ['18', '20', '22', '24'],
                           'q': 'In a 3 × 3 addition grid window with center 10, the top-left cell is 8 and '
                                'bottom-right is 12. What is their sum?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Top-left cell "
                                  "= 8.</li><li class='mb-2 text-slate-700 leading-relaxed'>Bottom-right cell = "
                                  "12.</li><li class='mb-2 text-slate-700 leading-relaxed'>8 + 12 = 20.</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>Notice that 20 = 2 × 10 (twice the "
                                  "central value).</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 "
                                  "p-3 rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key "
                                  'Takeaway:</strong> Every opposite pair passing through the center sums to 2 × '
                                  'Center.</div></div>'}],
        'section': 'Nim Strategies & Addition Chart Puzzles',
        'speech': '',
        'title': 'Challenge 1'},
    {   'id': 18,
        'quizzes': [   {   'ans': 1,
                           'exp': '27 + 72 = 99.',
                           'hint': 'Add 27 + 72.',
                           'options': ['89', '99', '109', '119'],
                           'q': 'Take the 2-digit number 27, reverse its digits to 72, and add them. What is the '
                                'result?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Original "
                                  "number = 27.</li><li class='mb-2 text-slate-700 leading-relaxed'>Reversed digits = "
                                  "72.</li><li class='mb-2 text-slate-700 leading-relaxed'>Units: 7 + 2 = 9.</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>Tens: 2 + 7 = 9.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>27 + 72 = 99.</li></ol></div><div "
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Reversing and adding "
                                  'a 2-digit number always yields a multiple of 11.</div></div>'},
                       {   'ans': 0,
                           'exp': '(10a + b) + (10b + a) = 11a + 11b = 11(a + b).',
                           'hint': 'Write the place values: original is 10a + b, reverse is 10b + a.',
                           'options': [   'Because (10a + b) + (10b + a) = 11(a + b)',
                                          'Because 10 + 1 = 11',
                                          'Because numbers are even',
                                          'Because 9 + 2 = 11'],
                           'q': 'For any 2-digit number with tens digit a and ones digit b, why is the sum of the '
                                'number and its reverse always a multiple of 11?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Original "
                                  "2-digit number = 10 × a + b.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Reversed 2-digit number = 10 × b + a.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>Adding both: (10a + a) + (b + 10b) = 11a + "
                                  "11b.</li><li class='mb-2 text-slate-700 leading-relaxed'>Factoring out 11: 11 × (a "
                                  "+ b).</li><li class='mb-2 text-slate-700 leading-relaxed'>Hence, the result is "
                                  "always an exact multiple of 11!</li></ol></div><div class='bg-amber-50 border-l-4 "
                                  'border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> Algebraic structure proves why "
                                  'reverse-and-add patterns hold universally.</div></div>'},
                       {   'ans': 3,
                           'exp': '14 + 41 = 55; 23 + 32 = 55; 32 + 23 = 55. All yield 55!',
                           'hint': 'Check if the sum of the digits (a + b) equals 5.',
                           'options': ['14', '23', '32', 'All of these'],
                           'q': 'Which of the following 2-digit numbers produces 55 when added to its reverse?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>We need 11 × "
                                  "(a + b) = 55, which means a + b = 5.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>For 14: 1 + 4 = 5 (14 + 41 = 55).</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>For 23: 2 + 3 = 5 (23 + 32 = 55).</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>For 32: 3 + 2 = 5 (32 + 23 = "
                                  "55).</li><li class='mb-2 text-slate-700 leading-relaxed'>All of these numbers "
                                  "satisfy the condition!</li></ol></div><div class='bg-amber-50 border-l-4 "
                                  'border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> Any 2-digit number whose digits sum "
                                  'to 5 produces 55 upon reversal and addition.</div></div>'},
                       {   'ans': 2,
                           'exp': '56 + 65 = 121 (since 5 + 6 = 11 ≥ 10).',
                           'hint': 'A 3-digit sum requires digit sum (a + b) ≥ 10.',
                           'options': ['25', '34', '56', '43'],
                           'q': 'Which 2-digit number yields a 3-digit sum when added to its reverse?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>To reach 100 "
                                  "or greater, 11 × (a + b) must exceed 99.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>This requires a + b ≥ 10.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Check options:</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>25: 2 + 5 = 7 (25 + 52 = 77).</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>34: 3 + 4 = 7 (34 + 43 = 77).</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>56: 5 + 6 = 11 (56 + 65 = 121).</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>121 is a 3-digit palindromic number!</li></ol></div><div "
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> When digits sum to 10 "
                                  'or more, the reversed sum enters the hundreds place.</div></div>'},
                       {   'ans': 1,
                           'exp': '11 × 12 = 132.',
                           'hint': '48 + 84 = 11 × (4 + 8).',
                           'options': ['122', '132', '142', '152'],
                           'q': 'What is the sum when 48 is added to its reverse 84?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Original: 48, "
                                  "Reversed: 84.</li><li class='mb-2 text-slate-700 leading-relaxed'>Digit sum = 4 + 8 "
                                  "= 12.</li><li class='mb-2 text-slate-700 leading-relaxed'>Reversed sum = 11 × 12 = "
                                  "132.</li><li class='mb-2 text-slate-700 leading-relaxed'>Direct addition: 48 + 84 = "
                                  "132.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'Multiples of 11: 11 × 12 = 132.</div></div>'},
                       {   'ans': 1,
                           'exp': '6,049 + 3,054 = 9,103.',
                           'hint': 'Add 6,049 + 3,054 using place value columns.',
                           'options': ['9,093', '9,103', '9,113', '9,203'],
                           'q': 'Karnataka shelters 6,049 wild elephants and Kerala shelters 3,054 elephants. What is '
                                'their combined elephant population?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Ones: 9 + 4 = "
                                  "13 (write 3, carry 1).</li><li class='mb-2 text-slate-700 leading-relaxed'>Tens: 1 "
                                  "(carry) + 4 + 5 = 10 (write 0, carry 1).</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Hundreds: 1 (carry) + 0 + 0 = 1.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>Thousands: 6 + 3 = 9.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>Total = 9,103 elephants.</li></ol></div><div "
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Meticulous column "
                                  'carrying yields the exact combined population.</div></div>'},
                       {   'ans': 1,
                           'exp': '785 - 563 = 222.',
                           'hint': 'Subtract 563 from 785.',
                           'options': ['212', '222', '232', '242'],
                           'q': 'Madhya Pradesh records 785 tigers while Karnataka records 563 tigers. How many more '
                                'tigers reside in Madhya Pradesh?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Ones: 5 - 3 = "
                                  "2.</li><li class='mb-2 text-slate-700 leading-relaxed'>Tens: 8 - 6 = 2.</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>Hundreds: 7 - 5 = 2.</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>Difference = 222 "
                                  "tigers.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'Standard subtraction without borrowing yields 222.</div></div>'},
                       {   'ans': 2,
                           'exp': '444 + 560 + 785 = 1,789.',
                           'hint': 'Add 444 + 560 + 785.',
                           'options': ['1,689', '1,779', '1,789', '1,799'],
                           'q': 'According to census reports, Maharashtra has 444 tigers, Uttarakhand has 560 tigers, '
                                'and Madhya Pradesh has 785 tigers. What is the total tiger count in these three '
                                'states?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Add the first "
                                  "two: 444 + 560 = 1,004.</li><li class='mb-2 text-slate-700 leading-relaxed'>Add the "
                                  "third: 1,004 + 785 = 1,789.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Check column addition: Ones 4+0+5=9; Tens 4+6+8=18 (write 8, carry "
                                  "1); Hundreds 1+4+5+7=17.</li><li class='mb-2 text-slate-700 leading-relaxed'>Total "
                                  "= 1,789 tigers.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 "
                                  "p-3 rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key "
                                  'Takeaway:</strong> Multi-addend addition requires carrying across tens and '
                                  'hundreds.</div></div>'},
                       {   'ans': 1,
                           'exp': '1,842 + 2,365 = 4,207.',
                           'hint': 'Add 1,842 + 2,365.',
                           'options': ['4,107', '4,207', '4,217', '4,307'],
                           'q': 'State A reports 1,842 leopards and State B reports 2,365 leopards. What is their '
                                'combined leopard population?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Ones: 2 + 5 = "
                                  "7.</li><li class='mb-2 text-slate-700 leading-relaxed'>Tens: 4 + 6 = 10 (write 0, "
                                  "carry 1).</li><li class='mb-2 text-slate-700 leading-relaxed'>Hundreds: 1 (carry) + "
                                  "8 + 3 = 12 (write 2, carry 1).</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Thousands: 1 (carry) + 1 + 2 = 4.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>Total = 4,207 leopards.</li></ol></div><div "
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Double carrying "
                                  'across tens and hundreds yields 4,207.</div></div>'},
                       {   'ans': 2,
                           'exp': '9 + 4 = 13 ones carries 1 ten; 1 + 4 + 5 = 10 tens bundles into 1 hundred.',
                           'hint': 'Look at the tens place sum: 4 tens + 5 tens plus 1 carry from ones.',
                           'options': [   'It is a typo',
                                          'A carry-over of 1 ten came from the ones',
                                          'The sum of tens (1 carry + 4 + 5 = 10) generated a carried hundred',
                                          'Addends always round up'],
                           'q': 'When adding 6,049 + 3,054, why does the hundreds place contain a 1 although both '
                                'addends have 0 in the hundreds place?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>In the ones "
                                  "column: 9 + 4 = 13 ones = 1 ten and 3 ones.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>The 1 ten carries to the tens column.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>In the tens column: 1 (carry) + 4 + 5 = 10 "
                                  "tens.</li><li class='mb-2 text-slate-700 leading-relaxed'>10 tens bundle together "
                                  "into exactly 1 hundred and 0 tens.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>This 1 hundred is placed in the hundreds "
                                  "column!</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'Place value bundling cascades carries smoothly into adjacent columns.</div></div>'}],
        'section': 'Reverse Additions & Wildlife Population Math',
        'speech': '',
        'title': 'Challenge 2'},
    {   'id': 19,
        'quizzes': [   {   'ans': 2,
                           'exp': '5,719 - 1,754 = 3,965.',
                           'hint': 'Subtract 1,754 from 5,719.',
                           'options': ['3,865', '3,955', '3,965', '4,065'],
                           'q': 'Assam shelters 5,719 wild elephants while Meghalaya shelters 1,754 elephants. How '
                                'many more elephants inhabit Assam?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Ones: 9 - 4 = "
                                  "5.</li><li class='mb-2 text-slate-700 leading-relaxed'>Tens: 1 - 5 requires "
                                  'unbundling 1 hundred from 7 hundreds (leaving 6 hundreds). 11 - 5 = 6 tens.</li><li '
                                  "class='mb-2 text-slate-700 leading-relaxed'>Hundreds: 6 - 7 requires unbundling 1 "
                                  'thousand from 5 thousands (leaving 4 thousands). 16 - 7 = 9 hundreds.</li><li '
                                  "class='mb-2 text-slate-700 leading-relaxed'>Thousands: 4 - 1 = 3 thousands.</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>Difference = 3,965 "
                                  "elephants.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'Successive unbundling ensures accurate multi-digit subtraction.</div></div>'},
                       {   'ans': 1,
                           'exp': '1 hundred = 10 tens.',
                           'hint': 'How many tens are in one hundred?',
                           'options': ['1 ten', '10 tens', '100 tens', '5 tens'],
                           'q': 'In subtraction, what does unbundling 1 hundred provide to the tens column?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>The base-ten "
                                  "number system is built on powers of 10.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>1 hundred is composed of 10 tens.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>Unbundling 1 hundred adds 10 to the tens "
                                  "digit.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  '1 Hundred = 10 Tens in our base-ten positional system.</div></div>'},
                       {   'ans': 1,
                           'exp': '9,115 - 8,426 = 689.',
                           'hint': 'Subtract 8,426 from 9,115.',
                           'options': ['679', '689', '699', '711'],
                           'q': 'In 2022, Kaziranga National Park welcomed 9,115 visitors, compared to 8,426 visitors '
                                'in 2021. What was the increase in visitors?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Ones: 5 - 6 "
                                  "(unbundle 1 ten -> 0 tens left; 15 - 6 = 9).</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Tens: 0 - 2 (unbundle 1 hundred -> 0 hundreds left; 10 - 2 = "
                                  "8).</li><li class='mb-2 text-slate-700 leading-relaxed'>Hundreds: 0 - 4 (unbundle 1 "
                                  "thousand -> 8 thousands left; 10 - 4 = 6).</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Thousands: 8 - 8 = 0.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Increase = 689 visitors.</li></ol></div><div class='bg-amber-50 "
                                  'border-l-4 border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> Triple unbundling across ones, tens, "
                                  'and hundreds yields 689.</div></div>'},
                       {   'ans': 2,
                           'exp': '4,320 + 3,895 = 8,215.',
                           'hint': 'Add 4,320 + 3,895.',
                           'options': ['8,115', '8,205', '8,215', '8,315'],
                           'q': 'A vehicle assembly plant produced 4,320 electric scooters in March and 3,895 in '
                                'April. How many scooters were produced altogether?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Ones: 0 + 5 = "
                                  "5.</li><li class='mb-2 text-slate-700 leading-relaxed'>Tens: 2 + 9 = 11 (write 1, "
                                  "carry 1).</li><li class='mb-2 text-slate-700 leading-relaxed'>Hundreds: 1 (carry) + "
                                  "3 + 8 = 12 (write 2, carry 1).</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Thousands: 1 (carry) + 4 + 3 = 8.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>Total = 8,215 scooters.</li></ol></div><div "
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Carrying across tens "
                                  'and hundreds produces 8,215.</div></div>'},
                       {   'ans': 1,
                           'exp': '4,320 - 3,895 = 425.',
                           'hint': 'Subtract 3,895 from 4,320.',
                           'options': ['415', '425', '435', '525'],
                           'q': 'How many more electric scooters were produced in March than in April (4,320 - 3,895)?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Ones: 0 - 5 "
                                  "(unbundle 1 ten from 2 tens -> 1 ten left; 10 - 5 = 5).</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>Tens: 1 - 9 (unbundle 1 hundred from 3 hundreds -> "
                                  "2 hundreds left; 11 - 9 = 2).</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Hundreds: 2 - 8 (unbundle 1 thousand from 4 thousands -> 3 "
                                  "thousands left; 12 - 8 = 4).</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Thousands: 3 - 3 = 0.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Difference = 425 scooters.</li></ol></div><div class='bg-amber-50 "
                                  'border-l-4 border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> Difference calculation verifies "
                                  'month-over-month factory trends.</div></div>'},
                       {   'ans': 1,
                           'exp': '3,450 + 2,870 + 1,680 = 8,000 crates.',
                           'hint': 'Add 3,450 + 2,870 + 1,680.',
                           'options': ['7,900', '8,000', '8,100', '8,200'],
                           'q': 'A juice distribution center shipped 3,450 mango crates, 2,870 apple crates, and 1,680 '
                                'orange crates. What was the total crate count?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Ones: 0 + 0 + "
                                  "0 = 0.</li><li class='mb-2 text-slate-700 leading-relaxed'>Tens: 5 + 7 + 8 = 20 "
                                  "(write 0, carry 2).</li><li class='mb-2 text-slate-700 leading-relaxed'>Hundreds: 2 "
                                  "(carry) + 4 + 8 + 6 = 20 (write 0, carry 2).</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Thousands: 2 (carry) + 3 + 2 + 1 = 8.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>Total = 8,000 crates.</li></ol></div><div "
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Carries of 2 across "
                                  'consecutive columns yield an even 8,000.</div></div>'},
                       {   'ans': 1,
                           'exp': '7,000 - 3,456 = 3,544.',
                           'hint': 'Unbundle 1 thousand into 9 hundreds, 9 tens, and 10 ones.',
                           'options': ['3,534', '3,544', '3,644', '4,544'],
                           'q': 'What is the difference when subtracting across zeros: 7,000 - 3,456?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>7,000 = 6 "
                                  "thousands + 9 hundreds + 9 tens + 10 ones.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Ones: 10 - 6 = 4.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Tens: 9 - 5 = 4.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Hundreds: 9 - 4 = 5.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Thousands: 6 - 3 = 3.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Difference = 3,544.</li></ol></div><div class='bg-amber-50 "
                                  'border-l-4 border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> Subtracting across multiple zeros "
                                  'converts intermediate zeros into 9s.</div></div>'},
                       {   'ans': 0,
                           'exp': '3,235 + 2,185 = 5,420.',
                           'hint': 'Difference + Subtrahend = Minuend.',
                           'options': [   '3,235 + 2,185 = 5,420',
                                          '5,420 + 2,185 = 7,605',
                                          '3,235 + 5,420 = 8,655',
                                          '5,420 - 3,235 = 2,185'],
                           'q': 'If 5,420 - 2,185 = 3,235, which addition equation verifies this subtraction?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>In "
                                  "subtraction: Minuend - Subtrahend = Difference.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Inverse operation states: Difference + Subtrahend = "
                                  "Minuend.</li><li class='mb-2 text-slate-700 leading-relaxed'>3,235 + 2,185 = "
                                  "5,420.</li><li class='mb-2 text-slate-700 leading-relaxed'>Adding the difference to "
                                  'the subtracted amount restores the original total.</li></ol></div><div '
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Addition serves as "
                                  'the universal verification tool for subtraction.</div></div>'},
                       {   'ans': 1,
                           'exp': '6,240 - 4,580 = 1,660.',
                           'hint': 'Subtract 4,580 from 6,240.',
                           'options': ['1,650', '1,660', '1,740', '1,760'],
                           'q': 'A wildlife sanctuary counted 6,240 migratory birds in December and 4,580 in February. '
                                'How many birds departed during this period?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Ones: 0 - 0 = "
                                  "0.</li><li class='mb-2 text-slate-700 leading-relaxed'>Tens: 4 - 8 (unbundle 1 "
                                  "hundred -> 1 hundred left; 14 - 8 = 6).</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Hundreds: 1 - 5 (unbundle 1 thousand -> 5 thousands left; 11 - 5 = "
                                  "6).</li><li class='mb-2 text-slate-700 leading-relaxed'>Thousands: 5 - 4 = "
                                  "1.</li><li class='mb-2 text-slate-700 leading-relaxed'>Departed birds = "
                                  "1,660.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'Accurate subtraction quantifies seasonal bird migration.</div></div>'},
                       {   'ans': 1,
                           'exp': '8,215 - 4,786 = 3,429.',
                           'hint': 'Carefully trace each borrow across all four columns.',
                           'options': ['3,419', '3,429', '3,439', '3,529'],
                           'q': 'Calculate 8,215 - 4,786 using column algorithm.',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Ones: 5 - 6 "
                                  "(unbundle 1 ten -> 0 tens left; 15 - 6 = 9).</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Tens: 0 - 8 (unbundle 1 hundred -> 1 hundred left; 10 - 8 = "
                                  "2).</li><li class='mb-2 text-slate-700 leading-relaxed'>Hundreds: 1 - 7 (unbundle 1 "
                                  "thousand -> 7 thousands left; 11 - 7 = 4).</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Thousands: 7 - 4 = 3.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Result = 3,429.</li></ol></div><div class='bg-amber-50 border-l-4 "
                                  'border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> Systematic unbundling gives "
                                  '3,429.</div></div>'}],
        'section': 'Regrouping Subtraction & Production Records',
        'speech': '',
        'title': 'Challenge 3'},
    {   'id': 20,
        'quizzes': [   {   'ans': 3,
                           'exp': 'All three combinations equal ₹3,650.',
                           'hint': 'Calculate the monetary value of each combination.',
                           'options': [   '7 × ₹500 + 1 × ₹100 + 1 × ₹50',
                                          '6 × ₹500 + 6 × ₹100 + 1 × ₹50',
                                          '5 × ₹500 + 11 × ₹100 + 1 × ₹50',
                                          'All of these'],
                           'q': 'A student deposits ₹3,650 into the school savings bank. Which breakdown of currency '
                                'notes equals exactly ₹3,650?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Option A: (7 × "
                                  "500 = 3,500) + 100 + 50 = ₹3,650.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Option B: (6 × 500 = 3,000) + (6 × 100 = 600) + 50 = "
                                  "₹3,650.</li><li class='mb-2 text-slate-700 leading-relaxed'>Option C: (5 × 500 = "
                                  "2,500) + (11 × 100 = 1,100) + 50 = ₹3,650.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>All combinations represent valid breakdowns of "
                                  "₹3,650!</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'A target currency sum can be composed using multiple denomination '
                                  'combinations.</div></div>'},
                       {   'ans': 1,
                           'exp': '2,000 + 800 + 70 = ₹2,870.',
                           'hint': '4 × 500 = 2,000; 8 × 100 = 800; 7 × 10 = 70.',
                           'options': ['₹2,860', '₹2,870', '₹2,880', '₹2,970'],
                           'q': 'What is the total value of 4 notes of ₹500, 8 notes of ₹100, and 7 notes of ₹10?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>500-rupee "
                                  "notes: 4 × ₹500 = ₹2,000.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>100-rupee notes: 8 × ₹100 = ₹800.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>10-rupee notes: 7 × ₹10 = ₹70.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>Sum: 2,000 + 800 + 70 = ₹2,870.</li></ol></div><div "
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Multiply each note "
                                  'count by its face value and sum the products.</div></div>'},
                       {   'ans': 1,
                           'exp': '683 - 100 + 1 = 584.',
                           'hint': '99 is 1 less than 100, so subtracting 100 removes 1 too many.',
                           'options': [   'Subtract 100 then subtract 1 (582)',
                                          'Subtract 100 then add 1 (584)',
                                          'Add 100 then subtract 1 (782)',
                                          'Subtract 90 then 9 (584)'],
                           'q': 'Using mental compensation, how do you quickly calculate 683 - 99?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Landmark "
                                  "number near 99 is 100.</li><li class='mb-2 text-slate-700 leading-relaxed'>683 - "
                                  "100 = 583.</li><li class='mb-2 text-slate-700 leading-relaxed'>Because 99 was to be "
                                  "subtracted and we subtracted 100 (1 too many), add 1 back.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>583 + 1 = 584.</li></ol></div><div "
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Subtracting 99 is "
                                  'equivalent to subtracting 100 and adding 1.</div></div>'},
                       {   'ans': 1,
                           'exp': '458 + 100 - 1 = 557.',
                           'hint': 'Adding 100 adds 1 too many, so subtract 1.',
                           'options': [   'Add 100 then add 1 (559)',
                                          'Add 100 then subtract 1 (557)',
                                          'Subtract 100 then add 1 (359)',
                                          'Multiply by 2'],
                           'q': 'Using mental compensation, how do you quickly calculate 458 + 99?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Landmark "
                                  "number near 99 is 100.</li><li class='mb-2 text-slate-700 leading-relaxed'>458 + "
                                  "100 = 558.</li><li class='mb-2 text-slate-700 leading-relaxed'>Because we added 100 "
                                  "instead of 99, we added 1 extra unit.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Subtract 1: 558 - 1 = 557.</li></ol></div><div class='bg-amber-50 "
                                  'border-l-4 border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> Adding 99 is equivalent to adding "
                                  '100 and subtracting 1.</div></div>'},
                       {   'ans': 2,
                           'exp': '2,740 - 1,000 + 1 = 1,741.',
                           'hint': 'Subtract 1,000 then add 1.',
                           'options': ['1,739', '1,740', '1,741', '1,841'],
                           'q': 'Using mental compensation, what is 2,740 - 999?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>999 is 1 less "
                                  "than 1,000.</li><li class='mb-2 text-slate-700 leading-relaxed'>2,740 - 1,000 = "
                                  "1,740.</li><li class='mb-2 text-slate-700 leading-relaxed'>Add 1 back to compensate "
                                  "for the extra 1 subtracted.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>1,740 + 1 = 1,741.</li></ol></div><div class='bg-amber-50 "
                                  'border-l-4 border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> Friendly milestone numbers make "
                                  '4-digit mental math instantaneous.</div></div>'},
                       {   'ans': 1,
                           'exp': 'Since 450 < 475, the left side is less than (<) the right side.',
                           'hint': 'Both share 3,800. Compare 450 and 475.',
                           'options': ['>', '<', '=', 'Cannot tell'],
                           'q': 'Without calculating, which symbol correctly compares: (3,800 + 450) ___ (3,800 + '
                                '475)?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Both "
                                  "expressions contain the common term 3,800.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Compare the remaining addends: 450 vs 475.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>Since 450 < 475, (3,800 + 450) < (3,800 + "
                                  "475).</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'Relational thinking compares terms directly without tedious addition.</div></div>'},
                       {   'ans': 0,
                           'exp': 'Since 320 < 350, subtracting 320 leaves more behind (>).',
                           'hint': 'Subtracting a smaller number leaves a larger remainder.',
                           'options': ['>', '<', '=', 'Cannot tell'],
                           'q': 'Without calculating, which symbol correctly compares: (5,000 - 320) ___ (5,000 - '
                                '350)?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Both "
                                  "expressions start from the identical base 5,000.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Comparing subtrahends: 320 is smaller than 350.</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>Removing a smaller amount leaves a "
                                  "greater remainder.</li><li class='mb-2 text-slate-700 leading-relaxed'>Therefore, "
                                  "(5,000 - 320) > (5,000 - 350).</li></ol></div><div class='bg-amber-50 border-l-4 "
                                  'border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> In subtraction from equal amounts, "
                                  'smaller subtrahend yields larger difference.</div></div>'},
                       {   'ans': 2,
                           'exp': 'Both expressions equal 3,700.',
                           'hint': 'Notice that 2,500 decreased by 100 to 2,400 while 1,200 increased by 100 to 1,300.',
                           'options': ['>', '<', '=', 'Cannot tell'],
                           'q': 'Compare the two expressions: (2,500 + 1,200) ___ (2,400 + 1,300).',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>First "
                                  "expression: 2,500 + 1,200 = 3,700.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Second expression: 2,400 + 1,300 = 3,700.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>Notice the balance: transferring 100 from 2,500 to "
                                  "1,200 yields 2,400 + 1,300 without changing the sum.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>The expressions are equal (=).</li></ol></div><div "
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Compensation "
                                  'preserves equality when equal amounts are transferred between addends.</div></div>'},
                       {   'ans': 1,
                           'exp': 'Odd numbers occupy the 4 corners and center; even numbers occupy the 4 edge cells.',
                           'hint': 'There are 4 even numbers (2, 4, 6, 8) and 5 odd numbers (1, 3, 5, 7, 9).',
                           'options': [   'All even numbers in the first row',
                                          'Even numbers placed in the 4 edge positions, odd numbers in 4 corners and '
                                          'center',
                                          'All odd numbers in the diagonal',
                                          'Random assignment'],
                           'q': 'In the 3 × 3 Neighbouring Square puzzle, numbers 1 to 9 are placed so no two even '
                                'numbers share a side. What structural pattern is required?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Numbers 1 to 9 "
                                  'contain 4 even numbers (2, 4, 6, 8) and 5 odd numbers (1, 3, 5, 7, 9).</li><li '
                                  "class='mb-2 text-slate-700 leading-relaxed'>A 3 × 3 grid behaves like a chessboard "
                                  'with 5 light squares (corners and center) and 4 dark squares (edge '
                                  "centers).</li><li class='mb-2 text-slate-700 leading-relaxed'>Dark squares do not "
                                  "touch each other horizontally or vertically.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Placing even numbers in the 4 edge positions ensures no two even "
                                  "numbers share an edge!</li></ol></div><div class='bg-amber-50 border-l-4 "
                                  'border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> Bipartite chessboard graph coloring "
                                  'solves adjacency parity constraints.</div></div>'},
                       {   'ans': 1,
                           'exp': 'The sum of integers from 1 to 9 is (9 × 10) ÷ 2 = 45.',
                           'hint': 'Sum the digits: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9.',
                           'options': ['40', '45', '50', '55'],
                           'q': 'What is the sum of all nine digits from 1 to 9 placed inside the Neighbouring Square '
                                'grid?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Sum = 1 + 2 + "
                                  "3 + 4 + 5 + 6 + 7 + 8 + 9.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Pairing from ends: (1+9) + (2+8) + (3+7) + (4+6) + 5.</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>10 + 10 + 10 + 10 + 5 = 45.</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>Alternatively: n(n+1)/2 = 9 × 10 / 2 = "
                                  "45.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'The total sum of numbers 1 through 9 is always 45.</div></div>'}],
        'section': 'Financial Slips, Mental Math & Logic Puzzles',
        'speech': '',
        'title': 'Challenge 4'}]
