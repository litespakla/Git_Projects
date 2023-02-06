'''
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are
an amicable pair and each of a and b are called amicable
numbers.

For example, the proper divisors of 220 are
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

import math

#Returns all natural divisors of n
def natural_divisors(n):
    divisors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    divisors.discard(n)
    return divisors

#Sum all amicable numbers below n
def sum_amicables(n):
    sol=0
    numbers=[i for i in range(n)]
    for i in numbers:
        x=sum(natural_divisors(i))
        if i==sum(natural_divisors(x)) and i!=x and x in numbers:
            sol+= i+x
        if x>i and x in numbers:
            numbers.remove(x)
    return sol

print(sum_amicables(10000))
