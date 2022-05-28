class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        ans = 0
        N = len(A)
        for index, number in enumerate(A):
            summ = 0
            for end in range(index, N):
                summ += A[end]
                subarray_length = end - index + 1
                if subarray_length % 2 == 0:
                    if summ < B:
                        ans += 1
                elif subarray_length % 2 == 1:
                    if summ > B:
                        ans += 1
        return ans
