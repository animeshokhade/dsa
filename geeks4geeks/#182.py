# question --> https://practice.geeksforgeeks.org/problems/delete-alternate-nodes/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions

'''class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  
        self.next = None'''

class Solution: 
    
    
    def deleteAlt(self, head):
        
        #add code here
        cur = head
        drop = True
        
        while cur.next:
            if drop: 
                cur.next = cur.next.next
                drop = False
            else: 
                cur = cur.next
                drop = True 

        return head 
        
        # TC: O(N); SC: O(1)