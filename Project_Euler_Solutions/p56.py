'''
A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100,
what is the maximum digital sum?
'''

#Gets maximum digital sum of numbers of the form a^b
def max_sum(a, b):
    max_digit_sum=0
    for i in range(2, a):
        for j in range(1, b):
            digit_sum=0
            for digit in str(i**j):
                digit_sum+=int(digit)
            if digit_sum>max_digit_sum:
                max_digit_sum=digit_sum
    return max_digit_sum

print(max_sum(100, 100))
