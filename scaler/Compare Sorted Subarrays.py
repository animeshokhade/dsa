import random


class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers

    # A can be max -> 10^5 which is approx 2^16
    inf = 1 << 17
    Hash = {}

    # rand46 along with set_hash will hash the array elements
    # to a unique set of values, so that the sum algorithm
    # can be applied without encountering collisions.

    def rand46(self):
        ret = random.randint(0, self.inf)
        return ret

    def set_hash(self, A):
        n = len(A)
        for i in range(n):
            # avoiding duplicates
            if self.Hash.get(A[i]) == None:
                self.Hash[A[i]] = self.rand46()

    def solve(self, A, B):
        n = len(A)
        self.set_hash(A)

        ps = [self.Hash[A[0]]]

        for i in range(1, n):
            cur_sum = ps[i - 1] + self.Hash[A[i]]
            ps.append(cur_sum)

        q = len(B)
        ans = []

        s1, s2 = 0, 0

        for i in range(q):
            if B[i][0] > 0:
                s1 = ps[B[i][1]] - ps[B[i][0] - 1]
            else:
                s1 = ps[B[i][1]]
            if B[i][2] > 0:
                s2 = ps[B[i][3]] - ps[B[i][2] - 1]
            else:
                s2 = ps[B[i][3]]

            if s1 == s2:
                ans.append(1)
            else:
                ans.append(0)

        return ans

        # TC: O(N + Q); SC: O(N) 