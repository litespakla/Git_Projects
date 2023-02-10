'''
Euler discovered the remarkable quadratic formula:

n²+n+41

It turns out that the formula will produce 40 primes
for the consecutive integer values 0<n<40
However, when n=40, result is divisible by 41,
and certainly when n=41 is clearly divisible by 41.

The incredible formula n²-79n+1601 was discovered,
which produces 80 primes for the consecutive values 0<n<80.
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n²+an+b where |a|<1000 and |b|<=1000
where |n| is the modulus/absolute value of n
e.g. |11|=11 and |-4|=4

Find the product of the coefficients a and b,
for the quadratic expression that produces the maximum number
of primes for consecutive values of n, starting with n=0
'''

#Check if number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#Returns the product of the coefficients a, b of the quadratic equation
#that produces the maximum number of primes for consecutive values of n
def consecutive_primes(a, b):
    longest=0
    for i in range(-a, a+1):
        for j in range(-b, b+1):
            n=0
            while True:
                x=n**2+i*n+j
                if not is_prime(x):
                    break
                n+=1
            if n>longest:
                longest=n
                ans_a=i
                ans_b=j
    return ans_a*ans_b

print(consecutive_primes(1000, 1000))
