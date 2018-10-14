#!/usr/bin/env python3


class Heap:
    def __init__(self):
        self.data = []
        self.size = 0

    def heapifyDown(self, i):
        largest = i
        leftIndex = 2 * i + 1
        rightIndex = 2 * i + 2
        if leftIndex < self.size and\
                self.data[leftIndex] > self.data[largest]:
            largest = leftIndex
        if rightIndex < self.size and\
                self.data[rightIndex] > self.data[largest]:
            largest = rightIndex
        if largest is not i:
            self.data[i], self.data[largest] =\
                self.data[largest], self.data[i]
            self.heapifyDown(largest)

    def heapifyUp(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.data[i] > self.data[parent]:
            self.data[i], self.data[parent] = self.data[parent], self.data[i]
            parent = (parent - 1) // 2

    def extract(self):
        max_data = self.data[0]
        self.data[0] = self.data[self.size - 1]
        self.size -= 1
        self.data.pop()
        self.heapifyDown(0)
        return max_data

    def insert(self, num):
        self.data.append(num)
        self.size += 1
        self.heapifyUp(len(self.data) - 1)

    def display(self):
        for i in range(self.size):
            print(self.data[i], end=' ')
        print(flush=True)


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    heap = Heap()
    for elem in arr:
        heap.insert(elem)
    heap.display()
    while heap.data:
        print(heap.extract())
