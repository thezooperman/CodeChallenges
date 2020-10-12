# longest_palindrome_substring.py

'''
Given a string s, find the longest palindromic substring in s.
'''


def longest_palindrome_sequnce(string):
    '''
    Run time complexity: O(n^2)
    '''
    maxLength = 1
    length = len(string)
    start = 0
    low = high = 0
    for i in range(0, length):
        low = i - 1
        high = i
        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1

        low = i - 1
        high = i + 1
        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1

    print(string[start: start + maxLength])


longest_palindrome_sequnce('AABCDEBAZ')
