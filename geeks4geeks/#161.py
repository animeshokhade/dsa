# question --> https://practice.geeksforgeeks.org/problems/key-pair5616/1/?page=4&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions#

class Solution:
    def hasArrayTwoCandidates(self, arr, n, x):
        # code here
        lkp = set()
        for a in arr:
            if x - a in lkp:
                return 1
            lkp.add(a)
        return 0
        # TC: O(N); SC: O(N)
