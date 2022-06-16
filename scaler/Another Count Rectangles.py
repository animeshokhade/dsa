class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        l, r = 0, n - 1
        cnt = 0

        while l < n and r >= 0:
            area = A[l] * A[r]
            if area < B:
                cnt += r + 1
                l += 1
            else:
                r -= 1

        return cnt % 1000000007

    # TC: O(N); SC: O(1)


# clean

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        l, r = 0, n - 1
        cnt = 0

        while l <= r:
            area = A[l] * A[r]
            if area < B:
                cnt += 2 * (r - l) + 1
                l += 1
            else:
                r -= 1

        return cnt % 1000000007

    # TC: O(N); SC: O(1)
