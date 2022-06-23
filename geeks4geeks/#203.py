# question --> https://practice.geeksforgeeks.org/problems/balanced-array07200720/1/?page=2&difficulty[]=-1&status[]=unsolved&sortBy=submissions

class Solution:
    def minValueToBalance(self,a,n):
        #code here.
        l, r = 0, 0
        m = n // 2
        
        for ind, ele in enumerate(a):
            if ind < m: 
                l += ele
            else: 
                r += ele 
                
        return abs(l - r)
        
        # TC: O(N); SC: O(1)