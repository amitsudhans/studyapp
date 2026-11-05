"""
Script to generate .agents/class6_science_ch3_data.py for
NCERT Class 6 Science Chapter 3: Mindful Eating: A Path to a Healthy Body.
Strictly zero raw LaTeX, zero lecturer persona names, rich comprehensive classroom lectures.
"""

import re

CHAPTER_META = {
    "chapter_num": 3,
    "title": "Mindful Eating: A Path to a Healthy Body",
    "subtitle": "Nutrients, Food Testing Labs, Balanced Diet, Millets & Food Miles",
    "course_type": "Interactive Visual Simulation & Comprehensive Spoken Lectures",
    "class": "Class 6",
    "subject": "Science",
    "curriculum": "NCERT Curiosity (NEP 2020)"
}

SLIDES = [
    {
        "id": 1,
        "badge": "Intro • Life Sustenance",
        "title": "Significance of Food",
        "subtitle": "Ancient Wisdom and the Biological Necessity of Nutrition",
        "theory": """
            <p>From ancient times, Indian thinkers recognized the sacred connection between food and life. The <em>Taittiriya Upanishada</em> proclaims: <strong>'Annena jātāni jīvanti'</strong>—meaning <em>'Food gives life to all living beings'</em>. Similarly, a timeless verse from the <em>Subhashita</em> reminds us that wholesome, moderate, and seasonal food forms the cornerstone of lasting health.</p>
            <p class="mt-2">Food is not merely fuel to satisfy hunger; it is the fundamental raw material that powers every cell in our body:</p>
            <ul class="list-disc pl-5 mt-2 space-y-1 text-slate-300 text-xs sm:text-sm">
                <li><strong>Energy Supply:</strong> Powers bodily warmth, cellular metabolism, movement, and physical work.</li>
                <li><strong>Growth & Tissue Repair:</strong> Supplies building blocks to generate new cells and repair wounds.</li>
                <li><strong>Disease Defense:</strong> Arms the immune system to fight off infections and illnesses.</li>
                <li><strong>Cognitive Function:</strong> Nourishes brain cells to support sharp memory, concentration, and emotional well-being.</li>
            </ul>
        """,
        "lecture": "Welcome to our study of nutrition and mindful eating! Think about what happens when you skip breakfast: by mid-day, you feel sluggish, unable to focus in class, and your energy dips. Why? Because food is our biological power station. For thousands of years, Indian philosophy has celebrated food with the phrase 'Annena jatani jivanti'—food gives life to all living beings. When we eat mindfully—choosing wholesome, seasonal, and freshly prepared meals—we provide our bodies with the precise molecular tools needed to grow tall, think clearly, and build a resilient immune system.",
        "checkpoints": [
            {
                "id": "1-1",
                "question": "What is the profound meaning of the Upanishadic phrase 'Annena jātāni jīvanti'?",
                "options": [
                    "Food is only for celebration",
                    "Food gives life and sustenance to all living beings",
                    "Food should only be eaten at night",
                    "Food causes fatigue"
                ],
                "correct": 1,
                "explanation": "The ancient Sanskrit phrase from the Taittiriya Upanishada emphasizes that food is the primary source of life, energy, and survival."
            },
            {
                "id": "1-2",
                "question": "According to traditional Subhashita wisdom, which three qualities make food healthy?",
                "options": [
                    "Cold, sweet, and packaged",
                    "Wholesome, moderate in quantity, and aligned with the season",
                    "Extremely spicy, oily, and processed",
                    "Deep-fried and salty"
                ],
                "correct": 1,
                "explanation": "Subhashita teaches that wholesome (nutritious), moderate (not overeating), and seasonal food keeps the body disease-free."
            }
        ]
    },
    {
        "id": 2,
        "badge": "3.1 • Regional Diversity",
        "title": "Food in Regions",
        "subtitle": "India's Culinary Tapestry: Crops, Climate, and Regional Staples",
        "theory": """
            <p>Travel across India, and you will discover an astonishing diversity of regional thalis! What people eat daily is intimately shaped by local climate, soil conditions, water availability, and cultural heritage:</p>
            <ul class="list-disc pl-5 mt-2 space-y-2 text-slate-300 text-xs sm:text-sm">
                <li><strong>Northern Plains (e.g., Punjab):</strong> Rich fertile alluvial plains favor wheat and mustard cultivation. Signature staples include hearty <em>Makki di roti</em> (maize flatbread), <em>Sarson da saag</em> (mustard greens), and fresh homemade butter (makhan).</li>
                <li><strong>Southern Deccan (e.g., Karnataka):</strong> Semi-arid red soil regions cultivate drought-hardy millets. Iconic traditional meals feature fiber-rich <em>Ragi mudde</em> (finger millet steamed balls) served with piping hot <em>Sambar</em> and crispy fermented rice-lentil <em>Dosas</em>.</li>
                <li><strong>Northeastern Valleys (e.g., Manipur):</strong> Hilly terrain and abundant monsoon streams foster unique indigenous vegetables and freshwater fish. Celebrated dishes include <em>Eromba</em> (mashed boiled vegetables with fermented fish and chili) and steamed bamboo shoots (<em>Uttis</em>).</li>
            </ul>
        """,
        "lecture": "Have you ever wondered why traditional cuisines vary so dramatically from one state to another? In Punjab, winters are chilly and wheat and mustard grow in abundance, so families enjoy steaming Makki di roti with Sarson da saag. Down in Karnataka, the dry red soil is ideal for growing Ragi, giving rise to wholesome Ragi mudde. In Manipur, surrounded by lush hills and clear streams, traditional meals feature Eromba prepared with seasonal herbs. Our regional cuisines are not accidental—they represent centuries of ecological harmony, matching what the local soil produces with what our bodies need in that climate.",
        "checkpoints": [
            {
                "id": "2-1",
                "question": "Which combination represents a famous traditional staple meal of Punjab?",
                "options": [
                    "Ragi mudde and Sambar",
                    "Makki di roti and Sarson da saag",
                    "Eromba and Uttis",
                    "Idli and Coconut chutney"
                ],
                "correct": 1,
                "explanation": "Makki di roti (cornbread) and Sarson da saag (mustard greens) form Punjab's iconic traditional winter meal."
            },
            {
                "id": "2-2",
                "question": "Why do traditional food habits differ significantly across Indian states?",
                "options": [
                    "Because people in different states cannot cook",
                    "Because regional meals depend on local climate, soil types, water resources, and native crops",
                    "Because state borders prevent spice transport",
                    "Because everyone eats the exact same thing"
                ],
                "correct": 1,
                "explanation": "Regional diets evolved directly around local agriculture, climate conditions, and indigenous harvest cycles."
            }
        ]
    },
    {
        "id": 3,
        "badge": "3.1.2 • Culinary History",
        "title": "Kitchen Evolution",
        "subtitle": "From Clay Chulhas and Stone Grinders to Modern Smart Cooking",
        "theory": """
            <p>The tools and techniques humans use to prepare food have undergone a dramatic transformation over the past century, driven by technological innovations, electricity, and changing lifestyles:</p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 mt-3">
                <div class="p-3 rounded-xl bg-amber-950/40 border border-amber-500/40 text-xs">
                    <span class="font-bold text-amber-300 block mb-1">🏺 Traditional Culinary Practices:</span>
                    <ul class="list-disc pl-4 space-y-1 text-slate-300">
                        <li><strong>Mud Stoves (Chulha):</strong> Wood and dried dung cake fire, producing high heat and slow earthenware cooking, but releasing indoor smoke.</li>
                        <li><strong>Stone Grinders (Sil-Batta):</strong> Heavy granite slabs and rolling stones that crushed spices and pastes while retaining coarse fiber and natural essential oils.</li>
                    </ul>
                </div>
                <div class="p-3 rounded-xl bg-cyan-950/40 border border-cyan-500/40 text-xs">
                    <span class="font-bold text-cyan-300 block mb-1">⚡ Modern Culinary Technologies:</span>
                    <ul class="list-disc pl-4 space-y-1 text-slate-300">
                        <li><strong>LPG Gas & Induction:</strong> Smokeless, instant flame control, energy efficient, and maintaining kitchen cleanliness.</li>
                        <li><strong>Electric Mixer-Grinders:</strong> High-speed stainless steel blades that pulverize spices in seconds, saving physical time and labor.</li>
                    </ul>
                </div>
            </div>
        """,
        "lecture": "Step into your grandmother's village kitchen and compare it with a modern city kitchen! Decades ago, cooking began by lighting a clay chulha using firewood, and spices were patiently ground by hand on a heavy granite sil-batta. While traditional slow cooking in clay pots imparted unique earthy flavors and preserved minerals, it required hours of manual labor and produced smoke. Today, LPG cylinders, smokeless induction hobs, and electric blenders have revolutionized kitchens, saving time and energy. Yet, modern chefs often return to slow clay-pot cooking to rediscover authentic nutritional depth!",
        "checkpoints": [
            {
                "id": "3-1",
                "question": "What traditional manual stone tool was widely used in Indian kitchens to grind fresh spices and chutneys?",
                "options": ["Microwave oven", "Sil-Batta (flat stone and rolling pin)", "Electric blender", "Pressure cooker"],
                "correct": 1,
                "explanation": "The Sil-Batta is an ancient granite stone tool used to grind spices, pastes, and chutneys by hand."
            },
            {
                "id": "3-2",
                "question": "What major environmental and health benefit came from shifting from wood Chulhas to LPG gas stoves?",
                "options": [
                    "Food cooks twice as cold",
                    "Elimination of harmful indoor smoke and particulate soot, protecting respiratory health",
                    "Food loses all its color",
                    "LPG does not require any cooking vessel"
                ],
                "correct": 1,
                "explanation": "LPG provides clean, smokeless combustion, dramatically reducing household air pollution and lung illnesses."
            }
        ]
    },
    {
        "id": 4,
        "badge": "3.2 • Energy Nutrients",
        "title": "Carbohydrates & Energy",
        "subtitle": "Starches and Sugars: The Primary Fuel for Cellular Metabolism",
        "theory": """
            <p>Our bodies require constant energy to breathe, pump blood, walk, and study. The primary, most readily accessible source of daily energy comes from <strong>Carbohydrates</strong>.</p>
            <p class="mt-2">Carbohydrates exist mainly in two chemical forms in our diet:</p>
            <ul class="list-disc pl-5 mt-2 space-y-2 text-slate-300 text-xs sm:text-sm">
                <li><strong>Complex Starches:</strong> Long-chain carbohydrate molecules that break down gradually in the digestive tract, releasing steady, long-lasting energy. Rich dietary sources include whole-grain cereals (wheat, rice, maize, oats), root tubers (potato, sweet potato, tapioca), and green bananas.</li>
                <li><strong>Simple Sugars:</strong> Small molecular carbohydrates that digest rapidly to deliver quick energy bursts. Found naturally in ripe fruits (mango, banana, grapes), honey, sugar cane, and jaggery (gur).</li>
            </ul>
            <p class="mt-2 text-slate-300 text-xs sm:text-sm">
                Carbohydrates and fats are collectively designated as <strong>energy-giving foods</strong>.
            </p>
        """,
        "lecture": "Imagine your body as a high-performance sports vehicle. What is its gasoline? Carbohydrates! When you eat a bowl of warm rice, a whole-wheat chapati, or a boiled potato, your digestive enzymes break down complex starches into glucose. Glucose enters your bloodstream and powers your muscles during running and your brain during exams. Whole grains and root vegetables provide sustained, steady energy that keeps you active for hours without fatigue.",
        "checkpoints": [
            {
                "id": "4-1",
                "question": "Which major nutrient serves as the body's primary and most immediate source of daily energy?",
                "options": ["Carbohydrates", "Minerals", "Vitamin C", "Roughage"],
                "correct": 0,
                "explanation": "Carbohydrates are broken down into glucose, serving as the main metabolic fuel for cellular energy."
            },
            {
                "id": "4-2",
                "question": "Which of the following food groups is exceptionally rich in complex dietary starch?",
                "options": [
                    "Potatoes, rice, and whole wheat",
                    "Mustard oil and butter",
                    "Fish and egg whites",
                    "Iodised salt and lemon juice"
                ],
                "correct": 0,
                "explanation": "Tubers like potatoes and cereals like rice and wheat are packed with complex starchy carbohydrates."
            }
        ]
    },
    {
        "id": 5,
        "badge": "3.2 • Stored Energy",
        "title": "Fats & Stored Energy",
        "subtitle": "Concentrated Reserve Fuel, Cell Membranes, and Thermal Insulation",
        "theory": """
            <p>Like carbohydrates, <strong>Fats</strong> provide energy to our body. In fact, gram-for-gram, fats yield <strong>more than twice the amount of energy</strong> as carbohydrates (1 gram of fat provides approximately 9 kcal, compared to 4 kcal from 1 gram of carbohydrate)!</p>
            <p class="mt-2">Fats are sourced from both plant and animal kingdoms:</p>
            <ul class="list-disc pl-5 mt-2 space-y-1.5 text-slate-300 text-xs sm:text-sm">
                <li><strong>Plant Sources:</strong> Groundnuts, almonds, walnuts, sesame seeds (til), coconut, mustard oil, sunflower oil, and soyabean oil.</li>
                <li><strong>Animal Sources:</strong> Pure ghee, butter, full-cream milk, cheese, paneer, eggs, and oily fish.</li>
                <li><strong>Vital Biological Roles:</strong>
                    <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
                        <li>Long-term stored energy reservoir utilized when food intake is delayed.</li>
                        <li>Subcutaneous fat layer beneath skin acts as thermal insulation against cold.</li>
                        <li>Essential for dissolving and absorbing fat-soluble vitamins (Vitamins A, D, E, and K).</li>
                    </ul>
                </li>
            </ul>
        """,
        "lecture": "Fats often get a bad reputation in casual conversations, but biologically, fats are indispensable! Did you know that one spoonful of pure desi ghee or a handful of roasted peanuts contains over twice the energy of the same weight of sugar? Fats act as our body's long-term backup battery. Furthermore, the delicate cells of our nervous system and brain are insulated by fatty sheaths. Even more crucially, vital vitamins like Vitamin A and Vitamin D cannot be absorbed by your intestines without dietary fats! The key is consuming healthy, unadulterated fats in mindful moderation.",
        "checkpoints": [
            {
                "id": "5-1",
                "question": "Compared to 1 gram of carbohydrate, how much energy does 1 gram of fat supply to the body?",
                "options": [
                    "The exact same amount",
                    "More than double the amount (approximately 9 kcal vs 4 kcal)",
                    "Zero energy",
                    "Half as much"
                ],
                "correct": 1,
                "explanation": "Fats are the most concentrated energy source in food, providing over twice the caloric energy per gram compared to carbohydrates."
            },
            {
                "id": "5-2",
                "question": "Which of these pairs represents healthy plant-based sources of dietary fats?",
                "options": [
                    "Groundnuts and mustard oil",
                    "White sugar and salt",
                    "Cucumber and watermelon",
                    "Boiled potatoes and rice"
                ],
                "correct": 0,
                "explanation": "Groundnuts, sesame, and vegetable oils are rich plant sources of healthy dietary fats and fatty acids."
            }
        ]
    },
    {
        "id": 6,
        "badge": "3.2 • Growth & Repair",
        "title": "Proteins & Body Building",
        "subtitle": "Amino Acids: Structural Blocks for Muscles, Enzymes, and Rapid Growth",
        "theory": """
            <p>Children in their growing years require abundant <strong>Proteins</strong>. Proteins are popularly termed <strong>body-building foods</strong> because they supply the essential building blocks (amino acids) needed to construct new tissues, build strong muscles, develop organs, and repair damaged cells.</p>
            <p class="mt-2">Proteins are abundantly available across diverse vegetarian and non-vegetarian food sources:</p>
            <ul class="list-disc pl-5 mt-2 space-y-2 text-slate-300 text-xs sm:text-sm">
                <li><strong>Plant Sources:</strong> Pulses (dal—moong, chana, toor, urad), soyabeans, kidney beans (rajma), chickpeas (chhole), green peas, almonds, cashews, and edible mushrooms. (Soyabean is the richest plant protein source!).</li>
                <li><strong>Animal Sources:</strong> Cow's milk, curd, paneer (cottage cheese), eggs, fish, and lean meats.</li>
                <li><strong>Critical Functions:</strong> Structural muscle synthesis, blood clotting, antibody production for immunity, and manufacturing metabolic enzymes and hormones.</li>
            </ul>
        """,
        "lecture": "Have you noticed how fast you are growing taller this year? Where does the material to build longer leg bones, stronger arm muscles, and healthy skin come from? It comes from proteins! Proteins are the master architects of the human body. Every muscle fiber, hair strand, enzyme, and disease-fighting antibody is built from protein chains. When you consume a bowl of thick dal, paneer, boiled eggs, or roasted chana, your body disassembles these proteins into amino acids and reassembles them into your own growing muscles and tissues.",
        "checkpoints": [
            {
                "id": "6-1",
                "question": "Why are protein-rich foods commonly called 'body-building foods'?",
                "options": [
                    "Because they make bones transparent",
                    "Because they provide structural blocks needed for tissue growth, muscle development, and cellular repair",
                    "Because they only contain water",
                    "Because they make people fall asleep"
                ],
                "correct": 1,
                "explanation": "Proteins supply amino acids necessary for synthesis of muscle fibers, enzymes, antibodies, and cellular repair."
            },
            {
                "id": "6-2",
                "question": "Which of the following plant foods is celebrated as the richest source of vegetarian protein?",
                "options": ["Soyabean", "Cucumber", "White rice", "Green apple"],
                "correct": 0,
                "explanation": "Soyabeans contain approximately 36–40% protein by weight, making them the richest plant protein source."
            }
        ]
    },
    {
        "id": 7,
        "badge": "3.2 • Protective Shield",
        "title": "Vitamins A, B, C & D",
        "subtitle": "Micro-Nutrient Defense: Eyesight, Nerves, Immunity, and Bone Strength",
        "theory": """
            <p>Unlike carbohydrates and proteins which are consumed in large quantities, <strong>Vitamins</strong> are required in tiny amounts. However, they are utterly vital for protecting our body against diseases, maintaining sharp vision, healthy gums, radiant skin, and strong bones:</p>
            <ul class="list-disc pl-5 mt-2 space-y-2 text-slate-300 text-xs sm:text-sm">
                <li><strong>Vitamin A:</strong> Keeps eyesight sharp (especially night vision) and maintains healthy skin and mucosal linings. <em>Sources:</em> Carrots, ripe papaya, mango, pumpkin, milk, and fish oil.</li>
                <li><strong>Vitamin B₁ (Thiamine):</strong> Essential for cellular respiration, nerve conduction, and heart function. <em>Sources:</em> Whole unpolished grains, pulses, nuts, and yeast.</li>
                <li><strong>Vitamin C (Ascorbic Acid):</strong> Powerful antioxidant that fights infections, keeps gums healthy, and speeds up wound healing. Highly sensitive to heat and destroyed by over-boiling! <em>Sources:</em> Indian gooseberry (Amla—richest source!), guava, lemons, oranges, and green chilies.</li>
                <li><strong>Vitamin D:</strong> Enables intestines to absorb calcium from food to build rock-hard bones and teeth. Synthesized naturally by skin exposure to morning sunlight! <em>Sources:</em> Morning sunshine, milk, eggs, and fish.</li>
            </ul>
        """,
        "lecture": "Vitamins are the body's protective guardians! Even though we only need a few milligrams of vitamins each day, their absence can cause devastating disorders. For instance, Vitamin A keeps your eyes sharp in twilight; Vitamin C, found in abundance in our humble Indian Amla, keeps your gums firm and arms your white blood cells against infections. And look at Vitamin D: nature has designed our skin to manufacture Vitamin D for free whenever morning sunlight touches us! Eating fresh seasonal fruits and spending time playing in the morning sun gives you an invincible protective shield.",
        "checkpoints": [
            {
                "id": "7-1",
                "question": "Which indigenous Indian fruit is recognized as the richest natural source of Vitamin C?",
                "options": ["Amla (Indian Gooseberry)", "Sweet banana", "Dry coconut", "Cooked potato"],
                "correct": 0,
                "explanation": "Amla contains twenty times more Vitamin C per weight than orange juice, making it nature's immunity powerhouse."
            },
            {
                "id": "7-2",
                "question": "How can the human body synthesize Vitamin D naturally without relying entirely on food?",
                "options": [
                    "By drinking cold sodas",
                    "Through direct exposure of skin to gentle morning sunlight",
                    "By sleeping in dark rooms during daytime",
                    "By reading textbooks under fluorescent lamps"
                ],
                "correct": 1,
                "explanation": "Skin cells synthesize Vitamin D when exposed to ultraviolet-B wavelengths in morning sunlight."
            }
        ]
    },
    {
        "id": 8,
        "badge": "3.2 • Mineral Shield",
        "title": "Essential Minerals",
        "subtitle": "Calcium, Iodine, and Iron: Foundations for Bones, Thyroid, and Blood",
        "theory": """
            <p><strong>Minerals</strong> are inorganic elements absorbed by plants from the soil and passed on to us through food. Just like vitamins, minerals are protective nutrients required in small amounts for critical physiological functions:</p>
            <ul class="list-disc pl-5 mt-2 space-y-2 text-slate-300 text-xs sm:text-sm">
                <li><strong>Calcium:</strong> The primary mineral component of our skeletal framework. Essential for building strong bones, healthy teeth, muscular contraction, and normal blood clotting. <em>Sources:</em> Milk, curd, paneer, ragi (finger millet), sesame seeds (til), and green leafy vegetables.</li>
                <li><strong>Iodine:</strong> Required by the thyroid gland located in the neck to synthesize thyroxine hormone, which regulates physical growth, body metabolism, and brain development. <em>Sources:</em> Iodised table salt, seafood, fish, and crops grown in iodine-rich coastal soils.</li>
                <li><strong>Iron:</strong> Essential for manufacturing <em>hemoglobin</em>, the red pigment inside red blood cells that transports oxygen from lungs to every living cell. Deficiency causes extreme fatigue known as anemia. <em>Sources:</em> Jaggery (gur), spinach (palak), green leafy vegetables, amla, dates, pomegranates, and legumes.</li>
            </ul>
        """,
        "lecture": "Let us explore three champion minerals that keep your body working smoothly. First is Calcium: your bones and teeth are living storehouses of calcium. Drinking a glass of milk or eating ragi porridge keeps them sturdy and fracture-proof. Second is Iodine: without a tiny pinch of iodine in our daily salt, the thyroid gland in our neck swells up into a condition called goitre, and children's mental development slows down. Third is Iron: ever wonder why blood is red? Because of iron! Iron builds hemoglobin, the microscopic oxygen delivery trucks in our blood. Eating jaggery, spinach, and dates ensures your cells never run out of oxygen.",
        "checkpoints": [
            {
                "id": "8-1",
                "question": "Which mineral is crucial for synthesizing hemoglobin to transport oxygen in the bloodstream?",
                "options": ["Iron", "Copper", "Gold", "Lead"],
                "correct": 0,
                "explanation": "Iron is the central chemical atom in hemoglobin, responsible for binding and carrying oxygen across tissues."
            },
            {
                "id": "8-2",
                "question": "Why is table salt universally fortified with the mineral Iodine across India?",
                "options": [
                    "To make salt look whiter",
                    "To ensure healthy thyroid hormone synthesis and prevent goitre and developmental delays",
                    "To make food taste sweeter",
                    "To make salt heavier for packaging"
                ],
                "correct": 1,
                "explanation": "Iodised salt provides the essential trace mineral needed to prevent goitre (thyroid swelling) and mental impairment."
            }
        ]
    },
    {
        "id": 9,
        "badge": "3.2 • Motility & Hydration",
        "title": "Fiber & Water",
        "subtitle": "Roughage for Bowel Health and Water for Universal Solvation",
        "theory": """
            <p>A healthy diet requires more than just nutrients. Two non-nutrient components are absolutely indispensable for life and digestive well-being:</p>
            <ul class="list-disc pl-5 mt-2 space-y-2 text-slate-300 text-xs sm:text-sm">
                <li><strong>Dietary Fibres (Roughage):</strong> Complex indigestible plant carbohydrates (mainly cellulose) that pass through the digestive tract without being absorbed. Roughage adds bulk to food, retains moisture, stimulates rhythmic muscular contractions (peristalsis) of the intestines, and ensures smooth bowel clearance, preventing painful constipation. <em>Sources:</em> Whole grains (unpolished rice, whole wheat flour with bran, millets), pulses with skin, fresh fruits with skin (apples, guavas), and leafy greens.</li>
                <li><strong>Water:</strong> Makes up about 60–70% of human body weight! Water acts as a universal biological solvent that dissolves and transports absorbed nutrients into cells, regulates body temperature via sweating and evaporation, and flushes toxic metabolic wastes out of the body through urine and perspiration.</li>
            </ul>
        """,
        "lecture": "Did you know that not everything we eat is meant to be digested? Dietary fiber, also called roughage, cannot be broken down by human enzymes. Yet, it is vital! Think of roughage as a broom that sweeps through your digestive tract, adding soft bulk to food waste and keeping your intestines clean and moving smoothly. Without fiber, waste stagnates and causes constipation. And what about water? Water is the liquid river of life inside you! Every chemical reaction in your cells takes place in water. Drinking 8 to 10 glasses of clean water daily keeps your kidneys flushing toxins and your body temperature perfectly balanced.",
        "checkpoints": [
            {
                "id": "9-1",
                "question": "What is the primary physiological benefit of dietary roughage (plant fiber) in daily meals?",
                "options": [
                    "It builds large muscles instantly",
                    "It adds bulk to stools, promotes healthy peristalsis, and prevents constipation",
                    "It turns bones into steel",
                    "It eliminates the need to drink water"
                ],
                "correct": 1,
                "explanation": "Roughage adds indigestible bulk, facilitating smooth intestinal motility and preventing waste stagnation."
            },
            {
                "id": "9-2",
                "question": "Which of the following functions is performed by water in the human body?",
                "options": [
                    "Dissolving nutrients and flushing metabolic wastes through urine and perspiration",
                    "Building solid tooth enamel directly",
                    "Synthesizing iron atoms",
                    "Replacing all dietary vitamins"
                ],
                "correct": 0,
                "explanation": "Water acts as a universal solvent, facilitates nutrient transport, and carries metabolic wastes out of the body."
            }
        ]
    },
    {
        "id": 10,
        "badge": "3.3.1 • Food Lab 1",
        "title": "Starch Iodine Test",
        "subtitle": "Chemical Detection: Formation of the Characteristic Blue-Black Complex",
        "theory": """
            <p>Scientists and students can readily detect the presence of complex carbohydrates (starch) in food samples using a simple chemical color reaction.</p>
            <div class="p-3.5 rounded-xl bg-slate-900/90 border border-slate-800 space-y-2 mt-2">
                <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block">Laboratory Procedure:</span>
                <ol class="list-decimal pl-5 space-y-1 text-slate-300 text-xs sm:text-sm">
                    <li>Take a small slice of a raw potato or a teaspoon of boiled rice/flour paste on a clean porcelain tile or watch glass.</li>
                    <li>Using a dropper, carefully place <strong>2 to 3 drops of dilute Iodine solution</strong> (light yellowish-brown liquid) directly onto the food sample.</li>
                    <li>Observe the immediate surface color change.</li>
                </ol>
            </div>
            <p class="mt-3 text-xs sm:text-sm text-slate-200">
                <strong>Scientific Observation & Conclusion:</strong> If the yellowish-brown iodine turns an intense <strong>blue-black color</strong>, it confirms the presence of <strong>starch</strong> in the food sample. (Negative samples like butter, egg white, or cucumber show no blue-black shift).
            </p>
        """,
        "lecture": "Step into our virtual school laboratory! Today, we are testing for starch. Take a fresh slice of raw potato or a small spoonful of boiled rice. Using a glass dropper, gently place two drops of dilute iodine solution onto the potato. Watch closely: the light yellowish-brown liquid instantly reacts with helical starch molecules, transforming into an unmistakable, deep blue-black color! This dramatic color shift is proof positive that the food contains starch. If you try the same test on a piece of cheese or an egg white, the color stays brown—confirming they contain no starch.",
        "checkpoints": [
            {
                "id": "10-1",
                "question": "Which chemical reagent is used in school laboratories to test for the presence of starch in food?",
                "options": ["Dilute Iodine solution", "Caustic soda", "Copper sulfate", "Hydrochloric acid"],
                "correct": 0,
                "explanation": "Dilute iodine solution reacts specifically with starch molecules to produce a characteristic blue-black complex."
            },
            {
                "id": "10-2",
                "question": "What dramatic color change confirms a positive test result for starch?",
                "options": [
                    "Bright pink color",
                    "Intense blue-black color",
                    "Translucent yellow color",
                    "Bubbling white foam"
                ],
                "correct": 1,
                "explanation": "A blue-black color change conclusively confirms the presence of starch in the tested food sample."
            }
        ]
    },
    {
        "id": 11,
        "badge": "3.3.2 • Food Lab 2",
        "title": "Fat Translucent Test",
        "subtitle": "Physical Spotting: The Greasy Translucent Patch on Paper",
        "theory": """
            <p>Testing for fats does not require complex reagents; it relies on the physical properties of lipids and their refractive behavior on paper fibers.</p>
            <div class="p-3.5 rounded-xl bg-slate-900/90 border border-slate-800 space-y-2 mt-2">
                <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block">Laboratory Procedure:</span>
                <ol class="list-decimal pl-5 space-y-1 text-slate-300 text-xs sm:text-sm">
                    <li>Take a small food sample (e.g., a crushed groundnut seed, a drop of oil, or a small smear of butter).</li>
                    <li>Wrap the sample inside a clean piece of white paper and press or rub it gently without tearing the paper.</li>
                    <li>Unfold the paper and remove the food crumbs.</li>
                    <li>If the paper is damp from water, let it dry in sunlight or air for a few minutes.</li>
                    <li>Hold the paper up against a light source (window or bulb).</li>
                </ol>
            </div>
            <p class="mt-3 text-xs sm:text-sm text-slate-200">
                <strong>Scientific Observation & Conclusion:</strong> If a persistent, oily <strong>translucent patch</strong> remains on the paper (allowing partial light to pass through), it conclusively confirms the presence of <strong>fat</strong> in the food!
            </p>
        """,
        "lecture": "Have you ever brought fried samosas or groundnuts wrapped in a paper bag and noticed that the paper became see-through in patches? That everyday observation is a genuine scientific test for fats! When you crush a peanut or smear butter on white paper, the oil molecules penetrate between cellulose fibers of the paper. Water dries up and evaporates completely, but fats do not evaporate. When you hold the dried paper against a light bulb, light scatters through the oily spot, creating a translucent patch. That permanent greasy spot tells you: fat is present!",
        "checkpoints": [
            {
                "id": "11-1",
                "question": "How can you distinguish whether a wet spot on paper is caused by water or dietary fat?",
                "options": [
                    "By freezing it",
                    "By letting the paper dry in air: water evaporates completely leaving dry paper, whereas fats leave a persistent translucent oily patch",
                    "By smelling it from 10 meters away",
                    "By setting it on fire"
                ],
                "correct": 1,
                "explanation": "Water dries and leaves paper opaque, while non-volatile lipids leave a permanent translucent greasy spot."
            },
            {
                "id": "11-2",
                "question": "Which of these food samples will produce an oily translucent patch when pressed on paper?",
                "options": ["Crushed groundnuts or butter", "Dry wheat flour", "Boiled potato", "Raw carrot slice"],
                "correct": 0,
                "explanation": "Groundnuts and butter are rich in lipids/oils that soak into paper fibers, creating a translucent spot."
            }
        ]
    },
    {
        "id": 12,
        "badge": "3.3.3 • Food Lab 3",
        "title": "Protein Biuret Test",
        "subtitle": "Biochemical Reaction: Copper Sulfate and Caustic Soda Yielding Violet",
        "theory": """
            <p>Proteins contain specialized chemical peptide bonds that react with copper ions in an alkaline medium to produce a distinct purple or violet hue (the Biuret reaction).</p>
            <div class="p-3.5 rounded-xl bg-slate-900/90 border border-slate-800 space-y-2 mt-2">
                <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block">Laboratory Procedure:</span>
                <ol class="list-decimal pl-5 space-y-1 text-slate-300 text-xs sm:text-sm">
                    <li>Grind or mash a small quantity of food sample (e.g., boiled dal paste, crushed soaked soyabean, or diluted milk).</li>
                    <li>Place the paste into a clean test tube and add about 10 drops of water. Shake well to form a suspension.</li>
                    <li>Add <strong>2 drops of Copper Sulfate solution</strong> (blue chemical liquid).</li>
                    <li>Add <strong>10 drops of Caustic Soda (Sodium Hydroxide) solution</strong>.</li>
                    <li>Shake the test tube gently and allow it to stand undisturbed for 5 minutes.</li>
                </ol>
            </div>
            <p class="mt-3 text-xs sm:text-sm text-slate-200">
                <strong>Scientific Observation & Conclusion:</strong> The appearance of a rich <strong>violet or purple color</strong> confirms the presence of <strong>proteins</strong> in the food sample.
            </p>
        """,
        "lecture": "Now let us conduct a sophisticated biochemical test! To test for protein, take mashed soaked soyabeans or boiled dal in a clean glass test tube with a little water. First, add two drops of bright blue copper sulfate solution. Next, add ten drops of caustic soda solution, which creates an alkaline environment. Shake the test tube gently and watch the magic of chemistry unfold: the blue liquid reacts with protein peptide bonds, turning into a gorgeous royal violet or purple color! That vivid purple hue is direct scientific evidence that your food contains proteins.",
        "checkpoints": [
            {
                "id": "12-1",
                "question": "Which two chemical solutions are required to conduct the protein test in a school laboratory?",
                "options": [
                    "Iodine and alcohol",
                    "Copper sulfate solution and Caustic soda (Sodium hydroxide) solution",
                    "Lemon juice and vinegar",
                    "Salt water and sugar syrup"
                ],
                "correct": 1,
                "explanation": "Copper sulfate provides copper ions while caustic soda creates the alkaline medium needed for the violet protein complex."
            },
            {
                "id": "12-2",
                "question": "What color change indicates a positive result for the presence of protein?",
                "options": ["A violet or purple color", "A deep blue-black color", "A bright green color", "A clear colorless liquid"],
                "correct": 0,
                "explanation": "A violet or purple coloration confirms the presence of proteins through peptide bond complexation."
            }
        ]
    },
    {
        "id": 13,
        "badge": "3.4 • Balanced Nutrition",
        "title": "The Balanced Thali",
        "subtitle": "Optimal Proportions, Demographic Factors, and Fortified Foods",
        "theory": """
            <p>No single food item contains all the nutrients our body requires. To maintain robust health, our daily meals must provide a harmonious combination of all dietary elements. A <strong>Balanced Diet</strong> is defined as a diet that contains all essential nutrients (carbohydrates, fats, proteins, vitamins, and minerals), adequate roughage, and water in the <strong>correct proportions</strong> for proper growth and health.</p>
            <ul class="list-disc pl-5 mt-2 space-y-1.5 text-slate-300 text-xs sm:text-sm">
                <li><strong>Individualized Needs:</strong> Nutritional requirements vary based on <em>age</em> (growing children need more protein), <em>gender</em>, <em>physical activity</em> (laborers need more carbohydrates and fats), and <em>health status</em>.</li>
                <li><strong>Junk Food Hazard:</strong> Highly processed foods (potato chips, sodas, burgers) provide 'empty calories'—high in refined sugars, unhealthy fats, and sodium, but devoid of fiber, proteins, and vitamins, leading to childhood obesity and lethargy.</li>
                <li><strong>Fortified Foods (+F Logo):</strong> Staple foods enriched with essential micronutrients under <em>FSSAI</em> regulations (e.g., Iodised salt, Vitamin A & D fortified milk/oil) to eliminate widespread public deficiencies.</li>
            </ul>
        """,
        "lecture": "Look at a traditional Indian thali: in the center, you have a bowl of rice or whole-wheat rotis for carbohydrates; a bowl of thick dal or paneer for protein; a colorful vegetable sabzi with carrots and spinach for vitamins and minerals; a cup of curd or buttermilk with healthy fats and probiotics; and a crunchy cucumber salad for roughage. That thali is a masterclass in balanced nutrition! When you replace this wholesome meal with potato chips and carbonated sodas, you are consuming empty calories—lots of sugar and processed fat with zero vitamins or fiber. True mindful eating means filling your plate with colors and balance.",
        "checkpoints": [
            {
                "id": "13-1",
                "question": "What is the defining feature of a 'Balanced Diet'?",
                "options": [
                    "Eating only desserts all day",
                    "A diet containing all essential nutrients, roughage, and water in proper proportions for optimal health and growth",
                    "Eating only meat without any fruits or vegetables",
                    "A diet consisting solely of boiled rice"
                ],
                "correct": 1,
                "explanation": "A balanced diet provides carbohydrates, fats, proteins, vitamins, minerals, roughage, and water in correct proportions."
            },
            {
                "id": "13-2",
                "question": "What does the '+F' logo on packaged milk, edible oil, and salt indicate in India?",
                "options": [
                    "The food is fried",
                    "The food is fortified with essential vitamins or minerals under FSSAI standards",
                    "The food is imported from foreign countries",
                    "The food is expired"
                ],
                "correct": 1,
                "explanation": "The +F blue logo signifies that the food is fortified with essential micronutrients like Vitamin A, D, Iron, or Iodine."
            }
        ]
    },
    {
        "id": 14,
        "badge": "3.5 • Super Grains",
        "title": "Millets: Super Grains",
        "subtitle": "Nutri-Cereals: Climate Resilience, Low Water Footprint, and Micronutrient Density",
        "theory": """
            <p>For thousands of years, indigenous small-seeded grasses known as <strong>Millets</strong> (or <em>Shree Anna</em> / Nutri-cereals) formed the backbone of India's traditional agricultural diet. Recently rediscovered globally, millets are nutritional powerhouses and climate heroes:</p>
            <ul class="list-disc pl-5 mt-2 space-y-2 text-slate-300 text-xs sm:text-sm">
                <li><strong>Major Native Millets:</strong>
                    <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
                        <li><em>Ragi (Finger Millet):</em> Outstanding source of natural Calcium (strengthens bones) and dietary fiber.</li>
                        <li><em>Bajra (Pearl Millet):</em> Rich in Iron (combats anemia), phosphorus, and energy.</li>
                        <li><em>Jowar (Sorghum):</em> High in antioxidants, protein, and gluten-free complex carbs.</li>
                        <li><em>Sanwa (Barnyard Millet):</em> Low glycemic index and rich in micronutrients.</li>
                    </ul>
                </li>
                <li><strong>Agricultural & Ecological Benefits:</strong> Millets thrive in poor, arid soils with minimal rainfall, withstand severe droughts, require far less chemical fertilizer than polished rice or wheat, and resist pest attacks naturally.</li>
            </ul>
        """,
        "lecture": "Let us celebrate India's ancient super grains: Millets! Long before polished white rice and refined flour dominated our plates, our ancestors thrived on Jowar, Bajra, and Ragi. Why are millets called 'Nutri-cereals'? Because they are packed with dietary fiber, iron, calcium, and complex vitamins! Furthermore, millets are true climate warriors: while one kilogram of polished rice can require up to 4,000 liters of water to cultivate, hardy millets grow in dry, rain-fed soils with minimal water and zero pesticides. Including millets in our daily rotis and khichdi protects both our personal health and the planet's water resources.",
        "checkpoints": [
            {
                "id": "14-1",
                "question": "Which native Indian millet is celebrated for having extraordinarily high natural Calcium content?",
                "options": ["Ragi (Finger Millet)", "White polished rice", "Refined maida", "Sweet corn"],
                "correct": 0,
                "explanation": "Ragi contains around 344 mg of calcium per 100 g—over thirty times higher than polished white rice."
            },
            {
                "id": "14-2",
                "question": "Why are millets considered environmentally friendly and climate-resilient crops?",
                "options": [
                    "They require vast amounts of plastic",
                    "They thrive in poor soils with very little water and resist extreme drought conditions naturally",
                    "They can only grow in air-conditioned greenhouses",
                    "They do not need soil to grow"
                ],
                "correct": 1,
                "explanation": "Millets have minimal water requirements, withstand heat and drought, and grow well without synthetic fertilizers."
            }
        ]
    },
    {
        "id": 15,
        "badge": "3.6 • Ecology & Plate",
        "title": "Food Miles & Ecology",
        "subtitle": "Farm-to-Fork Distance: Carbon Footprints and the Value of Local Produce",
        "theory": """
            <p>Have you ever wondered how far an apple, avocado, or exotic packaged snack traveled before reaching your dining table? The concept of <strong>Food Miles</strong> measures the total geographical distance food is transported from the agricultural farm where it is harvested to the plate of the final consumer.</p>
            <p class="mt-2">Long food miles carry hidden ecological and nutritional costs:</p>
            <ul class="list-disc pl-5 mt-2 space-y-1.5 text-slate-300 text-xs sm:text-sm">
                <li><strong>Carbon Pollution:</strong> Transporting foods thousands of kilometers by diesel trucks, cargo ships, and airplanes burns fossil fuels, releasing massive greenhouse gases.</li>
                <li><strong>Loss of Freshness:</strong> Foods traveling for weeks are picked prematurely, treated with synthetic chemical waxes, artificial preservatives, and refrigeration, degrading delicate vitamins like Vitamin C.</li>
                <li><strong>Benefits of Low Food Miles:</strong> Consuming locally grown, seasonal fruits and vegetables supports local farming communities, cuts packaging waste, guarantees superior freshness, and reduces transport carbon emissions.</li>
            </ul>
        """,
        "lecture": "Next time you bite into a piece of fruit, ask yourself: How many food miles did this travel? If you buy an apple imported from thousands of miles across the ocean, imagine the diesel burned by cargo planes, refrigeration ships, and highway trucks to deliver that single apple! Along that long journey, the fruit was coated in wax and lost much of its delicate vitamin content. By contrast, when you buy fresh guavas, papayas, or spinach grown by a local farmer in your district, the food miles are near zero. It arrives at your plate fresh, nutrient-dense, and without a heavy carbon footprint.",
        "checkpoints": [
            {
                "id": "15-1",
                "question": "What is meant by the scientific term 'Food Miles'?",
                "options": [
                    "The number of calories in a mile of walking",
                    "The total distance food travels from its place of harvest to the consumer's plate",
                    "The speed at which food is cooked",
                    "The size of a farmer's tractor"
                ],
                "correct": 1,
                "explanation": "Food miles represent the transport distance from farm to fork, reflecting energy expenditure and transport pollution."
            },
            {
                "id": "15-2",
                "question": "What is a major environmental benefit of choosing locally grown seasonal produce?",
                "options": [
                    "It drastically reduces transport fuel consumption and carbon greenhouse gas emissions",
                    "It makes transport trucks drive faster",
                    "It makes vegetables taste like candy",
                    "It requires imported plastic packaging"
                ],
                "correct": 0,
                "explanation": "Buying local cuts long-distance shipping, lowering fossil fuel combustion, transport emissions, and packaging waste."
            }
        ]
    },
    {
        "id": 16,
        "badge": "3.6 • Pioneers",
        "title": "Nutrition Pioneers",
        "subtitle": "Historic Discoveries: James Lind, Himalayan Goitre, and Dr. C. Gopalan",
        "theory": """
            <p>Modern nutrition science stands on the shoulders of dedicated researchers and communities who solved life-threatening dietary mysteries:</p>
            <ul class="list-disc pl-5 mt-2 space-y-2 text-slate-300 text-xs sm:text-sm">
                <li><strong>James Lind (1746):</strong> Scottish naval physician who conducted one of history's first controlled clinical trials aboard <em>HMS Salisbury</em>. He proved that sailors dying of scurvy (bleeding gums and fatigue) recovered rapidly when given fresh citrus fruits (oranges and lemons rich in Vitamin C), revolutionizing maritime health.</li>
                <li><strong>Himalayan Goitre & The Agariya Community:</strong> In the sub-Himalayan belt, soil was severely depleted of iodine by glacial runoff, causing rampant neck swelling (goitre). India launched the Universal Salt Iodisation Program, partnering with traditional salt farmers like the <em>Agariya community</em> of Kutch to ensure iodised salt reached every Indian household, eradicating endemic goitre.</li>
                <li><strong>Dr. Coluthur Gopalan (1918–2019):</strong> Renowned as the 'Father of Indian Nutrition Research'. As Director of the National Institute of Nutrition (NIN), he analyzed the precise nutrient composition of over 500 indigenous Indian foods. His landmark research laid the scientific foundation for India's national nutritional guidelines and inspired the Mid-Day Meal Scheme (PM POSHAN) feeding over 100 million schoolchildren daily!</li>
            </ul>
        """,
        "lecture": "Let us honor the pioneering heroes of nutritional science! In 1746, Dr. James Lind saved thousands of sailors from scurvy by proving that citrus fruits cure the disease, leading to the discovery of Vitamin C. In India, our scientists tackled the devastating Himalayan goitre belt by ensuring table salt was enriched with trace iodine, collaborating with the resilient Agariya salt-farming families in the Little Rann of Kutch. And above all stands Dr. Coluthur Gopalan, the father of Indian nutrition research! Dr. Gopalan analyzed the proteins, vitamins, and minerals of over 500 Indian foods, proving that traditional dals, millets, and greens are nutritional treasures, and laying the groundwork for the school Mid-Day Meal program.",
        "checkpoints": [
            {
                "id": "16-1",
                "question": "What historic medical discovery was made by Dr. James Lind in 1746?",
                "options": [
                    "He proved that citrus fruits containing Vitamin C cure and prevent scurvy in sailors",
                    "He invented modern microscopes",
                    "He discovered penicillin antibiotic",
                    "He proved that bread contains no energy"
                ],
                "correct": 0,
                "explanation": "Dr. Lind's clinical trial demonstrated that fresh citrus fruits cured scurvy, linking diet directly to disease prevention."
            },
            {
                "id": "16-2",
                "question": "How did Dr. Coluthur Gopalan transform public health and child nutrition across India?",
                "options": [
                    "He created artificial sugar syrups",
                    "He analyzed the nutrient profile of 500+ Indian foods and laid the scientific basis for the school Mid-Day Meal program",
                    "He built diesel cargo ships",
                    "He advocated for eating fast food daily"
                ],
                "correct": 1,
                "explanation": "Dr. Gopalan's pioneering nutritional surveys formed the bedrock of India's national dietary policies and school meal schemes."
            }
        ]
    }
]

# Quiz Questions for Slides 17 to 20
QUIZ_QUESTIONS = [
    # Quiz 1: Slide 17 (Q1 to Q10: Significance of Food, Regional Diets, Carbs & Fats)
    {
        "id": 1,
        "question": "What core message is conveyed by the ancient Sanskrit verse 'Annena jātāni jīvanti'?",
        "options": [
            "Living beings can survive without food",
            "Food gives life and sustains all living organisms",
            "Food should only be eaten during festivals",
            "Only cooked food has nutrients"
        ],
        "correct": 1,
        "solution": "The Taittiriya Upanishada verse establishes that food is the fundamental biological sustenance of all living creatures."
    },
    {
        "id": 2,
        "question": "Which of the following describes wholesome eating according to traditional Subhashita verses?",
        "options": [
            "Eating large quantities of fried food",
            "Consuming wholesome, moderate, and seasonal food suited to bodily needs",
            "Eating food late at night without drinking water",
            "Eating only sugary candies"
        ],
        "correct": 1,
        "solution": "Subhashita teaches that wholesome, moderate, and seasonal food maintains biological equilibrium and health."
    },
    {
        "id": 3,
        "question": "Why is Makki di roti with Sarson da saag a popular traditional staple in Punjab?",
        "options": [
            "Because wheat and rice do not grow in north India",
            "Because maize and mustard crops grow abundantly in Punjab's fertile winter agricultural cycle",
            "Because mustard seeds are imported from overseas",
            "Because it has zero nutritional value"
        ],
        "correct": 1,
        "solution": "Regional culinary traditions directly reflect native seasonal crop harvests—maize and mustard in Punjab."
    },
    {
        "id": 4,
        "question": "Which regional dish made from finger millet (Ragi) is a traditional staple in Karnataka?",
        "options": ["Ragi mudde", "Eromba", "Makki di roti", "Pav bhaji"],
        "correct": 0,
        "solution": "Ragi mudde (finger millet dumplings) is Karnataka's celebrated nutrient-dense, fiber-rich staple."
    },
    {
        "id": 5,
        "question": "What is the primary biological role of Carbohydrates in the human diet?",
        "options": [
            "To serve as the body's primary and most readily available source of daily energy",
            "To build tooth enamel directly",
            "To fight bacterial infections like antibodies",
            "To replace water in cells"
        ],
        "correct": 0,
        "solution": "Carbohydrates break down into glucose, providing immediate and daily cellular metabolic fuel."
    },
    {
        "id": 6,
        "question": "Which of the following food items is rich in complex starchy carbohydrates?",
        "options": ["Potatoes and rice", "Butter and ghee", "Egg white", "Common table salt"],
        "correct": 0,
        "solution": "Potatoes, rice, and whole grains are loaded with complex starchy carbohydrates."
    },
    {
        "id": 7,
        "question": "Why are carbohydrates and fats collectively classified as 'energy-giving foods'?",
        "options": [
            "Because they make bones soft",
            "Because they are the two primary nutritional classes oxidized to release caloric energy",
            "Because they contain no carbon atoms",
            "Because they are only found in fruits"
        ],
        "correct": 1,
        "solution": "Both carbohydrates and fats release energy upon cellular oxidation, powering all bodily activities."
    },
    {
        "id": 8,
        "question": "How does the energy yield of 1 gram of fat compare to 1 gram of carbohydrate?",
        "options": [
            "Fat yields over twice as much energy (9 kcal vs 4 kcal)",
            "Fat yields zero energy",
            "Carbohydrate yields ten times more energy",
            "Both yield exactly 1 kcal"
        ],
        "correct": 0,
        "solution": "Fats are chemically concentrated lipids yielding approximately 9 kcal per gram, compared to 4 kcal per gram of carbohydrate."
    },
    {
        "id": 9,
        "question": "Which of the following is a plant-based source of healthy dietary fats?",
        "options": ["Groundnuts and mustard oil", "Cow's milk butter", "Boiled chicken", "Egg yolk"],
        "correct": 0,
        "solution": "Groundnuts, seeds, and vegetable oils are excellent plant-derived sources of essential fatty acids."
    },
    {
        "id": 10,
        "question": "What role does the subcutaneous fat layer beneath human skin play?",
        "options": [
            "It turns food into bone",
            "It acts as thermal insulation to prevent excessive loss of body heat in cold environments",
            "It prevents skin from breathing",
            "It stores iron atoms"
        ],
        "correct": 1,
        "solution": "Subcutaneous adipose tissue insulates the body against thermal loss and cushions internal organs."
    },

    # Quiz 2: Slide 18 (Q11 to Q20: Proteins, Vitamins, Minerals, Fiber & Water)
    {
        "id": 11,
        "question": "Why are protein-rich foods designated as 'body-building foods'?",
        "options": [
            "Because they supply amino acids needed for muscle synthesis, cellular growth, and tissue repair",
            "Because they are completely transparent",
            "Because they dissolve body fat instantly",
            "Because they prevent sleep"
        ],
        "correct": 0,
        "solution": "Proteins supply amino acids, the fundamental building blocks for tissue synthesis, enzymes, and repair."
    },
    {
        "id": 12,
        "question": "Which vegetarian plant food contains the highest percentage of natural protein by weight?",
        "options": ["Soyabean", "Cucumber", "White rice", "Potato"],
        "correct": 0,
        "solution": "Soyabeans contain about 36–40% protein by dry weight, making them the richest plant protein source."
    },
    {
        "id": 13,
        "question": "Which vitamin is essential for maintaining sharp vision, particularly in dim light and at night?",
        "options": ["Vitamin A", "Vitamin C", "Vitamin D", "Vitamin K"],
        "correct": 0,
        "solution": "Vitamin A is essential for synthesizing rhodopsin, the visual photopigment in retina rod cells."
    },
    {
        "id": 14,
        "question": "Why should green vegetables and citrus fruits rich in Vitamin C NOT be overcooked or boiled for prolonged periods?",
        "options": [
            "Because Vitamin C is heat-labile and easily destroyed by excessive cooking heat",
            "Because it makes the food taste like salt",
            "Because it freezes the water in food",
            "Because Vitamin C turns into stone"
        ],
        "correct": 0,
        "solution": "Vitamin C (ascorbic acid) is water-soluble and chemically decomposes rapidly at high cooking temperatures."
    },
    {
        "id": 15,
        "question": "What unique natural process allows the human body to manufacture Vitamin D without ingesting food?",
        "options": [
            "Drinking warm water in winter",
            "Direct synthesis in skin cells triggered by morning sunlight exposure",
            "Sleeping under fluorescent room lights",
            "Exercising in total darkness"
        ],
        "correct": 1,
        "solution": "Ultraviolet-B photons in sunlight convert 7-dehydrocholesterol in human skin into Vitamin D3."
    },
    {
        "id": 16,
        "question": "Which mineral is the primary structural building block of bones and teeth?",
        "options": ["Calcium", "Sulfur", "Iron", "Potassium"],
        "correct": 0,
        "solution": "Calcium, together with phosphorus, forms hard calcium hydroxyapatite crystals that strengthen bones and teeth."
    },
    {
        "id": 17,
        "question": "Deficiency of which trace mineral causes swelling of the thyroid gland in the neck, known as Goitre?",
        "options": ["Iodine", "Sodium", "Calcium", "Zinc"],
        "correct": 0,
        "solution": "Iodine is required to synthesize thyroid hormones; its absence leads to compensatory gland enlargement (goitre)."
    },
    {
        "id": 18,
        "question": "Why is the mineral Iron indispensable for the proper functioning of human red blood cells?",
        "options": [
            "It turns white cells into green cells",
            "It is the core chemical atom in hemoglobin that binds and delivers oxygen to cells",
            "It breaks down starch in saliva",
            "It prevents skin from sweating"
        ],
        "correct": 1,
        "solution": "Iron binds oxygen molecules in hemoglobin, allowing erythrocytes to distribute oxygen throughout the body."
    },
    {
        "id": 19,
        "question": "What vital role does dietary roughage (insoluble fiber) play in the human digestive system?",
        "options": [
            "It adds bulk to food waste, stimulates intestinal peristalsis, and prevents constipation",
            "It digests complex proteins into sugar",
            "It dissolves bones",
            "It replaces red blood cells"
        ],
        "correct": 0,
        "solution": "Dietary fiber absorbs water and adds bulk, ensuring smooth, regular transit of waste through the bowel."
    },
    {
        "id": 20,
        "question": "What percentage of the average human body weight consists of water?",
        "options": ["Approximately 60% to 70%", "Less than 10%", "Exactly 99%", "Zero percent"],
        "correct": 0,
        "solution": "Water constitutes roughly 60–70% of human body mass, serving as the universal cellular solvent."
    },

    # Quiz 3: Slide 19 (Q21 to Q30: Testing Labs, Balanced Diet & Millets)
    {
        "id": 21,
        "question": "When dilute Iodine solution is added to a food sample, what color confirms the presence of starch?",
        "options": ["Intense blue-black", "Bright yellow", "Pale pink", "Milky white"],
        "correct": 0,
        "solution": "The formation of a blue-black iodine-starch helical inclusion complex is the classic positive starch indicator."
    },
    {
        "id": 22,
        "question": "Why does a piece of boiled rice turn blue-black with iodine, while a piece of butter does not?",
        "options": [
            "Because rice is white in color",
            "Because rice contains complex starch molecules, while butter contains fats and zero starch",
            "Because butter is too cold",
            "Because iodine only reacts with liquids"
        ],
        "correct": 1,
        "solution": "Iodine reacts specifically with amylose starch polymers present in rice, which are absent in pure butter."
    },
    {
        "id": 23,
        "question": "In the paper test for fats, what persistent observation confirms a positive result after drying?",
        "options": [
            "The paper turns black and crumbles",
            "A permanent translucent oily patch that lets partial light pass through",
            "The paper dissolves completely into liquid",
            "A powder of white salt forms"
        ],
        "correct": 1,
        "solution": "Lipids do not evaporate like water; they remain trapped in paper fibers, creating a translucent greasy patch."
    },
    {
        "id": 24,
        "question": "Which two laboratory chemicals are used in sequence to test for proteins in a food suspension?",
        "options": [
            "Copper sulfate solution and Caustic soda (Sodium hydroxide) solution",
            "Iodine solution and water",
            "Vinegar and baking soda",
            "Alcohol and sulfuric acid"
        ],
        "correct": 0,
        "solution": "Copper sulfate provides cupric ions while caustic soda supplies alkalinity for the Biuret protein color reaction."
    },
    {
        "id": 25,
        "question": "What characteristic color change confirms the presence of protein in the Biuret test?",
        "options": ["A violet or purple color", "A deep blue-black color", "A bright orange color", "A milky white precipitate"],
        "correct": 0,
        "solution": "Cupric ions coordinate with peptide nitrogen atoms in alkaline conditions, yielding a distinct violet/purple hue."
    },
    {
        "id": 26,
        "question": "Which of the following meals best exemplifies a complete 'Balanced Diet'?",
        "options": [
            "A plate of potato chips and two cans of sugary soda",
            "A thali with whole-wheat roti/rice, dal, mixed vegetable sabzi, curd, and fresh salad",
            "Eating only boiled chicken with no vegetables or water",
            "A bowl of pure white sugar"
        ],
        "correct": 1,
        "solution": "A balanced thali combines carbohydrates, proteins, fats, vitamins, minerals, roughage, and hydration in proper balance."
    },
    {
        "id": 27,
        "question": "Why is regular consumption of fast food / junk food harmful to growing children?",
        "options": [
            "It provides empty calories—high in refined sugars and unhealthy fats, but lacking proteins, vitamins, and fiber",
            "It contains too many vitamins and minerals",
            "It turns blood into water",
            "It causes bones to grow too rapidly"
        ],
        "correct": 0,
        "solution": "Junk foods lack essential protective micronutrients and fiber while contributing to childhood obesity and metabolic illness."
    },
    {
        "id": 28,
        "question": "What does the blue '+F' logo on packaged Indian salt, milk, and edible oils signify?",
        "options": [
            "The food has been fortified with vital micronutrients (such as Vitamin A, D, Iron, or Iodine) under FSSAI standards",
            "The food is fast food",
            "The food is frozen",
            "The food is free of charge"
        ],
        "correct": 0,
        "solution": "The +F logo indicates scientifically regulated fortification with essential vitamins or minerals to prevent deficiencies."
    },
    {
        "id": 29,
        "question": "Which traditional Indian millet is exceptionally rich in natural Calcium, making it ideal for bone strength?",
        "options": ["Ragi (Finger Millet)", "Refined wheat flour (Maida)", "Polished white rice", "Sweet corn"],
        "correct": 0,
        "solution": "Ragi contains around 344 mg of calcium per 100 grams, far outclassing polished wheat or rice."
    },
    {
        "id": 30,
        "question": "Why are millets designated as climate-smart 'Nutri-cereals'?",
        "options": [
            "Because they can grow with very little water in drought-prone poor soils while providing high fiber, iron, and minerals",
            "Because they grow exclusively inside polar ice",
            "Because they require massive chemical fertilizer input",
            "Because they are manufactured in plastic factories"
        ],
        "correct": 0,
        "solution": "Millets possess high photosynthetic water-use efficiency, thriving in rain-fed arid soils with superior nutrient profiles."
    },

    # Quiz 4: Slide 20 (Q31 to Q40: Food Miles, Ecological Footprint & Pioneers)
    {
        "id": 31,
        "question": "What does the environmental metric 'Food Miles' measure?",
        "options": [
            "The number of miles a person runs after lunch",
            "The total distance food travels from agricultural production to the consumer's plate",
            "The height of a wheat crop",
            "The depth of plant roots"
        ],
        "correct": 1,
        "solution": "Food miles quantify the geographic transit distance of food, reflecting transport fuel use and carbon emissions."
    },
    {
        "id": 32,
        "question": "What is an ecological consequence of consuming foods with extremely high food miles?",
        "options": [
            "Higher transport emissions from trucks and planes, contributing to atmospheric carbon pollution",
            "Instant reduction of all global greenhouse gases",
            "Food becoming completely weightless",
            "Water turning into milk"
        ],
        "correct": 0,
        "solution": "Long-distance refrigerated transit burns heavy quantities of fossil fuels, elevating the meal's carbon footprint."
    },
    {
        "id": 33,
        "question": "Why does eating locally grown, seasonal fruits provide superior nutritional value?",
        "options": [
            "Because local fruits are harvested ripe and consumed fresh without prolonged transit degradation or artificial waxes",
            "Because local fruits are made of plastic",
            "Because local fruits do not contain water",
            "Because local fruits are always blue"
        ],
        "correct": 0,
        "solution": "Locally harvested produce avoids prolonged storage, retaining high concentrations of delicate vitamins like Vitamin C."
    },
    {
        "id": 34,
        "question": "What groundbreaking clinical discovery was made by Scottish naval physician Dr. James Lind in 1746?",
        "options": [
            "He proved that citrus fruits rich in Vitamin C rapidly cure and prevent scurvy among sailors",
            "He discovered how to manufacture artificial salt",
            "He invented the electric stove",
            "He proved that meat contains no protein"
        ],
        "correct": 0,
        "solution": "Dr. Lind's controlled trial aboard HMS Salisbury proved that lemons and oranges successfully reversed scurvy."
    },
    {
        "id": 35,
        "question": "Which deficiency disease historically plagued sailors on long voyages due to lack of fresh fruits and vegetables?",
        "options": ["Scurvy (bleeding gums and poor wound healing)", "Diabetes", "Asthma", "Malaria"],
        "correct": 0,
        "solution": "Scurvy is caused by acute Vitamin C deficiency, impairing collagen synthesis and causing gum bleeding and fatigue."
    },
    {
        "id": 36,
        "question": "Why was the sub-Himalayan belt in India historically prone to widespread endemic Goitre?",
        "options": [
            "Because glacial meltwaters repeatedly leached natural iodine out of the soil, producing iodine-deficient crops",
            "Because the mountains were too high for cooking",
            "Because people ate too many citrus fruits",
            "Because snow contains too much iron"
        ],
        "correct": 0,
        "solution": "Glacial erosion and heavy rains wash soil iodine into rivers, making Himalayan agricultural crops iodine-deficient."
    },
    {
        "id": 37,
        "question": "Which traditional salt-farming community in the Little Rann of Kutch plays an indispensable role in India's salt production?",
        "options": ["Agariya community", "Toda tribe", "Gaddi shepherds", "Warli painters"],
        "correct": 0,
        "solution": "The Agariya community produces inland salt from underground brine in the salt pans of the Little Rann of Kutch."
    },
    {
        "id": 38,
        "question": "Who is universally celebrated as the 'Father of Indian Nutrition Research'?",
        "options": ["Dr. Coluthur Gopalan", "Dr. Homi Bhabha", "Dr. Vikram Sarabhai", "Sir Isaac Newton"],
        "correct": 0,
        "solution": "Dr. Coluthur Gopalan spearheaded modern Indian nutrition science and transformed public health policies."
    },
    {
        "id": 39,
        "question": "What major national initiative was inspired by Dr. C. Gopalan's research at the National Institute of Nutrition (NIN)?",
        "options": [
            "The Mid-Day Meal Scheme (PM POSHAN) providing wholesome daily nutrition to school children",
            "The space satellite program",
            "The construction of railway tracks",
            "The deep sea mining project"
        ],
        "correct": 0,
        "solution": "Dr. Gopalan's documentation of child undernutrition provided the scientific imperative for school mid-day meal programs."
    },
    {
        "id": 40,
        "question": "What is the primary holistic goal of practicing 'Mindful Eating' in our daily lives?",
        "options": [
            "Eating while distracted by phone screens",
            "Appreciating food origins, choosing balanced wholesome local meals, and nourishing body health with gratitude",
            "Eating as fast as possible without chewing",
            "Consuming only processed packaged snacks"
        ],
        "correct": 1,
        "solution": "Mindful eating fosters awareness of nutritional balance, seasonal harmony, sustainable food miles, and long-term health."
    }
]

# Helper function to generate clean spoken text for slides 1 to 16
def strip_html(html_str):
    text = re.sub(r'<[^>]+>', ' ', html_str)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

for s in SLIDES:
    if s["id"] <= 16:
        theory_clean = strip_html(s["theory"])
        lecture_clean = strip_html(s["lecture"])
        spoken = f"Slide {s['id']}. {s['title']}. {s['subtitle']}. Core Concepts: {theory_clean} Classroom Lecture: {lecture_clean}"
        s["spoken_text"] = spoken

# Verify zero raw LaTeX
raw_latex_pattern = re.compile(r'\\[a-zA-Z]+')

for s in SLIDES:
    for k in ["title", "subtitle", "theory", "lecture", "spoken_text"]:
        if k in s:
            matches = raw_latex_pattern.findall(s[k])
            if matches:
                raise ValueError(f"Found raw LaTeX in Slide {s['id']} field {k}: {set(matches)}")
    for cp in s.get("checkpoints", []):
        for k in ["question", "explanation"]:
            matches = raw_latex_pattern.findall(cp[k])
            if matches:
                raise ValueError(f"Found raw LaTeX in Slide {s['id']} checkpoint {cp['id']} field {k}: {set(matches)}")

for q in QUIZ_QUESTIONS:
    for k in ["question", "solution"]:
        matches = raw_latex_pattern.findall(q[k])
        if matches:
            raise ValueError(f"Found raw LaTeX in Quiz Q{q['id']} field {k}: {set(matches)}")

with open(".agents/class6_science_ch3_data.py", "w", encoding="utf-8") as f:
    f.write('"""\nNCERT Class 6 Science Chapter 3: Mindful Eating Data Module\n"""\n\n')
    f.write(f'CHAPTER_META = {repr(CHAPTER_META)}\n\n')
    f.write(f'SLIDES = {repr(SLIDES)}\n\n')
    f.write(f'QUIZ_QUESTIONS = {repr(QUIZ_QUESTIONS)}\n')

print("Successfully generated .agents/class6_science_ch3_data.py with zero raw LaTeX and rich lectures.")

