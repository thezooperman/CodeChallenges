#!/usr/bin/env python3

'''
Implement a Trie data structure
Worst Case Operation: O(m)
where m is length of the longest string
'''

from typing import List


class TrieNode:
    def __init__(self):
        self.key = None  # key - a,b,c
        self.value = 0  # value for the leaf node - 5
        self.edges = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, k: str, v: str):
        root = self.root

        for char in k:
            if char in root.edges:
                root = root.edges[char]
            else:
                node = TrieNode()
                node.key = char
                root.edges[char] = node
                root = node
            if root.value < v:
                root.value = v
        
        root.is_end = True

    def search(self, word: str):
        root = self.root
        for char in word:
            if char in root.edges:
                root = root.edges[char]
            else:
                return -1
        return root.value
    
    def _searchUtil(self, root: TrieNode, return_val: list):
        if root.is_end:
            yield return_val
        
        for k,v in root.edges.items():
            return_val.append(k)
            yield from self._searchUtil(v, return_val)
            return_val.pop()

    def search_all_values(self, word: str) -> List[str]:
        if not word or len(word) == 0:
            return ValueError("Search param cannot be empty")
        
        crawl = self.root
        result = []

        for letter in word:
            if letter in crawl.edges:
                result.append(letter)
                crawl = crawl.edges[letter]
            else:
                return []
        
        return_val = [''.join(r) for r in self._searchUtil(crawl, result)]

        return return_val
    
    def delete(self, word: str):
        if not word or len(word) == 0:
            return ValueError("Search param cannot be empty")
        
        crawl = self.root

        for letter in word:
            if letter in crawl.edges:
                crawl = crawl.edges[letter]
            else:
                raise ValueError('Word not found')



if __name__ == '__main__':
    input_str = {'hackerearth': 10, 'hackerrank': 9,
                 'hackerahan': 99, 'blob': 22}
    trie = Trie()
    # with open('trie_tc_12.txt') as fd:
    #     n, q = map(int, fd.readline().strip().split(' '))
    #     for line in fd:
    #         if n < 1:
    #             break
    #         tmp = line.split(' ')
    #         trie.insert(tmp[0], int(tmp[1]))
    #         n -= 1
    #     for line in fd:
    #         print(trie.search(line.strip()))
    for k, v in input_str.items():
        trie.insert(k, v)
    search_word = 'hacker'
    print(trie.search(search_word))
    print(trie.search_all_values('hack'))

