class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        setBit = 0
        while A:
            if A & 1:
                setBit += 1
            A >>= 1

        return setBit

# alternative approach

class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        q, r = A, 0
        count = 0
        while q > 1:
            if q % 2 == 1:
                count += 1
            q //= 2
        return count + 1


