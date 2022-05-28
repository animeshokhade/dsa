class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        maxSum, minSum = float('-inf'), float('inf')
        maxDiff, minDiff = float('-inf'), float('inf')

        for i in range(len(A)):
            maxSum = max(maxSum, A[i] + i)
            minSum = min(minSum, A[i] + i)
            maxDiff = max(maxDiff, A[i] - i)
            minDiff = min(minDiff, A[i] - i)

        return max(abs(maxSum - minSum), abs(maxDiff - minDiff))

# alternative approach

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        indexSum = [num + index for index, num in enumerate(A)]
        indexDiff = [num - index for index, num in enumerate(A)]

        ans = max(abs(max(indexSum) - min(indexSum)), abs(max(indexDiff) - min(indexDiff)))
        return ans

