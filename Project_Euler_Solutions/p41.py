'''
We shall say that an n-digit number is pandigital if it
makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

import itertools

#Check if number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#Finds the largest n-digit pandigital prime that exists
def n_pandigital():
    largest=0
    for n in range(1, 10):
        digits=[str(i) for i in range(1, n+1)]
        all_permutations = list(itertools.permutations(digits))
        for permutation in all_permutations:
            number = ''.join(element for element in permutation)
            if int(number)>largest and is_prime(int(number)):
                largest=int(number)
    return largest

print(n_pandigital())
