# question --> https://practice.geeksforgeeks.org/problems/red-or-green5711/1/?page=2&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

from collections import Counter


class Solution:
    def RedOrGreen(self, N, S):
        # code here
        col = Counter(S)
        if len(col) == 1: return 0
        p = min(col, key=lambda x: col[x])
        return col.get(p)

        # TC: O(N); SC: O(1)