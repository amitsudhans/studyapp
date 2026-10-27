with open('.agents/build_class8_math_squares_cubes_lab.py', 'r') as f:
    code = f.read()

# Replace ${u} with ${{u}}, ${sqU} with ${{sqU}}, and {0, 1, 4...}
old_sub = '(${u} \u00d7 ${u} = ${u*u} ends in ${sqU})'
new_sub = '(${{u}} \u00d7 ${{u}} = ${{u*u}} ends in ${{sqU}})'
code = code.replace(old_sub, new_sub)

old_set = 'Digits: {0, 1, 4, 5, 6, 9} | Forbidden: {2, 3, 7, 8}'
new_set = 'Digits: {{0, 1, 4, 5, 6, 9}} | Forbidden: {{2, 3, 7, 8}}'
code = code.replace(old_set, new_set)

with open('.agents/build_class8_math_squares_cubes_lab.py', 'w') as f:
    f.write(code)
print('Done!')
