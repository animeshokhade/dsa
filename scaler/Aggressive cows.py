class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def check(self, A, B, mid, n):
        j = 0
        cow = 1
        for i in range(1, n):
            if A[i] - A[j] >= mid:
                cow += 1
                j = i
        return cow >= B

    def solve(self, A, B):
        # to arrange the stalls by their location
        # each array element represents the location of the stall
        A.sort()
        n = len(A)

        low = float('inf')
        for index in range(n - 1):
            low = min(low, A[index + 1] - A[index])
        high = A[-1] - A[0]
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if self.check(A, B, mid, n):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans

        # R = (A[-1] - A[0]) - min_diff + 1
        # TC: O(NlogR); SC: O(1)
