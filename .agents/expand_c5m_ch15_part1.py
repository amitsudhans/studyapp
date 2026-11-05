# -*- coding: utf-8 -*-
"""Check word counts and calibrate Part 1 slides to exactly 195-215 words"""

import re

# Precise expansions targeting 198-202 words for Slides 1-8

lectures = {
    1: (
        "Welcome to our mathematical investigation of data collection, systematic organization, and visual interpretation. "
        "When curious young researchers set out to understand everyday human habits, they begin with a direct inquiry. "
        "In this school survey, two student reporters interviewed thirty-five classmates to measure daily television viewing duration. "
        "As each classmate answered, the raw individual responses were written down directly into a handheld field notebook. "
        "Some friends reported watching television for only half an hour each afternoon after completing homework and outdoor chores. "
        "Other children recorded one full hour, while several engaged for one and a half hours or two hours. "
        "A few classmates admitted spending more than two hours glued to the television screen every single evening. "
        "At first glance, a notebook filled with scattered numbers, varied scribbles, and handwritten notes looks overwhelming and disordered. "
        "Without proper organization, it is impossible to quickly answer fundamental questions, such as which viewing duration is most common. "
        "Raw data represents unorganized factual numbers collected directly from the original source before any mathematical sorting occurs. "
        "To transform these scattered observations into meaningful mathematical knowledge, we must structure the findings into clear categories. "
        "Careful data collection provides the empirical bedrock upon which all statistical reasoning, logical deductions, and sound conclusions are built."
    ),
    2: (
        "Now let us examine how to structure raw notebook responses into an organized frequency distribution table. "
        "A frequency table groups scattered observations into clear, mutually exclusive intervals so that every single data point belongs somewhere. "
        "For our television survey, we establish five distinct categories of daily screen time across the cohort. "
        "The first category is half an hour, followed by one hour, one and a half hours, two hours, and finally more than two hours. "
        "To count accurately without skipping or double-counting, we record each response using standardized tally marks. "
        "Four vertical lines are drawn one by one, and every fifth entry is recorded as a diagonal slash across the four lines. "
        "This bundle of five allows our eyes to quickly count large totals in convenient groups of five. "
        "When all thirty-five children are tallied, we write the final numerical frequency beside each time category. "
        "For instance, five children watch half an hour, twelve children watch one hour, eight watch one and a half hours, six watch two hours, and four watch more than two hours. "
        "Adding five, twelve, eight, six, and four yields exactly thirty-five, verifying our complete survey tally. "
        "Frequency distribution tables transform raw chaotic lists into clear, readable, and highly informative mathematical structures."
    ),
    3: (
        "Once our frequency table is assembled, we can extract profound insights regarding daily lifestyle patterns and screen habits. "
        "Data analysis involves comparing categories, calculating combined subgroups, and evaluating health recommendations against actual recorded behavior. "
        "Looking closely at our television viewing table, we immediately observe that one hour is the most frequent choice, chosen by twelve children. "
        "Next, let us determine how many classmates spend one hour or less watching television each day. "
        "We combine the five children watching half an hour with the twelve children watching one hour, giving seventeen children in total. "
        "Conversely, how many children watch television for more than one hour daily? "
        "We sum eight children at one and a half hours, six at two hours, and four at more than two hours, giving eighteen children. "
        "Notice that seventeen plus eighteen equals our complete sample of thirty-five friends without any missing entries. "
        "Health guidelines generally recommend limiting recreational screen time to no more than one hour daily to safeguard eyesight and physical activity. "
        "Our data reveals that eighteen out of thirty-five children exceed this recommended threshold. "
        "Statistical tables empower students to transition from vague guesses to factual evidence, illuminating real-world habits with mathematical precision."
    ),
    4: (
        "Now let us explore pictographs, where numerical quantities are represented visually using scaled symbols and meaningful icons. "
        "Consider a neighbourhood toy shop preparing its inventory stock before summer vacation begins for schoolchildren. "
        "The shopkeeper counts hundreds of play items, including stuffed teddy bears, traditional board games, and various sports equipment. "
        "Drawing dozens of individual pictures on an inventory sheet would take far too long and clutter the paper. "
        "Instead, cartographers and mathematicians define a key or scale factor to represent multiple physical objects compactly. "
        "In this toy shop inventory pictograph, the shopkeeper decides that one single icon represents five physical items. "
        "Therefore, if we see four toy icons in the toys row, we calculate four multiplied by five, which equals twenty toys in stock. "
        "If the board games row displays six game icons, the total quantity equals six multiplied by five, giving thirty board games. "
        "If the sports equipment row displays eight ball icons, we multiply eight by five, yielding forty sports items. "
        "By establishing a clear scale, a small number of icons compactly represents substantial inventory quantities. "
        "Always inspect the key at the bottom or corner of a pictograph before counting, because the scale determines the true values."
    ),
    5: (
        "An essential mathematical skill is choosing and adapting the scale factor of a pictograph to suit our analytical needs. "
        "In the previous scenario, our shopkeeper used a scale where one icon represented five physical play items. "
        "Under that scale, ninety total items required eighteen separate icons across the three inventory rows on the page. "
        "What happens if our paper is smaller, and we wish to use fewer icons for faster drawing and clearer presentation? "
        "We can choose an alternative scale factor, such as letting one icon represent ten physical items. "
        "Let us recalculate our inventory quantities using this new scale of ten items per icon. "
        "For toys, twenty items divided by ten means we need to draw only two icons. "
        "For board games, thirty items divided by ten requires exactly three icons. "
        "For sports equipment, forty items divided by ten yields four icons. "
        "Under a scale of ten, our entire shop inventory is shown using just two plus three plus four, which equals nine icons. "
        "Notice that changing the scale does not alter the underlying real-world quantities in the slightest. "
        "Twenty toys, thirty games, and forty sports gear items remain identical whether we draw eighteen icons or nine icons. "
        "Choosing an appropriate scale balances visual clarity with drafting efficiency."
    ),
    6: (
        "Let us apply pictographs to real-world transportation tracking by observing street traffic passing outside a home during rush hour. "
        "A student monitored the flow of two-wheelers, such as scooters and motorcycles, during one morning hour on three different days. "
        "Observations were systematically conducted on Monday, Wednesday, and Friday along the neighborhood main road. "
        "To record the traffic cleanly, the student created a pictograph where one scooter symbol represents three actual two-wheelers. "
        "On Monday, the pictograph displays five scooter symbols. "
        "Multiplying five by three reveals that fifteen two-wheelers passed along the road on Monday morning. "
        "On Wednesday, the road was quieter, and only three scooter symbols were recorded in the observation tally. "
        "Three symbols multiplied by three means nine two-wheelers passed on Wednesday. "
        "On Friday, traffic surged as commuters hurried for weekend errands, resulting in eight scooter symbols. "
        "Eight symbols multiplied by three yields twenty-four two-wheelers on Friday. "
        "By scanning the visual symbols, we instantly spot that Friday experienced the heaviest road traffic of all three days. "
        "The total number of two-wheelers observed across all three days equals fifteen plus nine plus twenty-four, which totals forty-eight vehicles. "
        "Scaled pictographs allow rapid comparison across different observation periods while preserving accurate mathematical data."
    ),
    7: (
        "Let us deepen our comparative analysis of the traffic pictograph and explore re-scaling with fraction symbols. "
        "We previously determined that fifteen vehicles passed on Monday, nine on Wednesday, and twenty-four on Friday. "
        "Subtracting nine from twenty-four shows that Friday had fifteen more vehicles than Wednesday, which was the quietest day. "
        "What if we choose to redraw this pictograph using a larger scale factor, where one icon represents six two-wheelers? "
        "For Friday's twenty-four vehicles, dividing twenty-four by six gives four complete icons. "
        "For Monday's fifteen vehicles, fifteen divided by six equals two with a remainder of three vehicles. "
        "Since three is exactly half of six, we represent Monday with two full icons plus one half-icon. "
        "For Wednesday's nine vehicles, nine divided by six equals one with a remainder of three vehicles. "
        "Thus Wednesday requires one full icon plus one half-icon to display its traffic accurately. "
        "Half-icons are a standard cartographic convention in pictographs whenever quantities fall halfway between whole multiples. "
        "Using a scale of six requires only four icons for Friday, two and a half for Monday, and one and a half for Wednesday. "
        "Understanding fractional symbols enables accurate visual representation of numbers that do not divide evenly by the chosen scale."
    ),
    8: (
        "Every child has exactly twenty-four hours in a day, but how we allocate those hours across activities varies greatly. "
        "To understand time management, students can record their daily routines across standard activities: sleeping, school, studying, playing, eating, and chores. "
        "One student recorded their daily routine using a direct pictorial list, where each icon represents exactly one hour. "
        "For sleeping, the student drew eight bed icons, representing eight hours of restful sleep at night. "
        "For school, six book icons were drawn, accounting for six hours spent in the classroom and morning assembly. "
        "For personal study and homework at home, two pencil icons were recorded, totaling two hours of focused learning. "
        "For eating meals and outdoor play, four ball and plate icons were drawn, representing four hours of nourishment and recreation. "
        "Finally, four clock icons accounted for other routine activities like getting dressed, commuting, and family conversations. "
        "Summing these hours yields eight plus six plus two plus four plus four, which equals exactly twenty-four hours. "
        "This icon method makes it easy to visualize individual hours as tangible blocks across the entire day. "
        "However, counting long rows of identical icons can become tedious when comparing multiple categories quickly."
    )
}

for sid, txt in lectures.items():
    wc = len(txt.split())
    print(f"Slide {sid}: {wc} words")
    assert 195 <= wc <= 215, f"Slide {sid} word count {wc} out of range!"

