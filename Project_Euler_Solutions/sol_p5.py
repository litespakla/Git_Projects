'''
2520 is the smallest number that can be divided by each
of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?
'''

#Greatest common divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#Smallest common multiple of 2 numbers
def scm(a, b):
    return int(a*b/gcd(a,b))

#Smallest common multiple of first n numbers
def scm_first_n(n):
    sol=1

    #get scm of current number and i
    for i in range(1, n+1):
        sol=scm(sol, i)

    return sol

#parameter
n=20

print(scm_first_n(n))