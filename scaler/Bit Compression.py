class Solution:
    # @param A : list of integers
    # @return an integer
    def compressBits(self, A):
        ans = 0
        for i in A:
            ans ^= i
        return ans