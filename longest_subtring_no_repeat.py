#!/usr/bin/env python3

'''
Given a string, find the length of the longest substring without
repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence
and not a substring.
'''


class Solution:
    ''' Runtime: O(n)
    Works on the principle of window [i, j)
    where i = fixed, j = exapnding range, unless it encoutners
    a duplicate. From there extend the sliding window'''

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(s) == 1:
            return 1
        i = j = ans = 0
        uniq = set()
        n = len(s)
        while j < n and i < n:
            if s[j] not in uniq:
                uniq.add(s[j])
                j += 1
                if ans < (j - i):
                    ans = j - i
            else:
                uniq.remove(s[i])
                i += 1
        return ans


if __name__ == '__main__':
    input_arr = ['abcabcbb', 'bbbbb', 'pwwkew']
    sol = Solution()
    for string in input_arr:
        print(sol.lengthOfLongestSubstring(string))
