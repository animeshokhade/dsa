# question --> https://practice.geeksforgeeks.org/problems/print-the-left-element2009/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def leftElement(self, arr, n):
        # Your code goes here
        arr.sort()
        if n & 1:
            return arr[n // 2]
        return arr[n // 2 - 1]

    # TC: O(NlogN); SC: O(1)
