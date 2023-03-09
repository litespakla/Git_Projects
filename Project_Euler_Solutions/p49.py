'''
The arithmetic sequence, 1487, 4817, 8147,
in which each of the terms increases by 3330,
is unusual in two ways: (i) each of the three terms are prime,
and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

#Check if number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#Finds the numbers that have the property
def property():
    sol=[]
    for i in range(1001, 10000):
        if all(is_prime(i+3330*j) for j in range(3)):
            if set(str(i))==set(str(i+3330)) and set(str(i))==set(str(i+6660)):
                sol.append(str(i)+str(i+3330)+str(i+6660))
    return sol

print(property())
