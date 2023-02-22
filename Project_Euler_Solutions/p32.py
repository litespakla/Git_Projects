'''
We shall say that an n-digit number is pandigital if it makes use
of all the digits 1 to n exactly once; for example, the 5-digit number,
15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure
to only include it once in your sum.
'''

from itertools import permutations

#Sum of all pandigital products. Multiplicands have to have 5 digits and the
#product 4 digits
def pandigital():
    digits = set('123456789')
    numbers=[]
    for a in range(1, 10000):
        for b in range(a, 10000):
            product = a * b
            #To prevent products that use more than 9 digits
            if product > 9999:
                break
            digits_set = set(str(a) + str(b) + str(product))
            if len(digits_set) == 9 and digits_set == digits and product not in numbers:
                #print(a, b, product, digits_set)
                numbers.append(product)

    return sum(numbers)

print(pandigital())
