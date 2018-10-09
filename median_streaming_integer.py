import heapq


class StreamingInteger():
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def insert(self, num):
        len_max = len(self.max_heap)
        len_min = len(self.min_heap)
        if (len_max + len_min) % 2 is 0:
            heapq.heappush(self.max_heap, num * -1)
            if len_min == 0:
                return
            if (self.max_heap[0] * -1) > self.min_heap[0]:
                # pop from max_heap and insert into min_heap
                to_min = -1 * heapq.heappop(self.max_heap)
                # pop from min_heap and insert into max_heap
                to_max = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, to_max)
                heapq.heappush(self.min_heap, to_min)
        else:
            to_min = -1 * heapq.heappushpop(self.max_heap, -1 * num)
            heapq.heappush(self.min_heap, to_min)

    def get_median(self):
        if (len(self.max_heap) + len(self.min_heap)) % 2 == 0:
            return ((-1 * self.max_heap[0] + self.min_heap[0]) / 2)
        return -1 * self.max_heap[0]
