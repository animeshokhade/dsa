class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def check(self, A, k, B):
        # finding the first window sum
        window_sum = 0
        n = len(A)

        # first window
        for _ in range(k):
            window_sum += A[_]

            # sliding window
        for _ in range(k, n):
            if window_sum > B:
                return False
            window_sum -= A[_ - k]
            window_sum += A[_]

        # to check for the last window_sum update
        if window_sum > B:
            return False
        return True

    def solve(self, A, B):
        n = len(A)
        low = 1
        high = n
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if self.check(A, mid, B):
                low = mid + 1
                ans = mid
            else:
                high = mid - 1
        return ans

        # TC: O(NlogN); SC: O(1)

