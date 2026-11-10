# -*- coding: utf-8 -*-
"""
Assemble Simulators for Class 3 Mathematics Chapter 2: Toy Joy
Combines simulators_part1 and simulators_part2 into class3_maths_ch2_sims.py.
"""

import os
import sys

sys.path.append(os.path.dirname(__file__))

from make_c3m_ch2_sims_part1 import simulators_part1
from make_c3m_ch2_sims_part2 import simulators_part2

all_sims = {}
all_sims.update(simulators_part1)
all_sims.update(simulators_part2)

print(f"Total simulators assembled: {len(all_sims)}")
assert len(all_sims) == 16, f"Expected 16 simulators, got {len(all_sims)}"

expected_sim_ids = [
    "sim_box_bottle_craft",
    "sim_cube_anatomy",
    "sim_rocket_assembly",
    "sim_toy_engine",
    "sim_cube_is_cuboid",
    "sim_flat_curved_surfaces",
    "sim_mystery_shape_describer",
    "sim_classroom_shape_hunt",
    "sim_shape_property_sorter",
    "sim_clay_stick_builder",
    "sim_toy_joy_board_game",
    "sim_dice_opposite_faces",
    "sim_two_cubes_join",
    "sim_three_cube_variations",
    "sim_cube_block_counter",
    "sim_master_geometry_table"
]

for sid in expected_sim_ids:
    assert sid in all_sims, f"Missing simulator: {sid}"

out_file = os.path.join(os.path.dirname(__file__), "class3_maths_ch2_sims.py")
with open(out_file, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Assembled Simulators for Class 3 Mathematics Chapter 2: Toy Joy"""\n\n')
    f.write("simulators = {\n")
    for k, v in all_sims.items():
        f.write(f"    {repr(k)}: {repr(v)},\n")
    f.write("}\n")

print(f"Simulators written to {out_file} ({os.path.getsize(out_file)} bytes)")

