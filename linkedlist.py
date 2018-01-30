'''
This module lists all the basic Linked List interview questions
'''
from queue import PriorityQueue


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
        '''Reverse a Linked List
           Complexity:O(n)
        '''
        current = self.head
        prev = None
        while current:
            nxt = current.next
            current.next = prev
            prev, current = current, nxt
        self.head = prev

    def mergesorted(self, list2):
        '''Merge two sorted linked list
           Complexity:O(n)
        '''
        list1 = self.head
        mergedlist = dummy = LinkedList()
        while list1 and list2:
            if list1.data < list2.data:
                mergedlist.add(list1.data)
                list1 = list1.next
            else:
                mergedlist.add(list2.data)
                list2 = list2.next
        remnodes = list1 or list2
        while remnodes:
            mergedlist.add(remnodes.data)
            remnodes = remnodes.next
        return dummy

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
        '''Print the Nth node from the tail of the Linked List
           Compleity:O(n)
        '''
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

    def sort(self):
        '''Given an unsorted list, sort the list
           Complexity:O(nlogn)
        '''
        if self.head is not None:
            tmp = []
            root = self.head
            while root:
                tmp.append(root.data)
                root = root.next
            tmp.sort()
            tmplist = LinkedList()
            for v in tmp:
                tmplist.add(v)
            self.head = tmplist.head

    def add2numbers(self, num1):
        '''Given two linked list with numbers, add and
           return the result in a Linked List
           Complexity:O(n)
        '''
        num2 = self.head
        if num1 is None and num2 is None:
            return None
        if num1 is None:
            return num2
        if num2 is None:
            return num1
        result = LinkedList()
        carry = 0
        while num1 or num2:
            num1_val = num1.data if num1 else 0
            num2_val = num2.data if num2 else 0
            add = num1_val + num2_val + carry
            if add >= 10:
                carry = 1
                add = add % 10
            else:
                carry = 0
            result.add(add)
            if num1:
                num1 = num1.next
            if num2:
                num2 = num2.next
        if carry:
            result.add(carry)
        return result

    def detectloop(self):
        '''Given a Linked List, if the list has cycle,
           return node else return -1'''
        slowptr = self.head
        fastptr = self.head
        while fastptr.next is not None and fastptr.next.next is not None:
            fastptr = fastptr.next.next
            slowptr = slowptr.next
            if fastptr == slowptr:
                return fastptr.data
        return -1

    def removeloop(self):
        '''Given a Linked List with loop, remove the loop
           Complexity: O(n)
        '''
        slowptr = self.head
        fastptr = self.head
        while fastptr.next is not None and fastptr.next.next is not None:
            fastptr = fastptr.next.next
            slowptr = slowptr.next
            if fastptr == slowptr:
                break
        ptr = self.head
        while ptr and ptr != fastptr:
            ptr = ptr.next
        ptr.next = None

    def flattenlist(self):
        '''Given a list, flatten the list and return the modified list
           Complexity:O(n)
        '''
        if self.head is not None:
            tail = self.head
            start = self.head
            while tail.next:
                tail = tail.next
            while start != tail:
                if start.child:
                    tail.next = start.child
                    tmp = start.child
                    while tmp.next:
                        tmp = tmp.next
                    tail = tmp
                start = start.next
            return self.head
        return None

    def findindexofsubset(self, sublist):
        '''Given a Linked List, find the index of
           another Linked List, if that List is a subset of the parent
           Complexity:O(n)
        '''
        root = self.head
        index = 0
        sublist_dummy = sublist
        while root:
            if root.data == sublist.data:
                root = root.next
                sublist = sublist.next
                if sublist is None:
                    return index
            else:
                sublist = sublist_dummy
                index += 1
                root = root.next
        return index if sublist is None else -1

    def findintersectionpoint(self, otherlist):
        """
        Given two linked lists, which intersected
        at some point, find the intersection node.
        Complexity: O(n)
        Args:
            otherlist (Node): The other created list
        Returns:
            The intersection node, if found, else -1
        """
        root = self.head
        root_len = otherlist_len = 0
        tmp_other = otherlist
        while root:
            root_len += 1
            root = root.next
        while otherlist:
            otherlist_len += 1
            otherlist = otherlist.next
        if root_len > otherlist_len:
            diff = root_len - otherlist_len
        else:
            root, otherlist = otherlist, root  # make root larger list
        root = self.head
        while diff > 0:
            root = root.next
            diff -= 1
        while root:
            if root == tmp_other:
                return root.data
            root = root.next
            tmp_other = tmp_other.next
        return -1

    def findduplicates(self):
        '''Find duplicates in linked list
           Complexity: O(n)
           Args:
                None
        '''
        duplicates = {}
        root = self.head
        prev = None
        while root:
            if root.data in duplicates:
                prev.next = root.next
            else:
                duplicates.setdefault(root.data, 1)
                prev = root
            root = root.next

    def leftrotate(self, k):
        '''Given a Linked List, rotate the k elements anti-clockwise.
           If the given linked list is 10->20->30->40->50->60 and k is 4,
           the list should be modified to 50->60->10->20->30->40
           Complexity:O(n)
           Args:
                k : value by which to rotate the Linked List
        '''
        if k < 1:
            return None
        root = self.head
        count = 1
        while count < k and root.next:
            count += 1
            root = root.next
        kthnode = root
        while root.next is not None:
            root = root.next
        root.next = self.head
        self.head = kthnode.next
        kthnode.next = None
        # data_list = []
        # while root:
        #     data_list.append(root.data)
        #     root = root.next
        # rotated_list = data_list[k:] + data_list[:k]
        # root = LinkedList()
        # for data in rotated_list[::-1]:
        #     root.add(data)
        # self.head = root.head

    def mergeksortedlists(self, klists):
        '''Given an array of k-sorted linked lists, merge the lists
           and return a single linked list of sorted elements
           Complexity: O(nlogk), n = nodes, k = lists
           Args:
                klists: list of k sorted Linked Lists
        '''
        q = PriorityQueue(len(klists))
        start = dummy = LinkedList()
        for slist in klists:
            if slist:
                q.put((slist.data, slist))
        while not q.empty():
            val, node = q.get()
            dummy.add(val)
            node = node.next
            if node:
                q.put((node.data, node))
        return start

    def midlistinonepass(self):
        '''Find Middle of a Linked List with One Pass/Loop'''
        ptr1 = self.head
        ptr2 = self.head
        length = 0
        while ptr1:
            if length % 2 != 0:
                ptr2 = ptr2.next
            length += 1
            ptr1 = ptr1.next
        return ptr2.data


def test_add_list():
    '''Call to populate a list'''
    root = LinkedList()
    # Add sample nodes to root
    root.add(1)
    root.add(3)
    root.add(2)
    root.printlinkedlist()  # prints 2 3 1


def test_print_nth_node_from_tail():
    '''Call to print nth node from tail'''
    root = LinkedList()
    # Add sample nodes to root
    root.add(1)
    root.add(3)
    root.add(2)
    # print nth node from tail of the list
    print(root.printnthnodefromtail(1))  # prints 1


def test_reverse_list():
    '''Call to reverse a list'''
    root = LinkedList()
    # Add sample nodes to root
    root.add(1)
    root.add(3)
    root.add(2)
    # reverse list
    root.reverse()
    root.printlinkedlist()  # prints 1 3 2


def test_merge_list():
    '''Call to merge two sorted list'''
    # merge 2 sorted lists
    root = LinkedList()
    root.add(3)
    root.add(2)
    root.add(1)
    second_list = Node(4)
    second_list.next = Node(5)
    second_list.next.next = Node(6)
    merged = root.mergesorted(second_list)
    merged.printlinkedlist()  # print 6 5 4 3 2 1


def test_sort_list():
    '''Call to sort an unsorted linked list'''
    root = LinkedList()
    root.add(9)
    root.add(4)
    root.add(12)
    root.add(3)
    root.sort()
    root.printlinkedlist()  # print 12 9 4 3


def test_add_two_list():
    '''Call to add two linked list numbers'''
    root = LinkedList()
    root.add(1)
    root.add(2)
    root.add(3)
    list2 = LinkedList()
    list2.add(7)
    list2.add(7)
    add_2_nos = root.add2numbers(list2.head)
    add_2_nos.printlinkedlist()  # print 200 -> 123 + 77


def test_detect_loop():
    '''Call to detect loop in list'''
    # detect loop in linked list and remove loop
    root = LinkedList()
    l1 = Node(5)
    l2 = Node(4)
    l3 = Node(3)
    l4 = Node(2)
    l5 = Node(1)
    l5.next = l4
    l4.next = l3
    l3.next = l2
    l2.next = l1
    l1.next = l4  # loop creation
    root.head = l5
    print(root.detectloop())  # prints 5


def test_remove_loop():
    '''Call to detect loop in linked list and remove loop'''
    root = LinkedList()
    l1 = Node(5)
    l2 = Node(4)
    l3 = Node(3)
    l4 = Node(2)
    l5 = Node(1)
    l5.next = l4
    l4.next = l3
    l3.next = l2
    l2.next = l1
    l1.next = l4  # loop creation
    root.head = l5
    print(root.detectloop())  # prints 5
    root.removeloop()
    root.printlinkedlist()  # print 1 2 3 4 5


def test_flattenlist():
    '''Call to flatten linked list'''
    root = LinkedList()
    l10 = Node(10)
    l5 = Node(5)
    l12 = Node(12)
    l7 = Node(7)
    l11 = Node(11)
    l4 = Node(4)
    l20 = Node(20)
    l2 = Node(2)
    l13 = Node(13)
    l16 = Node(16)
    l3 = Node(3)
    l17 = Node(17)
    l9 = Node(9)
    l19 = Node(19)
    l6 = Node(6)
    l8 = Node(8)
    l15 = Node(15)

    l10.child = l4
    l4.next = l20
    l20.child = l2
    l20.next = l13
    l13.child = l16
    l16.child = l3
    l7.child = l17
    l17.next = l6
    l17.child = l9
    l9.next = l8
    l9.child = l19
    l19.next = l15
    l10.next = l5
    l5.next = l12
    l12.next = l7
    l7.next = l11

    root.head = l10
    flat_list = root.flattenlist()
    root.head = flat_list
    # output 10->5->12->7->11->4->20->13->17->6->2->16->9->8->3->19->15
    root.printlinkedlist()


def test_findindexofsubset():
    '''Call to index of sublist'''
    root = LinkedList()
    root.add(2)
    # root.add(10)@adding this should return -1
    root.add(11)
    root.add(43)
    root.add(5)
    sub = Node(11)
    sub.next = Node(2)
    print(root.findindexofsubset(sub))  # returns 2[0 based index]


def test_findintersectionpoint():
    '''Call to find the intersection point of two merged lists'''
    root = LinkedList()
    root.add(2)
    root.head.next = Node(3)
    tmp = Node(4)
    root.head.next.next = tmp
    root.head.next.next.next = Node(5)
    otherlist = Node(1)
    otherlist.next = tmp
    otherlist.next.next = Node(5)
    print(root.findintersectionpoint(otherlist))  # prints 4


def test_findduplicates():
    '''Call to find duplicates in linked list and clean dups'''
    root = LinkedList()
    root.add(3)
    root.add(2)
    root.add(1)
    root.add(3)
    root.add(1)
    root.add(2)
    root.add(1)
    root.findduplicates()
    root.printlinkedlist()  # expected output 1->2->3


def test_rotateleft():
    '''Call to test Linked List left rotation'''
    root = LinkedList()
    root.add(60)
    root.add(50)
    root.add(40)
    root.add(30)
    root.add(20)
    root.add(10)
    root.leftrotate(4)
    root.printlinkedlist()


def test_mergeksortedlists():
    '''Call to test merge-k-sorted list'''
    root = LinkedList()
    list1 = Node(44)
    list1.next = Node(45)
    list1.next.next = Node(46)
    list2 = Node(2)
    list2.next = Node(3)
    # list2.next.next = Node(4)
    list3 = Node(10)
    # list3.next = Node(11)
    # list3.next.next = Node(12)
    kmerged = root.mergeksortedlists([list3, list1, list2])
    kmerged.printlinkedlist()  # expected output - 46->45->44->10->3->2


def test_midpointoflist():
    '''Call to test midpoint in one pass'''
    root = LinkedList()
    root.add(5)
    root.add(4)
    root.add(3)
    root.add(2)
    root.add(1)
    val = root.midlistinonepass()
    print(val)


def main():
    '''Entry point to Linked List routine'''
    test_add_list()
    test_print_nth_node_from_tail()
    test_reverse_list()
    test_merge_list()
    test_sort_list()
    test_add_two_list()
    test_detect_loop()
    test_remove_loop()
    test_flattenlist()
    test_findindexofsubset()
    test_findintersectionpoint()
    test_findduplicates()
    test_rotateleft()
    test_mergeksortedlists()
    test_midpointoflist()


if __name__ == "__main__":
    main()
