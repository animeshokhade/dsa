# question --> https://practice.geeksforgeeks.org/problems/count-leaves-in-binary-tree/1/?page=3&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions#

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''


# your task is to complete this function
# function should return the count of Leaf node's
# Note: You required to print a new line after every test case
def countLeaves(root):
    # Code here
    if root == None:
        return 0

    if root.left == None and root.right == None:
        return 1

    return countLeaves(root.left) + countLeaves(root.right)

    # TC: O(N); SC: O(Height of the tree)
