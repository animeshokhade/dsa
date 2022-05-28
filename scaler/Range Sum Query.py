class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
     # @return an list of long
    def rangeSum(self, A, B):
        add = 0
        a, b = len(A), len(B)
        prefixSum = [0]
        for number in A:
            add += number
            prefixSum.append(add)
        solution = []
        for i in range(b):
            startIndex = B[i][0] - 1
            endIndex = B[i][1]
            add = prefixSum[endIndex] - prefixSum[startIndex]
            solution.append(add)
        return solution


# alternative approach

class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
     # @return an list of long
    def rangeSum(self, A, B):
        add = 0
        prefixSum = []
        for number in A:
            add += number
            prefixSum.append(add)
        iterations = len(B)
        solution = []
        for i in range(iterations):
            startIndex = B[i][0] - 1
            endIndex = B[i][1] - 1
            if (endIndex == 0) or (startIndex == 0):
                add = prefixSum[endIndex]
            elif startIndex == endIndex:
                add = A[startIndex]
            else:
                add = prefixSum[endIndex] - prefixSum[startIndex - 1]
            solution.append(add)
        return solution


