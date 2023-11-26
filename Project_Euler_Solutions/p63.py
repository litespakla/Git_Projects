'''
The 5-digit number, 16807=7⁵, is also a fifth power. Similarly, the 
9-digit number, 1342117728=8⁹ , is a ninth power.

How many n-digit positive integers exist which are also an 
nth power?
'''

count=0
digits=1
exp=1

while len(str(9**exp))>=digits:
    for i in range(1, 10):
        if len(str(i**exp))==digits:
            count+=1
            #print(i, exp, len(str(i**exp)))
    exp+=1
    digits+=1

print(count)
