# question --> https://practice.geeksforgeeks.org/problems/find-unique-element2632/1/?page=1&difficulty[]=-1&status[]=unsolved&category[]=Hash&sortBy=submissions#

from collections import Counter


class Solution:
    def findUnique(self, a, n, k):
        # Code here
        freq = Counter(a)
        for ele in freq:
            if freq[ele] % k:
                return ele

    # TC: O(Number of Distinct Elements); SC: O(N)