# question --> https://practice.geeksforgeeks.org/problems/detect-loop-in-linked-list/1/?page=1&status[]=unsolved&sortBy=submissions#

'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here
        slow = fast = head
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
            if slow == fast: 
                return True
        return False
        
        # TC: O(N); SC: O(1)