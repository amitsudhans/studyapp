#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 9: Some Applications of Trigonometry
Data Generator - Part 2 (Slides 9 to 16)
Strict constraints:
- Titles: Strictly 1 to 3 words each
- Speech: Strictly 195 to 215 words each (spoken-friendly plain math phrasing)
- Checkpoints: Exactly 2 per slide with 4 options each
- Zero fictional human character names, zero lecturer personas
"""

slides_part2 = [
    {
        "id": 9,
        "title": "Pedestal And Statue",
        "subtitle": "Solving Unknown Bottom Segment h = 0.8(√3 + 1) When Only Top Statue Height 1.6 m Is Given (Ex 9.1 Q8)",
        "speech": (
            "Now invert Example Four into Exercise Nine Point One Questions Seven and Eight! In Question Seven, a transmission tower stands on a known twenty meter building with roof angles forty five and sixty degrees, giving tower height twenty times (root three minus one) meters! "
            "Wait—what happens in Question Eight when the BOTTOM height is UNKNOWN while ONLY the TOP statue height one point six meters is given? Look closely! "
            "A statue one point six meters tall stands upright atop a pedestal! From a ground point, elevation to the statue's TOP is sixty degrees, and to the pedestal's TOP is forty five degrees! Find pedestal height h! "
            "Let shared horizontal ground base equal x meters! Step One (Bottom Triangle, forty five degrees): tangent forty five equals h over x -> ONE equals h over x -> x equals h! "
            "Step Two (Full Tall Triangle, sixty degrees): tangent sixty equals full combined height (h plus one point six) divided by base x! Substitute x equals h cleanly: root three equals (h plus one point six) divided by h, giving h times (root three minus one) equals 1.6, rationalizing smoothly to pedestal height zero point eight times (root three plus one) meters!"
        ),
        "checkpoints": [
            {
                "question": "A 1.6 m tall statue stands on top of a pedestal. Ground elevations to top of statue and top of pedestal are 60° and 45° (Ex 9.1 Q8). Find pedestal height:",
                "options": [
                    "0.8(√3 + 1) m",
                    "1.6(√3 − 1) m",
                    "0.8(√3 − 1) m",
                    "1.6√3 m"
                ],
                "answer": 0,
                "hint": "45° makes base x = h; then (h + 1.6)/h = √3 ⟹ h(√3 − 1) = 1.6 ⟹ multiply by (√3 + 1)/(√3 + 1)!",
                "explanation": "h = 1.6 / (√3 − 1) = [1.6(√3 + 1)] / (3 − 1) = 0.8(√3 + 1) m."
            },
            {
                "question": "From a ground point, angles of elevation to bottom and top of a transmission tower fixed on a 20 m building are 45° and 60° (Ex 9.1 Q7). Tower height is:",
                "options": [
                    "20(√3 − 1) m",
                    "20(√3 + 1) m",
                    "20√3 m",
                    "10(√3 − 1) m"
                ],
                "answer": 0,
                "hint": "45° gives base = 20 m; 60° gives full height = 20√3 m ⟹ subtract 20 m!",
                "explanation": "Tower height = 20√3 − 20 = 20(√3 − 1) m."
            }
        ]
    },
    {
        "id": 10,
        "title": "Sun Shadow Shift",
        "subtitle": "Eliminating Unknown Inner Shadow x When Sun Altitude Changes 60° → 30° (Example 5: 40 m Longer)",
        "speech": (
            "Now rotate your right triangles horizontally so TWO ground stations sit in line behind each other, sharing ONE vertical height! Meet Textbook Example Five, the classic Sun Altitude Shadow Shift problem! "
            "Read carefully: The shadow of a vertical tower standing on level ground is found to be FORTY METERS LONGER when the Sun's altitude drops to thirty degrees than when it was sixty degrees! Find the height h of the tower! "
            "First clarify: what does Sun's altitude mean? It simply equals the ground angle of elevation to the Sun! Higher sixty degree Sun casts a shorter shadow x! Lower thirty degree Sun stretches the total shadow forty meters longer, making full base (x plus forty) meters! "
            "Write TWO clean equations sharing height h! First triangle (sixty degrees): tangent sixty equals h over x, giving x equals h divided by root three! Second triangle (thirty degrees): tangent thirty equals h over (x plus forty), giving x plus forty equals h root three! "
            "Substitute x cleanly into Equation Two: (h divided by root three) plus forty equals h root three! Solving two h equals forty root three yields exact vertical tower height twenty root three meters cleanly!"
        ),
        "checkpoints": [
            {
                "question": "A tower's ground shadow lengthens by 40 m when the Sun's altitude drops from 60° to 30° (Example 5). Find tower height h:",
                "options": [
                    "20√3 m",
                    "40√3 m",
                    "20 m",
                    "40 / √3 m"
                ],
                "answer": 0,
                "hint": "Set x = h/√3 and x + 40 = h√3 ⟹ h(√3 − 1/√3) = 40 ⟹ 2h/√3 = 40!",
                "explanation": "h√3 − h/√3 = 40 ⟹ (3h − h)/√3 = 40 ⟹ 2h = 40√3 ⟹ h = 20√3 m."
            },
            {
                "question": "Why does a tower's shadow grow LONGER when the Sun's altitude angle decreases from 60° down to 30°?",
                "options": [
                    "Because horizontal shadow x = h / tan θ increases whenever θ decreases (tan 30° < tan 60°)",
                    "Because tower height shrinks at afternoon",
                    "Because tan 30° is larger than tan 60°",
                    "Because 30° + 60° = 90° always doubles x"
                ],
                "answer": 0,
                "hint": "Notice h stays constant while denominator tan θ gets smaller!",
                "explanation": "Smaller Sun altitude produces a flatter ray and smaller tan θ, stretching ground shadow x = h cot θ farther."
            }
        ]
    },
    {
        "id": 11,
        "title": "Equal Poles Road",
        "subtitle": "Two Equal-Height Opposite Poles Along an 80 m Road Meeting at 60° & 30° (Ex 9.1 Q10)",
        "speech": (
            "Now face two separate vertical towers across a road—Exercise Nine Point One Question Ten! Read cleanly: Two poles of EQUAL heights stand strictly opposite each other on either side of an eighty meter wide road! "
            "From a point sitting on the road directly BETWEEN both poles, the angles of elevation to the tops of the poles measure sixty degrees and thirty degrees respectively! Find the equal height of both poles AND the distances of the observation point from each pole! "
            "Watch how smoothly splitting the eighty meter road solves BOTH unknowns! Let the point sit x meters from the sixty degree pole; then it automatically sits (80 minus x) meters away from the thirty degree pole! "
            "Notice BOTH poles share EQUAL vertical height h! Triangle One (sixty degrees): h equals x times tangent sixty equals x root three! Triangle Two (thirty degrees): h equals (80 minus x) times tangent thirty equals (80 minus x) divided by root three! "
            "Equate BOTH formulas for h immediately: x root three equals (80 minus x) over root three -> 3x equals 80 minus x -> 4x equals 80 -> x equals 20 m, other side 60 m, and pole height 20 root three meters!"
        ),
        "checkpoints": [
            {
                "question": "Two poles of equal height stand opposite across an 80 m road. Elevations from a road point between them are 60° and 30° (Ex 9.1 Q10). Find pole height and distances:",
                "options": [
                    "Height = 20√3 m;  Distances = 20 m and 60 m",
                    "Height = 40√3 m;  Distances = 40 m and 40 m",
                    "Height = 20 m;  Distances = 30 m and 50 m",
                    "Height = 80/√3 m;  Distances = 20 m and 60 m"
                ],
                "answer": 0,
                "hint": "Equate h = x√3 and h = (80 − x)/√3 ⟹ 3x = 80 − x ⟹ 4x = 80!",
                "explanation": "4x = 80 gives x = 20 m (from 60° pole) and 80−20 = 60 m (from 30° pole); height h = 20√3 m."
            },
            {
                "question": "Without even finishing the algebra, which pole MUST the observation point be closer to in the 80 m road puzzle?",
                "options": [
                    "The 60° pole (because steeper elevation angle means shorter horizontal distance x = h / tan θ)",
                    "The 30° pole",
                    "Exactly at the 40 m midpoint",
                    "Cannot be determined beforehand"
                ],
                "answer": 0,
                "hint": "Looking straight up steeper at 60° happens closer to the pole base!",
                "explanation": "Higher elevation angle 60° corresponds to shorter distance (20 m) vs flatter 30° (60 m)."
            }
        ]
    },
    {
        "id": 12,
        "title": "Multi Storeyed Building",
        "subtitle": "Looking Down From Roof at Top & Bottom of an 8 m Building (Example 6: 30° & 45° Depressions)",
        "speech": (
            "Now climb up onto the roof of a tall multi storeyed building in Textbook Example Six to conquer DOUBLE ANGLES OF DEPRESSION! "
            "Read carefully: From the top of a multi storeyed building, the angles of depression of the top AND bottom of an EIGHT METER TALL building are thirty degrees and forty five degrees respectively! Find the height of the multi storeyed building AND the horizontal distance between the two buildings! "
            "Step One: Draw horizontal sky line PQ at the tall roof top, then transfer BOTH depression angles via alternate interior angles straight into your two horizontal triangle legs: thirty degrees sits at the top roof of the shorter eight meter building, while forty five degrees sits cleanly at ground level! "
            "Step Two: Let the shorter upper difference height above eight meters equal h, and horizontal spacing equal x! From the large forty five degree ground triangle, tangent forty five equals ONE, forcing total height (h plus 8) equal to x! "
            "From the small thirty degree upper triangle, x equals h root three! Equating gives h + 8 equals h√3 -> rationalizing yields h equals 4(√3 + 1), so total height AND gap equal 4(3 + √3) meters!"
        ),
        "checkpoints": [
            {
                "question": "From top of a multi-storeyed building, depressions to top & bottom of an 8 m building are 30° and 45° (Example 6). Find tall building height and building distance:",
                "options": [
                    "4(3 + √3) m   for BOTH height and distance",
                    "8(√3 + 1) m",
                    "4(√3 + 1) m",
                    "8(3 − √3) m"
                ],
                "answer": 0,
                "hint": "Upper diff h satisfies h + 8 = h√3 ⟹ h = 8/(√3−1) = 4(√3 + 1), so full height = 8 + 4(√3 + 1) = 12 + 4√3 = 4(3 + √3)!",
                "explanation": "Both total height and horizontal gap equal x = h + 8 = 8 + 4(√3 + 1) = 4(3 + √3) m."
            },
            {
                "question": "Which building is taller in Textbook Example 6, and how do we know immediately?",
                "options": [
                    "The multi-storeyed observation building—because BOTH top and bottom of the 8 m building require angles of DEPRESSION (looking down)",
                    "The 8 m building is taller",
                    "Both have identical 8 m height",
                    "Cannot tell without side lengths"
                ],
                "answer": 0,
                "hint": "Looking DOWN with an angle of depression to the TOP of the 8 m building means your roof sits higher!",
                "explanation": "A downward angle of depression to the other roof confirms the observer stands strictly above 8 m."
            }
        ]
    },
    {
        "id": 13,
        "title": "River Bridge Width",
        "subtitle": "Measuring River Width From a 3 m Bridge (Example 7: 30° & 45°) & Canal TV Tower (Ex 9.1 Q11)",
        "speech": (
            "Put angles of depression straight onto water in Textbook Example Seven AND Exercise Nine Point One Question Eleven! "
            "First check Example Seven, the River Bridge! From a point P on a bridge straight across a river, angles of depression of the banks on OPPOSITE sides of the river are thirty degrees and forty five degrees respectively! If the bridge sits at a vertical height of three meters above the banks, find the total width of the river! "
            "Notice both banks lie on OPPOSITE sides of the bridge drop point D! By alternate interior angles, left triangle PDA holds thirty degrees and right triangle PDB holds forty five degrees, sharing vertical bridge height PD equals three meters! "
            "Left bank width AD equals three divided by tangent thirty equals three root three meters! Right bank width BD equals three divided by tangent forty five equals three meters! Adding both opposite segments cleanly gives total river width AB equals three times (root three plus one) meters! "
            "Compare against Question Eleven's canal TV tower: stepping back twenty meters along the same bank converts 60 degrees down to 30 degrees, yielding canal width ten meters and tower height ten root three meters!"
        ),
        "checkpoints": [
            {
                "question": "From a bridge 3 m above a river, depressions to opposite banks are 30° and 45° (Example 7). What is total river width?",
                "options": [
                    "3(√3 + 1) m",
                    "3(√3 − 1) m",
                    "3√3 m",
                    "6 m"
                ],
                "answer": 0,
                "hint": "Opposite banks ADD together: AD = 3 / tan 30° = 3√3 and DB = 3 / tan 45° = 3!",
                "explanation": "Width = AD + DB = 3√3 + 3 = 3(√3 + 1) m."
            },
            {
                "question": "A TV tower on a canal bank has 60° elevation from the opposite bank and 30° from 20 m further back (Ex 9.1 Q11). Find canal width and tower height:",
                "options": [
                    "Canal width = 10 m,  Tower height = 10√3 m",
                    "Canal width = 20 m,  Tower height = 20√3 m",
                    "Canal width = 10√3 m,  Tower height = 10 m",
                    "Canal width = 40 m,  Tower height = 20√3 m"
                ],
                "answer": 0,
                "hint": "Set h = x√3 and h = (x + 20)/√3 ⟹ 3x = x + 20 ⟹ 2x = 20!",
                "explanation": "Solving 3x = x + 20 gives canal width x = 10 m and tower height h = 10√3 m."
            }
        ]
    },
    {
        "id": 14,
        "title": "Lighthouse Two Ships",
        "subtitle": "75 m Lighthouse Tracking Two Aligned Ships (Ex 9.1 Q13) & Building-Tower Elevation/Depression (Q12)",
        "speech": (
            "Now master TWO signature Exercise Nine Point One puzzles combining opposing and aligned sightlines: Questions Twelve and Thirteen! "
            "Check Question Twelve first: Standing on top of a seven meter high building, the angle of ELEVATION of the top of a taller cable tower is sixty degrees, AND the angle of DEPRESSION of its bottom foot is forty five degrees! "
            "Spot that clean forty five degree right triangle at the bottom immediately: horizontal distance across to the cable tower equals building height seven meters! Then upper tower rise above seven meters equals seven times tangent sixty equals seven root three meters! Adding bottom seven meters gives full tower height seven times (root three plus 1) meters! "
            "Now sail out to Question Thirteen's seventy five meter sea lighthouse! Looking down from the top, TWO ships sit lined directly one behind the other on the SAME side of the lighthouse with angles of depression thirty degrees and forty five degrees! "
            "Closer sea ship sits horizontally at seventy five meters (45°); farther sea ship sits out at seventy five root three meters (30°)! Subtract both horizontal positions cleanly to get the exact gap between both ships: seventy five times (root three minus one) meters!"
        ),
        "checkpoints": [
            {
                "question": "As observed from top of a 75 m lighthouse, depressions of two ships one behind the other on the SAME side are 30° and 45° (Ex 9.1 Q13). Distance between the two ships:",
                "options": [
                    "75(√3 − 1) m",
                    "75(√3 + 1) m",
                    "75√3 m",
                    "150 m"
                ],
                "answer": 0,
                "hint": "Closer ship (45°) distance = 75 m; farther ship (30°) distance = 75√3 m; ships are on the SAME side ⟹ SUBTRACT!",
                "explanation": "Gap = 75√3 − 75 = 75(√3 − 1) m."
            },
            {
                "question": "From top of a 7 m high building, elevation of a cable tower top is 60° and depression of its foot is 45° (Ex 9.1 Q12). Find full tower height:",
                "options": [
                    "7(√3 + 1) m",
                    "7(√3 − 1) m",
                    "7√3 m",
                    "14 m"
                ],
                "answer": 0,
                "hint": "Bottom 45° gives gap x = 7 m; top 60° adds 7√3 m above 7 m!",
                "explanation": "Total height = 7 + 7√3 = 7(√3 + 1) m."
            }
        ]
    },
    {
        "id": 15,
        "title": "Balloon Horizontal Drift",
        "subtitle": "Tracking a Floating Balloon at 88.2 m Altitude as Elevation Drops 60° → 30° (Ex 9.1 Q14)",
        "speech": (
            "Inspect one of Chapter Nine's most celebrated real-world physics questions—Exercise Nine Point One Question Fourteen, tracking a horizontal wind-blown hot-air balloon cleanly without fictional names! "
            "Read every detail carefully: An observer measuring one point two meters tall spots a balloon floating horizontally with the wind at a fixed vertical height of eighty eight point two meters ABOVE THE GROUND! At that first instant, the angle of elevation from the observer's eyes equals sixty degrees! "
            "After some time passes, as the balloon glides strictly horizontally away at the same altitude, its angle of elevation drops smoothly down to thirty degrees! Find the total horizontal distance travelled by the balloon during that interval! "
            "Step One, Eye Level Adjustment! Never plug 88.2 meters directly into tangent! Subtract observer eye height one point two meters cleanly from eighty eight point two meters, giving crisp net vertical height equal to EIGHTY SEVEN meters! "
            "Step Two: Initial position at sixty degrees sits at horizontal distance 87 over root three, rationalizing cleanly to 29 root three meters! Final position at thirty degrees sits at 87 root three meters! Subtracting both positions gives exact drift: 87√3 minus 29√3 equals 58 root three meters!"
        ),
        "checkpoints": [
            {
                "question": "A 1.2 m observer watches a balloon drifting horizontally at height 88.2 m above ground as elevation drops from 60° to 30° (Ex 9.1 Q14). Distance travelled by balloon:",
                "options": [
                    "58√3 m",
                    "87√3 m",
                    "29√3 m",
                    "58.8√3 m"
                ],
                "answer": 0,
                "hint": "Net height above eye level = 88.2 − 1.2 = 87 m! Subtract 87/√3 (= 29√3) from 87√3!",
                "explanation": "87√3 − 87/√3 = 87√3 − 29√3 = 58√3 m."
            },
            {
                "question": "Before applying tan 60° and tan 30° in the balloon problem, what happens to the altitude number 88.2 m?",
                "options": [
                    "Subtract 1.2 m observer height immediately to get 87 m net vertical height above eye level",
                    "Add 1.2 m to get 89.4 m",
                    "Divide 88.2 m by 2",
                    "Keep 88.2 m unchanged inside both triangles"
                ],
                "answer": 0,
                "hint": "Elevation angles 60° and 30° are measured from the observer's EYES (1.2 m high), not ground feet!",
                "explanation": "Because line of sight begins at 1.2 m eye level, vertical triangle opposite leg is 88.2 − 1.2 = 87 m."
            }
        ]
    },
    {
        "id": 16,
        "title": "Car Motion Summary",
        "subtitle": "Uniform Speed Car Approaching Highway Tower (Ex 9.1 Q15: 3 s) + Section 9.2 Chapter Summary",
        "speech": (
            "Finish strong with Exercise Nine Point One Question Fifteen—linking Trigonometry straight into Uniform Speed Motion—followed by our complete Section Nine Point Two Chapter Summary! "
            "Look at Question Fifteen: A straight highway leads directly to the foot of a tower! Standing atop the tower, an observer spots an approaching car at an angle of depression of thirty degrees, cruising toward the tower foot at uniform constant speed! "
            "Six seconds later, the car's angle of depression deepens to sixty degrees! How much MORE time will the car take to reach the tower foot from that second point? "
            "Call tower height h! At thirty degrees, car distance from foot equals h root three! At sixty degrees, car distance shrinks to h divided by root three! "
            "Distance driven in six seconds equals (h root three minus h over root three) equals TWO TIMES (h over root three), precisely DOUBLE the remaining road gap! At constant uniform speed, covering HALF the remaining road distance takes HALF of six seconds, which equals just THREE SECONDS! "
            "Section Nine Point Two Summary: Always sketch flat horizontal eye lines first, transfer depression angles safely via alternate interior angles, adjust for observer eye height, and pick tangent, sine, or cosine cleanly!"
        ),
        "checkpoints": [
            {
                "question": "A car moves at uniform speed toward a tower as depression deepens from 30° to 60° in 6 seconds (Ex 9.1 Q15). Time needed to reach the foot from the 60° position:",
                "options": [
                    "3 seconds",
                    "6 seconds",
                    "4 seconds",
                    "2 seconds"
                ],
                "answer": 0,
                "hint": "Gap covered in 6 s = h√3 − h/√3 = 2(h/√3), which is DOUBLE the remaining distance h/√3!",
                "explanation": "Since remaining distance (h/√3) is half the distance covered in 6 seconds, uniform speed requires 6 / 2 = 3 seconds."
            },
            {
                "question": "Which summary rule guarantees accuracy across ALL NCERT Chapter 9 Heights & Distances problems?",
                "options": [
                    "Always trace horizontal eye level first, transfer depression angles via alternate interior angles, and adjust for non-zero observer height",
                    "Measure depression against vertical walls",
                    "Always add two opposite-side ships by subtracting",
                    "Always ignore observer eye height"
                ],
                "answer": 0,
                "hint": "Recall our three core geometry rules from Sections 9.1 and 9.2!",
                "explanation": "Horizontal reference, alternate interior angles for depression, and eye-height offset prevent all classic mistakes."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Generated {len(slides_part2)} slides for Ch9 Class 10 Maths Part 2.")
    for s in slides_part2:
        twc = len(s["title"].split())
        swc = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({twc} words) | Speech: {swc} words | Checkpoints: {len(s['checkpoints'])}")
        assert 1 <= twc <= 3, f"Title '{s['title']}' word count {twc} not 1-3"
        assert 195 <= swc <= 215, f"Slide {s['id']} speech word count {swc} not 195-215"
        assert len(s["checkpoints"]) == 2
    print("All Part 2 assertions passed cleanly!")
