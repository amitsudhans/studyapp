# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 8: Weigh It, Pour It
Part 2: Slides 9 to 16 Data Generator
Strictly 195 to 215 words per speech lecture.
Zero human names (Shrinathan, Mirabai, Raghav, etc. replaced with generic roles).
Clean Unicode throughout (kg, g, L, ml, ₹, ×, +, -, =).
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Litres And Millilitres",
        "section": "Metric Units of Liquid Capacity",
        "speech": (
            "Now let us turn our scientific attention from solid weight to the wondrous world of liquid capacity! Capacity "
            "measures the total volume of fluid that a container can hold. In the international metric system, liquids such as "
            "pure drinking water, fresh milk, cooking oil, fruit juices, and liquid medicines are measured using two standard "
            "units: litres and millilitres. We abbreviate litre with a capital letter L and millilitre with the small letters "
            "ml. The foundational conversion identity states that one single litre equals exactly one thousand millilitres. To grasp "
            "these units intuitively, observe common items around our homes and school kitchens. A standard personal reusable "
            "water bottle holds approximately one litre, while a family cooking oil jug holds five litres. Conversely, small fluid "
            "quantities are quantified using millilitres. A porcelain teacup holds about one hundred fifty millilitres, a ceramic soup "
            "bowl holds roughly three hundred millilitres, and a small glass tumbler holds two hundred fifty millilitres. Whenever "
            "measuring liquids, observing graduated container markings allows accurate pouring without spills. Connecting millilitres "
            "with litres strengthens decimal understanding, enabling students to compare beverage bottles, evaluate fluid recipes, "
            "and calculate liquid quantities reliably across diverse daily activities, scientific experiments, kitchen cooking, and health routines."
        ),
        "checkpoints": [
            {
                "q": "How many millilitres (ml) are in one standard litre (L)?",
                "options": ["100 ml", "500 ml", "1000 ml", "10000 ml"],
                "ans": 2,
                "exp": "1 litre equals exactly 1000 millilitres."
            },
            {
                "q": "Which container most commonly holds about 1 litre of liquid?",
                "options": ["A small teaspoon", "A standard reusable water bottle", "An eye dropper", "A kitchen sink"],
                "ans": 1,
                "exp": "A standard personal drinking water bottle typically holds 1 litre (1000 ml)."
            }
        ]
    },
    {
        "id": 10,
        "title": "Fractional Litre Measures",
        "section": "Half, Quarter, and Three-Quarter Litres",
        "speech": (
            "Just as we explored fractional subdivisions of one kilogram, dividing one litre into equal fractional parts "
            "unveils fundamental mathematical patterns. Since one full litre equals one thousand millilitres, dividing one litre "
            "into two equal portions yields five hundred millilitres, universally recognized as one-half of a litre. Similarly, "
            "dividing one thousand millilitres into four equal portions yields two hundred fifty millilitres, representing one-quarter "
            "of a litre. If we combine three quarter-litre portions together, two hundred fifty multiplied by three produces seven "
            "hundred fifty millilitres, which is three-quarters of a litre! These fractional benchmarks appear on grocery shelves "
            "every single day. For instance, cold milk pouches frequently come in convenient five-hundred-millilitre packets, while "
            "single-serving yogurt or fruit juice boxes contain two hundred fifty millilitres. Consider pouring milk for breakfast: "
            "combining two five-hundred-millilitre pouches fills a one-litre jug completely, because five hundred plus five hundred "
            "equals one thousand millilitres. Likewise, four two-hundred-fifty-millilitre cartons together equal one full litre. Practicing "
            "fractional liquid arithmetic deepens understanding of volume conservation, showing that total capacity remains identical "
            "whether packaged in one single large container or distributed among several proportional smaller vessels throughout daily life, ensuring fair trade and consistent nutritional intake across households."
        ),
        "checkpoints": [
            {
                "q": "What volume in millilitres corresponds to one-half of a litre (1/2 L)?",
                "options": ["250 ml", "500 ml", "750 ml", "1000 ml"],
                "ans": 1,
                "exp": "1000 ml ÷ 2 = 500 ml."
            },
            {
                "q": "How many 250 ml cartons of juice are needed to make 1 full litre?",
                "options": ["2 cartons", "3 cartons", "4 cartons", "5 cartons"],
                "ans": 2,
                "exp": "1000 ml ÷ 250 ml = 4 cartons."
            }
        ]
    },
    {
        "id": 11,
        "title": "Droppers And Spoons",
        "section": "Miniature Volumes & Medical Dosing Cups",
        "speech": (
            "When dealing with medical treatments, laboratory chemistry, and delicate infant care, liquids must be measured in "
            "exceedingly small, precise doses where even a single millilitre matters. For such miniature quantities, standard litre jugs "
            "are completely unsuitable. Instead, medical professionals and caregivers utilize specialized tools including eyedroppers, "
            "calibrated dosing spoons, and miniature measuring cups. A single slender eyedropper dispenses liquid drop by drop, where "
            "approximately twenty tiny drops equal one millilitre of fluid! A pediatric doctor might prescribe two millilitres of eye drops "
            "or vitamin syrup for a sick child. A standard household medicine teaspoon holds approximately five millilitres of liquid, "
            "while a calibrated dosing cup typically features marks for five millilitres, ten millilitres, and fifteen millilitres. If "
            "a patient takes ten millilitres of cough syrup twice daily, they consume twenty millilitres each day. Over five days, that "
            "totals one hundred millilitres, which matches the full contents of a standard syrup bottle! Precise measurement in millilitres "
            "protects human health, prevents underdosing or overdosing, and underscores the vital importance of metric precision in healthcare, "
            "pharmaceutical preparation, scientific experiments, and clinical laboratories, veterinary medicine, and scientific research institutes worldwide across our modern civilized society, keeping families safe, healthy, and protected."
        ),
        "checkpoints": [
            {
                "q": "About how many millilitres does a standard calibrated medicine teaspoon hold?",
                "options": ["1 ml", "5 ml", "50 ml", "100 ml"],
                "ans": 1,
                "exp": "A standard medicine teaspoon holds approximately 5 ml of liquid."
            },
            {
                "q": "If a patient takes 10 ml of medicine twice daily for 5 days, what is the total volume consumed?",
                "options": ["50 ml", "75 ml", "100 ml", "200 ml"],
                "ans": 2,
                "exp": "Daily dose = 10 ml × 2 = 20 ml. Over 5 days = 20 ml × 5 = 100 ml."
            }
        ]
    },
    {
        "id": 12,
        "title": "Perfumed Oil Bottles",
        "section": "Packaging Liquids into Modular Retail Containers",
        "speech": (
            "In traditional artisan perfumeries and essential oil workshops, aromatic floral extracts and perfumed hair oils "
            "are manufactured in bulk and subsequently packaged into elegant glass vials of various convenient retail capacities. "
            "Suppose a master artisan prepares a large master container containing exactly one litre of concentrated rose-scented "
            "hair oil. The packaging challenge asks how many smaller bottles of a given capacity can be filled from this single one-litre "
            "supply. First, we convert one litre into its equivalent metric value: one thousand millilitres. If the artisan selects "
            "one-hundred-millilitre bottles, dividing one thousand by one hundred demonstrates that exactly ten bottles can be filled. "
            "What if elegant fifty-millilitre travel vials are selected? Dividing one thousand by fifty reveals that twenty bottles can "
            "be filled. Alternatively, if larger two-hundred-millilitre bottles are chosen, dividing one thousand by two hundred yields "
            "five complete bottles. Notice how liquid division mirrors our earlier sweet box packaging: a fixed master volume divides "
            "evenly into smaller modular containers. The smaller each retail bottle, the greater the number of bottles produced. Understanding "
            "this inverse proportion enables small business owners, packaging technicians, and warehouse managers to calculate production yields, "
            "label retail inventory accurately, and serve community customers effectively."
        ),
        "checkpoints": [
            {
                "q": "How many 100 ml bottles can be filled from 1 litre of perfumed oil?",
                "options": ["5 bottles", "10 bottles", "15 bottles", "20 bottles"],
                "ans": 1,
                "exp": "1000 ml ÷ 100 ml = 10 bottles."
            },
            {
                "q": "If miniature 50 ml vials are used, how many vials can be filled from 1 litre?",
                "options": ["10 vials", "15 vials", "20 vials", "25 vials"],
                "ans": 2,
                "exp": "1000 ml ÷ 50 ml = 20 vials."
            }
        ]
    },
    {
        "id": 13,
        "title": "Milk Measuring Cans",
        "section": "Standard Dairy Dispensers & Additive Volumes",
        "speech": (
            "Every morning across towns and villages, local dairy vendors deliver fresh milk to households using polished "
            "metal dipping cans of specific calibrated capacities. Standard dairy measuring cans come in five certified sizes: "
            "fifty millilitres, one hundred millilitres, two hundred millilitres, five hundred millilitres, and one thousand millilitres, "
            "or one full litre. When customers request specific custom volumes, the dairy vendor combines these standard scoops skillfully. "
            "Suppose a customer requests seven hundred fifty millilitres of fresh milk. The vendor can fill one five-hundred-millilitre can "
            "plus one two-hundred-millilitre can and one fifty-millilitre can, because five hundred plus two hundred plus fifty equals "
            "seven hundred fifty millilitres! Alternatively, the vendor could pour three scoops using the two-hundred-fifty-millilitre measure "
            "if available, or seven scoops of one hundred millilitres plus one fifty-millilitre measure. What if a family orders one litre "
            "and two hundred millilitres? The vendor uses a one-litre can followed by one two-hundred-millilitre can, totaling one thousand "
            "two hundred millilitres. This everyday dairy practice demonstrates additive volume decomposition: any target capacity can "
            "be measured accurately by summing standard calibrated increments. Learning to assemble diverse liquid volumes through mental "
            "addition makes morning marketing quick, transparent, and mathematically enriching for all community members."
        ),
        "checkpoints": [
            {
                "q": "Which combination of standard cans measures exactly 750 ml of milk?",
                "options": ["500 ml + 250 ml", "500 ml + 200 ml + 50 ml", "Three 250 ml scoops", "All of the above"],
                "ans": 3,
                "exp": "All of these combinations equal 750 ml (500+250=750, 500+200+50=750, 3×250=750)."
            },
            {
                "q": "If a vendor pours one 1-litre can and one 200-ml can, what is the total milk poured in millilitres?",
                "options": ["1000 ml", "1100 ml", "1200 ml", "1500 ml"],
                "ans": 2,
                "exp": "1 L = 1000 ml. 1000 ml + 200 ml = 1200 ml."
            }
        ]
    },
    {
        "id": 14,
        "title": "Daily Water Consumption",
        "section": "Household Usage Surveys & Volume Accounting",
        "speech": (
            "Water is our planet's most precious natural resource, sustaining all living beings, agriculture, and industry. "
            "Conducting a household water usage survey helps us understand how many litres of water an average family consumes every "
            "single day. By monitoring daily domestic activities, students discover substantial volume variations across different "
            "household chores. For instance, drinking water accounts for approximately two to three litres per person daily, totaling "
            "about ten litres for a four-member family. Cooking nutritious meals and boiling tea uses another twenty litres. However, "
            "cleaning and hygiene activities consume significantly larger volumes: washing breakfast dishes and cookware takes thirty "
            "litres, mopping floors requires twenty litres, while doing laundry consumes fifty litres. Bathing consumes thirty to forty "
            "litres per individual bucket bath, adding up to nearly one hundred fifty litres for the entire family! Summing all these "
            "activities reveals that a typical household utilizes between two hundred fifty and three hundred litres of fresh water "
            "each day. Quantitative water auditing allows communities to recognize where resource usage is highest, identify wasteful "
            "habits, and appreciate why municipal reservoirs and rainwater systems are essential for sustaining our vibrant towns, cities, "
            "and thriving rural agricultural communities during both monsoon and dry summer seasons alike."
        ),
        "checkpoints": [
            {
                "q": "If a family uses 10 L for drinking, 20 L for cooking, 30 L for dishes, and 140 L for bathing, what is their subtotal?",
                "options": ["180 litres", "200 litres", "220 litres", "250 litres"],
                "ans": 1,
                "exp": "10 + 20 + 30 + 140 = 200 litres."
            },
            {
                "q": "Which household activity typically consumes the greatest volume of water daily?",
                "options": ["Drinking water", "Bathing and washing clothes", "Brushing teeth with a cup", "Boiling tea"],
                "ans": 1,
                "exp": "Bathing and washing laundry collectively consume the largest volumes, often over 150 litres daily per household."
            }
        ]
    },
    {
        "id": 15,
        "title": "Leaking Tap Investigation",
        "section": "Cumulative Wastage Math & Rate Calculations",
        "speech": (
            "A seemingly harmless dripping tap provides a striking mathematical lesson about how small, persistent losses accumulate "
            "into colossal waste over extended periods. Imagine a faulty kitchen faucet that drips at a steady rate of one droplet "
            "every single second. Placing a graduated measuring cylinder beneath the tap reveals that these droplets collect approximately "
            "one litre of clean water every single hour! Let us calculate the shocking cumulative wastage over time. In a single twenty-four-hour "
            "day, twenty-four hours multiplied by one litre equals twenty-four litres of wasted water! Extending this calculation over a full "
            "week of seven days, twenty-four multiplied by seven reveals that one hundred sixty-eight litres of clean potable water are lost "
            "down the drain. Over a standard thirty-day month, multiplying twenty-four litres by thirty yields seven hundred twenty litres! "
            "If five leaking taps in an apartment building remain unrepaired, that building squanders three thousand six hundred litres "
            "of water monthly! Calculating leakage rates proves that tiny drips cannot be dismissed as insignificant. Mathematical rate "
            "multiplication transforms abstract environmental awareness into concrete urgency, motivating us to replace faulty washers, "
            "tighten valves, and protect every drop of our community's water supply, protecting our natural environment for future generations to enjoy."
        ),
        "checkpoints": [
            {
                "q": "If a leaking tap wastes 1 litre of water per hour, how much water is wasted in 1 full day (24 hours)?",
                "options": ["12 litres", "24 litres", "48 litres", "100 litres"],
                "ans": 1,
                "exp": "1 litre/hour × 24 hours = 24 litres."
            },
            {
                "q": "How many litres of water are lost from this single tap in one week (7 days)?",
                "options": ["140 litres", "168 litres", "196 litres", "210 litres"],
                "ans": 1,
                "exp": "24 litres/day × 7 days = 168 litres."
            }
        ]
    },
    {
        "id": 16,
        "title": "Conservation Volume Math",
        "section": "Active Water Conservation & Multiplied Community Impact",
        "speech": (
            "Having discovered the staggering cumulative cost of water leakage, let us apply our mathematical skills to design "
            "and evaluate practical water conservation strategies! Simple daily habit modifications yield tremendous volume savings. "
            "For example, leaving a bathroom tap running continuously while brushing teeth wastes approximately ten litres of water. "
            "If an individual turns off the faucet and uses a small tumbler instead, they use just one-half litre, saving nine and a "
            "half litres per brushing session! Across two brushings daily, that individual conserves nineteen litres every day. In a "
            "school of five hundred students, if every child adopts this mindful practice, the school saves nine thousand five hundred "
            "litres of precious water daily! Furthermore, collecting rooftop rainwater during monsoon showers and storing it in large "
            "ten-thousand-litre community tanks provides abundant clean water for gardening, cleaning, and groundwater replenishment. "
            "Reusing greywater from vegetable rinsing to nourish school garden plants saves another fifty litres each day. Mathematics "
            "empowers us to calculate our collective environmental impact, proving that individual mindful actions, when multiplied across "
            "entire classrooms, neighborhoods, and towns, create powerful sustainable solutions for safeguarding our planet's ecological future, providing clean, reliable freshwater supplies for everyone in our shared communities."
        ),
        "checkpoints": [
            {
                "q": "If one student saves 19 litres of water daily by closing the tap while brushing, how much do 100 students save?",
                "options": ["190 litres", "1900 litres", "19000 litres", "3800 litres"],
                "ans": 1,
                "exp": "19 litres × 100 = 1900 litres saved daily."
            },
            {
                "q": "A school collects 10,000 L of rainwater in a tank. If 500 L are used daily for the garden, how many days will it last?",
                "options": ["10 days", "15 days", "20 days", "25 days"],
                "ans": 2,
                "exp": "10,000 L ÷ 500 L/day = 20 days."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(slides_part2)} slides for Part 2.")
    for s in slides_part2:
        wc = len(s["speech"].split())
        print(f"Slide {s['id']}: {s['title']} -> {wc} words (Title: {len(s['title'].split())} words)")
        assert 195 <= wc <= 215, f"Word count {wc} out of bounds for slide {s['id']}!"
        assert 1 <= len(s['title'].split()) <= 3, f"Title length out of bounds for slide {s['id']}!"
