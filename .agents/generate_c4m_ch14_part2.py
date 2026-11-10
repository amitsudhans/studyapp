# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 14: Data Handling
Part 2: Slides 9 to 16 Data Generator
Short headings (1 to 3 words each)
Zero human names (replaced with generic roles)
Speech strictly 195 to 215 words per slide
Clean Unicode throughout (×, ÷, ₹, etc.)
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Bal Mela Pictographs",
        "section": "Fair Stall Data & Scaled Pictographs",
        "speech": (
            "During our joyful school Bal Mela celebration, student stall managers set up a bustling food kiosk selling refreshing fruit chaat and wholesome sandwiches. "
            "To record the daily sales over three festive days, Friday, Saturday, and Sunday, the young organizers designed an illustrated pictograph chart. "
            "Because hundreds of food portions were sold, drawing individual snacks for every single customer was impractical and cluttered the poster board. "
            "Instead, the stall team established a clear scale key at the base of the chart: each drawn plate symbol represents five portions of snacks sold. "
            "On Friday, the chart displays four plate symbols for fruit chaat and six plate symbols for vegetable sandwiches. "
            "Using our scale key, four plates multiplied by five portions equals twenty servings of fruit chaat, while six plates multiplied by five portions yields thirty sandwiches. "
            "On Saturday, when visitor attendance surged, the stall recorded eight plate symbols for fruit chaat, which represents forty portions, and ten plate symbols for sandwiches, denoting fifty servings. "
            "On Sunday, six plates of fruit chaat were recorded, equaling thirty portions, alongside eight plates of sandwiches, equaling forty servings. "
            "Scaled pictographs turn large sales numbers into delightful, immediately comprehensible visual records for every visitor at the festive fair."
        ),
        "checkpoints": [
            {
                "q": "If each plate symbol represents 5 snack servings, what does 6 plate symbols represent?",
                "options": ["11 servings", "25 servings", "30 servings", "35 servings"],
                "ans": 2,
                "exp": "6 × 5 = 30 snack servings."
            },
            {
                "q": "Why did the student stall managers use a scale key of 1 symbol = 5 items instead of 1 symbol = 1 item?",
                "options": ["To hide real sales", "To make drawing faster and fit large sales numbers neatly onto the chart", "Because paper was unavailable", "To sell fewer items"],
                "ans": 1,
                "exp": "A scale key compacts large quantities into manageable, easy-to-read visual icons."
            }
        ]
    },
    {
        "id": 10,
        "title": "Food Sales Analysis",
        "section": "Comparative Sales & Trend Analysis",
        "speech": (
            "Now let us examine our Bal Mela sales records in detail to discover peak consumption trends and financial performance across the festive weekend. "
            "By converting our pictograph symbols into numerical totals, our stall team compiled an organized summary table. "
            "On Friday, total snack portions sold were twenty fruit chaats plus thirty sandwiches, yielding fifty total food servings. "
            "On Saturday, the festival experienced its highest footfall: forty fruit chaats plus fifty sandwiches produced an impressive peak sale of ninety portions. "
            "On Sunday, thirty fruit chaats and forty sandwiches yielded seventy portions across the afternoon. "
            "Comparing the two food offerings over all three days, total fruit chaat sales reached twenty plus forty plus thirty, equaling ninety servings. "
            "Total sandwich sales reached thirty plus fifty plus forty, equaling one hundred and twenty servings. "
            "Subtracting ninety from one hundred and twenty reveals that the stall sold thirty more sandwiches than fruit chaats throughout the event. "
            "Saturday emerged as the busiest sales day, driven by enthusiastic family crowds visiting the school grounds. "
            "This analytical comparison allows the young organizers to plan ingredient inventory wisely for future events, demonstrating how practical data handling guides real-world planning, budgeting, and financial decision making in community activities."
        ),
        "checkpoints": [
            {
                "q": "Which day experienced the highest total sales of food items (90 portions)?",
                "options": ["Friday", "Saturday", "Sunday", "Monday"],
                "ans": 1,
                "exp": "Saturday had 40 fruit chaats + 50 sandwiches = 90 portions, the highest of the weekend."
            },
            {
                "q": "How many more sandwiches (120 total) were sold than fruit chaats (90 total) over the 3 days?",
                "options": ["20 more", "25 more", "30 more", "40 more"],
                "ans": 2,
                "exp": "120 − 90 = 30 more sandwiches were sold."
            }
        ]
    },
    {
        "id": 11,
        "title": "Geometric Dienes Blocks",
        "section": "Spatial Representations & Base-Ten Models",
        "speech": (
            "In our hands-on mathematics laboratory, spatial data and numerical values come alive through geometric manipulatives known as Dienes base-ten blocks. "
            "These structured blocks build a powerful tactile bridge connecting single units, grouping structures, and multi-digit place value understanding in arithmetic. "
            "The smallest manipulative is the unit cube, measuring exactly one centimeter along each edge and representing the value of one single unit. "
            "When we connect ten unit cubes linearly end-to-end, they form a ten-rod or long, representing the value of ten. "
            "Arranging ten ten-rods side by side produces a square flat, containing one hundred unit cubes and modeling the hundreds place. "
            "Stacking ten hundreds flats vertically constructs a large cube, containing one thousand unit cubes and representing the thousands place. "
            "Young investigators can represent any multi-digit quantity physically by grouping these geometric forms on their laboratory desks. "
            "For instance, the quantity one thousand two hundred and thirty-four is formed using one thousands cube, two hundreds flats, three tens rods, and four unit cubes. "
            "By handling these concrete blocks, students visualize how place values grow tenfold at each successive step, linking three-dimensional geometry directly with Hindu-Arabic decimal numeration and structured mathematical reasoning. "
            "Observing these physical representations transforms abstract numbers into tangible geometric realities that make arithmetic completely intuitive."
        ),
        "checkpoints": [
            {
                "q": "How many unit cubes are combined to build a single hundreds flat?",
                "options": ["10 unit cubes", "50 unit cubes", "100 unit cubes", "1,000 unit cubes"],
                "ans": 2,
                "exp": "A flat consists of 10 rods of 10 cubes each, totaling 10 × 10 = 100 unit cubes."
            },
            {
                "q": "Which base-ten manipulative represents the value of one thousand?",
                "options": ["A unit cube", "A tens rod", "A hundreds flat", "A thousands block (cube of 10 flats)"],
                "ans": 3,
                "exp": "10 hundreds flats stacked together form a thousands cube."
            }
        ]
    },
    {
        "id": 12,
        "title": "Folding Three-Dimensional Nets",
        "section": "Geometric Unfolding & Spatial Nets",
        "speech": (
            "Let us continue our laboratory exploration by investigating two-dimensional nets that fold into solid three-dimensional geometric figures. "
            "A geometric net is a flat, unfolded pattern of two-dimensional polygons that can be creased and folded along its edges to construct a hollow three-dimensional solid without any gaps or overlapping faces. "
            "Consider a cube: its flat net consists of six congruent square faces arranged in specific planar patterns, such as a cross or a T-shape. "
            "When we fold the surrounding squares upward at right angles, they meet edge to edge to form the six faces of a perfect cube. "
            "Similarly, a rectangular prism or cuboid unfolds into six rectangular faces paired into three opposite congruent sets. "
            "A triangular prism unfolds into two congruent triangular bases connected by three rectangular side faces along their borders. "
            "A square pyramid unfolds into a central square base surrounded by four isosceles triangles that fold upward to meet at a single apex. "
            "Practicing spatial unfolding teaches young geometers to visualize how surface areas envelop three-dimensional volumes, strengthening spatial reasoning, manual dexterity, and geometric data analysis across practical mathematics and engineering projects. "
            "Constructing paper models allows students to explore geometric properties through hands-on creative experimentation."
        ),
        "checkpoints": [
            {
                "q": "How many flat square faces make up the net of a cube?",
                "options": ["4 faces", "5 faces", "6 faces", "8 faces"],
                "ans": 2,
                "exp": "A cube has exactly 6 equal square faces."
            },
            {
                "q": "What shapes make up the net of a square pyramid?",
                "options": ["6 rectangles", "1 square base and 4 triangular faces", "2 triangles and 3 rectangles", "4 circles"],
                "ans": 1,
                "exp": "A square pyramid consists of 1 square base and 4 triangular side faces meeting at an apex."
            }
        ]
    },
    {
        "id": 13,
        "title": "Place Value Cards",
        "section": "Arrow Cards & Expanded Notation",
        "speech": (
            "To deepen our mastery of multi-digit numbers, our laboratory uses place value arrow cards to deconstruct and assemble standard numerals dynamically. "
            "Each set of arrow cards contains color-coded cards cut with a pointed arrow tip on the right edge: "
            "thousands cards ending in three zeros, hundreds cards ending in two zeros, tens cards ending in one zero, and single-digit ones cards. "
            "To assemble the four-digit number four thousand three hundred and twenty-five, an investigator selects four specific cards: "
            "the four thousand card, the three hundred card, the twenty card, and the five card. "
            "When these cards are stacked so that their right-hand arrow tips align perfectly, the smaller cards cover the trailing zeros of the larger cards beneath them. "
            "The layered stack displays the clean compact numeral four thousand three hundred and twenty-five. "
            "When we pull the cards apart, the expanded notation reveals itself instantly: four thousand plus three hundred plus twenty plus five. "
            "Arrow cards eliminate common student confusion regarding the digit zero and place value holding across columns. "
            "They physically demonstrate that every digit value depends entirely upon the position it occupies within our decimal number system, reinforcing essential number sense and building lasting computational confidence."
        ),
        "checkpoints": [
            {
                "q": "Which four expanded cards combine to assemble the number 4,325?",
                "options": ["400 + 30 + 20 + 5", "4,000 + 300 + 20 + 5", "4,000 + 3,000 + 25", "4 + 3 + 2 + 5"],
                "ans": 1,
                "exp": "4,325 = 4,000 + 300 + 20 + 5 in expanded notation."
            },
            {
                "q": "What happens when arrow cards are stacked with their arrow tips aligned?",
                "options": ["They get hidden completely", "The non-zero digits cover the trailing zeros to show the standard numeral", "The numbers multiply together", "The cards turn into fractions"],
                "ans": 1,
                "exp": "Aligning the tips superimposes the cards so each digit sits in its exact place value."
            }
        ]
    },
    {
        "id": 14,
        "title": "Fraction Strip Kit",
        "section": "Visual Proportions & Fraction Strips",
        "speech": (
            "Our laboratory toolkit also includes colorful fraction strips that allow students to compare parts of a whole with tactile precision. "
            "Each fraction strip is identical in total length, representing one whole unit benchmark of twenty-four centimeters. "
            "The top whole strip is undivided and labeled with the number one. "
            "The next strip is partitioned into two equal segments, each measuring twelve centimeters and labeled one half. "
            "Subsequent strips are divided into three equal segments of one third, four equal segments of one fourth, "
            "six equal segments of one sixth, eight segments of one eighth, and twelve segments of one twelfth along the scale. "
            "By aligning different strips side by side along a centimeter ruler, young learners discover visual equivalence and fractional relationships directly. "
            "They observe that two one-fourth pieces fit exactly over one one-half piece, proving visually that two fourths equals one half. "
            "Similarly, four one-eighth pieces match two one-fourth pieces and one one-half piece with absolute perfection. "
            "Fraction strips transform abstract fraction notation into concrete spatial measurements, helping children understand how fractional pieces combine, compare, and relate to the unifying whole in practical measurement and sharing situations. "
            "This visual model nurtures deep conceptual clarity in fraction arithmetic."
        ),
        "checkpoints": [
            {
                "q": "How many one-fourth (1/4) strips are equal in length to a one-half (1/2) strip?",
                "options": ["1 strip", "2 strips", "3 strips", "4 strips"],
                "ans": 1,
                "exp": "2 × 1/4 = 2/4 = 1/2, so two 1/4 strips equal one 1/2 strip."
            },
            {
                "q": "If the whole strip is 24 cm long, how long is each one-third (1/3) segment?",
                "options": ["6 cm", "8 cm", "12 cm", "16 cm"],
                "ans": 1,
                "exp": "24 cm ÷ 3 = 8 cm."
            }
        ]
    },
    {
        "id": 15,
        "title": "Word Problem Models",
        "section": "Bar Modeling & Problem Solving Structures",
        "speech": (
            "When young mathematicians encounter complex word problems, drawing visual bar models or box diagrams transforms confusing sentences into clear mathematical equations. "
            "Mathematical word problems generally fall into three primary structural models: combine problems, change problems, and compare problems. "
            "In a combine model, two or more known parts are placed side by side inside a bar diagram to find the unknown total whole, using addition. "
            "For example, if twenty-four boys and twenty-four girls join a survey, two adjacent bars of twenty-four combine to equal forty-eight students. "
            "In a change model, an initial quantity increases through an incoming addition or decreases through an outgoing subtraction to produce a new resulting amount. "
            "In a compare model, two parallel bars of different lengths represent two distinct quantities, highlighting the difference between them clearly. "
            "For instance, comparing one hundred and twenty sandwiches with ninety fruit chaats shows a longer bar alongside a shorter bar, with a difference gap of thirty portions. "
            "Drawing bar models externalizes mental thinking onto paper, allowing students to select the correct arithmetic operation with calm clarity, structural confidence, and unwavering accuracy in every mathematical investigation. "
            "Visual schematics make problem solving enjoyable, approachable, and transparent for every curious student."
        ),
        "checkpoints": [
            {
                "q": "Which visual model uses two parallel bars of different lengths to show the difference between quantities?",
                "options": ["Combine model", "Compare model", "Change model", "Circle model"],
                "ans": 1,
                "exp": "A compare model contrasts two parallel bars to highlight their difference."
            },
            {
                "q": "In a combine model with parts 24 and 24, what is the unknown whole?",
                "options": ["0", "24", "48", "96"],
                "ans": 2,
                "exp": "24 + 24 = 48 is the combined whole."
            }
        ]
    },
    {
        "id": 16,
        "title": "Integrated Data Analysis",
        "section": "Synthesis & Multimodal Data Mastery",
        "speech": (
            "As we reach the synthesis stage of our laboratory curriculum, let us celebrate how all our mathematical tools unite into a comprehensive data analysis system. "
            "We began by framing targeted, unambiguous survey questions to gather high quality primary data from our classroom peers. "
            "We recorded raw responses efficiently using standardized letter abbreviations before organizing forty-five student preferences into clear frequency tables. "
            "We applied tally bundling rules with diagonal slashes to keep counts error-free, and designed scaled pictographs where single icons represented five food servings. "
            "We analyzed multi-variable relationships using two-way contingency matrices, verifying that row and column totals balanced across both genders. "
            "Furthermore, we connected our data investigations to physical manipulatives, examining base-ten Dienes blocks, three-dimensional geometric nets, place value arrow cards, and fraction comparison strips. "
            "Finally, we structured mathematical stories using bar models to solve arithmetic problems systematically and logically. "
            "Data handling empowers you to investigate the world, ask meaningful questions, collect reliable evidence, and communicate truths clearly to others. "
            "With these analytical skills, you are fully equipped to interpret information thoughtfully, solve real-world challenges, and appreciate the elegance of mathematics in everyday life. "
            "Keep questioning, observing, measuring, and discovering patterns wherever you go."
        ),
        "checkpoints": [
            {
                "q": "What is the primary benefit of combining frequency tables, pictographs, and bar models?",
                "options": ["It makes math confusing", "It provides multiple clear ways to understand, analyze, and present data", "It uses more paper", "It replaces the need for numbers"],
                "ans": 1,
                "exp": "Multimodal data representations offer clear, comprehensive views of numerical patterns."
            },
            {
                "q": "Which step in data handling comes first before tabulating and graphing?",
                "options": ["Drawing a pictograph", "Framing clear questions and collecting raw data", "Writing a final report", "Subtracting totals"],
                "ans": 1,
                "exp": "Data handling always begins with question design and data collection."
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
