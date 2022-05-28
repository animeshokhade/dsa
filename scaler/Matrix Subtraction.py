class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        rows, cols = len(A), len(A[0])
        ans = [[0 for c in range(cols)] for r in range(rows)]
        for r in range(rows):
            for c in range(cols):
                ans[r][c] = A[r][c] - B[r][c]
        return ans
