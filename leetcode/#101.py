# question --> https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, left, right):
        if left is None or right is None: 
            return left == right
        
        f0 = left.val == right.val
        f1 = self.helper(left.left, right.right)
        f2 = self.helper(left.right, right.left)
        
        return f0 and f1 and f2
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root.left, root.right)
    
    # TC: O(N); SC: O(Height of the Tree)
