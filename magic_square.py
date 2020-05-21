"""
A magic square of order n is an arrangement of n^2 numbers,
usually distinct integers, in a square, such that the n numbers
in all rows, all columns, and both diagonals sum to the same constant.
A magic square contains the integers from 1 to n^2.

The constant sum in every row, column and diagonal is called the magic
constant or magic sum, M. The magic constant of a normal magic square
depends only on n and has the following value:
M = n(n^2+1)/2

For normal magic squares of order n = 3, 4, 5, ...,
 the magic constants are: 15, 34, 65, 111, 175, 260, ...

Magic Square of size 3
-----------------------
  2   7   6
  9   5   1
  4   3   8
Sum in each row & each column = 3*(3^2+1)/2 = 15


Magic Square of size 5
----------------------
  9   3  22  16  15
  2  21  20  14   8
 25  19  13   7   1
 18  12   6   5  24
 11  10   4  23  17
Sum in each row & each column = 5*(5^2+1)/2 = 65
"""
from typing import List, Tuple


def next_position(row: int, col: int, n: int) -> Tuple[int, int]:
    # decrement row by 1, increment col by 1
    row = row - 1
    col = col + 1

    # row == -1, and col == n
    if (row == -1) and (col == n):
        return 0, n - 2

    # row == -1 or col == n
    if row == -1:
        row = n - 1
    if col == n:
        col = 0

    return row, col


def position_clash(row: int, col: int, grid: List[List[int]]) -> Tuple[int, int]:
    if grid[row][col]:
        row += 1
        col -= 2

    return row, col


def sum_magic_square(n: int) -> int:
    return n * (n ** 2 + 1) // 2


def print_matrix(grid: List[List[int]]) -> None:
    for i in range(len(grid)):
        for j in range(len(grid)):
            print(grid[i][j], end=' ')
        print(flush=True)


def magic_square(n: int) -> None:
    arr = [[False] * n for _ in range(n)]
    r, c = n // 2, n - 1
    arr[r][c] = 1
    for y in range(2, n * n + 1):
        row_pos, col_pos = next_position(r, c, n)
        row_pos, col_pos = position_clash(row_pos, col_pos, arr)
        arr[row_pos][col_pos] = y
        r, c = row_pos, col_pos
    print_matrix(arr)
    print(flush=True)
    sum_of_ms = sum_magic_square(n)
    print("Sum of magic square:", sum_of_ms)

    assert sum(arr[0]) == sum_of_ms


if __name__ == '__main__':
    magic_square(5)
