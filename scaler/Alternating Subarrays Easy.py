class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        ans = []
        N = len(A)
        size = 2*B + 1
        binaryType1 = [0] * size
        binaryType2 = [0] * size
        for index in range(size):
            if index % 2 == 0:
                binaryType1[index] = 1
            elif index % 2 == 1:
                binaryType2[index] = 1
        for index in range(0, N - size + 1):
            subArray = A[index:index + size]
            if (subArray == binaryType1) or (subArray == binaryType2):
                ans.append(index + B)
        return ans