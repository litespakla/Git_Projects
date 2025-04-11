'''
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the
digits 1, 2, 3 and 4. If all of the permutations are
listed numerically or alphabetically, we call it lexicographic
order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

import itertools

#Gets the nth permutation of listed permutations of digits
def lexicographic(digits, permutation):
    perms=list(itertools.permutations(digits))
    ans=''
    for i in sorted(perms, key=lambda x: x[0])[permutation-1]:
        ans+=str(i)
    return ans

#Parameters
d=[0, 1, 2, 3, 4, 5, 6, 7 ,8 ,9]
pos=1000000

print(lexicographic(d, pos))
