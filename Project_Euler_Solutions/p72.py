'''
Consider the fraction, n/d, where n and d are positive integers. If 
n<d and HCF(n, d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d<=8 in ascending 
order of size, we get:

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions 
for d<=1000000?
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
number=0

for i in range(2, n+1):
    if is_prime(i):
        number+=i-1
        continue

    totient=i
    for p in get_prime_divisors(i):
        totient*=(1-1/p)
    number+=int(totient)

print(number)