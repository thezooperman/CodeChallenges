# longest_palindrome_subsequence.py

'''
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.
Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
'''


def longest_palindrome_sequnce(text):
    length = len(text)
    counter = 0
    for i in range(length // 2):
        if text[i] != text[length - i - 1]:
            continue
        else:
            counter += 1
    return counter


print(longest_palindrome_sequnce('madam'))
