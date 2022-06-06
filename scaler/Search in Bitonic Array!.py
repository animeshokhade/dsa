class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def bitonic(self, A, n, low, high):
        while low <= high:
            mid = (low + high) // 2

            # bitonic would be the greatest element
            # which in a mountain array means
            # that it would be greater than both its
            # adjacent element and the only
            # element to satisfy this condition.
            if mid > 0 and mid < n - 1 and A[mid] > A[mid - 1] and A[mid] > A[mid + 1]:
                return mid

                # check if mid is in the ascending subarray => go right
            elif A[mid - 1] < A[mid] < A[mid + 1]:
                low = mid + 1

            # mid is in the descending subarray => go left
            else:
                high = mid - 1

    def binarySearch(self, A, B, low, high, reverse):
        if reverse:  # descending array
            while low >= high:
                mid = (low + high) // 2
                if A[mid] == B:
                    return mid
                elif A[mid] < B:
                    low = mid - 1
                else:
                    high = mid + 1
        else:  # ascending array
            while low <= high:
                mid = (low + high) // 2
                if A[mid] == B:
                    return mid
                elif A[mid] < B:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

    def solve(self, A, B):
        n = len(A)
        b = self.bitonic(A, n, 0, n - 1)
        if A[b] == B:
            return b
        left = self.binarySearch(A, B, 0, b, False)
        if left != -1:
            return left
        right = self.binarySearch(A, B, n - 1, b + 1, True)
        if right != -1:
            return right
        return -1

        # TC: O(logN); SC: O(1)
