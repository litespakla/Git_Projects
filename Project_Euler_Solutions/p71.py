'''
Consider the fraction, n/d, where n and d are positive integers. If 
n<d and HCF(n, d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d<=8 in ascending 
order of size, we get:
 
It can be seen that 2/5 is the fraction immediately to the left of 3/7.
 
By listing the set of reduced proper fractions for d<=1000000 in ascending 
order of size, find the numerator of the fraction immediately to the left of
3/7.
'''

from math import gcd

d=1000000
frac='3/7'

#Number to the left of the defined fraction
value=int(frac.split('/')[0])/int(frac.split('/')[1])
sol=[(0, 0), (frac, value)]


for n in range(2, d+1):
    for i in range(int(value*n), 0, -1):
        if gcd(n, i)==1:
            #print(i, n, i/n)
            if sol[0][1]<i/n<value:
                sol[0]=(str(i)+'/'+str(n), i/n)
                #print(sol)
            break

print(sol)