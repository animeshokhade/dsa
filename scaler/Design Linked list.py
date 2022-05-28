# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def insertAtBeginning(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
        self.count += 1

    def insertAtLast(self, val):
        if self.head == None:
            node = Node(val)
            self.head = node
        else:
            node = Node(val)
            current = self.head
            while current.next != None:
                current = current.next

            current.next = node
        self.count += 1

    def insertAtPosition(self, val, position):
        if position > self.count + 1:
            return
        node = Node(val)

        if position == 1:
            node.next = self.head
            self.head = node

        current = self.head
        curr_pos = 1
        while current:
            if curr_pos == position - 1:
                node.next = current.next
                current.next = node
                break
            else:
                current = current.next
                curr_pos += 1
        self.count += 1

    def deleteFromPosition(self, position):
        if self.head == None:
            return

        if position > self.count:
            return

        if position == 1:
            self.head = self.head.next

        current = self.head
        curr_pos = 1
        while current:
            if curr_pos == position - 1:
                current.next = current.next.next
                break
            else:
                current = current.next
                curr_pos += 1
        self.count -= 1


class Solution:
    # @param A : list of list of integers
    # @return the head node in the linked list
    def solve(self, A):

        ll = LinkedList()

        for i in range(len(A)):
            if A[i][0] == 0:
                # add node in the beginning
                ll.insertAtBeginning(A[i][1])
            elif A[i][0] == 1:
                # add node at last
                ll.insertAtLast(A[i][1])
            elif A[i][0] == 2:
                # add element at index position
                pos = A[i][2] + 1
                ll.insertAtPosition(A[i][1], pos)
            elif A[i][0] == 3:
                # delete index node
                pos = A[i][1] + 1
                ll.deleteFromPosition(pos)

        return ll.head

