'''
Euler's totient function, phi(n) [sometimes called the phi function], 
is defined as the number of positive integers not exceeding n
which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8
are all less than or equal to nine and relatively prime to nine, 
phi(9)=6.

n Relatively Prime	phi(n) n/phi(n)
2	   1	           1	2
3	  1,2	           2	1.5
4	  1,3	           2	2
5	1,2,3,4	           4	1.25
6	  1,5	           2	3
7	1,2,3,4,5,6	       6	1.1666...
8	1,3,5,7	           4	2
9	1,2,4,5,7,8	       6	1.5
10	1,3,7,9	           4	2.5

It can be seen that n=6 produces a maximum n/phi(n) for n<10.

Find the value of n<=1000000 for which n/phi(n) is a maximum.
'''

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

#Check if number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n=1000000
number=[0, 0, 0]

for i in range(2, n+1):
    if is_prime(i):
        continue

    totient=i
    for p in get_prime_divisors(i):
        totient*=(1-1/p)

    if i/totient>number[2]:
        number=[i, totient, i/totient]

print(number)