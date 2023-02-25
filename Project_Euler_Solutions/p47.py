'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each.
What is the first of these numbers?
'''

#Check if number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#Find all divisors of n
def find_prime_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
    return set([div for div in divisors if is_prime(div)])

#Finds the first of n consecutive integers to have n different prime factors
def consecutive_primes(n):
    i=0
    while True:
        i+=1
        if len(find_prime_divisors(i))!=n:
            continue
        elif all(len(find_prime_divisors(i+j))==n for j in range(1, n)):
            #print(find_prime_divisors(i), i)
            return i

print(consecutive_primes(4))
