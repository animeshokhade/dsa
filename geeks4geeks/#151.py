# question --> https://practice.geeksforgeeks.org/problems/print-linked-list-elements/1/?page=2&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions#

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''
class Solution:
    def display(self,node):
        #code here
        head = node
        while head:
            print(head.data, end = ' ')
            head = head.next

    # TC: O(N); SC: O(1) 