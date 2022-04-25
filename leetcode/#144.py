# question --> https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []; 
        stack.append(root); 
        ans = []; 
        while stack: 
            node = stack.pop(); 
            if node:
                ans.append(node.val); 
                if node.right: 
                    stack.append(node.right)
                if node.left: 
                    stack.append(node.left)
        return ans
        
        # TC: O(N); SC: O(N)
        
# end 
        