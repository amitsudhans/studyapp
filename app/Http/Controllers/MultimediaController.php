<?php

namespace App\Http\Controllers;

use App\Models\Standard;
use Illuminate\Http\Request;
use Illuminate\View\View;

class MultimediaController extends Controller
{
    /**
     * Display the textbook curriculum multimedia tree.
     */
    public function index(Request $request): View
    {
        $selectedSyllabus = strtolower($request->query('syllabus', 'cbse'));
        $selectedSubject = strtolower($request->query('subject', 'mathematics'));
        $selectedClass = strtolower($request->query('class', 'class10'));
        $searchQuery = trim($request->query('q', ''));
        $filterMode = $request->query('filter', 'all'); // 'all', 'multimedia', 'empty'

        // Define the standard textbook curriculum tree
        $syllabuses = [
            'cbse' => [
                'id' => 'cbse',
                'name' => 'CBSE (NCERT)',
                'badge' => 'Central Board of Secondary Education',
                'description' => 'National Curriculum Framework & NCERT Textbook Reprints',
            ],
            'scert' => [
                'id' => 'scert',
                'name' => 'SCERT',
                'badge' => 'State Council of Educational Research',
                'description' => 'State Curriculum Textbook Framework',
            ],
        ];

        $subjects = [
            'mathematics' => [
                'id' => 'mathematics',
                'name' => 'Mathematics',
                'icon' => '📐',
                'color' => 'emerald',
            ],
            'science' => [
                'id' => 'science',
                'name' => 'Science',
                'icon' => '🔬',
                'color' => 'cyan',
            ],
            'english' => [
                'id' => 'english',
                'name' => 'English',
                'icon' => '📖',
                'color' => 'indigo',
            ],
        ];

        $classes = [
            'class1' => ['id' => 'class1', 'name' => 'Class 1', 'level' => 'Primary'],
            'class2' => ['id' => 'class2', 'name' => 'Class 2', 'level' => 'Primary'],
            'class3' => ['id' => 'class3', 'name' => 'Class 3', 'level' => 'Primary'],
            'class4' => ['id' => 'class4', 'name' => 'Class 4', 'level' => 'Primary'],
            'class5' => ['id' => 'class5', 'name' => 'Class 5', 'level' => 'Primary'],
            'class6' => ['id' => 'class6', 'name' => 'Class 6', 'level' => 'Middle'],
            'class7' => ['id' => 'class7', 'name' => 'Class 7', 'level' => 'Middle'],
            'class8' => ['id' => 'class8', 'name' => 'Class 8', 'level' => 'Middle'],
            'class9' => ['id' => 'class9', 'name' => 'Class 9', 'level' => 'Secondary'],
            'class10' => ['id' => 'class10', 'name' => 'Class 10', 'level' => 'Secondary'],
        ];

        // Specific curriculum chapters definition
        $curriculumChapters = [
            // CBSE Mathematics Class 10
            'cbse-mathematics-class10' => [
                [
                    'chapter_num' => 1,
                    'name' => 'Real Numbers',
                    'has_multimedia' => true,
                    'media_key' => 'real-numbers',
                    'media_title' => 'NCERT Chapter 1 • Real Numbers Lab',
                    'media_url' => asset('animations/real-numbers.html'),
                    'description' => 'Interactive Factor Tree Generator (32760), HCF & LCM identity verification, why 4ⁿ/6ⁿ cannot end with 0, and visual contradiction proof of √2 & √3 with sports track simulation.',
                    'topics' => ['Fundamental Theorem of Arithmetic', 'Factor Trees', 'HCF × LCM = a × b', 'Proof of Irrationality (√2, √3)', 'Circular Track Simulation (LCM)'],
                ],
                [
                    'chapter_num' => 2,
                    'name' => 'Polynomials',
                    'has_multimedia' => true,
                    'media_key' => 'polynomials',
                    'media_title' => 'NCERT Chapter 2 • Polynomials Lab',
                    'media_url' => asset('animations/polynomials.html'),
                    'description' => 'Interactive 10-slide multimedia lab covering degrees, zeroes definition, parabola geometry, the 3 cases of quadratic graphs, Exercise 2.1 graph trainer, zeroes-coefficients relationships (α+β=-b/a, αβ=c/a), middle-term splitting, and cubic relations.',
                    'topics' => ['Degrees & Types (Linear, Quadratic, Cubic)', 'Value & Zeroes of p(x)', 'Parabolas & 3 Geometric Cases', 'Exercise 2.1 Graph Lab', 'Sum & Product of Zeroes (α+β, αβ)', 'Cubic Relations (α+β+γ, αβγ)'],
                ],
                [
                    'chapter_num' => 3,
                    'name' => 'Pair of Linear Equations in Two Variables',
                    'has_multimedia' => true,
                    'media_key' => 'linear-equations',
                    'media_title' => 'NCERT Chapter 3 • Pair of Linear Equations Lab',
                    'media_url' => asset('animations/linear-equations.html'),
                    'description' => 'Interactive 10-slide multimedia lab covering real-life modeling (Akhila at fair), graphical method, the 3 geometric cases & ratio tests (a1/a2, b1/b2, c1/c2), Table 3.1, substitution method, elimination method, and two-digit number problem.',
                    'topics' => ['Real-Life Modeling & Standard Form', '3 Geometric Cases (Intersect, Coincide, Parallel)', 'Ratio Comparison Tests (Table 3.1)', 'Graphical Solution (x+3y=6, 2x-3y=12)', 'Substitution Method (Ex 4, 5, 6)', 'Elimination Method (Incomes & Two-digit 42/24)'],
                ],
                [
                    'chapter_num' => 4,
                    'name' => 'Quadratic Equations',
                    'has_multimedia' => true,
                    'media_key' => 'quadratic-equations',
                    'media_title' => 'NCERT Chapter 4 • Quadratic Equations Lab',
                    'media_url' => asset('animations/quadratic-equations.html'),
                    'description' => 'Interactive 10-slide multimedia lab covering the prayer hall derivation, standard form ax²+bx+c=0, disguised equations checker, factorisation by splitting the middle term, Sridharacharya quadratic formula, discriminant (D=b²-4ac) & nature of roots, circular park pole problem, and finding k for equal roots.',
                    'topics' => ['Prayer Hall Derivation & Standard Form', 'Disguised Equation Detector (Trap Cases)', 'Factorisation (Splitting Middle Term)', 'Sridharacharya Quadratic Formula', 'Discriminant & 3 Root Cases (D>0, D=0, D<0)', 'Circular Boundary Pole Problem & Finding k'],
                ],
                [
                    'chapter_num' => 5,
                    'name' => 'Arithmetic Progressions',
                    'has_multimedia' => true,
                    'media_key' => 'arithmetic-progressions',
                    'media_title' => 'NCERT Chapter 5 • Arithmetic Progressions Lab',
                    'media_url' => asset('animations/arithmetic-progressions.html'),
                    'description' => 'Interactive 10-slide multimedia lab covering patterns in nature & real life, common difference d (positive, negative, zero & radicals), nth term an=a+(n-1)d, nth term from the end (reverse AP), Gauss trick for sum of terms, Sn=(n/2)[2a+(n-1)d] and Sn=(n/2)(a+l), double solution paradox (canceling terms), spiral semicircles & log stacking, and arithmetic mean.',
                    'topics' => ['Patterns & AP Definition (General Form)', 'Common Difference d (Positive, Negative, Zero)', 'nth Term Formula & Term from the End', 'Gauss Trick & Sum of n Terms (Sn)', 'Double Solution Paradox (Canceling Terms)', 'Real-Life Geometric Modeling & Arithmetic Mean'],
                ],
                [
                    'chapter_num' => 6,
                    'name' => 'Triangles',
                    'has_multimedia' => true,
                    'media_key' => 'triangles',
                    'media_title' => 'NCERT Chapter 6 • Triangles Lab',
                    'media_url' => asset('animations/triangles.html'),
                    'description' => 'Interactive 10-slide multimedia lab covering congruence vs similarity, Thales Basic Proportionality Theorem (BPT Theorem 6.1) with step-by-step area proof, converse of BPT (Theorem 6.2), AAA/AA, SSS, SAS, and RHS similarity criteria, and indirect measurement shadow modeling (girl walking away from lamp-post and tower heights).',
                    'topics' => ['Congruence vs Similarity (Circles, Squares)', 'Basic Proportionality Theorem (BPT / Thales)', 'Complete Proof of Theorem 6.1 (Area Ratios)', 'Converse of BPT & Trapezium Applications', 'AAA, AA, SSS & SAS Similarity Criteria', 'Real-World Shadow Modeling (Lamp-Post & Tower)'],
                ],
                [
                    'chapter_num' => 7,
                    'name' => 'Coordinate Geometry',
                    'has_multimedia' => true,
                    'media_key' => 'coordinate-geometry',
                    'media_title' => 'NCERT Chapter 7 • Coordinate Geometry Lab',
                    'media_url' => asset('animations/coordinate-geometry.html'),
                    'description' => 'Interactive 10-slide multimedia lab covering Cartesian plane (abscissa, ordinate, quadrants), distance on axes & town A-B problem, distance formula derivation via Pythagoras, shape verification (triangles, squares, collinearity, perpendicular bisector), section formula derivation via AA similarity, mid-point formula, trisection points, finding ratios (k:1), axis intersections, parallelogram diagonal bisector property, and Sports Day flag posting.',
                    'topics' => ['Cartesian Plane, Abscissa & Ordinate', 'Distance Formula Derivation & Origin Distance', 'Triangle & Square Proofs via Distance', 'Collinearity Test & Perpendicular Bisector', 'Section Formula Derivation via AA Similarity', 'Mid-Point Formula & Points of Trisection', 'Finding Division Ratios (k : 1) & Axis Cuts', 'Parallelogram Diagonals & Sports Day Flag Problem'],
                ],
                [
                    'chapter_num' => 8,
                    'name' => 'Introduction to Trigonometry',
                    'has_multimedia' => true,
                    'media_key' => 'trigonometry',
                    'media_title' => 'NCERT Chapter 8 • Introduction to Trigonometry Lab',
                    'media_url' => asset('animations/trigonometry.html'),
                    'description' => 'Interactive 10-slide multimedia lab covering real-world right triangles (Qutub Minar, river width, balloon altitude), Aryabhata history, the 6 trigonometric ratios (sin, cos, tan, cosec, sec, cot) & angle perspective switch (A vs C), invariance by AA similarity, geometric derivations of 45°, 30°, 60° and boundary limits (0°, 90°), Table 8.1 values, and proof derivations of the 3 fundamental identities (cos²A+sin²A=1, 1+tan²A=sec²A, 1+cot²A=cosec²A).',
                    'topics' => ['Real-World Modeling & Aryabhata History', 'The 6 Trigonometric Ratios (Perspective Shift)', 'Invariance by AA Similarity (Scale Independence)', 'Derivation of 45°, 30°, 60° & Boundary Limits (0°, 90°)', 'Master Values Table 8.1 & Finger Rule', 'The 3 Pythagorean Identities & Proof Playbook'],
                ],
                [
                    'chapter_num' => 9,
                    'name' => 'Some Applications of Trigonometry',
                    'has_multimedia' => true,
                    'media_key' => 'applications-of-trigonometry',
                    'media_title' => 'NCERT Chapter 9 • Applications of Trigonometry Lab',
                    'media_url' => asset('animations/applications-of-trigonometry.html'),
                    'description' => 'Interactive 10-slide multimedia lab covering heights and distances fundamentals (line of sight, angle of elevation, angle of depression, alternate interior angles), observer height offset rule, single right triangles (tower, ladder on 5m pole, chimney), the broken tree storm problem (standing opposite + bent hypotenuse), two-angle setups (building with flagstaff, pedestal and statue), Sun\'s altitude shadow lengthening (40m shift), multi-storeyed building depression, river width from bridge, and motion modeling (88.2m balloon horizontal drift and car approaching tower at uniform speed).',
                    'topics' => ['Line of Sight, Elevation & Depression', 'Observer Height (AE) Offset Rule', 'Direct Heights (Tower, Ladder, Chimney)', 'The Broken Tree Storm Problem (Hypotenuse)', 'Building with Flagstaff & Shared Base (AP)', 'Sun Altitude Shadow Shift (40m Lengthening)', 'Multi-Storeyed Double Depression Angles', 'River Width from Bridge & Motion Problems (Balloon, Car)'],
                ],
                [
                    'chapter_num' => 10,
                    'name' => 'Circles',
                    'has_multimedia' => true,
                    'media_key' => 'circles',
                    'media_title' => 'NCERT Chapter 10 • Circles Lab',
                    'media_url' => asset('animations/circles.html'),
                    'description' => 'Interactive 10-slide multimedia lab covering circle-line relationships (non-intersecting, secant, tangent), tangent as a limiting case of secant with coincident chord endpoints, Theorem 10.1 (radius perpendicular to tangent via shortest distance proof), number of tangents from points (inside=0, on=1, outside=2), Theorem 10.2 (equality of tangent lengths from external point via RHS congruence), concentric circles chord bisection, angle theorem ∠PTQ = 2∠OPQ, tangent length calculation (chord 8cm, radius 5cm), circumscribed quadrilateral theorem (AB + CD = AD + BC) & rhombus proof, and triangle circumscribing circle (r = 4 cm) area decomposition.',
                    'topics' => ['Non-Intersecting, Secant & Tangent', 'Tangent as Limiting Secant Case', 'Theorem 10.1: Radius ⊥ Tangent Proof', 'Tangents from Points (Inside, On, Outside)', 'Theorem 10.2: Tangent Lengths Equal (RHS Proof)', 'Concentric Circles & Chord Bisection', 'Angle Doubling Theorem (∠PTQ = 2∠OPQ)', 'Circumscribed Quadrilateral (AB+CD=AD+BC) & Rhombus', 'Triangle Circumscribing Circle (r=4cm)'],
                ],
                [
                    'chapter_num' => 11,
                    'name' => 'Areas Related to Circles',
                    'has_multimedia' => true,
                    'media_key' => 'areas-related-to-circles',
                    'media_title' => 'NCERT Chapter 11 • Areas Related to Circles Lab',
                    'media_url' => asset('animations/areas-related-to-circles.html'),
                    'description' => 'Interactive 10-slide multimedia lab covering minor & major sectors, minor & major segments, unitary method derivations for sector area (θ/360 × πr²) and arc length (θ/360 × 2πr), interactive dynamic circle slice calculator, the 120° obtuse angle segment derivation with trigonometry (altitude splitting), clock minute hand 5-minute sweep, horse grazing in a square field with rope extension, silver brooch with 10 sectors, round table cover 6-segment hexagonal cost calculation, and everyday models (umbrella ribs, wipers, lighthouse beacon).',
                    'topics' => ['Sectors vs Segments (Minor & Major)', 'Unitary Method Derivations (Area & Arc Length)', 'Interactive Dynamic Sector/Segment Lab', '120° Segment Trigonometric Altitude Splitting', 'Clock Minute Hand 5-Minute Sweep', 'Horse Grazing in Square Field (Quadrant)', 'Silver Brooch 10-Sector Symmetry', 'Round Table Cover 6-Design Hexagonal Cost', 'Everyday Circular Models (Umbrella, Wipers, Beacon)'],
                ],
                [
                    'chapter_num' => 12,
                    'name' => 'Surface Areas and Volumes',
                    'has_multimedia' => true,
                    'media_key' => 'surface-areas-and-volumes',
                    'media_title' => 'NCERT Chapter 12 • Surface Areas and Volumes Lab',
                    'media_url' => asset('animations/surface-areas-and-volumes.html'),
                    'description' => 'Interactive 10-slide multimedia lab covering combinations of solids, surface area rules (hidden faces disappear) vs volume rules (strictly additive), playing top (lattu), decorative block (6a²+πr²), wooden rocket with annular base, bird-bath cylinder, industrial shed cuboid with half cylinder, juice glass with raised bottom, circumscribed cylinder, 45 gulab jamuns sugar syrup, pen stand with 4 conical depressions, and lead shots water displacement.',
                    'topics' => ['Combining Solids in Real Life', 'Surface Area Rule (Disappearing Faces)', 'Volume Additive Principle', 'Playing Top (Cone on Hemisphere)', 'Decorative Cube Block (6a²+πr²)', 'Industrial Shed (Cuboid + Half Cylinder)', 'Juice Glass Raised Bottom', 'Gulab Jamuns Sugar Syrup (30%)', 'Lead Shots Water Displacement'],
                ],
                [
                    'chapter_num' => 13,
                    'name' => 'Statistics',
                    'has_multimedia' => true,
                    'media_key' => 'statistics',
                    'media_title' => 'NCERT Chapter 13 • Statistics Lab',
                    'media_url' => asset('animations/statistics.html'),
                    'description' => 'Interactive 10-slide multimedia lab covering the three measures of central tendency (Mean, Median, Mode), the Direct Method, Assumed Mean Method (deviations d=x-a), Step-Deviation Method (u=(x-a)/h), unequal class sizes (cricket wickets), missing frequencies (pocket money f=20, dual unknowns x=9, y=15), grouped mode formula (modal class peak), cumulative frequency ("less than" & "more than" ogives), grouped median formula, and Karl Pearson empirical relation (3 Median = Mode + 2 Mean).',
                    'topics' => ['The 3 Measures of Central Tendency', 'Direct Method & Midpoint Assumption', 'Assumed Mean Method (d=x-a)', 'Step-Deviation Method (u=(x-a)/h)', 'Unequal Class Sizes (Bowlers Wickets)', 'Grouped Mode Formula & Modal Class', 'Cumulative Frequency Distributions (Less & More Than)', 'Grouped Median Formula & Median Class', 'Dual Unknowns (x and y) Reverse Deduction', 'Empirical Formula (3 Median = Mode + 2 Mean)'],
                ],
                [
                    'chapter_num' => 14,
                    'name' => 'Probability',
                    'has_multimedia' => true,
                    'media_key' => 'probability',
                    'media_title' => 'NCERT Chapter 14 • Probability Lab',
                    'media_url' => asset('animations/probability.html'),
                    'description' => 'Interactive 10-slide multimedia lab covering classical (theoretical) probability (Laplace 1795), equally likely outcomes, axioms (0 ≤ P(E) ≤ 1, sure=1, impossible=0), elementary and complementary events (P(E)+P(not E)=1), two and three coin hierarchies (debunking 1/3 fallacy, Hanif game), single die prime number trap, two dice 6x6 grid (sum 2 to 12 pyramid with peak at 7), 52-card deck visualizer (12 face cards, 4 suits), sampling without replacement (queens put aside, defective bulbs), and continuous geometric probability (musical chairs, helicopter lake crash, circular die target).',
                    'topics' => ['Theoretical Probability (Laplace 1795)', 'Equally Likely Outcomes & Axioms', 'Complementary Events (P(E) + P(not E) = 1)', 'Coins Hierarchy (2 & 3 Coins, Hanif Game)', 'Single Die Prime Number Trap {2,3,5}', 'Two Dice 6x6 Grid & Sum 7 Pyramid', '52-Card Deck Breakdown (Suits & Face Cards)', 'Sampling Without Replacement (Cards & Bulbs)', 'Geometric Probability (Continuous Length & Area)'],
                ],
            ],

            // CBSE Mathematics Class 9
            'cbse-mathematics-class9' => [
                [
                    'chapter_num' => 1,
                    'name' => 'Number System',
                    'has_multimedia' => true,
                    'media_key' => 'number-system',
                    'media_title' => 'Class 9 • Number System Lab',
                    'media_url' => asset('animations/number-system.html'),
                    'description' => 'Interactive compass arc construction of √2 and √5 on the number line, nested Number Universe (ℕ ⊂ 𝕎 ⊂ ℤ ⊂ ℚ ⊂ ℝ), recurring decimals to p/q, and challenge quiz with voiceover.',
                    'topics' => ['Number Line Representation', 'Square Root Spiral (Compass)', 'Number Universe', 'Decimal Expansions (p/q)'],
                ],
                [
                    'chapter_num' => 2,
                    'name' => 'Polynomials',
                    'has_multimedia' => false,
                    'description' => 'Polynomials in one variable, zeroes of a polynomial, and remainder theorem.',
                    'topics' => ['Monomials, Binomials, Trinomials', 'Factor Theorem', 'Algebraic Identities'],
                ],
                [
                    'chapter_num' => 3,
                    'name' => 'Coordinate Geometry',
                    'has_multimedia' => false,
                    'description' => 'Cartesian plane, coordinates of a point, and plotting points on the coordinate axes.',
                    'topics' => ['Cartesian Plane', 'Abscissa and Ordinate', 'Quadrant Mapping'],
                ],
                [
                    'chapter_num' => 4,
                    'name' => 'Linear Equations in Two Variables',
                    'has_multimedia' => false,
                    'description' => 'Introduction to equations of the type ax + by + c = 0 and graphing lines.',
                    'topics' => ['Solution of Linear Equations', 'Graph of Linear Equations'],
                ],
            ],

            // CBSE Mathematics Class 6 (User's specific example!)
            'cbse-mathematics-class6' => [
                [
                    'chapter_num' => 1,
                    'name' => 'Knowing Our Numbers',
                    'has_multimedia' => false,
                    'description' => 'Comparing numbers, large numbers in practice, estimation, and use of brackets.',
                    'topics' => ['Place Value Chart', 'Indian & International System', 'Roman Numerals'],
                ],
                [
                    'chapter_num' => 2,
                    'name' => 'Whole Numbers',
                    'has_multimedia' => false,
                    'description' => 'Natural numbers vs whole numbers, number line operations, and properties of whole numbers.',
                    'topics' => ['Predecessor & Successor', 'Closure Property', 'Commutativity'],
                ],
                [
                    'chapter_num' => 3,
                    'name' => 'Playing with Numbers',
                    'has_multimedia' => false,
                    'description' => 'Factors and multiples, prime and composite numbers, divisibility tests, and HCF/LCM.',
                    'topics' => ['Divisibility Rules', 'Prime Factorisation', 'HCF and LCM'],
                ],
            ],

            // CBSE Science Class 10
            'cbse-science-class10' => [
                [
                    'chapter_num' => 1,
                    'name' => 'Chemical Reactions and Equations',
                    'has_multimedia' => false,
                    'description' => 'Chemical equation balancing, types of chemical reactions, corrosion, and rancidity.',
                    'topics' => ['Combination & Decomposition', 'Displacement Reactions', 'Oxidation & Reduction'],
                ],
                [
                    'chapter_num' => 2,
                    'name' => 'Acids, Bases and Salts',
                    'has_multimedia' => false,
                    'description' => 'Understanding chemical properties of acids and bases, pH scale, and common salts.',
                    'topics' => ['Indicators', 'pH Scale Importance', 'Bleaching Powder & Plaster of Paris'],
                ],
                [
                    'chapter_num' => 3,
                    'name' => 'Light - Reflection and Refraction',
                    'has_multimedia' => false,
                    'description' => 'Spherical mirrors, ray diagrams, mirror formula, refraction through lenses, and lens power.',
                    'topics' => ['Reflection by Concave/Convex Mirrors', 'Snell\'s Law', 'Lens Formula & Magnification'],
                ],
            ],

            // CBSE English Class 10
            'cbse-english-class10' => [
                [
                    'chapter_num' => 1,
                    'name' => 'A Letter to God',
                    'has_multimedia' => false,
                    'description' => 'Story of Lencho, a farmer whose crops were destroyed by hailstorm, and his unwavering faith.',
                    'topics' => ['Reading Comprehension', 'Character Analysis', 'Vocabulary & Themes'],
                ],
                [
                    'chapter_num' => 2,
                    'name' => 'Nelson Mandela: Long Walk to Freedom',
                    'has_multimedia' => false,
                    'description' => 'Extract from Nelson Mandela\'s autobiography recounting the historic inauguration.',
                    'topics' => ['Historical Context', 'Apartheid & Freedom', 'Speech Analysis'],
                ],
            ],

            // SCERT Mathematics Class 9
            'scert-mathematics-class9' => [
                [
                    'chapter_num' => 1,
                    'name' => 'Area',
                    'has_multimedia' => false,
                    'description' => 'Area of triangles and parallelograms on the same base and between the same parallels.',
                    'topics' => ['Triangle Area Theorems', 'Polygon Decompositions'],
                ],
                [
                    'chapter_num' => 2,
                    'name' => 'Decimal Forms',
                    'has_multimedia' => false,
                    'description' => 'Fractions to decimals, terminating and non-terminating recurring decimals.',
                    'topics' => ['Decimal Division', 'Recurring Patterns'],
                ],
            ],
        ];

        // Active key
        $activeKey = "{$selectedSyllabus}-{$selectedSubject}-{$selectedClass}";
        $activeChapters = $curriculumChapters[$activeKey] ?? [];

        // Check if active set has any multimedia
        $hasAnyMultimedia = collect($activeChapters)->contains('has_multimedia', true);

        // Calculate global statistics across curriculum
        $totalChaptersCount = 0;
        $totalMediaCount = 0;
        foreach ($curriculumChapters as $k => $chList) {
            foreach ($chList as $ch) {
                $totalChaptersCount++;
                if (! empty($ch['has_multimedia'])) {
                    $totalMediaCount++;
                }
            }
        }

        return view('multimedia.index', [
            'syllabuses' => $syllabuses,
            'subjects' => $subjects,
            'classes' => $classes,
            'curriculumChapters' => $curriculumChapters,
            'selectedSyllabus' => $selectedSyllabus,
            'selectedSubject' => $selectedSubject,
            'selectedClass' => $selectedClass,
            'activeKey' => $activeKey,
            'activeChapters' => $activeChapters,
            'hasAnyMultimedia' => $hasAnyMultimedia,
            'totalChaptersCount' => $totalChaptersCount,
            'totalMediaCount' => $totalMediaCount,
            'searchQuery' => $searchQuery,
            'filterMode' => $filterMode,
        ]);
    }
}
