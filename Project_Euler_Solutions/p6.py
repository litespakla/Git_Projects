'''
The sum of the squares of the first ten natural numbers is 385,

The square of the sum of the first ten natural numbers is 3025,

Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025-385=2640.

Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.
'''

#Square of the sum of first n numbers
def square_sum(n):
    return int(n*(n+1)/2)**2

#Sum of the squares of first n numbers
def sum_square(n):
    sol=0
    for i in range(n+1):
        sol+=i**2
    return sol

#Diference between sum of the squares and square of the sum of first n numbers
def dif_square(n):
    return square_sum(n)-sum_square(n)

print(dif_square(100))
