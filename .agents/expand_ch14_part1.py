with open('.agents/generate_c5m_ch14_part1.py', 'r') as f:
    text = f.read()

# Slide 2
s2_old = '''        "lecture": (
            "To explore the physical world with confidence, we must first master the four fundamental cardinal directions: North, South, "
            "East, and West. For thousands of years, people across ancient India and the entire world have used the rising sun as their "
            "primary celestial compass. If you stand outdoors early in the morning and face directly toward the glorious rising sun, you "
            "are facing East! Now, stretch both of your arms straight out to your sides like the wings of a soaring bird. Your left hand "
            "points directly toward the North, while your right hand points directly toward the South. Finally, the direction directly behind "
            "your back is West, which is where the sun sets in the evening! On almost all standard paper maps, atlases, and digital navigation "
            "screens, North is universally placed at the top of the page. Consequently, South is at the bottom, East lies to the right, and "
            "West lies to the left. Remembering this simple spatial orientation—East in front, West behind, North to the left, and South to "
            "the right—empowers you to read any geographical map and establish exact directional orientation anywhere on Earth with joyful certainty."
        ),'''

s2_new = '''        "lecture": (
            "To explore the physical world with true confidence, we must first master the four fundamental cardinal directions: North, South, "
            "East, and West. For thousands of years, people across ancient India and the entire world have used the glorious rising sun as their "
            "primary celestial compass. If you stand outdoors early in the morning and face directly toward the radiant rising sun, you "
            "are facing East! Now, stretch both of your arms straight out to your sides like the wings of a soaring eagle. Your left hand "
            "points directly toward the North, while your right hand points directly toward the South. Finally, the direction directly behind "
            "your back is West, which is where the sun sets peacefully in the evening! On almost all standard paper maps, atlases, and digital "
            "navigation screens, North is universally placed at the very top of the page. Consequently, South is always at the bottom, East "
            "lies to the right, and West lies to the left. Remembering this clear spatial orientation—East in front, West behind, North to "
            "the left, and South to the right—empowers learners to read any geographical map and establish exact directional orientation anywhere with certainty."
        ),'''

# Slide 5
s5_old = '''        "lecture": (
            "Mapping does not apply only to outdoor sanctuaries and national parks; it is equally powerful for organizing interior indoor "
            "spaces such as a bedroom or classroom! Imagine a student standing at the exact geometric center of a rectangular bedroom, "
            "facing directly toward the window on the northern wall. From this central vantage point, every piece of furniture occupies a "
            "distinct relative cardinal direction. Directly in front, toward the North, sits the wide window letting in fresh morning air. "
            "Directly behind, toward the South, is the wooden entry door leading into the hallway. To the left hand side, toward the West, "
            "stands a tall clothes cupboard and study bookshelf. And to the right hand side, toward the East, rests the cozy bed and small "
            "bedside lamp! Notice that determining directions indoors depends strictly on establishing a reference orientation. If the "
            "student rotates to face East instead of North, all relative directions rotate accordingly! However, true cardinal directions "
            "remain fixed: the northern wall remains the northern wall regardless of which way a person turns. Creating an overhead bird's-eye "
            "view map of a room teaches students to translate three-dimensional living spaces into clean two-dimensional architectural diagrams."
        ),'''

s5_new = '''        "lecture": (
            "Mapping does not apply only to outdoor sanctuaries and national parks; it is equally powerful for organizing interior indoor "
            "spaces such as a bedroom or school classroom! Imagine a student standing at the exact geometric center of a rectangular bedroom, "
            "facing directly toward the wide glass window on the northern wall. From this central vantage point, every piece of furniture occupies "
            "a distinct relative cardinal direction. Directly in front, toward the North, sits the wide window letting in fresh morning air. "
            "Directly behind, toward the South, is the wooden entry door leading into the hallway. To the left hand side, toward the West, "
            "stands a tall clothes cupboard and tidy study bookshelf. And to the right hand side, toward the East, rests the cozy bed and small "
            "bedside reading table! Notice that determining directions indoors depends strictly on establishing a clear reference orientation. "
            "If the student rotates to face East instead of North, all relative directions rotate accordingly! However, true cardinal directions "
            "remain permanently fixed: the northern wall remains the northern wall regardless of which way a person turns. Creating an overhead "
            "bird's-eye view map of a room teaches students to translate three-dimensional living spaces into clean two-dimensional architectural diagrams."
        ),'''

# Slide 6
s6_old = '''        "lecture": (
            "When navigating through spaces, it is essential to distinguish between absolute cardinal directions and relative observer "
            "directions. Cardinal directions—North, South, East, and West—are fixed with respect to planet Earth. The North Pole does not "
            "move when you turn around! In contrast, relative directions—such as forward, backward, left, and right—depend entirely on which "
            "way an individual observer is currently facing. Let us observe what happens: suppose an explorer is facing North. To this explorer, "
            "turning ninety degrees to the right means heading directly East. Now, suppose the explorer turns another quarter turn to the right; "
            "the explorer is now facing South! From this new southern orientation, what direction is to the explorer's right hand? Facing South, "
            "the right hand now points toward the West! Notice how the explorer's right hand pointed East initially, but after facing South, "
            "the right hand points West. This explains why directional instructions must always be interpreted with careful attention to the "
            "traveler's current heading. When sketching maps of homes, classrooms, or neighborhood parks, we establish fixed compass arrows "
            "so that everyone can navigate accurately regardless of personal bodily orientation."
        ),'''

s6_new = '''        "lecture": (
            "When navigating through diverse physical spaces, it is essential to understand the clear distinction between absolute cardinal "
            "directions and relative observer directions. Cardinal directions—North, South, East, and West—are permanently fixed with respect "
            "to planet Earth. The geographical North Pole does not move when you turn around! In sharp contrast, relative directions—such "
            "as forward, backward, left, and right—depend entirely on which way an individual observer happens to be facing at that exact moment. "
            "Let us observe what happens: suppose an explorer is facing North. To this explorer, turning ninety degrees to the right means heading "
            "directly East. Now, suppose the explorer turns another quarter turn to the right; the explorer is now facing South! From this new "
            "southern orientation, what direction is to the explorer's right hand? Facing South, the right hand now points toward the West! "
            "Notice how the explorer's right hand pointed East initially, but after facing South, the right hand points West! This explains "
            "why directional instructions must always be interpreted with careful attention to the traveler's current heading. When sketching "
            "maps of homes, classrooms, or neighborhood parks, we establish fixed compass arrows so that everyone can navigate accurately."
        ),'''

# Slide 7
s7_old = '''        "lecture": (
            "An exciting school field trip to the national zoological park begins bright and early in the morning! The yellow school bus departs "
            "from the main parking depot and must follow a designated street route to pick up students from various scheduled neighborhood "
            "bus stops before heading toward the zoo highway. Navigating a street map requires tracking both distances and directional turns "
            "at intersections. The bus travels two blocks East along Park Avenue, makes a ninety-degree left turn to travel three blocks "
            "North on Rose Street, and stops at Stop 1. From there, the bus turns right to travel two blocks East along Market Road to reach "
            "Stop 2. Next, it turns right again, driving two blocks South along River Road to reach Stop 3. Finally, turning left to head East, "
            "the bus merges smoothly onto Zoo Expressway! Notice how tracing this transit trajectory combines sequential cardinal steps: "
            "moving East, turning North, turning East, turning South, and turning East again. Reading street maps helps drivers avoid dead-ends, "
            "plan efficient fuel consumption, and guarantee that passengers are picked up on schedule with mathematical precision and safety."
        ),'''

s7_new = '''        "lecture": (
            "An exciting school field trip to the national zoological park begins bright and early in the morning! The large yellow school "
            "bus departs promptly from the main parking depot and must follow a carefully designated street route to pick up students from "
            "various scheduled neighborhood bus stops before heading toward the zoo highway. Navigating a street map requires tracking both "
            "measured block distances and directional turns at major intersections. The bus travels two blocks East along Park Avenue, makes "
            "a ninety-degree left turn to travel three blocks North on Rose Street, and stops at Stop 1. From there, the bus turns right to "
            "travel two blocks East along Market Road to reach Stop 2. Next, it turns right again, driving two blocks South along River Road "
            "to reach Stop 3. Finally, turning left to head East, the bus merges smoothly onto Zoo Expressway! Notice how tracing this transit "
            "trajectory combines sequential cardinal steps: moving East, turning North, turning East, turning South, and turning East again. "
            "Reading street maps helps drivers avoid confusing dead-ends, plan efficient fuel consumption, and guarantee that passengers are "
            "picked up safely on schedule with mathematical precision and peace of mind."
        ),'''

# Slide 8
s8_old = '''        "lecture": (
            "When traveling through city street grids, there are often multiple different pathways connecting a starting point to a "
            "destination. Determining which route is the shortest requires calculating total path lengths by adding individual street blocks! "
            "Consider a student walking from home at corner A to school at corner B on a rectangular grid. Route 1 heads three blocks East, "
            "then turns left and walks four blocks North, making a total distance of seven blocks. Route 2 walks four blocks North first, then "
            "turns right and walks three blocks East, also totaling seven blocks! What if a third route zig-zags through the neighborhood: "
            "one block East, one block North, one block East, two blocks North, and one block East, one block North? Adding the steps: one "
            "plus one plus one plus two plus one plus one equals seven blocks! On a clean rectangular grid without diagonal alleys, any path "
            "that moves exclusively toward the destination without backtracking has the exact same minimal distance, known as the Manhattan "
            "grid distance. However, if a route takes unnecessary detours or loops backwards, its total distance increases, wasting valuable time."
        ),'''

s8_new = '''        "lecture": (
            "When traveling through modern city street grids, there are often multiple different pathways connecting an initial starting "
            "point to a desired destination. Determining which route is the shortest requires calculating total path lengths by systematically "
            "adding individual street blocks! Consider a student walking from home at corner A to school at corner B on a rectangular grid. "
            "Route 1 heads three blocks East, then turns left and walks four blocks North, making a total distance of seven blocks. Route 2 "
            "walks four blocks North first, then turns right and walks three blocks East, also totaling exactly seven blocks! What if a third "
            "route zig-zags through the neighborhood: one block East, one block North, one block East, two blocks North, and one block East, "
            "one block North? Adding the steps: one plus one plus one plus two plus one plus one equals seven blocks! On a clean rectangular "
            "grid without diagonal alleys, any path that moves exclusively toward the destination without backtracking has the exact same minimal "
            "distance, known as the Manhattan grid distance. However, if a route takes unnecessary detours or loops backwards, its total distance "
            "increases significantly, wasting valuable travel time."
        ),'''

for old, new, sid in [(s2_old, s2_new, 2), (s5_old, s5_new, 5), (s6_old, s6_new, 6), (s7_old, s7_new, 7), (s8_old, s8_new, 8)]:
    assert old in text, f"Slide {sid} old text not found"
    text = text.replace(old, new)

with open('.agents/generate_c5m_ch14_part1.py', 'w') as f:
    f.write(text)

