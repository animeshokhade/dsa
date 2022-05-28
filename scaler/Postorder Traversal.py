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
        self.stack = list()


def postorderTraversal(self, A):
    ans = list()
    self.stack.append(A)

    while self.stack:
        A = self.stack.pop()
        ans.append(A.val)
        if A.left:
            self.stack.append(A.left)
        if A.right:
            self.stack.append(A.right)

    return ans[::-1]

# alternative approach

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def __init__(self):
        self.stack = list()

    def postorderTraversal(self, A):
        ans = list()
        self.stack.append(A)
        while self.stack:
            A = self.stack.pop()
            ans.append(A.val)
            left, right = A.left, A.right
            if left:
                self.stack.append(left)
            if right:
                self.stack.append(right)

        return ans[::-1]

# alternative approach

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def __init__(self):
        self.stack = list()

    def postorderTraversal(self, A):
        ans = list()
        self.stack.append(A)
        while self.stack:
            A = self.stack.pop()
            ans.append(A.val)
            left, right = A.left, A.right
            if left:
                self.stack.append(left)
            if right:
                self.stack.append(right)
            if not left and not right and self.stack:
                A = self.stack[-1]

        return ans[::-1] 