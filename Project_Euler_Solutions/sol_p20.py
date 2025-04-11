'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is
3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

#Sum the digits of n!
def sum_fact(n):
    fact=1
    for i in range(1, n+1):
        fact*=i

        #Eliminate the 0s
        while str(fact)[-1]=='0':
            fact=int(str(fact)[:-1])
    sol=0
    for i in str(fact):
        sol+=int(i)

    return sol

#Parameters
number=100

print(sum_fact(number))