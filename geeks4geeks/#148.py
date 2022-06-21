# question --> https://practice.geeksforgeeks.org/problems/anagram-1587115620/1/?page=2&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions#

from collections import Counter


class Solution:

    # Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self, a, b):
        # code here
        A = Counter(a)
        B = Counter(b)

        for key in B:
            if A[key] != B[key]:
                return 0
        return 1

    # TC: O(|B|); SC: O(|A| + |B|)
