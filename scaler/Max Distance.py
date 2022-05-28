class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        indexVal = []

        for index, number in enumerate(A):
            indexVal.append([number, index])

        indexVal.sort()

        maxIndex = indexVal[-1][1]
        ans = 0
        for index in range(len(A) - 2, -1, -1):
            ans = max(ans, maxIndex - indexVal[index][1])
            maxIndex = max(maxIndex, indexVal[index][1])

        return ans

