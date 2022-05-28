class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        ans = []
        for index, number in enumerate(A):
            summ = 0
            for end in range(index, N):
                summ += A[end]
                ans.append(summ)
        count_subarray = 0
        for number in ans:
            if number < B:
                count_subarray += 1
        return count_subarray

