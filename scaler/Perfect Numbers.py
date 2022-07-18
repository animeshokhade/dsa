from collections import deque


class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, A):
        q = deque()

        q.append(1)
        q.append(2)

        ans = ''

        while A:
            val = q.popleft()
            ans = str(val) + str(val)[::-1]

            for i in range(1, 3):
                q.append(val * 10 + i)

            A -= 1

        return ans

        # TC: O(A); SC: O(A)  