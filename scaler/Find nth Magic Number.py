class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        power = 1
        ans = 0

        while A:
            power *= 5
            if A & 1:
                ans += power

            A >>= 1

        return ans

# alternative approach

