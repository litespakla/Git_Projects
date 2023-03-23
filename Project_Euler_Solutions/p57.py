'''
It is possible to show that the square root of two can be
expressed as an infinite continued fraction.

By expanding this for the first four iterations, we get:

n1= 1 + 1/2 = 3/2
n2= 1 + 1/(2 + 1/2) =7/5
n3= 1 + 1/(2 + 1/(2+1/2)) = 17/12
n4= 1 + 1/(2 + 1/(2 + 1/(2 + 1/2)))  = 41/29

The eighth expansion is the first example where the number of
digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a
numerator with more digits than the denominator?
'''

from fractions import Fraction

def continued_fraction(i):
    # Base case: when i is 0, return 1/2
    fraction=Fraction(0)
    for _ in range(i):
        fraction=Fraction(1, 2+fraction)
    return 1 + fraction

def get_numerator_denominator(exp):
    # Get the numerator and denominator of the ith expansion for first exp expansions
    count=0
    for i in range(1, exp):
        expansion = continued_fraction(i)
        num, den= expansion.numerator, expansion.denominator
        if len(str(num))>len(str(den)):
            count+=1
    return count

print(get_numerator_denominator(1000))
