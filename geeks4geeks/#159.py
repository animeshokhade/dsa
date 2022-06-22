# question --> https://practice.geeksforgeeks.org/problems/who-will-win-1587115621/1/?page=4&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions#

class Solution:
    ##Complete this function
    def searchInSorted(self, arr, N, K):
        # Your code here
        lo, hi = 0, N - 1
        while lo <= hi:
            mi = (lo + hi) // 2

            if arr[mi] == K:
                return 1
            elif arr[mi] < K:
                lo = mi + 1
            else:
                hi = mi - 1

        return -1

        # TC: O(logN); SC: O(1)
