'''
Reference functions for solving the problems
'''

import numpy as np
from sympy import isprime

# Function to check if a number is palindrome
def is_palindrome(n):
    return str(n) == str(n)[::-1]

#Greatest common divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#Smallest common multiple of 2 numbers
def scm(a, b):
    return int(a*b/gcd(a,b))

#Smallest common multiple of first n numbers
def scm_first_n(n):
    sol=1
    #get scm of current number and i
    for i in range(1, n+1):
        sol=scm(sol, i)
    return sol

#Get prime divisors of n
def get_prime_divisors(n):
    prime_divisors = set()
    # Check for number of 2s that divide n
    while n % 2 == 0:
        prime_divisors.add(2)
        n //= 2
    # n must be odd at this point, so a skip of 2 (i.e., 3, 5, 7, 9, ...) is fine
    for i in range(3, int(n**0.5) + 1, 2):
        # While i divides n, add i and divide n
        while n % i == 0:
            prime_divisors.add(i)
            n //= i
    # This condition is to check if n is a prime number greater than 2
    if n > 2:
        prime_divisors.add(n)
    return prime_divisors

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

###################################################3

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


 