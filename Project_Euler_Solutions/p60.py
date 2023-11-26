'''
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes 
and concatenating them in any order the result will always be prime. For example, 
taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes,
792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes 
concatenate to produce another prime.
'''

import itertools

#Get a list of primes below n
def get_primes(n):
    primes = []
    is_prime = [True] * n
    for i in range(2, n):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n, i):
                is_prime[j] = False
    return [str(i) for i in primes]

#Check if number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#Lenght of the list 
n=5

#We try with every prime below a limit
limit=10000

max_length = 0

#Alternative solution
'''
while max_length<n:

    #Primes below a limit
    primes=get_primes(limit)

    #Candidates are every prime
    candidates=[[i] for i in primes]

    for z in range(n):
        plist=candidates.copy()
        while len(plist)>0:
            l0=plist.pop(0)
            max_l0=max([int(i) for i in l0])
            for p in primes:
                candidate=l0.copy()
                if int(p)<max_l0:
                    continue
                if all(is_prime(int(p+k)) and is_prime(int(k+p)) and p not in l0 for k in l0):
                    print(p, l0)
                    candidate.append(p)
                    candidates.append(candidate)
                    
                    # Convert lists to remove into sorted tuples for easy comparison
                    sublists_to_remove = [candidate[:i] + candidate[i+1:] for i in range(len(candidate))]
                    sets_to_remove = {tuple(sorted(lst)) for lst in sublists_to_remove}


                    # Use list comprehension to filter out the sublist
                    plist = [sublist for sublist in plist if tuple(sorted(sublist)) not in sets_to_remove]
                    
        max_length = max(len(lst) for lst in candidates)
        if max_length==z+2:

            #Remove all elements of length n-1
            candidates = [lst for lst in candidates if len(lst) == z+2]
        else:
            break

    if max_length==n:
        print('Candidates for n=', n)
        for c in candidates:
            print(c, sum([int(i) for i in c]))
    else:
        limit*=10
        print('new run', limit)
'''

def nested_loop(lst, init, previous, final_n):
    for i in range(init, len(lst)):
        if not previous:
            test=nested_loop(lst, init+1, [lst[i]], final_n-1)
            if not test:
                continue
            else:
                print(test, sum([int(j) for j in test]))
                return test
            
        test=previous+[lst[i]]
        if all(is_prime(int(item[0]+item[1])) and is_prime(int(item[1]+item[0])) for item in itertools.combinations(test, 2)):
            if final_n!=0:
                #print(test)
                test=nested_loop(lst, i+1, test, final_n-1)
                if not test:
                    continue
                else:
                    return test
            else:
                return test
    return False


#Primes below a limit
primes=get_primes(limit)

while not nested_loop(primes, 0, [], n-1):
    limit*=10
    primes=get_primes(limit)
    print('new run', limit)
    


