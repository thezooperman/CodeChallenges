# maximum_rotated_sorted_array.py
'''
Complexity: O(log n)
Runs a binary search
'''


def maximum_rotated_sorted_array(nums):
    '''Pass'''
    low, high = 0, len(nums) - 1
    if nums[low] < nums[high]:  # sorted array
        return nums[high]
    while low <= high:
        if high - low == 1:
            return nums[low]
        m = (low + high) // 2
        if nums[m] > nums[high]:
            low = m
        else:
            high = m
    return nums[high]


print(maximum_rotated_sorted_array([5, 6, 1, 2, 3, 4]))
print(maximum_rotated_sorted_array([1, 2, 3, 4]))
print(maximum_rotated_sorted_array([1, 2]))
print(maximum_rotated_sorted_array([2, 1]))
print(maximum_rotated_sorted_array([2, 3, 1]))
print(maximum_rotated_sorted_array([3, 1, 2]))
print(maximum_rotated_sorted_array([3, 1, 1]))
