# update_c5m_ch1_spoken_full.py
"""
Updates spoken_text for Slides 1 to 16 with full, rich classroom lectures
spoken by an authentic Indian male teacher.
Maintains zero lecturer names, zero raw LaTeX, clean spoken mathematics.
"""

FULL_SPOKEN_TEXTS = {
    1: (
        "Welcome young mathematicians! Since the earliest days of human civilization, people have had an adventurous desire "
        "to travel, explore new lands, and trade with distant communities. In ancient times, the only way to travel was by walking "
        "on foot at a gentle pace of three to five kilometres per hour. Later, humans learned to domesticate animals like bullocks, "
        "horses, and camels, pulling wooden carts at four to five kilometres per hour, and building timber boats to cross rivers. "
        "But modern technology changed everything! Today, high-speed electric trains like the Vande Bharat glide across our country "
        "at one hundred sixty kilometres per hour. Commercial aeroplanes fly through the clouds at eight hundred fifty kilometres "
        "per hour, and spacecraft soar into orbit at a breathtaking speed of twenty-eight thousand kilometres per hour! When speeds "
        "and travel distances expanded from just ten kilometres to thousands and millions of kilometres, humans needed much larger "
        "numbers to count travellers, measure distances, calculate vehicle fuel, and chart transport networks. This is why we study "
        "numbers beyond thousands, entering the wondrous realm of ten thousand. Look at the timeline simulator on your screen, test "
        "the speeds of different eras, and observe how our world grew closer through the power of mathematics!"
    ),
    2: (
        "Let us understand how large numbers are born from smaller ones by looking at the base-ten building blocks. In primary school, "
        "you learned that ten single unit cubes bundle together to make one ten rod. Ten of these rods make one flat hundred square, "
        "and ten hundred squares stack together to form one solid thousand cube. Now, what happens when we continue this journey in "
        "thousands? Suppose you have nine thousand cubes, which is nine thousand. If you add one more thousand cube, you have ten "
        "thousand cubes. In our decimal number system, we never write ten digits in a single place value column. Instead, all ten "
        "thousand cubes bundle together to form a brand new, massive unit called Ten Thousand! We write ten thousand as one followed "
        "by four zeros: one, zero, zero, zero, zero. It is the smallest five-digit number in the world. Just one number before it is "
        "nine thousand nine hundred ninety-nine, which is the largest four-digit number. When we add one to nine thousand nine hundred "
        "ninety-nine, we arrive right at ten thousand! Use the interactive block counter to bundle thousands one by one and witness "
        "the birth of ten thousand!"
    ),
    3: (
        "Now let us examine the Indian Place Value Chart for five-digit numbers. Every five-digit number has five distinct columns, "
        "read from right to left: Ones, Tens, Hundreds, Thousands, and our new column, Ten Thousands, abbreviated as T, T, h. Each "
        "step to the left increases the value of a digit by ten times! For instance, a digit in the Ones column represents single "
        "units. In the Tens column, it is worth ten times as much. In the Hundreds column, it is worth a hundred times. In the "
        "Thousands column, a thousand times. And in the Ten Thousands column, that same digit is worth ten thousand times its face "
        "value! Consider the number thirty-four thousand two hundred eighty-five. The digit three sits in the Ten Thousands place, "
        "giving it a value of thirty thousand. The digit four is in the Thousands place, representing four thousand. The digit two "
        "is in the Hundreds place, worth two hundred. The digit eight in Tens is eighty, and five in Ones is five. In expanded form, "
        "we write it as thirty thousand, plus four thousand, plus two hundred, plus eighty, plus five. Click on each spike of the "
        "interactive abacus on your screen to add beads and watch the expanded form build up dynamically!"
    ),
    4: (
        "Reading and writing large numbers becomes effortless when we use periods and commas according to the Indian system of "
        "numeration. In our Indian system, the digits are grouped into families called periods. The first three digits from the "
        "right—Ones, Tens, and Hundreds—form the Ones Period. To the left of the Hundreds place, we place our very first comma! The "
        "next two digits—Thousands and Ten Thousands—form the Thousands Period. This comma acts as a natural speaking pause. When "
        "reading a number, we read all the digits in the Thousands period together, say the word thousand, pause at the comma, and "
        "then read the remaining three digits in the Ones period. For example, look at the number four, eight, comma, two, one, five. "
        "The digits four and eight are in the Thousands period, making forty-eight thousand. After the comma, two, one, five is read as "
        "two hundred fifteen. So the complete number name is forty-eight thousand two hundred fifteen! If there are zeros, such as seven, "
        "zero, comma, zero, zero, eight, we read it simply as seventy thousand eight. Try entering different five-digit numbers in the "
        "comma formatter on your screen and listen to how neatly they are spoken and written!"
    ),
    5: (
        "When planning travels and comparing journey logs, we often need to sort multi-digit numbers from smallest to greatest, which "
        "is ascending order, or from greatest to smallest, which is descending order. To compare two or more five-digit numbers, we "
        "follow a simple, golden rule: always compare the digits starting from the highest place value column, which is the Ten Thousands "
        "place! If the digits in the Ten Thousands place are different, the number with the greater digit is immediately the larger number. "
        "For instance, seventy-eight thousand two hundred is greater than thirty-four thousand five hundred because seven is greater "
        "than three. But what if the Ten Thousands digits are identical? Then we move one step to the right and compare the Thousands digits. "
        "If those are also equal, we compare the Hundreds digits, followed by Tens, and finally Ones. Look at the vehicle odometer logs "
        "on your screen. We have a delivery van at twelve thousand nine hundred kilometres, a car at thirty-four thousand five hundred, a "
        "bus at seventy-eight thousand two hundred, and a highway truck at ninety-five thousand four hundred. Use the sorting buttons to "
        "toggle between ascending and descending order, and notice how comparing the leftmost digits guarantees a correct ordering every single time!"
    ),
    6: (
        "Here is a captivating mathematical puzzle that reveals the true power of place values: what happens when you swap the positions "
        "of two digits in a large number? The face value of each digit remains the same, but because its place value changes, the entire "
        "number can increase or decrease dramatically! Let us investigate the odometer reading twenty-five thousand four hundred eighty. "
        "Here, the digit two is in the Ten Thousands place, worth twenty thousand, and the digit five is in the Thousands place, worth five "
        "thousand. Now, imagine swapping the two and the five! The new number becomes fifty-two thousand four hundred eighty. Notice what "
        "happened: the five is now in the Ten Thousands place, worth fifty thousand, while the two is in the Thousands place, worth two "
        "thousand. The new number is greater than the original by exactly twenty-seven thousand! Conversely, if you swap two digits where the "
        "smaller digit moves to a higher place, the total value drops. Test this on the interactive number shifter on your screen. Click the "
        "swap buttons, observe the place value transformations, and see how calculating the difference helps us solve real-world mathematical mystery puzzles!"
    ),
    7: (
        "In everyday travel, we frequently use approximate numbers instead of exact measurements. For example, if a bus has forty-eight "
        "passengers, we might say it has about fifty passengers. This practical skill is called rounding off! To round a number to the nearest "
        "ten, we imagine a number line marked in multiples of ten, such as forty and fifty. Picture a hungry rabbit standing at a position "
        "between forty and fifty. At forty, there is a bundle of carrots, and at fifty, there is another bundle. The rabbit naturally wants to "
        "hop to the nearest food! The decision depends entirely on the digit in the Ones column. If the Ones digit is one, two, three, or four, "
        "the number is closer to the lower ten, so we round down. For example, forty-three is closer to forty than to fifty, so forty-three rounds "
        "down to forty. But if the Ones digit is five, six, seven, eight, or nine, the number is closer to the higher ten, so we round up. When "
        "a number sits exactly in the middle with a five, such as forty-five, mathematical convention always rounds up to fifty! Drag the rabbit "
        "on your screen to different positions and observe how the Ones digit determines the nearest ten!"
    ),
    8: (
        "Now let us take our rounding skills to the highway and learn how to round off to the nearest hundred! Imagine driving along a long "
        "national highway where major milestone markers are placed every one hundred kilometres, such as at three hundred kilometres and four "
        "hundred kilometres. When we round to the nearest hundred, which digit holds the secret key? It is the digit in the Tens place! We examine "
        "the number formed by the last two digits: Tens and Ones. If the Tens digit is zero, one, two, three, or four—meaning the remaining "
        "value is between zero and forty-nine—the number is closer to the lower hundred, so we round down. For example, three hundred twenty-eight "
        "kilometres has a two in the Tens place. Because twenty-eight is less than fifty, three hundred twenty-eight rounds down to three hundred "
        "kilometres. However, if the Tens digit is five or more—meaning the remaining value is fifty to ninety-nine—we round up to the next hundred. "
        "For instance, three hundred fifty and three hundred seventy-two both round up to four hundred kilometres! Test this on the interactive "
        "highway car simulator by selecting different distances and watching the milestone marker snap to the nearest hundred!"
    ),
    9: (
        "When measuring long train journeys or aeroplane flights across India, we round distances to the nearest thousand! To round to the nearest "
        "thousand, we inspect the digit in the Hundreds place. If the Hundreds digit is five, six, seven, eight, or nine—meaning five hundred or "
        "more—we round up to the next thousand. If it is less than five, we round down. For example, two thousand eight hundred fifty rounds up to "
        "three thousand. Now, here is a brilliant mathematical curiosity that will make you think like a true mathematician: can rounding a number "
        "to the nearest hundred give the exact same milestone as rounding it to the nearest thousand? Yes, it can! Consider the number two thousand "
        "nine hundred eighty. When rounding to the nearest hundred, we look at the Tens digit, which is eight. Since eight is greater than five, "
        "two thousand nine hundred eighty rounds up to three thousand! Now round the same number, two thousand nine hundred eighty, to the nearest "
        "thousand: we look at the Hundreds digit, which is nine. Since nine is greater than five, it rounds up to three thousand as well! Both "
        "roundings land on three thousand! Use the dual-rounding analyzer on your screen to test numbers like four thousand nine hundred sixty and "
        "seven thousand nine hundred seventy-five, and explore this wonderful mathematical harmony!"
    ),
    10: (
        "Speed tells us how fast an object moves, measured as the distance covered in one hour, written as kilometres per hour or km/h. To calculate "
        "the total distance covered during any journey, we use the fundamental mathematical formula: Distance equals Speed multiplied by Time! For "
        "example, if a passenger train travels at a speed of eighty kilometres per hour for four hours, the total distance covered is eighty multiplied "
        "by four, which equals three hundred twenty kilometres. If you travel on a modern superfast train at one hundred twenty kilometres per hour "
        "for five hours, you cover one hundred twenty multiplied by five, which equals six hundred kilometres! Now think about an aeroplane flying at "
        "eight hundred kilometres per hour. In just three hours, it covers eight hundred multiplied by three, which equals two thousand four hundred "
        "kilometres, flying almost the entire length of India from north to south! And what about an orbital spacecraft flying at twenty-eight "
        "thousand kilometres per hour? In two hours, it covers an astounding fifty-six thousand kilometres, circling more than the entire circumference "
        "of Earth! Experiment with the interactive flight deck on your screen: select different vehicles, adjust the travel duration slider from one "
        "to twelve hours, and watch the distance formula calculate every journey in real time!"
    ),
    11: (
        "Planning a school excursion requires sharp mathematical thinking to ensure that every student and teacher has a comfortable seat without "
        "wasting money on empty vehicles! Imagine our school is organizing a field trip for one hundred thirty-five travellers. Standard school buses "
        "have fifty seats each, while smaller mini-vans have fifteen seats each. How many vehicles should the school hire? Let us divide! First, we "
        "divide one hundred thirty-five by fifty. Fifty goes into one hundred thirty-five two times, because fifty multiplied by two equals one "
        "hundred. This leaves a remainder of thirty-five passengers. So, the school books two large fifty-seater buses, carrying one hundred passengers. "
        "Now, what do we do with the remaining thirty-five passengers? We divide thirty-five by fifteen. Fifteen multiplied by two is thirty, which "
        "leaves five students without seats! We cannot leave anyone behind, so we must round up and book three mini-vans, which provide forty-five "
        "seats. Two large buses plus three mini-vans provide a total of one hundred forty-five seats, seating all one hundred thirty-five passengers "
        "safely with ten extra seats to spare! Slide the headcount slider on your screen from twenty to two hundred fifty passengers to see how mathematics "
        "dispatches the perfect fleet for every journey!"
    ),
    12: (
        "Large five-digit numbers are not just abstract symbols in a math textbook; they are all around us in the real world every single day! Think "
        "about the book you are reading right now. A complete Joyful Mathematics textbook contains approximately eighteen thousand four hundred fifty "
        "words. That is a five-digit number where one is in Ten Thousands, eight is in Thousands, four is in Hundreds, five is in Tens, and zero is in "
        "Ones. Now picture a grand international cricket stadium during a match: there are forty-two thousand five hundred spectators cheering in the "
        "stands, which means four ten-thousands, two thousands, and five hundreds! When forest officers protect wildlife reserves, they count twenty-five "
        "thousand six hundred eighty trees in a protected sanctuary. And when governments conduct a census, a small bustling town may have sixty-eight "
        "thousand nine hundred residents! Understanding five-digit numbers allows engineers to build bridges, doctors to order medicines, and city planners "
        "to supply clean water and electricity to thousands of families. Tap on the different real-world scenarios on your screen to inspect their place "
        "value breakdowns and see how mathematics measures the vibrant world around us!"
    ),
    13: (
        "During long journeys across our country, travellers historically shared riddles, brainteasers, and puzzles to pass the time and sharpen their "
        "wits. One of the most famous puzzles in mathematical folklore is the River Crossing Puzzle! A boatman arrives at the riverbank with a lion, a "
        "sheep, and a bundle of lush green grass. He must ferry all three across to the opposite bank. However, his small boat can carry only himself "
        "and one item at a time. Furthermore, he faces two strict danger rules: if left alone together on either bank without the boatman, the lion will "
        "eat the sheep, and the sheep will eat the grass! How can he transport all three safely? The secret lies in a clever seven-step sequence! First, "
        "the boatman takes the sheep across, because the lion does not eat grass. Leaving the sheep on the far bank, he returns alone. Next, he takes "
        "the lion across. But to prevent the lion from eating the sheep, he brings the sheep BACK to the starting bank! Then, he leaves the sheep and "
        "takes the grass across to join the lion. Finally, he returns empty-handed to fetch the sheep one last time! Play this puzzle on your screen, "
        "test your logical deductions, and experience the joy of mathematical problem solving!"
    ),
    14: (
        "Here is another timeless pastime played by travellers under the shade of banyan trees: the Strategic Pile of Pebbles Game! Two players sit "
        "beside a pile of fifteen pebbles. On each turn, a player may take one, two, or three pebbles from the pile. The player who picks up the very "
        "last pebble wins the game! Can you guarantee a win every single time? Yes, if you understand the mathematics of multiples of four! Notice "
        "that whatever number of pebbles your opponent takes—whether one, two, or three—you can always take enough pebbles so that the sum of both "
        "turns equals four! For example, if they take one, you take three. If they take two, you take two. If they take three, you take one. In every "
        "round, the pile decreases by exactly four pebbles! Since fifteen divided by four equals three with a remainder of three, the winning strategy "
        "is clear: on your very first turn, take exactly three pebbles! This leaves twelve pebbles, which is a multiple of four. From that moment on, "
        "whenever your opponent takes N pebbles, you take four minus N pebbles, ensuring you leave eight, then four, and finally take the last pebbles "
        "to victory! Challenge the computer on your screen and master the multiple-of-four strategy!"
    ),
    15: (
        "Let us explore a delightful piece of number magic discovered by Indian mathematicians, including the legendary D. R. Kaprekar! Think of any "
        "two different digits, say eight and three. Use them to form a two-digit number: eighty-three. Now, reverse the digits to form thirty-eight. Next, "
        "subtract the smaller number from the larger number: eighty-three minus thirty-eight equals forty-five. Now examine forty-five: forty-five is a "
        "multiple of nine, because nine multiplied by five is forty-five! What is truly extraordinary is that the difference between the original "
        "digits, eight minus three, is five, and the answer is nine multiplied by five! Try it with any two digits you choose, like nine and two. "
        "Ninety-two minus twenty-nine is sixty-three, which is nine multiplied by seven, and nine minus two is seven! Why does this always work? Algebra "
        "gives us the beautiful proof: any two-digit number with tens digit a and ones digit b has the value ten a plus b. Its reverse is ten b plus a. "
        "When you subtract them, ten a minus a is nine a, and b minus ten b is minus nine b. This simplifies to nine times the quantity a minus b! It "
        "must always be a multiple of nine! Test different digits on the interactive engine and watch the magic of nine unfold!"
    ),
    16: (
        "Our final journey puzzle is the legendary King's Horses Stable Trick! A king kept twenty fine horses in a square stable arranged in a three-by-three "
        "grid with an open courtyard in the middle. The king was very particular: every evening, he inspected the stable by counting the horses along each "
        "of the four outer sides, making sure that each side had exactly five horses! One day, a clever caretaker secretly sold two horses, leaving only "
        "eighteen horses. Yet, when the king counted all four sides that evening, he still counted five horses on every single side, without suspecting a "
        "thing! How did the caretaker pull off this trick? By using the mathematics of corner sharing! When a horse is placed in a corner room, it touches "
        "two different sides of the stable, so it is counted twice! If there are five horses in each side, the king calculates four times five, which is "
        "twenty. But the actual total number of horses is twenty minus C, where C is the number of horses placed in the four corners! By placing one horse "
        "in each of two corners, and adjusting the middle rooms, the caretaker made eighteen horses sum to five on all four sides! Explore the three "
        "stable configurations on your screen, verify each side sum, and discover the mathematical secret of corner sharing!"
    )
}

# Update generate_c5m_ch1_part1.py
import re

with open('.agents/generate_c5m_ch1_part1.py', 'r', encoding='utf-8') as f:
    part1_code = f.read()

from generate_c5m_ch1_part1 import SLIDES_PART1
for s in SLIDES_PART1:
    sid = s['id']
    if sid in FULL_SPOKEN_TEXTS:
        s['spoken_text'] = FULL_SPOKEN_TEXTS[sid]

with open('.agents/generate_c5m_ch1_part1.py', 'w', encoding='utf-8') as f:
    f.write('"""\nGenerate Slides 1 to 8 for NCERT Class 5 Mathematics Chapter 1: We the Travellers - I\nJoyful Mathematics curriculum (NEP 2020).\nZero raw LaTeX! Clean Unicode symbols.\n"""\n\n')
    f.write('SLIDES_PART1 = ' + repr(SLIDES_PART1) + '\n')

print("Updated generate_c5m_ch1_part1.py successfully.")

# Update generate_c5m_ch1_part2.py
from generate_c5m_ch1_part2 import SLIDES_PART2
for s in SLIDES_PART2:
    sid = s['id']
    if sid in FULL_SPOKEN_TEXTS:
        s['spoken_text'] = FULL_SPOKEN_TEXTS[sid]

with open('.agents/generate_c5m_ch1_part2.py', 'w', encoding='utf-8') as f:
    f.write('"""\nGenerate Slides 9 to 16 for NCERT Class 5 Mathematics Chapter 1: We the Travellers - I\nJoyful Mathematics curriculum (NEP 2020).\nZero raw LaTeX! Clean Unicode symbols.\n"""\n\n')
    f.write('SLIDES_PART2 = ' + repr(SLIDES_PART2) + '\n')

print("Updated generate_c5m_ch1_part2.py successfully.")

