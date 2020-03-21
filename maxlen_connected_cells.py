#!/usr/bin/env python3

'''
    Problem: Find the maximum length of connected cells
        of 1s regions in the matrix
    grid:
       [
        [1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [0, 1, 0, 1, 1]
       ]
'''

'''
    # check left
    if array[x][y - 1] == 1:
        count[0] += 1
    # check right
    elif array[x][y + 1] == 1:
        count[0] += 1
    # check down
    elif array[x + 1][y] == 1:
        count[0] += 1
    # check up
    elif array[x - 1][y] == 1:
        count[0] += 1
    # check left-up diagonal
    elif array[x - 2][y - 1] == 1:
        count[0] += 1
    # check left-down diagonal
    elif array[x + 1][y + 1] == 1:
        count[0] += 1
    # check right-up diagonal
    elif array[x - 1][y + 1] == 1:
        count[0] += 1
    # check right-down diagonal
    elif array[x + 1][y - 1] == 1:
        count[0] += 1
'''


def _get_cell_value(array, x, y) -> int:
    if (x >= 0 and x <= len(array) - 1) and (y >= 0 and y <= len(array[0]) - 1):
        return array[x][y]
    return 0


def _maxlen_util(array, row, col, visited, count) -> int:
    if (row > len(array) - 1) or (col > len(array[0]) - 1):
        return
    # print(f'New Row: {row}, New Column: {col}')
    visited[row][col] = True
    directions = [(0, -1), (0, 1), (1, 0), (-1, 0),
                  (-1, -1), (1, 1), (-1, 1), (1, -1)]
    # increase the counter
    count[0] += 1
    for i in range(8):
        newr, newc = (row + directions[i][0]), (col + directions[i][1])
        val = _get_cell_value(array, newr, newc)
        if val == 1 and visited[newr][newc] == False:
            _maxlen_util(array, newr, newc, visited, count)


def max_region_len(array) -> int:
    row, col = len(array), len(array[0])
    visited = [[False] * col for _ in range(row)]
    result = 0
    for r in range(row):
        for c in range(col):
            if array[r][c] == 1:
                # re-init the counter
                count = [0]
                _maxlen_util(
                    array, r, c, visited, count)
                result = max(count[0], result)

    return result


if __name__ == '__main__':
    grid =\
        [
            [1, 1, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [0, 1, 0, 1, 1]
        ]
    print(max_region_len(grid))  # expected result = 5

    grid =\
        [
            [0, 0, 1, 1, 0],
            [1, 0, 1, 1, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1]
        ]
    print(max_region_len(grid))  # expected result = 6

    grid =\
        [
            [0, 0, 1, 1],
            [0, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]
        ]
    print(max_region_len(grid))  # expected result = 8
