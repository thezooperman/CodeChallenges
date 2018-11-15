#!/usr/bin/env python3

'''
Reverse a list in-place
without using any additional space.
Total space complexity: O(1)
'''


def in_place_sort(arr):
    s, e = 0, len(arr) - 1
    while s < e:
        arr[s], arr[e] = arr[e], arr[s]
        s += 1
        e -= 1
    return arr


if __name__ == '__main__':
    arr = list(map(int, input().strip().split(' ')))
    print(*in_place_sort(arr))
