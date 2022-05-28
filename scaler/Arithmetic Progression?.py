class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A = sorted(A)
        n = len(A)
        for i in range(1, n - 1):
            if A[i] - A[i - 1] != A[i + 1] - A[i]:
                return 0
        return 1

