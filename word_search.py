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

    def _search_helper(self, board: List[List[str]], visited: set, row: int, col: int, word: str):

        # return if characters do not match
        if not self._is_valid_cell(row, col, board) or \
                self._get_cell(row, col, board) != word[0]:
            return False

        if not word or len(word) == 1:
            return True

        visited.add((row, col))
        ans = False
        for (x, y) in self.directions:
            newr, newc = row + x, col + y
            if self._is_valid_cell(newr, newc, board) and (newr, newc) not in visited and not ans:
                ans |= self._search_helper(board, visited, newr, newc, word[1:])

        visited.remove((row, col))
        return ans

    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        # all occurrences
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if self._search_helper(board, visited, row, col, word):
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
    print(obj.exist(board=grid, word=search_word))  # False

    search_word = "ABCCED"
    print(obj.exist(board=grid, word=search_word))  # True

    search_word = "SEE"
    print(obj.exist(board=grid, word=search_word))  # True
