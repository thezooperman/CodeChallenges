"""
  Given a 2D board and a word, find if the word exists in the grid.
  The word can be constructed from letters of sequentially adjacent cell,
  where "adjacent" cells are those horizontally or vertically neighboring.
  The same letter cell may not be used more than once.

  Example:

    board =
    [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]

    Given word = "ABCCED", return true.
    Given word = "SEE", return true.
    Given word = "ABCB", return false.

   Constraints:

    board and word consists only of lowercase and uppercase English letters.
    0 <= board.length <= 200
    0 <= board[i].length <= 200
    0 <= word.length <= 10^3
"""
from typing import List


class Solution:
    directions = {(0, 1), (-1, 0), (1, 0), (0, -1)}

    def _is_valid_cell(self, row: int, col: int, board: List[List[str]]) -> bool:
        return 0 <= row < len(board) and 0 <= col < len(board[0])

    def _get_cell(self, row: int, col: int, board: List[List[str]]) -> str:
        if self._is_valid_cell(row, col, board):
            return board[row][col]
        return ""

    def _search_helper(self, board: List[List[str]], visited: List[List[bool]], row: int, col: int, word: str,
                       index: int, result=[]):
        # return if characters do not match
        cell_val = self._get_cell(row, col, board)
        if cell_val != word[index] or visited[row][col]:
            return False

        # if not visited[row][col]:
        visited[row][col] = True
        # result.append(cell_val)

        # check if word matches
        # if index == len(word) - 1:
        #     temp_str = "".join(result)
        #     return temp_str == word

        for (x, y) in self.directions:
            newr, newc = row + x, col + y
            if self._is_valid_cell(newr, newc, board) and not visited[newr][newc]:
                if self._search_helper(board, visited, newr, newc, word, index + 1, result):
                    return True

        result.pop()
        visited[row][col] = False
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False] * len(board[0]) for _ in range(len(board))]

        # all occurrences
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if self._search_helper(board, visited, row, col, word, 0):
                        return True
        return False


if __name__ == "__main__":
    grid = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    obj = Solution()
    search_word = "ABCB"
    print(obj.exist(board=grid, word=search_word))

    search_word = "ABCCED"
    print(obj.exist(board=grid, word=search_word))

    search_word = "SEE"
    print(obj.exist(board=grid, word=search_word))
