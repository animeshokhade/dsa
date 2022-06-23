# question --> https://practice.geeksforgeeks.org/problems/node-at-a-given-index-in-linked-list/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

"""index is the node which is to be displayed in output
  Node is defined as
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
# Linked List class contains a Node object
class LinkedList:
    def __init__(self):
        self.head = None
This is method only submission.
 You only need to complete below method.
"""
def getNth(head, k):
    # Code here
    cur = head 
    i = 1
    
    while cur: 
        if i == k: 
            return cur.data
        cur = cur.next 
        i += 1

    # TC: O(N); SC: O(1)