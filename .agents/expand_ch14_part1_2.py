with open('.agents/generate_c5m_ch14_part1.py', 'r') as f:
    text = f.read()

# Slide 2: add ~10 words
s2_old = 'establish exact directional orientation anywhere with certainty.'
s2_new = 'establish exact directional orientation anywhere on our beautiful planet with joy, confidence, and mathematical certainty.'
assert s2_old in text
text = text.replace(s2_old, s2_new)

# Slide 6: add ~10 words
s6_old = 'so that everyone can navigate accurately.'
s6_new = 'so that travelers, cartographers, and students can interpret spatial layouts and navigate complex territories with absolute accuracy.'
assert s6_old in text
text = text.replace(s6_old, s6_new)

# Slide 7: add ~8 words
s7_old = 'mathematical precision and peace of mind.'
s7_new = 'flawless mathematical precision, fuel efficiency, and complete peace of mind.'
assert s7_old in text
text = text.replace(s7_old, s7_new)

# Slide 8: add ~10 words
s8_old = 'wasting valuable travel time.'
s8_new = 'wasting valuable travel time and burning unnecessary energy along the way.'
assert s8_old in text
text = text.replace(s8_old, s8_new)

with open('.agents/generate_c5m_ch14_part1.py', 'w') as f:
    f.write(text)

