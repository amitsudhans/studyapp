# -*- coding: utf-8 -*-
"""Check word counts and calibrate Part 2 slides to exactly 195-215 words"""

lectures_part2 = {
    9: (
        "To overcome the limitations of counting long rows of identical icons, we transition to vertical bar graphs. "
        "A bar graph represents data using rectangular bars of uniform width where the height of each bar is proportional to the quantity. "
        "Let us examine how a student constructs a vertical bar graph to display the twenty-four hour daily routine. "
        "First, two perpendicular reference lines are drawn: a horizontal base axis and a vertical value axis. "
        "Along the horizontal base axis, we label the distinct activity categories: sleeping, school, study, play and meals, and other routines. "
        "Along the vertical axis, we establish an evenly spaced numerical scale marked in hours from zero up to ten. "
        "Next, rectangular columns of equal width are erected above each category label across the page. "
        "The sleeping bar rises vertically until it aligns with eight on the vertical scale. "
        "The school bar reaches upward to six hours, while the self-study bar reaches two hours. "
        "The play and meals bar and the other routines bar each rise to four hours. "
        "With a single glance, our eyes instantly compare relative durations without counting individual symbols. "
        "Bar graphs provide immediate visual comparison, making relative differences in magnitude evident across categories."
    ),
    10: (
        "Now let us analyze the daily schedule bar graph to evaluate the balance, equity, and healthfulness of a student's daily routine. "
        "Statistical graphs do not merely present numbers; they facilitate critical thinking and informed personal decision-making for young learners. "
        "Looking closely at the heights of the bars, we compare the hours dedicated to restorative sleep against active waking pursuits. "
        "Sleeping occupies eight hours, which represents exactly one-third of the twenty-four hour day. "
        "Medical researchers emphasize that growing children need at least eight to nine hours of sound sleep for healthy brain development and vitality. "
        "Next, consider academic learning, which combines six hours of school instruction with two hours of self-study at home. "
        "This totals eight hours of intellectual engagement, perfectly matching the eight hours allocated to restful sleep. "
        "The remaining eight hours are divided equally between active recreation, nourishment, hygiene, and essential personal care. "
        "This division exhibits a remarkably balanced three-part routine: one-third for sleep, one-third for education, and one-third for recreation and daily living. "
        "Students are encouraged to chart their own personal twenty-four hour day on grid paper. "
        "Plotting personal routines enables young learners to identify imbalances, reduce wasted time, and cultivate healthy lifelong habits."
    ),
    11: (
        "Data does not always arrive in printed survey sheets; frequently, students generate data through direct physical measurement. "
        "Consider a lively classroom inquiry where classmates investigate the question: whose index finger is longest in our group? "
        "To measure finger lengths accurately without rigid plastic rulers slipping, students employ flexible paper strips. "
        "Each child places a thin strip of paper along the inner length of their dominant index finger, starting from the base joint crease to the tip. "
        "The exact endpoint at the tip of the finger is marked cleanly with a sharp pencil. "
        "Using scissors, the student cuts or tears off the extra paper beyond the mark, creating a custom strip equal to their finger length. "
        "Next, each student places their strip against a standardized centimeter scale to record the length in centimeters and millimeters with precision. "
        "One classmate's strip measures four and a half centimeters, another measures five centimeters, while another reaches five point eight centimeters. "
        "Each paper strip is labeled clearly with the corresponding student's identification code for systematic record keeping. "
        "This tactile procedure bridges physical reality with mathematical abstraction. "
        "Collecting accurate measurements through standardized physical tools ensures data integrity before visual graphing begins across the class."
    ),
    12: (
        "Once all student finger strips are trimmed and measured, the class constructs a physical bar graph directly on chart paper. "
        "Instead of drawing ink bars with a pen, the students physically paste their paper strips side by side along a horizontal baseline. "
        "A vertical reference line is marked with centimeter intervals from zero up to seven centimeters. "
        "Each child pastes their labeled strip standing vertically from the baseline, keeping the width and spacing completely uniform. "
        "Suddenly, the physical paper strips themselves become the vertical bars of an authentic, tangible bar graph. "
        "Looking across the chart, the varying heights of the paper strips immediately reveal the comparative distribution. "
        "The tallest strip rises to five point eight centimeters, belonging to the classmate with the longest index finger. "
        "The shortest strip reaches only four point two centimeters, belonging to the classmate with the shortest index finger. "
        "Subtracting four point two from five point eight reveals a spread of one point six centimeters across the measured cohort. "
        "This hands-on creation of a physical bar graph cements the foundational mathematical truth that bar graphs are visual representations of physical quantities. "
        "Physical graphs make abstract coordinate systems tangible and intuitive for every young learner."
    ),
    13: (
        "Data analysis becomes particularly meaningful and impactful when applied to pressing real-world issues, such as environmental sustainability and cafeteria food conservation. "
        "In this school study, kitchen staff monitors daily food waste collected from the student canteen across five consecutive weekdays. "
        "Every single afternoon, the kitchen staff weighs uneaten food scraped from plates and records the total mass in kilograms on a bulletin board. "
        "A vertical bar graph is displayed on the main school notice board to inform all students and teachers about weekly food waste patterns. "
        "The horizontal axis lists the weekdays and corresponding lunch menus: Monday sandwich, Tuesday paratha, Wednesday khichdi, Thursday puri-sabzi, and Friday idli-sambar. "
        "The vertical axis indicates the waste in kilograms, marked clearly from zero up to ten kilograms. "
        "On Monday, sandwich day recorded four kilograms of plate waste. "
        "On Tuesday, paratha day recorded seven kilograms of plate waste. "
        "On Wednesday, khichdi day saw waste decline sharply to three kilograms, the lowest of the entire school week. "
        "On Thursday, puri-sabzi day recorded eight kilograms, reaching the highest waste level of the entire week. "
        "On Friday, idli-sambar day resulted in five kilograms of waste. "
        "Observing these bar heights stimulates thoughtful inquiry into why certain meals result in substantially higher waste across the dining hall."
    ),
    14: (
        "Let us take our canteen food waste analysis further by calculating the cumulative weekly impact and evaluating practical, sustainable solutions. "
        "To understand the total weekly toll, we sum the food waste across all five recorded school weekdays. "
        "Adding four kilograms on Monday, seven on Tuesday, three on Wednesday, eight on Thursday, and five on Friday yields twenty-seven kilograms in total. "
        "Twenty-seven kilograms of wholesome edible food discarded in a single school week represents a significant loss of precious agricultural resources. "
        "To grasp this waste in relatable human terms, we use an established nutritional benchmark: one kilogram of prepared food can feed three hungry children. "
        "Multiplying twenty-seven kilograms by three reveals that eighty-one children could have received a wholesome meal from the food discarded in just one week. "
        "Armed with this striking numerical data, the student council proposed three practical waste reduction strategies for the school. "
        "First, introduce flexible serving sizes, allowing students to request smaller initial portions and return for seconds if still hungry. "
        "Second, conduct student taste surveys to adjust recipes and seasoning for unpopular menu items. "
        "Third, display daily waste totals prominently in the dining hall to foster collective accountability. "
        "Mathematical data turns abstract numbers into compelling ethical catalysts for positive behavioral change."
    ),
    15: (
        "Data analysis also frequently involves verifying claims against detailed visual scenes, combining observational counting with rigorous logical reasoning. "
        "In this activity, students examine a lively illustration depicting a group of twelve school children gathered together in a sunny courtyard. "
        "The children wear various accessories and hold diverse school items: some wear caps, some wear spectacles, some carry backpacks, and some hold books. "
        "Students are presented with several statements to evaluate as True or False based strictly on careful visual counts. "
        "Consider the first statement: exactly five children are wearing caps. "
        "Scanning the illustration carefully, we count one, two, three, four, and five children sporting caps, confirming the statement as True. "
        "Consider a second claim: more children are wearing spectacles than are carrying backpacks. "
        "Counting spectacles reveals four children with glasses, while counting backpacks reveals six children with bags. "
        "Since four is strictly less than six, the claim is proven False. "
        "Consider a third statement: three children are wearing both a cap and spectacles simultaneously. "
        "Inspecting the intersection of features, we find exactly two children possessing both accessories, proving the claim False. "
        "Systematic observation trains young learners to scrutinize visual details methodically and resist hasty, unsubstantiated conclusions."
    ),
    16: (
        "We conclude our textbook journey by examining the supplementary geometric cutout nets that bridge flat two-dimensional data with three-dimensional space. "
        "A geometric net is a two-dimensional flat pattern that can be folded along scored edges to construct a hollow three-dimensional solid polyhedron. "
        "In the textbook appendix, students explore the nets of two remarkable regular polyhedra: the icosahedron and the dodecahedron. "
        "The icosahedron net is composed entirely of twenty congruent equilateral triangles joined along shared edges. "
        "When carefully folded and joined with adhesive tabs, these twenty triangular faces form a symmetrical solid with twelve vertices and thirty edges. "
        "In contrast, the dodecahedron net consists of twelve congruent regular pentagons arranged in two interlocking flower-like clusters. "
        "Folding this net encloses a beautiful spherical solid featuring twelve pentagonal faces, twenty vertices, and thirty straight edges. "
        "These geometric solids exemplify regular polyhedra, where every single face is an identical regular polygon and every vertex joins equal numbers of faces. "
        "From counting daily TV hours to folding twenty-faced polyhedra, mathematics weaves a continuous tapestry connecting numbers, geometric shapes, and the physical world. "
        "Through pictures, tallies, graphs, and spatial nets, we learn to perceive structure, beauty, and truth throughout our universe."
    )
}

if __name__ == '__main__':
    for sid in range(9, 17):
        txt = lectures_part2[sid]
        wc = len(txt.split())
        print(f"Slide {sid}: {wc} words")
        assert 195 <= wc <= 215, f"Slide {sid} word count {wc} out of range 195-215!"
    print("All slides 9-16 calibrated successfully!")
