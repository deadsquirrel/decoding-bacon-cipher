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
    s = ''
    # create list of tuples with key_value_structure = key_letter_of_alphabet
    key_v = [(ALPHABET[n], KEY[n:(n + 5)]) for n in range(len(ALPHABET))]

    newl = ['a' if j.islower() else 'b'
            for j in inp
            if j != " "]

    newstr = ''.join(newl)
    counter = len(newl)
    while counter > 0:
        word = newstr[0:5]
        for k, v in key_v:
            if v == word:
                s += k
        newstr = newstr[5:]
        counter = counter - 5
    print s
