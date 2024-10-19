'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

#get pythagorean triplet and product for a+b+c=n
def pythagorean_product_sum(n):
    sol=[]

    #a and b go to n/2 
    for a in range(n//2):
        for b in range(a,n//2):
            c=n-a-b
            if a**2+b**2==c**2:
                sol.append([(a,b,c),a*b*c])

    return sol

#Parameters
n=1000

print(pythagorean_product_sum(n))