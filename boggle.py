from typing import List


class TrieNode:
    def __init__(self):
        self.key = None  # key - a,b,c
        self.edges = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, k: str):
        root = self.root

        for char in k:
            if char in root.edges:
                root = root.edges[char]
            else:
                node = TrieNode()
                node.key = char
                root.edges[char] = node
                root = node

        root.is_end = True

    def search(self, word: str):
        root = self.root
        for char in word:
            if char in root.edges:
                root = root.edges[char]
            else:
                return -1
        return root.key


directions = {(0, -1), (0, 1), (1, 0), (-1, 0),
              (-1, -1), (1, 1), (-1, 1), (1, -1)}


def is_safe(matrix, row, col, visited):
    return bool(0 <= row < len(matrix) and
                0 <= col < len(matrix[0]) and
                (row, col) not in visited)


def searchWord(matrix: List[List[int]], trie: TrieNode, tmp_str: str, row: int, col: int, visited: set, dictionary: set):
    if trie.is_end and tmp_str in dictionary:
        # print(tmp_str, sep=' ', end=' ')
        result.add(tmp_str)
        dictionary.remove(tmp_str.strip())
        return

    if is_safe(matrix, row, col, visited):
        visited.add((row, col))

        for k, v in trie.edges.items():
            for (x, y) in directions:
                nr, nc = row + x, col + y
                if is_safe(matrix, nr, nc, visited) and matrix[nr][nc] == k:
                    searchWord(matrix, v,
                               tmp_str + k, nr, nc, visited, dictionary)

        visited.remove((row, col))


result = set()


def driver():
    testCases = 1  # int(input().strip())
    for tc in range(testCases):
        x = 6  # 4  # int(input().strip())
        # set(input().strip().split(None))
        # dictionary = {"GEEKS", "FOR", "QUIZ", "GO"}
        dictionary = {'dfd', 'ded', 'fd', 'e', 'dec', 'df'}
        # dimension = input().strip().split(None)
        # n, m = 3, 3  # int(dimension[0]),int(dimension[1])
        n, m = 4, 2
        # board_values = ['G', 'I', 'Z', 'U', 'E', 'K',
        #                 'Q', 'S', 'E']  # input().strip().split(None)

        board_values = ['f', 'f', 'd', 'e', 'f', 'b', 'b', 'e']

        visited = set()
        trie = Trie()

        # build trie
        for word in dictionary:
            trie.insert(word)

        # build matrix
        matrix = [[''] * m for _ in range(n)]
        row = start = 0
        end = m
        while row < n:
            matrix[row] = board_values[start: end]
            start, end = end, end + m
            row += 1

        # print(*matrix)
        # go through matrix for word
        visited = set()
        trie = Trie()

        # build trie
        for word in dictionary:
            trie.insert(word)

        # go through matrix for word
        visited = set()

        tmp_str = ''
        for row in range(n):
            for col in range(m):
                if matrix[row][col] in trie.root.edges:
                    tmp_str = tmp_str + matrix[row][col]
                    searchWord(
                        matrix, trie.root.edges[matrix[row][col]], tmp_str, row, col, visited, dictionary)
                    tmp_str = ''

        print(*sorted(result))
        result.clear()
        print(flush=True)


if __name__ == "__main__":
    driver()
