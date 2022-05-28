class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        ans = 0
        for a in A:
            ans ^= a
        return ans
