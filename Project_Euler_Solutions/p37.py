'''
The number 3797 has an interesting property. Being prime itself,
it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable
from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

#Check if number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#Check if a prime is truncatable
def is_truncatable_prime(p):
    # Check if p is truncatable from left to right
    for i in range(1, len(p)):
        if not is_prime(int(p[i:])):
            return False
    # Check if p is truncatable from right to left
    for i in range(1, len(p)):
        if not is_prime(int(p[:-i])):
            return False
    return True

#From a seed generates all truncatable primes
def add_recursion(seed):
    nums=['1', '3', '7', '9']
    sol=[]
    for num in nums:
        right=seed+num
        if is_prime(int(right)):
            sol+=add_recursion(right)
            if is_truncatable_prime(right):
                sol.append(int(right))
    return sol

#Generates all truncatable that exist and returns the sum
def truncatable_generator():
    seeds=['2', '3', '5', '7']
    truncatable_primes=[]
    for p in seeds:
        truncatable_primes+=add_recursion(p)
    #print(truncatable_primes)
    return sum(truncatable_primes)

print(truncatable_generator())

#Brute force solution
'''
#Check if a prime p is truncatable
def is_truncatable_prime(p, primes):
    # Check if p is truncatable from left to right
    for i in range(1, len(str(p))):
        if int(str(p)[i:]) not in primes:
            return False
    # Check if p is truncatable from right to left
    for i in range(1, len(str(p))):
        if int(str(p)[:-i]) not in primes:
            return False
    return True

#Finds all primes that are truncatable below a limit
def find_truncatable_primes(limit):
    # Generate all prime numbers up to limit using Sieve of Eratosthenes
    primes = set(range(2, limit))
    for i in range(2, int(limit**0.5) + 1):
        if i in primes:
            primes -= set(range(i**2, limit, i))
    # Find all truncatable primes
    truncatable_primes = []
    for p in primes:
        if p < 10:
            continue
        if is_truncatable_prime(p, primes):
            truncatable_primes.append(p)
    return sum(truncatable_primes)

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
print(find_truncatable_primes(1000000))
'''
