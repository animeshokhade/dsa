# question --> https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q: 
            return p == q
        
        f0 = p.val == q.val
        f1 = self.isSameTree(p.left, q.left)
        f2 = self.isSameTree(p.right, q.right)
        
        return f0 and f1 and f2
    
        # TC: O(N); SC: O(Height of the Tree)