'''
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
'''

#Return last n digits of series 1^1+2^2+...+1000^1000
def last_digits(n):
    sol=0
    for i in range(1, 1001):
        sol+=i**i%10**n
    return str(sol)[-n:]

print(last_digits(10))
