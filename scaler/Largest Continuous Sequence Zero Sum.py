class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        PS = dict()
        ans = list()
        summ = 0
        base = -1
        for index, num in enumerate(A):
            summ += num
            if summ in PS:
                if index - PS[summ] > base:
                    base = index - PS[summ]
                    ans = A[PS[summ] + 1:index + 1]
            elif summ == 0:
                if index + 1 > base:
                    base = index + 1
                    ans = A[:index + 1]
            else:
                PS[summ] = index
        return ans

# alternative approach

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        PS = dict()
        ans = list()
        summ = 0
        cmpp = -1
        for index, num in enumerate(A):
            summ += num
            if summ in PS:
                if index - PS[summ] > cmpp:
                    cmpp = index - PS[summ]
                    ans = A[PS[summ] + 1:index + 1]
            elif summ == 0:
                if index + 1 > cmpp:
                    cmpp = index + 1
                    ans = A[:index + 1]
                elif index + 1 == cmpp:
                    pass
            else:
                PS[summ] = index
        return ans

# alternate approach

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        ps = {}

        psa = []
        summ = 0
        i = 0
        is_zero = False

        for ind, ele in enumerate(A):
            summ += ele
            if summ == 0:
                i = ind
                is_zero = True
            if summ in ps:
                ps[summ] += 1
            else:
                ps[summ] = 1
            psa.append(summ)

        key_max = max(ps, key=lambda x: ps[x])

        n = len(A)
        l, r = 0, n - 1

        while True:
            if psa[l] != key_max:
                l += 1
            elif psa[r] != key_max:
                r -= 1
            else: break

        if is_zero:
            if i + 1 >= r + l - 1:
                return A[:i + 1]
        return A[l + 1:r + 1]

# alternate approach

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        ans = []

        lkp = {}
        summ = 0
        ps = []

        # generate prefix sum array
        for ind, ele in enumerate(A):
            summ += ele
            ps.append(summ)

        # if 0 or repeating element in ps => update ans
        n = len(ps)
        for ind in range(n):
            if ps[ind] == 0:
                if ind + 1 > len(ans):
                    ans = A[:ind + 1]
            elif ps[ind] in lkp:
                prev = lkp[ps[ind]]
                if ind - prev > len(ans):
                    ans = A[prev + 1:ind + 1]
            else:
                lkp[ps[ind]] = ind

        return ans

# TC: O(N); SC: O(N)







