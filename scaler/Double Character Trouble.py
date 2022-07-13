class Solution:
    # @param A : string
    # @return a strings
    def __init__(self):
        self.stack = ['#']

    def solve(self, A):
        n = len(A)

        for ind, ele in enumerate(A):
            if self.stack[-1] != ele:
                self.stack.append(ele)
            else:
                self.stack.pop()

        return ''.join(self.stack)[1:]

    # TC: O(N); SC: O(N)