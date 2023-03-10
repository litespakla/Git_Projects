'''
The number, 1406357289, is a 0 to 9 pandigital number because it is
made up of each of the digits 0 to 9 in some order, but it also has
a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on.
In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
'''

import itertools

#Finds the sum of all 0 to 9 pandigital numbers with the property
def sum_pandigital():
    digits=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    primes=[2, 3, 5, 7, 11, 13, 17]
    ans=0
    all_permutations = list(itertools.permutations(digits))
    for permutation in all_permutations:
        #Reject some non-valid permutations of the number
        if permutation[0]=='0' or int(permutation[3])%2!=0 or int(permutation[5])%5!=0:
            continue
        number = ''.join(element for element in permutation)
        d=[int(permutation[i]+permutation[i+1]+permutation[i+2]) for i in range(1, 8)]
        if all(d[j]%primes[j]==0 for j in range(len(d))):
            ans+=int(number)
    return ans

print(sum_pandigital())
