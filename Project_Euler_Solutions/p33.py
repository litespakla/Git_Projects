'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
'''

#Greatest common divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#Solves the problem
def fractions():
    num=1
    den=1
    for numerator in range(10, 100):
        for denominator in range(numerator+1, 100):
            num_digits = list(str(numerator))
            den_digits = list(str(denominator))
            #A repeated digit gets cancelled
            cancelled = set(num_digits) & set(den_digits)
            #In case we divide by 0 or the set is empty
            try:
                cancelled_digit = cancelled.pop()
                #If cancelled digit is 0 it's trivial
                if len(cancelled) == 0 and cancelled_digit!='0':
                    num_digits.remove(cancelled_digit)
                    den_digits.remove(cancelled_digit)
                    if numerator/denominator==int(num_digits[0])/int(den_digits[0]):
                        num*=numerator
                        den*=denominator
            except:
                pass
    #Return product of denominator in lowest common term
    return den/gcd(num, den)

print(fractions())
