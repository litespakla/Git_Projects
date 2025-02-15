'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

# Function to compute the length of the Collatz sequence for a given starting number
def collatz_chain_length(n, memo):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    if n % 2 == 0:
        next_n = n // 2
    else:
        next_n = 3 * n + 1
    
    #Recursively calculate collatz length
    memo[n] = 1 + collatz_chain_length(next_n, memo)
    return memo[n]

#Calculates number under n with largest Collatz chain
def longest_collatz(n):
    numbers={}
    max_count=0
    num=0

    #Numbers
    for i in range(1, n+1):
        count=collatz_chain_length(i, numbers)
        
        #Collatz lenght
        if count>max_count:
            max_count=count
            num=i

    return num, max_count

#Parameters
n=10**6

print(longest_collatz(n))