class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        l1, l2, l3 = len(A), len(B), len(C)
        p1, p2, p3 = 0, 0, 0
        min_max = float('inf')
        maxx = float('-inf')

        while p1 < l1 and p2 < l2 and p3 < l3:
            max1 = abs(A[p1] - B[p2])
            max2 = abs(B[p2] - C[p3])
            max3 = abs(C[p3] - A[p1])

            maxx = max(max1, max2, max3)
            min_max = min(min_max, maxx)

            if maxx == max1:
                if A[p1] > B[p2]:
                    p2 += 1
                else:
                    p1 += 1
            elif maxx == max2:
                if B[p2] > C[p3]:
                    p3 += 1
                else:
                    p2 += 1
            elif maxx == max3:
                if C[p3] > A[p1]:
                    p1 += 1
                else:
                    p3 += 1

        return min_max

        # TC: O(N); SC: O(1)


# clean

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        l1, l2, l3 = len(A), len(B), len(C)
        p1, p2, p3 = 0, 0, 0
        min_max = float('inf')

        while p1 < l1 and p2 < l2 and p3 < l3:
            tmp_min = min(A[p1], B[p2], C[p3])

            tmp_max = max(A[p1], B[p2], C[p3])

            min_max = min(min_max, tmp_max - tmp_min)

            # the minimum value of min_max is 0
            # so if we get it during the operation
            # we can break the loop

            if min_max == 0: return min_max

            if tmp_min == A[p1]:
                p1 += 1
            elif tmp_min == B[p2]:
                p2 += 1
            else:
                p3 += 1

        return min_max

    # TC: O(N); SC: O(1)
