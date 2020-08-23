"""
    Maximum of all subarrays of size k 
    Given an array A and an integer K. Find the maximum for each and every contiguous subarray of size K.

    Example:
    Input:
    2
    9 3
    1 2 3 1 4 5 2 3 6
    10 4
    8 5 10 7 9 4 15 12 90 13

    Output:
    3 3 4 5 5 5 6
    10 10 10 15 15 90 90
"""

from collections import deque
from typing import List, Iterable


def max_subarray(array: List[int], k: int) -> Iterable[int]:
    # assume - deque front contains largest element
    # deque back contains smallest elelents
    if not array:
        raise ValueError("Input array cannot be empty")

    if not k:
        raise ValueError("Window K cannot be empty")

    dq = deque()

    # store the largest element in window
    # at front
    for i in range(k):
        while len(dq) > 0 and array[i] >= array[dq[0]]:
            dq.popleft()
        dq.appendleft(i)

    for j in range(k, len(array)):
        yield array[dq[-1]]

        # cleanup elements from queue back
        # which do not fit in window K
        while len(dq) > 0 and dq[-1] <= (j - k):
            dq.pop()

        # check if deque[0] has the largest element
        # if not, clear out
        while len(dq) > 0 and array[j] >= array[dq[0]]:
            dq.popleft()

        dq.appendleft(j)

    yield array[dq[-1]]
    del dq


if __name__ == "__main__":
    # arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
    # k = 3
    k = 4
    print(' '.join(str(x) for x in max_subarray(arr, k)))
