'''
Consider the fraction, n/d, where n and d are positive integers. If 
n<d and HCF(n, d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d<=8 in ascending 
order of size, we get:

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced 
proper fractions for d<=12000?
'''

from math import gcd

d=12000
frac1='1/3'
frac2='1/2'

#Number to the left of the defined fraction
value1=int(frac1.split('/')[0])/int(frac1.split('/')[1])
value2=int(frac2.split('/')[0])/int(frac2.split('/')[1])
sol=0

for n in range(2, d+1):
    for i in range(int(value1*n)+1, int(value2*n)+1):
        if gcd(n, i)==1 and i/n<value2:
            #print(n, i)
            sol+=1

print(sol)