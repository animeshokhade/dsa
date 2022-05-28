# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preorderTraversal(self, A):
        stack = []
        stack.append(A)
        ans = []
        while stack:
            temp = stack.pop()
            ans.append(temp.val)
            if temp.right != None:
                stack.append(temp.right)
            if temp.left != None:
                stack.append(temp.left)

        return ans

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

    def preorderTraversal(self, A):
        ans = list()
        while A or self.stack:
            if A:
                self.stack.append(A)
                ans.append(A.val)
                A = A.left
            else:
                A = self.stack.pop()
                A = A.right

        return ans


