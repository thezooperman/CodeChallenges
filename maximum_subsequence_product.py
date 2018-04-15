# maximum_subsequence_product.py
'''
seq = [1,51,3,1,100,199,3]
'''

import sys

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


def maxsubseq(seq, i, prev, prod):
    if len(seq) == i:
        return prod
    incl = excl = 1
    excl = maxsubseq(seq, i + 1, prev, prod)
    incl = prod
    if seq[i] > prev:
        prod *= seq[i]
        incl = maxsubseq(seq, i + 1, seq[i], prod)
    return max(incl, excl)


print(maxsubseq([1, 51, 3, 1, 100, 199, 3], 0, -sys.maxsize, 1))
print(maxsubseq([10, 22, 9, 33, 21, 50, 41, 60], 0, -sys.maxsize, 1))
print(maxsubseq([10, 9, 2, 5, 3, 7, 101, 18], 0, -sys.maxsize, 1))
