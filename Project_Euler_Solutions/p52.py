'''
It can be seen that the number, 125874, and its double, 251748,
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x,
and 6x, contain the same digits.
'''

#Find the smallest positive integer n, such that 2n, 3n, 4n, 5n, and 6n contains the same digits
def smallest():
    n=0
    while True:
        n+=1
        if len(str(n))!=len(str(6*n)):
            continue
        elif all(sorted(str(n*i))==sorted(str(n)) for i in range(2, 7)):
            return n

print(smallest())
