# question --> https://practice.geeksforgeeks.org/problems/factorial5739/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

class Solution:
    def factorial (self, N):
        # code here
        fac = 1
        while N:
            fac *= N
            N -= 1
            
        return fac
        
        # TC: O(N); SC: O(1)