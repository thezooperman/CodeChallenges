# longest_palindrome_subsequence.py

'''
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.
Input: "AABCDEBAZ"

Output: ABCBA or ABDBA or ABEBA
'''


def longest_palindrome_sequnce(text):
    '''
    Use DP to scan and find the largest
    non-contiguous palindrome
    Run time complexity: O(n^2)
    '''
    i = j = 0
    dp = [[0 for _ in range(len(text))] for _ in range(len(text))]
    for i in range(len(text)):
        dp[i][i] = 1
    length = len(text)
    for i in range(length):
            pass


print(longest_palindrome_sequnce('AABCDEBAZ'))
