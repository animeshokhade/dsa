# converting 2D Matrix to 1D Matrix -> suboptimal

import numpy as np

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        A = np.array(A)
        A = A.ravel()

        # binary search
        n = len(A)
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2
            if A[mid] == B:
                return 1
            elif A[mid] > B:
                high = mid - 1
            else:
                low = mid + 1
        return 0

        # N => Number of elements TC: O(N); SC: O(1)

# optimised

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        r = len(A)
        c = len(A[0])
        low = 0
        high = r * c - 1

        # binary search
        while low <= high:
            mid = (low + high) // 2
            # using mod we can map mid into the range 0 to c - 1
            col = mid % c
            # every row would be a multiple of the total columns and
            # hence a division by c would render the row index
            row = mid // c
            if A[row][col] == B:
                return 1
            elif A[row][col] < B:
                low = mid + 1
            else:
                high = mid - 1

        return 0

        # TC: O(log(MN)); SC: O(1)



