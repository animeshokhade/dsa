# question --> https://practice.geeksforgeeks.org/problems/determine-if-two-trees-are-identical/1/?page=1&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions#

'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''


class Solution:
    # Function to check if two trees are identical.
    def isIdentical(self, root1, root2):
        # Code here
        if root1 == None and root2 == None:
            return 1
        elif root1 == None or root2 == None:
            return 0
        elif root1.data != root2.data:
            return 0

        l = self.isIdentical(root1.left, root2.left)
        r = self.isIdentical(root1.right, root2.right)

        return l and r

        # TC: O(N); SC: O(Height of the Tree)
