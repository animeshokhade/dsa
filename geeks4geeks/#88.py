# question --> https://practice.geeksforgeeks.org/problems/alone-in-couple5507/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def findSingle(self, N, arr):
        # code here
        xor = 0
        for a in arr:
            xor ^= a
        return xor

        # TC: O(N); SC: O(1)
