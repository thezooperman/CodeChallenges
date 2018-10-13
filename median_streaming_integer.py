#!/usr/bin/env python3
'''
Given a streaming set of infinite integer variable,
find the median of those variables, at any given point
in time.

O(n) = n log(n)
'''

import heapq


class StreamingInteger():
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.count = 0

    def insert(self, num):
        if self.count % 2 is 0:
            heapq.heappush(self.max_heap, num * -1)
            self.count += 1
            if len(self.min_heap) == 0:
                return
            if (self.max_heap[0] * -1) > self.min_heap[0]:
                # pop from max_heap and insert into min_heap
                to_min = -1 * heapq.heappop(self.max_heap)
                # pop from min_heap and insert into max_heap
                to_max = -1 * heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, to_max)
                heapq.heappush(self.min_heap, to_min)
        else:
            to_min = -1 * heapq.heappushpop(self.max_heap, -1 * num)
            heapq.heappush(self.min_heap, to_min)
            self.count += 1

    def get_median(self):
        if self.count % 2 == 0:
            return (-1 * self.max_heap[0] + self.min_heap[0]) / 2.0
        return float(-1 * self.max_heap[0])


if __name__ == '__main__':
    arr = [_ for _ in range(1, 11)]
    stream = StreamingInteger()
    for elem in arr:
        stream.insert(elem)
        print(stream.get_median())
