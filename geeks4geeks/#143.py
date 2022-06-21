# question --> https://practice.geeksforgeeks.org/problems/count-nodes-of-linked-list/1/?page=2&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions#

"""
# Linked list class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
"""
class Solution:

    #Function to count nodes of a linked list.
    def getCount(self, head_node):
        #code here
        l = 0
        tmp = head_node
        while tmp: 
            l += 1
            tmp = tmp.next 
        return l

    # TC: O(N); SC: O(1)