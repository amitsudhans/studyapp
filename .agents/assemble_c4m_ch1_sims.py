# -*- coding: utf-8 -*-
import sys
sys.path.append('.agents')

from make_c4m_ch1_sims_part1 import simulators_part1
from make_c4m_ch1_sims_part2 import simulators_part2

all_sims = {}
all_sims.update(simulators_part1)
all_sims.update(simulators_part2)

with open('.agents/class4_maths_ch1_sims.py', 'w', encoding='utf-8') as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 4 Mathematics Chapter 1: Shapes Around Us Simulators Markup"""\n\n')
    f.write("simulators = " + repr(all_sims) + "\n")

print(f"Successfully assembled {len(all_sims)} simulators into .agents/class4_maths_ch1_sims.py")
