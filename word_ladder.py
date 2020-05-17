import string
from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList = set(wordList)
        queue = deque([(beginWord, 1)])
        visited = set()

        while queue:
            edge, length = queue.popleft()

            if edge == endWord:
                return length

            for i in range(len(edge)):
                for char in string.ascii_lowercase:
                    new_word = edge[:i] + char + edge[i + 1:]
                    if new_word in wordList and new_word not in visited:
                        wordList.remove(new_word)
                        queue.append((new_word, length + 1))
                        visited.add(new_word)
        return 0


if __name__ == "__main__":
    obj = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(obj.ladderLength(beginWord, endWord, wordList))
