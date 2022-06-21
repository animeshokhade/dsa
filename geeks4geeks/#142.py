# question --> https://practice.geeksforgeeks.org/problems/implement-stack-using-array/1/?page=3&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions#

class MyStack:

    def __init__(self):
        self.arr = []

    # Function to push an integer into the stack.
    def push(self, data):
        # add code here
        return self.arr.append(data)

    # Function to remove an item from top of the stack.
    def pop(self):
        # add code here
        if self.arr:
            return self.arr.pop()

        return -1

    # TC: O(1); SC: O(1)
