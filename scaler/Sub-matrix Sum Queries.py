class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E):
        r, c = len(A) + 1, len(A[0]) + 1

        PS = [[0] * c for _ in range(r)]

        # column sum
        for row in range(1, r):
            for col in range(1, c):
                PS[row][col] += PS[row][col - 1] + A[row - 1][col - 1]

                # row sum
        for col in range(1, c):
            for row in range(1, r):
                PS[row][col] += PS[row - 1][col]

        query = len(B)
        ans = []
        mod = pow(10, 9) + 7
        matrixSum = 0

        for q in range(query):
            matrixSum = PS[D[q]][E[q]] - PS[D[q]][C[q] - 1] - PS[B[q] - 1][E[q]] + PS[B[q] - 1][C[q] - 1]
            ans.append(matrixSum % mod)
        return ans

# alternate approach

class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E):
        PS = [[0 for x in range(len(A[0]))] for y in range(len(A))]
        for row in range(len(A)):
            for col in range(len(A[0])):
                if col != 0:
                    PS[row][col] += A[row][col] + PS[row][col - 1]
                else:
                    PS[row][col] += A[row][col]
        for col in range(len(A[0])):
            for row in range(len(A)):
                if row != 0:
                    PS[row][col] = PS[row][col] + PS[row - 1][col]
                else:
                    PS[row][col] = PS[row][col]
        query = len(B)
        ans = []
        mod = pow(10, 9) + 7
        matrixSum = 0
        for q in range(query):
            topLeft = [B[q] - 1, C[q] - 1]
            bottomRight = [D[q] - 1, E[q] - 1]
            if B[q] == 1 and C[q] == 1:
                matrixSum = PS[bottomRight[0]][bottomRight[1]]
            elif B[q] != 1 and C[q] != 1:
                matrixSum = PS[bottomRight[0]][bottomRight[1]] - PS[bottomRight[0]][topLeft[1] - 1] - PS[topLeft[0] - 1][bottomRight[1]] + PS[topLeft[0] - 1][topLeft[1] - 1]
            elif B[q] == 1:
                matrixSum = PS[bottomRight[0]][bottomRight[1]] - PS[bottomRight[0]][topLeft[1] - 1]
            elif C[q] == 1:
                matrixSum = PS[bottomRight[0]][bottomRight[1]] - PS[topLeft[0] - 1][bottomRight[1]]
            ans.append(matrixSum % mod)
        return ans

# alternate approach

class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E):
        n = len(A)
        m = len(A[0])
        arr = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(m):
            arr[1][i + 1] = A[0][i]

            # Do column wise sum
        for i in range(1, n, 1):
            for j in range(0, m, 1):
                arr[i + 1][j + 1] = A[i][j] + arr[i][j + 1]

                # Do row wise sum
        for i in range(0, n, 1):
            for j in range(1, m, 1):
                arr[i + 1][j + 1] += arr[i + 1][j]

        ans = []
        q = len(B)
        for i in range(q):
            x1 = B[i]
            y1 = C[i]
            x2 = D[i]
            y2 = E[i]
            val = arr[x2][y2] - arr[x2][y1 - 1] - arr[x1 - 1][y2] + arr[x1 - 1][y1 - 1]
            # while(val < 0):
            # val += 1000000007
            val = val % 1000000007;
            ans.append(val)
        return ans

