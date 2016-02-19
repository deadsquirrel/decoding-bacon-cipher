#!/usr/bin/env python

'''
crypt message
Bacon's cipher
'''

import argparse


KEY = 'aaaaabbbbbabbbaabbababbaaababaab'
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

if __name__ = '__main__':
    # parse command line arguments, show help etc.
    parser = argparse.ArgumentParser(description='Bacon cipher')
    parser.add_argument('message', help='Message to encode.')
    opts = parser.parse_args()

    # create list of tuples with key_value_structure = key_letter_of_alphabet
    key_v = [(ALPHABET[n], KEY[n:(n + 5)]) for n in range(len(ALPHABET))]

    newl = ['a' if j.islower() else 'b'
            for j in opts.message
            if j != " "]

    newstr = ''.join(newl)
    counter = len(newl)
    s = ''
    while counter > 0:
        for k, v in key_v:
            if v == newstr[0:5]:
                s += k
        newstr = newstr[5:]
        counter = counter - 5
    print s
