# question --> https://practice.geeksforgeeks.org/problems/change-the-string3541/1/?page=1&difficulty[]=-1&status[]=unsolved&category[]=Strings&sortBy=submissions#

class Solution:
    def modify(self, s):
        # code here
        if s[0].islower():
            return s.lower()
        else:
            return s.upper()

    # TC: O(|s|); SC: O(|s|) 
