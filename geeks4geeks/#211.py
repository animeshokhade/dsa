# question --> https://practice.geeksforgeeks.org/problems/reverse-a-linked-list/1/?page=1&status[]=unsolved&category[]=Linked%20List&sortBy=submissions#

"""
# Node Class

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""


class Solution:
    # Function to reverse a linked list.
    def reverseList(self, head):
        # Code here
        aft = None
        bef = None
        cur = head

        while cur:
            aft = cur.next
            cur.next = bef
            bef = cur
            cur = aft

        head = bef
        return head

        # TC: O(N); SC: O(1) 