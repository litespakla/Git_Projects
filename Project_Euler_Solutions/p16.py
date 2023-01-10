'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

#Sums digits of 2^n
def sum_digits(n):
    s=str(2**n)
    solution=0
    for i in s:
        solution+=int(i)
    return solution

print(sum_digits(1000))
