'''
Reference functions for solving the problems
'''

import numpy as np
from sympy import isprime

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

#Finds nth prime
def nth_prime(n):
    if n < 2:
        return 2
    primes = [2]
    num = 3
    while len(primes) < n:
        #loop else
        for p in primes:
            if num % p == 0:
                break
        else:
            primes.append(num)
        num += 2
    return primes[-1]

#Check if number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#Check if the binary form of a number is palindromic
def is_palindromic_binary(n):
    binary = bin(n)[2:]
    return binary == binary[::-1]

#Gets the indexes of all possible subset combinations
def get_subset_indices(lst):
    n = len(lst)
    subsets = [[]]
    for i in range(n):
        for j in range(len(subsets)):
            subsets.append(subsets[j] + [i])
    return subsets

#Find all divisors of n
def find_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
    return list(set(divisors))

#Get a list of primes below n
def get_primes_below_n(n):
    primes = []
    is_prime = [True] * n
    for i in range(2, n):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n, i):
                is_prime[j] = False
    return primes
