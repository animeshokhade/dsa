class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        for index, i in enumerate(A):
            add = i
            for j in A[index + 1:]:
                add += j
                if add == B:
                    return 1
                add -= j
        return 0

