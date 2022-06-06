# In this problem, both minimum and maximum will act as
# pivots. If there are duplicates, then both the sub-arrays
# won't be monotonous and so a linear search solution would
# be the optimised one.

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        n = len(A)
        low = 0
        high = n - 1

        # conditional binary search
        while low <= high:
            mid = (low + high) // 2
            if A[mid] == B:
                return mid

            # check if the left subarray is monotonically increasing
            elif A[mid] > A[low]:
                # check if the target lies in the left subarray
                if A[low] <= B < A[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            # check if the right subarray is monotonically increasing
            else:
                # check if the target lies in the right subarray
                if A[mid] < B <= A[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

        # TC: O(logN); SC: O(1)

