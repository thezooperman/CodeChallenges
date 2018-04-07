'''
This module lists all the basic Binary Tree/Binary
Search Tree interview questions
'''

from collections import deque
import sys

MAX_INT = sys.maxsize
MIN_INT = -sys.maxsize


class Node:
    '''Class to define a Binary Tree Node'''

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    '''Binary Search Tree'''

    def __init__(self):
        self.root = None

    def setRoot(self, data):
        '''Add the root of BST
           Args:
                data - value, preferably int value, to store in
                BST root node
        '''
        self.root = Node(data)

    def insert(self, data):
        '''Insert data into BST
           Args:
                data - value, preferably int value to store in
                BST node
                If data is less than root, traverse left until right
                node is found to insert, else follow same logic on right
                tree
        '''
        if self.root is not None:
            if data < self.root.data:
                if self.root.left is None:
                    self.root.left = Node(data)
                else:
                    pass
        else:
            self.setRoot(data)

    def printKDistanceRecursive(self, root, k):
        '''Print all nodes at Kth distance from root - Recursive'''
        if root is None:
            return
        if k == 0:
            print(root.data, end=' ')
        else:
            self.printKDistanceRecursive(root.left, k - 1)
            self.printKDistanceRecursive(root.right, k - 1)

    def printKDistantIterative(self, root, k):
        '''Print all nodes at Kth distance from root'''
        if root is None:
            print(0)
            return
        q = deque()
        q.append(root)
        childQ = deque()
        while q:
            node = q.pop()
            if node.left is not None:
                childQ.appendleft(node.left)
            if node.right is not None:
                childQ.appendleft(node.right)
            if len(q) == 0:
                k -= 1
                if k == 0:
                    [print(val.data, end=' ') for val in reversed(childQ)]
                    print()
                q, childQ = childQ, deque()

    def isBST(self, root):
        '''Given a Binary Tree, determine if the
           Tree is a BST'''
        return self.isBSTHelper(root, MIN_INT, MAX_INT)

    def isBSTHelper(self, node, int_min, int_max):
        '''Helper function for IsBST'''
        if node is None:
            return True
        if node.data < int_min or node.data > int_max:
            return False
        return self.isBSTHelper(node.left, int_min, node.data)\
            and self.isBSTHelper(node.right, node.data, int_max)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(8)
    bst = BST()
    bst.printKDistantIterative(root, 1)
    bst.printKDistantIterative(root, 2)
    bst.printKDistanceRecursive(root, 1)
    print()
    bst.printKDistanceRecursive(root, 2)
    print()
    root = None
    root = Node(10)
    root.left = Node(7)
    root.left.right = Node(11)
    root.right = Node(39)
    print(bst.isBST(root))


if __name__ == "__main__":
    main()
