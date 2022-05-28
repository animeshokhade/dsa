class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        num = int(A)
        if num % 8 == 0:
            return 1
        return 0

