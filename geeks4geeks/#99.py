# question --> https://practice.geeksforgeeks.org/problems/pattern-of-strings3829/1/?page=2&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def pattern(self, S):
        # code here
        n = len(S)
        ans = []
        for i in range(n, 0, -1):
            ans.append(S[:i])
        return ans

    # TC: O(N^2); SC: O(N^2)
