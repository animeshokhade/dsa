import sys

sys.setrecursionlimit(10 ** 6)


class Solution:
    # @param A : integer
    # @return a list of list of integers
    def recursion(self, A, source, destination):
        temp = [A, source, destination]
        if A == 1:
            self.ans.append(temp)
            return

        self.recursion(A - 1, source, 6 - source - destination)
        self.ans.append(temp)
        self.recursion(A - 1, 6 - source - destination, destination)

    def towerOfHanoi(self, A):
        self.ans = []
        self.recursion(A, 1, 3)
        return self.ans

