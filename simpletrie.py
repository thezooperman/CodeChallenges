#!/usr/bin/env python3

from collections import deque
from timeit import default_timer as timer
from datetime import timedelta


class Node:
    __slots__ = ['nodes', 'is_leaf']

    def __init__(self):
        self.nodes = {}
        self.is_leaf = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        crawl = self.root

        for idx, letter in enumerate(word):
            if letter not in crawl.nodes:
                crawl.nodes[letter] = Node()
                if idx == len(word) - 1:
                    crawl.nodes[letter].is_leaf = True
            crawl = crawl.nodes[letter]

    def _get_all_prefix_recursive_util(self, root, result):
        if root.is_leaf:
            yield result

        for k, v in root.nodes.items():
            result.append(k)
            yield from self._get_all_prefix_recursive_util(v, result)
            result.pop()  # remove the node, after it has been processed

    def get_all_prefix_recursive(self, prefix):
        crawl = self.root
        result = []

        for letter in prefix:
            if letter in crawl.nodes:
                crawl = crawl.nodes[letter]
                result.append(letter)
            else:
                return []

        result_set = sorted(
            [''.join(r) for r in self._get_all_prefix_recursive_util(crawl, result)])
        return result_set

    def get_all_prefix(self, prefix):
        returnVals = []
        sb = []
        crawl = self.root

        # run the length of the prefix
        for index, letter in enumerate(prefix):
            if letter in crawl.nodes:
                sb.append(letter)
                crawl = crawl.nodes[letter]
            else:
                return returnVals

        # if prefix matches with any word completely, return
        # if prefix in returnVals:
        #     return returnVals

        if len(sb) > 0:
            returnVals.append([''.join(_ for _ in sb)])

        # traverse all the children from last matched node
        stack = deque()

        # populate the path for DFS
        for k, v in crawl.nodes.items():
            l = sb.copy()
            l.append(k)
            stack.append((l, v))

        # clear the compute path so far
        # as it is already stored in the stack trace
        sb.clear()

        # walk the DFS
        while stack:
            pre, node = stack.pop()
            if len(pre) >= len(sb):
                # if the previous path is retained
                # before branching, select previous path
                # e.g. - bagg --> baggi(t)/ bagga(ge)
                sb = pre
            else:
                sb.extend(pre)
            if node.is_leaf:
                returnVals.append([''.join(r) for r in sb])
                # if the tree does not terminate on leaf node
                # do not clear the string builder list
                if not node.nodes:
                    sb.clear()
            for k, v in node.nodes.items():
                # store the computed string, at the branching point
                # e.g. - goa --> goa(l)/goa(n)
                if len(node.nodes) > 1:
                    # shallow copy the pre-computed string
                    x = sb.copy()
                    x.append(k)
                    stack.append((x, v))
                else:
                    stack.append((k, v))

        returnVals = sorted(''.join(r) for r in returnVals)
        return returnVals


if __name__ == '__main__':
    t = Trie()
    # t.insert('go')

    start = timer()
    file_path = 'Civilization_of_Illiteracy.txt'
    # 'democracy_in_america.txt'

    # lines = (line for line in open(file_path, encoding='utf-8'))
    # split_line = (word.lower() for line in lines for word in line.strip().split(None))
    # for word in split_line:
    #     t.insert(word)

    with open(file_path, 'r', encoding='utf-8') as f:
        [t.insert(word.lower())
         for line in f for word in line.strip().split(' ')]
        # for line in f:
        #     for word in line.strip().split(' '):
        #         t.insert(word)

    print(f'Trie build completed in {timer() - start}')

    # t.insert('goa')
    # t.insert('bag')
    # t.insert('hawai')
    # t.insert('gone')
    # t.insert('baggit')
    # t.insert('baggage')
    # t.insert('bag')
    # t.insert('goal')
    # print('Iterative Trie prefix for string: ba', t.get_all_prefix('ba'))
    # print('Iterative Trie prefix for string: go', t.get_all_prefix('go'))
    # print('Recursive Trie prefix for string: go', t.get_all_prefix_recursive('go'))
    # print('Recursive Trie prefix for string: ba', t.get_all_prefix_recursive('ba'))

    start = timer()
    search_text = 'the'
    print(
        f'\nIterative Searching for "{search_text}" in time {timedelta(timer() - start)}', t.get_all_prefix(search_text))
    start = timer()
    print(f'\nRecursive Searching for "{search_text}" in time {timedelta(timer() - start)}',
          t.get_all_prefix_recursive(search_text))
