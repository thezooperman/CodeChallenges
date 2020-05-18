"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

"""

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
