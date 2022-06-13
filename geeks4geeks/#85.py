# question --> https://practice.geeksforgeeks.org/problems/identical-matrices1042/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def areMatricesidentical(self, N, Grid1, Grid2):
        # code here
        for r in range(N):
            for c in range(N):
                if Grid1[r][c] != Grid2[r][c]:
                    return 0
        return 1

        # TC: O(N^2); SC: O(1)
