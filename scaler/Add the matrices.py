class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        rows = len(A)
        columns = len(A[0])
        array = [[A[row][col] for col in range(columns)] for row in range(rows)]
        for row in range(rows):
            for column in range(columns):
                array[row][column] = A[row][column] + B[row][column]
        return array

