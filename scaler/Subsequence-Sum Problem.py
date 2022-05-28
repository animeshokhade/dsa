class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def subsetSum (self, Array, startingIndex, Sum):
        # Base Condition
        if Sum == 0:
            return 1

        elif len(Array) - startingIndex == 1:
            if Array[startingIndex] == Sum:
                return 1
            else:
                return 0

        result1 = self.subsetSum(Array, startingIndex + 1, Sum - Array[startingIndex])
        result2 = self.subsetSum(Array, startingIndex + 1, Sum)
        return result1 or result2

    def solve(self, A, B):
        return self.subsetSum(A, 0, B)

# alternative approach

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        for i in range(1<<n):
            s = 0
            for j in range(n):
                if (1<<j)&i:
                    s += A[j]
            if s==B:
                return 1
        return 0
