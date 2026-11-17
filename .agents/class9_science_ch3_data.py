#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Combined 20-Slide Dataset for NCERT Class 9 Science Chapter 3: Tissues in Action
"""

from generate_c9s_ch3_part1 import slides_part1
from generate_c9s_ch3_part2 import slides_part2
from generate_c9s_ch3_part3 import slides_part3

slides = slides_part1 + slides_part2 + slides_part3
