# question --> https://practice.geeksforgeeks.org/problems/delete-node-in-doubly-linked-list/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
'''


class Solution:
    def deleteNode(self, head, x):
        # Code here
        if not head or not head.next:
            return None

        if x == 1:
            head = head.next
            head.prev = None
            return head

        cur = head
        i = 0
        while cur:
            i += 1
            if i == x:
                cur.prev.next = cur.next
            cur = cur.next
        return head

        # TC: O(N); SC: O(1) 