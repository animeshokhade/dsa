class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        m, p = len(A), len(B[0])
        C = [[0 for x in range(p)] for y in range(m)]
        for i in range(m):
            rows = []
            for r in range(len(A[0])):
                rows.append(A[i][r])
            for j in range(p):
                temp = 0
                cols = []
                for c in range(len(B)):
                    cols.append(B[c][j])
                for k in range(len(rows)):
                    temp += rows[k] * cols[k]
                C[i][j] = temp
        return C


