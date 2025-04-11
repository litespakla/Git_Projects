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
    months=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    count_days=[0]*7

    #First month
    #count_days[start]+=1

    #Go through every year
    while year<=end:
        #print(year)
        
        #Check if leap year
        if year%4==0 and (year%100!=0 or year%400==0):
            months[1]=29
        else:
            months[1]=28

        #Rest of the months
        for days in months:
            count_days[start]+=1
            #print(start)
            start=(start+days)%7
        
        year+=1
    
    return count_days

#Parameters
start=1900
end=2000
first_jan=1

#Whe need 1st of january of 1901
#print(count_sunday(start, stat+1, first_jan))

print(count_sunday(start+1, end, 2))

