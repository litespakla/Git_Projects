'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

def nth_prime(n):
    if n < 2:
        return 2
    primes = [2]
    num = 3
    while len(primes) < n:
        for p in primes:
            if num % p == 0:
                break
        else:
            primes.append(num)
        num += 2
    return primes[-1]

print(nth_prime(10001))
