#!/usr/bin/env python3
'''
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)

search(word) can search a literal word or a regular expression string
containing only letters a-z or .. A . means it can represent any one letter.

You may assume that all words are consist of lowercase letters a-z.
'''


class Node:
    def __init__(self):
        self.key = None
        self.edges = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        root = self.root
        for char in word:
            index = char  # self.char_to_index(char)
            if index in root.edges:
                root = root.edges[index]
            else:
                node = Node()
                index = char  # self.char_to_index(char)
                node.key = char
                root.edges[index] = node
                root = node
        root.is_end = True

    def search_util(self, root, word, index):
        if index == len(word):
            return root.is_end
        char = word[index]
        if char == '.':
            for k in root.edges:
                if k in root.edges and\
                        self.search_util(root.edges[k], word, index + 1):
                    return True
            return False
        else:
            if char in root.edges:
                return self.search_util(root.edges[char], word, index + 1)
            return False

    def search(self, word):
        """
        Returns if the word is in the data structure.
        A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not word or len(word) == 0:
            return False
        return self.search_util(self.root, word, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

if __name__ == '__main__':
    word_dict = WordDictionary()
    word_dict.addWord("bad")
    word_dict.addWord("dad")
    word_dict.addWord("mad")
    print(word_dict.search("pad"))  # -> false
    print(word_dict.search("bad"))  # -> true
    print(word_dict.search(".ad"))  # -> true
    print(word_dict.search("b.."))  # -> true
