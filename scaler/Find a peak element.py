class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        if n == 1:
            return A[0]
        elif A[0] >= A[1]:
            return A[0]
        elif A[-1] >= A[-2]:
            return A[-1]

        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2
            if A[mid] >= A[mid + 1] and A[mid] >= A[mid - 1]:
                return A[mid]
            elif A[mid] >= A[mid - 1]:
                low = mid + 1
            else:
                high = mid - 1

        # TC: O(logN); SC: O(1)
