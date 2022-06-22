# question --> https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1/?page=4&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions#

class Solution:

    def findMinDiff(self, A, N, M):
        # code here
        A.sort()

        itr = N - M + 1
        ret = float('inf')

        for i in range(itr):
            ret = min(ret, A[i + M - 1] - A[i])

        return ret

    # TC: O(NlogN); SC: O(1)