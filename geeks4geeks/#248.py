# question --> https://practice.geeksforgeeks.org/problems/smallest-number-repeating-k-times3239/1/?page=1&difficulty[]=-1&status[]=unsolved&category[]=Hash&sortBy=submissions#

from collections import Counter


class Solution:
    def findDuplicate(self, arr, N, K):
        ans = float('inf')
        lkp = Counter(arr)

        for ind, ele in enumerate(arr):
            if lkp.get(ele) == K:
                ans = min(ans, ele)

        return ans if ans != float('inf') else -1

    # TC: O(N); SC: O(N)