class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        n, m = len(A), len(B)
        l, r = 0, m - 1

        diff = float('inf')
        ans = []
        ind = -1

        while l < n and r >= 0:
            cur_dif = A[l] + B[r] - C
            if abs(cur_dif) < diff:
                diff = abs(cur_dif)
                ans = [A[l], B[r]]
                ind = l
                # minimising r for the same l and diff
            elif abs(cur_dif) == diff:
                if l == ind:
                    ans = [A[l], B[r]]
            if A[l] + B[r] >= C:
                r -= 1
            else:
                l += 1

        return ans

        # TC: O(N); SC: O(N)