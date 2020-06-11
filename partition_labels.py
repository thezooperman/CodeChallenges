"""
    Partition Labels
    
    A string S of lowercase English letters is given. 
    We want to partition this string into as many parts
    as possible so that each letter appears in at most one
    part, and return a list of integers representing the
    size of these parts.

 

    Example 1:

    Input: S = "ababcbacadefegdehijhklij"
    Output: [9,7,8]

    Explanation:
        The partition is "ababcbaca", "defegde", "hijhklij".
    This is a partition so that each letter appears in at most one part.
    A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
 

    Note:

    S will have length in range [1, 500].
    S will consist of lowercase English letters ('a' to 'z') only.
"""


from typing import List


def partitionLabels(S: str) -> List[int]:
    if not S:
        return []

    # start with [i, j)
    # where i = initial anchor
    # j means- it can be extended to include
    # elements within the partition
    # when no elements are found within the window i,j
    # that is in the rest S[j: ],
    # add S[i: j - i + 1] to output
    j = 0
    start = -1
    out = []
    for i in range(len(S)):
        idx = S[i+1:].rfind(S[i])
        if i == j and idx == -1:
            out.append(j-start)
            start = i
            j = i + 1
        else:
            j = max(j, idx + i + 1)

    return out


input_str = "ababcbacadefegdehijhklij"
output = [9, 7, 8]

print(partitionLabels(input_str))


input_str = ["a", "b", "c", "a", "b", "c", "a", "e", "f", "g", "h", "e"]
output = [7, 5]

print(partitionLabels("".join(input_str)))


input_str = ["a", "b", "c"]
output = [1, 1, 1]

print(partitionLabels("".join(input_str)))


input_str = ["z", "z", "c", "d", "e", "z", "a", "c", "f", "c", "h", "i"]
output = [10, 1, 1]

print(partitionLabels("".join(input_str)))
