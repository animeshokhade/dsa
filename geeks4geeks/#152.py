# question --> https://practice.geeksforgeeks.org/problems/delete-a-node-in-single-linked-list/1/?page=2&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions#

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''


def delNode(head, k):
    # Code here
    prev = head
    curr = head

    if k == 1:
        prev = prev.next
        return prev

    pos = 1
    while curr:
        if pos == k:
            prev.next = prev.next.next
            return head

        prev = curr
        curr = curr.next
        pos += 1

    # TC: O(N); SC: O(1)
