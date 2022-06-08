class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def gcd(self, B, C):
        if C == 0:
            return B
        return self.gcd(C, B % C)

    def magic_num_count(self, A, B, C, LCM):
        return (A // B) + (A // C) - (A // LCM)

    def solve(self, A, B, C):
        mod = 1000000007
        GCD = self.gcd(B, C)
        LCM = (B * C) // GCD

        # binary search
        low = 1

        # the largest value for which we can find the smallest Ath
        # magical number is the Ath multiple of the smaller
        # of B or C.
        high = min(B, C) * A
        floor = 0
        while low <= high:
            mid = (low + high) // 2
            magic = self.magic_num_count(mid, B, C, LCM)
            if magic >= A:
                floor = mid
                high = mid - 1
            else:
                low = mid + 1

        return floor % mod

        # TC: O(log(min(B, C) * A)); SC: O(log(max(B, C)))
    # Space complexity is minimal, but it is there due to GCD recursive calculation

