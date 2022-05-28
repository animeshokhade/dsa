class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if (len(A) == 1):
            return -1
        first, second = A[0], 0
        for index in range(1, len(A)):
            if A[index] >= first:
                second = first
                first = A[index]
            elif (A[index] < first) and (A[index] > second):
                second = A[index]
        if second == 0:
            return -1
        return second

