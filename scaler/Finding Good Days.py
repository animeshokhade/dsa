class Solution:
    # @param A : integer
    # @return an integer
    def countSetBits(self, A):
        if not A:
            return 0
        A = A & (A - 1)
        return 1 + self.countSetBits(A)

    def solve(self, A):
        return self.countSetBits(A)

# alternative approach

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        q, r = A, 0
        count = 0
        while q >= 1:
            r = q % 2
            if r == 1:
                count += 1
            q //= 2

        return count

# alternative approach

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        ans = 0
        while A:
            if (A & 1 == 1):
                ans += 1
            A >>= 1
        return ans
