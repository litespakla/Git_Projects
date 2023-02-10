'''
Starting with the number 1 and moving to the right
in a clockwise direction a 5 by 5 spiral is formed
as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on
the diagonals is 101.

What is the sum of the numbers on the diagonals
in a 1001 by 1001 spiral formed in the same way?
'''

import numpy as np
import math

#Calculate sum of the elements of the diagonal of a nxn spiral
def create_spiral(n):
    spiral=np.zeros((n, n))
    ans=1
    #Movement direction
    dir=1
    #Location of 1
    row=math.ceil(n/2)-1
    column=row
    #Start with 1
    spiral[row][column]=1
    column+=1
    #Fill matrix
    for i in range(2, 1+n**2):
        if row==column or row==n-1-column:
            ans+=i
        #Move to the right
        if dir==1:
            spiral[row][column]=i
            if spiral[row+1][column]!=0:
                column+=1
            else:
                row+=1
                dir=2
        #Move down
        elif dir==2:
            spiral[row][column]=i
            if spiral[row][column-1]!=0:
                row+=1
            else:
                column-=1
                dir=3
        #Move to the left
        elif dir==3:
            spiral[row][column]=i
            if spiral[row-1][column]!=0:
                column-=1
            else:
                row-=1
                dir=4
        #Move up
        elif dir==4:
            spiral[row][column]=i
            if spiral[row][column+1]!=0:
                row-=1
            else:
                column+=1
                dir=1
    return ans

print(create_spiral(1001))
