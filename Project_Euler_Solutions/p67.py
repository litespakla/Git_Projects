'''
By starting at the top of the triangle below and moving to
adjacent numbers on the row below, the maximum total from
top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt
(right click and 'Save Link/Target As...'), a 15K text file
containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18.
It is not possible to try every route to solve this problem,
as there are 299 altogether! If you could check one trillion (1012)
routes every second it would take over twenty billion years to
check them all. There is an efficient algorithm to solve it. ;o)
'''

#receives a tringle as a list of rows and finds max from top to bottom
def max_sum(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            try:
                triangle[i][j]+=max(triangle[i-1][j], triangle[i-1][j-1])
            except:
                triangle[i][j]+=triangle[i-1][j-1]
    return max(triangle[-1])

#Name of file that contains triangle
name='p067_triangle.txt'

#Opens file
file= open(name, 'r')

#Turn triangle in file into a list of rows (similar to problem 18)
t=[]
for line in file:
    t.append([])
    row=line.split()
    for n in row:
        t[-1].append(int(n))

print(max_sum(t))
