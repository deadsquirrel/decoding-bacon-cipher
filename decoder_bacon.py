'''
crypt message
Bacon's cipher
'''
import sys
inp = sys.argv[1]
key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
n = 0
k = 5
key_v = []
newl = []
s = str()
'''
create list of tuples with key_value_structure = key_letter_of_alphabet
'''
for i in alphabet:
    y = (i, key[n:k])
    key_v.append(y)
    n = n + 1
    k = k + 1

for j in inp:
    if j == " ":
        continue
    else:
        low = j.islower()
        if low == True:
            newl.append('a')
        else:
            newl.append('b')

newstr = ''.join(newl)
counter = len(newl)
while counter > 0:
    word = newstr[0:5]
    for k, v in key_v:
        if v == word:
            lit = k
            s = s + lit
    newstr = newstr[5:]
    counter = counter - 5
print s
