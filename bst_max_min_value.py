import sys

class Node(object):
    def __init__(self, data):
        self.key = data
        self.left = self.right = None

class Bst(object):
    def __init__(self, root = None):
        self.root = root

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return self.root
        return self._insert(self.root, data)
    
    def _insert(self, node, data):
         if node is None:
            return Node(data)

         if data <= node.key:
             if node.left is None:
                node.left = self._insert(node.left, data)
                return node.left
             else:
                return self._insert(node.left, data)
         else:
             if node.right is None:
                node.right = self._insert(node.right, data)
                return node.right
             else:
                return self._insert(node.right, data)

    def kthlargest(self, k):
        if self.root is None:
            raise TypeError('Root node is not defined')
        count = [0]
        self._kth_largest_util(k, self.root, count)

    def _kth_largest_util(self, k, node, count = []):
        if node is None or count[0] >= k:
            return 0
        self._kth_largest_util(k, node.right, count)
        count[0] += 1
        if count[0] == k:
            print(node.key)
        self._kth_largest_util(k, node.left, count)

    def get_max(self, node):
        if node is None:
            return -sys.maxsize
        if node.left is None and node.right is None:
            return node.key
        right_max = self.get_max(node.right)
        left_max = self.get_max(node.left)
        return max(left_max, right_max, node.key)

    def get_min(self, node):
        if node is None:
            return sys.maxsize
        if node.left is None and node.right is None:
            return node.key
        left_min = self.get_min(node.left)
        right_min = self.get_min(node.right)
        return min(left_min, right_min, node.key)

if __name__ == '__main__':
    root = Bst()
    root.insert(10)
    root.insert(15)
    root.insert(12)
    root.insert(25)
    root.insert(22)
    root.insert(32)
    print(root.get_max(root.root))
    print(root.get_min(root.root))
    root.kthlargest(2)
