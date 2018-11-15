#!/usr/bin/env python3
'''
Given an array of 0s, 1s, and 2s, sort
the array in ascending order
'''

def sort_fn(arr):
    s, m, e = 0, 0, len(arr) - 1
    while m <= e:
        if arr[m] == 0:
            arr[s], arr[m] = arr[m], arr[s]
            m += 1
            s += 1
        elif arr[m] == 1:
            m += 1
        else:
            arr[m], arr[e] = arr[e], arr[m]
            e -= 1
    return arr

if __name__ == '__main__':
    arr = list(map(int, input().strip().split(' ')))
    print(*sort_fn(arr))
