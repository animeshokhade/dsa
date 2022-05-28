class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        summ = float('-inf')
        ans = max(A)
        if ans < 0:
            return ans

        for index, number in enumerate(A):
            summ += number
            if summ < 0:
                summ = 0
            ans = max(ans, summ)

        return ans

# alternative approach

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        max_so_far = max_ending_here = A[0]
        N = len(A)
        for index in range(1, N):
            max_ending_here = max(max_ending_here + A[index], A[index])
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far