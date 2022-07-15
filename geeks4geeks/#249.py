# question --> https://practice.geeksforgeeks.org/problems/check-arithmetic-progression1842/1/?page=1&difficulty[]=-1&status[]=unsolved&category[]=Hash&sortBy=submissions#

class Solution:

    def checkIsAP(self, arr, n):
        # code here
        arr.sort()
        d = arr[1] - arr[0]

        for ind in range(2, n):
            if d != arr[ind] - arr[ind - 1]:
                return False

        return True

        # TC: O(NlogN); SC: O(1)