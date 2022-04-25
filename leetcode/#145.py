# question --> https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.stack = []
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.stack.append(root)
        
        while self.stack: 
            root = self.stack.pop()
            if root:
                ans.append(root.val)
                if root.left:
                    self.stack.append(root.left)
                if root.right:
                    self.stack.append(root.right)

        return ans[::-1] 
        
        # TC: O(N); SC: O(N) 
        
# end 