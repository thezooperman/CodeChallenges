"""
Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = ListNode()
        heap_data = []

        # fucking stupid checks
        if not any(lists):
            return

        for list in lists:
            while list:
                heapq.heappush(heap_data, list.val)
                list = list.next
        
        # print(heap_data)
        
        head = root
        isFirst = True
        
        while heap_data:
            node = heapq.heappop(heap_data)
            if isFirst:
                head.val = node
                isFirst = False 
            else:
                list_node = ListNode(val=node)
                head.next = list_node
                head = list_node

        # print(root)


        return root