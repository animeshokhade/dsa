class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        low = 0
        high = A - 1
        ceil = high

        # edge cases
        if C < B[0]:
            return B[0]
        if C > B[-1]:
            return -1

        # binary search
        while low <= high:
            mid = (low + high) // 2
            if B[mid] == C:
                return B[mid]
            elif B[mid] > C:
                ceil = B[mid]
                high = mid - 1
            else:
                low = mid + 1

        return ceil

        '''
        TC: O(logN)
        SC: O(1)
        '''

# clean code
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        low = 0
        high = A - 1

        # giving a default value of -1 takes care of the edge case
        # in which the target might be greater than the max element in the
        # search space
        ceil = -1

        # binary search
        while low <= high:
            mid = (low + high) // 2
            if B[mid] >= C:

                # the ceil will update for the edge case in which
                # the target is smaller than the minimum element
                # in the search space
                ceil = B[mid]
                high = mid - 1
            else:
                low = mid + 1

        return ceil
        # TC: O(logN); SC: O(1)