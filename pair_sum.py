"""
    Given a list of positive integers nums and an
    int target,
    return indices of the two numbers such that they
    add up to a target - 30.

Conditions:

    You will pick exactly 2 numbers.
    You cannot pick the same element twice.
    If you have muliple pairs, select the pair with the
    largest number.

Example 1:

Input: nums = [1, 10, 25, 35, 60], target = 90
Output: [2, 3]
Explanation:
nums[2] + nums[3] = 25 + 35 = 60 = 90 - 30

Example 2:

Input: nums = [20, 50, 40, 25, 30, 10], target = 90
Output: [1, 5]
Explanation:
nums[0] + nums[2] = 20 + 40 = 60 = 90 - 30
nums[1] + nums[5] = 50 + 10 = 60 = 90 - 30
You should return the pair with the largest number.

"""

from typing import List


def pair_prob(arr: List[int], target: int):
    # actual value
    target -= 30

    complement_map = {}
    final_list = []

    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in complement_map:
            if complement_map[complement] > any(final_list) or i > any(final_list):
                final_list.clear()
                final_list.extend([complement_map[complement], i])
        else:
            complement_map[arr[i]] = i

    return final_list


if __name__ == "__main__":
    arr = [20, 50, 40, 25, 30, 10]
    target = 90

    print(pair_prob(arr, target))  # Output 1, 5

    arr = [1, 10, 25, 35, 60]
    target = 90
    print(pair_prob(arr, target))  # Output 2, 3
