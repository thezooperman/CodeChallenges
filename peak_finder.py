# peak_finder.py


def peak_finder(nums):
    '''Find the peak in an array.
       In-case of multiple peaks, pick any one.
       Return the index of the peak item.
       :type nums: List[int]
       :rtype: int
    '''
    if len(nums) == 1:
            return 0

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if mid - 1 >= 0 and nums[mid] < nums[mid - 1]:
            right = mid - 1
        elif mid + 1 < len(nums) and nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            return mid


print('Peak finder index: %d' % peak_finder([1, 2, 3, 4, 5]))
