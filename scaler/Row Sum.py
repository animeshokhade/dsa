class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        ans = []
        rows, cols = len(A), len(A[0])
        for row in range(rows):
            summ = 0
            for col in range(cols):
                summ += A[row][col]
            ans.append(summ)
        return ans

