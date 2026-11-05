# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 8: Weigh It, Pour It
Part 1: Slides 1 to 8 Data Generator
Strictly 195 to 215 words per speech lecture.
Zero human names (Shrinathan, Mirabai, Raghav, etc. replaced with generic roles).
Clean Unicode throughout (kg, g, L, ml, ₹, ×, +, -, =).
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Market Weight Estimates",
        "section": "Prior Knowledge & Benchmark Comparison",
        "speech": (
            "Welcome young scholars to our fascinating exploration of mass and capacity in our daily world! Whenever "
            "we visit a bustling vegetable market or carry our packed school bags, we intuitively experience the physical "
            "sensation of heaviness and lightness. In earlier grades, we learned that mass measures how heavy an object is, "
            "using standard kilograms as our primary reference unit. Imagine standing before a colorful produce cart loaded "
            "with fruits, leafy greens, and giant round pumpkins. An inquisitive shopper observes a large golden pumpkin "
            "resting on a two-pan balance scale. When cut exactly in half, each half pumpkin perfectly balances two standard "
            "five-hundred-gram metal weights! This delightful observation reveals that each half pumpkin weighs one kilogram, "
            "meaning the whole original pumpkin had a total mass of two kilograms. Estimating weights develops sharp spatial "
            "and numerical judgment. When comparing diverse living creatures, a tiny pet cat weighs about three to four kilograms, "
            "a powerful striped tiger reaches nearly two hundred kilograms, while a magnificent wild elephant exceeds three thousand "
            "kilograms. By evaluating common items around our homes—such as bags of flour, books, and water bottles—we learn to compare "
            "unknown loads against the reliable one-kilogram benchmark, grounding abstract measurement concepts in everyday physical reality."
        ),
        "checkpoints": [
            {
                "q": "If half a pumpkin balances two 500-gram metal weights (1 kg), what is the weight of the whole pumpkin?",
                "options": ["1 kg", "1.5 kg", "2 kg", "4 kg"],
                "ans": 2,
                "exp": "Half a pumpkin weighs 1 kg (500 g + 500 g = 1000 g = 1 kg). Therefore, the whole pumpkin weighs 1 kg + 1 kg = 2 kg."
            },
            {
                "q": "Which of the following animals is naturally the heaviest?",
                "options": ["Domestic cat", "Striped tiger", "Wild elephant", "Golden retriever dog"],
                "ans": 2,
                "exp": "An elephant weighs over 3,000 kg, making it far heavier than a tiger (approx 200 kg) or a cat (approx 4 kg)."
            }
        ]
    },
    {
        "id": 2,
        "title": "Kilograms And Grams",
        "section": "Standard Units of Mass & Fractional Halves",
        "speech": (
            "In the international decimal measurement system, mass is formally quantified using two closely related metric "
            "units: the kilogram for heavier items and the gram for lighter objects. The fundamental conversion rule establishes "
            "that one single kilogram equals exactly one thousand grams. Whenever an item weighs less than one thousand grams, "
            "we describe its mass in smaller gram increments, abbreviated with the letter g. Dividing one thousand grams into equal "
            "fractions produces standard retail packages familiar to every household shopper. Dividing one kilogram into two equal "
            "portions gives five hundred grams, which represents exactly one-half of a kilogram. Furthermore, dividing one thousand "
            "grams into four equal portions yields two hundred fifty grams, representing exactly one-quarter of a kilogram. Combining "
            "three of these quarter portions creates seven hundred fifty grams, known as three-quarters of a kilogram. Understanding "
            "these fractional relationships enables shoppers to convert seamlessly between different package sizes. For instance, "
            "buying two packets of turmeric powder weighing two hundred fifty grams each provides five hundred grams, or half a kilogram "
            "in total. Masterful understanding of kilograms and grams connects fractional arithmetic with practical market packaging, "
            "ensuring accurate estimation, culinary recipe precision, honest mercantile accounting, and fair trade everywhere throughout our communities."
        ),
        "checkpoints": [
            {
                "q": "How many grams are there in one complete kilogram?",
                "options": ["100 grams", "500 grams", "1000 grams", "10000 grams"],
                "ans": 2,
                "exp": "1 kilogram equals exactly 1000 grams."
            },
            {
                "q": "What fractional part of a kilogram is represented by 250 grams?",
                "options": ["One-half (1/2 kg)", "One-quarter (1/4 kg)", "Three-quarters (3/4 kg)", "One-tenth (1/10 kg)"],
                "ans": 1,
                "exp": "1000 g ÷ 4 = 250 g, so 250 g is exactly 1/4 of a kilogram."
            }
        ]
    },
    {
        "id": 3,
        "title": "Balancing Beam Scales",
        "section": "Two-Pan Equilibrium & Tilting Mechanics",
        "speech": (
            "A traditional mechanical beam scale provides an exquisite visual demonstration of mathematical equality and "
            "balance in action. The apparatus consists of a central pivot fulcrum supporting a horizontal crossbar with two identical "
            "suspended pans. When loads placed in both pans possess identical mass, the beam rests perfectly horizontal, indicating "
            "true equilibrium. However, if one pan holds a greater mass, gravity pulls that side downward, causing the beam to tilt "
            "towards the heavier load while lifting the lighter pan into the air. Market vendors use this principle to measure loose "
            "produce against standard iron counterweights. To balance a standard one-kilogram weight resting in the left pan, the vendor "
            "can arrange several combinations of smaller certified packages in the right pan. One could place two five-hundred-gram packs, "
            "or four two-hundred-fifty-gram packets, or even ten one-hundred-gram spice pouches. As long as the combined sum of the weights "
            "equals one thousand grams, the beam levels out in perfect horizontal harmony. Observing beam scale equilibrium reinforces "
            "algebraic balance: whatever is added to or subtracted from one side must be matched on the opposite side to maintain perfect "
            "equality and fairness in commerce. Developing intuitive physical balance prepares young minds for advanced equations and reliable civic measurement."
        ),
        "checkpoints": [
            {
                "q": "What happens to a two-pan beam balance when the left pan is heavier than the right pan?",
                "options": ["The left pan rises up", "The left pan tilts downward", "Both pans remain level", "The scale spins around"],
                "ans": 1,
                "exp": "Gravity pulls the heavier load down, causing the heavier pan to tilt downward."
            },
            {
                "q": "How many 250-gram packets are needed to balance a 1-kilogram standard weight?",
                "options": ["2 packets", "3 packets", "4 packets", "5 packets"],
                "ans": 2,
                "exp": "4 × 250 g = 1000 g = 1 kg, so exactly 4 packets are required."
            }
        ]
    },
    {
        "id": 4,
        "title": "Sweet Box Packaging",
        "section": "Decomposing One Kilogram into Modular Packets",
        "speech": (
            "Inside a traditional sweet confectionery shop, an expert vendor prepares diamond-shaped cashew sweets, known as "
            "kaju-katli, for festive celebrations. A freshly prepared batch weighing exactly one kilogram must be distributed "
            "into gift boxes of various designated capacities. The packaging puzzle explores how many boxes of a given size are "
            "required to hold the entire one-kilogram sweet batch without leaving any surplus. If the vendor selects five-hundred-gram "
            "boxes, dividing one thousand grams by five hundred demonstrates that exactly two boxes are needed. If the vendor chooses "
            "smaller two-hundred-fifty-gram boxes, dividing one thousand by two hundred fifty reveals that four boxes are required. "
            "Furthermore, using compact one-hundred-gram boxes requires ten full boxes, because ten multiplied by one hundred equals "
            "one thousand grams. Finally, if miniature fifty-gram sample cartons are selected, one thousand divided by fifty yields "
            "twenty boxes! Notice the fundamental inverse relationship: as the box capacity decreases, the total number of boxes "
            "required increases proportionally. Dividing a fixed mass into modular subsets strengthens division concepts, illustrates "
            "unit partitioning, and highlights how packaging engineers and merchants organize inventory efficiently to meet consumer "
            "demands and festive orders across diverse community celebrations, retail markets, and joyful household gatherings worldwide."
        ),
        "checkpoints": [
            {
                "q": "How many 100-gram sweet boxes can be packed from 1 kilogram of kaju-katli sweets?",
                "options": ["5 boxes", "10 boxes", "15 boxes", "20 boxes"],
                "ans": 1,
                "exp": "1000 g ÷ 100 g = 10 boxes."
            },
            {
                "q": "If miniature 50-gram cartons are used, how many cartons are needed for 1 kilogram?",
                "options": ["10 cartons", "15 cartons", "20 cartons", "25 cartons"],
                "ans": 2,
                "exp": "1000 g ÷ 50 g = 20 cartons."
            }
        ]
    },
    {
        "id": 5,
        "title": "Object Weight Comparisons",
        "section": "Spice Packs & Everyday Classroom Balances",
        "speech": (
            "In our school mathematics laboratory, students conduct hands-on balancing experiments comparing small classroom "
            "stationery items with standard commercial spice packets. Suppose a pan scale holds a small ten-gram packet of turmeric "
            "powder in the left pan. By placing rubber pencil erasers into the right pan one by one, students discover that two identical "
            "erasers bring the scale into perfect horizontal equilibrium! Dividing ten grams by two reveals that each rubber eraser weighs "
            "exactly five grams. Next, students test a twenty-gram box of saffron. Since each eraser weighs five grams, placing four erasers "
            "in the opposite pan balances the twenty-gram saffron box perfectly. What if we test a fifty-gram spice pouch? Dividing fifty "
            "by five shows that ten erasers are required. These experiments demonstrate indirect measurement: when standard metal gram "
            "weights are unavailable, any calibrated, uniform object can serve as a dependable secondary measuring unit. Comparing "
            "erasers, sharpeners, paperclips, and spice sachets trains students to reason proportionally about light masses, verify "
            "equilibrium, and appreciate that even tiny objects possess measurable gravitational mass in our physical universe. Practical "
            "classroom experimentation brings mathematical equations to vibrant life, fostering genuine curiosity, keen scientific inquiry, systematic reasoning, and collaborative investigation skills."
        ),
        "checkpoints": [
            {
                "q": "If 2 identical erasers balance a 10-gram spice packet, what is the weight of one eraser?",
                "options": ["2 grams", "5 grams", "8 grams", "10 grams"],
                "ans": 1,
                "exp": "10 g ÷ 2 = 5 grams per eraser."
            },
            {
                "q": "How many 5-gram erasers are needed to balance a 50-gram packet of spices?",
                "options": ["5 erasers", "8 erasers", "10 erasers", "15 erasers"],
                "ans": 2,
                "exp": "50 g ÷ 5 g = 10 erasers."
            }
        ]
    },
    {
        "id": 6,
        "title": "Weighing Machine Types",
        "section": "Scales in Daily Life & Household Consumption",
        "speech": (
            "Across homes, farms, hospitals, and markets, people employ several distinct types of weighing machines tailored "
            "to specific loads and measurement environments. The classic two-pan beam balance compares unknown goods directly against "
            "calibrated counterweights through gravitational equilibrium. The spring balance utilizes Hooke's elastic principle: an "
            "internal steel spring stretches proportionally as a load hangs from its hook, indicating weight on a vertical numbered "
            "dial, ideal for weighing gas cylinders or fisherman catches. In modern grocery stores and sweet shops, sensitive digital "
            "electronic scales display weight instantaneously down to single grams using internal electronic strain sensors. For bulk "
            "cargo, heavy-duty platform scales measure massive fifty-kilogram sacks of wheat, rice, and pulses. Families rely on these "
            "instruments to track monthly household consumption. A typical four-member family consumes approximately fifteen kilograms "
            "of wheat flour, ten kilograms of rice, five kilograms of assorted lentils, and three kilograms of sugar every month. "
            "Selecting the correct weighing apparatus ensures precision, durability, and convenience, whether verifying baby health at a "
            "medical clinic, buying spices, or loading freight trucks. Thoughtful observation of diverse weighing devices connects mechanical engineering "
            "with everyday arithmetic, fostering wise resource management, public health, and scientific problem solving across modern communities."
        ),
        "checkpoints": [
            {
                "q": "Which weighing device uses an internal stretching spring to measure suspended loads like gas cylinders?",
                "options": ["Digital micro balance", "Spring balance", "Two-pan beam scale", "Measuring cup"],
                "ans": 1,
                "exp": "A spring balance measures weight through the extension of an internal coiled spring."
            },
            {
                "q": "If a household consumes 15 kg of flour and 10 kg of rice monthly, what is their combined staple consumption?",
                "options": ["20 kg", "25 kg", "30 kg", "35 kg"],
                "ans": 1,
                "exp": "15 kg + 10 kg = 25 kg total grain consumption."
            }
        ]
    },
    {
        "id": 7,
        "title": "Heavy Load Multiples",
        "section": "Large Mass Multiples & Real-World Matching",
        "speech": (
            "When dealing with larger items, calculating multiples of one kilogram allows us to conceptualize substantial loads "
            "efficiently. If a wholesale grain store stocks sacks of wheat flour, one heavy sack may weigh ten kilograms, meaning "
            "it contains the equivalent of ten individual one-kilogram packets. A larger sack of basmati rice might weigh twenty-five "
            "kilograms, containing twenty-five one-kilogram packets, while an industrial jute sack holds fifty kilograms of grain, "
            "equaling fifty one-kilogram packets combined! Estimating large masses requires connecting numerical quantities with "
            "tangible real-world objects. For instance, an empty metal cooking gas cylinder weighs about fifteen kilograms, whereas "
            "a sturdy wooden dining chair weighs roughly six to eight kilograms. In the animal kingdom, a large domestic dog weighs "
            "around twenty-five kilograms, a royal Bengal tiger reaches two hundred fifty kilograms, and a full-grown rhinoceros exceeds "
            "two thousand kilograms! Associating realistic weight ranges with living creatures and household freight prevents absurd "
            "estimation blunders. Mastering mass multiples builds strong mental proportional reasoning, preparing young learners for "
            "advanced physics, cargo logistics, and practical trade calculations in everyday community life, commerce, agricultural trade, freight transport, industrial warehousing, vehicle weight checkpoints, and global shipping operations efficiently, smoothly, and safely across every highway route."
        ),
        "checkpoints": [
            {
                "q": "How many 1-kilogram packets make up a large 50-kilogram sack of wheat?",
                "options": ["25 packets", "50 packets", "75 packets", "100 packets"],
                "ans": 1,
                "exp": "50 kg ÷ 1 kg = 50 packets."
            },
            {
                "q": "Which object's weight is most realistically estimated at around 15 kilograms?",
                "options": ["A lead pencil", "An empty domestic gas cylinder", "A full-grown rhinoceros", "A plastic ruler"],
                "ans": 1,
                "exp": "A standard empty metal LPG gas cylinder weighs approximately 14 to 15 kg."
            }
        ]
    },
    {
        "id": 8,
        "title": "Olympic Weightlifting Feat",
        "section": "Athletic Strength Ratios & Comparative Lift Math",
        "speech": (
            "The world of sports provides an awe-inspiring demonstration of human strength through Olympic weightlifting! At the "
            "Tokyo Olympic Games, an accomplished Indian female weightlifter achieved a historic silver medal in the women's "
            "forty-nine-kilogram division by lifting a monumental total of two hundred two kilograms across the snatch and clean-and-jerk "
            "disciplines. Let us analyze this extraordinary athletic achievement mathematically! The athlete competed in the forty-nine-kilogram "
            "bodyweight category, which means her own body mass was under forty-nine kilograms. Yet, she successfully hoisted barbell weights "
            "totaling two hundred two kilograms above her head! Dividing two hundred two by forty-nine reveals that she lifted more than "
            "four times her own body mass! To put this feat into perspective, lifting two hundred two kilograms is equivalent to raising "
            "more than eight heavy twenty-five-kilogram sacks of rice simultaneously, or balancing fifty full-grown domestic cats in the air! "
            "Weightlifting relies on biomechanical leverage, rigorous training, and profound discipline. Analyzing athletic lifting ratios "
            "connects sports celebrations with comparative division, percentage strength multipliers, and deep appreciation for dedicated "
            "human achievement on the international world stage. Inspiring sports achievements remind us that discipline, dedication, rigorous "
            "training, and mathematical mechanics combine to produce incredible athletic excellence across our world."
        ),
        "checkpoints": [
            {
                "q": "If an athlete weighing 49 kg lifts a total of 202 kg, about how many times her bodyweight did she lift?",
                "options": ["About 2 times", "About 3 times", "More than 4 times", "About 10 times"],
                "ans": 2,
                "exp": "49 × 4 = 196 kg, and 202 kg > 196 kg, so she lifted more than 4 times her bodyweight."
            },
            {
                "q": "How many 25-kg bags of rice equal 200 kg in total weight?",
                "options": ["4 bags", "6 bags", "8 bags", "10 bags"],
                "ans": 2,
                "exp": "200 kg ÷ 25 kg = 8 bags."
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
