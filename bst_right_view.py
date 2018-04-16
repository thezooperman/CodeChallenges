# bst_right_view.py
'''
Given a binary tree, imagine yourself standing
on the right side of it, return the values of
the nodes you can see ordered from top to bottom.
Example:
        1
       / \
      2   3
       \   \
        5   4
Output: 1->3->4

Example:
        1
       / \
      2   3
       \   \
        5   4
         \
          6
Output: 1->3->4->6
'''
from collections import deque


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class BST(object):
    def rightView(self, root):
        q = deque()
        q.append(root)
        childQ = deque()
        returnVal = [root.val]
        while q:
            node = q.popleft()
            if node.right:
                childQ.append(node.right)
            if node.left:
                childQ.append(node.left)
            if len(q) == 0:
                if len(childQ) > 0:
                    returnVal.append(childQ[0].val)
                q, childQ = childQ, deque()
        return returnVal

    def rightViewByLevel(self, root, level, maxlevel, returnVal):
        if root is None:
            return
        if maxlevel[0] <= level:
            returnVal.append(root.val)
            maxlevel[0] = level
        self.rightViewByLevel(root.right, level + 1, maxlevel, returnVal)
        self.rightViewByLevel(root.left, level, maxlevel, returnVal)


bst = BST()
'''
        1
       / \
      2   3
       \   \
        5   4
         \
          6
'''
root = Node(1)
root.left = Node(2)
root.left.right = Node(5)
root.left.right.right = Node(6)
root.right = Node(3)
root.right.right = Node(4)
print(*bst.rightView(root))

'''
        1
       / \
      2   3
       \   \
        5   4
'''
root = Node(1)
root.left = Node(2)
root.left.right = Node(5)
root.right = Node(3)
root.right.right = Node(4)
retVal = []
bst.rightViewByLevel(root, 0, [-1], retVal)
print(*retVal)
