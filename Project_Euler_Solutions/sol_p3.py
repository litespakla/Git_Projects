'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

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
    return max(prime_divisors)

#parameter
n=600851475143

print(get_prime_divisors(n))
