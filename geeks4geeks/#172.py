# question --> https://practice.geeksforgeeks.org/problems/implement-queue-using-linked-list/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

'''class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None'''
        
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class MyQueue:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    #Function to push an element into the queue.
    def push(self, item): 
         
        #Add code here
        if self.head:
            self.tail.next = Node(item)
            self.tail = self.tail.next
        else:
            self.tail = self.head = Node(item)
    
    #Function to pop front element from the queue.
    def pop(self):
         
        #add code here
        if self.head:
            p = self.head
            self.head = self.head.next 
            return p.data
        return -1
        
    # TC: O(1); SC: O(1)