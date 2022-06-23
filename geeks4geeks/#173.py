# question --> https://practice.geeksforgeeks.org/problems/count-squares3649/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

class Solution:
    def countSquares(self, N):
        # code here 
        sqr = 0
        if N == 1: return sqr
        
        lo, hi = 1, N
        while lo <= hi: 
            mi = (lo + hi) // 2
            sq = mi * mi
            if sq < N: 
                lo = mi + 1
                sqr = mi
            else:
                hi = mi - 1
        return sqr
        
        # TC: O(logN); SC: O(1)