'''
It is well known that if the square root of a natural number is not an integer, 
then it is irrational. The decimal expansion of such square roots is infinite 
without any repeating pattern at all.

The square root of two is 1.41421356237..., and the digital sum of the first 
one hundred decimal digits is 475..

For the first one hundred natural numbers, find the total of the digital sums 
of the first one hundred decimal digits for all the irrational square roots.
'''

import math
from decimal import *

decimals=100
getcontext().prec = decimals+2

n=Decimal(100)
squares=[i**2 for i in range(int(n.sqrt())+1)]

count=0
for i in range(int(n)+1):
    if i not in squares:
        j=Decimal(i)
        digits=math.trunc((j.sqrt())*10**decimals)
        print(i, str(digits)[:100])
        for s in str(digits)[:100]:
            count+=int(s)

print(count)