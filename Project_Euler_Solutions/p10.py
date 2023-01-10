'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

#Check if number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#Returns sum of all primes below n
def prime_sum(n):
    solution=0
    for i in range(n):
        if is_prime(i):
            solution+=i
    return solution

#Returns sum of all primes below n using a Sieve of Erathostenes for n
def prime_sum2(n):
    sieve=list(range(2, n))
    # Create a list of all the integers from 2 to n
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            # Mark as composite all the multiples of i
            for j in range(i * i, n + 1, i):
                primes[j] = False
    #List of primes below n
    primes= [i for i in range(2, n + 1) if primes[i]]
    #Returns sum of elements of the list
    return sum(primes)

#print(prime_sum(2000000))
print(prime_sum2(2000000))
