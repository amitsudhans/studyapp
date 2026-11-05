import re
import sys

def verify_no_latex(text, context=""):
    matches = re.findall(r'\\[a-zA-Z]+', text)
    if matches:
        print(f"ERROR: Raw LaTeX found in {context}: {matches[:10]}")
        sys.exit(1)

quiz_questions = [
    # Challenge 1 (Q1 - Q10): Slides 1-4 topics
    {
        "id": 1,
        "slide_id": 17,
        "challenge_num": 1,
        "q_num": 1,
        "question": "What natural magnetic rock was discovered in ancient times and used by early navigators?",
        "options": ["Bauxite", "Lodestone (Magnetite)", "Limestone", "Hematite"],
        "correct": 1,
        "explanation": "Lodestone is a naturally occurring magnetic iron oxide mineral (magnetite) that aligns North-South when suspended.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. In ancient times, shepherds and travelers discovered a black rock that attracted small iron particles.</p>
    <p>2. This natural mineral is called <strong>lodestone</strong>, composed of the iron oxide magnetite.</p>
    <p>3. Because it possessed the directive property, it was used to find directions, giving it the name 'leading stone' or lodestone.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Lodestone (Magnetite)</p>
</div>
"""
    },
    {
        "id": 2,
        "slide_id": 17,
        "challenge_num": 1,
        "q_num": 2,
        "question": "On clear nights before compasses, which celestial body did Northern Hemisphere sailors use to find North?",
        "options": ["The Pole Star (Polaris)", "The Planet Mars", "Halley's Comet", "The Moon at zenith"],
        "correct": 0,
        "explanation": "The Pole Star (Polaris) sits almost directly above Earth's geographic North Pole and remains fixed in the northern sky.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Earth's rotational axis points almost directly towards Polaris (the Pole Star).</p>
    <p>2. While other stars appear to rotate across the sky due to Earth's rotation, Polaris stays stationary in the North.</p>
    <p>3. On overcast or stormy nights, clouds blocked Polaris, necessitating the magnetic compass.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: The Pole Star (Polaris)</p>
</div>
"""
    },
    {
        "id": 3,
        "slide_id": 17,
        "challenge_num": 1,
        "q_num": 3,
        "question": "Which of the following is an example of an artificial magnet?",
        "options": ["A raw lump of lodestone", "A manufactured cylindrical bar magnet", "A piece of limestone", "Granite rock"],
        "correct": 1,
        "explanation": "Artificial magnets are human-made magnets formed by magnetizing magnetic metals like iron and steel into specific shapes.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Natural magnets occur naturally in the Earth's crust as lodestone.</p>
    <p>2. Artificial magnets are synthesized by shaping iron, steel, or alloys and subjecting them to magnetic fields.</p>
    <p>3. Common shapes include bar, U-shaped (horseshoe), ring, cylindrical, and magnetic needles.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: A manufactured cylindrical bar magnet</p>
</div>
"""
    },
    {
        "id": 4,
        "slide_id": 17,
        "challenge_num": 1,
        "q_num": 4,
        "question": "Why are horseshoe magnets curved into a U-shape?",
        "options": ["To make them easier to paint", "To bring both magnetic poles close together for a concentrated field", "To eliminate the South pole", "To reduce the magnet's mass"],
        "correct": 1,
        "explanation": "The U-shape positions North and South poles side by side, creating a very strong, focused magnetic field across the gap.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. In a straight bar magnet, the two poles are separated by the full length of the bar.</p>
    <p>2. Bending the bar into a horseshoe shape brings both poles into close proximity.</p>
    <p>3. This concentrates magnetic flux lines between the tips, maximizing lifting power on iron objects.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: To bring both magnetic poles close together for a concentrated field</p>
</div>
"""
    },
    {
        "id": 5,
        "slide_id": 17,
        "challenge_num": 1,
        "q_num": 5,
        "question": "Which of the following materials is strongly attracted to a magnet?",
        "options": ["Rubber eraser", "Pure copper wire", "Steel paper clip", "Glass marble"],
        "correct": 2,
        "explanation": "Steel is an alloy composed mostly of iron, making paper clips ferromagnetic and strongly magnetic.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Magnetic materials contain ferromagnetic elements like iron, nickel, or cobalt.</p>
    <p>2. Steel is made by adding small amounts of carbon to iron, retaining strong magnetic properties.</p>
    <p>3. Rubber, copper, and glass are non-magnetic substances with no attraction to magnets.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Steel paper clip</p>
</div>
"""
    },
    {
        "id": 6,
        "slide_id": 17,
        "challenge_num": 1,
        "q_num": 6,
        "question": "Which list contains ONLY non-magnetic materials?",
        "options": ["Iron, Nickel, Cobalt", "Wood, Plastic, Aluminium, Glass", "Steel, Glass, Iron, Wood", "Nickel, Copper, Brass, Paper"],
        "correct": 1,
        "explanation": "Wood, plastic, aluminium, and glass are all non-magnetic and experience zero attraction to a magnet.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Non-magnetic materials do not experience attraction toward magnetic poles.</p>
    <p>2. Wood (cellulose), plastic (synthetic polymers), aluminium (non-ferrous metal), and glass (silica) are non-magnetic.</p>
    <p>3. Any list with iron, steel, nickel, or cobalt contains magnetic materials.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Wood, Plastic, Aluminium, Glass</p>
</div>
"""
    },
    {
        "id": 7,
        "slide_id": 17,
        "challenge_num": 1,
        "q_num": 7,
        "question": "When iron filings are sprinkled around a bar magnet, where do they cling most densely?",
        "options": ["At the exact geometric center", "Near the two ends (poles)", "Evenly spread across the whole surface", "Only on the top surface"],
        "correct": 1,
        "explanation": "Magnetic attraction is strongest near the ends (poles) of a magnet, creating dense clusters of filings there.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Magnetic field lines emerge from the North pole and curve into the South pole.</p>
    <p>2. Field line density is greatest at the two ends, which are called the poles.</p>
    <p>3. Therefore, iron filings cling densely near the ends and remain sparse in the middle.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Near the two ends (poles)</p>
</div>
"""
    },
    {
        "id": 8,
        "slide_id": 17,
        "challenge_num": 1,
        "q_num": 8,
        "question": "What are the two poles of a magnet named?",
        "options": ["East and West poles", "Positive and Negative poles", "North and South poles", "Upper and Lower poles"],
        "correct": 2,
        "explanation": "The poles are named the North-seeking (North) pole and South-seeking (South) pole based on geographic alignment.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. When a magnet is suspended freely, one end always points towards geographic North.</p>
    <p>2. That end is designated as the North pole (N).</p>
    <p>3. The opposite end pointing towards geographic South is designated as the South pole (S).</p>
    <p class='text-emerald-400 font-bold'>Correct Option: North and South poles</p>
</div>
"""
    },
    {
        "id": 9,
        "slide_id": 17,
        "challenge_num": 1,
        "q_num": 9,
        "question": "Why is brass used to make the outer casing of a magnetic compass instead of iron?",
        "options": ["Brass is cheaper than iron", "Brass is non-magnetic and will not distort the needle's orientation", "Brass makes the needle spin faster", "Brass is transparent like glass"],
        "correct": 1,
        "explanation": "Iron is magnetic and would attract and misguide the compass needle, whereas brass is non-magnetic and inert.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. If a compass box were made of iron, the magnetic needle would be drawn to the casing walls.</p>
    <p>2. This would prevent the needle from responding to Earth's geomagnetic field.</p>
    <p>3. Brass is a copper-zinc alloy that is completely non-magnetic, allowing the needle to spin freely.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Brass is non-magnetic and will not distort the needle's orientation</p>
</div>
"""
    },
    {
        "id": 10,
        "slide_id": 17,
        "challenge_num": 1,
        "q_num": 10,
        "question": "A student touches a bar magnet to an aluminium foil roll and a copper coin. What will happen?",
        "options": ["Both will stick tightly to the magnet", "Only the copper coin will stick", "Only the aluminium foil will stick", "Neither will stick because both are non-magnetic"],
        "correct": 3,
        "explanation": "Both aluminium and copper are non-ferrous metals and do not experience magnetic attraction.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. It is a common misconception that all metals are magnetic.</p>
    <p>2. Pure copper and aluminium lack magnetic domains and are non-magnetic.</p>
    <p>3. Thus, neither the aluminium foil nor the copper coin will stick to the magnet.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Neither will stick because both are non-magnetic</p>
</div>
"""
    },

    # Challenge 2 (Q11 - Q20): Slides 5-8 topics
    {
        "id": 11,
        "slide_id": 18,
        "challenge_num": 2,
        "q_num": 11,
        "question": "What happens if a bar magnet is sawed into two equal halves?",
        "options": ["One half has only a North pole and the other only a South pole", "Each half becomes a complete magnet with both North and South poles", "Both halves lose their magnetism completely", "The cut ends become neutral and non-magnetic forever"],
        "correct": 1,
        "explanation": "Cutting a magnet creates new opposite poles at the cut faces, producing two complete smaller magnets.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Magnetism arises from microscopic aligned atomic dipoles throughout the material.</p>
    <p>2. Slicing the magnet separates the dipoles into two groups, each with aligned ends.</p>
    <p>3. New North and South poles immediately appear at the fresh cut surfaces.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Each half becomes a complete magnet with both North and South poles</p>
</div>
"""
    },
    {
        "id": 12,
        "slide_id": 18,
        "challenge_num": 2,
        "q_num": 12,
        "question": "What is an isolated, standalone magnetic pole called in physics, and does it exist in nature?",
        "options": ["Monopole; yes, found in rocks", "Monopole; no, magnetic poles always exist in pairs", "Dipole; yes, found in all magnets", "Quadrupole; only in outer space"],
        "correct": 1,
        "explanation": "An isolated magnetic pole is called a magnetic monopole, which has never been observed to exist in nature.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Unlike electric charges (which can exist as isolated positive or negative charges), magnetic poles cannot be isolated.</p>
    <p>2. A hypothetical single magnetic pole is termed a magnetic monopole.</p>
    <p>3. In classical physics and empirical observation, magnetic poles always exist in inseparable pairs.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Monopole; no, magnetic poles always exist in pairs</p>
</div>
"""
    },
    {
        "id": 13,
        "slide_id": 18,
        "challenge_num": 2,
        "q_num": 13,
        "question": "A freely suspended bar magnet always settles pointing along which geographic direction?",
        "options": ["East-West direction", "North-South direction", "Random direction each time", "Directly toward the Sun"],
        "correct": 1,
        "explanation": "Due to Earth's planetary magnetic field, a freely suspended magnet always aligns along the North-South axis.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. When a magnet is suspended on a thread, it is free to rotate in the horizontal plane.</p>
    <p>2. Earth's geomagnetic field exerts a magnetic torque on the magnet's poles.</p>
    <p>3. It turns until the torque balances out, aligning parallel to Earth's North-South magnetic lines.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: North-South direction</p>
</div>
"""
    },
    {
        "id": 14,
        "slide_id": 18,
        "challenge_num": 2,
        "q_num": 14,
        "question": "What is the natural tendency of a suspended magnet to align North-South called?",
        "options": ["Attractive property", "Directive property", "Thermal property", "Conductive property"],
        "correct": 1,
        "explanation": "The directive property is the property of a magnet that enables it to seek and point in a definite geographic direction.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Magnets possess two key fundamental properties: the attractive property and the directive property.</p>
    <p>2. The attractive property attracts magnetic materials like iron and nickel.</p>
    <p>3. The directive property guides a suspended magnet to point North-South, enabling navigation.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Directive property</p>
</div>
"""
    },
    {
        "id": 15,
        "slide_id": 18,
        "challenge_num": 2,
        "q_num": 15,
        "question": "What generates Earth's vast geomagnetic field?",
        "options": ["A giant bar magnet buried in the crust", "Circulating currents of molten iron and nickel in the outer core", "Ocean waves churning salt", "Volcanoes erupting on the surface"],
        "correct": 1,
        "explanation": "Convection currents of molten iron and nickel in Earth's outer core act like a giant dynamo, producing the geomagnetic field.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Earth has a liquid outer core composed of molten iron and nickel at high temperature and pressure.</p>
    <p>2. As Earth rotates, convection currents generate electrical currents in this conductive fluid.</p>
    <p>3. These self-sustaining currents produce Earth's geomagnetic field via the geodynamo mechanism.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Circulating currents of molten iron and nickel in the outer core</p>
</div>
"""
    },
    {
        "id": 16,
        "slide_id": 18,
        "challenge_num": 2,
        "q_num": 16,
        "question": "Which magnetic pole of Earth's internal magnet lies near the geographic North Pole?",
        "options": ["Earth's magnetic North pole", "Earth's magnetic South pole", "Earth's magnetic East pole", "Earth has no internal magnetic poles"],
        "correct": 1,
        "explanation": "Since opposite poles attract, the North pole of a compass is attracted to Earth's magnetic South pole near geographic north.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. By definition of magnetism, opposite poles attract: North attracts South.</p>
    <p>2. The North-seeking pole of our compass needle points toward geographic North.</p>
    <p>3. Therefore, the magnetic pole residing inside Earth near geographic North must behave as a magnetic South pole.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Earth's magnetic South pole</p>
</div>
"""
    },
    {
        "id": 17,
        "slide_id": 18,
        "challenge_num": 2,
        "q_num": 17,
        "question": "Why is the needle inside a magnetic compass mounted on a sharp jewel or agate pivot?",
        "options": ["To make the compass expensive", "To minimize rotational friction so the needle swings freely", "To prevent the needle from becoming hot", "To magnetize the glass cover"],
        "correct": 1,
        "explanation": "A sharp pivot point with a hard jewel bearing minimizes mechanical friction, allowing weak geomagnetic forces to turn the needle.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Earth's magnetic field at the surface is relatively weak (about 25 to 65 microteslas).</p>
    <p>2. If there were significant mechanical friction at the bearing, the needle could not turn.</p>
    <p>3. A sharp jewel bearing reduces contact area to near zero, eliminating frictional drag.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: To minimize rotational friction so the needle swings freely</p>
</div>
"""
    },
    {
        "id": 18,
        "slide_id": 18,
        "challenge_num": 2,
        "q_num": 18,
        "question": "How do you align a handheld compass to read other directions like East or West?",
        "options": ["Shake it until the needle stops pointing North", "Rotate the outer case until the dial's 'N' matches the red needle tip", "Turn the needle with your fingers", "Heat the casing with a match"],
        "correct": 1,
        "explanation": "Keep the compass level and rotate the casing until 'N' on the dial aligns beneath the red North needle; then read other directions.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. The needle automatically points to magnetic North.</p>
    <p>2. Slowly rotate the compass housing so that 'N' aligns directly with the painted red tip.</p>
    <p>3. The graduated dial now accurately points out East (90 degrees), South (180 degrees), and West (270 degrees).</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Rotate the outer case until the dial's 'N' matches the red needle tip</p>
</div>
"""
    },
    {
        "id": 19,
        "slide_id": 18,
        "challenge_num": 2,
        "q_num": 19,
        "question": "What English scientist published 'De Magnete' in 1600, concluding that Earth is a giant magnet?",
        "options": ["Sir Isaac Newton", "Dr. William Gilbert", "Michael Faraday", "James Clerk Maxwell"],
        "correct": 1,
        "explanation": "Dr. William Gilbert, physician to Queen Elizabeth I, deduced in 1600 that Earth itself behaves as a giant spherical magnet.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. William Gilbert shaped a spherical lodestone called a 'terrella' (little Earth).</p>
    <p>2. By moving miniature compasses over it, he reproduced every directional phenomenon seen on Earth.</p>
    <p>3. He concluded that our entire planet acts like a giant permanent magnet.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Dr. William Gilbert</p>
</div>
"""
    },
    {
        "id": 20,
        "slide_id": 18,
        "challenge_num": 2,
        "q_num": 20,
        "question": "If you are facing the direction in which a compass needle points, which direction is directly to your right?",
        "options": ["South", "West", "East", "North-West"],
        "correct": 2,
        "explanation": "When facing North, your right hand points directly toward the East.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. The compass needle points toward North.</p>
    <p>2. Facing North: directly behind you is South.</p>
    <p>3. To your right is East (where the Sun rises), and to your left is West (where the Sun sets).</p>
    <p class='text-emerald-400 font-bold'>Correct Option: East</p>
</div>
"""
    },

    # Challenge 3 (Q21 - Q30): Slides 9-13 topics
    {
        "id": 21,
        "slide_id": 19,
        "challenge_num": 3,
        "q_num": 21,
        "question": "What was the ancient Indian maritime compass called?",
        "options": ["Surya-Yantra", "Matsya-Yantra (Machchh-Yantra)", "Vayu-Chakra", "Drishti-Yantra"],
        "correct": 1,
        "explanation": "Matsya-Yantra was an ancient Indian device consisting of a magnetized iron fish floating in oil for sea navigation.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. 'Matsya' means fish in Sanskrit, and 'Yantra' means instrument or device.</p>
    <p>2. A magnetized iron cutout of a fish was floated on oil inside a vessel.</p>
    <p>3. The fish turned autonomously until its head aligned toward the North.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Matsya-Yantra (Machchh-Yantra)</p>
</div>
"""
    },
    {
        "id": 22,
        "slide_id": 19,
        "challenge_num": 3,
        "q_num": 22,
        "question": "Why did ancient mariners float the magnetized fish of the Matsya-Yantra in oil instead of water?",
        "options": ["Water causes iron to dissolve in minutes", "Oil's viscosity helps damp down swaying caused by ocean waves", "Oil makes iron magnetic permanently", "Water blocks magnetic fields"],
        "correct": 1,
        "explanation": "The viscosity of oil prevented erratic needle oscillation when the ship rocked in ocean swells.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Ships constantly roll and pitch when sailing through open ocean waves.</p>
    <p>2. If floated on water, the iron fish would wobble violently with every wave.</p>
    <p>3. Thick, viscous oil damped these mechanical oscillations, keeping the directional indicator steady.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Oil's viscosity helps damp down swaying caused by ocean waves</p>
</div>
"""
    },
    {
        "id": 23,
        "slide_id": 19,
        "challenge_num": 3,
        "q_num": 23,
        "question": "When magnetizing a steel sewing needle by the single-touch method, what is the correct motion?",
        "options": ["Rubbing back and forth rapidly like an eraser", "Stroking in one direction only and lifting the pole away at the end of each stroke", "Tapping the needle firmly on the center with a hammer", "Holding the magnet stationary against the needle for 10 minutes"],
        "correct": 1,
        "explanation": "Stroking in a single direction aligns magnetic domains; rubbing back and forth scrambles them.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Place the needle on a table and stroke from one end to the other with one pole.</p>
    <p>2. Lift the magnet into the air, return to the start, and stroke again in the same direction.</p>
    <p>3. Repeating this 30 to 40 times pulls the atomic domains into uniform parallel alignment.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Stroking in one direction only and lifting the pole away at the end of each stroke</p>
</div>
"""
    },
    {
        "id": 24,
        "slide_id": 19,
        "challenge_num": 3,
        "q_num": 24,
        "question": "What is the fundamental law of magnetic poles regarding attraction and repulsion?",
        "options": ["Like poles attract and unlike poles repel", "Unlike poles attract and like poles repel", "All poles attract each other equally", "Poles only repel when heated"],
        "correct": 1,
        "explanation": "Unlike poles (North-South) attract, while like poles (North-North or South-South) repel.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. North pole facing South pole: magnetic lines pull them together (attraction).</p>
    <p>2. North facing North or South facing South: lines push each other away (repulsion).</p>
    <p>3. This is the universal rule: 'Like poles repel, unlike poles attract.'</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Unlike poles attract and like poles repel</p>
</div>
"""
    },
    {
        "id": 25,
        "slide_id": 19,
        "challenge_num": 3,
        "q_num": 25,
        "question": "Why is repulsion considered the ONLY sure test of magnetism?",
        "options": ["Magnets cannot attract in air", "A magnet attracts both an opposite pole AND unmagnetized iron, but only repels another magnet", "Repulsion can be heard with our ears", "Iron bars repel both poles of a magnet"],
        "correct": 1,
        "explanation": "Because a magnet attracts both ends of an unmagnetized iron bar, attraction does not prove magnetization. Only repulsion proves it is a magnet.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. An ordinary iron nail will stick to the North pole of a magnet and also to the South pole.</p>
    <p>2. Therefore, attraction occurs between a magnet and any unmagnetized magnetic material.</p>
    <p>3. Repulsion, however, can ONLY happen between two like magnetic poles.</p>
    <p>4. Hence, repulsion is the sole definitive test for magnetism.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: A magnet attracts both an opposite pole AND unmagnetized iron, but only repels another magnet</p>
</div>
"""
    },
    {
        "id": 26,
        "slide_id": 19,
        "challenge_num": 3,
        "q_num": 26,
        "question": "A bar magnet rests on round pencils. When the North pole of another magnet approaches its South pole, what occurs?",
        "options": ["The resting magnet rolls rapidly away (repulsion)", "The resting magnet rolls toward the hand (attraction)", "The pencils snap into pieces", "The resting magnet loses all magnetism"],
        "correct": 1,
        "explanation": "North and South are unlike poles, creating an attractive pulling force that draws the roller magnet forward.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. The round pencils reduce friction, allowing the resting magnet to move easily.</p>
    <p>2. Opposite poles (North and South) generate attractive magnetic lines of force.</p>
    <p>3. Therefore, the resting magnet rolls forward toward the approaching magnet.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: The resting magnet rolls toward the hand (attraction)</p>
</div>
"""
    },
    {
        "id": 27,
        "slide_id": 19,
        "challenge_num": 3,
        "q_num": 27,
        "question": "You bring the North pole of a bar magnet near End A of a metal rod; it attracts. You bring the North pole near End B; it also attracts! What is this rod?",
        "options": ["A permanent bar magnet with North at End A", "A permanent bar magnet with South at End B", "An unmagnetized piece of magnetic material (such as soft iron)", "A non-magnetic wooden cylinder"],
        "correct": 2,
        "explanation": "If both ends of a metal rod are attracted to the same magnetic pole with zero repulsion, the rod is plain unmagnetized magnetic material.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. If the rod were a magnet, one of its ends would be a North pole and would repel the approaching North pole.</p>
    <p>2. Since both End A and End B are attracted, the rod lacks permanent poles.</p>
    <p>3. The rod is an unmagnetized magnetic material (like soft iron) whose domains temporarily align toward the magnet.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: An unmagnetized piece of magnetic material (such as soft iron)</p>
</div>
"""
    },
    {
        "id": 28,
        "slide_id": 19,
        "challenge_num": 3,
        "q_num": 28,
        "question": "When a needle is stroked from eye to point with the North pole of a magnet, what pole forms at the point?",
        "options": ["North pole", "South pole", "East pole", "It remains neutral"],
        "correct": 1,
        "explanation": "As the North pole of the magnet leaves the point of the needle, it pulls and leaves behind an opposite South pole at that point.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. In the single-touch method, the end where the stroke finishes develops the opposite polarity to the stroking pole.</p>
    <p>2. Since the stroking pole was North, the departing tip develops a South pole.</p>
    <p>3. The starting end (the eye) retains the same polarity as the stroking pole (North).</p>
    <p class='text-emerald-400 font-bold'>Correct Option: South pole</p>
</div>
"""
    },
    {
        "id": 29,
        "slide_id": 19,
        "challenge_num": 3,
        "q_num": 29,
        "question": "Which of the following setups will show magnetic repulsion?",
        "options": ["North pole near iron nail", "South pole near copper coin", "South pole near South pole of another magnet", "North pole near wooden block"],
        "correct": 2,
        "explanation": "Repulsion only occurs between two like magnetic poles, such as South facing South or North facing North.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. An iron nail and copper coin cannot repel a magnet.</p>
    <p>2. Wooden blocks do not interact with magnets.</p>
    <p>3. Two identical poles (South and South) push apart with repulsive magnetic force.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: South pole near South pole of another magnet</p>
</div>
"""
    },
    {
        "id": 30,
        "slide_id": 19,
        "challenge_num": 3,
        "q_num": 30,
        "question": "What is the primary function of floating a magnetized needle on a cork in water?",
        "options": ["To wash the needle clean", "To allow the needle to rotate freely in the horizontal plane with minimal friction", "To test if the needle can sink", "To neutralize the needle's North pole"],
        "correct": 1,
        "explanation": "Water provides a near-frictionless fluid bearing that allows the light cork and needle to turn toward North-South.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. A magnet cannot align North-South if resting on a high-friction rough surface.</p>
    <p>2. Floating the needle on a buoyant slice of cork in water eliminates friction.</p>
    <p>3. The weak geomagnetic torque easily turns the needle into alignment with Earth's poles.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: To allow the needle to rotate freely in the horizontal plane with minimal friction</p>
</div>
"""
    },

    # Challenge 4 (Q31 - Q40): Slides 14-16 topics
    {
        "id": 31,
        "slide_id": 20,
        "challenge_num": 4,
        "q_num": 31,
        "question": "Can magnetic force act across a sheet of glass, cardboard, or plastic without direct physical contact?",
        "options": ["No, magnetic force requires direct physical touch", "Yes, magnetic fields easily penetrate non-magnetic barriers", "Only if the barrier is wet with saltwater", "Only when the magnet is heated"],
        "correct": 1,
        "explanation": "Magnetic field lines pass freely through non-magnetic materials like glass, paper, cardboard, and plastic.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Magnetism is a non-contact field force that acts across space.</p>
    <p>2. Non-magnetic materials do not absorb or redirect magnetic field lines.</p>
    <p>3. Thus, a magnet held under a cardboard or glass sheet can easily guide a paper clip above it.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Yes, magnetic fields easily penetrate non-magnetic barriers</p>
</div>
"""
    },
    {
        "id": 32,
        "slide_id": 20,
        "challenge_num": 4,
        "q_num": 32,
        "question": "How can you retrieve steel pins dropped inside a glass of water without getting your hands wet?",
        "options": ["Pour cold oil into the glass", "Slide a strong magnet along the outside wall of the glass to guide the pins upward", "Whistle loudly to vibrate the glass", "Shine an ultraviolet light beam into the water"],
        "correct": 1,
        "explanation": "Because magnetic fields penetrate water and glass, sliding a magnet up the outer wall pulls the pins up inside.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Both water and glass are non-magnetic substances.</p>
    <p>2. The magnetic force lines pass straight through the glass and water to attract the steel pins.</p>
    <p>3. As you move the magnet up the outside of the glass, the pins follow to the top rim.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Slide a strong magnet along the outside wall of the glass to guide the pins upward</p>
</div>
"""
    },
    {
        "id": 33,
        "slide_id": 20,
        "challenge_num": 4,
        "q_num": 33,
        "question": "Which of the following actions can cause a permanent magnet to lose its magnetic strength (demagnetize)?",
        "options": ["Washing it with clean tap water", "Heating it strongly over a flame or hammering it repeatedly", "Storing it in a dark wooden box", "Painting its ends red and blue"],
        "correct": 1,
        "explanation": "Heating and mechanical impact provide energy that disrupts aligned magnetic domains, randomizing them.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Permanent magnetism depends on aligned microscopic domains.</p>
    <p>2. High temperature increases thermal kinetic vibrations, scrambling domain orientation.</p>
    <p>3. Hammering or dropping from height mechanically dislodges the alignment, causing demagnetization.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Heating it strongly over a flame or hammering it repeatedly</p>
</div>
"""
    },
    {
        "id": 34,
        "slide_id": 20,
        "challenge_num": 4,
        "q_num": 34,
        "question": "How should bar magnets be properly stored in pairs to preserve their magnetic strength for years?",
        "options": ["With like poles touching directly", "In pairs with unlike poles facing the same direction, separated by wood and bridged with soft iron keepers", "Immersed in boiling water", "Wrapped tightly in aluminium foil"],
        "correct": 1,
        "explanation": "Pairing unlike poles with a wooden spacer and bridging the ends with soft iron keepers forms a closed magnetic circuit that prevents flux leakage.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Free magnetic poles tend to self-demagnetize over long periods of time.</p>
    <p>2. Storing bar magnets in pairs with unlike poles side-by-side, separated by a wooden strip, minimizes repulsion.</p>
    <p>3. Placing soft iron pieces (keepers) across the ends channels the magnetic lines into a closed loop.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: In pairs with unlike poles facing the same direction, separated by wood and bridged with soft iron keepers</p>
</div>
"""
    },
    {
        "id": 35,
        "slide_id": 20,
        "challenge_num": 4,
        "q_num": 35,
        "question": "What is the purpose of placing soft iron 'keepers' across the poles of stored magnets?",
        "options": ["To keep the magnets from rusting", "To complete a closed magnetic loop and prevent loss of magnetism", "To make the magnets heavier", "To change their color to grey"],
        "correct": 1,
        "explanation": "Keepers provide a high-permeability pathway for magnetic field lines, forming a closed loop that preserves magnetic potency.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Without keepers, magnetic field lines spread out through air, leading to slow demagnetization.</p>
    <p>2. Soft iron easily conducts magnetic lines, routing them from North directly to South.</p>
    <p>3. This closed magnetic circuit keeps the atomic domains locked in alignment.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: To complete a closed magnetic loop and prevent loss of magnetism</p>
</div>
"""
    },
    {
        "id": 36,
        "slide_id": 20,
        "challenge_num": 4,
        "q_num": 36,
        "question": "Why should strong magnets be kept away from credit cards, bank ATM cards, and audio cassettes?",
        "options": ["Magnets dissolve plastic cards", "The strong magnetic field can erase or corrupt data stored on magnetic stripes and tapes", "Magnets make cards too heavy to carry", "Magnets set cards on fire"],
        "correct": 1,
        "explanation": "The dark stripe on ATM cards stores account data using magnetized iron particles that can be scrambled by external magnets.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. Credit cards, transit passes, and magnetic tapes store binary digital information in tiny magnetized zones.</p>
    <p>2. Bringing a strong magnet near the card randomizes these magnetic patterns.</p>
    <p>3. Once randomized, card readers can no longer decode the stored account data.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: The strong magnetic field can erase or corrupt data stored on magnetic stripes and tapes</p>
</div>
"""
    },
    {
        "id": 37,
        "slide_id": 20,
        "challenge_num": 4,
        "q_num": 37,
        "question": "What technology enables high-speed Maglev trains to travel at over 500 km/h without wheel friction?",
        "options": ["Steam jet propulsion", "Magnetic levitation using repelling electromagnets to float above the track", "Liquid nitrogen lubricants", "Rocket boosters on each car"],
        "correct": 1,
        "explanation": "Maglev trains use magnetic repulsion to hover above the track, eliminating mechanical contact and wheel friction.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. 'Maglev' stands for Magnetic Levitation.</p>
    <p>2. Powerful electromagnets beneath the train repel magnets on the guideway track.</p>
    <p>3. The train lifts 10 to 15 mm into the air, allowing frictionless gliding at extreme speeds.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Magnetic levitation using repelling electromagnets to float above the track</p>
</div>
"""
    },
    {
        "id": 38,
        "slide_id": 20,
        "challenge_num": 4,
        "q_num": 38,
        "question": "What medical diagnostic technology uses superconducting magnets to capture detailed 3D images of soft tissues without ionizing radiation?",
        "options": ["X-ray radiography", "MRI (Magnetic Resonance Imaging)", "CT scan", "Ultrasound echo"],
        "correct": 1,
        "explanation": "Magnetic Resonance Imaging (MRI) uses strong magnetic fields and radio waves to create detailed images of organs and tissues.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. MRI utilizes a giant magnetic coil to align hydrogen protons in body water.</p>
    <p>2. Radio waves temporarily shift these protons, which emit signals as they re-align.</p>
    <p>3. Sensors capture these signals to construct high-contrast cross-sectional images of the brain, heart, and joints.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: MRI (Magnetic Resonance Imaging)</p>
</div>
"""
    },
    {
        "id": 39,
        "slide_id": 20,
        "challenge_num": 4,
        "q_num": 39,
        "question": "What is the name of the planetary magnetic shield that deflects high-energy solar wind away from Earth?",
        "options": ["The Ionosphere", "The Ozone Layer", "The Magnetosphere", "The Stratosphere"],
        "correct": 2,
        "explanation": "Earth's magnetosphere is the region of space dominated by Earth's magnetic field that shields the biosphere from cosmic solar particles.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. The Sun constantly emits a stream of charged particles known as solar wind.</p>
    <p>2. Earth's geomagnetic field extends tens of thousands of kilometers into space, forming the magnetosphere.</p>
    <p>3. This magnetic barrier deflects solar radiation around Earth, protecting life and telecommunication satellites.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: The Magnetosphere</p>
</div>
"""
    },
    {
        "id": 40,
        "slide_id": 20,
        "challenge_num": 4,
        "q_num": 40,
        "question": "Why does a horseshoe magnet only require a SINGLE soft iron keeper when stored?",
        "options": ["Horseshoe magnets are half as strong as bar magnets", "Both North and South poles lie on the same side and can be bridged by one straight bar", "Horseshoe magnets do not need keepers at all", "Keepers only stick to North poles"],
        "correct": 1,
        "explanation": "Because the U-shape places both poles side by side at the tips, a single straight soft iron bar across the gap connects both poles.",
        "solution_html": """
<div class='text-sm space-y-2'>
    <p><strong>Step-by-Step Explanation:</strong></p>
    <p>1. In a bar magnet, poles are at opposite ends, requiring two keepers and a partner magnet.</p>
    <p>2. In a horseshoe magnet, both North and South poles are right next to each other at the open end.</p>
    <p>3. A single piece of soft iron laid across the two tips completes the magnetic loop perfectly.</p>
    <p class='text-emerald-400 font-bold'>Correct Option: Both North and South poles lie on the same side and can be bridged by one straight bar</p>
</div>
"""
    }
]

# Verify no latex
for q in quiz_questions:
    verify_no_latex(q['question'], f"Question {q['id']} question")
    for opt in q['options']:
        verify_no_latex(opt, f"Question {q['id']} option")
    verify_no_latex(q['explanation'], f"Question {q['id']} explanation")
    verify_no_latex(q['solution_html'], f"Question {q['id']} solution_html")

print(f"Verified {len(quiz_questions)} quiz questions with zero raw LaTeX.")
