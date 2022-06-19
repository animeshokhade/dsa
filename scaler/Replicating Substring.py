from collections import Counter
class Solution:
    # @param A : integer
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        if A == 1:
            return 1

        if A > len(B):
            return -1

        freq = Counter(B)

        for key, val in freq.items():
            if val % A != 0:
                return -1

        return 1

        # TC: O(N); SC: O(N)