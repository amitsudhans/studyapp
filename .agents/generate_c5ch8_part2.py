"""
Part 2 of NCERT Class 5 Science Chapter 8: Clothes - How Things are Made
Slides 9 to 16
Short Headings (1-3 words) with exact same meaning:
9. Running Stitch
10. Chikankari Craft
11. Kantha Quilts
12. Phulkari Toda
13. Kashmiri Khneng
14. Cloth Upcycling
15. Fabric Testing
16. Textile Guardians
Zero Raw LaTeX! Pure clean Unicode symbols.
"""

import sys

SLIDES_PART2 = [
    {
        "id": 9,
        "title": "Running Stitch",
        "subtitle": "Activity 7 & 8: Basic Needlework & Upcycling Scraps into Functional Mats",
        "concept_html": """
            <p>While weaving creates continuous sheets of cloth, <strong>stitching</strong> uses a pointed needle and thread to join two or more pieces of fabric together, hem borders, or mend tears.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-amber-400 block mb-1">🪡 The Running Stitch (Kacha Tanka)</span>
                    <p class="text-xs text-slate-300">
                        In <strong>Activity 7</strong>, students learn the foundational hand stitch: the <strong>running stitch</strong>. The needle passes smoothly <em>in and out</em> (up and down) through the cloth in a continuous straight line, creating evenly spaced dashes of thread on both sides!
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-cyan-400 block mb-1">🧵 Joining Tailor's Fabric Scraps</span>
                    <p class="text-xs text-slate-300">
                        In <strong>Activity 8</strong>, students collect leftover colorful cloth scraps (chindi) from local tailor shops. By stitching multiple rectangular pieces side-by-side using running stitches, small discarded cut-offs are upcycled into durable table mats, potholders, or cleaning cloths!
                    </p>
                </div>
            </div>
            <p>Every complex garment—from shirts and trousers to quilts—relies on basic stitches holding pieces together along structural seams.</p>
        """,
        "spoken_text": "Now pick up a needle and thread in Activities 7 and 8 to master basic stitching! Threading cotton yarn through a steel needle's eye and tying a secure knot at the base, we practice the fundamental running stitch. The needle glides into the fabric from underneath, comes up on top, dives down again, and re-emerges in a clean straight rhythm: up, down, up, down! By connecting leftover colorful fabric scraps from neighborhood tailor shops with running stitches, we can craft delightful checkered floor mats, coasters, and tablecloths. Stitching breathes new, useful life into discarded cloth!",
        "lecture_script": "Introduces hand stitching through Activity 7 (the up-and-down rhythm of the running stitch) and Activity 8 (piecing together tailor fabric scraps into functional household textiles).",
        "checkpoints": [
            {
                "question": "What is the defining mechanical pattern of a simple 'running stitch' across fabric?",
                "options": [
                    "Passing the needle and thread up and down through the cloth in a continuous straight line",
                    "Tying fifty knots on top of each other in one single spot",
                    "Cutting circular holes into the fabric with scissors",
                    "Gluing plastic tape across the border"
                ],
                "correct": 0,
                "explanation": "A running stitch involves passing the needle in and out of the fabric at regular intervals in a straight or curved line.",
                "study_insight": "A thimble is a pitted metal or rubber cup worn over the middle fingertip to push needles through thick fabric without pricking skin."
            },
            {
                "question": "In Activity 8, what useful household items can students create by stitching leftover tailor fabric scraps together?",
                "options": [
                    "Useful table mats, cleaning cloths, patchwork coasters, and pot holders",
                    "Heavy concrete garden bricks",
                    "Drinking water glasses",
                    "Metal cooking pans"
                ],
                "correct": 0,
                "explanation": "Patchwork stitching joins small discarded fabric scraps into large, durable, washable household textiles, preventing fabric waste.",
                "study_insight": "Patchwork quilting has been practiced in rural India for centuries, creating famous layered winter quilts known as Godharis."
            }
        ]
    },
    {
        "id": 10,
        "title": "Chikankari Craft",
        "subtitle": "Regional Embroideries: Lucknow Chikankari & Rajasthani Banjara Mirror Art",
        "concept_html": """
            <p>Across India, needle and thread do far more than merely join fabric—they become brushes for exquisite storytelling through <strong>traditional embroidery</strong>.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-cyan-400 block mb-1">🕊️ Chikankari (Lucknow, Uttar Pradesh)</span>
                    <p class="text-xs text-slate-300">
                        World-famous delicate white-on-white embroidery traditionally executed on translucent cotton muslin or georgette. Master artisans use 36 distinct stitches (such as <em>Bakhiya</em> or shadow stitch, <em>Phanda</em> knots, and <em>Jaali</em> lattice work) depicting delicate floral vines, paisleys, and peacocks.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-amber-400 block mb-1">🪞 Banjara Embroidery (Rajasthan)</span>
                    <p class="text-xs text-slate-300">
                        Vibrant, bold folk embroidery crafted by the nomadic Banjara community. It features brilliant geometric diamond stitches, bright yellow and red threads, cowrie shells, and small reflective circular <strong>mirrors (abhla)</strong> locked in place by herringbone stitches to reflect desert sunshine!
                    </p>
                </div>
            </div>
            <p>Both styles reflect their regional geographic spirit: the serene refined breeze of the Awadh royal courts versus the radiant desert celebrations of Rajasthan.</p>
        """,
        "spoken_text": "Travel across India to explore regional embroideries! In the historic city of Lucknow, Uttar Pradesh, artisans craft delicate Chikankari. Using fine white cotton thread on soft muslin, they stitch gossamer shadow-work vines, delicate flower buds, and lattice jaali patterns that look like morning mist over flowers. Journey west into the sun-drenched sands of Rajasthan, and the embroidery transforms into the energetic, colorful Banjara craft! Nomadic women stitch vibrant yellow, crimson, and green geometric lines embedded with tiny shimmering glass mirrors and cowrie shells, catching the golden desert sunlight as they walk!",
        "lecture_script": "Explores two contrasting Indian embroidery traditions: Lucknow Chikankari (delicate white-on-white floral shadow work) and Rajasthani Banjara (vibrant geometric mirror-work embroidery).",
        "checkpoints": [
            {
                "question": "Which historic Indian city is world-renowned for the delicate white-on-white shadow embroidery known as 'Chikankari'?",
                "options": [
                    "Lucknow, Uttar Pradesh",
                    "Chennai, Tamil Nadu",
                    "Shimla, Himachal Pradesh",
                    "Panaji, Goa"
                ],
                "correct": 0,
                "explanation": "Lucknow is the traditional home of Chikankari embroidery, refined under the patronage of the Nawabs of Awadh over centuries.",
                "study_insight": "In Chikankari shadow work (Bakhiya), the herringbone stitch is worked on the reverse side of sheer muslin so only a delicate shadow outline shows on the front."
            },
            {
                "question": "What sparkling decorative elements are characteristically stitched into traditional Banjara embroidery from Rajasthan?",
                "options": [
                    "Small circular reflective glass mirrors (abhla) and cowrie shells",
                    "Heavy iron building bolts",
                    "Fresh flower petals that wilt in an hour",
                    "Electronic LED computer chips"
                ],
                "correct": 0,
                "explanation": "Banjara embroidery secures small glass mirrors with intricate needlework, reflecting light and traditionally believed to ward off evil spirits.",
                "study_insight": "Traditional mirrors were originally crafted by blowing thin glass globes coated on the inside with reflective zinc or lead, then cutting them into round discs."
            }
        ]
    },
    {
        "id": 11,
        "title": "Kantha Quilts",
        "subtitle": "Storytelling Textiles: Eastern Indian Kantha & Rajasthani Gota Patti",
        "concept_html": """
            <p>Indian embroidery traditions transform everyday household needs into priceless cultural artworks celebrating domestic love and royal elegance.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-rose-400 block mb-1">🧵 Kantha (West Bengal, Odisha & Tripura)</span>
                    <p class="text-xs text-slate-300">
                        Born from the sacred tradition of upcycling, rural women layer multiple soft, worn cotton sarees and dhotis. Using thread pulled from the saree borders, they quilt the layers together using rippling <strong>running stitches</strong> depicting folk tales, rural life, birds, elephants, and lotus blooms!
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-amber-400 block mb-1">👑 Gota Patti (Rajasthan)</span>
                    <p class="text-xs text-slate-300">
                        A regal applique technique originating in Rajasthan. Gold and silver metallic ribbons (zari tape) are cut into small floral petal shapes (patti), folded, and stitched onto rich silk, chiffon, or bandhani turbans and lehengas for grand festive celebrations.
                    </p>
                </div>
            </div>
            <p>Kantha turns everyday discarded fabrics into heirloom family treasures, while Gota Patti brings royal metallic grandeur to festive weddings.</p>
        """,
        "spoken_text": "Observe two more magnificent textile traditions: Kantha of Eastern India and Gota Patti of Rajasthan. In the green villages of West Bengal, Odisha, and Tripura, women take old, soft cotton sarees that have become supple with washing. They layer three or four sarees together, and using colourful threads pulled directly from the borders, they quilt the entire fabric with endless ripples of running stitches! These Kantha quilts depict village scenes, playful peacocks, and auspicious lotus flowers. Meanwhile, in royal Rajasthan, artisans craft Gota Patti by cutting shiny gold and silver ribbons into shimmering petal shapes, stitching them onto festive silks for weddings!",
        "lecture_script": "Examines Eastern Indian Kantha (upcycled layered saree quilts stitched with pictorial running stitches) and Rajasthani Gota Patti (applique ribbon art with metallic petal motifs).",
        "checkpoints": [
            {
                "question": "How did traditional 'Kantha' embroidery originate in the homes of West Bengal, Odisha, and Tripura?",
                "options": [
                    "By layering worn, soft cotton sarees and quilting them together with continuous decorative running stitches",
                    "By printing designs on plastic sheets with computers",
                    "By knitting sweaters with thick mountain wool",
                    "By melting gold coins onto cotton robes"
                ],
                "correct": 0,
                "explanation": "Kantha is an ancient upcycling art where rural women stitch layered old sarees with embroidered storytelling motifs to create warm baby wraps and quilts.",
                "study_insight": "A Nakshi Kantha is a specialized narrative quilt where every embroidered motif illustrates folk stories, wedding rituals, or rural agricultural life."
            },
            {
                "question": "What is the defining visual characteristic of Rajasthani 'Gota Patti' textile craftsmanship?",
                "options": [
                    "Gold and silver metallic ribbon tape cut into petal and leaf shapes and appliqued onto festive fabrics",
                    "Coarse black wool woven into heavy carpets",
                    "Plain white threads stitched in straight hospital lines",
                    "Fabric dipped in black mud to create shadows"
                ],
                "correct": 0,
                "explanation": "Gota is woven metallic ribbon; artisans fold and cut it into leaf/petal (patti) shapes, stitching the edges onto silk or georgette.",
                "study_insight": "Gota patti gives garments the dazzling appearance of solid gold embroidery while remaining lightweight and flexible to wear."
            }
        ]
    },
    {
        "id": 12,
        "title": "Phulkari Toda",
        "subtitle": "Agrarian & Tribal Art: Punjab's Phulkari Gardens & Nilgiri Toda Shawls",
        "concept_html": """
            <p>From the golden wheat fields of Punjab to the misty Nilgiri hills of Tamil Nadu, needlework expresses regional cultural identity and tribal heritage.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-amber-400 block mb-1">🌸 Phulkari (Punjab)</span>
                    <p class="text-xs text-slate-300">
                        Literally meaning 'flower work' (Phul + Kari). Women embroider vibrant geometric motifs using untwisted, glossy <strong>pat (floss silk)</strong> thread on coarse, homespun khaddar cotton. The darning stitch is worked entirely from the <em>reverse side</em> of the fabric without counting threads, creating a dense, velvety floral tapestry on the front!
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-rose-400 block mb-1">🏔️ Toda Embroidery (Pukhoor - Tamil Nadu)</span>
                    <p class="text-xs text-slate-300">
                        Practiced by the indigenous Toda pastoral tribe living in the Nilgiri highlands. Women embroider thick unbleached white cotton shawls (Poothkuli) using solely <strong>red and black woollen threads</strong>, counting individual fabric warp threads to create striking geometric motifs resembling buffalo horns and celestial stars.
                    </p>
                </div>
            </div>
            <p>A Punjabi bride receives an heirloom Bagh or Phulkari from her maternal grandmother, while a Toda shawl is a sacred life-long identity wrapped during tribal ceremonies.</p>
        """,
        "spoken_text": "Experience the festive colors of Punjab and the sacred tribal heritage of the Nilgiri mountains! In Punjab, women create Phulkari, which means 'flower crafting'. Using lustrous, untwisted silk floss on handspun cotton shawls, they embroider dazzling geometric diamonds and marigold gardens. Wonderfully, the embroiderer works completely from the back of the cloth, counting threads in her mind! Now travel south to the misty Nilgiri hills of Tamil Nadu, home to the ancient Toda pastoral tribe. Toda women embroider thick white shawls using only deep red and black wool. They count every weave thread to create bold, striking geometric patterns representing sacred buffalo horns and stars!",
        "lecture_script": "Contrasts Punjab's Phulkari (silk-floss floral darning stitch on khaddar cotton) with the Toda tribe's Pukhoor embroidery of the Nilgiris (red-and-black counted-thread geometric motifs on white shawls).",
        "checkpoints": [
            {
                "question": "What does the word 'Phulkari' from Punjab literally translate to in English?",
                "options": [
                    "Flower work (Phul = flower, Kari = craft)",
                    "Ocean wave",
                    "Desert sand",
                    "Running river"
                ],
                "correct": 0,
                "explanation": "Phulkari literally translates to 'flower work', celebrated for its rich, vibrant floral embroidery covering shawls and dupattas.",
                "study_insight": "When a Phulkari is so densely embroidered that the underlying base fabric is entirely hidden by silk stitches, it is reverently called a 'Bagh' (garden)."
            },
            {
                "question": "Which two specific thread colours do the indigenous Toda women of the Nilgiri hills use on their traditional white shawls?",
                "options": [
                    "Red and black",
                    "Bright neon green and purple",
                    "Yellow and pink",
                    "Gold and silver"
                ],
                "correct": 0,
                "explanation": "Toda embroidery (Pukhoor) strictly uses striking red and black woollen threads on unbleached white cotton, producing dramatic high-contrast geometric art.",
                "study_insight": "Toda embroidery has received Geographical Indication (GI) status in India, protecting the unique cultural intellectual heritage of the pastoral Nilgiri community."
            }
        ]
    },
    {
        "id": 13,
        "title": "Kashmiri Khneng",
        "subtitle": "Mountain Masterpieces: Kashmiri Kashida & Meghalaya's Khneng Eri Silk",
        "concept_html": """
            <p>From the northern snow-capped valleys to the misty cloud forests of Northeast India, regional stitching captures local biodiversity and endemic flora.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-cyan-400 block mb-1">🍁 Kashmiri Kashida & Aari (Kashmir)</span>
                    <p class="text-xs text-slate-300">
                        Celebrated for intricate nature-inspired motifs: serrated chinár tree leaves, saffron flowers, almonds (badam), irises, and nightingales (bulbul). Stitched on woollen pashminas and pherans using fine single-needle satin stitches or hooked <strong>aari needles</strong> with fine silk and wool threads.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">🐟 Khneng Embroidery (Meghalaya)</span>
                    <p class="text-xs text-slate-300">
                        An exceedingly rare, ancient embroidery preserved exclusively in the village of Mustoh in the Khasi Hills of Meghalaya. Stitched onto locally spun <strong>Eri peace silk</strong> shawls (Ryndia) using black wool, its geometric pattern mimics the delicate central spine and bones of a local river fish!
                    </p>
                </div>
            </div>
            <p>These embroidery traditions are not mere commercial garments; they are living botanical and zoological records of India's diverse regional ecosystems.</p>
        """,
        "spoken_text": "Ascend into the crisp mountain air of Kashmir, where master needleworkers practice Kashida embroidery. Inspired by the paradise gardens of the valley, their delicate needles trace rust-red maple-like chinár leaves, blooming saffron blossoms, ripe almonds, and singing nightingales on warm woollen pherans. Now journey across the country to the Khasi hills of Meghalaya! In the remote village of Mustoh, Khasi artisans practice an extraordinary embroidery called Khneng. Stitched onto cream-colored Eri peace silk using black thread, Khneng patterns faithfully depict the delicate backbone and ribs of a local river fish. It is an ancient textile homage to river ecology!",
        "lecture_script": "Explores Kashmiri Kashida (chinar leaf, saffron, and nightingale motifs on wool) and Meghalaya's rare Khneng embroidery (fish-bone motifs stitched on Eri peace silk in Mustoh village).",
        "checkpoints": [
            {
                "question": "Which iconic leaf motif inspired by Himalayan deciduous trees is frequently featured in Kashmiri Kashida embroidery?",
                "options": [
                    "The serrated Chinár (oriental plane tree) leaf",
                    "The cactus leaf",
                    "The banana leaf",
                    "The sea palm leaf"
                ],
                "correct": 0,
                "explanation": "The majestic chinar tree, whose leaves turn golden-red in autumn, is the most celebrated nature motif in Kashmiri carpets, shawls, and woodwork.",
                "study_insight": "Kashmiri artisans often use an 'Aari'—a fine hook needle that creates continuous chain-stitch loops rapidly across thick woollen carpets and shawls."
            },
            {
                "question": "What natural ecological feature does the ancient 'Khneng' embroidery of Meghalaya depict on Eri silk shawls?",
                "options": [
                    "The backbone and rib skeleton of a local freshwater river fish",
                    "A soaring eagle with giant wings",
                    "A tiger catching deer",
                    "A blooming desert cactus"
                ],
                "correct": 0,
                "explanation": "Khneng embroidery, unique to Mustoh village in Meghalaya, consists of fine geometric needlework representing the spine of a local riverine fish on traditional Ryndia silk.",
                "study_insight": "Eri silk is known as 'peace silk' or Ahimsa silk because the caterpillar naturally cuts its way out of the cocoon as a moth before the silk is reeled, without harming the insect."
            }
        ]
    },
    {
        "id": 14,
        "title": "Cloth Upcycling",
        "subtitle": "Sustainable Traditions: Hand-Me-Downs, Godharis & Zero-Waste Culture",
        "concept_html": """
            <p>Long before 'sustainability' became a global buzzword, Indian households practiced an unbroken tradition of <strong>zero-waste circular fashion</strong>.</p>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 my-3 text-xs">
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="font-bold text-emerald-400 block mb-1">👶 1. Hand-Me-Downs</span>
                    <span class="text-slate-300">Clothes outgrown by older siblings or cousins are lovingly passed down. Softened through repeated washings, they are gentler on young children's skin!</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="font-bold text-amber-400 block mb-1">🪡 2. Godhari & Quilts</span>
                    <span class="text-slate-300">Worn cotton sarees and dhotis are layered and quilted with running stitches into cozy patchwork blankets, mattress pads, and baby swaddles.</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="font-bold text-cyan-400 block mb-1">🧹 3. Final Utility</span>
                    <span class="text-slate-300">When fabric finally wears thin, it is repurposed as kitchen cleaning wipes, mop cloths (pocha), or cordage string—nothing is thrown away!</span>
                </div>
            </div>
            <p>Fast fashion—buying cheap synthetic clothes and tossing them into landfills after a few wears—clogs global waterways with microplastics. Indian textile traditions show the world how to cherish every thread!</p>
        """,
        "spoken_text": "Consider the wise, sustainable traditions of Indian homes! In our culture, a piece of clothing is almost never casually thrown away. When an older brother or sister outgrows a sturdy shirt, it is lovingly handed down to a younger cousin. Worn cotton clothes, softened by years of washing, become tender swaddling blankets for newborn babies. When grandma's cotton sarees wear thin, they are layered and hand-quilted into beautiful Godhari blankets. Finally, scraps become cleaning cloths and kitchen dusters. Every single thread serves a lifelong purpose, keeping mountains of textile garbage out of our landfills!",
        "lecture_script": "Celebrates the traditional Indian circular textile lifecycle: hand-me-down clothing sharing, quilting old sarees into Godharis/blankets, and final repurposing into household cleaning cloths.",
        "checkpoints": [
            {
                "question": "Why is passing down outgrown clothes to younger siblings or relatives an ecologically sustainable practice?",
                "options": [
                    "It extends the useful life of garments, dramatically reducing textile waste, water consumption, and chemical dyeing pollution",
                    "It turns the clothes into solid gold",
                    "It makes the fabric heavier each year",
                    "It destroys the sewing stitches"
                ],
                "correct": 0,
                "explanation": "Reusing garments reduces demand for new manufacturing, conserving thousands of litres of water and preventing synthetic textiles from choking landfills.",
                "study_insight": "Manufacturing a single new cotton t-shirt requires approximately 2,700 litres of fresh water—enough drinking water for one person for two and a half years!"
            },
            {
                "question": "What traditional Indian quilted textile is created by layering and stitching worn-out cotton sarees and dhotis together?",
                "options": [
                    "A Godhari (or Kantha quilt)",
                    "A plastic raincoat",
                    "An iron door mat",
                    "A synthetic parachute"
                ],
                "correct": 0,
                "explanation": "A Godhari is a traditional quilted cotton blanket made by layering old sarees or dhotis and securing them with dense lines of running stitches.",
                "study_insight": "In traditional rural households, making a Godhari was a joyful social activity where mothers, aunts, and grandmothers sat together to quilt and sing songs."
            }
        ]
    },
    {
        "id": 15,
        "title": "Fabric Testing",
        "subtitle": "Scientific Inquiry: Identifying Fibres by Touch, Weave Density & Flame Burn Test",
        "concept_html": """
            <p>How can a textile scientist determine whether an unknown fabric scrap is pure cotton, luxurious silk, warm wool, or synthetic polyester? Through <strong>scientific fibre testing</strong>!</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-cyan-400 block mb-1">🔍 Magnifier & Touch Test</span>
                    <p class="text-xs text-slate-300">
                        Under a magnifying lens, natural cotton shows twisted, ribbon-like fibres with matte texture. Silk filaments appear smooth, triangular, and lustrous. Synthetic polyester strands look like perfectly uniform, glassy plastic cylinders.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-rose-400 block mb-1">🔥 The Flame Burn Test (Scientific Forensic)</span>
                    <ul class="text-xs text-slate-300 space-y-1">
                        <li><strong>Cotton/Linen:</strong> Burns with a yellow flame, smells like burning paper (cellulose), leaves soft grey ash.</li>
                        <li><strong>Silk/Wool:</strong> Burns slowly with self-extinguishing flame, smells like burning hair (protein), leaves dark crushable bead.</li>
                        <li><strong>Synthetic Nylon/Polyester:</strong> Melts rapidly, drips like boiling plastic with chemical odor, forms hard black unbreakable bead!</li>
                    </ul>
                </div>
            </div>
            <p><strong>Safety Note:</strong> Burn tests must always be demonstrated by an adult teacher over a ceramic dish with cold water nearby.</p>
        """,
        "spoken_text": "How do textile scientists identify mystery fabric scraps? Through careful observation and the famous burn test! Under a magnifying glass, natural cotton threads have tiny twists, while synthetic polyester looks like flawless, shiny plastic rods. In a controlled laboratory flame test, observe the smell and ash: cotton burns cleanly with a smell of burning paper and leaves soft grey ash, because it is plant cellulose! Wool and silk burn slowly with a smell of singed hair, because they are animal proteins. But watch out for synthetic polyester: it melts instantly into a hot, sticky chemical puddle and leaves a hard, sharp plastic bead!",
        "lecture_script": "Explains textile identification methodologies: tactile feel, magnifying weave analysis, and the laboratory flame burn test distinguishing plant cellulose, animal protein, and synthetic polymers.",
        "checkpoints": [
            {
                "question": "During a scientific flame burn test, what distinct odour does a pure cotton thread produce when burning?",
                "options": [
                    "It smells like burning paper or leaves, because cotton is composed of plant cellulose",
                    "It smells like sweet melted chocolate",
                    "It smells like fresh ocean seawater",
                    "It produces no smell at all"
                ],
                "correct": 0,
                "explanation": "Because cotton is nearly 90% pure plant cellulose (the exact same chemical polymer that makes paper and wood), it smells like burning paper and leaves soft ash.",
                "study_insight": "Protein fibres like wool and silk smell distinctly like burning feathers or hair during a flame test because they contain keratin and fibroin proteins rich in sulfur."
            },
            {
                "question": "What residue is left behind when a synthetic polyester or nylon thread is burned?",
                "options": [
                    "A hard, round, uncrushable plastic bead formed from melted polymers",
                    "Fine, soft grey powder that dissolves in air",
                    "Cold drinking water",
                    "Solid copper metal wire"
                ],
                "correct": 0,
                "explanation": "Synthetic petrochemical fibres do not char into soft ash; instead, they melt into molten plastic that solidifies into a hard, rigid synthetic bead.",
                "study_insight": "A simple burn test requires only a tiny 2 cm yarn snippet held with metal tweezers over a flame-proof ceramic dish."
            }
        ]
    },
    {
        "id": 16,
        "title": "Textile Guardians",
        "subtitle": "Mindful Fashion: Honoring Handloom Artisans & Practicing Conscious Clothing Care",
        "concept_html": """
            <p>We conclude our journey into clothes and craftsmanship by recognizing our role as <strong>Textile Guardians</strong>. A piece of clothing is never just cloth—it represents soil, water, agricultural labour, and artisan genius.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-3">
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-amber-400 block mb-1">🧶 Valuing Every Individual Thread</span>
                    <p class="text-xs text-slate-300">
                        A single shirt contains over <strong>20 kilometres of spun yarn</strong>, woven across thousands of intersections. Respecting clothes means mending loose buttons, sewing popped seams, and washing garments gently instead of discarding them.
                    </p>
                </div>
                <div class="p-3 rounded-xl bg-slate-900 border border-slate-700/80">
                    <span class="text-xs font-bold text-emerald-400 block mb-1">🤝 Supporting Handloom Communities</span>
                    <p class="text-xs text-slate-300">
                        Visiting local weavers, khadi bhandars, and tailors connects us with the living hands that dress our nation. Choosing authentic Indian handlooms sustains millions of rural families and protects ancient cultural heritage.
                    </p>
                </div>
            </div>
            <p>Wear natural, mend with care, upcycle with creativity, and wear India's handcrafted pride with honour!</p>
        """,
        "spoken_text": "We conclude our journey into clothing with a heartfelt appreciation for every thread! The next time you put on your school uniform or festive kurta, remember the long chain of nature and human hands behind it: from the sun and soil that nurtured the cotton plant, to the farmer harvesting fluffy bolls, the spinner twisting fibres on a charkha, the weaver guiding shuttles across the loom, and the tailor stitching seams with needle and thread! A single shirt holds twenty kilometres of yarn and days of human devotion. Treat your clothes with care, mend loose buttons with running stitches, upcycle old fabrics, and celebrate the timeless beauty of Indian handlooms!",
        "lecture_script": "Synthesizes the entire textile supply chain from agriculture to spinning, handloom weaving, stitching, and recycling, encouraging ethical stewardship and support for artisan communities.",
        "checkpoints": [
            {
                "question": "Approximately how many total kilometres of spun thread can be interlaced inside a single cotton shirt?",
                "options": [
                    "Over 15 to 20 kilometres of thread",
                    "Only 5 centimetres",
                    "Exactly 1 metre",
                    "1,000 kilometres"
                ],
                "correct": 0,
                "explanation": "Because fine yarns are packed at 50 to 100 threads per inch across both warp and weft, an average cotton shirt contains roughly 20 km of spun fiber!",
                "study_insight": "National Handloom Day is celebrated every year in India on August 7 to commemorate the historic Swadeshi Movement launched in 1905."
            },
            {
                "question": "What is the most respectful and sustainable way to care for our personal wardrobe?",
                "options": [
                    "Mending loose seams and buttons, washing gently, and upcycling old clothes instead of throwing them away",
                    "Throwing clothes into garbage bins after wearing them twice",
                    "Burning clothes whenever they get a small stain",
                    "Only buying clothes made of plastic foil"
                ],
                "correct": 0,
                "explanation": "Proper garment care, timely mending with needle and thread, and creative upcycling preserve natural resources and reduce landfill pollution.",
                "study_insight": "Visiting a local tailor or khadi handloom cooperative gives students direct firsthand understanding of the skill, patience, and dignity of artisan labour."
            }
        ]
    }
]

print("Part 2 slides defined:", len(SLIDES_PART2))

