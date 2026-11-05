with open('.agents/generate_c5m_ch13_part2.py', 'r') as f:
    text = f.read()

s15_old = '''        "lecture": (
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

s15_new = '''        "lecture": (
            "To synthesize our comprehensive understanding of multiples and divisibility, let us examine an elegant classification puzzle "
            "using a Venn diagram with overlapping circular regions! We have a large pool of fifteen distinct numbers to categorize: ninety, "
            "twenty-two, thirty-eight, thirty, seventy-five, forty-five, sixty-six, seventy-eight, sixty-two, forty, eighty-four, fifty-six, "
            "twenty-five, ninety-five, and fifty-five. We sort them systematically based on whether they are divisible by two, by five, or "
            "by both two and five simultaneously! What happens when a number is divisible by two only? These are even numbers that do not end "
            "in zero, such as twenty-two, thirty-eight, sixty-six, seventy-eight, sixty-two, eighty-four, and fifty-six. What happens when a "
            "number is divisible by five only? These are odd numbers that end in five, such as seventy-five, forty-five, twenty-five, "
            "ninety-five, and fifty-five! Now, what belongs in the overlapping center region where both circles intersect? Numbers that are "
            "divisible by both two and five must end in zero! Because two times five equals ten, any number in this shared region is "
            "automatically divisible by ten as well: ninety, thirty, and forty. A number cannot be divisible by ten without being divisible "
            "by both two and five! Visual sorting diagrams provide instant clarity for recognizing multiple factor rules at a single glance."
        ),'''

s16_old = '''        "lecture": (
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
            "By connecting physical animal jumps, geometric rectangle arrays, and divisibility logic, students possess an exceptionally versatile "
            "mathematical toolkit to uncover numerical harmony and solve complex arithmetic problems with speed and confidence."
        ),'''

assert s15_old in text
assert s16_old in text
text = text.replace(s15_old, s15_new)
text = text.replace(s16_old, s16_new)

with open('.agents/generate_c5m_ch13_part2.py', 'w') as f:
    f.write(text)

