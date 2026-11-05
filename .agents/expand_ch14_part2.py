with open('.agents/generate_c5m_ch14_part2.py', 'r') as f:
    text = f.read()

# Slide 9
s9_old = '''        "lecture": (
            "Modern bustling metropolitan cities rely on intricate public rapid transit networks such as the world-renowned Delhi Metro! "
            "To help millions of daily commuters travel smoothly without confusion, transit engineers design highly specialized schematic "
            "network maps. Instead of depicting actual curved geographical terrain, a transit map uses simplified straight lines, bold "
            "distinct colors, and clear standardized symbols. Each major subway route is represented by a unique vivid color: the Yellow "
            "Line connects northern districts to southern tech corridors, the Blue Line crosses horizontally across east and west suburbs, "
            "the Red Line serves northern historical sectors, and the Violet Line links central heritage gates to southern industrial towns! "
            "Along these colorful transit corridors, specific stations feature circular ring symbols or interlocking dual circles. These "
            "are interchange stations, where passengers can step off one train and board a completely different line without leaving the "
            "station premises! For example, Kashmere Gate is a major triple-interchange hub connecting three different lines. Reading transit "
            "legends, identifying junction nodes, and recognizing line color codes enable students to navigate complex urban transportation "
            "systems independently, efficiently, and with total mathematical confidence."
        ),'''

s9_new = '''        "lecture": (
            "Modern bustling metropolitan cities across the world rely heavily on intricate public rapid transit networks, such as the famous "
            "world-class Delhi Metro! To help millions of daily commuters travel smoothly and comfortably without confusion, transit engineers "
            "design highly specialized schematic network maps. Instead of depicting actual curved geographical terrain, a modern transit map "
            "uses simplified straight lines, bold distinct colors, and clear standardized symbols that can be understood in seconds. Each major "
            "subway route is represented by a unique vivid color: the Yellow Line connects northern districts to southern tech corridors, the "
            "Blue Line crosses horizontally across bustling east and west suburbs, the Red Line serves northern historical sectors, and the "
            "Violet Line links central heritage gates to southern industrial towns! Along these colorful transit corridors, specific stations "
            "feature prominent circular ring symbols or interlocking dual circles. These are vital interchange stations, where passengers can "
            "step off one train and board a completely different line without leaving the station premises! For example, Kashmere Gate is a "
            "major triple-interchange hub connecting three different lines. Reading transit legends, identifying junction nodes, and recognizing "
            "color codes enable students to navigate complex urban transportation systems independently, efficiently, and with complete mathematical confidence."
        ),'''

# Slide 10
s10_old = '''        "lecture": (
            "When traveling across an interconnected metro rail network, passengers frequently discover multiple distinct routes to reach "
            "their destination. Selecting the optimal travel path requires calculating and comparing the total number of intermediate stations "
            "and line transfers! Suppose a student wishes to travel from Qutb Minar station on the Yellow Line to Supreme Court station "
            "on the Blue Line. Let us evaluate two possible travel strategies. In Route A, the passenger rides the Yellow Line northward "
            "all the way to Rajiv Chowk interchange station, passing through thirteen stations, and then switches onto the Blue Line to "
            "travel two stops east to Supreme Court, totaling fifteen stops and one transfer. In Route B, the passenger rides just three "
            "stops to Hauz Khas, switches to the Magenta Line for five stops to Botanical Garden, and then transfers to the Blue Line heading "
            "west to Supreme Court! While Route B connects three lines, Route A requires only one single train transfer and significantly "
            "less walking across interchange corridors. Analyzing metro itineraries teaches students real-world mathematical optimization: "
            "we weigh total stop counts, transfer waiting times, and directional flow to choose the most efficient journey to our destination."
        ),'''

s10_new = '''        "lecture": (
            "When traveling across an interconnected modern metro rail network, passengers frequently discover multiple distinct routes to "
            "reach their intended destination. Selecting the truly optimal travel path requires calculating and comparing the total number "
            "of intermediate stations, line transfers, and walking distances! Suppose a student wishes to travel from Qutb Minar station on the "
            "Yellow Line to Supreme Court station on the Blue Line. Let us evaluate two possible travel strategies. In Route A, the passenger "
            "rides the Yellow Line northward all the way to Rajiv Chowk interchange station, passing through thirteen stations, and then "
            "switches onto the Blue Line to travel two stops east to Supreme Court, totaling fifteen stops and only one transfer. In Route B, "
            "the passenger rides just three stops to Hauz Khas, switches to the Magenta Line for five stops to Botanical Garden, and then transfers "
            "to the Blue Line heading west to Supreme Court! While Route B connects three lines, Route A requires only one single train transfer "
            "and significantly less walking across crowded interchange corridors. Analyzing metro itineraries teaches students real-world "
            "mathematical optimization: we weigh total stop counts, transfer waiting times, and directional flow to choose the most efficient journey."
        ),'''

# Slide 11
s11_old = '''        "lecture": (
            "When creating a detailed map of our own school campus, drawing every single leaf, brick, and doorway realistically would "
            "make the paper overcrowded, messy, and impossible to decipher! Professional cartographers solve this challenge by inventing "
            "a standardized map key, also known as a map legend. A map key replaces complex physical structures with clean, intuitive geometric "
            "symbols. Let us examine the official school cartography palette! A sturdy solid rectangle represents the main school Building; "
            "a double parallel gap indicates the grand Entrance Gate; a small circle with a cross stands for the clean Water Tank; a dashed "
            "boundary line denotes the outer Security Fence; a solid thick outline marks the brick Boundary Wall; a dotted winding strip "
            "traces the gravel Footpath; a tiny brown rectangle represents a garden Bench; a flowering cluster symbolizes the Botanical Garden; "
            "and a cheerful green canopy icon marks an ancient Banyan Tree! By assigning a distinct, unmistakable symbol to each real-world "
            "feature, anyone holding the school map can immediately identify locations, calculate distances, and explore the campus grounds "
            "with effortless clarity, consistency, and spatial accuracy."
        ),'''

s11_new = '''        "lecture": (
            "When creating a detailed map of our own school campus, drawing every single leaf, brick, and classroom doorway realistically "
            "would make the paper overcrowded, confusing, and impossible to decipher! Professional cartographers solve this challenge by "
            "inventing a standardized map key, which is also commonly called a map legend. A map key replaces complex physical structures with "
            "clean, intuitive geometric symbols and vivid colors. Let us examine the official school cartography palette! A sturdy solid "
            "rectangle represents the main school Building; a double parallel gap indicates the grand Entrance Gate; a small circle with a "
            "cross stands for the clean drinking Water Tank; a dashed boundary line denotes the outer Security Fence; a solid thick outline "
            "marks the brick Boundary Wall; a dotted winding strip traces the gravel Footpath; a tiny brown rectangle represents a garden Bench; "
            "a flowering cluster symbolizes the Botanical Garden; and a cheerful green canopy icon marks an ancient Banyan Tree! By assigning "
            "a distinct, unmistakable symbol to each real-world feature, anyone holding the school map can immediately identify locations, "
            "calculate distances, and explore the campus grounds with effortless clarity, consistency, and spatial accuracy."
        ),'''

# Slide 12
s12_old = '''        "lecture": (
            "One of the most thrilling mathematical applications of campus cartography is organizing an interactive outdoor treasure hunt! "
            "In this lively game, a team of young explorers hides secret numbered clue tokens across the school grounds and marks their exact "
            "locations on a master campus map using colored flags and coordinates. To discover the hidden treasure, another team of students "
            "must carefully interpret the map legend, establish cardinal orientation from the central courtyard flagpole, and follow precise "
            "navigational directions. Clue one directs the seekers: 'Start at the main gate, walk thirty paces East along the perimeter wall, "
            "and inspect the base of the tallest banyan tree.' Consulting their map key, the searchers identify the banyan tree symbol, "
            "verify its eastern bearing with their compass, and locate the first silver token nestled in its aerial roots! Clue two instructs: "
            "'Now head forty paces North past the herbal garden to the eastern corner of the water tank.' By systematically connecting cardinal "
            "headings, pacing distances, and map icons, the searchers solve the puzzle without taking a single wrong turn! Treasure hunts prove "
            "that spatial navigation is both an exact mathematical science and an exhilarating real-world adventure."
        ),'''

s12_new = '''        "lecture": (
            "One of the most thrilling mathematical applications of campus cartography is organizing an interactive outdoor treasure hunt! "
            "In this lively game, a team of young explorers hides secret numbered clue tokens across the school grounds and marks their exact "
            "locations on a master campus map using colored flags and coordinates. To discover the hidden treasure, another team of students "
            "must carefully interpret the map legend, establish cardinal orientation from the central courtyard flagpole, and follow precise "
            "navigational directions across the campus. Clue one directs the seekers: 'Start at the main gate, walk thirty paces East along the "
            "perimeter wall, and inspect the base of the tallest banyan tree.' Consulting their map key, the searchers identify the banyan tree "
            "symbol, verify its eastern bearing with their magnetic compass, and locate the first silver token nestled safely in its aerial roots! "
            "Clue two instructs: 'Now head forty paces North past the herbal garden to the eastern corner of the water tank.' By systematically "
            "connecting cardinal headings, pacing distances, and map icons, the searchers solve the puzzle without taking a single wrong turn! "
            "Treasure hunts prove that spatial navigation is both an exact mathematical science and an exhilarating real-world adventure."
        ),'''

# Slide 13
s13_old = '''        "lecture": (
            "Inside a bustling corner of the zoological park, an industrious ant departs from its underground anthill on an important "
            "foraging expedition! To trace the ant's precise movements, entomologists and mathematicians record its trajectory along a standard "
            "one-centimetre square grid paper. The anthill sits at the bottom-left origin. Scattered across the grid are four delicious "
            "food treats: a golden sweet laddoo, sugar crystals, a slice of bakery bread, and a crunchy red apple slice. Let us trace the "
            "ant's journey to the laddoo! From the anthill, the ant crawls two centimetres East along the bottom grid line. Next, it makes a "
            "sharp ninety-degree turn and crawls three centimetres North, reaching the golden laddoo! Recording this route in formal direction "
            "shorthand, we write: two centimetres East, three centimetres North. What if the ant then travels from the laddoo to the sugar "
            "crystals? It crawls four centimetres East and two centimetres North. By breaking continuous physical journeys into discrete "
            "centimetre segments aligned with cardinal axes, students connect geometric grid lines with coordinate distances, turning complex "
            "organic animal pathways into clean, quantifiable mathematical vectors."
        ),'''

s13_new = '''        "lecture": (
            "Inside a bustling corner of the zoological park, an industrious ant departs from its underground anthill on an important daily "
            "foraging expedition! To trace the ant's precise movements across the terrain, entomologists and mathematicians record its exact "
            "trajectory along a standard one-centimetre square grid paper. The anthill sits at the bottom-left origin point. Scattered across "
            "the grid are four delicious food treats: a golden sweet laddoo, sparkling sugar crystals, a slice of bakery bread, and a crunchy "
            "red apple slice. Let us trace the ant's journey to the laddoo! From the anthill, the ant crawls two centimetres East along the "
            "bottom grid line. Next, it makes a sharp ninety-degree turn and crawls three centimetres North, reaching the golden laddoo! "
            "Recording this route in formal direction shorthand, we write: two centimetres East, three centimetres North. What if the ant then "
            "travels from the laddoo to the sugar crystals? It crawls four centimetres East and two centimetres North. By breaking continuous "
            "physical journeys into discrete centimetre segments aligned with cardinal axes, students connect geometric grid lines with coordinate "
            "distances, turning complex organic animal pathways into clean, quantifiable mathematical vectors and reliable navigational tracks."
        ),'''

# Slide 16
s16_old = '''        "lecture": (
            "Let us apply our coordinate mastery to complete a comprehensive cartographic survey of the national zoological park! "
            "Across our numbered twelve-by-twelve grid system, various beloved wildlife species live in spacious natural habitats. "
            "Let us locate each animal with mathematical exactness! Near the bottom-left entrance, the Giant Panda resides at coordinate (1, 1). "
            "Moving eastward along row one, we find the Giant Tortoise basking peacefully at coordinate (4, 1). Continuing further east "
            "and slightly north, the spotted Deer grazes in an open meadow at coordinate (8, 3). In the central wetland lagoon, the saltwater "
            "Crocodile rests on a sandy bank at coordinate (7, 6). High up in the north-western forest sector, the majestic Lion guards its "
            "rocky den at coordinate (3, 10). And near the top-right sanctuary border, the Asian Elephant family drinks from a deep pool at "
            "coordinate (11, 11)! Notice how each animal's unique ordered pair specifies its exact spatial address with zero ambiguity. "
            "By plotting color-coded dots at intersection vertices, cartographers, wildlife biologists, and visitors maintain perfect spatial "
            "records. You now possess the complete geometric language of maps, cardinal directions, and coordinate systems to navigate the world."
        ),'''

s16_new = '''        "lecture": (
            "Let us apply our coordinate mastery to complete a comprehensive cartographic survey of the national zoological park! Across our "
            "numbered twelve-by-twelve grid system, various beloved wildlife species live in spacious natural habitats designed to mimic their "
            "native environments. Let us locate each animal with mathematical exactness! Near the bottom-left entrance, the Giant Panda resides "
            "at coordinate (1, 1). Moving eastward along row one, we find the Giant Tortoise basking peacefully at coordinate (4, 1). Continuing "
            "further east and slightly north, the spotted Deer grazes in an open meadow at coordinate (8, 3). In the central wetland lagoon, "
            "the saltwater Crocodile rests on a sandy bank at coordinate (7, 6). High up in the north-western forest sector, the majestic Lion "
            "guards its rocky den at coordinate (3, 10). And near the top-right sanctuary border, the Asian Elephant family drinks from a deep "
            "pool at coordinate (11, 11)! Notice how each animal's unique ordered pair specifies its exact spatial address with zero ambiguity. "
            "By plotting color-coded dots at intersection vertices, cartographers, wildlife biologists, and visitors maintain perfect spatial "
            "records. You now possess the complete geometric language of maps, cardinal directions, and coordinate systems to navigate our world."
        ),'''

for old, new, sid in [(s9_old, s9_new, 9), (s10_old, s10_new, 10), (s11_old, s11_new, 11), (s12_old, s12_new, 12), (s13_old, s13_new, 13), (s16_old, s16_new, 16)]:
    assert old in text, f"Slide {sid} old text not found"
    text = text.replace(old, new)

with open('.agents/generate_c5m_ch14_part2.py', 'w') as f:
    f.write(text)

