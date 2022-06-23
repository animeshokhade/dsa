# question --> https://practice.geeksforgeeks.org/problems/number-is-sparse-or-not-1587115620/1/?page=2&difficulty[]=-1&status[]=unsolved&sortBy=submissions

class Solution:
    
    #Function to check if the number is sparse or not.
    def isSparse(self,n):
        #Your code here 
        while n: 
            if n & 1: 
                n >>= 1
                if n & 1: 
                    return False
            n >>= 1
        return True 

    # TC: O(logN); SC: O(1)