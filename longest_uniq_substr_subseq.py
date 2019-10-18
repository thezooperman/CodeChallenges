#!/usr/bin/env python3

'''
Find the longest substring with k unique
characters in a given string.

Examples:

"aabbcc", k = 1
Max substring can be any one from {"aa" , "bb" , "cc"}.

"aabbcc", k = 2
Max substring can be any one from {"aabb" , "bbcc"}.

"aabbcc", k = 3
There are substrings with exactly 3 unique characters
{"aabbcc" , "abbcc" , "aabbc" , "abbc" }
Max is "aabbcc" with length 6.

"aaabbb", k = 3
There are only two unique characters, thus show error message.
'''

MAX_SIZE = 52


def longest_subsequence(string: str, k: int) -> tuple:
    count = [0] * MAX_SIZE
    unique = 0
    # check if total unique count is less than k
    for s in string:
        if count[ord(s) - ord('a')] == 0:
            unique += 1
        count[ord(s) - ord('a')] += 1
    if unique < k:
        return 'Minimum unique characters is less than k'
    # find unique subsequence
    count = [0] * MAX_SIZE
    cur_end = cur_start = 0
    win_max_size = 1

    count[ord(string[0]) - ord('a')] += 1

    for s in range(1, len(string)):
        count[ord(string[s]) - ord('a')] += 1
        # increase window end
        cur_end += 1

        # check if unique value exceeds k
        def isUniqueValid(count: list):
            val = 0
            for i in range(MAX_SIZE):
                if count[i] > 0:
                    val += 1
            return k >= val

        while not isUniqueValid(count):
            # if unique > k, reduce the left window
            count[ord(string[cur_start]) - ord('a')] -= 1
            cur_start += 1

        # compare max window state
        if (cur_end - cur_start + 1) > win_max_size:
            win_max_size = (cur_end - cur_start) + 1

    return win_max_size, string[cur_start:]


if __name__ == '__main__':
    print(longest_subsequence('AAbbCC', 1))
    print(longest_subsequence('aabbcc', 2))
    print(longest_subsequence('aabbcc', 3))
    print(longest_subsequence('aaabbb', 3))  # should show error
