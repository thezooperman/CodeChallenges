# maximum_subsequence_product.py
'''
seq = [1,51,3,1,100,199,3]
'''

from numpy import prod


""" def maxsubseq(seq, result=[]):
    for s in seq:
        if result is None or len(result) == 0:
            result.append(s)
        elif s > result[-1] and prod(result) * s > prod(result):
            result.append(s)
    return result, prod(result) """


""" def maxsubseq(seq, result):
    for idx, s in enumerate(seq):
        if result is None or len(result) == 0:
            result.append(s)
        elif s >= result[-1]:  # and prod(result) * s > prod(result):
            result.append(s)
            return maxsubseq(seq[idx + 1:], result)
        else:
            return maxsubseq(seq[idx + 1:], result)
    return result, prod(result)
 """


def maxsubseq(seq, result):
    for idx, s in enumerate(seq):
        for idy, n in range(0, idx):
            if result is None or len(result) == 0:
                result.append(s)
            elif s >= result[-1]:  # and prod(result) * s > prod(result):
                result.append(s)
                return maxsubseq(seq[idx + 1:], result)
            else:
                return maxsubseq(seq[idx + 1:], result)
    return result, prod(result)


print(maxsubseq([1, 51, 3, 1, 100, 199, 3], []))
print(maxsubseq([10, 22, 9, 33, 21, 50, 41, 60], []))
print(maxsubseq([10, 9, 2, 5, 3, 7, 101, 18], []))  # [2, 3, 7, 101]
