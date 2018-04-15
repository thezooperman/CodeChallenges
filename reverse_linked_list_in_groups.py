# reverse_linked_list_in_groups.py
'''
Given a linked list, write a function to
reverse every k nodes (where k is an
input to the function).
Inputs:  1->2->3->4->5->6->7->8->NULL and k = 3
Output:  3->2->1->6->5->4->8->7->NULL.

Inputs:   1->2->3->4->5->6->7->8->NULL and k = 5
Output:  5->4->3->2->1->8->7->6->NULL.
'''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def push(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def reverse(self, head, k):
        current = head
        next = prev = None
        count = 0
        while current and count < k:
            next = current.next
            current.next = prev
            prev, current = current, next
            count += 1
        if next:
            head.next = self.reverse(next, k)
        return prev

    def print(self, head):
        cur = head
        while cur:
            if cur.next is None:
                print(cur.val, end='')
            else:
                print(cur.val, end='->')
            cur = cur.next


def main():
    ll = LinkedList()
    ll.push(9)
    ll.push(8)
    ll.push(7)
    ll.push(6)
    ll.push(5)
    ll.push(4)
    ll.push(3)
    ll.push(2)
    ll.push(1)
    ll.print(ll.head)
    ll.head = ll.reverse(ll.head, 3)
    print()
    ll.print(ll.head)
    print()


main()
