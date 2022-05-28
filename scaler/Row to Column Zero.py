class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        rows, cols = len(A), len(A[0])
        rowZero, colZero = [], []
        for r in range(rows):
            for c in range(cols):
                if A[r][c] == 0:
                    rowZero.append(r)
                    colZero.append(c)
        for r in rowZero:
            for c in range(cols):
                A[r][c] = 0
        for c in colZero:
            for r in range(rows):
                A[r][c] = 0
        return A
