'''
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are
an amicable pair and each of a and b are called amicable
numbers.

For example, the proper divisors of 220 are
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

#Find all divisors of n
def find_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)

    divisors.remove(n)
    return list(set(divisors))

#Sum all amicable numbers below n
def sum_amicable(n):

    #All numbers under n
    numbers=[i for i in range(n+1)]
    sol=0

    #index
    i=-1
    while i<len(numbers)-1:
        i+=1
        if numbers[i]==0:
            continue
        
        #First sum
        sum1=sum(find_divisors(numbers[i]))

        #If already tested continue
        if sum1>n or numbers[sum1]==0:
            continue
        
        #Check if numbers are amicable or delete them from list
        else:
            sum2=sum(find_divisors(numbers[sum1]))
            if sum2==numbers[i] and sum1!=sum2:
                #print(numbers[i], numbers[sum1])
                sol+=sum1+sum2
                numbers[sum1]=0
            else:
                numbers[sum1]=0
    return sol

#Parameters
number=10000

print(sum_amicable(number))


