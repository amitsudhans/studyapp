#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assembler for NCERT Class 9 Maths Chapter 5: I'm Up and Down, and Round and Round
Combines Parts 1, 2, 3 into full 20-slide curriculum dataset.
"""

from generate_c9m_ch5_part1 import slides_part1
from generate_c9m_ch5_part2 import slides_part2
from generate_c9m_ch5_part3 import slides_part3

slides = slides_part1 + slides_part2 + slides_part3
