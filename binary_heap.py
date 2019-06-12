#!/usr/bin/env python3

'''
Binary Heap implementation
Build Heap - O(n)
Heapify - O(log n)
'''


class BinaryHeap:
    def __init__(self, arr=[]):
        self.heap = arr or []
        self.size = len(arr) or 0

    def get_size(self):
        return self.size

    def getParentIndex(self, i):
        return (i - 1) // 2

    def getParent(self, i):
        return self.heap[self.getParentIndex(i)]

    def hasParent(self, i):
        return self.getParentIndex(i) >= 0

    def getLeftChildIndex(self, i):
        return 2 * i + 1

    def getLeftChild(self, i):
        return self.heap[self.getLeftChildIndex(i)]

    def hasLeftChild(self, i):
        return self.getLeftChildIndex(i) < self.size

    def getRightChildIndex(self, i):
        return 2 * i + 2

    def getRightChild(self, i):
        return self.heap[self.getRightChildIndex(i)]

    def hasRightChild(self, i):
        return self.getRightChildIndex(i) < self.size

    def heapifyup(self, i):
        while self.hasParent(i) and self.heap[i] > self.getParent(i):
            self.heap[i], self.heap[self.getParentIndex(i)] =\
                self.getParent(i), self.heap[i]
            i = self.getParentIndex(i)

    def heapifydown(self, i=0):
        while self.hasLeftChild(i):
            largest = i
            if self.hasLeftChild(i) and self.getLeftChild(i) >\
                    self.heap[largest]:
                largest = self.getLeftChildIndex(i)
            if self.hasRightChild(i) and self.getRightChild(i) >\
                    self.heap[largest]:
                largest = self.getRightChildIndex(i)
            if largest is not i:
                self.heap[i], self.heap[largest] = self.heap[largest],\
                    self.heap[i]
            i = self.getLeftChildIndex(largest)

    def build_max_heap(self, arr):
        # for i in range(self.size // 2 - 1, -1, -1):
        #     self.heapifydown(i)
        for elem in arr:
            self.add(elem)

    def extract(self):
        item = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.heap.pop()
        self.size -= 1
        self.heapifydown()
        return item

    def add(self, num):
        self.heap.append(num)
        self.size += 1
        self.heapifyup(self.size - 1)

    def print_heap(self):
        print(self.heap)

    def sort(self):
        while self.size > 1:
            self.heap[0], self.heap[self.size - 1] =\
                self.heap[self.size - 1], self.heap[0]
            self.size -= 1
            self.heapifydown(0)


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    heap = BinaryHeap()
    # heap.build_max_heap(arr)
    from random import randrange
    from datetime import timedelta
    from timeit import default_timer as timer
    s = timer()
    print('Generating random intergers...')
    # nos = [randrange(0, n + 1) for n in range(30 ** 6)]
    nos = set(randrange(0, n + 1) for n in range(10 ** 6))
    print(f'Integeres generated in :{timedelta(seconds=timer() - s)}')
    s = timer()
    print(f'Building heap of size : {len(nos)}')
    heap.build_max_heap(nos)
    # heap.print_heap()
    nos.clear()
    del nos
    heap.sort()
    # heap.print_heap()
    print(f'Heap op completed in :{timedelta(seconds=timer() - s)}')
