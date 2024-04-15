'''
The square root of 2 can be written as an infinite continued fraction.

The infinite continued fraction can be written, sqrt(2)=[1; (2)], (2)
indicates that 2 repeats ad infinitum. In a similar way,
sqrt(23)=[4; (1, 3, 1, 8)].

It turns out that the sequence of partial values of continued fractions 
for square roots provide the best rational approximations. 
Let us consider the convergents for sqrt(2).

Hence the sequence of the first ten convergents for sqrt(2) are:

What is most surprising is that the important mathematical constant,
e=[2; 1, 2, 1, 1, 4, 1, 1, 6, 1, ..., 1, 2k, 1, ...].

The first ten terms in the sequence of convergents for are:

The sum of digits in the numerator of the 10th convergent is 
1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the 
continued fraction for e

'''

import math
from decimal import *

getcontext().prec = 120
e=Decimal('2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391932003059922')
convergents=100

def continued_fractions(x):
    r0=x
    rep=[]

    for i in range(convergents):
        b0=int(r0)
        rep.append(b0)
        r0=Decimal(1)/Decimal(Decimal(r0)-Decimal(b0))
        #print(b0, r0)

    return rep

def convergent_num(a, n):
    p0, p1 = a[0], a[1]*a[0]+1
    if n==0:
        return p0
    elif n==1:
        return p1
    
    for i in range(2, n+1):
        p1, p0 = a[i]*p1+p0, p1
    return p1

series=continued_fractions(e)
nums=[convergent_num(series, i) for i in range(convergents)]

ans=0

for n in str(nums[-1]):
    ans+=int(n)

print(series)
print(ans)