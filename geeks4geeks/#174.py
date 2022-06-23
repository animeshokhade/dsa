# question --> https://practice.geeksforgeeks.org/problems/maximize-arrii-of-an-array0026/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

class Solution:
    def Maximize(self, a, n): 
        # Complete the function
        a.sort()
        max_sum = 0 
        mod = pow(10, 9) + 7
        
        for ind, ele in enumerate(a):
            max_sum += ind * ele
            max_sum %= mod
            
        return max_sum % mod 
        
        # TC: O(NlogN); SC: O(1)