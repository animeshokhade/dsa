class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        l1, l2, l3 = len(A), len(B), len(C)

        p1, p2, p3 = 0, 0, 0

        min_dif = float('inf')

        while p1 < l1 and p2 < l2 and p3 < l3:
            tmp_max = max(A[p1], B[p2], C[p3])
            tmp_min = min(A[p1], B[p2], C[p3])

            min_dif = min(min_dif, tmp_max - tmp_min)

            if tmp_min == A[p1]:
                p1 += 1
            elif tmp_min == B[p2]:
                p2 += 1
            else:
                p3 += 1

        return min_dif

        # TC: O(N); SC: O(1)
