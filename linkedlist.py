class Node:
    '''Class to define Linked List Node'''
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.child = None

class LinkedList:
    '''Linked List class'''
    def __init__(self):
        self.head = None

    def add(self, data):
        '''Adds a linked list node to the front of the list'''
        node = Node(data)
        if self.head is not None:
            node.next = self.head
            self.head = node
        else:
            self.head = Node(data)

    def reverse(self):
        '''Reverse a Linked List'''
        current = self.head
        prev = None
        while current:
            nxt = current.next
            current.next = prev
            prev, current = current, nxt
        self.head = prev

    def mergesorted(self, list2):
        '''Merge two sorted linked list'''
        list1 = self.head
        mergedlist = dummy = Node(-1)
        while list1 and list2:
            if list1.data < list2.data:
                mergedlist.next = Node(list1.data)
                list1 = list1.next
            else:
                mergedlist.next = Node(list2.data)
                list2 = list2.next
        remnodes = list1 or list2
        while remnodes:
            mergedlist.next = Node(remnodes.data)
            remnodes = remnodes.next
        return dummy.next

    def getlistlength(self):
        '''Get the length of the linked list'''
        counter = 0
        if hasattr(self, 'head'):
            start = self.head
        else:
            start = self
        if start is not None:
            while start:
                counter += 1
                start = start.next
        return counter

    def printlinkedlist(self):
        '''Print the Linked List'''
        if hasattr(self, 'head'):
            start = self.head
        else:
            start = self
        while start:
            print(start.data, end=' ')
            start = start.next
        print(flush=True)

    def printnthnodefromtail(self, n):
        '''Print the Nth node from the tail of the Linked List'''
        if self.head is not None:
            ptr1 = self.head
            ptr2 = self.head
            while n > 0:
                ptr1 = ptr1.next
                n -= 1
            while ptr1:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            return ptr2.data
        return -1

def main():
    '''Entry point to Linked List class'''
    root = LinkedList()
    root.add(1)
    root.add(3)
    root.add(2)
    root.printlinkedlist()
    print(root.printnthnodefromtail(1))

if __name__ == "__main__":
    main()
