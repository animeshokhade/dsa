class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        low = 0
        high = n - 1

        # boundary conditions
        if high == 0:
            return A[0]

        # the two conditions below are necessary because,
        # the algorithm based on pattern of indices will only
        # work if the element occuring only once is not at the edge.
        if A[0] != A[1]:
            return A[0]
        if A[-1] != A[-2]:
            return A[-1]

        # binary search
        while low <= high:
            mid = (low + high) // 2
            if A[mid] != A[mid + 1] and A[mid] != A[mid - 1]:
                return A[mid]
            # conditions in which we must discard the right searchspace
            elif (mid & 1 == 0 and (A[mid] == A[mid - 1])) or (mid & 1 == 1 and (A[mid] == A[mid + 1])):
                high = mid - 1
            # discard the left searchspace
            else:
                low = mid + 1

        # TC: O(logN); SC: O(1)
