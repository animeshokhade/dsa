class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        x = 0
        # iterate from the rightmost bits of A to find the set bit and mark
        # it as 0 as this would make number as minimum as possible

        for i in range(30, -1, -1):
            if B == 0:
                return x
            if (1 << i) & A:
                x |= 1 << i
                B -= 1

        # if number of set bits is less than B then start iterating from leftmost
        # side and mark zeros with 1

        for i in range(31):
            if B == 0:
                return x
            if (1 << i) & x == 0:
                x |= 1 << i
                B -= 1

        return x

