# hashing

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        lookup = set()
        p = 0
        for a in A:
            if B - a in lookup:
                p += 1
            lookup.add(a)
        return p

    # TC: O(N); SC: O(N)

# optimisation - 2 pointers

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        p1 = 0
        p2 = n - 1
        ans = 0

        while p1 < p2:
            pr_sum = A[p1] + A[p2]
            if pr_sum > B:
                p2 -= 1
            elif pr_sum < B:
                p1 += 1
            else:
                ans += 1
                p1 += 1
                p2 -= 1

        return ans

    # TC: O(N); SC: O(1)
