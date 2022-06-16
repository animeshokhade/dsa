class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        n = len(A)

        if n == 1: return 0

        mx_area = float('-inf')
        p1 = 0
        p2 = n - 1

        while p1 < p2:
            w = p2 - p1
            h = min(A[p1], A[p2])
            mx_area = max(mx_area, w * h)
            if A[p2] < A[p1]:
                p2 -= 1
            else:
                p1 += 1

        return mx_area

    # TC: O(N); SC: O(1)