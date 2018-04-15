# max_sum_increasing_subsequence.py
'''
The Maximum Sum Increasing Subsequence problem is to
find the maximum sum subsequence of a given sequence
such that all elements of the subsequence are sorted
in increasing order.

Input:  [1, 101, 2, 3, 100, 4, 5]
Output: [1, 2, 3, 100]

Input: [10, 9, 2, 5, 3, 7, 101, 18]
Output: [2, 5, 7, 101]
'''


import sys


def maxSumSubsequence(arr, index, prev, cur_sum):
    if len(arr) - 1 == index:
        return cur_sum
    excl = incl = 0
    excl = maxSumSubsequence(arr, index + 1, prev, cur_sum)
    incl = cur_sum
    if arr[index] > prev:
        cur_sum += arr[index]
        incl = maxSumSubsequence(arr, index + 1,
                                 arr[index], cur_sum)
    return max(incl, excl)


arr = [1, 101, 2, 3, 100, 4, 5]
print(maxSumSubsequence(arr, 0, -sys.maxsize, 0))

arr = [10, 9, 2, 5, 3, 7, 101, 18]
print(maxSumSubsequence(arr, 0, -sys.maxsize, 0))
