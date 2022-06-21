# question --> https://practice.geeksforgeeks.org/problems/preorder-traversal/1/?page=2&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions#

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''


# Function to return a list containing the preorder traversal of the tree.
def preorder(root):
    # code here
    pre = []

    if root:
        pre.append(root.data)
        pre += preorder(root.left)
        pre += preorder(root.right)

    return pre

    # TC: O(N); SC: O(N)
