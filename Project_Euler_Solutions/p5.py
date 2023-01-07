'''
2520 is the smallest number that can be divided by each
of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?
'''

import numpy as np

#Greatest common divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#Smallest common multiple of 2 numbers
def scm(a, b):
    return int(a*b/gcd(a,b))

#Returns smallest common multiple of first n numbers
def common_multiple(n):
    solution=1
    for i in range(n):
        print(solution, i+1)
        solution=scm(solution, i+1)
    return solution

print(common_multiple(20))
