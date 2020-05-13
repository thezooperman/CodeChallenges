"""
    Given a 2D board and a list of words from the dictionary, find
    all words in the board. Each word must be constructed from letters of
    sequentially adjacent cell, where "adjacent" cells are those horizontally
    or vertically neighboring.The same letter cell may not be used more
    than once in a word.

    Example:
    Input:
        board = [
                ['o', 'a', 'a', 'n'],
                ['e', 't', 'a', 'e'],
                ['i', 'h', 'k', 'r'],
                ['i', 'f', 'l', 'v']
            ]
    words = ["oath", "pea", "eat", "rain"]

    Output: ["eat", "oath"]

    Note:
        All inputs are consist of lowercase letters a - z.
        The values of words are distinct.
"""
from typing import List


class Trie:
    __slots__ = ["nodes", "word"]

    def __init__(self):
        self.nodes = {}
        self.word = ""

    def insert(self, word) -> None:
        current = self

        for idx, letter in enumerate(word):
            if letter not in current.nodes:
                current.nodes[letter] = Trie()
            if idx == len(word) - 1:
                current.nodes[letter].word = word
            else:
                current = current.nodes[letter]

    def search(self, word) -> bool:
        current = self

        for idx, char in enumerate(word):
            if char in current.nodes:
                if idx != len(word) - 1:
                    current = current.nodes[char]
            else:
                return False
        return current.nodes[char].word == word


class Solution:
    directions = {(0, 1), (-1, 0), (1, 0), (0, -1)}
    result = []
    root = Trie()

    def is_cell_valid(self, row: int, col: int, max_row: int, max_col: int) -> bool:
        return 0 <= row < max_row and 0 <= col < max_col

    def find_helper(self, board: List[List[str]], word: str, row: int, col: int, trie: Trie) -> str:
        current_char = board[row][col]

        if current_char not in trie.nodes:
            return False

        word += current_char
        if self.root.search(word):
            self.result.append(word)

        # replace current position
        board[row][col] = "!"

        ans = False
        # iterate over all possible directions
        for (x, y) in self.directions:
            newr, newc = row + x, col + y
            if self.is_cell_valid(newr, newc, len(board), len(board[0])) and \
                    board[newr][newc] != "!":
                ans |= self.find_helper(board, word, newr, newc, trie.nodes[current_char])

        # replace dummy var with actual, backtrack
        board[row][col] = current_char
        return ans

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        flag = False
        self.result.clear()
        for word in words:
            self.root.insert(word)
        head = self.root
        for row in range(len(board)):
            for col in range(len(board[0])):
                # if word[0] == board[row][col]:
                if self.find_helper(board, "", row, col, head):
                    flag = True
                    break
            if flag:
                flag = False
                break
        return self.result


obj = Solution()
matrix = [
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
]
word_list = ["oath", "pea", "eat", "rain"]

output = obj.findWords(matrix, word_list)  # Output: ["eat","oath"]
assert output.sort() == ["eat", "oath"].sort(), "Wrong values returned"

matrix = [
    ["a", "b"],
    ["c", "d"]
]

word_list = ["ab", "cb", "ad", "bd", "ac", "ca", "da", "bc", "db", "adcb", "dabc", "abb",
             "acb"]  # Output: ["ab","ac","bd","ca","db"]
output = obj.findWords(matrix, word_list)
assert output.sort() == ["ab", "ac", "bd", "ca", "db"].sort(), "Wrong values returned"

matrix = [
    ["a"]
]
word_list = ["ab"]  # Output: []
output = obj.findWords(matrix, word_list)
assert output.sort() == [].sort(), "Wrong values returned"
