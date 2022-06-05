class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        n = len(A)
        left = 0
        right = n - 1

        # edge cases
        if B > A[-1]:
            return n

        if B < A[0]:
            return 0

        # binary search
        while left <= right:
            mid = (left + right) // 2

            # discarding left
            if A[mid] < B:
                left = mid + 1

            # discarding right
            elif A[mid] > B:
                right = mid - 1

            elif A[mid] == B:
                return mid

        return left

    '''
    TC: O(logN)
    SC: O(1)
    '''

# library function
from bisect import bisect_left
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        return bisect_left(A, B)

    '''
    TC: O(logN)
    SC: O(1)
    '''




