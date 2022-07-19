from collections import Counter, deque


class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        ans = ''
        dic = Counter()
        q = deque()

        for ch in A:
            dic[ch] += 1
            if dic[ch] == 1:
                q.append(ch)
            while q and dic[q[0]] != 1:
                q.popleft()
            ans += q[0] if q else '#'

        return ans

        # TC: O(N + Distinct characters); SC: O(K) 