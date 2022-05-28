class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        N = len(A)
        if N % 2 == 1:
            return 'NO'
        elif (A[0] % 2 == 0) and (A[-1] % 2 == 0):
            return 'YES'
        return 'NO'