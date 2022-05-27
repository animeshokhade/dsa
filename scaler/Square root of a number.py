class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        import math
        a = int(math.sqrt(A))
        if a * a == A:
            return a
        return -1

    