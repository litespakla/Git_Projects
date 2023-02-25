'''
It was proposed by Christian Goldbach that every odd composite number
can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of
a prime and twice a square?
'''

import math

#Check if number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#First composite odd number
x=9

while True:
    #If x is composite
    if not is_prime(x):
        #Calculate every possible x-2y^2
        for i in range(int(math.sqrt(x))):
            test=x-2*i**2
            #if x-2y^2 is prime, the Goldbach condition is true
            if is_prime(test):
                break
        #Otherwise x doesn't fulfill Goldbach condition
        else:
            print(x)
            break
    x+=2
