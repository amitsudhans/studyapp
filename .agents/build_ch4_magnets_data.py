import re
import sys

def verify_no_latex(text, context=""):
    matches = re.findall(r'\\[a-zA-Z]+', text)
    if matches:
        print(f"ERROR: Raw LaTeX found in {context}: {matches[:10]}")
        sys.exit(1)

slides = [
    {
        "id": 1,
        "title": "Reshma's Story & Compass",
        "subtitle": "Maritime Navigation, Overcast Storms & The Magic of Magnets",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-indigo-500/30 shadow-lg">
        <h4 class="text-indigo-400 font-bold text-base mb-2 flex items-center gap-2">
            <span>⛵</span> Ancient Maritime Navigation
        </h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            In coastal Kerala, ancient spice traders sailed across vast oceans to Rome, Arabia, and Southeast Asia. On clear nights, sailors navigated by observing the <strong>Pole Star (Polaris)</strong> in the northern sky and constellations.
        </p>
        <p class="text-slate-300 text-sm leading-relaxed">
            During heavy monsoon storms, dense overcast clouds hid the Sun and stars completely. Sailors relied on a remarkable instrument called the <strong>magnetic compass</strong> to find directions reliably across open waters.
        </p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-amber-500/30 shadow-lg">
        <h4 class="text-amber-400 font-bold text-base mb-2 flex items-center gap-2">
            <span>🧲</span> Magnets in Everyday Life
        </h4>
        <ul class="text-slate-300 text-sm space-y-2">
            <li class="flex items-start gap-2">
                <span class="text-amber-400 font-bold">•</span>
                <span><strong>Geometry Box & Pencil Cases:</strong> Self-snapping lids stay firmly locked with hidden magnets.</span>
            </li>
            <li class="flex items-start gap-2">
                <span class="text-amber-400 font-bold">•</span>
                <span><strong>Refrigerator Doors:</strong> Magnetic rubber gaskets along the perimeter seal the cold interior air.</span>
            </li>
            <li class="flex items-start gap-2">
                <span class="text-amber-400 font-bold">•</span>
                <span><strong>Whiteboard Dusters & Handbags:</strong> Magnetic catches grip steel pins or whiteboard frames.</span>
            </li>
        </ul>
    </div>
</div>
<div class="mt-4 p-3 bg-indigo-950/40 rounded-xl border border-indigo-500/20 text-xs text-indigo-300">
    <strong>Natural vs Artificial:</strong> Ancient Greeks and shepherds discovered naturally magnetized black rock called <em>Lodestone</em> (rich in iron oxide, magnetite). Today, humans manufacture shaped artificial magnets from iron, nickel, and cobalt alloys.
</div>
""",
        "lecture_script": """Welcome to our exploration of magnets! Imagine sailing hundreds of years ago along the Arabian Sea coast of Kerala. You are guiding a merchant ship loaded with black pepper, cardamom, and cinnamon. Suddenly, monsoon clouds cover the sky. The Sun disappears, and at night, no stars or constellations are visible. How would you steer your ship safely without drifting onto rocky reefs? The answer lies in one of humanity's greatest scientific discoveries: the magnetic compass. Natural magnetic rocks called lodestones were first discovered in antiquity. People noticed that when a piece of lodestone was suspended by a thread, it always turned until one end pointed towards the northern horizon. Today, magnets are everywhere around us, from the gentle click of a pencil case lid to refrigerator gaskets, electric motors, and modern smartphones. Let us uncover the hidden invisible forces of magnetism.""",
        "spoken_text": "Slide 1: Reshma's Story and Compass. Maritime Navigation, Overcast Storms and The Magic of Magnets. Welcome to our exploration of magnets! Imagine sailing hundreds of years ago along the Arabian Sea coast of Kerala. You are guiding a merchant ship loaded with black pepper, cardamom, and cinnamon. Suddenly, monsoon clouds cover the sky. The Sun disappears, and at night, no stars or constellations are visible. How would you steer your ship safely without drifting onto rocky reefs? The answer lies in one of humanity's greatest scientific discoveries: the magnetic compass. Natural magnetic rocks called lodestones were first discovered in antiquity. People noticed that when a piece of lodestone was suspended by a thread, it always turned until one end pointed towards the northern horizon. Today, magnets are everywhere around us, from the gentle click of a pencil case lid to refrigerator gaskets, electric motors, and modern smartphones. Let us uncover the hidden invisible forces of magnetism.",
        "checkpoints": [
            {
                "question": "What celestial body did ancient sailors rely upon on clear nights before the compass?",
                "options": ["Pole Star (Polaris)", "Planet Venus", "Shooting meteors", "Halley's Comet"],
                "correct": 0,
                "explanation": "Sailors in the Northern Hemisphere tracked the fixed Pole Star (Polaris) to identify true north on clear starry nights.",
                "study_insight": "When overcast storm clouds blocked the stars, sailors depended entirely on the magnetic compass."
            },
            {
                "question": "What naturally occurring magnetic mineral was discovered in ancient times?",
                "options": ["Bauxite", "Lodestone (Magnetite)", "Limestone", "Hematite only"],
                "correct": 1,
                "explanation": "Lodestone is a naturally magnetized mineral form of iron oxide (magnetite) that acts as a natural magnet.",
                "study_insight": "Artificial magnets are manufactured today by magnetizing iron, steel, nickel, and cobalt into custom shapes."
            }
        ]
    },
    {
        "id": 2,
        "title": "Shapes of Magnets",
        "subtitle": "Bar, Horseshoe, Ring, Cylindrical & Magnetic Needles",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-3 gap-3">
    <div class="bg-slate-800/80 p-3 rounded-xl border border-sky-500/30">
        <div class="text-sky-400 font-bold text-sm mb-1">1. Bar Magnet</div>
        <p class="text-xs text-slate-300">Rectangular or square straight bar with North and South poles at opposite ends. Widely used in school laboratories.</p>
    </div>
    <div class="bg-slate-800/80 p-3 rounded-xl border border-red-500/30">
        <div class="text-red-400 font-bold text-sm mb-1">2. Horseshoe (U-Shape)</div>
        <p class="text-xs text-slate-300">Bent U-shape bringing North and South poles close together, producing an intense concentrated magnetic field between the tips.</p>
    </div>
    <div class="bg-slate-800/80 p-3 rounded-xl border border-emerald-500/30">
        <div class="text-emerald-400 font-bold text-sm mb-1">3. Ring & Disc Magnet</div>
        <p class="text-xs text-slate-300">Circular washer shape with opposite poles on the top and bottom flat faces. Found in audio speakers and electric motors.</p>
    </div>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 gap-3 mt-3">
    <div class="bg-slate-800/80 p-3 rounded-xl border border-amber-500/30">
        <div class="text-amber-400 font-bold text-sm mb-1">4. Cylindrical / Button Magnet</div>
        <p class="text-xs text-slate-300">Compact cylinder or button with poles on circular flat ends. Used in magnetic catches, toys, and whiteboards.</p>
    </div>
    <div class="bg-slate-800/80 p-3 rounded-xl border border-purple-500/30">
        <div class="text-purple-400 font-bold text-sm mb-1">5. Magnetic Compass Needle</div>
        <p class="text-xs text-slate-300">Tapered diamond-shaped slender magnet balanced on a sharp low-friction pivot point for direction finding.</p>
    </div>
</div>
""",
        "lecture_script": """Magnets come in many purposeful shapes and sizes engineered for specific technical tasks. A straight bar magnet has its two poles located at opposite extreme ends and is the classic model we study in laboratory experiments. When engineers bend a bar into a U-shape or horseshoe, both the North and South poles are brought close together. This concentrates the magnetic force lines in the narrow gap between the tips, making horseshoe magnets exceptional at lifting heavy iron weights. Circular ring and disc magnets have their opposite magnetic poles located on their flat circular faces; you find these inside loudspeakers where magnetic forces vibrate sound diaphragms. Cylindrical and tiny button magnets are used in sensors and magnetic closures, while ultra-light balanced magnetic needles pivot effortlessly inside compass dials.""",
        "spoken_text": "Slide 2: Shapes of Magnets. Bar, Horseshoe, Ring, Cylindrical and Magnetic Needles. Magnets come in many purposeful shapes and sizes engineered for specific technical tasks. A straight bar magnet has its two poles located at opposite extreme ends and is the classic model we study in laboratory experiments. When engineers bend a bar into a U-shape or horseshoe, both the North and South poles are brought close together. This concentrates the magnetic force lines in the narrow gap between the tips, making horseshoe magnets exceptional at lifting heavy iron weights. Circular ring and disc magnets have their opposite magnetic poles located on their flat circular faces; you find these inside loudspeakers where magnetic forces vibrate sound diaphragms. Cylindrical and tiny button magnets are used in sensors and magnetic closures, while ultra-light balanced magnetic needles pivot effortlessly inside compass dials.",
        "checkpoints": [
            {
                "question": "Why is a horseshoe magnet shaped in a U-curve?",
                "options": ["To make it lighter in weight", "To bring both poles close together for a stronger gap field", "To prevent it from rusting", "To eliminate the South pole"],
                "correct": 1,
                "explanation": "Bending the magnet brings North and South poles adjacent, concentrating intense magnetic attraction across the gap.",
                "study_insight": "Horseshoe magnets are commonly used in industrial lifting and electric generators."
            },
            {
                "question": "Where are the North and South poles located on a flat ring or disc magnet?",
                "options": ["On the outer curved rim", "At the inner hole center", "On opposite flat circular faces", "Ring magnets do not have poles"],
                "correct": 2,
                "explanation": "On a disc or ring magnet, one flat face acts as the North pole and the opposite flat face acts as the South pole.",
                "study_insight": "All magnets, regardless of shape, always possess exactly two opposite poles."
            }
        ]
    },
    {
        "id": 3,
        "title": "Magnetic Materials",
        "subtitle": "Iron, Nickel, Cobalt, Steel & Atomic Domain Alignment",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-emerald-500/30">
        <h4 class="text-emerald-400 font-bold text-base mb-2">Definition of Magnetic Materials</h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            Substances that experience a strong attractive pull when brought near a magnet are called <strong>magnetic materials</strong>.
        </p>
        <div class="bg-emerald-950/40 p-2.5 rounded-lg border border-emerald-500/20 text-xs text-emerald-300">
            <strong>Key Ferromagnetic Elements:</strong><br>
            • <strong>Iron (Fe):</strong> Nails, steel pins, paper clips, iron filings, window grilles.<br>
            • <strong>Nickel (Ni):</strong> Stainless steel alloys, rechargeable batteries.<br>
            • <strong>Cobalt (Co):</strong> High-strength permanent magnets, jet engine alloys.<br>
            • <strong>Steel:</strong> An alloy of iron and carbon that retains permanent magnetism.
        </div>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-sky-500/30">
        <h4 class="text-sky-400 font-bold text-base mb-2">How Magnetism Works (Microscopic View)</h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            Inside an unmagnetized iron nail, microscopic groups of atoms called <strong>magnetic domains</strong> point in random directions, canceling each other out.
        </p>
        <p class="text-slate-300 text-sm leading-relaxed">
            When an external magnet approaches, its invisible magnetic field forces these microscopic domains to swing and align in the same direction, turning the iron nail into a temporary magnet that is immediately pulled toward the magnet!
        </p>
    </div>
</div>
""",
        "lecture_script": """What makes certain materials stick firmly to a magnet while others feel completely unaffected? In scientific terms, materials that are attracted by a magnet are called magnetic materials. The primary magnetic elements found in nature are iron, nickel, and cobalt, along with alloys such as steel. When you touch an ordinary iron nail, paper clip, or sewing needle to a magnet, it jumps forward and clings tightly. Inside every iron object are billions of tiny microscopic regions called magnetic domains. Each domain behaves like a miniature atomic magnet. In a normal nail, these domains point every which way in complete chaos, canceling each other out. But the moment a strong magnet comes near, its magnetic field acts like a drill sergeant, aligning all the domains in parallel. Instantly, the nail becomes a temporary magnet and is pulled in.""",
        "spoken_text": "Slide 3: Magnetic Materials. Iron, Nickel, Cobalt, Steel and Atomic Domain Alignment. What makes certain materials stick firmly to a magnet while others feel completely unaffected? In scientific terms, materials that are attracted by a magnet are called magnetic materials. The primary magnetic elements found in nature are iron, nickel, and cobalt, along with alloys such as steel. When you touch an ordinary iron nail, paper clip, or sewing needle to a magnet, it jumps forward and clings tightly. Inside every iron object are billions of tiny microscopic regions called magnetic domains. Each domain behaves like a miniature atomic magnet. In a normal nail, these domains point every which way in complete chaos, canceling each other out. But the moment a strong magnet comes near, its magnetic field acts like a drill sergeant, aligning all the domains in parallel. Instantly, the nail becomes a temporary magnet and is pulled in.",
        "checkpoints": [
            {
                "question": "Which set of metals are all classified as magnetic materials?",
                "options": ["Aluminium, Copper, Gold", "Iron, Nickel, Cobalt", "Lead, Silver, Brass", "Zinc, Tin, Magnesium"],
                "correct": 1,
                "explanation": "Iron, nickel, and cobalt are the classic ferromagnetic metals strongly attracted to magnets.",
                "study_insight": "Common everyday steel is an alloy composed predominantly of iron, making it magnetic."
            },
            {
                "question": "What happens to the magnetic domains in an iron nail when a magnet approaches?",
                "options": ["They melt into liquid", "They align in the direction of the magnetic field", "They spin backwards and disappear", "They convert into copper"],
                "correct": 1,
                "explanation": "The external magnetic field forces randomly oriented domains to line up in parallel, causing attraction.",
                "study_insight": "When the external magnet is removed, soft iron domains randomize again, losing temporary magnetism."
            }
        ]
    },
    {
        "id": 4,
        "title": "Non-Magnetic Materials",
        "subtitle": "Wood, Plastic, Glass, Copper, Aluminium & Zero Attraction",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-rose-500/30">
        <h4 class="text-rose-400 font-bold text-base mb-2">Definition of Non-Magnetic Materials</h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            Substances that do not experience any noticeable attraction when brought into contact with a magnet are classified as <strong>non-magnetic materials</strong>.
        </p>
        <div class="bg-rose-950/40 p-2.5 rounded-lg border border-rose-500/20 text-xs text-rose-300">
            <strong>Everyday Non-Magnetic Items:</strong><br>
            • <strong>Wood:</strong> Pencils, wooden desks, matchsticks, cardboard.<br>
            • <strong>Plastics & Polymers:</strong> Rulers, pen barrels, water bottles, eraser rubber.<br>
            • <strong>Ceramics & Minerals:</strong> Glass beakers, ceramic cups, sand, clay bricks.<br>
            • <strong>Non-Magnetic Metals:</strong> Copper electrical wire, aluminium foil, brass screws, gold, pure silver.
        </div>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-amber-500/30">
        <h4 class="text-amber-400 font-bold text-base mb-2">Crucial Common Misconceptions</h4>
        <div class="space-y-3 text-xs text-slate-300">
            <div class="p-2.5 bg-slate-900/60 rounded-lg border border-slate-700">
                <strong class="text-amber-300">Myth: "All metals stick to magnets."</strong><br>
                <span class="text-slate-400">Fact: Most metals (copper, aluminium, brass, gold, silver, lead) are completely non-magnetic. Only ferromagnetic metals like iron, nickel, and cobalt stick.</span>
            </div>
            <div class="p-2.5 bg-slate-900/60 rounded-lg border border-slate-700">
                <strong class="text-amber-300">Practical Application: Scrap Metal Sorting</strong><br>
                <span class="text-slate-400">Giant electromagnets on cranes lift scrap iron and steel cars from recycling piles while aluminium cans and plastic debris remain untouched on the ground.</span>
            </div>
        </div>
    </div>
</div>
""",
        "lecture_script": """Now let us explore the other side of the material world: non-magnetic substances. When you hold a strong magnet against a wooden table, a plastic scale, a glass windowpane, or a cotton shirt, absolutely nothing happens. There is zero pull. But here is where many people make a big mistake: they assume that because an object is made of metal, it must stick to a magnet. That is completely false! Take an aluminium beverage can, a piece of copper wire, a brass key, or a gold ring. None of these metals will stick to a magnet. Their atomic structures do not possess unpaired electron spins that can form magnetic domains. In industrial recycling yards, operators use massive electromagnets suspended from cranes to separate valuable iron and steel beams instantly from mixed piles of non-magnetic aluminium cans, plastics, and glass.""",
        "spoken_text": "Slide 4: Non-Magnetic Materials. Wood, Plastic, Glass, Copper, Aluminium and Zero Attraction. Now let us explore the other side of the material world: non-magnetic substances. When you hold a strong magnet against a wooden table, a plastic scale, a glass windowpane, or a cotton shirt, absolutely nothing happens. There is zero pull. But here is where many people make a big mistake: they assume that because an object is made of metal, it must stick to a magnet. That is completely false! Take an aluminium beverage can, a piece of copper wire, a brass key, or a gold ring. None of these metals will stick to a magnet. Their atomic structures do not possess unpaired electron spins that can form magnetic domains. In industrial recycling yards, operators use massive electromagnets suspended from cranes to separate valuable iron and steel beams instantly from mixed piles of non-magnetic aluminium cans, plastics, and glass.",
        "checkpoints": [
            {
                "question": "Which of the following objects is completely non-magnetic?",
                "options": ["Steel sewing needle", "Aluminium beverage can", "Iron window hinge", "Cobalt alloy pin"],
                "correct": 1,
                "explanation": "Aluminium is a non-ferrous metal that is not attracted by magnets.",
                "study_insight": "Never assume all shiny metals are magnetic; copper, aluminium, and brass are non-magnetic."
            },
            {
                "question": "How do recycling plants separate iron scrap from aluminium and plastic trash?",
                "options": ["By dissolving them in cold water", "Using powerful industrial electromagnets", "By burning the whole pile", "Using high-speed wind fans"],
                "correct": 1,
                "explanation": "Electromagnets attract magnetic iron and steel scrap, leaving non-magnetic materials behind.",
                "study_insight": "Magnetic separation is one of the most efficient eco-friendly sorting technologies in recycling."
            }
        ]
    },
    {
        "id": 5,
        "title": "Poles of a Magnet",
        "subtitle": "Activity 4.2: Iron Filings, Maxima at Ends & Pole Definitions",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-cyan-500/30">
        <h4 class="text-cyan-400 font-bold text-base mb-2">Activity 4.2: Iron Filings Investigation</h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            Spread fine iron filings evenly across a flat white sheet of paper. Place a bar magnet into the filings and gently tap the sheet.
        </p>
        <div class="bg-cyan-950/40 p-3 rounded-lg border border-cyan-500/20 text-xs text-cyan-300 space-y-1.5">
            <div><strong>Observations:</strong></div>
            <div>• Dense, bristling clusters of filings cling firmly near the two extreme ends of the bar magnet.</div>
            <div>• Very few, if any, filings cling to the middle section of the magnet.</div>
        </div>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-indigo-500/30">
        <h4 class="text-indigo-400 font-bold text-base mb-2">Defining North & South Poles</h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            The regions near the ends of a magnet where its magnetic attractive power is strongest are called its <strong>poles</strong>.
        </p>
        <ul class="text-xs text-slate-300 space-y-2">
            <li class="flex items-start gap-2">
                <span class="text-red-400 font-bold">N</span>
                <span><strong>North Pole (N):</strong> The end of the magnet that seeks and points towards geographic north when freely suspended. Usually painted red.</span>
            </li>
            <li class="flex items-start gap-2">
                <span class="text-blue-400 font-bold">S</span>
                <span><strong>South Pole (S):</strong> The end of the magnet that points towards geographic south when freely suspended. Usually painted blue or white.</span>
            </li>
        </ul>
    </div>
</div>
""",
        "lecture_script": """Where is a magnet's power concentrated? If you take a bar magnet and roll it in a tray of fine iron filings, you witness a striking pattern. The iron filings do not coat the magnet uniformly. Instead, massive, thick, bristling clusters of filings gather tightly at both extreme ends, while the middle zone remains almost completely bare! This classic experiment demonstrates that the magnetic force is concentrated at the two extremities of the magnet. These two powerful focal regions are called the poles of the magnet. Every magnet possesses two distinct poles: a North-seeking pole, simply called the North pole, and a South-seeking pole, called the South pole. In laboratory apparatus, manufacturers often paint the North pole bright red and the South pole blue or white for easy visual identification.""",
        "spoken_text": "Slide 5: Poles of a Magnet. Activity 4.2: Iron Filings, Maxima at Ends and Pole Definitions. Where is a magnet's power concentrated? If you take a bar magnet and roll it in a tray of fine iron filings, you witness a striking pattern. The iron filings do not coat the magnet uniformly. Instead, massive, thick, bristling clusters of filings gather tightly at both extreme ends, while the middle zone remains almost completely bare! This classic experiment demonstrates that the magnetic force is concentrated at the two extremities of the magnet. These two powerful focal regions are called the poles of the magnet. Every magnet possesses two distinct poles: a North-seeking pole, simply called the North pole, and a South-seeking pole, called the South pole. In laboratory apparatus, manufacturers often paint the North pole bright red and the South pole blue or white for easy visual identification.",
        "checkpoints": [
            {
                "question": "Where on a bar magnet do the maximum iron filings cling during Activity 4.2?",
                "options": ["Exactly at the middle point", "Near the two ends (poles)", "Evenly all over the surface", "Only on the top face"],
                "correct": 1,
                "explanation": "Magnetic attraction is strongest near the ends (poles) of the magnet, so filings concentrate there.",
                "study_insight": "The center of a bar magnet exhibits near-zero external attraction."
            },
            {
                "question": "What are the two ends of any magnet called?",
                "options": ["East pole and West pole", "Positive terminal and Negative terminal", "North pole and South pole", "Top pole and Bottom pole"],
                "correct": 2,
                "explanation": "Every magnet has two opposite ends called the North pole and the South pole.",
                "study_insight": "These names originate from the directional alignment of freely suspended magnets relative to Earth."
            }
        ]
    },
    {
        "id": 6,
        "title": "Inseparable Poles",
        "subtitle": "Dipole Pairing, Breaking Magnets & The Myth of Monopoles",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-violet-500/30">
        <h4 class="text-violet-400 font-bold text-base mb-2">Can You Cut Off One Pole?</h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            Suppose you take a bar magnet with North at one end and South at the other, and cut it exactly in half with a saw. Do you get an isolated North pole and an isolated South pole?
        </p>
        <div class="bg-violet-950/40 p-3 rounded-lg border border-violet-500/20 text-xs text-violet-300">
            <strong>The Universal Law:</strong><br>
            <strong>No!</strong> The moment the bar is cut, new opposite poles instantly appear at the cut faces. You now have <strong>two complete smaller magnets</strong>, each with its own North and South pole!
        </div>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-fuchsia-500/30">
        <h4 class="text-fuchsia-400 font-bold text-base mb-2">Magnetic Dipoles Exist in Pairs</h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            Even if you crush a magnet into millions of microscopic dust grains, every single microscopic grain will still have a North pole and a South pole.
        </p>
        <p class="text-slate-300 text-sm leading-relaxed">
            In classical physics, an isolated magnetic pole (called a <strong>magnetic monopole</strong>) has never been observed in nature. <strong>Magnetic poles always exist in inseparable pairs.</strong>
        </p>
    </div>
</div>
""",
        "lecture_script": """A common question students ask is: what happens if I cut a magnet in half to separate the North pole from the South pole? Can you create a standalone North pole? The answer is a firm no! In nature, magnetic poles are completely inseparable. If you slice a bar magnet right down the middle, you do not end up with one North piece and one South piece. Instead, the freshly cut ends instantly form opposite poles. You end up with two complete smaller magnets, each possessing both a North pole and a South pole! If you cut those two pieces again, you get four complete magnets. Even if you pulverize a magnet into microscopic dust, every microscopic particle is a tiny magnetic dipole. Isolated magnetic poles, known as magnetic monopoles, do not exist in classical physics.""",
        "spoken_text": "Slide 6: Inseparable Poles. Dipole Pairing, Breaking Magnets and The Myth of Monopoles. A common question students ask is: what happens if I cut a magnet in half to separate the North pole from the South pole? Can you create a standalone North pole? The answer is a firm no! In nature, magnetic poles are completely inseparable. If you slice a bar magnet right down the middle, you do not end up with one North piece and one South piece. Instead, the freshly cut ends instantly form opposite poles. You end up with two complete smaller magnets, each possessing both a North pole and a South pole! If you cut those two pieces again, you get four complete magnets. Even if you pulverize a magnet into microscopic dust, every microscopic particle is a tiny magnetic dipole. Isolated magnetic poles, known as magnetic monopoles, do not exist in classical physics.",
        "checkpoints": [
            {
                "question": "What happens when you break a bar magnet in half?",
                "options": ["Both halves lose all magnetism permanently", "You get one North pole piece and one South pole piece", "You get two complete smaller magnets, each with North and South poles", "The magnet explodes into sparks"],
                "correct": 2,
                "explanation": "Breaking a magnet produces two complete magnets, each developing new opposite poles at the break.",
                "study_insight": "Magnetic poles always exist in inseparable pairs (dipoles)."
            },
            {
                "question": "Does an isolated magnetic monopole (a single North or South pole alone) exist in nature?",
                "options": ["Yes, inside batteries", "No, magnetic poles always exist in pairs", "Yes, in horseshoe magnets", "Only at the South pole"],
                "correct": 1,
                "explanation": "Single isolated magnetic poles do not exist; every magnet has both North and South poles.",
                "study_insight": "This is a fundamental law of classical electromagnetism."
            }
        ]
    },
    {
        "id": 7,
        "title": "Freely Suspended Magnet",
        "subtitle": "Activity 4.3: Thread Suspension & North-South Alignment",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-teal-500/30">
        <h4 class="text-teal-400 font-bold text-base mb-2">Activity 4.3: Thread Suspension</h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            Tie a piece of thread around the exact middle of a bar magnet and suspend it horizontally from a wooden stand in a draft-free room.
        </p>
        <div class="bg-teal-950/40 p-3 rounded-lg border border-teal-500/20 text-xs text-teal-300 space-y-1">
            <div>1. Gently disturb the magnet by rotating it in any random direction.</div>
            <div>2. Let it oscillate freely until it comes to rest.</div>
            <div>3. Mark the line along which it settles on the table below.</div>
            <div>4. Repeat several times: <strong>It consistently settles along the exact same North-South line!</strong></div>
        </div>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-amber-500/30">
        <h4 class="text-amber-400 font-bold text-base mb-2">The Directive Property of Magnets</h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            This remarkable natural behavior is known as the <strong>directive property</strong> of magnets.
        </p>
        <p class="text-slate-300 text-sm leading-relaxed">
            An ordinary wooden stick, glass rod, or non-magnetic metal bar suspended by a thread will come to rest in any random direction. Only a magnet feels an unseen cosmic torque that re-aligns it with our planet's geographic poles.
        </p>
    </div>
</div>
""",
        "lecture_script": """Let us perform one of the most elegant experiments in science: Activity 4.3. Take a bar magnet and tie a thin silk thread around its center of gravity. Hang it horizontally from a wooden stand so it can rotate freely without friction or air drafts. Now spin the magnet gently and step back. The magnet slowly oscillates back and forth and eventually comes to rest. If you check with the morning Sun, one end points toward the North and the other toward the South. Now rotate it toward the East or West and release it. Amazingly, it swings right back to the exact same North-South orientation! No matter how many times you spin it, a freely suspended magnet always seeks the North-South direction. This is called the directive property of magnets, and it is the foundation of all terrestrial navigation.""",
        "spoken_text": "Slide 7: Freely Suspended Magnet. Activity 4.3: Thread Suspension and North-South Alignment. Let us perform one of the most elegant experiments in science: Activity 4.3. Take a bar magnet and tie a thin silk thread around its center of gravity. Hang it horizontally from a wooden stand so it can rotate freely without friction or air drafts. Now spin the magnet gently and step back. The magnet slowly oscillates back and forth and eventually comes to rest. If you check with the morning Sun, one end points toward the North and the other toward the South. Now rotate it toward the East or West and release it. Amazingly, it swings right back to the exact same North-South orientation! No matter how many times you spin it, a freely suspended magnet always seeks the North-South direction. This is called the directive property of magnets, and it is the foundation of all terrestrial navigation.",
        "checkpoints": [
            {
                "question": "In which direction does a freely suspended bar magnet always settle at rest?",
                "options": ["East-West direction", "North-South direction", "Randomly every time", "Pointing directly up towards the sky"],
                "correct": 1,
                "explanation": "A freely suspended magnet always aligns itself along the geographic North-South direction.",
                "study_insight": "This directional behavior is known as the directive property of magnets."
            },
            {
                "question": "What happens if you suspend an unmagnetized wooden stick with a thread?",
                "options": ["It always points North-South", "It comes to rest in any random direction", "It starts spinning indefinitely", "It points to the Sun"],
                "correct": 1,
                "explanation": "Non-magnetic materials do not experience Earth's magnetic torque and settle in random directions.",
                "study_insight": "Only magnetized objects demonstrate the directive North-South alignment."
            }
        ]
    },
    {
        "id": 8,
        "title": "Earth as a Giant Magnet",
        "subtitle": "Geomagnetism, Molten Iron Dynamo & Magnetic Polarity",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-blue-500/30">
        <h4 class="text-blue-400 font-bold text-base mb-2">Why Does a Magnet Align North-South?</h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            A suspended magnet aligns North-South because our planet <strong>Earth itself acts as an enormous natural bar magnet!</strong>
        </p>
        <p class="text-slate-300 text-sm leading-relaxed">
            Deep beneath our feet in the Earth's outer core, swirling currents of molten iron and nickel generate a massive planetary magnetic field called the <strong>geomagnetic field</strong>.
        </p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-emerald-500/30">
        <h4 class="text-emerald-400 font-bold text-base mb-2">The Magnetic Polarity Paradox</h4>
        <div class="p-3 bg-emerald-950/40 rounded-lg border border-emerald-500/20 text-xs text-emerald-300 space-y-2">
            <div>
                <strong>The Law of Attraction:</strong> Unlike poles attract. A magnet's North pole can only be attracted by a magnetic South pole.
            </div>
            <div>
                <strong>The Scientific Truth:</strong> Near Earth's geographic North Pole lies the <strong>Earth's magnetic South pole</strong>!
            </div>
            <div>
                Therefore, our magnet's North-seeking pole points toward geographic North because it is magnetically attracted to Earth's internal magnetic South pole.
            </div>
        </div>
    </div>
</div>
""",
        "lecture_script": """Why does a freely suspended magnet always point North-South? Is there some magical force in the air? In the year 1600, English scientist William Gilbert proposed a revolutionary answer: the Earth itself is a gigantic magnet! Thousands of kilometers beneath the crust, Earth has a churning core of liquid molten iron and nickel. As the planet spins, these circulating liquid metals act like a colossal electrical generator, creating a vast planetary magnetic field. Now, think about the fundamental law of magnetism: opposite poles attract! If the North pole of your pocket compass needle points towards the Arctic in the north, what kind of magnetic pole must reside up there inside the Earth? It must be a magnetic South pole! That is why the North-seeking pole of our compass is pulled toward geographic North.""",
        "spoken_text": "Slide 8: Earth as a Giant Magnet. Geomagnetism, Molten Iron Dynamo and Magnetic Polarity. Why does a freely suspended magnet always point North-South? Is there some magical force in the air? In the year 1600, English scientist William Gilbert proposed a revolutionary answer: the Earth itself is a gigantic magnet! Thousands of kilometers beneath the crust, Earth has a churning core of liquid molten iron and nickel. As the planet spins, these circulating liquid metals act like a colossal electrical generator, creating a vast planetary magnetic field. Now, think about the fundamental law of magnetism: opposite poles attract! If the North pole of your pocket compass needle points towards the Arctic in the north, what kind of magnetic pole must reside up there inside the Earth? It must be a magnetic South pole! That is why the North-seeking pole of our compass is pulled toward geographic North.",
        "checkpoints": [
            {
                "question": "What causes Earth to behave like a giant magnet?",
                "options": ["A giant steel bar buried by astronauts", "Circulating molten iron and nickel currents in Earth's outer core", "Lightning strikes in clouds", "The ocean tides"],
                "correct": 1,
                "explanation": "Convection currents of molten iron and nickel in Earth's outer core generate Earth's geomagnetic field (geodynamo).",
                "study_insight": "Earth's magnetic field extends thousands of kilometers into space, forming the magnetosphere."
            },
            {
                "question": "What magnetic pole of Earth's internal magnet lies near the geographic North Pole?",
                "options": ["Earth's magnetic North pole", "Earth's magnetic South pole", "Earth has no internal poles", "Earth's magnetic West pole"],
                "correct": 1,
                "explanation": "Because opposite poles attract, the North pole of a compass is attracted to Earth's magnetic South pole situated near geographic north.",
                "study_insight": "Compass North points to geographic North because Earth's magnetic polarity is inverted."
            }
        ]
    },
    {
        "id": 9,
        "title": "The Magnetic Compass",
        "subtitle": "Pivot Bearing, Cardinal Dial, Brass Casing & Glass Cover",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-sky-500/30">
        <h4 class="text-sky-400 font-bold text-base mb-2">Anatomy of a Compass</h4>
        <ul class="text-xs text-slate-300 space-y-2">
            <li class="flex items-start gap-2">
                <span class="text-sky-400 font-bold">•</span>
                <span><strong>Magnetic Needle:</strong> Slender, lightweight magnetized steel needle balanced on a sharp pin.</span>
            </li>
            <li class="flex items-start gap-2">
                <span class="text-sky-400 font-bold">•</span>
                <span><strong>Jewel / Agate Bearing:</strong> Ultra-low friction pivot allowing the needle to spin freely.</span>
            </li>
            <li class="flex items-start gap-2">
                <span class="text-sky-400 font-bold">•</span>
                <span><strong>Non-Magnetic Case:</strong> Housing made of brass, aluminium, or plastic so it does not interfere with the needle.</span>
            </li>
            <li class="flex items-start gap-2">
                <span class="text-sky-400 font-bold">•</span>
                <span><strong>Graduated Dial:</strong> 360-degree face marked with cardinal directions: North (N), South (S), East (E), and West (W).</span>
            </li>
        </ul>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-emerald-500/30">
        <h4 class="text-emerald-400 font-bold text-base mb-2">How to Use a Compass in the Field</h4>
        <div class="p-3 bg-emerald-950/40 rounded-lg border border-emerald-500/20 text-xs text-emerald-300 space-y-2">
            <div>1. Place the compass flat on horizontal ground, well away from iron objects or mobile phones.</div>
            <div>2. Wait for the needle to stop swinging and settle along North-South.</div>
            <div>3. Gently rotate the circular compass case until the 'N' mark on the dial aligns directly beneath the red-painted tip of the needle.</div>
            <div>4. You can now read all directions (East, West, South) accurately!</div>
        </div>
    </div>
</div>
""",
        "lecture_script": """Carrying a delicate bar magnet dangling on a thread through ocean waves or forest trails is clumsy and impractical. To make the directive property truly portable, engineers invented the magnetic compass. A compass consists of a small circular box, typically crafted from non-magnetic brass, aluminium, or plastic, with a transparent glass lid. Inside, a tiny, ultra-light magnetized steel needle is balanced on a sharp jewel bearing that allows it to spin with practically zero friction. One end of the needle—the North-seeking end—is painted bright red. Underneath the needle is a circular dial marked with the cardinal directions: North, South, East, and West. To use it, you place it on a flat surface, let the needle settle, and gently turn the casing until the dial's 'N' lines up with the red needle. Instantly, all directions are revealed!""",
        "spoken_text": "Slide 9: The Magnetic Compass. Pivot Bearing, Cardinal Dial, Brass Casing and Glass Cover. Carrying a delicate bar magnet dangling on a thread through ocean waves or forest trails is clumsy and impractical. To make the directive property truly portable, engineers invented the magnetic compass. A compass consists of a small circular box, typically crafted from non-magnetic brass, aluminium, or plastic, with a transparent glass lid. Inside, a tiny, ultra-light magnetized steel needle is balanced on a sharp jewel bearing that allows it to spin with practically zero friction. One end of the needle—the North-seeking end—is painted bright red. Underneath the needle is a circular dial marked with the cardinal directions: North, South, East, and West. To use it, you place it on a flat surface, let the needle settle, and gently turn the casing until the dial's 'N' lines up with the red needle. Instantly, all directions are revealed!",
        "checkpoints": [
            {
                "question": "Why is the casing of a magnetic compass made of brass, aluminium, or plastic rather than iron?",
                "options": ["Iron is too expensive", "Iron is magnetic and would attract and deflect the needle", "Plastic is transparent to sound", "Aluminium makes the needle heavier"],
                "correct": 1,
                "explanation": "If the case were iron, its magnetism would interfere with and distort the needle's alignment.",
                "study_insight": "Compass housings must always be manufactured from non-magnetic materials."
            },
            {
                "question": "Which end of the compass needle is traditionally painted red?",
                "options": ["The South-seeking end", "The North-seeking end", "The East-pointing end", "The bottom pivot"],
                "correct": 1,
                "explanation": "The North-seeking tip of the compass needle is painted red for quick, unmistakable identification.",
                "study_insight": "Once the red tip points North, rotating the dial aligns East at 90 degrees and South at 180 degrees."
            }
        ]
    },
    {
        "id": 10,
        "title": "Ancient Matsya-Yantra",
        "subtitle": "Maritime Heritage: The Floating Iron Fish Compass of Ancient India",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-amber-500/30">
        <h4 class="text-amber-400 font-bold text-base mb-2 flex items-center gap-2">
            <span>🐟</span> The Matsya-Yantra (Machchh-Yantra)
        </h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            Centuries before modern dry-pivot compasses became widespread, ancient Indian navigators and mariners engineered an ingenious aquatic compass known as the <strong>Matsya-Yantra</strong> (fish machine).
        </p>
        <p class="text-slate-300 text-sm leading-relaxed">
            A thin piece of iron was shaped like a fish, magnetized by stroking with lodestone, and placed gently upon the surface of oil or water in a brass vessel.
        </p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-indigo-500/30">
        <h4 class="text-indigo-400 font-bold text-base mb-2 flex items-center gap-2">
            <span>🌊</span> Scientific Ingenuity of Oil Flotation
        </h4>
        <div class="space-y-2 text-xs text-slate-300">
            <div class="p-2.5 bg-slate-900/60 rounded-lg border border-slate-700">
                <strong class="text-indigo-300">Frictionless Floating:</strong><br>
                Surface tension and the fluid oil film allowed the iron fish to rotate horizontally with virtually zero mechanical friction.
            </div>
            <div class="p-2.5 bg-slate-900/60 rounded-lg border border-slate-700">
                <strong class="text-indigo-300">Damping Wave Shock:</strong><br>
                Oil is more viscous than water. When ocean waves rocked the ship, the thick oil prevented the fish from violently wobbling, giving steady directional readings.
            </div>
        </div>
    </div>
</div>
""",
        "lecture_script": """India's ancient maritime heritage was profoundly technologically advanced. Indian shipbuilders and master navigators sailing the Indian Ocean, Bay of Bengal, and Arabian Sea used a legendary instrument called the Matsya-Yantra, or Machchh-Yantra, which translates to 'fish instrument'. Historical Sanskrit texts document this brilliant design: an iron sheet was cut into the silhouette of a fish and carefully magnetized using a natural lodestone. This magnetized fish was then placed inside a brass vessel filled with oil. Because oil has greater viscosity than water, it damped out the tremors and swaying caused by rolling ocean waves. Supported by surface tension and buoyancy, the iron fish floated horizontally and turned automatically until its head pointed North. This ancient Indian invention guided spice ships across thousands of miles of uncharted waters.""",
        "spoken_text": "Slide 10: Ancient Matsya-Yantra. Maritime Heritage: The Floating Iron Fish Compass of Ancient India. India's ancient maritime heritage was profoundly technologically advanced. Indian shipbuilders and master navigators sailing the Indian Ocean, Bay of Bengal, and Arabian Sea used a legendary instrument called the Matsya-Yantra, or Machchh-Yantra, which translates to fish instrument. Historical Sanskrit texts document this brilliant design: an iron sheet was cut into the silhouette of a fish and carefully magnetized using a natural lodestone. This magnetized fish was then placed inside a brass vessel filled with oil. Because oil has greater viscosity than water, it damped out the tremors and swaying caused by rolling ocean waves. Supported by surface tension and buoyancy, the iron fish floated horizontally and turned automatically until its head pointed North. This ancient Indian invention guided spice ships across thousands of miles of uncharted waters.",
        "checkpoints": [
            {
                "question": "What was the ancient Indian maritime compass device called?",
                "options": ["Surya-Yantra", "Matsya-Yantra (Machchh-Yantra)", "Vayu-Chakra", "Agni-Stambha"],
                "correct": 1,
                "explanation": "Matsya-Yantra was an ancient Indian navigational compass consisting of a magnetized iron fish floating in oil.",
                "study_insight": "The fish-shaped iron magnetized pointer pointed reliably toward the North."
            },
            {
                "question": "Why did ancient mariners float the magnetized fish in oil rather than pure water?",
                "options": ["Oil is heavier than lead", "Oil's viscosity helps damp down swaying caused by ocean waves", "Water makes iron lose magnetism instantly", "Oil turns the fish golden"],
                "correct": 1,
                "explanation": "The viscosity of oil prevented erratic needle oscillation when the ship rocked in ocean swells.",
                "study_insight": "Viscous damping is still used today in precision aircraft compasses and compass capsules."
            }
        ]
    },
    {
        "id": 11,
        "title": "Making a Magnet",
        "subtitle": "Activity 4.4: Single-Touch Stroking Method & DIY Cork Compass",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-emerald-500/30">
        <h4 class="text-emerald-400 font-bold text-base mb-2">Step-by-Step Stroking Method</h4>
        <div class="text-xs text-slate-300 space-y-2">
            <div>1. Place an unmagnetized iron sewing needle or nail flat on a wooden table.</div>
            <div>2. Take a bar magnet and place one of its poles (say North) at one end of the needle.</div>
            <div>3. <strong>Stroke the needle</strong> along its entire length to the opposite end without lifting.</div>
            <div>4. Lift the magnet into the air, bring the same pole back to the starting point, and stroke again.</div>
            <div>5. Repeat this unidirectional motion <strong>30 to 40 times</strong> in the exact same direction!</div>
        </div>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-amber-500/30">
        <h4 class="text-amber-400 font-bold text-base mb-2">DIY Cork Water Compass</h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            Push the newly magnetized needle through a small slice of cork or foam. Float the cork in a wide bowl of water.
        </p>
        <div class="p-2.5 bg-amber-950/40 rounded-lg border border-amber-500/20 text-xs text-amber-300">
            <strong>Result:</strong> The cork rotates smoothly on the water's surface until the needle aligns North-South. You have built a functional DIY magnetic compass!
        </div>
    </div>
</div>
""",
        "lecture_script": """Did you know you can create your own magnet at home in just two minutes? Let us explore Activity 4.4: the single-touch stroking method. Place an unmagnetized steel sewing needle on a wooden table. Take a bar magnet and rest one pole—say the North pole—at one end of the needle. Now, press firmly and stroke the magnet all the way along the needle to the other tip. When you reach the end, lift the magnet high off the needle, bring it back through the air to the starting end, and stroke it again. Never rub back and forth like an eraser! You must stroke in one single direction 30 to 40 times. Each stroke pulls the microscopic magnetic domains inside the steel into parallel alignment. Once magnetized, push the needle through a thin slice of cork and float it in a bowl of water. Watch the cork spin until the needle proudly points North-South!""",
        "spoken_text": "Slide 11: Making a Magnet. Activity 4.4: Single-Touch Stroking Method and DIY Cork Compass. Did you know you can create your own magnet at home in just two minutes? Let us explore Activity 4.4: the single-touch stroking method. Place an unmagnetized steel sewing needle on a wooden table. Take a bar magnet and rest one pole—say the North pole—at one end of the needle. Now, press firmly and stroke the magnet all the way along the needle to the other tip. When you reach the end, lift the magnet high off the needle, bring it back through the air to the starting end, and stroke it again. Never rub back and forth like an eraser! You must stroke in one single direction 30 to 40 times. Each stroke pulls the microscopic magnetic domains inside the steel into parallel alignment. Once magnetized, push the needle through a thin slice of cork and float it in a bowl of water. Watch the cork spin until the needle proudly points North-South!",
        "checkpoints": [
            {
                "question": "What is the critical rule when magnetizing an iron needle using the single-touch method?",
                "options": ["Rub back and forth vigorously like an eraser", "Stroke only in one single direction and lift at the end", "Heat the needle red-hot over a flame first", "Dip the needle in salt water"],
                "correct": 1,
                "explanation": "Stroking in one direction aligns domains; rubbing back and forth scrambles them, destroying magnetism.",
                "study_insight": "Lifting the magnet away at the end of each stroke prevents reverse domain randomization."
            },
            {
                "question": "Why is a slice of cork used to float the magnetized needle in water?",
                "options": ["Cork is magnetic", "Cork floats and provides near-frictionless rotation on water", "Cork turns into iron", "Cork attracts South poles"],
                "correct": 1,
                "explanation": "Lightweight cork floats easily, allowing the magnetized needle to pivot with minimal water resistance.",
                "study_insight": "This setup mimics the ancient floating compass mechanism."
            }
        ]
    },
    {
        "id": 12,
        "title": "Attraction & Repulsion",
        "subtitle": "Activity 4.5: Pencil Rollers & The Fundamental Law of Poles",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-indigo-500/30">
        <h4 class="text-indigo-400 font-bold text-base mb-2">Activity 4.5: Low-Friction Pencil Rollers</h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            Place three round wooden pencils side by side on a smooth table. Rest a bar magnet horizontally across the pencils so it can roll back and forth with minimal friction.
        </p>
        <p class="text-slate-300 text-sm leading-relaxed">
            Bring a second bar magnet close to one end of the resting magnet without touching it, and observe the invisible magnetic forces at work.
        </p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-rose-500/30">
        <h4 class="text-rose-400 font-bold text-base mb-2">The Fundamental Law of Magnetic Poles</h4>
        <div class="space-y-2 text-xs text-slate-300">
            <div class="p-2.5 bg-emerald-950/40 rounded-lg border border-emerald-500/30">
                <strong class="text-emerald-400 font-bold">1. Unlike Poles Attract:</strong><br>
                When North faces South (N → S) or South faces North (S → N), a strong invisible pulling force draws the magnets together.
            </div>
            <div class="p-2.5 bg-rose-950/40 rounded-lg border border-rose-500/30">
                <strong class="text-rose-400 font-bold">2. Like Poles Repel:</strong><br>
                When North faces North (N → N) or South faces South (S → S), an invisible pushing force drives the magnets apart!
            </div>
        </div>
    </div>
</div>
""",
        "lecture_script": """What happens when two magnets interact directly? In Activity 4.5, we place a bar magnet on a bed of three round pencils acting as frictionless rollers. When you bring another bar magnet close, something extraordinary happens before they even touch. If you bring a North pole near a South pole, the roller magnet rolls eagerly toward your hand. Unlike poles attract each other! But now, flip your hand magnet around so its North pole faces the North pole on the pencils. Instantly, an invisible wall of repulsion pushes the roller magnet backward! Like poles repel each other. This is the fundamental law of magnetic poles: opposite poles pull together with attraction, while identical poles push apart with repulsion.""",
        "spoken_text": "Slide 12: Attraction and Repulsion. Activity 4.5: Pencil Rollers and The Fundamental Law of Poles. What happens when two magnets interact directly? In Activity 4.5, we place a bar magnet on a bed of three round pencils acting as frictionless rollers. When you bring another bar magnet close, something extraordinary happens before they even touch. If you bring a North pole near a South pole, the roller magnet rolls eagerly toward your hand. Unlike poles attract each other! But now, flip your hand magnet around so its North pole faces the North pole on the pencils. Instantly, an invisible wall of repulsion pushes the roller magnet backward! Like poles repel each other. This is the fundamental law of magnetic poles: opposite poles pull together with attraction, while identical poles push apart with repulsion.",
        "checkpoints": [
            {
                "question": "What happens when the North pole of one magnet is brought near the North pole of another magnet?",
                "options": ["They attract tightly", "They repel each other and push away", "They turn into non-magnetic wood", "They create water"],
                "correct": 1,
                "explanation": "Like magnetic poles (North and North, or South and South) always repel each other.",
                "study_insight": "Opposite or unlike poles (North and South) attract each other."
            },
            {
                "question": "Which combination of magnetic poles produces an attractive pulling force?",
                "options": ["North and North", "South and South", "North and South", "Both B and C"],
                "correct": 2,
                "explanation": "Unlike poles (North and South) attract each other.",
                "study_insight": "Remember: Opposites attract, likes repel."
            }
        ]
    },
    {
        "id": 13,
        "title": "Repulsion: The Sure Test",
        "subtitle": "Distinguishing True Magnets from Unmagnetized Iron Bars",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-amber-500/30">
        <h4 class="text-amber-400 font-bold text-base mb-2">The Mystery: Two Identical Bars</h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            Imagine you are handed two identical-looking shiny metal bars: <strong>Bar A</strong> and <strong>Bar B</strong>. One is a permanent magnet, and the other is an ordinary unmagnetized iron bar.
        </p>
        <p class="text-slate-300 text-sm leading-relaxed">
            How can you determine with 100% scientific certainty which one is the real magnet using a known test magnet?
        </p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-indigo-500/30">
        <h4 class="text-indigo-400 font-bold text-base mb-2">Why Repulsion is the Only Sure Test</h4>
        <div class="p-3 bg-indigo-950/40 rounded-lg border border-indigo-500/20 text-xs text-indigo-300 space-y-2">
            <div>
                <strong>The Trap of Attraction:</strong> A magnet attracts both opposite magnetic poles AND unmagnetized iron bars. Both ends of an iron bar will stick to a magnet!
            </div>
            <div>
                <strong>The Decisive Test:</strong> Bring one pole of your known magnet to both ends of the test bar. If either end is pushed away (repelled), the test bar <strong>must be a magnet</strong>!
            </div>
            <div>
                <strong>Conclusion:</strong> <em>Repulsion is the surest test for magnetism.</em>
            </div>
        </div>
    </div>
</div>
""",
        "lecture_script": """Here is a classic puzzle that every budding scientist should master. Suppose someone hands you two identical steel rods with no labels. One is a powerful magnet, and the other is just an unmagnetized iron rod. Can you identify the magnet simply by seeing if they attract? No, you cannot! A magnet attracts an unmagnetized iron bar no matter which end you touch. If you bring the North pole of a test magnet to an unmagnetized iron bar, it attracts. If you bring the South pole to the other end, it still attracts! An unmagnetized bar is always attracted. But what happens if the object is another magnet? When like poles face each other, they experience repulsion. Only a magnet has like poles that can push another magnet away. That is why science teaches us that repulsion, and never attraction, is the only sure test of magnetism!""",
        "spoken_text": "Slide 13: Repulsion: The Sure Test. Distinguishing True Magnets from Unmagnetized Iron Bars. Here is a classic puzzle that every budding scientist should master. Suppose someone hands you two identical steel rods with no labels. One is a powerful magnet, and the other is just an unmagnetized iron rod. Can you identify the magnet simply by seeing if they attract? No, you cannot! A magnet attracts an unmagnetized iron bar no matter which end you touch. If you bring the North pole of a test magnet to an unmagnetized iron bar, it attracts. If you bring the South pole to the other end, it still attracts! An unmagnetized bar is always attracted. But what happens if the object is another magnet? When like poles face each other, they experience repulsion. Only a magnet has like poles that can push another magnet away. That is why science teaches us that repulsion, and never attraction, is the only sure test of magnetism!",
        "checkpoints": [
            {
                "question": "Why is repulsion, rather than attraction, considered the only sure test of magnetism?",
                "options": ["Attraction only works in water", "A magnet attracts both opposite poles and unmagnetized iron, but only repels another magnet", "Repulsion creates sound waves", "Iron bars cannot be touched"],
                "correct": 1,
                "explanation": "Because a magnet attracts unmagnetized iron at both ends, attraction cannot prove an object is a magnet. Only another magnet can experience repulsion.",
                "study_insight": "If both ends of a metal bar are attracted to a magnet, the bar is plain iron, not a magnet."
            },
            {
                "question": "If end 1 of Bar X attracts the North pole of a magnet, and end 2 of Bar X also attracts the North pole, what is Bar X?",
                "options": ["A strong permanent magnet", "An unmagnetized magnetic material (like soft iron)", "A piece of wood", "A compass needle"],
                "correct": 1,
                "explanation": "Since both ends attract the same pole without any repulsion, Bar X is an unmagnetized piece of magnetic material.",
                "study_insight": "A true magnet would repel from one end when exposed to the same pole."
            }
        ]
    },
    {
        "id": 14,
        "title": "Action Through Barriers",
        "subtitle": "Activities 4.6 & 4.7: Penetration of Paper, Glass, Wood & Water",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-teal-500/30">
        <h4 class="text-teal-400 font-bold text-base mb-2">Penetrating Solid Barriers</h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            Place a steel paper clip on top of a sheet of cardboard, a wooden board, or a glass plate. Hold a strong bar magnet underneath.
        </p>
        <p class="text-slate-300 text-sm leading-relaxed">
            As you slide the magnet underneath, the paper clip mirrors every movement above the barrier! Magnetic field lines pass completely through non-magnetic solids.
        </p>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-sky-500/30">
        <h4 class="text-sky-400 font-bold text-base mb-2">Magnetic Attraction Through Water</h4>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            Drop several steel pins into a glass tumbler filled with water. How can you retrieve them without getting your fingers wet?
        </p>
        <div class="p-3 bg-sky-950/40 rounded-lg border border-sky-500/20 text-xs text-sky-300">
            <strong>The Water Trick:</strong> Press a strong magnet against the outside glass wall and slide it upwards. The pins stick to the inner glass wall through the water and slide right out to the rim!
        </div>
    </div>
</div>
""",
        "lecture_script": """Does magnetism require direct physical contact? In Activities 4.6 and 4.7, we discover that magnetic forces easily pass through non-magnetic barriers. If you place a steel paper clip on a thick piece of cardboard, plywood, or glass and hold a magnet underneath, the paper clip locks onto the magnet's invisible field. As you slide the magnet below, the paper clip dances across the top surface as if by telekinesis! You can even drop iron pins into a glass of water, press a magnet against the outside of the glass, and drag the pins straight up to the rim without wetting a single finger. Magnetic force fields penetrate paper, plastic, wood, glass, air, and water without being blocked.""",
        "spoken_text": "Slide 14: Action Through Barriers. Activities 4.6 and 4.7: Penetration of Paper, Glass, Wood and Water. Does magnetism require direct physical contact? In Activities 4.6 and 4.7, we discover that magnetic forces easily pass through non-magnetic barriers. If you place a steel paper clip on a thick piece of cardboard, plywood, or glass and hold a magnet underneath, the paper clip locks onto the magnet's invisible field. As you slide the magnet below, the paper clip dances across the top surface as if by telekinesis! You can even drop iron pins into a glass of water, press a magnet against the outside of the glass, and drag the pins straight up to the rim without wetting a single finger. Magnetic force fields penetrate paper, plastic, wood, glass, air, and water without being blocked.",
        "checkpoints": [
            {
                "question": "Can magnetic force act through a sheet of cardboard, glass, or plastic?",
                "options": ["No, all solids block magnetism completely", "Yes, magnetic fields pass easily through non-magnetic materials", "Only if the cardboard is soaked in acid", "Only during thunderstorms"],
                "correct": 1,
                "explanation": "Magnetic field lines penetrate non-magnetic substances such as paper, cardboard, glass, plastic, and water.",
                "study_insight": "This non-contact force enables magnetic stirrers and sealed aquarium cleaners."
            },
            {
                "question": "How can you retrieve iron pins dropped in a glass of water without touching the water?",
                "options": ["Blow into the glass with a straw", "Slide a strong magnet along the outside glass wall to pull the pins up", "Freeze the glass instantly", "Shine a flashlight into the water"],
                "correct": 1,
                "explanation": "The magnet's field acts through the glass and water, pulling pins along the inside wall to the rim.",
                "study_insight": "Magnetic force is an action-at-a-distance non-contact field force."
            }
        ]
    },
    {
        "id": 15,
        "title": "Care & Storage of Magnets",
        "subtitle": "Demagnetization Triggers, Soft Iron Keepers & Wooden Spacers",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="bg-slate-800/80 p-4 rounded-xl border border-rose-500/30">
        <h4 class="text-rose-400 font-bold text-base mb-2">How Magnets Lose Power (Demagnetization)</h4>
        <ul class="text-xs text-slate-300 space-y-2">
            <li class="flex items-start gap-2">
                <span class="text-rose-400 font-bold">🔥</span>
                <span><strong>Heating:</strong> Extreme heat provides thermal kinetic energy that shakes aligned atomic domains back into random chaos.</span>
            </li>
            <li class="flex items-start gap-2">
                <span class="text-rose-400 font-bold">🔨</span>
                <span><strong>Hammering & Mechanical Shock:</strong> Heavy blows physically vibrate and dislodge domain alignment.</span>
            </li>
            <li class="flex items-start gap-2">
                <span class="text-rose-400 font-bold">💥</span>
                <span><strong>Dropping from Heights:</strong> Repeated falls onto hard concrete floors weaken magnetic field strength.</span>
            </li>
        </ul>
    </div>
    <div class="bg-slate-800/80 p-4 rounded-xl border border-emerald-500/30">
        <h4 class="text-emerald-400 font-bold text-base mb-2">Proper Scientific Storage Rules</h4>
        <div class="p-3 bg-emerald-950/40 rounded-lg border border-emerald-500/20 text-xs text-emerald-300 space-y-2">
            <div><strong>1. Store in Pairs:</strong> Place bar magnets in pairs with unlike poles facing the same direction.</div>
            <div><strong>2. Wooden Spacer:</strong> Separate the two magnets with a non-magnetic wooden strip to prevent direct clashing.</div>
            <div><strong>3. Soft Iron Keepers:</strong> Place pieces of soft iron (called keepers) across both exposed ends to channel magnetic field loops.</div>
            <div><strong>4. Electronic Safety:</strong> Keep magnets away from credit card magnetic strips, old CRT TVs, and precision instruments.</div>
        </div>
    </div>
</div>
""",
        "lecture_script": """Magnets are powerful, but they can be permanently ruined if mistreated. When a magnet is heated over a burner, struck violently with a hammer, or dropped repeatedly from a high table onto concrete, the violent physical vibrations scramble the orderly magnetic domains back into random disorientation, destroying its magnetism! Furthermore, magnets naturally weaken over years if left sitting alone due to self-demagnetizing free poles. To preserve bar magnets for decades, scientists store them in pairs with unlike poles facing the same side, separated by a thin wooden spacer. Across the two exposed ends, we attach strips of soft iron called magnetic keepers. The keepers provide an easy closed-loop highway for magnetic field lines, preventing the magnet from leaking flux and losing strength.""",
        "spoken_text": "Slide 15: Care and Storage of Magnets. Demagnetization Triggers, Soft Iron Keepers and Wooden Spacers. Magnets are powerful, but they can be permanently ruined if mistreated. When a magnet is heated over a burner, struck violently with a hammer, or dropped repeatedly from a high table onto concrete, the violent physical vibrations scramble the orderly magnetic domains back into random disorientation, destroying its magnetism! Furthermore, magnets naturally weaken over years if left sitting alone due to self-demagnetizing free poles. To preserve bar magnets for decades, scientists store them in pairs with unlike poles facing the same side, separated by a thin wooden spacer. Across the two exposed ends, we attach strips of soft iron called magnetic keepers. The keepers provide an easy closed-loop highway for magnetic field lines, preventing the magnet from leaking flux and losing strength.",
        "checkpoints": [
            {
                "question": "Which of the following actions can cause a permanent magnet to lose its magnetism?",
                "options": ["Washing it with clean cold water", "Heating it strongly or hammering it repeatedly", "Painting it red and blue", "Wrapping it in dry paper"],
                "correct": 1,
                "explanation": "Heating, hammering, and dropping from height disrupt the aligned magnetic domains, causing demagnetization.",
                "study_insight": "Thermal and mechanical energy randomize atomic dipoles."
            },
            {
                "question": "What are the soft iron pieces used across the ends of stored magnets called?",
                "options": ["Keepers", "Insulators", "Anodes", "Resistors"],
                "correct": 0,
                "explanation": "Soft iron keepers complete the magnetic circuit, preventing field leakage and preserving magnetic strength.",
                "study_insight": "For a horseshoe magnet, a single soft iron keeper across the poles is used."
            }
        ]
    },
    {
        "id": 16,
        "title": "Modern Marvels & Maglev",
        "subtitle": "Maglev Trains, Medical MRI & Earth's Magnetosphere Shield",
        "concept_html": """
<div class="grid grid-cols-1 md:grid-cols-3 gap-3">
    <div class="bg-slate-800/80 p-3 rounded-xl border border-cyan-500/30">
        <div class="text-cyan-400 font-bold text-sm mb-1">🚄 Maglev Trains</div>
        <p class="text-xs text-slate-300">
            Magnetic Levitation trains float 10 mm above guide tracks using powerful repelling electromagnets. With <strong>zero wheel friction</strong>, they cruise silently at over <strong>500 km/h</strong>!
        </p>
    </div>
    <div class="bg-slate-800/80 p-3 rounded-xl border border-emerald-500/30">
        <div class="text-emerald-400 font-bold text-sm mb-1">🏥 Medical MRI Scanners</div>
        <p class="text-xs text-slate-300">
            Magnetic Resonance Imaging utilizes superconducting magnets to align hydrogen nuclei in water molecules, producing ultra-high resolution 3D scans of the brain and organs without X-ray radiation.
        </p>
    </div>
    <div class="bg-slate-800/80 p-3 rounded-xl border border-purple-500/30">
        <div class="text-purple-400 font-bold text-sm mb-1">🛡️ Cosmic Shield</div>
        <p class="text-xs text-slate-300">
            Earth's geomagnetic field forms the <strong>magnetosphere</strong>, deflecting deadly high-energy solar wind and cosmic radiation, protecting our atmosphere, satellites, and all living organisms.
        </p>
    </div>
</div>
""",
        "lecture_script": """As we conclude our conceptual journey, let us marvel at how magnetism shapes the modern world. In high-speed transport, Maglev trains utilize powerful magnetic repulsion to literally float 10 to 15 millimeters above the railway track. Because there are no wheels touching steel rails, mechanical friction is eliminated, allowing trains to glide smoothly and quietly at speeds exceeding 500 kilometers per hour! In medicine, Magnetic Resonance Imaging, or MRI machines, use giant superconducting magnets to image the human brain, spinal cord, and internal organs in vivid microscopic detail without exposing patients to harmful radiation. And on a planetary scale, Earth's invisible magnetosphere acts like a giant protective bubble, deflecting deadly radiation from solar storms. From ancient lodestones guiding spice ships to futuristic floating trains, magnets remain one of science's greatest wonders!""",
        "spoken_text": "Slide 16: Modern Marvels and Maglev. Maglev Trains, Medical MRI and Earth's Magnetosphere Shield. As we conclude our conceptual journey, let us marvel at how magnetism shapes the modern world. In high-speed transport, Maglev trains utilize powerful magnetic repulsion to literally float 10 to 15 millimeters above the railway track. Because there are no wheels touching steel rails, mechanical friction is eliminated, allowing trains to glide smoothly and quietly at speeds exceeding 500 kilometers per hour! In medicine, Magnetic Resonance Imaging, or MRI machines, use giant superconducting magnets to image the human brain, spinal cord, and internal organs in vivid microscopic detail without exposing patients to harmful radiation. And on a planetary scale, Earth's invisible magnetosphere acts like a giant protective bubble, deflecting deadly radiation from solar storms. From ancient lodestones guiding spice ships to futuristic floating trains, magnets remain one of science's greatest wonders!",
        "checkpoints": [
            {
                "question": "How do Maglev trains achieve ultra-high speeds exceeding 500 km/h?",
                "options": ["Using rocket fuel", "By magnetically levitating above tracks to eliminate mechanical wheel friction", "By rolling on thousands of tiny ball bearings", "By traveling through vacuum tunnels underwater"],
                "correct": 1,
                "explanation": "Magnetic levitation floats the train above the guideway, eliminating friction between wheels and rails.",
                "study_insight": "Like magnetic poles repel, lifting the train carriage off the ground."
            },
            {
                "question": "What planetary shield protects Earth's atmosphere and life from solar storm radiation?",
                "options": ["The ozone layer only", "Earth's magnetosphere created by its internal magnetic field", "Ocean cloud layers", "Mountain ranges"],
                "correct": 1,
                "explanation": "Earth's magnetosphere deflects charged particles from solar wind around the planet, preserving life.",
                "study_insight": "Charged solar particles trapped in the magnetosphere cause the Northern and Southern Lights (Auroras)."
            }
        ]
    }
]

# Verify no latex in slides
for s in slides:
    verify_no_latex(s['concept_html'], f"Slide {s['id']} concept_html")
    verify_no_latex(s['lecture_script'], f"Slide {s['id']} lecture_script")
    verify_no_latex(s['spoken_text'], f"Slide {s['id']} spoken_text")
    for cp in s['checkpoints']:
        verify_no_latex(cp['question'], f"Slide {s['id']} checkpoint question")
        for opt in cp['options']:
            verify_no_latex(opt, f"Slide {s['id']} checkpoint option")
        verify_no_latex(cp['explanation'], f"Slide {s['id']} checkpoint explanation")
        verify_no_latex(cp['study_insight'], f"Slide {s['id']} checkpoint insight")

print(f"Verified {len(slides)} concept slides with zero raw LaTeX.")
