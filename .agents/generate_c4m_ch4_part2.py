# -*- coding: utf-8 -*-
"""
Generate Slides 9 to 16 for Class 4 Maths Chapter 4: Thousands Around Us
Calibrated strictly to 195-215 words per speech.
"""

def get_part2_slides():
    return [
        {
            "id": 9,
            "title": "Decomposing One Thousand",
            "section": "Let Us Break Up One-Thousand",
            "speech": (
                "One thousand is a majestic milestone number with fascinating additive properties. Just as ten decomposes into smaller pairs like seven and three, "
                "one thousand can be split into complementary parts that sum to one thousand. On a number line from zero to one thousand, "
                "we can observe these additive complements visually. For example, starting at nine hundred, we need exactly one hundred more "
                "to reach one thousand. Starting at eight hundred fifty, adding one hundred fifty brings us to one thousand. "
                "Subtraction mirrors this balance: if you have one thousand and take away six hundred, four hundred remains. "
                "Now consider a colorful puzzle shaped like segmented orange slices. In each slice, two numbers combine to complete the full fruit "
                "of one thousand. If one segment contains six hundred seventy, its complementary slice must be three hundred thirty. "
                "If another segment holds eight hundred thirty, its partner is one hundred seventy. What if a segment holds four hundred ninety-seven? "
                "To reach one thousand, we add three to reach five hundred, and then five hundred more, giving five hundred three! "
                "Decomposing one thousand builds strong mental math fluency and prepares us for efficient multi-digit addition and subtraction. "
                "Use the interactive orange slice puzzle below to rotate segments and discover missing complements that complete one thousand."
            ),
            "checkpoints": [
                {
                    "q": "What is the missing complement in the equation: 850 + ___ = 1000?",
                    "options": ["100", "150", "200", "250"],
                    "ans": 1,
                    "exp": "1000 - 850 = 150. Therefore, 850 + 150 = 1000."
                },
                {
                    "q": "What number completes the orange slice puzzle for 497 to reach 1000?",
                    "options": ["503", "513", "597", "603"],
                    "ans": 0,
                    "exp": "497 + 3 = 500, and 500 + 500 = 1000. So the missing complement is 500 + 3 = 503."
                }
            ]
        },
        {
            "id": 10,
            "title": "Regrouping Place Values",
            "section": "Grouping and Regrouping",
            "speech": (
                "In our decimal place-value system, no column can ever hold ten or more units without bundling into the next higher place. "
                "Whenever we accumulate ten or more items in any column, we must regroup. Let us observe loose units turning into structured bundles. "
                "Suppose you have one ten and twenty-seven loose ones. Twenty-seven ones can be grouped into two tens and seven loose ones. "
                "Combining the two new tens with the existing one ten gives three tens and seven ones, which equals thirty-seven. "
                "Now imagine a collection of ten tens and six ones. Ten tens bundle directly into one complete hundred! "
                "With zero tens left over, this collection represents one hundred, zero tens, and six ones, written as one hundred six. "
                "What if you have eleven tens and fourteen ones? Fourteen ones regroup into one ten and four ones. "
                "Adding that extra ten to eleven tens gives twelve tens. Twelve tens regroup into one hundred and two tens! "
                "Combining everything yields one hundred twenty-four. Similarly, thirty-five tens simply represents three hundred fifty. "
                "Mastering regrouping allows us to convert unorganized collections of tokens into clean, standard numerical notation effortlessly. "
                "Step into the interactive regrouping laboratory below to bundle loose tokens and watch them promote automatically into higher columns."
            ),
            "checkpoints": [
                {
                    "q": "What standard number is represented by 10 Tens + 6 Ones?",
                    "options": ["16", "106", "160", "1006"],
                    "ans": 1,
                    "exp": "10 Tens = 1 Hundred (100). Adding 6 Ones gives 100 + 6 = 106."
                },
                {
                    "q": "Convert 35 Tens into standard numerical form:",
                    "options": ["35", "305", "350", "3500"],
                    "ans": 2,
                    "exp": "35 Tens = 35 × 10 = 350 (or 3 Hundreds and 5 Tens)."
                }
            ]
        },
        {
            "id": 11,
            "title": "Color Token Model",
            "section": "Numbers Beyond 1000 (One Thousand)",
            "speech": (
                "Carrying hundreds of wooden base-ten blocks around the classroom can be cumbersome. To represent large four-digit numbers compactly, "
                "we use lightweight, color-coded circular tokens. Each color represents a specific place value: green tokens represent ones, "
                "yellow tokens represent tens, red tokens represent hundreds, and large blue tokens represent thousands. "
                "Suppose we place three blue thousand-tokens, zero red hundred-tokens, one yellow ten-token, and nine green one-tokens on our counting mat. "
                "To read this number, we write its expanded form: three thousand plus zero plus ten plus nine. Combining these values produces "
                "the standard four-digit numeral three thousand nineteen, written as three, zero, one, nine. Notice that although there are zero hundreds, "
                "the zero digit must be recorded in the hundreds column to keep three in the thousands place. "
                "Token models also make tracing sequential four-digit numbers easy, such as counting from one thousand twenty-seven up to one thousand thirty-four, "
                "or stepping across thousands from two thousand eight to two thousand nine and two thousand ten. "
                "Color-coded tokens provide an organized visual bridge between physical counting and abstract four-digit numbers. "
                "Experiment on the interactive token board below to drop colored tokens and generate expanded addition statements instantly."
            ),
            "checkpoints": [
                {
                    "q": "What standard number is formed by 3 Thousands, 0 Hundreds, 1 Ten, and 9 Ones?",
                    "options": ["319", "3019", "3109", "30019"],
                    "ans": 1,
                    "exp": "3 Thousands (3000) + 0 Hundreds (0) + 1 Ten (10) + 9 Ones (9) = 3019."
                },
                {
                    "q": "What is the expanded form of the number 4508?",
                    "options": ["400 + 50 + 8", "4000 + 50 + 8", "4000 + 500 + 0 + 8", "4000 + 500 + 80"],
                    "ans": 2,
                    "exp": "4508 expands to 4000 + 500 + 0 + 8 (4 Thousands, 5 Hundreds, 0 Tens, 8 Ones)."
                }
            ]
        },
        {
            "id": 12,
            "title": "Place Value Slider",
            "section": "Let Us Play (Place Value Slider & Error Identification)",
            "speech": (
                "A wonderful hands-on tool for exploring multi-digit numbers is the place value slider. Made with sliding paper strips, "
                "this mechanism allows young mathematicians to adjust individual digit columns independently while observing the overall numerical change. "
                "Suppose your slider displays the number one thousand eight hundred ninety-five. If you increment the ones slider by one, "
                "the five becomes a six, giving one thousand eight hundred ninety-six. What if you add twenty? Adding two to the tens place causes "
                "ninety plus twenty to equal one hundred ten, triggering a carry-over into the hundreds column and turning eight hundred into nine hundred! "
                "The slider also helps us avoid a very common student mistake: omitting zero as a placeholder. Imagine being asked to write "
                "seven thousands, zero hundreds, two tens, and four ones. An untrained student might ignore the zero hundreds and write seven, two, four, "
                "producing seven hundred twenty-four. That is completely incorrect, because seven hundred twenty-four is a three-digit number! "
                "Zero must be written in the hundreds place: seven, zero, two, four, representing seven thousand twenty-four. "
                "Zero is not nothing; zero is a vigilant guardian that preserves the true value of its neighbor digits. "
                "Use the interactive place value slider below to adjust digits and test carry-over mechanics."
            ),
            "checkpoints": [
                {
                    "q": "How should '7 Thousands, 0 Hundreds, 2 Tens, and 4 Ones' be written in standard numeral form?",
                    "options": ["724", "7024", "7204", "70024"],
                    "ans": 1,
                    "exp": "Zero must hold the Hundreds place: 7 in Thousands, 0 in Hundreds, 2 in Tens, 4 in Ones = 7024."
                },
                {
                    "q": "If you increase the tens digit of 6487 by 2 tens (adding 20), what is the new number?",
                    "options": ["6489", "6497", "6507", "6687"],
                    "ans": 2,
                    "exp": "6487 + 20 = 6507 (80 + 20 = 100, which carries over into the Hundreds place)."
                }
            ]
        },
        {
            "id": 13,
            "title": "Four-Digit Number Scale",
            "section": "Number Line (4-Digit Scale)",
            "speech": (
                "As numbers grow into the thousands, number lines require calibrated scales so we can plot values accurately without running off the page. "
                "Instead of drawing a single endless line, mathematicians zoom into specific segmented ranges. "
                "Consider a scale stretching from one thousand to one thousand one hundred, divided into ten equal tick intervals of ten units each. "
                "Here, one thousand twenty sits two ticks past one thousand, while one thousand fifty sits squarely in the middle. "
                "On a broader scale from two thousand to two thousand five hundred, marked in intervals of fifty, two thousand two hundred fifty "
                "sits at the exact midpoint. Number lines also allow range filtering. Suppose you must identify all numbers that lie strictly between "
                "two thousand two hundred twenty-six and three thousand two hundred twenty-six. You simply locate both boundary points and select "
                "any value positioned between them, such as two thousand five hundred or three thousand. "
                "Observing intervals like five thousand five hundred to five thousand seven hundred, or eight thousand five hundred to nine thousand, "
                "develops our spatial sense of numerical scale and distance. "
                "Step into the interactive multi-scale number line below, zoom between different thousand intervals, and plot target values with precision."
            ),
            "checkpoints": [
                {
                    "q": "Which of the following numbers lies strictly between 2226 and 3226 on the number line?",
                    "options": ["2190", "2850", "3250", "3500"],
                    "ans": 1,
                    "exp": "2850 is greater than 2226 and less than 3226, so it falls strictly inside the range."
                },
                {
                    "q": "On a number line from 1000 to 1100, what number sits at the exact midpoint?",
                    "options": ["1025", "1050", "1075", "1090"],
                    "ans": 1,
                    "exp": "The midpoint of 1000 and 1100 is: 1000 + (100 ÷ 2) = 1050."
                }
            ]
        },
        {
            "id": 14,
            "title": "Overlapping Arrow Cards",
            "section": "Let Us Play (Arrow Cards & Find Me Grid)",
            "speech": (
                "Arrow cards are an ingenious visual device that makes expanded form completely tangible. Each arrow card is cut with a pointed tip on the right, "
                "printed in graduated widths corresponding to place values. Thousands cards are four digits wide, hundreds cards are three digits wide, "
                "tens cards are two digits wide, and ones cards are a single digit wide. When we take the card for three thousand, layer the four hundred card "
                "over its right zeroes, place the fifty card over the tens, and cap it with the two card, the cards overlap neatly to display "
                "the complete number: three thousand four hundred fifty-two! If you pull the arrow cards apart, the hidden expanded form is instantly revealed: "
                "three thousand plus four hundred plus fifty plus two. Arrow cards physically demonstrate how standard numerals conceal expanded additive layers. "
                "This insight helps us solve Find Me Grid visual puzzles, where clues challenge you to search a matrix for the smallest four-digit number, "
                "a value matching specific dice faces, or a number lying between five thousand and five thousand two hundred. "
                "Try layering and pulling apart arrow cards in the interactive workshop below to see expanded forms assemble and disassemble before your eyes."
            ),
            "checkpoints": [
                {
                    "q": "Which 4 arrow cards are layered together to form the number 3452?",
                    "options": ["3000, 400, 50, 2", "300, 40, 5, 2", "3000, 40, 50, 2", "3400, 50, 2"],
                    "ans": 0,
                    "exp": "3452 is composed of 3000 + 400 + 50 + 2 layered by place value."
                },
                {
                    "q": "In a Find Me Grid, which number satisfies the clue: 'Between 5000 and 5200'?",
                    "options": ["4950", "5120", "5250", "5500"],
                    "ans": 1,
                    "exp": "5120 is strictly greater than 5000 and less than 5200."
                }
            ]
        },
        {
            "id": 15,
            "title": "Comparing Place Values",
            "section": "Comparing Numbers",
            "speech": (
                "When comparing the size of two numbers, we follow a strict left-to-right place-value comparison rule. "
                "Higher place-value columns carry far greater weight than lower columns. For example, two hundreds is vastly greater than nine tens, "
                "even though nine is a larger single digit than two, because two hundreds equals two hundred, while nine tens equals only ninety. "
                "When comparing four-digit numbers, we always inspect the leftmost column first: the Thousands place. "
                "Consider community kitchen dining plate counts from two months: in February, one thousand two hundred thirteen plates were used, "
                "while in March, two thousand one hundred twenty-one plates were used. Comparing the thousands digits, two thousand is greater than "
                "one thousand, so two thousand one hundred twenty-one is immediately greater, written with the greater-than symbol. "
                "What if the thousands digits are identical? Compare September with one thousand three hundred plates against October with two thousand three hundred. "
                "Again, October has two thousands versus one thousand in September. If both numbers share identical thousands, we move rightward to compare hundreds. "
                "If hundreds match, we compare tens, and finally ones. Comparing place values left to right ensures reliable, lightning-fast mathematical judgments. "
                "Use the interactive comparison balance below to evaluate four-digit pairs using greater-than, less-than, and equal symbols."
            ),
            "checkpoints": [
                {
                    "q": "Which comparison statement is correct: 1213 ___ 2121?",
                    "options": ["1213 > 2121", "1213 < 2121", "1213 = 2121", "Cannot be compared"],
                    "ans": 1,
                    "exp": "1 Thousand is less than 2 Thousands, so 1213 < 2121."
                },
                {
                    "q": "Why is 2 Hundreds greater than 9 Tens?",
                    "options": ["Because 2 is bigger than 9", "Because 2 Hundreds = 200, which exceeds 9 Tens = 90", "Because Tens are always bigger", "They are equal"],
                    "ans": 1,
                    "exp": "Place value determines magnitude: 200 > 90 regardless of individual digit values."
                }
            ]
        },
        {
            "id": 16,
            "title": "Ordering Four-Digit Quantities",
            "section": "Let Us Do (Ordering & Real-World Data)",
            "speech": (
                "Let us apply our four-digit skills to real-world ordering challenges, such as shopping appliance prices, sports statistics, "
                "and Himalayan mountain peak elevations. Suppose three kitchen appliances are priced at one thousand nine hundred eighty-six rupees, "
                "one thousand ninety-nine rupees, and one thousand eight hundred ninety-nine rupees. To arrange them in increasing order, "
                "we compare their digits. All three have one thousand. Looking at the hundreds, zero hundreds is smallest, followed by eight hundreds, "
                "and nine hundreds. Thus, the increasing order is one thousand ninety-nine, one thousand eight hundred ninety-nine, and one thousand nine hundred eighty-six. "
                "In international women's cricket, star batters have scored thousands of career runs: one legendary Indian captain scored seven thousand eight hundred five runs, "
                "while an international star scored five thousand one hundred fourteen runs. In Himalayan geography, we order soaring mountain peaks in decreasing order: "
                "Kangchenjunga at eight thousand five hundred eighty-six meters, Nanda Devi at seven thousand eight hundred sixteen meters, and Chaukhamba at seven thousand one hundred thirty-eight. "
                "Between seven thousand and eight thousand, there are exactly nine hundred ninety-nine whole numbers! "
                "And using four distinct digits like two, three, four, and seven, we can construct twenty-four unique four-digit numbers. "
                "Use the interactive sorting lab below to order real-world four-digit records in ascending and descending sequences."
            ),
            "checkpoints": [
                {
                    "q": "Arrange in increasing order (smallest to largest): ₹1986, ₹1099, ₹1899",
                    "options": ["₹1099, ₹1899, ₹1986", "₹1986, ₹1899, ₹1099", "₹1899, ₹1099, ₹1986", "₹1099, ₹1986, ₹1899"],
                    "ans": 0,
                    "exp": "Comparing Hundreds: 0 Hundreds (1099) < 8 Hundreds (1899) < 9 Hundreds (1986)."
                },
                {
                    "q": "How many whole numbers exist strictly between 7000 and 8000?",
                    "options": ["998 numbers", "999 numbers", "1000 numbers", "1001 numbers"],
                    "ans": 1,
                    "exp": "The numbers are 7001 to 7999. Total count = 7999 - 7001 + 1 = 999 numbers."
                }
            ]
        }
    ]

if __name__ == '__main__':
    slides = get_part2_slides()
    for s in slides:
        words = len(s['speech'].split())
        print(f"Slide {s['id']}: {s['title']} -> Word count: {words}")
        assert 195 <= words <= 215, f"Slide {s['id']} word count {words} outside 195-215 range!"
    print("All slides 9-16 pass word count validation!")
