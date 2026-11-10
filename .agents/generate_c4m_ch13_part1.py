# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 13: The Transport Museum
Part 1: Slides 1 to 8 Data Generator
Short headings (1 to 3 words each)
Zero human names (Chinnu, Raghav, etc. replaced with generic roles)
Speech strictly 195 to 215 words per slide
Clean Unicode throughout (×, ÷, ₹, etc.)
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Mystery Matrix Logic",
        "section": "Grid Multiplication & Multiplier Deduction",
        "speech": (
            "Welcome young mathematicians to our study of grid multiplication logic through the engaging mystery matrix puzzle. "
            "In this mathematical challenge, we explore a grid where numbers along horizontal rows and vertical columns intersect. "
            "Each box within the matrix displays a product created by multiplying a secret single-digit row multiplier by a single-digit column multiplier. "
            "To solve the mystery, we must become mathematical detectives and analyze the given target products carefully. "
            "Suppose a white cell reveals the number twenty-four while its adjacent neighbor in the same row shows thirty-six. "
            "We immediately look for common factors shared by both products. Since twelve is not a single digit, we deduce the row multiplier must be six, "
            "or perhaps four depending on the column clues. If the row multiplier is six, then the corresponding column values must be four and six because six times four is twenty-four and six times six is thirty-six. "
            "Orange and blue highlight boxes introduce additional constraint clues, helping us isolate unknown factors systematically without guessing. "
            "This grid logic strengthens our understanding that multiplication is commutative and factor pairs connect rows and columns seamlessly. "
            "By verifying row totals and column totals against our deduced multipliers, we ensure complete mathematical consistency across the entire matrix puzzle."
        ),
        "checkpoints": [
            {
                "q": "If a row contains products 28 and 35, what single-digit multiplier is common to both?",
                "options": ["4", "5", "7", "8"],
                "ans": 2,
                "exp": "Both 28 (7 × 4) and 35 (7 × 5) share the common factor 7."
            },
            {
                "q": "In a multiplication matrix, what operation links the row header and column header?",
                "options": ["Addition", "Multiplication", "Subtraction", "Division"],
                "ans": 1,
                "exp": "Each cell represents the product of its row multiplier and column multiplier."
            }
        ]
    },
    {
        "id": 2,
        "title": "Visualizing Tens Multiplication",
        "section": "Base-Ten Scaling & Unit Bundling",
        "speech": (
            "Let us explore how numbers grow when we multiply by ten using visual representations of base-ten bundles and rods. "
            "When we consider two times ten, we are gathering two complete bundles containing ten individual items each. "
            "Counting by tens, we say ten, twenty. Therefore, two times ten equals twenty, which can also be described as two tens. "
            "Similarly, three times ten represents three tens, giving a total value of thirty. "
            "Notice how multiplying any single-digit number by ten preserves the original digit in the tens place while placing a zero in the ones place. "
            "What happens when we scale up to ten times ten? We are combining ten complete rods of ten units each. "
            "Counting ten groups of ten reveals the sequence ten, twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety, and one hundred. "
            "Ten tens bundle together to create one flat of one hundred. "
            "This fundamental place-value shift is the foundation of our decimal number system. "
            "Whenever we multiply by ten, every digit shifts one place to the left, and a place-holding zero occupies the empty ones column. "
            "Mastering this base-ten visualization allows us to compute large products mentally with exceptional confidence and structural speed."
        ),
        "checkpoints": [
            {
                "q": "What is the value of 10 groups of 10 items bundled together?",
                "options": ["10", "50", "100", "1,000"],
                "ans": 2,
                "exp": "10 groups of 10 equal 100, forming one hundred flat in base-ten blocks."
            },
            {
                "q": "How can 7 × 10 be expressed in place-value language?",
                "options": ["7 Ones", "7 Tens (70)", "7 Hundreds", "17 Units"],
                "ans": 1,
                "exp": "7 × 10 equals 7 Tens, which equals 70."
            }
        ]
    },
    {
        "id": 3,
        "title": "Constructing Table Arrays",
        "section": "Area Breakdown & Multi-Digit Tables",
        "speech": (
            "We can construct multi-digit multiplication tables effortlessly by breaking numbers into tens and ones using the visual area model. "
            "Consider constructing the times-fifteen table. Remembering fifteen facts from memory might appear intimidating at first glance, "
            "but fifteen is simply the sum of ten and five. Therefore, to multiply any number by fifteen, we split the problem into two friendly calculations. "
            "For example, let us compute four times fifteen. We construct a rectangular area partitioned into two neat sections. "
            "The first section represents four times ten, which yields forty. The second adjacent section represents four times five, which yields twenty. "
            "Adding forty and twenty gives sixty, which is the exact product of four times fifteen. "
            "Let us try another calculation such as six times fifteen. Six times ten equals sixty, and six times five equals thirty. "
            "Combining sixty and thirty gives ninety. This distributive strategy applies universally to any multi-digit number in our curriculum. "
            "Whether constructing tables for twelve, thirteen, fourteen, sixteen, or eighteen, we decompose the number into convenient decade bundles and manageable units. "
            "Breaking complex arrays into simpler geometric rectangles transforms overwhelming rote memorization into clear, systematic mathematical reasoning that never fails under examination pressure."
        ),
        "checkpoints": [
            {
                "q": "How can 8 × 15 be calculated using the tens and ones split method?",
                "options": ["(8 × 10) + (8 × 5)", "(8 × 10) - (8 × 5)", "(8 × 15) + 10", "(8 × 20) - 5"],
                "ans": 0,
                "exp": "(8 × 10) + (8 × 5) = 80 + 40 = 120."
            },
            {
                "q": "What is the product of 6 × 15 when calculated by area decomposition?",
                "options": ["75", "80", "90", "95"],
                "ans": 2,
                "exp": "6 × 10 = 60, 6 × 5 = 30; 60 + 30 = 90."
            }
        ]
    },
    {
        "id": 4,
        "title": "Comparing Number Tables",
        "section": "Pattern Discoveries & Table Relationships",
        "speech": (
            "Mathematical insight blossoms when we compare different multiplication tables side by side to uncover their hidden relationships and structural symmetries. "
            "Let us place the times-five table alongside the times-fifteen table and examine their corresponding products closely across each position. "
            "In the times-five table, the sequence of products progresses steadily as five, ten, fifteen, twenty, twenty-five, thirty, thirty-five, and forty. "
            "In the times-fifteen table, the products progress as fifteen, thirty, forty-five, sixty, seventy-five, ninety, one hundred five, and one hundred twenty. "
            "Notice that every product in the times-fifteen table is exactly three times the corresponding product in the times-five table. "
            "Why is this so? Because fifteen is three times five, every multiple of fifteen must be three times the multiple of five. "
            "Furthermore, observe the final digits of both tables. Both tables end strictly in five or zero, reflecting their shared divisibility properties. "
            "When we compare tables from eleven through twenty, we notice how the ones digits cycle predictably based on the units component of each base number. "
            "Recognizing these inter-table patterns empowers us to verify our calculations quickly, connect multiplication to scaling factors, "
            "and develop deep structural number sense across all arithmetic operations in our daily studies."
        ),
        "checkpoints": [
            {
                "q": "What is the relationship between any entry in the times-15 table and the times-5 table?",
                "options": ["It is 2 times bigger", "It is 3 times bigger", "It is 10 more", "It is 5 times bigger"],
                "ans": 1,
                "exp": "Since 15 = 3 × 5, every multiple of 15 is 3 times the multiple of 5."
            },
            {
                "q": "What digits can appear in the ones place of products in both times-5 and times-15 tables?",
                "options": ["Only 0", "Only 5", "Either 0 or 5", "Any even number"],
                "ans": 2,
                "exp": "All multiples of 5 and 15 alternate between ending in 5 and 0."
            }
        ]
    },
    {
        "id": 5,
        "title": "Halving And Doubling",
        "section": "Grouping Strategies & Factor Splitting",
        "speech": (
            "A powerful mental math tool used by experienced mathematicians is the halving and doubling strategy for constructing complex multi-digit tables. "
            "Suppose we need to calculate three times fourteen, but we have not memorized the fourteen table by rote memory. "
            "We can split the group of fourteen into two equal halves of seven items each. "
            "First, we calculate three times seven, which is a familiar foundational fact giving twenty-one. "
            "Since fourteen is twice seven, the total product must be twice twenty-one. "
            "Doubling twenty-one gives forty-two, which is the exact product of three times fourteen. "
            "This strategy works because splitting one factor in half and doubling the resulting product preserves the total quantity perfectly. "
            "Let us apply this method to calculate six times twelve. Half of twelve is six, and six times six is thirty-six. "
            "Doubling thirty-six yields seventy-two, so six times twelve equals seventy-two. "
            "Alternatively, we could halve six to get three, compute three times twelve which is thirty-six, and double thirty-six to obtain seventy-two. "
            "Whether we halve the multiplier or the multiplicand, factor manipulation gives us extraordinary mental flexibility and computational speed in computing multi-digit multiplication without paper and pencil during daily classroom problem-solving activities."
        ),
        "checkpoints": [
            {
                "q": "How can 4 × 16 be calculated using the halving and doubling strategy?",
                "options": ["Double (4 × 8)", "Halve (4 × 8)", "Add 16 to 4", "Multiply 4 × 10"],
                "ans": 0,
                "exp": "Half of 16 is 8; 4 × 8 = 32, and doubling 32 yields 64."
            },
            {
                "q": "If 3 × 7 = 21, what is 3 × 14 by doubling?",
                "options": ["28", "35", "42", "49"],
                "ans": 2,
                "exp": "Doubling 21 gives 42 (since 14 is 2 × 7)."
            }
        ]
    },
    {
        "id": 6,
        "title": "Scaling Decade Multiples",
        "section": "Multiplying Multiples of Ten",
        "speech": (
            "Now let us extend our multiplication principles to larger multiples of ten, which we call scaling by decades in mental arithmetic. "
            "Consider calculating fourteen times ten. We express this in words as fourteen tens. "
            "Since one ten is ten, fourteen tens equals one hundred forty without any complicated column addition. "
            "Now consider a more advanced problem: twelve times twenty. Twenty can be decomposed cleanly into two times ten. "
            "Therefore, twelve times twenty can be calculated in two effortless sequential steps. "
            "First, we multiply twelve by two, which gives twenty-four. Then, we multiply twenty-four by ten, which gives two hundred forty. "
            "Notice how the problem simplified into basic single-digit multiplication followed by a base-ten place-value shift. "
            "Let us examine thirty times forty. Three times four equals twelve. "
            "Since both thirty and forty are multiples of ten, we have two factors of ten involved in the calculation. "
            "Twelve multiplied by ten gives one hundred twenty, and multiplied by ten again gives one thousand two hundred. "
            "Counting the zeroes in our decade factors provides a reliable structural shortcut, but understanding the underlying place-value shifts ensures we never make magnitude errors when estimating large industrial quantities in real life."
        ),
        "checkpoints": [
            {
                "q": "What is 15 × 20 calculated by decade factoring (15 × 2 × 10)?",
                "options": ["150", "250", "300", "350"],
                "ans": 2,
                "exp": "15 × 2 = 30, and 30 × 10 = 300."
            },
            {
                "q": "How many tens are contained in the product 18 × 10?",
                "options": ["8 Tens", "10 Tens", "18 Tens (180)", "180 Tens"],
                "ans": 2,
                "exp": "18 × 10 represents 18 Tens, which equals 180."
            }
        ]
    },
    {
        "id": 7,
        "title": "Transport Museum Math",
        "section": "Real-World Contexts & Transit Exhibits",
        "speech": (
            "Welcome to the historic Transport Museum, where dynamic artifacts of human travel illustrate the practical power of mathematics in motion and structural engineering design. "
            "From ancient wooden bullock carts and riverboats to modern steam locomotives, diesel engines, and passenger aircraft, "
            "transportation logistics rely fundamentally on multiplication and division algorithms to manage passengers safely and reliably. "
            "When museum curators organize historical tours, they must calculate vehicle passenger capacities, ticket revenues, and schedule intervals with meticulous precision. "
            "Suppose the museum miniature railway features special vintage passenger coaches that transport visiting school groups across the extensive exhibition grounds. "
            "If each vintage carriage seats a specific number of passengers, determining the entire fleet capacity requires scaling passenger counts across multiple coaches. "
            "Similarly, calculating fuel consumption, maintenance schedules, visitor arrival quotas, and tour guide assignments demands systematic multi-digit computation every single morning. "
            "As we explore the transport galleries, we will see that numbers are not merely abstract figures written on a classroom chalkboard; "
            "they represent real seats, tickets, coaches, platform tracks, and travel distances across our country. "
            "Connecting our classroom mathematical algorithms to tangible transport vehicles helps us understand why accuracy and speed matter in real-world engineering and public transit operations."
        ),
        "checkpoints": [
            {
                "q": "If a heritage museum tram has 8 rows of 4 seats each, what is its total passenger capacity?",
                "options": ["24 seats", "28 seats", "32 seats", "36 seats"],
                "ans": 2,
                "exp": "8 rows × 4 seats per row = 32 seats."
            },
            {
                "q": "Why do transport managers use multiplication when planning vehicle fleets?",
                "options": ["To guess passenger numbers", "To compute total capacity quickly across identical vehicles", "To slow down departures", "To eliminate tickets"],
                "ans": 1,
                "exp": "Multiplying number of vehicles by capacity per vehicle gives total fleet capacity instantly."
            }
        ]
    },
    {
        "id": 8,
        "title": "Toy Train Grid",
        "section": "Box Method for 2-Digit Multiplication",
        "speech": (
            "At the museum outdoor exhibit, a beloved toy train transports visiting children around a scenic loop with vintage miniature signals. "
            "The train consists of fifteen passenger coaches, and each coach comfortably accommodates fourteen children on its wooden bench seats. "
            "How many children can ride the toy train simultaneously? We must calculate fifteen times fourteen. "
            "To solve this two-digit by two-digit multiplication with total clarity, we employ the box grid area method. "
            "We partition fifteen into ten plus five along the top edge, and fourteen into ten plus four along the vertical edge. "
            "This creates four distinct calculation chambers inside our visual grid. "
            "The first chamber computes ten times ten, which equals one hundred. "
            "The second chamber computes five times ten, which equals fifty. "
            "The third chamber computes ten times four, which equals forty. "
            "The fourth chamber computes five times four, which equals twenty. "
            "Now we sum all four partial products together: one hundred plus fifty plus forty plus twenty. "
            "One hundred plus fifty is one hundred fifty; adding forty gives one hundred ninety; adding twenty yields exactly two hundred ten. "
            "Thus, the toy train carries two hundred ten children in full capacity without confusion or arithmetic errors."
        ),
        "checkpoints": [
            {
                "q": "In the box method for 15 × 14, what are the four partial products?",
                "options": ["100, 50, 40, 20", "150, 140, 50, 10", "100, 20, 14, 15", "140, 50, 20, 10"],
                "ans": 0,
                "exp": "(10×10=100) + (5×10=50) + (10×4=40) + (5×4=20) = 210."
            },
            {
                "q": "What is the total capacity of 15 coaches with 14 children each?",
                "options": ["190 children", "200 children", "210 children", "220 children"],
                "ans": 2,
                "exp": "15 × 14 = 210 children."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(slides_part1)} slides for Part 1.")
    for s in slides_part1:
        wc = len(s["speech"].split())
        tw = len(s["title"].split())
        print(f"Slide {s['id']}: {s['title']} -> {wc} words (Title: {tw} words)")
        assert 1 <= tw <= 3, f"Title '{s['title']}' must be 1 to 3 words"
        assert 195 <= wc <= 215, f"Slide {s['id']} speech {wc} words out of range (195-215)"
        assert len(s["checkpoints"]) == 2, f"Slide {s['id']} must have 2 checkpoints"
    print("All Part 1 slide constraints validated successfully!")
