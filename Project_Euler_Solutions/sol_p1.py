'''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

#Get the sum of all multiples in numbers below n
def natura_multiples(numbers, n):
    sol=0

    #iterate over n
    for i in range(n):
        
        #find if multiple
        for j in numbers:
            if i%j==0:
                sol+=i
                break
    return sol

#parameters
numbers=[3, 5]
n=1000

print(natura_multiples(numbers, n))
