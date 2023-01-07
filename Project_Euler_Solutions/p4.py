'''
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

solution=0

for i in range(99, 1000):
    for j in range(99, 1000):
        s=str(i*j)
        if s == s[::-1] and solution <i*j:
            solution=i*j

print(solution)
