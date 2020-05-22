from typing import List


class Solution:
    def row_sum(self, sub_grid: List[List[int]]):
        return sum(sub_grid[0]) == sum(sub_grid[1]) == sum(sub_grid[2])

    def col_sum(self, sub_grid: List[List[int]]):
        cols = [0 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                cols[i] += sub_grid[3 - j - 1][i]
        return all(x == cols[0] for x in cols)

    def diag_sum(self, sub_grid: List[List[int]]):
        left = right = 0
        for i in range(3):
            left += sub_grid[i][i]
            right += sub_grid[i][3 - i - 1]

        return left == right

    def unique_items(self, sub_grid: List[List[int]]):
        unique_nos = {i for i in range(1, 10)}
        return unique_nos == set(sub_grid[0] + sub_grid[1] + sub_grid[2])

    def dumb_validations(self, sub_grid: List[List[int]]):
        return self.row_sum(sub_grid) and self.col_sum(sub_grid) and \
               self.diag_sum(sub_grid) and self.unique_items(sub_grid)

    def print_grid(self, arr):
        print('-' * 6)
        for i in range(3):
            for j in range(3):
                print(arr[i][j], end=' ')
            print(flush=True)
        print('-' * 6)

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n = len(grid)

        grid_count = 0

        for row in range(2, n):
            for col in range(2, len(grid[0])):
                sub_grid = [grid[r][col - 2: col + 1] for r in range(row - 2, row + 1)]
                # self.print_grid(sub_grid)
                if self.dumb_validations(sub_grid):
                    grid_count += 1

        return grid_count


if __name__ == '__main__':
    obj = Solution()
    matrix = [
        [3, 2, 9, 2, 7],
        [6, 1, 8, 4, 2],
        [7, 5, 3, 2, 7],
        [2, 9, 4, 9, 6],
        [4, 3, 8, 2, 5]
    ]

    print(obj.numMagicSquaresInside(grid=matrix))

    matrix = [
        [4, 3, 8, 4],
        [9, 5, 1, 9],
        [2, 7, 6, 2]
    ]
    print(obj.numMagicSquaresInside(grid=matrix))
