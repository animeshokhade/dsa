# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def __init__(self):
        self.stack = []

    def inorderTraversal(self, A):
        ans = list()

    while self.stack or A:
        if A:
            self.stack.append(A)
            A = A.left
        else:
            A = self.stack.pop()
            ans.append(A.val)
            A = A.right

    return ans

