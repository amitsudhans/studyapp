# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 7: The Cleanest Village
Part 1: Slides 1 to 8 Data Generator
Strictly 195 to 215 words per speech lecture.
Zero human names (Daisy, Lou, Sapan, Udaya, Krishna, Sudama, Mala, Neela, etc. replaced).
Clean Unicode throughout (₹, ×, +, -, =).
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Village Trip Logistics",
        "section": "Field Trip Context & Poster Data Analysis",
        "speech": (
            "Welcome young mathematicians to our exciting study journey exploring the cleanest village in Asia, "
            "nestled peacefully among the lush green East Khasi Hills of Meghalaya! A vibrant school field trip "
            "poster presents crucial mathematical information for four hundred fourteen residents living harmoniously "
            "across seventy-seven village families. Careful planners must analyze numerical logistics before "
            "embarking on such an inspiring educational tour. Notice the departure time is scheduled for seven o'clock "
            "in the morning, while the arrival time at the village entrance is marked at four o'clock in the afternoon. "
            "By calculating the elapsed travel duration, we discover that nine full hours are spent traveling on the scenic "
            "mountain road. Furthermore, each child ticket costs five hundred rupees, covering guided tours to the world-famous "
            "Living Root Bridge, the historic stone church, and the roaring waterfalls. Mathematical thinking begins with "
            "observing details, identifying numerical values, and organizing facts systematically. When we examine community data, "
            "we see that dividing four hundred fourteen people among seventy-seven families indicates roughly five to six people "
            "in every household. Through careful timetable reading, cost estimation, and population awareness, mathematics connects "
            "classroom calculation with real-world exploration and environmental stewardship across our magnificent country and beautiful green states."
        ),
        "checkpoints": [
            {
                "q": "If departure is at 7:00 AM and arrival is at 4:00 PM, what is the total travel duration?",
                "options": ["7 hours", "8 hours", "9 hours", "10 hours"],
                "ans": 2,
                "exp": "From 7:00 AM to 12:00 noon is 5 hours, and from 12:00 noon to 4:00 PM is 4 hours; 5 + 4 = 9 hours."
            },
            {
                "q": "If 77 families reside in the village with 414 total residents, about how many people live in each family on average?",
                "options": ["About 2 to 3 people", "About 5 to 6 people", "About 10 to 12 people", "About 20 people"],
                "ans": 1,
                "exp": "Dividing 414 by 77 gives approximately 5.37, meaning roughly 5 to 6 members reside in each household."
            }
        ]
    },
    {
        "id": 2,
        "title": "Market Cart Pricing",
        "section": "Per-Kilogram Unit Rates & Price Lists",
        "speech": (
            "At the bustling village market square, a dedicated farmer sets up a colorful wooden cart loaded with fresh "
            "vegetables and sweet local fruits. Every item displays a clear unit rate tag stating the exact cost per kilogram. "
            "Studying this vibrant rate board reveals that crisp radishes cost twenty-three rupees per kilogram, pungent onions "
            "are priced at thirty-two rupees, firm potatoes cost thirty-seven rupees, and hearty mountain yams cost forty-five "
            "rupees. Fresh green beans cost ninety-five rupees per kilogram, while sweet custard apples cost forty-five rupees, "
            "creamy sapotas cost seventy rupees, yellow papayas cost sixty-five rupees, and ripe bananas cost fifty-five rupees. "
            "Unit pricing is the foundation of market arithmetic because knowing the price for one single kilogram enables "
            "shoppers to determine the expense for any requested quantity through repeated addition or multiplication. For example, "
            "if two kilograms of fresh beans are purchased, we calculate ninety-five plus ninety-five, giving a total of one "
            "hundred ninety rupees. Comparing unit prices also sharpens our numerical intuition. Green beans are the most expensive "
            "produce on the cart at ninety-five rupees per kilogram, while humble white radishes are the most economical at "
            "twenty-three rupees. Clear price lists empower fair trade, accurate budgeting, and disciplined shopping habits."
        ),
        "checkpoints": [
            {
                "q": "What is the cost of purchasing 2 kilograms of fresh green beans priced at ₹95 per kilogram?",
                "options": ["₹180", "₹185", "₹190", "₹195"],
                "ans": 2,
                "exp": "2 kg of beans at ₹95 per kg equals ₹95 + ₹95 = ₹190 (or 2 × 95 = ₹190)."
            },
            {
                "q": "Which produce item on the farmer's market cart has the lowest unit price per kilogram?",
                "options": ["Potato at ₹37", "Radish at ₹23", "Onion at ₹32", "Yam at ₹45"],
                "ans": 1,
                "exp": "Radish at ₹23 per kilogram is the most economical item among the listed vegetables."
            }
        ]
    },
    {
        "id": 3,
        "title": "Total Cost Calculations",
        "section": "Multi-Step Shopping Combinations & Target Totals",
        "speech": (
            "When shoppers visit the market cart, they frequently purchase combinations of several different fresh items, "
            "requiring multi-step addition to determine the final grocery bill accurately. Suppose a customer selects one kilogram of "
            "yellow onions costing thirty-two rupees and two kilograms of golden potatoes priced at thirty-seven rupees per "
            "kilogram. We first calculate the potato subtotal by adding thirty-seven and thirty-seven, which yields seventy-four "
            "rupees. Then, we add the thirty-two rupees for onions to seventy-four rupees, arriving at an exact total of one "
            "hundred six rupees. Mathematicians also enjoy solving reverse shopping challenges, where a specific total expense "
            "must be assembled from available goods. Consider having exactly one hundred sixty-three rupees in your coin purse. "
            "Can you select items matching this exact budget? Combining one kilogram of ninety-five rupee green beans, one "
            "kilogram of thirty-two rupee onions, and one kilogram of thirty-six rupee produce creates ninety-five plus thirty-two, "
            "which is one hundred twenty-seven, plus thirty-six, equaling one hundred sixty-three rupees! Breaking complex purchases "
            "into separate unit multiplications followed by column addition ensures every rupee is accounted for. Practicing multi-item "
            "costing builds speed, mental clarity, numerical accuracy, and immense confidence in managing everyday financial transactions during local market visits."
        ),
        "checkpoints": [
            {
                "q": "What is the total cost of 1 kg onions (₹32) and 2 kg potatoes (₹37 each)?",
                "options": ["₹96", "₹106", "₹111", "₹116"],
                "ans": 1,
                "exp": "2 kg potatoes cost 37 + 37 = ₹74. Adding 1 kg onions (₹32) gives 74 + 32 = ₹106."
            },
            {
                "q": "Which combination of items totals exactly ₹163?",
                "options": ["Beans (₹95) + Onion (₹32) + Produce (₹36)", "Radish (₹23) + Sapota (₹70) + Papaya (₹65)", "Yam (₹45) + Banana (₹55) + Beans (₹95)", "Potato (₹37) + Onion (₹32) + Custard Apple (₹45)"],
                "ans": 0,
                "exp": "₹95 + ₹32 + ₹36 = ₹163 exact total."
            }
        ]
    },
    {
        "id": 4,
        "title": "Grocery Balance Math",
        "section": "Tendering Currency Notes & Returning Change",
        "speech": (
            "Inside the village grocery store, customers tender various paper currency denominations, requiring the shopkeeper "
            "to calculate exact change accurately and swiftly. The fundamental relationship of cash commerce states that the "
            "change returned equals the money paid minus the total bill amount. Imagine a traveler buys packets of local dried herbs "
            "totaling sixty-four rupees and hands over a one-hundred-rupee banknote to the cashier. To calculate the balance, we "
            "subtract sixty-four from one hundred. We can count upward using an open number line: adding six rupees brings sixty-four "
            "to seventy, and adding thirty more brings seventy to one hundred, revealing a change of thirty-six rupees. Efficient cashiers "
            "also select the fewest currency notes and coins when returning balance to avoid heavy coin bags. Returning thirty-six "
            "rupees is best done with one twenty-rupee note, one ten-rupee note, one five-rupee coin, and one one-rupee coin. Currency "
            "arithmetic teaches us to verify transactions from both directions. When the bill is sixty-four rupees and thirty-six "
            "rupees are returned, adding sixty-four and thirty-six confirms the full one hundred rupees handed over. Mastering balance "
            "calculation guarantees fairness, builds mental math proficiency, and protects everyone from transaction errors during "
            "daily community shopping activities and fair trade deals."
        ),
        "checkpoints": [
            {
                "q": "If a purchase costs ₹64 and a customer pays with a ₹100 note, how much change is returned?",
                "options": ["₹26", "₹34", "₹36", "₹46"],
                "ans": 2,
                "exp": "₹100 - ₹64 = ₹36 change."
            },
            {
                "q": "What is the most efficient note and coin combination to return ₹36 change?",
                "options": ["36 one-rupee coins", "Three ₹10 notes and six ₹1 coins", "One ₹20 note, one ₹10 note, one ₹5 coin, and one ₹1 coin", "Two ₹20 notes"],
                "ans": 2,
                "exp": "₹20 + ₹10 + ₹5 + ₹1 = ₹36 using only 4 currency pieces."
            }
        ]
    },
    {
        "id": 5,
        "title": "Orange Purchase Denominations",
        "section": "Uniform Purchases with Varied Currency Tenders",
        "speech": (
            "A delightful village fruit stall presents an intriguing mathematical pattern involving identical purchases paid "
            "with completely different currency denominations. Four young shoppers each decide to buy two fresh golden oranges. "
            "The fruit seller charges twenty-one rupees per orange, making each child's bill twenty-one plus twenty-one, which "
            "equals forty-two rupees. However, each child opens their wallet and pays using a different currency banknote! The "
            "first child pays with a fifty-rupee note. Subtracting forty-two from fifty leaves an exact balance of eight rupees. "
            "The second child pays with a crisp one-hundred-rupee note. Subtracting forty-two from one hundred yields fifty-eight "
            "rupees in change. The third child hands over a two-hundred-rupee banknote; subtracting forty-two from two hundred "
            "leaves one hundred fifty-eight rupees. Finally, the fourth child tenders a large five-hundred-rupee note. Subtracting "
            "forty-two from five hundred gives four hundred fifty-eight rupees in balance! Notice the beautiful mathematical symmetry: "
            "because the purchase price remains fixed at forty-two rupees, the change returned increases in exact lockstep with "
            "the larger denomination offered. Comparing transaction balances across different tenders reinforces column subtraction, "
            "place value structure, and mental subtraction accuracy for every practical consumer, thoughtful spender, and young student buyer everywhere in real life."
        ),
        "checkpoints": [
            {
                "q": "What is the total cost of purchasing 2 oranges priced at ₹21 each?",
                "options": ["₹32", "₹40", "₹42", "₹44"],
                "ans": 2,
                "exp": "2 × ₹21 = ₹21 + ₹21 = ₹42 total bill."
            },
            {
                "q": "If a shopper pays ₹42 using a ₹200 note, how much balance is returned?",
                "options": ["₹148", "₹158", "₹168", "₹242"],
                "ans": 1,
                "exp": "₹200 - ₹42 = ₹158 change."
            }
        ]
    },
    {
        "id": 6,
        "title": "Triangle Magic Sums",
        "section": "Combinatorial Number Placement Along Polygon Sides",
        "speech": (
            "In the village school courtyard, students enjoy a traditional mathematical game called Magic Triangle Sums. "
            "A large equilateral triangle is drawn on the pavement with circles placed at each of its three vertices and along "
            "the middle of each of its three edges, creating six circular positions in total. The challenge requires placing "
            "the counting numbers one, two, three, four, five, and six into these circles without repeating any number, such that "
            "the three numbers along every side add up to an identical target sum! For a target sum of nine, strategic thinking "
            "reveals that the smallest numbers—one, two, and three—must occupy the three corner vertices, because corner circles "
            "are shared by two intersecting sides and counted twice. Then, the larger numbers—four, five, and six—are placed "
            "between them: six goes between one and two, five goes between one and three, and four goes between two and three. "
            "Checking every side gives one plus six plus two equals nine, one plus five plus three equals nine, and two plus four "
            "plus three equals nine! By altering which numbers occupy the vertex positions, mathematicians can construct triangles "
            "summing to ten, eleven, or twelve. Strategic deduction replaces random guessing."
        ),
        "checkpoints": [
            {
                "q": "In a magic triangle using numbers 1 to 6 with a target sum of 9 on each side, which numbers must be placed at the three corners?",
                "options": ["4, 5, 6", "1, 2, 3", "2, 4, 6", "1, 3, 5"],
                "ans": 1,
                "exp": "Placing the smallest numbers 1, 2, 3 at the shared vertices keeps side sums low, achieving target sum 9."
            },
            {
                "q": "For the side containing corner 1 and corner 2 in the sum-of-9 triangle, which middle number completes the side?",
                "options": ["3", "4", "5", "6"],
                "ans": 3,
                "exp": "1 + 6 + 2 = 9, so the middle number is 6."
            }
        ]
    },
    {
        "id": 7,
        "title": "Base Ten Addition",
        "section": "Dienes Blocks Regrouping & Place Value Transition",
        "speech": (
            "Before performing multi-digit column addition on paper, manipulating physical base-ten Dienes blocks provides a "
            "concrete visual foundation for regrouping. In our decimal numbering system, every column operates on strict bundles "
            "of ten. Single unit cubes represent Ones, ten unit cubes joined into a solid rod form a Ten, and ten rods grouped "
            "into a square flat create a Hundred. When we add numbers such as forty-eight and twenty-six, we combine eight single "
            "cubes with six single cubes, yielding fourteen Ones. Because fourteen exceeds nine, our place value rules mandate "
            "bundling ten individual cubes together into one brand-new Ten rod. This leaves four single cubes in the Ones column "
            "while transferring one extra Ten into the Tens column as a regrouped carry. Next, we gather all the Tens: four original "
            "rods, two added rods, and the one carried rod, totaling seven Tens. Combining seven Tens and four Ones reveals the "
            "sum of seventy-four. The exact same bundling principle governs the transition from Tens to Hundreds: whenever ten Tens "
            "accumulate, they form one hundred-flat. Visualizing base-ten blocks prevents mechanical carrying mistakes by revealing "
            "the logical physical grouping behind every arithmetic step in primary elementary mathematics classroom studies."
        ),
        "checkpoints": [
            {
                "q": "When adding 8 Ones and 6 Ones, how are the 14 resulting unit cubes regrouped?",
                "options": ["14 remain in Ones", "1 Ten rod and 4 Ones cubes", "2 Ten rods and 4 Ones cubes", "1 Hundred flat and 4 Ones"],
                "ans": 1,
                "exp": "14 Ones is regrouped into 1 Ten (bundle of 10) and 4 Ones."
            },
            {
                "q": "What happens when 10 Ten-rods accumulate in the Tens column?",
                "options": ["They are discarded", "They form 1 Hundred flat", "They turn into 100 Ones", "They form 1 Ten"],
                "ans": 1,
                "exp": "10 Tens = 1 Hundred, so they regroup into 1 Hundred flat in the hundreds column."
            }
        ]
    },
    {
        "id": 8,
        "title": "Field Trip Totals",
        "section": "Multi-Digit Column Addition with Regrouping",
        "speech": (
            "Organizing the grand village field trip requires adding attendance counts from several participating primary "
            "schools. First, let us calculate the total number of accompanying staff members. One school sends twenty-four "
            "teachers while a partnering academy sends twenty-eight teachers. Arranging these numbers vertically into columns, "
            "we begin by adding the Ones digits: four plus eight equals twelve Ones. We write down two in the Ones column and carry "
            "one Ten above the Tens column. Adding the Tens gives one carried Ten plus two plus two, equaling five Tens, making fifty-two "
            "teachers in total. Next, consider the total student attendance: four hundred thirty-eight girls and four hundred seventy-six "
            "boys embark on the journey. In the Ones column, eight plus six equals fourteen; we write four and carry one Ten. In the "
            "Tens column, one carried Ten plus three plus seven equals eleven Tens; we write one Ten and carry one Hundred. In the "
            "Hundreds column, one carried Hundred plus four plus four equals nine Hundreds. The total student travelers count reaches "
            "nine hundred fourteen! Aligning columns precisely by place value ensures error-free addition across both simple and large sums "
            "for any practical mathematical calculation across daily life."
        ),
        "checkpoints": [
            {
                "q": "What is the total count of teachers when combining 24 teachers and 28 teachers?",
                "options": ["42", "50", "52", "62"],
                "ans": 2,
                "exp": "4 + 8 = 12 (write 2, carry 1); 1 + 2 + 2 = 5 Tens; total = 52."
            },
            {
                "q": "When adding 438 girls and 476 boys, what is the total student count?",
                "options": ["814", "904", "914", "924"],
                "ans": 2,
                "exp": "438 + 476: 8+6=14 (carry 1); 1+3+7=11 (carry 1); 1+4+4=9 Hundreds -> 914."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(slides_part1)} slides for Part 1.")
    for s in slides_part1:
        wc = len(s["speech"].split())
        print(f"Slide {s['id']}: {s['title']} -> {wc} words (Title: {len(s['title'].split())} words)")
        assert 195 <= wc <= 215, f"Word count {wc} out of bounds for slide {s['id']}!"
        assert 1 <= len(s['title'].split()) <= 3, f"Title length out of bounds for slide {s['id']}!"
