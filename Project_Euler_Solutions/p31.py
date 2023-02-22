'''
In the United Kingdom the currency is made up of pound (£) and pence (p).
There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

#Different ways to make money with given coins
def coin_change(coins, money):
    C = [0]*(1+money)
    print(C)
    C[0] = 1
    for coin in coins:
        for i in range(coin, money+1):
            C[i] += C[i-coin]
    return C[-1]

#Available coins
coins = [1, 2, 5, 10, 20, 50, 100, 200]

print(coin_change(coins, 200))
