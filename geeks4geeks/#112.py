# question --> https://practice.geeksforgeeks.org/problems/addition-of-two-square-matrices4916/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def Addition(self, matrixA, matrixB):
        # Code here
        n = len(matrixA)
        for r in range(n):
            for c in range(n):
                matrixA[r][c] = matrixA[r][c] + matrixB[r][c]

    # TC: O(N^2); SC: O(1)
