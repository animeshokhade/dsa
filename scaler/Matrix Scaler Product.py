class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B):
        row, col = len(A), len(A[0])
        for r in range(row):
            for c in range(col):
                A[r][c] *= B
        return A
