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

        while queue:
            size = len(queue)

            node = queue.pop()

            for k, v in node.edges.items():
                queue.append(v)
                if v.is_word:
                    return_list.append(v.is_word)
                size -= 1

        # return_list.sort()
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
    output = [[],[],[],[],[],[],[]]

    actual = obj.suggestedProducts(products, searchWord)

    print(actual)
    assert actual.sort() == output.sort()
