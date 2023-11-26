'''
Comparing two numbers written in index form like 2^11 and 3^7
is not difficult, as any calculator would confirm that
2^11 = 2048 < 3^7 = 2187.

However, confirming that 632382^518061 > 519432^525806 would
be much more difficult, as both numbers contain over three
million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'),
a 22K text file containing one thousand lines with a base/exponent
pair on each line, determine which line number has the greatest
numerical value.

NOTE: The first two lines in the file represent the numbers in the
example given above.
'''
import math

#Return biggest number where a=[base, exponent]
def biggest_exp(a, b):
    if a[1]*math.log(a[0]) > b[1]*math.log(b[0]):
        return a
    else:
        return b

#Name of file that contains numbers
name='p099_base_exp.txt'

#Opens file
file= open(name, 'r')

#line in file
i=1

#To store values with biggest number
n=n1=[1, 1]
j=0

#Check every line of the document
for line in file:
    row=line.split(',')
    m=[int(x) for x in row]
    n=biggest_exp(n, m)

    #if n changes, store ith line value in j
    if m==n:
        j=i
    i+=1

print(n, j)
