'''
An irrational decimal fraction is created by concatenating the
positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part,
find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

#Finds the value of the product of d10^n blow a limit of digits
def product_fraction(limit):
    word='.'
    i=1
    ans=1
    #Produces digits for the fractional part
    while len(word)<limit+1:
        word+=str(i)
        i+=1
    #Gets the product of the digits
    exp=1
    while 10**exp<limit+1:
        print(len(word), 10**exp)
        ans*=int(word[10**exp])
        exp+=1
    return ans

print(product_fraction(1000000))
