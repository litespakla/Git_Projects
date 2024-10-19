'''
The sum of the squares of the first ten natural numbers is 385,

The square of the sum of the first ten natural numbers is 3025,

Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025-385=2640.

Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.
'''

#Diference between sum of the squares and square of the sum of first n numbers 
def dif_sum_squares(n):
    sum_sq=0
    sq_of_sum=(n*(n+1))//2

    #loop
    for i in range(n+1):
        sum_sq+=i**2

    return sq_of_sum**2-sum_sq

#parameter
n=100

print(dif_sum_squares(n))