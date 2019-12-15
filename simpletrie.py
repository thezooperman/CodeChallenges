#!/usr/bin/env python3

from io import StringIO
from collections import deque


class Node:
    def __init__(self):
        self.nodes = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        crawl = self.root

        for idx, letter in enumerate(word):
            if letter not in crawl.nodes:
                crawl.nodes[letter] = Node()
                if idx == len(word) - 1:
                    crawl.nodes[letter].is_end = True
            crawl = crawl.nodes[letter]

    def get_all_prefix(self, prefix):
        returnVals = []
        crawl = self.root
        sb = StringIO()

        # run the length of the prefix
        for index, letter in enumerate(prefix):
            if letter in crawl.nodes:
                sb.write(letter)
                if crawl.nodes[letter].is_end:
                    returnVals.append(sb.getvalue())
                    sb = StringIO()
                    sb.write(prefix[:index + 1])
                crawl = crawl.nodes[letter]
            else:
                return returnVals

        # if prefix matches with any word, return
        if prefix in returnVals:
            return returnVals

        # traverse all the children from last reached node
        stack = deque(crawl.nodes.items())

        while stack:
            v, n = stack.pop()
            sb.write(v)
            if n.is_end:
                returnVals.append(sb.getvalue())
                sb = StringIO()
                if not n.nodes:
                    sb.write(prefix)
                else:
                    sb.write(returnVals[-1])
            if n.nodes:
                stack.extend(n.nodes.items())

        return returnVals


if __name__ == '__main__':
    t = Trie()
    # t.insert('go')
    t.insert('goa')
    t.insert('bag')
    t.insert('hawai')
    t.insert('gone')
    t.insert('baggit')
    t.insert('baggage')
    # t.insert('bag')
    t.insert('goal')
    print(t.get_all_prefix('ba'))
    print(t.get_all_prefix('go'))
