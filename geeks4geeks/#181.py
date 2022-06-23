# question --> https://practice.geeksforgeeks.org/problems/middle-of-three2926/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

class Solution:
    def middle(self,A,B,C):
        #code here
        ma = max(A, B, C)
        mi = min(A, B, C)
        
        if A != ma and A != mi: 
            return A
        if B != ma and B != mi: 
            return B
        
        return C 
        
    # TC: O(1); SC: O(1)