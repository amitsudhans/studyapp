# -*- coding: utf-8 -*-
"""NCERT Class 5 Mathematics — Chapter 11: Grandmother's Quilt Master Data"""

slides = [{'id': 1,
  'title': 'Quilt Perimeter',
  'tagline': "Outer Boundaries • Grandmother's Quilt Lace Border & Total Edge Length",
  'lecture': 'Welcome to the inspiring world of perimeter and area. Our journey begins with a heartwarming story from '
             "Preetha and Adrit's home. Their grandmother has just finished stitching a beautiful rectangular "
             'patchwork quilt made from soft cotton fabric scraps. To give the quilt a neat and festive finish, she '
             'wants to stitch a continuous decorative lace ribbon all the way around its outer edge. How can '
             'grandmother determine the exact length of lace ribbon she needs to buy from the market? She uses a '
             'measuring tape to measure each of the four outer edges: the top edge, the bottom edge, the left edge, '
             'and the right edge. When she adds these four side lengths together, she calculates what mathematicians '
             'call the perimeter. Perimeter is the total continuous distance around the outside boundary of any closed '
             'two-dimensional shape. If a quilt measures 200 centimetres in length and 150 centimetres in breadth, '
             'grandmother needs 200 plus 150 plus 200 plus 150 centimetres of lace ribbon, which equals 700 '
             'centimetres or 7 metres. Whether you are fencing a farming field, framing a family photograph, or '
             'running around a jogging track, you are always measuring perimeter along the outer boundary lines.',
  'content_html': '\n'
                  '        <div class="space-y-3 text-xs leading-relaxed text-slate-300">\n'
                  '            <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700">\n'
                  '                <h3 class="text-sm font-bold text-amber-400 mb-1">What is Perimeter?</h3>\n'
                  '                <p>The <strong>perimeter</strong> of any closed two-dimensional shape is the '
                  '<em>total path length</em> along its outer boundary edge. It is measured in linear units like '
                  'centimetres (cm) or metres (m).</p>\n'
                  '            </div>\n'
                  '            <div class="grid grid-cols-2 gap-2 font-mono">\n'
                  '                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">\n'
                  '                    <span class="text-cyan-400 font-bold block mb-1">Grandmother\'s Quilt:</span>\n'
                  '                    <p class="text-[11px] text-slate-300">Length = 200 cm, Breadth = 150 '
                  'cm.<br>Perimeter = 200 + 150 + 200 + 150 = 700 cm (7 m of lace ribbon needed).</p>\n'
                  '                </div>\n'
                  '                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">\n'
                  '                    <span class="text-emerald-400 font-bold block mb-1">Everyday '
                  'Boundaries:</span>\n'
                  '                    <p class="text-[11px] text-slate-300">• Fencing wire around a garden.<br">• '
                  'Picture frame around a canvas.<br">• Running track outer lane.</p>\n'
                  '                </div>\n'
                  '            </div>\n'
                  '        </div>\n'
                  '        ',
  'checkpoints': [{'id': 'cp1_1',
                   'question': 'What does the perimeter of a closed shape represent?',
                   'options': ['The total continuous length of its outer boundary',
                               'The flat surface region enclosed inside',
                               'The weight of the cardboard sheet',
                               'The number of corners inside the shape'],
                   'answer': 0,
                   'explanation': 'Perimeter is strictly the total length around the outer boundary edges of a closed '
                                  'figure.'},
                  {'id': 'cp1_2',
                   'question': 'If a rectangular quilt measures 3 metres in length and 2 metres in breadth, what is '
                               'its perimeter?',
                   'options': ['10 metres (3 + 2 + 3 + 2)', '6 metres (3 × 2)', '5 metres (3 + 2)', '12 metres'],
                   'answer': 0,
                   'explanation': 'Perimeter = Top + Bottom + Left + Right = 3 + 3 + 2 + 2 = 10 metres.'}]},
 {'id': 2,
  'title': 'Regular Polygons',
  'tagline': 'Equal-Sided Shapes • Equilateral Triangles, Squares & Hexagonal Perimeters',
  'lecture': 'When all the sides of a polygon are equal in length, mathematicians call it a regular polygon. '
             'Calculating the perimeter of regular polygons is delightfully fast and simple because you do not have to '
             'add each side individually. Instead, you can use multiplication! Consider an equilateral triangle, which '
             'has three identical sides. If each side measures 6 centimetres, its perimeter is simply 3 times 6 '
             'centimetres, which equals 18 centimetres. Next, consider a square, which has four identical sides. If '
             'each side of a square patch measures 8 centimetres, its perimeter is 4 times 8 centimetres, which equals '
             '32 centimetres. For a regular pentagon with five equal sides of 5 centimetres, the perimeter is 5 times '
             '5, or 25 centimetres. For a regular hexagon with six equal sides of 4 centimetres, the perimeter is 6 '
             'times 4, or 24 centimetres. The universal formula for any regular polygon with n equal sides is simply n '
             'multiplied by the length of one side. This shortcut saves enormous time when craftspersons construct '
             'hexagonal tile mosaics, star badges, and geometric quilt patches with matching borders, enabling '
             'builders to measure outer boundaries swiftly without repeatedly measuring each individual identical edge '
             'with a ruler.',
  'content_html': '\n'
                  '        <div class="space-y-3 text-xs leading-relaxed text-slate-300">\n'
                  '            <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700">\n'
                  '                <h3 class="text-sm font-bold text-amber-400 mb-1">Perimeter Formula for Regular '
                  'Polygons</h3>\n'
                  '                <p>For any regular polygon having <strong>n equal sides</strong> each of length '
                  '<strong>s</strong>:</p>\n'
                  '                <div class="p-2 rounded bg-slate-950 font-mono text-cyan-300 font-bold text-center '
                  'mt-2">\n'
                  '                    Perimeter = n × Side Length (s)\n'
                  '                </div>\n'
                  '            </div>\n'
                  '            <div class="grid grid-cols-3 gap-2 font-mono text-center">\n'
                  '                <div class="p-2 rounded bg-slate-900 border border-slate-800">\n'
                  '                    <span class="text-amber-300 font-bold block text-xs">Equilateral '
                  'Triangle</span>\n'
                  '                    <span class="text-cyan-300 font-bold block my-1">3 × s</span>\n'
                  '                    <span class="text-[10px] text-slate-400">3 equal sides</span>\n'
                  '                </div>\n'
                  '                <div class="p-2 rounded bg-slate-900 border border-slate-800">\n'
                  '                    <span class="text-amber-300 font-bold block text-xs">Square</span>\n'
                  '                    <span class="text-cyan-300 font-bold block my-1">4 × s</span>\n'
                  '                    <span class="text-[10px] text-slate-400">4 equal sides</span>\n'
                  '                </div>\n'
                  '                <div class="p-2 rounded bg-slate-900 border border-slate-800">\n'
                  '                    <span class="text-amber-300 font-bold block text-xs">Regular Hexagon</span>\n'
                  '                    <span class="text-cyan-300 font-bold block my-1">6 × s</span>\n'
                  '                    <span class="text-[10px] text-slate-400">6 equal sides</span>\n'
                  '                </div>\n'
                  '            </div>\n'
                  '        </div>\n'
                  '        ',
  'checkpoints': [{'id': 'cp2_1',
                   'question': 'What is the perimeter of a regular pentagon having side length of 7 cm?',
                   'options': ['35 cm (5 × 7 cm)', '28 cm (4 × 7 cm)', '49 cm (7 × 7 cm)', '12 cm (5 + 7 cm)'],
                   'answer': 0,
                   'explanation': 'A regular pentagon has 5 equal sides. Perimeter = 5 × 7 cm = 35 cm.'},
                  {'id': 'cp2_2',
                   'question': 'If a regular hexagon has a perimeter of 48 cm, what is the length of one side?',
                   'options': ['8 cm (48 ÷ 6)', '6 cm (48 ÷ 8)', '12 cm (48 ÷ 4)', '24 cm (48 ÷ 2)'],
                   'answer': 0,
                   'explanation': 'Side length = Perimeter ÷ Number of sides = 48 cm ÷ 6 = 8 cm.'}]},
 {'id': 3,
  'title': 'Drawing Rectangles',
  'tagline': 'Constrained Boundaries • Constructing Multiple Rectangles with a Fixed Target Perimeter',
  'lecture': 'Here is an intriguing mathematical puzzle: can multiple different rectangles share the exact same '
             'perimeter? Absolutely! Let us investigate how to draw distinct rectangles that all have a fixed target '
             'perimeter of 26 centimetres. Remember that the perimeter of a rectangle consists of two lengths and two '
             'breadths: two times length plus two times breadth equals 26 centimetres. If we divide 26 by 2, we '
             'discover a powerful secret: the sum of one length plus one breadth must always equal half the perimeter, '
             'which is 13 centimetres! Now, we simply find whole-number pairs that add up to 13. We can draw a long, '
             'narrow rectangle with a length of 12 centimetres and a breadth of 1 centimetre. We can draw a second '
             'rectangle with a length of 11 centimetres and a breadth of 2 centimetres. Other valid pairs include 10 '
             'and 3, 9 and 4, 8 and 5, or 7 and 6. Every single one of these different rectangles uses exactly 26 '
             'centimetres of lace ribbon around its edge! The half-perimeter strategy unlocks an entire family of '
             'shapes from a single boundary measurement, showing how one fixed piece of ribbon can enclose shapes with '
             'widely varying dimensions.',
  'content_html': '\n'
                  '        <div class="space-y-3 text-xs leading-relaxed text-slate-300">\n'
                  '            <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700">\n'
                  '                <h3 class="text-sm font-bold text-amber-400 mb-1">The Half-Perimeter Secret</h3>\n'
                  '                <p>Because Perimeter = 2 × (Length + Breadth), dividing the target perimeter by 2 '
                  'gives the sum of one length and one breadth:</p>\n'
                  '                <div class="p-2 rounded bg-slate-950 font-mono text-cyan-300 font-bold text-center '
                  'mt-2">\n'
                  '                    Length + Breadth = Perimeter ÷ 2\n'
                  '                </div>\n'
                  '            </div>\n'
                  '            <div class="overflow-x-auto">\n'
                  '                <table class="w-full text-left font-mono text-[11px] border border-slate-700">\n'
                  '                    <thead class="bg-slate-800 text-slate-300">\n'
                  '                        <tr>\n'
                  '                            <th class="p-1.5 border-b border-slate-700">Target Perimeter</th>\n'
                  '                            <th class="p-1.5 border-b border-slate-700">Half-Perimeter (L + '
                  'B)</th>\n'
                  '                            <th class="p-1.5 border-b border-slate-700">Distinct (Length, Breadth) '
                  'Combinations</th>\n'
                  '                        </tr>\n'
                  '                    </thead>\n'
                  '                    <tbody class="divide-y divide-slate-800">\n'
                  '                        <tr>\n'
                  '                            <td class="p-1.5 text-amber-300 font-bold">26 cm</td>\n'
                  '                            <td class="p-1.5 text-cyan-300">13 cm</td>\n'
                  '                            <td class="p-1.5 text-slate-200">(12, 1), (11, 2), (10, 3), (9, 4), (8, '
                  '5), (7, 6)</td>\n'
                  '                        </tr>\n'
                  '                        <tr>\n'
                  '                            <td class="p-1.5 text-amber-300 font-bold">18 cm</td>\n'
                  '                            <td class="p-1.5 text-cyan-300">9 cm</td>\n'
                  '                            <td class="p-1.5 text-slate-200">(8, 1), (7, 2), (6, 3), (5, 4)</td>\n'
                  '                        </tr>\n'
                  '                    </tbody>\n'
                  '                </table>\n'
                  '            </div>\n'
                  '        </div>\n'
                  '        ',
  'checkpoints': [{'id': 'cp3_1',
                   'question': 'If a rectangle has a perimeter of 18 cm, what must the sum of its length and breadth '
                               'equal?',
                   'options': ['9 cm (18 ÷ 2)', '18 cm', '36 cm', '4.5 cm'],
                   'answer': 0,
                   'explanation': 'Length + Breadth = Half-Perimeter = 18 cm ÷ 2 = 9 cm.'},
                  {'id': 'cp3_2',
                   'question': 'Which of the following (length, breadth) pairs produces a rectangle with a perimeter '
                               'of 26 cm?',
                   'options': ['Length = 10 cm, Breadth = 3 cm',
                               'Length = 10 cm, Breadth = 6 cm',
                               'Length = 13 cm, Breadth = 13 cm',
                               'Length = 5 cm, Breadth = 5 cm'],
                   'answer': 0,
                   'explanation': '10 + 3 = 13 cm. Perimeter = 2 × 13 cm = 26 cm.'}]},
 {'id': 4,
  'title': 'Area & Tiling',
  'tagline': 'Surface Coverage • Tessellation Without Gaps vs Circular Empty Spaces',
  'lecture': 'While perimeter measures the boundary ribbon running around a quilt, area measures something entirely '
             'different: the flat surface region enclosed inside the boundary! Area is defined as the amount of flat '
             'surface covered by a shape without any gaps or overlapping edges. To understand area deeply, imagine '
             "tiling a bathroom floor or assembling patchwork cloth blocks for grandmother's quilt. What shapes can "
             'tile a flat surface completely? If you use square cloth patches, they fit together seamlessly at every '
             'corner with zero gaps. Rectangular blocks and equilateral triangles also tile a surface flawlessly '
             'without leaving empty spots. However, try tiling a table surface with round circular coins or circular '
             'coasters! No matter how tightly you press circles together, tiny diamond-shaped empty gaps always remain '
             'between them. Circles cannot tile a flat plane completely! Polygons that fit together edge-to-edge '
             'without gaps create what mathematicians call a tessellation. Because squares tile perfectly without gaps '
             'or overlaps, the unit square was chosen as the universal standard unit for measuring area across '
             'science, design, and mathematics, allowing architects, builders, craftspersons, and landowners to '
             'quantify floor space, tile counts, carpet needs, and farming plots with absolute geometric clarity and '
             'precision.',
  'content_html': '\n'
                  '        <div class="space-y-3 text-xs leading-relaxed text-slate-300">\n'
                  '            <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700">\n'
                  '                <h3 class="text-sm font-bold text-amber-400 mb-1">What is Area?</h3>\n'
                  '                <p><strong>Area</strong> is the measure of the <em>flat surface region</em> '
                  'enclosed within a boundary, quantified by the number of unit shapes needed to cover it completely '
                  'without gaps or overlaps.</p>\n'
                  '            </div>\n'
                  '            <div class="grid grid-cols-2 gap-2 font-mono">\n'
                  '                <div class="p-2.5 rounded-lg bg-emerald-950/30 border border-emerald-800/40">\n'
                  '                    <span class="text-emerald-300 font-bold block mb-1">Shapes that Tile (Zero '
                  'Gaps):</span>\n'
                  '                    <p class="text-[11px] text-slate-300">• Squares (Standard unit!)<br">• '
                  'Rectangles<br">• Equilateral Triangles<br>• Regular Hexagons</p>\n'
                  '                </div>\n'
                  '                <div class="p-2.5 rounded-lg bg-rose-950/30 border border-rose-800/40">\n'
                  '                    <span class="text-rose-300 font-bold block mb-1">Shapes with Gaps:</span>\n'
                  '                    <p class="text-[11px] text-slate-300">• Circles & Ovals<br>• Irregular curved '
                  'shapes<br>Always leave empty diamond-like voids between contact points!</p>\n'
                  '                </div>\n'
                  '            </div>\n'
                  '        </div>\n'
                  '        ',
  'checkpoints': [{'id': 'cp4_1',
                   'question': 'What is the key difference between perimeter and area?',
                   'options': ['Perimeter measures outer boundary length; area measures enclosed flat surface',
                               'Perimeter is measured in square centimetres; area in linear metres',
                               'Perimeter applies only to circles; area applies only to squares',
                               'They are identical terms measuring the exact same quantity'],
                   'answer': 0,
                   'explanation': 'Perimeter is 1-dimensional boundary length; area is 2-dimensional surface '
                                  'coverage.'},
                  {'id': 'cp4_2',
                   'question': 'Why are squares chosen as the standard unit for measuring area instead of circles?',
                   'options': ['Squares pack together tightly leaving zero gaps or overlaps',
                               'Squares are colorful and circles are colorless',
                               'Circles are too heavy to hold on paper',
                               'Squares have no perimeter'],
                   'answer': 0,
                   'explanation': 'Squares tessellate a plane perfectly without leaving empty gaps, making them ideal '
                                  'standard units.'}]},
 {'id': 5,
  'title': 'Non-Standard Units',
  'tagline': 'Informal Area Benchmarks • Table Surface Covering & Triangular Patch Equivalence',
  'lecture': 'Before using standard square centimetres, students learn to measure and estimate surface areas using '
             'everyday classroom objects as non-standard units. For example, how many math textbooks are required to '
             'cover your study desk completely? You might lay out 6 textbooks neatly in 2 rows of 3, concluding that '
             'the desk has an area of 6 textbook units. You could also measure the same desk using pencil boxes or '
             'lunch boxes, discovering that smaller units yield a larger count to cover the same surface! In patchwork '
             'quilt design, grandmother uses geometric fabric tiles of different sizes. Consider a decorative mat '
             'filled with blue squares and green triangles. If you slice a 1 centimetre square along its diagonal, you '
             'produce two identical right-angled triangles. That means two small triangular patches equal the area of '
             'one full square patch! If a quilt design contains 10 blue squares and 8 green triangles, its total area '
             'in square units is 10 plus half of 8, which equals 10 plus 4, or 14 square units. Grouping partial units '
             'into whole units is the foundational stepping stone to rigorous area calculation, helping young '
             'mathematicians grasp fractional combinations before working with abstract algebraic formulas.',
  'content_html': '\n'
                  '        <div class="space-y-3 text-xs leading-relaxed text-slate-300">\n'
                  '            <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700">\n'
                  '                <h3 class="text-sm font-bold text-amber-400 mb-1">Composite Tile Equivalence</h3>\n'
                  '                <p>When measuring area with multi-shape tile sets, convert smaller non-standard '
                  'units into full square units:</p>\n'
                  '                <div class="p-2 rounded bg-slate-950 font-mono text-cyan-300 font-bold text-center '
                  'mt-2">\n'
                  '                    2 Half-Triangles = 1 Full Unit Square\n'
                  '                </div>\n'
                  '            </div>\n'
                  '            <div class="grid grid-cols-2 gap-2 font-mono">\n'
                  '                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">\n'
                  '                    <span class="text-amber-400 font-bold block mb-1">Desk Tiling Example:</span>\n'
                  '                    <p class="text-[11px] text-slate-300">Desk covered by: 12 Blue Squares + 6 '
                  'Green Triangles.<br>Area = 12 + (6 ÷ 2) = 12 + 3 = 15 square units.</p>\n'
                  '                </div>\n'
                  '                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">\n'
                  '                    <span class="text-cyan-400 font-bold block mb-1">Unit Size Principle:</span>\n'
                  '                    <p class="text-[11px] text-slate-300">Smaller non-standard units (e.g. pencil '
                  'boxes) require a higher count to cover the same table than larger units (e.g. textbooks).</p>\n'
                  '                </div>\n'
                  '            </div>\n'
                  '        </div>\n'
                  '        ',
  'checkpoints': [{'id': 'cp5_1',
                   'question': 'If two identical right-angled triangles combine to form one square tile, how many '
                               'triangles equal 5 square tiles?',
                   'options': ['10 triangles (5 × 2)', '7 triangles (5 + 2)', '2.5 triangles (5 ÷ 2)', '25 triangles'],
                   'answer': 0,
                   'explanation': 'Each square requires 2 triangles, so 5 squares require 5 × 2 = 10 triangles.'},
                  {'id': 'cp5_2',
                   'question': 'A patchwork mat contains 8 whole squares and 6 half-triangles. What is its total area '
                               'in square units?',
                   'options': ['11 square units (8 + 3)',
                               '14 square units (8 + 6)',
                               '7 square units',
                               '48 square units'],
                   'answer': 0,
                   'explanation': '6 half-triangles = 3 whole squares. Total area = 8 + 3 = 11 square units.'}]},
 {'id': 6,
  'title': 'Grid Measurement',
  'tagline': 'Standard Grids • 1 cm Square Grid Overlays & Unit Square Foundations',
  'lecture': 'Because non-standard units like books and lunch boxes vary in size across different schools and homes, '
             'mathematicians established a universal standard: the 1 centimetre square grid. A unit square is defined '
             'as an exact square whose sides each measure 1 centimetre. The flat surface region enclosed inside this '
             'unit square is defined as exactly 1 square centimetre, abbreviated as 1 sq cm or cm squared. When you '
             'place any geometric shape onto a 1 centimetre grid paper, you can determine its exact area by counting '
             'the unit squares it covers! To count accurately, we follow three simple rules: first, count every full '
             'square covered as 1; second, count every half-square covered as half; and third, if a boundary cuts a '
             'square irregularly, count squares that are more than half covered as 1 full square, while ignoring '
             'squares that are less than half covered. By pairing up half squares into whole numbers, you can '
             'determine the area of irregular garden plots, triangular sails, and patchwork mats with remarkable '
             'geometric accuracy, establishing an objective baseline that remains identical in every classroom and '
             'scientific laboratory across the entire world, enabling learners to communicate spatial measurements '
             'without any misunderstanding.',
  'content_html': '\n'
                  '        <div class="space-y-3 text-xs leading-relaxed text-slate-300">\n'
                  '            <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700">\n'
                  '                <h3 class="text-sm font-bold text-amber-400 mb-1">Standard 1 cm² Grid Counting '
                  'Rules</h3>\n'
                  '                <p>When finding the area of any shape overlaid on a 1 cm square grid:</p>\n'
                  '            </div>\n'
                  '            <div class="grid grid-cols-3 gap-2 font-mono text-center">\n'
                  '                <div class="p-2 rounded bg-slate-900 border border-slate-800">\n'
                  '                    <span class="text-emerald-400 font-bold block text-xs">Full Squares</span>\n'
                  '                    <span class="text-sm text-cyan-300 font-bold block my-1">Count as 1</span>\n'
                  '                    <span class="text-[10px] text-slate-400">Completely filled cells</span>\n'
                  '                </div>\n'
                  '                <div class="p-2 rounded bg-slate-900 border border-slate-800">\n'
                  '                    <span class="text-amber-400 font-bold block text-xs">Half Squares</span>\n'
                  '                    <span class="text-sm text-cyan-300 font-bold block my-1">Count as 1/2</span>\n'
                  '                    <span class="text-[10px] text-slate-400">Two half cells = 1 cm²</span>\n'
                  '                </div>\n'
                  '                <div class="p-2 rounded bg-slate-900 border border-slate-800">\n'
                  '                    <span class="text-indigo-400 font-bold block text-xs">&gt; Half Squares</span>\n'
                  '                    <span class="text-sm text-cyan-300 font-bold block my-1">Count as 1</span>\n'
                  '                    <span class="text-[10px] text-slate-400">Ignore cells &lt; half</span>\n'
                  '                </div>\n'
                  '            </div>\n'
                  '        </div>\n'
                  '        ',
  'checkpoints': [{'id': 'cp6_1',
                   'question': 'What is the area of a square whose sides each measure 1 cm?',
                   'options': ['1 square centimetre (1 sq cm)',
                               '4 centimetres',
                               '2 square centimetres',
                               '10 millimetres'],
                   'answer': 0,
                   'explanation': 'A unit square with sides of 1 cm covers an area of 1 cm × 1 cm = 1 square '
                                  'centimetre.'},
                  {'id': 'cp6_2',
                   'question': 'A shape on grid paper covers 6 full squares and 4 half-squares. What is its total '
                               'area?',
                   'options': ['8 sq cm (6 + 2)', '10 sq cm (6 + 4)', '12 sq cm', '7 sq cm'],
                   'answer': 0,
                   'explanation': '4 half-squares = 2 full sq cm. Total area = 6 + 2 = 8 sq cm.'}]},
 {'id': 7,
  'title': 'Palm Tracing',
  'tagline': 'Organic Area Estimation • Tracing Handprints on 1 cm Grids',
  'lecture': 'How large is your own hand? We can answer this question with scientific precision through the palm '
             'tracing activity. Place your hand flat on a sheet of 1 centimetre squared grid paper, keeping your '
             'fingers gently spread. Using a sharp pencil, trace the outline of your palm and fingers carefully along '
             'the paper. When you lift your hand, an organic silhouette appears across the grid lines. How do we '
             'compute the area of such an irregular shape with curved fingertips? We apply the standard grid counting '
             'conventions. First, mark every completely filled square with a blue dot and count them up. Next, look '
             'for squares that are cut by your skin boundary: count squares that are more than half covered as 1, '
             'count squares that are roughly half covered as half, and ignore tiny slivers that cover less than half. '
             'Adding these counts gives a close estimate of your palm area in square centimetres! Comparing handprints '
             'with classmates reveals fascinating variations: taller students often have palm areas exceeding 80 '
             'square centimetres, while smaller hands measure around 50 square centimetres, demonstrating how '
             'empirical grid counting bridges geometry with human anatomy and personal biology in an engaging, '
             'interactive classroom experiment.',
  'content_html': '\n'
                  '        <div class="space-y-3 text-xs leading-relaxed text-slate-300">\n'
                  '            <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700">\n'
                  '                <h3 class="text-sm font-bold text-amber-400 mb-1">Estimating Irregular Organic '
                  'Surfaces</h3>\n'
                  '                <p>Natural objects like human hands, footprints, and water puddles do not have '
                  'straight edges. Square grids allow estimation via threshold counting:</p>\n'
                  '            </div>\n'
                  '            <div class="grid grid-cols-2 gap-2 font-mono">\n'
                  '                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">\n'
                  '                    <span class="text-cyan-400 font-bold block mb-1">Step-by-Step '
                  'Procedure:</span>\n'
                  '                    <p class="text-[11px] text-slate-300">1. Trace hand flat on 1 cm grid.<br>2. '
                  'Count full cells (N_full).<br>3. Count cells &gt; 1/2 covered (N_more).<br>4. Estimated Area ≈ '
                  'N_full + N_more.</p>\n'
                  '                </div>\n'
                  '                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">\n'
                  '                    <span class="text-emerald-400 font-bold block mb-1">Typical Class '
                  'Results:</span>\n'
                  '                    <p class="text-[11px] text-slate-300">• Grade 5 student palm: ~50 to 75 '
                  'cm²<br>• Adult teacher palm: ~90 to 120 cm²<br>Enables direct empirical comparison!</p>\n'
                  '                </div>\n'
                  '            </div>\n'
                  '        </div>\n'
                  '        ',
  'checkpoints': [{'id': 'cp7_1',
                   'question': 'When tracing an irregular curved handprint on grid paper, how should a square that is '
                               'more than half covered be counted?',
                   'options': ['As 1 full square centimetre',
                               'Ignored completely as 0',
                               'Divided by 10',
                               'Multiplied by 4'],
                   'answer': 0,
                   'explanation': 'In grid area approximation, any cell more than half covered is rounded up and '
                                  'counted as 1 full square.'},
                  {'id': 'cp7_2',
                   'question': 'A student traces their palm and counts 42 fully covered squares and 14 squares that '
                               'are more than half covered. What is the estimated palm area?',
                   'options': ['56 sq cm (42 + 14)', '28 sq cm (42 - 14)', '588 sq cm (42 × 14)', '42 sq cm'],
                   'answer': 0,
                   'explanation': 'Estimated area = Full squares + More-than-half squares = 42 + 14 = 56 square '
                                  'centimetres.'}]},
 {'id': 8,
  'title': 'Leaf Area',
  'tagline': 'Botanical Surface Comparison • Tracing Garden Leaves from Smallest to Largest',
  'lecture': 'Just as we estimated handprint areas, we can venture into the school garden to explore the diverse '
             'geometry of plant leaves. Collect a variety of fallen leaves from different plants: a tiny coriander or '
             'neem leaf, a slender mango leaf, a broad banyan leaf, and an expansive peepal leaf. Lay each leaf flat '
             'against your 1 centimetre grid paper, press it gently with your fingers, and trace its outer contour '
             'with a fine pencil. By counting the enclosed unit squares using our established estimation guidelines, '
             'you can calculate and rank the surface areas of these botanical wonders with confidence. A small rose '
             'leaflet might cover only 4 square centimetres, whereas a mature peepal leaf can span over 65 square '
             'centimetres! Biologists use this exact mathematical grid method to study photosynthesis, because a leaf '
             'with a larger surface area captures more sunlight and carbon dioxide to produce food. Comparing leaf '
             'areas bridges mathematics and botany, illustrating how living organisms adapt their flat surface '
             'geometry to thrive in their natural forest habitats, showing that mathematical principles of surface '
             'coverage govern the living natural world all around our homes, classrooms, school courtyards, parks, and '
             'diverse outdoor natural environments.',
  'content_html': '\n'
                  '        <div class="space-y-3 text-xs leading-relaxed text-slate-300">\n'
                  '            <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-700">\n'
                  '                <h3 class="text-sm font-bold text-amber-400 mb-1">Botanical Leaf Surface '
                  'Ranking</h3>\n'
                  '                <p>Grid paper provides an objective tool to compare organic shapes without complex '
                  'calculus:</p>\n'
                  '            </div>\n'
                  '            <div class="overflow-x-auto">\n'
                  '                <table class="w-full text-left font-mono text-[11px] border border-slate-700">\n'
                  '                    <thead class="bg-slate-800 text-slate-300">\n'
                  '                        <tr>\n'
                  '                            <th class="p-1.5 border-b border-slate-700">Leaf Sample</th>\n'
                  '                            <th class="p-1.5 border-b border-slate-700">Shape Character</th>\n'
                  '                            <th class="p-1.5 border-b border-slate-700">Estimated Area</th>\n'
                  '                            <th class="p-1.5 border-b border-slate-700">Biological '
                  'Significance</th>\n'
                  '                        </tr>\n'
                  '                    </thead>\n'
                  '                    <tbody class="divide-y divide-slate-800">\n'
                  '                        <tr>\n'
                  '                            <td class="p-1.5 text-amber-300 font-bold">Neem Leaflet</td>\n'
                  '                            <td class="p-1.5 text-slate-200">Serrated, slender</td>\n'
                  '                            <td class="p-1.5 text-cyan-300">~3 to 5 cm²</td>\n'
                  '                            <td class="p-1.5 text-slate-400">Minimizes water loss in dry '
                  'climates</td>\n'
                  '                        </tr>\n'
                  '                        <tr>\n'
                  '                            <td class="p-1.5 text-amber-300 font-bold">Mango Leaf</td>\n'
                  '                            <td class="p-1.5 text-slate-200">Elongated lanceolate</td>\n'
                  '                            <td class="p-1.5 text-cyan-300">~25 to 35 cm²</td>\n'
                  '                            <td class="p-1.5 text-slate-400">Balanced sun capture and wind '
                  'tolerance</td>\n'
                  '                        </tr>\n'
                  '                        <tr>\n'
                  '                            <td class="p-1.5 text-amber-300 font-bold">Peepal Leaf</td>\n'
                  '                            <td class="p-1.5 text-slate-200">Broad cordate with drip tip</td>\n'
                  '                            <td class="p-1.5 text-cyan-300">~55 to 70 cm²</td>\n'
                  '                            <td class="p-1.5 text-slate-400">High photosynthetic surface area</td>\n'
                  '                        </tr>\n'
                  '                    </tbody>\n'
                  '                </table>\n'
                  '            </div>\n'
                  '        </div>\n'
                  '        ',
  'checkpoints': [{'id': 'cp8_1',
                   'question': 'Why is grid paper useful for finding the area of a peepal leaf?',
                   'options': ['A leaf has irregular curved edges that cannot be calculated with simple ruler '
                               'multiplication',
                               'Grid paper changes the color of the leaf',
                               'Grid paper makes the leaf grow larger',
                               'Leaves only grow in perfect rectangular shapes'],
                   'answer': 0,
                   'explanation': 'Because organic leaves have irregular curved boundaries, counting unit squares on '
                                  'grid paper provides an accurate surface estimate.'},
                  {'id': 'cp8_2',
                   'question': 'Leaf A covers 28 unit squares on a 1 cm grid, while Leaf B covers 45 unit squares. '
                               'Which leaf has a larger surface area?',
                   'options': ['Leaf B is larger by 17 sq cm',
                               'Leaf A is larger by 17 sq cm',
                               'Both leaves have identical area',
                               'Cannot be determined without weighing them'],
                   'answer': 0,
                   'explanation': '45 sq cm - 28 sq cm = 17 sq cm. Leaf B covers 17 more unit squares than Leaf A.'}]},
 {'id': 9,
  'title': 'Same Area Perimeters',
  'tagline': 'Fixed Area Investigation • Arranging 12 Unit Squares into Multiple Perimeters',
  'lecture': 'A fascinating mathematical mystery unfolds when we explore shapes with identical surface areas: do '
             'shapes that cover the exact same area always have the same perimeter? Let us test this using twelve unit '
             'squares, each measuring 1 square centimetre. Because we are using twelve squares, every single '
             'arrangement will have an identical area of 12 square centimetres. If we arrange all twelve tiles into a '
             'single long strip measuring 1 centimetre wide and 12 centimetres long, the perimeter equals 1 plus 12 '
             'plus 1 plus 12, which totals 26 centimetres! Next, rearrange the twelve tiles into two rows of six. Now '
             'the length is 6 centimetres and the breadth is 2 centimetres. The perimeter becomes 2 plus 6 plus 2 plus '
             '6, giving 16 centimetres! Finally, arrange them into three rows of four. The perimeter is now 3 plus 4 '
             'plus 3 plus 4, which is only 14 centimetres! Notice what occurred: while every shape maintained an '
             'identical area of 12 square centimetres, their perimeters changed drastically from 26 down to 14 '
             'centimetres! As shapes become more compact and closer to a square, their perimeter shrinks, proving that '
             'having the same area does not guarantee having the same perimeter.',
  'content_html': '\n'
                  '<div class="space-y-4">\n'
                  '    <div class="bg-gradient-to-r from-amber-900/40 via-orange-900/30 to-amber-900/40 border '
                  'border-amber-500/30 rounded-xl p-4">\n'
                  '        <h4 class="text-amber-300 font-bold text-sm tracking-wider uppercase mb-1">Core '
                  'Investigation</h4>\n'
                  '        <p class="text-slate-200 text-sm leading-relaxed">\n'
                  '            Shapes having the <strong>exact same area</strong> can possess vastly different '
                  'perimeters depending on how their unit tiles are configured!\n'
                  '        </p>\n'
                  '    </div>\n'
                  '\n'
                  '    <div class="grid grid-cols-1 md:grid-cols-3 gap-3">\n'
                  '        <div class="bg-slate-800/80 border border-slate-700/70 rounded-xl p-3 text-center">\n'
                  '            <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Strip: 1 × '
                  '12</span>\n'
                  '            <div class="my-2 bg-slate-900/80 p-2 rounded border border-slate-700">\n'
                  '                <div class="text-lg font-black text-white">Area = 12 cm²</div>\n'
                  '                <div class="text-xs text-rose-400 font-mono mt-1">P = 2 × (1 + 12) = 26 cm</div>\n'
                  '            </div>\n'
                  '            <p class="text-xs text-slate-400">Extremely elongated shape yields the maximum border '
                  'perimeter.</p>\n'
                  '        </div>\n'
                  '\n'
                  '        <div class="bg-slate-800/80 border border-slate-700/70 rounded-xl p-3 text-center">\n'
                  '            <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Grid: 2 × '
                  '6</span>\n'
                  '            <div class="my-2 bg-slate-900/80 p-2 rounded border border-slate-700">\n'
                  '                <div class="text-lg font-black text-white">Area = 12 cm²</div>\n'
                  '                <div class="text-xs text-cyan-400 font-mono mt-1">P = 2 × (2 + 6) = 16 cm</div>\n'
                  '            </div>\n'
                  '            <p class="text-xs text-slate-400">Moderately compact arrangement with a reduced '
                  'perimeter.</p>\n'
                  '        </div>\n'
                  '\n'
                  '        <div class="bg-slate-800/80 border border-slate-700/70 rounded-xl p-3 text-center">\n'
                  '            <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">Block: 3 × '
                  '4</span>\n'
                  '            <div class="my-2 bg-slate-900/80 p-2 rounded border border-slate-700">\n'
                  '                <div class="text-lg font-black text-white">Area = 12 cm²</div>\n'
                  '                <div class="text-xs text-emerald-400 font-mono mt-1">P = 2 × (3 + 4) = 14 cm</div>\n'
                  '            </div>\n'
                  '            <p class="text-xs text-slate-400">Most compact rectangle configuration gives the '
                  'smallest perimeter.</p>\n'
                  '        </div>\n'
                  '    </div>\n'
                  '\n'
                  '    <div class="bg-blue-950/40 border border-blue-500/30 rounded-xl p-3 flex items-center '
                  'justify-between">\n'
                  '        <span class="text-xs text-blue-300 font-medium">Key Takeaway</span>\n'
                  '        <span class="text-xs text-slate-300">More compact / squarish shapes have smaller perimeters '
                  'for a fixed area!</span>\n'
                  '    </div>\n'
                  '</div>\n',
  'checkpoints': [{'question': 'If you arrange 16 unit squares into a 1 × 16 rectangle and a 4 × 4 square, what are '
                               'their perimeters?',
                   'options': ['1 × 16 has P = 34 cm; 4 × 4 has P = 16 cm',
                               'Both shapes have identical perimeters of 16 cm',
                               '1 × 16 has P = 17 cm; 4 × 4 has P = 8 cm',
                               '1 × 16 has P = 32 cm; 4 × 4 has P = 24 cm'],
                   'answer': 0,
                   'explanation': 'For 1 × 16: P = 2 × (1 + 16) = 34 cm. For 4 × 4: P = 4 × 4 = 16 cm. The compact '
                                  'square has less than half the perimeter of the strip!',
                   'hint': 'Add length and breadth, then double for the rectangle; multiply side by 4 for the square.'},
                  {'question': 'Which rectangle with an area of 18 cm² has the smallest perimeter?',
                   'options': ['1 cm × 18 cm (P = 38 cm)',
                               '2 cm × 9 cm (P = 22 cm)',
                               '3 cm × 6 cm (P = 18 cm)',
                               'All rectangles of 18 cm² have the same perimeter'],
                   'answer': 2,
                   'explanation': 'As the factors get closer together (3 and 6), the shape becomes more compact, '
                                  'minimizing perimeter to 2 × (3 + 6) = 18 cm.',
                   'hint': 'Check which factor pair has the smallest sum.'}]},
 {'id': 10,
  'title': 'Same Perimeter Areas',
  'tagline': 'Boundary Optimization • Maximizing Enclosed Area for a Fixed Perimeter',
  'lecture': 'Now let us turn the question upside down and investigate the reverse puzzle: do shapes that share the '
             'exact same perimeter enclose the same surface area? Suppose you are given a piece of wire or lace '
             'measuring 24 centimetres in total length. You can bend this wire to form many different rectangles, but '
             'the sum of length and breadth must always equal 12 centimetres. If you make a very thin rectangle with a '
             'breadth of 1 centimetre and length of 11 centimetres, its perimeter is 24 centimetres, but its area is '
             'only 11 square centimetres! If you change the dimensions to 2 centimetres by 10 centimetres, the '
             'perimeter remains 24 centimetres, but the enclosed area jumps to 20 square centimetres! Make it 3 by 9, '
             'and the area climbs to 27 square centimetres! Keep adjusting until the sides are 6 centimetres by 6 '
             'centimetres: a perfect square. The perimeter is still 24 centimetres, but look at the area: 36 square '
             'centimetres! That is over three times the area of the 1 by 11 rectangle! For any given fixed perimeter, '
             'a square always encloses the maximum possible rectangular area, a principle used by farmers, architects, '
             'and designers worldwide.',
  'content_html': '\n'
                  '<div class="space-y-4">\n'
                  '    <div class="bg-gradient-to-r from-emerald-900/40 via-teal-900/30 to-emerald-900/40 border '
                  'border-emerald-500/30 rounded-xl p-4">\n'
                  '        <h4 class="text-emerald-300 font-bold text-sm tracking-wider uppercase mb-1">Perimeter '
                  'Optimization Rule</h4>\n'
                  '        <p class="text-slate-200 text-sm leading-relaxed">\n'
                  '            Given a fixed perimeter, as length and breadth become closer to equal, the enclosed '
                  'area increases until it reaches its <strong>maximum in a square</strong>!\n'
                  '        </p>\n'
                  '    </div>\n'
                  '\n'
                  '    <div class="overflow-hidden border border-slate-700 rounded-xl bg-slate-900/80">\n'
                  '        <table class="w-full text-xs text-left text-slate-300">\n'
                  '            <thead class="bg-slate-800 text-slate-200 font-semibold uppercase tracking-wider">\n'
                  '                <tr>\n'
                  '                    <th class="p-3">Dimensions (L × B)</th>\n'
                  '                    <th class="p-3">Sum (L + B)</th>\n'
                  '                    <th class="p-3">Perimeter (cm)</th>\n'
                  '                    <th class="p-3">Enclosed Area (cm²)</th>\n'
                  '                    <th class="p-3">Efficiency</th>\n'
                  '                </tr>\n'
                  '            </thead>\n'
                  '            <tbody class="divide-y divide-slate-800 font-mono">\n'
                  '                <tr class="hover:bg-slate-800/40">\n'
                  '                    <td class="p-3 text-white font-bold">11 cm × 1 cm</td>\n'
                  '                    <td class="p-3">12 cm</td>\n'
                  '                    <td class="p-3 text-cyan-400">24 cm</td>\n'
                  '                    <td class="p-3 text-rose-400 font-bold">11 cm²</td>\n'
                  '                    <td class="p-3 text-slate-400">Lowest area (skinny)</td>\n'
                  '                </tr>\n'
                  '                <tr class="hover:bg-slate-800/40">\n'
                  '                    <td class="p-3 text-white font-bold">10 cm × 2 cm</td>\n'
                  '                    <td class="p-3">12 cm</td>\n'
                  '                    <td class="p-3 text-cyan-400">24 cm</td>\n'
                  '                    <td class="p-3 text-amber-400 font-bold">20 cm²</td>\n'
                  '                    <td class="p-3 text-slate-400">Moderate area</td>\n'
                  '                </tr>\n'
                  '                <tr class="hover:bg-slate-800/40">\n'
                  '                    <td class="p-3 text-white font-bold">9 cm × 3 cm</td>\n'
                  '                    <td class="p-3">12 cm</td>\n'
                  '                    <td class="p-3 text-cyan-400">24 cm</td>\n'
                  '                    <td class="p-3 text-yellow-400 font-bold">27 cm²</td>\n'
                  '                    <td class="p-3 text-slate-400">Substantial area</td>\n'
                  '                </tr>\n'
                  '                <tr class="hover:bg-slate-800/40 bg-emerald-950/30">\n'
                  '                    <td class="p-3 text-emerald-300 font-bold">6 cm × 6 cm (Square)</td>\n'
                  '                    <td class="p-3">12 cm</td>\n'
                  '                    <td class="p-3 text-cyan-400">24 cm</td>\n'
                  '                    <td class="p-3 text-emerald-400 font-bold">36 cm²</td>\n'
                  '                    <td class="p-3 text-emerald-300 font-bold">★ Maximum Area!</td>\n'
                  '                </tr>\n'
                  '            </tbody>\n'
                  '        </table>\n'
                  '    </div>\n'
                  '</div>\n',
  'checkpoints': [{'question': 'A string of length 20 cm is bent into different rectangles. What is the maximum area '
                               'that can be enclosed?',
                   'options': ['25 cm² (when shaped as a 5 cm × 5 cm square)',
                               '24 cm² (when shaped as a 6 cm × 4 cm rectangle)',
                               '9 cm² (when shaped as a 9 cm × 1 cm rectangle)',
                               '20 cm² (when shaped as a 10 cm × 2 cm rectangle)'],
                   'answer': 0,
                   'explanation': 'With P = 20 cm, L + B = 10 cm. The maximum area occurs when L = B = 5 cm (a '
                                  'square), giving 5 × 5 = 25 cm².',
                   'hint': 'Divide the perimeter by 4 to find the side of the optimal square.'},
                  {'question': 'If two rectangles have the exact same perimeter of 16 cm, must their areas be equal?',
                   'options': ['No, their areas can differ (e.g., 7 cm × 1 cm gives 7 cm², while 4 cm × 4 cm gives 16 '
                               'cm²)',
                               'Yes, shapes with equal perimeters always have identical areas',
                               'No, but the area of any rectangle with P = 16 cm must always be at least 20 cm²',
                               'Yes, because both require the exact same length of boundary wire'],
                   'answer': 0,
                   'explanation': 'Different factor pairs with the same sum give different products. 7 × 1 = 7 cm², '
                                  'but 4 × 4 = 16 cm².',
                   'hint': 'Think about a thin ribbon rectangle compared to a square.'}]},
 {'id': 11,
  'title': 'Array Multiplication',
  'tagline': 'From Counting to Multiplication • The Row-Column Array Structure of Area',
  'lecture': 'Counting every single unit square one by one is wonderful for small shapes, but imagine counting '
             'thousands of squares to measure a playground or house floor! Fortunately, rectangles have an elegant '
             'mathematical property: their unit squares are arranged in neat, uniform rows and columns. This organized '
             'grid structure allows us to replace slow counting with rapid multiplication! Suppose a rectangle is 5 '
             'centimetres long and 3 centimetres wide. It contains exactly 3 horizontal rows of squares, with each row '
             'containing 5 unit squares. Instead of counting one, two, three all the way to fifteen, we simply '
             'multiply the number of rows by the number of squares in each row: 3 times 5 equals 15! We can also view '
             'it vertically as 5 vertical columns, each containing 3 unit squares: 5 times 3 equals 15! This powerful '
             'row-column array model connects basic arithmetic multiplication directly and visually to two-dimensional '
             'geometric area. Whether you are laying bathroom tiles, assembling quilt patches, planting orderly tomato '
             'beds in an agricultural field, or designing pixel arrays on computer screens, the total count of squares '
             'is always the product of rows and columns, unlocking rapid spatial calculation without tedious manual '
             'counting.',
  'content_html': '\n'
                  '<div class="space-y-4">\n'
                  '    <div class="bg-gradient-to-r from-blue-900/40 via-indigo-900/30 to-blue-900/40 border '
                  'border-blue-500/30 rounded-xl p-4">\n'
                  '        <h4 class="text-blue-300 font-bold text-sm tracking-wider uppercase mb-1">Array '
                  'Multiplication Model</h4>\n'
                  '        <p class="text-slate-200 text-sm leading-relaxed">\n'
                  '            In any rectangular grid, unit squares align in uniform rows and columns:\n'
                  '            <span class="text-amber-300 font-bold">Total Area = Number of Rows × Number of '
                  'Columns</span>.\n'
                  '        </p>\n'
                  '    </div>\n'
                  '\n'
                  '    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">\n'
                  '        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-4">\n'
                  '            <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Row '
                  'Perspective</span>\n'
                  '            <div class="mt-2 text-sm text-slate-300">\n'
                  '                <p>3 horizontal rows</p>\n'
                  '                <p class="text-xs text-slate-400 mt-1">Each row contains 5 unit squares:</p>\n'
                  '                <div class="mt-2 p-2 bg-slate-900/80 rounded border border-slate-700 font-mono '
                  'text-cyan-300 font-bold">\n'
                  '                    5 + 5 + 5 = 3 × 5 = 15 cm²\n'
                  '                </div>\n'
                  '            </div>\n'
                  '        </div>\n'
                  '\n'
                  '        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-4">\n'
                  '            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">Column '
                  'Perspective</span>\n'
                  '            <div class="mt-2 text-sm text-slate-300">\n'
                  '                <p>5 vertical columns</p>\n'
                  '                <p class="text-xs text-slate-400 mt-1">Each column contains 3 unit squares:</p>\n'
                  '                <div class="mt-2 p-2 bg-slate-900/80 rounded border border-slate-700 font-mono '
                  'text-indigo-300 font-bold">\n'
                  '                    3 + 3 + 3 + 3 + 3 = 5 × 3 = 15 cm²\n'
                  '                </div>\n'
                  '            </div>\n'
                  '        </div>\n'
                  '    </div>\n'
                  '\n'
                  '    <div class="p-3 bg-amber-950/40 border border-amber-500/30 rounded-xl flex items-center '
                  'justify-between text-xs">\n'
                  '        <span class="text-amber-300 font-bold">Commutative Property:</span>\n'
                  '        <span class="text-slate-300 font-mono">3 × 5 = 5 × 3 = 15 cm²</span>\n'
                  '        <span class="text-slate-400">Rotating the rectangle does not alter its area!</span>\n'
                  '    </div>\n'
                  '</div>\n',
  'checkpoints': [{'question': 'A chocolate bar has 4 rows of squares with 6 squares in each row. What is the total '
                               'area in squares?',
                   'options': ['24 squares (4 × 6)',
                               '20 squares (4 + 6 + 4 + 6)',
                               '10 squares (4 + 6)',
                               '36 squares (6 × 6)'],
                   'answer': 0,
                   'explanation': 'Total squares = Rows × Columns = 4 × 6 = 24 squares. (Notice that 20 is the '
                                  'perimeter, not the area!).',
                   'hint': 'Multiply the number of rows by the number of squares in each row.'},
                  {'question': 'A floor is tiled with 7 rows of 8 tiles each. How many tiles are on the floor in '
                               'total?',
                   'options': ['56 tiles', '30 tiles', '15 tiles', '64 tiles'],
                   'answer': 0,
                   'explanation': 'Total tiles = 7 × 8 = 56 tiles.',
                   'hint': 'Use multiplication table of 7 and 8.'}]},
 {'id': 12,
  'title': 'Rectangle Formulas',
  'tagline': 'Mastering the Equations • Area = Length × Breadth and Perimeter = 2 × (L + B)',
  'lecture': 'From the row and column array model, we can now state the two foundational formulas that govern every '
             'rectangle in mathematics. First, the area formula: the number of columns corresponds to the length of '
             'the rectangle, and the number of rows corresponds to its breadth or width. Therefore, the area of any '
             'rectangle is calculated by multiplying its length by its breadth: Area equals Length times Breadth! For '
             'example, a rectangle with length 8 centimetres and breadth 5 centimetres has an area of 8 times 5, which '
             'equals 40 square centimetres. Second, the perimeter formula: to traverse the outer border of a '
             'rectangle, you walk along its length, down its breadth, back along its opposite length, and up its '
             'opposite breadth. Since there are two lengths and two breadths, the perimeter equals two times the '
             'length plus two times the breadth, or more elegantly: Perimeter equals 2 times the sum of Length plus '
             'Breadth! For our 8 by 5 rectangle, the perimeter is 2 times 8 plus 5, which is 2 times 13, giving 26 '
             'centimetres. Always remember the distinction: perimeter measures outer boundary in centimetres, while '
             'area measures flat surface coverage in square centimetres!',
  'content_html': '\n'
                  '<div class="space-y-4">\n'
                  '    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">\n'
                  '        <!-- Area Card -->\n'
                  '        <div class="bg-gradient-to-br from-indigo-950/60 to-slate-900 border border-indigo-500/40 '
                  'rounded-xl p-4">\n'
                  '            <div class="flex items-center justify-between mb-2">\n'
                  '                <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">Surface '
                  'Coverage</span>\n'
                  '                <span class="text-xs bg-indigo-500/20 text-indigo-300 px-2 py-0.5 rounded '
                  'font-mono">2-Dimensional</span>\n'
                  '            </div>\n'
                  '            <h4 class="text-white font-extrabold text-lg">Area of Rectangle</h4>\n'
                  '            <div class="my-3 p-3 bg-slate-950/80 rounded-lg border border-indigo-500/30 text-center '
                  'font-mono">\n'
                  '                <span class="text-amber-400 text-lg font-black">Area = Length × Breadth</span>\n'
                  '            </div>\n'
                  '            <p class="text-xs text-slate-300 leading-relaxed">\n'
                  '                Measures square units enclosed inside. Units: cm², m², km².\n'
                  '            </p>\n'
                  '        </div>\n'
                  '\n'
                  '        <!-- Perimeter Card -->\n'
                  '        <div class="bg-gradient-to-br from-rose-950/60 to-slate-900 border border-rose-500/40 '
                  'rounded-xl p-4">\n'
                  '            <div class="flex items-center justify-between mb-2">\n'
                  '                <span class="text-xs font-bold text-rose-400 uppercase tracking-wider">Boundary '
                  'Length</span>\n'
                  '                <span class="text-xs bg-rose-500/20 text-rose-300 px-2 py-0.5 rounded '
                  'font-mono">1-Dimensional</span>\n'
                  '            </div>\n'
                  '            <h4 class="text-white font-extrabold text-lg">Perimeter of Rectangle</h4>\n'
                  '            <div class="my-3 p-3 bg-slate-950/80 rounded-lg border border-rose-500/30 text-center '
                  'font-mono">\n'
                  '                <span class="text-emerald-400 text-lg font-black">Perimeter = 2 × (L + B)</span>\n'
                  '            </div>\n'
                  '            <p class="text-xs text-slate-300 leading-relaxed">\n'
                  '                Measures total outer boundary length. Units: cm, m, km.\n'
                  '            </p>\n'
                  '        </div>\n'
                  '    </div>\n'
                  '\n'
                  '    <!-- Comparative Example -->\n'
                  '    <div class="bg-slate-900/80 border border-slate-700 rounded-xl p-3 text-xs">\n'
                  '        <span class="text-slate-400 uppercase tracking-wider font-semibold">Worked Example: L = 8 '
                  'cm, B = 5 cm</span>\n'
                  '        <div class="mt-2 grid grid-cols-2 gap-3 text-center font-mono">\n'
                  '            <div class="bg-slate-800 p-2 rounded border border-indigo-500/30 text-indigo-300">\n'
                  '                Area = 8 × 5 = <strong class="text-white">40 cm²</strong>\n'
                  '            </div>\n'
                  '            <div class="bg-slate-800 p-2 rounded border border-rose-500/30 text-rose-300">\n'
                  '                Perimeter = 2 × (8 + 5) = <strong class="text-white">26 cm</strong>\n'
                  '            </div>\n'
                  '        </div>\n'
                  '    </div>\n'
                  '</div>\n',
  'checkpoints': [{'question': 'A rectangular rug has a length of 7 m and a breadth of 4 m. What are its perimeter and '
                               'area?',
                   'options': ['Perimeter = 22 m; Area = 28 m²',
                               'Perimeter = 28 m; Area = 22 m²',
                               'Perimeter = 11 m; Area = 28 m²',
                               'Perimeter = 44 m; Area = 56 m²'],
                   'answer': 0,
                   'explanation': 'P = 2 × (7 + 4) = 2 × 11 = 22 m. Area = 7 × 4 = 28 m².',
                   'hint': 'Perimeter is 2 × (L + B); Area is L × B.'},
                  {'question': 'If a rectangle has an area of 48 cm² and a length of 8 cm, what is its breadth?',
                   'options': ['6 cm (since 48 ÷ 8 = 6)',
                               '40 cm (since 48 - 8 = 40)',
                               '12 cm (since 48 ÷ 4 = 12)',
                               '8 cm (since all rectangles have equal sides)'],
                   'answer': 0,
                   'explanation': 'Breadth = Area ÷ Length = 48 ÷ 8 = 6 cm. Check: 8 × 6 = 48 cm².',
                   'hint': 'Divide the total area by the given length.'}]},
 {'id': 13,
  'title': 'Square Formulas',
  'tagline': 'Equilateral Symmetry • Area = Side × Side and Perimeter = 4 × Side',
  'lecture': 'A square is a special, wonderfully symmetrical rectangle where all four sides are exactly equal in '
             'length! Because the length equals the breadth, the formulas for the perimeter and area of a square '
             "become even simpler and more elegant. Let us call the length of any side 's'. To find the perimeter of a "
             'square, we simply add the four equal sides: side plus side plus side plus side, which is four times the '
             'side length: Perimeter equals 4 times Side! For a square napkin with sides of 6 centimetres, the '
             'perimeter of decorative border lace needed is 4 times 6, which equals 24 centimetres. To find the area '
             'of the square, we apply our rectangle formula of length times breadth; but since length and breadth are '
             "both equal to 's', the formula becomes side times side: Area equals Side times Side! For our 6 "
             'centimetre napkin, the surface area covered is 6 times 6, which equals 36 square centimetres. Notice the '
             'power of units: the perimeter is measured in linear centimetres, whereas the area is measured in square '
             'centimetres! Knowing these formulas allows you to calculate both border trims and surface materials for '
             'tiles, gameboards, handkerchiefs, and picture frames in an instant.',
  'content_html': '\n'
                  '<div class="space-y-4">\n'
                  '    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">\n'
                  '        <!-- Square Area -->\n'
                  '        <div class="bg-gradient-to-br from-emerald-950/60 to-slate-900 border border-emerald-500/40 '
                  'rounded-xl p-4">\n'
                  '            <div class="flex items-center justify-between mb-2">\n'
                  '                <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">Surface '
                  'Area</span>\n'
                  '                <span class="text-xs bg-emerald-500/20 text-emerald-300 px-2 py-0.5 rounded '
                  'font-mono">s²</span>\n'
                  '            </div>\n'
                  '            <h4 class="text-white font-extrabold text-lg">Area of a Square</h4>\n'
                  '            <div class="my-3 p-3 bg-slate-950/80 rounded-lg border border-emerald-500/30 '
                  'text-center font-mono">\n'
                  '                <span class="text-emerald-300 text-lg font-black">Area = Side × Side</span>\n'
                  '            </div>\n'
                  '            <p class="text-xs text-slate-300 leading-relaxed">\n'
                  '                Multiply the side length by itself. Example: 6 cm × 6 cm = 36 cm².\n'
                  '            </p>\n'
                  '        </div>\n'
                  '\n'
                  '        <!-- Square Perimeter -->\n'
                  '        <div class="bg-gradient-to-br from-cyan-950/60 to-slate-900 border border-cyan-500/40 '
                  'rounded-xl p-4">\n'
                  '            <div class="flex items-center justify-between mb-2">\n'
                  '                <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Boundary '
                  'Length</span>\n'
                  '                <span class="text-xs bg-cyan-500/20 text-cyan-300 px-2 py-0.5 rounded '
                  'font-mono">4s</span>\n'
                  '            </div>\n'
                  '            <h4 class="text-white font-extrabold text-lg">Perimeter of a Square</h4>\n'
                  '            <div class="my-3 p-3 bg-slate-950/80 rounded-lg border border-cyan-500/30 text-center '
                  'font-mono">\n'
                  '                <span class="text-cyan-300 text-lg font-black">Perimeter = 4 × Side</span>\n'
                  '            </div>\n'
                  '            <p class="text-xs text-slate-300 leading-relaxed">\n'
                  '                Add all 4 identical sides together. Example: 4 × 6 cm = 24 cm.\n'
                  '            </p>\n'
                  '        </div>\n'
                  '    </div>\n'
                  '\n'
                  '    <!-- Quick Reference Comparison -->\n'
                  '    <div class="bg-slate-900/80 border border-slate-700 rounded-xl p-3">\n'
                  '        <h5 class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-2">Square '
                  'Dimensions Quick Guide</h5>\n'
                  '        <div class="grid grid-cols-4 gap-2 text-center text-xs font-mono">\n'
                  '            <div class="bg-slate-800 p-2 rounded">\n'
                  '                <div class="text-slate-400">Side = 3 cm</div>\n'
                  '                <div class="text-cyan-400 mt-1">P = 12 cm</div>\n'
                  '                <div class="text-emerald-400">A = 9 cm²</div>\n'
                  '            </div>\n'
                  '            <div class="bg-slate-800 p-2 rounded">\n'
                  '                <div class="text-slate-400">Side = 5 cm</div>\n'
                  '                <div class="text-cyan-400 mt-1">P = 20 cm</div>\n'
                  '                <div class="text-emerald-400">A = 25 cm²</div>\n'
                  '            </div>\n'
                  '            <div class="bg-slate-800 p-2 rounded">\n'
                  '                <div class="text-slate-400">Side = 7 cm</div>\n'
                  '                <div class="text-cyan-400 mt-1">P = 28 cm</div>\n'
                  '                <div class="text-emerald-400">A = 49 cm²</div>\n'
                  '            </div>\n'
                  '            <div class="bg-slate-800 p-2 rounded">\n'
                  '                <div class="text-slate-400">Side = 10 cm</div>\n'
                  '                <div class="text-cyan-400 mt-1">P = 40 cm</div>\n'
                  '                <div class="text-emerald-400">A = 100 cm²</div>\n'
                  '            </div>\n'
                  '        </div>\n'
                  '    </div>\n'
                  '</div>\n',
  'checkpoints': [{'question': 'A square chessboard has sides of 30 cm. What is its perimeter and area?',
                   'options': ['Perimeter = 120 cm; Area = 900 cm²',
                               'Perimeter = 60 cm; Area = 900 cm²',
                               'Perimeter = 120 cm; Area = 60 cm²',
                               'Perimeter = 300 cm; Area = 1200 cm²'],
                   'answer': 0,
                   'explanation': 'P = 4 × 30 = 120 cm. Area = 30 × 30 = 900 cm².',
                   'hint': 'Perimeter is 4 times the side; Area is side multiplied by side.'},
                  {'question': 'If the perimeter of a square garden is 36 metres, what is the area of the garden?',
                   'options': ['81 m² (side = 36 ÷ 4 = 9 m; Area = 9 × 9 = 81 m²)',
                               '144 m² (side = 12 m; Area = 12 × 12 = 144 m²)',
                               '36 m² (side = 6 m; Area = 6 × 6 = 36 m²)',
                               '72 m² (side = 9 m; Area = 9 × 8 = 72 m²)'],
                   'answer': 0,
                   'explanation': 'First find the side: 36 ÷ 4 = 9 m. Then find the area: 9 × 9 = 81 m².',
                   'hint': 'Divide perimeter by 4 to get side, then square it.'}]},
 {'id': 14,
  'title': 'Real-World Measurement',
  'tagline': 'Practical Applications • Sizing Classroom Floors, Notebooks, and Blackboards',
  'lecture': 'Mathematics truly comes alive when we apply perimeter and area to everyday real-world objects around us! '
             'Depending on the physical size of what we are measuring, we choose appropriate standard metric units. '
             'For small handheld objects like a postage stamp, an eraser, or a mobile phone screen, we measure '
             'perimeter in centimetres and area in square centimetres. For example, a student notebook cover measuring '
             '20 centimetres by 15 centimetres has an area of 300 square centimetres. However, when measuring larger '
             'architectural spaces such as our classroom floor, a basketball court, or an outdoor garden, centimetres '
             'are far too small! Instead, we measure boundaries in metres and floor surfaces in square metres. A '
             'square metre represents the area of a square whose sides are each 1 metre long. If our classroom floor '
             'measures 8 metres long and 6 metres wide, its perimeter for skirting boards is 2 times 8 plus 6, which '
             'equals 28 metres, while the floor area for laying ceramic floor tiles is 8 times 6, which equals 48 '
             'square metres! From buying chalkboard paint for school blackboards to purchasing wire fencing for '
             'agricultural fields, mastering real-world dimensions ensures accurate planning and zero wasted material.',
  'content_html': '\n'
                  '<div class="space-y-4">\n'
                  '    <div class="bg-gradient-to-r from-purple-900/40 via-violet-900/30 to-purple-900/40 border '
                  'border-purple-500/30 rounded-xl p-4">\n'
                  '        <h4 class="text-purple-300 font-bold text-sm tracking-wider uppercase mb-1">Scale & Unit '
                  'Selection</h4>\n'
                  '        <p class="text-slate-200 text-sm leading-relaxed">\n'
                  '            Always match the metric unit to the physical scale of the object:\n'
                  '            <span class="text-amber-300 font-bold">cm and cm²</span> for desk objects;\n'
                  '            <span class="text-emerald-300 font-bold">m and m²</span> for rooms and fields!\n'
                  '        </p>\n'
                  '    </div>\n'
                  '\n'
                  '    <div class="grid grid-cols-1 md:grid-cols-3 gap-3">\n'
                  '        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-3">\n'
                  '            <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Notebook '
                  'Cover</span>\n'
                  '            <div class="mt-2 text-xs text-slate-300 space-y-1 font-mono">\n'
                  '                <div>Dimensions: 20 cm × 15 cm</div>\n'
                  '                <div>Perimeter: 2 × (20 + 15) = 70 cm</div>\n'
                  '                <div class="text-cyan-300 font-bold">Area = 300 cm²</div>\n'
                  '            </div>\n'
                  '            <p class="text-xs text-slate-400 mt-2">Unit: Square Centimetres (cm²)</p>\n'
                  '        </div>\n'
                  '\n'
                  '        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-3">\n'
                  '            <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">Classroom '
                  'Blackboard</span>\n'
                  '            <div class="mt-2 text-xs text-slate-300 space-y-1 font-mono">\n'
                  '                <div>Dimensions: 3 m × 1.5 m</div>\n'
                  '                <div>Perimeter: 2 × (3 + 1.5) = 9 m</div>\n'
                  '                <div class="text-emerald-300 font-bold">Area = 4.5 m²</div>\n'
                  '            </div>\n'
                  '            <p class="text-xs text-slate-400 mt-2">Unit: Square Metres (m²)</p>\n'
                  '        </div>\n'
                  '\n'
                  '        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-3">\n'
                  '            <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Classroom '
                  'Floor</span>\n'
                  '            <div class="mt-2 text-xs text-slate-300 space-y-1 font-mono">\n'
                  '                <div>Dimensions: 8 m × 6 m</div>\n'
                  '                <div>Skirting: 2 × (8 + 6) = 28 m</div>\n'
                  '                <div class="text-amber-300 font-bold">Area = 48 m²</div>\n'
                  '            </div>\n'
                  '            <p class="text-xs text-slate-400 mt-2">Unit: Square Metres (m²)</p>\n'
                  '        </div>\n'
                  '    </div>\n'
                  '\n'
                  '    <div class="p-3 bg-slate-900/80 border border-slate-700 rounded-xl flex items-center '
                  'justify-between text-xs">\n'
                  '        <span class="text-slate-400">Remember:</span>\n'
                  '        <span class="text-indigo-300 font-bold font-mono">1 m² = 100 cm × 100 cm = 10,000 '
                  'cm²</span>\n'
                  '        <span class="text-slate-400">A square metre contains 10,000 square centimetres!</span>\n'
                  '    </div>\n'
                  '</div>\n',
  'checkpoints': [{'question': 'Which metric unit is most appropriate for measuring the area of a school football '
                               'ground?',
                   'options': ['Square metres (m²)', 'Square centimetres (cm²)', 'Centimetres (cm)', 'Metres (m)'],
                   'answer': 0,
                   'explanation': 'A football ground is large, so square metres (m²) is the standard unit. '
                                  '(Centimetres are for lengths, not areas!).',
                   'hint': 'Area requires square units, and large open grounds are measured in metres.'},
                  {'question': 'A square ludo board has a side length of 40 cm. What is the area of the ludo board?',
                   'options': ['1,600 cm²', '160 cm²', '80 cm²', '1,200 cm²'],
                   'answer': 0,
                   'explanation': 'Area = Side × Side = 40 × 40 = 1,600 cm².',
                   'hint': 'Multiply 40 by 40.'}]},
 {'id': 15,
  'title': 'Applied Word Problems',
  'tagline': 'Real-Life Problem Solving • Fencing Costs, Missing Dimensions, and Composite Surfaces',
  'lecture': 'Real-world challenges often require using both perimeter and area formulas together to solve practical '
             'questions. Consider a rectangular agricultural plot measuring 25 metres long and 10 metres wide. A '
             'farmer wants to fence the entire plot with barbed wire that costs 20 rupees per metre. To calculate the '
             'total fencing cost, we first find the perimeter: two times 25 plus 10, which equals 70 metres of fence. '
             'Then we multiply 70 metres by 20 rupees, giving a total cost of 1,400 rupees! Notice that fencing goes '
             'along the border, so it uses perimeter, not area! Now consider a second problem: a gardener has a '
             'rectangular flowerbed with an area of 72 square metres. The length is known to be 9 metres, but what is '
             'its breadth? Since Area equals Length times Breadth, we divide the area by the length: 72 divided by 9 '
             'equals 8 metres! For composite L-shaped or T-shaped regions, you can split the complex shape into two '
             'simpler rectangles, calculate the area of each rectangle separately, and then add their areas together. '
             'Always identify whether the practical question asks for boundary length or surface coverage before '
             'choosing your mathematical formulas and problem-solving strategy.',
  'content_html': '\n'
                  '<div class="space-y-4">\n'
                  '    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">\n'
                  '        <!-- Problem 1: Fencing Cost -->\n'
                  '        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-4">\n'
                  '            <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Type A: '
                  'Boundary Cost</span>\n'
                  '            <h5 class="text-white font-bold text-sm mt-1">Fencing a 25 m × 10 m Field</h5>\n'
                  '            <div class="mt-2 text-xs text-slate-300 space-y-1.5 font-mono bg-slate-900/80 p-3 '
                  'rounded border border-slate-700">\n'
                  '                <p>1. Perimeter = 2 × (25 + 10) = <span class="text-cyan-400 font-bold">70 '
                  'm</span></p>\n'
                  '                <p>2. Rate = ₹20 per metre</p>\n'
                  '                <p>3. Cost = 70 × 20 = <span class="text-emerald-400 font-bold">₹1,400</span></p>\n'
                  '            </div>\n'
                  '            <p class="text-xs text-slate-400 mt-2">Rule: Fencing = Perimeter × Rate per unit '
                  'length.</p>\n'
                  '        </div>\n'
                  '\n'
                  '        <!-- Problem 2: Missing Dimension -->\n'
                  '        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-4">\n'
                  '            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">Type B: '
                  'Missing Side</span>\n'
                  '            <h5 class="text-white font-bold text-sm mt-1">Flowerbed: Area = 72 m², Length = 9 '
                  'm</h5>\n'
                  '            <div class="mt-2 text-xs text-slate-300 space-y-1.5 font-mono bg-slate-900/80 p-3 '
                  'rounded border border-slate-700">\n'
                  '                <p>1. Area = Length × Breadth</p>\n'
                  '                <p>2. 72 = 9 × Breadth</p>\n'
                  '                <p>3. Breadth = 72 ÷ 9 = <span class="text-indigo-400 font-bold">8 m</span></p>\n'
                  '            </div>\n'
                  '            <p class="text-xs text-slate-400 mt-2">Rule: Breadth = Area ÷ Length (or Length = Area '
                  '÷ Breadth).</p>\n'
                  '        </div>\n'
                  '    </div>\n'
                  '\n'
                  '    <!-- Composite Shapes Tip -->\n'
                  '    <div class="bg-gradient-to-r from-teal-950/40 to-slate-900 border border-teal-500/30 rounded-xl '
                  'p-3 text-xs">\n'
                  '        <span class="text-teal-300 font-bold uppercase tracking-wider">Composite Shapes '
                  'Tip:</span>\n'
                  '        <span class="text-slate-300 ml-2">\n'
                  '            To find the area of an L-shape, partition it with a dotted line into two rectangles, '
                  'find each area, and add them together!\n'
                  '        </span>\n'
                  '    </div>\n'
                  '</div>\n',
  'checkpoints': [{'question': 'A square courtyard of side 15 m needs fencing. If wire costs ₹10 per metre, what is '
                               'the total fencing cost?',
                   'options': ['₹600 (Perimeter = 60 m; 60 × 10 = ₹600)',
                               '₹2,250 (Area = 225 m²; 225 × 10 = ₹2,250)',
                               '₹150 (15 × 10 = ₹150)',
                               '₹300 (Perimeter = 30 m; 30 × 10 = ₹300)'],
                   'answer': 0,
                   'explanation': 'Fencing requires perimeter: P = 4 × 15 = 60 m. Total cost = 60 × ₹10 = ₹600. (Do '
                                  'not confuse area with fencing!).',
                   'hint': 'Find the perimeter of the square first, then multiply by ₹10.'},
                  {'question': 'A rectangular swimming pool has an area of 120 m² and a breadth of 8 m. What is its '
                               'length?',
                   'options': ['15 m (120 ÷ 8 = 15)',
                               '112 m (120 - 8 = 112)',
                               '960 m (120 × 8 = 960)',
                               '12 m (120 ÷ 10 = 12)'],
                   'answer': 0,
                   'explanation': 'Length = Area ÷ Breadth = 120 ÷ 8 = 15 m. Check: 15 × 8 = 120 m².',
                   'hint': 'Divide total area by breadth.'}]},
 {'id': 16,
  'title': 'Perimeter Dice Game',
  'tagline': 'Two-Player Strategic Math Game • Roll, Append Square Tiles, and Race to Perimeter 24',
  'lecture': 'To celebrate everything we have discovered about perimeter and area, class five students play the '
             'exciting Perimeter Building Dice Game! This thrilling two-player game brings geometry to life through '
             'playful strategy. Players take turns rolling a standard six-sided die. When it is your turn, the number '
             'rolled indicates how many unit square tiles you must add to your expanding geometric creation. Each new '
             'tile must connect firmly along at least one complete edge of an existing tile: no diagonal corners '
             'allowed! After attaching your new tiles, you must recalculate the total outer perimeter of your shape. '
             'Here is the strategic twist: if you attach your tiles in a long straight line, each new tile exposes two '
             'new border edges, causing your perimeter to surge! However, if you tuck tiles snugly into inside '
             'corners, edges touch and cancel out, keeping your perimeter compact. The goal of the game is to be the '
             'first player to construct a valid connected shape whose outer boundary perimeter reaches exactly 24 '
             'units! Through this hands-on interactive gameplay, you develop sharp tactical intuition for how '
             'edge-sharing transforms boundary perimeter while simultaneously growing the total enclosed area and '
             'surface coverage on the game grid.',
  'content_html': '\n'
                  '<div class="space-y-4">\n'
                  '    <div class="bg-gradient-to-r from-amber-900/40 via-yellow-900/30 to-amber-900/40 border '
                  'border-yellow-500/30 rounded-xl p-4">\n'
                  '        <h4 class="text-yellow-300 font-bold text-sm tracking-wider uppercase mb-1">Game Rules & '
                  'Strategy</h4>\n'
                  '        <p class="text-slate-200 text-sm leading-relaxed">\n'
                  '            Players take turns rolling a die, adding that number of unit tiles edge-to-edge, and '
                  "updating their shape's outer perimeter.\n"
                  '            <span class="text-emerald-300 font-bold">Goal: Reach an exact perimeter of 24 '
                  'units!</span>\n'
                  '        </p>\n'
                  '    </div>\n'
                  '\n'
                  '    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">\n'
                  '        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-4">\n'
                  '            <span class="text-xs font-bold text-rose-400 uppercase tracking-wider">Perimeter '
                  'Expansion Tactic</span>\n'
                  '            <h5 class="text-white font-bold text-sm mt-1">Linear Extension</h5>\n'
                  '            <p class="text-xs text-slate-300 mt-2 leading-relaxed">\n'
                  '                Adding tiles in a straight chain exposes 2 new exterior edges per tile (+2 to '
                  'perimeter). Great for surging toward 24 quickly!\n'
                  '            </p>\n'
                  '            <div class="mt-2 text-xs font-mono text-rose-300 bg-slate-900/80 p-2 rounded border '
                  'border-rose-500/30">\n'
                  '                1 tile: P=4 ➔ 2 tiles: P=6 ➔ 3 tiles: P=8\n'
                  '            </div>\n'
                  '        </div>\n'
                  '\n'
                  '        <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-4">\n'
                  '            <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Perimeter '
                  'Control Tactic</span>\n'
                  '            <h5 class="text-white font-bold text-sm mt-1">Corner Filling</h5>\n'
                  '            <p class="text-xs text-slate-300 mt-2 leading-relaxed">\n'
                  '                Tucking a tile into an inside L-corner touches 2 existing edges, adding 0 net edges '
                  'to the outer perimeter (+0 change)!\n'
                  '            </p>\n'
                  '            <div class="mt-2 text-xs font-mono text-cyan-300 bg-slate-900/80 p-2 rounded border '
                  'border-cyan-500/30">\n'
                  '                Corner tuck: +1 tile, +0 to perimeter!\n'
                  '            </div>\n'
                  '        </div>\n'
                  '    </div>\n'
                  '\n'
                  '    <div class="p-3 bg-indigo-950/40 border border-indigo-500/30 rounded-xl flex items-center '
                  'justify-between text-xs">\n'
                  '        <span class="text-indigo-300 font-bold">Rule Check:</span>\n'
                  '        <span class="text-slate-300">Tiles must touch along whole edges (no vertex-only diagonal '
                  'contacts allowed).</span>\n'
                  '    </div>\n'
                  '</div>\n',
  'checkpoints': [{'question': 'If you add 1 square tile to the end of a straight strip of squares, how much does the '
                               'perimeter increase?',
                   'options': ['By 2 units', 'By 4 units', 'By 1 unit', 'By 0 units'],
                   'answer': 0,
                   'explanation': 'The new tile has 4 edges. 1 edge connects to the existing strip (hidden), 1 edge '
                                  'covers an existing boundary edge, and 3 edges become new boundary. Net change = +3 '
                                  '- 1 = +2 units.',
                   'hint': 'Count how many new outer sides are exposed minus the edge that got covered.'},
                  {'question': "If you place a unit tile into an inside 'L' corner where 2 edges touch existing tiles, "
                               'how does the perimeter change?',
                   'options': ['Perimeter does not change (+0 units)',
                               'Perimeter increases by 2 units',
                               'Perimeter decreases by 2 units',
                               'Perimeter increases by 4 units'],
                   'answer': 0,
                   'explanation': '2 edges of the new tile touch the existing shape (replacing 2 boundary edges) and 2 '
                                  'edges become new boundary. Net perimeter change = +2 - 2 = 0!',
                   'hint': 'Two edges are covered, and two new outer edges are created.'}]},
 {'id': 17,
  'title': 'Challenge 1',
  'tagline': 'Mastery Challenge 1 • Boundary Lengths & Regular Polygons',
  'lecture': 'Welcome to Mastery Challenge 1. In this interactive session, you will test your understanding of '
             'boundary lengths, perimeter calculations, and the geometry of regular polygons.',
  'content_html': '\n'
                  '<div class="space-y-4">\n'
                  '    <div class="bg-gradient-to-r from-blue-900/40 to-indigo-900/40 border border-blue-500/30 '
                  'rounded-xl p-4">\n'
                  '        <h4 class="text-blue-300 font-bold text-sm tracking-wider uppercase mb-1">Challenge '
                  'Overview</h4>\n'
                  '        <p class="text-slate-200 text-sm leading-relaxed">\n'
                  '            Test your skills on finding outer boundaries, sum of all sides, regular polygons, and '
                  'drawing rectangles with fixed perimeters. Solve all 10 questions to unlock the next level!\n'
                  '        </p>\n'
                  '    </div>\n'
                  '</div>\n',
  'questions': [{'id': 1,
                 'question': 'What is the mathematical definition of perimeter?',
                 'options': ['The total length of the continuous outer boundary of a closed 2D shape',
                             'The total flat surface area enclosed inside a shape',
                             'The number of square units required to cover a shape completely',
                             'The product of all side lengths of a polygon'],
                 'answer': 0,
                 'hint': "Think about the lace ribbon running around grandmother's quilt.",
                 'explanation': 'Perimeter is strictly a 1D measurement of the outer boundary length around a closed '
                                'shape.',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. <strong>Perimeter</strong> comes from Greek <em>peri</em> (around) and '
                                  '<em>metron</em> (measure).</p>\n'
                                  '    <p>2. It measures the total distance traveled along the outer border or edge of '
                                  'a closed shape.</p>\n'
                                  '    <p>3. Surface coverage inside is called <em>area</em>, while outer edge length '
                                  'is called <em>perimeter</em>.</p>\n'
                                  '</div>\n'},
                {'id': 2,
                 'question': "Grandmother's quilt is 2 metres long and 1.5 metres wide. How many metres of lace border "
                             'ribbon are needed to trim all four edges?',
                 'options': ['7 metres', '3 metres', '3.5 metres', '14 metres'],
                 'answer': 0,
                 'hint': 'Add length and breadth, then double it: P = 2 × (L + B).',
                 'explanation': 'P = 2 × (2 m + 1.5 m) = 2 × 3.5 m = 7 metres.',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. Length (L) = 2 m, Breadth (B) = 1.5 m.</p>\n'
                                  '    <p>2. Formula: Perimeter = 2 × (L + B).</p>\n'
                                  '    <p>3. P = 2 × (2 + 1.5) = 2 × 3.5 = <strong>7 metres</strong>.</p>\n'
                                  '</div>\n'},
                {'id': 3,
                 'question': 'An equilateral triangle has sides measuring 8 cm each. What is its perimeter?',
                 'options': ['24 cm', '16 cm', '32 cm', '64 cm'],
                 'answer': 0,
                 'hint': 'An equilateral triangle has 3 equal sides.',
                 'explanation': 'Perimeter = 3 × side = 3 × 8 cm = 24 cm.',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. Number of sides in an equilateral triangle = 3.</p>\n'
                                  '    <p>2. Side length s = 8 cm.</p>\n'
                                  '    <p>3. Perimeter = 3 × 8 = <strong>24 cm</strong>.</p>\n'
                                  '</div>\n'},
                {'id': 4,
                 'question': 'A regular hexagon has a perimeter of 42 cm. What is the length of each side?',
                 'options': ['7 cm', '6 cm', '8 cm', '14 cm'],
                 'answer': 0,
                 'hint': 'A regular hexagon has 6 equal sides: Side = Perimeter ÷ 6.',
                 'explanation': 'Side = 42 cm ÷ 6 = 7 cm.',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. Regular hexagon has 6 equal sides.</p>\n'
                                  '    <p>2. Formula: Side = Perimeter ÷ 6.</p>\n'
                                  '    <p>3. Side = 42 ÷ 6 = <strong>7 cm</strong>.</p>\n'
                                  '</div>\n'},
                {'id': 5,
                 'question': 'Which formula gives the perimeter of a regular pentagon with side length s?',
                 'options': ['5 × s', '4 × s', 's × s', '6 × s'],
                 'answer': 0,
                 'hint': 'A pentagon has 5 sides.',
                 'explanation': 'A regular pentagon has 5 equal sides, so Perimeter = 5 × s.',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. A pentagon is a 5-sided polygon.</p>\n'
                                  '    <p>2. In a regular pentagon, all 5 sides are equal.</p>\n'
                                  '    <p>3. Perimeter = s + s + s + s + s = <strong>5 × s</strong>.</p>\n'
                                  '</div>\n'},
                {'id': 6,
                 'question': 'If you want to draw a rectangle with a perimeter of 26 cm, what must the sum of its '
                             'length and breadth be?',
                 'options': ['13 cm (half of 26 cm)', '26 cm', '52 cm', '6.5 cm'],
                 'answer': 0,
                 'hint': 'Perimeter = 2 × (L + B), so L + B = Perimeter ÷ 2.',
                 'explanation': 'Sum of length and breadth = 26 ÷ 2 = 13 cm.',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. Formula: P = 2 × (L + B).</p>\n'
                                  '    <p>2. L + B = P ÷ 2.</p>\n'
                                  '    <p>3. L + B = 26 ÷ 2 = <strong>13 cm</strong>.</p>\n'
                                  '</div>\n'},
                {'id': 7,
                 'question': 'Which of the following whole-number pairs can form a rectangle with a perimeter of 18 '
                             'cm?',
                 'options': ['7 cm and 2 cm', '6 cm and 4 cm', '9 cm and 9 cm', '10 cm and 8 cm'],
                 'answer': 0,
                 'hint': 'The sum of L and B must equal 18 ÷ 2 = 9 cm.',
                 'explanation': '7 + 2 = 9 cm, giving P = 2 × (7 + 2) = 18 cm. (6 + 4 = 10; 9 + 9 = 18).',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. Target perimeter = 18 cm, so L + B = 18 ÷ 2 = 9 cm.</p>\n'
                                  '    <p>2. Check 7 + 2: 7 + 2 = 9 cm. P = 2 × 9 = 18 cm (Valid!).</p>\n'
                                  '    <p>3. Check 6 + 4: 6 + 4 = 10 cm. P = 20 cm (Invalid).</p>\n'
                                  '</div>\n'},
                {'id': 8,
                 'question': 'A square photo frame has a side of 12 cm. What is the length of wooden moulding required '
                             'to make the frame?',
                 'options': ['48 cm', '24 cm', '144 cm', '36 cm'],
                 'answer': 0,
                 'hint': 'A square frame has 4 equal sides.',
                 'explanation': 'Perimeter = 4 × side = 4 × 12 cm = 48 cm.',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. Wooden moulding forms the outer border (perimeter).</p>\n'
                                  '    <p>2. Square perimeter = 4 × Side.</p>\n'
                                  '    <p>3. P = 4 × 12 = <strong>48 cm</strong>.</p>\n'
                                  '</div>\n'},
                {'id': 9,
                 'question': 'A triangular park has sides of 25 m, 30 m, and 35 m. What distance does an athlete run '
                             'in completing one full round of the park?',
                 'options': ['90 m', '60 m', '80 m', '105 m'],
                 'answer': 0,
                 'hint': 'Add all three sides: 25 + 30 + 35.',
                 'explanation': 'Perimeter = 25 + 30 + 35 = 90 metres.',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. Running one round of a park covers its perimeter.</p>\n'
                                  '    <p>2. Perimeter = Side 1 + Side 2 + Side 3.</p>\n'
                                  '    <p>3. P = 25 + 30 + 35 = <strong>90 m</strong>.</p>\n'
                                  '</div>\n'},
                {'id': 10,
                 'question': 'A regular octagon has an outer perimeter of 64 cm. What is the length of one side?',
                 'options': ['8 cm', '7 cm', '6 cm', '16 cm'],
                 'answer': 0,
                 'hint': 'An octagon has 8 equal sides: Side = 64 ÷ 8.',
                 'explanation': 'Side = 64 cm ÷ 8 = 8 cm.',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. An octagon has 8 sides.</p>\n'
                                  '    <p>2. For a regular octagon, all 8 sides are equal.</p>\n'
                                  '    <p>3. Side = 64 ÷ 8 = <strong>8 cm</strong>.</p>\n'
                                  '</div>\n'}]},
 {'id': 18,
  'title': 'Challenge 2',
  'tagline': 'Mastery Challenge 2 • Area, Tiling & Grid Estimation',
  'lecture': 'Welcome to Mastery Challenge 2. In this round, you will test your knowledge of tessellation, unit '
             'squares, grid counting rules, and estimating irregular handprints and leaves.',
  'content_html': '\n'
                  '<div class="space-y-4">\n'
                  '    <div class="bg-gradient-to-r from-teal-900/40 to-emerald-900/40 border border-teal-500/30 '
                  'rounded-xl p-4">\n'
                  '        <h4 class="text-teal-300 font-bold text-sm tracking-wider uppercase mb-1">Challenge '
                  'Overview</h4>\n'
                  '        <p class="text-slate-200 text-sm leading-relaxed">\n'
                  '            Test your understanding of surface coverage, why circles leave gaps, unit square '
                  'definitions, counting whole and partial squares, and palm/leaf area estimation.\n'
                  '        </p>\n'
                  '    </div>\n'
                  '</div>\n',
  'questions': [{'id': 1,
                 'question': "What is meant by the geometric term 'tessellation'?",
                 'options': ['Covering a flat surface completely with shapes without leaving any gaps or overlaps',
                             'Measuring the outer boundary of a polygon with a ruler',
                             'Drawing a shape that has reflectional symmetry',
                             'Dividing a shape into two equal halves'],
                 'answer': 0,
                 'hint': 'Think about tiling a floor perfectly with square tiles.',
                 'explanation': 'A tessellation or tiling is covering a plane using geometric shapes without overlaps '
                                'or empty spaces.',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. <strong>Tessellation</strong> means tiling a surface with repeating '
                                  'geometric shapes.</p>\n'
                                  '    <p>2. Rule 1: No gaps between tiles.</p>\n'
                                  '    <p>3. Rule 2: No overlapping edges.</p>\n'
                                  '</div>\n'},
                {'id': 2,
                 'question': 'Why are circles unable to tessellate a flat surface?',
                 'options': ['Because curved boundaries leave empty diamond-shaped gaps between adjacent circles',
                             'Because circles have infinite sides',
                             'Because circles have no area',
                             'Because circles cannot be measured in centimetres'],
                 'answer': 0,
                 'hint': 'Think of placing circular coins next to each other on a table.',
                 'explanation': 'Curved edges cannot meet edge-to-edge; they leave empty voids (interstices) between '
                                'circles.',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. Circular edges curve away from contact points.</p>\n'
                                  '    <p>2. When circular coins touch, diamond-shaped gaps are left behind.</p>\n'
                                  '    <p>3. Therefore, circles cannot tile a flat plane completely without leaving '
                                  'empty gaps.</p>\n'
                                  '</div>\n'},
                {'id': 3,
                 'question': 'How many half-triangle tiles are needed to cover the same area as 1 full unit square?',
                 'options': ['2 half-triangles', '4 half-triangles', '1 half-triangle', '3 half-triangles'],
                 'answer': 0,
                 'hint': 'Cutting a square diagonally produces 2 identical triangles.',
                 'explanation': 'Two diagonal half-triangles join together to make 1 full unit square.',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. Cut a 1 cm × 1 cm square diagonally into 2 triangles.</p>\n'
                                  '    <p>2. Each triangle has an area of 1/2 cm².</p>\n'
                                  '    <p>3. Two half-triangles = 1/2 + 1/2 = <strong>1 unit square</strong>.</p>\n'
                                  '</div>\n'},
                {'id': 4,
                 'question': 'What is the area of a square whose sides are each 1 centimetre long?',
                 'options': ['1 square centimetre (1 cm²)',
                             '4 centimetres (4 cm)',
                             '2 square centimetres (2 cm²)',
                             '1 centimetre (1 cm)'],
                 'answer': 0,
                 'hint': 'Area = 1 cm × 1 cm.',
                 'explanation': 'Area of a unit square = 1 cm × 1 cm = 1 cm².',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. Side s = 1 cm.</p>\n'
                                  '    <p>2. Area = s × s = 1 cm × 1 cm = <strong>1 cm²</strong>.</p>\n'
                                  '    <p>3. (Note: 4 cm is its perimeter, not its area!).</p>\n'
                                  '</div>\n'},
                {'id': 5,
                 'question': 'When estimating area on a 1 cm² grid, how do we count a square that is more than half '
                             'covered by a shape?',
                 'options': ['Count it as 1 full square',
                             'Ignore it completely',
                             'Count it as 1/2 square',
                             'Count it as 2 squares'],
                 'answer': 0,
                 'hint': 'The standard rule: full squares = 1, more than half = 1, less than half = 0.',
                 'explanation': 'Squares more than half covered are rounded up and counted as 1 full square.',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. Standard Grid Counting Convention:</p>\n'
                                  '    <p>• Fully covered: Count as 1.</p>\n'
                                  '    <p>• More than half covered: <strong>Count as 1</strong>.</p>\n'
                                  '    <p>• Exactly half covered: Count as 1/2 (pair them up).</p>\n'
                                  '    <p>• Less than half covered: Ignore (0).</p>\n'
                                  '</div>\n'},
                {'id': 6,
                 'question': 'A traced shape covers 14 fully enclosed squares and 6 exactly half-covered squares on a '
                             '1 cm grid. What is its total area?',
                 'options': ['17 cm² (14 + 3)', '20 cm² (14 + 6)', '15 cm² (14 + 1)', '12 cm² (14 - 2)'],
                 'answer': 0,
                 'hint': 'Each pair of half-covered squares equals 1 full square: 6 halves = 3 full squares.',
                 'explanation': 'Total area = 14 + (6 × 0.5) = 14 + 3 = 17 cm².',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. Fully covered squares = 14 cm².</p>\n'
                                  '    <p>2. Half-covered squares = 6 × 1/2 = 3 cm².</p>\n'
                                  '    <p>3. Total Area = 14 + 3 = <strong>17 cm²</strong>.</p>\n'
                                  '</div>\n'},
                {'id': 7,
                 'question': 'When tracing a handprint on a 1 cm² grid, which student has the larger handprint?',
                 'options': ['Adrit whose handprint covers 52 unit squares',
                             'Preetha whose handprint covers 46 unit squares',
                             'Both handprints have equal surface area',
                             'It cannot be determined without measuring fingers'],
                 'answer': 0,
                 'hint': 'Compare the number of unit squares covered: 52 vs 46.',
                 'explanation': '52 cm² > 46 cm², so Adrit has the larger handprint surface area.',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  "    <p>1. Adrit's hand covers 52 square centimetres.</p>\n"
                                  "    <p>2. Preetha's hand covers 46 square centimetres.</p>\n"
                                  '    <p>3. Since 52 > 46, <strong>Adrit</strong> has the larger handprint.</p>\n'
                                  '</div>\n'},
                {'id': 8,
                 'question': 'Rank the following leaves in order from smallest to largest surface area: Peepal, '
                             'Coriander, Mango.',
                 'options': ['Coriander < Mango < Peepal',
                             'Peepal < Mango < Coriander',
                             'Mango < Coriander < Peepal',
                             'Peepal < Coriander < Mango'],
                 'answer': 0,
                 'hint': 'A coriander leaflet is tiny; a peepal leaf is very broad.',
                 'explanation': 'Coriander (~2-4 cm²) < Mango (~25-35 cm²) < Peepal (~65-80 cm²).',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. Coriander: small compound leaflet (~3 cm²).</p>\n'
                                  '    <p>2. Mango: medium slender leaf (~30 cm²).</p>\n'
                                  '    <p>3. Peepal: broad heart-shaped leaf (~70 cm²).</p>\n'
                                  '    <p>4. Ascending order: <strong>Coriander < Mango < Peepal</strong>.</p>\n'
                                  '</div>\n'},
                {'id': 9,
                 'question': 'If a tabletop is completely covered by 24 identical mathematics textbooks, what is the '
                             'area of the table in textbook units?',
                 'options': ['24 textbook units', '12 textbook units', '48 textbook units', '6 textbook units'],
                 'answer': 0,
                 'hint': 'The area is the number of non-standard units needed to cover the surface.',
                 'explanation': 'Area = 24 textbook units, because 24 books cover the surface without gaps or '
                                'overlaps.',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. A non-standard unit of area is any consistent object used to tile a '
                                  'surface.</p>\n'
                                  '    <p>2. 24 books cover the table surface without gaps.</p>\n'
                                  '    <p>3. Table Area = <strong>24 textbook units</strong>.</p>\n'
                                  '</div>\n'},
                {'id': 10,
                 'question': 'Why do mathematicians prefer a standard 1 cm² grid over non-standard units like pencil '
                             'boxes or erasers?',
                 'options': ['Because 1 cm² is universally uniform, standardized, and communicates identical sizes '
                             'across the world',
                             'Because pencil boxes are too heavy to carry',
                             'Because squares are the only shapes that exist',
                             'Because erasers cannot be placed next to each other'],
                 'answer': 0,
                 'hint': 'Think about why standard units were invented.',
                 'explanation': 'Standard units like cm² ensure universal consistency regardless of who is measuring.',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. Non-standard units vary in size between brands and individuals.</p>\n'
                                  '    <p>2. Standard 1 cm² units are identical across the globe.</p>\n'
                                  '    <p>3. They allow reproducible, accurate, and universal measurement.</p>\n'
                                  '</div>\n'}]},
 {'id': 19,
  'title': 'Challenge 3',
  'tagline': 'Mastery Challenge 3 • Area vs Perimeter & Rectangle Formulas',
  'lecture': 'Welcome to Mastery Challenge 3. In this section, you will evaluate the mathematical relationships '
             'between area and perimeter, row-column arrays, and the formulas for rectangles and squares.',
  'content_html': '\n'
                  '<div class="space-y-4">\n'
                  '    <div class="bg-gradient-to-r from-purple-900/40 to-pink-900/40 border border-purple-500/30 '
                  'rounded-xl p-4">\n'
                  '        <h4 class="text-purple-300 font-bold text-sm tracking-wider uppercase mb-1">Challenge '
                  'Overview</h4>\n'
                  '        <p class="text-slate-200 text-sm leading-relaxed">\n'
                  '            Test your mastery of fixed area variations, fixed perimeter optimizations, array '
                  'multiplication, rectangle formulas, and square properties.\n'
                  '        </p>\n'
                  '    </div>\n'
                  '</div>\n',
  'questions': [{'id': 1,
                 'question': 'Three rectangles each have an area of 12 cm²: (1 × 12), (2 × 6), and (3 × 4). Which one '
                             'has the largest perimeter?',
                 'options': ['The 1 cm × 12 cm rectangle (P = 26 cm)',
                             'The 2 cm × 6 cm rectangle (P = 16 cm)',
                             'The 3 cm × 4 cm rectangle (P = 14 cm)',
                             'All three have identical perimeters'],
                 'answer': 0,
                 'hint': 'The most elongated, stretched-out shape has the largest perimeter.',
                 'explanation': 'P for 1 × 12 = 2 × (1 + 12) = 26 cm, which is greater than 16 cm and 14 cm.',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. P(1 × 12) = 2 × (1 + 12) = 26 cm.</p>\n'
                                  '    <p>2. P(2 × 6) = 2 × (2 + 6) = 16 cm.</p>\n'
                                  '    <p>3. P(3 × 4) = 2 × (3 + 4) = 14 cm.</p>\n'
                                  '    <p>4. The long thin strip <strong>1 cm × 12 cm</strong> has the largest '
                                  'perimeter (26 cm).</p>\n'
                                  '</div>\n'},
                {'id': 2,
                 'question': 'For a fixed perimeter of 24 cm, which rectangular shape encloses the maximum possible '
                             'area?',
                 'options': ['A 6 cm × 6 cm square (Area = 36 cm²)',
                             'An 8 cm × 4 cm rectangle (Area = 32 cm²)',
                             'A 10 cm × 2 cm rectangle (Area = 20 cm²)',
                             'An 11 cm × 1 cm rectangle (Area = 11 cm²)'],
                 'answer': 0,
                 'hint': 'A square maximizes area for any fixed perimeter.',
                 'explanation': 'Among all rectangles with P = 24 cm, the 6 × 6 square achieves maximum area: 36 cm².',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. Fixed perimeter P = 24 cm ➔ L + B = 12 cm.</p>\n'
                                  '    <p>2. Check products: 11 × 1 = 11, 10 × 2 = 20, 8 × 4 = 32, 6 × 6 = 36.</p>\n'
                                  '    <p>3. The <strong>6 cm × 6 cm square</strong> maximizes area at 36 cm².</p>\n'
                                  '</div>\n'},
                {'id': 3,
                 'question': 'A grid has 6 horizontal rows and 9 vertical columns of unit squares. What is the total '
                             'area?',
                 'options': ['54 cm²', '30 cm²', '15 cm²', '60 cm²'],
                 'answer': 0,
                 'hint': 'Multiply rows by columns: 6 × 9.',
                 'explanation': 'Total Area = Rows × Columns = 6 × 9 = 54 cm².',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. Number of rows = 6.</p>\n'
                                  '    <p>2. Number of columns = 9.</p>\n'
                                  '    <p>3. Area = 6 × 9 = <strong>54 cm²</strong>.</p>\n'
                                  '</div>\n'},
                {'id': 4,
                 'question': 'What is the area of a rectangular classroom blackboard measuring 4 metres in length and '
                             '2 metres in breadth?',
                 'options': ['8 m²', '12 m', '16 m²', '6 m²'],
                 'answer': 0,
                 'hint': 'Area = Length × Breadth = 4 × 2.',
                 'explanation': 'Area = 4 m × 2 m = 8 m².',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. Length = 4 m, Breadth = 2 m.</p>\n'
                                  '    <p>2. Formula: Area = Length × Breadth.</p>\n'
                                  '    <p>3. Area = 4 × 2 = <strong>8 m²</strong>.</p>\n'
                                  '</div>\n'},
                {'id': 5,
                 'question': 'What is the perimeter of a rectangular rug measuring 9 metres long and 5 metres wide?',
                 'options': ['28 metres', '45 square metres', '14 metres', '56 metres'],
                 'answer': 0,
                 'hint': 'P = 2 × (L + B) = 2 × (9 + 5).',
                 'explanation': 'Perimeter = 2 × (9 + 5) = 2 × 14 = 28 m.',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. Length = 9 m, Breadth = 5 m.</p>\n'
                                  '    <p>2. Perimeter = 2 × (9 + 5) = 2 × 14 = <strong>28 m</strong>.</p>\n'
                                  '    <p>3. (Note: 45 m² is its area, not its perimeter!).</p>\n'
                                  '</div>\n'},
                {'id': 6,
                 'question': 'A square garden has sides of 9 metres. What are its perimeter and area?',
                 'options': ['Perimeter = 36 m; Area = 81 m²',
                             'Perimeter = 81 m; Area = 36 m²',
                             'Perimeter = 18 m; Area = 81 m²',
                             'Perimeter = 36 m; Area = 18 m²'],
                 'answer': 0,
                 'hint': 'P = 4 × 9; Area = 9 × 9.',
                 'explanation': 'Perimeter = 4 × 9 = 36 m. Area = 9 × 9 = 81 m².',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. Side s = 9 m.</p>\n'
                                  '    <p>2. Perimeter = 4 × s = 4 × 9 = <strong>36 m</strong>.</p>\n'
                                  '    <p>3. Area = s × s = 9 × 9 = <strong>81 m²</strong>.</p>\n'
                                  '</div>\n'},
                {'id': 7,
                 'question': 'If a square has an area of 49 cm², what is its perimeter?',
                 'options': ['28 cm', '14 cm', '49 cm', '36 cm'],
                 'answer': 0,
                 'hint': 'First find the side: what number multiplied by itself gives 49? Then multiply by 4.',
                 'explanation': 'Side = 7 cm (since 7 × 7 = 49). Perimeter = 4 × 7 = 28 cm.',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. Area = s × s = 49 cm² ➔ s = 7 cm.</p>\n'
                                  '    <p>2. Perimeter = 4 × s = 4 × 7 = <strong>28 cm</strong>.</p>\n'
                                  '</div>\n'},
                {'id': 8,
                 'question': 'A rectangle has an area of 60 cm² and a length of 12 cm. What is its breadth?',
                 'options': ['5 cm', '48 cm', '10 cm', '6 cm'],
                 'answer': 0,
                 'hint': 'Breadth = Area ÷ Length = 60 ÷ 12.',
                 'explanation': 'Breadth = 60 ÷ 12 = 5 cm.',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. Area = Length × Breadth.</p>\n'
                                  '    <p>2. 60 = 12 × Breadth.</p>\n'
                                  '    <p>3. Breadth = 60 ÷ 12 = <strong>5 cm</strong>.</p>\n'
                                  '</div>\n'},
                {'id': 9,
                 'question': 'If you double both the length and breadth of a rectangle, what happens to its area?',
                 'options': ['The area becomes 4 times as large',
                             'The area doubles (becomes 2 times)',
                             'The area remains the same',
                             'The area increases by 2 cm²'],
                 'answer': 0,
                 'hint': 'Original: L × B. New: (2 × L) × (2 × B) = 4 × (L × B).',
                 'explanation': 'Doubling both dimensions multiplies the area by 2 × 2 = 4 times.',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. Original Area = L × B.</p>\n'
                                  '    <p>2. New Area = (2L) × (2B) = 4 × (L × B).</p>\n'
                                  '    <p>3. The area increases by a factor of <strong>4</strong>.</p>\n'
                                  '</div>\n'},
                {'id': 10,
                 'question': 'Which of the following statements is ALWAYS true?',
                 'options': ['Perimeter is measured in linear units (cm, m), while area is measured in square units '
                             '(cm², m²)',
                             'Two shapes with the same area must always have the exact same perimeter',
                             'Two shapes with the same perimeter must always have the exact same area',
                             'A longer rectangle always has a larger area than a square'],
                 'answer': 0,
                 'hint': 'Consider the difference between 1D boundary length and 2D surface coverage.',
                 'explanation': 'Perimeter is 1-dimensional (cm, m); Area is 2-dimensional (cm², m²).',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. Perimeter measures distance around boundary ➔ linear units (cm, m).</p>\n'
                                  '    <p>2. Area measures surface coverage ➔ square units (cm², m²).</p>\n'
                                  '    <p>3. Shapes can share area with different perimeters, and vice versa.</p>\n'
                                  '</div>\n'}]},
 {'id': 20,
  'title': 'Challenge 4',
  'tagline': 'Mastery Challenge 4 • Real-World Costs & Strategic Math',
  'lecture': 'Welcome to Mastery Challenge 4. In this final challenge, you will prove your mastery of fencing costs, '
             'real-world metric scales, composite surface regions, and Perimeter Dice Game strategies.',
  'content_html': '\n'
                  '<div class="space-y-4">\n'
                  '    <div class="bg-gradient-to-r from-amber-900/40 to-rose-900/40 border border-amber-500/30 '
                  'rounded-xl p-4">\n'
                  '        <h4 class="text-amber-300 font-bold text-sm tracking-wider uppercase mb-1">Final Challenge '
                  'Overview</h4>\n'
                  '        <p class="text-slate-200 text-sm leading-relaxed">\n'
                  '            Apply your geometric knowledge to practical word problems: calculating fencing costs, '
                  'tiling floors, solving composite L-shapes, and mastering the Perimeter Dice Game.\n'
                  '        </p>\n'
                  '    </div>\n'
                  '</div>\n',
  'questions': [{'id': 1,
                 'question': 'A farmer has a rectangular field 30 metres long and 20 metres wide. He wants to fence it '
                             'with wire costing ₹15 per metre. What is the total cost?',
                 'options': ['₹1,500', '₹9,000', '₹750', '₹3,000'],
                 'answer': 0,
                 'hint': 'Fencing requires perimeter: P = 2 × (30 + 20) = 100 m. Cost = 100 × ₹15.',
                 'explanation': 'Perimeter = 2 × (30 + 20) = 100 m. Total cost = 100 m × ₹15/m = ₹1,500.',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. Perimeter = 2 × (30 + 20) = 2 × 50 = 100 m.</p>\n'
                                  '    <p>2. Rate = ₹15 per metre.</p>\n'
                                  '    <p>3. Total Cost = 100 × 15 = <strong>₹1,500</strong>.</p>\n'
                                  '</div>\n'},
                {'id': 2,
                 'question': 'A classroom floor is 10 metres long and 8 metres wide. It is to be paved with square '
                             'tiles of side 1 metre. How many tiles are required?',
                 'options': ['80 tiles', '36 tiles', '40 tiles', '100 tiles'],
                 'answer': 0,
                 'hint': 'Floor Area = 10 × 8 = 80 m². Each tile covers 1 m².',
                 'explanation': 'Number of tiles = Floor Area ÷ Tile Area = (10 × 8) ÷ (1 × 1) = 80 tiles.',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. Floor Area = 10 m × 8 m = 80 m².</p>\n'
                                  '    <p>2. Area of 1 tile = 1 m × 1 m = 1 m².</p>\n'
                                  '    <p>3. Number of tiles = 80 ÷ 1 = <strong>80 tiles</strong>.</p>\n'
                                  '</div>\n'},
                {'id': 3,
                 'question': 'How many square centimetres (cm²) are in 1 square metre (m²)?',
                 'options': ['10,000 cm²', '100 cm²', '1,000 cm²', '1,000,000 cm²'],
                 'answer': 0,
                 'hint': '1 m = 100 cm. So 1 m² = 100 cm × 100 cm.',
                 'explanation': '1 m² = 100 cm × 100 cm = 10,000 cm².',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. 1 metre = 100 centimetres.</p>\n'
                                  '    <p>2. 1 m² = 1 m × 1 m = 100 cm × 100 cm.</p>\n'
                                  '    <p>3. 100 × 100 = <strong>10,000 cm²</strong>.</p>\n'
                                  '</div>\n'},
                {'id': 4,
                 'question': 'An L-shaped room is split into two rectangles: Rectangle A (4 m × 3 m) and Rectangle B '
                             '(5 m × 2 m). What is the total floor area?',
                 'options': ['22 m²', '14 m²', '28 m²', '20 m²'],
                 'answer': 0,
                 'hint': 'Area A = 4 × 3 = 12 m². Area B = 5 × 2 = 10 m². Add them together.',
                 'explanation': 'Total Area = Area A + Area B = 12 + 10 = 22 m².',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. Area of Rectangle A = 4 × 3 = 12 m².</p>\n'
                                  '    <p>2. Area of Rectangle B = 5 × 2 = 10 m².</p>\n'
                                  '    <p>3. Total Area = 12 + 10 = <strong>22 m²</strong>.</p>\n'
                                  '</div>\n'},
                {'id': 5,
                 'question': 'A square garden has an area of 64 m². A runner jogs around its boundary 3 times. What '
                             'total distance did the runner travel?',
                 'options': ['96 metres', '32 metres', '192 metres', '64 metres'],
                 'answer': 0,
                 'hint': 'Side = 8 m (since 8 × 8 = 64). Perimeter = 4 × 8 = 32 m. 3 rounds = 3 × 32 m.',
                 'explanation': 'Side = 8 m. One round (perimeter) = 32 m. 3 rounds = 3 × 32 = 96 m.',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. Area = 64 m² ➔ Side = 8 m.</p>\n'
                                  '    <p>2. Perimeter (1 round) = 4 × 8 = 32 m.</p>\n'
                                  '    <p>3. 3 rounds = 3 × 32 = <strong>96 m</strong>.</p>\n'
                                  '</div>\n'},
                {'id': 6,
                 'question': 'In the Perimeter Dice Game, what is the winning objective?',
                 'options': ['To be the first player to build a connected shape with an exact outer perimeter of 24 '
                             'units',
                             'To cover the entire board with the most tiles',
                             'To roll a six on three consecutive turns',
                             'To make the smallest possible perimeter with 50 tiles'],
                 'answer': 0,
                 'hint': 'Recall the game rules from Slide 16.',
                 'explanation': "The winner is the first player whose shape's outer boundary reaches exactly 24 units.",
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. In the Joyful Mathematics Perimeter Building Game:</p>\n'
                                  '    <p>2. Players take turns rolling dice and attaching unit tiles '
                                  'edge-to-edge.</p>\n'
                                  '    <p>3. The goal is to reach an <strong>exact perimeter of 24 '
                                  'units</strong>.</p>\n'
                                  '</div>\n'},
                {'id': 7,
                 'question': 'In the Perimeter Dice Game, why would a player choose to attach tiles in a long straight '
                             'line?',
                 'options': ['Because a linear chain exposes 2 new exterior edges per tile, rapidly increasing '
                             'perimeter',
                             'Because straight lines are not allowed by the opponent',
                             'Because straight lines reduce the perimeter to zero',
                             'Because it rolls higher numbers on the die'],
                 'answer': 0,
                 'hint': 'Adding to the end of a line adds 2 to the outer perimeter.',
                 'explanation': 'Linear chains maximize exposed edges, expanding perimeter by +2 for every tile added.',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. A new tile at the end of a chain covers 1 boundary edge but introduces 3 '
                                  'new ones.</p>\n'
                                  '    <p>2. Net perimeter increase = +3 - 1 = <strong>+2 units</strong> per '
                                  'tile.</p>\n'
                                  '    <p>3. This linear tactic surges the perimeter toward the target 24 '
                                  'rapidly.</p>\n'
                                  '</div>\n'},
                {'id': 8,
                 'question': 'If your current shape in the dice game has a perimeter of 22 units, and you roll a 1, '
                             'where should you place the tile to win the game immediately?',
                 'options': ['At the open end of a straight row (adding +2 to reach exactly 24)',
                             'In an inside corner (adding +0)',
                             'Diagonally at a corner (which is an illegal move)',
                             'On top of an existing tile'],
                 'answer': 0,
                 'hint': 'You need 24 - 22 = +2 units. An end-of-row placement adds +2.',
                 'explanation': 'Placing the tile at the end of a row adds +2, turning 22 into exactly 24 to win!',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. Current perimeter = 22. Target = 24. Needed increase = 24 - 22 = '
                                  '<strong>+2</strong>.</p>\n'
                                  '    <p>2. End-of-row placement gives net change of +2.</p>\n'
                                  '    <p>3. 22 + 2 = 24 ➔ Immediate victory!</p>\n'
                                  '</div>\n'},
                {'id': 9,
                 'question': 'A wire of length 36 cm is bent into a rectangle with breadth 6 cm. What is the length of '
                             'this rectangle?',
                 'options': ['12 cm', '24 cm', '18 cm', '30 cm'],
                 'answer': 0,
                 'hint': 'Perimeter = 36 cm. So L + B = 36 ÷ 2 = 18 cm. Length = 18 - 6.',
                 'explanation': 'L + B = 36 ÷ 2 = 18 cm. Length = 18 - 6 = 12 cm.',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. Wire length = Perimeter = 36 cm.</p>\n'
                                  '    <p>2. L + B = 36 ÷ 2 = 18 cm.</p>\n'
                                  '    <p>3. Given Breadth B = 6 cm ➔ Length = 18 - 6 = <strong>12 cm</strong>.</p>\n'
                                  '</div>\n'},
                {'id': 10,
                 'question': 'A square photo with side 10 cm is pasted in the center of a rectangular cardboard sheet '
                             '16 cm by 12 cm. What area of the cardboard sheet remains uncovered?',
                 'options': ['92 cm²', '192 cm²', '100 cm²', '52 cm²'],
                 'answer': 0,
                 'hint': 'Cardboard Area = 16 × 12 = 192 cm². Photo Area = 10 × 10 = 100 cm². Uncovered = 192 - 100.',
                 'explanation': 'Uncovered Area = Total Area - Photo Area = 192 - 100 = 92 cm².',
                 'solution_html': '\n'
                                  "<div class='space-y-2 text-sm'>\n"
                                  "    <div class='font-bold text-cyan-400'>Step-by-Step Solution:</div>\n"
                                  '    <p>1. Cardboard Area = 16 cm × 12 cm = 192 cm².</p>\n'
                                  '    <p>2. Square Photo Area = 10 cm × 10 cm = 100 cm².</p>\n'
                                  '    <p>3. Uncovered Area = 192 - 100 = <strong>92 cm²</strong>.</p>\n'
                                  '</div>\n'}]}]
