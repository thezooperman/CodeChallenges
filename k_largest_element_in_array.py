# k_largest_element_in_array.py

'''
Write an efficient program for printing k
largest elements in an array. Elements in
array can be in any order.
Input: [1, 23, 12, 9, 30, 2, 50]
Output: [50, 30, 23]
k: 3
'''
import heapq


def getKLargestElement(arr, k):
    heap = []
    for i in range(k):
        heapq.heappush(heap, arr[i])
    for j in range(i + 1, len(arr)):
        if arr[j] > heap[0]:
            heapq.heappushpop(heap, arr[j])
    return (heapq.heappop(heap) for i in range(k))


k = 3
print('Kth Largest Element in Array:',
      *getKLargestElement([1, 23, 12, 9, 30, 2, 50], k))
