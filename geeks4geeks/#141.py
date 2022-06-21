# question --> https://practice.geeksforgeeks.org/problems/minimum-element-in-bst/1/?page=3&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions#

def minValue(root):
    ##Your code here
    if not root: return -1
    if root.left == None:
        return root.data

    return minValue(root.left)

    # TC: O(Height of the Tree); SC: O(Height of the Tree)