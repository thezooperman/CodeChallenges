"""
Trapping Rain Water

Given an array arr[] of N non-negative integers representing height of blocks at index i
as Ai where the width of each block is 1. Compute how much water can be trapped in 
between blocks after raining.
Structure is like below:
|  |
|_|
We can trap 2 units of water in the middle gap.

Input:
The first line of input contains an integer T denoting the number of test cases.
The description of T test cases follows. Each test case contains an integer N
denoting the size of the array, followed by N space separated numbers to be stored in array.

Output:
Output the total unit of water trapped in between the blocks.

Constraints:
1 <= T <= 100
3 <= N <= 107
0 <= Ai <= 108

Example:
Input:
2
4
7 4 0 9
3
6 9 9

Output:
10
0

Explanation:
Testcase 1: Water trapped by block of height 4 is 3 units,
block of height 0 is 7 units. So, total unit of water trapped is 10 units.
"""

from typing import List
from collections import deque


COLUMN_WIDTH = 1


def maxWater(height: List[int], size: int) -> int:
    water_count = 0
    stack = deque()

    for i in range(size):
        while len(stack) > 0 and height[stack[-1]] < height[i]:
            prev_height = height[stack.pop()]

            # safety net - no need to access stack anymore
            if len(stack) < 1:
                break

            # get the distance between the left and right bounds
            distance = i - stack[-1] - 1
            min_height = min(
                height[i], height[stack[-1]]) - prev_height

            water_count += distance * min_height * COLUMN_WIDTH

        stack.append(i)

    return water_count


def driver():
    # arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    # expected_output = 6

    arr = [3, 0, 2, 0, 4]
    expected_output = 7

    actual_output = maxWater(arr, len(arr))

    assert actual_output == expected_output, f"Incorrect computation. Actual Output - {actual_output}"


driver()
