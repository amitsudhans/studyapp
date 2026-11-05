# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 11: Fun with Symmetry
Part 3: Slides 17 to 20 Data Generator (40 Quiz Questions)
Short headings: Challenge 1, Challenge 2, Challenge 3, Challenge 4.
Zero human names replaced with generic roles.
Clean Unicode throughout (×, ÷, °, +, -, =).
"""

def make_sol_html(steps, note=None):
    items = "".join(f"<li class='mb-2 text-slate-700 leading-relaxed'>{s}</li>" for s in steps)
    html = f"<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside space-y-1.5 text-sm'>{items}</ol></div>"
    if note:
        html += f"<div class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> {note}</div>"
    html += "</div>"
    return html

slides_part3 = [
    {
        "id": 17,
        "title": "Challenge 1",
        "section": "Ink Blots, Gliders & Paper Folding",
        "speech": "",
        "quizzes": [
            {
                "q": "When a folded sheet with wet paint is pressed and opened, what is the crease dividing the design called?",
                "options": ["Line of symmetry", "Diagonal hypotenuse", "Perimeter boundary", "Chord line"],
                "ans": 0,
                "hint": "It divides the artwork into two identical mirror halves.",
                "exp": "The crease is the line of symmetry (or mirror line).",
                "sol": make_sol_html([
                    "The paint is pressed between the two folded halves of the sheet.",
                    "Both halves receive matching paint imprints.",
                    "The central fold divides the design into two mirror halves.",
                    "Hence, this central line is termed the line of symmetry."
                ], "A line of symmetry divides a shape into two congruent mirror reflections.")
            },
            {
                "q": "Why does a paper airplane with identical wing sizes and fold angles fly straighter than an asymmetrical plane?",
                "options": ["It is heavier", "Equal wing geometry creates balanced aerodynamic lift on both sides", "It has more paper layers", "It flies faster"],
                "ans": 1,
                "hint": "Consider how air pushes against both wings equally during flight.",
                "exp": "Bilateral symmetry ensures balanced lift and drag, maintaining level flight.",
                "sol": make_sol_html([
                    "A symmetrical paper airplane has identical wing areas on the left and right.",
                    "When moving through the air, air resistance and lift are distributed evenly.",
                    "This balance prevents the airplane from tilting or rolling.",
                    "An asymmetrical plane experiences unbalanced lift, causing it to spiral and crash."
                ], "Symmetry in aerodynamics ensures balance and directional stability.")
            },
            {
                "q": "A square paper is folded in half once, and a triangular notch is cut on the fold. How many cutouts appear upon unfolding?",
                "options": ["1 cutout", "2 cutouts", "3 cutouts", "4 cutouts"],
                "ans": 0,
                "hint": "A cut on the crease line joins both sides together upon opening.",
                "exp": "A cut on the fold itself opens into a single symmetric shape (like a diamond).",
                "sol": make_sol_html([
                    "The cut is made directly along the fold line.",
                    "When unfolded, the two mirrored triangular halves join together across the fold.",
                    "They form one single, complete symmetric cutout (a rhombus or diamond)."
                ], "A cut directly on the crease joins across the fold to form a single centered shape.")
            },
            {
                "q": "A paper is folded in half twice (into 4 layers), and a hole is punched away from all folded edges. How many holes appear when unfolded?",
                "options": ["2 holes", "4 holes", "6 holes", "8 holes"],
                "ans": 1,
                "hint": "Each fold doubles the paper thickness and number of layers.",
                "exp": "Punching through 4 separate layers creates 4 symmetrical holes.",
                "sol": make_sol_html([
                    "Folding once in half creates 2 layers.",
                    "Folding in half a second time creates 4 layers.",
                    "Punching a single hole through 4 layers penetrates each layer independently.",
                    "When opened flat, exactly 4 holes appear, one in each quadrant."
                ], "Each fold doubles the number of layers and subsequent independent cutouts.")
            },
            {
                "q": "On a dot grid with a vertical line of symmetry, a point is located 3 units to the left. Where is its mirror reflection?",
                "options": ["3 units to the right along the same horizontal line", "3 units above the line", "6 units to the left", "On the mirror line"],
                "ans": 0,
                "hint": "Symmetry requires equal perpendicular distance from the line.",
                "exp": "Reflected points maintain equal perpendicular distance on the opposite side.",
                "sol": make_sol_html([
                    "The mirror line is vertical.",
                    "Perpendicular distance from the line is 3 units to the left.",
                    "The corresponding reflection must lie at the same perpendicular distance of 3 units to the right.",
                    "The vertical height (row) remains unchanged."
                ], "Reflection preserves perpendicular distance from the line of symmetry.")
            },
            {
                "q": "If a line segment starts on the line of symmetry at distance 0 and ends 5 units to the left, what does its reflection look like?",
                "options": ["A segment starting at distance 0 and ending 5 units to the right", "A circle of radius 5", "A vertical line", "A point"],
                "ans": 0,
                "hint": "The point on the fold line remains fixed in place.",
                "exp": "The start point on the mirror line stays fixed; the end point reflects 5 units to the right.",
                "sol": make_sol_html([
                    "The starting point lies on the line of symmetry, so its reflection is itself.",
                    "The ending point is 5 units to the left, so its reflection is 5 units to the right.",
                    "Connecting the fixed start to the reflected end creates a matching symmetrical segment."
                ], "Points on the line of symmetry are invariant under reflection.")
            },
            {
                "q": "How many lines of symmetry does a plain, blank circular piece of paper have?",
                "options": ["1 line", "2 lines", "4 lines", "Infinite lines (any diameter)"],
                "ans": 3,
                "hint": "Consider folding the circle across any line passing through its center.",
                "exp": "Any diameter passing through the center of a circle serves as a line of symmetry.",
                "sol": make_sol_html([
                    "A circle is completely rotationally and reflectionally symmetric.",
                    "Folding a circle along any diameter folds one semicircle onto the other.",
                    "Because there are infinitely many diameters passing through the center, a circle has infinite lines of symmetry."
                ], "Every straight line passing through the center of a circle is a line of symmetry.")
            },
            {
                "q": "A student folds a square paper along its diagonal. How many lines of symmetry does a square have in total?",
                "options": ["2 lines", "4 lines", "6 lines", "8 lines"],
                "ans": 1,
                "hint": "Check folds through side midpoints as well as corner diagonals.",
                "exp": "A square has 4 lines of symmetry: 2 through side midpoints and 2 along diagonals.",
                "sol": make_sol_html([
                    "Folding horizontally down the center gives 1 line of symmetry.",
                    "Folding vertically down the center gives 1 line of symmetry.",
                    "Folding along the top-left to bottom-right diagonal gives 1 line of symmetry.",
                    "Folding along the top-right to bottom-left diagonal gives 1 line of symmetry.",
                    "Total = 1 + 1 + 1 + 1 = 4 lines of symmetry."
                ], "A regular 4-sided polygon (square) has exactly 4 lines of symmetry.")
            },
            {
                "q": "If you cut a heart shape from paper, along which line must you fold it so both halves match?",
                "options": ["A horizontal line across the middle", "A vertical line down the center crease", "A diagonal line across one lobe", "No line works"],
                "ans": 1,
                "hint": "Notice that the bottom comes to a single sharp point.",
                "exp": "A heart has bilateral symmetry across a single vertical centerline.",
                "sol": make_sol_html([
                    "The top has two rounded lobes and the bottom has a single pointed tip.",
                    "Folding vertically down the center aligns the left lobe onto the right lobe.",
                    "Folding horizontally does not align, because the top is curved and the bottom is pointed.",
                    "Thus, a heart possesses exactly 1 vertical line of symmetry."
                ], "A standard heart shape has 1 vertical line of symmetry.")
            },
            {
                "q": "Which of the following geometric tools is best used to verify if a drawn shape has mirror symmetry?",
                "options": ["A small flat upright mirror placed along the fold", "A heavy hammer", "A thermometer", "A stopwatch"],
                "ans": 0,
                "hint": "This optical tool shows reflections instantly without cutting paper.",
                "exp": "Placing a flat mirror along the proposed fold reveals if the reflection recreates the original shape.",
                "sol": make_sol_html([
                    "When placed upright along a proposed line of symmetry, a mirror reflects the front half.",
                    "If the reflection combined with the visible half looks identical to the whole shape, the line is a true line of symmetry."
                ], "A mirror test provides immediate visual verification of reflectional symmetry.")
            }
        ]
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "section": "Mirrors, Ambulances & Geometric Reconstruction",
        "speech": "",
        "quizzes": [
            {
                "q": "Why does a flat mirror reverse left and right (lateral inversion) but not top and bottom?",
                "options": ["Because gravity pulls downwards", "Because it reverses the direction perpendicular to the mirror surface (front-to-back inversion)", "Because light is colored", "Because human eyes are round"],
                "ans": 1,
                "hint": "Think about looking straight into a glass mirror.",
                "exp": "Mirrors reverse the axis perpendicular to their surface, which our brain interprets as a left-right swap.",
                "sol": make_sol_html([
                    "A flat mirror reflects light straight back along the perpendicular axis.",
                    "Points closer to the mirror appear closer in the reflection.",
                    "This front-to-back reversal makes our left hand appear as the reflection's right hand.",
                    "Vertical positions remain aligned because the mirror does not flip up and down."
                ], "Lateral inversion is a perceptual interpretation of front-to-back mirror reflection.")
            },
            {
                "q": "Which of the following numbers reads identically in a vertical mirror?",
                "options": ["808", "123", "456", "789"],
                "ans": 0,
                "hint": "Check which digits have vertical symmetry and read same backwards.",
                "exp": "Digits '8' and '0' possess vertical symmetry, and 808 is a palindrome.",
                "sol": make_sol_html([
                    "Examine each digit: '8' has vertical symmetry, '0' has vertical symmetry.",
                    "The sequence is 8-0-8.",
                    "In a vertical mirror, the first 8 reflects to the last position, the center 0 stays in the center, and the last 8 reflects to the first position.",
                    "The reflected number still reads 808."
                ], "Palindromes formed of vertically symmetric glyphs reflect identically.")
            },
            {
                "q": "Which capital letter has BOTH horizontal and vertical lines of symmetry?",
                "options": ["A", "B", "H", "C"],
                "ans": 2,
                "hint": "Test folding this letter both vertically and horizontally.",
                "exp": "The letter 'H' can be folded horizontally or vertically into matching halves.",
                "sol": make_sol_html([
                    "'A' has only 1 vertical line of symmetry.",
                    "'B' and 'C' have only 1 horizontal line of symmetry.",
                    "'H' has 1 vertical line (down the crossbar) and 1 horizontal line (along the crossbar).",
                    "Hence, 'H' possesses both horizontal and vertical symmetry."
                ], "Letters like H, I, O, and X possess dual lines of symmetry.")
            },
            {
                "q": "How does the word 'AMBULANCE' appear when viewed through a driver's rear-view mirror?",
                "options": ["In normal, correctly oriented letters (AMBULANCE)", "Upside down", "Completely blacked out", "Blurred into circles"],
                "ans": 0,
                "hint": "A rear-view mirror reflects already-reversed letters back to normal.",
                "exp": "The mirror laterally inverts the already-reversed letters, restoring normal readability.",
                "sol": make_sol_html([
                    "The lettering painted on the vehicle hood is pre-reversed.",
                    "The rear-view mirror applies a lateral inversion to what it sees.",
                    "Two consecutive reflections restore the original orientation.",
                    "The driver ahead sees 'AMBULANCE' reading normally from left to right."
                ], "Two reflections undo lateral inversion, restoring original orientation.")
            },
            {
                "q": "If you look at the word 'BED' in a vertical mirror, what happens to the letters?",
                "options": ["They read normally", "The letters reverse and face the opposite direction", "They turn into numbers", "They turn upside down"],
                "ans": 1,
                "hint": "Think about how B, E, and D face when turned around.",
                "exp": "Letters B, E, D do not possess vertical symmetry, so they face backwards.",
                "sol": make_sol_html([
                    "In a vertical mirror, the order of letters reverses from left to right.",
                    "Additionally, each individual letter is reflected horizontally.",
                    "'B', 'E', and 'D' all face backwards in the mirror image."
                ], "Asymmetrical letters flip laterally in vertical mirror reflections.")
            },
            {
                "q": "Which of the following words reads identically in a vertical mirror reflection?",
                "options": ["WOW", "CAT", "DOG", "FISH"],
                "ans": 0,
                "hint": "Check if each letter has vertical symmetry and forms a palindrome.",
                "exp": "'W' and 'O' have vertical symmetry, and 'WOW' is a palindrome.",
                "sol": make_sol_html([
                    "Check letter symmetry: W is vertically symmetrical, O is vertically symmetrical.",
                    "Check word order: 'W-O-W' is a palindrome (reads same backwards).",
                    "Therefore, the mirror reflection of WOW is WOW!"
                ], "Words like WOW, MOM, TOOT, and RADAR reflect identically when letters are symmetric.")
            },
            {
                "q": "When completing a symmetric drawing across a vertical axis, if an anchor point is at coordinate (5, 8), where should its reflection lie (assuming the axis is at x = 0)?",
                "options": ["(-5, 8)", "(5, -8)", "(-5, -8)", "(0, 8)"],
                "ans": 0,
                "hint": "Negate the horizontal distance while keeping vertical height identical.",
                "exp": "Reflection across x = 0 negates the x-coordinate while preserving the y-coordinate.",
                "sol": make_sol_html([
                    "The line of symmetry is the vertical line x = 0.",
                    "The x-distance is 5 units to the right.",
                    "Its reflection must be 5 units to the left, so x = -5.",
                    "The height y = 8 remains unchanged.",
                    "The reflected coordinate is (-5, 8)."
                ], "Reflection across a vertical axis flips x-coordinates: (x, y) -> (-x, y).")
            },
            {
                "q": "What is the mirror reflection of the digit '3' across a vertical line?",
                "options": ["The letter 'E' (or backward 3)", "The digit '8'", "The digit '0'", "The digit '3'"],
                "ans": 0,
                "hint": "The open curves flip to face the opposite direction.",
                "exp": "The curved arcs of 3 face left instead of right, resembling an 'E'.",
                "sol": make_sol_html([
                    "The digit 3 has open curves facing to the left and a flat back to the right.",
                    "Reflecting it horizontally across a vertical line reverses this orientation.",
                    "The curves now open to the right, resembling the capital letter 'E'."
                ], "The digit 3 lacks vertical symmetry and flips laterally under reflection.")
            },
            {
                "q": "How many lines of symmetry does a non-square rectangle have?",
                "options": ["1 line", "2 lines", "4 lines", "0 lines"],
                "ans": 1,
                "hint": "Try folding diagonally to see if the sides match.",
                "exp": "A non-square rectangle has 2 lines of symmetry (connecting opposite midpoints).",
                "sol": make_sol_html([
                    "Folding along the vertical line connecting top and bottom midpoints matches the halves.",
                    "Folding along the horizontal line connecting left and right midpoints matches the halves.",
                    "Folding along a diagonal does NOT match the sides, because adjacent sides have different lengths.",
                    "Total = 2 lines of symmetry."
                ], "A rectangle has 2 lines of symmetry; diagonals are NOT lines of symmetry for non-squares.")
            },
            {
                "q": "Which shape has exactly 1 line of symmetry?",
                "options": ["An isosceles triangle (with 2 equal sides)", "An equilateral triangle", "A rectangle", "A circle"],
                "ans": 0,
                "hint": "Only two sides of this triangle are of equal length.",
                "exp": "An isosceles triangle has only 1 line of symmetry running down the apex between the equal sides.",
                "sol": make_sol_html([
                    "An equilateral triangle has 3 lines of symmetry.",
                    "A rectangle has 2 lines of symmetry.",
                    "A circle has infinitely many lines of symmetry.",
                    "An isosceles triangle has exactly 1 line of symmetry connecting the apex to the base midpoint."
                ], "Isosceles triangles possess exactly 1 line of bilateral symmetry.")
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "section": "Polygons, Angles & Tessellation Rules",
        "speech": "",
        "quizzes": [
            {
                "q": "How many lines of symmetry does an equilateral triangle have?",
                "options": ["1 line", "2 lines", "3 lines", "6 lines"],
                "ans": 2,
                "hint": "All three sides and angles are identical.",
                "exp": "An equilateral triangle has 3 lines of symmetry passing through each vertex.",
                "sol": make_sol_html([
                    "All three sides and all three angles (60°) are equal.",
                    "A line from each vertex to the opposite midpoint divides the triangle into matching halves.",
                    "Since there are 3 vertices, there are exactly 3 lines of symmetry."
                ], "Regular polygons with n sides have exactly n lines of symmetry.")
            },
            {
                "q": "How many lines of symmetry does a regular pentagon (5 equal sides) have?",
                "options": ["3 lines", "4 lines", "5 lines", "10 lines"],
                "ans": 2,
                "hint": "In regular polygons, the lines of symmetry equal the number of sides.",
                "exp": "A regular pentagon has 5 lines of symmetry, one through each vertex.",
                "sol": make_sol_html([
                    "A regular pentagon has 5 equal sides and 5 equal angles (108°).",
                    "A line connecting each vertex to the midpoint of the opposite side bisects the figure.",
                    "With 5 vertices, there are exactly 5 lines of symmetry."
                ], "The rule for regular polygons: n sides = n lines of symmetry.")
            },
            {
                "q": "What is the sum of corner angles that must meet around a shared vertex for shapes to tessellate seamlessly?",
                "options": ["180°", "270°", "360°", "540°"],
                "ans": 2,
                "hint": "A complete rotation around a single point equals 360 degrees.",
                "exp": "Angles around a complete point on a flat plane must sum to exactly 360°.",
                "sol": make_sol_html([
                    "A complete turn around a point in a plane is 360 degrees.",
                    "For tiles to fit together without gaps or overlaps, the sum of their corner angles meeting at every vertex must be exactly 360°."
                ], "Planar tessellation requires vertex angles to sum to 360°.")
            },
            {
                "q": "Why can regular hexagons tessellate a floor by themselves without any other shapes?",
                "options": ["Their interior angles are 120°, and 3 × 120° = 360°", "They have 6 sides", "They are larger than squares", "They are round"],
                "ans": 0,
                "hint": "Each corner angle is 120 degrees: 3 × 120° = 360°.",
                "exp": "Three 120° angles meet at every vertex to sum to exactly 360°.",
                "sol": make_sol_html([
                    "The interior angle of a regular hexagon is 120 degrees.",
                    "When three hexagons meet at a common vertex: 120° + 120° + 120° = 360°.",
                    "Since 360° is completely filled, they tile the plane with zero gaps, just like honeycombs!"
                ], "Regular hexagons form one of the three regular tessellations of the plane.")
            },
            {
                "q": "Why can regular pentagons NOT tessellate a plane alone?",
                "options": ["Their interior angle is 108°, and 360° is not divisible by 108°", "They are too small", "They have odd sides", "They are curved"],
                "ans": 0,
                "hint": "Each angle is 108 degrees, which does not divide 360 degrees evenly.",
                "exp": "3 × 108° = 324° (leaving a 36° gap) and 4 × 108° = 432° (causing an overlap).",
                "sol": make_sol_html([
                    "Each interior angle of a regular pentagon is 108°.",
                    "Three pentagons give: 3 × 108° = 324°, which leaves a 36° gap.",
                    "Four pentagons give: 4 × 108° = 432°, which overlaps by 72°.",
                    "Since 360 is not a multiple of 108, regular pentagons cannot tile alone."
                ], "Shapes whose interior angles do not evenly divide 360° cannot form monohedral tessellations.")
            },
            {
                "q": "In tile geometry, what is the motion called when a tile is shifted in a straight line without rotation or reflection?",
                "options": ["Translation (slide)", "Rotation (turn)", "Reflection (flip)", "Dilation (resize)"],
                "ans": 0,
                "hint": "Shifting an object in a straight line without turning it.",
                "exp": "A translation moves every point of an object by the same distance in the same direction.",
                "sol": make_sol_html([
                    "Moving an object along a straight path without changing its size or orientation is a translation (slide).",
                    "Turning around a point is a rotation.",
                    "Flipping across an axis is a reflection."
                ], "Translation preserves size, shape, and orientation.")
            },
            {
                "q": "What motion turns a tile around a fixed pivot point by 90° or 180°?",
                "options": ["Rotation", "Translation", "Reflection", "Extrusion"],
                "ans": 0,
                "hint": "Spinning an object around a center pivot point.",
                "exp": "Rotating turns an object around a central pivot point.",
                "sol": make_sol_html([
                    "Rotating means spinning a shape around a fixed center point.",
                    "A 90° turn is a quarter-turn, while a 180° turn is a half-turn.",
                    "The shape changes its directional orientation while remaining in place."
                ], "Rotation preserves shape and size while altering angular orientation.")
            },
            {
                "q": "What is the difference between a 'standing' tile and a 'sleeping' tile in masonry?",
                "options": ["A standing tile is oriented vertically; a sleeping tile is oriented horizontally", "One is broken and one is whole", "One is made of wood", "One is painted blue"],
                "ans": 0,
                "hint": "Think about vertical upright vs horizontal flat positions.",
                "exp": "Standing refers to vertical orientation; sleeping refers to horizontal orientation.",
                "sol": make_sol_html([
                    "In descriptive craft vocabulary, oblong rectangular tiles are classified by orientation.",
                    "A vertically placed brick or tile is described as 'standing'.",
                    "A horizontally laid brick or tile is described as 'sleeping'."
                ], "Colloquial craft terms describe vertical vs horizontal tile orientations.")
            },
            {
                "q": "How many regular polygons can tessellate a flat surface alone?",
                "options": ["Only 3 (equilateral triangle, square, regular hexagon)", "Only 1", "5 shapes", "All polygons"],
                "ans": 0,
                "hint": "Check shapes whose corner angles evenly divide 360 degrees.",
                "exp": "Only triangles (60°), squares (90°), and hexagons (120°) have interior angles that divide 360°.",
                "sol": make_sol_html([
                    "For a regular polygon with interior angle A to tile alone, 360° ÷ A must be an integer.",
                    "Equilateral triangle: A = 60° (360 ÷ 60 = 6 tiles per vertex).",
                    "Square: A = 90° (360 ÷ 90 = 4 tiles per vertex).",
                    "Regular hexagon: A = 120° (360 ÷ 120 = 3 tiles per vertex).",
                    "No other regular polygon has an interior angle that evenly divides 360°."
                ], "There are exactly three regular tessellations in Euclidean geometry.")
            },
            {
                "q": "How many lines of symmetry does a scalene triangle have?",
                "options": ["0 lines", "1 line", "2 lines", "3 lines"],
                "ans": 0,
                "hint": "None of the sides or angles in this triangle are equal.",
                "exp": "All sides and angles in a scalene triangle are unequal, so it has zero lines of symmetry.",
                "sol": make_sol_html([
                    "A scalene triangle has three distinct side lengths and three distinct angle measures.",
                    "Folding along any line through any vertex fails to align the unequal sides.",
                    "Therefore, a scalene triangle has 0 lines of symmetry."
                ], "Scalene triangles are completely asymmetrical.")
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "section": "Custom Tiles, Catty Walls & Nature Art",
        "speech": "",
        "quizzes": [
            {
                "q": "When creating a custom tile, if you cut a shape from the left edge and tape it to the right edge, why does the tile still tessellate?",
                "options": ["Because the projection on the right perfectly fits the recess on the left of the next tile", "Because the paper is stretchy", "Because glue expands", "It does not tessellate"],
                "ans": 0,
                "hint": "The piece removed from one side fills the gap on the adjacent tile.",
                "exp": "Translating edge modifications creates complementary interlocking edges.",
                "sol": make_sol_html([
                    "Every tile in the pattern has a hollow recess on its left edge.",
                    "Every tile has an identical jutting protrusion on its right edge.",
                    "When placed side-by-side, the protrusion of one tile nestles exactly into the recess of the neighbor.",
                    "This forms a continuous, seamless interlocking tessellation."
                ], "Translational modification creates interlocking Escher-style tessellating tiles.")
            },
            {
                "q": "What happens to the area of a square tile when a piece is cut from one edge and taped onto the opposite edge?",
                "options": ["The area remains exactly conserved (unchanged)", "The area increases by 50%", "The area decreases to zero", "The area doubles"],
                "ans": 0,
                "hint": "The shape cut from one side is reattached to the other side.",
                "exp": "Area is conserved: Area_final = Area_initial - Area_cut + Area_cut = Area_initial.",
                "sol": make_sol_html([
                    "Let the original square have area A.",
                    "A small piece of area c is removed from one side: A - c.",
                    "That exact piece is attached to the opposite side: (A - c) + c = A.",
                    "The net area remains identical to the original square."
                ], "Area conservation is a fundamental property of cutting and translating shapes.")
            },
            {
                "q": "In the 'catty wall' project, what shape is cut from the top edge of the square paper to create the ears?",
                "options": ["A curved downward crescent (forming ears on the corners and a chin when attached below)", "A large square", "A circle from the middle", "A straight horizontal slit"],
                "ans": 0,
                "hint": "A curved shape cut from between the top corners leaves two sharp ears.",
                "exp": "Cutting a downward crescent between the top corners leaves two pointy ears and forms the chin when taped below.",
                "sol": make_sol_html([
                    "Cutting downward into the top edge leaves two sharp corners at the top (the cat ears).",
                    "The removed crescent is taped to the bottom edge.",
                    "The curved protrusion at the bottom represents the chin of the cat.",
                    "The chin of the upper tile fits right between the ears of the lower tile!"
                ], "Top-to-bottom translation ensures vertical interlocking of cat tiles.")
            },
            {
                "q": "Which part of a peepal or mango leaf functions as an organic line of symmetry in nature?",
                "options": ["The central midrib vein", "The outer tooth of the margin", "The petiole stalk base", "The leaf tip"],
                "ans": 0,
                "hint": "Look at the thick central vein running from stem to tip.",
                "exp": "The central midrib divides the leaf blade into matching left and right halves.",
                "sol": make_sol_html([
                    "The central vein running down the middle of a leaf is called the midrib.",
                    "Secondary lateral veins branch off the midrib at matching angles on both sides.",
                    "Folding the leaf along the midrib brings both halves into close alignment.",
                    "Thus, the midrib serves as the organic line of symmetry."
                ], "The midrib is nature's botanical line of bilateral symmetry.")
            },
            {
                "q": "What type of symmetry do animals like butterflies, tigers, and birds display across their body axis?",
                "options": ["Bilateral symmetry (left and right mirror reflection)", "Radial symmetry", "Rotational symmetry", "Spherical symmetry"],
                "ans": 0,
                "hint": "Left and right sides mirror each other across a central body axis.",
                "exp": "Bilateral symmetry divides an animal's body into mirrored left and right halves.",
                "sol": make_sol_html([
                    "Most animals that move actively have a distinct head, tail, left side, and right side.",
                    "A single vertical plane dividing the body from head to tail creates two mirror halves.",
                    "This is termed bilateral symmetry (two-sided symmetry)."
                ], "Bilateral symmetry is the primary body plan of birds, insects, and mammals.")
            },
            {
                "q": "Which of the following flowers exhibits radial symmetry (symmetry radiating around a central core)?",
                "options": ["A marigold or sunflower", "A curved pea flower", "An asymmetrical orchid", "A snapdragon"],
                "ans": 0,
                "hint": "Petals radiate outward equally from a central core like wheel spokes.",
                "exp": "Sunflowers have identical petals radiating around a central disc, possessing multiple lines of symmetry.",
                "sol": make_sol_html([
                    "Radial symmetry means multiple planes of symmetry pass through a central axis.",
                    "A marigold or sunflower has circular symmetry with petals radiating outward evenly like wheel spokes.",
                    "Folding along any diameter produces matching halves."
                ], "Radial symmetry in flowers allows petals to attract pollinators from all directions.")
            },
            {
                "q": "How can you create a leaf-imprint art design with perfect symmetry on paper?",
                "options": ["Paint a leaf, press it on one side of a folded crease, and fold the other half over to print", "Throw paint at a wall", "Trace a leaf in the dark", "Cut the leaf into confetti"],
                "ans": 0,
                "hint": "Folding wet painted paper transfers an exact mirror impression.",
                "exp": "Folding painted paper across a central crease stamps a mirror reflection across the crease.",
                "sol": make_sol_html([
                    "Fold a sheet of paper to create a central line of symmetry.",
                    "Apply paint to the textured vein side of a leaf.",
                    "Press the leaf on one side of the fold.",
                    "Fold the opposite half of the paper over and press firmly.",
                    "Opening the paper reveals two identical mirrored leaf imprints!"
                ], "Pressing wet paint across a fold stamps an exact mirror reflection.")
            },
            {
                "q": "What is a key benefit of a staggered running bond floor tile pattern over a stacked grid?",
                "options": ["It staggers seams, preventing long continuous crack lines and improving strength", "It requires zero tiles", "It makes the room colder", "It curves the floor"],
                "ans": 0,
                "hint": "Staggered seams break continuous lines of stress across the floor.",
                "exp": "Staggered seams prevent cracks from propagating in a straight line across the floor.",
                "sol": make_sol_html([
                    "In a stacked grid, all seams run continuously in straight horizontal and vertical lines.",
                    "Stress or settling can cause cracks to travel directly down the long seam.",
                    "In a running bond pattern, vertical seams end at the solid center of neighboring tiles.",
                    "This interlocking arrangement distributes mechanical load and resists cracking."
                ], "Running bond patterns enhance mechanical durability and crack resistance.")
            },
            {
                "q": "Which of the following capital letters has NO line of symmetry at all?",
                "options": ["F", "A", "H", "M"],
                "ans": 0,
                "hint": "Check if any horizontal or vertical fold aligns the letter.",
                "exp": "The letter 'F' is asymmetrical; no horizontal or vertical line divides it into matching halves.",
                "sol": make_sol_html([
                    "'A' and 'M' have 1 vertical line of symmetry.",
                    "'H' has 2 lines of symmetry (horizontal and vertical).",
                    "'F' has horizontal bars on only one side and no matching opposite features.",
                    "Therefore, 'F' has 0 lines of symmetry."
                ], "Asymmetrical letters (like F, G, J, L, P, Q, R) possess no lines of symmetry.")
            },
            {
                "q": "Why is symmetry considered a fundamental bridge between art, mathematics, and nature?",
                "options": ["It unites visual balance and beauty with rigorous geometric rules and physical stability", "Because numbers are colorful", "Because paper is flat", "Because trees have leaves"],
                "ans": 0,
                "hint": "Symmetry connects natural balance, mathematical laws, and artistic design.",
                "exp": "Symmetry combines aesthetic elegance with mathematical invariance and physical balance.",
                "sol": make_sol_html([
                    "In nature, symmetry provides aerodynamic balance for birds and efficient growth for plants.",
                    "In architecture and art, symmetry creates visual harmony and structural stability.",
                    "In mathematics, symmetry provides precise rules of reflection, rotation, and tessellation.",
                    "Thus, symmetry is a unifying universal language."
                ], "Symmetry embodies the deep connection between geometric logic, natural law, and human art.")
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(slides_part3)} challenge slides.")
    total_q = sum(len(s['quizzes']) for s in slides_part3)
    print(f"Total quiz questions: {total_q}")
    assert len(slides_part3) == 4, "Must have exactly 4 slides"
    assert total_q == 40, "Must have exactly 40 quiz questions"
    for s in slides_part3:
        assert len(s["title"].split()) <= 3, f"Title {s['title']} has too many words"
        assert len(s["quizzes"]) == 10, f"Slide {s['id']} must have 10 questions"
        for q in s["quizzes"]:
            assert 0 <= q["ans"] < len(q["options"]), f"Invalid answer index in {q['q']}"
    print("All Part 3 challenge assertions passed successfully!")
