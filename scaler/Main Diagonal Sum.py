class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        summ = 0
        for index in range(n):
            summ += A[index][index]
        return summ

# alternative approach

class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        row = len(A)
        col = len(A[0])
        summ = 0
        for r in range(row):
            for c in range(col):
                if r == c:
                    summ += A[r][c]
        return summ
