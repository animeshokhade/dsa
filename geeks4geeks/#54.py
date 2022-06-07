# question --> https://practice.geeksforgeeks.org/problems/print-table0303/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def getTable(self,N):
        # code here
        ans = []
        for index in range(1, 11):
            ans.append(N * index)
        return ans

    # TC: O(1); SC: O(1)
    