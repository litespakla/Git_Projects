'''
Surprisingly there are only three numbers that can be written as
the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum
of fifth powers of their digits.
'''

#Finds the sum of all numbers that can be written as fith powers
def fifth_sum():
    sum=0
    #You can express numbers up to six digits as fifth power sums
    for i in range(10, 1+6*9**5):
        number=0
        word=str(i)
        for char in word:
            number+=int(char)**5
        if number==i:
            sum+=i
            #print(i)
    return sum

print(fifth_sum())
