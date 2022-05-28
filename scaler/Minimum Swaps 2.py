class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        ans = 0
        for index in range(len(A)):
            a, b = A[index], A[A[index]]
            while A[index] != index:
                A[A[index]], A[index] = A[index], A[A[index]]
                ans += 1
        return ans