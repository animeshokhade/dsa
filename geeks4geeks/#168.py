# question --> https://practice.geeksforgeeks.org/problems/implement-stack-using-linked-list/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyStack:


    # class StackNode:

    # # Constructor to initialize a node
    # def __init__(self, data):
    #     self.data = data
    #     self.next = None
        
    def __init__(self):
        self.top = None 
        
    #Function to push an integer into the stack.
    def push(self, data):

        # Add code here
        node = StackNode(data)
        node.next = self.top
        self.top = node
        
        


    #Function to remove an item from top of the stack.
    def pop(self):

        # Add code here
        if not self.top: 
            return -1
            
        p = self.top.data
        self.top = self.top.next
        return p
        
    # TC: O(1); SC: O(1) for both push and pop operations 
