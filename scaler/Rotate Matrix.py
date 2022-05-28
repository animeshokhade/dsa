class Solution:
    # @param A : list of list of integers
    def solve(self, A):
        n = len(A)
        for i in range(n):
            for j in range(i + 1, n):
                temp = A[i][j]
                A[i][j] = A[j][i]
                A[j][i] = temp
        for i in range(n // 2):
            for j in range(n):
                temp = A[j][n - i - 1]
                A[j][n - i - 1] = A[j][i]
                A[j][i] = temp
        return A
