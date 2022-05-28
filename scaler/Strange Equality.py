import math

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        MSB = int(math.log(A, 2)) + 1
        xor = (1 << MSB) - 1
        return xor ^ A + (1 << MSB)

# alternate approach

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        ans = 0
        bitCount = 0
        while A:
            if not A & 1:
                ans += 1 << bitCount
            bitCount += 1
            A >>= 1
        return ans + (1 << bitCount)

