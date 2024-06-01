'''
It turns out that 12cm is the smallest length of wire that can be bent 
to form an integer sided right angle triangle in exactly one way, 
but there are many more examples.

12cm: (3, 4, 5)
24cm: (6, 8, 10)
30cm: (5, 12, 13)
36cm: (9, 12, 15)
40cm: (8, 15, 17)
48cm: (12, 16, 20)

In contrast, some lengths of wire, like 20cm, cannot be bent to form an 
integer sided right angle triangle, and other lengths allow more than 
one solution to be found; for example, using 120cm it is possible to form 
exactly three different integer sided right angle triangles.

120cm: (30, 40, 50), (20, 48, 52), (24, 45, 51) 

Given that L is the length of the wire, for how many values of 
L<=1500000 can exactly one integer sided right angle triangle be formed?
'''

from math import gcd

# Generate Pythagorean triplets using Euclid's formula
def count_single_right_triangles(L):
    tuples_sum=[0]*(L+1)

    for i in range(1, int((L/2)**0.5)+1):
        for j in range(i, int((L/2)**0.5)+1):

            if gcd(i, j)==1 and (j-i)%2==1:
                lenght=2*j*(i+j) #Euclid's formula

                while lenght<L:
                    tuples_sum[lenght]+=1
                    lenght+=2*j*(i+j)

    return len([key for key in tuples_sum if key == 1])

limit=1500000
print(count_single_right_triangles(limit))

