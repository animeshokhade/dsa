from collections import OrderedDict


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        AA = OrderedDict()

        for a in A:
            if a in AA:
                AA[a] += 1
            else:
                AA[a] = 1

        BB = OrderedDict()

        for b in B:
            if b in BB:
                BB[b] += 1
            else:
                BB[b] = 1

        ret = []

        for key in BB:
            if key in AA:
                val = AA[key]
                while val:
                    ret.append(key)
                    val -= 1
                del AA[key]

        aa = sorted(AA.items())

        for key, val in aa:
            while val:
                ret.append(key)
                val -= 1

        return ret

        # TC: O(NlogN); SC: O(N)
