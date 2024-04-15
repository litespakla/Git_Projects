'''
Consider quadratic Diophantine equations of the form:

x²-Dy²=1

For example, when D=13, the minimal solution in x is
649²-13x180²=1.

It can be assumed that there are no solutions in positive integers when 
D is square.

By finding minimal solutions in x for D={2, 3, 5, 6, 7}, we obtain the following:

3²-2x2=1
2²-3x1=1
9²-5x4=1
5²-6x2=1
8²-7x3=1
 
Hence, by considering minimal solutions in x for D<=7, the largest x is obtained when 
D=5.

Find the value of D<=1000 in minimal solutions of x for which the largest value of 
x is obtained.
'''

import math

D=1000

def is_square(n):
    if n < 0:
        return False
    root = int(math.sqrt(n))
    return root * root == n

def odd_periodic_continued_fractions(i):
        
    m = 0
    d = 1
    a0 = a = math.isqrt(i)  # Integer part of the square root
    rep=[a0]

    while a != 2 * a0:
        m = d * a - m
        d = (i - m**2) // d
        a = (a0 + m) // d
        rep.append(a)

    return rep

def convergent_den(a, n):
    q0, q1 = 1, a[1]
    if n==0:
        return q0
    elif n==1:
        return q1
    
    for i in range(2, n+1):
        q1, q0 = a[i]*q1+q0, q1
    return q1

def convergent_num(a, n):
    p0, p1 = a[0], a[1]*a[0]+1
    if n==0:
        return p0
    elif n==1:
        return p1
    
    for i in range(2, n+1):
        p1, p0 = a[i]*p1+p0, p1
    return p1

ans=[0, 0]

for i in range(2, D+1):
    if is_square(i):
        continue

    a=odd_periodic_continued_fractions(i)

    if len(a)%2==0:
        a=a+a[1:-1]
        num=convergent_num(a, len(a)-1)
    else:
        a=a[0:-1]
        num=convergent_num(a, len(a)-1)
    
    #print(i, num)
    if num>ans[0]:
        ans=[num, i]
    
print(ans)