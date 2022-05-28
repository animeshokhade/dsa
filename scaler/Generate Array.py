class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        for index, ele in enumerate(A):
            bitIndex = 0
            while not ele & 1:
                bitIndex += 1
                ele >>= 1
            A[index] = 1 << bitIndex
        return A           