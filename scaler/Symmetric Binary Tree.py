# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        if A is None and B is None:
            return 1
        elif A is None or B is None:
            return 0

    return self.isSameTree(A.left, B.right) and self.isSameTree(A.right, B.left)


def isSymmetric(self, A):
    return self.isSameTree(A.left, A.right)

# alternative approach

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        if A is None and B is None:
            return 1
        elif A is None or B is None:
            return 0

        if A.val != B.val:
            return 0

        return self.isSameTree(A.left, B.right) and self.isSameTree(A.right, B.left)

    def isSymmetric(self, A):
        return self.isSameTree(A.left, A.right)

# alternative approach

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        if A is None and B is None:
            return 1
        elif A is None or B is None:
            return 0

        if A.val != B.val:
            return 0

        return int(self.isSameTree(A.left, B.right) and self.isSameTree(A.right, B.left))

    def isSymmetric(self, A):
        if self.isSameTree(A.left, A.right):
            return 1
        return 0

# alternative approach

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        if A is None and B is None:
            return 1
        elif A is None or B is None:
            return 0

        if A.val != B.val:
            return 0

        left_subTree = self.isSameTree(A.left, B.right)
        right_subTree = self.isSameTree(A.right, B.left)

        if left_subTree == right_subTree:
            return 1
        return 0

    def isSymmetric(self, A):
        if self.isSameTree(A.left, A.right):
            return 1
        return 0
