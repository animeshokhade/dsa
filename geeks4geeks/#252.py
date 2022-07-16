# question --> https://practice.geeksforgeeks.org/problems/index-of-first-1-in-a-sorted-array-of-0s-and-1s4048/1?page=2&difficulty[]=-1&status[]=unsolved&sortBy=submissions

from bisect import bisect_left


class Solution:
    def firstIndex(self, arr, n):
        # Your code goes here
        ind = bisect_left(arr, 1)
        return ind if ind < n else -1

        # TC: O(logN); SC: O(1)