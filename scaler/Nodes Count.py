import sys
sys.setrecursionlimit(10 ** 6)

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        ans = 0 if A is None else 1
        if A is not None:
            ans += self.solve(A.left)
            ans += self.solve(A.right)
        return ans

