from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nrows = len(board)
        ncols = len(board[0])

        def backtrack(i, j, idx):
            char = board[i][j]
            if char != word[idx]:
                return False
            elif idx == len(word) - 1:
                return True

            board[i][j] = ''

            if i > 0 and backtrack(i - 1, j, idx + 1):
                return True
            if j > 0 and backtrack(i, j - 1, idx + 1):
                return True
            if i < nrows - 1 and backtrack(i + 1, j, idx + 1):
                return True
            if j < ncols - 1 and backtrack(i, j + 1, idx + 1):
                return True
            board[i][j] = char
            return False

        for i in range(nrows):
            for j in range(ncols):
                if backtrack(i, j, 0):
                    return True

        return False


obj = Solution()
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