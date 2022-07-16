class Solution:
    # @param A : list of list of integers
    # @return an integer
    def area(self, A):
        stack = []
        n = len(A)
        rec = 0
        cur = 0
        area = 0

        ind = 0
        while ind < n:
            if not stack or A[stack[-1]] < A[ind]:
                stack.append(ind)
                ind += 1
            else:
                cur = stack.pop()
                area = A[cur] * (ind if not stack else ind - stack[-1] - 1)
                rec = max(rec, area)

        while stack:
            cur = stack.pop()
            area = A[cur] * (ind if not stack else ind - stack[-1] - 1)
            rec = max(rec, area)

        return rec

    def solve(self, A):
        # process the input array
        r = len(A)
        c = len(A[0])

        for row in range(1, r):
            for col in range(c):
                if A[row][col]:
                    A[row][col] += A[row - 1][col]

        ret = 0

        for row in range(r):
            area = self.area(A[row])
            ret = max(ret, area)

        return ret

        # TC: O(rows * cols); SC: O(cols)

# clean

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def area(self, A):
        A.append(0)
        stack = [-1]
        n = len(A)
        rec = 0
        cur = 0
        area = 0

        for ind, ele in enumerate(A):
            while stack and A[stack[-1]] >= ele:
                cur = stack.pop()
                if stack:
                    area = A[cur] * (ind - stack[-1] - 1)
                rec = max(rec, area)
            stack.append(ind)

        return rec

    def solve(self, A):
        # process the input array
        r = len(A)
        c = len(A[0])

        for row in range(1, r):
            for col in range(c):
                if A[row][col]:
                    A[row][col] += A[row - 1][col]

        ret = 0

        for row in range(r):
            area = self.area(A[row])
            ret = max(ret, area)

        return ret

        # TC: O(rows * cols); SC: O(cols) 