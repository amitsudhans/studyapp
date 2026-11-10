#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 8: Food We Eat
Data Generator - Part 1 (Slides 1 to 8)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each
- Checkpoints: Exactly 2 per slide with 4 options each
- No human character names (including Shirin), no lecturer personas
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Wholesome Homemade Dishes",
        "subtitle": "Celebrating Nutritious Home-Cooked Meals and Cultural Family Flavors",
        "speech": (
            "Welcome, curious young learners, to our delicious scientific exploration of the wonderful foods that fuel our energetic growing bodies! "
            "Think for a joyful moment about your absolute favorite homemade dish cooked with care inside your family kitchen. Perhaps it is "
            "steaming golden moong dal paired with soft wheat chapatis, fragrant spiced vegetable pulao, crisp dosa with coconut chutney, or warm "
            "homemade kheer drizzled with chopped almonds! Why do homemade meals nourish us far better than packaged factory snacks sold inside "
            "shiny crinkly wrappers? Look right inside your home cooking pot: fresh farm ingredients are washed thoughtfully with clean water, "
            "seasoned lightly with natural digestive spices like turmeric, cumin, and ginger, and prepared cleanly without excess refined sugar, "
            "stale frying oil, or chemical preservatives! Every beloved homemade recipe also carries wonderful family memories, connecting generations "
            "across shared dining mats and lunchboxes. When young learners sketch colorful pictures of their favorite traditional home meals and tell classmates "
            "which healthy farm ingredients went inside each pot, everyone discovers how wonderfully tasty wholesome family nutrition truly is—proving that simple, freshly cooked kitchen dishes "
            "deliver steady athletic stamina, sharp classroom focus, and lasting joyful health every single day of childhood."
        ),
        "checkpoints": [
            {
                "question": "Why are freshly prepared homemade kitchen dishes generally healthier for growing children than packaged factory snacks?",
                "options": [
                    "Homemade meals use clean, washed fresh ingredients without artificial chemical preservatives or stale excess oils",
                    "Factory chips come wrapped in diamond foil that melts in water",
                    "Home kitchens never use vegetables, grains, or gentle spices",
                    "Packaged snacks contain zero sugar, salt, or frying fats"
                ],
                "answer": 0,
                "hint": "Think about cleanliness, fresh farm produce, and chemical preservatives.",
                "explanation": "Home-cooked foods rely on fresh washed ingredients and mild spices, avoiding excess sodium, refined sugars, and artificial preservatives."
            },
            {
                "question": "Which combination represents a wholesome traditional homemade lunch meal?",
                "options": [
                    "Bottled soda and sugary colored candy bars",
                    "Soft wheat rotis, warm yellow lentil dal, cooked spinach, and fresh curd",
                    "Fried salty chips alone inside a plastic packet",
                    "Two scoops of colored ice frost without any grains"
                ],
                "answer": 1,
                "hint": "Look for freshly cooked grains, pulses, greens, and dairy.",
                "explanation": "Roti, dal, leafy vegetables, and curd combine energy carbohydrates, proteins, vitamins, and calcium naturally."
            }
        ]
    },
    {
        "id": 2,
        "title": "Six Culinary Tastes",
        "subtitle": "Discovering Sweet, Sour, Salty, Spicy, Bitter, and Astringent Flavors",
        "speech": (
            "Close your eyes gently and imagine tasting a juicy ripe mango versus biting softly into a tangy lemon wedge! Right across our tiny "
            "pink tongues sit thousands of sensitive microscopic taste buds designed to detect extraordinary flavor dimensions. Culinary science "
            "and Indian food heritage recognize six primary distinct tastes! First comes sweet, found naturally in jaggery, ripe dates, bananas, "
            "and honey—offering quick cellular energy. Second is sour, experienced crisply in tamarind, raw green mangoes, yogurt, and fresh lime "
            "juice. Third is salty, delivered carefully by natural earth and sea salt crystals to maintain body fluid balance. Fourth is spicy or "
            "pungent, sparked warmly by black pepper, ginger, cloves, and green chilies. Fifth is bitter, present inside healthy bitter gourd "
            "(karela) and fenugreek seeds that cleanse digestion. Sixth is astringent—that dry, puckering sensation tasted when nibbling raw amla, "
            "pomegranate peel tea, or unripe bananas! Consider India's fascinating festival tradition of Chhappan Bhog—a magnificent fifty-six dish "
            "celebration platter carefully balancing all six wonderful natural tastes together in harmony! Eating diverse healthy flavors moderately satisfies sensitive taste buds deeply "
            "while nourishing every vital human organ evenly without letting just one strong sweet or overly salty craving dominate our everyday meals."
        ),
        "checkpoints": [
            {
                "question": "How many harmonious traditional tastes are celebrated inside a traditional Chhappan Bhog festival spread?",
                "options": [
                    "Only one single sugary flavor",
                    "Six balanced tastes: sweet, sour, salty, spicy, bitter, and astringent",
                    "Zero natural tastes—only plain warm water",
                    "Two flavors strictly: spicy and sweet"
                ],
                "answer": 1,
                "hint": "Recall the full palette of tastes from sweet mangoes to pungent spices and tart amla.",
                "explanation": "Chhappan Bhog harmonizes all six traditional tastes (sweet, sour, salty, spicy, bitter, and astringent) for complete nourishment."
            },
            {
                "question": "Which natural food provides a healthy bitter taste that aids digestion alongside vitamins?",
                "options": [
                    "Honeycomb syrup",
                    "Bitter gourd (karela) and fenugreek seeds",
                    "Ripe sweet watermelon",
                    "Refined white cane sugar"
                ],
                "answer": 1,
                "hint": "Its very name describes its sharp bitter flavor profile.",
                "explanation": "Bitter gourd (karela) and fenugreek seeds supply healthy bitter compounds beneficial for balanced digestion."
            }
        ]
    },
    {
        "id": 3,
        "title": "The Runner's Diet",
        "subtitle": "Learning Why Balanced Meals Beat Narrow Eating Habits for Athletes",
        "speech": (
            "Picture a spirited Class 3 school sprinter who loved dashing swiftly across muddy grassy tracks faster than almost anyone! Yet despite "
            "practicing sprints diligently every morning, this young runner suddenly began catching frequent fevers, feeling dizzy after short laps, "
            "and struggling with weak legs. Why did such an energetic athlete keep falling sick? One afternoon, a visiting national champion runner "
            "sat kindly beside the young student and asked a straightforward question: what meals appear on your plate every day? Embarrassed, the "
            "young runner admitted pushing aside leafy spinach, lentils, fruits, and milk—eating practically nothing except plain white rice and "
            "fried potatoes at every meal! Smiling gently, the champion explained a fundamental nutrition truth: while rice and potatoes offer starchy "
            "fuel, eating solely two foods leaves growing muscles, red blood, and immune shields completely starved! True endurance requires eating "
            "a bright rainbow variety of whole grains, protein-building pulses, colorful fresh vegetables, juicy seasonal fruits, crunchy nuts, and clean dairy every day. Inspired "
            "deeply by that wise sports lesson, the young Class 3 sprinter began happily enjoying diverse home-cooked daily meals—soon dashing swiftly across the grassy school track finish line feeling stronger, brighter, faster, and completely illness-free every week!"
        ),
        "checkpoints": [
            {
                "question": "Why did the fast Class 3 student sprinter repeatedly fall sick despite eating large plates of rice and potatoes?",
                "options": [
                    "Eating only two starchy foods lacked vital proteins, vitamins, and minerals needed for immunity and strong muscles",
                    "Rice and potatoes are poisonous when eaten on running tracks",
                    "Running slowly causes instant rainstorms inside shoes",
                    "Drinking water causes tiredness during daylight hours"
                ],
                "answer": 0,
                "hint": "Can energy carbohydrates alone build muscles and fight off germs?",
                "explanation": "Relying solely on rice and potatoes causes severe deficiencies in proteins, vitamins, and minerals that fight illness."
            },
            {
                "question": "What golden advice did the seasoned champion runner give to rebuild stamina and immunity?",
                "options": [
                    "Skip breakfast and eat only salty chips before every race",
                    "Eat a balanced variety of grains, pulses, vegetables, fresh fruits, and wholesome home meals",
                    "Eat strictly white sugar spoons every single hour",
                    "Stop drinking clean water on warm afternoons"
                ],
                "answer": 1,
                "hint": "Different food groups perform different jobs inside the human body.",
                "explanation": "A varied balanced diet supplies energy (grains), muscle repair (pulses/dairy), and disease protection (fruits/vegetables)."
            }
        ]
    },
    {
        "id": 4,
        "title": "Balanced Food Plates",
        "subtitle": "Grouping Energy Fuels, Bodybuilding Proteins, and Protective Vitamins",
        "speech": (
            "Building a powerful balanced thali resembles assembling a winning team where every single player holds a special essential job! "
            "Nutritional scientists organize healthy daily foods into three vital cooperative groups so no body system ever goes neglected. Group "
            "one consists of Energy-Giving Foods: whole wheat chapatis, brown rice, ragi, jowar, oats, potatoes, and modest healthy ghee or oils "
            "supplying steady fuel to walk, study, climb stairs, and sprint happily around playgrounds! Group two encompasses Body-Building Foods: "
            "protein-packed dals like moong and toor, chickpeas, kidney beans, fresh paneer, milk, curd, soy, nuts, and eggs serve as living bricks "
            "repairing scraped knees, lengthening growing bones, and strengthening arm muscles! Finally, Group three stars Protective Foods: vibrant "
            "spinach, carrots, pumpkins, tomatoes, guavas, oranges, and apples burst with invisible vitamins and essential minerals acting like vigilant "
            "vigilant bodyguards fighting off seasonal coughs, colds, and infections! Whenever we happily dish up a colorful balanced lunch plate holding golden whole grains, warm protein lentil dal, "
            "bright sautéed leafy vegetables, cool fresh homemade yogurt, and crisp juicy seasonal fruit slices, our whole active body thrives harmoniously together with boundless daily athletic stamina, crystal-clear classroom study focus, and beaming healthy smiles all day!"
        ),
        "checkpoints": [
            {
                "question": "Which food group acts like living building blocks to grow taller and repair muscles in children?",
                "options": [
                    "Sugary fizzy cola sodas",
                    "Protein-rich pulses (dals), chickpeas, milk, paneer, nuts, and eggs",
                    "Refined white table salt crystals",
                    "Artificial yellow food coloring drops"
                ],
                "answer": 1,
                "hint": "Think about body-building foods rich in proteins.",
                "explanation": "Pulses, beans, milk products, nuts, and eggs supply dietary proteins required for bone growth and tissue repair."
            },
            {
                "question": "What vital role do colorful fruits and green leafy vegetables play inside a balanced meal?",
                "options": [
                    "They act as protective foods rich in vitamins and minerals that guard against sickness",
                    "They turn teeth bright green forever",
                    "They stop lungs from breathing oxygen",
                    "They replace drinking water completely"
                ],
                "answer": 0,
                "hint": "Remember why the runner fell sick without vegetables and fruits!",
                "explanation": "Fruits and vegetables provide protective vitamins and minerals that boost immunity and keep skin, eyes, and blood healthy."
            }
        ]
    },
    {
        "id": 5,
        "title": "Cooling Summer Treats",
        "subtitle": "Replenishing Water and Electrolytes During Hot Summer Months",
        "speech": (
            "Step outside during scorching May afternoons when hot golden sunshine warms pavements, and notice what immediately happens along your "
            "forehead and palms: salty perspiration droplets begin glistening across your skin! Sweating acts as Earth's clever personal air conditioner, "
            "evaporating moisture to cool our bodies safely—yet simultaneously losing precious water and vital salts! That biological truth explains "
            "why Indian families instinctively prepare wonderfully refreshing cooling summer foods and drinks throughout hot weather! Crack open "
            "a fresh green tender coconut to sip naturally sterile coconut water packed with hydrating minerals. Stir tangy roasted green mango pulp "
            "with cumin, mint, and jaggery into revitalizing glassfuls of chilled aam panna preventing heat exhaustion! Squeeze fresh yellow limes "
            "into sparkling nimbu pani, blend sweet golden ripe mango shakes, press juicy oranges, or savor creamy frozen homemade kulfi and fruit "
            "ice creams on sunny evenings. Crunchy water-rich summer vegetables and melons—like cucumbers, crisp watermelon, and muskmelon—also consist "
            "of over ninety percent pure refreshing water! Choosing hydrating natural seasonal summer refreshments instead of sugary bottled chemical sodas keeps playful outdoor children remarkably energetic, cool-headed, comfortable, cheerful, and safely well-hydrated "
            "even under intense blistering sunny afternoon summer heatwaves across bustling Indian towns and quiet green villages!"
        ),
        "checkpoints": [
            {
                "question": "Why do families drink tender coconut water, lime water (nimbu pani), and aam panna especially during blistering summer months?",
                "options": [
                    "To quickly replace water and essential body salts lost through summer sweating",
                    "Because coconuts only grow inside frozen snow glaciers",
                    "To increase fever heat during afternoons",
                    "Because drinking water evaporates off plates immediately"
                ],
                "answer": 0,
                "hint": "Think about what your body loses through glistening sweat drops on hot days.",
                "explanation": "Summer sweat drains fluids and salts; drinks like coconut water, aam panna, and lime water rehydrate and cool the body safely."
            },
            {
                "question": "Which refreshing summer fruit is over 90% natural water, making it ideal for cooling hot bodies?",
                "options": [
                    "Dry roasted peanuts",
                    "Juicy red watermelon and crisp green cucumbers",
                    "Dry wheat flour crackers",
                    "Solid salty rock crystals"
                ],
                "answer": 1,
                "hint": "Think of heavy green-striped summer melons sliced cold on hot afternoons.",
                "explanation": "Watermelons and cucumbers carry exceptionally high water content and natural minerals that hydrate thirsty cells swiftly."
            }
        ]
    },
    {
        "id": 6,
        "title": "Warming Winter Meals",
        "subtitle": "Choosing Cozy Soups, Ginger, Nuts, and Seasonal Harvest Foods in Cold Months",
        "speech": (
            "Now fast-forward several months across the spinning calendar until crisp December fog blankets fields and chilly morning breezes prompt "
            "everyone to pull on cozy wool sweaters! Just as summer heat asks for cooling coconut water and crisp salads, chilly winter weather invites "
            "completely different seasonal kitchen favorites! When outdoor temperatures plunge, human bodies burn extra internal energy simply to stay "
            "snugly warm. Stepping back inside after frosty outdoor play, nothing comforts cold hands faster than cradling a steaming bowl of spiced "
            "tomato-carrot soup or creamy lentil shorba seasoned generously with crushed black pepper and fresh ginger! Across Indian households, "
            "winters welcome nutrient-dense seasonal treasures: dark mustard greens (sarson ka saag) paired with golden corn rotis, steaming hot "
            "moong dal khichdi topped with fragrant ghee, roasted peanuts, crispy sesame-jaggery chikki, dates, walnuts, and warm spiced turmeric milk "
            "at cozy bedtime! Eating fresh seasonal winter harvest crops—sweet green peas, crunchy red carrots, snow-white cauliflower, crisp guavas, and juicy sweet oranges ripening naturally right inside cool golden winter sunshine—"
            "ensures nutritious garden vegetables arrive cleanly at peak sweet crispness, budget affordability, and vitamin richness while naturally shielding active loving families safely against bitter freezing winter chills, colds, and sniffles."
        ),
        "checkpoints": [
            {
                "question": "Which cozy homemade food choice naturally warms and energizes the body during chilly winter evenings?",
                "options": [
                    "Icy slush popsicles eaten barefoot in cold wind",
                    "Steaming vegetable soup seasoned with ginger and black pepper, or sesame-jaggery chikki",
                    "Frozen watermelon ice cubes right out of deep freezers",
                    "Chilled soda water without any meals"
                ],
                "answer": 1,
                "hint": "Warm soups, ginger, sesame seeds, and jaggery provide cozy winter calories.",
                "explanation": "Hot soups, warming spices like ginger, and energy-dense winter seeds like sesame and jaggery keep bodies warm and nourished."
            },
            {
                "question": "Why is eating vegetables that grow naturally in the current season—such as winter carrots and peas—a smart habit?",
                "options": [
                    "Seasonal local produce is fresher, tastier, richer in vitamins, and gentler on farm soils",
                    "Seasonal vegetables cost ten times more than imported canned plastics",
                    "Plants only have green leaves during one day a year",
                    "Out-of-season frozen snacks contain higher sunshine vitamin power"
                ],
                "answer": 0,
                "hint": "Freshly harvested seasonal crops spend less time sitting in cold warehouses.",
                "explanation": "Eating in-season crops ensures maximum nutrition, peak flavor, lower transport waste, and harmony with local farming cycles."
            }
        ]
    },
    {
        "id": 7,
        "title": "Regional Indian Foods",
        "subtitle": "Exploring Traditional Dishes Shaped by Local Climate, Crops, and Heritage",
        "speech": (
            "Board an imaginary train journey across India's diverse mountains, coastlines, deserts, and river valleys—and discover how wonderfully "
            "everyday food plates transform from state to state! Why do families in Tamil Nadu and Kerala relish fluffy steamed rice idlis, crispy "
            "dosas, and coconut-rich avial, while families across Punjab savor golden wheat parathas alongside mustard greens and creamy buttermilk? "
            "The fascinating science behind regional cuisine lies in local geography, rainfall, and native crops! Rain-fed coastal plains and river "
            "deltas grow lush emerald rice paddies and towering coconut palms, giving rise to coastal rice dishes, banana-leaf feasts, and tangy coconut "
            "curries across South and East India—from Odisha's cooling fermented pakhala to Bengal's fragrant rice and fish curry! Conversely, drier "
            "sun-drenched northern and western plains thrive cultivating wheat, bajra, chickpeas, and groundnuts—inspiring Gujarat's steamed chickpea "
            "dhokla, Maharashtra's wholesome millet bhakri, and Rajasthan's crisp roasted dal-baati! Up in icy Himalayan mountain valleys, families slurp steaming vegetable noodle "
            "thukpa and warm steamed momos, while traveling cousins cheerfully share fascinating stories of delicious regional dishes sampled across distant Indian states. Celebrating rich regional food diversity teaches young curious learners to respect, enjoy, and deeply cherish every single local community's ingenious culinary heritage and agricultural wisdom!"
        ),
        "checkpoints": [
            {
                "question": "Why do southern and eastern Indian coastal states traditionally feature plenty of rice, coconut, and banana-leaf dishes?",
                "options": [
                    "Abundant monsoon rain and warm coastal climates allow lush rice paddies and coconut groves to thrive there",
                    "Because wheat seeds turn into rocks near oceans",
                    "Coastal trains strictly ban breads and chapatis",
                    "Mountains only exist inside deserts"
                ],
                "answer": 0,
                "hint": "Traditional cuisines always grow around the crops flourishing best in local weather and soil.",
                "explanation": "Local rainfall, temperature, and soil determine which crops thrive—shaping coastal rice-coconut diets versus inland wheat-millet staples."
            },
            {
                "question": "Which popular dish pairs properly with its home culinary region of India?",
                "options": [
                    "Steamed chickpea dhokla in Gujarat, and dal-baati in Rajasthan",
                    "Icy snow soup in scorching desert dunes",
                    "Fresh whale meat in dry central farmland villages",
                    "Fried plastic chips in Himalayan tea gardens"
                ],
                "answer": 0,
                "hint": "Think about chickpea-flour dhokla from western India.",
                "explanation": "Gujarat's fermented chickpea-flour dhokla and Rajasthan's hearty dal-baati reflect local drought-tolerant pulses and grains."
            }
        ]
    },
    {
        "id": 8,
        "title": "Edible Plant Leaves",
        "subtitle": "Identifying Nutritious Farm Leafy Greens Like Spinach, Fenugreek, and Mint",
        "speech": (
            "Now let us embark on an eye-opening field expedition straight into lush green agricultural farms to answer a vital scientific mystery: "
            "exactly WHICH parts of green plants end up cooking inside our lunch plates? Plants do not give humans merely one single part—we harvest "
            "leaves, fruits, roots, stems, and seeds! Let us inspect our very first verdant treasure: Edible Plant Leaves! Walk gently down damp "
            "farm rows sprouting lush emerald foliage. Look at broad, glossy dark leaves of spinach (palak)—brimming with iron that helps crimson "
            "blood cells ferry fresh oxygen throughout energetic muscles! Beside spinach grow feathery, slightly bitter aromatic sprigs of fenugreek "
            "(methi) tucked often into warm winter parathas. Look closely at plump layered heads of green cabbage—actually dozens of tender, tightly "
            "packed overlapping leaves curled gracefully around a short core! Nearby sway broad pungent mustard (sarson) leaves harvested for savory "
            "saag, cooling mint (pudina) crushed into summer chutneys, and fragrant lacy coriander (dhaniya) sprinkled freshly over hot curries. "
            "Always rinse fresh leafy green vegetables gently inside clean kitchen water bowls to wash away tiny garden soil specks before cooking briefly over moderate flames so all delicate natural vitamins "
            "remain vibrant, bright green, wonderfully tasty, and crisp inside your warm meal!"
        ),
        "checkpoints": [
            {
                "question": "Which group contains ONLY vegetables where humans primarily eat the green LEAF part of the plant?",
                "options": [
                    "Carrot, radish, and beetroot",
                    "Spinach (palak), fenugreek (methi), cabbage, mustard (sarson), and coriander",
                    "Potato, ginger, and white onion",
                    "Guava, apple, and sapota"
                ],
                "answer": 1,
                "hint": "Think about broad green leafy bunches sold at vegetable stalls.",
                "explanation": "Spinach, methi, cabbage (tightly folded leaf head), mustard greens, and coriander are all nutritious edible plant leaves."
            },
            {
                "question": "Why is dark leafy spinach (palak) considered especially valuable for growing Class 3 runners?",
                "options": [
                    "It contains rich dietary iron and vitamins that build healthy red blood to carry oxygen to muscles",
                    "It dissolves shoes into green wings",
                    "It holds zero water and zero minerals",
                    "It keeps ears from hearing whistles"
                ],
                "answer": 0,
                "hint": "Remember what mineral builds strong red blood cells!",
                "explanation": "Spinach is packed with iron, calcium, and vitamins that support oxygen transport in blood and steady energy."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part1)} slides for Part 1.")
    for s in slides_part1:
        wc = len(s["speech"].split())
        twc = len(s["title"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} title words) | Speech: {wc} words")
        assert 1 <= twc <= 3, f"Slide {s['id']} title word count {twc} not in 1-3"
        assert 195 <= wc <= 215, f"Slide {s['id']} speech word count {wc} not in 195-215"
    print("All Part 1 assertions passed!")
