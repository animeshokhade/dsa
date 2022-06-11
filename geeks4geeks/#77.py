# question --> https://practice.geeksforgeeks.org/problems/check-string1818/1/?page=2&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def check (self,s):
        # your code here
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                return 0
        return 1

    # TC: O(|s|); SC: O(1) 