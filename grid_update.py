def update_grid(rows, columns, grid):
    '''
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
    '''
    min_days = 0
    updatedServer = False
    tobe_updated = set()
    iteration = 0
    while True:
        iteration += 1
        for row in range(rows):
            for col in range(columns):
                if grid[row][col] == 0:
                    # left
                    if (col - 1) >= 0 and grid[row][col - 1] == 1:
                        tobe_updated.add((row, col))
                        # grid[row][col] = 1
                        updatedServer = True
                    # right
                    if (col + 1) < columns and grid[row][col + 1] == 1:
                        tobe_updated.add((row, col))
                        # grid[row][col] = 1
                        updatedServer = True
                    # up
                    if (row - 1) >= 0 and grid[row - 1][col] == 1:
                        tobe_updated.add((row, col))
                        # grid[row][col] = 1
                        updatedServer = True
                    # down
                    if (row + 1) < rows and grid[row + 1][col] == 1:
                        tobe_updated.add((row, col))
                        # grid[row][col] = 1
                        updatedServer = True
            if (row + 1) == rows and (col + 1) == columns:
                if updatedServer is True:
                    min_days += 1
                for v in tobe_updated:
                    r, c = v
                    grid[r][c] = 1
                tobe_updated.clear()
                if updatedServer is False:
                    print(f'grid: {grid} iteration:{iteration}')
                    return min_days
                updatedServer = False
    return min_days


if __name__ == '__main__':
    grid = [[0, 1, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 1],
            [1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1]]
    print(update_grid(4, 6, grid))
