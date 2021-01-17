"""
Search Suggestions System

Given an array of strings products and a string searchWord. We want
to design a system that suggests at most three product names from
products after each character of searchWord is typed. Suggested products
should have common prefix with the searchWord. If there are more than three
products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed. 

 

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]

Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]


Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]


Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]


Example 4:

Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]
 

Constraints:

1 <= products.length <= 1000
There are no repeated elements in products.
1 <= Σ products[i].length <= 2 * 10^4
All characters of products[i] are lower-case English letters.
1 <= searchWord.length <= 1000
All characters of searchWord are lower-case English letters.
"""

from collections import deque
from typing import List


class TrieNode:
    def __init__(self, key: str = ""):
        self.key = key
        self.edges = {}
        self.is_word = ""


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str) -> None:
        root = self.root

        for char in key:
            if char in root.edges:
                root = root.edges[char]
            else:
                node = TrieNode(char)
                root.edges[char] = node
                root = node

        root.is_word = key

    def search(self, word: str) -> List[str]:
        if not word:
            return []

        return_list = []

        root = self.root

        # serch first instance of matching letter
        for char in word:
            if char in root.edges:
                root = root.edges[char]
            else:
                return []

        queue = deque([root])

        # if the keyword is a word itself, add it
        if root.is_word:
            return_list.append(root.is_word)

        # do a bfs to search relevant words and add it
        while queue:
            node = queue.pop()

            for k, v in node.edges.items():
                queue.append(v)
                if v.is_word:
                    return_list.append(v.is_word)

        return_list.sort()
        return return_list[:3]


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        obj_trie = Trie()

        for product in products:
            obj_trie.insert(product)

        res = []

        for i in range(len(searchWord)):
            res.append(obj_trie.search(searchWord[:i + 1]))

        return res


if __name__ == "__main__":
    obj = Solution()

    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord = "mouse"
    output = [
        ["mobile", "moneypot", "monitor"],
        ["mobile", "moneypot", "monitor"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"]
    ]

    actual = obj.suggestedProducts(products, searchWord)

    print(actual)
    assert actual.sort() == output.sort()

    products = ["havana"]
    searchWord = "tatiana"
    output = [[], [], [], [], [], [], []]

    actual = obj.suggestedProducts(products, searchWord)

    print(actual)
    assert actual.sort() == output.sort()
