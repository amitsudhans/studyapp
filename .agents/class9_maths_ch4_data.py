#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assembler for NCERT Class 9 Maths Chapter 4: Exploring Algebraic Identities
Combines Parts 1, 2, 3 into full 20-slide curriculum dataset.
"""

from generate_c9m_ch4_part1 import slides_part1
from generate_c9m_ch4_part2 import slides_part2
from generate_c9m_ch4_part3 import slides_part3

slides = slides_part1 + slides_part2 + slides_part3
