'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

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

#Get  prime below w which can be written as the longest sum of consecutive primes
def longest_sum(n):
    primes=get_primes_below_n(n)
    max_sum = 0
    max_length = 0
    for i in range(len(primes)):
        sum_primes = 0
        for j in range(i, len(primes)):
            sum_primes += primes[j]
            if sum_primes > n:
                break
            length = j - i + 1
            if length > max_length and sum_primes in primes:
                max_length = length
                max_sum = sum_primes
    return max_sum, max_length

print(longest_sum(1000000))
