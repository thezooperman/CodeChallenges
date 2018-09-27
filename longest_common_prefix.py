#!/usr/bin/env python3

'''
Write a function to find the longest common prefix string amongst an array
of strings.

If there is no common prefix, return an empty string "".
Runtime - O(m), where m is the length of the longest string
for search/insert operation in Trie
'''

from io import StringIO


class Node:
    def __init__(self):
        self.key = None
        self.edges = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, string):
        root = self.root
        for char in string:
            if char in root.edges:
                root = root.edges[char]
            else:
                node = Node()
                node.key = char
                root.edges[char] = node
                root = node
        root.is_end = True

    def longest_common_prefix(self, string):
        '''Traverse from root, for each string to match.
        Check these conditions for each character:
         - node is not last
         - char value is in node edge
         - length of node is 1
         '''
        sb = StringIO()
        root = self.root
        for char in string:
            if char in root.edges and len(root.edges) == 1 and not root.is_end:
                sb.write(char)
                root = root.edges[char]
            else:
                return sb.getvalue()
        return sb.getvalue()


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        trie = Trie()
        s = set()
        for str in strs:
            trie.insert(str)
        for str in strs:
            s.add(trie.longest_common_prefix(str))
        return ''.join(_ for _ in s)


if __name__ == '__main__':
    sol = Solution()
    input_arr = ["dog", "racecar", "car"]  # ["flower", "flow", "flight"]
    print(sol.longestCommonPrefix(input_arr))
