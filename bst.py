'''
This module lists all the basic Binary Tree/Binary
Search Tree interview questions
'''


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
