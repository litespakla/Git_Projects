'''
All square roots are periodic when written as continued fractions and can be written in the form:

For example, let us consider 

If we continue we would get the following expansion:

The process can be summarised as follows:
 
It can be seen that the sequence is repeating. For conciseness, we use the notation 
to indicate that the block (1,3,1,8) repeats indefinitely.

The first ten continued fraction representations of (irrational) square roots are:

Exactly four continued fractions, for n<=13, have an odd period.

How many continued fractions for n<=10000 have an odd period?
'''

import math

def odd_periodic_continued_fractions():
    odd_fracs = 0
    perfect_squares = {i**2 for i in range(101)}  # Set of perfect squares
    print(perfect_squares)
    for i in range(2, 10001):
        if i in perfect_squares:  # Skip perfect squares
            continue

        m = 0
        d = 1
        a0 = a = math.isqrt(i)  # Integer part of the square root
        rep=[]

        while a != 2 * a0:
            m = d * a - m
            d = (i - m**2) // d
            a = (a0 + m) // d
            rep.append(a)

        if len(rep) % 2 == 1:
            odd_fracs += 1
            #print(i, rep, len(rep))

    return odd_fracs

# To run the function and get the result
result_faster = odd_periodic_continued_fractions()
print(result_faster)
