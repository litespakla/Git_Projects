'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text
file containing over five-thousand first names, begin by sorting it
into alphabetical order. Then working out the alphabetical value for
each name, multiply this value by its alphabetical position in the list
to obtain a name score.

For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

#Get total of all the name scores in  a list of names
def name_scores(name_list):
    ans=0
    count=1
    for name in sorted(name_list):
        for l in name:
            ans+=count*(ord(l) - ord('A') + 1)
        count+=1
    return ans

#Name of file that contains the names
name='p022_names.txt'

#Opens file
file= open(name, 'r')

#List of names in the file
names=[]

#Create a list with names
for line in file:
    row=line.split(',')
    for n in row:
        names.append(n.replace('"', ''))

print(name_scores(names))
