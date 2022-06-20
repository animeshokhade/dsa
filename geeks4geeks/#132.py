# question --> https://practice.geeksforgeeks.org/problems/diagonal-sum0158/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def DiagonalSum(self, matrix):
        # Code here
        summ = 0
        n = len(matrix)
        for r in range(n):
            summ += matrix[r][r] + matrix[r][n - 1 - r]

        return summ

    # TC: O(N); SC: O(1)