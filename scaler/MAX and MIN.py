class Solution:
    # @param A : list of integers
    # @return an integer
    def nsl(self, A):
        stack = []
        n = len(A)
        ret = [-1] * n

        for ind in range(n):
            while stack and A[stack[-1]] >= A[ind]:
                stack.pop()
            if stack:
                ret[ind] = stack[-1]
            stack.append(ind)

        return ret

    def nsr(self, A):
        stack = []
        n = len(A)
        ret = [n] * n

        for ind in range(n - 1, -1, -1):
            while stack and A[stack[-1]] >= A[ind]:
                stack.pop()
            if stack:
                ret[ind] = stack[-1]
            stack.append(ind)

        return ret

    def ngl(self, A):
        stack = []
        n = len(A)
        ret = [-1] * n

        for ind in range(n):
            while stack and A[stack[-1]] <= A[ind]:
                stack.pop()
            if stack:
                ret[ind] = stack[-1]
            stack.append(ind)

        return ret

    def ngr(self, A):
        stack = []
        n = len(A)
        ret = [n] * n

        for ind in range(n - 1, -1, -1):
            while stack and A[stack[-1]] <= A[ind]:
                stack.pop()
            if stack:
                ret[ind] = stack[-1]
            stack.append(ind)

        return ret

    def solve(self, A):
        maxx = 0
        minn = 0

        nsl = self.nsl(A)
        nsr = self.nsr(A)
        ngl = self.ngl(A)
        ngr = self.ngr(A)

        mod = pow(10, 9) + 7

        for ind, ele in enumerate(A):
            NSL = nsl[ind]
            NSR = nsr[ind]
            NGL = ngl[ind]
            NGR = ngr[ind]

            minn += ((ind - NSL) * (NSR - ind) * ele) % mod
            maxx += ((ind - NGL) * (NGR - ind) * ele) % mod

        return (maxx - minn) % mod

    # TC: O(N); SC: O(N)