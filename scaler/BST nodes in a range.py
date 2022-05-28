# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        if not A:
            return 0

        if A.val < B:
            return self.solve(A.right, B, C)

        if A.val > C:
            return self.solve(A.left, B, C)

        return 1 + self.solve(A.left, B, C) + self.solve(A.right, B, C)

# alternative approach

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        if A is None:
            return

        node_count = 1 if B <= A.val <= C else 0
        if A.left is not None:
            node_count += self.solve(A.left, B, C)

        if A.right is not None:
            node_count += self.solve(A.right, B, C)

        return node_count

