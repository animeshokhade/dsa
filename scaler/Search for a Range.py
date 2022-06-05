class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def floor(self, A, B, n, low, high):
        # first occurence
        while low <= high:
            mid = (low + high) // 2
            if A[mid] == B and (mid == 0 or B > A[mid - 1]):
                return mid
            elif A[mid] < B:
                low = mid + 1
            else:
                high = mid - 1

        return -1

    def ceil(self, A, B, n, low, high):
        # last occurence
        while low <= high:
            mid = (low + high) // 2
            if A[mid] == B and (mid == n - 1 or B < A[mid + 1]):
                return mid
            elif A[mid] > B:
                high = mid - 1
            else:
                low = mid + 1

        return -1

    def searchRange(self, A, B):
        n = len(A)
        low = 0
        high = n - 1

        floor = self.floor(A, B, n, low, high)
        ceil = self.ceil(A, B, n, low, high)

        return [floor, ceil]


'''
TC: O(logN)
SC: O(1)
'''

