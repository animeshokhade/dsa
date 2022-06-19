from collections import Counter


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        mod = pow(10, 9) + 7
        ans = 0

        x = Counter(A)
        y = Counter(B)

        n = len(A)

        for i in range(n):
            ans += (x[A[i]] - 1) * (y[B[i]] - 1)

        return ans % mod

        # TC: O(N); SC: O(N)
