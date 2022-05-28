class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)

        # for B = 1 the same array will be replicated
        stripSum = [[0 for col in range(n)] for row in range(n)]

        for col in range(n):
            summ = 0

            for row in range(B):
                summ += A[row][col]

            stripSum[0][col] = summ

            for row in range(1, n - B + 1):
                summ += A[row + B - 1][col] - A[row - 1][col]
                stripSum[row][col] = summ

        maxSum = float('-inf')

        for row in range(n - B + 1):
            summ = 0

            for col in range(B):
                summ += stripSum[row][col]

            maxSum = max(maxSum, summ)

            for col in range(1, n - B + 1):
                summ += stripSum[row][col + B - 1] - stripSum[row][col - 1]
                maxSum = max(maxSum, summ)

        return maxSum

# alternate approach

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        stripSum = [[0 for j in range(n)] for i in range(n)]
        for j in range(n):
            s = 0
            for i in range(B):
                s += A[i][j]
            stripSum[0][j] = s
            for i in range(1, n - B + 1):
                s += A[i + B - 1][j] - A[i - 1][j]
                stripSum[i][j] = s
        maxSum = float('-inf')
        for i in range(n - B + 1):
            s = 0
            for j in range(B):
                s += stripSum[i][j]
            maxSum = max(maxSum, s)
            for j in range(1, n - B + 1):
                s += stripSum[i][j + B - 1] - stripSum[i][j - 1]
                maxSum = max(maxSum, s)

        return maxSum

# alternate approach

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        # pf_sum matrix
        N = len(A)
        pf_sum = [[0 for _ in range(N)] for _ in range(N)]
        pf_sum[0][0] = A[0][0]
        for c in range(1, N):
            pf_sum[0][c] = pf_sum[0][c - 1] + A[0][c]
        for r in range(1, N):
            pf_sum[r][0] = pf_sum[r - 1][0] + A[r][0]
        for r in range(1, N):
            for c in range(1, N):
                pf_sum[r][c] = pf_sum[r - 1][c] + pf_sum[r][c - 1] - pf_sum[r - 1][c - 1] + A[r][c]

        r1, c1 = 0, 0
        r2, c2 = B - 1, B - 1
        maxSum = float('-inf')
        for r in range(N - B + 1):
            for c in range(N - B + 1):
                r2 = r + B - 1
                c2 = c + B - 1
                maxSum = max(maxSum, self.findSubSum(pf_sum, r, c, r2, c2))
        return maxSum

    def findSubSum(self, matrix, r1, c1, r2, c2):
        if r1 == 0 and c1 == 0:
            val = matrix[r2][c2]
        else:
            if r1 == 0:
                val = matrix[r2][c2] - matrix[r2][c1 - 1]
            elif c1 == 0:
                val = matrix[r2][c2] - matrix[r1 - 1][c2]
            else:
                val = matrix[r2][c2] - (matrix[r1 - 1][c2] + matrix[r2][c1 - 1]) + matrix[r1 - 1][c1 - 1]
        return val

