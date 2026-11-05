with open('.agents/generate_c5m_ch14_part2.py', 'r') as f:
    text = f.read()

# Slide 11: add ~12 words
s11_old = 'effortless clarity, consistency, and spatial accuracy.'
s11_new = 'effortless clarity, remarkable consistency, complete peace of mind, and absolute spatial accuracy on every field journey.'
assert s11_old in text
text = text.replace(s11_old, s11_new)

# Slide 13: add ~8 words
s13_old = 'reliable navigational tracks.'
s13_new = 'reliable, highly predictable navigational tracks across the entire landscape.'
assert s13_old in text
text = text.replace(s13_old, s13_new)

with open('.agents/generate_c5m_ch14_part2.py', 'w') as f:
    f.write(text)

