"""
Given a m * n grid, where each cell is either 0 (empty) or 1 (obstacle).
In one step, you can move up, down, left or right from and to an empty cell.

Return the minimum number of steps to walk from the upper left corner (0, 0)
to the lower right corner (m-1, n-1) given that you can eliminate at most
k obstacles. If it is not possible to find such walk return -1.

 

Example 1:

Input: 
grid = 
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 
k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10. 
The shortest path with one obstacle elimination at position (3,2) is 6.
Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
 

Example 2:

Input: 
grid = 
[[0,1,1],
 [1,1,1],
 [1,0,0]], 
k = 1
Output: -1
Explanation: 
We need to eliminate at least two obstacles to find such a walk.
 

Constraints:

grid.length == m
grid[0].length == n
1 <= m, n <= 40
1 <= k <= m*n
grid[i][j] == 0 or 1
grid[0][0] == grid[m-1][n-1] == 0
"""

from typing import List


class Solution:
    directions = {(0, 1), (1, 0), (-1, 0), (0, -1)}
    cache = {}

    def is_valid_cell(self, row, col, max_row, max_col) -> bool:
        return 0 <= row < max_row and 0 <= col < max_col

    def dfs(self, row, col, k, grid):
        # print(row, col)
        # end condition
        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            return 0

        if (row, col, k) in self.cache:
            return self.cache[(row, col, k)]

        if grid[row][col] == -1:
            return -1

        if grid[row][col] == 1:
            # k limit exceeded
            if k <= 0:
                return -1
            grid[row][col] = 0
            path_1 = self.dfs(row, col, k - 1, grid)
            grid[row][col] = 1

            self.cache[(row, col, k)] = path_1
            return path_1
        else:
            ans = float('inf')
            grid[row][col] = -1
            for (x, y) in self.directions:
                newr, newc = row + x, col + y
                if self.is_valid_cell(newr, newc, len(grid), len(grid[0])):
                    path_2 = self.dfs(newr, newc, k, grid)
                    if path_2 != -1:
                        ans = min(path_2 + 1, ans)
            grid[row][col] = 0
            if ans == float('inf'):
                ans = -1

            self.cache[(row, col, k)] = ans
        return ans

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        self.cache.clear()
        return self.dfs(0, 0, k, grid)


if __name__ == "__main__":
    obj = Solution()

    matrix = [
        [0, 1, 1],
        [1, 1, 1],
        [1, 0, 0]
    ]
    k = 1
    expected_output = -1
    actual_output = obj.shortestPath(matrix, k)
    assert expected_output == actual_output, "Wrong output"

    matrix = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0],
        [0, 1, 1],
        [0, 0, 0]
    ]
    k = 1
    expected_output = 6
    actual_output = obj.shortestPath(matrix, k)
    assert expected_output == actual_output, "Wrong output"

    matrix = [
        [0, 1, 1],
        [1, 1, 1],
        [1, 0, 0]
    ]
    k = 1
    expected_output = -1
    actual_output = obj.shortestPath(matrix, k)
    assert expected_output == actual_output, "Wrong output"
