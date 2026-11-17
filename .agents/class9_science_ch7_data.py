#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.dirname(__file__))

from generate_c9s_ch7_part1 import slides_part1
from generate_c9s_ch7_part2 import slides_part2
from generate_c9s_ch7_part3 import slides_part3

slides = slides_part1 + slides_part2 + slides_part3
