# question --> https://practice.geeksforgeeks.org/problems/inorder-traversal/1/?page=2&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions#

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''


# Function to return a list containing the inorder traversal of the tree.
class Solution:
    def InOrder(self, root):
        # code here
        ret = []

        if root:
            ret += self.InOrder(root.left)
            ret.append(root.data)
            ret += self.InOrder(root.right)

        return ret

        # TC: O(N); SC: O(Height of the Tree -> worst case: N)
