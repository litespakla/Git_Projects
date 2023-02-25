'''
If p is the perimeter of a right angle triangle with
integral length sides, {a,b,c}, there are exactly three
solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

#Finds all integer pitagorean triplets for n
def pythagorean_triples(n):
    triples = []
    for a in range(1, n//2):
        for b in range(a+1, 1+n//2):
            c = n - a - b
            if a*a + b*b == c*c:
                triples.append((a, b, c))
    return triples

#Finds which integer below a limit has the most pitagorean triplets
def most_solutions(limit):
    ans=0
    max_size=0
    for n in range(1, limit):
        triples = pythagorean_triples(n)
        if len(triples)>max_size:
            ans=n
            max_size=len(triples)
    return ans

print(most_solutions(1000))
