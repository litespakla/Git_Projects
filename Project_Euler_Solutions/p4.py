'''
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

#Finds largest palindrome fron the product of two n-digit numbers
def palindrome(n):
    solution=0
    for i in range(-1+10**(n-1), 10**n):
        for j in range(-1+10**(n-1), 10**n):
            s=str(i*j)
            if s == s[::-1] and solution <i*j:
                solution=i*j
    return solution

print(palindrome(3))
