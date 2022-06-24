# question --> https://practice.geeksforgeeks.org/problems/remove-loop-in-linked-list/1/?page=1&status[]=unsolved&sortBy=submissions#

'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''

class Solution:
    #Function to remove a loop in the linked list.
    
    # Floyd’s cycle detection algorithm
    def detectLoop(self, head):
        slow = fast = head
        
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast: 
                return slow
                
        return None
    
    def removeLoop(self, head):
        # code here
        # remove the loop without losing any nodes
        
        slow = self.detectLoop(head)
        if slow: 
            n = 1
            p = slow
        
            # counting nodes in the loop
            while p.next is not slow: 
                n += 1
                p = p.next 
            
            # set cur at the nth node
            cur = head
            for _ in range(n):
                cur = cur.next
            
            # moving head and curr at same speed
            # until they meet
        
            while cur is not head: 
                cur = cur.next
                head = head.next
            
            # move cur to point to the last node of the ll
            while cur.next is not head:
                cur = cur.next
            
            cur.next = None 
            
        # TC: O(N); SC: O(1)