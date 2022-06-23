# question --> https://practice.geeksforgeeks.org/problems/check-if-a-string-is-isogram-or-not-1587115620/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

class Solution:
    
    #Function to check if a string is Isogram or not.
    def isIsogram(self,s):
        #Your code here
        return len(set(s)) == len(s)
        
        # TC: O(1); SC: O(|S|)