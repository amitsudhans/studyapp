import re

with open('.agents/generate_c5m_ch13_part2.py', 'r') as f:
    text = f.read()

# Slide 9
s9_old = '''        "lecture": (
            "Deep within a dense tropical forest, a young wildlife explorer follows an ancient stepping-stone trail numbered from zero to "
            "fifty-nine to visit various animal habitats. Depending on the size of the steps taken, the explorer lands on distinct subsets "
            "of numbered stones! When taking steady two-step jumps, the explorer touches stones four, twelve, fourteen, and fifty. "
            "Because two divides every single one of these numbers with zero remainder, the number two is a common factor of all four numbers! "
            "Next, when the explorer switches to taking brisk three-step jumps, the path touches stones nine, twenty-one, thirty-nine, and "
            "fifty-seven. Here, three divides each position completely, proving that three is a common factor of this new set of locations! "
            "What happens when the explorer takes five-step jumps? Every stone touched—such as fifteen, twenty-five, thirty-five, and fifty—ends "
            "in either five or zero! And when leaping in ten-step bounds, every single stone ends in zero: ten, twenty, thirty, forty, and fifty. "
            "This lively jungle expedition reveals that stepping intervals correspond directly to division factors. Stepping stones shared "
            "by both two-step and five-step paths—like ten, twenty, thirty, and fifty—demonstrate numbers divisible by both factors simultaneously."
        ),'''

s9_new = '''        "lecture": (
            "Deep within a dense tropical forest, an inquisitive young wildlife explorer follows an ancient stepping-stone trail numbered from "
            "zero to fifty-nine to visit various friendly animal habitats. Depending on the exact size of the steps taken, the explorer lands "
            "on distinct subsets of numbered stones along the lush forest path! When taking steady two-step jumps, the explorer touches "
            "stones four, twelve, fourteen, and fifty. Because two divides every single one of these numbers with zero remainder, the number "
            "two is a true common factor of all four locations! Next, when the explorer switches to taking brisk three-step jumps, the path "
            "touches stones nine, twenty-one, thirty-nine, and fifty-seven. Here, three divides each position completely, proving that three "
            "is a common factor of this new set of locations! What happens when the explorer takes five-step jumps? Every stone touched—such "
            "as fifteen, twenty-five, thirty-five, and fifty—ends in either five or zero! And when leaping in ten-step bounds, every single "
            "stone ends in zero: ten, twenty, thirty, forty, and fifty. This lively jungle expedition reveals that stepping intervals correspond "
            "directly to mathematical division factors. Stepping stones shared by both two-step and five-step paths—like ten, twenty, thirty, "
            "and fifty—demonstrate numbers divisible by both factors simultaneously."
        ),'''

# Slide 11
s11_old = '''        "lecture": (
            "Let us apply our common factor method to larger composite numbers and discover an intriguing mathematical theorem regarding "
            "consecutive numbers! Consider finding all common factors of twenty-four and thirty-six. Let us list all factors of twenty-four: "
            "one, two, three, four, six, eight, twelve, and twenty-four. Now let us list all factors of thirty-six: one, two, three, four, "
            "six, nine, twelve, eighteen, and thirty-six. Comparing both lists, we find an impressive collection of shared divisors: "
            "one, two, three, four, six, and twelve! Both twenty-four and thirty-six share six distinct common factors, with twelve serving "
            "as their highest common factor. Now, let us examine an entirely different pair: twelve and thirteen! Notice that twelve and "
            "thirteen are consecutive numbers—they sit right next to each other on the number line. Factors of twelve are one, two, three, "
            "four, six, and twelve. Factors of thirteen are simply one and thirteen. What is their only common factor? Exactly one! "
            "This illustrates a universal mathematical truth: any two consecutive whole numbers share only one as a common factor. "
            "Because no number greater than one can divide two numbers that differ by only one, consecutive numbers are always co-prime."
        ),'''

s11_new = '''        "lecture": (
            "Let us apply our common factor method to larger composite numbers and discover an intriguing mathematical theorem regarding "
            "consecutive numbers! Consider finding all common factors of twenty-four and thirty-six. Let us list all factors of twenty-four: "
            "one, two, three, four, six, eight, twelve, and twenty-four. Now let us list all factors of thirty-six: one, two, three, four, "
            "six, nine, twelve, eighteen, and thirty-six. Comparing both lists carefully, we find an impressive collection of shared divisors: "
            "one, two, three, four, six, and twelve! Both twenty-four and thirty-six share six distinct common factors, with twelve serving "
            "as their highest common factor. Now, let us examine an entirely different pair: twelve and thirteen! Notice that twelve and "
            "thirteen are consecutive numbers—they sit right next to each other on the continuous number line. Factors of twelve are one, "
            "two, three, four, six, and twelve. Factors of thirteen are simply one and thirteen. What is their only common factor? Exactly "
            "the number one! This illustrates a universal mathematical truth: any two consecutive whole numbers share only one as a common "
            "factor. Because no whole number greater than one can divide two numbers that differ by only one, consecutive numbers are always co-prime."
        ),'''

# Slide 12
s12_old = '''        "lecture": (
            "Let us sharpen our analytical skills by working through a comprehensive common factor practice set covering a variety of pairs! "
            "First, consider twelve and sixteen: factors of twelve are one, two, three, four, six, and twelve. Factors of sixteen are one, "
            "two, four, eight, and sixteen. Their common factors are one, two, and four, with four being their HCF. Next, consider two "
            "and nine: factors of two are one and two; factors of nine are one, three, and nine. What do they share? Only the number one! "
            "Even though nine is composite and two is prime, their only shared divisor is one. Now consider nine and twenty-one: factors "
            "of nine are one, three, and nine; factors of twenty-one are one, three, seven, and twenty-one. Their common factors are one "
            "and three! Notice how systematic listing makes finding common factors completely foolproof. Always start by writing the factors "
            "in ascending order from one up to the number itself. Next, circle the matching entries. By comparing multiple pairs, students "
            "discover that some numbers share several factors, while others share only one, building deep intuition for fractions and number theory."
        ),'''

s12_new = '''        "lecture": (
            "Let us sharpen our analytical skills by working through a comprehensive common factor practice set covering a variety of diverse "
            "number pairs! First, consider twelve and sixteen: factors of twelve are one, two, three, four, six, and twelve. Factors of sixteen "
            "are one, two, four, eight, and sixteen. Their common factors are one, two, and four, with four standing proudly as their highest "
            "common factor. Next, consider the pair two and nine: factors of two are one and two; factors of nine are one, three, and nine. "
            "What do they share in common? Only the number one! Even though nine is a composite square number and two is a prime number, "
            "their only shared divisor is one. Now consider nine and twenty-one: factors of nine are one, three, and nine; factors of "
            "twenty-one are one, three, seven, and twenty-one. Their common factors are one and three, making three their highest common "
            "factor! Notice how systematic listing makes finding common factors completely foolproof. Always start by writing all factors "
            "in ascending order from one up to the number itself. Next, circle the matching entries. By comparing multiple pairs, students "
            "discover that some numbers share several factors, while others share only one, building deep intuition for fractions and number theory."
        ),'''

# Slide 13
s13_old = '''        "lecture": (
            "Mathematics is celebrated for its ironclad logical rules! Let us examine five important statements about numbers and test whether "
            "each statement is true or false using rigorous mathematical reasoning. Statement one: 'Factors of even numbers must always be even.' "
            "Is this true? No, this is completely false! For example, the number ten is even, but its factors include one and five, which are odd! "
            "Statement two: 'Multiples of odd numbers cannot be even.' Is this true? No, this is also false! Three times two equals six, which "
            "is even; multiples of odd numbers alternate between odd and even! Statement three: 'Factors of odd numbers cannot be even.' "
            "Is this true? Yes, this is absolutely true! If an odd number had an even factor, multiplying that even factor by any integer "
            "would produce an even number, which is impossible! Statement four: 'The only common factor of any two consecutive numbers is one.' "
            "Yes, this is true, as consecutive numbers differ by one. Finally, statement five: 'Zero cannot be a factor of any whole number.' "
            "Yes, this is true because division by zero is mathematically undefined. Testing statements with counterexamples builds strong logical reasoning."
        ),'''

s13_new = '''        "lecture": (
            "Mathematics is rightly celebrated for its ironclad logical rules! Let us examine five important statements about numbers and "
            "test whether each statement is true or false using rigorous mathematical reasoning and clear counterexamples. Statement one: "
            "'Factors of even numbers must always be even.' Is this true? No, this is completely false! For example, the number ten is an "
            "even number, but its factors include one and five, which are completely odd! Statement two: 'Multiples of odd numbers cannot "
            "be even.' Is this true? No, this is also false! Three times two equals six, which is even; multiples of odd numbers alternate "
            "regularly between odd and even products! Statement three: 'Factors of odd numbers cannot be even.' Is this true? Yes, this is "
            "absolutely true! If an odd number had an even factor, multiplying that even factor by any integer would produce an even number, "
            "which is mathematically impossible! Statement four: 'The only common factor of any two consecutive numbers is one.' Yes, this "
            "is true, as consecutive numbers differ by only one. Finally, statement five: 'Zero cannot be a factor of any whole number.' "
            "Yes, this is true because division by zero is mathematically undefined. Testing statements with counterexamples builds strong logical reasoning."
        ),'''

# Slide 15
s15_old = '''        "lecture": (
            "To synthesize our understanding of multiples and divisibility, let us examine an elegant classification puzzle using a Venn "
            "diagram with overlapping circles! We have a pool of fifteen numbers to categorize: ninety, twenty-two, thirty-eight, thirty, "
            "seventy-five, forty-five, sixty-six, seventy-eight, sixty-two, forty, eighty-four, fifty-six, twenty-five, ninety-five, and fifty-five. "
            "We sort them based on whether they are divisible by two, by five, or by both two and five! What happens when a number is divisible "
            "by two only? These are even numbers that do not end in zero, such as twenty-two, thirty-eight, sixty-six, seventy-eight, "
            "sixty-two, eighty-four, and fifty-six. What happens when a number is divisible by five only? These are odd numbers that end in "
            "five, such as seventy-five, forty-five, twenty-five, ninety-five, and fifty-five! Now, what belongs in the overlapping center "
            "region where both circles intersect? Numbers that are divisible by both two and five must end in zero! Because two times five "
            "equals ten, any number in this shared region is automatically divisible by ten: ninety, thirty, and forty. A number cannot "
            "be divisible by ten without being divisible by both two and five!"
        ),'''

s15_new = '''        "lecture": (
            "To synthesize our comprehensive understanding of multiples and divisibility, let us examine an elegant classification puzzle "
            "using a Venn diagram with overlapping circles! We have a large pool of fifteen distinct numbers to categorize: ninety, "
            "twenty-two, thirty-eight, thirty, seventy-five, forty-five, sixty-six, seventy-eight, sixty-two, forty, eighty-four, fifty-six, "
            "twenty-five, ninety-five, and fifty-five. We sort them systematically based on whether they are divisible by two, by five, or "
            "by both two and five simultaneously! What happens when a number is divisible by two only? These are even numbers that do not end "
            "in zero, such as twenty-two, thirty-eight, sixty-six, seventy-eight, sixty-two, eighty-four, and fifty-six. What happens when a "
            "number is divisible by five only? These are odd numbers that end in five, such as seventy-five, forty-five, twenty-five, "
            "ninety-five, and fifty-five! Now, what belongs in the overlapping center region where both circles intersect? Numbers that are "
            "divisible by both two and five must end in zero! Because two times five equals ten, any number in this shared region is "
            "automatically divisible by ten: ninety, thirty, and forty. A number cannot be divisible by ten without being divisible by both two and five!"
        ),'''

# Slide 16
s16_old = '''        "lecture": (
            "As we conclude our mathematical expedition through animal jumps, let us reflect upon the unified principles of factors and multiples "
            "that we have mastered! Every whole number can be expressed as a product of factors, geometrically represented by solid rectangular "
            "tile arrays. Numbers that form only a single straight-line rectangle are prime numbers, possessing exactly two factors: one and "
            "the number itself. Numbers that form multiple rectangular configurations are composite numbers, while the number one is uniquely "
            "neither prime nor composite. When animals leap along the number line, their footsteps map out skip-counting sequences of multiples. "
            "Where their footprints coincide, we uncover common multiples. The very first shared stepping stone represents the least common "
            "multiple, synchronizing repeating cycles in time, gears, and planetary orbits. Conversely, when comparing the divisor sets of "
            "multiple numbers, we find common factors, with the largest being the highest common factor. Consecutive whole numbers always "
            "share only one as a common factor, making them fundamentally co-prime. By connecting physical jumps, geometric rectangles, and "
            "divisibility logic, you possess a versatile mathematical toolkit to unlock patterns across arithmetic and advanced problem solving."
        ),'''

s16_new = '''        "lecture": (
            "As we conclude our inspiring mathematical expedition through animal jumps, let us reflect upon the great unified principles "
            "of factors and multiples that we have mastered together! Every whole number can be expressed as a product of factors, geometrically "
            "represented by solid rectangular tile arrays. Numbers that form only a single straight-line rectangle are prime numbers, "
            "possessing exactly two factors: one and the number itself. Numbers that form multiple rectangular configurations are composite "
            "numbers, while the number one is uniquely neither prime nor composite. When animals leap along the continuous number line, "
            "their footsteps map out skip-counting sequences of multiples. Where their footprints coincide, we uncover common multiples! "
            "The very first shared stepping stone represents the least common multiple, synchronizing repeating cycles in sports, clocks, "
            "and nature. Conversely, when comparing the divisor sets of multiple numbers, we find common factors, with the largest being the "
            "highest common factor. Consecutive whole numbers always share only one as a common factor, making them fundamentally co-prime. "
            "By connecting physical jumps, geometric rectangles, and divisibility logic, students possess a versatile mathematical toolkit to unlock patterns everywhere."
        ),'''

for old, new, name in [(s9_old, s9_new, 'S9'), (s11_old, s11_new, 'S11'), (s12_old, s12_new, 'S12'), (s13_old, s13_new, 'S13'), (s15_old, s15_new, 'S15'), (s16_old, s16_new, 'S16')]:
    assert old in text, f'{name} not found'
    text = text.replace(old, new)

with open('.agents/generate_c5m_ch13_part2.py', 'w') as f:
    f.write(text)

print('Updated generate_c5m_ch13_part2.py successfully!')
