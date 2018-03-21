def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if len(nums) == 0:
        return [-1, -1]

    ret = [-1, -1]
    if len(nums) == 0:
        return ret
    lower, upper = 0, len(nums) - 1

    while lower < upper:
        m = (lower + upper) // 2
        if nums[m] < target:
            lower = m + 1
        else:
            upper = m

    if nums[lower] != target:
        return ret
    else:
        ret[0] = lower
    upper = len(nums) - 1
    while lower < upper:
        m = (lower + upper) // 2 + 1
        if nums[m] > target:
            upper = m - 1
        else:
            lower = m
    ret[1] = upper
    return ret


print(searchRange([5, 7, 7, 8, 8, 10], 8))
print(searchRange([], 8))
print(searchRange([1], 1))
print(searchRange([1], 0))
