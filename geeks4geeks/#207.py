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

# alternative approach

class Solution:
	def minJumps(self, arr, n):
	    #code here
	    if n <= 1: 
	        return 0
	        
	    if arr[0] == 0:
	        return -1
	        
	    if arr[0] > n: 
	        return 1
	        
	    jum = 1
	    cur_str = 1
	    steps = arr[0]
	    max_reach = arr[0]
	    
	    while cur_str < n - 1: 
	        max_reach = max(max_reach, cur_str + arr[cur_str])
	        steps -= 1
	        if arr[cur_str] == 0:
	            return -1
	        if max_reach >= n - 1:
	            jum += 1
	            return jum 
	        if steps == 0: 
	            steps = max_reach - cur_str
	            jum += 1
	            
	        cur_str += 1
	    
	    return jum   
	    
	# TC: O(N); SC: O(1)