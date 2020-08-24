from collections import deque

# Binary tree node 
class Node: 
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = self.right = None

def traverse(root: Node):
    queue = deque([root])

    ltr = True
    childQ = deque()

    while queue:
        node = queue.pop()
        print(node.data, sep=' ', end=' ')

        if ltr:
            if node.left:
                childQ.append(node.left)
            if node.right:
                childQ.append(node.right)
        else:
            if node.right:
                childQ.append(node.right)
            if node.left:
                childQ.append(node.left)
        
        if len(queue) == 0:
            ltr = not ltr
            queue, childQ = childQ, deque()

    # while queue:
    #     node = queue.popleft()

    #     print(node.data, sep=' ', end=' ')
    #     if node.right:
    #         queue.append(node.right)
    #     if node.left:
    #         queue.append(node.left)
    #     if level != 1 and level % 2 != 0:
    #         queue.reverse()
    #     level += 1

def driver():
    # Driver program to check above function 
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(7) 
    root.left.right = Node(6) 
    root.right.left = Node(5) 
    root.right.right = Node(4) 
    print("Zigzag Order traversal of binary tree is")

    traverse(root)

if __name__ == "__main__":
    driver()