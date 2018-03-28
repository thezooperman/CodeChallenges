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
    for i in range(length):
        for j in range(i + 1, length):
            if text[i] == text[j]:
                counter += 2
        print(counter)


print(longest_palindrome_sequnce('madam'))
