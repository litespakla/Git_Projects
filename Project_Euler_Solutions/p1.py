'''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

#Finds the sum of all multiples of 3 or 5 below n
def multiples_3_5(n):
    result=0
    for i in range(n):
        if i%3==0 or i%5==0:
            result+=i
    return result

print(multiples_3_5(1000))
