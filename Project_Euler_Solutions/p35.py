'''
The number, 197, is called a circular prime because all rotations
of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

#Returns rotations of a number n
def rotations(n):
    n_str = str(n)
    rotations = [int(n_str)]
    for i in range(1, len(n_str)):
        rotation = int(n_str[i:] + n_str[:i])
        rotations.append(rotation)
    return rotations

#Check if number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#Counts how many circular numbers are below n
def circular(n):
    count=0
    for i in range(n):
        if all(is_prime(j) for j in rotations(i)):
            count+=1
    return count

print(circular(1000000))
