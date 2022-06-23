# question --> https://practice.geeksforgeeks.org/problems/last-index-of-15847/1/?page=3&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

class Solution:
    def lastIndex(self, s):
        # code here
        n = len(s)
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                return i
        return -1
        
        # TC: O(|S|); SC: O(1)