from collections import deque


"""
    	Given a grid of cells, which has value 0 or 1
        -1 -> updated cell, 0-> need to be updated
        a cell's neighbour can be updated -> left, right, up and down, not diagonal
        find minimum number of days to update all the cells
        in a tower
        rows: number of rows
        columns: number of columns
        grid:
            [[-2, 1, 0, 1, 0, 1],
            [-2, 0, 0, 1, 0, 1],
            [-1, 1, 0, 0, 0, 0],
            [-2, 0, 0, 0, 0, 1]]
"""

visited = set()
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def grid_update_helper(row, col, grid):
    min_count = 0
    queue = deque([(row, col)])

    old_visited = len(visited)

    while queue:
        row, col = queue.popleft()

        for (x, y) in directions:
            new_row, new_col = row + x, col + y
            if 0 <= new_row < len(grid) and \
                0 <= new_col < len(grid[0]) and \
                    grid[new_row][new_col] == 0 and \
            (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                queue.append((new_row, new_col))

    return 1


def grid_update(grid):
    min_days = 0
    visited.clear()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) not in visited and grid[row][col] == 0:
                visited.add((row, col))
                min_days += grid_update_helper(row, col, grid)

    return min_days


if __name__ == '__main__':
    # grid = [[0, 1, 0, 1, 0, 1],
    #         [0, 0, 0, 1, 0, 1],
    #         [1, 1, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 1]]
    # print(f'Total hours:', grid_update(grid))

    # grid = [
    #     [0, 1, 1, 0, 1],
    #     [0, 1, 0, 1, 0],
    #     [0, 0, 0, 0, 1],
    #     [0, 1, 0, 0, 0]
    # ]

    # print(grid_update(grid)) # output = 3

    grid = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 0, 1]
    ]
    print(grid_update(grid))  # output = 1
