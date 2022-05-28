class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        product = 1
        iterations = len(A)
        for index in range(iterations):
            product *= A[index]

        newA = []
        for number in A:
            temp = product // number
            newA.append(temp)

        return newA

