'''
The decimal number, 585 = 10010010012 (binary),
is palindromic in both bases.

Find the sum of all numbers, less than one million,
which are palindromic in base 10 and base 2.

(Please note that the palindromic number,
in either base, may not include leading zeros.)
'''

#Check if the binary form of a number is palindromic
def is_palindromic_binary(n):
    binary = bin(n)[2:]
    return binary == binary[::-1]

#Finds the sum of all numbers less than n which are palindromic in base 10 and base 2
def sum_palindromic(n):
    ans=0
    for i in range(n):
        s=str(i)
        if s == s[::-1] and is_palindromic_binary(i):
            ans+=i
    return ans

print(sum_palindromic(1000000))
