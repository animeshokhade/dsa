# question --> https://practice.geeksforgeeks.org/problems/find-position-of-set-bit3706/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

class Solution:
    def findPosition(self, N):
        # code here 
        if N == 0: return -1
        pos = 0
        ret = None
        
        while N: 
            pos += 1
            if N & 1: 
                ret = pos
                N >>= 1
                break
            N >>= 1
            
        if N: 
            return -1
            
        return ret 
        
        # TC: O(logN); SC: O(1)