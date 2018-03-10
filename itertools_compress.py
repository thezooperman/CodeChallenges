"""
You are given a string S. Suppose a character 'c' occurs
consecutively X times in the string. Replace these
consecutive occurrences of the character 'c' with (X,c) in the string.
"""


import itertools

string = input().strip()

[print('(%s, %s) ' % (len(list(cgen)), c), end='') for c, cgen in
    itertools.groupby(string)]
