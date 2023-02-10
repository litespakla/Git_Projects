'''
A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions
with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest
recurring cycle in its decimal fraction part.
'''

#calculates the value of 1/d with the longest cycle
def longest_cycle(d):
    ans=0
    for i in range(2, d):
        cycle=[]
        num=[10]
        while True:
            cycle.append(num[-1]//i)
            num.append(10*(num[-1]%i))
            if num.count(num[-1]) >1:
                break
        if len(cycle)>ans:
            ans=i
    return ans

print(longest_cycle(1000))
