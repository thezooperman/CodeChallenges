# search_rotated_array.py


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or target is None:
            return -1
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if target >= nums[low] and target < nums[mid]:
                    high = mid - 1
                else:
                    low = low + 1
            else:
                if target > nums[mid] and target <= nums[high]:
                    low = mid + 1
                else:
                    high = high - 1
        return -1


call_method = Solution()
print(call_method.search([4, 5, 6, 7, 0, 1, 2], 4))
print(call_method.search([4, 5, 6, 7, 0, 1, 2], 0))
print(call_method.search([4, 5, 6, 7, 0, 1, 2], 7))
print(call_method.search([4, 5, 6, 7, 0, 1, 2], 2))
