'''
This module lists all the basic Binary Tree/Binary
Search Tree interview questions
'''

from collections import deque, defaultdict, OrderedDict
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
            node = q.popleft()
            if node.left is not None:
                childQ.append(node.left)
            if node.right is not None:
                childQ.append(node.right)
            if len(q) == 0:
                k -= 1
                if k == 0:
                    [print(val.data, end=' ') for val in childQ]
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

    def rootToLeafSum(self, node, target_sum):
        '''Function to check if root to leaf nodes
            adds up to match the target sum'''
        path = deque()
        result = self.rootToLeafSumHelper(node, target_sum, path)
        return result, path

    def rootToLeafSumHelper(self, root, target_sum, path):
        '''Helper to root to leaf sum'''
        if root is None:
            return False
        if root.left is None and root.right is None:
            if target_sum == root.data:
                path.append(root.data)
                return True
            else:
                return False
        if self.rootToLeafSumHelper(root.left, target_sum - root.data, path):
            path.append(root.data)
            return True
        if self.rootToLeafSumHelper(root.right, target_sum - root.data, path):
            path.append(root.data)
            return True
        return False

    def sumTree(self, root):
        '''Returns if the sum of the nodes if left sub tree
            and right sub tree equals the root node'''
        if root is None:
            return 0
        if (root.left is None and root.right is None):
            return root.data
        left_sum = right_sum = 0
        left_sum = self.getSum(root.left)
        right_sum = self.getSum(root.right)
        return root.data == left_sum + right_sum

    def getSum(self, node):
        '''Helper method to get the sum of the tree'''
        if node is None:
            return 0
        return self.getSum(node.left) + node.data + self.getSum(node.right)

    def sumTreeOptimized(self, node):
        '''Value at each non-leaf node is sum of its left
        and right sub-trees. Use this trick to optimize  post-order Tree
        traversal into O(n)'''
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return node.data
        left_sum = right_sum = 0
        left_sum = self.sumTreeOptimized(node.left)
        right_sum = self.sumTreeOptimized(node.right)
        return 2 * node.data if node.data == left_sum + right_sum else MIN_INT

    def verticalTraversal(self, root):
        '''Print a Vertical Traversal of Tree View'''
        hashMap = defaultdict(list)
        self.verticalTraversalHelper(root, 0, hashMap)
        sortedSet = OrderedDict(sorted(hashMap.items()))
        {print(*v) for v in sortedSet.values()}
        return

    def verticalTraversalHelper(self, root, distance, hashMap):
        '''Helper function for a Vertical Tree Traversal'''
        if root is None:
            return
        hashMap.setdefault(distance, hashMap[distance].append(root.data))
        self.verticalTraversalHelper(root.left, distance - 1, hashMap)
        self.verticalTraversalHelper(root.right, distance + 1, hashMap)

    def verticalTreeSum(self, root):
        '''Given a Binary Tree, print the vertical
           sum of its nodes'''
        hashMap = defaultdict(list)
        self.verticalTreeSumHelper(root, 0, hashMap)
        sortedSet = OrderedDict(sorted(hashMap.items()))
        {print(sum(v)) for v in sortedSet.values()}
        return

    def verticalTreeSumHelper(self, root, distance, hashMap):
        '''Helper function for Vertical Tree Sum'''
        if root is None:
            return
        hashMap.setdefault(distance, hashMap[distance].append(root.data))
        self.verticalTreeSumHelper(root.left, distance - 1, hashMap)
        self.verticalTreeSumHelper(root.right, distance + 1, hashMap)

    def widthOfBinaryTree(self, root):
        '''Given a Binary Tree, find the maximum width
            of the tree'''
        if root is None:
            return
        q = deque()
        q.append(root)
        max_width = MIN_INT
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            cur_width = len(q)
            max_width = max(cur_width, max_width)
        print('Max Width of Binary Tree:', max_width)
        return

    def lowestCommonAncestor(self, root, node1, node2):
        '''Given two nodes in a Binary Tree, find their lowest
            common ancestor in O(n) time
        '''
        if root is None:
            return None

        if root.data == node1 or root.data == node2:
            return root.data

        left_tree = self.lowestCommonAncestor(root.left, node1, node2)
        right_tree = self.lowestCommonAncestor(root.right, node1, node2)

        if left_tree and right_tree:
            return root.data

        return left_tree if left_tree else right_tree

    def distanceOfNodeFromRoot(self, root, node):
        '''Given a Binary Tree, find the distance
            of the node from the root. The distance of the node
            is measured by the number of edges between the root and
            the node'''
        if root.data == node:
            return 0
        s = deque()
        s.append(root)
        distance = 0
        while s:
            n = s.pop()
            if len(s) == 0:
                distance = 1  # reset distance from root again
            if n.data == node:
                return distance - 1
            distance += 1
            if n.right:
                s.append(n.right)
            if n.left:
                s.append(n.left)
        return -1

    def distanceBetweenTwoNodes(self, root, node1, node2):
        '''Given a Binary Tree, find the distance between
            the two nodes in the tree. Distance between the
            nodes is a sum or count of the number of edges
            between the nodes'''
        if root is None:
            return 0
        get_node1_distance = self.distanceOfNodeFromRoot(root, node1)
        if get_node1_distance == -1:
            return -1
        get_node2_distance = self.distanceOfNodeFromRoot(root, node2)
        if get_node2_distance == -1:
            return -1
        lca_node1_node2 = self.lowestCommonAncestor(root, node1, node2)
        distance_lca_root = self.distanceOfNodeFromRoot(root, lca_node1_node2)
        return (get_node1_distance + get_node2_distance) -\
               (2 * distance_lca_root)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(8)
    bst = BST()
    # bst.printKDistantIterative(root, 1)
    print('Kth Distance Iterative:')
    bst.printKDistantIterative(root, 2)
    print('Kth Distance Recursive:')
    bst.printKDistanceRecursive(root, 1)

    # bst.printKDistanceRecursive(root, 2)
    print()
    print('-'*20)
    root = Node(10)
    root.left = Node(7)
    root.left.right = Node(11)
    root.right = Node(39)
    print('Is Binary Search Tree:', bst.isBST(root))
    print('-'*20)

    root = Node(10)
    root.left = Node(8)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right = Node(2)
    root.right.left = Node(2)
    print('Root to Leaf Sum:', end='')
    result, path = bst.rootToLeafSum(root, 21)
    if result:
        # print(result, end=' ')
        [print(val, end=' ') for val in path]
        print()
    else:
        print(result)
    print('-'*20)

    root = Node(44)
    root.left = Node(9)
    root.right = Node(13)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print('Is Sum Tree == ', bst.sumTree(root))
    print('Is Optimized Sum Tree == ', True if
          bst.sumTreeOptimized(root) != MIN_INT else MIN_INT)

    print('-'*20)
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.right = Node(6)
    root.right.left = Node(5)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
    print('Vertical Tree Traversal:')
    bst.verticalTraversal(root)

    print('-' * 20)
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print('Vertical Tree Sum:')
    bst.verticalTreeSum(root)

    print('-' * 20)
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)
    root.right.right = Node(8)
    root.right.right.left = Node(6)
    root.right.right.right = Node(7)
    bst.widthOfBinaryTree(root)

    print('-' * 20)
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    # root.left.right = NOde(5)
    root.right = Node(3)
    root.right.left = Node(6)
    # root.right.right = Node(7)
    print('LCA(2,6) =',
          bst.lowestCommonAncestor(root, 2, 6))

    print('-' * 20)
    root = Node(5)
    root.left = Node(10)
    root.left.left = Node(20)
    root.left.right = Node(25)
    root.left.right.right = Node(45)
    root.right = Node(15)
    print('Distance of 45 from Root(5):', bst.distanceOfNodeFromRoot(root, 45))

    print('-' * 20)
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)
    root.right.left = Node(6)
    root.right.left.right = Node(8)
    root.right.right = Node(7)
    print('Node Dist(8, 5):', bst.distanceBetweenTwoNodes(root, 5, 8))
    print('Node Dist(2, 4):', bst.distanceBetweenTwoNodes(root, 2, 4))

    print('-' * 20)


if __name__ == "__main__":
    main()
