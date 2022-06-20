# question --> https://practice.geeksforgeeks.org/problems/parenthesis-checker2744/1/?page=1&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions#

class Solution:

    # Function to check if brackets are balanced or not.
    def ispar(self, x):
        # code here
        if len(x) == 1: return 0
        stk = []
        for br in x:
            if stk and br == ')' and stk[-1] == '(':
                stk.pop()
            elif stk and br == '}' and stk[-1] == '{':
                stk.pop()
            elif stk and br == ']' and stk[-1] == '[':
                stk.pop()
            else:
                stk.append(br)
        if stk:
            return 0
        return 1

        # TC: O(|S|); SC: O(|S|)
