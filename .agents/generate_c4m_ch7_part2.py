# -*- coding: utf-8 -*-
"""Class 4 Mathematics Chapter 7 Part 2 Slides (9-16)"""

slides_part2 = [
    {
        "id": 9,
        "title": 'Traditional Snack Expenses',
        "section": 'Local Food Calculations & Savings Additions',
        "speech": 'During the village excursion, travelers stop at a charming roadside tea stall to savor authentic regional delicacies. A popular treat in this scenic hill region is pusaw, a traditional steamed cake prepared from hill-grown red rice. One traveler orders a large plate of warm pusaw costing thirty-eight rupees along with a cup of aromatic spiced hill tea costing sixteen rupees. To determine the combined expense, we perform column addition. In the Ones column, eight plus six equals fourteen Ones; we write four in the Ones place and carry one Ten into the Tens column. In the Tens column, one carried Ten plus three plus one yields five Tens, establishing an exact snack bill of fifty-four rupees. Later, the young traveler reviews personal piggy bank savings gathered over several months before the trip. One pocket contains one hundred eighty-five rupees while an auxiliary savings pouch holds one hundred twenty-five rupees. Adding five and five in the Ones gives ten (write zero, carry one); one carried Ten plus eight plus two equals eleven Tens (write one, carry one Hundred); and one carried Hundred plus one plus one equals three Hundreds, totaling three hundred ten rupees saved! Calculating food expenses and tracking personal savings teaches financial responsibility, sharpens across our diverse, beautiful nation.',
        "checkpoints": [
            {
                "q": 'What is the total cost of a plate of pusaw (₹38) and spiced hill tea (₹16)?',
                "options": ['₹48', '₹52', '₹54', '₹56'],
                "ans": 2,
                "exp": '8 + 6 = 14 (write 4, carry 1); 1 + 3 + 1 = 5 Tens; total = ₹54.'
            },
            {
                "q": 'Combining savings of ₹185 and ₹125 yields what total amount?',
                "options": ['₹300', '₹310', '₹320', '₹410'],
                "ans": 1,
                "exp": '185 + 125: 5+5=10 (carry 1); 1+8+2=11 (carry 1); 1+1+1=3 Hundreds -> ₹310.'
            },
        ]
    },
    {
        "id": 10,
        "title": 'Snack Choice Differences',
        "section": 'Comparative Subtraction & Quantity Discrepancies',
        "speech": 'When a large group makes decisions during a community meal, comparing different preferences introduces the concept of mathematical difference through subtraction. At the village lunch pavilion, eighty-three children select traditional steamed pusaw cakes, while forty-six children choose fresh fruit plates featuring sliced papaya and bananas. How many more students preferred the traditional steamed cakes over fruit plates? To solve this comparative inquiry, we subtract forty-six from eighty-three. Notice that in the Ones place, we cannot take six Ones away from three Ones because three is smaller than six. We must regroup by taking one Ten from the eight Tens, leaving seven Tens in the Tens place, and converting that borrowed Ten into ten single Ones. Combining ten Ones with our existing three Ones produces thirteen Ones. Now, subtracting six from thirteen leaves seven in the Ones column. In the Tens column, subtracting four Tens from the remaining seven Tens leaves three Tens. The final difference is thirty-seven children! Subtraction answers how much greater one quantity is compared to another. Whether evaluating snack choices, survey tallies, or attendance figures, difference subtraction enables analysts to interpret group choices, understand student preferences, and plan future events with great precision and numerical confidence.',
        "checkpoints": [
            {
                "q": 'If 83 children chose pusaw and 46 chose fruit plates, how many more chose pusaw?',
                "options": ['27', '33', '37', '43'],
                "ans": 2,
                "exp": '83 - 46: Borrow 1 Ten to make 13 Ones; 13 - 6 = 7; 7 Tens - 4 Tens = 3 Tens -> 37.'
            },
            {
                "q": 'Why was regrouping necessary when subtracting 46 from 83?',
                "options": ['Because 8 is larger than 4', 'Because the top Ones digit (3) is smaller than the bottom Ones digit (6)', 'Because both numbers are even', 'Because subtraction always requires borrowing'],
                "ans": 1,
                "exp": 'In the Ones place, 3 is less than 6, requiring 1 Ten to be unbundled into 10 Ones.'
            },
        ]
    },
    {
        "id": 11,
        "title": 'Regrouping In Subtraction',
        "section": 'Decomposing Place Value Bundles (Tens & Hundreds)',
        "speech": 'Mastering multi-digit subtraction requires understanding the reverse process of base-ten bundling, known as borrowing or decomposition. When adding numbers, ten smaller units combine into one larger unit; when subtracting, one larger unit is unbundled into ten smaller units whenever the minuend digit is smaller than the subtrahend digit. Consider subtracting one hundred seventy-six from three hundred twenty-four. We write three hundred twenty-four on top and one hundred seventy-six below it, aligning columns carefully. In the Ones column, four is smaller than six, so we borrow one Ten from the Tens column. The two Tens reduce to one Ten, while the four Ones become fourteen Ones. Subtracting six from fourteen gives eight Ones. Moving to the Tens column, we must subtract seven Tens from the remaining one Ten. Since one is smaller than seven, we borrow one Hundred from the Hundreds column! The three Hundreds reduce to two Hundreds, and the one borrowed Hundred converts into ten Tens, giving eleven Tens. Subtracting seven from eleven yields four Tens. Finally, in the Hundreds column, two minus one leaves one Hundred. The difference is one hundred forty-eight! Concrete block decomposition proves that numbers merely reorganize across place value columns while keeping their overall value constant.',
        "checkpoints": [
            {
                "q": 'When subtracting 176 from 324, what is the resulting difference?',
                "options": ['138', '148', '158', '248'],
                "ans": 1,
                "exp": '324 - 176: 14 - 6 = 8 Ones; 11 - 7 = 4 Tens; 2 - 1 = 1 Hundred -> 148.'
            },
            {
                "q": 'When 1 Hundred is borrowed into the Tens column, how many Tens does it provide?',
                "options": ['1 Ten', '5 Tens', '10 Tens', '100 Tens'],
                "ans": 2,
                "exp": '1 Hundred equals 10 Tens, so borrowing 1 Hundred adds 10 to the existing Tens.'
            },
        ]
    },
    {
        "id": 12,
        "title": 'Travel Spend Balances',
        "section": 'Spend-Down Accounting & Harvest Comparisons',
        "speech": 'Tracking expenditures throughout an educational excursion provides excellent real-world practice in spend-down subtraction and budget management. Suppose a student starts the field trip day with a total pocket allowance of three hundred ten rupees. After purchasing bus snacks, handmade bamboo souvenirs, and admission tickets, the student counts the cash remaining in their wallet and finds exactly one hundred seventy-nine rupees left. How much money was spent during the day? We subtract the remaining balance of one hundred seventy-nine from the initial three hundred ten rupees. In the Ones place, zero cannot subtract nine, so borrowing one Ten leaves zero Tens and creates ten Ones; ten minus nine is one One. In the Tens place, zero cannot subtract seven, so borrowing one Hundred leaves two Hundreds and creates ten Tens; ten minus seven is three Tens. In the Hundreds place, two minus one leaves one Hundred. The total expenditure was one hundred thirty-one rupees! Similarly, farmers compare crop yields between seasons using subtraction: if an orchard produced five hundred twenty kilograms of sweet mangoes last year and four hundred fifteen kilograms this year, subtracting reveals a decrease of one hundred five kilograms. Consistent financial record-keeping ensures travelers maintain control over their budgets responsibly.',
        "checkpoints": [
            {
                "q": 'Starting with ₹310 and having ₹179 remaining, how much money was spent?',
                "options": ['₹121', '₹131', '₹141', '₹231'],
                "ans": 1,
                "exp": '₹310 - ₹179: 10 - 9 = 1; 10 - 7 = 3; 2 - 1 = 1 -> ₹131 spent.'
            },
            {
                "q": 'What is the difference between an orchard yield of 520 kg and 415 kg?',
                "options": ['95 kg', '105 kg', '115 kg', '205 kg'],
                "ans": 1,
                "exp": '520 - 415: 10 - 5 = 5; 1 - 1 = 0; 5 - 4 = 1 -> 105 kg difference.'
            },
        ]
    },
    {
        "id": 13,
        "title": 'Train Passenger Tracking',
        "section": 'Sequential Multi-Station Boarding & Alighting Arithmetic',
        "speech": 'A fascinating application of combined addition and subtraction occurs when tracking passenger occupancy aboard an intercity express train across several sequential railway junctions. Imagine an express train departing New Delhi with six hundred forty-two passengers aboard. At the first intermediate stop in Dadri, eighty-five passengers alight from the train while one hundred fourteen new passengers board. To find the new occupancy, we first subtract the departing travelers: six hundred forty-two minus eighty-five leaves five hundred fifty-seven passengers. Next, we add the newly boarded travelers: five hundred fifty-seven plus one hundred fourteen equals six hundred seventy-one passengers on board. As the train pulls into Ghaziabad junction, ninety-six passengers step off onto the platform, and sixty-two travelers step aboard. Subtracting ninety-six from six hundred seventy-one yields five hundred seventy-five, and adding sixty-two brings the count to six hundred thirty-seven. Finally, approaching Aligarh, forty-five passengers disembark. Subtracting forty-five from six hundred thirty-seven leaves five hundred ninety-two travelers arriving at the final terminal! Dynamic tracking problems demonstrate that arithmetic in real life is rarely a single isolated calculation, but rather an ongoing sequence of adjustments where each answer forms the starting point for the next operational step. This builds thorough operational tracking competence.',
        "checkpoints": [
            {
                "q": 'If a train starts with 642 passengers, 85 get off, and 114 board, how many are now on board?',
                "options": ['661', '671', '681', '691'],
                "ans": 1,
                "exp": '642 - 85 = 557; 557 + 114 = 671 passengers.'
            },
            {
                "q": 'From 671 passengers, if 96 get off and 62 board, what is the updated occupancy?',
                "options": ['627', '635', '637', '647'],
                "ans": 2,
                "exp": '671 - 96 = 575; 575 + 62 = 637 passengers.'
            },
        ]
    },
    {
        "id": 14,
        "title": 'Mental Math Shortcuts',
        "section": 'Near-Tens Adjustments & Compensation Strategies',
        "speech": 'Skilled mental calculators rarely perform slow, mechanical column paper calculations when clever mathematical shortcuts allow near-instant computation. One of the most powerful strategies involves adjusting numbers to their nearest tens or hundreds, a technique known as compensation. For example, suppose you must add ninety-nine to three hundred fifty-six. Instead of adding nine twice with carries, recognize that ninety-nine is just one less than one hundred! First, add one hundred to three hundred fifty-six, which effortlessly gives four hundred fifty-six. Then, compensate by subtracting the extra one we added, arriving instantly at four hundred fifty-five! Similarly, when subtracting near-tens, suppose you need to subtract forty-nine from two hundred eighty. Subtracting fifty is simple: two hundred eighty minus fifty gives two hundred thirty. Because we subtracted one too many, we add one back, yielding two hundred thirty-one! Another quick strategy involves breaking numbers into expanded form: adding forty-five and thirty-two is simply forty plus thirty equaling seventy, plus five plus two equaling seven, producing seventy-seven without paper. Mental math strategies develop deep mathematical agility, save precious time during problem-solving, and transform arithmetic into a playful, joyful puzzle. Practicing shortcuts regularly enhances everyday mental calculations and unlocks deep intuitive mastery.',
        "checkpoints": [
            {
                "q": 'What is the mental math shortcut to add 99 to 356?',
                "options": ['Add 90 and subtract 9', 'Add 100 and subtract 1', 'Add 100 and add 1', 'Double 356 and divide by 2'],
                "ans": 1,
                "exp": '99 = 100 - 1. Adding 100 gives 456; subtracting 1 yields 455.'
            },
            {
                "q": 'Using mental compensation, what is 280 - 49?',
                "options": ['229', '230', '231', '241'],
                "ans": 2,
                "exp": '280 - 50 = 230; add back 1 because 49 is 1 less than 50 -> 231.'
            },
        ]
    },
    {
        "id": 15,
        "title": 'Number Target Equations',
        "section": 'Decomposing Target Sums & Invariant Differences',
        "speech": 'Mathematics reveals that a single target number can be formed through infinitely many different numerical expressions, deepening our understanding of equality and number relationships. Consider the target sum of eight hundred fifty-six. Can we find multiple pairs of numbers that add together to produce exactly eight hundred fifty-six? We can decompose this target by splitting place values: eight hundred plus fifty-six equals eight hundred fifty-six; seven hundred plus one hundred fifty-six equals eight hundred fifty-six; five hundred plus three hundred fifty-six equals eight hundred fifty-six; and even eight hundred fifty plus six equals eight hundred fifty-six! Next, consider creating a target difference of five hundred sixty-three through subtraction. We can start with six hundred and subtract thirty-seven to obtain five hundred sixty-three, or start with seven hundred sixty-three and subtract two hundred, or take eight hundred and subtract two hundred thirty-seven. Notice the constant difference principle: if we increase both numbers in a subtraction expression by the exact same amount, their difference remains completely unchanged! Deconstructing numbers into diverse additive and subtractive components fosters flexible algebraic thinking, prepares students for advanced algebra, and proves that numbers are versatile, flexible building blocks in mathematics. Flexible numbers unlock creative mathematical problem-solving.',
        "checkpoints": [
            {
                "q": 'Which pair of numbers adds up to the target sum of 856?',
                "options": ['500 + 356', '600 + 246', '700 + 166', '800 + 46'],
                "ans": 0,
                "exp": '500 + 356 = 856 exact target sum.'
            },
            {
                "q": 'Which subtraction expression yields the target difference of 563?',
                "options": ['763 - 100', '763 - 200', '863 - 200', '663 - 200'],
                "ans": 1,
                "exp": '763 - 200 = 563 exact target difference.'
            },
        ]
    },
    {
        "id": 16,
        "title": 'Number Grid Pairs',
        "section": 'Spatial Matrix Operations & Missing Digit Logic',
        "speech": 'Our mathematical adventure culminates in an engaging spatial puzzle called the Number Pair Hunt Grid! Students are presented with a four-by-four grid filled with two-digit and three-digit numbers. The challenge tasks players with analyzing horizontally and vertically adjacent number pairs to discover the pair that produces the greatest sum, the smallest sum, the greatest difference, or the smallest difference. To find the greatest sum quickly, sharp mathematicians scan the matrix for the two largest neighboring numbers, such as eighty-seven adjacent to ninety-four, adding them to achieve one hundred eighty-one. Conversely, to find the smallest difference, they look for two neighboring cells containing numbers closest in numerical value, such as fifty-two next to fifty-five, which yields a tiny difference of only three! A related mathematical drill involves solving missing digit puzzles, where ink smudges erase digits from column addition or subtraction problems. By reasoning backward from known totals using inverse operations, students deduce the missing numbers with detective-like precision. Exploring numbers arranged in two-dimensional grids sharpens pattern recognition, strengthens mental estimation, and celebrates the joyful, practical harmony of addition and subtraction operations across all our everyday classroom learning adventures. Grid puzzles foster keen spatial observation, logical reasoning, and enthusiasm.',
        "checkpoints": [
            {
                "q": 'If two adjacent cells in a grid contain 87 and 94, what is their sum?',
                "options": ['171', '181', '191', '201'],
                "ans": 1,
                "exp": '87 + 94 = 181.'
            },
            {
                "q": 'If neighboring cells contain 55 and 52, what is their difference?',
                "options": ['2', '3', '7', '107'],
                "ans": 1,
                "exp": '55 - 52 = 3 difference.'
            },
        ]
    },
]
