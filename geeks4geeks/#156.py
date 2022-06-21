# question --> https://practice.geeksforgeeks.org/problems/linked-list-insertion-1587115620/1/?page=2&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions#

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''


class Solution:
    # Function to insert a node at the beginning of the linked list.
    def insertAtBegining(self, head, x):
        # code here
        curr = Node(x)
        if head:
            curr.next = head
        return curr

    # Function to insert a node at the end of the linked list.
    def insertAtEnd(self, head, x):
        # code here
        node = Node(x)
        if not head:
            head = node
        else:
            curr = head
            while curr.next:
                curr = curr.next
            curr.next = node
        return head

        # TC: O(N); SC: O(1)