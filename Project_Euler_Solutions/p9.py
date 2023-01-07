'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

#Looks for triplets for a+b+c=n and returns them with their product
def find_triplet(n):
    triplet=[]
    for a in range(1, n):
        for b in range(a, n):
            c = n - a - b
            if a**2 + b**2 == c**2:
                triplet.append([(a,b,c), a*b*c])
    return triplet

print(find_triplet(1000))
