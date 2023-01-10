'''
You are given the following information, but you may prefer
to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4,
but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during
the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

#Counts number of Sundays between a year and an end year.
#Start is 1 Jan of the given year (0 for Sun, 1 for Mon, 2 for Tues, etc)
def count_sunday(year, end, start):
    n_leap=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    count=0
    while year<end:
        if year%4==0 and year%400!=0:
            for n in leap:
                start+=n
                start=start%7
                if start==0:
                    count+=1
        else:
            for n in n_leap:
                start+=n
                start=start%7
                if start==0:
                    count+=1
        year+=1
    return count

print(count_sunday(1900, 2000, 1))
