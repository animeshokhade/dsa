class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        ans = []
        rows, cols = len(A), len(A[0])
        for c in range(cols):
            summ = 0
            for r in range(rows):
                summ += A[r][c]
            ans.append(summ)
        return ans
