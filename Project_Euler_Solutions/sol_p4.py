'''
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

# Function to check if a number is palindrome
def is_palindrome(n):
    return str(n) == str(n)[::-1]

# Get largest palindrome made from the product of two n-digit numbers
def largest_n_palindrom(n):

    # Finding the largest palindrome from the product of two n-digit numbers
    largest_palindrome = 0
    factors = (0, 0)

    #iterate over n-digit numbers
    for i in range(-1+10**n, 10**(n-1), -1):
        for j in range(-1+10**n, 10**(n-1), -1):
            product = i * j
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product
                factors = (i, j)

    return largest_palindrome, factors

#parameter
n=3

print(largest_n_palindrom(n))


    