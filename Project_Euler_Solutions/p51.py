'''
By replacing the 1st digit of the 2-digit number *3,
it turns out that six of the nine possible values:
13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit,
this 5-digit number is the first example having seven primes among
the ten generated numbers, yielding the family:
56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family,
is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number
(not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.
'''

import itertools

#Check if number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#Gets the indexes of all repeated positions
def check_repeated_chars(string):
    counts = {}
    repeated = []
    for i, char in enumerate(string):
        if char in counts:
            counts[char].append(i)
            if char not in repeated:
                repeated.append(char)
        else:
            counts[char] = [i]
    return [counts[char] for char in repeated]

#Finds the smallest prime which is part of an eight prime value family
def find_eight_prime_value_family():
    replacements=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    #Start with the smallest prime greater than 56003
    n = 56003
    while True:
        n += 1
        if not is_prime(n):
            continue
        #The replaced numbers have to be the same. We get their positions
        subset_indices = check_repeated_chars(str(n))
        #If there are not repeated numbers, it couldn't form the eight prime family
        if len(subset_indices)==0:
            continue
        for subset in subset_indices:
            fail=0
            #Replace numbers
            for replace in replacements:
                new_num=str(n)
                for index in subset:
                    new_num= new_num[:index] + replace + new_num[index+1:]
                #If number isn't prime, or if it's prime but first digit is 0, we fail
                if not is_prime(int(new_num)) or (is_prime(int(new_num)) and new_num[0]=='0'):
                    fail+=1
                #If we fail more than 2 times, the prime family isn't eight valued
                if fail>2:
                    break
            else:
                return n

print(find_eight_prime_value_family())
