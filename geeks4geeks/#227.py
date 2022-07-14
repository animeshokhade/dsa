# question --> https://practice.geeksforgeeks.org/problems/consecutive-elements2306/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

class Solution:
    def removeConsecutiveCharacter(self, S):
        # code here
        stack = ['#']
        for ch in S:
            if stack[-1] != ch:
                stack.append(ch)
        return ''.join(stack[1:])

        # TC: O(|S|); SC: O(|S|)