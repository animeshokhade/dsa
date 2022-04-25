# question --> https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.stack = list()
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = list()
        while self.stack or root: 
            if root: 
                self.stack.append(root)
                root = root.left
            else:
                root = self.stack.pop()
                ans.append(root.val)
                root = root.right
                
        return ans
        
        # TC: O(N); SC: O(N)
        
# end 
    
    
        
        