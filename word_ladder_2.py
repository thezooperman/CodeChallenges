"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
from typing import List
from collections import deque, defaultdict
import string
import math


class Vertex:
    def __init__(self, key: str):
        self.neighbours = list()
        self.distance = -1
        self.key = key

    def add_neighbour(self, vertex: str, distance: int):
        if vertex not in self.neighbours:
            self.neighbours.append(vertex)
            self.distance = distance
            self.neighbours.sort()
 
    def __str__(self):
        return "Node:{}\n,Distance:{}\n,Neighbours:{}".format(self.key, self.distance, self.neighbours)


class Solution:
    def get_neighbours(self, word_list: set, word: str) -> List[str]:
        neighbours = []

        # get one letter different neighbours from the word list
        for i in range(len(word)):
            for char in string.ascii_lowercase:
                new_word = word[:i] + char + word[i + 1:]
                if (new_word in word_list) and word != new_word:
                    neighbours.append(new_word)

        return neighbours

    def show(self, graph):
        for node in graph:
            node = graph[node]
            print("Node:{}, Distance:{}".format(node.key, node.distance))
            print("Neighbours:\n")
            for nbr in node.neighbours:
                print("Node:{}, Distance:{}, Neighbours:{}".format(
                    nbr.key, nbr.distance, nbr.neighbours))

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        return_list = []
        word_store = set(wordList)
        if beginWord not in word_store:
            word_store.add(beginWord)

        # build graph
        graph = defaultdict(set)

        for word in word_store:
            if word not in graph:
                graph[word] = Vertex(word)

            for ng in self.get_neighbours(word_store, word):
                node = graph[ng]

                if not node:
                    node = Vertex(ng)
                    graph[ng] = node

                graph[word].neighbours.append(node)

        # bfs to calculate shortest path distance
        distance = -1
        queue = deque()
        queue.append(graph[beginWord])

        while queue:
            queue_size = len(queue)

            while queue_size:
                cur_node = queue.pop()
                if cur_node.distance != -1:
                    queue_size -= 1
                    continue

                cur_node.distance = distance + 1
                for nbr in cur_node.neighbours:
                    if nbr.distance == -1:
                        queue.appendleft(nbr)

                queue_size -= 1
            # increment the distance per level
            distance += 1

        # self.show(graph)

        # get shortest path via dfs
        min_dist = math.inf
        stack = deque()
        stack.append((graph[beginWord], [],))

        while stack or len(stack) > 0:
            node, chain = stack.pop()
            if node.key == endWord:
                min_dist = min(min_dist, len(chain) + 1)
                return_list.append((*chain, node.key))
            else:
                for nbr in node.neighbours:
                    if nbr.distance > node.distance:
                        stack.append((nbr, [*chain, node.key]))

        return [list(item) for item in return_list if len(item) == min_dist]


if __name__ == "__main__":
    obj = Solution()

    begin, end = "hit", "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    expected = [
        ["hit", "hot", "dot", "dog", "cog"],
        ["hit", "hot", "lot", "log", "cog"]
    ]

    actual = obj.findLadders(begin, end, wordList)
    # print(*actual)

    assert expected.sort() == actual.sort(), "Actual returned values - {0}".format(actual)

    begin = "hit"
    end = "cog"
    wordList = ["hot","dot","dog","lot","log"]

    expected = []

    actual = obj.findLadders(begin, end, wordList)
    # print(*actual)

    assert expected.sort() == actual.sort(), "Actual returned values - {0}".format(actual)
