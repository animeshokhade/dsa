class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        subArray, ans_index = A[:B], 0
        min_sum = new_sum = sum(subArray)
        iterations = N - B + 1
        for index in range(1, iterations):
            new_sum = new_sum - A[index - 1] + A[index + B - 1]
            if new_sum < min_sum:
                ans_index = index
                min_sum = new_sum

        return ans_index




