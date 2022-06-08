import numpy as np


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        A = np.array(A)
        A = A.ravel()
        A.sort()
        n = len(A)
        if n & 1 == 0:
            median = (A[n // 2] + A[n // 2 - 1]) // 2
        else:
            median = A[n // 2]
        return median

        # TC: O(N * M + (N * M)log(N * M)); SC: O(N * M)


# optimised

from bisect import bisect_right


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        row = len(A)
        col = len(A[0])

        # this is where the median should be placed if the
        # matrix was a sorted 1D array
        desired_count = (row * col) // 2
        min_ele, max_ele = self.matrix_range(A)
        return self.binary_search(A, min_ele, max_ele, desired_count)

    def matrix_range(self, matrix):
        min_ele = float('inf')
        max_ele = float('-inf')

        for row in matrix:
            min_ele = min(min_ele, row[0])
            max_ele = max(max_ele, row[-1])

        return min_ele, max_ele

    def binary_search(self, matrix, minimum, maximum, median_index):
        low = minimum
        high = maximum
        while low < high:
            mid = (low + high) // 2
            count = 0
            for row in matrix:
                count += bisect_right(row, mid)
                # bisect_right returns the rightmost index
                # at which the element can be inserted without
                # disturbing the sort order

            if count <= median_index:
                low = mid + 1
            else:
                high = mid  # since we want the rightmost index, we won't do -1
        return low  # low would act as a ceil in this scenario

    # TC: O(N + log(max_ele - min_ele) * N * logM) => O(log(max_ele - min_ele) * N * logM)
    # SC: O(1)