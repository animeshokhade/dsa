# question --> https://practice.geeksforgeeks.org/problems/implement-queue-using-array/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

class MyQueue:
    
    def __init__(self):
        self.queue = []
    
    #Function to push an element x in a queue.
    def push(self, x):
         
        #add code here
        self.queue.append(x)
     
    #Function to pop an element from queue and return that element.
    def pop(self): 
         
        # add code here
        if not self.queue: 
            return -1
             
        return self.queue.pop(0)
        
    # TC: O(1); SC: O(1)