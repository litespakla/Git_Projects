'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

#Return largest prime factor of x
def largest_prime(x):
    i=2
    while i**2<x:
        if x%i==0:
            x=int(x/i)
        else:
            i+=1
    return x

print(largest_prime(600851475143))
