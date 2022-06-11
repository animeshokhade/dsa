# question --> https://practice.geeksforgeeks.org/problems/find-n-th-term-of-series-1-3-6-10-15-215506/1/?page=2&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def findNthTerm(self, N):
        # code here
        return (N * (N + 1)) // 2

    # TC: O(1); SC: O(1)
