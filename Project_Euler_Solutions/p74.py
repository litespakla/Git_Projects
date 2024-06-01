'''
The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
1!+4!+5!=1+24+120=145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169;
it turns out that there are only three such loops that exist:
169->363601->1451->169
871->45361->871
872->45362->872
 
It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,
540->145->145
 
Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with 
a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
'''

from math import factorial

# Precompute the factorial of digits 0 to 9
factorials = [factorial(i) for i in range(10)]

# Cache to store the length of chains
chain_cache = {}

def chain_length(start):
    """Compute the length of the non-repeating chain starting from a given number using caching."""
    seen = {}
    current = start
    length = 0

    while current not in seen:
        if current in chain_cache:
            length += chain_cache[current]
            break
        seen[current] = length
        current = sum(factorials[int(digit)] for digit in str(current))
        length += 1

    # Update the cache with the new lengths
    for key, value in seen.items():
        chain_cache[key] = length - value

    return length

# Count chains with exactly 60 non-repeating terms
count = 0
limit = 10**6
size=60

for i in range(limit):
    if chain_length(i) == size:
        count += 1

print(count)