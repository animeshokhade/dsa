# question --> https://practice.geeksforgeeks.org/problems/sum-of-numbers-in-string-1587115621/1/?page=2&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

class Solution:
    
    #Function to calculate sum of all numbers present in a string.
    def findSum(self,s):
        #code here
        summ = 0
        ind = 0
        n = len(s)
        while ind < n: 
            tmp = ''
            while ind < n and s[ind].isdigit(): 
                tmp += s[ind]
                ind += 1
            if tmp: 
                summ += int(tmp)
            ind += 1
                
        return summ 
        
        # TC: O(N); SC: O(N)