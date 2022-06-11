class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        low = 0
        high = min(A)
        ceil = 0
        while low <= high:
            mid = (low + high) // 2
            if self.check(A, B, mid):
                low = mid + 1
                ceil = mid
            else:
                high = mid - 1
        return ceil

    def check(self, A, B, mid):
        offices = 0
        for people in A:
            if mid == 0:
                offices += people
            else:
                offices += people // mid
        return offices >= B

    # high = min(A), as it is the maximum possible minima
    # for this BS, mid represents a particular population for
    # which we calculate number of offices per city (A[i] // mid)
    # if the count of offices is >= B, then we search right,
    # discard left and update ceil. Else search left.

    # Range(R) = log(min(A))
    # TC: O(N + NlogR) => O(NlogR); SC: O(1)
