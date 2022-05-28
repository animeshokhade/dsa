class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        M = len(A)
        summ = 0
        for m in range(M):
            summ += A[m][M - m - 1]
        return summ

