class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        ans = 0
        for row in range(len(A)):
            for col in range(len(A[0])):
                ans += (row + 1) * (col + 1) * (len(A) - row) * (len(A) - col) * A[row][col]
        return ans

# alternate approach

