class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        row, col = len(A), len(A[0])
        count = 0
        for r in range(row):
            for c in range(col):
                if A[r][c] == B[r][c]:
                    count += 1
        if count == row * col:
            return 1
        return 0
