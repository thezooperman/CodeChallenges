'''
Given an array of distinct integers. The task is to count all the
triplets such that sum of two elements equals the third element.
'''


def triplet(arr, n):
    result = 0
    arr.sort()
    d = set(arr)
    max_elem = arr[-1]
    for i in range(n - 1):
        for j in range(i + 1, n - 1):
            s = arr[i] + arr[j]
            if s > max_elem:
                break  # sum of numbers has crossed max element
            if s in d:
                result += 1
    return -1 if result == 0 else result


if __name__ == '__main__':
    print(triplet([1, 5, 3, 2], 4)) # Output: 2
    print(triplet([7, 2, 5, 4, 3, 6, 1, 9, 10, 12], 10))
    print(triplet([1, 3, 4, 15, 19], 5))
    print(triplet([3, 2, 7], 3)) # Output: -1
