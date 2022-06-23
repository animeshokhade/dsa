# question --> https://practice.geeksforgeeks.org/problems/check-for-bst/1/?page=1&status[]=unsolved&sortBy=submissions#

import sys
class Solution:
    
    #Function to check whether a Binary Tree is BST or not.
    def check(self, node, minn, maxx):
        if root is None: 
            return 1
            
        if root.data < minn or root.data > maxx: 
            return 0
            
        return self.check(root.left, minn, root.data - 1) and \
        self.check(root.right, root.data + 1, maxx)
        
    
    def isBST(self, root):
        #code here
        return self.check(root, -sys.maxsize, sys.maxsize)
        
    # TC: O(N); SC: O(Height of the BST)