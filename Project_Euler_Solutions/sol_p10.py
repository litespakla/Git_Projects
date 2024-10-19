'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

#Get a list of primes below n
def sum_get_primes_below_n(n):
    primes = []
    is_prime = [True] * n

    #erathostenes algorithm
    for i in range(2, n):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n, i):
                is_prime[j] = False

    return sum(primes)

#Parameters
n=2000000

print(sum_get_primes_below_n(n))

