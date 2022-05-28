class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0
        A.sort()
        for i in range(len(A) - 1):
            if abs(A[i] - A[i + 1]) > B:
                count += 1

        return count