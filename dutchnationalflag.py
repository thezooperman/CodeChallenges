# dutchnationalflag.py


def sort012(arr):
    ''' Given an unsorted array of 0, 1 and 2's
        sort the array into 0, 1 and 2 in that order
        in O(n) time
    '''
    lo, hi, mid = 0, len(arr) - 1, 0
    while mid <= hi:
        if arr[mid] == 0:
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi -= 1
    return arr

arr = list(map(int, input().strip().split(' ')))
print(sort012(arr))

