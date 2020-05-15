"""
Given a non-empty string s and a dictionary wordDict containing a
list of non-empty words, determine if s can be segmented into a
space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""


class Trie:
    __slots__ = ["nodes", "word"]

    def __init__(self):
        self.nodes = {}
        self.word = ""

    def insert(self, word) -> None:
        current = self

        for idx, letter in enumerate(word):
            index = ord(letter) - ord('a')
            if index not in current.nodes:
                current.nodes[index] = Trie()
            if idx == len(word) - 1:
                current.nodes[index].word = word
            else:
                current = current.nodes[index]

    def search(self, word) -> bool:
        current = self

        for idx, char in enumerate(word):
            index = ord(char) - ord('a')
            if index in current.nodes:
                if idx != len(word) - 1:
                    current = current.nodes[index]
            else:
                return False
        return current.nodes[index].word == word


class Solution:
    def word_dfs(self, trie: Trie, word: str, wordDict: List[str]) -> bool:
        if len(word) == 0:
            return True

        for i in range(1, len(word) + 1):
            if trie.search(word[:i]) and self.word_dfs(trie, word[i:], wordDict):
                return True
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = Trie()

        for word in wordDict:
            root.insert(word)

        return self.word_dfs(root, s, wordDict)


if __name__ == "__main__":
    obj = Solution()
    s = "leetcode"
    word_dict = ["leet", "code"]
    expected_output = True

    assert expected_output == obj.wordBreak(s, word_dict)
