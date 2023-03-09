'''
The nth term of the sequence of triangle numbers is given by
tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding
to its alphabetical position and adding these values we form
a word value. For example, the word value for SKY is
19 + 11 + 25 = 55 = t10. If the word value is a triangle number
then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'),
a 16K text file containing nearly two-thousand common English words,
how many are triangle words?
'''

#Get total of all the name scores in  a list of names
def triangular_words(word_list):
    triangular_n=[int((n+1)*n/2) for  n in range(1, 20)]
    print(triangular_n)
    count=0
    for word in word_list:
        value=0
        for l in word:
            value+=(ord(l) - ord('A') + 1)
        if value in triangular_n:
            count+=1
    return count

#Name of file that contains the names
name='p042_words.txt'

#Opens file
file= open(name, 'r')

#List of names in the file
words=[]

#Create a list with names
for line in file:
    row=line.split(',')
    for n in row:
        words.append(n.replace('"', ''))

print(triangular_words(words))
