class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        ans = [[0 for num in range(len(A))] for num in range(2 * len(A) - 1)]
        i = 0
        for c in range(len(A)):
            j = 0
            r = 0
            while ((r < len(A)) and (c >= 0)):
                ans[i][j] = A[r][c]
                j += 1
                r += 1
                c -= 1
            i += 1

        for r in range(1, len(A)):
            c = len(A) - 1
            j = 0
            while ((r < len(A)) and (c >= 0)):
                ans[i][j] = A[r][c]
                c -= 1
                r += 1
                j += 1
            i += 1
        return ans
