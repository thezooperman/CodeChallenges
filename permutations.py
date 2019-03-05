# !/usr/bin/env python 3

def basic_permutation(string, index):
    '''
        Prints the permutation of all characters
        in input string.
        Prints non-unique elements also
        O(n) = n * n!
    '''
    if index == len(string):
        print(*string, sep=' ')
        return
    j=index
    while j < len(string):
        string[index], string[j] = string[j], string[index]
        basic_permutation(string, index + 1)
        string[index], string[j] = string[j], string[index]
        j+=1

basic_permutation(list('madam'), 0)
