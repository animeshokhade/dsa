class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if A == 1:
            return 0
        parent = self.solve(A - 1, (B + 1) // 2)
        if B & 1: return parent
        return parent^1

# alternative approach

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        # Base Condition
        if A == 1:
            return 0

        # Recursive relation
        mid = 2 ** (A - 2)
        if B <= mid:
            return self.solve(A - 1, B)
        else:
            return 1 - self.solve(A - 1, B - mid)

# alternative approach

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if A == 1: return 0
        parent = self.solve(A - 1, B // 2 + B % 2)
        isAOdd = B % 2 == 1
        if parent == 1:
            return 1 if isAOdd else 0
        else:
            return 0 if isAOdd else 1