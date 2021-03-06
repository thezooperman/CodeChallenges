"""
question: MaxRewards
Input :
    a. NXN Grid
    b. SRC, DST tuples(example  (0,0) and (N-1,N-1))
    c. Instruction_set : Each cell can contain any one of the following values :
          1 -> Right
          2 -> Down
          3 -> Both right and down

Output :
    1. Total number of ways to reach from src to dst
    2. Max_Rewards

Code below :
——————————————————————
"""

import copy


class Output:
    def __init__(self, _tot=0, _reward=0):
        self.total_ways = _tot
        self.reward = _reward


def _print_matrix(matrix):
    print(flush=True)
    rows, cols = len(matrix), len(matrix[0]) + 2
    print('-' * cols)
    for row in range(rows):
        print(*matrix[row])
    print('-' * cols)


def _get_cell_value(matrix, row, col):
    if (0 <= row <= len(matrix) - 1) and (0 <= col <= len(matrix[0]) - 1):
        return matrix[row][col]
    return 0  # if out of bounds return 0


def _max_rewards_helper(matrix, row, col, start_pos: tuple, end_pos: tuple, output) -> Output:
    current_cell = _get_cell_value(matrix, row, col)  # get current cell value
    output.reward += current_cell  # update reward

    if row == end_pos[0] and col == end_pos[1]:  # has reached destination
        output.total_ways += 1  # update the total ways
        return output

    # make traversal decisions
    if current_cell == 1:  # traverse right
        new_row, new_col = row + 0, col + 1  # compute next cell value
        return _max_rewards_helper(matrix, new_row, new_col, start_pos, end_pos, output)
    elif current_cell == 2:  # traverse down
        new_row, new_col = row + 1, col + 0  # compute next cell value
        return _max_rewards_helper(matrix, new_row, new_col, start_pos, end_pos, output)
    elif current_cell == 3:  # traverse down and right
        current_output = copy.copy(output)
        new_row, new_col = row + 0, col + 1  # compute next cell value
        path_1_reward = _max_rewards_helper(matrix, new_row, new_col, start_pos, end_pos, output)  # right

        new_row, new_col = row + 1, col + 0  # compute next cell value
        path_2_reward = _max_rewards_helper(matrix, new_row, new_col, start_pos, end_pos, current_output)  # down

        # between the two paths in option 3 - pick the one with max reward
        output.reward = max(path_1_reward.reward, path_2_reward.reward)
        output.total_ways += max(path_1_reward.total_ways, path_2_reward.total_ways)
        return output
    return Output()  # edge cases - breached borders or did not reach target


def max_rewards(matrix, start_pos: tuple, end_pos: tuple) -> Output:
    rows, cols = len(matrix), len(matrix[0])
    result = Output()
    result = _max_rewards_helper(matrix, 0, 0, start_pos, end_pos, result)
    return result


if __name__ == '__main__':
    grid = [
        [1, 2, 1],
        [2, 3, 2],
        [3, 1, 2]
    ]
    start = (0, 0)
    end = (2, 2)
    out = max_rewards(grid, start, end)  # expected outcome : total ways: 2, max_rewards = 10
    assert out.total_ways == 2
    assert out.reward == 10
    _print_matrix(grid)
    print(f'Start Co-ord:{start}, End Co-ord:{end}')
    print(f'Total ways: {out.total_ways}, Max Reward: {out.reward}')

    grid = [
        [1, 1, 3, 2],
        [2, 1, 3, 2],
        [3, 2, 1, 3],
        [1, 1, 2, 3]
    ]
    start = (0, 0)
    end = (len(grid) - 1, len(grid[0]) - 1)
    _print_matrix(grid)
    out = max_rewards(grid, start, end)
    print(f'Start Co-ord:{start}, End Co-ord:{end}')
    print(f'Total ways: {out.total_ways}, Max Reward: {out.reward}')  # total ways: 3, max_rewards = 16
    assert out.total_ways == 3
    assert out.reward == 16

    grid = [
        [1, 1, 2, 2],
        [2, 1, 2, 2],
        [3, 2, 1, 1],
        [1, 1, 2, 3]
    ]
    start = (0, 0)
    end = (len(grid) - 1, len(grid[0]) - 1)
    _print_matrix(grid)
    out = max_rewards(grid, start, end)
    print(f'Start Co-ord:{start}, End Co-ord:{end}')
    print(f'Total ways: {out.total_ways}, Max Reward: {out.reward}')  # total ways: 0, max_rewards = 0
    assert out.total_ways == 0
    assert out.reward == 0
