# question --> https://practice.geeksforgeeks.org/problems/search-a-node-in-bst/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

class BST:
    
    #Function to search a node in BST.
    def search(self, node, x):
        #code here
        if not node: 
            return 0
            
        if node.data == x:
            return 1
            
        elif node.left and node.data > x: 
            return self.search(node.left, x)
            
        elif node.right and node.data < x: 
            return self.search(node.right, x)
            
    # TC: O(Height of the BST); SC: O(Height of the BST)