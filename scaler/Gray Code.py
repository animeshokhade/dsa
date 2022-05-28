class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        if A == 1:
            return [0, 1]
        first_half = self.grayCode(A - 1)
        second_half = [(1 << (A - 1)) + first_half[i] for i in range(len(first_half) - 1, -1, -1)]
        return first_half + second_half

# alternate approach

class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        if A==1:
            return [0, 1]
        res = self.grayCode(A-1)
        msb = 2**(A-1)
        for i in range(len(res)-1, -1, -1):
            res.append(msb+res[i])
        return res



