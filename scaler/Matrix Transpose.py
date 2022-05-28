class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        rows, cols = len(A), len(A[0])
        ans = [[0 for r in range(rows)] for c in range(cols)]
        for c in range(cols):
            for r in range(rows):
                ans[c][r] = A[r][c]
        return ans
