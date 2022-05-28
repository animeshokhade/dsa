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
        def goodNode(A, maximum):
            if A is None:
                return 0

            ans = 1 if A.val > maximum else 0
            maximum = max(A.val, maximum)
            ans += goodNode(A.left, maximum)
            ans += goodNode(A.right, maximum)

            return ans

        return goodNode(A, float('-inf'))
