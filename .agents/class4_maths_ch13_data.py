# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 13: The Transport Museum
Full 20-slide structured curriculum dataset.
"""

SLIDES_DATA = [   {   'checkpoints': [   {   'ans': 2,
                               'exp': 'Both 28 (7 × 4) and 35 (7 × 5) share the common factor 7.',
                               'options': ['4', '5', '7', '8'],
                               'q': 'If a row contains products 28 and 35, what single-digit multiplier is common to '
                                    'both?'},
                           {   'ans': 1,
                               'exp': 'Each cell represents the product of its row multiplier and column multiplier.',
                               'options': ['Addition', 'Multiplication', 'Subtraction', 'Division'],
                               'q': 'In a multiplication matrix, what operation links the row header and column '
                                    'header?'}],
        'id': 1,
        'section': 'Grid Multiplication & Multiplier Deduction',
        'speech': 'Welcome young mathematicians to our study of grid multiplication logic through the engaging mystery '
                  'matrix puzzle. In this mathematical challenge, we explore a grid where numbers along horizontal '
                  'rows and vertical columns intersect. Each box within the matrix displays a product created by '
                  'multiplying a secret single-digit row multiplier by a single-digit column multiplier. To solve the '
                  'mystery, we must become mathematical detectives and analyze the given target products carefully. '
                  'Suppose a white cell reveals the number twenty-four while its adjacent neighbor in the same row '
                  'shows thirty-six. We immediately look for common factors shared by both products. Since twelve is '
                  'not a single digit, we deduce the row multiplier must be six, or perhaps four depending on the '
                  'column clues. If the row multiplier is six, then the corresponding column values must be four and '
                  'six because six times four is twenty-four and six times six is thirty-six. Orange and blue '
                  'highlight boxes introduce additional constraint clues, helping us isolate unknown factors '
                  'systematically without guessing. This grid logic strengthens our understanding that multiplication '
                  'is commutative and factor pairs connect rows and columns seamlessly. By verifying row totals and '
                  'column totals against our deduced multipliers, we ensure complete mathematical consistency across '
                  'the entire matrix puzzle.',
        'title': 'Mystery Matrix Logic'},
    {   'checkpoints': [   {   'ans': 2,
                               'exp': '10 groups of 10 equal 100, forming one hundred flat in base-ten blocks.',
                               'options': ['10', '50', '100', '1,000'],
                               'q': 'What is the value of 10 groups of 10 items bundled together?'},
                           {   'ans': 1,
                               'exp': '7 × 10 equals 7 Tens, which equals 70.',
                               'options': ['7 Ones', '7 Tens (70)', '7 Hundreds', '17 Units'],
                               'q': 'How can 7 × 10 be expressed in place-value language?'}],
        'id': 2,
        'section': 'Base-Ten Scaling & Unit Bundling',
        'speech': 'Let us explore how numbers grow when we multiply by ten using visual representations of base-ten '
                  'bundles and rods. When we consider two times ten, we are gathering two complete bundles containing '
                  'ten individual items each. Counting by tens, we say ten, twenty. Therefore, two times ten equals '
                  'twenty, which can also be described as two tens. Similarly, three times ten represents three tens, '
                  'giving a total value of thirty. Notice how multiplying any single-digit number by ten preserves the '
                  'original digit in the tens place while placing a zero in the ones place. What happens when we scale '
                  'up to ten times ten? We are combining ten complete rods of ten units each. Counting ten groups of '
                  'ten reveals the sequence ten, twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety, and one '
                  'hundred. Ten tens bundle together to create one flat of one hundred. This fundamental place-value '
                  'shift is the foundation of our decimal number system. Whenever we multiply by ten, every digit '
                  'shifts one place to the left, and a place-holding zero occupies the empty ones column. Mastering '
                  'this base-ten visualization allows us to compute large products mentally with exceptional '
                  'confidence and structural speed.',
        'title': 'Visualizing Tens Multiplication'},
    {   'checkpoints': [   {   'ans': 0,
                               'exp': '(8 × 10) + (8 × 5) = 80 + 40 = 120.',
                               'options': ['(8 × 10) + (8 × 5)', '(8 × 10) - (8 × 5)', '(8 × 15) + 10', '(8 × 20) - 5'],
                               'q': 'How can 8 × 15 be calculated using the tens and ones split method?'},
                           {   'ans': 2,
                               'exp': '6 × 10 = 60, 6 × 5 = 30; 60 + 30 = 90.',
                               'options': ['75', '80', '90', '95'],
                               'q': 'What is the product of 6 × 15 when calculated by area decomposition?'}],
        'id': 3,
        'section': 'Area Breakdown & Multi-Digit Tables',
        'speech': 'We can construct multi-digit multiplication tables effortlessly by breaking numbers into tens and '
                  'ones using the visual area model. Consider constructing the times-fifteen table. Remembering '
                  'fifteen facts from memory might appear intimidating at first glance, but fifteen is simply the sum '
                  'of ten and five. Therefore, to multiply any number by fifteen, we split the problem into two '
                  'friendly calculations. For example, let us compute four times fifteen. We construct a rectangular '
                  'area partitioned into two neat sections. The first section represents four times ten, which yields '
                  'forty. The second adjacent section represents four times five, which yields twenty. Adding forty '
                  'and twenty gives sixty, which is the exact product of four times fifteen. Let us try another '
                  'calculation such as six times fifteen. Six times ten equals sixty, and six times five equals '
                  'thirty. Combining sixty and thirty gives ninety. This distributive strategy applies universally to '
                  'any multi-digit number in our curriculum. Whether constructing tables for twelve, thirteen, '
                  'fourteen, sixteen, or eighteen, we decompose the number into convenient decade bundles and '
                  'manageable units. Breaking complex arrays into simpler geometric rectangles transforms overwhelming '
                  'rote memorization into clear, systematic mathematical reasoning that never fails under examination '
                  'pressure.',
        'title': 'Constructing Table Arrays'},
    {   'checkpoints': [   {   'ans': 1,
                               'exp': 'Since 15 = 3 × 5, every multiple of 15 is 3 times the multiple of 5.',
                               'options': [   'It is 2 times bigger',
                                              'It is 3 times bigger',
                                              'It is 10 more',
                                              'It is 5 times bigger'],
                               'q': 'What is the relationship between any entry in the times-15 table and the times-5 '
                                    'table?'},
                           {   'ans': 2,
                               'exp': 'All multiples of 5 and 15 alternate between ending in 5 and 0.',
                               'options': ['Only 0', 'Only 5', 'Either 0 or 5', 'Any even number'],
                               'q': 'What digits can appear in the ones place of products in both times-5 and times-15 '
                                    'tables?'}],
        'id': 4,
        'section': 'Pattern Discoveries & Table Relationships',
        'speech': 'Mathematical insight blossoms when we compare different multiplication tables side by side to '
                  'uncover their hidden relationships and structural symmetries. Let us place the times-five table '
                  'alongside the times-fifteen table and examine their corresponding products closely across each '
                  'position. In the times-five table, the sequence of products progresses steadily as five, ten, '
                  'fifteen, twenty, twenty-five, thirty, thirty-five, and forty. In the times-fifteen table, the '
                  'products progress as fifteen, thirty, forty-five, sixty, seventy-five, ninety, one hundred five, '
                  'and one hundred twenty. Notice that every product in the times-fifteen table is exactly three times '
                  'the corresponding product in the times-five table. Why is this so? Because fifteen is three times '
                  'five, every multiple of fifteen must be three times the multiple of five. Furthermore, observe the '
                  'final digits of both tables. Both tables end strictly in five or zero, reflecting their shared '
                  'divisibility properties. When we compare tables from eleven through twenty, we notice how the ones '
                  'digits cycle predictably based on the units component of each base number. Recognizing these '
                  'inter-table patterns empowers us to verify our calculations quickly, connect multiplication to '
                  'scaling factors, and develop deep structural number sense across all arithmetic operations in our '
                  'daily studies.',
        'title': 'Comparing Number Tables'},
    {   'checkpoints': [   {   'ans': 0,
                               'exp': 'Half of 16 is 8; 4 × 8 = 32, and doubling 32 yields 64.',
                               'options': ['Double (4 × 8)', 'Halve (4 × 8)', 'Add 16 to 4', 'Multiply 4 × 10'],
                               'q': 'How can 4 × 16 be calculated using the halving and doubling strategy?'},
                           {   'ans': 2,
                               'exp': 'Doubling 21 gives 42 (since 14 is 2 × 7).',
                               'options': ['28', '35', '42', '49'],
                               'q': 'If 3 × 7 = 21, what is 3 × 14 by doubling?'}],
        'id': 5,
        'section': 'Grouping Strategies & Factor Splitting',
        'speech': 'A powerful mental math tool used by experienced mathematicians is the halving and doubling strategy '
                  'for constructing complex multi-digit tables. Suppose we need to calculate three times fourteen, but '
                  'we have not memorized the fourteen table by rote memory. We can split the group of fourteen into '
                  'two equal halves of seven items each. First, we calculate three times seven, which is a familiar '
                  'foundational fact giving twenty-one. Since fourteen is twice seven, the total product must be twice '
                  'twenty-one. Doubling twenty-one gives forty-two, which is the exact product of three times '
                  'fourteen. This strategy works because splitting one factor in half and doubling the resulting '
                  'product preserves the total quantity perfectly. Let us apply this method to calculate six times '
                  'twelve. Half of twelve is six, and six times six is thirty-six. Doubling thirty-six yields '
                  'seventy-two, so six times twelve equals seventy-two. Alternatively, we could halve six to get '
                  'three, compute three times twelve which is thirty-six, and double thirty-six to obtain seventy-two. '
                  'Whether we halve the multiplier or the multiplicand, factor manipulation gives us extraordinary '
                  'mental flexibility and computational speed in computing multi-digit multiplication without paper '
                  'and pencil during daily classroom problem-solving activities.',
        'title': 'Halving And Doubling'},
    {   'checkpoints': [   {   'ans': 2,
                               'exp': '15 × 2 = 30, and 30 × 10 = 300.',
                               'options': ['150', '250', '300', '350'],
                               'q': 'What is 15 × 20 calculated by decade factoring (15 × 2 × 10)?'},
                           {   'ans': 2,
                               'exp': '18 × 10 represents 18 Tens, which equals 180.',
                               'options': ['8 Tens', '10 Tens', '18 Tens (180)', '180 Tens'],
                               'q': 'How many tens are contained in the product 18 × 10?'}],
        'id': 6,
        'section': 'Multiplying Multiples of Ten',
        'speech': 'Now let us extend our multiplication principles to larger multiples of ten, which we call scaling '
                  'by decades in mental arithmetic. Consider calculating fourteen times ten. We express this in words '
                  'as fourteen tens. Since one ten is ten, fourteen tens equals one hundred forty without any '
                  'complicated column addition. Now consider a more advanced problem: twelve times twenty. Twenty can '
                  'be decomposed cleanly into two times ten. Therefore, twelve times twenty can be calculated in two '
                  'effortless sequential steps. First, we multiply twelve by two, which gives twenty-four. Then, we '
                  'multiply twenty-four by ten, which gives two hundred forty. Notice how the problem simplified into '
                  'basic single-digit multiplication followed by a base-ten place-value shift. Let us examine thirty '
                  'times forty. Three times four equals twelve. Since both thirty and forty are multiples of ten, we '
                  'have two factors of ten involved in the calculation. Twelve multiplied by ten gives one hundred '
                  'twenty, and multiplied by ten again gives one thousand two hundred. Counting the zeroes in our '
                  'decade factors provides a reliable structural shortcut, but understanding the underlying '
                  'place-value shifts ensures we never make magnitude errors when estimating large industrial '
                  'quantities in real life.',
        'title': 'Scaling Decade Multiples'},
    {   'checkpoints': [   {   'ans': 2,
                               'exp': '8 rows × 4 seats per row = 32 seats.',
                               'options': ['24 seats', '28 seats', '32 seats', '36 seats'],
                               'q': 'If a heritage museum tram has 8 rows of 4 seats each, what is its total passenger '
                                    'capacity?'},
                           {   'ans': 1,
                               'exp': 'Multiplying number of vehicles by capacity per vehicle gives total fleet '
                                      'capacity instantly.',
                               'options': [   'To guess passenger numbers',
                                              'To compute total capacity quickly across identical vehicles',
                                              'To slow down departures',
                                              'To eliminate tickets'],
                               'q': 'Why do transport managers use multiplication when planning vehicle fleets?'}],
        'id': 7,
        'section': 'Real-World Contexts & Transit Exhibits',
        'speech': 'Welcome to the historic Transport Museum, where dynamic artifacts of human travel illustrate the '
                  'practical power of mathematics in motion and structural engineering design. From ancient wooden '
                  'bullock carts and riverboats to modern steam locomotives, diesel engines, and passenger aircraft, '
                  'transportation logistics rely fundamentally on multiplication and division algorithms to manage '
                  'passengers safely and reliably. When museum curators organize historical tours, they must calculate '
                  'vehicle passenger capacities, ticket revenues, and schedule intervals with meticulous precision. '
                  'Suppose the museum miniature railway features special vintage passenger coaches that transport '
                  'visiting school groups across the extensive exhibition grounds. If each vintage carriage seats a '
                  'specific number of passengers, determining the entire fleet capacity requires scaling passenger '
                  'counts across multiple coaches. Similarly, calculating fuel consumption, maintenance schedules, '
                  'visitor arrival quotas, and tour guide assignments demands systematic multi-digit computation every '
                  'single morning. As we explore the transport galleries, we will see that numbers are not merely '
                  'abstract figures written on a classroom chalkboard; they represent real seats, tickets, coaches, '
                  'platform tracks, and travel distances across our country. Connecting our classroom mathematical '
                  'algorithms to tangible transport vehicles helps us understand why accuracy and speed matter in '
                  'real-world engineering and public transit operations.',
        'title': 'Transport Museum Math'},
    {   'checkpoints': [   {   'ans': 0,
                               'exp': '(10×10=100) + (5×10=50) + (10×4=40) + (5×4=20) = 210.',
                               'options': ['100, 50, 40, 20', '150, 140, 50, 10', '100, 20, 14, 15', '140, 50, 20, 10'],
                               'q': 'In the box method for 15 × 14, what are the four partial products?'},
                           {   'ans': 2,
                               'exp': '15 × 14 = 210 children.',
                               'options': ['190 children', '200 children', '210 children', '220 children'],
                               'q': 'What is the total capacity of 15 coaches with 14 children each?'}],
        'id': 8,
        'section': 'Box Method for 2-Digit Multiplication',
        'speech': 'At the museum outdoor exhibit, a beloved toy train transports visiting children around a scenic '
                  'loop with vintage miniature signals. The train consists of fifteen passenger coaches, and each '
                  'coach comfortably accommodates fourteen children on its wooden bench seats. How many children can '
                  'ride the toy train simultaneously? We must calculate fifteen times fourteen. To solve this '
                  'two-digit by two-digit multiplication with total clarity, we employ the box grid area method. We '
                  'partition fifteen into ten plus five along the top edge, and fourteen into ten plus four along the '
                  'vertical edge. This creates four distinct calculation chambers inside our visual grid. The first '
                  'chamber computes ten times ten, which equals one hundred. The second chamber computes five times '
                  'ten, which equals fifty. The third chamber computes ten times four, which equals forty. The fourth '
                  'chamber computes five times four, which equals twenty. Now we sum all four partial products '
                  'together: one hundred plus fifty plus forty plus twenty. One hundred plus fifty is one hundred '
                  'fifty; adding forty gives one hundred ninety; adding twenty yields exactly two hundred ten. Thus, '
                  'the toy train carries two hundred ten children in full capacity without confusion or arithmetic '
                  'errors.',
        'title': 'Toy Train Grid'},
    {   'checkpoints': [   {   'ans': 1,
                               'exp': '15 × 21 = 315; 324 - 315 = 9 remainder.',
                               'options': ['20 remainder 14', '21 remainder 9', '22 remainder 0', '21 remainder 5'],
                               'q': 'What is 324 ÷ 15 expressed as quotient and remainder?'},
                           {   'ans': 1,
                               'exp': 'In real-world passenger transit, any remainder requires an additional coach to '
                                      'carry everyone.',
                               'options': [   'Coaches must be even',
                                              'To ensure the 9 remaining children also have a seat',
                                              'For luggage storage only',
                                              'Because 21 is unlucky'],
                               'q': 'Why must 22 coaches be ordered instead of 21 for 324 children?'}],
        'id': 9,
        'section': 'Long Division with Remainders',
        'speech': 'When organizing transport for large visiting assemblies, division with remainders becomes an '
                  'essential logistical tool in daily operations. Suppose three hundred twenty-four school children '
                  'arrive at the Transport Museum station eager to board vintage passenger coaches. If each railway '
                  'coach has a strict seating limit of fifteen children, how many coaches must the station master '
                  'allocate? To solve this real-world problem, we divide three hundred twenty-four by fifteen using '
                  'systematic long division steps. First, we estimate how many groups of fifteen fit into thirty-two '
                  'tens. Since fifteen times two equals thirty, fifteen times twenty equals three hundred. Subtracting '
                  'three hundred from three hundred twenty-four leaves twenty-four children remaining on the departure '
                  'platform. Now, how many groups of fifteen fit into twenty-four? Exactly one group, because one '
                  'times fifteen is fifteen. Subtracting fifteen from twenty-four leaves a remainder of nine children. '
                  'Our quotient is twenty-one, with a remainder of nine. Twenty-one full coaches accommodate three '
                  'hundred fifteen children. However, nine children cannot be left behind waiting alone on the '
                  'platform! Therefore, the station master must allocate twenty-two coaches in total so every single '
                  'child has a safe, comfortable seat on the historic train journey with total comfort and security.',
        'title': 'Coach Allocation Remainders'},
    {   'checkpoints': [   {   'ans': 1,
                               'exp': '(24 × 6 = 144) + (24 × 30 = 720) = 864.',
                               'options': ['844', '864', '884', '904'],
                               'q': 'What is the product of 24 × 36?'},
                           {   'ans': 1,
                               'exp': 'Dividend = (Divisor × Quotient) + Remainder.',
                               'options': [   'Dividend = Divisor + Quotient',
                                              'Dividend = (Divisor × Quotient) + Remainder',
                                              'Dividend = Divisor - Remainder',
                                              'Dividend = Quotient ÷ Divisor'],
                               'q': 'What is the division verification formula?'}],
        'id': 10,
        'section': 'Algorithm Mastery & Remainder Verification',
        'speech': 'Let us sharpen our procedural fluency through rigorous multi-digit multiplication and long division '
                  'practice drills in our mathematics notebooks. When performing two-digit by two-digit '
                  'multiplication, such as twenty-four times thirty-six, we systematically compute partial products '
                  'column by column. First, we multiply twenty-four by six ones to obtain one hundred forty-four. '
                  'Next, we multiply twenty-four by three tens, which is thirty, yielding seven hundred twenty. Adding '
                  'one hundred forty-four and seven hundred twenty gives the complete product of eight hundred '
                  'sixty-four. Now let us examine the complementary inverse operation: long division with remainder '
                  'identification. Suppose we divide four hundred seventy-eight by eight. We divide forty-seven tens '
                  'by eight, yielding five tens with seven tens remaining. Bringing down the eight units gives '
                  'seventy-eight. Dividing seventy-eight by eight yields nine, since eight times nine is seventy-two. '
                  'Subtracting seventy-two leaves six as our final remainder. The quotient is fifty-nine with '
                  'remainder six. We always verify our work using the fundamental division formula: Dividend equals '
                  'Divisor multiplied by Quotient plus Remainder. Eight times fifty-nine is four hundred seventy-two, '
                  'and adding six brings us back to four hundred seventy-eight. This self-checking loop guarantees '
                  'absolute accuracy in every arithmetic assessment we encounter.',
        'title': 'Multiplication Division Drill'},
    {   'checkpoints': [   {   'ans': 1,
                               'exp': '8 × 5 = 40; appending two zeroes gives 4,000.',
                               'options': ['400', '4,000', '40,000', '850'],
                               'q': 'What is the product of 80 × 50?'},
                           {   'ans': 2,
                               'exp': '11 × 2 = 22, and 22 × 100 = 2,200.',
                               'options': ['1,100', '2,000', '2,200', '2,400'],
                               'q': 'What is 11 × 200 calculated by factoring?'}],
        'id': 11,
        'section': 'Scaling Factors & Multiples of 100',
        'speech': 'We can scale our mathematical understanding to larger horizons by exploring patterns involving '
                  'multiples of one hundred across transit systems. When we calculate two times one hundred, we are '
                  'grouping two hundreds flats, which clearly equals two hundred. Now consider eleven times two '
                  'hundred. We can decompose this expression into eleven times two, which is twenty-two, multiplied by '
                  'one hundred. Twenty-two multiplied by one hundred equals two thousand two hundred. What happens '
                  'when both factors contain trailing zeroes, such as eighty times fifty? Let us decompose eighty into '
                  'eight times ten, and fifty into five times ten. Rearranging the factors gives eight times five, '
                  'which is forty, multiplied by ten times ten, which is one hundred. Multiplying forty by one hundred '
                  'shifts forty two places to the left, yielding four thousand. Students sometimes make the common '
                  'error of writing four hundred because they overlook that forty itself already ends in a zero! Eight '
                  'times five produces forty, and the two decade zeroes append to create four thousand in total. '
                  'Always compute the basic single-digit multiplication first, and then apply the combined power of '
                  'the trailing zeroes to guarantee place-value precision in all calculations without making any '
                  'estimation blunders.',
        'title': 'Hundreds Scaling Patterns'},
    {   'checkpoints': [   {   'ans': 1,
                               'exp': '750 ÷ 10 = 75 sacks.',
                               'options': ['70 sacks', '75 sacks', '80 sacks', '750 sacks'],
                               'q': 'How many 10 kg sacks can be filled from 750 kg of grain?'},
                           {   'ans': 1,
                               'exp': '846 = (8 × 100) + 46. Quotient is 8, remainder is 46.',
                               'options': ['84 remainder 6', '8 remainder 46', '80 remainder 46', '8 remainder 0'],
                               'q': 'What is 846 ÷ 100 expressed as quotient and remainder?'}],
        'id': 12,
        'section': 'Base-Ten Division & Packaging Logic',
        'speech': 'In real-world transport and trade logistics, division by ten and one hundred represents the '
                  'physical act of packaging and freight distribution. Imagine a heritage agricultural transport depot '
                  'where a harvest of seven hundred fifty kilograms of rice must be bagged for shipment. If the '
                  'warehouse workers pack the grain into ten-kilogram sacks, how many full sacks can they prepare? '
                  'Dividing seven hundred fifty by ten removes one place-value factor of ten, yielding exactly '
                  'seventy-five complete sacks. Every digit shifts one position to the right because dividing by ten '
                  'is the precise inverse of multiplying by ten. Now imagine distributing two thousand four hundred '
                  'kilograms of grain into heavy hundred-kilogram bulk transit containers. Dividing two thousand four '
                  'hundred by one hundred shifts each digit two places to the right, yielding twenty-four containers. '
                  'What happens if an amount does not divide evenly, such as eight hundred forty-six divided by one '
                  'hundred? Eight hundred forty-six contains eight hundreds with forty-six units left over. Therefore, '
                  'eight hundred forty-six divided by one hundred gives a quotient of eight with a remainder of '
                  'forty-six. Understanding this base-ten shift makes calculating inventory shipments, financial '
                  'payouts, and bulk freight distributions instant, efficient, and completely error-free.',
        'title': 'Dividing Tens Hundreds'},
    {   'checkpoints': [   {   'ans': 1,
                               'exp': '(3 × 200 = 600) + 50 + 20 = ₹670.',
                               'options': ['₹650', '₹670', '₹680', '₹700'],
                               'q': 'What is the total value of 3 notes of ₹200 + 1 note of ₹50 + 1 note of ₹20?'},
                           {   'ans': 2,
                               'exp': '35 ÷ 5 = 7 coins.',
                               'options': ['5 coins', '6 coins', '7 coins', '8 coins'],
                               'q': 'How many ₹5 coins are needed to make ₹35?'}],
        'id': 13,
        'section': 'Financial Math & Denomination Combinations',
        'speech': 'At the museum ticket counter, a young visitor purchases special admission passes using a collection '
                  'of Indian currency notes and coins. Indian currency denominations include two-hundred-rupee notes, '
                  'fifty-rupee notes, twenty-rupee notes, five-rupee coins, and two-rupee coins in common circulation. '
                  'Suppose four heritage passes cost a total of six hundred eighty-five rupees. How can this exact '
                  'amount be paid using the fewest possible currency notes and coins? We begin with the highest '
                  'denomination that fits into six hundred eighty-five. Three notes of two hundred rupees provide six '
                  'hundred rupees, leaving eighty-five rupees to settle. Next, one note of fifty rupees brings our '
                  'subtotal to six hundred fifty rupees, leaving thirty-five rupees remaining to pay. One note of '
                  'twenty rupees brings the total to six hundred seventy rupees, leaving fifteen rupees. One ten-rupee '
                  'note, or three five-rupee coins, completes the remaining balance. If five-rupee coins are used, '
                  'three coins of five rupees provide fifteen rupees, reaching six hundred eighty-five rupees '
                  'precisely. Denomination puzzles teach us to decompose large monetary totals into optimal additive '
                  'combinations of standard currency units. This financial arithmetic is essential for cashiers, '
                  'business operators, and smart consumers handling everyday transactions across India in every '
                  'marketplace.',
        'title': 'Currency Denomination Puzzles'},
    {   'checkpoints': [   {   'ans': 2,
                               'exp': 'All multiples of 9 have a digital root of 9 (e.g., 5 + 4 = 9 for 54).',
                               'options': ['3', '6', '9', '10'],
                               'q': 'What is the digital root (sum of digits) of any multiple of 9?'},
                           {   'ans': 2,
                               'exp': 'Split 3 and 4, and insert (3 + 4 = 7) in the middle: 374.',
                               'options': ['344', '364', '374', '384'],
                               'q': 'Using the 11s shortcut, what is 34 × 11?'}],
        'id': 14,
        'section': 'Digit Sum Invariants & Number Symmetries',
        'speech': 'Mathematics is the science of patterns, and multiplication reveals some of the most captivating '
                  'numerical symmetries in all of arithmetic. Let us investigate what happens when we multiply numbers '
                  'by nine in our daily mathematics studies. Notice the sequence of products: nine, eighteen, '
                  'twenty-seven, thirty-six, forty-five, fifty-four, sixty-three, seventy-two, eighty-one, and ninety. '
                  'If we calculate the digital sum of each product by adding its digits together, an astonishing '
                  'pattern emerges. One plus eight equals nine; two plus seven equals nine; three plus six equals '
                  'nine; four plus five equals nine! Every single multiple of nine possesses a digital root of nine. '
                  'Now consider multiplying eleven by single digits: eleven, twenty-two, thirty-three, forty-four, '
                  'fifty-five. The tens digit and ones digit are identical twins. When we multiply two-digit numbers '
                  'by eleven, such as twenty-five times eleven, we split the digits two and five, and insert their '
                  'sum, which is seven, directly between them to obtain two hundred seventy-five! Discovering these '
                  'colored digit patterns transforms arithmetic from mechanical labor into a joyful treasure hunt of '
                  'structural symmetry. Recognizing patterns helps us detect calculation errors immediately and '
                  'reinforces our intuition about numbers. Mathematical patterns reveal that numbers behave according '
                  'to dependable, elegant rules that make problem solving truly delightful.',
        'title': 'Multiplication Pattern Discovery'},
    {   'checkpoints': [   {   'ans': 2,
                               'exp': '8 × 20 = 160 passengers.',
                               'options': ['120 passengers', '140 passengers', '160 passengers', '180 passengers'],
                               'q': 'What is the passenger capacity of 8 minibuses seating 20 passengers each?'},
                           {   'ans': 2,
                               'exp': '45 ÷ 5 = 9 cars.',
                               'options': ['7 cars', '8 cars', '9 cars', '10 cars'],
                               'q': 'If 1 car carries 5 passengers, how many cars are needed for 45 travelers?'}],
        'id': 15,
        'section': 'Multi-Modal Vehicle Capacity Calculations',
        'speech': 'At the grand finale of the Transport Museum, visitors explore the vehicle matching gallery '
                  'showcasing entire fleets at full passenger capacity. Different modes of transport carry vastly '
                  'different passenger quotas depending on their engineering design, physical size, and safety '
                  'specifications. A standard passenger bicycle carries one person. An auto-rickshaw carries three '
                  'passengers through bustling streets. A passenger car seats five travelers. A school minibus '
                  'accommodates twenty passengers safely. A commercial airliner carries one hundred eighty passengers, '
                  'while an express train sleeper coach accommodates seventy-two passengers across long distances. Now '
                  'let us calculate fleet totals. Suppose the museum fleet includes eight minibuses. Eight minibuses '
                  'times twenty passengers each equals one hundred sixty passengers. If a railway company operates '
                  'twelve sleeper coaches, twelve times seventy-two equals eight hundred sixty-four sleeping berths! '
                  'Let us check six passenger cars: six times five equals thirty travelers. Notice how fleet matching '
                  'requires multiplying vehicle units by their individual passenger rate. By comparing these fleet '
                  'capacities, transit engineers determine which combination of vehicles best serves a city during '
                  'peak rush hour. Multiplication allows transport planners to balance traffic flow, minimize fuel '
                  'consumption, and ensure that thousands of citizens reach their destinations safely every single '
                  'morning.',
        'title': 'Fleet Capacity Matching'},
    {   'checkpoints': [   {   'ans': 1,
                               'exp': '4 × 25 = 100 passengers.',
                               'options': ['75 passengers', '100 passengers', '125 passengers', '150 passengers'],
                               'q': 'If 4 minibuses carry 25 passengers each, what is their combined capacity?'},
                           {   'ans': 2,
                               'exp': '400 ÷ 50 = 8 buses.',
                               'options': ['6 buses', '7 buses', '8 buses', '9 buses'],
                               'q': 'How many 50-seater buses are required to transport the remaining 400 '
                                    'passengers?'}],
        'id': 16,
        'section': 'Integrated Logistics & Multi-Step transit Problems',
        'speech': 'We conclude our exploration of the Transport Museum by synthesizing all our multiplication and '
                  'division skills into integrated fleet logistics problems. Consider a complex transportation '
                  'scenario where five hundred visitors must travel from the central railway junction to the museum '
                  'exhibit grounds. The transport coordinator has a mixed fleet consisting of four minibuses seating '
                  'twenty-five passengers each, and several large electric buses seating fifty passengers each. First, '
                  'let us calculate the capacity of the four minibuses. Four times twenty-five equals one hundred '
                  'passengers. Subtracting one hundred from five hundred leaves four hundred visitors still needing '
                  'transportation. Now, how many fifty-passenger electric buses must be deployed to carry the '
                  'remaining four hundred visitors? We divide four hundred by fifty. Since four hundred divided by '
                  'fifty equals eight, exactly eight electric buses are required. The total fleet consists of four '
                  'minibuses and eight electric buses working together in perfect operational coordination. Every step '
                  'of this logistical solution relied upon the principles we mastered: decomposing numbers, scaling by '
                  'tens, performing multi-digit multiplication, and applying division with precision. This harmonious '
                  'combination of arithmetic and engineering ensures our world stays reliably in motion with safety '
                  'and efficiency every single day.',
        'title': 'Transport Fleet Arithmetic'},
    {   'id': 17,
        'quizzes': [   {   'ans': 2,
                           'exp': '8 × 3 = 24 and 8 × 4 = 32. 8 is the common single-digit factor.',
                           'hint': 'Find the highest common single-digit factor of 24 and 32.',
                           'options': ['6', '7', '8', '9'],
                           'q': 'In a mystery matrix, a row contains products 24 and 32. What single-digit row '
                                'multiplier divides both numbers evenly?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Factors of 24 "
                                  "include 1, 2, 3, 4, 6, 8, 12, 24.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Factors of 32 include 1, 2, 4, 8, 16, 32.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>The common single-digit factors are 1, 2, 4, and "
                                  "8.</li><li class='mb-2 text-slate-700 leading-relaxed'>Choosing 8 gives column "
                                  'multipliers 3 and 4, which are valid single digits.</li></ol></div><div '
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Common row "
                                  'multipliers represent shared factors across row products.</div></div>'},
                       {   'ans': 0,
                           'exp': '(7 × 10) + (7 × 5) = 70 + 35 = 105.',
                           'hint': 'Split 15 into 10 + 5 and apply the distributive property.',
                           'options': ['(7 × 10) + (7 × 5)', '(7 × 10) - (7 × 5)', '(7 × 20) - 15', '(7 × 5) + 10'],
                           'q': 'How can 7 × 15 be computed by decomposing 15 into tens and ones?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Decompose 15 "
                                  "into 10 and 5.</li><li class='mb-2 text-slate-700 leading-relaxed'>Multiply 7 by "
                                  "10: 7 × 10 = 70.</li><li class='mb-2 text-slate-700 leading-relaxed'>Multiply 7 by "
                                  "5: 7 × 5 = 35.</li><li class='mb-2 text-slate-700 leading-relaxed'>Sum the two "
                                  "partial products: 70 + 35 = 105.</li></ol></div><div class='bg-amber-50 border-l-4 "
                                  'border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> Breaking numbers into tens and ones "
                                  'simplifies multi-digit multiplication.</div></div>'},
                       {   'ans': 0,
                           'exp': 'Half of 14 is 7; 4 × 7 = 28, and doubling 28 gives 56.',
                           'hint': 'Split 14 in half, multiply by 4, and double the result.',
                           'options': [   'Halve 14 to 7, calculate 4 × 7 = 28, then double 28 to get 56',
                                          'Multiply 4 × 10 and subtract 4',
                                          'Double 4 to 8 and add 14',
                                          'Divide 14 by 4'],
                           'q': 'Using the halving and doubling strategy, how can you calculate 4 × 14?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Halve the "
                                  "factor 14: 14 ÷ 2 = 7.</li><li class='mb-2 text-slate-700 leading-relaxed'>Compute "
                                  "the simpler multiplication: 4 × 7 = 28.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Double the intermediate result: 28 × 2 = 56.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>Therefore, 4 × 14 = 56.</li></ol></div><div "
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Halving one factor "
                                  'and doubling the product preserves the total quantity.</div></div>'},
                       {   'ans': 1,
                           'exp': 'Since 15 = 3 × 5, every multiple of 15 is 3 times the corresponding multiple of 5.',
                           'hint': 'Divide 15 by 5 to find the scaling factor.',
                           'options': ['2 times', '3 times', '5 times', '10 times'],
                           'q': 'How many times greater is each multiple in the times-15 table compared to the times-5 '
                                'table?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Compare 1 × 15 "
                                  "= 15 with 1 × 5 = 5 (15 ÷ 5 = 3).</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Compare 2 × 15 = 30 with 2 × 5 = 10 (30 ÷ 10 = 3).</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>Every multiple of 15 is exactly 3 times "
                                  "larger than the multiple of 5.</li></ol></div><div class='bg-amber-50 border-l-4 "
                                  'border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> Table scaling follows the ratio "
                                  'between the base factors.</div></div>'},
                       {   'ans': 1,
                           'exp': 'Double 48 is 96. Therefore, 6 × 16 = 96.',
                           'hint': '16 is double 8, so double the product 48.',
                           'options': ['84', '96', '106', '112'],
                           'q': 'If 6 × 8 = 48, what is 6 × 16 using doubling?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Notice that 16 "
                                  "is twice 8.</li><li class='mb-2 text-slate-700 leading-relaxed'>Since 6 × 8 = 48, 6 "
                                  "× 16 must equal 2 × 48.</li><li class='mb-2 text-slate-700 leading-relaxed'>48 + 48 "
                                  "= 96.</li><li class='mb-2 text-slate-700 leading-relaxed'>Therefore, 6 × 16 = "
                                  "96.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'Doubling one factor doubles the final product.</div></div>'},
                       {   'ans': 2,
                           'exp': '(9 × 10 = 90) + (9 × 2 = 18) = 108.',
                           'hint': '(9 × 10) + (9 × 2).',
                           'options': ['98', '102', '108', '118'],
                           'q': 'What is the product of 9 × 12 using the tens-and-ones split?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Split 12 into "
                                  "10 + 2.</li><li class='mb-2 text-slate-700 leading-relaxed'>9 × 10 = 90.</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>9 × 2 = 18.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>90 + 18 = 108.</li></ol></div><div "
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Distributive "
                                  'breakdown works for all numbers 11 to 20.</div></div>'},
                       {   'ans': 2,
                           'exp': '5 × 4 = 20.',
                           'hint': 'Multiply row header 5 by column header 4.',
                           'options': ['10', '15', '20', '24'],
                           'q': 'In a 3×3 multiplication matrix, if row headers are 3, 5, 7 and column headers are 2, '
                                '4, 6, what is the center cell value (row 5, column 4)?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Locate row 2 "
                                  "header: 5.</li><li class='mb-2 text-slate-700 leading-relaxed'>Locate column 2 "
                                  "header: 4.</li><li class='mb-2 text-slate-700 leading-relaxed'>Compute cell "
                                  "product: 5 × 4 = 20.</li></ol></div><div class='bg-amber-50 border-l-4 "
                                  'border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> Each matrix cell is the product of "
                                  'its row and column headers.</div></div>'},
                       {   'ans': 0,
                           'exp': 'Multiplying any whole number by 10 shifts it one place left, placing 0 in the ones '
                                  'column.',
                           'hint': 'Think of 10, 20, 30, 40...',
                           'options': ['0', '1', '5', 'Even numbers only'],
                           'q': 'What digit do all products in the times-10 table end with?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Multiples of "
                                  "10 are 10, 20, 30, 40, 50, etc.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>The ones digit is always 0 because each product consists of whole "
                                  "tens.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'Multiplication by 10 always produces a ones digit of zero.</div></div>'},
                       {   'ans': 0,
                           'exp': 'Half of 18 is 9; 5 × 9 = 45; doubling 45 gives 90.',
                           'hint': 'Half of 18 is 9; 5 × 9 = 45.',
                           'options': [   'Halve 18 to 9, compute 5 × 9 = 45, double to 90',
                                          'Add 18 five times',
                                          'Multiply 5 × 10 and add 8',
                                          'Double 5 to 10 and double 18'],
                           'q': 'How can 5 × 18 be calculated using halving and doubling?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Half of 18 is "
                                  "9.</li><li class='mb-2 text-slate-700 leading-relaxed'>5 × 9 = 45.</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>Double 45: 45 × 2 = 90.</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>Therefore, 5 × 18 = "
                                  "90.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'Halving and doubling turns unfamiliar facts into simple single-digit '
                                  'calculations.</div></div>'},
                       {   'ans': 0,
                           'exp': '8 × 10 = 80; 8 × 5 = 40; 80 + 40 = 120.',
                           'hint': 'Multiply 8 by both 10 and 5, then add.',
                           'options': [   '(8 × 10) + (8 × 5) = 120',
                                          '(8 × 10) + 5 = 85',
                                          '(8 × 5) + 10 = 50',
                                          '(8 × 20) - 10 = 150'],
                           'q': 'Which of the following equals 8 × 15?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>8 × 10 = "
                                  "80.</li><li class='mb-2 text-slate-700 leading-relaxed'>8 × 5 = 40.</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>80 + 40 = 120.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>Thus, 8 × 15 = 120.</li></ol></div><div "
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Distributive area "
                                  'decomposition guarantees quick, accurate table generation.</div></div>'}],
        'section': 'Mystery Matrix, Tables & Halving-Doubling',
        'speech': '',
        'title': 'Challenge 1'},
    {   'id': 18,
        'quizzes': [   {   'ans': 2,
                           'exp': '14 × 2 = 28; 28 × 10 = 280.',
                           'hint': 'Multiply 14 by 2, then multiply by 10.',
                           'options': ['140', '240', '280', '320'],
                           'q': 'What is the product of 14 × 20?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Decompose 20 "
                                  "into 2 × 10.</li><li class='mb-2 text-slate-700 leading-relaxed'>14 × 2 = "
                                  "28.</li><li class='mb-2 text-slate-700 leading-relaxed'>28 × 10 = "
                                  "280.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'Scaling by decades decomposes the multiple of 10 into single-digit × '
                                  '10.</div></div>'},
                       {   'ans': 0,
                           'exp': 'The 4 chambers are 10×10=100, 6×10=60, 10×3=30, and 6×3=18. Sum = 208.',
                           'hint': 'Split 16 into 10 + 6 and 13 into 10 + 3.',
                           'options': [   '(10×10=100), (6×10=60), (10×3=30), (6×3=18)',
                                          '(16×10=160), (16×3=48), (10×3=30), (6×1=6)',
                                          '(10×10=100), (6×3=18), (10×1=10), (6×1=6)',
                                          '(100, 60, 40, 18)'],
                           'q': 'In the box grid method for 16 × 13, what are the four chamber products?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Partition "
                                  "factors: 16 = 10 + 6, and 13 = 10 + 3.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Chamber 1: 10 × 10 = 100.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Chamber 2: 6 × 10 = 60.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Chamber 3: 10 × 3 = 30.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Chamber 4: 6 × 3 = 18.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Sum: 100 + 60 + 30 + 18 = 208.</li></ol></div><div "
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> The box method "
                                  'organizes all 4 partial products without carrying confusion.</div></div>'},
                       {   'ans': 2,
                           'exp': '12 × 10 = 120; 12 × 5 = 60; 120 + 60 = 180 visitors.',
                           'hint': 'Calculate 12 × 15 using (12 × 10) + (12 × 5).',
                           'options': ['150 visitors', '165 visitors', '180 visitors', '195 visitors'],
                           'q': 'A museum miniature railway has 12 coaches, each seating 15 visitors. What is the '
                                'total capacity?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Number of "
                                  "coaches = 12.</li><li class='mb-2 text-slate-700 leading-relaxed'>Seats per coach = "
                                  "15.</li><li class='mb-2 text-slate-700 leading-relaxed'>Total seats = 12 × "
                                  "15.</li><li class='mb-2 text-slate-700 leading-relaxed'>12 × 10 = 120, and 12 × 5 = "
                                  "60.</li><li class='mb-2 text-slate-700 leading-relaxed'>120 + 60 = 180 "
                                  "seats.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'Vehicle fleet capacity equals number of vehicles × capacity per '
                                  'vehicle.</div></div>'},
                       {   'ans': 2,
                           'exp': '25 × 3 = 75; 75 × 10 = 750.',
                           'hint': 'Multiply 25 by 3, then multiply by 10.',
                           'options': ['650', '700', '750', '800'],
                           'q': 'What is 25 × 30 calculated by decade multiplication?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Decompose 30 "
                                  "into 3 × 10.</li><li class='mb-2 text-slate-700 leading-relaxed'>Compute 25 × 3 = "
                                  "75.</li><li class='mb-2 text-slate-700 leading-relaxed'>Apply the decade shift: 75 "
                                  "× 10 = 750.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'Decade multiplication shifts the single-digit product one place left.</div></div>'},
                       {   'ans': 1,
                           'exp': '4 × 6 = 24; 24 × 100 = 2,400.',
                           'hint': '4 × 6 = 24, with two decade zeroes.',
                           'options': ['240', '2,400', '24,000', '460'],
                           'q': 'What is the product of 40 × 60?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>40 = 4 × 10, "
                                  "and 60 = 6 × 10.</li><li class='mb-2 text-slate-700 leading-relaxed'>4 × 6 = "
                                  "24.</li><li class='mb-2 text-slate-700 leading-relaxed'>10 × 10 = 100.</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>24 × 100 = 2,400.</li></ol></div><div "
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Multiplying two "
                                  'decade numbers produces two trailing zeroes.</div></div>'},
                       {   'ans': 1,
                           'exp': '100 + 80 + 40 + 32 = 252.',
                           'hint': '(10×10=100) + (8×10=80) + (10×4=40) + (8×4=32).',
                           'options': ['242', '252', '262', '272'],
                           'q': 'Using the box grid method, what is the product of 18 × 14?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>18 = 10 + 8, "
                                  "and 14 = 10 + 4.</li><li class='mb-2 text-slate-700 leading-relaxed'>Partial "
                                  "products: 100 + 80 + 40 + 32.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>100 + 80 = 180.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>180 + 40 = 220.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>220 + 32 = 252.</li></ol></div><div class='bg-amber-50 border-l-4 "
                                  'border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> Box grid method breaks multi-digit "
                                  'multiplication into 4 clean additions.</div></div>'},
                       {   'ans': 2,
                           'exp': '4 × 30 = 120; 4 × 5 = 20; 120 + 20 = 140 passengers.',
                           'hint': '4 × 35 = 4 × 30 + 4 × 5.',
                           'options': ['120', '130', '140', '150'],
                           'q': 'If 1 vintage bus carries 35 passengers, how many passengers can 4 such buses '
                                'transport?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Number of "
                                  "buses = 4.</li><li class='mb-2 text-slate-700 leading-relaxed'>Passengers per bus = "
                                  "35.</li><li class='mb-2 text-slate-700 leading-relaxed'>4 × 30 = 120.</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>4 × 5 = 20.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>120 + 20 = 140 passengers.</li></ol></div><div "
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Multiplying decade "
                                  'and unit components gives quick fleet calculations.</div></div>'},
                       {   'ans': 1,
                           'exp': '16 × 10 represents 16 Tens, which equals 160.',
                           'hint': 'Think of 16 rods of ten units each.',
                           'options': ['16 Ones', '16 Tens (160)', '16 Hundreds', '106 Units'],
                           'q': 'What is 16 × 10 expressed in place-value terminology?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>16 × 10 means "
                                  "16 groups of 10.</li><li class='mb-2 text-slate-700 leading-relaxed'>16 groups of "
                                  "10 = 16 Tens.</li><li class='mb-2 text-slate-700 leading-relaxed'>16 Tens = "
                                  "160.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'Multiplying by 10 bundles the number directly into tens.</div></div>'},
                       {   'ans': 1,
                           'exp': '100 + 50 + 50 + 25 = 225.',
                           'hint': '(10×10=100) + (5×10=50) + (10×5=50) + (5×5=25).',
                           'options': ['215', '225', '235', '245'],
                           'q': 'What is the product of 15 × 15 (a square array)?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Split both "
                                  "factors into 10 + 5.</li><li class='mb-2 text-slate-700 leading-relaxed'>10 × 10 = "
                                  "100.</li><li class='mb-2 text-slate-700 leading-relaxed'>5 × 10 = 50.</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>10 × 5 = 50.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>5 × 5 = 25.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>100 + 50 + 50 + 25 = 225.</li></ol></div><div class='bg-amber-50 "
                                  'border-l-4 border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> Square numbers can be verified "
                                  'through four-quadrant area decomposition.</div></div>'},
                       {   'ans': 2,
                           'exp': '45 × 2 = 90; 90 × 10 = ₹900.',
                           'hint': '45 × 2 = 90; 90 × 10 = 900.',
                           'options': ['₹800', '₹850', '₹900', '₹950'],
                           'q': 'A tour guide orders 20 souvenir caps at ₹45 each. What is the total cost?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Unit price = "
                                  "₹45.</li><li class='mb-2 text-slate-700 leading-relaxed'>Quantity = 20.</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>Total = 45 × 20.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>45 × 2 = 90.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>90 × 10 = ₹900.</li></ol></div><div class='bg-amber-50 border-l-4 "
                                  'border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> Financial procurement uses decade "
                                  'factoring for rapid mental calculation.</div></div>'}],
        'section': 'Decade Scaling, Box Method & Products',
        'speech': '',
        'title': 'Challenge 2'},
    {   'id': 19,
        'quizzes': [   {   'ans': 1,
                           'exp': '250 = (20 × 12) + 10. 20 vans leave 10 students behind, so 21 vans are needed.',
                           'hint': '250 ÷ 12 = 20 remainder 10. The 10 remaining students still need a van!',
                           'options': ['20 vans', '21 vans', '22 vans', '25 vans'],
                           'q': 'A school group of 250 students boards museum shuttle vans seating 12 students each. '
                                'How many vans are needed to carry all students?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Divide total "
                                  "students by van capacity: 250 ÷ 12.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>12 × 20 = 240 students.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>250 - 240 = 10 students remaining.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>Quotient = 20, Remainder = 10.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>Since 10 students cannot be abandoned, 20 + 1 = 21 "
                                  "vans are required.</li></ol></div><div class='bg-amber-50 border-l-4 "
                                  'border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> In passenger transit, any remainder "
                                  'requires an additional vehicle.</div></div>'},
                       {   'ans': 1,
                           'exp': '8 × 23 = 184; 185 - 184 = 1 remainder.',
                           'hint': '8 × 23 = 184.',
                           'options': ['22 remainder 9', '23 remainder 1', '24 remainder 1', '23 remainder 5'],
                           'q': 'What is the quotient and remainder of 185 ÷ 8?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Divide 18 by "
                                  "8: 8 × 2 = 16 (remainder 2).</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Bring down 5 to make 25.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Divide 25 by 8: 8 × 3 = 24 (remainder 1).</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>Quotient = 23, Remainder = 1.</li></ol></div><div "
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Long division "
                                  'processes digits from left to right systematically.</div></div>'},
                       {   'ans': 1,
                           'exp': '7 × 6 = 42; 42 × 100 = 4,200.',
                           'hint': '7 × 6 = 42, then attach two zeroes.',
                           'options': ['420', '4,200', '42,000', '760'],
                           'q': 'What is the product of 70 × 60?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>70 = 7 × 10, "
                                  "and 60 = 6 × 10.</li><li class='mb-2 text-slate-700 leading-relaxed'>7 × 6 = "
                                  "42.</li><li class='mb-2 text-slate-700 leading-relaxed'>10 × 10 = 100.</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>42 × 100 = 4,200.</li></ol></div><div "
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Multiplying two "
                                  'multiples of 10 creates a product in hundreds or thousands.</div></div>'},
                       {   'ans': 1,
                           'exp': '900 ÷ 10 = 90.',
                           'hint': 'Dividing by 10 shifts digits one place right (removes one zero).',
                           'options': ['9', '90', '900', '9,000'],
                           'q': 'What is 900 ÷ 10?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>900 consists "
                                  "of 90 tens.</li><li class='mb-2 text-slate-700 leading-relaxed'>Dividing by 10 "
                                  "removes one factor of 10.</li><li class='mb-2 text-slate-700 leading-relaxed'>900 ÷ "
                                  "10 = 90.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'Dividing by 10 shifts the decimal point one position to the left.</div></div>'},
                       {   'ans': 0,
                           'exp': '3,500 ÷ 100 = 35.',
                           'hint': 'Dividing by 100 shifts digits two places right (removes two zeroes).',
                           'options': ['35', '350', '3,500', '35,000'],
                           'q': 'What is 3,500 ÷ 100?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>3,500 contains "
                                  "35 hundreds.</li><li class='mb-2 text-slate-700 leading-relaxed'>Dividing by 100 "
                                  "removes both trailing zeroes.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>3,500 ÷ 100 = 35.</li></ol></div><div class='bg-amber-50 "
                                  'border-l-4 border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> Dividing by 100 determines how many "
                                  'hundreds are in the dividend.</div></div>'},
                       {   'ans': 0,
                           'exp': '645 = (64 × 10) + 5. 64 full bags, 5 kg remaining.',
                           'hint': '645 ÷ 10 = 64 remainder 5.',
                           'options': [   '64 bags, 5 kg remaining',
                                          '60 bags, 45 kg remaining',
                                          '65 bags, 0 kg remaining',
                                          '640 bags, 5 kg remaining'],
                           'q': 'A warehouse has 645 kg of wheat. How many 10 kg bags can be filled completely, and '
                                'how many kg remain?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Divide total "
                                  "wheat by bag size: 645 ÷ 10.</li><li class='mb-2 text-slate-700 leading-relaxed'>64 "
                                  "× 10 = 640 kg.</li><li class='mb-2 text-slate-700 leading-relaxed'>645 - 640 = 5 kg "
                                  "left over.</li><li class='mb-2 text-slate-700 leading-relaxed'>Quotient = 64 bags, "
                                  "Remainder = 5 kg.</li></ol></div><div class='bg-amber-50 border-l-4 "
                                  'border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> Real-world packaging problems map "
                                  'directly to quotient and remainder.</div></div>'},
                       {   'ans': 1,
                           'exp': '12 × 3 = 36; 36 × 100 = 3,600.',
                           'hint': '12 × 3 = 36; then multiply by 100.',
                           'options': ['360', '3,600', '36,000', '1,230'],
                           'q': 'What is the product of 12 × 300?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Decompose 300 "
                                  "into 3 × 100.</li><li class='mb-2 text-slate-700 leading-relaxed'>12 × 3 = "
                                  "36.</li><li class='mb-2 text-slate-700 leading-relaxed'>36 × 100 = "
                                  "3,600.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'Factoring hundreds scales the single-digit product by two decimal '
                                  'places.</div></div>'},
                       {   'ans': 2,
                           'exp': '(7 × 14) + 3 = 98 + 3 = 101.',
                           'hint': 'Dividend = (Divisor × Quotient) + Remainder.',
                           'options': ['95', '98', '101', '105'],
                           'q': 'If a divisor is 7, the quotient is 14, and the remainder is 3, what is the dividend?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Apply formula: "
                                  "Dividend = (Divisor × Quotient) + Remainder.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>7 × 14 = 98.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>98 + 3 = 101.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Dividend = 101.</li></ol></div><div class='bg-amber-50 border-l-4 "
                                  'border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> The division formula is the "
                                  'universal proof check for long division.</div></div>'},
                       {   'ans': 1,
                           'exp': 'If remainder ≥ divisor, another full group can be subtracted into the quotient.',
                           'hint': 'If you have 8 items left and groups are size 8, you can make 1 more group!',
                           'options': [   'By random rule',
                                          'Because if the remainder were equal to or greater than the divisor, another '
                                          'group could be formed',
                                          'To save paper',
                                          'Because division only works on even numbers'],
                           'q': 'Why is the remainder in any division problem always strictly less than the divisor?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Division "
                                  "groups items into equal sets of size Divisor.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>If leftover items ≥ Divisor, at least one more full set can be "
                                  "formed.</li><li class='mb-2 text-slate-700 leading-relaxed'>Therefore, the final "
                                  'remainder must always be strictly less than the divisor.</li></ol></div><div '
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Remainder < Divisor "
                                  'is an inviolable law of integer arithmetic.</div></div>'},
                       {   'ans': 1,
                           'exp': '5 × 4 = 20; 20 × 1,000 = 20,000.',
                           'hint': '5 × 4 = 20, then attach three zeroes (two from 500, one from 40).',
                           'options': ['2,000', '20,000', '200,000', '4,500'],
                           'q': 'What is 500 × 40?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>5 × 4 = "
                                  "20.</li><li class='mb-2 text-slate-700 leading-relaxed'>500 has two zeroes; 40 has "
                                  "one zero (total 3 trailing zeroes).</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Append 3 zeroes to 20: 20,000.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Therefore, 500 × 40 = 20,000.</li></ol></div><div "
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Do not confuse the "
                                  'zero in 20 with the attached place-holding zeroes!</div></div>'}],
        'section': 'Long Division, Remainders & Scaling',
        'speech': '',
        'title': 'Challenge 3'},
    {   'id': 20,
        'quizzes': [   {   'ans': 0,
                           'exp': '400 + 50 + 20 + 10 + 5 = ₹485 using 5 notes/coins.',
                           'hint': 'Start with the largest denomination: ₹200 × 2 = ₹400.',
                           'options': [   '2 notes of ₹200 + 1 note of ₹50 + 1 note of ₹20 + 1 note of ₹10 + 1 coin of '
                                          '₹5',
                                          '4 notes of ₹100 + 8 notes of ₹10 + 5 coins of ₹1',
                                          '9 notes of ₹50 + 3 notes of ₹10 + 1 coin of ₹5',
                                          '1 note of ₹500 - ₹15 change'],
                           'q': 'A museum ticket buyer needs to pay ₹485. Which combination uses the fewest notes and '
                                'coins?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Highest "
                                  "denomination: 2 × ₹200 = ₹400 (leaves ₹85).</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Next denomination: 1 × ₹50 = ₹50 (leaves ₹35).</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>Next denomination: 1 × ₹20 = ₹20 (leaves "
                                  "₹15).</li><li class='mb-2 text-slate-700 leading-relaxed'>Next denomination: 1 × "
                                  "₹10 = ₹10 (leaves ₹5).</li><li class='mb-2 text-slate-700 leading-relaxed'>Final "
                                  "coin: 1 × ₹5 = ₹5 (balance zero).</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Total = ₹485 with only 5 currency units.</li></ol></div><div "
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Greedy denomination "
                                  'selection minimizes the physical count of notes and coins.</div></div>'},
                       {   'ans': 2,
                           'exp': '4 _ 5 with 4 + 5 = 9 gives 495.',
                           'hint': 'Split 4 and 5, insert (4 + 5 = 9) in the middle.',
                           'options': ['455', '485', '495', '505'],
                           'q': 'What is the product of 45 × 11 using the two-digit multiplication pattern?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>To multiply a "
                                  "two-digit number by 11:</li><li class='mb-2 text-slate-700 leading-relaxed'>Keep "
                                  "the hundreds digit as 4.</li><li class='mb-2 text-slate-700 leading-relaxed'>Keep "
                                  "the ones digit as 5.</li><li class='mb-2 text-slate-700 leading-relaxed'>The middle "
                                  "tens digit is the sum of the digits: 4 + 5 = 9.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Result: 495.</li></ol></div><div class='bg-amber-50 border-l-4 "
                                  'border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> Multiplying by 11 inserts the sum of "
                                  'digits between the original digits.</div></div>'},
                       {   'ans': 2,
                           'exp': '6 × 3 = 18; 4 × 5 = 20; 18 + 20 = 38 passengers.',
                           'hint': '(6 × 3) + (4 × 5).',
                           'options': ['32 passengers', '36 passengers', '38 passengers', '42 passengers'],
                           'q': 'What is the total passenger capacity of a fleet of 6 auto-rickshaws (3 passengers '
                                'each) and 4 cars (5 passengers each)?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Auto-rickshaws "
                                  "capacity = 6 × 3 = 18 passengers.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Passenger cars capacity = 4 × 5 = 20 passengers.</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>Total combined capacity = 18 + 20 = 38 "
                                  "passengers.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'Mixed fleet calculations sum the individual sub-fleet products.</div></div>'},
                       {   'ans': 2,
                           'exp': '5 × 70 = 350; 5 × 2 = 10; 350 + 10 = 360 passengers.',
                           'hint': '5 × 72 = (5 × 70) + (5 × 2).',
                           'options': ['340 passengers', '350 passengers', '360 passengers', '370 passengers'],
                           'q': 'If 1 train sleeper coach accommodates 72 passengers, how many passengers do 5 sleeper '
                                'coaches accommodate?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>5 × 70 = "
                                  "350.</li><li class='mb-2 text-slate-700 leading-relaxed'>5 × 2 = 10.</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>350 + 10 = 360 "
                                  "passengers.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'Long-distance train coaches offer massive passenger capacities per '
                                  'coach.</div></div>'},
                       {   'ans': 2,
                           'exp': '(5 × 200 = 1,000) + (6 × 50 = 300) = ₹1,300.',
                           'hint': '(5 × 200) + (6 × 50).',
                           'options': ['₹1,200', '₹1,250', '₹1,300', '₹1,350'],
                           'q': 'What is the total value of 5 notes of ₹200 and 6 notes of ₹50?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>5 × ₹200 = "
                                  "₹1,000.</li><li class='mb-2 text-slate-700 leading-relaxed'>6 × ₹50 = ₹300.</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>₹1,000 + ₹300 = "
                                  "₹1,300.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'Combining note bundles requires evaluating each denomination group before '
                                  'adding.</div></div>'},
                       {   'ans': 1,
                           'exp': '8 + 1 = 9. 81 is a multiple of 9 (9 × 9).',
                           'hint': '8 + 1 = 9.',
                           'options': ['73', '81', '92', '100'],
                           'q': 'Which number has a digital root (sum of digits) equal to 9?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Compute digit "
                                  "sums:</li><li class='mb-2 text-slate-700 leading-relaxed'>7 + 3 = 10 (1 + 0 = "
                                  "1).</li><li class='mb-2 text-slate-700 leading-relaxed'>8 + 1 = 9 (Multiple of "
                                  "9!).</li><li class='mb-2 text-slate-700 leading-relaxed'>9 + 2 = 11 (1 + 1 = "
                                  "2).</li><li class='mb-2 text-slate-700 leading-relaxed'>1 + 0 + 0 = "
                                  "1.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'All multiples of 9 reduce to a digital root of 9.</div></div>'},
                       {   'ans': 2,
                           'exp': '3 autos carry 9 people. 15 - 9 = 6 people, requiring 6 bicycles.',
                           'hint': '3 auto-rickshaws carry 3 × 3 = 9 people. Remaining = 15 - 9.',
                           'options': ['4 bicycles', '5 bicycles', '6 bicycles', '7 bicycles'],
                           'q': 'How many bicycles (carrying 1 person each) and auto-rickshaws (carrying 3 persons '
                                'each) are needed to carry 15 people if exactly 3 auto-rickshaws are used?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Auto capacity "
                                  "= 3 × 3 = 9 people.</li><li class='mb-2 text-slate-700 leading-relaxed'>Remaining "
                                  "people = 15 - 9 = 6 people.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Bicycle capacity = 1 person per bicycle.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>Bicycles needed = 6 ÷ 1 = 6 "
                                  "bicycles.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'Multi-modal vehicle matching uses subtraction and division to balance '
                                  'fleets.</div></div>'},
                       {   'ans': 1,
                           'exp': '72 = (7 × 10) + 2. Quotient 7, remainder 2.',
                           'hint': '7 × 10 = 70 with 2 left over.',
                           'options': ['6 remainder 12', '7 remainder 2', '7 remainder 0', '8 remainder 2'],
                           'q': 'What is 72 ÷ 10 expressed as a mixed quotient and remainder?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>70 contains "
                                  "exactly 7 tens.</li><li class='mb-2 text-slate-700 leading-relaxed'>72 - 70 = 2 "
                                  "units remainder.</li><li class='mb-2 text-slate-700 leading-relaxed'>Quotient = 7, "
                                  "Remainder = 2.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 "
                                  "p-3 rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key "
                                  'Takeaway:</strong> Dividing by 10 separates the tens digit from the ones remainder '
                                  'digit.</div></div>'},
                       {   'ans': 1,
                           'exp': '5 _ 2 with 5 + 2 = 7 gives 572.',
                           'hint': 'Split 5 and 2, insert (5 + 2 = 7) in the center.',
                           'options': ['562', '572', '582', '592'],
                           'q': 'What is the product of 52 × 11?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>First digit: "
                                  "5.</li><li class='mb-2 text-slate-700 leading-relaxed'>Last digit: 2.</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>Middle digit: 5 + 2 = 7.</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>Combined product: "
                                  "572.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'The 11s pattern enables rapid mental multiplication without carrying when sum < '
                                  '10.</div></div>'},
                       {   'ans': 2,
                           'exp': '3 × 18 = 54; 54 × 10 = 540 passengers.',
                           'hint': '3 × 180 = 3 × 18 × 10.',
                           'options': ['480 passengers', '520 passengers', '540 passengers', '560 passengers'],
                           'q': 'A museum hangar holds 3 transport aeroplanes seating 180 passengers each. What is the '
                                'total fleet capacity?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Number of "
                                  "aeroplanes = 3.</li><li class='mb-2 text-slate-700 leading-relaxed'>Seats per "
                                  "aeroplane = 180.</li><li class='mb-2 text-slate-700 leading-relaxed'>Total capacity "
                                  "= 3 × 180.</li><li class='mb-2 text-slate-700 leading-relaxed'>3 × 18 = 54.</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>54 × 10 = 540 "
                                  "passengers.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'Scaling aeroplane fleets demonstrates how commercial transit moves hundreds of '
                                  'citizens.</div></div>'}],
        'section': 'Denominations, Patterns & Fleet Matching',
        'speech': '',
        'title': 'Challenge 4'}]
