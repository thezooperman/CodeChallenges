# minimum_rotated_sorted_array.py
'''
Complexity: O(log n)
Runs a binary search
'''


def minimum_rotated_sorted_array(nums):
    '''Pass'''
    low, high = 0, len(nums) - 1
    if nums[low] < nums[high]:  # sorted array
        return nums[0]
    while low <= high:
        if high - low == 1:
            return nums[high]
        m = low + high // 2
        if nums[m] > nums[high]:
            low = m
        else:
            high = m
    return nums[low]


print(minimum_rotated_sorted_array([5, 6, 1, 2, 3, 4]))
print(minimum_rotated_sorted_array([1, 2, 3, 4]))
print(minimum_rotated_sorted_array([1, 2]))
print(minimum_rotated_sorted_array([2, 1]))
print(minimum_rotated_sorted_array([2, 3, 1]))
print(minimum_rotated_sorted_array([3, 1, 2]))
print(minimum_rotated_sorted_array([3, 1, 1]))
