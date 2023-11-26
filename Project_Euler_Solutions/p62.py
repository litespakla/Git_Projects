'''
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest 
cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''

import itertools

permutations=5

num=1
cubes = {}

while True:
    x=num**3

    # Sort the digits to create a key (this groups all permutations)
    key = ''.join(sorted(str(x)))

    # If the key is not in the dictionary, add it with a count of 1
    if key not in cubes:
        cubes[key] = {'count': 1, 'smallest_cube': x, 'n':num}
    else:

        # If the key exists, increment the count
        cubes[key]['count'] += 1

        # If the count reaches number, return the smallest cube for this key
        if cubes[key]['count'] == permutations:
            print(cubes[key]['smallest_cube'], cubes[key]['n'])
            break
    num += 1
