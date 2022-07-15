class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        stack = []
        n = len(A)
        G = [-1] * n

        for ind in range(n - 1, -1, -1):
            while stack and A[ind] >= stack[-1]:
                stack.pop()

            if stack: G[ind] = stack[-1]

            stack.append(A[ind])

        return G

        # TC: O(N); SC: O(N) 