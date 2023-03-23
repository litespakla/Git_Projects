'''
Starting with 1 and spiralling anticlockwise in the following way,
a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal,
but what is more interesting is that 8 out of the 13 numbers lying along both
diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with
side length 9 will be formed. If this process is continued, what is the side length
of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
'''

import numpy as np
import math

#Check if number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#Finds the length of square spiral which prime ratio along diagonals is less than value
def diagonal_ratio(value):
    n=1
    iter=1
    count=0
    ratio=1
    i=2
    #Iterate until the ratio is less than the value
    while value<ratio:
        #Calculate the diagonals of the square
        for _ in range(4):
            n+=i
            if iter%4!=0:
                if is_prime(n):
                    count+=1
            iter+=1
        i+=2
        ratio=count/(2*int(math.sqrt(n))-1)
    return 1+int(math.sqrt(n))-int(math.sqrt(n))%2

print(diagonal_ratio(0.1))
