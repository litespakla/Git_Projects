'''
A perfect number is a number for which the sum of its proper divisors
is exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less
than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant
numbers is 24. By mathematical analysis, it can be shown that all integers
greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis
even though it is known that the greatest number that cannot be expressed
as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written
as the sum of two abundant numbers.
'''
 
import math

#Returns all natural divisors of n
def divisors(n):
    divisors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    divisors.discard(n)
    return divisors

#Return a list of abundant numbers less than a limit
def abundant_numbers(limit):
    abundant = []
    for i in range(1, limit):
        if sum(divisors(i)) > i:
            abundant.append(i)
    return abundant

#Return the sum of all positive integers that cannot be written as the sum of two abundant numbers
def find_non_abundant_sums(limit):
    abundant = abundant_numbers(limit)
    abundant_sums = set()
    #Get all possible sums of the abundant numbers
    for i in range(len(abundant)):
        for j in range(i, len(abundant)):
            abundant_sums.add(abundant[i] + abundant[j])
    #Remove all sums from all the numbers until the limit
    non_abundant_sums = set(range(1, limit)) - abundant_sums
    return sum(non_abundant_sums)

#Parameters
limit=28123

print(find_non_abundant_sums(limit))
