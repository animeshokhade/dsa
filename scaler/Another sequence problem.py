class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 0 or A == 1: return 1
        if A == 2: return 2
        return self.solve(A - 1) + self.solve(A - 2) + self.solve(A - 3) + A

'''
Standard Recursion: 
    TC: O(3^N)
    SC: Depth of the Recursion Tree

DP: 
    TC: O(N)
    SC: O(N)
'''

# alternate approach

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 0 or A == 1: return 1
        if A == 2: return 2
        return self.solve(A - 1) + self.solve(A - 2) + self.solve(A - 3) + A

# alternate approach

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 0: return 1
        if A == 1: return 1
        if A == 2: return 2
        return self.solve(A - 1) + self.solve(A - 2) + self.solve(A - 3) + A
