'''
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, 
and each line adding to nine.

Working clockwise, and starting from the group of three with the numerically 
lowest external node (4,3,2 in this example), each solution can be described uniquely. 
For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. 
There are eight solutions in total.

Total	Solution Set
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; 
the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- 
and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?
'''

import itertools

numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

perm = itertools.permutations(numbers)

ring={}

sol='0'

for p in perm:
    ring[0]=(p[0], p[1], p[2])
    ring[1]=(p[3], p[2], p[4])
    ring[2]=(p[5], p[4], p[6])
    ring[3]=(p[7], p[6], p[8])
    ring[4]=(p[9], p[8], p[1])

    if all(sum(ring[0])==sum(ring[i]) for i in range(5)):
        lowest=ring[0][0]
        x=0
        for i in range(1, 5):
            if ring[i][0]<lowest:
                x=i
                lowest=ring[i][0]
                
        set=''
        for i in range(5):
            for n in ring[(x+i)%5]:
                set+=str(n)

        if int(set)>int(sol) and len(set)<17:
            sol=set

print(sol)