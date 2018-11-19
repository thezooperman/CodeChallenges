'''
Find the maximum element in an array which is
first increasing and then decreasing
Given an array of integers which is initially
increasing and then decreasing, find the
maximum value in the array.

Examples :

Input: arr[] = {8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1}
Output: 500

Input: arr[] = {1, 3, 50, 10, 9, 7, 6}
Output: 50

Corner case (No decreasing part)
Input: arr[] = {10, 20, 30, 40, 50}
Output: 50

Corner case (No increasing part)
Input: arr[] = {120, 100, 80, 20, 0}
Output: 120
'''


def find_maximum(arr):
    low, high = 0, len(arr) - 1

    #find max
    while low <= high:
        pass

    while low <= high:
        if high - low == 1:
            return arr[low]
        mid = (low + high) // 2
        if arr[mid] > arr[high]:
            high = mid
        else:
            low = mid
    return arr[high]


if __name__ == '__main__':
    arr = [
        [120, 100, 80, 20, 0],
        [8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1],
        [10, 20, 30, 40, 50],
        [1, 3, 50, 10, 9, 7, 6]
    ]
    [print(find_maximum(n)) for n in arr]
