# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def boolean(self, A, B, C):
        if A is None:
            return False

        C.append(A.val)

        if A.val == B:
            return True

        if self.boolean(A.left, B, C) or self.boolean(A.right, B, C):
            return True

        C.pop()
        return False

    def solve(self, A, B):
        C = list()
        if A is None:
            return C

        self.boolean(A, B, C)
        return C

