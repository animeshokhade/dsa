from collections import deque


class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):
        ans = []
        q = deque()

        for _ in range(1, 4):
            q.append(_)

        while A:
            val = q.popleft()
            ans.append(val)

            for _ in range(1, 4):
                q.append((val * 10) + _)
            A -= 1

        return ans

    # TC: O(N); SC: O(N) 