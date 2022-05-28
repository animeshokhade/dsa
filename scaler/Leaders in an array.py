class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        maxx = A[-1]
        N = len(A)
        ans = [maxx]
        for index in range(N - 2, -1, -1):
            if A[index] >= maxx:
                maxx = A[index]
                ans.append(maxx)
        return ans
