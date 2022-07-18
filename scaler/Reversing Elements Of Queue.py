from collections import deque

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        A = deque(A)
        q = deque()

        for _ in range(B):
            q.append(A.popleft())

        for _ in range(B):
            A.appendleft(q.popleft())

        return A

    # TC: O(A); SC: O(A) 