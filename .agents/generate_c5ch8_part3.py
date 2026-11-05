"""
Part 3 of NCERT Class 5 Science Chapter 8: Clothes - How Things are Made
Mastery Challenge Quiz Questions 1 to 40 (Slides 17 to 20)
10 Questions per Challenge Slide with instant feedback, explanation, and solution_html.
Zero Raw LaTeX! Pure clean Unicode symbols.
"""

import sys

QUIZ_QUESTIONS = [
    # =========================================================================
    # Challenge 1 (Q1 to Q10): Nature's Weavers, Warp & Weft, Handlooms, Spinning
    # =========================================================================
    {
        "id": 1,
        "question": "Which natural creature constructs intricate pouch-shaped hanging nests by interlacing grass ribbons over and under each other?",
        "options": [
            "The Indian robin",
            "The male baya weaver (weaverbird)",
            "The house sparrow",
            "The common kingfisher"
        ],
        "answer": 1,
        "explanation": "The male baya weaver bird selects sturdy blade strips of grass or palm fronds and expertly weaves them in an over-under pattern to form a secure hanging pouch nest with a downward entrance tube.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Nature's Master Architect:</strong></p>
                <p class='text-slate-300'>The male baya weaver (<em>Ploceus philippinus</em>) harvests flexible green leaves and ties loops around tree twigs. By weaving crosswise strips over and under lengthwise ribbons, it constructs a durable nesting chamber that sways safely away from predators.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (The male baya weaver)</p>
            </div>
        """
    },
    {
        "id": 2,
        "question": "What are the two intersecting sets of threads in fabric weaving called?",
        "options": [
            "Stamens and pistils",
            "Warp (tana) and weft (bana)",
            "Ribbons and shoelaces",
            "Stems and roots"
        ],
        "answer": 1,
        "explanation": "In weaving, the stationary vertical threads held under tension on a loom are called the warp (tana in Hindi), and the horizontal thread interlaced back and forth across them is called the weft (bana in Hindi).",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Loom Geometry & Terminology:</strong></p>
                <p class='text-slate-300'>Weaving is the orthogonal interlacing of two thread families: the <strong>warp</strong> (longitudinal lengthwise threads) and the <strong>weft</strong> (transverse crosswise threads carried by a shuttle).</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Warp (tana) and weft (bana))</p>
            </div>
        """
    },
    {
        "id": 3,
        "question": "How long has the tradition of handloom weaving flourished across the Indian subcontinent?",
        "options": [
            "Around 50 years",
            "Over 4,000 years, dating back to the Indus Valley Civilization",
            "Since only the 1990s",
            "Just 200 years"
        ],
        "answer": 1,
        "explanation": "Archaeological discoveries in Mohenjo-daro and Harappa prove that cotton cultivation, spinning with clay spindles, and handloom weaving have thrived in India for over 4,000 years.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Ancient Indian Textile Heritage:</strong></p>
                <p class='text-slate-300'>Textile fragments dyed with madder roots recovered from Indus Valley excavations prove that Indian weavers mastered sophisticated weaving techniques and mordant dyeing more than four millennia ago.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Over 4,000 years, dating back to the Indus Valley Civilization)</p>
            </div>
        """
    },
    {
        "id": 4,
        "question": "Which luxurious Indian weave from Tamil Nadu is renowned for pure mulberry silk, heavy gold zari threads, and contrasting temple borders?",
        "options": [
            "Kanjeevaram (Kanchipuram)",
            "Pashmina",
            "Chikankari",
            "Bandhani"
        ],
        "answer": 0,
        "explanation": "Kanjeevaram sarees from Tamil Nadu are handwoven from three-ply mulberry silk and pure metallic zari (gold/silver wrapped silk thread), celebrated for intricate temple motifs and interlocking borders.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Kanchipuram Silk Craft:</strong></p>
                <p class='text-slate-300'>Kanjeevaram weavers use the <em>Korvai</em> technique where the body and border are woven separately and locked together with remarkable tensile strength, often adorned with woven golden peacock and lotus patterns.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Kanjeevaram)</p>
            </div>
        """
    },
    {
        "id": 5,
        "question": "What is authentic Kashmiri Pashmina wool harvested from?",
        "options": [
            "The underbelly down-fleece of high-altitude Changthangi goats",
            "Synthetic polyester plastic fibres",
            "Coarse camel bristles",
            "Domestic duck feathers"
        ],
        "answer": 0,
        "explanation": "Pashmina is the ultra-fine winter undercoat combed from Changthangi (Capra hircus) goats living at freezing altitudes above 4,000 metres in Ladakh and Kashmir.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Pashmina Fleece Origin:</strong></p>
                <p class='text-slate-300'>Changthangi goats survive winter temperatures down to -40 °C by growing an ultra-soft undercoat beneath their coarse guard hair. The combed fibres measure just 12 to 15 microns in diameter—several times finer than a human hair.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (The underbelly down-fleece of high-altitude Changthangi goats)</p>
            </div>
        """
    },
    {
        "id": 6,
        "question": "What distinctive dyeing technique gives Ikat fabrics from Odisha and Gujarat their soft, feathered geometric edges?",
        "options": [
            "Tie-dyeing the yarn bundles with precision resistance bindings BEFORE weaving",
            "Painting directly onto finished garments with oil paints",
            "Dipping completed clothes into bleach buckets",
            "Spraying chemical ink through stencils"
        ],
        "answer": 0,
        "explanation": "In Ikat (such as Odisha's Bandha or Gujarat's Patola), weavers bundle warp and/or weft yarns and tie them with water-resistant ties before dyeing, aligning dyed dots on the loom into intricate feathered patterns.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Resist-Dye Precision in Ikat:</strong></p>
                <p class='text-slate-300'>Because the calculation and binding occur on bare yarn bundles before a single shuttle is thrown, the slight shift of thread tension on the loom produces the iconic feathered or blurred edge prized in world textiles.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Tie-dyeing yarn bundles with precision bindings BEFORE weaving)</p>
            </div>
        """
    },
    {
        "id": 7,
        "question": "Why does twisting cotton fibres during spinning turn a weak cloud of fluff into a strong, continuous thread?",
        "options": [
            "It glues the fibres with synthetic liquid rubber",
            "Twisting presses overlapping fibres against each other, creating interlocking surface friction",
            "It melts the cellulose into glass",
            "It turns the cotton into metallic wire"
        ],
        "answer": 1,
        "explanation": "When short fibres are drawn parallel and given a spiral twist, lateral pressure causes their microscopic ridges to interlock, generating enough surface friction to resist tension without breaking.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>The Physics of Spinning:</strong></p>
                <p class='text-slate-300'>Raw cotton fibres are only 2 to 3 cm long. Pulling and twisting them (using a spindle or wheel) converts tensile pull along the thread into compressive inward clamping force, holding the strand together purely through friction.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Twisting creates interlocking surface friction)</p>
            </div>
        """
    },
    {
        "id": 8,
        "question": "What traditional Indian handheld tool consists of a slender metal rod with a small whorl weight used for manual spinning?",
        "options": [
            "Takli (drop spindle)",
            "Chisel",
            "Hacksaw",
            "Weaving shuttle"
        ],
        "answer": 0,
        "explanation": "A takli is a simple handheld spindle consisting of a weighted disc and a thin shaft, spun between the fingers to draw and twist fibre slivers into yarn.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>The Ancient Takli:</strong></p>
                <p class='text-slate-300'>The takli is one of humanity's earliest spinning tools. The spinner twirls the spindle with one hand while drawing out raw cotton fibres with the other; inertia from the spinning whorl twists the thread continuously.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Takli (drop spindle))</p>
            </div>
        """
    },
    {
        "id": 9,
        "question": "Why did Mahatma Gandhi promote the charkha (spinning wheel) and khadi during India's freedom struggle?",
        "options": [
            "To promote reliance on imported British factory textiles",
            "As a powerful symbol of self-reliance (atmanirbhar), village empowerment, and swadeshi economic freedom",
            "Because machines were completely banned by law",
            "To make spinning mandatory for sports events"
        ],
        "answer": 1,
        "explanation": "Mahatma Gandhi championed khadi (homespun and handwoven cotton cloth) produced on village charkhas to break foreign economic dependence, revive rural livelihoods, and unite Indians under the ideal of self-reliance.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Khadi and Swadeshi:</strong></p>
                <p class='text-slate-300'>Gandhi realized that true independence required economic freedom for rural millions. By spinning daily on the charkha, people produced their own cloth, boycotted imported mill-made cloth, and dignified manual labour.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Symbol of self-reliance, village empowerment, and swadeshi freedom)</p>
            </div>
        """
    },
    {
        "id": 10,
        "question": "In classroom Activity 1 (Paper-Strip Weaving), what happens if you place all weft strips strictly over the warp strips without alternating?",
        "options": [
            "It forms a tough, rigid fabric",
            "The strips do not interlock and slide completely apart when lifted",
            "The paper turns into transparent plastic",
            "The paper strips glue themselves together"
        ],
        "answer": 1,
        "explanation": "Without the alternating 'over-under, under-over' pattern, there is no physical entrapment or friction between perpendicular strips, meaning the structure falls apart immediately.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Principle of Interlacing:</strong></p>
                <p class='text-slate-300'>Weaving requires every successive weft thread to alternate its path relative to its neighbor (Row 1: over-under; Row 2: under-over). This alternation traps each thread between its neighbors, creating mechanical coherence.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (The strips do not interlock and slide completely apart)</p>
            </div>
        """
    },

    # =========================================================================
    # Challenge 2 (Q11 to Q20): Natural Fibres, Silk Cocoon, Synthetics, Tailorbird
    # =========================================================================
    {
        "id": 11,
        "question": "Which of the following fibres is derived from a plant stalk or stem rather than a seed pod?",
        "options": [
            "Cotton",
            "Jute and Flax (Linen)",
            "Wool",
            "Silk"
        ],
        "answer": 1,
        "explanation": "Jute and flax are bast fibres harvested from the phloem tissues of plant stems through retting (soaking in water), whereas cotton grows as seed hairs inside a pod.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Plant Stem vs Seed Pod Fibres:</strong></p>
                <p class='text-slate-300'>Cotton fibres are protective cellulose hairs surrounding cotton seeds. In contrast, jute, flax (linen), and hemp are harvested by submerging bundles of plant stems in water to loosen the long bast fibres from the woody core.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Jute and Flax (Linen))</p>
            </div>
        """
    },
    {
        "id": 12,
        "question": "What is the primary chemical building block of natural plant fibres such as cotton and linen?",
        "options": [
            "Petroleum hydrocarbons",
            "Cellulose (natural plant polymer)",
            "Keratin protein",
            "Calcium carbonate"
        ],
        "answer": 1,
        "explanation": "Plant fibres are composed of cellulose, a natural polysaccharide polymer formed by chains of glucose molecules synthesized by plants.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Chemical Composition of Fibres:</strong></p>
                <p class='text-slate-300'>Cotton, linen, jute, and bamboo consist of over 85–95% cellulose. Animal fibres (wool and silk) are made of proteins (keratin and fibroin/sericin), while synthetic fibres are petroleum polymers.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Cellulose (natural plant polymer))</p>
            </div>
        """
    },
    {
        "id": 13,
        "question": "What are the four chronological stages in the life cycle of the silkworm (Bombyx mori)?",
        "options": [
            "Egg -> Adult moth -> Cocoon -> Caterpillar",
            "Egg -> Larva (caterpillar) -> Pupa (inside cocoon) -> Imago (adult silk moth)",
            "Pupa -> Egg -> Cocoon -> Caterpillar",
            "Larva -> Egg -> Adult moth -> Pupa"
        ],
        "answer": 1,
        "explanation": "The silk moth undergoes complete metamorphosis: tiny eggs hatch into voracious caterpillars feeding on mulberry leaves, which spin protective silk cocoons to pupate before emerging as adult moths.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Silkworm Metamorphosis:</strong></p>
                <p class='text-slate-300'>1. Egg: Laid by female moth.<br>2. Larva/Caterpillar: Feeds on fresh mulberry leaves for 4 to 6 weeks.<br>3. Pupa: Inside the silk cocoon spun by salivary glands.<br>4. Adult Silk Moth: Emerges to reproduce.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Egg -> Larva -> Pupa -> Imago)</p>
            </div>
        """
    },
    {
        "id": 14,
        "question": "How does a silkworm caterpillar spin its protective silk cocoon?",
        "options": [
            "By secreting liquid fibroin protein from modified salivary glands in continuous figure-8 head motions",
            "By collecting spider webs from garden branches",
            "By chewing dry twigs into paste",
            "By rolling itself in dry mulberry leaves"
        ],
        "answer": 0,
        "explanation": "The caterpillar expels two strands of liquid fibroin coated with gummy sericin from its spinneret, swinging its head in figure-8 motions. Upon air contact, the liquid solidifies into a single unbroken filament up to 1,000 metres long.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Silk Spinning Mechanism:</strong></p>
                <p class='text-slate-300'>Specialized silk glands produce fibroin protein coated with sticky sericin glue. Moving its head 300,000 times in continuous figure-8 patterns over 3 to 4 days, the caterpillar creates a warm, resilient cocoon.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Secreting liquid fibroin protein in figure-8 head motions)</p>
            </div>
        """
    },
    {
        "id": 15,
        "question": "What raw material is used to manufacture fully synthetic fibres like polyester, nylon, and acrylic?",
        "options": [
            "Petroleum crude oil and petrochemical derivatives",
            "Crushed rock salt",
            "Cow milk whey",
            "Pure river rainwater"
        ],
        "answer": 0,
        "explanation": "Synthetic fibres are non-natural polymers synthesized from petrochemical feedstocks derived from refined crude oil and natural gas.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Petrochemical Origin of Synthetics:</strong></p>
                <p class='text-slate-300'>Nylon (polyamide) and polyester (polyethylene terephthalate) are produced through industrial chemical synthesis using hydrocarbon molecules extracted from petroleum.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Petroleum crude oil and petrochemical derivatives)</p>
            </div>
        """
    },
    {
        "id": 16,
        "question": "Why is wearing synthetic clothing (such as polyester or nylon) dangerous around open kitchen flames or Diwali firecrackers?",
        "options": [
            "Synthetic fabrics freeze solid when exposed to fire",
            "Synthetic fabrics melt into hot, sticky molten plastic that adheres to human skin, causing severe deep burns",
            "Synthetics cause sudden electrical explosions",
            "They attract insects when near heat"
        ],
        "answer": 1,
        "explanation": "Unlike cotton which burns to harmless powdery ash, synthetic fibres melt at high temperatures into sticky molten plastic drops that weld to human skin, causing excruciating, deep thermal burns.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Thermal Hazard of Synthetics:</strong></p>
                <p class='text-slate-300'>Natural cotton burns cleanly without melting, making it easy to remove if ignited. Synthetic polymers melt into blazing viscous liquid that cannot be wiped off without tearing the skin underneath. Always wear 100% cotton around flames.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Melts into hot, sticky molten plastic adhering to skin)</p>
            </div>
        """
    },
    {
        "id": 17,
        "question": "Which bird acts as nature's tailor by puncturing holes along leaf margins and stitching them together into a nesting cone?",
        "options": [
            "The common tailorbird (Orthotomus sutorius)",
            "The house crow",
            "The blue rock pigeon",
            "The great Indian bustard"
        ],
        "answer": 0,
        "explanation": "The tailorbird uses its sharp, needle-like beak to punch pairs of eyelet holes along the edges of broad leaves (like mango or fig leaves) and stitches them together using plant lint and spider silk.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Nature's Living Tailor:</strong></p>
                <p class='text-slate-300'>The common tailorbird (<em>Orthotomus sutorius</em>) selects living leaves on a branch. Piercing tiny holes along the edges, it threads cotton fibres or spider silk through, forming tiny tangled knots on the outer side like rivets to create a cradle nest.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (The common tailorbird)</p>
            </div>
        """
    },
    {
        "id": 18,
        "question": "What keeps the tailorbird's thread from slipping out of the punctured leaf holes?",
        "options": [
            "The bird glues them with superglue",
            "The bird tangles and fluffs the thread ends on the outside into small knots resembling rivets",
            "The leaves heal around the thread instantly",
            "The bird holds them with its claws for three months"
        ],
        "answer": 1,
        "explanation": "The bird pulls the fibre through and pecks at the exposed ends so they unravel into little cottony balls or knots on the leaf exterior, acting like rivets or stops that prevent thread slippage.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Avian Rivet Mechanism:</strong></p>
                <p class='text-slate-300'>By deliberately fraying the fibre ends on the outside of the leaf, the tailorbird forms a natural knot or stopper that anchors the stitch under tension, creating an enclosed leafy hammock for its eggs.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Tangles thread ends into small knots resembling rivets)</p>
            </div>
        """
    },
    {
        "id": 19,
        "question": "Why are woollen clothes uniquely suited for cold winter months?",
        "options": [
            "Wool fibres are solid glass cylinders that radiate electricity",
            "Wool fibres possess natural crimps and curls that trap millions of dead-air pockets, creating a superb thermal insulator",
            "Wool absorbs all sunlight and turns blue",
            "Wool has no weight and floats in air"
        ],
        "answer": 1,
        "explanation": "The natural crimp and elasticity of sheep wool fibres create pockets of still, trapped air. Since stagnant air is a poor conductor of heat, it prevents body warmth from escaping into cold surroundings.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Thermal Insulation of Wool:</strong></p>
                <p class='text-slate-300'>Air is one of the best natural thermal insulators if prevented from circulating. The wavy, scaly structure of wool fibres holds air stationary against the skin, maintaining core body temperature during chilly winters.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Crimps and curls trap dead-air pockets as thermal insulation)</p>
            </div>
        """
    },
    {
        "id": 20,
        "question": "Which of these is a semi-synthetic fibre manufactured by chemically regenerating natural wood pulp cellulose?",
        "options": [
            "Rayon (viscose)",
            "Nylon 6,6",
            "Pure mulberry silk",
            "Polyester"
        ],
        "answer": 0,
        "explanation": "Rayon is classified as a regenerated cellulose fibre because it starts with natural plant wood pulp or bamboo, which is chemically dissolved and extruded into silky filament threads.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Regenerated Cellulose:</strong></p>
                <p class='text-slate-300'>Unlike purely synthetic fibres derived from petroleum, rayon is manufactured from renewable wood cellulose. Because its chemical backbone remains cellulose, it breathes and absorbs moisture much like cotton.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Rayon (viscose))</p>
            </div>
        """
    },

    # =========================================================================
    # Challenge 3 (Q21 to Q30): Running Stitch, Chikankari, Banjara, Kantha, Gota
    # =========================================================================
    {
        "id": 21,
        "question": "What is the most fundamental hand-stitching technique, characterized by an even 'in-and-out' needle motion along a straight line?",
        "options": [
            "Running stitch (kaccha tanka)",
            "Cross stitch",
            "Satin stitch",
            "Blanket stitch"
        ],
        "answer": 0,
        "explanation": "The running stitch is the simplest and oldest hand-sewing stitch, created by passing the needle evenly up and down through the fabric at regular intervals.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>The Fundamental Running Stitch:</strong></p>
                <p class='text-slate-300'>In Hindi termed <em>kaccha tanka</em>, the running stitch involves passing a threaded needle alternately over and under the cloth. When stitched with even tension and spacing, it creates flexible, durable seams and forms the basis of Kantha quilting.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Running stitch (kaccha tanka))</p>
            </div>
        """
    },
    {
        "id": 22,
        "question": "In classroom Activity 7 and 8, what practical everyday item can students create by joining colourful textile scraps with running stitches?",
        "options": [
            "A patchwork mat, coaster, or table runner",
            "A steel cooking spoon",
            "A glass windowpane",
            "A clay flowerpot"
        ],
        "answer": 0,
        "explanation": "Students salvage unused fabric cuttings from local tailor shops and join them edge-to-edge using running stitches to create beautiful patchwork mats, coasters, and small tote bags.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Patchwork Craft (Activities 7 & 8):</strong></p>
                <p class='text-slate-300'>Patchwork combines creativity and zero-waste discipline. By cutting leftover scraps into uniform geometric shapes (squares, triangles) and stitching them with running stitches, waste is converted into functional, durable home textiles.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (A patchwork mat, coaster, or table runner)</p>
            </div>
        """
    },
    {
        "id": 23,
        "question": "Which historic city in Uttar Pradesh is globally famous for the exquisite, delicate white-on-white embroidery known as Chikankari?",
        "options": [
            "Lucknow",
            "Agra",
            "Varanasi",
            "Kanpur"
        ],
        "answer": 0,
        "explanation": "Lucknow is the heartland of Chikankari, a refined art form involving 32 distinct stitches embroidered onto lightweight, translucent fabrics like muslin, cotton, and georgette.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Lucknow Chikankari:</strong></p>
                <p class='text-slate-300'>Patronized by the Nawabs of Awadh, Chikankari traditionally uses white untwisted cotton thread on sheer white cotton or muslin, celebrated for intricate floral creepers, paisleys, and airy jaali (net) work.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Lucknow)</p>
            </div>
        """
    },
    {
        "id": 24,
        "question": "What is the famous shadow-work herringbone stitch in Chikankari called, which is worked on the reverse side of cloth to create an opaque silhouette on the front?",
        "options": [
            "Bakhiya",
            "Murri",
            "Tepchi",
            "Phanda"
        ],
        "answer": 0,
        "explanation": "Bakhiya is the signature shadow stitch of Chikankari: worked crisscross on the reverse side of sheer muslin, it leaves a delicate faint outline on the front with a softly shaded interior.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Bakhiya (Shadow Stitch):</strong></p>
                <p class='text-slate-300'>By covering the back of the motif with dense herringbone stitches, light passing through translucent fabric shows a solid shadow surrounded by a crisp perimeter—a hallmark of authentic Lucknow craftsmanship.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Bakhiya)</p>
            </div>
        """
    },
    {
        "id": 25,
        "question": "Which nomadic community in Rajasthan and Gujarat is renowned for embedding shimmering circular mirrors (aabhla) into vibrantly embroidered textiles?",
        "options": [
            "Banjara (Lambani)",
            "Inuit",
            "Maasai",
            "Bedouin"
        ],
        "answer": 0,
        "explanation": "The Banjara (Lambani) artisans craft breathtaking embroidered garments using chain stitches, cowrie shells, coins, and tiny circular glass mirrors (shisha or aabhla) bound tightly with buttonhole stitches.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Banjara Mirror-Work Tradition:</strong></p>
                <p class='text-slate-300'>Banjara embroidery uses brilliant red, indigo, and yellow fabrics. Small reflective mirrors are encased within secure circular stitches to ward off evil spirits, reflect the fierce desert sun, and display striking tribal identity.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Banjara (Lambani))</p>
            </div>
        """
    },
    {
        "id": 26,
        "question": "How are traditional Kantha quilts in West Bengal, Odisha, and Tripura created from worn-out sarees and dhotis?",
        "options": [
            "By layering old cotton cloths together and binding them with thousands of tiny, rippling running stitches",
            "By melting the old clothes in acid",
            "By gluing them with rubber cement",
            "By painting them with oil varnish"
        ],
        "answer": 0,
        "explanation": "Kantha is a centuries-old recycling craft where women stack four to seven layers of soft, worn cotton sarees and dhotis, sewing them together with dense rows of running stitches using threads pulled from the saree borders.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>The Art and Soul of Kantha:</strong></p>
                <p class='text-slate-300'>Nothing was wasted: thread was carefully unraveled from old garment borders to stitch layered quilts (nakshi kantha). The thousands of running stitches give the quilt a warm, textured, rippling quilted feel and depict folk motifs of fish, trees, and lotus blooms.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Layering old cloths with thousands of rippling running stitches)</p>
            </div>
        """
    },
    {
        "id": 27,
        "question": "Which royal Rajasthani applique craft uses gold and silver metallic ribbons cut into diamond and petal shapes to embellish festive attire?",
        "options": [
            "Gota Patti",
            "Kashida",
            "Toda",
            "Khneng"
        ],
        "answer": 0,
        "explanation": "Gota Patti is an applique embroidery originating in Rajasthan (Jaipur, Bikaner) where narrow woven gold and silver ribbons (gota) are shaped into leaf, petal, and bird motifs and hand-stitched onto royal silks and bandhanis.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Gota Patti Applique:</strong></p>
                <p class='text-slate-300'>Artisans fold and trim the metallic ribbon into delicate teardrops (patti) and diamonds, stitching each petal down with fine thread to form flowers, peacocks, and geometrical lattices that shimmer in the sunlight.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Gota Patti)</p>
            </div>
        """
    },
    {
        "id": 28,
        "question": "What is the primary aesthetic and practical benefit of the rippling Kantha running-stitch layers?",
        "options": [
            "It traps air between the soft layers for light warmth, softens with each wash, and transforms fragile old cloths into a strong composite fabric",
            "It turns the quilt into waterproof rubber",
            "It makes the fabric heavy like concrete",
            "It bleaches the fabric completely white"
        ],
        "answer": 0,
        "explanation": "The dense grid of running stitches anchors multiple thin, soft layers into a cohesive composite textile. The tiny ripples trap warmth, and the repeated washing softens the fabric while preserving incredible strength.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Textile Engineering of Kantha:</strong></p>
                <p class='text-slate-300'>A single worn saree is weak and tearable. By quilting 4 to 6 worn layers with thousands of micro-stitches, the tension distributes across millions of contact points, giving birth to a breathable, cozy baby blanket or winter quilt.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Traps air for warmth, softens with washing, and creates a strong composite)</p>
            </div>
        """
    },
    {
        "id": 29,
        "question": "In Banjara mirror work, why are mirrors held in place with thread rather than glue?",
        "options": [
            "Interlocking buttonhole and chain stitches wrap firmly around the mirror rim, ensuring mirrors never drop off during active desert movement and washing",
            "Glue was completely unknown to mankind",
            "Thread makes the mirror grow larger",
            "Mirror edges become invisible with thread"
        ],
        "answer": 0,
        "explanation": "Traditional Banjara women engineered circular cage stitches that grip the bevelled edge of each mirror securely against the thick fabric, ensuring longevity through nomadic travels and strenuous celebrations.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Mechanical Fastening in Textiles:</strong></p>
                <p class='text-slate-300'>Glue dissolves in water and turns brittle under desert heat. By building a structural web of interlocking foundation stitches and buttonhole knots over the perimeter, the mirror is permanently trapped against the cloth.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Interlocking stitches wrap firmly around the mirror rim)</p>
            </div>
        """
    },
    {
        "id": 30,
        "question": "Why is Chikankari traditionally executed on sheer, breathable fabrics like mulmul (fine muslin)?",
        "options": [
            "Muslin provides a translucent canvas where the shadow stitches on the reverse side shine through delicately while offering sublime comfort in hot Awadh summers",
            "Thick canvas is impossible to cut with scissors",
            "Muslin glows in the dark at night",
            "Muslin repels all rain completely"
        ],
        "answer": 0,
        "explanation": "Awadh's warm climate required breezy, lightweight cottons. Sheer mulmul allowed the cooling comfort of pure cotton while highlighting the subtle interplay of light through delicate white embroidery.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>The Canvas of Awadh:</strong></p>
                <p class='text-slate-300'>The extreme fineness of Dacca and Lucknow muslin made it the perfect medium for white-on-white needlework. The contrast between opaque thread stitches and translucent base fabric creates an ethereal, royal texture.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Translucent canvas showcases shadow stitches while offering cool comfort)</p>
            </div>
        """
    },

    # =========================================================================
    # Challenge 4 (Q31 to Q40): Phulkari, Toda, Kashmiri, Khneng, Upcycling, Testing
    # =========================================================================
    {
        "id": 31,
        "question": "What is Punjab's iconic folk embroidery called, which literally translates to 'flower work' and is stitched with bright silk floss (pat) from the reverse side of handspun khaddar?",
        "options": [
            "Phulkari",
            "Kashida",
            "Toda",
            "Kantha"
        ],
        "answer": 0,
        "explanation": "Phulkari (literally 'flower work') is the traditional embroidery of Punjab, created using untwisted silk floss (pat) worked in long and short darning stitches from the reverse side of coarse khaddar cotton.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Punjab's Floral Heritage:</strong></p>
                <p class='text-slate-300'>Mothers and grandmothers in Punjab embroidered Phulkari shawls for brides. When the entire surface is covered so densely with silk floss that no base cloth is visible, it is called a <em>Bagh</em> (meaning 'garden').</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Phulkari)</p>
            </div>
        """
    },
    {
        "id": 32,
        "question": "Which indigenous pastoral community of the Nilgiri Hills in Tamil Nadu embroiders striking red-and-black geometric patterns on white cotton shawls (Poothkuli)?",
        "options": [
            "The Toda tribe",
            "The Santhal tribe",
            "The Gond tribe",
            "The Bhil tribe"
        ],
        "answer": 0,
        "explanation": "The Toda people of the Nilgiris craft Poothkuli shawls featuring bold red and black geometric bands inspired by buffalo horns, butterflies, and stars, counted thread by thread to resemble woven cloth.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Toda Pukhoor Embroidery:</strong></p>
                <p class='text-slate-300'>Toda women use a single needle and thick unspun wool/cotton thread, counting the warp and weft threads on unbleached white fabric without drawing any outlines. Sacred buffalo motifs honour their pastoral way of life.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (The Toda tribe)</p>
            </div>
        """
    },
    {
        "id": 33,
        "question": "What natural motifs are famously depicted in Kashmiri Kashida embroidery on woollen pherans and shawls?",
        "options": [
            "Chinar leaves, apple blossoms, almonds (badam/paisley), and nightingales (bulbul)",
            "Automobiles and skyscrapers",
            "Desert camels and cacti",
            "Ocean sharks and starfish"
        ],
        "answer": 0,
        "explanation": "Kashida draws direct inspiration from the paradise of Kashmir's valleys: chinar tree leaves, pine cones, saffron flowers, apple blossoms, and singing bulbuls stitched with fine single-strand thread.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Kashmiri Kashida Motifs:</strong></p>
                <p class='text-slate-300'>Using chain stitch (Aari) or satin stitch with vivid jewel tones, Kashida artists reflect Kashmir's seasonal changes—from green spring blossoms to fiery autumn maple-like chinar leaves.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Chinar leaves, apple blossoms, almonds, and nightingales)</p>
            </div>
        """
    },
    {
        "id": 34,
        "question": "Which rare fish-bone motif embroidery is practiced by Khasi women in Mustoh village, Meghalaya, using black thread on handspun Eri peace silk?",
        "options": [
            "Khneng",
            "Zardozi",
            "Bandhani",
            "Chamba Rumal"
        ],
        "answer": 0,
        "explanation": "Khneng is an endangered embroidery tradition from Mustoh village in Meghalaya, where artisans meticulously stitch fish-bone patterns along the border of Eri silk wrap-around skirts (Jainsem).",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>The Unique Khneng of Meghalaya:</strong></p>
                <p class='text-slate-300'>Khneng mimics the spine of a local river fish. It is embroidered onto handspun Eri silk—known as 'peace silk' because the moth emerges naturally from the open cocoon without boiling the pupa.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Khneng)</p>
            </div>
        """
    },
    {
        "id": 35,
        "question": "In traditional Indian households, what is the sustainable life cycle of a cotton textile garment?",
        "options": [
            "Brand new clothes -> Younger sibling hand-me-down -> Godhari quilt / rag doll -> Cleaning mop -> Composted in garden soil",
            "Worn once -> Thrown into a plastic landfill",
            "Burned immediately after two washes",
            "Buried in metal boxes underground"
        ],
        "answer": 0,
        "explanation": "Indian culture practices true circularity: good clothes pass to younger siblings; worn garments are stitched into Godhari quilts, baby wraps, or kitchen mats; remnants become mops; and 100% cotton decomposes naturally into compost.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Zero-Waste Indian Circular Economy:</strong></p>
                <p class='text-slate-300'>Indian homes maximize every thread's lifetime. From festive celebration to soft cradle cloth, quilt padding, dusters, and organic soil enrichment, zero fabric reaches municipal landfills.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (New clothes -> Hand-me-down -> Quilt -> Mop -> Compost)</p>
            </div>
        """
    },
    {
        "id": 36,
        "question": "In a laboratory flame burn test, what distinct odor and residue does pure cotton produce?",
        "options": [
            "Smells like burning paper and leaves light, fluffy grey-black ash",
            "Smells like sweet candy and turns into yellow liquid",
            "Smells like burning hair and forms a hard rock",
            "Produces no smoke and turns into green sparks"
        ],
        "answer": 0,
        "explanation": "Because cotton is composed of pure plant cellulose (the exact same chemical substance as wood pulp paper), it burns with a steady yellow flame, smells like burning paper or dry leaves, and leaves powdery grey ash.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Cotton Burn Test Signature:</strong></p>
                <p class='text-slate-300'>- Chemical: Cellulose polymer.<br>- Flame: Ignites quickly, steady glowing ember.<br>- Odour: Burning paper/wood.<br>- Residue: Soft, light grey-white ash that crumbles easily between fingers.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: A (Smells like burning paper and leaves fluffy grey ash)</p>
            </div>
        """
    },
    {
        "id": 37,
        "question": "In a flame burn test, what characteristic smell identifies natural animal fibres such as wool and silk?",
        "options": [
            "A sharp chemical plastic odor",
            "A strong smell of burning hair or feathers (due to sulfur-bearing proteins)",
            "The scent of fresh cut grass",
            "A citrus lemon smell"
        ],
        "answer": 1,
        "explanation": "Wool and silk are animal proteins (keratin and fibroin) containing sulfur amino acids. When burned, they emit a distinct singed hair or burning feather smell and leave a dark, crushable irregular bead.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Protein Fibre Burn Test:</strong></p>
                <p class='text-slate-300'>- Chemical: Keratin/Fibroin protein chains.<br>- Flame: Burns slowly, self-extinguishes away from flame.<br>- Odour: Burning hair or roasted feathers.<br>- Residue: Black, hollow, brittle bead that easily crumbles into powder.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Smell of burning hair or feathers)</p>
            </div>
        """
    },
    {
        "id": 38,
        "question": "What happens when synthetic polyester or nylon is touched by a flame during a burn test?",
        "options": [
            "It turns instantly into clean drinking water",
            "It shrinks away from the heat, melts into a dark liquid, emits black chemical smoke, and hardens into an uncrushable plastic bead",
            "It blows up like a party cracker",
            "It freezes into cold ice cubes"
        ],
        "answer": 1,
        "explanation": "Synthetic petrochemical fibres are plastics. When heated, they shrink, melt, produce pungent chemical smoke, and cool down into a hard, rigid plastic bead that cannot be crushed by finger pressure.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>Synthetic Polymer Burn Test:</strong></p>
                <p class='text-slate-300'>- Chemical: Petrochemical polymer chains.<br>- Flame: Melts and drips sticky black droplets with acidic smoke.<br>- Odour: Sweet chemical / celery-like pungent plastic odor.<br>- Residue: Hard, round, shiny uncrushable plastic bead.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Shrinks, melts, emits black smoke, and hardens into an uncrushable bead)</p>
            </div>
        """
    },
    {
        "id": 39,
        "question": "Approximately how many kilometres of continuous thread are woven together to craft an ordinary adult cotton shirt?",
        "options": [
            "Just 10 metres",
            "About 20 to 25 kilometres of fine thread",
            "Exactly 5 centimetres",
            "Over 1,000,000 kilometres"
        ],
        "answer": 1,
        "explanation": "A typical cotton shirt contains between 20 to 25 kilometres of spun yarn, representing thousands of farmer hours, spinning rotations, and loom crossings.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>The Scale of Textile Creation:</strong></p>
                <p class='text-slate-300'>If all the warp and weft yarns in your school shirt or dress were unraveled and tied end-to-end, they would stretch across 20 to 25 kilometres—connecting two nearby towns! Every garment embodies enormous human effort and natural resources.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (About 20 to 25 kilometres of fine thread)</p>
            </div>
        """
    },
    {
        "id": 40,
        "question": "What core attitude does NCERT Chapter 8 inspire students to adopt toward our clothes and the artisans who create them?",
        "options": [
            "Discard clothes after one wear to buy fast fashion",
            "Value garments as precious treasures of nature and human artistry, practice mending and upcycling, and honor our handloom artisans",
            "Replace all handloom clothes with single-use plastic wraps",
            "Never wash any clothes to save soap"
        ],
        "answer": 1,
        "explanation": "Understanding how threads are spun, woven, and embroidered teaches us deep respect for natural fibres, circular recycling traditions, and the gifted master weavers and tailors of India.",
        "solution_html": """
            <div class='space-y-2 text-xs'>
                <p><strong>The Textile Guardian Ethos:</strong></p>
                <p class='text-slate-300'>Clothes are not disposable garbage; they are crafted from nature's gifts and human genius. By learning basic stitching, caring for our clothes, mending loose buttons, and supporting Indian handlooms, students become responsible Textile Guardians.</p>
                <p class='text-emerald-400 font-bold'>Correct Option: B (Value garments as precious treasures, practice mending and upcycling, and honor artisans)</p>
            </div>
        """
    }
]

print("Mastery quiz questions defined:", len(QUIZ_QUESTIONS))

