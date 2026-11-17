#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.dirname(__file__))

from make_c9s_ch9_sims_part1 import sims_part1
from make_c9s_ch9_sims_part2 import sims_part2

simulators = {**sims_part1, **sims_part2}
