from collections import deque


def update_grid(rows, columns, matrix):
    """
        Given a grid of cells, which has value 0 or 1
        1 -> updated cell, 0-> need to be updated
        a cell's neighbour can be updated -> left, right, up and down, not diagonal
        find minimum number of days to update all the cells
        in a tower
        rows: number of rows
        columns: number of columns
        grid:
            [[0, 1, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 1],
            [1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1]]
    """
    min_days = 0
    updated_server = False
    tobe_updated = set()
    iteration = 0
    while True:
        iteration += 1
        for row in range(rows):
            for col in range(columns):
                if matrix[row][col] == 0:
                    # left
                    if (col - 1) >= 0 and matrix[row][col - 1] == 1:
                        tobe_updated.add((row, col))
                        # grid[row][col] = 1
                        updated_server = True
                    # right
                    if (col + 1) < columns and matrix[row][col + 1] == 1:
                        tobe_updated.add((row, col))
                        # grid[row][col] = 1
                        updated_server = True
                    # up
                    if (row - 1) >= 0 and matrix[row - 1][col] == 1:
                        tobe_updated.add((row, col))
                        # grid[row][col] = 1
                        updated_server = True
                    # down
                    if (row + 1) < rows and matrix[row + 1][col] == 1:
                        tobe_updated.add((row, col))
                        # grid[row][col] = 1
                        updated_server = True
            if (row + 1) == rows and (col + 1) == columns:
                if updated_server is True:
                    min_days += 1
                for v in tobe_updated:
                    r, c = v
                    matrix[r][c] = 1
                tobe_updated.clear()
                if updated_server is False:
                    print(f'grid: {matrix} iteration:{iteration}')
                    return min_days
                updated_server = False
    return min_days

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
    # print(f'Total hours:', update_grid(4, 6, grid))

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
