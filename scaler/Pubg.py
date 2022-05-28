class Solution:
    # @param A : list of integers
    # @return an integer
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def solve(self, A):
        minHealth = 0
        for ele in A:
            minHealth = self.gcd(minHealth, ele)
        return minHealth

