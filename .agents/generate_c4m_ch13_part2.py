# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 13: The Transport Museum
Part 2: Slides 9 to 16 Data Generator
Short headings (1 to 3 words each)
Zero human names (Chinnu, Raghav, etc. replaced with generic roles)
Speech strictly 195 to 215 words per slide
Clean Unicode throughout (×, ÷, ₹, etc.)
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Coach Allocation Remainders",
        "section": "Long Division with Remainders",
        "speech": (
            "When organizing transport for large visiting assemblies, division with remainders becomes an essential logistical tool in daily operations. "
            "Suppose three hundred twenty-four school children arrive at the Transport Museum station eager to board vintage passenger coaches. "
            "If each railway coach has a strict seating limit of fifteen children, how many coaches must the station master allocate? "
            "To solve this real-world problem, we divide three hundred twenty-four by fifteen using systematic long division steps. "
            "First, we estimate how many groups of fifteen fit into thirty-two tens. "
            "Since fifteen times two equals thirty, fifteen times twenty equals three hundred. "
            "Subtracting three hundred from three hundred twenty-four leaves twenty-four children remaining on the departure platform. "
            "Now, how many groups of fifteen fit into twenty-four? Exactly one group, because one times fifteen is fifteen. "
            "Subtracting fifteen from twenty-four leaves a remainder of nine children. "
            "Our quotient is twenty-one, with a remainder of nine. Twenty-one full coaches accommodate three hundred fifteen children. "
            "However, nine children cannot be left behind waiting alone on the platform! "
            "Therefore, the station master must allocate twenty-two coaches in total so every single child has a safe, comfortable seat on the historic train journey with total comfort and security."
        ),
        "checkpoints": [
            {
                "q": "What is 324 ÷ 15 expressed as quotient and remainder?",
                "options": ["20 remainder 14", "21 remainder 9", "22 remainder 0", "21 remainder 5"],
                "ans": 1,
                "exp": "15 × 21 = 315; 324 - 315 = 9 remainder."
            },
            {
                "q": "Why must 22 coaches be ordered instead of 21 for 324 children?",
                "options": ["Coaches must be even", "To ensure the 9 remaining children also have a seat", "For luggage storage only", "Because 21 is unlucky"],
                "ans": 1,
                "exp": "In real-world passenger transit, any remainder requires an additional coach to carry everyone."
            }
        ]
    },
    {
        "id": 10,
        "title": "Multiplication Division Drill",
        "section": "Algorithm Mastery & Remainder Verification",
        "speech": (
            "Let us sharpen our procedural fluency through rigorous multi-digit multiplication and long division practice drills in our mathematics notebooks. "
            "When performing two-digit by two-digit multiplication, such as twenty-four times thirty-six, we systematically compute partial products column by column. "
            "First, we multiply twenty-four by six ones to obtain one hundred forty-four. "
            "Next, we multiply twenty-four by three tens, which is thirty, yielding seven hundred twenty. "
            "Adding one hundred forty-four and seven hundred twenty gives the complete product of eight hundred sixty-four. "
            "Now let us examine the complementary inverse operation: long division with remainder identification. "
            "Suppose we divide four hundred seventy-eight by eight. We divide forty-seven tens by eight, yielding five tens with seven tens remaining. "
            "Bringing down the eight units gives seventy-eight. Dividing seventy-eight by eight yields nine, since eight times nine is seventy-two. "
            "Subtracting seventy-two leaves six as our final remainder. The quotient is fifty-nine with remainder six. "
            "We always verify our work using the fundamental division formula: Dividend equals Divisor multiplied by Quotient plus Remainder. "
            "Eight times fifty-nine is four hundred seventy-two, and adding six brings us back to four hundred seventy-eight. "
            "This self-checking loop guarantees absolute accuracy in every arithmetic assessment we encounter."
        ),
        "checkpoints": [
            {
                "q": "What is the product of 24 × 36?",
                "options": ["844", "864", "884", "904"],
                "ans": 1,
                "exp": "(24 × 6 = 144) + (24 × 30 = 720) = 864."
            },
            {
                "q": "What is the division verification formula?",
                "options": ["Dividend = Divisor + Quotient", "Dividend = (Divisor × Quotient) + Remainder", "Dividend = Divisor - Remainder", "Dividend = Quotient ÷ Divisor"],
                "ans": 1,
                "exp": "Dividend = (Divisor × Quotient) + Remainder."
            }
        ]
    },
    {
        "id": 11,
        "title": "Hundreds Scaling Patterns",
        "section": "Scaling Factors & Multiples of 100",
        "speech": (
            "We can scale our mathematical understanding to larger horizons by exploring patterns involving multiples of one hundred across transit systems. "
            "When we calculate two times one hundred, we are grouping two hundreds flats, which clearly equals two hundred. "
            "Now consider eleven times two hundred. We can decompose this expression into eleven times two, which is twenty-two, multiplied by one hundred. "
            "Twenty-two multiplied by one hundred equals two thousand two hundred. "
            "What happens when both factors contain trailing zeroes, such as eighty times fifty? "
            "Let us decompose eighty into eight times ten, and fifty into five times ten. "
            "Rearranging the factors gives eight times five, which is forty, multiplied by ten times ten, which is one hundred. "
            "Multiplying forty by one hundred shifts forty two places to the left, yielding four thousand. "
            "Students sometimes make the common error of writing four hundred because they overlook that forty itself already ends in a zero! "
            "Eight times five produces forty, and the two decade zeroes append to create four thousand in total. "
            "Always compute the basic single-digit multiplication first, and then apply the combined power of the trailing zeroes to guarantee place-value precision in all calculations without making any estimation blunders."
        ),
        "checkpoints": [
            {
                "q": "What is the product of 80 × 50?",
                "options": ["400", "4,000", "40,000", "850"],
                "ans": 1,
                "exp": "8 × 5 = 40; appending two zeroes gives 4,000."
            },
            {
                "q": "What is 11 × 200 calculated by factoring?",
                "options": ["1,100", "2,000", "2,200", "2,400"],
                "ans": 2,
                "exp": "11 × 2 = 22, and 22 × 100 = 2,200."
            }
        ]
    },
    {
        "id": 12,
        "title": "Dividing Tens Hundreds",
        "section": "Base-Ten Division & Packaging Logic",
        "speech": (
            "In real-world transport and trade logistics, division by ten and one hundred represents the physical act of packaging and freight distribution. "
            "Imagine a heritage agricultural transport depot where a harvest of seven hundred fifty kilograms of rice must be bagged for shipment. "
            "If the warehouse workers pack the grain into ten-kilogram sacks, how many full sacks can they prepare? "
            "Dividing seven hundred fifty by ten removes one place-value factor of ten, yielding exactly seventy-five complete sacks. "
            "Every digit shifts one position to the right because dividing by ten is the precise inverse of multiplying by ten. "
            "Now imagine distributing two thousand four hundred kilograms of grain into heavy hundred-kilogram bulk transit containers. "
            "Dividing two thousand four hundred by one hundred shifts each digit two places to the right, yielding twenty-four containers. "
            "What happens if an amount does not divide evenly, such as eight hundred forty-six divided by one hundred? "
            "Eight hundred forty-six contains eight hundreds with forty-six units left over. "
            "Therefore, eight hundred forty-six divided by one hundred gives a quotient of eight with a remainder of forty-six. "
            "Understanding this base-ten shift makes calculating inventory shipments, financial payouts, and bulk freight distributions instant, efficient, and completely error-free."
        ),
        "checkpoints": [
            {
                "q": "How many 10 kg sacks can be filled from 750 kg of grain?",
                "options": ["70 sacks", "75 sacks", "80 sacks", "750 sacks"],
                "ans": 1,
                "exp": "750 ÷ 10 = 75 sacks."
            },
            {
                "q": "What is 846 ÷ 100 expressed as quotient and remainder?",
                "options": ["84 remainder 6", "8 remainder 46", "80 remainder 46", "8 remainder 0"],
                "ans": 1,
                "exp": "846 = (8 × 100) + 46. Quotient is 8, remainder is 46."
            }
        ]
    },
    {
        "id": 13,
        "title": "Currency Denomination Puzzles",
        "section": "Financial Math & Denomination Combinations",
        "speech": (
            "At the museum ticket counter, a young visitor purchases special admission passes using a collection of Indian currency notes and coins. "
            "Indian currency denominations include two-hundred-rupee notes, fifty-rupee notes, twenty-rupee notes, five-rupee coins, and two-rupee coins in common circulation. "
            "Suppose four heritage passes cost a total of six hundred eighty-five rupees. "
            "How can this exact amount be paid using the fewest possible currency notes and coins? "
            "We begin with the highest denomination that fits into six hundred eighty-five. "
            "Three notes of two hundred rupees provide six hundred rupees, leaving eighty-five rupees to settle. "
            "Next, one note of fifty rupees brings our subtotal to six hundred fifty rupees, leaving thirty-five rupees remaining to pay. "
            "One note of twenty rupees brings the total to six hundred seventy rupees, leaving fifteen rupees. "
            "One ten-rupee note, or three five-rupee coins, completes the remaining balance. "
            "If five-rupee coins are used, three coins of five rupees provide fifteen rupees, reaching six hundred eighty-five rupees precisely. "
            "Denomination puzzles teach us to decompose large monetary totals into optimal additive combinations of standard currency units. "
            "This financial arithmetic is essential for cashiers, business operators, and smart consumers handling everyday transactions across India in every marketplace."
        ),
        "checkpoints": [
            {
                "q": "What is the total value of 3 notes of ₹200 + 1 note of ₹50 + 1 note of ₹20?",
                "options": ["₹650", "₹670", "₹680", "₹700"],
                "ans": 1,
                "exp": "(3 × 200 = 600) + 50 + 20 = ₹670."
            },
            {
                "q": "How many ₹5 coins are needed to make ₹35?",
                "options": ["5 coins", "6 coins", "7 coins", "8 coins"],
                "ans": 2,
                "exp": "35 ÷ 5 = 7 coins."
            }
        ]
    },
    {
        "id": 14,
        "title": "Multiplication Pattern Discovery",
        "section": "Digit Sum Invariants & Number Symmetries",
        "speech": (
            "Mathematics is the science of patterns, and multiplication reveals some of the most captivating numerical symmetries in all of arithmetic. "
            "Let us investigate what happens when we multiply numbers by nine in our daily mathematics studies. "
            "Notice the sequence of products: nine, eighteen, twenty-seven, thirty-six, forty-five, fifty-four, sixty-three, seventy-two, eighty-one, and ninety. "
            "If we calculate the digital sum of each product by adding its digits together, an astonishing pattern emerges. "
            "One plus eight equals nine; two plus seven equals nine; three plus six equals nine; four plus five equals nine! "
            "Every single multiple of nine possesses a digital root of nine. "
            "Now consider multiplying eleven by single digits: eleven, twenty-two, thirty-three, forty-four, fifty-five. "
            "The tens digit and ones digit are identical twins. "
            "When we multiply two-digit numbers by eleven, such as twenty-five times eleven, we split the digits two and five, "
            "and insert their sum, which is seven, directly between them to obtain two hundred seventy-five! "
            "Discovering these colored digit patterns transforms arithmetic from mechanical labor into a joyful treasure hunt of structural symmetry. "
            "Recognizing patterns helps us detect calculation errors immediately and reinforces our intuition about numbers. "
            "Mathematical patterns reveal that numbers behave according to dependable, elegant rules that make problem solving truly delightful."
        ),
        "checkpoints": [
            {
                "q": "What is the digital root (sum of digits) of any multiple of 9?",
                "options": ["3", "6", "9", "10"],
                "ans": 2,
                "exp": "All multiples of 9 have a digital root of 9 (e.g., 5 + 4 = 9 for 54)."
            },
            {
                "q": "Using the 11s shortcut, what is 34 × 11?",
                "options": ["344", "364", "374", "384"],
                "ans": 2,
                "exp": "Split 3 and 4, and insert (3 + 4 = 7) in the middle: 374."
            }
        ]
    },
    {
        "id": 15,
        "title": "Fleet Capacity Matching",
        "section": "Multi-Modal Vehicle Capacity Calculations",
        "speech": (
            "At the grand finale of the Transport Museum, visitors explore the vehicle matching gallery showcasing entire fleets at full passenger capacity. "
            "Different modes of transport carry vastly different passenger quotas depending on their engineering design, physical size, and safety specifications. "
            "A standard passenger bicycle carries one person. An auto-rickshaw carries three passengers through bustling streets. "
            "A passenger car seats five travelers. A school minibus accommodates twenty passengers safely. "
            "A commercial airliner carries one hundred eighty passengers, while an express train sleeper coach accommodates seventy-two passengers across long distances. "
            "Now let us calculate fleet totals. Suppose the museum fleet includes eight minibuses. "
            "Eight minibuses times twenty passengers each equals one hundred sixty passengers. "
            "If a railway company operates twelve sleeper coaches, twelve times seventy-two equals eight hundred sixty-four sleeping berths! "
            "Let us check six passenger cars: six times five equals thirty travelers. "
            "Notice how fleet matching requires multiplying vehicle units by their individual passenger rate. "
            "By comparing these fleet capacities, transit engineers determine which combination of vehicles best serves a city during peak rush hour. "
            "Multiplication allows transport planners to balance traffic flow, minimize fuel consumption, and ensure that thousands of citizens reach their destinations safely every single morning."
        ),
        "checkpoints": [
            {
                "q": "What is the passenger capacity of 8 minibuses seating 20 passengers each?",
                "options": ["120 passengers", "140 passengers", "160 passengers", "180 passengers"],
                "ans": 2,
                "exp": "8 × 20 = 160 passengers."
            },
            {
                "q": "If 1 car carries 5 passengers, how many cars are needed for 45 travelers?",
                "options": ["7 cars", "8 cars", "9 cars", "10 cars"],
                "ans": 2,
                "exp": "45 ÷ 5 = 9 cars."
            }
        ]
    },
    {
        "id": 16,
        "title": "Transport Fleet Arithmetic",
        "section": "Integrated Logistics & Multi-Step transit Problems",
        "speech": (
            "We conclude our exploration of the Transport Museum by synthesizing all our multiplication and division skills into integrated fleet logistics problems. "
            "Consider a complex transportation scenario where five hundred visitors must travel from the central railway junction to the museum exhibit grounds. "
            "The transport coordinator has a mixed fleet consisting of four minibuses seating twenty-five passengers each, "
            "and several large electric buses seating fifty passengers each. "
            "First, let us calculate the capacity of the four minibuses. Four times twenty-five equals one hundred passengers. "
            "Subtracting one hundred from five hundred leaves four hundred visitors still needing transportation. "
            "Now, how many fifty-passenger electric buses must be deployed to carry the remaining four hundred visitors? "
            "We divide four hundred by fifty. Since four hundred divided by fifty equals eight, exactly eight electric buses are required. "
            "The total fleet consists of four minibuses and eight electric buses working together in perfect operational coordination. "
            "Every step of this logistical solution relied upon the principles we mastered: decomposing numbers, scaling by tens, "
            "performing multi-digit multiplication, and applying division with precision. "
            "This harmonious combination of arithmetic and engineering ensures our world stays reliably in motion with safety and efficiency every single day."
        ),
        "checkpoints": [
            {
                "q": "If 4 minibuses carry 25 passengers each, what is their combined capacity?",
                "options": ["75 passengers", "100 passengers", "125 passengers", "150 passengers"],
                "ans": 1,
                "exp": "4 × 25 = 100 passengers."
            },
            {
                "q": "How many 50-seater buses are required to transport the remaining 400 passengers?",
                "options": ["6 buses", "7 buses", "8 buses", "9 buses"],
                "ans": 2,
                "exp": "400 ÷ 50 = 8 buses."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(slides_part2)} slides for Part 2.")
    for s in slides_part2:
        wc = len(s["speech"].split())
        tw = len(s["title"].split())
        print(f"Slide {s['id']}: {s['title']} -> {wc} words (Title: {tw} words)")
        assert 1 <= tw <= 3, f"Title '{s['title']}' must be 1 to 3 words"
        assert 195 <= wc <= 215, f"Slide {s['id']} speech {wc} words out of range (195-215)"
        assert len(s["checkpoints"]) == 2, f"Slide {s['id']} must have 2 checkpoints"
    print("All Part 2 slide constraints validated successfully!")
