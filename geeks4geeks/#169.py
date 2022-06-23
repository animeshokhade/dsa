# question --> https://practice.geeksforgeeks.org/problems/postorder-traversal/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing the postorder traversal of the tree.
def postOrder(root):
    # code here
    post = []
    
    if root:
        post += postOrder(root.left)
        post += postOrder(root.right)
        post.append(root.data)
    
    return post
    
    # TC: O(N); SC: O(N)