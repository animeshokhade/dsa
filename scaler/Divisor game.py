import math
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        gcd = math.gcd(B, C)
        LCM = (B * C) // gcd
        return A // LCM


