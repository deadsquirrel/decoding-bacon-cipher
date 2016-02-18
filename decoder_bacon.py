#!/usr/bin/env python

'''
crypt message
Bacon's cipher
'''
import sys

KEY = 'aaaaabbbbbabbbaabbababbaaababaab'
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

if __name__ = '__main__':
    inp = sys.argv[1]
    n = 0
    key_v = []
    newl = []
    s = ''
    # create list of tuples with key_value_structure = key_letter_of_alphabet
    for i in ALPHABET:
        key_v.append((i, KEY[n:(n + 5)]))
        n += 1

    for j in inp:
        if j == " ":
            continue
        if j.islower():
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
