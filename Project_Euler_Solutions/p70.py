'''
Euler's totient function, phi(n) [sometimes called the phi function], is used to determine 
the number of positive numbers less than or equal to n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, 
phi(9)=6

The number 1 is considered to be relatively prime to every positive number, so phi(1)=1.

Interestingly, phi(87109)=79180, and it can be seen that 87109 is a permutation of 
79180.

Find the value of n, 1<n<10**7, for which phi(n) is a permutation of n and the ratio 
n/phi(n) produces a minimum.
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

n=10**5
number=[0, 0, n]

for i in range(2, n+1):
    if is_prime(i):
        continue

    totient=i
    for p in get_prime_divisors(i):
        totient*=(1-1/p)

    if len(str(i))==len(str(int(totient))):
        if ''.join(sorted(str(i)))==''.join(sorted(str(int(totient)))) and i/totient<number[2]:
            number=[i, totient, i/totient]
            print(number)
    
print(number)

