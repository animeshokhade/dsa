class Solution:
    # @param A : list of integers
    # @return an integer
    def xor(self, A):
        stack = []
        xor = 0

        for a in A:
            while stack and stack[-1] <= a:
                stack.pop()
            if stack:
                xor = max(xor, a ^ stack[-1])
            stack.append(a)

        return xor

    def solve(self, A):
        l = self.xor(A)
        A.reverse()
        r = self.xor(A)

        return max(l, r)

        # TC: O(N); SC: O(N) 