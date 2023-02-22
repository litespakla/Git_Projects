'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the
factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
'''

import math

#Finds the sum of all numbers that can be written as sum of factorial
def fact_sum():
    sum=0
    #You can express numbers up to seven digits as factorial sums
    for i in range(10, 1+math.factorial(9)*7):
        number=0
        word=str(i)
        for char in word:
            number+=math.factorial(int(char))
        if number==i:
            sum+=i
            #print(i)
    return sum

print(fact_sum())
