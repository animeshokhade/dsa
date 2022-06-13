# question --> https://practice.geeksforgeeks.org/problems/find-difference-between-sum-of-diagonals1554/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

class Solution:
    def diagonalSumDifference(self, N, Grid):
        # code here
        diag1 = 0
        diag2 = 0
        for r in range(N):
            for c in range(N):
                if r == c:
                    diag1 += Grid[r][c]
                if r == N - c - 1:
                    diag2 += Grid[r][c]
        return abs(diag1 - diag2)

        # TC: O(N^2); SC: O(1)
