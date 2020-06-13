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




from collections import deque
def _get_cell_value(array, x, y) -> int:
    if (0 <= x <= len(array) - 1) and (0 <= y <= len(array[0]) - 1):
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
    for (i, j) in directions:
        newr, newc = (row + i), (col + j)
        val = _get_cell_value(array, newr, newc)
        if val == 1 and visited[newr][newc] is False:
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


visited = set()


def other_fn_helper(array, row, col) -> int:
    directions = [(0, -1), (0, 1), (1, 0), (-1, 0),
                  (-1, -1), (1, 1), (-1, 1), (1, -1)]
    count = 0

    if array[row][col] == 1 and (row, col) not in visited:
        count += 1
        visited.add((row, col))
    queue = deque([(row, col)])

    while queue:
        row, col = queue.popleft()

        for (x, y) in directions:
            new_row, new_col = row + x, y + col
            if _get_cell_value(array, new_row, new_col) == 1 and (new_row, new_col) not in visited:
                count += 1
                # print(new_row, new_col)
                visited.add((new_row, new_col))
                queue.append((new_row, new_col))

    # print("count:", count)
    # print("-" * 5, flush=True)
    return count


def other_max_region(array):
    visited.clear()
    count = 0
    for row in range(len(array)):
        for col in range(len(array[0])):
            count = max(other_fn_helper(array, row, col), count)
    return count


if __name__ == '__main__':
    grid = \
        [
            [1, 1, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [0, 1, 0, 1, 1]
        ]
    # print(max_region_len(grid))  # expected result = 5

    print(other_max_region(grid))

    grid = \
        [
            [0, 0, 1, 1, 0],
            [1, 0, 1, 1, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1]
        ]
    # print(max_region_len(grid))  # expected result = 6
    print(other_max_region(grid))

    grid = \
        [
            [0, 0, 1, 1],
            [0, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]
        ]
    # print(max_region_len(grid))  # expected result = 8
    print(other_max_region(grid))