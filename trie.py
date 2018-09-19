#!/usr/bin/env python3

import sys
from collections import deque


class TrieNode:
    def __init__(self):
        self.key = None  # key - a,b,c
        self.value = None  # value for the leaf node - 5
        self.edges = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, k, v):
        root = self.root
        last_char_index = None
        for index_char, char in enumerate(k):
            # the key already exists in the Trie,
            # move to next children
            if char in root.edges:
                root = root.edges[char]
            else:
                last_char_index = index_char
                break
        if last_char_index is not None:
            # key does not exist
            # create a new node and assign
            for char in k[last_char_index:]:
                root.edges[char] = TrieNode()
                root.edges[char].key = char
                root = root.edges[char]
        # assign the value to the terminating node
        root.value = v
        root.is_end = True

    def search(self, word):
        if word:
            root = self.root
            for char in word:
                if char in root.edges:
                    root = root.edges[char]
                else:
                    return -1
            if root.is_end:
                return root.value
            else:
                # search and compare terminating node in child
                max_value = -sys.maxsize
                store_childs = deque()
                for ch_k, ch_v in root.edges.items():
                    store_childs.append(ch_v)
                while store_childs:
                    node = store_childs.popleft()
                    if node.is_end:  # leaf node
                        if node.value > max_value:
                            max_value = node.value
                    for e_k, e_v in node.edges.items():
                        store_childs.append(e_v)
                return max_value
        return -1


if __name__ == '__main__':
    input_str = {'hackerearth': 10, 'hackerrank': 9,
                 'hackerahan': 99, 'blob': 22}
    trie = Trie()
    for k, v in input_str.items():
        trie.insert(k, v)
    search_word = 'hacker'
    print(trie.search(search_word))
