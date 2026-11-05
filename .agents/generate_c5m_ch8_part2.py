# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 8: Weight and Capacity
Part 2: Slides 9 to 16
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Multiplying Weights",
        "tagline": "More Operations on Weight • Scaling Quantities & Double Number Lines",
        "lecture": (
            "When dealing with multiple identical packages or scaling up a culinary recipe, we use multiplication. There are two robust mathematical pathways to multiply compound weights by a whole number. Let us examine both methods by finding the total mass of four identical sacks of potatoes, where each sack weighs two kilograms three hundred and fifty grams. In Method One, we multiply the units separately: four times two kilograms equals eight kilograms, and four times three hundred and fifty grams equals one thousand four hundred grams. Since one thousand four hundred grams exceeds one thousand, we regroup it into one kilogram and four hundred grams. Adding this carried kilogram to the eight kilograms gives nine kilograms four hundred grams. In Method Two, we convert the entire compound weight into total grams first: two kilograms three hundred and fifty grams becomes two thousand three hundred and fifty grams. Multiplying two thousand three hundred and fifty by four gives nine thousand four hundred grams. Finally, dividing by one thousand returns nine kilograms four hundred grams. Both methods yield the exact same answer! We can also visualize this proportional scaling along a double number line when adjusting recipes—doubling ingredients for four people to feed eight people. Both strategies provide clear mathematical pathways."
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>🥔</span> Two Methods to Multiply Mixed Weights
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    Calculate: 4 sacks × 2 kg 350 g per sack:
                </p>
                <div class="space-y-2 text-xs">
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60">
                        <div class="font-bold text-cyan-300 mb-1">Method 1: Unit-by-Unit Multiplication</div>
                        <ul class="text-slate-300 space-y-1 text-[11px]">
                            <li>• Multiply kg: 4 × 2 kg = 8 kg</li>
                            <li>• Multiply g: 4 × 350 g = 1,400 g = 1 kg 400 g</li>
                            <li>• Combine: 8 kg + 1 kg 400 g = <span class="font-bold text-emerald-400">9 kg 400 g</span></li>
                        </ul>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60">
                        <div class="font-bold text-amber-300 mb-1">Method 2: Convert to Grams First</div>
                        <ul class="text-slate-300 space-y-1 text-[11px]">
                            <li>• Convert: 2 kg 350 g = 2,350 g</li>
                            <li>• Multiply: 2,350 g × 4 = 9,400 g</li>
                            <li>• Reconvert: 9,400 g = <span class="font-bold text-emerald-400">9 kg 400 g</span></li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>👩‍🍳</span> Recipe Proportional Scaling
                    </h4>
                    <p class="text-xs text-slate-300 leading-relaxed mb-2">
                        When scaling up food preparation, multiply all ingredient quantities by the same scaling factor:
                    </p>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 space-y-1.5 text-xs">
                        <div class="flex justify-between border-b border-slate-700 pb-1 font-semibold text-slate-300">
                            <span>Biryani Ingredient</span>
                            <span>For 4 People</span>
                            <span class="text-emerald-400">For 8 People (×2)</span>
                        </div>
                        <div class="flex justify-between text-slate-300">
                            <span>Basmati Rice</span>
                            <span>500 g</span>
                            <span class="font-bold text-emerald-400">1,000 g (1 kg)</span>
                        </div>
                        <div class="flex justify-between text-slate-300">
                            <span>Vegetables</span>
                            <span>750 g</span>
                            <span class="font-bold text-emerald-400">1,500 g (1.5 kg)</span>
                        </div>
                        <div class="flex justify-between text-slate-300">
                            <span>Ghee</span>
                            <span>125 g</span>
                            <span class="font-bold text-emerald-400">250 g (1/4 kg)</span>
                        </div>
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-indigo-950/40 border border-indigo-800/40 text-[11px] text-indigo-200 mt-3">
                    💡 <strong>Pro Tip:</strong> Converting to total grams first is completely immune to carry-over confusion during multi-digit multiplication!
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c9_1",
                "question": "A baker prepares 6 fruit cakes. Each cake requires 1 kg 250 g of mixed candied fruit. What is the total weight of candied fruit needed?",
                "options": [
                    "6 kg 500 g",
                    "7 kg 500 g",
                    "7 kg 250 g",
                    "6 kg 250 g"
                ],
                "answer": 1,
                "hint": "Convert to grams: 1,250 g × 6, or multiply 1 kg × 6 and 250 g × 6.",
                "explanation": "Method 1: 6 × 1 kg = 6 kg, and 6 × 250 g = 1,500 g = 1 kg 500 g. Total = 6 kg + 1 kg 500 g = 7 kg 500 g (or 7 1/2 kg)."
            },
            {
                "id": "c9_2",
                "question": "A recipe uses 350 g of paneer to feed 3 family members. How much paneer is required to prepare the same dish for 9 family members?",
                "options": [
                    "700 g",
                    "1 kg 50 g",
                    "1 kg 500 g",
                    "1,050 g"
                ],
                "answer": 1,
                "hint": "9 members is 3 times 3 members. Multiply 350 g by 3.",
                "explanation": "The scaling factor is 9 ÷ 3 = 3. Multiplying 350 g × 3 gives 1,050 g, which converts to 1 kg 50 g."
            }
        ]
    },
    {
        "id": 10,
        "title": "Dividing Weights",
        "tagline": "More Operations on Weight • Equal Distribution & Scrap Dealer Rates",
        "lecture": (
            "Dividing weight quantities arises when sharing bulk supplies equally among several people or calculating the cost per kilogram at a scrap dealer. Suppose a cooperative store receives a large crate containing seven kilograms five hundred grams of roasted cashew nuts, which must be divided equally into six identical gift packets. How much does each packet weigh? The cleanest strategy is to convert the compound mass into total grams first. Seven kilograms five hundred grams equals seven thousand five hundred grams. Now, perform single whole-number division: seven thousand five hundred divided by six. Seven divided by six gives one with a remainder of one. Bring down five to make fifteen; fifteen divided by six gives two with a remainder of three. Bring down zero to make thirty; thirty divided by six gives five with zero remainder. Finally, bring down the last zero to get zero. The quotient is exactly one thousand two hundred and fifty grams. Splitting this back into compound units gives one kilogram two hundred and fifty grams per packet. We also encounter division when dealing with scrap dealers: if eight kilograms of discarded newspaper fetches one hundred and twelve rupees, dividing one hundred and twelve by eight gives the unit rate of fourteen rupees per kilogram. Division helps us allocate resources fairly and evaluate economic unit values."
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>🥜</span> Fair Sharing: 7 kg 500 g ÷ 6 Packets
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    Converting compound weight to grams simplifies long division into standard arithmetic:
                </p>
                <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-700/80 font-mono text-xs space-y-2">
                    <div class="flex justify-between border-b border-slate-700 pb-1">
                        <span class="text-slate-400">Total Cashews:</span>
                        <span class="text-cyan-300 font-bold">7 kg 500 g = 7,500 g</span>
                    </div>
                    <div class="flex justify-between border-b border-slate-700 pb-1">
                        <span class="text-slate-400">Division:</span>
                        <span class="text-amber-300 font-bold">7,500 g ÷ 6 = 1,250 g</span>
                    </div>
                    <div class="flex justify-between pt-1">
                        <span class="text-emerald-400 font-bold">Per Packet:</span>
                        <span class="text-emerald-400 font-black">1 kg 250 g (1 1/4 kg)</span>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>📰</span> Scrap Dealer Unit Pricing Ledger
                    </h4>
                    <p class="text-xs text-slate-300 leading-relaxed mb-2">
                        Calculate the rate per kg: Rate = Total Earnings ÷ Total Mass:
                    </p>
                    <div class="space-y-1.5 text-xs">
                        <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                            <span class="text-slate-300">🗞️ Old Newspapers</span>
                            <span class="text-slate-400">8 kg sold for ₹112</span>
                            <span class="font-bold text-emerald-400">₹14 / kg</span>
                        </div>
                        <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                            <span class="text-slate-300">🔩 Waste Iron</span>
                            <span class="text-slate-400">5 kg sold for ₹140</span>
                            <span class="font-bold text-cyan-400">₹28 / kg</span>
                        </div>
                        <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                            <span class="text-slate-300">🥤 Plastic Bottles</span>
                            <span class="text-slate-400">12 kg sold for ₹144</span>
                            <span class="font-bold text-amber-400">₹12 / kg</span>
                        </div>
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-800/40 text-[11px] text-emerald-200 mt-3">
                    💡 <strong>Economic Insight:</strong> Knowing the rate per kilogram allows you to predict earnings for any quantity: 20 kg of iron = 20 × ₹28 = ₹560!
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c10_1",
                "question": "A 9 kg sack of basmati rice is divided equally into 8 smaller cloth bags. What is the mass of rice in each bag?",
                "options": [
                    "1 kg 125 g",
                    "1 kg 250 g",
                    "1 kg 150 g",
                    "1 kg 75 g"
                ],
                "answer": 0,
                "hint": "Convert 9 kg to 9,000 g and divide by 8.",
                "explanation": "9 kg = 9,000 g. 9,000 ÷ 8 = 1,125 g. Converting back gives 1 kg 125 g (or 1 1/8 kg)."
            },
            {
                "id": "c10_2",
                "question": "Rohan sells 15 kg of cardboard boxes to a kabadiwala and receives ₹180 in total. What was the rate per kilogram paid by the kabadiwala?",
                "options": [
                    "₹10 per kg",
                    "₹12 per kg",
                    "₹14 per kg",
                    "₹15 per kg"
                ],
                "answer": 1,
                "hint": "Divide the total money by the total weight: ₹180 ÷ 15 kg.",
                "explanation": "Rate per kg = Total Price ÷ Total Weight = ₹180 ÷ 15 = ₹12 per kg."
            }
        ]
    },
    {
        "id": 11,
        "title": "Measuring Capacity",
        "tagline": "Introduction to Litres and Millilitres • Everyday Liquid Volumes",
        "lecture": (
            "Just as weight measures the gravitational pull on an object's mass, capacity measures the maximum volume of liquid that a three-dimensional hollow container can hold. In the international metric system, the standard unit of capacity is the litre, symbolized by a capital L or lowercase l. For smaller liquid quantities, we use the millilitre, abbreviated as mL. Exactly one thousand millilitres make up one litre. To build an intuitive grasp of capacity, let us explore familiar liquid benchmarks. A small medicinal spoon or dropper holds about five millilitres of syrup. A ceramic teacup holds approximately one hundred and fifty millilitres of tea. A standard glass of drinking water contains about two hundred and fifty millilitres. A tetra-pack juice carton holds one litre, which is one thousand millilitres. In household chores, a bathroom bucket typically holds fifteen to twenty litres of water. The overhead water storage tank installed on a residential rooftop holds between five hundred and one thousand litres! When choosing units, we measure cough syrup, eye drops, ink bottles, and perfumes in millilitres, while water tanks, petrol fuel, milk deliveries, and swimming pools are measured in litres. Recognizing these real-world benchmarks helps us select the correct metric unit for any liquid volume."
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>💧</span> Real-World Liquid Benchmarks
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    Capacity reflects container volume. Notice how units scale across everyday liquids:
                </p>
                <div class="grid grid-cols-2 gap-2 text-xs">
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-300">🥄 Medicine Spoon</span>
                        <span class="font-bold text-emerald-400">5 mL</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-300">☕ Chai Cup</span>
                        <span class="font-bold text-emerald-400">150 mL</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-300">🥛 Drinking Glass</span>
                        <span class="font-bold text-cyan-400">250 mL</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-300">🧃 Juice Carton</span>
                        <span class="font-bold text-cyan-400">1,000 mL (1 L)</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-300">🪣 Bath Bucket</span>
                        <span class="font-bold text-amber-400">15 to 20 L</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-300">🏠 Rooftop Tank</span>
                        <span class="font-bold text-indigo-400">500 to 1,000 L</span>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>🧪</span> The Litre-Millilitre Relationship
                    </h4>
                    <div class="p-4 rounded-xl bg-gradient-to-r from-blue-500/10 via-cyan-500/10 to-teal-500/10 border border-cyan-500/30 text-center my-3">
                        <div class="text-2xl font-black text-cyan-300 tracking-wide">1 Litre (L) = 1,000 mL</div>
                        <div class="text-[11px] text-slate-400 mt-1">1 mL = 1/1,000 L = 0.001 L</div>
                    </div>
                    <ul class="text-xs text-slate-300 space-y-2 leading-relaxed">
                        <li class="flex items-start gap-2">
                            <span class="text-emerald-400 font-bold">•</span>
                            <span><strong>Quarter Litre (1/4 L):</strong> Exactly 250 mL (one standard drinking glass).</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <span class="text-emerald-400 font-bold">•</span>
                            <span><strong>Half Litre (1/2 L):</strong> Exactly 500 mL (two standard drinking glasses).</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <span class="text-emerald-400 font-bold">•</span>
                            <span><strong>Three-Quarter Litre (3/4 L):</strong> Exactly 750 mL (three standard drinking glasses).</span>
                        </li>
                    </ul>
                </div>
                <div class="p-2.5 rounded-lg bg-cyan-950/40 border border-cyan-800/40 text-[11px] text-cyan-200 mt-3">
                    💡 <strong>Unit Selection Rule:</strong> If the volume can easily fit inside a small handheld cup, choose mL. If it fills a bucket or tank, choose L.
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c11_1",
                "question": "Which of the following items is most appropriately measured using millilitres (mL) rather than litres (L)?",
                "options": [
                    "Water inside a residential rooftop storage tank",
                    "A doctor's eye-drop bottle",
                    "Petrol pumped into a highway tour bus",
                    "Water inside an Olympic swimming pool"
                ],
                "answer": 1,
                "hint": "Think about which item holds only a few drops or a tiny fraction of a glass.",
                "explanation": "An eye-drop bottle holds around 5 to 10 mL of liquid. Rooftop tanks, bus petrol tanks, and swimming pools hold hundreds to thousands of litres."
            },
            {
                "id": "c11_2",
                "question": "How many 250 mL glasses of water are required to completely fill a 2-litre water jug?",
                "options": [
                    "4 glasses",
                    "6 glasses",
                    "8 glasses",
                    "10 glasses"
                ],
                "answer": 2,
                "hint": "Convert 2 litres to millilitres: 2 L = 2,000 mL. Then divide by 250 mL.",
                "explanation": "2 L = 2,000 mL. Since each glass is 250 mL, 2,000 ÷ 250 = 8 glasses (4 glasses make 1 L, so 8 glasses make 2 L)."
            }
        ]
    },
    {
        "id": 12,
        "title": "Volume Scales",
        "tagline": "Big to Small, Small to Big • Reading Graduated Cylinders & The Meniscus",
        "lecture": (
            "To measure liquid capacity accurately in science laboratories and pharmacies, we use transparent graduated cylinders, beakers, and measuring jars. These cylinders feature engraved vertical scale markings called graduations. When reading any graduated cylinder, two essential mathematical rules must be observed. First, determine the value of each subdivision mark by checking the interval between major numbered lines. For example, if the distance between zero and one hundred millilitres is divided into ten equal tick spaces, each single subdivision mark represents ten millilitres. If divided into five tick spaces, each mark represents twenty millilitres. Second, observe the unique physical shape of the water surface. Due to surface tension and adhesion with the cylinder wall, water curves slightly upward at the edges, forming a curved dip called a meniscus. The universal scientific convention is to always read the volume at the absolute bottom of this curved meniscus, keeping your eye at the exact horizontal level of the liquid surface. Looking from above causes parallax errors that make the volume seem too high, while looking from below makes it seem too low. Graduated cylinders also show how small units combine to fill larger vessels—such as ten two-hundred-millilitre measuring cups perfectly filling a two-litre jar. Accurate observation ensures scientific precision."
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>👁️</span> The Meniscus Eye-Level Reading Rule
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    Liquids adhere to glass surfaces, creating a concave curved boundary. Read strictly at the lowest central point:
                </p>
                <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700/80 space-y-2 text-xs">
                    <div class="flex items-center gap-3 p-2 rounded-lg bg-rose-950/30 border border-rose-800/30">
                        <span class="text-rose-400 font-bold">❌ High Angle:</span>
                        <span class="text-slate-300">Looking down produces an over-estimation reading error.</span>
                    </div>
                    <div class="flex items-center gap-3 p-2 rounded-lg bg-emerald-950/40 border border-emerald-800/40">
                        <span class="text-emerald-400 font-bold">✓ Eye Level:</span>
                        <span class="text-slate-200 font-semibold">Align eye directly horizontal with the bottom of the curved meniscus!</span>
                    </div>
                    <div class="flex items-center gap-3 p-2 rounded-lg bg-rose-950/30 border border-rose-800/30">
                        <span class="text-rose-400 font-bold">❌ Low Angle:</span>
                        <span class="text-slate-300">Looking up produces an under-estimation reading error.</span>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>🧪</span> Container Refill Partitions
                    </h4>
                    <p class="text-xs text-slate-300 leading-relaxed mb-2">
                        How many smaller calibrated scoops or cups fill standard bottles?
                    </p>
                    <div class="space-y-1.5 text-xs">
                        <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                            <span class="text-slate-300">1 L Bottle</span>
                            <span class="text-cyan-300 font-mono">1,000 mL ÷ 100 mL</span>
                            <span class="font-bold text-emerald-400">= 10 scoops of 100 mL</span>
                        </div>
                        <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                            <span class="text-slate-300">1 L Bottle</span>
                            <span class="text-cyan-300 font-mono">1,000 mL ÷ 200 mL</span>
                            <span class="font-bold text-emerald-400">= 5 cups of 200 mL</span>
                        </div>
                        <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                            <span class="text-slate-300">2 L Jug</span>
                            <span class="text-cyan-300 font-mono">2,000 mL ÷ 250 mL</span>
                            <span class="font-bold text-emerald-400">= 8 glasses of 250 mL</span>
                        </div>
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-amber-950/40 border border-amber-800/40 text-[11px] text-amber-200 mt-3">
                    📏 <strong>Tick Scale Formula:</strong> Value of 1 division = (Upper Mark - Lower Mark) ÷ Number of subdivision spaces.
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c12_1",
                "question": "A 500 mL measuring cylinder has major markings at every 100 mL. Between 200 mL and 300 mL, there are 5 equal spaces. If the liquid meniscus touches the 3rd mark past 200 mL, what is the volume?",
                "options": [
                    "230 mL",
                    "260 mL",
                    "215 mL",
                    "250 mL"
                ],
                "answer": 1,
                "hint": "Each subdivision space = (300 - 200) ÷ 5 = 100 ÷ 5 = 20 mL.",
                "explanation": "Each division represents 100 ÷ 5 = 20 mL. 3 marks past 200 mL equals 200 + (3 × 20) = 200 + 60 = 260 mL."
            },
            {
                "id": "c12_2",
                "question": "A laboratory technician needs 1 litre 500 mL of saline solution. How many 150 mL test beakers must be poured to obtain this exact volume?",
                "options": [
                    "8 beakers",
                    "10 beakers",
                    "12 beakers",
                    "15 beakers"
                ],
                "answer": 1,
                "hint": "Convert 1 L 500 mL to mL: 1,500 mL. Divide by 150 mL.",
                "explanation": "1 L 500 mL = 1,500 mL. Dividing 1,500 mL ÷ 150 mL = 10 beakers."
            }
        ]
    },
    {
        "id": 13,
        "title": "Capacity Equivalence",
        "tagline": "Different Units but Same Measure • Khayal Chacha's Milk Route & 3-Digit mL",
        "lecture": (
            "Every morning across towns and villages in India, milk vendors like Khayal chacha deliver fresh milk to neighborhood doorsteps. Khayal chacha carries large steel milk cans on his bicycle, fitted with brass measuring ladles of five hundred millilitres, two hundred and fifty millilitres, and one hundred millilitres. In his delivery diary, Khayal chacha logs each family's daily order. Some customers ask for compound quantities like one litre five hundred millilitres, while others ask for fifteen hundred millilitres. Are these two quantities identical? Yes, absolutely! One litre equals one thousand millilitres; adding five hundred millilitres yields one thousand five hundred millilitres. Just as with weights, capacity obeys the strict three-digit millilitre rule because one litre contains one thousand millilitres. Consider a customer who orders two litres seventy-five millilitres. A careless apprentice might write two thousand seven hundred and fifty millilitres. But that would deliver almost three litres! Seventy-five millilitres has zero hundreds, so it must be written as zero-seven-five. The correct volume is two thousand and seventy-five millilitres. Similarly, three thousand and forty millilitres splits into three litres and forty millilitres. Khayal chacha verifies his weekly accounts by adding customer logs using double number lines that keep litres and millilitres in synchronized harmony."
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>🥛</span> Khayal Chacha's Daily Milk Ledger
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    Notice how compound litre-millilitre orders translate directly into total millilitres:
                </p>
                <div class="space-y-2 text-xs">
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <div>
                            <div class="font-bold text-slate-200">Sharma Family: 1 L 500 mL</div>
                            <div class="text-[11px] text-slate-400">1,000 mL + 500 mL</div>
                        </div>
                        <span class="font-mono font-bold text-emerald-400">1,500 mL</span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <div>
                            <div class="font-bold text-slate-200">Verma Family: 2 L 75 mL</div>
                            <div class="text-[11px] text-slate-400">2,000 mL + 075 mL</div>
                        </div>
                        <span class="font-mono font-bold text-emerald-400">2,075 mL <span class="text-amber-400 text-[10px]">(not 2,750!)</span></span>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <div>
                            <div class="font-bold text-slate-200">Patel Family: 3 L 8 mL</div>
                            <div class="text-[11px] text-slate-400">3,000 mL + 008 mL</div>
                        </div>
                        <span class="font-mono font-bold text-emerald-400">3,008 mL <span class="text-amber-400 text-[10px]">(not 3,800!)</span></span>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>🔍</span> Decomposing Total Millilitres
                    </h4>
                    <p class="text-xs text-slate-300 leading-relaxed mb-3">
                        The digit in the thousands place gives whole litres; the remaining three digits give millilitres:
                    </p>
                    <div class="space-y-2 text-xs font-mono">
                        <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                            <span class="text-cyan-300 font-bold">4,650 mL</span>
                            <span class="text-slate-400">➔</span>
                            <span class="text-slate-200">4 L 650 mL</span>
                        </div>
                        <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                            <span class="text-cyan-300 font-bold">5,040 mL</span>
                            <span class="text-slate-400">➔</span>
                            <span class="text-slate-200">5 L 40 mL</span>
                        </div>
                        <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                            <span class="text-cyan-300 font-bold">7,005 mL</span>
                            <span class="text-slate-400">➔</span>
                            <span class="text-slate-200">7 L 5 mL</span>
                        </div>
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-indigo-950/40 border border-indigo-800/40 text-[11px] text-indigo-200 mt-3">
                    🥛 <strong>Standard Brass Measures:</strong> Khayal chacha uses 500 mL, 200 mL, and 100 mL ladles. To pour 800 mL, he dips the 500 mL ladle once, 200 mL once, and 100 mL once!
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c13_1",
                "question": "A milkman delivers 3 litres 60 millilitres of buffalo milk to a sweet shop. What is this volume in total millilitres?",
                "options": [
                    "3,600 mL",
                    "3,060 mL",
                    "360 mL",
                    "30,060 mL"
                ],
                "answer": 1,
                "hint": "3 L = 3,000 mL. Write 60 mL with a leading zero as 060.",
                "explanation": "3 L = 3,000 mL. Adding 60 mL gives 3,000 + 60 = 3,060 mL. 3,600 mL would be 3 L 600 mL."
            },
            {
                "id": "c13_2",
                "question": "A water filter pitcher contains 4,050 mL of purified water. How is this quantity written in litres and millilitres?",
                "options": [
                    "40 L 50 mL",
                    "4 L 500 mL",
                    "4 L 50 mL",
                    "40 L 5 mL"
                ],
                "answer": 2,
                "hint": "Divide by 1,000: 4,050 = 4,000 + 50.",
                "explanation": "4,050 mL = 4,000 mL + 50 mL = 4 L 50 mL."
            }
        ]
    },
    {
        "id": 14,
        "title": "Volume Calculations",
        "tagline": "Let Us Think • Dialogue Errors (1,400 mL vs 1,040 mL) & Daily Hydration",
        "lecture": (
            "Clear communication in mathematics prevents serious real-world misunderstandings. In a famous classroom dialogue, two students debated a bottle label: Arjun stated that one litre forty millilitres equals one thousand four hundred millilitres, while Priya maintained it was one thousand and forty millilitres. Who was correct? Priya was absolutely right! One thousand four hundred millilitres equals one litre four hundred millilitres—four hundred millilitres is nearly half a litre, whereas forty millilitres is barely three tablespoons! Confusing forty with four hundred changes the volume by three hundred and sixty millilitres. We also use capacity calculations to monitor daily personal health through hydration tracking. Medical doctors recommend that a ten-year-old child drink approximately two litres five hundred millilitres of water every day to stay active and healthy. Suppose Aarav drinks two hundred and fifty millilitres before school, five hundred millilitres during morning recess, seven hundred and fifty millilitres in the afternoon, and five hundred millilitres after football practice. Adding these amounts: two hundred and fifty plus five hundred plus seven hundred and fifty plus five hundred equals two thousand millilitres, which is two litres. Subtracting two litres from his goal of two point five litres shows he needs five hundred millilitres more before bedtime. Mathematics keeps our bodies properly hydrated!"
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>🗣️</span> Dialogue Error Analysis
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    Compare Arjun's claim versus Priya's claim on "1 L 40 mL":
                </p>
                <div class="space-y-2 text-xs">
                    <div class="p-2.5 rounded-lg bg-rose-950/40 border border-rose-800/40">
                        <div class="font-bold text-rose-300">❌ Arjun's Error: 1 L 40 mL = 1,400 mL</div>
                        <p class="text-[11px] text-slate-300 mt-1">
                            Arjun misplaced the zero in the tens place! 1,400 mL = 1 L 400 mL (nearly half a litre more than 40 mL).
                        </p>
                    </div>
                    <div class="p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-800/40">
                        <div class="font-bold text-emerald-300">✓ Priya's Truth: 1 L 40 mL = 1,040 mL</div>
                        <p class="text-[11px] text-slate-300 mt-1">
                            1 L = 1,000 mL. 40 mL has 0 hundreds, 4 tens, 0 ones: 1,000 + 040 = 1,040 mL.
                        </p>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>🚰</span> Aarav's Daily Hydration Log
                    </h4>
                    <p class="text-xs text-slate-300 leading-relaxed mb-2">
                        Recommended Daily Water Target = <strong>2,500 mL (2 L 500 mL)</strong>:
                    </p>
                    <div class="space-y-1.5 text-xs">
                        <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                            <span class="text-slate-300">🌅 Morning Wakeup</span>
                            <span class="font-mono text-cyan-300">1 glass</span>
                            <span class="font-bold text-emerald-400">250 mL</span>
                        </div>
                        <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                            <span class="text-slate-300">🥪 School Lunch Recess</span>
                            <span class="font-mono text-cyan-300">2 glasses</span>
                            <span class="font-bold text-emerald-400">500 mL</span>
                        </div>
                        <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                            <span class="text-slate-300">🏠 Afternoon Homework</span>
                            <span class="font-mono text-cyan-300">3 glasses</span>
                            <span class="font-bold text-emerald-400">750 mL</span>
                        </div>
                        <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                            <span class="text-slate-300">⚽ Evening Sports</span>
                            <span class="font-mono text-cyan-300">2 glasses</span>
                            <span class="font-bold text-emerald-400">500 mL</span>
                        </div>
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-blue-950/40 border border-blue-800/40 text-[11px] text-blue-200 mt-3">
                    💧 <strong>Current Total:</strong> 2,000 mL (2 L). Remaining to goal: 2,500 - 2,000 = 500 mL (2 more glasses before sleep!).
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c14_1",
                "question": "What is the difference in volume between 1 litre 400 millilitres and 1 litre 40 millilitres?",
                "options": [
                    "360 mL",
                    "400 mL",
                    "40 mL",
                    "3,960 mL"
                ],
                "answer": 0,
                "hint": "Convert both to millilitres: 1,400 mL and 1,040 mL. Subtract them.",
                "explanation": "1 L 400 mL = 1,400 mL. 1 L 40 mL = 1,040 mL. Difference = 1,400 - 1,040 = 360 mL."
            },
            {
                "id": "c14_2",
                "question": "Meera's doctor recommends drinking 2 L of fluid daily. She drinks 350 mL of milk, 1 L 200 mL of water, and 250 mL of soup. Has she met her daily requirement?",
                "options": [
                    "No, she is short by 200 mL",
                    "Yes, she drank exactly 2 L",
                    "No, she is short by 400 mL",
                    "Yes, she drank 200 mL extra"
                ],
                "answer": 0,
                "hint": "Sum all fluids: 350 mL + 1,200 mL + 250 mL = 1,800 mL. Target is 2,000 mL.",
                "explanation": "Total fluids = 350 + 1,200 + 250 = 1,800 mL (1 L 800 mL). Her target is 2 L = 2,000 mL. Shortfall = 2,000 - 1,800 = 200 mL."
            }
        ]
    },
    {
        "id": 15,
        "title": "Comparing Capacities",
        "tagline": "Let Us Compare • Petrol Pump Volume Operations & Fuel Arithmetic",
        "lecture": (
            "A highway petrol pump is a dynamic real-world laboratory of capacity arithmetic. At a petrol pump, fuel dispensers meter liquid petrol and diesel with electronic precision, measuring every millilitre pumped into fuel tanks. Different motor vehicles have vastly different fuel tank capacities depending on their engine power and travel range. A motorcycle or two-wheeler has a fuel tank holding about ten to twelve litres. An auto-rickshaw holds about fifteen litres. A family passenger car holds around forty-five litres. A long-distance interstate passenger bus holds about two hundred litres, while a heavy eighteen-wheel multi-axle freight truck has fuel tanks holding up to three hundred and fifty litres or more! Comparing these capacities using relational inequality symbols: two-wheeler less than car, car less than bus, bus less than freight truck. We also solve refuelling operations: if a car with a forty-five litre tank arrives at the pump with twelve litres eight hundred millilitres of fuel remaining, how much fuel is required to fill the tank completely? We subtract twelve litres eight hundred millilitres from forty-five litres. Regrouping one litre as one thousand millilitres from forty-five gives forty-four litres one thousand millilitres. Subtracting leaves thirty-two litres two hundred millilitres. Fuel arithmetic combines practical economics and volume measurement."
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>⛽</span> Vehicle Fuel Tank Capacities
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    Notice how fuel tank sizes scale across vehicle categories:
                </p>
                <div class="space-y-2 text-xs">
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-300">🛵 Two-Wheeler Motorcycle</span>
                        <span class="font-bold text-emerald-400">~10 to 12 L</span>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-300">🛺 Auto-Rickshaw</span>
                        <span class="font-bold text-emerald-400">~15 L</span>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-300">🚗 Family Sedan / Car</span>
                        <span class="font-bold text-cyan-400">~45 L</span>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-300">🚌 Tour Bus</span>
                        <span class="font-bold text-amber-400">~200 L</span>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900/60 border border-slate-700/60 flex items-center justify-between">
                        <span class="text-slate-300">🚛 Multi-Axle Freight Truck</span>
                        <span class="font-bold text-indigo-400">~350 L</span>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>🧮</span> Fuel Refill Subtraction Algorithm
                    </h4>
                    <p class="text-xs text-slate-300 leading-relaxed mb-2">
                        Fuel needed to fill a 45 L car tank with 12 L 800 mL already inside:
                    </p>
                    <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700/80 font-mono text-xs space-y-1">
                        <div class="flex justify-between text-slate-400 border-b border-slate-700 pb-1">
                            <span>LINE</span>
                            <span class="w-16 text-right">LITRES</span>
                            <span class="w-20 text-right">MILLILITRES</span>
                        </div>
                        <div class="flex justify-between text-amber-400 text-[11px]">
                            <span>Borrow 1 L:</span>
                            <span class="w-16 text-right">44</span>
                            <span class="w-20 text-right">(1,000)</span>
                        </div>
                        <div class="flex justify-between text-slate-200">
                            <span>Full Tank:</span>
                            <span class="w-16 text-right">45</span>
                            <span class="w-20 text-right">000</span>
                        </div>
                        <div class="flex justify-between text-slate-200 border-b border-slate-700">
                            <span>Current Fuel:</span>
                            <span class="w-16 text-right">- 12</span>
                            <span class="w-20 text-right">- 800</span>
                        </div>
                        <div class="flex justify-between text-emerald-400 font-bold text-sm pt-1">
                            <span>NEEDED:</span>
                            <span class="w-16 text-right">32 L</span>
                            <span class="w-20 text-right">200 mL</span>
                        </div>
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-800/40 text-[11px] text-emerald-200 mt-3">
                    💡 <strong>Inequality Chain:</strong> 12 L < 15 L < 45 L < 200 L < 350 L (Motorcycle < Auto < Car < Bus < Truck).
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c15_1",
                "question": "A motorcycle tank has a capacity of 12 litres. If it currently contains 4 litres 350 millilitres of petrol, how much more petrol is required to top up the tank completely?",
                "options": [
                    "7 L 650 mL",
                    "8 L 650 mL",
                    "7 L 350 mL",
                    "8 L 350 mL"
                ],
                "answer": 0,
                "hint": "Borrow 1 L from 12 L to make 11 L 1,000 mL. Subtract 4 L 350 mL.",
                "explanation": "12 L 000 mL - 4 L 350 mL: Borrow 1 L to get 11 L 1,000 mL. Millilitres: 1,000 - 350 = 650 mL. Litres: 11 - 4 = 7 L. Needed = 7 L 650 mL."
            },
            {
                "id": "c15_2",
                "question": "A tour bus driver started the morning with 65 L of diesel. During the trip, 120 L 500 mL of diesel was added. At the end of the trip, 32 L 200 mL remained. How much diesel was consumed?",
                "options": [
                    "153 L 300 mL",
                    "152 L 300 mL",
                    "153 L 700 mL",
                    "185 L 500 mL"
                ],
                "answer": 0,
                "hint": "Total diesel available = 65 L + 120 L 500 mL = 185 L 500 mL. Subtract the remaining 32 L 200 mL.",
                "explanation": "Total fuel = 65 L 000 mL + 120 L 500 mL = 185 L 500 mL. Consumed fuel = 185 L 500 mL - 32 L 200 mL = 153 L 300 mL."
            }
        ]
    },
    {
        "id": 16,
        "title": "Multi-step Problems",
        "tagline": "Let Us Solve • Juice Vendors, Oil Partitioning & Commercial Packaging",
        "lecture": (
            "In practical commerce and community life, mathematical challenges rarely consist of a single isolated calculation. Instead, they require multi-step reasoning: converting units, executing division or multiplication, and calculating monetary costs or earnings. Consider a sugarcane juice vendor who prepares a large ten-litre insulated dispenser of freshly squeezed cane juice for an afternoon cricket tournament. The vendor serves the juice in uniform paper cups holding two hundred millilitres each, charging fifteen rupees per cup. How many cups can he serve, and how much total money does he earn? Step one: convert ten litres into millilitres: ten times one thousand equals ten thousand millilitres. Step two: divide ten thousand millilitres by two hundred millilitres per cup: ten thousand divided by two hundred equals fifty cups. Step three: multiply the number of cups by the price per cup: fifty cups times fifteen rupees equals seven hundred and fifty rupees total earnings! Another multi-step task involves packaging fifteen litres of mustard oil into seven hundred and fifty millilitre bottles: fifteen thousand divided by seven hundred and fifty equals exactly twenty bottles. Solving multi-step problems systematically by breaking them into logical sequential stages empowers you to master real-world mathematics with complete accuracy."
        ),
        "content_html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                <h4 class="text-sm font-bold text-amber-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                    <span>🥤</span> Sugarcane Juice Vendor Logistics
                </h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-3">
                    Analyze the 3-step breakdown for 10 L of juice sold in 200 mL cups at ₹15 each:
                </p>
                <div class="space-y-2 text-xs">
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60">
                        <div class="flex justify-between font-bold text-slate-200">
                            <span>Step 1: Unit Harmonization</span>
                            <span class="text-cyan-400">10,000 mL</span>
                        </div>
                        <p class="text-[11px] text-slate-400 mt-0.5">10 L × 1,000 mL/L = 10,000 mL total juice.</p>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60">
                        <div class="flex justify-between font-bold text-slate-200">
                            <span>Step 2: Container Partitioning</span>
                            <span class="text-amber-400">50 Cups</span>
                        </div>
                        <p class="text-[11px] text-slate-400 mt-0.5">10,000 mL ÷ 200 mL per cup = 50 cups served.</p>
                    </div>
                    <div class="p-2.5 rounded-lg bg-slate-900/60 border border-slate-700/60">
                        <div class="flex justify-between font-bold text-slate-200">
                            <span>Step 3: Revenue Calculation</span>
                            <span class="text-emerald-400">₹750 Total</span>
                        </div>
                        <p class="text-[11px] text-slate-400 mt-0.5">50 cups × ₹15 per cup = ₹750 earned.</p>
                    </div>
                </div>
            </div>
            <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700 flex flex-col justify-between">
                <div>
                    <h4 class="text-sm font-bold text-cyan-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                        <span>🧴</span> Mustard Oil Partitioning Station
                    </h4>
                    <p class="text-xs text-slate-300 leading-relaxed mb-2">
                        Dividing a 15-litre bulk tin into 750 mL commercial retail bottles:
                    </p>
                    <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700/80 font-mono text-xs space-y-1.5">
                        <div class="flex justify-between text-slate-300">
                            <span>Bulk Oil Tin:</span>
                            <span class="text-cyan-300 font-bold">15 L = 15,000 mL</span>
                        </div>
                        <div class="flex justify-between text-slate-300">
                            <span>Bottle Volume:</span>
                            <span class="text-amber-300 font-bold">750 mL per bottle</span>
                        </div>
                        <div class="flex justify-between border-t border-slate-700 pt-1 text-emerald-400 font-black text-sm">
                            <span>Total Bottles Packed:</span>
                            <span>15,000 ÷ 750 = 20 Bottles</span>
                        </div>
                    </div>
                </div>
                <div class="p-2.5 rounded-lg bg-indigo-950/40 border border-indigo-800/40 text-[11px] text-indigo-200 mt-3">
                    📌 <strong>General Strategy:</strong> (1) Convert all quantities to the smaller unit. (2) Divide total volume by unit size. (3) Multiply count by unit price.
                </div>
            </div>
        </div>
        """,
        "checkpoints": [
            {
                "id": "c16_1",
                "question": "A dairy cooperative has 24 litres of buttermilk. They pack it into pouches holding 400 mL each and sell each pouch for ₹12. What is their total revenue if all pouches are sold?",
                "options": [
                    "₹600",
                    "₹720",
                    "₹840",
                    "₹960"
                ],
                "answer": 1,
                "hint": "Convert 24 L to 24,000 mL. Find number of pouches: 24,000 ÷ 400. Then multiply by ₹12.",
                "explanation": "24 L = 24,000 mL. Number of pouches = 24,000 ÷ 400 = 60 pouches. Total revenue = 60 × ₹12 = ₹720."
            },
            {
                "id": "c16_2",
                "question": "A picnic group brings three 2-litre bottles of lemonade. They pour 150 mL into each of 35 paper cups for the children. How much lemonade remains in the bottles?",
                "options": [
                    "750 mL",
                    "500 mL",
                    "1 L 250 mL",
                    "1,750 mL"
                ],
                "answer": 0,
                "hint": "Total lemonade = 3 × 2,000 mL = 6,000 mL. Used lemonade = 35 × 150 mL = 5,250 mL.",
                "explanation": "Total lemonade = 3 × 2,000 mL = 6,000 mL. Lemonade poured = 35 × 150 mL = 5,250 mL. Remaining = 6,000 - 5,250 = 750 mL (or 3/4 L)."
            }
        ]
    }
]

