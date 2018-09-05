# LRU Cache implementation
# Put/Get operation O(n) = 1


class Node(object):
    '''Double Linked List Node Class'''

    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.left = None
        self.right = None


class LRUCache(object):
    '''LRU Cache implemented
        with Doubly linked list and HashMap
    '''

    def __init__(self, capacity):
        self.CAPACITY = capacity
        self.start = self.end = None
        self.CACHE = {}

    def get(self, key):
        if key in self.CACHE:
            node = self.CACHE.get(key)
            self.remove_node(node)
            self.add_at_top(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.CACHE:
            node = self.CACHE.get(key)
            node.value = value
            self.remove_node(node)
            self.add_at_top(node)
        else:
            node = Node(key, value)
            if len(self.CACHE) >= self.CAPACITY:
                self.CACHE.pop(self.end.key)
                self.remove_node(self.end)
                self.add_at_top(node)
            else:
                self.add_at_top(node)
            self.CACHE.setdefault(key, node)

    def add_at_top(self, node):
        node.right = self.start
        node.left = None
        if self.start:
            self.start.left = node
        self.start = node
        if self.end is None:
            self.end = self.start

    def remove_node(self, node):
        if node.left is not None:
            node.left.right = node.right
        else:
            self.start = node.right
        if node.right is not None:
            node.right.left = node.left
        else:
            self.end = node.left


if __name__ == '__main__':
    # cache = LRUCache(4)
    # cache.put(1, 1)
    # cache.put(10, 15)
    # cache.put(15, 10)
    # cache.put(10, 16)
    # print(cache.get(10))
    # cache.put(12, 15)
    # cache.put(18, 10)
    # cache.put(13, 16)
    # print(cache.get(1))
    # print(cache.get(15))

    # cache = LRUCache(1)
    # cache.put(2, 1)
    # print(cache.get(2))
    # cache.put(3, 2)
    # print(cache.get(2))
    # print(cache.get(3))

    cache = LRUCache(2)
    cache.put(2, 1)
    cache.put(2, 2)
    print(cache.get(2))
    cache.put(1, 1)
    cache.put(4, 1)
    print(cache.get(2))
